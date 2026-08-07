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
<img src="https://cdn4.telesco.pe/file/unjV7PusOWgWK5spoVRUnafP5_9I7qjUfcOZtWDT0U5OkdJIx-tRemqZFsDapSd7N1_sB2AQrgJ9nBo-bFsi8BPF0oZ4YRTYQm9OE9U0oAruRVBEJX-1rfd1TznG0UeV_FMpI9i1YHLgg-D5e00EPp-3z6w6RQKKxbkWF5hwTNt62W5A96tuT_0rZJYFYM3JrIsMb7hWUeNu-ypjb0w9LZLZpEu6umt0COGymGUFHMjcjYeSEftmgIuYdOVmlCy5rRs0n5ScwRa1hsBM0MVod-tBhGCUF44ByJcHpyTX9bGbPz5lEiG4NmTDsc-uzHGeVENZXcNE7rSA-jk_clq9hQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 274K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-16 15:35:27</div>
<hr>

<div class="tg-post" id="msg-87205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-ewAyKkqoSpUrVKUOiVqHr9s2sUnN6prp7giDUpomcTAvRtPWvq0a8MORpd8MNV9-0uL_GnmBnEGxYur-3mHg3ipNqzC8Efmdf8IjpMa6slHpBwHXy_smOcZlzPxQn0yNyqM-dmpTwXLpQhEmzNObtAXz4lQMePKX1gHgQf50dwsdnFpqXF5ksFvSqUHPTK7xd7wpLhwJtJsFP4yhbhB-_UMfj22MwUwodyt7aQsEsUuqGuIXk3mqQ0bmaKIUE8tnXoJ3cA33RystFfR_yxWKDjjke42CWUCqC-6KQvC9Tsqp_xFuJrTqZfp8rtt81kuk7bSyEtqNw7_q-QcMsVHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو لجنة الأمن القومي في البرلمان الإيراني إبراهيم رضائي:
ينبغي للسعوديين أن يدركوا أن اتفاقية ورقية مع تركيا وباكستان لن تجلب لهم الأمن، تماماً كما أن سنوات من الاستغلال الامريكي الأحادي الجانب لم تجلب لكم الأمن. أصلحوا الأمر حتى لا تضطروا إلى التوسل للحصول على الحماية من الآخرين.</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/naya_foriraq/87205" target="_blank">📅 15:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية:
لا وكيل رسمي لستارلنك في العراق وكل من يدّعي ذلك يواجه المساءلة القانونية.</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/naya_foriraq/87204" target="_blank">📅 15:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🇾🇪
🇾🇪
‏بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية نوعية.</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/87203" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ignou_JYHQob3-lXMfIUaq0jK1PH1IPdvkvO8rRlN4YG5f9P-8r2iqxlbszk6edQ85VAcm_gApw31VWdVViHCMCRJqrNsgM-4aF3fF6detwwTFdZMlEhJfv6E2gz_mJ0DtLffyyxbv911bDHKiaYWN-zQq7roWMdiyq29ui2RIoXmMNgCYJfAEjxt-eFBBxkOCcNaGmgqK2-1USnn0VpCgKovebgXnPEKv-E565BLm1GPLirCjEWb93Dku124RA92u28aQpy4_1K-hoYazkJuS-evDHPKPcOgR4z-o47JZ-ckQeGweW9dSuQlGnB2W4N_ORkEbco15vGIF0o44v58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">للبيع – F-15 Eagle
🔥
تشغيل وقيادة ممتازة (إذا عندك مدرج).
عداد الكيلومترات غير متوفر… لأنها تطير.
مكيف شغال، والمحركات بحالة ممتازة.
البيع كما هي (AS IS)، بدون ضمان.
السعر: لا تبخس… أعرف اللي عندي.
😎</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/87202" target="_blank">📅 14:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارة الخارجية الباكستانية: تركيا والسعودية وباكستان توقع اتفاقية دفاع مشترك.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/87201" target="_blank">📅 14:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزارة الخارجية الباكستانية: تركيا والسعودية وباكستان توقع اتفاقية دفاع مشترك.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/87200" target="_blank">📅 14:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
اندلاع اشتباكات مسلحة بمنطقة المنصور غربي العاصمة العراقية بغداد  ؛ ضابط في جهاز مكافحة الارهاب يطلق النار على موظف في مجلس محافظة بغداد و القوات الأمنية تفرض طوق امني حول مكان الحادث .</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/87199" target="_blank">📅 13:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇺🇸
🇮🇱
وسائل اعلام خليجية:
واشنطن أبلغت إسرائيل عبر اتصالات مكثفة ضرورة خفض التصعيد في لبنان.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/87198" target="_blank">📅 13:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660bec9997.mp4?token=VEFpSpEY4RwMDRSPXBhPnnLGbT3W7NJd4n-BpRwk1sW1WAtoVT_37hhyCv0M3z-lAtf_mhUNdZci5CuPIB4J1SgF5mF0GLZ29AlepEyG7YVX4qmwkgrTilBNNZw5xSBbN5N1AmXX5nXSmBXPzgeBA5X8Zjlm2NCwv7i6_gFSa1jPyOC0GgGx1IDpv1ZQOOq8ewn6uz1TeTRueFDUDvveB2tJnj9qr33EDp4twvcZIqs1fHmtUZz3gLLq8VUMymYeUSSlq4dUdRYBIsyfJjaJe9hyVxc_1-8ksxvuOO-L_kMKHR-LGsDRZk4KYH2ADwmvHC_MZby3TZ3zS4wCbaQgqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660bec9997.mp4?token=VEFpSpEY4RwMDRSPXBhPnnLGbT3W7NJd4n-BpRwk1sW1WAtoVT_37hhyCv0M3z-lAtf_mhUNdZci5CuPIB4J1SgF5mF0GLZ29AlepEyG7YVX4qmwkgrTilBNNZw5xSBbN5N1AmXX5nXSmBXPzgeBA5X8Zjlm2NCwv7i6_gFSa1jPyOC0GgGx1IDpv1ZQOOq8ewn6uz1TeTRueFDUDvveB2tJnj9qr33EDp4twvcZIqs1fHmtUZz3gLLq8VUMymYeUSSlq4dUdRYBIsyfJjaJe9hyVxc_1-8ksxvuOO-L_kMKHR-LGsDRZk4KYH2ADwmvHC_MZby3TZ3zS4wCbaQgqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أزمة الوقود في إقليم كردستان مستمرة..
مواطن يفترش الرصيف منذ ساعات طويلة بانتظار دوره لتعبئة الوقود لسيارته في مشهد يعكس استمرار معاناة الأهالي مع شح الوقود وطول طوابير الانتظار.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/87197" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae7cba1e7.mp4?token=qokxOAvPAeWUHW9k6iRxZ9XaiZLdJtR_7JbrhTGi0hun3gLbcwzspY9kqhvkd6pMEcF4m3nhw6RhykIKpFd5Zpl3CflhUmKFlvRZ0MgWzzY2vbNnhKoM03EmDnfovEjFyjGt2erqQd8rhqgssCQ0xs8sStlWRi_NK7Bk97y1SwLw8HHGVCgO5b82wc17BFhNsCxLB9zLRAyv6BiBicEd3n1m0-j2sd1vriX8NfWWMxCVqY_tw6nzqN8NLK_X3i8wUfqyPi8MQQMp7BmyeyEDX_1AnsK9Nt84qigYNrCboxHHV1zMqfRu9TrsSB_8XNuolwcydoUU3kOEaLdisvGJQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae7cba1e7.mp4?token=qokxOAvPAeWUHW9k6iRxZ9XaiZLdJtR_7JbrhTGi0hun3gLbcwzspY9kqhvkd6pMEcF4m3nhw6RhykIKpFd5Zpl3CflhUmKFlvRZ0MgWzzY2vbNnhKoM03EmDnfovEjFyjGt2erqQd8rhqgssCQ0xs8sStlWRi_NK7Bk97y1SwLw8HHGVCgO5b82wc17BFhNsCxLB9zLRAyv6BiBicEd3n1m0-j2sd1vriX8NfWWMxCVqY_tw6nzqN8NLK_X3i8wUfqyPi8MQQMp7BmyeyEDX_1AnsK9Nt84qigYNrCboxHHV1zMqfRu9TrsSB_8XNuolwcydoUU3kOEaLdisvGJQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇮🇶
🔻
القناة الروسية الأولى:
بسبب عدوان الولايات المتحدة الأمريكية وحلفائها على ايران اصبح الوضع في الشرق الأوسط متوترا من جديد وتهز الانفجارات بما فيها في بغداد إعادة بناء العراق في هذه الظروف بما في ذلك على عاتق هؤلاء الذين أنقذوا البلاد قبل 12 سنة عندما بعد السنوات العديدة من عدم الاستقرار الناتج عن الغزو الأميركي للبلاد اقتربوا ارهابيو داعش تقريبا من بغداد نفسها
بعد فتوى المرجعية الشيعية العليا اخذ الآلاف من المتطوعين سلاحا بايديهم وتم تشكيل الحشد الشعبي
اليوم الحشد هو ما زال احد اكثر القوى نفوذا في البلد ولا يحبه للغاية الأمريكان وحلفاؤهم
لانه بالإضافة إلى المسائل الأمنية والأنشطة الانسانية يُحدَّث هنا عن العلاقات الحميمة الحسنة مع روسيا وحتى يزيّنون شوارع بغداد بصور بوتين ويسفر هذا عن عدم الرضاء القوي من قبل السفارة الأمريكية
مهند العقابي، المدير العام لمديرية الاعلامي لهيئة الحشد الشعبي:
"اننا نعتبر روسيا صديقنا. في العلاقات معنا الروس أمناء ومخلصون خلافا لممثلي بعض الدول الأخرى</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/87196" target="_blank">📅 13:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_X60oTXbFMn6cb2M4hO8wM_1y30d7_wxW0CQaqdDDt7pG4oFwwg5ZFBKN1O1hF8vKtj2sNSz08lZGg6wqPSSwGfI7BXDhZjYcXDrNOD_y9CWQeDyLtsnNSP9xNPXwl3DhGqe8oaEXNwWU6kjG-3g685KByGLOGdoRb1qiZk9a_EpMqI6VfXIxK8nAkz6PC-dv39jEPu9FZzLY-EEwx9n4ZoBh815Co14Jx88b3bquxy_vskOCDi-OFYKNGwnEGRe2qvfkSyMlSuLXfUQhA7IvSRAUV1RZq72kSpA6ssBPplkGNH5i38J828Z95Gs7fy1thA1NR1NyfumfBFKuCBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلية الإعلام الأمني في العراق: الحكومة ماضية في حصر السلاح بيد الدولة دون رجعة</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/87195" target="_blank">📅 12:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87193">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mM293fKBZNMTuFHl7jvwtDvLD0O99rsn69akt5MskREkDppCzNW3BbYhFZsqliMYDxKanW9WvW7OWyAirkWhwUGMGbtZLiis2XJ6CidV0UU8yok_Xt3-nn4c8gbV0un3ZbHsQlflu7vaAtCMi7GUwA5gZ5jURTgh9GRxpXUFu6cpCsbw2BYNZbBbr0MmTfX2HvEDvipLOQwV5AmJIHHZbC5Na1kw4hmXDLJhKRbljZj1bFj_wUnFF9-E0oJXlZisf9DDr_o-tIYFHgm7ShgO2QFzzV-uchu3a-mIom3n9HwUua9IPYucloW4xC6XxaaPTktLdCBkuaKd2mmaAe_vAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FzBsdT8fqSEcs6RQYavbv6llv8m1TnuQe14p_dqHreb79toXINgQZTdiebdBkA_mc14dBj4zG1Ov4N-UitsYN9Q7MhASpkIulOgT2iEaeMkWnz3k4Tmo9TX7lmwk77E_fyqK4c1jtfMigCSfVxbbfEIgdKwYH0F9rgTsaVRcQ6kOYai_0IquvLjQkWao8nx6R70IZCkIL-GMrYV44ETdbLyzo-daRfE87hS6wzqUrxeRxGTcJWkK-BKT1C2utJDswTNLk_79LjF63DcdrCTpOMQAy1W-ELrUP2O-D-ZfurbYPkNyWeaaD2ymGHh0GX3IKLI8v1_kiuRFvTcLA9XGpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">الانفجارات في صنعاء نتيجة إطلاق صواريخ أنصار الله باتجاه مواقع المرتزقة السعوديين في مأرب</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87193" target="_blank">📅 12:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87192">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">نايا - NAYA
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/87192" target="_blank">📅 12:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87191">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blz0ctEkzDxSl88eh2t5EYOl-9PZ_j1KkoAJsUqrYqQER9LFEa6lEKsQ6aIFRlyWKC78eZc183VU4H-F1UfvOhlgdcfVeDlJEOLt-5aFZlnbn55dAhr9yVPHsqpnwPYIAr33Hilx2F1OsX7hN-2OKKFfmZrdiym1YAVVBOl952v3SdtPezYWOdgDUILZbeWUes6gMfHX9zH3RuRES5JxS_qSstzRz9DsTo1LAjaQB9QCfzR9hJZOCB3z7tVFBUtTWq5Me2yHbZs5xSfDxJIFGpFROQSnlQRvag5wnBN-mUn0MMuIZ2jW2f-V_KAW37NaGVoRr5E6vvmkMyp5FrfDoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد خيار ستراتيجي ، والرد هو نتيجة
الحرب المفروضة
على الشعب العراق من قبل ال سعود  وعلى الجميع ان يعلم ان زمن الصبر و قواعد الاشتباك انتهت منذ رمضان ..
المقاومة لا تعمل بنظام الدكة العشائرية ولا على ردود الأفعال والمشاعر ؛ نتفهم جيدا غضبكم يا ابناء الرافدين فالعراق بريء بشهادة الحكومة العراقية من اي استهداف على السعودية وان ال سعود الذين عجزوا الرد على ايران راحوا يفرغون هرموناتهم المضطربة على ابناء الشعب العراقي … ومن حق الشعب والحكومة العراقية وفصائل المقاومة ان تدافع عن ابناؤها حسب قرار ٥١ من ميثاق الأمم المتحدة . لا يهمكم نعيق مغردي حوالات الرياض</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/87191" target="_blank">📅 12:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87189">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKR8Ss-OLGnyttvJeiqUBJ-lk59QZkUZ-AcU_s3R-oRsg7J8pYlaK0Y5G-tzN6kq8d8afQp_Y5Ohovo3wosWOw8kO0oadiFVTfMMYRVO0Xi9zEPwrVXVEkzmZGMIRdV9O5N4BjBFTVXw_Ua9CfkT5Bv3qISupdSHS64ysyvKNg4q8ouICikSC-GhBI_2_X5Z8StdomnJrPGQTuC0OQqXZgpYjBsQFnwkYMN2Q6YUON51mN2cTWIw9iYUYrfVw2S2kAIgWGrxXKmNzv62FnJ4fEJwsw13D_1EpI5wbfCZpDpv2HkojAh7DqcpfkI4HXAXUXTJNnHSyc4oF04LEXoyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nNPLscoQ_RCPGABE7lNypjEZ5Gu9I5qIRFZPPbTwdFwSNpa0kjG6Xn_AaMoNyJzYY852YEhc5lXnox6hfphRT-DFEusyarxsxqg1YxZJcLPBGoD8NkiUu3dS2giZkmXlXtd6OfPgBHe-Hacess1xOWm6Peif0sAtl6Av8DgWntRuEILEpBUB8CXKcg-mjoS7eRLb62XAo10awUzubSSObtwDfhw9gAj32Tc8XI7HsDu-SNMBip7gKww1vfxhu-S7q_XVVbaeDzYE6f1CJz_kb3zKRB1p0mq1HVh6hU2c55ZQHGRRdobgRtmkv8i3br55JNKZy29KzVfTFCKM633ghA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/87189" target="_blank">📅 12:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87188">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نقسم برب العرش خلاق السماء بانعدم الجيش السعودي نعدمه  عيسى الليث…</div>
  <div class="tg-doc-extra">Ahmet Demrak</div>
</div>
<a href="https://t.me/naya_foriraq/87188" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">نقسم برب العرش
#شاركها</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/87188" target="_blank">📅 12:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87187">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/87187" target="_blank">📅 11:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9K6PUCldtAWPM9raSBPCbU6EjogNRt-BHlKj-7O4I-5Sb4JPh0ZmexVpi5kHT14nHGoEkOpktuXf_wGULSBSIDdiGyM1dZQk6iEszopM4GjRrBbznGBqYJ7lT83OhyIJLY31DBt8QSXeA6kYOZiVkdpVLychwJM9cCGy-Rb1RN0m8GopkbfXTxRgd6pWW4ZOfDk5Bf3jQuenPMbjDoKk7zbu6aqtJgkKKrlS1nnOVuAuk_VRBbay39COCFloZtEnb95gDMYx4IZC89WenBFa8PjgU_kM2n6Jnk2m6FGwtkkVoFD-QK8_xrXIs5rQXkkiov-2fUG8waG8pEyZL_uEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات جديدة تهز معسكر صحن الجن</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/87186" target="_blank">📅 11:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">تصاعد أعمدة الدخان من معسكر صحن الجن بعد قصفه بصواريخ أنصار الله والذي يعد أحد مقرات مرتزقة السعودية في مدينة مأرب باليمن.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/87185" target="_blank">📅 11:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVI44UVhzNVk-0LjFZIbL2GDtwDfWXUhDDHRssohs-dhkL4h4vfsECazn8-P4PN6iyeW3ddCQgAhvzrxypxK5fEKGx5O3s1PPzdh0kr2pmrnyPoAeV9hsVUV5BbVshQXVWXvkXLsOMHmCCRyROg-wXCNjFrmUYl1C9ZqE3FMgI1dxUknZgBwr3GT-BUKFzuxNl_tXBQUkJKCIm3kBdoSWre7ZYyk4TaVbIa5d-rpuNoj0q0pjX_rjlTpCzQTqYmBUa14Bfv5rZvItehkMYi0XC21hPI7pSEw0KUADbNR3tcAlyBsxXskvaQzs_FzL5c_LhFWlChXw89duDKCwZ42sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو حركة أنصار الله حزام الأسد: من يُدِن عملياتنا فليفتح بلاده وأراضيه لإقامة معسكرات سعودية</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/87184" target="_blank">📅 11:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87183">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇱
🇺🇸
إعلام عبري عن مصدر صهيوني: واشنطن أرسلت رسالة لـ"إسرائيل" تؤكد عدم وجود خرق من حزب الله جنوب لبنان، وطالبت بتجنب أي رد عسكري عقب مقتل الجنديين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/87183" target="_blank">📅 11:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87182">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/87182" target="_blank">📅 10:38 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87181">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmQaa8cnSJ6NaLnV2TVz8uj4IDMboqeUQgCjja_7l36XJq_tJgcOP_EY3_PlvENOlHqo5LZjJBQLFCSgM7lCVglvd4dI4rKQp9uB_oMgctJy_EQnaMKfQxsDSyRy8W29oraDtkPE3chZbbHWyP6JdYohF_4nQAl5NhU_RlrwmDdj-DIPkXxEAYt23oLXoWvS72eVLUQS000nsawLM5dY0hdudP1_ag8-LIbhOZVPMaw5cAA_kfkyQJR17tBZeoq4EScz4xAR15QXfG7Qh890zUFBp2PBq0npuOk5dfEyETkHPlYTT2gQFO9GdPckrzJ3t2x2OwiG9vpGFYhpP0mlhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/87181" target="_blank">📅 10:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87180">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بورصة لندن: أسعار الغاز الأوروبية واصلت ارتفاعها بنسبة 3% لتصل إلى 686 دولارا لكل ألف متر مكعب.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/87180" target="_blank">📅 10:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87179">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شركة كيبلر لتتبع السفن: 6 ناقلات نفط غادرت مضيق هرمز و21 سفينة دخلت المضيق هذا الأسبوع</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87179" target="_blank">📅 09:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87178">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVtd6tmFNvWYpKvlgKj2K_AyFW_2UFGwvJedeR3IuRamVLFjdwwJm8zGQ9W4_Hjtlkm_1Knt0NQ8sLAfkP74yi5n0liI06VS9LbRUCfr3LL7axgsrWlDVT-HIug2jvyD4cd23rs63QqpmsKzLN3Lof566DWh3wl5bQKwjsDTBurMV1COlGGrT5p_CgFtiAyEGdaMyMJDiODMPDqFleAuAuHtouQMsuZHKfM4dzGVlj-HfAU8LWRNV8lLZt-OCEZqfi1YUUZfjv0-RbK-rLi7FzEEKRvG9npIX8ac10wgLaiVZ77VphvPliroGgNEAOr-CtjTGy-FWnbyCfZX-HEbCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صواريخ أنصار الله تستهدف المرتزقة الموالين السعودية في مأرب باليمن</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/87178" target="_blank">📅 09:23 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87177">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2feb1679.mp4?token=uQ_mtVxLV-Kzaxg7y_XhBQNaWAUF70jx_MmFXrkPw0-fAeuFgf6HgrfViMQMnPjtdOb0KapMGfysJManukrMwCfmb5S_x5KUaVPksR6Y0WGThwedHd_tX6LW7gCetiS5manLZ-UDKfi3zbtvo7vENCagmSF2v0qH4ksW3IrinM-kNPAJXxZ-U57cyBSgcvlhIo06GUVyYEK8ALoLGRrwUvf2E3GBv9_z74eyTktQaJTPCLcZXSrMxv56SfptRPfKzEKF1EU1bdO7Yi3nB_ry186cms0MPhoa8jylGlg0Jab-H4-YON_b0sTp2jNTix4T-8JxhaUiXpwGsNHOr2jh3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇭
حادثة إطلاق نار داخل مدرسة في بانغ كرواي بتايلاند مقتل وإصابة أكثر من 20 شخص.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87177" target="_blank">📅 07:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87176">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275832bc3a.mp4?token=U8-C4ojj9kqy4r4IqjpgAt5cbzSo6N1_zgX1cOfjSfON9XMJyKPFxg7bs_UxiMgTHVbrTt2Cjg9TzWtbql_YM8IhWUugYSsiQnjQMC2w5_8KNZuzqEcICRrFlvO-ZPJkiGA6CSD3agCxi_XKkTfb9GUh64VqVGM5Dy2ZkwG2ynZKr_Ft2Ki_sYH8DvmflsmL4QN4wL-zP9p6DoWbew0cKymilFNqAw-KvPgQAmPxtgif6SXamCiFdExcjafNCgRtHl-k2rw7FmgT1RdqMjiznCU7d5NXP7TweeDqhU_PuhM09XJ-vfqELtypp9jWKBOA0klUx3C25k2l-cJrnu-TQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المروحيات تحلق بكثافة أيضاً في سماء محافظة كربلاء المقدسة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87176" target="_blank">📅 06:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87174">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd0d2b7aa1.mp4?token=S8ACvVe93YhpG1dRL0TxqYqTNabhlTGb8Ty3FJA2UNoteWRFyPYpIcoj2jGQkcPlfqOx7sQhAaHauocRp0ZvY6k2p_gu2y1beue3hwdK3PAtOvw9W33aZc7WnnEJ24M0MOHRFmC7ppjU_OZc1M3eM7GM-B9H5Xu3frIh90DsTyG7GRUj5yx2uEIIukkbmq_TR32DjbA2LT6HeGckIiZdYtGJ1JkItvhlUCgoUTW7i1tF-vqz3H74zHUkWR_hKZMbd6Cb36TtKs211zx6luPFalNZlxR7IuDzs6ZOIUfQGw1NLOxUYvRZeufOYyXwaVJbodRKJul2qZeXi8mYnXkjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
من تحليق الطيران المروحي في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/87174" target="_blank">📅 06:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87173">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjO9ZhgLf5bm8r0C8ZMk_fNf-vO8VzTdFcGeXroZpUtJuoI65V_tINZoXKcJluCXhtJUuOcgNc9WFRs4pk0_4Ra3Hnr6H-gA8VPmZoQr4kxWX_OvLwLseLMnP5QA3l7Ao0Y0xjcFeCc_VzFAmbnfOUKulWa98tBwtEPlr1_BrqdW7HVNazMbHNDmo2b56X--PUJY5NhpuTzqesVWhXdcsgLEN0yipd6YlCM-RnaGsf2RmsDK0c_6hSTKKOFF5gKQNGboBOWT5LfdhbSv3YAlA_UmBXBXpJrvWO5kPur0NhPO3qgpLaEr1KoeCIUG9OLLowWswXPywvuYZOe25nBYYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87173" target="_blank">📅 05:59 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87172">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/302813141c.mp4?token=FtktAFa_dyOWyPynFbQ9TZhVAg3nuEMZF43m0xiGd1sbQdBcx5rJVpNtsCI9vUrOT8V3y7p9qiQ3ScjM_xJHe_ivvOtVygNKFF0Ko5ZEoIwuySsWgG3yHAGw8v3wQY0elVF8tRfYeNBhVO1DznKxkTu58uj36-A_BY8nh-oE1p8tCz91ZXVG5Hg_j-Lwu8ZqFb7myaWUriW6r-x7uNoqOLo6RMMUUOGqsAG2HG5rTxiiR6YhlS016OSzVS7vSr4XSKgAyZC4mhMNf93_-yLU-W_FJ4Wj7QgG8vSvszm02cn-APq8fc20oPbG3MbQrSziJFPdC6lGiAL4SaUilwZgk0i-vlMLHeuqT1kCxsEe8wXfyICzBCcQL2WB3G7AFijMYTdNmdt8FzobqLjy1_l9ksqF_JHLf8uFR5oX37THNiILZk4UGXrqUzWwwzpQ0C_4oR7XFji4E0iWtl8VQE_miSb0zwLTkTtfLPVflh_QSHGxCy01GUVO94gU_fGfl2xJh7A6WhQMg3Mg9GyEQaUnen1mkPIq87FqB8VXy5jGxprVL6h5ZXT00vLAR4i5imf4mQCf6IPuymKlwC_aRIp0B28RXHxDvbp34IbwhySR0SAnMoTZ-T1lBRPPKJaKAFyAWOdrhCCsMAicQxBSiEjOiAN1iH7HNdFJuZt50xxDfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مروحي كثيف يجوب سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/87172" target="_blank">📅 05:55 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87171">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/87171" target="_blank">📅 05:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87170">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔻
هجوم يمني بالطيران المسير على مقرات مرتزقة السعودية في محافظة حضرموت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/87170" target="_blank">📅 05:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87169">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfd307190.mp4?token=RnSPVuaZ4dhffSeYX5C3H79acp73jXyqKXjX7SGpFI2Ksc8h8CLo9Ko5PTOPEj-doB_ECP2wGeDMqdpMtxB_iVlQPP3bFlZkaA5EKQU_JuHMBUkJPR1_AO0sUaInk_oiFjEIqMHdbtvKOtvppen0fDwQJnwIxQ_nBt-2QbFk93z0j71OSZSWGmC9dF6tNMMVHYyn66I4OHLcvChDTQXJ8eqzdCcMao6c5yu3eba5_Jxwe8LHHNasGFUocwdplqPaxDomgwDqZP2U2v34QqSK_G2PUypLv3WWT4f8Jocn0aT1rv1rIqjGtbpIuV3EhIabQOepJzSDji0nEWYBIwGP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/87169" target="_blank">📅 04:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87168">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=C26gAz4qBvVs_L_ajt4UY1DbeBBszgz5xKp8-BjgBq1T18TSGtglM9HQujHmlfhDJ1zeR0lO8qj0j2MLwoU1CfZraABegkT60QLUZEEZ2GBuey6Qs1Q6WDLED5-4v0I0oNlL7vOcbErdVYv4--b56e4MhTMU5FMJp7JJLo7SPOB8QPy6J8k78TM8EaZ_Y_7uVKHleTbEI-h7CIkuuF9rSctbFYlvvTwvguy8fYqEUNSCE-j5y9-HoWa_vQJlarSFzlgtfbMrsdMu8S2jQVwggCtnd6y3IwD4gHPmWCPrAhWvb4x9IpKT9iXXhn7kIIbZXC4JfPGMOzrrGErZifLM2iUqvZKJkDm5gUK4DNuPKEXGRjhItwjkKmx4ddjQriaOuz0F1oISh5zWgndJq5F-O8iU2yOFYLOVHbJN7CU6IGZ5OxIgZ9lMcgocwhz8H6V5OJQ1GyMgjZ_ncrSEa669TTx0xhhV2H3NkW_f6SJpultLefj5b8eJiUfKyYPQ_i3qt0qBvxDptpxT1-uMqR-MPdgBqNuvgC7Sd9pbLE35p69nwzdBYtrEuffMqapC-WNJAtZYiWTQVPncCtImoUqheRrgCkNHcKaHjuz29WMq7sUhmg92iMA7-_83b7xsty5ZF2oK3oPHjO1GTGW_WHp9Z99qNhSHAZAaSwrzxvJJaGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff414bfdb.mp4?token=C26gAz4qBvVs_L_ajt4UY1DbeBBszgz5xKp8-BjgBq1T18TSGtglM9HQujHmlfhDJ1zeR0lO8qj0j2MLwoU1CfZraABegkT60QLUZEEZ2GBuey6Qs1Q6WDLED5-4v0I0oNlL7vOcbErdVYv4--b56e4MhTMU5FMJp7JJLo7SPOB8QPy6J8k78TM8EaZ_Y_7uVKHleTbEI-h7CIkuuF9rSctbFYlvvTwvguy8fYqEUNSCE-j5y9-HoWa_vQJlarSFzlgtfbMrsdMu8S2jQVwggCtnd6y3IwD4gHPmWCPrAhWvb4x9IpKT9iXXhn7kIIbZXC4JfPGMOzrrGErZifLM2iUqvZKJkDm5gUK4DNuPKEXGRjhItwjkKmx4ddjQriaOuz0F1oISh5zWgndJq5F-O8iU2yOFYLOVHbJN7CU6IGZ5OxIgZ9lMcgocwhz8H6V5OJQ1GyMgjZ_ncrSEa669TTx0xhhV2H3NkW_f6SJpultLefj5b8eJiUfKyYPQ_i3qt0qBvxDptpxT1-uMqR-MPdgBqNuvgC7Sd9pbLE35p69nwzdBYtrEuffMqapC-WNJAtZYiWTQVPncCtImoUqheRrgCkNHcKaHjuz29WMq7sUhmg92iMA7-_83b7xsty5ZF2oK3oPHjO1GTGW_WHp9Z99qNhSHAZAaSwrzxvJJaGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
طيران مسير يحلق بإستمرار في سماء العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/naya_foriraq/87168" target="_blank">📅 03:04 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87167">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKskodymInD8j8GeHu8uEEo_x350cPfGe4cXOYmvpbWQ8H3hlGsP2KJ65nNKfFXUV3145q9DGbByxRC5VRPwydJiH49KcgY17HNwyhEorb5McHjrBFhy-wIysQ5LGVsMCJ2aP2iBU-R7jMJCkQqmnNtJTCUzNOWYMeJtVdENk9OLdHeEfrFEGzDmf5tnKj2xCn1egmoEgwUXJ6AdrqTIGhnK2MNba4dkFkobjzZ4Ulb3oBpEbVkuMaYV5q4ZCAwsP7XKEFPOks2JushV9BDygOcEDTXZiD7pv2IBZkT6j-hM4VSc0wkRjeiYG8AtzAg_vyGvfzleLlf1ROPmENHBvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
إغلاق مطارات أبها الدولي والملك عبدالله بمدينة جازان ومطار نجران الدولي في السعودية وخلو أجوائها من الطيران المدني.</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/naya_foriraq/87167" target="_blank">📅 02:35 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87166">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
عصابات السعودية في اليمن:
مقتل 17 جنديا وضابطا وإصابة آخرين في هجوم المليشيات الحوثية بصواريخ باليستية ومسيرات انتحارية.</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/naya_foriraq/87166" target="_blank">📅 02:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87165">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
ترامب اشتكى سرا في الأيام الأخيرة من أن الكشف عن انخفاض مخزون الذخائر الأميركية يجعل واشنطن تبدو ضعيفة.
ترامب كان على دراية تامة بأي مشاكل محتملة تتعلق بالذخيرة منذ أشهر ولم تكن التقارير مفاجئة له.
ترامب كلف وزارة العدل بالعثور على ما وصفه بالأفراد "الخونة" داخل الإدارة الذين يكشفون المعلومات.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/naya_foriraq/87165" target="_blank">📅 01:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87164">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/curgJPMk0zIh7lxhhERsIqw6JPukYk1GX3j3_FL11GGVDdNNBGi9f5I_mCLofytOJ7LA1k6HaKQWo2ghdbeyLUE3Zr8Lw-ViolQwkqIo6SaUNHcgKcFZPo9XduCYtOX2pYRMBViFP7pYrHNbXiS9dI8xJbVUpSRmpNi5V09I4zS6O7QlDyy11JvfwyfiZoaQi1oSLmHnw56ZzFklyXOozjvkrFm2UkS1ae9lDKplKlxNxT8qE6ydN9nAucl6vsGev6keb-ihcmzlHwAytG0eS1L06VNw32RO7y1awkC62wW69I9JVxvVsdK7aNjHqjDtqmUgoLx-C2EPJNEPTOnnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/naya_foriraq/87164" target="_blank">📅 00:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87163">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇸🇦
🇾🇪
السعودية تعلن عن تعرضها لهجوم صاروخي يمني في نجران؛ إصابة 11 شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/naya_foriraq/87163" target="_blank">📅 00:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87162">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔻
مصدر يمني لنايا: مقتل عدد من الضباط السعوديين واصابة اخرين في المعسكرات التي استهدفها انصار الله.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/naya_foriraq/87162" target="_blank">📅 00:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87161">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8949db271c.mp4?token=mA7lBynqeXJRCbw_GO8RTH6d6BcJESUTjhJrWK6MLdJtufQI4cA9qp5Dc39DLVweQJVOHUQpEA6Iim44JpdkaM8jASAvZ3eXGfvtIlvYbSY1AR6qSOo13dcEs0WeMgPW-fcdedCNnAXHzUCU3zqMhZ15ZkYxrapeJduaj4IHoKUL5Tfm_7Mu3gP21jY-j2PKUnmgh75iqICIp-Pc5hCjLFw8vf-3vXCQD9-Jqj_xOATwA9SKvdXp3LwdWyuxD2H80rwQLp_GvDwryycSkE4vAT5sGSh1FLVMOAqIi_XYDiNMZCrdv1s-cZbjD5QEVEDOvQ-iM7vfM4F7uRgO-9wiCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8949db271c.mp4?token=mA7lBynqeXJRCbw_GO8RTH6d6BcJESUTjhJrWK6MLdJtufQI4cA9qp5Dc39DLVweQJVOHUQpEA6Iim44JpdkaM8jASAvZ3eXGfvtIlvYbSY1AR6qSOo13dcEs0WeMgPW-fcdedCNnAXHzUCU3zqMhZ15ZkYxrapeJduaj4IHoKUL5Tfm_7Mu3gP21jY-j2PKUnmgh75iqICIp-Pc5hCjLFw8vf-3vXCQD9-Jqj_xOATwA9SKvdXp3LwdWyuxD2H80rwQLp_GvDwryycSkE4vAT5sGSh1FLVMOAqIi_XYDiNMZCrdv1s-cZbjD5QEVEDOvQ-iM7vfM4F7uRgO-9wiCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏س: لقد نشرتم ليلة أمس أن الولايات المتحدة تمتلك مخزوناً هائلاً من الذخائر، ونفيتم وجود أي نقص. هناك طلب إضافي بقيمة 21 مليار دولار لإعادة التموين، فلماذا هذا ضروري؟  ‏ترامب: لأننا نحتاج إلى المزيد باستمرار. لقد قدمنا ​​دعماً هائلاً لأوكرانيا. هذا ما قاله…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/naya_foriraq/87161" target="_blank">📅 00:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87160">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=ixtBN7UOvkgxm6Vbt-D593tv9dYtZQE1ozovbucBAJ3iyl1JRuYmY6aNguOk4ONtCNnIc6HJC85soNyMxbHDyGBZLzARIs1GPNeIwfwwto_J7hj1oINJ42kLafB2gvEs0puWDHPd-OsrNJLQpkuuQggksLX7S3Hww5Zi2UllEUXzaGx1CWPekbx2tcaO0G-7Fu5o5c83ux8N7n7urk5RZqOjYCltLBpogXIbMiyBi5ksmhTosK5c8fdaDhXQmeSUWJMysTlZCqQHBNoq-GAXxfpERNSjgZfrrBLaQPLtz_ICjYqLkOb9-ELoEpzFHv1j5v12CLTB3DXSiiiJ74zcSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b995216d5d.mp4?token=ixtBN7UOvkgxm6Vbt-D593tv9dYtZQE1ozovbucBAJ3iyl1JRuYmY6aNguOk4ONtCNnIc6HJC85soNyMxbHDyGBZLzARIs1GPNeIwfwwto_J7hj1oINJ42kLafB2gvEs0puWDHPd-OsrNJLQpkuuQggksLX7S3Hww5Zi2UllEUXzaGx1CWPekbx2tcaO0G-7Fu5o5c83ux8N7n7urk5RZqOjYCltLBpogXIbMiyBi5ksmhTosK5c8fdaDhXQmeSUWJMysTlZCqQHBNoq-GAXxfpERNSjgZfrrBLaQPLtz_ICjYqLkOb9-ELoEpzFHv1j5v12CLTB3DXSiiiJ74zcSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:  يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.  ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث -…</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/naya_foriraq/87160" target="_blank">📅 00:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87159">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=JIZkmvQCSGirobcU72Ic74EhfTY0VklfVRc5lgHq714lZyVZ5VKwiFaBehtVpgZNDDRoW0Urnv_to3xFWwY3fVxdRp_vt7W-eNsTRVuh2Kf0f2t-TWoqN7QF2c9JkIwiM9v6uiIOKXP7U6pAP5bLE4MTS6XBqbS0M4n6ynsFHjs_xA8nJSAJ-IW6fYaXfbFakShwVh5LczTtCSMLxDdGTS6RmWVkZMiYD2_k2dnEwlqBGERhGHcEI81YXADNy7OYaHfJJ-RkhttxychjXOq6Hi8xNNdWxPJEOzdjvOigpc0qOZVFBJ_McrG48mSfChmUbyagd0TKq8b6v6iwsUVNpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bad4fe07.mp4?token=JIZkmvQCSGirobcU72Ic74EhfTY0VklfVRc5lgHq714lZyVZ5VKwiFaBehtVpgZNDDRoW0Urnv_to3xFWwY3fVxdRp_vt7W-eNsTRVuh2Kf0f2t-TWoqN7QF2c9JkIwiM9v6uiIOKXP7U6pAP5bLE4MTS6XBqbS0M4n6ynsFHjs_xA8nJSAJ-IW6fYaXfbFakShwVh5LczTtCSMLxDdGTS6RmWVkZMiYD2_k2dnEwlqBGERhGHcEI81YXADNy7OYaHfJJ-RkhttxychjXOq6Hi8xNNdWxPJEOzdjvOigpc0qOZVFBJ_McrG48mSfChmUbyagd0TKq8b6v6iwsUVNpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اطفأء ابار النفط الكويتية علئ الحدود العراقية تحسبا لاحتمال هجوم قادم.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/87159" target="_blank">📅 00:00 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87158">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامب بشأن إيران: أعتقد أن الحرب ستنتهي قريبا جدا.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/87158" target="_blank">📅 23:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87157">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/naya_foriraq/87157" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87156">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/naya_foriraq/87156" target="_blank">📅 23:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87155">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قنوات العربية ؛ الحدث حاليا</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/naya_foriraq/87155" target="_blank">📅 23:46 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87154">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DgGMHJEr3yhAibSObkJd4c-NUAAEmykwnrZdprRGixb4h08VDcMYnGxCxD_Rtg48OC294k2Jj7HA8EIvuNjgtyUHRA-AJMc7fuyq5dBI8XS7zEz4yor69pW3DBVgNzEB8rNNnejyf0nXHd1_PNLtzsJS30Znhnv7HyLSeNjUvwekWqeIumktGAsxrnw6NVIuNsOVL_Li2n3jGMeyvUN7XpWtuRcnM1k2dbFqO9gAtnqYI3YR2izYybV9BkSwaKk8KphQ2ckwReFS3yfINQaCQQ1ri33zKWSrR5RhS4-akV9EPibimBW_plUYLnlqncPoZbzp6An56Z6EYm3cuaxC1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
إلى أعزائي، أعضاء مجلس الشيوخ الجمهوريين، أصدقائي "جميعًا"، يرجى العلم أن المرشح الشيوعي الديمقراطي لمجلس الشيوخ من ولاية ميشيغان، عبد الرحمن محمد السيد، يروج، ربما باعتباره أهم نقطة لديه، إلى إلغاء نظام "الاعتراض" (Filibuster).
لقد شاهدت ذلك بالأمس، وهو يتحدث بحماس شديد عن هذا الموضوع.
إذا نجح، سيكسب الديمقراطيون 4 مقاعد في مجلس الشيوخ، و8 مقاعد في الكونجرس، والعديد من الأصوات الانتخابية والشعبية، وسيكون لديهم محكمة عليا تضم 23 قاضيًا، وسأكون، ويا للأسف، على الرغم من العمل الرائع الذي نقوم به، آخر رئيس جمهوري.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/87154" target="_blank">📅 23:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87153">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5UFH1lsvWioLnheBXOpRoHAiNzRPGEj32ZWS7XXyz5gHiGIJ7rVCtvv22ekYGGxeLTlbAIP03XIK_oLz4FlriqVyvTI4jMCKrTLeH7tKjsrpaFriWjmeEXC5kjescMNUS3jwDJOyI5LXySe9r8-3Jq5ErvFzocmHK3U0C_HzBxh_4cdp3J8PG-LyscwpclFsKCR-jnctKAf4qiZt47tgoM6ij5d1nhSz6TBLBbaZFCou7hdODd6LtR5uw7kr9mmP-Dp11Vu3_I-jvh7fXVlMXrmfA6_UfRBv1kw_00g4GJWy9mH3yEKE34WkF6eSv4hBsrsrTOeOpBUyaCDVzoiDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
من جديد تعاود اسعار النفط العالمية بالارتفاع مع استمرار غلق مضيق هرمز وباب المندب.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/87153" target="_blank">📅 23:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87152">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=s98ILs1DJsE-aXGexGNWCjR2Nfd2q3bPseHy97AbXgmRvH3Tgm50c2NCm1Xu0iQ8PkRL-ffS2kb8QuhXonsQDJpeaWbt2ZyN0vEcJp2LWnnDMsCaHcW_ZJugETazcxexeflCR3Z8HNFXPExY0B0b8zBnGBaTOki04fEclqcDWoX5rmP-nr2XTKaZ_akT_MCy7Y6H2h4gt_Nr41i3Y9X6vZCQCuGqJC4BTBKOPPYYCfiDpHUvgtdd1dDphux4sWyewyOReEXPvc7xJBSwCvNj1E1jKyHXZ5xkWQOk0IMxNkha9hx0Fi7IiaWDxAisGRrsPIX2KSd1FRip7i2BJ55l5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26eeb049c1.mp4?token=s98ILs1DJsE-aXGexGNWCjR2Nfd2q3bPseHy97AbXgmRvH3Tgm50c2NCm1Xu0iQ8PkRL-ffS2kb8QuhXonsQDJpeaWbt2ZyN0vEcJp2LWnnDMsCaHcW_ZJugETazcxexeflCR3Z8HNFXPExY0B0b8zBnGBaTOki04fEclqcDWoX5rmP-nr2XTKaZ_akT_MCy7Y6H2h4gt_Nr41i3Y9X6vZCQCuGqJC4BTBKOPPYYCfiDpHUvgtdd1dDphux4sWyewyOReEXPvc7xJBSwCvNj1E1jKyHXZ5xkWQOk0IMxNkha9hx0Fi7IiaWDxAisGRrsPIX2KSd1FRip7i2BJ55l5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
الناطق الرسمي باسم القائد العام للقوات المسلحة العراقية:
لن تكون هناك فصائل مسلحة في العراق بعد 30 سبتمبر المقبل.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/naya_foriraq/87152" target="_blank">📅 23:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87151">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سبب الاصوات في مضيق هرمز ناتجة عن اطلاقات من قبل حرس الثوري نحو سفن مخالفة لقوانين عبور مضيق هرمز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/87151" target="_blank">📅 22:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87150">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/87150" target="_blank">📅 22:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87149">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eG_XNHyDl0bFgc6DPSPu69HwJTwtr-gtLizIE-N4-gkis1KKWIyyzn3PpghnYu-FlLXaFZE8thOAXOY8zm2gzK5_c4jox0huXHPDqLHVVG41gn3ySiRivE16ND4MOks_zpiDmOhYgIMclDcP0w_V3Awt2tqfjbZB7OkEpOie0KF4TQfX-5-MAVK6WH6D54AfyPgVMJSxutNNookLrqmSKnsHAD9fwaLSLSBJXp_YWWAmLRu-fSnvpLlm7poHiNmWd6enGvakHgd5YVnF6eGtyFukgIRfFDHOWz-oTCIXWfG5KK8Q-ZVSH8qf-iex8SNfyi6h1mQq3QSPROFLn1Kb1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
حشدُ الله… حماةُ الأرض.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/87149" target="_blank">📅 22:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87148">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وقوع انفجارات بالقرب من مطار كابول بافغانستان.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/87148" target="_blank">📅 22:18 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87147">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e086b316fd.mp4?token=O44GAfvm9jcLEVluuPrTDmaGCkSZ03cO4QKTIokTSXIcpnTfc67Y2otSL0lAGX-oVRw2c-joB67j3DQP1BGwqX1OrEGYdB__by3QVg__kX9Pmz8il18N6kvY3-WmiDTyg6ldx8QkCl3ihnogdIsiI8eBNmDUOUzhUQOODOzVIH7dN7KOTAaLk3qvpjyrKVJXJRVQq7XEF86M1_wzAl5Lhm5gfuRk8MVYwuP6m8oD5NfKB6gHCqXtHkambrWRf6FZb5ADQzZTIGPQoHixVcIc0xyeqnUFU3VdaMLwN9i-klnX61qbEWZ_XB2XiDFg0dvhouOtdueDOCrNchJ4QfibBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e086b316fd.mp4?token=O44GAfvm9jcLEVluuPrTDmaGCkSZ03cO4QKTIokTSXIcpnTfc67Y2otSL0lAGX-oVRw2c-joB67j3DQP1BGwqX1OrEGYdB__by3QVg__kX9Pmz8il18N6kvY3-WmiDTyg6ldx8QkCl3ihnogdIsiI8eBNmDUOUzhUQOODOzVIH7dN7KOTAaLk3qvpjyrKVJXJRVQq7XEF86M1_wzAl5Lhm5gfuRk8MVYwuP6m8oD5NfKB6gHCqXtHkambrWRf6FZb5ADQzZTIGPQoHixVcIc0xyeqnUFU3VdaMLwN9i-klnX61qbEWZ_XB2XiDFg0dvhouOtdueDOCrNchJ4QfibBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قنوات العربية ؛ الحدث حاليا</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/naya_foriraq/87147" target="_blank">📅 22:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87146">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJgbnk0V2J_51HG5M1GqdDOVcufgyRNbj4zj2fu2702sjYXojvU8Cok-i_d8umK3oN8-_4P5wRJj_ekYuT6_8MohDUmMQ0t7yLwrhVE7qWyW0a9nKjNTykSSPcbRHKMYkOx4pmmIMou_sISweoGpoKaA2uGDwRTDhnWBSy_cLzHmVgB6GKUjWVXI-F3f9v8EH8fDbJh6YIk4xDroMRrO2xULJ8nKyW1p9D2f97LzuRVfQZqCK1iEef2TGmQdaS289Wcpea-syZLaZmC65sWr53LZTEk4IO--HAAArvwy6gK4vq8y9FyGmUq6y0V6jncdGhLaOMvAKEFMQ6ei5xo99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قاليباف
:
هجوم ضخم قادم... انتظر، لا يهم، إنهم يريدون التفاوض."
‏هذا هو الدبلوماسية المسرحية في حلقة مفرغة.
‏إن استخدام التنمر والوعود الكاذبة والأخبار الكاذبة كوسيلة ضغط هو استراتيجية فاشلة.
‏اعترفوا بالحقائق والتزموا بتعهداتكم. لسنا بحاجة إلى مزيد من المسرحيات.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/87146" target="_blank">📅 22:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87143">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MvnQDI-XyqcxH69efcVFTg5CNwbcAp2bR3Z4lvbWd2QZRk225KiOb4mph817am6xVpF0_tNt5ax1IRQkscm49KRhzH29_F_-hy00gcxxT34nnW_s2uRtsiP5JqhTo_OBt3z8rjBvg56FGUdzgZM12Ms4VL_SnJj2UqjzfnD3GtaJ6JuIg1tmY147VWHMBvDfWmYhiWj6tLJi63rt71qo0eWiS_xocIHJoNyRv65hlg2qw6pvmdevpMH-N1ohQZKPQJKnSER0Qd0nZ0csY2PFKUCCLP_mmlWj86RYH9OPRVRY0wOeG4-IbrCwEOkD7WTxqU3NnJnSL8h4kWcff9z-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKkPrt9qphvdX59jM1ugdwiQOvSP3V_q_HIirg0ZIh3amAxzQxuIS9TOZu_ZFfwTjrzGxsHQGzETPzOkO4SfH7dM7A5ogGU7MsXDmJgymdD59HUam8AUNCZQteBKX_x45qa4m2E0hscpwpZMs-FgejBfeGurSJqPQU2LDVqFwMmIXNrIJVqodOdzIr2oGHDCWztV_-S-eArFdItajbis9XrbnKwC_qmSzVJgBQGvtxW3Mvu9eEzqqBmuki0WFqlowkDbZryCyiqbw2fKDFIR4ubs2yNOJqryGQs8bfyV4PGEDbYdEr7FZ23O0K9ra4xtILSprSfA7s2XYwabX6M6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBbm1zKKDc2KZGVgnclRI7yg5DABHxG63UpUheyp-u4XMXN7dNXRUrXxpA4zRyD72g96ghD4TwSdLkcyVr_KJg7jWK9vDV2JAAhjnW7SZeqhxip0Mv2hFO7OZKNfoGK58L2pyKJFGt0PvcgpW1bsW70FX7-5FDexvQuQ1IUROwp6Hp1STMth34O2vIr-3xSe4qROC1_ATuAEaQbQLeUwPZkCTRQIHZj5nJfSygTHnw63L8-C6RCDNj8gp0HURk7SK0JMpnCdCHsRiY8r0v6gWPggBUMPRppTB-0EIV9gp96lEhPtphmUUhbUUgpdhhmbm3Y1CwkswSrVHXuEnvQewg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انتشار عناصر من جهاز مكافحة الارهاب بالمنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/87143" target="_blank">📅 21:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87142">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في جزيرة قشم</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/87142" target="_blank">📅 21:44 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87141">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXRYIeswxfRXTxWEi1cDC6YPQO2r8pMDQKZuJtqRCd65mxR6qH41cfSxPLdjaL21i887Fp1pr_ajX_qQggHMQOzv-ZuLWAnClr-sBM98b0pl-eBn1ZStEur7tv0Hi_k0aqMwSlJADFC2xHnb3Yb2-E13WiUfjSaF_Afg1S6nff7Cd4xGlB1v-ZiGr8LUUFGBZArKs6FRL-DjbP8cb3HDGKQjU89uuCPWbuB6ASgk-d4l_aan7Ubq_Dh5H-BcymzI5WCXR0-O2ZHq_pHwDhHUlHMqcSeRyZKeMUx5SA_LIefu_DaH1AFXALgNJ8zhdTWZnYSFAKd2lCs8YmSeojQ8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:  يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.  ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث -…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/87141" target="_blank">📅 21:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87140">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇺🇸
الاعلام الاميركي:
يشعر ترامب بغضبٍ شديدٍ في السرّ إزاء التقارير التي كشفت عن تقلص مخزونات الصواريخ الأمريكية، إذ يعتقد أنها تُظهر الولايات المتحدة بمظهر الضعيفة بينما تُمارس ضغوطًا على إيران للتفاوض.
ويُلقي باللوم على التسريبات - وليس على بيت هيغسيث - وقد وجّه وزارة العدل لتحديد المسؤولين عنها.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87140" target="_blank">📅 21:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87139">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv3B3XO9a7VFkhUTXUvXwQn-cuSXE3EPUniC9K3o3BIXMrF77lD0UpaAg7sEmCv7AlnXiX_NtPgYOi6fBgerQC3y_neIMX1P2I4VNm7PfhaLgaWRXCnN7ICzpjT0Ons3toL3MW2T2nEHJfQ2IuMO2A5V0BkjwYfRX98n-CjkrC5H7RIWmGPaFF2PD7H9P6vpJR540Aq2RTpzZkNaqCVwLzZmWnJedgunBTtIqS5Oq3OLKrzkgKabAzAwXa6i7Nr28NaAI_l6aUuwEM_NLZ5pQLA5b7-Qviyw_lLd8RJA7Bdv1p_EVZFU32dq1-qfum0l4WZwQA8PKpXW8ZZYb4BNIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في اربيل</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/87139" target="_blank">📅 21:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87138">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انفجارات في اربيل</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87138" target="_blank">📅 21:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87137">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K48J-9JFY1gcnhsAmeQeDDp4Cj2NHh-ymO0qxxJfMRmXYspnrQx8eehHcgewY2YRpF03hwDJ9OH36f8c-WSwCukUbahRk3P8ndVDfBpOhTZLFBy7asjsQI0QshLA6QufvzUKBQUxoRqweZ1u9iNFpHmPtPmCtGxkV73buZ8g6vYDY-okturhQav2pvU3vyjXdqoupdfKdPz3PbV2CwS9qz7UhnU3Ri8RfncCkNt8nWojFlSiHwwJMVpVgOmDGPF6yWo3Bx8F1L1ppTjbI1VetJNHai5jWSa8iwxT7yr1n_y8uOSKRlaNoDXI4KyuPy5Vha1hRp9YcPW4x_7Qla8qoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارين قرب سفينة حاولت عبور مضيق هرمز على بعد 9 أميال بحرية جنوب شرق كومزار، عمان.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/87137" target="_blank">📅 21:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87136">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762fd91ecb.mp4?token=YvtJGZVqkmyyaYp92SKoQ5IbipyW7sesbD4Xk4dzAvfpgl5pGr4yqdrE4lXRLAYfewXIlZ3-XOlMrMr-RQHWHzpHM_oAqoRG6Yqu5Av6tEyncUNJdnF8gk6qugZ727j_pPjvJl2EBPfzy8TORrLYwagMMpV7IrDrJthY-2mzR3GJzw0Bs093vpj85ZoWhUw0LlaXdMAgry84N8qh3NfKJdlBWlFCeM7ZTz_3wuo9VoKLOBA2q99tR397X7qxRjJt-v2j9x27TRTMHB-XycjGf9vkCujJL2MNuT_8VVrfg3hccY2kQjEDDv_xKjfqbEdKOp0_wAhT4iVHjtEFgO0OVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762fd91ecb.mp4?token=YvtJGZVqkmyyaYp92SKoQ5IbipyW7sesbD4Xk4dzAvfpgl5pGr4yqdrE4lXRLAYfewXIlZ3-XOlMrMr-RQHWHzpHM_oAqoRG6Yqu5Av6tEyncUNJdnF8gk6qugZ727j_pPjvJl2EBPfzy8TORrLYwagMMpV7IrDrJthY-2mzR3GJzw0Bs093vpj85ZoWhUw0LlaXdMAgry84N8qh3NfKJdlBWlFCeM7ZTz_3wuo9VoKLOBA2q99tR397X7qxRjJt-v2j9x27TRTMHB-XycjGf9vkCujJL2MNuT_8VVrfg3hccY2kQjEDDv_xKjfqbEdKOp0_wAhT4iVHjtEFgO0OVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اللحظات الأولية لوقوع الانفجار في مدينة جرمانا</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87136" target="_blank">📅 20:55 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87135">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9GhQfBU3akbH8wFQWOOcQMLwaRMUsQPETKomeEsMyEiL8RgpuRf2MNbiFmtz9ank6_1prdR_5MD47Fhel5k1NlTS90MFV9TltDWyISDOJCuzaaE1XAkeKWzSCfoE_scpbPpmd3pcvWM17OibpKPjX1fKue2vlOHjl59OGbX4SuOtsT_2g4xmHL_XJAk-sNJ9ptWmYzH666m7uYITImPNR8X6rtD8xN5ZdIuqQrl_g1gkGQKWiMx6oGZZwnzn_KNe0SowaU7jnFbYwxGG38DJoWjdQwpiLIu7K4MUr4HTTE4a-0DjuA12IY7-VkgbGADUQv8OUHJmDk22L04sCr88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
صحفي عراقي ؛ قرار إنذار الزيدي للقوات الامنية خوفا من قيام الفصائل باستهداف احد دول الجوار ..</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/87135" target="_blank">📅 20:49 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87134">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfwWWQOoq02FiECnY47LydtjLWtzDSeIIoh2IfvAPZCjSlnjt-nWCiJLekcwhrYr3YS7OepBnXWhngzou58ikvFEUxdeSarYLCtcGfXtG3gQMnxwawbwNEHtTHO-EeeFLveId8uOCwuzmHlEA1WAjeGY1BNaCRQkbscmUPIbe8aN35Y2ouWC2PRVT7OQYtElXh02IHKP3XWt8wGISmsoi-tbyZhF_Cqm8h1hhD9l0H2m2SQcwaYpeDdnvuGkx3RJ1vl34wXhoKIbvdrExZ-1xCnmGCyNpi1uA5_NPfEG7ABPdHG_nd7VblhTjeVs8MrCXit7ZaRq8gTx-D4XcQdzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
تنشر الأخبار المزيفة، كالعادة، شائعات كاذبة ولا أساس لها من الصحة تماما. أنا سعيد للغاية بالعمل الذي يقوم به بيت هيغسيث. كان كل شيء غير عادي، بما في ذلك هجومنا على فنزويلا، حيث تم تحقيق النتيجة في أقل من يوم واحد، مما سمح لنا بتقديم أحد أسوأ المجرمين في أي مكان في العالم، نيكولاس مادورو، إلى العدالة! وبالمثل، فإن إيران، حيث تم دمر البلاد لغرض عدم السماح لها بامتلاك سلاح نووي على الإطلاق، تسير على ما يرام! يحظى بيت باحترام كبير داخل الجيش، وقد حقق تحسينات هائلة، بما في ذلك التخلص من DEI، وزيادة التوظيف إلى المستويات التاريخية. بدأت هذه الشائعات من قبل واشنطن كوم بوست، واحدة من أسوأ وسائل الإعلام في العمل، على الرغم من إخبارهم بقصتهم خاطئة تماما. في الواقع، أعتقد حقا أن "تقاريرهم" المزيفة خيانة! الرئيس دونالد جي. ترامب</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/87134" target="_blank">📅 20:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87133">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0dca0aa65.mp4?token=Zx7JBr4KFbqvN1OkqRDEwSMBl27w7QUe2pKv0X6tAXC0T8lAi6hJLHatCj297f9tRoGb-v8unULcOT1QqBEU3uexLhb5fqSA0zqgUU9OpWfM5-4vKh3j6J8_RuEoX3aN4IR7B6OlNcaFFy7ADexkynslQ23FDccEeNI--Vpvk-DizfDpBpU9MZ57koo8IOoL7rGQy8kZCiy-3jCa42elQCalxkTp5Vk2zfKnxx_e5-vfDzsdnGcLtEulnmgxPMsJT1NFg-ApRBMQv6y6Duh_TMM5tJZo0o47ezP6bEAVHHgqs3MO2vncSqzvHBvNWJDLjCOIhUqYOFviQJdlMwvVXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0dca0aa65.mp4?token=Zx7JBr4KFbqvN1OkqRDEwSMBl27w7QUe2pKv0X6tAXC0T8lAi6hJLHatCj297f9tRoGb-v8unULcOT1QqBEU3uexLhb5fqSA0zqgUU9OpWfM5-4vKh3j6J8_RuEoX3aN4IR7B6OlNcaFFy7ADexkynslQ23FDccEeNI--Vpvk-DizfDpBpU9MZ57koo8IOoL7rGQy8kZCiy-3jCa42elQCalxkTp5Vk2zfKnxx_e5-vfDzsdnGcLtEulnmgxPMsJT1NFg-ApRBMQv6y6Duh_TMM5tJZo0o47ezP6bEAVHHgqs3MO2vncSqzvHBvNWJDLjCOIhUqYOFviQJdlMwvVXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محيط موقع الانفجار في جرمانا</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/87133" target="_blank">📅 20:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87132">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99fe71b04.mp4?token=kqQ3l_5Fw_SkItDZfqOeQ4yx6igQPAI5r75CR0l67s18Z6rAkm91MphLtByhu9ZtqA_x3jfZyMPwHtmEmIt3YpOJbqWDlczYIwSwkxsP_5F8T5svP2P1_24usLhuUmHbSgK-HajQibrhrNzdbqDKnAURpA76akCbwa_x1kMpRPvep-V1ISD0alOtteUIWJZjFDzTqNyHrwXskcUEoA7tm1c2ec77deW8Vz5Q2h8NLDshFrmpBOcQLj5I5h2YMLp05MkRl_Qd5gRrVArFCVIVn1aEIUUSkLzmeXl1gb_XDOhJtTbL3OiHnq6Gl4sYk6Ef1VRdcIZ8gChQzq4UoHy15Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99fe71b04.mp4?token=kqQ3l_5Fw_SkItDZfqOeQ4yx6igQPAI5r75CR0l67s18Z6rAkm91MphLtByhu9ZtqA_x3jfZyMPwHtmEmIt3YpOJbqWDlczYIwSwkxsP_5F8T5svP2P1_24usLhuUmHbSgK-HajQibrhrNzdbqDKnAURpA76akCbwa_x1kMpRPvep-V1ISD0alOtteUIWJZjFDzTqNyHrwXskcUEoA7tm1c2ec77deW8Vz5Q2h8NLDshFrmpBOcQLj5I5h2YMLp05MkRl_Qd5gRrVArFCVIVn1aEIUUSkLzmeXl1gb_XDOhJtTbL3OiHnq6Gl4sYk6Ef1VRdcIZ8gChQzq4UoHy15Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار باص مفخخ وعدد كبير من الضحايا والمصابين</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87132" target="_blank">📅 20:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87131">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaTDULB99iauzjvLh69Bhlaha_L5DzSMNjc6aRko6N98oegSVFnTHLAd7vsRG1-OlUKoPwdf1wt4tXZLjt1isyhM2YvdE-5Czx_nYvkQ_AfW40bq4AdoxmBYwar-BGVCXZW8xgkLMp8oem7EE6n-XwXUbX1HNXdMXVaHLsbdCKecIZhziM_HJ7a_MzFW6Rgs1QSbMV9t6pDv4st-dee2tUF21Hrl2bP3K8-Tve_zBu2A-Ghlws986y3RAH8qjA9_ol91QwFcW9Yy5WypPWJqkUg2pABZ8YepEEfzwf0IKGH9UM1FadjJxTqIkATTOzExCobaSGCOwCKbO65DJ5Up4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عجلة مفخخة قرب مفرق الروضة بمدينة جرمانا</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/87131" target="_blank">📅 20:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87130">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPs5F4WuYUoNz9fGzzwGAIFGbGb_5NEUzvGYf1oyInEODFTPu3HwzrA6PhTF8xEjl5LN_0DeUUO2EEI_f0me0ewnWxx44sdqePLYr2abPBV6AMBmpeTNgjiY1VYPScN-L5T2NhhYAbRC440fOAmN1hWtd56FBBNwnYVlXXqs8k3X2f9iZf4usJ7OIRtY989otF1VhdRbSL-VfTqUBcvBKsxXY6DIcoisMLEBsBgUTeLGsRKPSOv7067DC57HcC15Gmef86TOWGnFzucePwlVd-R9TX-4a6lFLRwtWQHedJebJW3sRP_MPuKyxc0vI_TReD3hRpZNH7ZC5jJ4Mn2LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار عجلة مفخخة قرب مفرق الروضة بمدينة جرمانا</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87130" target="_blank">📅 20:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87129">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوي انفجارات في مدينة جرمانا بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/87129" target="_blank">📅 20:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87128">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دوي انفجارات في مدينة جرمانا بالعاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/87128" target="_blank">📅 20:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87127">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
تفاصيل النص الأولي للخطة الاستراتيجية لإدارة مضيق هرمز
سليمي، عضو رئاسة مجلس الشورى الإسلامي: يخضع النص الأولي لخطة "العمل الاستراتيجي لضمان أمن مضيق هرمز والخليج الفارسي وازدهاره" للمراجعة من قبل لجنة الأمن القومي.
وبحسب هذه الخطة:
يُحظر مرور سفن تابعة للولايات المتحدة، والكيان الصهيوني، وغيرها من الدول المعادية عبر مضيق هرمز.
لا يُسمح للشحنات المتعلقة بالكيان الصهيوني، سواءً كانت عسكرية أو مدنية، بالمرور عبر هذه المنطقة.
كما يشمل الحظر السفن أو الشحنات التي تلعب دورًا في العمليات ضد جبهة المقاومة.
ولن يُسمح للدول والأفراد الذين تسببوا في أضرار لإيران بالمرور عبر مضيق هرمز والخليج الفارسي حتى يتم دفع التعويضات.
يُتوقع فرض غرامات باهظة، تصل إلى 20% من قيمة الشحنة، على المخالفين.
ستُلزم الحكومة، بالتعاون مع القوات المسلحة، بتولي مسؤولياتٍ مثل توجيه الملاحة، ومراقبة حركة السفن، وحماية أمن الخليج الفارسي وبيئته.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87127" target="_blank">📅 19:26 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87126">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NNz9FoxrT0pi6sXVZflcALGPm9Ztrc_9lPfflF3QON0SBzuf3DuoIPjAUUYZKsl9JhfG7DjU-Ere2xfRYWps5mMIttWAKZENCBb2h1Km5eVYRNknJ-EKdOK9QFHCDC6y_hjCv0Cz1fKnpJ32_8oUPn43PXC_XjKaNM4q1Ps0uv-lvKNprLof69L1ntlAOQraXrJshLbvVOn7eOGGFoW6odClHAeP-9nnWcVqOBxN1onWMN2dZTvzc3rekW8QodX2LfgyJ63ucb57KdBZs2xrESPA7fKbyhe-64_BRo620N6su0cE-pNcvvx7jTlQi-BSjFX-KnW8eiY1kzPJQ2Vyzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتشار عناصر من جهاز مكافحة الارهاب بالمنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/87126" target="_blank">📅 19:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87125">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🇾🇪
🇾🇪
مرتزقة السعودية في اليمن يفرون من معسكرات العبر والوديعة الى الصحراء والخط العام بعد تدمير معسكراتهم بمسيرات وصواريخ انصار الله.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87125" target="_blank">📅 18:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87122">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qQ013Xz1XlwQNdqf9lbDfrKAhcQwEQ5YVsoaa_X5upTy_UsB-KXKIq1CekCEcfLZjNor04X2fPsjiglQ-rIZzZl4SQOj_cjZyWk4-cmwYvTFu5sq9IM_YDSBftogandRh-bLxSDcwe0vZ5vZenCSx2ug_Q8Ge7oAnmcd8aurdzNxbWKh0MjRoymfR9cWE1vWIyX8QMds73ubKU7i-pIl8v4XYGYYQhR2hd_JRDKEcwuVR4EO_p6f7L-gIOA7eT5rzwz6MZWHMzEJQ1UxE44Af04ZZTwlFo0Pk1IAGikn0sUTec6OKvRxRjzE4meald0I2fh20M58zjXJCHVSS7t6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nA5xXAmgRQsP2DRzrIcEzL-k6kBINduL1m3bI2QSV0aeTInZNbmugth46pK4buuLXisvQVu0RWisFPiKCg-8IvfKJN8svN2D2p5BXrpuMqwgAKBiE0lEvs-MtjT5j2KFQohB8qso6SjdsDPo5Sku_4h0kxoUXIID98Ssu58u4mVvtf3faL7fTIDlsqHx2rpVLb5478OfIOEg-_jpDNoXS18PCNJqf4k46GbdbqmCtuFAm-4imK9Yqt-lETkDIlUeV02bHr8G5bbLbc3yNConwCpIdyNUL3HGmUPbeP1897JU_Uie1xR6aLaHgRT13L6Mcq9Qip9vyH8Ft4P_nhm_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVRaah-9O4gb1QHeYsXqj6QYSIqA6Xesfrv7NoT7AVkuiTUjuR0YO04An8Q6xQ12l5ebJU-IhPmmZWjwWQVxkRIlSvz37h0NwNWw18o_bWV2R3LFURoDY3E9tTuhdH3TwGGN8Bkh8dC5EmKkhET8gwYtTD9Y6DMlHDGQO7zS0obSvT8eieGAAFi77UpqRIN11DMGHCOlgpWtIrv371JuFsRYwF88UUlM2QjurqA6Z9_agEf7b9aW4uTik04K4vgFq0h58KSxc_RqcQlS-IQuPGvZJWRRlUEqkJFgMtZ8y5mtm5yOWHaUticotGapdNlaAAEZ5VOKIbDiL8-O7zfj3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
شرطة محافظة الانبار غربي العراق:
ضبط كدسٍ من الأسلحة كان مخبأً تحت الأرض، وإلقاء القبض على المتهمين (ا.ع.ف.ج)، و(ا.ع.ف.ج)، و(ن.م.ج.ع). وضُبط خلال العملية (5) بنادق كلاشنكوف، و(2) بندقية (RBK)، و(2) رشاشة (BKC)، و(2) بندقية (G.C) عيار (ناتو)، و(7) أشرطة عتاد (BKC)، و(500) إطلاقة (BKC)، إضافةً إلى (250) إطلاقة من عيارات مختلفة.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87122" target="_blank">📅 18:10 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87121">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اعلام سعودي:
80 مصابا من المرتزقة في مستشفيات مأرب وسيئون بعد هجوم انصار الله.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87121" target="_blank">📅 18:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87120">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07b8e26a8.mp4?token=Fln5hxiNDoNTYCzpGqMWCBwzv0-TrrNQGTZ59f45cgt6IocqgZO3MGcARCGMZ3D8LT5RvmVeC4Os4Z6Ren0aY6snDyFN8jnoeJZVTj3ykSGyg4GHEdlUQu80OUXb2YHrhjLa8An3B8Nykmcj7XFehg2Z2Vp3f3M9ApY37GQZIfy1on_x3TKp8gX3uiAWpOlu3d9pqpLfyChVoBrUERIs5N6uSOcxY679KTdqvmRK6-UpOkAbuqMcRO3Kgwa26qCtELcgZlldIRzVT0rDJm1Du9TvvOYKVKXufM7vcm8Zc-fBx_c95HmU5pnCSXiyMJiy--IO0AYwsOKskvi26PBlQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07b8e26a8.mp4?token=Fln5hxiNDoNTYCzpGqMWCBwzv0-TrrNQGTZ59f45cgt6IocqgZO3MGcARCGMZ3D8LT5RvmVeC4Os4Z6Ren0aY6snDyFN8jnoeJZVTj3ykSGyg4GHEdlUQu80OUXb2YHrhjLa8An3B8Nykmcj7XFehg2Z2Vp3f3M9ApY37GQZIfy1on_x3TKp8gX3uiAWpOlu3d9pqpLfyChVoBrUERIs5N6uSOcxY679KTdqvmRK6-UpOkAbuqMcRO3Kgwa26qCtELcgZlldIRzVT0rDJm1Du9TvvOYKVKXufM7vcm8Zc-fBx_c95HmU5pnCSXiyMJiy--IO0AYwsOKskvi26PBlQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بيان القوات المسلحة اليمنية سيكون في تمام الساعة 5:30م، بعد قليل</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/87120" target="_blank">📅 18:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87119">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
مصدر لنايا:
خروج فرقة مدرعة للجيش العراقي من معسكر التاجي لجهة غير معروفة.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/87119" target="_blank">📅 17:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87118">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
الاعلام الامريكي:
البنتاغون يعقد اجتماعاً طارئاً لمعالجة غضب الرئيس ترامب بشأن التقارير التي تتحدث عن نقص الذخيرة الذي يعاني منه الجيش الأمريكي.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/87118" target="_blank">📅 17:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87117">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/naya_foriraq/87117" target="_blank">📅 17:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87116">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇶
خلية الإعلام الامني
في العراق:
بتوجيه من السيد القائد العام للقوات المسلحة، تقرر رفع مستوى الجاهزية الأمنية والاستعداد القتالي للقوات الأمنية والعسكرية بما يتضمن تنفيذ ممارسات تدريبية وحركة للقطعات وذلك في إطار استمرار ديمومة الجاهزية العالية لجميع تشكيلات القوات الأمنية وتعزيز قدرتها على أداء واجباتها، بما يسهم في ترسيخ الأمن والاستقرار وحماية المواطنين والمصالح العامة.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/87116" target="_blank">📅 17:04 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87115">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed2183872.mp4?token=DZhsbrzbOScuumPR1eri-muLQZCu2UwQFHFYchcQzNo8xa50RRI--fnGBz2yFlxNuajnN1uVsKRo0OZN9V27EKB_9TJCemcq1ugmbdF2r_W6DDA25hHwRzPPVAMyIAKBTqyHj5xA3AB2x0kcecRB45i6vzbZQcvD29cir8iIS1zpYAhfP86l0T7LPYebi6Y8sr_Ja3FtNC9adz3rirubJzi3uHNQjTxZJTvpcbz8L78ypn_Xdn0t8-ZsNTpHx2hGSN4dJ1nkzZ5Vea261Hyzj08TDFVqf0pFaST3NryolCuZ0SBs8Va5EEBpGUJnbyYCfnDdVEpBcaA5vZmI_lmC_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed2183872.mp4?token=DZhsbrzbOScuumPR1eri-muLQZCu2UwQFHFYchcQzNo8xa50RRI--fnGBz2yFlxNuajnN1uVsKRo0OZN9V27EKB_9TJCemcq1ugmbdF2r_W6DDA25hHwRzPPVAMyIAKBTqyHj5xA3AB2x0kcecRB45i6vzbZQcvD29cir8iIS1zpYAhfP86l0T7LPYebi6Y8sr_Ja3FtNC9adz3rirubJzi3uHNQjTxZJTvpcbz8L78ypn_Xdn0t8-ZsNTpHx2hGSN4dJ1nkzZ5Vea261Hyzj08TDFVqf0pFaST3NryolCuZ0SBs8Va5EEBpGUJnbyYCfnDdVEpBcaA5vZmI_lmC_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
وكالة فارس:
رسالة شكر من مقاتلي وحدة الصواريخ التابعة للحرس الثوري الإيراني إلى شعب العراق.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/87115" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87114">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e89f203653.mp4?token=CdMUfBVvH-SkWrX6AbG4yiv4rNy-Ccg3CbzZdeTfLX3tesu9FC4f1XiVcoaNF0JcSwhI6fLZZg3vmb4Rb0cRLLIfBT4XD0xVhx03LP1autVmTOZ_kZVgk_RfV3IGxWORJpz8ToXF8INZNx-wxTDzexl0-CcJ_VQzo477FaQ6FgD11p5o9Snn2uyVeZMqFZS7CW46ys7flFw1lnlqcRKYkxHqwv8n4im7z51I3cICbdrJ_0lATWFsduAyAP8ISOsYFnQkbgZGNNR5qVv-yuGJnHPQTCCtpeBhHRappLIwVDZ2Ni7_fPTFOtTjITMmaX1R7QUQgdnZDbnNv6X08qJdtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e89f203653.mp4?token=CdMUfBVvH-SkWrX6AbG4yiv4rNy-Ccg3CbzZdeTfLX3tesu9FC4f1XiVcoaNF0JcSwhI6fLZZg3vmb4Rb0cRLLIfBT4XD0xVhx03LP1autVmTOZ_kZVgk_RfV3IGxWORJpz8ToXF8INZNx-wxTDzexl0-CcJ_VQzo477FaQ6FgD11p5o9Snn2uyVeZMqFZS7CW46ys7flFw1lnlqcRKYkxHqwv8n4im7z51I3cICbdrJ_0lATWFsduAyAP8ISOsYFnQkbgZGNNR5qVv-yuGJnHPQTCCtpeBhHRappLIwVDZ2Ni7_fPTFOtTjITMmaX1R7QUQgdnZDbnNv6X08qJdtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مصدر يمني لنايا: مقتل عدد من الضباط السعوديين واصابة اخرين في المعسكرات التي استهدفها انصار الله.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87114" target="_blank">📅 16:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87113">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇾🇪
لحظة استهداف انصار الله لمعسكرات مرتزقة السعودية في حضرموت ومأرب بالصواريخ والمسيرات مما اسفر عن اكثر من 45 قتيل كحصيلة اولية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87113" target="_blank">📅 16:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87112">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هجوم مدفعي ومسير يشنه انصار الله على شمال الضالع استهدف مرتزقة السعودية وتسجيل عدة قتلى وجرحى في صفوفهم</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/87112" target="_blank">📅 16:09 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87111">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6675bcd19.mp4?token=IGITscJuyaoezYLInIhQudA2KfgJT0HaAtccsTKcxDiGT941OeCTuIOTs-RHiJ6FBGh0DE-lv9tzYzCNY_zFWNiQEPgJah5McZd3k-CznSbbUq8wmky27Kt5s5K0tKKPoKuOQhy60VcVpjonD94F_qEBotcGGFg1-kkiN8MgV3kukAmmCEHkTV8cUaJvCk-fI6ZhuoH_FRs4TTIGe4u8nmkPsHAgJWkgV4uDP_rWQ-51sdZBke8EzwCq_08J4bvP6DhTIYjizRtAXSqTORr98CSGHAEzilon8wHUihPdsYC3_2HfNLxmB0aU_qwEbNyXnxyOwxvInmwNQ68H1ZtpMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رويترز عن مصادر يمنية: 30 قتيلا على الأقل في استهداف حوثي لمواقع مرتزقة السعودية بحضرموت ومأرب</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/naya_foriraq/87111" target="_blank">📅 15:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87110">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇾🇪
بيان مرتقب للقوات المسلحة اليمنية للإعلان عن عملية عسكرية واسعة ونوعية.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87110" target="_blank">📅 15:38 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87109">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87109" target="_blank">📅 15:34 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87108">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcR7Ighypd9mKbsxhU9nVlk2DrdTqsaRwraWOBWvotHX9o1JoOLxTw1oSRYbYJAXORBnPq--X4PqShPH3hR5RyrAfdneDAfslat9Qc2CGETWC7mvIhID2GUOhLvjHSMFIul-IBX1yhSMIbcRjV-V83J64X62FiDpEh0vBBFCn-O6vMGtHNjiEXon-vRjXQha8KGDEmpjOXxAL1VOAzsrqPCS7aIDgaFT0YFnMvgkyYLdQ0pbt8m15cwCQOdw401EgDd9gIynHtle_BuBztsS8wSsrgxNwnkx_e4a2nDRsHoHGMH2zvzpUPSjHKN72Fo382Koocz0U6CLRun8Z0I2rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
وزير النقل العراقي يوجه بإعفاء مدير الشؤون البحرية ومديرة هيئة ميناء الفاو الكبير من منصبيهما في موانئ العراق.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/87108" target="_blank">📅 15:31 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87107">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">في اول رد كويتي مزلزل
🇰🇼
السلطات الكويتية تلغي ترخيص المدرسة الايرانية في الكويت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/87107" target="_blank">📅 15:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87106">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9BPaZJ5v2KRNixVjWvH7srPu7i0G4OOLpurEvCpbY-ZeALWuAdw0iPleG-1P_3r_uAyQUGzNqdvmfg4kOgjyB4ia3AGW7-y22jGYsqLt6DrMC98kpS1GgdxyA2ZGrrea2xhY8Zg1ls7-2czGjvewio5xZlxReD7DL8Hjcw08a8u2-aYvDu-PQezq2T1SiwmfgoYTKbvuAjTphO1XMuF5WdFvFFANiU6mrGwxQnv91fVqilMHojRcnED4DVM-CK8U9aekwQu5n2vIwbkdNC_ELrQR0z9mTP4994PGWQK6AljYV0rPPue8pL8CigU1YkIRXEfDWq0jxkcVG0adTMEtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
دميتري ميدفيديف:
من العار أن يتم تذكر القصف النووي لهيروشيما وناجازاكي مؤخرًا، ولم يذكر رئيس الوزراء الياباني أو أي مسؤول ياباني آخر ولو مرة واحدة من الذي قام بذلك. اليابان هي تابع للولايات المتحدة، وفي مرحلة ما، ستصبح دولة مارقة.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87106" target="_blank">📅 14:43 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87105">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">السيناتور الامريكي برني ساندرز:
عندما كنت طفلاً، كانت المعركة ضد حرب فيتنام، التي قتلت 59 ألف أمريكي في الحرب، وأكثر من ذلك عندما عادوا إلى الوطن وناموا في شوارع هذا البلد. كانت تلك الحرب مبنية على كذبة.
الحرب في العراق، التي صوتت ضدها عندما كنت في الكونجرس، كانت مبنية على كذبة.
الحرب في إيران - "أوه، إيران ستمتلك سلاحًا نوويًا غدًا وستهاجم الولايات المتحدة" - مبنية على كذبة.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87105" target="_blank">📅 14:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87104">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇶
مديرية مخدرات محافظة الأنبار غربي العراق تُفكِّك شبكةً مكوَّنةً من 19 متهماً وتضبط 408 آلاف حبة كبتاجون</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/87104" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87103">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇹🇷
وزير الخارجية التركي هاكان فيدان:
بإذن الله، ستنتهي المفاوضات بين إيران وأمريكا اليوم بأخبار جيدة. يتم حاليًا مناقشة فترة مدتها 60 يومًا. إذا تم التوصل إلى اتفاق خلال هذه الفترة التي تبلغ 60 يومًا، فيمكن التوصل إلى اتفاق دائم بين الأطراف.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87103" target="_blank">📅 13:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87102">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=HWfLbTEO2tu1PMyhByiRouKEJ29tGUmTJPmDphXYjJbM-wX0EZw455m54rlvqaeE9wlub8nQoEbkg5WPOKPAEoCTN9FGjOR_9mT1yDIhnp-1ZtQdTwwMsFh2_x9f04GavJiqW5z_GqBR1VDrCf38yDtjC8H60VliIfHgKZfXSDjOv9VQEUT-CQ669VfgkjTUu0OiH6Sf05tAvvvs8mQsBZy8UIV_Avl5_3gI4YijvV9-ozruj0ZWCm9pVcmReHpaZ2iAYpXK7HD9MzWs2TBI3bTdvjO9YZYMo_kl5L3121qXwDA-AiC8QPrsdomzuJOJjmy2IL5eMJOsOPcd39HSkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55c345b1d2.mp4?token=HWfLbTEO2tu1PMyhByiRouKEJ29tGUmTJPmDphXYjJbM-wX0EZw455m54rlvqaeE9wlub8nQoEbkg5WPOKPAEoCTN9FGjOR_9mT1yDIhnp-1ZtQdTwwMsFh2_x9f04GavJiqW5z_GqBR1VDrCf38yDtjC8H60VliIfHgKZfXSDjOv9VQEUT-CQ669VfgkjTUu0OiH6Sf05tAvvvs8mQsBZy8UIV_Avl5_3gI4YijvV9-ozruj0ZWCm9pVcmReHpaZ2iAYpXK7HD9MzWs2TBI3bTdvjO9YZYMo_kl5L3121qXwDA-AiC8QPrsdomzuJOJjmy2IL5eMJOsOPcd39HSkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
انصار الله في اليمن يطلقون 8 صواريخ بالستية باتجاه معكسرات مرتزقة الفرقة الأولى التابعة للسعودية.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/87102" target="_blank">📅 13:11 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87101">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي  وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/87101" target="_blank">📅 12:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87100">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇸🇾
صحيفة لبنانية: الجولاني لا يريد دخول قوات سوريا إلى لبنان بشكل منفرد ويرى أن أي وجود عسكري أو أمني يجب أن يأتي ضمن إطار عربي
وجود طرف سوري منفرد في لبنان قد يعيد إلى الأذهان مرحلة الوجود السوري السابق، وهو أمر قد يواجه رفضاً من أطراف لبنانية ودولية</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/87100" target="_blank">📅 12:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-87098">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇰🇵
🇯🇵
توجيهات صادرة عن مكتب الدفاع الياباني للتعامل مع حادثة إطلاق صاروخ باليستي مشتبه به من قبل جمهورية كوريا الديمقراطية الشعبية</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/naya_foriraq/87098" target="_blank">📅 12:19 · 15 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
