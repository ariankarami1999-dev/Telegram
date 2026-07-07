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
<img src="https://cdn4.telesco.pe/file/OXfZBxJXwcQA6tYk7B0UZw5IjDh_LArjxR3rICAipzw3hukEOejxiFFb4PXc68sVWrYuW3z3YjMXQyz-zGPH9EHElvtiKcKlW1glvfWolO-NbUVBapvobXd5uN0SnlDc32HkiYXj3f1sCjMAA9mSkk3tWA45KCtj1kE2l0VaMxymeaoYhXejGKsswmaupSrtRIaTUEtNAMikbtOgDXzkm1-cEXJ0lHyRxTrTHd151-fLRb4wrNZcEaeqACldGrN5LltsLTsGLNwpfOpWRNnO9EkK3xqpMgBPXXkiSHPsqngEOfjS4Jb9h8dsT93iwNaPA4y5oNKYJCouy86JB5X5zQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 195K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 14:39:20</div>
<hr>

<div class="tg-post" id="msg-79575">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/funhiphop/79575" target="_blank">📅 14:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79574">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O87moylNzYldv4tEhn4cxtmlxlB6R0YOAGpwwAWOtxzJT0Z8MGe7QJzwDzasMbLTk_GnWa9eFAIIMjDUzPjWQAWvbGTM-txUHEY6aUeGNitU-QAJYwI8dOybpdyA-zHDA_lrrYka1ICvZK0IgxOXAnP4ceQScXWRe2ixEA2fSwVY_MLTnNeIvwC8eRWC2s_KYzKAYuIB-g5zGPNCsMhjxtl_OOYVG8Iv1Ar3NZwJmRzF1xC3l_myzIFvcsm9rP2wcEs-BEQYD8N01gJpmj1GHynGvX4tPC91sbgRTzEwbSBMQ5ErGxacTqbmxxdgYXjmjOvF4gyW_pnf1yUTN4KD0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی میتونی با کلاهبرداری از ۱۰۰ هزار نفر که ۲۰ دلار دارن ۲ میلیون دلار در بیاری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/funhiphop/79574" target="_blank">📅 14:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79573">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">هیپهاپولوژیست ی فوت فتیش دزده که بعضی وقتام آهنگ میخونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/79573" target="_blank">📅 14:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79572">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه دکی لباسا و کارت صدا عمرانم برداشته نمیده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/79572" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79571">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jK7lkSG--_ZAPBb5efUFhf_4iutrqacnli74HIHbZ8nf2p7dmFdizX4zYjhiwSFWB68k3AsGrEhPr1AtY0O1I6svoCuWadb1bH9oZj0Ga6-a-r_foyst3sfrB4L8oBYoZYSKOuo6Sx7lvT8bBHUyMdL-1F2cJ-88aPnmVGHNg00JWF014vhasCEnz_FWVEYdWFVokaVNxf2JMLUQPhnBpkSnBoK-LvH5Y4uBBGvNlxt-p4_qTHI54vWrQ288xze8jpm600_hb7LyWC7GNx5FMRFsw9diKglfjpAMbKGratZVP0E892K3ju0vKNGJopY3IVb--CLpm6AC2IxewEqVVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک بلادو دوباره را انداخت، بنزین زن دکی هم عضوشه
دکی لباسا و کارت صدا عمرانم برداشته نمیده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/funhiphop/79571" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glAjdqjOCwzHcS-t4p_QFxbrTCjuabM6JgRvzn-ngRAsS17AmEiRWZ7yuQEl8oUc_vpMi12MvykQKiBD9cpjlh3RRZEmLbuUnmzfjwtnb6ySTOcFEc5mmOhvPclfGq9kkGNuBQwtwGvfnbqTdO0ATRHJR4TIHCvmEjoKvH4H3HtCStlwEvaX-gXInAZAD7r0-qgkRqI4HX5kByA_rk2bXTX3XZt8hGqvsFRtb2EWyyptMIn7CNkqGGap2bBfvjlYDWlaX40D4IODH7xXHOV3pP4CsWBViWO5EepfHd_rdq3Mw7THvdzGdLECO56boTtkQFvk3313jX2G00wnyZnhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق این نقشه باز هم میشه نتیجه گرفت که سمنان چیزی جز یک تئوری توطئه که ساخته دست دولت ها برای کنترل انسان هاست، نیست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/79569" target="_blank">📅 13:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">امشب سیریکو میزنن
بماند به یادگار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/79568" target="_blank">📅 13:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qv_yaMIG3nHJpVorqMEuXH1JRqPM-7KlUO5r4k-a8CdeqLdDF5OyHk28nQseAtNQR801ToNSaQW0x0168-BUoGd5YU0CK8GZyw-rhlhBA49Qv-aGToqb2az8EvEjOUeWoEfRD5Yfbq8XPn-VRR9s3ow7Y0ui-c328VoFjOoPp7oP8qsRsWiGuzIUZHgYk582x2i2jJv6ee5gvQbLLGgebQ0e7lUpO9_00Xo3pKy_aHoM3wOKslyXU9LtY1OGmbPaHxsX-DQXQZRAz5jSqRDZRMH7t_pXP2xrR4Q-mKabmTjq1ZsNDZhNqjn-BkTQRiez3JDvrSXFyl9AAdsbFPMxOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که میدونم مارتینز مادرجنده از قصد باخت ولی نمیتونم ثابت کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/79567" target="_blank">📅 12:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">امروز تا اینجا اتفاقات زیاد هیجان‌انگیزی تو خاورمیانه نیفتاده متاسفانه.
فقط یه سری آدم ناشناس سعی کردن با ترکوندن چند تا ماشین روبه‌روی هتل محل اقامت مکرون تو سوریه، مکرون رو ترور کنن و سوریه رو به دوران اوجش برگردونن ولی ضریب هوشی‌شون اونقدرا زیاد نبوده که بفهمن برا ترور رئیس جمهور یه کشور دیگه، علاوه بر تروریست بازی به نقشه و برنامه‌ریزی و اینجور چیزا هم نیازه و متاسفانه موقع انفجار، مکرون اصلا تو هتل نبوده که بخواد آسیب ببینه.
فرمانده‌های سپاه هم دیدن حواس باقرشاه به مراسم تشییع پرته برا همین دستشون خورده دوتا کشتی رو تو تنگه‌ی هرمز فرستادن هوا که ضمن تبریک این پیروزی بزرگ، متاسفانه باید بگم که اونقدرا هیجان‌انگیز و خاص نیست.
به امید اتفاقات هیجان‌انگیزتر در ادامه‌ی روز.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/79566" target="_blank">📅 12:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnuglonPyEzZ4FmfTxVrLpb7swxYwGoCk47DEpkTtjWhdBbpbmUeXYixuq3JyRml4JxIq4gh437Y5opth2s2KsiCQZGSAS3kG2-UC65OxINTU7l3FedVzeS7KP2UmcObxP0EevP-fzy_VnVXqPiyBliV6UGcrPRSv_FM7Y7ZhbIjWzWniplNJzvV9yKAvtL0OXOkZd7ReFeyZhbB04y_TI-TEQoEEYFhH59yYefRW0jN0KGGBWIKsbHuOdKqeB8q9eN2RZjJfPWlLfwG6Rn2oh_FpX98-trse-nGNQczg5T0fES1xl-q7PBw5MC_XDVajlyO6ViKAhpAmNyrU3Vy0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79565" target="_blank">📅 12:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اینهمه به یامال فحش دادید گفتید بزرگتر کوچیکتر سرش نمیشه، تهشم همین یامال بیشتر از هم تیمیای رونالدو به فکرش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79564" target="_blank">📅 11:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ببین تلخون چه موجودیه که برا اولین بار حس کردم ادرویت کارش خوبه و بهتر از کسی بود که باهاش فیت داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79563" target="_blank">📅 10:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFWpv7ZUxS9SCXtBiowiymnH24X4GPQo9KogP4OnskzRMGJGea-PZtxp-_QMSU2yRhZt7eOMAzO0V4oOP0gSc8KphJ7Ga0cpTnKm0WhtzJXMu_aA4YHCetICOzAQaE6MqfY7V4rBI9Ql4j0R7ACZWpLghVaEShKMtq2BbJE1wiH-JI9suIHMm6IBNdyfdx0YppIqk9WPxCoZvnT6H7PzxWX1ByktQl9mztQfRcWjQ-fwa-mrKCRuI8muGRWEGMdB1A3XLhDKTcA7R5t8nKSVgELNH7x_d805cc8vSoStOSkYQF2msqGvgq2G7W27pkbzBfkDbMvUaGj6aWBUsCXQig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این رفتار لیدر طلبی برونو فرناندز که حتما باید خودش همکاره تیم باشه بعید میدونم منچستر هم گوهی بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79562" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⏩
دسترسی به اینترنت آزاد، با ربات تلگرام بت‌فوروارد
🟢
🔥
با ربات تلگرام بت‌فوروارد، هر روز جدیدترین کانفیگ‌های رایگان و پروکسی‌های به‌روز را دریافت کنید و در سریع‌ترین زمان ممکن به بت‌فوروارد متصل شوید. کافی است وارد ربات شوید و از بخش
«فیلترشکن رایگان»
، کانفیگ اختصاصی خود را دریافت کنید.
👍
همین حالا ربات تلگرام بت‌فوروارد را دنبال کنید و به جدیدترین کانفیگ‌ها و سرویس‌های فیلترشکن پرسرعت دسترسی داشته باشید.
👍
ورود به ربات تلگرام بت‌فوروارد
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
R16
🅰
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79561" target="_blank">📅 10:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">عجب یک چهارم جذابی شد ولی</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79560" target="_blank">📅 09:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بلژیک ورژن فوق تخمیشو برا قلعه نویی گذاشته بود
از بعد اون بازی همه رو درو کردن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79559" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سلام دوستان صبحتون بخیر
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79558" target="_blank">📅 09:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHExtvZ9Mt69LWPsMyEWHb3SGBNy_aZn1AsMDo0ZsE8eQyw9la7ebVJjpd1hPCZGFmBCwFWWyfWRyJ9RNCQH_woNjzAYjESKEFxKLva2tbWRyoaVUSud7ALO7s3LAVCm0tAvZz_k9fAGvHnOG7ArBB2a-sO_9xMXGCjMN-BITMz-r7-trYQLxgpfqXShtlR2I2YTMKbls7TXDq1J5MqTyc8ImcKEImp_TiKcSRBwWpeP15eOBMeuuHRzbot8qb2QLjGENs8TdWWo9oBKbk2Wmcud0o8nSZdiXZJhtbGGUlwKxdIqZ9sC-luPSnAY-aOyAFZB4txvG2FPcWKHE4aupQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه ذره حرفات به قدت میومد هم باحال بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79557" target="_blank">📅 02:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79555">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cYoGh7yKGkjIYeAo9bL6rQtirTHo6WaKQiy5pWyfc7jFErDnKa5PiNG-7KvgbUMBE1-5-rlZOcRfeoSRd1WRJBeFbthKhlA7tIPCZitwzaK7doX5fLGL6oJH60zyy9-YpLBpzNI9aFPvkweX1g6o2PMWbDKQXBz6LwqnuhCW44OqExPb6dnshcknjbtKbCX62keO0UrMlAvRUVDA65srjNN_DR5JB7suXgqqUM5KHrFfhQx1OPMn6MiSPUbs5CWF19BgfFCVx-0lAveuXS3umiqkLy2RE1LOX9wCnjfpk4uq79R6Isc5Q_OKxUZg1goN8KfsaAWoWnmGvGi6OzJgNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jfiv8rhi8IuAplyxVgIWZtxTKSTklIcg6ZuWWtlhWXEfLmHNDNhtI_fHMgwau-zpOmTM04POuCiWw--10wiRJj3Bi7QkFFY-Glj-I4-tdsV_UiP8wE94wl-pt_bWsPNtXHa7qylEEJG_wIRWPESjJ5DsEqMlFN51q7GTBovHnbMEIYCf7UX5JPVa8w_wEZ1KPOoNatrO-vbZXk-FqDaalSYZhMr15Pcn5u-mmVEhQz5lXOSBVvrV2gr29qwJAH3dteU49jyZiC4xg5qFdfOufR7WfN72QNMI5-JyVHG9n5i5icdBcFCTqduQWuT7w6uP8ZZzaN2qoD15Kd5V3rn7Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فک کنم دعای خیر زید یامال بود که بردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79555" target="_blank">📅 02:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79553">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن  https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79553" target="_blank">📅 02:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79552">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دخترا پاشید بیایید چنل دیلیم دلداریتون بدم، پسرا میتونن برن بمیرن
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79552" target="_blank">📅 02:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79550">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0585a7a92.mp4?token=ok95xaTKysb6vzOJwVD00G3Pj3AR228C81_6KlLBuWdxx3rU4OqxZKnMyuEhCv4nINDn6aiG89AfVEmOsBKCyqlO3Sp7ukYP6FNhP6ta5ofnIVCk3z0dAitNZ2IjOl58K3yBmZVW-5YLy5UcnhCX2s4D_LZPQrhFHtrFaQiC_-JgbX42OQteOXG89Gi8XxGnRG9t7ST0i9pzwqVLcs__2G1-CxmAaYDRmLkeu0DDW7tCwWz6u4DBhSQQf2J40AtvSz08oU-r47Q7YJsJLXwnDS7tf_5OQ0I3KPlXazViEGoSAORDov7uqsZfguwTELhFWy2XKGDbgBsfWobB1JQ6zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شب بخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79550" target="_blank">📅 02:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79549">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromEliAS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZVxq9SUGbxDWs5rKXXBSa68_F0juU1BN12grnHOWQiOVUmeurWr_5Nl826mM8wQ0iacmcyu1BYnCyEvgoZo6UHM1RXU4Ami3Y_hKGSO-zdt0FN-Mf2jb2iaSA9TSGlBeiM4SYKoNe6cUtbqLsvdOKMuydjrV0TI9tzUhjGla_W3OEpUf8j-3aJiHcSg9n2RdH9DYmU7yCfiPm3_AuiprQrMupRmtvdMY1StX96CU0DonZtuJTmsiMDxI3dS_ANqfA33GDnNNmlkpD0PqYBHcaoCeXyPtBVK1YYRubh0uIwgIC8-iZE5asKkhFa8t4FtZcA4M-VM01KOv1gQJpkgUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعصابم از تیم تخمی پرتغال کیریه پاشم برم فیلم ببینم:</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79549" target="_blank">📅 02:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79548">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دوستان رونالدو فن نظرتون با خواب چیه؟</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79548" target="_blank">📅 02:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79547">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79547" target="_blank">📅 02:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79545">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHadi(idk version)</strong></div>
<div class="tg-text">رونالدو باید بقیرو اروم کنه بلاخره سه تا جام جهانی بیشتر حذف شده تجربه داره</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79545" target="_blank">📅 01:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79544">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaueZdQax4uzvG-g1Lqx384cOjXMWr4KqNUNH8xBJbFM1I3CHvF0dyO1ShRy-63XxIXSL3XuzRq07ie02rD4pXKNEtPXz1hCy8Y-IZIz5X5GOmbEkX70z3RKMHcXzAZUTVaDZR5AfazHoO9JmnV8hv9P-o7RO9iLjMa5bpHzzcjPvxwxTAigJkj-adAGt9J7zedcr_S_vhDt2rqq3OkkZm-MNLSHeVpHLOcYJwZ1obuzGOU85iuPC0qKL_tIbPxzoevfLjiorwxDw6pwElyzh4x2cw0fs_5f1n3ReEpKG9wwugVl0lBqOYgOvvvamNh2Wensrz_tCSk-v6jdeK_rFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79544" target="_blank">📅 01:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79543">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">یجوری به بازیکنا پرتغال فحش میدید انگار آلوارز و مارتینز نفری ۱۰ تا گل زدن و مسی بدون گل و پاس گل قهرمان شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79543" target="_blank">📅 01:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79541">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aylktyUTVtbRwmrugHu0sCZ4_SXeLG0YFRwfBSmU0Kvfefege5g76vMD_USrdtnOMjzRx0-1br3TTVqVVuDANeGj-DxIZyhDl0rexxgMw6DCnlibwBuPtupL8TtfbufQWWw-kBw0aq_zT_Kknmveb6kb4pucCYTlnH7YtgEhU03-W7bJWY-b9mLGge3alfwqwmFcE_SqqldnmGdPbcBzTWA8IAiS2LlDDGguZEJu5DLSivNHEFi_L57qps2vEIU1t46s2pEHy07ylD2K0lk5seFxUlLy1Noze5A8D-YXfV8hDXTOwAAdLuRRV2QO7RDSuTUisGDg_MmbqVqorqpY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیاد گرونم نیستا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79541" target="_blank">📅 01:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79539">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شما یادتون نیست(منم یادم نیست) ولی اسپانیا ۲۰۱۰ هم همینطوری بود، خوب دفاع می‌کرد تهش یه گل میزد صعود میکرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79539" target="_blank">📅 01:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79537">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کاربر Mmd به ائتلاف تحریم پرتقال پیوست
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79537" target="_blank">📅 01:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79536">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsD38v3lIOi2eb5EL1Fi3hQLtZAo-5FPvA2diOCtaoWOihrI6K3KrOgyVxgE1IJRyZP2tz9buEq0C-jVF_GzXWFPaqYBalAx548ogGEqsbBzY3hdzCtSFRTkoa9hexatyxpHAUJZ11JR_GNrYvAhpRHnLQXI7ucli1sh3sP2L0U3TV3yJruyeLm8WUS434SfVjojesH7DGzvQXqd9BYPndREemPIJmSDX_tqRS1KGnKGjQa50rGK1_pcV-k0aQagGAcCpSk5MON5-dprEsf2WsYjY1BKJcfQbDTZGt7bWukXHe4z3oSkpXzZAcvFcMRvYS6AcDYZrgWcyG5okpciCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا داره مارو میکنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/79536" target="_blank">📅 01:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79535">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رونالدو بعنوان سرمربی جام جهانی میگیره
بماند به یادگار 405/4/16
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79535" target="_blank">📅 00:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79534">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPmxyNHnMwtNrV4fNNcgJPnGKAwk7JLCOK-ngrQVWsYUFzch0VXtzaWoC2Uo50_o4vVnDkf-e4yK_YeZkkSqPNM_rfN5CtuGS3OXz7NEYvhvnrhfc0pK1BHG7eGVX-P6qgLcrba5OPk0DV1R7njao-KKCMksy8hwXO3D_oWEXHKPUXHhQKyyWDw4cJ5upNZsbqZWO6KzEqO-BHGIQiu2ACune2dsZuW3UP8QCsWz3ITrKz09zENAGpCrFPCCYSXVXZSc5xVqEn2zL142xO2v5ghR50KVwbNgP24ahULT1WYSBzsrw9sexL9hgSoOeHquAsDd6Kf9gv2xwxp9j8vZ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا ۵ تا بازی تو جام جهانی انجام داده یدونه گلم نخورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79534" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79533">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دوستان بالا برید پایین بیایید مسی و رونالدو ۲۰ سال تو یه سطح باهم رقابت کردن و الان دیگه داره تموم میشه، با کوبیدن طرف مقابل شخصی که فنشید نمیتونید کارایی که اون یارو برا فوتبال کرده رو نابود کنید، پس شل کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79533" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79532">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">عزرائیل فوتبالیستا داره در خونه تک تک اسطوره های کودکیمون رو میزنه، نیمار، رونالدو و به احتمال زیاد مسی هم بعدیش(
فقط رامین رضاییان مونده
)
جدی جدی دوران طلایی فوتبال تموم شد</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79532" target="_blank">📅 00:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79531">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YU9d1psTVD7sYZkymW74IVsJtciofe5q04GcWeJdewq_wQw3Naaksc_C-qI084ZKs4yX0mvcV8OiGOLvxQ-kFv0b0Bl2ONr1gEPGRJ5By-n2x_HuWH-ygqnc9DrmcD2OrPVZK5gGrTJWUKNcq1lX3puVLONQ4l5daeXvyQyWMirPvuosIfvmYhPp4mCxLYvu4nXVFaqZRlgwB2GmOq3akRiYnjOCH4APbeyf3MR7IEU12HWac1WVFnt9RZtG63ecCTfi2gSG2sYZobiw51VuHoK4vKdopmzFMJpQVvuGyvNEqG4-lus48wvWXYuopiMweQb9gGUDny6oAvRDo-8Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79531" target="_blank">📅 00:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79530">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvHXEgVK20kUaK5aQMeuLa7Jn81Mu-nCtkEit9x6BGVyoJQ1RBlqqdc1j7p9vcchfTIE8pLp2br0mgG2pRnKmi7SAXeav3eY4E15C8KYL6LvC4YPtV5Bf29r4-4CDAJMAuqnzQE0hk4YKZA9LAtPJAzZm4GpvgwkeqpETQn2nbhQF9UccXmjzac91qczQrPyjAxsuZaJSquLDlaavN_8m61ImfQPumULujOerFKEeNlaKxYxbNxdg9299Wm9RqIy3ghwwRgOotmrTGqQi1dqSUS11WU6QZTdA6jZcgzB-6IYHx-7YUryHR0YY8TB89RAqtmd0kbcQ3KH0VkqbHuWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدای تمام شوخی ها و کری ها، پایان ۲۰ سال سلطنت، ممنون برای همچیز و خداحافظ برای همیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79530" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79522">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=aqLPk-VUOzpXYKKST30A837ioJaLmz3mB40OdIMYOCduF9tyOuRXyxoiZ3UW5tnWZH5c5VWbizvUp-05BISuCz5WiSv0Yf_mhhaH1FTP_YU3p4IL8EFZvMUDHeEBI36hHe_RSLoZTQHQOjOZH6uY4MpOmLFNYQuxmdGzGNOqPRbBpB5Zlx-jiwDK2HzzuGspdc0TNSl58WSfXQo42AxrRoLCKmBFGxIIWuZ8rmk98PqH_WA0vINyosvKpZhIyCFbEg4YmS2VrJS0Pwzjre2SJshcAX0xCeeTi1jBYi9h6m0rs9_WfrAg-UOOwcZGbEkoxZPro4rOg4JLfymdzkENoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beeb485ed8.mp4?token=aqLPk-VUOzpXYKKST30A837ioJaLmz3mB40OdIMYOCduF9tyOuRXyxoiZ3UW5tnWZH5c5VWbizvUp-05BISuCz5WiSv0Yf_mhhaH1FTP_YU3p4IL8EFZvMUDHeEBI36hHe_RSLoZTQHQOjOZH6uY4MpOmLFNYQuxmdGzGNOqPRbBpB5Zlx-jiwDK2HzzuGspdc0TNSl58WSfXQo42AxrRoLCKmBFGxIIWuZ8rmk98PqH_WA0vINyosvKpZhIyCFbEg4YmS2VrJS0Pwzjre2SJshcAX0xCeeTi1jBYi9h6m0rs9_WfrAg-UOOwcZGbEkoxZPro4rOg4JLfymdzkENoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79522" target="_blank">📅 00:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79520">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79520" target="_blank">📅 00:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79518">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGRyKVFlfY4BlzYQskpwaTEEyBPoBWGESwZjLzC2Pwgs3Acvz__Ak-0G0XeM5kbZooQ1tMb0qPHoyFKBROGwgFKff90prwQoBDFgdxMxK9KPaBwQB3R0gES-Kk6h_w_5LhAaAPiY1raOYS_keeSgwUtO3xn3K9-sDA4Hxp6utVyrq-ZUdBIIhEuITtRgkKX0YmJo05jSWaaiR-2_TqSEPh2MaV9jcYd5EkOojq4u68FcK3xSG9iMFs1V6m_HFjogfzQHYra04ohC8a2HBNI1IWcZsPgw2IPCnLTRMsFaQQlkzwDT-uhG_2E4ey7a6qNXj1kwd1I6drTmfi2ZAo-I3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرهنگ صفدر سلطانی جانشین سپاه پاوه در مسیر بازگشت از مراسم تشییع علی خامنه‌ای توسط یک خودروی ناشناس منحرف و دچار سانحه تصادف گردید و کشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79518" target="_blank">📅 00:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79516">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یامال داره گرم میکنه بیاد تو زمین</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79516" target="_blank">📅 23:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79515">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بابای یامال مصدوم شد</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79515" target="_blank">📅 23:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79509">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cr1jW9HFCzXFgAg1e0v-TIyQEREpvgprzK4vA31QFeJe-lFsuDaGTPgaDlH4mQu65zrUrZLJI-MAb2MScxWAW37uM5c6S7WYffL-5NFj-PIO4TbN9q3jJPOPh5d7TfQ-3ddgJaU0CCK-5rLKp5-55RjfL7Tpi6g9nsm5FaW0ZE1jdB5RY3wdDyJ0MIC1Xs6oJrt9gwyCesnHFCHMBa1mCyxK2Ov6qeBy6asqRYl5LWSMA-0uEUs_uM8bFPlegGikF_Gi6tPlMnhuQbiUfE_M311_m-zF7ZbPrJmSNmAUCyHeFwjqeFboSSXLx_8-IFKi4DFz_gWgHVrqfM7ghDMV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4VPUfxcO8VoDTd5P-OFxapO7OQq0SRqHblMcB1AYUNUglv0t0W2JSr66u-w7EQZLyYZRL5VrRe9c9mv9i36VzRjNaTz3RsYnCxYFIEjCh-BaUho323TlrpTJ5et8J0WwZW3Wq14u9QdUl3ztc6uj2XcdurGQMws2fbuETGqExP3udwiJpf3R15MkZGEfNrkcHOh811hXPCp835EdPa1hffc9ERIs881O0lRiwu-Xri4HoBKprgD-Ajm7mGeIdN0KiU8EQdAx57x9JtbA1KNoJB3h7kmtgHEX4QVMabHM_7t1qqCBsbeQm1v45e4yc76rimtMpP66ZNejm8TjCIfTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خلیفه سوم سلسله عباسیان هم امشب داره بازی رو تماشا میکنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79509" target="_blank">📅 23:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79496">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">امشب حتما ی تیم صعود میکنه و بازی صد در صد ی برنده داره و ی بازنده و احتمال خیلی زیاد هم بازی گل داره.
بماند به یادگار
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79496" target="_blank">📅 22:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79495">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FbUXVc0m7Cl4wmdgBuzB8LNo89vqrfdYQ-wx3OTPALuSFHeaTF2LKM2Q0LpBYmIRu7rjVN2wX5qUq5Z1pnp_JL69SSDDA3Pr25-XBRIygJGOvN_jnyuInVenIc1PgzuVVTN5DK578Hqe9-oeaHdseEfLJFKFejqBVY63aPdv7bQaEGdLYwGwOtcHhhiz1GTbt8Lv4e0wetaqFpAyzxB8OQoavz3VMgJQ7EVQciYd8OasR6lnqgT_nsnG5MBoX94vCgzh1c4jsTgqq7Ff5CSMiLHawaXgWVosZxE8j2nKeQrXyZYF0eIzZx6fmZ4bc-upPjOeRHdhtoI5a4kaDe0AAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودکشی نکنی کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/79495" target="_blank">📅 22:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79494">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTlXAbWsCExarjcI2eqpIGVGzyesNoI8vcv8Y8ZDwaFYRUaqYd7gZFg_tTHhllWXzGFOWjuEF5OdoOt_VhjZ6pDr5xpVj202uoEZtuT7hxodgkwTUpLP9V7XMPCKNespkr9220Zuuk4IO_Y-EZNBeLlqpMPWff0qFbVyz-SmW9ThWPHzeHNdz-OOHGRGVlG3iWOVlj9cMME_zA14Fl6ksOqB5C9eShwaAacRIDhbQ1TYlXJl-IzysfPS2WDIyGmRG3OeIor2Fd2rtlWNw9yw7jCzhbvPtQ8AtBQwAzzXqDxb58RC62cexsyILYStd6BssoTa5PrRcNlZWbN4JvcAbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79494" target="_blank">📅 22:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79493">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVwFOu5805oGYP_WpILrz62VWy5x1QB4-UsQ3PqMU6q7Phw6J5h4wI8Lvyr_qIRZKWXJZXwniSFY6qFfNQJLb9qQEuH51Mhxb7DzrFik_PJVFic712Au3CdsWR9FTDfAS2EUQeg0-dAfMeDnhLCQKa44tzb2n4ZKq3MvuXYaPQiDhAxcuDaiK9hSJsIcL_uT3yloU6kmDfhs_vIXL4-DG2Q87_-oRS4LuwARiKqJ2GsvlttBFAF-DwHzjwa9ez1trnCUnXJEt1Cu_Kg6ILo6gYBBZTJoCWgZ28vDAtoeOT40xL5fesHOIC9n1jMV6-bX6id5IGG0cpUl9KKog5GgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند کصکش
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79493" target="_blank">📅 22:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79492">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط 40 تومن
🚀
20 گیگ --->
❗
فقط 79 تومن
🚀
30 گیگ --->
❗
فقط 118…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79492" target="_blank">📅 22:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79491">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
HappySmile VPN
🚀
🔺
فوق سریع
🔹
فوق پایدار
🔻
بدون لحظه ای قطعی
✅
متصل با تمامی اپراتورها و نت‌های خانگی
🔺
تمامی سرویس‌ها آیپی ثابت هستند.
🐱
مولتی لوکیشن واقعی در 7 کشور
🇩🇪
🇳🇱
🇦🇹
🇫🇷
🇸🇪
🇬🇧
🇺🇸
🚀
10 گیگ --->
❗
فقط
40 تومن
🚀
20 گیگ --->
❗
فقط
79 تومن
🚀
30 گیگ --->
❗
فقط
118 تومن
🚀
50 گیگ --->
❗
فقط
198 تومن
🚀
100 گیگ --->
❗
فقط
388 تومن
🚀
150 گیگ --->
❗
فقط
578 تومن
🚀
200 گیگ  --->
❗
فقط
768 تومن
🟩
تست رایگان
♻️
ضمانت بازگشت وجه
✅
خرید فوری از طریق بات
👇🏻
✅
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79491" target="_blank">📅 21:59 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79490">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ژائو نوس امشب برای رونالدو بازی نکنی مادرتو میگام.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/79490" target="_blank">📅 21:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79489">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzStht9ffiUgVZIldVwgvwFrLjBt3LtkdjXTAutYV402Zk5nwdndBcauwzXWj8bWeGxa80dOHgL40AMDSZhP4Nj91wMRUWnhvBwoaeBPFzGf-yux5EaJjlov3FTXNuHDoDZVJlQolpzrh1MZdOIWexJi3BBmljoN7ywl0_ZznunRv1Bj3QOcCOCpwBR_P9lx8QsDulqIyBrwDdzZjLkxfT34dgAZjUAqerbXuW9I6Le3yJshSqzSK7vMngH97Xjstf-R37lVuIANojIiP3iV1nlYu1QZRmYwzBy9F3IeEWloLDtfdKs_dwBSmbSD77ZbVj2Y5xd_atXUbt4TuX_QiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دماغ بیرانوند تو گلوی کینگ گیر کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79489" target="_blank">📅 21:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79488">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gunTaEJMFzP_eZe_i8iY-qt-BaSREdspfG45oM5LrJ8b_YTa5JEDwEu5zY6M8A3puEA36qjICaiAMOqL7ZyHvFdblsCkLqrkQP3VnToVcpqPJnclxDUbacawf2c_gnEV2A41eDbGey85-qBlQwXt-riHcdd0wIGyevmUSHPJSMDH_wO2cCmckL2rdq0CkXQtFrmC7mX3gT1LAZHtQ4BjLMgS9r3B6j5CeHrUcWvy1LizBeNTY2HmawDOylTPjQB7u8BD_BCDo5x9XnHwGkcJx4BwC3f7IMzFJh2XS0pT3iyTSBD0iVvu6GZoDP85tZEotHYFCMYVjrv8JJ6TXAOFEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب اصلی پرتغال
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79488" target="_blank">📅 21:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79486">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">انگار این ترکیبه فیکه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79486" target="_blank">📅 21:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79484">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D_rYtCouKQWZSNfsQ4KWiiOMmJosQNOOurjYfHSUHufhZW5KzTTWvJvyRcrSoQKQMUKTXz3Nti6P2KiTwCuFh5HInnZrIbqkkYVs3DwQGY0XzD3cwPX5j1PIRuvANHDyti_3iKHsk7I2LxEvCeyNJTYpqwRcnjYdU6CZkJpbm_ak_SJlbVt4b0R5pz_MOcwTupC6efoEXHDJN0pc8A3wlV3N2PwO2KcEz-Epr1VoS_XA8o-JstG1bumqT1KZUvlzh75qogdQ5-BNA3yfa2Zt41fjq8PTSu9joAqzFREQ4JjhD691ZMAGvgnhkq8Py7XJlvtoPp8o0w-OHtc7yZXF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KEwrq5HJb0TRp0m504GG_NP4Nm2FD9JgFbjJXQnf-4pMGtHUe7Sj6mKhWE572Lr2saxfVHGMQmXvQlMM7V3m152Ugq_wIV51xpC6en3XWJRIqPZgt9w2PDMLBnP3j0vSl5pPMhtmAepRGx5dfLw8D9nfuKeYGrMDQTkpKiuyUbDiXVw9kNdEkChX6WbZ7U9asMSRVxMVqs8ogTzk55CgtzYey8tra3amg-ww43iyBuoygRBi-QYuP-cd0gTbnS5sUsmH4vCR-nDSvelSt5tXotilCmAU-aCnsPsvylS0R6eSv5yucmlT-V0TnqkHoJR56Rg0LMn8UgBjRLi6XggHnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ژائو نوس بدبخت چرا نیمکت نشین شده جاش روبن نوس پیر سگو گذاشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79484" target="_blank">📅 20:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79483">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">مبارک رونالدو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79483" target="_blank">📅 19:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79482">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E4uCb2yS9FhyEQP7nKN07YQ_LQ_nr9oVrvUEzW7cdMaVzTucTRgU1QNiKPo2mfu_zHE6b4FupTfkBnaTZ_D_2bAhIEGVPZBrFnJ-a-9f7TVOOasB-_wKE7w7LxAudaCfY6-MIbKzWTZkiIv5ntMjdhmdzE1HIumSkGbeLZEuNzNSjA2pHmAXBurREpkXohwkdcXTZnZoIFI9AOIMzuCgpl_pWENsIhscgZxFpAZKu1UnA46AlxnzEXnURwfMCK0kBFiAt4tEM7v4hCGX0LPu-ha-7XrH_qcPmgPYuRON9tRES7IZgxMPux58ahZReLg2Jgk8JQOHNnythaZ2HbIWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مبارک رونالدو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79482" target="_blank">📅 19:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79481">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTMTP0IYqWWnRU2cbCbVmbrEkRBjSHOansNV2oboooary9_ReVDkgAyqR_DyiunrJ06tkwFYNY_k4ln0EVw3L3oP_H2pukhhOVImw-OAw1jQ4XRh5fjPLG3G-qHSqIvPwCVz3q1jYOnWjTzQDltg-qYFhuwnWKzR0NM_Tq7Q3JOERtRc_l3uEBwQrqQRoO2En07WRcJSMI-Y0xQsZjOkZqV6TB14AbRykuELT7Pws20kko25xWZOES-nSSxTaKC4em1bUQZ_Wm9wOVaz5ueZ9kmz7jTZEYlPX_7Bv8SI2Du9WmM2Nv6KT_4iJaoHrcGBaGdoh01mWHYwTq-aNbP73Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79481" target="_blank">📅 19:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79480">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osGwRmaIblYvmlYIaubyf2_HNWlobEl_fyg8sNwe4Fhtq0XqNxVEpXLIL8WqZ2Hfzx37PRwCb4P71EqSgY4VfyaktzMXtSFS4R9h7WXF6-isQuVPTvDyD55p6SnpiJGfi65447EJsyANLor0uUl3ocGDTsfJ_DNmEipjXarSw90tAtOYUzs_dwpw-Ej5n5R8DAqgOFq5bmM5VnsJ0gxCQciGhqhdbH7p0tmfchra0x_QAr6Zn4DmfXkBHc-EMap4uIS3E2DJtVKxpHZq3Bj8SF3bEFeLjMd3w4RHj6jY8FkAfkZbAdIMu52d4DJa12-7qjFRbvv5p7_BfEBrKMu4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79480" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79479">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcyV0OYyvOGYiPzVCfafY4Q7vDcMG4CDym6h86bAFsGWRU3KfuCa7nt9Moe7klm9pBl4BpLihDvHF8HaJhdKluFQzVWOInucX_C6bFW2qiwa-7UXJEF_JBDgiYnHMNrI208VuMRCPFzAlYjRP90sQfn12_nWEXUitSTdBq8PXcY6lcPCtmFNBRmUSOG0CnNuTgN4mG4A5g-KL2aDB_gnB7qnfBrjsSvhXQNNcKYuJj1kp65jntV4tP6pFpVtSsGWB5askS0B6ebd1MXpLVgQiurXVGwbNARtHb1Ubog5AYs66d734RMFiUnZCvS0WDaIzgGzNimGHMEzi2aOH4hFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79479" target="_blank">📅 18:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79478">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79478" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79477">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حماس قراره منحل بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/79477" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79476">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KakObLir1IaNduTj6DfH5lWYgGu3NReZfj_Lwl0aWkFFc0dxlT3A07lWOMSwEptXsfx4ZYS0i7Rr-Whshu1NP-11BYSTMgcKG2wMrIyhJy5OdICLK45d0RrheTwSgQGnJZwURyJpJSn7DqYhHF1E87_z17aSm4bVIdivLmlIwNdaW4bOO4I4OaQYA9i52AWeaq47RcrgjsoWTfhq3SE_J2ukCjV8SqdFXMhuEb3ECyrpzvnYmqHZKryuj17FR4QlhYEn9wiV89rCu3zFWrVYgR3H38xDVcdzYR-GOCSuT86r1AtswPCiK0Hy2jzp42_v1N5A4xtNbRn_8PLilJF7Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت هر تیمی پوشیده اون تیم حذف شده
امشب هم که با کیت پرتغال میاد تو استادیوم
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79476" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79475">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC6FEoGjzn5A039RYHiL_qI1qpYYnDi54ABddjgbyDQKI2WIoYJW-dLzj-bQm3bpc548jriWPPAgZJCDz2m9UxlbifjdLbrifaXXhjzAplmIKfrjnHuAbe_9UQ02dfBUwx_9Fnl5jV4T0RRZrVfZEO2v-4dDFdRlnP_C4MqUqbWadIRCJMWkdaHuQN38a-pnd-r6EZ739yrTVJHSUw3Piwy8jNp9Smo6I_yxp6iS9lMjbT95bhZVyFGveXm6TrteOA0K3IKoj8nZaY_GzxArYLJvtVmfShJanwf-Xj91ZkhILhKUtGpIHSQZscJ1QT1GnKlzccnIVuKk6q76RShdMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79475" target="_blank">📅 17:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79474">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دیس جدید دکی به زنش  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79474" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79473">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bddb338012.mp4?token=p5wE9HZu801L35syxHk4fSzmy7vLSQLnWL4OWQPC1TdA9iC2l1lMK9C8I8GQWq9rYEwCyYQmmZPYseTXX4rShRy9_XTpbXVU9hEGUv0HbSCsaQL9JtJD9MnhC6quPNwORP9SPQlHKaIVwjJSaiB3Bog_4d9GyD3Nr5KzqmhlQfWlhu2_juunFFnt7aZVCibFoQ4C37lekU3txGf2usxCu7O5u7M7-hZBBzL3ZlRT-QhiCJjih0MWI0CG9_vb84g0VCpae1PZ3bs7zBBN2Y4x5zyqgptFkLZ50aLqSlBAECwoy5jEf51UTpqNtI9yHz-Aze9CH0WbopNAyrYl0ZS9nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bddb338012.mp4?token=p5wE9HZu801L35syxHk4fSzmy7vLSQLnWL4OWQPC1TdA9iC2l1lMK9C8I8GQWq9rYEwCyYQmmZPYseTXX4rShRy9_XTpbXVU9hEGUv0HbSCsaQL9JtJD9MnhC6quPNwORP9SPQlHKaIVwjJSaiB3Bog_4d9GyD3Nr5KzqmhlQfWlhu2_juunFFnt7aZVCibFoQ4C37lekU3txGf2usxCu7O5u7M7-hZBBzL3ZlRT-QhiCJjih0MWI0CG9_vb84g0VCpae1PZ3bs7zBBN2Y4x5zyqgptFkLZ50aLqSlBAECwoy5jEf51UTpqNtI9yHz-Aze9CH0WbopNAyrYl0ZS9nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیس جدید دکی به زنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79473" target="_blank">📅 17:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79472">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=dRIVDQ7911rIpuIrThVgPfZM76hyVCTHal19xH9EB-w9CEhuoL13ZYA86cTSVFXIZBTt8Hc5ITCsPy2zlK8yuQemJOA3hGOS0APnQOrGn_edyUqsFHJWPBB2NXF1V_0KHTxIdogojdENvv81yXaQkFNppGwXTCQxUgGolgLJ0ya4UVp24mn38KHTHnwjfq-3tSLxzKm2oiIcStX5hpGbAeQt0E8u4GYFVYeHnbZE76HL4DJniUtSHy8jzilVW6bCVy0mFg7YW1eXNqmwhtO9EcLsMo8H14wBQblfdj_k2fHN1V_-u4bAMfWS3MTtesM8nAw-cnP6XjIQKyL0sAIIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbb8eb97fb.mp4?token=dRIVDQ7911rIpuIrThVgPfZM76hyVCTHal19xH9EB-w9CEhuoL13ZYA86cTSVFXIZBTt8Hc5ITCsPy2zlK8yuQemJOA3hGOS0APnQOrGn_edyUqsFHJWPBB2NXF1V_0KHTxIdogojdENvv81yXaQkFNppGwXTCQxUgGolgLJ0ya4UVp24mn38KHTHnwjfq-3tSLxzKm2oiIcStX5hpGbAeQt0E8u4GYFVYeHnbZE76HL4DJniUtSHy8jzilVW6bCVy0mFg7YW1eXNqmwhtO9EcLsMo8H14wBQblfdj_k2fHN1V_-u4bAMfWS3MTtesM8nAw-cnP6XjIQKyL0sAIIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیر دیگه حرومزاده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79472" target="_blank">📅 16:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79471">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">امروز روز جهانی بوسه نمیدونم چیچی آمیزه، به همین مناسبت روز دختر مبارک.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79471" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79470">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مندز و یامال کدوم سگین، امشب رقابت پدری با ویتینیا و نوسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79470" target="_blank">📅 16:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79469">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6d2CvNNCRAccmgaPUN8XS8sgKbQUmbxw29k28eY0q0NvmCaCwd6hMGlAn-LzuBxMac-Xlyo5eNs9DtNdqks2OTbcF8I8xMdpjgMqFh18OKCqZoUeM94tHf3Yd76fulBzlY5PrOFTwLu5R2tx0GQDJXRh_mTZpbXlUrZ83bOB1f7hHMHncVRTepKxDOX2bh3lIQ9ZbUmiLK-peC0jQ-NVLTlyGcah_YtnN9zvxlKuQ21EzYsYWFC8luN4URam31Iq1au3tJsNzk8iIacLwMNRaxceMTTzGqofta9RJL9m5mxRzrkBuiBMLdsSSACIFfHbcBm9yXrDgguViXKpOpZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به همین مناسبت ۲۰ تومن بکش رو بدهی دکی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79469" target="_blank">📅 15:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lMauONsb45GNX76hMB1JMjF9sHMZzoTW9yVU-J5seidclkWn7f2kK1byv4H8hgYm4xMg6hmYZ-m48E2h1cB0FhEXH-OwHhM2TjjMVDY7JmjW4HYJGbbibj0U6-okV-gM1g4TfUOWcy1_DtI1VkJ1n9Zm7D0cNhP5S6TAWa_siq1OTiQSSG42ik9JHkBFUVN46ZEVobMua5fhBAbQho4tV9NuCeuOtSBzhI56U_qx9vEbVEkshDPMC0SWtVnFhKbIYbL6X-e4VATz2klJxe0JA1CdmuwDcvBkuB2zIrFEEvIu2E2sXprx1HRHw0pqhLRlvYRor2YGGI-nzueNc-XiNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگ گنگ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79468" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiGIAg7YMcnrNK_nJbsR0bWx-UxYevC-ziQmjDcirrVnZUANjn27hmXNMznPO0ovEDF-P_YwQDjd0Gz7et3NXu7gzfDDTJwdtp52gHC37W2ee_zzEgQQon-fST31t2SpHyh7SUERHaYlDlvIuirD6rDKl-9dNF1IjI4pYfQgpQEVScRJ_XI9UPhI2eisuQO2l2ATCLPyUvZiCP5qfamUjSrMTskVMfh6PRfHffsPqZnHIfG4VPLFJKJADw_a1AuP7lIeb6f0IpO42-t5AMEyBuO9TLFiHduWh3FsZeLQCp-70nu_VRHj2g9DK5lv3OJboqtEktZHzzuydoL4wsmJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام مجتبی بالاخره رویت شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/79467" target="_blank">📅 13:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79465" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">صبح امروز اسرائیل در طی یک بازی تدارکاتی دوستانه با دولت لبنان، حملاتی به مواضع حزب الله در جنوب لبنان انجام داد، این بازی با نتیجه یک بر صفر به نفع اسرائیل به پایان رسید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/79464" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لاپورتا کصخل کینو بیار برا دو سه سال پولدار که شدی برو سراغ هالند</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79463" target="_blank">📅 13:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop | Farid</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/79462" target="_blank">📅 12:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1706GC7l92cM7GPXgYAQg8iZJT82ot1Tunp8MLYdknOrY9QnUW3H8asTPAeA2cLQoq2drfF-xOjuYSihgQXV3XmfHFkDqBDMugx3hkCgmsH5ZJe8rx1PCwwuzyAi8TWm-TnVPjWnncHcKrWNrlrOMbuXykxH5N9Iiknii7hgqykU_MXtuhtG1G1CC9krHOqz1mAxGSxhugv3k8Jmf8nNtC5SEB6T8l53QwGqhFf8C7a7NZ41mQBzRiKc2YPX2iXdm-CDIjyU4nr9MTg8OwKfPW_YjS2d1lJ-Kz2viQYlFoQozQ--vkKDyRodQeNH01ifu3diX6Fm_DjiVzILrc-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79461" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">میدونستید وایکینگا تورک بودن</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79460" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">حس میکنم نروژ انگلیس هم میبره</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79459" target="_blank">📅 12:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h_dHyZ2o6b36RFp6fu6XRfbYkbQagQMK5dxT7B-KCQ0UYgxg4sByg6b5Tm4HglynwK8hX8FQU3Wlcv9CvhYZ_SSv5yO9KS-EEY7dBSAWPSqk4BcNmUvgvn_vSSbEB3RlwyEMlaNQBpzZwzEA1Py189bt3Sw2strNEXzZ_dZw7mIJHPGRgv-lnFZXeFkEdTLMmUBr1tEare5aGm8yoBzJPjIjddwmFq1rl6-8ZikPfUd_5uwhC0NZqhSNccCW7keFhaOgQAiPNdXRAu65Oks5oKmCGgc4KkBZ5gLofJmQ9ItkCfXHbaVbT7HOksP6oZf-_2lpxGSP_zHmAL1eejjYyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDf5CHhH9MNeKv75jATge1JS_NCqlJGhH9gRAd-ltn0vo7wR8yvXIeLzG0MId5xwsLRHbitG45__lBFZUmWRIGjOfHbXbAph1f9-wUaMuridGad3vjgMDvCFf2mlG53hL929mT12HH7IBsUFOthm8IHWRQ06OEeQ-Hbskg0DY6SRBalUaPvVvOYtV_RHOT5ql75XHV4iGtu4MsMT3UYjjxgxnybW6gjBACA3fTLbVgHpYzY8-SB4yCwxPNTQTnklKRZlN6tLl4sBpkQFsymaGFECRNDKr5eYjaHJ60waIvhKs98kHC1CVTbZWsk8thpAETA79BdQyE0amd670Ymulw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا این حساب نیست نروژ دیشب 12 نفره بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79457" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXd77xlP_qyhjRqm7vb3-9b6CJmOVx-hzAl3g73brP1Awm28_-FUi5AFODkR5XPYFFZq6-Tt-1LHLkxs_hTl5P31CAQsCgKTtPMySKOWDny4yiimIWm9b1riHRGFkDcfxHiRlcNcMSpmOu4gJ25gY8HwG4T9m51VCw2X8aKgHilhu0N52YvSF752BaFTf1P1cOvhW9pfy00vr9KpPV7JaEN0PpkgHR8R2h3obWgQS72RmciFPHXJvMp_8sioOsXX7sb_Gk3L8MOh66obHh0Dq1lRvRY3jzZ5iVDpy0Ey59piLQxikwf0BszRdbgVZThUUgCl2eaIGMJcrxdLU3W-lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ ورد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WR1DdRM1gLyQi_0IEsbBVfgut6ywFIC7sFZDwPqhFGiOurtrQz8FUAFyj68xjc7ngZ4izJr6DD2Lhw3AAGvRFbGpcLoz5msGy57oVorFtDgO_EESO76GrU5n4GXIQrvgURJCXY3-RsyScCYEoMRlP4Q1P5tNDSrftkq1ZaCHOOUna6cHTVlXW1MwpxHfSxt0ofJqyS7SdmjXzaKfsF3IYo-ZmBjqFpHo9HIhHePdVgAT_mszhbmRzdvkGTwDnNZC198Ql792pRqOAUEGnevfPtMiB9D6Zv1QV2ljZL46JjnZCyDEmYFc_h59sOSWoWN8166tHiWa6roobTUsd44umw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79455" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">چه بازی بشه بازی رده‌بندی فرانسه نروژ</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عجب بازی شده انگلیس و مکزیک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79453" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQgSwnH2cuHn4vRH0p9b1LEBUUWyl6ZOOTarT63GjMml9qKtq8yEtHrbyfsm1bbGc2206sMTEtYFqGWzZEKFk3JAKhoT625z48oBYLWHnl-JzcPO0aVxz-1wYvCzs9z_c95Atvl5X2U9PsaR22m4As7VJtgPwAkSHkypgiJ5FStsvSnGiUzKUzwI8obsApqdv-cs3gQiTPWxqTe1Boj1c_Wy070QVQ9G0ajtRQkNxrnIqK41s55JbrFC0fI3TErensph8WO62T11e0YUmgxUTVPnMZYqmNuVVjXTnK2vSkpT13KWOM5W7gNdrNW0f329ouzqcyvOeCiy2MBqGJLpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا تو امشب نباختی، ۸ سال پیش باختی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/79451" target="_blank">📅 03:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">استوری جدید علی آقا دایی خطاب به کارلتو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/79450" target="_blank">📅 03:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDaOgpaoWxqQuMway_e07Rp4_vq0LmOapJ-CROW_LKPkxKO1wtX-T-koz1Gsknj9bPqbc7mEGVrBd9xcczO_PC337mOecESLXC6OlMpO6v1IPZXbQaM8ZNvUKGgAaKgCJrSSq7TN31fF3dR_R2FH0qXy6sOnzLV515NGCyPNsM-1M3rMsuKnYGx7MW92igcUIR_I_vTuIIwC5Bi-8fy5STGy8fGvL-xoU4VCMcvHvS7lW6A90sZ3qX5r6EDNtXgQNMCwvMtfsx0BC0tvtS0q7YsRbanxaa4KgiQrHZiMW5Nl8Iy_kdzwie5B5B_SNjnnhTX49_8bgw4H7cBn_t9VLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79449" target="_blank">📅 02:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هالند وقتی تو سیتی بازی میکنه، بین بهتریناس و جلو هر تیمی که بازی کنن دست بالاتر رو دارن تقریبا، ولی تو نروژ این شرایط رو نداشته هیچوقت و همیشه بار تیم به دوش خودش بوده، دلیل این که قدر موقعیتش هاش رو میدونه هم سر همینه حس میکنم چون میدونه که جز خودش کسی نیست که جور اشتباهاتشو بکشه و ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79448" target="_blank">📅 02:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79447" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UavU3ydHlqIVFBkTywo2BkSbacImlwwJCAizwydCj6HDMeSBoxoOqKDHNqhA7C_BWHyX6wS9lnaoHGWvNttqxmpsf-a0z0VKNGSocgEHsef7uKgOpRgyPxnA1pf4PxLte1KRAQHqCI0z7cnmjVv70pqlIxmTZcClQwV6H2SkyrGT9HtNES8ZStrES-I_Wd8k_juMyZZZXFwOfkHBokrfgLZHLYSilvyVd3_pcTcTwAxDuSkJos7pHc-WrNYPRXEtSGnrEz1MUbwX4i8NNlAn71hF4CHOZgqBwpY-AyQM3EAos-icni8b_zC_Yd1jJgkaNvt0UsVsinlYcnHUf7YbsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اندریک وقتی یک تنه رید به امید مردم یک کشور
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/79446" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بازم چیزی از ارزش های نداشته‌ی نیمار کم نشد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79445" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیمار کصخل تیمت وقت نداره وایمیستی اونجا میخندی و کری میخونی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79444" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xm6g3VuiX8Ynge-hmD_qabXk2lK9TbsI2f1QDgYnBqiMWEFrHdIRALrpO1iBmXhqNVEjaEclz-wkBVUFPDYplNQCnDJs_ySqjK9SZ_mAKP3Q2MSABE8iiaDtOTYSx6_SJcfHW8GXm4VsMY4vA-pnINr8wx48hkcoEl6NX-4LZyDgvwupHayTnMLl8dqAl67v4JYE1-qTiInZSAYg4D1JA-PkFrjWgKyuo3iNMu_2oNxXmMVZdwtt9V2lXil2YG9Skv2pD-eJOVuPsX4RWAQ0e7EPkiKDRP2adJddz7Lz0fGqIvqNJZzmEdvQfqMsForj_QhZBh9T_Ye8BYWOL_mGLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم هالند هم رفت تو لیست برترین گلزن های این تورنمت کنار امباپه و پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79441" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ریدم هالند دبل</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79439" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">وینیسیوس
😂
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79438" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">مهاجم خوب اینطوری کار رو در میاره
هالند تک موقعیت رو گل کرد اونور بازیکن های برزیل انواع و اقسام موقعیت های عالی رو به باد دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79437" target="_blank">📅 01:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نیمار، شاهزاده فوتبال جهان که متاسفانه پادشاه نشد به بازی اومد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79434" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارلتو این سبک کصشرشو تو تیم ملی برزیل هم اورده</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79429" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79428">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انگلیس به این فکر کرده که بعد بردن مکزیک چطوری قراره از مکزیک خارج بشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/79428" target="_blank">📅 23:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79427">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رضا پهلوی یا مجتبی خامنه
❌
رضا پهلوی و مجتبی خامنه ای
✅
بیایید از آخرا فوتبالشون لذت ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/79427" target="_blank">📅 22:23 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
