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
<img src="https://cdn4.telesco.pe/file/G9J1pBprPfnMwJmOnyULoLmHmz7z3xz5hUj7if8QZkknkFGt6ERC7tv-2NkI8IxSn0-gdKrV0oaz_VZzFNOn8O0LgkjAD78oioXyov4doxVLKnk1BQnzxjYJntsnPXS7YUpTnu36IzjlWzjswFHqnXUxevBq0z9Aq6nlZAT7TKd1BJSpakfL8F9Gqht_ZTFauYkvxNOXntwQIkjG60vvuAw_4S6E2LQxQhtNEEmJgTQVUoSREgHkOTJ-uYjgbHX8QEM13vyUSy7XouhgtP3BE_pnBMVccYxTkTDjY5981FOdUN2qmMAXwRWju0sLrHav6yBKB3XpC-8YQ4Ve_GaRRA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 پروکسی</h1>
<p>@IranProxyV2 • 👥 1.31K عضو</p>
<a href="https://t.me/IranProxyV2" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 18:55:34</div>
<hr>

<div class="tg-post" id="msg-97">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">به مناسبت ۵/۵/۵ روز دخترا مبارک.
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
<div class="tg-footer">👁️ 123 · <a href="https://t.me/IranProxyV2/97" target="_blank">📅 15:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-96">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جکی چان گفته ۴۰۰ میلیون دلار ثرورتم رو میخوام به خیریه کمک کنم و پسرم باید خودش بره کار کنه موفق بشه.
پروکسی
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
<div class="tg-footer">👁️ 206 · <a href="https://t.me/IranProxyV2/96" target="_blank">📅 19:31 · 03 Mordad 1405</a></div>
</div>

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
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/95" target="_blank">📅 21:29 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 299 · <a href="https://t.me/IranProxyV2/94" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 277 · <a href="https://t.me/IranProxyV2/93" target="_blank">📅 21:19 · 30 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 278 · <a href="https://t.me/IranProxyV2/92" target="_blank">📅 12:18 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 281 · <a href="https://t.me/IranProxyV2/91" target="_blank">📅 01:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-90">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdLw0lY0gCoD_SXMqr5oBx2xZMqQudmZx_OSnjrnWLqUPf-lplFhrWQFIcsThiM3NdukFSVuCYa1lDTh5iGmrRncxQFb74vPgontvMQZMPhP6LtqENAwPeLNw0R5reARUBWsGumq5liCmpDn4scYgcPnyP-MxP6m_mKC3ajpkbMmVEs34xBZx0xe5fgq-KTxxlgg9V8ZkBYCqJHU_-LpcuLh8zRXbsg9SvK0bmYfVGIW3GN6ProX8chFoRMAPTJ8H8GCu5OGA_MhN6DrmP8zfJ3tOtUlusgsKz2MgWrz0V4099XmT3nVLytiVTRt52nq3fNv_2GsygMWqSB9YbDd-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 242 · <a href="https://t.me/IranProxyV2/90" target="_blank">📅 16:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-89">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IgsZGgoboKHtVTNsGInB-xoJ7aaB6_daJEv9a4LLtv7mk_jdlvouTINA32JZh0C15OI1Po_c9zWDRSDMcrg7pHpW8RGXYwpyMg_s2IYeHq2xxvn3cn5k2KPist9eJlCr-eACpKiW96AhQR4xJ5KSA454MglMDGGr-F-yyvK5xfqTXEg_SmOrfjBQNIUJSbJlvhxMdHnAcBA_Kiphe82cm_XXIhk-cqLuuPCud9hoMihGlykVgUOoCwuMlg7T7nKfVTTLUjDXDlqHN8NLPWC4-SCrLXvZyun1HriUsNvRNFouFgGT308GRm_FitQLyo3UDnnaFv8PFOcaPba4eYsdYw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 235 · <a href="https://t.me/IranProxyV2/89" target="_blank">📅 23:51 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 213 · <a href="https://t.me/IranProxyV2/88" target="_blank">📅 17:54 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 204 · <a href="https://t.me/IranProxyV2/87" target="_blank">📅 08:58 · 27 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 229 · <a href="https://t.me/IranProxyV2/86" target="_blank">📅 21:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-85">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XblzHAJb5LbRRVGfXSGAaxuBqTEApj5wpj9UF9iIGZFUvxPbl3CWZ0-PrkaEaqayZGUSxkIkzRU1b2qYEZhmH3Wm5Wfv27O2jC3CRkd7tH20pF9L5bxClWo4xm0zc4c1WPiHW_phl184s8iXe0_QBOBJLO_EjSvUAOaAga-x50E7OeUPu7WZszgSFjbldzPIQN7tKiKeeO0_v7U31mJSKQ6TaR53j3GvSukmq4UrJ3F-v30KHaloecb9LOfHd7CxmAi5jJkD5CnnzTO2newWmoH0FCW7iH1D7WceqcVXDYJUIPnRdANdi2qtV5-gzhDvmzmOJs-d-WBsXO8A_b2THQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 268 · <a href="https://t.me/IranProxyV2/85" target="_blank">📅 15:29 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 225 · <a href="https://t.me/IranProxyV2/84" target="_blank">📅 11:18 · 26 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 283 · <a href="https://t.me/IranProxyV2/81" target="_blank">📅 17:34 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 273 · <a href="https://t.me/IranProxyV2/80" target="_blank">📅 13:47 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 281 · <a href="https://t.me/IranProxyV2/79" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 268 · <a href="https://t.me/IranProxyV2/78" target="_blank">📅 00:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-77">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpbftkrSNDFjn3gdtOMMZr2FYwfjcamSLTTlv_gznRRexrTybeBj94071Mz1Os5nxV2PNN6yHrNI2vAKe-fsPfEdTqZyzBYkvOSzWW4a-VRogQsnWQC4jf9R4tDN7BYVhaznErlpHz0hfciUl9BbwgGlrJyv2c5pqJIzWflEilaKUEwP14adBrOigNJaXyQoZWoSsUIXWSRbRBpLrtU2fdZGaioNnZ9C7hxFf-uKNUxluk9BnT6j8V2amdxwbYWcCFX-sAu5ExGbtuFOgmIjA652W2oURKq-tladn7wxitGOsPy7MNOXR7qD94zuKKBigxpZ828sbQSNJSbpcqTq7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 245 · <a href="https://t.me/IranProxyV2/77" target="_blank">📅 23:48 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 209 · <a href="https://t.me/IranProxyV2/76" target="_blank">📅 22:40 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 236 · <a href="https://t.me/IranProxyV2/75" target="_blank">📅 19:07 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 210 · <a href="https://t.me/IranProxyV2/74" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 214 · <a href="https://t.me/IranProxyV2/73" target="_blank">📅 12:48 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 270 · <a href="https://t.me/IranProxyV2/72" target="_blank">📅 00:08 · 24 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 236 · <a href="https://t.me/IranProxyV2/71" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 200 · <a href="https://t.me/IranProxyV2/69" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pldRwQzrq8FZyoYzRpr3q1ryaNjbVEnaxfH4i07WJJHHMfW2E6ebCdjA19aBNwKUXJHRyG9oFaAP8ipElKTZ2bjUynLumnBG5soZIuF2ePZ8ehY1B50JCvP52G7Ljzg8L5M7LeNyc1M7BK8lp7eO4N3CAiWA5_O8eIiMNzqei6VeW_zrPQZ00mXcD1PCjpTLmCOTr5VurZhCrKKqAN13Xan1mRSGDod6CfETHZu1PocyIf7fmrYeFeaj82h3ieGpDnjjwSY-kQsrbVdAC2GiZ2VmwOdDTIBTUkPO8iJpURkdJjhbEjPlh276FUbqMS9fWVxVdXDD1g2Y3Mbdez3-ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 238 · <a href="https://t.me/IranProxyV2/68" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 166 · <a href="https://t.me/IranProxyV2/67" target="_blank">📅 09:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzodaTtD2EDlKi3FfeUVWPZHjFXiSevPFebcTptzOb-9WAAZQz-hhm6q9ZddVDJjEKyYk0BVZ1tRaRYsFN7Yaj-ly6laViK4Fr9_GFyYFaNOb41Wj-bD8tglpflVMafh7-I-OmwyutMhR3lHmFuoDAziUVd_HglkzinutaTqf5y5HJSaz7dXNSxE3beQfusUhRP0GFsVuyYzB1TxhVJDPzGz6RSQjR9dgf9L-iInd9nPDW3R8IC1oz8CiEwExkw3hKKgro1OrdFXPbZMTIZ1cnWMHDonwHSqhv2UVC7z9MYhOywzks8KOdS0vHbumvM-uO9RKzpNbVdhPbFHzxoLNA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 208 · <a href="https://t.me/IranProxyV2/66" target="_blank">📅 00:23 · 23 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 199 · <a href="https://t.me/IranProxyV2/65" target="_blank">📅 22:01 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 221 · <a href="https://t.me/IranProxyV2/64" target="_blank">📅 19:46 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 235 · <a href="https://t.me/IranProxyV2/63" target="_blank">📅 14:23 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 235 · <a href="https://t.me/IranProxyV2/62" target="_blank">📅 11:58 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 232 · <a href="https://t.me/IranProxyV2/61" target="_blank">📅 08:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-60">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWwbBqb047cxo4HSZqRVAZG68Yc-bwyItNPzd1BPg7xKpcEUtgtwjMXnf2hkaccv40gQUYT9EHNFj9upIgKVqFWq6MGKy72eu2ndy6gWts0vtJm_d_W94ld4_K_d9WWyqMeCfe_wrBMloIH6V6KZU99nIQ4AIe2zRtZ7dPJpqOWm3i1qYY4uzEPvsjROTyqs72gaB0L49WNdBAF1POAHB2ijJF44R2XkqYEU4kyjooUK8qJgsTxiZRCbmkMy5BMvn5OZcxRaXBGxvkNQ82uI69LQsrWMm-QlMogm7nN7BDnfrdX5sxyHm8lpaKJaw9idNe7bLXq-hUbssToD3OaXHw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 230 · <a href="https://t.me/IranProxyV2/60" target="_blank">📅 01:08 · 22 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 221 · <a href="https://t.me/IranProxyV2/59" target="_blank">📅 22:50 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 285 · <a href="https://t.me/IranProxyV2/58" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 285 · <a href="https://t.me/IranProxyV2/57" target="_blank">📅 17:05 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 256 · <a href="https://t.me/IranProxyV2/56" target="_blank">📅 15:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-55">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1F3hSSTwjrmIbUejGmy-9wi2174Clxx8ZHEMe2F9iZETXhBUEXCs8DnAlBo8j-o3UaeM6nMc7kPW3fSnZRnHYC2f2iUE3joE3jbQYV4HCFDELyK7d3hxtc8lfko7ndFIwBlSJ2fOXqg3xVzu4QNXx1-9bqo3zCvJtXQZWvfYJLjFcG33UKjL8OfSqmi-jQ9TmXH3amYU6aoBjemHvPSkAmO6cFXJltxypgbhp7WZlil9Tyi83hi5oCzTDhF3gw6HavIJ90M74hLwPPtrVpFvftGhwptHq2Dxlw8ooi1r0V1UVBNWuds6RhcbelFAmqCGZ69pEm-7fmX067-zeGRhg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 312 · <a href="https://t.me/IranProxyV2/55" target="_blank">📅 14:51 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 213 · <a href="https://t.me/IranProxyV2/54" target="_blank">📅 12:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-53">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EA-zUJ-g2Jve3UIb4qK8WzA8Cqv81EnA8_6K9Al1J44fSG4jCK7WVTt8iR9GXAoOCPSuZPsOobxgrMGnp09VOkcdMmDbSkxD1_ah0N77nO74X3jZBDzER5x_kBChnMLSMndUbSqUehfoHnuUlei1ogRAosPTogVfVu2hHx4tPtygeNycAr01bGyJwmhPpCjkIh5QEs34b9kna7JJW2tpmJjhq7wzvCerufUrxFDp_aqyTJyEVFFLMofseuq4FKTBlAdN4oW1yID-02iWlZs-YowtAJ87zYxu0jJtdV9l6cTKA8xUJkl1BwRsBiO5jrTQ1xrl18qipJQIyZ8lk0g7dQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 304 · <a href="https://t.me/IranProxyV2/53" target="_blank">📅 11:55 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 224 · <a href="https://t.me/IranProxyV2/52" target="_blank">📅 08:34 · 21 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 247 · <a href="https://t.me/IranProxyV2/51" target="_blank">📅 22:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-50">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5HhXn2HByxSF9SPMF7yEektH8wEpTIzI-Z5gW2w571fXDZZeYfoDtbruhilq46tksMDxLyPq5qqVNiB_DdCcJppY9R_tml6nCcAaC069OGtOUhaNj5zmjfZ8x1bP1gejm78zDpYL48dDNRK6DXd8mEOpkzTexpn1Htg_ie6iNFB4Ccf3nAXxvllJ5xA9EFuV8DqNHiTQeI6n-kUdWrYtjngA3q3C5-_8HFlNTOMIW-hdWapjab2e7hKIZIHNWz3em9fmGb-xIOuNsXPaikXv5AA7JFJlY0x25UQjFQwD1JBUHh7JEh-0aqHOkU8jcUxEj8Avy--ivkKGGEvSi1Pdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 241 · <a href="https://t.me/IranProxyV2/50" target="_blank">📅 21:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-49">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVzl0phypnkszRDdslo9VXUjYWXN58qJeHyOP8B1MvxxsnF5HH-vYQLEjav-B9vcVBONoRypDIwinEQcleK5yKn3cMFNNGwa91TNqV1wJ30rSs-7kgwXBaTzFgnSIHvcfAh65VpdPwFPkL7g_b0SqkaEsuNpLqfKHkdAse12XBu-MdIXvmJqLLX_gU2ov9b--6jnhqLUu2H-c2KUbeuZkF8fer-aR_SrnhrxjXOC8HRHtl4fMKFhOJxRIscj5OldCXx6qWmtpWPTCYIIxUWxbGIDGSKzqrRTCvl6XBAMIrkJv1EyYXF3oe6t0N4YezcG897ecTQ62-lebH0CV-q2BQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 212 · <a href="https://t.me/IranProxyV2/49" target="_blank">📅 20:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-48">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKxM2Sw7oIb98H2y5jpSbaCEz2UKCIlkhWy4zVSckbyTERIFiLcZOE1Sco1DZIowhLPPjMoFGumjKi0UzR6s_tkTqcVcQlMVowKMI_pbyrlXJddzkDQDEPPnr3QyO9q38uU3Nw6OiMZFyn5XW0vP7HrnbL3j8Conid4OVRWg_xIJg55whphSG90oMTdUsHilUwSf44du-noTMkIFa-NCSG05YuvQsn8RFUiC9tUaIOGbvOk_O0-czykLIb113ZAQZc68wcfb5eIN46FKuLkEMJosUnq3ywpAuWM2gXAtOUOncxtR-_Xd5jOpg7Ua-8bE7kaR3OY1jKF6L0eHGKdVQw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 246 · <a href="https://t.me/IranProxyV2/48" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-47">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jL6mQHvSjMiid20IEdu1v7Z_xxIuGPMom3fDYLuvtuhYHMHpbc3eUBbLk_W8Wke6igLO0U6Az3jCvoHuw8JG1eGftzgeQKHQtzWcTegiJmhEN6MfPg0EUJwnwd_8KCLzkhzNHexXjNForeZYjlFg6IwQ04b_drJMgVszZ8Ba00i38UmPqjPeAKvWKgfepjqZ2Fsv5xxacExCVFKWie-dYC_djC8jHJiu_qWLPw3CldC1Rvguf3GEVlnR2Gg-QhVxIxlKLoM1MMkevaKo0Je-xMHKsWvJo14AEWd4lJXEuWfA_JS6LScgwTJSTWSEq1Afyw9tdi-9x3J8rDeba98Hkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 281 · <a href="https://t.me/IranProxyV2/47" target="_blank">📅 17:08 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 321 · <a href="https://t.me/IranProxyV2/46" target="_blank">📅 16:10 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 377 · <a href="https://t.me/IranProxyV2/45" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 426 · <a href="https://t.me/IranProxyV2/44" target="_blank">📅 14:24 · 20 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 520 · <a href="https://t.me/IranProxyV2/43" target="_blank">📅 12:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-42">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">يك بار برای همیشه غرورم را برای يك نفر کنار گذاشتم او هم نشان داد چرا نباید هرگز این کار را میکردم
پروکسی
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 541 · <a href="https://t.me/IranProxyV2/42" target="_blank">📅 11:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-41">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بنظرم هیچ حسی قشنگ تر از اینکه مطمئن باشی یکی دوستت داره و برات تلاش میکنه...
پروکسی
پروکسی
پروکسی</div>
<div class="tg-footer">👁️ 570 · <a href="https://t.me/IranProxyV2/41" target="_blank">📅 10:45 · 20 Tir 1405</a></div>
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
