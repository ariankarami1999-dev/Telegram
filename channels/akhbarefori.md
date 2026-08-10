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
<img src="https://cdn4.telesco.pe/file/AISTfjBj_wPqBOHU0SBZqdOVDami_CwZ3xI_njsOFyyzxr_Y1SmbENZ8jRcnadOBhR_PN4SHZLb2oVdOlEAs1oqlos-FkDk94Ilx1oOG2g7HnhpbRIfyuhSDUVWTkxm-p8Oz9BwP5oSG14NlDWRiEwMwCWAoBFfiwJJ4ByNHhmRJDZWRMNgDsDKpiw7jV0TigOVapRJYPAXds6nUQ_5iEiLyUDnetGQRT3ZnkxmmenOe0whvL37POgd2QiWJYBmezwoaqLanmG1SoG4LeWlfhnoBxMYPsrA4_0NMXW1jHD4DnOk2PS4Xe8yN8V3pjBZOrSctAl3Os2-x2KWKCq_0eg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.24M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 22:57:44</div>
<hr>

<div class="tg-post" id="msg-680127">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3TFgYaeUaNaX4JCXNIFTAtx1k5Rc-DOWuSBIs37iXHEFU9QoEw7B9phi0Vy0SRKJMM0guOiEv2eJr35QfokP4L4RFcIHHbQEnb79lQC4n7CofRfVGdSuEuqixWX2k-ycBwPqNyM3xXKCamPDe83CFblO0HH_1nKkYF8bRtCK0ZiRedXg0T1YlVJ5IfhX70C1WMoV5AwnMj0WXkHBBkkhRrNe3BoAgLKcKQ0MMaN87VkkKhi_mc96kScp8uyIL0GSVu6v7qrOVwzEQLdHxG_P_xLH4Ay-U06IOSEL6ovV0wAk4VMZZr7KtwRmxBvQAoI3K3u--oz3lxVM2HrjH8QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه ایران: وزیر خزانه‌داری آمریکا به «خفه کردن» ایران از طریق تحریم‌های اقتصادی افتخار کرده است
🔹
این ادعا، فراتر از تأثربرانگیزی محض، گواه روشنی بر اعتیاد اجباری آمریکا به تحریم‌هاست. هرگاه واشنگتن ناتوانی خود را در پیگیری دیپلماسی نشان می‌دهد، به تحریم‌ها پناه می‌برد و هرگاه این تحریم‌ها نتیجه نمی‌دهند، صرفاً دوز آن را افزایش می‌دهد.
🔹
این دیگر «سیاست» نیست، «عادت» است؛ و خطرناک‌تر اینکه، اعتیادی است که جای تفکر را گرفته است. ایران طی دهه‌ها نشان داده که با این لفاظی‌های فرسوده خفه نخواهد شد. خطر واقعی این است که سیاستمداران آمریکایی، با چسبیدن به این عادت بد، آخرین شانس‌های باقی‌مانده خود را برای خروجی کم‌آبروتر از بحرانی که خود ساخته‌اند، از بین ببرند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/680127" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680126">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
آژیر هشدار آزمایشی فردا در جاسک هرمزگان به صدا در می‌آید
🔹
به منظور آمادگی و ارزیابی عملکرد تجهیزات، تست آژیر هشدار توسط نیروهای نظامی از ساعت ۱۰ صبح سه‌شنبه در سطح شهر جاسک انجام می‌شود.
🔹
این اقدام صرفاً یک مانور و تست فنی است و هیچ ارتباطی با وقوع حادثه یا شرایط اضطراری ندارد و شهروندان نگرانی نداشته باشند.
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/akhbarefori/680126" target="_blank">📅 22:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680125">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8ae789ba.mp4?token=IjLUipfISLWvZtMOtTQuC1LuXWdyrSDpmjYMwbzjLmrMLowLCQQsGg5qGCHaw4i8UL9v39b_PB_0nQgnU8iBwQDoTSdvrXWrV55F9_FvhhCcjKZfRN58nzWbwLwxkZiyxTeMnoALJjJNHo-dyLIOv1VafBN0b8KgJ23VGWnMmqgvJclfTifEo3fcbajwii7lZyRUv05c4OE4CdDrl2t_vnfkdYutzXIeLeXa60BksQpq2qdw1dobwzG8TlEWTCEzyCnh0rHHIoBiYerYOd0IghcP9mLME0cgIGbUTZPLr2LY_uH0Gy5uMYRqM6NEQUJEI8l9bDy9UUsTSihQmcaEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرت زدن رئیس جمهور متوهم آمریکا تمامی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/akhbarefori/680125" target="_blank">📅 22:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680123">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
دست و پا زدن‌های ترامپ برای فرار از معرکه جنگ با ایران
🔹
بر اساس تازه‌ترین آمار، ذخایر نفت خام راهبردی آمریکا به زیر ۳۰۰ میلیون بشکه و رقم ۲۹۸.۷ میلیون بشکه رسید، که پایین‌ترین سطح آن‌ها از سال ۱۹۸۳ به این سو است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/680123" target="_blank">📅 22:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680122">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b99cc09220.mp4?token=jotNA5rKibylGlgjWM9D8PB0BPhdBfSU1X9XoCHxQD_RLR0x9vnu1EjHNLG5ZgcchwzHwYu6m_Zl81W5tVB1B5oSgz5WyG76aamhrc2GCiymtDPDJGKTaGtgshHTg8nJY2TRobwC4QVBX0o-vXuxt-Pb0Epdd9ucicf7Ck3kUvdv0ocHhnrguIxCsfwi5Xp93oLmAiHn8UFKNDA29fCYeA0qmmmb3_3stNlDGoP7hws3Qc-AI5XIFiNeYJ7jep5HVYYgZ7EMxvssNNgcGDKcqFQtVCDi3_3QMCeh6f9N7UZ6I7iQT7vgHUX-beAWHPSIlOpXlV7E4G_RFwzA2_l2bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مراحل درست کردن یک شات قهوه به صورت متفاوت و جالب
🧋
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/680122" target="_blank">📅 22:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680120">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc5a794ee.mp4?token=FUSQcxsN83T3024-geM6-5-jp1l3ICZ1BG2PyVotRe1y_c-brwND4oYrwbuRLSdN7hjK3YXwN-dDNtPxg1Dx5ptxrAaDywusp9tZ3UFKhZakwWcD4Je50mX0WhFk9eejsUjdI0V5tze1W4UMpFMaf1aWf0YcfsNQiluMtfv-RfCgjU1m4A1_x93kqMqrUgP_2k5VYplbBUi8xGg0TZqBOAtKJOugP9sfQl-s2Ia6EmE3M29x0W7-PHz0p2H6fDwvRkdrOa1RrTo-owmeF8aFHTWsRFwlXY-Qmg7Ki2LHdjmIX_pZPUBITSevLb93NI698Qk2wFuFZPo9ZT7DxtRv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پورجمشیدیان؛ رئیس ستاد مرکزی اربعین: هنوز شرایط حضور زائرین در عراق با خودرو شخصی فراهم نشده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/akhbarefori/680120" target="_blank">📅 22:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680119">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cf02b7944.mp4?token=Plh26WTQuO-JE51FaHOa6hl0PScT-mjpvnD3rpHEB5uQK3Kh5unWIQYKuM_S9eDopuBOTMFwucogMpRxTd2qDwk_dZi6Am7zuGxP6OJdlUorZJns3a24f4vWMla0vzf-gAyx0isWFh_mMx39oS-qfCJV5Z7M8jsZ14keCDbXwxZOwT9SqXpG_dJ615egZHCNF9wGNamE3z91zpAdWVSk7pUGVdS9unLePkmrh0jlrzRsSAF92sWiV8l2vX8dC2bUzHJTKhqbYRyPMwDa66tTW_bWtrMa-aZKSCU-WPD2Zh0RUBh3_iQKyi6HN5FonLnv218KpQ12Q271GwUV9_1aQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد ۴ تنی با ماه؛ فالکون ۹ چه بر سر سطح ماه آورد؟
🔹
ماه حالا یک زخم تازه دارد؛ بقایای موشک فالکون ۹ اسپیس‌ایکس با سرعتی سرسام‌آور به سطح آن برخورد کرد.
🔹
این برخورد که چند روز قبل رخ داد؛ اکنون نخستین تصاویر از دهانه ایجادشده، توجه دانشمندان را به خود جلب کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/680119" target="_blank">📅 22:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFd9HswKgN4A9ZK7N8JeVGkXboOF6ptG8ddNIQ_u8gGxrI-JwrsC5gsIueVpvDitkW1Pas0fu_IzrZi7wQ77bDW5ev5gzIyL6Uox889igIf9gHoR33SnEByi8Z2eh6M7YU4gGGXPOmq28wtF4UIVYXBhjCYT0jiX8ItWmQnvScQ77Y_hLgNx6k-jlAcCedBh3KSj28goNcWTNTwrFq_Mc9IXEc8gmrhJXCucWEKfSjtprNukuzjZ0V8zsq61tgi2f1q893maw7kq0uv5LdXW3aQXu-j51Twsg4d2icUAavFgZRxBo6X7N7D0pcez52Su2_zWYMWkwRUYGJLRDsepSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قواعد دیده‌شدن محتوا در سرچ گوگل تغییر می‌کند
🔹
گوگل در حال تغییر شیوه ارزیابی محتوا در جست‌وجو است، تغییری که با گسترش پاسخ‌های هوش مصنوعی می‌تواند قواعد سئو را دگرگون کند.
🔹
بر اساس گزارش Search Engine Journal، گوگل برای سنجش حضور آنلاین برندها و محتوا از سیگنال‌های بیشتری استفاده می‌کند.
🔹
به این ترتیب، موفقیت محتوا دیگر فقط به تعداد کلیک‌ها وابسته نیست و میزان دیده‌شدن، اعتبار و حضور یک برند در پاسخ‌های هوش مصنوعی نیز اهمیت بیشتری پیدا می‌کند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/680118" target="_blank">📅 22:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رسوایی امنیتی در نیروی دریایی انگلیس
♦️
شهپادهای انگلیس داده‌های خود را مخفیانه به چین می‌فرستادند
تلگراف:
🔹
داده‌های شهپادهای نیروی دریایی انگلیس به طور مخفیانه به چین ارسال می‌شد. با وجود تضمین‌های امنیتی ، دوربین‌های نصب‌ شده روی ناوگان شهپادهای نظارتی انگلیس حاوی قطعات چینی بودند.
🔹
تحقیقات نشان داد که این دوربین‌ها سیگنال‌ها را به یک آدرس IP در چین ارسال می‌کردن، که وزارت دفاع  انگلیس بعد از آگاهی از این موضوع اتصال آن‌ها کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/680117" target="_blank">📅 22:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680116">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
موانع واردات بیشتر شد؛ انتخاب مردم کمتر
🔹
واردات خودرو که قرار بود به تعادل بازار کمک کند، حالا خودش به یکی از گره‌های اصلی این بازار تبدیل شده است. جزئیات موانع تازه واردات خودرو را در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/680116" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680115">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29d40ed29a.mp4?token=NB-u-HgocqGIp8_VOsyRM_8GS3JBKP75Nnj6Outjb9TR8q3aO8z3a_jY-ONDU5rqBO9Y25c92NOUcmlKFkg-HgPJuD6ZwLmnPYlKu3l48E5qsCQyPjs2HVh1VrwJ1ydRBugcaJ47GVGSUC8pgHgfJFz4VsX_kGM7f8xRLREKGF6Cli5QPUQXMF0Q6ADg58-RXOJqvMFk8PEcj3P-gx2B5CRqaSkilWcIyN5om2AEuU_gLcQrIsC3_8NXrvGGHKQ8oB--vchfdIIQ9LEzw3Za-aMBtZki5PbDVH3R1gDi-XImlWA27Q0Xsa0hCSvYxZzUDXf2Z2gkXbESPNPjDgAiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29d40ed29a.mp4?token=NB-u-HgocqGIp8_VOsyRM_8GS3JBKP75Nnj6Outjb9TR8q3aO8z3a_jY-ONDU5rqBO9Y25c92NOUcmlKFkg-HgPJuD6ZwLmnPYlKu3l48E5qsCQyPjs2HVh1VrwJ1ydRBugcaJ47GVGSUC8pgHgfJFz4VsX_kGM7f8xRLREKGF6Cli5QPUQXMF0Q6ADg58-RXOJqvMFk8PEcj3P-gx2B5CRqaSkilWcIyN5om2AEuU_gLcQrIsC3_8NXrvGGHKQ8oB--vchfdIIQ9LEzw3Za-aMBtZki5PbDVH3R1gDi-XImlWA27Q0Xsa0hCSvYxZzUDXf2Z2gkXbESPNPjDgAiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سنج و دمام‌زنی اطراف حرم مطهر رضوی
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/680115" target="_blank">📅 22:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd1qbGTZiDL7SVGPZg46lrMVQ-ey1-1xzRdhiVODCRKg-Sse3tD8A_yaUsiE7WEWHlwvd4ufggmrFluEK1vhUSevgVos6x1nOFb_hYswT33pD6FoirJRHjxbncIuitwcTKNo567eJWyd1aJweQEiWOykTozyFtUtvIyj5EvdtpQSQfeSd2DrF6GXfkSxa8PYDueZ3g4K_OA4tIt4AGCoA4w4SeivVkfQnhT36_GSGwgPnV7rFvetcOYqACrLpGONmGgZvAt6vP0sU-VSfjuY4cdHl2qWMy73CSSYWdCkT-zEwxTUc6QN0693R4k2Cb3lEFcc9snhYLPrdSVBXz4UFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خردمند، پیش از سخن گفتن می‌اندیشد
🔹
امام علی(ع) در حکمت ۴۰ نهج‌البلاغه یادآوری می‌کند که سخنِ سنجیده نشانه عقل و پختگی است. انسان خردمند ابتدا حرفش را در ذهن و دل می‌سنجد و بعد بر زبان می‌آورد؛ اما سخن عجولانه گاهی در چند ثانیه چیزی را خراب می‌کند که ساختنش…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680113" target="_blank">📅 22:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ob30-pJvwmZqRcbNWnccrl1tHvhMlliN6JHH8IgfcLa9x32iQ8MktvimSDqidflEkShVdTW_pok1hOzsMd3w3fhhAH9RYfqE0e3OnH_R60H4iiCsok9QkMuqx5Iz_bvISaDtQbRWN8CFasP15A5TxQSPYj5xfzPI987cD2uC35TYGw-D1ievNwmmmQEpBf75qYLDYZfYX7LEUhbUajmVyZ8YAOob7XNWbnzGKWnW-hzx_mdE0Sv5oEYAF45S7I2IbBGNhy_9lDvJXlgVBksmiCfBTJBBxq6S2ktq-epZ9Y5I2-otUd3sf47q129hYzayrud_7brpQxdO4ShOGtW8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خوراکی‌های مفید که برای استخوان‌ها خیلی مفید هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680112" target="_blank">📅 22:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4143c1388.mp4?token=DnqSrIZX9UaEvLKYbHh-1kxw34_voRw0vCFeQSSc8fufU9rSLj_276he5G6Ct0itDLpqb79wGxgTMOqkXeFzo75LHcw0oAuWoTgQgHZRD90h96eXIeJiXhUkhTcjFNEOCFjq5i5qv7-r3DYmybU-j7Qr6pU7EHToCNLOhtiulJOLvy2eLKcbip2MVmlrZN1bIQ7qFiD-ELhqZp_oOJjtIw4nlibx4dsRu3QRiyi6nCpmkf3A_J8Kp1VbJbbb3NfgEJwoYzqB3NzKfPNoGOwgjVcE2fAm-XScBSCpRgiMe99nWOrFsc_rsY7jBOCxfS5PbG_JK5uaBjR2xB7B1-GekAqhaop5gAdsm7e8ZkX-42_nPxADOV6yzclVVUeHMf8KfaoXqKQduPHyw7fCQgTgAUyEyLAeDwJqmAXIKRDVkqvGoHJAH_vF5pw9KGRwIqOa4y9Zprg-Wqx0nm8jYVda-Ct1PAP0hOcGCiew3s-jdV8nzeh4b4jRBrIX8vpuQMk2bnI-OB00usYVnsO2Gr8IFAF7f3qRzEfKKhhiHgrQfV45CXbU36_Hw81RzgOECU-MkXORgGTWEOPIp3OWXvIxaWyjZ3HsfH8yWQLtG1tTExNaSt35tXHdV7bByqcK8JvWvQ0tuhaOdJisOiE_DgVFSkfoIPEGTZCaujgYmO52RTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: حدود ۸۰ درصد واردات کالاها به کشور از جنوب انجام می‌شود
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
درحال حاضر حدود ۶۰ تن کالای اساسی نیاز داریم.
🔹
فردای روز تشییع رهبر شهید در مشهد، راه‌آهن تهران به مشهد مورد هدف قرار گرفت که کمتر از ۱۳ ساعت دوباره شبکه ریلی را به مسیر آوردند.
🔹
با فرض اینکه در جنوب محاصره دریایی شدیم و نتوانستیم کالایی جابه جا کنیم، به راحتی از شمال و کشورهای حاشیه کریدورهای زیادی داریم.
🔹
کریدورها نیاز به ساماندهی دارند و میزان فعال بودن آنها کم است مثلا با پاکستان خیلی محدود می‌توانیم کالا ردوبدل کنیم.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680111" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2xLDNbyX_9cVouc_H9yxkx5Rv4qdSswXSYXFJ9N-GI_oNGSBViAHnZQP6Up-o_tCiPnlMWO9oQE9QeBQ1aYSu0DKsQI95NwHLBtAm5u0qofu1jDW4o9vt4_Q_mArISf5gmHRnysu2NSk9AbH9pZSfem_gShX9VhkFm4OVAQ-PmC6hZkB1y5kxpvtEqYO3fl6i-3cFtqLjomSblYVHWyE0q20ZeveOVBg-NI2qIzmtGZ3DdbM2Y48su2nMyiuOnjPvKTw8mlUl8W-U3kbQSGGCoSlv-ddiCdpEF-NJ83T3YCvolw-XuiqRcZLwjMU--PTpu-yrxAT7UVqTeeTNrtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📢
خبر فوری برای مالباختگان گوشی در سراسر کشور
🚨
اگر در ۳۰ روز گذشته گوشی شما در ایران یا عراق گم شده یا به سرقت رفته است، همین حالا از طریق لینک زیر سریال (IMEI) آن را در سامانه همیاب۲۴ ثبت کنید
تا فرآیند ردیابی و اطلاع‌رسانی کشوری برای گوشی شما فعال شود.
📲
ثبت سریال و فعال‌سازی ردیابی:
https://hamyab24.ir/l/nzw
https://hamyab24.ir/l/nzw
⚠️
توجه: اگر گوشی شما در همیاب۲۴ ثبت نشود، فرآیند ردیابی و اطلاع‌رسانی کشوری برای آن انجام نخواهد شد.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/akhbarefori/680110" target="_blank">📅 22:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=eeO4PcliHCA7d5oJYv95k64MjBorPGcEu1INvAPdT93IeMFtvUb2DJ211pmBvbAvdpTSO6yagw5Q02V0--pXBfwIvM8Is5WBGDgdpNjDZwuZ8Zku36G2rsmFXLZmVf7Q6xXMt9vRJ8DEQKOGT-lFGEqySz9T_JsEpezhPitKWNArisscFuF_6QiF0G257UdTAizseYdqJ_dh0mmD8txYb5qZxYMriFmFn8QRomVuRKrdaGsyBfXf9zUeqdd9KF66kz5mkP5vCWBvz-4v3KE3Bd5Yqp27cs_C0tksjXYYXrPmgRxwsjhK-QYKZGNnbFLujTTG9URb3gK4uqKvM1roTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/658af79ef2.mp4?token=eeO4PcliHCA7d5oJYv95k64MjBorPGcEu1INvAPdT93IeMFtvUb2DJ211pmBvbAvdpTSO6yagw5Q02V0--pXBfwIvM8Is5WBGDgdpNjDZwuZ8Zku36G2rsmFXLZmVf7Q6xXMt9vRJ8DEQKOGT-lFGEqySz9T_JsEpezhPitKWNArisscFuF_6QiF0G257UdTAizseYdqJ_dh0mmD8txYb5qZxYMriFmFn8QRomVuRKrdaGsyBfXf9zUeqdd9KF66kz5mkP5vCWBvz-4v3KE3Bd5Yqp27cs_C0tksjXYYXrPmgRxwsjhK-QYKZGNnbFLujTTG9URb3gK4uqKvM1roTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقوع انفجار در یک مخزن سوخت در لیبی
🔹
منابع خبری گزارش دادند چندین انفجار در یک مخزن سوخت در پالایشگاه الزاویه در لیبی رخ داده است، هنوز علت انفجارها مشخص نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/680108" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680106">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d62d01e2d2.mp4?token=NDMTicVo2Wg4PWWUiOD9SKbj02hQiaeL3j-SV374WdKh34v_UBY6X5mP9__rtX7AUIFeB7g-WYPKsEIfMS19hC747uR37uq6BfJhNQvIeuQ_P2LCYnNmpF_csO1IdLhJWtbILpPtLN7Xn59iSPKYiMYXhEW5Tgf5tU3NoTAz0pmYxrHUMUmSgCVslkmoy96bnR-cuGY43MPnYD1gSrf-w2RuPu_JwFlHaZ-uA-1NI1MoERJVN7zrN-rKZoIOIhJCjtzx-NkwdgAeyGnf21fZWBlgHtRDD2cukQEXnsCwBRNEk7xVxUVO9KhsJYpCLxT8Fa2mOLnZP046_OoNFjo19A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میگ-۲۹ اوکراین سقوط کرد
🔹
یک فروند جنگنده میگ-۲۹ اوکراین در جریان یک مأموریت رزمی در منطقه اودسا دچار سانحه شد و سقوط کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/680106" target="_blank">📅 21:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680102">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
نظامی سابق آمریکا: روند خروج ما از منطقه آغاز شده
اسکات ریتر، نظامی بازنشستۀ آمریکایی:
🔹
ارتش آمریکا بخش قابل‌توجهی از ذخایر موشک‌های دورایستا و مهمات دقیق خود را مصرف کرده و ذخایر تاماهاوک نیز کاهش یافته.
🔹
در نتیجه آمریکا برای حمله به اهداف عمیق در داخل ایران با کمبود سلاح‌های دورایستا مواجه است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/680102" target="_blank">📅 21:52 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680101">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca3fe4fef4.mp4?token=Z1GyQ6EgwRszSFAMR7Xm9BuYJC0LZdzhWc0kpw9MxTYWvKkcoSkzEBTXwG4SMZOe02YfHgefvzeJmrURXLZn21CQKxrUhAZ5gyzYIQFXyS_ax1nUe9j-FVvcFRCWbBSntbt4r1BIZtU419Ne4bvyp9OvdlUV7UPltwKKTeRuXkezzGWSILYuduiv8zBG9sgtiv2_69Pzi3sHJ92dbFXDN1MiyGZIku8mPi-Hwe-pxwlsPDfX3o_OEQ2UxQxgmJ0XSQ1_WIu04HQSC_o4MCOB7fG7sDItuZzA8aNRUgGOm8Iov7mvk4EzfQRCd72hNxQuF88hfd7enJy3G2oIFQjPXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی پزشکیان و حداد عادل با معادل فارسی پازل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/680101" target="_blank">📅 21:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680100">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/680100" target="_blank">📅 21:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680099">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
ایران از اوکراین غرامت خواست
ادعای شبکه سی‌بی‌اس نیوز:
🔹
ایران از اوکراین بابت حمله مرگبار به یک کشتی ایرانی در دریای خزر درخواست غرامت کرده و ادعای کی‌یف مبنی بر تصادفی بودن این حمله را رد کرده است.
🔹
در حمله ماه گذشته، یک ملوان ایرانی جان باخت که اوکراین بعداً آن را یک اشتباه اعلام کرد. از آنجایی که مقامات ارشد اوکراین به انجام این حمله اذعان کرده‌اند، تهران انتظار دارد کی‌یف غرامت پرداخت کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/680099" target="_blank">📅 21:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680098">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxwBP_f_oWe2GyoTqLv0MC88WXTiXUoYyTn-IlmPFODLO0pje2UcK4ahGD-Wnv1zVNVLvBtiSE4gxJbypZH523w8gz9CBICrleJqpdXTK72Qkgoyw9CWtuzuNN0gepfvLxeK0sv7kEzNXDcirsvyVJSsY4ZvBtF278vulzyIP7CNaIbC69MQ_luFQ7ChGAw6GCopVCSTNZNcczMtzTx0cpfAIji5lBStgi-3RKkHIGtFmo83M3tlcn9QN9i3wdHmVNvUHjYjNOMxM1CqM5UQ6BPdRY2u8ThtR0Sg6QltBodSueIqyULaCgD1K0dTU8_5DSf1pFdWxCUGJ7TtugAqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش مراقبت سلامت همگانی در کشورهای مختلف به چه صورت است؟
🔹
مراقبت‌های بهداشتی همگانی بیش از یک قرن است که به اشکال مختلف وجود دارد؛ آلمان اولین سیستم بیمه سلامت ملی جهان را در سال ۱۸۸۳ تحت نظر بیسمارک معرفی کرد.
🔹
امروزه، کشورها از طریق مدل‌های متنوعی از جمله: خدمات درمانی ملی، بیمه سلامت اجتماعی و ... به پوشش همگانی دست می‌یابند.
🔹
ایران از پوشش گسترده سلامت و شبکه مراقبت‌های اولیه برخوردار است و خدمات اولیه در شبکه بهداشت به‌صورت رایگان یا با هزینه بسیار پایین ارائه می‌شود، اما همه خدمات درمانی برای همه مردم رایگان نیستند.
@amarfact</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/680098" target="_blank">📅 21:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680097">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قیمت نفت همچنان در حال افزایش است و به ۸۷ دلار رسیده
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680097" target="_blank">📅 21:38 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680096">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEoqro6qUKyWAGMtEgEagdjv67IS6EjkrYLVCtfDiMpvauQsU_SyeeMAOlGofSrqvCqZIlQMJBXY-cICW1yWXencakF-15v8Bgkyg2SR38bxAu6qLv7KBvvKjGjRCwl8YUikorRVYml-eGEjjoOESqP4dv_Uas8qiFawxNC9IC4iSy3qPOXLNmfQyECdATefqg50jw_RJcywGXduG17pLdxuNlDdrvKX33MQ7NFwZ6DaGIgIcB-5XOl_ZzCVJ8mfYqoc2gSll7LxxoaPzxxQDzgyy7HbMltMo6d0D-TzwxC67vdzSRk2214yvZqcYOPJmdH_gVr5YEwoMsurZKFi7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ به نقل از یک مقام کاخ سفید: ترامپ مهلت اجازه به کشتی‌های خارجی برای انتقال نفت و سایر کالاها در داخل کشور را ۹۰ روز تمدید کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680096" target="_blank">📅 21:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680095">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44abb3be14.mp4?token=SqK5rbYRvAMHVrINiJPKQIwudc5hDZEGfm3GBOiWb8RAr7wFF2VCnKWcqB-6_HMq3A-dlcc2qLbz_nv69F__tJ1y7r-pSXrIucj2HK1zIuhrt7-HCG-yW8xJR5ZxnGP-tKAO334dPzAwcgfK0TgVzqY_FG6hE3pkMeX5P3TcFd-ciTzo0azoAgIiyLWn_e8CjqrVhGHUMhyOGDDbnFIVY1wIoZXAmqpLPmIAWsFKVCmYoHqwqRy9FzW5R9nDRYlC2sBYl0t07TtHgeO0fxA2eddn8wTf-HPpAIzgDFdfKRUV7-WUrtW37LHnEc7Q2-4M2HRkzXLqe6hSIZrpuDhnYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برخورد هواپیما با یک خودرو در فرودگاه میلان
🔹
یک خودروی خدمات فرودگاهی حین مانور در فرودگاه «لیناته» میلان، با بخش جلویی بدنه یک هواپیما برخورد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/680095" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680094">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc830b3a13.mp4?token=mTHjpa-5tnOs2L3vA_YLI296Q_qtCueBi2rdv_Horbmi1y-I8HRQGzA7I7V8kvu9jVFDLfineXpPFkjlnrtUfoFvP_CZrfsdNwpE8R6uCMTMnf5fkVa7h_7Hr8OjUF0IFckPdLBEYwPVrzqa7AZLOKPFL4WbKEMePby7w3Y8o93olDwjZ9tN5tgMBTXMvL0pDCB_Cu9tXcYZHp3Z0pC5WqYAmatUKgFoHadvr3giXEr2sw_cdG5sHEU--PVkWm6HbDkPv-T2wHYhennn_rCBHtLMlzB8zyHmnA3ijqZ1wxC2bTCjso-EXUQU1tNBpLiia8KgX7VgI3E8bkzjkRmTGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی مرعشی با ریش یوسف سلامی: بهترین ریش دنیا رو داری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680094" target="_blank">📅 21:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680092">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyD20qz43MkXAT-uVOQEWhg2te0FqavQncLyjfTD5O7hMubftQBgVzyDBFy2-8LQkOH5s-X0GtedJzkKkrexA3-oEbqjAXqTGbJg3DbVEannyDIvsUk1Ujr4PIzM152l2LGf8sKRaa-9p51XYkNcUOouS1LuplU5bbb8ghgpAOO4l5alQSn1tp5rpzKXZ9beEB524tkGGTAQ6qdTv-stCfF_iQ5thj5Oq3pdFjSaSOSvT34KgGOOdwhD5yuq3TVNTxRHDxlFP8ZcllS-i6VRSjrOTkGoMZ0CFQb1X_ljCXWVNyjBm1pqKjLn2on72AqVXL23MlFspdMZE_7o5SEs0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
متری شیش و نیم
🔹
کارگردان: سعید روستایی
🔹
ژانر: جنایی، اجتماعی، درام
🔹
بازیگران: پیمان معادی، نوید محمدزاده، پریناز ایزدیار، فرهاد اصلانی و…
🔹
خلاصه داستان: یک پلیس سرسخت در تعقیب یکی از بزرگ‌ترین قاچاقچیان مواد مخدر است؛ اما این پرونده خیلی زود او را وارد…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680092" target="_blank">📅 21:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680091">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رادیکالیسم؛ پاسدار اصول یا مانع وحدت؟
🔹
این گزارش با نگاهی تاریخی؛ جریان‌ های رادیکال و نمونه‌ هایی از تقابل میان جریان‌ های سیاسی را بررسی می‌کند و در ادامه به این پرسش می‌پردازد که در مقطع حساس کنونی، فضای سیاسی کشور تا چه اندازه به وحدت، گفت‌وگو و مسامحه میان گروه‌ های سیاسی نیازمند است.
@TV_Fori</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/680091" target="_blank">📅 21:26 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680090">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxhi3rPI1B9QFJ7BjZhG0eHdCxXqLAp2j2uKikjsJe3kvaZN_MUMsehSRFtZwaTkYylhw6QWDaUpK5gMRaZOr4T9C3-O1WZmQFd_weEQtF6GQyI0pu_Ses_DTxo3r0Jc40N203mgtOYTENsTgSd2TpNRADWUZvbjAFlPc-GYOf5BgHSkaQsEIub4rjm3eKHF9uJfFirwyI3hbWgUZ2fncpr6sz_v3X7lS4UTNhXp42EsVgxM_M_BIX0voS2DqEDYo73OOulVrVsD7UL-ZTABVaYgyddkS6xKnIWnh3je6nAqMVJaxEoEbVfFKhjN7zUf5ZuOrBNfcfuWcYPvZoHUng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت همچنان در حال افزایش است و به ۸۷ دلار رسیده
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/680090" target="_blank">📅 21:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323c86efd9.mp4?token=f5FjRX7WDVkzRbKBWtjlNoGC0AmKlQOfypY0W2Oya0_9oaS-Mcv7NkJN0LGjTzpTI2iQiC2kIIIym7DnFOTFoPDN631d5pwTWsSYGJs5fecJJVBrQvauVZoURRjjQ9TTorQemNOGTeT9EqaiaJLm1EMWeT4sPXUP-WNxte1p7hWOe5GB2GLR22Gva46jjai3YVXJe8rSOeQlqkX2HyfFvp1MelWwKFQpyX9ca2LQIWluH28LCXxE6Z8y427gb2dpb7Hn14kyrpT-TO0tH2n1V2hT7G--nKH_F9-zPpsWphG-4vBxmy6jGVIrwuEWEVG47zClbNl0-aYTMAuPdHWS_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323c86efd9.mp4?token=f5FjRX7WDVkzRbKBWtjlNoGC0AmKlQOfypY0W2Oya0_9oaS-Mcv7NkJN0LGjTzpTI2iQiC2kIIIym7DnFOTFoPDN631d5pwTWsSYGJs5fecJJVBrQvauVZoURRjjQ9TTorQemNOGTeT9EqaiaJLm1EMWeT4sPXUP-WNxte1p7hWOe5GB2GLR22Gva46jjai3YVXJe8rSOeQlqkX2HyfFvp1MelWwKFQpyX9ca2LQIWluH28LCXxE6Z8y427gb2dpb7Hn14kyrpT-TO0tH2n1V2hT7G--nKH_F9-zPpsWphG-4vBxmy6jGVIrwuEWEVG47zClbNl0-aYTMAuPdHWS_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر آخرالزمانی از زلزله عظیم کلمبیا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680087" target="_blank">📅 21:22 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رایزنی تلفنی عراقچی و وزیر خارجه آلمان
🔹
وزرای امور خارجه ایران و آلمان، عصر امروز در تماسی تلفنی درباره تحولات دوجانبه، منطقه‌ای و بین‌المللی گفت‌وگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/680086" target="_blank">📅 21:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
تصویب منع تردد تجهیزات آمریکایی و اسرائیلی از تنگه هرمز
سخنگوی کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
بر اساس مصوبه امروز کمیسیون، عبور و مرور امکانات و تجهیزات با مالکیت آمریکا و رژیم صهیونی و کشورهای متخاصم از تنگه هرمز ممنوع شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/680085" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee69767cf2.mp4?token=qtLNV64RRvBbesdtlraGWLZegLCEz9Uw2HWXc4KriVcv4OHyMEUlDspu76oDgPXjx_GNpJ4G0YjS-Htk1KSy7yr-Lp0kSq4PoSbwAAC1F6by9ipMb2nawzr5jOohRqCBPwLSXJvMe4Wqp1mlF0sLVbQiuSDcviItp9aCv2mn6nIxJf9eRpozxSv-NVOSUBcujTqyGM3201ylDmkIHQxB7bdzet0_8sgILFbWefQ_hdXB25goIO4P91YNPJXLLl5KETBz9eOO5Jz070HS6N_4CPc1gqJJduU0masz9gVf6pjSXfQKnuprrLOWwIFGSMIZaZJWHv73TctyTu7TP_RsxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee69767cf2.mp4?token=qtLNV64RRvBbesdtlraGWLZegLCEz9Uw2HWXc4KriVcv4OHyMEUlDspu76oDgPXjx_GNpJ4G0YjS-Htk1KSy7yr-Lp0kSq4PoSbwAAC1F6by9ipMb2nawzr5jOohRqCBPwLSXJvMe4Wqp1mlF0sLVbQiuSDcviItp9aCv2mn6nIxJf9eRpozxSv-NVOSUBcujTqyGM3201ylDmkIHQxB7bdzet0_8sgILFbWefQ_hdXB25goIO4P91YNPJXLLl5KETBz9eOO5Jz070HS6N_4CPc1gqJJduU0masz9gVf6pjSXfQKnuprrLOWwIFGSMIZaZJWHv73TctyTu7TP_RsxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مقام اطلاعاتی اسرائیلی؛ ایران قطعا تسلیم نمی‌شود
رئیس پیشین بخش ایران در اطلاعات جنگی اسرائیل:
🔹
در نهایت، این یک انتخاب ساده است یا پذیرش کنترل ایران بر تنگ یا تشدید تنش و ورود به جنگی که هیچ‌کس نمی‌داند چگونه پایان خواهد یافت؛ اما قطعا به تسلیم ایران منجر نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/680084" target="_blank">📅 21:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
سی‌ان‌ان به نقل از یک مقام اسرائیلی: در حال حاضر هیچ تاریخ مشخصی برای دور جدید مذاکرات با لبنان وجود ندارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680083" target="_blank">📅 21:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1739212760.mp4?token=IMuhzpL4_RuAqfNE04bKgW7ZH__WjJYVspqczq5Ghk2fksUKmrWFiw_uG6ABS0bWZYnpcc4C8kqK3T7-veuNN_pl7-6sVq1IIoIaxgHpw63Ona1NjVD_6UbTUsA5tSJF6njEZ1Qj7cqjDoF5Im0Rh_3huC61Y_GyvXg2VCcQdbqSnVHHAbowRUhMhGcK_3CayFYZskN4o8t068Z1hNEU3Rsftn54VTcY1coXP2Kp3DN_YhC75Yrg3i3HI6trgoxtK1_qC9h2A7DUcS6Ho7EmWuEWyjnlo7tJTCIeiDIyY3xYFSDaLhBFqsi91ZDLby5yvaVqvD5QTN1ZZfRKwfkN5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1739212760.mp4?token=IMuhzpL4_RuAqfNE04bKgW7ZH__WjJYVspqczq5Ghk2fksUKmrWFiw_uG6ABS0bWZYnpcc4C8kqK3T7-veuNN_pl7-6sVq1IIoIaxgHpw63Ona1NjVD_6UbTUsA5tSJF6njEZ1Qj7cqjDoF5Im0Rh_3huC61Y_GyvXg2VCcQdbqSnVHHAbowRUhMhGcK_3CayFYZskN4o8t068Z1hNEU3Rsftn54VTcY1coXP2Kp3DN_YhC75Yrg3i3HI6trgoxtK1_qC9h2A7DUcS6Ho7EmWuEWyjnlo7tJTCIeiDIyY3xYFSDaLhBFqsi91ZDLby5yvaVqvD5QTN1ZZfRKwfkN5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۳ راه تشخیص زردچوبه اصل
🔹
رنگ زرد مایل به نارنجی
🔹
در آب آرام ته‌نشین می‌شود و سریع رنگ پس نمی‌دهد
🔹
عطر تند و طعم کمی تلخ دارد #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/680082" target="_blank">📅 20:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMB_q0ZmYINo5V9kv7hs5Kmp41HChaKi6FN_U0CDkNxs18RrFx62PgpGIsL5PvAcSY-_tu94E6bKqqwLYWT65EKeF2rXEnjTpp6T1YVRbF-JUu4e3ZTUP86tI1mbq-lpnEm4CGOtHt6SH7rxPZpwh1GfebrTQck6oVime1MNpDi_Q1PcuDb5919puRwZYrDW00UuUNNUaqi5RTDuRoua2rHSxbD28qnRZAzh4-W6gFjSv1-2chG1qbEDq8VAJNuV-LF2jcMbu5Oz5r7R7D5vn2y_lhG6gfkMAj4yfVT5xPnnRowBq_pZ7o4n0JnlPkE9mNOYwdTE3ps64G1rUQa6HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینفانتینو به رابطه غیراخلاقی با یکی از کارکنان یوفا متهم شد    نشریه انگلیسی «تلگراف»:
🔹
جانی اینفانتینو متهم شده که در زمان تصدی پست دبیرکلی اتحادیه فوتبال اروپا (یوفا) با یکی از کارمندان رده‌پایین فیفا رابطه غیراخلاقی داشته است.
🔹
گفته می‌شود این خانم در…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680081" target="_blank">📅 20:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سهمیه سوخت سالانه تراکتورها به ۲ میلیارد و ۶۸۰ میلیون لیتر افزایش یافت
🔹
توانیر: قطع برق پتروشیمی دماوند برای حفاظت از شبکه بود
🔹
مارین ترافیک: تردد در تنگه هرمز به شکل قابل توجهی کاهش یافته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/akhbarefori/680080" target="_blank">📅 20:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2fb02188.mp4?token=gTGJMPJLA5_M2zJ_tvRIe0fbd_evVScPhXZQwcJIWiL65dQInS6xz5vVwplE4I9eRgYSFe2TCyCWqm1TxBReJll2bjtRmwmJ9YP5P3f7qi3mmqGvkLo9CYObFbWuIxnAItc1NbwRXn06jRh8wxUMuLli81I6D0uyGV0W1zcnlkOdl5z6QsuRNrnHChZZeFknXw3tagaonYQz8hi_4g4rDuKp6aDRav6ssVe9wk68dUAHDBxOQXel2GYEpN-JneKyoYF-58J7HfaaSSg_tD_lbSUpWDz5_NZJq-rMFggWTmicItu1yfXqAfxpsNmMCDQbYKmn8UBi9pddT6p7j41E4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680079" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319955d4cd.mp4?token=U2jEAQPSelnBCu7BhGau719pAqk3yAsXs2hlgYtMXGEiAhFgnSaQstUVAJdr8cgHLm27zX_C9SY3ZjtsePbjSNK7ChPBnaj1ViTM8IyFeyUJWlWVICWVNb4nlvP77yc9Tu7f3z5YQvSUP0bUuSd2mN-Lzl5xdbHFmvT2mp_ppEjz9CnfHUhqPnDGSECYc_Be25dj9ZWtqyMc238-BpAao5A0uQtY2Ox9xionYzWWwCE2YEQWY-FFRiAZpNkmdj_zWHxmmvhrC4Y4tC5PKtYF-oTobcBrVjnLY7oN7iEPaR6nP6s2ratqBiuv4xkG2HNixQN6rL3TUjkqmGpSflhnrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار دریادار علی عظمایی به سِمت فرمانده نیروی دریایی سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار دریادار علی عظمایی را به سِمت فرمانده نیروی دریایی…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680078" target="_blank">📅 20:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فعلا خبری از تسهیلات کسب‌وکارهای اینترنتی نیست
رضا الفت‌نسب، رئیس اتحادیه کشوری کسب و کارهای مجازی در
#گفتگو
با خبرفوری:
🔹
کسب‌وکارهای اینترنتی نسبت به فعالیت‌های سنتی، هزینه راه‌اندازی پایین‌تر و امکان بازگشت سریع‌تری دارند و برخلاف مغازه‌ها، نیازمند هزینه‌های سنگین اجاره و راه‌اندازی نیستند.
🔹
با وجود پیگیری‌ها از نهادهای دولتی و حاکمیتی برای پرداخت تسهیلات به کسب‌وکارهای مجازی، فعلا برنامه جدیدی اعلام نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/680077" target="_blank">📅 20:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a82ea307d.mp4?token=uDFuCcP7kvSNC6VIwBBSo2IMNSmam9PVpBIIpuSoAq5N0mCHmzZYLM3QZSpRf7nxknhfXotuEtpSxOpgjh_j2EoP7iLBC8Hof2drx9rDGWlC96OCzuFxJVusOOWoTDNQzs46N5amqrgJAfOcqWkRePMUIOVDzf5bWmZm1ML90udVeWbuSBKaDkqvjqS7zImlQJYayZfkeTOGcO9MwQ_muDbQy29yrVd1daNQtCnVCvRCqEvg5bo2eR0QvCdt3FBeMYS8hG_jkU4mYTvpVM23kGdyk3_A-V79UB1YYBA_TOqu8BKR4GBfuZUmYjj_H-WY_rSHULnmyFABBaRr0nBEbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب امیر سرتیپ کیومرث حیدری به سِمت جانشین رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی امیر سرتیپ کیومرث حیدری را به سِمت جانشین رئیس ستاد کل نیروهای…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680076" target="_blank">📅 20:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cb31addbe.mp4?token=h7IZgaiIH_GloYCpuoSJ35MYQ9ttOyps66XG3OLBawlQk9XuwnBG0JQSAr7V6nfrsnLm-q3XmweU9PbYw4-elZghcylRHrNqFgsfbcreS7UNJMiGdE5cdCKm3-uymcX5yt4Yy5YsSUJOzYZKoffF2S4eQhW4uHnXQVWYOEyqnd8CYa4o0_h23gdPi3PmR8UIC-6gk3HQX8x0DAfy1mMpEFXXES_3bQn9rQGaVUOqahdFpsxWy_OIAfxhD0VW0FnJWx2A-Q_GcVX9Oz45fhcChu_xnu5dI8DehVz00154oPo5naBvj-6hzTp97njkWHp-gLmROLc5t-zKqf50q7dhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/680075" target="_blank">📅 20:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680074">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwYx96E6CCzhnFP0DqKaRjsDQ1EOWeB6crGr2LvlZVIqul3M3NeOtAc7ilFDu6Z8ngPAhKtAoslvVVQklNpQCIXAI9vun-0gTkZi87_-KdMHl68A8fK-w3uFVxvi6Oa4XFiHK-BpSCE134qxOyD7UPOxW0hIoCnijiAqFL2LuqMLn-wrKIr-fZKQ5cS2FHDaTZZF_AFbiV3JRxAwG7zteLI69aKVYMF9mBxWOCvjkL1wLqk0gKNS9RVDXlSzWvV_4qMSEibgOlbv9y3FehlSmFMgaqEUN7IFBda6i-BtjI3DncTNx2Cie-ETm1DAZLk5Nz3QbA5bks2mjiWipmg_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور احکامی جداگانه از سوی فرمانده کل قوا صورت گرفت؛
📝
انتصاب شش فرمانده عالی‌رتبه در ستاد کل نیروهای مسلح، سپاه پاسداران و بسیج مستضعفین
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/680074" target="_blank">📅 20:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680073">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rvPt4c7Y4LLoUhvFAeMcrolfkySdBxXH-TzUbkpI_GSisN40YPOMRcRWA34CmVMY1gpMzTiJFbOjlATc1FVQNQLXQ6jtHcyI6t7IlZHEy3_VTXZtrwmImp3uBt3C_JB8agGpRFhrFa2Xf1e1ASljglKx3_LDwdaG1vlEvKSQG2HwKl6L7EN3yjVX48cagQWQrH1GznNFUdggfltFypZTySY8UZQ-Kca_wRztYnhZRxzQpecGWWe7vdxNUvxtRg30Pw6ydUiVQ3koEo-ymHvr8dFXgNlDueAQqI25mw8rUTof6RCSeZQsoCviEyw-epTPlnvxyQbfPSVY1WGlnV8S3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: ایران قوانین را در هرمز تغییر داد/ عربستان، ترکیه و پاکستان به فکر افتادند
الجزیره:
🔹
خلیج فارس در حال تغییر قوانین برای ایران است.
🔹
ایران از جنگ به عنوان اهرم فشاری برای کسب برتری بر تنگهٔ هرمز استفاده کرده است.
اکنون عربستان، ترکیه و پاکستان در حال تشکیل یک ترتیبات امنیتی جدید هستند که می‌تواند تا حد زیادی مانع از پیش‌برد مزیت‌های کسب‌شدهٔ تهران شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680073" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680072">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وقتی از کما بازگشت؛ روایتی عجیب از شفا و یک سفارش مهم
🔹
00:12:45 صحت خواب مادربزرگ از حادثه تصادف
🔹
00:23:40 هم صحبتی با روح فردی که در زمان کما بودنم، فوت کرد
🔹
00:31:00 حضور فرد نورانی و دست کشیدن به شکستگی داخلی بدن که بیمارستان متوجه آن نشده بود
🔹
00:35:10 سفارش حضرت موسی‌بن‌جعفر برای حق‌الناس و طلب حلالیت
🔹
00:49:50 کارهای خیری که نجات‌دهنده شد
🔹
00:57:30 رؤیت سقوط افراد عریان در دره‌ای خوف‌ناک
🔹
01:03:05 اهمیت دادن به خواندن نماز اول وقت بعد از تجربه
🔹
01:12:00 نیکی کنید و بازتاب آن را ببینید
🔹
قسمت بیست‌وهفتم (حلالیت)، فصل پنجم
🔹
#تجربه‌گر
: سید‌ امید متقی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/akhbarefori/680072" target="_blank">📅 20:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680069">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URZBPHxwuH9LDpfNEOIUd1ZEuK01VGH7CLW-mVxHKVlTD2PURG9LDbRV8MCTgnLNzRZT4TKpMdHXuf81w6MKMJAEBprTF0kBSpCUwx6kW5cKTchCHmVkQFe6ZAkgbtdpNN0BCF1N3C8lfHm6R4qLiHWPhaAtnwowCprPn0aAciENg7CF90SGcVboak4CDVkP7TIeMx2D71AVGx5lJhLX1KqF19uRWF0_hXvFBANWgQzWUefCtMKZmqjunGlt8ummwfMntOg92bnT_XzcCl8RkMU9jG-PRPHLG3-97n4dw-h7IcEA1VQUQNBjmcn6MruFZh2J5KkYYYxXuDa_8KaD-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرکز؛ قربانی اول استفاده افراطی از شبکه‌های اجتماعی
🔸
در این نظرسنجی بیش از ۲۶ هزار نفر شرکت کردند که سهم روبیکا حدود ۵۴، بله ۲۸ و تلگرام ۱۸ درصد بوده است.
🔸
شرکت‌کنندگان به ترتیب: افت تمرکز، آسیب به ارتباطات حضوری و اخبار زرد و شایعات را به عنوان بزرگترین آسیب‌های استفاده بیش از حد از شبکه‌های اجتماعی معرفی کرده‌اند.
🔸
استفاده افراطی از شبکه‌های اجتماعی می‌تواند با پراکنده‌کردن توجه و کاهش تعاملات حضوری، زمینه را برای مواجهه و انتشار بیشتر اطلاعات نادرست و شایعات فراهم کند.
@amarfact</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/akhbarefori/680069" target="_blank">📅 20:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680068">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJXFhi3cX2CgqPNPJOgy00s0sHENr_xYjmGZDOOS75LitGmwU-cl6pCH3k-SILqy5AfMWGig9_f7wDoyq-n_D1kAipILhZNjXrFO-zc76Yu93pniQS8ECZyMtQ4JdzDKS9we5wZbX566Ud7dTZhU1kEHFn7L6bytlxyj_vWo5o6JLYAAC4--RvoBSXvgeB0P5OJgYImG9gt-2IyHSNLInhEH9wg-fSmaguvtkS4QE6oVsCMEFfdBlgSmym4wJ5G-ztwiMAfYe_M-f-TyqFhTKWyasoGYjiIv2eV5VX-kGJgpweWyT4LuzPdAyADK3ZTqTrnltGqsKRaHtgFWN_CJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد: من هم از ایران می‌خواهم خسارات ما را جبران کند
رئیس جمهور تروریست امریکا مدعی شد:
🔹
ایران خواستار جبران خسارات ناشی از درگیری‌های نظامی پنج ماهه است و من نیز از آن کشور خواهان جبران خسارت هستم.
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/680068" target="_blank">📅 20:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680067">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sg3P0RKaesqaYjrnrAlR_LYiqZ6GozErv3Rb5J2HEFz38p-AHY-umgGQys8pLMuxtI2C5RvPUMgjFAo6MjatYrfBoPN1X_PpdunYkWBDoThB2YKnyV7m2-irKVpA3MTwivtGmHMLdEv6GRZ2NveAfbDwzpehVk_bwJ9iZSIcYKdMRAsCEOV1S0LPKFz99xG0tiYSbj-eZlAWv1Utch-202LYxeuEEINsnBwlQMbu67-XYoSorI6VMaz7B8oy4zwmmBr8N6AreP3XB9exDTTKTtF8yumt3pdU8zUPCRGlpASkAuDpX8s3_J1zxB4L7TBR-Vu8RWkPyR9V6Jm5devF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/680067" target="_blank">📅 20:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680065">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcZ7eU_wILpQijxXTSafgl4JJvDOpOQUfVcKRGU2kavCX4HPwa__Ie6uq1I1GJj922d5lyZWEW0zeC2E4HkHZAtzpKi5ws86j3_-XozKvcBwbaBeP2T-VeKCWh6ZmGsgFJTXC8r-pNMUM6WuHfr89d-n0UUmnpfoB6GPSOJzFnoepjMd8BT0rETRhMXPQZjHin6SVLbK-3cWa0t6NF5sJd7DglLt5oUl_MAAsnjQ_K1xyyeVwYmvikUVNsGs7xAdVHTENl8y6YAJ_0UF797cdUzzui_Bf-l2BuliAI34g3FV_vIGtlADlq8unP-CdTUIVf6AQsHGYgw7PVNilFpYEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمد مرندی: ایران آگاه است که نیروهای رژیم ترامپ در کویت، امارات متحده عربی، قطر، عربستان سعودی، بحرین و اردن در حال بسیج برای یک حمله برق‌آسای بالقوه احتمالاً در کنار نیروهای اسرائیلی علیه مردم ایران هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/680065" target="_blank">📅 20:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680064">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed2fc31183.mp4?token=CJlJZni7DOF_d4AB-puEhx3pk8Q7V4jLJjtFZZxB5IvTJT9YpFRHfQLsH1w4qjvJaEJ-Y3-2o9WS4Z5FH0jHf1JyadBg_fKBL_Pykl8dcI_ZGwzrYHhx3gpXU1nu3HGaLtUwhASAYmh8bOK_OOTPEE7iraAYKqALDtZju6YJDgSu-ShlseeXQURwx7_E6cMzFXr2ZZQbM263V4CQjI-4sNpDeLRL51FfzOUwmMKvzbcrQFt7u1jptzJkJiCrGNB1IzfnN82FpZAQuhR8aU-9QXmbbaSehb_CwqNSm7nsdcWykkOu18pe-aHihKwe5e3OCb1CzH2AkJ0c6NDyxZMmkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افسر بازنشستۀ آمریکا: ایران معادلات را از هسته‌ای به تنگۀ هرمز تغییر داد
ویلیام پاتنم:
🔹
هدف آمریکا همیشه این بود که ایران به سلاح هسته‌ای دست پیدا نکند اما امروز تمام تمرکز آمریکا روی بازکردن تنگۀ هرمز است.
🔹
اقدامات نظامی آمریکا تاکنون نتوانسته به اهداف تعیین‌شده علیه ایران منتهی شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680064" target="_blank">📅 19:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680063">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-0EfHWFBC7uWxkUEONlSn_aWaHXrKQEKXFF6vNVQtrie-aQ5OSISkMj9B4iQGXt79L8QczZop773D4zQNT6FFld57tnigVJdIAqB0r3pQlxHNJeKIW_mRYtawDWQtcKaAc3oHz5XTRQ3W_KNjv7I2I_8EPtRxvZ0Zdt1_kNxb5m2Cvc1R-1fpbGfO45NQjAhoQAStQ-OaM9qtbZ-nqNMvPmmymgXrwrJaAhP7osKSpiFe3lBQCwkNJAvsmxWzWSSWlxOYWFQ1DBMd-E1qwoVdSBk8EmFHaERLqf6BDQbjm5UrvSCunZivmtqhS0SSZOh7_s-EYVVm1sOHOELVenMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای نوشابه‌خورها؛
نوشابه چگونه می‌تواند به گسترش سرطان کمک کند؟
🥤
🔹
پژوهش‌ها نشان می‌دهد فروکتوز می‌تواند در برخی شرایط به رفتار تهاجمی‌تر سلول‌های سرطانی کمک کند؛ اما این به معنای اثبات مستقیم نقش نوشابه در ایجاد یا گسترش سرطان نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/680063" target="_blank">📅 19:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
کاهش سوخت‌رسان‌های آمریکا در فرودگاه بن‌گوریون
شبکه ۱۲ عبری:
🔹
ارتش آمریکا روند خروج و کاهش تعداد هواپیماهای سوخت‌رسان خود از فرودگاه بن‌گوریون را با شتاب بیشتری ادامه می‌دهد.
🔹
گزارش‌ها نشان می‌دهد شمار هواپیماهای سوخت‌رسان آمریکایی مستقر در این فرودگاه، به عدد دوران آتش‌بس (حدود ۲۰ فروند) نزدیک شده است.
📲
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680061" target="_blank">📅 19:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQTtCoojAAyXBaZp5wGDDd05NIzoIkJ4z8a-azBRM8VoMXvH4y5p3zLYGbWq03mCQSdbvMroapm0jNBMeR9Gtx3yFKn9-i3VF8P5afZXHWf0XbIAMYo1zDLBqwDDIVdHcxCF_eh4w5NnPWdB8ml9XmyhVwPJdPD-nHkr8N7aOizCGswbCcjt9K6YuoVTDeMRlFUHBSsn_4wPxVRoq0EAcmm6GjDrhOfRERpk7pWi_l4uQERjCQn4D2KjXVka-uis1lFxFPtcV04bs4yyd81CJYTQMCCpwZiObSW-u7mWjnbRl1JiT7GqiK3U3fELEL5VZD5Jn2TwwRqwBwxWNNSQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح…</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/680060" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcsVTrBpQ1F_LYi55wcPVT4ODdJT4WghlJsvWqlCpw_NtDw4yvxtsVabcWZNH14RfAOkiDcOnWjJyiLlrHGKCJAyWLcj2qEDMYplznbxITCVm17RqGAkv82BKhNCJ-9GB-gQa3H_yv9TlA9RgQsvrqVsq5pXMwNswUMe4jcL9SuyetbaDrQklxnAgLLQ6kVHFVT4uwpfv5vhKoNnzpmr_JU94tKBr8ohb2ca3m4HGsL_s_rFj6eAVKzO45sfI0FQ3fsiIbjZSLrGuTOt6Eore7VidngMc9Hi6zE01t0nZ9iApm8naB1JD2oIbeoBzPM-_QXn6l5nWwUJQvpdj3dTjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی به Word اضافه شد؛
چگونه آن را فعال کنیم؟
🔹
افزونهٔ Autopilot را نصب کن، درخواستت را بنویس، نامهٔ رسمیات را آماده بگیر.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/680059" target="_blank">📅 19:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJLi4guRrQml5Umhc5AFT2NDYkD0_YFR_-_5MlGRrYAmf2ev_gGpc7cWdt180GRQkh8KMSmBZWyHHDwuQZxtlG3-jPQaQJrk8GmfbtQj5WcRmKWkvlKYCxrA8j2ijYyIVLHk1d8Z2Br1tkBSN5yeT_bNHdIfjJi6ZIji2C2UES4Z3c6vKdi6Dv2_jXPLQIAH-zKSQoSbyaWk2Ji-S1HaEFcT2Lkp42E-UY7mqxjHiPozJ5EKSrKqyTwiXiQnQ-dwxfAjgPUW2Ww8SLjMOwMISazUrzJTZnTxRj0ZNIhOqa7sQIIkItgpiVOav9UUicvQ6R1wKwyyz1pec41BFlS2NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز؛ اهرم فشار ایران برای بازگرداندن ترامپ به توافق
🔹
ایران بازگشایی تنگه هرمز را منوط به اجرای کامل تعهدات آمریکا در توافق ۱۷ ژوئن (رفع محاصره، لغو تحریمها، آزادسازی داراییها و عقبنشینی نظامی) کرده است.
🔹
مذاکرات با عمان نهایی شده، اما بازگشایی فوری نیست و به تحقق شروط ابلاغشده به آمریکا بستگی دارد. کارشناسان میگویند تهران تا حصول اطمینان، این اهرم فشار را حفظ میکند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680058" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680057">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36a60f89dd.mp4?token=ormAawlbf2IzJxRQuFCsXTZdbIdIxCJ9PVdP7QN4g1LBXiSK5Xcp4_Heap1Ev4r-63tUcI6n0sygUSIaAQYN7ZJGwzzSwqiOKE_UBsd3XaWVEu3BHogeQdtO_WvNRBdU9DfeNAVKM7cnqbbv1LNdTSoQzoW1SURlxXCDcsYihG2xRYe2JhjO8szU8pnnDFoVtwaP9n-lugXK_m6HappfaTT_TpgpICZXAz7aLfs7479HENQELSGTjtmkgYy2zivyrRb3-Ijf8cQmudSwcqWro0ggcKIZ9-R7FK9sHtFwXi7ayjQI009fQt_qFgHxKfFyATDohLe1yhwmN9Xg46SopQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجموعه‌های تابعه شرکت توسعه نیشکر راهی بازار سرمایه می‌شوند
🔹
دکتر علیرضا کاظمی در حاشیه برگزاری مجمع عمومی «شرکت توسعه نیشکر و صنایع جانبی آن» راهبرد جدید این شرکت را ورود مجموعه‌های تابعه به بازار سرمایه دانست و افزایش NAV را از نتایج این استراتژی برشمرد.
🔹
مدیرعامل «شرکت توسعه نیشکر و صنایع جانبی آن» افزود: در همین راستا خبرهای خوبی را بزودی از طریق اطلاعیه‌های مندرج در کدال به استحضار سهامداران حقیقی می‌رسانیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680057" target="_blank">📅 19:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680056">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6888c6d752.mp4?token=LFGIYXptTPrRU2r9qbPiMVvEEsLdE7-_YYrft7MhVhZ7ORNxqiJsJq8g6ruc8xtYLDuWM3FpiNg8vxIA6C02B7a-ZP-jqRwFnUN13gJAK8rTcNvHXHHjSPUQKiYetg0jeNdPlB-E4w1EwH0GLWdbrU8O4jf4ETuPaqUXiB3uFdMDsRu2kshT7BnXenUsoRoX_VRx1A0wtSfpAZM_rfl5f_un-NPuK_Wc67ZyKg1Opqd3OZS086BYj_TcCfpZWWIoLNHJvuERrn3W79iCpdOWtOZE7Yge8wVLTnYG8e1NABAPPtmjZX9OrgpHEEz4iYM3yH6datFIcOM3G6GHEz9BTDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران؛ قدرتی نوظهور در باشگاه قدرت‌های جهان
!
شبکه آی۲۴ اسرائیل؛ دکتر محمود افندی، کارشناس و استاد آکادمی روسیه:
🔹
آمریکا نه در یک باتلاق، بلکه در یک فاجعه گرفتار شد؛ زیرا نتوانست به هدف راهبردی خود در برابر ایران دست یابد و حتی نتوانست توان موشکی و پهپادی ایران را از بین ببرد. کمبود مهمات مورد نیاز این جنگ و فرسودگی توان پدافندی آمریکا، واشنگتن را به سمت راه‌حل سیاسی سوق داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/680056" target="_blank">📅 19:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680055">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8e0GhYr3c1TlLDhALBL7qreNlfoelq8m1PDuU9iXfSGINihLuTXldjHLv4jEo8w1OjII-_UHnTAN2Hj9W9-n65eADM_Ry9PccQfqimLS_jwBI6_fCbZ_w4LMb1Tp8zcpxVF_K9d6VYdQ7JWaQLMgR1Q_A0T06DoFJkN_ilQX0MDyO1KhXqSPGftQtqiUmTnajN8yx0xopR4q4JmkcsbgBS3EncH3xkNlspKwHqN0B6_80gDU6cISEYV7CGW-1dSd_JJHuVO5fkreNr29Pxrvv65HQ3K7cBgzcgWQx207RmY3Y_P59cF7BdEhTrCr0fjFvvwSM8bsIuoAHtibWzQLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از یک بشکه نفت خام چه فرآورده‌هایی تولید می‌شود؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/680055" target="_blank">📅 19:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680053">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب حجت‌الاسلام ‌والمسلمین حسین طائب به سِمت رئیس سازمان بسیج مستضعفین سپاه پاسداران
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی حجت‌الاسلام ‌والمسلمین حسین طائب را به سِمت
رئیس سازمان بسیج مستضعفین سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
حجت‌الاسلام والمسلمین حسین طائب
نظر به شهادت پرافتخار و سرافرازانه سردار سرلشکر غلامرضا سلیمانی به دست دشمن صهیونی-آمریکایی، و با عنایت به تعهد، شایستگی، و تجارب ارزنده‌تان، و بنا به پیشنهاد فرمانده کل سپاه، جناب‌عالی را به سِمت
رئیس سازمان بسیج مستضعفین سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
با توجه به اقتضائات و شرایط جدید کشور، تحقق مطالبات زیر با لحاظ تدابیر فرمانده کل سپاه، مورد انتظار است:
1️⃣
تعمیق و گسترش فرهنگ بسیج و مقاومت به منظور تحقق شعار «هر ایرانی، یک بسیجی» با استفاده از ظرفیت آحاد مردم مبعوث شده و اقشار میلیونی جانفدا در راستای ایران قوی و متحد و حفاظت از انقلاب اسلامی
2️⃣
تقویت شبکه‌ی اطلاعات مردمی، افزایش مهارت‌ها و آموزش‌های لازم توأم با بصیرت‌افزایی و بهره‌گیری از فناوری‌های نوین برای مقابله‌ی مردم‌پایه با تهدیدات دشمن
3️⃣
تعامل سازنده و مؤثر با دیگر نهادها و سازمان‌های حاکمیتی، دولتی و عمومی و گسترش گروه‌های جهادی، بسیج اقشار و محلات به منظور توسعه‌ی خدمات اجتماعی اثربخش با محوریت مسجد
4️⃣
ترویج فرهنگ بسیجی به عنوان الگوی مقاومت و پایداری مردمی در سراسر جهان در برابر استکبار صهیونی-آمریکایی
امید است توجهات و ادعیه سرورمان (عجل الله تعالی فرجه الشریف)، موجب توفیقات روزافزون شما و همه‌ی بسیجیان عزیز گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/680053" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680052">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار دریادار علی عظمایی به سِمت فرمانده نیروی دریایی سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار دریادار علی عظمایی را به سِمت
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار دریادار پاسدار علی عظمایی
نظر به شهادت پرافتخار و سرافرازانه‌ی سردار دریابان پاسدار علیرضا تنگسیری به دست دشمن صهیونی-آمریکایی، و با عنایت به تعهد، شایستگی و تجارب ارزنده‌تان، بنا به پیشنهاد فرمانده کل سپاه، شما را به سِمت
فرمانده نیروی دریایی سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
ارتقاء آموزش و مهارت‌ها، تجهیزات و امکانات دریایی، اشراف اطلاعاتی توأم با رشد توان و آمادگی‌های رزمی، تعالی معنوی و بصیرتی، و توجه به نیازهای معیشتی برای تحقق نیروی دریایی تراز انقلاب اسلامی و همچنین تعامل اثربخش و هم‌افزا با سایر اجزای سپاه، بسیج و نیروی دریایی ارتش جمهوری اسلامی ایران و دیگر بخش‌های ذی‌ربط لشکری و کشوری، مورد انتظار است.
امید است توجهات و ادعیه‌ی سرورمان (عجل الله تعالی فرجه الشریف) موجب توفیقات روزافزون شما و همه‌ی رزمندگان آن نیرو گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/680052" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680051">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردار لشکر مصطفی ایزدی به سِمت جانشین فرمانده کل سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی سردار لشکر پاسدار مصطفی ایزدی را به سِمت
جانشین فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرلشکر پاسدار مصطفی ایزدی
نظر به تعهد، شایستگی و تجارب ارزنده‌تان، و به پیشنهاد فرمانده کل سپاه، شما را به سِمت
جانشین فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
ایفای نقش جهادی در ارتقاء سطح آمادگی‌های سازمانی، با تقسیم نقش و مأموریت در راستای تدابیر فرمانده کل سپاه، مورد انتظار است.
امید است با عنایات الهی و در ظلّ ادعیه‌ی پر خیر و برکت سرورمان (عجل الله تعالی فرجه الشریف) مزید توفیقات و انواع فتح و ظفر برای همه‌ی نیروهای مسلح نظام اسلامی حاصل گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680051" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سردارسرتیپ احمد وحیدی به سِمت فرمانده کل سپاه پاسداران
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی کل قوا در حکمی سردار سرتیپ پاسدار احمد وحیدی را به سِمت
فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرتیپ پاسدار احمد وحیدی
نظر به شهادت پرافتخار و سرافرازانه‌ی سردار سپهبد پاسدار محمّد پاکپور به دست دشمن صهیونی-آمریکایی، و با عنایت به خدمات شایسته و تجارب ارزنده‌تان، جناب‌عالی را با اعطای درجه‌ی سرلشکری به سِمت
فرمانده کل سپاه پاسداران انقلاب اسلامی
منصوب می‌کنم.
در شرایطی که نظام مقدس جمهوری اسلامی ایران در مواجهه‌ی راهبردی و سرنوشت‌ساز با استکبار جهانی قرار دارد، تحقق مطالبات زیر مورد انتظار است:
1️⃣
ارتقاء مستمر و همه‌جانبه‌ی توانمندی‌ها به منظور بازدارنگی حداکثری، و آمادگی هوشمندانه برای اجرای عملیات تهاجمی پرقدرت علیه دشمن
2️⃣
اعتلای فرهنگی در سازمان سپاه و تقویت تقوا، بصیرت و روحیه‌ی انقلابی به عنوان گوهر درونی آحاد پاسداران و فرماندهان
3️⃣
گسترش مدیریت و فرماندهی برخوردار از بنیه‌ی معنوی و علمی و مهارت‌های نوین در سلسله مراتب سازمانی
امید است در ظلّ ادعیه و شفاعات سرورمان (عجل الله تعالی فرجه الشریف) توفیقات مضاعف و فتوحات پی‌‌درپی نصیب همه‌ی نیروهای مسلح نظام مقدس جمهوری اسلامی ایران گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/680050" target="_blank">📅 19:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب امیر سرتیپ کیومرث حیدری به سِمت جانشین رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده‌ی معظّم کل قوا در حکمی امیر سرتیپ کیومرث حیدری را به سِمت
جانشین رئیس ستاد کل نیروهای مسلح
منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
امیر سرتیپ کیومرث حیدری
نظر به تعهد، شایستگی و تجارب ارزنده‌تان، و به پیشنهاد رئیس ستاد کل، شما را به سِمت
جانشین رئیس ستاد کل نیروهای مسلح
منصوب می‌کنم.
کمک به ارتقای توانمندی‌های دفاعی و امنیتی، تقویت بنیه‌ی معنوی و روحیه‌ی جهادی نیروهای مسلح جمهوری اسلامی ایران، و توجه به نیازهای معیشتی نیروها، با لحاظ نظر رئیس ستاد کل نیروهای مسلح، مورد انتظار است.
امید است توجهات و ادعیه سرورمان (عجل الله تعالی فرجه الشریف) موجب توفیقات روزافزون شما و آحاد نیروهای مسلح گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/680049" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680048">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور حکمی از سوی حضرت آیت‌الله خامنه‌ای صورت گرفت
📝
انتصاب سرلشکر علی عبداللهی به
سِمت رئیس ستاد کل نیروهای مسلح
💬
حضرت آیت‌الله سیّدمجتبی حسینی خامنه‌ای، فرمانده معظّم کل قوا در حکمی سردار سرلشکر پاسدار علی عبداللهی را به سِمت رئیس ستاد کل نیروهای مسلح منصوب کردند.
🔻
متن حکم فرمانده‌ی معظّم کل قوا بدین شرح است:
✏️
بسم الله الرحمن الرحیم
سردار سرلشکر خلبان پاسدار علی عبداللهی
نظر به شهادت پرافتخار و سرافرازانه‌ی امیر سپهبد شهید سیدعبدالرحیم موسوی به دست دشمن صهیونی-آمریکایی، و با عنایت به خدمات شایسته و تجارب ارزنده‌تان، جناب‌عالی را به سمت
رئیس ستاد کل نیروهای مسلح
منصوب می‌کنم.
تحقق حداکثری مطالبات زیر مورد انتظار است:
1️⃣
ارتقاء توانمندی و آمادگی‌های همه‌جانبه و روزآمد دفاعی-امنیتی نیروهای مسلح و بسیج مردمی
2️⃣
فراهم‌سازی امکان پاسخگویی به‌موقع، انقلابی و مؤثر به هر سطح و نوع از تهدیدات متعارف و نوین نظامی، شناختی، و ترکیبی علیه نظام مقدس جمهوری اسلامی ایران
3️⃣
تکمیل روند ادغام ستاد کل نیروهای مسلح و قرارگاه مرکزی خاتم الانبیاء(ص) مبتنی بر تدبیر امام شهید (رضوان الله تعالی علیه)
امید است با عنایات الهی و در ظلّ ادعیه‌ی پر خیر و برکت سرورمان (عجل الله تعالی فرجه الشریف) مزید توفیقات و انواع فتح و ظفر برای همه‌ی نیروهای مسلح نظام اسلامی حاصل گردد.
✍
سیّدمجتبی حسینی خامنه‌ای
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/680048" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680047">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رهبر انقلاب اسلامی</strong></div>
<div class="tg-text">با صدور احکامی جداگانه از سوی فرمانده کل قوا صورت گرفت؛
📝
انتصاب شش فرمانده عالی‌رتبه در ستاد کل نیروهای مسلح، سپاه پاسداران و بسیج مستضعفین
💬
حضرت آیت‌الله سیدمجتبی حسینی خامنه‌ای، فرمانده معظم کل قوا، با صدور احکام جداگانه‌ای مسئولیت‌ها و مأموریت‌های شش تن از فرماندهان و مدیران عالی‌رتبه نیروهای مسلح را ابلاغ کردند.
▪️
بر اساس این احکام، سردار سرلشکر خلبان پاسدار علی عبداللهی به عنوان رئیس ستاد کل نیروهای مسلح و امیر سرتیپ کیومرث حیدری به عنوان جانشین رئیس ستاد کل نیروهای مسلح تعیین شدند.
▪️
همچنین سردار سرتیپ پاسدار احمد وحیدی با اعطای درجه سرلشکری عهده‌دار فرماندهی کل سپاه پاسداران انقلاب اسلامی شد و سردار سرلشکر پاسدار مصطفی ایزدی مسئولیت جانشینی فرماندهی کل سپاه را بر عهده گرفت.
▪️
در ادامه این احکام، مسئولیت فرماندهی نیروی دریایی سپاه به سردار دریادار پاسدار علی عظمایی و ریاست سازمان بسیج مستضعفین به حجت‌الاسلام والمسلمین حسین طائب محول شد.
💻
Rahbar.ir
|
📲
@Rahbar_ir</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/680047" target="_blank">📅 19:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680046">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b18ec1b8e9.mp4?token=MOTEx1YD4n1BrNrFC6J7IKGCREa_QmRpp5MH5PjEjy87PJuTYRmQK3oTyUc7BFOMKAtTlHe60Yd191EE3HxDnb0BrzmGsGI0m4w4AKJUePIQLgO2tqOwu6l5C66x8e9dOXlN4xGkyLCv--MGlYQGjT7srjWPUI-EJUnpOsvwozw3q8CyZzVpWekbltPbYKGD0GaI96fvmmpVu8fw4yviApSN_JLyEiFcrM4u9TDpeYVnFDl-uLv6plpH2pUIVv_x-k0fObu0qRWHJq6eh4YSPhGoF4MtdGylLaNcpURjz9I8BZ2kGQ-f7oH-WgjOI6CgEFmQuW4A7fc6n6j-aJa7Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b18ec1b8e9.mp4?token=MOTEx1YD4n1BrNrFC6J7IKGCREa_QmRpp5MH5PjEjy87PJuTYRmQK3oTyUc7BFOMKAtTlHe60Yd191EE3HxDnb0BrzmGsGI0m4w4AKJUePIQLgO2tqOwu6l5C66x8e9dOXlN4xGkyLCv--MGlYQGjT7srjWPUI-EJUnpOsvwozw3q8CyZzVpWekbltPbYKGD0GaI96fvmmpVu8fw4yviApSN_JLyEiFcrM4u9TDpeYVnFDl-uLv6plpH2pUIVv_x-k0fObu0qRWHJq6eh4YSPhGoF4MtdGylLaNcpURjz9I8BZ2kGQ-f7oH-WgjOI6CgEFmQuW4A7fc6n6j-aJa7Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات مشق‌نویس؛ از نسخه اول تا نسخه چهارم
🔹
رباتی که متن را با دستخط شبیه‌سازی‌شده روی دفتر می‌نویسد و صفحه را ورق می‌زند، حالا به نسخه چهارم رسیده است.
🔹
هدف سازنده، ساخت دستگاهی است که با کمک ابزارهایی مانند ChatGPT پاسخ تکالیف را تولید و با دستخط کاربر بنویسد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/680046" target="_blank">📅 19:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680045">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rp9LF_mgDM6YnaZ3CrE5Zfr7BkRHLBKP7_cB_Sn9EpWkvnUpN-Sw4aOk8hEOLqYHuPuXH-Hti7CoDGgSnlKTuzXeUqSSHOrQ1T4cUMBxUjbcU0CmqAfaJd_KPP1uT5YSZpWGK25tsjRr-bEVFiwKfujKOLvVELGmaW1z56JBz3BQ1U5MDSqABWqgHtVyHe9UXLGW4K4j63JDMlN0Z8uXA_juWuGKdpcE95AlY3VT55aLkXRoFFJ5LM5Xmf600DMqAZtQW_0w26iIFpwsV7vgN3Xgc2VpINU6r1nPx7o9FHYgbx1-v8uunQqZAse5sXOOKBbMMkNbmcL0fdNG2zmdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون قرعه کشی، 50 دلار برنده شو
🎉
۵۰ تتر سرمایه معاملاتی، برای کاربران جدید ورسلند که باهاش می‌تونی  ترید کنی و سودش رو برداشت کنی
💸
🔻
فقط کافیه ثبت نامت رو تکمیل کنی و به صورت آنی، 50 تتر رو دریافت کنی
🔸
بدون قرعه‌کشی
🔸
بدون واریز اولیه
همین الان ثبت نام کن و از 50 دلارت استفاده کن
👇
🔗
ثبت نام در 5 دقیقه
🆔
https://t.me/versland_io
🆔
https://t.me/versland_io</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/680045" target="_blank">📅 19:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680044">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJNQC_4UpD_s0UJYKzXHIVy-PzLBqcgCOHDDGdajdJfd4HgHY5vkBWeZfiPAcHrKhnoqtYph_-cFUcoWC8g-7GO4-hCZeTQvyTcpxpZv5qIS5QeTnNlE47cpiSGePTNaVZ19W1avohzlaq7gknEcPYWN6hGJPWwQ481MOV5HtbADGTkDOkibpnBpfBAzs0myHLM-knXp8D0loDtocWGvi-P3V2fUAIa-dTCQzNZyrpn5zmacw1uBukOGApY1SeHiQGGTAFbG_iu02YmWLQP0afVPxkRFqf6rF4p6xxGinKloF6bmMrpA2YLq4_Vfl25mVFoVjUccCTj8vj2v7Zd5jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
انواع ست ورزشی مردانه با قیمت تولیدی رسید
🔥
اگه دنبال یه ست شیک، راحت و باکیفیت هستی، این مدل‌ها رو از دست نده
👕
✅
کیفیت بالا و دوخت حرفه‌ای
✅
قیمت مناسب بدون واسطه
✅
پرداخت درب منزل
🚚
برای مشاهده مدل‌ها و ثبت سفارش کلیک کنید
👇
https://khabarfouritel.affdn.com/productsList/default_affdn_set_men_off
انتخاب‌های بیشتر با پرداخت درب منزل رو ببین
👇
https://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/680044" target="_blank">📅 19:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72e3762d0b.mp4?token=FdYR6H_3Jxb3sHnive6AG3Sk8ImiU0RA7KbsyY3CaOTngbFFiq8Im5gZB8boqh-sWzYT8k8csCBnZWcEii2qClg4iafAoxBOSIzW9a6o0CWV61Y3RRbUfrYja1T7GjPG4m1IgbxuQ5ucIrbrgw_AsP4_PA8NRNre4FQ7kdSfr09fR0crnjkdDswzx-_9PuAFZ1HRCfgkp3bxbjv9IvhSR1d7GThc2bfWKzDrSktDmjz2zXd9BHD-2ymYNZqkI5oeGfM3PSKVTOFUXrS6jBltEimPnkt9S0qLBF86mHdyrXPBlLvdb7LyXNH2JUJnLwxhcpBnh2ta8KRS74ZKbHuj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72e3762d0b.mp4?token=FdYR6H_3Jxb3sHnive6AG3Sk8ImiU0RA7KbsyY3CaOTngbFFiq8Im5gZB8boqh-sWzYT8k8csCBnZWcEii2qClg4iafAoxBOSIzW9a6o0CWV61Y3RRbUfrYja1T7GjPG4m1IgbxuQ5ucIrbrgw_AsP4_PA8NRNre4FQ7kdSfr09fR0crnjkdDswzx-_9PuAFZ1HRCfgkp3bxbjv9IvhSR1d7GThc2bfWKzDrSktDmjz2zXd9BHD-2ymYNZqkI5oeGfM3PSKVTOFUXrS6jBltEimPnkt9S0qLBF86mHdyrXPBlLvdb7LyXNH2JUJnLwxhcpBnh2ta8KRS74ZKbHuj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افعی شاخدار دم‌عنکبوتی، یکی از عجیب‌ترین نمونه‌های فرگشت
🔹
انتهای دمش شبیه عنکبوته و با حرکت دادنش پرنده‌ها رو به دام می‌اندازه!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/680042" target="_blank">📅 18:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/958354fbb3.mp4?token=Wjt8TUST1wjvH4ka25GLuzgf_RJMIvTK_LjrZejwAN-MpMxr7wMbj1_2OfnpuQ2LEuzGx3RyaNXDn6lZS5BGnWXDEAbKqQEPHve8PNfCzcYKPyWlNmS-PqeVT4KJdYrC7Kd9o9FntLMEZNJHXzqrJWrLZN-l-BG8EmLsRAz-HDPyKulLtTSIlz6g3YyXxwOU0GK4SeFtPVz-v1ax3Z5XSPlM4c1cYK9mcaNxL_fk4TBpppwl-dfurnyf8t31BNwW4hKA7etZqk7la7NYtneMZkSpD8V2oPCQ58MmhnqXsqfu1ugmTPzqEzg5-Uwmd0ZNp0m-xnVKNOzR7Skvi8-Th5bBANWfe7evN7urMp1H6VFZJdIw7QZnVlClNWgNfSR0HYsS49hl8izDJ2ukVV5X8DLx5-75Y6Hg-_e9HDmZRMOY-oYTE_QKoh8ue0f_bPVEnb5MRMdY-1dpJdP9_6pKltUJNPPPWsLv-U4djnISGPPsLw9CWcPvr4YLVJku-0jv5qWwsVOpoUp0Euig1LGZgsOCKETWp-qR3YWJKOEYF54fgO-Y6RzGtf_qGOkenNfRy3wu7u39DLTduHHAFY8YVeonRX8HgxXocFeTuvj-I-flJBMEVN-uWMhUcCc-BuXBN695mUao047Y-K6z9-qfuu-ESVA0b-pWS9fT2qP0ibo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/958354fbb3.mp4?token=Wjt8TUST1wjvH4ka25GLuzgf_RJMIvTK_LjrZejwAN-MpMxr7wMbj1_2OfnpuQ2LEuzGx3RyaNXDn6lZS5BGnWXDEAbKqQEPHve8PNfCzcYKPyWlNmS-PqeVT4KJdYrC7Kd9o9FntLMEZNJHXzqrJWrLZN-l-BG8EmLsRAz-HDPyKulLtTSIlz6g3YyXxwOU0GK4SeFtPVz-v1ax3Z5XSPlM4c1cYK9mcaNxL_fk4TBpppwl-dfurnyf8t31BNwW4hKA7etZqk7la7NYtneMZkSpD8V2oPCQ58MmhnqXsqfu1ugmTPzqEzg5-Uwmd0ZNp0m-xnVKNOzR7Skvi8-Th5bBANWfe7evN7urMp1H6VFZJdIw7QZnVlClNWgNfSR0HYsS49hl8izDJ2ukVV5X8DLx5-75Y6Hg-_e9HDmZRMOY-oYTE_QKoh8ue0f_bPVEnb5MRMdY-1dpJdP9_6pKltUJNPPPWsLv-U4djnISGPPsLw9CWcPvr4YLVJku-0jv5qWwsVOpoUp0Euig1LGZgsOCKETWp-qR3YWJKOEYF54fgO-Y6RzGtf_qGOkenNfRy3wu7u39DLTduHHAFY8YVeonRX8HgxXocFeTuvj-I-flJBMEVN-uWMhUcCc-BuXBN695mUao047Y-K6z9-qfuu-ESVA0b-pWS9fT2qP0ibo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوخی علی مطهری با شایعات استعفای رئیس‌جمهور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/680041" target="_blank">📅 18:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680038">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPytvPOpQEB4Tuga766wkochsCaXLH0C4epzjd0ooNMlZFPjgtTz-IpygA0Ah2MLqdJQwx3T_geniH1M825I_NnDExxQRBD0cff7FPY3KytN3uW9F1FiwL3J2y-TgeG58g9C2ZHP6Zk3T_52jTc5oQebLAiHvN2iC6BVx8PTlXHQ7P3PGKtByc1xqZ-UP3Mecu-K4o-jzHIEPUCTLH7PRr0-CmmEhBwPdoIhJXqIDUZwo1lmiao4iIsstQyroeT8M4N7mMjTdnJ_RDLBCcKHX_0xv-I0P4N0gst6L0TK78M-3n_rgmsPunDYcfIbZiCSP4wbXubV53smSWXv8MG55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تا ساعتی دیگر منتشر خواهد شد؛
احکام انتصاب تنی چند از فرماندهان بلندپایه نظامی جمهوری اسلامی ایران توسط فرمانده معظم کل قوا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/680038" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680037">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ae89fdc1e.mp4?token=Oo7GOcKkhRTXbVzsSFM516Uq_wEyPeoDzq-ovmTxzIIpVO8aBsDJoyLSfVo8sFNJTU9QwQta5xAArwY3ozT00Y6BMWq7AhLCGP68jYWEQk7nSif8Ve-lJta8GQjUV5c7cJJRq-dxnRLsSBCF-FxafrWypApGaK86T6r496D0VOH_y0YnFwk79YwseE1BoppvAgrfQhjPiPSMkc1C9hB8J0ibhjqHA3S5YO-P22_cgADVb7YB2Gi-aRy4kHS2MIz_lnZxFTZBKxEyU-sfadPIzrIPpjBiGMDankrpc_fcOLj_utX7S7e3QrT2GFFrpLajwnrWgDgY5dofZ7UyYzzgtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ae89fdc1e.mp4?token=Oo7GOcKkhRTXbVzsSFM516Uq_wEyPeoDzq-ovmTxzIIpVO8aBsDJoyLSfVo8sFNJTU9QwQta5xAArwY3ozT00Y6BMWq7AhLCGP68jYWEQk7nSif8Ve-lJta8GQjUV5c7cJJRq-dxnRLsSBCF-FxafrWypApGaK86T6r496D0VOH_y0YnFwk79YwseE1BoppvAgrfQhjPiPSMkc1C9hB8J0ibhjqHA3S5YO-P22_cgADVb7YB2Gi-aRy4kHS2MIz_lnZxFTZBKxEyU-sfadPIzrIPpjBiGMDankrpc_fcOLj_utX7S7e3QrT2GFFrpLajwnrWgDgY5dofZ7UyYzzgtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین تصاویر ماهواره‌ای از تنگه هرمز
🔹
با وجود ادعای ترامپ درباره باز بودن و کنترل تنگه هرمز، پایش‌های دریایی از کاهش محسوس تردد کشتی‌ها خبر می‌دهند؛ روز یکشنبه ۹ کشتی کمتر از جمعه از تنگه عبور کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/680037" target="_blank">📅 18:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680036">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52c4a7ad6a.mp4?token=udP38rW7efuf950_Qb0kXA1GXRxoZ9Xka78wDAhwceTyknMBo0XrprdUIQn4C9sI2HbmB7EpWEWCgQ2EDYogwZX0ZOg7b4lFgG7PCZrFrEIm53WW9V5Lq1pGxbnO8YvBr3qm-rkbZnJdLUJGK7zoSfIs1ppE4ne3G_1aH2Tg6YW3agK5PVHZBuyuOwY0ioa9E6bGu2epKubxIdh0ONetTX8JfZ5nEUMMdfetiTKlL6mkcwzx0GxdgiI2vU2K7uWHtJkUOUcMM0n4SaunNDX4Z4iBsQmOa23WSfIOS0j0Ccw_SUqfRNsFsWwaANvv1v6NePzSCZEGDn_iFfsL3f2Q4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52c4a7ad6a.mp4?token=udP38rW7efuf950_Qb0kXA1GXRxoZ9Xka78wDAhwceTyknMBo0XrprdUIQn4C9sI2HbmB7EpWEWCgQ2EDYogwZX0ZOg7b4lFgG7PCZrFrEIm53WW9V5Lq1pGxbnO8YvBr3qm-rkbZnJdLUJGK7zoSfIs1ppE4ne3G_1aH2Tg6YW3agK5PVHZBuyuOwY0ioa9E6bGu2epKubxIdh0ONetTX8JfZ5nEUMMdfetiTKlL6mkcwzx0GxdgiI2vU2K7uWHtJkUOUcMM0n4SaunNDX4Z4iBsQmOa23WSfIOS0j0Ccw_SUqfRNsFsWwaANvv1v6NePzSCZEGDn_iFfsL3f2Q4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رکورد ماهی صید شده با دو متر و ۱۲ سانتی‌متر شکسته شد
🔹
ماهیگیران روسیه یک ماهی تن به طول ۲ متر و ۱۲ سانتی‌متر در خلیج پتر کبیر صید کردند که رکورد رسمی این منطقه محسوب می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/680036" target="_blank">📅 18:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680035">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رییس کمیسیون عمران مجلس: قرار است در تنگه هرمز خدماتی به کشتی‌ها دهیم و به ریال هم عوارض دریافت کنیم
محمدرضا رضایی کوچی، رییس کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
با وجود اینکه قسمت عمده‌ای از تنگه هرمز سرزمین ماست، اما محل تامین تجهیزات نظامی بر علیه کشور ما بوده است.
اگر دنیا و کشورهای همسایه بخواهند علیه کشور ما اقدامی انجام بدهند، باید جایی باشد که آنها را مدیریت کنیم و آنجا هم تنگه هرمز است.
🔹
یک طرح ده ماده‌ای برای اعمال حاکمیت ایران بر تنگه هرمز در مجلس بررسی شد و اعلام وصول هم شده است.
🔹
به هیچ عنوان امکان برگشت تنگه هرمز به شرایط قبل وجود ندارد. هزینه انتقال کالا از مسیرهایی غیر از تنگه هرمز زیاد است.
#فوکوس
@Tv_Fori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/680035" target="_blank">📅 18:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680034">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT0U7eVjbEjnptcWRtsBj32sNvdWyqiHb4MaNze_cKuP29hmlbWCwfEIeEAw61Y-zFYl88gia1aEu_85DMkKFRwEga2huhKEO1CUsU2qFFcQqibN1VTYkeAklCVbXiw9rdNi64NdvvkO3vBhxbxgdsj3htweunT_m3Vrx-I1jfS_v-WK-I6XrJwTk9ODWmU3pFDQmwxFhS2W2MknIjN78gge1bauI-qVd2Si7wzjN7OLFE1YnhIX-VuVdqUTAjdJp6CZeSagR1H2Ttgx84WpjVE0r9ECLvnVa8_O6UjHytfuDuvrITiII4D-7XSsrC7hvKfsOjOlrMsHMcEnzGBmUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاعری که عشق را به زبان جان ترجمه کرد؛ مولوی
🔹
جلال‌الدین محمد بلخی، معروف به مولوی، از بزرگ‌ترین شاعران و عارفان جهان است. آثار او، به‌ویژه «مثنوی معنوی» و «دیوان شمس»، قرن‌هاست انسان‌ها را به عشق، خودشناسی، رهایی از ظاهر و رسیدن به حقیقت دعوت می‌کند. ویژگی‌های…</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/680034" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680033">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxaPKdEE6sLlNJC99oZt2l1YgpUYxZCQowUE3dRrDisykM83zQ91ykxHG1CktqO3n4_3FK96A04TsHGhVDpIDpjQyCAKLLdOFcxy2g42-7nztfk-s_kj7L01WKsbMOEFaXw9XApwNVo8K0eFQXjQuzVtuYbQktNrlUdnutRy9hgfVuMZAvXYspcNEZfDqsKYbyWMMytsFhfXEVFXoZjCGN2gcwRh_Etjx5VbUF6GkEiVcn5pmnL4CG2OOYGOr3TOapfsTXAXCezRh2AGrwavqmjmhHXhmjcGGyLntWVFZ0ufvP2v-9XPNgb16gHqVJViqXwpZeHwO6h6GBWNdSvZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون نیاز به چک‌وضامن و در عرض یک دقیقه
ملّی‌گلد امکان خرید اقساطی طلا تا سقف یک میلیارد تومان را فراهم کرد
ملّی‌گلد در راستای توسعه خدمات خود، امکان خرید اقساطی طلا تا سقف یک میلیارد تومان را برای کاربران خود فراهم کرد. این مجموعه همچنین سقف وام آنی نقدی با پشتوانه طلا را از ۵۰ میلیون تومان به ۱۵۰ میلیون تومان افزایش داده است.
در سرویس خرید اقساطی ملّی‌گلد، کاربران می‌توانند در یک بازه زمانی بسیار کوتاه،‌ تا سقف یک میلیارد تومان، به صورت اقساطی طلا بخرند؛ این سرویس بدون نیاز به چک و ضامن ارائه می‌شود و کاربران می‌توانند با انتخاب بازه‌های زمانی ۱۲ یا ۱۸ ماهه، برنامه بازپرداخت خود را انتخاب کنند.
در این مدل، طلای خریداری‌شده با قیمت زمان خرید محاسبه شده و تا زمان تسویه کامل اقساط نزد ملّی‌گلد نگهداری می‌شود. پس از پایان دوره بازپرداخت، طلای خریداری شده با نرخ روز به کیف‌پول منتقل می‌شود و کاربران می‌توانند آن را به صورت آنلاین نگه دارند یا به صورت فیزیکی تحویل بگیرند.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/akhbarefori/680033" target="_blank">📅 18:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bce5f4670.mp4?token=aKuaKqrPywgwAgFtj0rgl8zi4KWU6rhhy5k0QQTXhgK7jsp567fWqRZa8l8-hz373_psLUjQjpOCsEd8j1nYzdm_t9apTqj3_TmvMKNnFyRe9TLN9xCUX1R5khGEBIH38DlpWT4PFugU4-2oE8BjNhM3l-BlmkRgpv4-R4vtqiifGgUo8GJo7fP7UUJjuD8_hsRn3PszvfT_fosvkeKg0Hm1i4LrBvhASmNsaU2CbPazInNB3XYm36MvXmSOj0Q1NfCnhrEmfBr-q3hngEC3HLRvXW3gngushW-PEUlcvTRPLHQGqy-s6yIyA2IkCMKMkpgILvc4jUowQ1p3y92-vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bce5f4670.mp4?token=aKuaKqrPywgwAgFtj0rgl8zi4KWU6rhhy5k0QQTXhgK7jsp567fWqRZa8l8-hz373_psLUjQjpOCsEd8j1nYzdm_t9apTqj3_TmvMKNnFyRe9TLN9xCUX1R5khGEBIH38DlpWT4PFugU4-2oE8BjNhM3l-BlmkRgpv4-R4vtqiifGgUo8GJo7fP7UUJjuD8_hsRn3PszvfT_fosvkeKg0Hm1i4LrBvhASmNsaU2CbPazInNB3XYm36MvXmSOj0Q1NfCnhrEmfBr-q3hngEC3HLRvXW3gngushW-PEUlcvTRPLHQGqy-s6yIyA2IkCMKMkpgILvc4jUowQ1p3y92-vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از لحظه کشف خیانت تا تصمیم نهایی، چه باید کرد؟/
تلویزیون اینترنتی مدار
برنامه کامل مُدارا را تماشا کنید
👇
https://youtu.be/4127WFofp-M?si=05Z3uS5Mhr--u9Vb
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/680030" target="_blank">📅 17:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680026">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28de48ce92.mp4?token=J4KaeBzxRTOdBrtxnkWdGpX0bE3c51FewYR2mmJKu59X0ST0xTNgSNY2COIrSXE7MmJcvIqlo31Gy7ANV31cjKhrhLu7p4IO5bFuqAtzrwRI8thDH7bwe5QnEfl59eTJSQXM0geuKwegIJBnF0tNLDlOoq5df94G6TPKQK7hU4uhGh9dcdFO6UnkHWUTRYpH3ZNLA8qdoYrl5VZw8-lVs_7cB4NjnDY-hxMnsSY3IHLQzhLCd5lwMupolAPB6h5B4xRU_mfl7kQK2dJb66-ixmFtLsNw9R3IY8FZ7FHwhm22hufjuDm70KwWWbYkyr1yAgmlWdMUKL6OLBF4FdK7hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/680026" target="_blank">📅 17:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680025">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
حمید رسایی: مگر منصوب رئیس جمهور می‌تواند مجلس را تعطیل کند؟! جایگاه حقوقی دبیر شورای عالی امنیت ملی در جایگاهی نیست که بتواند مجلس را تعطیل کند
نایب رئیس مجلس:
🔹
مصوبات شعام پیش از ابلاغ به استحضار رهبر انقلاب می‌رسد اما در نهایت با امضای دبیر شعام ابلاغ می‌شود
🔹
ما سر هر موضوع و مصوبه‌ای نمی‌پرسیم آیا به استحضار رهبر انقلاب رسیده است یا خیر؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680025" target="_blank">📅 17:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680024">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904a9af188.mp4?token=cU3Z3wDWl9rGL477vlQzM_NEbJpe1xi_KRqa99NLFLHlDeSjSf5yIeKKDg1IEHQgzMhCqic8hKFGuTiAB9Zn3EwOFaZf_e5R2OW08GaZh7LQ3YXc7iqCgl8Dg4axWrb5znzKB-gdMtr69qTcq2tc1TmA4MviMMrOQfTWb2pVCJ1o0xDNvE86rbPYdBnW7gWTUmGcVLrJe63MFR9NMQLof7q56VQBK2-bFfg3pnTV-vGIOFgcZfb10IvATU04wleNKv5gjeVm1Mo9vrbhs5zsDowZsZD-__Qs83nQJGMNQLIAajVrEaoK_31qGckIrdQfwgdxWLUdnEjCySXVy5h8GxKZxR2CMghLTHOvqWUU6fal3_XqwIrA3UrxCxW4N5ag1mHHfV3FBIa0YQu4ynECCgt4BUIobm0rklQOV9U_j6RsMsL5eKlctVCY3A1LkNmvqmD9Q4YMd3foCBjDzY_e8U6PQdo3YMpRzzMTBX7rBJqXBvJORYCTG5JaWHNHjle7VcurnmVsAHDXrJx5sZi5YleFNp4XLTIX4R4JvSYFi8CPR97prt45I4v4faj3LoO30kqV7t0enhAeT7r9rD1ipBAMEQs9dLFX4_jS1xyRAm8EKVc5ES6qAKnkUDwkhZp9C_Dejb2D0B_XJHnTA60qT-7x2cbiSKgmeVOgIDhpYto" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از حمله آمریکا به اداره پست آذرشهر در ۱۹ اسفند
#اخبار_اذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/680024" target="_blank">📅 17:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680023">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/111e8c1034.mp4?token=L5Ky80QaJumaRXMM7Pg_4lex_tY1Fbz2U1p8mJmhQdOLh7v4DfE05H_cXFx974F-vigWyo-gTY-XAa570RIRwFvQeBmzzAUizdMejrIr-KqjrVVIyodZ-xlipJxZCTq2aQ1tG5kA50boI7dhzo1yS4b9dWpOp8ntUEIHsdCzUk87w3pO3WMeNfXUdyWOGm5tUQflbB3Y5tOpZJgoKm0Iu1EsHJvAOcBW7Y5vI5Y5nT36gwJ3C11oujUPZ3CnNYTedhUE72hc7LCdbTj4k_Try-lw_OfKafY-RVNTdPJvvpuKl0gsItYkfjc_6QdSzjdKBgqrYiWMfsChyKboToQC4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادعادل: کسانی‌که هنوز در رویای دوران انتخابات هستند اشتباه می‌کنند؛ وقتی که کشور در معرض خطر است چه اصولگرا و چه اصلاح‌طلب باید به دولت کمک کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/680023" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680020">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cad9612af.mp4?token=Yt31narOd5Fu9sftic5W6gmJno7EoKfYSuSfI7H0BDYaHTdNw8qCbRJFOUZrct0oBp20RyV2lyTNQppgVvBVKbjM2LOQ6DDapmDdLNKSGJcgb1b0yNhvgOoVXHL31-zt5DWoYBHoTs_4ME5kPVGpuzSpFh6j9kLUwoT55xQQ6-ZifR2lXX4RhqOQQhtzFJideIpXDjAOfB3q6_JzOqULxuSWqiMLv60W-PRG3ooCYN5WbTrcijoumQLbfJ9fdNo4JdN4gF3rMqaJp5DT3RI6EeWv7ZbDvXxj2UpRv6BledUbIyzihorOBivr7TgXRYeH4sGFa6Cvd9HhKYNWG9RynjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: خدمت رهبر انقلاب رسیدیم و از هر دری گفتیم
🔹
ایشان از لحاظ جسمی در صحت و سلامت کامل بودند؛ ایشان رهنمودهای خود را ارائه فرمودند و دغدغه‌ها و مشکلات را گفتم و به راحتی سخنانم را گوش دادند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/680020" target="_blank">📅 17:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680019">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/680019" target="_blank">📅 17:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680018">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpSOiM6Ru61MPJX13MCxSeEO3ZtG8GL4UOaIG4k9JlXpub92QA14L3U9XsrTm2aFqW9JP4P29BBfp6nUYtKbAYwZAaDy65gBP9Poj9c0V8xQsbxEYNDhgDMnihgqlVGfr1Ke1QNO2zaYZJChWizXmIvqdejs04ySkJRkxi_1_IH5_bcpfcJA5pRl9yS9MWRu0KknWO1lnyfCn1skyw53iy2jReTZW5HZ4_4wpeaSRCaSMDl6Vo6NOagJs_OOJPTfCiAlWFYnYw65nDCiGOe6sDQW-0lZKQ_8aDZSu85CiiFyiRnO-3JHXny7Ks7TsyqjhGn_z_SCn9KL17xKuFzI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۴
🔹
عبور سهم از بازار بانک کشاورزی از مرز ۷ درصد پس از ۲۰ سال
🔻
سهم بانک کشاورزی از کل سپرده‌های شبکه بانکی برای نخستین بار طی ۲۰ سال گذشته، در تیرماه ۱۴۰۵ از مرز ۷ درصد عبور کرد.
🔻
سهم از بازار این بانک پس از یک دوره تثبیت در بازه زمانی ۱۴۰۰ تا ۱۴۰۲، روند صعودی به خود گرفته و از ۴.۳۶ درصد در ابتدای سال ۱۴۰۳ به ۴.۵۱ درصد در فروردین ۱۴۰۴ رسید و سپس با عبور از کانال ۶ درصد در پایان سال ۱۴۰۴، در تیرماه ۱۴۰۵ به ۷.۱۷ درصد رسید.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/680018" target="_blank">📅 17:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680017">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f2576f565.mp4?token=YPxQdIA5H7-2R2thSDfajxooIZcyF4_qiA6ZTRQ7TnmvVTduZL6dZ20I4kmaOqKGjDBRvApHbzEknaxdLWZ0Uhek6e2RJ67h0ye9FfrJsvsdHcwfK4cr3SB9NLIJVC99lToc3HgnHI_xhQt797ZcMKRdWOTbHFg-PXAFMYn4GDIDx4eCgXEo5L0FXSzz4y1jQDd3_kUISM3__FPMYLjd1eijaSvDb2OLo6e7HxDMrP4oGSQKeGBgCN7XCAM47f1XXH6i05QP0mIK7F34xQ__kJTdwooitQZccz7M0i5seeQ2gDjyEDdtLQ9-Dme8MnxUsWl58hnbxo8w0yUbSwCBrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات اولیه زلزله ۷.۴ ریشتری کلمبیا
🔹
سازمان زمین‌شناسی آمریکا از وقوع زمین‌لرزه‌ای به بزرگی ۷.۴ ریشتر در کلمبیا خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/680017" target="_blank">📅 16:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680016">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e15e2b081d.mp4?token=j6_nKPqtPAqPd4qWHygxFSSVzpCSoel66Az-qrCNxD8qp_scdsOYJS8OQifoS2-pqxHtcR5fZgm2V7xcmcOkTWTeN1p2oqj2lhdn5KDpAtaDtctlR1VWzjZGyTKcK5K8YT2GLlT79DrbxgVZNLk5WPwgV8f9s9gixh5F8g5p8pkQqbh4H9qznsC9FuyQ2ZNckJTjP71RIgXqCxH_HU0z_KD_F4clH_7AjA4JT-18aJ5yNIJRPCEG9Mj4FfK52XFu0LNGqau8t7m0WOjF5RrYhqf2fk6vYCSDMbzHDOWvDFrUJYzht6-siHt35qc8Nv40xy2UV_HQumSOXJ8XhIdLvQrmUoRZcLCR1m8Yu2Bvg_pPtomq-grRsDJNE5NCNvTXfbIzFiURofc9Is3yxRkXmG7K5_EnmiKvmfvs7rSucf9mIQDbJcGUC8pnddmnfjiI0eJ7rByYxDeOukQWmkZoum4lCip1gBYM71L4njyQfZSZBIcGNQPGt4usT6NkedtyTExzt7eE13k9iTBWFfAmLmJiqkaSqUy955oESBWQwgy8S8p3jBZZvn3yhOYaj7KmNP-U-j6PQj9E2CYPuWvNoNnktbF5iAaXoZUt-0fZCEhin-MQj6gF0mzgZBztbU5L_Lq4AuWK74sN18WnR5NdRiJaBiayFwjF07rrbj8Fus8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/680016" target="_blank">📅 16:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680015">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO2WlF3RIFQbgLD2sw_mCxMIGSWKxMfPUeg4PIXwQYU46dWPHxrpDsDjv9bvof_8vzNW77gn9gr3l_7jQ3WliUplQQ3uvluv8tHHHYdFNXefz2Bsoj7M8hIon4QybeKoI00m-ZL7QYkUbpFmJnzlzIrJO3HccieREc8FkUTC7Q9ANMUyWR8tNxm0J-9zcP9bSyizvV_SWV-BqNoe8FKsFXqyIONVezCsKo1EkgGHA70AdJcXMsYkjAX2Bes5pkdxcUhA06C3U2mtWSbsIVzJqJWyXHZsAUQKMYzxp9QTQWMQ3J5tmqmIq5XNvgd25vpy1VLbzIpHp-tiBDBENILcjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وال‌استریت‌ژورنال: ایران در چارچوب توافقی برای بازگشایی تنگه هرمز، متعهد شده مانع عبور ناوهای جنگی آمریکا از این آبراه شود؛ اقدامی با هدف محدود کردن حضور نظامی آمریکا در خلیج فارس/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/680015" target="_blank">📅 16:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680014">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxKJibBbD21UNk5G60ZPYse05Ru35Cbe9CZhPmL8IIS5yomfA1cYtYRDD0SNMHdXoGgchaRPDfTLFMnW_fOydCPKyO_1q0vEELxoLp-NFoxCJmYWu2WnQ9wDYxJkmSkQ9Zleu_6269T-K19HsNc6zsEJVh9KHzN0kKvLQe6ruu1nZ76YShF1-6a8V1mI7TMSkOVRznVRR_OYhuoj6XsiB1KmS9Mwk0gUfzRV7D8PpJ77pAAbP-wdAfFcFLN4I-SN-SsMoELMeY8u1WsDC_vaGWZm-hcAYi5RO7dypaVDXq-44qARTWRWkM1vmo7ZWexf6cf4rE4fRrEnp0eJS7vg-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت سالروز شهادت امام رضا (ع)؛ حاجت روا
🔹
همراهان گرامی خبرفوری؛ برای شرکت در این پویش کافی‌ست یک پیام صوتی حداکثر ۱۵ ثانیه‌ای ارسال کرده و از حاجت شیرینی که با عنایت و لطف امام رضا (ع) برآورده شده است، برایمان بگویید.
🔹
در ابتدای ویس، نام و شهر خود را بگویید و روایتگر کرامت و نگاه ویژه ضامن آهو در زندگی‌تان باشید.
🔸
صدای شما می‌تواند امیدبخش دل‌های بی‌قراری باشد که این روزها به سوی خراسان پر کشیده‌اند
👇
#حاجت_روا
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/680014" target="_blank">📅 16:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680013">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b1219c01.mp4?token=pd72VzqxZXAcP79Qk1_vv1KwvvVDWsXo83YqrAyGp5a6OtUhZw4DfUrbxgtmXGuM7zXWTkNSnvs7dP8yHbZlWlZDCWvXO7Hln3SGpPNB5-wbqbAUbc7Dbjqmxig6-dQP3YoZucEyMonVUHkQ3BAsa7KFF4vXKW4CoMTdhRNYJx0KozG4MArSp4wujo-FURqh8LJ_D-hgnQorVjfPzPlXQ59ADmXWPmWQiEEyuFrix9WRLhcUgD2G3VDP1cy8k5aa02bkAX0UnqoLBEaLwCNFyisGsMfr51cZL0o8PLWrX_bHHxzSVnIEaVgiqPiJoXX2wp2El0X6EQii93X6JdAV3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی عجیب از خانومی که بخاطر عمل زیبایی ماشین خودش رو زیر قیمت بازار فروخته!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/680013" target="_blank">📅 16:27 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680011">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156dbace98.mp4?token=txic4fgf0JGklJyq40DpDHlRuPVlN4Hw_paQ3p7744sKJpacPf5L5RWceQW03wWHn7dNo_x_LDlbU51t71CePEk78l3u1BpTDMrBwmlO0rtFb58zVV3nQYU1pIJXyCl3QMR83IZ3JMIrFe_6XXsu1pd5N2o-91M5X5QHRS8G4DPpHX1su2dRHQBMEkwTMCxdHdWgV_VoMcSxbEKAMSgyNuoKNqQJUOH2wTFqktXV3El7kYMekunXDKOvlbe_72dGMNrTsmv1hpgrOTDq8EAHUf9j6oS-fwhI3k7dZY5z-_gSuWBMNL-RC7sFUmYLeaHNf6wzz68kO8hDRceSiZZnJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایده جالب برای بسته‌بندی محصولات کوچک
🎁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/680011" target="_blank">📅 16:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680008">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7557a5a45e.mp4?token=W6CsG-FlFumz2e9H8lPmfbq--1TnBe-JLp6BYr3qmoeMYLBWkfqrB8rDTFUL8hq4iuKZHrHtLOt9gXuzR54iwQog-SG1BJRr1I6ge487LU_Nww_Ja7uF1jbgVfkGSvXlUBGluIsFKMt_beqd5egKOAzwN1G1ASI3DPlUMSJ7NHTRaWd31fMhQU3rBoQBpSR0R9iiHMpJ0NHntryLdYoFZ2gYjzJagfSmHtGVd1UNoYVX8x5ggCgznVzxzq8rSeqKkTaCohVjoXOCTiP51r83TY0Dj1g_Rns998bE4a-iXGqgKWDmeJ1gdRniHBG_l0w2NfowrTc0OnIUzH8wjW5Kzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش عجیب از «مستراح سنتی» در تلویزیون ملی بریتانیا
🔹
در اقدامی که برای بسیاری از بینندگان غیرمنتظره بود، تلویزیون ملی بریتانیا در گزارشی به شیوه استفاده از مستراح سنتی پرداخت!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/680008" target="_blank">📅 16:12 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680007">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ibe1oxfyBXTy_rrOH6TI3roDs95GtxKHK5G3o3iFs9koBVlgLpEO66gDbgCvIMOcxijMa3AwPNyzAcej-z8XNHP-rnR_gCWIQ3HfiklwtgCUUya_PBm-uDTCFlyBOJ29sBr5tWdAfh6J3G-aKM4fmRkTJWtSf5M6hmKJvQ8PlY-N4ur9xAOFORKEWlhXQtuff3h1iRmvTadX29mr2gACccwmHyGk-FnZeVvCCWXD2QDuNXNxXS-A0IcLchQon4kIWCX_76OdUvIkbrqEwg4DQl7X_WpxnP_HUf5LXoyNkWm1bKqrMvnaWir7SwI8qMgoY-RZRM4Kqe-Et1LXh4XQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا می‌توان با ۱۰۰ هزار تومان طلا خرید؟
صندوق‌های طلا با پشتوانه فیزیکی سکه و شمش و امکان خرید از ۱۰۰ هزار تومان را دارد که امکان پس‌انداز تدریجی طلا را فراهم می‌کند.
رشد قیمت صندوق‌ها مانند طلا است، مثلا صندوق «رز ترنج» بازدهی ۱۲۶ درصدی داشته، اما چگونه می‌توان صندوق طلا خرید
👇
👇
👇
📌
آموزش نحوه خرید صندوق طلا را اینجا ببینید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/680007" target="_blank">📅 16:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680006">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785faa238a.mp4?token=qBnzchO4JPMrp-QjYnDlGDSVZIHFet0QTvJzQBD2cZY0B4-D5AEiWpFJQv6lAk8_J1yYpAPGNl79trnbQp7RZG3s-TWYycBh3oNyvJxa8wTgeRb7xaRPjFEr8jNQ4Rrfx3D2VBe5sdjk8V1WdgYgqnDj_8ZbulPBfQ6paAhniH1tHW37iW8krYGCI0iAVp8YlcIrU7l2h946KD_4v4Jjlxdl6Xxcl6-gdHOnS59mI6Z38iZTRldbzErpusO4NuIPP-M_Dk4oZ8U97AI3iYJ3gMOwvAwaCaJi4C22NXYQ9bV0XmEGBUltVhgBrKjLOgtehL8FJd_QmmzToiJpjcX-jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور با سرمایه کم، یاد بگیریم دارایی‌مون رو زیاد کنیم؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/680006" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680005">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر کار: پرداخت معوقات بازنشستگان احتمالا از دهم شهریور آغاز خواهد شد
🔹
نتایج آزمون ورودی پایه دهم مدارس نمونه دولتی و تکمیل ظرفیت سمپاد اعلام شد
🔹
سخنگوی دولت عراق: هیچ اطلاع قبلی از حمله سعودی آمریکایی به مواضع حشد الشعبی نداشتیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/680005" target="_blank">📅 16:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680003">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428feada65.mp4?token=GJ3v-Q5zTkmoLR7A2NJTKTuApTE8rte3hB3vj192bdTFEHRhYl1FSRRqVjJKOOPxxWG4paQuEZGeRrmM_a9AWON0wABeTMfC2PtBvXH_u1yKAOxAKJtYt_j_kmTVMLhbIODG5FjJCAAMR-EiJE84NRQcqAHjBMKagE4_DbOk2gf4pzSLZRGz7qEYDQLNYslHMGkQxjC2_dThCqv-p2zp8Jij7UXV8LO9bnTOhk1zA6DZn5WpoMMb-WlNyecPnbZjq67fVF-sM70qc8Sk6_HWQvHnUO0pdBMdqT0qa_3tWS0xodw1uJH0RwDYQ4WHME0ZHSowWcArgMnfIhZbgli6MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دارو چطور در بدن پخش می‌شود؟
🔹
این همان چیزی است که وقتی تزریق می کنید داخل بدن‌تون اتفاق می‌افتد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/680003" target="_blank">📅 15:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-680001">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6d8e98d63.mp4?token=THh5CgTCBvfTMBRgzCK7UgSVtB9OzwjTU457gaAOaE_VOzXhQvk9_eStj1KfvGBYE6uP7jkpmjSHaP3Ebdm93Vc9a-x40WziJRMaDaMSjkcL_TVMysADjb5Hkwby5jq8xWCq0YS6PDIJsBbtI2SOtdL0aNddgAMbeKSKzzWRpm68N1ugGBj3hyN9eS-_i9hJ9QnZ7T0z40BSLzOfeRnyGEq0Ai5y-YiXOxjveTl6q0mqgbuFgsly49tpKdzFjt4A1Ip3Y1iwV1Du6LHjubA5FbmmVtWVPX8ItUuuBlzm_fzLj4YKKLIg9vicNVni0Y8cbS-UKXnlkd6v1kYkELxHAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب‌ترین ترکیب طبیعت: پلاتیپوس؛ هم تخم‌گذار، هم شیرده، هم سمی!
🔹
این پستاندار آبزی استرالیایی هم تخم می‌گذارد، هم به بچه‌اش شیر می‌دهد، منقاری مانند اردک، پاهای پرده‌دار و دمی مثل سگ‌آبی دارد. جالب‌تر اینکه نرها روی پاهای عقبشان خار سمی دارند! انگار طبیعت چند حیوان را در یک قالب خلق کرده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/680001" target="_blank">📅 15:50 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679998">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
اتاق تهران، راهبری مسئولیت اجتماعی برای آینده پایدار اقتصاد
🔺
واحد مسئولیت اجتماعی اتاق تهران با ترویج پایداری و اجرای برنامه‌های اجتماعی، نقش بخش خصوصی را در توسعه پایدار اقتصاد تقویت می‌کند. برای کسب اطلاعات بیشتر اینجا
کلیک
کنید با شماره (داخلی۱۶۵۱)۰۲۱۸۸۷۱۹۰۱۱ تماس بگیرید.
https://t.me/TehranChamber</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679998" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679994">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YSQznovN28jPGzFqUJdUZMItTdWaNNliV18QGvlGDJ4tgf_RZJJMcSjSY5OoSRn7SD5BYp5eG5W4MN4wBQWMZ7APlwU8D5YI3nbDEzM5ObKuSmnXlXHzWS9tT79eDxTUb8LZN7hj31cEtf5sbesSWi5mGgwynrpWYpsWwLv3bXMZ6OllC7b9eYxLOhCVD6md75SwVd7JksoLxd4dh0Cil1r4llHXhogqnYSwJTQA6edb7XcAqrvVoZFGziRbQVQ4z2kELf7sFdn2ASRc8imyQnUuEO_3oVzcCQ2a4S8eniCFHQ7iQK0oIpVGy6_D37SXQjDAqDV4jtF7AKYn5GRXwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qq8Qq_SxPT3gUFk3N39Z-pd1SAPhcadOQyvsdKF_XH4aY53sXhllQRtip2dA21akspm_z-EW01SrPGm7WMxav6f9pT5yt-kSlVCV_C3xRC5Xx8Ni6PVWe1RmapnHbGVkM6pdt_BTwGmKNBKSyk47zq6rSW_60UiBcd0Ze-3VdWogRIiO2hopTDNXOQ-90UJV7E67uxoN4r8h80bkI_y9w1ATdrmRyzkJn2lJC8D00WXGAKZTKHtqddJzlrhi6mKmeyUzZSYSTgKIu12WOAJZXYdD8YVzwpQOoK2rYVLkKH5J5tocrnSu27ZgWryknr_PW8GdvNxbUYIWRg-62HRiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fY7zukPvwrEuhIY2nGFtE0q_h2KHcbWkgaElAJXHlEpA-F8vyTuwoI2AqHgr0iDNkAs_Ug5uhTQDBNHNgeTqe-ggifc3bj3a96q794xZ7EXm-DeTYJd9_vN-uMxxdtKMiLFfvgBO9Ps2aUSIxcX3THnAwIpF0kjcmnStbp2Z_q1E_vWmb_pzaeegXl1l9SZiGqWIKrZWSe_9QLW34tVoOJfgyV9FWBNgxMrf9L-l639i1Hsbz9sIZMSNkB8iv4f2xEWP02uUz-o1lAKsRLkgdGER9exF7SAQCXgKSsVwPPajOuoEpu5K3r2H7aZZOJM4hSqIM3HFcH75m9pymVM99A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cee229a5.mp4?token=HilZV0DvcRQMw_UdJZ-vd8LwjdpsyslWPJX_C43whIyO74IucomRKolD42v6mOeYzhOjCxhwGzuxYKDhi80RfZyp6_xAoBPxqugYXcuNA0epFcxkFGy6pwowDA0lQNwbhRskevL0r0aZQ-idYtS9OH5Y8J0fFBIhSp8sL23yps9PTU7BrP7Dm6q5D-D21n4FwIj5D389GDAAClqSEjr6aBU6uZu7e822iqKaI-erpuITPqX7-s7HnbE-49bBlCusxPIVONOUekn8OxDTcFdjrkWH9PQ45k52Q3Ex_DmhZowg4uKgEM5s0pY6-0x_B4vlR_vdhb9aaIZIBaxoohaTrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر ماهواره‌ای از انهدام ایستگاه پمپاژ شرکت STAR ENERGY زیر مجموعه شرکت ADVARIO در بندر جبل علی امارات متحده عربی در جریان جنگ رمضان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/679994" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679993">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d332845585.mp4?token=fwei3MYjSJKXpdF7Ycs3UfBFKl1k1C61rj8j59XtykLhXEtvnaWyPd5k6nXUDpkOG7oGIy5vYMzkbF1TALRfZLyoBXIs4ecII2n5GDnAlPysaEZUZ0XzWht-eaXb11vVskYbozTErmU9rnmi2odlY66upkFd6tYilIFEbyFuZnkIapF6T2G0cRy3VQxRCctIP1MRs9Sa18XlGxTX3_Q6XwXkL0S_Q0G7PE6B8bR6UenT6PjKCv-P0eBkECeFp__yXzJZFh_pOkvKYirsiPy-Kn6MZLItJom8Po7DcYx_pJdNdWJXVsoIy8Oehi0oTk1U7npqQqWpt1BHxsxnihxG1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای چهره وحشی آمریکایی‌ها؛ از ویتنام تا امروز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/679993" target="_blank">📅 15:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679992">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ba76786ce.mp4?token=hePW2MvCASeSWcXt-JLcvd4Z5QmftboDAkfhdQ8HH7Xxv1ibnovOar7T2OLLPgGlvl_nQqR-bST8P2liegIZrgGFAPZcXRlSEkF2kCGtBjYDsfrfYxOIHbyJ5BRJF7q8J2fA2jxhjN8wFj3sCdFD9uMl4Ajd-RR6xpHl1YNbn9A9yL-Ff5XGINzhXjnqqzrmLM_XDjw5gv6kJo-9jxR8zxgVl9UFKf-wlXr5ns-AEhtoksJ1C3XvO9YYlRV8Rv0xuIMvrnn1LIWkb7ULOu56jVG1vEPLjabZJm0_Lbi_K6J7b_FXcAt9dKdSwTYgWuyLKBYIOp0kXWKPY6Qb3cBoEBVQGBUIsbScqxQsFOshCjshzXILmENEFjL-LambBDDQYFBybkN1Pu5RQmbhU4jxL-tXS2FSHvQah0l_YWlxxvcppOaVY71Kzn9mospM8zScypH0o0bQ643aCOfZEZ6IPEcgzgPFyxGiFidaLUurZwC3nusSz5cH7PawM8urkaJ5HQkjQWJvxYQbBuiCdz9p2mxy1wS7-62RcWVSt1zy1RDjnBaMT6XPHnyr0dxiqA8WDWnJlXCXbbGYAfaav8nY29rINo3Tkc-eRQ5z-OKYDSQ3t-APcfiAv3hSmBmsV_46gECEjU-WWbSv8wqcl-oWJfrGRbhCk15IfsDvv6Zz4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت رئیس‌جمهور از دیدار ۷ ساعته خود با رهبر معظم انقلاب و تاکید ایشان بر حفظ وحدت و انسجام ملی و توجه به معیشت مردم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/679992" target="_blank">📅 15:30 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
