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
<img src="https://cdn4.telesco.pe/file/ZC3v3NThZD6RgR-NuyWjE4jMAyd4EvuyzbNGXtlMJ8YcGe2hh83uwuCEk6COmBeiDWGmxeNPXCGMXjNgMOPDCqMzAc6N06XFHbERfW__uxDY3_OwlNiNNajLQLXQuaMTL2Kjace7bE4JsKqQASATV3k6COjObcmwamn7EnEHt5Qk6mUSutyOnfuNYagkX_KDxjyF0xHQ4A1f59oz_or3vVsRqDJsw3lYioNbmancI2eplE0ZlPFp_V_8kdBIwnWs2LuvYwi_nlmLahAzvMQTT3Lx_670-HqaqSxmsAQU_eYsTxQ82nMPSNnab2mjZKCcPrk5pz4dw9tf8HuXWaZRmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 11:38:00</div>
<hr>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کی قراره قبول کنید از وقتی تیما ایتالیایی افت کردن کیر رفت تو فوتبال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/funhiphop/79348" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fEJjoCAQfzBYfu8ldg3cTsEbWxD9yC6Ij2USZ1a92G9jglVie_Kc2L4FIipuYgOwcV69lx9cz1tfLl5qp_SryAbNBGbBJhpWYg6dRy4F_zB78dSnrjOY75dJ1yr3ovy-bGjmXy_PQe6y414Mul5spT4zxdfO0wAJwQRDsHebN9a1w3tC6EoD_xc8KopzDXMZJIvHHw8gBRT8so9U3XNfDFRYsKnha0y5sls6_8doBK46TPkD6IxWLJdnLq_iBgJzcPNfBOpVZLxRjxNkw0r9Xjw_QIUHaHUicHrtk1fzfjK39AKV_wsiGEtgVA0Vcvk_cx3Bi9DSjHEuPdlrxnVyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب بازی مصر و استرالیا خیلی عجیب بود، یهو استرالیا برا پنالتی گلرشو تعویض کرد، گفتم دیگه هیچی سوپرایزم نمیکنه که چشمم خورد به بازیکنا مصر که داشتن قبل پنالتی هایلایت بازیا رئالو میدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/funhiphop/79347" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79346">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj24RH7xXPK2EzUlQEZhSEJggDgceufriLA_7iOnNcI6A66rzVqvzGOrnx0Sas9ctDMwd7f8x2s4qkqxCZdRJ6qicFM8uRcjDnfrEzk7xJNeytq-nIDm9jaScKvxlUoW0AmHV09KhF5X0-tpfgnt54MM9gF7rjS1NykvzNOWFU7r11RIozlUiah_hQe-L833WfPLVIIuFpJK52uiIyhrvGwBYsHc1C5Ity1tD3AugnrmkGEmVqkLxS0P71dkfNmMnf4FisS14nKPbM-Chj5QkZVz0HNVGsaKC1sTixnPaY1obnNTxoVvvmOw4Ro3TBgyvhiePb9FB4S2_gYrqKlbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پاراگوئه
🇵🇾
-
🇫🇷
فرانسه
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه فیلادلفیا (لینکولن فایننشال فیلد)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
✍️
اطلاعات و شرایط بازی:
- پاراگوئه در مرحله قبل شگفتی‌ساز شد و آلمان قدرتمند را در ضربات پنالتی شکست داد.
- فرانسه در دور قبل در یک دیدار راحت با نتیجه سه بر صفر سوئد را شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی کانادا و مراکش برود.
- با توجه به دیدارهای اخیر و آمادگی فرانسه، برد فرانسه و گلزنی امباپه می‌توانند گزینه‌های مناسبی باشند.
🧠
با پول قرضی یا ضروری هرگز بازی نکنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/funhiphop/79346" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/al69tOeFAlqmYub83ydxK63Fi3KoflwXVsniLDM8TxCSh5yzfi-vWry_PRFQbBYODizn2VSNCEnOsYjkLimRtjcOgOmnWhj1P3qA6o7FGO1jVy4m36HQp4z3vY_GTiK97VrdPtBN1fr5qmAk0iTcL3y8OTGgQOY6P8uGB5XzaLxzziprniDQBwpKIHpKg0PN0vi4uyYlJJFzuOUG8bs5FwqMzjPTj4XQjSqi07CFwPPRr8ADXHieaTNDKocFG4-s-JWTYD8ZWOeP5g9w___nsMg4ZPWZeznsLVqDbn25pjPPXCQw39tCAK5rA22qg3wx_oVNXmzmSPjBM3nAVTpyHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببین حرامز
هم آرژانتین برد و صعود کرد، هم مسی گل زد و هم تیم کشورت یعنی غنا باخت و حذف شد و این یعنی به فاصله چند ساعت سه تا کیر خیلی گنده خوردی.
به نظرم الان وقتشه بری صورتت رو بشوری و یه عنوان آخرین جادوت سعی کنی یه وردی چیزی بخونی که مردم جایی تو خیابون دیدنت فقط یه دور به قیافه‌ت بخندن و دیگه دلقک بازیات و کیر شدنات یادشون نباشه که یه دور دیگه به اونا هم بخندن.
موفق باشی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/79344" target="_blank">📅 08:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af167dceef.mp4?token=jNPRgmv7KsBtKyNtlqZGQH76esB7uP55BDhdBWnBI9tIHccH8WTYb35_H2hp_9cP4J4zinZHB6h6b9YV-S-6tnYDvI-pwQuzz4QNFCfNStnPVy8Gfqvd7DOnVp2CDUo1KMZV_C70Xcl5kCvtRNsBo6-RlvDqElPVj6IBjybsu2Z8JERFA4vvBrvWwjRfa81VewlicvsnHEuF1Ubv5sv9I4311HSn66ClCUeUE_6Ecg5RcKA_-MHq2Vja6MPlPe_a_tzFHdKF_iwKa2pjRbe9-VzkcJ7JW_jUpLAGNtW2-Fbwf71IrEvPpvgJjHfscbPml4qw9HfLdnRxlPMdrXfY8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af167dceef.mp4?token=jNPRgmv7KsBtKyNtlqZGQH76esB7uP55BDhdBWnBI9tIHccH8WTYb35_H2hp_9cP4J4zinZHB6h6b9YV-S-6tnYDvI-pwQuzz4QNFCfNStnPVy8Gfqvd7DOnVp2CDUo1KMZV_C70Xcl5kCvtRNsBo6-RlvDqElPVj6IBjybsu2Z8JERFA4vvBrvWwjRfa81VewlicvsnHEuF1Ubv5sv9I4311HSn66ClCUeUE_6Ecg5RcKA_-MHq2Vja6MPlPe_a_tzFHdKF_iwKa2pjRbe9-VzkcJ7JW_jUpLAGNtW2-Fbwf71IrEvPpvgJjHfscbPml4qw9HfLdnRxlPMdrXfY8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 2
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/funhiphop/79343" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پروردگار بی همتای فوتبال، حضرت لیونل مسی بهترین بازیکن زمین شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.2K · <a href="https://t.me/funhiphop/79342" target="_blank">📅 04:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171cc02113.mp4?token=B7SCsjc5hnuz0x4WV6IQa-sXYNfkBCwU2nBS6R87O0orNwVzrBC-efGvyg5VhojnIWnDAcXEIC2t1ilw-Ln82cARR0XMxp3Ue9GGO_yYTzq4sruDwp10Nj2nNg5Z9EE3TdZ57QKO96aL5DKlBXH_OkQ8TvgiXhR8DisB8bJT40yR9EOHexdwfGm3qwX-X1w8_HXLQSV4acuCWSKFwYJXKLdRVklA6GKS4QEIeilSwZIkm7Z4e7f617V-6ooe11x9sFL___bqBnhzkzQnJ6qAHYXiWvfubI2ZBy5DrX0bhUVnQXJbFiU3VKJG6ofr86c46mEO2a0E640ECTvLMCDzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171cc02113.mp4?token=B7SCsjc5hnuz0x4WV6IQa-sXYNfkBCwU2nBS6R87O0orNwVzrBC-efGvyg5VhojnIWnDAcXEIC2t1ilw-Ln82cARR0XMxp3Ue9GGO_yYTzq4sruDwp10Nj2nNg5Z9EE3TdZ57QKO96aL5DKlBXH_OkQ8TvgiXhR8DisB8bJT40yR9EOHexdwfGm3qwX-X1w8_HXLQSV4acuCWSKFwYJXKLdRVklA6GKS4QEIeilSwZIkm7Z4e7f617V-6ooe11x9sFL___bqBnhzkzQnJ6qAHYXiWvfubI2ZBy5DrX0bhUVnQXJbFiU3VKJG6ofr86c46mEO2a0E640ECTvLMCDzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جادگر کصکش من الان اینو چیکار کنم؟
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/79341" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تمام ارژانتین صعود کرد</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/79340" target="_blank">📅 04:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">جادوگر بیناموس چیشد پس</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/79330" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79329">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گللل سوم هم میزنه آرژانتین
و پاس گل توسط پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/79329" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79326">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">سیمئونه لاشی از تو تماشاگرا بلند شو بیا بشین رو نیمکت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/79326" target="_blank">📅 03:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79325">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ایفانتینو کونی کجایی پس، داریم حذف میشیم کصکش</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/79325" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79324">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این جام جهانی خیلی شبیه ۲۰۱۸ عه
عملا یک مدعی وجود داره همونم فرانسس
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/funhiphop/79324" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79313">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">نیمه اول با درخشش پروردگار فوتبال جهان به پایان رسید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79313" target="_blank">📅 02:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79312">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کاش‌ میتونستم از عمر خودم کم کنم و به عمر فوتبالی حضرت لیونل مسی اضافه کنم
ولی افسوس که نمیشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79312" target="_blank">📅 02:12 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79311">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الله اکبر ازین عظمتی که پروردگار بی بدیل فوتبال جهان داره
ترجیح میدم برم وضو بگیرم تا بیشتر از دیدن بازی لیونل مسی ثواب کنم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79311" target="_blank">📅 02:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79310">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فرید بیا بمال</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79310" target="_blank">📅 01:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79309">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهد حرکات بیرانوندی از گلر کیپ ورد هستیم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79309" target="_blank">📅 01:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79308">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خداوند و نویسنده تاریخ فوتبال نزدیک بود بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79308" target="_blank">📅 01:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79307">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم   @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79307" target="_blank">📅 01:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79306">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خدایا شکرت که یک شب دیگه زنده موندم تا دوباره شاهد بازی پروردگار بی همتای فوتبال باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79306" target="_blank">📅 01:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79305">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بازی جذاب قهرمان بر حق و تنها تیم بدون باخت جام جهانی با آرژانتین شروع شد.
به امید درخشش جادوگر غنایی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79305" target="_blank">📅 01:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79304">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پادشاه باقر امروز یه جوری تو مراسم خامنه‌ای گریه کرد و خودشو زد که انگار این منم که قاتل حضرت آقا هر شب از طریق واسطه پاکستانی بهم پیام می‌ده ?slm chi tanete
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79304" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79303">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">توماج صالحی رپر خوب مملکتمون تو رتبه بندی جهانی مادرجنده ها قرار گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79303" target="_blank">📅 00:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79301">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استرالیا با حذف مصر رفت به یک هشتم جام جهانی، حریفش برنده بازی ایران ایتالیاست که فردا ساعت سه و نیم صبح مشخص میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79301" target="_blank">📅 00:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارشگر مادرجنده اسپویل نکن</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79298" target="_blank">📅 00:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79296">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUMFZHPFLO4dOFF2GpuIKzwkD2WmuRc7_4iJSita49uLvw1SSMhB2Qhcfyr75xXJtKF8QMK38cijq0jwBV30v1p34szj6k8rDnXejbORbE-t83Uk_3mWGbombS_XevQjrsxydZ9rIQS46ImqFU_J2vZVGZCCK62LJ-7mwxzX0aMIPNCobCHeRa-XRdUVI9fy4dPLSE8qhkIHtw27mOoVceRVm76kHJYajEV-xJjxW_dsb2q8oWq56LYuS6ifKEzC-uPUZ9pH-aKWIK66ECXYIuDlBz-DbRUO3P5EIYNkOigAZiZp83ZfaAsKiGJafUWZwZrBJc78tDUOgPNoJPly7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت عجیب اسرائیل به فارسی درمورد مراسم تشییع:
بسیاری از افراد (ما) هم می‌آیند، نه برای سوگواری، بلکه برای اینکه مطمئن شوند او واقعاً فوت کرده است.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79296" target="_blank">📅 23:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79295">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaVePTBBFu755Km37DnO1qtAvi7zwP0QPcqIvGq_J_n7wH6ws9oxACeWnZ6xIP0mLvQbgDPMWio-ESrQm4HjmSv77RSgRBfirDMLW2UGTFW8-6PsZ_b4eM3rm9Pt60oHq9yuTkdzdZhQlsYaKmjKdd60ySpwbCde1nMUqItGTJfylGKcD22tfobK8e0GewL9R0EewXU2UMDMRSBe10LUICaDrP5EPfZAveIXSmX47w6aslxzSrSKAwkmes-o-vkPBwWNgB5NP7_O88plbkng_UiVgrXmCpO16HzbgnejhbVVplbOXWMqFb482Rw4y5jJEWMjD85JgRqM4oVm8lb_cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باقرشاه قالیباف:
ترامپ که کشورش ۴۰ و خورده‌ای میلیون نفر گرسنه و نیازمند کمک غذایی داره حق نداره به ما بگه گرسنه و برامون دل بسوزونه.
پولای بلوکه شده هم مال خودمونه هر جور دلمون بخواد خرج می‌کنیم، آمریکایی‌ها بهتره به فکر آمار سوء تغذیه و گرسنگی تو کشور خودشون باشن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79295" target="_blank">📅 22:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79294">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79294" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79293">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فصل جدید سریال سایلو راجب جمهوری اسلامیه و دلیل بگا رفتن دنیا رو جمهوری اسلامی نشون میدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79293" target="_blank">📅 22:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تنها کشوری هستیم که توش
هم مرد ستیز هست
هم زن ستیز هست
هم به پسر تجاوز میشه
هم به دختر تجاوز میشه
هم به خر تجاوز میشه
هم ترنسا رو کتک میزنن هم ترنسا رو میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79292" target="_blank">📅 22:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzOqVMQkGrA8UbhAC9le-S01LkqWzXFTND1te5E5HZLuCMXdo3Xrpg8mH5XvZkvb3VMzSPlyRpqwKRLbzSdvFAP0KPZvrhI3S70dZUDIVmA6OpRYzL5iE4elsMUMzoKoV8AsB8Vul7cjj0f-QYW026r-iujqewGBmCeFI2LPBOqnwSoKvLynI4pdzWfHXEyRLV4mjjKwi8XylVxhkMv24u5orJQMSC2RxTTCXgwG3i5PFsnPEKUe7ohFG0nO5fq8uP2yr5bhAkmbpnfNDChF5xhMymkVpKmu3adyemqQBTuzuLaTzuaRz58q8mXEMhfMWUaj5eIYr5KFo4F372kboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جادوگر غنایی چرا یه جادو نمینویسه یه دکتر زیبایی بیاد صورتشو عمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79291" target="_blank">📅 21:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMWBQG_zBVEi2CRsV8EryWZPdaq7lUZ7pDJze2jTcMnvw-CcGDhvzwozHRsel6R_dC8EWq3iwpaFpyUArSgtBBNOIcpHNpcU21c8ret0sLbSVghY2EGjDp4HqCxXay_F3Yi9fbdMMw5IqjUuexuxpQlnWCSpvDHf-EGvD3wtRqpao7nC3ec9Fk2mM5YBJYkuHiKVxiuYzofUGpVYLlEWznwGwLnhPKHol-BHSqxcs5NW_PffjAAbe1myd9YJ6GSSfbv8uoryAlsYCfgrO_gL1TfUfeRDThT8uQIUDOxDMxS185WFcz878tS0Uk-OC_uw4AoD6E3BO3q0_R9qdlpsBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کی رفت
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79290" target="_blank">📅 21:23 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">چندتا سریال تاریخی بگید ببینم بلدید</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79289" target="_blank">📅 21:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با اعلام رسمی فیفا، علیرضا فغانی به عنوان داور بازی انگلیس و مکزیک انتخاب شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79288" target="_blank">📅 20:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1up14oPPkZ2jocRSftdbvkmcTjOrGdwUFBV_EuqfuZQSKE6bFoenubi90DJNt9e9LhV8WkhAON6oft9Gk7XPqdNaokR5jxzHybwJsWwLsu-PtP9qCnGuwPH_v8q8zdrKGF85lJDMChfkDpYoS-C2OvQCIovSkS_TnF1giCjl4T02X_cbZ7pOTKm63WBLTZOO9sbFZiVqXnJeLp3uhMAaqiUBgidbXVFYKcU55VXR9HMopE0IEtGaiQ9GHOHYx4CYj_nZ4mfBiS6VD4mjl0b3wKN2wpj5a-mG0V2OHNQL9CRDbOZuxpqn8QkB9_Vw2OCyx09yIRI4ZWZnNrxRpRB2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه عباس یه خوارتو گاییدم عجیبی دیده میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79287" target="_blank">📅 20:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79286">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یکی از عجیب ترین چیزایی که تو ترکیه دیدم این بود که تو کلاس دانشگاه نشسته بودیم یهو یکی از دخترا با دستش نماد گرگ رو نشون داد و کل ترکا شروع کردن به زوزه کشیدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79286" target="_blank">📅 20:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79285">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLFNvhtt79UikRaCqSMsLgUmdZGFFFRkKBBku3laZbxvjt9TM57J3TYwJ1mUkA5eR9En9--7tIvYJbdnwMPSD4CFTNdt4HEd-e_1AOFIeuII8W2aKGvJpn3YHE97qf95fjjcy06WzHbLwQNiQEAqvzGM98HO7IP1utcCfZAdwgo0ufQMt4350dZNJcp62h25Gj-Gr7W2hjMfxq27-amh6Ua7dNK80PGlMyJAxMkqc9Oj4wD4QEpkahakjR27cBouheGppiZVZzrHAXADrNJwVXOedjsordgTGENGu3eHbBUkiHbM7GVSyn2W9bObp-ooeln86a7zqSbevORN_TS9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ژنرال مرحله بعدی با چه تیمی بازی داره؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79285" target="_blank">📅 19:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79283">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayNShIhUf-nt5s99AzHOqtSEeuMRH85K2KZn4hE3ZyBELNeXiE1ns88df3ANMAfrCesdfBs4jhD6ApcKi-5KFXn7fcsj4CSrpWjCZqOaS3rI_FhiLvKG8DapS_T--0Q7dKzzyk0MsmQPjgeulsInpyHb2ypaBhDmSS8_80jsSGcwqLZTeBBtTOlheksbqjyedZFpF8SiGDCdtF05PBuZXgjB9eRAuwH5kX_SMf5HVpBCotQyYuoVfuPXiu2Taz5trjLQ4RB0xuEllq_R6nCSOUJ4SnOxs6smQyA4kGYbiMj6B5QPS5yEyPvq19TM9nOJb1VF7XJXKY3firL8N6z1Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79283" target="_blank">📅 18:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79282">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hF84PAdk_S7JQZh8LzVNb4lhokzzjCzxL832c7TWj8H3WeswQNrk8qnyBpwmO5pLPm7L9mTSdKLyJpq8nWlC0xYgsTUTA_SrVBOR9hLieW97bTrZ2v941RjPIQ8fpidCHwxwrJwHldfZ7t457qkLFOzIxY0i3y2osv_pYIOb6sQBh6iKmYFKfIWc2BpXnZb02sShTHmWW9TUDc0KzDPX7e_HOD5lsyv9t5C2PexrXafN-nwSh0B5zI0u9WbkfBsFJ1jyF7HInqYoC_UM91BFFbxiUihi6YVgJ9t_sozVXvKQAoWEdhLB4D2ghw1aGjT8KQYSFWp2cnGEAeXoD6Nc-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهر حیدری و ارام طلاق گرفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79282" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79281">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqDGXnIpfyHSGRF1EbcMMzbMml_45CKKqXE6wNgAEPr7NaMgRSd4_Vd9_NebUg73A1D--Muu0KB1kOPlGU2uyx0-tfMGADlMMxr1sS9edPW8nlXVHbUxU1ZGPisLYKtCy8vK2Qcy0-5IXTjfY2bGdN4eHIuSjxXK6df8cLOfLYPbNrpt4gM-9y0tnfDaFWjBdUqAzpxku6cHb6Y6oWGlZ0__T9ALB2CUsRqZ2L0GmSEUm1C_YO6UkL64Ev9x3JXLXiXt0zoPA8MhGNXP9yG7Wo-19ByIFUeTPbIk1qEQkRMSesviXDWiE9-z4IKrkWihVbMeOHfk1Gn-Vre5gQasPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇨🇻
کیپ ورد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد شنبه ساعت ۰۱:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- آرژانتین با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- کیپ ورد با ۳ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی استرالیا و مصر برود.
- با توجه به اختلاف قدرت دو تیم، گزینه پیروزی آرژانتین می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
روند موفق، نیازمند توقف‌های آگاهانه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
G12
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79281" target="_blank">📅 17:55 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79280">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhTHNqsAGso70bZjzj8wo46MQ6Ne6S8VFNz58lL18-9d_VmRgz59_sArsAV8TI7zytjUb0sk58QTrB2mQdQsSL7GaCjdD4pc6KXv8VvXuzxiez0xt6a7JXRE0IgTi3tl27fbfmr10_LmuWiFKFzJdENn9L5WBYbarGP4AAGmkWWZOU061qkg1nJSuTiieGh89v5rAdIyko-367jjaF_QekrlmJv0Br4dRixHvyI5VsNXxrKmHv6nEisj96sRwiURFCXOwu0DjywFvEMjouo26BEdiZsugrotRyEbQUfHCfkxKa3ZMVCEma-3AZ9WzHhTZgkqvUtWxjEjntSegs4tQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه پاشون لیز میخورد میفتادن چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79280" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79279">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBNWFCCRjo-vc2LXtWOw3x_smyFEgLzZutbS0UKb9TJs6hsQeXgnT6kK9wT45GPN1vDaVIs6704NOGDoJ63eA9rz9ymAWY93k91WTmyaB3qQXbOWiUiFWA1pPzUzPnMakHg0FwdvItRkI9hJzBk97ZkGNfhP6F7I-CqXfHEG0da-DuhjmZBVHw8P7Kl_Dxxw2lp3oYNwYH1iz6OurSAon7p2MsnfWwAEaiMSOTGIkcSMnrTMKiht6MGMhe9cFPoPZNskU6ZaMzAf9l3_MlxTydhIGSEc4pr_fyB5QRsg75S_0jgsx0p8X2dc03K6sQd4Xz_Pw5NNRLCTtkhD_dzWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79279" target="_blank">📅 16:58 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79278">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=tJIg43xVpHICxD19cuBTVf_xxR3EhCOHMec0BA6X1Jt5esOMo-urLlRKSSQGrJW6jnFoBuwtFLjdAYpERWoCBeaz10R4JIA3q0dHc6itnbibPz12nBF87H_AoZi4C6aLQ0AUKACrrBOWvd-_zL1H3yIyE4f3bQX5AGv4Lec6bNgbZpYfhYR-rXekAFXHp8CNmrTXK-L7yKOVy_1TBeBmv5O9e2fTow80zk3K3N5ZT7MdmWZ3Xw8NK0efW7Gwoo2vVLhHiOD8l9eRo9u449o5ecRJtVL6DDyqWVY83WFizdsjFdPi6kOsZlEkENYNQfTtjxI8dKek6b5rHy3h8rk8xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c4c7250ff.mp4?token=tJIg43xVpHICxD19cuBTVf_xxR3EhCOHMec0BA6X1Jt5esOMo-urLlRKSSQGrJW6jnFoBuwtFLjdAYpERWoCBeaz10R4JIA3q0dHc6itnbibPz12nBF87H_AoZi4C6aLQ0AUKACrrBOWvd-_zL1H3yIyE4f3bQX5AGv4Lec6bNgbZpYfhYR-rXekAFXHp8CNmrTXK-L7yKOVy_1TBeBmv5O9e2fTow80zk3K3N5ZT7MdmWZ3Xw8NK0efW7Gwoo2vVLhHiOD8l9eRo9u449o5ecRJtVL6DDyqWVY83WFizdsjFdPi6kOsZlEkENYNQfTtjxI8dKek6b5rHy3h8rk8xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کنم دکی پولو زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79278" target="_blank">📅 16:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79277">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اینستاگرام مادرجنده من علاقه ای به خداداد افغانی و خیابانی ندارم، دست از سرم بردار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79277" target="_blank">📅 15:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79276">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0TaQy1IP0zfPDfCsXVAxdGWi1qsYGEK-Q-FbmSBY5HDtzeD76T7wuwT9GoRRhKVbzpW2IGKxRS5ev9rlIH242jH3S2JcYVPqNqVkxTSYonaOS0wvXpU6FsI4poz4rPNn716b5zfMQt8NdmljEjCe1yc7ohL_33tbGlb_JqksJgbdSpni3QxBh9DTFYNQFneh5MXKk9qXqezb8YN8XMtiGEPGCeQUkB1o7AZVyGLBnryCul9wcbML6vzUetHlFE4-GXe9oT61EX560xcihfMO4wbspdJcdTjwGLd1CVxOm8R1BQwvuZn8OlCLEzEPqFI5yIqLDV-SG5116wYwh3YqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقریبا تمام مقامات نظامی و سیاسی امروز تو مراسم بودن به جز اسی کوهن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79276" target="_blank">📅 15:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79275">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کاش یه مقدار از پولای بلوکه شده رو اهدا کنیم اروپا کولر بخرن باهاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79275" target="_blank">📅 13:53 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79274">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیروز میثاقی اسنایدرو دعوت کرده بود، بعد میگفت آره ما سه تا مساوی اوردیم شایسته حذف شدیم، اسنایدر گفت خب کصخل وقتی حذف شدی چه فرقی داره سه تا باخت بیاری یا سه تا مساوی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79274" target="_blank">📅 13:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79273">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr2pQUHBdWJAjE1ULyPE0iTgllDr5j-JrmJRQ0NJVX1qB7Y7JMqZ5nRup6BVqMW8E4VTKTDPj2cIcPXC9skIKtddTyOhYo_DKWWLuXTpN4BJ5fegyOu8GXR4Ex8L_Ckg3Avurv_JTM6zFrWvaskePRO2y6Cbj-d_iS25wDuJhEFx8CA0-IBxAg30Za1tl43kprYsc2TZIOmoPTjuj84PuZJGk556Ui4n9vAYvKsBlKykKuh09dHx4lHZHCnY9lsqR3aVoYR0zxV9bO8TqFcLiAOVw83upNuQ08gdpurX52Nczuihhve_XruA6i29G6c2daaDbojrZEs9IZyGyWBDdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سروش سروش ببین چی پیدا کردم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79273" target="_blank">📅 13:11 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79272">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">درار از جیبت بیبی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79272" target="_blank">📅 13:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79271">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hu9TC1RGKcfEOUhNiCYqex4xNW7LyS2jgYvlzPxqyUp5BuV_3SxCAxi7nBGSD7W5MHUTqcMv6jy2QOtfkHzSQjYFTq9PFLiE1Veo_9dUElCnG7dn7UYAjGUfhRlOHb_CwCYhIsPU0oympnJtS-xf7i_bbFL21bRTGnbJMZOCpiIT9N9sUV_EaFY_-iEF3G8VZn-OrXUftdnpwaklRM9QxKv0L8qxHHXchrEpmFUYoaFdleyo8peXk2oCYbie0pBpmeZi3WtGnMHwFtjLc_qsAOLcsmI7h0dfofk19_mjhuToN4XE_XSrO224jGH5MQXcxmEPbt-UzJmT1UwxIjOnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام امنیتی اسرائیل  در گفتگو با i24news:
هر زمانی بخوایم کسی را حذف کنیم اینکار را میکنیم. هرکسی الان در ج.ا زنده است یعنی هنوز زمان کشته شدنش فرا نرسیده‌.
همه مقامات ج.ا در دسترس ما هستند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79271" target="_blank">📅 12:36 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79270">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HAbCfNTHJKtJt01PVJuXJu-4q8pxJsToxJtADyJsjJ1Vdt43wjHGZJYcQTHD95hgEQjmO8LGP8DXchsP4uYt3eJJ8FsIQpNSZfyour4GvT0F95fUqFiDM6xNZ6NU_yjihgMGBOiIbj7vGPhqsLq7DFeEZhCHSYADjm9pwDRMpOHJVKhVq-f_G3vc9oeIlZ_wDCpkZDi0wHgAM1KENh6pzm1cuWwAKFNUjDc3FLi-AWX3MLwSk-fbaiABgsWiIae_egYaeVsAlX4G30muYXML8Z2UU3s3qJrR-VjmuqW3RLPJrnCzVz8eAS6Z8QJF2NqwKxqzfrJ6TNcBR8u5J5iDjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">که گفتی شاه ساندکلادی؟
😂
😂
😂
😂
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79270" target="_blank">📅 12:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79269">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skZd2AngH2Nw5IQid2TivXInEei1u-aNg2AM0M50JR2ydYeDeAVCZXWdAQo5sp9o5QcPrItS4jTOMUXfLleJCzp6zXjdwJDtVkYphiLwOmJvF2hIoaNVEb0HLLFQr1nVcBmjgoPaq5p2bmIy8YByRS5X6Dpynxz6YKqVb3AW0qqe8BB7BkW5geGdsnkI04cyMIb_xlG-stWBpmUcl0TEYYECPE1n5AyVrojseMROTjJrn2ZChnUa-Lazn-ORritk2BXK9uD8M0LJX7c4F3gSCYFWmnPUnulmEM6Id1muSowzxVcP5Nazlv5k91PhSeFbYqC3IsT_5_1s9NSl_nSMWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
آرژانتین
🇦🇷
-
🇨🇻
کیپ ورد
🏆
یک‌شانزدهم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
بامداد شنبه ساعت ۰۱:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- آرژانتین با ۳ پیروزی (۹ امتیاز)، به عنوان صدرنشین از گروه خود صعود کرده‌ است.
- کیپ ورد با ۳ امتیاز، به عنوان تیم دوم به این مرحله صعود کرده‌ است.
- برنده این دیدار باید در مرحله یک‌هشتم‌نهایی به مصاف برنده بازی استرالیا و مصر برود.
- با توجه به اختلاف قدرت دو تیم، گزینه پیروزی آرژانتین می‌تواند انتخاب مناسبی برای پیش‌بینی باشد.
🧠
روند موفق، نیازمند توقف‌های آگاهانه است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R12
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79269" target="_blank">📅 12:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79268">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYJECpHoMm2_sd-ujTZr-CSVb6rgy9CvhtKYYLggmVmX7FlTAduaFwu9rwXjF_CZqeJO4ncEl_e0SH0bdOJFBXGcKRs8wyPKF4YYfSGuIvm-tKCjRZua95EM7SNQoJN44R_VVBwxMTjhCmzhaSwMMmG2tKKW82zob8PjFOEJJnrWKnDBHrVfybUkQsx99_EGh2apkPhUCOP9XuHdS1YOWy7YUO_Y5Ul6BKR5ftOzHmNsk4sdlHka5wqrHouYsLxLzeVeUtKQRfFyXQjzGwuT90Sn08loLIrg6B5TTqVBJYTNE07UnO2pAVjc79MlYk38scP_ZNEZ1kvUPcjuwJ4cbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این بگه همین که نشستن مذاکره میکنن یکی از اهداف آمریکا از جنگ بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79268" target="_blank">📅 11:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79267">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یه پرامپت خفن میخوام تولید کنم که توش کون نیما بزارم با آهنگ ترویس اسکات، فقط برای ساختش به خود نیما و یه دوربین نیاز دارم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79267" target="_blank">📅 11:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79266">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4PRdgX3zxow-8WSrIV4KNgpZIPAsZZTdhgp49izQv2aZa_8eA0yDplbYNoZ9q-3zjq0Et3OtMYs8ze2sntQDCEjA2DRWK6ctb0WKHXrdzTmjZuVZIqS60gBgz5ckr7Das6hfREJf8NprL_jE2Qv6lnoym8gsPFWWT9cKZHpLuNqZYu7OiMssfWSffNg1ZB0DN3piipsQv_1uEaO94h1VDTSIa-qW6aODKKLIE6k2N2UkCDaZGDiLo2F23M2j7Qoh2OiLWYFmHcHDOf2OxnNVSa4wL_PauYQ6MRc7SqD5i3hJAxSYVSPrmwKnnexI8b3Bi8LWTr8KU6Zzp5QS16PgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت خفن اوردم براتون که تجاوز پنگوئن به سیاوش قمیشی با آهنگ دلخواه شما
(به جای **** اسم آهنگ دلخواهتون رو بذارید.)
A medium shot, front-facing photo of a middle-aged bald man with glasses wearing a plain black t-shirt. He is bending forward slightly, his face contorted in a realistic expression of intense pain, anger, and physical distress. Clinging tightly directly onto his back is a full-sized King Penguin that appears to be straining hard. Both the man and the penguin are staring directly into the camera lens. Photorealistic style, studio lighting, isolated against a solid, put **** Cover's music as background.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79266" target="_blank">📅 11:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79263">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lEPxAptGXEBVWbGLyt9bsgI70vyn4JwAdnSR2WrwVmodFtnlb5xCm4OI4lJwroU-5YAAh8qHkSEsVIutFDVZwCFg1EfbqrgoU7WVD_-71VlM-BL6ews6Y0dpM7KGU3qo0J9K1zXkhhlX2qNu5MSSZ2-kkQtn5KdJh7KsKq5LRedBvpI95VUw6SDHA0A0ru46ghREmhYNNsHr-o8ldXMPhjLRxz9j9kbT5t2vORaBVtYoxca8ZPRf1QQdNxLH1kxlwBB8LGJWzvqlguAdEH0kaX9MxMUZJmLKWwlAU7FDeIY3VJP7MPbtxaMpLx58e1wHZ55uJBgrS0nYBYzsNWEeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4CpaxDRvlHNZr9SfdgH1gebVX4i3TdxkUT8E4N4oNB00MA6QkeoCsnGChZkjiFeEPrOdEJ1fxW6KnfH_GpyjU-uu1BWb4RmuXpEhbWo21jIRYfz7_dFC0uMi9excxgyu4LDouJmdInNVbqiRTVR4dy0U5u2ZG5XVieI4oRn_ilMZCSa-L6e6Rw3bq_33K5PFwRDIlqjDWomNMHCBAMLvERjHCFZsN-bXycF4xIknNBU1_yM_4v9jBAKABr58bSfTBLQpREY9u16vGBUZ1d75ZEVVgApg802yrTTVp1A2PS8Y3cXdDVmnxQmuv5JIdF5zOSUWKjkLjleHno7FpnAFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پشششماااممم من از الان طرفدار تیم قبرستون اسپانیا و یامالم دلیلشم به خودم مربوطه
😂
😂
😂
😂
😂
😂
😂
😂
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79263" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79262">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79262" target="_blank">📅 10:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">زنوزی: تمام مردم ترکیه قبل این که فن تیمای خودشون باشن فن تراکنورن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79261" target="_blank">📅 10:07 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=aTJ9GK7EMGMZDDnWjca4taP6UVAd0wGIA_26vSpbTXEAUa1nGVDG1ObxP9PyCj6gNBFp0VBDBoCHQG4Dbiim4zAPBHV5XVMWSJ_bBfsYw5irM5rwo2WZ0h9uAmVuyygdourUjxW8y__5RmUpGuLRmxAXbf-9sSk2bFBiHnBUV7C0KhxLyU-wHM_GqqRk7OJ6draEoLyWSqkGI6T-lH5d3V-5oe6eXRyZJ1jgG1svxxoiUJSf10HnKMZCOICVkxkrQiLQkRHhW2sPZ2VVBPxI-_bX4wdG6rVh_1KH0UsUizvjljO0lHAYVi_BCalnVpGDVxAeOFjhj7rsY_IH8NO5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08e68880fd.mp4?token=aTJ9GK7EMGMZDDnWjca4taP6UVAd0wGIA_26vSpbTXEAUa1nGVDG1ObxP9PyCj6gNBFp0VBDBoCHQG4Dbiim4zAPBHV5XVMWSJ_bBfsYw5irM5rwo2WZ0h9uAmVuyygdourUjxW8y__5RmUpGuLRmxAXbf-9sSk2bFBiHnBUV7C0KhxLyU-wHM_GqqRk7OJ6draEoLyWSqkGI6T-lH5d3V-5oe6eXRyZJ1jgG1svxxoiUJSf10HnKMZCOICVkxkrQiLQkRHhW2sPZ2VVBPxI-_bX4wdG6rVh_1KH0UsUizvjljO0lHAYVi_BCalnVpGDVxAeOFjhj7rsY_IH8NO5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79260" target="_blank">📅 08:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">پسر خوب فیفا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79259" target="_blank">📅 04:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79258" target="_blank">📅 02:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">فیلم مستند "از چشمان جاسوسی درتهران" که حاوی تصاویر مستند از چشم موساد در قلب‌ تهران است و از شبکه ۱۴ اسرائیل پخش شده است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/79257" target="_blank">📅 02:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رونالدو بعد از جام جهانی از تیم ملی پرتغال خداحافظی میکنه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79256" target="_blank">📅 01:57 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">امشب یکی از تلخ ترین شب های فوتبالی برای رئالیاست
۱: یا شاهد گریه مودریچ و خداحافظی احتمالیش از فوتبال هستند
۲: یا شاهد گریه رونالدو و برآورده نشدن رویای قهرمانی جام جهانی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79255" target="_blank">📅 01:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79254">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79254" target="_blank">📅 01:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXJ3A524eEpZTEmizkjDw9NWa2lNKbXLxAo7Vga6O-FZk3FjSxnQvh_C9TagJEnEaML8DWkXw_o5hrPe2-_GXRWEBjUFhNZuOyqEAzUWkE81n2xfntdN2DLsxDNqN5ZoS3ksUJpxgkguygHTCNrAMIvzGBhpo1aq1Ch0_e2Qls7TrRaUnBQTmvMDvADok0a_WKvEGXkJXYipcCH4jRjbwmR8RYfCD5KQwleWuHH1Gf--iO9YP8iX91fIoxHrFMckKv5-fnZgazlhNlTl8C7bojIDUFSwTRl7DsN7eWcV1wqePvh2s-8q_9MYRvNe9aaNboCXOm3FQLIoFyP5kU7rTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاگرد سیجله دیگه، زیاد سخت نگیرید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79252" target="_blank">📅 00:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مطمئنم یامال کرجیه</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79251" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7A6qP_UsVo--PXRm7qUYnJHYaxN3z2pksPyaXZCD2EI9WPcm8EDEGGRAvH6FJzXFD1n5rcmM8DkKbVTQ01cRkEkdyPdnwZ9C1PpjSKTpGlxWjSd30IbLxdTU260ZTVtMNscBpb8YoC_0Cab9Xwqq0KPBbBiUt0uAIZiZ_9o8r9KaodD8uu-5UQ29QT9A_Hwbz5263HYscERdw5wc5Zt8CT0Pa0H6SizD-HPlGIDIgsdxHbgIUT9wV05R98g5yjCC2e_-eLD2M_i1nId139ZGQWqFKv9kmnU3MNrc0SukXJ9AqkN7HiwXZv9uMNPwqQ9md43ZE1Z_cMsllfHqSIUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و مشخص کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79250" target="_blank">📅 22:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79248">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I35DZl_nxPuJDRnW8Yho0dPHl7HlsIuSpC27MjVvIK8vfQOjLJt_AcJB-DZE4VXqajppnx0Q8q2pn3Hx1wiev5Fin_qOpI_TDCXD1Og9dZgD7PKzVStio4qTUg1P9G0zw-Wb2jMvoMe9QqQsQMqmcOKsDRuBSb25ptu_6_J1QivKvy-krZHPL5JrCEn3puqZZjDcJvNFzmwiP6uwKqiyyO6zpPbdWj_biD0eb1k2iVxZBoNdGaunDPghIyPQ8F4Nwy9oykA4ph5PpodNODaq4Hq8HcrXl-b-e4onmMRh175YuWXijryokm3fq9VpY2zYnYtO9lIoqNfoPLPSS14UzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوری به نام “به زندگی اعتبار نی۲” ریلیز شد.
Youtube
Downloed
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79248" target="_blank">📅 22:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79247">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QP043PskMWkPxNibP6mdu-yJdQebnKlhbnT6WCNosNfJjdFU1ycARuwL-eYDeuOES67poji6XBoI1ue-dq0_wTef45TNyqkw1fKX_Bz73ERc32UTrDMxKN3DcdQv3sQqfh0BhN1gFuHq30kNhF4sHeW0yxz4n1A15IyWeZDKQ4RbhGo7G8nuPsLXT1yXPmCmSjQHvpKwYhShTCDvpcERXyNq3Gjlo8CFl3Q2cmg3-ihzkSP1DyRNS-I6RCG4gFyxsRZEiIlxNgt0ncF7SY3KsRJZVZ8NIWI8tOu87kgehzrPSFMGPWgR--5ZMJyN0t2Ke7DwdnectTj8YzaVfz5Zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هلیوم جان قلب خیلی بزرگی داری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79247" target="_blank">📅 21:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79246">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ns1NVNOqLu7rkbXDbBtPMTjERVaWu9BWAlBErsWs8yiluh5RDrKq2KXTBNgEDLXLoN3mGffMvNJpOZwBaAbzkcHTFhuNNygRejFETMz6Dd2LKnIRiZRDqkrnU5bx6gv6B6xhO57s9bgS6rd3ORl8du574cThF1kYA51zm6kCYrRLprVOHbGcmAOjIaWVxAxkjiq0x1dPvYvMTTk67BzKjG9IYa-RH1rVrRDJGHpN_blwSwt89Ga8SxzBrv6hmUtByXd_FRAsEPn26B5YuA5cPHSYoAfdLkVpU8phsTfgDDQLcouQP4KTcegViWetU4oll4AXeRPEOWrbmUy2ua5lIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
با Legovpn وصل بمون، همیشه و همه‌جا
✅
سرعت بی‌نظیر برای استریم و گیم
✅
لوکیشن‌های متنوع از سراسر دنیا
✅
قیمت‌هایی که نمی‌تونی رد کنی
✅
پشتیبانی ۲۴ ساعته، ۷ روز هفته
✅
کشبک ۱۰٪ روی هر خرید
🤑
کافیگت رو بگیر، دنیا مال توئه
🌍
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot
@vmoon_pn_bot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79246" target="_blank">📅 21:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79245">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">لومر؛ خبرنگار نزدیک به ترامپ:
مراسم تشییع خامنه ای پر از هدف برای تروره. مراسمو بمباران کنید تموم شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79245" target="_blank">📅 20:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آفریقاییا یجوری تو جام جهانی با دل و جون بازی میکنن انگار به برنده غذا میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79244" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یه خبری اومده که خروج از کشور واس کسایی که پویش جان فدا ثبت نام کردن ممنوع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79243" target="_blank">📅 18:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxGvHdsXj-_an4LQVCG5sZgQpSiDvpqclCvNo1AYKJ8GYfeyT1bCBo5VzLKjsJrlQPkshKpgHYQtHpOaqgqiRUqLhhznrFQ37GyzsjbBu53LEEpSwmVjJK1obCuuyYwDj3n5ScC6Dn3sYDAD6ooNIfzzdAe6QLned-J0VRRsfpZfcrfzvG2h5SVq6bRgrkxh-dKQsWZ0RZAiHsFDSHvDiElbyX76OpjbJ3m5NkNZUWZUJpo4sC2P4RBzQaFfJ75v3fhxix8zBZikbT7wZjVsCqXQcLWk2kNElEo1BxnubUd78XzJdy6H7i4SWkYkNexNWUejNgs45FwilbSH83Q6cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش بینی سه هوش مصنوعی واس مرحله حذفی جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79242" target="_blank">📅 17:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAY5FVTo6_EEiRbIyT6A8ZyoTVFt9Bnv2XwJqtIlxD2eDhKmce5x2RnlJDK-CcdMnknZg-j7CqTNQN150fENBgmfAa5HLpaKsQyzUi6BJ38X8scVJ9aqISpjuwsHXqiVusN5A4xPWzO8JQMzJa4BemRJRsjwcImqyNEmuLFaIvafAGESC7JXUDYYMrxwfyfJYL7olFvzY_BaayZ-LHU5xTEj04LC1LPT5wA3r6DqxT5hGXpIv3JFSNwytOvClIKI16NYFYKBIO21C6hUPHLjJrTo29QHJaCoOn6ViS9ih3bwNb6d9yAn-EQNiHO2XxSLEsmWY8Q57MgbMurJCFI0Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد کشته های اروپا به خاطر گرمای ۳۵-۴۵ درجه به ۲۱۲۹ نفر رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79241" target="_blank">📅 17:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsCEBpfKWNmRIHI1mAqzn98RlAUSOWm8uEqw5kIn4m0iDrqONin9ZqxSdxn2S_e58TlkBS9CUN10Guc9I4I8f5keL8yL0cTVfSb891-tDpl9mFyVJOnuBeBHL0G1YxWIbjydWFXZEUViu0Yvt2vzEPEqv1a6ngtfZxNxAGZ_QzdXqM-NL-XGnoL1FCcHu4BBHrB64gb_GlkIYgTl2g0cFEpBTGyj2l4cv3OFw_54pposMLqzDMjHa1VgPyA6G46TKOkKoa1IaIsf-Z1fOhWoIGRss77eaIJsbdnuxQv4b6A6VRDPgVvID3ECcVdUCPAEp3ljIJm6zfnAZyxOWwN4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر منتخب بازی سنگال - بلژیک :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79240" target="_blank">📅 17:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79238">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مامان شام درست نکن نمیاییم خونه
ویناک شام خریده برامون
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79238" target="_blank">📅 17:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79237">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwDmsAFGRL6evK-HsfMvVPJ_c2tY51V_xxrBP3E1wOh4gOlzXmQ0bX3SKD2byf4unkaAmZyAsHi0INUyao60Cb33sRO5q8xzYjxfo5cnSV-Tc0zrMU1j8B8LoVQfulg4BB4C4nfpetfehoCCkUn9usN0r1_YkfyDOt3z9bioe36nZ0hH2zEZQk5am5TW1TtZqNbvDRi_dpQlXNdtEoPavubJ-dlp69eKO4-rpGpr5adReOrz9zpeHc6PbhB99PsK6nDJ3hN3aTCy0xJ8wgmAS0tvmlCvkt6Hdg0CDBj8nOgrfo2X9DYOWQfg9SuNcaT88kysT5aYwfn6rE4xx-dNJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب مراسم وداع با زن مجتبی خامنه ای بوده (دختر حداد عادل)
پ.ن: مجتبی تو مراسم زنش شرکت نکرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79237" target="_blank">📅 16:24 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79236">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">میگن ویناک گدا گشنس بخاطر پول داره این کصونه واویلا بازیارو در میاره، خب اگه دکی نیست بیاره پول ملتو بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79236" target="_blank">📅 16:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79235">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بذار جیبت بیبی از بلادیا پول زدم
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79235" target="_blank">📅 15:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79234">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaGBHZZZQ-NlQsEtuXUonWmEA5bxgwhVGxTjs9s40__DbrLpO34d1534f9AObk-BXnA9Jwjcuu7bM4RW2l6b7ddc-Ap-MJ7y5Ja1gZM2_ma5gotROqeIRY_TQgxZt1uQ-iRTOd0gy63CNKZQsTLvr_AKLm1o2VETbB_yqJidFyRiiPxb4skk3zYAd3IzFBGY-I9h8EnjK4dXc1avg2e2KVEB49l7mPdAqBLcOV_5j2VRfpcsiKaUNk0xLd-jueVGYLuUNoBGdDpZMkcmSRvl60Fr0sEm6AGEmP0o4viFD491_IlCRr0XuoAs8eeQBkF1Mun2H5o9aVN01vItwKwjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به اسم
ویناک فلو
ریلیز شد
Youtube
Downloed
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79234" target="_blank">📅 15:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79233">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">نفهمیدم پیشم بودن سارقا تو بلاد هوس</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79233" target="_blank">📅 15:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79232">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ویناک عجب چیزی داد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79232" target="_blank">📅 15:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79231">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اگه فان هیپ هاپ نبود بازم تلگرام میومدید؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79231" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79230">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli</strong></div>
<div class="tg-text">رفسنجانی این بی جنبه بازی هارو در نیاورد
که خامنه‌ای رهبر کرد
بعد همون خامنه‌ای کشتش
این بخاطر چند میل پول داره خودشو جر میده</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79230" target="_blank">📅 15:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این کصکشا بهترین ترکای دو سه سال اخیرشون فیتاشون باهم بود، ریدن تو همچی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79229" target="_blank">📅 15:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79228" target="_blank">📅 14:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">درکل کل رفاقتا رپفارس سر منفعته، همه اینایی که میبینید تو رو باهم رفیقن پشت سر هم تو پیوی اینو اون ناموسی میکشن به هم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79227" target="_blank">📅 14:30 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چمن کونی پاشو ۷۵۰ هزار تومن بدهیتو بیار بده</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79226" target="_blank">📅 14:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79225" target="_blank">📅 14:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79224">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پول کاگانم نداده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79224" target="_blank">📅 14:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79223">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79223" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دکی ۳۳۰‌ میلیون تومن پول ویناکو خورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79223" target="_blank">📅 14:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79222">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کونکش برداشته به باباشم زنگ زده
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79222" target="_blank">📅 14:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79221">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🗣️
چاقال چاقالا چاقال چاقال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79221" target="_blank">📅 14:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79220">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بابا
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79220" target="_blank">📅 13:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79217">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79217" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79217" target="_blank">📅 13:53 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79216">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Dxa82ppsxFKK3lDnD1v0tJzK5MsvdiqFFNoTK8B6niXTdf0zDk845l9jXe1-f_J_BvO8kmJbpEv-zmzqQiSQYX2-8rMfbYCpUTlaQ4tmQl5hr8iiBl8XbyC3XtRCuZydd8qixhcaC-lO1R189SUK4xLS9g9TxLy5VsqqxjJETKaotUbDCLU8vStDNAcMGoKwGBpHFb1IxZ0Z_qdeCIzdbNEZ-t7vUIJ474yZ2GjO8za4enxQ_w-FKGIpQOh5JpOIpWuuvrk1BQDfB1PpiwtU0yP_hZJYuqWgXB-JRUsDPyZNyJC5sCuexrFt_BWlCsmTRQGKQAdzIUuzbN1tVjmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز تا قبل تعویض شدن مادوئکه کل موقعیت های انگلیس رو مادوئکه ساخته بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79216" target="_blank">📅 13:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79215">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">تاج: پیگیر هستیم به پاس افتخار آفرینی بازیکنان تیم ملی کشورمون به هر کدومشون به عنوان پاداش خودروی لوکس یا خونه بدیم.
- جوابش با شما.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79215" target="_blank">📅 13:15 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
