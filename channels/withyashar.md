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
<img src="https://cdn4.telesco.pe/file/gXWM3fLObt5ePspFHClWkm199pIFyqwpoEsKqzrwaFXf3MUYw296b5NzIWAMwn9J4jNfFMy1INi3BR6eoi1eIRH3pWkUv_9-aGlO6LKEpZs3zMxOqa5XVp55DUXjcTkJA-sdqeje4ND2kisKzfC159xz8Ge0NKDEdDB-yGYWAtp8b8sRk1Dac4ffPSZGYQIj2hpfgPMeGiWUgB_5_oE922dLFhzgR5DgTtMXrMeK0OdkHg43IlWbL5jdXcs66Ml4TFEBVnOXqbKQsrbdxYswoqwKHBaLG7yFRr1NuztLyoUt-edrBXatV_yqNliiVcslkJZa4n_5ZQLtuyRU9EPcyQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 451K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 04:45:16</div>
<hr>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=MTBAPsDTR-6n_q_aCClY-o6OJEb3MG79U6sQ41x3kStivJy77-qaAaTOOh-b_E1BzWOmjy1WHxCwZAQLVD3VD3Unu0c73POuAWkbQvuY-XYlGpeTnGIbooOo4SLs1YhsboODJo26n6pYrvKlPp9NESomS2kn_WObZ4_0poW1-UH-wBVkgkhSxOaSgg60aZ0js-a2GS3xaxbzvPJ6p4PgjBahm48BTI0fKq5MMZgK2K4kiPAD2EMWwk4gPiUqom0lQnXr_eBYplmcAmmScT9Ow6IsyqP8WKQddeWQWGYjrPiLkQXwLbgk1HsGdvz9RCb-5TWu6Czh6_uRDnn1PD_Ehg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4a9d76473.mp4?token=MTBAPsDTR-6n_q_aCClY-o6OJEb3MG79U6sQ41x3kStivJy77-qaAaTOOh-b_E1BzWOmjy1WHxCwZAQLVD3VD3Unu0c73POuAWkbQvuY-XYlGpeTnGIbooOo4SLs1YhsboODJo26n6pYrvKlPp9NESomS2kn_WObZ4_0poW1-UH-wBVkgkhSxOaSgg60aZ0js-a2GS3xaxbzvPJ6p4PgjBahm48BTI0fKq5MMZgK2K4kiPAD2EMWwk4gPiUqom0lQnXr_eBYplmcAmmScT9Ow6IsyqP8WKQddeWQWGYjrPiLkQXwLbgk1HsGdvz9RCb-5TWu6Czh6_uRDnn1PD_Ehg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/withyashar/22754" target="_blank">📅 03:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromabas</strong></div>
<div class="tg-text">سلام
یاشار من عصری از خستگی و بی بازاری و کلافگی خوابم برد بازارم نرفتم خداگواه خواب دیدم. مانوک اومد تو خوابم. اصلا بهش فکر نکرده بودم ها. گفت فقط ۱۲روز دیگه صبر کنین</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/withyashar/22753" target="_blank">📅 03:53 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/withyashar/22752" target="_blank">📅 03:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/withyashar/22751" target="_blank">📅 03:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/withyashar/22750" target="_blank">📅 03:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/withyashar/22749" target="_blank">📅 03:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/withyashar/22748" target="_blank">📅 03:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">فنر رو بکشید !</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/withyashar/22747" target="_blank">📅 03:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22746">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دارم یه کارای میکنم از قلب واشنگتن دی سی ! تا کی‌تماشا ؟! خودم دست به کار میشم ! در چند روز آینده متوجه میشوید !</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/withyashar/22746" target="_blank">📅 03:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f949e07910.mp4?token=oBjlC2d4vJydIwQxBK5n9g-Zmw5HDywfxyIETqcR3KsapSqPl0zuu-zjlAXyxf9fbMBoPsoy_tTtlyzXK6VrS5C2bEfTIotHTV4Q3dWhsjvArkqd5Cc55xPoFZy1RhBNL6mm5FHYE46EsTT_3jInpr_i2Qc449FVYmLMVDZaK7iXw-3X0lV1HL1CBVtvAADn-X-C2D1pa1jtAK8HmSREzo6Gz7K7BFoCP3Ef37asm9UP1cqlUjCjt-UG5XLZarZdu1JVnEU4_v2XYgiu4DUB5ygZGkwIMqXQqGwqX9p-zRDAEX9hVhC7q7EXO2JsOyT7HXWDfLYO-ZKwdyHzCj3Srw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f949e07910.mp4?token=oBjlC2d4vJydIwQxBK5n9g-Zmw5HDywfxyIETqcR3KsapSqPl0zuu-zjlAXyxf9fbMBoPsoy_tTtlyzXK6VrS5C2bEfTIotHTV4Q3dWhsjvArkqd5Cc55xPoFZy1RhBNL6mm5FHYE46EsTT_3jInpr_i2Qc449FVYmLMVDZaK7iXw-3X0lV1HL1CBVtvAADn-X-C2D1pa1jtAK8HmSREzo6Gz7K7BFoCP3Ef37asm9UP1cqlUjCjt-UG5XLZarZdu1JVnEU4_v2XYgiu4DUB5ygZGkwIMqXQqGwqX9p-zRDAEX9hVhC7q7EXO2JsOyT7HXWDfLYO-ZKwdyHzCj3Srw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">راه فریدون فروخزاد و مانوک خدابخشیان را ادامه می‌دهم، نه کسی خرج من را می‌دهد، نه از کسی می‌ترسم.
@WarRoom</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/withyashar/22745" target="_blank">📅 02:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHECFApheHrkHumeQa3lJ-omRl5otfQp4CApIHPJ5WU455GRWz2zb41TNyHbrbkcNeq7OvzRLiDUjr5EVZCB8fGa619CWvxjcVzZgGftrkT7nsHiGG8digcmZYCtpehANlpfdLFoswunwjWYMx8Q7EKlF0Ni4YoaozFVUea-LEnEbo0HCDvzw7qu_JmvOpToEZZWq-wpkEIVgaYvEJe6HhD_4WYPy8vHhKsH-JYTB2JgHxDhpSPiD-ipj4fV1zKe2mOjaccePjcz3RS_vxESE9Wo2I1K3CIy3ZBln4_e0KpDytV0lMHRY7hyKNljVuzGPh6_OqSx8-zvJ6j3IB0p0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت محدودی خلیج فارس حاکی از ، همچنان در جریان بودن عملیات دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/withyashar/22744" target="_blank">📅 02:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22743">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آیت الله بی بی سی دقایقی پیش گزارش انفجار از میناب و سیریک گزارش‌کرد
@WarRoom</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/withyashar/22743" target="_blank">📅 02:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لازم می‌دونم یه چیزی رو کاملاً کلیر و واضح بگم. من، اگر امثالی مثل نادان لینو کس ، بهشت هم برن، من می‌رم جهنم مستقیم. خیالتون راحت باشه.
شما اگه جهنم رو هم انتخاب کنید من با مردمم و میام و بت نمیسازم از چیزی ، لطفاً به من دایرکت ندید که، امیدواریم که تو... تو زرد از آب در نیای. این اعصابم رو به هم می‌ریزه.</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/withyashar/22742" target="_blank">📅 02:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">علت اینکه سنتکام امشب حمله را اعلام نکرده فقط می‌تواند قیمت نفت باشد چون جامپ میزنه
@WarRoom</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/withyashar/22741" target="_blank">📅 02:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امشب بخوام نخوام بیدارم
🤣
😌</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/withyashar/22740" target="_blank">📅 02:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مهم اینه که بتونی ولی با مردم باشی وگرنه که عمه جان منم میتونه</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/withyashar/22739" target="_blank">📅 02:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22738">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b3484ab8c.mp4?token=dP0ryf7Hv3a_9wKwUhXAfLWRcaAB9BD07S5lwiDSYLWH1kqNZ8udD21oo_0z6cGJJzmN-6TJTt3H3zT9IiIQage83HkZYem1yDWZsY7BS6FxUUOcFRXpq03trl26oWPDmhx89azsmLjpdXU67s492bpl5XdM2ycmtKMAhZk2TYdjVPTWqD7gLi5OqGxqleTt_gDDNsv4xirH5TPJizuYSsj-siZpAxKC-kiBRYxxit2IaqggX-fgK58nnXDrSmu8JeAhVj12YUBiCqHiQ2oV4HBxb-MKZarB1PBIOqs3G4-3_onajV_CP7OofDMRveaCEoOwJm5rvxyEqI16sd_BoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b3484ab8c.mp4?token=dP0ryf7Hv3a_9wKwUhXAfLWRcaAB9BD07S5lwiDSYLWH1kqNZ8udD21oo_0z6cGJJzmN-6TJTt3H3zT9IiIQage83HkZYem1yDWZsY7BS6FxUUOcFRXpq03trl26oWPDmhx89azsmLjpdXU67s492bpl5XdM2ycmtKMAhZk2TYdjVPTWqD7gLi5OqGxqleTt_gDDNsv4xirH5TPJizuYSsj-siZpAxKC-kiBRYxxit2IaqggX-fgK58nnXDrSmu8JeAhVj12YUBiCqHiQ2oV4HBxb-MKZarB1PBIOqs3G4-3_onajV_CP7OofDMRveaCEoOwJm5rvxyEqI16sd_BoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/22738" target="_blank">📅 01:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">https://www.instagram.com/reel/DdFPOr5xRMu/?comment_id=18007178039969398
کامنت برای ترامپ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/withyashar/22737" target="_blank">📅 01:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شاید فیلم‌هاش بعدم بذارم. تاریخ ثبت بشه. ولی اگه بگم توی پنت که گم می‌شی دعوتم ، بیست نفر دارن می‌رقصن. من دارم برای خودم یه Grey Goose می‌زنم و اخبار جنگ می‌زنم ، فکر کنم با دمپایی بزنن تو سرم. حتماً مستندش رو بعد از آزادی می‌سازم.</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/22736" target="_blank">📅 01:52 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">منور زدن ، فک کنم آمریکا زده قایق های تند رو رو درو کنن  @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/withyashar/22735" target="_blank">📅 01:50 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZO4ahjTenez1KZiDuU-Xl_TCC-gwTNxhfQhrTsn9ywrHfNAC_flQV9xp6k8ZrOuZ97rYtzfwr9jRxovzGj8wKt2i61KSlV5l4jByi8kB-D3HztHjjcPc3lEwDcCmTB8DwrQwNy2vzS1y6CLxxujHF5HTyLNc-m9eFfbvY-MAn63r4UYh8c5kDXqSaouCBfU62-YKbX0tN8hSwYpAvB5Th6yg9mFla41hOHcBmiVw82Gf8tArNqQGCWe9eJn5iWhVxZPGBDPFa-MUcmhxqXSAQXP0bt8ESxeo13Z__26TmdCQ9wmHUi60uGPcmy9YuHErcw2YVNBoN4hqFGGDRr1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منور زدن ، فک کنم آمریکا زده قایق های تند رو رو درو کنن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/withyashar/22734" target="_blank">📅 01:49 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نفت یا ریال ؟ پیروز کیست ؟ کی تاب بیشتری داره ؟ نفت ۱۰۱،۲۱ $ و دلار ۲۳۵،۸۸۶ تومان !
@WarRoom</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/withyashar/22733" target="_blank">📅 01:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آمریکایی قایق تندرو جمهوری اسلامی را در نزدیکی سلامه هدف قرار داد و در آتش میسوزد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/withyashar/22732" target="_blank">📅 01:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چیزی نیست کابل فلت گوشیت خرابه ( بچه ها بهش نکین که EA-18G Growler بالا سرشه )</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/22731" target="_blank">📅 01:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSepehr</strong></div>
<div class="tg-text">یاشار سلام خوبی برادر
نمی دونم چی شد یهو گوشی تو قشم حالت پارازیتی مثل فیلما شد که صفحه بالا پایین میشه
😂
😂</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/withyashar/22730" target="_blank">📅 01:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هواپیما های جنگ الکترونیک آمریکا برای کور کردن رادار های احتمالی پرتیبل وارد عمل شدن درقشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/22729" target="_blank">📅 01:23 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22728">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سردار آزمون امروز در استوری صفحه اینستاگرام خود تصویری با پرچم جمهوری اسلامی و یکی کشته‌شدگان مدرسه میناب منتشر کرد.
پس از این روزنامه فرهیختگان نوشت: «مشکلات حضور سردار در تیم ملی برطرف شده و او قرار است در فیفادی پیش‌رو و در ادامه فرایند آماده‌سازی تیم ملی برای رقابت‌های جام ملت‌های آسیا قرار بگیرد
@WarRoom</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/withyashar/22728" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دکل سیریک حتما سر پا شده بوده
😌</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/22727" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری رژیم ایسنا : چند مکان در سیریک و زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/withyashar/22726" target="_blank">📅 01:09 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش پرتاب موشک از اصفهان
@WarRoom</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/22725" target="_blank">📅 01:07 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">درگیری‌امشب فک میکنم همه جانبه بشه حزب الله هم پهپاد زدن شمال اسرائیل
@WarRoom</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/22724" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22723">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ارسالی : یاشار داداش میناب در و پنجره خونه کاملا لرزید و احتمالا کرگان رو زده باشن
@WarRoom</div>
<div class="tg-footer">👁️ 82.7K · <a href="https://t.me/withyashar/22723" target="_blank">📅 01:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiTbO1ofB6BDtmMWyu-eaNxjPHwH3VRkOmdu-4l1BLlpyXxGm4FkKPqiATyUQGuTmOs2Df7WZE-7n3Zqote628ATVQYOiIq4QezKMNoNplor-cl_SQ6T1sqUrI4cO0FaS4V8y-apjtYaNTtFK9635qRYpFL4lj_nveHezJC7Ax8OKeP1WgkWs34wbNu55H06vwiY6Hvv1847NUfB7h2VJUFuFuJ5I0GfUf8b8js0TGNjy-1a7k_CZwArdNydQz_uU3A3RXQwMOpXBLv-KRKUF09Mi5cRyvairOV9y_2VYJRx_Sa42yLGYT722hjsABhB0agx2Yhh4_rMUgZxX4d9LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: یک فروند هواپیمای هشدار زودهنگام و کنترل هوابرد E-3 سنتری نیروی هوایی آمریکا بر فراز خاورمیانه توسط یک فروند سوخت‌رسان KC-135 استراتوتانکر سوخت‌گیری می‌شود. هواپیمای E-3 می‌تواند در منطقه‌ای وسیع، عملیات نیروهای هوایی و زمینی را هماهنگ کند.
@WarRoom</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/22722" target="_blank">📅 00:56 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">قشم گزارش شده به شرکت کشتی سازی‌هم زدند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/22721" target="_blank">📅 00:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بچه‌های بندرعباس لطفاً بیشتر گزارش بدین. عکس و فیلم اگه دارین، چیزی هست بفرستین.</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/withyashar/22720" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گویا قرارگاه طولا در قشم هدف حملات سنگینی قرار گرفته.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90K · <a href="https://t.me/withyashar/22719" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">صدا و سیما قشم رو تایید کرد صدای انفجار از قشم رو تایید کرد مال اونا نبوده
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92K · <a href="https://t.me/withyashar/22718" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">صدای انفجار بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/22717" target="_blank">📅 00:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22716">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">صدای دو انفجار مهیب گزارش شده که درو پنجره به شدت لرزیده…
@WarRoom
🚨
🚨</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/withyashar/22716" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مردم تاکید دارن که حمله شروع شده و پرتاب نیست !در انتظار تایید میمونم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 94.6K · <a href="https://t.me/withyashar/22715" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای پرتاب موشک از قشم
@WarRoom</div>
<div class="tg-footer">👁️ 94.3K · <a href="https://t.me/withyashar/22714" target="_blank">📅 00:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a5956945.mp4?token=qpPCefFwIi2DQBVjs-f9hnWTfr7mYq9DSWoc18kRf1xHE2VPMqvhtIVU0KOZPRPQI2KldE1EgD8zRg82FjTUbUryURYgTWQJ-PGOuNEuihE-H2hZRpsxm_ppQylo00P7KhzATQ_3zHXvhujSrfYVf_xQ35Ail2PyCCEeh7x2b9aLCOtcUT2r2u8WZCOgkn14XGfN3oASSryNqQdTnPFo8OAxfa8Orz2ryVRDVWnZQEZDiT0Rdk2halqtjelxdz1y75Z8oPCg1bsgXMDcGiIpbjKCoJ0ffwn2UEctCaqkTxXJp28TLMzmlgyyWlEgCA-VoWuH83GyCNuTn9lFPy_53oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a5956945.mp4?token=qpPCefFwIi2DQBVjs-f9hnWTfr7mYq9DSWoc18kRf1xHE2VPMqvhtIVU0KOZPRPQI2KldE1EgD8zRg82FjTUbUryURYgTWQJ-PGOuNEuihE-H2hZRpsxm_ppQylo00P7KhzATQ_3zHXvhujSrfYVf_xQ35Ail2PyCCEeh7x2b9aLCOtcUT2r2u8WZCOgkn14XGfN3oASSryNqQdTnPFo8OAxfa8Orz2ryVRDVWnZQEZDiT0Rdk2halqtjelxdz1y75Z8oPCg1bsgXMDcGiIpbjKCoJ0ffwn2UEctCaqkTxXJp28TLMzmlgyyWlEgCA-VoWuH83GyCNuTn9lFPy_53oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر خارجه آمریکا: ما معتقد نیستیم که هیچ کشوری بتواند چیزی به ایران بدهد که معادلات یا شرایطی را که شاهد آن هستیم تغییر دهد. در نهایت، آنها همچنان به کشتی‌های دریایی شلیک می‌کنند و وقتی به کشتی‌های ما شلیک می‌کنند، هزینه آن را با از دست دادن نفتکش‌هایشان می‌پردازند. آنها به کشتی‌های ما اصابت نمی‌کنند، اما پنج نفتکش خود را از دست می‌دهند. دیشب هم پنج نفتکش دیگر را از دست دادند؛ چهار نفتکش آسیب دیدند و یکی غرق شد. آنها به دلیل این کار همچنان
هزینه‌اش را پرداخت خواهند کرد
و ما نیز به اعمال فشار اقتصادی و خفه کردن اقتصاد آنها ادامه خواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/22713" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نخست‌وزیر نروژ: به هواپیمای زلنسکی حملۀ پهپادی شد
هواپیمای زلنسکی هنگام برخاستن از مولداوی به ‌سمت نروژ، هدف حملۀ پهپادی قرار گرفت و تا آستانۀ برخورد با یک پهپاد پیش رفت.
مقامات اوکراینی هنوز دراین‌باره اظهارنظر نکرده‌اند.
@WarRoom
یاشار : برخوردی صورت نگرفته</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/22712" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">@WarRoom
???!!</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/22711" target="_blank">📅 23:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">گزارش صدای انفجار/پرتاب در‌ سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/22710" target="_blank">📅 23:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فایننشال تایمز: ایران برای دور زدن تحریم‌ها به رمزارز روی آورده است؛ نزدیک به ۱۰ میلیارد دلار رمزارز در سال ۲۰۲۵ از مسیر ایران جابه‌جا شده است. همچنین ایران طی سال‌های گذشته از طریق استخراج بیت‌کوین نیز به درآمد رمزارزی دست یافته و برآوردها نشان می‌دهد حدود ۴.۵ درصد از کل استخراج بیت‌کوین جهان در ایران انجام می‌شود
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22709" target="_blank">📅 23:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">پست جدید ترامپ در تروث : ترامپ :
این رژیم به‌زودی خواهد فهمید که هیچ‌کس نباید قدرت و توان ایالات متحده را به چالش بکشد.
گوینده : او بار دیگر به جهان یادآوری کرد، همان‌طور که بارها و بارها گفته است، که آمریکایی بودن معنایی شکست‌ناپذیر دارد. اگر آمریکایی‌ها را بکشید، اگر در هر نقطه‌ای از زمین آمریکایی‌ها را تهدید کنید،
ما بدون عذرخواهی و بدون تردید به سراغتان خواهیم آمد و شما را خواهیم کشت.
ما این جنگ را آغاز نکردیم، اما تحت ریاست‌جمهوری ترامپ،
آن را به پایان خواهیم رساند.
جنگ آنها علیه آمریکایی‌ها، به انتقام ما تبدیل شده است.
ترامپ :
ای مردم سربلند ایران، ساعت آزادی شما فرا رسیده است.
زیرا ما آماده‌ایم دولت شما را به دست بگیریم.
این حکومت متعلق به شما خواهد بود که آن را به دست بگیرید
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22708" target="_blank">📅 23:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نوش…
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22707" target="_blank">📅 23:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ترامپ: [ایرانی‌ها] تمام تلاششان را می‌کنند تا روی نتیجه انتخابات ما اثر بگذارند، به این امید که یک گروه ضعیف روی کار بیاید تا کاری به کار آن‌ها نداشته باشد و بگذارد به سلاح هسته‌ای برسند
@WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22706" target="_blank">📅 22:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTc08oxpu9lmRxRCl3xkTf--XwJXvs8NoAI7JUVULiws2TfpGm7P2iUAmkOImTH-6rLBEW554zDtKbxuxzGGpaPKpgQiETIWyDy9Y8iSyasuHMMCKWYxi6WUiUBHSs6obaLHY644-2Cwt3gvzbCWJ99cC7qmXW73-wUICuq2HhXI-nNN3EAtb055kMTolz6yxlcSpCRkM0UrPqnl_PQRPGvXvfkN1PWiXM4P8aPyX6JpG9K2QLB4I0qltHf6WgNdsQOivaqO4dy_lADwtBYxsNC3AzxX3VZEUr_68Ldfq4_3Tu8erP0zUPAFtK-FCeU_JPPfdDT87_cmh2QEzqtwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید سفارت ایران :
سرآشپز رضا در حال پخت و پز است.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22705" target="_blank">📅 22:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b54a836c4.mp4?token=ok_Hs1Z0V1AAerO7W-hSORgfGuKXaJmrFHEWrjLhDT33hW1CwtkK3SBEYwqnsnST7f_wjMyf_qY_autoiJgE1WydZmn_mLSYhpvDUSK9DreSkrJozh5jpYV5BT0Ez6Ctusk3zKMPcCR2GRau9Am2bKo33zrgQHD82oSHdNYHy5PLrgf6uk-bjTgkKDiKNbejspuSz9lTRpf4IVLjGZnPnW0KK0vt-FwXSj6F_6kiRARBsvZ7RhSrycYwqVMFhdqi1_dcGUcUmubn1sjOJptfyWmTSuNlhvAuqc041B_McUWBxE_gdK_TjKEEx_Lb3vSuESc-VY1WBobx_D0luUEv7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b54a836c4.mp4?token=ok_Hs1Z0V1AAerO7W-hSORgfGuKXaJmrFHEWrjLhDT33hW1CwtkK3SBEYwqnsnST7f_wjMyf_qY_autoiJgE1WydZmn_mLSYhpvDUSK9DreSkrJozh5jpYV5BT0Ez6Ctusk3zKMPcCR2GRau9Am2bKo33zrgQHD82oSHdNYHy5PLrgf6uk-bjTgkKDiKNbejspuSz9lTRpf4IVLjGZnPnW0KK0vt-FwXSj6F_6kiRARBsvZ7RhSrycYwqVMFhdqi1_dcGUcUmubn1sjOJptfyWmTSuNlhvAuqc041B_McUWBxE_gdK_TjKEEx_Lb3vSuESc-VY1WBobx_D0luUEv7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: ما شاهد حملات زیادی در تنگه هرمز بوده‌ایم.
ترامپ: ۹ نفتکش ایران را نابود کردیم
این حملات توسط ما انجام می‌شوند. شما شاهد حملات بسیار بیشتری خواهید بود
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22704" target="_blank">📅 22:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ: چیز زیادی از کشور آن‌ها [ایران]باقی نمانده است. احتمال مذاکره وجود دارد، اما ما به دنبال آن نیستیم. جنگ پس از انتخابات میان‌دوره‌ای ایالات متحده پایان خواهد یافت.
وضعیت ایران بسیار وخیم است. کشورشان در حال حاضر درهم‌شکسته و نابسامان است؛ تورم ۳۰۰ درصدی دارند، ارزش پولشان از بین رفته و حتی حقوق سربازانشان را هم نمی‌پردازند. ما کنترل تنگه [هرمز] و بسیاری موارد دیگر را در دست داریم.
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/22703" target="_blank">📅 22:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ درباره ایران: «ما به دنبال توافق نیستیم. من در حال انجام کاری بسیار فراتر از یک توافق هسته‌ای هستم؛ مسائل زیادی روی میز قرار دارد.» ترامپ همچنین گفت جنگ با ایران «بلافاصله پس از انتخابات» پایان خواهد یافت @WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/22702" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ درباره ایران: «ما به دنبال توافق نیستیم. من در حال انجام کاری بسیار فراتر از یک توافق هسته‌ای هستم؛ مسائل زیادی روی میز قرار دارد.»
ترامپ همچنین گفت
جنگ با ایران «بلافاصله پس از انتخابات» پایان خواهد یافت
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/22701" target="_blank">📅 22:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره اوکراین: ما گفت‌وگوی بسیار خوبی با پوتین داشتیم. او می‌خواهد به توافق برسد. اگر زلنسکی هم بخواهد به توافق برسد، خیلی خوب خواهد بود
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/22700" target="_blank">📅 22:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22699">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خبرنگار: شما گفته بودید قیمت نفت و گاز کاهش پیدا خواهد کرد. اما قیمت نفت دوباره به بالای ۱۰۰ دلار رسیده است. این موضوع را چگونه برای مردم آمریکا توضیح می‌دهید؟ ترامپ: توضیحش برای مردم آمریکا خیلی ساده است؛ فقط کافی است بگویید: آیا اجازه می‌دهید ایران به سلاح…</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22699" target="_blank">📅 22:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e04575e679.mp4?token=Jk5fZf2PUcbjLVIZYnLNtxomufX2-y_X3OsZWdCnW3_EGObOqwbZybIxIzFeb6bqqq5MLcGdbwD5orTCTHtM5M3jy3U58X5fwtNRb7ZlYx126bddf1U-n4V4hw10-h0dBKjfUrUEoZPoPE5f9MmRoLG32ebs2f4-XEZ9nSXBozy_9S1sEakGBfvUk1NrWJjVDWUJmRisGGi4hlH7yK-9LZhYWmV_AdWEhpvKzZKGpgPWR3LJSiy2Zj0gg_FmWl0ZA5-PRd3A4eKXsK-1ms6cJPXfck34ik8mRtBduQGwdY41CroxpeHuhQIaljugXo_XBPt2eo1Z8uqbJpo4oKqLUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e04575e679.mp4?token=Jk5fZf2PUcbjLVIZYnLNtxomufX2-y_X3OsZWdCnW3_EGObOqwbZybIxIzFeb6bqqq5MLcGdbwD5orTCTHtM5M3jy3U58X5fwtNRb7ZlYx126bddf1U-n4V4hw10-h0dBKjfUrUEoZPoPE5f9MmRoLG32ebs2f4-XEZ9nSXBozy_9S1sEakGBfvUk1NrWJjVDWUJmRisGGi4hlH7yK-9LZhYWmV_AdWEhpvKzZKGpgPWR3LJSiy2Zj0gg_FmWl0ZA5-PRd3A4eKXsK-1ms6cJPXfck34ik8mRtBduQGwdY41CroxpeHuhQIaljugXo_XBPt2eo1Z8uqbJpo4oKqLUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید قیمت نفت و گاز کاهش پیدا خواهد کرد. اما قیمت نفت دوباره به بالای ۱۰۰ دلار رسیده است. این موضوع را چگونه برای مردم آمریکا توضیح می‌دهید؟
ترامپ: توضیحش برای مردم آمریکا خیلی ساده است؛ فقط کافی است بگویید: آیا اجازه می‌دهید ایران به سلاح هسته‌ای دست پیدا کند؟ پاسخ «نه» است
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/22698" target="_blank">📅 22:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d8e57fc1.mp4?token=v6neCmKvFlrVxee_LwJQvkEEg6Ry6lvR-UT_2yUB5WFh2VErbgFG8kziKVl_yJuRqgwpp8zbGaFHm7K5gFjs-W2HYZ6B3XtGH61pr5KzoEci8TV7ajcfLCMcRzKr-auDb5YuxrVp1FbR5szFC27C6PYqBk6egn6obUP2JUyV_NjKTdod3JtqJFbMCYo75IAmWbC0kMR6D-IWZyQIloyAu5FfPqteHIqT4DpS6rHRZ9FXeOhpdWNZeU9R02--Oo3vlvQM2BpEyK5arrB2k26XPYEaDoV0uZjgzIZ2kMMEKAWh5n6lZXNoa-O5GwFskcjORK-X04_Dbduo3My-D52Uhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d8e57fc1.mp4?token=v6neCmKvFlrVxee_LwJQvkEEg6Ry6lvR-UT_2yUB5WFh2VErbgFG8kziKVl_yJuRqgwpp8zbGaFHm7K5gFjs-W2HYZ6B3XtGH61pr5KzoEci8TV7ajcfLCMcRzKr-auDb5YuxrVp1FbR5szFC27C6PYqBk6egn6obUP2JUyV_NjKTdod3JtqJFbMCYo75IAmWbC0kMR6D-IWZyQIloyAu5FfPqteHIqT4DpS6rHRZ9FXeOhpdWNZeU9R02--Oo3vlvQM2BpEyK5arrB2k26XPYEaDoV0uZjgzIZ2kMMEKAWh5n6lZXNoa-O5GwFskcjORK-X04_Dbduo3My-D52Uhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آیفون تاشو و سنت‌شکن اپل با نام دوو «Duo» رونمایی شد. شروع قیمت از دو هزار دلار تا سه هزار دلار بسته به گیگ ، امکاناتی همانند استفاده از دو آیفون به شما میدهد. میتوانید چند اپلیکیشن را همزمان باز کنید و … تاریخ عرضه یکم آبان.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22697" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">کانال۱۲ اسرائیل : اسرائیل تصمیم گرفته است که به هر حمله موشکی جمهوری اسلامی حتی اگر به اشتباه از مرزهای اردن عبور کند، پاسخ دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/22696" target="_blank">📅 21:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22695">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دلار ۲۳۵،۲۰۰ (سقف تاریخی)
تتر ۲۳۴،۴۰۰(سقف تاریخی)
@WarRoom</div>
<div class="tg-footer">👁️ 111K · <a href="https://t.me/withyashar/22695" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هم اکنون برگزاری جلسه اضطراری در کاخ سفید درباره ایران
به گفته خبرنگار ارشد کاخ سفید:
ترامپ در اتاق جنگ کاخ سفید حضور دارد و دیرتر از موعد مقرر به سمت دالاس، ایالت تگزاس، حرکت خواهد کرد، به گزارش‌ها، ترامپ در حال حاضر در حال دریافت گزارش‌های اطلاعاتی درباره ایران است و وزیر جنگ و رئیس ستاد کل ارتش آمریکا نیز وارد جلسه اضطراری با ترامپ شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22694" target="_blank">📅 21:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بنیاد دفاع از دموکراسی‌ها FDD
:
ایران پریشب با سه پهپاد یکی از اردوگاه‌های حزب «کومله زحمتکشان کردستان» در منطقه سورداش، استان سلیمانیه عراق، حمله کرد. در این حمله کسی کشته یا زخمی نشد، اما به یکی از ساختمان‌ها آسیب وارد شد. کومله اعلام کرده از آغاز درگیری ایران و آمریکا، مقرها و اردوگاه‌هایش بیش از
۱۰۸ بار
هدف موشک و پهپاد قرار گرفته‌اند؛ حزب دموکرات کردستان ایران نیز از
۱۵۵ حمله
و بیش از
۳۰ کشته
خبر داده است. این حملات در حالی ادامه دارد که آمریکا در حال خروج نیروهای خود از عراق است و بغداد اعلام کرده تا
۳۰ سپتامبر
نیروهای ائتلاف و سامانه‌های پدافندی آمریکا از عراق خارج خواهند شد. هم‌زمان عراق برای خلع سلاح گروه‌های مسلح مورد حمایت ایران مذاکره می‌کند، اما برخی از این گروه‌ها با خلع سلاح کامل مخالفت کرده‌اند. در صورت خروج آمریکا و ادامه حملات ایران می‌تواند
شکاف امنیتی گسترده‌تری در اقلیم کردستان و منطقه ایجاد کند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22693" target="_blank">📅 20:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گزارش صدای انفجار جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/22692" target="_blank">📅 20:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بلومبرگ به نقل از یک مقام ارشد ایرانی گزارش داد تهران در صورت ادامه حملات آمریکا به خاک و زیرساخت‌های ایران،
پاسخ خود را تشدید خواهد کرد
و برای یک درگیری طولانی‌تر آماده است.
این مقام گفت ایران با وجود فشارهای اقتصادی فزاینده، محاصره دریایی آمریکا و حملات به نفتکش‌های ایرانی،
قصد عقب‌نشینی ندارد
و درگیری کنونی را تهدیدی موجودیتی برای جمهوری اسلامی می‌داند. به گفته او، ایران از زمان پایان شدیدترین مرحله جنگ در ماه آوریل، در حال
بازسازی توان نظامی خود
بوده و خود را برای ادامه یک جنگ فرسایشی آماده کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22691" target="_blank">📅 20:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به شورای امنیت ارجاع داد
شورای حکام آژانس بین‌المللی انرژی اتمی پرونده هسته‌ای ایران را به بهانه آن چیزی که نقض تعهدات توصیف کرده، به شورای امنیت سازمان ملل ارجاع داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22690" target="_blank">📅 20:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بیانیه مشترک ایران، روسیه و چین:  از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22689" target="_blank">📅 20:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیانیه مشترک ایران، روسیه و چین:
از اعضای شورای حکام آژانس اتمی می‌خواهیم به پیش‌نویس قطعنامه آمریکایی-اروپایی رأی ندهند
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/22688" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گویا جاسک دوبار نفتکش زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/22687" target="_blank">📅 19:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گزارش صدای انفجار جاسک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22686" target="_blank">📅 19:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkI8BAQV1lz4TU59VNwivc-agJteHvjJoB4skegn5TW22195GF-mYk7PjT8QupNS2a3Lx60s9lK3ox-so6x6vKl2Z08Rt9G9zdEUXnhZ04Jbid7Lb8f1xOJxbciCl65nVV4Y_TEPCyQHABinIG6RjzVd4JRX8FeyYtSP4KjP8SuemD8kt4fk_vLST0qMd_VhAoEjcHzGOV6rKP0qxnIdr1WJ95D4Zgp7RswKqOOKk7_jIgxrSJHkYnLVPMdmO4inIZi3BBGvDXJe1zoBuLusGyfVbHDQaCLwPOUqGblGIGu4B_2Td91MKjzaQ4a_FCXBS23JCVznIPFdUmT1Wf4FjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتاق جنگ با یاشار : شهپادی که سپاه چندین سال به دنبالش بود و یک بار ۴ سال پیش اقدام به سرقت کرد ولی ناموفق ماند، توسط دیدبان اتاق جنگ شکار شد.
این یک شناور سطحیِ بدون‌سرنشین از نوع «Saildrone Explorer» است که شرکت آمریکایی سیل‌درون آن را طراحی و تولید کرده است. این شناور حدود ۷ متر طول دارد و با استفاده از یک بالِ سختِ بادبانی حرکت می‌کند؛ انرژی دوربین‌ها، حسگرها، سامانه ناوبری و ارتباطات ماهواره‌ای آن نیز از پنل‌های خورشیدی روی عرشه تأمین می‌شود. سیلدرون اکسپلورر برای مأموریت‌های طولانی‌مدت طراحی شده و می‌تواند ماه‌ها بدون خدمه در دریا باقی بماند. این شناور به دوربین، رادار، حسگرهای هواشناسی و اقیانوس‌شناسی، تجهیزات پایش سطح و زیر سطح آب و سامانه کنترل از راه دور مجهز است و داده‌ها و تصاویر را از طریق ارتباطات ماهواره‌ای به مرکز فرماندهی ارسال می‌کند. ناوگان پنجم آمریکا از سال ۲۰۲۲ استفاده از این شناورها را در خلیج فارس آغاز کرد؛ مأموریت اعلامی آن‌ها افزایش آگاهی دریایی، پایش تردد شناورها، جمع‌آوری اطلاعات محیطی و شناسایی فعالیت‌های دریایی در منطقه است. این شناور پیش‌تر نیز در خلیج فارس خبرساز شده بود؛ آمریکا اعلام کرد در
۲۹ اوت ۲۰۲۲، شناور پشتیبانی «شهید بازیار» متعلق به نیروی دریایی سپاه به یک فروند Saildrone Explorer متصل شد و آن را یدک کشید. طبق روایت آمریکا، پس از نزدیک‌شدن شناور و بالگردهای آمریکایی و چند ساعت پیگیری، طناب یدک‌کشی جدا شد و شناور بدون‌سرنشین رها شد؛ حادثه بدون درگیری نظامی پایان یافت.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22684" target="_blank">📅 19:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیدبان اتاق جنگ وسط تنگه هرمز شکار کرده
🤣
خبر تا دقایقی دیگر ….
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/22683" target="_blank">📅 18:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22682">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">آکسیوس گزارش داده بسیاری از جمهوری‌خواهان و دستیاران کاخ سفید، با وجود تردید فزاینده درباره تصمیم‌های سیاسی ترامپ، عملاً از تلاش برای تغییر نظر او دست کشیده‌اند و ترجیح می‌دهند از خواسته‌هایش پیروی کنند. یک مشاور قدیمی گفته است: «چرا زحمت بکشیم؟ رئیس اوست.» با نزدیک شدن به انتخابات میان‌دوره‌ای، نگرانی جمهوری‌خواهان از رویارویی با ترامپ بیشتر شده است؛ یک اهداکننده جمهوری‌خواه این وضعیت را چنین خلاصه کرده: «هرچه بخواهد، به دست می‌آورد.» در همین حال، نزدیکان ترامپ معتقدند نباید منتظر کاهش نفوذ او بود و هشدار داده‌اند که
حتی پس از پایان دوره ریاست‌جمهوری‌اش، ترامپ همچنان یک شخصیت سیاسی غالب باقی خواهد ماند
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22682" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22681">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتانیاهو: در آستانه سال نو یهودی «روش هشانا» در ارتفاعات جبل‌الشیخ هستیم. پایینِ سرِ ما دمشق قرار دارد، اینجا لبنان است و آنجا بلندی‌های جولان. ما بر تمام این منطقه، از جبل‌الشیخ تا رود یرموک و از اینجا تا دریای مدیترانه، کنترل داریم؛ این سطح از کنترل کامل، بی‌سابقه است. این یکی از دستاوردهای بزرگ ماست. هنوز کارهایی باقی مانده است؛
مأموریت اصلی، شکست دادن جمهوری اسلامی در ایران است و ما به آن بسیار نزدیک شده‌ایم
. ما می‌دانیم که در نهایت تمام محور سقوط خواهد کرد. ما برای انجام این کار متعهد هستیم و آن را انجام خواهیم داد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22681" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22680">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رویترز گزارش داد نفتکش سوخت‌رسان «Hercules Star» با پرچم جبل‌الطارق، در فاصله حدود ۱۷ مایل دریایی شمال‌غربی بندر میناء صقر در رأس‌الخیمه هدف یک پرتابه قرار گرفت و دچار آتش‌سوزی شد. آتش‌سوزی مهار شد و نفتکش سپس به لنگرگاه دبی بازگشت؛ خدمه این کشتی سالم گزارش شدند.
همچنین گزارش شده است که نفتکش «MKD Vyom» در آب‌های نزدیک عمان هدف قرار گرفت و
یک خدمه آن کشته شد
.
@WarRoom
یاشار : در خبر رویترز «یک کشته» مربوط به MKD Vyom است و نه هرکولس استار،  در تمام رسانه ها به اشتباه منعکس شده
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22680" target="_blank">📅 16:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22679">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ارم‌نیوز ‌امارات گزارش داده است که آمریکا در حال بررسی طرحی برای استقرار تفنگداران دریایی در برخی جزایر خالی از سکنه ایران در اطراف تنگه هرمز است. بر اساس این گزارش، در صورت اجرای طرح، جنگنده‌های F-35B مستقر روی ناو تریپولی وظیفه پشتیبانی هوایی از نیروهای آمریکایی را بر عهده خواهند داشت.
هدف احتمالی این طرح، ایجاد نقاط دیده‌بانی و پایگاه‌های لجستیکی برای نظارت بر تنگه هرمز و حفاظت از کشتی‌های تجاری عنوان شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22679" target="_blank">📅 16:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22678">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqhIkbU8Rj8MPym_FLwt3Wx8eL0Cbz60UwC40noaSUT6P6BJA7hyV92aFOJMVzSp4DJLkb2TRgev36LWEj3j9riMDiaaIfx40k5C3PDosXtsCnaG5p5LgR5RWN_RypvYgCTbloqJ_gCCb28YP-x2Li12vOwuf2pEXas-kU7ctj5b1-FL7tIPzmFYP3v9s0XfSSZDakDsqe2vhJEtIJc7XhAYcAZUWE9cPBzToA-_u8pwmOVLDMSazNAWUaXGP3ovo6g1Y0IglQ8LVPIdXYNM8Z3Dxjmjn8jrC076tXPuV0-xZjf5nBDYqsH0dkPO8BXN-eS-IKNg0wdV5ov1r39cMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه ایران، ۱۱
شهریور ۱۳۸۲
@Warroom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22678" target="_blank">📅 16:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22677">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvFlZCkJJ7TxKL32Y3NMFMPZArniYDIQdu_67N723_EcmUpjc43LpJ9R2KcKrmRySCVfob5uPPuNQ9Pj1KY_vbUHt2aebSew-KDVhDaz3TiQVIFqXHIAKiUSCFCCJQL5-Ag2kjb5-oRn_hf9wZUjNhsiSfd6QYS_AYKrGvIhU1UP98hsJa27BRZCpce23em-JMjtq14wFObU3eMsoioI60mPhr5AhrO90JE4XRw_F8Zj9YMJuyOj1DvFQHgXN_XE_tuYyz096tuQRlj7DTQAYeztMaDRPKNRAlWZw8qW_jb7kCEJZBPOYFzc6rCFBiKDybnHakTSJTw-P-afYczJIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو رعدنیاهو دیشب در آسمان تهران کلی بچه ها رو ترسوند
😁
@WarRoon</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22677" target="_blank">📅 15:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22676">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9f7b7cff.mp4?token=LrnwmJXvinObvwroBcha4JSFTU_jSWBPm8BEZ5J_XPZab5zcORlrq4QJdFYmtl6uwzpNpbwMzhFxGSV4pOrRg5M27uyrV_QTX5uYPLgZR1DwwzgRNUMq4yBYI1FRt0wS30bIeiwJNYeYN4nAiNCC76KkiLXwGtcag8uI1TbJgsxyLNbVwm_c6MoYEjWvDw-D01gDupHc3C9L0igH3Uq4-uykR1j9Eu5v0wiTdvTeBbwUtivHVDM2maNr1FzCC4WhxDLGyMjMW6Q56X-DILhxgQY_6oLFoFMxdmIfBemkRMvOS91pVGuQ4Xt11AiMNwaG7z68IAp2XGK0LNnIb4Gn6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9f7b7cff.mp4?token=LrnwmJXvinObvwroBcha4JSFTU_jSWBPm8BEZ5J_XPZab5zcORlrq4QJdFYmtl6uwzpNpbwMzhFxGSV4pOrRg5M27uyrV_QTX5uYPLgZR1DwwzgRNUMq4yBYI1FRt0wS30bIeiwJNYeYN4nAiNCC76KkiLXwGtcag8uI1TbJgsxyLNbVwm_c6MoYEjWvDw-D01gDupHc3C9L0igH3Uq4-uykR1j9Eu5v0wiTdvTeBbwUtivHVDM2maNr1FzCC4WhxDLGyMjMW6Q56X-DILhxgQY_6oLFoFMxdmIfBemkRMvOS91pVGuQ4Xt11AiMNwaG7z68IAp2XGK0LNnIb4Gn6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در فیلم جدیدی که کانال چهارده از حملات دیشب به اردن منتشر کرده، در ثانیه اول واضح است که پدافند آمریکایی پر قدرت عمل کرده و «موشک قدر» جمهوری اسلامی را منهدم می‌کند و ذراتی که پخش می‌شود حاصل این مهار است و موشک خوشه‌ای در کار نبوده.
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22676" target="_blank">📅 15:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22675">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6GjzhNzchxKpvIT0E4EzFMTLoT2zJMY9JAD9asdmctwFHQ4ww-S6Z2nx6P2SISWuNmiUNQwXgQMNY7vX-hKDDwN49k9l8nALwKrJiQ-2JFZQDD-U3OVukbMCqAJJBWpNR5LIkSqfKE_L96wn4Ix3RkMi2y24p1bBxONIXUxiASH3seUGVw6gWsynZ5H4dOXvTROw3laeKLcu_ft9wl_p7JAMrIgw01ia140pOW-3q50nAXGifm2mWZsRmaPgxnr1ov9MUYykx5obRn6MZEf5KhyvpAPAVAck_2QYBlxR_O1TMfFtBprKj-Z01xdoPFPlbIqBuCJgTu_e3h7UpmdoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان به ترامپ : ۷ میلیارد دلار سلاح‌ها آمریکایی بجا مانده اکنون متعلق به افغانستان هستند و ما آن‌ها را پس نخواهیم داد.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22675" target="_blank">📅 15:30 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22674">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یک مقام آمریکایی:
تمام نیروهای آمریکایی در خاورمیانه در حالت آماده‌باش کامل قرار دارند، پس از حمله شب گذشته ایران ,
ما همه منتظر دستورات رئیس‌جمهور هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22674" target="_blank">📅 15:24 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22673">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سی‌ان‌ان: تصاویر ماهواره‌ای از افزایش چشمگیر ساخت‌وساز در سایت به‌شدت مخفی «کوه کلنگ گزلا» در نزدیکی نطنز خبر می‌دهد؛ محلی که ممکن است به تأسیسات غنی‌سازی اورانیوم یا یک مرکز امن هسته‌ای تبدیل شده باشد @WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22673" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22672">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سخنگوی سپاه: ناو هواپیمابر آمریکا را در فاصله ۵۰۰ کیلومتری هدف قرار دادیم
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22672" target="_blank">📅 15:18 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22671">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">شروط جدید جمهوری اسلامی برای توقف جنگ اعلام شد
سخنگوی سپاه: اگر دشمن خواهان پایان این وضعیت است، باید:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش رژیم صهیونیستی از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22671" target="_blank">📅 15:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22670">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۱۰ دقیقه پیش چندین گزارش داشتم از‌صدای انفجار‌ از تنگه
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22670" target="_blank">📅 14:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22669">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حداد عادل بود نه لاریجانی
😁</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22669" target="_blank">📅 14:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22668">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHBjBAwDx8boJPhFMl7LUhURzKFWJCVOlEGGHuzcEy69RGTgIVPYyDQT0HVT_0mVjy5xXracOTkDpy6YC2F5Hvzko2WcoyvlcDFI1tUoSXDxwC7T9lg_sz9PayLlJQju1UmtH15KsKysSX7X8IOFGwX-fMqyP53kNmLuQdAx8VCVRtSUEM3AZOBvh18b7hB_HCvO_nRvljmdy4YizINu0i9QzsJpHQJfHDTo_6d1xf070s0BcU38qHVIprk2I7iBXOoxhSyP26YNQLrXjcrtO2_9q1nd0aFMWwbHr1963InfivklDaEraNGMHx5ofTVVf0Kx8PPZ1Yl4NnyyT4RPQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان تجارت دریای بریتانیا UKMTO: گزارشی از وقوع یک حادثه در ۲۸ مایلی دریایی جنوب‌شرقی الفاو عراق در فاصله‌ای نزدیک از آب‌های کویت دریافت کرده است. ناخدای یک نفتکش اعلام کرده که شناور با یک پرتابه ناشناس مورد اصابت قرار گرفته است. خدمه در سلامت هستند
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22668" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22667">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXns4UxRFEZvzW-RmfPk1dpfeo0hIi4Fc3PFujk5D_oR4q5o7C-1xBd-LSZJIrfnOG2o56zEgj-92KYauu5WPh7IwZZ7vgwCHjfLlch98_oDtXLE041OuDjHs9c6zpV296ZrtFD8Jn3d1eZ2w4o1VQnN_kFzhX1KIQj5RKbRRA9oK1Qo6aTcULeVrz3X-L-pbdc6Ozbx-K2wPJlsLWjB0-IiKhBt_wVBxjQqMevm21dgo0qmcHc0CDhvTRgPSm-YJJrLPiqEz_5PCOKmWLzikCD548p-_xB7s5YqiUC2NmdSnySVBUf133fTIkzp9VUebrVljiAhrWYvgnjroZn8kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: تصاویر ماهواره‌ای از افزایش چشمگیر ساخت‌وساز در سایت به‌شدت مخفی «کوه کلنگ گزلا» در نزدیکی نطنز خبر می‌دهد؛ محلی که ممکن است به تأسیسات غنی‌سازی اورانیوم یا یک مرکز امن هسته‌ای تبدیل شده باشد
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/22667" target="_blank">📅 14:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22666">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">العربیه : نیروهای مسلح یمن رسماً اعلام کردند که طی عملیات اخیر خود، تعدادی از سرکردگان شبه‌نظامیان حوثی، از جمله طراحان اصلی حمله به تنگه استراتژیک «باب‌المندب» را کشته و شماری دیگر را به اسارت درآورده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/22666" target="_blank">📅 14:16 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22665">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کانال ۱۴ اسرائیل در یک افشاگری ، مدعی شده قالیباف در یک جلسه غیرعلنی گفته تحریم‌های آمریکا اثرگذار بوده و خسارات ناشی از جنگ تقریباً جبران‌ناپذیر است و گفته «جمهوری اسلامی در آستانه فروپاشی است». بر اساس این ادعا، قالیباف همچمین اضافه کرده: «همه ما میلیاردها دلار دزدیده‌ایم، اما دیگر نمی‌توانیم مردم را برای مدت زیادی کنترل کنیم.» او همچنین از رویکرد تندروانه احمد وحیدی، فرمانده سپاه، انتقاد کرده و گفته «پافشاری و رویکرد او، ایران را به خطر انداخته».
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/22665" target="_blank">📅 13:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22663">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حقیقت یاب سنتکام : هیچ ناو جنگی نیروی دریایی آمریکا مورد اصابت قرار نگرفته است؛ تمام حملات تلاش‌شده از سوی سپاه شکست خورده‌اند. در همین حال، نیروهای آمریکایی تنها در هفته گذشته با موفقیت
۱۰ نفتکش ایرانی
را منهدم کرده‌اند. این شناورها بخشی از یک شبکه چندمیلیارددلاری موسوم به «ناوگان سایه» بودند که برای تأمین مالی سپاه پاسداران فعالیت می‌کرد و ایران قادر به دفاع از آنها نیست
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/22663" target="_blank">📅 13:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22662">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">یک مقام آمریکایی به الجزیره:
پاسخ ایران در برابر پدافند هوایی و موشکی یکپارچه ناکارآمد بود.
موشک‌های شلیک شده توسط ایران به سمت اردن منجر به تلفات جانی در میان نیروهای آمریکایی نشد.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22662" target="_blank">📅 13:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22661">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دلار ۲۳۲،۱۰۰ تومان (سقف تاریخی)
بازار آزاد ۲۳۶-۲۳۸ هزار تومان
تتر ۲۳۱،۰۰۰ تومان(سقف تاریخی)
نفت برنت ۱۰۰.۴۰$
انس جهانی طلا ۴،۳۹۸$
۱ ظهر تهران
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/22661" target="_blank">📅 13:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22660">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22660" target="_blank">📅 12:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22659">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رویترز گزارش داده بنیامین نتانیاهو در آستانه مهلت ثبت فهرست‌های انتخاباتی، برای متحدکردن احزاب راست‌گرا تلاش می‌کند. انتخابات پارلمانی اسرائیل قرار است ۲۷ اکتبر (۵آبان)برگزار شود
@WarRoom</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/22659" target="_blank">📅 12:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22658">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igZltiGG4BtkwU40FfdmzETN6SV-IxeYnVO-TxgsVx8ssM9zukA-WQfr9608RmmSUIXfh9EIUM0zy2og0YQX8vtCFX01WeTD47RwpuD4Q3sPMAzF8X_lT21dRxO31CzbsnXPK20HAumveovHnmkv20RT7RQsuVS_AOGsGRlSq-y1E3US16Z-t98YLdYr4QEWxJVhyLdKhsfTWjvYKs4l7Zq_Fnjh3gmDpGcBwUSvBqUqWHdn7jCFQQ2lpS_GjK-MwdRVS71fcvzQFN40EJQ9DwklGCZ4lf97jMkwa4GZVjPBLDdvmKkQuWQ20S3a1eKkv2MbACYJ8t8gU0uiI1fEXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریایی بریتانیا (UKMTO) با تاخیر گزارشهایی از چندین مورد کشتی تجاری در شمال خلیج فارس و خلیج عمان دریافت کرده است.
گزارش‌ها حاکی از آن است که این کشتی‌ها به عنوان بخشی از فعالیت‌های نظامی دیشب در منطقه، هدف آتش‌سوزی قرار گرفته‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/22658" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22657">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رویترز گزارش داده هزینه بیمه و ریسک جنگ برای نفتکش‌هایی که از هرمز عبور می‌کنند به‌شدت افزایش یافته و هزینه بیمه جنگی در برخی موارد به حدود ۶ درصد ارزش محموله رسیده است؛ موضوعی که باعث شده برخی شرکت‌ها از عبور از این مسیر صرف‌نظر کنند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/22657" target="_blank">📅 12:08 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22656">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آسوشیتدپرس گزارش داده ایران در حال شکل‌دهی به شبکه‌ای تازه از گروه‌های نیابتی، به‌ویژه حوثی‌های یمن و گروه‌های مسلح عراقی، برای افزایش فشار بر متحدان آمریکا در خلیج فارس است. بر اساس این گزارش، نشانه‌هایی از هماهنگی میان حوثی‌ها و گروه‌های عراقی دیده شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/22656" target="_blank">📅 11:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22655">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">دلار ۲۳۰،۱۰۰ تومان (نرخ تاریخی)
بازار آزاد ۲۳۵-۲۳۷ هزار تومان
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/22655" target="_blank">📅 11:46 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22654">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=p8wQFUweU6ywSjrD8LjOX0l4IyWWOVKYtkM2v_cpmiEHVYhBN_aKebftNc6UWOiyfgRo4u0zIkahwCpxnkn1d2JZMB3bT7Ot2ZwoiHSH8rCT_adN1V49Vyht-pUpFkCtk3YZzSAjyFYzrn9GNBxTbJez_BySUpyNYCF43UbmmHZqtjSEYxZhsZIPdF-4aLL2QKxAgGSW4w6YggUg5ugkcu1mVZWHnbMS5NpCMpVHO8hRBic43TUQMzedCjiCR-WezejzDWHLGCPgAMJA39da_CQmcPsnyPsPEEquLOfoivcIPtc94j87i2dS08jKkrb0bXmXR2QOM6O3NmOMhMHB2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe589f1aee.mp4?token=p8wQFUweU6ywSjrD8LjOX0l4IyWWOVKYtkM2v_cpmiEHVYhBN_aKebftNc6UWOiyfgRo4u0zIkahwCpxnkn1d2JZMB3bT7Ot2ZwoiHSH8rCT_adN1V49Vyht-pUpFkCtk3YZzSAjyFYzrn9GNBxTbJez_BySUpyNYCF43UbmmHZqtjSEYxZhsZIPdF-4aLL2QKxAgGSW4w6YggUg5ugkcu1mVZWHnbMS5NpCMpVHO8hRBic43TUQMzedCjiCR-WezejzDWHLGCPgAMJA39da_CQmcPsnyPsPEEquLOfoivcIPtc94j87i2dS08jKkrb0bXmXR2QOM6O3NmOMhMHB2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک از نجف آباد اصفهان به جنوب
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/22654" target="_blank">📅 11:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-22653">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">قیمت نفت با رسیدن به ۱۰۰ دلار در بالاترین سطح از اردیبهشت امسال قرار گرفت
وقایع شب گذشته در تنگه هرمز کافی بود تا سقف هفته‌های اخیر نفت شکسته شود.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/22653" target="_blank">📅 11:21 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
