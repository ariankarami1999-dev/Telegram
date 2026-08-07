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
<img src="https://cdn1.telesco.pe/file/vU5VBi6Vxc0TJD6VpfaLGizVzQ6QRoq4HkawTMzQqhez5dwrQT4-1jgU_A2g07qP8WmaVsHdCxeexd-vJnazvnVP9kooGvABSpah4BpkTcEKDd0MEJqtcfHtOSX75DezlCe04eEphTOGrW0vlFXB0rW3PgrL2aWQAtPxnGXT_GqlA9ksgvS2Sos_Xf0rVSHlkwp5j8Jh4Ev2RK3jN2tmfWtOdSCUCMWnE1IGH9jwTIlLFicIQcz-qpQZl-_CQ0KyrWBQTsYkf2oT_3wxXLdnZ0lWU1lmXJqU2gVKJ6j5xQWwyQ--vzoQan4GzSx6ywbuKCjkCQOW9sVUEWb7Ipc0vQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 156K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 19:14:45</div>
<hr>

<div class="tg-post" id="msg-4868">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hptbY3WMTwko-RphibHpS90t03iAx8WxRGKjiA9a7IvBudULp_wbGYwacfFYh8pCV7OHzgn09ZlI3tPjdEnlbmKjyRCQtaKCjNWA7qaW4EP0HUqH7iZSWWTd6nSfOZDUxEhrK8dgZ3JY0xwprhWP2zHjdxYViQ46gPwcgF7_AfOj1d2ueKxhx2DkdR1x4get1WxoX77jeM1UG__gALWXpcqa9TB1T9r2F4pbWjNZSZW43WjriDIpAQevJ_kEHPRXWkspBKAdRQaY-i0NPpRxJL_UqRc1nMAY-QOXBhnHYFRPToTtslYHO8AELve8Rrj2yo3rZjnjoGLloPOLGaDqcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین اپلیکیشنی که برای نوشتن چیز میزایی که توی ذهنم میان استفاده کردم، TickTick هست. ساده، راحت، بین گوشی و سیستم هم سینک میشه می‌تونید توی گوشی به عنوان ویجت هم اد کنید. خیلی هم سبکه در عین مدرن بودن و چشم‌نواز بودن طراحیش، هیچ چیز غیرضروری‌ای نداره. پلن رایگانش هم از کافی، یه چیزی اونور تره</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/MatinSenPaii/4868" target="_blank">📅 14:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4867">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مارک زاکرچیزبرگر هم muse coder داده که تستش میکنم. سرگیجه گرفتیم از بس بین ایجنتا چرخیدیم.
اما جدی مدل‌هاش قیمتشون عالیه اگه بنچمارکا درست باشن</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/MatinSenPaii/4867" target="_blank">📅 05:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4866">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/MatinSenPaii/4866" target="_blank">📅 05:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4865">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=b0y_PlyINNO48-OwcCZ7EqvlskMV7lAhPqL0gE1K0nXPLsz2p0wfEI1WNWOITwpehj5sos5ZL39xyTpymSItf0hUR29s9uQmvWR5rphB7wXkZqW851cdeIlwSEKLoUPFQDzZONPxsZVoBjQ5Hb60xOwxUMvNcmhFfLMYlFDb7yeQWUoYqxqhJ2pZkHZqY4hK6sXR5INqsX6RvAWAMLyX9ipdGi9EtK_pHc-LJ11_EQosnb8J9QdKRHruHA3lmgggEJY6KEmT6UH3zNmmwJ_9jtyS5_gkhD7_o7c3Jd9pPfmoJV2ocSvJlNkfHVm_cwL_LL6RhSpiOj6ExKydPO2ySg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59cf6c69cd.mp4?token=b0y_PlyINNO48-OwcCZ7EqvlskMV7lAhPqL0gE1K0nXPLsz2p0wfEI1WNWOITwpehj5sos5ZL39xyTpymSItf0hUR29s9uQmvWR5rphB7wXkZqW851cdeIlwSEKLoUPFQDzZONPxsZVoBjQ5Hb60xOwxUMvNcmhFfLMYlFDb7yeQWUoYqxqhJ2pZkHZqY4hK6sXR5INqsX6RvAWAMLyX9ipdGi9EtK_pHc-LJ11_EQosnb8J9QdKRHruHA3lmgggEJY6KEmT6UH3zNmmwJ_9jtyS5_gkhD7_o7c3Jd9pPfmoJV2ocSvJlNkfHVm_cwL_LL6RhSpiOj6ExKydPO2ySg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏯️
آموزش فیلترشکن رایگان و امن با استفاده از متد های MITM و Serverless
مشاهده در یوتیوب
https://youtu.be/VYfQePhgEUU</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/MatinSenPaii/4865" target="_blank">📅 01:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4864">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یکی از دوستام برای رفع لیمیت اوپن کد روی 9Router، حذف و نصبش می‌کنه و درست می‌شه.
به زودی واسش یه اسکریپت می‌نویسیم که این مشکل حل بشه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4864" target="_blank">📅 19:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4863">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=pcXUFRynPOtJGZjJPUJNkoIxwEpDvngwQKTgXGlT2jpNZmXIyR-LOfKyVcpWWBQ_u7wecLk4dxTqWngdrAZQt1KgOCLxqken2PrlihfCd1Qykk_MR1sfGjUEq0M1NIhuQpZ6lfmgP-yzl13okvXaUP-quJyaWZF7aDWIkM5LgJdzIauyyUg8qiruyPK0nBhOsMBRee3qxRMO8t7uAZ-aoMAf4G5e9Oq_KmgSWhuTGelV3jpGnbRgAOO3Xt-k5jbqkUp281CldgsBIWm7rxVqe6KHvbvtF63eY9W-OMTttGWhNpevuyxv7FQOgPm4svPeWgbCNAl0zHdZ40qT5R5CRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f4ff82cb28.webm?token=pcXUFRynPOtJGZjJPUJNkoIxwEpDvngwQKTgXGlT2jpNZmXIyR-LOfKyVcpWWBQ_u7wecLk4dxTqWngdrAZQt1KgOCLxqken2PrlihfCd1Qykk_MR1sfGjUEq0M1NIhuQpZ6lfmgP-yzl13okvXaUP-quJyaWZF7aDWIkM5LgJdzIauyyUg8qiruyPK0nBhOsMBRee3qxRMO8t7uAZ-aoMAf4G5e9Oq_KmgSWhuTGelV3jpGnbRgAOO3Xt-k5jbqkUp281CldgsBIWm7rxVqe6KHvbvtF63eY9W-OMTttGWhNpevuyxv7FQOgPm4svPeWgbCNAl0zHdZ40qT5R5CRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4863" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4862">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rcDGEYjPKY2L9Y3Zxt_97VfQn9isE7GZR6lISJhRoOv55heRWohdiRpczWBmBh0d7xXap1vE3XXGXsM9XUV4-0oxtbbIBxWN6Eivy_RuSCDgPRVuX1Fx-pxJTtesv46a2brSwgFRIWoEV7EZP4tqn03pi92OQRNtIet4nxym8rs1-SSXTCTZR7kPLki1wOBdkrlcqzDxCjOjfCbdXLqKwqgPoNEm6vk-I0FYxK_7DxWlhok4Ful5IM5D8e8XCtsGN47My3RXcgA7wRs_ICwtBAxFe0gm_-EGRGwTfb7_bucePgrS2CS4z2SUyrAIonAlC_3pu9sgIhZ60phwO94RUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلودفلر یه جوری ما رو دعوت کرده به سان فرانسیسکو، انگار حالا ما میریم
😏
😏</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4862" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4861">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">Matin SenPai
pinned «
خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید: https://t.me/Editor_MatinSenPai شرایط کامل توضیح داده شده
❤️
»</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4861" target="_blank">📅 21:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4860">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگر وسط آپدیت کرش کرد، یک بار دیگه باید re-deploy کنید</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/4860" target="_blank">📅 19:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4859">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4859" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4858">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">«بعدش هم روشن شو»</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/MatinSenPaii/4858" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4856">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/nFoH28lsucjHG_91YlrMYjIi6AZC8gUypxKxhyVHrZu0QTvSz77FmVBBdHHlHMVcRmpIfIvbMT5yzjdJrA1Oh2DIBm5zKz4cd4N57QfzMsvvPjuzMrf00MthYeXJNPRgNdcFyp5fHwi9YKaqdO3rgkMkbMUY544jXGtjy2Xn3VttyAvP0CwmaUxwYfm2cYEgKLsHTBisjuz0YXbysfAmXcH1sJN3ro_ZOiLqx-1YLD3Lsqf-493S57kX-vAg1IAIZoZqZYrPgvlmPuunulcBQuV6btm5bWsePpt1pJcP7nNfH5trHEQq8p9zZtsy02DTEwrmUwbGfzlHKBnV0S1qXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sTs5eKJHKWCJWUD8SHA9892UWnSVgrvTgPaileiM24WE-Pp9bANbz7a4_bRfyZI-G8y7yS1HMmSXfwxdPhCF465kZs5H-1kQqrZFAMBB0UhqNu-OnkDIc_np8xFRmlQPRZImB1-lMcHFTJXw8eKCdn4hKqvhB-Md57mw5n7vMBW2bwoSvxw1BjyfR-bOyaWAXaC92nDYWrG0sHu_7PB6OHZ7dK7rLzZp9qWBzDBJ-0Mbm27qx99BQNwI86mtt9l8q8XLdperyAzWBNYQi9hqmlMu96AGck01ZGVnOLTGKHsxIgln_ASqluPSVeiS_eYhJvCa4Bcn5e_FJU6l317Vdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">متین الان که هرمس اپدیت داده
چطوری ربات تلگرامیشو اپدیت کنیم رو railway؟</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4856" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4855">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hunc0nu6TF3jaosSdvqL5SqfUq8t2R2IYDCoKNaHc6x0xxUzTTer10UV-ovbYneZB_XhGfMU53a7U3AIBqwIX7KDoJ-R7eixDH-OQ2jhn9zWBgiYZNHuqO_iSadG7aI3xsa-vuT6yC-rj4-J7vYj9FaBk3-OeJbjscHrWZqNYiiYCTSgAyM_3h_qPL_scyyKj0yQbjhPrtws-WGZVP5lJsCCFtcLJxicjA87hYMzZ1PsNiUejQKQapDcWQh6snjgWuA7azr3uBSqgfANMgcKihUjcdIxILllHlt_QjaPYE1sSInoLW6sJ8faRq9_LS74PPSUY3V6xEFh4tYpK0OC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت بزرگ Hermes، ایجنتِ دوست‌داشتنی ما، نسخه v0.20.0 منتشر شد!
📊
این نسخه که بهش "The Herald Release" می‌گن، کلی قابلیت باحال مثل ارتباط صوتی زنده، سرچ با منبع معتبر، وب‌هووک، اتصال ایجنت به ایجنت و بهبودهای شدید پرفورمنسی داره
🩰
تغییرات و ویژگی‌های اصلی این آپدیت:
1- گفتگوی صوتی زنده (Talk to Hermes): پشتیبانی از استریم صوتی زنده با قابلیت قطع کردن حرف ایجنت (Interruption) و کلیدواژه‌ای که باهاش بیدار میشه (Wake-phrase).
🎙
2- منابع و استنادات دقیق (Cited sources): توی کارهای پژوهشی تمام ادعاها رو با منابع واقعی و مستندات و سیستم راستی‌آزمایی (Fact-check) لینک می‌کنه.
📚
3- وب‌هووک‌های خروجی (Outbound webhooks): فرستادن اطلاعات و رویدادهای چرخه‌ی حیات ایجنت به HTTP Endpoint‌های خودتون به صورت امضا شده و امن.
🔗
4- ارتباط ایجنت به ایجنت (Agent to agent): پشتیبانی از پلاگین R2A v1.0 برای شناسایی و واگذاری کارها بین ایجنت‌های مختلف.
🤖
5- سرعت به‌شدت بالاتر (Faster everywhere): سرعت لود اولین توکن (First-token) تا ۸۰٪ کاهش پیدا کرده و پرفورمنس اپ دسکتاپ به ۶۰ فریم رسیده.
⚡️
6- پلتفرم دسکتاپ: قابلیت پیش‌نمایش زنده آرتیفکت‌ها، کیت توسعه پلاگین (Plugin SDK) به همراه تسک‌بورد Kanban و پنجره دسترسی سریع به دسکتاپ اضافه شدن.
💻
7- تاییدهای هوشمند (Smart approvals): پیشنهاد تایید دستورات ترمینال بر اساس تاریخچه استفاده و قطع‌کننده هوشمند برای لوپ‌های ریجکت شدن متوالی.
🛡
8- قدرت‌نمایی در CLI: اضافه شدن ابزارهای اسکن پروژه، مهاجرت ساده و اجرای مستقیم کدهای شل.
🛠
9- هدایت بهتر ایجنت وسط اجرای کار: قابلیت اصلاح مسیر و دادن دستور به ایجنت وسط کار بدون اینکه پیشرفت قبلیش خراب بشه. نسخه‌ی قدرتمندتر Steer که داشتیمش
🧭
10- ابزارهای خودترمیم: توانایی خواندن خروجی‌های نصفه‌کاره ترمینال، تشخیص خودکار خطاها و بالا رفتن محدودیت تعداد تلاش‌ها.
🧹
11- اتصالات جدید: هماهنگی کامل با پلتفرم‌ها و مدل‌های خفن جدید مثل Buzz, GPT-5.6, Claude Opus 5, Gemini 3.1 Pro, Grok-4.5 و  Vercel AI Gateway و رفع باگ‌هایی که داشتن
12- قابلیت‌های جانبی: پسورد Vault داخلی، فشرده‌سازی خودکار سشن‌ها، لوکال عربی، فایروال و مقاوم‌سازی امنیتی روی ویندوز اضافه شدن
🌐
این دستور رو توی ترمینال بزنید، آپدیت میشه:
hermes update
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4855" target="_blank">📅 18:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4854">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کانفیگای کلودفلر من هر 5-6 دقیقه، 1 دقیقه قطع می‌شن نمی‌دونم چرا</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4854" target="_blank">📅 17:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4853">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">راستی این ویس با میکروفون گوشی ضبط شده و با هوش مصنوعی رایگان Enhance شده و به زودی AI اش رو بهتون معرفی می‌کنم
🥰
https://t.me/Editor_MatinSenPai/3</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4853" target="_blank">📅 16:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4852">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خب دوستان من، اگر ادیتور ویدئو هستید یا ادیتوری میشناسید، خوشحال میشم براش بفرستید:
https://t.me/Editor_MatinSenPai
شرایط کامل توضیح داده شده
❤️</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4852" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4851">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VYzZep6FD3z9Ulad2gTWhHSe3q8dpyTKoiDFyiYILx2U-4kvoCszj7ZL9K2A3sGiGUJbapFu2aovqXFQ0z_B2JajWaijCqgC9K9eise4I_zDur-wVe5GRrCuzIPnf4cz8Axf61g_Bzh0Ttdn1BfXZteunTfaxpAuSuA6EUXyd8HpD-qo547Tn_XoSaXRw4uA7Mk2KTpCEw2P-IEBsOgxlKVqVYuRVmX4guVCCe9pTqWNw-Geq3mSHm4R-Zb9cHyw8gQJSiwsQBmkPr5Ylkl5Ibo4Ynurjib8J4uuM6s5-Fmk-uvNKcjKuaqF0AXBlVKy_8xFbu6uTEr9tkkCa37BxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این اپ INCY که امیرپارسا بهم معرفی کرد خیلی خوبه
دم برادران روس گرم</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/MatinSenPaii/4851" target="_blank">📅 16:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4850">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست  https://t.me/RasadAIOfficial و برای خودم هم جالبه کلا به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4850" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4849">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">این چنل به شدت به روز و خفن، تمام اخبارش با AI درست میشه. اوپن سورس هم هست
https://t.me/RasadAIOfficial
و برای خودم هم جالبه کلا
به شدت هم پستا تر و تمیزه با فرمت‌بندی جدید تلگرام</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/4849" target="_blank">📅 16:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4846">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NRo4uVTasQC-4c8W_wwrbwyfBzq5-djnyVn3imx0-d0Msmxoxs8SORnqJvEZ6nN8wQmIgLl9u1cVO0z5nW3aPG-Ge6GFBUnZZPvFkx7kEpjUEtkLrgQCGmjeWzfaEn3JH9O-ix3HGEi253vgZY29r-IQnUCrOT-ucFYMAaosofM7F01mLb7HFlJteGIuSeEX3bsEwVBuCf1ub2M-eDCbO1-z0rZG9b49cMyiq0mZ0Js-kO0Pb4RFpGAFPsJQyT3r3eRCtQoCjIsm0b2NGZunAdIDWkro4ke3O5BkupZReS7mmH4UdnXyqbXiDtGJuWRngxh13km-wVLs9tpLgnGk4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r5RS6NWtl0w2k0zALBtrcdTsY8fHw5_-Jg-d6-MQN11gwizzhstLI-RShIUtbkZtwaa8UDOjMoQDeAZrS7u2e_Av_b2v0TjWt1R_e-zU4LuMRxD3dV1toa52jCf3x5Dx07I3VoFJvBI5Ruwl5VLOUHQOZDOHHfEzG8jsdj4cIOMSsO445Op9UBpP6ho9bQpnUewgz2SF7I96FFo61ZmPqsKoIvWlZmV089Bae42Wr2O6ZnoM2I_O41fwaTQYQDCoC0gNfI4QO7zoQPcT_OOwZcOz21a8b6fRP4K4wV2lHuBs5O4-ml8mDDFlgov8Ql_CYErK740qbWYw6XrniI_1Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fHauoZfoqoW1D7lnrSYS6lbKSOjgqDJkjXqETqyro4y-Z2OE8iFrOrSJGO2JuV2rpCvuNnM0ulJxCrq1vDwS8l1zKweD8Ys-7mYsLsr_LyMY5eYodCCHLy5iDr6ZQ18SbMop6kLFXnlW9FfgcvBfZHPspcr66kIqp2YQcwV2W4or7ThQYY4DSJVcUMr-REsoDBVxzEhkBY-AMW1Yut7mnjxi24EW9uagJIGhq-sH0Z3OUc3gMPzrzetGZtyQ8wZgMEzLl8dlEB6bujL9DCmff9qfNxqsCUnqsmNG7Emen49S2P44WojYr9RMtM6ApaignrEnGxRUZv4jOnCgNw7a4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم برای رفع دائمی مشکل هرمس با Antigravity یا مدلهای دیگه، از اونجایی که گوگل داره به پرامپت اولیه سرک می‌کشه، بهتره ما هم هوشمندانه عمل کنیم.
وقتی متن خاص اول رو تشخیص داده، متن خاص دوم رو هم تشخیص میده اگه هممون همون یه کار رو انجام بدیم.
پس چیکار کردم؟
این پرامپت رو نوشتم و بهش دادم:
توی
soul.md
هسته‌ات، برو و تمام چیزی که نوشته شده رو به یه لحن دیگه متفاوت باز نویسی کن. محتوا همون باشه، اما کلمات و چینششون تغییر کنه
و بوم! جمنای دوباره فعال شد روی آنتی گرویتی</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4846" target="_blank">📅 08:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4845">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انگار نتیجه‌ی کارآگاه بازیا درست بود این هم راه حل آنتی گرویتی روی هرمس، با تشکر از سهیل و Moh جان: https://x.com/i/status/2084572159016382738</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/4845" target="_blank">📅 08:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4844">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NdDUrkK0K7ukZXGOlY9pFJw9tE43iOP5LbBI0-Qg8HP2R-Hp3mDBR8-u5a0sVcGwwU3bo8oXC_5ixQrmhUWNTczQA0_yPPaP900Cy6QcCkhHWBGTpw2LefPlF-eHvkYXWRxma-MoXiSMu1wJIeoGVGfLtlF3VjEiNCuUIuGdUwoSJT4Uu1uc6OGLBgCNhVVzkmwAYLO2R817tzSG3ZSeetdl9gvtWfjZF98SNy7GqS2p-ag1CqTRMoCVqH1N_JPn-tyRKQBm6MJov_-n2o_pdOdkW2ZACiXPu31IPpiTZYLXuSddviXg1_KRgCq2KvBHy4IpUJXJYCxpstkHNSRa5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به نظرم مسئله از خود پرامپت سیستمی هرمسه چون درجا ارور نمیده قشنگ ۱۰ ثانیه طول میکشه. میره فکر می‌کنه و برمیگرده</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/4844" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4843">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LAToxVaHeu9Ka5d4lV5oiZR72pz4cMZcND21NNmNy8M3vlfDTlRzyaVywJMYng9rK_pqOf91GB38F9J5SXvfYZELcFDeepkZMNMAZ8T4UxpSgxk6CA3bmcFynjIxmt2mdoctPWaRnp36fozWtarCFEl8bJUWsqpE6-qQWP_ZeqsAQfb93xAWUYsBg3ld5zp-Y2s8au6uk7YpcgcvN4yUbYAjrit7G73dkmTXwummiXV_N1E89iLaemJOZqYQKjkAEv7LylSqWX7BmpaSXyOA__1Ec9yVroWpU_Mte5qwyEv7uRBft1gMp6faldfRqPohHZy9VyTQKa5rGYcrlxVdWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلا درخواست‌هایی که "Hermes" توش باشه رو رد میکنه</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4843" target="_blank">📅 07:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4842">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router جالبه که روی هرمس هست فقط جای دیگه ازش استفاده میکنم مشکلی نداره در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4842" target="_blank">📅 07:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4841">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sW84-cR7ZGFF_W39dWNTLFSgXTxGxC6nERxoxgNJQJxgLcUtq05zRiu-F2xKdZPNzI-Z-79kMaj4etdwRbUWujQ6gRDutWjJmt_5NuN2ve879W4LSe6w961BSxgrJnxg1W0HcnZ530UaEraps4eq0d8xvuTbXizWIrvpLiTlWVzEzCAIn2c-ZgKsbTdXegmi8R-7M1WLQSlZ84ucA3dCl5i61ePST6jLoUkLFsuHOwcsa-2_mevphAksiDW0bV9RxYg1-ph6F7BgdFzb5cld136AJjPotSAGR-vEtLmQlJB3SXAufunV7RBRFa0A4cZmuYWe4T38ZwOLyMbLm26rDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان منم دارم به ارور جمنای می‌خورم روی 9router
جالبه که روی هرمس هست فقط
جای دیگه ازش استفاده میکنم مشکلی نداره
در تلاشم درستش کنم</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4841" target="_blank">📅 03:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4840">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ODQCgAWDMU9PzymXE-Cq6qKNfCZc3TcA7xC1NkeENJdvp51V_kCKwhbLEvD53uzBHfBzEyiq_O_fKj92qG3b_g_1ECOHbZdkJupOhw2c9DXvcNVjtggmSV3Ep0Wy-RThj7NJEFR8uZfen_DUnxuiiKyEnyEWYAKrHDBwNDVyhhAeZoE-3AvU9TkFLSsDANmB3_jbwpCIe5yBoHigeUKMfdJITvhuPtVAd9Y7s4dD7p0g8TzC2SSxoF8HDyk198pkffLy8dD002yaTuxk5btN_TBs8bF1evG7UHEkN0ZeG41IGcknoxFhyiJEmFtwa6JkdRTqNT3hdcd_tW5tFZVjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچها اگه از pomodorus استفاده میکنید</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4840" target="_blank">📅 00:57 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4839">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">رفقا ما داشتیم خریدهامون رو به دانش‌آموزهای بی‌بضاعت سیستان‌وبلوچستانی تحویل میدادیم که یکی از همکارامون گفت یه خانواده‌ای هستن که چند ماهه وضعیت خیلی خطرناک و بدی دارن.
بهشون سر زدیم، دیدیم کولرشون چندماهه که سوخته و شبا موقع خواب میرن تو حیاط و پشت‌بام می‌خوابن، اواخر هم فهمیدیم بخاطر گرمای زیاد، یخچالشون هم خراب شده. بیشتر پیگیری کردیم فهمیدیم خیلی وقته که وضعیتشون این‌شکلیه و کسی بهشون توجه نکرده.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4839" target="_blank">📅 00:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4838">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">به زودی قراره یه چالش(چالش هم نه) ادیت بذارم، و ادیتور بگیرم
خوشحال میشم که اگر دوست داشتید، داخلش شرکت کنید
اطلاعات لازم رو می‌ذارم تا فردا</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/4838" target="_blank">📅 00:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4836">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cp3XdZZjq2ye9ZGnNpOtcpDf9O7fCtIKLLCIB-c3CWGl46Yiff_XaWQuqZ9axGHj6XOJL9zJaIhv89-Vwb21RzT4ZfaWfr2ZQ0KGiJBH6xcn6hvdUL58aN_KrHaMNz2W4MhwHc83-l8xbDMpZa0Je38XcFCLCcXyvE71j6kWJ_7ZdfrhTpCvEdiehYckAgWtREo5KL0qYCSXZCu7FGdPhg6EmzPZXTI7GcpuhFjTjskaB7xPbaXA_rPu6z1DBJolh_Jg7AVTqHYmQKuK9ihsrXi341YMNePNLVM-kfaD1fqXJN5t2mDRwB1Wj8ltLB9U0PhiF7VHW5J7C3-rvOVaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از چیزایی که راجب کامیونیتی فارسی باحاله و دوست دارم، اینه که زیاد توی کامنت‌ها با هم در ارتباطیم. کامیونیتی خارجی، این شکلیه که ویدئوی تکنیکال می‌ذارن، 60 کا ویو میخوره اما کلا 25 تا کامنت میگیره. یوتوبره اون 25 تا کامنت رو حتی لایک هم نمیکنه. اما کامیونیتی…</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/MatinSenPaii/4836" target="_blank">📅 21:09 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4835">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RnFnggmUDTINS1JXh6rBA6-ON_b-Deu4Byx0F73GpQnRDczoar4FI2ZbmGijov1XljigPfBcKdqrq6IkqCfiHdF5kug3mzWYygz6tglN4LwelTKV26a35wmNIaCO6vZWcrEBGxMZGelshwQh2-h6Qv9guqr0xX5RqRiYsI1cWQXARiA1WPl0KMp-ThpFPtEL-wb5nRx2N-IsC3rVwoWNCfv4xUaeRImpzhrew2aHKgNwRPrtTVLJftOA_2hgv6MOZkGojKx9Q9RoZIJylqq4ATEbmAiNL3B3vKnvfXc_CWrGqqRK7t4_Rb0GI68S6dLlbE24CeXY65ryNi_hkA3sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگزین متن باز Fonto، رایگان، تحت وب
دیگه برای استوریاتون پول اشتراک ندید
😁
و اگر دوست داشتید، از بالا(علامت قلب) به سازنده دونیت کنید تا لایسنس تجاری بخره و فونت‌های خفن‌تر واستون بذاره.
لینک پروژه:
https://github.com/FontWoW/FontWoW.github.io
لینک سایت:
https://fontwow.github.io</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/MatinSenPaii/4835" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4834">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">و به هیچ وجه، به هیچ وجه روی کانفیگ VPS نذارید.
فقط روی ورکر و کانفیگای رایگان
چون به سرعت از طرف دیتاسنتر ابیوز می‌خورید</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/4834" target="_blank">📅 19:19 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4832">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pd4lGygL8BNlpUKft23TOCb5rjfGyFx6XlZyOpscrMKx2CBGFJrWPO_bQPUjtEKgJYJ621MyfDwNTGQNaQcbuICx-gwNcaRQBjzAHznqYG2a_qeQbeRgs4E-26OYZyVKSd4dKWx55WmAZA7l5M--HTvH2vn-Zx5PFXlBw7G2mHXfmWXM1JfSALs9yqlVP5E9FQqmYgj5GJdwktH-NnFSBP6m76fY83x8IbgkXtLGmsOSpRLQSTqcGHQUbLT884p_p61NXo7W5bk65ZvObR_fFPc50A4QsIOutaKHQnoZH4Nr_Teb-KU2goZYOk-zkGqi897WVDjjN4t9C0Qn6pff-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/g56SzKyxHxhxNzAysP6cisKf2cJUbkMJmcsRu1vMgCACUHeI8a6dHDMeZ92bGHYBmOGl6ovCWhEZ5Fzb6qvTh6AO5jKdWSV9_rotDtd8gj2Q6oDo4P0XQeMvVKshzh6IqleG89J48h6ld105egAyQkV2ot7Hc-EWgwX_eBaR_C6SbfOXme70XrLkTfH2nLgVksoiidIWNzwpTh9d9tpPQxJoXttNIpQyV47nsdkD6LezdKQ63EFSwjAVDJ3pM3QxR3i050mJmXQljkndArREhhx7WHoSn4IdC9Fbb8elfX8YlNACaTkvHGL4F4G5UDHXiyA-BkEiD679o61d0Nt62w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/4832" target="_blank">📅 19:18 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4831">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cdKzgJxT57Jov7fGn8TwTmkLIM7DwLKb6UHqIvBJB0VzS5WPWDUvZzokIvC_lhAqVVBf3QPwCD7WaRvLSv0xtSfYj1QETbKUlLH0j44jGtMeSopVpnBXkVa5yNAfPGHuGwhlwwvLQ5BeGQilB_cz4CuFsQfDTGQ3-j3WM8JbSLvAeh9SSkvkKd-oSbChQl569lAG2LMBdAwUta50ULtQHdaZe1veYKnayYlPeN47oJCTVr3CYbBCs8cZClDmADDAWzaVRVgkPvNs_bbTZcJc3qZ_XLzxBR-hMIumQ62xHeCnLEo7ojPXUUqazYZDDMbA_chlJItsyyaq7DuWBM8bOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید: https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/MatinSenPaii/4831" target="_blank">📅 18:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4830">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اگه براتون سؤاله بین مراکش و اسپانیا چه خبره، این ویدئو رو ببینید:
https://www.youtube.com/watch?v=7k-TTp84X6w</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/4830" target="_blank">📅 18:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4829">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خیلیا ایمیل دادن پرسیدن با چه شرکتی کار کنیم
ببینید شرکت‌های ایرانی همشون یه افتضاحی به بار آوردن. یا چنل پروندن یا..
من هم شرکتی که واقعا کارش درست باشه نمیشناسم. ولی خب متأسفانه وقتی مجبور باشیم، چه میشه کرد
الان خدا رو شکر دوستم واسم نقد میکنه از خارج از کشور و میفرسته و دمش گرم</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/MatinSenPaii/4829" target="_blank">📅 18:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4827">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/LuQ0-LqqX7BUbrC5vUBQXPYsX0Zxdo_AzjmGHqsTEyu5y8SrVhJtDM3MvydjrJ4rf0iBjGtKi0c00ppNaUtfxWG5EcNF6WWIByYEFhFOWlocjEdv9btu9sL6lwu4MnNdMkkxYgaNcUsU-hEDE7xdszun1aAZAtDo_kYAtMTSR-av-aSB7zDxVQp2Eca__fGYXHlWlgB0KIibA-1CaE_MeeJMSVakXY567ebFxaJAaxviWArTGS7R_VEmamsDBE7xJBl-MyeZLlTDho6TGpj1HHNlpNYPaKGg8W8ktI7zYQT3kSeZ6CL4igOfBePgwG2CAiBo9CGoJVoj_5ojOCRIzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n4z9uyoc3mz0AVTyZIx_GDib7sm8Z-rmf0fvfOHVGw0IJP57OcrhKscrp2mwVa6hYh6Mfao3HYW-FiKM3MsoTtoLZRTvqai5JAPfP0HGFYroBDgIdUoS7ErN4fFpKDSxqFxxu7Z8rc7KMhNJD8oBrR3ZIxMjR61_dN3XjbEc_e8kLDlQeh0NyTnFuPPQfnyX2XYr690ncXy7XDyakOBm9CJS76TIjUYFyNSsNVFjPG8XqQgcd9w-8VGy-N1yxRkukWkZfLuvdXMAjF2opwD94Qmr5dhPNHtdec1R0JFoQoIR6WUcrqHzHNMhCkqw5A5U-DK94766SsVvyXZoq3dZbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادش به خیر. زمانی که من یه میلیون تومن هم برام نجات دهنده بود، یوبر این شکلی جوابمو داد و هنوز هم اون سه تومن مال 7 ماه پیش اونجاست:)
تازه اونم با قانونی که یهویی گذاشتن.
همون روز ادسنسم رو قطع کردم و کلا حسابشونو از اکانتم حذف کردم.
هیچوقت با همچین شرکت‌هایی کار نکنید</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4827" target="_blank">📅 16:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4826">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPavel Durov(Pavel Durov)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr2lm2befFI1FZocVKfwjUwWm_RUaJ7KE01GCLw4wt5S-W37sdQ92xHlWt8hog9L94mo2bgFzmcckVbD7tynCY2CGJQFqcvh2PBLCZdsmGREQeWkz344-KXUFscxmjyghGiZn00Pdr4jdPaVum-0BnuvbNjaWiIudY-sVQL8UpNKULNwqwlgBd9WfBJofEp1RFBj-hMoTM7kDUkY913B4tWWSR_LiDaXp2HQK3tSZ8Yxva-PoLLgRX9uEGZapjnwnSNLy5ihYRNkEqYw-_Oiq_kHyd7zx5SPdYWNjIAB6gkD7frQ6XNJiuEmkcjJduG_HiNL0R2gmhVloz2AyFQ56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
The 2026 International Olympiad in
Artificial Intelligence
starts today.
As a token of support for those who will reinvent our civilization, we'll issue
🏆
240
exclusive
Intelligence Cups
to the winners.
💵
We guarantee minimum buyback prices ($
1,000
per
Gold Cup
, etc.), but the cups' limited supply may make them worth much more on the secondary market.
Good luck, AI coders!
🍀</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/4826" target="_blank">📅 15:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4825">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromPersian GitHub</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aT_mVuG6Pf1unyOeLjvFnrJd2yA5F7ImiL8jrKwqYLIv_Aq0AuC8MPuVepwbZIsq6d9CL8-8g0kR6sYJ7dzTa55BJDcCZ4vGpGC-Ev7INv-nv22AOeCtWqeEoiMIG_ruNOWqrjQLSAwS9vTsImK9PYWq2kj6QCtG7BeBIHQgV6w44oXsNCfna0NeZ5bGIuK_kCPXdUiNWrX1UyeJI-97UDWq8m2501njf_ylTmPXT8a6t9DYelQ3mN0G_hWTW2Wu2_MAHOX1s07P0pfJFCiL48GgWLhzqc-QuNRGGTZTdXa2H33VeAVKEKDDU5uoZpU9oWS5FLH8gC4ANA4qqD4Bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر روی گوشی VPN دارید، دیگر لازم نیست برای لپ‌تاپ هم VPN جداگانه تهیه یا تنظیم کنید.
ریپو
Relay
یک ابزاریه که با اسکن یک QR Code، اینترنت گوشی به همراه VPN فعال روی آن را به‌سرعت روی ویندوز به اشتراک می‌گذارد.
اگر زیاد بین گوشی و لپ‌تاپ جابه‌جا می‌شوید یا نمی‌خواهید روی ویندوز VPN جداگانه تنظیم کنید، این پروژه می‌تواند گزینه‌ی کاربردی‌ باشد.
https://github.com/Mahdi-mortazavi/relay
⁠
@RepoFA</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4825" target="_blank">📅 15:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4824">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PNRVSfevR2meO0ire-bkUIfjjU8zyPNB79Xt-yf5PfKvAV5TPWJ4lefyBV3n_qMcWph1kKH7sTgzlC2toexIh1Rf2rcAhMmzXOruMpInCHWOGXg-Plgdf6qA5ZEz3t5QGEZ0YYW8jFOtiE93Dk_dyO-JIxHR6ZWikWlV0wn_ZqnXP76ABMXKqRIfD0R_oEEBKVPixP0vgGoGkSNE-16iBIOFyuaK96lBPFB3gsIuVH3JgZO54rL0f-sgz2JW05KU1eKebvZLmfv_vjjiHkpryReyXt3UeeovbgptsMWIo_CYBKR4sAnMQ5RPRC82Band0Ow-2ish8UhUw-NSmhwJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقااا من رندوم برداشتم از گوگل
برای این ویدئو
اصلا هیچی از F1 نمیدونم
😂
😂</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/MatinSenPaii/4824" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4823">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=o20ND9qztdSDYsjBakZavmtPB0mU_c_r9GEjh-Y20K2XrA0fpDUnRfoP1OTlXdjOtZ7c5ewng-FaRpaodj_V5XMLKBbCsOD0qS5UGpMVZhFgtt6p6JudFTw0CCt4CBWtjmSom62HSYURjN1-ueG7_OkQLO7D5QyIUTReomfLWGOKv3Xaib9TRSH8u2jc0Wyzhk7WtEz61CBJGbzftDotWwJzjv44_jG7lYYiVT3ZqgSdnTOXU7G95kLzcf6pR66wt6x7LXkEwQN5wk4aSVI44zH0MOOZzX833fhSx6q69VefeIAmwX042Zsu5FSMVtEE2em1XAI4pOVu7xCzz0QjFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7797f080f2.mp4?token=o20ND9qztdSDYsjBakZavmtPB0mU_c_r9GEjh-Y20K2XrA0fpDUnRfoP1OTlXdjOtZ7c5ewng-FaRpaodj_V5XMLKBbCsOD0qS5UGpMVZhFgtt6p6JudFTw0CCt4CBWtjmSom62HSYURjN1-ueG7_OkQLO7D5QyIUTReomfLWGOKv3Xaib9TRSH8u2jc0Wyzhk7WtEz61CBJGbzftDotWwJzjv44_jG7lYYiVT3ZqgSdnTOXU7G95kLzcf6pR66wt6x7LXkEwQN5wk4aSVI44zH0MOOZzX833fhSx6q69VefeIAmwX042Zsu5FSMVtEE2em1XAI4pOVu7xCzz0QjFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍷
درود به همه رفقا...
آموزش
سا
خت کانفیگ Amnezia VPN(وارپ)
• صبرکنید ای پی ها رو لود کنه
• بعد یکی انتخاب کنید
• تیک فعال سازی پارامترهای امنزیا 1.5 حتما بزنید
• بزنید روی ساخت کانفیگ Amneziawg
• دانلود کنید وارد کنید داخل Amnezia VPN
• میتونیدم کانفیگو کپی کنید + بزنید بعد insert بزنید کانفیگ اضافه بشه
💡
نکته:روی تمام اپراتور ها متصله هست.
لینک ابزار(ساخت کانفیگ):
👇
https://darknessshade.github.io/Amnezia-VPN-Config/
دانلود اپلیکیشن ios
دانلود اپلیکیشن اندروید
@xsfilterrnet
👑
@ConfigWireguard
✅</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/MatinSenPaii/4823" target="_blank">📅 08:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4822">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/W_ElIMQTT7oWw-EJWMLcWGoRwq-h9WihjMujkwLwu6gNQC0r6EbLn8ezthmbM-Ftv0vNdFXilrFFFPFnAqShu4IqIe5jcxC_jxshzm282rJTnGziN560cgqT7s-RDEaKhXoeeA15uSTPnzCaA4osMBQrXTQbGayBmc8GRGTHB74Xi2i6WH-l-aGPmVsoXm8IVF1T4K-5c3XRhRB1qCX8518dG_M-77shBymwCnjfq7QCaGTVkn_zDcyKZj7JCuvYCBI--mPRDtP5Fi5_KYw-P_aoNfyf_pqBnT6uuKuz78lUYZyPulw9qfKLE2G1CASI0k3KlY6mAOY0aqzfMbzTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)  بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.  مهم‌ترین تغییرات:
🖥
یک GUI کامل…</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4822" target="_blank">📅 03:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4821">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EAvSL8z4NNu4Nre-0xuIFlHF_58mszIO8i4w2Px8ULQLc847JBGK9u7_wMxtBk1x0XEUs0pyId2ttlfzjhYRyrCPFYcIxXY6TJP6085wM6NvBF-WRqG4Z3mFseOvXhrxgCzAHBLNp_JjxdM_AEZb8uOdOmlUtarZWaMAkNdseYLyzJEDxsI4tchO-M186Ayj2XCAE-yM-rNrnPMoY-hEXgT9-VbmOCvjrjqgoW6MIE0tlBDnQgtC3PlhdZDNKZP-ImMCDvyJhQmjXqtYyX--cgGeSthSbwXFDu8omSEaC0S_RJTHO6RGz4OsFKJj7kPjhF74XC_LgBaVRPBIj0woxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن دهم و استیبل SenPai Scanner 1.0.0 منتشر شد!(اندروید و دسکتاپ + GUI)
بعد از تغییرات گسترده نسبت به 0.7.1، این نسخه رو با رابط کاربری گرافیکی، موتور اسکن بهبودیافته و پشتیبانی کامل از دسکتاپ، اندروید و CLI منتشر کردم.
مهم‌ترین تغییرات:
🖥
یک GUI کامل دسکتاپ برای Windows، Linux و macOS
📱
اندروید از نو بازطراحی شده؛ Kotlin + Jetpack Compose + Material 3، پشتیبانی از اندروید 7 به بالا، APK جدا برای ARM64/ARM32/Universal
⚡️
دیگه لازم نیست منتظر پایان اسکن بمونید — هر وقت IP سبز کافی پیدا شد، متوقفش کنید و فقط از همون‌ها تست سرعت بگیرید!
📋
امکان کپی نتایج (همه IPهای سبز، ۲۰ تای برتر یا یک endpoint خاص) حتی وقتی اسکن هنوز در حال اجراست
🔎
اسکن همسایه (Neighbor Scan) دیگه اختیاریه و به‌صورت پیش‌فرض خاموشه
🌐
تشخیص ISP و ASN چندمرحله‌ای با چند منبع (Cloudflare، IPWhois، IPinfo، Team Cymru + دیتابیس داخلی رنج‌های ایران)
🛡
اعتبارسنجی واقعی کانفیگ‌ها با هسته Xray؛ پشتیبانی از VLESS، Trojan و VMess
📦
خروجی مستقیم به IP:Port خام، Share URL، Base64 Subscription، Sing-box JSON و Clash YAML
🧠
موتور اسکن بهتر: الگوریتم weighted-random برای رنج‌های Cloudflare، جلوگیری از IP تکراری، پشتیبانی چندپورتی، خواندن ورودی از IP/CSV/CIDR
جزئیات کامل و دانلود:
https://github.com/MatinSenPai/SenPaiScanner/releases/tag/v1.0.0</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4821" target="_blank">📅 02:55 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4820">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Hallelujah</div>
  <div class="tg-doc-extra">Leonard Cohen</div>
</div>
<a href="https://t.me/MatinSenPaii/4820" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">00:21</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/4820" target="_blank">📅 17:25 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4819">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه. همینطور قابلیت ip fronting هم داره و سرعتش…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/MatinSenPaii/4819" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4818">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">⛏
۲ نکته برای بهبود سرعت WhiteVPN
۱. بعد از اتصال روی دکم
ه اتصال مجدد
کلیک کنید تا به سرور جدید وصل بشید.
۲. همچنین میتونید به صورت دستی تمام سرور هارو پینگ بگیرید و به بهترین سور به انتخاب خودتون وصل بشید.
آموزش تصویری</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4818" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4813">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN1.2.0-arm64-v8a.apk</div>
  <div class="tg-doc-extra">35.6 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/4813" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/MatinSenPaii/4813" target="_blank">📅 11:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4812">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgNN46K3br4bm-_CWumiCBZ2ZHlhclDbWnR9V5d15RGKtXrkBQ5oAwAWlm_FqhcAePdDROGTe96oUUBQvZQf-wLxLOrAE1FdSqMawoFguYq_lX5C7xh_oFF1I-s09JfkWBuxc5ujawsUaPSr7RflxGAeua8aTOFrb1cgDKUbPXg1HcZK6kNx6hNpRsmc9GB3_CF6kKD7k-LSPY_qKAJWr2cUr7_kBmUAUKTB3O76PYPsSYMh1hOcOQUhtm6f1M9v8kW2jFvvzvgLGJ3v8gzjBYEMuZik9vdICKtAT_kz_mdkV13wfyuPmiX1S58AO58-KjdxqX2D2DiuCXRdTC8Ghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
آپدیت WhiteVPN 1.2.0
✍️
تمرکز این نسخه فقط روی اتصال
سریع‌تر و پایدارتر بوده است.
امکانات و بهبودهای جدید:
•  شروع اتصال سریع‌تر
•  انتخاب هوشمند بهترین سرور
•  جابه‌جایی خودکار در صورت اختلال سرور
•  کاهش خطا و نیاز به چندبار زدن دکمه اتصال
•  بهبود Real Delay Test
•  رفع مشکل متوقف‌شدن اتصال در مرحله شروع
هیچ تنظیم خاصی لازم نیست؛ فقط برنامه را به‌روزرسانی کنید.
@WhiteDNS</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/4812" target="_blank">📅 11:32 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4811">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GqC_bqAWhYSEWtEiwlK9qQ5CzyxEgbv57_BGVJP1Vr6C16U-HB4lkUxSwiic0TyBkXjyVSCCS4tnfQVlM-jQa90s5rRFj1LUcVYhhK_M7ksc3WYDYz10wRJhh6ybBVPH3SnEwYAVotNew7IfDeDLnYD7sIc3X-YImOmuc5aSIwvz2VYVw1ZAtiRuH4Kd7mwUe_6Vgc9owGDeLRslJHnnylUq9OJ_EBg01TRfCofDMAUYiKV0cf9b0YARe9duha6CYZu1p69PgSeOeVM0yXZgLCCXutfnV_Zf5mXqcljCRrU-2aO_3PCTMRzjF56RLqwQXCaYIrhqTPFkFeD9f5wwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متاسفانه پرومو رایگانش تموم شد:)</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/4811" target="_blank">📅 10:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GhLxhaHLtxsME6FlnEnlAQyIZaCVkte3DmNrUquMs5mjUQledGLbR6Or46Nbw9JZlDJr9NyHoNiUMmj97hq6LgsbyWIHriaEL3gPIGKhG3hR2YVwx3JNlvbIeFaUfWLq1P1gILcbUQ1OQ8xLt1t7FLGiWLfECXAp6cLcaI8FxsUlwiRDD4cdjbsegI5eBeCqz2GqFFMXjSuDVGeBsyfM81EstWuSvFHLwIwkRF9p-8BrQt5e4mdjmkHo-BmiCpYLORDxvUz4ppllVHWekohGGbJCpKuRprVFdlwjieE4P5SGVocXqaI04a1uWflijodFgPQr9nsM1dPcpo3UXmHw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان بیشتر مدل‌های دنیا وارد «منطقه کشتار DeepSeek» شدن.
یعنی مدل‌هایی که توانایی‌شون کمتره و قیمت‌شون بالاست، دیگه رقابت سختی دارن و ممکنه کم‌کم کنار برن.
✍️
Ali</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/MatinSenPaii/4810" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4809" target="_blank">📅 06:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سرعت آپلودش هم عالیه.
قابلیت‌هایی توش پیاده‌سازی شده که از همیشه استیبل‌تر بشه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/4808" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/udjP2MbEcK6kyLTo97gP8gT23Mc9NWQR6ubYZF7O0hlD5o5S3qApj1xC-dlQawIFrQ7Y36zsubTPWeao2AlFS6ezj-00FCGYNnNdiQoZd5cP0cYjJ6AGyaSzztqKLi4VZNYiaccjt1Cho12V1j02bRU8wekLk5YqsEzi-JdAHqmbbq4_31ZlIPHjKJkruutXKPXiSibHffBqadat-FVF0uP6ERg_Hwn_nu9OhMboajN1uEb1tdnSMPXCc8z9o3oGsFIITwYC4klWDeee7Aj7IDYA-OyeO-bqmcSsVQjaUlUOrVOl5Ac24gumdXBtxhL7ndeqGfYy9dRwgHRi3TkE4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/bVAxripVBbe5KVizxzoVOrl5T6bh5kkRS_qig3bjteZ8ThIhYO_LsrsXVx9EzbTe44wvHnGIMA9_silwy5S4TtHzUrrum0e4NvEPvAnYjoXz1j3yRWi3WRKlC5NR3sJljmIXV1d-FRqIbjFpsiChjQ_b5KKzXk6dqNKEMtc9g3Av05QyXJbRXMK3BNY2FIXyTZWmzmmU4y2zfYqrhgSa6Y9xgFcGoFFAzMYK9iwy3vECbW1xXGTrbQmPYVJYL4zoOyjcwbBIWC9UMNf9ztlypbMMOG7wyzyZ3q6hjdSIUdnguEaUToV-BSdlWkJcJ6kvdM6aZgJooYkS0ykdDnE-aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دارم با پدی نسخه‌ی جدید WhiteVPN رو تست می‌کنم که چند ساعت دیگه میرسونه دستتون
اول از همه، روی همراه اول با سرعت فوق‌العاده کانکت میشه(زیر ۵ ثانیه) و بعد از اون هم آیپی/سرور شما رو یادش می‌مونه و درجا کانکت میشه.
همینطور قابلیت ip fronting هم داره
و سرعتش عالیه(حداکثر سرعتی که اینترنتم میده)
دم بچه‌های WhiteDNS گرم واقعا
❤️
🔥</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/MatinSenPaii/4806" target="_blank">📅 06:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دقیقا این اتفاق برای منم افتاده بود و سه ساعت داشتم میگشتم ببینم کجا پروکسی روشنه که بدون وی‌پی‌ان داره آلمان نشون میده
🫩
🫩
روانیمون کردن</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4805" target="_blank">📅 05:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Qwen-3.8-preview.html</div>
  <div class="tg-doc-extra">44.4 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایلی که الان با Qwen رایگان ساختم</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4804" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4803">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">3DHouse-Kimi-K3.html</div>
  <div class="tg-doc-extra">41.3 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4803" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فایل 4 میلیونی‌ای که توی ویدئو ساختم</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/MatinSenPaii/4803" target="_blank">📅 04:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4802">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پرامپت ویدئو آخریم رو که با KIMI3 رفته بودم، الان دادم بهش و واقعا نزدیک بهش در آورد
🔥
به نظر باید منتظر یه مدل خفن باشیم. فعلا توی Preview هست مدل  تازه Kimi نتونست One Shot کنه، و این One Shot کرد اونم فعلا رایگان! کیمی نزدیک 3-4 میلیون پولمو خورد
😂</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/MatinSenPaii/4802" target="_blank">📅 04:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4800">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Hfqi6FdAiY24j4Ojw9THoGvbiGJqNGHnvUbxPOY-h1CT6BmiwpC5aPA61hD81H1g63XsoTEe19tNQimYQCq8DnTdPjgqYfhxynK9xo10GxinU82pIoBQ4g9lTXCx1StjhpFXUjp4JuUp_3Fj0KxLuTf_L2UFmb93UoaCFDeHzUww5RVDgvOUSVJsWljos7Pu7QszSPJ3q3nOuUs8Ob42Qq2g90olk0BumaBuS2bjb3PaTsvhg0FPoVBFUPpZJnNol6lulcJc2NfXEjWAK077aWGiqChLzrrp_DiZYuWvcROJKN_BDikGbTJWw4BJZQElA06105HLOgGomA_lB3zaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ThHDHniY1rhZZGmly7Dg4kRaL0J8OBcIC_z91PJXU0bsDflC_RxVZtdMWQnPmotoVB7xjx0-xyT2Gb_PePO92q0gHUyFOSAnAPLllQ137uCUe0Icd8zZXS009K8ENwwW_XwQNWn3Wu4h7rENo4-UOMmJISFdUcvI0Gav34jgWqGz0ZsU1XAjsbhW7eb8nq25mf72p1944whKyW7ZHLNjoMLpv-neJRkQLIYqF1JxoF7IBlFOYQVGG2jP7hXC78YcQdy8VXLsAiiTqKBawiGgOs5gExY3dLTtaX5OSrmdR6lcMRVRkivzuWInN-P9IaY9pN6tNnsclcR_pLPa0P13rg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوستان توی infron.ai میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.  ممنون از confesious عزیز بابت معرفی. فعلا دارم باهاش کار میکنم ببینم چه شکلیه  تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/4800" target="_blank">📅 04:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4799">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fN8GtcGHOKYTSoOVVck61prIcmSbp-76_ZS8K0lgR8TUIXXB53yz5HLtG0FjXrO0apny48vfkxgpX5-oJUXn5RpvjwfPyA60CR_HkWRF0LArPek1EiiyNBS5QwhgnYpReDUU9-epzE3EBMalA_77AzWv8BzN06EBd5Ilci4H1zooa-jpEM_2YQ1ITNX0rfNcm8aU_e5lksR8ljWulUAdOOnzoBEwgn5_Bg2b6tSC4RYz6h8fySfNiTovwPlesg3cWlsj82pJLr5W-uB3hdQce5v2uR77tMhCQnfmbLlHJ2i_6of0UqkQ4PaH9S38eWSAPq9wdVrb4YgBEpBmJoO7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان توی
infron.ai
میتونید رایگان از Qwen 3.8 Max به صورت کاملا رایگان استفاده کنید.
ممنون از confesious عزیز بابت معرفی.
فعلا دارم باهاش کار میکنم ببینم چه شکلیه
تنها محدودیتی که داره RPM 5 هست که میشه تحمل کرد</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/4799" target="_blank">📅 03:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4798">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/MatinSenPaii/4798" target="_blank">📅 02:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4797">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">برای منم روی فیبر مخابرات فرقی نداشت
تا اینکه یه پینگ از همراه اول گرفتم دیدم همه چی رسما قطعه
🫤</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/4797" target="_blank">📅 01:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4796">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-poll">
<h4>📊 از گوشه کنار زیاد میشنوم اینترنت دچار اختلال شده. مال شما چطوره؟</h4>
<ul>
<li>✓ به زور به تلگرام وصلم⚠️</li>
<li>✓ اینترنتم کند تر شده🔴</li>
<li>✓ فرقی نکرده✅</li>
<li>✓ ایران نیستم👌دیدن نتایج</li>
</ul>
</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/MatinSenPaii/4796" target="_blank">📅 01:37 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4795">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">خدا رو شکر توی قطعی نت دستاوردهای بزرگی داشتیم و اپراتورها از وی‌پی‌ان فروش‌ها ضریب دادن رو یاد گرفتن
😑</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4795" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4794">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRCF | اینترنت آزاد برای همه</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uIVLZOXeEYwRYNFcflLd2CNsbAxvJPRWQO597zXE2mtXasNKrVMLT7AzU6u4T0GLF67AnV4f0o93c3EE18QnPMxyaJWJUq6lk8L-elw9iQvQbfR6oR--_jynda_x8DDY-Vzvre8sxH03p2pN2tYcoH8butfVzwpth-Tv6fikIvgmZQvp_N-RpPAkbM-Ou1tSum1Svz7a6AzY0pyE28E_jdcwwZ1JbyqZtowcECxKB6xUyrKc-XNbFys_uKf_5aDG7JrvRrp-ksOwVMiZZfXMLjj-W2WxSvXpi4Xx3qP77uW4yhmtEyrNZju7ZNK8w8tfN7L7-7lqlkRckN6OXH4O4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهت کنجکاوی در مورد موضوع ضریب جدید روی اینترنت بین‌الملل، ۱ گیگ دانلود کردم و توی پنل دیدم ۲ گیگ محاسبه شده!
©
Farshad
🔗
ᴡᴇʙꜱɪᴛᴇ
•
ᴠᴘɴʜᴜʙ
•
ɢɪᴛʜᴜʙᴍɪʀʀᴏʀ
@ircfspace</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/4794" target="_blank">📅 00:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4793">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4793" target="_blank">📅 00:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4792">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7lIVgWsTKPsl4h6B8UQw9tA5UsVoE5AaR2r3OGSmJOG05InQuohMzjK2PCMJaUIwvt5jrsxAqWoajKrTlQAEaZrly9I78YVuCoP6sq1KDmOacSwSSOwrLxiH02nHXsSV5j5vSIxzzjjZ_bkBw7JKGnC0UWWOr6FFi1xRbWW5xEK7C7W7Wt9ff9aUt-S2e_Gbvc-LxueOVfbDJ_Jwf4YvEvSRxJqmDgJMuhm66Izep25DSsABjAKe01_A07lm9sO0T-ESjRjB4s2gTzTm2bK0RQsIgPDbyLl-XhAvYEn0s5u7tJ-lMdIKAd9e2jvrhQVuWMJnuAr-Bz1A9kCHWwtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">+000000000
😔
شرکت PCCW Global</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/4792" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4791">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">به نظرم یه تماس بگیریم باهاشون</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/4791" target="_blank">📅 00:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4790">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج 205.252.xxx.xxx داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/4790" target="_blank">📅 00:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4788">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromiran internet monitor</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHf829JjkjEDyhBK137X0V6mtl0aMhjVghbFjFAcrQbnBT472WrOpofudxrPcXnkHLihXr3Iz7FyFIwuBlreqB8DrA6jOWY2Ux1T_tah19JULD5kYnfPGMA6S3ryL3cDlpbmpr6lT8gDSj4r9LPu8dB-pEJqSWGNx2gOngWKGkO4yZqfGdsYsvnZL6O21TWnSsmd8D7gQn6idBZDbQRPC5NpN0-1Hfud0g-5RHi2BdMTPqozvthfCnwsTveg-GqV-E3U7l8GvJ_NRh8Q7PbGHT_lkfhCyPZ3WCcNnz87h68n87i4Bwxjlnypobmlnre2Zk-1rs3_GsecRiH6fhiKRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnHOF18r5Ptr-eoUygQRxjTPACipyjlvK-lMUL1igm0JIiaSYUxtjRnAJkzzXj4kmMAHHdyBGNpHvc6Bth_wOHj8XEygWqe30G9sZ2sasgUnEecD7Hu-mc_OyvY6PlGa7zz0SkgXQBHfVioVgM-uyVEQBaNYK9EBr39ullUAojMNjciOJpQof7Vs_WZTsAguQuZ0nr1HB2WehJxWrLgYLtcSZ7h9F3TolcyoqKqL8OVqgc0sqRpHhswNHb93PDMaxFkII-wDN8RxCRkIzno2y8J2pO608zTVCRpG0WCLBYXVW-6DcjmVfCU8jt2xzlMl_FSm09iQYNr6QkDFbfeGrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهرا تغییراتی در مسیر های اینترنت بین الملل زیرساخت ایران به وجود آمده ، دیگر به جای اذربایجان و شرکت دلتا تلکام شرکت المانی PCCW Global و ایپی رنج
205.252.xxx.xxx
داره نمایش داده میشه ، وضعیت بهتر که نشد هیچ بدتر هم شده ، مثلا پینگ تایم کلودفلر رو 5g ایرانسل قبل محدوده 80 90 بود الان 140 160 ، درنهایت این وضعیت nat کردن اینترنت در ایران داره به یک روال عادی تبدیل میشه که جای تاسف دارد</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/4788" target="_blank">📅 00:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4787">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B_xFasJAXuC4O1RVhd_lscbq-TvLtKpxD7zCJuQAXFi7AZU_VbUa4TtYAETV17j32jb5ejme-ouJuh5xHgQFUxxigLsxkGgkBpQ9ybDA9W84C2eHdu8pv0nLyfwQ5GYLQHxPlxsTj8zgn7Zb6Yg3o63Li74e7PWj2j4JgbFUCgBZTSG3l-w4g3r7zyVUo17w2uthC9vnYMD5jHAEkEP9F3ZptH3Al7u0F0fmZFUd9OSWMhJ5PMrqof1Vc9bfpqe7Pcmnw8K-X2g9sUFGYRltjsB5kmgt8i47Gmv2rSULg1l7hkCle9ydrXGOA4bk4M4e4YSu-24E_Uj_Uh3NhEB-3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریم‌ورک Science One گوگل
💡
گوگل یه فریم‌ورک تحقیقاتی خودمختار و «قابل‌تأیید» معرفی کرده با Chain-of-Evidence — یعنی مدل فقط نتیجه رو نمی‌گه، بلکه زنجیره‌ی شواهد رو هم ارائه می‌ده تا کارش قابل راستی‌آزمایی باشه. قدم خوبی به سمت تحقیق و توسعه "کم‌خطا‌تر" با AI
🔗
https://research.google/blog/science-one-framework-a-verifiable-autonomous-research-framework-via-chain-of-evidence/
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/MatinSenPaii/4787" target="_blank">📅 22:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4785">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HgqK4NZMFD5g9852F1xnF1hV5yuy7OG-KBNkUKuFsxaLKg5ayjonSzE5r3z38rlCm4dnGOZTwQNfHy7mNUQA-prZ-S8c2kx4kiOGD5oEYyUncIyNNd5U_oRdDQQ7yM6NRGmlErnpM2hl0l0JgRCE3YH96J9lwRSlzi2WNAlC_TTnoDtp-yV2plj9EnQMzcYNdosnDrdHRfFXlD4J04QoypWJ3vij72dkkXd0EVNCQowP2Kbt2mOdHlgmdHncg-x1vfDVKQI9Hrc4hb59D9dbvfd6qUhbMCZJ2pyltOzWiAHxUo7iUf2DjkkDmPyysrVJheJITGg-BkuWMv0H_KxvVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/HhSmkkQjrjnirSzutRm0CBBRplISN_PM2Xopl8l2Umq0inYBalZDCjpDdm9FaWhAdKexnbzNL6_5gmql9o1xl3afceB1cx77KWBj0kXl40Gimwd21iRNgFSBpXlfKPP0eQSwMUViLbV2oAVS39s8sTTTp9JmEVTMf9UP9D7_XEaXIblfusy4QNoLb2XwVEgBmpScR5uDfdnL1Lr5vKey8vlxncYcBgdb-jttXqHBPuTKJZQTFtgvs2szqJxcrQa49XunZ_mK6URyBloysSHGryAEFUFdNRPdzTqoclcZiRQo3JC0rd_YebmEGeAYezZlnLaH6JgGDGzGeTek37Urpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/MatinSenPaii/4785" target="_blank">📅 21:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4784">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/MatinSenPaii/4784" target="_blank">📅 18:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4783">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">برق رفت
🥀</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/MatinSenPaii/4783" target="_blank">📅 18:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4782">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">این پرامپت‌های ساخت بازی سه بعدی واقعا به درد نخورن(توی سنجش قدرت واقعی مدل) اما از طرفی اعتیاد آورن. هرچی میرسه زیر دستم پرامپت ویدئو آخری رو بهش میدم ببینم چیکار میکنه
😂</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/MatinSenPaii/4782" target="_blank">📅 18:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4781">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی: https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو: 1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت…</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/MatinSenPaii/4781" target="_blank">📅 18:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4780">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام رفقا
ما به رسم هر سال، نزدیک مدارس که می‌شه پول جمع می‌کنیم و واسه بچه‌های سیستان‌وبلوچستانی که بخاطر وضعیت بد مالی نمی‌تونن ادامه تحصیل کنن کیف‌کفش و لوازم مورد نیاز واسه یک‌سال تحصیلی رو می‌خریم و بهشون میدیم.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4780" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4779">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">با پنج دلار ویزا کارت خریدم، ایشالا که کلاهبرداری نیست
😂
اگه خرید کردم و اوکی بود بهتون میگم. برای Claude که حقیقتا جرأت نمی‌کنم</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/MatinSenPaii/4779" target="_blank">📅 08:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4778">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یه هارنس چندنفره برای اجرا کردن Agent‌ها. یعنی چند نفر می‌تونن همزمان روی یه تیم از Agent‌ها کار کنن — یه جور VS Code مولتی‌پلیر ولی برای اجرا و مدیریت agent
👍
🔗
https://github.com/yc-software/qm
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/MatinSenPaii/4778" target="_blank">📅 01:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4777">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromxsfilternet | فیلترنت(امیرپارسا گودمن)</strong></div>
<div class="tg-text">🍷
درود به همه رفقا...
پترنیها یه اپلیکیشن مشابه v2rayng زده که به نظرم از خود v2 هم بهتره چرا؟
هسته بروز که توسط خود پترنیها داخل اپ قرار گرفته و بروز بودنش حتی از v2 هم زودتره(بیشتر آپدیت هسته v2rayng از سمت پترنیها بوده)
رابطه کاربری روان تری داره.
مهم ترین نکته اش اینه با قابلیتی که واسه
#فرگمنت
اضافه کرده شما دیگه محدودیت آپلود داخل کانفیگ هاتون ندارید(بیشتر کلودفلره) ولی بعَی سرور شخصی ها هم مشکل آپلود دارن که طبق تنظیمات پترنیها اکی میشه
🔥
دانلود اپ از گیتهاب:
💓
https://github.com/patterniha/v2rayNG/releases
تنظیمات مربوطه به آپلود:
📝
https://t.me/patt_channel_x/94?single
💡
دوستانی که پترنیها رو نمیشناسن:پتنریها خالق sni spoof و شیر و خورشید و همچنین کلی از کارای بزرگتری بوده و داشته از جمله خود v2ryang و...
@xsfilterrnet
👑
@patt_channel_x
✅</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/4777" target="_blank">📅 00:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4776">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">Matin SenPai
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/MatinSenPaii/4776" target="_blank">📅 17:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4775">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">با تینا پارتنرم مشورت کردم و یه سری تصمیمات خیلی عالی گرفتم واسه‌ی کانال و چند ماه آینده
فعلا لو نمیدیم
🎨</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/MatinSenPaii/4775" target="_blank">📅 16:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4774">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود مخصوصا راجب این Demo های وان شات https://www.youtube.com/watch?v=LmXU6SEH3Ks  جمله‌ی کلیدیش این بود: The Demo is cool, but not actually a game این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/MatinSenPaii/4774" target="_blank">📅 04:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4773">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QJfm5wtF7zPTWDuBadd7emADtqqeL0hAIKy7-5FoOrS0xXWlvA3HVGbLG00xPGc_5MPnu5wLAirrofqvLv2QRV7tmFgmvk8728StVESCvUuKGlfTc7V7jwY9n84d_VIkd-WnTOcWqfnNjp0htEmwOr3sZuey0y46pOQjfL1flAnCeAiC8nPeuFfXqhxbx5UcGg9Y88tSxVyqE-_AEZHNppfoSwBQmyBpYCIussk-DqG1gZbniJaGVHfrNDBZAHuAtRVlX6fB5a6dgvZVBEuITrifg6PFHLM1fuws1RFcAYRsfZnnnUmY2KfgxAoBNBOwOpdfufshGmJU8L8jTJtq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئوی پرایم واقعا خوب بود
مخصوصا راجب این Demo های وان شات
https://www.youtube.com/watch?v=LmXU6SEH3Ks
جمله‌ی کلیدیش این بود:
The Demo is cool, but not actually a game
این یعنی شما نباید با دیدن یه چیزی که یه نفر با ai اومده کدشو زده، یه وقت این توهم رو داشته باشید که می‌تونید همین الان(حتی با یه اشتراک 200 دلاری کلاد)، بازی بسازید بدون هیچ دانشی!
طبیعتا کار رو خیلی سریعتر می‌کنه، اما باید مراقب این باشید که ai، لااقل هنوز به این درجه نرسیده(و به نظر من امکانش هست که هیچوقت به این درجه نرسه که دانش پایه حذف بشه از این چرخه) و خلاصه، یادگیری رو متوقف نکنید. حالا توی هر حوزه‌ای که هستید
نه جزو اون دسته‌ای باشید که میگه ai به درد نمی‌خوره و Anti-AI هستن،
نه جزو اون دسته‌ای باشید که ai تبدیل به بُت‌شون شده و می‌پرستنش!</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/MatinSenPaii/4773" target="_blank">📅 04:09 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4772">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سی‌ان‌ان:
فرماندهی مرکزی ایالات متحده (سنتکام) در حال آماده‌سازی برای یک دوره دو هفته‌ای از بمباران شدید پایگاه‌های موشکی است.</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/MatinSenPaii/4772" target="_blank">📅 03:28 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4771">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یکی کامنت گذاشته بود، بعد کلی که تایپ کردم راه حلش رو دیدم کامنته غیب شد. رفرش کردم دیدم پاک کرده
😭
خوشحالم که خودت راه حلت رو پیدا کردی مشتی ولی این رسمش نبود</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/MatinSenPaii/4771" target="_blank">📅 03:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4770">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Claude-Free.txt</div>
  <div class="tg-doc-extra">4.6 KB</div>
</div>
<a href="https://t.me/MatinSenPaii/4770" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">مربوط به ویدئو بالا</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/MatinSenPaii/4770" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4769">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ea5gk7FE7LteIrCAqS0eU2Fy4RMFbpI5esqAkjVaRtU5matC5RwrgxtsVYAIHWxil8K_2gWCav2wh8gkLH-FJ8qkawR8nWUQmsSAYuafQufczrUIrE4zueO1IuRGKqRAVsKcMfkvkGE12RaNeHo8Kp_8H-g-Y59IEXiw8Qit_Nhm-D4UGOW3j75IFN5bXgLW8kmR8jc_BXmXse3M6MGeANqOGwScFd8SHfFDBULSSyEfHpruDHv01BOIa4hf8DFQWWXkqpuiNwnV3jhBH1GVq5GHYYnHQxwKywhL2KYZk7adlc9TE2fYqVXhy6GWVEmEmDx_fPOWQiUFBnjdZrPIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
استفاده مجانی از Claude و کلاد کد روی سیستم خودتون!
⚡️
دستورات استفاده شده توی ویدئو + پرامپت سه بعدی:
https://t.me/MatinSenPaii/4770
⭐️
توی این ویدئو:
1- بهتون میگم که Harness چیه و دوتا پروژه با یه پرامپت یکسان که با مدل یکسان ولی Harnessهای متفاوت زدم رو بهتون نشون میدم
2- کلاد رو نصب میکنیم روی سیستم و به روش استفاده‌ی رایگان ازش رو یاد میگیریم
3- با استفاده از 9Router، بهش Mimo رایگان شیائومی رو وصل میکنیم و استفاده می‌کنیم ازش توی Claude Code
4- با استفاده از API از Kimi3(مدل قدرتمند Moonshot که توی بنچمارک‌های فرانت‌اند در حد Fable5 قدرتمند ظاهر شده بود) هم استفاده می‌کنیم
5- با Hermes+Mimo و با Claude+Mimo و با Claude+Kimi، و با یه پرامپت یکسان، یه بازی سه‌بعدی می‌سازیم و خروجی رو مقایسه می‌کنیم
⚠️
پیش‌نیازها و نکات مهم:
1️⃣
همه‌ی مراحل ساده‌ست و نیاز به پیش‌نیاز خاصی نداره
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/MatinSenPaii/4769" target="_blank">📅 01:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4768">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vo1tXqyF-ZGfsDiPHmNjIg9EGdyG2FKBLklGydkNAFK7YcVvzF0vyRLx27CogNbFEDhQbpvEj5WUmQv2P4LRsj8-6yZEndGyywYyy6E_z9_XQalovjLrxEewiZvayIoxdJz8t87aL98MQ8jsK116wugaWDOKMdeLen5BZ7w1feKGaXv_gyN3jxFIob-IMbZNZGxQnfy9WRpbleSgnWs1coQBmM_xTV7saOTen5pULZb6naHtf6h7wdMtyiUa4uadIwE8dBlbrYWCPFrUFn0Icoomf5jUYhzHoy_1M_ay9S6XcbjixLRwnysLrJGdGOW4zetiZIopGaUNMDWAjtdYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/MatinSenPaii/4768" target="_blank">📅 00:57 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4767">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">یه آموزش باحال AI هم سر همین سایت ادوبی داریم</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/MatinSenPaii/4767" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4766">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.7.0 منتشر شد!
➖
هستهٔ Aether از 1.4.0 به 1.5.0 ارتقا یافت؛ شامل بهبودهای اتصال مجدد، اسکن، پایداری و امنیت SOCKS5.
➖
پشتیبانی کامل Zero Trust اضافه شد: Team، ورود با کد ایمیل، Service Token، Access Token و Gateway سازمانی.
➖
DNS سفارشی…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/MatinSenPaii/4766" target="_blank">📅 00:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4765">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بچه‌ها اگه خواستید شما هم توی هاگوارتز ثبت نام کنید
من نفر 37 هستم
🥰
https://potterhead.ir/?ref=WL-1B24AC#waitlist</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/MatinSenPaii/4765" target="_blank">📅 00:40 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4764">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">(با کلاد رایگان زدیمش ولی)</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/MatinSenPaii/4764" target="_blank">📅 00:22 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4763">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OHndvmR0Wzh-VyfMm3fLHb-vY5Y-t7qjje03uZL96k5TI6Gtvz6ijS9eXO3HNjbcml1b3bms3fXxlkedu0xMPdyGuKJzXDHA4D7Xn9ZOlIg6cP2AC6ZXeGSmp1j2y8S7ggcbKA8brbQBfP8Yg6bvwFeCMba_6y6dXkpERRn3m3rlTokg84Y3VQlMoXk9FV1HN2sCOMJIQWC9HMdAcuYaNozuQRqSBuRJGT9fC364ngNktNFcjNZU3ETHmBZ65-NMW8zp0L25c_73OFKLLWfwwShk4PLGGbVD9nZr9DZs2GSaib8tmDFK_nW5dVlIGCtAzUgVXGKALb_184mU_r6hbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این قراره اولین ویدئوی گیمینگ چنل باشه
😂
😂
(بازی سه بعدی توی یه فایل HTML که 15 دلار پول رفته سرش)</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/MatinSenPaii/4763" target="_blank">📅 00:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4762">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/MatinSenPaii/4762" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4761">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gRmCQl6At9pmqOcb0b7Ykf6I33_6aH27r7F-FkR65ZdHPjnqtT4S77Ag3c7CF0srgTLnNtPqbQiCvWhhKVy4XrsIaDdVTjF9ggqb2ulx5s9mLORR5pssSB7G6qTQYz34Vn6HmykeSes8rltwgnTUg2G1h4BUpj0fuQkdZa38uLBldFBpAkHPQF7xXgfF7MqjtCzXkCq34RVTE8fes2Y7iVRYGFlk35y7bROq2BlUJjPB3InfJkLVPeROl3kOR8d4ppie5WQYrV0cl-6dqOja772PoN5p8WZYvOJRGmNjNp9J7HnuZ6FmrBSaHZYu1Pbby_UNVaBJz5ZQxaRZEEt5Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت بسیار جالبی بودش</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/MatinSenPaii/4761" target="_blank">📅 23:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4760">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QS1Ct6SwUGXQH18Cpeq9i6B5Scpir5lMT_ICLz6orNH91GZEQHr8QWjgrOTH56QI3yl5RdX7Tdpvpm88h-8XS0gMcVpnLi8XgiJ4Cs1docg3hY8bVwswClzGCCaXKjhpKcNJVog8MmRV5QJX3XfiOJakmI1hTNEUkUYix1pL4wZxDPloSWVMmns0bd9dLqJaOKPwQQK8m8fQBzzMVrntVH_pP_GM_lgsNR-hNKdvTGScpFatfeMsH8B9a_zUIHmvYISW4Sq6grZ11XQ-7Owvnm79yEmK3W5LFbA1a6575QDPSf8DNJexnTI-iMzQLm0Q4IRSd39sPbVEqiUVjKMM4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه پرامپت دادم به هرمس که تمام اتصالات سی پی یو لپ تاپم رو داره میسوزونه</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/MatinSenPaii/4760" target="_blank">📅 18:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/jDjIf0VylwBXvlUEKeZdKuf2MivBFq36jD3ZQ5aMky7618DYcLoXxrNuCXBZ1x3DfW0RGAk8ducp2KLkvwWkMJSh6zT8zZOlLkVPbSZpHyl8aigmLlxZahTPjNneZsCcLynidva1Yq4tsc0rrhcEkvoqAMsLvQOqDPWQVuOJRSh5El4jHgbx2_HofNpISza8k3B4j_SXZRlQS4_zW8h6O8O0pFA1mnhSB4Wum5Sq-BhpsFxOXOTwdW-UwSagMiqwSp5f4O6BwnxdiUzgSyjCZBNU9VU75Dbr_gCA4DTHe8BiZ1M__Y6J0or6oA2TyChvDVBXnY22PqO9G-BBB_zYIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آپدیت جدید Aether-GUI v0.6.0 منتشر شد!   هسته‌ی برنامه رو به نسخه‌ی جدید v1.4.0 ارتقا دادم. تو این نسخه تمرکز اصلی سازنده روی تأمین امنیت MASQUE، فیکس کردن باگ‌های مموری و بالا بردن پایداری اتصالات WireGuard و Gool بوده. منم یه مشارکت کوچولویی روی خود هسته…</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/MatinSenPaii/4759" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">و روی یه سری قابلیت خیلی عالی برای SenPai Scanner دارم کار میکنم که به زودی ریلیز میشه</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/4758" target="_blank">📅 17:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/V1bUV7g6OH9Oy5E8wIUco3PgnPtK_b-e_oPM5yYazAxRdPKtb8mjhWP-3mw67ErauzhVlrBGpCGUUshIQjnRqXOU2-44WbSrc1ijW8lRbQrR-PcucbEyFMCrCYUrenJsoavG_A8un7jmRKE5nOpz_XYfXDkWCAAsGJNl6xoBP7W10FO8aIw80GLdgX1IdqQ-QOoe1lhhKWT0SsHzQ7j6RyHKdFDoBdcsYKdDKSy3j5AvCJiqclxaC0K2JwrF_aQPF6YJDLq2whIObGvxYPxqZgezM4Wmp0lysM50VW_uXbg5gp1aDYzynKbv9K1wYd-5xAR5t9pKYlqdZBOZ118ygA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورژن جدید Aether GUI هم به زودی آپلود میشه روی گیتهاب</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/MatinSenPaii/4757" target="_blank">📅 16:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNima Aksoy</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=aGjNQUmUyFvxs5uAXV1mtW7K_Kus_x2GTL4JmwK0wYkAZObPscQFq3ouUZ2BeyQoR_hnhb8nM3_J45RqsLqQjtsxtVZj5r4j1roYiBA5EnPN0422Oz8bkSn7PiRyHASIXHndafrbF2VD8ExH26rmyBSyDm12qEs9wtBCLEOM4ABGAgaHXIQAAYfO7nt8ketMRGJvcEDSH0n5a1Cc9Xo9yEN9QeztwMCXu_NIR10xrvDIw9owTSG3bYBBB7DrfoHAFpWu5OXsFKgXH2elDPADLTngGfFkU_m4uDADppHH5QcEd36bp4UoqffUopB06IPrEv-Dcnto34zwt0sGoUK7ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21266e3b26.mp4?token=aGjNQUmUyFvxs5uAXV1mtW7K_Kus_x2GTL4JmwK0wYkAZObPscQFq3ouUZ2BeyQoR_hnhb8nM3_J45RqsLqQjtsxtVZj5r4j1roYiBA5EnPN0422Oz8bkSn7PiRyHASIXHndafrbF2VD8ExH26rmyBSyDm12qEs9wtBCLEOM4ABGAgaHXIQAAYfO7nt8ketMRGJvcEDSH0n5a1Cc9Xo9yEN9QeztwMCXu_NIR10xrvDIw9owTSG3bYBBB7DrfoHAFpWu5OXsFKgXH2elDPADLTngGfFkU_m4uDADppHH5QcEd36bp4UoqffUopB06IPrEv-Dcnto34zwt0sGoUK7ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر با QR Code یه سیستم جالب برای انتقال فایل از یه گوشی به گوشی دیگه ساخته.
فایل رو به تعداد زیادی QR Code تبدیل می‌کنه که با سرعت پشت سر هم نمایش داده می‌شن و گوشی دوم با دوربین اون‌ها رو می‌خونه و دوباره فایل رو می‌سازه.
بدون نیاز به اینکه دو گوشی روی یک شبکه باشن
https://github.com/bashalarmistalt/decimen-optical-transfer/</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/MatinSenPaii/4756" target="_blank">📅 16:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-4755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">مصرف GPT خیلی خوب شده الان که تست کردم
گویا از خود GPT-5.6-Sol استفاده کردن که مصرف هزینه‌ها رو کاهش بدن
😂
شرکت OpenAI امروز قیمت GPT-5.6 رو به شکل چشمگیری کاهش داد: مدل Luna حدود ۸۰٪ ارزان‌تر شده و Terra هم ۲۰٪ تخفیف خورده. نکته جالب اینه که خود مدل 5.6 Sol (قدرتمندترین نسخه) برای بهینه‌سازی load balancing و حتی بهینه‌سازی forward pass مدل‌های کوچک‌تر استفاده شده — یعنی یک مدل هوش مصنوعی داره مدل‌های دیگه رو بهینه‌تر می‌کنه.
این هم خبرش بود</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/4755" target="_blank">📅 16:46 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
