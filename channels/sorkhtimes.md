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
<img src="https://cdn4.telesco.pe/file/EgDCOS65lr_9VKhDIC0xXSfsnC18aIFYGQZan4v6MCVTq6OLTbUD0ZqcAIihWSVoKknGC-HOV7fG07zjVZNTCVC3z-hhlBATq9vFclOixne5HTpC-hjp2ichRG8eT28ajpZfHnh29hpiI_58ExZVzRBloFMASohu08CRJStESWI6X9HG_Xg-Z3fOBWiJhs8OjyNDpWJFeH8koUKy0o6xP-LtsgMed3cet8a3MyMXOF3_93e7_fbowc79BiJXH8n3XDsDMNStji3b6udh8IBasiuVJ4aJJIIl36c6Yg7F9WWc8bvpM6QIXdJgDX74h-cLi5Aa4v-KNdP72tbDplRQWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 11:38:34</div>
<hr>

<div class="tg-post" id="msg-140555">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/SorkhTimes/140555" target="_blank">📅 10:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140554">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/SorkhTimes/140554" target="_blank">📅 10:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140553">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ogs5jiDEi5j64Twf2pSJMQqzSpEXRnsZHr0wheJJ5SYGV8fAjMcYBu0-eEKzE8C_Ps01a3qYIXbft9zeLtaaIEGKPGfzyZNq2O7150hI_i2NzLHAFNBe_kNrcxl7cf41OfWhctGpE66E1b0QLPtYFaOwUM9807nU85dT0sw_v9vWVnUG_jTu5V5nuJHleZSTiv1Ma7RjNXSWfoV0MCyI4t55ro_k5sH36xlqMCEk0DBIYmfpgqmVIdqim9tQw6PF62HCr76qE8JTrBH6IbKvMOPgOVIRPhCWqYGAC9z6-UFzv-4SyPcTiYkR-m8rsrqMHckA27qBH-TJadHQd0YJHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
⚡️
باشگاه استقلال در پرونده فابیو کاریله که فقط اومد یه سلام کرد و رفت به پرداخت ۴۰۰ هزار دلار محکوم شده است.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/SorkhTimes/140553" target="_blank">📅 10:43 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140552">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">❌
❌
❌
سه وکیل خارجی باشگاه بعد از دیدن مدارک جدید در پرونده آسانی اعلام کردن، درصد پیروزی پرسپولیس تو پرونده زیاده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SorkhTimes/140552" target="_blank">📅 09:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140551">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQKvWrwWgEMNU9C8aqN80_lAm1BY7FzNKNM9wsmQmvprjK9k3f1xOcy2F2Unyg7JnYpQcAaNlX8jCxFMFG3x2bXCQPlbBvQwxFlJkZ06wqMy7vzocWUD09ZlPu8kw323CqTEONYXH2DUFAbDtL8m_b3QI3qIqmdVrIlj2hhGc0ZV0xZ6VsUbZgz9Q7q9SdwJu4UQKh04oIaZJYEB9Uc45oq34NyuceZUWf2TbONYiLHDt7CAtPyW2GEt0SsFfTpgLtc-DzYlLboV-wvcpt6eE938BP3BSh2qk5oC2dNYSEiXGI3cBWHZBsdn1YnbjHBTBATmHdZOSBBTDncnnkCv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/SorkhTimes/140551" target="_blank">📅 09:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140550">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srsOVRUHnKj0nXd5s4aHrwXz-FifjpJq8VbMv7QtUh-0MNrEuYKEUZqJ7ioVwDi3XBxkLeUF7emJ2a97K9Ikr5rvsskXZebeHy5YgWETAYjsRGFs3fOojhrjHKZeSygyh1pGsOch0AqXPnF6_BYc3jSdKzAn5k9rEuuzznaQWODlTmjN-OX4owo3gS0Bgbo5CrAZvEcMxqet9kvx8IIxdHZ99EFO9ejFz8AwGsj2u0Jj8RwX_vpq5w4qpFUAoQURTd3TtwV7ZHebyLF8fX3SrcTFc3SFDYRdkqEMGsm9V9IU124uauCO4rgLRnTv-r8MNAxYVxCpKOO49yP32oIoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
شبِ حساس لیگ ملت‌های اروپا
🔥
⚽️
فرداشب چند تقابل جذاب در برنامه است؛ از جدال نزدیک اسلوونی و اسکاتلند تا رویارویی مدعیانه چک و کرواسی. آلبانی با توجه به ضرایب، شرایط بهتری مقابل بلاروس دارد و سوئیس هم برابر مقدونیه شمالی دست بالا را دارد. اما حساس‌ترین بازی شب، انگلیس و اسپانیاست؛ دیداری که می‌تواند از نظر فنی و نتیجه، متفاوت‌ترین مسابقه این کنداکتور باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/SorkhTimes/140550" target="_blank">📅 01:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140549">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASINgTwpTewXrqY00gnelIcgmsPVystys_oEtuIX6yGqFn0sXgEalZ_nHekGFKwQWcUH3U0pw_28g_a0ThGgwDyDbYyA-x7vl_oCRBfx5YVqSm5R7i08tBSXx1_fISfMwnb4QtAuTzqP0vt7pRB9RdhJyxVWFly44ZLjuSQwh775eum5buy4EIVnhG17JkjY0cFZtv-vsBoqxkb_EmY5NjINf5K6-Kuba27UGLo_I8TE_6HPuJCfzbpAgAH08htqPjesnyUbsmGlY6oriMxJH7TCMFqlomMiQrL5AGBAy6poipeeXbKPZGSaxwToTGcTKaV0yJNE-BId6sihdjO3wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اعتماد ویژه تارتار به جوانان آکادمی
🔻
مهدی تارتار در دیدار تدارکاتی امروز مقابل چادرملو نشان داد که برای بازیکنان جوان و محصولات آکادمی پرسپولیس اهمیت ویژه‌ای قائل است
🔴
در این مسابقه، ۷ بازیکن جوان آکادمی فرصت حضور در ترکیب را پیدا کردند تا خود را در سطح تیم بزرگسالان محک بزنند
🔴
این فرصت می‌تواند سکوی پرتابی برای جوانان پرسپولیس باشد؛ حالا نوبت آنهاست که با ارائه بهترین عملکرد، اعتماد کادرفنی را پاسخ دهند و مسیر خود را برای حضور بیشتر در تیم اصلی هموار کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/140549" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140548">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGWuBJOSh4B-f6A3iImAu-iGOvtp7CXMI1qDWyLEBJWe1HjYdbNwDP5mymvNZTmS6OwrUPs4b5Wz7xT6eRcvdICgylRdEtXUiTGAzXJv5aNlFeoNgXNbZJOvw5cgAVSfIGmSRjXrEg6fv-DaY55_hhmRwBsBhzmD5o6LgC_sna7dui3gu954KpNYJ6awRJZlQ2p0K2r1eujHBNSkL2jxjZaafCLZNfLmGMMqUtoHVC42pdNZGI4CVkKyIp7bjoJ3_rRF5Hjwg1wS_gcN5KQZjb9RWFWm5J35coxN5iBKUWx06CUmnBaATzvOOVtZEbD5J1DmmhQdSZHlcGDGlWVXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نتایج هفته دوم لیگ برتر بانوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/140548" target="_blank">📅 00:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140547">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/140547" target="_blank">📅 00:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140546">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpEu0j2WnzQZatAmA_jw0T2ZkQaqLQaZJaZIs-IMerye-5ylFsA9CMbLr276hnEPVHpqfZiuEfk1QCllyww44hr5OoPG3cW3bxLdppVlboSkc2H6ExVcDyJdCVilX5_NEne9k4AMJAVKFK5m-kmjhvNSCuX1fgA7e84dI9zSbRSLZ_AnqKC1amKraKK5ZVb3NbFvAB4uj59iShTPXRQIqyq4Qv2kpISByLOgY1Naaqyju7sYRy86BLddJ82Vo29_LwhtQPzRFhAHVz4W443vtM4asJPYIdfYB4tB1h4uSXz6-Fs3ccpG7w3dRlGbp5fBRF_5FG0qndyQsRRwZOww7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یه سری شایعات از بازگشت اسکوچیچ به تیم ملی در حال انتشاره که نه تایید می‌کنیم و نه رد می‌کنیم.
/فوتبال برتر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140546" target="_blank">📅 23:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140545">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⭕️
نتایج ۲۰ بازی اخیر ایران با قلعه نویی ؛ ۸ برد - ۷ مساوی - ۵ باخت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/140545" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140544">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">❌
❌
برخی اعضای هیات رییسه فدراسیون فوتبال هم از امیر قلعه‌نویی راضی نیستند و خواهان اخراج او هستند اما مهدی تاج تمام قد حامی او است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/140544" target="_blank">📅 23:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140543">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
👀
صدای پای اسکوچیچ به گوش می‌رسد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/140543" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140542">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✔️
✔️
چیت ساز، معاون وزارت ارتباطات :
🗣
حتی تو شرایط جنگی هم اینترنت قراره برقرار بمونه و همین که الان اینترنت وصله، نشون میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه؛
✔️
✔️
اینترنت پایدار و باکیفیت جزو حقوق اولیه مردمه و خدمات ارتباطی…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/140542" target="_blank">📅 23:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140541">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای  جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/140541" target="_blank">📅 23:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140540">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/140540" target="_blank">📅 23:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140539">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeDcdfPp3doXZwDJ1OalD5uZUne9obUHCeZVmmVqEFOfRlkM4Y35b8XpS9yQiUFiYtyINaOoXaAziPuYRvDpN9CwslILh1ThSfoLy5v86BnCjMmcdXJsFAJ9HegExS-PiDgXIecw1eAk6eWxSxChD2w9EQCWPTPwdu82USngUXxXoNUYIDprx789_nIZbshd6FAjjA24ZrDsQMclhVDjgcVUo6c63tOiewh4aJb5ZqpnhsEUF0v1Kn1oS-Bk_fnHy8pc2INML4iWlwjf0cnU6Y3SQq2A-ffJJeFaa1h_urAnom0Pd1fb5_8U_mnFBf0fE-K48PPk7dxP1zkrOzvLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تولد مهدی تارتار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140539" target="_blank">📅 21:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140538">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
مهدی تارتار با بازگشت میلادمحمدی مخالفت کرد/تارتار همچنان رزاق پور را میخواهد/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140538" target="_blank">📅 21:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140537">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140537" target="_blank">📅 20:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140536">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
غایبان پرسپولیس در دیدار دوستانه امروز
⏺
حسین کنعانی، علیپور، عمری، ابوالفضل جلالی و حسین ابرقویی، باکیچ، ارونوف، نیازمند، زارع، محبی، محمودی، ایری، لطیفی فر و شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140536" target="_blank">📅 20:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140535">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsk4D9cYZ9Ce-26zH5V8yGI3AVv3qOe-SP8Z6egUxujjiEdfukpjs3f58QkyHIRVw1izT0YbdlddNCoM2PEVdFjsr3DkrpnHjqh0AZl_0Yf1E9TgsKxudFAlWgVHC8T9FcGlAeT8TRzvmG38njMsyrY3eHrSYgADnwdPz7ug4U1xCZdbpJT6V4PLCgrWmbb6LA0hGz8QLzrA6LbBOaUVKSPvZCUOs_9So75MOYBRgN5-o91GTu1UxelK9SMbg2DUFJipSE1PZxrgAUU8Lm74WzF0ziX8aX4umRS2lkZK-HADnaUMg_KbtgXP6C6HVp5H2JWyYgK16li7o6Gum5g4ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیه - فرانسه؛ جدال پرتنش در قلب استانبول!
[
ترکیه
🇹🇷
🆚
🇫🇷
فرانسه
]
⚽️
ترکیه در خانه با تکیه بر فشار و انتقال سریع می‌تواند فرانسه را تحت فشار بگذارد، اما غیبت چالهان‌اوغلو و ییلدیز روی تعادل تهاجمی میزبان اثر دارد. فرانسه با حضور امباپه، دمبله و اولیسه از نظر کیفیت فردی دست بالاتری دارد، هرچند اولین بازی زیدان و تغییرات ترکیب دفاعی می‌تواند هماهنگی را تحت تأثیر قرار دهد. باتوجه به فرم دو تیم، بازی می‌تواند نزدیک و پرموقعیت باشد.
سناریوی محتمل: گلزنی هر دو تیم و برتری نزدیک فرانسه.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/140535" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140534">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f84e7380b8.mp4?token=i2tpzbKET_aiFwyfccCTDrz4QLf360OHpAGCSUiG-7nVepDOOGLdzRE9JujGhVjjmGDsrKpgy5cgOby6q2DoXriFNFiUoniPvm2yJUwRmqKfFLI_uTAWPULpDUmBuwNm_HkW-gpHgl08EqmltpZfxS4NuU0tR8DVbzahht5yv-aOy9MYNE_k6n9ONt8wNUAJpUf3nBphebNbO2I2wN0LceHO490QVlGe72CcgKimtCV7YaDxLqj3LrGaN0enW4qH9vZh7sHJzqc4HcvTAhqgePQMr6uJxlpLmfH_1zmUszZqac9AOUb-J6_REWmabHRNmkfMPqKsxpNcG3KKAylfM72bhP-94jCi4NQuPS0K4GvMwyxcGCsDFJ0fo7ZZy38Ijkd7Nc8puSrDCAVPec4kDqwlkElo0i4r9LUe6V9OKUC977wUG3zvaWiDn5i45gOO5W-G_1Qz5WRpZWh0sRMhWpTwlEaqYNyXSGgmFIu2WM_fP_WLkiT2L3KlAcCUMAu1cS1Fb9Lx3LlWzgcJUVvJbxBUYei635fRL4ZKPturu19cu3Kht7rMa_hU95D8YcbJ_Zk63kEJPAUaMXR_p27FtUhNs22c1urwv9PtMlXJoXz26NBJ1RFA0D_hvI_gtaZw2xQLlFt91H97t5TJoKFHbyu76GiT5AKg7Z98gRmDAvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
صحبت‌های کنایه‌آمیز توتونچی، مجری برنامه شب‌های فوتبالی به تیم‌ ملی فوتبال: دمتان گرم! در کمتر از 48 ساعت 7 گل از کره شمالی و ازبکستان خوردیم..!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140534" target="_blank">📅 19:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140533">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140533" target="_blank">📅 19:34 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140532">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
❌
❌
❌
شاگردان مهدی‌تارتار درپرسپولیس امروز عصر در دیداری دوستانه یک‌برصفربازی رو به چادرملو واگذار کرد. علیپور بدلیل مصدومیت دراین‌بازی غایب بود!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/140532" target="_blank">📅 19:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140531">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18169032d.mp4?token=aQ-V_51O5Q5U87qkbXQaby-VhJkSKvdjRsjDCuUA4a1nsl8XOnMSZc4nX9Y_9YshbWB-RqRPHssCyy8fxiUtH7Jb8j7FHwJnjyPtKt7vYOEWmATDt0opXK_f986BAk89awvdDxqxKzoJf15RYtrGWP-QssSDKoOh-YKP_Prrx3s0DMsfvOWAzNmRaqJcCBsCOjJpvYQ5-hZwgn_s3wOUCoZXhDxPoHvnlraECmy9ndlFuIYTcQIdnTtTYTGYewmeYBPzNl_vBlqz_safBH-p5aJzgdbVdAyHvkdS9xh1cF3-sDBiNOhXLJvm8OC1CFywe37xJM3XYsanPJjyVYUQyTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل های بازی بانوان پرسپولیس چهار - صفر ملوان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SorkhTimes/140531" target="_blank">📅 19:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140530">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
پایان نیمه نخست  بازی دوستانه
✔️
پرسپولیس صفر ـ چادرملو صفر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/140530" target="_blank">📅 19:00 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140529">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/140529" target="_blank">📅 17:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140528">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjhGObPvczjAzEPcMKHRrm03GLjRRMB4liPJhIzSL3VuvFTA1CFn2oztpqtdv2W5hky9ImOUf2I7sd_yetJZ6zF7osARO7lcLJA8vCvL7-0_iY0HnFxY2irF-7tuPpwqpMwOoAm_CnF1MFNrn4-kWD7aDtc5nfAvoamu1YDhyYxsK4jESlSQKWF-aUko49rogX76L22i5PxCFd5H3tGCrrYoaTByBDCF_ybPNgFoiOa1OuOhf1U3pzQZt6ra6ZNib3fTIvU-FZWKc_0mD4Wc2tIcU1CTwhNJMoi0_gxT-izdlgbFSpyHVJoBxEK5cQV6vb1aCu0KasshFUkt8Bj_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
پیمان حدادی که بازی پرسپولیس و چادرملو را در ورزشگاه کاظمی تماشا می‌کرد همزمان بازی تیم فوتبال بانوان پرسپولیس با ملوان رو هم با گوشی دنبال می‌کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140528" target="_blank">📅 17:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140527">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFo4YSaVPVD2ha48NuS_aMr71zzL7dRbsSUg3M-pt2LFHtwUo3VPmVF9qAtw44xyJehqNeWi6jYOGREhyDbTifRJJS_PMM19QYsKyAkmWZWJVat6sMarSmom82dNdvsF5umRgSfnMmpARgR8ejTuheLxHYyAPvRkzVA6_nWbr41r-_YNGxbsqmUmdJ6EYBcMy5N_eH3ms8QQRtDNYpbOrNF7L2wtsKc8tGehytZiZH3yyXQhcFdD5b72k3edSWDmFtw7hgqGDjXDf9FNkVeUcrKShBBNbSejN2HJYn99ikB51j2y9VFm5OHlR_KDZEkQjjqXmAN-kCPR1jyJ_JxARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عکس تیمی پرسپولیس پیش از دیدار تدارکاتی با چادرملو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140527" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140526">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
❌
پرسپولیس فردا بعدازظهر در دیداری تدارکاتی به مصاف چادرملوی اردکان می‌رود. با تصمیم کادر فنی دو تیم این بازی پشت درهای بسته برگزار خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140526" target="_blank">📅 17:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140525">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOYW4-o5Dboz_tQeDnDY-fcjultnPXVeqscSLZ7cD46t-try1DeweNH8XQYnge554l1hCTcm1QfKseys7CFssvEG7gG-oMWYOBdMaQkokReBfJD7H3sx29Ayh6fxfuFDjn4dNKDbrzLjlHNqp06poX93nJPNGtg0bVFimlIGoK4OcMVmrLBabOYwJ9dxHMxsmps5zaMUISrVbwPx3E4d-3_AzaXvtc5B4L3ZV8XzTojHLmQNcRhoz_xhSC1Q16hbPCTJYkHDezXHgYMJLkCkxFAliucowdKHgTQxmq_eY4BERHUrlRyrUSPaB9E9BG-5AW-rAO-RtqC3PnyrrIDdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با توجه به حذف دیروز امیدها؛
❌
❌
میراثِ قهرمانی «برانکو» با تیم امید در بازی‌های آسیایی بوسان ۲۰۰۲ دست‌نخورده باقی ماند...
❌
❌
این آخرین قهرمانی امیدهای ایران بود و ۲۴ ساله هرگز دیگه هیچ مربی نتونسته تکرارش بکنه تا بزرگی کار برانکوِ کبیر بیشتر به چشم بیاد...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/140525" target="_blank">📅 15:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140524">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/140524" target="_blank">📅 15:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140523">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
🤩
فرهیختگان: بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/140523" target="_blank">📅 14:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140522">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O49xbQ0cKlC1PHnXwSU_UhbciAsUd8VVWIMpqJyuUcVjXPwxf2DKmOsphXiFawFaIJXpC3lhkiggP0Vnh-BIcjlNyuoDLB3mwa9HJTV2r4E2PR58vUAEsq29FivmXF3wV5hV5_rO-OPGSN_1K2DA002bv8dG4Za3Tu_-Hoe0ocltSymxJg10Eh2p0bntARfgaR83JUbvY3tVZnFS5H440WSMfjnyT1dBCjJBHwKxIJOljxO0rs-cKsqGSeiFscyS__Tq3UqMN3ECeCe1N8nC79dt5UYrcWes_YuZ0VsphqAqF6DXg7At7w1MgqlUfD0NAIGbBfqsQUMPRuQowYsCgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری؛ ترامپ: تمایل دارم با دکتر پزشکیان در سازمان ملل دیدار کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140522" target="_blank">📅 14:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140521">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SorkhTimes/140521" target="_blank">📅 14:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140520">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🤝
🤝
مدیربرنامه‌های فرهان جعفری: فرهان اوایل دی‌ سربازی‌‌اش به‌پایان‌ میرسه و میخوایم توافقی که هم منافع او حفظ شود هم منافع باشگاه خوب ملوان حفظ شود از این تیم جدا شیم.
❌
❌
فرهان از دو باشگاه پرسپولیس و استقلال آفر دریافت کرده و در پنجره نیم فصل راهی یکی از…</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140520" target="_blank">📅 13:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140519">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=Ae5KBfhBmpqh1ILe1_3TUQW5xALY3LP8Vae0n31j-qH7wzJ3YTE585WL1djducgLKDjrKO22Wu7P9e3l8VPnBoVaQWyYs9dHgiEqJLrTWKxOV5q-enLwG2UR3VdRQ8KMhwWIVLgwtwBC8iCtvAyxlyZkYqgPXvyge8P5qLI6EUo6MXQmYotE57NEWYpgG2HytGWCD8slQB3oqlwl7EL7tSfGylfay3Oms3zX686NsC8h9BSmLYcv0T-0ez7E2qEbDKl-PsOsztoR5d2pyS5pB-BINdyvvqAS9LHQax9VJXwbON33fblkIqha5DNBJDGVRX8idBET6bSFeQsfBcX57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=Ae5KBfhBmpqh1ILe1_3TUQW5xALY3LP8Vae0n31j-qH7wzJ3YTE585WL1djducgLKDjrKO22Wu7P9e3l8VPnBoVaQWyYs9dHgiEqJLrTWKxOV5q-enLwG2UR3VdRQ8KMhwWIVLgwtwBC8iCtvAyxlyZkYqgPXvyge8P5qLI6EUo6MXQmYotE57NEWYpgG2HytGWCD8slQB3oqlwl7EL7tSfGylfay3Oms3zX686NsC8h9BSmLYcv0T-0ez7E2qEbDKl-PsOsztoR5d2pyS5pB-BINdyvvqAS9LHQax9VJXwbON33fblkIqha5DNBJDGVRX8idBET6bSFeQsfBcX57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140519" target="_blank">📅 13:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140518">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLFyzOFlmHWbZ9wtzTO-z_updpBrDVtkILCBbX8ZWm1wRroX8VvitWMEkVMGrXQihIwRp0oWVWN8J9UAgDAtHUvQopyEkhqiLXu0GZHxMSnE3bfOn6-RCKEXeMSH7sL-z5Un0VRVv7JIg2CShEBMokhw7LDT2nC7NGFdvf6vM_fnGUVSu_eXIlqHG4uvV989DNdnwPK_0Nf-Fxn0D1EvW_l1KIgAMRIwXDI-gaDX9TF2WKy8NAaRUf0RgpRWPE3M5xP2Mp7eZD57K08JaWCrS-5Q7I-z2SUWEVpd2Qe4lLKvJwxiRwaDx3pBxLRC6dTzfcC7B7G04ARwTWvjSNFE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
🚨
✅
⭕️
⭕️
⭕️
با تصویب شهرداری نوشهر؛ امتیاز لیگ دویی این تیم به پرسپولیس تهران واگذار شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140518" target="_blank">📅 13:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140517">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
جواد نکونام؛ مهدی ترابی به دیدار حساس‌فردا باپرسپولیس رسید اما مهدی هاشم نژاد بدلیل مصدومیت این دیدار رو از دست داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140517" target="_blank">📅 13:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140516">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJt4B60mq6A48ueofKS9utzCw1JRJ2WauWNmN6vBXLphjyDIuHH6PsysEXMSebPWCCdOQr0AIjksg6BZMroLQwVawFhdGSHdHdhDid6PU5S0JCsi4tBOeMLalO5c0Ro_hymWOC6ar1wuYsq8166IxncKtsGnZiCh739DB0I-qCNrBxov6Nij63CzU2rLGxZ8BkR95Dulzc7PRaQ1e1ZuP0MmMa0_KaNqMBswixdirFN5h8H9Gh4ssW7se21GCqj7ODNAC2kc49RvV6FHUBxOwcatNTyY5ZsdjcLYaXssb9CK8y9Ob0YrjicqvZ1MEquWcdNTnHrPtAN5gxN-W7cYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
گاریدو یکی از گزینه‌های تیم‌ملی برای
جانشینی امیر قلعه‌نوعی هستش
😐
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SorkhTimes/140516" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140515">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⭕️
⭕️
#فوری | ترامپ:
🔻
مقامات آمریکایی به مدت سه ساعت با یک هیئت ایرانی دیدار کردند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140515" target="_blank">📅 11:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140514">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
✔️
✔️
محمدحسین صادقی، وینگر ۲۲ ساله پرسپولیس، در نیم‌فصل به‌صورت قرضی از این تیم جدا خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140514" target="_blank">📅 11:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140513">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">⚪️
⚪️
⚪️
مهدی تیکدری در غم از دست  دادن دایی خود عزادار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140513" target="_blank">📅 11:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140512">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140512" target="_blank">📅 11:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140511">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvcrdv956PSOo20jZfcbDKhIfTzvS98Big5lS1TUZdfxe5aN_dsNJpCT8t0KXRIheyJFZSCHA-y99BfE11r9L1JP7uwSjbGKa-jJAoqoIyjL8VjwabnbWjGqZqTx8H6GFKKhlkHTAxdvDNwIo07tbfEpAsPpNqhF4zOtbfOs5ysw_oTK2eMQ0ou9rGv4AmqoJ0DTU_dhISrjbNy-1joVaWG3Kaw-2JLMmOzJBEuFrnJCmWl9D97c3FsJxDuc7olO59E_mdwIbA7XthY7MGPRvVV4M8m9C39UE5Vi4xT2MQGe_n-MWbMrQxayubVBG_Y3Xf27HTMa7PDUVvmLo5KjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔻
پرسپولیس قید جذب اندونگ رو زد
🔻
باشگاه پرسپولیس به خاطر ریسک بالای این انتقال و دور بودن اندونگ از شرایط بازی، تصمیم گرفت بی‌خیال جذب این هافبک گابنی بشه
🔻
طبق شنیده‌ها، تا این لحظه تراکتور تنها تیمیه که همچنان دنبال جذب اندونگه و نکونام هم روی این انتقال اصرار داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140511" target="_blank">📅 10:57 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140510">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvlO1ZF-mB4CMZZMK7hb1P-6wuJFoTaZ3ftt3J6JC8riCGjfF_zNYlp6vhuG939HKBE000AFuoZO_SZrPfCIgT5K9PUpdTiFreeN1KymSmQHwfs0ohH4KhbC2gI_3S8aw-bVIX9LExxoxLN5rB_45VCU_3G6PTMpdb6y9IfdEKg7PEOP8Ldoo73jjLPbSVxY3EsmjHc1_nVwOsoEgPis2pshluoooMCSzMQn-qNXNSR9kwddp0SNlHQK7ZScXRlNAZqmlxNfXwf_QaUZvsm0CLkQ6w54jsB3HcSLkZqI1bXbtwOtf4MzKaNLrGaLllqKdZ3566CEKKg5lcQlqa7LUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
علیپور و کنعانی‌زادگان ابتدای هفته آینده تست پزشکی می‌دهند
✔️
نتایج این تست‌ها وضعیت بازگشت دو بازیکن به تمرینات را مشخص می‌کند‌ و پرسپولیس امیدوار است هر دو به دیدار ۱۷ مهر مقابل صنعت نفت آبادان برسند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/140510" target="_blank">📅 10:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140509">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140509" target="_blank">📅 10:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140508">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/140508" target="_blank">📅 10:17 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140506">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6qM2-Z_BNX81PFazb1PIYr0hmIt-HcxVrmVbubKSYD1upGQRUcMLc8y7SeN5iWfapz93vRaElPSqCK5oBq6mHFVvGjvaNNjoc0_ho-PrZjAwcSkF0hjnzxreeUfHQpk6uSjRtvBLF3V2S242N3xtuGBPk2sMW8AKsTsQgd1sxo9KbUobeQlimtF1yVC8SAwnGi0a-8r86CUAV2_i0fmdQ7AN9HvRDqt0H-359a3Mic5ExJKfKBrSifdh_xnbpLn7PykDaSy0gTvFjTz6x4C3NG_ydgWdDXC0OXB-m5qqeeFcVg8GzLlfPt0KxYdibyk8KjWiqm5kNcHfKuWhMP1yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ITALY -
❤️
BELGIUM
⏰
Tonight 22:15
🏟
Stadio Olimpico
🇪🇺
ایتالیا با بازگشت مانچینی و ترکیبی جوان‌تر، بازی را احتمالاً با مالکیت و فشار از کناره‌ها شروع می‌کند. بلژیک با حضور بازیکنانی مثل دی‌بروینه همچنان در انتقال سریع خطرناک است، اما غیبت تروسار، دوکو و کورتوا روی کیفیت ترکیب اثر دارد. آخرین تقابل رسمی دو تیم با برتری ۱–۰ ایتالیا تمام شد و تقابل قبل‌تر هم ۲–۲ بود؛ بنابراین بازی‌های اخیرشان نزدیک بوده است.
نقطه کلیدی بازی: عملکرد ایتالیا در پرس و کنترل دی‌بروینه مقابل ضدحملات بلژیک؛ احتمالاً جزئیات و توپ‌های دوم تعیین‌کننده خواهند بود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140506" target="_blank">📅 01:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140505">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⭕️
⭕️
⭕️
فوتبالی: جام حذفی به‌دلیل فشردگی تقویم مسابقات و برنامه تیم ملی و امید برگزار نمی‌شود. سهمیه‌ آسیایی هم بر اساس جدول نهایی لیگ برتر تعیین خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140505" target="_blank">📅 23:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140504">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI8rpie2v-_6YLmQ2yR2J25hNIlfuLoVBwIOEtyVYqJ-FRRJmYah2KhuETRHtMivJNBcyCPzLXImp46HpXgyuaHWWG_MovYGZ89oyC6n1pppJ6gWAEEJrG9R-ZohfIGW3qXdAQKj8whj4I_LrVGBP3LTBBuFu8QNkbDrjOz-WgQMhomBZSIDWK7555oEzHKmvMPZ2aBFvaq4KH6REHgNDjbx5b9VyWc8RvLUSxVU62HD5UNCCOeGu45xdXTBvmnxullkmqT5PXxo4wt-VEZtC_PMcfvUXEVGFUyBaeEyynNDkhhieVEcYc_CU7yRQU_Aw5Jwpj_zuQfrmc5TIf_9GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎉
جشن تولد آقاکریم برا محمود خان و آقامهدی
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140504" target="_blank">📅 23:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140503">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199c169158.mp4?token=lf0_xZdd9d3lFA8FSzf6VBLpaT5QgyMQuK4YG2Zwef0Q7tW7_aWfyu1Ewde_MqqMxUwGFF_Z-FuvjVSb_7B7tzEg3FfTbDOGyuhV2L-UBv7ST-Vcxk83kansIBfDrslDfodSP2OE0pNCVUx0_fhZXMhdq451YXntEBX62EOi-mZ3YYM_LSQsTybmjPscpLd493ItmxRBGpEgWV16e8TnAgkvkXCNI-3cm5yX1SYzJm3OIX9LxT0nzqxBp_HMFsk4lfLilmhxRljh6haZ-e9Gl-TklFJCDb8OK_dQdu1WHIMQ-Xia_VpomamBlaWKXq0WTyGuMJAJ8wdn4p3vFpjOAYue2t3eXM65kEOOB94pnffePuSUCPAfpaFy4WkBY_Ei_wcX9HIQ3m0E5P8590HQewcnN5-zuYuuH2S3k0TTE5H6mfOlG3t9Fy0fNTiDGns-j8HECAhbrnBiLNfIUqA5GT9K6Fz7gLq8-IhQ6G4hV6BjnhC2TIRxeucJk0QTlAqERYxs8uw8DKr1YB6ilGAM_rOK4wlp26pJJcVPdYUSgr6olKQsNEmrTAl1F-WEyx7YOEuRw2Vq_dRH6rZn8AeLaTVoSll9qwFuUFy4bkJoX21uucc5lsOzIQ1cnbrm0yreWk9HxAvpmzwEP4qQZrKGVYj36P_1CSsydg8RLcdEckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199c169158.mp4?token=lf0_xZdd9d3lFA8FSzf6VBLpaT5QgyMQuK4YG2Zwef0Q7tW7_aWfyu1Ewde_MqqMxUwGFF_Z-FuvjVSb_7B7tzEg3FfTbDOGyuhV2L-UBv7ST-Vcxk83kansIBfDrslDfodSP2OE0pNCVUx0_fhZXMhdq451YXntEBX62EOi-mZ3YYM_LSQsTybmjPscpLd493ItmxRBGpEgWV16e8TnAgkvkXCNI-3cm5yX1SYzJm3OIX9LxT0nzqxBp_HMFsk4lfLilmhxRljh6haZ-e9Gl-TklFJCDb8OK_dQdu1WHIMQ-Xia_VpomamBlaWKXq0WTyGuMJAJ8wdn4p3vFpjOAYue2t3eXM65kEOOB94pnffePuSUCPAfpaFy4WkBY_Ei_wcX9HIQ3m0E5P8590HQewcnN5-zuYuuH2S3k0TTE5H6mfOlG3t9Fy0fNTiDGns-j8HECAhbrnBiLNfIUqA5GT9K6Fz7gLq8-IhQ6G4hV6BjnhC2TIRxeucJk0QTlAqERYxs8uw8DKr1YB6ilGAM_rOK4wlp26pJJcVPdYUSgr6olKQsNEmrTAl1F-WEyx7YOEuRw2Vq_dRH6rZn8AeLaTVoSll9qwFuUFy4bkJoX21uucc5lsOzIQ1cnbrm0yreWk9HxAvpmzwEP4qQZrKGVYj36P_1CSsydg8RLcdEckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هر جا رفتیم اوت شدیم؛
🎙
درخشان: مشکل، ساختار فوتبال ماست
🟢
سال‌هاست فوتبال ما به قهقرا رفته است
🟢
آیا لژیونرها فوتبال ما را ارتقا داده‌اند؟
🟢
بی رو در بایستی ما فقر فرهنگی فوتبال داریم
🟢
ساختن 10 برابر نیرو، بیشتر از تخریب می‌خواهید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140503" target="_blank">📅 22:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140502">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=sR6Z27BieFxkPJecs_sXNiYTZwWXrGpnwJbSHpBFgIHaZUVPaFXfEnnqbb_pFmWjVC7VwaPsLArTTHi3zVeuVz_-h-ZfRv0L51iJlYcBQiSIvFdg8XpnEHEvsq3QIiKmrp7Ghx_oWHwY1avoA2HWSGbz56qmbWF_1k_lTcLaVLJFQNQ5MROO4-5gUd3tpsnfRhKOlYMrd58gKjmhVUvfMlQW8C1K2rTsLP3gi8IUyEjdeb1_xnT2MeTaeaq53nkwFZm_WQYMJUICBTPrqzVmMKEFpkj89IpoFWTpEKr49FNPuPWnyAxt5oU0G7R-V2dh4kb8H-9Vojady7_xq4OWRLO5_3UEZmGU_Sz_frtlc2kAhaD1EAiIWhAIZ5wkDkDd3uDBNj8Zyq6EI7GFZ94djxN-8BXROnjC2PE_QTYS4vCNeTNVwGsJ4gqREfpnL7R7hrBbWl_ou67EupFpSEL9lmFVchvQBgL03p5cvAvYlX5U9FzEJ3zSe-yF5s0SKfJCPMkN1cU1w6cZyH30iCuiui1kdaTnG9Ty2Z-FpMP5rTQdTvWqYSWJnHXgFzm89uDO69pCX86PnxEJ89rhtr4h9nkZruXR8ZhgypYU68QWP7xR2NMWgrdc-llamSYzL0FUvqxwiJBavt7Pys5dQc3gIsz5lSEGGf5T_ezq57_Cm8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab25e53c97.mp4?token=sR6Z27BieFxkPJecs_sXNiYTZwWXrGpnwJbSHpBFgIHaZUVPaFXfEnnqbb_pFmWjVC7VwaPsLArTTHi3zVeuVz_-h-ZfRv0L51iJlYcBQiSIvFdg8XpnEHEvsq3QIiKmrp7Ghx_oWHwY1avoA2HWSGbz56qmbWF_1k_lTcLaVLJFQNQ5MROO4-5gUd3tpsnfRhKOlYMrd58gKjmhVUvfMlQW8C1K2rTsLP3gi8IUyEjdeb1_xnT2MeTaeaq53nkwFZm_WQYMJUICBTPrqzVmMKEFpkj89IpoFWTpEKr49FNPuPWnyAxt5oU0G7R-V2dh4kb8H-9Vojady7_xq4OWRLO5_3UEZmGU_Sz_frtlc2kAhaD1EAiIWhAIZ5wkDkDd3uDBNj8Zyq6EI7GFZ94djxN-8BXROnjC2PE_QTYS4vCNeTNVwGsJ4gqREfpnL7R7hrBbWl_ou67EupFpSEL9lmFVchvQBgL03p5cvAvYlX5U9FzEJ3zSe-yF5s0SKfJCPMkN1cU1w6cZyH30iCuiui1kdaTnG9Ty2Z-FpMP5rTQdTvWqYSWJnHXgFzm89uDO69pCX86PnxEJ89rhtr4h9nkZruXR8ZhgypYU68QWP7xR2NMWgrdc-llamSYzL0FUvqxwiJBavt7Pys5dQc3gIsz5lSEGGf5T_ezq57_Cm8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
نتانیاهو تقریبا برای یک سالن خالی سخنرانی کرد
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140502" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140501">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">❌
❌
حین سخنرانی پزشکیان، نماینده‌های: ایالات متحده آمریکا ، بریتانیا ، آلمان ، فرانسه ، اسرائیل ، سوریه ، لبنان ، عربستان ، مصر ، امارات ، الجزایر ، لهستان ، سوئد ، دانمارک ، کانادا ، ژاپن ، جمهوری آذربایجان , مالزی ، نیوزیلند ، استرالیا ، جمهوری خلق کنگو ،…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140501" target="_blank">📅 22:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140500">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
✔️
✔️
✔️
✔️
تکرار تورنمنت سه‌جانبه؛ دو بازی دوستانه در برنامه پرسپولیس
❌
در جریان تعطیلات پیش روی مسابقات لیگ برتر، شاگردان مهدی تارتار تا پیش از ادامه مسابقات لیگ برتر، دو بازی دوستانه با چادرملو اردکان و گل گهر سیرجان برگزار می کنند.
🎗️
«سرخ تایمز» دریچه ای…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140500" target="_blank">📅 22:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140499">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">✔️
✔️
#فوروووووی
❌
با اعلام حدادی جام حذفی برگزار میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140499" target="_blank">📅 21:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140498">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=WGaWhg_suq1LipIliBfWb5--LWQVW_NyiHsoX_DaUV2aqmzIUC4NLcYhX1IJyzF2ikvfiP9hSyEGTpad2-KF4TMcxNndpXsW71G3TEywKBn1vIE9aS4QZG9teCTuV2bNS7YjPqOgkmSq2TLG7abyFDRJm41yK6UmhPm-hLYifZ5SFbW_mdvMLt9MqrJcA5wFqxT4DgkSiJ9gkJVSVheLi3xwFvVhATAwqd6On-IlkktwCzuxSwgncI5Bm4QbCE7VAYbI3BBVqbEkB-SdYX7cIeJCnkr110Ta95ijUBmHkmXLafHNQx7_oWb3MlVyNDdEnWTMal4hC_2oyUnm-BaYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=WGaWhg_suq1LipIliBfWb5--LWQVW_NyiHsoX_DaUV2aqmzIUC4NLcYhX1IJyzF2ikvfiP9hSyEGTpad2-KF4TMcxNndpXsW71G3TEywKBn1vIE9aS4QZG9teCTuV2bNS7YjPqOgkmSq2TLG7abyFDRJm41yK6UmhPm-hLYifZ5SFbW_mdvMLt9MqrJcA5wFqxT4DgkSiJ9gkJVSVheLi3xwFvVhATAwqd6On-IlkktwCzuxSwgncI5Bm4QbCE7VAYbI3BBVqbEkB-SdYX7cIeJCnkr110Ta95ijUBmHkmXLafHNQx7_oWb3MlVyNDdEnWTMal4hC_2oyUnm-BaYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140498" target="_blank">📅 20:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140497">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1FiK4CdnwhjmRr0CT68baP22LXN_Fj_mqF_lMfQ-PXOL7JBaS3-BWPv6AKYEyDPt6van1fv_gVHSXJJn5vxAwXGy8FN7hZplZdvN7SWbndYbW8VpLw3_2DJ604R7kT9ERYAsJx-_KSIZEYWBa_70k0yYTqEU3hJM06nkR764ctF-9WAmnwZHh5ZB2v2kJfjiqN8N7ZapU55vvW3CGbyHpfMOoMjqqsot7ZwC_9alx9i1SIrEM6IneX05x98eI5T1mteUf5fWq3UmzZZ9w41F267rmJk9FfbdQt1Tv_sY66fGC1hfao3wd0nebtaV4Lmy4x40-alnsLIDL_DUMfeuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/140497" target="_blank">📅 20:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140496">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=n4mYp1gdJzllMyltv9fWDlIQKlc1LbmOGLM35NxZ_qVoQDgBXDRwmrAE8yDSONA65ng1Bf3FJA4ovp60zdwHA2HrBzYV8LEiOg9gRMxhbXl7kD5NMKFykGNAkT0GD0z0NN9U1uXCbIt9XsSrCrjlam39sYNBJcxXXDgG4dwfha2BlYqcYGGHgsKDxwx9apRmTFF0aZaXtzRbT3DIczRl0NM_PeyTBVI55jJd0dqEvntZX7FN2n27YNPGQ80Sf1U0n9aCYFxRxm-oE0U2PCcsL04xfkF2bEp3OvoV0p0udD3kZp62gIXC7f-ULf295G8LABMfy9jM24e-rCy6zV7HSp4p8ZkgRoXWCRJk-0CSfqNH5_FIATJImHkBwskYqZSOvTBSuAP_SHz2x9IQ-5IjZ6SvFlCy1rC0UsQYa5Ywnya2pvdzJGUG30wLksiq_tiSRk47u_B8JZytfnIaf-vqMUYCO4WESQLmZ-ng6oJkHs477RScEWFScJFY9C96CV0YOXPnUXBzybYSKwA-6rPLW8obyhbt6ywB_9CKxoZVbP0vdpi0FrLvm4oEnqVKgWCPyT7po0k_AGRaOVKkvjNrtWghTWPhIKHGZ_wqUz5E4CYp_4kwxDNLxhbQK_l05XhJG3U4EX3oXBk_WZQs5EawX2PKgzN2jcH55iokBWM-Oco" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=n4mYp1gdJzllMyltv9fWDlIQKlc1LbmOGLM35NxZ_qVoQDgBXDRwmrAE8yDSONA65ng1Bf3FJA4ovp60zdwHA2HrBzYV8LEiOg9gRMxhbXl7kD5NMKFykGNAkT0GD0z0NN9U1uXCbIt9XsSrCrjlam39sYNBJcxXXDgG4dwfha2BlYqcYGGHgsKDxwx9apRmTFF0aZaXtzRbT3DIczRl0NM_PeyTBVI55jJd0dqEvntZX7FN2n27YNPGQ80Sf1U0n9aCYFxRxm-oE0U2PCcsL04xfkF2bEp3OvoV0p0udD3kZp62gIXC7f-ULf295G8LABMfy9jM24e-rCy6zV7HSp4p8ZkgRoXWCRJk-0CSfqNH5_FIATJImHkBwskYqZSOvTBSuAP_SHz2x9IQ-5IjZ6SvFlCy1rC0UsQYa5Ywnya2pvdzJGUG30wLksiq_tiSRk47u_B8JZytfnIaf-vqMUYCO4WESQLmZ-ng6oJkHs477RScEWFScJFY9C96CV0YOXPnUXBzybYSKwA-6rPLW8obyhbt6ywB_9CKxoZVbP0vdpi0FrLvm4oEnqVKgWCPyT7po0k_AGRaOVKkvjNrtWghTWPhIKHGZ_wqUz5E4CYp_4kwxDNLxhbQK_l05XhJG3U4EX3oXBk_WZQs5EawX2PKgzN2jcH55iokBWM-Oco" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🎙
جواد خیابانی: تا دلتون بخواد تیم ملی با قلعه‌نویی به ازبکستان باخته. سال به سال دریغ از پارسال. تیم از جام جهانی حذف شد، رفتن فرودگاه استقبال!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/140496" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140495">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=f86yeAhXbWJXLQmnfHmMiynEjjfStR-Zzo51wn1vxtBzBd5p-LwIuLxfvIDWo3WPoZuNHMfz9d5dad68FAXYsyz80xcxdGbqGeaG8QNFCG2u7tiawC6OBCmOlPPrsg1koYdx3jEySyA-7-DcwM-CMHz8cVvCoAl4a7rQYnDYH1TcJcSF2Jvj5vqKtunLs9cBP8Hh-TQrPhCQ-rFFKeuMazqqAtNYm3NsUWwcki2WsCSNRRksZWNOPvub3sohosQ1caVE283chzcBs7xlV8X1wPOzEX_v5elhMhY8FwbXkpfrYlrHC5ATatn7SSkwyGEHm03MjErL0anz_X7DB_E4c0C_hoZ5Rt8snSe__lYQ9X1hGgN5oT73LRxLhlzPM5VOyoCDF3JQ7wrRtbhGdwgN80fa3GM79Pu2rtAl0ehQGdALPilfMMno1pRQybOmG0BIHMaKZ6qz7xyOVALuYTO-DB49k5xoR7ZRXdxojIZ04eBQm21CWeRQhUDsOYTsOKWmvxa791d3y9Nu05drETP8pb9CPCPHI99J6pfiq77tnFXCW8GsjRmg5vcsj6wikptSAn4LpkZT4Wf_yjJA_nR5MEPVLiBfDopepPFDohxc85CKB70nx5JMu7jRkGrfwNQNEHxjYaf1tEGyP1NT2oOZDduGC1ZSYgnZ37GmwANWnfo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=f86yeAhXbWJXLQmnfHmMiynEjjfStR-Zzo51wn1vxtBzBd5p-LwIuLxfvIDWo3WPoZuNHMfz9d5dad68FAXYsyz80xcxdGbqGeaG8QNFCG2u7tiawC6OBCmOlPPrsg1koYdx3jEySyA-7-DcwM-CMHz8cVvCoAl4a7rQYnDYH1TcJcSF2Jvj5vqKtunLs9cBP8Hh-TQrPhCQ-rFFKeuMazqqAtNYm3NsUWwcki2WsCSNRRksZWNOPvub3sohosQ1caVE283chzcBs7xlV8X1wPOzEX_v5elhMhY8FwbXkpfrYlrHC5ATatn7SSkwyGEHm03MjErL0anz_X7DB_E4c0C_hoZ5Rt8snSe__lYQ9X1hGgN5oT73LRxLhlzPM5VOyoCDF3JQ7wrRtbhGdwgN80fa3GM79Pu2rtAl0ehQGdALPilfMMno1pRQybOmG0BIHMaKZ6qz7xyOVALuYTO-DB49k5xoR7ZRXdxojIZ04eBQm21CWeRQhUDsOYTsOKWmvxa791d3y9Nu05drETP8pb9CPCPHI99J6pfiq77tnFXCW8GsjRmg5vcsj6wikptSAn4LpkZT4Wf_yjJA_nR5MEPVLiBfDopepPFDohxc85CKB70nx5JMu7jRkGrfwNQNEHxjYaf1tEGyP1NT2oOZDduGC1ZSYgnZ37GmwANWnfo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💛
🎙
حمله جواد خیابانی به امیر قلعه‌نویی: باید چیکار کنیم که کادرفنی تیم ملی تغییر کنه؟ نتیجه افتضاحی بود. آقای قلعه‌نویی نمیتونی تیم رو جمع کنی.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/140495" target="_blank">📅 20:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140494">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=BNwLq3e0uE4t0ajTZ-w9YINi_9ZRRRplWjPE1_EHPY0mbn5atpPvwzi6EZSvJu2-XUfXeeSw4eQo-3c-mV90oUsBwHsfUod3NaSK-1YYTPqNPUcu5q3Krq4Hm7DRYVOScwa9Cj-rTzY41az9jlEs4QnXdnJ7gV018k7PMlOVLGh61fqdPkhOwTnUPI1jbQB4xHHdQLiX-yZmELDrVNY1T1YoGwhZc_6OZeopiq0lP95MOm8HPfBImL4PMOZAhiRjsrZDvUwZ3bclUVebTuduboNFBJtEjGpJlCumqBkf1EPUplKtIJExzn8jJT6tIICcFOhibbJnFFd35Xgggk3pDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=BNwLq3e0uE4t0ajTZ-w9YINi_9ZRRRplWjPE1_EHPY0mbn5atpPvwzi6EZSvJu2-XUfXeeSw4eQo-3c-mV90oUsBwHsfUod3NaSK-1YYTPqNPUcu5q3Krq4Hm7DRYVOScwa9Cj-rTzY41az9jlEs4QnXdnJ7gV018k7PMlOVLGh61fqdPkhOwTnUPI1jbQB4xHHdQLiX-yZmELDrVNY1T1YoGwhZc_6OZeopiq0lP95MOm8HPfBImL4PMOZAhiRjsrZDvUwZ3bclUVebTuduboNFBJtEjGpJlCumqBkf1EPUplKtIJExzn8jJT6tIICcFOhibbJnFFd35Xgggk3pDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
💚
حمله شدید خیابانی به تیم ملی امید و کنایه به قلعه‌نویی: بازیکنان کره‌شمالی نه مدل مو داشتن نه قیافه آنچنانی می‌گرفتن ولی اومدن مارو درب و داغون کردن، بازیکنان ما چی یکیشون 20 میلیارد میگیره یکیشون 800 میلیارد میگیره اما دوهزار بازی نمیکنند و تحقیر میشیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140494" target="_blank">📅 20:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140493">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWbwoDmUvRhpgmGiOMoKrnxqy6tp_s3r5zKT9rmqBV0jvQ00zEMzDBbWTD10IpdiWixns2reiNvd26gz9QqFnupBMeN7clbttm8imUng4U6DxzD1NThsvHP2XKxkyxyarTskauq7NTxljHSQTlRYNitYgo9t5ZmlY1LjJc_LPBM0WMOW4G4BBTX51s55xCo9dQd4aw4lzHuFWiSNXfQB7mXlsVO22_thtBb8FSaU788bT-glhglxbsBOdCg4egDLlA8uwAfRcw99jP8YacKQZScybwYulQ03J5TGDWYwRXS0HQj8W8rY-HfyBCmGGfcvK-MgUZjiS7TppWT5DP7iog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
Netherlands -
🇩🇪
Germany
⏰
Tonight 22:15
🏟
Johan Cruijff Arena
⚽️
آلمان و هلند در شروع لیگ ملت‌های ۲۰۲۶/۲۷؛ دیداری که از نظر آماری کاملاً نزدیک است. هلند در ۱۰ بازی اخیر میانگین ۲.۲ گل زده و ۱.۹ گل خورده داشته، در حالی‌که آلمان ۲.۴ گل زده و فقط ۱.۲ گل خورده است. در تقابل‌های اخیر هم آلمان دست بالاتر را داشته؛ ۳ برد و ۳ تساوی در ۷ رویارویی اخیر و آخرین بازی دو تیم با برتری ۱-۰ آلمان تمام شده است. از نظر روند گلزنی، هر دو تیم پتانسیل بالایی برای گل دارند؛ ضمن اینکه تغییر سرمربی در هر دو تیم، یعنی نخستین بازی رسمی یورگن کلوپ و ژاوی، می‌تواند بازی را از نظر تاکتیکی غیرقابل‌پیش‌بینی‌تر کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140493" target="_blank">📅 20:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140492">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✅
✅
✅
سرگیف، اورونوف، آشورماتوف و ماشاریپوف از لیست ازبکستان خط خوردن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140492" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140491">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
دو گل خوردیم .اونم آقایون شجاع و بیرانوند تقدیم کردن و دوتنه تیم ملی و نابود کردن   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140491" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140490">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⚡️
⚡️
⚡️
عالیشاه از دو سه سال قبل با خانومش هست، مثل کریس و جورجینا و حالا امشب عروسی میکنن، قرار نیست اتفاق خاصی بیفته، عروسی صرفا یه جشنه و قبلا با عقد رسمی شدن!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140490" target="_blank">📅 19:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140489">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
این بازی ساعت 17/30 انجام میشه و بلاخره روی ماه اقای درگاهی رو میبینیم ...ببینیم چه جور بازیکنی هست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SorkhTimes/140489" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140488">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
✅
✅
با اعلام باشگاه دوا یونایتد بانتن اندونزی، اوسمار ویرا هدایت این تیم را برعده گرفت
❌
این تیم فصل گذشته در لیگ اندونزی هفتم شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/140488" target="_blank">📅 16:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140487">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
❌
سعید الهویی : قائدی چون گفت بهترین مربی هایی که باهاشون کرده مجیدی و استراماچونی هستن دعوت نشده تیم ملی
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140487" target="_blank">📅 16:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140486">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">❌
ترکیب ایران مقابل ازبکستان اعلام شد
⏺
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس درگاهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140486" target="_blank">📅 16:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140485">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/140485" target="_blank">📅 16:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140484">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
مهدی ترابی بازیکن32ساله باشگاه تراکتور که دچارپارگی رباط‌صلیبی شد هفته آینده پای مصدومش رو به تیغ جراحان خواهد سپرد و تا اوایل اردیبهشت ماه سال بعد دور از میادین خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140484" target="_blank">📅 16:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140483">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">✔️
✔️
فدراسیون به باشگاه گفته که مدرکتون برای یاسر آسانی کمه و اون مدرک اصلی و قوی که ما میخایم رو ندارید شما ، حالا باشگاه از طریق یکی از ایجنت های ایرانی یاسر آسانی یه مدرک فوق العاده قوی رو کرده که فسخ رسمی این بازیکن با استقلال رو نشون میده و فدراسیون هم…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140483" target="_blank">📅 16:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140482">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
✅
✅
فشار شدید امریکا علیه ایران
✔️
✔️
امارات، ترکمنستان و تاجیکستان ۳ کشور جدیدی هستند که حریم هوایی خودشون رو به روی هواپیماهای ایرانی تحریم کردند !
❌
مکزیک برزیل و بقیه کشور ها هم رسما تحریم کردند   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140482" target="_blank">📅 16:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140481">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❌
❌
❌
گفته میشه عربستان و چند کشور منطقه دنبال فشار به فیفا برای تعلیق فوتبال ایران هستن؛ اتفاقی که می‌تونه باعث حذف تیم ملی از جام ملت‌های آسیا بشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/SorkhTimes/140481" target="_blank">📅 13:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140480">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q7dvT-vy4k6twu7dZGMj6jmlTxeGFw3C2NEjDJiZMh5AJRdEEozQ_rKhD2aUk_kwkONQaPUtkfTjiZkgIqGtBcXVA-9hkkwU33V-IWutWhB7jpxpb050XmPAxTCFENPec1lvf7bbLG23MGBklstwD3Irflag03ng1uu0849AUMW4vDyL9qRyfyuYU9dJ9sqBR6zNfNqpruDjAeIz--rFBmNZNCZBbNRyB7BrJ73Yh0JR2NYXidPMFBZ5DFJBsHZlAxqCfrP8F2IhoBYf8qhAceTWqW5rNf8V1d0Qhc8M1qV5N0jjfyLFIKkGT_OocSHForf8MCf9cPLmewFj5LD2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوری از قدوسی: قربانی به شدت تمایل داره پرسپولیسی بشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140480" target="_blank">📅 13:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140479">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gXAz98MsGlZHoygcE4ILOkao84xlDrgzB_iCI_T1pEgKRNn99KpLbA3YRplc62MjKJ_S5zehaxwKEbL5Rp60LeLhDqz0B1mApJo111b4OnRPmMK0ppGZFbAk7mCzQHmq9-9zTWQuYmDuu0-IzZsKXWWXAUeyN7d3RPQ-xjH9eBz6evYUNXQCjLvq15rdTVsdOHNkWQu2ptUnlmyWXdfp4mAy2TTpY46cQ5Ms46zd3hvYR3vXTzz7SUnVLTRoJiG4TblBAWeDruAJCW7xFDQ5-qi_Lni7OKXRb5UPKIF5_N4SHQcqawoaAZbFm5P5cxFJ6aPgJTM81o8E_Bx8zkj1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
از ریفوی ژاپن تا لیسبون؛ شبِ دوئل‌های حساس
ملی
🔥
⚽️
فوتبال امروز با دیدار ژاپن و اروگوئه شروع می‌شود و در ادامه، ایران وارد یکی از متعادل‌ترین بازی‌های روز مقابل ازبکستان خواهد شد.
هلند با آلمان و صربستان با یونان از دوئل‌هایی هستند که فاصله تیم‌ها در ضرایب هم کاملاً نزدیک است. در سوی دیگر، نروژ مقابل دانمارک و پرتغال مقابل ولز؛ جایی که پرتغال با ضریب ۱.۲۰ واضح‌ترین برتری این جدول را دارد. یک روز پر از بازی‌های نزدیک، ضریب‌های متنوع و چند تقابل که نتیجه‌شان می‌تواند جذاب باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای امشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140479" target="_blank">📅 12:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140478">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
✔️
بیرانوند برای فرار از سربازی، این‌بار به بهانه خالکوبی، دست به دامن کمیسیون اعصاب و روان شده تا شاید با برچسب اختلال روحی، کارت معافیت بگیرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/140478" target="_blank">📅 12:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140477">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
چمن شماره ۳ آزادی به مشکل خورد!
❌
❌
بعد از دو سال تمرین پرسپولیس در این زمین، چمن سفت و نامناسب شده و قراره به‌زودی زیر کشت بره. احتمالاً سرخ‌ها چند ماه آینده تمریناتشون رو در شهید کاظمی و زمین شماره ۲ آزادی برگزار می‌کنن.  «سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140477" target="_blank">📅 12:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140476">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">✅
✅
ورزش سه : زارع امروز جلو ازبکستان فیکسه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140476" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140475">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAQANmsQ27W3jQS4sxTpctjFejXHsdkdXdgPpWbnEtnzXkoqspapHsSNCQr0rEbdq3gQy7s0w9QtMdlniGdgVPwzIyHnlPV6yO0BY8jjKW4Qg7UJNNDAMnTsGbt44LD-_113dYL_mkmiIJRH4Gii_eYyurvl0YDnBJhM4WIdO6bo-Kpzcbs3LPK8h5b4l05lFX0LvukwUQxgMB5yqUTPo8mKGma7GH-7B63yPskfxIDpMs45evWlerhdFDiUY8nV_zFLsPAbRotQCgqhCJa5DeuZ52N-jqmW7dczjyh39-Ck9qttAyX0xbqgR1JLy2kbHplsOU_T1RkFQXFt7Jd9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
| طرفداری:
🔴
⏳
🔄
تارتار اصرار به جذب رزاق‌پور دارد و ولکن این بازیکن نیست
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140475" target="_blank">📅 11:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140474">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
فووووووووری از قدوسی : کمیته انضباطی به باشگاه گفته مدارک شما برای محکوم کردن آسانی کمه و اون چیزی که ما نیاز داریم ندارید.. که یکدفعه باشگاه مدرک جدید و آس رو کرده و فدراسیون آچمز شده و هنگ کرده   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/140474" target="_blank">📅 10:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140473">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
بازگشا، سخنگوی باشگاه پرسپولیس:
✔️
از فدراسیون خواستیم رسیدگی به پرونده آسانی با حضور وکلای ما و آنلاین باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/140473" target="_blank">📅 10:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140472">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140472" target="_blank">📅 10:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140471">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/140471" target="_blank">📅 09:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140470">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj6X8KbQk_EjEESxyqUoHHHaPx4ag8UCezuuUShDxGRf2UJcbOg1WVaQ7UjTJxMhuSrDyIlfzlkmBH4ugXN1oQSK1r-ZuyNKvD_FLHGOjqJ3dqSCaNvmeDn1rymoAi34gkJ_Al_biJIGgQQO62XfPpric5zVPpHr3Q98v0NOj_AeuMZ4WUT48NprP3rCtufwL1mfZW4SLIk4APD0x8fnVhjt9ZEYzdBD2c7xNIaxT6eGo1Tty-kMn58kjyFqeI23dV3QwbHPT764LtYr8tUZAijZS3wO4DiJco3AFd6iwG5XjwmtIJ2P3p27UJQOM4X-Wp4DbUnMcdo4d-euCZs7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140470" target="_blank">📅 09:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140469">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kmp2ePNeAEegUyZZOfxfCwmcCKODtk6vek-oM0KrjRLo6u_oxsgwVF_IkFN3NH7QIVXL7myWdbYzGsIjhY8JovCuXu73H0FoDsbvuhTiKDXAx-ZyyHtxnGXYt6VXNwpoAa-MLc6vc-blts-K9TW2guEuT4a2XKk_pZ7czuGkC0aZN4ukQy-u45j0arlx67fFmyQMxCZ2sa2vx0WDVt81CnNdkiwtpAWiPZTMbX_qHH9tqp-6XZPkKhTW3cymyPsAXmnvrus0wtdJizStLvAsGmmEQH788mGWD7f9xlKQ8SS_iMCZnhPFRMfpQhcMYnpQUY9-shPUrOBbOINV3Igqtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ایران و ازبکستان؛ محک جدی در یک روز دوستانه!
[
ایران
🇮🇷
🆚
🇺🇿
ازبکستان
]
⚽️
ایران و ازبکستان فردا در یک دیدار  دوستانه به مصاف هم می‌روند؛ دیداری که بیشتر از نتیجه، برای محک ترکیب و هماهنگی بازیکنان اهمیت دارد. ایران معمولاً در بازی‌های مستقیم و انتقال سریع خطرناک‌تر است، در حالی که ازبکستان با مالکیت و بازی ترکیبی می‌تواند فشار ایجاد کند. با توجه به ماهیت دوستانه، احتمال چرخش ترکیب و افت‌وخیز ریتم بازی بالاست و آمار نیمه دوم می‌تواند متفاوت باشد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140469" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140468">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
🤩
فرهیختگان:
بزودی قرارداد اوستون اورونوف با پرسپولیس با دستمزد 2.2 میلیون دلاری تمدید خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140468" target="_blank">📅 01:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140467">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omHCJuxjEbwTo3qdgkB7OMvuo3vd2pBFJMetaKilTImpVsNUh_k74WXYezkWIZX_4xPyfg9hVlhHaQkc90rr4SNyRuWUElxHoaFp150As4zAWiCQqUhrZyYve-uQs0807JH_KpC9C1edvX7qfV2sA8HhnZOC90U_Q4oQ62kOPN6ySFwHkB8VwnJuT-8Y1V067_qD9EwwcWFvh1SfiQLxtI40Ne1eMqEJIOSBG6KpzTvNeUggUByOoEzHYvlio3Fjfn4eaO_mzzGiyzsFT7mXOMUyvdGdE1-oS8mnWyMlsJRuEMetIbFALF9udRce-FjNJ_uY8RtERswCRMOp97T-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
❤️
پرسپولیس در نامه‌ای خواستار برگزاری حضوری جلسات پرونده آسانی و ضبط کامل فرآیند رسیدگی شد
‌
📌
باشگاه پرسپولیس در دو مکاتبه رسمی خطاب به رئیس فدراسیون فوتبال و رئیس کمیته استیناف، خواستار برگزاری حضوری جلسات رسیدگی به پرونده شکایت این باشگاه از یاسر آسانی، حضور رسمی نماینده باشگاه و ضبط صوت و تصویر کامل جلسات شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140467" target="_blank">📅 01:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140466">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🤩
👤
🔴
فوتبالی: تارتار بعد از دعوت نشدن کنعانی نگران وضعیت روحی اوست و قصد دارد جلسه‌ای با کاپیتان تیمش در این باره برگزار کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140466" target="_blank">📅 01:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140465">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
⚽
طرفداری: پرسپولیس در آستانه‌ی تیمداری در لیگ دو و شهر مشهد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/140465" target="_blank">📅 23:32 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140464">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQRLvGnfc-pFG7RIo64HcR8XivaSuhRHgLJRMFGeJ6Xtqaok7X6mkdAfy0EA3njmRaaDRv-pYCDAi1QaQbAIHWLXk5VmIxwNTNsn2uU9cyV2-62wcLDkd5vhODI2ofbHyCPMJJpQ4XptGyeozoCzduUYKg3W5klVwNK3cv6FiTfrAHLdw4Nkbm-ZoVE7fDswbDuYCvOAAiohmUMWhgQ-vWk_V0FRG1_KO3MXIQ0ZaXA2_WrNYP1YP0SsaDJC5FMRgU4HFleu0VEm8C6OzwabzsmKq_UMz3Jt_svkk-W4mKfyQJeYdtLz6WrBIO_s0LzQh2j4JTxRsA5OWT6kXVM4Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🇮🇷
سه درخواست رسمی پرسپولیس در پرونده یاسر آسانی
🚫
باشگاه پرسپولیس پس از ثبت لایحه تجدیدنظرخواهی در پرونده یاسر آسانی، طی نامه‌ای رسمی خطاب به مهدی تاج و ارکان قضایی فدراسیون فوتبال، سه درخواست را مطرح کرد.
🚫
این درخواست‌ها شامل برگزاری جلسه استماع با حضور نمایندگان و وکلای باشگاه، ضبط کامل ویدئویی جلسه رسیدگی و فراهم کردن امکان پخش آنلاین آن با هدف افزایش شفافیت و اطلاع‌رسانی عمومی است.
🚫
باشگاه پرسپولیس ابراز امیدواری کرده است این درخواست‌ها با توجه به اهمیت پرونده، مورد توجه مسئولان فدراسیون و ارکان قضایی قرار گیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140464" target="_blank">📅 23:20 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140463">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CogWKZn1F-vz-OX6bFIkc3Xco5oXpuyVeVp9_WgdT62yv-OZKXPb6pWFYCMSV__gECnHvi84L-Uo3AUR45HHVV5Vgm-WPF_yKjUYZsSZ29dB41ccxBmJmZOs6xwOTO_ye8NIU2OuVhlqVBqHbl3ukYJDkz-TeB9sG53QoIzgU02RnqwCh5EIqcu143KF2etLUiEv9uJ2Z6aJlnf0SUJrkYWpme1hRU8gJH7PkCoJ-XcmvbB6U_jj5O70789lb_42FTgi8ZV0cjvUPPGNwbJQWFxCtFot8P4HTNBD1OOyTaQfYaRkQutAfj9wgUSXc0QLtn7XlC4ic74pFxqHjjlI5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سعید آقایی: در پرسپولیس کم بازی کردم اما بیشترین لطف را از هواداران این تیم دیدم آنها را از صمیم قلب دوست دارم
❌
بعد از مصدومیتم در نساجی کلا فراموش شدم تنها دلخوشی‌ام در یک سال اخیر فقط هواداران پرسپولیس بودند که جویای حالم میشدن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/SorkhTimes/140463" target="_blank">📅 22:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140461">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">⭕️
⭕️
⭕️
🚨
🚨
🚨
در پرونده‌ی آسانی، پرسپولیس در استیناف پیروز میشه/قدوسی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/SorkhTimes/140461" target="_blank">📅 22:19 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140460">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASozxpkCswKkGzSU63x4hLh01WNCP1zJX-iEHI5c7yGQRgDIkaeLIOoWAiXBxQI30qPvihq0nOackFN3fIfIiAj465zKfrCE5y20RUwE8DLlIdp7eVwYucWRQSRT10PpIBfbhrgFv1pn_z60IP-aFRckMCnfyAKyKWwz_Re9V-yzOctzS-hEZwjxRjqoGnjHhbwWwfCW-IjaS-FkzO13tKRQei2BoK9cyTibtSfAskOI_G2yZoQpG3lp9yB08Cj5dMzrcDHaKmrPr8qTV5wtYPUqT0tiufNmT5sUEFyfFJnP07c99gig1tpahgBAiSpdTvirvc5PFSzeB2uolzlvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
✔️
حسین عبدی: مقصر اصلی شکست من هستم، اما بچه ها با توان فردی خودشان فاصله داشتند از مردم ایران عذرخواهی می‌کنم
✔️
✔️
باید به کره شمالی تبریک گفت؛ آنها خیلی خوب بازی کردند. باعث تأسف است که در این گروه سخت نتوانستیم پیروز شویم و به مرحله بعد صعود کنیم.ما…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/140460" target="_blank">📅 22:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140459">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
ویدیوی‌کامل سخنرانی فوق العاده و طوفانی پزشکیان در سازمان‌ملل  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/SorkhTimes/140459" target="_blank">📅 22:06 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140458">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
حسین عبدی: از مردم ایران عذرخواهی می‌کنم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/140458" target="_blank">📅 22:04 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140457">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏅
🏅
پرسپولیس مدارک جدیدی رو به کمیته استیناف برای 3_0 شدن بازی دربی ارائه داده
⚪️
حتی اگه رای استیناف به سود آسانی باشه پرسپولیس تمام این مدارک رو به CAS میبره
✍️
همشهری  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140457" target="_blank">📅 21:10 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140456">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbEKOj0KTVfswbjS39LnC9aByH-zjfLO0tcOqqkJAvNuMxNE_NVaCLOAAMqcjuxbwaASIUbHrQScLeYnFGZ-cNNvQavBA7P4P7xnw4YnFlfDP2Mm58R-woUNR4kHB69rAbRgSFeoEdgeXdmZwNBiTPY8eGTfTYqLh8LHIHF2UNIHHzTVLAWEnqnCq60E_Q8K69EXCmnjSk101iFqHd9KOBTtWEL3RZ_3nJTDy6QVVypRGB4nijg28Tw4_DG0-Ra68l0cAysdtY8uAW7O3iq452Xx8loDLbRL4PtJEuS2ot5UirIyLftTl9TWVtcbMfRniBoCnt7-tBiXg7ruV7IhBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ایتالیا مقابل فنلاند در یورو والی؛ جایی برای غافلگیری نیست!
🏐
ایتالیا در این مرحله با ۶ برد متوالی وارد یک‌چهارم نهایی شده و در مرحله قبل دانمارک را ۳-۰ شکست داده؛ فنلاند هم بعد از یک بازی سنگین ۳-۲ مقابل یونان صعود کرده است.
ایتالیا با سرویس، دفاع روی تور و تنوع حمله دست بالاتر را دارد و روند ۶ برد پیاپی هم نشان‌دهنده ثبات بالای تیم است. فنلاند در بازی با یونان توانست در لحظات حساس برگردد، اما فشار حملات ایتالیا آزمون سخت‌تری برای دریافت اول این تیم خواهد بود. با توجه به اختلاف کیفیت و فرم دو تیم، ایتالیا شانس بیشتری برای کنترل مسابقه و برد ۳-۰ یا ۳-۱ دارد.
🏐
اوج هیجان همراه با اسپورت‌نود، پنجشنبه ساعت ۲۲:۳۵ دوتیم ایتالیا
🇮🇹
-
🇫🇮
فنلاند به مصاف یکدیگر می‌روند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/140456" target="_blank">📅 20:15 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140455">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
#تسنیم؛ بیرانوندیه پرونده تو کمیسیون پزشکی ایجاد کرده و گفته من چون خالکوبی زدم مشکل اعصاب و روان دارم و باید معاف شم
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140455" target="_blank">📅 18:57 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-140454">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6eVFlbKKJicNVxYNLy9pH63G4uJvAIPw-u6EvIaWw4gtCm3MA02vXKzcskJOlmHoTjvP_4u76ZQN5PfJRi5v9xt8cykB_uj3tS15aBCLxxodgFkK9qJle4gbEztixThqqFy7mDgReXAhGm9bYBdruKPYtBToPv5CFuu21gxBhtr7yW_z2JKycpHhFehZ7RuwI2Ty8AqxmbXE3wip1f2MK_CyA1XtqijwbvhpEtkUjTQeheEzx_gskZCJBY4sU9ICZ2tezrb0_riRRaQ5oic--C473KmCxMIOX8G4fkqjgPKBMZCcZQVvQk1-Y4Aq4l9GXuiTFCqiZrT3cNeDsNtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
⚪️
رنگ پیراهن دو تیم ایران و ازبکستان برای دیدار دوستانه مشخص شد و ایران قرمز میپوشه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/140454" target="_blank">📅 18:56 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
