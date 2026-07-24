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
<img src="https://cdn4.telesco.pe/file/uhX2OIq-Rlf5iwctTeAb4K1GY_pzjbQqU5GscHbN_9Znd_o6ELwFVkUKzZ28vSP3Foxz2zMPRvS_77nCyTyibm6SRyJM2gr_anoLzgYJTcLHXwZcB-jI1JyXKXB9KhI_vKy2nSVsxcuf6FdUJeaP_KSCNlDBL-_NdcFhkCsoA7WXGW4S9QKL9vMvqgEUTlnVht9DRniDIVcq0jDfVrmCzEuCRkOWPYX_bJ3XmowA0yuHOZPnf38jj188Oy2Ua3FOevmlqw3t4Xj7DvSMGEGKjntrJkR-Fc12NmjWw1cbwy8sHu0c0ZDbtNDVfmoeupodIeT2Nu-U3sAZP-IKvvIs4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی</h1>
<p>@IranProxyV2 • 👥 1.33K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 02:24:00</div>
<hr>

<div class="tg-post" id="msg-95">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
اکبر عبدی، بازیگر سینما و تلویزیون در سن ۶۶ سالگی درگذشت
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
<div class="tg-footer">👁️ 68 · <a href="https://t.me/IranProxyV2/95" target="_blank">📅 21:29 · 02 Mordad 1405</a></div>
</div>

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
<div class="tg-footer">👁️ 149 · <a href="https://t.me/IranProxyV2/94" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 161 · <a href="https://t.me/IranProxyV2/93" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 182 · <a href="https://t.me/IranProxyV2/92" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 198 · <a href="https://t.me/IranProxyV2/91" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-90">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSV2VcdwddfQgxAmZFCeaOtCkj_HjFxmG48HURymrHs5j1dqSTopGJYyporx3MuH5IpdTiJo3bHS9IdqCHESv1HNi34S0mo89npMVJUb76-ZPkFwTxB7qKMDTlVJ_KjD_JXa_3yHO_ih34jXSnwQvCoqdFc7U5PnqV4LCEwhR0mPYzECpOKZII5RRqXz_oie6i0zoFX7unPcxafkxs1JX0gUAgBa-G3v8-xhtrV_aHO7mVaricO_X1-9XMivDXc_AzPn4AH4S_UEcn3J7CEoq-_I4cCnAbdjXaDLSRQ8RhJwvOzgDk7H9JTD1_AdTbM5nfnS-ML8aUgDSUcg0Qmirg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 181 · <a href="https://t.me/IranProxyV2/90" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-89">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsDJbc67IEdActKgLi_pFfN-UTBYRMNAm557cOFOg7wVvzOma2k-mEP2f5GeIvKLJhjCW5J2g03xE3alIvCcMxNq6Hg6PfFJ6rNSfVJorXcNN36FjadcWFZfF0JIv3TLShh2m_q6mTALmMCh5sdRX_WGBUu4O-nyjz8pHiLoxRSg0DjC5xPVa71ic2R_ZDztWMEKqMQ4Wi5qK4hhFF1Af_KWMx1AKBZ6oplFbdEYq_X5HNqFN8QjgeiScSSlfejsSLkjIRRgzGNlnsnI-0wjnFz5kxQPjBIfOjHbYPm-K6oox5BxUmdkzgMLZaLeU_V1jWWjr5Kvh66tEMBFgKcPKw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 178 · <a href="https://t.me/IranProxyV2/89" target="_blank">📅 23:51 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 174 · <a href="https://t.me/IranProxyV2/88" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 169 · <a href="https://t.me/IranProxyV2/87" target="_blank">📅 08:58 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 204 · <a href="https://t.me/IranProxyV2/86" target="_blank">📅 21:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-85">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJavgRM--46vMJMU88L5anzHo1q8yZsn93ZFJZbbSaYa4A0ptEXnYg8EyQjaCeqtc6Jea0nzXGzynYjKD9hC02AaQpT5Ml9Wrlq4jZ9eX9kt95w-4KcxI4ccQj3wuNInKbGYUXq9bSLzU8koMmFh3f_SFlPCTZe0NSO8pagepNiGAK6WEbWWfjFi64y211EnRl6LK1es8IbtgQqdbasqnKBqNqv4PMHoYj773n_JF5hNMJg92hMnncNLzzn-dy3maeP-ltJ4Wvtwlmz9oO1Ohfq5LIvEVQQWQG9vsxt8EQ78ja7GpI4q7cMUKK587ts8oVtpS8dtoyrf9-7LlOM1xA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 223 · <a href="https://t.me/IranProxyV2/85" target="_blank">📅 15:29 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 186 · <a href="https://t.me/IranProxyV2/84" target="_blank">📅 11:18 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 251 · <a href="https://t.me/IranProxyV2/81" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 243 · <a href="https://t.me/IranProxyV2/80" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 253 · <a href="https://t.me/IranProxyV2/79" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 242 · <a href="https://t.me/IranProxyV2/78" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu-AmIXfzvqtIyDO1ZgM9RzqTzKOIEEO4aZ9A_yIIQhzsu4FJ8SvAO_PnbHfECsx_Dz9CXY8KpVhjdR8pVKl1FTkqgbZtEjushFYQNQ9-YB325wiUkqmFNX7G3nKIQ_KKERPYxndGqye_Frrd_GnOnEdZQyPwRZC63vJ6eI6Y_c7jaY0B0O5u0h4L5CJtp0UvRQ3VHL0JC-Vp4U1HfRhTGxFD2Dq1mR6fR4mjmLRIwxB4RnnN5FpJfdFOtvKdWIkCqhq73wTpdbIbU54QsVVd6P430_HKppFXBOlIYDsiuf-V-MLc4whn3iFPpdbY84LEn4d_Sdswk6MgiVm2uNTIg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/77" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 198 · <a href="https://t.me/IranProxyV2/76" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/75" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 200 · <a href="https://t.me/IranProxyV2/74" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 200 · <a href="https://t.me/IranProxyV2/73" target="_blank">📅 12:48 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 258 · <a href="https://t.me/IranProxyV2/72" target="_blank">📅 00:08 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 224 · <a href="https://t.me/IranProxyV2/71" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 189 · <a href="https://t.me/IranProxyV2/69" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cefwBDKqICu7u4zkchYAAbDEkAaFiCUUbXjRRBsEYa9a1ULDVd7uC53HK_uJLVf0Q6dxaf8BvZ9tvJ0ziLa1rUmlvh0O14cWYPM3ZT_9_hCTSM8UTUig9nLJUgwH6S7G6gcDNQSsWp4ZEMCj70sSEgcgsx8djkhlPIH3KuMFvvaasD9jf91V3QQqAHGxiLGC1kFh3GpHp9_KpyyNMfCAShY0wk25FW2daE0Jz4lcObfZa3d5QEDYayNH3qhhOswmHtlnpwspIoxOOg9Yjja3vPDO-9finXHRY67zRIKVmNtbj7sQZZeg_s-JJrpR5meWVaE79wqjbsFE64I2S3MgVA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 230 · <a href="https://t.me/IranProxyV2/68" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 162 · <a href="https://t.me/IranProxyV2/67" target="_blank">📅 09:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1qlQFqGXsIjMpdSllekW9Y0JMAh3OOKSJhpRm9yYWxObjiA5N9j0REuzYiU0kJa69clQBSxaZTzi3e9fwnGAva9z96we4z-WjtMGi3uj4XUvJNO9ZhqzTYdzdAcG4zvnQlFxjzTq0A3xaQmePlxX97RHxcb-5BYWRwzUDlVY1f6KKWy6kV232rdnf_4PFfLgci2uA8UvRFPbxWOxS0LwdXGk_NhOSuVEWWSGO9O1ibrQuuemM6HIWwsv3GPmaebpXY2e89Thp6f0ZWIw5nF8SXsDdjACCS1WVLRbqyPpQFrok4AqaqHmJjSil1o0JmlzMU2nPZgDBfQN7MncQ1q8A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 202 · <a href="https://t.me/IranProxyV2/66" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 195 · <a href="https://t.me/IranProxyV2/65" target="_blank">📅 22:01 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 204 · <a href="https://t.me/IranProxyV2/64" target="_blank">📅 19:46 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 209 · <a href="https://t.me/IranProxyV2/63" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 210 · <a href="https://t.me/IranProxyV2/62" target="_blank">📅 11:58 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 217 · <a href="https://t.me/IranProxyV2/61" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-60">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET_GHyje4xlZzdcpFL1W3nHN6RM3Ltc4-RsuV1pDQn0p71aNxLclE9sK5lvLuwOvBxT-_eADPK05dTyANdlHNG8sGVVyk0wPFSN1qHXmqthqj0Wcnlf3-O9PykBcNZtYAar6pGfbIVW0Tlzo_hOef5J4e6jGIkT0OIFarxVmL9rgjy7w_TW_cVV6vvYlPDuQrQpTqpONOg7hAISRXnrJgKsvNRGlaMwlYhjcJFoVg2p7ypNG_eDkGgRw5Gadyz_Oa-ORwbiH1RTSmCWLUE3lu6dWIzmDZJhnLmhfpQmcASCqZHi4x2FUuREYk3PBzljh-FXLaq_fGahpRfYzyKZamA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 221 · <a href="https://t.me/IranProxyV2/60" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 211 · <a href="https://t.me/IranProxyV2/59" target="_blank">📅 22:50 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 268 · <a href="https://t.me/IranProxyV2/58" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 273 · <a href="https://t.me/IranProxyV2/57" target="_blank">📅 17:05 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 251 · <a href="https://t.me/IranProxyV2/56" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-55">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AaS0B9Hsm08OS-gXaTRPel9b2YVIWQdClZiPMQLlMxp-CKvOzDYc9qMCWhpVs5iWVJN4XEl0efXljm9smFGrTUPTVoYM822-Y5xbFB8x5POEz_hU_UdTPMinujstxrQaD2Dj4ECK42LkJxfa4i_qkbikY78hmfMjMRXvqQ8BB6f5ADyeX0kgfemKSfGEGlmwHLTuHDxIhbnR5IKP3tK3WfAutKSJWpvnWajKTEmdH3cjIloghy3d5W1ibaJeSBsChDAnJYcuMBGyThvAGwqEJd8VBBgAmaMnHspF-pLyvOSTntfFhP89hpac5IYYlU94hDqWdXeM6B4tnZKEcsdjmw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 302 · <a href="https://t.me/IranProxyV2/55" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 206 · <a href="https://t.me/IranProxyV2/54" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-53">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSNRDkDdZ49PnPb1wm2tdtoUbGELng4CTDKmmSAhQBQjWd5nBFbTLwEt_c-7PlJ7-Tyn7EfgT2nLa12pZEJxwwR1mibaXQeJ7SPbkSSUagzy13PjdRiCp2yLb4Q_1skPlqZMpRYoEBeuqfqwStATWUPZfjYnVfEg1dQRCMgQTamRWC8oATagRRMxQ95pykkOTU9MdBh0ubQ34cVKoTHP8rijqNuTFtuSdMEcYXxS-HHZHKE-b4G_sSf3PmBS5syO8UxbACoAr4c9SVPUGKjZcqOpcgxaQOddQbO4D5_-5UkbU5vuOYmPZsJ5Yoa2lLo9GXqGx9saC9NcVGZ3HBnSvQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 292 · <a href="https://t.me/IranProxyV2/53" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 220 · <a href="https://t.me/IranProxyV2/52" target="_blank">📅 08:34 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 244 · <a href="https://t.me/IranProxyV2/51" target="_blank">📅 22:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-50">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwItOASEz5glvqXgBsiQVuuUKpCONoTKwdrbEOO8iHbxSApTTMMcEuto44f-qFTQX4NeToeU5EgGN7Wrme9wjKUDMOmnkibZNNMiWbRik-17ZqooNr2rarV_ncB3p9g8RZSIoRVt5dhiqHYY7VBYQMrM1AI12TRATFx723XOECoWI_khf_X-QB2dbgWNabZrf5HOWh2iskfqk2xz9UbbRNFJmwJT49E-oS0INLX86DVcrI9yPrQIVqyp_U1IwWSkxD26-04ehP_WRwtwGhvQohFJKoq6Pk6YxAkWFq_Jsju0HGUeiXGYRWntLQAuFHez8YYTX0tj7wUAxboEsBPOSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 237 · <a href="https://t.me/IranProxyV2/50" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-49">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evcjozHpnqHFbVY_dPdPy4e7-7rxGN951wHDNh5v0lZFiqxeCEuKXZPXARm3ObJs_dRTbdOfh3iGSVrpRTHYYKX7ZhfBzILTBzRIpsTkdmUiLPyNT7uGDEQEL66QuuUCgT2hPvuonvXb7PedPxuiwBMRlnaydPhxlSoCmHa_iTUXkQ81eH1hQfzoSMzbY2xI3T3k8K2BKuOBNpuAxDA8rPW8L8ONUx6Z8tVf8QGkwB9Sainj89eqMFe_P3de7iUErGU4NjZu8AIXXvVcMKsxoGsh03Tex6Os84k4p7qBj8dqlhmu_0Yk9VpEXiqlQUwDwpZwcRkdzGEaaywbU0CHmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 208 · <a href="https://t.me/IranProxyV2/49" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-48">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJ4US8XLjPT5i0bnzLHLnhrMe9Hy8gnL2G-lA7P4BUr_f74Lb9xz8g_SjCo-DL2zd3OvMeIHuQXfOubrpFU6vfC18v_kRCkoLubsnBoBTD7yOt5daLxXY4-JF58BTGtPqJAECcdVBJ2qnVyRUzmC4SuKgNbXdAmvWRyDc3RFJ6g8bhbUAhb3b0qreltlj_QWjvICSsPvki0mw_vxcBi1lOa-dKMwVnj6Ug8rE-0qG20jiCwYSgWzsgmWvYKX_TbWDVFZ4nd1Q-SnBlLM-kmvTlOPHQb1ort_AznaN92YOK6zhQIxqbQIXHh8NCFvocZPO3vf886WdOebQkOR46R_Ng.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 238 · <a href="https://t.me/IranProxyV2/48" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-47">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVVxhq3J_rinmy7O-r0aGR4Uprc0g8rFDNtrFFQEd-j3kKbuIenb4zZkfolLGfoT4n403kf5X8eKMNCWI_0j9T3iU3GID-QTHWMDhfw8hf6Lnjf-uSBI6Lp-Nxt2jEC1TEQp5FqZAgMYZ-kjtDGbOxFJSG97a5EEOhKONwos9ks8h4Ie8yt5sNNl-SnC8hGYRyWLgoDEqeXjuaqeE8m-8N5AMX5LIYwURLchp6iaBzHqEtOSqHoNHO-4WTcsXdsGxmzFjkFeXMrrJFy8x8T6U-lu_OGriZSyM0KfyQNMJ7LQXMs518DXztBvygMxME5HKKfANzUyaMQ8zBN_HAGVsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 269 · <a href="https://t.me/IranProxyV2/47" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 308 · <a href="https://t.me/IranProxyV2/46" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 360 · <a href="https://t.me/IranProxyV2/45" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 411 · <a href="https://t.me/IranProxyV2/44" target="_blank">📅 14:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 497 · <a href="https://t.me/IranProxyV2/43" target="_blank">📅 12:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-42">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يك بار برای همیشه غرورم را برای يك نفر کنار گذاشتم او هم نشان داد چرا نباید هرگز این کار را میکردم
پروکسی
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 518 · <a href="https://t.me/IranProxyV2/42" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-41">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظرم هیچ حسی قشنگ تر از اینکه مطمئن باشی یکی دوستت داره و برات تلاش میکنه...
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 546 · <a href="https://t.me/IranProxyV2/41" target="_blank">📅 10:45 · 20 Tir 1405</a></div>
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
