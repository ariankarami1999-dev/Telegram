<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/Zfgx4fYUmAajDKAL8UNuYT2eUzK1wS-ss0J36oaGbCIrlr4wbXXlCr86x33b4OX9SeXMVaqOB1IPIGFz8gg195xqiubt2fuVcgOj3za55x6IF469hB-3mp7iUSOF82c-rxTxZ362qTXhIT92WyFt1iqaggBl50wtjXbQYtFp8oFueThxMocL52Lee02_1qj4n0-6wk2dHZQhkYaq1kL5LtwT_fbwIQIO_iGiwCQ_qobpNdVxvdVWaN-_DwBDbQ1u7QHvDRoYfw7GgKhNtt4J5Y_lcoi0sa6LqnMp86OeQN3x77cneuTFTC0PrzvnKflASXBJqoTyxR0-19QLEOMeNw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 White DNS</h1>
<p>@whitedns • 👥 71.3K عضو</p>
<a href="https://t.me/whitedns" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-26 00:08:19</div>
<hr>

<div class="tg-post" id="msg-643">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(ÐΛɌ₭ᑎΞ𐒡𐒡)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=kMYjByWhztJfFSAmUxi65TuLu69erhgsraAwncg-u-zVG3K25O2AW0JZz9vaduhQTbWhQFX2aBaVvUxM_W_5Lk9ldRvC1uFUTpbMmDctA0qH35o9sO2b799tMErUfY6oJXk7QdkrXIhGP0IKCX9ajm5zvt7tANz-LCSrdaO38nYpx7MZ3klDUjGkcccLRLtaxZiWDNJB5K32LMABvd-Izowl7_54mKkhWppS4dL5qbDSQiRkdpXWdOcE4mu4K9vpRqZFc5ut6KFUzJQjkJkX2KiteyhXnPB9Nt2jPna0b-uvDKbDf8gGrsxpmtkkypzdVyLY28CZrG_TlxojA7CKIHIq5LaLdAlVlOS-Ub62qdxN4NjRP0vWcByRsOf-LndZTz1zDkTX4l7tdf1pwqj7hsMhgwkRrIMdQ65iHgAcFlRrvEliOWogW400khNYcsYOEYF4lCPtPvEzudzXxriN-yiI5bFZTC0ny8uBX1frhhzxrjRETFUwHo2152EaGpF7r_jC8wbxLNuyGi3zv1f9Sapbr31XkLRuRugxi0gjDXvrBhHzoAdliG0GeMWLgZWVdrZ8l4bdOsi_BUAhJ22nHhy6yZpFX-axE6AXOQub6sSA4pQNOIsqAyUTGDuZNGCw8NykNVYacFeey_4udy9SE3zojHrPrgEhh2mu4a7cpL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77e656a8.mp4?token=kMYjByWhztJfFSAmUxi65TuLu69erhgsraAwncg-u-zVG3K25O2AW0JZz9vaduhQTbWhQFX2aBaVvUxM_W_5Lk9ldRvC1uFUTpbMmDctA0qH35o9sO2b799tMErUfY6oJXk7QdkrXIhGP0IKCX9ajm5zvt7tANz-LCSrdaO38nYpx7MZ3klDUjGkcccLRLtaxZiWDNJB5K32LMABvd-Izowl7_54mKkhWppS4dL5qbDSQiRkdpXWdOcE4mu4K9vpRqZFc5ut6KFUzJQjkJkX2KiteyhXnPB9Nt2jPna0b-uvDKbDf8gGrsxpmtkkypzdVyLY28CZrG_TlxojA7CKIHIq5LaLdAlVlOS-Ub62qdxN4NjRP0vWcByRsOf-LndZTz1zDkTX4l7tdf1pwqj7hsMhgwkRrIMdQ65iHgAcFlRrvEliOWogW400khNYcsYOEYF4lCPtPvEzudzXxriN-yiI5bFZTC0ny8uBX1frhhzxrjRETFUwHo2152EaGpF7r_jC8wbxLNuyGi3zv1f9Sapbr31XkLRuRugxi0gjDXvrBhHzoAdliG0GeMWLgZWVdrZ8l4bdOsi_BUAhJ22nHhy6yZpFX-axE6AXOQub6sSA4pQNOIsqAyUTGDuZNGCw8NykNVYacFeey_4udy9SE3zojHrPrgEhh2mu4a7cpL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
دور زدن فیلترینگ با کانفیگ سرورلس با ترکیب nekobox و v2rayng
•
✅
لینک کانفیگ nekobox
•
https://pastebin.com/raw/rWeHKSt3
•
✅
لینک داخلی کانفیگ nekobox
•
https://seup.shop/t/exks1
•
✅
لینک کانفیگ V2rayNg
•
https://pastebin.com/raw/Yfymhyy5
•
✅
لینک داخلی کانفیگ‌ V2rayNg
•
https://seup.shop/t/k9mmj
❗️
هر دو کلاینت رو، رو حالتvpnبزارید .
📥
لینک داخلی ویدیوها
•
🎥
https://seup.shop/f/uns5
•
🎥
https://seup.shop/f/v4jx
•
𝕏 Irvictorious
kian
•
@ConfigWireguard
💎
•
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/whitedns/643" target="_blank">📅 19:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-642">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">White DNS
pinned «
💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/642" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-641">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">💥
💥
💥
💥
💥
💥
💥
برای تبادل نظر و همگرایی در گروه ما عوض شوید
🔄
👥
@whitedns_group
🌐</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/whitedns/641" target="_blank">📅 19:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-639">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">لیست ۱۰۰ ریزالور که طول ۲۴ ساعت گذشته به سرور های WhiteDNS وصل شدند
185.94.98.34
2.189.44.68
185.44.36.216
185.137.25.146
94.232.173.28
185.142.158.162
217.219.162.200
185.88.178.196
178.252.143.130
134.255.206.206
80.75.7.2
134.255.206.205
185.53.142.174
89.32.197.226
185.37.55.30
77.238.111.234
31.214.169.244
80.71.149.62
185.109.61.27
62.60.197.83
185.88.178.177
178.252.128.66
158.58.184.147
5.202.252.30
74.63.24.205
74.63.24.211
216.147.121.134
74.63.24.210
46.209.209.209
217.66.203.211
74.80.77.246
80.191.221.26
2.189.44.98
216.147.121.98
164.138.17.122
207.211.215.145
151.232.36.4
185.208.175.228
2.188.21.58
108.162.192.0
172.64.32.0
80.191.163.249
173.245.58.0
78.39.234.140
185.208.183.29
2.188.21.138
2.188.21.70
2.188.21.46
185.255.91.60
66.185.123.243
2.189.44.85
2.189.44.82
2.189.44.83
2.189.44.86
2.189.44.84
2.189.44.14
74.80.77.247
109.107.159.45
2.189.44.92
2.189.44.94
2.189.44.91
2.189.44.93
2.189.44.90
78.157.41.60
193.178.200.3
46.32.31.30
185.208.174.167
85.185.157.181
77.238.123.179
185.141.105.139
5.160.140.16
5.160.227.78
185.53.141.230
185.105.101.1
37.255.223.218
85.133.129.242
78.38.174.2
37.191.95.70
74.80.77.244
74.80.77.245
93.118.109.213
194.61.120.143
121.127.46.65
93.126.5.205
5.160.137.130
2.180.21.241
82.114.164.226
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/whitedns/639" target="_blank">📅 16:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سرور اهدایی از رسول عزیز از تیم وایت دی ان اس
Name: H3 (Germany)
Domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Serbia
Domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Turkey
Domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: USA
Domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: Switzerland
Domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
Name: RMFT g1-7
Domain:
g1-7.rmft.tech
Encryption Key:
a337e9fa75161c44bebe7d717da36afc</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/636" target="_blank">📅 12:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرور اهدایی از چنل
@Masir_Sefid
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
Name:
@Masir_Sefid
🕊
(1)
Domain:
v1.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(2)
Domain:
v2.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(3)
Domain:
v3.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Name:
@Masir_Sefid
🕊
(4)
Domain:
v4.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor
Name:
@Masir_Sefid
🕊
(5)
Domain:
v5.masir-sefid-1.shop
Encryption Key:
Telegram-Channel--->@Masir_Sefid
Encryption Method: xor</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/whitedns/635" target="_blank">📅 12:36 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-633">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/whitedns/633" target="_blank">📅 12:23 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-631">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F-0ggytAg84IDdO4uVoJrsFBIy8LPsWoI2XbR1ZxUAD2ZUqInGNvsCZJaRyej1lXLFeID1in2opHWwQQmr-UO-NIGIxHfSCh3oPsX7t8pmK36sL5v9gm8kWKvGGUciNbPslxkk4FhtJn3Vf-MXRr9Cbm6CsjuQmEKKpH884XbDjZFxzjolyR5AqtIKrGOfLsUglGhF00b-vicUH5bSsdoveMeCXje0F0WjiDDnhLJPDZriptpn2wZSVMukhkUmLwkQJxnI_LFJ7iHuFu3Ck6C02o0oFY_C7_mEv_GwUJ_if0S8uzSnXWwvOAw7ToOJRKN6A_i5xtigVatetNO2jrUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMJSeQ6RkmhZlZ_XMieewHT4VDMDXHFMHHWhzmTAIhBDPCDtjJQ7jxD5WAXGxevEI722Wb-f3bh8Lm6blfKG4VI1krkjKYM-j4gZvei6Eck_0BIr17sunnOrXP7Gim9-h7oOlOhSVSZMYIX3PeM0goTiC2thDy7Y8Tj6_FcyLM7jZ5Rci2czfC-QbWVpJoZm1tFTPfVZezFLpGi0g4Wao7YEM2nrcIoZObyexuj3kboLH3ve08a0TXxTJdjQgpZwWktwap7b1RkrnbzgwGsz8dWmPiHqN53WMjF8fU6OTzfcygxk9XGvIg4PNgOkNYTapJutdJ8ly5NPo_XnNj61wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">درحال حاضر نزدیک ۱۰۰۰ نفر فقط به سرور ما متصل هستند. سرور تا نزدیک ۲۴۰۰ نفر میتونه کاربر بدون افت کیفیت رو پشتیبانی کنه.
جدا از سرور های ما، سرور های اهدایی باقی چنل ها مثل مسیر سفید هم هست. ویدیو آموزش سرور اختصاصی هم پست های بالاتر گذاشتیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/whitedns/631" target="_blank">📅 11:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-630">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=JGBzOF8IezEZoIYR2bXU079jqYmzkTCOmpMQvlLj3KWAzjB7zlTwrOjtmqj93mYpSxgBsHpASdcMcrGsJjCuTJ9F-g1qV0d3HSf3UsAu7qtBQLVew6O-6G8gQB2RWZjKkoiw8t0art2HTT4t5KpFbsSbMg3HAFT0J_H6dFub_PzRsDm1YlL_jvjmIDORLaWrXuC19HZDtxiubcr96o8Hv5wsnmmXcSO8U-EtWPMWP4T0zsarGX-gW0A4NyEL05wLkQNIG55sdOtuflWWqMt9wXbk7OwXcNs-nhKHdSVE0-2n8UkjsxqVy7TcDSNMSPL0eas9EP-PB68j-u47LwPHWw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f406ca77b7.mp4?token=JGBzOF8IezEZoIYR2bXU079jqYmzkTCOmpMQvlLj3KWAzjB7zlTwrOjtmqj93mYpSxgBsHpASdcMcrGsJjCuTJ9F-g1qV0d3HSf3UsAu7qtBQLVew6O-6G8gQB2RWZjKkoiw8t0art2HTT4t5KpFbsSbMg3HAFT0J_H6dFub_PzRsDm1YlL_jvjmIDORLaWrXuC19HZDtxiubcr96o8Hv5wsnmmXcSO8U-EtWPMWP4T0zsarGX-gW0A4NyEL05wLkQNIG55sdOtuflWWqMt9wXbk7OwXcNs-nhKHdSVE0-2n8UkjsxqVy7TcDSNMSPL0eas9EP-PB68j-u47LwPHWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.site
Encryption Key:
bad99364093861634030e96f11fe3132
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/whitedns/630" target="_blank">📅 11:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.4.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/625" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان  نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/whitedns/625" target="_blank">📅 11:05 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nNuiFKqN2hJ8wJCYa9-iPH8caK0NqtWY5UcU17viVqflqJJPl34ygeRfYRK4wQYq24j9C_HMhQtOl09rOlHOCy4PePS81gxtHSf-EWZSoHtHFeAHJ-hbQmU6qf5QGEPTsay9zopwppt_xhrZepol9PfwChMPup2PxR3o8uZAxPwnsQENxSzORdt9_GzMF-6fx43jDXzpZKWdcrIiwX7xOvxAITivQEERPkdy1ZuCZsa1Xai56HGMVV2MRxmBxsBkLxyUpivJXtDKTl4kdcCVbi6numNGCOkIIS4s_NLgbW1GhCioZ_Uri7mLcRfxIvp7p9YznoGmcVy8v3Z01Lz6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
🤖
دانلود نسخه یونیورسال از سرور های داخلی
🔴
ویدیو آموزشی استفاده از اپلیکیشن
🔴
گروه اصلی شمامل تاپیک ریزالور، سوال های متداول، آموزش و ریزالور
تمرکز اصلی این نسخه روی ساده‌تر شدن اتصال و پیدا کردن بهترین تنظیم برای هر کاربر بوده است. هدف این بود که WhiteDNS قبل از اتصال، چند کانفیگ مختلف را با Parallel Test بررسی کند، بهترین گزینه را از نظر سرعت و کیفیت انتخاب کند، و کاربران بدون نیاز به گشتن دنبال Resolver، با لیست پیش‌فرض ۴۵۰۰+ Resolver داخل اپ سریع‌تر اسکن کنند و راحت‌تر وصل شوند.
تغییرات این نسخه
:
✅
نسخه اپلیکیشن به 1.4.0 ارتقا پیدا کرده
✅
قابلیت Parallel Test برای تست هم‌زمان چند تنظیم مختلف قبل از اتصال اضافه شده
✅
حالا WhiteDNS می‌تواند قبل از اتصال، چند حالت اتصال را هم‌زمان بررسی کند
✅
اپ سرعت و Ping هر تنظیم را تست می‌کند و بهترین گزینه را برای همان اتصال انتخاب می‌کند
✅
قابلیت Parallel Test هم برای Proxy Mode و هم برای Full VPN قابل استفاده است
✅
در حالت Full VPN، اپ اول بهترین تنظیم را با Parallel Test پیدا می‌کند و بعد اتصال VPN نهایی را روشن می‌کند
✅
نتایج Parallel Test بعد از اتصال داخل صفحه اصلی نمایش داده می‌شود
✅
می‌توانید تنظیم موفق Parallel Test را با نام دلخواه ذخیره کنید
✅
چند تنظیم آماده WhiteDNS برای تست سریع اضافه شده
✅
می‌توانید پروفایل‌های تنظیمات پیشرفته خودتان را هم وارد Parallel Test کنید
✅
بیش از 4500 Resolver داخل اپ قرار گرفته تا برای اسکن و اتصال راحت‌تر استفاده شود
✅
لیست Resolver پیش‌فرض داخل اپ کامل‌تر شده
✅
پروفایل Default Resolver اضافه شده تا اپ همیشه یک لیست آماده Resolver داشته باشد
✅
امکان اسکن مستقیم لیست Resolver پیش‌فرض اضافه شده
✅
اسکن فایل‌های بزرگ Resolver سبک‌تر و بهتر انجام می‌شود
✅
ریزالورهای تکراری یا قبلاً پیدا‌شده بهتر کنار گذاشته می‌شوند
✅
شمارش Resolverهای سالم و ردشده در اسکن دقیق‌تر شده
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر جلوی شروع اسکن را می‌گیرد
✅
ویرایش سرور، Resolver و تنظیمات از صفحه اصلی راحت‌تر شده
✅
امکان حذف پروفایل‌های اتصال تکراری اضافه شده
✅
پروفایل Default Resolver از حذف یا جابه‌جایی اشتباهی محافظت می‌شود
✅
هشدار باتری حالا قابل بستن است
✅
نمایش سرعت، مصرف اینترنت و آمار اتصال دقیق‌تر شده
✅
تنظیمات پیشرفته برای اتصال‌های کندتر و مسیرهای سنگین‌تر بهتر تنظیم شده
✅
وارد کردن و خروجی گرفتن فایل‌های TOML با گزینه‌های جدید کامل‌تر شده
✅
هسته داخلی StormDNS به‌روزرسانی شده
تنظیماتی که به صورت اتوماتیک انتخاب میشوند، تمرکز روی سرعت و کیفیت دارد. امکان افزایش مصرف اینترنت شما با کانفیگ انتخاب شده می‌باشد. اگر نگران این موضوع هستید تنظیمات را مرور کرده و مقدار  Upload Dup را کمتر کنید.
⚠️
⚠️
⚠️
⚠️
⚠️
حجم کپی از کانال ما واقعاً باورنکردنیه؛ در حدی که آدم شک می‌کنه شاید ما ناخواسته برای بعضی دوستان واحد تولید محتوا راه انداختیم.
کمترین کاری که می‌تونید انجام بدید، انتشار همین پست یا حداقل ذکر منبع کانال ماست. باور کنید نوشتن منبع، اینترنت رو خراب نمی‌کنه و از اعتبار شما هم کم نمی‌کنه.
همراهان عزیز WhiteDNS،
اگر دیدید کانالی بدون ذکر منبع مطالب ما رو کپی کرده، لطفاً با احترام منبع اصلی رو بهشون یادآوری کنید. شاید فقط فراموش کردن؛ کپی‌کردن زیاد آدم رو خسته می‌کنه.
@WhiteDNS</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/whitedns/624" target="_blank">📅 11:03 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf7H8Ivu4JlK_PcEKi86ZI5EgKoZN9ZWatAHU--yiZHTznOZLVIe5LCx19mDUw7ptB-MyA4SUx-H77Q_PD744bJ6KKQ7O_95wisHH9u3d8hYDnmP09XU-3ZM_ZobdCwZtaqcTtY4bdBTjKnXZINt7EKJxWAYiuUMpBgmsusrLDd80wIwFwa_4CrqO95VlmIeJeoOd5Lxw4P7CcVCOPaKlX2jD20UZWqrlmzH-aztoPh2hmZ_8A1Y4VLw8nNihtAlv6awQFTUQi2_gFjKP_ltgvx1bqRabhkjUqpt1emdbNggqg1Iwt2RBSb_B99ihy9lEAHfmNXSCwzRvw5i6UbpAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن ۱.۴.۰ کلاینت اندروید WhiteDNS به‌زودی منتشر می‌شود. در این نسخه سعی کردیم کار شما را راحت‌تر کنیم و اتصال سریع‌تر و ساده‌تر انجام شود.
در این ورژن، اپ به‌صورت خودکار ۷ تنظیم مختلف را با قابلیت Parallel Test بررسی می‌کند و در نهایت بهترین کانفیگ را از نظر سرعت و کیفیت برای شما انتخاب می‌کند.
همچنین بیش از ۴۵۰۰ Resolver که قبلاً داخل بات و گروه منتشر شده بود، به‌عنوان لیست پیش‌فرض داخل اپ قرار گرفته است تا بدون نیاز به گشتن دنبال لیست، بتوانید مستقیم اسکن را شروع کنید و راحت‌تر وصل شوید.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/whitedns/623" target="_blank">📅 10:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pwWgpl-5kPURtE-KmF6FmceZmqEcfjl5-kmvsKfLf8gsGUSC3Ni8DC9CBk4fDbsArtNuWpxNHIm5yrbYFHcHSh-UzNpxH-Vd74Zr_FLve8X1WrKxW7NZSvoyCTDxPzK6paJyz0yu8cGJrQHsxi3nnA0jjNXTxO9EAGfZgVzmq5AT7anCMjtigK1fYoLiZ4_G7GNvjpbjMl5_in2ihRC5jmm4Q9d2r7cybXG5jndgUjDf8I2LUY5L_JEB0ZM7eMDygFjBmJRhZBQXM4gI5F-FRHYPzngYCfa4gQeryUZrtNap75FIIbG9O2-N_6K7S06L43f4-yrWnoAeQLmiOV7_2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/whitedns/622" target="_blank">📅 07:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">StormDNS-Setup-Guide.mp4</div>
  <div class="tg-doc-extra">151.4 MB</div>
</div>
<a href="https://t.me/whitedns/620" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دوستان عزیز سلام
یک فیلم آموزشی آماده کردم برای نحوه راه‌اندازی سرور شخصی StormDNS/MasterDNS
دانلود سرور داخلی
https://guardts.ir/f/3c4216b2ea16
✍️
آموزش متنی
پیش‌نیاز:‌ تهیه سرور و دامنه خارج از ایران
1️⃣
آماده‌سازی DNS
ابتدا یک ساب‌دامین کوتاه بسازید و آن را به نیم‌سروری وصل کنید که به IP سرور شما اشاره می‌کند.
مثال:
ns.example.com  A   1.2.3.4
v.example.com   NS  ns.example.com
توضیح:
ns.example.com
باید به IP سرور شما وصل باشد.
v.example.com
باید به عنوان Subdomain Delegation به
ns.example.com
اشاره کند.
یعنی تمام درخواست‌های DNS مربوط به
v.example.com
به سرور شما ارسال می‌شود. اینترنت هم بالاخره یک جایی باید بفهمد با خودش چند چند است.
2️⃣
نصب سرور
روی سرور لینوکسی خود، دستور زیر را اجرا کنید:
bash <(curl -Ls https://raw.githubusercontent.com/nullroute1970/StormDNS/main/server_linux_install.sh)
بعد از نصب و اجرای سرور، برنامه به صورت خودکار کلید رمزنگاری فعال را نمایش می‌دهد.
همچنین این کلید داخل فایل زیر ذخیره می‌شود:
encrypt_key.txt
برای مشاهده کلید می‌توانید از دستور زیر استفاده کنید:
cat encrypt_key.txt
3️⃣
موارد موردنیاز برای اتصال کلاینت
بعد از راه‌اندازی، برای ساخت پروفایل یا اتصال کلاینت معمولاً به این اطلاعات نیاز دارید:
Domain: v.example.com
Encryption Key: مقدار داخل encrypt_key.txt
Server IP: 1.2.3.4
لینک داخلی:
https://guardts.ir/f/3c4216b2ea16
@WhiteDNS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/620" target="_blank">📅 03:18 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nKxdZY10r6KW4AhHifyQV6P0_Oh3k9dYPTsfWetJRo2lL7hK4QGeJbBYfo3FcHu2_g7n3pw_Bei_3MN3KNm556u7PBRKm8-FZqgqEsNrJy9ONk6f2Nun21mhRIkve9GOPbekCC67PM68vkSv5Cr-fxQmIxcoqYqFFjI_LqAxTqAShSli3hzL4GwDsMpfChWOckMWMtS24zGwSWedTIwuMeh0cljSCPCNHZSTQ7zl8raj3Ft6lISOelsk4dirRIGb9Auoim4oPsUyYm1Tr8yA1AzICotW1s-sHD4YfoqzEkhU-F1srJTYKo63ycTQLspUZxTZjiKLAQJpoeI7nXo6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ql9if0Q1kxCjFYBsN-7O4kulHjXMJh-6iGBfkHlswL6ZquurHOgYRMWxehqVMsDdC4FhegS_fd9fAPFWj99tDk0wEwH0NN6n4HtHvfkA1VQpQ-sMwQxU08o-r1o5DiFsFIaIWtqRYv_aCA1Thg8v6gtXf_hEk7L1-4fnirQwoBSihy6wcjHnslCdYaOgeBdjRJLry9sa3y48Fs-7vygLn9AB4xZ4-NNQr1T5CNJ2JZdbIrGKZgds5IFkajRN9wHR7JN9axJ39U09Cl0ytZbYrC918nVD_ukA1xvQqC5CdQkZyIKNWxtZLk_Z6LlFXXtocnC7-Ig7LQowF59yQO7UVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داخل پروژه
TheFeed
که متعلق به
Sarto
عزیز هست یک فیچر برای ریزالورها وجود دارد. یک
جدول امتیازدهی برای ریزالورها
درست شده و بازخورد خوبی از سوی کاربران داشته بخاطر اینکه وضعیت ریزالورهای داخل جدول به طور واضح مشخص شده است.
همچنین خود برنامه به صورت رندوم از ریزالورهایی استفاده میکند که امتیاز بیشتری دارند تا کیفیت اتصال ریزالورها به
حداکثر
برسد.
متاسفانه اکانت گیتهاب
Sarto
ساسپند شده اما میتونید برای دریافت برنامه‌ی
TheFeed
به لینک زیر که پست کانال خود
Sarto
هست مراجعه کنید و ازش
حمایت
کنید:
لینک پست
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/617" target="_blank">📅 00:22 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
آموزش خیلی مقدماتی و ساده برای استفاده از این نسخه
@whitedns</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/whitedns/616" target="_blank">📅 18:35 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">6.8 MB</div>
</div>
<a href="https://t.me/whitedns/615" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">Whitedns windows v1.0.2</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/whitedns/615" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/rRn-XfMbBjTlyei-FhvBJNpP_kw2kOdscXfqQGinofky2uWsHQSQs3iJNKrEHBnv_mpScftVKoxQsLL2R3zM5Ce-t-QIfLOj8v-TXDB1JggKMPTSvz4VaxmC8UUQgJLf8pJCAYKYDyKtRGytP7PaRF5yonyCSWliYCz_xwo9Yjuq4V3Y3umYCZ8MgMfWkkIkdr9Z_1ETXrfIlyeMdVA_KvIQqivyFk9kD9PxUlAh7JPkU8M6P_g0vatnd4IycaTcssqHr_3EyihwqteJeih5I8aSS68tp7MPZ-YZEtphUHV_Kjk3v3kl12-8GrpYzOIFRsLO7mY-croYeSzoG-zgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/whitedns/614" target="_blank">📅 17:37 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-612">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/YWtrJXmYeYE9FtGjkk3l2ebRek_pdnDSSUg7gYqTfrVJoMhxZQsiC_mp1Z790wil-iT_i98CNOOt7kYFD_oBLZpbH7gUJBeu32oviDoyYEk4H7XbSUL0KTOWnp_Hex2TBU2zzHx8uhjPWcATGhruckZrJ0WmmvWgba9s9nVSTeuSElGHh-A-dItV2dXG02SDMSGxLKrg7nzOTxMeQ7ILAfe_6AwAEaF92hJE_f052E3IHkgiQZMG2IBKSqh8npBSCTMv_a-hcofdL5dRvxGjMTQRFpz-tYFyD-1KxMRdZJ3eflN5tCiICfNGu0wkuOdEBeBo0ZYO8u9Y18cIxj54Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/Y8RfxLsr5bEw1M7ZNn3Bc4UP0nCZPu930eh0qp6Rrbod8_edtOEwUv4y7PSD9KE3NLTuINUGaVPgK9pTUhmgrX0QQ1RBmn29r31OaEb7fQBJTraaSbtKsIbYx2_u_sMOeYGUmD1BXmyUymNZQBK15_gJYipCWj0znEVErh5io13Wf_3U9xC5k4S-4x_nJsKZgO5m2lFn_2ufohNKFIs7Q-uRZJazEBXWNvJExAO-smgVouZD-Jd2SkBAiMX_etsArYZzaw0NVhCtb3pFyznJDZoOIkZ-a38Ge6QGnprbMqfsNkUlOV6mN-kaeDoGVxyuSK2eFo6lJ44U4TY1lKp2KA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">(موقت)
تنظیمات کلاینت Whitedns اندروید
همراه و رایتل و اپتل و مخابرات
یکی از اعضای عزیزی کانال "ارام " زحمت این کار کشیدید که از ایشون تشکر میکنیم
@whitedns</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/612" target="_blank">📅 17:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ShirOKhorshid-2026.05.14.apk</div>
  <div class="tg-doc-extra">23.9 MB</div>
</div>
<a href="https://t.me/whitedns/611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🛡
مهم: اگر این نسخه رو نصب کنید دیگه دردسر ستاپ کردن MITM و... ندارید!
این نسخه حدودا یک ساعت پیش توسط برنامه‌نویس شیر و خورشید آپدیت شد و به راحتی می‌تونید طبق این آموزش بهش وصل بشید:
1- وارد اپلیکیشن شیر و خورشید(آخرین نسخه که امروز منتشر شده) می‌شید
2- وارد بخش Options میشید از نوار بالا
3- روی More Options کلیک میکنید
4- گزینه‌ی  Connection Protocol رو قرار میدید روی CDN Fronting
5- میرید و عادی کانکت میشید و به راحتی وصل میشه!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/whitedns/611" target="_blank">📅 16:49 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MITM-DomainFronting-14.zip</div>
  <div class="tg-doc-extra">18.3 KB</div>
</div>
<a href="https://t.me/whitedns/610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود: https://guardts.ir/f/db4006f1197c و https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947 (شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی،…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/whitedns/610" target="_blank">📅 16:48 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش اتصال رایگان و نامحدود به اینترنت با متد ترکیبی MITM + Psiphon
⚡️
لینک‌های داخلی جهت دانلود:
https://guardts.ir/f/db4006f1197c
و
https://uploadgirl.ir/d/1f4fb76a-c869-494a-b439-b11cb8d35947
(شامل فایلهای V2rayNG، کلاینت شیر و خورشید، ویدئو آموزشی، V2rayN و فایل Certificate Generator و خود فایل Json پترنیها)
لینک پروژه اصلی:
https://github.com/patterniha/MITM-DomainFronting
⭐️
توی این ویدئو بهتون یاد میدم که چطوری با استفاده از متد ترکیبی سایفون(کلاینت شیر و خورشید) + کانفیگ دامین فرانتینگ پترنیها، به اینترنت بین‌الملل وصل بشید!
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/whitedns/608" target="_blank">📅 15:16 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-606">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z27wp_RwHtfmtblQETmmhD3gw7sBW0oEZ-QFQfk_wtwWbd2WeOZj3-XYYrTL0-3XRly2bvcVTC67hSD7ZFSNW7NUzOQQp_qWWbM2Ph6l-FpibxmH2JBPk9591mGh684ofCdo56hk9JzGITkZsbBl7BzrXZbx3b11FdPEjasMqXgLjmqzpLiyJ8e69h2XlK9n50XRDHXXih9QMuNUVBjf-jv5RyZjhBrRtIGlQczgV5yGXQnf2srczldT5ajYc-IkC-YRcoUbAPrx2SlJ9ElPjwq9M4qQilmoeJxixrCh-ckvm5dAxM4B6F0aVXCiYQsGhCLUnJ9XdkAzBkqZHtYETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرور جدید WhiteDNS
Domain:
v.whitedns.space
Encryption Key:
bad99364093861634030e96f11fe3132
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
این بزرگترین سرور ما هستش. ۱۲ هسته سی‌پی‌يو و ۲۴ گیگ رم.
✈️
هر مشکلی هست، از سمت اختلال شبکه، تنظیمات و ریزالور ها هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/whitedns/606" target="_blank">📅 09:31 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">📢
اطلاعیه مهم برای کاربران WhiteDNS
دوستان عزیز،
برای بهبود کیفیت اتصال و افزایش پایداری سرویس، تمام سرورهای فعلی WhiteDNS به‌زودی پاک‌سازی و جایگزین خواهند شد.
✅
سرورهای جدید به‌زودی از طریق همین کانال در اختیار شما قرار می‌گیرند.
تا زمان انتشار سرورهای جدید، لطفاً فقط به سرورهایی متصل شوید کهآدرس آن‌ها
whitedns.shop
نیست.
یعنی فعلاً از اتصال به سرورهای دارای دامنه زیر خودداری کنید:
whitedns.shop
ممنون که همراه ما هستید
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/whitedns/602" target="_blank">📅 09:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/R539fs7Ha6kVqyOY5Hc_u5PLHPP0rFcQo9CMM5YXmZ_ZeHMSZATVZkUX9W0TWitvoa8Z81xcv0KTk1rZ5u7kraSbAvbz9Ta4D62gXmPP3EkJe-KGS4M30lUqZpLC8pktgm3XDTmxZgJjsNEGQ710iXiGYyWHPkAoeahhlPw229DWSm7jrEouSVSDpmNPTjNWYmffkMs5KA03S44ONEjkuhtCJh4FhlFuasrmeeHLa133Cr02segT82ARq0-96gC6m2TCEpuxpHQ3OrXyDHr464gUu1zYBsVPQqFF5DfgKKlLNnKpWLhKWiAdx7azmheWzdbQ-n9wjKQTJKDlznkBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نسخه ۱.۰.۲
🔄
WhiteDns Windows
به زودی.................
🔥
🔥
🔥
🔥
نسخه ۱.۰.۲ بر پایداری، قابلیت استفاده و تشخیص‌های بسیار قوی‌تر رزولور تمرکز دارد.
🛠
این بروزرسانی مشکل آکاردئون را در بخش تنظیمات پیشرفته اصلاح می‌کند تا بخش‌ها با قابلیت اطمینان بیشتری باز و بسته شوند و چیدمان تنظیمات رفتار سازگارتری داشته باشد. همچنین اسکنر رزولور را با یک حالت اسکن پیشرفته جدید بهبود می‌بخشد که رزولورها را به روشی واقع‌گرایانه‌تر و آگاه به تونل، با استفاده از دامنه فعال تونل آزمایش می‌کند، از جمله بررسی‌های DNS بدون کش، قابلیت EDNS0، یکپارچگی NXDOMAIN، مدیریت زیردامنه‌های تو در تو و جستجوهای پروب به شکل تونل.
🌐
تجربه نتایج اسکن نیز بهبود یافت. اکنون خروجی با اطمینان بیشتری کار می‌کند، مرتب‌سازی به درستی عمل می‌کند و نتایج صادر شده اکنون بهتر با آنچه در رابط کاربری نمایش داده می‌شود مطابقت دارند. جزئیات اضافی اسکن مانند امتیاز، دامنه پروب و قابلیت مشاهده بار EDNS اضافه شد تا رزولورهای قوی‌تر را با دقت بیشتری شناسایی کنید.
📊
✨
@whitedns</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/whitedns/601" target="_blank">📅 08:04 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-593">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.3.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.2 MB</div>
</div>
<a href="https://t.me/whitedns/593" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی اسکن Resolverها، مدیریت ساده‌تر پروفایل‌ها و پایدارتر شدن اتصال در خود WhiteDNS بوده است. هدف این بود که کاربران راحت‌تر Resolverهای سالم را پیدا کنند، نتیجه اسکن را ذخیره و دوباره استفاده کنند، و اتصال Proxy یا Full VPN در پس‌زمینه و بعد از قطع‌و‌وصل شدن مطمئن‌تر بماند. در کنار این موارد، امنیت خروجی‌ها، بکاپ و اشتراک‌گذاری فایل‌ها هم بهتر شده است.
✅
نسخه اپلیکیشن به 1.3.0 ارتقا پیدا کرده
✅
بخش جدید Scan برای بررسی و پیدا کردن Resolverهای سالم اضافه شده
✅
حالا می‌توانید فایل Resolver وارد کنید و اپ خودش Resolverهای سالم را جدا کند
✅
نتیجه اسکن به‌صورت خودکار داخل پروفایل‌های Resolver ذخیره می‌شود
✅
می‌توانید نتیجه اسکن را با نام دلخواه به عنوان Resolver Profile جدید ذخیره کنید
✅
Resolverهایی که قبلاً سالم شناخته شده‌اند دوباره بی‌دلیل اسکن نمی‌شوند
✅
امکان توقف اسکن و ادامه دادن آن از همان‌جایی که مانده اضافه شده
✅
سرعت اسکن قابل تنظیم شده تا بین سرعت بیشتر و مصرف باتری کمتر انتخاب کنید
✅
وضعیت اسکن با تعداد کل، سالم، ردشده و میزان پیشرفت واضح‌تر نمایش داده می‌شود
✅
می‌توانید برای اسکن، پروفایل سرور جداگانه انتخاب کنید
✅
اگر پروفایل اسکن سرور یا کلید نداشته باشد، اپ واضح‌تر هشدار می‌دهد
✅
حالت روشن، تاریک و خودکار برای ظاهر اپ اضافه شده
✅
مدیریت پروفایل‌های اتصال، Resolver و تنظیمات پیشرفته مرتب‌تر و راحت‌تر شده
✅
امکان وارد کردن تنظیمات پیشرفته از فایل یا متن TOML اضافه شده
✅
امکان خروجی گرفتن تنظیمات پیشرفته به فایل advanced_settings.toml اضافه شده
✅
خروجی گرفتن و اشتراک‌گذاری فایل‌ها امن‌تر و تمیزتر شده
https://dl.toolschi.com/view.php?f=e15bcec825298e4c.zip
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.3.0
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/593" target="_blank">📅 06:12 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-588">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بعد از اسکن بیش از
60,000
آی‌پی، تعداد
435
ریزالور سالم و قابل استفاده پیدا شد.
لیست این ریزالورها حالا از طریق ربات زیر در دسترسه:
@dns_resolvers_bot
برای دریافت لیست، وارد ربات شوید و دستور زیر را ارسال کنید:
/dns_master
بعد از ارسال دستور، می‌تونید لیست ریزالورها رو دریافت کنید یا فایل آماده رو دانلود کنید.
از همه کانال‌ها و دوستانی که این لیست رو بازنشر می‌کنند خواهش می‌کنیم حداقل سهم و همکاری‌شون این باشه که کانال ما رو به عنوان منبع ذکر کنند. این داده‌ها با زمان، هزینه و اسکن گسترده جمع‌آوری شده، نه با جادو و دعای نیمه‌شب.
Source:
@WhiteDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/588" target="_blank">📅 18:51 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-587">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
از چنل اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 1
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey Server 2
Domain:
v2.abolfazlshahi.cloud
Key:
965a568dccef58af7afb86e8ee55eea6
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/whitedns/587" target="_blank">📅 18:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-586">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن رسمی (WhiteDNS)
❤️
تاریخ بروزرسانی : ۲۳ اردیبهشت
👾
لینک دانلود
کلاینت :
1️⃣
WhiteDNS
1.2.0
⬅️
نحوه ی اضافه کردن پروفایل ها
⬅️
فیلم اموزش وایت دی ان اس
👍
تنظیمات مخصوص وایت دی ان اس
👌
آموزش ترکیب با برنامه ی نکوباکس
👍
آموزش ترکیب با برنامه npv
(پیشنهادی)
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJ2MS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJ2Mi5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJ2My5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NC5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJ2NS5tYXNpci1zZWZpZC5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
✉️
Channel |
@Masir_Sefid
| کانال
✉️</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/whitedns/586" target="_blank">📅 18:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-585">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/UBLwccaDPgy0hT2si1X538DhWkQWY71HNikt_0aqZ161ql7KzBZ74tOBIfYmPsh5DPwSPzs0hCBG_SpTE3_W3z_vZPDuGJhcozIKKskh9zKsLqVm9NUtpNZ8RuJnvHgI8oNI6py4JZALSxaoBmHcwYjzhKJJwm7UGRkbwrzDok9-e4QjkAGyCQm0P_8sfIVObaQ4kTP-sJ62aeInIfP1EP8aRlNJHuTzxTpyvbbneF62OhipCb61sJO4LMIi7vEGkbEDyj6UwLxCQ0nrhIOZFg6Qq64c90CC2L9iUhu0KIDc6-S5-ApeemexOOq_SLX19Xyv2tEljIV5EU4zcsS0OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/whitedns/585" target="_blank">📅 16:49 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-584">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDns-Windows-Setup.exe</div>
  <div class="tg-doc-extra">9.1 MB</div>
</div>
<a href="https://t.me/whitedns/584" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار اولین نسخه ویندوز WhiteDNS
نسخه
WhiteDNS Windows V1.0.1
منتشر شد.
این اولین نسخه رسمی ویندوز WhiteDNS است؛ نسخه‌ای که برای شبکه‌های سخت، محدود و فیلترشده طراحی شده تا اتصال پایدارتر، سبک‌تر و قابل‌اعتمادتر فراهم کند.
در این نسخه تلاش کردیم هسته‌ی ارتباطی WhiteDNS را برای ویندوز آماده کنیم و امکانات اصلی را در اختیار کاربران قرار دهیم:
• انتقال ترافیک از طریق DNS Tunnel با سربار پایین و پایداری بهتر
• پشتیبانی از چند مسیر اتصال از طریق چند Resolver و Tunnel
• تشخیص سلامت Resolverها و غیرفعال‌سازی یا فعال‌سازی خودکار مسیرها
• مدیریت هوشمند MTU برای حفظ پایداری اتصال در شبکه‌های ضعیف
• بهینه‌سازی جریان اتصال برای SOCKS4 و SOCKS5
• سرویس DNS محلی و قابلیت کش DNS سمت کلاینت
• پشتیبانی از روش‌های رمزنگاری مختلف مثل AES، ChaCha20 و XOR
• استفاده از Wintun Adapter برای ساخت اتصال VPN در ویندوز
• مدیریت Route و DNS به‌صورت خودکار
• رابط کاربری دسکتاپ با امکان ساخت پروفایل، ذخیره‌سازی امن، Import/Export، ویرایش ساده و پیشرفته، نمودار زنده، لاگ‌ها و تنظیمات
این نسخه شروع مسیر WhiteDNS روی ویندوز است و مثل همیشه با کمک فیدبک‌های شما بهتر و پایدارتر خواهد شد.
اگر تست کردید، لطفاً نتیجه اتصال، لاگ‌ها و مشکلات احتمالی را با ما به اشتراک بگذارید تا نسخه‌های بعدی دقیق‌تر و قوی‌تر منتشر شوند.
لینک داخلی :
https://uplod.ir/8h2n22ficr8f/WhiteDns-Windows-Setup.exe.htm
Special thanks to
Masterdns
❤️
for their amazing work - without them non of this was possible
@WhiteDNS</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/whitedns/584" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-583">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qPVZdrTBljmMLNsL2KQN4QD3MGyvuJE6Q5wjw65U8A3NPE70CIvj9UJvoqDka6vYxZz1CVaGl2DXO1TNb8qp6LFiEAemTlEnaS-8vUue7kpGF2cZAOWxN7qrTuwbCw43nw98cDd0CDJJt40YG6iHJr4EFIiL2vyedeh8YSOJqcLINL4cL8dR4HZb5Y3ZivJPvGVCASWuoZu0Wgcevg0lZhUzJiAXOU7QqfiLJtIQsYnwVabZYpkmiZTQlwF4oZS3brtdIbVXa6dP0L29tHi7GNANOVUIgDX1fhgmbg2sZebcQIJlgevd0F0CBL9FSNEvvg0JSOp47KepKN5Kvbnz6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/whitedns/583" target="_blank">📅 14:29 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-582">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUdp5voJuxZUOyMBH1RktAXdVAj047JrKefrCeKYKh2JV9NAUji91-AL_o3kKcLlaEUgQzNp625VxgHpQeZmdojytvYCLb6AgvdBqzVCZAbD0Ig3sRbtJu7Z7d2n8PkzgSoncpNkeqTY2kWgdcAC7Iu-gEbvb0h_fiAJSOnJjn-NXXMlXtCRJp7JMIidg_gpoMJUdBmTaEiHxWcnzpaTywCopD7tzSG89f0Fsgca4J3U--AqK0Hu1k3tOW3dwRKlA8-Lx8JI2bq464XY7BmOc42BZ3K1o1alVjZ0Km37W4iSenjKrphcF-sjebfBNQuRYsBURV9_eGAePx8YbnugXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز،
یک نکته مهم را لازم دیدیم با شما به اشتراک بگذاریم.
بر اساس بررسی‌هایی که انجام دادیم، فیلترینگ دامنه‌های عمومی همیشه به‌صورت کامل و یکسان انجام نمی‌شود. در واقع این محدودیت‌ها معمولاً به‌شکل منطقه‌ای و بسته به اپراتور، مسیر شبکه و Resolverهایی که استفاده می‌شوند متفاوت است. اینترنت هم طبق معمول تصمیم گرفته مثل یک موجود عصبی رفتار کند.
برای مثال، اگر به وضعیت سرورهای WhiteDNS در تصویر دقت کنید، میزان لود شبکه یکی از سرورهای ما از حدود
4Mbps
به نزدیک
400Kbps
کاهش پیدا کرده است. این یعنی در بعضی مسیرها یا اپراتورها، دسترسی به برخی دامنه‌ها محدودتر شده یا کیفیت ارتباط افت کرده است.
به همین دلیل، ممکن است روی بعضی از سرورها تعداد Resolverهای کمتری دریافت کنید یا کیفیت Resolverها نسبت به قبل پایین‌تر باشد.
ما در حال بررسی راهکاری هستیم تا بتوانیم دامنه‌های سرورها را به‌صورت روزانه به‌روزرسانی کنیم و کیفیت اتصال را پایدارتر نگه داریم.
تا زمان آماده شدن این راهکار، می‌توانید از سرورهای کانال همکار ما،
@Masir_Sefid
، که در پست قبلی معرفی کردیم استفاده کنید.
تمام سرورهای ما و سرورهای کانال همکار، به‌صورت مداوم مانیتور می‌شوند تا در صورت افت کیفیت یا مشکل اتصال، سریع‌تر بتوانیم وضعیت را بررسی و اصلاح کنیم.
ممنون از همراهی و گزارش‌های دقیق شما
🤍
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/whitedns/582" target="_blank">📅 10:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQ-D7YGV5Ck_r_kKgv4ULI8BFvqKMd8A00fY73Anbm0xJrssi5rChwDiACDnxP6QUwZvPsI4_efqLri8zfL1X4b3eIs3R2HC3y9qfGY3egu9puBDkTsJawGe7sTVlFbUNPVphtChddJN2TVYwNppFNBrPNilJsAw1UpDAOxLvTv5DbVz1FCRtO9ScomaG0Ag6XW6E8MpMlaTL3GZvnyWukspIw7SlpqtHp0IFbr14wBYCNcHWSM_pzepejlLL33vM6o8vIFAOw9Uk5_GxsFhCl75HolDlDQ17ZuXooL0MilVHxWRDFT4lwo2v_VhBQxctVLXLP8Zm7pLiY9FMp0lPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امکان دانلود کل ریزالور ها به ربات
@dns_resolvers_bot
اضافه شد
@WhiteDNS</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/whitedns/580" target="_blank">📅 05:25 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به دلیل تعویض زیاد سرور ها توسط کاربران، تلگرام ممکنه بخاطر امنیت اکانت شما دستگاه شما رو از روی اکانت logout کنه و دیگه نتونید وارد اکانتتون بشید!
راه‌حل:
1. اکانت تلگرام خود را روی یک گوشی دیگر login کنید تا در صورت logout شدن شما بتونید دوباره به اکانت بازگردید.
2. رمز دو مرحله‌ای اکانت و ایمیل بازیابی را فعال کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/whitedns/579" target="_blank">📅 14:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/olGVe3CUVV3-vXQWXAz7Ry2KbzHOsT_VX9RoVCVkHLt7hH2cyEp_UqTCQ__82jh1Wj9WtoirJUndL79ytQYFNzZGiXmflZRFh2uY9utcKhifHAY9EBwwlfrCxs4qnB9Y4hP2iGL754v85uaEph_H4IAnmlSHhXA_3PZpz986r2du5ge7DUMsiLaPiPwKuNpjUeUMAgyk02l-VhyS89ZYcipe0CV12_9QQHoC_dGhS2AtV0ibKWR_1-GyBXlWFJoor_uhKlrMYy3ZPPabVTYOzq_FhAif9W_Ae38hH_nW445uWT2VM9Ek7uYccGHz0M7zGnJhWPhRduQNeLim0a4bBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اگر اینترنت غزه، اوکراین یا هرجایی که حمایت از آن برای حامی‌نماهای حقوق بشر "ویترین اخلاقی" داشته باشد فقط ۷ روز قطع میشد، دنیا را روی سرشان خراب می‌کردند؛ اما اینترنت ایران ۷۴ روز است عملاً قطع شده و آب از آب تکان نخورده است.
‏فکر می‌کنید اتفاق خاصی افتاده؟ خیر.
‏ضریب دسترسی واقعی به اینترنت آزاد در ایران به گواه نت‌بلاکس به حدود ۲ درصد رسیده؛ میلیون‌ها انسان نه ۷ روز، بلکه ۷۴ روز عملاً در یک زندان دیجیتال گروگان گرفته شده‌اند و همزمان که جمهوری اسلامی در پشت پرده به سرکوب، بازداشت و اعدام مشغول است، آشغالی به نام ⁧
#اینترنت_پرو
⁩ را به‌عنوان راه‌حل به مردم می‌فروشد، که عقیم‌سازی عمدی دسترسی آزاد به اطلاعات و نقض آشکار حقوق انسانی و حریم خصوصی شهروندان است.
‏ظاهراً برای جهان مدعی آزادی، فقط آن دسته از رنج‌هایی دیده می‌شوند که موضع‌گیری برایش هزینه‌ای نداشته باشد، یا چشم‌های مردمانش رنگی باشد.
منبع
https://x.com/ircfspace/status/2054094958353678824?s=46</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/whitedns/578" target="_blank">📅 12:53 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-poll">
<h4>📊 آیا به اپ WhiteDNS تونستید وصل بشید؟</h4>
<ul>
<li>✓ آره</li>
<li>✓ نه</li>
</ul>
</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/whitedns/577" target="_blank">📅 11:23 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-575">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB4S_xbErZs8OxrtqCHEM_tOzXPEfrqZEHE7xCg03OMvh4eAvP1aBLQsja9irPg08_o2e89YC5BzkTmfAynvXEr5L4c9uijvNRS4ye1mLRAfM1rCVn1PIVkDSymQovcDgKsqWMBtKRAy5_QWJw4hzr6HsQSliHUr4nKlxszwvS3x7r_UKK81so8eFXYzbudClSeqzamOPKvtO_tkkwLBR2TCGCEnEwJhBV9T5eYoSgt-fvXtdhzvAGGrPYLUOKQiTiTiYNmbwpM3gVm0T_WlV394gsKtUh7WanXh_V5VWh-Ma_zDW4c4Uzi7JY9rth9SyPC587XTpN250BUsaX6W1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای دریافت ریزالورهای MasterDNS / StormDNS در WhiteDNS
ربات WhiteDNS حالا امکان جدیدی برای دریافت ریزالورهای MasterDNS / StormDNS دارد.
برای دریافت لیست ریزالورها مراحل زیر را انجام دهید:
1️⃣
وارد ربات زیر شوید:
@dns_resolvers_bot
2️⃣
دستور زیر را برای ربات ارسال کنید:
/dns_master
3️⃣
بعد از نمایش لیست ریزالورها، برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید.
4️⃣
لیست کپی‌شده را داخل اپلیکیشن WhiteDNS وارد کنید و از آن برای اتصال استفاده کنید.
#آموزشی
@WhiteDNS</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/whitedns/575" target="_blank">📅 10:04 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-574">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚀
سرور اهدایی از چنل
@Masir_Sefid
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigxKSIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbS1DaGFubmVsLS0tPkBNYXNpcl9TZWZpZCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigyKSIsInNlcnZlciI6eyJkb21haW4iOiJzMi5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-ViigzKSIsInNlcnZlciI6eyJkb21haW4iOiJzMy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig0KSIsInNlcnZlciI6eyJkb21haW4iOiJzNC5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQE1hc2lyX1NlZmlk8J-Viig1KSIsInNlcnZlciI6eyJkb21haW4iOiJzNS5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW0tQ2hhbm5lbC0tLT5ATWFzaXJfU2VmaWQiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/whitedns/574" target="_blank">📅 09:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-573">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">White DNS
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/whitedns/573" target="_blank">📅 09:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-572">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=e5XXDfeo6a7UNs9r7RH49yr7H8g2OrjoVs8yMEo2rciZOnVUZDhaCEWtJnca_IVOdt03hXB-LzBWLT2iUt1M2PpeT9jKpJstM8nIJw13xhCaQaNmIsszM8OC7mUyBMdwYjnfSRwK30Yfp7g3Hf-BFpHVEldY77A16UYLIn__ZkUaImpCmpYqDjskaXNBedQWAvWcn7nSvh_VTWSx7VeaI8sjjcNeBKwUAFHVfQZMbdBkhBWugLeHAQRqizVBnBIOV-F6Thw1VZKrKRAaytDfBmeD5ZbnJDPDgn7lV6WciwoLpl0s5L-m-8yfbTjpUg1hgRawePxkw7AUzjnccxr5Vw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/9ad3f5766c.mp4?token=e5XXDfeo6a7UNs9r7RH49yr7H8g2OrjoVs8yMEo2rciZOnVUZDhaCEWtJnca_IVOdt03hXB-LzBWLT2iUt1M2PpeT9jKpJstM8nIJw13xhCaQaNmIsszM8OC7mUyBMdwYjnfSRwK30Yfp7g3Hf-BFpHVEldY77A16UYLIn__ZkUaImpCmpYqDjskaXNBedQWAvWcn7nSvh_VTWSx7VeaI8sjjcNeBKwUAFHVfQZMbdBkhBWugLeHAQRqizVBnBIOV-F6Thw1VZKrKRAaytDfBmeD5ZbnJDPDgn7lV6WciwoLpl0s5L-m-8yfbTjpUg1hgRawePxkw7AUzjnccxr5Vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموژش نسخه جدید Whitedns
📲
✨
یکی از اعضای کانال آقا محسن زحمت کشیدند
👨‍💻
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
🚀
✅
حالت Full VPN کامل‌تر و پایدارتر شده
🔒
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
🌐
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
🚫
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
⚡️
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
🎯
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
⚠️
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
💾
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
📂
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
🔄
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
↩️
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
📋
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
📄
#آموزشی
@whitedns</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/whitedns/572" target="_blank">📅 09:21 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-567">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/567" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم
🙏
تمرکز اصلی این نسخه روی بهبودهای داخلی VPN در خود WhiteDNS بوده است. هدف این بود که اتصال کامل‌تر، پایدارتر و مستقل‌تر شود تا کاربران برای باز شدن سایت‌ها و اپ‌ها دیگر نیازی به NekoBox، NVPN یا راه‌حل‌های مشابه نداشته باشند.
در این نسخه مسیر DNS و ترافیک داخل خود WhiteDNS بهتر مدیریت می‌شود، بنابراین تجربه اتصال ساده‌تر شده و کاربر می‌تواند مستقیماً از داخل اپ وصل شود.
✅
نسخه اپلیکیشن به 1.2.0 ارتقا پیدا کرده
✅
حالت Full VPN کامل‌تر و پایدارتر شده
✅
حالا DNS هم داخل خود WhiteDNS مدیریت می‌شود
✅
دیگر برای باز شدن سایت‌ها و اپ‌ها نیازی به NekoBox، NVPN یا ترفندهای مشابه ندارید
✅
مشکل وصل بودن VPN ولی باز نشدن بعضی سایت‌ها و اپ‌ها برطرف شده
✅
اتصال روی اینترنت‌های کند و Resolverهای دیرپاسخ بهتر کار می‌کند
✅
صفحه اصلی ساده‌تر شده و انتخاب سرور، Resolver و نوع تنظیمات راحت‌تر انجام می‌شود
✅
اگر سرور یا Resolver درست تنظیم نشده باشد، اپ واضح‌تر نشان می‌دهد چه چیزی کم است
✅
می‌توانید تنظیمات پیشرفته را با نام دلخواه ذخیره کنید
✅
امکان ساخت چند پروفایل تنظیمات پیشرفته اضافه شده
✅
می‌توانید هر زمان بین پروفایل‌های ذخیره‌شده تنظیمات پیشرفته جابه‌جا شوید
✅
امکان برگشت سریع به تنظیمات پیش‌فرض اضافه شده
✅
بعد از اتصال، نام پروفایل سرور، Resolver و تنظیمات فعال نمایش داده می‌شود
✅
امکان خروجی گرفتن فایل client_config.toml از داخل اپ اضافه شده
✅
ظاهر صفحه اتصال و دکمه Connect/Stop مرتب‌تر و جمع‌وجورتر شده
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.2.0
از همراهی و حمایت شما ممنونیم
❤️
1⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/whitedns/567" target="_blank">📅 06:55 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-565">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/whitedns/565" target="_blank">📅 14:20 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-564">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👇
👇
👇
👇
👇
👇
👇
👇
👇
https://t.me/whitedns_group</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/whitedns/564" target="_blank">📅 12:02 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-562">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امروز یک هفته از انتشار نسخه بتا۱ اپلیکیشن WhiteDNS می‌گذره
🎉
فکر می‌کنم برای شروع، اپلیکیشن مسیر خوبی رو طی کرده و این فقط با همراهی شما ممکن شده.
خواستم از همه دوستانی که در این مدت با دقت تست کردند، مشکل‌ها رو گزارش دادند و فیدبک درست و کاربردی به تیم ما دادند تشکر کنم. همین بازخوردها باعث شده هر روز بتونیم WhiteDNS رو بهتر، پایدارتر و کاربردی‌تر کنیم.
از اینجا به بعد، سرعت آپدیت‌های نسخه اندروید کمی کمتر میشه تا بتونیم تمرکز بیشتری روی توسعه نسخه ویندوز داشته باشیم.
از دوستان عزیزی که خارج از کشور هستند، همچنان درخواست داریم اگر امکانش رو دارند با دونیت سرور به پروژه کمک کنند. این کمک‌ها مستقیماً به بهتر شدن کیفیت سرویس برای همه کاربران کمک می‌کنه.
از دوستانی که داخل ایران هستند هم یک درخواست مهم داریم:
لطفاً فقط مصرف‌کننده ریزالورها نباشید. برای زنده نگه داشتن شبکه، باید مداوم اسکن انجام بدیم و ریزالورهای جدید پیدا کنیم.
WhiteDNS با کمک جامعه کاربری خودش قوی‌تر میشه؛ نه فقط با استفاده، بلکه با مشارکت همه ما.
ممنون از همراهی شما
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/whitedns/562" target="_blank">📅 10:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-561">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDwENwFLOaU43tj7C8ZBQDNBvqffLwrnZsQOK69sCf5HhDtmkzTJUbzFNGY3E4yhzBZlQolAQMZ1CKI36qANzGAwjFgcFyoSBIzNGzkNLoCJXIiIP8tn2gR7_xwSr8fPZudNDggUAM0j1C7EaVdRsjdrvE0ex9ohPHM26NBGl3kcDr1inMIMcTirMrpuPMnOLgMNNepcBfEJb-ndi3yM3jrGQBkXKtwg6DKNuQy1J22XsUPM-eQH1J_winHwvhSGcE_aDqYg9LOQQxv2vkDQIXlSWOz1NWvmd1IanhcQwbUcAIgpfimlVEOs4A6ro8yc3MGHJMivvmNrcIwP5fd04Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/561" target="_blank">📅 09:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-556">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.1.0-arm64-v8a-1778467437126.apk</div>
  <div class="tg-doc-extra">5.1 MB</div>
</div>
<a href="https://t.me/whitedns/556" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید  WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
هدف اصلی از انتشار نسخه ۱.۱.۰، رفع مشکل «وصل می‌شود و دیتا مصرف می‌کند، اما چیزی باز نمی‌شود» است.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
در این نسخه، اپلیکیشن بعد از اتصال وضعیت واقعی مسیر ارتباط را بررسی می‌کند و دیگر تلاش برای استفاده از Resolver یا تونل ضعیف و بدون پاسخ را بی‌پایان ادامه نمی‌دهد. اگر مسیر اتصال بعد از چند تلاش قابل استفاده نباشد، ارتباط‌های جدید رد می‌شوند و اتصال معیوب بسته می‌شود تا حجم بسته شما بی‌دلیل مصرف نشود.
همچنین هسته StormDNS در این نسخه تغییرات مهمی داشته و به همین دلیل اتصال بسیار سریع‌تر برقرار می‌شود. VPN/Proxy بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن سریع‌تر فعال می‌شود و اسکن کامل Resolverها و MTU در پس‌زمینه ادامه پیدا می‌کند. علاوه بر این، اتصال‌های ناسالم زودتر تشخیص داده می‌شوند، مدیریت ارتباط‌های جدید پایدارتر شده و کتابخانه‌های native برای همه معماری‌های اندروید دوباره ساخته شده‌اند.
در این نسخه تمرکز اصلی روی پایداری بهتر اتصال، شروع سریع‌تر VPN/Proxy، مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و عیب‌یابی امن‌تر بوده:
✅
نسخه اپلیکیشن به 1.1.0 ارتقا پیدا کرده
✅
مشکل گزارش‌شده‌ای که بعضی کاربران وصل می‌شدند و مصرف دیتا دیده می‌شد، اما سایت‌ها و اپ‌ها باز نمی‌شدند، برطرف شده
✅
حالا بعد از اتصال، مسیر ارتباط بررسی می‌شود و اگر تونل، Resolver یا مسیر خروجی پاسخ‌گو نباشد، اتصال‌های جدید به جای گیر کردن و مصرف بی‌فایده دیتا رد می‌شوند
✅
وضعیت سلامت اتصال داخل اپ نمایش داده می‌شود تا مشخص باشد اتصال واقعاً قابل استفاده است یا نیاز به بررسی دارد
✅
سرعت شروع اتصال بهتر شده؛ اپ بعد از پیدا کردن حداقل Resolverهای سالم با MTU امن، VPN/Proxy را سریع‌تر فعال می‌کند
✅
اسکن کامل Resolverها و MTU حالا در پس‌زمینه ادامه پیدا می‌کند و Resolverهای سالم بعداً به اتصال اضافه می‌شوند
✅
امکان روشن و خاموش کردن WhiteDNS از Quick Settings اندروید اضافه شده
✅
دکمه Disconnect به نوتیفیکیشن VPN و Proxy اضافه شده
✅
امکان Import پروفایل از لینک‌های stormdns:// اضافه شده
✅
هنگام Export پروفایل، QR Code نمایش داده می‌شود تا اشتراک‌گذاری راحت‌تر باشد
✅
ورود Resolverها ساده‌تر شده و حالا می‌توانید چند Resolver را با کاما، سمی‌کالن یا خط جدا وارد کنید
✅
پورت پیش‌فرض :53 به صورت خودکار مرتب و ساده‌سازی می‌شود
✅
اگر Resolver واردشده اشتباه باشد، اپ قبل از اتصال خطا را نشان می‌دهد
✅
تنظیمات پیش‌فرض MTU و پایداری اتصال بهینه‌تر شده‌اند
✅
مدیریت پروفایل‌ها هنگام اتصال بهتر شده و فقط در زمان Connecting محدود می‌شود
✅
بخش Split Tunnel و تنظیمات پیشرفته مرتب‌تر و جمع‌وجورتر شده‌اند
✅
بخش Logs به جای خروجی فایل، Diagnostics آماده و امن تولید می‌کند که اطلاعات حساس داخل آن مخفی می‌شود
✅
هسته StormDNS برای همه معماری‌های اندروید دوباره ساخته شده و پایداری اتصال بهتر شده است
🔗
GitHub:
https://github.com/iampedii/WhiteDNS/releases/tag/1.1.0
از همراهی و حمایت شما ممنونیم
❤️
1️⃣
WhiteDNS</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/whitedns/556" target="_blank">📅 06:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-553">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1QFnrgWruC58q5G5eL8FhHitmPnSF0q7Ea8Ah_nQhNsr5Xd1gH-csnoc4MQP6bGF6b9zvrwHkYSoJOERHDmlKRTd3jWs2JcJ_dJPdkkBGDpPX41pkIfKK7Kp3a64sIvNYyLEE6Da8Eg2IVg6SSN_iObFp8AwpXwvqt9roVQQ4ge73HNQqmUzuQE2mOR0mAjlKtr6LjL8wy-6mHqf6wPYv0WLcFRVbDlwe2So7Pbf_cDzaG3jo6HZiP9SyXk9p-pD-r7OctJ_JWmkerXIKCWF50YPHmxfcGIUJ5O_5cf-yDU_a4ObE4c08MkNd85o2U0LHgF5fdeTaNddh5bwGahWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمام سرور هایی که داخل اپ بودن داخل تاپیک سرور این گروه هستند. لطفا عضو بشید و گفت و گو ها اصلی رو اونجا ادامه بدید.
1⃣
t.me/whitedns_group</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/whitedns/553" target="_blank">📅 15:47 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-552">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnFy_0yBEIoBe2nMPz9025byAr6in1TBz9QB8oscShd-otbs11GSMkQq7JFEj3xvWvbSrXVc19cEGRUoxgXZcVjE9Ah3Dhm6uvY4RbenvBr06K4S4UGGCB-LulET3hx_LOn8659Vpf7o8VztpcyGPNlFo-hFgd0ChZvoIFHk0SGJmFpkQnfvrEMqvk_qTir7C4x89jA-DqVlyuxhq0b2d-MGWi9C_aM6NFGi3Y5zfXIAoGOBarg8vgvN-gea5hem17wykJ7BQYscCoN6m_8Ufzp7hM4lJmD3kxAPQFYEN_NRsVcSas5K_C7PBYsOV5NtIMaqYg94AwexhKErxHm4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/whitedns/552" target="_blank">📅 15:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-551">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">White DNS
pinned Deleted message</div>
<div class="tg-footer"><a href="https://t.me/whitedns/551" target="_blank">📅 14:01 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-544">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-1.0.0-x86_64-1778404214016.apk</div>
  <div class="tg-doc-extra">5.3 MB</div>
</div>
<a href="https://t.me/whitedns/544" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
انتشار رسمی WhiteDNS به صورت متن‌باز
دوستان عزیز،
پروژه WhiteDNS رسماً به صورت Open Source روی GitHub منتشر شد.
این نسخه، اولین ریلیز رسمی
1.0.0
بعد از ۷ نسخه بتا است و از این به بعد مسیر توسعه پروژه شفاف‌تر، عمومی‌تر و با مشارکت جامعه ادامه پیدا می‌کند.
در این نسخه، پروفایل‌های پیش‌فرض WhiteDNS از داخل اپ حذف شده‌اند
تا برنامه به شکل مستقل‌تر و عمومی‌تر قابل استفاده باشد.
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
قبل از آپدیت به این ورژن ، تمام پروفایل های خودتون رو Export بگیرید. ورژن جدید دیگه سرور های WhiteDNS را در اپ ندارد.
ورژن جدید اپ Sign شده هستش و از لحاظ امنیتی بهبود یافته.
برای نصب، ورژن قبلی اپ باید به صورت کلی از روی دستگاه شما حذف شود.
از این ورژن به بعد، نیازی برای پاک کردن اپ در هر آپدیت نیست.
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
👆
از این مرحله به بعد، توسعه‌دهندگان و کاربران می‌توانند پروژه را بررسی کنند، مشکل‌ها را گزارش دهند و در بهبود آن مشارکت داشته باشند.
🔗
GitHub:
https://github.com/iampedii/WhiteDNS
از همراهی و حمایت شما ممنونیم
❤️</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/whitedns/544" target="_blank">📅 12:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-538">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
پروفایل های مخصوص وایت دی ان اس ورژن جدید( 7 WhiteDNS)
👾
کلاینت :
WhiteDNS
1️⃣
|
WhiteDNS
2️⃣
⬅️
نحوه ی اضافه ی کردن پروفایل ها
⭕️
پست تنظیمات کلاینت
⭕️
پست تنظیمات بهینه تر
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoicy5vNHMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMikiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oMykiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczMubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNCkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczQubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiQGxpbmtfZGFraGVsaV9hcHDirZDvuI8oNSkiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczUubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/whitedns/538" target="_blank">📅 09:40 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-537">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">سرور اهدایی از چنل
@pythash
لطفا از چنل دوستان اهدا کننده سرور حمایت کنید.
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
🇹🇷
Turkey
Domain:
v1.abolfazlshahi.cloud
Key:
a4c5649c628ac1103ad55c5208e0d74d
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
〰️
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/whitedns/537" target="_blank">📅 09:27 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-536">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سلام خدمت همگی دوستان
🔴
11 سرور اختصاصی جدید و بهینه برای اپلیکیشن WhiteDNS
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidi53aGl0ZWRucy5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InYud2hpdGVkbnMuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiYjA3ZGMzNTczNjBkNmU2ODk2NTA5MTM2ZDcwOTc4OTciLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEyLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEyLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjAwOWM1MTRiMmE2NDNlZDQwY2JkN2NjNjE5Mzg5YjBmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEwLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEwLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjFlY2Q1ZmRmZTM1MWE5MzEzY2VhMzlmZTFiOWM1OWRkIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjkud2hpdGVkbnMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJ2OS53aGl0ZWRucy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJhMmYzMzQ4YmZhMDIxNzA2Mzk5NzBmMmQ2M2YxMDNkYyIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjExLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjExLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjRjMTY2OTMyNmNkYmU4OThjYWIwOTY1YWNlMzAxMGMwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjEzLndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjEzLndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImUyOTE4ODcwY2U4OGYwNTU0N2ZiZmJhOTlhZWU0ZWM1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE0LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE0LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjliODY3MmEzNTJkMDQwNDg5ZDk2YmU5ZGY5N2VkOTY2IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE1LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE1LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjlhYTY4ZTdlOWE3YzIyZDkxZDhmNDY2ZDY0YTM1ZGZmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE2LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE2LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU5Mjg0NWNhMzhmMTk0NjEzODNkMDU3MzNjMzMyMTRjIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE3LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE3LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IjU3NjU1MDM1NGE3MzA5NTMwYjdmYTI1MTUyZGM2NzJmIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidjE4LndoaXRlZG5zLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoidjE4LndoaXRlZG5zLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6ImQwNTM4YTNkNTQ1YTc4MzBiOGJiMmViMGMzNzQ4ZTk1IiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
#Servers
@WhiteDNS</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/whitedns/536" target="_blank">📅 07:42 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-535">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dE_s5gJXemLpbOkLf0_ch6nncvDzCbbjnqq3ZgXHyJcogq7i9K0l5ya4tj_Dxg9HolyMhhMsVUH8AdzQ-DFoJvKcpjrOQmgRluOT36ytceW-XU_GlfhjDe52xoVEW_SoxzD9SgaXY8bvbgfX64xNLodlMSR-bVMk6QmUCZgyE2Pfr1yUeoeGLPjgUq4Gn0IkokwmkhYhVCy48AIHt84S1oM59p_-nqOAOu4rqdXB7U6aZZDrPKsrzbefB_UvQO_1PuoUQS3_TAzn_ppuQsXGJssmqnBACobHpzo_aue5bnobJvUiyQHWBStws-ZolQD_5eRuEIorRn3Yq1FGS771Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چگونه بعد از اسکن، DNS های سالم رو برای بعدا ذخیره کنیم؟
بعد از اتصال، زیر دکمه
Connect
یک عدد نمایش داده می‌شود.
اگر روی عدد بخش
Valid
بزنید، فقط لیست ریزالورهایی که با موفقیت تست شده‌اند نمایش داده می‌شود.
می‌توانید همان لیست را کپی کنید و با آن یک پروفایل ریزالور جدید بسازید. بعد از آن، هنگام اتصال، پروفایل جدید را انتخاب کنید.
با این کار هم اتصال سریع‌تر برقرار می‌شود و هم اپلیکیشن سبک‌تر اجرا می‌شود
@WhiteDNS</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/whitedns/535" target="_blank">📅 05:18 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-533">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه، یک گروه جدید برای کانال ساختیم.   متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/533" target="_blank">📅 20:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-532">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سلام خدمت همه دوستان عزیز
🌿
برای اینکه مطالب، آموزش‌ها، فایل‌ها و بحث‌های مرتبط با WhiteDNS بهتر دسته‌بندی بشن و دسترسی بهشون راحت‌تر باشه،
یک گروه جدید برای کانال ساختیم
.
متأسفانه تلگرام این امکان رو به ما نمی‌ده که گروه فعلی رو به گروه دارای Topic تبدیل کنیم. برای همین، جهت حفظ بهتر مطالب و جلوگیری از گم شدن آموزش‌ها و اطلاعات مهم، لطفاً عضو گروه جدید ما بشید.
از این به بعد گفت و گو های اصلی تیم، آموزش‌ها، مطالب فنی و اطلاع‌رسانی‌های مهم داخل گروه جدید انجام می‌شه.
گروه فعلی فقط برای کامنت‌های مربوط به پست‌های کانال استفاده خواهد شد و فعالیت اصلی تیم در اون محدود می‌شه.
ممنون از همراهی همیشگی‌تون
❤️
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/whitedns/532" target="_blank">📅 20:38 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-531">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بازی ساده اس !ً مدت ها ذهن شما با قیمت vpn های هر گیگ 1 میلیون و یا 500 هزار و یا 200 هزار تومن عادت کرده بود
حالا وقتی vpn بشه هر گیگ 80 تا 100 کلی حس پیروزی و خوشحالی داری و مدتی لذت میبری ازش .
بعدش پیش خودت میگی خب میرم سیمکارت پرو میگیرم بشه هر گیگ 40 هزار تومن و اون لحظه اس که دیگه حسابی خوشحال خواهی بود چون با نصف قیمت VPN دیگه اینترنت داری  !
حالا اینکه روزی سه چهار گیگ میتونی در روز مصرف کنی و 11 برابر گرون تر از 3 ماه پیشه که اینترنت وصل بود دیگه اصلا به ذهنت نمیرسه چون مدت ها درگیر بازی قیمت توسط حکومت بودی
اینجوری چرخه بردگی تا ابد ادامه پیدا می‌کنه
حالا فهمیدید چرا ما با هر رانت دولتی مخالفیم ؟
@whitedns</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/whitedns/531" target="_blank">📅 19:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-530">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سوالات پرتکرار مربوط به برنامه‌ی WhiteDNS
این تلگراف به مرور تکمیل تر شده و سوال های بیشتری نیز داخل آن قرار خواهد گرفت.
@WhiteDNS</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/whitedns/530" target="_blank">📅 16:17 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-529">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/529" target="_blank">📅 16:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-527">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Ml_CmafD3cP_OPPiHucQsddz_Pc2U2EEJcPId5hJDEh1O2A3KW05VevNv5BzIxHHmMZ5m8eTnAdLXlzFk2q_pR4u8ATFyLkpIU5CeP3kvgQdccy948JVvBHQUXZs8BkL3JdIByZQh__qRNb-HvhLbfLMh42mpJ9HNHKCQeVQrscKnhv1uQRtg38JCqc7rAiw63Adg7fNhsDiWEu-b7a_I-te9xfHmg0jWCAGn0qk6CUhpzHjt6cVCQqhYqpYy863VJTAhlaWefFd7V-3mDRI9QhmUFfKQBqbkWzxYp5dxhnZDm4I4NmBZKicRz_8nI2nGrRkouuRlOd0IdR7hBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام خدمت همه دوستان
🙌
دکمه Donation به ورژن بتا۷ اضافه شده. هر کمکی  از سمت شما فقط هزینه ساخت سرور های جدید و بهبود اپ WhiteDNS خواهد شد.
هیچ اصراری برای کمک نیست و تیم WhiteDNS کاملا رایگان و تا اتمام قطعی اینترنت ایران ادامه خواهد داد.
ممنون بابت همراهی شما
🙏
USDT (TON)
UQCVUC-eZzxNkVVewFp9pz43JKd0XIc55KCdC5gbwxJKiqoL
USDT (TRC20 / TRON)
TNvdayQydF8t8bNHMuBctxVdgiaWeNKhmR
USDT (ERC20 / Ethereum)
0x87519c886F79d3935b9A45519f821519272D9967
USDT (Solana)
7zKyVVnJRBEiw6vL6vnX1VKUTEkw5QvXu696QV5qLS94
@WhiteDNS</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/whitedns/527" target="_blank">📅 13:36 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-525">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsQqqBcM0hN1AAeKpdl1g-o2JQwuJCLOYIuGA8-QyszqafI0vTTdB0zAepWU8TLBrQNXqS7-mxfr9XVHL80kTexjPb8oL8WknvVpzJQKscHRaM1BRFWYh2Hq2nSUVV_nzglKq_II9C6qQYfmeVaABAXxhCLYIVFElsRGF_QvCLPC7mGX4StFVXxtfQDg1gtMaMfm7W0bri2PX4KHEEruhXzppoJn3BRSjfbPgxd_zOEZkIKZepD5fvF62D8waHEZBhIST07bvk8-vL-IJ6R4ZWhOzhGLnaAp6psiGToBLHhmhwWY11X2nbmMCdKe8PsyOx3U6wSM_d9PY7ptnBpAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/whitedns/525" target="_blank">📅 10:43 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">White DNS
pinned a file</div>
<div class="tg-footer"><a href="https://t.me/whitedns/523" target="_blank">📅 10:15 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-521">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTcND5o1jKG7gOUKOt9bAGfa2lHTV37XZceKjC7aToaojON5R4EcdDzCW5WqFCfzPG0CGzWgmFtmr2vf_Zav2j-MVufp9eWfq3OJApoEdkvu-VmfB1ndoDoOGHu86ncVlHGVvhR_BoQWaoTaJhbWyoPE5Ve5L229PisC3wveKX1bcxxqeupAZBIcueG9QIB5evoiY1MnkfQMiUnMe51z0Tje2oniUJucH4WFRbaPDsL2L8mhB9n59lfkb-DiTl0FrXm9qX6IN6EG3yEvgAi8oTT-zYnaUPb0TluijgtraGpc4IgAU49oja1IcSoFS2YHStNPfofHSngfV197lkgo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵ سرور اهدایی از چنل همکار
@link_dakheli_app
برای ایمپورت ابتدا ورژن اپ رو به بتا۷ آپدیت کنید، سپس وارد بخش پروفایل بشید و بعد دکمه ایپمورت رو بزنید.
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoidGUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InRlLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiZXUubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6ImV1LmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoic3IubGluay1kYWtoZWxpLWFwcC5zaG9wIiwic2VydmVyIjp7ImRvbWFpbiI6InNyLmxpbmstZGFraGVsaS1hcHAuc2hvcCIsImVuY3J5cHRpb25fa2V5IjoiVGVsZWdyYW1DaGFubmVsQGxpbmtfZGFraGVsaV9hcHAiLCJlbmNyeXB0aW9uX21ldGhvZCI6MX19fQ
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoicy5vNHMuc2hvcCIsInNlcnZlciI6eyJkb21haW4iOiJzLm80cy5zaG9wIiwiZW5jcnlwdGlvbl9rZXkiOiJUZWxlZ3JhbUNoYW5uZWxAbGlua19kYWtoZWxpX2FwcCIsImVuY3J5cHRpb25fbWV0aG9kIjoxfX19
stormdns://eyJzY2hlbWEiOiJ3aGl0ZWRucy5wcm9maWxlIiwidmVyc2lvbiI6MSwicHJvZmlsZSI6eyJuYW1lIjoiczIubzVzLnNob3AiLCJzZXJ2ZXIiOnsiZG9tYWluIjoiczIubzVzLnNob3AiLCJlbmNyeXB0aW9uX2tleSI6IlRlbGVncmFtQ2hhbm5lbEBsaW5rX2Rha2hlbGlfYXBwIiwiZW5jcnlwdGlvbl9tZXRob2QiOjF9fX0
👾
لینک دانلود نسخه بتا ۷ از سرور داخلی
WhiteDNS
1⃣
|
WhiteDNS
2⃣
@WhiteDNS</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/whitedns/521" target="_blank">📅 10:03 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-516">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta7-x86.apk</div>
  <div class="tg-doc-extra">22.8 MB</div>
</div>
<a href="https://t.me/whitedns/516" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه جدید تستی WhiteDNS آماده شد. ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
در این نسخه تمرکز اصلی روی مدیریت راحت‌تر پروفایل‌ها، اشتراک‌گذاری تنظیمات اتصال و پایداری بهتر بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta7 ارتقا پیدا کرده
✅
امکان Import و Export پروفایل‌های اتصال StormDNS اضافه شده
✅
حالا می‌توانید تنظیمات سرور شخصی را به شکل لینک stormdns:// خروجی بگیرید و برای دیگران بفرستید
✅
امکان وارد کردن چند لینک پروفایل به صورت هم‌زمان اضافه شده
✅
دکمه‌های Copy و Share برای لینک پروفایل اضافه شده‌اند
✅
امکان Export All اضافه شده تا بتوانید همه اتصال‌های سفارشی را یکجا خروجی بگیرید
✅
پروفایل‌های اتصال حالا با کشیدن و رها کردن قابل مرتب‌سازی هستند
✅
Resolver Profileها هم حالا قابل مرتب‌سازی شده‌اند
✅
ظاهر بخش Profiles مرتب‌تر شده و دکمه‌های ویرایش، حذف و خروجی گرفتن واضح‌تر شده‌اند
✅
وضعیت پروفایل انتخاب‌شده و پروفایل فعال واضح‌تر نمایش داده می‌شود
✅
قابلیت Traffic Warmup اضافه شده تا بعد از اتصال، مسیر ارتباط سریع‌تر آماده شود
✅
قابلیت Keepalive اضافه شده تا با ارسال ترافیک سبک دوره‌ای، اتصال پایدارتر بماند
✅
Traffic Warmup و Keepalive هم در Proxy Mode و هم در Full VPN فعال هستند
✅
از تنظیمات پیشرفته می‌توانید Traffic Warmup را روشن یا خاموش کنید و مقدار آن را تغییر دهید
✅
نمایش لاگ‌ها و وضعیت اتصال سبک‌تر و مرتب‌تر شده تا صفحه هنگام دریافت پیام‌های زیاد روان‌تر بماند
✅
دکمه Donate اضافه شده و امکان کپی کردن آدرس‌های حمایت مالی داخل اپ وجود دارد
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN برای تست وجود دارد و بهتر شده، اما چون کل ترافیک دستگاه را از تونل عبور می‌دهد ممکن است روی بعضی دستگاه‌ها یا شبکه‌ها سرعت و پایداری متفاوتی داشته باشد.
اگر سرور StormDNS شخصی دارید، حالا می‌توانید پروفایل اتصال خود را راحت‌تر با لینک stormdns:// ذخیره یا برای دیگران ارسال کنید. همچنین استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند فشار روی سرورهای عمومی WhiteDNS کمتر شود.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/whitedns/516" target="_blank">📅 09:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-515">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/djFlfVXj0kiwFCvzunnfBkeg_e2adkaxUsaYwtalHfZsrbD3Cnkq8B-GZ_IEG4atibpqPAKR6oi08BsYTkSO3SRmwTEA-FDemoycO1giDTFFqrIKDCZyN8PK1GY8ijMOKHDzh3qrsqbrzn7ZUFN7AZhGoXOuMoStYrZvPRlOd7Rti2EbPdc4IeUD05Fxq9izmoX5-29P8vW8tBdFxBDnir4f2FrPGnaRFk4xILr32sS9GW6dQ5ytVAf4yo71sAbG1SUWr17Fcpd9R8FjugtxVOAF8iuh97cY6Am9G3ZwFYGZSYnS7gzOoRllHLn49dLK_SsrC2EIt87WHOG_Lct39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/whitedns/515" target="_blank">📅 06:59 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-513">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">❤️
سرور اختصاصی whitedns برای Slipnet
❤️
آموزش کامل :
https://t.me/whitedns/294
دانلود کلاینت :
https://github.com/anonvector/SlipNet/releases/tag/v2.5.3
User:
whitedns
Password:
whitedns
[dnstt-socks] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-socks]
slipnet://MjJ8ZG5zdHR8ZG5zdHQtc29ja3N8dC5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wwfHx8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDB8MHx8fDgwODB8fDB8L3wxfHw=
[noizdns-socks]
slipnet://MjJ8c2F5ZWRuc3xub2l6ZG5zLXNvY2tzfHQuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[dnstt-ssh] Public Key: 1b23cc151ab07274a4f2623a94b7172d61803956fa068f5074e38ec5eb800516
[dnstt-ssh]
slipnet://MjJ8ZG5zdHRfc3NofGRuc3R0LXNzaHx0cy5pcmFubW90b3IuYml6fDguOC44Ljg6NTM6MHwwfDUwMDB8YmJyfDEwODB8MTI3LjAuMC4xfDB8MWIyM2NjMTUxYWIwNzI3NGE0ZjI2MjNhOTRiNzE3MmQ2MTgwMzk1NmZhMDY4ZjUwNzRlMzhlYzVlYjgwMDUxNnx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[noizdns-ssh]
slipnet://MjJ8c2F5ZWRuc19zc2h8bm9pemRucy1zc2h8dHMuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfDFiMjNjYzE1MWFiMDcyNzRhNGYyNjIzYTk0YjcxNzJkNjE4MDM5NTZmYTA2OGY1MDc0ZTM4ZWM1ZWI4MDA1MTZ8d2hpdGVkbnN8d2hpdGVkbnN8MXx3aGl0ZWRuc3x3aGl0ZWRuc3wyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MHwwfHx8ODA4MHx8MHwvfDF8fA==
[slipstream-socks]
slipnet://MjJ8c3N8c2xpcHN0cmVhbS1zb2Nrc3xzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHx8d2hpdGVkbnN8d2hpdGVkbnN8MHx8fDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[slipstream-ssh]
slipnet://MjJ8c2xpcHN0cmVhbV9zc2h8c2xpcHN0cmVhbS1zc2h8c3MuaXJhbm1vdG9yLmJpenw4LjguOC44OjUzOjB8MHw1MDAwfGJicnwxMDgwfDEyNy4wLjAuMXwwfHx3aGl0ZWRuc3x3aGl0ZWRuc3wxfHdoaXRlZG5zfHdoaXRlZG5zfDIyfDB8MTg1LjIzMC4yMTkuMTY3fDB8fHVkcHxwYXNzd29yZHx8fHwwfDQ0M3x8fDB8fDB8MHx8MHx8MHwwfDEwODB8MHx0eHR8MTAxfDB8MHwwfDB8MHwwfDB8fHw4MDgwfHwwfC98MXx8
[vaydns-socks] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-socks]
slipnet://MjJ8dmF5ZG5zfHZheWRucy1zb2Nrc3x2LmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDB8fHwyMnwwfDE4NS4yMzAuMjE5LjE2N3wwfHx1ZHB8cGFzc3dvcmR8fHx8MHw0NDN8fHwwfHwwfDB8fDB8fDB8MHwxMDgwfDB8dHh0fDEwMXwwfDB8MHwwfDB8MnwwfHx8ODA4MHx8MHwvfDF8fA==
[vaydns-ssh] Public Key: ecef7073cd119405e62f1347daa949794193ccd618f0f879fa7c10da37a7f53e
[vaydns-ssh]
slipnet://MjJ8dmF5ZG5zX3NzaHx2YXlkbnMtc3NofHZzLmlyYW5tb3Rvci5iaXp8OC44LjguODo1MzowfDB8NTAwMHxiYnJ8MTA4MHwxMjcuMC4wLjF8MHxlY2VmNzA3M2NkMTE5NDA1ZTYyZjEzNDdkYWE5NDk3OTQxOTNjY2Q2MThmMGY4NzlmYTdjMTBkYTM3YTdmNTNlfHdoaXRlZG5zfHdoaXRlZG5zfDF8d2hpdGVkbnN8d2hpdGVkbnN8MjJ8MHwxODUuMjMwLjIxOS4xNjd8MHx8dWRwfHBhc3N3b3JkfHx8fDB8NDQzfHx8MHx8MHwwfHwwfHwwfDB8MTA4MHwwfHR4dHwxMDF8MHwwfDB8MHwwfDJ8MHx8fDgwODB8fDB8L3wxfHw=
@whitedns</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/whitedns/513" target="_blank">📅 05:31 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-510">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🎁
۷ سرور اهدایی
با تشکر از رسول عزیز، یکی از اعضای خوب WhiteDNS
❤️
#Servers
🌐
Domain:
g1.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g2.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g3.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g4.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g5.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g6.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
🌐
Domain:
g7.rmft.tech
🔐
Encryption Key:
a337e9fa75161c44bebe7d717da36afc
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/whitedns/510" target="_blank">📅 05:14 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-507">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانفیگ تمام سرور های WhiteDNS و اهدایی آپدیت شد
🚀</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/whitedns/507" target="_blank">📅 03:39 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-506">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دانلود WhiteDNS Beta6 از سرور های داخلی
📶
WhiteDNS Beta 6
1⃣
📶
WhiteDNS Beta 6
2⃣
منبع
@link_dakheli_app</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/whitedns/506" target="_blank">📅 18:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-505">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">White DNS
pinned «
سلام خدمت همه دوستان  ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.  برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم.…
»</div>
<div class="tg-footer"><a href="https://t.me/whitedns/505" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-504">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سلام خدمت همه دوستان
ما تا امروز حدود ۳۰ سرور مختلف داخل کانال منتشر کردیم. بعضی از این سرورها داخل اپلیکیشن اضافه شده‌اند و بعضی دیگر از پست‌های فوروارد شده یا منابع مختلف بوده‌اند.
برای اینکه همه چیز یکجا و مرتب باشد، لیست کامل سرورها را اینجا قرار می‌دهیم. ممکن است کیفیت و پایداری بعضی سرورها در زمان‌های مختلف تغییر کند، پس اگر یک سرور کار نکرد، سرورهای دیگر را هم تست کنید.
ادامه داشتن این پروژه و وصل ماندن کاربران، مستقیم به حمایت شما بستگی دارد. اگر دانش فنی دارید و می‌توانید ماهانه حدود ۵۰ دلار هزینه کنید، با دونیت کردن ۵ سرور می‌توانید به وصل شدن تعداد زیادی از کاربران کمک کنید.
domain:
t1.prs612.us
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
domain:
t2.prs612.us
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
domain:
t3.prs612.us
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
domain:
t4.prs612.us
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
domain:
t5.prs612.us
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
domain:
t6.prs612.us
Encryption Key:
71201fedadfbc0b62189c08961bce651
domain:
t7.prs612.us
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
domain:
t8.prs612.us
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
domain:
t9.prs612.us
Encryption Key:
a01c03a340a3e684a2815961e086eb27
domain:
t10.prs612.us
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
domain:
t11.prs612.us
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
domain:
te.link-dakheli-app.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s.o4s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
s2.o5s.shop
Encryption Key:
TelegramChannel@link_dakheli_app
domain:
v.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v3.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v4.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v5.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v6.eshkaftak.vip
Encryption Key:
8705eb75abeedcd99001ef8d01cf9fad
domain:
v.whitedns1.shop
Encryption Key:
c8328f9d541860df1637b9b3ed7b990e
domain:
v.whitedns2.shop
Encryption Key:
7ecd7b6271c47e348f6ab177517ee8fa
domain:
v.whitedns3.shop
Encryption Key:
9d7aedcaf1f94e784a24fdfc1348a337
domain:
v.whitedns4.shop
Encryption Key:
0ce14ab71acebbd46b8129e25593155a
domain:
v.whitedns5.shop
Encryption Key:
2dffd162cb02b278c1ab57ee17fe07ae
domain:
v.whitedns6.shop
Encryption Key:
e32afdaa30ca36ead696cd90d84ced15
domain:
v.whitedns7.shop
Encryption Key:
6394eec942238533798ec7524eb7ea66
domain:
v.whitedns8.shop
Encryption Key:
1c167e9850936655c480e4938b2c5c35
domain:
ob.networks.icu
Encryption Key:
3947d5ac68015a09a53a0b361bd82999
domain:
ts.networks.icu
Encryption Key:
e0e71e667e5dcfe3b18e3bce659773d2
domain:
zw.networks.icu
Encryption Key:
0798c0e8aa05080125e6c65282fd792b
domain:
v.0x0.guru
Encryption Key:
33815e1bcb88873f2199c735828ea745
domain:
v.iranmn.best
Encryption Key:
aaed913b8367fce3e20910472d9e3e2d
domain:
v.kmjhfilterchi.shop
Encryption Key:
4f3d0262ba2bd7cc20b596bdbc77f761
@WhiteDNS</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/whitedns/504" target="_blank">📅 18:08 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-503">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRVOWJwrtsbFcHYNl-exk_Udzd1P9KcrfP3tUHWcHuWsh2YJNTPtXDbbnBUEzGCbrrjdxCzGqTwQxmorf10up12AX12-Y9EQGAIvomTnjAmgpxjGDbFZ3qpF_Rru3MwQjrBG6H0jR-HwL_llUCXQvQNbxtxPA_OzBgOT-7_0SCdsDtzg_tzY8VG_2ra6LKPH5Vbc43pcLETV00qY8a0ECccDKPUcfnjMKMuo-Yd84neGmYKymHapzVF1jv3xjZqXXP4b36kcOJF3iH0uV_n4rSbE-bqqqu4QpUqxFu-8IaAyqDpmfDG70nqBcq5T--_blldChfNXkicdLq71S5SyBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/whitedns/503" target="_blank">📅 16:26 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-502">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/gfzwvtnIobn_rdGTYEdsb1bdbp8w0naofPWx-O0OymL-SdA4zXkY3CwiWVewmBmvHFIcnut4nF0zAIhNJlQIWe6QgKNMObAkENOtjCzWjeU1cM2hsKUggQ9n7Zgegi-xfR6qVmp74Ipde9-duCkOJcWDVAeKmGf7YBD3co614dURK5YmmGEGf1AI_TH162U94PIe9zXg3asUk_MyLAaF3dnYdX4wbwb6wJjSpFQOxJUAlv7HReqU8bV8Py_vBs0PpI4oRDduvLW-t-WZTeOstURLc1T0xuUWZkq1ZjxaxNQko6Ru4JUPWHyjhcNd-7mbQmQ9xokaCy7wdHOOfv7qkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به هر دلیلی میخواهید از حالت پراکسی در whitedns استفاده کنید بهترین کار استفاده از اپ نکوباکس هست   https://github.com/MatsuriDayo/NekoBoxForAndroid/releases/tag/1.4.2  #Nekobox #Proxy #WhiteDNS  @whitedns</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/whitedns/502" target="_blank">📅 12:29 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-501">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/JCWFSE1n__XWrXiL2Y24JitenCwmRjmzImSzZJstaZn1XFQwRxpPJEHVsXNTafaNut1CjzMjwBafJxViF4R8F57zCaONEzmjHOxs35DOLanPI4dyVkcVnqs3Gl6IWVqaMtPm__yiCGB4HVP9WeP4WliuZvf5T1qNQUgxeTGVi_KFPjfe_aG9klvmTuEwbe_Ru1hcXTu2xFnSgPAlPOlGdB7q_tBcXrU8Yhaeb9Kk9DW8uzKAtrFp1a1Oe-2WvEIszodKmKAsFvCt8Hs11_J-nDCg1C_YgUUNbSZ03dXlH78aW4BmYjNHq0LA34mG2m_zlYPlRnGOAnDEH1ggQpzgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/whitedns/501" target="_blank">📅 11:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromConfig plus</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pRm0rQDwlVewC95O83B5zft3b6QkAvhCH_1hqHNXee9Lh0VZkdWjBzxcD2D__38D3lu3eaEr-z31sThXnTyouwVIOBeSs83SphcHKRSsg-a-uuRnuUK83EiqUOFq51uA19n-I2L4DspVg1UjfA4GFHX5gIOOzo_HBC1PC85KKMmDTN8dGjUTSnKmfOCqB2Q96qdN8iS-qjp6dUwzh83TIR1h7LVam4NUtgZ4OY2W29PjNDE_H-4U8mwoY-TOyvPFxmAyAW2OfUvVeznM1KYesJ-Dill79VsmApnL2O1X4HZm0GMc3-0oelmWK-bYo7lWmJvGl5mW0FIBWbIb7UNETg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biFf1_EbYpvqYQmAldRua9bXw9GPt5aDsd2RKEm-dgA0KL-W3gWXVNRPWDpLIK2Q9oA65_MsON2tjwPWDaUezAU2GQo0lwiaKu0zvB0rQr46VX5YA9UkcNm2iXH3pr0VK6M-w2UUJJDoi1GztsBc46-Pm6_9nc8bmHRBZlJ1CrJcXMwo5rWmiBKpqCYareUF2zmuh2NcDCBm0RqAHba05lpkrbzgcYDiWI_QG14Xe3LJg7b47XU3MmicGp25AQZM4rzbPAi3ColSGe_LzRZoyeorrdKn91x1I2lGosS7VSRHe3z8O_A7TXU4jdotpVum7CfCZ3oV3v_1qdip-1gqpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PYiwT345vGCItk54CNzqISX80_6gkRk5Xxxt3h25uA0u0OLhYTp4nlssNWRxrJGol81z-cK-8Z74DJjEBF12QQ18A4wX6cUgoKyH3thVroeDkGjS6fUZGqZdzglAkd-cjaNU1qwonkp_UUxTxfeGwNab8io5jnAgyLeZbmtfcastF5Fvsec1JU6gbX9s1bH_lGwUQPmRgDLqhEqI1dRFw4oatWHnegi89HsZuZPTZwm-tOShUF7kW6pnV1pPLimiZo7ou-GYSYLu2n5z6WkUlvsbI6VuUQXzZ3Bs59Zf5y4rUG7fLqq5XkUYTvYGS0BlSI-LKG39zEuG9QkNGJBGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SEULwpxHEoeazcfQOjUoiyiaALRKZ1T9oaceNUvjoa2USvsx03XBKnqsJnBuEA-LqDSa8V7MC9NKyAmKNQmHn_bQ0Zp01HFnWgJvNVdhnSA9ukbdrHHSkIxRyAN333DUC3pBZgny8P-d25E_p2VQW-lOPvrPlhz45A86WD7-oRNOKGGu3wh0eFhkRWpIv_bghrNJrcvpFtjWoKlh4oQ4k_pj0m147AHy6DB8Ownn_xkzerwPxRPDT4J7vVKgAxMulrQV34Y5xsc18hFx5DA3WJ1Znl6sp9PEGVD1tNjHeztX9U4hCejLobmekwsGvxBeItG_bXjZosbXVpGfv-eRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OYZSSEDieOyNPV98Y6Kk0VLbdMX2Gog5zwjz9pmmxHy_5YDx2Jn6sk68hq7Wr5mdVJYuPgaQCbN9vI6xonOY26kJlg3h3R8Dln9ygzzOBAYWwnUyHa7E3wVk--zP-Vlzsijz6_J16EPBxQ2wfY_H0EIO8ABE84FndfpA0M-gSqyqFVlROLAxB9o1TLGg6lF-AEg9WtPZ0g1KkqshEM9KsEWWjNJtJL8lnKursgcCpvzuUOmyCUXudmWi5ppnYm3ENbbjpQWmTGtU9_X1356tbE74zKNDuKMOx9V68zYhGLkILR-tqsfHz1fvB9OEJFKNtGnXO3SzlavX29JesDy_Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PoVZabqwcJzgTVivtI7aaZ7RtUgLcNU1rtf_Iu1Kr0A-rGG_k_r9L5Zrz4G0fxyqQkiGTt-9Xaid21MrY8JKmr1E89AGe0Qr3U3Fr8KMhpiulPbhZzfBQNeeFS06dD0tCCfoZpaN1cEEQ3W7uQOFF37b2jpcs7cL37JpxYqx7u-boe8yZ3ceeVobX4IH3AMz9wDXBf-GIp6sg8Vha3iUHNpzSxzzor_Z2n4cvR2a27QIqneUNHPk9ujGoNhV-GRNc24Bj-VProuaK3Ab2QOfjpKSXo76QMWohmFSo-I14jPd6kRGn27RLCovrY9Yjn1K5jAJtnsmJUNxfavXZ0kGwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔺
آموزش اتصال به برنامه whiteDNS در اندروید
1.ابتدا اول برنامه رو دانلود کنید از طریق لینک داخلی :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل موقع استخراج:
3666
مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1- دامنه :
ob.networks.icu
🔐
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2- دامنه :
ts.networks.icu
🔐
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3- دامنه :
zw.networks.icu
🔐
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
اتصال برای تلگرام با پروکسی از طریق پورت 10886 و لوکال‌ هاست
127.0.0.1
به پروکسی زیر متصل شده و وارد تلگرام شوید و حدود 3 الی 5 دقیقه منتظر بمانید تا تلگرام آپدیت بخوره
https://t.me/socks?server=127.0.0.1&port=10886
این روش و برنامه برای تلگرام تست شده ولی خیلی خوبه ، برای اینکه سرعت بهتری داشته باشد در تایم شب بهتر عملکرد دارد و سرعت بالاتری دارد. اما در طی روز هم برای تلگرام برنامه جواب میده.
هر گونه سوال بود داخل دایرکت هستم :
t.me/Config0plus?direct
🟢
Join:
https://t.me/Config0plus
جهت حمایت از ما ری اکشن فراموش نشه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/whitedns/495" target="_blank">📅 09:46 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سرورهای WhiteDNS تا امروز نزدیک به ۶ ترابایت دیتا جابه‌جا کرده‌اند.
این آمار فقط مربوط به سرورهای اصلی WhiteDNS است و دیتای سرورهای اهدایی داخل این عدد حساب نشده.
حالا بیایید خیلی ساده حساب کنیم:
اگر هر گیگ کانفیگ فیلترشکن را حدود ۲۰۰ هزار تومان در نظر بگیریم:
۶ ترابایت = ۶۱۴۴ گیگابایت
۶۱۴۴ × ۲۰۰,۰۰۰ تومان = ۱,۲۲۸,۸۰۰,۰۰۰ تومان
یعنی با کمک هم، تا امروز چیزی حدود ۱.۲ میلیارد تومان هزینه خرید کانفیگ را کمتر کرده‌ایم.
برای مقایسه، هزینه سرورهای ما نهایتا حدود ۳۰۰ دلار بوده.
اما اگر همین حجم دیتا را می‌خواستیم از فروشنده‌های فیلترشکن بخریم، با دلار حدود \`۱۸۰ هزار تومان\`، هزینه‌اش تقریبا می‌شد:
\`۶,۸۰۰ دلار\`
این یعنی با یک هزینه خیلی کمتر، چندین برابر ارزش واقعی سرویس به کاربران رسیده.
دم همه کسانی که تست کردند، گزارش دادند، سرور اهدا کردند و کمک کردند این مسیر ادامه پیدا کند گرم.
WhiteDNS رایگان ساخته شده، رایگان می‌ماند، و هدفش این است که دسترسی آزادتر برای همه راحت‌تر شود.
ممنون از سازنده های اصلی پروژه هایی مثل MasterDNS و فورک StormDNS
🙏
این اعداد فقط برای سرور های ما هست و نه سرور های اهدایی. اعداد واقعی خیلی بیشتر از این چیزا هستش.
@WhiteDNS</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/whitedns/494" target="_blank">📅 09:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCVkdmD2igcvK8CKI6Oi-zmTWOFIinHrnxaht1vaqwJBE7a4VhAUbl3ICgY1dgYHYwRsmli2adzQE2Qv8xO_fYqcyNdxZDJo9hPdT1qSB14AkVvsMBFVoklNRhnSvJDwTx0M7zZwWMiots79yH8PgiQzzLdI4E6COYfNafJ4FhL5TPXvD4ICh9JWfXUuhW87Gf4L9brm1eoi8oeFcykPN2Ym8BzueHBL4ASrT26jICU2Ul14uEWcaa4lte72y-ms3w5oQ5fPM6t6OoihxayvSHqlWOjsl5lzW5YuyhdotL62gfJyNm0kDewJvnMCl5MWPzy9JmxQSeJxPiaWpKueiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربات WhiteDNS حالا امکان جدید دارد برای دریافت ریزالور های MasterDNS / StormDNS
۱) وارد بات زیر شوید
@dns_resolvers_bot
۲) متن زیر را برای ربات ارسال کنید
/dns_master
۳) برای استفاده در اپلیکیشن WhiteDNS روی دکمه Copy Raw بزنید
@WhiteDNS</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/whitedns/493" target="_blank">📅 09:09 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-491">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">server_config.toml</div>
  <div class="tg-doc-extra">11.1 KB</div>
</div>
<a href="https://t.me/whitedns/491" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🚀
StormDNS Server Tuning برای لود بالا
پست مخصوص دوستانی که سرور شخصی دارند
!
ما برای سرورهای StormDNS یک اسکریپت تیونینگ آماده کردیم که هدفش پایداری بهتر زیر
فشار و کاهش قطعی کاربران است.
این اسکریپت چه کار می‌کند؟
👇
✅
قبل از هر تغییر، از فایل‌های مهم بکاپ می‌گیرد
✅
تنظیمات server_config.toml را برای لود بالا بهینه می‌کند
✅
تعداد UDP reader و DNS worker را بیشتر می‌کند
✅
صف پردازش درخواست‌ها را بزرگ‌تر می‌کند
✅
بافر UDP/socket را افزایش می‌دهد
✅
محدودیت فایل‌ها و پردازش‌ها را در systemd بالا می‌برد
✅
تنظیمات kernel/sysctl مخصوص UDP و شبکه را اعمال می‌کند
✅
پورت‌های DNS یعنی 53/udp و 53/tcp را در فایروال باز می‌کند
✅
لاگ را روی WARN می‌گذارد تا زیر لود، سرور با لاگ زیاد کند نشود
✅
تایم‌اوت اتصال SOCKS را روی 5s می‌گذارد تا مقصدهای خراب یا unreachable کاربرها را
مدت طولانی معطل نکنند
✅
در پایان سرویس stormdns را ری‌استارت می‌کند تا تنظیمات اعمال شوند
⚠️
نکته مهم: ری‌استارت باعث قطع شدن sessionهای فعلی می‌شود، پس بهتر است روی هر سرور در زمان مناسب اجرا شود
اگر نمی‌خواهید همان لحظه ری‌استارت کند:
sudo bash /root/stormdns_tune_all_servers.sh --no-restart
اجرای عادی:
sudo bash /root/stormdns_tune_all_servers.sh
📌
این تیونینگ جادو نمی‌کند؛ اگر مشکل از resolver، DNS delegation، مسیر اینترنت
کاربر، یا destinationهای خارجی باشد، فقط با افزایش منابع حل نمی‌شود.
ولی برای سرورهای پرلود، باعث بهتر شدن queue، socket buffer، limitها و رفتار اتصال
می‌شود.
@WhiteDNS</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/whitedns/491" target="_blank">📅 08:32 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-490">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروح جنگلی👻</strong></div>
<div class="tg-text">اخرین اپدیت سرور های روح جنگلی از ۵ سرور ۳ عدد به استورم اپدیت شدن
سرور فنلاند
v.0x0.guru
Key:
33815e1bcb88873f2199c735828ea745
سرور فنلاند
v.iranmn.best
Key:
aaed913b8367fce3e20910472d9e3e2d
سرور آلمان
v.kmjhfilterchi.shop
Key:
4f3d0262ba2bd7cc20b596bdbc77f761
روح جنگلی
WhiteDNS</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/whitedns/490" target="_blank">📅 08:11 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-489">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw5WltTzsxqGP_VweVsxvR5DLNki3_VAouXBqNH0fhHcPHK5y6OX3msHzovno58-wAWvtuUCQBg9Y7WVRMo5DiyHyIgPcgFEBiB5qVvVLH0TcRYirWtLWJB93DoXbgE_vUpEed3FLQuDNGpZyxdZeBU6ydLZHRWMkXAnpS-df6DPemeaBoggrKMD054hzxq5EgG3W72Is_HGBt26-ixYbCn277MZFKWJ3ShBNrdfnxdzxTqA9Eh20huXgcQu3uViDNVz1GlCFR-0Lad0Z5VDLCUKWSvR3kmVKJeic-vP7i_-00cw61chLhhWRavwEKo5MKzyk1351XhgcxMPeaSCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به همه دوستان
🌐
برای دریافت آخرین آپدیت‌ها، آموزش‌ها و اطلاعیه‌های مهم خارج از تلگرام، حتماً اکانت جدید ما در X رو دنبال کنید:
🔗
https://x.com/WhiteDNS_Team
@WhiteDNS</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/whitedns/489" target="_blank">📅 07:48 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-488">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد Advanced Settings شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup:…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/whitedns/488" target="_blank">📅 05:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-487">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">White DNS
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/whitedns/487" target="_blank">📅 05:01 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-486">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M35hoDjYmAgCbuXyAo-GLAtFsg-KCMRRuKTRnkYk7FycNRotU72OGF5mP_-c10V1Kcb5zlO8nmE7WSXAymv-HJ7h8Stow82MF22YRPZO1D0tDbzAeQrDHf5gREmp4NM6Jh36vjLAKlke8Ig8uAaphCBxCH1Iu_KwdVncZpMzvhUva1SDVF3_pQVukrQsRThIaMRkCegL2ueBpS9BGgBbkPU3mS1lCGzOpc0qEwnYqbNQ1crZv-CCyqHs8Rafrla6D8-oZaioC93UHyWf3eDBtFH_-p4MPGnyCPLOcA0nOv81cUhJZt-KhaYXwYHfaVNE78gQnn963b-ofEkaugyMFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آموزش تنظیم WhiteDNS برای سرعت بیشتر
⚙️
وارد
Advanced Settings
شوید و این مقدارها را تنظیم کنید:
📌
بخش MTU
🔸
Min Upload: 80
🔸
Max Upload: 137
🔸
Min Download: 384
🔸
Max Download: 1000
🚀
بخش Network Tuning
🔸
Balancing Strategy: Least Loss
🔸
Upload Dup: 1
🔸
Download Dup: 4
🔸
Upload Compress: OFF
🔸
Download Compress: LZ4
📊
این کانفیگ به‌صورت حدسی انتخاب نشده.
ما لاگ‌های سرور در ۷۲ ساعت گذشته را پردازش و بررسی کردیم و بر اساس پروفایل‌های موفق‌تر، MTUهای پایدارتر و مسیرهایی که سرعت بهتری داده‌اند، این تنظیمات را پیشنهاد دادیم.
@WhiteDNS</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/whitedns/486" target="_blank">📅 04:59 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-485">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS_Resolvers.txt</div>
  <div class="tg-doc-extra">8.5 KB</div>
</div>
<a href="https://t.me/whitedns/485" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">۵۱۲ ریزالور جدید تست شده تیم  WhiteDNS
مخصوص اتصال StormDNS/MasterDNS
@WhiteDNS</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/whitedns/485" target="_blank">📅 02:44 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-478">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخدماتی حامد📱📶</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ejMJUMHzLDGywdruwTtkx15JNWirf0kIJrQhCzyHnXMCuQd5CyHEXpXCSKqKNG4n2GRh-v2HSS_3MA-bsnKs1tEOpTXIWQDUvIdvtro99Lq0pfSX8T00iymRtpGnV3JP3sxEIwsfmpxc6p4Ulm_GhLAXNovkHhHQhFVFIUq2jxqapNWyhBZwtC0FYBNKCcl9jBpVw77vF2EOfj7c-c7WSHaj44xvNR0_TiOPXKw4VYwaC8LK3u5hBIJrzqFBqG2vI52kyE30X13bapKkpJn80wSUmoXCLPsglJafSLphFum2FyNZoGdrpT9hFMP6PYg2KmzEg4JQrmTPdOQAz4lyqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OSaWy9mXnUJspc-E9lYGJX-ob4Ap8KYNPAzV2OG5kCzuMEn30Rh3JXBOJQmpPvtrDgOFaQ1B5PjFazeMP8TRQiO-xr31yRpCe8vp4cx6g3IUImzTwJ_6Hzeltd9T1GevPGPZxM3Dhk3wzVa9motX59cnhv2C0uYheW_M-K7yXppzAtYZ0zE1aqEo9n-t_RRWFJuP0W2TNIVTizt2iJj0RHZDXTgvpezutam6lmS2gKhqNJxmD-EwAhL8o2joZtPqQBKANASJnIkeoi10idqtX21FScSZRb0Kt3OOLA1LEFbsE9lbQuGIkSxx4nhEFX5BopYbvkqBug0w8HwQf0nzWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiHJFF_JlP-Lib_ygjND47pzRto7YWo35-RRQVQ9Tnih_Isb8qwN9PUVUBZ4VbMIC-AaWuUA1lRtvKR2IIWrBQFaU2TUL7KUetcoo7i4XGp-abmXoE6xeHJHkJidacXaJb7YNQcIYlfr378lvg2m16n0N7IxAabssqzXJ3nyJaJs61jWZGuv7xsI31ktBYGSiSu7GVro8kpC7L91E9-KvcGO9hdx6Gb2R1tqrvHA2sNPbsjdcBpPgeIuZcEqFH-l10z9D0j6d0_nfKGXaclAJ77Zs1dwea7JAV07Psqg42w0RCwIHOA9QscTLqDR5V3EjHN40-GX5RwZKwJ_sAfJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kPSFkBsk88vevzqJPpMDblp_sk-ZCV-oSQewWJ-iiLm-TDhZctoN3js4W2V068kUsOUYQT7LAD679hl17x6uHBWJhh6Rx4lDofeUjJO_CQurIKIDvphpWo7Pw_koWOKj5cZuqfOJRxtoKPdEuSZdOUWqGBPOlVKhCt4Mv6wYNvSVdG3QvOx2p21Fdp7W1rRjlduuY0bVLcOJwgCUP6qX_eRJ71mljIHofP7IyuNAuPCznT50EBF-SBmz6ZKpciG_5xemj8wXenN1qfmj0cP6NiGBW6YbOV4CEcLSx5yK6NI-Hy1YZ_PiTfGwsAdcYiJhouEf-3uPW5WKPwxXnj_YPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X4RFNhWaoiqaOG8CmKH3ilteidiV3Idy85MRWkcyRPy9X84m9U8oIznfhlDIlTtcwyo4ZA3yeTcOF4zFRfjU5iQnLYerFAwjS_eZuc0nhDSCkQ7TLi43dpJMaDNESYA7lpJELahOLqHf_06qornd7zfO1gJFuSarbAvYcAqtNB9RRal_f6_5L-ysE_gkZGG8SzzbmZOPq5sD2s1tB2xssBXP6SEOoUzVHGipIREql2DNxr33LVbWx0lwAQYhwD4wjGl_OmhaxJLdjxBsWgvjF97tqEBp-ky6gaJ6C_FoGIrUH3N2-rBqCEkld9iqH66m7tY6nb-Qqg-s7dZoxWCZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnuICg5cFGtNE2s2xhE7r4Qzve526pEo0x5KPbTo9Asm_LqwnkOdAyzv2_1CjVAHJTbqwr0IraA6IGu3gyEgN2-Vpb0uXbRXQluiH6bo6d52olT1042M5bVt4eNhTfJ3BoYyS1zzQLELiHAkjRPO-kezIK3xKy1GVAdlkiJ9ox0VKVbG2G5R3wj1Sbtb9qUm3ceXXewGCMnnLLEaSzeFZzXz6auscyKtJkzKZCEr2BF9PyB5442cki39rvp87Q_bL9Nv5DHC9CNXvBgzlTX790w1JJZlPkV69Kt6m5J-0nH21QOhZig9ATlcrtqgr__qWEB-ezVh_xKlzSmouaSIMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش اتصال وایت dns در اندروید
1- نرم افزار را از آدرس های زیر یا پیام بعدی دانلود و نصب کنید. (White DNS)
لینک شبکه داخلی (بدون نیاز به فیلتر شکن)
https://dl.toolschi.com/view.php?f=48c485b41de6bf08.zip
https://guardnet.ir/f/Universal
رمز فایل : 3666
2- مطابق تصاویر بالا کانفیگ ها و ریزالوز ها را وارد نرم افزار کرده و تست کنید.
کانفیگ ها :
1-
🌐
دامنه :
ob.networks.icu
🔑
کلید رمزنگاری :
3947d5ac68015a09a53a0b361bd82999
2-
🌐
دامنه :
ts.networks.icu
🔑
کلید رمزنگاری :
e0e71e667e5dcfe3b18e3bce659773d2
3-
🌐
دامنه :
zw.networks.icu
🔑
کلید رمزنگاری :
0798c0e8aa05080125e6c65282fd792b
برای دریافت ریزالوزها از ربات زیر استفاده کنید :
@dns_resolvers_bot
اتصال این نرم افزار در اندروید روی پورت 10886 و لوکال هاست (
127.0.0.1
) است.
پروکسی تلگرام :
tg://socks?server=127.0.0.1&port=10886
‌‌
@hamedvpns
☑️
لایک   |   Like
👍
❤️
اشتراک بزارین   |   Share
⭐</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/whitedns/478" target="_blank">📅 02:00 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-477">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/whitedns/477" target="_blank">📅 13:21 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-476">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HwRxKP2QR4Z8awV3mm6HPbfYrDWHCQz8IP6xZkzo3iMPC_NArdl59GKK9kCTVJgeN1ym1memuXIJt_WHWA7HNS06Vfoxkep48esw912cTkfGQyhDF9fn3PDIyD-KWu_vF_fvv0VUGVaZEmuqUkW4u5soTQPA0nBytNYJ2eNzjXntzYX5bdp-w-2Hv-D2r0YEtEAe8o85ZB-3ZoEiD6jVgTT7GMEj0XMKnwRlunIm0Kzo74glDEDjtqncgDoRdgU-9KSeOmWt52TU8G93ZyJwuP4b1ZEAA6fgpODYwB0UPse_Bg1-_q1dhavMfu-sXjG8ArCMZrxv2hVtPbFPeXqimA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان سلام
تلگرام قابلیتی به نام Search دارد. لطفاً قبل از پرسیدن هر سؤال، چند لحظه وقت بگذارید و ابتدا در کانال و سپس در گروه جستجو کنید.
تعداد سؤال‌های تکراری به‌قدری زیاد شده که دیگر قابل مدیریت نیست و واقعاً آزاردهنده شده است. این روند فقط زمان و انرژی را هدر می‌دهد.
زمانی که باید برای کارهای مهم‌تری مثل توسعهٔ اپلیکیشن‌ها و بررسی موارد جدید صرف کنیم، متأسفانه مجبوریم آن را برای پاسخ دادن به سؤال‌های تکراری و غیرضروری اختصاص دهیم.
اکیدا از پرسیدن سوالات تکراری خودداری کنید
@whitedns</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/whitedns/476" target="_blank">📅 13:12 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-474">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8UHjC8brbqmt-J9pf3Iyv1a1cRyyFPeTid8MxzZI4gJKRS1QvGIgUpq0o15vg2C_otRLJx_OW50kC-wUG2zBQRHU5fCtV1YnsqRHUExngjV-TColxmYmX5vaH-UQ_b9fiz1u27nTngLUcFXW4DMXkQ2q245mJvRQ_KOc7MQgxL5unzOk8UaZQBRhBkAz2VPf5EkuREtxuCTP8Nr_0ee_IiH1zO4FMhCvliw3bO0zOCWwv7u_28ZLwvRU_JehKf9UmX4MC2R3wKnkFAkOVMVFD94c_6pFcZAiBsHWXGCmtD_j1h_2UHOeBNSl5l9TcnM5iMRTy0eBM-eBFWt71PYGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LoeW2NHTlbP0xqJQirYeCXBRZfpZsHnY_597zVFnwTonr7SgPnTdgVYUMNTr97vrI_dt2qRmiu8I8mf8jCUDz2O9FuYw-J5G4HrEiNbzgNeGAjRUWtri7ToMR6j3xHwSyx3ETsdk5FhHlnptuTgQe5we9VqfQxplpjrCYPlso9tzvAkUztjajTF-LddS0jB153BBXshCQhYlQx6HF6utUIbM-V2t-Q-QOPNkJtB8jxt9dcJS6lU05fF6NTBBhk6nnx77ANIRNbHJ5yLiCa4LcNZU0IigrM2D0a5W7w8Zl4zAQtv4zupOKv9aqkH8XGfqE07x_u6-KjM9VxYECsNL6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت ╰────────────────────────────╯  01.
🌐
Domain: t1.prs612.us
🔑
Encryption Key: 3e80a0eb3e1fba2bf17e0e0eb5783dc5 ━━━━━━━━━━━━━━━━━━ 02.
🌐
Domain: t2.prs612.us…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/whitedns/474" target="_blank">📅 12:31 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-473">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">╭────────────────────────────╮
⚡️
WhiteDNS Configs For StormDNS
⚡️
🔐
۱۰ کانفیگ‌های اختصاصی و پرسرعت
╰────────────────────────────╯
01.
🌐
Domain:
t1.prs612.us
🔑
Encryption Key:
3e80a0eb3e1fba2bf17e0e0eb5783dc5
━━━━━━━━━━━━━━━━━━
02.
🌐
Domain:
t2.prs612.us
🔑
Encryption Key:
afc1bd5e98cd98cde7515adb7295122b
━━━━━━━━━━━━━━━━━━
03.
🌐
Domain:
t3.prs612.us
🔑
Encryption Key:
8786a860148e2d4d55403ae3c80ba854
━━━━━━━━━━━━━━━━━━
04.
🌐
Domain:
t4.prs612.us
🔑
Encryption Key:
943664f15fd1763e242ce12ba993d9c9
━━━━━━━━━━━━━━━━━━
05.
🌐
Domain:
t5.prs612.us
🔑
Encryption Key:
6a9ab24a8bd3937378efbfb3c23e1358
━━━━━━━━━━━━━━━━━━
06.
🌐
Domain:
t6.prs612.us
🔑
Encryption Key:
71201fedadfbc0b62189c08961bce651
━━━━━━━━━━━━━━━━━━
07.
🌐
Domain:
t7.prs612.us
🔑
Encryption Key:
c4ff91174a79e9e03a4d6727878ada17
━━━━━━━━━━━━━━━━━━
08.
🌐
Domain:
t8.prs612.us
🔑
Encryption Key:
ae5db6f03e485214e1fcc9d26a4c0a2f
━━━━━━━━━━━━━━━━━━
09.
🌐
Domain:
t9.prs612.us
🔑
Encryption Key:
a01c03a340a3e684a2815961e086eb27
━━━━━━━━━━━━━━━━━━
10.
🌐
Domain:
t10.prs612.us
🔑
Encryption Key:
f3a3c5d02bb7ce04f6a4f144fc35e9cb
━━━━━━━━━━━━━━━━━━
11.
🌐
Domain:
t11.prs612.us
🔑
Encryption Key:
e7f2db07e778563d31ed1fc80d5fe612
╭────────────────────────────╮
🚀
Powered By StormDNS + WhiteDNS
📡
Stable • Fast • Secure
Configs by
@PersiaTMChannel
@WhiteDNS
#Servers
╰────────────────────────────╯</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/473" target="_blank">📅 12:20 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-472">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGLYmBTsQGCpJoCJYsUGT4J8taHOKLlPUFIJq7ARpAD46_FYW-pwdiRYUjfrdPuLVT-UvN7DHQmFQb0cCs6HxTwqjQb-KsKAwgKvhpoym2DjYa_1RfjcrOTJp7GHTEjSzwSpNYNPtCJMixpTQRX-Gib1BnnX3wfflk2HGcQBEpnpHB2TOijHwkC49ieGcKZEWLPquZGa5ygNKxHNc4S3c4AQ3NwPHrOE8kyn0mX54KFexy7zjwtLnCDyGlcTOJePdmNg6kKnOMY-7MRsDfeS2QAMlGDBSWsm_3C9nSybMoro-4XfI_90ikPagG1bhAzcjSeBLSkxa08NZ9aqwpy4VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">WhiteDNS روی گوشی مثل «کلاینت» کار می‌کند و به سرور StormDNS/MasterDNS وصل می‌شود. چون این روش ترافیک را داخل درخواست‌های DNS می‌فرستد، برای اینکه روی اینترنت ضعیف یا پر از قطعی پایدارتر باشد، بعضی پیام‌ها را چند بار می‌فرستد.
Upload Dup = 3 یعنی وقتی گوشی می‌خواهد داده‌ای به سمت اینترنت بفرستد، همان داده در مسیر DNS تقریباً ۳ بار ارسال می‌شود. سرور معمولاً نسخه‌های تکراری را تشخیص می‌دهد و فقط یک بار به مقصد واقعی می‌فرستد، اما حجم اینترنت گوشی قبلاً مصرف شده است.
Download Dup = 7 کمی اسم گمراه‌کننده‌ای دارد. یعنی خود فایل دانلودی لزوماً ۷ بار دانلود نمی‌شود، بلکه پیام‌های کوچک تأیید دریافت دانلود چند بار فرستاده می‌شوند. ولی چون هر پیام DNS جواب هم می‌گیرد، این هم می‌تواند مصرف اضافه ایجاد کند.
نتیجه: این تنظیمات می‌تواند مصرف اینترنت را خیلی بالا نشان بدهد. مخصوصاً با مقدارهای فعلی مثل Upload Dup = 3 و Download Dup = 7 و اندازه بسته‌های خیلی کوچک، داده به قطعات زیاد تقسیم می‌شود و روی هر قطعه هم هزینه اضافی DNS، رمزنگاری و تکرار اضافه حساب می‌آید.
برای مصرف کمتر، معمولاً بهتر است تست کنید با:
Upload Dup = 1
Download Dup = 2 یا 3
اگر پایداری هنوز خوب بود، همین مقادیر مصرف اینترنت را خیلی منطقی‌تر می‌کنند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/whitedns/472" target="_blank">📅 11:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-467">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteDNS-Beta6-arm64-v8a.apk</div>
  <div class="tg-doc-extra">22.2 MB</div>
</div>
<a href="https://t.me/whitedns/467" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سلام به همه دوستان
نسخه WhiteDNS Beta6 آماده دانلود است.
ممنون از همه کسانی که نسخه‌های قبلی رو نصب کردند، تست گرفتند، لاگ فرستادند و با فیدبک‌هاشون کمک کردند مشکلات رو پیدا و برطرف کنیم.
لینک دانلود (Universal) :
https://guardnet.ir/f/8f0ef50b3049
رمز فایل:
3666
در این نسخه تمرکز اصلی روی پایداری اتصال و رفع چند مشکل گزارش‌شده بوده:
✅
نسخه اپلیکیشن به 1.0.0-beta6 ارتقا پیدا کرده
✅
قابلیت HTTP Proxy اضافه شده
✅
حالا علاوه بر SOCKS Proxy، می‌توانید از HTTP Proxy هم استفاده کنید
✅
صفحه اتصال حالا درصد پیشرفت را هنگام وصل شدن نشان می‌دهد
✅
هنگام اتصال، وضعیت بررسی Resolverها واضح‌تر نمایش داده می‌شود
✅
بعد از وصل شدن، تعداد Resolverهای فعال و سالم نمایش داده می‌شود
✅
امکان دیدن و کپی کردن Resolverهای فعال اضافه شده
✅
وارد کردن Resolverها بهتر و دقیق‌تر شده
✅
حالا اگر Resolver اشتباه وارد شود، اپلیکیشن بهتر آن را تشخیص می‌دهد
✅
امکان Import کردن لیست Resolver از فایل اضافه شده
✅
5 سرور عمومی جدید به مسیرهای داخلی اضافه شده‌اند
✅
پایداری جابه‌جایی بین Proxy Mode و Full VPN بهتر شده
✅
اگر اپ را ببندید و دوباره باز کنید، وضعیت اتصال فعال بهتر تشخیص داده می‌شود
✅
نوتیفیکیشن اتصال بهتر شده و وضعیت مصرف دیتا را واضح‌تر نشان می‌دهد
✅
هشدار Full VPN حالا قابل بستن است
✅
آیکون اپلیکیشن به‌روزرسانی شده
پیشنهاد ما این است که اگر فقط به تنظیم پروکسی نیاز دارید، همچنان از Proxy Mode استفاده کنید. حالت Full VPN بهتر شده، اما ممکن است روی بعضی دستگاه‌ها یا بعضی شبکه‌ها رفتار متفاوتی داشته باشد.
همچنین اگر سرور StormDNS شخصی دارید، بهتر است از سرورهای خودتان استفاده کنید. فشار زیادی روی سرورهای عمومی WhiteDNS وجود دارد و استفاده از سرور شخصی هم برای شما پایدارتر است و هم کمک می‌کند سرویس عمومی برای بقیه کاربران بهتر کار کند.
⚠️
این نسخه هنوز Beta است. یعنی نسخه نهایی نیست و ما داریم با کمک شما قبل از انتشار رسمی تستش می‌کنیم. ممکن است هنوز روی بعضی دستگاه‌ها یا بعضی شبکه‌ها مشکل وجود داشته باشد. اگر مشکلی دیدید، لطفا از بخش Logs خروجی بگیرید و برای ما ارسال کنید.
#WhiteDNS
لینک کانال:
https://t.me/whitedns</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/whitedns/467" target="_blank">📅 11:22 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-466">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(سال گودمن)</strong></div>
<div class="tg-text">📣
تمام پروژه های به درد بخور برای دسترسی به
#اینترنت
همراه با یه سری ابزار های دیگه:
💎
پروژه آموزش تانل گوگل به vps
💎
آموزش کامل slip net برای سرور
💎
آموزش متد MHr
💎
آموزش نصب تانل به گوگل(خارج)
💎
آموزش متد Flowdrive
💎
پروژه آپلود داخلی بدون محدودیت
💎
آموزش قابلیت های Mahsang
💎
رادار چک کردن وضعیت اینترنت
💎
پروژه پیام رسان داخلی(شخصی)
💎
اپلیکیشن فیلم و سریال رایگان
💎
پروژه انتقال فایل به اپ داخلی
💎
متود گوگل درایو برای اندروید
💎
متود MHR و بردن پشت کلودفلر
💎
پروژه گوز مشابه MHR پرسرعت تر
💎
جلسه آنلاین با نت داخلی
💎
بالا آوردن کانال های تلگرامی داخلی
💎
آموزش متین برای Mhrv
💎
نسخه جدید اپ vay dns
💎
سایت رایگان فیلم و سریال
💎
پروژه vps شخصی با mhr
💎
اخطار کلودفلر
💎
پروژه تلگرام داخلی
💎
پروژه وایت dns
💎
پروژه های عزیزی
💎
پروژه Mhr روی اندروید
لیست بروز میشود
🍿
@xsfilterrnet
👑</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/whitedns/466" target="_blank">📅 10:49 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-465">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin SenPai(᯽マティ️️ン先輩)</strong></div>
<div class="tg-text">☠️
آموزش ساخت متد MHR با گوشی + کاهش مصرف ریکوئست های گوگل
⚡️
لینک‌های داخلی جهت دانلود:
https://t.me/MatinSenPaii/2969
لینک پروژه اصلی:
https://github.com/therealaleph/MasterHttpRelayVPN-RUST
⭐️
توی این ویدئو بهتون یاد میدم که چطوری متد MHR رو صفر تا صد با گوشی بسازین، به علاوه‌ی آموزش یه کوچولو کاهش مصرف ریکوئست‌ها(به نظرم دیپلویمنت بیشتر بسازید راحتتره)
🚀
لینک‌های دانلود با نت داخلی:
https://t.me/MatinSenPaii/2969
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
این ویدئو هیچ پیش نیازی نداره
✉️
تماشا در تلگرام
📹
تماشا در یوتوب
💰
دونیت</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/whitedns/465" target="_blank">📅 10:41 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-464">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet(مایلز گودمن)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PysBTQWnmmNTzIiwJo798w8n31INBjac9JZYV2vOMXmTCevTbcW_FVk0CiIDv8OuMos-t5aDLcmUgOegBHkvqQwIa-WTY1mZKVrzob0-2I1bqca0SfLqTijUVhwB_7jx6BepDfnIse3tZfpFNRp0es2J3XSbGc1I1Habplxl8Bzpv4JEj-r6OEoEbTtKaPbCIRFO1_B8BxchFaTE-oPi3KKeOV3c-t907bVlneMWBrRYfc8UPID0OigTC0bqvR1V2s5Af7KJWy4-c6KzYpCO2CqMM67hzVdu0ki0cHyFF-9tNlb_oRR9x41kxU8p1dov-O0w8O1USQDmj5nqY2xFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پروژه AzuDL - GC2GD
پروژه AzuDL - GC2GD یک ابزار کاربردی برای دانلود فایل‌ها از طریق Google Colab و ذخیره مستقیم آن‌ها روی Google Drive است.
💡
با این ابزار می‌تونید لینک‌های مختلف رو داخل گوگل کلب اجرا کنید و فایل نهایی رو مستقیم داخل گوگل درایو تحویل بگیرید؛ سپس با متود MHR فایل نهایی رو دریافت کنید.
قابلیت‌های اصلی پروژه:
⚡️
✔️
دانلود لینک مستقیم روی Google Drive
✔️
دانلود ویدیو و پلی‌لیست YouTube
✔️
انتخاب کیفیت ویدیو
✔️
استخراج فایل صوتی MP3
✔️
دانلود Magnet / Torrent
✔️
دانلود چندتایی یا Batch Download
✔️
تشخیص خودکار نوع لینک
✔️
نمایش نوار پیشرفت دانلود
✔️
ذخیره تاریخچه دانلودها
✔️
مدیریت فایل‌های دانلودشده
﻿
🚀
ویدیوی آموزشی پروژه در تلگرام:
https://t.me/luluch_code/22941
🔗
لینک‌های مهم:
🐱
سورس پروژه در GitHub:
https://github.com/TheGreatAzizi/AzuDL-GC2GD
👩‍💻
سورس پروژه در Git سلف‌هاست:
https://git.theazizi.ir/TheAzizi/AzuDL-GC2GD
📌
وبسایت Google Colab:
https://colab.research.google.com
📌
وبسایت Google Drive:
https://drive.google.com
🗣️
اینترنت برای همه، یا هیچ‌کس!
👑
@xsfilterrnet
🗣
@luluch_code
🏠
theazizi.ir</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/whitedns/464" target="_blank">📅 08:59 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-463">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمسیر سفید🕊</strong></div>
<div class="tg-text">✔️
سرور استورم دی ان اس (StormDNS)
Domin 1:
te.link-dakheli-app.shop
Domin 2:
s.o4s.shop
Domin 3:
s2.o5s.shop
Key :
TelegramChannel@link_dakheli_app
👾
کلاینت ها :
1️⃣
MasterDNS
|
WhiteDNS
2️⃣
MasterDNS
|
WhiteDNS
اگه وصل شدین ری اکشن برید بدونم
❤️
✉️
Channel |
@link_dakheli_app
| کانال
✉️</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/whitedns/463" target="_blank">📅 08:27 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-455">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">tele-mirror-win-x64.zip</div>
  <div class="tg-doc-extra">141.6 MB</div>
</div>
<a href="https://t.me/whitedns/455" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📡
معرفی TeleMirror  در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.  این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/whitedns/455" target="_blank">📅 08:00 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-454">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMGEHIXbVE-hk3kFcS3zih7Ai53TPNPUHBpV0lwaAiHAo8woeyQFbgIXPrdWtWCC2hgsXtdqzFZpxDWAB3bMmmgXXY0rXjt7-tykHKCjedt4BO-EozHq2g56_Fw5hYWxurqWQhsuIGjps-OZVnT-opxUOG974YlyU4HmCJP45LQCwR8oiu1uKoXQvFxUZL9NGrKdzkFdmDW_P_1lRt6xEvr6OUgxILGgkxq1k75vOznCc4nu5Or_Sggf02_8kJcM8R4Tdxu4rvUhmC2WtDmrSPdmo-WozPtBaVw6_zX4nT5vndjTnm7yOYVhrgiZxS4nsx8qpoUEl4IyH-VhnPpWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📡
معرفی TeleMirror
در شرایطی که دسترسی مستقیم به تلگرام سخت، کند یا حتی مسدود می‌شود، TeleMirror یک راه ساده و قابل‌اعتماد برای مشاهده محتوای کانال‌های تلگرامی فراهم می‌کند.
این ابزار با استفاده از چند روش مختلف برای دور زدن محدودیت‌ها و همچنین منابع جایگزین، کمک می‌کند محتوای کانال‌ها حتی زمانی که اتصال مستقیم به تلگرام ممکن نیست، همچنان در دسترس بماند.
☁
https://github.com/ircfspace/teleMirror
🤩
🤩
🤩
🤩
✨
ویژگی‌ها
👀
بدون نیاز به تلگرام
برای دیدن محتوای کانال‌ها نیازی به نصب اپ رسمی تلگرام نیست.
🔄
دسترسی چندمنبعی
ترکیب دسترسی مستقیم به تلگرام + نسخه پشتیبان JSON روی GitHub برای پایداری بیشتر.
🛡
روش‌های پیشرفته برای عبور از فیلترینگ
استفاده از چند روش Proxy مختلف، حتی روش‌هایی مثل Google Translate برای افزایش شانس دسترسی.
🎨
رابط کاربری تمیز و ساده
طراحی مدرن و مناسب برای خواندن راحت محتوا، بدون شلوغ‌کاری‌های بی‌خود، چون ظاهراً همین اینترنت هم به اندازه کافی اعصاب‌خردکن هست.
💾
کش هوشمند
کاهش تعداد درخواست‌ها، افزایش سرعت لود و تجربه بهتر برای کاربر.
📊
نمایش محتوای کامل‌تر
نمایش پست‌ها همراه با View، پیش‌نمایش Media و اطلاعات کاربردی‌تر.
🌐
پشتیبانی چندزبانه
امکان جابه‌جایی بین فارسی و انگلیسی فقط با یک کلیک.
---
TeleMirror برای زمانی ساخته شده که دسترسی آزاد به اطلاعات تبدیل به یک جنگ روزمره شده؛ ابزاری ساده، سبک و کاربردی برای اینکه محتوای کانال‌ها از دسترس خارج نشود.
☁️
https://github.com/ircfspace/teleMirror
@WhiteDNS</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/whitedns/454" target="_blank">📅 07:54 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-453">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Channel photo updated</div>
<div class="tg-footer"><a href="https://t.me/whitedns/453" target="_blank">📅 04:37 · 17 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-452">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۵ سرور اهدایی از رسول عزیز به کانال WhiteDNS  StormDNS Server Configs
🇩🇪
Germany Domain: v.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇷🇸
Serbia Domain: v3.eshkaftak.vip Key: 8705eb75abeedcd99001ef8d01cf9fad
♠️
♠️
♠️
♠️
♠️
🇹🇷
Turkey Domain:…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/whitedns/452" target="_blank">📅 23:46 · 16 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
