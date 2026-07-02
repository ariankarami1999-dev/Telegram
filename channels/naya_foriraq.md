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
<img src="https://cdn4.telesco.pe/file/VvIezF4SPOsBFVdjVWcZcVTcl0Zw49RYuX0-nw1MV9OGMC540mEnEJY11p8ZaCiTeNj-hTNdnkyiZIk9B5UuLkfXpTIUF1lhO9EXqCJhFdbVykmWTm3hzI00zHwO6HMHBzCx9M0dpfEY4_RVJe6e6q5JlDRV-NKclSIkWiq1Ui4HXBe0KD7qjjGvXimLh6areh5xlk1ZR-a_EDNag1f7BDVloq5CocAdiAJL--_ON18u1Y5koaYMKMFws77Meogbshbo3I5ywczKTIREXq97Hw0t8fpLvSeiHUaw8PwroWCFtrBZK0ZeIOuL-ofMlAD3JKHWEfQUfQijSHta1o5tcg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 256K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 23:28:44</div>
<hr>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5460badcf.mp4?token=UCX1x4L9oNJYWEWO0yIwlpcmiNzjops_3MGEVUs-oofb8uYtbOQeAdEyF3W67oE7e-rsAWybHc16AZHT0mjRjNl8KO_pWvcTbTH0OkNd7LCXCLdMonESjS5e6GgS1SXVGK6spp9pcz98cu8BWdMmn0AV0qmgA6Z6gjLUbaxmaLRs-pI5pffifElOFQkW9u-dAj_UQTTQP-wHxurIUFyUo_S-_PdlLpyg0tD3MN9c5U8Rmto9zCHE2R8HVuLVLwTjbFM7BtNHFygSjlAoteppmh19P8DfkMn1pBOhyGCv9Pql9nlp_97G2Leqxftqyr0eIT-OiDNhXVyOZ_D0d4v82g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
المصلى الذي سوف يتم الصلاة على امامنا السيد الولي في العاصمة طهران.</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/naya_foriraq/80624" target="_blank">📅 23:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s57DxaAf_COalK3ySnMABh8Zx4zk-yY11pjSwVXdoc2YpHBlGgX8mn5NjfOy423fY-ARPCdKp7QR7eJOBb91PnsXvHRlUVKC_FxbRPkmzP1FbSpPj3yNqm7sfLYw4xL2OelNojxyWZXPEsBX8WQ-lOgo1TlG3RweKAuqk59PZn6qcahT_2jH_TR4wmL_k761YtbL6LrDJ8YpNvnB1d7RFmEq3BGbCxv1FbTIl4Ydmasw65I-ms4rvG6_kdQb3zxBnrdnTlJX2ZlG_-3h79h3mmm6ZkFadgcQFGTcg49irvLMRi-8LxpTi6ms1EFAPSebXvLQ5y0urPjqeoDprq6MIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
بزشكيان:‏
الآن وقد أصبحت إيران، المليئة بالأحداث الملحمية، تستعد لتوديع الخادم الحقيقي للإسلام والثورة، أدعو جميع الناس من كل عرق ودين وذوق وتوجه سياسي إلى تصوير مظهر دائم للوحدة الوطنية والولاء للمثل العليا للنظام الإسلامي من خلال حضور شغوف وثابت وتاريخي.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/naya_foriraq/80623" target="_blank">📅 23:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SoWqjmQyc3y9gS72wABoPVsnYNNw6kkI98jNnr58ZeCMnt4cSMSwtZTkSxoGDPOfp1gus9H9sBEa97ArGbAlt4NQIqiDA4ySmNK-Q9mOa6d4jN6wwleCZqdpg8fx4g3RnTc5qZoL7Dbl-yT8trnVjaB5mcWCkDIRdLm2zI5sDsK_sc-rny5-HzIC6pGGUG1J2Whd_n9H2bzIJZD4Yy3AsNKhEIHlDn4TzCJqrsGDS3dK8vGb55Az-wO92dbnO1Wl4o_di22Cvgwf8E1jaZm33CPEHlcQVezhhB7SbRF1oI8f52WgKEwrQwuf_C97mFRpqtL2MF2KFk57Fy2a6uHFww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
في الوقت الذي تقوم به حكومة الجولاني الإرهابية بهدم قرى الشيعة والتخلي عن قرى آخرى لإسرائيل.. استشهاد شابين من أبناء شيعة سوريا تحديداً "نبل والفوعة" واحتجاز جثمانيهما بعد معارك مع الكيان المحتل في محافظة درعا دفاعاً عن الجنوب السوري.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/naya_foriraq/80622" target="_blank">📅 22:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">صوت مجلس محافظة واسط على تقليص الدوام الرسمي ساعة واحدة " من نهاية الدوام لشهري تموز وآب.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/naya_foriraq/80621" target="_blank">📅 22:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
انباء عن انفجار في مدينة دير زور السورية المجاورة للحدود العراقية.</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/naya_foriraq/80620" target="_blank">📅 22:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6-Zhd5zReoRnat2_w4Wo8zPkkG7hDBxbc1ewwWmPDMcbLHnmQI-JuGKtSwvcg1flrgHeD7QEKQeEG_MjVjTD3EC4m-NM7plTJR8ze3-8eWO6UI0X8bq-uLfxipGKOTPOK46TgemX2EgORx-FsSrK-d5ewrepydy3w_By1YPlrJ596-DYBVJxqDdULUjTn1naWio9hXBGKoA8TosdY7l4ZglJkcc8w0eGKA_u_2B_VlmnXzfHREdsTS4vqX9N9rfp6IbeGlx1FgXVki8YSPB1G23lsIQG1vrxR5Yc4ANkBYradBxurdUgCRCE00tUU0xQfFdpTQJ1e9ZMfm8B3Wdwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عراقجي
: ‏
هل جلبت القيادة المركزية الأمن أم انعدام الأمن إلى منطقتنا؟ الجواب واضح.
‏وبالمثل، أثبتت قواتنا المسلحة القوية أن الغرباء لا يستطيعون حتى حماية أنفسهم.
‏لا يمكن الحفاظ على السلام في منطقتنا إلا من خلال نهج شامل وجامع، دون أي تدخل خارجي.</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/80619" target="_blank">📅 22:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80618">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/naya_foriraq/80618" target="_blank">📅 22:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80617">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">السفارة الأمريكية في بغداد سوف تجري تفجيرات وتدريبات بعد قليل بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/naya_foriraq/80617" target="_blank">📅 22:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80616">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇹🇷
🌟
وزير الخارجية التركي:
تبحث إسرائيل حاليًا عن عدو جديد.
طالما أن إسرائيل - أو أي طرف آخر - تتصرف بطرق تتعارض مع مصالحنا الوطنية والإقليمية، فليس لدينا أي سبب للخوف من أي شخص، أو التردد، أو التراجع.
لا نمانع المواجهة. إذا حدث ذلك، فهذا ليس مشكلة بالنسبة لنا.
إسرائيل ليست مشكلتي فقط؛ إنها مشكلة العالم.</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/naya_foriraq/80616" target="_blank">📅 21:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80614">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇫🇷
‏
الخارجية الفرنسية:
قوات التحالف الدولي ستنتشر في لبنان بدعم أميركي.</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/80614" target="_blank">📅 21:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80613">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=gaBaIMMD2mTPLnaF8k_wRXgKXEM6-pSr8OaWUjM6mKyIsNjtnGH_zR4r5jDuwmNr2-J2naWUv7PfDPy3YF7iCOdvtbP2djiGk4GpDnkxskKQr8Dq60MJf1pj8rcSIcXjDZxGpjIlQGseetJQ0u3l_z3NUgFYa1YJuQ6zrWwbW4o5-pMXAY8gl7yKqbkyg06QLZcvugwbjDxCTzgwi77LwNeUgHoa-odQeLmF5A47E1mGYylXkzBPo3JpC99ZqlDQdcNk0v1g5PfkEmJy_BXfmslzxxzDLZHOvfpdNJ3HsIWimF9LUeYUzURTqmfJ7SIJOE10_CBYuar2luEJCyTh6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d12f5ea17.mp4?token=gaBaIMMD2mTPLnaF8k_wRXgKXEM6-pSr8OaWUjM6mKyIsNjtnGH_zR4r5jDuwmNr2-J2naWUv7PfDPy3YF7iCOdvtbP2djiGk4GpDnkxskKQr8Dq60MJf1pj8rcSIcXjDZxGpjIlQGseetJQ0u3l_z3NUgFYa1YJuQ6zrWwbW4o5-pMXAY8gl7yKqbkyg06QLZcvugwbjDxCTzgwi77LwNeUgHoa-odQeLmF5A47E1mGYylXkzBPo3JpC99ZqlDQdcNk0v1g5PfkEmJy_BXfmslzxxzDLZHOvfpdNJ3HsIWimF9LUeYUzURTqmfJ7SIJOE10_CBYuar2luEJCyTh6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
الرئيس الكوبي حول التهديدات الأمريكية:
إذا حدث هجوم، فإن الشعب الكوبي سيستجيب بوحدة ورسوخ ودفاعًا عن سيادتنا.
نحن لا نريد الحرب، لكننا لسنا خائفين منها.
ونحن نستعد حتى لا نُفاجأ أو نُهزم.
علمنا فيدل أنه لا يوجد أعداء لا يمكن إلحاق الهزيمة بهم.
قد تكون هناك جيوش قوية جدًا من الناحية التكنولوجية، لكن في الصراعات، هناك قناعات، والقرارات التي يتخذها الناس، والتضحيات التي هم على استعداد لتقديمها من أجل الدفاع عن سيادتهم.
قال الجنرال أنطونيو ماسايو: "كل من يحاول الاستيلاء على كوبا لن يتمكن من أخذ سوى غبار تربتها المغمورة بالدم".
هذا ليس مجرد شعار. إنها قناعة تم تبنيها من قبل ملايين الكوبيين.</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/naya_foriraq/80613" target="_blank">📅 21:23 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80612">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANblqj8TGl3H4Q9m59YBgYH2Z7FukyuDTekr9ZmcKUhA-Gyc4u2haXGHpbYwSd6CJOGsVIMQxMdoPvTxOw0iKkO7j8WeYxi29k8_2ySKJR_BFWqrskCXz5hVjMJLN1rL3xnmW9jCHgRU2lXHgz9aoCeVZxXsdsO9ykZvOKyc6_ZUCOoxrEwqub7cANkVUNEev0eJp1VSR7z6VvlZe7ssYpQy-ON9K95hC_Q-lRj5wXy_VWXkuF5GKM1_DZ5IHltpuBiWXgCh89bJWXWMeOznv5hm7vox4l5JA_-gNHzjOYYM-DXQkHcvfZDQ5mlFD9xZjbKr6YwbtvUtIdDVkyTwFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
أعلن اليوم يومًا وطنيًا للإسكالوب احتفالًا بإجراء اتخذته الإدارة الوطنية للمحيطات والغلاف الجوي (NOAA) والذي سيفتح الحافة الشمالية لبنك جورج لصيد الإسكالوب، محققًا حلم صيادينا العظماء الذين عوملوا معاملة سيئة للغاية من قبل إدارتي أوباما وبايدن، ومن قبل دولة كندا. هذا يعني ملايين الأرطال الإضافية من الإسكالوب البري الجميل سنويًا على مائدة مطابخ الأمريكيين، والمزيد من فرص العمل في نورفولك، وفرجينيا، وكيب ماي، ونيو جيرسي، ونيو بيدفورد، وماساتشوستس، وجميع أجزاء الساحل الشرقي تقريبًا. هذا بالإضافة إلى تحرير منطقة شاسعة قبالة الساحل الشرقي لصيادي جراد البحر العظماء لدينا، وغيرهم (نصب تذكاري بيئي أعلنه باراك حسين أوباما وجو بايدن النعسان، والذي قمتُ بإنهاءه!)، ونصف مليون ميل مربع من المحيط الهادئ الجميل، حيث سُمح لكل دولة بالصيد باستثناء صيادينا الأمريكيين العظماء! لقد فتحتُ المحيطات والأنهار والبحيرات والبحار أمام صيادينا، وحررتهم من القيود البيئية السخيفة التي سمحت لدول أخرى بالاستفادة من مياه الولايات المتحدة في عهد باراك حسين أوباما، وجو بايدن، والديمقراطيين. إنه لشرف عظيم لي أن أفعل ذلك لأني صديق الصيادين - اخرجوا وصوتوا للجمهوريين في انتخابات التجديد النصفي، لأنه إذا وصل الشيوعيون إلى السلطة، فلن تتمكنوا من الصيد مرة أخرى!</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/naya_foriraq/80612" target="_blank">📅 21:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80611">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=udgbC1tc0dzJeQODUcXWdeelSD_egwkpJrFe9b6LOlWu9GcZDlhpe80E0Fn0FM-zX6RJKH_Qg0HnNC5Ic2jivhz082x4sPM1jzSjdicWTLS8SrNBe9KP-m9rYSwSTtz-AQw7ALFjPJXjWBVzaFAMlfakS1X1gpM7YJ72BeXyci2oP_uKEc6ozA72UO7RsomsHCZWYkhN0RYugaZT45xfMSdI0WbfyA-93-uMsnigEBIWqL5LchH3dKzA_jcpgAIwY9cp1DwtY_9UFPg6MJjnUBlgCaF0wzcmm0QpDClPioDLlkMRrvznE8Lx1dTb4NfvAKeHvpuw5Be30tCvP0SVbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c576dcf67b.mp4?token=udgbC1tc0dzJeQODUcXWdeelSD_egwkpJrFe9b6LOlWu9GcZDlhpe80E0Fn0FM-zX6RJKH_Qg0HnNC5Ic2jivhz082x4sPM1jzSjdicWTLS8SrNBe9KP-m9rYSwSTtz-AQw7ALFjPJXjWBVzaFAMlfakS1X1gpM7YJ72BeXyci2oP_uKEc6ozA72UO7RsomsHCZWYkhN0RYugaZT45xfMSdI0WbfyA-93-uMsnigEBIWqL5LchH3dKzA_jcpgAIwY9cp1DwtY_9UFPg6MJjnUBlgCaF0wzcmm0QpDClPioDLlkMRrvznE8Lx1dTb4NfvAKeHvpuw5Be30tCvP0SVbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
المواكب الحسينية تستعد لإستقبال المشيّعين وتقديم الخدمات خلال مراسيم تشييع قائد الثورة الإسلامية وعائلته في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/80611" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80608">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=QihV4F4_G9VyJ-3jgzQECgTr8TpIJfOtJPa9BWhnklcObzYZiRgaTYB7CVCA08XksnoSZM3ppahFLFeQ5wZQE0pPMprqeqS3gQigrjDvjEJLCieBknOfibcK-If4Zut_joHd18kVmei1BxENB80yD2FT-ib6a2wH2PSBr6OLS8dLl61dz-5xVtgVdAV5oeYvLOkLtEL-iHL2gYOC4OIt3KyKxs6zA-hodJsGMs6pWfAg9VDE4TqLaFmN_liiOwEKHp5pWiXuQYfs50BjFVb75F2gIotKexVVzd04UAjB7aKA5lisbkuf_Jp2yvv5ZxYH7YHPHZUCP-F2rKYIFefWAB87_ezK9-0pkeby3jqMemMAagGUC40ul2IKOPwNhTIlVA1hrUrT7uymNyZRZ5vLJSoLwCtA3WqoRUU7muopp9kMnzFsCkpcLacUrfCgms8tUY9qhf1em8rxi6eONKLV4BeFRbmGQ0rXbET-z2wNrXtogqSjk-dARIt5T4qaSSH7DoPyubijy25HnamYcYQGLy2gXu18100kwnBhsNYB9s2cHR4rGcjswpq5vywbAbWdixAE3TzHndZNtAe7XIeIez9EKsJxxxNN5XwetI4ba4x_gABNLaF98DaE3uYAY42zfeLBP6bO9eOuPHWIeDZrpQvjaI0ZlVWkBDyccBhxU4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65bb5c1cc2.mp4?token=QihV4F4_G9VyJ-3jgzQECgTr8TpIJfOtJPa9BWhnklcObzYZiRgaTYB7CVCA08XksnoSZM3ppahFLFeQ5wZQE0pPMprqeqS3gQigrjDvjEJLCieBknOfibcK-If4Zut_joHd18kVmei1BxENB80yD2FT-ib6a2wH2PSBr6OLS8dLl61dz-5xVtgVdAV5oeYvLOkLtEL-iHL2gYOC4OIt3KyKxs6zA-hodJsGMs6pWfAg9VDE4TqLaFmN_liiOwEKHp5pWiXuQYfs50BjFVb75F2gIotKexVVzd04UAjB7aKA5lisbkuf_Jp2yvv5ZxYH7YHPHZUCP-F2rKYIFefWAB87_ezK9-0pkeby3jqMemMAagGUC40ul2IKOPwNhTIlVA1hrUrT7uymNyZRZ5vLJSoLwCtA3WqoRUU7muopp9kMnzFsCkpcLacUrfCgms8tUY9qhf1em8rxi6eONKLV4BeFRbmGQ0rXbET-z2wNrXtogqSjk-dARIt5T4qaSSH7DoPyubijy25HnamYcYQGLy2gXu18100kwnBhsNYB9s2cHR4rGcjswpq5vywbAbWdixAE3TzHndZNtAe7XIeIez9EKsJxxxNN5XwetI4ba4x_gABNLaF98DaE3uYAY42zfeLBP6bO9eOuPHWIeDZrpQvjaI0ZlVWkBDyccBhxU4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترند_تركيا
🇹🇷
في تطور خطير بساحة التحرش والمضايقات
😆
..
امرأة تتجول منذ ثلاثة أيام في شوارع إسطنبول وتتحرش بالشباب حيث يتولى نشر فيديوات لها عبر كاميرات المراقبة في مواقع مختلفة.. منصة تركية: منذ ثلاثة أيام وهي تتجول ولم تترك شابًا إلا وتحرشت به، ورغم ذلك لم يتم اعتقالها. ماذا لو كان المتحرش رجلًا؟!</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/80608" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80607">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/naya_foriraq/80607" target="_blank">📅 20:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80606">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل وصافرات الرعب تدوي.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/80606" target="_blank">📅 20:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
إعلام العدو: حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/80605" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
وزارة الداخلية العراقية:
إحكام السيطرة على الشريط الحدودي العراقي - الإيراني في هور الحويزة بعد إكمال سدة حدودية بطول 50 كيلومتراً.</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/naya_foriraq/80604" target="_blank">📅 19:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjF0KtIjK2yJg5cg3nbW-1xXRBfTSeo_57nYLpnh5Rf0QS8HKVPkJzN84ZzBEk2pbw2RcGxiB1ps7aTLZSL7RfPTta6JzVtQsTHiBB3bJsxh_kDfp4S0-TuBkXuJHFou4VocVkii-cmc3lsu_MFX5vh5wjB3b3XznjEDqMzrQC80Yi_XaggPNGcXpFpzZ1kOMAu8ZeZ8UODUc8qiizBkkzAZ4SGfOXuf9rtb01KHxw2nIHWSnTa2z8QG4DB9KJzeUxgeeBtMwMQsRtg8RcbJA8pkDOTDJ-AKzhvV2OWIli3h_sUJghjIta1wxKyYIY0tWyW_NTZh2LpSq16PO9t_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
غارات للطيران المسير الإسرائيلي على النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80603" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=lgWCm4JmoQcgUxxk_GoND3f0kRDYJH-noCu02FiBvTPSnf0enUQ2VzfxZZBXsVqUlPSaV3XGgAiPoXZPzzXq7Rx2w6Ck8oOyVCOiyUc1hhQwLtygm7OWuT3gQbB-oWC0ANDhAXvlGXp-Uox1GZKJLzGXx08xsUodLfOKkwXlroHryCFxH0ieBJ9YT957VZqT1u03Xdte-sE0Su7qE52f6v-JqP_NEtvcEbzODuyl2kDVD0ix01XQbzLM1cKW89-RoTYaQvfLLUZ15mBZ2diEhJgRTMiqfe_NZqq1FpLu6MPLI7T_PcvBYi3vqmJTHW7qk2nYQ4XVBi9jftRztfpiBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb72d46ebc.mp4?token=lgWCm4JmoQcgUxxk_GoND3f0kRDYJH-noCu02FiBvTPSnf0enUQ2VzfxZZBXsVqUlPSaV3XGgAiPoXZPzzXq7Rx2w6Ck8oOyVCOiyUc1hhQwLtygm7OWuT3gQbB-oWC0ANDhAXvlGXp-Uox1GZKJLzGXx08xsUodLfOKkwXlroHryCFxH0ieBJ9YT957VZqT1u03Xdte-sE0Su7qE52f6v-JqP_NEtvcEbzODuyl2kDVD0ix01XQbzLM1cKW89-RoTYaQvfLLUZ15mBZ2diEhJgRTMiqfe_NZqq1FpLu6MPLI7T_PcvBYi3vqmJTHW7qk2nYQ4XVBi9jftRztfpiBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
إعلام العدو:
حدث أمني صعب في جنوب لبنان ومروحيات الجيش الإسرائيلي تنفذ عملية إخلاء لجنود قتلى وجرحى.</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/naya_foriraq/80602" target="_blank">📅 19:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=YCGp0tgmZabqOLfETosRUEvq17Cg1olfABq-6K16ic2sDxRXvRGsMmnLBu_5SCD0ziP9uNFXmH0R_HAEryMlLIBhpRpagndkkyiYyQMzEZ22ncmFrHaieECsFKqCkQLsEhbFzuXPfF9d5J82gM5_vmLuvvaY3UZbZNeEmmknxSCUhot1YvbahA76RVxwBHZkaYa4CrIjFBbWsmksu47b4r_DMbEY0Fmht0NLN7zIwe_eLrrOObxc9Wv73zYkEVank8GiMiteNRvh0hHWEoLTsGVIa4tLAtsll4i68bhI-Jk8JzxcWjfn_WlgpS2cwsNW-z246ARC3fx9K7tMpK1U-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79d8bde8ed.mp4?token=YCGp0tgmZabqOLfETosRUEvq17Cg1olfABq-6K16ic2sDxRXvRGsMmnLBu_5SCD0ziP9uNFXmH0R_HAEryMlLIBhpRpagndkkyiYyQMzEZ22ncmFrHaieECsFKqCkQLsEhbFzuXPfF9d5J82gM5_vmLuvvaY3UZbZNeEmmknxSCUhot1YvbahA76RVxwBHZkaYa4CrIjFBbWsmksu47b4r_DMbEY0Fmht0NLN7zIwe_eLrrOObxc9Wv73zYkEVank8GiMiteNRvh0hHWEoLTsGVIa4tLAtsll4i68bhI-Jk8JzxcWjfn_WlgpS2cwsNW-z246ARC3fx9K7tMpK1U-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/naya_foriraq/80601" target="_blank">📅 19:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇷
‏
مندوب إيران في الأمم المتحدة:
سنرد على أي انتهاك لمذكرة التفاهم.
‏الولايات المتحدة هي من تخون الدبلوماسية.‏
حرية الملاحة مكفولة دون رسوم بمضيق هرمز لمدة 60 يوما.‏
نحذر من استخدام مسارات خارج السيطرة الإيرانية في مضيق هرمز.
الهجمات الإيرانية على القواعد الأمريكية استندت إلى المادة 51 من الميثاق وشكلت دفاعاً مشروعاً عن النفس.
إن تقاعس مجلس الأمن عن أداء مسؤولياته عزز مناخ الإفلات من العقاب وشجّع على المزيد من الممارسات غير القانونية.
استهدفت القوات الدفاعية الإيرانية المنشآت والقواعد والأصول العسكرية الأمريكية في المنطقة التي انطلقت منها الهجمات ضد إيران.</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/naya_foriraq/80600" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
القوات الأمنية الإيرانية تتمكن من قتل 2 إرهابيين في مدينة تفتان بمحافظة بلوشستان جنوب شرق إيران.</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/naya_foriraq/80599" target="_blank">📅 19:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromقوموا لله</strong></div>
<div class="tg-text">إلى عموم المؤمنين والمعزّين الكرام.. استعدّوا للمشاركة في مراسم تشييع السيد القائد علي الخامنئي (رض)
#قوموا_لله
#باید_برخاست
#KHAMENEI
https://t.me/in_front_of_the_martyr</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/80598" target="_blank">📅 18:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8425182b.mp4?token=hGjcgChSLVNVkXj4OBkRKklyNw1r9uUHBEAanpNeHrbIB2Tg98ZGx9JbvYumOp3KBUgASriWvPI85QS2Iv6aJTYC26TJUsV7rujrVT8YnuW-OXWD8IThKvTpGX3cDKY9NUJa07YoDy7CQDxIIvMUEc5g8kdXbJylCTwSDDa3DovD2oS-rJ_dv5_x0u3TfSXd06YXZ556rx8uTiN0Xfi5sZrNes5fvywzkB7XXvrCneOYTWcBgvfHeqKXxjFlarWoul7Z8c4uXj_CAituRLVTrMeU3ls_yohmbiiMA9S42s72vYgLagn4rvCOsuoiSGJj196ybWVI4SX9jbH0k7aBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8425182b.mp4?token=hGjcgChSLVNVkXj4OBkRKklyNw1r9uUHBEAanpNeHrbIB2Tg98ZGx9JbvYumOp3KBUgASriWvPI85QS2Iv6aJTYC26TJUsV7rujrVT8YnuW-OXWD8IThKvTpGX3cDKY9NUJa07YoDy7CQDxIIvMUEc5g8kdXbJylCTwSDDa3DovD2oS-rJ_dv5_x0u3TfSXd06YXZ556rx8uTiN0Xfi5sZrNes5fvywzkB7XXvrCneOYTWcBgvfHeqKXxjFlarWoul7Z8c4uXj_CAituRLVTrMeU3ls_yohmbiiMA9S42s72vYgLagn4rvCOsuoiSGJj196ybWVI4SX9jbH0k7aBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
وزير الصحة اللبناني:
البديل عن إتفاق الإطار هو الجرأة في الموقف والإستفادة من المفاوضات الإيرانية-الأميركية وليس الإنبطاح.</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/naya_foriraq/80597" target="_blank">📅 18:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
جيش الإحتلال الإسرائيلي:
لواء غفعاتي ينهي مهامه القتالية في جنوب لبنان.</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/80596" target="_blank">📅 18:39 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">⭐️
بلومبرغ:
عدة دول في أوروبا توافق الآن على أن السفن التي تمر بمضيق هرمز ستدفع لإيران وعُمان.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/80595" target="_blank">📅 18:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80594">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60dd59daab.mp4?token=XB_LEgFn3ozS-eg0lhduhFm839tvjYM8c3fpzZb10jGy0PxTL7D1lwQZ4B3sBrwBczx7mDEKTGLmf3DUo9dFcirwhTdj21gtCgwGLDKlJXK5aoDmXwJL-7D-NhqNXKMqgGKWdnZjyxLKPboty6h2NGk1Lh3UwylOHWrvuT1Fr_nODwgunt7ek1deeyoypuDNTFcBRJxjFwJrKt7tUx6b2Mzr0gK7w3NXqLOc-04FCNqc90oIKe8xKibNwqxqmnWzT-_GsW6iiqddji5no0XZ2GIk9hEw3uYsyxiF0_oYvuAtcla2gYmMuh3t7bwy4XStM5hGRkDobOz_5mQ8Oao1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60dd59daab.mp4?token=XB_LEgFn3ozS-eg0lhduhFm839tvjYM8c3fpzZb10jGy0PxTL7D1lwQZ4B3sBrwBczx7mDEKTGLmf3DUo9dFcirwhTdj21gtCgwGLDKlJXK5aoDmXwJL-7D-NhqNXKMqgGKWdnZjyxLKPboty6h2NGk1Lh3UwylOHWrvuT1Fr_nODwgunt7ek1deeyoypuDNTFcBRJxjFwJrKt7tUx6b2Mzr0gK7w3NXqLOc-04FCNqc90oIKe8xKibNwqxqmnWzT-_GsW6iiqddji5no0XZ2GIk9hEw3uYsyxiF0_oYvuAtcla2gYmMuh3t7bwy4XStM5hGRkDobOz_5mQ8Oao1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
بعد إتفاق الإتحاد الوطني الكردستاني وحركة الجيل الجديد..
بافل جلال طالباني:
الاتفاق بين باك والجيل الجديد سيعيد توازن القوى. أصبحنا القوة رقم واحد هنا، في بغداد وحتى في جميع أنحاء كردستان.
شاسوار عبد الواحد:
احتكار حزب ما للمناصب خطر على بنية إقليم كوردستان. اليوم يوم تاريخي للشعب الكردي. اتفاقنا ليس ضد أي حزب أو شخص.يمكن للأحزاب الانضمام إلى ائتلافنا.الحياد يعني عدم التدخل.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80594" target="_blank">📅 18:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80593">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c843cb12.mp4?token=Ouauz2dXM_EIb6hlnauCJuFH9CY9PTIsqtBU7Ass4vXanhiBqTR3kvqIW4QeRxqV1BCAbSLMxtNq20iOjS25WhUajJV_eDq5-Cel3ceiICrAJQeO0Bv113r9jDgL6SYLrM0Q5CIaoweFD21IQQ1Alx3Y868Tc8cQF0d9lYRUffjDaIcyB5thWmTqItFSJF-LMyvXwsb4D-OGJ22yYaI02LB_Srb51yZyWSFpo_6bxqZltRWrCLmzqwZ0_KsYDkoDwwcfFtudMZ67YBrANXW_bUFlfo2N_pG1HwYil5Eltf9K-FVApg4WC0wZCbkHDY4JmDysESBxqkjaXxCShq-CYFtih6ojcfRrVAWxpswaVc_7IhJD0Rxg5fMfVWhp9Ryeed_4lNonZir5ztRMbp_k76BSiTpXA3dTGS56KnwOMsqX4PTNW78mpFYRKdQXgaYf9gCd3OhGNH6dNtv3DWhAxh92XpuS06cI6bTmel9z-mhnCw6uD1VcYGqCysUzCQvxOlAw6tZujBZ8Zv_dMDMxbUOq8SGnHHIoNP54QoxHKs1MJUBcPgjk2naBaxD4LhHwubIEmnK_AhTPu8uRU8TnYrQpLpKYWeYPUZvWi9KQwNefJdigF1m3g6iekMcxKjkigDM_i1wMJKNsl856nt4JH4kYcXcn5oBhwgUKjgKnY7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية من مصلى العاصمة الإيرانية طهران حيث سيتم فيها إقامة صلاة الجنازة لجثمان الطاهر لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي وعائلته ثم مراسيم التشييع والتوديع.</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80593" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80592">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
رئيس الأركان الإسرائيلي "إيال زامير":
تظل إيران المحور الرئيسي لجاهزيتنا؛ ويحافظ جيش الدفاع الإسرائيلي على حالة اليقظة والاستعداد لتصعيد سريع وعودة فورية إلى القتال.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80592" target="_blank">📅 17:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80591">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🌟
الخارجية البحرينة:
تعرضنا مؤخرا لعدوان إيراني غادر بصواريخ باليستية ومسيّرات.
‏إيران أطلقت أكثر من 200 صاروخ و600 مسيّرة تجاه أراضينا خلال الحرب.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80591" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80590">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🏴‍☠️
المتحدث باسم جيش العدو:
أنباء أولية عن محاولة تنفيذ عملية دهس قرب بلدة بيت أمر شمال الخليل (ضمن منطقة لواء عتصيون)، قوات الجيش تبدأ عملية تمشيط واسعة ومطاردة للمشتبه بهم في المنطقة.</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/80590" target="_blank">📅 17:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80589">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duR3XTqd7M4Bf8OlGYFDOrXnqSb8bS7vtQlNrRizJc8-zY2CSj342FAQ6AEvNzNFBYMQ9Iv4ja8CQEHgUOTD1XsjjfU4oNX9LDK0SGetFW716PwAuo7BfzkmIiLdl01DfrG_MMyvxTlfsBTLu0y4fSlBLcqQNSrthq9Oj-9SsDROv7l1w6F6NCKMsNqzQ52tv8iHJ5sY2JIhnml1cpXJDvaFcUOBjk5Vs2iKKGMan0Ujvz8w_Zt4aaWyWIXCmgC8zCtCreNMFD5aMy2lTPtFDPrxHe6GA8OwjLhXvP69id71-vo9M4YK-ha0hHpO_R2YXiMKgw--XaSoOU0sb0oicg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▪️
إن تشييع جثمان الشـ ـ H ـيد القائد اية الله العظمى السيد علي الخـ ـ ـ|منئي (قدس سره)
جاء بناءً على طلب الحكومة العراقية، وبالتنسيق مع القوى السياسية
.
▪️
لنا الشرف مرةً أخرى أن نُسهم في خدمة تشييع رمزٍ من رموز الأمة والعالم.
⚫️
المدير العام لمديرية الإعلام العامة الدكتور مهند العقابي</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/80589" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80588">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ارتفاع الاصابات الى 15</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/80588" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80587">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ارتفاع عدد الوفيات الى 5 والاصابات الى 11</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80587" target="_blank">📅 16:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80586">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80586" target="_blank">📅 16:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80585">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‏وكالة الانباء السورية: 4 قتلى و10 مصابين في انفجار مقهى وسط دمشق.</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80585" target="_blank">📅 16:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80584">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">هكذا يتم نقل الاصابات في سوريا بعد الانفجار في دمشق وسط غياب تام لسيارات الاسعاف</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/80584" target="_blank">📅 16:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80583">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f42a8a6d0c.mp4?token=sizr8aIvuEFlyfDXMmousp6nLyciOtCFiEKDgrRv7dqdX7LYohvuuhPWxfj9SX4ILd-h0OBuulflcC4RNNVvlOmabw8mzbH4TNtclsMhG8tvqPNhhVadGN5amLCUfCN-gsBkYMgCa2EmKIJ7T6_uS-mQGPslQ05LzagaxOfJE0j7oxap8FZD3DBKbX_kr2-XfhpsgaA-G1NQ6g6dhwecpNa-C8RpCsUMhl1Gp71SCE_VIIGk4sHddpZGa9r_uSMsR7JtMO99a7srf4c1_cxh8VUVzmuiCG9OlC4lCh8d03wuIRha0222f9O06KizwB6XJ5B0lypzM0l1kzCdaksQzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من جبل حريري في محافظة اربيل بعد استهداف مقر للمعارضة الايرانية الكردية بطائرة مسيرة</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/80583" target="_blank">📅 16:26 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80582">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOn37EwLvhZOOFBfftf5Aiz9Ms5Rjc_zFTgeoAg5CP5GO-Se1g12o48zPDHWIzpAcmwYoVXtj5ak2DtPUELdO4YzgQWC0Doq9DOf5eQOa9yQ9yqo58imTUhXa9Y0nhF-4XH9PDbpiat0xC8dXXN1nFqUFVWV3aR3huVaDYS1bKyiip3H50AL0WNA6oQjqHNo4EJTBFPD2yqtlUXTKIFbzSqQrnNEWNKX0LSsC6LOkpVPidVV6sh-BIbksD_d_AeHnufJujAHqFCmzC7KXzx9lNWgWIVB0QwHxyifdpjwbZRf9hANot5B_XfhI6h0eQExTNZyyOJzzjDMox0EqH4ohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام سوري: الانفجار وقع داخل قهوة المشيرية في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/80582" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80581">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5487b8626e.mp4?token=tAUms2BsLXejaszZ1M4jH4nuXOJ5Ag6cSuREJEX1f28N8POZ9ZkNSHA0rBQL90hwhlpLy5vqsqqsZmG_zvaaKYPdT6lSI5SS8up15se6oYaUDRLf4MXpR2CqvXyvkUk8EVtjopnTseinqJQ9JoxEbbwGl8618Mqyyq3keJRtQP-EERyLJ3NGuquBxDM22S0xWexlAp_y9hFsw6-ewQjn9GU8xYExO1dPhc43pQFO3yXlkhCCAX9WIwhEmoikpLgOGXFTU7VvHZFZVZrMA8g156Ccf06HQnrSkdQq2f0jxv8i9Zff6UGtW41tvPBvDZoLQDrhkZ-NOXuk2ojQkHEe7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/80581" target="_blank">📅 16:18 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/80580" target="_blank">📅 16:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=tJeTI8zCzLZ9700AGXPla9jt6Ip3COEY0gxL4oJYm_oLRHTaiCey230CRGz2AKY5bikzdH_q5D-UJbjv-BM8C_5jb7D-fpmLEiKovGbqlcLmYamKBkKnGbSHc4o6Fp1WyvrP9ytHmWMqp53nIDpCNNuAOQSCbPrQn89wp1TzI_b_Yia6HruC4gZyC6lYm3d7g3gSXmZZKYQ8TADkCeXnaFV9QO14-ZvAjNCuc-jyqygadh0CoD0dFzx1iY8gSmsotdWB-LlmAM1Gc2OsdPdk8PmD35h7L-ZZeJsXyPs-tvgkaXu4xcqRI12mfg66y7ihOXO7ekfv2f_24gRtILf4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2773ef443d.mp4?token=tJeTI8zCzLZ9700AGXPla9jt6Ip3COEY0gxL4oJYm_oLRHTaiCey230CRGz2AKY5bikzdH_q5D-UJbjv-BM8C_5jb7D-fpmLEiKovGbqlcLmYamKBkKnGbSHc4o6Fp1WyvrP9ytHmWMqp53nIDpCNNuAOQSCbPrQn89wp1TzI_b_Yia6HruC4gZyC6lYm3d7g3gSXmZZKYQ8TADkCeXnaFV9QO14-ZvAjNCuc-jyqygadh0CoD0dFzx1iY8gSmsotdWB-LlmAM1Gc2OsdPdk8PmD35h7L-ZZeJsXyPs-tvgkaXu4xcqRI12mfg66y7ihOXO7ekfv2f_24gRtILf4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80579" target="_blank">📅 16:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80578">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مشاهد من المقهى المستهدف</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/80578" target="_blank">📅 15:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80577">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=M1BIhsbJVDIlBwuhYmfbUvuJL29i2sfBKHGfIwiYCUiteeSzQaSMs5-WILUegOzq9NbXpaVPczU_NgWZOAuO1lDXmpLbJ5pMSQv-ar0yHext3m7WsVw3AYpM2TnydyDBcv5xYIAq7GhK8xO_C4hw1CMSQ6r0GXCP90NeW0i208CjnYkFskjfI8DxEiv38vMJvowfIy3xMKVAmop6xl8-w9ewGfyMIW2TLnEC3gkvrR4fN0uMsc7JdA0Nn5g4qDEDE9oOLOJ2X5ATTaVIbSe76GkgWtgX9zI0cG0vsMAntQV0Bbtp5a6VL1Ksx4l0gpQiLUpOL6Z8R5x2R1qm6honWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b37ae7cf1.mp4?token=M1BIhsbJVDIlBwuhYmfbUvuJL29i2sfBKHGfIwiYCUiteeSzQaSMs5-WILUegOzq9NbXpaVPczU_NgWZOAuO1lDXmpLbJ5pMSQv-ar0yHext3m7WsVw3AYpM2TnydyDBcv5xYIAq7GhK8xO_C4hw1CMSQ6r0GXCP90NeW0i208CjnYkFskjfI8DxEiv38vMJvowfIy3xMKVAmop6xl8-w9ewGfyMIW2TLnEC3gkvrR4fN0uMsc7JdA0Nn5g4qDEDE9oOLOJ2X5ATTaVIbSe76GkgWtgX9zI0cG0vsMAntQV0Bbtp5a6VL1Ksx4l0gpQiLUpOL6Z8R5x2R1qm6honWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نقل عدد من القتلى والجرحى بعد الانفجار في دمشق</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/80577" target="_blank">📅 15:49 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80576">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afbe8efc5.mp4?token=cIyECsedckXzfVFcwDtxrgiP3uhGemz5CLRQZQdonbNoiNJclGFWNjGjxXX5Ry3rldLtTn5TLlGM0ILIdZxbCWtwVak7FdO6w90iER4cGcSUUZXb1smTDqT1RzOPz8ICqvyI0LvuiWLeBINKYTIvuHWI6kdOkns7Dl_-NrbmM6NtuDgveM3qoPaM4ixY3Xc58O7ysIZdHh7IRWNsNE9L4CgRP3naqPnhZ1f8wqOl6QaXbj7DzIok7CuUy6hf9gTL6c8SBWSq38pDsOpjNoDF0v6LONxEWW_sTtA9YcPduAfhqJsseLkRnLFCK7NnsEmdxGHY5xthNYyyxOzaFYiqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من دمشق بعد الانفجار الذي استهدف مقهى في محيط القصر العدلي</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/80576" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80575">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21adf25199.mp4?token=gAB2_T1RmjtogQYW6rSiDk2bsZWsWIXGoEZrJuJ9dtDs7ke_E9O_MSX32JS78Df2Gh-y7uibqsCcXvkxQHksrhoeg79QJ5sxBpfiW7xiwRJ9Iv1EsSK78s3SRXhoI-73btej_ejo9xO6mnO4hN5cpN1sHrJMJOGHr46ZuAsd9CnJp5wFd5M1o9OoIOYYKNqDgaCGAyh2shPyZSH00vC2FaHkg4eEG0EJXszdAQUEx0q9NfGcBV-zDlwcMCTt-HKlPP5xYAS8DPXEAOthJwFEWSF62TJauC5VwGCV11IMdqP3Qr9v3sqJOCNwzM_FRd8wyf8jde8-zXI4xKFVWEH-XyRUXZkODjmc4XSWKxolMz6LWk3yKIPuxh3mEMqWo84bF_VNcM42e_TImVtW73OFhjocR8MqDgLLY3hxg3tcGdlRrcegVQCQO4LkFQ-fbis0k74A7CDF5Fy7rHMuYtePkNsJF_t-3_nLwAsmwMqvd2vwfQUmVcDCq3E1LUloTvpwIsbq4UXl2vDDYzf3IvvBIHh6WDEkhgO_3oqHAMoiISPMAWu5bWfh_8jwas3dWozRZaOYVJGaMpUAom3scwcmVqAOV4_FELuKKiQbMmWfX5wgXgy8aSlJ7AlHvofNsydvfRRDhs8cu5Jq9bk0F69yhNBVUcjrr-3cYY6CBgAbugk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21adf25199.mp4?token=gAB2_T1RmjtogQYW6rSiDk2bsZWsWIXGoEZrJuJ9dtDs7ke_E9O_MSX32JS78Df2Gh-y7uibqsCcXvkxQHksrhoeg79QJ5sxBpfiW7xiwRJ9Iv1EsSK78s3SRXhoI-73btej_ejo9xO6mnO4hN5cpN1sHrJMJOGHr46ZuAsd9CnJp5wFd5M1o9OoIOYYKNqDgaCGAyh2shPyZSH00vC2FaHkg4eEG0EJXszdAQUEx0q9NfGcBV-zDlwcMCTt-HKlPP5xYAS8DPXEAOthJwFEWSF62TJauC5VwGCV11IMdqP3Qr9v3sqJOCNwzM_FRd8wyf8jde8-zXI4xKFVWEH-XyRUXZkODjmc4XSWKxolMz6LWk3yKIPuxh3mEMqWo84bF_VNcM42e_TImVtW73OFhjocR8MqDgLLY3hxg3tcGdlRrcegVQCQO4LkFQ-fbis0k74A7CDF5Fy7rHMuYtePkNsJF_t-3_nLwAsmwMqvd2vwfQUmVcDCq3E1LUloTvpwIsbq4UXl2vDDYzf3IvvBIHh6WDEkhgO_3oqHAMoiISPMAWu5bWfh_8jwas3dWozRZaOYVJGaMpUAom3scwcmVqAOV4_FELuKKiQbMmWfX5wgXgy8aSlJ7AlHvofNsydvfRRDhs8cu5Jq9bk0F69yhNBVUcjrr-3cYY6CBgAbugk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قتلى وجرحى في دمشق بعد انفجار في مقهى</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/80575" target="_blank">📅 15:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80574">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/80574" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80573">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سماع دوي انفجار في دمشق</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80573" target="_blank">📅 15:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80572">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkDVVJuisDyh16MNw0kT8Uff3wNlh4DajpIVRUDbiSYbHUYYMZocX88blGthK6Bxdc65Ec4boZE0QQSntbU46wAV5svsNVTKaSoR4TLy2lwNiCMbsS2f_EVkaWzwetKxAfGK3SbVq5LV7b4DOB42p6R03m2KC6kcdCSOfhmug3v4yX6mpsio9JQRdY3cFu5tJniwKSNChkGHMG5PGoJFCQ8gfqzTRaorJFSSYOl3dFw8m6e63DxgalxtVDv5JD-gK-82ZtVjmo4Fk5rMbRNBbLw6Azz4uQXh7CZNi3dWILUSDRtUSH15DAZGJfsHS809d4rMSznq3-nzFqIM0yzjaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ترامب:
تنفق الولايات المتحدة أموالاً على حلف الناتو أكثر بكثير من أي دولة أخرى لحمايته، دون أن تجني أي فائدة من ذلك: الولايات المتحدة 999 مليار دولار، المملكة المتحدة 90.5 مليار دولار، فرنسا 66.5 مليار دولار، إيطاليا 48.8 مليار دولار، بولندا 44.3 مليار دولار. أما دول أخرى، بما فيها ألمانيا، فتنفق مبالغ أقل بكثير. (2014-2025) أمرٌ سخيف!</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/80572" target="_blank">📅 15:34 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KeLsiygtA_6PXeoErY8CFotcgarBmoNzDxEVXudju4yfGMzZZWSgs5tMuAEpzl9XZYOIkjilxxT2olhvd6Kou1nAE4reoJsEg43Auq47dCQx-xCnDdmrfd06sZLRQqTFaIHF7BKZt4wZWnjPZxzzpz5bdkKqwPXxKdvxxXOy4lmnmoVKPtGr-MWd2hbLvT5SfbFUNml6BQ944FQ-BSyU6_jnFa5bh8F1iClBue7kGuiiMFvM3BNPIjcVvBF153Q3Wg-vS869gSQU8GFoW1aKom5DOLSLZOP-tjuWPu4yvKw3NtsU6aYXvmjwb6HhtzUwnt5ruARJzgJA5RS5tSyOWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWWmbVO-YQiWcJ-et2Eb0S1UUaeMWTNQQkEj04OzSqA1GbMfAhI47qJTWzifEtNquU0RTsyoUOtpBVR2V3UOX7fvIl-2YxOD1o6eN5ZGdLNBx6C9xYxQ9gQTFawwnN-9UBtvb4umWNq2gQ-fXYhI6n4vEktZAFrnZlL7yT_AofXMmT6zapv1IWrokxp68HoGPoEZMl5qXuy5X3zB60p0oTAB6yTFOwP2aqqC_fcMTcq45nfVzHboequRsgkSTmJwCye0lQSyYOfVi4Dv8KJjx9Dj8kIIEj0HY0bULutjt8pSa6qsjsHVtgEmF4b3i6Tnp__xBnbqlI9pOlwiFaUCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRbGhoEWpNICAMsiK2t7gq4BM0pVn3Pv4mQ_PJq7b3XOGuV6oYfbNgZLpOcOLoYXwwec55VimdPLHLf6X31sHtO4uaNRKsTZOirLJT3VsE3q0PqoT4ZVP7LaHX70CVE-rJ4qTUsbn1zW9kAxVhyE3eG5BbSIdSx9GGxo3gH_fyELUel6epftfp5mkSnKQ1f6_IkCZwgGPsY4aAVFfHK7Kba2uyDCHOWI86QG7Xgt-8vzVk6ka1Dqh8eWwm0ITKUM_n3N81_1PlOf0YHlyK4wJiK2z5Jo3dL76rfTy1bPOQlqEO2uLRQWNT5qF4BwHfkrqUJBSXmNhvLLd4oTbJz7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWHGpX9T_9rjklB468HOKyJOB3VkwMhEreRN3Af_5ZjkWwUZ9dx0TvxXGHHfPrxfUafmWoSiGGZcdBYrFlb-m8j-vQPeb5Qj5GED_HNPBEaMIFyHGWNat0hq3EHB4VrCICWZsqj-NP_w619TOfhkKdhdGsy__YHLqEwiW0GuqOHDLGeKXnTjujrwSPfXM0SFDk6aPuzdR10WWhbG6oMPlvIblM72FPGowmXWh6ZAJnBAT8BXXY8cFV8zMNfklfZpsY_2Ua19NYHGYAyKFRUVKoa7nWrZ6Hoh1Zt8sFLaRXdnmmkBfcAXfyLGguBwx3qASLF3H29i-hwJOn2x9U9YDw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇶
ضمن استعدادات التشييع..
الحشد الشعبي يواصل استكمال نشر المظاهر العزائية، ونصب الرايات واللافتات في المواقع المحددة</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/80568" target="_blank">📅 15:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1ed8bed24.mp4?token=M8YnHFZXVZvmk-DJTyHyy3lk9VX-UCA4mEHsaHDyg-Tnz0Ga5nlhnRo6BP84vv1hgAFT_T7npAJaRgF-uCqhD-Nf-yfqm_yhDTsbCZhjHYEM-dG-Qwgk9pja60eE8VVUB5RiGL1onjqEmXhi7QfRNEkEbXChLYA0PE12G1I6d9Xi6Le1zcIjHw5R2bYtxzVFTXlx1cZ4x1u1bQvy1mfopx8X0HDpDgt6xyxr1aQtW2pPg_xUZwT-D_U4bn3UFc5IY9LJsBDCuD6lyd_RCYR-m4fEQfvHmI84GsJ0V0E4dmy_c4Ei_FskIG4NcnfpYkdLNSi5_pnqIUgfabzYcObkTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالات اغماء في صفوف المسافرين على متن احدى طائرات الخطوط الجوية العراقية خلال رحلة بغداد - بيروت بسبب غياب التبريد والاوكسجين طوال الرحلة</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/80567" target="_blank">📅 15:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39a62f24c.mp4?token=VJyO0B8CpaE5pwSU6WXFLwnAjspqWG593nYHy8hkk4RIgMc_Xj-E08uH-vnyLxIOFdgD3ky4DhzDBmJqXfBRNiPxyjqsFvbA-VsCpCe-Of5w59fQG7UP9yPa9yRIuPLWS9eYL8qgWKj3gfwpA3yf2iFLV_tPeObIpBbrTMsRbMFdGPzdM_MtsQbD6SIHuidxSFKdyPCvDfxxq7azx8NwTcVG-GCzxfGOq1LBKErtqQS8cCI2OShYrNqc324aI4N66LnjNEf6p85_1UEjdcQ7AdpdrtsAo7BJSyOiEsWZe7yNgQgJcluJx3iWPTsC8vhjqF5uXZY5dHt_mtIK7sLeZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من التعذيب الذي تعرض له الشبان الاكراد على يد جيش الاحتلال التركي</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/80566" target="_blank">📅 15:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80560">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BslYbU6IV0gucLOJ4eVc8p-XZZ90DiunhIpEhskOOziU1XfAHLuKiOOhoH6r1C5wYwNsoyOb6Isw_KUtMwzo0HMDRGe-FdG4i8QygK1Gm6-3txfXkMGi6FRWViaA6TdnRS_T6ZlnJ24nT1HMZ20GX23k1zHil9PPCwDy1LSnJMIvtm5TEmICKZqa_Agx8dGNRGJ-q__M4lYJZPndHZfL5rwqTxDeCOZeIVH9-zNmbbPsX76uIVHpalnUqW-DxAqqZkYgPjJiGmhZHwnrFA42s9F0THiHbr-tIxxk_2NFaD_AR-khTYLNzG3idIiOKwdEIiI8QwFVhdzMF86XmN_CCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TUfR_9vW7dnPwMm8W-BcPGEAj0I9eDUI0ND1UymEJStAatzs5ns3JEQaYKxw03VAnu7kpr7CR8cjTMkYQ1ZJEwFDRB6fpKqbt_ZjJXZP0T40Rn7l1NKZ8hxK1sLuZxYW1m6_XiSMhsCCClTty0nIb2OPEPkPi5nLA_NgRcKT7qP310zMRLjgFlJQcS3vPTTeT_F6K4pSoEQhwMxoAZa8yc0-zFEujSRB9K4Zsd168wp-2ydZtc0E4XFkJvNURUQpN9aG0sf5N23Totr8EViEvAJsnkwOtOEgQU2kuf7ZNlCotra9xU4vrjAI-KZchHuu-q98vEso4bUDOcDsQ5esRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZQdo4A7QUWJj1m8WNh4enrUgcSTcBrv5ejXqDXOI7ph_9IjG6qu3X2I-W5CompUbHl-X5BD-fX1OXXwmhc4-3LX2Wu8txgoorfAM5PZD22EDvs41KDav428-jkiMPkj2ALZLcgcRp0HUCQKQKdG5unEr1GEpo51_oXZVExRZH6eUBB7oQ4VsGYBeH_s7_Pumi8hM9UuYEzjkE38mPjGRrIaZ9pH8V-A0VFs4vuHSitb0hDK4ognSPhCAQCDyw4q13ANre9k5WgXsBR-p4TUXDYh13cZhsQ59d6aiJ71TgreY6HZ7ImHGCjTuy59ttzKyoUGUZSNWItaz-kZacT1v-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tdwbCO_F2AL5hIokYC83Ype3rsjB6RYU2qTbN1rbzw-vHG_KEyw7x0ghhkRn5O7OWqqlzgx-xZY_RsZUi_IKUeDUwNiEKgmqWMlGY64fOjWArJsNMa6mhkW8Ghib60rQVnjGu7-y1QnGlefYxyvCGHVfx2EqPYdx-CACKUMhVcCEoQv33BpPryQFE_0Yv2UQvtjTDJnjERLgvKb2fLdF6HUAMSNJb0dwMXtMVTOEWSqBRkXUmmNmbjH06b-oCnh-pMz8TiC1IQLSdUeaxIvhz0ZjJXVGJepwUtDwkSXwehkHFWPhjQ6fMpFgjv-sUV-U2KGqvKKzhBKewyoar4F-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rUMO0m8g0-X43SNOkGVqxlPYEk-uQkKQaT26OI5WYYxM-vS9mIR7NEMGCzUgPDNkzaBp_K5ybA-a3cVrT0xASwRGGOS9Z1MAd-hkHMWt6DdZ7MLrN9L0AjHtXxiKJVO0_chha1C7noaJNymj3wTbqOQDdQR8aEdeNVdWFvY9H5y3Gime3t513qWu0ZVhX6tDrWFzRuN4ufWuKDIyBNnyQJNPOXyNWa3fE5KfDTu7hx6jy5sOZXZyWbNS5Xp1s0-5eYLjpXWmXj42NikH5WckBq5BlhOfGxDlBb5h5g1IO8eWlcs6ZRrE1q0sXp_tmTvWdOodu3BQxaunkXQg0z8M3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P74J4qZx_TRJjVpaA26Hz1Rskkv543aLJUSFtB02qiq1osDxwDRzU-1CjTJX7zHbUYgRQMahWYF5PmF5UGLBnTELAEtsvHWHs6U3qiiXU0kFLWDWWgE2VBksaU4ki-NxCikrq3-YfZ6QuJEMJc3LDc0D1MBHMWYT0M6wcFqnU2LdYAzkpcfpJlM-ClBLZP9C8n98uKtBKflUrUSWDQphz-7bPgiI8IYDKVCUWHinL6zz18cRUKWS6_v7_sXSVrBtRQnHxo8PaWnf6HydlcIJbbnuVxe6-t3YmIdluTZjWb1OWhjiRe5aWZL9NJU7peoYaATuplC_4ShF3t4lgG3ANA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جيش الاحتلال التركي يلقي القبض على ستة شبان اكراد في قرية شيلادزه ضمن اقليم كردستان العراق ويطلق سراحهم بعد يوم من التعذيب</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/80560" target="_blank">📅 15:08 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80559">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">توقيف الإعلامي حيدر الحمداني في كربلاء المقدسة بعد شكوى رفعتها العتبة العباسية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/80559" target="_blank">📅 14:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
أيدينا على الزناد، وأنظارنا مصوّبة نحو العدو، وآذاننا صاغية لأوامر القائد العام؛ فبمجرد صدور الأمر، سنخوض الحرب ضد العدو.
المفاوضات تقع على عاتق المسؤولين السياسيين؛ وهم يؤدون مهامهم.
التفاوض معركة تُخاض في خندق مختلف. ولا نواجه أي مشكلات تتعلق بالأمن.</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80557" target="_blank">📅 14:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYOaGzq1qf1Kb7HQ9vPIKl3kQGwbitzXTE-ZFCA_OnnnLRY4Ge1pqxqDVtu0czf04mcYLKFtmN5Al96bK0fXW5VKrKBKeG_MtkEozLKBmQu5RXehzoXsWhTRClrVn54voQvdX66QK-liImgtexRXgGmqACl9AxNSh05rKxYLntywFILHBawq_GT5FWKCcHGHx6e-Pl2hz1nOBfrpeTuB852LCtIM-9XCqYcIGsZ-iwqFaINj7vnX7KFXquRJdXcofd1Ha4JI9fvQ4NSKhmeumcQfSnMlVRMhPPMBgDQkSGOUHpxh75kqyZO1wl2grZ_AMay1ogY9BqUbcfIpTFKRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇬
السلطات المصرية تلقي القبض على الرادود الحسيني العراقي السيد مشتاق الأعرجي إلى جانب نحو 50 شخصًا من جنسيات مختلفة بينهم عراقيون ولبنانيون ومصريون وآخرون أثناء وجودهم بمنطقة السيدة زينب (ع) في القاهرة خلال احيائهم مراسم عاشوراء.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80556" target="_blank">📅 14:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raCINI53BwIE2f7zeDUWITX8FjTBBftueJkGsWdVsMsxnyM3iD_JjR9aCNMsefBxiroWkxQD08Mlo2Len978SVbSvvcX7_jJ0IgW2NcMBy36GkyKcIBHSEjQYOat8WHeu1LCawL6oB915w3LdFq1acvS4Kv8AzpDexPhJz1CivnY8ycRXLJs88tdzNOmCByejgzY8IHtz8DlcmM3MqWH67wqiXY1KOurEWl29sN-NJDE1OVK44QMAWhW14gUG6x-hOZzr10y2-ZhNkCRwIhRjPEYnVm7BsIlQyiGurDiQbRTdk1OcBBS94eSkw14DIR3wQizJWMDY9D51CQeu3YL7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
محكمة التمييز العراقية تصادق على حكم الإعدام شنقاً حتى الموت الصادر بحق المدان عجاج أحمد حردان التكريتي بعد إدانته بارتكاب جرائم إبادة جماعية وضد الإنسانية وأغتصاب وجرائم قتل بحق محتجزين من ضحايا عمليات الأنفال.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80555" target="_blank">📅 13:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔻
الجمهورية الإسلامية الإيرانية تعلن تعطيل الدوام الرسمي يوم الثلاثاء 7تموز في جميع أنحاء البلاد</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/80554" target="_blank">📅 12:50 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">قناة خاصة باللجنة الاعلامية المركزية لتشيع الشهيد الامام السيد الخامنئي "قده" في العراق
https://t.me/KhameneiMediaIQ</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/80553" target="_blank">📅 12:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/80552" target="_blank">📅 12:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80551">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">▫️
سيُعقد مؤتمر صحفي آخر يوم الأحد أو الاثنين، للإعلان عن تفاصيل تنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست نفسه الزكية).
▫️
الاجتماعات مستمرة مع جميع الجهات ذات العلاقة بمراسم تشييع الشهيد القائد السيد علي الخامنئي (قدس)، ونؤكد أن جميع الجهات…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/80551" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80550">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
سعد معن: التقديرات الأولية تشير إلى مشاركة ملايين الزائرين في مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
أُعِدَّت خطة متكاملة لتنظيم مراسم تشييع الشهيد القائد السيد علي الخامنئي (قدست روحه الزكية) .
▫️
نهيب بالمواطنين الكرام التعاون…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/80550" target="_blank">📅 12:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80549">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80549" target="_blank">📅 12:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80548">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoRoEjI544r7BJGYuWxa3GLDP7O2I3-c6j1MLEHce8zKC3bcCsJVsvSYun7Ch2sb50Bup4x82K5FXVavNIFQc_73sxTqmSNwpQgGg1Lk-DmX0SECFRGjLgSPMBMWK2yXIcCjLv34U21UgMWXckQ9z8nLIriK4i2X14v7RR15iJqYF-TgvaMv7E_OfacGyfnB8eO0cOPyGwFXipmCRW6ibvBmHdjqXfWuCHHodjdjQVB3zECe9RrQO0RPxu9QA304hMHb31GifuU0CIhEwDKMawSyzJ9-gAFBVT0tUcNZISFafOenfmuA0EKqx3kuc84JAK8q-7U31_A3QXPUfb07ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
اللجنة الإعلامية: ستُمنح كل التسهيلات اللازمة بما يضمن نقل وقائع المناسبة بصورة دقيقة ومنظمة</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/80548" target="_blank">📅 12:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80547">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔻
الكيان الصهيوني يدعي إلقاء القبض على مواطن أجنبي من طاجيكستان يحمل جواز سفر روسي، بتهمة التجسس لصالح إيرانيين على الأراضي الإسرائيلية.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/80547" target="_blank">📅 11:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80546">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
ترامب يُفاقم شعوره بجنون العظمة.. حيث نشر مقطع فيديو تم إنشاؤه بواسطة تقنيات الذكاء الاصطناعي قدم نفسه ك طبيب يقدم خطة علاجية لما وصفها ب"متلازمة هوس ترامب"</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/80546" target="_blank">📅 11:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80537">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCz2RraJwDPWyFj1PHqkk7D2_McnEEY1ftk91cMQcGHDIhksL7ZuiCHTJO2Pzhw8iIvzh3OELFXpyNgSR-iygWrbh2ytk1VZVbxjrjkvgNVy8MZeYq0mVCnw7GJY_IVy9gDpFVc3icyzkHeyXKNOL_xLf9kT6BQiYVP_UerTxQRHtPBZYOdVVkr8Nw_4OpaxctMmTupzHtgr6Q_EhG6MYJKdLbzLQhfVbynVA8ek9uDVzEWBrjXA2johNr3z5k8CYB5N2r-F-QofNzIfPScajN7ENQC_Dz_1IhvNDGedbB1fzglTm_7OWwdpv-XIu9W71fnUHGkNHLMNSkxlDUCL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bwANPSHvTJAGcixPAIsNQOzWftrMTZ7rL_JCBm3kFNTUwSDUCg4VEx2XagstkVqxdSLOo-F5y3KZFlxKmYk3ujWKz6Ko4RBuDBTxy4rxXzhwJfdcz-YspEq7pH8frLHzLoJijyNBGY3BJWtBWGDgExvZ8SRnq7Hov62TpnDhce4_EjWaVZOXv9_oDgTmAp7oR-qA0rilJwEJLPVhbZ6VQAFAB-LbSep5SZG6egoCIF14IU3YxZqWWfmT0Xe5jc3dUWpB5vxnpcHp3M7VhZ21aa-kD4O8KlbDOJcSMbqv4iNPydZTTzaKsw7GPQU4x3KMZflFybWL0dpf7zyrrT_k1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gfT1_hz4iIvacqWEWpr17GyU-nnrq58gb2qHeltvbMc4HIhFxgiY0nyZfQiPq284ky2pGnYDn1jrtuLw4YbUSNorWC0wUYKYidwFscPO6o_FGZVHIaKxrpjD0lo0v-d4KFA7j57klL6PSLUxFKx2DIIjJmXGR92eQ2z3qA3GX5t-7lcmKHH0M3W6NX6rFV_7j3zYKprPVViXaRw7KvIy6OrHLH1AkM_1ymvEt46ncHa_QnHZviESChwqwrz3f9omuCQCzHe3GI5CXPBw6lWtJ6_XtYuCroVy0IyujsZYl9SDPjMFtA_iLf5ppqosOHF8D2NdMoIxQ21lePloQSl0ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbPFNWpM2zosJu_imCHoFNW3TsqiMkjTJ2OBn_7MV84muwCDeVmmEIBZXvOBx9xYeWxiXIshrNEhrTtbW9iDKPG8ijlGt7EBLA_GeGB_zR0s_I_KvT3nMAguaa9K_RQOhAdlKbjbRm0q65XbCwc_gOlIC7GLclCAg9l1oZt3aL9BcYTxhS6OeJWCn5En4KU6cTh62LzMHpNAtPiAanIMcDwyIuufhLcaniGt4D_EDWzJ4JV0Bhd0yC3uH7B90PC1fvOfEZlWLhQYx4VhmzTxVWYkic9A6hxnh82LXZrj3Z1X2X9o7ZTPI2GO94Pl8sOKLIgAhw2QjxYT3hR0XQ7kMQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
مشاهد من مراسم وداع المعلمة الشهيدة زهرة حداد عادل، زوجة السيد مجتبى الخامنئي في مدرسة فرهنك بطهران.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/80537" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80535">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6wfoH-2EIq227p31jbjnY4iab-S2Z6HpnZc-Sm-E8CVRe7tFIJmfsBU-6AnWfQloaf-A5d4QOmfbpatJcP1YYLYjih1ww_Y6q7c-gf4YuteHOmkvLbTxk-h3KEQ2xfMTPiKGVdQWj1BfLdKGLkx7k7bKP3PhgAn0ZGN3w4bPqHuAVOOFATMbwFzcpPMd513p1R7OVn3f-etbxhmxR1KVvJdAcMHgIB7LZj49KO4Ph_gwjJCtGT2mtk4ScBLvSiM5-BZp1kmhU8waiDii2I4hlS4utYKvfVhHZ4xRgwPaMoFUhs31cYbB5GRvOtWPNMAKduHrp8V4-p2lTpEm9WSkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
عصابات الجولاني الإرهابية تطلق قذائف ورمي بالأسلحة الثقيلة والخفيفة في وادي بردى على الحدود السورية اللبنانية بحجة التدريبات العسكرية.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/80535" target="_blank">📅 10:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80533">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
رسالة من قائد المقر المركزي لخاتم الأنبياء بمناسبة مراسم دفن قائد الأمة الشهيد، قداسة آية الله العظمى السيد علي خامنئي:
▫️
ندعو مختلف شرائح الشعب، ولا سيما جيل الشباب وبناة الوطن في المستقبل، إلى إظهار وحدة إيران المقدسة وتضامنها الدائم من خلال حضورٍ مهيبٍ وفريدٍ في مراسم وداع الشهيد العزيز وأفراد أسرته، وتخليد ذكراه ومحبته للمحافظة في التاريخ، والإعلان لروح الإمام الجليل أن أمتنا، بفضل تضحياته الجليلة
▫️
أنا، مع جميع قادة ومقاتلي القوات المسلحة للبلاد، إذ نجدد عهدنا مع الإمام الجليل والإمام الشهيد للثورة والشهداء الأعزاء في الدفاع عن الوطن، نعلن استعدادنا التام لحماية استقلال إيران الإسلامية وأمنها ووحدة أراضيها، ونؤكد على الطاعة المطلقة لتوجيهات خليفته الصالح، صاحب السلطة العظيمة في ولاية القيادة والقيادة العامة للقوات المسلحة، آية الله الإمام السيد مجتبى حسيني الخامنئي.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/80533" target="_blank">📅 10:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80532">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2095ae6f9.mp4?token=lRRTjG1SK3-1rOixoDSVW01nAv49UfRP46B8eQZVXUI8nWTr0ObISO-Mtk4bpqRqYb907W6QCAlEX7BB6lcSwitkHC9pwChU1zbnZrRQilY4CjBXmqyuO_vn3q0hvOww178AyFAx_dr0vq3sILCZrCqTcr8G9MX9-xVV0YpqpWsNcKJPQfC2imTjqZ0Id1bne7MkCvziSwkHwB738L4vr9L_gjuiC5FGd1OCYLcNyEBTIFCp_KGaArNuIXwrI3BtgjQG-SEfi0PSNNYfm5hQCFJTKxvbLTmgh9jzycToF-k86FOMYKFVwqVA0ASLmibRGM55jdwBljPbZLjhyf-OGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
قائد الحرس الثوري لمحافظة قم: تغيير مسار جنازة القائد الشهيد في قم ؛ اتُخذ القرار النهائي ببدء المراسم من مرقد السيدة المعصومة عليها السلام والتوجه نحو مسجد جمكران.
▫️
تمّ اعتماد هذا القرار، وبإذن الله، سيُنفّذ صباح يوم الثلاثاء الموافق 7 تموز، وفقًا لظروف ومتطلبات الوقت، وبعد وصول الشهداء والحشود إلى مسجد جمكران، ستُقام الصلاة هناك
▫️
تجهيز قدرة استقبال تصل إلى مليون زائر لتشييع الشهيد السيد علي الخامنئي في محافظة قم وتم توفير جميع الترتيبات اللازمة.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80532" target="_blank">📅 09:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80531">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
اشتباكات بين الجماعات ارهابية وقوات الحرس الثوري الإيراني في منطقة قازقابان بمدينة بيرانشهر شمال غرب إيران ؛ مقتل 6 إرهابيين كحصيلة أولية.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/80531" target="_blank">📅 09:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80530">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عمدة كييف يتحدث عن انفجارات عنيفة تهز العاصمة الأوكرانية كييف نتيجة هجمات روسية منظمة</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/80530" target="_blank">📅 02:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80528">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgegFlBRQw0iSXanRZyvFCOY38BfTH7zy4O_Ryaarc9GGfq_gNwyXcqFgZjlEUZ1-ZqFoNckByIs7O85-ZWN5yhu0McQXrERt_vd1c0KWrV96vIOzc0f2oIV_cSUT4vL7ssZkiwR6_oEQzS_ZQiBee_0lUWnlr3FIPXpnLK4t2KUQ26E6kY8viLQGLjE4q7ZxcN6LW4Mf7U3Jj-zzVx_efXnco_frQv2PPfN0WZxdBXlH6-caq08AQcAn4C3edCTCcL-KnUTPlnk5zp_Pddrf2fvsWKPdlsxhb31uYhuspuq7JIgJTgpgc5dImUdDTLZWvd7cIvW_dHgsYJK4DmvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKhslfBjoH6oaoSKPlwrmZZNinkmS9mD1vzH4i9Nri2GdfwTP-yMo2hNTWSVVqPLcSkfHB4Z4AJm8fKF8vKZIkxCGyxnox_5cj5K-J_ztpJ6rPJXG7Sa9lHH0buPbuBU21MPsViUq2lCsHPtucqm5M6xBCUvX9ePRsf9aMQgHTjY3F0HTkaho0u8n50SdffbitXdHeAXKTK40G0luxIPQY7ow2kd20rghfnDDfijK33pmcV3wPJyA7wYQYZHRe16xNLGH1EOUILiRKiYGGM-rp3FI-VVvYeeyYstKWjFy4T39PLhNf4tm1OXPfEYTEhzq4D-yqR_d69w2JqaH6EG-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
وصول قوة أمنية كبيرة إلى محافظة صلاح الدين حيث فرضت طوقًا أمنيًا حول منزل تمهيدًا لاعتقال عدد من الاشخاص.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/80528" target="_blank">📅 02:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80527">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdVRr89Aq_SIYjkdg6jJ6e7i7d_axXLjpsLG6cP9EBfZi9cwTzEXyPd_FyqAkcohGpH_Lm-tB_syP7HjgGGSk45Ey7IlhwgtgGhgjANBD0X3lNOPMZ8H-AqKPNZJSmg3lryDW3kVxQAyiwRES1O-pjRBfeMOaKy3itP0Uc_WBOYOh7d2BZp5CQMgIMo8y4iQ1XtaiAC2VbhAhYyGVlEAB0JxrzP4sYZWqSwtn6ZgrltoACcqg_0zFPODavfCvD2cS7PxHhJ5rwaM7Dkm3t0QgKRcIiWpTTP_Im0QtqztwTJ35eZ1mCpUmOVaHmGJf4JOsNicYr8hKqiQMlWmPiRVwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
مشاهد ختامية قبيل انطلاق مراسم تشييع السيد الولي من موقع المصلى في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80527" target="_blank">📅 01:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80524">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCIsHnHT-yYalndYrQsMoKBtb8mfvBU0cekpWCZZLy1ejBvmh9uG3zMmRIzxopsTrQTi0xAysyS3QajwKXBVfaVF1RUspCOcNwUHiX02HK_8QAF1vig6buysPxuM4zrlbLOJ0fOJW_vEMvAZQ5s82CnCr9c4R1c_45Z1iHhpseKakMCxadl-G5e9GrcZlVlEiy992i1-HXwsFVql2UvCpsCsOaXFrjk_QTBgspXiXKku_E5LnlYkgiGnjnFET1xnA3HFHD67Kp0S5ZkDRNDX-V6Z-SSAEX5qUTpaMXqNX2p9bl-2KO4-RXU3TLL_kdbbRi35xBxximaAiG9OZchMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hAc4o0It2-OwWXK-XmccRiFpMbO4Wjacjq2ctDgwtQ5CT8eqT4vLYFVJDe3X84q6P2xkAyfN7OdVDSSUgugzgCfiMv9ZARZDaEw5HyFYbombR8CXlshjKj8DJyKrs-xrb6DdDnBQBxkAf8fVDx08PSNMlT7HVVj-ZV382ZrBNRQSJkapB6kSLzFH3pF-H3QA2nIF4zZ8CtzTuQMG3mGKvg_NhGQltQMlTbCyB-HFD2rvZ04R-s5imcgSkdjloxYgsTvzmEbVesN1BYlpEROr82Rzis45kneh20f6uQslzdi9aSMspvcYOSjtG4DIm-C7bgivxucb2HLBn_qf5u0eBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbtlrC075z_jM1_ISzVa9cHYKWCJb26Rtlb6GnLYrFvJ0TawaSN_lF20fIe4kbP686XTfx-W9vUudzPJ7xwWH4NdFHIlLhzClm5WMoLotCrPemALTM5nMkSKNx5sdNQW7xBEBCLu9FezrAK4azYJhn347NSjBS1B1f5_y6gyT33aWhb7FPjjOLvxVoEM8L2l8F6FdxHRf0Mfxue-kgw-iarZpmcNIhWl65EkZxAPX2UoKXZlO4bqwymQyBSUE2xyQ1ECIw7U3PPDXp4p3-WBU5xH1UQq57PZkZ8SriFbTeDmiNYL3J6yVdLKSyyrssmZTImUhAQA7lPDSPdvQQetzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
سقوط عدد من القتلى في حزب الحرية بمحافظة اربيل بعد استهدافهم بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/80524" target="_blank">📅 01:16 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80523">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=CCt3SAXDBuGMW57orRNCpm2jOD8MeV3V-GvkWGjFfR6VtTMSRFFbXMjxXoYCg-shw2Z1IwjqpNrGFtYf499eiI2Hj9gWIv1YB4KAmTRGEStTgz_t4KN2QNX1MT2B7VTRyXnyb-RpneGE0qRgHPgwSHC6l6bC86fsec1zquUxEaePfsazAluCTGbkdnU7RI5p_XuNGVIawmdkqEFnXIs8DN1FuaZSKBIorQY6uJTc7aOyPzANgcaponHXSdVCBE_Eq1-uZTB-u9U0axmSUS6U9MiZWsix-jSeSiaLjpmLchQZuaXM4IaFyNW6ny2Nk7A9hi8qiopoLzG9CfbyZcf-9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ce18b1c2.mp4?token=CCt3SAXDBuGMW57orRNCpm2jOD8MeV3V-GvkWGjFfR6VtTMSRFFbXMjxXoYCg-shw2Z1IwjqpNrGFtYf499eiI2Hj9gWIv1YB4KAmTRGEStTgz_t4KN2QNX1MT2B7VTRyXnyb-RpneGE0qRgHPgwSHC6l6bC86fsec1zquUxEaePfsazAluCTGbkdnU7RI5p_XuNGVIawmdkqEFnXIs8DN1FuaZSKBIorQY6uJTc7aOyPzANgcaponHXSdVCBE_Eq1-uZTB-u9U0axmSUS6U9MiZWsix-jSeSiaLjpmLchQZuaXM4IaFyNW6ny2Nk7A9hi8qiopoLzG9CfbyZcf-9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
انفجار ثلاث عبوات ناسفة من مخلفات تنظيم داعش الإرهابي في محافظة الأنبار قضاء الفلوجة كانت متروكة داخل بزل، ما أدى إلى إصابة شخص واحد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/80523" target="_blank">📅 01:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80522">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629a285c37.mp4?token=KgRsUFI2BIzvlR_BT_SJ6eyd-l_h5rie2G7lEjgU1Qsbhm2nytn3MwMHfyJxmzt2MW0PKou_WampzKehZEimYIJd822BsbRmOI8EtqUxJ4-lUZyX7_gemjO6kOoC3QpTj6_EFSU7Of3M9kRgMVwIWP84WL-5C44eVXWVQC9pLsh3MS0uyJE4qS4QC6_eeFxCu5dQogjlae-KhTuPLtm0DQiJuQWKa7Ej9ClaBF4oyNzQESvFG6NeNGRFtsV97qnQOliOhfcciinUaqNEUMwGX40mpdHBmfN8fPuzGJ3z1DvCUci42-3pOFJFYfDmmsAI0sCVFMjbH3TxH4gKoEQiJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629a285c37.mp4?token=KgRsUFI2BIzvlR_BT_SJ6eyd-l_h5rie2G7lEjgU1Qsbhm2nytn3MwMHfyJxmzt2MW0PKou_WampzKehZEimYIJd822BsbRmOI8EtqUxJ4-lUZyX7_gemjO6kOoC3QpTj6_EFSU7Of3M9kRgMVwIWP84WL-5C44eVXWVQC9pLsh3MS0uyJE4qS4QC6_eeFxCu5dQogjlae-KhTuPLtm0DQiJuQWKa7Ej9ClaBF4oyNzQESvFG6NeNGRFtsV97qnQOliOhfcciinUaqNEUMwGX40mpdHBmfN8fPuzGJ3z1DvCUci42-3pOFJFYfDmmsAI0sCVFMjbH3TxH4gKoEQiJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اعمدة الدخان ما زالت ترتفع من وسط مقر حزب الحرية الكوردستاني في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/80522" target="_blank">📅 00:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80521">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=BBQFJy0eTy8OSZXNMZbWlxMIzFfLGAQFosZVpDxKqTjHNV6Otg0s0FGc2pMQ4Y9a3KMcFFcax6C9YSDy5B6qIWebmNzMnQ9vp1LXqJ_0_fpQU858iuOXgz7id_-_6R9wogmPK7z8VLX-IyBMBnrrzgGXlHwmCKo9CakUmYFPmry4XMjzjwnVzinvDHt8wGfqafyt-_yLJiQE8D6Gh6tqqFCcRAEpEChylaywSJF6uXLk1RDbSh-PF3g9J1x1rGTZE5-NwXFc6ACOgatnwrjL8A5WHOMTcbJfEO_SDK8h1jUTr8zawZHho1S6rrA5lXiZjkdgFTQMcb4-_7liQNtTRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fa60cf3d.mp4?token=BBQFJy0eTy8OSZXNMZbWlxMIzFfLGAQFosZVpDxKqTjHNV6Otg0s0FGc2pMQ4Y9a3KMcFFcax6C9YSDy5B6qIWebmNzMnQ9vp1LXqJ_0_fpQU858iuOXgz7id_-_6R9wogmPK7z8VLX-IyBMBnrrzgGXlHwmCKo9CakUmYFPmry4XMjzjwnVzinvDHt8wGfqafyt-_yLJiQE8D6Gh6tqqFCcRAEpEChylaywSJF6uXLk1RDbSh-PF3g9J1x1rGTZE5-NwXFc6ACOgatnwrjL8A5WHOMTcbJfEO_SDK8h1jUTr8zawZHho1S6rrA5lXiZjkdgFTQMcb4-_7liQNtTRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حزب الحرية المعارض لايران: الذي يتخذ من إقليم كوردستان العراق مقرًا له يعلن تعرض مقره في محافظة أربيل لاستهداف بصاروخ باليستي.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/80521" target="_blank">📅 00:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80520">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=DrDYc03zm6W9QwbIJGY9sUKJdT9tFTz4vKt0C402NCQWoUu2q-OwOQR8gp5cs_s6oZsGCf6_EvbK36eukwTHUcTJzVsIDzidxehZADLtrAh5PmxDHckMTs7FppTjIf_3onpJ66mVU6XZgFQq30sf7qE1Wfk4e49S8daQa8c6uzBsyICCjJKMnGyoWBJKT4NbruNZeGUGAxo3YFdKDpBFNwe0ZmSaI7bMVrrU2skCe-0LzKWB2OjWbXkU50X9R7iA5rHCpvGNhq-xufGxG-rctFmpnNuYyxTWJsD0x6SHEeCryRl-FhXl2hoPZtbew5RtrWWwAsQ36NEcVyURR7uxeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef95cce284.mp4?token=DrDYc03zm6W9QwbIJGY9sUKJdT9tFTz4vKt0C402NCQWoUu2q-OwOQR8gp5cs_s6oZsGCf6_EvbK36eukwTHUcTJzVsIDzidxehZADLtrAh5PmxDHckMTs7FppTjIf_3onpJ66mVU6XZgFQq30sf7qE1Wfk4e49S8daQa8c6uzBsyICCjJKMnGyoWBJKT4NbruNZeGUGAxo3YFdKDpBFNwe0ZmSaI7bMVrrU2skCe-0LzKWB2OjWbXkU50X9R7iA5rHCpvGNhq-xufGxG-rctFmpnNuYyxTWJsD0x6SHEeCryRl-FhXl2hoPZtbew5RtrWWwAsQ36NEcVyURR7uxeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استهداف مقرٍّ لأحد الأحزاب المعارضة في محافظة أربيل شمالي العراق بطائرتين مسيّرتين.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/80520" target="_blank">📅 00:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80519">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=TWsNSRzFHCjMm5UQ9vS3ZfRp0GJ90gspoSGByArcuu0E9TqGO7byiIsxsFsvRrFMo_M_2ZAPLeAvPmbAh172UjMFmZurr871nA9_pgagtfjQxBvtSxfFlzJkluhHjN_2RO0VGWSx_J23ZMqsZH2ruKzeWMUSv-ue0ClsqK7qNcCOIGfgY3KBDPpfgCl30rhAjAk3OkNR8hs3GdS9RHO9HhmP_44kJllV-bL9BHaGz4M1NzTDM-8mhTdSYLc4THZ9xX2aw0-WVVZcOuUmqHd5gY5Ecb648-7GPxp5ylJjVGQqI0vwD99UZ8pnr8KAI1ZixnfMDu-t20EH8mWoCK3-ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8144f7598a.mp4?token=TWsNSRzFHCjMm5UQ9vS3ZfRp0GJ90gspoSGByArcuu0E9TqGO7byiIsxsFsvRrFMo_M_2ZAPLeAvPmbAh172UjMFmZurr871nA9_pgagtfjQxBvtSxfFlzJkluhHjN_2RO0VGWSx_J23ZMqsZH2ruKzeWMUSv-ue0ClsqK7qNcCOIGfgY3KBDPpfgCl30rhAjAk3OkNR8hs3GdS9RHO9HhmP_44kJllV-bL9BHaGz4M1NzTDM-8mhTdSYLc4THZ9xX2aw0-WVVZcOuUmqHd5gY5Ecb648-7GPxp5ylJjVGQqI0vwD99UZ8pnr8KAI1ZixnfMDu-t20EH8mWoCK3-ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/80519" target="_blank">📅 00:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80518">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGlDz0O6NqNvkCliEPitTk9aNKu3c8lKOTtx3pl9hSBndwUUZqojvlMI1m1qHzYcyJEaJVxUwLC-OgmY3xmAUA5Et7sH-E92SlZnp1VFVlAB5OBrjBhQGSdeV31163rEonnqY1PDgs0uPKKFNT-kdMNIJihOr6zqEAICBQrfLW2o709hNmoTd2noWo-qtQu7M-D7sPY2ccUO2i5nkfK_Kygo2E1dL-7YMKfQkXbMDP-x1lArxWO16IozXlWs6Qycd11irkKeBbsSKCO4g3BJnPh-YXtMG74wp6ukAaEB73I-nxQIeFTINxStVSHMzNc1Hmk6MlbjhuqSZZA1-Y_kLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
سماع دوي انفجارات في محافظة السليمانية شمالي العراق.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/80518" target="_blank">📅 00:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80517">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔻
قالبياف:
تعهدنا بمنح الوكالة الدولية للطاقة الذرية إمكانية تفتيش محطة بوشهر ومفاعل طهران البحثي.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/80517" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80515">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=AaiPsX77Rvk3HU7m_JCpEfjCXNYz3ZycE27fTBYPd8aILSDiLB8As3zB5ey44J8slgt4u-Swco3nHiLuBvn7n97lC09kxF4GFWVwWMCVi_3A0XOLLL6HXBKMRDVxghuYpCZX8P1Vxn9V55a2GpHY8o5LgHWynL5_iYIa8uZ9mpHqsMBpqCPE_9ns5UsUVJ9nTcqVvgC1x7-d-J345tYSngl3ZRKSBGWR3R0sYpxIQ4PWywx72UrJM4pQi1zexH9akhdlH9fynrQSagpjBaYg-I5r4C3BO3cBx35p8_kkDdugEPD7MubgJ0TojfXjG0r4eAuRJJ2HOMHtSd5ev5LtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbdbcef6e0.mp4?token=AaiPsX77Rvk3HU7m_JCpEfjCXNYz3ZycE27fTBYPd8aILSDiLB8As3zB5ey44J8slgt4u-Swco3nHiLuBvn7n97lC09kxF4GFWVwWMCVi_3A0XOLLL6HXBKMRDVxghuYpCZX8P1Vxn9V55a2GpHY8o5LgHWynL5_iYIa8uZ9mpHqsMBpqCPE_9ns5UsUVJ9nTcqVvgC1x7-d-J345tYSngl3ZRKSBGWR3R0sYpxIQ4PWywx72UrJM4pQi1zexH9akhdlH9fynrQSagpjBaYg-I5r4C3BO3cBx35p8_kkDdugEPD7MubgJ0TojfXjG0r4eAuRJJ2HOMHtSd5ev5LtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أرتفاع عدد قتلى الزلزال في فنزويلا إلى 2295.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/80515" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80514">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇮🇶
هيئة الحشد الشعبي تنشر:
بهذا النعش يستريح سيد زمانه، وقائد الشرف وأهله، وزعيمٌ بوزن الجبال، ورجلٌ بحجم الدنيا.
قد يخفّ الوزن الحسابي لهذا النعش، لكن أكتاف بني البشر جميعاً تعجز عن حمل قيمة صاحبه.
قوموا لله، وهبّوا مسرعين إلى استقبال السيد العظيم الذي حلّ زائراً.
هو الزائر بعد فراقٍ دام سبعاً وخمسين سنة.
ألبسوا المدن سواداً عليه وغضباً، فهذه هي الزيارة الأخيرة قبل الوداع الأخير.
ولا تدعوا هذا اليوم التاريخي يفوتكم .</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/80514" target="_blank">📅 21:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80513">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية: تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/80513" target="_blank">📅 21:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80512">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇷
الرئيس الإيراني مسعود بزشكيان:
لو أمر القائد بعدم التفاوض، لامتثلنا للأمر بالتأكيد.
الدفاع عن القوات المسلحة واجبي وسأدعمها بكل ما أوتيت من قوة.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/80512" target="_blank">📅 21:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80511">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
تقرر استخدام جزء من الـ6 مليارات دولار المجمدة لشراء سلع بناء على احتياجاتنا.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80511" target="_blank">📅 20:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80510">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">⭐️
أكسيوس:
تحاول الولايات المتحدة إقناع إيران بالتخلي عن فرض رسوم على مضيق هرمز مع استئناف محادثات الدوحة.
يشارك مفاوضون أمريكيون وإيرانيون في محادثات في الدوحة تركز بشكل أساسي على مضيق هرمز، حيث تجادل واشنطن بأن إيران ستكسب أكثر بكثير من صفقة نووية مقابل فرض رسوم على الشحن.
وقال مسؤول أمريكي: "كانت رسالة الولايات المتحدة إلى إيران هي 'فكر بشكل أكبر'، مشيرًا إلى أن رفع العقوبات بموجب اتفاق أوسع سيكون 'أكثر قيمة بـ100 مرة' من 'استخدام أسلوب العصابات في محاولة فرض رسوم'.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/80510" target="_blank">📅 20:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80509">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Wv3MsjF9m3IYbXK29YbEO4cAtmG2J8ihKZuEiBDDngyJJB0fLzvOnWpN3O0IRyvTeZ82E0pO4XDw-FJrRgVeuVEoU-TtZGTD2Yob-WEMUvV8ie7D8S51zILg85CMtxmA1B436IDm5mV4r8wSZhxsEEkwnO5Xt93bThWaUaQVInLkAgjKd2EeIhqBT1aH9aqS_yAN9B6Y8gMGpJSiWmtdM1TQHuCeZ2BvIXEoow9iQ8MrXiJKidtrYJS94OcZ_6fljFVa0B6CGK_vatVCiqstuQEz_CCcDOAMuzgFmx11sEmGJVgyjl_lUm6xuh0hEpDYUoh1hDZnYgvyFNQLsmkuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1236dd9ce6.mp4?token=Wv3MsjF9m3IYbXK29YbEO4cAtmG2J8ihKZuEiBDDngyJJB0fLzvOnWpN3O0IRyvTeZ82E0pO4XDw-FJrRgVeuVEoU-TtZGTD2Yob-WEMUvV8ie7D8S51zILg85CMtxmA1B436IDm5mV4r8wSZhxsEEkwnO5Xt93bThWaUaQVInLkAgjKd2EeIhqBT1aH9aqS_yAN9B6Y8gMGpJSiWmtdM1TQHuCeZ2BvIXEoow9iQ8MrXiJKidtrYJS94OcZ_6fljFVa0B6CGK_vatVCiqstuQEz_CCcDOAMuzgFmx11sEmGJVgyjl_lUm6xuh0hEpDYUoh1hDZnYgvyFNQLsmkuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
غارة من الطيران المسير الإسرائيلي على بلدة النبطية الفوقا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/80509" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80508">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية: في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/80508" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80507">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
القوات البحرية الأمريكية:
في الأول من يوليو/تموز، الساعة 3:30 صباحًا بتوقيت شرق الولايات المتحدة، هبط طاقم مروحية MH-60S Sea Hawk التابعة لحاملة الطائرات الأمريكية جورج إتش دبليو بوش (CVN 77) اضطراريًا في بحر العرب. ولا توجد أي مؤشرات تدل على أن الحادث ناجم عن عمل عدائي. وقد تم إنقاذ ثلاثة من أفراد الطاقم الأربعة وهم في حالة مستقرة على متن حاملة الطائرات جورج إتش دبليو بوش. وتواصل وحدات البحرية الأمريكية في المنطقة البحث عن باقي أفراد الطاقم المفقودين. ويجري التحقيق في سبب الحادث.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/80507" target="_blank">📅 20:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80506">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=SU0DYNTHPLjvoyT2_EzWXI0Pa55YW91MlQ005QbmaCjHsBmtF2oGoJLA-WbcFLJgaQ7EeFHFqyHKBE5jnBwaNZxL4879qe4uobsSgKQUkiMoRCUdVylWrR_Fczoidqac5usbRI8-4zf9xuxKfhSwsg95DxEsVeuuNKcumyNZwVR4aENdIjAxfSoxl3sPGKkmwPTUferwJIYsG-aHEhxvOUvCSprsbaQ3DIFCBIa_Dj_VS33MloyNmZNAIMHEwxqjjY7C8aHVBdc0OGouANsctw7CSRK0MhbM4NbwuXcMW9mOpxd0Kxq7v9E0LlvMSO4vMyBUbNI1fBkX7tEllxvJpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9458e9fe.mp4?token=SU0DYNTHPLjvoyT2_EzWXI0Pa55YW91MlQ005QbmaCjHsBmtF2oGoJLA-WbcFLJgaQ7EeFHFqyHKBE5jnBwaNZxL4879qe4uobsSgKQUkiMoRCUdVylWrR_Fczoidqac5usbRI8-4zf9xuxKfhSwsg95DxEsVeuuNKcumyNZwVR4aENdIjAxfSoxl3sPGKkmwPTUferwJIYsG-aHEhxvOUvCSprsbaQ3DIFCBIa_Dj_VS33MloyNmZNAIMHEwxqjjY7C8aHVBdc0OGouANsctw7CSRK0MhbM4NbwuXcMW9mOpxd0Kxq7v9E0LlvMSO4vMyBUbNI1fBkX7tEllxvJpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80506" target="_blank">📅 20:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80505">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇺🇦
ليلى عبداللطيف أوكرانيا مجدداً.. زيلينسكي:
هناك معلومات من المخابرات حول استعداد روسيا لشن هجوم جديد.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/80505" target="_blank">📅 19:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80504">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=NQIYds1htRaf4PFXDaDENK3W48PT_VeLMxIeov9reJ0J1qMXHXPuWC5h6F28OmCWpNH26sSCPBRCMRalxOXSbM8MlVlMOJJ9vROK4QKhohEcy2xwDwiSSB992-vqw2Z2kQieUlQ913wByxybjngTOPe5tnU5mtcU5ZWCoRIy3-cGzlnmN4CwlbzvFcBrrib6Z7IY_bouOtes4w8QfuRgBpEX5Yy2PHgt2MJGw44rp3QTtnUFWkw82_a95SG1rY4B8Fh0oMAYLYJYGfB-GMqwqQzqxZ6CLQXaeG_jb8tZt1wxWKNM_z9b0tcjdknuvcnJ-N-Zc85W2GvoaK08TPvlXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d17df36d2b.mp4?token=NQIYds1htRaf4PFXDaDENK3W48PT_VeLMxIeov9reJ0J1qMXHXPuWC5h6F28OmCWpNH26sSCPBRCMRalxOXSbM8MlVlMOJJ9vROK4QKhohEcy2xwDwiSSB992-vqw2Z2kQieUlQ913wByxybjngTOPe5tnU5mtcU5ZWCoRIy3-cGzlnmN4CwlbzvFcBrrib6Z7IY_bouOtes4w8QfuRgBpEX5Yy2PHgt2MJGw44rp3QTtnUFWkw82_a95SG1rY4B8Fh0oMAYLYJYGfB-GMqwqQzqxZ6CLQXaeG_jb8tZt1wxWKNM_z9b0tcjdknuvcnJ-N-Zc85W2GvoaK08TPvlXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصابات الجولاني تستكمل هدم منازل الشيعة في قرية المزرعة الشيعية وسط اعتقال وتعذيب عدد كبير من الشباب الرافضين للهدم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/80504" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80503">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🌟
نائب الرئيس الأمريكي دي فانس:
إذا حاولت إيران إعادة بناء برنامج نووي وتهديد جيرانها ودعم الإرهاب فالرئيس ترمب لديه خيارات للتعامل معها.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/80503" target="_blank">📅 19:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80502">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">⭐️
بالتزامن مع عملية إعتقال المتهمين بقضايا الفساد..
وسائل إعلام كردية:
وفد من جهاز المخابرات العراقي يصل سراً إلى إقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/80502" target="_blank">📅 19:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80501">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=SWAvGMUq27pv-VpeflD89GfR4DRG4H_RVaVpillCrbJnAKkb8J55VM63wanzoWUpAfF2PLaSLL1LAKZgn09tFDRYkQ0uUkfe-1a5UuHox-4QWmaGVQUcDCE0cknFIRQyI86mG2QelencfQ6P0TGZVWHyfILgl7-ZLxS9i8IsgiYCgH8uaus0YkSupXwbi-Rove0j52uOty6STLdWUBb_JfFobp4kd_AdjiyheUzoz0LCUceuBzGUTOSAJYcSJ4uXJywhjdGkH3cDj2Xa3HjK7adL8VIoOZ4bCkqFbdr5Jys7p67E6cVpG77ExqRXzqGmJ1U-uxFlWfX5CiNXLDuoIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d2f2f3651.mp4?token=SWAvGMUq27pv-VpeflD89GfR4DRG4H_RVaVpillCrbJnAKkb8J55VM63wanzoWUpAfF2PLaSLL1LAKZgn09tFDRYkQ0uUkfe-1a5UuHox-4QWmaGVQUcDCE0cknFIRQyI86mG2QelencfQ6P0TGZVWHyfILgl7-ZLxS9i8IsgiYCgH8uaus0YkSupXwbi-Rove0j52uOty6STLdWUBb_JfFobp4kd_AdjiyheUzoz0LCUceuBzGUTOSAJYcSJ4uXJywhjdGkH3cDj2Xa3HjK7adL8VIoOZ4bCkqFbdr5Jys7p67E6cVpG77ExqRXzqGmJ1U-uxFlWfX5CiNXLDuoIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
عمليات تمشيط وإطلاق نار كثيف من قبل جيش الإحتلال الصهيوني بإتجاه بلدة حداثا بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/80501" target="_blank">📅 19:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80500">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔻
سيُغلق مطار مهرآباد اعتبارًا من الساعة الخامسة صباحًا يوم الجمعة وستُعلق رحلات طهران بالكامل يوم الاثنين.
▫️
سيستأنف مطار مهرآباد عملياته يوم الثلاثاء بينما سيبقى مطار الإمام الخميني الدولي مغلقًا لنقل جثمان القائد الشهيد إلى العراق.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/80500" target="_blank">📅 18:57 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80499">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇷
الإعلام الإيراني:
بموجب مرسوم صادر عن سماحة قائد الثورة، السيد مجتبى الخامنئي، تم تعيين حجة الإسلام والمسلمين محسني إيجئي رئيساً للسلطة القضائية لولاية أخرى مدتها خمس سنوات.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/80499" target="_blank">📅 18:53 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
