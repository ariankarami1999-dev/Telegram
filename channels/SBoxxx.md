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
<img src="https://cdn4.telesco.pe/file/tH7D_vfb_xFyvns1-X4wHx-36w1UWVO1rWaZTMloPuodItnEVMQDS3WNFfHAJEhA220J2lQ2TlTZ_cQNLAkdE58RY24wQ7D1GHkNl-WfkQ9_CP_4bVCznuDjMK3mUopaeDmhJetyoCCKmNHiuu1y6-_qPeDNelCsrY6qgwYO37xJZzAxIWiDue55UfOdr65iiCDMpuX0qvw_ACU-BejIhLXJ6pcTQETCGZR4btl5U8oF57dZ9M-RUL-1JP7TVxU0cOAno9D-u8238rKMkhww7wR6cXXdVewq5AEwXYz91vnGN8hFo2rbG5f14QbUXNjCa00IdMbrJ-iimtuatOtPpQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.7K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-11 01:22:27</div>
<hr>

<div class="tg-post" id="msg-20451">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFaRlRSeCcfBOf5fX4XN26UIrIm_HzS0YJLNNQgN4kh7Lh575whY42Y_q-8agkcvsNGB052einm5bL6TNp-Rk40KbrPCQTbzVoGe-THvOfJfuQl5iya99k2sTd2Q9FxCszoJPzN2JQkncrwNC3DJ2GxI6LehgOnyThRvKQ3adKT7KpN7h1fHasaLdKEB55uxaDR1KfZwHZkyr2qcQo0eMloUX-h5STKQ7CITyhu_EXg23UI38jRThoDMvG6hD9S-Gb1DW5ukq6Q8VCWUtTwWw0tJKvH67QNRgF9s71DhXYq5uWLfFUcNWRFi-PRaBedNwfPRmS3ZV3az4nD7AXE7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«سپر آشیل»؛ ورود یونان به عصر دفاع هوایی چندلایه   یونان و اسرائیل در ۳۱ اوت ۲۰۲۶ قرارداد تاریخی «سپر آشیل» (Achilles’ Shield) را به ارزش حدود ۳ میلیارد یورو امضا کردند؛ توافقی که آن را می‌توان یکی از مهم‌ترین پروژه‌های دفاعی مشترک دو کشور و نشانه‌ای از تعمیق…</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/SBoxxx/20451" target="_blank">📅 00:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20450">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 1.17K · <a href="https://t.me/SBoxxx/20450" target="_blank">📅 00:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20449">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این هم موج شماری
😂</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SBoxxx/20449" target="_blank">📅 00:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20448">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بالگردهای ارتش آمریکا برای انتقال زخمی و کشته های خود در اردن به پرواز درآمده اند.</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/SBoxxx/20448" target="_blank">📅 00:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20447">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">#WHEAT — D</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SBoxxx/20447" target="_blank">📅 00:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20446">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eadj9qdjIHLlcY7JyxTCAHjHHtvRTP66KPiXewMfhat74fkUsI3jC472xSpvlVVwRDWq6oaeVHFrxumWB41s-OLYPSiPUzji7zLJ5L8_deNNfPtHJ8wygOHqZlpjMuxx6bOAB9cwGW3K1o0JiwKxKxlIm1opGyHCq_E65eD44SB0njkap9ekhlSeaXPajKzc3-njzjHkb9N9FI-ewwEg1NCb6NGulWgBPOXV7hHDHSK_XR3xDDr7v29xdCFv5oFurWr2XjmoBYIuoRW2ZXAceuUQMxbS4dhIwS2c62v9m15ONU7Vpi6IoFYOCBb40ZW-6RekKtzSblVsDtKfWA8xEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#WHEAT — D  به نظر می رسد گندم هم دارد همان مسیری را می رود که نقره 3 سال پیش در آغاز آن بود...</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/SBoxxx/20446" target="_blank">📅 00:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20444">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gr0VI5iGuCIUXNbsI57altuhE_q4z5bN7q4JMFK5I4SXvpM0wZHd6dIYv-dDvL7Kg13A17Ml_dfVch01eJg0ymZ0pF6TFrpmR2xvpUbBfQOlP64J-XgmAOL_YbSYCGHeVXpeA4WjBWBAeAWw_Dz7pbsFmrqWvj--33WJmH4GRx1EMSo-LQqp8igANl_fM8Anz0Dp56iZlH08A9QyHF74tUMzTXpo-v9ZbQgNyjzT6uFQyA-7j_WInwqjM3rwrVbFZP_eBnRbp8k-vD2H9zucBzJxTM3ZmdtFciwXOSsi86cS-ykpql_qykEbrSpc9b3mAzdOdS5MdwYPPauDvgnMOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=hENs3IUTm3RLhLnh-2Hu7-paIPfnzTug1zh1grnBRIJHTopPRuVaP9QnyH_XkJOVh-R0mm91oaEeZCVcdX0rMXCcpGL90SN0fWAsxCeHXMtOqvnmXA3Ji6DBdnVcj-wFLoUMhATRs3Djd1A8gmmzTPzxSuoOeSmu9rFCeohJ7Hcr8KqjfgY7T7XFpdvzSMN-PfOJfdLtIKcAAinHZLeyVRDL4NGj50OhaeAdh2U-88DG-T4vhO-Z_hGs4rdA9-aDUv4Vp0HxLtga5aCxJrAXzuGHRVVd4BHHli19aetkBRJjl9iLm7NM0ml4LfkPd-B4FxuPnMwQjNzdXsWobaCAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42fd12b2d1.mp4?token=hENs3IUTm3RLhLnh-2Hu7-paIPfnzTug1zh1grnBRIJHTopPRuVaP9QnyH_XkJOVh-R0mm91oaEeZCVcdX0rMXCcpGL90SN0fWAsxCeHXMtOqvnmXA3Ji6DBdnVcj-wFLoUMhATRs3Djd1A8gmmzTPzxSuoOeSmu9rFCeohJ7Hcr8KqjfgY7T7XFpdvzSMN-PfOJfdLtIKcAAinHZLeyVRDL4NGj50OhaeAdh2U-88DG-T4vhO-Z_hGs4rdA9-aDUv4Vp0HxLtga5aCxJrAXzuGHRVVd4BHHli19aetkBRJjl9iLm7NM0ml4LfkPd-B4FxuPnMwQjNzdXsWobaCAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/SBoxxx/20444" target="_blank">📅 00:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20443">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-tr7vKsAFTaqWQ3CT8W0BsUNVrD1kLzvFY1j20_e4mjfObnOTZcuAbfmkIhexX_eYGwKm76XpqKims4gdHPM52RNTrDY1i5NntXwTHUdnhD3-poWOo6FAUY-duSk_PsaRvD35zOQyeBGuEr0aIbhVQe6IdwJet7yj3CaN98NFb8GQ1iUvUPd50fg1QzggD3yiXgBogSxLjfVl8Kh6GCcDRER8ZkGPGXZ8hGapUcYX1s02vwYXf2I9ukEJxVFEMFdnLZ2VNfagcxbprj1yiCjsiwUXxW9nJwuwMgSMJJ3jQmwW1eGQXVd8ro8CkVUldzUxPmZ1SdCdWUkq8nUnwxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/20443" target="_blank">📅 00:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20442">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb8-6UbNwn4bcp2r7W0rYbdmopN2JtJEmtVOIdCd9h2HrJsYCJ-dO61KHpBgKPBDQ8x2x6VnpGyHV8_R93_wL0c9mf9A8-dPD-x5Hc3JU0twACzUAl5lIEMlS_tcy3Jy54JwX8EgJRkdTKFelLaUkS8vIJIAUG6VCMNEIc0R0RlJRu7Utftib3-9eAd2NdzpYYDQcIio_i_Z6qPD-aW4tzPqVulwfax9hZzqQlTT0EvZVMs0awKL6mTGyAg53Vmonxf2Mv3oPcd3rtcg5POnyeCQsZZyXo6FHYa68BEKkD7NxTuWu-5kiD72BK0Updxc2LQzf8yCCzSOBBxnEvk0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفاً یک نفر لفت بدهد میخواهم معنی 10666 را از آرش بپرسم. ممنون</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/20442" target="_blank">📅 00:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20441">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
قَاتِلُوهُمْ يُعَذِّبْهُمُ اللَّهُ بِأَيْدِيكُمْ وَيُخْزِهِمْ وَيَنْصُرْكُمْ عَلَيْهِمْ وَيَشْفِ صُدُورَ قَوْمٍ مُؤْمِنِينَ
🔹
ملت قهرمان و بپاخاسته ایران اسلامی،
ارتش تروریستی و شکست خورده آمریکا، عاجز از رویارویی مستقیم با رزمندگان اسلام با حمله وحشیانه به یک منزل مسکونی در سیریک، محل مجلس عقد دو جوان پاک را به خاک و خون کشیده و با به شهادت رساندن و مجروح کردن نزدیک به پنجاه نفر از مردم عزیزمان خاطره وحشیگری مدرسه میناب و ورزشگاه لامرد را زنده کرد.
🔹
رژیم کودک‌کش آمریکا در این حمله جنایتکارانه یک بار دیگر با به شهادت رساندن چندین نفر از جمله یک کودک، عمق کینه‌توزی و دشمنی خود با مردم ایران را آشکار کرد.
🔹
در پاسخ به این شرارت سبعانه، رزمندگان دلیر نیروی هوافضای سپاه در موج دوم عملیات تنبیه متجاوز "با رمز مقدس یا رسول الله (ص)"
با حمله سنگین موشک های بالستیک به پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تیتین، واقع در سواحل خلیج عقبه
، تعداد زیادی از نیروهای آمریکایی را به درک واصل کرده و چند تاسیسات مهم و بالگردهای هجومی دشمن را منهدم نمودند.
🔹
عملیات انتقامی نیروهای اسلام
ادامه دارد
.</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SBoxxx/20441" target="_blank">📅 00:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20440">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">باز ما یک سفر آمدیم همه چیز به هم ریخت....حتی سفر درمانی ما هم بی عوارض نیست چه برسد به تفریحی</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SBoxxx/20440" target="_blank">📅 00:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20439">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ساعتی قبل یک خودرو وارد تجمعات شبانه در خیابان اقبال لاهوری (مشهد) شد و جمعیت را زیر گرفت، چند تن نیز کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/20439" target="_blank">📅 00:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20438">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/20438" target="_blank">📅 23:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20437">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار فوری | اخبار جنگ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=j9pBiVJkUFQBP-WdtJwVHTnaltruAB3sDfxjwUsZeyfnDhaAppoHA7dhmxLnyzVvnhICd9K9qHlAQVI-Sq5qMokH_W5H3GoHB_wscQfqpjtGpPNT8vxqK-wA4_N_X5En4jG4-kab9r0F3eQZbc4fJQe8hnTyQX_pzCczIkaXzJbc7dD2MGuvcBr8TuyVJ0vqgKQgwaELYLZcSXVW7JNf5UA7AS5_qMXU4avNMhaIVKmFJBGP0wjbEhY7ikjZVrQeSIlQpYnMMg18DSoLHn75EGSlIHHNUu_jAAc8kC2-BLQPXvKqnKMqJ0cHykwG4YmZ3W-TUrdFL-_C44tAH4IiDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10aa2a3f52.mp4?token=j9pBiVJkUFQBP-WdtJwVHTnaltruAB3sDfxjwUsZeyfnDhaAppoHA7dhmxLnyzVvnhICd9K9qHlAQVI-Sq5qMokH_W5H3GoHB_wscQfqpjtGpPNT8vxqK-wA4_N_X5En4jG4-kab9r0F3eQZbc4fJQe8hnTyQX_pzCczIkaXzJbc7dD2MGuvcBr8TuyVJ0vqgKQgwaELYLZcSXVW7JNf5UA7AS5_qMXU4avNMhaIVKmFJBGP0wjbEhY7ikjZVrQeSIlQpYnMMg18DSoLHn75EGSlIHHNUu_jAAc8kC2-BLQPXvKqnKMqJ0cHykwG4YmZ3W-TUrdFL-_C44tAH4IiDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
موشک بالستیک سپاه به سمت اردن، که از اسرائیل مشاهده شده است
⭐️
@AkhbareFouri</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/SBoxxx/20437" target="_blank">📅 23:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20436">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یه کویت مون نشه؟!</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/SBoxxx/20436" target="_blank">📅 23:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20435">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مرندی ذوالاکتاف:
با توجه به اظهارات ترامپ و بسنت، به نظر می‌رسد که روزهای رژیم‌های خانوادگی عرب در خلیج فارس به شماره افتاده است. آن‌ها نمی‌توانند از جنگ پیشِ رو جان سالم به در ببرند.</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SBoxxx/20435" target="_blank">📅 23:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20434">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">جهت نوسانات رو شاخص درست تشخیص داد (رو به پایین) اما شدت ریزش قیمت با تحلیل ما سازگار نبود.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SBoxxx/20434" target="_blank">📅 23:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20433">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2Z9gmDuZlStXPS4oH-cfFKFsp_8-8xSKSexA7x3RnZ4JEsk_Om9mFbdGqB3V3Jz70_J-k0YrGW5bkcc_xAFfR8zi5n43p_WjxH1hS9g9NYftY_kdZA6l285dFztNVVAKHPAZvvYJ0d2V5jS_l9nrDrGZpwlR-bQtutxeqg1HFx5AaIGV9PEtMfGhu0xkG87InlD_SfN4SB-kohDpApXgnb5rkHvtxJXUr9Ob_b13pBXPm67YYbX6bR0gRwD4xehTCu6deV13HrsktDFihNT-I2IeMOE9ZY9T7Pg0xEJb7W85lOn45hmOLGpyp5K5Jrz1CGU8c3iVm9t_TFkaPM88g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.  با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/SBoxxx/20433" target="_blank">📅 23:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20432">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شلیک موشک از تهران!</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/SBoxxx/20432" target="_blank">📅 23:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20431">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان:   همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SBoxxx/20431" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20430">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان:
همهٔ اعضای شانگهای بدون استثنا تجاوز به ایران را محکوم کردند</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SBoxxx/20430" target="_blank">📅 23:13 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20429">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یک درس دیگر هم این بود که در جنگ با آمریکا و اسراییل، باید بیشترین موشکها و پهپادها را توی سر‌ همین جهان اسلام زد تا بهتر بشود جلوی شیطان بزرگ ترسمان ریخته بشود.</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/20429" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20428">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">حمله ایران به اردن</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20428" target="_blank">📅 23:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20427">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">معاون سیاسی و امنیتی استان هرمزگان: در حمله به یک مراسم عروسی در سیریک دو نفر شهید و تعدادی از افراد نیز مجروح شدند.</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/20427" target="_blank">📅 23:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20426">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سقوط یک پهپاد MQ-9 آمریکا</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/20426" target="_blank">📅 23:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20425">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">اگر آمریکا باز هم به تجاوزاتش ادامه دهد، خمین را با خاک یکسان خواهیم کرد.</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/SBoxxx/20425" target="_blank">📅 23:04 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20424">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمله آمریکا به همون همیشگی!
سیریک
!</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SBoxxx/20424" target="_blank">📅 22:19 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20423">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/20423" target="_blank">📅 22:18 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20422">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انفجار در همون همیشگی !
اربیل
!</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20422" target="_blank">📅 22:17 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20421">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حمله به عسلویه!</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20421" target="_blank">📅 22:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20420">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گفته می شود بقایای موشک در خود خمین فرود آمده</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SBoxxx/20420" target="_blank">📅 22:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20419">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آژیر خطر در قطر!</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SBoxxx/20419" target="_blank">📅 22:07 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20418">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7gba8nAQt44qZ7TFjasTmITI3Mgymv9veEjDeLVRxvJRiBpx_79gieKzfiL71GD8jAytNWrVJ3BPfcCP9NXVOAI9HK-5a3wxVbhmRR7AeCeHuKNaUI4LijQWSt_pmk_T7KDFxiO7lgYPfwzLAqySG9gzrA_41GFWPXXsnhEoTVRd9mlpE1yfEFMfYG6MFcbB-vvm6HIvYc1DlJzH9MrzEXweLcj1MuXPs8YSJ-Vu9kVwsu5-owJVlNQPn_IaQjISPdQ-zwm8350NuVMSxkwr9YNqFQ8ct0IFFRPs_eyz_navMg8HmzqRAfjXQmLFCdV_xQrpGbtTtmIXF3IDNImhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آن دو هواپیما نیستند پس احتمال حمله به تهران هم هست.</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20418" target="_blank">📅 22:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20417">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-text">‏ترامپ:
حملات جدید آمریکا سیستم راداری ایران  و کارخانه های تن ماهی را هدف قرار داد
@Piknikanalyst</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SBoxxx/20417" target="_blank">📅 22:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20416">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">حالا که همه چیز را دادید رفت، دستکم به رستم تهمتن بگویید دیگر نزند!  کور شد بدبخت!</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/20416" target="_blank">📅 21:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20415">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/SBoxxx/20415" target="_blank">📅 21:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20414">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دقایقی پیش فرودگاه جیرفت مورد حمله هوایی قرار گرفت.</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20414" target="_blank">📅 21:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20413">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">منظورم موشکی است که از خمین بلند شده بود.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/20413" target="_blank">📅 21:41 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20411">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">موشک های بالستیک از ایران شلیک شدند</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/20411" target="_blank">📅 21:38 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20410">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:  «مجازات شدیدی در انتظار متجاوزان است.  آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20410" target="_blank">📅 21:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20409">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
«مجازات شدیدی در انتظار متجاوزان است.
آمریکایی‌ها به خاطر حملات جدیدشان پشیمان خواهند شد.»</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/20409" target="_blank">📅 21:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20408">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
«ایالات متحده همین حالا در حال حمله به اهداف ایرانی در نزدیکی تنگه هرمز است. این حملات گسترده و قدرتمند هستند و در واکنش به تلاش ناموفق ایرانی‌ها برای کارگذاری مین‌های دریایی در تنگه هرمز انجام می‌شوند؛ تنگه‌ای که در حال حاضر هیچ مینی در آن وجود ندارد (تمام مین‌ها کاملاً پاکسازی یا منفجر شده‌اند).
همچنین در واکنش به شلیک هشت موشک از سوی ایران به پایگاه نظامی ما در اردن که همه آن‌ها با موفقیت سرنگون شدند.
اگر کشور شکست‌خورده ایران در واکنش به این حمله کاملاً موجه، اقدام تلافی‌جویانه‌ای انجام دهد، بار دیگر و در سطحی بسیار شدیدتر و گسترده‌تر هدف قرار خواهد گرفت؛ اما این بزرگ‌ترین حمله از همه نخواهد بود. بزرگ‌ترین حمله همچنان در حال آماده کردن است و هنگامی که به پایان برسد، چیز بسیار کمی از جمهوری اسلامی ایران باقی خواهد ماند!»
— رئیس‌جمهور دونالد جی. ترامپ</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/20408" target="_blank">📅 21:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20407">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دور جدید حملات آمریکا</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/20407" target="_blank">📅 20:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20406">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تسنیم:
برخی منابع از شلیک موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه خبر می‌دهند</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20406" target="_blank">📅 20:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20405">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">– گزارش‌های تأیید نشده حاکی از آن است که موشک‌های زمین به زمین دیگری، احتمالاً HIMARS یا ATACMS، از بحرین شلیک شده‌اند.</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20405" target="_blank">📅 20:14 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20404">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امروز ساعت ۱۲ ظهر به وقت شرقی، نیروهای ایالات متحده شروع به حمله به اهداف نیروی دریایی سپاه پاسداران انقلاب اسلامی (IRGC) در ایران کردند.
این حملات پس از تلاش‌های اخیر IRGC برای حمله به کشتی‌های تجاری در تنگه هرمز و علیه نظامیان آمریکایی مستقر در منطقه صورت گرفته است.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20404" target="_blank">📅 20:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20403">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">به نظرم نیازی نیست چون خود آمریکایی ها هر هفته چند بار پیش دستی می‌کنند</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20403" target="_blank">📅 20:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20402">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">— سفارت‌های ایالات متحده در اسرائیل، قطر و عراق هشدار امنیتی صادر کرده‌اند و از آمریکایی‌های ساکن در سراسر خاورمیانه خواسته‌اند در میان نگرانی‌ها درباره تشدید بیشتر منطقه‌ای، «هوشیاری بالاتری» به خرج دهند.</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SBoxxx/20402" target="_blank">📅 20:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20401">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">— انفجارهایی در بندرعباس، سیریک، قشم، چابهار،لارک، جاسک و میناب گزارش شده است.</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20401" target="_blank">📅 19:49 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20400">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انفجار در بندرعباس</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/20400" target="_blank">📅 19:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20399">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SBoxxx/20399" target="_blank">📅 19:25 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20398">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس مجلس ایران از شهروندان خواست مصرف بنزین را کاهش دهند</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20398" target="_blank">📅 19:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20397">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20397" target="_blank">📅 15:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20396">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر راه:   رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20396" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20395">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزیر راه:
رادار نداریم و مجبوریم پروازها را به صورت ذهنی راهنمایی کنیم</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20395" target="_blank">📅 15:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20394">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار فردایی تهران
⏳
213,600 فروش
🔴</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20394" target="_blank">📅 13:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20392">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏نبویان:   اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/20392" target="_blank">📅 13:10 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20391">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏نبویان:
اکنون بهترین زمان برای حمله پیش‌دستانه به منافع امریکا است</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/20391" target="_blank">📅 13:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20390">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/20390" target="_blank">📅 13:00 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20389">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20389" target="_blank">📅 12:21 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20388">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان…</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/20388" target="_blank">📅 11:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20387">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZcvO9vFKj1rHIYEeMeWzvchHQ76IsPsSW5NSZGxCvuQiQiXiNcbooYdW4h7Aa8GjsBk5xV83u1UB_x3ZkPGR8BhwMHX6xcjryjd_5ZD8Bn8LBi6zY6dzZvP4IKPTKgECLh885sdEbu29Fom2HjMFUKuagerHurCIF0YXYdRZXuX6XGeqSHrfALIgTawdZVVASC1ufqhD5E4cHNAHG8XDyAkQ_c4ExkjUJdWR-IWfSkkTy5CSpE0dzNzNuQkMIED4Hbsx28stlXMP6cXnQp4deySQBUyxBX9wi9KlHsU9f_mtBsvWrFp8iZHy80YdJh5iOW6V6QeLCMLPuUYrCcuow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آمریکا در جهت ضربه به تمام فرماندهان سپاه آماده می شود ! عملیات روانی همزمان با برنامه جدی برای ترور !
⏺
در لیست تهیه شده توسط دپارتمان جنگ ایالات متحده، فرماندهان بسیاری از نیروی زمینی سپاه، قرارگاه های این نیروی و حتی فرماندهان سپاه های استانی و فرماندهان نیروی دریایی دیده می شود! حتی سرپرست فعلی سازمان اطلاعات سپاه نیز در این لیست می باشد.
⏺
هدف آمریکا از تهیه این لیست اجرای یک عملیات روانی و همچنین دریافت اطلاعات دقیق از وضعیت این فرماندهان می باشد. همچنین به نظر می رسد آمریکایی ها با انتشار زودهنگام و غیر دقیق این لیست عجله در دریافت اطلاعات دارند .
⏺
گزارشی مبنی بر نشر این لیست در مجموعه های خاصی وجود دارد که مرتبط با اعضای نیروهای مسلح هست، نکات بسیاری وجود دارد که فکر میکنم اگر بگویم برای خودم دردسر ایجاد می شود پس فعلا از گفتن آن پرهیز می کنم. اما جدی بگیرید اوضاع را !
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20387" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20386">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⚔Iranian Militarism⚔</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtQwQm2i5bvh6k8cmiqowSSXiLbQJdY7pu-q4U2-_3DGYNBSQVZ6ZxatCYHJKsnYrwoMw7mPLoWg08FELot3-JaifcteYKmxyrO8tr0gkkqmx9-VHo20Kea2jxKbwpf6zd651aLMy2d48mNNNGEdnzRefwPhr79VjTWJanDH0YWy6V301tRKFMs9tXs9GSrLfvyvlWNhyXrX_Go1EEiP5YAKbix363IAcZyk_vyyh987A4MbLSX5PblNdYZ1ZV56hBpfStTsWA2IZ_iCTKFry3v-1VJxql-AvKWamsW6n7RSkfvU3akY-9MxhsE0XHTk8UWsWhPnIvwCR6TJvw--BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویر سردار حسن زاده در صفحه وزارت جنگ آمریکا به عنوان فرد ترور شده !
🚫
دپارتمان جنگ ایالات متحده سایتی برای دریافت اطلاعات از برخی فرماندهان ارشد سپاه تهیه کرده است! در این سایت لیست قابل مشاهده است که صرفا به چند فرمانده به صورت پراکنده می پردازد، نکته جالب اینجاست روی تصویر شهید خادمی علامت ضربدر قرمز خورده است به این معنی که به شهادت رسیده است! حالا جالب تر اینجاست روی سردار سرتیپ حسن زاده فرمانده سپاه محمد رسول الله تهران نیز همین ضربدر دیده می شود!
Join us |
@Iranian_Militarism</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20386" target="_blank">📅 10:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20385">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve-VO5cugk5gyB0VkJDKiVju8vUDN6NJXZyUL9O1WmeNUHprax-vbOyme_epoRC39s1XpCLjUJ7tKKb4i4LXVmRnnTjS8IeZpyQYNFQdGXdM6DpMzIZnFOfg3U3BSf4GC-_WCym1epU1D-Z-YTZTSI1K6Eo0urZdZmc38u0roTz26dtERwTQ2ylD-kxPZCkFPgVv-FAkz2xjjQxQfww8O6G08j85oO0rauuzE2v9WFHS3hW8HcFZ0A5g1LrVlAITUzDIFEyh2QH01vxsjAF-_b0InSF6zuoOyr_7-wF4wxPBv1sW0Wt7zQjsmWVqn_gvEvTYgO-J9gzkCIUf2GFOvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح میانه بالا قرار دارد و بازار رنج و کم نوسان پیش بینی می شود.
با توجه به روند عمومی نزولی در 1-ساعته، فروش در سطوح مقاومتی (4477) بهترین راهبرد است.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20385" target="_blank">📅 10:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">این چیزی که ما اکنون تجربه می کنیم عملاً نوعی «تجربه نزدیک به زندگی» است.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/20384" target="_blank">📅 01:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار در سیریک</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/20383" target="_blank">📅 01:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ایران یک تانکر نفتی سعودی را در تنگه هرمز متوقف کرد.
بر اساس گزارش خبرگزاری فارس، یک تانکر نفتی بزرگ سعودی در حالی که از مسیر جنوبی تنگه هرمز عبور می‌کرد، متوقف شد.
ظرفیت این تانکر 2 میلیون بشکه نفت است.
طبق این گزارش، در حالی که این کشتی از تنگه عبور می‌کرد، ناگهان سیستم شناسایی خودکار آن فعال شد. فعال شدن ناگهانی سیستم AIS نشان می‌دهد که یا به این کشتی دستور داده شده بود تا موقعیت خود را اعلام کند، یا اینکه در شرایط اضطراری در تلاش برای اعلام حضور خود بوده است.
امروز، سازمان UKMTO گزارش داد که گزارش‌هایی مبنی بر وقوع یک حادثه امنیتی مربوط به یک تانکر نفتی دریافت کرده است.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20382" target="_blank">📅 00:48 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">- یونان و اسرائیل در آستانه اجرای توافق‌نامه‌ای به ارزش ۳.۱ میلیارد یورو برای برنامه «سپر آخیل» قرار دارند که در آن سامانه‌های اسپایدر، باراک MX و اسلنگ داوید با زیرساخت‌های دفاعی موجود یونان یکپارچه خواهند شد.  این شبکه مبتنی بر هوش مصنوعی برای مقابله با…</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20381" target="_blank">📅 00:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il_ZOFrZ2q1z31aOeQopLFJWNpXJ0gAwz34by-mYc5I_qgwVETx5cxNJWF4Vut94BxiYQRh0WCtb3EOW4bQTorpTCQdhb_dbDl2IPmVu_RwKzumKt-Nosgo5pzQW1E4ZMq_NJdvRFQ_7ia7kaCfQvwwF9YRyLSpvQCn5UpNbStTYLTH0eM1P_W4y8ZVMK9YwsPiiSOyvS8uosICf6D3KoXFu6nap5mNER2kDtkG_DHiqEtO2ZDioWoXQlaHKHtDvlFKMn3pDJPJA9qQjelxa9RIa2oW3iELr3UOa4CDVqco8X_Z7_Vu3sBVbrgrOb3OBQyDBLDhpTGPO858cL8_wJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو بار رشدهای عالی را در طلا شاهد بودیم.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20380" target="_blank">📅 00:42 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">گزارش های اولیه از حمله موشکی آمریکا به یک نفتکش ایران در اقیانوس هند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/20379" target="_blank">📅 00:40 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حملهٔ مسلحانهٔ عناصر پژاک به اهالی یک روستا در مریوان کردستان
در جریان این حمله، تعدادی از شهروندان محلی زخمی شدند.</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20378" target="_blank">📅 00:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20377" target="_blank">📅 23:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUTM6cM3-1MBDMRSE-5MxMzc1J-fnTWtl0pYkW_0MkQ8pDAp5XIHDUa2UdBkjgs1wRZOq_cBDSI-yErHA_kWRtSJhPmXPlcENYLoZ1foX4AWG9NgwHrfmOOb8gy-MwzCy4mPPG7XM6FO-n5UpsSJRWnBfgG8lxnRQ2hUGt1QKId7PZwF_EigPgPZWxjD7tkMOJArglVS3gkb13UOMsWrTmc9c9_M7jZd3J7EZ3UTQzsk4RmiV6OhZNgyYPwp-87trOHZ11mguzu45zehsaGVEUCEyL3gp3hz1vaZ4520Vbj5GjY0auVdmtq6CqNi_yt6CIwH0gPUyQzi0yjZD0Vmnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20376" target="_blank">📅 19:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20375">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">دادگاه مرکزی کیفری عراق، امیر رحیم جبار لازم، عضو کتیبه‌های حزب‌الله وابسته به ایران، را به دلیل گروگان‌گیری روزنامه‌نگار آمریکایی شلی کیتلسون، بر اساس قانون ضدتروریسم به ۱۵ سال حبس محکوم کرد.
کیتلسون در ۳۱ مارس در بغداد ربوده شد و پس از حدود یک هفته، در ۷ آوریل آزاد شد.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20375" target="_blank">📅 19:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20374">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اسکات بنت:
به دلیل محاصره، تنها 30 میلیون بشکه نفت ایران روی آب باقی مانده است - بنابراین حتی اگر آنها بتوانند از چین پول دریافت کنند، این مقدار تمام خواهد شد.</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20374" target="_blank">📅 19:20 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20373">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شمار کشته های حمله شب گذشته آمریکا در لارک به ۳ نفر رسید
خبرگزاری تسنیم:
در پی حمله شب گذشته آمریکا به نقطه‌ای در جزیره لارک، ۲ نفر به شهادت رسیدند و چند نفر نیز مجروح شدند. مجروحان این حمله برای مداوا به بیمارستان منتقل شدند که ساعاتی بعد، یکی از آنان نیز بر اثر شدت جراحات به شهادت رسید.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20373" target="_blank">📅 18:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20372">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا، درباره ایران:
«ایران تحریم‌ها را بسیار جدی گرفته است. رهبران ایران از وضعیت اقتصادی کشورشان شوک‌زده شده‌اند.
ما شاهد صف‌های ۳ تا ۴ ساعته در جایگاه‌های سوخت ایران هستیم.
ایران به دلیل از دست دادن توان اقتصادی خود، به اقدامات نظامی روی آورده است.
می‌خواهم از اتحادیه اروپا بابت حمایت آن از عملیات موسوم به «Economic Outcast» تشکر کنم.
خبرنگار: آیا بازه زمانی مشخصی برای فروپاشی اقتصاد ایران وجود دارد؟
بسنت: لازم نیست اقتصاد ایران فروبپاشد؛ فقط کافی است حکومت ایران به خود بیاید.</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SBoxxx/20372" target="_blank">📅 16:51 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20371">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">سرتیپ ابوالفضل شکارچی، سخنگوی ارشد نیروهای مسلح ایران: صدها نیروی آمریکایی در طول جنگ کشته و هزاران نفر زخمی شدند
➡️
در این جنگ نابرابر، نیروهای مسلح ایران با استفاده از تاکتیک‌های جدید و نامتقارن در مقابل توانایی‌های فوق مدرن آمریکایی و صهیونیستی صف‌آرایی کردند و ضربات سنگینی به دشمن آمریکایی-صهیونیستی وارد کردند.
➡️
به عنوان مثال، هر زمان که یک پهپاد ۴۰ هزار دلاری ایرانی به سمت اهداف آمریکایی یا صهیونیستی پرتاب می‌شد، ارتش آمریکایی-صهیونیستی از چهار موشک به ارزش هر کدام ۴۰ میلیون دلار فقط برای رهگیری آن استفاده می‌کرد که نشان دهنده میزان خسارت مالی وارد شده به دشمنان آمریکایی-صهیونیستی توسط ایران است.
➡️
با وجود این هزینه‌ها برای آنها، پهپادها و موشک‌های بالستیک ایرانی همچنان از لایه‌های دفاعی آمریکایی و صهیونیستی عبور کرده و به اهداف مورد نظر خود در پایگاه‌های آمریکایی و سرزمین‌های اشغالی اصابت می‌کردند.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20371" target="_blank">📅 16:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20370">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ به فاکس‌نیوز:
ما به حمله ایران به نیروهای آمریکایی که شب گذشته در اردن رخ داد، پاسخ خواهیم داد!
ما به آنها ضربه سختی وارد خواهیم کرد. پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20370" target="_blank">📅 16:30 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20369">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">میگویم اینکه خارج نرفتیم به این می ارزید که موقع برگشتن زیر تیغ «حافظه تاریخی» نرویم!
سبحان الله !</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20369" target="_blank">📅 11:54 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20368">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnqJwMeCk11l8fEJ9BurmbZeRzD_chS3N5DZcz0E0N2jlDfNazL-q30I6wZ_JyiSKEd4fAXVV0HrMeNwixI0LJRAXrfhZDEsjtqcFs6GHaVP17kfQSXbuNYHkd0MdS8miiTOwTjCU9_O2IJabIpOs9zbVol-AtJrEWfqOmc9cUpvp1F8HvKA6KoMYj6sbEW5dPQ4D4sD7T6A9XQUBYFK-ql7DpItcqV3agCOQkda3gD97XSorx5w7n4muhphlOXB9ea36fUmNf-eR1z6HlcMt7SOrWGhyu89VCgl8WlinJP2CZehVAm_tGasUg7x70ALnYiZRLM3pWjkntOL7RRy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پایش</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SBoxxx/20368" target="_blank">📅 10:44 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20367">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">امارات متحده عربی اعلام کرد که با یک پهپاد که از ایران به سمت آب‌های این کشور پرواز می‌کرد، مقابله کرده است.</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SBoxxx/20367" target="_blank">📅 10:26 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20366">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67mP6e9x5uvYfjRcqNlKSlbdYaORF-JuCoBwHwP5JM9SOFiLjjF2oUEtwVXbfzG58DHsMqsvnWgqptxHBUIN2AqHB-m22Hdr_07Y_l2NIUa_gCRM3b8PM9Lyz1CUHq3ZjnboXj_E-FJTpUdrbqh_xIjR8fCRzEODdolB5rsFH_-FXd4y_YZfUiTTb5W5HJpciAgHz9TXrm3zaF0M3NkMa8IaG9NYdMDJHsTfgpVXqJGoinFK7CAV0psXjq8lPZrxn2Mjn11tI5kNFA31BV-54GXN9hMgDAPBAaG8bVgwO7c9Mqo9aNr5bNwnesy58SOx_ZgI-VRo5xcBFscGOHpEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک برای امروز در سطح متوسطی قرار دارد و با توجه به ریزش بامدادی طلا، پیش بینی می شود از این ساعت به بعد شاهد رشد طلا باشیم.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/20366" target="_blank">📅 09:31 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20365">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔺
پایگاه آمریکایی «المنهاد» در امارات هدف پهپادهای ارتش
🔹
ارتش جمهوری اسلامی ایران، محل استقرار بالگردها و نیروهای آمریکایی در پایگاه «المنهاد» امارات را مورد هجوم پهپادهای انهدامی قرار داد.
👤
روابط عمومی ارتش:
🔸
از بامداد امروز در پاسخ به تجاوزات اخیر دشمن متجاوز و در انتقام شهدای دلیر سپاه پاسداران انقلاب اسلامی و مردم بی گناه ایران اسلامی در جزیره لارک، ارتش جمهوری اسلامی ایران، محل های استقرار بالگردها و نیروهای ارتش کودک کش آمریکا در پایگاه «المنهاد»  امارات را با شلیک دهها پهپاد انهدامی، هدف قرار دادند.
🔸
پایگاه المنهاد، یکی  از مراکز مهم پشتیبانی و جابه جایی هوایی نیروهای خارجی است.  روابط عمومی ارتش، با اشاره به تجاوز اخیر دشمن به جزیره لارک، اعلام کرد، رزمندگان ارتش جمهوری اسلامی برای تامین امنیت پایدار و حراست از سرزمین ایران اسلامی تا رفع تهدید دشمن از متطقه، ایستاده اند و انتقام خون همه شهدای جنگ تحمیلی را از نیروهای ترویست آمریکایی خواهند گرفت.
☑️</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20365" target="_blank">📅 08:04 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20364">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCqd33i-HkAxkmslWvcP1vMGthV9eZ3E1hg3-lqg5yUditJSY1xbLDWHfQ4VCoOkpkTDHgGUjbJOQAnmdicQ4Wa9gZTIB5tYutis5eI9E89iXgsli4AfhZhC9E2c66cu2m5dA7dyoBiAgyg5ET8jYKUGW-HD8mSbBo0smuy2dWhueFPNvK4lLHS5uTz73bI0oZlYRJM9Xty40oVAtM7-_M7roJ_jsWuBQGt-lCFnV0w2bN6EbqnGL31XenWffhszPSKO_g5-VVJ80mgy36IUPDyP5idq9oOvpq9ysNE6pdYJMrvgBmGyLcBSj_zUZlLEHk-rekVYzP0l4YWqOarjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه وزارت خارجه</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20364" target="_blank">📅 07:53 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20363">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ:
دور جدید عملیات نظامی ما در ایران تازه آغاز شده است</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/SBoxxx/20363" target="_blank">📅 02:49 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20362">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گزارش هایی از حمله ایران به قطر</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SBoxxx/20362" target="_blank">📅 01:52 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20361">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مدیر Secret Box بر این باور است که این تنش‌ها هنوز به جنگ نهایی موج ۵ ختم نمی‌شود و چند هفته ای دیگر زمان داریم.
لذا اگر تن ندارید لااقل آماده باشید.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SBoxxx/20361" target="_blank">📅 01:29 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20360">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ادامه پرتاب موشک ها از ایران</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20360" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20359">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مجری صداوسیما:  به خدا، به صدوبیست‌وچهار هزار پیغمبر، به همه اهل بیت باور کنیم که ما در جنگ پیروز شدیم.</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SBoxxx/20359" target="_blank">📅 01:24 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20358">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دلار ۲۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20358" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20357">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار در جزیره ایرانی سیریک</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20357" target="_blank">📅 01:21 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20356">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارهای پی در پی در اردن</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20356" target="_blank">📅 01:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20355">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SBoxxx/20355" target="_blank">📅 01:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20354">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfgA4SVpg-6KCppdzJvUqQMdGsyyon1_2-pE5emsoP7tuvlDJsLvFpJbNSg_EMZZKk_OtgKwqLqB-qraf_EzOmr2CBCS7QSIoE9-6INglqZxisvGRh6PiM_Ej2WercWlvgmHW62nE9bNGQzH3Aw3ax_0ujbksDaZMcp6iybHQ-8ePaGvhUl6Ss9-4f_0TYRyHI7M-lwXDBLi0ou5av9goMzmUJfQG9ZgjIy5YqMZyjAGWxhRCLRkBBui6LNzwK1n51ll5MioJXMcQXEFeQZ-KyEv4ETewEucrpdAuAgxG9anN5nN3i6XIcZvwRNYoo2YvsDgAVggVqPBcvKT04sc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ‌ترین کشورهای هر قاره جهان
بر حسب مایل مربع</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20354" target="_blank">📅 00:57 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20353">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrXauPVgfcZXAsjhlJXc2i1KE9Ftfi47TdV0c08PX1Ve8H5Ugeq_beOMv7Hq5_CQUqkozpq4NzV8-0Vt_fxVpANYPiMSP88fG-mGbnq9bPkCAs7srH0uQiU9zTW74S0DGuWerjPEsZGz4ZQ9HY4fNnJ8Pd3go6hsztE6IfHncL4tRwXedbvRYViEc7bfLomGxSdH24dNzuIaYSATkEGToY1aNmIY2BtN5pj2YzBHFjnWfPhsb_HlX2JaiDVdNp19wN-ObfKjlHKFw1GhPuf0nqwKC4j3rH12FYyitSkQ67eJvpOYqhRu-DKLPTMS2A3j5C6yuZakh4kQVtX4JQSZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20353" target="_blank">📅 00:34 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20352">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بحرین — اربیل — اردن  کدامیک؟</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/20352" target="_blank">📅 00:33 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20351">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcJmsIuncyUADXjkquVk3lG-1TCFd4wLoKOW_f2Nh22BKPycU6D5prPe-nIH6dv3rOOz94jmygyqK6HAzFMHs8JHZ5-zWFft3c8RBykQcHyZAgkfnWwf7pRDby57BpQlBCZDwLGY6UCVtXSaBQlEcQwOqFF8Hfx7fP_FI--IEF9EhL5Lgi2pKzRSRPXYpoLhFD-BEDcsxPzgSVxlKNA5xwygBwoB-KnjQk36jHqFbClNC8FE0Jo_1uRXfoLpVfO-iDHm4e4lTJG0L-rIrNDC84sYrinkOj8PAovwd5KItLFp3z7fTIPCQtSBI5QmDINVWbgRVy7bNDKIA6UBAIs4XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مسیر محتمل وقایع آتی از دید من است:  — شکست عملیات طرد اقتصادی در تسلیم یا فروپاشی جمهوری اسلامی — حملات جمهوری اسلامی به تاسیسات نفتی و گازی منطقه — آغاز دوباره جنگ — عملیات زمینی آمریکا برای تسخیر بخش هایی از جنوب کشور با این نتیجه: موفقیت کوتاه مدت…</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20351" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20350">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">Secret Box
pinned an audio file</div>
<div class="tg-footer"><a href="https://t.me/SBoxxx/20350" target="_blank">📅 00:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20349">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اخباری دال بر شلیک موشک از مناطق مرکزی ایران!</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20349" target="_blank">📅 23:58 · 08 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
