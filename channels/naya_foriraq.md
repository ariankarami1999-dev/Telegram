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
<img src="https://cdn4.telesco.pe/file/FKHlvjEDVU9q_fLGcjHvfUGNv90uwNr6RfMxM3Q46hT6ZoQq3ofAdA_kX23C_fGzPnIaxR57Ov-Kw-vaZnNQxtr5bd92n2QNUvx6E3kG6bkPhx1mMnlXLj1zUoXJiK9fPUjr_hdqVP4WYAGI7hUokHnDZzvQGzY2lai8gijiJlwIgsXIJBu7o0kMr3jaZh1XAj4TWrgBeOy8CBAGKnXpQKxRx0N850HO5YEcjktrpkwZ9yrZh4lWRDzj1L1nFE8xR3F2f9ZHQUjwplRMlS3PZV1hn-TfeHc2FzsKJBcDc4aVou2a26ct-y5iH0PE2fzyXlER9v5vnuEahbUdgPsvZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 265K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 20:31:51</div>
<hr>

<div class="tg-post" id="msg-83634">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d684ca866.mp4?token=rGhImTzMlgzXa-poGqlBZ68LTsMbZuNZ960vB0T8sErYhsPJqJpIIlqTfdXqy9np8s_Vd9-4WZPp7XM0TnHGdJWgqqAxKKI4s-W1efpOIzU9aFNbmUctC_JFPMnBs8cL03gzQae8t99YvWhteduW2KSTz1nxNaZ0vMFSQTxBQcxV5OYtoxSmL6CW6Dm06VbmXvZM406SZx9PuztRGVNEaz-psjWToO6xtX4ol0wU-xXT7v1_RY3iuanM6fkPfV1o1iOrZFRTa2G16TAQrX9G5exkVXK4tplJzvYO6heoozyS04WmIg1uw3DjZhF-kVu5B1k12u3qqXL3B00h2Fn-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d684ca866.mp4?token=rGhImTzMlgzXa-poGqlBZ68LTsMbZuNZ960vB0T8sErYhsPJqJpIIlqTfdXqy9np8s_Vd9-4WZPp7XM0TnHGdJWgqqAxKKI4s-W1efpOIzU9aFNbmUctC_JFPMnBs8cL03gzQae8t99YvWhteduW2KSTz1nxNaZ0vMFSQTxBQcxV5OYtoxSmL6CW6Dm06VbmXvZM406SZx9PuztRGVNEaz-psjWToO6xtX4ol0wU-xXT7v1_RY3iuanM6fkPfV1o1iOrZFRTa2G16TAQrX9G5exkVXK4tplJzvYO6heoozyS04WmIg1uw3DjZhF-kVu5B1k12u3qqXL3B00h2Fn-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
تدمير موقعين داخل قاعدة الشيخ عيسى الجوية في البحرين إثر ضربتين بصاروخين إيرانيين.</div>
<div class="tg-footer">👁️ 1.88K · <a href="https://t.me/naya_foriraq/83634" target="_blank">📅 20:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83633">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1x80uOt8s9tofmnW3O5kyPWXEEQGDWQFhpN6Kvxx9Q-JEDXQE4hZRIPtfU1PFigsNx5FITL_5ors4Evo3_GlbkFUfB5zWe1H728ITgs4ciyaFOxxI0jB5D8ysByWTTNNFn8YBlvFe3iS0TZQECHRJImJIqMPOqn8J2H8OzQ6azzBY-jR_LJaor4izmiznE-CPTBEzsvFFTK9f5ZqrT-ZkkG8lnmQXwpLYbpG7bR7-wC1rp0ee4MmiwZe_TVlkYHWmyFNJIajHaqJAU8M3Wq-1Il7XSMpjdpFcvuuantVZ1ONV1IDMsAKwXWkzQYyqXcaqXX93ZdGvnun33q-dDcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في بغداد تشيد بزيارة الزيدي ولقائه في هيوستن شركات الطاقة لتحقيق هيمنة امريكا في مجال الطاقة</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/naya_foriraq/83633" target="_blank">📅 20:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83632">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6cbb7713.mp4?token=RSvesRsSK33rOIoi2OXt3sLh6dQ-bbwNKpuLWmyYuDDvshJ4JTOIPahN2LkDZBmmzCASK8imF8Vc5th8NcuRWnJ-s5aosCMdSw3Dy2ZTPznm9TZIpIOC0WxQzsX6-IaXy7Zv5OCz7C05rJLz8x3VV3N4HVomoUyy5_w9M4SrkICs34nTAXbr1BAbYf6_V-yIkJ3-iGVqKuzE4XpB8LLWS9_rnPWkgJW0QTKcQknrd9HjUdrl_XlTvq4Vwu3U2fSslL65zEgRv029JTBJmLhi9DhPy4vkg0wgSI_5Ql_b_atO0dhct3ECaaYdn3C8Vj0eiFkNxPG6VcQe84BNYO2MFmTMY5llTT8TPv_A7i0GeXz2y0wamefb2aiInPhbCK6fVEqifMSjljg3XJoc_FBdbUhr5MNCgRa9_6hQ1EDEzZr8gbt7CzkDSv0erm54adjHY_34fSWpeoNmi5tp4gDf2HRpOkaK6s-qPAc3JJMh-8QTkEgjdGBLAD5AMYVHCRQcowfEDJKmvKx65WrKaOSKKddL341GSeptn50maPxZRyup_JKykovLsopc-kAh7cai-DWdNlNQPWRcQGssbc2Mo7tssYDfRm7NlmOyvQOPkENqvjKcHCrFAP7o-UCruNbH15RlAlm9LyLYFUrG0XHYZ-0gGqyQGdc60Rw-rMGoAeU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6cbb7713.mp4?token=RSvesRsSK33rOIoi2OXt3sLh6dQ-bbwNKpuLWmyYuDDvshJ4JTOIPahN2LkDZBmmzCASK8imF8Vc5th8NcuRWnJ-s5aosCMdSw3Dy2ZTPznm9TZIpIOC0WxQzsX6-IaXy7Zv5OCz7C05rJLz8x3VV3N4HVomoUyy5_w9M4SrkICs34nTAXbr1BAbYf6_V-yIkJ3-iGVqKuzE4XpB8LLWS9_rnPWkgJW0QTKcQknrd9HjUdrl_XlTvq4Vwu3U2fSslL65zEgRv029JTBJmLhi9DhPy4vkg0wgSI_5Ql_b_atO0dhct3ECaaYdn3C8Vj0eiFkNxPG6VcQe84BNYO2MFmTMY5llTT8TPv_A7i0GeXz2y0wamefb2aiInPhbCK6fVEqifMSjljg3XJoc_FBdbUhr5MNCgRa9_6hQ1EDEzZr8gbt7CzkDSv0erm54adjHY_34fSWpeoNmi5tp4gDf2HRpOkaK6s-qPAc3JJMh-8QTkEgjdGBLAD5AMYVHCRQcowfEDJKmvKx65WrKaOSKKddL341GSeptn50maPxZRyup_JKykovLsopc-kAh7cai-DWdNlNQPWRcQGssbc2Mo7tssYDfRm7NlmOyvQOPkENqvjKcHCrFAP7o-UCruNbH15RlAlm9LyLYFUrG0XHYZ-0gGqyQGdc60Rw-rMGoAeU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
لجأت السلطات في محافظة البصرة جنوبي العراق إلى بذور هولندية هجينة لزراعة حزام أخضر على طول الحافة الشمالية الغربية للمدينة النفطية العراقية، سعياً منها لتلطيف حرارتها.</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/naya_foriraq/83632" target="_blank">📅 20:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83631">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/163aae010f.mp4?token=c-s_anDeHIlkyCXRMH2f41gRixXYqwbki0Qrrm7j2-w--jujJz8fFiNUR5ccViyvG8NkWYN8efpWmad_0YhNBhtoA7Gjkc53wRUhE26LIFmChj68D7HUuPKS3u_ahRZo1tVb6pyXIpOC9k010Ifrxwj37dpasKig4ozPiDZIDkbEmYBzL-guQuW-8TZ_NXiGu3OA10miFAVqBco_JDp5NG8AAJyctsUYP5wN2L3Bo9qDU9umUBUkRKxRGXJkMlduhRRalkODR1VXhdBWRRFrdgXvmSDX0zkM0ChnRP3Vx-KEs0zzJmb8LIWchzmUcSIM5rf8W_L_jrt-6yvFJlUptw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/163aae010f.mp4?token=c-s_anDeHIlkyCXRMH2f41gRixXYqwbki0Qrrm7j2-w--jujJz8fFiNUR5ccViyvG8NkWYN8efpWmad_0YhNBhtoA7Gjkc53wRUhE26LIFmChj68D7HUuPKS3u_ahRZo1tVb6pyXIpOC9k010Ifrxwj37dpasKig4ozPiDZIDkbEmYBzL-guQuW-8TZ_NXiGu3OA10miFAVqBco_JDp5NG8AAJyctsUYP5wN2L3Bo9qDU9umUBUkRKxRGXJkMlduhRRalkODR1VXhdBWRRFrdgXvmSDX0zkM0ChnRP3Vx-KEs0zzJmb8LIWchzmUcSIM5rf8W_L_jrt-6yvFJlUptw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
انخفضت حركة الملاحة في مضيق هرمز إلى 8 عمليات عبور في 16 يوليو، وهو أدنى مستوى خلال ثلاثة أسابيع، مع تركّز معظم العبور عبر المسار الإيراني واستمرار تراجع النشاط الملاحي.</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/naya_foriraq/83631" target="_blank">📅 20:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83630">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇺🇸
🇮🇱
🇮🇷
الولايات المتحدة تُبلغ إسرائيل بأنها سترسل عشرات الطائرات الإضافية للتزود بالوقود إلى البلاد، وذلك في إطار استعدادات محتملة لتوسيع العمليات العسكرية ضد إيران.</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/naya_foriraq/83630" target="_blank">📅 19:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83629">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c172eb3bd0.mp4?token=YPnmcDOF91vSz7k5_pox7Y10ubwpsCcQ4C2oGRhZcbRzPefyZiVDYUCjOxu3E6lywtQTK1icfmGgzeGFP2vnrAfJVOgQQzxEurxC_DBHzKzw98-Yb0ABJg3B2bW8Wf23bSga2J2C8UKSNPH3hMdHvHtPZXBZetPPW-DQrCFmO-5BYZr9I2MevEohQRDC2FDdxi7bNHl6TbH5o0Bv93ZQ4mV5xoKlNILtlUAaKS31JfPuB7565Fd-WtsihPpMkeg7sv-qirast6B10GTWrJv_7-YUjdrjrA0Cnt_-ivonblomBfbE87m31dNJN4ljMy42chCkUvs_iTa8Wcht7XC49g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c172eb3bd0.mp4?token=YPnmcDOF91vSz7k5_pox7Y10ubwpsCcQ4C2oGRhZcbRzPefyZiVDYUCjOxu3E6lywtQTK1icfmGgzeGFP2vnrAfJVOgQQzxEurxC_DBHzKzw98-Yb0ABJg3B2bW8Wf23bSga2J2C8UKSNPH3hMdHvHtPZXBZetPPW-DQrCFmO-5BYZr9I2MevEohQRDC2FDdxi7bNHl6TbH5o0Bv93ZQ4mV5xoKlNILtlUAaKS31JfPuB7565Fd-WtsihPpMkeg7sv-qirast6B10GTWrJv_7-YUjdrjrA0Cnt_-ivonblomBfbE87m31dNJN4ljMy42chCkUvs_iTa8Wcht7XC49g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تُظهر صور الأقمار الصناعية مزيدًا من الدمار الذي لحق بمستودع في ميناء عبد الله بالكويت، في أعقاب غارات سابقة شنتها طائرات إيرانية بدون طيار. واكدت إيران أن المنشأة المستهدفة تابعة لشركة كي جي إل للخدمات اللوجستية.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83629" target="_blank">📅 19:25 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83628">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔻
مصدر بالحرس الثوري لنايا
نفّذ عناصر اللواء 65 للقوات الخاصة المحمولة جوًا في جيش الجمهورية الإسلامية الإيرانية، خلال الحرب التي استمرت أربعين يومًا، 11 عمليةً خارج الحدود في إقليم كردستان، أسفرت عن تحييد 8 من القادة العملياتيين للجماعات الكردية الانفصالية، إضافةً إلى تدمير ثلاثة معسكرات ومقرات عملياتية تابعة لها.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83628" target="_blank">📅 19:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83627">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5552eed251.mp4?token=f2lDDzEja_HblsuErc2W8xA-7YSjRQiifVvf5LwwOeeL7wRRAlaFKrZLNdfPp0Izli6SjHt556rfEX85Hdb9bcnkqcHa6kC5eUCxNTJVuxsJCEV3PMqQMI4GdfjpNObFFm7_rF3W-4PQ0yqVIlNhtznYDn86Jzm-VSPtLC3MCPitSN7RF4Dq_jpAdnc_z_gaDw7QKwg_F2_TgFqVdYKnJG6uSCpOhqy3dkq-eaWroQtHCmMhZFT0bii7c42_VJL7pR7U0szoH36OGE9D8rmy_x096yZFm-FqPXXuLQMsm3D36Hs69V_jCrlSJC5rL9xJ0LGyp_JeBoTUSju2NtBGcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5552eed251.mp4?token=f2lDDzEja_HblsuErc2W8xA-7YSjRQiifVvf5LwwOeeL7wRRAlaFKrZLNdfPp0Izli6SjHt556rfEX85Hdb9bcnkqcHa6kC5eUCxNTJVuxsJCEV3PMqQMI4GdfjpNObFFm7_rF3W-4PQ0yqVIlNhtznYDn86Jzm-VSPtLC3MCPitSN7RF4Dq_jpAdnc_z_gaDw7QKwg_F2_TgFqVdYKnJG6uSCpOhqy3dkq-eaWroQtHCmMhZFT0bii7c42_VJL7pR7U0szoH36OGE9D8rmy_x096yZFm-FqPXXuLQMsm3D36Hs69V_jCrlSJC5rL9xJ0LGyp_JeBoTUSju2NtBGcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
الخارجية القطرية:
دولة قطر تحتفظ بحقها الكامل في الرد على اعتداءات إيران وفقا لأحكام القانون الدولي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83627" target="_blank">📅 19:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83626">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3kPp1eRM2vPiA17m6x7W5SxB5EtX2ogqIRzNDWBPDHEwt670KU_42-BcHjnLY5CuJA89wTet_VBfvdVkfPOt5AtAIIOLQTaFhk63--7eARgiTyvaAqyuk6IIRikWNAFfelcrc42NOflOirzjK6Ry-5qDJfJdzJypHB6Qyx0RUKRb_9gud4rishQAkQrKucUXftc01xS3qiU_ziF-cgQPqBdp5CTB19g3BAoeJpcZbSLd0ZRbELqGsCZW7gU9-diny4Q6V24jCiTEKx_MXsLPEHzmGVIoDW2rxHOCP8kgDc4EZK4USeR-UIFoMwzwOpTfMw-NI3APwfWExabhhXifQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الكويت تبدأ حملة ترشيد الكهرباء بسبب الضربات الصاروخية الإيرانية الأخيرة ..</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/83626" target="_blank">📅 19:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83625">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">زلزال بقوة 7.4 درجة يضرب منطقة 71 كيلومترًا غرب غرب بويرتو ماديرو بالمكسيك</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83625" target="_blank">📅 18:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83624">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇺🇸
‏
القيادة المركزية الأمريكية تزعم:
تدمير برج المراقبة بميناء شهيد كلانتري في تشاه بهار، وهو جزء من شبكة مراقبة بحرية على طول ساحل خليج عُمان.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83624" target="_blank">📅 18:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83623">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">العراق يطالب سوريا بتسليمه السائق الذي اعتقلته عصابات الجولاني بتهمة التهريب</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83623" target="_blank">📅 17:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83622">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شركة "كونوكو فيليبس" الأمريكية تستحوذ على 42% من حصة شركة "بي بي" البريطانية في اربعة حقول نفطية عراقية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83622" target="_blank">📅 17:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83621">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">شركة سي بي سي:
ناقلة النفط المستأجرة نورديك زينيث تعرضت لهجوم أثناء اقترابها من محطة سي بي سي في البحر الأسود.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83621" target="_blank">📅 16:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83620">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826f62ba3a.mp4?token=cX0jAg2kR1kP0IE72fLfMwKEtjRtc5CJmgOpdevrCEAyNuJjSoRDD3Ol-pot7jtKAfwUSX1rWmXbgWrwjo3EECUhW39is5RwE9e8zgQd0VYvsbCh0oQEBHU_Lx_J4WVqVHXweezyrB36bKQWNZzhTxwLwU0YrsT3UXFTsWVBUBI_iQFzhZIweaawVxa-BnhTtTMgjFhZ8Y42XqcHatPZlY1d5mTTV78OEkQDuwEYQdh4NLJ_pXb1U9i2W74tlOp5zK6WEbwjH8pK5q6k3W0PYg1W26SQ0gxM9UwMwp0rNvtfFChwWSc23dfcM3l-zLFTNksTqJQlF8XiwQclmi1__Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826f62ba3a.mp4?token=cX0jAg2kR1kP0IE72fLfMwKEtjRtc5CJmgOpdevrCEAyNuJjSoRDD3Ol-pot7jtKAfwUSX1rWmXbgWrwjo3EECUhW39is5RwE9e8zgQd0VYvsbCh0oQEBHU_Lx_J4WVqVHXweezyrB36bKQWNZzhTxwLwU0YrsT3UXFTsWVBUBI_iQFzhZIweaawVxa-BnhTtTMgjFhZ8Y42XqcHatPZlY1d5mTTV78OEkQDuwEYQdh4NLJ_pXb1U9i2W74tlOp5zK6WEbwjH8pK5q6k3W0PYg1W26SQ0gxM9UwMwp0rNvtfFChwWSc23dfcM3l-zLFTNksTqJQlF8XiwQclmi1__Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
مشاهد من الاقمار الصناعية تظهر اخلاء قاعدة العديد الجوية في قطر من الطائرات الامريكية بسبب التهديد بضربات صاروخية إيرانية ومن المرجح أن تتفرق الطائرات إلى قواعد في إسرائيل والسعودية.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/83620" target="_blank">📅 16:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83619">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8c4cf5444.mp4?token=eumzvn5MEMrcNkqC6OZ5klOrfprhccchkSszNKFqnVKqwU1OQU6K0gdfRrI2HFjmz-VNNSfksyv0PicV-32_VYGrr6uBm14c2vLG3q4ap8oYM2csJO_mQ0D4T-aNYy95lxZjcHqbZZ_GsL8xS0e9oOBJthPsn9deMPp9eqei8VNwYnx-_sbdaQXc6c7d_0WWTMzKgE4zZGgG3P1mk3C1XOOIHZstO6uRM7SZFXgQ_ZLWFrVscITjTAQoAJ7gKGedgsE0dw9NrmkhlbeV38MolwNeaLLJRSrtx2_gsaPZaHN0aQOpELJRVqjSvfXpwRBjtX__B1jkcszb9eXBqFP4ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8c4cf5444.mp4?token=eumzvn5MEMrcNkqC6OZ5klOrfprhccchkSszNKFqnVKqwU1OQU6K0gdfRrI2HFjmz-VNNSfksyv0PicV-32_VYGrr6uBm14c2vLG3q4ap8oYM2csJO_mQ0D4T-aNYy95lxZjcHqbZZ_GsL8xS0e9oOBJthPsn9deMPp9eqei8VNwYnx-_sbdaQXc6c7d_0WWTMzKgE4zZGgG3P1mk3C1XOOIHZstO6uRM7SZFXgQ_ZLWFrVscITjTAQoAJ7gKGedgsE0dw9NrmkhlbeV38MolwNeaLLJRSrtx2_gsaPZaHN0aQOpELJRVqjSvfXpwRBjtX__B1jkcszb9eXBqFP4ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83619" target="_blank">📅 16:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83618">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">انفجارات تهز محافظة اربيل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83618" target="_blank">📅 16:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83617">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OoML3In7n7mPIiqzvP_H50HU8-yxKHQhzkZnQNy6XDddfqzyM1R7OdSUpzZeC3JTrpqhlcFe8NLBvNWIzoZz9osoedNs0udDGT-17AOa3rS0iG5W_zLzUeRv6MJHduaJoUuIvdrr0Wtd3ez3ILT1LhcxJQz-2qqd_a3PSI2eiwWzQy2gVJ1AUWgyl8xohcBKPNOMC8u1wlP8CAI-XvbUmBJD0D8vx7LJPGKxnx0VVCuyqhkpySqSZOWkya9cJyEGrRUwho7jf5errkdKuiVUqFSXrHJ2FVeljdnuooPNpLIZzEUyj7VVWTMefAC6-eO3lpq_zRQMQPVrozYMeSkXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛐
سماحة المرجع السيد علي السيستاني يجيز للشيخ محمود الفياض نجل المرجع الراحل محمد إسحاق الفياض، إدارة الشؤون الحوزوية في أفغانستان، وتولي رعاية مؤسسات والده في افغانستان.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83617" target="_blank">📅 16:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83616">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">غلق مضيق باب المندب؟!   والمثل العراقي يقول " ام حسين ما رضينا بواحد صاروا اثنين" بعد غلق مضيق هرمز الإيراني الان باب المندب وميناء ينبع هو الاخر سيكون أيضا هدف نحن لا نتحدث عن شلل في مصادر الطاقة نحن نتحدث عن توقف تام  EU this, winter are to cold</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83616" target="_blank">📅 16:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف: الزملاء الأميركيون يدعون إلى استئناف حرية الملاحة لكن هذه الحرية كانت قائمة بالفعل قبل بدء العدوان على إيران</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/83615" target="_blank">📅 16:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇷🇺
وزير الخارجية الروسي لافروف:
الزملاء الأميركيون يدعون إلى استئناف حرية الملاحة لكن هذه الحرية كانت قائمة بالفعل قبل بدء العدوان على إيران</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/83614" target="_blank">📅 16:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8aaed9139.mp4?token=Q_aVnbz7CvjKqUDBL30VVs11YGpf3jUYitGLScXsoMAs7NxgqQstbaGLg9MIpCgQShaVAJ4rEuMpXfB8y3qbR2rUHDLGB6oY5QDfwgzy6YlK6JGxUVr8Gngl6zfOt5CeYRuRVNz_dnvs_w7MFloiprMPcJkmIAT9j2MRFff8BzDP0-svDT8pJdsbyhAJwTH2wM64-L-nK938x8GduxVvTgtMBxgfDYU2VoABsxZk_yyWHuQ-5pOCktRz2jMNey4dgepXtf0SmTrkLKQv-z_TBURU0wTZG7mq7G_nYcWn8X45MnLcBYuaed7IA-QZB_ZcPYwk5SmoRcPm-6nawtGICg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8aaed9139.mp4?token=Q_aVnbz7CvjKqUDBL30VVs11YGpf3jUYitGLScXsoMAs7NxgqQstbaGLg9MIpCgQShaVAJ4rEuMpXfB8y3qbR2rUHDLGB6oY5QDfwgzy6YlK6JGxUVr8Gngl6zfOt5CeYRuRVNz_dnvs_w7MFloiprMPcJkmIAT9j2MRFff8BzDP0-svDT8pJdsbyhAJwTH2wM64-L-nK938x8GduxVvTgtMBxgfDYU2VoABsxZk_yyWHuQ-5pOCktRz2jMNey4dgepXtf0SmTrkLKQv-z_TBURU0wTZG7mq7G_nYcWn8X45MnLcBYuaed7IA-QZB_ZcPYwk5SmoRcPm-6nawtGICg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">أنا احب قطر بس….</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83613" target="_blank">📅 16:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb30544783.mp4?token=iAEXWfcw-VQEmaH-xazLVDZtJxbCNjlswJu43IddP6EAcNlJuxWpsbHuR-RNr_Tt0rJq_XlpZs1PaqK2fy2llcHc-oQh6cmSnF2bhl2T_ncvdnMigVM4sFH53zKAYE-lNtdn841kLZc3vcUVqjYY12AQMMDfy6fo4Gl3kgOlo3s7mGXGFkkEnH5udtBBQwfZ2LUxB6KunOyWOX6I-NhX4JlS5FCPHuJ1xIFxamOwWt1OFvQPd3jkc2teIj7L612GnugvYDbjChhaAoan0emUdxJ4VuuRxYku4q20DjnAxyaBqP5IWftDgfxgEBQy5pdAuMP89Zr3e6tacrkdNT6kcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb30544783.mp4?token=iAEXWfcw-VQEmaH-xazLVDZtJxbCNjlswJu43IddP6EAcNlJuxWpsbHuR-RNr_Tt0rJq_XlpZs1PaqK2fy2llcHc-oQh6cmSnF2bhl2T_ncvdnMigVM4sFH53zKAYE-lNtdn841kLZc3vcUVqjYY12AQMMDfy6fo4Gl3kgOlo3s7mGXGFkkEnH5udtBBQwfZ2LUxB6KunOyWOX6I-NhX4JlS5FCPHuJ1xIFxamOwWt1OFvQPd3jkc2teIj7L612GnugvYDbjChhaAoan0emUdxJ4VuuRxYku4q20DjnAxyaBqP5IWftDgfxgEBQy5pdAuMP89Zr3e6tacrkdNT6kcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الاقمار الصناعية ترصد أضرار جديدة ناجمة عن الضربات الإيرانية الأخيرة في مقر قيادة الأسطول الخامس للبحرية الأمريكية في البحرين. ‏تُظهر الصور أن هوائيًا من المحتمل أنه كان يستخدم كمحطة اتصالات، قد تعرض للضرب خلال الهجمات الأخيرة</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83612" target="_blank">📅 16:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVOfjUoQSIsq74W3IYftI9HKUwzVFyrk5ejRadnRzZwad_0gQEfcB4ilni1Qun_Y_XUmaHlfGGg2YUHlmAdos-S4Xmu0pVzdzjIY4AfPo_4G4B6dyOQUzXWpw1vjSOb8Z_DKseJtri8g5mbskeY--1_HskF6N2hW1Oq1oRdRg8btuk304FjJzqlDBS15YN73NVhp6PPZk8Z5FWJ14aBVNMmZjYG6BBo64t4vZtgODgGZKU7fCwiKXn8KogdwR3aiWJ3s-PUPr_lGzSGNR3hvOYm2qKazjY5iBt8deRWxSHTAa8J2rQwbEs6JkLnKqCVQhMZEDaZow-woDRNH7zyK-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
صور الأقمار الصناعية تظهر أن مستودعًا لوجستيًا تابعًا لشركة هاليبرتون الأمريكية لخدمات حقول النفط في منطقة ميناء عبد الله الصناعية بالكويت قد دُمر بالكامل واشتعلت فيه النيران بعد أن تعرض لهجوم في وقت سابق من اليوم بواسطة طائرات مسيرة إيرانية</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83611" target="_blank">📅 16:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb38a92c43.mp4?token=vurnN4nlQY6VhLwQFkw3jccRGLZzaIuG_3UwcA0m5xYHfLwIB3ifpx4SDLmtA_D7pc5BavxbWyV14v3AOnoMExPtjYBYH92Kj-6biTG1C52NpvuC1au4Y2y1KakbvxTM0uWjexDLaaSViYBunrVIzlNuNaNU127N9Wa3h85EkBP9gMj8xXKHgsbcVrwDX-lz1yBEiXmQchpRDqKDB_dLfCTNXFEbAgYrT95OdZSM-3Qu4EPn3EfJj_uLKOgiInZNsq6IT73kYAv8PB5eGUQaYBHtTPLskwWcUw3jupJqdd8cooSNBVzk81m4Ddy7xPDOQlUQaPQiuLYDwYIj94Bohg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb38a92c43.mp4?token=vurnN4nlQY6VhLwQFkw3jccRGLZzaIuG_3UwcA0m5xYHfLwIB3ifpx4SDLmtA_D7pc5BavxbWyV14v3AOnoMExPtjYBYH92Kj-6biTG1C52NpvuC1au4Y2y1KakbvxTM0uWjexDLaaSViYBunrVIzlNuNaNU127N9Wa3h85EkBP9gMj8xXKHgsbcVrwDX-lz1yBEiXmQchpRDqKDB_dLfCTNXFEbAgYrT95OdZSM-3Qu4EPn3EfJj_uLKOgiInZNsq6IT73kYAv8PB5eGUQaYBHtTPLskwWcUw3jupJqdd8cooSNBVzk81m4Ddy7xPDOQlUQaPQiuLYDwYIj94Bohg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
صور الأقمار الصناعية تظهر أن مستودعًا لوجستيًا تابعًا لشركة هاليبرتون الأمريكية لخدمات حقول النفط في منطقة ميناء عبد الله الصناعية بالكويت قد دُمر بالكامل واشتعلت فيه النيران بعد أن تعرض لهجوم في وقت سابق من اليوم بواسطة طائرات مسيرة إيرانية</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/83610" target="_blank">📅 15:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cq-bPeR3vimVpXK9QPVj5u2pCSul1jAQsS7VlEsklReFkW6Q_b06OJYdh7LsZtrRh1wG_BTK4f4UI9p5m9sQSmeQw1LJhWRmrXCmMVhwhI_S_eRs0K61k3hKyAH2jORjlwQi65AAqaJoNYGcGDZQYWASiIlFKX8OIyRNrX1sCkks4OZJU6eX3TqeprngA0prz1G_-lNYK3W6Z458qrz7GIg24HpWaynoHd1eSwss-1gdad2Px8PSiD6z54OrI-Uc933xnNJm-kTol7AgvQI7ZpY0vxSBp1hR-yppX97DFxb8bkgwU_KUZA9UaK9azIqvL9MAw6NZY5AdzQC6WqASLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
السيد مجيد موسوي
قائد القوات الجوفضائية التابعة لحرس الثورة الإسلامية:
في نظامنا الحسابي، الأرض هي الأرض، وطهران والجنوب جزء واحد لإيران. عملياتنا الفعالة والموجهة من جميع أنحاء إيران ستستمر في استهداف العدو حتى عودة الهدوء إلى الساحل الجنوبي ومضيق هرمز.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83609" target="_blank">📅 15:40 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">انفجارات تهز سليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83608" target="_blank">📅 15:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انفجارات تهز سليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83607" target="_blank">📅 15:27 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLRT5ywRYepD39uDtiLOkHVFem5lrhlI_2BaNDif9k9v_ue1bW_VvtExY1Z82xnsZ5_3DyiUwj4sgQm5Yff4eRH9F8_OgZE-uXIFLZOEgn9BpzzaFVh_8UrYjpCSfpeuLy1EEHHdC5vecgw0hbxlbtp2knjOx1UuiEzGGAT_VX7N9Z4OvANwogtSBTxGiXP81l2_COQOriAOKrmhUT_o0k2Px8p5Aj8hpotRbLHTygYOFd3IP-Yr5wn5RtP7QWbiwc5SajnTZGyzS_Qx0JZtrO_coqkdbl7X_K2woQY2azh42HaHg5v_qlNjabdF2E3QwYFbqIhvmSBOxY99M4d-SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتعال النيران في منصة إطلاق صواريخ هيمارس امريكية عقب هجمات ايرانية يوم امس على الحدود الكويتية العراقية</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/83606" target="_blank">📅 15:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQm_UPaOYEO-PpByOEW_PKQVs3IcoujtU4j_zrsu5GpL3zaKQqjTNZip76utEm07OabvfWE032DUBPJJ2b2t52juGMJSKCFA-v7lwmeDnASgXWs-j3YNyOWk6AmI_cjkMlTEnz_wd3o-SmRrPNqiYWf6mHLXHE9yG1kX-dKsHKDn5gIfm8T6fMxbuQAS3T06qdU28f2eaONLPUY6XvJZUxZIJpOb5vDZ-RsaxDQZFb7LLB6-VmyOiXGff8UFZP3UFInil428O0votHfckiAvCovMNwNMOHl5VDHrf54mkiatH4XaWq1iEo82a1VoPWO_ExBpEBkuDquZcS8Wn6eiAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئاسة أركان ما يسمى الجيش الكويتي تزور عدد من الجنود الجرحى بسبب تعرضهم لإصابات اليوم نتيجة الهجمات الإيرانية</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/83605" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇬🇧
حزب العمال البريطاني:
فوز آندي بيرنام بزعامة الحزب بالتزكية خلفاً لكير ستارمر.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/83604" target="_blank">📅 14:58 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">طيران حربي مجهول يحلق على ارتفاع منخفض فوق قضاء سوران في محافظة اربيل</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/naya_foriraq/83603" target="_blank">📅 14:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">مهاجمة سفينة في ميناء الدقم قبالة عمان</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/83602" target="_blank">📅 14:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83601">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/naya_foriraq/83601" target="_blank">📅 14:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83600">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اقليم كردستان:
بسبب توقف حقل كورمور انخفضت كمية الكهرباء المنتجة بمقدار 2500 ميغاواط.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/83600" target="_blank">📅 14:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83599">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">العلاقات العامة للحرس الثوري الإسلامي:
بسم الله قاصم الجبارين
﴿وقاتلوهم حتى لا تكون فتنة﴾
استكمالًا لعملية الرد بالمثل التي نفذها الليلة الماضية مقاتلو القوة الجوفضائية التابعة لحرس الثورة الإسلامية، وفي الموجة الخامسة عشرة من عملية «نصر 2»، وبالرمز المبارك «يا أبا صالح المهدي أدركني»، وإهداءً إلى شهداء الجرائم الأمريكية الأخيرة المظلومين، وبهدف تأديب المعتدي ومعاقبة الجيش الأمريكي قاتل الأطفال، نُفِّذ هجومٌ عنيف ومباغت على القاعدة الجوية الأمريكية في العديد بقطر، جرى خلاله تدمير منظومة رادار بعيدة المدى وعدة طائرات أمريكية استراتيجية للتزوّد بالوقود بشكل كامل، كما تعرضت عدة طائرات أخرى لأضرار جسيمة.
ليعلم العدو الأمريكي ومستضيفو قواعده في المنطقة أن تجاوز الخطوط الحمراء والاعتداء على المدنيين والبنى التحتية غير المدنية ستكون له كلفة باهظة ومُفجعة، وفي حال استمرار هذا النهج من قبل العدو، فإن ردودًا أشد تدميرًا في الطريق؛ ردودًا ستبقى خالدة في تاريخ المعارك.
(وما النصر إلا من عند الله العزيز الحكيم)</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/83599" target="_blank">📅 13:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83598">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇺🇸
🇮🇶
السفارة الأمريكية في العراق :
ويُنصح المواطنون الأمريكيون بما يلي ، لا تسافروا إلى العراق بسبب الإرهاب، والاختطاف، والنزاع المسلح، والاضطرابات المدنية، ومحدودية قدرة الحكومة الأمريكية على تقديم الخدمات الطارئة لمواطنيها داخل العراق. ولا يُنصح بالسفر إلى العراق لأي سبب كان</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/83598" target="_blank">📅 13:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الله اكبر   احتجاز السفينة من قبل أنصار الله</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/83597" target="_blank">📅 12:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/naya_foriraq/83596" target="_blank">📅 12:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">أنصار الله يهاجمون سفينة في باب المندب منطقة المكلا</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/naya_foriraq/83595" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83594">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/naya_foriraq/83594" target="_blank">📅 12:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83593">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خون ریختن خون بریزید خون در برابر خون پل در برابر پل برق دربرابر برق برج در برابر برج</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/naya_foriraq/83593" target="_blank">📅 12:29 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83592">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce814b2d1f.mp4?token=tlVe4KLa3ciCwVZAyTvCwW4uqLUkhXM8oTIfId10JQNoslf5_VtiDrDqN8HaHwYurIkCZ69GP9VjzoTyNZk6scwfRAqk7kimlRl-XliN2MZCE_SsaOXvbnHLdNrz0fc4DnND33_yvZU1gJ6j28jNZIkJy4ZB6bel9VqgYxMPRAzrtTpOsCkhiFvWhOzo74Ucp0DhfBnViRcaEg_34GS6CsG_Nhppdudp8v-qgnP2pWdzqjkPr3fIKuLPhd3TEfQCdC1juUlTkHW3ctNvIPOeORc6UQbDNxocJECRGcOVgGh4kRCSXv3RDRCsG0BLw8IDsCyGr-K8U9570dpi3NSjkLDcai2A49igrXSofe9HwF0iXdRAKexdccbxhGNfHVUIfUCHTlMDE5wUh3qk1W9KiUR2vBXVa5f-S_jjnpRf97i46OBA6lK5Uu7HDBdXUoT5hMh634mPM6oeW1thJwulfqaUxVGGVbRK3MYF3zLVBVqvk8-XeR6pAFJyqa-XnQknIfbBPPylCLU5qYRTf9_UJlZtZJKlRC-xH9zhhqo-mTamwTZo6WKjmkNf28iKAFVNWJXsW_r6IAt7DJ-nxSYc3UjxOg6BWtU3U8Hh1eUjGmrupxJS9zGufKzfRYsj7y6Uhp0u-Hg4tFz7E9RaM3gs6rN04W4KfmGCJCXjugR4rVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇪
🇺🇸
🚀
صور الأقمار الصناعية تكذب وزارة الدفاع الاماراتية
صور جديدة تظهر احتراق ثلاثة مباني بقاعدة زايد العسكرية ، علما ان الدفاع الاماراتية قالت حريق خشب
😆</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/naya_foriraq/83592" target="_blank">📅 12:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83591">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEMn5baYAsrhiw8zPftexTB3jf7XGvBcdm3O9ayLVTCkWOt7vQat5t2htN0Qe7exDMtqreln7yw0BSwlK5mtgQwJvIAjun67OMXN8kaHJKtfuX5fGh1cM9QS14HGcrNWQsTQJW0QIZ6gASuHvyEVD__xXIiuiujLOTnWEZkfoH4oI4lt-YEAIWPIVQ7F0PTx14dpYyvKcuaVZXpAnFLSIONZdMC4-8N2kKLUMT1ssFKF1zyCCpqTUtCJDm1J56cswWgTuQ8vdz19VfR-x_yI7IJdYpORq8ALmv66Zw5nlDG_E6LmSMPRCx74Gmcur0ADq6rEpfoEx8NoCbakuXWS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
🔻
مسؤول في حزب الكومله الإيراني الارهابي : تم إطلاق ستة صواريخ على مقرنا، أصاب ثلاثة منها مكاناً قُتل فيه ثمانية من البيشمركة، وسقطت الصواريخ الثلاثة الأخرى بالقرب من نفس المكان.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83591" target="_blank">📅 12:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83590">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d374976c66.mp4?token=aR9ndIZ9uj9_YcTKKSD7iZbffoT0scVxPxBJWROrLiJYn4y6kHN7NQMLxBe48w177JY_01ycwJPSJm9gBlaBsnXS_GbMgcmEB97ZuT10qPv8tNW_QFjptx3N-dyZg9uNKL8g0M1x0cWh3IqjfSkWJmPquyW3F-yhK4526nc-QMyJ7Mi3hNPFRqpXUpLzCpwg3j7pherW1OGMFbw18u2K9eMm7n3Vzl1rEvYhUuBgDXXE0JqQoCoKJ5Fg9dSdK8dpsRcYWbv10jzC9lvp6-_36iJLbEKSM_jP9sfxr3uKns-BaJwmu8xhJrNR9dTDg4URdI9GZ-iTwbtR_B2TD7QPQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
US ready for airborne operations inside Iran</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83590" target="_blank">📅 12:01 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83589">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
في إطار استمرار عمليات "المعاملة بالمثل" وردًا على الجرائم الحربية التي ارتكبت الليلة الماضية، قام مقاتلو القوات البرية التابعة لحرس الثورة الإسلامية، في الموجة الخامسة عشرة من عملية "النصر 2"، تحت شعار "يا مهدي، أدركني"، بالإضافة إلى تدمير منصة صواريخ "هيمارس" في الكويت، بتدمير عدة مواقع لقوات أمريكية ومعارضة مرتزقة لأمريكا وإسرائيل، من خلال عملية جوية وصاروخية، وقاموا بقتل عدد كبير من المعارضين والقوات الخاصة الأمريكية. وتستمر عمليات "المعاملة بالمثل".</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/83589" target="_blank">📅 11:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83588">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/naya_foriraq/83588" target="_blank">📅 10:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83587">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/83587" target="_blank">📅 10:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83586">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkwsMZ_WqTaWQqPlZvFXnXoUHZH19Qs3hvGOwvbe375EYNvVXYUULba1F1UFAI4LFaEfm6itS1R5uwfzQcZzsJ2GNPZYykspCe9_s4MRVvWr0gad1DkaYJAM1sYdipS6DmMjTicA7R-LhtXuKztqW05UGFbx71dA1btLseTeHBZQ-J7xNh738uWC3PBuxqFlq7yBjiSNX_45dcJfDnntSVxzEQPklTsLiJLXXKn46TMgJKZ40kxjkfJy-K_JDNYsAm7830-5WgFt5kAoVV-RJ2ZmymsZaYnAn2iZ3MydZSVQNUvyFcjvMHxFEirX7flG-OqcJrcDxCikjbyw6A56Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/83586" target="_blank">📅 10:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83585">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d471f185cb.mp4?token=Y6DMl-eXMrz6a1tYPnihAPRgcd0ngAwKdC8Spatnc6ZyGHeuCLoQSnSlFKuoh8f5TXhkU7gbAjMu-ZIQ4t0G2ArJD8LBb4GQH5zn6jsh5nZddRKSwkh1vqErwvFlcXEMOF_mpN-YEJ_JRDcIzdKQfPfOZVRDs5lTbAXMWEJffqKmm4lifaBdwrHtYY_t10pEvaxWqofNVSUPNDRxauX-g_v-L-0W9rjcdRWN3mntLw1wPtEGsw2yUB_wlJnQ6FAywFxtUR2tF1P2c8Apstfy7Cy1CyoLMmGajcDQdO6Vm824ODYrVhq4yvXF1I2a0HcnKxyHtlNTf4JI_f6o3yr49GAHoHgJB7fAU1M6pLoFBVGrbYmdfEk5BRTMCvOu8XEfFZ1FxIicfzB5Mwkm2PkJGOnwrwcSaUXqXrcydZSr3EWITl4Ap-apetogWDNPhFNRLiuerCNff7qJlOAfvcjHurVPJIDb2Z-hEXMLrIUI9oQ-lWB_1yzypdRenLwW6HJmvg3DZlVfZBFlJdIKVCQH80kO7F_0ec_akrUmLOUk4OQS43h7oPytoo-53mvB8d6FUM9vJcrL2WwqMVtQJIo7GFQX8-acO6PxFZkSN2k6TIGGQuuYp8MhDyIKXpQY_V5y7EepGu-9dOBlXY50TkR6T8dwqUVV61iE-t7zBtCoAgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دريغا كه ايران ويران شود
🇮🇷
🔻
🇺🇸
Trump , If you are man come in the ground</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/83585" target="_blank">📅 10:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83584">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83584" target="_blank">📅 10:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83583">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">استهداف سفينة قبالة سواحل عمان</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83583" target="_blank">📅 10:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83582">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/83582" target="_blank">📅 09:34 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83581">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بكين وباكستان تدعوان إلى وقف إطلاق النار واستئناف المحادثات بين واشنطن وطهران</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/83581" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83580">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">استهداف رادار أمريكي في سلطنة عمان</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83580" target="_blank">📅 09:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83579">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/83579" target="_blank">📅 09:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83578">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URWjItrk5Ks5n7xyvrB7n-f5GooEkqlpQ0BzlLHGkGozY7Qk-0VBfJDz8mhXxJKnFl_ERW-KfVW_ahTKgqAm9pAt2yzXefnRB9tCwmtutxIOoSAyCmI4BnCgd9et0qtjgn4rJ7efd43xxcQD9hCG-TYjmR8ZJeRDNboXcu0opsb2RXZvPdfHjX1QVpnHn8op_s80f1qDnxE2b2d1pNKpF-WrCrAPkcSDaThqgO3PxwUDD6zWVsgOtI-x4A373Vm2n2vRX2t-l03ti5HN4ZAYGtdpD_PGrh5Piy32vRa35HZYFcjSz5o2hICirpEUF0tnHsFMjx0NNMS3WiBOIvOQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇮🇷
🇦🇪
بالتزامن مع تبادل الضربات
الإمارات ليست برئية ، حيث أظهرت بيانات تتبع الطيران تحليق طائرة تزويد بالوقود جواً من طراز Boeing KC-135R Stratotanker تابعة للقوات الجوية الأمريكية فوق منطقة الخليج الفارسي ، بالقرب من سواحل الإمارات .</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/naya_foriraq/83578" target="_blank">📅 08:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83576">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a186bf2799.mp4?token=nE_9O7G8Hg-rQM21npF3DPbz10PXEU4hANRcV1pD9OXHWJrCzqCiWqiTqPDdUI7L9I7i68KLamvw4enHVJZ3PtH0NfotOL4iwZLP2lbpRD5Q3u8UVT42VKU4rHHFz7Awv0THJ6-bc4bkrTPtP7Fr-K-fm_f37YeowD_u6fDFoO4jjMAL_s9GaioI_3Y8JX0RLPI6g_cQSdzA1LcuoRegTkis8TK5Lo5vxeDWKBlQ52nATIQc5Z5HddrqIr9al4oQ7-_Lo9buZ1XdTBrAToT_fSqhLjYsGm91M-VdautkT3uX-DdlqVZdwbkLVkG9I5JFQJMYuQRz5XiyBKMsT7dsvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز السليمانية مقرات المعارضة الإيرانية الكردية المصنفة كمنظمة إرهابية في العراق</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/naya_foriraq/83576" target="_blank">📅 08:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83575">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUN_7ALzk8ppSYc0004XmHXeM4SUru26FDBM8JlbI_AaiAnAsBFItu5gSFEvn80ZPdYRiTZb7BNG36sm9smvUm0_ckW0vPeu_gXdQA8xN4EnUoORk4Sxv7FBaH6iZt8-pzsO6ov08qxgkFDdMIBjOKiptkIbI4u22u7MZ26S6jdrZmvysksjWz_MuigESZ8mS_WTUyM5VXsuHRAiXCJdBIscutZnycHBUHKhhkiiXWBsZ-a6OG0n75J-SZtNQn8MPKK4e3_kHngFY1hkSnTrnNqz8scvHZbtMmzapP30wzlSUdvgDgvc3v4admgKKPW7jnybthabVRJFca1K3tNzHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خون ریختن
خون بریزید
خون در برابر خون
پل در برابر پل
برق دربرابر برق
برج در برابر برج</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/83575" target="_blank">📅 07:50 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83574">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇷
الحرس الثوري:  ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/83574" target="_blank">📅 07:41 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83573">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83573" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83572">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83572" target="_blank">📅 07:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83571">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇮🇷
الحرس الثوري:
ردًا على جرائم جيش الأطفال الأمريكي، قام مقاتلو القوة الجوية والفضائية التابعة لحرس الثورة الإسلامية، في الموجة الحادية عشرة من عملية "النصر 2"، تحت شعار مبارك "يا أبا عبد الحسين (ع)"، وإهداءً لشهداء مدينة بمبور في إيرانشهر، بهجوم مفاجئ على مركز قيادة العمليات الخاصة للعدو في منطقة التنف السورية. بالإضافة إلى تدمير نظام راداري، تم تدمير عدة طائرات هليكوبتر خاصة تستخدم في العمليات الخاصة، وفي انتقام لدم الشهداء الذين سقطوا الليلة الماضية في إيرانشهر، تم القضاء على عدد كبير من القوات الأمريكية المجرمة.
لا يزال السيطرة الكاملة على مضيق هرمز في قبضة مقاتلينا الشجعان، ولن يتم تصدير قطرة واحدة من النفط أو الغاز من هذه المنطقة طالما استمرت جرائم أمريكا.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/83571" target="_blank">📅 07:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83570">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veRXBs0YWIxcPhAYJUOa8p95ClvMlB4ht8gt_uXD0mvMLKSXzn3mzTe__Sn3la8S_sTSDKeNk9qH-M1sdTkVcKym1Y4U7uubI8YoOQiPpxwCUsKj-7pyuf0zNUvKg36F1V7XnApQB3AiVlXf3xPiSZV15SvLUAA9Ny3nIhBuJFFtQQuBvRpbyRQzFBK2PkE2VRokND3BDXxsmMWxxJ8fYmc9BrvmUqw1PvFOKiW05YtMDRfHa8mvMOgxkZZifwk4K3MJfAjLwa34Xeet5MhM435oVmyyKw9SYX3Mtz_yEgZSY_Nz7n1sByXeIg2rM4xpY8QSMnH9hb6rOK8TdpFHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشر وزير الدفاع الأميركي لقطة لاستهداف برج مراقبة في تشاهبار</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83570" target="_blank">📅 07:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83569">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجارات عنيفة تهز السليمانية شمالي العراق</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/83569" target="_blank">📅 06:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83568">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجارات البحرين مجددا</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/83568" target="_blank">📅 06:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83567">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هجوم جديد على قطر</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/83567" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83566">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/83566" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83565">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/naya_foriraq/83565" target="_blank">📅 06:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83564">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سماع دوي انفجار مجهول في العاصمة اليمنية صنعاء.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/83564" target="_blank">📅 06:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83563">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-LMUysa1TjaTm3vZ4OtBvP-HmZhtkvhnNRPdu6KrvtAuwZa1gwVWqqrCOvOtx-efE8GLbDZ9HXlF6mRDwRvCuU3g67bdvhY2MpYDno_2yyOrZg5_OZc6kIVOe4n2pnPVfm5-c4axBD3PK-5mNBDbVks4jHefbcBQK-Rb2QjdB6hG21Gp6PbRtKyAKFWChUEV84ElpNYf6BC3dB6cRENPCqAXZ7orwAhL2Oj4mf6FwMLOEITQ0ODLE65zWVgtKj2kYL5uhJzwp2O5qtRYuKZCruBCcUnFvu-L54c9qP2pcwOghj8j6Mc9NdCG4hOK8H-XsXUYim9o35huePsFQnqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/naya_foriraq/83563" target="_blank">📅 06:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83562">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vc0nE1nbGnJBk_P2ideO0rvgjsOR_2TX8rzMtQqH5ieqc3uLIyBID7976-_lxdC0Xs86OCNXsNSh0Uo0cXHdgD1TloW0-eK-O1tMhSUa8U11ojGD9VVr0tVI0MJe_zfUl45lsTLRPvDYbO4rBLZCneJsCS3xUaIlEgixjEnBGAwSzhg4trKKCJAJnwqJ7B04xFFbmm0UZCFDju9F2fAc3K9cf3ZlKjxPzw06Xj9vA2xnduhjztDOSPjmAuI7B9vhmB2d8ws2JM7rko36huFhnRn-IA-YxE3PcZ7pU2TkBjyxcqYoyjXCVtueN9g0cJ7GGGpDbtWffKfrZCaV2x1LIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83562" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83561">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTDYh6qaGynJ8mq8i5KCrqXsAZpRRKhQ9BkNq35dTmL2SH2kBkcc6iQUGL4pRT985nuLtBLyuijyutVh6aPeQxqy-Qw2tpoMiuN6wMnBb_vY8FQOsWjM-lA9_1tGtp1v7cVvVP4OynksHYbne6h8FOzUXSoWO3VzM2tk7UrliqEpCyp6wwe60x31z-b27CNIxL0wWizR6ZdOkXRimSzT3TAzHjo5Qiue_48Keq1Z5wOoCGZCmhPFhHVJ3-0o_WpL-QjyEGME04O6Bo_lj_1-7NWPt0tM8PmYGzZ38fSXJUD7z4zcXHxzjmPZcVX5L3C3uLLIlIEPPvZMDtci0DdP_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83561" target="_blank">📅 06:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83560">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8733970ed8.mp4?token=mqZlYwWj53FQbpzRkItCq04ds-90K3EIqeuLf57R5aAHu8XnW0RwiRkwoo-9OcmZR10iaiGi1FMQVSl0OmQsY1yI8QYLUHXHmNEAkTktEest-L_MiJ6L9g37pqe20Hs0BDkU3Joj1wWwUwA9zR5GFH7tZM4L_R2BeTROCyDUdQhQUmuyAlNE1NkWFkyy7gOBonx3YZs8y6qNQX0qsewdnfAo7xaY4cRlKsd6kqKQHLaLltznEJ3M0ExD5rp8Dfxr39aklrwEqdI3XX7Fnnh510GSyS6JrZlpPCqHIhZgqLj0KqLoLodffzRtqXRH5KgBKnBaN1IiwU7dJRlUzLWa9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران مروحي أمريكي  من نوع اباتشي يجوب سماء البحرين في محاولة لإعتراض الطيران المسير الإنتحاري الإيراني.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83560" target="_blank">📅 06:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83559">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/353f3a3410.mp4?token=hYdOjS20GKBC2ZIYbYNZPnp-6NLMBYfA4-HJ0vfN26bcruUPmPXCA2e-nWNX0YkYW0s1hnO3cTWJC5ASDpipjP4mepEqDVvrfiEMb-r08vWV_jDhEDGTXkGhoziTCTm7ySMPyGbGoXSlSyF5WxSOnE24vn7BCyX-otk3MsCRVZB8DV9mo116h-jIpUPmGGLpljhYO-lKUIiFz4le7BMXz8jQo9SQOSl97wJpwJFMv7wfPUPCtUfBQHseqbDMFEzeYF46K8a3IthsLhgt_XCxva2WuTjbcXZzaJ3zsqHwPEtz_gpkSlMHpRfFmZ0VaOUGKvzh3YenmEnrrGGo_CTXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني:
هجمات بطائرات مسيرة تابعة للجيش على مراكز دعم الجيش الأمريكي الإجرامي في الكويت.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83559" target="_blank">📅 06:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83558">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a39b1f78.mp4?token=qB7ieZ9JoWNNJ7KJh80Jp-OmAkA4LZCKRwIF4Un8Z8NcIfpkQhmmfRA7uSff39AAGEfm10HcudSHH1NNjC7BxD3APPu-Mh22DQOZpb5km8XnNQWfLfe-drkLoRwjSMJB1AzAJ3zriI-eHPOmPt6yrdpW0W_T7m5NIEC3io0qtK-3KBg7lF11eZLqaz-IfQUPRcpn7Cks0M8dWfswx-73mLhtdcSalHfW9Gtg6BnlP_XI0YGDBG-3qQ3v_qGPfro5yPePq8oz-jTmbfPpieqvwxzjCUYoBFDLiYm0w22TBp_XNkXDGhH-4qk0n46JkpFeyT4q7cCape0a-926F78PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من القاعدة الأمريكية في أربيل بعد استهدافها بعدد من الطائرات المسيرة الإنتحارية.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83558" target="_blank">📅 06:15 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83557">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انفجارات في الدوحة</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83557" target="_blank">📅 06:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83556">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات البحرين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83556" target="_blank">📅 06:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83555">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b0f5c801.mp4?token=mP2sWOthOn7xB_WZeZgFs5A05Srx0UsCBNhSDIJ2Vnbad8GDp8frC5jZ_EMctvN3A5vX4XKGJjzkJvY6J9MAkYm19KZqt84yVyn2BbO_s-QGBA-k_50PbJIgEvo6pIDpmDbkKk4np2jMM1B0iDvoHrBIn2iXATGwphSnyBiU9UwvtH8jCQV5TraMfEPClwu9fkvLWvL4IfKbKet4d1r9uTmKSa4CGooFgaQFSgKOjHBVE2EWQlNMslRf5n9tHyC9xli18_Y_3CsKikrpwr6h9PRZyLZ6O44a8s7wDct27xy3fFXVNI9KYQNBdv9K-7Eenh4XOy_Zpk84aw8OgMqVKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83555" target="_blank">📅 06:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83554">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6d2c418d6.mp4?token=mRDICXiYBqpiDDUP-7hTX7-aY7x6VN31qnOeXvcK8W2U6kgliMC4l93iLOYggaAH7I8rJp0kBLo-3mbv_txN0r-bqAG5j5VR8V99D-JWgNZ8if-oRJNMIC1M6J-9CHRtO1E9Oo7pGgdKNAU2JQTDstk8RbG5YfhQPCtCHodqAXE7wQFG234BbC1TRlcDH8xKXIkgp9XEaUeiKBCdoMkCOWII4rgHPkSC2rMeIaETSPXRE9aMd8BodzFVDvzvkpi-M06Yha1ZX6-oVTVGOKBAXbXSF-hrYGcJ-jGszwaHLTV80414OO1nsAEYVGBJ1PXaI7Vygf8iWmm-YKuir1xRgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت تحاول الصد وسط انفجارات عنيفة وتساقط شظاياها على منازل المواطنين في أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83554" target="_blank">📅 06:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83553">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98243b5322.mp4?token=hoCIXF6BQnOVvAt74dtYC88UUuCZlNFJF44V_hxFG-Bayppg6b6ZXr3NkaXccx17FxmwbGy1-Paf7RX2_hz8lHYKH5qwz4sdKsPkbn8rXVIr0LO9eCVNdlUshM2YnQ8ONqpvFHAosVhS2c99UF9V-jyIIVKFZESPdQn3z2ielTRk8nA8fqR17SS9C1B-KOYueky6xDIdCxG_XeybCw9MjWYFU2lSvHYVlXZx99cLrV8VxZ8hwGGnlEill0L0YB3m7G4a-LMe8jT5pTrcNF3tBUulVhRmWr1To6vmA3ukd0GFEjpfoJEZa20njiQm2xGQM2tkPcSIKaL5pqhMZJujyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار عنيفة في أربيل بعد هجوم بأسراب من الطائرات المسيرة الإنتحارية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83553" target="_blank">📅 06:06 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83552">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpWquTerW2y0SQUFnOM7ICTwwwXir3RcJPPwPwI32h0xnVGbSMszhn_QvtLX4f4G5ZviscuQfGvUaI3yLmK2aYuLGxa-WPLDFOjw6ulqmp2UMjOfnzKKIXuh_rmpJwPnxJ_YyOP4NzoVAH9ZmZ-rd8aMW2EqEVW2D67UHe0_Q02CGw_e2ZVl1Iv_AytwQItPvPhKqnsT53Z0ZuohMBtPzAzUJO8sc2iMVMj8qaqBp7SVrzYjOaAwObw1jW8YgJbnH3IPRHB-FT4vIKGwbrfrLBXEoJKMLWHf0jf11yLc8iblw1KGzQAt3JcwVq0ju4aKvaCnRgdrWXoxnm8lRZbb_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83552" target="_blank">📅 06:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83551">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تجدد الانفجارات في أربيل الان</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83551" target="_blank">📅 06:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83549">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43539170aa.mp4?token=VwisUm3oPuNyPNkHE6iAvzovZ7wFuiJ82l9Y_dCjj9b314MDnB3CFS5BsT-uNvERwK5fDamamwbUnnNXqBzPDJ81CDhV3zzaP5jwDt6i_VM08YrM4OKBfPpsBT9mQb4AaMBWbd950Kb1nUB5IFZsUweGCBwlkFzN8ZLdMjUedQ1bQKjJjHBVqIN570sBXC0aZAhPYi7Ora-yVG2d7R5tGPIGhnaJI2vKaH_9WQmrlzozdBSwVViO9whvLxAmenHxhkcdCYMMHe6akNZV6XKGqBorKB514tgkO1HGAJhVRCqCE5IG7fHQv4S6UPnDCbGd1wQKuLAFOoe-Y0GQTk38Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/83549" target="_blank">📅 06:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83548">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d537f28b30.mp4?token=p736gsnK4zcfd43PO66eX2EtNbGb7g77vuwKdT5UMdlpNX0fGqK_TUpgnJk1JfWPR8q3pxXu1AP5mZ-P061vPpRVcIrc-vsfzqF2XrG_P2HfUA49hYzKu4ue4i3oPPh8Xh34BguroEcPQ03uo5RejIWNUBJ0YFo3nGAJqtwvweqp2iVPtc_N0dQtpnCFFRic-YAw0eqitj9WpZo31dGZjhjiJ2vjn4LHFZd7HNwBU1XVo75xGGhS7857BQ4s5uyLNZwV_IHA-YhF94u1p5F3f3Sx0pJvBbxBaghx3zw4XPZNk-sNk8Da9ZsZSAamNoYXYrk8ZC_W4VfWgKUth0njdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة الباترويت في سماء أربيل</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83548" target="_blank">📅 06:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83547">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc9b8186b6.mp4?token=oJqglUWSCRPQ9TILSK_TWamUGuKjp_SGt5hqR75qu7bPzAsxf2BTk1HyeQdkr2O3EzFHiA8wyczUP-QBQWw2sYShggQmlMTq8ZOJg02m8lrlD8Gk4MeXbvGhVjW4-wEsKZu04Z8DJUcMEk1Ax90ZmvD6Vdmz4VDbgSuSnoWvTGTgSUvhretZiZLuEM0WbY0BgkM-pQYubF8YUqkLL7lGO7CIJ2cGgmMQ7jFZxazKPCjA-Khy_5m7Sg7OY10RndnCEDMxrkcbbCk-RVK9keL-icuFiKctMD_LY29mpd1aS9INCV2icZPeAtvWFPDWbEQu7Oq5eELzP05lZwbS6Mv-Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83547" target="_blank">📅 05:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83546">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995536560e.mp4?token=ldJth9rWF-2o6hvznZ_UxeuKNU4f00dzEPz0Qc5jSwFxXI-vyBzT1TUMARC9iIMOqFcuhta4uMbr22gwSy-HojmU8hcjr0vpsU-Ob-rDeI7C3gJm-Oo7uKolJO3CYClZPtxh2FyZItIhPb0WRpWpb4fem3va5ZZWmD7z-I-jcjMCq2IW-eC1Nc0bon9KADGpq3nd2gimsdaJaKUt6xoGnq8sEyrn1DHZaZ8yBnRzUWcwnSQ0g4VpnSIlZSxsjTFPSick_N3PuAXlaeEOR8NiN5Yj7_fUPc9CerVn1cma7CYZVjh_lcu8j1jnnKHRpcmEEzapTSru4gSQRAfxquCdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفعيل منظومة أفينجر الأمريكية في سماء أربيل</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83546" target="_blank">📅 05:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83545">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇷🇺
هجوم روسي واسع على ميناء أوديسا الاوكراني .</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83545" target="_blank">📅 05:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83542">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f41868f4.mp4?token=KJByZXbS2zl-RH-eTl9D8DchR8k5hRVT2CGMOPIOKKtrMJqJrp1DdDiHCcJXREzSUMslw6hPX83I2FuRPIUbpZg3Rbdsg2URek2bpEKR_aGUalAkKTJ3aPTMvzfoPkKLBaCQ3dVJBipDC3ntzHf0RUbv5ChqaaWjrR5CSUSHqq3s9UEPMjDENy7I02tqh0AU1L96N8KPkEw38x7ABu88F_qVHFORMeUrqAEwxCGAuDcCn2aW0yrchi98rNJP-q0KTiMNcpHd53wUCk2HH3R7iHfgevQlNx-jhw4DgMG49C89nHkOsx1Jo6L7jk1zTkTDiHU-VLmFKa7Sh0xLnPfANg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $   But park your ATCAM near Persian Gulf cost more</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83542" target="_blank">📅 05:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83541">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">قطر تعلن اصابة مواطن نتيجة الصواريخ الاعتراضية الأمريكية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83541" target="_blank">📅 05:43 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83540">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6598f4c01a.mp4?token=pH0EDEYBzdoo_bclV6bNCsWNcAi3rCEn6y4wB6jwH8hZthfpkEHJh1ukgmjQOhJcCroHCNuvPivyoHVrf4QLgrBkfujVkFOeMpkEXKR-_h42c-HaHMkXHCY6ucQbWBtEnCt3IQ1dVqQGxXiwMv0kTBIBape2I7MQbIhIEaTdxnpcER3kLourFMmHZtoNh_FSqBf1ngWlGKkII5pDJnfnsDh0s7RD80uZqw29hGghybjfcEddGKC5qUdc15Mh2BuimweQXMKJ6DPom04g1UT5CDYw3kNwxsYMzyVeoxwCvNVpSuVpIPztretO6YCzahnS7GBBwmzU-IcmkYO4rawD3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
الدفاعات الجوية الكويتية حاليا</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83540" target="_blank">📅 05:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83539">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91f0d257d.mp4?token=LDNJUHGMiI9vkifqeV10hxEsIksWRsjBkF-iE49vpc68be8Kfgrbdy0NVRJnIRw0dV9n8l7OfOD0U364u8yBUa6GICVSegAAOgp19ykdnZFoRpSr6ktp-dk-GA2s3qzoWT-d6y2sA9OgddQ0K8eXDo0h02mlRbiQlLqIrxP5XR5cRNlsYG7aq3VlK8SnYI_xwh3AiaFk6D0qSG5I1HlJhJIIEcb5fzMUntFFXiUrEpFBcxSmsfTwHA_sWoU9ulIQQ88XdXSz6uH-aJHXeiW30LdVQ5aVWJxq8qa-3O_pytrMFdfIvDAJQFJVBptPkzbOuLvdyAqWAHFaHI56NKgjbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من القصف الصاروخي الإيراني الذي طال القواعد الأمريكية في البحرين.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/83539" target="_blank">📅 05:26 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83538">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256d6464ef.mp4?token=TJf9-xzuuZQYZknfEIDAxZl9i8EEO8ktyzheypTuHQi-HI2A2jJF7TE1cB4BgG16_YMM9PTqo0FD9KmWAxS14VwgxZwJB1OGEQ_X1vxu9g6Q3l8RlYvqHmobaRUI41u2uG14rrXYiChQ2BAIJa9RUW5ESR2At2rf-N5yeDPNzqENYWY1HPeW8FlCSeqR5m3QOLPEQX44L1y2uoefCn9c3UMp3NB78wrmj95xgGqecApjYx1t1tTB0hzgJHkuVy8pOtfRS8HhCjTuJM5nLWb9LV2TZ1ZrnF6ZDKgQE0PvJ1T-47OtWac__xeylM5kBbOLJ_3DK5lUaGHwiWtI6C7Kpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي:
اليوم، في الساعة 9:40 مساءً بتوقيت الساحل الشرقي للولايات المتحدة (ET)، أنهت القيادة المركزية الأمريكية (CENTCOM) أحدث موجة كبيرة من الضربات ضد إيران.
شنت القوات الأمريكية، بما في ذلك الطائرات المقاتلة والطائرات المسيّرة والسفن الحربية، ضربات دقيقة استهدفت عشرات الأهداف العسكرية الإيرانية، مثل مواقع المراقبة الساحلية والدفاع الجوي، والبنية التحتية اللوجستية العسكرية، والقدرات البحرية.
وتمثل هذه الليلة السادسة على التوالي من الضربات الأمريكية ضد إيران.
وبناءً على توجيهات القائد الأعلى للقوات المسلحة، تواصل القيادة المركزية الأمريكية إضعاف القدرات العسكرية الإيرانية ومحاسبة إيران على الهجمات الأخيرة التي استهدفت السفن التجارية.
وينتشر أكثر من 50 ألف عسكري أمريكي في أنحاء الشرق الأوسط، وهم في حالة يقظة وجاهزية قتالية كاملة</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83538" target="_blank">📅 05:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83537">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WpMMeC2OlDi562QyXt_7JUfYs9ru2t5dL71Mkl68TAGBM3ytZklSLYQSM885RUehGkzh-x1ifYh7u2QSEXFXRzw6EVMbXskyrYhCRdAsmWzcQqCm0rmrqXjvFSsXMKUSMovP0THrG4GgN55PtFJebp_YcNywwiCNOcwuuB5Z4gX2kCSvgDzXKBXMws4nDVIS3iqiEGhNXora74eCNV6fvPTtF7SW8nR9klIM9h4b8if02fOxFYhXlAvf6mOJAtLvZc96wONQVhdveUTkK2E8c2NcoS8OXJ3N1ADwd-OWSYdb9FyDxYAbZG2Ci5jnL_Cgq6rx30JG8ZTFIkp4HJK79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83537" target="_blank">📅 05:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83536">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تُظهر لقطات مرعبة من المنامة، عاصمة البحرين، فشل بطاريات الدفاع الجوي باتريوت باك 3 التابعة للجيش الأمريكي، والمُخصصة لحماية البلاد، في اعتراض وإسقاط صاروخ باليستي إيراني قادم أطلقته القوات الجوية التابعة للحرس الثوري الإيراني. وكما يظهر في اللقطات، أُطلقت ثلاثة صواريخ أرض-جو من طراز MIM-104F باتجاه الصاروخ الباليستي، لكنها فشلت جميعها في اعتراضه. يُذكر أن البحرين لا تمتلك منظومة ثاد المضادة للصواريخ الباليستية، مما يجعلها عُرضة لمزيد من هجمات الصواريخ الباليستية التي يشنها الحرس الثوري الإيراني.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83536" target="_blank">📅 05:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83535">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVz5Je8F8SgYpr0vDROJw6JzJ9ngN48IfJPcBDO32FCxuRO5HkGz5xNG3mJEY9v5rsTbroK-XDI7rXebPSqXVXBCpcIJEG-2vBbopxqpAW43qw8FVS4k6ACKN7ngA1f9JK8kXCEw3FI9PTwKiPJfJfLGpjGm_I61kQ74fV0WCxgEKSgfAWeHnajJ7UAYljn-k0IALpoABGcF8PwbghT6Hu9gwkgrLL6jGzvNns9PHeGqNTUNfpAVG8U6M5HahGBP5RKWbeJoaFD4Mwx1gFvapPUjFeoILO1MwDzURzxYgStAbPK49IbGO5BmdC-aEaHn9Exz0Gv13m5i42ION_GqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Parking Us cars in time square New York City cost 10 $
But park your ATCAM near
Persian Gulf
cost more</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83535" target="_blank">📅 05:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83534">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏
😆
ترامب: يجب سحب تراخيص القنوات التلفزيونية التي لا تغطي الخطابات</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83534" target="_blank">📅 04:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83533">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">انفجارات في قطر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83533" target="_blank">📅 04:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83532">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🇷🇺
🇮🇷
🇨🇳
🇰🇵
🇺🇸
ترامب: يمتلك خصوم الولايات المتحدة، بمن فيهم روسيا والصين وإيران وكوريا الشمالية، القدرة على اختراق البنية التحتية للانتخابات الأمريكية.   لدينا نظام انتخابي منهار تماما ولا يمكن لأي شخص الدفاع عن سلامته.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/83532" target="_blank">📅 04:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83531">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏ترامب: الصين حرضت صحفيين على كتابة تقارير ضدي.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/83531" target="_blank">📅 04:52 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
