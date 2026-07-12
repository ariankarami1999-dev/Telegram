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
<img src="https://cdn4.telesco.pe/file/KvRRoHMgctw-ifpnNZYr_KLKb5rpm2pTmX66vDC0J0qK6iRlWdtDeLzwgBjF7fiNfyheALMoGH4YtyQXF0INRppfl3cAeXBiPIXTy-FeZuT4Akf4XCwi2YUJQF-pQtCzVxZNGVR9T_dWhwSSvP8CB786wbwM7mBBucSE5XA6MFBke3Ekr66wq03nsshsVhLnipybK9hnp8hncrGUxx7734BkrK2rUS8O9206PDLlkPdVmSiO6YkdPfgJAB556-yHtqmrDGbPJJ6tZMUPAH47ExE8hTTxCEYjqd9PllPaJibXTf4L_AoxyTBhuMgo0d52vZCspEL0wxbEeGucv1_0cg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 374K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 01:42:33</div>
<hr>

<div class="tg-post" id="msg-17705">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">آکسیوس: ایران به چند کشتی در تنگه هرمز حمله کرده است!
@withyashar</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/withyashar/17705" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17704">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجار میناب دوباره
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/withyashar/17704" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17703">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش ‌انفجار اهواز
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/withyashar/17703" target="_blank">📅 01:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17702">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTArh9HD_vaNOMNQw4ESQClZ1vkr5YvSGuhJo3JPy_C-yDsef8wtMvd76e1T1MQLWdympAjZyIFqvAZFoMdfxfpJPk6dhtWbZdwPcvzVRqri2AlJ4NEtOyiPMyD3xdAWAaStf5nDfCaj_eXWwdoTQMewGeUcm9YypVMe8_WQjKADbByubrM3Ay7Bw4sghjxzjPCWH4aUDoj3sfkmPxfamauRD6OHoOrxOdI6ux3V08b8vOCF4BHD7F2AJi6Wx57o7K-Xb7lLT63GExizY3mwqw2qql_3sNlvCSqR2Q6ljrcZVUOfWEZu0Gfet24G-T-G69lN37W-BBpDGkwKsvr9xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور مک میچ کانل که صبح شایعه شد و گفتن سکته کرده، عکس منتشر کرد و گفت بخاطر زمین خوردن رفته بیمارستان چند هفته و سالمه.
البته من گفتم قبلش به شما
@withyashar</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/withyashar/17702" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17701">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/withyashar/17701" target="_blank">📅 01:29 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17700">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/withyashar/17700" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17699">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neHtYz3r0ThoXQCcNqi3SIwCeQmEAGX2h7idTBalyaAsqcuh-XWPo5tFzLdAAQGNKh5yJjCdrTr5W358ytGi2DyZz3YEwPTDcmVkNuwTepR83U2l5otxltBlaY33FW9Zyh82ibbpeOK6FOR7e2RB4mS_SZNTWfQSd2OJTGf28WbuCqsr-7kaqTJmIX-va9Cry-9Gjx_cY_7TTSHOfgLDqquT8tCDLys1gXciXokYtbGlFAmJdsnX2rPGV6iLKFRPNthUhZPYYELww-tyUIYlnG37QZIU_bSuJsT-NehQ1CHBAAEMbjYM1aMXqczONHFAqZYllgd6nv8MZvQf3fqPOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/withyashar/17699" target="_blank">📅 01:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17698">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">انفجارها در جابر، جنوب شرقی ایران!
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/17698" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17697">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">شبکه سی‌ان‌ان با استناد به تیم هاوکینز، سخنگوی فرماندهی مرکزی، گزارش می‌دهد که نیروهای آمریکایی یک موشک کروز ضد کشتی و یک پهپاد را که به سمت کشتی‌های در حال عبور از تنگه هرمز شلیک شده بودند، سرنگون کردند.
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/17697" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17696">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">درگیری نیروی دریایی سپاه با یگان های ارتش آمریکا در منطقه تنگه هرمز!
@withyashar</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/withyashar/17696" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17695">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=fk8WgHimw1kbTpaCxWCfaQn6vN7zY3naDJ7hs3-bds_-UeyRlZ6dfrAkHwArLU0mmGjCjJV6SxEyrG2ZN7-78zILB8qvOHQerxY8pIhDcG4r-hW5k28Uo27KyBI6eTonvGdpg53O_vF_sAQcc5ueQ78yIerIQfjzvf-wENkSZ68NIxfejl0EzTO0499ty3RxACUA3sjDjVU658xFbdUYSaYUj7Gd21c_yPgY5zOYX5Gz35h2nOuus-sX7TtaDPxDLpPPB-hXil3orFuzDvqzIkDwM4x-rKMlRso54-KC8mlbfpj1IvIXR_4SXnuskxOi1N7o-KkfQLkJD3II8W81Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cb166f70c.mp4?token=fk8WgHimw1kbTpaCxWCfaQn6vN7zY3naDJ7hs3-bds_-UeyRlZ6dfrAkHwArLU0mmGjCjJV6SxEyrG2ZN7-78zILB8qvOHQerxY8pIhDcG4r-hW5k28Uo27KyBI6eTonvGdpg53O_vF_sAQcc5ueQ78yIerIQfjzvf-wENkSZ68NIxfejl0EzTO0499ty3RxACUA3sjDjVU658xFbdUYSaYUj7Gd21c_yPgY5zOYX5Gz35h2nOuus-sX7TtaDPxDLpPPB-hXil3orFuzDvqzIkDwM4x-rKMlRso54-KC8mlbfpj1IvIXR_4SXnuskxOi1N7o-KkfQLkJD3II8W81Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/withyashar/17695" target="_blank">📅 01:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17694">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خبرگزاری صدا و سیما: گزارش‌های اولیه حاکی از آن است که حمله امشب یک دکل مخابراتی در نزدیکی روستای طاهرویی در سیریک، استان هرمزگان را هدف قرار داده است - همان مکانی که در حملات قبلی نیز مورد اصابت قرار گرفته بود
@withyashar</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/withyashar/17694" target="_blank">📅 01:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17693">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دکل سیریک رو زدن
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/withyashar/17693" target="_blank">📅 01:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17692">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50699388f.mp4?token=PFp8zRxz3W22CIoiQe9BS44MTC2XdSvRvGu9YV0MSs0kJqKY6jcnSv7vXJt06O01RBW3Mx1bH6uN_mD0RK8Om5Edlc6rUqYoj1QY8OYIxCT91_eZr6fu8NdSCNbRQmJ3aH-zdS9KXP-tLCmk6sOEDipriuJNdHhwCu9U5QoG5_OCpsYsxlW4ZX6yPXkcUldayqMMpw0ZmyhqK4gtRMsaXqFKeEPIwYzmEO6w9zZQLPaNyYi2x_ECyQySz_IgySDvPyDomELusU_1HlvRJ7Z5Cs7ns5DNx5vyGMewSVItBrJ9twL4DZ74E7XmcRv_JHWrP9TVnJj9To0qI6vuJ9iRGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50699388f.mp4?token=PFp8zRxz3W22CIoiQe9BS44MTC2XdSvRvGu9YV0MSs0kJqKY6jcnSv7vXJt06O01RBW3Mx1bH6uN_mD0RK8Om5Edlc6rUqYoj1QY8OYIxCT91_eZr6fu8NdSCNbRQmJ3aH-zdS9KXP-tLCmk6sOEDipriuJNdHhwCu9U5QoG5_OCpsYsxlW4ZX6yPXkcUldayqMMpw0ZmyhqK4gtRMsaXqFKeEPIwYzmEO6w9zZQLPaNyYi2x_ECyQySz_IgySDvPyDomELusU_1HlvRJ7Z5Cs7ns5DNx5vyGMewSVItBrJ9twL4DZ74E7XmcRv_JHWrP9TVnJj9To0qI6vuJ9iRGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به جایی در جنوب الان ، فیلمو داد نتش قطع شد
🥲
💥
@withyashar</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/withyashar/17692" target="_blank">📅 01:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17691">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آب سنگین خنداب ‌اراک رو زدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/withyashar/17691" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17690">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پایگاه امام علی سپاه در چابهار هدف قرار گرفت  ۴ انفجار سنگین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/17690" target="_blank">📅 01:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17689">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۲ انفجار بندر
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/17689" target="_blank">📅 01:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17688">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17688" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17687">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">فقط عکس بدید و فیلم هچ چیزی‌نفرستید
🙌🏾</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/withyashar/17687" target="_blank">📅 01:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17686">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/withyashar/17686" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17685">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSEZTnsGmOXyRhqSx6-UYwBb43-lZpJRWhjGfbdVoGLsJ4G0nYXKSpLwIY15y_cG0Vt_xz8JCDmajZ2eEJtxbrQTDOGViLX2zejbsyNBdQ-9PLmY9wVrRA4sqchOKho9Zz27FyVnvTLybO2t7b38hbi5snzyPDBnQUlX0GU_Gf61lK8X-ZzKNHhAPAEqmiFh2yv1So9aX9ySqWr3EAo5mOySg2WtCLw2imgZkmmYk-LVdOKpog6jbTiqtbv7K6HPaq69_dIrgVstZO5iZ30-4gCQQu3a9z30HmH6QT2DeWS7PIE_Rd5W7TZHuGh5wQl5y8X6vxx9FqV9rcTcTscf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار شدید و سنگین سیریک طاهرویی روز شد !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/17685" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17684">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer"><a href="https://t.me/withyashar/17684" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17683">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">همه جارو دارن جنوب میزنند دایرک هنگکرد
😭</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/17683" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17682">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2qDA5ktPodPH3V1H7Y4JltlZkP1XBz4HmFIny6ZMHk7Ds_39N0WJc5dpQAa61fCnR2JFllnNfdEu12JbzmDDJ3aXQ5nhORu2QRjrHhPeS7n4XLxpWee5ImQDhusOxVlzCYOgxKoEhmjXRPZzFpgsIG7tCHSygQULTz_k8E439FjCiv6hkAn8bf7z0wCkrKvwIqM8OCnzOS1qzcoI9XZoprKfQ2iHqsjo360KBBD3SLVXYiH4oEpVOW_wXghY_HZMr92WarC9yhfM2TRb_OzODFcsAJLxdi3vAqCGy0e40K-gYqtt34z177xFu35c0S_RxBoJzLfLXG_attNlAvykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:ساعت 5 بعدازظهر به وقت شرق آمریکا (ET)، نیروهای فرماندهی مرکزی ایالات متحده دور تازه‌ای از حملات علیه ایران رو آغاز کردن تا توانایی این کشور برای حمله به دریانوردان و کشتی‌های تجاری که به‌طور آزادانه از تنگه هرمز عبور می‌کنن، بیش از پیش تضعیف شود.
این حملات به دستور فرمانده کل قوا انجام شده تا نیروهای ایرانی در قبال اقداماتشان پاسخگو بشن.
@withyashar</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/withyashar/17682" target="_blank">📅 00:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17681">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">گزارش ۳ انفجار از جاسک
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17681" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17680">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">میناب موج انفجار و لرزش شیشه ها مشاهده شد
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17680" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17679">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بوشهر صدای انفجار
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/17679" target="_blank">📅 00:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XS71TdRH6asOPxUegUbHNFx2mhZ0eNZp-YO0zHfMkscEKqxyqVvqPrx-cqlSf_9AtSDsEBZ-vHBR6YOlqsV4qHxAOMM2p7Q8H8Rd50lYvqxyvnLA2EGeM0LYlvuV5FYIsplHdkO93mu_N931hF3_X9ZnU8F-soAhuM_5-JsMKWel8q53LzGSUt_Bmil6ZtVPHSnlJzPs9LgNvt55tHVA0VjYB8DRaW4Bx1m-YKoM0GNNJboeIeWvPRr7HYDanJy9_rLLX3_nut-nujYxatdugTOVEGIeHekCL_IzDpVpquNS0ZSsiGQuSauaqjq24sxsyUkyZ-Er0RCDux0frLJ2uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سوخت رسان از‌ انگلستان نزدیک منطقه داره میشه احتمال داره بمب افکن خاص همراش‌باشه
🚨
🚨
🚨
سوخت رسان های که از اسرائیل بلند شده بودن به سمت عراق میرن ولی حدود ۷-۸ سوخت رسان در خلیج فارس هم اکنون در حال انجام مأموریت هستند
@withyashar</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17678" target="_blank">📅 00:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17676">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در کنگان
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/withyashar/17676" target="_blank">📅 00:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17675">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">قشم صدای انفجاررررر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 86.3K · <a href="https://t.me/withyashar/17675" target="_blank">📅 00:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17674">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شروع شددددد
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/17674" target="_blank">📅 00:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17673">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">۳ انفجار شدید بندر عباس
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/17673" target="_blank">📅 00:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17672">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار سیریک در مجموع به ۸ عدد رسید !!!!
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/17672" target="_blank">📅 00:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17671">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">دو انفجار‌ دیگه سیریک (۳تا)
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.5K · <a href="https://t.me/withyashar/17671" target="_blank">📅 00:35 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17670">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجار سیریک
🚨
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/17670" target="_blank">📅 00:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17669">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سنت‌کام
: رسانه‌های تبلیغاتی ایران امروز مدعی شدند که در حملات ایران به کویت، سه نظامی آمریکایی کشته شده‌اند.
نادرست.
واقعیت
: هیچ گزارشی از کشته یا زخمی شدن نیروهای آمریکایی در منطقه وجود ندارد و تمام نیروهای آمریکایی در سلامت هستند و حضور همه آن‌ها تأیید شده است.
@withyashar</div>
<div class="tg-footer">👁️ 95.7K · <a href="https://t.me/withyashar/17669" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17668">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یک مقام آمریکایی: ایالات متحده عصر امروز به یک سامانه دفاعی و قایق‌های سپاه حمله کرد و در حملات اخیر جمهوری اسلامی «هیچ آسیبی به نیروهای آمریکایی وارد نشده است.»
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17668" target="_blank">📅 00:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17667">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWlrsZFqha-NSBV0R84tEFfDTdLG6mX5oPJUt-Ccb0LsL6X1Z_c4up3VSQCPQpbxdh3yYy4XFlj9PZCp8RIiCPbkk0EFmINwYiREGoCXU6KmGQ8cmA1usRpOxm7FTh2kHkKhJsvYw6ZP7Uo2kL92QuQC-hybXVdV64uKMcRASSxnD6wFZRJak2W2OmQWZmzEX2D76NaXaHn2ewX3b-6DLrZ2j2EG4XcwGnZQWfYpJuRvolSVaNm6QqKZdgRx0KgH07ZzfqblBhl20DWLDqASQeGnppynmY2H_w4QRCk7FAWFbJ7lUMteiEiomPiA1ZwDvv0sMu-ljI-e7rRPYJ2egA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخلاف برخی اخبار، پرواز های انجام شده به سمت عراق ربطی به گروه مذاکره کننده ایران ندارد و برای بازگرداندن افراد، مقامات و هیأت های شرکت کننده در مراسم تشییع رهبر انقلاب است که در مشهد حضور داشتند
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17667" target="_blank">📅 23:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17666">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">الکساندر دوگین تئوریسن مخوف پوتین:
مرگ ناگهانی لیندسی گراهام می‌تواند ترامپ را به تجدید جنگ تمام‌عیار با ایران سوق دهد. این به وضوح به این معنی است که "شما نفر بعدی هستید". لیندسی گراهام سایه ترامپ بود.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17666" target="_blank">📅 22:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17665">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نیروی قدس سپاه پاسداران انقلاب اسلامی در یک اطلاعیه رسمی:
به ساکنان کشورهای عربی: از حضور در نزدیکی پایگاه‌های آمریکایی و مناطقی که سامانه‌های موشکی در آنجا مستقر هستند، خودداری کنید، زیرا این مناطق ممکن است هدف حملات قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17665" target="_blank">📅 22:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17664">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">فارس: قطر و عربستان بازوهای حملات هوایی آمریکا به ایران هستند
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17664" target="_blank">📅 22:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17663">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی: به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس، به زودی یک هشدار فوری منتشر خواهد شد، لطفاً کاملا هوشیار باشید. @withyashar</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/17663" target="_blank">📅 22:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17662">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">اطلاعیه ناگهانی منابع خبری عربی:
به شهروندان و ساکنان کشورهای خاورمیانه و شورای همکاری خلیج فارس،
به زودی یک هشدار فوری منتشر خواهد شد،
لطفاً کاملا هوشیار باشید.
@withyashar</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/17662" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17661">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کانال ۱۲ اسرائیل : بنیامین نتانیاهو با اشاره به مرگ سناتور لیندسی گراهام که امروز درگذشت، گفت: اون به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید.
@withyashar</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/17661" target="_blank">📅 22:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آنتونیو گوترش، دبیرکل سازمان ملل متحد، صبح امروز از آمریکا و ایران خواست تا به دور جدید درگیری‌ها پایان دهند و مذاکرات برای خاتمه دادن به آن را از سر گیرند.
این درخواست در حالی مطرح شده که درگیری‌ها عصر امروز از سر گرفته شد.
@withyashar</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/17660" target="_blank">📅 22:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17659">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snligxLRTMnsdy9hwWT10OAnUhRiDpGhjE7whD0B8yVIgWeCnXZzPidPThehp6-BunAPx2sgqxy8hbKsT7A89NiENT2kebcma33FnL6Fz47uLicE_bccH0sjf-XRaFkWAKNSen2Ngol5_EZPUd-zWUqkDL7mzUMBCULncioE2TwiQ2maX18cwgckedSD6E_LkBSCTrien8LZA2t9gIMQiR8g7BfMiCrI7MwiTxVZOfjq8suTcC9-QMtsWn6QhMY5z4TYw4YdUyjgROazSd6xNItlBA0wqt162FZJsjzTRsebzVnGu3AXGvOGwt3WJOuXFQDU0Qh19AcW2-y3a077_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تریپولی‌رفته و باکسر الان جاش در خاورمیانه است که خیلی امکانات بیشتری داره
تریپولی:
بیشتر یک «مینی ناو هواپیمابر» است و قدرت هوایی بیشتری دارد.
باکسر:
برای تهاجم آبی‌خاکی کلاسیک مناسب‌تر است، چون می‌تواند نیرو، خودرو و تجهیزات را با شناورهای فرود مستقیماً به ساحل برساند.
@withyashar</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/17659" target="_blank">📅 21:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17658">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نیوزمکس گزارش می‌دهد که ناو یو‌اس‌اس باکسر و یازدهمین واحد اعزامی تفنگداران دریایی (MEU) که ​​در حال حرکت بودند، در طول هفته‌های آغازین درگیری با ایران، پس از آنکه نقص سیستم خنک‌کننده موتور، این کشتی تهاجمی آبی-خاکی را مجبور به تغییر مسیر به دیگو گارسیا برای تعمیرات کرد، موقتاً از خدمت خارج شدند.
طبق گزارش‌ها، این مشکل غیرمنتظره تعمیر و نگهداری، قابلیت کلیدی واکنش سریع ایالات متحده را در زمانی که پنتاگون در حال اعمال محاصره دریایی ایران و بررسی گزینه‌های نظامی اضافی بود، از بین برد. پس از اتمام تعمیرات، گروه آماده آبی-خاکی باکسر عملیات خود را از سر گرفت و اکنون از عملیات جدید ایالات متحده در خاورمیانه پشتیبانی می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17658" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17657">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اکسیوس: لیندسی گراهام ساعاتی قبل از مرگ گفت «الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم»
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17657" target="_blank">📅 21:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17656">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اتاق جنگ با یاشار : این جریان خیلی مشکوکه صدا و سیما داره اینو یهو بولد میکنه مخصوصا این چند روز!  سید علی مصطفوی ، زادهٔ ۲۱ فروردین ۱۳۶۵ (هم سنه منم هست) مشهور به حجت الاسلام والمسلمین سید علی خمینی. وی فرزند سید احمد خمینی و نوه سید روح‌الله خمینی است  از…</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17656" target="_blank">📅 21:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17655">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ : کشتن سلیمانی یکی از بزرگترین اتفاقاتی بود که تابه‌حال در خاورمیانه رخ داده است. من فکر می‌کنم خمینی [خامنه‌ای‌] و دیگران در ایران از اینکه من سلیمانی را کشته بودم خوشحال بودند. چون آنها هم از او می‌ترسیدند.  او یک ژنرال درخشان بود. او مردی بسیار بیمار…</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17655" target="_blank">📅 21:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17654">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حالا یه چیز بگم مغزت اتاق جنگی رگ به رگ بشه بری تعویض اتاق کنی؟!</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17654" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17653">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد! @withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17653" target="_blank">📅 21:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17652">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بر اساس گزارش‌ها، چندین پهپاد ایرانی به تعدادی از اهداف متعلق به کردها در سلیمانیه، شمال عراق حمله کردند.
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17652" target="_blank">📅 21:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">متیو ویتاکر، سفیر آمریکا در ناتو: معتقدم در صورت برآورده شدن شرایط قانونی، توافق جنگنده‌های اف-۳۵ با ترکیه نهایی خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17651" target="_blank">📅 21:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17650">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد!
@withyashar</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/17650" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17649">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اگه بیرون میرین پاور بانک امشب فول شارژ همراهتون باشه
😁
کلا کاراتونو انجام بدید</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17649" target="_blank">📅 20:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17648">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">رسانه های داخلی : گزارشات از اصابت دو پرتابه به جزیره بوموسی
@withyashar</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/17648" target="_blank">📅 20:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17647">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نتانیاهو همکنون در حال حاضر در یک جلسه امنیتی با مقامات ارشد دستگاه‌های امنیتی است.
@withyashar</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/17647" target="_blank">📅 20:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17646">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2uwo_K8Q2_GpmEeE-CDRymeYpRJxasZg6iKP1OxjWyqY49qSY2ljWrfQBmy3eSWwJnGO_BksqAA_2k-I4M3KctHu5usgB-EJbCgxwAmu2tzORJ7xWSVOJwiegE5cpE4YryTXrIcEWEgXN7IY_EKrgWSOdBGzTGheHtexXKAnktZK44KvqHMUEgEgoGlfthL_Db2E9HEVVV1jhi7ZQsO3vgzy3mPe-BH0M1ZE1O3PK_k6HZcL6HLG5qNrj0XAttfXwWmZqIa1tpzYDthsIXNk6QVBu2wO2XJIG7fUbscmq-pvHCUPh2uWlprsDHKXtAWmKChZ_u_Ow6K-znqixGAyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ دستور داد تمام پرچم‌های ایالات متحده در ایالات متحده به مدت شش روز آینده به نشانه احترام به لیندزی گراهام به صورت نیمه برافراشته اهتزاز کنند:
به افتخار زندگی و دستاوردهای قابل توجه سناتور لیندزی گراهام، دوست عزیز من، و مردی واقعاً بزرگ که برای کشورمان و ایالت محبوبش کارولینای جنوبی دستاوردهای زیادی کسب کرد، دستور می‌دهم تمام پرچم‌های آمریکایی در سراسر ایالات متحده تا عصر جمعه ساعت ۶ بعد از ظهر پایین آورده شوند. خدای متعال تو را برکت دهد لیندزی.
@withyashar</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/17646" target="_blank">📅 20:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17645">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیویورک تایمز به نقل از یک مسئول آمریکایی : حملات آمریکایی که حدود یک ساعت پیش علیه ایران انجام شد، با هدف تضعیف توانایی تهران در حمله به کشتی‌های تجاری صورت گرفته است.
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17645" target="_blank">📅 20:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17644">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17644" target="_blank">📅 20:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17643">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وال استریت ژورنال یک ماه پیش در خبری مدعی شد: در صورت کشته شدن سربازان آمریکایی ترامپ پایان کامل مزاکره با ایران را بررسی خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17643" target="_blank">📅 20:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17642">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ولی خوب مشخصه دیگه امشب میترکونن
🫱🏼‍🫲🏽
😂</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17642" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17641">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">وقتی چیزی ننوشتم یعنی ترامپ چیزی‌ نگفته فیکه ! برو همونا رو دنبال کن  دایرکت منو سوراخ نکن  اه</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17641" target="_blank">📅 20:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اف بی آی به کمک پلیس محلی در پرونده مرگ لینزی گراهام ملحق شد.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17640" target="_blank">📅 20:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اعزام سه اسکادران جنگنده از انگلستان به منطقه خاورمیانه
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17639" target="_blank">📅 20:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17638">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">آکسیوس به نقل از یک مقام آمریکایی: ارتش آمریکا یک ساعت پیش به سامانه‌ های موشکی، پدافند هوایی و قایق‌های کوچک سپاه پاسداران در دو موقعیت در حوالی تنگه هرمز حمله کرد.
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17638" target="_blank">📅 20:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17637">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">منبع آمریکایی: حادثه امنیتی بسیار جدی در پایگاه آمریکایی در کویت پس از حمله ایران
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17637" target="_blank">📅 20:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gjJCW1-jI2iUafHqCe0IGZHFmOmgzPqNfmMwykASasDGoszwKq8gDnFjluQAhzrgv7gkEH0Nfg14L5-A6k4ZDHvaIvq8DKp58HzGyO2DGNmTE14aA1p-W6AtAyn3VVbpqbfvhWxh4EWfSFNYnSvvAegDvYjexvojVkh2EwmCVud4FDI9KJ-01Qem2c49lJ9Wj1mYQQL1JDEzgRmbIdKmuyd0WHhCxA_tZqLRbsQoP0EqQ78ErUdUbb_1KiYly_wL1YuRwQXylJof6I0TCTeVBZwhpbmhbOmlPqaAQNDM2LX1S-crXKNGV6kMimqt87ij2Cne7wA3b-dM4qiAM78fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس‌ها نشان می‌دهند که سناتور لیندزی گراهام در حالی که از محل سکونت خود بیرون برده می‌شد، که پرسنل اورژانس به او کمک‌های اولیه می رساندند.
@withyashar</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/17636" target="_blank">📅 20:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17635" target="_blank">📅 20:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17633">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGIe1W2rruVr4HTPb8odgEsDg6f9Vumo3jPVZyo7tFmHMmAzET92Nt1LUEno7rEWTz7jVu4snTLpM93X1YQ-KB3cNaipwqRA0kB8EO3F3J55KqanSzqVjRzwcgDZBrTqF4FSj4Pl9EgdW5xBqXQnw90kFSmKgxaLBG8xLeshDPRmmeNFAS6ExyWTA4XvyhCt1UBWXizQPD0wiauJ__--xAQwPIEoWRvfRg3yzBZcIzjyXEKLkg8r-fKnvYk-e4HFhyavq93mXkZ1LfuQVOmpo43Xe07Iouc2aqvp1tlrvKSi0JqvhlSMHxnDlL5lpAY_Z-n69kN5fa4lCQnWRbipUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون قشم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17633" target="_blank">📅 19:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17632">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SmczWbiiFOTj2uqfclHWXaJr7gzNREGn-cwkeRX8N2YSqrwDSkaBCGzuaXa5wiWG_YKGt9IPXMgzp5zh64IfKh2G2dLtyMuvENQt0AW_yCfV6JdHalwnB5LtLZ8aLtvszxe0wM4uwOig9wMBb2574-zAt0yYfG_8cEjYM9na92cAldNdT0yIhq5924HmHexYEfC57NyGm9Y97TCtD9NbWrckTLc6Fv1QHevEBsF-HUrg5BMrSMsB0mcifnpqLZdb-B4hP3cSjUxGoPY8jT-tTtLaEC4xlPkbcemAWVA-cKHqDffbTkK16yZCSJYiYIE7NaapZCfgrprjE2RD49PoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون چند انفجار جدید مِسِن در قشم ( مناره مسجدش تابلوعه تو ویدو هم دیده میشد )
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17632" target="_blank">📅 19:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17631">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رویترز:
12 مجروح آمریکایی که حال 2 تن از آنها بسیار وخیم است به پایگاه رامشتاین در آلمان منتقل شدن
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17631" target="_blank">📅 19:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17630">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش چند انفجار قشمممم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17630" target="_blank">📅 19:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17629">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان @withyashar</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/17629" target="_blank">📅 19:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17628">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45a1593a64.mp4?token=e1tWsr3gXkHNuj4kCs73sv2bnIU8Allp16CsUrc6t53s1B8wkKGbfH7OpssbNPLkXQqVQoumsDbbDyZVWdvaf3LPXcus2kE073zeRC7lcferEz7v2NuJ-8q9R27AotoRtag8v9JUWG6SEkyXAm-7eiBE-lDRL-gYFKbdC6q9jI8r-rWjAxx1hM5M6vk0HXKYPV3JRAi3SNQgEMvKtvehxGqUoOP72wNk-a8gXda3F5IBz0PYe1yNSvEfT5ysZm4QLmHP3jI7HMA4QY_4wBd1fnmd4KPFkYOkycMV3D9uy2NCeIsiOHM3QzXXQuNqEmZYa9xqvezUa4Z9ZLJkOJBbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون شهر مِسِن هرمزگان
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17628" target="_blank">📅 19:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17627">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تنگه بد دعوا شده…
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17627" target="_blank">📅 19:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17626">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیده شدن دود در آسمان قشم و بندرعباس
@withyashar</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17626" target="_blank">📅 19:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17625">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وزیر دفاع اسرائیل: به ارتش دستور آماده‌سازی برای عملیات مستقل علیه رژیم ایران داده شد.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17625" target="_blank">📅 19:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17623">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">رسانه های
عربی از کشته شدن سه سرباز آمریکایی و جراحت شدید تعدادی دیگر از سربازان خبر می دهند
.
@withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17623" target="_blank">📅 19:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17622">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عراقچی در دیدار با نماینده ویژه سازمان ملل در امور لبنان، بر ادامه حمایت از لبنان و تمامیت ارضی آن تاکید کرد.
@withyashar
🤡</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17622" target="_blank">📅 19:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17621">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امشب
🫱🏼‍🫲🏽
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17621" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17620">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری کویت :
رژیم ایران در یک حمله غافلگیرانه پایگاه آمریکایی رو مورد هدف قرار داد
بدلیل غافلگیری ۳ موشک پرتاب شده اصابت کردن
@withyashar</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/17620" target="_blank">📅 19:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17619">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گزارش شلیک موشک از یزد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17619" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17618">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارش شلیک جدید از قشمممم
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/17618" target="_blank">📅 19:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17617">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">رسانه های رژیم : ۵ لانچر از نوع هیمارس که درحال آماده سازی جهت حمله به خاک مقدس جمهوری اسلامی ایران بودند طی یک حمله پیش دستانه و غافلگیرانه توسط یگان موشکی هوافضای سپاه مورد اصابت ۴ فروند موشک فاتح ۱۱۰ قرار گرفتند.
همچنین در این حملات یگان پهپادی ارتش جمهوری اسلامی ایران با استفاده از پهپاد های آرش ۲ مسیر امداد رسانی و دستگاه های ارتباطی این پایگاه تازه تاسیس را مورد اصابت قرار داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/17617" target="_blank">📅 19:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17616">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم ! @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17616" target="_blank">📅 19:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17615">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/17615" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17614">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">مهر : شنیده‌ها از حمله موشکی جمهوری اسلامی به موقعیت یگان موشکی نیرو زمینی ارتش آمریکا در کویت می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17614" target="_blank">📅 18:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17613">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uU2jZl-MCUHtfaAEz_25pAEXpuMxzrZFsP0D7EsPbn6x_o5cFbVTg-bN0DcBXKVjPArVkqcjHx01o4kalmOJNTZ2GQA1Klt4WMZ8E7ZUih0bdB0qYYk5rLtpEgAKmQrSIPhqn5X60DVdrn5MdCjSDbLckMRwT7XKRwlzY8Tblga4TGyJAvYy_rtmZ_QJUY3vfj9utcCRC8X05Ado6t6TBKFWuAaW-xkyxpCRmmIZfPw_AnbRFuteSzeLtjo0Y8lHu6GBuN50sGhfDtxShtQ6DGNv2shrcWaUR2fkVstiYOk0A56jkYJw8Sk3OItYQ4nXTn5ZI4BryZkAWHpclnCHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون انفجار و ستون دود قشم !
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17613" target="_blank">📅 18:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17612">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۶ موشک یا پهپاد شلیک از قشم
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17612" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17611">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">سه انفجار یا شلیک پایگاه امام حسین بندرلنگه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17611" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17610">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨
تنگه دعوا شد
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17610" target="_blank">📅 18:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17609">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ارسالی : قشم درگهان یه دود غلیظ از وسط دریا مشخصه اطراف تنگه
@withyashar</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/17609" target="_blank">📅 18:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17608">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ5ushjrdrC37vCkKWjvKMHxOgkjpmLuOprGCMeYOOp2T69qGwHeEsFcR700AdlPn0Pxxuuw3Kp5hcMHnFEu-9mIqWED5hl10GRNWFJH5sxlX_kH5NKpusd420BWA2M-D6doW3CEZQWE_G8MMVzuzvyorPw1TG4lI7ER2IPzKoQ6S3LDA4OMGD3CJMgecr46Ip1PJL_XJJ9Ic0dQdftoKn65HuW_MT-Jd9oiztgbvLlCJDYNRC3S8XSseJwYtCyBbRVxQoG7tP2uekRutWXqrE1czubBt4U5eXiDTrlxLSwSNMZ_vNydkGGZh3ISyBrUkHQFKI1tGoWfkGYrtkPC9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه راکت بالستیک در حال حاضر برخورد کرده‌اند.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17608" target="_blank">📅 18:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17607">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">هدف قرار گرفتن محل‌های پرتاب موشک‌های ATCAMآمریکا
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/17607" target="_blank">📅 18:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17606">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارهایی در کویت رخ داد.
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/17606" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17605">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d44ac8d93.mp4?token=Id3sgJZaeTTv-ZWMIqoQjTjqFIurQvTRUCp3wcW1x20ZRG3PpCFR9b8-Q0aNmKNIUzofngPZtzapI4iMYXbWV8iXOg_Lbj58gtGkourJXMg4twWg_PCUH4rVer7kwNVNJRgYs4i5BgoKrn0tj9QCdQdYKylRFlm2Wxde7lshpX-YPvkY1jaKHnfR44sKIVo1U56V8O6qaPsXKBpRd9vCByxkiwxPWYtpOgd_s_hwOg6aX7pKOmbI9DyOE8642t9zTe660c4-ZXki4_UchAiqCt8rdZrVIWaynjoqaquYj8TqqErITTw9B9PMyiuDaAqgcxaXsNoUdk24fT5SAHT3GzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های مانوک خدابخشیان درباره‌ی سناتور لیندزی گراهام.
@withyashar</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/17605" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17604">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/facaf1d397.mp4?token=bE_axnCezWoyFulKdntgV8GhS3s_wNKybRknxj9i23mJ3Zk79pEIEA9k7Va0C5Zg0tkpaDiXMob6lLvg_cam_9gHUMqWcw516s8ceRwKWWbSQLZwSVAK6SJk335w_yRS7gzhl25UzbKeYU9UaNjLhIQAPzWBT-Iz3TigAfEg8ndj01Yy3cz57udyQ61LlJsUnXHKrhi9YYnIO-mg9-LYzUiURgOCV48acXcJJ01W3wn3MYZ-C7Tynyokk-1QD0sWXoz3fmQg-6-rGFbLgCS-l4Q1xjWt7r2vHlxSuMvgwJimbPx0vxyBeeVGg_Di4hKCcgMDaA6OlmzNByZOtRUoqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو درباره لیندسی گراهام:
شما کمیک‌های سوپرمن را به خاطر دارید: «حقیقت، عدالت و روش آمریکایی».
این لیندسی گراهام بود.
@withyashar</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/17604" target="_blank">📅 18:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17603">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0736854521.mp4?token=Ag6Cx1xx8ZMD8P2AK1tylphMks7wkqGkw38LSHBxeVOZKlbsZotNZMSutZrM-0bwf7B7hW3vVyPkjEgMEhmCZsU0lZy5gEr8s_4iJlG7kx4f6NWyclY6aF6_YdNp_WaomS790Teb7qqP6PGIW94aVqH00LEnj3d-D1nvPxJDz6gUeDdWyh7kXj4eWWW0tsgXcjpGV547ptZeOorF4BweDK_CvmRckAc7PBw9Jvz_jJB5ba3eSmX5mjrab8hL8vo8bMkeQrU6iomM4_Z4rqwHBtzyLNci2Q3KrUPi69QnVe5_Umnr0MI1avoCVOJBrHykXqxJM_wn9p5hwB1eNNRrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ درباره سناتور لیندسی گراهام:
«او سیاستمدار بزرگی بود. مردم نمی‌دانند که او چه سیاستمدار خوبی بود... احتمالاً هرگز نشنیده‌اید که من این را درباره کسی بگویم. تعدادشان خیلی زیاد نیست... این مرد سیاستمدار بزرگی بود. واقعاً حرفش را می‌فهمید.»
@withyashar</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/17603" target="_blank">📅 18:09 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
