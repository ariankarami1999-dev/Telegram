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
<img src="https://cdn4.telesco.pe/file/J7CrJOBKNgmDvdO5bIZs5mFAzD9UO1SCVYtqipE4XFFYaVH60gCuQ9gg-JIo4GL7cwo7fxUbaJkv3bTI--Cz749PCqjEXan3hGO9gg3ySTHBEq9k2_pSH3Krxl_UTjVFfb5JHl-OFvkZdRdNW8slTmDUKMjGLPbEoHHcLHy5-JRrQA-T5PY9kAgMcJ63A_Q6o4Dg-QXXbw1X_BH5mFfLrl4mK0S9vSg2yFDkGlwZPCp7Dx6RRKgfThJ4qmI1KINF-3j0uK35QpwYBJ2uRjubQjTyabTm0E3Lw8dQr8hpo7TT2EBTM2ZGETOxdvD600UsweWPGHkmCOo60CQFCS0JBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 330K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 14:37:40</div>
<hr>

<div class="tg-post" id="msg-15237">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دنبال شخصی هستم که برام ویکیپدیا بیاره بالا خیلی کم لطفیه بعد از حدود ۲۵ سال فعالیت در حوزه تک و کارهای انقلابی بسیار بزرگ، صفحه ویکیپدیا نداشته باشم و افرادی که خودم به مارکت آوردم و معروف کردم داشته باشند. امیدوارم یک فرد فوق‌العاده قوی در این زمینه کمک کنه و واسم بسازه.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/withyashar/15237" target="_blank">📅 14:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15236">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/withyashar/15236" target="_blank">📅 14:32 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15235">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فقط ‌یک پیغام</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/withyashar/15235" target="_blank">📅 14:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15234">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=v486I7XFlHJSa_MmS2wM09Xv3iV_L9sk_zk22GalZ8oONgEshX6qTH2iFqYEMhoiJa8_4yNJwj7QQ5Q9k8bgi7x4gMJLhdMTJq-feZHsH8ZtARCXm1mKmki8wy_-kVPQyPCrShswNe_tgoQAMkCOrzRH4N02sbVCXX-kp5mkoi4OpsaEbN3EFKfCiWpceXEPdK0GEikcvvn5Gpay4FBWnoB94Opwy9ZbAQutvU0MRxltDLC_3bxfRkmuZCBmvdQzmncGikeXjjoYvJjMwqSCAU7-zMs_xr0j5iRPWaFYlCzyOK92z3nJcgNlefYnQhDCJqNDvfv3mY5smoFgpDXbzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e87c2bd5.mp4?token=v486I7XFlHJSa_MmS2wM09Xv3iV_L9sk_zk22GalZ8oONgEshX6qTH2iFqYEMhoiJa8_4yNJwj7QQ5Q9k8bgi7x4gMJLhdMTJq-feZHsH8ZtARCXm1mKmki8wy_-kVPQyPCrShswNe_tgoQAMkCOrzRH4N02sbVCXX-kp5mkoi4OpsaEbN3EFKfCiWpceXEPdK0GEikcvvn5Gpay4FBWnoB94Opwy9ZbAQutvU0MRxltDLC_3bxfRkmuZCBmvdQzmncGikeXjjoYvJjMwqSCAU7-zMs_xr0j5iRPWaFYlCzyOK92z3nJcgNlefYnQhDCJqNDvfv3mY5smoFgpDXbzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/withyashar/15234" target="_blank">📅 14:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15233">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر جنگ آمریکا: به طرف ایرانی اعتماد نداریم و آماده هستیم در صورت لزوم حملات علیه ایران را از سر بگیریم
@withyashar</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/withyashar/15233" target="_blank">📅 14:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15232">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=uUfqUSEql0hyDyqzCwjUqwLLBRAg26oehZQuWNE5xu01awLXsF-ZMITR9h_vL8w7quDBZ3Z9pS9CGkSoKpSAHte_TR_qNqiyyteCjgFtFUn_nza2uQdOAx2yUpE01TFznAFbciISDGxsp8hPVa7MButuTCIsum9X0fu4SAvYHnvqbwuN78sTGd7LBCY8M4YykLzxpvvkAkKfJjCnDZ5a-wtYX8AnJoLccIMENAQ6AGMpWnOkb775FcwEXwN-1VvBXsrwVOfwXNANnLqoHJTMqhf-5-U9SdyDkD5LWNJSEbOWTN8U9MP9pzhpwug10-wnD5Fh6er-O2R_fqGd7xrYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a485ae7493.mp4?token=uUfqUSEql0hyDyqzCwjUqwLLBRAg26oehZQuWNE5xu01awLXsF-ZMITR9h_vL8w7quDBZ3Z9pS9CGkSoKpSAHte_TR_qNqiyyteCjgFtFUn_nza2uQdOAx2yUpE01TFznAFbciISDGxsp8hPVa7MButuTCIsum9X0fu4SAvYHnvqbwuN78sTGd7LBCY8M4YykLzxpvvkAkKfJjCnDZ5a-wtYX8AnJoLccIMENAQ6AGMpWnOkb775FcwEXwN-1VvBXsrwVOfwXNANnLqoHJTMqhf-5-U9SdyDkD5LWNJSEbOWTN8U9MP9pzhpwug10-wnD5Fh6er-O2R_fqGd7xrYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد محبی فوتبالیست تیم جمهوری اسلامی که در خوشحالی زدن گل به تیم نیوزلند، به مردم شلیک کرد، رفته و عکس مهسا امینی رو کنده و انداخته توی سطل زباله...
@withyashar</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/withyashar/15232" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15231">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگه سر حال هستین بریم برای مرحله بعدی کارا و گسترده تر کنیم
👍
یه ریکشن لایک بدین پر ریزون باشه تا بگم</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/withyashar/15231" target="_blank">📅 13:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15230">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آژانس بین‌المللی انرژی اتمی اعلام کرد:
در حال حاضر، سطح تماس‌ها و ارتباطات با ایران در پایین‌ترین حد خود قرار دارد.
@withyashar</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/withyashar/15230" target="_blank">📅 13:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15229">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/withyashar/15229" target="_blank">📅 12:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15228">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وزیر امور خارجه اسرائیل : روابط با مسئول سیاست خارجی اتحادیه اروپا را قطع خواهیم کرد.
@withyashar</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/withyashar/15228" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15227">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منابع العربیه گزارش دادند «نخستین دور از مذاکرات فنی مستقیم واشینگتن و تهران فردا در زوریخ سوئیس برگزار می‌شود.»
به گفته منابع این مذاکرات فنی میان ایران و آمریکا شامل جنبه‌های حقوقی و قانونی مربوط به رفع تحریم‌ها علیه ایران خواهد بود.
منابع العربیه خاطرنشان کردند گفت‌وگوهای فنی ایران و آمریکا پرونده دارایی‌ها و وجوه مسدودشده ایران در قطر و همچنین پرونده هسته‌ای ایران را در بر می‌گیرد.
قرار است در نشست‌های مذاکراتی غیرعلنی و اعلام‌نشده، پرونده‌های مرتبط با لبنان و حزب‌الله نیز مورد بحث و بررسی قرار گیرد.
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15227" target="_blank">📅 12:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15226">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN0Wa1qPmPIBAm-Gp-qPlGeYDNHJUS__fpa24CYgP2offF8q2W-huPmCRniCnww8_T_86Zxq_VqubPKFP9uCAc2pWvJ7DyvmsNWTD7Li0v_dIms2dLCy6CZOe9_q3ecNqYfOw5O0W9ML-jvJKaeEGId0AhvMNsil-CLy15OYQ__k4n01gnD2WIiIExeuxHztI_MyFME-6xM3fkVNoYE7C_EiUFyMfESNHR80sLCSm7PkYvxfNNJxChU9ccd4hAkGmZse5ngLfnshS6xvXlU2Z3_Bc2AIHtizFvJVF4Jivf14ni4my8b6-uC0LYZA4ZuO-S-jITPaqL7F3E2Sio29_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در‌تروث:  این احمق‌ها که فکر می‌کنند من در قبال ایران به اندازه کافی سختگیر نبودم، در حالی که بازار سهام به تازگی به بالاترین حد خود رسیده و قیمت نفت «به سرعت در حال سقوط» است، یا حسودند، آدم‌های بد یا احمق. آمریکا را دوباره بزرگ خواهیم کرد!!!
@withyashar</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/15226" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15225">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد @withyashar</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/15225" target="_blank">📅 12:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15224">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=kS3v9atglwR7-TbiUiCtZQY22ZM8I7-dlqe1GRVkKmKMiGcU_2gPL4ZH6BZZ69H1c7_LjE_A6SAwZCM-hiqpcrzF1KM2EFqSv94QvspexC_IlDFbIJHQKr_BxeidAVPs_eSBCeJUSr1xtQmv0GHG58TUllpPRBChXxHvPwbQjOcjCxYvy6VJYoebLXPZihY-yjcAQpUdH2CG71SEVebWWxq4xCalu7WLvHX446KjdQzOAyCwPe1V_Rt13tRnJ44KGyYyCJ4T7ELblEAYiUPinsbmXmpFTN5HjmvTKVrFSDZds4NeDv6AlNark5uYda4BvGYYBsnzxnut2JyCQkK2Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b5b52d5b0.mp4?token=kS3v9atglwR7-TbiUiCtZQY22ZM8I7-dlqe1GRVkKmKMiGcU_2gPL4ZH6BZZ69H1c7_LjE_A6SAwZCM-hiqpcrzF1KM2EFqSv94QvspexC_IlDFbIJHQKr_BxeidAVPs_eSBCeJUSr1xtQmv0GHG58TUllpPRBChXxHvPwbQjOcjCxYvy6VJYoebLXPZihY-yjcAQpUdH2CG71SEVebWWxq4xCalu7WLvHX446KjdQzOAyCwPe1V_Rt13tRnJ44KGyYyCJ4T7ELblEAYiUPinsbmXmpFTN5HjmvTKVrFSDZds4NeDv6AlNark5uYda4BvGYYBsnzxnut2JyCQkK2Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهباز شریف هم یادداشت تفاهم ایران و آمریکا را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/15224" target="_blank">📅 11:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15223">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حسن روحانی هم اومد:
اسرائیل احتمالاً سعی می‌کنه با ایجاد تنش( در لبنان و …)، توافق ایران و آمریکا رو به هم بزنه؛ همون‌طور که قبلاً هم برای ضربه زدن به برجام تلاش کرده بود…
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/15223" target="_blank">📅 11:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15222">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وزیر دفاع آلمان اعلام کرد این کشور در حال اعزام دو کشتی مین روب به دریای سرخ است تا برای یک مأموریت نظامی احتمالی در تنگه هرمز آماده شود.
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/15222" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15221">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVxKBPhaXt742k9Lm5ZG-bCH1khjR2ZmSH12QTP9HPeFzKg90Cj1yz_-gDJ1sSs8SRG9XBHIHnE3fViOyzNeYDuNdHZsFlpNNisqXo1MoTrO488YxHGzdc7JmRExgxYD-j4kAYrzh1FCGXXEpdiMVB7IDKIciuWLuBGp9MlzfegsZ7Z0IiezUOKfl9v1ls6ErMIJb0yXGJTQS7En64L5Rfbp9LhSuid1KKzh-k5mZy-9V-WSuv2YX9YX_dqwkpu3xrxjtA-hJczC1Q_YvCILfDmnRp1MKWSi3bwBFBO3O58ToT7N6ZwfVOuOlpKgJ0qQ3p07iFr_nEdNGY2CO5QVkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری متفاوت از ترامپ و مکرون در ورسای
@withyashar</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/withyashar/15221" target="_blank">📅 11:41 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15220">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رویترز: اسرائیل قصد عقب‌نشینی از مواضع خود در جنوب لبنان را ندارد.
@withyashar</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/withyashar/15220" target="_blank">📅 11:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15219">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گروسی (مدیر کل
آژانس بین‌المللی انرژی اتمی
) : در مذاکرات سوئیس شرکت خواهیم کرد
@withyashar</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/15219" target="_blank">📅 11:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15218">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/15218" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15217">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با شما : درود و خسته نباشید
ما که می دونیم به قاهره نزدیک میشیم
حالا تو این راه تفاهم امضا بشه یکم از لحاظ اقتصادی و گرونی بهتر بشه
به نفع مردمه که یخورده تو این مدت نفس بکشن
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15217" target="_blank">📅 10:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15216">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15216" target="_blank">📅 10:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15215">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آکسیوس: رسانه‌های نزدیک به نتانیاهو به دلیل توافق با ایران، حمله به دولت ترامپ را آغاز کردند
مجری شبکه ۱۴ اسرائیل: ویتکاف و کوشنر یهودستیز هستند و اسرائیل را فروخته‌اند
@withyashar</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/15215" target="_blank">📅 10:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15214">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tG-9vD_T_x_9JWEBSGR_jvMCuBi0cF-pg0nog_h6DiW02_LCHN9ct_ko-lCUU9Op9t-22oOzQfKKdbV1HE2YyXzLmrPPXNYIho7Qb3BiYRqfHt4EaDqUv1N3Ilv2ZDVxF7IEJKruz8GYqGJfpsybKdY2FtD50iAP2UzB-M0SAqFusRreGyn14h53h0MXT-Q0c97o82UFgx5cA4B694NuVSjEI4B801CYWLEjY7jpQQvnIAFlwEeCKUqyu9Sk5evZEjfn6bKENtO6w3xNLXj8vcmoFc2SZ-8ct-K-A1b2Q0n4erUy81vv_yk4fWQQEjXLBUqBDAWPNU74enwIjJongw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضای مضحک پزشکیان که مانند یک شکلک کارتونی با دماغ بزرگ و دست دراز شده برای گدایی است.
@withyashar</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/withyashar/15214" target="_blank">📅 10:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15213">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دولت سوئیس اعلام کرد که روز جمعه نشستی با حضور نمایندگان آمریکا، ایران، پاکستان، قطر و دیگر کشورهای مرتبط برگزار خواهد شد تا مذاکرات مقدماتی انجام شود.
@withyashar</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/15213" target="_blank">📅 10:12 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15212">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وال استریت ژورنال: ترامپ در حال از دست دادن تندروهایی است که زمانی از جنگ ایران دفاع می‌کردن
@withyashar
الجزیره: موجی از خشم سیاسی واشنگتن را بر سر توافق با ایران فرا گرفته</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15212" target="_blank">📅 10:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15211">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سناتور بلومنتال: سنا قطعا توافق با ایران را تصویب نمی‌کند
محکومیت دو حزبی برای یک توافق ننگین عجیب نیست که شبیه «تسلیم بی‌قید و شرط» است، نه توسط ایران، آنطور که ترامپ خواسته بود، بلکه توسط آمریکا.
بیش از ۳۰۰ میلیارد دلار ثروت بادآورده، لغو تحریم‌ها، فروش نامحدود نفت، عدم بازرسی یا تأیید کامل. همه اینها به خاطر وعده‌های مبهم و غیرقابل اجرا در مورد تسلیحات هسته‌ای است که ادعای ایران برای پیروزی در برابر شیطان بزرگ را تقویت می‌کند.
هر چیزی شبیه به این توافق به محض ورود به سنا از بین خواهد رفت. برای اینکه اثر اجرایی داشته باشد، باید در اینجا تصویب شود.
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/15211" target="_blank">📅 10:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15210">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بلومبرگ از عبور یک نفتکش و یک کشتی حامل گاز مایع از تنگه هرمز پس از توافق آمریکا و ایران خبر داد.
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/15210" target="_blank">📅 10:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15209">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=coNXWnJYPbRsypoyYHKFgLkB3uGV70sKCaCOMnX8SU1bQw5rGJBe1AVIFwc-hCZPClmAyvmYx7coXq9DfkiCiysdZd5tZBEiK0Cjm5TNgWkt3kKUTIJdTlF0lAAgttml9U1_SxMU6XMetL83AVPaOKH4h0UAb8KtKt0acfaKGJU9LDtrg8VAQOBFtZdb3yrlkMxsRW1xKTtdb0LgpO7Vf2Ji9U3ODvufIpdh8_1WYyRNZTY1Vaz26qniQKa9S31-e4yIlL529q0YbBeFWNm0bvDV5l47Sy3VSK8-VB2pPJPMkdw2icCLUk1JkkfgRT9KSQ2IVB255QeD8s17Yf9MoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a024bb7519.mp4?token=coNXWnJYPbRsypoyYHKFgLkB3uGV70sKCaCOMnX8SU1bQw5rGJBe1AVIFwc-hCZPClmAyvmYx7coXq9DfkiCiysdZd5tZBEiK0Cjm5TNgWkt3kKUTIJdTlF0lAAgttml9U1_SxMU6XMetL83AVPaOKH4h0UAb8KtKt0acfaKGJU9LDtrg8VAQOBFtZdb3yrlkMxsRW1xKTtdb0LgpO7Vf2Ji9U3ODvufIpdh8_1WYyRNZTY1Vaz26qniQKa9S31-e4yIlL529q0YbBeFWNm0bvDV5l47Sy3VSK8-VB2pPJPMkdw2icCLUk1JkkfgRT9KSQ2IVB255QeD8s17Yf9MoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه امضا توسط ترامپ در مراسم شام کاخ ورسای
@withyashar</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/withyashar/15209" target="_blank">📅 09:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15208">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjoFnA3Cjcl2hI8HLwy4rK5l3WqX7cKeiPw1efF9FQtfKteUCb_d04AdBIDZbXEtt-SovmM_mTFQmkeo114EsL8vzOh4fodlbcAQ9fLBQdR6JV5lP5QdH-aL6QtBi9Aa8bhGD5JqB_bxx7rJueJ46Oif3fvn92ZR9ne_5x6jXPhlSadN7naGUqR-STmmgT7AhaLN9wBRc1XYlChALstxJM-PmyIPvp44fTmkiO1Dt_jcFCp2qNYvrgfOiQkAME22G0Eg9mDIB-Vq72ElV-42BbJcpDny2b4kCjb8h0z6xrP1_wBhmJArNoSsz5Dp1UnlG7TpJ6aD9Z91G_adFHxtAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امضا توسط ‌پژشکیان
@withyashar</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/withyashar/15208" target="_blank">📅 09:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15207">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند   اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم الان هم قیمت قطعی دلار و طلا تا پایان تابستان…</div>
<div class="tg-footer">👁️ 89K · <a href="https://t.me/withyashar/15207" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15206">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دلار و طلا تا بفروشیم یا بالا میره؟ سوالی که اکثر مخاطبین کانال در چند روز اخیر می‌پرسند
اول پاییز اعلام کردیم که دلار تا اخر سال به ۱۹۰ هزا تومان می‌رسد و طلای ۲۲ میلیونی را به درستی همانند قبل پیشبینی کرده بودیم
الان هم قیمت قطعی دلار و طلا تا پایان تابستان و بعد از آن را در کانال زیر اعلام کردیم ، حتما عضو شوید تا با آگاهی از قیمت دقیق در روزهای آینده تمام سرمایه گذاری های خود را مدیریت کنید و از تورم جا نمانید
👇
https://t.me/+hLt81qXCGTQzOWQ0
https://t.me/+hLt81qXCGTQzOWQ0</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/15206" target="_blank">📅 03:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15205">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=sQDx0_wFEqk0Mp6HgpF7oz3reCN_qWiuh0779TDOpLte3za5_P41cG61SHckfdudRUR7Hck5e70q856og7j4bEFhtZnc0HXj9pGg-bKeXdCFIdUsIQq3-BxE-AB1TpKkur9MHbuaKqqfrT2zOJvKUTLRk7SgO0viW7UvF1wpPfKv17xEZh9K1w-putGpfBWWmVYsGo92N8dxA47IStNDJW_JJRnQRNKVqYuKjVSHtN6YTvQGjasZmfHk5DIQn3xJfQZiy_Hl64cKe1iUVPjxDjjBkCVAxnZoFQePuREHlVY2_gy0RixeRfOnlJLQGYAYXygggoK1FBjh3cdukXskxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0641a8394a.mp4?token=sQDx0_wFEqk0Mp6HgpF7oz3reCN_qWiuh0779TDOpLte3za5_P41cG61SHckfdudRUR7Hck5e70q856og7j4bEFhtZnc0HXj9pGg-bKeXdCFIdUsIQq3-BxE-AB1TpKkur9MHbuaKqqfrT2zOJvKUTLRk7SgO0viW7UvF1wpPfKv17xEZh9K1w-putGpfBWWmVYsGo92N8dxA47IStNDJW_JJRnQRNKVqYuKjVSHtN6YTvQGjasZmfHk5DIQn3xJfQZiy_Hl64cKe1iUVPjxDjjBkCVAxnZoFQePuREHlVY2_gy0RixeRfOnlJLQGYAYXygggoK1FBjh3cdukXskxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعت ۳:۱۹  صبح امروز (کمی پیش) چند قایق متعلق به سپاه پاسدارن درحال اقدامی نامشخص در تنگه هرمز هستند.
ناو آمریکایی در بیسیم به زبان فارسی متنی هشدار آمیز را پخش می‌کند که می‌گوید:
جمهوری اسلامی کنترلی بر تنگه ندارد، عملیات را متوقف کنید و به بندر باز گردید، وگرنه نیروی دریایی ایالات متحده به کشتی شما حمله خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/withyashar/15205" target="_blank">📅 03:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15204">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">مذاکرات جمعه ایران و آمریکا در سوئیس الان قطعی نیست
بقایی، سخنگوی وزارت خارجه:
جلسه جمعه تا چند ساعت قبل قطعی بود ولی وقتی قرار شد روسای جمهور دو طرف (ایران و آمریکا) تفاهمنامه را امضا کنند، قرار شد درباره جلسه جمعه فعلاً تامل شود.
@withyashar</div>
<div class="tg-footer">👁️ 91.1K · <a href="https://t.me/withyashar/15204" target="_blank">📅 02:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15203">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 96K · <a href="https://t.me/withyashar/15203" target="_blank">📅 01:53 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15202">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">https://x.com/yasharrapfa</div>
<div class="tg-footer">👁️ 97K · <a href="https://t.me/withyashar/15202" target="_blank">📅 01:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15201">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/withyashar/15201" target="_blank">📅 01:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15200">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاخ سفید:
ترامپ تفاهم‌نامه با ایران را امضا کرد
@withyashar</div>
<div class="tg-footer">👁️ 97.6K · <a href="https://t.me/withyashar/15200" target="_blank">📅 01:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15199">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طبق گزارش Axios، رئیس‌جمهور ترامپ شخصاً نسخه‌ای از توافقنامه را در حین صرف شام با رئیس‌جمهور فرانسه ماکرون در کاخ ورسای امضا کرد.
عکسی از توافقنامه امضا شده به ایرانی‌ها و کشورهای میانجی ارسال شد.
@withyashar</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15199" target="_blank">📅 01:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15198">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تسنیم: متن فارسی تفاهمنامه نیز به عنوان سند رسمی به امضای ایران و آمریکا رسیده است
@withyashar</div>
<div class="tg-footer">👁️ 98.6K · <a href="https://t.me/withyashar/15198" target="_blank">📅 01:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=i_gIDtJ7ig4f49bzpRJxC8YK-zxanqdGAj_sAKdRfiLTeRsuaDSq0L4xJtKrBL4dzh_EVFZI3MhToB3FfCgTjWNqCjjYDjju_bLC4QOoN2nadh6kFZaf49Sf8HnfL0xPh7o5lcCIBgqs0BQoCcRqxIysCjK-AvoBjMku_KLX-LSI__ERfE4mzIEH3muBcI-JjQeO0jJ6RcDAhsMq3Ac4VvQfcSrt0wtwM7_9MWkM1YP_QpXT7Ue8zbn1ote-rT3FEncIqowhGR0sszw7mzvUNL6kncEHqUpMp6QFn4898Q2e5ttFE5b5f4ewA84EIoYocaoSHd2gRWNrCLq0-1BJZrAk0c0gvHFkoWqEHoF0IAJuZmUXh-un7pW9rlwLjwK0Jho64T0qx-Z_q87GlQ7M-pUDpyhzaxUagrifAtlZJPDixC_dzAkrKYKVfuw6KoHW-Y_16L4YOWEn_eqgwOXXVJ9B651QxIxsOMgWy51hB04GoNbrSX6L-THYG6X723DddC-Sg5OL-NoqH5mdWKNUDiqTPvGQqM_oCMbVfiCFRFxBYH-PFrA7pejX_DULVA-kQ6VIez0jAcTjUDxzfrb9tPSFv1990KQPk4hSh9aX26sG7tZIspJjW2uoOimk1rkLrIG9a718Ky6jyYNNykZ_GwPuk6C7QexGfNHOcwP_08U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0a3d37ce.mp4?token=i_gIDtJ7ig4f49bzpRJxC8YK-zxanqdGAj_sAKdRfiLTeRsuaDSq0L4xJtKrBL4dzh_EVFZI3MhToB3FfCgTjWNqCjjYDjju_bLC4QOoN2nadh6kFZaf49Sf8HnfL0xPh7o5lcCIBgqs0BQoCcRqxIysCjK-AvoBjMku_KLX-LSI__ERfE4mzIEH3muBcI-JjQeO0jJ6RcDAhsMq3Ac4VvQfcSrt0wtwM7_9MWkM1YP_QpXT7Ue8zbn1ote-rT3FEncIqowhGR0sszw7mzvUNL6kncEHqUpMp6QFn4898Q2e5ttFE5b5f4ewA84EIoYocaoSHd2gRWNrCLq0-1BJZrAk0c0gvHFkoWqEHoF0IAJuZmUXh-un7pW9rlwLjwK0Jho64T0qx-Z_q87GlQ7M-pUDpyhzaxUagrifAtlZJPDixC_dzAkrKYKVfuw6KoHW-Y_16L4YOWEn_eqgwOXXVJ9B651QxIxsOMgWy51hB04GoNbrSX6L-THYG6X723DddC-Sg5OL-NoqH5mdWKNUDiqTPvGQqM_oCMbVfiCFRFxBYH-PFrA7pejX_DULVA-kQ6VIez0jAcTjUDxzfrb9tPSFv1990KQPk4hSh9aX26sG7tZIspJjW2uoOimk1rkLrIG9a718Ky6jyYNNykZ_GwPuk6C7QexGfNHOcwP_08U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بقایی: همین الان که در حال صحبت هستیم متن توافق رسما به امضا رئیس جمهور های دو طرف رسیده است
قرار بود که بامداد روز ۲۸ خرداد ماه رئیس جمهور دو کشور این متن و توافق رو امضا کنند.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/15197" target="_blank">📅 00:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15196">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 99.2K · <a href="https://t.me/withyashar/15196" target="_blank">📅 00:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15195">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/15195" target="_blank">📅 00:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15194">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: ظرف ۴۸ ساعت آینده توافق با ایران امضا خواهد شد و احتمالا برای مدتی ارتش رو در خلیج فارس نگه خواهیم داشت.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15194" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15193">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">@withyashar
Reeee</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15193" target="_blank">📅 23:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15191">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجری شبکه خبر : چرا ایران در روز آخر مذاکره حمله به اسرائیل را متوقف کرد؟
قالیباف: ما هر آنچه که می‌خواستیم با حمله بگیریم را چندین برابرش را با مذاکره گرفتیم. ساعت ۲ صبح ترامپ آتش‌بس را در کل لبنان داد و با آن ادبیات با نتانیاهو صحبت کرد.
قرار بود آمریکا محاصره را ظرف ۳۰ روز بردارد اما ترامپ گفت همین امشب محاصره را برمی‌داریم
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/15191" target="_blank">📅 23:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15190">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">@withyashar</div>
<div class="tg-footer">👁️ 99.9K · <a href="https://t.me/withyashar/15190" target="_blank">📅 23:19 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15189">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۹. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند که تا زمان توافق نهایی وضعیت موجود را حفظ کنند؛ جمهوری اسلامی ایران وضع موجود را در برنامه هسته‌ای خود حفظ خواهد کرد، و ایالات متحده آمریکا هیچ تحریم‌های جدیدی علیه ایران وضع نخواهد کرد و نیروهای نظامی بیشتری را در منطقه مستقر نخواهد کرد.
@withyashar
۱۰. ایالات متحده آمریکا متعهد می‌شود بلافاصله با امضای این یادداشت تفاهم و تا زمان خاتمه تحریم‌ها، اسقاطیه‌های وزارت خزانه‌داری را برای صادرات نفت خام ایران، محصولات پتروشیمی و مشتقات آنها، و تمامی خدمات مرتبط شامل تراکنش‌های بانکی، بیمه‌ها، حمل و نقل و غیره صادر کند.
۱۱. ایالات متحده آمریکا متعهد می‌شود تا وجوه و دارایی‌های محدود یا مسدود شده جمهوری اسلامی ایران را با اجرای این یادداشت تفاهم به طور کامل برای استفاده در دسترس قرار دهد. ایالات متحده آمریکا و جمهوری اسلامی ایران در مورد روال مربوط به آزادسازی این وجوه در طول مذاکرات، به صورت دوجانبه توافق می‌کنند. این وجوه، چه در حساب اصلی نگهداری شوند و چه منتقل شوند، برای پرداخت به هر ذینفع نهایی که توسط بانک مرکزی جمهوری اسلامی ایران تعیین می‌شود، باید به طور کامل قابل استفاده شوند. ایالات متحده آمریکا متعهد می‌شود که تمامی تاییدیه ها و مجوزهای لازم را در این رابطه صادر کند.
@withyashar
۱۲. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت می‌کنند تا یک سازوکار اجرایی برای نظارت بر اجرای موفق این یادداشت تفاهم و پایبندی آتی به توافق نهایی تشکیل شود.
۱۳. پس از امضای این یادداشت تفاهم و منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ این یادداشت تفاهم و تداوم اجرای این اقدامات، جمهوری اسلامی ایران و ایالات متحده آمریکا مذاکرات درخصوص توافق نهایی را منحصرا در مورد بقیه بندها آغاز خواهند کرد.
۱۴. توافق نهایی با یک قطعنامه الزام‌آور شورای امنیت سازمان ملل متحد تایید خواهد شد.
(امضاء) از طرف دولت جمهوری اسلامی ایران
تاریخ
(امضاء) از طرف دولت ایالات متحده آمریکا
تاریخ
( امضاء) در حضور میانجی
از طرف دولت جمهوری اسلامی پاکستان
تاریخ
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/15189" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15188">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یادداشت تفاهم اسلام‌آباد بین جمهوری اسلامی ایران و ایالات متحده آمریکا
به گزارش تسنیم، متن تفاهم‌نامه ایران و آمریکا به شرح ذیل است:
جمهوری اسلامی ایران و ایالات متحده آمریکا، به طور مشترک و با حسن نیت، در تاریخ ۲۸ خرداد ۱۴۰۵ نسبت به موارد زیر توافق کردند:
@withyashar
۱. جمهوری اسلامی ایران و ایالات متحده آمریکا و متحدین آنها در جنگ حاضر، با امضای این یادداشت تفاهم خاتمه فوری و دائمی عملیات‌های نظامی را در تمامی جبهه‌ها، از جمله در لبنان، اعلام کرده و تعهد می‌کنند از این پس هیچ جنگ یا هیچ عملیات نظامی علیه یکدیگر آغاز نکنند و از تهدید یا استفاده از زور علیه یکدیگر خودداری کنند و تمامیت ارضی و حاکمیت لبنان را تضمین کنند. توافق نهایی خاتمه دائمی جنگ در تمامی جبهه‌ها، از جمله در لبنان، و بقیه مفاد این بند را تایید خواهد کرد.
۲. جمهوری اسلامی ایران و ایالات متحده آمریکا متعهد می‌شوند که به حاکمیت و تمامیت ارضی یکدیگر احترام بگذارند و از مداخله در امور داخلی یکدیگر خودداری کنند.
@withyashar
۳. جمهوری اسلامی ایران و ایالات متحده آمریکا به انجام مذاکرات و حصول به یک توافق نهایی در مدت حداکثر ۶۰ روز، قابل تمدید با رضایت طرفین، متعهد می‌شوند.
۴. بلافاصله با امضای این یادداشت تفاهم، ایالات متحده آمریکا شروع به رفع محاصره دریایی خود و هرگونه مزاحمت یا ممانعت علیه جمهوری اسلامی ایران می‌کند، و ظرف ۳۰ روز به محاصره دریایی به طور کامل خاتمه خواهد داد. در طول این مدت، تردد کشتی‌ها متناسب با تعداد ترافیک قبل از جنگ که از سوی جمهوری اسلامی ایران برقرار می‌شود، خواهد بود. ایالات متحده آمریکا همچنین متعهد می‌شود تا ظرف ۳۰ روز پس از توافق نهایی، نیروهای نظامی خود را از حوزه پیرامونی جمهوری اسلامی ایران خارج کند.
۵. با امضای این یادداشت تفاهم، جمهوری اسلامی ایران ترتیباتی را با حداکثر تلاش خود برای عبور ایمن کشتی‌های تجاری، بدون هزینه فقط برای ۶۰ روز، از خلیج فارس به دریای عمان و بالعکس، اتخاذ خواهد کرد. تردد کشتی‌های تجاری بلافاصله آغاز، و با توجه به ضرورت رفع موانع فنی و نظامی و مین‌زدایی توسط جمهوری اسلامی ایران، ظرف ۳۰ روز برقرار خواهد شد. جمهوری اسلامی ایران با سلطنت عمان برای تعیین اداره آینده و خدمات دریایی در تنگه هرمز، مطابق با حقوق بین الملل قابل اجرا و حقوق حاکمیتی کشورهای ساحلی تنگه هرمز، گفتگو خواهند کرد و با دیگر کشورهای ساحلی خلیج فارس نیز تبادل نظر می‌کنند.
@withyashar
۶. ایالات متحده آمریکا متعهد می‌شود، با شرکای منطقه‌ای خود، برای بازسازی و توسعه اقتصادی جمهوری اسلامی ایران یک برنامه قطعی مورد توافق طرفین را با تامین حداقل ۳۰۰ میلیارد دلار ایجاد کند. سازوکار اجرایی‌سازی این برنامه، به عنوان بخشی از توافق نهایی ظرف ۶۰ روز نهایی خواهد شد. تمامی تائیدیه‌ها، اسقاطیه‌ها و مجوزهای مورد نیاز برای تراکنش‌های مالی مربوطه توسط ایالات متحده آمریکا ارائه خواهد شد.
۷. ایالات متحده آمریکا متعهد می‌شود به تمامی انواع تحریم‌ها علیه جمهوری اسلامی ایران، از جمله قطعنامه‌های شورای امنیت سازمان ملل متحد، قطعنامه‌های شورای حکام آژانس بین‌المللی انرژی اتمی، و تمامی تحریم‌های یکجانبه آمریکا، اعم از اولیه و ثانویه، برابر یک برنامه زمانی مورد توافق به عنوان بخشی از توافق نهایی، خاتمه دهد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوع خاتمه تحریم‌ها که در بالا ذکر شده است اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
۸. جمهوری اسلامی ایران مجدداً تایید می‌کند که سلاح هسته‌ای تولید یا ابتیاع نخواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا موافقت کرده‌اند که وضعیت مواد غنی‌شده ذخیره شده را از طریق یک سازوکار مورد توافق طرفین و مطابق با برنامه زمانی مندرج در بند ۷، حداقل به شیوه رقیق‌سازی در محل، تحت نظارت آژانس بین‌المللی انرژی اتمی، حل و فصل کنند. دو طرف همچنین موافقت می‌کنند تا در مورد موضوع غنی‌سازی، و دیگر موضوعات مورد توافق دو طرف مرتبط با نیازهای هسته‌ای جمهوری اسلامی ایران، بر اساس یک چارچوب رضایت‌بخش که در توافق نهایی مورد موافقت قرار خواهد گرفت، بحث کنند. توافق نهایی مفاد این بند را تایید خواهد کرد. جمهوری اسلامی ایران و ایالات متحده آمریکا به اهمیت اساسی موضوعات هسته‌ای ذکرشده در بالا اذعان دارند و قصد خود را برای رسیدگی فوری به این موضوعات در مذاکرات، به منظور دستیابی به توافق متقابل در مورد آنها اظهار می‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 97.7K · <a href="https://t.me/withyashar/15188" target="_blank">📅 22:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15187">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">طبق برخی گزارش ها نیروهای ارتش جولانی در سوریه برای ورود به لبنان و مبارزه با حزب اللّه آماده میشوند
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15187" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15186">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه خبر: انتشار متن تفاهم نامه ایران و آمریکا تا دقایقی دیگر
@withyashar</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/withyashar/15186" target="_blank">📅 22:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15185">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">شبکه i24News اسرائیل:
متن رسمی یادداشت تفاهم ایران و آمریکا منتشر شده و طبق این توافق، همه درگیری‌ها از جمله در لبنان باید فورا متوقف بشه.
همچنین یک برنامه اقتصادی 300 میلیارد دلاری برای جمهوری اسلامی در نظر گرفته شده.
بر اساس گزارش، ذخایر اورانیوم با غنای بالای ایران داخل کشور و تحت نظارت آژانس رقیق خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/15185" target="_blank">📅 22:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15184">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/15184" target="_blank">📅 22:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15183">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3f8b7f61.mp4?token=Kqium351hovlMo_IV89cLmtz6DpU5Ljw_3Yx3yAj6YAHqlVV2hYR7tsXg6JCuQ2PeFPNci6G32sHI5LdSQWm-UWZ4c5MUN25jWZA2tQCLo7DwDLn-vfAFLAHV1tioEx6k3FiBBW3WlxwiLrPMbqk_IqB1aIcgYPJ00obr4PBeDwdW8S-OzaTylOhKbTbj5Wn3aQAwl7CeNj7-TVdA74s_ub5qdFmSLZ8wLE3Qe5OWLw_TTYLt9FxMh8VvAMCdii_ivXRPZpgkOwOUqpUwm8Fdf3TZmxw4BcjfiCw2b7Bgy5nBw4UUdOvs4OoQ3MjWzU59AUv38rbgCRlkKBlFTPSCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با هواپیما به سمت کاخ ورسای رفت، تا مکرون و رهبران کشوران اروپایی شام بخوره
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/15183" target="_blank">📅 22:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15182">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1GvKM1-auVUtMQRW3xne8EmVupj2NZEcVsy9oE6ZHe2hruzj-VHvsFTnsXa58MarU9YV7fBmhQ40pyBnM9UA3GdQvKnv8xLE9ZDPurvi8hQiIu6LIi9dNxdc4r3TJHY583wbXAUxx-SMR84jXTercvEplIk70brAd-zsIxEfBJS3tgxsp0I7xhfhE9ew6N7ycE4CxfHNkPwMA7eUCPmztdybd9BlRJ4LFfUJa-N0W04lGtlurOhDh7ES3XDiuH6WJHKJRDzUeXgJFGULFlk5dVtWspCsHm6GW2zGgRaPUb23JmIMSmoI4rIVSOO4ZOOWLXd2Vp4JIsFKgSluvQ5VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سناتور لیندسی گراهام: به نظر من امضای این تفاهم‌نامه به نفع آمریکا خواهد بود، چون تنگه هرمز شروع به بازگشایی میکنه و درگیری‌ها با ایران متوقف میشه.
اینکه آیا آمریکا میتونه با ایران بر سر برنامه هسته‌ای و سایر مسائل به توافقی قابل قبول و قابل راستی‌آزمایی برسه یا نه، هنوز مشخص نیست، اما من تلاش برای رسیدن به چنین توافقی رو کم‌هزینه می‌بینم.
@withyashar</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/withyashar/15182" target="_blank">📅 22:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15181">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزارت امور خارجه ایران: ادامه اشغال جنوب لبنان توسط اسرائیل، نقض تفاهم‌نامه است و ما اقدامات لازم را انجام خواهیم داد
ایالات متحده متعهد شده است که تمام تحریم‌ها از جمله تحریم‌های شورای امنیت سازمان ملل را در یک جدول زمانی که در طول مذاکرات مورد بحث قرار خواهد گرفت، لغو کند
@withyashar</div>
<div class="tg-footer">👁️ 86.8K · <a href="https://t.me/withyashar/15181" target="_blank">📅 21:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15180">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
کانالی که ترور هنیه و نصرالله رو دقیق پیشبینی کرده بود، دلار ۱۶۰ تومنی رو هم دو ماه پیش اعلام کرده بود از تاریخ و نحوه حمله ایران به اسرائیل پرده برداشت!!!
🚨
نمیدونم به کجا وصله ولی از همه چی خبر داره بیا خودت ببین
👇
👇
🔴
LINK - CHANNEL
🔴</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/15180" target="_blank">📅 21:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15179">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الجزیره به نقل از وزارت امور خارجه ایران: در حال حاضر در حال بررسی ایده امضای تفاهم‌نامه از راه دور توسط رؤسای جمهور ایران و ایالات متحده هستیم.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15179" target="_blank">📅 21:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15178">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">معاون وزیر ارتباطات: اینترنت دیگر در شرایط بحران قطع نخواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15178" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15177">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یک مقام کاخ سفید: نشست سوئیس برای مرحله بعدی بسیار مهم خواهد بود زیرا سند کنونی نیت‌های طرفین را منعکس می‌کند.
@withyashar</div>
<div class="tg-footer">👁️ 87.4K · <a href="https://t.me/withyashar/15177" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15176">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">خبرنگار: آیا اکنون می‌توانید بگویید که آیا کسی را در دولت خود به خاطر حمله به مدرسه‌ای که در اولین روز جنگ بیش از ۱۰۰ کودک را کشت، مسئول می‌دانید؟
پرزیدنت ترامپ:
این سوال عجیبی است که در این تاریخ پرسیده می‌شود، چون شما درباره زمانی صحبت می‌کنید که مدت زیادی گذشته است، اما کسی این کار را عمداً انجام نداد.
فکر می‌کنم باید درباره آن‌ها بگویید، چه می‌شود درباره هزاران سربازی که وقتی در ماشین خود را باز کردند منفجر شدند؟ چه می‌شود درباره هزاران نفری که توسط ایران کشته شدند؟
اشتباهات رخ می‌دهد، جنگ زشت است، می‌دانم که تحت بررسی است. از پیت هگستث این سوال را می‌پرسم زیرا آن‌ها آن را تحت بررسی دارند.
﻿
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/15176" target="_blank">📅 20:46 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15175">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4pcsty2vPiUv-wD9IFDY0NMFzTdE3LoBwEbn7LkuW59avI5vKhqtirREHai297H-qTbLmBDTvIORlW0MyH-OIxSXrUqvyQI4PH-fvOjUhJDZUiiXBBlGev-FwPoeQrh4FuHiJXy7zR1aQDP2xTCdWq-L0ZRHEbmTUuClEqZ7rN82YF6JiiGBoj7FFCwpDTmaaVHtw_xsTDwdtP3DBoC06vXzPA4tMCxbsjs0_U94Cmp7vIY-vcquU-4_0z-Ol4779CVWynNK4mOJ5V2E5_hS5YQcddQYKX2wuzY2OWi6PaxvqVxPHUwuCWorxRFGZIoMJXsj-xwapxXG0NGgwPB3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش‌ها از وقوع حادثه دریایی در نزدیکی سواحل یمن
گزارش‌های امنیتی از وقوع یک حادثه دریایی جدید در آب‌های نزدیک به یمن خبر می‌دهد.
گزارش شده قایق‌های تندرو و کوچک ناشناس، یک کشتی عبوری را در فاصله ۱۰۵ مایل دریایی شمال شرق عدن هدف قرار دادند.
@withyashar</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/withyashar/15175" target="_blank">📅 20:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15174">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-footer"><a href="https://t.me/withyashar/15174" target="_blank">📅 20:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15173">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ : به آنها می‌گویم: شما احتمالاً سومین ذخایر بزرگ نفت در جهان را دارید، به چه دلیل به سلاح هسته‌ای نیاز دارید؟
@withyashar</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/withyashar/15173" target="_blank">📅 20:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15172">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ: ایرانی‌ها باید تعدادی موشک داشته باشند، چون دیگران هم دارند
ما روی یک تلاش موازی با کشورهای حوزه‌ی خلیج فارس کار خواهیم کرد تا به مسائل غیرهسته‌ای، مانند موشک‌های بالستیک متعارف که درباره‌شان صحبت خواهیم کرد، و حمایت‌ها بپردازیم.
کسی می‌گفت: شما نباید حتی یک موشک هم به آن‌ها بدهید برخی از این آدم‌ها را دوست دارم، اما فکر نمی‌کنم زیاد باهوش باشند.
می‌گفتند: جناب، شما نباید اجازه دهید آن‌ها هیچ موشکی داشته باشند. من گفتم: «خب، پس من باید چه کار کنم؟ آیا باید اجازه دهم عربستان سعودی موشک داشته باشد، اما آن‌ها نداشته باشند؟» گفتند: «بله جناب.»
اما نمی‌شود، کارها این‌طور پیش نمی‌رود، می‌دانید؟ این‌گونه کارساز نیست و موشک‌ها مشکل اصلی نیستند. موشک‌ها فقط به یک نقطهٔ کوچک آسیب می‌زنند، اما کرهٔ زمین را نابود نمی‌کنند.
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15172" target="_blank">📅 20:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15171">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامپ : رهبرهای جدید ایران آدم‌های باهوشین، خیلی هم باهوشن؛
به اندازه قبلی‌ها تندرو و افراطی نیستن، فکر می‌کنم واقعاً کشورشون رو دوست دارن و آدم‌های خوبی هستن.
@withyashar
🤣</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/15171" target="_blank">📅 20:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15170">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامپ: خب، آنها به سرمایه‌گذاری نیاز دارند، چون ما حدود یک و نیم تریلیون، شاید دو تریلیون دلار خسارت وارد کردیم.
پس کسی باید به آنها کمک کند خب، هیچ تضمینی برای کمک به آنها وجود ندارد، و ممکن است همسایگانشان کمی به آنها کمک کنند، نمی‌دانم، اما این مقدار زیادی پول است.
تقریباً هیچ‌کس چنین پولی ندارد این همان نوع خسارتی است که وارد شده است
@withyashar</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/15170" target="_blank">📅 20:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15169">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ: ما موظف نیستیم چیزی به ایران بدهیم، اما ممکن است برخی بخواهند آنجا سرمایه‌گذاری کنند.
آنها از یک نظر فرهنگی ابتدایی دارند، اما این فرهنگ ابتدایی نابغه است، آنها مردم بسیار باهوش و مذاکره‌کنندگان بسیار خوبی هستند
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/15169" target="_blank">📅 20:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15168">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=ikqAvT5kxsuiH1IA7Ww82vCujmwhQiA03FyDAu6Zw3mYHi2g0-YsRhoorh4lqaNF9_yLdypFwfMgj4RITd3fDBt5ejaa_E83sHRC84D-9h6mcVgctV_AsZjC5Qot1QOP5erbGyRgodU3bgJEYSanghF3scXnKThekxfSYSrhE7c--97d7F8Qzxhfk2Hd5lR7rXVLsFFWe5avJQZ9AIDoUw_jUaanIFAL-CdEhAiMxY0l3T8vaX8fBTAb8wU2xIh-uiw2UWjr5VxJfLpsN3AWqYLXdYk6pQgOrg9J9glCT8k8IrhdQNf2kHqcVCMqtU-NXkqcNiNQGH2gTkNZBJtdnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0786cbbc7f.mp4?token=ikqAvT5kxsuiH1IA7Ww82vCujmwhQiA03FyDAu6Zw3mYHi2g0-YsRhoorh4lqaNF9_yLdypFwfMgj4RITd3fDBt5ejaa_E83sHRC84D-9h6mcVgctV_AsZjC5Qot1QOP5erbGyRgodU3bgJEYSanghF3scXnKThekxfSYSrhE7c--97d7F8Qzxhfk2Hd5lR7rXVLsFFWe5avJQZ9AIDoUw_jUaanIFAL-CdEhAiMxY0l3T8vaX8fBTAb8wU2xIh-uiw2UWjr5VxJfLpsN3AWqYLXdYk6pQgOrg9J9glCT8k8IrhdQNf2kHqcVCMqtU-NXkqcNiNQGH2gTkNZBJtdnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما یک نسخه از توافق ایران را به اسرائیل ارسال کردیم
@withyashar</div>
<div class="tg-footer">👁️ 78.3K · <a href="https://t.me/withyashar/15168" target="_blank">📅 20:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15167">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ: من با نتانیاهو در مورد لبنان اختلاف نظر داشتم و به او گفتم که مودبانه رفتار کند
نتانیاهو گاهی اوقات کمی از کوره در می‌رود، اما من با او همکاری بسیار خوبی دارم
ما به احتمال زیاد توافق را امضا خواهیم کرد و ایران خواهان آن است؛ آنها به طور مناسب عمل کرده و موافقت کرده اند که سلاح هسته ای تولید نکنند
@withyashar</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/withyashar/15167" target="_blank">📅 20:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15166">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامپ: من توافق کردم چون نمی‌خواستم شاهد یک فاجعه اقتصادی باشم.
دو روز گذشته به شدت دشوار بوده است، و ما به ایرانی‌ها اطلاع داده‌ایم که اگر به توافقی نرسیم، بمباران آن‌ها را برای شب دوم از سر خواهیم گرفت
@withyashar</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/withyashar/15166" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15165">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjtpzyeOlZLe_og6fJq5CGMFKHVBJCP-klJZq2qfotvScSebRgsJYJpeiXp35Co5vA4K0_dhwRoYNRf5oN3L9uxbLewKPXOwPk9rg5X4uwQO-aHpA5nSRL5ABdUaOOXaM0Zt7o56W-e4_E-01qZH32rvxV1peer_uYLNzJ_lxGLJZwwVEbHi8MaOYrx6i--cl-ha8PC1wLEFoWbU_bG-y69w9R2N42sdEpSBMXLLfw_TdrnlQnk4HHtsG37mnYiyvcd6JtDoe46IxzPCh-li0QPO_G814T2DF3-2DWfK8uX3CLlB6EeCtf7C76qlAFv2RdcBgAlkMKrZQ0luO0hP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وال استریت ژورنال دارایی‌های مسدود شده ایران را اعلام کرد:
چین: ۲۰-۵۰ میلیارد دلار (بزرگ‌ترین)
قطر: ۲۰-۵۰ میلیارد (شامل ۶ میلیارد بشردوستانه)
عراق: ۱۵ میلیارد (برق و گاز)
هند و کره جنوبی: هرکدام ۷ میلیارد
ژاپن: ~۳ میلیارد
آمریکا: ۲ میلیارد
لوکزامبورگ و عمان: مبالغ کمتر
@withyashar</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/withyashar/15165" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15164">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آکسیوس: حتی اگر زمان امضا تغییر کنه، نشست هیئت‌های آمریکا و ایران به ریاست جی‌دی ونس و محمدباقر قالیباف طبق برنامه روز جمعه در سوئیس برگزار خواهد شد.
انتظار میره دو طرف درباره آغاز مذاکرات پیرامون برنامه هسته‌ای ایران گفت‌وگو کنند.
@withyashar</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/withyashar/15164" target="_blank">📅 19:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15163">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آکسیوس
: دیدار هیئت مذاکره کننده ایرانی و آمریکایی در روز جمعه در سوئیس برای امضای یادداشت تفاهم نامه به احتمال زیاد برگزار نخواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/15163" target="_blank">📅 18:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15162">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک منبع نزدیک به تیم مذاکره کننده به تسنیم گفت:
سفر تیم مذاکره کننده به سوئیس در روز جمعه لغو نشده است اما جزییات ترتیبات مربوط به امضای تفاهم نامه همچنان در حال رایزنی است و هنوز هیچ جزییاتی در این باره(چگونگی امضای تفاهم) نهایی نشده است.
@withyashar
اگه تسنیم میگه پس یه خبرهایی هست داره لغو میشه
🤣</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15162" target="_blank">📅 18:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15161">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس جمهور فرانسه، مکرون پیرزن باز:
من فکر می‌کنم توافق ترامپ با ایران توافق خوبی است.
البته که همه چیز را فوراً حل نمی‌کند، نه.
اما اگر ما به جنگیدن ادامه می‌دادیم، این به چه معناست؟ این به معنای بسته ماندن تنگه هرمز بود.
@withyashar</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/15161" target="_blank">📅 18:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15160">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترامپ: من وارد توافق‌هایی شده‌ام که ۱۰۰ درصد قطعی بودند، اما عملی نشدند؛ وارد توافق‌هایی هم شده‌ام که هیچ شانسی برای انجام‌شان وجود نداشت، اما اتفاق افتادند؛ فکر می‌کنم توافق [با ایران] انجام خواهد شد
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/15160" target="_blank">📅 18:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15159">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Parandeh (IG @yashar)</div>
  <div class="tg-doc-extra">Martik (t.me/withyashar)</div>
</div>
<a href="https://t.me/withyashar/15159" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15159" target="_blank">📅 18:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15158">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: اگر ایران یادداشت تفاهم را تکمیل نکند، دوباره به نقطه شروع برمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/withyashar/15158" target="_blank">📅 18:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15157">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اخبار اولیه‌ای و تأیید نشده‌ مبنی بر لغو امضای جمهوری اسلامی برای یادداشت تفاهم در روز جمعه، به دلیل حملات به لبنان.
@withyashar
🚨</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/15157" target="_blank">📅 18:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15156">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8u27aD2AWwl3PVNwTsutqVeZXk0Wne1QDeKf36a4JTW2kYreAVkfCnWnmmGRNAdN7thmRxxxZQlwj3-U20d0g-yL2nVFtLZqNoRtWORjmsGm92m8jX3_8dfp417v1dxxcYUCZ4p6f4Z8Rj2PmcfmT_tIxVE2CDkVQCVCC4NsmEla5s2ZJyAMyXZdJN7O0XDBv3fdWAXvKZ0O2qR5v5xMkQcAHmlId3eJUnPMV3Vr5mdi6WVgfF0tkIM5GVyElYorDWhCITxNVkwlMjFdNmRXpjPrJjs32KutDH3FCv2FaaEUUL7uSFQ8Botd7AYn3U_ZLH9XnWjq8DEvfgi0tdutQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : من در عرض ۴۵ دقیقه از فرانسه یک کنفرانس خبری برگزار خواهم کرد. سپس به ورسای برای صرف شام با رهبران فرانسوی و دیگر رهبران اروپایی خواهم رفت و بعد از آن امشب به خانه بازمی‌گردم!
این سفر یک موفقیت بزرگ بود، اما عمدتاً چیزی که همه می‌خواستند درباره‌اش صحبت کنند این است که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد!
شاخص‌های عظیمی در همه بخش‌ها برای اقتصاد ایالات متحده وجود دارد، به طوری که امروز بیشتر از همیشه افراد مشغول به کار هستند.
بیش از ۱۹.۱ تریلیون دلار در آمریکا سرمایه‌گذاری شده است، با تمام کارخانه‌ها و سایر موارد، اما نکته مهم این است که شاخص‌های اخیر بازار سهام به دلیل توافق افزایش یافته‌اند و به همین ترتیب، قیمت نفت به سرعت در حال کاهش است!
@withyashar</div>
<div class="tg-footer">👁️ 85.7K · <a href="https://t.me/withyashar/15156" target="_blank">📅 17:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15155">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">️جی‌دی ونس: برخی افراد فقط می‌خواهند بمباران ادامه یابد، صرف نظر از اینکه آیا برای آمریکایی‌ها دستاوردی دارد یا خیر.
ترامپ سعی در ایجاد بدبختی برای مردم ایران ندارد
@withyashar</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/15155" target="_blank">📅 17:12 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15154">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اسرائیل پرچم خود را در منطقه‌ای از سوریه برافراشت
منابع خبری در سوریه از نفوذ نظامیان ارتش اسرائیل به روستای «القحطانیه» در استان قنیطره خبر دادند و پرچم خود را برفراشتند
@withyashar</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/withyashar/15154" target="_blank">📅 17:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15153">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کانال ۱۳ اسرائیل: آمریکا جزئیات توافق با ایران را از اسرائیل مخفی نگه داشته، زیرا نگران است که تل‌آویو محتوای آن را فاش کند و کارزاری رسانه‌ای علیه آن به راه بیندازد
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/15153" target="_blank">📅 17:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15152">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">پاکستان خواستار تعویق انتشار متن تفاهم‌نامه شد
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، در گفت‌وگو با CBS اعلام کرد که طرف پاکستانی درخواست کرده است متن کامل یادداشت تفاهم (MOU) فعلاً منتشر نشود.
وی بدون ارائه جزئیات بیشتر گفت که به درخواست پاکستان، متن این سند به‌طور موقت محرمانه باقی خواهد ماند.
@withyashar</div>
<div class="tg-footer">👁️ 88.1K · <a href="https://t.me/withyashar/15152" target="_blank">📅 17:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15151">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">سوئیس: امضای یادداشت تفاهم ایران و آمریکا با حضور نمایندگان ۴ کشور ایالات متحده، ایران، قطر و پاکستان برگزار خواهد شد.
بیش‌از ۲۰۰۰ سرباز امنیت محل امضا را تأمین خواهند کرد و برای تضمین امنیت، منطقه پرواز ممنوع اعمال خواهد شد.
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/15151" target="_blank">📅 16:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15150">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تسنیم: اختلال خدمات بانکی ادامه دارد , تجهیزات شبکه فرسوده هستند
@withyashar</div>
<div class="tg-footer">👁️ 88.9K · <a href="https://t.me/withyashar/15150" target="_blank">📅 16:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15149">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ایران امروز یک تفاهم‌نامه با شرکت سهامی خاص هلی‌کوپترهای روسی برای ۲۰ هلی‌کوپتر سری mi-8/17 امضا کرد (۴ تا از آن‌ها قبلاً قرارداد بسته شده است) که باید تا مارس ۲۰۲۷ تحویل داده شوند تا برای مقاصد اطفاء حریق، انتقال پزشکی و نجات استفاده شوند
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/15149" target="_blank">📅 16:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15148">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=W3JlkN1oCLSGwGgZXNpoVlar87oTMYFFuGTtDmk90S2Oi1kw_ItGP_tdr-gKcX6kf_kNxgFVsBjgo5D9Pmf8RIgEDYfTtH2zzOrimOd_OV-gQm6qz-7n88YWkIPUYiTWAvU68nQjHSp4ltG6lY8QLccVFr40R-LEY-KfPskYL0uaWZjiP7O9ZNrKvA82lXwOi4-K3oW4YuUojAOXzEQSpWAU2sdVUMgo0QtZwSVBlD9BAkXsh18WdAKq_EQApnHw6tTCvyn-sKkLxpqxkQGlZbc8eyvTE7_4BVaGqP-R3ft3hbRWt-nRMV4lcoF0371PjCbnSVKx2wg0ky-G4mtB8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fff486d39a.mp4?token=W3JlkN1oCLSGwGgZXNpoVlar87oTMYFFuGTtDmk90S2Oi1kw_ItGP_tdr-gKcX6kf_kNxgFVsBjgo5D9Pmf8RIgEDYfTtH2zzOrimOd_OV-gQm6qz-7n88YWkIPUYiTWAvU68nQjHSp4ltG6lY8QLccVFr40R-LEY-KfPskYL0uaWZjiP7O9ZNrKvA82lXwOi4-K3oW4YuUojAOXzEQSpWAU2sdVUMgo0QtZwSVBlD9BAkXsh18WdAKq_EQApnHw6tTCvyn-sKkLxpqxkQGlZbc8eyvTE7_4BVaGqP-R3ft3hbRWt-nRMV4lcoF0371PjCbnSVKx2wg0ky-G4mtB8oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران: دلیل پایین ماندن قیمت نفت این است که هر شب کشتی‌هایی را از بین می‌بردیم که حتی شما از آن‌ها خبر نداشتید.
دو روز پیش، سه روز پیش، یک ماه پیش، ۲۲ کشتی را از بین بردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی را از بین می‌بردیم. هیچ‌کس این را نمی‌دانست.
نیروی دریایی ما کار بزرگی انجام داد. هیچ‌کس نمی‌دانست چه اتفاقی می‌افتد. به همین دلیل نفت به ۳۰۰ دلار در هر بشکه نرسید؛ بلکه به ۱۲۵ تا ۱۵۰ دلار رسید.
حالا قیمت آن ۷۲، ۷۳ دلار است. شنیده‌ام که الان حتی کمتر از این است
@withyashar</div>
<div class="tg-footer">👁️ 91.7K · <a href="https://t.me/withyashar/15148" target="_blank">📅 14:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15147">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ترامپ: با احمد الشرع، رهبر سوریه، درباره مقابله با حزب‌الله گفت‌وگو کردم.
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/15147" target="_blank">📅 14:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15146">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=YrKOb1kjQfqSlk1N4VXBR5L7Azu_PcgCyiTIS5XgkWjYd6PV7sq6Wy2BiJJHfj9eML7AheosvARlYi99G5X7WRfq5bdWtZoubP1BhzfAWYCRRo1TuWZhuds6_r6vzSq7e1WLNLQQ4OnJpa0YErhSc_BxxdgpeIfT59slD1WjLxaGbVSFn71tchNU4PPs0qtYWyT6uDCwHaf7KUZ5cmHhewfzXC1jbDu34JBTlW7p4K5whkELXiFTJoAkuw7sxHS5Che_ArsWhfdPP-meYJFhsBt0GBPJuMOGkaVCvOij6aZIXoWdh5IkcWtRZSydnzm-4OrAlW4_nBq_QkAGroCczA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10b0e16f.mp4?token=YrKOb1kjQfqSlk1N4VXBR5L7Azu_PcgCyiTIS5XgkWjYd6PV7sq6Wy2BiJJHfj9eML7AheosvARlYi99G5X7WRfq5bdWtZoubP1BhzfAWYCRRo1TuWZhuds6_r6vzSq7e1WLNLQQ4OnJpa0YErhSc_BxxdgpeIfT59slD1WjLxaGbVSFn71tchNU4PPs0qtYWyT6uDCwHaf7KUZ5cmHhewfzXC1jbDu34JBTlW7p4K5whkELXiFTJoAkuw7sxHS5Che_ArsWhfdPP-meYJFhsBt0GBPJuMOGkaVCvOij6aZIXoWdh5IkcWtRZSydnzm-4OrAlW4_nBq_QkAGroCczA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ‌ در‌کنار ژنرال السیسی (واقعی): فراموش نکنید، هیچ‌کس هرگز به اندازه من با ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری از افراد دیگر انجام می‌شد.
@withyashar</div>
<div class="tg-footer">👁️ 87.7K · <a href="https://t.me/withyashar/15146" target="_blank">📅 14:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15145">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ترامپ: قابلیت پرداخت فقط یک حقه دیگر است. آنها کلمه «قابلیت پرداخت» را ساختند
@withyashar</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/withyashar/15145" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15144">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم @withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15144" target="_blank">📅 14:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15143">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامپ: یادداشت با ایران نهایی نیست. اگر از توافق خوشمان نیاید، دوباره به بمباران بازمی‌گردیم
@withyashar</div>
<div class="tg-footer">👁️ 86.9K · <a href="https://t.me/withyashar/15143" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15142">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpK5qlBBecbVO7ZA7EfakHiZCin6lMINi0XL9b8_47wUQbT0L-9_aZqdTMWSTb8NpVoWHduykRfnuEEBjlbUKHsdd9roGHaz_w-pECmBEGtr4jdeX8KOVPrjZzkyQs05tcHPBn243XTf9lO-36ynCYPugqPdvjap0Koe2bmJMSb1jPL3m68mBnE7C7rVkYJdTL3YJs2f-3uOqbSTHlH9S6RlpUfXiQedTHMGJo3imN14XJ-EwqVshZBbkzEUMqi2-PLbrgSzKZxb8xuPBlwLbhxcSD9mWhhaVKI2ipBwjmpVd1yh7PTcYTyHdlx1xdzsNVbKAXl4qYWLXIloNjDKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اندرو تیت که ۱۰۷ بار لیکویید شده، دوباره در صرافی هایپرلیکویید با اهرم ۴۰ و حجم حدوداً ۴ میلیون دلار، روی بیت‌کوین پوزیشن لانگ (خرید) باز کرده و باز هم بخشی از سرمایه‌اش (۱.۳۵ میلیون دلار) لیکویید شد.
اگه قیمت به 64,626 هزار دلار برسه کامل لیکویید می‌شه.
نرخ فعلی بیت‌کوین: 64,800$
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/15142" target="_blank">📅 14:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15141">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=cNTRAZd6TLftS1X0jv9EncvUZkVJwhjZofLUbrJh-_6ee6Vl1zeMbWQOArjebFNzuzQWPzD6FwoYXJ2_Opd4Snj9fjpbumq1U1tItZ0j8945iTe0X-dB11NdSImoYSuFtED1hZ88hp3mrmfDKDeBNe2kBwSLm3xDTjMxUSPn8y5Qy4ma0torX0yJAOcb5IpSp9khgNd5Qn5RcYb6GsaSCl55Z8l_FG7WY7TEm4hZySKuVP7O7E8KTrK9KCFU9seujajFRZoR9-X0bNaPLCCLM9zceiwTHgxfh34mLBLz5qFJWXzBL9h2v2PAmV5tuSJVfttNjIOmXt4h5ishNyr0zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d627cfcdc.mp4?token=cNTRAZd6TLftS1X0jv9EncvUZkVJwhjZofLUbrJh-_6ee6Vl1zeMbWQOArjebFNzuzQWPzD6FwoYXJ2_Opd4Snj9fjpbumq1U1tItZ0j8945iTe0X-dB11NdSImoYSuFtED1hZ88hp3mrmfDKDeBNe2kBwSLm3xDTjMxUSPn8y5Qy4ma0torX0yJAOcb5IpSp9khgNd5Qn5RcYb6GsaSCl55Z8l_FG7WY7TEm4hZySKuVP7O7E8KTrK9KCFU9seujajFRZoR9-X0bNaPLCCLM9zceiwTHgxfh34mLBLz5qFJWXzBL9h2v2PAmV5tuSJVfttNjIOmXt4h5ishNyr0zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‎بخشی از سخنرانی قالیباف که تو رسانه‌ها وایرال شده
دیگه ساختار مدیریتی کشور از فردمحوری خارج شده و گروهی تصمیم میگیریم.
@withyashar</div>
<div class="tg-footer">👁️ 89.5K · <a href="https://t.me/withyashar/15141" target="_blank">📅 14:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15140">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وزیر دفاع اسرائیل کاتز: تمام روستاهای نزدیک به مرز لبنان به صورت سیستماتیک ویران می‌شوند.
@withyashar</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/15140" target="_blank">📅 14:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15139">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فاکس نیوز: ترامپ به زودی درباره توافق ایران کنفرانس خبری برگزار می‌کند
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/15139" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15138">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تسنیم: متن توافقنامه به صورت کامل در روز جمعه و پس از امضا منتشر خواهد شد
یک منبع نزدیک به تیم مذاکره‌کننده   گفت: تفاهمنامه همانطور که پیشتر اعلام شده ۱۴ بند است و موضوعات مربوط به ۱۴ بند نیز بارها در رسانه‌ها مطرح شده، اما جزییاتی که در بلومبرگ‌ درباره هر بندی آمده است در موارد قابل توجهی ناقص است.
@withyashar</div>
<div class="tg-footer">👁️ 91K · <a href="https://t.me/withyashar/15138" target="_blank">📅 12:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-15137">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKkSCvAL905A_LlgRg5RPAMM85ob5jTK9xITUh5J0PbRlkWiq0nRJOcz9Zco_d5Xt6e1jM7K700a_63_3_LoNJTKlfac5WF0vvGDfPVCl4z6Z7sFrNcZBI_v6S7_A_0j06DszsDdiZhUge1DVZdJjYffOM-RRXMS6PTtLm6FcTC5s_qgVcYWQXhu7uMp94V3UtUo4RYmXofCZAx1JQJzCLFHcvjhg0zglKG77FoPwuM-AL9XMx3JibWugEtjFbThRAhTY9ZfclfrUZXAYR61Sqm5jFeKpiAuucfZ7PbSNyL-e3T0h53CN7vsNFsGaARJ1WOaQ8-mz_P0LsXMojAaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودرو پورشه سردار آزمون در کرمان توقیف شد
به گزارش تابناک به نقل از ایسنا، سرهنگ اکبر نجفی ۲۶ در تشریح این خبر گفت: خودروی مذکور که به دلیل تخلفات قانونی و برابر با احکام صادره در لیست توقیفی‌های مصادره اموال سردار آزمون قرار داشت، توسط گشت‌های محسوس و نامحسوس یگان امداد شناسایی و پس از طی مراحل قانونی، به پارکینگ منتقل شد.
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/15137" target="_blank">📅 12:47 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
