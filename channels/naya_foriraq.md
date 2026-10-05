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
<img src="https://cdn4.telesco.pe/file/pY1c3vwG2wyE7Vch64owomQdHqsyrmrvhw_D7WUPt0OJvgyztPDYUaWNz94it0oMxYAxWyArVvz6DUmZaF6lgz75ajTi3g4MwcGUgELi92MhiUp-CRhVvWHddHD9LmT5uQDidbrETJBZmuqho9JvZTYMqsi67zQxxNGOsYaPZAXCPMi0va5HQBnZoB6Gkp9gh5b97CR4InAkGfcxN6UuCgDfnFUeUTWPcxrl4Qh9SlErcOz4O5rDeK69CuBAvfuwn91oodZFurdYmBSYt99D7v1wk9U63aBadSdZ0sT41PL1nLkO_VR_hnknSAKosHtBSR9FO5sA9q6NSXHVaqoxJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 264K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-92553">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">النظام السعودي: سنستهدف كل هدف متحرك في مضيق باب المندب</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/naya_foriraq/92553" target="_blank">📅 12:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92552">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">النظام السعودي يعلن مشاركة 100 طائرة مقاتلة اليوم ضد انصار الله</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/naya_foriraq/92552" target="_blank">📅 12:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92551">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">النظام السعودي يعلن مشاركة 100 طائرة مقاتلة اليوم ضد انصار الله</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/naya_foriraq/92551" target="_blank">📅 12:37 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92550">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇾🇪
🇾🇪
الاهالي يحتفلون في سوق التربة بعد دخول القوات المسلحة اليمنية الى مدينة التربة في تعز وطرد مرتزقة السعودية منها.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/naya_foriraq/92550" target="_blank">📅 12:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92549">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad6eeb18a.mp4?token=Y4hHiu4BakWmR8cWPEv9wCsU20byraH5cmpCt_Mc8hVzNGFTRM2F1R2bKQ1IXmjQ65SKgaaZuR6tFHu5cdBX8QwXOW4DIFJ6I__AY7bGb8ftxGxG8iDVXuuKXWyfsYhOAbD9JCZGq7GDDjdvaWs5psqFm9muMiH3nMXZ4oe36d5o2X8WbpVEOalSQCYUBHoZGmzwg1DWf29f2mSq3hmv04kAuf8iWsTYCDDJ_b-zg-LF8qhozBTE94D7TgD759R0hnfvjvZwN7PU5ajrpDz3Fyi96LOI9nE3LlYjFCI2i5SgUECTDUEXLY0124heWYlnP-LfFh8kiZzSiI6uNhF6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad6eeb18a.mp4?token=Y4hHiu4BakWmR8cWPEv9wCsU20byraH5cmpCt_Mc8hVzNGFTRM2F1R2bKQ1IXmjQ65SKgaaZuR6tFHu5cdBX8QwXOW4DIFJ6I__AY7bGb8ftxGxG8iDVXuuKXWyfsYhOAbD9JCZGq7GDDjdvaWs5psqFm9muMiH3nMXZ4oe36d5o2X8WbpVEOalSQCYUBHoZGmzwg1DWf29f2mSq3hmv04kAuf8iWsTYCDDJ_b-zg-LF8qhozBTE94D7TgD759R0hnfvjvZwN7PU5ajrpDz3Fyi96LOI9nE3LlYjFCI2i5SgUECTDUEXLY0124heWYlnP-LfFh8kiZzSiI6uNhF6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🏴‍☠️
نجحت القوات الروسية في اعتراض وتدمير طائرة أوكرانية مسيّرة انتحارية من طراز "ليوتي" (Liutyi) فوق موسكو باستخدام منظومة الدفاع الجوي المحمولة على الكتف 9K38 إيغلا-إس (Igla-S / SA-24 Grinch)، ما حال دون استهداف الطائرة لمصفاة نفط في المنطقة في اللحظات الأخيرة.</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/naya_foriraq/92549" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92548">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يدور الحديث عن محاولة دهس قوة تابعة للجيش الإسرائيلي. وكان في المركبة المستخدمة في عملية الدهس ثلاثة فلسطينيين، أصيبوا جميعاً بجروح خطيرة جراء إطلاق قوة الجيش الإسرائيلي النار عليهم</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/naya_foriraq/92548" target="_blank">📅 12:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92547">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الاقمار الصناعية تظهر ان خط أنابيب النفط السعودي بين الشرق والغرب قد تعرض للتدمير مرة أخرى وتصاعد اعمدة الدخان منه</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/naya_foriraq/92547" target="_blank">📅 12:11 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92546">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf2Vs840BsEXhssQWOG6zhpP3cXajYmbolK0pzPv7YBvNev7rtU1ZUK1Vf79AYa0FiYtrht3_NrcOZG6Tqg3ef95_Y90RKYsJ04mhF-ka-SCo7e45yubjrs_b1Z1fj71OVfGXaSl6_NL2JU1u-oKULam98aDcYQ9vtOwCys71msE7oa8W8Ivv0wEn9YniK-cHeLzCh5Q0pzUZhyFZaSSMuri_rOVbmRxSLL6Rh3ZwMW468XuUU9TG98JayZA_U1HmHvXq7eg1QebdoP2wSyaJX5M5iKLXV8c3oJ_D2z3pzDKR9wN1rO5zyc14Yhc9FqJvaC83P6qxTL6mLTocI2jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحشد الشعبي يعتقل 45 متهما وتفكيك شبكات للإرهاب وحزب البعث المحظور في 12 محافظة</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/naya_foriraq/92546" target="_blank">📅 12:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92545">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6634fd1307.mp4?token=gUvd_Pf889aaNS3Y1A3Kiywv2mMeIqOLt8yMXZ11WoJhyjoEEW8bGx9cAkNOqZPPd-4MDfSe_u8sM4amOtAi2sYtZ_vLwYPlf4LQQ_5Jku_k74qCLtJe7eOfpWpDsogDrIJe1rrKvxDaYfCBbR4VSZoKmxJR1XHkRPBULujDk90LOND-iBX9jxIU-Cglz354AGoOEo7Ahf9VUdafvI-oV1E553ZsM7sM2z0MKfYm16DtBcaafnQpku8tDeMRZ_DEe9rcJCtBya0Ei3HJFsBrd1fio4mKuu7epzKo2kRktojvjjtA8bDAgw0mzuTzz0AM7VQIm9dDbf6835R00URKmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6634fd1307.mp4?token=gUvd_Pf889aaNS3Y1A3Kiywv2mMeIqOLt8yMXZ11WoJhyjoEEW8bGx9cAkNOqZPPd-4MDfSe_u8sM4amOtAi2sYtZ_vLwYPlf4LQQ_5Jku_k74qCLtJe7eOfpWpDsogDrIJe1rrKvxDaYfCBbR4VSZoKmxJR1XHkRPBULujDk90LOND-iBX9jxIU-Cglz354AGoOEo7Ahf9VUdafvI-oV1E553ZsM7sM2z0MKfYm16DtBcaafnQpku8tDeMRZ_DEe9rcJCtBya0Ei3HJFsBrd1fio4mKuu7epzKo2kRktojvjjtA8bDAgw0mzuTzz0AM7VQIm9dDbf6835R00URKmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/naya_foriraq/92545" target="_blank">📅 11:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92544">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/naya_foriraq/92544" target="_blank">📅 11:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92543">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">رئيس أرامكو:
ضغوط أسعار النفط ستزداد سوءاً حتى إعادة فتح مضيق هرمز وإعادة ملء المخزونات العالمية قد تستغرق عامين بعد إعادة فتح المضيق.</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/naya_foriraq/92543" target="_blank">📅 11:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92542">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">القوات المسلحة اليمنية تصل إلى منزل ما يسمى بالرئيس اليمني (رشاد العليمي) المقيم في العاصمة السعودية الرياض</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/naya_foriraq/92542" target="_blank">📅 11:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92541">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">القوات المسلحة اليمنية تتعامل مع هجوم غادر لمرتزقة الامارات وتتصدى لهجماتهم مع تواصل تقدم انصار الله في جبهة تعز</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/naya_foriraq/92541" target="_blank">📅 11:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92540">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مرتزقة الامارات في اليمن يعلنون بدأ الحرب ضد انصار الله الى جانب مرتزقة السعودية</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/naya_foriraq/92540" target="_blank">📅 11:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92539">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مرتزقة الامارات في اليمن يعلنون بدأ الحرب ضد انصار الله الى جانب مرتزقة السعودية</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/naya_foriraq/92539" target="_blank">📅 11:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92538">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b010f7c4.mp4?token=dHaFlyTwJMBb8ynOtfdebBUJ7wAMqS9P--MAnFAeZ28OHceA91MFv1Zr-Vixkfeq0kNnFa_y-agSgc3GGSViReWAL2YOKnTtxXOJT_pE_5_LAfCxNGr3vklMfcFC2r3TXtXrCaxIgVZSkXsDxaetz9QBuhJ6tQNBo72iao2Cl1tKP6oaojGVOPNYEn8bvvYzm_c5AJtRQX2MiZG0dLXG0lENePmFFY2DPAjUxmXaF6O6HxHcWgzQwmL7T4OSeU6xGFTW07tPgffjWMv2e7ROHAkVvWcRdTvP-JbYhvUrR13n1bcXewW6mQyqHodiMOOh8lHmMl64zIzhH_lQyvMWEQw6LCT2IAoBJ-d6GXAiKoRplegjTxW2CF7K15P0HDbzUOKGeB6bWHpBqFRgKkcr_QaW3wbmM37CMBjtKc4RAz5ej_ZfGv9SgXQuEgd7ehlReMhcVce-VMPdH1Jjwb_Sd0v2kFw-xbkyJ4N9EwSK6J9qvmiPPIp4bfVzZ08FkyR8etVeqGlQH_HjnKRNF5eEERaoEKArXD5_pOwynBy8vCcn9NTsNSzaOvPaWUtAg3yCaKZIkZGT3Nt4CxTIcytPeLpLYGh6nDeXdd-GssAs5hJsnZctFUhRhH9G_6my45Sll2elA-e5xpYyv7AdsfnqpyXZ2ttkTwQ84joGXm-8oT0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b010f7c4.mp4?token=dHaFlyTwJMBb8ynOtfdebBUJ7wAMqS9P--MAnFAeZ28OHceA91MFv1Zr-Vixkfeq0kNnFa_y-agSgc3GGSViReWAL2YOKnTtxXOJT_pE_5_LAfCxNGr3vklMfcFC2r3TXtXrCaxIgVZSkXsDxaetz9QBuhJ6tQNBo72iao2Cl1tKP6oaojGVOPNYEn8bvvYzm_c5AJtRQX2MiZG0dLXG0lENePmFFY2DPAjUxmXaF6O6HxHcWgzQwmL7T4OSeU6xGFTW07tPgffjWMv2e7ROHAkVvWcRdTvP-JbYhvUrR13n1bcXewW6mQyqHodiMOOh8lHmMl64zIzhH_lQyvMWEQw6LCT2IAoBJ-d6GXAiKoRplegjTxW2CF7K15P0HDbzUOKGeB6bWHpBqFRgKkcr_QaW3wbmM37CMBjtKc4RAz5ej_ZfGv9SgXQuEgd7ehlReMhcVce-VMPdH1Jjwb_Sd0v2kFw-xbkyJ4N9EwSK6J9qvmiPPIp4bfVzZ08FkyR8etVeqGlQH_HjnKRNF5eEERaoEKArXD5_pOwynBy8vCcn9NTsNSzaOvPaWUtAg3yCaKZIkZGT3Nt4CxTIcytPeLpLYGh6nDeXdd-GssAs5hJsnZctFUhRhH9G_6my45Sll2elA-e5xpYyv7AdsfnqpyXZ2ttkTwQ84joGXm-8oT0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر ان خط أنابيب النفط السعودي بين الشرق والغرب قد تعرض للتدمير مرة أخرى وتصاعد اعمدة الدخان منه</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/naya_foriraq/92538" target="_blank">📅 11:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92537">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">▫️
تصاعد اعمدة الدخان من بلدة بيت جن في ريف دمشق الغربي.</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/naya_foriraq/92537" target="_blank">📅 10:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92536">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad89acdc29.mp4?token=ibQEufnUgGfZrYyVyH1xITovycZC5g4WShgXk-DXPW8z1hkk329kxGQ-fZhJCvHJZuWXj-AZG5aeqf1IO_EBnwBfdajxfxq3QLDE_MYFxIe7bvgmGYoT00mfvGsw4nVllcsZUypHw_bMk-qw7aBL8p3d_D3ARDNNn0tqBOFVVGARbELcSm6m8-AQjVk7AbDce_PdWX_DL36aH5PQlPTPQA0wcStWcDF8YyIHm0HJlE-sUQN1rdn2d96VEvThWnTLXQsd1Su8KgITB5rWoEh8cSvGwTMHQA7ppQIHNuOssFq8TlfnmrsYUT-k4Lb3PYk6XhgIZ8i_JT2EbsXIT5lzaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad89acdc29.mp4?token=ibQEufnUgGfZrYyVyH1xITovycZC5g4WShgXk-DXPW8z1hkk329kxGQ-fZhJCvHJZuWXj-AZG5aeqf1IO_EBnwBfdajxfxq3QLDE_MYFxIe7bvgmGYoT00mfvGsw4nVllcsZUypHw_bMk-qw7aBL8p3d_D3ARDNNn0tqBOFVVGARbELcSm6m8-AQjVk7AbDce_PdWX_DL36aH5PQlPTPQA0wcStWcDF8YyIHm0HJlE-sUQN1rdn2d96VEvThWnTLXQsd1Su8KgITB5rWoEh8cSvGwTMHQA7ppQIHNuOssFq8TlfnmrsYUT-k4Lb3PYk6XhgIZ8i_JT2EbsXIT5lzaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار ضخم يهز ريف دمشق الغربي</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/naya_foriraq/92536" target="_blank">📅 10:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92535">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇱
اعلام العدو يزعم
: اعتقال سائح أميركي قرب مقر وزارة الدفاع في تل أبيب بعد أن زعم أنه يعتزم تنفيذ عملية.</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/naya_foriraq/92535" target="_blank">📅 09:48 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92534">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxd_igIJ0Mz2ynjbLVdi9OttWNLqnO6wVKBim95F9awjDyyPWfTzkorwsqNvop7NQn0RZJDXZEgGwQXhzUp2Y9s4OnnsMwxnHlwR-6SKYu5V6b7E5MXbOy8JjdoiZ9WhqMh2xAQ2PcBd1kZHw113SHdotly6BQ3iBxfQfeZtL-XUyijspJF3ouRZdX1JEkDLN4_LhiUiiVhSAlvNQm5k42QAQnzmQtIfbkldQgXEgsjbC_SAcUtV_vVlzCqphAsKXQMjdpsFdP-3TWG0d86P52CSeiNZX5l6uuop0rQLl-GOsDyxFBiDtbd3k5L4SGfYTsfb-OkMCAY6lycnhf9LvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استشهاد شرطيين ايرانيين في هجوم على دورية للشرطة بمدينة بمبور جنوب شرقي البلاد</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/naya_foriraq/92534" target="_blank">📅 09:42 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92533">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار ضخم يهز ريف دمشق الغربي</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/92533" target="_blank">📅 09:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92532">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuATB3MYRSJqytFxAbXbfYLhCKd-Ry91dZjDZHj7P7vTgSpcDpHgaV6KfjtI6GVnoEGuWnbYWlT1eXp3DtyV7YFRijOyhoZpPSWhvfOzpO_jrR8QaBSPlSWhLeokJ-Ef7fRcyYPRWccaDvtvhsYvLFCCdziEyRJAFgRl1AFgWFPggVtMnBdIx7F73U-i8Wdkfdo0OXTfwinMGU-H1NzUUuohnF49Awlp9durpKX1hWc-8s4mQDbctiuKTWka8sRlvZWCVZTsIgKFmD0SxaPPV5F218bdoLasKoKOqp7QoRRVc_gusHCJxv6Om7jSWx9eAWXZ_pVRCT1ctgq41Fn62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
توقف حركة الملاحة الجوية في العاصمة السعودية الرياض و مطار الملك عبد العزيز في جدة
.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92532" target="_blank">📅 03:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92531">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/207f1330af.mp4?token=gWH-PbTemXNpULyVoypr5WPv9Fqec04d2hS9ADNoLw2OHUZlXbIOLYd__90UWBhXsezAjhBKCSP5KnqGrzJmmkQZLMkFzmykpanHgwNpOT_U8JU8TEXVPRNT_tbPfHJ9JfhSbZM6wcabxWQHveF5_FGzosI4bzFYVy6d0pRj1PHkYXKHCkHFsHf4gZVM8iu2MWb8-S7DoR_afP2T06clkDUqa8iwRYWl_mA5W67QrI0pG_HO_Hww4uyaEqUDUqnji2uKhyFYuv76H0cPRviIVZcDNbtR67RS5Za6O0IGdzgf1uXkMhZWC1VEchXOfXAW6kH8JFAAPGQj_pm3dJ73BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/207f1330af.mp4?token=gWH-PbTemXNpULyVoypr5WPv9Fqec04d2hS9ADNoLw2OHUZlXbIOLYd__90UWBhXsezAjhBKCSP5KnqGrzJmmkQZLMkFzmykpanHgwNpOT_U8JU8TEXVPRNT_tbPfHJ9JfhSbZM6wcabxWQHveF5_FGzosI4bzFYVy6d0pRj1PHkYXKHCkHFsHf4gZVM8iu2MWb8-S7DoR_afP2T06clkDUqa8iwRYWl_mA5W67QrI0pG_HO_Hww4uyaEqUDUqnji2uKhyFYuv76H0cPRviIVZcDNbtR67RS5Za6O0IGdzgf1uXkMhZWC1VEchXOfXAW6kH8JFAAPGQj_pm3dJ73BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
مشاهد حصرية لنايا...
🇸🇦
من اندلاع حرائق واسعة النطاق في العاصمة السعودية رياض اثر الهجمات الاخيرة للقوات المسلحة اليمنية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/92531" target="_blank">📅 02:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92530">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42d457ab53.mp4?token=c858emqgHL7Qk0Ryx6V-k66PF_0ZG7i3Eq2yfkukgrd1UGBvQGfuponwjcgty4Z4Kba8mFz61M24ZYpC_bCHIFOgNQ4IbtwRysiiARH_jv6vjgMbeTsFvpXM5kYUuiw-8LpgcjXHaoqgzPo-JwCKFSqK0CdFnG_sfig5tilin_q-ef3EJBM3jeXEX56513Uvn5u1g11oq9TtqpGFU8H2PsuUlp2hjjQo9FsBX9Q4GugeCGYbqnUtxxREp_PtcMcJplZuX6XzNAM-Cfa6WkxmwvHp75QJdO9HrLhdVUnga-QPDX5qGWC-YC1DYvttGP20sxGXJ3--YmsdISWg34QSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42d457ab53.mp4?token=c858emqgHL7Qk0Ryx6V-k66PF_0ZG7i3Eq2yfkukgrd1UGBvQGfuponwjcgty4Z4Kba8mFz61M24ZYpC_bCHIFOgNQ4IbtwRysiiARH_jv6vjgMbeTsFvpXM5kYUuiw-8LpgcjXHaoqgzPo-JwCKFSqK0CdFnG_sfig5tilin_q-ef3EJBM3jeXEX56513Uvn5u1g11oq9TtqpGFU8H2PsuUlp2hjjQo9FsBX9Q4GugeCGYbqnUtxxREp_PtcMcJplZuX6XzNAM-Cfa6WkxmwvHp75QJdO9HrLhdVUnga-QPDX5qGWC-YC1DYvttGP20sxGXJ3--YmsdISWg34QSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇸🇾
جيش الاحتلال الاسرائيلي
: رصدت قواتنا شخص سوري متسلل الى جنوب سوريا وفور رصده تم تحيده فورا.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/92530" target="_blank">📅 01:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92528">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tu_STmx8xOGcnpqi1w4JGi4Rn4N0o4ISi4XzwpSD18ONQ5bXKyBioJzNnonrgZJTOZNm0RV9Chj4_JTLOC6ETjn133ITbSEDZ3v9ogACV-1yrZN5bXox_FSi_7Ju4XziePXO8mv_SROFEEw99PDFWJlsDnDyCxp1wMaxMarQovMHYRsMv99ZIUoO-pUp0TQYDviyH8hTG8PbqpwWstoR0YT4sUbgduF6AymYgxACv05Px7KRIbqo914R1N8OWLEMmLH6Y39Zne66QSXFAUcbRFrkVYmqhDuAOJBMg6h7eUjRt2QnoPNum5AyMUCBGO5ZZeSnBnjscO9XEJaXED2KXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rE3-mQGKCEnSLPI6Vp5pEFGqFbrD7mKlQssb-jncVa8Ekac_1W9QxwACSAqzIa4lUnSU7JVmjVYlj8lNGdVrvEm0ZtOE6sTSt1rgAKOL7NElgvGE4cMyWsmJ6I0wbGjWThmwEXPhRdBvY7WK2pKliDOqfJdQ8Tg8ArscHHpEgG-O2ePrQ8rGkS9xAVhtfNCVhYAnhF6n9rXfTxUMRbKVq5X6Duyv7jg22Jdzw_kK54LabEigyrnLJeI2MRemQ3RbPswGLOEwAfBE9Ab-QlkLjZ6bq20A-OqIKDj-zhkLskueOqhdUSNbbe4PA2ZXMOK2nAOSjJ-Ck2JcXaRoe7Et-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
🇸🇦
🇪🇬
بلوكر مصرية كانت مقيمة في السعودية وتعيش حالياً في العراق تعلن أمس عدم احتفالها باليوم الوطني العراقي معللةً ذلك بإقرار قانون الأحوال الشخصية (القانون الجعفري) في العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/92528" target="_blank">📅 00:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92527">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
بعد الحادثة الاخيرة لمحاولة استهداف قاعدة فيرفورد
صرح
مسؤولون أميركيون:
سحبنا قاذفات B-1 من قاعدة فيرفورد في بريطانيا.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92527" target="_blank">📅 23:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92526">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzmMg0_HWtpoxMhgfbbcxNfqZq8nueFA1bmow6PyZOG5Ch937shcper-y516kxuLmCGPiUcG2mTUfjJSlspiG0fg-nhymSDZaEsGkSe6cFh5fmIwpCKhBFD3vFAkKHWRGJwwO-j3OXDPrE8mEkuV-oSHUVkp2gUxBSSPT0eGHaQ5JffLLmW5zccptN4CMJ7gRKZsWmDYuPORXPeg_wchAuzvzvczcTarlfmMBPb7MEbyCVCJSzh_rYqfwCuGY8hlMspm6sb9mgSYhK5nbUt76U28XRWUgb18oSY3M8gygaCf8SLtPabORxWCmNueEwKx9CUo7zguw-R8mzVxnREITQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
نشر خريطة الميثاق الوطني التي أقرّها آخر برلمان عثماني عام 1920 في شوارع إسطنبول، وتُظهر الخريطة مناطق من دول عربية عدة، من بينها العراق.
🇮🇶
ننتضر هيبت الحلبوسي ينشر خريطة العراق خلفه
😆</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92526" target="_blank">📅 23:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92525">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇾🇪
انتشار قوات المسلحة اليمنية في ارجاء مدينة التربة بعد معارك مع المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/92525" target="_blank">📅 23:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92524">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4FAYyPDA_aALjJ3_TfbEgXRkNGu7fyv8rkszFnUamQCH1mn3nXEbe2MBAZ_Om4sDQ-rVpZLoFBVzyctmw-_SSpaIZAbDWxf0oYewwYn36pjk9W1ooUuPJNGVwKt7Eolq4Dm5x_VNeM1stvYfloCn4DaPNNoZhmIFE7KiUixMUpSD54wztIEu5tKG1D9AN2b-r-Gj2Ys88zCFkF5rmOWxVN3nnpP4VL-wX9cX1jFrp9C62hYWvgeiaovlbmSFggcGxFTEKrYj3jQ9Z6PcZKVlmdeyYbirVqq-QjhxdxSRgaPse2ScPTmiPOPgHJvHGTEezbYg5dNZlqgXS61ai6mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استهداف سفينة مجهولة في مضيق باب المندب.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92524" target="_blank">📅 22:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92523">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/92523" target="_blank">📅 21:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92522">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔻
إستهداف مكة والمناطق والفنادق المحيطة بها قد يقع بعد ساعات من الآن !
🔻
تفاصيل صادمة اكثر تابع هنا وانضم
👉🏼
👉🏼
#مكة_شرف_المسلمين</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/92522" target="_blank">📅 21:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92521">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-aiKhj1PFFMWlJFvczcTNO-M7cXF-HiyEN3TzwnVpM1ufn9BZX9KnfO9BI-5M5G4EpEsFmRZMCFhLi4BnxFYbMj7QAzb3sdQwahUu1W_7qwiLhl4n12KpOD5PSr3ypPmoJ38Ovs-4luUSSAwmgixD5_aKaGmicdWeRoa8lEIuFhzHgZl8I7JOfN3hxwr21YBaFz6Ti6coWuHOUT86QT6mYVjZwdqgvOSspT9rkOPLdleo2EP-zbESS7ESWbfZkFJs-alK25k_4kbE9lwQKeS1bA6o6NxBQ2dmCX0mIg_ecpGf63q0jbeS-DKEYsaUBOzDAHv4jYPz8w5V2Klnh10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇨🇳
ترامب
: ترامب يبدو اصغر سنا.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92521" target="_blank">📅 21:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92520">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 106 غارات جوية وصواريخ، استهدف بها الأعيان المدنية في العاصمة صنعاء ومحافظات الجوف وتعز وعمران وحجة وصعدة وذلك من خلال طائرات "F-15" و "تايفون" أقلعت من قاعدتي خميس مشيط والطائف، والعدوان الصاروخي من نجران.
ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1516 غارةً جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/92520" target="_blank">📅 21:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92519">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcdf208476.mp4?token=mxY68wunbOy8b6Jnnav_3T6Psbwi0aQOTGYUuGu6Y57jal6Yh2NjWJ02jYeFEEkr97s0G_DZDTOEgVR7lz6HxqeI_qWcAlzWvsSIG77j643rMKS_Fp5p2VgxNp4knvhfvgCoS_LDAnzrePeXpK7At4fUC7JWh8ZMrTDth2bhtHWHTrQYED2evKZWrNiBozFfnls7bwB4AIZn1Lo74WCrvCJ31PFIH6p-UnZI6nt8vY_dLkafAvEDRwHIjBEjBWIJl6QLHT1TwJ4-SzoFD3Lk8WuKiOH1CTra-iCeUKtHhT67AtO8rp10OYirnzC6pnCf8uNfxW6L-j4qNuJfP8wXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcdf208476.mp4?token=mxY68wunbOy8b6Jnnav_3T6Psbwi0aQOTGYUuGu6Y57jal6Yh2NjWJ02jYeFEEkr97s0G_DZDTOEgVR7lz6HxqeI_qWcAlzWvsSIG77j643rMKS_Fp5p2VgxNp4knvhfvgCoS_LDAnzrePeXpK7At4fUC7JWh8ZMrTDth2bhtHWHTrQYED2evKZWrNiBozFfnls7bwB4AIZn1Lo74WCrvCJ31PFIH6p-UnZI6nt8vY_dLkafAvEDRwHIjBEjBWIJl6QLHT1TwJ4-SzoFD3Lk8WuKiOH1CTra-iCeUKtHhT67AtO8rp10OYirnzC6pnCf8uNfxW6L-j4qNuJfP8wXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇮🇶
🇸🇦
🇪🇬
بلوكر مصرية كانت مقيمة في السعودية وتعيش حالياً في العراق تعلن أمس عدم احتفالها باليوم الوطني العراقي معللةً ذلك بإقرار قانون الأحوال الشخصية (القانون الجعفري) في العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92519" target="_blank">📅 21:17 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92518">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في قشم</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/92518" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92517">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇷
سماع دوي انفجار في قشم</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92517" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92516">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة بفضل الله من التصدي لتشكيلين قتاليين سعوديين نوع" F15" قبل قليل،  في أجواء محافظة تعز وتم إجبارهما على المغادرة، تمت عملية التصدي بعدد من الصواريخ أرض جو محلية الصنع.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92516" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92515">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
أفاد الطيار العماني خلال التحقيق، بأنه كان يخطط لتحطيم الطائرة بالقرب من مطار بن غوريون.
كان يخطط للهبوط بشكل طبيعي، وفي اللحظات الأخيرة، عندما لم يعد من الممكن اعتراضه، كان سيحطّم الطائرة على المبنى.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/92515" target="_blank">📅 20:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92514">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c113cf919.mp4?token=jj4HMYwvYs_G4X5EozpW_zRBqL2kkBvDPdf7ORrfPlwiqTgYBIZNqT0LpC4cefLhORk941UmVie3bdFcpxHN1ude5GHsRDX-ZreQ2SG38rq_teXX4NjihQrD5wD2Jlk1SbAZ8oUNEs-Ybf0sadBiLacpaDNGLmKgvfx77uB_Mf0XXuNDI1qB9fAA3efHBjoHYeLYNNRT4LUdrLM5KT4FY_lXGc38w2mrnJsn3RbBwVW2CQrEugknU2Y-NtTQ4AwObbQpPjd8mWQCRp9UkPPjoZsHqsxzOEg-kZmlAU1HimrI_v_1d_q4TCliXxbCn7VjaqvwK0XIvoSmWb7RSXrf4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c113cf919.mp4?token=jj4HMYwvYs_G4X5EozpW_zRBqL2kkBvDPdf7ORrfPlwiqTgYBIZNqT0LpC4cefLhORk941UmVie3bdFcpxHN1ude5GHsRDX-ZreQ2SG38rq_teXX4NjihQrD5wD2Jlk1SbAZ8oUNEs-Ybf0sadBiLacpaDNGLmKgvfx77uB_Mf0XXuNDI1qB9fAA3efHBjoHYeLYNNRT4LUdrLM5KT4FY_lXGc38w2mrnJsn3RbBwVW2CQrEugknU2Y-NtTQ4AwObbQpPjd8mWQCRp9UkPPjoZsHqsxzOEg-kZmlAU1HimrI_v_1d_q4TCliXxbCn7VjaqvwK0XIvoSmWb7RSXrf4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
دوي صفارات الإنذار خلال جولة المستشار الألماني فريدريش ميرتس والرئيس الأوكراني زيلينسكي في كييف ما دفعهما إلى مغادرة الموقع والتوجه إلى مكان آمن بالتزامن مع هجمات روسية عنيفة.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/92514" target="_blank">📅 20:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92513">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf58c285b.mp4?token=pz8behAvo8TGyWCSlti_AX9vu1wjpZSWdkTQh1w4_K9HVEVaOGYcU9gZ568h37gfTyMn8FOeLoIgVCR1m-e5R1fAl_azWakTauD-5B4kXzSFHUK34fod0cSif6cF1Hpmu8yU_FkWcWFgHdYXjvhgKp9XD0QdyDs6aJr7sQ1K0YbcNz4iYnnAsgwJLdvz3pbjYe6AQtxZ1dqz6GvzxJjiAABE9q71A4Vdg77bnsaj7bcJPVWvZPhG0JjjBmoi7VgTu0LfdosbmTRg5uN0o5P0KuzSunk7M7cpz0W2yEm86bpW_9Sl-ou961AZMHa-mOGxKYvnvfy3_91dg2Ejk2Twqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf58c285b.mp4?token=pz8behAvo8TGyWCSlti_AX9vu1wjpZSWdkTQh1w4_K9HVEVaOGYcU9gZ568h37gfTyMn8FOeLoIgVCR1m-e5R1fAl_azWakTauD-5B4kXzSFHUK34fod0cSif6cF1Hpmu8yU_FkWcWFgHdYXjvhgKp9XD0QdyDs6aJr7sQ1K0YbcNz4iYnnAsgwJLdvz3pbjYe6AQtxZ1dqz6GvzxJjiAABE9q71A4Vdg77bnsaj7bcJPVWvZPhG0JjjBmoi7VgTu0LfdosbmTRg5uN0o5P0KuzSunk7M7cpz0W2yEm86bpW_9Sl-ou961AZMHa-mOGxKYvnvfy3_91dg2Ejk2Twqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
الشيخ اكرم الكعبي:
#إجرامكم_تحت_اقدامنا</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92513" target="_blank">📅 19:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92512">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocmgABEtGhQ_OKkE6lceqGSsBFstZgQRsrKuiMs2nnAWO4fsIi2WHiokaG0k05aaRzjjxGSENMLcF5uVZ2xgJqDS_MzEQaqhK4AgYwFv1OSDOI3-FV0arzpIoEi-j42oad2RJQsK_apm7jvNapPQGd2Ob63z1-hNpXjSCPJpaSM82l9PUbMO_QzSzmO0blzplit_nQYt0f9Hiy2tSUH4M5qPr981YRwJm240NY4yOQg06Txe3Z3HKKRRPg50Uwh0-ZgNGiyfqzylew2pfV14--yEnH3HW9hgds9K4ZR56iRBrdlIQe_2LH35V7KsJLT1DlNMYuJaSJIFxnjYqQQRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
انتشار قوات المسلحة اليمنية في ارجاء مدينة التربة بعد معارك مع المليشيات الموالية للسعودية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/92512" target="_blank">📅 19:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92511">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇶
🔻
تفاصيل العملية النوعية الكبرى التي نفذتها هيئة الحشد الشعبي، والتي أسفرت عن الإطاحة بعدد من كبار تجار المخدرات الدوليين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/92511" target="_blank">📅 19:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92510">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f1232971.mp4?token=M6AFBC5PdyD4j4FVYmpkpMOcXut5DoMqSI1gIBX1ZlDluvCA5fHiDkPXmacvmcrofO345N2Th7f5QB2ON-XsCMFQnkRzkAbAh9_Kh95EsoEIde6NkgWUQEhQp9Jh7LW-9dvQ648f497S0aHMRD4FSTQ6Uaeijh9JeBLpnNwW6Zgdz0xJFF0T1driOk7K64UGP-fXsnjS7K3cY1gXEfWdkw1x0L0lJ5qwizaJjVotFaO5YSEu_LWK43oM3KHJv3EfWCsPCMLszX7T83y7LBqRuNJNxWwijfNnPLiN_Q7Ehs3XNKGN72E0LhW8n1jl8c9VLyZ4RD4l6k4MIw3fdc57sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f1232971.mp4?token=M6AFBC5PdyD4j4FVYmpkpMOcXut5DoMqSI1gIBX1ZlDluvCA5fHiDkPXmacvmcrofO345N2Th7f5QB2ON-XsCMFQnkRzkAbAh9_Kh95EsoEIde6NkgWUQEhQp9Jh7LW-9dvQ648f497S0aHMRD4FSTQ6Uaeijh9JeBLpnNwW6Zgdz0xJFF0T1driOk7K64UGP-fXsnjS7K3cY1gXEfWdkw1x0L0lJ5qwizaJjVotFaO5YSEu_LWK43oM3KHJv3EfWCsPCMLszX7T83y7LBqRuNJNxWwijfNnPLiN_Q7Ehs3XNKGN72E0LhW8n1jl8c9VLyZ4RD4l6k4MIw3fdc57sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بالانتشار في مدينة التربة وتبسط سيطرتها على المباني والمؤسسات الحكومية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/92510" target="_blank">📅 19:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇱
‏إعلام العبري:
3000 جندي أميركي ينتشرون في إسرائيل تحسبا لاندلاع مواجهة جديدة.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92509" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92508">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlaZTLyHg62F3IhmI9PCuyN5oInULz9OOSm0H5vnRh98smLGjw1lPxL0bpu9rskiBHqQzPbNv_wC9755aSXDKx5FmG7BRqyhnAY_KrTiPZUqouX17yF3o4eqLLUvtN0TBXNp9J4ezBEm2kLBcFHYughwesvmNsFR3jFLKtUrnf_CptN-0JYqZ9AW43_q_ojMAaLnQIucYgRESXtCF6ctWp_j3FD2eaXuipO-jYEGyX7qM0ro60wFiFRttCxN0aaeKC3XXyU7bbznuXiJH3Prm4vEyNupLRcxAifEaorEYzGVm5D1VlBPkbxjOaM8ChO509xGp7KVNPntgCm_PBBikQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
حول العالم حرق علم امريكا ليس جنحة جنائية إلا في العراق !</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92508" target="_blank">📅 18:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92507">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇺🇸
اكسيوس عن مسؤول أميركي:
لن نتخذ إجراء عسكريا مباشرا في الوقت الراهن بشأن التطورات في اليمن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92507" target="_blank">📅 18:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92506">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecbo2c20pgaD1n1x-EpfNKJ8UUiBdJ4E0AftmPLw6D2MqKt44ddZwp16NGikPMc-GW40dPUzZuh2aLuaiJifH2QjrBkLD5xv_N0zYk5g5hfzjqHbD3O8xyQ0LG3VhTlv9vHvEzoh4FdjT9_v3IrUUgnAsI4E2DtXFubFuifhYCxATLDZP4TgI2IdY2joQp0Ihc-TnguOA-LudRlHbmNbMXy2t93AIf8l7y-ZTrMA3Y09JlahYoR0iKpsrgLDm9_7mTn64kUSfa0tsW3hg7fXfnSJEVIIISapeo47XAdE8oEDlIExuWiG8MnLg3uD1gc7n_fABjPHQdNI5s8WSo3RTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مطار النجف الأشرف الدولي يستقبل أول طائرة إيرانية بعد استئناف الرحلات
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92506" target="_blank">📅 18:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92505">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل التربة  قلعت البيضا ثارت  كل نشمي حر ثار</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92505" target="_blank">📅 18:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92504">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">القوات المسلحة اليمنية من داخل التربة  قلعت البيضا ثارت  كل نشمي حر ثار</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/92504" target="_blank">📅 18:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92503">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50253c8a21.mp4?token=igZRHQxPnUYwdP0ah_BreXF421xiz4th23ItWaBbacYlCOQd3RkJdPDlbiYQKy7udH82PWtxgRa0NFzUF7Ptk762e09h0vBrJ28VVY1hLNGmp52wSJ92_7BWq5VtLYSyXAXRKTairqGQIv6OX6p-VFedblAFmThThIq0xDYUHm0GlUmUQJt75Vw-tg4EFbdLdXaAJTo9JdYPYNJpXEA6Css11QTI4umCYaMO6VQrE_mTxQCIYLr0hhJniocjqqXBW13P8WraofJIwPPTKQDW4qdFjb-dxhpjuHWzyVVGnCdFtqNMPm_bIT8zfU9NautBjUA4suRUjRrJkDOVMo2Syw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50253c8a21.mp4?token=igZRHQxPnUYwdP0ah_BreXF421xiz4th23ItWaBbacYlCOQd3RkJdPDlbiYQKy7udH82PWtxgRa0NFzUF7Ptk762e09h0vBrJ28VVY1hLNGmp52wSJ92_7BWq5VtLYSyXAXRKTairqGQIv6OX6p-VFedblAFmThThIq0xDYUHm0GlUmUQJt75Vw-tg4EFbdLdXaAJTo9JdYPYNJpXEA6Css11QTI4umCYaMO6VQrE_mTxQCIYLr0hhJniocjqqXBW13P8WraofJIwPPTKQDW4qdFjb-dxhpjuHWzyVVGnCdFtqNMPm_bIT8zfU9NautBjUA4suRUjRrJkDOVMo2Syw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بدخول مدينة التربة</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/92503" target="_blank">📅 18:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92502">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">القوات المسلحة اليمنية تبدأ بدخول مدينة التربة</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92502" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92501">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqslLHRiqe0KakroJJ-Vvi5XTW4UtQg8-4hhHgixs5mh1siXBxC42JfEdu1qL9kpUz643-Xu3fHlj5FTfQBXKztSS9zNoPSN98YmBWVEc3G3OuSe-mqL5yku5GrHtfuD_Mc0kImpDowjaZQiHmwhNJyKSjDk_AauLSVGrJ8gVH6eD_fijXQspRmX9kO6CVKKBjvACq_LE2IBp-7jZFur73WSW5elmKuTMc04ylikHwaErRRzeSGijIbdaEaP8ncUlFOYqUbvdheDvRRhHVvB6xBkYMndyqyjTzKzp6VdBqSLFKGUIHvKBRxo8VgAMM5mNAikCcvZeWLsYEbMrBT0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران العدو السعودي يستهدف مرتزقته ومواقعهم في تعز بعد فرارهم امام القوات المسلحة اليمنية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/92501" target="_blank">📅 17:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92500">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa1ecee80.mp4?token=VqinAV7kR652onvcLWsOeBwjfXMkpSHFmNpMsTm2mpA3nkTr5ahH9WgEDo_lkwQyhpeNXPnZ40zsMsKpNPLfB2WrrXu-iNT7O7puGtGAs9e1wTCpjM4RIWFbLcfPDg29reC4egf8QM8ibDJvrktLN8fsm4xK0LytvDuEtlWycesB8DU83mdNbPDSraZUaHJpid9b_IiPAMl4mPwwOnK9odvQrOqedJ9LD-4a7UATOd09v-N-Ze5h5NJtgVY83_8nLJrE6Dzs3JiAEcVWsmkj-gmMPK3jxbCF6rJoNJUZheC_YnkCnL993ZK3tFr8I0hJtkF9TCHJ1kOlgYWBmLW72Hzb62tQNFT--fShuMDhJvxDBd4RyTB2nDO2UIQTIR8enKWaxqBvoSvOstkOZ6KVOQN1KXQGjVgC5ZFh53ZROS9Qottk880XSTAuvdwCjnXDB0ZPo0kQETcwmdfi_HdCma2JtDUPxH1-x8BjsqCfEDjhi744HyRJEdEuvfBfy65vmNUgFaBdkqf9OqQACgxh2b977rs-1y_cx0V1NCx-flSLnWkDHmX8ESK6LnD7LhgS48Vvalvfofx7Yy7j-j2MI8k-PvkeOe3CSMeCUttAa4lObNYI3CEi6TXX8SCLNsa8nvDGnk7EEfHEMo1gwE1h1IhFA7CGJQnV-8r_sThJNgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa1ecee80.mp4?token=VqinAV7kR652onvcLWsOeBwjfXMkpSHFmNpMsTm2mpA3nkTr5ahH9WgEDo_lkwQyhpeNXPnZ40zsMsKpNPLfB2WrrXu-iNT7O7puGtGAs9e1wTCpjM4RIWFbLcfPDg29reC4egf8QM8ibDJvrktLN8fsm4xK0LytvDuEtlWycesB8DU83mdNbPDSraZUaHJpid9b_IiPAMl4mPwwOnK9odvQrOqedJ9LD-4a7UATOd09v-N-Ze5h5NJtgVY83_8nLJrE6Dzs3JiAEcVWsmkj-gmMPK3jxbCF6rJoNJUZheC_YnkCnL993ZK3tFr8I0hJtkF9TCHJ1kOlgYWBmLW72Hzb62tQNFT--fShuMDhJvxDBd4RyTB2nDO2UIQTIR8enKWaxqBvoSvOstkOZ6KVOQN1KXQGjVgC5ZFh53ZROS9Qottk880XSTAuvdwCjnXDB0ZPo0kQETcwmdfi_HdCma2JtDUPxH1-x8BjsqCfEDjhi744HyRJEdEuvfBfy65vmNUgFaBdkqf9OqQACgxh2b977rs-1y_cx0V1NCx-flSLnWkDHmX8ESK6LnD7LhgS48Vvalvfofx7Yy7j-j2MI8k-PvkeOe3CSMeCUttAa4lObNYI3CEi6TXX8SCLNsa8nvDGnk7EEfHEMo1gwE1h1IhFA7CGJQnV-8r_sThJNgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏القوات المسلحة اليمنية داخل منزل ما يسمى بـ"رئيس البرلمان اليمني" سلطان البركاني جنوبي تعز  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92500" target="_blank">📅 17:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92499">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇱
🇺🇸
تقول السفارة الأمريكية إن نقاط التفتيش في جميع أنحاء الضفة الغربية ستغلق يومي 5 و7 أكتوبر، مما سيمنع فعلياً الدخول إلى " إسرائيل " باستثناء الحالات الطبية والإنسانية.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92499" target="_blank">📅 17:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92498">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm2K_bX3YNvLTfIwb69UqH_jpiWjdZdInReJ1spy9NlyXYDnaI-TxlbQHtOdstX_TzjsBz0uS-OqE62rucurJjwkhu3_as8-IH_7Q_fBOhtYEG4PO8dT1luh3P6B4Gceqf05IuIk5tGGdAZahAPEaMthRYqHqeMnZsr3dNFEZujj03uUMtbm3qpBIjuAA712vnQU3hD3DcLh1MqIRRPCxb4XtBjkKtljG8TKwx_VvnlLej_XPmtdpwy1x-E_3bD22-T8gMCqWffonbSUJMmgametj7aeUnDvymV4UGIy5vHsRRfsH_c3I80wjOSdu2NDS7lYCTsFzQK4swKXJhrZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
حول العالم حرق علم امريكا ليس جنحة جنائية إلا في العراق !</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/92498" target="_blank">📅 17:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92497">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇱
بينيت:
هناك رابط مباشر بين الطائرة وبين 7 أكتوبر، والشعب يستحق إجابات عاجلة.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92497" target="_blank">📅 17:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92496">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjkeUJBEV_gYxa5Qt07gJn_t8w8inrT7r9SJau0APQEto6kRQc2Dmcl9lS1K9Lk1yHIgjGhucxQRoUBd2R5TOjXdaMMVEz8kHIc_EVBbA5n8605navf_VuTsv7-reRFedgmd2iC6yPvrzYhl9oBdWtLv7rZwEdyk4c4rkmAcaHuVv2RGG_KOM8y_hvB8GGK7cjnKxSLbRatJxg36jQQ14ic4NrsLzbT_A4Sa8gTy1gT-YXrkP3m5VSO_V1-PwMCxGy_CLn1kI_TmDOvVZlVJhzHau6desOw51sQFuSnCBJDXWF899t_i7V8FxZG8ZNoWRf3eu-VXlrWG3nUMcnhvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات المسلحة اليمنية تسيطر على طريق تعز–عدن في عدة نقاط على محور التربة
وسيطرت على عدد من المناطق، بينها سوق الصافية، السمسرة، جبل سمدان، والزكيرة، ما أدى إلى استكمال تحرير كل الطرق الحيوية لتعز، تمهيدا للسيطرة على مداخلها ومخارجها، دون دخول قلب المدينة، وإدارتها بالتعاون مع الشرطية المدنية المتواجدة داخلها
كما أن القوات سيطرت دون اشتباكات على الزريقة ومرتفعات جبل منيف، فيما تتواصل المعارك في منطقة البركاني، بالتزامن مع تقدم باتجاه المنصورة والتربة ونجد النشمة جنوب تعز.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92496" target="_blank">📅 16:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92495">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يأمر بتشكيل لجنة تحقيقية بشأن التجاوز على علم الولايات المتحدة خلال يوم السيادة  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/92495" target="_blank">📅 16:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92494">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية
:
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
يواصلُ العدوُّ السعوديُّ المجرمُ عدوانَه الظالمَ على شعبِنا بشنِّه المزيدَ من الغاراتِ العدوانيةِ والتي بلغت خلالَ 12 ساعةً الماضيةَ 50 غارةً جويةً وصاروخًا استهدفَ بها العاصمةَ صنعاءَ والمحافظاتِ الجوفَ وتعزَ وعمرانَ وحجةَ وصعدةَ
ليبلغَ إجمالي غاراتِه العدوانيةِ على شعبِنا منذُ بدءِ التصعيدِ 1460 غارةً جويةً وصاروخًا.
وفي إطارِ الردِّ على هذا العدوانِ نفذتِ القواتُ المسلحةُ اليمنيةُ بعونِ اللهِ عمليتينِ عسكريتينِ نوعيتينِ بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ.
الأولى استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
والأخرى استهدفت شركةَ أرامكو في منطقةِ خريصَ.
وقد حققتِ العمليتانِ أهدافَهما بنجاحٍ بفضلِ اللهِ تعالى وكانتِ الإصاباتُ دقيقةً بفضلِ اللهِ وتسببت بنشوبِ حرائقَ كبيرةٍ في المواقعِ المستهدفةِ.
ستواصلُ القواتُ المسلحةُ دكَّ قواعدِ العدوِّ السعوديِّ المجرمِ ومنشآتِه النفطيةِ بالصواريخِ والمسيراتِ اليمانيةِ الصنعِ والتي أثبتت قدرَتَها على إصابةِ الأهدافِ بدقةٍ ونجاحَها في اختراقِ منظوماتِ التصدي والاعتراضِ الغربيةِ ولن تتوقفَ القواتُ المسلحةُ عن تنفيذِ المزيدِ من العملياتِ المؤلمةِ للعدوِّ السعوديِّ وفي استهدافِ تحشيداتِه وتثبيتِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ.
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 23 ربيع الثاني 1448هـ
الموافقُ 4 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92494" target="_blank">📅 16:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92493">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
تمكنت قواتنا المسلحة _بفضل الله تعالى_ من طرد واستهداف تحشيدات العدو السعودي من شرقي الجوف إثر محاولات فاشلة للتقدم باتجاه مواقع قواتنا المسلحة ونتج عن عملية الاستهداف والطرد ما يلي:
-إحراق عدد كبير من الآليات التابعة لتحشيدات العدو السعودي.
-مصرع وإصابة العشرات من تلك التحشيدات.
-ملاحقة ومطاردة من تبقى منهم في صحراء الجوف.
-استهداف تجمعات تلك التحشيدات بعدد من الصواريخ الباليستية والطائرات المسيّرة.
​التحية لأبناء الجوف ومأرب وهم يقفون موقف الحق مع شعبهم وبلدهم، يقفون إلى جانب قواتهم المسلحة في التصدي الفعال والمؤثر للعدو فأفشلوا _بعون الله_ تحركاته وكسروا بفضل الله زحوفاته فهزموا أدواته ونكلوا بعملائه وأسقطوا خططه وأهدافه ودفنوا في الصحارى والأودية أحلامه وطموحاته وأمانيه .. وهذا هو اليمن الحر العزيز.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92493" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92492">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">في خبر غير مهم
رئيس مرتزقة السعودية:
أعلن بدء العمليات العسكرية لاستعادة ما تبقى من أراضي الجمهورية وبسط سلطة الدولة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92492" target="_blank">📅 15:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92491">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92491" target="_blank">📅 15:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92490">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇱
اعلام العدو:
جبهة اليمن على جدول أعمال الكابينت اليوم
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/92490" target="_blank">📅 15:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92489">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية: عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92489" target="_blank">📅 15:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92488">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇾🇪
وكالة الانباء الفرنسية:
عناصر أنصار الله يقطعون طريقاً رئيساً لمدينة تعز ويحاصرونها
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92488" target="_blank">📅 15:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92487">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي يأمر بتشكيل لجنة تحقيقية بشأن التجاوز على علم الولايات المتحدة خلال يوم السيادة
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/92487" target="_blank">📅 14:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92486">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انصار الله يسيطرون على سوق المركز ويستمرون في التقدم باتجاة التربة في تعز</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/92486" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92485">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNsgZ5zFTc7vybnHstNPX_m3ZIqET8Pj0KfJUBiteL0Omwpkco_qDCetQzywlV4sD_toSnu7bZUF2pLbQugFcekVJLBIb8t-NMmRdtYMJIystTMOTwQ7jmRlQwUdEMYTXSWSsE-OXtVyyqOWQlPX9zASg4FTopJFVPNmq4AYC5z7mrZdzMj5AkPaOM15BsnEMkSN0ME0kZUgJ8ancn2V5FmPiD7AbdghSpbQCvQlBqnrn-vF5JRKpbGX2v6bg4lYOU7Gm9Dg21yHl7zw5r4o19yHVsY4V9k1Wu9nWWW5Ky6EpHB4WN5IIw6A_bCfj4Ilz1BtjDZNzK4herbys2aEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇱
غضب في الشارع العراقي بسبب غزو المنتجات الصهيونية للاسواق العراقية عن طريق الاردن.
العراق كان قد اعفى الاردن من ادخال نحو 399 منتج من الكمارك وهو رقم هائل اكبر مما تستطيع الاردن انتاجه الامر الذي سمح للكيان الصهيوني بادخال منتجاته الى العراق عن طريق الاردن.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/92485" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92484">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b3fa96286.mp4?token=RNsh9wuU7oPWVF7AY12lfV2Vp_R5-JUSJOCEvGdSWIRMRsSdsR6DSf1wGnZMQvntoVxb0NY_NI19wRZem2uMIVApP0ubC8cuy2dQhktrihVIPF_ujQIoHXzviA-OqVhCEN-WM0nWuQbmPiLqy24UZojvBtRGN1c3481RwxQYbBpgJJWh8RDMLXH7l0MHYbRCYXSkaMuJn54K1JwZfFQoKRucIwd349uDRqUBAk4FUgfrIahNmSjd2mJM1AFVCMdd3ZPAYhkFoAdRzWNQevEPNY8bR5foYzANsiEfvo8NgUca-1zQIK2VPejjShe2V-QCtCYusoK3MXB69gZHFHuUIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/92484" target="_blank">📅 13:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92482">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏مصادر يمنية: الحوثيون سيطروا على منزل رئيس البرلمان اليمني سلطان البركاني جنوبي تعز بعد اشتباكات مع القوات الحكومية</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/92482" target="_blank">📅 13:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92481">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKShszTQRss8m0Ab-7CVCngr2PMzpNNLO-s8UHzOhBn_9JN6plegcxGIslycqv_43AO0iOCKQ1KClDJk2VnoJlW1HA8GrDYzIzvlyWjhwV1kUDlb65NjVWwuOPFYOd6LwKOctQ8NWy5F9HIAfZzNJhrdKtPFJNfJFE7YJvNQ0lDTa2xKlk4ul1sn6PdaRehb2db0hjO8T0Mauzb8Dm38JMgfhuejp6iJhWwNi6VUA_8TZVNFmsOre6_WlcrIR_eLmVbMn3uI1L3RW9YAtrIqerac8FF6KH49BTLF36lXHgt-NiuqeBdlb0KFV6e5OANqsCd1n8AyK8NtWpqO2WbiZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بعد أن أغلقت نتيجة الإقتحام..
القائم بالأعمال السويدي يعلن توجه حكومة بلاده نحو إعادة فتح سفارتها في بغداد.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92481" target="_blank">📅 13:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92478">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EZ20Owa3V6tR9vkPwQZclQuG0Fol54UGvTdS5Yrosf9UA4vu5WH8ugvO7nbV5RuPVdlYCFrloefixAA8t6wOsJxOHcE9qfD6e9vfo6IZvpt4zBhb6k8z9OWMAR8vBkWu-KK3_wP3axStTPZVEvYQwJW7pxdJ9Kktq4uaGxCCrK__j72bAlzAon-aRRZWXgxiJUGHO4sENE0rAIhO88qIcXPlncpIuV6tN2XIWwb5f3wE21me2kaNnmacw-jqRKjX53X_pYIfApHnvuBj3OWvMYTlQAmJBPpaiKUQGMD2eK7pESt4WalRrL9eqII3g59AoRpqmBZx0wLQcFcwOQRA8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sACnLc4woABbFnn1D1sHyKWXkAOQ307uzpWzRwzRPuNIJrAix__Vcu4qrTHmi_JSft0L2NpGleNungDF0NSMLSRTpHFSuq2XnelwTL1I2xYjdkWMSUjANVAzBpeNudaHB4wOoIdUpruLDB1JtR6Z7Yj13KzbCdwLo6X1KBv6thjR73f8vLwq6gjOItmz9cGuCzJla9HIYJjT00RcqP_Zi6Gr-EWPzI4ImcdmXoKp3pDew-Ls-eDHvxnpjrLOAMpAbebEVlaJMlmCubq9w7M6YQAsqTx_p37rL94fgp7w9Bh8jF1hjcKiFeKzfoPqSMXFFF7OUPijabmvJZIhORpwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D05UXcI2R_D6tyzMcI9AKk3_1mEUyw2WlEmqBEQseaVS3VpUb5xw6q_SelmfhXqmvuCMY5CEgRdWcXJwYJ8Qdz2-MxEZixUF5wPSNsooDUWB-tSkSzVaZvJ-DbnhMrScDm5f-X-hSvThjouIIn-kyfPWlIL7vU5A2nOmrWZ3HCECWwnshX-M9Yx8ffs51tcjemjjCGWBc3XnKwleP-eBwR8CYZoFLwDphODpviC6iDwxc5gjnBEsf08Ho3pwofCkswqKzdbLGLhuLq_R_HFanjWFydz362BUqwUd8S0ZIerD0lmCHtbTlzAljiNObZbE251UniN17XLdw3CuQbxQVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
من إنفجار العبوة الناسفة التي طالت عجلة تابعة للجيش العراقي في صحراء راوة جنوبي محافظة الموصل؛ حيث أدى ذلك لإستشهاد وإصابة 4 منتسبين من الجيش العراقي.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/92478" target="_blank">📅 13:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇸🇦
توقف العمليات الجوية في مطار الطائف الدولي بالسعودية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/92477" target="_blank">📅 13:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
عملية دهس في القدس المحتلة؛ مقتل مستوطنة كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/92476" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇶
🇮🇷
مطار النجف الأشرف يعلن استئناف عدد من الرحلات الإيرانية.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/92475" target="_blank">📅 11:58 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0012925a86.mp4?token=SHU6vUB8x7B4yF81mxpj9Clc3FFO5OdAk6_DZc_q4ZaYz1xR4ucyfZ8IabbsrRcF15qPCvoKTFTVMj8kiVbTxXMikg83sSKK-ajwqFTRvlDBShnD845ZWJZxC6f4EFWKwLr-z4bC0NThGl1TcimFmgcBVUBuDvJgxinn9yWpp0YLDryzirFsDnkqP4mGx27XLweeGMGEerkdCRjlpfJKjL1jeeKWEEbbGBqlpSj5Qkix3m0bKP7Ogd30BYtAiG7_DxAQPlk40zqfOAkCuUkUCIIcWm3N9OpYsudATjduHtcI3c5-tQG60xSs6X2JFgmd26EBNyiHUDK4U8pp_RQ1IDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0012925a86.mp4?token=SHU6vUB8x7B4yF81mxpj9Clc3FFO5OdAk6_DZc_q4ZaYz1xR4ucyfZ8IabbsrRcF15qPCvoKTFTVMj8kiVbTxXMikg83sSKK-ajwqFTRvlDBShnD845ZWJZxC6f4EFWKwLr-z4bC0NThGl1TcimFmgcBVUBuDvJgxinn9yWpp0YLDryzirFsDnkqP4mGx27XLweeGMGEerkdCRjlpfJKjL1jeeKWEEbbGBqlpSj5Qkix3m0bKP7Ogd30BYtAiG7_DxAQPlk40zqfOAkCuUkUCIIcWm3N9OpYsudATjduHtcI3c5-tQG60xSs6X2JFgmd26EBNyiHUDK4U8pp_RQ1IDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/92474" target="_blank">📅 11:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9lJuRGp70jkvJTTEdlr9ie3iMsAtF6ECvaQkuaU13QTG7daXvUKDlC0JWx7g9NNla5C6o-i4KY4QLfXFbEkQM028k4mU__14wN7o70mm6gLXofXXjS8ddWda03YJIDfXvhzg85CKqfvs5Kqu-jwwZOh9RVGLyDpWub-Elhyo0EWAWTqWaVwr2Cg1O0DZbSsWah8bJOvC7OABQBrvHURWITBAaAW-O9-mLOl0sGLBp968QtXA2kEFFORu2zCr7BW7QbRoAdjtfRMIsJmD0oXqFB_ZvGs4qVlE9spBC_uUYZ2rmOVrkqAGChinkKEYsCvMpxP-m2A0lOdPJ0euzMbAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
الهيئة البحرية البريطانية:
ناقلة نفط أبلغت عن تعرضها لمقذوف مجهول بمضيق هرمز ألحق أضرارا بغرفة المحركات.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/92473" target="_blank">📅 11:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CxhN_QCYP1N9c6-6u96APZxjQJxdUwfzH-KcbOLPfxtYHM43_WYdWeuYO0mK_GX3dJHMzQK1Ze49LAxOtUpgebr3wgqHwGw5lw1D2-ogViZodpCtecqQmHoeajDC_SSwtd1CgphTwY8V_a1_jnSLRUnd85rXPxf42QV8u5IFYHDhLCWvILwyDEBLMBjc_gvgCGyPYbRJ75IR2V8dM1yHj2HWdZVxDb66mkw2DT7Bg5hYR9ixPt5e0v2VtG5HDS66_d5Ogdxn92EuK30aRFgsk6OQ35OrgqgXKrynGdXqN9YqaoTBF3awbumR_NTv6fuv8iRgfwwu9Uk_zR0x-ijOpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية  عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92472" target="_blank">📅 11:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇸🇦
🇾🇪
توثيق من نقطة قريبة لمخازن النفط المشتعلة داخل مصفاة أرامكو بالعاصمة السعودية الرياض جراء دكها بالصواريخ والمسيرات الإنقضاضية اليمنية.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/92471" target="_blank">📅 10:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">النظام السعودي يواصل عملية اخماد الحرائق</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/92470" target="_blank">📅 10:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔻
أوبك بلاس تتوصل إلى اتفاق مبدئي للإبقاء على أهداف إنتاج النفط دون تغيير في نوفمبر المقبل.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/92469" target="_blank">📅 10:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qarfkdmdW9SlkPhn3eo4EuPWxbBfuJ7Hwty1YR2C6RlzcRjU9rdwNXlrhMGTSrAbsNQl1WpmgntY4NRXRgj3_7egX8mP6oRMjOm_bgmpL4Ztga-T1i-AFLKiYxe5LJn497xW4XkmZTtiY8XbRUy3Eg2HDHK2jrxFnGuCvJepJOsq_epEy3eJVoo2u4gAuDFYKt9P7hNlf2VtDfdAELRlsYMTHdlM9ABpw4EqXGuARfAtS86Rvc9m4yoofi3SiqqPr9T9UsgEOLuoghfj3zqc_PY4A0vUWgrv1bOt_NHCzJN55mqA6_k0es4tZ73JIJqF8BWm6zxmYngHi8V2kQ0Cog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
🇺🇦
إنفجارات وتصاعد أعمدة الدخان في العاصمة الأوكرانية كييف عقب هجوم روسي.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/92468" target="_blank">📅 09:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92467">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=D4CcodDAbbL6LYzB6kHPCRt_GkGjAvHueebBeL_hHIjWTstSpoRLGdPA25pfhojVtfeTOY9w5gaNsGE0gBbgI5NROf_8i5-ipE5vprFAuMqgwp2JZAjpE2Fm929whdrX0bmJjv1tkrCuzEcG8T2ZlYNkJefKOwK475lFkOMLaFn9iFlCRBEHhzOtPwd155bhmxG7uPsbgA4jv8-RxqHUm51cgF5rDq137QuCLPcqjFIAhkC5grBgWuOq1GibWKvRyOs4C10JDizVrXWbpe1m-wDmpiYrePyEOr59-iemU_fVWtmwJT9yz51PdqiDK-MjYUdH_hewgeEgJJ6X_ROuMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa57f09733.mp4?token=D4CcodDAbbL6LYzB6kHPCRt_GkGjAvHueebBeL_hHIjWTstSpoRLGdPA25pfhojVtfeTOY9w5gaNsGE0gBbgI5NROf_8i5-ipE5vprFAuMqgwp2JZAjpE2Fm929whdrX0bmJjv1tkrCuzEcG8T2ZlYNkJefKOwK475lFkOMLaFn9iFlCRBEHhzOtPwd155bhmxG7uPsbgA4jv8-RxqHUm51cgF5rDq137QuCLPcqjFIAhkC5grBgWuOq1GibWKvRyOs4C10JDizVrXWbpe1m-wDmpiYrePyEOr59-iemU_fVWtmwJT9yz51PdqiDK-MjYUdH_hewgeEgJJ6X_ROuMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
الأمريكيون، الذين يتحدثون شيئًا مختلفًا في وسائل الإعلام، قد طرحوا مؤخرًا مقترحات من خلال وسيط. ولكن يجب أن يدركوا أن عصر إضاعة الوقت وإملاء المطالب من جانب واحد قد انتهى. وموقف الجمهورية الإسلامية الإيرانية واضح وثابت تمامًا. ولن يتم فتح مضيق هرمز إلا عندما يتم تحقيق الشروط السبعة التي وضعناها استنادًا إلى اتفاقية إسلام آباد.
بناءً على استراتيجية القوة والعقلانية، نحن لا ننفعِل ولا نُرهَب. نحن نقاتل ونتفاوض في الوقت نفسه. نحن موجودون بكل قوتنا في ساحة المعركة العسكرية وسنواجههم بمفاجآت جديدة، وفي الوقت نفسه، نستخدم أدوات الدبلوماسية لترسيخ تفوقنا في الساحة العسكرية وفرض حقوق الشعب الإيراني. لقد ذكرت مرارًا وتكرارًا أن الفائز في ساحة التفاوض هو من أعد نفسه للحرب.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/92467" target="_blank">📅 09:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92466">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
🇮🇷
هزة أرضية بقوة 3.6 ريختر تضرب الحدود الشمالية بين العراق وإيران.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/92466" target="_blank">📅 09:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92465">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYjy-9egTHm2e3vNBB5GhrarFR1UCnQX11xDp7zwwnnlbLaP7lq2ydtxIXtdALje7GVKaxXbZQWubjW4zB8SB09pOF2-uTesiyalVmDgfyqsGK8IuqP9h_4Vqz3-OXD3zCvfTgCCfUeVZGD6R7gpaETRb0c33OOzlws6rMUVevng3nRSSB-R1cIFj4nYFIxapJx4r0guKg4wxrprghqKrkEVlBvljja69blUzFvka3gPmKLkD4cGZXcpEYZb8gNmiA9piV9tuP14O_ZTKQGeXG8bXLtQFoOJAjCquqB2v9spjTDl0K8SCXrOiuUvZBWjNzl8Ab9mwyxdR04YLowWOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
النائب الامريكي جو ويلسون ينتفض
😆
:
شوهدت قوات الحشد الشعبي، وهي قسم رسمي من الأجهزة الأمنية للحكومة العراقية، وهي تدنس العلم الأمريكي بدافع عدم الاحترام وتمجيد النظام القاتل في إيران.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/92465" target="_blank">📅 03:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92463">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">▫️
‏الكويت تقرر سحب الجنسية الكويتية من 415 شخصاً وممن اكتسبها معهم عن طريق التبعية
عيل منو بقى بالكويت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/92463" target="_blank">📅 01:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92462">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGH3FPddaFTgXGpWvDE4AKP4v5xDvbHGxOZVLNc7LA60K0sWEMXUplCEPoWMh7wrhdEsIIm6t1ALQ6bufD0jDyYJFZWMyRP94dtTp7AMx_XtHbyIbP53dDlvqrTO8ESdPLv3lY4wmTpbBBJMyIEDgmJkstKY5IYVD3LdrEcI2R85cpCh9v_SMYQhVPRNkYngUtTUEoxBddwcnKNibRpoXMS7SqbH12AQfQRqEofQkdViKj6-yfqSHAuFy7VAY87q8H9xNq9cvDoOBT_TZIKMI-VQe28GRiqk3SiS8flKf1effn30e4alQQaZBrtKrxAhf54tEP-N6QCI5hNmdZzAjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الرد اليمني وصل،هجوم صاروخي عكسي من اليمن يستهدف السعودية في ينبع واصابة عدد من  المواقع النفطية</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/92462" target="_blank">📅 01:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92461">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxCv82jIU7okMrsSHewTOMfY9pcUfFRHJX5kXCUUvzL-z4JPW--PpRYSoSXn3HvucyiKYL9Y9llIqtX_MLS92SMVH9oS3FfVs-Fb2yKEFGIT-5Z0wI-lpASzuZGQvnTUVnlxb2leBkRSQ_P-jM25DWkBvif7RlNa13ggLcvSwWqa0jVz1VHiDcU3ssIqKI6rsHPVH6DHvebaLa1MuMwqIHBYdsGcbGCYQppDZO4xCbd5IOTzVr8Q1z1L880TNUMtsHCa2tu6wEybSIP2Jwia3HeDrjyqYPU6DfU4-Wwd22e2sordSgtA9lWtPc7nRjcs-jqimiNGaGBljaYf3XOSdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/92461" target="_blank">📅 01:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92460">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">القوات اليمنية المسلحة تستهدف الدمام شرق السعودية</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/92460" target="_blank">📅 01:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92459">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQ7wlfRDrSnpBlajJEN7_yTm4MtZJv-3aux2eA9U5B9UfCS3ukhPekcfPI-YLkG_s7oCPNngoUT5zwxqGlacmNVVfiQl-J2dV7w2x6SesiSR4bQZYHhb0_xhkdCXcd3Gr4qMiFGY3ISbBQqEuXgsMAUInbfdZhjU66Ruwd_B68piavK_SdGIO6CCyVZJotWqGdTNeUcdR8I5aZTlZd1xDUMX_ZNM_JxCLuYMflF2HfN20gH-cn3WQ1oNmtXZLsNARTlIFwAlhsN6wRxec9aFD8Aw1Lj9t7t82SOHEQ3SNmLUc4uNhEQrW-cGa4wPliHFBKRz_dLtmCIlbN-rdJ-VKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تداول ناشطون على مواقع التواصل الاجتماعي وثيقة تشير بمؤشرات امنية خطرة تخص والد مرشح حقيبة وزارة التخطيط و تؤكد انتماء الأخير لعصابات داعش الارهابية</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/92459" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92458">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇸🇦
🇾🇪
غارات سعودية تستهدف محافظة عمران والعاصمة صنعاء</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92458" target="_blank">📅 00:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92457">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=owEozL96scfsumFdP6wtQ431RHQ30S-C2RDelBIkZjOokx7A70rwSY5Sr75VCxHbe3cDgatEYhknDl5vSMgXnSiU7CEeYxRvlhdf2QK8JlM8CbZc7g-UFqd5GpNMGrTZCJlHFeFCUGCjMJOWMSs4ZwyKgBEZ56o6yjwiE5XdU8e3NDUvWk7geLqpAF7RT0Im5YkA74zL5RkFndOigwiKvPw4Ri7Do4PoP1zN4QrIHxBHINBCyJipF9_OtQSvyAglKY4TiAKzrh5t64SbFZ1XfsvuZnxnXAI6rKhmU9cpL7xmBCN9KNxhbvqXTsYM4KoN7mn76InRoz-xWKE_CNOX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab78e7a2b6.mp4?token=owEozL96scfsumFdP6wtQ431RHQ30S-C2RDelBIkZjOokx7A70rwSY5Sr75VCxHbe3cDgatEYhknDl5vSMgXnSiU7CEeYxRvlhdf2QK8JlM8CbZc7g-UFqd5GpNMGrTZCJlHFeFCUGCjMJOWMSs4ZwyKgBEZ56o6yjwiE5XdU8e3NDUvWk7geLqpAF7RT0Im5YkA74zL5RkFndOigwiKvPw4Ri7Do4PoP1zN4QrIHxBHINBCyJipF9_OtQSvyAglKY4TiAKzrh5t64SbFZ1XfsvuZnxnXAI6rKhmU9cpL7xmBCN9KNxhbvqXTsYM4KoN7mn76InRoz-xWKE_CNOX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لدي قرار سأتخذه بشأن إيران. وسنتخذه بالطريقة السهلة أو الصعبة.
‏-لا يمكن لإيران أن تمتلك سلاحاً نووياً. بالمناسبة، كما تعلمون، تخلت إيران فعلياً عن أي خطط لامتلاك سلاح نووي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/92457" target="_blank">📅 00:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92456">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🇷🇺
🔻
خوفا من مسيرات روسيا
‏تقوم ولاية مكلنبورغ-فوربومرن الألمانية ببناء شبكة للكشف عن الطائرات بدون طيار على طول ساحل بحر البلطيق بأكمله، حيث من المقرر أن توفر مئات أجهزة الاستشعار السلبية بيانات في الوقت الفعلي للسلطات بحلول الربيع</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/92456" target="_blank">📅 00:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92455">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالإعلام الحربي</strong></div>
<div class="tg-text">🔴
الرصد اليومي لطلعات العدو الجوية التي يخرق بها السيادة العراقية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/92455" target="_blank">📅 23:46 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92454">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة   بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ  بسمِ اللهِ الرحمنِ الرحيمِ قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/92454" target="_blank">📅 23:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92453">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇸🇦
تعليق الدراسة غداً الأحد في جيزان خوفا من هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/92453" target="_blank">📅 23:22 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92452">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇺🇸
🇮🇷
الاعلام الاميركي:
طرد دبلوماسيين إيرانيين من الولايات المتحدة بعد تجاهلهما أمر المغادرة.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/92452" target="_blank">📅 23:04 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92451">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utj-MXTzXZRqE78QoKhavLLbu6CvXvwvY4iexRA1YxfWRiyySLZbx8_zc4gYJZajwxzjVvaow3DHT44qtb87ds7y4L1s-YfSqIkyioRMNaycFhVs6WYcpHlxphXiJJv3mEpEROYLKHKg_d28Pcu9RNsokxqN0dOqenykUob9TTEdmJPksZVNj2hTxfMWOOoUpZrWIGSY6PhZMktKGFkvWJcROzcVj7dhlDLRY85H65GFDKIW96J-w-lPO7IAso1CfqS23s9oCLNP8xLZWHKKTXteFZqMrVfXtk82QZvV5TmAKR0JKWKXIGZOFQEALO5pqND8N0ZBM5oUqyT8R7BpZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الرئيس الايراني: ‏
اتخذت الحكومة نهجاً جديداً في إدارة هذه الظروف الاستثنائية. تمثلت خطة العدو في الأشهر الأخيرة في قطع شرايين البلاد الحيوية بهدف الضغط على الشعب الإيراني الكريم. وقد ازداد الضغط الاقتصادي، ولكن بفضل الله، وبدعم من الشعب، وبجهود زملائنا في الحكومة، لم نسمح للعدو بتحقيق أهدافه في الحرب الاقتصادية.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/92451" target="_blank">📅 22:53 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92449">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇾🇪
بيان القوات المسلحة اليمنية بشأن تنفيذ عملية عسكرية نوعية استهدفت شركة أرامكو في عاصمة العدو السعودي الرياض وأدت إلى اشتعال النيران في المواقع المستهدفة
بيانٌ صادرٌ عن القواتِ المسلحةِ اليمنيةِ
بسمِ اللهِ الرحمنِ الرحيمِ
قالَ تعالى: {فَمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُوا عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ} صدقَ اللهُ العظيم
في إطارِ الردِّ على العدوانِ السعوديِّ على العاصمةِ صنعاءَ والمحافظاتِ الحرةِ والتي بلغت خلال 24 ساعة الماضية 60 غارة جوية وصاروخ ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد على بلدِنا 1410 غارة وصاروخ
نفذتِ القواتُ المسلحةُ اليمنيةُ عمليةً عسكريةً نوعيةً وذلك بعددٍ من الصواريخِ الباليستيةِ والطائراتِ المسيرةِ استهدفت شركةَ أرامكو في عاصمةِ العدوِّ السعوديِّ الرياضِ.
​وحققتِ العمليةُ هدفَها بنجاحٍ بفضلِ اللهِ
وكانتِ الإصاباتُ دقيقةً ومباشرةً وأدت إلى اشتعالِ النيرانِ في المواقعِ المستهدفةِ.
​إنَّ سفكَ دماءِ اليمنيينَ بهذا الإجرامِ وبهذه الوحشيةِ يُحَتِّمُ على القواتِ المسلحةِ ومعها كلُّ أحرارِ شعبِنا ضرورةَ اتخاذِ ما يلزمُ من خطواتٍ تصعيديةٍ وإجراءاتٍ رادعةٍ تؤكدُ للجميعِ أنَّ ثمنَ الاستهتارِ بدماءِ شعبِنا المؤمنِ سيكونُ كبيرًا وباهظًا وليدركَ العدوُّ المجرمُ أنَّ الاستمرارَ في سفكِ دماءِ شعبِنا سيكلفُه الكثيرَ.
مستمرونَ في فرضِ معادلةِ الحصارِ بالحصارِ والتصعيدِ بالتصعيدِ واستهدافِ التحشيداتِ التابعةِ للعدوِّ السعوديِّ حتى وقفِ العدوانِ وإنهاءِ الحصارِ عن بلدِنا العزيزِ
واللهُ حسبُنا ونعمَ الوكيلُ، نعمَ المولى ونعمَ النصيرُ.
عاشَ اليمنُ حراً عزيزاً مستقلاً،
والنصرُ لليمنِ ولكلِّ أحرارِ الأمةِ.
صنعاءُ، 22 ربيع الثاني 1448هـ
الموافقُ 3 أكتوبر 2026م.
صادرٌ عنِ القواتِ المسلحةِ اليمنيةِ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92449" target="_blank">📅 22:20 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-92448">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
شركة ناقلات النفط العراقية:
تنفيذ عملية نقل مليوني برميل من النفط الخام العراقي بواسطة ناقلة عملاقة من نوع (VLCC) إلى خارج مضيق هرمز.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/92448" target="_blank">📅 22:08 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
