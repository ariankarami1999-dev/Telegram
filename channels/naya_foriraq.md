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
<img src="https://cdn4.telesco.pe/file/hHN-KtnS6JNJw2NUUrZ-gGJkC4e1i0Lmz9pRJ2gFWdOLek1_ZHF0fb2dBgzcs0tbm0pynx0KA8eua1W_7LmRQFSN1NIHwWzCqkdaCh2f16ryn-3BoNfbuS9gxK6B74zY9-yPDjTh4YWARBm0VqE8bkGiJvLjO3mPmz0a4Cg63Ys8gA-FdZP5KHi01Uk2q08J4kR4gOSKa7OTB4TZ9Eq3ZyQUNK-3OZpsOs9BfZDtx1Wk-70hU9pQoYVRvuoZdTcWYmoW7z9_HAJulV49y0HiRzzSjv36EDf84S2fQP8NG_xF0u3pUraZwG4k96RpLGjz3lC9ReFI2HhbmioUCc_WXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 268K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 01:44:06</div>
<hr>

<div class="tg-post" id="msg-84299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_cX3eylwSaIviHwC7oaJO1UEaAK_Pp1ofCwJDe2Vz-RKaeCc9twBVAkRNZNK67Gi0bkienU3pGOwVe_a7Lnd5N5aMWjPlk2Fco-2JxVt4lFI-kqOQlh9hQ-VowpETuYChbKZgMEnBSzFeRZrIKyWzbkUnTlV3uwg9xzr149VvwKSgjASbJ5vsabKxzCC-EfxbInFfQ2Kcndlkuorovm9sDfnyH41PUWkNYdrvgl4fE7vL68876_kwmoA-GtA9T80pVNan2k40ajK7Adlavl-rl59xR_EapFAI1SQVXB2fAUu8mWnyL79xRKkmEy_iNNrEhavR-i6_Ic4ecjwG8Ecg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/naya_foriraq/84299" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1f0fpy8PfbOzFN7kcSmBxDtv2qjJZqUScBbk60DURUrLQ_afRx2zzOyex7bIDxfwTRCQb1Uiquf6IrtxtgPhfiUCK2hJg6jMPF2J6n-Q2J9kHuhZizF7LG0Ndd3MHintSqqn8XqaVNejIxFgthgcMmTI_VqzrIXALlV_dLR04Mi7d0_1KTBSZxiSLREE5P_EQz5_lhcSYLtUJoCCsxpNiBWRU9eQu6km7HCNAB1OkgTwOQhySF5adYRCPPwJGt8aALsTQdaHJQGQDHUPHPHUUq_8uK94NgfSU8P-pNODHVN3CYp4rQWxBL7JjNz8PrBZjBtRXvMtpYBbDNo6wZJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوارع طهران حاليا</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/naya_foriraq/84298" target="_blank">📅 01:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ka-aQoCzb6-Cqq7EMyzqFi4Q-sxqz2oSjnTl1gCKAeUXgGqPMXJhw3ql4Kogp1zGJ2Qz8pBKHpIoOJpUl6OyjXSARj0zP3JqC9GnVA6Eh82Q_6Eui0_fdB8RT667JKApgAA6hgcBkdaKgwuYva2NuqSVT3sArlIlMVXSE5k5eYV11YDdtU5_w-Jw6Twn23FBCc5qE2J3w8b669w3ZMQCzLqKpZknuw5K2_CFuVUypRDsQnzkXgUqN7BK78Ap94pV1-mOTvgn6Zn0b4HoEjBygu5j2-NoigHP-h76vPENfHyVzL2u54Np9AFFdT_R98_mun0BBCay78txEuxs-f9L4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
نحسی و شومی اگه عکس بود
..
@Naya_Press</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/naya_foriraq/84297" target="_blank">📅 01:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQmUR0FtB2I3SiwzXE_h7Jd83jq9kD0YZcdcgbneFamNJrFQsXtHzWPfPJxn9OzivA6QCLZ7ohU3foHEwlw8SxPeQytYqSMF2UX5lt2po6VxwpMtzoVWYez3ToaLUPqpkLsmrTkCXM7FMKPEfxPVJ8JwT8-SLpQ_70rFwRiyJBrWuysQnWJ465DNw6LvHEH4W5_6tcU_51gGN37xrD3dw_1MjMBtQJj3ktnlDoXFTyWfnGJmoc8X8GQvGHsv-R-PcyLjq2qXyangtVfRtX7moUQu_hFJwS6ySpq2yIIK3S2IPTry_sUKRq_NlGCqxfMTBZhgMCW32YlkJecPFa7EqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/84296" target="_blank">📅 01:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انطلاق نهائي كأس العالم بين اسبانيا والارجنتين.</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/84295" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O6w3xirKuVJtCHGdyYUkq3sC0CyjmN6HN6TY9mJ-adndxjgAjhppF5MyUljtxIwb_UZWANaUhBYdCJzQbP7J94x8KMlme4GaXkp_p6vO76IyWSCdC33wdRqoD_ghfK1l-03QPhcjQ3HteuVw7FceTioMZKAKWTgPK5ZeGJ-ZytjvYPJbBa2JGEaP1j1aU--a1hs9mkSDn-cCDNp3rkOMYfGOGcO2n04zI0CNznkBnhfNRbgdA6Z6ITmqpiVMMMx6ONl9hb2ptdhhATOMu3QJkviGf1or2WXkM42mXgMvw1YeFkiTlb72i7eAWo2lNOVdm23yOtsQtI6ACR8buoqzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحزن يعم أرجنتين حليفة ترامب والصهيونية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84294" target="_blank">📅 01:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اسبانيا تدك حليف الصهاينة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84293" target="_blank">📅 01:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">كووووول</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84292" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84291">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">كووووول</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/84291" target="_blank">📅 01:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84290">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔻
المعارضة الكردية الإرهابية في كردستان العراق:
تعرضت مقراتنا إلى هجوم من قبل إيران بعدد من الصواريخ والمسيرات الإنتحارية.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/84290" target="_blank">📅 01:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84289">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مهزلة تحكمية كبرى !
الحكم يلغي هدف لإسبانيا مستحق على الأرجنتين !</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/84289" target="_blank">📅 01:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84288">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxXo6y_cdzKPgV7OJ-8PlWFpP-5AdVRnD3itCiN4Vf5MOu2UXFfFgyo41Vr-HNeDJondHkGREIJMsip7E_ZnWIKeHzcuEXVQX4wUSTobwLcwlQwm_QyqPrwXCkABV-7l_eSRiCVInn6TgxrAfLGWn6jrMt0bmnneJsIQWsGdA4ddltJj9q9RP_QUqa4fLpCmNx9Nm0QtLP12ByiaJHa7VcpDfNbteD3bwBcyp1sg6Ag8mI5wkei35lYr6882T87af0PROz_ifiM5MMwF0EUcgdArSgTX5LlaSkGAi9MkNWccbH6p7MHSXuge9Svd-oXKsqJLwsIBMvMlTiR44BXDzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
المقاومة الإسلامية في العراق:
بسم الله الرحمن الرحيم
​تُجدّد المقاومة الإسلامية تأكيدها بالانخراط المباشر في المعركة ضد العدو الأمريكي إذا ما تمادى في توسيع عدوانه على الجمهورية الإسلامية، وأنها ستستهدف بكل قوة وحزم كافة المصالح والقواعد الأمريكية في البلاد والمنطقة.
​وفي هذا السياق، نلفت إلى أن المقاومة الإسلامية في العراق لم تُنفّذ أي استهداف عسكري ضد القواعد الأمريكية في العراق والمنطقة خلال الأيام الماضية.
​(وَمَا النَّصْرُ إِلَّا مِنْ عِندِ اللَّهِ الْعَزِيزِ الْحَكِيم)
المقاومة الإسلامية في العراق
20-7-2026</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/84288" target="_blank">📅 00:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84287">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OENxKnjTlcNogACUoaR2pkzc3eP1-X0jtXiBYlkQ2edQoiExP10g6XFvYjV_IaXQzNzrjs12eYL7F8kc8in1qn5gPt-VBhtbDeMJb6YS_F6DVfhOflAXkzMw7TepBgU5w6By90l1L5s9QcwqmezeJPoZf-jUUjD9GzVNeHvkHoNkwKSA9BPVplI7rGrf3WGILAI4E_j7ZHFZv9sR5suZwK70Y2kCViWcS8Qd9KXf-g-6hIEEiqF_o4-ZSmpT18dLmpshWackNQQJnQJ0aTtGhlsPEL1RvMiG0GaSFNjq0KETAa1-GHOX-TiBf3iMfziDLzcKv6SQGSzsa6htUJis4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
واشنطن بوست :
مسؤول أمريكي حذّر من أن توسيع العمليات الأمريكية سيظل محدودًا بسبب تناقص مخزونات أنظمة الدفاع الجوي والذخائر بعيدة المدى، إضافةً إلى القيود التي تعوق إرسال المزيد من القوات والطائرات إلى المنطقة نتيجة الأضرار التي لحقت بها بسبب المعارك. لا نملك ما يكفي لمواصلة العمليات بأمان، ولا أعتقد أن البيت الأبيض يدرك ذلك”، على حد قول المسؤول</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/84287" target="_blank">📅 00:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84286">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين جراء هجوم إيراني</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84286" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84285">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات عنيفة تهز البحرين جراء هجوم إيراني</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84285" target="_blank">📅 00:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84284">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سماع دوي انفجار بقضاء كويا في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84284" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84283">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84283" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/naya_foriraq/84283" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84282">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">يا فاطمة الزهراء</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84282" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84280">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84280" target="_blank">📅 00:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84279">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLUfisRos7iczuBobbczsrS4lXdzbYDIcBmgvSbfSyZjw0hvrqovio6UUX20uWs3ZSwUXGyl10gyOoq9Dyxaey4IS72Vx6vWRnzQ45LHgiO64kxCw8-8K5D_XmInRenRcmgADFG0gn9a1R69Yd1ELZ9MIs7loST9XWB-5pWZOVsKHZL24K-EycsxoVM6H9d8COccI_28Bfyjg3sSaVtahWvVsGaupmguLG29FQHfXPy3VZeQNIuyeregYJZJnXJrwdMb5pB-cJ7vTNCg_MzEXIbPzkHLKD4lQioavZ3JODy8EEf9_f66nI4i8jIj9zDDFUPXAzhXel39cyZigzexeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسقاط طائرة تجسس معادية في منطقة كهكيلويه بجنوب ايران من قبل الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/84279" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84278">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الله اكبر... اصابات في صفوف الجيش الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84278" target="_blank">📅 23:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84277">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02dfa7de95.mp4?token=n5QyRa1eq4dyGKZArdHhEb2qvJThXG2vh2FOloOZliO5w2oAXum2LHtcnsguONKqf8bkM-ygX9vPckYPdIOcBbQbRp_X9qdtOL6iICIEXZ1gipYnyj8Cl2K0oZPQS4Ufv9EMlfTilOF1GrUwi2Om-Ti_EFh9psR7sqrmZaOV13XengloNPmrCxuTBLiKIUwZmg7wtS4QcZRu0hp2a1U-ikCa_0isW-3Qts4psFvYq8XhKHoFO-IOTBBowgv_RG-MzSIF1didZR9zfbJf-CuyXJMSW6dou5Nhxb_AS5AV7xomlVz318mzS-0s7Lre-CkNjxXZstt2rJiFlKVvBPgAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02dfa7de95.mp4?token=n5QyRa1eq4dyGKZArdHhEb2qvJThXG2vh2FOloOZliO5w2oAXum2LHtcnsguONKqf8bkM-ygX9vPckYPdIOcBbQbRp_X9qdtOL6iICIEXZ1gipYnyj8Cl2K0oZPQS4Ufv9EMlfTilOF1GrUwi2Om-Ti_EFh9psR7sqrmZaOV13XengloNPmrCxuTBLiKIUwZmg7wtS4QcZRu0hp2a1U-ikCa_0isW-3Qts4psFvYq8XhKHoFO-IOTBBowgv_RG-MzSIF1didZR9zfbJf-CuyXJMSW6dou5Nhxb_AS5AV7xomlVz318mzS-0s7Lre-CkNjxXZstt2rJiFlKVvBPgAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Parents of U.S. troops, get your children out of the Persian Gulf region. Your president does not care about their lives.
We miss you man
#مرد_ميدان
🇮🇷
سرباز سردار قاسم سليماني</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84277" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84276">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxObvp5OA5pL9e2B8ISC25h-rmPoePmMLWmJRC2b9ITda9oc2N1WNP5h8ewWIDRVRp0YKu1pSMbee5Ygh36edYgYk9Zfv9Aq58NhPhjDem-eSab6zb4WxKn-m0YEGbWBNNQ0JGcIVbqy-zMyzgWQ6S3IPMB15njrjBrYg2TMedRC6Azv_UhqkFxmmp9SP64suj85WrAZ5h1oM-vAv_EFT3toEJbnkYckbiru-iBwMcLTwEBcnm0mWubr-DCoCOwu9UZHvJXeic3C-drUUmuhDoDaCKwQlqwGlpcw0nsgM3CJa8tvAQY7IkVXjaJkB02D2Q7rK4hwXS2Qlccpg_Gwlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😆
Just imagine, study a lot of time in air dynamic , IT , Mechanical Engineering then The Lurs are taking this technology to reverse engineer and use donkey to cary the best US equipment MQ9</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/84276" target="_blank">📅 22:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84275">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">الاعلام الاميركي: 16 عسكريا أمريكيا قتلوا وأصيب أكثر من 430 آخرين منذ اندلاع الحرب مع إيران في فبراير الماضي.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/84275" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84273">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84273" target="_blank">📅 22:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84272">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/84272" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/naya_foriraq/84272" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84271">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84271" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84270">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84270" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84269">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84269" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84268">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مقتل جندي امريكي بشمال العراق</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/84268" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84267">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انطلاق نهائي كأس العالم بين اسبانيا والارجنتين.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84267" target="_blank">📅 22:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84266">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
دفاعًا عن مقتل اثنين من أفراد الخدمة الأمريكية، رفض ترامب الانتقادات من خلال مقارنة الصراع بالحروب السابقة، وسأل:
"هل سألتم يومًا كم عدد الأشخاص الذين لقوا حتفهم في فيتنام؟ هل سألتم يومًا كم عدد الأشخاص الذين لقوا حتفهم في أفغانستان في يوم واحد؟"</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84266" target="_blank">📅 22:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84265">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ace39da0.mp4?token=cE-rOYyV8NyY7Pa97UIVxDqlXbzaQb1PvI6iQ3RDFRXhZRWjbQHSfP2RRB9P3yp7AQ-Fq4A0g6uxYi24ucKZuauhvjs0BhS8S5AU0X5pPmuqWhBKI3WF1eKa5ZeTN8qX2AJkpKKDJEjW2iHL04469cS7gQS49zZtCketoRtuKe9WzfmsfMZhvPia6zFlmmdXYsvuprJsm5cAg4ujt8YuXAdVAcZZTyz_lRPdrFFSwhu8bmGSfpkvUcUdbYST54mIR-04xt9N58T8X6h5XXtm9c5I9aX7HUTxoLV9Aqwj6EPhv-QfS-qxo2iuReNrQZgUHmuw6WXfOVLHphN6msgsgVLZRxTAo89A6sV5cA_V7OT6K_zhqsvDXBPlDgdX8xdTvp-cyLC0AmPXjlqDBH-I_q83FWUXkWURjyAtYznPqRdIhOqGMNL0wyG-1V-lFC6qg6ZuLMsK4W5SQs3Tu-Ay5vUCXlkZ_JPihsOgV8pvcnhKxwe9QdSRsscZNg1frvxE_gcqD9ojRdIBBODhau8kkMdv00BYIgP9cKeOsc1uOVXwb0nqItrMZnodepgNeduQPbK6LhRlDMA8TNc07HFk_4fJx0UNzY8tgbvNQG0lvexqQSLpTC9lx6EDLoOKQ29GZmsml2QiGaC6HIYsHwq1UoJy19k0Y5Jarsg9kvDbBeE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ace39da0.mp4?token=cE-rOYyV8NyY7Pa97UIVxDqlXbzaQb1PvI6iQ3RDFRXhZRWjbQHSfP2RRB9P3yp7AQ-Fq4A0g6uxYi24ucKZuauhvjs0BhS8S5AU0X5pPmuqWhBKI3WF1eKa5ZeTN8qX2AJkpKKDJEjW2iHL04469cS7gQS49zZtCketoRtuKe9WzfmsfMZhvPia6zFlmmdXYsvuprJsm5cAg4ujt8YuXAdVAcZZTyz_lRPdrFFSwhu8bmGSfpkvUcUdbYST54mIR-04xt9N58T8X6h5XXtm9c5I9aX7HUTxoLV9Aqwj6EPhv-QfS-qxo2iuReNrQZgUHmuw6WXfOVLHphN6msgsgVLZRxTAo89A6sV5cA_V7OT6K_zhqsvDXBPlDgdX8xdTvp-cyLC0AmPXjlqDBH-I_q83FWUXkWURjyAtYznPqRdIhOqGMNL0wyG-1V-lFC6qg6ZuLMsK4W5SQs3Tu-Ay5vUCXlkZ_JPihsOgV8pvcnhKxwe9QdSRsscZNg1frvxE_gcqD9ojRdIBBODhau8kkMdv00BYIgP9cKeOsc1uOVXwb0nqItrMZnodepgNeduQPbK6LhRlDMA8TNc07HFk_4fJx0UNzY8tgbvNQG0lvexqQSLpTC9lx6EDLoOKQ29GZmsml2QiGaC6HIYsHwq1UoJy19k0Y5Jarsg9kvDbBeE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الحمدالله كادر القناة يشجع رونالدو
😆
سييييييييييي</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/84265" target="_blank">📅 22:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84264">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏
رئيس مجلس الأعيان الأردني:
إيران تشكل خطرا على جميع دول الإقليم</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84264" target="_blank">📅 21:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84263">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/84263" target="_blank">📅 21:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84262">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">الكويت تعترف بتعرض المصالح الأمريكية على أراضيها لاستهداف بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/84262" target="_blank">📅 21:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84261">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇾🇪
بيان للقوات المسلحة اليمنية يوم غد إن شاء الله للإعلان عن موقف مهم</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84261" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84260">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇮🇶
🇮🇷
انفجار في منطقة عبادان المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/84260" target="_blank">📅 21:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84259">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">م/ توضيح
🔻
جمهورنا العزيز...
نؤكد لكم أن الفيديو الذي نُشر على أنه يوثق قصف محطة كهرباء الصبية في الكويت هو فيديو قديم ولا يعود إلى الأحداث الحالية.
ومن باب الأمانة والمصداقية الإعلامية نتقدم إليكم بخالص الاعتذار عن هذا الخطأ غير المقصود ونؤكد التزامنا بالتحقق من صحة المواد المنشورة قبل نشرها حرصًا على نقل المعلومات بدقة والحفاظ على ثقة متابعينا.
شكرًا لتفهمكم وثقتكم المستمرة.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84259" target="_blank">📅 20:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇺🇸
🇮🇷
نييورك بوست : ترامب يدافع عن الحرب: "هل سألتم يومًا كم عدد القتلى في فيتنام؟ ... لقد ماتوا لأنهم لا يريدون أن تمتلك إيران سلاحًا نوويًا، ولا يريدون أن يُدمَّر الشرق الأوسط"</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/84258" target="_blank">📅 20:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇮🇶
🇮🇷
وزارة الخارجية العراقي:
رئيس الوزراء العراقي يزور طهران نهاية الأسبوع الجاري.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84257" target="_blank">📅 20:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سماع دوي انفجار في محافظة السليمانية</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84256" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtV1ckVaQNWDvXbxItdy5w5EUArTsUYnAwCo8y77In_XDdPUpQPKkZ84UgMMbM0vAllNTnL5gPoHFzodjZNupCpCzMSqZ690sPsiIXo2fCS312lV2Xz91G4_GMGguiG3jyS-z0wRnkvcP3nGuI74bgs1HwSQsf7YmFtdsBfHGtURYHgSDJiOMEF3lwjZqByuvJo-4jv_F1OYert9IsCNxIxmhredY0-g1fWurfVAjfGRW0L2xAUmjvssVv0QAhXqKKZ46C17UcV0JfGx7BszvRhHG4Y3jzASKriT94KJJii7cpi9-3pr3fbQvBAQ7nvnqpbnKZ_A2fi0U1dsqaKh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P9Bp1dVufA6AWDG9vPGIfYfOXe-ghhwuPU6-9_c9IBvrriBicV_r2dUEacCeMblWaEOainHSV82-Bzt-_UjXYRLYvM599Vp-bCuodHGQ6E17GV1K8ptnAV9XfIC_Xe72orYygg2OFIykDh-PGrz99rA0LeiLOLV8LfUpk9xrWbXWN3mItsikVEOBESFob_B7pSEUk0nzaUlyoFUZNq8Sdc1Uv3rGvCEc0NcgfvS2z_EWqcS07J07qcjn5NPR8RKU7V4VL3jaSi5qXZWsWtubrlZkKfrzkqid2gN6YheDboYQF9b7sk3EWB04mWW7dt2OV6_9NNp-WDRl6mbsl3AbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZFGcPDNj6-ehHXDxHtSzK1KiLjebfjFBvR-pVsWkMCrCrSoxOM0Egk76bD311YtDJXkD1ZMoNIIJpiM1umafgbdVeghxel22Av-jLFgB-SeLmxFMCeU8DglEDNhcWF4RdUcqdpH9IFhhQKOuteQbLjdVDiwWkaYaTZiRHvQQws55gr2rr3q5zOAnuRkfQ6r5tE6guO4p6YepRHz76MbIzESa-RHewoPh5BWwS8PuFBtsjRMhiUZsFFN6qlLCCXNUo3asCgIosCSEh1Zr3qeosAiYnj4YcOPHHPbHyPTVCaXsQUGAK2jJ9EtEPGJFqw24Rx918RAyh4mw0TwZWK96w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
قسم العلاقات العامة للجيش الايراني:
قبل ساعات، تم اعتراض وإسقاط بنجاح صاروخ كروز معادٍ.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/84253" target="_blank">📅 20:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16bb68cab4.mp4?token=iv7e-VPip0Sh8ABwnNk0DosYoIWBEJ5FHUCGiupkAUQVGKXi_G-fmwF0wjB-95v6U_e4rw1zZi16A2hC7BraphNhVTT_0wyKliU2RAFkFPH5S36Zcvwn4KXhX3caFaEtyQTawd8E2JVVnNv6xUsHZ4Fr7Wrp9TUmrGI82twGp1gUcaVX13016YoUy3cc4WqmSALn2oS27at-H6y00tN40kWORgWPw9gYleoeTbZB_YL9qwy4Bbn0aYpEtQalB1Htot9H_YZ6fe87I5peqNjf7yVc-SZSlrlgh0dmyK4yZySBgcykLXlJbRiLj_IigC3jmH5Fjg_8YkQvfrCdrADv6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16bb68cab4.mp4?token=iv7e-VPip0Sh8ABwnNk0DosYoIWBEJ5FHUCGiupkAUQVGKXi_G-fmwF0wjB-95v6U_e4rw1zZi16A2hC7BraphNhVTT_0wyKliU2RAFkFPH5S36Zcvwn4KXhX3caFaEtyQTawd8E2JVVnNv6xUsHZ4Fr7Wrp9TUmrGI82twGp1gUcaVX13016YoUy3cc4WqmSALn2oS27at-H6y00tN40kWORgWPw9gYleoeTbZB_YL9qwy4Bbn0aYpEtQalB1Htot9H_YZ6fe87I5peqNjf7yVc-SZSlrlgh0dmyK4yZySBgcykLXlJbRiLj_IigC3jmH5Fjg_8YkQvfrCdrADv6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
الخارجية الأردنية:
أبلغنا القائم بالأعمال الإيراني رسالة احتجاج شديدة اللهجة.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84252" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngcEhxyZhPROme92uQLKymG2yIrnbG__dGcCqbzA8DOwNsxIMrtCRvR3tvQkwQxSzsyB3AFECMOnyeHiD1OUxishcZcs-kSUKR8zf7MtmYXV_nNAt-sejNIoh8UDa40b0RAgvIBrvZTbj2Yigkfq_C0zXkOYlTRFh4wZLdwnPFSApJ3w4KfFZitvetG1HT4BR8z3Sz3SMbtEjnzlAzyc-Fx30LbtAJrOo3KnNE7YwrOTbiV_xyXXSGOsWPtj4CtfXG4VggvHOSBqbyTCqrWNq6nV64YDAWUNWe0PdbIxbv6og_oyDhktNsnm65ruG8cVJ323nIxDJpsUwovJF8cIgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Is still ours
King of Hormuz</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84251" target="_blank">📅 20:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84248">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxD72GCnU1zzslvHBYWBhzRxliHxritxFpLK7UKQE3d4Xd0Vumz2YbRU9A01JaTEk9arDTqCCJOyg5Z3DP-o12JSM_oaTH8iklmbUAjatH6g3LC9uodJVGHOzV-I0FZBCOwajLvJp2qMBh96iljS6Elo72FYlOsNzslThAfFHl8UDs1SKKRDJdufpOc68W1-VbA4evylOFHTotsyVcMlauYbj53pwfLBiP3K2JfG5ZbC0rS_JAOdV6XdJwKECblry-egi3qiv-lqcE-WAsAv5GakX6Z5fyCRtIHJhOii9pBDMQOxabdL9gcLSJWd9RXnwhsluJ-uXgz08rFlYh4tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jkYpyYpYP77HmMvvu7PBSyQgZ0ofx0azST4D5IcyIcJxNcN8HQxCoqXV380u8rW2kkRFXYu3Nx0xZ09Jnj5UiwE7caV-xwWGTLkhln-2VmekH1NNjnYsRE1XigI31uLUbN2vXDuyKFL9J7fNgKmdtCmaDmEJ7Ra7Zk4EEuu80dyPNS56x3OVxUR_SlRRxRVesxCOCxVD_MwAcv4TlaC1L1UlM5WjC5JNrI7oCTpiwmbDqg30PtfO7YfVkZa5HVaeIlB9V5NJ6Kjahgk7BQU5yFfD-vH636yHNVhaNBq3DC8PSN5v5oPYz-4hszf71oIvzmpuKjjUng4dfa946W86JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jBw-1yK4yZmi20CTd9aDQtT0EgApqKtAgH__QqRcGMh2xYR-Pr2GB0GyJ79vrzXXbKd4x7HCbCNvcYsJzt9yJ-pJdhaTL6FogvTtognRoeu-J-sKZsUUfse8mpe-XHUTbHSYD5tZdOmUpql85z5JKv-Thna2w2BFVszMe7pvPNvecFkieZTZsbadhWf080OpC9JsDaQbukli7NgZm8DPa6mnZdvpeT9TFdvXmzxRmUdYsJ7M-KQSn8geoUZLiBubcWj-VJFNLCI_7y4j8MEzlERFp18F3drtM_WjlN0p_SJsVYNUSX_GLYr4mjfQk787ZeBziFxF6KyWUmggJi54WQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استهداف وإسقاط طائرة مسيرة أمريكية من طراز MQ9 بواسطة أنظمة الدفاع الجوي التابعة للجيش الايراني</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84248" target="_blank">📅 19:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84247">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">جيش الاحتلال الاسرائيلي:
قبل قليل اعترض سلاح الجو طائرةً مسيّرة تم رصدها في منطقة الحدود مع سوريا.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84247" target="_blank">📅 19:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84246">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/84246" target="_blank">📅 19:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84245">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">هجوم إيراني يطال محطة كهرباء حطين في الكويت</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/84245" target="_blank">📅 19:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84244">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVKNhi7NnI5nalSQJtReYjIAj2ZSP7i4XH7N3lrRpdf9s0YJD3PQ3qYr2YzRCLnCEB2VbySt_MxbB9Ev0ELyyJ0U31ussbN5se170aGrY5kcRU86sVPvi47DfakuhQkYVBBSRSP9d9MdfZpHVoMbFYpIr94nsoKcyj1rPBf2_Mpcd3vAZ6YBpsYYyYGkFcJ_rePFhtI3afXFS4XbF3wbbcwtcuRnOnnkg5lwEsggbPZ7Ch7AWMOK_dwfaHdTzZekGGi5vsk--r_8eKto4wjaNbKZoAMHkEQP3b6ZhsHNybH0LpE1ZYfqhwYsdDRCVJjJulKS7PQZ1n0CYj8DEQi2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسقاط طائرة تجسس معادية في منطقة كهكيلويه بجنوب ايران من قبل الحرس الثوري الايراني.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84244" target="_blank">📅 19:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏الاعلام العبري: تقديرات أمنية إسرائيلية بأن قيادة إيران ستأمر بشن هجوم على إسرائيل</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/84243" target="_blank">📅 19:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انفجارات تهز دولة الكويت من جديد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/84241" target="_blank">📅 18:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84240">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الاحتلال الاسرائيلي يعترف  بمشاركته بالتصدي لصواريخ الايرانية المتجهه لقواعد الاحتلال في الاردن</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/84240" target="_blank">📅 18:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84239">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=KKmBA49Noep4FjgqzBNxai-VocVbxdk1RJlfKt_-PNXIV0vsW2lRLM3F5-HHZjUwODH82i8NTZZamHszbZUu2Xjmi702V6ISUaVoOypKyEVGLItDzSBvRZfTR87UsGT1Ft-KUwQMWljV3jx6999E_RhHLzinfWNLhqrTG8pdOzKJtrfM0YQlC7cI4t481YkMHPnCTulyvOtqxH_U2ZrLAT4YzIN2fuHZHW5uH8As9sYOApMewmy3k1mjb9qofQQvk9NAoWxjgWyyt-q85Rt1MqQ6hgsj5eD5E7vWg0KrY3z_FVFhZodvCm-Q5-_MOT4cWDYSwM4RZbWoDp-j9oTqJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24db6b1462.mp4?token=KKmBA49Noep4FjgqzBNxai-VocVbxdk1RJlfKt_-PNXIV0vsW2lRLM3F5-HHZjUwODH82i8NTZZamHszbZUu2Xjmi702V6ISUaVoOypKyEVGLItDzSBvRZfTR87UsGT1Ft-KUwQMWljV3jx6999E_RhHLzinfWNLhqrTG8pdOzKJtrfM0YQlC7cI4t481YkMHPnCTulyvOtqxH_U2ZrLAT4YzIN2fuHZHW5uH8As9sYOApMewmy3k1mjb9qofQQvk9NAoWxjgWyyt-q85Rt1MqQ6hgsj5eD5E7vWg0KrY3z_FVFhZodvCm-Q5-_MOT4cWDYSwM4RZbWoDp-j9oTqJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع أعمدة الدخان من مدينة دزفول الإيرانية يرجح انه عدوان أمريكي انطلق من الكويت ..</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/84239" target="_blank">📅 17:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84238">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS3dsHTq6tmGuOuanEPkJrgHfLhXMrBUb63lJrLWcn82UbvD0Yh7M9R_XpgRO_BmJMdwc7mGNcq8mAUODwx4n8A07Kt9-KTX0rHxW_3aPvhsVLZigsg5217f1logPbu6KpTA8z0fhK53r5J8Pj3SnGOuJ7cfBQ631GohNgzEvV7hmIriPH4tm0T5z3fn-VKfoO4dkvKV90TTNoyEO65Oz19OcdnSPWzG6I9RKNiwfkWtDdKJIme2hpwsUfBxscOHgoW_YcOyYBknKRTJVWEwoVIX6BICv87VaJwk2Ic6lhKtH_f1hVlIE0lBeGoh4FnBBoE62YqKxBGH6cgi45_irw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84238" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84237">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84237" target="_blank">📅 17:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84236">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44cc310eee.mp4?token=dC05oLOklenJcze2SPinWGNGN4q9TVoYiPmSaEA1BPxeaAeXmhrlRT7iIhQO973F5Z63boeo1ZCoG8C5wysCu0STWaZmLAWGdcHlQdFYcROKjCGBB0_ZIZvRem3zsGWyyJUxUetbFHw6HIACyTg3U0v1ikW5Aq1LTu4a2o3NmeCtdgxFyljksjkDLrcugxkL2u1eUz-BzIm5rCsWSsdMRCS7FGeK9e8-5SwtXGjmucJweLlXHN9urUSltGTjUIypMwtuiYbJV_7zEddyOPfmiCe_hmK8yNSO2xe6hBtiEHQ4BiEGoX0wgRDS82tWemzzP1XhbmkqEVkhX7R-RZeCyCHWE2zL0O6VHyj9O_SWkl4cK8nRSVE_TZydHDjZDrhTwOqaFEEbaB7VaaKOA8MMnNHF-B-DC45vTLG_lI1Ib7e95wrjQDUpBY9c8YwJ2Ic3MDh02E2k2d-n49WXkWmJT1VcNgzJieFBUCqVu2WoNkXUPpS50NxnLGj39YtyhRoVfbiVlftdQQCNfveix2k1BbNwIVC_4TmMqSRkzYZiS-OttUqtqUtKj8ZP4mG4gsYljJGNQjSZsV__ifu2klkMpOb71RImkJMcyQmHWA1Z1fcZ8ohJo3MnNE906_NuPVp1nZospaAht74Ec7_qLp8hfJzeet5qfCww4_0XUPuq5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44cc310eee.mp4?token=dC05oLOklenJcze2SPinWGNGN4q9TVoYiPmSaEA1BPxeaAeXmhrlRT7iIhQO973F5Z63boeo1ZCoG8C5wysCu0STWaZmLAWGdcHlQdFYcROKjCGBB0_ZIZvRem3zsGWyyJUxUetbFHw6HIACyTg3U0v1ikW5Aq1LTu4a2o3NmeCtdgxFyljksjkDLrcugxkL2u1eUz-BzIm5rCsWSsdMRCS7FGeK9e8-5SwtXGjmucJweLlXHN9urUSltGTjUIypMwtuiYbJV_7zEddyOPfmiCe_hmK8yNSO2xe6hBtiEHQ4BiEGoX0wgRDS82tWemzzP1XhbmkqEVkhX7R-RZeCyCHWE2zL0O6VHyj9O_SWkl4cK8nRSVE_TZydHDjZDrhTwOqaFEEbaB7VaaKOA8MMnNHF-B-DC45vTLG_lI1Ib7e95wrjQDUpBY9c8YwJ2Ic3MDh02E2k2d-n49WXkWmJT1VcNgzJieFBUCqVu2WoNkXUPpS50NxnLGj39YtyhRoVfbiVlftdQQCNfveix2k1BbNwIVC_4TmMqSRkzYZiS-OttUqtqUtKj8ZP4mG4gsYljJGNQjSZsV__ifu2klkMpOb71RImkJMcyQmHWA1Z1fcZ8ohJo3MnNE906_NuPVp1nZospaAht74Ec7_qLp8hfJzeet5qfCww4_0XUPuq5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظة سقوط الصواريخ الايرانية بشكل مباشر على اهدافها في العقبة</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84236" target="_blank">📅 17:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84235">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c82dfd1851.mp4?token=rwe0mkRxkNe0QDek3mSe1FgXUwrJvMSZ98DUHT4MX3qCXLNRkhclICk6jUnuf6jF6fNNVYD1fgiBMovbcM4jo8qUDd_lKjpvMyj1wmXVxNb7AzN6X57qfrlGXV0q9cePfBNf_66BgQBF7QJNA56B9zoVs2Lh6fnuVi5ow0RIqo9YvZKFGKWwAtUAUiJMUTDfF9IZVOoI1uBsEB2VPhT42-icQk2MRKn6Pb4bA9BbN1TSs9824UdEDP17guPoPK_GIV4NBErwP4FzJGMmW-lxZSuD7WdkoBKIl9XBZX53Jc1DxAhqTzJ1WYgGiizEn6TahvPsvo-vMcJPJSTSH5FxMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c82dfd1851.mp4?token=rwe0mkRxkNe0QDek3mSe1FgXUwrJvMSZ98DUHT4MX3qCXLNRkhclICk6jUnuf6jF6fNNVYD1fgiBMovbcM4jo8qUDd_lKjpvMyj1wmXVxNb7AzN6X57qfrlGXV0q9cePfBNf_66BgQBF7QJNA56B9zoVs2Lh6fnuVi5ow0RIqo9YvZKFGKWwAtUAUiJMUTDfF9IZVOoI1uBsEB2VPhT42-icQk2MRKn6Pb4bA9BbN1TSs9824UdEDP17guPoPK_GIV4NBErwP4FzJGMmW-lxZSuD7WdkoBKIl9XBZX53Jc1DxAhqTzJ1WYgGiizEn6TahvPsvo-vMcJPJSTSH5FxMTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اندلاع حريق كبير في مجمع مشن لتجارة الاطارات والبطاريات بمنطقة الكرادة ضمن العاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84235" target="_blank">📅 17:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84234">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇱
وزير الحرب الصهيوني:
لقد أبلغنا أنه إذا أطلقت إيران صواريخ على إسرائيل، فسوف نرد عليها بقوة، دون أي تردد أو شروط.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/84234" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84233">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انباء عن انفجارات في بندر عباس</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84233" target="_blank">📅 16:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84232">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84232" target="_blank">📅 16:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84231">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">من سماء الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/84231" target="_blank">📅 16:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84230">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
مسؤول الشؤون السياسية في حرس الثورة الاسلامية:
وجهنا ضربات قوية للقواعد الأمريكية في الأردن والكويت ودول أخرى.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/84230" target="_blank">📅 16:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84229">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTVkzExreWRnAAhxK7HPJL0WLrFBvlbcesbsn2fpt5cluLFsIrbPlCNuyajxvs2WBGNnW7hgeA6TOWVo-0q-ULegg-P7OwEMBh1TWHeToBcy_58r1s7zPA80yX7nz9Vs8Y-0vONgR-6fw_cJ3a6CPasJiVcCpZwVy1YPz4QwN3Xo0m0k94DPiyZ5AbvZ-6oGJmYN6Boyv_NEBchK9mabmKFjFbs6ux0LkiLFOn4k0BVTEkGuud8zLVsUZ2z851pqauaay2BDJkEgi6HWxeevZdJ8lAlN4HaaBdBfLLvB_p9UpaaRAPht5tc-wFXbUGJtUvrs1mVgEx3ZX4P9EWhniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن اطلاق جديد من ايران</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/84229" target="_blank">📅 16:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84228">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwVxJnUp4S3lFALl90NxeLnx1kT90VZWZ7E0CAaBb9odTcb2NTaegXwH5xJ1skUtwMKhXju6fOAvDDQviqC1YST3rz9CT2RY4wBkIYTcWNIc-5sOR0RlJneaecI4ujSCZae4YAvPBWwoIqx9l0rJTP35mzKmPfq9QGD1j0zGc5Y9fq8GezMg5j7KYWQv3nlE1AJjSyi8PK9ByEfcG7hS51_U5A5133BbJL3D15r9707Pi7795TJiXuZ_7n2yTSUbcm5yxm0XYLgdDh4E_qS0jCvunq6UtHMqHEwsrwPvdfsD-RVGUTm0BggpA93qpyDhF21UN-Fu_RIYUI5-vJu3Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رصد غواصة اسرائيلية قرب ايلات</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/84228" target="_blank">📅 16:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84227">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/84227" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84226">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84226" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84225">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
🇺🇸
منظمة الطاقة الذرية الإيرانية:  حكومة الولايات المتحدة الإرهابية والمجرمة، التي لا تملك طبيعة سوى التسلط وانتهاك القوانين، قامت، في عمل عدواني ومتوحش يتعارض مع القوانين الدولية بشن هجوم على موقع بناء محطة دارخوين النووية - أحد رموز عزيمة واكتفاء إيران…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/naya_foriraq/84225" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84224">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اعلام العدو: إخلاء طائرات الوقود الأمريكية من مطار رامون بعد استهداف العقبة بالأردن</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84224" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعلام العدو: قد تكون الصواريخ الإيرانية الأخيرة تجاه العقبة بمثابة رسالة وتحذير إيراني لإسرائيل.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/84223" target="_blank">📅 16:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">امريكا تتوقع الهجوم
الاردن تنفي
امريكا تحاول التصدي
الاردن تنفي وجود قواعد في الاردن
اسرائيل تحاول التصدي داخل الاردن
الاردن تنفي خرق اسرائيل لسيادتها
الملك عبدالله خلال كل هذه الاحداث:</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84222" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اعلام العدو: سقوط شظايا في منطقة "شحورات" الصناعية بالقرب من مدينة إيلات</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/84221" target="_blank">📅 16:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الشرطة الصهيونية تلوذ بالفرار خلال الهجوم الايراني على العقبة</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84220" target="_blank">📅 16:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84219">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd2cd208b.mp4?token=cJJBuHwWHXUalm4pV5LP6COG0BS0AEXWt3W8JNpQul98LVJmAXk5J9tevSlWWOJj-oiWV4xnKINe8vRyfvz4nEtiAU9pU7FjOwAGI5eH1o3qWjcZj48IARu7K3bnFYlIRmKTJTduGNN-c25eiVdfLKIcb69-VznMvX44JEQUfS86QfRAPrLcyVYA0rRtjurmqyvtS5hVTj3-FdYIc6kU1etKhzo0eUGyejfKLIhWNmmOw1yJZ0tUI03wFErOLASjdUP8l1hEFNHGyEXPV9gRNFFuNmNtZGjPApea6e8zXoJ524Qsy5idjMHDFViPPnj4FDgRIZl4l6k8rmxKt_gKHYhxFyA0gFJVIHMyXNf7cUeO1vcPXKI6LXBEbe6JUDZKDYLKPcjW05Ih11KXKK5VQWewGhm4MllrZ_S5MjxZHZgE-AHooU9N3fSKbM9Djp3onWEHVAg8Y9046-kfLn6tb3Q_sJZa1Jv8dnpICt7Zn1xOnMVhLMXKvC4TQkxLVYNdWTdiOfLJTzWVBqsogY5rQ0YVsA9qBZaQhYRwrafvkUIS0f0rHYLu4Y5liJ8cuuFWDScOKabtbMPksSqobtg_8Qjodj52l1xtpZSF_x1axaLh_XWAayMti0QlzV6r52aUDkga-CauiuEZPsVWX1_bNodsPCCYSJ9jkhpqWMW39iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd2cd208b.mp4?token=cJJBuHwWHXUalm4pV5LP6COG0BS0AEXWt3W8JNpQul98LVJmAXk5J9tevSlWWOJj-oiWV4xnKINe8vRyfvz4nEtiAU9pU7FjOwAGI5eH1o3qWjcZj48IARu7K3bnFYlIRmKTJTduGNN-c25eiVdfLKIcb69-VznMvX44JEQUfS86QfRAPrLcyVYA0rRtjurmqyvtS5hVTj3-FdYIc6kU1etKhzo0eUGyejfKLIhWNmmOw1yJZ0tUI03wFErOLASjdUP8l1hEFNHGyEXPV9gRNFFuNmNtZGjPApea6e8zXoJ524Qsy5idjMHDFViPPnj4FDgRIZl4l6k8rmxKt_gKHYhxFyA0gFJVIHMyXNf7cUeO1vcPXKI6LXBEbe6JUDZKDYLKPcjW05Ih11KXKK5VQWewGhm4MllrZ_S5MjxZHZgE-AHooU9N3fSKbM9Djp3onWEHVAg8Y9046-kfLn6tb3Q_sJZa1Jv8dnpICt7Zn1xOnMVhLMXKvC4TQkxLVYNdWTdiOfLJTzWVBqsogY5rQ0YVsA9qBZaQhYRwrafvkUIS0f0rHYLu4Y5liJ8cuuFWDScOKabtbMPksSqobtg_8Qjodj52l1xtpZSF_x1axaLh_XWAayMti0QlzV6r52aUDkga-CauiuEZPsVWX1_bNodsPCCYSJ9jkhpqWMW39iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من مطار الملك حسين في العقبة</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/84219" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84218">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quC2Dr0r1mWmv2PhcA84tN3G6_3Q-ixWS_oONrXvqYpBsyn4pA78nb7FDfYbYs8yKYn3PE0EYB1nbhNgs31xLVS7P2Vlahqdh-63v56fNHDB2TCL46ZLbeVWnID0oRfoAEhV-NvNxLpVYRcWkJ-LL7aAGKOLcPm21uqZ9nm4xXb4sZuu_PDIW6DNSM7c9s0xcxjT3d9Mez_QUdsfAIRi0TwGz0stFBcozyxq_yHCg6sohGVVf7KeZd99lVo8WWVOO96yLEhTmVz7t3IOaae6QJ-4NQzx9vLTu-PIc1jYNICzMjlqIfxhwWXzGI-U-CxRNxsXJPByOB76ai2GSZj9mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجيش الإسرائيلي: قوات إسرائيلية وأردنية نفذت عمليات اعتراض لصواريخ إيرانية فوق العقبة</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84218" target="_blank">📅 15:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84217">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194f305a4a.mp4?token=ctGY2AtSzNs3CSwCY5IEdCOxxOy5Mvs2wtyF2Bh2t55yUxnM1ZqM242B425u9gdXZSc2ihe5_3vGOfnGHZcchZB10jzl_R76YQe9QczTh20OUr-tQOYFDBzl-X8VvpN3eGmf7sfL4ixfY6X_X80yUiZodb3QfbC-0Z2NLcuOXaPqi94-Ba0dcxw5P_xjUwSsjdhH7loPKlHxcpDvixJt0RY2BFzY6nJ0REBInmijH_6rAvazEp35DrtepfkuqAOk0NPQZQq8a1-YaVsTgoyGNv_TeLtsz1ov16iYPYEvbWSrNjwIw8sK3YKJ9QRK3PsaU-Mi_e4b4QhpANq20v7-HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194f305a4a.mp4?token=ctGY2AtSzNs3CSwCY5IEdCOxxOy5Mvs2wtyF2Bh2t55yUxnM1ZqM242B425u9gdXZSc2ihe5_3vGOfnGHZcchZB10jzl_R76YQe9QczTh20OUr-tQOYFDBzl-X8VvpN3eGmf7sfL4ixfY6X_X80yUiZodb3QfbC-0Z2NLcuOXaPqi94-Ba0dcxw5P_xjUwSsjdhH7loPKlHxcpDvixJt0RY2BFzY6nJ0REBInmijH_6rAvazEp35DrtepfkuqAOk0NPQZQq8a1-YaVsTgoyGNv_TeLtsz1ov16iYPYEvbWSrNjwIw8sK3YKJ9QRK3PsaU-Mi_e4b4QhpANq20v7-HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سقوط صاروخ في مطار العقبة</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84217" target="_blank">📅 15:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84216">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">سقوط صاروخ في مطار العقبة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84216" target="_blank">📅 15:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84215">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">متداول ارتفاع أعمدة الدخان في ايلات جنوب فلسطين المحتلة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84215" target="_blank">📅 15:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84214">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1702163fed.mp4?token=J0I8Xb4VeqsT-tRL0SBtskYA5tjertth8XduiLupgXJtzIrDUj9MyvhydYmia94Epxhh2UOq0duglnsXmn3P4Osm6kSoAk3ldGae8O4wL9AfRhjj8CNyMjY5ugYd_RzMiWCoMTuPGVJW0V824COyszHnfwOSKlXTwliZEJlVZbSmAzxuRir3vI90aX6KIQli8PICc5vBY9MUltvv_u2hTXeEYIORmiRzsOBt8K7FzrcNAjmuBVLfNdL2A2xsrQBruJsdPaSroso0Ljrq2MPwYJB56FzteKrXDiNUTfBqJnLnXrooCJUwGiquKuv7dmRto5QRgBZii2J3lbNM3K1YDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1702163fed.mp4?token=J0I8Xb4VeqsT-tRL0SBtskYA5tjertth8XduiLupgXJtzIrDUj9MyvhydYmia94Epxhh2UOq0duglnsXmn3P4Osm6kSoAk3ldGae8O4wL9AfRhjj8CNyMjY5ugYd_RzMiWCoMTuPGVJW0V824COyszHnfwOSKlXTwliZEJlVZbSmAzxuRir3vI90aX6KIQli8PICc5vBY9MUltvv_u2hTXeEYIORmiRzsOBt8K7FzrcNAjmuBVLfNdL2A2xsrQBruJsdPaSroso0Ljrq2MPwYJB56FzteKrXDiNUTfBqJnLnXrooCJUwGiquKuv7dmRto5QRgBZii2J3lbNM3K1YDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متداول ارتفاع أعمدة الدخان في ايلات جنوب فلسطين المحتلة</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84214" target="_blank">📅 15:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84213">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=o-KgmCvHr1yAnJ84Y7I3txIZGuWf9VOAHmcQ7zWV-tgjeKP6TM0cuyzApANg9ZKPjTmR-3BMvokAaG1Hh5je7b7nNwAnZf9kHu392KWXVaAo5CDRmsel0Ex5j3EUKmU2E47xSS93MXym6aFtzyAxbH28oFcwRK4OOSG9xEgHj8vrTwOZ141nqAaVP1Iux9LoCy7uejjTZCv6AnuzHHXR2DlTe2TPJlFgsO1CXnNPCyMwgzfIZmQKA0PQLsinnFmYB5o9eUYtW0AKor34hanjPpPlnI4eK-ebPlobe7Fn3-yv_N1IVixrqzdmsJwXjhodks6xfQsgLyRNnzw1mPVJKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07aff8569.mp4?token=o-KgmCvHr1yAnJ84Y7I3txIZGuWf9VOAHmcQ7zWV-tgjeKP6TM0cuyzApANg9ZKPjTmR-3BMvokAaG1Hh5je7b7nNwAnZf9kHu392KWXVaAo5CDRmsel0Ex5j3EUKmU2E47xSS93MXym6aFtzyAxbH28oFcwRK4OOSG9xEgHj8vrTwOZ141nqAaVP1Iux9LoCy7uejjTZCv6AnuzHHXR2DlTe2TPJlFgsO1CXnNPCyMwgzfIZmQKA0PQLsinnFmYB5o9eUYtW0AKor34hanjPpPlnI4eK-ebPlobe7Fn3-yv_N1IVixrqzdmsJwXjhodks6xfQsgLyRNnzw1mPVJKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام العدو: سقوط شضايا في ايلات</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84213" target="_blank">📅 15:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84211">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O83ESLvLZBda5gB4I0r809RmFf-A8VU_EBtvM0hxkMmwXq6IvzXNSNAGvSTMoPQUAlXoayJtguY2FdqLwvzorzF_eBni-dOAV566k0l4IVeqE8a3mc7P_76fiU_dyvXi2PzFe7-tdlyLTJ9iZIGA9pFgG6IfijIccX3BNMbfQq5KLscjhsubPukdL1PVTJ8zlezsI6qiGefOAi3wgNmAhMI9rvCCcgUBEGIxAmUxA2Gw2Fom0hmdI3OgOFL4x7iGFGxa8WeKK7qDPHgLiw1lm9b9pyaD6RtaxdzG4wDaJHmRvuL9hGhisNf5Trc7uOAv6AzUX3QKC4bJxmBhH2OPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nePQMxeGOBUuwO-e8wmrrr_ihnLcYZBJbhg2EPB-1bCYkSnEXcAJenQ7X8svd8IN3p88vDBVWN66sZFpdo8wAzDTPc-hzdkUgkEvg-ZcLmm6PbukZb3Nrb4OCSO5M8Gkq6qJxq38EomW2KXwdfyIMBtAL9okk8dc0FTimoGQ0TWBbVAceObJqqrxCvtcACT8t11lupJUPzA3CuHp58PQuMs-eywYFneG6n47LXAyTq0J7K4734KgsuBYC2HyW5aaY1uLG_maEVcndQdS-2jcdNi2MKXSEBdstL85lhBI9Vgw72kFLltKnaBK_4B7z8u6rluiPanl_I2mGkss74vY7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طيران المدني يغادر ويبتعد عن الأجواء في الأردن نتيجة القصف الإيراني على العقبة …</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84211" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84210">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اعلام العدو: اطلاق صاروخين من القبة الحديدية للتصدي للصواريخ في سماء الاردن</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84210" target="_blank">📅 15:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84209">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">إيقاف هبوط واقلاع الطائرات من مطار رامون شمال إيلات بعد الهجوم الايراني</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84209" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">شلل يصيب السيطرات في اجواء الأردن ، الطيران المدني يغادر اجواء عمان</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84208" target="_blank">📅 15:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84207">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات في سماء ايلات</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84207" target="_blank">📅 15:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84206">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز إيلات</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/84206" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84205">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scosYyV8eOZawk9Nu2tgFi4EY0HvUdcUQ02nJCHiyr7EY_X7hvY9QYarWSA5GsoCblYoSSIfWAkq_g48zIgvF3ul8aIBQyBiK8-1XN1DSdm0yMHYhrtpdr8VXlpYhcoQkXzb3IXA_nTX-x_QguB6P81mfROLlZHVHaGpHT3sqkSuBPZqHx7MvBH0VCmbdiGgBfbAkvLI_sY0VDsFd_ClERW1g41nyg5aKF_U1bS8iFEjURNetMa9_MpauqJw0mpyOj2UYn7c1n-1JoUn6pYz-aCQlSbvYT8Gc9NTPMq81vu50knge2kYdPGIFIz2ezQAE_lKwHHW1Tl7b8UNN_fSCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سماء ايلات</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84205" target="_blank">📅 15:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84204">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl3MYMvYvJxxd-loT50fsQ0E0UB6CrNoGkt5ylXw0OXbD19fokoyV1Fd9077_ncJKpn4RNqfk2Zqoua9_shcWwpAVEwzPnQ5pzGleXjeqkoeHkWjK90JOagKUjmv281gruvePLevozzbrBh3Cg6-HbEAADquL2rWA-7Vg8jhGFgrw3cso6kcc1NSUG7E2xYxSVD66SYNjcbG20Nlv_KW0UhAOEIu5GaXo1cHSWRy48Re1ZS5HmAMxtDmsLiQFZ3vg5q2vmCGmUTrfJ0Lwp3EFFksIyFggCovi7ZI7UH7ljqGFDqrqlkID8BTjMtdY9BhzhXA78sDWUBEEHoGrbXcMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من سماء ايلات</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/84204" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84203">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geh1FFDc_nrdJVTMHztxV0gYgEIdLVV0tDbI1lt54yZ8V7atHrjRh1_GRslcFn57WQ-01V9Sumbuv9x22r63vtGLIq-lJ-iHPqeADHqUiHxocn6bZP4GP0tBiSbngKnODTlikOX9IFMkTKH9IOE9cSzxMHYbCDSMlJ3PdrQpKp5Od2_MQ_qSZjFbmngVXRR-K80oB4OcwQP8rcDVWipqZIx9MkyG0oFKQ9nORJGOzihrXGmXH6pHss58f38GVsk6a9-kQrPA_-WGjGNYTtflv5vTEA0SX43qEnlcUkvj7BXHvhnoau7ZyC2wLHdo8jfTYvtFhT3b-Y88zcRQE9Yimw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صافرات الانذار تدوي في العاصمة الاردنية عمان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/84203" target="_blank">📅 15:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84202">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e79776748.mp4?token=mfol-NNVukG5y1sFKot2kJ3EILsIK6b0sd8l5dArFrHzyL-bJYxuE5WABloW4D6ozQRdWPJGcpHgYDPBairXztRBSisNwcQ2s0RB21nnmjoPkpAVAz96UlOb6lp7hivsLlL35wo2TIcwH4V7IAFTHuhnffOvqV40le6OlyhCJ_WVzjVVyuHL3VOK5f0vqTHSfCVA2-vPdyo4mpYrWcQUrlh7N-CK7O9PE_j39M7Tv7zvhhezpVWYJGAFJsuZQ_9WeMfrwe0zmOJ13Xk6opc2lYh50lBO22bX1q5-6npbewJ26tfJLJROKjnY4cPo3U7I9EtQefK9CcCjUnfkyuo1fhK7BLkZvj-WLIvEJVuD-5awqWYHku0GtZOFnhHTRTO0aLfnNPovfD9ZJ3xVooM6quatsuJ1aYRxuCyCV1WpRM-ASu8goAE2VXxz2NKgmgzQFiLadFCVqnwTaSoGeuR-pZ5743zQgcWVZ2p5CqU_jo3IYujBNYDnGbnjPnrZs8FnFux7eB0KfoR2upKQTq-qbq7wUKbpb0eUegL1rE63ZByixq24vuflJoRXoQ4Wh4GHxPdUE9k-7OHKPQ11Ogq_9a5if4LAVkAAgeRG_H7E09MTLRB1B-KPHH4QVDa0qvgLWPUVByDb8_Nf1DYkkkE_2g39H5P7v9AltMB7I5oxndE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e79776748.mp4?token=mfol-NNVukG5y1sFKot2kJ3EILsIK6b0sd8l5dArFrHzyL-bJYxuE5WABloW4D6ozQRdWPJGcpHgYDPBairXztRBSisNwcQ2s0RB21nnmjoPkpAVAz96UlOb6lp7hivsLlL35wo2TIcwH4V7IAFTHuhnffOvqV40le6OlyhCJ_WVzjVVyuHL3VOK5f0vqTHSfCVA2-vPdyo4mpYrWcQUrlh7N-CK7O9PE_j39M7Tv7zvhhezpVWYJGAFJsuZQ_9WeMfrwe0zmOJ13Xk6opc2lYh50lBO22bX1q5-6npbewJ26tfJLJROKjnY4cPo3U7I9EtQefK9CcCjUnfkyuo1fhK7BLkZvj-WLIvEJVuD-5awqWYHku0GtZOFnhHTRTO0aLfnNPovfD9ZJ3xVooM6quatsuJ1aYRxuCyCV1WpRM-ASu8goAE2VXxz2NKgmgzQFiLadFCVqnwTaSoGeuR-pZ5743zQgcWVZ2p5CqU_jo3IYujBNYDnGbnjPnrZs8FnFux7eB0KfoR2upKQTq-qbq7wUKbpb0eUegL1rE63ZByixq24vuflJoRXoQ4Wh4GHxPdUE9k-7OHKPQ11Ogq_9a5if4LAVkAAgeRG_H7E09MTLRB1B-KPHH4QVDa0qvgLWPUVByDb8_Nf1DYkkkE_2g39H5P7v9AltMB7I5oxndE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في ايلات جنوبي الكيان نتيجة الهجوم الصاروخي على العقبة الاردنية</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84202" target="_blank">📅 15:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84201">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">المتحدث باسم جيش العدو الإسرائيلي: قبل وقت قصير، تم رصد عمليات إطلاق من إيران باتجاه مدينة العقبة في الأردن، وقد تحدث شظايا أو سقوط بقايا مقذوفات داخل أراضي اسرائيل نتيجة هذا الإطلاق.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/84201" target="_blank">📅 15:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84200">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">صواريخ تتجه الى العقبة</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84200" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84199">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84199" target="_blank">📅 15:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84198">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صواريخ باتجاه الاردن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/84198" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84197">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/84197" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84196">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">انباء اولية عن اطلاق صواريخ من ايران</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/84196" target="_blank">📅 15:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84195">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUiFwOHz-yvnhAalnqqMLNmVfMyCMoypBmNNkBI3H9P5V92pgKGuokiEKu7MDPXVWFgRa55m0kfja231lABrLYwuXq0iedYvu9tuYh_AIuBi-jSb7SzlDmrpMM5-jaeHC0Q1iJInFVDtunCcc2Ua7xYAORMsJYwQHYGTwx64FDpI3mCFGdkSHxL_m_Evl0-x3ZJrGYWb8l5EhG6JfwSYOjnw7jycILaMMko3e4TQ6tfrbdIHkSX2WJfkbJVTpVZBQCM8JPIGeIlF9RNTIUFkKwjPno3240XhUqBlAg_i3EgfERdArlSeR1X8nnWkHEZwMIkI-qjvV479d3n7Ri1eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
‏على الجمهوريين إضافة إيران إلى مشروع قانون العقوبات على روسيا. هذا ما أراده ليندسي، وكان سيحدث لا محالة. هام!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84195" target="_blank">📅 15:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84194">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مجلس النواب العراقي يصوت على إعفاء قائد القوة البحرية وآخرين بسبب تقصيرهم بشأن فاجعة قتل الصياد العراقي من قبل عصابات خفر السواحل الكويتية والاعتداء على الصيادين الآخرين.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84194" target="_blank">📅 15:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84193">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇮🇶
🇰🇼
مجلس النواب العراقي يُصوت على إضافة فقرة على جدول أعماله قراءة تقرير لجنة الامن والدفاع بخصوص استشهاد الصياد العراقي من محافظة البصرة على يد عصابات خفر السواحل الكويتية.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84193" target="_blank">📅 15:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84192">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
🇺🇸
القضاء الايراني:
لم يتم إطلاق سراح أي سجين أمريكي بالمواصفات التي ذكرها ترامب من سجون إيران. السيدة التي يتم الحديث عنها لم تكن سجينة ولم تتهم بالتجسس. ترامب في وضع صعب للغاية ويحتاج إلى إظهار أي إنجاز. حتى خروج مواطن إيراني-أمريكي من البلاد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84192" target="_blank">📅 15:12 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
