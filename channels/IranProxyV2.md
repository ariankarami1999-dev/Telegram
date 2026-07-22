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
<img src="https://cdn4.telesco.pe/file/BjVlKd7Jp-ocBAbesyEFsILhanEEk27WSS8XR3OGc-l_RcO072Q_IQSI3X_HfDG0Nw-dGXB1rKWNBP1eEhcxSioBy2tSDfH7D3U-IZ4wHfAC4SkaGsq0q-oRr2toqT0IAoEF3ylARtVM1mL1MErQAFC9VF9X_5nGrzf3M-MjtJ11Hq4U7TDYi2aYFSEC7LtDLE8rDmoLs9Lh961cGfOYNl05uR4IqPiJew8JQx06JZqz7mny4qvsZTORQWwBaMB-khfZSPX5CJPUZDtYM9T7CYaQiknnbMenPq9cFcj08iGthKTcDkpNaLCoBb4e5Mr6WvK0d7JiM15ddZZfyVPm0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی</h1>
<p>@IranProxyV2 • 👥 1.33K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-31 21:16:59</div>
<hr>

<div class="tg-post" id="msg-94">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پروکسی جدید
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 78 · <a href="https://t.me/IranProxyV2/94" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-93">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
فاکس‌نیوز: احتمال داره آمریکا یه جنگ تمام عیار با ایران رو شروع کنه.
پروکسی
•
پروکسی
•
پروکسی
•
پروکسی
•
پروکسی
•
پروکسی
•
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
|
پروکسی
✅
با ما اخبار جنگی بروز باشید
@War_Now24</div>
<div class="tg-footer">👁️ 81 · <a href="https://t.me/IranProxyV2/93" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-92">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">پروکسی جدید
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 123 · <a href="https://t.me/IranProxyV2/92" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-91">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اسپانیا قهرمان جام جهانی 2026 شد
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/IranProxyV2/91" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-90">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lwe4YSsTJ0wB3sbuUs4TXyf9DEe300Z2Yn6gmorTDG--DTl6hPNxjqUUze1o-FlNl-9adTiGo7fr2thYtVwvsi7op-JDwU4KISU7FaNkQsS0WdwBS6DSfTWLeHw1KRWTbcswqf0zAkAklWSxt4XU52uoM4DodUav15QjtIfpvpDprlOPNw12DtNUHDIHTAn76PRvYLH7l5RO99xIZDprLEjQVTjeRyvZjr8bfP1j-Rw_PCa1OLVqEuBbXFso0oxmy-ZjoP8bwL8qzPmp7T4xYtDLPuoJTBsYFNim2lLGymnwDN36QsNyRGuMogRk6FpAJ0Ed9LtHZ_N1YD_Y57KjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 146 · <a href="https://t.me/IranProxyV2/90" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-89">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVPsooSk7DVeVhP51EBbXkeUEfRLstMfWVaaSMg_JiH6ImQMxwmO8ZENaNPRImnSAkppZvnBjrto0sGM-uIG2YTvGzZzfaidDs5GjJXf5OaDcnoHbxYBj7tnwe_dIPztPTmraS6hr9qemLtrxtXtl1mmFwvRXsr-t_QcYuiPz8p7206KADoNZ1aiUEVnJ6qLf3R3AGFkIHKW3W9SWuK7Bna0LWJSl1xpo8hvxPYWlUPGCIjAHXMalQZ0eDTqrsYKOh4nmeUrdSeeXDMM-ECjSf0v432ap6nxt9vWKzeGyYan4diwfLGJ1E1LakMgQw99K8trgdNzDHJNflv2aEFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور بستنی
منم همینطور.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 158 · <a href="https://t.me/IranProxyV2/89" target="_blank">📅 23:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-88">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چه حوصله‌ای دارين براى تلافى!
به قول محمود درويش:
همين تورا بس كه من ديگر تو را
انطور كه ميديدم نميبينم...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 154 · <a href="https://t.me/IranProxyV2/88" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-87">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">چطور ممکنه در زندگی از کسی جلوتر یا عقب تر باشی وقتی در مسیری حرکت میکنی که فقط خودت میتونی اون رو طی کنی...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 157 · <a href="https://t.me/IranProxyV2/87" target="_blank">📅 08:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-86">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آدمِ بالغ،
کسی نیست که دیگر نمی‌شکند؛
کسی‌ست که
بعد از هر بار شکستن،
شکلِ تازه‌ای از خودش را
با آرامشِ بیشتری
کنار هم می‌گذارد..
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 192 · <a href="https://t.me/IranProxyV2/86" target="_blank">📅 21:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-85">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDtJIkKGpPQO4qIw_7Nbx8F0HJ_grOY06milwtQRvhnyJk1uesogiglUI-B_0xNPTMYrmBlVlhj3dbGx_DXcqzHWQIga3U3eZxxuDigUY1qqoAt1wRWAL2wEAeHrkpgtApRG8Gx4qIrPM_DUqBU3a8GQmfjT4sKgCwaL_cBLqOw_sHIkvds4wmL4OtuxwoMOZGCROf0C9LLY4wqM6MMS3vq64wkGr9K2KAjN19JxmI7LfpxxzAB_R8MgNdkQF30Pey0a_FAND-udl0Z8FwEncBfdacN8HzYouYeDCEdjXGOCVImGucaG2CaTggCkcwY-WdI_pNaStLV01XAZ63htGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حتی با دیدنش هم خنک شدم
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 208 · <a href="https://t.me/IranProxyV2/85" target="_blank">📅 15:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری مهر:
ایستگاه انشعاب راه‌آهن بندرعباس مورد حمله قرار گرفت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 177 · <a href="https://t.me/IranProxyV2/84" target="_blank">📅 11:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">علیرضا فغانی داور ایرانی احتمال زیاد داورِ فینال جام جهانی میشه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/81" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همه چی به کنار برق قطع کردن تو اوج گرما به کنار
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 221 · <a href="https://t.me/IranProxyV2/80" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شب آرامی داشته باشید
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 244 · <a href="https://t.me/IranProxyV2/79" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">و سوت پایان
مسی راهی فینال شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/78" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV5e_srMaQQ84fWaKaXUMvNJr0cMCjG4YTiz7MMlhR3xof0gu_4DpiReAa-sNIieqZ0cvY2QVpETa5sgYbAtmX5WEXS9z1C8YA6pc0rdk-rtMgdZ9wJrmU89noeC0_eOwHjO6yBPyGcrZwhRZd_zLTrTepsm9UIJKhxJapXlQ1IELT0eXjyC5T4_rgGAT2Q6AqNB5B0JP7bD0-yxBT8j3Z-H_EAzwcqs3yp0RFOynD8p5evE8odSoVKM8x0A1QZxOb9HRg2xT1bGuJ7mjNn2YEJYfxkWgc8-4yKnUcxPk_kthZNPGqyYKGzj9zl8gIH7sps_S6l-d-3TbJ9lq-SH7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی انگلیس - آرژانتین به روایت تصویر:
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 213 · <a href="https://t.me/IranProxyV2/77" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میدونم پیام دادن نوبتی نیست ولی خب باید مطمئن شم تو هم دلت میخواد باهام حرف بزنی یا نه.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 191 · <a href="https://t.me/IranProxyV2/76" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-75">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گاهی لازم نیست چیزی را نجات بدهی،
توضیح بدهی،
یا به سرانجام برسانی.
بعضی فصل‌های زندگی
فقط آمده‌اند تا به تو یاد بدهند
همه‌چیز قرار نیست مالِ تو باشد،
اما هر چیزی
می‌تواند چیزی از تو بسازد...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 217 · <a href="https://t.me/IranProxyV2/75" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-74">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه ۲۵ تیر و شنبه ۲۷ تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
پروکسی
پروکسی
پروکسی
پروکسی
پروکسی
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 197 · <a href="https://t.me/IranProxyV2/74" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-73">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اگه هوا دو درجه دیگه گرم بشه انبه میدم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 197 · <a href="https://t.me/IranProxyV2/73" target="_blank">📅 12:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-72">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سنتکام:
محاصره‌ی دریایی ایران با بیش از 20 کشتی جنگی و صدها هواپیمای نظامی آمریکا، رسما از همین الان شروع شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 253 · <a href="https://t.me/IranProxyV2/72" target="_blank">📅 00:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-71">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شنیده‌شدن صدای چند انفجار در اهواز
🔹
دقایقی پیش صدای چند انفجار در اهواز شنیده شد و تاکنون جزئیاتی درباره منشأ و محل دقیق این انفجارها اعلام نشده است.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 220 · <a href="https://t.me/IranProxyV2/71" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-69">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">امروز روز جهانی قدردانی از گاوهاست.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 185 · <a href="https://t.me/IranProxyV2/69" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmvuRCFc0HMoK1wVj7lC8-VA4ocF7d-Y3g5L-0qyRgr5tzLVLiG6RGCPdVZoyqcHAkBvgn0wbrOwahS8GuxERBKoljTZVPV_PeZXE-PlWUBf0-JEO37kXYNFoB2K9DWjSWCKzlsfXcGT8niHsR5pz0VhcoWLKiNdhwDLH23KvzYj6m7mKoToP1wIeTX7BMvA2TeLsy9wTMdz3_jLYffOS7n1Tb7lntEqMdzqdTkNSwZ2quu3DnVTbCAwm0-AuIUOgQ0j-Jp-x8dowuVI1uybjBpjfe49Jln_QGvqz-_QS4V5KiAU2hQACPbebyqjJ-lNW542xTrSrI4YdSmzf4IxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش فرضیایی به سوگ مادر نشست.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 224 · <a href="https://t.me/IranProxyV2/68" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اونارو میبینی اقای رنگو، مردم نمیدونن یک ساعت بعد نت دارن یا نه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 160 · <a href="https://t.me/IranProxyV2/67" target="_blank">📅 09:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf_V04tTYgiqysMFQKsWZFMwIwxaVmhQBIEppIVzEvTMtk0l_TlL2MskTcfxCn96trNg9vM5X3GJeWkt-1kbOEsyTEqXOTtJ7vfLzAXgMkDRmMydXOXGY3l9Unoe0PDbStGev1-2Orwq8e2H08gtuognLXoM5Zlvg2I25uwj043F4i_5Ifs-25WCRk-bjjo9rECdAAFyoPnYKweAjEGr7Et9kgPa1EqXh236MIBEf60niX-ct1UQ342WRVVM6mRp3H7_G8SHosUQGYmLcwDRFk2YsWast72vLShIvLgVebqvgPHaFOgRhC1ioNmE0ulAftC_1sVpgqgaQxOH-eF1fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین:
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 199 · <a href="https://t.me/IranProxyV2/66" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-65">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">درد، یا نابودت می‌کنه یا تبدیلت می‌کنه به کسی که هیچ‌چیز دیگه اونو نمی‌شکنه
بزرگ‌ترین انتقام، موفق شدنه؛ نه توضیح دادن
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 193 · <a href="https://t.me/IranProxyV2/65" target="_blank">📅 22:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-64">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ: محاصره ایران را دوباره برقرار خواهیم کرد
🔹
ترامپ مدعی شد: تنگه هرمز چه با حضور ایران و چه بدون آن، باز است. عملیات محاصره ایران بلافاصله آغاز خواهد شد.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 201 · <a href="https://t.me/IranProxyV2/64" target="_blank">📅 19:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-63">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امیدوارم اون چیزی که الان خیلی نگرانشی
فردا یه "آخيش حل شدِ عمیق" باشه
گوشه‌ی قلبت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 203 · <a href="https://t.me/IranProxyV2/63" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-62">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">در پی بالا رفتن تنش‌ها در منطقه خلیج فارس، باز هم قیمت نفت به مرز ۸۰ دلار در هر بشکه رسید
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 204 · <a href="https://t.me/IranProxyV2/62" target="_blank">📅 11:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-61">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بهترین راه برایِ درکِ زندگی، نه تحلیلِ آن، که تماشایِ آن با چشمانِ یک کودک است.
کودکان، چیزی را که بزرگسالانِ “عاقل” از دست داده‌اند، درک می‌کنند:
اینکه حقیقتِ دنیا، نه در منطق، که در اعجاب و شگفتیِ لحظه‌هایِ گذراست..
👤
گابریل گارسیا مارکز
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 209 · <a href="https://t.me/IranProxyV2/61" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-60">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thR7z0CTIrNeH1IfmxWIKvYnjoKmt_71Trpe2IBfnbt439VOEEmBgZNjxRqq0hezd8fIW-zEWBvULRKv9OIkuzY6Mm4G7QdfVWMHo461cKjugRL4FpV-IN81INWhoHqgUi8h97miIFxLNtSOZqub51MQzgqFSoUPOz0cvawuKInR2GIi7dTwRequURVqUhXc5nXWtGcb-VoyW6ttJRilPBSBgXzAv2niIqJD308ct2GUwK7mxqnVe8eF1h7QcmNnq2PkC6Wm_Bvs9rqmJxQVR8Apmxc6AWf5SaS9Kex2lQDz_QN9cZUKCgfw_m_-ZWLV86TJOzTlqYXZ2LrnsaYRrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لباس‌های فوتبال سال ۱۹۱۴
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 215 · <a href="https://t.me/IranProxyV2/60" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-59">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">در حالى كه تو مشغول بيش از حد فكر كردن و ترديد در خودت هستى، يه نفر ديگه داره بهت نگاه مى كنه و با خودش ميگه: «چطور همه كارها رو اين قدر خوب انجام میده و از پس همه چى بر مياد؟»
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 209 · <a href="https://t.me/IranProxyV2/59" target="_blank">📅 22:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-58">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">کیفیتم خیلی خوب بود اما امتحانش نکردی...
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 263 · <a href="https://t.me/IranProxyV2/58" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-57">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">+ خوبی؟
- آره بابا، یه چایی بخورم اوکی میشم.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 267 · <a href="https://t.me/IranProxyV2/57" target="_blank">📅 17:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-56">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واقعا قدیما بدون گوشی چیکار میکردید ؟!
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 246 · <a href="https://t.me/IranProxyV2/56" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-55">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C369R7_nkH10eyjtaM_4mtdqzQ7UHBXRu09sNSexH1uwGXj_mPcfOhQ2G5jq0hBl9gxFNTcFWmBvzPELr3AgCXIUscTSIGaVg7t15QICuAMkWIFPi5Ozx0QLGshZixQ_0261weFAdR-zAdbg1nU141oQtOhLIFT5WKfxRGhu12drxO7R7LlyHfvlrsKm1DwyQ_UdOeIa1yAeE-hM2KKc9CPRg40I7s9QSafLwEy-C10ufHPbEJytDJQNrLWfxspI-JH2D-FEDoDrx9QtvD_9vAzWx1CeHbAokDXQGoahs4pZ07DGKvHpSWiE4Yg9B9aEZlrm6dMc_WlKxgUk6Bz1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداقت اگه عکس بود :
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 300 · <a href="https://t.me/IranProxyV2/55" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-54">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔹
لیندزی گراهام، سناتور جمهوری‌خواه آمریکا، درگذشت.
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 203 · <a href="https://t.me/IranProxyV2/54" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-53">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8uBMfm8Gg0EtQCzUz7k-Pv4wC80L6ePVsBq_j_ezpeSp2iTU_q6NrRDiJKAouSQWHRoppMkhrIOBkEkhpYqi5kP6kBg4ARf6aZiEBcLPQLJwg3jA5Erekuv6-ufzp6aAXB9_3d1amXz3L1UqtmDeoFN_1TAxdJgTFBQSAeO9OubwRTCT975unZCBaAfPu38gFg6pxyyNsoxiQfMOS1DF2vnccNy3I3vMZdgKU71nPkBnufo3vaK_ujkLMI2ujS-TOZKqHEmS8oRZkRUuJQnGlI5j7ipvrrT8FEUOix4z8PlVVmWLv4ALTbTF9l_xjDmgQcZfzGypaqQgnqc3RuNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شخصی که قرار بود انگلیس رو از جام حذف کنه:
پروکسی‌
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 286 · <a href="https://t.me/IranProxyV2/53" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-52">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">امیدوارم امروز مثل روزای دیگه تکراری نباشه
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 219 · <a href="https://t.me/IranProxyV2/52" target="_blank">📅 08:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-51">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۲۰ دقیقه ای که بین دو تا پارت درس خوندن چرت می‌زنی، بهترین ۲ ساعت دنیاست. اون ۴ ساعت رو از خودت دریغ نکن.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 243 · <a href="https://t.me/IranProxyV2/51" target="_blank">📅 22:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-50">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYzAfLtN_DASnLaVGJYkrNaAsiwGTBrZkii086r7EU7Kb-hngycuMNLo-2GNYqu6kEQz3AH0dvYQeoTDhyZbehBXPFvs1SH1bx2bfglVxBEzrIrLfdAJfJO5hH3lCljp8Jd8wJzaP3EciUfUO9sxQeL8dzRhbbRMflKpS0D1uY4AChsClBuPyg6FpOn1gKF8JN3CRlCgdVKXino9EJNlBQzEDZTBi21McYwHSmdB5QZLz6p13CwbtLuYYM8TnYO32Djjv25vNwaRREWFNfxNjt2Nz7UJJCWXWf6t4TFnV-dS86wzIwOSnslDUCazVVjkMwwL8jegFk8KDLBR-9QvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه شترها وقتی میشینن، پاهاشون شبیه چرخ میشه.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 236 · <a href="https://t.me/IranProxyV2/50" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-49">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfHJLbHIDZBIfrYEp7JOIsuWVYHqADHOFBcmiz-h1sBdIJ-16WGaxqX3orlJUr6rc5Vq4oos5-c3d8IsAFMs9Z6Aq9Rx2bSmmtjagmTsgEfBlttZOHZcc9-PPRhjDS6SdQ7234x2MQ4t_VIjQUdQvHek673rlEmS3hnZZGGfR2Js2_x-SgikAUsJ6Fnv8ngszFjnFf5xfEt_ww0a2S7zTQf7nye2lgs8MumxgRuwiAfRVgA3bFrjUQ2HfVrMuAjSJRWcNRTmSq2VVzTIvfwM03EwJsKcdGsMvD58YxjKrBfhafmvYplDfQjZmlElmbVgndCD3xgHJr2VClT9tOeaxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی وسط درس نخوندنام به خودم
استراحت میدم :
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 207 · <a href="https://t.me/IranProxyV2/49" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-48">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDpJE7gpHJJs63vFIcvxmdhuWE8T_fY_9mQmiMR47mdEgZc19OufG4S76IgV5U_XCazwvioc2owaMeqs1JnKJTDINyoV_Hfyh9nag4C0HRpE6rB3YDtvte1VM9_pRqpJFPspK1Wydo93rC6tdFixaAbWC1bN8gsbCPkH-zabVm49K-ID3HaXloTSfFtlmtXsYBIQwhVxDuWs3uBg6LXJp_AOBWmxvwJ0cqeckzwFNGwGTcW-NiZOrrP8CJETt3A9LQz2fl597YSvLz2BUTobvxCxzqupleqRoGlB6bgNoexjbXpdIYHv1xkGPrD1ak6K3S0l3xD4q6eRCbbK9yNB3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم واسه حس گناه بعد از با دست هُل دادن تو
تنگ شده :))
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 235 · <a href="https://t.me/IranProxyV2/48" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-47">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgE3ah5odv1ytJWYEPKGn1N25yFgekeVj5g93zU_-5LV_nm9mtXn82d5-5572U5Z-HI9Is0Ju_iJG3P8b7jt-63CcDc7W_qXdgErc4KUyQbnPw-i9lBFfPGKZMymMWXrtR5yyn8fJ1ITKCxQWRA7wLeDx3QJPCpwMCEEX0nMJZjGxtpbOBKQyzjVtOrwqqVzpcrkjaCJUHlma2E1LGOuwkUdG84-CNX847ljKWoN_0kvljZbMzyx2QcCUiCltZ98bvO7Avyfd_qwc84IwHwCmNg8kXHVEftASN61i6aEHz1RTdDUf7Vuf24kcMqxTBVrOC5O7VB45mFjfPN4tbiiNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♾
اتصال مطمئن، تجربه‌ای روان با Lost vpn
اگر به‌دنبال یک سرویس باکیفیت برای استفاده روزمره هستی، اینجا جای درستی است.
📣
ویژگی‌های سرویس:
🔗
اتصال پایدار
🌎
سرورهای بروز
📶
سازگار با اپراتورها و دستگاه‌های مختلف
🖱
مناسب برای وب‌گردی، استریم و استفاده روزمره
🔴
تمدید آسان
💬
پشتیبانی پاسخگو
@LOST_VPNBOT
@LOST_VPNBOT</div>
<div class="tg-footer">👁️ 263 · <a href="https://t.me/IranProxyV2/47" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-46">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نمیفهمم واقعا چجوری غذای دریایی میخورید خود باب اسفنجی زیر آب همبرگر میخورد
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 300 · <a href="https://t.me/IranProxyV2/46" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-45">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز گرم‌ترین روز تابستون امساله این پست رو تا پایان تابستون میتونی هر روز بخونی.
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 351 · <a href="https://t.me/IranProxyV2/45" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-44">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
زیرنویس شبکه خبر ساعت ۱۲:۵۱ امروز ظهر :
با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 400 · <a href="https://t.me/IranProxyV2/44" target="_blank">📅 14:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-43">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
طبق تحقیقات جدید، کسایی که دل خانمارو میشکونن، زودتر کچل میشن
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
@IranProxyV2</div>
<div class="tg-footer">👁️ 485 · <a href="https://t.me/IranProxyV2/43" target="_blank">📅 12:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-42">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يك بار برای همیشه غرورم را برای يك نفر کنار گذاشتم او هم نشان داد چرا نباید هرگز این کار را میکردم
پروکسی
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 507 · <a href="https://t.me/IranProxyV2/42" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-41">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظرم هیچ حسی قشنگ تر از اینکه مطمئن باشی یکی دوستت داره و برات تلاش میکنه...
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 535 · <a href="https://t.me/IranProxyV2/41" target="_blank">📅 10:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-38">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Channel name was changed to «
پروکسی
»</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/38" target="_blank">📅 11:10 · 14 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-1">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">Channel created</div>
<div class="tg-footer"><a href="https://t.me/IranProxyV2/1" target="_blank">📅 03:18 · 06 Ordibehesht 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
