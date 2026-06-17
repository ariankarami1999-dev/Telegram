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
<img src="https://cdn4.telesco.pe/file/kdhf4drlnjuwXvCCsdOfv4YdnCtN9EMOCVjKY9W6qd-bcbqVbnXffymJ53HDLZKsX7izLgz9fGvlA5SiqxX1uW4Uqgtb2cxJ1qNg9JCQkChemWsyZL2O8OYIilG7dBx0IXvCwPuf8_w348nSgbaJLdKETyWrGTd9kUVFYl_RtnRsS59q861juIYKJ6IFeUQ-npiME1uLP6-UjVuHoeTof8nS2Wu83fXZcRMGMtXKjfuPSxrrmtR9SXgbCigmgj791HOEnOgFE8gw_yU48BYmiGQVIUMZ5VJD6CGD21XZzn9pPmF4dNx47GHgjTOWPj-NgH3A8DWfHUYNoSH52iTV1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 20:57:42</div>
<hr>

<div class="tg-post" id="msg-79147">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇷
الخارجية الإيرانية:
ندرس حاليا فكرة توقيع مذكرة التفاهم من قبل رئيسي إيران والولايات المتحدة عن بعد.</div>
<div class="tg-footer">👁️ 1.49K · <a href="https://t.me/naya_foriraq/79147" target="_blank">📅 20:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79146">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني:
إذا كان المقصود أن علينا الاستسلام من أجل رفع العقوبات فذلك لن يحدث أبدا.
غير صحيح أن جيشي أمريكا وإسرائيل عديما الكفاءة ورغم قوتهما هزمناهما خلال الحرب الأخيرة.</div>
<div class="tg-footer">👁️ 2.52K · <a href="https://t.me/naya_foriraq/79146" target="_blank">📅 20:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79145">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b481a9a85.mp4?token=O-8rI6I7iWBimUtpPhHfLQ_8HP1eixc4rAhnpci6fQtoUcEHQS4wIIE5QyRHcj0OsZEf8YxQnnGz6zJEepgOtPTMLxxiHARNINAv6vOvafQGWjszijRcuB3xP6gKmKUDeq8lIgT2tmU22KSbpD1F1Mka7GCdHWyrF8531YkGR0iKWXSO3LOuuyLWQjHXwyAagYONUWpcimfLeQBMBKikPglELYRpWBqg_A6lWCHWAwmwU1G04Qx2enKA-ARG1o8hSyJs-td3RPROmhUvjajQkMdw_VhpDZDLFVymj_p-zWhBKqk-ehCsQYvG9aAnrog_Vkbtj1KoGhLH4H_lkEv_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بعد محمد بن سلمان.. ترامب: أفغانستان تقبل مؤخرتنا.</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/naya_foriraq/79145" target="_blank">📅 20:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638e58ad.mp4?token=qDKiwpEzAwnPbO4y3w_Uy5J1NgLOUXZ9vpe-Go33OvybrObFw0qOfxVPWtGI9YeJ7-xlt9PMcyjGkEySei0_ytYI6TewnYkFGUB0loT0QeByAlHl9o5rHhYUd_o_PuBzokUNJXssPVMw-cOiZY2GpixmhYFwQ5ftflso3q331wkm36pAGXOZStMRRvFw0ljtNcoB6EP3Kmp1MZvVOL6XAmTqv7_nnjUfqkO8svKAYp6MtiR1QWkCmNaLYdwjzo3jgSDnssnTvYMXlDPYIorJ6C4Z9GqVrNQlOzAd8ljp8Cv70CF527o0Tx5s89_Il8eZmHNWX4RiB1eL4uq-wIPT6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب بشأن الحرب على إيران: أيضاً، ستنفد احتياطياتنا في غضون أربعة أسابيع تقريباً، كما تعلمون، هناك احتياطيات في جميع أنحاء العالم، وستنفد بالفعل، وسيكون هناك وقت لن تتمكنوا فيه من الحصول عليها.</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/naya_foriraq/79144" target="_blank">📅 20:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/naya_foriraq/79143" target="_blank">📅 20:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79142">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">⭐️
حدث امني بالقرب من اليمن</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/naya_foriraq/79142" target="_blank">📅 20:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17258c72ec.mp4?token=c-Mu_NfdsZFOBxmKhtpgVmJpdzwEimsiTA1_aoMduf-aVvjrV3X9D3f1cWPq59SD1rDM-mLxT2OmnElDD3SfmM4g-kRdCYo1JDkrAD09vJ0OfnqJmWH0ObJscnX1WkfugSQIxWAjlUfQ1N6Mko_zBx7ECdhjieS6CBHSXduqg3nwg1iqbFSy3OaQ1gjDkGCaNQnu-jumEUrn0EPlikdDYlLXDkJkxvgcDg8YD0BPbnP_U2qe3rPTM6Y62O9s0UmQibzr5NFyO6jIqUdbF1YBmPBUf0w4NjTFHBgBCtOcXyJ7QNlDXJo0bnLiHqd13U6HW-Q5l5R6ClcttLMxICeDVYiT6GKrO8Ai8dN49FWMdolFuCtOSLM04mVohF6hSJ0Xg62NbXOqfslfkAZQcFAx_qlWJ18-7CsXmOKqNGWTUoJ-dp3axNI-ovfgUv9mjIYUnwqLHGXsm9XKXckMeznPsZAaYQcXJmUpn1NAsoQXCbJb4kX1hdi3zJ-K8eK6YH3zsT-DqceC4PeE5r5OaCKCk198eBv46MScJe_zVmfKFoP6Z1Pv2jxOozjkpCav9fp-qBpcGiqUvlyGZLQ3FivKkpkzAgioPV6_KbXeaRBW49ZpAyoDTKX7DIYCnffuncYNUUwfAnsPNUjJHsa_Lk5gY71R5-RUQQVflxo0TS66rhY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب حول إيران:  حسنًا، إن إلغاء التجميد - إنه سؤال سهل الإجابة عليه.   لقد أخذنا الكثير من أموالهم، وقد - أموالهم التي أخذناها منهم.   عندما لا تكون أموالنا، فهي أموالهم، وقد جمدناها في وقت معين.   أعتقد أننا سنضطر إلى إعادتها، أتعلم؟   إذا لم نقم بإعادتها،…</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/naya_foriraq/79141" target="_blank">📅 20:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79ca6e5e7.mp4?token=lZ8LkT2Ch2TPrqRvDQT2J2iOeUnLKiTDCRh9ZMj72xJWswClCfJmnRBIcPdeX-tZpW5rb29DqYP9utpgJt95_2AZ2yxpyHys0SOIvvrhKq2qIg7SEvXy_BozZsrfcYrKSaI4UIao2qme_672MUrY7ci8PDTQVuViSf3USQ6Eh4lsY3HtY9qrRUfUssO6mUOW-2sMuUkOC7loc5SgzDFc6XgUEqXWLYFgb123wVfXexfYnJa5nFZ6O7tLvcZw5P6jI7l6pl2jvpxBWk2YSUloAKWJ0PAjNYR6D9R5z598wYce8aXgqub4_QeDZ409gC9DHDXpd-Rij4c-M-NafZhzPRgph4lVV89Js0xPG_UUVZu7FQrqBH84lTnEym5qZW_O132XOGVcKAkWrBDT1luoN5hHnDnXRHrhPmYybEgoLi2YXPrWO0O7R4spta_OckcDciD5XU_7lgzKb9x2k1QQ5jyx1Iu9Sucdx81R_1agOwDc6f-GBBycYKL_2_jBhrCaubMvj-zpRLuQdJNSoM7HUS5bj39Bkb-6Nosq2yldUbsqDxAKGdpB4AbuDQNGjSBg65dwky8i_QXGzRKq1S3F5w3jgpQ5Au73macwiwHmYy1l4oWoL-JaS30sjUEj8-HHlqu5TalaHFwwOF6B3qqzSu38ogOmsgIqW8Ga2DN8hp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
03-06-2026
ناقلة جند تابعة لجيش العدو الإسرائيلي في الأطراف الجنوبيّة لبلدة زوطر الشرقيّة جنوبيّ لبنان بمحلّقة أبابيل انقضاضيّة.</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/naya_foriraq/79140" target="_blank">📅 20:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79139">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c093a28307.mp4?token=F5KP87vi0Nz5iHR-SsEVmTZGwdEPlIu-fWkWXFV3Icd_VDqiQkt2OJWQKCSRVZ_6pvUuldulYY5bVLfd7C8edBaXLZrjwzpznCCVziy-vkmzptIEzuaJ5FALCEiaFn_ZrqZl1bZcpYk0zAPI46yxEo2fRIhKIHq9rAD6GdDe2oKpx7uHnM92QA28WjPi0yC0lQiJMecCj6te51ZbjLJ_YR5AVji21XXS78MC8YVM5Xas-DXicKiAPlrJZF6_gZarZZdGolLiJyrfcjI4BoADMl206hWvngnRDj0MVuwva4-yN3H01ZymrymwH0HMqjf8Epv1oa1si2vMYAWiwNdgEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب يسخر من محمد بن سلمان:  لقد تحدثت إلى ولي العهد السعودي عدة مرات - إنهم سعداء للغاية لأنهم لا يزالون... يجب أن تجعلهم سعداء أيضًا، أتعلم؟   نحن نستخدم مطاراتهم، وليس أنهم يمكنهم إيقافنا إذا لم نرغب في ذلك.   ذهبت للحصول على ذلك الوغد الصغير. لكني أخطأت.…</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/naya_foriraq/79139" target="_blank">📅 20:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XO3i-4CIzyTPVXgDPSFUX1ppe0t_PbaeQm4BfGecINhLTk9vcEWx2psB7579gAEtgaRhJ5g-kBzfAs3im2U-wGWML_nuT5Y-YJ0k40Pa_rKQeLH8oqzhZ8ZUnOayWAuCKXxEEfs-tdK9jvWqq7_NKPIC2YVwKoMX-aZzlN60fB19ACNt4BmX4tKeqO3JDtEVXPa4LT8G5fglOitiocwgWfVNXUfIQiUxELpnLojMOl4cWwcwEdX3pTX_524MikltTeD391BPzwNd6YfMwNm6r0ec4sKnG4HAwLMHhwLAML_1-77eCgisST-1eTsQ2dK3HMwmiBNJDigSrqVtOkCIlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ إعتراضية في سماء مستوطنة المطلة في الشمال الفلسطيني المحتل دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/naya_foriraq/79138" target="_blank">📅 20:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=HMl_lKGcVwlcOCvRIaPXAihVOKuDe4znmdwedxNg0TQiJwd0HT0_ibYjYz8pdJzBuNlIA2xXoGuPXQy19H65wndBXIGxLt834OT2yHLx0e6Akw2SqO7Go_Mgn6P-5hKzwfxFLZsOF77jlqvb5cQQkRRpcQbvmvFnDuIew7_I2c_m96cDxar8if1j8VbShtXyg9sL_z_o-3in5R71xkAQO9-uDMe_2qy3wNwh1hEKnCEOHdTR5r3p66HsFXLQ--rX770pH2-BpI2X9vHPj_-sUjKR8yBxbzEz3grDzpvHRkhou8powhRbvspNaW1X_NaRkJ3eV5CEzxD0_cQEvnp2hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02d9c91b.mp4?token=HMl_lKGcVwlcOCvRIaPXAihVOKuDe4znmdwedxNg0TQiJwd0HT0_ibYjYz8pdJzBuNlIA2xXoGuPXQy19H65wndBXIGxLt834OT2yHLx0e6Akw2SqO7Go_Mgn6P-5hKzwfxFLZsOF77jlqvb5cQQkRRpcQbvmvFnDuIew7_I2c_m96cDxar8if1j8VbShtXyg9sL_z_o-3in5R71xkAQO9-uDMe_2qy3wNwh1hEKnCEOHdTR5r3p66HsFXLQ--rX770pH2-BpI2X9vHPj_-sUjKR8yBxbzEz3grDzpvHRkhou8powhRbvspNaW1X_NaRkJ3eV5CEzxD0_cQEvnp2hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: ‏إن توسيع نطاق اتفاقيات أبراهام هو الأمر الآخر الذي نأمل أن نحصل عليه. ‏وأعتقد أن المملكة العربية السعودية، إذا قادت الطريق، ستكون قد قدمت خدمة كبيرة لنفسها.</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/naya_foriraq/79137" target="_blank">📅 20:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79136">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇺🇸
🇸🇾
‌‏ترامب: الرجل المحترم في سوريا، الذي أصبح الآن رئيسًا لها، قام بعمل رائع، فقد أعاد بناء ذلك البلد في عام ونصف، مثل بلدنا إلى حد ما، عام ونصف، بحجم مماثل تقريبًا.  ‏قالوا: "لا، من فضلك لا تضعهم هناك، إنه رجل عنيف للغاية، من تنظيم القاعدة".  ‏قلت: "حسنًا،…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/naya_foriraq/79136" target="_blank">📅 20:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=E9gUMnqxjhln202zbPPxutWQBWdXm34pDB_ors6JPtA-nrV1WYnF9kRoQb90v4Dxrj5pEbLVDBs3xARt13-L9nESxlxDTeMQ-J9eHngnGF9KwZTR1LwViU_oEQYjd4_sjcWXJ_JoDVyp0FoImrxlv1GM0S9KvU_m3qakCg1eLNCEj-VeoJNcY119RFoULBjDce-5li3mY7Z1PmFhaSUg_beWHza7SvgSXuBgoqjs2T7i7STQ6nznS1dnQTcAIvNYIFQMotfTkM47SRWR7MYscKDJ1qLSvuS9miwDVUkgxs4ZaMYvAFcQ2NNzc7To7FDLp3z5JleuGpI0Wcs0KG2topFiVdBcTKTlCiWS70VgG4B4tDv-xsk8YTN4N3FXAhsND_fzaEasmYoCKNmf5-9qyOZLP2Kq42wtIhgoPQj0X6KplxWXW91BHNJGRkaI08uBhaWVhEyZcJJhhMzaRkVD4giRjmRZh8HVqx_dO6801bJyXmo-5leh7_1wX2RmNfDNW71R0WbaCbhb3UdTkZyAAnH1aAHKlU5PcMETKrxTd4BwxuGpDIQFeuEP58UsGe4_ybJhw7tZC9zqgSKA84bZcWXIBhhexkJ65_3XGJj-H2JEdhHjaDL8a69OkOQrCGTD16CsMxzS9nT4NWA_Mihj0nOsEeh11A0JWxIbV3v-Nvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/318ac4b0e0.mp4?token=E9gUMnqxjhln202zbPPxutWQBWdXm34pDB_ors6JPtA-nrV1WYnF9kRoQb90v4Dxrj5pEbLVDBs3xARt13-L9nESxlxDTeMQ-J9eHngnGF9KwZTR1LwViU_oEQYjd4_sjcWXJ_JoDVyp0FoImrxlv1GM0S9KvU_m3qakCg1eLNCEj-VeoJNcY119RFoULBjDce-5li3mY7Z1PmFhaSUg_beWHza7SvgSXuBgoqjs2T7i7STQ6nznS1dnQTcAIvNYIFQMotfTkM47SRWR7MYscKDJ1qLSvuS9miwDVUkgxs4ZaMYvAFcQ2NNzc7To7FDLp3z5JleuGpI0Wcs0KG2topFiVdBcTKTlCiWS70VgG4B4tDv-xsk8YTN4N3FXAhsND_fzaEasmYoCKNmf5-9qyOZLP2Kq42wtIhgoPQj0X6KplxWXW91BHNJGRkaI08uBhaWVhEyZcJJhhMzaRkVD4giRjmRZh8HVqx_dO6801bJyXmo-5leh7_1wX2RmNfDNW71R0WbaCbhb3UdTkZyAAnH1aAHKlU5PcMETKrxTd4BwxuGpDIQFeuEP58UsGe4_ybJhw7tZC9zqgSKA84bZcWXIBhhexkJ65_3XGJj-H2JEdhHjaDL8a69OkOQrCGTD16CsMxzS9nT4NWA_Mihj0nOsEeh11A0JWxIbV3v-Nvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب بشأن حماس: ‏عندما ولدوا، خرجوا وفي أيديهم رشاش.</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/naya_foriraq/79135" target="_blank">📅 20:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cad99d52e3.mp4?token=XBvEA1qnQgKKOpYP9Wj5yO8qUFTmK9jgp7sVXBIAdoDN3OMO8Md70O53UgYyfDXyvQEX-d8PBFofcr2qKjGMnjofkUk9mbRpdufO2MzHeQ9mXrq-oYyUmwVpz8oRo2r0uSj08B8knO1RZc4bq0wyuzeHovkwW_QaIxiTD8NFExJ8LUWnchp0HCBKtDnfQXbmPdXgMEB6MDrJ2t0A4I5rZhdEDJpZ-Cve-1VjD5eNdiT-jK29E4qJ4I6cwwKB_g9KRWN6VkhcL4hle5-GZHR4uf8PbbfJacaGo5Bd9RuXkyYoMBfA5P9ZgDJ8fkzFvdc7W5fp972qRIz1kKoASt28dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🌟
‏ترامب عن محمد بن زايد: ‏محمد في الإمارات مقاتلٌ لا يُستهان به. كان يُلقي القنابل الأسبوع الماضي، فقلتُ: "من بحق الجحيم يُلقي كل هذه القنابل؟"، كانت الإمارات. إنه مقاتلٌ بارع.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/naya_foriraq/79134" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/naya_foriraq/79133" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=ObPOazdZukEEpUwXrQiRd26fP_Ooc9pCt_XpY-XikqDc8Eh4NaKNCIlhXe_pAaPLZJ0VoXxXZZmOLxX0bC2G4t7BUGdiMrKCIgV25QUEOdt5_JZ_FXnil9HL8K7X_SCZohrjLoZBJdpRZFmt4UTUQHh2yUlLbORiZ8_N00V6H3Edbg8BrG-m51BroFPdpu09IgRwkWG6HBx71P9AyEEPBcoE9QFIZum5fSRN1Zk9iaf44TQv9PvpW2CZUuH3Y2M38Qrz4yTDTVDV8t6-DR0t8lIgeZltQmdRGmf01s3HUBCB9Zu6Zk_N3amWPru2JJeAvvh5hHaQG1KMCBXXPowSoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3484ff455.mp4?token=ObPOazdZukEEpUwXrQiRd26fP_Ooc9pCt_XpY-XikqDc8Eh4NaKNCIlhXe_pAaPLZJ0VoXxXZZmOLxX0bC2G4t7BUGdiMrKCIgV25QUEOdt5_JZ_FXnil9HL8K7X_SCZohrjLoZBJdpRZFmt4UTUQHh2yUlLbORiZ8_N00V6H3Edbg8BrG-m51BroFPdpu09IgRwkWG6HBx71P9AyEEPBcoE9QFIZum5fSRN1Zk9iaf44TQv9PvpW2CZUuH3Y2M38Qrz4yTDTVDV8t6-DR0t8lIgeZltQmdRGmf01s3HUBCB9Zu6Zk_N3amWPru2JJeAvvh5hHaQG1KMCBXXPowSoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لدينا القدرة على الوصول الى اليورانيوم المخصب في ايران.  لدينا عدد القنابل النووية الأكبر في العالم ونأمل عدم استخدامها.  ‏من يبيعهم سلاحاً نووياً سيُقصف هو نفسه، إذا باعوا سلاحاً نووياً، فقلة قليلة فقط قادرة على ذلك، ستُقصف.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/naya_foriraq/79132" target="_blank">📅 19:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب عن إيران: سوق الأسهم رائع للغاية. وفي كل مرة قلنا فيها شيئًا مذهلاً، مثل "سنقوم بتسوية الأمر"، كان يرتفع.   وفي كل مرة، في كل مرة قلنا فيها شيئًا سلبيًا، مثل، "خمنوا ماذا، لن نكون قادرين على تسوية الأمر"، كان ينخفض — بشكل كبير جدًا، كبير جدًا جدًا. …</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/79131" target="_blank">📅 19:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=bNpnWRYoCAEkAYGU0DbTWh5FtWZfbnSKj6mTwSPPbrGu-Qw8Iz1p3D_7oXOInHXXvO-7P0UiDVHpBkZrkJkfuJ4n6ADJeqJhxMkmF8SUgRpNzBU8LDHCwWv2eqOI_FKunJLFKM8_-CzZ2XTrNI61KsT5HMMJciL6IFlSrvIaX3MYPqegu_EhsdLwOuNID2rCkMNOsAqsS_sUbVk_vRri0JDRtGkAq9dKebxSrNN2Ay4zuqiSYxP5X0iTiQKdSkphtmTOZpmXdFAGN14f1fVl0xGCll9uTSp8SqKrdu6FY04O1e8NXQDgR9UOM7MNbw2hpA1Hua2CPIhotS6HnAo9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fd4976e9.mp4?token=bNpnWRYoCAEkAYGU0DbTWh5FtWZfbnSKj6mTwSPPbrGu-Qw8Iz1p3D_7oXOInHXXvO-7P0UiDVHpBkZrkJkfuJ4n6ADJeqJhxMkmF8SUgRpNzBU8LDHCwWv2eqOI_FKunJLFKM8_-CzZ2XTrNI61KsT5HMMJciL6IFlSrvIaX3MYPqegu_EhsdLwOuNID2rCkMNOsAqsS_sUbVk_vRri0JDRtGkAq9dKebxSrNN2Ay4zuqiSYxP5X0iTiQKdSkphtmTOZpmXdFAGN14f1fVl0xGCll9uTSp8SqKrdu6FY04O1e8NXQDgR9UOM7MNbw2hpA1Hua2CPIhotS6HnAo9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: نتنياهو ينفعل قليلاً أحياناً، لكنه كان شريكاً جيداً.  ‏نحن الشريك الكبير، وهو الشريك الصغير جداً.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/79130" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=axnQ25ELKrI194IU7LC3YWZAM5gRBv1LUYdQaUseMq5Odbv8SDiq__qtEG38KPEpnWuptDo2wxo4e_c1p5XNmqMv6BIzy83wCs5VnhIpK0sGNwlRdNuynv5tgQZFYeQ-AyiTsKaFXUvAiE5gqDyJo9kWGL6zHWnaNcuSpcM1DaJ3VmA4I6_Fa1cGMFL7DT2AsE9lZGCCy-_ZEWtPZLDZJvTYedLLVQ_EIEfIbwpkMyotnuPfsmM_2f0Dvr0Bu72YLheydGcsLuiDHk4JDp-iubryAJyRFtjKPm4nuhwYbmMJ4h18hgyWpRcdCQac9iLOOKD9ROu7VcDCpRw9lOHAMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5e46b9b2b.mp4?token=axnQ25ELKrI194IU7LC3YWZAM5gRBv1LUYdQaUseMq5Odbv8SDiq__qtEG38KPEpnWuptDo2wxo4e_c1p5XNmqMv6BIzy83wCs5VnhIpK0sGNwlRdNuynv5tgQZFYeQ-AyiTsKaFXUvAiE5gqDyJo9kWGL6zHWnaNcuSpcM1DaJ3VmA4I6_Fa1cGMFL7DT2AsE9lZGCCy-_ZEWtPZLDZJvTYedLLVQ_EIEfIbwpkMyotnuPfsmM_2f0Dvr0Bu72YLheydGcsLuiDHk4JDp-iubryAJyRFtjKPm4nuhwYbmMJ4h18hgyWpRcdCQac9iLOOKD9ROu7VcDCpRw9lOHAMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: أبلغنا الإيرانيين بأننا سنعود للقصف إذا لم يلتزموا.  ‏القادة الجدد لإيران أذكياء، بل أذكياء جداً. ‏إنهم أقل تطرفاً بكثير. أعتقد أنهم يحبون وطنهم حقاً. إنهم طيبون.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/naya_foriraq/79129" target="_blank">📅 19:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79128">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=PPRW0SO9FAxF6KgrvNmRkUhOFzf9OqIWseGqttfdgOKx_cLJ1HGQ_Ge1FwqvyqAqTRdpmMeh28El0-gt72xZvUY6-FQNmK19NOTZ1wo-Ef4el3KDUXJ9L2dm_cqewbxKAWZE67h3QKl_M6UCxmeOB45ic3RiRI3mQHJ6aSgqByZzgjW6g4cnvCklFeJXIQqAto8euij_BKsjTsZFltUfQypVFrhEQzfqA4POpP7xUVKqkM3jZNV0_7lnSYT7kmqGV-tJ2GpGKx-Gpetdo3KMssMHNEvX6Xb2dLlCQlUl63b5Gxo0yg-hM5TohABt40XtiuOw_TIWmwbKNfPXYb0FUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41cf81574e.mp4?token=PPRW0SO9FAxF6KgrvNmRkUhOFzf9OqIWseGqttfdgOKx_cLJ1HGQ_Ge1FwqvyqAqTRdpmMeh28El0-gt72xZvUY6-FQNmK19NOTZ1wo-Ef4el3KDUXJ9L2dm_cqewbxKAWZE67h3QKl_M6UCxmeOB45ic3RiRI3mQHJ6aSgqByZzgjW6g4cnvCklFeJXIQqAto8euij_BKsjTsZFltUfQypVFrhEQzfqA4POpP7xUVKqkM3jZNV0_7lnSYT7kmqGV-tJ2GpGKx-Gpetdo3KMssMHNEvX6Xb2dLlCQlUl63b5Gxo0yg-hM5TohABt40XtiuOw_TIWmwbKNfPXYb0FUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:  حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.  ‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.  أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.  ‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه -…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/naya_foriraq/79128" target="_blank">📅 19:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=UpYw4l_W3JtzGrtm8-G_O5Y1wuX4TV2fLbY6YKEN1Zy0jivp5f67r9npV2mnDEN29cBash5jI_7UsQnNOmnz-OTFrKqdxXRAaVd-LpNk9HzTn80BA-dxvqtIS2VYy1warpiNgV1LS0EwqlQThwZTQ8ze2zRqFcaS_-otxwIalp0yBKUpFP-Ubjnld4pXD7BBW8TKZoOVPc1oU8OxCoCFIq1_BxNGO_q8OuuQAU3cTAumzXeIId84TzXJmVTGJloo4Qp_cIT7YcieYU_fu_L4f_fSatf1kbIZFfapbDm7MXS-LJHEIqqfLZryRN_-YlN2_sDQl8puFDAiN1gDewu_0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68b83f5a15.mp4?token=UpYw4l_W3JtzGrtm8-G_O5Y1wuX4TV2fLbY6YKEN1Zy0jivp5f67r9npV2mnDEN29cBash5jI_7UsQnNOmnz-OTFrKqdxXRAaVd-LpNk9HzTn80BA-dxvqtIS2VYy1warpiNgV1LS0EwqlQThwZTQ8ze2zRqFcaS_-otxwIalp0yBKUpFP-Ubjnld4pXD7BBW8TKZoOVPc1oU8OxCoCFIq1_BxNGO_q8OuuQAU3cTAumzXeIId84TzXJmVTGJloo4Qp_cIT7YcieYU_fu_L4f_fSatf1kbIZFfapbDm7MXS-LJHEIqqfLZryRN_-YlN2_sDQl8puFDAiN1gDewu_0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترمب:
حققنا جميع أهدافنا وأنهينا النزاع الحالي بعد التوصل إلى اتفاق مع إيران.
‏لا يمكن لإيران امتلاك سلاح نووي أو تطويره.
أسعار النفط انخفصت لمستويات غير مسبوقة بعد الاتفاق مع إيران.
‌‏يوم الأحد، توصلنا إلى اتفاق مع إيران يحقق كل ما كنا نسعى لتحقيقه - كل شيء وأكثر من ذلك بكثير.
‏أعتقد أن القادة الإيرانيين سيتصرفون بشكل مختلف تماماً.
إذا لم نقم بهذه الصفقة، كان بإمكاننا إسقاط المزيد من القنابل لمدة أسبوعين أو ثلاثة أو أربعة أسابيع أو سنتين أخرى.
لو واصلنا القتال ما كان مضيق هرمز ليفتح إطلاقا.</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/naya_foriraq/79127" target="_blank">📅 19:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
مشروعهم في لبنان إنهاء حزب الله عسكرياً وثقافياً وسياسياً واجتماعياً وشعبياً ليسهل لهم ابتلاع لبنان، ونتنياهو أعلن صراحة أنه يريد إسرائيل الكبرى.
لم نمكن إسرائيل من تحقيق مشروع إسرائيل الكبرى فنحن كسرناه.
عدد آليات العدو المستهدفة 518 آلية وعدد الطائرات المستهدفة 85 حيث أسقطنا 12 مسيرة و12 محلقة وأصبنا مروحية.
لا وجود لمناطق صفراء أو حمراء وعلى إسرائيل أن ترحل.</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/naya_foriraq/79126" target="_blank">📅 19:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇷
وكالة إرنا: لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ…</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/naya_foriraq/79125" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
وكالة إرنا:
لا صحة لخبر إلغاء رحلة الوفد الإيراني إلى سويسرا كما جرى تداوله في بعض المواقع.تمّ صباح الاثنين وضع الصيغة النهائية لمذكرة التفاهم لإنهاء الحرب بشكل نهائي على جميع الجبهات، بما فيها لبنان. وفي هذا الإطار، ستدخل هذه المذكرة رسمياً مرحلة التنفيذ يوم الجمعة 19 يونيو/حزيران. ولا تزال آلية إضفاء الطابع الرسمي على الاتفاق قيد المراجعة من قبل الجهات المختصة في البلاد.</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/79124" target="_blank">📅 18:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dc2cjGdOlhAYX1dcSrcd7-ezHey2N3KeGKoOVLb6z79CLdHSp9H-hZiJ3zub-PxcqLpECNxc5fvn_qnTRHJa3kdPSd_rVzk6lshuKF7hqyPnpydxLi-LWta6BMbdOefhwElbCfFi29vheqtm7TMKT-5hmOpEXf0g6QnY7_G_ut5UvUHxaNWPwbIY1cAbNMYq8qZTjhv2lN386kmS2KM25zpHIBJBdy3POMuRW2e8K0-MJNB19LcJHjvglmxrm9R1griR7zwZ-mFmFPktpcqv_HwRmHXIjydt-UUd2WRU4UkZ7KA_sN_Zb2OJ1NNJtR8D6WCsuA6Fi8LQffIVnDwskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
الغاء رحلات جوية من مطار النجف الأشرف في العراق إلى عدد من المدن الإيرانية دون معرفة الأسباب.</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/naya_foriraq/79123" target="_blank">📅 18:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
حدث أمني في جنوب لبنان وإجراء عملية إخلاء لعدد من جنود الجيش الإسرائيلي.</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/naya_foriraq/79122" target="_blank">📅 18:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=ZWIMYj1_xREGh-6Wl3REJmcPjLa-bdxm1J7Di2zib2P2eMEgD9qBzFP-36o3jXrXND5IImnSbddIZcMbWjOcTy83tkzDll82oMZY8Nehd26cIb289lPjvouT7nRxHSWfN816LNDuL-HQpWk60Uc6wpDESjHvZl76OINbofT1gLODrEa0YAMqmwvCcfmL0YQTL-sRxVYu2eTBiIDcSEjnJiIKGsrdFGdSuXDoh8HjeqJI3gpm61gWA-dqbSRHYjNbrO-yaTKpFJio0ptGfRoKkZKZiU3agVnl0NB8ssqHLAGwOYbbobUC_DhYZE8hw2y532ydYNYtdTo0S5N3w-yC_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41129f47e0.mp4?token=ZWIMYj1_xREGh-6Wl3REJmcPjLa-bdxm1J7Di2zib2P2eMEgD9qBzFP-36o3jXrXND5IImnSbddIZcMbWjOcTy83tkzDll82oMZY8Nehd26cIb289lPjvouT7nRxHSWfN816LNDuL-HQpWk60Uc6wpDESjHvZl76OINbofT1gLODrEa0YAMqmwvCcfmL0YQTL-sRxVYu2eTBiIDcSEjnJiIKGsrdFGdSuXDoh8HjeqJI3gpm61gWA-dqbSRHYjNbrO-yaTKpFJio0ptGfRoKkZKZiU3agVnl0NB8ssqHLAGwOYbbobUC_DhYZE8hw2y532ydYNYtdTo0S5N3w-yC_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇳
‏ترامب: سنساعد الهند إذا تعرضت للهجوم.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/79121" target="_blank">📅 17:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1QFlkaLyr82uz4-tuGkdVKrPysE2u54pYfAsTNf_cSbn7qkVEldFVRW9Wmy0JOpzdwRbSehDky0CBcfYK37lt7SBMV9IyPxeBJFsL_zeUHx6jRV9Uk-jOVEwvySh-tJdr17mjYILB1vJOJayb7S8ud9mjfJbRKj6g036UVL4pmpxDUVNCi8nEaR10hQV1MBTWdPo29WUoHMkgchZIrTTfWSkKHoz5Thc72nCDiD0hiPDep9eUjZ_hX_xMjFa_AgVgaiKAAMOnH8MU15wvQ_uaJTmfGplrO0V8oTbqqsbGbQ6VoljQZth3C_glG7XNfbXB6PygtklSwMCDlVIzqRd3sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df442586ac.mp4?token=G37Zu40YWb2o0pU_shzOKm-QKVCC0TkWVKyzKiD3yNp_Lcz3pgJjGhgfrlhcL7JhGRhZ1Ltvvlh-1OAQU6qtpNgIMouLjhz3AlBTRClldv8-iI1uPzOjv8F0j73Rjh7LW8OLk1YTCOpU0KrxpOraKUcMyALZ2w7-pMocYQf-didBE3xCfealA_hTkzFy4BOLHViy2GsCjF_2S9Lq5MPaZ89yYGk3sEdpVJNpNTpFtNHi41dQrTOL_ffCXXbkD3u97s0tg3lgrSmnvB8um_EqIuMw9MMA8qAh0UdZRPnTWmrIxA07n2qDKRXnA3zW-rQWQyI8fq-nU34HdakHNgLb1QFlkaLyr82uz4-tuGkdVKrPysE2u54pYfAsTNf_cSbn7qkVEldFVRW9Wmy0JOpzdwRbSehDky0CBcfYK37lt7SBMV9IyPxeBJFsL_zeUHx6jRV9Uk-jOVEwvySh-tJdr17mjYILB1vJOJayb7S8ud9mjfJbRKj6g036UVL4pmpxDUVNCi8nEaR10hQV1MBTWdPo29WUoHMkgchZIrTTfWSkKHoz5Thc72nCDiD0hiPDep9eUjZ_hX_xMjFa_AgVgaiKAAMOnH8MU15wvQ_uaJTmfGplrO0V8oTbqqsbGbQ6VoljQZth3C_glG7XNfbXB6PygtklSwMCDlVIzqRd3sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل: هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب: نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/naya_foriraq/79120" target="_blank">📅 17:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">المجلس الإسلامي الأعلى في العراق:
استجابةً لنداء الوفاء.. بلدية طهران تُلبي مطالبات المجلس الأعلى وتشهد بغداد تشييعاً مهيباً للقائد الشهيد الامام الخامنئي*
استجابةً للمطالبات والنداءات الروحية والوطنية المتكررة التي أطلقها المجلس الأعلى الإسلامي العراقي، وتأكيداً على عمق الروابط الوجدانية والجهادية التي تجمع الشعبين الأبيين، أعلن رئيس بلدية طهران رسمياً عن تلبية هذه الدعوات المباركة.
حيث تقرر أن تشهد أرض العراق الطاهرة ،أرض المقدسات والشهادة مراسم تشييع جثمان القائد الشهيد، الامام الخامنئي، وذلك في تاريخ 8 تموز (يوليو) 2026.
وتأتي هذه الخطوة التاريخية تلبيةً لقلوب العراقيين التي نبضت بالوفاء لقائدٍ عاش مدافعاً عن قضايا الأمة، ليمتزج تراب العراق بفيض وداعٍ مهيب يليق بمقام القائد الشهيد، وسط ترقب واسع لمشاركة ملايين المحبين والمقاومين في هذا الوداع الأخير.</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/naya_foriraq/79119" target="_blank">📅 17:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13deced209.mp4?token=SuTYJibOMadK1mb_bh_Oju1Vo3KSciVJNpdmZ1MJtzpo39LuajjcUwGjKRvI9HUilraUD7Qp3wpfrAomA-4WGM8CLDhUFRg4VkVylh2otMwrMBK9sbiwCsORirV6PcSyyBa7KdCxDg1YkKtSngifMsZgtaIuFg7xbP4mDONJ0_oeJS15viz_sEXLkJrQwe5eUR5_suDia57xET9lFIDwSV3hgHA7FKZiC82weJ9jsS9P2rHouMtmDQhBSHfpbaG0xDmYkHsJ3qwoVFRoAui8NkaV7hBEIEjQcwSTt1hibZzK2ygm9qWuyrrqP1N7U5INSdzfbKcKVb_efQHYeHB3xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13deced209.mp4?token=SuTYJibOMadK1mb_bh_Oju1Vo3KSciVJNpdmZ1MJtzpo39LuajjcUwGjKRvI9HUilraUD7Qp3wpfrAomA-4WGM8CLDhUFRg4VkVylh2otMwrMBK9sbiwCsORirV6PcSyyBa7KdCxDg1YkKtSngifMsZgtaIuFg7xbP4mDONJ0_oeJS15viz_sEXLkJrQwe5eUR5_suDia57xET9lFIDwSV3hgHA7FKZiC82weJ9jsS9P2rHouMtmDQhBSHfpbaG0xDmYkHsJ3qwoVFRoAui8NkaV7hBEIEjQcwSTt1hibZzK2ygm9qWuyrrqP1N7U5INSdzfbKcKVb_efQHYeHB3xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
المراسل:
هل تريد من الأوروبيين إرسال كاسحات الألغام إلى مضيق هرمز؟
🇺🇸
ترامب:
نحن لا نحتاج إليها، لكن إذا أرادوا إرسالها، فهذا أمر جيد.</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/naya_foriraq/79118" target="_blank">📅 17:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
الأمين العام لكتائب حزب الله:
بسم الله الرحمن الرحيم
(يَا أَيُّهَا الَّذِينَ آمَنُوا إِن تُطِيعُوا فَرِيقًا مِّنَ الَّذِينَ أُوتُوا الْكِتَابَ يَرُدُّوكُم بَعْدَ إِيمَانِكُمْ كَافِرِينَ * وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ آيَاتُ اللَّهِ وَفِيكُمْ رَسُولُهُ ۗ وَمَن يَعْتَصِم بِاللَّهِ فَقَدْ هُدِيَ إِلَىٰ صِرَاطٍ مُّسْتَقِيمٍ * يَا أَيُّهَا الَّذِينَ آمَنُوا اتَّقُوا اللَّهَ حَقَّ تُقَاتِهِ وَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسْلِمُونَ)
مع اطلالة شهر محرم الحرام ودخول أيامه المثقلة بالأسى والبطولة، حيث تجسَّدَ جهاد الإمام الحسين (عليه السلام) وأهل بيته وصحبه بأوضح صوره في طف كربلاء، وأثبتوا فيه أن «الجودُ بالنَّفْسِ أَقْصَى غَايَةِ الجُودِ»، لتبقى تلك التضحيات العظيمة منارةً تضيء درب الأحرار في كل زمان ومكان، وتعلّم البشرية جمعاء أن الحياة بلا كرامة لا قيمة لها، وأن الثبات بوجه الطغاة أمر إلهي لا يجوز تركه أو الحياد عنه مهما بلغت التضحيات وعظمت البلاءات.
وامتداداً لهذا النهج الحُسيني الخالد، ننهي جولةً أخرى من جولات الحرب ونخرج منها بانتصار ناجز، وندرك تماماً أن المعركة لم تنتهِ بعد، وأن أمامنا جولات ومحطات هي أكثر خطورةً وضراوةً؛ لذا، يفرض علينا الواجب والوعي أن نكون على أهبة الاستعداد لأي طارئ، متمسكين بسلاحنا، وأيدينا على الزناد.
إن هؤلاء الأعداء من الوحوش البشرية لا يمكن الوثوق بعهودهم أبداً، وأن التغافل عن مكرهم هو الغباء بعينه؛ فالمعادلة واضحة: لن يرضوا عنا ولن نرضى بظلمهم، فكيف نرضى عنهم وقد قتلوا إمامنا الخامنئي في وضح النهار وبين ظهرانينا، وقتلوا العبد الصالح عروة المجاهدين الوثقى السيد حسن نصر الله، واغتالوا علماءنا، وحصدت آلتهم الإجرامية أرواح عشرات الآلاف من شيوخنا، وشبابنا، ونسائنا، وأطفالنا في غزة، ولبنان، واليمن، وإيران، وسوريا، والعراق؟!
فأيُّ صفحة تُطوى؟ وأيُّ جريمة تُنسى؟ وأيُّ مجرم يُسامح؟! لا سامحَ الله من يسامحهم. إن قتالنا مع الباطل ممتدٌ وفي معارك صفرية تطيح بها الرؤوس وتحذف فيها دول، ليرتسم من خلالها عالم جديد، ونحن نعلم يقيناً أيَّ عالم نريد؛ عالم تسوده العدالة والكرامة وتتحطم فيه عروش الظالمين. إنها معركة الحق ضد الباطل، ولن تنتهي حتى قيام الساعة.
أما أولئك الذين وقفوا مع الخنازير وأبناء القردة، فعليهم أن يترقبوا أمر الله وحكمه فيهم، فلا نامت أعين الجبناء والخونة، وأنّ خدعة (الصفحة الجديدة) لن تنطلي علينا، (يُخَادِعُونَ اللَّهَ وَالَّذِينَ آمَنُوا وَمَا يَخْدَعُونَ إِلَّا أَنفُسَهُمْ وَمَا يَشْعُرُونَ).
وفي الختام، نتوجه بآيات الفخر والاعتزاز والامتنان إلى صناع النصر وبناة المجد:
شكراً لحزب الله، درة تاج المقاومة الإسلامية وعنوانِ عنفوانها.
شكراً للقوات المسلحة الإيرانية الشجاعة.
شكراً لرجال اليمن، أهل الصدق والوفاء.
شكراً لكل أبناء المقاومة الإسلامية في فلسطين، والعراق، والبحرين، وأرض الحجاز عامة، وخاصة أهل الشام.
وشكراً لمجاهدي التبيين الذين أبلوا بلاءً حسناً في معركة الحق، ولكل الأحرار من سياسيين، ورجال عشائر غيارى، وعلماء دين مخلصين، وإلى شعوب أمتنا الإسلامية الذين نصروا قضايا الأمة العادلة، مجسدين أسمى معاني التضامن والوحدة في هذه المرحلة المصيرية.
وعظيم الامتنان والتبجيل لمراجعنا العظام الأعلام، الذين وقفوا موقفاً تاريخياً، مشرفاً، شجاعاً، وواضحاً لا لبس فيه؛ فبيّض الله وجوههم في الدنيا والآخرة كما بيّضوا وجوه الأمة، وجزاهم الله خير الجزاء عن الإسلام وأهله.
﴿سَلَامٌ قَوْلًا مِّن رَّبٍّ رَّحِيمٍ﴾
الأمين العام لكتائب حزب الله
17 حزيران 2026 ميلادية
الموافق لـ  1 محرم 1448 هجرية</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/naya_foriraq/79117" target="_blank">📅 17:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrNGAJ-4HrITZTNtaL922B4hkiA4TCYj7x-Vvw6-xuzEeLMbk84AoOCkmmn7czd5XO0TBFQnYzMNlvPBkTyav8zXEjIhChsDIk9WIYsbixwCaeYbZgunOpX32WhPioguTHgbQKys8V1cMhu81NyY-6PGSQjhsNsoEYB_SORyqNkiPMMMGHUGrZnTkRjkzkKd6jeCglHb3fJ0m5zKWtOdjPHVuz-iELy8N0OOzCWL0LzehHQw9YjcA-vZgzp5JpDUC3Wb14A_XXu59_D_UhXT3BlXONAgTUkeoT9V3RfoVMTOWugL9Livp4W5YqeCip8vrYLKH6c__JrzizW3Uj-_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب:
سأعقد مؤتمراً صحفياً خلال 45 دقيقة من فرنسا. ثم سأتوجه إلى فرساي لتناول العشاء مع القادة الفرنسيين والأوروبيين الآخرين، ثم أعود إلى الوطن الليلة! كانت الرحلة ناجحة للغاية، ولكن ما أراد الناس التحدث عنه في الغالب هو حقيقة أن إيران لن تمتلك سلاحاً نووياً، وأن مضيق هرمز سيُفتح على الفور! أرقام رائعة في جميع فئات اقتصاد الولايات المتحدة مع عدد أكبر من الناس يعملون اليوم أكثر من أي وقت مضى. يتم استثمار أكثر من 19.1 تريليون دولار في الولايات المتحدة الأمريكية مع المصانع وكل شيء آخر يحدث، ولكن الأهم من ذلك، أن أرقام سوق الأسهم الأخيرة مرتفعة للغاية بسبب التسوية، وبالمثل، أسعار النفط تتراجع</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/79116" target="_blank">📅 17:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">جيش الإحتلال الإسرائيلي يعلن اصابة 5 جنود صهاينة في جنوب لبنان</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/naya_foriraq/79115" target="_blank">📅 17:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79113">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4504333bd3.mp4?token=V7Sx11IYf3mS1hfXE91HsfoMIWjOv7pRLL9nrKb8sdsZuTHmvHPzM2iSZ6yvvUYZI__U0_23cPVo14c0YfLlVk3urU2VyGvibQd1iGN2mDUobNxs3cfWNK2nXT8nSW-f7u1PQ0JPohitRgWHEaky_TP4agRHTGVI-rKWQ16_ry0-x-TWnbSdGlrQ6IIjSqgFh89Vo5JALbrLRV9efiZ8R8vM5grkuo0gZb9g1QZdlZs-QkC3ZW27Jf8299EVqwcsdbsW-7sz8ipTOBbjM7PrKQWigCEW0gkuBS054aLszpby6KqNEDNoMOTJCNUpEAyOyqr8RNBjHJ8u0awEzu8doA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا...
🌟
🇹🇷
الجيش التركي سمح بعودة سكان 25 قرية في منطقة باتيفا بمحافظة دهوك شمالي العراق ضمن إجراءات تنظيمية شملت فرض قيود على حركة السكان.
🤔
و تضمنت الشروط منع التجوال من الساعة 6 مساءً حتى 7 صباحاً وتقييد الحركة داخل القرى وحصرها بالطرق المحددة…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79113" target="_blank">📅 16:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79112">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/naya_foriraq/79112" target="_blank">📅 16:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79111">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نائب الرئيس الأمريكي: نص مذكرة التفاهم مع إيران سينشر يوم الجمعة المقبل على أقصى تقدير</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/79111" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79110">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=nJM1AAZ5n9VF_P-iUJzx971aEBk4xgt63PXPphKagVDuYk9lJGmEfzP0NZeG0TzB4AHAjrkfoMu62pYpklKcRCJiFVF1p-3_hzhbq_DG-tKsuFXLtCT78mRj7NhTT5DKAiqOyqHiAWQISjRU5y8GB0hYbYE8Dzm1F3SuN5wTwC5GJ_fJ4o7Pa05mcQpa9Idm5yR_45SZGNWjMdHdW29UEpfVPu2w6p0dazeL8ueExl-IL--CtwZUX8NMF11SsAMrqhYy_3U8-b0MF4x0cFsG0--Ag4f6ZqJp11Ugo_uhi7f7GuMEaRumZsue-b6x05aW8lA-uPv6DcCYbcnzKFnLnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf841e5ce1.mp4?token=nJM1AAZ5n9VF_P-iUJzx971aEBk4xgt63PXPphKagVDuYk9lJGmEfzP0NZeG0TzB4AHAjrkfoMu62pYpklKcRCJiFVF1p-3_hzhbq_DG-tKsuFXLtCT78mRj7NhTT5DKAiqOyqHiAWQISjRU5y8GB0hYbYE8Dzm1F3SuN5wTwC5GJ_fJ4o7Pa05mcQpa9Idm5yR_45SZGNWjMdHdW29UEpfVPu2w6p0dazeL8ueExl-IL--CtwZUX8NMF11SsAMrqhYy_3U8-b0MF4x0cFsG0--Ag4f6ZqJp11Ugo_uhi7f7GuMEaRumZsue-b6x05aW8lA-uPv6DcCYbcnzKFnLnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79110" target="_blank">📅 16:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79108">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">الحكومة السويسرية: توقيع مذكرة التفاهم سيعقد بمشاركة ممثلين رفيعين عن الولايات المتحدة وإيران وقطر وباكستان.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79108" target="_blank">📅 15:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79107">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79107" target="_blank">📅 15:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79106">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_PhJsqz0OKWpNgLGHIDUIllsGLyqevKAQ6zCgeuaxXuowQw2_YuLRmIbFAEpUiuIxcgufcb_DFfgNQ4iIihhK1t9jJIRIzzT5Dyem-ipgG0-YWIRPcAlQXI-FzIeFaRb3BM8K3TCChpmCDlgGWDik1UKSUscgn51OEjwrBeQSHYOjUAeaI9Uq06xeHzYQOd9Ag9phurKuw5TErpKEn-NZ0UFpRDO7QJ8AlyEYKSJwLw15KtjnllJNu3zxnIh2_bV7tg0swlgKusTWt-fiXePAOJpRumxWjmI7YT-yK0oOTQ4E_uOKcKAxsxlTYuGIvcYTVPl8bllfa9Qz9EHNi1vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختفوا وابتلعتهم أربيل
!
العشرات من شباب الوسط والجنوب بسبب باج معهم من الحشد الشعبي او صورة لسيد حسن بالهاتف او الشك فقط او العثور على اسمائهم ضمن قوائم رواتب الحشد الشعبي ادى الأمر إلى اختفائهم ، وسط صمت مخزي من القوى السياسية الشيعية الشريكة معهم في الوزارات وتقاسم الكعكة
المواطنون يناشدون الشيخ علي الزيدي مدير الامن والانضباط
بالحشد
و قادة الإطار التنسيقي ومن لا نزال نحسن الظن بهم لا سيما الشيخ
همام حمودي
و
إلحاج العامري وسيد قاسم الاعرجي لمتابعة امر المعتقلين الذين تجاوز عددهم ٧٠ شخص حتى اللحظة
!</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79106" target="_blank">📅 15:52 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79105">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">#ترفيهي
الرئيس اللبناني:
لا خوف على السلم الأهلي ومن يهدد به أصبح ضعيفا وهو يبغي إخافة الآخر ليبقى موجودا</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/79105" target="_blank">📅 15:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79104">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a50e9b741.mp4?token=v2buw2sXuU61LmmgO6oOmIF9pj0KXDpifbKp5preLQgVjjGq3nTUHNH_fnzXgE3amMgmbk9ExwF9RSliPz1vAN57l3LVQ99EEwOyzXmJ6IuCeVqk6iPE_QQbgVmqe7ejOTzr6dk4iTPbuM_aQbwU541Nkaeq9Ew0mwONGSWyiciSTV_nBQ42BAkMNHj3K4BJHDItl5MJvUVhYkGZb0fs3HBKjeOkoHzaxVZb0BFYeW02ktNd_1Ke8V5PazWlZ4bb86_5KJiH2DXL189vcuY-E2FBerxzXKbynxRqtUtPEx6rdCAsvtUNj811cIZDowPGxT7Z9jbiaAWCPMrZnOvtTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
🇺🇸
تنفرد نايا بنشر مشاهد في حرب رمضان من مدينة إيلام الحدودية مع العراق تظهر انطلاق صواريخ توم هوك كروز مرورا بسماء العراق ؛ الصواريخ رصدت حوالي الساعة 8.50 بتوقيت العراق …
يوم ٢٨ فبراير</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79104" target="_blank">📅 15:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79103">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
محكمة جنايات النجف تصدر حكما بالسجن الشديد 4 سنوات لمدير مؤسسة السجناء السياسيين في النجف</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79103" target="_blank">📅 15:04 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79102">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇷
🚨
السلطات السويسرية تغلق المجال الجوي فوق منتجع بورغنستوك بشعاع 46 كم ضمن سلسلة اجراءات لتأمين توقيع الاتفاق الايراني الامريكي</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/79102" target="_blank">📅 14:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79101">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇸🇾
🇺🇸
ترامب: تحدثت مع الرئيس السوري حول إمكانية القتال ضد حزب الله.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/79101" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79100">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران: النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/79100" target="_blank">📅 14:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79099">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامب حول اتفاقه مع إيران:
النص ليس نهائيًا؛ إنها مذكرة تفاهم. إذا لم يعجبني ذلك وإذا لم يتصرفوا بشكل جيد، فسنعود مباشرةً إلى إلقاء القنابل في وسط رؤوسهم</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79099" target="_blank">📅 14:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79098">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🌟
ترامب يواصل جعل نفسه اضحوكة للعالم:
أتابع كأس العالم وأرى دولاً مختلفة من شمال أفريقيا مثل المغرب والجزائر وتونس ومصر. إنهم موهوبون وسريعون للغاية، لكنهم منفصلون. تساءلت: لماذا لا تتحد دول شمال أفريقيا لتشكيل فريق واحد كبير؟ لو فعلوا ذلك، لفازوا بالبطولة بسهولة! هذا يعكس نقصاً في القيادة هناك. ربما بعد أن ننتهي من إنقاذ أمريكا سأذهب وأترشح لرئاسة أفريقيا ، سنربح الكثير!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79098" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79097">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇮🇷
🌟
الجمهورية الاسلامية تحتفي بطفل عراقي باع دراجته الهوائية وتبرع بثمنها نصرة للحق على الباطل</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/79097" target="_blank">📅 14:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🇮🇷
التلفزيون الإيراني:
3 ناقلات نفط إيرانية تبلغ حمولتها 5 ملايين برميل من النفط الخام عبرت مضيق هرمز</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/79096" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79095">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=YFWdSiIAuKYdCrMxvo1mXYQgdTunAhSeSLR8Mnp00OgY2eL3JV9oPgU0mM5-beDlXYEAH6Fj4I57wLwOVggZHwDuOGeDN6HE4wVChxD3z93f8as4_FLHFPKVN3RcamFwWLedL96Owvo_LJEHvivOAoQUl_QIrkT64-eX7b8VpRaqpHk4dc1S7HHav8NDwfL1e1wN152syKI7hgRfhAUe1hFZcKBO0LsMlQhfqQBAqylvrJN9orWVfTm7t5y9sLvew5Vw9hCM4rjgEnfoQ6IyqgjtxsMcOpOejAABvxNblD4MqDrU886EAkEsmwbf-BgKu496ff-AXcDHYo7dQ_XuxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7120c31b.mp4?token=YFWdSiIAuKYdCrMxvo1mXYQgdTunAhSeSLR8Mnp00OgY2eL3JV9oPgU0mM5-beDlXYEAH6Fj4I57wLwOVggZHwDuOGeDN6HE4wVChxD3z93f8as4_FLHFPKVN3RcamFwWLedL96Owvo_LJEHvivOAoQUl_QIrkT64-eX7b8VpRaqpHk4dc1S7HHav8NDwfL1e1wN152syKI7hgRfhAUe1hFZcKBO0LsMlQhfqQBAqylvrJN9orWVfTm7t5y9sLvew5Vw9hCM4rjgEnfoQ6IyqgjtxsMcOpOejAABvxNblD4MqDrU886EAkEsmwbf-BgKu496ff-AXcDHYo7dQ_XuxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: لقد قضينا على رجل يدعى سليماني. هل تعتقد أن هذا كان سيحدث لو كان على قيد الحياة؟ لقد كان عبقرياً</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/79095" target="_blank">📅 14:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79094">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=H0u8C90G34sQhaWAB4-NxauJc6ePF8edVenp2TKWOKgOZQTuppz1DGfnGSeOjYhey9ZTrWyfwosx9FQS6-bnwhPjcZ94I1kb4GU6dqhgRr1bX-bj1e7Y9gSv-941OeAFk_Zkkzhyx6M3nX-3x6SYItJqenzJf9V0YKWUszxKL1CSW4-7A7B4cmcD5Isky2ne8kgS8Mx-1RWkRMHzxM7f_w3sYgCg-EqyCPz9WDxRQf3VHalhWfaL76Jxrj8ZsBHXWnVuX0yBVkeZmydMF86Lmn9i_hhXslqK0fjKcnbMpLBrDW6Q-IaH5B2YQQpL454t0pNvKUBLT0oJkdvFG5C_Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4487321f0.mp4?token=H0u8C90G34sQhaWAB4-NxauJc6ePF8edVenp2TKWOKgOZQTuppz1DGfnGSeOjYhey9ZTrWyfwosx9FQS6-bnwhPjcZ94I1kb4GU6dqhgRr1bX-bj1e7Y9gSv-941OeAFk_Zkkzhyx6M3nX-3x6SYItJqenzJf9V0YKWUszxKL1CSW4-7A7B4cmcD5Isky2ne8kgS8Mx-1RWkRMHzxM7f_w3sYgCg-EqyCPz9WDxRQf3VHalhWfaL76Jxrj8ZsBHXWnVuX0yBVkeZmydMF86Lmn9i_hhXslqK0fjKcnbMpLBrDW6Q-IaH5B2YQQpL454t0pNvKUBLT0oJkdvFG5C_Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: الإيرانيون خدعوا أوباما وحصلوا على المليارات من الدولارات</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/79094" target="_blank">📅 14:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامب: إثيوبيا عاملت مصر بطريقة غير منصفة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79093" target="_blank">📅 14:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6DLtmsTaO3a6p93TmnM6kBG7qrG3qy5M2lJzJm19h87O9kkpYpBsaLqCMs-QJUJo9t8vV9yFvRGTCFqjy1Rsk1Jl1yNQmD486Z_uiQQ9Qc1qNkqaRYm9IM8lncel6BXiF1it9lGMfC73II5OasYYG0JvhD7lzDlTMILi0CEkGyrKUro15J5THYVo0ODc8EX9YQnubMauXGBOz-rBU1p_6WzJVxQTsqtAg01j6NGoVthNy_AHqGs0szuD9b3zms76RwJmGiPgx8sLKj6_rsCKXoS_-NTzjxdn3ytOJP7I5ALfKY1Oi_EqNjrv1lwa5g6Do4mZikwe7oaogyfYDs1OXBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00afa6948.mp4?token=OuasFh2D3zIFa3Qf84l-2J-Db4j4-yQcQ0UChUPIbayBwK0t9R9lfDkgca9y_2AzraNLjWvhWnOyRS27bHAAcVKQJ_2qxNp18U-ThRMozASGUyd50ClIX8nYZkPlsVczU_fp_CA4L_K-knMvO5JXMTDDzLW7FbP_D5YIhzH8DoU3ut7e9yJ4-QRjbRIQOgMZr-TjGVu8EJy-tIqV2IvgkqsHioB7n-_pi9KWaVJM2PL406siS7YM2bAlsobSDDT_u49B1r24P6v9lZKS6t7azubxMzushhp0DMFoCK1i2x1EzlELVTlFbvLWchuX6NWPKcd3W7S0EJ-nCT5jmQCk6DLtmsTaO3a6p93TmnM6kBG7qrG3qy5M2lJzJm19h87O9kkpYpBsaLqCMs-QJUJo9t8vV9yFvRGTCFqjy1Rsk1Jl1yNQmD486Z_uiQQ9Qc1qNkqaRYm9IM8lncel6BXiF1it9lGMfC73II5OasYYG0JvhD7lzDlTMILi0CEkGyrKUro15J5THYVo0ODc8EX9YQnubMauXGBOz-rBU1p_6WzJVxQTsqtAg01j6NGoVthNy_AHqGs0szuD9b3zms76RwJmGiPgx8sLKj6_rsCKXoS_-NTzjxdn3ytOJP7I5ALfKY1Oi_EqNjrv1lwa5g6Do4mZikwe7oaogyfYDs1OXBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">"انا الزعيم "..
هكذا قال ترامب لقادة مجموعة السبع بعد وصوله متأخرا !</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/79092" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/79091" target="_blank">📅 14:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ترامب:‏ أدرك أن سد النهضة يؤثر على مصر.. نحن نعمل على حل أزمة سد النهضة</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/79090" target="_blank">📅 14:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79089">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gV_3An9fvrnIvlcdy7t0Rb0t8TS7LTj_ddTd1QsaQtCgA-YcpplBzBLbboWHNhVFahMM9aAj9cweTfbCEWLkoaSgf4dl1YX7tKhhJ_ksNze2CK4xv_uzW8GU1MjTBVHK5wg8gns15UsaHT7UAKCE-8SXuJign6XHETjDpuidi1LacqLlb-Qy-RkZLC8sJ4APxrOzUCuvYLRm9XhmXdFHQWDyBiY7gHN_lcBFYbYNOX2p30JrwdDpapf0N77TNU4oDBzq2AivEUnk4CyYt8m4mAjqq7opfk6SHoIdr82HRlFjxi0YXZCn49xLlznAXmTWkIr4pWd0oYevk8yf63nMHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترامب
:
وافق الجمهوريون مع الديمقراطيين على إبعاد ويليام بولت، وهو شخص موهوب وعادل للغاية، عن منصب مدير الاستخبارات الوطنية بالإنابة (DNI)، مقابل حصول الديمقراطيين على موافقتهم على قانون مراقبة الاستخبارات الأجنبية (FISA). لكن الجمهوريين تحركوا بسرعة كبيرة في جلسات الاستماع الخاصة بجاي كلايتون العظيم، المدعي العام الحالي للمنطقة الجنوبية من نيويورك، بحيث كان بولت سيغادر منصبه قبل أن يصوت الديمقراطيون على قانون FISA.
والآن يقول الديمقراطيون إنهم سيصوتون ضد قانون FISA. وبالتالي، كان الجمهوريون سيفون بالتزامهم، لكن الديمقراطيين هم من نكثوا بالاتفاق.
بالإضافة إلى ذلك، يجب أن يتم اعتماد المدعية العامة المرشحة حديثًا، جيمي ماكدونالد، والحصول على موافقة ما يُعرف بـ”الورقة الزرقاء” (Blue Slip). وبسبب المواقف غير المنطقية للجمهوريين بشأن هذه الآلية (مع أن الديمقراطيين غالبًا ما يكونون مستعدين لتجاوزها)، فقد لا أتمكن من الحصول على موافقة جيمي، الشريكة الاستثنائية في شركة Sullivan & Cromwell، ولا أريد إبعاد جاي كلايتون عن العمل الرائع الذي يقوم به حتى تتولى جيمي المنصب.
لذلك، ومع إضافة هذا التعديل البسيط، ومن أجل مصلحة الوطن وشعبنا، لن أوافق على قانون FISA ما لم يتم تمرير قانون SAVE AMERICA ACT معه أيضًا.
الأمر ليس معقدًا. في الواقع، وقع الجمهوريون في فخ.
وفيما يتعلق بالموافقة على الوطني العظيم جاي كلايتون، فإننا نلغي اليوم جلسة الاستماع الخاصة بتعيينه مديرًا للاستخبارات الوطنية، ولن نمضي قدمًا بها حتى تتم الموافقة على جيمي ماكدونالد كمدعية عامة للولايات المتحدة.
وفي هذه الأثناء، سيبقى بيل بولت مديرًا للاستخبارات الوطنية بالإنابة</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/79089" target="_blank">📅 13:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">في تصرف مستفز وخسيس..
قناة AVA الكردية التابعة للبرزاني والتي لديها مقر في بغداد تحتفل بخسارة المنتخب العراقي في مباراته الأولى بكأس العالم عبر بث الأغاني وإظهار أجواء الرقص والفرح داخل الاستوديو!
علما ان المنتخب العراقي يعد اكثر منتخب في العالم يضم لاعبين اكراد ويحترم حقوقهم في الوقت الذي تحرمهم البلدان التي يتواجدون بها من ابسط حقوقهم مثل تركيا ووصلت في بعض البلدان الى سبي نسائهم مثل سوريا الجولاني</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/79088" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن: - طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات - طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد - طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/79087" target="_blank">📅 12:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tnqyu1-jo4N2z4IUP8QXULcVz8nAGH7XhlvsoK7g987kRlqdUJ7SP-DdB5QXUBdpOdwmSPIVXw5za-1KSPrNCV6DqpoyfDj-Pv5dE3MSMJzuKjzwd7b1HDS4gcf023N4xUit1v1KBV8mEx3da6nxp-strX8Y5u-inXPkdUti8qtwxRNs_P5eLLSq5ARszxk-sSJShORfM2JavSU-SnX1LG2n39RvBRPk5DsOCF1qDl-JEjARWR2_KHM85yMzBbRx1GJrvnv7wakFD-oTyH7quSS-JtBAoHPDEBguneGB0FTo1lYQexZOLjFMP0CG3BUyEN21JZ51RUMzqYElLriZWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇺🇸
سفير أمريكا في الكيان المحتل:  الفكرة: ترحيل كل أعضاء حزب الله وحماس إلى "السفينة الأم" في إيران.. النتيجة؟ لبنان وإسرائيل خاليان من وكلاء إيران الإرهابيين. امنح السلام فرصة!</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79086" target="_blank">📅 11:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=hxajsP0XkLbFIhSf5DHLILnI6D8GFIJSrJcYEbkRceLzLwVWgxpA2s-HcO2rKCzBFmNSAjLdbUWoVDthM9FUpPA7Hxo8T2drphz8SUjlbADX9ieDKY7iw3C3aAA7tWIz2kVHizw5PQ631OppbFEzkLn9IWMvq0N4WnhUpuf6TObxR_p47uinaFkxFZybCmZroSm-t81JMf6V3UgDUYimev5ssFEwNrYNiDwZ-VA4gqRgyWBJG6a4VU-s5Z6fIj0wFsl_YlI8nTpZRQW5b62RrA8U85Y5UhkF1UssJnw-bWlGBcZhLsKVh1a58SFCNAbtozvle21V_nRGlJd_G3UuWwg_k_yTAx2JXwWxsv6HoCk63oe8FKo9LKT2q4__I0oP8a_1HBwlhU6t6JLmdVqhZigwDdlV-vTND6OFJlqjyUarf_qJGichXV21n0DiBbiAz18j6KPQ2T7rc5AA1QleDf9dDnmA2R3S2VkphA-a1Ryd5w2n0T0P9Ga9fX8_tVKQtW1wEngGc4WMJAkdoLWAdeN6L1L7X8U3O-i03I4GxHfbZukxHCn0xeyOD1W2_f61E4IxQoXa0h5IjQhBK9577X9F2kbDcDKo80cJW5nUq0dvnwUVlfVNZa8cENmQQYIc9Br9aryOoxuS0GNcBMtHUhL9aukmDau11yP6U0bsu8o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d8bb2548a.mp4?token=hxajsP0XkLbFIhSf5DHLILnI6D8GFIJSrJcYEbkRceLzLwVWgxpA2s-HcO2rKCzBFmNSAjLdbUWoVDthM9FUpPA7Hxo8T2drphz8SUjlbADX9ieDKY7iw3C3aAA7tWIz2kVHizw5PQ631OppbFEzkLn9IWMvq0N4WnhUpuf6TObxR_p47uinaFkxFZybCmZroSm-t81JMf6V3UgDUYimev5ssFEwNrYNiDwZ-VA4gqRgyWBJG6a4VU-s5Z6fIj0wFsl_YlI8nTpZRQW5b62RrA8U85Y5UhkF1UssJnw-bWlGBcZhLsKVh1a58SFCNAbtozvle21V_nRGlJd_G3UuWwg_k_yTAx2JXwWxsv6HoCk63oe8FKo9LKT2q4__I0oP8a_1HBwlhU6t6JLmdVqhZigwDdlV-vTND6OFJlqjyUarf_qJGichXV21n0DiBbiAz18j6KPQ2T7rc5AA1QleDf9dDnmA2R3S2VkphA-a1Ryd5w2n0T0P9Ga9fX8_tVKQtW1wEngGc4WMJAkdoLWAdeN6L1L7X8U3O-i03I4GxHfbZukxHCn0xeyOD1W2_f61E4IxQoXa0h5IjQhBK9577X9F2kbDcDKo80cJW5nUq0dvnwUVlfVNZa8cENmQQYIc9Br9aryOoxuS0GNcBMtHUhL9aukmDau11yP6U0bsu8o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
🇸🇾
بعد إعلان نتنياهو عن تعزيز تواجده في سوريا.. الاحتلال الإسرائيلي ينصب أبراج مراقبةوتركيب كاميرات مراقبة وأجهزة رصد على قمة تل أحمر بريف القنيطرة السورية.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/79085" target="_blank">📅 11:21 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇱
المحلل العسكري "الإسرائيلي" يوسي يهوشع: يشهد الشارع الإسرائيلي حاليًا شعورًا بالخسارة يفوق ما شهده عقب حرب لبنان الثانية عام 2006.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/79084" target="_blank">📅 09:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇬🇷
إعلام يوناني: البحرية اليونانية تستعد لنشر وحدتين بحريتين عند مضيق هرمز</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/79083" target="_blank">📅 09:56 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=XHtum8Hair_3BPhPDJ78axEYK3iP6htWPMd4NpINoQ6yq9DTR-6Bf_M7si0FDMlqL-C8WWQiTWhIKzgBs1n3wyQFVYZF2o2nQHmHKHQY2SUfSb1-Is8BzROcDPHvh5As2x0QerzlBHTfmKpJ-jghvUoqq-UpTBAz98TO5EP32yA4UL1ln4KdnvbaiV89eQ9JYyl344cLorGi8jb6pYQ2iRhMcVnStlGQNG4Gq1HrXxq5Zx2y9B6x9gUtnPCitOYAuRnbVnKWRnWGBZkAbMZutFbptVgV4MHJ7XHBWxz7pcJLrexKKT4mIHqHDPXC3xzlbXcZ8lufG4Q7rnGOfsLx1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec10e5aeb.mp4?token=XHtum8Hair_3BPhPDJ78axEYK3iP6htWPMd4NpINoQ6yq9DTR-6Bf_M7si0FDMlqL-C8WWQiTWhIKzgBs1n3wyQFVYZF2o2nQHmHKHQY2SUfSb1-Is8BzROcDPHvh5As2x0QerzlBHTfmKpJ-jghvUoqq-UpTBAz98TO5EP32yA4UL1ln4KdnvbaiV89eQ9JYyl344cLorGi8jb6pYQ2iRhMcVnStlGQNG4Gq1HrXxq5Zx2y9B6x9gUtnPCitOYAuRnbVnKWRnWGBZkAbMZutFbptVgV4MHJ7XHBWxz7pcJLrexKKT4mIHqHDPXC3xzlbXcZ8lufG4Q7rnGOfsLx1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🏴‍☠️
أهالي الجنوب اللبناني العائدون إلى قراهم يتفاجأون بتوغل صهيوني جديد في قرى الجنوب.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/79082" target="_blank">📅 09:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني بيزاليل سموتريتش يتحدى ترامب علانيةً: لن يكون هناك انسحاب من لبنان - ليس بحلول الجمعة ولا بعد الجمعة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79081" target="_blank">📅 09:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🏴‍☠️
جي دي فانس: السعودية تحولت من كونها مرتبطة بـ "انتشار التطرف الإسلامي" إلى أن أصبحت شريكًا مقربًا للولايات المتحدة بعد أن "خفضت ذلك تمامًا" و"حولت بلدهم".
إذا كانت إيران "مستعدة لتغيير سلوكها بنفس الطريقة التي فعلت بها السعودية"، فإن الولايات المتحدة سترغب في أن تكون إيران "دولة ناجحة".</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/79080" target="_blank">📅 09:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79079">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184d624d60.mp4?token=WQ3QJ-WR6TnEzURoJ03aDwK3s29fvQQFolKV0hrD8aVgHxf_7UJshqztPOONAoS1vkvLKwqm-i4xMS36h6GeIANnfhwrhbz7SegF9wseqotw-JWFgh_30QFlp0qVFJZqtEte-GFnW40K0FULSD8i2VWrmcU7LQ35-mK9fPtxqavGphZbVSbbNx9puwam7ARI-_lLnfJ_KC-nniCq2M6w2_1aHhG1ZYq8TlYjzlmfyw5UElFhDfvQJsFGa8oI6B77eA585CjcwOnqE3hGdb0Y2bPoUJwUowGvgRqPacW_gpNZY1dPToW7KXSdU7g_PivPYYU6ewSczo-HFPpaIhEX5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184d624d60.mp4?token=WQ3QJ-WR6TnEzURoJ03aDwK3s29fvQQFolKV0hrD8aVgHxf_7UJshqztPOONAoS1vkvLKwqm-i4xMS36h6GeIANnfhwrhbz7SegF9wseqotw-JWFgh_30QFlp0qVFJZqtEte-GFnW40K0FULSD8i2VWrmcU7LQ35-mK9fPtxqavGphZbVSbbNx9puwam7ARI-_lLnfJ_KC-nniCq2M6w2_1aHhG1ZYq8TlYjzlmfyw5UElFhDfvQJsFGa8oI6B77eA585CjcwOnqE3hGdb0Y2bPoUJwUowGvgRqPacW_gpNZY1dPToW7KXSdU7g_PivPYYU6ewSczo-HFPpaIhEX5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
تظاهرات وقطع طرقات وأحداث شغب يقوم بها الحريديم في الكيان الصهيوني</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79079" target="_blank">📅 09:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79078">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🏴‍☠️
حدث أمني جنوب لبنان ومروحيات الإنقاذ تنقل جنود مصابين نحو مستشفيات الشمال المحتل.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/79078" target="_blank">📅 08:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79077">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/79077" target="_blank">📅 03:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79076">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f554e92f52.mp4?token=V6n-7dHTU4Xp0YykNyLGrBhYo2ypNgAJtHCgyhu8hd-wK2C4REfuKCWDSLHKbNThuv9Kv8S9CRvkxiFlmN25E97Xc1PfaYVai-fWbAHPeZy48XXJpkRuzsJR3tX8pCwN3dD7f0-AINTHmRNH9lpTUOYUJ3o0Tm3JswkpzmZlwx_Puub4JyUBgqbswpXxENIkIVT5ohLdIarNyk7wMK8jEQnZooab27CH77utzdZI1ZTFDMa2-3DOKXpMkb5FXqhEzjWWB2LxCHs66BPZo582wQSr9wNOL4XuNNHc3BKoF6Xn5c7ePgwm9MwTY5Nu36bE-frUE0aW9MgFSbt8kPtKuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منتخبنا الوطني يخسر أمام النرويج 4 - 1 في أولى مبارياته بكأس العالم</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/79076" target="_blank">📅 03:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79075">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هدف نرويجي رابع</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/79075" target="_blank">📅 03:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79074">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">هدف ثالث للمنتخب النرويجي</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/79074" target="_blank">📅 03:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79073">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">بلومبرغ تنشر مذكرة التفاهم بين طهران وواشنطن:
- طهران وواشنطن وحلفاؤهما يعلنون إنهاء فورياً ونهائياً للحرب على جميع الجبهات
- طهران وواشنطن وحلفاؤهما يتعهدون بعدم شن أي عمل عدائي والامتناع عن التهديد
- طهران وواشنطن تتعهدان بالتوصل إلى اتفاق خلال فترة أقصاها 60 يوماً قابلة للتمديد
- الولايات المتحدة ترفع فور التوقيع على مذكرة التفاهم الحصار البحري على إيران
- الولايات المتحدة تتعهد بسحب قواتها في غضون 30 يوماً من تاريخ الاتفاق النهائي
- إيران تعمل على استئناف حركة السفن خلال 30 يوماً مع مراعاة حاجتها لإزالة العوائق
- واشنطن تتعهد بالتعاون مع شركائها الإقليميين بإعادة تأهيل إيران وتنميتها اقتصادياً
- واشنطن تلتزم بإنهاء العقوبات على إيران وفق جدول زمني يتفق عليه كجزء من الاتفاق
- طهران وواشنطن اتفقتا على بحث مصير المواد المخصبة والقضايا النووية في اتفاق نهائي
- إيران تحافظ على برنامجها النووي الحالي دون فرض واشنطن عقوبات أو تعزز قواتها</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/79073" target="_blank">📅 03:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انطلاق الشوط الثاني وسط ترقب الجماهير لما ستسفر عنه الدقائق القادمة.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/79072" target="_blank">📅 03:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e89085b7.mp4?token=l5XTyKiVNUp8m1YtiVfClue95YBPTA3_I-QeORiQfmyfLpo9OPIkc7xG3FvXBHLD8-A4c2IGArMU7C7pY3E2ZbNLGJsxPXDrdvYg4_V4HdVEGXVHuGHwUNnFF-jqFi-8pFbQg_W-ts83M_U7UNqNLAWyclXQCBc4w3q_pk46DJZscRmgVYNPL9VThCtJlzOtikD5YrMpjDLhPkyzWQxENbaEngwgeKswaIJQHpgoUVdR40EuAm7DVhG4u_1dRI8oFvnHmeoERwV_V2zRo-6kSBpc-oTb6LU15MKlGtVbuJ5qnp0uiSqx1ITOh9Oh6gJdjbL1z9DwSHecv1xpuyYEAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/79071" target="_blank">📅 02:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انتهاء الشوط الأول بتقدم النرويج 2-1 على منتخبنا الوطني الأفضل في كل شيء</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/79070" target="_blank">📅 02:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">هدف ثاني للمنتخب النرويجي بذلك تصبح النتيجة 1-2</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/79069" target="_blank">📅 02:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هدف أول للمنتخب العراقي بذلك تصبح نتيجة 1-1.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79068" target="_blank">📅 02:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/79067" target="_blank">📅 02:09 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">على غرار فشل منظومة السيرام بالسفارة الأمريكية،الدفاعات العراقية تفشل بصد الهجوم النرويجي،بذلك تصبح النتيجة 1-0.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79066" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79065">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRSY78a6qJBJhkE2QM1moKXK2JHFuG4B9r9QCwSsEZnxpURHbPbyNPZ-k0tMFVQRyJGNNPeLp4Y25suH_bYtELRumqfbN_eg0Jgf4rerTc5B1VuHhlp5t2g_SOwKjmp6z2kh2JFT9s99OBFJYnnGrDjjtkl-dcomzpol-jlFbiCIBKsKsKhVL9Pf7pSSdy7eUaUajFRE4QNUJ9Qqjh5wqcGREcRAA1iX-AVC-xX2exO9aCRT7OhA-nQ_i7ZD76QyRQDsAW_8w6TszQAXH6pzcSIYNdVMZ-eH8zu4Oi8Lov596lt8UarRmjRbC6ApMGosHf8mAeBHnK-pIe4UqVREJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
عزف وقراءة النشيد الوطني العراقي في أجواء مهيبة داخل الملعب، وسط تفاعل كبير من الجماهير العراقية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/79065" target="_blank">📅 01:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvPycJ3YQwxarCIgGi3J0bAHdGt_5N9zU7R0P-gmOGgfWpjoFbuM5Bogqtlm2SRcsDtfcEoojGymtj9vzCFsRPwcnPy02Iwv4UtoTjKG_Jemulv4a4CCDxyWIkMjKWXtN3GH0-c9FJgXNrWDnoTEP02rgtfkpKb-L9VETZzntfX2zIYhnOwW4bUBT1jYBwvZCdXJ58jhyBnxBVU8oyGYwlChKizijHLSmjfIdWZk6L3JlCTdC1OQsPwxVcMPtsScb1U736uT8W-MoTX_RAk-OI5hG-yvASun58iJdD3hntCLPphVWVAJNtFlI84EUcWi56eud32_Ywf1X6pM4JMG3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اسد رافدين حاضر في مباراة منتخبنا الوطني
هو هذا جني مو اسد للعلم</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/79064" target="_blank">📅 01:18 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79063">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2923a06709.mp4?token=jZSf0zxe-uZ_POBsS_duePuuyZegbfeFr7ufTZsZKG1QkMxyEUbKjHNMeytrurjVFNO32wpOkQOPCufOhA29TXggKaXmFAoPCs1jHjN3f7Mu8BqC-B7AH9tcOicBnP0OPq8izQRz6DN4fKisIInQLM3n3t-oF0v9_sRx5ZVu9HAozXsgTm2s0n4sI3VtV1wD-BWMh4v63V3Tfa4ldRxfoX8_bH5-kAaEW-zQXCOiLXqRvbO8X6YrdCZgGObU1iGiSsVAKmLZPgLVW4-B0WeGXOKWBsHvvuJMdKyydmqtKJnfg7sVVpeFOJdHGDuBrWpHz2uuwIoLVxi3OZ4jziPjdVEUVfiBDx5Uf3agm5UC2M9Z3bF8RNHjbuL9HExShkPqi2JCuVp1aG068y2b54g7bawH2MamdK2zkub65XvbqsJWGl1Lrp9C559qCcLGqQNRCUIw1VTPHEfg5Ch-brztxcEHavEjwdiICyxbegCGvaBc8zplPDWZ5ghP2sU8sAU7LhWqB-X8MNt2EAG7pvFWv_6I4cKceTyJb1zIZFf6JuXsX3HgIXe_2PPMZuR-z6MqUQn3KGFghyfJ7XRj5bum_w-9vrE-IM3QvTj5We19tkQgYI_FAF90ZerJmMrL7s7XBUzJLf7h_AvzePDBZhD4SGMnPvYwDtV1cZPjXM8e01k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2923a06709.mp4?token=jZSf0zxe-uZ_POBsS_duePuuyZegbfeFr7ufTZsZKG1QkMxyEUbKjHNMeytrurjVFNO32wpOkQOPCufOhA29TXggKaXmFAoPCs1jHjN3f7Mu8BqC-B7AH9tcOicBnP0OPq8izQRz6DN4fKisIInQLM3n3t-oF0v9_sRx5ZVu9HAozXsgTm2s0n4sI3VtV1wD-BWMh4v63V3Tfa4ldRxfoX8_bH5-kAaEW-zQXCOiLXqRvbO8X6YrdCZgGObU1iGiSsVAKmLZPgLVW4-B0WeGXOKWBsHvvuJMdKyydmqtKJnfg7sVVpeFOJdHGDuBrWpHz2uuwIoLVxi3OZ4jziPjdVEUVfiBDx5Uf3agm5UC2M9Z3bF8RNHjbuL9HExShkPqi2JCuVp1aG068y2b54g7bawH2MamdK2zkub65XvbqsJWGl1Lrp9C559qCcLGqQNRCUIw1VTPHEfg5Ch-brztxcEHavEjwdiICyxbegCGvaBc8zplPDWZ5ghP2sU8sAU7LhWqB-X8MNt2EAG7pvFWv_6I4cKceTyJb1zIZFf6JuXsX3HgIXe_2PPMZuR-z6MqUQn3KGFghyfJ7XRj5bum_w-9vrE-IM3QvTj5We19tkQgYI_FAF90ZerJmMrL7s7XBUzJLf7h_AvzePDBZhD4SGMnPvYwDtV1cZPjXM8e01k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">The fight for football has only just begun...
⚽
🔥
Don't miss the next chapter of the story.
👀
🏆
Watch the full Episode 2 now on our YouTube channel:
📹
Football Against Enemy - E02
🆔
@explosivemedia</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/79063" target="_blank">📅 01:17 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34WBv0XxxWMBCJ4YnQTRp746WwpIT5LPTSLtP0tMYb5fj6CNoKFhcE0X5jUMLWRFs99jMx0PxSBJqPR_C2rmXt-dMicvARhCs8m2eO60j3u1luDCrxZdHH7_VR3_pFe5-z7uGstk7Y54-M9HBLQ-CYNlV7BqXN0QL8nPKkwlaINKVq76jNZ4W6dFNSInvr39C9COVpGeq0aY64Xdl7fDMXaLbmWuCwbqUMknzAFRzwlIHnO-0OcTtrdKVK53xLSGgNJmCMYQuk3F6BQjWqx9MPXtMOGKvoIqQR0kUe_Hqka-dae3jRXPNzdHwICmzUk7dBIUAsOm0NYYDxVMQ96lHQLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21b8ac1d54.mp4?token=Obzcai9fvx_ddZaHdbw9qc81o94sy5TMTJos4yGd-muOmDzjbrdMi4a5Mo86oJ3TBqb99IkNKNZRIiEannCz7Dj4Yl7czQGwj723I_iQz4014gNVW6fZ7LocqA2gpHtFCWZLZezqoMnRJebajEkpwJelPCfS0qfEia9yU5VbdxjLixVb3vU1M0-glAn52QJnIdDlWwg-zVy17188wywY-vTyTb0jNgmCmvUY-wpf6edN_MaNY6HM3pKyY2bV3HLRrZ4ym8XWEqz8qXPiK3-sQB3fN__hmENTaacgUM9bxT8coxdzPD7hRc-v5IdovPu8RA_L8RgB0UlLfTeOq9Z34WBv0XxxWMBCJ4YnQTRp746WwpIT5LPTSLtP0tMYb5fj6CNoKFhcE0X5jUMLWRFs99jMx0PxSBJqPR_C2rmXt-dMicvARhCs8m2eO60j3u1luDCrxZdHH7_VR3_pFe5-z7uGstk7Y54-M9HBLQ-CYNlV7BqXN0QL8nPKkwlaINKVq76jNZ4W6dFNSInvr39C9COVpGeq0aY64Xdl7fDMXaLbmWuCwbqUMknzAFRzwlIHnO-0OcTtrdKVK53xLSGgNJmCMYQuk3F6BQjWqx9MPXtMOGKvoIqQR0kUe_Hqka-dae3jRXPNzdHwICmzUk7dBIUAsOm0NYYDxVMQ96lHQLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79061" target="_blank">📅 01:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=NOaf3eJau7pTWZ94mcAmv-DR7Lx-ypYiy8gqMYaSxVQwvGyYxX41sktSkE3TwwIdiYt9RFc50rIqOF8bNdqoH8cWnpiWx6NrLHXxdfH6iOprMhG3guwdZbKOAZAMwADwbrMaIWx3MpOkZ1Z7b8K88LOFNDzaow6s1uGcO9QINVz-jjvglraQrwGjE0NVMNQflrKzveXpi7AWNaxZoYrx7BhHC2oOcEbDQiuGexhgZOGqNY1dGKqoNhLqGWfwK5Xb26hpXsSl784RHH0p0N3vkTGnQMwT0nwHbUempDSUdNrdPldmPjdCOyRC0xZh3TJeWVyYjZ_iujJuEmr7SqJy0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00a9bf1be7.mp4?token=NOaf3eJau7pTWZ94mcAmv-DR7Lx-ypYiy8gqMYaSxVQwvGyYxX41sktSkE3TwwIdiYt9RFc50rIqOF8bNdqoH8cWnpiWx6NrLHXxdfH6iOprMhG3guwdZbKOAZAMwADwbrMaIWx3MpOkZ1Z7b8K88LOFNDzaow6s1uGcO9QINVz-jjvglraQrwGjE0NVMNQflrKzveXpi7AWNaxZoYrx7BhHC2oOcEbDQiuGexhgZOGqNY1dGKqoNhLqGWfwK5Xb26hpXsSl784RHH0p0N3vkTGnQMwT0nwHbUempDSUdNrdPldmPjdCOyRC0xZh3TJeWVyYjZ_iujJuEmr7SqJy0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما ضم روحة يحسين ابنك</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79060" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=OwQ70NAWhiEg214SkYCVveu61Vbq_O2UirH9_5FPB_Px5AW9vF8INWTh5n_BnFs597So4P1Dno8ENm-n4C0fe7VQqMJyR2myPXgZqFrJvMlELM-m88rlX8eKH2dpogu39Aaei1dJNigQJfR8YZupLVeNM5WRK6kOypk-QGJdqgEM0SEtjoSsA4XeNX3d2sySP8jbi_TdcOh2R9v4Vj0NNXR-XE4R3PdZaxQhY_ZpeT_Z4R6g5TWQBxVNakTHYDFG7_6hAQgd442xbkAuSb6E1qel4MjhdknsczQgivn9L0yoTdlNTVAaW-aTSIq8U-3TOVnXPLSzMKILAXYeHw9Ihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9b1f4a323.mp4?token=OwQ70NAWhiEg214SkYCVveu61Vbq_O2UirH9_5FPB_Px5AW9vF8INWTh5n_BnFs597So4P1Dno8ENm-n4C0fe7VQqMJyR2myPXgZqFrJvMlELM-m88rlX8eKH2dpogu39Aaei1dJNigQJfR8YZupLVeNM5WRK6kOypk-QGJdqgEM0SEtjoSsA4XeNX3d2sySP8jbi_TdcOh2R9v4Vj0NNXR-XE4R3PdZaxQhY_ZpeT_Z4R6g5TWQBxVNakTHYDFG7_6hAQgd442xbkAuSb6E1qel4MjhdknsczQgivn9L0yoTdlNTVAaW-aTSIq8U-3TOVnXPLSzMKILAXYeHw9Ihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
توافد الجماهير العراقية إلى ملعب بوسطن الذي يحتضن مواجهة منتخبنا الوطني أمام نظيره النرويجي.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79059" target="_blank">📅 00:55 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">" اني سائل عنكم "
آخر ما سمعناه منه عام ٢٠٢٢
ونحن ايضا لن ننساك وستتشرف العراق بك</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/79058" target="_blank">📅 00:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79057">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نايا - NAYA
pinned «
السلام على الخامنئي   الخامنئي منا أهل العراق
🇮🇶
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/79057" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79056">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">السلام على الخامنئي
الخامنئي منا أهل العراق
🇮🇶</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79056" target="_blank">📅 00:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79052">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LscsEr1yRnjj_bFXQszPwSe3kpvo_AdVbblKJNfRdE0RQW_Wa0AyXWoHU5Aq8gqbFLSl1uAzAfLo_Vsm__IhQeN8yXzndvgcOD7v1P8xmj1OpqAyj5ujF2YXnoj4CDHoGCT27KKgHd7VMiwicyorR97BPrbeIGgi1h_u3i60OSYCnIuwry3RqdblsnzPtl6DwowKHOICOMzHZguXi2WC9N0uQI_rjjnhpQi58xizHUDKiJ18fAwYnmOp3zMefELxyDiJVqYvdvDnsf6rgEu1FxSEBlhgAjkmEiYvq_dkhpZpGYYEloiLpQYaAlniIHq85-nlltSgvtG19FZ1PxzStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GWbbVl-Ql6Rmi4AvvwCh9Hh5ze6VHjVMEp4A7OgvbKtzm-FkPbfImFHaGL2KfGpq2rUevl5ZOVnASMjGxkFSW-ubceoCUpkRSkW0DKD6jLLDu-fUzFscRFDKYfh2-zSXitmlKwZV4Z0NlPMR9JirsO2c1nNvFtxTyK6HycG1lFDHv9vTPf8opJGLUZVGJ6wHMBuoZfsEJKvQHok3D69YZjKK1mJouUBcDVu7wXm9zXtkYZS7Ybe1RbnvGxox5YawUdXDb_OvaqMnV4wFx6rYQwokLbqfMWLoGhIwkUchbzgieZRxSHZMbaln_8IwyfY2M1M4CSuwsgaxUmSDCD6tkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bLhXaF36NFFf4Nra2FTMtRcPCQx-CvuDfKeI6OltTB6SmcBYwvV43Mx3CcmrPielas3cpko6SNfymfbJ78XZ6B9bUmRVAGiKKLGzynGdzNmYxfm9otU1TgOq68otpWopcJ9UUYUDPx5VwUgm-1QNK2ybGzYpUPLlGXHRCGC73F5XDPO-6BvZeQdKx9WSlLZqkyeA4aci-Ob0x5HCsztfvSYGv5b2lkecUq0GfFzPICPtCxdn7zrpjSv5O7I_LcsUAE1FkdRd8OJGqNZy97OZIwQrpSMlEo0ERjrMp35_E1WdBuvJMNcqee8isYHWCRNDoOM5aa6PO7mtzF-KyeprQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MOEv6tKvgKfmvcVJSwP4ZmxqmAq4uLSpxwZJWaQlObtpehb-c0O04vFeqaH3yGeASKkpnzThMiLKX-BrzXgCFDzqEaURI_9XaVhnAefy-R16Rz6-WFnv9rRl9Zu9VHU9LzGyjj0YpHBIIpY0JeWXwjNclEFD94HrH0EyCPy4873UZak9zxM5tnsMIS9sGUOsFkltyypLKwfGDoWTzzeYFMMwzXKeyFRPANYV9pcggUOgm2b70nSubJ-rE3urxb02Jn9k_Vptwcy2Cdf70TGHsmFSanZeWf0rCP0ur-iTrSk-f_9NAcOC4_EoD4dqK_f2rt0rqz2BccqFI8X6vsTlcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🌟
لاعبين منتخبنا الوطني والنرويجي قبيل انطلاق المباراة المرتقبة على ملعب بوسطن.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79052" target="_blank">📅 00:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79051">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🌟
الجماهير العراقية تتوافد إلى ملعب بوسطن لدعم منتخبنا الوطني.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/79051" target="_blank">📅 00:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌟
تشكيلة منتخبنا الوطني لمواجهة النرويج في كأس العالم.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79050" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79047">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=oayqwiI21qhsGy0DAN7mpueoNI-2S90HLinPqy7V7NwpUW4ooN3se-VHYxm4KrS50tFXuTfErFY8y0OSRQ-FRZ9B-8XBop3INuwXD24nHXwTaJ-NhSghI2o9zusrUIHrzIhoBacmFH6TT6M-clgF3iKOYRbBDao_3QIg8eQ1bCBVjPXIQRn2FXXkcAyoyswi6OGU8DzrOUdCNg2SoooBUYT5SYOb4ZpHc2rUahNAmBWl8X051TrlJsLAEseNPUijwDr45dJ5iMHxnh_hyvm0TYuVZCyId6qEH4oYi4Nza1o7jgjuSZAl_NemacRbo2LOyCR6ryPvgxDkwj8dau1zJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ff81bb17.mp4?token=oayqwiI21qhsGy0DAN7mpueoNI-2S90HLinPqy7V7NwpUW4ooN3se-VHYxm4KrS50tFXuTfErFY8y0OSRQ-FRZ9B-8XBop3INuwXD24nHXwTaJ-NhSghI2o9zusrUIHrzIhoBacmFH6TT6M-clgF3iKOYRbBDao_3QIg8eQ1bCBVjPXIQRn2FXXkcAyoyswi6OGU8DzrOUdCNg2SoooBUYT5SYOb4ZpHc2rUahNAmBWl8X051TrlJsLAEseNPUijwDr45dJ5iMHxnh_hyvm0TYuVZCyId6qEH4oYi4Nza1o7jgjuSZAl_NemacRbo2LOyCR6ryPvgxDkwj8dau1zJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
الجماهير العراقية تواصل مؤازرة منتخبنا الوطني قبيل انطلاق مواجهته المرتقبة أمام نظيره النرويجي، وسط أجواء حماسية ودعم كبير.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/79047" target="_blank">📅 23:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79046">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=XgP3EyBmlibCgt_kvHP_4hAvSII3ptdQ6Q5QCo_oXI2MR0yo66GHdkZ1G_ZrpiIIFOWprsJf-9bUQjh__nErcJgyZokkVwys2_oxNHM-RNomMBfiU8JiTnBw89UOz-Q_MdHNgZpJWa3ciG9tipj8HOWW1CfNGbGn2sDMM6Uen6GjHWFRdfGtcdePwQNCNBv5xNEnXvgelyTEUk1fEfbgova4AoZBYvuT5088ueEA_Jg6qFQmHJorQb5NIUHoloRoH68Vsy4EsoKk3eCxpDNylEP8yt3E490rGEZVm80rddGhBaJAmcJ-gjqUx89_XwSCcfk8ZjFjccZ_N6SsBoynyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293589ed4f.mp4?token=XgP3EyBmlibCgt_kvHP_4hAvSII3ptdQ6Q5QCo_oXI2MR0yo66GHdkZ1G_ZrpiIIFOWprsJf-9bUQjh__nErcJgyZokkVwys2_oxNHM-RNomMBfiU8JiTnBw89UOz-Q_MdHNgZpJWa3ciG9tipj8HOWW1CfNGbGn2sDMM6Uen6GjHWFRdfGtcdePwQNCNBv5xNEnXvgelyTEUk1fEfbgova4AoZBYvuT5088ueEA_Jg6qFQmHJorQb5NIUHoloRoH68Vsy4EsoKk3eCxpDNylEP8yt3E490rGEZVm80rddGhBaJAmcJ-gjqUx89_XwSCcfk8ZjFjccZ_N6SsBoynyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عناصر تابعة للجولاني تشن هجومًا على مدينة المزة ذات الغالبية العلوية في محافظة دمشق السورية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/79046" target="_blank">📅 23:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79045">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=E2RiywNfXAl3x1AJNjS3qYHCHPUOTenRP--Gn4xgiKvirNx_OrErQgDwPyTZ1ZXp2-XtSchjQvG8SUUXpV9KqR29IcPgiJqIaaI2KPyXbTNTXFuEiJl5_qjg9a50fPB6L-JNA8mbbTk8xQDdrrp2NLvftE_a9WIfiD72s4RlCqFoInUWeXlUGM7gySTjjYxqRrZzLuhFZD0jAwR0JcpRvlnuI9Ist5SCE3hApMEkvVImk-MrnHms6vBJxFKlNM0_NJs35OvQZVCbOgPA93EVAxg4fBrSo_qQwJp_fjMmmScDZ5tL2-NGFW6UVSf1FPjLnpYIB8Y2L16baJO0vBL3eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eac4c8ff20.mp4?token=E2RiywNfXAl3x1AJNjS3qYHCHPUOTenRP--Gn4xgiKvirNx_OrErQgDwPyTZ1ZXp2-XtSchjQvG8SUUXpV9KqR29IcPgiJqIaaI2KPyXbTNTXFuEiJl5_qjg9a50fPB6L-JNA8mbbTk8xQDdrrp2NLvftE_a9WIfiD72s4RlCqFoInUWeXlUGM7gySTjjYxqRrZzLuhFZD0jAwR0JcpRvlnuI9Ist5SCE3hApMEkvVImk-MrnHms6vBJxFKlNM0_NJs35OvQZVCbOgPA93EVAxg4fBrSo_qQwJp_fjMmmScDZ5tL2-NGFW6UVSf1FPjLnpYIB8Y2L16baJO0vBL3eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
طائرة مسيرة تستهدف مقر لاحد الاحزاب المعارضة الايرانية الكوردية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/79045" target="_blank">📅 23:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79044">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b152a86.mp4?token=RfFw8Lgn_GDquhlN79KsTeLHx_VcFalqa60DbHaaiARcHffdph7t4CwseFRPzTJcqbWdn2oJkI1iJEIgpnhE9ye4V8SIo1Jv6M6ls-knTREcuQmh_WutIg8JcqVOozJT88sR3BfBS5BbU7Rf5fwdduYJU_r2mPD6WkqC3b39wgBMsIdnrhWV4-sil15fEQw78VJZwun-tatfzjP43E__kS57z6zy_RfZ0jOGW_aQbck53xvGS3M0jjGxb_Ws6OksOyYkdWH4mpUaXCt6rgA-0PpAW2AB3jpSGs-CQglPopjitBizc8bAcJjcIEE0gnt7iSufSJ5CY9PBehwsY4cn4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b152a86.mp4?token=RfFw8Lgn_GDquhlN79KsTeLHx_VcFalqa60DbHaaiARcHffdph7t4CwseFRPzTJcqbWdn2oJkI1iJEIgpnhE9ye4V8SIo1Jv6M6ls-knTREcuQmh_WutIg8JcqVOozJT88sR3BfBS5BbU7Rf5fwdduYJU_r2mPD6WkqC3b39wgBMsIdnrhWV4-sil15fEQw78VJZwun-tatfzjP43E__kS57z6zy_RfZ0jOGW_aQbck53xvGS3M0jjGxb_Ws6OksOyYkdWH4mpUaXCt6rgA-0PpAW2AB3jpSGs-CQglPopjitBizc8bAcJjcIEE0gnt7iSufSJ5CY9PBehwsY4cn4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#عاجـــــــــــــل
⭐️
إندلاع إشتباكات مسلحة في ناحية كردرش بمحافظة أربيل شمالي العراق؛ سقوط عدة اصابات كحصيلة أولية.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79044" target="_blank">📅 23:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79043">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=iSQsh_O2HxNFClXQVqneEcbQSDBCYObYPk0cHeP1vbOMJnSgVkJcXlML23lrV5N2OJq2fJdw8Etb7f9nki-BdG2QDjlOstCQU8seeJgaCIcMkaadiHUsI0vAe6onxXkTXF1RkqkzD8tlJilX7cQ3BXRtgvPCoww-OWk5nO61WRO0hmBmBoHtT5c2rHvhrhWhASIE2XRgdY5zwc5lvqyZEhnxs5DxNQtoFpcWJ3JYi-jY7h6dIf6iGzz06QnHKuSZz_Y3kA6uj-iOo3OGQJWyvta5g5tR2Fs4MeJDJjIabokIROlbgM1Sz2kvpO8TAGOHTGFkB72arqvtvVzsuP7PTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c939a9b30.mp4?token=iSQsh_O2HxNFClXQVqneEcbQSDBCYObYPk0cHeP1vbOMJnSgVkJcXlML23lrV5N2OJq2fJdw8Etb7f9nki-BdG2QDjlOstCQU8seeJgaCIcMkaadiHUsI0vAe6onxXkTXF1RkqkzD8tlJilX7cQ3BXRtgvPCoww-OWk5nO61WRO0hmBmBoHtT5c2rHvhrhWhASIE2XRgdY5zwc5lvqyZEhnxs5DxNQtoFpcWJ3JYi-jY7h6dIf6iGzz06QnHKuSZz_Y3kA6uj-iOo3OGQJWyvta5g5tR2Fs4MeJDJjIabokIROlbgM1Sz2kvpO8TAGOHTGFkB72arqvtvVzsuP7PTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/79043" target="_blank">📅 22:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79042">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🌟
انفجار مجهول في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/79042" target="_blank">📅 22:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79041">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=HmuYxAL8qjN6QRyj819yowIiITnyUQe1rD1JqTLd5gshykphJGdQmwk72t6Je-k84zNJHsQUuiVJbpTabHzVIGD3SiJ91mwXL2QErDS0IuslYN003KXP2hmoj8ogG2H0QxCQbWatztkeCh1jBfCpPmL1-pTjnVQSk2y41T4ucOlW49UPIE-mjFra6cODjePXu1-54tjwcB1tbka2fdYvxj-UNdmIBC_sDzlgBv_IVnfbjwmQiCoq90doRdkUI7Sns9PgK7JVeZfobj2372A051o8N3YENzIu48oMaF1XgDTltpi3FKI4MZrczKyGAWAVbRpp0W2BkRwQeAgaUkB44g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/258e6fd627.mp4?token=HmuYxAL8qjN6QRyj819yowIiITnyUQe1rD1JqTLd5gshykphJGdQmwk72t6Je-k84zNJHsQUuiVJbpTabHzVIGD3SiJ91mwXL2QErDS0IuslYN003KXP2hmoj8ogG2H0QxCQbWatztkeCh1jBfCpPmL1-pTjnVQSk2y41T4ucOlW49UPIE-mjFra6cODjePXu1-54tjwcB1tbka2fdYvxj-UNdmIBC_sDzlgBv_IVnfbjwmQiCoq90doRdkUI7Sns9PgK7JVeZfobj2372A051o8N3YENzIu48oMaF1XgDTltpi3FKI4MZrczKyGAWAVbRpp0W2BkRwQeAgaUkB44g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنظيم داعش الإرهابي يتبنى استهداف صهريج نفط عراقي في مدينة منبج السورية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/79041" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-79040">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هام.. وزارة النقل العراقية مسارات الحركة الجوية فوق العراق ستعود خلال ٢٤ ساعة</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/79040" target="_blank">📅 22:32 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
