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
<img src="https://cdn5.telesco.pe/file/Z94rPtLCt9ntGAgePpfzjchZ_JqVA6gFLKnzwPb3nDFBUWn-8CFcOZ_hGqrI7v92SHOaH-haX17CN7KzjNTijwlSs4YdsIVsMgf2g0igPslQW_M0LlyX129bxZSZBVK2Yht-qWqOss4w-810z4Poit7_Z_wMMk4kJG-_09YypHEYvGDsV7x0wUZRe7zAMPcSiPWSpw4IsTgx9XLrUnZ8AB4XLL4Yovm9GtZ96PABwTcU509d4HPAGs4ff9FSofaVf-33dgWpiEtMG8HA_sbRNFCediNf8beyW7P1W1OoHqb_pnxrWvwv7yQGyGw0VTc-gMmiDhXA52vyY6FOzIDu-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 509K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-102429">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b472a6619e.mp4?token=oHS00TsnqkM_SA1MJRP-pk3yHsZFHF9oR_EwVAVTFqWb6P7bA1iGdGYEXs9OIVF2Nk5F5n81uYs6r-ji5bg3Gy-acOXeJ6Eo3-EJmXIkdBmUusptln6m86OOsljARsTrW6dY4Fn3mkm5cX0VSaKCYJ_PqCFDhVS8qhbqSiJS_441XfloMkDqrUCXh-K_9Z7OQUafUHCFtnMiSc7JJ4NxV1AOcnLtCxU0nWXhpDfAM1inkKhjkfWs5AI5ZiEF0hU2kIq0RewfHg6ZxlS4KD7OqTLLvGSBqRzIXcWRdms5Y6pNMdk2dRSlrpeeBgfs6KnhQgtyIkDtQFvoEB-kJ0ZKjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
یادی‌کنیم از بازی تاریخی ایران و قطر با گزارش جذاب عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 761 · <a href="https://t.me/Futball180TV/102429" target="_blank">📅 16:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102428">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfd29d0ef7.mp4?token=XXBL4ux_HV034ypaftx85bkH8zkZqLF9-88R3IKceiysSy9a3Tbklb8z4tk2n_yloglBOQUZdIFgdNHVqwl-_cLwpaRbPx827QxrQ2GXXX6zj8hC4KuYdmTA4xdRrAJE2jaUvigTYFSWYgQeqmc-nCaGu6iUHqkKsnig0D-Q6To9AvFjGW9ZzoVusS4aOjKzBF0c635u3f-aZDj491VaeXcLkTDCcJo_EkRgaxzN6Q685Elm9y3j-tHQ3qqWic8Nhv_kNBT2vJH8geWn3-_XI66C4MSe-Fv5t4tKp58107HATWbpl7J7r7OjV7dug_q1BZv3oGa9Oz9oBYKenftiHoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیاز بود یه آیتم جدا برا لحظات تاریخی فیروز خان کریمی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/Futball180TV/102428" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102427">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17c8ef3f2.mp4?token=VqAl1faROEG2VGU0ggFZuDFcfB0t6dD1BdEMsbg0uqhUUZVgx5QsEVqgvEYHAwWSwLOvdoeswd-4t0sc1PKOVm110JFrahn6pIQtm9qY_1gXHWBlLoatD1jRaQUlWl-o_4_02LED8_YDwDyw0kDEMR6qeJau1oFWWgnE_n9tlQLoluWoWcMCscLyBdntR-9EL0wJkm9VBjQBGxfyDhFXC0HIvhN2wO4Xn-d0jSN7Vjb_VRm06RFwimxrdEAKXk7yHor4h7MS5j8j3lXjUK8SASnQrg5J4oR6Yfo7sieALFxW5LBHuCAILcwMLux0C--8FE1vnk7zAw-Xr-ZX-HvKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
▶️
رکورد پرش سه گام جاناتان ادواردز (۱۹۹۵) با ۱۸.۲۹ متر ثبت شد و ۳۰ سال پابرجاست. این دستاورد استثنایی در دو و میدانی تحسین شده است. ادواردز در مصاحبه اخیر بر تکنیک منحصر به فرد و هماهنگی قدرت و تکنیک تأکید کرد. او پیشرفت رشته را با شکستن رکورد توسط نسل جدید ورزشکاران مفید می‌داند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/102427" target="_blank">📅 16:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102426">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543e2ce52d.mp4?token=XgIL1xFEgqpFi7MiVK8jmsJLAmswmVSgSCzCqy2FpiAUxuxmPFS6ecLNJAwPzqN9iw5PHVS10tmhMctgIOI3mC1TsuG4EihV2qSEWZb0ZVIVoB_oZYZAiC4CYJRstGvRplGMaCsEb0Ll5RHHOckzmmXD1smMgTE4Xj8TnykCblimnSbT5Mod9Zz91X4l-WbF3kCAMNhzSP5QVF2vuKl7gr-U87oUEC6tTXe73zkwxmpGLLi0DirDbBRKsHP0c1p6UzVz7IEOcSosbqIGlzMEr2fYZCsGnr_VGRoG5gfLRMK41xexJbXeLUy764vdlEYmPN0wlJe3IKrkvJs3n3ilhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو کمتر دیده شده از مارادونا و فن‌پرسی
💘
💘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/Futball180TV/102426" target="_blank">📅 15:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102425">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43f315425.mp4?token=e3UbMDRw95mJIJHS347Jdcjh5XzV3UnN_suk4LRUICTGI6LbeCWYcUEAJel8GnpSpXUxTSvQnvYsFm3JFxHwZa8N7ni3i_MZQH5bt0b5C-tu2NkqwqvIq6XR4ubFNPySfbtoNRnhRmuh7cdUmbNQbxEVsp0B3LSrsMyCsHEDH3pyT7QicYYntnvxSeApbDIOQyAnIVAq0SiSEeCUvP2z4C48zHSI0T9akMRZgTOE102Zlmqs7DsbUH-qjyfX-2tiEBXPtzZ-QS0bjkynuyLm_xYxCi5hOq9JPIvzeZe_JoZel278-a8JEbok27UwgUu0oWt1vEUs4YJ4SRZWaINKIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚠️
تجسمی از المپیک اگر تهران برگذار میشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/Futball180TV/102425" target="_blank">📅 15:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102424">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea1f4ae5ef.mp4?token=r1IHsPWJFEHraRIBXHOeZhfrpP3wiQOX_Cv8XuzwdO7QAvvAy1jjGBJ7B_-_ttxXlAxSBKz_8j_EL2g7XwctrGNLLfU3xfse6Yyg7NgEPwVPFMFQy1T5wfq9XqT-VA815_QCVlFkstJizasppXNM7D0HmTQ9toWXY0rG6xAd5zRfBmsA3BQwqrZCWKqky8zBvcxRY0YWjRHueNhAckrf3Yq48j68kR9SLD_b5pE0Wjt-QQCeoXLiyzJ69ff9EOsybSDjsTOVZOR_V5V89hfJzEwKXEnAjSw_Y7fTnCVGY3spVq2EIaRo1yH0BUrjSVwjFVv-mDXfhI6-GCOQKpSCGnN3_Kt7emR2rbKOccUqylzUyUlAnkeyPs_ZZnVPpJ-DWdPvs76TjDBkFC0pBAbZgc3azO2T9fODosyEYxdYFq0L_CvT2Zn8gBt_yJUV3FFT3MEtRqKJmdHNoCHdygl4VqBk-x0kckRlP9oqyfjefP8qVLn9Mu-jL-Wyo8KDWrgxetyEpeJIWW3_kf8Q1_2CrwK8gL0d1LJLaHHPa1gxxVOA8SzpHYuVvKgLtifUxCVq_nyVDpZT7PwwfE9XMbutgM_jJjrz8s_bQJ1JwqibfDrBR0U5GMtUaVY7ykFURPIZmHfl2R_vHyoz0xdbhZq7U11h2WVfQSw9LGYG7NjCryo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🔥
👀
۵ گل زیبا و برتر اولیویر ژیرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/Futball180TV/102424" target="_blank">📅 15:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102423">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a3bfea056.mp4?token=inBN7lvOH8hovwQv33D0yAb1Cjwh7Qlya4ef-xnuoU6s6MFyqqeRFRV0dukCz-dWIefi0PwBxlZX3w5eG1eDIfHq41V9DcWhI9ZQ0nJZAtO9MtzD_hH_r0pNK1jPJpYUiHPwqfQnYmULn4Gyyiacjac2EhbioHNWwhEdE24vknr_6SOmiZwlVh14yezA0SG-spovpxNNVDKD4MhCiudfgtmD7L4SWF69N73Ui0THIJEoqTXKdbXQEaJeAcjDuI-k5UTj30ZvhrMUbgNm3KO_nQIsdA2sCNFBLfRp74qlirURBPxaiTR5_KkcEOiHoYKGXB8__I-E2t2iJzKYEDVqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
سه دقیقه با لیونل مسی ورژن 2014/15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102423" target="_blank">📅 14:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102422">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rywlk-lHzeNCeoeNN_Jiqx2xrNkirD6Vu503ukSJHy5a53Fqd6feQcP956JIBaM8h-1nm5YfqPTwkrWE5iNbrywnhDt5WdB0TygfginqH89hg8RWGb2zGKrxYSdEFOP0pQE4QCnGnTn5LSzFliJQX4A1egRiJbQzX5D85R9R3Aivzo_Yg3xKElYIysI9HX9nDyfGeY8IcDO0SW4XfftbzaIEykBFOhCAClljRSOpKBXvYzshWo8npqy00R0jkrW07_c9WQ19OSBXTcTDGHPabEyn2R3xYr4wl5w2WOE8gcGRiLnoWn5dKLZ89VEsYtu2jUROeeH2DE4vI5E9wPkjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
لیست رئال‌مادرید برای بازی با فیورنتینا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/102422" target="_blank">📅 14:36 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102421">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0ZBbWq5loshZJ6Jw6jKA2YRi7w-LzEGOHvKahPWpW7XNE3ZKN-OphaNBUX9ASFDdSTLjYlHNlPm9mInz8wBAx5JxemcpDCTOzE8UaiWOIGAPyKk95YyLtHVGKD0-44A8MsDmcZ9o9flRerclvKkI9tdH2nGezdZTKzwRCGNoOC3aknhsUr2B8WZNvbK-Dg0yLjM2sChpPM0nkfQda2y9vnFPukhPux3wuy_ohu8lzttFnUEtfoKBlp0Moyb5uY7QXQnpKzTrfmO1IBoK55IlaL1_XeC6TKAb74VKD95sJSTHjJXdkBDu_8x1wT-ZEPQwuxQSRlx_eBXAKaud0_Hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووووری
از نشریه اکیپ فرانسه: آرسنال با نیوکاسل بر سر انتقال برونو گیمارش به مبلغ ۹۰ میلیون یورو به توافق‌نهایی دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102421" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102420">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529b07ca6f.mp4?token=P-2j7ZHXIPyArZpKhltpMbvbIIXhwtfz1Wet7fxpq_51Xj-1_hb-QAtC5Fmq-XHnWYZnxlqAVWUpetlm0oZKGX4anuDAAJQHzFYduglTADZ8B_6WGPZ6GXDD1M3zllKj2EOGQQctC9nixZHJUeywgNyTUfN1cNojppBMeDQ1F3x7w08swEDIkB7jO-OPSJvALuPtYpjiSE2ro3MBo-Bw_OA_4tao2c6okxqHBsU3O2kKp0oUDlkzxTkFZDDszUJQIwXsZCqcD73oKPjFljlGyhv66Os-HpMY8myC_ThNdzKkOOvljH6L3WBmcgqFc20FOT39ZD71P7ZSSXVvoyWtTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
✅
یوسفی: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/102420" target="_blank">📅 14:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102419">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9889076a09.mp4?token=ligMdqapXWUeSUbke9KuZoLiuLT1s_n0IXtW96I1W1v2fdEYifk2SkfF76IXipGhHnN2rm9fpdPRO1auoPBMM8DrYZTrz8pPZKAsFMtcG3Z8zsneXPbEh9rJdWm0ndwRL83X1DPHcGfCeCW8NXBqBqxMI5kImHaTTApbrRX7ZMKkwXyzJrbu-Eivaa-bDR_nVEGtNnUNZYLWlhCUfskn5PRvX7BYlg6ySjcDFpbvl1zxJQtmkeNAH8hT8FPWXqB-u_NMvL8Nag45vpO0OPojhlIJQLJ7ZYNuX9-tbNr6v0PMOwkvD9KeLYgUpDL-2PdMO179vVYLxmer5HM90EtSMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
💥
روزی که پیتر چک آماده ترین گلر آن دوران فوتبال میخکوب شد و این اثر هنری شاعر رو تماشا کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102419" target="_blank">📅 13:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102418">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteR7XqaN5FUFgLlu8vFNX0_Ki3NNllHo04vCpjlVF_9v8CtrAun7pD-xHWe7QOkgiMnBaseSRrWEvLWswUyIJeCwsYQ8_5n6UaVNNas8JXlnUL8PV_46GNPwTJnLvj_82i5Su6Ql-IxdRrRe995HYPnL_Qq9h2Adpr4aI2TQ-o166-uNthzenKVnND1yNxxV4PzHwDhB-tZbzxJKRQdULi0KupU8mPMtqm_JE0yLd4FfDZ2hCSAo2nzrQN3ltkg9cgMi2JAspz6nMR_z6QcwsDVNt-r9aRlbI1E8dUOQPN6s8LNjl99oqOXxwqs0RBT3_o_FuOcb2SaIHxH77NqaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
کارلوس اسپی تو تمرینات رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102418" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102417">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YFsubHB4HPc3NDVspKB5sf82GciA4_ImB1xkQ7AJ4WJJSbJ07irfQbVBXuWkj0tHYLbJreKFgHcl_hdB9qEezM1b115qxmCYoDzFm4NIZ6S3KpSmlWACwg8V8UGv9lJ1BiWDgUv1wxZAm0cze_9OGayhuHSNri5SM6mLSOqqYaUayALeQKrKb42utQe1ly27Ddlebd6edBZeBT_y0Gf6BQMPp7L72UauCYwXwruToBs-iiMePAPsbwjSYkLSm5aY-fW7IHxEq3zPMragAJPF1MBHwcpATyBgJrSlwP5iJ205qeVsLC4ysmpxFMz2XO1L7UbPyfmFtVe7NpThfDXy5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
روزنامه اسپورت: دو باشگاه آرسنال و تاتنهام به رقابت برای جذب فران‌تورس پیوستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/102417" target="_blank">📅 13:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102416">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4938ae1d8.mp4?token=XPbjlkJf9SiLoeo4rC2LUhrl3XSKByIqCortcUDzSW6yuwWql6wqXjPT6Ervbep4LgYFtSgodFCgkm2E1tSmLuiaU_GLUpWvUMc5My5MfFa6P0GOqPzl9cU6etN5DY2jvNZv-OePuUi-FcQqv0UVbRPIp8brV1kXyVuxv_Bl1hS-r7zBZhnwLVTLCXpB915ZZHR4RWkCgxaO_wRLkxt8eIyQFKCwMX2Yys6J_m3Uurq_nFJ0jcWCo2EG7yI744QdE1GZJpkQeusZk9m8Y8VysYFQznLLAHCAZon2AyGbVFx6L3CAkKlngxOdrjW6hcl-reZ5Dwl1e_S9PIOB22KdNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های بامزه رونالدو از ارتباط صمیمی با پسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/102416" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102415">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5029f55db8.mp4?token=v1LZzdyZc_QPndIy4f580icj87kauh6VV-S1Ji3-7pERiHV2AWA7vKymm3baHJu0ib_XeE7jjg0dki4e9Ar-9wp5vWJgO5N4ZC76u9KwalAS8GapDWZ10n4DGIdIfg_qgPkTU3cBPGmr8ipCUNnDh2lb4UEeDnDgWMHux0ZLUm-KIjldTZ1QfEOnjnlmE5QA_Tfw4xNCfqxL1P6SoheuNBEqC4kAlC4V1qcaW9FH7P3mYYxnpHjvYFD2Sbr2bukY9wa7S5__k5aleU1DM2hLQXwB9kw3cIwZyN7elGOOxdbg-E3Z5RPD6uMHeeyad_JAgKlu3K0lfoynVI2w4yISjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🔵
درخواست کودکان جنوبی کشور در وضعیت جنگی از رامین‌رضاییان بازیکن استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102415" target="_blank">📅 13:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102414">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac78119da.mp4?token=c8z2cbeLKgt7OoFzChOGLNUoF4hl_uk5aH3mxNSZMcN_rwZRw7u8wlPDy4XG4PslKLVly4QUA8UEDLuACjKVedJMtJR-1_6Cm97smGGAAjKK41YrBji2ONgr-DbIjxAHQFECvJyRHJPb3M4Lpqei1GIYqEuC_4jSPrdhe4nU8eQxqYB5CesUBryGAK5qVJdwFTr1Xx6hIOtMJyNd2NwUXE9cWuQpxp4hJS4SpOc7WTiNR9n3n8nKlrwghTblatLxqL3bEDWVZzKHNIwBxzfi13MWqMi36kQ6kmgra8sD3ZtQH-Ew84d8Jxkq81_FJnAitqqbYMw7JxxgLXxZzOBDAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
نصیحت اسطوره‌رونالدو به امباپه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102414" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102413">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🤩
#فوووووری فابریزیو رومانو: آلن هالیلوویچ استعداد برباد رفته بارسلونا در آستانه امضای قرارداد با پرسپولیس قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102413" target="_blank">📅 12:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102412">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b732a95e.mp4?token=Izrc80HCjYv9FhwZfqoTxtH7Gxq5iWZmPCdh9pH0j2o6owm-wZ95H1PGFonyeWBKYu19ZTXgHvhex6ANzIlkiKj-nD59_jmQBACumb8kc66eRMvlMIymtmciL5o--c7IBLp7aq4WdNnPAlEpTGfa5PZlDakZq0IlSJtCTqfZ_7Dc0Q6gVJQ7WGIYNHHxb85crRgeOMrQqc23kf5zlc06NkzcyzOpff3zPFGBW0w6S1KxqKNtwVUv7qFTdpebeHJu0gxB05B-EBialBQ3h4EXXJ8rVV0Pw6vMM0IiwEfeBde044I5PGyOohJ9T2N_3qD16P3hsyr7xT0PX0r_dG4bsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇧🇷
آنچلوتی: "در هایدریشن بریک نیمه دوم بازی جلو نروژ اشتباه کردم تیم رو تغییر دادم که باعث شد کنترل بازی از دستمون در بره و ببازیم..."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102412" target="_blank">📅 12:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102411">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=EBZeBcWkmOwxfU2mt07N9FAuluqdkzMLCEdAPkYOHpLK9HhcNouUF7dc52Pzebfb87ITNWcAQiwJuTzaZNgJdjLTTBnqXvb25bltLzjxR9eThanlcUgOyJ2pH3YHCTL5PebSD3wZCsfcuiIitgTrh1d7yA4KB-oIK4T7s60A7nklMqL01w9f7bUQkwEd9ZkTJsvKi21A__HkKhQHkS8WQhSk3pDhprXCb2vTMQHlRVGgHiHFm8lQzd47s4qBMRyAwwJ23qBFWqmHhBq0SYBUc5x3QMyj0Zo9SgvFrIQClOG617lPU5dfRatL-Z9rW9aHNYorgU0QSfd_Gx0BMauvjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
جواد موگویی که اخیرا در گفتگو با عراقچی یه سری اطلاعات حساس تهران رو داده بود، این سری اطلاعات مسکونی مقامات نظامی و ... هم افشا کرد
😳
😳
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102411" target="_blank">📅 12:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102410">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5a4f433a.mp4?token=aeCm49yvCWSiL77lQU-lI0JqQz61z-hMB8_QgN9cl_zOIFPX-DfFIy_6nemxPliq2dZTyEIA5Fb6Cv2quKZOArZZjYvF12_ykZ--5eA1nar4bVszh2i2aT8apdZIJaHQg4uVfQGPcuQXijYV7VKTd7jKeUhA7WM-3AyicZ9Ou5i1LLCtQcIn9UiObem6ExSxtrDWUxInZ6oeLjDw2jpZP7WK59wi3FQ7F--zNya88YHlIazTwam0_hUpwH9FKmPHHYRwLpa2chbqBVq8IgWX8lWj9Bj5Qw5ROlkM7XnL3vHFAnjqGJMDD93a72RHQ0TzeF5yOX_Y3lQMNepVJKcFWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
🔴
‼️
علیرضا بابایی مدیرعامل چادرملو: تورنمنت سه جانبه به دلیل کمک به پرسپولیس برگزار شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102410" target="_blank">📅 12:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102409">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c746b16b5a.mp4?token=RzCkqd1wndnwMQgUAB0b7tNjMm1N0Z-jLV6ij4NsvAWp4EKK3xcnLtHzj4iR6q80hxWwmbXKyXPux0We230jTzkej0muGtN0wenNU9T57Yns3vmcNWPbcWnfabHA2HSdWjeIYPE-x4XnawTfkgh8WQ9mtBejIBWa0UUb1KcLeQQfyTngoCqmrYzEo_uXquvDW7WmQjTDTDQHsfcwrei3TxjAyZ6GHEmpa3kXtYNMJjPUFv_EOThasMwhvPg52C1amhl95cfof7bbCEWYauRD0SQ8d71Y27Dt0Fg1Pu959gu-mOo80IusxhJ57-BYouEb_JVqTBs0eLoIsLmGze9dAF4f5aplsbngjmtaIV_V9DNhsbyqjPiMO7AUyR1lUmiXTZFPwreoPH9cPoGCuQooDtPiHryHQ7Es9XXDTaTS9uVwRXqn_JWPN1KsoEKN7-w6kRY4sc6GIjYEZ3JQKFjyRqArKBA6Y7MQIrHEeYgw6L22iwBqGANrWncraMlfkIG0BLUxv3lu8yvRss5OmF8rSaXpSTardjH-ywplPDoOWsYEWVOGNrlKfgKLfCGUHslaJk3j3N1ICtu14vq1X1rPnkHCo0uN7U13CapnWUtW7bltKNNfmmMCDdpnWKwtp8h_rNE0-l_jXNHxn-Uc4v6K55nhEIsnU3baVjbpDyMijPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔵
علیرضا بابایی مدیرعامل چادرملو: بازیکنان را از پای دیگ نذری آوردیم و با خواست خدا پرسپولیس را شکست دادیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102409" target="_blank">📅 12:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102408">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1b81246b4.mp4?token=hTfDp_W3Qa--rmRTY5hUPsEqYi0632tXR0DNmRz4hEVZcH-BsPUMi5m0satUgTJu8agFfe_FjxYc2NxWLLXTbG7ddPg4TMwxMZ-OaTBtEdsUxoT884FQqfzwlRpZWMNZZmHmvXZUEpb9ykLb9Gu-N3IFiH-_5GfEdnQdPHXTUaoSO5OaHCbishizOMaT1oZ9_eCwrxJJLcoRhJ5pO-E_y5pNg0kJsAsX3VBDX6t9QRyPtN-jIULsx7SiFLB7LIw9LrGNm-JYe6YSLoQoz0FqmQrSYBvqhlpyxfJpeYYK5NQ5R822CtidJheFTBrzk6rDu-teCWjKukRgtKX5knvXvXVoYiqY9nTVpzEQqCiHeC_jwIuv5iiRTF7P4dunYfuXsTVNGdQujlQL3MvEMRukirn238SlZULPoBP466JMCwYY6XaDOy4SdVjJqr_2RhI-4l6EvfHzRWlqb-3J2kLbBssy0L22mCY6PTxX64Z5IQ-FZL7syZbW_GN6JaByBm1dDArvlX_ErfFJiVXtKTcFMBzuC_5DQh-03wS_HRcs2IKpF4G6vud7MhisQ_1s1r8vgbVP6n3EwsVl8K7tnFqXbKkk0q18OzR-dGXqqQFCffxXGL1PcfYrJphor4-_AWBii8z_qEKtMF0br2Qjsldt4g1TmqwQFggGfenOPmQVvNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇪🇸
مشکل ایمنی ورزشگاه‌ها به لالیگا هم رسیده‌ و تیم رایووایه‌کانو نمیتونه از استادیوم خانگی خودش در فصل‌آینده استفاده کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/102408" target="_blank">📅 12:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102407">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a01fbf75.mp4?token=XzEt7Y7hISi-cDjUUgKb6k75w9H0-AfgB5Ey-Khfky_R8TkncnLhZF_3ygZuwHZBfu7IRemZV1gniDuGFpuMDhNh84gqwTbo7Ga_DxOc6mc0LemHlxDmFTIWqiy1WPxXHsjOAMsj28qEKe4PkHxkguKS3G5NqzXdzrWdqZ5zehqUDEkXa-jEM_qPUYoohFI591QM_P2qkvyekEpv5gqbY_Nqt4SSQYHok2OXgtIFETF7LlIZlWZX5YoPytcH2XZfrzMYedfVoHk2F-xdDyQTScytQZY2HQeMztPAoE6qQU46EyBLrphxONzDqRlqTaztfaONTigENqK_JWH9Gv-stg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ویدیو وایرال شده از صحبت‌های تلخ و بامزه یک ایرانی حین ورود به‌تونلی در بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/102407" target="_blank">📅 11:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102406">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262957043c.mp4?token=n0_YmwG4LIqx_NN_zOTqfcuSU-qvKHy_3Ti_VGOnH0uvu-LNjTLrjypURbmEK4ebHvQT148GAd-ibqtXyq_FFdGPnLWSX1ct3gUVrKRy_TcHNqeGnSaMLzvM0kI_kYRyisbCEVrMf6qOFtXXXeK5PkFJ0qGHfGlNQClWUZwFoJPVPey05SOZ9Epnbg8rxrRQ8PP037U9nKW3yiyor2aPuMOyGrdXv7mQ-ovO0zDvjlZaC8k1kMJDDwOZfjDxsD9dBl39AGnZpM9pE5V8wNyY4DEStJPxW8OCcbfJfVYoV5slVbvwGSg-Mm3vSEUW3QXnzBPehNE8oqISUllAtKTNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏴󠁧󠁢󠁥󠁮󠁧󠁿
سوپرایز خاص‌ ژابی‌آلونسو برای فصل‌آینده؛ رونمایی از ستاره ۱۷ ساله قزاقستانی چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/102406" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102405">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2180d890.mp4?token=UnPIE_XkIgYljwrt_Qj6FsE0FaCB4AWzN2ZlSZYRSDiKTvKJKOXYE2_JJPLctjZOXqornLZayscHCJgehbsjurnCZIepvwfHdO6cf2TMpiSwgvx5GitND_U6hQU8Ztf34ML0fnW8sdAsiF4GB7g_eqfPdpaZXZ7ZasummX7hRwmbu_okuTBDQUdE4DeoJ0OP-RizUtn39Ez2GI_trdR3qRK8La_k55ZamIcUaNxoI4DqkV9wQbuNim5T1oIB2-_XzUIRuizEwG6DqJq9zUDYulgPyUnUF5FAPoOLT82XuyRcju_2jlkrvW9w4MyAGIKO2rJrsdWQONr89MM_AckU-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
آماده‌سازی استادیوم نیوکمپ برای فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/102405" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102404">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31c9897d6.mp4?token=kAXXN6j-M9Cn94WEzXUS-LoPZO-XiGqjlUU9sA1cod_29-_TBINZjjVCgaTq8hfe7dWPwB8QFybty2XMqFSYG3qIuYFLHllkM3US3FRlBlXUGUI6FWBEjLmLMr74Lj2ftAVMXREqrkmQT9AvA8IriRNdANpJk5I1gGaRmmtzqpp_oRTYsOiQP6ah2hC-mVyZSYmCwc5SVSo9R9SgOvDlYSvB_Hq39WMuZUehBM2UcRKkMF5s9fcwxFy31A4KbX74azjKGwsPTnecrt2yJkwFEzwCydKSh4tPgGTNZG_aIkBODTnblNblDZk-kqqrxbmJoP5wPcI-tIZbRrzBD9hLgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
پاسخ‌تند و کنایه‌آمیز مهدی‌رحمتی به صحبت اخیر معدی‌قایدی: بذارید تو‌ توهم خودش بمونه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/102404" target="_blank">📅 10:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102403">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
✅
کیت‌دوم فصل‌آینده منچسترسیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/102403" target="_blank">📅 10:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102402">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869e38d1a5.mp4?token=TJEOIp7dNRPZgckON6clqMBnqc4fs22cZ0n47l0IcMTAY8iuL0RLCsZD8qEoMjGd3zcvhhQWELnDcqww_HgvENDG4yEodMR_wyiD3WTVdX-IIZiTwsEQt2iKhlwUdgqRuUVbSqKfAN6Ejh6vfVYXbzz5fyRuby7Mimqu1pY4NP7Nz5aNSM5nCRsexxUzNqrj-rZA3Ha384ZFtfGRmxuO_OAeaoZ95pjRbS1y1K8RHmigfPToslndIHTSE4kE9SdusaccrWnr5h94cBQaex2H924JrvBrvg9A8p3f5U0yZsS_AnZBpQvPqPB-kxzoan8d4CDAf8E4sg-dYTUmrGOaDoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
درگیری شدید فیل‌فودن ستاره سیتی به همراه مادرش با چنتا از مردم در یکی از کلاب‌های شهر منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102402" target="_blank">📅 10:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102401">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XHvfZyuPq_rKJ8t1CLnsYv2hwc1RHk8G6LiGVXJES4U4qtU5r1UZJalqULBV78D7Ihxj3m40ZxpXUcVYKVLl7otRwvFwleTxiYzmvMP2yo0WmesSlxhQkjWlPZhc7XUwyyQyfbQBD1_P6Q3MvIZjqAvSYCV0dZ5gUkH0SiRA4XMSsnE81UG0mWsmzh9lE_kqd01XTUHAUQeCzkx04PRmG8XWPVGLPyDvdjkQYRFPEXmIhU345yfG_jMGnMPqm8jSNU6_o8JnQwewIXH2xSy6c8i1p14tvNq85DAqc6UIGXoFM6vFjzsfgO8e03UB0Xe7mutYk3dH4J2IFIjrQ6JpHug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0266060c.mp4?token=gdYFGpOuizG6BBVJl2i7Ede6zT0kETkZURJBZKI3KkOcr-tTYzz5EnrLSb7Kmp2ZIxiZm5qSkJ9CBdx9O0IZK7AF7mXSkK-8MXqEhjOvn5tPngrQkS66z1GXlzgYEzoeWxv8MEndnE67-33IMIC_EXGgyYlNPuJCigQrKQgVTIgH3tQrnXJDY-_5w04KKUU7dxhzDA1FOYAZEhSPYgn1942V3uzznIg2KnzzEwJ65tvJGaAqrR1mO0nPjwxzfD5ADZ7TPfIaWFpmfE_Xz6OI3qNDORqNUcG4vPHDWzkB805Hb96HjgdgyJNNittHSsFR5VEbjKgLmUQJerYTdVv4XHvfZyuPq_rKJ8t1CLnsYv2hwc1RHk8G6LiGVXJES4U4qtU5r1UZJalqULBV78D7Ihxj3m40ZxpXUcVYKVLl7otRwvFwleTxiYzmvMP2yo0WmesSlxhQkjWlPZhc7XUwyyQyfbQBD1_P6Q3MvIZjqAvSYCV0dZ5gUkH0SiRA4XMSsnE81UG0mWsmzh9lE_kqd01XTUHAUQeCzkx04PRmG8XWPVGLPyDvdjkQYRFPEXmIhU345yfG_jMGnMPqm8jSNU6_o8JnQwewIXH2xSy6c8i1p14tvNq85DAqc6UIGXoFM6vFjzsfgO8e03UB0Xe7mutYk3dH4J2IFIjrQ6JpHug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
نظر سرالکس فرگوسن درباره‌مثلث جادویی بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102401" target="_blank">📅 10:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102400">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=o386oid2il-UWxt2YVWsNoik5j1KrpAtUlEnwspxWZCCjqWtgu49GPiF9C4S12V3F10V1tukbMt5d1bFCKNPuQ-Hv4LnCEuFW0_r9Uk7T0vTRQo_XWdPD9xHYkNMlHhyp_vEkcSlXqfZ2z6CzcnJpqgQg1_lUkLnrD3hweossedJVnH1jmxDxLeaofEOwzJFqj_rrZE5NiNs5-QrRGNC1BWFBDKUyrTkViaVP93FwXjhdLgNjm2rgLb8L3v6RS5HL7x2re9fh12Yv2mKLZmcsL1PIsAswRDhXjX_kOz3pxp0TzWUP0gXP26H_HiMPNvLh5IksDj7RH01C_p2AGPBbXH7xynIkhbVVpevx44n82JpB9bTxtIT_6OSRiCh_aq4eAFKV-10XN7H9xpzrZmO_2HNnRgs0Biz91tBbYLoJaoFryRZezqhbnbjoiEyWnBE1Tn6FW3UrgMS2MO81tlwHMHLMzgan3otylDxUxMcBlRGPG2D0Rg89-x1RlGS9YY6CgncOsAKVb0S4cuR9NLdxRSs3aEmw3pAWhm4jXvU8AoDfUtVY6fg8TZr3Cpyh2Scha1kswK6sjBgCjHBvKJsRAD6FUemK2dQ4L85Z0XjJrh4IOX4PQj_HeVfzGyO3IsMWEbxKycb5cyX3-QFytedFr7HcF15LywB7Da2yOSBkwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f864b5c9ce.mp4?token=o386oid2il-UWxt2YVWsNoik5j1KrpAtUlEnwspxWZCCjqWtgu49GPiF9C4S12V3F10V1tukbMt5d1bFCKNPuQ-Hv4LnCEuFW0_r9Uk7T0vTRQo_XWdPD9xHYkNMlHhyp_vEkcSlXqfZ2z6CzcnJpqgQg1_lUkLnrD3hweossedJVnH1jmxDxLeaofEOwzJFqj_rrZE5NiNs5-QrRGNC1BWFBDKUyrTkViaVP93FwXjhdLgNjm2rgLb8L3v6RS5HL7x2re9fh12Yv2mKLZmcsL1PIsAswRDhXjX_kOz3pxp0TzWUP0gXP26H_HiMPNvLh5IksDj7RH01C_p2AGPBbXH7xynIkhbVVpevx44n82JpB9bTxtIT_6OSRiCh_aq4eAFKV-10XN7H9xpzrZmO_2HNnRgs0Biz91tBbYLoJaoFryRZezqhbnbjoiEyWnBE1Tn6FW3UrgMS2MO81tlwHMHLMzgan3otylDxUxMcBlRGPG2D0Rg89-x1RlGS9YY6CgncOsAKVb0S4cuR9NLdxRSs3aEmw3pAWhm4jXvU8AoDfUtVY6fg8TZr3Cpyh2Scha1kswK6sjBgCjHBvKJsRAD6FUemK2dQ4L85Z0XjJrh4IOX4PQj_HeVfzGyO3IsMWEbxKycb5cyX3-QFytedFr7HcF15LywB7Da2yOSBkwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
شباهت حرکت‌های یامال و اولیسه
🔥
😮‍💨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/102400" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102399">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=Byk4rMQ-4mAvWhwI2JQ9lqzBGtXO5cR1araTjQTXXRKT9Dux88EZUZ3WLYK3-hR03OKyVkrKDHXE6EpuBMEb-zKX7QDZCBRfapJteMDjuyHxOxjAxTnJeyfI8XkH0D-kLB8_NfnnJOI_j6pdVWmvw8W5OIdX-8Gf9aDH-zSYKZgkY8N-GPxHaqWmVXOZAZ0cqWVwLjqJ5ReCmmvRBTGvy-9EtdXSPPEV0K6bypktiwyS2M_6vFO3aVExRScte-KtlpsqarI_2PtwldHEwrNBrheFPAKxt4I0mDQ4aVzq5mC9mGTwchy3N6GvIN4E8VI8binlEf40pzKogBpIKOKcXIpLZjqMUh-xGRDNYweOzUKQu5rpW2IMeUNTXLcLFLGayxExS0GzQvqvmNb-WJFxDKsQ5O2j2ItUOV6XyGfhfYCGPDOStLaOQAWPdrNRkHCqHxDeR18CvFyIfnXs4qHTn4A4tlYvzdoHfsPM5qQG8GXFEebGg5F2dLmWNim49Fwj1uQJ6q8VpiBzn4-nwo4GYvq0sBmqDR7_S7QNKPpTP8H-LbAP7eNEGV5a1jimsy0sXblS17XY0svf6yVmdNEH0zMmpCIoLvmlJLR-oHSxcFmORbPQqT89k3X-lLSpsiJeSHkFDgFhnm8qNUMa2zdkUhuMkTLrQjy5c-epKhX6THw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5630cebcb5.mp4?token=Byk4rMQ-4mAvWhwI2JQ9lqzBGtXO5cR1araTjQTXXRKT9Dux88EZUZ3WLYK3-hR03OKyVkrKDHXE6EpuBMEb-zKX7QDZCBRfapJteMDjuyHxOxjAxTnJeyfI8XkH0D-kLB8_NfnnJOI_j6pdVWmvw8W5OIdX-8Gf9aDH-zSYKZgkY8N-GPxHaqWmVXOZAZ0cqWVwLjqJ5ReCmmvRBTGvy-9EtdXSPPEV0K6bypktiwyS2M_6vFO3aVExRScte-KtlpsqarI_2PtwldHEwrNBrheFPAKxt4I0mDQ4aVzq5mC9mGTwchy3N6GvIN4E8VI8binlEf40pzKogBpIKOKcXIpLZjqMUh-xGRDNYweOzUKQu5rpW2IMeUNTXLcLFLGayxExS0GzQvqvmNb-WJFxDKsQ5O2j2ItUOV6XyGfhfYCGPDOStLaOQAWPdrNRkHCqHxDeR18CvFyIfnXs4qHTn4A4tlYvzdoHfsPM5qQG8GXFEebGg5F2dLmWNim49Fwj1uQJ6q8VpiBzn4-nwo4GYvq0sBmqDR7_S7QNKPpTP8H-LbAP7eNEGV5a1jimsy0sXblS17XY0svf6yVmdNEH0zMmpCIoLvmlJLR-oHSxcFmORbPQqT89k3X-lLSpsiJeSHkFDgFhnm8qNUMa2zdkUhuMkTLrQjy5c-epKhX6THw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شیرجه زد، گرفتش، زد زمین، شوتش کرد!⁣ جوک خنده‌دار بیلی مک‌کالاک ماساژور سابق چلسی درباره‌ی پتر چک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102399" target="_blank">📅 09:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102398">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3hbPlj7gVqpSdU0dVF04mV7WAHvstwKppOfYZSQFBEO7MpPEPHm5lX_2evfbwiJe_IVt3zE6yzowd0ACqhroV7aEXDrv6-6lejyJFrkhOFEnqQ5TZbtYrzELzorFd04cy3qupQmY0QB0s17Q0m6l6ilgQnB4THw0CmsT8XdkEDo6SkJV9YqXvfDLQxaxy4ECqov82Iow3svJeiqLmK2mFX-10S02JVfbrz9JjbASuMbI-e29VP6rZ_3GjnDsEDL4TDag26FCpephRhy70ra7BKvrw8TLxTX_v3U7n9oYE0zZiPmuA3KkOGQOHoYzjGmiIlW0qYAerafRH81IyTTzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
🇮🇹
لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/102398" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102397">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=aefqPt_sYpa9_BD9oCOKUw4gieKlMLPmHg7BnDUkSIGlLHM-AiHWEXYq_X6xqISDzKzOcRGpiOKJndr8YrGs94pmDP1_-DOyp2b5ko3INDyzNef6MdA42_dsW4xGNzTQ4In9921U3juTq_a9IfqLqVHf_j3Tls8Rrwc4YLyBOi4i8JSNUq4YjHRMawiSVoYiBHw6crrCqaZ96_6LyHR_gbOCG1wLlQweevYNUgpkJHZO-p1vlNvJBGL2Ywx5iWkr3Mm_O56om1y7iFW9yCzN-UneqGgkGEMNNoeYfvthwYxZOjF-2RzaFwI6WzYVLSD2URWgMlA9VRN66IUeGzV4cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a6dc02d.mp4?token=aefqPt_sYpa9_BD9oCOKUw4gieKlMLPmHg7BnDUkSIGlLHM-AiHWEXYq_X6xqISDzKzOcRGpiOKJndr8YrGs94pmDP1_-DOyp2b5ko3INDyzNef6MdA42_dsW4xGNzTQ4In9921U3juTq_a9IfqLqVHf_j3Tls8Rrwc4YLyBOi4i8JSNUq4YjHRMawiSVoYiBHw6crrCqaZ96_6LyHR_gbOCG1wLlQweevYNUgpkJHZO-p1vlNvJBGL2Ywx5iWkr3Mm_O56om1y7iFW9yCzN-UneqGgkGEMNNoeYfvthwYxZOjF-2RzaFwI6WzYVLSD2URWgMlA9VRN66IUeGzV4cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت فوتبالیا اوایل هر فصل
🤧
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102397" target="_blank">📅 09:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102396">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=qrnT89pLB1Qy8VWPUZTHpUhbsdSRSRuhQsYlZXR5DwcO577Kf-u7g1qwJNWWq6pd8jtGgvXBLyGwhRbeNCDwAKTz5kAxI7yhCa8qgyrwNDayTrCNb-X0rPwyzLDtfe3MGgYPYoUpApWC52cxViMRuCtqQxKu2t513N5gyqOdBQGrVQnwPrUUet6f_dP1mBEABpygEThl1NKj_shFB2y3xFosa1gXM7zq4a-Y6nDm9kgVjk5lPXPV7HaCyPdTrpJmqlHxRtAXA31F3CbpDPTywIB3Lf6QhMWCUtw0P300T35EW03zeIFH2QrUc79WH0cpCH08FaI4jQkH9ZPQAsvprQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e396ec62ed.mp4?token=qrnT89pLB1Qy8VWPUZTHpUhbsdSRSRuhQsYlZXR5DwcO577Kf-u7g1qwJNWWq6pd8jtGgvXBLyGwhRbeNCDwAKTz5kAxI7yhCa8qgyrwNDayTrCNb-X0rPwyzLDtfe3MGgYPYoUpApWC52cxViMRuCtqQxKu2t513N5gyqOdBQGrVQnwPrUUet6f_dP1mBEABpygEThl1NKj_shFB2y3xFosa1gXM7zq4a-Y6nDm9kgVjk5lPXPV7HaCyPdTrpJmqlHxRtAXA31F3CbpDPTywIB3Lf6QhMWCUtw0P300T35EW03zeIFH2QrUc79WH0cpCH08FaI4jQkH9ZPQAsvprQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
نظر پرز وقتی مورینیو میگه وینیسیوس رو بدیم به تیم‌های دیگه تو این پنجره نقل و انتقالاتی...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102396" target="_blank">📅 09:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102395">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SCaNsa8LMXyBml9Lonx4qFhu5eefxJT-yTKILen4Pds_V_wlu0WujZ7uCCbvSM_2DI5PLR0jZRESLizVFGYsnvq7nta0NtmNLMirf-h9fCpHc0ygCPv-d_ezoisWdhFyLci7G6XriTGrsFcV8P3Qr7xBImBYWa2M4FYoxjsyuzNTHakGVywqBTmlJeBK8uDz3_gu76NAf4JPgXxTfbgT2YtiweNqiNXj6NFg87zNmuEsaPuCU4BvwtYsJwYBjiGEJqG_RXGI1KFKqcOQ4VwyN2s6Ft3AFpBZU--bdfExd38lAR7mcWV4O60PGXTGCgu3-D1bPugZWy4EdMoVD20OBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
🗞
رومانو: حاضرم قسم‌بخورم که دیومانده بازیکن رئال‌مادرید شده و فقط تا وقتی لایپزیگ بازیکن جدیدی نگیره قراره رونمایی رسمی انجام نشه. اگر این اتفاق نیفتاده باشه از حرفه‌ خبرنگاری خودم کنار میرم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/102395" target="_blank">📅 03:13 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102394">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laP4yYUHSSwYc9Bzfh2bBl0ZnwHtyNcK2nAk2RFvWNPSEwvdx9Fe02csrGurmyTIJPryZzPSbO3Z95zDKDo_2saEFEvXiiD656nZXwNO45ZMvX_oz4W201vN1lhPes8DauLiiZK5n795o4klZ4HfmZn2d4Rs3RdpFh4ZE6smWbGMVocXa-1N4U8vJdgE30svhejWNyuzNlZl4rqPS0Re4dW0IsuXPMPMxDRpmLoM_zOunsQzDKFYu4Sr9wmryxuYs83284VjH3_0i05UUkR2QXDi1pG4OZv8I2TUtrS5tk2SznoQWhVrIPYb8OK3H8p49aW542L8PdYqN9lSuLcWHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کاسمیرو:
خوشحالم که اینجا هستم و به لئو مسی کمک میکنم، او پادشاه فوتبال است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/102394" target="_blank">📅 03:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102390">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYZbJUyHka4TPFVRci2eZ8fdLqtpqa21jx6uCz7JnYYITQxTVbj0KJ3rf5lsr4WhEQvrtumZ73B8n1Vxi0_rMZ8Kbxmf8VUywKN3iZD6L1k50VJi91XFMlk0Bh6gFMMxXUkmR4OhmsU-EH-UOSot4MKZMaP53TupTEC7NV6i7R_RVgph9XLX6wtK7GYbf02uNokvYMoj8digyF5bppNcZC3YSO5WX21OQZhS9dsdYm0Lfbe1APQjHWsWi0RslvmnxFp7nCZzgAmrDvUT-470CuIbsKo7q4HAFcR7fpj2S5qgcSIZ2XOG78O81gLZOKeEBLVfoibK9QMAxGEYhZ6DsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptMAibXmtrPM8n7LEX7jOp6fX2LbWshNquTomtQmReumjtp-YPICikgAMmsw4CgFU9Dw8GfwQ9Pw_eVjsy0mK-5wCifPVc8l5fTRr23-6kknjrb8WqVHNjTOGSkFrgyFmuE9IL8sGbOZeIhyM3P2SdP7uJ7pInJGUer8VASycxnM9cRHlNM-lcqQ0QmmYZssa8npnuZ8-D9bVklDedvTqLeiyrrUA4vREhI9EXUmXqBHbNb8B4NNsu9ptgBdubP5urFpJWYyX2zkqkdEjDX8Yp2ZleFaO1DTB0LoEBCTQ6OwqjPrFaGztTIYr8zfXqu028yM0_CKDmsko3kNZIWa8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E435LWHXqj5B0Ss21MCtzuegNqbD9qteIiM0nGgnjQxzMrItYGvQONStZ8g-YfsLRfW2rZo8OuYO8dPnw3teGtu3UHRbNFysAIOWg8Svwv8zKwaMmDlEUyfNx1NEqMUN7l-zwbGB71L-F6VGrywzjiwpC6xdc7BOsw9XqyyHaV9GQNWnc5IYE_o6-tdxNl3MX4I3F0XECpisAxaosVBZTLBy8UGsVHs2dHv77bQtbkWCldgqgsEyfPDlR2-VB2WhblVs5A6S2G3wHiH6AFDhR4FzFT6RgwapNHGhNDhKI8yCfP-TPqILKKyUyJfZkOWrPurAWLzA1MA_p8YV04gHIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckzvb4vQbE6PcpKVP6iAAMgylaNGXwYnb3F5GO0gcFCbJFcZ2ZMznIz82qwQslXSwhjkqCMySdMbNkd93vnSyOB2EEs1ANKz5G3NdQgi5KUpWo5_VepV7x94h7zWvUtbRViCRyk3pSEIpaFeH5xXgtguBj5uAXXasfa7pQ8ja9EfWKfsibB-fKWP-VvLqZSiSNbzRGwMUgymACHlxRJjVemUfMbBwJRJsPrF-qtFvqlJrI-5QmG5TCIIVq4c0YyglOwYRVptbljtKemboOU-WGhsIRxiELYjWfr1QcBQfLKB-PHmYQuh3ro3Z5MFDEBcYK-VL-Xj7n42JXD0kDm1uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کریس و جونیور و جورجینا رفتن عشق و حال.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/102390" target="_blank">📅 00:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102389">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNW78FjcVjXN4LH70kxcdC1OvIZqMMJJNGSYTUB-5PqLRO5-jdkRbRUcBT93lUrXtDc7EsLESV1Bo6i4T8i4r-qrAk-I_p20t4jARDSCNR63AX1OSl8YgeyGkjhP85qYpgBEn-KxToTP08dt4kRLc1NBXByxDsG2-6mqeut58J2DbnL7LcB6vje3sKU3Pio-QvzTClzZkfR745YoJG7I7SQ-tQAN9MBKSlZZsHTfaIxnxKbujmzq9E6jvOlklJnOHaNzviZ9TF3AriT_JOG87nfmajI07RBan6HlC-I4PfL0dPXwwmKE09ls5ELg1nfkksJgi2OvRZxlRYFndYPl68jc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511459b235.mp4?token=IHEXFEMrdcfu8b8HQ1pm7EBgOmcwxUKFLdOBYhDTmq9nC1O6xbO0a_PS3CT40yXv1dNy95w7bAOCvmQ3psuPbn1HUiKcsWAN9CQ6K14OLwxU5OtbTdj0K4oq1LG64BE1szkoAAIksnjwf7bbyTK1J_XKxp4riDrAwfYjvxmQwk3aXZKQohwvIDtCXgMKL4y_ffFxpO33zFZbcO0VjLwVbvSO_BUmVJFH3ANwmWIUqtg_84R9WenSYReHCZzVLzk58RdY4kVJqRaZhmgH3XzDoddYB7GQR5BQv3nMd7W2-DusHSvRdy9DELeUL7Bny104y4BgDSAi7FCFroDxgKSQNW78FjcVjXN4LH70kxcdC1OvIZqMMJJNGSYTUB-5PqLRO5-jdkRbRUcBT93lUrXtDc7EsLESV1Bo6i4T8i4r-qrAk-I_p20t4jARDSCNR63AX1OSl8YgeyGkjhP85qYpgBEn-KxToTP08dt4kRLc1NBXByxDsG2-6mqeut58J2DbnL7LcB6vje3sKU3Pio-QvzTClzZkfR745YoJG7I7SQ-tQAN9MBKSlZZsHTfaIxnxKbujmzq9E6jvOlklJnOHaNzviZ9TF3AriT_JOG87nfmajI07RBan6HlC-I4PfL0dPXwwmKE09ls5ELg1nfkksJgi2OvRZxlRYFndYPl68jc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل فردوسی‌پور بعد از کلیپ دست‌بوسی که ازش منتشر شد یه کلیپ گرفته و میگه ویدیوهایی از گذشته من رو گزینشی منتشر کردن. هجمه عجیبی علیه من اومده! من اگه قرار بود چاپلوسی کنم الان تو صداوسیما کار میکردم و نَود رو داشتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/102389" target="_blank">📅 00:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102388">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPIWJbeArWd_QeQXvRtycCxbud3u0OYIV6zWfGY-qykzC6hJOM-mEkfDWjTT2P-yGf2nuglRe3M0XlFkYtuxeYhkBkw3n8EW4ue2kDv4lx2-KIjCET_-ji50cjV4N3kaNuHZYCCVrVsyInchpn7rNPrQ485Z0GnBOipgdPdkLxCYuaQN1ZgOzUs0TItkKtUcGvy-EOmJY04FZkcVLvxMDP4p9mpSahFZwU1500LvWsNuOdf5MfBwcMPn_gflzw2Gg978aoPblirIt7kWf0hUw8aSSe0CwdiZ6Ogv-eONpJY5x3SpwnKRt7WrUjUyeyN24k2E_xq7sO5E4uUEDsTYiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102388" target="_blank">📅 00:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102387">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IMNt4ZZapiI85ThkUCjszkS2sj_AV4jppfq7eLvhqJ5Lidz-FrU16OK8vXdPGfSGiKOsPrDTkikxFnvP4bM_0jUirUcQCIt5C2L_kgjtAdeUeoha5nqjT7T1bbVbTgqsX4LX9snutLtmV4mtQHQs6U9GosesfJt12g5VeiMIHj1mr7wt4-ZMwz73gv-Wsg1aWD02z0frbCodohTyEqrXB7n28Xu42i7Uzlc96FdK2EhA9jic7CuKwN96ZneFTgvn0FlUMg4uZAezna3qTdaeG--zAKMjk8PTFTcNYrBhNZB1GX7xZKJlkATu0CUQkbi5fKPL8EgNz85S2sRZvVtYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بلینگهام که رو دستای زیدش خوابش برده.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/102387" target="_blank">📅 23:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102386">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=T7Flmk5u1_iVoetfs7FNybhxDefGgjx-yUxkfoFA0tyxJIGdOjrtt86oWmLOw-nimFauiFDbEdNG5QRWNOSjFRjh2pQ2cVkn8FGakZAvOPaCgsWde8MFRPEdHQkNnYAzcMVrNNZGHE9AxGm45eUGT8P23nwHV2_eVRQ0tFA78YT9tFXQ-1mjCJTUK_ixB0_zHFz6NiMr75Fw78ETya3LjWQCnJqFMf3yP_DfPMxFM4lnn2667-N1mgQC7qt5iLBOZTM1kyLRGKTuTXPMtLMSvXM7q_aiDGjAqCG1Gp-ZglVy7UGMKH0MzZYiiaMh4CzuEz9RqihXGh6JKBuIotpQhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae65f1051a.mp4?token=T7Flmk5u1_iVoetfs7FNybhxDefGgjx-yUxkfoFA0tyxJIGdOjrtt86oWmLOw-nimFauiFDbEdNG5QRWNOSjFRjh2pQ2cVkn8FGakZAvOPaCgsWde8MFRPEdHQkNnYAzcMVrNNZGHE9AxGm45eUGT8P23nwHV2_eVRQ0tFA78YT9tFXQ-1mjCJTUK_ixB0_zHFz6NiMr75Fw78ETya3LjWQCnJqFMf3yP_DfPMxFM4lnn2667-N1mgQC7qt5iLBOZTM1kyLRGKTuTXPMtLMSvXM7q_aiDGjAqCG1Gp-ZglVy7UGMKH0MzZYiiaMh4CzuEz9RqihXGh6JKBuIotpQhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
روایتی جالب از تمرین‌های پاری‌سن‌ژرمن؛ جایی که حتی امباپه هم از دقت باورنکردنی مسی شگفت‌زده شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102386" target="_blank">📅 23:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102385">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4-CzYJ9Fz4ffTmLmIeYdr3WzCK8FKzLbznRiUpcVOu7Fsa_NMpzvnEV8j2Juway4Dnxgq6k80CcAfCs6filxV-NPkTRPuz0qyQDeLMwDpe8uXRkHYTc3lQQC82TjYBKb2VBW1-0qofD6vkvbmnTagKiQg-hCgf1J-YcAxLFGFZWB0cNI1Ei5VvdpaZMwIVGzGqhNd6P5DYn0vM8vxIABW5DZgjwsU54T7Ds-Mr0RK1h_rse4Ra8M_q0KwV_qpDuhGJFyqSqYULqy8EWlVzUb94Oiv32Yxo0nIPF7ESbbzi_U1E9tbyrCLdjyxz5PiFaJF1Re1E94pI2NQgjy7nM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اولی هوینس:
ما حتی به امپراطور چین هم اولیسه رو نمی‌فروشیم چه برسه به رئال مادرید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/102385" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XnNT8Cfm4-Co1kc9OfTQcWI7r0tYj8FB92BYstqFRC1OFAoMKwdf5iLsIkB0sDQdoBi6zfjsVg_1mD_kxKnKabmWlh8XNwKWVk4DswkGhWxfafr9QwRATeIKCyPzu1CNsvFiP_QYki9fuJZZLiOFIkx0rb76nz2HAJ2WwPygdT_kKwQCSFSLA6sdYWIx2Y44w5UNRpFmQOAI14t12QcmlJFLf7jPY0fWJKjawDwKl8o3jM-n1Ua8dUgOVFjNC9b9foR2DclTFj-P5PpZqB8IG4YoQktthiqHuDYui_ccyxN_N8fMsS-NCUvENmX4eM3MsfYWw01LnZD5wj60_GfNfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
رئال تو این تابستون شاهکار کرده و همه اینارو فروخته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102384" target="_blank">📅 22:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iXtL_irDgMvV3t_7DJrscmxB28EInkdrhJxqJj6ZkV4r46fGJOTqe2vZrLKnJuUKP5nODp18T-Q2cRxrWx0rLQyT27Jse4fT7efrMmKo7V_3KrdWvUlHKVPwi0QKKUozUtGFUEZwbdygWgpJRtMDhNFJYRMtPUH_-WdaFMwl8qEj-qPrt4pHvTpaYge8GsAhwejyNbpPIFSt0-200tqiu9gSV9LvCrf6DjF3dqbeMbGFrjZ9g5xyGxswCMUJaGiaMgyMxAmBX2SAD12l6vObocJDbfDbHqCtQQy_ATVEV-hKK0Wimx7J0_mGr-fUHRiHgtmyJRwsFI_nNtu5q5FNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtmwUOZ2RxfZE2DfZMpeOaR2bQUvXwT5T9uDAp5bb08XjB87gBiLbSujJRe2qux2t4UZWRWs4xOxmTAsYJbXiRwZj1Q3Nf2aJBbKp50HQdCUsSjgmEXhtckBQyGyewnRpZaU6PwMjjMdth1plMP_NqtTns0i7AbmLqr8FxZD6V36DMwyd-OxMlNFguMG03mfKOM7Kl8nzy4ZkMYbpV5t7M5i0et3udplsbtbfs9YnvtFRP3R7ugpNkl3BP4P7NMHxRSrGJDIVHqAxfEGiRfUllMVHJu9DdX8Rb4LRIOesqI928wcpHAdHonS5UIAKI8gl5wq5N21R7A2pn5s6ub4hg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در 2003
🆚
رونالدو در 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/102382" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-text">▶️
زودتر حرکت کن؛ راحت‌تر زیارت کن
🔹
همه راه‌ها به عشق حسین(ع) ختم می‌شود؛ اما زمان سفر می‌تواند تجربه زیارت را متفاوت کند.
🔹
اگر سفر خود را به روزهای اوج تردد موکول نکنید، هم مسیرتان آرام‌تر خواهد بود، هم زمان انتظار کمتر و هم خدمات بهتر.
🎥
این ویدئو را ببینید و بدانید چرا
«سفر با برنامه»
، بهترین همراه زائران اربعین است.
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102381" target="_blank">📅 22:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pReaYvgqzRrD1RsvLfeVcmt3hlaILuwUiWgK-fKNDwia-f4vHARRvmuKFPbc4LXY5yjaKmUTX24eW4XSo3z2ZBKUXPZKb2t62Ht51gGdlWgsCRU_fSg8d8aHa-RF770HNCHaMrEDEK2MUO1uYcErUTP1TUa9UrQtMKCL5TZHd-ng3P-LmaQOMHqRzCOYL5TQNm96P-8GjPFBBJZDtUNGBuSiJ8CNmavC6F9OL-G68uYEpslL0THlTAZQ1z-IF4NW9IX5eNte9qlYkltubu0Dz5AANabC4PZWXJxHSuInyRKKV2GysbxMI5NRi8WSq4HQGTGwUCJPKHaQkvUSoauxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری: کارلوس اسپی شده با بند فسخ به مبلغ 25 میلیون یورو به رئال مادرید پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/102380" target="_blank">📅 22:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYt-58V4lpqDagfDLrQt_k6tXToQbkBg-nci0-110YKBD1cBP6hM4VkhGfKGQ9FjUHdMPWkRcHoMknO1w4x2nvr2CPqkvurXsqE9rvsInekwp82PgalYE6XpH_Hr0Ejib3qdCNfKL8h_GOr5e_XuxUCpPu8rh15Hb2mwbhfqtBfqWfBDrhKzTDvNG8Sbvwr3Fw2r5FnwRcMdvmZZxLD3ucZxelXpuqQGOFxluXefRz3_JGg8juywPE2YnKxX520xJIW7-wsIdRZ6197pRqy1EwRbiJHCsdW6u5jcFPgw91O9YeyUyDL-naq7eEeF0fBDnhnEF_BwZHvf4dSc-WCUCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تغییرات وینی تو  فیفا اعمال شد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102379" target="_blank">📅 22:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTrAjhf4e1zRQYLz1VFRmWVETHo_yLNZM8Oq-JZYHYwL_g1BLvtaR3jkiS9UAx0H1ak3V0DEJQ5ZFPxum2ZvtcjooPW7maGf_gU4q_DzbjQvGb-yuT6xrSgA77gH_Lvo_ufMt6pU9D4ThwFSfL741tn6dy2wG2MakM27jvNmTGpysw7y873yKIqpGPytHVSBlDwCPvmCBedVJtUoxNXd01gYBRTcokzCWb_ZQ0qcaP4LH1TaBu_PBbFAE9pJXfSVZzlk3plONY-J6k0ziTcbSEdvMC3ilMUx0DtAHReVI5_dUgN6Cof_AM9MrT7dPEB0nnZ2hMOdMx0G_qCD4oBlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بایرن طبق معمول به این تیمه تجاوز کرد.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/102378" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8b5NTiNStfnwb4bNwEuWgX3wakd-Bv72_xGeQdMMzRaNskwnOmBldSsn_uqLShnZecBvGWk06wihhOYE144ij2B6HIcYMidtice-k1ep34uwYiLvYd_k7caNF5POUOlWzZ1_jMLUgLMO5luwhvUWxUapATF7KITsD5K8DbqnWlJ6c644eT37X2R3dheZSa6b0hQnjhn8Mi5tOp-ff_o3AvY9D5zygrElKdmakZ63KPE_pnRpHz1CMBnARmcrYf2oatIrsQ6V2aoA4oQ92gZZuubgvkAWsVHUtSolq0HCFQA9poufBkMMMTrXgs5QV26jXnhGvExxNEcbTdk5leHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بیانیه فدراسیون انگلیس:
ما در کنار همکاران اروپایی خود ایستاده‌ایم و بطور کامل از موضع مشترک آن‌ها حمایت میکنیم، ما با برنامه‌های فیفا مخالفیم، جام جهانی متعلق به فوتبال است و همیشه همین‌طور خواهد ماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/102377" target="_blank">📅 21:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102375">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtyQ9Pd11tUOcqAZYM5vltC2SWwz6JcZzJEpFHowBX2ttWxyqeV9mOrvk_tDMo-p41eZMs3Raap8XJzte6G-BW7hFt9wcM4ygq14DwuiKH2fjrmgUDV8fGquG7FzjDj1Wogm7tJNY22Q9NVaVx9E6yTPBIh4XZDkaWgyUM7NXNUD8gYpHj3ZdyReC7oYdZswhc8LgswcCuuqfmXKgf5RMqIpQllffTW3tP_aza3R5asOpdIFj7Ja8B9jLBw80SW-Ml4AHJ1VMz8JhH3tlK5QsDC3uSp3lwL0janMkZUeOz2InBxBAOTn-YFZrWyTKt4puwkL_z9GGT2DeWFy6DTkEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
اسکای‌اسپورت: منچسترسیتی برای فروش رودری حداقل ۷۵ میلیون یورو میخواد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102375" target="_blank">📅 20:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102373">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaccCoe4fZIFQfRzEsTvB1k8YK-YET7FqSxghdtix85rp-7Cbz_GuH4R1Ia2wCpt0B6EH9MHjPhlujx0cTo3W7ixJKfqZkM2UkSdoFlieowFnnmFqEESbDXAR2HTFBjEJyVl7B554KOBfqfgV6vxa6QvFIrJbO79EpeiY0lD_Z4UnYSd6AufnhC86s61vIeKvc25dTxoT0xJPxC2wt6cntkoIo80LRAQGz2rGhevgar08DKabGZgvaAONHgU1dJq3KIPJBacwRRicpS_IlnF4VaLxPYn2mvC1XTGU_1xCI0WnDecK9CF2IPYrMd9kPtdcivrENNwt_40wOQ7bRAt9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=DXukGlXznScAyCOMXtN6WBawWxLBUwXEiQVZISI7GHeHnhlkZ1VmL2YAYt-fpjiLADCV-IcizTJdhsngPhcdtM4D5sKL4HHzgM6z1RIoM3FPZdiikAO9fNznv4FqKUopDLv_brTEWFqcHinkrvWZimyta7k27oy_YjVmN25SlRoSTnlzpoXb3ofy1kkUUCWYXHsXSdYp4adfy3wyOujRr_BhKdWp8XlaCiI-kxEh-HJKnA5TZ1aJqknjiMnFTC0hyAMukimsVygAZzRdO4RBplI5IUCIokoz7DIm0mCILmrT21-rzswvz4uXHJwgXY1ZiQxloxCj3JMYJEVi736uQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56d9c0f441.mp4?token=DXukGlXznScAyCOMXtN6WBawWxLBUwXEiQVZISI7GHeHnhlkZ1VmL2YAYt-fpjiLADCV-IcizTJdhsngPhcdtM4D5sKL4HHzgM6z1RIoM3FPZdiikAO9fNznv4FqKUopDLv_brTEWFqcHinkrvWZimyta7k27oy_YjVmN25SlRoSTnlzpoXb3ofy1kkUUCWYXHsXSdYp4adfy3wyOujRr_BhKdWp8XlaCiI-kxEh-HJKnA5TZ1aJqknjiMnFTC0hyAMukimsVygAZzRdO4RBplI5IUCIokoz7DIm0mCILmrT21-rzswvz4uXHJwgXY1ZiQxloxCj3JMYJEVi736uQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
استر اکسپوزیتو درباره آشنایی‌اش با کیلیان امباپه:
ما در مادرید با هم آشنا شدیم. حکیمی به من گفت که کیلیان خجالتیه و خودش نتونسته شماره‌ام رو بخواد، برای همین حکیمی شماره‌ام رو از طرف اون گرفت. چند روز بعد همدیگه رو دیدیم و بقیه‌اش تبدیل به تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102373" target="_blank">📅 20:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VgYfi4iHQSiDYZnWwy01vWctlAuxoRH_DwNxLhVxzHoCnrIfU4SxzHTgjRKPnJYghednxA7RsB6Ez5lgExXFh9QrxllfrZ-__EwR5onuSBkBFpeSc0nFum_bCYLHxBEyEpizHcfPmumycdKCCHMGUIayVbI0DNxbMp0PPvjMf_3l7Ex3djeHaY6v9wkxvWXUb4rUw-3ueQN72jS93mfqbWixA-bMXynMxTxWPP5q-ydDHCQz5g-HmmQKvF4vyUsDOozfSKWVMyJWUiTs66-4y_66Jjnsgjap_wNWz_YfEW68fwbiHCfKqD5E7Td9Re0HuEa4SExVn4lB3PkKOX6z6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwCEKQWK9nweqDiMrNnXT1DGQfT88mWqRKLzsWdEIDJAuPbVxZeo4W1QfFeQDbeWFAAL2_WII8jhD-Hv77vSsg-83sBypjmrgGXTX1xHhka38NrnXiHkoCyiU0pC2SF0ivEHDUqOkID5-OC4OY08Mv_etefAUDoIw0a6rQqiarQhaxjNMEs1RaDasl8oB0dli8t7bFQxYdeDRG4eD7kRLzPo7sYT8v2gPqutCbaeqHktUjYWjQEOH3H3SnWhVo1mReNY0ueOMk_F_OH6CqWQSvOwrn_-A9JrbUpv2FDFM9MBtMJurTWzuNO4A9IwQwzAFYBEdzJT_Mvz8YCJ7JImYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3zKdYKa39oVgWhei5p7vXBvUCat0E-EAfuUJO3fyq2CViObiZH-AJLF2r6CIEINtSsA56VZQWONcbEvu9nLJtYspLOD_I-55HcTbmUrIMN6lSck33jJBvbF6E_aev7GUVyj8xZi0zLPWkclfJFvB5FYUJXnJ1S0IPWC5B0UpluqdV6hXgIGBzWX7UGa9W7jH3zz7g3pLhJmffsy7-ryfOJIWqsHs316g61dfBGv2XxYuVDBJqvHeoioaXjXF-caiExH3qkTHntPnGCqOfxpUchVQ2hNgcnkKtlqHFAYQAgE28XLT9BsIs7aBb0bYtcmjTUbS3d-wIatcdKKt1Pjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLTeZxXuFii0JIJJJEkeowCYMqIsZqhmoD6c0vw2t6sUL1Y-KpBq7heA9mO5SaoYjzN9QaoqVFWvRWLU5y3P6H9nm9sqV8LaeX0D-zr8OdRGnSs_nCXdApVrKiG8k6PrDqRPdx_4ofId8swgT5FBoOUaytA64ue2kFLbnrnehFko37l2wm3nZYOLg7qiX67K9TwXBWZpUJuiRGIax_66YRHxDcTbQeGUQt-5b1OpCidmB3CvZStS1oQktGrYm73Auksvwcw0ODh1RAQClC-uY8I8Bc7H2M990xx5YRgH4HeBtRfolZsG3JhebCSXScU7yuzXc4GL5elT__LvsWlLPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔵
چلسی در همین پنجره نقل‌وانتقالاتی حدود ۳۴۲ میلیون یورو هزینه کرده!
💰
💸
خریدهای آبی‌ها:
🔺
مورگان راجرز
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— ۱۳۸ میلیون یورو
🔺
مکسنس لاکروآ
🇫🇷
— ۶۰ میلیون یورو
🔺
مارکو پالسترا
🇮🇹
— ۵۷ میلیون یورو
🔺
ژئووانی کوئندا
🇵🇹
— ۵۰ میلیون یورو
🔺
امانوئل امه‌گا
🇳🇱
— ۲۵ میلیون یورو
🔺
آلوز دنر
🇧🇷
— ۱۰ میلیون یورو
🔺
دستان ساتپایف
🇰🇿
— ۲.۴ میلیون یورو
⏳
بزودی رسمی میشن:
🔺
والنتین بارکو
🇦🇷
🔺
جردن هندرسون
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
دنی ولبک
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102369" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=JujY6rh-ApD70dgD0r0jlnLL3TWDRZfT1siS2WdEMix6dpwHbcsXZ4MeavUStwzZ1HiCc0O_LtlCyU9I9xMsZvzdu3m_jIQEt8JWbQkSqkJxlFYxfwWZDVmeO-rm0NfWZNVRzJ-EX53PS47ESENUQ6SyKom1Ds70YjWsL6r5cmEhc27ImJm_fRylN7QiUKLPPLWaEG3hnlnBnFjeMhOuwrwxe9-WvCuXqQ6D8E4o_ICfURVNVzQV5MhpKvwhwwMxaqyTnJy0KB6HYjRc16ExUw7fMnqlwD0kn00QjHys0Bv1a5IbUN3lbNCnc6vmFU7dat1bjOmFyVsEFiumnVXzww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b486c4e528.mp4?token=JujY6rh-ApD70dgD0r0jlnLL3TWDRZfT1siS2WdEMix6dpwHbcsXZ4MeavUStwzZ1HiCc0O_LtlCyU9I9xMsZvzdu3m_jIQEt8JWbQkSqkJxlFYxfwWZDVmeO-rm0NfWZNVRzJ-EX53PS47ESENUQ6SyKom1Ds70YjWsL6r5cmEhc27ImJm_fRylN7QiUKLPPLWaEG3hnlnBnFjeMhOuwrwxe9-WvCuXqQ6D8E4o_ICfURVNVzQV5MhpKvwhwwMxaqyTnJy0KB6HYjRc16ExUw7fMnqlwD0kn00QjHys0Bv1a5IbUN3lbNCnc6vmFU7dat1bjOmFyVsEFiumnVXzww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🔴
🔵
تاجرنیا: «ما و تراکتور، بصره را به خاطر نزدیک بودن به مرز، به عنوان ورزشگاه میزبان انتخاب کرده‌ایم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102368" target="_blank">📅 19:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntX01kjZazy6CIpvqTOWl2FYvDG7Mp8AZAZdXIVLlI9GCi3mx_xkXPQC2KqqCwNXtWEGnbcy42oQf558C32-jeYrlvNH9YmzvybgIf_1gcEKJMa6z2eGylNa_fAWVe3E2YjqOvYprti4-WKPcPZlRszFqBgkKN0OVaw_cFzhMQ3eYzGl6HgQ9A-vP5kvndP6gfBf-kc3c46-rBGWyIdpWnetCBXhbeRTijpGBJoz6s34p_YZOYWWpADMDLkyxi7Zrp6C7lpVmuwrwfiYy_zNDzs6jfwEcSk-hnRBUfQbHP4uXgvb2lU2qPBRUHrqcWVXs15PpOgJduP8hBwHrlx1ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
✅
تیم‌فوتبال پرسپولیس در دومین بازی تدارکاتی در اردوی ترکیه مقابل آلانیا اسپور این کشور با تک‌گل علی‌علیپور به برتری دست‌یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102366" target="_blank">📅 19:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG-tx2tjgiDnIu84adobHKge7qEACizyJtPrCm7WhQNYgPopnSuk4MEmQrxc4cqaTmgNIjTHuJl-OrNErEwWtrvtanMwMpbzghexfKSbdtbaH-ae6_4OQX3HxintiOxF1w8ekd_3kRxVWZ7oJMqZGxYX7GKmtSUTlLUcdjei95F1oHc2Gx7ppUKyV1neM4quoZkkIRMkbpkd51ReL7W5i75LoMu-Jfd_-pesU9E7yPBIvaZrV2WHOJkEXLXieK_q2BprwDf51qK6yyY4IgWZUWUBjJJDJBPwQWNMH1gyqc_azWBi_TjbeROhRBuZqG-2EapOD03PzoWLGWNt4vlYXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=KepfJFsdYkrUNU9p8f8uplutuH2q9U6fOdTv9XYeiaaOz28NP1J2GFXsByYeYQe22nKhV4FpJKOW4yxZJFjz-voSechc3LhdUcdKt-haQzOyPEzYWAf2tJa9NzzR0CE3PAY_E-WcAoE3SGw4vtgAk5c82_I-92mtHv0BbjsoXS6MdvRN92VF1AUtGsq6KJcqAaEoDTwenIS-IS5NiRVycxdbWBRHjmb9BRHGqimDkmd4nexDpVrxrkaxTzhi-InK8ArqsL2hHvVyXKD7Rgy6WgAbrJURUwyDKVj2zVbi0oLxmzUvX8p9hEbrDKPDrgJhCiQISDcB9rVHdfiOQ9hzNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08c0c36c9e.mp4?token=KepfJFsdYkrUNU9p8f8uplutuH2q9U6fOdTv9XYeiaaOz28NP1J2GFXsByYeYQe22nKhV4FpJKOW4yxZJFjz-voSechc3LhdUcdKt-haQzOyPEzYWAf2tJa9NzzR0CE3PAY_E-WcAoE3SGw4vtgAk5c82_I-92mtHv0BbjsoXS6MdvRN92VF1AUtGsq6KJcqAaEoDTwenIS-IS5NiRVycxdbWBRHjmb9BRHGqimDkmd4nexDpVrxrkaxTzhi-InK8ArqsL2hHvVyXKD7Rgy6WgAbrJURUwyDKVj2zVbi0oLxmzUvX8p9hEbrDKPDrgJhCiQISDcB9rVHdfiOQ9hzNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
اولیسه درحال لذت بردن از تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102364" target="_blank">📅 19:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102362">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EpXeFkh23xU3X4pXlen3rukPcDRXj4pvYNztm2VRuaqcdqTiByF7uNPT8xxNO643lslF91Fq5pP00kPwgL9xeeyT_SwBo3DjsTPnvUcVour294-_327S1td73dBPAn-TM5EbO5r1wxZcx77-K-jRfw0br1evOteHnvvi-LZr7RW_9sKamjtfSEmpg8KF1S8LxKR-bOo3LQ8s57liE_nrVUzcdCP4FqRs5SvFuy9Fucuhes2IOnjLXHs-gWTv3RRm61nfMSAjact8gyAUOuhty6hPuc75gx44FBulbrQzO7yNMBxgQRmB4F168JJkmwairnQD75n4tk8m9Le1ccFLkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=BkRC7kkRPcAe0_JDXBdBkZSHCB4rKINWnlX_O-nnqhVPE3rlldClBXosKk0SBGBoa4aJKpuIl4y5k5uyxlSvS3zW8zykVVLcKlrSuVFGA0bZ1TFnYsffw5AwUJse9Z-_aXT7KD7rheLA5OZngYJ8fWKDWUdxxpKX-9u7ZJt3OTbR2c5NOEREcfQvptOvvrDSZ5az9wBBDSgtx6LulEOPoN9oNI4lRvcTpVDKHVzCSJQRRglQa-FoFQoWos7_CNv7h8yBSi8OkNffrwqdPmcrT4MXredb88U3mgBIANH63MweAipm0M_7WfmC3aLDLd07YLxiOpiQcS-NzB1YgnHHFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3645ae0183.mp4?token=BkRC7kkRPcAe0_JDXBdBkZSHCB4rKINWnlX_O-nnqhVPE3rlldClBXosKk0SBGBoa4aJKpuIl4y5k5uyxlSvS3zW8zykVVLcKlrSuVFGA0bZ1TFnYsffw5AwUJse9Z-_aXT7KD7rheLA5OZngYJ8fWKDWUdxxpKX-9u7ZJt3OTbR2c5NOEREcfQvptOvvrDSZ5az9wBBDSgtx6LulEOPoN9oNI4lRvcTpVDKHVzCSJQRRglQa-FoFQoWos7_CNv7h8yBSi8OkNffrwqdPmcrT4MXredb88U3mgBIANH63MweAipm0M_7WfmC3aLDLd07YLxiOpiQcS-NzB1YgnHHFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول، رپر آرژانتینی و دوست‌دختر سابق لامین یامال، در مصاحبه‌ای مدعی شد که رابطه‌اش با ستاره بارسلونا فقط برای بیشتر دیده شدن بوده:
راستش باید اینو اعتراف کنم. مهم نیست وایرال بشه یا با واکنش منفی روبه‌رو بشم؛ من سال گذشته فقط با لامین وارد رابطه شدم چون می‌خواستم اسمم بیشتر دیده بشه و به کار موسیقی‌ام کمک کنه. با این حال برای اون خوشحالم و امیدوارم اینس مثل من ازش استفاده نکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102362" target="_blank">📅 19:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPOzMjdZYpx_ebs9IBvSSQIsYKjmAf-kTZO11LYKM2BKt5gDpxeU8Iq568zL0KOubZiwgNpdG1XQzfHyzbnriwrPgg8GTJDiU4QQ-OlD-i4tgyyBA4k4uOZkY-nN4bNOHX0NloXttFlZiNxC9PTds_c6WhnemuSVhTMF-Hgkfv5Vo-TWLmdaVGfwpNtlhYjJMqfGT8F5DPIgdpahM8r7CX9QwZYzKJnBktZde_l4cjoxfKSOurGwPWh1qNsrWTeDfO_xNHUQ3kSnSZv9akDSp_cra-opKu5AXX4Cuzmz77-ct6gKJE99TujGxQJqT-QrGeTWk9AoRAx3DOy1EGK74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuXaC3luXjTqUxgJ75aQ5Qf2oaelprEYUL_ugeD8Qr1zcXg5PXQ7NLt4JGIpOvxq6tvmHN5a3e2ScHdW2Qa_ToqmOOgQLYvPPzOFJPcDFryr_UxOe3KqrUcnP1l0JEgjGWIyYJdk3fE3iMuRFn8ivVXNSR-1ZTLnp-vmTmizcJHGr_H5rRUEVwVORT3VBBs_PP2PzQM3hbnHETdBk1fKFg4h3a-kjrzj8Vf2LXcTGIIenriYE2LOF1CtDmLLGz8sqO2GGZ0c95xoWjW7n2CT5LSlojj3TYsYzz5tXrXJKOY9_ot-kvF-N01f3Qs7i_p6amw_7T3NJ-VSDAhkuIXocQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇦🇷
طبق گزارش‌ها، لیساندرو مارتینز و الکسیس مک‌آلیستر بعد از پیروزی آرژانتین مقابل انگلیس در جام جهانی، برای خانه‌هایشان در انگلیس نیروی امنیتی خصوصی گرفتن. گفته میشه بعد از حواشی جشن پیروزی و نمایش یک بنر جنجالی درباره جزایر فالکلند، به خاطر بالا بودن احساسات و احتمال واکنش هواداران انگلیسی، برای چند روز مراقبت امنیتی در نظر گرفتند. البته گزارشی از حمله یا خرابکاری علیه خانه‌های آنها منتشر نشده و این فقط یک اقدام احتیاطی بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/102360" target="_blank">📅 18:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102358">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2-Ku3gLHcFYy5MfglnMUuZiJq11egvS0cPJvuQYZ5ldmMU-QJuLJi9b6QsMmCRqteMsPQlXJDhmOgHw2Y8j88Bs76B2d9V0zTorxdtHZH8rjzZQ7YgJHEl4fg_cJEL_fO5PwYRqrdArMxF3sh6qotBYcKUWUx5JRS2nHEmthC4i4EC1Q93Mdmuied9XxX9l__wLbPZf8izF1-UjLC97FFKnqNmpfT9T6mX_sr4sMRKISZc3pYyY_iZ2YqORY6btYNY4rmxYbsE9JwQU4ldEUEoKDvfFyrb5LussEvsvAbvfFxeS2bPcmjIR0dqgv8Ih1tK87IelOvc-ei06X11FhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5yUxtIT2Wdr6fbKYvG8xIah8sZDEndWb1xapodokAESRTTs0TF1okSQh6mlRDKukd4mwKUZ4QUiu6pl6X55WcRnIecVW9U31tPVonjlhEgAKvyvlH9odpARIs5EfEvqFdzuF8fS6Z3IQMKUX4junuZsotFBdf26lX-2H4eN5gDHDJsLukksuKGTqJJoyJi3AuXnPbNvdbh_DvRm2sUuJ3HyWebJUmK0tqANFmEEGhm1EggIutJWYIcRMmA5CjoowiuhWccIQMrTpX7oJkIKG664k1cH_sERJcEEHTBUC8yCfck3FHBqpWlYNeIdytaD8vGy5hJbRgAt8665nh2XyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
نیکو ویلیامز و دوست‌دخترش آینهی گارسیا جدایی‌شون رو اعلام کردن. طبق ادعاهای منتشرشده، گفته میشه آینهی نیکو رو در ایبیزا و روی یک قایق در حالی دیده که مست بوده و کنار سه دختر دیگه حضور داشته. بعد از این اتفاق هم وسایلش رو جمع کرده و جزیره رو ترک کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102358" target="_blank">📅 18:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102357">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=cagHr4JxO4wih6brTRg0t9CVPiBKEVceLZCu5_1P6OKwt91XAKTQ13x8l9cXRDtWF3vh71Kjq1XaIPikBFw_Fix_oEzCeeNDOAkgQIyGr65hhPRwYOStFvxqB5UPHFS5B1XMJRbXlUNZjYt8I51NpKkqZtuBkjNAZLNIPEmLigxCxJ0w_PRcsq5fl1-xRfdKIheZbz5uCwGsA7X_cfSvOS5iUjzSgHwXSCn0itF0dWjautXQLurKSx378eoSxaZchRNLSqee-YwkQn9iW0aKdmfp1QEamJjqcCgSlnHwh7QT8fznjVJOhDxM2LEiFZpjvIidI-v1XB9XEJ23FhTTLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14e33cfddb.mp4?token=cagHr4JxO4wih6brTRg0t9CVPiBKEVceLZCu5_1P6OKwt91XAKTQ13x8l9cXRDtWF3vh71Kjq1XaIPikBFw_Fix_oEzCeeNDOAkgQIyGr65hhPRwYOStFvxqB5UPHFS5B1XMJRbXlUNZjYt8I51NpKkqZtuBkjNAZLNIPEmLigxCxJ0w_PRcsq5fl1-xRfdKIheZbz5uCwGsA7X_cfSvOS5iUjzSgHwXSCn0itF0dWjautXQLurKSx378eoSxaZchRNLSqee-YwkQn9iW0aKdmfp1QEamJjqcCgSlnHwh7QT8fznjVJOhDxM2LEiFZpjvIidI-v1XB9XEJ23FhTTLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی ترامپ‌نادان با بازیکن غول‌پیگر فوتبال آمریکایی؛ بعدش که مزه میریزه از اتاقش بیرونشون میکنه
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102357" target="_blank">📅 18:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102356">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=lzDiOPSoc9CogHJf7gphw836zxQ0ENf1RO3hcRzwTw_Ukk8VmZIlp1rx1QeQYM2ZY717EuRS8t0hNLDv0oBAdCxwvoyinGMz_5f-yOC8DX0FfTCiF00X01IhM3-_6gZYA6OyExBmtPUCHFZT62UzrvSZnzRcbPD1K3YsiBgMVpv79owlrd1NIjw5wE5dcHJd1wiHaLTCafJbi1CxaST8cZyXhAyDALFANA1uu-G_bGkPz5xpEOQD_JgH5_2O3WpyuCeA573DrIxdyJTtOZOzwKYxWVi4DLBPWQdIr2Ua5oIvb90k_sS0NBVUVUIaCox-12F0H5JDYiQxX38MTRtZm5gViClcKchXh5wq9jYC4KsRtqrnfssnD7wLSvUMoM3NtulkHPpT-hKT8qNofS9ahDIbvETboZc_N7p3o9v59cdyrRGTVzJmvxVp_A30MUEPXtPeJ3WmI7306EV09selDMKu_iH0smeHJVVvtCi0OfRSMKLM7onobZi8HZ1sR6mT2WDzPZQthG8IGatCird7RKZ9hsD-tvfqWw3b9uuU1vb4OINhCLA5dq8dDTUQap450cLk1Gl26wiWKbIaQMh76D9YGIETX9-FiCzQeRUkOkYLBUBoURrIZsH4S--oVqXHyE22ShPPAY3eClTKMVKu2xpLNL5-wC3iVqoRr5nhtfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff5a8032cf.mp4?token=lzDiOPSoc9CogHJf7gphw836zxQ0ENf1RO3hcRzwTw_Ukk8VmZIlp1rx1QeQYM2ZY717EuRS8t0hNLDv0oBAdCxwvoyinGMz_5f-yOC8DX0FfTCiF00X01IhM3-_6gZYA6OyExBmtPUCHFZT62UzrvSZnzRcbPD1K3YsiBgMVpv79owlrd1NIjw5wE5dcHJd1wiHaLTCafJbi1CxaST8cZyXhAyDALFANA1uu-G_bGkPz5xpEOQD_JgH5_2O3WpyuCeA573DrIxdyJTtOZOzwKYxWVi4DLBPWQdIr2Ua5oIvb90k_sS0NBVUVUIaCox-12F0H5JDYiQxX38MTRtZm5gViClcKchXh5wq9jYC4KsRtqrnfssnD7wLSvUMoM3NtulkHPpT-hKT8qNofS9ahDIbvETboZc_N7p3o9v59cdyrRGTVzJmvxVp_A30MUEPXtPeJ3WmI7306EV09selDMKu_iH0smeHJVVvtCi0OfRSMKLM7onobZi8HZ1sR6mT2WDzPZQthG8IGatCird7RKZ9hsD-tvfqWw3b9uuU1vb4OINhCLA5dq8dDTUQap450cLk1Gl26wiWKbIaQMh76D9YGIETX9-FiCzQeRUkOkYLBUBoURrIZsH4S--oVqXHyE22ShPPAY3eClTKMVKu2xpLNL5-wC3iVqoRr5nhtfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
یادی‌کنیم از کینگ‌کمالی از اساطیر بدنسازی ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102356" target="_blank">📅 17:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102355">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a15854e8.mp4?token=SDG9U6C483ktaxEZjNtKOAYWwpdU9MtVHPluTSBL2ERxPDeNaFnidgb0tAPz7gY-4u-H-V4gtvQapvnY5n8b1qWytHOc1C75HpDuATB7a74fq-ZWBSe5FECGZAep07OH6-4VJPIRcwT5AxeTvafZbpmcy_XBn6KglTKsVtqL2XsmbpbmtzLp_Lqq-t0p-s1l3RjvpmereEWGYX2ojBBtINdSc1EM6UW_MTMCEzwajiay3Fiizp90dbZw4TMro1TV2l8jNK7e3LyoYuab5SysJ-ybYSOvdzjCSZ2jdnXD5aG25QqyL7UfFDb5_y4X7_-hPyezvNHJUorxn17qf5YxAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت این‌روزهای هانسی‌فلیک در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/102355" target="_blank">📅 17:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102354">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=IvjhRdJQ-bp3V6_38TcbqP50QRl-x6NoC2h0ax5prspCVVwiz5oB72ZaN6TCz7_ai-c-K1w9RQuCrGIB3-CDWNFuVeVJjuYTJGRmnvEtyJNN02Jma9ksfHMgV_FG12Yqqp7QvO_fTJ9cOOKYsD30DDnZRmC1Apz9GxRlxVoymWZRm6Lq3QKCtxNHQbEu7nkUxT-HrWK3RmhiPtEQKM3W0TWgrxM90YBF7EAWBmkvsGSU5_Bgr8QquqngSxezs8hXyBFlylgUnUyEBxPlNIyGwJZjPNB1E4c4VGauy1WmEXPUVQVMFtjVMFe7EBD_7bqrlVKikcofUglIpMr4ogOwwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/262bb95a39.mp4?token=IvjhRdJQ-bp3V6_38TcbqP50QRl-x6NoC2h0ax5prspCVVwiz5oB72ZaN6TCz7_ai-c-K1w9RQuCrGIB3-CDWNFuVeVJjuYTJGRmnvEtyJNN02Jma9ksfHMgV_FG12Yqqp7QvO_fTJ9cOOKYsD30DDnZRmC1Apz9GxRlxVoymWZRm6Lq3QKCtxNHQbEu7nkUxT-HrWK3RmhiPtEQKM3W0TWgrxM90YBF7EAWBmkvsGSU5_Bgr8QquqngSxezs8hXyBFlylgUnUyEBxPlNIyGwJZjPNB1E4c4VGauy1WmEXPUVQVMFtjVMFe7EBD_7bqrlVKikcofUglIpMr4ogOwwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‌‌ ‌ ‌ یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102354" target="_blank">📅 17:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102353">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKkzAgkg93D1wYzIYPSxnucKmLru7JYhjSZ0LC3o3PNpcGlH-5XAXw68jHkg_qfRTM2ziL_-nH50BwmzX-mH1juCBLW_Em86y4Yj8JiHRBAT1Lj_1MrPV67KoJc5NqxnboAh4XiGYqdxuNkB31gRPU0ng2blqPT8fRzsypJZP-0v5RySzGCl4OSCJYhNgv3sPMQk3NdNImYgmAmtjXNZ5sqAX0_KeWLAIygytDtfupfqmNLmSwKTLV6JaGTDX5FXeRV2ubeQfSw_UeKbkwj_VrkJg3Q8sAP3aDZOCG-QNt7KwL1PNYsJdA8qwttGxjGLVOLQx_BnWGZENHa_iedO_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🗞
رئال مادرید، پیشنهاد رسمی ۵۱ میلیون پوند برای جذب رودری از منچسترسیتی ارائه کرده است.
❌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی قصد فروش او را ندارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/102353" target="_blank">📅 16:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102352">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=YSIrhcwo4e5ULqmeIbb9inUskpazAXhjs1PDPt4_6y2E6fRRJcB2A4GDMyTnG6q7a2p2p8t0Fj67ktU-aVzX7DoNnHDGLeUV2mqkW8qtYRDKukNGBwPwxtIozP593bCE1bOyzxXC76RhCZu5__HIrR8bv_kRbDuvjPPwusb_FknrUbt4TF2zv2K_ZSzxKUEXAByuWp9K0NUFtGZjX1VYNr-AG8Ade3DZdzQfb_v9T2BW408xFEH-w4RWacr7Halvm_3nUD-a3quZFxXyO5M-6N28cn9p3Nr4M6GemUDGTHHi64hJFs1k3UwiHStf9Cpss0dCuWapm6gBcfLwOknhjX5VpP_75RVXnlkuKuCPSc6rMOYq3ZQgFwuLTu9o3pimnKQICIy6Irls3QgAmmIYo1FZJQGocAjneENUt7d0d6jKg8q1HNGsfMwC_bFgrHrbjNlkNRtS4KJjbHS-PYkWUmWd-gsovW5DnAlXCLuQNgnjqPnigcDan7bNyv2PABRoTIKsxDaFjD_6ed9L5jB985tXVUP-P966pp9GCBoUmHwhcmxy3Na4Zqvoyq77PosqvlS7CP6G9H5uWImGRa9VqsI-n-c5mCDYwDqDIiEqqWfYfoEhQQv7uTRfbf36tJ92onUKShG4GL9uQNCNMLnHN7SXqTGTBD5G_OMOj0eivAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17f25fd06c.mp4?token=YSIrhcwo4e5ULqmeIbb9inUskpazAXhjs1PDPt4_6y2E6fRRJcB2A4GDMyTnG6q7a2p2p8t0Fj67ktU-aVzX7DoNnHDGLeUV2mqkW8qtYRDKukNGBwPwxtIozP593bCE1bOyzxXC76RhCZu5__HIrR8bv_kRbDuvjPPwusb_FknrUbt4TF2zv2K_ZSzxKUEXAByuWp9K0NUFtGZjX1VYNr-AG8Ade3DZdzQfb_v9T2BW408xFEH-w4RWacr7Halvm_3nUD-a3quZFxXyO5M-6N28cn9p3Nr4M6GemUDGTHHi64hJFs1k3UwiHStf9Cpss0dCuWapm6gBcfLwOknhjX5VpP_75RVXnlkuKuCPSc6rMOYq3ZQgFwuLTu9o3pimnKQICIy6Irls3QgAmmIYo1FZJQGocAjneENUt7d0d6jKg8q1HNGsfMwC_bFgrHrbjNlkNRtS4KJjbHS-PYkWUmWd-gsovW5DnAlXCLuQNgnjqPnigcDan7bNyv2PABRoTIKsxDaFjD_6ed9L5jB985tXVUP-P966pp9GCBoUmHwhcmxy3Na4Zqvoyq77PosqvlS7CP6G9H5uWImGRa9VqsI-n-c5mCDYwDqDIiEqqWfYfoEhQQv7uTRfbf36tJ92onUKShG4GL9uQNCNMLnHN7SXqTGTBD5G_OMOj0eivAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مملکت به شدت عجیب و غریبی داریم
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102352" target="_blank">📅 16:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102351">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/138f735fee.mp4?token=r_xkn9wXsANr6RXDo9CW3gVEGsA1YpAzWmFIs9eFU0DA1To-r4lNWpqcmHTAwwAO4ujCy9VuCe96IP_ICs924tveecAZm3WTdT_PlV_v2CrztdUTt7xbQ6UROqWqk_hr5L7Ka-ZI2hWCZAz73U7ld0yGkdTdLZtLwHJFwaNVmrcrwH05OoEFSKkkbQiuOJ7v2V_PYyKQa4wGD9Y_7zrCk0fT2qo2IAax5so_BL-RrcuOSR5fk9XYm-2adHMJkIaxCZokUu29AOxfYJkP9WjlMN0s1gK2hVXoLFyW9n4vpNMWg7QwkLdcCWtWVcB_urqay1ays0DkQrR2qZak2eD5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/138f735fee.mp4?token=r_xkn9wXsANr6RXDo9CW3gVEGsA1YpAzWmFIs9eFU0DA1To-r4lNWpqcmHTAwwAO4ujCy9VuCe96IP_ICs924tveecAZm3WTdT_PlV_v2CrztdUTt7xbQ6UROqWqk_hr5L7Ka-ZI2hWCZAz73U7ld0yGkdTdLZtLwHJFwaNVmrcrwH05OoEFSKkkbQiuOJ7v2V_PYyKQa4wGD9Y_7zrCk0fT2qo2IAax5so_BL-RrcuOSR5fk9XYm-2adHMJkIaxCZokUu29AOxfYJkP9WjlMN0s1gK2hVXoLFyW9n4vpNMWg7QwkLdcCWtWVcB_urqay1ays0DkQrR2qZak2eD5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
برترین‌های تاریخ از زبان رودری ستاره اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/102351" target="_blank">📅 16:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102350">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇪🇺
🇪🇸
یادی‌کنیم از آخرین قهرمانی بارسلونا در اروپا با مثلث تاریخی کاتالان‌ها در خط‌حمله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102350" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102349">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnpIOnR2D4qvWnKFNJTwGlfpwnqGXLI85y4vorj--saFRG99Eqeg2P8t_yHwimNfFXBoUUyZGn-d0o0nlgtFdDG_pYFKINOEjTU_ZsCk4_SXNqFgLll58GLuFVX7QfGkywjubkUXU8j4GkN4PLMoU1j71RrqeCfihrF2kcc71U9hwsktXhGgtPKnJMYv2b4iMG9_0iUWuT0qt3-4TFodLDVyojr-cZGhd5ij5hvhIzL-BddrFBBsbsBoxHLalUe0QBIAycjPZhdAZuGJpqQWXJrBx362F-imio42RHasObhYoOpys7z09xOWRyJxsMDyJKc_zTjLzukL3YZxRm93iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گونزالو گارسیا به فولام پیوست
۴۰ میلیون یورو
۲ میلیون بند پاداشی
۳۰٪ از فروش بعدی به رئال مادرید میرسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102349" target="_blank">📅 15:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102348">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=S621ULuACfAKB2DXVg6e-2zfpKJbhwtEzRR8fykpKOf1S_FtXCYUBB5-BDeDIjA86pHzt_gNSeRLbig2le3a5Q9Xe-hxLtk4PRBY_sTCDYl5JK_0123Bvk4ncQ0aoQbAHcpFBz6qtObkKU8pahuKIujPchP5vPSmCTLUJ4TUhfMn4ENolUI35_oVFIPltY2XP5PHML_U_CmsO2_0eSNOaCZCQwP8BtPVGToefAnk5Uvx1Nj-gCtpNxoCt3KGdVeAj_6F9G0-9u9KiL-ua1iZqVRJs2vD5Cxezn1aO_MGj0LwTjN1h_y7fRP1QaSeUQSPzyTRNxaA89YpcQFYqqK4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88e7b9804.mp4?token=S621ULuACfAKB2DXVg6e-2zfpKJbhwtEzRR8fykpKOf1S_FtXCYUBB5-BDeDIjA86pHzt_gNSeRLbig2le3a5Q9Xe-hxLtk4PRBY_sTCDYl5JK_0123Bvk4ncQ0aoQbAHcpFBz6qtObkKU8pahuKIujPchP5vPSmCTLUJ4TUhfMn4ENolUI35_oVFIPltY2XP5PHML_U_CmsO2_0eSNOaCZCQwP8BtPVGToefAnk5Uvx1Nj-gCtpNxoCt3KGdVeAj_6F9G0-9u9KiL-ua1iZqVRJs2vD5Cxezn1aO_MGj0LwTjN1h_y7fRP1QaSeUQSPzyTRNxaA89YpcQFYqqK4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
💥
حالا که بحث تیم‌ملی داغ شده، این تیم‌ملی و بازیکنانش بنظر از همه سر تر بودن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102348" target="_blank">📅 15:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102347">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=Q866UQGDBtXEbhVTjb2WO6FSTK2Q5hSwmJ2reUjFNRWz1xWTaBpIRcgKzS7WrEvb2jpwb7Bn54du6QOSB53u9c5wPXQqzHyShWB3ziBbQBj2JKjW02Vhl8tWS2nvK1dfgeu6rFoC34d60MIlajAyZSWehEs2ghqY50go7XsoH1CNFOuktEDJtwLSONLxDqN-mue2XA9zek9APZ5fvNIhhmpAoGxpgDzUUQPrt1P6daLWbO6D-usLSq_Wd6CkuDR3S-MNVQP474qpCWzTM89hnHZG1m_ukvdBn1RjuoDd0bm1D5IggJKgGlOMuLnqKnkxqwXiN4s4bVEau2GLFS1OsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0063915b2d.mp4?token=Q866UQGDBtXEbhVTjb2WO6FSTK2Q5hSwmJ2reUjFNRWz1xWTaBpIRcgKzS7WrEvb2jpwb7Bn54du6QOSB53u9c5wPXQqzHyShWB3ziBbQBj2JKjW02Vhl8tWS2nvK1dfgeu6rFoC34d60MIlajAyZSWehEs2ghqY50go7XsoH1CNFOuktEDJtwLSONLxDqN-mue2XA9zek9APZ5fvNIhhmpAoGxpgDzUUQPrt1P6daLWbO6D-usLSq_Wd6CkuDR3S-MNVQP474qpCWzTM89hnHZG1m_ukvdBn1RjuoDd0bm1D5IggJKgGlOMuLnqKnkxqwXiN4s4bVEau2GLFS1OsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌بامزه از زبان فیروز کریمی
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102347" target="_blank">📅 15:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102346">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2314f18179.mp4?token=qBCv5REgR31hUiX_OHKwNium-4QteJeRZwmU2-d5diXw7faUp6Bxn9MduBoxFNrV5k34fH3dpuOVAb2sFd20gL1mAiGMTk_CrpXHhQY02FM83sXhROC5OpNQxuo_gm9iwYSVor61kB2Fz0Oc9hpkcNNtglv_zIEdJaTyydlwn_wwOBtUVt9EQOJYEmLCQ4OuR5M4qrvyXb5IoawojBdex-fuh7dRaXIh-xyinZG4lsmat74rm5eLpFdRxVi74lz2tPBoKMLk9NtDNPgoUkYm6-ekIliOZfXudqswqrRCkYlKaxFI9AapXShaQ9UXQTVnLRylWzFa97bH3YTguk5zXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2314f18179.mp4?token=qBCv5REgR31hUiX_OHKwNium-4QteJeRZwmU2-d5diXw7faUp6Bxn9MduBoxFNrV5k34fH3dpuOVAb2sFd20gL1mAiGMTk_CrpXHhQY02FM83sXhROC5OpNQxuo_gm9iwYSVor61kB2Fz0Oc9hpkcNNtglv_zIEdJaTyydlwn_wwOBtUVt9EQOJYEmLCQ4OuR5M4qrvyXb5IoawojBdex-fuh7dRaXIh-xyinZG4lsmat74rm5eLpFdRxVi74lz2tPBoKMLk9NtDNPgoUkYm6-ekIliOZfXudqswqrRCkYlKaxFI9AapXShaQ9UXQTVnLRylWzFa97bH3YTguk5zXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
تمرینات پیش‌فصل بادیگارد لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/102346" target="_blank">📅 15:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇪🇸
🔥
۵ گل زیبا در تاریخ باشگاه بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102345" target="_blank">📅 14:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=KMvCdXC_IucpcPgXbsCELVL6jX4YTs5vlOC7gyBxVrCbeIzRIo55QfGl6GtNMDgAk1pB6fTapIR1hPwO7cH9DBmgb7i3FmGn6N3TFYU7pBg3CrI62H0T0oZGybdlyI66kC-3cAkkgW7ws64qGyPqkeuEcazSrCdk90_ZuDymzZRAUpLOLxeXcRQZ77cgq_6-FVd3uQDLbOXeEHnsB1mejmcasKra8Fz77ELvnvqEr0STzzHZEPyGbVEATOebq5yLZEibs98msQA5evcbHypiKDxGu689AG-ON-7ThPTucTIDqQtb1Xh4WMT1G3VKJkuYsj6FYV14LUus8d0ideUIObEo_q7NWYB1fcsd--TjePYpzRms1kZfEEc4ebD7X3noN-EHrd5i_2cTTrBs1FOJjB1_1ARnKZjICfm3uv9lZEa5dPu7wu0-6Hujcxc59elJHWzqYsPKQvBfKDrdAG7V2B2v5Xna_jmFtnjqH1evRMxsGajUhklv3GB0XztlMBBkHkPHFXXlntm64sTfhFqFXUegX3oTA8oyJiIRi3_HKeZ92etKMtMlt8fryVHzLyBdThMuAdS7WB4lzEE4IjkmQBKFIsu67KnUMHnKF8jIyEdx-slq5l5fjEJPhdESte608-lUKzApX4XVDae-5D8orBcZ98Jjo1FZn-_yQ9vNJeo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e80cceff6.mp4?token=KMvCdXC_IucpcPgXbsCELVL6jX4YTs5vlOC7gyBxVrCbeIzRIo55QfGl6GtNMDgAk1pB6fTapIR1hPwO7cH9DBmgb7i3FmGn6N3TFYU7pBg3CrI62H0T0oZGybdlyI66kC-3cAkkgW7ws64qGyPqkeuEcazSrCdk90_ZuDymzZRAUpLOLxeXcRQZ77cgq_6-FVd3uQDLbOXeEHnsB1mejmcasKra8Fz77ELvnvqEr0STzzHZEPyGbVEATOebq5yLZEibs98msQA5evcbHypiKDxGu689AG-ON-7ThPTucTIDqQtb1Xh4WMT1G3VKJkuYsj6FYV14LUus8d0ideUIObEo_q7NWYB1fcsd--TjePYpzRms1kZfEEc4ebD7X3noN-EHrd5i_2cTTrBs1FOJjB1_1ARnKZjICfm3uv9lZEa5dPu7wu0-6Hujcxc59elJHWzqYsPKQvBfKDrdAG7V2B2v5Xna_jmFtnjqH1evRMxsGajUhklv3GB0XztlMBBkHkPHFXXlntm64sTfhFqFXUegX3oTA8oyJiIRi3_HKeZ92etKMtMlt8fryVHzLyBdThMuAdS7WB4lzEE4IjkmQBKFIsu67KnUMHnKF8jIyEdx-slq5l5fjEJPhdESte608-lUKzApX4XVDae-5D8orBcZ98Jjo1FZn-_yQ9vNJeo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فرشاد محمدی‌مرام درتست گزارشگری سال ۱۳۹۴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/102344" target="_blank">📅 14:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBA2oerGMH-xyhJvjkcEoTrFgBubr-zVzX0dYWmuER3CmdeJawHFZwCR2Lsj1G2ifY4QvrABY8rzN0JHm8vJijdAEDYN0kMMc7NKsnkY_bTkNpPJoCoRj0cuG9Bi5H_K8x91yYiP_5kYnCcbbuUK29TdD8tTKnEIEgxNnZ3OqjFp7a7wiK-UrnDK007B-NhzQ0e8vPM9y9AFMxImicvZsZiHID_SKqrRFbvgg1oQZ61ATnkCiEGKo0DjnXNmTRaUZrq1G_RhA4cuojkr5w7TCrtpuWUVQqqGIpsiarVdUyi5DA6_bAcLIlz0yWSK5pNUzJjCKaonDZaXLAlMoDiktQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔹
رسمی؛ نیو راموس مصدوم شد و حدودا یه ماه و نیم از میادین دوره‌.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102343" target="_blank">📅 14:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3336c43202.mp4?token=GIe8w5kyIY0GHizeyeDyUJmxZqsuAfR4QHS0txm5vxC0jDl2MU7yLBpfiXUr8vf26yjwu2pErGsAiJ5_CUwiRHg-e4aoJTioLDKWIv-IXd-Ac_3ZpUWhQAkQ69BEJo_lXMFS5tWdQ-2xQ_9-hiTTdz3AHs-NlCZF2eUx9IB7BMST9O3qWgumCHu4Fy285cfOJFuBBgVZr4DtIzKZ4B9o3W5K2Xg3306zSw2dzjlviYcbkj1oherJ3234MPA7bsfyicHPs23AJNeR-iM2VTN8gWgi6bpJ6UhvU9KsYwHL-QMYPFvljy-JBuNfUXu8A6Mxm6NPtwcLCpuHB_QcR0dSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3336c43202.mp4?token=GIe8w5kyIY0GHizeyeDyUJmxZqsuAfR4QHS0txm5vxC0jDl2MU7yLBpfiXUr8vf26yjwu2pErGsAiJ5_CUwiRHg-e4aoJTioLDKWIv-IXd-Ac_3ZpUWhQAkQ69BEJo_lXMFS5tWdQ-2xQ_9-hiTTdz3AHs-NlCZF2eUx9IB7BMST9O3qWgumCHu4Fy285cfOJFuBBgVZr4DtIzKZ4B9o3W5K2Xg3306zSw2dzjlviYcbkj1oherJ3234MPA7bsfyicHPs23AJNeR-iM2VTN8gWgi6bpJ6UhvU9KsYwHL-QMYPFvljy-JBuNfUXu8A6Mxm6NPtwcLCpuHB_QcR0dSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
رتبه بندی سوپر گل های فرناندو تورس ستاره سابق باشگاه لیورپول و تیم ملی اسپانیا، توسط خودش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/102342" target="_blank">📅 14:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRDvqvV2mBZuk40kmG15ZAGabSRHQmXqZm0R5uuNMYAFl5uji0cnITr37cDjtFcSYzOM33g7OS49AiNBME5Wa9vgPUNIiefkC-GXP0EHifhJHV3MLBmDaQj_XpraiIbIJoN9LOsdHqb4NXXmgG5T-SbFctt6C-AZnSVC13r6e4OX4KKVnuYhdsnexdtVvg9oyb3l0uJ1dcPuZj70c92nop06Ma92SfFKPqrnR3bhD0HPowau4LT__PAPSWQNRyb_VwKNAtNNVVgCQyDIiXqZOeYNZAhImrmHkx-NazJ5mlS2dWPsDWNFrfEc-7M0KJOf3khN0jHNSAbDQMPYnSIQPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102341" target="_blank">📅 13:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102336">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/knVtB2lxph_ZoVbHJHIxZ_AvIfb6queQDBFNwsHq3Im1UdnKu-DPNZnBriyifty8twVzNaRTCyRAVKueFpCLGEl29TDJvkFhta1ex_tjxmR4TseKn9oG0a9u94vUcBJMPmRYi4Sdp1Vy-k28ffXNzi6A0YF7wxxcENhp-F9Hn1Q9Hq16zUL1rum6fC5qt1rv0nqiFMXQEbvUnv-OpsFPtJLiayNjmsPe3K5LWII6N4DEVy_X3YGfRy5DR0x9-Dl7k3Z9mbban8oYHAC0xbiVQR-VFy2ud6pkw2HJ0VqCid0gWTV5whGT7kdV_aP5UOWnkRpwj5h15Soe6sWDy4lw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vzn0-14YSeS0PLuFEbGFY4ENxz1mw7Z5orENkuQibE8LGqpt7NSHH5CoGyOL2BUD3FBvpunJtdHm-l3yBZF4dLMEJ8aO0kdEJrwdVsfqbokvIVW7rqlkZudyGtzy8eca6I9psXlkrTC3s9gMDqvHZx2CJgJGPlfLVtzzGpjRx2vv7cdGEB1skRCeruI5st0tun2V34CtLXKovvUaUIDu1y9yclJdxXUS90rB7YplDYYDTpsb07G81MYW3eS6jemVymv-YGgcFfKWrzHXk0aCnbLScMI4skG--BgifTxulpi4tvKvBaChGiCcGDpoBLTSutNwLugHlgtaC6TYhE3CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBYk_1s5frsqpgBr9il_A99OnX3yf4p_rLjtMYzRasp7J9-hvNVCFabbcniUwj71nVtNamzFs_sj0OfuJSYLhA64HzHBFRHi0QpS4EzaE7VeHirTh7DNGbEzDCEq5zNrAXtDv-uZ8LK6i_jE1svJiOl5S85naeTNbp6hBbBjb5IP5RQG68mOH3lzM-coCAhSHOZL5yqVqg5ZgQ_ec0Q-pmjspLW3RHW3dp7KyK86KHT6zySmf7jOcogwL7Vx5lbaFncn3orX3kE8Wh2csF32YS-j6f7FHqZLsG8L6NeqQL2l6zbAhSEgZAGHMphQV7tLAOi4MSGAYs_Jw2Vjpe357Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFfwkv8v6Mjd1uFFVrWIRFHcByy78e8GVQvYJj51Jhw0tWXDtgy21DouA6oh1-PjmOjeFXQCaEV1d895R8E_EUGvq-s0sbJqDVSb4mb6m7t-LQKldVB7AcJLcs3wHXAWQRqTOtrsEqM3Z2jNZLxGbFEuJVUl5hrxqN-Tnqtj2zSux6LP_BAhWH3_x66p1_yfFb8r9du7MDBYh_BDt2SiELgl5ju0bHjOPzDq5d6MMKanaZu6nZBGN4h9BsWcEOnLGzHYg3TcgUl6OIlWK83knBWQ7-RPwojG7PcEGBO2IbaoNULRv0xMyBFW6-5GuA_W6hvAtWfkZcJe-0Xsxt2dQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oaGgUOQow1cxdgGGh2Q99bXDV07XFbJKHfjTtMQ6JWjbfmgYhp_kewTNNEl8wRkiBDF9H4ZnC0gORjVrlksrHVkvYOYa-joSV0GNMW_dM47eIbaI9hSAptto0enIGdVmHiK2QS5pGKJ47lzDsyCZPHxz6PD66CMcckfFslJqF5M_PdRHfHQDgYapub348RalHrZbR6C5UWGmK6efR_6HqB0lBRO8InB3W6nwDwSNKRGMwyE_vHeS6LNHCAlGw8OQTHVrWqwpcOIpD_FOhdQC4BAmeDUK_hXX5wDQfbPbITLFK7-Y_nfZA2M4H-Be2X-YkicLaECDzZHsvFZ5YF0g1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">+ قدرت تورم :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102336" target="_blank">📅 13:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102335">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGPCgXWl9totEqFJ4gptrIoa_ORv1dl7japcO8L44nlKmDUBELImwikFRHY-A7_k3WzVsdF2uxJRozak4edRcnfBz-1DqWHF2PdNn0vpKNOYAg8XP4E1MG5ShL4bI_npF-si5IENeT0VrsathF6mFfHs9qEY7glVJCRtC0pqlArbmxIlwHz4Dr40sT7vCqOcSv2HePrXSL7fGLjFkse323FhA9wrtmvwMpoIALpYOLlCEdi36K61YHHBRJHZFB6UL1N98TReksVVotEnEiW8mMBtfsthA9S4rF4imXA4-Hy9ffOR9wp1FtZigVFJlNUycycqAyMG9Y3mBJWP2EIUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
💙
#رسمیییییی
؛ روزبه چشمی قراردادش را برای یک فصل دیگر با استقلال تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102335" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102334">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNHdYJOe559OG6S5JnIJDmMpxQ4DrPk4F69TYrxHqdmkc8yYh9-W-C1P7VpsVH6Hk9fGfPqZv-MZxcMQki4bYr2-5dYzwiA6fpgXj6zjcMvgBIeWBpjYgE40dbQWaRhtfUZ7m9TzqUe2V7KVv_W8QcvkJRUeXsDGKlcRWYQ07zmFgagj4FNUiyv74zyqs7Gqcmx44log8rhMIbfUhkK22-7MOxuBNkqZRWH3OvH_B0VALipjberqpWdGd_s27RexHFQE9Tth6ayCQxO9Xr2ajvUREA73D6l4NfMBAdoUG6i7Q9h_G0cGqE0IQbTzhG74MkkGAEv1Vqz0G8Y3H6I7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/102334" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102331">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPdICouNu_9PEYOfTDtHcbmDEARw9UpOt5BM752RMDlYTn_l_SG4lx3a_GDSj5M_Qwxlb4pXlzFx1PY4-wQGqMFYlnfYC6RgY18Bf9bsyZJdJrw30ARQi0oyWGYIzh6oRZP-sr2e4Ee_QqTiG5t-nNTdpCrsazRXRNwUq6_5e9dhMexrd6sgro5MuQGsFf6Nj9NIPo78YG-mIV0hsDrsJI_vn1D8eTWIWSZz1HL9DGqxkdasYhZNCypjKMXZMF0tGEggJsP3JWGt7s--sFvJhFfjvklMTaHVd9nslpbREHHh2NtEoowQprXKadyE3shjTc-q7X3xd6MnH-Gxx97cUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPbC12LqzMJWWCN9G8s40EfpCBZHYnlnSfAAEyF-lilWS5QKVABLxlIJ0l8z1sSWWk3DKjSNgRSemF1qbZDMJPHM_OA44xLLzG7yWnobWXvQzG4X5bGptwcFANTV9TKVILBY8l0q4YQMSnBxudHxERzoB9D7fdK8kNrbQ6FmgSianhlQ98fsONrFTdqQObTH311X5WoNoJzdf0BcL6IbKGXbtiDuZOscTe234B5mLaSNiyRGazWrGwNmrzg2q3iwSDWz3Y5ZAYmiL9YoEDOfB0rx7uo2S0YJFIHnJG0eEOM8-ak8brmBncM0qx8Wtu5rUaAYC4LWQDLxOoIXDiEV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eYg3mb3sWs-c_5PrhJ-nEBWYS6GusRwnMYEa1EIGmx_epXxkzRC75R9CMVgUpl9oPYoBl3EbjP1MJlMeff_phGyHVrJys--LxZhw87grGUEcBnj0FK-PiKO1TtQ1PHe-mJvzduE3HRPnmDcw2R3451iJtOUCv8s2JAvaamw8pce_0S9tWKXS8SpzlhH6DdXZOVw0jzBTFBvubHk7Co_5kz43WlphJsT9jnkqiTWMdVs-GASx3qZ1iEr049RGqv07iqWpkXXoYFIAYwiTf8nXS-h2Iw4_kX4brvnigCSwPginMP9jUiPsw9e1IPclHvSlh6x65L0b-ImVLf1I2zXFlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🗓
🔹
اعلام برنامه مسابقات سه هفته ابتدایی پریمیر لیگ ایران
⚪️
هفته‌اول لیگ‌برتر
🔵
استقلال - مس‌شهربابک جمعه ۲۳ مرداد
🔴
شمس‌آذر - پرسپولیس شنبه ۲۴ مرداد
⚪️
هفته‌دوم لیگ‌برتر
🔵
استقلال - نساجی سه‌شنبه ۲۷ مرداد
🔴
پرسپولیس - اس‌خوزستان چهارشنبه ۲۸ مرداد
⚪️
هفته‌سوم لیگ‌برتر
🔵
استقلال - سپاهان یکشنبه ۱ شهریور
🔴
پرسپولیس - تراکتور دوشنبه ۲ شهریور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102331" target="_blank">📅 13:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102330">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO9PWYFccHYtCoAMrnM_d2ypzPoCgCp_l74FBraPJDnb07UyCfOb8HUWGoIflfM4gKwCsayLIzdMN8y2-Y0G7J7bsXdESpVei1PQZ5CQ1Jt9gzDb_A6Z7P41u0kubrEIf0UKLULuIw1bk5Z_cyWosbbzXbRi80lbRb_WJRwmSxYWxnCehpNUd20LgKAVkAqBtCZGtryhIsBoQ9lMb1FssAf4z7apkFS7mn_7il0CypdIDN7DnSfh3eRY4yE3iGJHnt19lZwTuwnQLatqYYxwVqfjucivTCJlT9FfpVKxg4itxSQdsBZV2y1Hraod9PmsWs_XhqyZ6igmKiWui2cA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از کوپه: رئال‌مادرید و فولام بر سر انتقال گونزالو گارسیا به مبلغ ۷۰ میلیون یورو به توافق نهایی دست‌یافتند تا این بازیکن شاگرد آربلوآ شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102330" target="_blank">📅 13:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3-sdCSZgngQlCT5Wl1HkB7IzhGncZCkQ9n4Rh765RxkUfuDR19cXjoMCpWcNSPfq3dWjowb9xpA7ahd42snw4JAv2S46n05SWrpe0MawEW_OqoQlyVpYLUDRE0E2r4MbI7uiYMn3ZsBMLqspjJwaUZYqjUb0w-Vbw15hfoFLbxfSuiaCe0CdjtPq-FWqM78BKnOpoE8KS0hXTXmk4HXoYLfzIh_oEuHWbLJenACvESSMcJkLmO3X6i-TWCnMkfNKSdGzJS64kl6cWfU1WRscGEay_x9yJZqc05YHd2tULR0xsqRQRTLcB9wq6j-uY6xC54gb8HdUKKq25P1ILaRTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
✅
توییت مجتبی پوربخش مجری سابق صداوسیما علیه عادل فردوسی‌پور.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/102329" target="_blank">📅 13:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=JL7b0XNTIRkeF39u-KsDYhXE0SfeTw74HujZx2pTp6fkkzH7jmcAtObuLd2Ql8WPh9cU14yW2EDIGeQVQwhmiOSwDlp7WR5660AN-xa_i8p4rJu7OQ2nnSntTvGfWVua2yQW53RVUSk58DxTPtJLb-GZtNf29q5dyLbiRhuo_0B6WscjTclx-AbzT0irpXK5B5byhqJ1mRefS4M20SULy-vCfVnxF_0jpLTFScMPiYATl_5WEOwBOxtY_DcEwkFMHNsvixXnfvypMbchvvowEyNCPvkRbLGrZqQ9VddvMGI6O3DF3XXVUH-ta__QzXmubC-kaUoD48H45Lv-Bbc7eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee8b739e27.mp4?token=JL7b0XNTIRkeF39u-KsDYhXE0SfeTw74HujZx2pTp6fkkzH7jmcAtObuLd2Ql8WPh9cU14yW2EDIGeQVQwhmiOSwDlp7WR5660AN-xa_i8p4rJu7OQ2nnSntTvGfWVua2yQW53RVUSk58DxTPtJLb-GZtNf29q5dyLbiRhuo_0B6WscjTclx-AbzT0irpXK5B5byhqJ1mRefS4M20SULy-vCfVnxF_0jpLTFScMPiYATl_5WEOwBOxtY_DcEwkFMHNsvixXnfvypMbchvvowEyNCPvkRbLGrZqQ9VddvMGI6O3DF3XXVUH-ta__QzXmubC-kaUoD48H45Lv-Bbc7eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
روزی که مسی به برونو فرناندز درس فوتبال داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102328" target="_blank">📅 13:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEpHPO1UZpjHra1G0EJKVGBk18ehHMtCWKwkN1pq4dkq94SWYLkU6D-FYFj8EDqpzce2uYgoqvxr6wLs0KEeSo7HqS4qmUBdEZd4tSH_IIiqSyaf0Ewog_oxDBpqWaQkmfyhDmh_la23f7FKrQdEPWA3qncHnit2jetum9RMr6WohOsZfJsNML9APtE-2MAsZoKsKJedcdV1F3vS6aljKALFxc5czYx5I09t2A-6Zuciqw9zZylB4boa-VkF5Zk34WTL03VYxI-itcW32L9R5fpbN4A1junxdLHdsZ8ROSpqBaZqvPSJcXC9KIGDpxpCMji4dCPP_GpldaRqYOuVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🟢
صندوق سرمایه‌گذاری عربستان سعودی ضمن تقدیر از یاسیله پس از کسب دو عنوان قهرمانی متوالی در آسیا برای الاهلی، با جدایی این سرمربی به مقصد نیوکاسل موافقت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/102327" target="_blank">📅 12:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102326">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=vQ-d2slyKhZAZU77z7sZ1XnVdovEzlqj2u_z67gz1bjUYwha0p5XrlZ1mK7qiDg5UvlznMapS8157tBXztNf50rxsvG2oNp9nnF0H6eC9CWV1EXNBRs0uZ8CYg9RWbUEBVFQGsbgvYtYzCXQnsp5g1BB2hXetF9FnJyLco-MUsEYTiEt8BdzqpKK-nZDH_pWAmwuyburfcqqa3GYwKFBO7PrNKYVhyOdOr5JLZAkUeSfeQZE-avHmYFiW6RTTZf-VUeI524O0XmnZHY4rD5fZ1YlexruihorwpsoNeKP3lttVR3AJqGhaE-tqfi6Kp7vxAh5R5bkn8iLhoX8m6ciWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa8a1ce74f.mp4?token=vQ-d2slyKhZAZU77z7sZ1XnVdovEzlqj2u_z67gz1bjUYwha0p5XrlZ1mK7qiDg5UvlznMapS8157tBXztNf50rxsvG2oNp9nnF0H6eC9CWV1EXNBRs0uZ8CYg9RWbUEBVFQGsbgvYtYzCXQnsp5g1BB2hXetF9FnJyLco-MUsEYTiEt8BdzqpKK-nZDH_pWAmwuyburfcqqa3GYwKFBO7PrNKYVhyOdOr5JLZAkUeSfeQZE-avHmYFiW6RTTZf-VUeI524O0XmnZHY4rD5fZ1YlexruihorwpsoNeKP3lttVR3AJqGhaE-tqfi6Kp7vxAh5R5bkn8iLhoX8m6ciWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🙂
یه فلش بک بزنیم به زمانیکه داور زن بازی رو متوقف کرد تا به کاکا کارت زرد بده و باهاش سلفی بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102326" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102325">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_BLlwZHgqmxGDGI_XuZ5QqxwImrJ1LyFUH-2yMDBkkUmNSLHmiavt_J9JvtFYeoJY6aps65-AK1pH_41X7QQ9WxZ-CqmBr4ErjyfGSpco9g4FcJZp6zk8hT4UbFL1066uTG9omVXdbpiae-UlElv_tsA7J-B9RJP_Tk5HSVwq7ZVZJ2kZ_2Z7DbworOvAk4Gl-faAM2LetPbMY4NljQxjqL30n9o83KMiuEC8gMPjhEvoOk29O4XIWulr9yXW0uWkVGRbAVZ1CLLB6DrSDaTmAz50m6WFNbJ5J4bOINnsPdDIuNh_t-7Pvg1H9FacBFCCpdZIuCB6KjDdtXN4ySLXkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49420aa7fc.mp4?token=fE1ShMo9XrrBD6aDT0jDLCEK0jGwJ4VPJ3FsESDv5CuLClJPIxHsODtkqo9Uu5FdV_hc8HtAkl3EpVbJ2v-323oLyuqwimZqa1wlLXEydV7rhAlI1I9aLYlXs1eKZJdd5LoDwdqI87oScNGLwrimK4CudeeS6pWL7w3OaShAF79fphEEo7p-GI40WDOfqF8ioXSMoHqZbhOo5BY8YpEFNBT3H0h_7o5EkCqV5RRysK_ZSyc1v3B6Nfbv28O2nLXcMu5vYsu5thOl5VGfzeBiHiza3IVSoFPp9npbBQu42Js6kWcmsefGgCBmJuCItgp7MMUJIVIh5Ba-3KvFeIOb_BLlwZHgqmxGDGI_XuZ5QqxwImrJ1LyFUH-2yMDBkkUmNSLHmiavt_J9JvtFYeoJY6aps65-AK1pH_41X7QQ9WxZ-CqmBr4ErjyfGSpco9g4FcJZp6zk8hT4UbFL1066uTG9omVXdbpiae-UlElv_tsA7J-B9RJP_Tk5HSVwq7ZVZJ2kZ_2Z7DbworOvAk4Gl-faAM2LetPbMY4NljQxjqL30n9o83KMiuEC8gMPjhEvoOk29O4XIWulr9yXW0uWkVGRbAVZ1CLLB6DrSDaTmAz50m6WFNbJ5J4bOINnsPdDIuNh_t-7Pvg1H9FacBFCCpdZIuCB6KjDdtXN4ySLXkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در هرجای دنیا همواره فوتبال آبستن حوادث است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/102325" target="_blank">📅 12:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102324">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnIOu9qpaAYgWJ_M_4M7t8fTwhQGYafV6RG_VgFwV9fP45_GvPlxra0beqtkigR9zVTPmshce3WBJ6JhgAcXxEOqb69xU6phhdiztBbv7f4kRgjcKr16UQEwN86nuzTW0_mC6gpJ-HR-gp5sGqc9Q1gBzlx9D4snfFL-bHmZaZr1weq57cf_DIn2EttiJi5tfaDNg86leSxkvH7sBVQ2BswL1wCRIecJA5tfO6Fb0S5Zc1xdIg0R5kmH8d_W-RX7uuqs1QVl9U_FjiDej7YZt4nt5nTnRqKdY4u0TutdRjr9xLWdLz3Vgefrwg4OlY7uWzKLLU_rnyL7E4h2MC0suw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102324" target="_blank">📅 12:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102323">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=sG9NeI729GyAInHKmUTRVXg3t9bH4HnOvFnu6V2qmMq_dtk23TjS2gIJCvvA2at7Q_yYgri5bg1gAfb1Dw9lUywks5XowF46qmzUmxlR6ieXuWjXgqkYBgQkSBLKEh2btzFJI1VT6Nxmy1HPkqRN4BWPkbWhr8lPSNaB6qm3fKTbuFb3x0ECIzc8Tu0kT4dgxOdvQ6fOSQBAAVsy84UyTW5e3Eh6yJq6sNaiMnB9wb5z1YQFwyVCo2m1-5oT1xl-SzTTTjCvvAUl89HZ0NWvWqKPaj97esd6z5Qf1SzZujLAItM0cvISjyBCOhEarvdTqrq_AtC6p5F6SLJ35I2R1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9305c345ee.mp4?token=sG9NeI729GyAInHKmUTRVXg3t9bH4HnOvFnu6V2qmMq_dtk23TjS2gIJCvvA2at7Q_yYgri5bg1gAfb1Dw9lUywks5XowF46qmzUmxlR6ieXuWjXgqkYBgQkSBLKEh2btzFJI1VT6Nxmy1HPkqRN4BWPkbWhr8lPSNaB6qm3fKTbuFb3x0ECIzc8Tu0kT4dgxOdvQ6fOSQBAAVsy84UyTW5e3Eh6yJq6sNaiMnB9wb5z1YQFwyVCo2m1-5oT1xl-SzTTTjCvvAUl89HZ0NWvWqKPaj97esd6z5Qf1SzZujLAItM0cvISjyBCOhEarvdTqrq_AtC6p5F6SLJ35I2R1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇧🇷
فالکائو برزیلی بهترین فوتسالیست تاریخ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/102323" target="_blank">📅 12:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102322">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=LEVonnbMacgCkoQ3rD3RI0X8eoOMyyiTscejx7B65OiPsmm9fFeMe7FAp9kQ--i9xuU9JqTtHzBouGdweXo5TCkip2Xsc5xWW73QW4-_6U4TfhS2452jf_fwZrXhzgaf4qkajWyLR2tOTx9GM61jh2z8JIsIRh48zBCDEh0OKystMqmIKdgQUn6oKf_xXOAbmMGmXOkNpS2RtEflfP0s80Vdpqk5T_ejIDvdq_8pMtVfrdR8nCjbeYoH7Jnor68lP3516uENGGemIzr9Gv6Jg9RSlDxhu5qIRq2XjcdBX2OdeJia7DsqogBgWAIm3gOvDP8NVlqGpD7Xykks_qpw-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc1c528fcb.mp4?token=LEVonnbMacgCkoQ3rD3RI0X8eoOMyyiTscejx7B65OiPsmm9fFeMe7FAp9kQ--i9xuU9JqTtHzBouGdweXo5TCkip2Xsc5xWW73QW4-_6U4TfhS2452jf_fwZrXhzgaf4qkajWyLR2tOTx9GM61jh2z8JIsIRh48zBCDEh0OKystMqmIKdgQUn6oKf_xXOAbmMGmXOkNpS2RtEflfP0s80Vdpqk5T_ejIDvdq_8pMtVfrdR8nCjbeYoH7Jnor68lP3516uENGGemIzr9Gv6Jg9RSlDxhu5qIRq2XjcdBX2OdeJia7DsqogBgWAIm3gOvDP8NVlqGpD7Xykks_qpw-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
❌
الکساندر پاتو؛ ستاره‌ای که قدر خودشو ندونست و خیلی زود از فوتبال محو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102322" target="_blank">📅 11:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102321">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CiI0clwA5FdYHAQ9xEBE5xadKzDt035mzPMDvfRTiyspwQDBdiG5pqAisvQUrxzD21iabu5u-lIX4zjyoV0BHMF285YKb6hMTO_M2WhkP1lYOdsb086RK-UwUAQ9E9TjedEYnU8jGDnO_XXjZxu9EDlKmSIn7KaePU6eWma6nMNlb-O8Sh5B-bwG6c7N3JTx5VSob80vQvtMd_5c7j_Bx6jIvUWZW8CwI0V5iLCCiFWJYyCqMApnrPcAdP_KUV5ZM7iCWAKYZ_wWGuzZ5HxQX5d4OFdbONLCGXic2neDQsjVzAz3rokMHUvWQPsCaBUkHWWmEENNOcXdG8WzPYto9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
⚽️
رونمایی از کیت اصلی النصر برای فصل بعد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/102321" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102320">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
🔹
بازیکنان خارجی ، 4 مدعی لیگ برتر
:
🔵
استقلال:
🔵
آشورماتوف، ماشاریپوف، آسانی
🔴
تراکتور:
🟠
خامروبکوف، هلیلوویچ، ایگور پوستونسکی، اشترکالی
🟡
سپاهان:
🟡
ریکاردو آلوز
🔴
پرسپولیس:
🔴
دنیل گرا، اوستون اورونوف، مارکو باکیچ، ایگور سرگیف، تیوی بیفوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102320" target="_blank">📅 11:26 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102319">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-q_ytkM53PA5TfhlexmTLL6yPk81JCieTebAyqIrx4BtcHVB_-qf2FTLoRA1NivVN8TF0X7zYLSx7H56PQe66_0wDRSI1XyyeekqINerTDn0H9sGpYpibK_Btd7uUlBDipaFGsj70jO7da5DlQxHx6ESf2Xa48HepvuCSOT22AztvAQZyTc_f13fGB4zXyElCkolHo3dXZyMOin6ZqoZqTYWAPkjljHf3V5UuNOnIuGaooF_ckkyQ88bRq8288ab-EcpsL8copr-oQEhu0MZ8Fmq5JdUiVTwiOrQWKDUEBfjRjYgc5aIxhWMdKl5_EueAMK57dVSmYDhjmzrxn4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ماتیاس‌یاسیله سرمربی الاهلی عربستان در آستانه هدایت نیوکاسل قرار دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102319" target="_blank">📅 11:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102318">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=KVXIeFXbMtLAAYzxXcWv5fogeZiaGIbdTg28JdYpi_Wphwgr3idSpCf2IG-kX1xIBey5n00jqJxpVo8xDTgWbDKGr1eFr0lMOz_1cTk6EWcAq2RNwOlYlSKnK8MdyISMyiv6_mYwhAU71hrCUnWflLArPsh8CjsxHk3bb3ZZJlVnPENOOVCy1BFN3v9lYXAl4XGomRWfWqDkxwSqcjEugTkFU4qJbKjMkzCpxaKL0jfiFoVRaCjavlebyjevDoshvuEGnBsGJ9-cedXJ_7HrBt0W7G-HQQ2-iE2iXC6Z_O0WKFx9wYpdW-qO3OkPCfO4KpSuY0FEexN-0w0RNLjyFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b07d2f0b1a.mp4?token=KVXIeFXbMtLAAYzxXcWv5fogeZiaGIbdTg28JdYpi_Wphwgr3idSpCf2IG-kX1xIBey5n00jqJxpVo8xDTgWbDKGr1eFr0lMOz_1cTk6EWcAq2RNwOlYlSKnK8MdyISMyiv6_mYwhAU71hrCUnWflLArPsh8CjsxHk3bb3ZZJlVnPENOOVCy1BFN3v9lYXAl4XGomRWfWqDkxwSqcjEugTkFU4qJbKjMkzCpxaKL0jfiFoVRaCjavlebyjevDoshvuEGnBsGJ9-cedXJ_7HrBt0W7G-HQQ2-iE2iXC6Z_O0WKFx9wYpdW-qO3OkPCfO4KpSuY0FEexN-0w0RNLjyFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
با اعلام خبرگزاری رکنا، نوید زیادخان قره‌داغی همون حیوون کثیفی که دخترارو تو خونش کتک می‌زد و لایو می‌ذاشت، بازداشت شده
⚠️
‌‌ ‌ ‌
یه ویدیوی وحشتناک ۱۰ دقیقه‌ای از
این حرومزاده منتشر شده
🔗
🔞
مشاهده ویدیوی کامل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102318" target="_blank">📅 11:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102317">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
‼️
🗞
🇪🇸
رومانو: رئال‌مادرید و لایپزیگ بر سر انتقال دیومانده به توافق نهایی رسیدن اما دلیل اعلام نشدن خبر اینه که لایپزیگ ابتدا باید بازیکن جایگزین جذب کنه و سپس خبر رسمی اعلام میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/102317" target="_blank">📅 11:08 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102316">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=KTY7G4za1txlT1JlGXdKizePf0FUnp5QJmAYzZAFGFJoJC4zR-O-gxdICUAGJTu_cb8lOPBowrsNbN4z3mnwLSIC5d0HYgjd_TpvSN7yiN9dH50vOo3JCsDAqIYCoTOzq4XRr62XftqPtXq2Ggs4faKZyhkVm-yTZe95j8pjQ2JfXRz0IGJl83e-DJf9I56qxXJl6V0WtFIgAOvusWkgY_ub4ldaKzT4bEzK-l4mbl4tSjfwZUSja3gUDyLBJk0JG-3tlo4Sp0F62tecF3dM0OGQLkAFMrhIcIWJSkNqY_5OhZXNXlrNO0drMmk_g-ESO_K6ckVZmDKy3xHV38rUjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a432ebcf02.mp4?token=KTY7G4za1txlT1JlGXdKizePf0FUnp5QJmAYzZAFGFJoJC4zR-O-gxdICUAGJTu_cb8lOPBowrsNbN4z3mnwLSIC5d0HYgjd_TpvSN7yiN9dH50vOo3JCsDAqIYCoTOzq4XRr62XftqPtXq2Ggs4faKZyhkVm-yTZe95j8pjQ2JfXRz0IGJl83e-DJf9I56qxXJl6V0WtFIgAOvusWkgY_ub4ldaKzT4bEzK-l4mbl4tSjfwZUSja3gUDyLBJk0JG-3tlo4Sp0F62tecF3dM0OGQLkAFMrhIcIWJSkNqY_5OhZXNXlrNO0drMmk_g-ESO_K6ckVZmDKy3xHV38rUjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
از دعا کردن تا بزرگ کردن لامین؛ چند کلمه درباره یامال از زبون مادربزرگش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102316" target="_blank">📅 11:04 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102315">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgO-rKO0qrEIYeQ5G9_D1gDfULhrDr09cQ2LYgyzqheOcvZuqqSGDCv0qu8G2KCJdK9ZothvA7I4Or0Y9WYpUO6H2VCBK7bSVmzqvFbHN601tNikY2ld4P0Q-veoTl_XKB9gxib4kObFU1SouZr7jMlei1y3YXhMYOSCD4eRwuGs5w3f4vyki5aasRsMDiwcycHsE2PefmRxM6zZgN1k_NOTACaZ0xpiDF3KP3UZKC1q_rKiQv8Du_Wa1JmgvtQ6yfhJnHMpKxUU2L4N_X4u1tM06rTQByZ-xRjQlED-LuxWajZI39SS_PLPP9MnZb6FNXjU-AlQMWHcmxu4HJTVNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
🔵
با اعلام رسمی AFC، مراحل حذفی سه فصل‌آینده لیگ‌نخبگان آسیا به صورت متمرکز در کشور عربستان‌سعودی برگزار میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/102315" target="_blank">📅 10:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102313">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOy0sXfXgrninxukLVPRKa8J6HR_sPjGwlAnoWT0QWNsn2cO81k8NuwpP3e5_O6-IDk6cxjrGkqyZrSbiieSZxgtVTCNOuNtvup8A6Uhg51rG-LlX6xVLKWbBpJADK160hHfOeRTrDcTrN59-EkkO-wCP7mRv4_kO3KRoFYiahHSk1fKPvQWAvZ_OoXaliFbdkout7ar7Ont5fXq27J8UcKyI3Vqpvz9tXU0RYsmMxuZ4Zj9nhng5OqYg4YgbrMyHYcNsCX7ykeqpJF2aQGiBSu8MRbiT3_xteH0CBX9fvNpUQ4Ckt-uj6hNG_QX9URd_mSCzZGZdYP26szWNBNsPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایوب‌بوعدی ستاره جوان و مراکشی باشگاه لیل در آستانه عقد قرارداد با منچسترسیتی قرار داره و بزودی جانشین رودری میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/102313" target="_blank">📅 10:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102312">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fac4341594.mp4?token=Ono8zM9Kj2gYE-hP8PzPH1CMfgVySY2Uy7kI-EuZqqG9sITAbmAxxpDLyc9bmeaPKEozT8ruX-6D5BjmO4ytlL-hzohYUWY9TiLIFVA3ttJEYl0jvK4VxVC2lRuQ_ocIu-RggBL4Xttg2z31iZ9coQmB3aCCD8iNIYx2WduhYAQsApE68UaVDhF6mdbr8WKXC1aM8TRtTDZf-MV4X39YeoIamwgjRlvlhTSO-J3Svxd1E8twOT1a0cbw-7I9Q0vuJxOtoxGR8WVmQKMjEyVgyvPHzjKwVecJX5ZjO0KtnIHdQT-UksGeeoq8G9U8kgRcUadkbF1JZI60D2UJgCF9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fac4341594.mp4?token=Ono8zM9Kj2gYE-hP8PzPH1CMfgVySY2Uy7kI-EuZqqG9sITAbmAxxpDLyc9bmeaPKEozT8ruX-6D5BjmO4ytlL-hzohYUWY9TiLIFVA3ttJEYl0jvK4VxVC2lRuQ_ocIu-RggBL4Xttg2z31iZ9coQmB3aCCD8iNIYx2WduhYAQsApE68UaVDhF6mdbr8WKXC1aM8TRtTDZf-MV4X39YeoIamwgjRlvlhTSO-J3Svxd1E8twOT1a0cbw-7I9Q0vuJxOtoxGR8WVmQKMjEyVgyvPHzjKwVecJX5ZjO0KtnIHdQT-UksGeeoq8G9U8kgRcUadkbF1JZI60D2UJgCF9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Auraboat kids
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102312" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102311">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1GNR_kGlNmxrXVjiqvHzDut98Ksd0f7iOAaTpydhpDspxl_YoGolDi0i5ZqxJ2g2aNs61hbI_5sT6usyu2I-Vv5b0umQr-EOuBGY7Ybr_hhK7PrGvywZ75Tw-maALsnpcjt2FSSMP_RF6uuR-IC9TQAJXOH554TKqGKgyfQtlujoJkGZF1AVeOtZAeL-j3is0pesojB1lCDf6-P2TapwdQ9Y6wx4X9En7DOaEWlvZA4UcIo6iCrkmUmGtz32KNG656Dw1SkC7rJKXeT-IadtsNdhy1h9jwqj2ePhOJql1iqVB1jt4pY9gRsvX8kHaNS2u6Pq5VfQoBrSg4u9sVe5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
تمام‌نیازمندی پسران فوتبالی سرزمینم :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/102311" target="_blank">📅 10:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102310">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0DDZs6QqmXHlGBCoBpW5stbnYc8Wky96qqxpUwVRGrVzdkZM7QPjsDAjokYZEAMmuEVfarD7xJ8291h2qIYp3VIrglN_Bq2vsySYyRhxIJpXmbRoQGTjZ1FJ-1ictjd_CdUywqMdrDGB-QhGToSx1DZlNP1hHt0smmtGwc1eGvv0E69l-9AB1G01U5PQqA7gpNO_xAdq1SsKBifFhi4DATohVHW3IJiBSsVnTN3oYgiopT6DBNGDCcHPpIU5IzWArLbBHiWEn8TNZYzdAkg3rfMmmnj3DJDYyQu2-QgXfI50N4U2kb0bBhdXLTF7XaWOliebH12XN3sUOpsE41Bug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🔵
فابریزیو رومانو:
پاریسن ژرمن و موناکو برای انتقال مگنس آکلیوش پیشرفت زیادی داشتن و معامله در قسنت نهایی خودش قرار داره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/102310" target="_blank">📅 09:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102309">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cAwRNvgY-HwbQCUeLShLKnkGv7mjwWd91Z80O8-XrHdfXvIJRepzjg_liSgu8WDpvt3U7VEN_zQac6TPD1fOFjO6bLlszp10J6xiqexb0-zGbaN4p-qWTFG-DGwsV4BEIebp8KQyfsuL2UTvTjz0wA93Nkvc1rHWfJh4n6XajYyIIOyRoQ0CwP8GK8g2eoFVuXGJwmp_SnjfrsvAfxSOySg9vHWSHRHtBMbDC2r_YV1YScNPD6tBDzwF4Oh1RCUbw5EUEtpR0nbkusNMtG3HEXi_uJXjgjGL98hfHdsCTwkd6N8kPndqe6fvyLADw_ZgsVGkJpra1tnk2pCDvvrJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
بلینگهام برا زیدش تو تعطیلات عجب پایی میخوره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102309" target="_blank">📅 09:20 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
