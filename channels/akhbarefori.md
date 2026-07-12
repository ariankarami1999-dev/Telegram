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
<img src="https://cdn4.telesco.pe/file/q7btbIWmJNxPbtsN00J1Zi4cY88SLk0JgU9gtsLuXRYDwwFk70wZuIGYEgyrpU9vpA_FCzMyi9qCVlXIHJzuKj8hTg9qZR4FkvR4maYaRdBEZQnbRtA9arG80gXUDj53vasPCUtLUU2ApBzXfnYvH9AyMUKaikeGFwyIFB2lv1QAMmC_23flN-xjvYaExg9ASNsThwCVom0bY8xChVdNU31d9HoMdM3jme67LFfYwphT3CV6iUFqYlSleg9wSCiWJ0o4uAw8WN2Gv7Uz4BBYSPkRwV7tSqRNxeebqHurVgkBwJqNrbatu-Griaygm7jH-CqdCQ6JQ4vPSfphSWhVUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.4M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 02:44:12</div>
<hr>

<div class="tg-post" id="msg-670377">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tfJdy6UBlC2p880OTPKSNLGlT5rpH2uzipif3k_ShMiwKP-dGDLHI0QVi2kQ_XWrYAye_diwHOrQ_MoviO2h9AgvHRWM0EEN15AcEMSIgkE7C7lmTbNZxXBFEAk7g-rtGavdrm9R5sLJ3pn-w9bLMvP_63lGGxb8r263GGExNqgI5Kq-0hwShi9RqfItJwHY-c8v_E5WwTWUlDO8NxK-b2myiJBFKL8xt26jrNKdE6ETFTXftNS7OcVlOEPNBKB0e8XtRLumyahgX4kSwULcpFle_5UTc-Bxt-aXuYhyBxaB8K-MT_rhtUArPwLU-Cb2swtQfX3Qlkjk1Jlh0xWb4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همزمان با شدت‌گرفتن درگیری‌ها، قیمت نفت برنت به ۷۳.۶۹ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/670377" target="_blank">📅 02:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670376">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
نقاطی در آبادان و اطراف شادگان مورد اصابت پرتابۀ دشمن قرار گرفت
معاون استانداری خوزستان:
🔹
در ساعت ۲ و ۲۰ دقیقه بامداد امروز نقاطی در شهرستان‌های آبادان و شادگان مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/akhbarefori/670376" target="_blank">📅 02:40 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670375">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
معاون استاندار خوزستان هرگونه اصابت به فرودگاه اهواز را رد کرد
حیاتی:
🔹
دو نطقه مورد اصابت اطراف محدوده شهر بوده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/akhbarefori/670375" target="_blank">📅 02:21 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670374">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت  حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در…</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/akhbarefori/670374" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670373">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
برخی منابع خبری مدعی شدند، برخی از موشک‌های آمریکایی از کویت به سمت ایران شلیک شدند
🔹
طبق این گزارشها، موشک‌های آمریکایی از کویت شلیک می‌شوند، وارد حریم هوایی عراق می‌شوند و به سمت ایران حرکت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/670373" target="_blank">📅 02:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670372">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ایرنا: شنیده شدن چندین صدای انفجار در قشم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/670372" target="_blank">📅 02:08 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670371">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
چهار نقطه در امیدیه و ماهشهر مورد تهاجم هوایی دشمنان آمریکایی قرار گرفت
حیاتی معاون استاندار خوزستان:
🔹
در ساعت یک و ۴۵ دقیقه بامداد امروز دوشنبه ۲۲ تیرماه ۴ نقطه در شهرستان های امیدیه و ماهشهر مورد اصایت پرتابه های دشمن قرار گرفت.
🔹
دستگاه های مربوطه در حال ارزیابی خسارات احتمالی هستند که گزارش های تکمیلی متعاقبا اعلام خواهد شد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/670371" target="_blank">📅 02:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670370">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/670370" target="_blank">📅 02:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670369">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
مهر: معاون استاندار مرکزی حمله دشمن به مناطقی خارج از شهر خنداب را تایید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/670369" target="_blank">📅 01:56 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670368">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
معاون امنیتی و انتظامی استاندار خوزستان: در ساعت یک و ۳۵ دقیقه بامداد امروز دوشنبه دو نقطه در اطراف اهواز مورد تهاجم پرتابه های دشمن آمریکایی قرار گرفت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/670368" target="_blank">📅 01:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670367">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
فاجعه در بانکوک؛ ۲۷ کشته در آتش‌سوزی یک رستوران
🔹
شعله‌های آتش نیمه‌شب، یک رستوران شلوغ در بانکوک را به صحنه‌ای از وحشت تبدیل کرد. در حالی که مردم برای نجات جان خود فرار می‌کردند، آمار قربانیان لحظه‌به‌لحظه افزایش یافت و علت این حادثه همچنان در هاله‌ای از ابهام قرار دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/670367" target="_blank">📅 01:48 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670366">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
مهر: ساعت ۱:۳۰ بامداد امروز دوشنبه صدای دو انفجار شدید در اهواز و ماهشهر به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/670366" target="_blank">📅 01:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670365">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
حمله دوباره آمریکا به دکل مخابرات اطراف روستای طاهرویی سیریک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/670365" target="_blank">📅 01:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670363">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nCRrqA5XMyexG-7G4AEK4J4gJ3yNasWXkGIKNS18HODwrCiylegrb4BtPfmEoR_BcW28IAEO4qHJ84P7ywn_LP2qVZCp7JlASUWIQonxoWHalyNv8Ez1UNgZll-Pddfged4ZBbd1ROVZd5aLE5JQuws__EU43o-RklrvGnjAjXJxYrIp1BlcJMMeriisaawavVvD8Tv0izhxE8pR1-CMOWvY6u70nDRa2IhYmcwP-vDRq-rXt_frot9HMv_Qk6hmmI9ayJa1HfMSS8QSfvFbYmrcAKA0FHbFlY0leNcUt8oNgl7pPxYPkEI60gs4E0LbZgTnRvZviU_27T1-bEv03w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pz4X81mvX7gNB43Y0zJ_eUUEO0cxfAkHxFjMBU35IZIjPy-UCJ_Sicbo3mSiJ7kYcou4tsjh5oPMjc3cW8cdKYkvxqLwNfpxa7FbyqYcC4h7E_xZnfhNoLtBmCS4uI_9MAyPGnhVIYacPzbrxrAgVZ6VR4QP8_EqjAQW4xtpt3V0mZKhYBgRCg--UG0GgRaIyDT9GstBB6y57N-f8M2FjISn0KyTEwyd0_pvOoFXQpR3wXx2CWvGR_9ZwQ8LcGYM661IVdVp9xPH_GhJbB0eKRtMscEfdOM5jxyFGT63QoX-jR33LsTunSREHTwmEaXM7Q-DVWGQZQuHQSQZPotoJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصویری
کم‌تر دیده‌شده از لحظه ورود پیکر رهبر شهید انقلاب به کنار ضریح مطهر حرم مطهر سیدالشهدا علیه‌السلام در کربلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/670363" target="_blank">📅 01:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670362">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-3wxMDooGvLRi12ZLIkCGz5zuvwGMkHtN2bVuzLYUQdGK5vI_1hAEcJqqqYf86HgaCSqizPJ-ktxke1oQO7pGZe6FdTz21jucT4L-M-bPLrnTT2mUlAhMC3gTLNjqlcUR-LpDXQZFg1UfmxOZsiofPsm4xj5iavRm3Tl_iAxwd7qXMulgE7YCUX09HdpisYdKJTSrU19cJlt7u-LeUUKkdECDcjBPe16tQ9-btBJ6bzNsjmDySoPoHdaTUwxJy5L67hUMqz7GJATRbbpcStMWENXyRPFRd2awVZNuxAP4Z7qZrUhS1F7DO0uKt6c9YguhDNcj_AXwRh3ZbEcUMcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیت‌الله اراکی: ریختن خون ترامپ و نتانیاهو و شرکای آن‌ها «واجب» است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/670362" target="_blank">📅 01:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670361">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ah3hfvglhfzYNW4RrpZdNjV8CzHrJE5PAneXhU4-yHK3hOtzFvZ8dmTHvbucp0GmIy4phuM2Qn_5lao7MtBfelj3bPREAXCd61Cj2IGGLA0He1BDHu-SS2yxiWuqQY2QqJ8KYtUjI2qInWBrBuKtk21kjx0c3vmL7H7i0ZPfMepj_QaN8SX8npi_uj87dMk0y9e4yIwzKr0e1SEbUv60Yx1baCU7LptV_GF0v2qT8r9e1mANbWgSYhC3sFFDSCItrQw41qAKNfxKewNO-OPZC3N2pLlEcZsStWV8V6AwGcnHW3VBDJHYWL1faevs5LLd57kkm2ehDg2xDpcnkFIHrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار نفت با افزایش قیمت شروع کرد
🔹
نفت با ۷۸ دلار بازگشایی شد که رشد ۲.۵ درصدی را نشان می‌دهد و در ادامه رشد آن به ۳.۵ درصد هم رسیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/670361" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670360">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
سخنگوی فرماندهی مرکزی ایالات متحده در گفتگو با سی ان ان مدعی شده که سپاه پاسداران انقلاب اسلامی ایران به تازگی به سوی شناورهای در حال عبور از تنگه هرمز آتش گشود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/670360" target="_blank">📅 01:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670359">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
برخلاف ادعاهای مطرح شده در فضای مجازی مبنی بر تهاجم دشمن به اهدافی در این استان، تا این لحظه اصابت در مرکز استان از سوی فرماندار شهرستان بوشهر و نیز در کنگان توسط منابع محلی تایید نشده است
./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/670359" target="_blank">📅 01:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670358">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
پرس‌تی‌وی: صدای انفجار در کنگان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/670358" target="_blank">📅 01:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670357">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در جنوب شرق کشور؛ جزئیات رسمی در انتظار اعلام مراجع مسئول
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/670357" target="_blank">📅 01:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670356">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670356" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670355">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
رسانه‌های پاکستانی از چند انفجار در چابهار نوشتند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670355" target="_blank">📅 01:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670354">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
مهر: گزارش‌های اولیه از شنیده‌شدن صداهای انفجار در برخی نقاط استان بوشهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670354" target="_blank">📅 01:13 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670353">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/670353" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670353" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670352">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">علی فانی</div>
</div>
<a href="https://t.me/akhbarefori/670352" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670352" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670351">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A3SUUMfTS1B5KhgLSunq_WKKUxphJa_JNzYB2OnCDBIrIBKpHwMkpEQxNf-KEHZLDI8VPVNmDsb81xdpCVwrLFYdBqbwetGhGDYRqwl6oupPhsqh8AAHyeEm3dXg6Io0J2JRbidoP0hzotURpLoXfmDUTuKT8VtlFmGeLp9YUt0IOmM7xsYp2jn6ZYlz9r_DmV9Y-ilU-s6_GWSd0T3HUP8pR1f497S2VvcfPrJdYqi5SceM5LO4OqzqgAYL-Y44L-CHCvPcyPlg6uhQIeVpPOQTFEs3yabiXD359IKER-wf0dfP3A-pnb_Fvvjc5rb5zzWowIz31RmuiQ8AeEKvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
به تو از دور سلام
چله زیارت عاشورا تا اربعین حسینی
#روز_هفدهم
▫️
امروز با خواندن زیارت عاشورا به نیت شهید دکتر مصباح الهدی باقری کنی  ، دل‌هایمان را به سوی امام حسین (ع) میبریم. امیدواریم که ایشان ما را پیش اربابمان شفاعت کنند
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/670351" target="_blank">📅 01:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670350">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/670350" target="_blank">📅 01:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670349">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
استانداری هرمزگان: در حملات جدید آمریکا به برخی نقاط استان هنوز مصدومی غیر نظامی یا خسارت به زیر ساختهای مسکونی و تجاری  گزارش نشده است/مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670349" target="_blank">📅 01:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670348">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svJAYS4RNua-vYBn_a1Stb2gNrAo4IS-w5RH5RQorUJh2tKJs8MUbu07B6l22di0t2_yGnqNLGEPbLgDIGZw0R1poIYWqkx2W2bnxFtSMwnegfwVcmb0T0qu7d2P2Teu33Hsgwa2CQyf0_DC9-y8HYRnJdfXPXpP8wfhNCBqxeXErlTnjhiICvmUEe0a33ErBmchKrIq1FKrFapiwtFFb44Gyh35YMP_BkyJEdC9HPO6bKPsaTZYfTGQWA2fmfAV2RqKUIX2cge_bDbZ09i_icFGwtk7Ii2zbp0VylaLQbvHEV-LZGEBtmRhJt9gcx7-Yh-Fw-CNaQxvpXe709TbaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه حملاتی که تاکنون علیه ایران انجام شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670348" target="_blank">📅 01:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670347">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONn5CTW5TE9wDf_OO3L0o6c13sAzkE8UIGncmJSA6CeE9JqceE_VZwWUsfxMVtDgeJJqAuTriCemsp9m6mFb8lF08EiX7M_KVkJg7yDQI13OIfpPFfa-0WFLS0PKHzWTUp5mT35IEOxARi5l703_QG1mBw45L-vJcHUwqKA7s2RbVurBA4r5iTUohrDHRWb17rDjDasOTsoqUMe1DCwRNCLIG-iqbqlvNe4jmyAnsp4Y_daPfi5ukDdOjqjkeTLcEaZQn9u6Ef86z1YzLsYmb1yl85kgs58H69U2MQGR2zL7x1NSimqT1u9bi-IhCkpLgv6igqgOrfzSv_5l5dwOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670347" target="_blank">📅 01:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670346">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjNxCx8zRjtVB2lvJ1FDk1km0DFSciCKl9ad0RortXTAZ2htFAX0HgPl45iZDAHAQZvFCC4Ww47E0OSp09HvqopcxgQfFjJ5TKoBiITF_oPk120MgfAePOAa66pEfH_YK9ugj4Xt1uFiuKGVod4Gu8oVu3fxFrelLrMsA2Q76HmHYLqu9-tF3p90bfY4Kk7CEsJc4Bu2f1FpnFWp8iiQQioRlPmfborT7JyxTws4PqZlGHuJVRcYBTV5Agc3oq8bJPiF4HXUPCLHdnqh70_uktBk-FSUDsEOP9k84tJdfGMVFfteg-nfXwN93VlAUuSKfHFmdasxsNEgc5qBQoVAUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زینب سلیمانی: مرگ راحت برایتان آرزو خواهد شد
🔹
زینب سلیمانی در پیامی در صفحه شخصی خود با تأکید بر حتمی بودن انتقام نوشت: خواب راحت از چشمان‌تان رخت برمی‌بندد و مرگ راحت برای‌تان آرزو خواهد شد. این پیش‌بینی تحقق یک وعده صادق است؛ به اذن‌الله.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670346" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670345">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
پزشکی قانونی واشینگتن علت مرگ لیندزی گراهام را پارگی آئورت اعلام کرد
🔹
بررسی‌های اولیه دفتر پزشکی قانونی واشینگتن نشان می‌دهد که سناتور لیندزی گراهام (جمهوری‌خواه از کارولینای جنوبی) بر اثر پارگی آئورت ناشی از بیماری قلبی-عروقی آرتریواسکلروتیک (سخت و باریک شدن شریان‌ها) درگذشته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670345" target="_blank">📅 00:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670344">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Shabaye Jang</div>
  <div class="tg-doc-extra">Reza Sharifi</div>
</div>
<a href="https://t.me/akhbarefori/670344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
بین بردگی و جنگ
انتخاب من تفنگ
🎼
شبای جنگ
🎙
رضا شریفی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/670344" target="_blank">📅 00:57 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670343">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8dW5Qx5xnf1MJS4BcpHxZTv9BRdqC2TcdM5vOohHKNwkmj7UUZYtDu9ZNbN-tsr1SBxrZXbpwOvJotGmtiyUH-Jf8ei4RM1Ba7ridyrdDHMfGNq8NENcYzZqPlMpSjHAL5p45cN4xi8svkmTsQ4EQUKbmqHcsDjjNYyxqlgdFiNIoACHMWs1I9iFKczyJ9s67EqDl3q2FIA9yD6lEIw5Epq2TxX-F3_XODc7aklqv5mDDuBZtnBL2qxh-sw9BIiwnwCJiacpk7mcYrocpiMgwOHed9j5yX3z2VrsAGamUt3WDcAKrSVyi4tXFpIkEoRlMlM5vVZNmunMSC0hTC9JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سنتکام از حمله ارتش آمریکا به خاک ایران خبر داد
فرماندهی مرکزی ایالات متحده:
🔹
ما حملات بیشتری را علیه ایران آغاز کرده‌ایم تا به تضعیف توانایی آن در حمله به کشتی‌های تجاری در تنگه هرمز ادامه دهیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/670343" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670342">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/670342" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670341">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFc1ZaS6DuUoFV9oukxafdZrodU-2X4Z4OYswJs5sfnBp3IEcbDW40cWSTe8V4Y_m0sEEGSaLYqrfJ7aU9tDSFe1YQWQx_4TY1u6tIfTvimDE8lUXxPbbSVEEdDAtBHwQedOZm_dBEYPUBRXPNjNjffWbJG-IXARKVk_THCLt25ap9sv_HT6D2ikcO656J4agtNMMlwzWSwgJpcNkM-PR2DlZOadDYbxl1iB-kTko-B2zRllFI4AelVG85TC0jHWJF2guxNITQo4JFGnU_Bx815_c6_tB7Zx3qn9w0TvpCh5V6oFN0LDfJNEcexJ3IS9M_3QGOm1Rm_XBsWBGLQawg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تاکید غریب آبادی بر تعیین واکنش به هر سوقصدی علیه رهبری و دیگر مقامات از سوی شعام و مجلس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/670341" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670340">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
صداوسیما: صدای سه انفجار در جاسک شنیده شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/670340" target="_blank">📅 00:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670339">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/670339" target="_blank">📅 00:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670338">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJ-lD-5DyiK2QF1pQvTcI_2UmfXyv8GbiAbjhGNHo_GrE5qjDTF4jOTWS-I2JgiHN6ZPTKyOA33W8T1lbbAZMdtS3Tk8hctuppZv8xdm9gtXl_aevm5hk1YK7p4BKg1HSr5gX4pt7iIXTFrlJRpppY4RnItEpBUujv66rvazeYoxjEV3utJkoIJDkyJ5CY0z0dCpr_HSHlBgejzNubuBjuc0OnUEkrGEMyrQBIamy-t45q9VvR9tXKgtFiP6vNwoU5XKvNSDOenzQ4d7qykyEItIs1OjLqiSeDNV6ZEEdf6NYak3Yk2XvCGxyD28csD2hYBcqm6PjLo42c7ZcA4aTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره تجاوز نظامی آمریکا علیه ایران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/670338" target="_blank">📅 00:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670337">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
صدای ۶ انفجار در اطراف روستای طاهرویی سیریک (هرمزگان ) /باشگاه خبرنگاران
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/670337" target="_blank">📅 00:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670336">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
منابع اطلاعاتی آمریکایی مدعی شدند: آمادگی‌هایی از سوی ایران برای انجام یک حمله گسترده علیه امارات و کویت مشاهده شده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/670336" target="_blank">📅 00:31 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670335">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6800058819.mp4?token=pSGn8hBdeOo9Ai56JXJOQeDeln7sfdO0HvQJfE3cHuIkcKUlmc7RS-BxCab0kb6Zhe6QxTnKPjVrwJPuY0Rafwi6q-kcdKBNzfkMvv6EFH0Do5e6-TYqJdXbU6tyHkYY3EhAxwmCAoWt1X9E-KmoiKJGQc2-iB0hSDKqc0Y0L2E2CcfD9tYMPclRuvx29zem3AqAdvhcXISiFFhhHQGNE_F57lrM8NIrgPU_jozbOrf76R0ge8qcvYt2LyBlmhdCfm9rohIE_EeLs7ebJm8AKum0Vl41a6tP4x_HD6KEaFCyU6cyCIUZEmdaXSnWKqAI07CMw3-3gta5Fd8ma3s_NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6800058819.mp4?token=pSGn8hBdeOo9Ai56JXJOQeDeln7sfdO0HvQJfE3cHuIkcKUlmc7RS-BxCab0kb6Zhe6QxTnKPjVrwJPuY0Rafwi6q-kcdKBNzfkMvv6EFH0Do5e6-TYqJdXbU6tyHkYY3EhAxwmCAoWt1X9E-KmoiKJGQc2-iB0hSDKqc0Y0L2E2CcfD9tYMPclRuvx29zem3AqAdvhcXISiFFhhHQGNE_F57lrM8NIrgPU_jozbOrf76R0ge8qcvYt2LyBlmhdCfm9rohIE_EeLs7ebJm8AKum0Vl41a6tP4x_HD6KEaFCyU6cyCIUZEmdaXSnWKqAI07CMw3-3gta5Fd8ma3s_NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقت راننده پیک در پرتاب روزنامه در هند به سرعت وایرال شده است: او می‌تواند برنده المپیک شود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/670335" target="_blank">📅 00:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670334">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
هلاکت ۳ نظامی آمریکایی در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این سه نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات، زخمی شده‌اند.
🔹
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/670334" target="_blank">📅 00:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670333">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yc2i07eMcSiLqDnpnTQk7-sEMCNQc1nng8SXZLRBnWO2yN_JK1b_BMPyzag7dYCUp-U02ipzg363HN20JlAGMe2yYrHIrALoJ5-T7NaL2fjc2urjO6firBDOBWInuXboC9Mq5M0wuNR39dG_-ec5Y7dbFnWL5u26bRqU7UBlIbPF-U8rbAnWIkzucJsO1El7xdJ-lJxaDnD_oR0pswcdtanEoysTCEuD6XQL2oxBecrPamOtb4uXfvvrr7tiMsWn7uYOtY2Y9Mx9txI8c2P6HTsE5OErcNq2PYxHyplGAKHxEm39ApX06Ocho5dijwcC78AA9-8u3fK3jis9Lb6AxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناسا دنبال داوطلب‌هایی می‌گرده که یک سال در انزوای کامل، در محیط شبیه‌سازی‌شده مریخ زندگی کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/670333" target="_blank">📅 00:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670332">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: شماتت کردن ایران به‌خاطر دفاع از خود در برابر تجاوز، غیرمسئولانه و ناروا است
🔹
این وضعیت، «برخورد نظامی» نيست بلکه ادامه تجاوز آشکار نظامی است که از ۲۸ فوریه توسط آمریکا و رژیم صهیونیستی علیه ایران آغاز گردید.
🔹
ایران به جایی حمله نکرده است؛ ضربات ایران علیه پایگاه‌ها و دارایی‌های نظامی متعلق به آمریکا، مستقر در کرانه جنوبی خلیج فارس، اعمال حق ذاتی دفاع مشروع طبق حقوق بین‌الملل است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/670332" target="_blank">📅 00:16 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670331">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/phIkcitfKGxS_KPMYf2ZeecnL2Xt64rkOYHJ0YQfkVWI4x4PvXVKhXnN2QIEyWgySbkSIDoZciT5jiX8EktTM5Vge7YDZEU9If8jsXfkAxkAHzs14CkqhjqGT14pV3MnFyKze7VE6YeMeCvRh_ByX4QAtsq2l_rF1o1WT7LOxXK8qdge2mX0oe4kcVN2qoZihE3f4AHmk_-q4BsxkC_i2rfUrhoILudC01437zEJ2dhMpBzkTMUWVMmuo4yaTO5qoUJbw0VFpFvLhbF5gNa0Yw4Oup4lsi0ttfjEmSnUA4Jn2E46OIrho8UDhhBpKb7rjF1lzHHEcG9oL2ua3csyGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آرزوی خواب راحت و مرگ طبیعی در بستر را به گور خواهید برد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670331" target="_blank">📅 00:11 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670330">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
وزیر امور خارجه عربستان سعودی با همتایان خود در قطر، بحرین، عمان و اردن درباره آخرین تحولات اوضاع منطقه گفت‌وگو کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/670330" target="_blank">📅 00:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670329">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx93LoAQijaEcXjukECts6fkW84vVLAaj0QzFf0JNg3R5payyR0zoVjPJQQJ_sZ6p-yG-Z6omEmbTluBEnD-93Tjlz8oVLLZNNqVjerHIPOCbkIm8dM0MoFYiYczk-q-ft1V0qaSssxE8tDO4908a8UUfq8UfM5N_jPLgSIHYMcgBeJsp2ANONcNnytr961T5NTodrNdF4ofz7YrwSQI00if697mgh4yQxW5DYQtOHFsUnc5ARbxF2Jcs3F8QpYpNU9-sIRqk3h6lZyJPLJ-Cx-C61tp0G60LZAwQa39cvOwfPcTxbr228b48ZOxOqCH06AYWnrWUYLnimeljCdO2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اوکراین پهپادهایی را به کریمه و غرب روسیه پرتاب کرده است
🔹
منابع نظارتی حاکی از آن است که تاکنون ۴۵۰ پهپاد پرتاب شده است.‌‌
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/670329" target="_blank">📅 00:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670328">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fN7npBPeS3HTB1IrgMGhBeH_sEysV7Xf6iS3mlLwuMmiwJsbNH7uu-UrL1TbLeiFvOndd6Aryq3lDTg08i2vyAIXEKGvX8ueTkLyTeLT4SaOVGBoTXq89GBeQ9Vlb_7EPumW_aMXBRH2ucDAB4RELvLkscU4sTGhcTqSKhO4P2BMBnD8HwVfpYb6uSgtBOOKKXq6cLxzsn1WtDSdLXkm5WpjiuLRLSVRRLYNzFFkbUDLBQg9CqnaWNRgUMyaWF08EHivLDLo99z0Kck_x1dNsQMHXoZ6GAUPgHbM8nqSaekl7UqDbwGL8wE_L584t8onzGsJAgUXx9uhkU3smHi-LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/670328" target="_blank">📅 00:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670327">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
باغی که سنگ‌هایش موسیقی می‌نوازند
🔹
باغ صدا، موزه‌ای روباز در شهر سن اسپراته ایتالیاست که «پینوچو شیولا» با تراش سنگ‌های عظیم، آن‌ها را به سازهایی طبیعی تبدیل کرده است؛ کافی است دست بر سنگ‌ها بکشید تا صدای موسیقی از دل آن‌ها برخیزد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/670327" target="_blank">📅 23:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670326">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
نیروهای نظامی ایران با هشداری از شهروندان کشورهای امارات، بحرین و کویت خواستند از مراکز نظامی دوری کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670326" target="_blank">📅 23:44 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670324">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RCRLUpSTxQm7NjDrF81yt-VV9mGZ3O1YEIZLRVUKuhyca1vY_n-NuR_gfOqB4-fUwxlow28oYIMALgJ0tEJ5vwykVXtxyjrk2Z4CRMlz4qjPi2cjxWUHNuClyZTwidSlVMD9ApxKQYnJAgLPUeYFddlsLlLh0BSMS8I-47t5Etz7I6VZD7yAsEmm2nNaHypdAfDLmxtFCZJ8OhqoPUhgBLYwvsw5pMnne_rg_nec-Qsib3TorHCoqNddixJIYveD0hH6mgfnfpoNyls0F8di9_aKpu-8PxVlD3pYTiNm6aNAhmBqJ1Ya-6oq0uOJl6Ihk10VR3UF4AXn0wWJhZ9wpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sU536tVcl7YZKPqe81rd30fMTn2BYMGKgTAc1eYF61sQ2KsdMv9kOap8JbM98JLLgnhr1QZmU_HjyayaWSrgNYHCd0nioRpsUbO6JVyIeZcXbo7fD1K5ZkDDYoWVr-IaAa1kHUcIKfllVr-gB-M4z-yjiKZy9P8I5ch6oU_g2rMs5tS7VHGMmx-7uhAw3A15hCmI2pbQLDhVn0TYxTEaAb4LhKXCQg9Jn70_bwAda7yNLGtd5OXb627Rujo_9fUBYah07OFQW3T7-225ML6fcXRuNx07wj5yN97PEQdUfFRE5WLfqf5937RLf-TSkkvPBDnlN9_biikWg86sFklSrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو پست جدید دیگر خوک هار که دقایقی پیش منتشر کرد
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/670324" target="_blank">📅 23:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670323">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnt77Pqz1EJZVde0w_yCLLpBAnT3wgfpfn7t3c9MQL24IdzKP2HKWU1tKJd42RsYYQt_8fFKtPa8ywkrmLKWcsDmjh8Y4AVDG82LHNJXW_mSFtLJP95v71i-hLjVwJpNczLVhW30mNk-dNyQJ55LcrGOLqYWNOnNc1UE04B1RN0g-OoLJfGq1r679bOxaT9_54p0BZyJzlQC7vWtzXH7kmAAOWdCJBFg34JQ4L2ZKXgIYzzg8hFoCnE85-mcUwX8fxZ4NsP2hMneHUy43zCGWAH0t97iAT0hB15qi9CyCLFf2lQLcLksOTmD4bfyfh9ozgV0Ow3N1KFpI7zaYoVGVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توئیت جدید خوک زرد: من به ترامپ باختم!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670323" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670322">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5422faa93.mp4?token=MeVdX3n1yIKWEFTfL7eM20SZqeg6PEj43Ky2iKjLfqcC-rgx6a85DL1Hmy15mFTCUY7Erz_yLW41rAz_JI6NKItzJvGMx3JwyJkVQLXpc3yjDy1icEnBaSPl869mLlv2q_ntHJWLHdkSGogmwmWInrqxny7TxGy6buRCHxT9hPlTnW47ZkJrfQMs4Gpb5vDEY0OTOB1MJZDE8nrpIvIyXaTCKEOONPU2wDSlg8doChLJcTyLpmyMY_TYSPJrUOQ584JYWFBAa9w-lKg8KPfOMrvOq28LriMYZ6MeVwpbJXpAkMdTqgXhNmgOr-hwf41QLfNV-bjVULQnyAglUci32m0RyXHOy8mzWos8bs4N-IR9CSw95BrLEQyZ71qPm3MtLvPnn_3wUxeBueNb22y4aaIBt6C8jozZzp0idkAzEtraaRvQREu0BaDBfhkAqRqo9s5ZNStvHxM4P_OXXCBfYnm8pyudM88POoCDGdYnAEmQvFQ8iLILUq5bL2lWe0jU6b4ZiLL47TiUxYndh51P-wxnJmL0TKlafQFjY1var2lEApmE9A1smx9j_TkcIFDkSQ4U7NTBebEO22CRN6dIO-spcpgpIw6_tqa3qsoHLNeptDrEPbgodtU6WlgNMcb0wTa376QfnZYjtJ6Y3CrV1QMme6l-e9B3bQEnbwMtR64" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5422faa93.mp4?token=MeVdX3n1yIKWEFTfL7eM20SZqeg6PEj43Ky2iKjLfqcC-rgx6a85DL1Hmy15mFTCUY7Erz_yLW41rAz_JI6NKItzJvGMx3JwyJkVQLXpc3yjDy1icEnBaSPl869mLlv2q_ntHJWLHdkSGogmwmWInrqxny7TxGy6buRCHxT9hPlTnW47ZkJrfQMs4Gpb5vDEY0OTOB1MJZDE8nrpIvIyXaTCKEOONPU2wDSlg8doChLJcTyLpmyMY_TYSPJrUOQ584JYWFBAa9w-lKg8KPfOMrvOq28LriMYZ6MeVwpbJXpAkMdTqgXhNmgOr-hwf41QLfNV-bjVULQnyAglUci32m0RyXHOy8mzWos8bs4N-IR9CSw95BrLEQyZ71qPm3MtLvPnn_3wUxeBueNb22y4aaIBt6C8jozZzp0idkAzEtraaRvQREu0BaDBfhkAqRqo9s5ZNStvHxM4P_OXXCBfYnm8pyudM88POoCDGdYnAEmQvFQ8iLILUq5bL2lWe0jU6b4ZiLL47TiUxYndh51P-wxnJmL0TKlafQFjY1var2lEApmE9A1smx9j_TkcIFDkSQ4U7NTBebEO22CRN6dIO-spcpgpIw6_tqa3qsoHLNeptDrEPbgodtU6WlgNMcb0wTa376QfnZYjtJ6Y3CrV1QMme6l-e9B3bQEnbwMtR64" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
امیر سابق قطر درگذشت
🔹
دیوان قطری اعلام کرد که شیخ حمد بن خلیفه آل ثانی، امیر سابق، درگذشته است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670322" target="_blank">📅 23:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670321">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXMRq5_hHzX-Qv287aeOHwPryaT1NLsQr1HNOh4A_R8jjebJVf5PEOJ2E1WAoy7fL59AEfuFu96RTTF-6iz1kOQcZ2XyTg_iP_ChFeeRBfPHOKXHMJM4M6JIlo7hB1nWAjUO8WE5D6lXrCdNekvtr-b5vnl4GdGleufjx-f_iM09As27wHZ1M1BFzdv1XJB30F50bi-rPlziZ8-bFaJhTR2Ab5S0KVNrgKzv1AdvHC4WrX6ubAFesb1fbCvcFZiHX1jcaVpL6Wu0LWHS0nIF2e040OWNUbjc2RUO_EfAMyCbnyRrcuUzM5tt50e7NZy7fU8D0PWPc4L3SbicIYPJgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام مهم مقاومت عراق به دولت الزیدی در آستانه سفر به آمریکا
🔹
مقاومت اسلامی عراق در بیانیه‌ای ۹ بندی ضمن اعلام مخالفت خود با سفر هیاتی از بغداد به واشنگتن، تصریح کرد که دولت الزیدی باید ضمن پایان دادن به حضور نظامیان بیگانه، برای رهاسازی اقتصاد عراق از هیمنه آمریکا تلاش کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670321" target="_blank">📅 23:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670320">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kkMDWItFvUgtDmaxeN_bvMVAM9lbfLwaVoVBqj3H9R-2OkVpo9MPO6WPiS9lN66SoLrsBFkms7Yx6lLuKbDImTRjujhowO4FbF9yAzukgBNwfh9WnpsAsHxiENIemh2lEcl_hTDlW49YIO-RIBGMLJB06TS46g9IalsXSn9EHXvyQdSDkv2Us7pURRc-ibW2a8HXAtctdqcqs7x_8ZgEKrQ1ZzyQILpIBDelM7qW5wedi002wlvBHwB9UCVyQSxRFXLzzsuu9wrzBwn9qS65-nTw9ifSIvlQl4psYIY5WXCGZAjNfA9T43e2olCRhN6Y8f7_G3t-RkpGB6C-fTVTew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پوستر فیفا در فاصله یک هفته تا فینال جام جهانی ۲٠۲۶
🔹
ساعت ۲۲:۳٠ (به وقت ایران)
🔹
استادیوم مت‌لایف
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/670320" target="_blank">📅 23:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670319">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتانیاهو، درباره مرگ لیندسی گراهام: در اسرائیل اندوه است و در ایران جشن
🔹
مقاومت اسلامی عراق: سفر هیئت دولت به واشنگتن قابل قبول نیست.
🔹
آژانس بین‌المللی انرژی: عرضه ال‌ان‌جی قطر و امارات به شدت کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670319" target="_blank">📅 23:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670318">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b76bad9173.mp4?token=eawDMyPK09lm6mUEUJR5GbJizFb8SfQqisdiXckH1crV-LIVBzS5ZTb9i786suUOAqdLW5ClLfcKBDTROujS2hMjUgJjbbYPlAICXrSJAoC0jM2fwVOwbV9e5Ep-hi3qPt9O1WkGGMBQNInLCQDQC-qb85ySzz9M9CaXm0fMP0Sdg0kbyUmi6jaAmNTGnOuwUbYw0N3s53e6wIeYbPaIGgx89WhEgyex3SnLSyK6Q9eEh9FNjY1VMtI0dYUAADjIC7HyZuDi0_KkpkZGKrwayURJ7hDgHKfC_WxWU9Yb28-NAWQg3HTXnDCr8y1ygve6YFf0lcg7h2XDseoyNopY0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b76bad9173.mp4?token=eawDMyPK09lm6mUEUJR5GbJizFb8SfQqisdiXckH1crV-LIVBzS5ZTb9i786suUOAqdLW5ClLfcKBDTROujS2hMjUgJjbbYPlAICXrSJAoC0jM2fwVOwbV9e5Ep-hi3qPt9O1WkGGMBQNInLCQDQC-qb85ySzz9M9CaXm0fMP0Sdg0kbyUmi6jaAmNTGnOuwUbYw0N3s53e6wIeYbPaIGgx89WhEgyex3SnLSyK6Q9eEh9FNjY1VMtI0dYUAADjIC7HyZuDi0_KkpkZGKrwayURJ7hDgHKfC_WxWU9Yb28-NAWQg3HTXnDCr8y1ygve6YFf0lcg7h2XDseoyNopY0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طفره رفتن خوک هار از سوالی دربارۀ تنگه هرمز
🔹
مجری: ایران اعلام کرده که تنگه هرمز را بسته است؛ آیا این درست است، آقای رئیس‌جمهور؟
🔹
ترامپ: از نظر ما، این تنگه باز است؛ درباره این موضوع سوال نکنید. درباره دلیلی که از من خواستید صحبت کنم، صحبت کنید.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/670318" target="_blank">📅 23:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670317">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O349jRR06Vzl5LPlBI6k_9ackrc44BgEjpQY4cXiZTMp2w_lD0U5CNUh1rjL-ynTppnhfdtyv7nPikunCPlfAoWSfUEfs4UaGHLDMdHA_ILLGQITXFf4RMQzNIA-NdRt9kIZgHhW8DbyRK6466kTddqNZMhW6IOrpeW4JGwMLsPegXXGAkk_AvxuDk50dnGq0E7GVlNFgLcWsvb6UABWDvSt5L9uWx6-PDUXtdu86yfzAwNHIcBJN7d-Voi4B-nfrim50YP0oJ4ksWfHg7LAfRH_0uSwO4NvSD_8NAiOIG6E6xLYk1vVQp3tUfMBh0LbDDotqAqJz-s8jHI9Tgixwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پاپ لئو چهاردهم: متأسفانه، بادهای جنگ بار دیگر در خاورمیانه، در اوکراین و در بسیاری از نقاط دیگر جهان می‌وزد و خشونت، ترور و مرگ را می‌کارد و بار دیگر بر بسیاری از مردم بی گناه تأثیر می‌گذارد
🔹
اجازه ندهیم این بادها شعله امید و آرامش را خاموش کنند، حتی اگر شکننده و سوسوزن به نظر برسد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/670317" target="_blank">📅 23:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670316">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBO8UaiR0hpjv8Z5NiSaeDhbuUy9C4-CS1UQUipmo09tgm3JX0_EZmtdCspxuD8JnYtC-ad3TiPQtz0WMB0hCkkjt3qTq3ewg_rb8t5RMy-Us3fr5XxBy83EUIRNfGXN6eOvyKGyI1Fxs6de4zv0Jh74aY50zSJsUAZADMUigGugXgjrk11Bd3Vxn1Sr0hPLP7hfDnRV5SFBSUNKQLu3LsumlHa7S1zD89BtUdMC4ocu5SK-K1bgsSVvrMGdkCFJJdiiXRcCYB9P2ifpjDAWePHK4UaDmHd6flrDvnB5Dw6ezqqsEubCABLNcK8KJhP6W0WvF7Zq8IDgIjt9c2WQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشتازی حزب آیزنکوت از لیکودِ نتانیاهو در نظرسنجی جدید
🔹
براساس تازه‌ترین نظرسنجی شبکه ۱۱ اسرائیل، حزب «یاشار» به رهبری گادی آیزنکوت با کسب ۲۴ کرسی، از حزب لیکود به رهبری بنیامین نتانیاهو با ۲۳ کرسی پیشی گرفته است./ جماران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/akhbarefori/670316" target="_blank">📅 23:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9054413b86.mp4?token=JY6WZ59_4109rNC56QvbWfKBkHVRIMS_r7wEkxp70GaQnDL2-uSfBx4G3F_RIPfVS3f9JIPhMDpbBPaCL4MYdkY0f78S1pO5ryLxhFLaAWh1ad25jIkcH7d6NuArvmQE-8JYN0rqyB8eQSEnc3XA_4QNEiH0ZwNWw9UnPnKMvvjWk1VgyE6dZFjeW1Pje4IaJHFtuiyNRtZ-thx9ytnPNuUv-SM8wjmfteimKvt8yaW9BZIPyq_29kFCKDJQdQZneiHbxlAVv-XqpW92pJ3BFlCfOx52cHnvcpNdHrof7hUdPS7smw4bft1I-aV8arCG3kd4IP3boTfe8SUX_1XjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9054413b86.mp4?token=JY6WZ59_4109rNC56QvbWfKBkHVRIMS_r7wEkxp70GaQnDL2-uSfBx4G3F_RIPfVS3f9JIPhMDpbBPaCL4MYdkY0f78S1pO5ryLxhFLaAWh1ad25jIkcH7d6NuArvmQE-8JYN0rqyB8eQSEnc3XA_4QNEiH0ZwNWw9UnPnKMvvjWk1VgyE6dZFjeW1Pje4IaJHFtuiyNRtZ-thx9ytnPNuUv-SM8wjmfteimKvt8yaW9BZIPyq_29kFCKDJQdQZneiHbxlAVv-XqpW92pJ3BFlCfOx52cHnvcpNdHrof7hUdPS7smw4bft1I-aV8arCG3kd4IP3boTfe8SUX_1XjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین ویدئو از سردار عظمایی، فرمانده نیروی دریایی سپاه: هیچ کشتی خارجی بدون شناسایی ایران از تنگه هرمز نمی‌گذرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670315" target="_blank">📅 22:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
عبور نفتکش چینی از تنگه هرمز در مسیر تعیین‌شده ایران
🔹
بر اساس گزارش‌های منتشرشده، یک نفتکش چینی تحت مدیریت سپاه پاسداران از مسیر دریایی تعیین‌شده از سوی ایران در تنگه هرمز عبور کرده است.
🔹
طبق این گزارش، مسیر جنوبی نزدیک به سواحل عمان همچنان بسته اعلام شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/akhbarefori/670314" target="_blank">📅 22:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670310">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jCM3AvkMcxOuoe7449FLqi7e73Hqu0-J3V7bjbQilQ8PcAFZqpNlmuJu_MEVQlj_t7PGQBjQYKY4tJeY85rm2X1d-CLD5y4tJuzYTgT-V8PKsIXE5iBJ3DINIsJen7-SoNMKgO3u0C-GePx8S1oB9cc6K6z55XEXbc8ERBwPWjn-SfNn_GKTs0gzej6EnX-LNPZZ-cIsOC5qFOJaZTTrWrzQYMHiWjlcDH8jPqgiZVBRyDPjyNEvBea5h5d1VdcNMST1691v0hvVrG5J4zl2zMz1LBcOGCcnZxQy_jztHg2lbaG1lPvx_hM9W-LmUfZmGjS-q1nDsBN6cMRD4CdHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_0xB2QU0lc1bV4P01v4ZT8A2o-lI7SeloOjJ6wpViZZGNlv6XGzQqknpJ0zVwIGzd4yZvK9q5tQvkAr3s1zL8CA3A7W5I0EfnS_-DswScOKgjaep0ASZbCLFcZw-XravyEgEIss1BtGstslDby1a0VShhz_QAJjoDMK139Ss7AH513axDsLAhOmw3QnTn9QoYoMuB6BihXXSPdl_gwPSn4pQqxctovIwgVokr4LMMd2IEvEPOydFBBasHjVdlz5HGTlAlxYUxhBcx3SbJw2lz12TJ7Qo1gUla88skNLAgSP5WLK_qAMOQxjUGRMnDBDIiQXrrhEBv29Fc-vHP9HGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ndSH-PNKzcK-wRRFw3zB9of9qrhbaudMAePRXFxpDXX418fAgGzDGyzGKYaxRELb-N4FsLpr8Btmu9OHvs7lDIn8q56J62ldgBZui4lpVtTqALPslp3gyg6pLzxuILGDmgQifP1fgvwY51bd9JJ3o4DL2J9mfdFq22wkcKwT5KERZP3YtvKMiYXLz2IHDzfN9G1mBT-sAuDGbU8yVYW-EXSHmJU_nkc8wYzaYKrUWPRFvtWmADTpimSRMDSHUHQE21gDb0NULmV4jg6gL9a6119-IlwDEiYzHS50ZIwH_RO39QVHxKXo5mb8KARrE6f5Qp8VLspbzIr9gYjtMpeDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HJQU_ciDhG-ajx32mueoCbborZWxUu4oolWOPgVBrKLpuNjWGZAgGte-Dmd72dsGv7i_AeicRctaRRecFTSG43_OEKORA363jh2l58B6DZTvAIugUHG9xlE_zYP01E-WHBeBIrN257x4qz0nBmLhKefBxhF1nmUS7YRvcu2EzQ2y4-aRaVlafjMij0acn2ICyOd3-DWUD7Bgxuxunbgf17Oy4nrl4NOgFUpvzaM5IwSImZ3cNUjPTPqcS_kKRGYCX88HJ9JoZrrMeSJi83li8QzYZGeKJdn328AJmMGPi7D2DkK50MuRJGgkFscOGH3JYJK7E00M9oMKc6VhhgJbNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از حملات ایران به تأسیسات آمریکایی در خلیج فارس، که در تصاویر ماهواره‌ای دیده می‌شود
🔹
آشیانه پهپاد MQ-4C تریتون در پایگاه هوایی شاهزاده حسن در اردن ویران شد.
🔹
آشیانه‌ای در پایگاه هوایی العدید در قطر آسیب دید.
🔹
به یک تأسیسات انبار در مقر ناوگان پنجم ایالات متحده در بحرین اصابت شد.
🔹
آتش‌سوزی در یک پایگاه در کویت، که ایران می‌گوید ایالات متحده از آن برای حملات هایمارس استفاده کرده است./ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670310" target="_blank">📅 22:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670309">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5aab71909.mp4?token=QljBvg9qaJQk0jvOrR6HQLX93HR_6ZI6OPgtZOi5ufjCD1IQ8F6PWcfpMaN5BfYkMO5-LLaPzRvSFkjqx-oPypH3tr4VOFoH0aF2OS3nJrkafCwjy8Zmki93yScZG0WTRoVl-BfJGB5a6G_EScs0YE3kb6gagCOyBRlMHhqR_hHi4lmaMXd0CqbK0j6xFq6k1YdE5zlE41Q5st1waYjdbxnJP36LBEai03QaPSiBsjYIWkAD6_xF3BZRqSUwoTydArSwIHlXGT_vig-OKeJGWkOcPep0CdWWYEMD3o4aEXIEnFqF_17Nl2rrZHt0K3_ylhdivB-yHyE6HxQOVuAyxZS_Tz2ZYCQL-TQ2fK45y8m5Lz9URxv76xMDTstIHZKdhTASVD1d5Q1XCxiTM-je3cHLvpnWaPkHSqCLPNDDOcPlctQK9fAqET5_Wm2oHHLZSAvEqCF1rrQNQT6Jt_oDoqspcj3R8mTQSX7vgRO3pACyPbxZ28QB3f2Tfcck00BuBc_gt4hk1sOIj4e_Y2rSoJJrQnhUQERDjOF7Q1oW9ptUpZSy-7Or1whf-ybUiy_dmNsbsdXqw2uDr3Agr7IDs4YCG4NnfLPuH3jeeCllIlqMSX3pOtl6elQp2goifMRD-2OBLQnlt63W4iKaC54peGomJ47ecncoEjC5GThMofo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5aab71909.mp4?token=QljBvg9qaJQk0jvOrR6HQLX93HR_6ZI6OPgtZOi5ufjCD1IQ8F6PWcfpMaN5BfYkMO5-LLaPzRvSFkjqx-oPypH3tr4VOFoH0aF2OS3nJrkafCwjy8Zmki93yScZG0WTRoVl-BfJGB5a6G_EScs0YE3kb6gagCOyBRlMHhqR_hHi4lmaMXd0CqbK0j6xFq6k1YdE5zlE41Q5st1waYjdbxnJP36LBEai03QaPSiBsjYIWkAD6_xF3BZRqSUwoTydArSwIHlXGT_vig-OKeJGWkOcPep0CdWWYEMD3o4aEXIEnFqF_17Nl2rrZHt0K3_ylhdivB-yHyE6HxQOVuAyxZS_Tz2ZYCQL-TQ2fK45y8m5Lz9URxv76xMDTstIHZKdhTASVD1d5Q1XCxiTM-je3cHLvpnWaPkHSqCLPNDDOcPlctQK9fAqET5_Wm2oHHLZSAvEqCF1rrQNQT6Jt_oDoqspcj3R8mTQSX7vgRO3pACyPbxZ28QB3f2Tfcck00BuBc_gt4hk1sOIj4e_Y2rSoJJrQnhUQERDjOF7Q1oW9ptUpZSy-7Or1whf-ybUiy_dmNsbsdXqw2uDr3Agr7IDs4YCG4NnfLPuH3jeeCllIlqMSX3pOtl6elQp2goifMRD-2OBLQnlt63W4iKaC54peGomJ47ecncoEjC5GThMofo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محمدجواد لاریجانی، کارشناس ارشد مسائل بین‌الملل: از دیپلمات‌ها و دیپلماسی انتظار داریم که سایه جنگ را دور کند و علاوه بر آن باید سایه ترور را نیز دور کند
🔹
اگر انتقام نگیریم، سایه ترور همیشه وجود دارد.
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670309" target="_blank">📅 22:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670308">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CW9fP4TFE8CxQ75gMmDdPVdysCfoO48lsSzpIEaM1KOs2QqzJxn2tshLL_65uaLTCeCykBT0D-9lV6JauK42F_KD4C49WlcdyRVNpInkQsd3U4ItUUA867m_Q5idTgaW5sZ1uhL_NhWrxpQrAMsalyPOFNUjOrzSf_xLcpQQQTYV83V4ue2YC3q8MmpjNRpeOj97RNLMEnC92h_8nwgFTnNV2PgE9dW8LCADSZjG3GdmW6OQKH7uDobEzc2GyvAxxVaH_Cir6my3bWWxBpCFiBbW3X4vEu0z4eqkKu1Vhw01R_ujA-qmbcXPowdodSELZ4tY0i1hQP81UnVnDctf0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حقیقت وجود هر آدمی در طوفان‌ها شناخته می‌شوند
🔹
آدم‌ها در روزهای آرام کمتر شناخته می‌شوند؛ این فراز و فرود زندگی است که گوهر واقعی‌شان را آشکار می‌کند. ثروت، قدرت، سختی و دگرگونی‌های اجتماعی، نقاب‌ها را کنار می‌زند. بعضی در غرور،  دنیاطلبی و سختی‌ها سقوط…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/670308" target="_blank">📅 22:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670307">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
کانال ۱۲ اسرائیل: نتانیاهو با اشاره به مرگ گراهام که امروز مرد، گفت: «او به من گفته بود: باید به تأسیسات هسته‌ای ایران حمله کنید.»
/ انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/670307" target="_blank">📅 22:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670306">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bad85807b.mp4?token=rKVTuo976iFIuBnJk4tvqUyb61wx8aVWKCgaAQSmD_zwtDuqbURUZwyI5MoHaUnz-l-2gx7p_-T2GvD0Rl7Ic5YMjE5kl-4WS7_3sXZ9ydFO8DaSAMI_cH13HknTW65CjsUuTuUYdpmi-Am_BFEawDxnCvXoCUZTB3emP-2XUzVAmW1nwBtF_IV3PP42AtCHAgGQc0e1Q4Bo_iryAkP3JHVnhYPXB5UhOWlNEBfOMTDMU6qT3dx4Xx43R8VUeFifrBHnE8fPXmlsLcOC1aaLJZLWsfHND5c2A7My22FBZERl3U2KjCyZX-l_ihSGAVG--k0BHrhzXqujyD8TwTdLsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bad85807b.mp4?token=rKVTuo976iFIuBnJk4tvqUyb61wx8aVWKCgaAQSmD_zwtDuqbURUZwyI5MoHaUnz-l-2gx7p_-T2GvD0Rl7Ic5YMjE5kl-4WS7_3sXZ9ydFO8DaSAMI_cH13HknTW65CjsUuTuUYdpmi-Am_BFEawDxnCvXoCUZTB3emP-2XUzVAmW1nwBtF_IV3PP42AtCHAgGQc0e1Q4Bo_iryAkP3JHVnhYPXB5UhOWlNEBfOMTDMU6qT3dx4Xx43R8VUeFifrBHnE8fPXmlsLcOC1aaLJZLWsfHND5c2A7My22FBZERl3U2KjCyZX-l_ihSGAVG--k0BHrhzXqujyD8TwTdLsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بستنی میوه‌ای، پادشاه فصل تابستان
🍦
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/670306" target="_blank">📅 22:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670305">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBank Maskan | بانک مسکن</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68c4e1f16a.mp4?token=vVrX1ULMRH44AK3MdiPaPaFoOcuJUO6WqsoEvNzQIqet2GrwoxjvZtmeUMQkvL4r1yD2USm6BmvRcZidiky4DaB-BQXMZmTRXux_pTNkXcqicY7hZJmNl1XQ2XAvdnsS5unZeQg-KyL7mflTdvpamE1My5axV1WjmGf22voKlErc3uOqNJ4I51tUYJOVx-Slrt_gZZQJXwk6WFj37fWZDp7_6zpHzq_42sSY43vNkEdJa7ZIISgFxA9BQWRE9yr3_CKmd_zYAY9oq9aJ6AV-sevRwpiDCdU4j8Kqmy_S3vFF59UBvdpKL5we4BeW6b0pjQIVFyJV1SvJ0s6-ZcyA4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68c4e1f16a.mp4?token=vVrX1ULMRH44AK3MdiPaPaFoOcuJUO6WqsoEvNzQIqet2GrwoxjvZtmeUMQkvL4r1yD2USm6BmvRcZidiky4DaB-BQXMZmTRXux_pTNkXcqicY7hZJmNl1XQ2XAvdnsS5unZeQg-KyL7mflTdvpamE1My5axV1WjmGf22voKlErc3uOqNJ4I51tUYJOVx-Slrt_gZZQJXwk6WFj37fWZDp7_6zpHzq_42sSY43vNkEdJa7ZIISgFxA9BQWRE9yr3_CKmd_zYAY9oq9aJ6AV-sevRwpiDCdU4j8Kqmy_S3vFF59UBvdpKL5we4BeW6b0pjQIVFyJV1SvJ0s6-ZcyA4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چهل و ششمین مرحله
#قرعه_کشی
حساب های
#قرض_الحسنه
پس انداز بانک مسکن
#زندگی_در_دستان_ماست
🔹
۶۰۰ کمک هزینه
#خرید
یا
#نوسازی
واحد مسکونی به ارزش ۲/۵ میلیارد ریال
🔹
۳۰۰ کمک هزینه خرید
#وسیله_نقلیه
دوستدار محیط زیست به ارزش ۵۰۰ میلیون ریال
🔹
۳۰۰ کمک هزینه خرید
#لوازم_خانگی
تولید داخل و صنایع دستی به ارزش ۲۰۰ میلیون ریال
و صدها هزار فقره جوایز نقدی دیگر
🗓
#مهلت
#افتتاح
حساب و یا
#تکمیل
موجودی تا پایان تیرماه ۱۴۰۵
◀
#حداقل_موجودی
جهت شرکت در قرعه کشی ۱ میلیون ریال
🏆
هر یک میلیون ریال در هر روز یک امتیاز
🔗
جهت کسب اطلاعات بیشتر به لینک زیر مراجعه نمایید.
👇
👇
https://bank-maskan.ir/g1405
@bankmaskan</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/670305" target="_blank">📅 22:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670304">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIa2wxeGe8JJTvKLH5e28dRAI-Uhdrak97DozGxmdNPaAJx5r2kuIgUmt5BGzzLN0oxvk7IvVvYEtny2YvRc-5mZrDVw4iPjGqp03o28HlyzBs6HKuursS_pgQETOUz-OCmw4h1YJIpj6Xrn9UpqNiu8eiYNK5suBGEY3b8o4fdchKouy2elseTK27KAbW5eGrsAVyNwqjolWiKBzk68KGcH7PL_ysJZcenWFyKS8O-K1-Ib6NqccyaIQlWQN9U7-bkqQOIwVeJEAf4Irfz9TSpC69EsKzyeDpdbRt668m3XHRK_c0QBAxdFqwRz-ORNY0ZNwbElL6o2WLeYLXxmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الکساندر دوگین، از مقامات نزدیک به پوتین: احتمالا موساد، گراهام را ترور کرده و به ترامپ پیام می‌دهد: «نفر بعدی تویی»
🔹
محتمل‌ترین سناریو این است که موساد گراهام را ترور کرده تا ترامپ را به جنگ تمام‌ عیار علیه ایران تحریک کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/akhbarefori/670304" target="_blank">📅 21:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670303">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏆
آخرین اخبار و حواشی جام جهانی ۲۰۲۶
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/670303" target="_blank">📅 21:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670302">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0e8abfa4.mp4?token=l82x5L74XsOOqpYOIXdoMlQHXMcHbkp_KOqHjwPNubnpMnngaQRRa_cIyGeypapoOlNBgXxA_CigFUyj8WxvhhKmXKFEAiHXA31Ixap5EkS_NlJnGSx_GUKVpuTzwBYJGEwUf6t_L4whP_ik-1fF7bgNx5afK2b1vWwWxQ6ecbq1S0oaTXd5oUGrRadzrGTR_D6u72TpVyLu_ADX3vhFbGoME6ZRW6NSPMN_aHzGl4POic0lQPNBb4l1vu4VAkx-pBZhm3U6TGIlFlwaB1ogO_XGXOmlYOeDeNr1-1KYUUGHGHIoUqbPziTDakhCLv9UZG8o_Piaw4n6Ijqve08OLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0e8abfa4.mp4?token=l82x5L74XsOOqpYOIXdoMlQHXMcHbkp_KOqHjwPNubnpMnngaQRRa_cIyGeypapoOlNBgXxA_CigFUyj8WxvhhKmXKFEAiHXA31Ixap5EkS_NlJnGSx_GUKVpuTzwBYJGEwUf6t_L4whP_ik-1fF7bgNx5afK2b1vWwWxQ6ecbq1S0oaTXd5oUGrRadzrGTR_D6u72TpVyLu_ADX3vhFbGoME6ZRW6NSPMN_aHzGl4POic0lQPNBb4l1vu4VAkx-pBZhm3U6TGIlFlwaB1ogO_XGXOmlYOeDeNr1-1KYUUGHGHIoUqbPziTDakhCLv9UZG8o_Piaw4n6Ijqve08OLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدرت پنهان کلمات منفی در زندگی آدم‌های معروف
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670302" target="_blank">📅 21:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670301">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: ضمن خداقوت به تیم مذاکره‌کننده، تلاش خود را کردید ولی نتیجه نداد و حالا میدان رزم را به نظامی‌ها و مردم در خیابان تحویل دهید تا ما در جنگ بتوانیم منافع ملی را به دست بیاوریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/670301" target="_blank">📅 21:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670300">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
معاون استاندار بوشهر: حمله به نیروگاه اتمی بوشهر صحت ندارد
معاون سیاسی و امنیتی استاندار بوشهر:
🔹
انتشار برخی مطالب در خصوص اصابت پرتابه دشمن به نیروگاه اتمی بوشهر صحت ندارد. نیروگاه اتمی بوشهر هم اینک هیچگونه مشکلی ندارد و در امنیت کامل در حال فعالیت است.
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670300" target="_blank">📅 21:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670299">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وقوع انفجار در استان سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670299" target="_blank">📅 21:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670298">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
آکسیوس: لیندسی گراهام ساعاتی قبل از مرگ گفت الان نمی‌توانم بمیرم، هنوز باید ماجرای ایران را حل کنم و تحریم‌های روسیه را پیش ببرم
🔹
او چند ساعت قبل از مرگ، احساس ناخوشی کرده بود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/670298" target="_blank">📅 21:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670297">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3SCrD3VMDnc7yjQ1WUypEo5dvZ1NkOcgY_bJfxI8UxDjsU3NcuqsHie2d9tjElCZrZCKodBYqnR_eE8UfXECSKqRXwSESYeljJsGfiqGD5Ou461XzITYwswXULwb2Td3OorNwt8uAcrYIJTN-UILvSnHkmefN6JAjeEF8amM9WLgCXNim9DQzoP4p0ZkIE-cG1IM23MCdTgdd8bjycNO5ePrrAaFPcPyuUg-08t79F-sgIG1TzYra8NUCx_tlhkubCalxvCb3mVKrzdcbhJHQGHCK9DM9b_M-8M4hdPQSu4ER-tEx78PF2-mP2bu_qfmnKd9IUF30ibMyb6NXytrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر کمتر دیده‌ شده از رهبر مسلمانان جهان، سید مجتبی خامنه‌ای در منطقه زلزله‌زده سرپل‌ذهاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/akhbarefori/670297" target="_blank">📅 21:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670296">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_i-QvJd_fTlwi2LL3FaCm900-8_pXwWUE-yecuZ4D35W6kDnYJ_XqrWxltuC64Ty6Eg5JRtB5XvsiKabKAWkCtHA4MAT2o0E5n8Mg2ldIpNsYve9Uu6DIiu816766BN-l4x1K6YYAlYEnAAAyoZh_IS7nS8VYtb84RDpfl_woUAkmDkx3vLc2jPMY43F5ub8uIrG_CRl5PGHJ_XPkHDhonANPxnNRbojCutdXJTb-0f_M1bcBKoMabbpDJOCBBznKOzJS5K9CI3rBG_19SjO6t6qnQ-bWsprNoTjFsODcEg3HMuFERMZXlts3ID2JAIAG85AfVkurksvhIOH6peXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چک‌ لیست ملزومات شرکت در کنکور ارشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/670296" target="_blank">📅 21:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670295">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی بانک قرض الحسنه مهر ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPg5aXTAd3IC-r86PMWSaXUX4q2o8aCcY3U0SERXhX3_Uv7p7XdZAVexehcToabcwZKoMDEcdwEaM_wNaqXT6nKyclKuJdUyUP7-7Gjk1nKedXMx4WaDg0t23iq8n72XtHs1noqH77pnlyYZGPrlrHQncytaB0R_obiiWBdt69TCe0DAsE1EkbUY82iDJQoI98kP4rkuWjaWWhGj3AJtZa4NJk9gDpmFPeKcIohXJDRVRuanG1p9_CLV7tmclgbOZ0FfgQpLeN9PS34xZa2-8QBPGk0gsl6s3pWRFQ5TcNcE5kzxjVMwW85T0vBT2s86yu8dkEZrc5lRqM44HEF9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
🔹
🔸
🔹
🔸
به همت بانک مهر ایران و در رویداد کیوتاک انجام می‌شود
🔰
بررسی توسعه راهکارهای بانکی برای ۷۰۰ هزار کسب‌وکار تجارت اجتماعی/ نحوه حضور در نشست برای علاقه‌مندان
🔸
بانک قرض‌الحسنه مهر ایران در چارچوب حمایت از تولید ملی و تحقق سیاست‌های اقتصاد مقاومتی، توسعه خدمات بانکی ویژه فعالان تجارت اجتماعی را در دستور کار قرار داده است.
🔸
در همین زمینه، جلسات کمیته علمی این رویداد با موضوع «تجارت اجتماعی و شبکه بانکی؛ راهکارهای نوین بانکی در توسعه اکوسیستم تجارت اجتماعی» برگزار شد.
🔸
مدیران و نمایندگانی از دیجی‌کالا، اسنپ، زرین‌پال، پادرو، پیام‌رسان بله، شرکت معتمد مالیاتی تیس و هفته‌نامه کارنگ حضور داشتند و محورهای علمی رویداد را نهایی کردند.
🔸
این رویداد روز پنج‌شنبه ۲۵ تیرماه از ساعت ۹ تا ۱۵ برگزار خواهد شد. با توجه به محدودیت ظرفیت سالن، علاقه‌مندان می‌توانند برنامه را از طریق صفحه آپارات بانک قرض‌الحسنه مهر ایران به نشانی
www.aparat.com/mehreiran_bank
و به‌صورت آنلاین دنبال کنند.
جزئیات خبر...
🔸
🔹
🔸
🔹
🔸
🆔
@mehreiran_bank</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/akhbarefori/670295" target="_blank">📅 21:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670294">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6943e537c.mp4?token=Cup9Q_DIu9mHwNniNPZJW9R6Kwp55qRZPOzU3PVaxeZUvpIPVzm_C5tLsqK6JWlrTdPuP4x046HSMmTCesXr2lUs4OHLB50L5oE_uQwDX69ihkll9uXfzLpEcUzvm5ts0PDlgE2UAv5CsWtmyGYvSEkgzytNgP5yT3YVjccVKMrZCygO8CtJeJJrSa9Ip8y9N0UeOSnRoBIDmEd1XXK5-g7k7ygjmSfypyBnWAOXSCWXkH_V2_ax-zUlxPiu99rGdfjzcqIbWTDr2y6oHRMfQHBJnvrDfb-Ac6tgLhO5j8ccxdJL9acRe4N3el4z5IxFk31X6a2akstKWzmwBaM4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6943e537c.mp4?token=Cup9Q_DIu9mHwNniNPZJW9R6Kwp55qRZPOzU3PVaxeZUvpIPVzm_C5tLsqK6JWlrTdPuP4x046HSMmTCesXr2lUs4OHLB50L5oE_uQwDX69ihkll9uXfzLpEcUzvm5ts0PDlgE2UAv5CsWtmyGYvSEkgzytNgP5yT3YVjccVKMrZCygO8CtJeJJrSa9Ip8y9N0UeOSnRoBIDmEd1XXK5-g7k7ygjmSfypyBnWAOXSCWXkH_V2_ax-zUlxPiu99rGdfjzcqIbWTDr2y6oHRMfQHBJnvrDfb-Ac6tgLhO5j8ccxdJL9acRe4N3el4z5IxFk31X6a2akstKWzmwBaM4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نتانیاهو: در آخرین مکالمه‌ای که با گراهام داشتم، گفتم: ما می‌توانیم خودمان هزینه دفاع از خودمان را تأمین کنیم
🔹
او گفت به هیچ وجه شما نمی‌توانید این کار را انجام دهید و او آنقدر به امنیت اسرائیل متعهد بود که در واقع با من بحث کرد که کمک‌های آمریکا به اسرائیل ادامه یابد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670294" target="_blank">📅 21:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670293">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7541b6913f.mp4?token=GFjsatZeWL-ADvt0WxsIwqX_2qYowsAZ9K0jQkW-_NAwLfhQqMC4BB6NEexJl846YX3Vvsdnlwkmrv0UmPVfP3B5wdVQws815TPdbgqGfkFpzCyJbnMn--SSm5EAIBfD6iOhaZqGfwnUx_gz9XFhsu1H2aI6mD9_sl60i7wI23o5QCY8vm7caZlDTFxYbDR70UNWKy0klGA-zSPR8kTT8M7uINmT1JgdWMfpHAAOVtoHWTiRrjwpKW0xojTYpCl_CATDjjia1wjdtGuIMlhrvJqScNLgUIaUMfpStJMFMsOCZb4ewyl1pIZtqXEt6nXPTUhI1SWLPmTgYRVx2D2o2JBBKZEVkeFTEkz_bjYerDIrW5UnvhIYRTyZy44iwKizgWyB2SaKcyT9ZpZon1pumjGnhqxLmvBXV9wsucjBQTu_efOoH1gmcPrSuAydoWwej14l38hUecgyEQz7qx0LhoqcEBSaEf4bROS6Fb82nuGgJBC2jESTOUyLf5K0LzlIx1JmrEpBj7vwC_8PlGKkR1eD2ecqJ7ARC26nu5pPNdHxmonzGBnoVkpFNSWBkYiwmLGM3oGXKgF-fT8B2EHik-LO74ptWHhVbGpSED1sKn3xzMuEyBRFEyEdI2I5p_d1-d-5UY5np3RuDMikb9a4ny7dKHTK_0-mKz2lTRekjRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7541b6913f.mp4?token=GFjsatZeWL-ADvt0WxsIwqX_2qYowsAZ9K0jQkW-_NAwLfhQqMC4BB6NEexJl846YX3Vvsdnlwkmrv0UmPVfP3B5wdVQws815TPdbgqGfkFpzCyJbnMn--SSm5EAIBfD6iOhaZqGfwnUx_gz9XFhsu1H2aI6mD9_sl60i7wI23o5QCY8vm7caZlDTFxYbDR70UNWKy0klGA-zSPR8kTT8M7uINmT1JgdWMfpHAAOVtoHWTiRrjwpKW0xojTYpCl_CATDjjia1wjdtGuIMlhrvJqScNLgUIaUMfpStJMFMsOCZb4ewyl1pIZtqXEt6nXPTUhI1SWLPmTgYRVx2D2o2JBBKZEVkeFTEkz_bjYerDIrW5UnvhIYRTyZy44iwKizgWyB2SaKcyT9ZpZon1pumjGnhqxLmvBXV9wsucjBQTu_efOoH1gmcPrSuAydoWwej14l38hUecgyEQz7qx0LhoqcEBSaEf4bROS6Fb82nuGgJBC2jESTOUyLf5K0LzlIx1JmrEpBj7vwC_8PlGKkR1eD2ecqJ7ARC26nu5pPNdHxmonzGBnoVkpFNSWBkYiwmLGM3oGXKgF-fT8B2EHik-LO74ptWHhVbGpSED1sKn3xzMuEyBRFEyEdI2I5p_d1-d-5UY5np3RuDMikb9a4ny7dKHTK_0-mKz2lTRekjRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متیو ویتاکر، سفیر آمریکا در ناتو: معتقدم در صورت برآورده شدن شرایط قانونی، توافق جنگنده‌های اف-۳۵ با ترکیه نهایی خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670293" target="_blank">📅 21:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670292">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=RHQayocZgeUmcY-xyiNPCbQ2jcqjZ02fNgPzZINMZhsFaNJ7yBDsFqfMoGt4ClYAWn7g4hlSQX2_kG9F1opD_3ra9_t4aDiuopDEvUQ5UAEjfYhH27FZhDFGqo7sCRe2ASnvz1bV2CDzZuIai6miflQ5SDru_Y2aOfm5e1moI7JsAlGkyj130FMNHHqsHHz4dw_M1l8QU_zrX3Wpdb3PRK6CVOMmBo-hMaD-uQFK5RAR2kqudYxAl3OCHkBdKqrGDwmwnnWlsesUW3kDPz0886SEp099TKGtFYaInmCe-B_9VoQJCnxeOD_1BC2aqA6pkK4CIJbbl_zFpxM8BThUC0OTVV-6pEuVPiz75Le1Rv1L9ttKOEyY9IvZ-PBjayiKVpaSvLi_JrOLxX6u2sb9fiQ4HM6RiYdw7yCt5pQWC31LO8wRvXZ2waOdBJt-ira8ALumQhkN85RYU7NsjAuLevdzCAI_EVXZKLKXIlRELriYLP186qnLPtipyWJbveUvFTTThADEsjtDu58NTHpIqxt48uUYDh-ajZ41sU3lwitFn_oPHtT9VJ7FBRqPmhe4bd8MGf3ze8iryFhZ-FVsJRy2b5az7JaiIsl-vuiuzJr_rgUaGWHi_kHOvqP8TfkOMQyYZ8avcQO5ptqT8R_S0Cp1tYxzAuXNDpohUIUdh-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63fb7b34c.mp4?token=RHQayocZgeUmcY-xyiNPCbQ2jcqjZ02fNgPzZINMZhsFaNJ7yBDsFqfMoGt4ClYAWn7g4hlSQX2_kG9F1opD_3ra9_t4aDiuopDEvUQ5UAEjfYhH27FZhDFGqo7sCRe2ASnvz1bV2CDzZuIai6miflQ5SDru_Y2aOfm5e1moI7JsAlGkyj130FMNHHqsHHz4dw_M1l8QU_zrX3Wpdb3PRK6CVOMmBo-hMaD-uQFK5RAR2kqudYxAl3OCHkBdKqrGDwmwnnWlsesUW3kDPz0886SEp099TKGtFYaInmCe-B_9VoQJCnxeOD_1BC2aqA6pkK4CIJbbl_zFpxM8BThUC0OTVV-6pEuVPiz75Le1Rv1L9ttKOEyY9IvZ-PBjayiKVpaSvLi_JrOLxX6u2sb9fiQ4HM6RiYdw7yCt5pQWC31LO8wRvXZ2waOdBJt-ira8ALumQhkN85RYU7NsjAuLevdzCAI_EVXZKLKXIlRELriYLP186qnLPtipyWJbveUvFTTThADEsjtDu58NTHpIqxt48uUYDh-ajZ41sU3lwitFn_oPHtT9VJ7FBRqPmhe4bd8MGf3ze8iryFhZ-FVsJRy2b5az7JaiIsl-vuiuzJr_rgUaGWHi_kHOvqP8TfkOMQyYZ8avcQO5ptqT8R_S0Cp1tYxzAuXNDpohUIUdh-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی خضریان، عضو کمیسیون امنیت ملی مجلس: مسئولان دستگاه دیپلماسی ایران در دنیای موازی زندگی می‌کنند/ آمریکا و ترامپ می‌گویند که ما از توافق‌نامه خارج شده‌ایم و آتش‌بس تمام شده است بعد مذاکره‌‌کنندگان ایرانی می‌گویند فلان اقدام دشمن نقض آتش‌بس است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/akhbarefori/670292" target="_blank">📅 21:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670290">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
وقوع انفجار در استان سلیمانیه عراق
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670290" target="_blank">📅 21:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670289">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8c9fe4ad.mp4?token=VZ4GV0bZC3flfnmKT3mXZaVdGzsKukn54mCvHcupmKs27S3zmGB3rA8okBg8_EESaLeAbo648AhD_3k4m_8NrF6eYYGYOpQCBTZbetoTjOGGUYe_zFqId776FqaMY5OlJ13YAkcFD0ZZ2MMT5WufLF6xk_ou_cBHDe-aAPWTnaepyjebDCNni5ZhhHC7CktcWFGDTAy_09s6RGyO8WxJsMJYmVQf-vtTg8ylzgg139sbpESl82xnmjCXvSrQYof2VZfWhBDx0SXBnrlZMKPhDrsjtoMGZ6g_HPZHuOcHhivRhiJNson82v5TVlHpkonZSz62TcUPJpQMJzz3khrj7IVt3vZ2WFvBGJpdraj-08k1yRaf8KA7S3_JP5b6bC836Ui-mTI0pYLUba7ZfCVMxYtP18Mn4z4_OgrHUJvdU5__UjBPIvOY0q_fhtqMX9ph4jKdkdxfPZ1_ipXl4yDRRbnV4FelXLUeOcz5Y8YKskgDyDSjcnz2sGbzLy7v4Ll04rJ3LijUslkBqa2y1dxXDuRwJ-wQwHhc-dwRXI5CPClvhOsm3WrKBkfM1psQYOhhdWwhMIwvvVZhG6o8hcdgZ28jJgLOGvPiuoc1KpsqFmIRsmvuR3JN8tSYeZ50aAU7Ghv0LCHkMCkmoQJp9_cSawo9WZR9VqnTeK0eoIxpMyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8c9fe4ad.mp4?token=VZ4GV0bZC3flfnmKT3mXZaVdGzsKukn54mCvHcupmKs27S3zmGB3rA8okBg8_EESaLeAbo648AhD_3k4m_8NrF6eYYGYOpQCBTZbetoTjOGGUYe_zFqId776FqaMY5OlJ13YAkcFD0ZZ2MMT5WufLF6xk_ou_cBHDe-aAPWTnaepyjebDCNni5ZhhHC7CktcWFGDTAy_09s6RGyO8WxJsMJYmVQf-vtTg8ylzgg139sbpESl82xnmjCXvSrQYof2VZfWhBDx0SXBnrlZMKPhDrsjtoMGZ6g_HPZHuOcHhivRhiJNson82v5TVlHpkonZSz62TcUPJpQMJzz3khrj7IVt3vZ2WFvBGJpdraj-08k1yRaf8KA7S3_JP5b6bC836Ui-mTI0pYLUba7ZfCVMxYtP18Mn4z4_OgrHUJvdU5__UjBPIvOY0q_fhtqMX9ph4jKdkdxfPZ1_ipXl4yDRRbnV4FelXLUeOcz5Y8YKskgDyDSjcnz2sGbzLy7v4Ll04rJ3LijUslkBqa2y1dxXDuRwJ-wQwHhc-dwRXI5CPClvhOsm3WrKBkfM1psQYOhhdWwhMIwvvVZhG6o8hcdgZ28jJgLOGvPiuoc1KpsqFmIRsmvuR3JN8tSYeZ50aAU7Ghv0LCHkMCkmoQJp9_cSawo9WZR9VqnTeK0eoIxpMyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتی از کوچک‌ترین نوه رهبر شهید؛ نوری که تنها ۱۴ ماه در این دنیا تابید
محمدی گلپایگانی، پدر زهرا کوچولو:
🔹
زهرا کوچولو در تمام روزهای عمرش همیشه کنار رهبر شهید انقلاب بود. من خودم پیکر زهرا کوچولو را بر روی سینه رهبر شهید انقلاب در قبر قرار دادم تا در برزخ نیز انشاالله با هم باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670289" target="_blank">📅 21:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670288">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrNj_6sKNLvONMKFlh4CM4sy-PAxCM4KOGFIJE8_ZQqoe96V7I-OTJiWhkMHlfIWHgxZostHK_8_qyTVywUtfpifu_eH3qHACQ11xd5ko5M12Jt0WKUVO22R2QIfiItlIuOvhitU76S9ahN4zxoZZPciH8o3Co-Xaf79W-DwJ2vvD1YHBmqadVHA0DxbnJqtRsIdy9xv9CrL0CqRfwnyWGjgSPlSCbcXac_e4paRKOkCQrtTppRoc2YOnI_uTviZZ6qdCk3WCPYD1WEncTP8hhA3CfiB9Nslv69olNqzADgbLOW_22zkYKgBC_E1qKRcrHLvCWuAMExOIo8W6ZzbzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امكان سفارش و دریافت رایگان ۳۰ طرح جدید و متنوع كارت های بانك ملت فراهم شد
🔷
مشتریان بانک ملت می توانند طرح های متنوع و جذاب ملت کارت را به صورت رایگان و از طریق اپلیکیشن "دیما" سفارش داده و در کوتاه ترین زمان ممکن دریافت کنند.
🔷
کارت‌های جدید بانک ملت در ۳۰ طرح شامل ۱۶ طرح عمومی، ۱۲ طرح ماه تولد و ۲ طرح ویژه مشتریان مهان، در سامانه‌ دیما(شعبه دیجیتال بانک ملت) قابل سفارش است.
🔷
در جشنواره کارت های جدید بانک ملت که تا پایان شهریورماه ادامه دارد، صدور و ارسال کارت از هر حساب به نشانی متقاضی کاملا رایگان است، به این صورت که پس از ثبت درخواست صدور کارت و کسر کارمزد مربوطه، ظرف ۲۴ ساعت کارمزد کسر شده به صورت کامل به حساب مشتری بازگردانده می شود.
🔗
لینک نصب دیما و سفارش ملت کارت</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670288" target="_blank">📅 21:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670287">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9017039415.mp4?token=ajLtXcFP1mZm0hCTfbQo89UfpWswZq95o80UCrCLFlUX2s4-qIysiRne4J2QUqcSICYgXYbZ_77o82D6-aYvjZxw7FjH8kIqxX9mT_JjG3zzA0hXSdRkcasKA5cyUY0084qBEXEMpRuNdcLxBNwt7W2RyuywiMBEOSzo5PnSFbup7Lv19y7FcPr_fRQzeFA5VfksouKMn8S_R4NRTKFhNUVaF4Veo3zCU1gdsiSPAAt9x52lGChtthJCW_JkGFxpYA10-wcsyQa8oi8eV49-QvoiDuCHeymZ0Jwe7YLBdmHHNNNlOxmjhzWVLafJxQQorqc81MtQzkyd-Sxmo2cRrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9017039415.mp4?token=ajLtXcFP1mZm0hCTfbQo89UfpWswZq95o80UCrCLFlUX2s4-qIysiRne4J2QUqcSICYgXYbZ_77o82D6-aYvjZxw7FjH8kIqxX9mT_JjG3zzA0hXSdRkcasKA5cyUY0084qBEXEMpRuNdcLxBNwt7W2RyuywiMBEOSzo5PnSFbup7Lv19y7FcPr_fRQzeFA5VfksouKMn8S_R4NRTKFhNUVaF4Veo3zCU1gdsiSPAAt9x52lGChtthJCW_JkGFxpYA10-wcsyQa8oi8eV49-QvoiDuCHeymZ0Jwe7YLBdmHHNNNlOxmjhzWVLafJxQQorqc81MtQzkyd-Sxmo2cRrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معرفی فیلم: هامون | Hamoon (۱۳۶۸)
🔹
ژانر: درام، روان‌شناختی
🔹
امتیاز (IMDb): ۷.۸/۱۰
🔹
خلاصه: حمید هامون، روشنفکری که زندگی مشترکش در آستانه فروپاشی است، میان عشق، فلسفه، عرفان و بحران هویت دست‌وپا می‌زند. او در سفری ذهنی و پر از رؤیا، کابوس و خاطره به دنبال…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670287" target="_blank">📅 21:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670285">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
گزارش‌هایی از شنیده شدن انفجار در جزیره بوموسی؛ وضعیت جزیره لارک عادی است
🔹
در حوالی ساعت ۲۰:۳۰ امشب، صدای چند انفجار دیگر در بندرعباس شنیده شده است که به نظر می‌رسد مربوط به شلیک یا اصابت‌هایی در محدوده دریایی بوده است.
🔹
وضعیت جزیره لارک نیز واقع در تنگه هرمز کاملاً امن بوده و هیچگونه گزارشی از حمله یا حادثه‌ای در این منطقه وجود ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670285" target="_blank">📅 20:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670284">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
واشنگتن‌پست: فرماندهان آمریکایی در جنگ ایران فرار کردند
واشنگتن پست:
🔹
پس از حمله پهپادی ایران به پایگاه بندر شعیبه در کویت برخی فرماندهان ارشد، نیروهای گرفتار را رها کرده و هشدارهای اطلاعاتی درباره احتمال حمله ایران و درخواست استقرار سامانه‌های بیشتر مقابله با پهپاد را نیز پیش‌تر نادیده گرفته بودند.
🔹
این حمله که تنها یک روز پس از آغاز جنگ آمریکا با ایران رخ داد، به کشته شدن ۶ نظامی آمریکایی و زخمی شدن بیش از ۳۰ نفر انجامید و اکنون به یکی از جنجالی‌ترین پرونده‌های ارتش آمریکا تبدیل شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670284" target="_blank">📅 20:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670283">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32baad9c73.mp4?token=MRNKq4tml2eeQwkjif_DbQMTklFEoaGOYKcLw1M7YuNzqeP8Oti2FDRdryNxWNVf6EyY9ZFEiyh1VFBUpi7Op3MTJSet6htvn06oACUYbwJdARzBqB4Qzc6BS_OZNgbwujFl0bTEcyFlQSB74Y5amHKTAhEafFWmzxR7LK33prCO2DosrGv6kHVIaKAnul4O7jk_OAxsWEfQXUEKjNmkq7wzf6i1pC5ltj-Yqm6PrGnsAI-01t7hqUfm_gKmtrLtq1SCGR5XiAOPHMjZ8FQbpX86Fqpnh4tGP-lpcdX3iB8VA8D3iNCcrsNatXtJquu5voUT5xzMI_4vlNxJ_-bVNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32baad9c73.mp4?token=MRNKq4tml2eeQwkjif_DbQMTklFEoaGOYKcLw1M7YuNzqeP8Oti2FDRdryNxWNVf6EyY9ZFEiyh1VFBUpi7Op3MTJSet6htvn06oACUYbwJdARzBqB4Qzc6BS_OZNgbwujFl0bTEcyFlQSB74Y5amHKTAhEafFWmzxR7LK33prCO2DosrGv6kHVIaKAnul4O7jk_OAxsWEfQXUEKjNmkq7wzf6i1pC5ltj-Yqm6PrGnsAI-01t7hqUfm_gKmtrLtq1SCGR5XiAOPHMjZ8FQbpX86Fqpnh4tGP-lpcdX3iB8VA8D3iNCcrsNatXtJquu5voUT5xzMI_4vlNxJ_-bVNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیطان زرد: به احترام لیندسی گراهام فعلاً درباره ایران صحبت نمی‌کنم
🔹
مجری: آیا دوباره با ایران وارد جنگ شده‌اید و چه کسی تنگه هرمز را کنترل می‌کند؟
🔹
شیطان زرد: به احترام لیندسی، در مورد آن صحبت نمی‌کنم. ما دیشب خیلی محکم به آنها ضربه زدیم. ما دیروز توافق کردیم. آنها داشتند همه چیز را رها می‌کردند و ناگهان، به یک کشتی حمله کردند، واقعا آدم‌های مریضی هستند!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/akhbarefori/670283" target="_blank">📅 20:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670282">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800df09f03.mp4?token=C5Dn_vPfGMFo8KXpGCF7o6pvhgkNS_G5qdHeP9n_8JtSKGE8hmMLKBhlHqiN_xOIEYy2JuV4_X_pG-Rwkl-odTKBHY-V21CCTuwk-sVe66jzK-I0Ua_7P0DMNa9sGiSCYVW0gRigickPLPigdB1KXMOeZEoadGlC2Fz4FlPedY4woVJH-ta4cY66UrwqD9uMonAjPXh08tPbk2uN-0cEmpXRq-HM9BnX4l21DducP2X8i2sc4F0_9xbrAc47TDMCZoT3oeCqp1j1hGf0QCD32C3v0XerDntjPf80j0D4X7zfuTYrRIlF6pj67wD9thjhFj7uw8vbdtt7mUQPju6Fcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800df09f03.mp4?token=C5Dn_vPfGMFo8KXpGCF7o6pvhgkNS_G5qdHeP9n_8JtSKGE8hmMLKBhlHqiN_xOIEYy2JuV4_X_pG-Rwkl-odTKBHY-V21CCTuwk-sVe66jzK-I0Ua_7P0DMNa9sGiSCYVW0gRigickPLPigdB1KXMOeZEoadGlC2Fz4FlPedY4woVJH-ta4cY66UrwqD9uMonAjPXh08tPbk2uN-0cEmpXRq-HM9BnX4l21DducP2X8i2sc4F0_9xbrAc47TDMCZoT3oeCqp1j1hGf0QCD32C3v0XerDntjPf80j0D4X7zfuTYrRIlF6pj67wD9thjhFj7uw8vbdtt7mUQPju6Fcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از مزار رهبر شهید؛ رواق دارالذکر در سومین شب بزرگداشت در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/akhbarefori/670282" target="_blank">📅 20:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670281">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
صدای انفجار مجدد در بندرعباس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670281" target="_blank">📅 20:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670280">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
از غفلت تا تحول؛ روایت عجیب مردی که مرگ را از نزدیک لمس کرد
🔹
00:10:00 شرایط و حال وخیم تجربه‌گر بعد از تصادف
🔹
00:19:00 همراهی دوست صمیمی در داروخانه‌ها توسط روح
🔹
00:31:00 تغییر نیت حضور در هیأت قبل و بعد از تجربه
🔹
00:37:25 خدا و اهل بیت تنها مسیر نجات انسان‌اند
🔹
00:47:50 توصیف جامع و کامل مقایسه اینجا و آنجا در یک جمله شنیدنی
🔹
00:52:10 چاپ کتاب تجربه نزدیک به مرگ تجربه‌گر اسپانیایی
🔹
01:00:00 عدم قید بندهای دنیایی در عالم معنا
🔹
قسمت سی‌ودوم (به کدامین هیأت)، فصل چهارم
🔹
#تجربه‌گر
: علی فضلعلی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/akhbarefori/670280" target="_blank">📅 20:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670279">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e9730b63b.mp4?token=TKll5K83lqUhLwV8I5C34X0mus23pfJvMErB2cOQWwzfr0wKoc2GwNbyHJ3_bvYpRCjfFfs_dyVR4iFJjcWl6IugvNJhueF3KZ3al3RVihs-5IIILeHf0ODidTGXLXf_0ELLJEOEV4ptmypTfCHRQfhZBeY2YSNyUXxPYMZMRSy3vfRGzFDpiSx5bw3XnSg3FdoKc0EoPW8F4mNi3FR1f9PriKhmOw45nbFwV_ywlm4lH66aibC2A35G5w9rDRQ3nXQE91VfPTD6sMwecnXGU4nCKpmElroqxSUzsDI1UZckVuzKY85RVV7BbkN3ONKzPnjmERIiVDIzj98HRUjFPFSA00SVkg2O0ZF1lYhdsloLHRtZaeKqTMvGpocoZZMnFYuTzY3kPAjRBOuOfvouGntcaDZhvEwpAWt_haXSmUEVHBGMM5qWI6cNv6wGQMtrUGFJNxaatNEM_luizBddAr8uZSlxv_jhN6YAR8SVQK2eAd0HGxzqpQEnoTocHBFm3Xv-9yTe_kWDO6EnAcDTP4GJezvP-9_SwrU1P_RtKkGjcIhqKNkFJ0t5fGMQcqrkQxHBnn3_6zHsbCG0k8L6nnL85kJd4Nijixgj8wDvluxWXFCde1gezzGxutSz8cjtdWaxZ_q9PF6n3E3xl-yjjb1yqHB0tugQTBe46mzO4PE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e9730b63b.mp4?token=TKll5K83lqUhLwV8I5C34X0mus23pfJvMErB2cOQWwzfr0wKoc2GwNbyHJ3_bvYpRCjfFfs_dyVR4iFJjcWl6IugvNJhueF3KZ3al3RVihs-5IIILeHf0ODidTGXLXf_0ELLJEOEV4ptmypTfCHRQfhZBeY2YSNyUXxPYMZMRSy3vfRGzFDpiSx5bw3XnSg3FdoKc0EoPW8F4mNi3FR1f9PriKhmOw45nbFwV_ywlm4lH66aibC2A35G5w9rDRQ3nXQE91VfPTD6sMwecnXGU4nCKpmElroqxSUzsDI1UZckVuzKY85RVV7BbkN3ONKzPnjmERIiVDIzj98HRUjFPFSA00SVkg2O0ZF1lYhdsloLHRtZaeKqTMvGpocoZZMnFYuTzY3kPAjRBOuOfvouGntcaDZhvEwpAWt_haXSmUEVHBGMM5qWI6cNv6wGQMtrUGFJNxaatNEM_luizBddAr8uZSlxv_jhN6YAR8SVQK2eAd0HGxzqpQEnoTocHBFm3Xv-9yTe_kWDO6EnAcDTP4GJezvP-9_SwrU1P_RtKkGjcIhqKNkFJ0t5fGMQcqrkQxHBnn3_6zHsbCG0k8L6nnL85kJd4Nijixgj8wDvluxWXFCde1gezzGxutSz8cjtdWaxZ_q9PF6n3E3xl-yjjb1yqHB0tugQTBe46mzO4PE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیده نشده از لحظات آماده‌سازی مرقد ابرمرد شهید تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/670279" target="_blank">📅 20:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670278">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
استانداری هرمزگان: شهادت یکی از مدیران مخابرات هرمزگان در حمله آمریکا به جزایر
🔹
نوح مهدوی اهل شهرستان بندرلنگه بوده است که برای انجام عملیات پایدارسازی ارتباطات مخابراتی بعد از حملات دشمن به این ماموریت اعزام شده بودند. بر اثر این حمله دو تن از همراهان شهید مهدوی نیز مجروح شده‌اند و تحت درمان قرار دارند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/670278" target="_blank">📅 20:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670277">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/154436e4c8.mp4?token=ULfqu9eIar2SaBg9QSLQhyO69Cp69sYSWaDsiweZmpLrkRH8i-mDd3oyzTG_ffB3K8-67reWWfzNPokVSnIWrHiJRCNmloL7dh6Lt3E5CMrgj5cfPHRCtfNtCdzPJNir2l8QfMs0aKt2StWrlBpDxc5vSax_z9X1TBcuBiDSjG5yDT6caPf6hCepevRdZKUCe1evWbC6Ti8-LbFHvzQLuIOTyjT66901ati3zMc_AzHnUw5LXtor6uGW41K-WgZn23jDc3ao4Baprtsu0KivwBnfn6hJiy3GB8y1WV-_spANU1rzAmEEOwtBtOALf2G2sGSB7lXr7jIve3TqrW85ujUCgvYuESVo-1rCfQDEtpPilvNS70n5mH5wD6-N_lnvACAFn89JaeQf-C5XH10_wSZacip0iwaq7kIHp50B_ZfDhpPbrALJA556g4SA-LBSOFFOclBPlddVZ8qBS2pK39lNCHjPEPVfSGQJWFghFh3heuQaMDJx5oW9vpUubYE6mBTBsJ1LPMOsE7uDzLyORzsVLkso0HA_mKTvbsKfbElV_daBcBxT4eNlNp9Shsr087g17vz08-gihZ9J16-lMpqokktZgZmtootl_XgfLELmWm3Kb0DQv7aJ7O38qEQC3UKRT8Jayo9docwU5uxKLPrg8bUBm5UlI8KhwqZaelU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/154436e4c8.mp4?token=ULfqu9eIar2SaBg9QSLQhyO69Cp69sYSWaDsiweZmpLrkRH8i-mDd3oyzTG_ffB3K8-67reWWfzNPokVSnIWrHiJRCNmloL7dh6Lt3E5CMrgj5cfPHRCtfNtCdzPJNir2l8QfMs0aKt2StWrlBpDxc5vSax_z9X1TBcuBiDSjG5yDT6caPf6hCepevRdZKUCe1evWbC6Ti8-LbFHvzQLuIOTyjT66901ati3zMc_AzHnUw5LXtor6uGW41K-WgZn23jDc3ao4Baprtsu0KivwBnfn6hJiy3GB8y1WV-_spANU1rzAmEEOwtBtOALf2G2sGSB7lXr7jIve3TqrW85ujUCgvYuESVo-1rCfQDEtpPilvNS70n5mH5wD6-N_lnvACAFn89JaeQf-C5XH10_wSZacip0iwaq7kIHp50B_ZfDhpPbrALJA556g4SA-LBSOFFOclBPlddVZ8qBS2pK39lNCHjPEPVfSGQJWFghFh3heuQaMDJx5oW9vpUubYE6mBTBsJ1LPMOsE7uDzLyORzsVLkso0HA_mKTvbsKfbElV_daBcBxT4eNlNp9Shsr087g17vz08-gihZ9J16-lMpqokktZgZmtootl_XgfLELmWm3Kb0DQv7aJ7O38qEQC3UKRT8Jayo9docwU5uxKLPrg8bUBm5UlI8KhwqZaelU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای ما مظلوم اما مقتدر بود / دلگرمی او آیه «مَنْ ینْتَظِرُ» بود
ما یار این مظلوم، ما ظالم‌ستیزیم
/
باید که خون قاتل او را بریزیم
🔹
هم‌اکنون؛
شعرخوانی حاج احد سبزی در سومین شب مراسم بزرگداشت رهبر شهید و شهدای خانواده ایشان در حرم مطهر امام رضا علیه‌السلام. ۱۴۰۵/۴/۲۱
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/akhbarefori/670277" target="_blank">📅 20:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670273">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ia49kyNEJLAmcUnC00nGZKV-iMCer0pe-bwsmsmhguGyr9v0cGFYWDmWquvjIyD5f1dhXd4N1cv_gO-O_Q6kNt_RoURmL0BHdbgwKXs-w4r-1GAbVB9Boka2eNT0RdNPMHDpd17ShnzXBUNNYM7bz1qScEedDHjWapHFVcg5zCoBiUN4Ms7dIZODMu6Bu9pzMYZVglIXohqBu0YG5cVBr2o795zP0jYbDDggml-v3PcBaq193Dy83Y2eI1qJmc1SKVBcofgs5pBPyKB3TlUo0ibyQ0hBYAPcTdeMvIqVoWTC6uqJYEuaNfrpcgUyFTK1j2J7-2DMuhl-yy1yLpQ87Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PdEqid68K4S7yMU93A-KVMAAv3eeTsaVo0ee-Qs16qv3FEGKDJIdNWj7vE_Zt5ZNMfvzo8zRqlIkn644DBup5viyOk2eGhkiB_kMebQz4TTV6w21m9OX1cntY6sNHS6S35jdCEyWN0g_FyWkpWwcVxzhMg6zxOYZDKELo9TMqv4LeciUrbNy6qCfdBeVnC96tvFhfkh6QkBJaVqBrS6YyBSnTcPpaT8eJp5UkMCB30p41YLKa-wWjDeW-RYpyo-eQ1yzNEId30F0ukJ93_1PliUxaVduG4jfbyZvtjJhLHj59sA2UGLMGJ2-hIRTW9BpLSUWRjn9w5lYl91Xi316VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODYsMmE4C55VYaQnBwAhkNYzhn7NiypRHGyrcVeoXgcS0G6UWSQ1izE-2oqJ8Q5YROsHB6JgZevXfuEWb0Ufqo1sCAJ9InYfhAN5JNnXPrS9fco7c7uvOglT7QK2Mp9uuS1_KJVK56FjtssqeA00pw1SmANTd1J9ZB7wAsEJfZEDwlLjVXvfYgYb7RiWTyWKzZa1Jwt_Rr9XpszzsM67NaD9FnmJxeSJGoS7XuhxLxIMyZ528dFASzm7t90PXZ4_mobpIfaaD_AItYdBUnyHP0SuboJfKThFdHT2W7nWLqefN1AXZRul5aljRjOpQJIYbpcNjSw6weLClmtwHF7d3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
لیندزی گراهام، سناتور جمهوریخواه آمریکا به‌درک واصل شد| علت: بیماری کوتاه و ناگهانی! #خونخواهی #تقاص_خواهید_داد   #WillPayThePrice ⁩ #Trash
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/670273" target="_blank">📅 20:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670272">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
کویت انجام حملات به این کشور را تائید کرد
🔹
وزارت دفاع کویت با صدور بیانیه‌ای، هدف قرار گرفتن مراکز مرزی در شمال این کشور را تأیید و اعلام کرد سه مرکز مرزی زمینی در شمال این کشور هدف یک حمله قرار گرفته‌ است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/670272" target="_blank">📅 20:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670271">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
هلاکت ۳ نظامی آمریکایی در حملات موشکی به کویت
🔹
برخی منابع گزارش دادند علاوه بر این سه نفر، چند نظامی آمریکایی دیگر هم در جریان این حملات، زخمی شده‌اند.
🔹
هنوز منابع رسمی، این خبر را تأیید نکرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670271" target="_blank">📅 20:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670270">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ruR13Fc_Q0hd9S6ei8OrhB5qOpETAB6BxA5lg8cHt9WM7z6QcGNzd0cM9Um1v2etE86_rz4yW9i-fnWJSUjNvvt-cgMGwmxuwr9YFhTCJiKpiSWTC_NmT7jEVfOBv0zPhp2FHCmUYwwrEfjBfpSpfPlc36w8v8sQwXT-uN9ZStTZJARUHAAJxyiUdDY2HxuISkIxLhHIfPc5UdJQUr6J5crcoj0pfjKGLsi9UOiH1GOv3ujhRlQyBk5Gtij6_8D9F01z0Kv-5rZQPUNKUdX_bOIIZcXuP9DUGSmH3Lmrd8fiX9LPH13CKgonpqf8rVRN3nX00CSveLXQAws-hOSoVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به جهنم
🔹
لیندسی گراهام، سناتور جمهوری‌خواه و جنگ طلب واشنگتن که همواره مواضع بسیار تندی علیه کشورمان اتخاذ می‌کرد و خواستار اقدام نظامی علیه ایران شد، در شامگاه شنبه، بر اثر یک بیماری مرد. گراهام سال‌های زیادی علیه ایران و در حمایت بی‌قیدوشرط از اسرائیل دفاع می‌کرد و در دی ماه گذشته، خواستار موج عظیم حملات نظامی، سایبری و روانی علیه ایران شد. دشمنی او با مردم ایران به حدی بود که در یک برنامه به طور علنی گفت: ما این مردم (ایران) را حسابی با خاک یکسان خواهیم کرد. وی طراح بسیاری از لوایح تحریمی کنگره بود که شرکت‌های اروپایی و آسیایی طرف معامله با ایران را جریمه می‌کنند.
🔹
هشتصدوهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/670270" target="_blank">📅 20:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670263">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpSeKxd4wmIvUpmrHB6F-BO7CxKAGB36EPPVBJev1uQr8ng2eXPICZSATbibMCVGsmvec3YlemzTDsehCBW8ASnnIW3c84NWVh6SVu8qfZc_itiJhH1UZarS4sJ_8adiHUFYM5caQSZeVRgz3LfKBD3ccGyrmxHugTgxr0r3obOuKbMpppwVxARKlrVwT_0lYKiuGlp6MW5lPK8aVrSrOKP1CF9sJyj450crl4hULleHRRPp9LgmMfvxq1W6RTQdtfKXSVqMDVUKnernNiD3JAMy0ZdDBy6QBJ2PiOORW3sYc0elXySABUG-VlPNpuJ26d63Bc0Fmb6jxEWvzJFiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SPqepPumtEPKY63eE3G1zEgg-wG6KLZbAAVKOADfbrxk8EtEUzOmo57Se4UcnyAd6JNiVxZydCUeMIAw0V_nqaVel11Tqkm3g-tP5vY5R3FNmWTIRRLPcBceGPvTivxoFY0DvWUFdR9f5uFKaxfDfPr_vi4P-qbZbLaAEEcbb8-hmXULXcJ59uczL8xGcfEV207nRbQOnlwVTnllvYMY36Y9gzOWp6-mf6wQhFEYMjPtkUgZxCC1knCB_9AzqDmERLQ0mqlQE8M8oNCl3IigBrn_C-XFOYOip-7rCQPCiaIEYjQHo3F2aeH-FW31Nt13aEGl6RG6_VPL643W-mj7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBLKzAChFUL4dibrjU2fzJTC9JuwCJGkz7ikMZPLWiS1dv4gMJYeBpN3sQbBt0FYlvH9RWXdk1PhhYZf7hLiKXbywZLuCWIAgU5BbbA6JrF1mv3vkBSWmnqX5clgy0LCT8SD4piGWU4BVp2FdUyn1o7-cVIdR3QmscG9uB6ZHBMIkR_fKXl_3qumq24Ez-OS1E6h8XC3OGSviKVurI3qMCXm45AvIz4PnIkG1MKHJJXYVwkhI7evxJVQfT6Tc_N4TH8m1zv91EbiZ8zx6yiAfH2P4bDDSXTJE-p44732GO958bQUjXPC8YgdHXlornOhJCRa1f6SlTPPrEVWX9_T_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqr0myXwHyMjvMx6_4iRqke7n7UHzxZaFRFSVhYBpC3vj4qlKDdBwqQnzmCHaFjS1Mp18C-N-jAtYwM7JdwvUK8Wz63SIk5ojLHogvz_c-v2pgqzg3AK5ynjUuJGIXha0Bg7_bdXQlNryWjoK_u3McUzrQ2HFxGyZAZfXXQGJ2WmAEhlu6qCvGYCm1U-5YzyDcNSD8ZtKRuE9xnCeXEgvXmSL2G55pUxizN8qWhs43h14eVwWB77yl3uN7YMbvk-tcqxzlLJHLxIRIWSLT_Ngt5_c-AeK4db4LlameDvuIEjnps6IlZ6luVZrXurjP0flr2Tbr7B5YhjEGnszGjOBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MMdX2E4YRGnzOxJeybnpDxUVnkIuw3bnUJOzGxUxK2IW8gDh8sm_KywrKPx9JFxaSNluHOvSaEz1nayaZSZ5aIKUU9QyDsAd4GHCIdksrRBFbV-K_5P2QYR7C1rnIZwfN1ogd3kTtr10rA9YwKu4Z_HuBRqlAQdDG2dM_3fs0EO7MwkOuJUcVPDYkgjtfDsMzNX-K7JgBIYfErXJeuUN5OjCQi_QdW62uknPdns9H1ewoZcSEj-JgsddkWdgxX6QxitE7MR5u3EqXuwnIjvVv68AeejuPPn85eH6taodsQyFLlctTa4rRiUad84EPriS5rPx-EYDQ4PfJY9k73ULQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IMa5rReHteaa7r8vRaq8yeJ97wHisBwFwAqLPeu1X7ChFAcYxNts016tjWBHtMJr0Q5w7ju3A_ZxRKuYWpBsFcnPsjRGD69XyI98Pg2qd4mnoOMIwNEuOOb-dYkpoqlM35y7aevrn-LkBOzDr-W4UlYHs7C7uQUB7p_aSjsvES6iLQR-vjQyrzqfjVyJRKDdEdGgGVXtQMtdGsnQixlfFRFGeDjqKKXJUc_rrgb53waNi8PIftZHqsHfQ6TXO3caLxrBM2_PQUPqogzPwccwXSLFkXRPWy9Pz97CPEnRl6qvZK_HlwAxgMW-Fk3_8clK_ZDq_IXCFfSYGPnJ3WQQbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avJCphW9jMLnOL4sVK7uiXkwmG3h9WUpWstzWHdlMYeHoku_rdne5FzM54Eqnkbdugl8xFSvmy-xwPZAPyezZMHeJYloyIQCU9kDH51z8ypE07taiAY2Q3XS9QspSuugmQaiIXthPGKUWP85GafRsnLjP4DeX0M9jWAgRp5jD250s1X-Xzz_jsQDMob38NZ7eI2b-2uooAdWpukSd-pIqNzOXlbhg0iw_xHIaAQ2Z8JrVFE5vpIcSovfEYeI2297l-g_5q40l9Q3nuzFdRti-sNMtqw9cP3MxyswtPZg82MkKxaoDLt0TWCeV1wMj22OjUwsBhAAzokVeI5bmSIKgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کالکشن کیف‌های مدرن و گران‌قیمت ارلینگ هالند در جام‌ جهانی
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/670263" target="_blank">📅 20:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-670262">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ColqgToJ0_H7yRROUNunNn5wzkO4gGFha-3Iby5q4yQcOoPTzF1QiIH0gN7NKEjNUadskrmqRJ6rKpeUEYlALOxUgCg1fXy1SFCVpbeVfqNa_7jxvmisRmvcuv1-8wT3fzMtFrpmGaVcCW4VZn92ZEz26Pq-pU4Xx9q1c9imPI_odO2SMXfIhNkRIxqXgHmribL8MVaPs3RzaJkpHnwrWrynqwZOzQmwjBuZ3WQkjXNUYXtWtMKMOPcEg187y_XKHgfgYlNzZtSGaqowYiM72KofLfKKAHOyclg7FzTBlOPLGCQVpisO1uuCBDKECwNGaj3Lr0zast-2f0hnhWfPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم چگونه در مصرف برق صرفه‌جویی می‌کنند؟
🔸
در این نظرسنجی بیش از ۲۰ هزار نفر شرکت کردند که سهم روبیکا ۴۷ درصد، بله ۴۰ درصد و تلگرام ۱۳ درصد بوده است.
🔸
۶۳ درصد از شرکت‌کنندگان، خاموش کردن لامپ‌های اضافی و استفاده از نور طبیعی را مؤثرترین راهکار برای کاهش مصرف برق در تابستان می‌دانند.
🔸
تنها ۱۳.۵ درصد از شرکت‌کنندگان اعلام کرده‌اند که به دلیل گرمای شدید، امکان صرفه‌جویی قابل‌توجه در مصرف برق را ندارند.
@amarfact</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/670262" target="_blank">📅 20:07 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
