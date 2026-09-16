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
<img src="https://cdn4.telesco.pe/file/EqnfuJv3GHJ-9iBcSQcN7A6ESnJv8wtZOGq9175Xk5F7c29Om7CVoGOIm8RWJLBn3Uckemjg2mIvqIziDPcTyf_CkpepfNvO_KRhWXEykkiiMZM1yGmef3Tnck3hculPzTc89hAyXw8xxeHdFw_QkJA3lZ43ZfhW_YS6ee-UgkzMSYFoqL7vJtjyYNPzi7zt5LgHt5nYE6t4Uv4VdjRCF5cyN_WMDWlR6DWPdzvucMJNQ1HIGT0PVj-jS29-5PC8p2KTDX42o70fO9z55tktRSgEmeeg4Bh4FzQpmqma4FwAxqhw-YpUszTuI0UUus9CmWaYbYdehhXEvZ5yRolS4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-140147">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJ-iRc4gYsOIWuWdzVTqiJBQEqqj2AaTFPvIjY46ESgqd5fgTfi0_W6ItzSIWAlLO9TFxPXRR34YyLzXeXJMu7P3kIURRKLKw8gzXjb15kOphuYWEjE9btLq34vyiHRpUtAGHwJdeICxTYuhDag1G5su_a783MRw8a7HRXbc-SxXFuW5o6pPWk_UC7qk372aRUApOIsSYXFSVRYt2XenjPgfEEQLdekjJmM-KS77wFaxh3nwMt1Z-a65e3d7IowgY7q7khrcSKOMsF58rQulkyxT1iAxOwqyvHLe2lQ55ewRZq0u2sEacjTLOHH_lHSrgOZqTyL_lFwA3ma6B_QCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب؛ چندین بازی با چند مسیر متفاوت برای پیش‌بینی
🔥
⚽️
امشب کنداکتور با چند تقابل جذاب از لالیگا، لیگ برتر و اروپا سنگین شده؛ از جدال اتلتیکو با اوساسونا تا میلان مقابل بنفیكا و منچستریونایتد با برایتون.
بارسلونا و لورکوزن روی کاغذ شرایط متفاوتی دارند، اما بازی‌هایی مثل میلان و بنفیكا و همچنین اندرلخت با لیون می‌توانند معادلات متفاوتی بسازند.
شبی پر از بازی‌های قابل بررسی؛ جایی که انتخاب درست، بیشتر از اسم تیم‌ها به جزئیات مسابقه بستگی دارد.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/SorkhTimes/140147" target="_blank">📅 13:14 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140146">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibSsuLhg4iBKo4TPhY9WQWvZWMuLLmDcggrvZdvsMpD4ceGJYNE_phuas_2Dl4Hd0DV_o4naZ1Smo45-Se4Z9KZ4lN-56j4K_GOYc36IYwrrR3lM9WinHsn9g2_zncJZkl5wc_xL-hjuSB938wFWf0wmCIoIbzkvJ6URQ8dpILd-YvA78DoUwF-Z-JPwBc1sIEsAFqswDiCYQvTuQNf9klmMrTpCTa_RhUQjEcvK9MPUkSI1s4NUUSc08umZu4E-rxr8B2U9Q_4mIIU6posWPFFwJF4zpQsfDnggfix4tNfgMdi5JZs7kNi7qdmgzkxSmk6BZ7ZiMKOOqsrpHBC57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔹
ماریو توکیچ دستیار سابق برانکو به پرسپولیس پیشنهاد شده و درصورت تأیید تارتار به کادرفنی تیم اضافه میشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SorkhTimes/140146" target="_blank">📅 12:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140145">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTTy9RdZcNJTVxXcG5Km4-3TPRU8l_MMAucSX_-N-Wfnez0ULb0h28oa-C3YyWazNwFZcpJiCLtzrwkE-OEH0t0V56cxX0-ZPBo_f-QQ1tjdxus7uLgKiAgcqHUCddOyNXC4clv95TE5A02cFxT4NL1WHfJurzSwdivvVfVXxZfjVQCG8K7svLio6CU3fC1VNUdGM1KhV5xgAhYB9gjH2Ksz5SMKxi5cT9TF9QQkFjqVT1Hm47HBwCGfzFN48aGDtHl2BD819IxKuHmyEs66wqDYXmJ7YcsanlAn2kFATrAke8LkQ4nCtyHhwPojgWQuKtgQjFxMJV6uUrr0xgJd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
با پنجره ی بسته و کلی مصدوم و محروم و فقط با ۱۲/۱۳ بازیکن با علوان زاده ای که الان خدا میدونه کجاست و ادام همتی که بنگاهی شده رفتیم فینال آسیا.
✔️
✔️
با برد جلوی السد برای کی کری میخونید بدبختا؟ اخرین افتخارتون تو اسیا کوپا امجدیه بوده که چند تا تیم محلی رو بردید سماور گرفتید . حد و ظرفیت شما همینه پنجرتون بسته ست ولی بازم تیمتون پر ستارست با برد السد میخواید برید پای سهراب بختیاری زاده رو ببوسید!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/140145" target="_blank">📅 12:20 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140144">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
پرسپولیس فردا به حای بازی لغو شده با خیبر احتمالا تو یه دیدار دوستانه به مصاف تیم شهید قندی یزد میره و بعد از اون تمرینات مدتی کنسل و بازیکنان به استراحت میرن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/SorkhTimes/140144" target="_blank">📅 11:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140143">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=JM9XeQZUjQmM5b0DZgr0pdWgtFwB3iWTCFAwNQoYWJcM4Fv3XhNfhMELwYoEic8_ItSVVLOpf2Y-ZOOpOgwqVzYzg1-93JItoPnanPEhssjBWCOEMc9o16fMcL5xQDaDndTb1tM7OhofTudN8Qw-T0To9LD5R3wDDzyMhEFXoDs-23wChZOZzIO9x7WWCB-l-mS6FdFUrgtXqPbNyPW-AwcS0To7OMnJZ9Su1tspGoNpC3uI_vgSj1cLKgk2N_tr9i6wV54ldp15WasRk-IBKUU3UjFVQex-GOwPqQ2uT3nOlVJOidKp5rn0C3Pl61TwzIVoS8zyLv28_0glKsyBow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f24687d0a.mp4?token=JM9XeQZUjQmM5b0DZgr0pdWgtFwB3iWTCFAwNQoYWJcM4Fv3XhNfhMELwYoEic8_ItSVVLOpf2Y-ZOOpOgwqVzYzg1-93JItoPnanPEhssjBWCOEMc9o16fMcL5xQDaDndTb1tM7OhofTudN8Qw-T0To9LD5R3wDDzyMhEFXoDs-23wChZOZzIO9x7WWCB-l-mS6FdFUrgtXqPbNyPW-AwcS0To7OMnJZ9Su1tspGoNpC3uI_vgSj1cLKgk2N_tr9i6wV54ldp15WasRk-IBKUU3UjFVQex-GOwPqQ2uT3nOlVJOidKp5rn0C3Pl61TwzIVoS8zyLv28_0glKsyBow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل سوم ایران به امارات توسط مزرعه(89)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/140143" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140142">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=KJkHMf16-cOYirhh3p1zyx4ErBsvmn4dAgsC7mFOdEYgKahLrGWzYvn0-kA-H-bEWKK47aPB-SIN_1Vhe9o01xEf_gDFKoTXc6o0Q4wWmdw2wq_R0pk2df0Z0WVuEjOUswyqO7cqj-fasDglJb3jwjtfusGdlijMq9CPflxEf2c5ndfL8SmNK9fIhBSdVe97ZtauyoSKzKuh8pfyL2re915xayB87qm-T_1lLLPVJmw-B14WNVeYAtMHzqPVmLvsn5oDex8z5IRvuCDVfXAY6HHW_x-qoIZqiEuPk0AyZHJeM_DAGaQ3bBsK0TRoyqy2sc8QguYjiPBmxbLiooMdAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6962fda1a.mp4?token=KJkHMf16-cOYirhh3p1zyx4ErBsvmn4dAgsC7mFOdEYgKahLrGWzYvn0-kA-H-bEWKK47aPB-SIN_1Vhe9o01xEf_gDFKoTXc6o0Q4wWmdw2wq_R0pk2df0Z0WVuEjOUswyqO7cqj-fasDglJb3jwjtfusGdlijMq9CPflxEf2c5ndfL8SmNK9fIhBSdVe97ZtauyoSKzKuh8pfyL2re915xayB87qm-T_1lLLPVJmw-B14WNVeYAtMHzqPVmLvsn5oDex8z5IRvuCDVfXAY6HHW_x-qoIZqiEuPk0AyZHJeM_DAGaQ3bBsK0TRoyqy2sc8QguYjiPBmxbLiooMdAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل دوم ایران به امارات توسط پوریا شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/SorkhTimes/140142" target="_blank">📅 10:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140141">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=N0k4na-oP9Kj5RS4-ogqXC77SWAkfauKxJqFdaGBorPoaNyimEvb5m9lFqNs5fkijGm9Wl9hyjRRlA_HqNNENpdwRQEJuKiaZPRzMwh-K2J5GcDEs80_N2ho9kHReYekV8G6_xHeVLM8yRXD_MTKcN9De0iUy49JrkmN8JSuJked9Nyf1TFTmzKF_Got7EYBZhnJOOjh_YVLTAXuFzt3hEOwPSE--cgT8wQWzR980nhpoyBjVQ3ccx9ywa7X9ASSijalOX-SIa81SujOrxQKEDq9nasxF6KhjSPaZsha_ttjGmRfEigiayX_zjf_Nh5le_sti_WFYDiK3Tx-uUtL_T2DEuEoNKlhxgHChJ5K6FYbGyJrTk5VV1Q9mFAiLgux9tQgWCZ9l7zhLvo5o1wGsnhDv3aJZ8MDZvrzjpLWIRwDRwTZR9luOH_rtvEdFA2nLAXRLWPJy8E1HL_kl2zwKUV3fUnSAMdaw5lqaFc_51hmBHsqWs7MiEnAkXUMUGixHYw3smzAKRQUBru2Vb9gsR3R_Ubjz7AfIb4bEwiM0caJ-F0fOCs9kQqDRjpIQevSRnJ32NbEaz1Kj7qXKJ_DjNzVcLe4-8i707v8iwpXg2vhs9C1-x7o21YvODxjCgNqIxRwc6ivG2KKL_2nyijrjP6wDwIOaVefGj41dvHVdsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0c59ac2ee.mp4?token=N0k4na-oP9Kj5RS4-ogqXC77SWAkfauKxJqFdaGBorPoaNyimEvb5m9lFqNs5fkijGm9Wl9hyjRRlA_HqNNENpdwRQEJuKiaZPRzMwh-K2J5GcDEs80_N2ho9kHReYekV8G6_xHeVLM8yRXD_MTKcN9De0iUy49JrkmN8JSuJked9Nyf1TFTmzKF_Got7EYBZhnJOOjh_YVLTAXuFzt3hEOwPSE--cgT8wQWzR980nhpoyBjVQ3ccx9ywa7X9ASSijalOX-SIa81SujOrxQKEDq9nasxF6KhjSPaZsha_ttjGmRfEigiayX_zjf_Nh5le_sti_WFYDiK3Tx-uUtL_T2DEuEoNKlhxgHChJ5K6FYbGyJrTk5VV1Q9mFAiLgux9tQgWCZ9l7zhLvo5o1wGsnhDv3aJZ8MDZvrzjpLWIRwDRwTZR9luOH_rtvEdFA2nLAXRLWPJy8E1HL_kl2zwKUV3fUnSAMdaw5lqaFc_51hmBHsqWs7MiEnAkXUMUGixHYw3smzAKRQUBru2Vb9gsR3R_Ubjz7AfIb4bEwiM0caJ-F0fOCs9kQqDRjpIQevSRnJ32NbEaz1Kj7qXKJ_DjNzVcLe4-8i707v8iwpXg2vhs9C1-x7o21YvODxjCgNqIxRwc6ivG2KKL_2nyijrjP6wDwIOaVefGj41dvHVdsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
گل اول ایران به امارات توسط شهرآبادی(49)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/SorkhTimes/140141" target="_blank">📅 10:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140140">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/140140" target="_blank">📅 10:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140139">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaAZR1A4-S227nUZNMQ-edxXrkMQDIrXJ9jtHxYld4yY6Mbhfb4bBYXtB-QqRFT0B8i54avXQI2YyHBdALn6dUQET6aBfC9z1abiFPc8ZxtsiaYEgYYRrGQttO-0yoxFH6L4k1r-rOGOo2u2K2uZ19x3Vf69JAc3wfdW7inKpncdZRloBYKLyoKW6PGh-5gmXW73zL1-bOse2kb41plt04aeYdCSfANjPTqQIDZ0AbaxkmmQrknHlkJjHv_uQwn-hG_orXuNdKmKcuMiaEdJEoV8lZC2qGcjlnmrpS9Z9M540bZK-6r4_d_PBfylr1V4XOSttTm8fHKL4aBvBSZbyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🌏
بازی های آسیایی ناگویا | گام اول امیدها با برد مقابل امارات
🇮🇷
تیم امید ایران
3⃣
🆚
1⃣
تیم امید امارات
🇦🇪
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.14K · <a href="https://t.me/SorkhTimes/140139" target="_blank">📅 10:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140138">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4roGZzlW8qwRNAr2exb7QZnDT1LfY1SwBYyx7lgXKRLyb1hvG6GpO7QZ8j6Y8eUF0mG4C6M2OFHbyUw6Q5eKBaL_s2_2GS5t6QsdZt8KOpJTzK-IbbkDwjy4-zefV4w7JmPUeBQm_mPMlcQbo53GXGdRu7pVdH3mSVmdYI2Nje0M3IezJS1xoWw_hySTbOVwTnA3qK5E_rqPotHBM3No0j7yzyTrEy67XdPlyvFgdWUo-0ykBk00UvOJspWbKIzvukoEAxgDW6FImp0XVdeOqB6pGwZr3F4-sbTkt61Z4_j_AMb9g6l23F7rEsRyKlkTo4p88PVapgJ-DS8QCoPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/140138" target="_blank">📅 09:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140137">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/knLFBoBJfYdYr72xOq_mQXhTsAN-ZicytYYJCSmJRXvUzYjzQKdNNkDw20FpEPT0Z_08XjeQTnTjhrkCamYEJY7bFNCMP0v0GcLpFFOPNU7H9nxCXhWx8PbR2XANJB4mzmzq0Cb06gsM_jMvtcC18I0_b03qwWUJBlro2AiTLg01u792QAIJGIBDkv4slOid55qG46PgzrEGeRf2M9W7UZmJwUABVVdmI4PkfSUa_oW_HdCyN1wAT7XpLOGBlyLaot1KYNlI0zEpQbpN_-KpIg33PRTxmjwDVubEU7-PYUlsNwawXzsXLG1FAPdqgANJxNSaHRFzr3mA-FSfFEX9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بونوس ویژه اسپورت‌نود
🔵
با هر واریز بین ۵ تا ۱۰۰ میلیون تومان ۱۰٪ بونوس ورزشی تا سقف ۵ میلیون تومان دریافت کنید.
🔗
آزادسازی بونوس خیلی ساده‌ست؛ فقط کافیه یکی از این دو روش رو انجام بدی:
👇
📌
شرط تکی با ضریب حداقل ۱.۹
📌
شرط میکس با ضریب حداقل ۴
🟢
مدت استفاده از بونوس ۲ روز می‌باشد.
🔗
همین حالا واریز کن، بونوس بگیر و شانس بردتو بیشتر کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
مینی‌اپ رسمی اسپورت‌نود:
🔵
@Sportnavad_bot</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/140137" target="_blank">📅 01:23 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140136">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140136" target="_blank">📅 00:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140135">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZW3M64wk_HzYYgc-G-fXphfVm0UYBNm6hLOfZwM-YapPXkbIIaQUWat1OsLdefblLzJxsfywzJWlHHtGb8Uc8yEjhjZ_C3u4_3RTfTgF-bgggqJy2YzYtqa-UB9bMR_IXH6gHw30rJUuPKVDfzCjIOf9EXK7aYo_aPKmCOTkxRXHd0UD3sr0EVrUvW73aGXqwwTZQz2-NaWxBo32XkI6HvZuxL0ZmQCitB6YN5bUSDuVnoEqGZOFzM5ttReHW02k9yfIGY-INMrgQ8HAhO9Ec_huF1DvBJilLcR8MAHPndtrUjrcs7cXouKp2zXJ99fjY1m2fOw2i6c1npmthbPvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
انگار بو جنگ میاد
✔️
کارشناس صداوسیما میگه امروز به مراکز نظامی دستور تخلیه دادن و دشمن میخواد مقامات رو ترور کنه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140135" target="_blank">📅 00:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140134">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=KDvpEGu_irC13BQhPcjM2VZER3vgEO1357LwjZeICS1CpU9yrp60ikrf7fAmhS2Rc84bjdHBXi88EvDSQP6zvHW8ZJMs23OVLfadtlMMSGdSIadEPa7-18lTo0TMGLjiihkLulP5hxz6esI0CsoTc1n6j1ISoaJu4ydv5W5OZ7fFch8qNmm-a85I1h3G-GXsAQPTBQUaZP_Ttlr3MYgomJkYcATGAxP6ax-u5Gaprt58YaLI4qM-GZ0M5qc63xdEBN1ZOQc3zi8HIFJGeaiEAqBKvWnwXgHuebErli8P-ZR7XshdsLOCkWn2dSAUDf1vzuGHPjsx6Z0-QnK0ATU72g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3657efb8.mp4?token=KDvpEGu_irC13BQhPcjM2VZER3vgEO1357LwjZeICS1CpU9yrp60ikrf7fAmhS2Rc84bjdHBXi88EvDSQP6zvHW8ZJMs23OVLfadtlMMSGdSIadEPa7-18lTo0TMGLjiihkLulP5hxz6esI0CsoTc1n6j1ISoaJu4ydv5W5OZ7fFch8qNmm-a85I1h3G-GXsAQPTBQUaZP_Ttlr3MYgomJkYcATGAxP6ax-u5Gaprt58YaLI4qM-GZ0M5qc63xdEBN1ZOQc3zi8HIFJGeaiEAqBKvWnwXgHuebErli8P-ZR7XshdsLOCkWn2dSAUDf1vzuGHPjsx6Z0-QnK0ATU72g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
پویا پورعلی، پسر خاله حسن یزدانی است
آیا می‌دانستید؟/ ورود همزمانشان به کشتی و راهی که در نهایت جدا شد؛ خانواده یزدانی و پورعلی همه پرسپولیسی، به جز پدر استقلالی پویا!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140134" target="_blank">📅 23:56 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140133">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=hkLS3zG5ifZsZz-KwL99TrJOZ46hBUmW3BDAx2gWwfiWHSeY2UwsxOs2Pw1mR4rUoQgBhztlWweZUQDFIsgT_SVsh9qQc9Svb4ALyXINAd6JPzfJ31vec-Z-upTGFrvZTr0TE4DYgtG0ZTb7oeMihFGwVRkWNY4MBnDR3o6A5dixcI5xlG63JHBDuQiUXLY3oJCApIqJv6tkhdT3LUcSINUYZDONZoJzKFzYLiogO64DxvUsD5Qm32DC4_C-ImxYLL4gZ6yOZ3QuOd2FxBnbAmwXVIs9jqJB1iahHVcH0ZvtSf-qhX-6hq2KPOrsLBp1QIVRIk8w1m4ZAIFUj2bouQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9adb7db192.mp4?token=hkLS3zG5ifZsZz-KwL99TrJOZ46hBUmW3BDAx2gWwfiWHSeY2UwsxOs2Pw1mR4rUoQgBhztlWweZUQDFIsgT_SVsh9qQc9Svb4ALyXINAd6JPzfJ31vec-Z-upTGFrvZTr0TE4DYgtG0ZTb7oeMihFGwVRkWNY4MBnDR3o6A5dixcI5xlG63JHBDuQiUXLY3oJCApIqJv6tkhdT3LUcSINUYZDONZoJzKFzYLiogO64DxvUsD5Qm32DC4_C-ImxYLL4gZ6yOZ3QuOd2FxBnbAmwXVIs9jqJB1iahHVcH0ZvtSf-qhX-6hq2KPOrsLBp1QIVRIk8w1m4ZAIFUj2bouQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
افشاگری عادل فردوسی‌پور: درخواست وحشتناک قلعه‌نویی؛ از ماهی ٣ میلیارد رسید به ماهی ۱۵ میلیارد! چیزی به نام قرار سفید امضا وجود ندارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/140133" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140132">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=WYpTgQ6Tik5M_jktKKvb_7-9izZkecFzLD543RQBkpzU1uJ0xZB0dfjP4jWmbreQo8Xi-1-R3Wwebeu-RKS80JMWIs8sbz__Ti2DwKM90QV25EspZtYsLEaqgGd62TIMNSdVLA8pIXjNhJezltVEjEn0F8OmR3ldABf5MI8OGn58ITGcKjGIkXDRfNFHu-UhOm1-ir-SsZsGC-47Wxwh5QcT1hOfK9G-nDxiqKf_bHnOz-GgggqiY6yqVU6KSvlKSMDqoEGLkwgf26kI9PXXeLb4lzxExQvEwORFJQOxoCbKWhXud4qp-sOdAV3JauqDA7nG5h0H7hG28W1ZH0ALgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d778bc850.mp4?token=WYpTgQ6Tik5M_jktKKvb_7-9izZkecFzLD543RQBkpzU1uJ0xZB0dfjP4jWmbreQo8Xi-1-R3Wwebeu-RKS80JMWIs8sbz__Ti2DwKM90QV25EspZtYsLEaqgGd62TIMNSdVLA8pIXjNhJezltVEjEn0F8OmR3ldABf5MI8OGn58ITGcKjGIkXDRfNFHu-UhOm1-ir-SsZsGC-47Wxwh5QcT1hOfK9G-nDxiqKf_bHnOz-GgggqiY6yqVU6KSvlKSMDqoEGLkwgf26kI9PXXeLb4lzxExQvEwORFJQOxoCbKWhXud4qp-sOdAV3JauqDA7nG5h0H7hG28W1ZH0ALgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏅
💛
🎙
واکنش عادل فردوسی‌پور به اسم‌های روی پیراهن بعضی از بازیکنای استقلال در بازی با السد: مگه خونه خاله‌ست که هرکی هر اسمی خواست بزند؟ یکی نوشته گودی، یکی دیگه اسم پسرش رو زده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/140132" target="_blank">📅 23:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140131">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=odzEdUqPPv6Lq8IPpj8QgcwDgXM1w-Vz7_Qm5oDJOfO73d9Q2xErnt6UG8uJ0f8aMwNNFzWdjXAmf2DZZgRybES5UF56-dERV_nHkdVHQgpdIgH33v5pmUl_RQLfmLJGic0doXmeslm3b6SRqP2TLBx28GcULg946ROrkhC2RzM9tD9LgmP-q8c03-0OH-7-9uwjv0gN6ZlqI888rqtLesYO2cuoaZUAKIZTWlH51TgfVCg33CCHXSN2YMGh-_l0uu4XWsJnTT3cRXH8oJZAWcxZ5TY078vwK01Ej5mKnfH-vrVJnJu-sF6zTZpwZDXzFuLMFNVBoKZK-oePI1Y8jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9929527fe.mp4?token=odzEdUqPPv6Lq8IPpj8QgcwDgXM1w-Vz7_Qm5oDJOfO73d9Q2xErnt6UG8uJ0f8aMwNNFzWdjXAmf2DZZgRybES5UF56-dERV_nHkdVHQgpdIgH33v5pmUl_RQLfmLJGic0doXmeslm3b6SRqP2TLBx28GcULg946ROrkhC2RzM9tD9LgmP-q8c03-0OH-7-9uwjv0gN6ZlqI888rqtLesYO2cuoaZUAKIZTWlH51TgfVCg33CCHXSN2YMGh-_l0uu4XWsJnTT3cRXH8oJZAWcxZ5TY078vwK01Ej5mKnfH-vrVJnJu-sF6zTZpwZDXzFuLMFNVBoKZK-oePI1Y8jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
محمدمهدی محبی : این همه هوادار داریم ولی چمن نداریم، شما کیفیت بازی اورونوف رو میخواین ببینین باید بازیش جلوی مصر رو نگاه کنین، بنده خدا تو این چمن نمیتونه دریبل کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/140131" target="_blank">📅 23:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140130">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
پورعلی: الگوم آقا کریمه و هیچکس هیچوقت به سطح آقا کریم نمیرسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/140130" target="_blank">📅 23:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140129">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❤️
پورعلی : من به مهرداد میناوند قول دادم یک روزی شماره ۱۱ دایی کمال رو بپوشم و انشالله در آینده می‌پوشم ، می‌خوایم قهرمان بشیم و آخر فصل جام رو به روح آقا مهرداد تقدیم کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/140129" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140128">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I05QC97LDBiakkJoDrGL88lQbJzIwOzqmCgEd8gd0U2gy4jV_MF0rm_aZ4SaQFpTMjkHkjTKg7k-PvEnX6npwuP9tU_BtdLaUisbyAeynU9_ztpAt9owdXMkg81jDE3Azy_IGv9RKSZM-neJLvZzVtuPEuR00Qx3rqIWBk0iIHJL2f4uroMFgmkcN4Xcrb1gF0SY5oxG6jk1hGS57NBigCFooFL4yZ9lU6JprBHCPpBa1aIkoEUIP4AfTMlZJAx6CbH5fX8nDoN9uB_BzyQi-sd34x281FP-c1LoXbvVeLLIC4RrzCd9v5d4qbPNxl2ZB0isEuwfudNbVeP7CWCRgaoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3207916b83.mp4?token=iMwrPrVXNo_X4QSLjBEEFKy6CjkpOSwRbDmHVK_H_om8AFx9t2H0IXat8dA-pAFomjX8k5uNW7RlwiW9qqLPKc5WhKeS0nQvvb1jDWB548PLAC4CBC5hw1AlfQqTiM9zl1Ejnp7WXxbZ3LSpzTwwsS1ABSfOSQQuOzVWAID3FLFXtE0lddaiH5KJnAysb-17h6lKbAK7748fu7C_qiwvn1_Uadb-oLTTmPs-sSqt-vYc_zMdmD1dI8EU5kJIGddQwCwW0h4trlH8WSGzkIyJdl6qrKT69C7aOTZFfssn7d1F4kKP5szTrmR2UjPwKMETgo148WrQvYq3-YIUku1I05QC97LDBiakkJoDrGL88lQbJzIwOzqmCgEd8gd0U2gy4jV_MF0rm_aZ4SaQFpTMjkHkjTKg7k-PvEnX6npwuP9tU_BtdLaUisbyAeynU9_ztpAt9owdXMkg81jDE3Azy_IGv9RKSZM-neJLvZzVtuPEuR00Qx3rqIWBk0iIHJL2f4uroMFgmkcN4Xcrb1gF0SY5oxG6jk1hGS57NBigCFooFL4yZ9lU6JprBHCPpBa1aIkoEUIP4AfTMlZJAx6CbH5fX8nDoN9uB_BzyQi-sd34x281FP-c1LoXbvVeLLIC4RrzCd9v5d4qbPNxl2ZB0isEuwfudNbVeP7CWCRgaoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💬
محمدمهدی محبی: خوشحالم که در پرسپولیسم، همه خانواده‌ام هم قرمزند!/ سیر فوتبالی محمدمهدی محبی، که پای او را به تیم نونهالان استقلال هم باز کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/140128" target="_blank">📅 23:36 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140127">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">📹
همه‌چیز از مصدومیت زارع، زیر دوش و در حضور پویا پورعلی شروع شد...
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SorkhTimes/140127" target="_blank">📅 23:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140126">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
پورعلی:
✔️
حاج مهدی یروز سجاد(پسر تارتار) رو اورد و یجوری باهاش رفتار می‌کرد که انگار نه انگار که پسرشه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/140126" target="_blank">📅 23:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140125">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
پورعلی:
🔻
من نزدیک ۳ بار میخواستم بیام پرسپولیس یبار نیم فصل ملوان که بودم و بار دوم که از تراکتور میخواستم برم گل‌گهر قراردادم رو بسته بودم با پرسپولیس و فشار هواداری نذاشت که بیام.
✔️
من و حاج مهدی رابطه خیلی نزدیکی باهم داریم و رابطه پدر پسری داریم…</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140125" target="_blank">📅 23:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140124">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
تیکدری بازیکن پرسپولیس: مهدی تارتار یک مربی بی نظیر است  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140124" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140123">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViJzlW09kaBiKMp4ByvNgbJmADwV5x6KvPfK69EVzqMYbB8Zv3kt6xYtGBIh6S9GWgeEW_CUvHP5recDLfz3SrM46dS4JUoXzHP5fKeSu0JnQWJZ4WV_ZF6e9ZYQAudyV6BoNzEJ6XwPubsu451xXeU3i65LwS-r_i6LEqCVW0opNFajYUxqVccHhJVu_bwbv-LjYDsLuW3pdOLAe_P1EQzq-BsmRZZd9KGnTrzSQxSsX2DECZD6GcKJD-l_gnb5I0ZcwBnrgJSJIvyZXWyTfE0_MSPI28FRXeKRxnwGom8QPWBohMurblxbOy6hmCSsd4ceo-43v7-7lLtu9Z8TTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جادوگر استقلال عالی مینوازد
😂
✔️
اسماعیل بن ناصر هافبک فعلی الغرافه (که سابقه عضویت در آرسنال و میلان داره) مقابل الهلال اخراج شد و بازی با کیسه رو از دست داد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/140123" target="_blank">📅 22:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140122">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
فوری ترامپ: آماده حمله دیگری به ایران هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/140122" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140121">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1HBaAYqG8jbU2YCs32osoFPFeJqu_C3UzBZ4SmQqGpxMV4BIJrMc2t3uOu5OOY_dhKSBjmORbBXIqEbK_8Eblh5_LDlfI2SjxvCSlAY71qoLDjVsMmYtrqo7balKW2RmqEJBvgKEaRLxpMhXoiYkpt2GQBjXx0LCzJtFR7GJIKU7yB5tw0yq29yGBDeXcqIqFY3AKWtfb4ubkfxyFx95itxX_CoM7kEtNa3n043TrGHQ1dlygrI_tk7tXVk-1BpPa1CJRR2SyadpLKaRxnKktb5fiQBrIhEtzOPVgGEZQ3ZimoW4jDe_QBJu7vrHYaz_SbDLXF4moHbOcoYvV8Rwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
جام اتحادیه؛ لیورپول و تاتنهام، نبردی برای بقا در مسیر جام
🏆
🔥
[
لیورپول
🔴
🆚
⚪️
تاتنهام
]
⚽️
لیورپول و تاتنهام در جام اتحادیه؛ جدالی حذفی که کوچک‌ترین اشتباه می‌تواند سرنوشت بازی را عوض کند. کفه ترازو کمی به سمت لیورپول است، اما تاتنهام می‌تواند با ضدحملات خطرساز شود.
🔵
بونوس ویژه اسپورت‌نود، با هر واریز بالای ۵ میلیون تومان ۱۰٪ بونوس ویژه تا سقف ۵ میلیون تومان دریافت کنید.
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
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140121" target="_blank">📅 22:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140120">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnjDA7fJ1dN3PKUQapdf9ArY9PxGAfw9BOly3Oc7LUNACSBl4Ga8Qbt_Yjq40H_6yM-1XHk2AkH-WuwzQFohOmfG3UpuLHYBPDZw8EaysZkbEhkztRNTbFl-joto69XMH-AvpJuVB71Wn9likEhbQ3GO_Il9WSmZAEsX6Ij1PdUpQh0ibezQqPEh99QXlBrhpANHVwcfMeRQO-OkGxnG-5fAqRjcAzbp9wrYAjEv2cT_4EZ1z37AK3UQuFcvwwT2be6JzXAjy_15xErQSJBNOrp6OX_Zv9yriDSr6dCnQBQjyGbJvmdxg5WQKRuu2DtwdOQlLYF-GAjy3WluS1ABTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔄
🔄
عملکرد یاسین سلمانی در دیدار های تدارکاتی
امسال پرسپولیس: ۸ بازی - ۴ گل - ۵ پاس‌گل :
پ.ن تارتار به شدت راضیه از یاسین
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/140120" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140119">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
الجزیره امارات با مالکوم ؛ کولیبالی و تالیسکا و بیست بازیکن خارجی دیگه با گلگهر هیچ گوهی نخوردو مساوی شدن!
❌
پ.ن تیم‌های عربی زاییدن امسال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/140119" target="_blank">📅 21:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140118">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_Ex7F5zY1cvTaq2dTlDg2r-pOdk7BsRcEzPZLcwSZQLvGIojWtj1FhaV2jsBw6rCXtUb79ZlbsTLpWguBnISxSRrbdv4zVwNpIrSFqhMtZjDHQigESH7zBLBudcPkqyq_39WshHqlx8a4yEQmOJpqGMdrGE_ydaRs7mJzXg4ybKqTpP3rKq6qmdfRh9k28E-OJOJ1MtkLS6Llh8keWmA04QTRI5CmcK_kvf-F5UApLIhdO6NdGciGfYyeh2_Uo__I7lTMhrhvPQEhST5EJHhFaM3qRgAPs2WidlxXJRrJgLjmeJ5aE2Aa0jo7eJ-6IufTiGyM5VThal5pviYjIKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏅
🇮🇷
نیازمند، کنعانی، زارع، عیدی، جلالی، خدابنده‌لو، تیکدری، محبی و علیپور از پرسپولیس در فهرست تیم ملی حضور دارند.
✍️
طرفداری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SorkhTimes/140118" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140117">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6zb44E5KY7CFpFNqO89MCzUVuW_wUDFg2dCtr84CZdhDI0a4IlZWIdxW-mEHTjikPhCGpRJcg3T0VbESiaDO_LgAqhP4nSzB-KUcbM2iAj1hx-yzXsYZ8cFLNtYUIpdBTZ5PLMgwZ2oHcT2ibFNKDK5ljIG0DhY8xLD3UNnrkYK9WPI-44VjZby6VNSRGhsdbMWfxH6xbaxxC4ch199WQZtr2rL7ciqImAet3kL5Xt4u-_L4HtJbxqxs7wckl_9Ylg-DOUm5bb4Zjnvc2IHvQY7Ly3K0F8ZsTqnScR1EpZrKEP-jWK0M3RG__cMJKnvhmi9ScY9fcDX2y28cZ0Pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
ایران ورزشی: تکلیف دنیل گرا همچنان مشخص نیست و باشگاه هم پاسخ روشنی نمی‌دهد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140117" target="_blank">📅 21:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140116">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✅
✅
اخباری زمان خواسته تا بیشتر فکر کنه چون یه پیشنهاد دیگه هم داره و میخواد جایی باشه که بازی کنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/140116" target="_blank">📅 20:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140115">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">❌
❌
تیما عربی انگار ریدن اونطرف الاهلی که 2 ساله پشت سر هم داره قهرمان میشه دقیقه 90 تونسته به پاختاکور گل بزنه و 1 بر 1 کنه
🙁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140115" target="_blank">📅 19:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140114">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">✔️
✔️
#فوررری
🚨
باشگاه پرسپولیس پیشنهاد اولیه خود را برای تمدید قرارداد با اورونوف آماده کرده است. قرارداد او در انتهای فصل به پایان می‌رسد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140114" target="_blank">📅 19:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140113">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⭕️
⭕️
⭕️
باشگاه طی روز های آینده و تا پیش از نیم‌فصل‌قرارداد اوستون اورونوف ستاره 26 ساله‌ازبکستانی خود راتاسال 2030 تمدید خواهد کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140113" target="_blank">📅 18:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140112">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
🔻
🔻
🔻
سویه جدید کرونا، کاتریدا نام دارد!
🔴
مینو محرز، عضو ستاد ملی مبارزه با کرونا، در گفت‌وگو با #جریان:
🔴
کاتریدا، سویه جدید بیماری کرونا است که در اکثر نقاط جهان شیوع پیدا کرده و بیشتر در افراد مسن مشکل‌ساز شده است.
🔴
این بیماری، برخلاف قدرت سرایت بالایی…</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/140112" target="_blank">📅 18:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
منهای ورزش
✔️
عکسی از افزایش عجیب و غریب قیمت دارو.
🔄
شما دیگه سرما هم نمیتونید بخورید. چون یه بسته آموکسی سیلین شده ۸۷۶ هزار تومن!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/140111" target="_blank">📅 18:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SorkhTimes/140110" target="_blank">📅 18:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">❌
❌
❌
پرسپولیس پیشنهاد تراکتور برای نیم‌فصل رو رد کرده و اصلاً قصد نداره اورونوف رو به رقیب مستقیمش بده. قرارداد اورونوف آخر فصل تموم میشه و موندن یا رفتنش برای تابستون هنوز مشخص نیست.
✔️
خبرورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/140109" target="_blank">📅 17:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
✅
اورونوف نمیخواد جدا بشه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/140108" target="_blank">📅 16:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d87f4723.mp4?token=T_ic9VAlr-PrqlW48cOfnNvScZdnWp_R-XtRD1tQ3rUH3GtzUR6D3GatQ5DzKZgiYKofJiIREmDqdnz6eNRudWZ9qQifSyIZOQdFRkptk7MAh0O5fgGORb11LuX-RPxJ2dnNL9Z8RCdqiZiWjvYOGEBhPGVwERV6wqQzdC0S90UIc3c89RjIm2fxPTEJSuJ9nW0f74tx2_8REH8R12YPlSV9DlMrr2_KFWqp1VezPyTEYf7YzIVwz3vBJkXYeMX74LM62x9jGAMm9S8JnOKi_T-V8g-Kb830OypPol-n_Idr-VEf4DPxJaTm7xzESL3cVA5huWNGCBAUjn-fLwgQrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
پویش مردمی با عنوان فرستادن صفر بیرانوند بعنوان #سرباز_نخبه به جزیره سیریک در جنوب ایران راه افتاده
✔️
✔️
این بازیکن به دلیل پرتاپ های بلندش می تونه نقش پدافند سیار ایفا کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140107" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/140106" target="_blank">📅 16:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140105" target="_blank">📅 16:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔄
🔄
احد میرزایی، عضو هیات مدیره باشگاه پرسپولیس با جذب محمد قربانی مخالف هست و میگن لازم نیست!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/140104" target="_blank">📅 16:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Kl5gYFfIiZ3oeWQNsd20pARwIjZbrAzBlvryTRYwtoe1KQU5hYrgcuZXk9ZOsZ4B1AyX23N1GYd-1c4r65Faicu_HCmJZtST5Pz87K1uXfZdnzFuNI94ILjbyx-1hBfsicsFBL67ElQrUPMBad3b-LvLcqSwG1WlEW8qLUPvwZPbOW3euuYVvUN1_91HO-XoVIJNs6kmrgLzCrxWOR3uix98JUWmoYnbZ1OzzsQbicndZhJEt4sF9ibjk49UcHMfH49P-qhe8Bt8ZVchhDLXvwPU9wqRHTNIAzyMXyr4nIY1D-XYYBtgLrIJY8S8FY4zztnBZ9CoVFKTSA5FG9EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
حامد کاویان پور مدیر آکادمی پرسپولیس شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SorkhTimes/140103" target="_blank">📅 16:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇷
محمد حسین صادقی برای اولین بار در لیست پرسپولیس پرسپولیس قرار گرفت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/140102" target="_blank">📅 14:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">✔️
✔️
علیرضا بیرانوند در دفترچه خدمتی که پست کرده، بخاطر سرماخوردگی از کمیسیون پزشکی درخواست کرده اعزام او به جای اول، مهر، اول آبان انجام شود.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/140101" target="_blank">📅 14:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
عبدی: با ۱۸ بازیکن مقابل امارات قرار می‌گیریم/ بازیکنان استقلال و تراکتور روز بازی می‌رسند
✔️
✔️
زمان حضور رضا غندی پور بازیکن شباب الاهلی امارات؟ ما منتظر تمام نفرات ایست بودیم. مبین دهقان از امارات آمد اما غندی‌پور نیامد و متاسفانه او در تیم باشگاهی‌اش…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/140100" target="_blank">📅 13:59 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140099">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKKcXttJOtIW9qFNKvMtlcA1JeBXV9U7Cb4FsCasYyz2oFQhgskPScGwVLesgtsrcbsQW1PlC2DxYOcaPFoFDKO2OmenJVDDtl4odAF65kVIOSxLUyuPJfVKLv_1WaE7oNqtpRYV2kWmcXbJzv5cuLskUaZkiUllAZcIc9Kd9EoM6uimnQZE8o2TzXETLlNHTll3p-K-zJKmNqbd5uNK6Iv_MkCOtbiFMziYewTj2u-zkQ-nPgNtst68-wOXfprhMWmcEfI-PtHNvKrVJaY-1zlTDOhHDo3mECh1K8XFIpj25HjkkHnk3ouVHQX7bNBlE3PRQuNAdVXWHrMZY59r2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
🤩
سپاهان باکیچ را می‌خواهد!
❌
گفته میشه سپاهان به‌دلیل عملکرد نه‌چندان خوب هافبک‌های فعلیش،
دنبال جذب مارکو باکیچ
در نیم‌فصل رفته و محرم نویدکیا هم تأکید زیادی روی جذب هافبک پرسپولیس داشته.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SorkhTimes/140099" target="_blank">📅 12:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140098">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">⚽
امیر عابدینی مدیرعامل اسبق پرسپولیس: مدیران پرسپولیس عملکرد خوبی دارند؛قهرمان جام ملت‌ها نمی‌شویم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140098" target="_blank">📅 12:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140097">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gntdzQjOtuekfuha1_XtahmHY9ysU0k_3j2LNFeXIiH3z0zp-SlbSRf2Vi5LtPrBMypqZgRsYgDJvOBfbE1RpUuHOV6XGXhrMMoVPZoAD6M03RtHejwY0ZAAwZMsr9IwuGA_VzAa9J32vWh7CQ6LsJ2AgxNHnhcxxtKTSozZDQYPJp9IQW9NdpukgzRGXgO9Y1E4yvOUcCjlC4-VMe_8WBEZkPAObtL9gsu9oJq-l6vbwXUkw72SvqhGrDtA1b6nI0NoIMOv2HsbZ7504R3mAfDRl_ItVVF0hi6WWGdWBqFsLrcv2pNMbhGcSip2xDQcgAdR4Bdnwx2PevP8F4y3Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
Liverpool -
⚪️
Tottenham
⏰
Tonight 22:30
🏟
Anfield
🟢
لیورپول با وجود احتمال چرخش ترکیب، در آنفیلد از نظر کیفیت و عمق تیم دست بالاتر را دارد؛ مخصوصاً مقابل تاتنهامی که در چهار بازی لیگ هنوز گل نزده است.
اسپرز برای جبران فشار فعلی احتمالاً بازی بازتری ارائه می‌دهد و همین موضوع می‌تواند فضاهای مناسبی برای حملات سریع لیورپول ایجاد کند.
کفه ترازو به سمت لیورپول است؛ برد میزبان محتمل‌تر به نظر می‌رسد، اما چرخش ترکیب می‌تواند بازی را از یک‌طرفه شدن دور کند.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140097" target="_blank">📅 12:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140096">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">❌
❌
❌
محمدحسین میثاقی:
🔄
🔄
طبق دفترچه‌ای که بیرانوند پُر کرده، باید به فجر سپاسی (متعلق به سپاه) برود، ولی چون زمان نقل و انتقالات لیگ برتر تمام شده، گزینه حضور در تیم لیگ یکی نیروی زمینی که متعلق به ارتش است مطرح می‌شود حالا باید دید این مسئله تقسیم چطور حل…</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SorkhTimes/140096" target="_blank">📅 11:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">✔️
✔️
پیمان حدادی: از کمیته انضباطی درخواست دارم هرچه سریعتر رای پرونده شکایت ما از آسانی را صادر کند زیرا میخواهیم این پرونده‌ را به cas ببریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/140095" target="_blank">📅 11:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140094">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axUp0zEFdxq8D5zRs9EkVmYHimkAEBDiD9vgKDPeoOD8HsE56B93o65m4dZ8QH4ar0EYwRPSeAkJ-io0EpJxBoBvW1-2A6PphJdSIe-61LDkIMpTD86mh8UDRt2Y3GQNoyz8FF7XHoGLSyJSxHaJPtSwkHkdyPmExMjQ3_gHtfLdUPV7TMq1hKLa-lSgx0TpqZS8-BdlhugtpWJmI8lVKveDCFasEfOaeIZAgHoH_BiLVkOfSSpBoeVYgNdvQKaC3BbxosWQp9LyAWiGCFtvFLwkLDUNH5jND6ZAmhYpUkwwlOH7AQpOSAalEKYDlh7rg6Q-CFTI71BJvKpAvw90lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرسپولیس؛ عاشق لیگ فشرده
🔺
اسکواد پرمهره پرسپولیس باعث شده برخلاف رقبا، سرخ‌ها از بازی‌های بیشتر استقبال کنن؛ حتی لغو بازی با خیبر هم با اعتراضشون همراه شد.
🔺
پرسپولیس برای برگزاری جام حذفی هم اصرار داره؛ چون با این تیم، شانس گرفتن جام بالاست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/140094" target="_blank">📅 11:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140093">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✔️
✔️
حسین عبدی: محسن خلیلی همین الان بهم زنگ زد گفت سه تا بازیکن مون برای دربی بهمون قرض بدین منم گفتم با فدراسیون صحبت کن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/140093" target="_blank">📅 11:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140092">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❌
❌
علیرضا بیرانوند: هراسی از رفتن به سربازی ندارم. دنبال رانت و پارتی هم نیستم. وقتی گلر تیم ملی هستم، اونجا هم سرباز کشورم. دنبال فرار از سربازی نیستم. همیشه کنار مردم هستم. الآنم سرباز وطن میشم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140092" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140091">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwoarVXdqZMtLWaifLtn5V9NmCby2udF6AJf7Imj72g5HgEOLQv4nhzvGumL0J6x_dD8_q53xCaFGMfS9UezprmboLQyUthfM6y9DTUWq12U4053FkRqqUJTPsiG3ZM111qpeXc5S2XkrZJafM9Vg0Cqpwx-c13EmtwgPDHqONSbQuVqHljyG9gbKhgAuECeSYYTt3ocu6i0WczveSZ1XKaQ_UFYW-ShKYhqrivvLvJq1TXcjalJAt-miOtlDYLHPpofaPiaXFOkgTuKpzLja2QsUbby5idBUVU3IoSmPetrb4NasIBSFiqnEERhPu8Ze2auVDIncKLAICcZXIw8wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبحتون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/140091" target="_blank">📅 09:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140090">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlPJLDDBkaTscfC3328sd-GWyJxcIluFoOm61dp7KY7Gkxfhffuu1y_fVCGmJS0iHGs2-YBbR601m9sjMog5XIfeDEOgOHqUv7m-oFpjqugg04SoM-IpqyNl1YPzPLyNCQJNyg8s6lSiapwQ9Txuch0paSOyRYBmeNWZ04QlGTY5xytXfi9NImd7S4uliCk_IpE3H40jsPIF00XF2NU9fwa59d8zwsFKdIcYITIoYqsuSQUUiRb-57eraWQOH5eo2ge9xSxuPGq6z0Z4YcqrG4qBPDD0mJh2TsUU9bacERrc2SMtcA_mGJ8QlIoqPyEWyY7VHQNd7v0qHYbVF1-DbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فردا شبِ پرهیجان فوتبال؛ بازی‌هایی که روی کاغذ ساده‌ان، اما داخل زمین داستان فرق می‌کنه
🔥
⚡️
⚽️
فردا ترکیبی از بازی‌های کم‌ریسک و چند تقابل جذاب برای دنبال‌کردن دارد؛ الهلال روی کاغذ شانس اول برابر الغرافه است و رئال مادرید هم مقابل الچه دست بالاتر را دارد، اما ارزش اصلی در بازی‌های نزدیک‌تر دیده می‌شود. لیورپول با تاتنهام می‌تواند از نظر ریتم و موقعیت‌سازی دیدنی باشد، در حالی که آرسنال مقابل ایپسویچ و فیورنتینا برابر پیزا با توجه به شرایط بازی، گزینه‌های قابل‌توجهی برای بررسی هستند. در مجموع، شب شلوغی پیش روست؛ جایی که تفاوت بین «انتخاب روی کاغذ» و «انتخاب با تحلیل» می‌تواند تعیین‌کننده باشد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/SorkhTimes/140090" target="_blank">📅 01:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140089">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
حداقل میذاشتین یه سال از حماسه ۷ تایی شدنتون بگذره بعد کری میخوندین نخبه های لعنتی، هر وقت رسیدین فینال آسیا میتونین کری بخونین هفتایی های جوگیر
✔️
✔️
کیسه‌کشا هفته اول آسیا: بریم واسه ستاره سوم
✔️
✔️
کیسه‌کشا بعد حذف: عشق فقط فوتبال اروپا
😂
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/140089" target="_blank">📅 00:57 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140088">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n63GOxmnOsP7W4JXCsC0hZEcsV0eGCyh0aEBT8jXQ1yyy2MsWF1fmX6WXXouAjp3Hb2-jAjt52U6OXQAhpWguvbYcAQn6clUuDeq-7T1eaOdSx_vsWMnXnxRgbpmXDvGShCZ4w8IXaIPQ1KKRsqWpimm9IawUGcBzYOMJeBahekj1724rqRJWZ_J82tpQmZgUpNThQGVGgqlG0FMApADLHOLU3YnpGmIWy_FvfGBs2FXzjYX7t3-8fWO_qdrEKG3Q35sx_dFOxs7Hi5ZUem9hSejGixCX60BHeSiVTdWQbd1oS2U1ZdaJdnjV4soKeTyiNTgvNUVH-L9_EuZ8ppe8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕
اگه برد تو بازی اول لیگ نخبگان تضمینی برای موفقیت بود که تیم جواد نکونام در فصل آخرش تو استقلال که بازی اول سه هیچ الغرافه رو برد هم ۳ گانه داخلی میزد هم تو آسیا نتیجه میگرفت ولی خب اون سال اخرش هشتم شدید
🔴
اتفاقا جوگیر شدن شون بعد یه برد تو آسیا میتونه به نفع ما باشه و اون اعتماد به نفس کاذبی که بهشون تزریق میشه کار دستشون میده ، حالا خوبه بازی اول بود و هنوز بازی با تیمای اماراتی مثل الوصل و شباب و بقیه مونده حالا که انقدر خوشحالی میکنید
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/140088" target="_blank">📅 00:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140087">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AKGcggQLwq6FYo_6j2W35_bAGAYkKK6YeJOuGslln9a5brbVyBMjTS7LvxLb4ZcZ2PsbU4hAfOD4ZivyN0rokVzIQ33F4V5gDRXwwf62ymsMISIJhYqqz_YfQruuapTHxUAQWqiJpBlAMBjL25XD0x0Xj9A7C2xUmvxHSGMhhAyFj9Vi6V1RB4hRBvacR4zvPBk2MqfoGLcuegW4pU7v98DKmcMPFazEwjm6vh4l8vaJ7_UAXXIB0wX2LKPqeLw_RVtYlh2iRlTiEQmMi3yvWzLdjzv0oOL6j8BldumB2Yq16pPVFnPB8TRenM5tQV2o2YifH_8m6xCSO0-aWCcVEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
❌
پرسپولیس با اختلاف بهترین تیم ایران در آسیا طی ۲۰ سال اخیر
❌
علاوه بر دو فینال آسیا و سه نیمه نهایی از نظر مجموع امتیاز هم عملکرد بهتری از بقیه تیم های ایرانی داشته
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140087" target="_blank">📅 00:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140086">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/140086" target="_blank">📅 00:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bu6gFkZkYMtuOIh1iSmlyv5sj_xyLtGW2S3k64gdao0hJq_KTic-x2aKbz7J28Y47JADXboa7NDDauhz0M7sRtN1vrhIUO2iGo2JTwWGz3NHuLKZ188GtH3fMUoiEIgl5GY9FL7gPmUaKq4UUax5GZS3FuFBtxrPC7GNhCa-VMvFGdN9v0_JGPZhQjMwBsuLJ3dQlaML0aK8x7Av8Lj750LGGeYxK7HiRcWenQ35zGaoapWwdEoHDS7smbqd_4rP-_o5IUspR57bADLRepnkH7N2HQSLGcfu7iyksf-xyeM-d4x8poB69EWCimZq-Pcb6jH94rKv-k6qUqs6eISphA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
یا رب روا مدار که گدا معتبر شود ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/140085" target="_blank">📅 00:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/140084" target="_blank">📅 00:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140083">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">❌
❌
السد هم از آسانی شکایت کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/140083" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140082">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SorkhTimes/140082" target="_blank">📅 23:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140081">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✔️
✔️
✔️
✔️
✔️
از داخل ایران مدارکی به باشگاه السد ارسال شده که در صورت بازی کردن یاسر آسانی، ازش شکایت بشه
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/140081" target="_blank">📅 23:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140080">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">❌
❌
السد چه قدر شخمی بود که ی گل هم نزد و سه تا گل هم خوردن ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/140080" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140079">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
باور کنید پیکان هم این تیم السد و میبرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/SorkhTimes/140079" target="_blank">📅 23:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140078">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/140078" target="_blank">📅 23:37 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140077">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/140077" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140076">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O5Utnn9Jqsz8Gl0d2m3-piVZ1MHibkeWCXL0Z5i6fZHY1ckAjc7qNgpm6kuCmSVPHUOlDiql1oUOQpBzIfWlm6qVQdXelFgpuJluRl1lV2ri_x7zOExPrj9SqdBodsmaRAcDPESEqp-fBBPQ8dVf8qMYSND941bDpc-svhaaV9JCA0WQm0ohQ4pNOLSfVDJECs3Et27OaHjcHFdrNwIKajGHc3RMxSXIDZR3F7d5WrgdGwPuj8BKvNCwIGER9q4n_kyCwYBXYlupqyuDc30njZSG0E8NsDf9a2iWOK0QRoqthJlsZ9C007w5N3OrjBs3FGLgIKR1Yu3k7EePdQWGh8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b77b4fb53.mp4?token=ufCh6kO1zqnUBuO5wMeiwllJlIp553uYZlpzLkbATE_XLGgZBalQ1MmB0GbyfsRZJoVC1ZMuJxeaOdDAPFlEgxjNcyhMcQZsEXhSAhu_z8nwE1z2I0jK1fpVLjskNgqEEmF0JFbgctajStLWqnhOUZN-9pd629W4Our5uA6gkmLVgQJoWQr3Z8qMsPtRyJC1Ji6U7AGeKuz-CFYq6dQ8VP6MNpfrOeUNC1Vk8ZgxMDN7sM3itLMjaLd-6E8rzGn-rh-kxNbwMLfnxEEwGR978jFqGSoebbbmkmTeF_NhufCEP1aqdjeyw43V7cSia0mBb0jMoPvvKj4PizmDL8Y6O5Utnn9Jqsz8Gl0d2m3-piVZ1MHibkeWCXL0Z5i6fZHY1ckAjc7qNgpm6kuCmSVPHUOlDiql1oUOQpBzIfWlm6qVQdXelFgpuJluRl1lV2ri_x7zOExPrj9SqdBodsmaRAcDPESEqp-fBBPQ8dVf8qMYSND941bDpc-svhaaV9JCA0WQm0ohQ4pNOLSfVDJECs3Et27OaHjcHFdrNwIKajGHc3RMxSXIDZR3F7d5WrgdGwPuj8BKvNCwIGER9q4n_kyCwYBXYlupqyuDc30njZSG0E8NsDf9a2iWOK0QRoqthJlsZ9C007w5N3OrjBs3FGLgIKR1Yu3k7EePdQWGh8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
جروبحث پیمان حدادی، مدیرعامل پرسپولیس با خبرنگاران درباره دنیل گرا:
✔️
✔️
بعد از فیفادی کیفیتش را می‌بینید. به او گیر می‌دهید تا حواس‌ها را از سایر بازیکنان بی‌کیفیتی که به فوتبال ایران آمده‌اند پرت کنید.‌بازیکنی که از اروپا به کشور جنگی می‌آید نباید دستمزد بیشتر بگیرد؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140076" target="_blank">📅 23:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140075">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/140075" target="_blank">📅 23:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140074">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">✔️
✔️
حدادی: محمد عمری پیشنهاد رسمی خارجی نداشته است
✔️
دو باشگاه بعثت کرمانشاه و فرد البرز پیشنهاد دادند که امتیازشان را به ما واگذار کنند اما چون زمان از دست رفته تلاش می‌کنیم در لیگ ۲ تیم داری کنیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SorkhTimes/140074" target="_blank">📅 23:24 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140073">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⬅
➡️
⬅
➡️
پرسپولیس در آستانه خرید امتیاز بعثت کرمانشاه و تشکیل «پرسپولیس ب» در لیگ یک قرار گرفته؛ توافقات دو باشگاه خوب پیش رفته و احتمال نهایی شدن این انتقال در روزهای آینده بالاست.
⬅
⬅
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/140073" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140072">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140072" target="_blank">📅 23:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140071">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
حامد کاویانپور به پرسپولیس بازگشت
🔹
حامد کاویانپور، ستاره سابق پرسپولیس، به عنوان مدیر فنی آکادمی و مسئول بخش استعدادیابی در این باشگاه مشغول به فعالیت شد.
🔹
کاویانپور این سالها مدیر تیم های پایه پیکان بوده که از موفق ترین اکادمی های تهران است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/140071" target="_blank">📅 23:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
❌
دفاع السد اتوبانه واقعا مرخصه .الکی گندش کردن السد و
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/140068" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140067" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxH405SHZd4vNyLKBolVjOZAaJCRuAWMEHo4C2NWCakqJevtmDjbhVU21R0OSXkxUTOsd5SjLTX6asKnLoi9guax_7_pF9ZvVrwoexYm1tBJ8flxTWUKFCGqJrS5qX_kvBW1kiYfa0kBHxdJLtNBc17dezaKRnFMiTT52kJGkY_X03fR39AVqRhkbuFh8HRXHe9YLZwYMDri-ViVIYpLWrTo5S_D1gRyGpYr8qMmc0E_BlxCkQ1v-Ha9PZt9sVi0F4dshx_izGbwuh-s9X5DgBFVGaPPO7CL29lbcZT4hw2FgT6d_sBTWHNq1tYrXihqWhzqRUO1siIbvbWHi3uvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟧
🟧
کیسه گل اول و زد به السد
🔴
گزارشگر میگه غول آسیا گل زد
🤣
🤣
🤣
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/140066" target="_blank">📅 22:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140065">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/140065" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140064">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">❌
❌
تراکتور که باخت حالا نوبت استقلاله
🤣
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/140064" target="_blank">📅 21:32 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140063">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
امشب ی عروس دیگه و ی آبروریزی قطعا داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140063" target="_blank">📅 21:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140062">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">❌
❌
ترکیب پرستاره و برگ ریزون السد برای دیدار با استقلال ایران؛ هرچی ستاره داشنه فیکس گذاشته!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/140062" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140061">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✔️
ترکیب السد برابر استقلال.
✔️
سعد الشیب، الساندرو رومانیولی، یوسف الحناچ، محمد الوعد، پدرو میگل، محمد منایی، روبرتو فیرمینو، کلودینیهو، آگوستین سوریا، اکرم عفیف، حسن الهیدوس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/140061" target="_blank">📅 21:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140060">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✔️
✔️
✔️
عملکرد مثلث هجومی السد در ۴ هفته اخیر
✔️
اکرم عفیف: ۵ گل، ۴ پاس گل
✔️
روبرتو فیرمینو: ۴ گل، ۲ پاس گل
✔️
کلودینیهو: ۳ گل، ۱ پاس گل
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/140060" target="_blank">📅 21:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140059">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHH1wqqc5HUg6OQRXgkzavwZc2kT8zyU6pSdfSstyspCI6q8AGMQakv1C2dH0ELKwyTWE4ZalMpDnzAYQTXCrlVGOerKpkBU2jjIwnaLNBKLCDsre2iz2T4Ta8aWEy34Gx-qkwrja_MRQjrh_7x6Z8Ut_sqmOdI6ddZJ5d-qZ3XXCCl7uwhVUI4Fzthn94ZhiSStq3RQDc9tovoMHo11x23ND4ccsiac1ZcSgoNa9nG8FFKIh0YaAGNxU5ydb0GrbBrIGUdJeEw_qSCW0iPkDmLGMTheTtE0pCzxycJx9EEvr_JTKgV-8irmzrgtbpfAOaBQKiXmQmUDD_CjCV5AsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
آزادی 10 زندانی توسط مهاجم استقلال
❌
باشگاه استقلال اعلام کرد سعید سحرخیزان،  10 زندانی جرایم نقدی غیرعمدی را آزاد کرد و آنها را به آغوش خانواده‌های خود بازگرداند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/140059" target="_blank">📅 21:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140058">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔵
اعلام برنامه مسابقات هفته‌های هشتم تا دوازدهم و دیدارهای معوقه لیگ برتر
✔️
هفته‌هشتم جمعه ۱۷ مهر
🔴
پرسپولیس - صنعت نفت آبادان ساعت ۱۷
✔️
معوقه هفته هفتم لیگ‌برتر چهارشنبه ۲۲ مهر
🔴
پرسپولیس - خیبر خرم‌آباد ساعت ۱۷
✔️
هفته نهم لیگ‌برتر دوشنبه ۲۷ مهر
🔴
پرسپولیس…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/140058" target="_blank">📅 21:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140057">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✔️
✔️
✅
تصمیم تارتار درباره تمرینات پرسپولیس
⏺
با وجود لغو مسابقه پرسپولیس و خیبر، تمرینات پرسپولیس طبق برنامه امروز برگزار خواهد شد و سرخپوشان پایتخت یک جلسه تمرینی دیگر را پشت سر می‌گذارند.
⏺
مهدی تارتار، سرمربی پرسپولیس، قصد دارد از فرصت به‌وجود آمده برای…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/140057" target="_blank">📅 21:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140056">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/140056" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140055">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SH1DhxtPUU4M8aWBka4aY6nvQfXYVcsvQDCRcpI0RFdD-RHbuCEchCSMo-RYh5onQ3jUsuOL5lY4kcXyDlMbwJvtg04w9k3uzDLc5EoSOZJ7tsrUd9s62iTKQKknCh5k6aXfWgsbsjEe54LoJbiSmwRYCY5EBOK6aRW0yUdb4p0BzE1dHCtUaU2008d2lMnJH1ZGpjbYX_cUVv6BacSMmKOiapgcmRm-vWFa_9uLUkYj3PXvLYtDKsiyV77oTHaY0ylA-wHJ0b0_d_QLROVtGD7gPR5f67pdutlDMRCgRnMRWd2mvxXRk0mgYrPovL7UwHlg1BKgGlFhYPfo1VhATw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
✔️
اطلاعیه رسمی قرارگاه جانفدای کشور:
✔️
از سه شنبه 24 شهریور ماه قراره هزار گردان مقاومت ملی تشکیل بدیم که شامل کسایی هست که جانفدا ثبت‌نام کردن.
✔️
قراره به این افراد آموزش نظامی و امدادی بدن تا اگه جنگ شد، فورا اعزام بشن.
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140055" target="_blank">📅 21:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140054">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=XK9nP_NJgg0JcRHYRvTBbOdocfVevunnA5YVIhnWIhgHNUxbc6jp4GFQaj5kSLezw-9tjKgcBRNZu6p5ia4Q7iiZF7X_tX8EXkhYoOGqM56AsUUkTn7hVd5Tt7Bg0X_dUU6s9tJlVOXVOL8WuSbhoq_wp3EZbFPb7QLYoV3s_ExXP7QZWmwaTQALIs6rilqnvM9445xTFgj5kb9uCpg18YKcJhaCz44xjTV2Z6DXLZmfT-QWBSDl8H0BqfS0ounrdTKxXQF7yhBOuG0Fwm2zL3wU7Er__CwNVVJ_g4LdiRXJ-uBl3qPYCjQvXwzA0SHcuuflPg_v3o65cgylC97T9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511d4f624c.mp4?token=XK9nP_NJgg0JcRHYRvTBbOdocfVevunnA5YVIhnWIhgHNUxbc6jp4GFQaj5kSLezw-9tjKgcBRNZu6p5ia4Q7iiZF7X_tX8EXkhYoOGqM56AsUUkTn7hVd5Tt7Bg0X_dUU6s9tJlVOXVOL8WuSbhoq_wp3EZbFPb7QLYoV3s_ExXP7QZWmwaTQALIs6rilqnvM9445xTFgj5kb9uCpg18YKcJhaCz44xjTV2Z6DXLZmfT-QWBSDl8H0BqfS0ounrdTKxXQF7yhBOuG0Fwm2zL3wU7Er__CwNVVJ_g4LdiRXJ-uBl3qPYCjQvXwzA0SHcuuflPg_v3o65cgylC97T9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟥
دانیال اسماعیلی فر از تعویض ناراحت شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/140054" target="_blank">📅 21:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140053">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
❌
❌
رسمی؛ ممبینی که صبح از سمت دبیرکلی برکنار شده بود، مشاور مهدی تاج شد.
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140053" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140052">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=JlTQFEnhXCUprj2oE9pcxgiTE13gbwIlwY2N7EVSJR2uzNgWJ787xkYWJRwkAKJHxqawu5SRTjiZlIT3tMAr9BN9rKkJpNbZXUgyb7SW9k8W_mp90w9zljRfP5CxnrUQdwopUOcUfMWG4-e4I1MCHg3TOhkerOd-Hl0n9IAvZu0KENCRGGvuQSol6zVEYhvSWEw0WqRpo_rPkoN-Y6_bah2spQsI6op55CztjwYKFrFRJ6WNsLiawoK66k8Dte_-u-OX5VMGHOhr6DtdMs7JqP2x2qTcT6tbskHkMobCtImNUgDkzraS2PulkRZtrgtDb5ay1mCloFTsDUQT2eOfCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238a9ee677.mp4?token=JlTQFEnhXCUprj2oE9pcxgiTE13gbwIlwY2N7EVSJR2uzNgWJ787xkYWJRwkAKJHxqawu5SRTjiZlIT3tMAr9BN9rKkJpNbZXUgyb7SW9k8W_mp90w9zljRfP5CxnrUQdwopUOcUfMWG4-e4I1MCHg3TOhkerOd-Hl0n9IAvZu0KENCRGGvuQSol6zVEYhvSWEw0WqRpo_rPkoN-Y6_bah2spQsI6op55CztjwYKFrFRJ6WNsLiawoK66k8Dte_-u-OX5VMGHOhr6DtdMs7JqP2x2qTcT6tbskHkMobCtImNUgDkzraS2PulkRZtrgtDb5ay1mCloFTsDUQT2eOfCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
سایه‌‌زنی شجاع‌خلیل‌زاده اسکل مدافعِ پیرسگ تیم قلعه‌نوعی‌ روی گل الشباب
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/140052" target="_blank">📅 20:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140051">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5804386d73.mp4?token=CuUsMT5W9m_STTkOhfQcIB_SJXvLSWxPE1O4dyo2QQSquRqwNVB820IoX3KJQp0XCel4_S1I9PN0VZEl74mxFMgGqjzvJ_zHyf39GjA0OSZID856Amk8Wp33tk-31mU5-lRH9fxRt8e-LGXELDZKOjL5NfHHwVQG7Rzh156X768DUpGh-62zaUSiCBDJqwhFxMpMK3ejHjWQtsUtnVmNUZXd66XkKIVB2gg9B3DxrUrnDi2YD1IUQpgVvb2wrpsMSi9Psl-GrQ0yM0pXlHpxJ7JvOel9UCizCBojMji3RWiWJiD4y72rcJWZ1yS2u-VcZ0ctzfrdiKYL-UeeUKQ6zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5804386d73.mp4?token=CuUsMT5W9m_STTkOhfQcIB_SJXvLSWxPE1O4dyo2QQSquRqwNVB820IoX3KJQp0XCel4_S1I9PN0VZEl74mxFMgGqjzvJ_zHyf39GjA0OSZID856Amk8Wp33tk-31mU5-lRH9fxRt8e-LGXELDZKOjL5NfHHwVQG7Rzh156X768DUpGh-62zaUSiCBDJqwhFxMpMK3ejHjWQtsUtnVmNUZXd66XkKIVB2gg9B3DxrUrnDi2YD1IUQpgVvb2wrpsMSi9Psl-GrQ0yM0pXlHpxJ7JvOel9UCizCBojMji3RWiWJiD4y72rcJWZ1yS2u-VcZ0ctzfrdiKYL-UeeUKQ6zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل اول شباب الاهلی به ترتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/140051" target="_blank">📅 20:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140050">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW_A3LHYq72ZHXFETbAPZ36z48RcWOvgWGLbp4gZkSuPjHFpjJlDVt2xR-ZG5vvPOVyaFwl46dyv3j__rf0tzpjCkrorpt_uB8f0g73fePKTmeFf3l78og1Li9Q7hv6MxAr7B-RX4-I9tgLMUPl7vyQcAkdSlwGXohw9zKLjd7oFUJppulk8gFoKpwMcuj5IXXhKGmyC-qfwPfGeGQqpENMc3jH6i0x9dnHFaLyc5805STC7RTNx4GQ4qsyta2P2Z5rcs6YOURkqpNzzkaF2ZHJ5CbC70chCyPGK1yly0qbt8dDUIVpEWLQElB_hf4WU7YNzFsu-3uzfx1Z3IDx7Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
Esteghlal -
⚪️
AL Sadd
⏰
Tonight 21:45
🏟
Basra International Stadium
🟣
استقلال با تکیه بر ساختار دفاعی منسجم و روند بدون شکست اخیر، احتمالاً بازی را محتاطانه و کنترل‌شده آغاز می‌کند.
السد در نقطه مقابل با ۴ برد متوالی و خط حمله‌ای بسیار آماده وارد میدان شده و روی انتقال سریع می‌تواند استقلال را تحت فشار بگذارد.
با توجه به کیفیت هجومی السد و رویکرد محافظه‌کارانه استقلال، بازی نزدیک و کم‌ریسکی در نیمه‌اول محتمل است؛ اما نیمه دوم می‌تواند کاملاً متفاوت شود.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
آدرس دائمی سایت:
👇
🟣
Wincobet.com
🤖
ربات رسمی مینی‌اپ وینکوبت برای ورود سریعتر به سایت:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140050" target="_blank">📅 20:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140049">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=LfIru_3-O6fKEAYYtgHDChZVbo-lC2ZdiZ_RxD-q3hu31Nm5gwnWPop-oKn5euhBLohcBiFqV6EbO3k6CvIB9kGfOnnoZV-cT2KigQ-Yv9s_264HDqM_-tzDwqypm4DBDEZUZpPQw5HLw-CMLQUYABeTNGU7GUjFy2B6m6X1omFkMBGVCto2cmAFGp-OLWjYBrxefQdwHO3Pl3i3jjz_EXxK5GJx2nqhlqUUh317PUP9s9x32Sou7g77BehGOKj0fkqBSrH0hL0l6Av3w_aB-ZWgVKgjGvq4z2szxtg9OddqBTHUjb1_C5LMFIk4N1qMyIg9ygrc0VizwGtlPb5grw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88ba81229c.mp4?token=LfIru_3-O6fKEAYYtgHDChZVbo-lC2ZdiZ_RxD-q3hu31Nm5gwnWPop-oKn5euhBLohcBiFqV6EbO3k6CvIB9kGfOnnoZV-cT2KigQ-Yv9s_264HDqM_-tzDwqypm4DBDEZUZpPQw5HLw-CMLQUYABeTNGU7GUjFy2B6m6X1omFkMBGVCto2cmAFGp-OLWjYBrxefQdwHO3Pl3i3jjz_EXxK5GJx2nqhlqUUh317PUP9s9x32Sou7g77BehGOKj0fkqBSrH0hL0l6Av3w_aB-ZWgVKgjGvq4z2szxtg9OddqBTHUjb1_C5LMFIk4N1qMyIg9ygrc0VizwGtlPb5grw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
گل مردود سردار
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SorkhTimes/140049" target="_blank">📅 19:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140048">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
✔️
ترکیب شباب الاهلی مقابل تراکتور با حضور فیکس سردار آزمون و سعید عزت‌اللهی   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/140048" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140047">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2yMrZ1j7bCjKZ1ABOojEtXA2TyS_g-6aEItHabIZ1zbrvYVzlrRohbruMMUEDX8RtfFbspu_69UAcoop99RocymlRvpHWYXz2eLrVMHIQVov_z6QL_bIFjNL1zCGkehnsZNxYuR1kSmMDFSbDNZWiSlh5LiA4QfoIwIe1qDShATLyC3hT8c2eKkQZA2MkkgtBD2gJv3v0igKrHydp_54kC-sWlpj5pvaqn8Rc535e8oGSJjZUhAsphMIeWQUevmTnv_rHBipe6NHwWBHGLeP2wdVnndNbPCcXzEXdvNlSbEBI26kBV-8lf-JsJnOrPL1e5593JMyyh8At7LAR95NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
علی علیپور با وجود اینکه پرسپولیس یک بازی کمتر انجام داده، همچنان صدر جدول موثرترین بازیکنان لیگ رو در اختیار داره.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/140047" target="_blank">📅 18:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-140046">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
✔️
علیرضا بیرانوند دروازبان تیم تراکتور، دو دیدار آغازین مقابل شباب الاهلی امارات و الغرافه قطر را به دلیل محرومیت غایب خواهد بود  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/140046" target="_blank">📅 18:28 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
