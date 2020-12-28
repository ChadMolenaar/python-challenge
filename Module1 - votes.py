Attribute VB_Name = "Module1"
Sub stock_counter():
    
    Dim lastRow As Long
    Dim start As Long
    Dim openingValue As Double
    Dim closingValue As Double
    Dim ticker As String
    Dim totalVolume As Double
    Dim YearlyChange As Double
    Dim PercentChange As Double
    
    
    Range("I1").Value = "Ticker"
    Range("J1").Value = "Opening Price"
    Range("K1").Value = "Closing Price"
    Range("L1").Value = "Yearly Change"
    Range("M1").Value = "Percentage Change"
    Range("N1").Value = "Total Volume"
    
        lastRow = Cells(Rows.Count, "A").End(xlUp).Row
    
        start = 2
        nr = 0
        totalVolume = 0
       
    For Row = 2 To lastRow:
    
        totalVolume = totalVolume + Cells(Row, 7).Value
       
    If Cells(Row, 1).Value <> Cells(Row + 1, 1).Value Then
    
        ticker = Cells(start, 1).Value
   
        Range("I" & 2 + nr).Value = ticker
    
        openingValue = Cells(start, 3).Value
        Range("J" & 2 + nr).Value = openingValue
    
        closingValue = Cells(Row, 6).Value
    
        Range("K" & 2 + nr).Value = closingValue
    
        YearlyChange = closingValue - openingValue
        start = Row + 1
        Range("L" & 2 + nr).Value = YearlyChange
        
        Range("N" & 2 + nr).Value = totalVolume
        
        totalVolume = 0
            
        Range("M" & 2 + nr).Value = start
    
    If openingValue > 0 Then
        PercentChange = YearlyChange / openingValue
        Range("M" & 2 + nr).Value = PercentChange
    
    Else
        PercentageChange = -1
                      
    End If
        
        nr = nr + 1
        
        End If
    
   
    Next Row

   
End Sub


