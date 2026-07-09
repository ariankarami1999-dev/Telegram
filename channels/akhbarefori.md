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
<img src="https://cdn4.telesco.pe/file/oS3HjtFqTy3dSLsVhC3-wZ0nyoCK7nzk6d5KvLIaAUzgFTRETWuetsMVllhAGVkhPZ4Xmqsf_aKtDA26CpxsEVbm0m4ImNgnqlDdGOSubgyY_jtQlLU0PSoVEINeB-ss6-5lNGNcHcqe0SqGpMgKFwb9l4wvjrlqq0Po-ayclVoe2Kjnj0BVumncU1zR7VLwWe2c3QInj8IEQehpl0AmLOpD0ass51qLrQ9TG7c6ggp1fwqq_2f0tGU0o4J5A2K6jNvI7fBLj8ndpHzSH7lk_0yJg3he8VyU7jQlsTmZFhpwnA5mqvyg96hsLfTV_G00mXzgod2vfbP2CNm1g0HSQQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-669027">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
بیانیه نیروی دریایی سپاه درباره مدیریت تنگه هرمز
🔹
نیروی دریایی سپاه ضمن اشاره به پاسخ نظامی به آمریکا، تأکید کرد مدیریت و امنیت تنگه هرمز در دست رزمندگان اسلام است و ظرفیت تردد در این مسیر به ۵۰ درصد رسیده است.
🔹
بر اساس این بیانیه، تردد شناورها منوط به رعایت ضوابط و کسب مجوز از نیروی دریایی سپاه است و دخالت آمریکا در این روند، بازگشایی کامل مسیر را با اختلال مواجه می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/akhbarefori/669027" target="_blank">📅 15:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669026">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
تکذیب شایعه تهاجم نظامی به کرمان
🔹
معاون امنیتی استاندار کرمان ضمن رد شایعات، اعلام کرد هیچ‌گونه تهاجم یا تهدیدی علیه این استان رخ نداده و وضعیت در سراسر کرمان کاملاً عادی و تحت کنترل است.
#اخبار_کرمان
در فضای مجازی
👇
@kerman_news</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/669026" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669025">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89acbaa58b.mp4?token=QfUiWUqnsL_Dl9LifssRbLzmWWt6SO8joodU12YPniNjGJXa7DsYlwxK5wtFHpnvd9pG3w0B1VvczVN0EOCkxfyexWpW3GOKpKlm_7RX0HxEpwM-Kt2AdatRl5dvNySr_FS9YPp4gSMLnUomL1r3w9A4WybIvi9iJfjIhfm5qs3jg-DLNrFd0VCnzirXFGXT46WoWzMN2E3_0b_cEi3DKgSXZC8IFczvpkNjOiY7RCWjoL7PKveA-GZKxcyGPfRjiClwTXSU0Pu8a3HE4LUJ3ghUOUfvvdysVzf7HeaaaktnI7U9X0KusHUIY1pcvc0-5fgRZ6-mdIUTXtdvCooAAlZWSvP0mEg057-MiTGIAze6eUaipTUffEIu1Y2V7KsACzL-zNucC2E_WT4noEL598ytgfsZkzGdSaoxhV9Jw_ivVrm3FtcSuTh7mIV0y2nJumvgbEd5xVMyaEA9jVVYuk0zMPP7cfitAoFsYRhkUlrZaVbluMoQ3bzXmNhSh83Hf6Bg1Bh0LDtF-6mRaB8WMWTUo8BcmOx7uZuLaaLvupz9M97y-h9aOdThPfpS4zhAnozzs0thvZpul6oZTdRg__MYQ5L_uXTxa3iqCkStQd4ka7eIZMdKTo8ZEWfdB8SArmjjwyGEZKIumyPjcMPVgayIHmpJefpLXraxe9tOYnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89acbaa58b.mp4?token=QfUiWUqnsL_Dl9LifssRbLzmWWt6SO8joodU12YPniNjGJXa7DsYlwxK5wtFHpnvd9pG3w0B1VvczVN0EOCkxfyexWpW3GOKpKlm_7RX0HxEpwM-Kt2AdatRl5dvNySr_FS9YPp4gSMLnUomL1r3w9A4WybIvi9iJfjIhfm5qs3jg-DLNrFd0VCnzirXFGXT46WoWzMN2E3_0b_cEi3DKgSXZC8IFczvpkNjOiY7RCWjoL7PKveA-GZKxcyGPfRjiClwTXSU0Pu8a3HE4LUJ3ghUOUfvvdysVzf7HeaaaktnI7U9X0KusHUIY1pcvc0-5fgRZ6-mdIUTXtdvCooAAlZWSvP0mEg057-MiTGIAze6eUaipTUffEIu1Y2V7KsACzL-zNucC2E_WT4noEL598ytgfsZkzGdSaoxhV9Jw_ivVrm3FtcSuTh7mIV0y2nJumvgbEd5xVMyaEA9jVVYuk0zMPP7cfitAoFsYRhkUlrZaVbluMoQ3bzXmNhSh83Hf6Bg1Bh0LDtF-6mRaB8WMWTUo8BcmOx7uZuLaaLvupz9M97y-h9aOdThPfpS4zhAnozzs0thvZpul6oZTdRg__MYQ5L_uXTxa3iqCkStQd4ka7eIZMdKTo8ZEWfdB8SArmjjwyGEZKIumyPjcMPVgayIHmpJefpLXraxe9tOYnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی یک جنگنده F-16 نیروی هوایی یونان پس از فرود اضطراری در فرودگاه زاکینتوس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/669025" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669020">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMU0toam_JCYoOFTUjMQGgahDkCMxfjYtU1KiM1DkKd4SYppjMkwdlswc0H2nIiK0ko7x4_sWAKUVYn-P5B0ZmaxyrMWDRIFI9S5sygzMV_Z2g_dWAvVCeco6KtrMjafcjZpJEmqUC5qTv8pNRwRFxd2C2sZOOBcDTuBrKRxWNNBZswpTzbL-MgdjbNjz1vjdbaB_Yi-CDCsyRfx7mT7VGs_J7qIkre4MbsMbI2itsNTiioyY7DbD7BOW2nukxpv6C6O-WyLyMlp27gj7KhaCA35YB7AyDZjDIfr33bKJUbbMkBxNgYazh_28XP9XsSvozd2QYs8u5eORH3fp5Rwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v834gohJnYFWMCC0_qbMKjfdbqGhq9Mr1rQJbIquGHPyKzekXDVtoNeUJc0U7HXoz_pw5Lp9ut91psbjLArM_CE0Refr9sLjSv8qC2tCJ0G70kkHmLttHqZeDPwFWaVDsV5cYJGO55JNrIMyF6lOZF5nUvF5V3VxYiNNFupiCUjJwgYUAPdFE0NyXb7kZbFAgzqpWYurLh7McSEtjHLvymF6MJsjK_zRH7uJpKpmProN5j70j9M2zewnC0JopG7gkHToZQc1Ebrg28kXq458R0o6QCQpZJEAM-G3E8IQHmNuHDpQ162gIky-jF5AGqztBpOsHUr7I2do2S4UQeyocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHcMkPSPJE2yF74vdioXYu4A14vttp9VuF_tKbl1ZgJV8du258QxlCFuVKS7m8TTZ5j0LHl29YP2Aye5ZzVwjshfxGxmyNSe5-2SLwEFwp5lhxEkX4l_5oBP1m818Yu6D0vH4_xU0tK4zagS49kzLDEJx7jdxkmcUoTpqKwnyyCXPHywzFzsXGtagVBmvgf2Ku4Fjj3Myk-E_LDPeBIb80ufpsjwB7hxm612cji7fL_ghEckR9SwunU0Kaw7HL7XMsp_FYPsJvgZlGNrvbP_rw7EIrqnOJbJJKeET1l-KpNK7lnTz_Z-QVPZjxakoef5gZL01Z-ZKJ1KhBKJVXaUDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BPjc4fniBb0jUg0ZGEk-HycWgSMIsBvc332dqeOXF9OZ5PPfP4iP6bmqpqCGSDh1avTPxTXWsh-YpG9i6LvKlAslq7hdaBHjGFi9KoKt1x-91LbHuhMEt8WBY9yiGUbRZJiOCxOd0zs-kIxrqGTFjZ2YmmsVF6qIDh3N2oyA9MqFe_KpyUiLTmbX0SbS-g5H2vG0dWkqWg-6P4Xc6qLYZ9lyxqnQvjBjktmxt7WkkelqZ6yRsvBq2LThjMfJEOF5apwF6SwedTph7pdLkpoXXvtFNxmmTIZ8Z2t9lFsHPBsE-4X77zC2ML8RwruJRx4XGTwPYjc2DRc7QuHnlcuIJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cacf1e7839.mp4?token=Sy_DI-Zv7Tf8kDPutZs1zmJGvWl4MjQwS73YPEAcZEnG9WxTbq7edwwNwrYXtBQF1xDBGYHvXWTbjIpEfo1gQqhNcueThHJaqbm5olUc3VeBAP9HwK2BeLQ3n57-irYtRiHtrmRcO1cgX8xF99ZUY-TlRBiygsGnz2ZuDHccTxuHtUIXuHGCHsH-7uo3MdfBICe9QoFYCmVp5bJ9TN8PyZY8ymdaWs-GITm_llaQNpdYNXghX4F_mT7dtQmxJEe1DFvQnF3_LkI2BeBPzHk6c6ZSVCya4KVr4fkWXL-oZxa9GsN_-iiPnJu-02y2Vfc4kVzOVPgkf-5GycGdNZESQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cacf1e7839.mp4?token=Sy_DI-Zv7Tf8kDPutZs1zmJGvWl4MjQwS73YPEAcZEnG9WxTbq7edwwNwrYXtBQF1xDBGYHvXWTbjIpEfo1gQqhNcueThHJaqbm5olUc3VeBAP9HwK2BeLQ3n57-irYtRiHtrmRcO1cgX8xF99ZUY-TlRBiygsGnz2ZuDHccTxuHtUIXuHGCHsH-7uo3MdfBICe9QoFYCmVp5bJ9TN8PyZY8ymdaWs-GITm_llaQNpdYNXghX4F_mT7dtQmxJEe1DFvQnF3_LkI2BeBPzHk6c6ZSVCya4KVr4fkWXL-oZxa9GsN_-iiPnJu-02y2Vfc4kVzOVPgkf-5GycGdNZESQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از ورود پیکر رهبر شهید انقلاب به مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/akhbarefori/669020" target="_blank">📅 15:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669019">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6cbce3695.mp4?token=i_xpFZK0zi18ccyCZAKB3zcoBtrSATNs9EdjyHx6p9k5vCDPrA0KOePo6zC_wxYHkcBt51rcoyACyXXS4rtZBf4lKjPQ7KGD0NY8J0Z9BLZAQR8BAQ5QzFADk5D2MDd6SrtmyeAT_4lR5s9Ly8QTRaGU2MIDZlG0ZgT4XCkYMNSrYi_AE_ITNCWGk4nnW5eJ_78p9XmHqQsPHVtBeDu1t9F7b7UO1dLpMknUuDIdlci1EMUbb-G4kdTnCmbCJpRKkMzxODMfc3kMjdT8m0lc_uoiV3zk9wFkarG-xqPSQSFIEKvnhBIBxIHTFf050uYhPCajCXpefTtCWMyTnVPNg6SaL2DJP3n87-8eYDp5HeAeCCwTuNF0G3Lsp-24m7b6uyF6gqjMFG5-NvuNjRyWK9r9Abs3m7jLwdBKKPfqSYq2fUlqJ9GFJ9omyE__32Ymo-Tdsv3Pef1-U-mND39wfsZ7UlFcgywtR84jdwf3chL5tpltPb9qOs3HvaK9sO0XzFC2vpUxYsoZiaGKar4OpPW9nEP2j6vZQ2LnhyB0SK4ORzLikS1j6kJNuPhwAUjQo6Plxz7HiEKDTm9QlZdycK7c8Okp6HUYDoYzBDO9N3R1vy6lR7bNMGjwzC2nJwJEt04Kjgn0Jj7bCdsv80e20vfFF4OUGLlie2h1aUMvWd4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6cbce3695.mp4?token=i_xpFZK0zi18ccyCZAKB3zcoBtrSATNs9EdjyHx6p9k5vCDPrA0KOePo6zC_wxYHkcBt51rcoyACyXXS4rtZBf4lKjPQ7KGD0NY8J0Z9BLZAQR8BAQ5QzFADk5D2MDd6SrtmyeAT_4lR5s9Ly8QTRaGU2MIDZlG0ZgT4XCkYMNSrYi_AE_ITNCWGk4nnW5eJ_78p9XmHqQsPHVtBeDu1t9F7b7UO1dLpMknUuDIdlci1EMUbb-G4kdTnCmbCJpRKkMzxODMfc3kMjdT8m0lc_uoiV3zk9wFkarG-xqPSQSFIEKvnhBIBxIHTFf050uYhPCajCXpefTtCWMyTnVPNg6SaL2DJP3n87-8eYDp5HeAeCCwTuNF0G3Lsp-24m7b6uyF6gqjMFG5-NvuNjRyWK9r9Abs3m7jLwdBKKPfqSYq2fUlqJ9GFJ9omyE__32Ymo-Tdsv3Pef1-U-mND39wfsZ7UlFcgywtR84jdwf3chL5tpltPb9qOs3HvaK9sO0XzFC2vpUxYsoZiaGKar4OpPW9nEP2j6vZQ2LnhyB0SK4ORzLikS1j6kJNuPhwAUjQo6Plxz7HiEKDTm9QlZdycK7c8Okp6HUYDoYzBDO9N3R1vy6lR7bNMGjwzC2nJwJEt04Kjgn0Jj7bCdsv80e20vfFF4OUGLlie2h1aUMvWd4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود پیکر رهبر شهید انقلاب به مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/akhbarefori/669019" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669018">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
هشدار سفارت آمریکا در اردن به اتباع خود؛ فوراً به دنبال سرپناه باشید   سفارت آمریکا در اردن:
🔹
گزارش‌ها حاکی از آن است که چندین موشک‌، پهپاد یا راکت‌ در حریم هوایی اردن هستند. فوراً به دنبال سرپناه باشید و در محل خود پناه بگیرید. در داخل خانه بمانید و به…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/669018" target="_blank">📅 15:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669016">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
پیکر رهبر شهید و خانواده شهید ایشان در میان عزاداران عاشق مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/669016" target="_blank">📅 15:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669015">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJUEM3aoN8Yt4AqrpsoxvqLzUDvWojpEQW5WX_UumZsFBpkp_La-zzWiQvCCOUwJG6Y8txxiXNxwrEi9kbQ3IMQ0G3R523Cfydstvsvf4ExOgjLP8cT2kjAX3qTuwI6jkEizhNAaydmXRpjRKuWXps_be3fosDt9iqGwAdfp-zc-WBjDtj9yggkyQs_82Ppp1z4FkvMEaG0gj8UVh4AW1B8VhjrAHIpvx9opIC9dENDihxegpKJXy2BKttm75k37Hvs3P7QeA-DVMRDHNTV4BLtSe_y-F_DySzrby1KzfYAHKDgwruJfXMbr1FR_TO74M25PZ9dwpL7Dp-4mkHJ01Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجتماع بزرگ مردم مشهد در مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، چهارراه احمدآباد
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/669015" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669014">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd16554b7c.mp4?token=Z6JGzvvtr-3z813Xd_Vlv1py0qxagHbhnjsrlJFgpiHQyJJs1clvcvDlPIjd95hqjBJ-WhNqKdQQWVlUSRLI68zXMUSBddxdZR1-jYS5ZDIvNyLnKqYq4mzq_PFscJp94XlPVTr1pzV02oJf8JtAzGssxVSfRYpCHtGLFRPqapjdr_AZ7g2E6K-qt62vGzWSqmyvFprMtjEobXuBIRHLHysccfabg2icU0H8iRjTEPpt1ZGmkHUsC1pK9jmjxfcCLtr6SzX06ixcL2VWGLq1fcKD_sawormF8rehL34XAazCfjkCu8C83-96rvBClwyM8fyXBWzcOnY2fx4_iq5RVVpjQ6S5_3mz2kTz9YttAPJGTVV162ZKsp8lfyW-FWB1cpP3l5zr77Bdp1U0C1pjJ2sxXecC7jmN9_Ml3GUix-LiDrb-dBYBT2_zjysO-HMzJ_1PD7NJ1A7RTNqHcyu5LzLflj5QLenHndrH0k6OdI0heLaoWgMdhi6k4gzzTf42JY67b378izh9j8F55LHTNcdF5v-2tUDg6aJQnQTp4d0GHEItdDfmOeIqqw-C8nGNfZfLlpkOsiB8xpeO6ADwQxS0zyqX9vtz9m5LS0ES4IMCOoeOuh1dmIQqRRw0KwlgB6XJHKoOqzkAdtoR6eL7W1EALV9Nvd8xm4l6F0ctj1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd16554b7c.mp4?token=Z6JGzvvtr-3z813Xd_Vlv1py0qxagHbhnjsrlJFgpiHQyJJs1clvcvDlPIjd95hqjBJ-WhNqKdQQWVlUSRLI68zXMUSBddxdZR1-jYS5ZDIvNyLnKqYq4mzq_PFscJp94XlPVTr1pzV02oJf8JtAzGssxVSfRYpCHtGLFRPqapjdr_AZ7g2E6K-qt62vGzWSqmyvFprMtjEobXuBIRHLHysccfabg2icU0H8iRjTEPpt1ZGmkHUsC1pK9jmjxfcCLtr6SzX06ixcL2VWGLq1fcKD_sawormF8rehL34XAazCfjkCu8C83-96rvBClwyM8fyXBWzcOnY2fx4_iq5RVVpjQ6S5_3mz2kTz9YttAPJGTVV162ZKsp8lfyW-FWB1cpP3l5zr77Bdp1U0C1pjJ2sxXecC7jmN9_Ml3GUix-LiDrb-dBYBT2_zjysO-HMzJ_1PD7NJ1A7RTNqHcyu5LzLflj5QLenHndrH0k6OdI0heLaoWgMdhi6k4gzzTf42JY67b378izh9j8F55LHTNcdF5v-2tUDg6aJQnQTp4d0GHEItdDfmOeIqqw-C8nGNfZfLlpkOsiB8xpeO6ADwQxS0zyqX9vtz9m5LS0ES4IMCOoeOuh1dmIQqRRw0KwlgB6XJHKoOqzkAdtoR6eL7W1EALV9Nvd8xm4l6F0ctj1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ موشکی و پهپادی ایران به پایگاه‌های آمریکا
🔹
سپاه و ارتش در اولین مرحله از پاسخ تنبیهی خود، زیرساخت‌های نظامی آمریکا در کویت، بحرین و قطر را هدف حملات موشکی و پهپادی قرار دادند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/669014" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669013">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa41a940a5.mp4?token=VGGOXlmTTtijWSkiZ0jq5988P8JH71cLHrUAVp1_j8F2GfZ_pQwKdE0G9BnPciiPXl3_VCQ3fRGjE0-aYir9zcuCcIf398VTpxs1ig05olJRj-Jt5Nqkw0zYXLveOKxBLztbhrCCJ0LvqH-lEsGUAl3k1qDBQfbV9Q78_WbSE0ZUgVFCtqpgfjrbqqrjIGmgoUsdxoHPsxJmQEyVd65kFrgg7qjzDs_PgJ2_X-V9uNtJBdkwvoe-D6tgnaRmHMnBDj5A9QEIoWy91n4zsXhkxgkwCvc9ZVyuledCNmdITP63JvAjBlgj0z-DyJ0qJOFs2QU_8uaeVmBjdukgPFriDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa41a940a5.mp4?token=VGGOXlmTTtijWSkiZ0jq5988P8JH71cLHrUAVp1_j8F2GfZ_pQwKdE0G9BnPciiPXl3_VCQ3fRGjE0-aYir9zcuCcIf398VTpxs1ig05olJRj-Jt5Nqkw0zYXLveOKxBLztbhrCCJ0LvqH-lEsGUAl3k1qDBQfbV9Q78_WbSE0ZUgVFCtqpgfjrbqqrjIGmgoUsdxoHPsxJmQEyVd65kFrgg7qjzDs_PgJ2_X-V9uNtJBdkwvoe-D6tgnaRmHMnBDj5A9QEIoWy91n4zsXhkxgkwCvc9ZVyuledCNmdITP63JvAjBlgj0z-DyJ0qJOFs2QU_8uaeVmBjdukgPFriDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صداوسیما: همه کشتی‌ها از سراسر جهان برای اینکه از خلیج فارس و تنگه هرمز بگذرند حتماً باید از مسیر ایرانی عبور کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/669013" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669012">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlBjoPNOnFlAn7erE-b5emUPxs1PlShWUIK_PwNbpT-ZtL3fRWSrQjIsaDrXhzKUzQEi1W-N1DpsDdyATO8M3wyZVXfvvDsHpiU6m37PGX8x6PLIv6GtXeYDI8k7tx7QBiuVtEGVXXkZyv8_OWB9acNgvvC5ifdHjSpBCM3_Oz4Tw3wt4xREfCsj8CKFw2ofw7iD146tYTaopN8LGJrTodxSikMDv8pig6BlnDIkJ_Gp8hzs-uDG3w5-7IkazfCHrWzwpxefjhk5HGDLr6drS5sBnqKKEGhe5_4wFlgrR8Dqw6krYT7rbrV2S41Z_fDS_oireRaIAgCpXMHnLgp2ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش مچ‌بند و پرچم سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با مچ‌بند سرخ و پرچم سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ و پرچم سرخ، نماد عهد، وفاداری و خون‌خواهی امام شهید است.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/akhbarefori/669012" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669004">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sGPwxEJMq1hycyc4fEkzwJJjADe8rnH5kL5PG-OGRJ66mLGpeXzielPy6mBNoHYqefZZfxqdF9Muo8lAjhCpm-pLNXFW5Wn4UMKtMN4Dg4qYktOLBqbscyZsQi6zBCspBwrohqNuaTlsB5XjyBEGozn29HDAzjqURvVXB3nsexbO74gFLRXvgQ4jUGHGPooLwGXWMvhfaqCB6xUjR3f-bMp6CJLoL5E71zwGKEB4SwSeRVh3TKrjj65ZC3gV3o3dudQ9qHBb9qpUwkqbQ4qMO-b5h5hNEkHkzc2sCJGJxfPazXt0IImGbeqD2clPudAMDE0CfHulOyh1Wylpv51QVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XMdCSUwCoQWemtxzntzeWLDNC6FkJV_mBZqY-OYpJfYygidSnIoWqeiXawZKrFhn3yFfek80KYmCbKKa6XDgdwX-eEosowDoOlzN83VZ_-gRsr_3nSZuVS_KAMbUfF6Gc3Mga5a9Mk0qh0l0v1Hr6hVO4sjl0j2IV5YGAokIcawuHOeAtIuSn6P-PJON6iBY0jlJrBOQ7D-8tLf3lVlj0spA8dL02RIwUixY0tYgGMcNWyWE18yuKR4Idy1zmRRQWEtJ5uOf0cJBFfxK4FEldQCBUvaQJNsHMMQslVeg3nuRfB_Hg-jZYaOWymUgTDji_wtcQDo9cHFRTe7CKknPcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQIDHq6a2vI5jHh2Az1W_QSUv82VZCBvLMWaAAgNC0bEAnhx8H4b8xG13mbqRy9_9MBsm_yLKNKD2uhMKsFaqVYYyAunY_4WgaSGM5Egd2h8_De3Rz6YDajlcUfvFIzezy0gFghDZd42addlgKhItMDCqGazpEvAKjN1NZthgu0_DVdaiF7fdJes9eH7uhc0IJsszDA_JE7N_Y8Z60i-wdv7lOWb27z5ypFsMtDD-5751XTHi-LHBY8D_Yab4D7zEVZUKJLEu5M6Aw0dLc1pPcMcWH3WRDHunl-eIu5SVozdT7Qs5-p9LHEBPvaMO-KP2l5AV-gWg8DlwN84rBkp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rzaCy6q5NLGzET9lduITzlxVX6_SGFJ2xhPyVyrv3yVtfX0EAKd34C2wMF1eUK5t0-RKCyl9MXsUt40CNPBOY_LQXy0wWvESn3BeXOz82WBO9AKjJZ_Bp3J0OOxXvfTMgD8EHJczmU3cYrKCnNFn0J8JMj8MNdXPSisYXUZgacC1tT2MZ0wjgrj5G7U6v0fRnuSkFJKvtbQ6b4C6h29YaOt9lhsMnB30ebjAnhDpUlZQdCqduoG8AXy9RIxdWHtzXjozdVPMLhwMgWdigdCGsxK6PJoJXkaFD3zrn-nJo3sJKUUzJozWSpBDeIUSIAF0DGC3WMEJc-xSRt36CENu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phhDwor3KW9SxyM0QBu1PY6Znp4U5b--tJ_b-XyW2HuF6eIqkHxyS8RNpZgQG9TGalUXPoRknAHxApHP1S_EnMtreVd94SfT1ow2fvfg2_ATxL94vj34QbhbF0K8H02e-No1Bs_0rFezV9bddTGELOLdERDKsE0LheVk72lZLTX-Ib0VxrZ12GVnH3qkYpE3h5Yy59Ih1Vxu2rhVzJwc_KFBKjvpkJXjepBNb7T5dNznXF0wu4lpOK7NfRhDZZIcsIaDr2pOg6waaQO7dwrYZ5pGHnVlGPbIOI2_csKy7pD5RouuXZSPE0Pga0EYCm0d-a7fDPkyWbsiFUOHFwbJDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LT8CLd6ewJIdxphuC6YKpAJjGosmJ4-yi273ICBIhqj6tSYMT3tKXWp07bfXMIjlw5J33abgFzCPkwRC8v7IhVCGSLMWw_2rpcJ1t2PUPf4JF00Q6QP7ZxI-AVvs_G6IwCRx-x_6N0yLF9d_-XXfKulgXvYsh0VtHKGAUf38FpIAGMKvd-cVJIIZfVFP3IfSGo1QRzkUDURHrcp4P0bUcwkVCw2W3H8lZ-v77w6Vq19EJSxanNfgxKqHoSM7nHswTzxVn59-RA-NYeH4qfitU245b0dftu6wafiSoGAd8_Migv4KQVRveI01Y5w0cX60_M8tT10lluhtGYQoyBCXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6aA6wY7cyIiiEj3zwMMf-habpCV9TJNB40rk_q9GM8pfotN332cRcC87St6DKPE3AjnmW1f1NJahsn3I4aMeAphL35rXK7_gvwdy_3PN3xObEosAY0YB_mnYgQiCNLbPmC0e6o8O8FbUYOspTB8y2bg810tWcZowtEBFjZptKTihguidrZXVxca8A9qIePH_OVTzfJ4aJVlPL_4L_snG7pCAyfdb5hol8wxOY5S2xLhCd6HFt1lROlpby3f--pwpIZhYi-4hXf6epRE-_hJqL_IgI8u0jwGCPNBbe8CPlDdKfwJf91Wdmm4Z4adwOXVuc7_FiyV0YVHiSPi9R4CKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_Yej8EA77fybJP28q6lRX-8A29PpMgGYxnyGDfuqnHSQn69vnkkWXK7GRTGR1e-OwC5_c1i7layZ_Iz88Gda8tZyHfldWiyRmE4bh7sr-1pFRYyP8flhEYZ1sm86vDDXfQguzR1enzH_ywzmGQi3FN71J5-C3AsQqxbHGrDMM3DZqrK2MYBPcKHPRj5u7O_42py_j44rmEK-yOrXq3BBuSKh7anFJg6lg0ydJQC0rRfDWxhqeA4MTc88sUQEV6-XCoK6jy2rPmqny9Xfl8Bq3IoChyIzg_FTn_xj9IK5rP3SUxuDAH2yFqsJzY9k9XKPJPI4ZSIaiiTluNzCVo1YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
توزیع هشتصدوپنجمین روزنامه خبرفوری با تیتر
#بدرقه_یار
در میان تشییع کنندگان پیکر مطهر ابر مرد تاریخ
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/669004" target="_blank">📅 14:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669003">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
صدای انفجار در خلیج فارس
🔹
حوالی ساعت ۱۴ امروز، صدای چندین انفجار در مناطق دریایی و غربی بندرعباس شنیده شد که احتمالاً ناشی از تبادل آتش در خلیج فارس است.
🔹
برخی منابع از فعالیت پدافند خبر داده‌اند، اما مقامات رسمی هنوز جزئیاتی از ماهیت حادثه یا خسارات آن اعلام نکرده‌اند./ مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/669003" target="_blank">📅 14:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669002">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
مدیر بنادر و دریانوردی شهید باهنر: به شناورها و تجهیزات بندر سیریک بر اثر اصابت‌های بامداد گذشته آسیب وارد شده است. یکی از اسکله‌های شناور بندر سیریک دچار آسیب جدی شده
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/669002" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669001">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
رسانه‌های عراقی: صدای آژیر خطر در پایگاه ویکتوریا در نزدیکی فرودگاه بغداد به صدا درآمد/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/669001" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-669000">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
پرواز جنگنده‌های خودی بر فراز آسمان مشهد
🔹
صدای پرواز هواپیماهای نظامی در شهر مشهد شنیده می‌شود؛ این پروازها جهت تأمین امنیت مراسم تشییع پیکر رهبر شهید و پوشش هوایی محدوده حرم رضوی انجام شده و جزئیات رسمی آن هنوز اعلام نشده است./ مهر
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/669000" target="_blank">📅 14:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668999">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b7b47f69.mp4?token=XeliRu9tVfdueLaWRGNEPHt5x111k5_E6EXhqb5UPSz4c_G4OKPMF8aQLDB9_XWa6bdgkpZYzZ8FsTJg0WtveHdtO9v4ZmE5ud3xTwJTPFl-tPDTi5koHEHVxBko3RbiggwTDB-bbKIrXEHvzr5iSE9SIn9YDWYKkRcurp0z_tvL87kgq5Fu6BxlxA7RVE0xaDaVQsLjgbl7u4tb438RYcLc1ufKPc1QkTOk_9sXKlOlyKoU_QFX8gJtkNSqekO_WgGTYNAJrDREySNS9TDgP_8wMXZp34N8QrhHbKjTcEifxBnANWWRWj_G2Gj0RcwdI4zEiKKl0cwCp4P5pBzTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b7b47f69.mp4?token=XeliRu9tVfdueLaWRGNEPHt5x111k5_E6EXhqb5UPSz4c_G4OKPMF8aQLDB9_XWa6bdgkpZYzZ8FsTJg0WtveHdtO9v4ZmE5ud3xTwJTPFl-tPDTi5koHEHVxBko3RbiggwTDB-bbKIrXEHvzr5iSE9SIn9YDWYKkRcurp0z_tvL87kgq5Fu6BxlxA7RVE0xaDaVQsLjgbl7u4tb438RYcLc1ufKPc1QkTOk_9sXKlOlyKoU_QFX8gJtkNSqekO_WgGTYNAJrDREySNS9TDgP_8wMXZp34N8QrhHbKjTcEifxBnANWWRWj_G2Gj0RcwdI4zEiKKl0cwCp4P5pBzTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از جمعیت حاضر در مسیر تشییع پیکر رهبر شهید انقلاب در مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/668999" target="_blank">📅 14:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668998">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H7mmSPoFQ6sApgFBK2rlxo2oozvQ8oW0KZX-_FhxXoSA65FgYL6aSZPk4rZW5NFYfLQ3p6cQCSFiE3DImSmw9wjvaTqtTWWOzndp969PCjyVzITnjl25NGrN05zDigyNuiyZ78hTpb0l85nntiEkzw2AnoHyznvPt-n9ILf329dpwVOj8WBfQF3xcUjsqfmB_K1AYG06ibrHH1kCzcOoq69Nj3X3az8j0sjPNo_DA8lKqrP9JA9VR8QwUmiIncZGlDN22pb9r_IQkLa4H8evicjmgGjT45km1xDBuhLww28Qtn91TJZ8--qap8VH7Y2ud56J3kNQ7eXkB1ILgMKd3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای تانکر ترکرز: خروج ۱۰ میلیون بشکه نفت ایران از تنگه هرمز
وب‌سایت تانکر ترکرز:
🔹
تهران به دلیل احتمال ازسرگیری محاصره دریایی توسط آمریکا، شب گذشته دست‌کم ۱۰ میلیون بشکه نفت خام و نفت کوره را از تنگه خارج کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668998" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668997">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد/ فارس
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668997" target="_blank">📅 14:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668996">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
موشک‌های ایران در آسمان اردن
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668996" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668995">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcc65c428.mp4?token=Y3FORRdxiHe_ohwZHRe2gltKqEeGWs46PeplOlHe4ol_FqQpd78SvZ0VjL6xaCsvtNJaew-Hz9mTk-BMx6-nw-lEwWiKaJzTSYTWdxwMUrhtg8xk8bHTBCmBrocDGP4TUpyVGzmMiK-OVvuH4BTt42bFrjeE6LAVLJE_zW563NTOHoRWrvqXuMbVMbdmMdyHvS8kXCAmcQFXSlmoBi6-pNts7-B8OxRAMKR8_SbCiDUiWufmB8ffj_Y06C2Jv5sugC4Mg7bomJDvYuZoe3AMTRjAn862M6p-sRMGxMP6ATy_un4f89jUwuVcztDoWmsh9ECS1d5BHB4tnS1tm9bw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcc65c428.mp4?token=Y3FORRdxiHe_ohwZHRe2gltKqEeGWs46PeplOlHe4ol_FqQpd78SvZ0VjL6xaCsvtNJaew-Hz9mTk-BMx6-nw-lEwWiKaJzTSYTWdxwMUrhtg8xk8bHTBCmBrocDGP4TUpyVGzmMiK-OVvuH4BTt42bFrjeE6LAVLJE_zW563NTOHoRWrvqXuMbVMbdmMdyHvS8kXCAmcQFXSlmoBi6-pNts7-B8OxRAMKR8_SbCiDUiWufmB8ffj_Y06C2Jv5sugC4Mg7bomJDvYuZoe3AMTRjAn862M6p-sRMGxMP6ATy_un4f89jUwuVcztDoWmsh9ECS1d5BHB4tnS1tm9bw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آژیرهای خطر در چندین منطقه اردن به صدا درآمدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668995" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668994">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd2fb8a1ce.mp4?token=tmP68fDBHSdr2Z9LkWQQVax3FzueGTuFFoWVIQtgrj0dGVEONrVpzY7d0F26_3tQqgRmJAUXKsSMdM_yrLli1u8I130eIwtQGlNAM-K4IyJ-SLv0ZeH3G_Ris9niILNwQiV8TOVP1MjGCWFyxCmnBjbbAjgOLANsfvQALrR4Jq4snUeJurXTb_hWCHmoQe5noCsnuGDcsL_0sn0jOVtWz2XYDCYz7laox2rI1W-Z2FweZBsvjbCiky4oinNF2AN_r9XnyAd9wxjRi_Mlaxr6ZRBnn-Efb1ysmoo4dw8NxsuG-1KlkYbgsLlCV5CGao4QXozCbIPX0M6fRCBGbd5tOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd2fb8a1ce.mp4?token=tmP68fDBHSdr2Z9LkWQQVax3FzueGTuFFoWVIQtgrj0dGVEONrVpzY7d0F26_3tQqgRmJAUXKsSMdM_yrLli1u8I130eIwtQGlNAM-K4IyJ-SLv0ZeH3G_Ris9niILNwQiV8TOVP1MjGCWFyxCmnBjbbAjgOLANsfvQALrR4Jq4snUeJurXTb_hWCHmoQe5noCsnuGDcsL_0sn0jOVtWz2XYDCYz7laox2rI1W-Z2FweZBsvjbCiky4oinNF2AN_r9XnyAd9wxjRi_Mlaxr6ZRBnn-Efb1ysmoo4dw8NxsuG-1KlkYbgsLlCV5CGao4QXozCbIPX0M6fRCBGbd5tOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تاحالا مهمون ناخونده براتون اومده؟
🔹
شما تو همچین موقعیتی چیکار میکردین؟!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668994" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668993">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96cd2cf2b2.mp4?token=QjAU2mJSoKu-PY8p-OzCzEChsQJ6DFNYHUb2IrrLPkYJno0b0ujyMmr8JKlXO5KAgluOgqBGsIdmIzeJmDHbu65QCICdk6Bog7EE-oPssqHzcghq7Xd-5LGfWZXV7kCVR8oEmAdXWIpESs4AaMJqCx0nScCSQ7YyRKYlUfMgbhjV1MYWB_dQ1HZ5uwxH7EwHvxkXufRwk17k1u-fb39XNHLdJB3liEg0RQyoJWHPfbN3qezz0-6s6xMu1zWS1tGHwBBWQSZmjBbkNBfsSHNFfCxYHDLxRWVXDONe_QMxy6rDkPabosFZsDtTyCLOfeNz3IEMrSeWAIBoKOkH4haoiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96cd2cf2b2.mp4?token=QjAU2mJSoKu-PY8p-OzCzEChsQJ6DFNYHUb2IrrLPkYJno0b0ujyMmr8JKlXO5KAgluOgqBGsIdmIzeJmDHbu65QCICdk6Bog7EE-oPssqHzcghq7Xd-5LGfWZXV7kCVR8oEmAdXWIpESs4AaMJqCx0nScCSQ7YyRKYlUfMgbhjV1MYWB_dQ1HZ5uwxH7EwHvxkXufRwk17k1u-fb39XNHLdJB3liEg0RQyoJWHPfbN3qezz0-6s6xMu1zWS1tGHwBBWQSZmjBbkNBfsSHNFfCxYHDLxRWVXDONe_QMxy6rDkPabosFZsDtTyCLOfeNz3IEMrSeWAIBoKOkH4haoiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از تو همه فرزند شهیدیم ای پدر امت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668993" target="_blank">📅 14:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668992">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
شنیده‌شدن صدای چند انفجار در چغادک بوشهر
🔹
دقایقی پیش مردم شهر چغادک استان بوشهر صدای چند انفجار شنیدند؛ هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است./ فارس  #اخبار_بوشهر در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668992" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668991">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
توقف موقت خدمات ۵ ایستگاه مترو در مشهد
شرکت بهره‌برداری قطارشهری مشهد:
🔹
به دلیل ازدحام جمعیت در مراسم تشییع، خدمات‌رسانی در ایستگاه‌های غدیر، پروین اعتصامی، هفده شهریور، بسیج و امام خمینی (ره) موقتاً متوقف شده است و پس از کاهش تراکم جمعیت، از سر گرفته خواهد شد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668991" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668990">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
از هر رنگ و هر ملت؛ همه به اشتیاق و انتظار برای سلام آخر آمده‌اند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/668990" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668989">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
رسانه‌های عربی: موشک‌های ایرانی به سمت پایگاه‌های آمریکایی شلیک شدند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668989" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668988">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2392049a.mp4?token=QdW5xoZaF0M85Zrae6sF55JK9GETQ1VmvMa_DFx23KJglf-Z0Q9kPByHLw6zMQo4WW186i7tOo0qtZFb6HRpaFiy5qnV--VtSc1sH5Ii7-gwqXZCsXjOVB4jGMW1A3k7k8ypJdIAq7gi9xUtZjxhdu__TjxlbDehbjNGi93q2c1ezbd3F3nU_1FuOor1PHt6k8P75Amcsh3zcoNGpHUwrNPQ9SNc9daeJ9hCegqjPRDGcKwUt2u7Sgb-a-V4je1kzg7_mh-z-_3ubY8BZUHR9y2XW4vor2mO-ucfnepMz8TCHqfc13BR0JcU5NjAXgwEjw72fUhANQKdePUqzWyIyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2392049a.mp4?token=QdW5xoZaF0M85Zrae6sF55JK9GETQ1VmvMa_DFx23KJglf-Z0Q9kPByHLw6zMQo4WW186i7tOo0qtZFb6HRpaFiy5qnV--VtSc1sH5Ii7-gwqXZCsXjOVB4jGMW1A3k7k8ypJdIAq7gi9xUtZjxhdu__TjxlbDehbjNGi93q2c1ezbd3F3nU_1FuOor1PHt6k8P75Amcsh3zcoNGpHUwrNPQ9SNc9daeJ9hCegqjPRDGcKwUt2u7Sgb-a-V4je1kzg7_mh-z-_3ubY8BZUHR9y2XW4vor2mO-ucfnepMz8TCHqfc13BR0JcU5NjAXgwEjw72fUhANQKdePUqzWyIyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آژیرهای خطر در چندین منطقه اردن به صدا درآمدند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668988" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668987">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرنگار الجزیره: آژیرهای خطر در چندین منطقه اردن به صدا درآمدند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668987" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668986">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
برخورد دو پرتابه به اسکله صیادی بنود؛ ۱۰ قایق در آتش سوخت
🔹
فرماندار عسلویه از برخورد دو پرتابه دشمن به اسکله صیادی بنود در صبح پنجشنبه خبر داد که منجر به آتش‌سوزی ۱۰ قایق صیادی شد.
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668986" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668985">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54296d85ef.mp4?token=W3foI461KahUND_HKJBZoRBMT93AqmI59wNb75UOLxYEl-7MREWK22Q45Y2RsNGclnJu4d3IQOyXyM8MpH0DK764zV7nuCVgPfkstEZqmPJTyPb6_iGXFRDc1Seo8BOV1Ld_piokqzkVtxxDHcDuV1PGZmexPpbCQF6XI1ljsF-ssFf3KsFVnUFdAkcDgpd_4VRSzxtc6wmVG9b_ZP965rk52KU7Bp6b1_Fx1NwBPKp7Vrji9Pfz5wDbM1N2EzrU4cGn_F845tWGfRexKMrhVyscshchNG3rX0BKqfY-t_vZo384K3DwtYye4wFUV5tmTUUMDjmnEGqN1tIzNv_ulA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54296d85ef.mp4?token=W3foI461KahUND_HKJBZoRBMT93AqmI59wNb75UOLxYEl-7MREWK22Q45Y2RsNGclnJu4d3IQOyXyM8MpH0DK764zV7nuCVgPfkstEZqmPJTyPb6_iGXFRDc1Seo8BOV1Ld_piokqzkVtxxDHcDuV1PGZmexPpbCQF6XI1ljsF-ssFf3KsFVnUFdAkcDgpd_4VRSzxtc6wmVG9b_ZP965rk52KU7Bp6b1_Fx1NwBPKp7Vrji9Pfz5wDbM1N2EzrU4cGn_F845tWGfRexKMrhVyscshchNG3rX0BKqfY-t_vZo384K3DwtYye4wFUV5tmTUUMDjmnEGqN1tIzNv_ulA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ارتش: به دنبال حملات بامداد آمریکا، ۸ نفر از دلاورمردان ارتش به شهادت رسیدند  روابط عمومی ارتش:
🔹
در پی حملات جنایتکارانه ارتش آمریکا به مناطقی از جنوب کشور (بندرعباس و بوشهر) در بامداد امروز، ۸ نفر از نیروهای هوایی و دریایی ارتش در حین دفاع از میهن به شهادت…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/668985" target="_blank">📅 13:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668984">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
قالیباف در پیام تشکر از مردم عراق: تشییع تاریخی رهبر شهید، اعلامیه خونخواهی این مجاهد بود
🔹
محمدباقر قالیباف از مردم عراق برای برگزاری تشییع حماسی و بی‌نظیر رهبر شهید تشکر کرد و آن را نمایانگر عزت اسلام و مسلمین دانست.
🔹
وی از مراجع عظام، روحانیون، عتبات مقدسه، عشایر، موکب‌داران، دولت، مجلس، نیروهای امنیتی و حشدالشعبی عراق برای خلق این مراسم ماندگار قدردانی کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668984" target="_blank">📅 13:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668980">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r7lsbfFom2uYlyTfcT_FmhUegMHB4g6ygZ88oY066r1UHRziRP6EkUAjl02jb-AqRj5ojG1wH6fsvuCtMGEqSaHZMpdGlUBAIDpj9_tFiE8z3yFMwDix5fpM9QAM4PO0uQteomYWnI8U8332a9mCoptdZX-QjqHSm7urCclTdRncOSELoAJqJ16k41-m9HmN61wXvm-vUbSgqiN5Wlm35NwVYCkVN6yiD_UWPquKlb5qaiTwd4NuAyU9KN8vSxf2l23p2WACXeVOwALBQLyUW7oldlEelc0HZ20LZ4k7Yj8fPjlKUuNqK93O7vjn_xwzOi_i2zDdm8lRtLiGXaS7FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ag6KVDew7oK4G5EjA5FFnSZMZiMIpIN0knVfzoapoJ8h0qqiXhQsb0diZSdQ-1KMTijw2ErHROsFBYTnao14FSMK9JKHXdKw4bOnU77LFMR1PWAFakk8hoyI0a2Yk_MX11zJXJkAelVOLlTVZvYz31W4vILv-coRGMMDjXNK8MwzpFXoJIVArIeB2qKC_yApNN1yh1doSTVltvoCYNh67jc3eK4shTMk1ji-A_Rl6B9zRT34CIWb3SE9X_tal6tKfTzOyWtzBn9TO3PTAUYgDUw9h2U4iVKnsNFQ-fT_jo5pmEQYr4Zsr0D67amD74p53urp0eY3PPr8tW95Q3tmCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60880bf273.mp4?token=mgNW88nId8zCLRUrTiFFNsbl2Y2e1vaOCQG-la2ZhiGIuja_ub3W3xJ16-8Nn2bdIHJGS7ZHaNQ0e1R3yosizQGsDWOGixBux-GHISB0dCPY_vm6XksohOT-JdrdQHorWuJ-lFUwCjtsg2uZ-JP3Xy_Slj9TmY_wYpS0ZXMaU8YAUYlDArrby1WAjKac8xD7VkT0SqGSJx-PYobkYpJA_p6vRDV2A1jeMD5zOM5dTgAR9CfNacwXBj7TtbVXL-UMU4QoGe2Fwj3eRFZCG46gRHDPV1YFkwNg2edMmC9Efr4CPXitnrCW58ga5OzxvuzT61s9THbUxg_zI-hK1RXC4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60880bf273.mp4?token=mgNW88nId8zCLRUrTiFFNsbl2Y2e1vaOCQG-la2ZhiGIuja_ub3W3xJ16-8Nn2bdIHJGS7ZHaNQ0e1R3yosizQGsDWOGixBux-GHISB0dCPY_vm6XksohOT-JdrdQHorWuJ-lFUwCjtsg2uZ-JP3Xy_Slj9TmY_wYpS0ZXMaU8YAUYlDArrby1WAjKac8xD7VkT0SqGSJx-PYobkYpJA_p6vRDV2A1jeMD5zOM5dTgAR9CfNacwXBj7TtbVXL-UMU4QoGe2Fwj3eRFZCG46gRHDPV1YFkwNg2edMmC9Efr4CPXitnrCW58ga5OzxvuzT61s9THbUxg_zI-hK1RXC4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌های مشهد آکنده از بیرق‌های خونخواهی شده‌اند
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668980" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668979">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بوشهر  بر اساس گزارش‌های اولیه منابع محلی، پیش از ظهر پنجشنبه صدای چند انفجار در محدوده استان بوشهر به گوش رسیده است./مهر  #اخبار_بوشهر در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668979" target="_blank">📅 13:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668978">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
پخش زنده مراسم وداع با ابرمرد شهید تاریخ را از اینجا ببینید
👇
https://www.aparat.com/MADAAR_TV/live</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/668978" target="_blank">📅 13:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668977">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxBXCnwqETJ9NA5HJV38QI-oV_KF8v3iy8hwZcsWEMN_5wtwZzrgxSygLQfoQY2Ac_3l60J4_AFG1MFLIxbuwAappcjmxLD5pJt4Vmzul-GoEDIeUOQMwgsHaWb0_L3u-G4W4-XL_ilkS8_A0MnWFg8PvWbEMY-3MhwdeVO2_4SwS0igLtv0V3U_ordo0a_4sa04QcsHx09Rmll-54xhPQMslMUnW8nHH-1n2azjIKcrlcbo9rIgeF9OIhMbDEt3lAgCQ6fl0efJ7ehCpi26ogxxemVAcIELP-ORfVoVakCenLoCNDqwcLxOqvin6MUHE0j-eI2wOfbJSvNlnfjBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ
تحت تعقیب
🔹
پوستر جالب در حاشیه مراسم تشییع پیکر رهبر شهید
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/668977" target="_blank">📅 13:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668976">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553644aec4.mp4?token=TMzDZPkTYTES2x8Rodo9E9TtuzvuZfPJ4OprnKPEIlcVThSup8d5dUyXXO1taI9G1y5f2RkTuQ-RrZ4lW2Flg-bH_9ILRTS94wv3nkAn2NJUz764sXr4rimughpvJjpkT6EjqH3k_keucWtegZyI3el0VW8nY8GAt-OuB2S-IT-UGfz3FmWllTNTsJQYRFKQVWeUii-OQ3tXWNf2wY8kXLVzYenjNsxfeERHVKPhsEdMdZa1WEdS2ugVkxR9o94d0iY1IPTEpesp2RuowZ4-ZoHLqxaEYNOZ823vxkpGTUTcA_CBCpNQQjM_PD8xCD4kTLFwTPQN6oZKXMmQmtXDJiEnU56up9_W0WRcK4cWCDRVAunaHL7sRLi05VuXihsIsjxSaCh589yC3QTpkitvA1JCFnD4JqCTJmqZsZYpewb7FqtVbXWoH7Cgf9G1mUMZJY4vBSWPSz9cMfsV9Eo4X05Re_ZFYsp6FAjfaUIvNwU8SfwOi-batY-eXLsWNCyywT8wTEYyIwEydB3xJ6TbNj9UPCebDjV3pG66fylc1Ab-_TWE5Ji3RGX5BpzC7bU1pG4zMlMeHc0LER-suzHSskct6rbp3pz7AG21e_DJSybtiUosz8sSdKrlYdv_L2yQU0PKv89wJAYitho1nCYWrRU2uYA3QxvIn3S2qb7yyc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553644aec4.mp4?token=TMzDZPkTYTES2x8Rodo9E9TtuzvuZfPJ4OprnKPEIlcVThSup8d5dUyXXO1taI9G1y5f2RkTuQ-RrZ4lW2Flg-bH_9ILRTS94wv3nkAn2NJUz764sXr4rimughpvJjpkT6EjqH3k_keucWtegZyI3el0VW8nY8GAt-OuB2S-IT-UGfz3FmWllTNTsJQYRFKQVWeUii-OQ3tXWNf2wY8kXLVzYenjNsxfeERHVKPhsEdMdZa1WEdS2ugVkxR9o94d0iY1IPTEpesp2RuowZ4-ZoHLqxaEYNOZ823vxkpGTUTcA_CBCpNQQjM_PD8xCD4kTLFwTPQN6oZKXMmQmtXDJiEnU56up9_W0WRcK4cWCDRVAunaHL7sRLi05VuXihsIsjxSaCh589yC3QTpkitvA1JCFnD4JqCTJmqZsZYpewb7FqtVbXWoH7Cgf9G1mUMZJY4vBSWPSz9cMfsV9Eo4X05Re_ZFYsp6FAjfaUIvNwU8SfwOi-batY-eXLsWNCyywT8wTEYyIwEydB3xJ6TbNj9UPCebDjV3pG66fylc1Ab-_TWE5Ji3RGX5BpzC7bU1pG4zMlMeHc0LER-suzHSskct6rbp3pz7AG21e_DJSybtiUosz8sSdKrlYdv_L2yQU0PKv89wJAYitho1nCYWrRU2uYA3QxvIn3S2qb7yyc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر جدیدی از جزیره اپستین توسط فاکس نیوز منتشر شد
#جاسوس_موساد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668976" target="_blank">📅 13:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668974">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NYuSODzsfEdNrMsl9irN2COnS9nEDzHLClj90lyiyAX3kD-4IehIrds5MjvVYh1uSAM7GOWt1Y0F23rWozBxrTbumDJrX_lmX1fqI0-n7wECJ3LeJOv0zhQ4jLaC8MRTHv4ARAGaVS3si6OYobIJJyd7S47T9TcVY4ji8a9RU9T8yNpE9kwkDQkBFewTpyeyIfvDI9YzERBgyzUqRIqu6iyMt3N1ZgA2sefTrDpBDEMJclB7f0qSlCUBsZynIK7PBqIqAJ48jvHpHwkhXK-mbBpbYL1cmoTUvzyB8R4WDxQlSaRWgZKesnLMQ4n-ZTod_JUp9RfqfDk4amnjdRECRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K-Z5kfNPlDnevQzP2Ebcn_mIicRES8tnwQqr4UFE43F84-bMfz7LD1IhyexLYOwrUB8G5gB1ayjHCIQPHh6tvtQQfvesJZCjGhd-oJk9KfStrVBWvtAt2uV-Y7DQiX_O0tDvs9l62MVNSvrZUUClI-r8zXvxR7GSp_OQvscwuR-uUEcumqvrzZ5aSK3TitZTFEvPpm8E9NW8RRggmvJGeM9tlD4aQIledZnFgSYgaXZPekpmxaxsYl4cZlvZqU6TwS0sv__E1twC8Z9l4KVeZyquiP-gQGCXuN7KGw2ZnbJiic4A0-jR4bU9BHA55XOfn2078Os86VQn9qky6XZt4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خاندوزی: ظاهراً تجاوزپذیری در ذهن مسئولین عادی شده است!
🔹
سید احسان خاندوزی، وزیر اقتصاد دولت سیزدهم، با انتشار تصویری از حمله آمریکا به آق‌قلا هشدار داد که تخریب ریلی و زمینی کریدورهای جایگزین، در تکمیل پروژه محاصره دریایی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668974" target="_blank">📅 13:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4859ce07.mp4?token=RdyoN1fcZqXb-TwM8iuFJOivMdWF_eW-pd5s2sztdue47_N-b8gTuZwNkWg8Y5H8jMPRIVhW6hTlL2xJSn1W1kMKaKDiZJKFfddSI_srRmRizV4Xy6VEtKwCg9AnJ72LLi73Dl9Xp-AzS-mUrtqQEwbMcGV1d2EmDvhdJkhwJ9CjRnyc6gI-1GETQO_Q_gYzElfzBtvTHoYxbklRVSBRhARovABCoKrYwVCBWS3JOe8I8AmQDIOKxsqZ9MP5a4z3hQDbW0GfZVlxfNY-ksS0SvFjOuFkqGvr9ivDBJTtC1LdCg8b3c3TX46KGGMHIiuMakFYdaIBc61LU30qTayxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4859ce07.mp4?token=RdyoN1fcZqXb-TwM8iuFJOivMdWF_eW-pd5s2sztdue47_N-b8gTuZwNkWg8Y5H8jMPRIVhW6hTlL2xJSn1W1kMKaKDiZJKFfddSI_srRmRizV4Xy6VEtKwCg9AnJ72LLi73Dl9Xp-AzS-mUrtqQEwbMcGV1d2EmDvhdJkhwJ9CjRnyc6gI-1GETQO_Q_gYzElfzBtvTHoYxbklRVSBRhARovABCoKrYwVCBWS3JOe8I8AmQDIOKxsqZ9MP5a4z3hQDbW0GfZVlxfNY-ksS0SvFjOuFkqGvr9ivDBJTtC1LdCg8b3c3TX46KGGMHIiuMakFYdaIBc61LU30qTayxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیابان‌ها در انتظار؛ خروش جمعیت برای بدرقه رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/668972" target="_blank">📅 13:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668971">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
مراسم تدفین پیکر مطهر رهبر شهید با حضور اعضای بیت رهبر انقلاب برگزار می شود
🔹
مراسم تشییع پیکر مطهر رهبر شهید پس از برگزاری نماز بر پیکر شهدا پایان می‌یابد و مراسم تدفین با حضور اعضای بیت رهبر انقلاب برگزار می شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/668971" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668964">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGU9ZAvHOW4jSj2zYqsezjYgVyOgc9r0_PawcBXDAFsqX_VkFjWYU6dT9N9gsskW9Yf8IlNr29hz6HcOQhdzTMJaOMBrvJVSb7pDCasX4R8MvrKmkkpSW5iLhk2tFvw5lJ4sVGAYCAszp-rdTDhzT5pEbhOskhVfwcxlJxKnYyVL3hbOVlmwc0np2Pzzm-rEMI7F2jmOM-ou_QrF925kq6oK3AnREcx9T59bD_sOcQ1C1TS7pAbL-_Miw0IIKMd-PaR4jf2VxPgURG2qfRq_kPRZRKQRi9d0BEEfsCDsEtpkWfMKS8lhTNM3ssQP9NBRC3tb3VkJzBUd55L5XuyyHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2lOBrOp2MG8x90nfpxwwm0mkNc4x4o-T4uVRsOjd1o5RnaVL-yM_ZYDP_Yw93cnUYO7QLg7OTUm5nWrLmWd7kR_53rKHGMjywLxRvEdGYsBHF3LlODPKtecF6ht0yfPQflMOpv8vQSu1tK7tHCpZ06urzdSKthtotyTT1XtQ1a6Zi5h0n15THIkJNT3BGw30U_lhMu9dGDRmUqeRPN42olWxRZB8cdUT_Rv2m8vDPNOgKSTJa2ykx_0H3O7xH7PPpJlWMDfhT0UefR5nxFQRo-KUpwpnhmYRRalfSTbC-x-aLLJfp9vudxQL8dJKZogTT0cHOJhcjhhvRJN3xd47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pNlLKAkajPMSEv-i4jTHR9nCDQPgs3GivfyXNZ0M60z5VleZaoTuU53-4qI3KCw78km0nPxIOzoBRhkp15ix0zrtg6L3SgHFYDyT-5Kj_koXxd1qO7sIJV0ZfHzxPBHuEjebV2whicRRHuJa8vwTsHCxGjUv-Y-kWRxoiqymGiHVHAun05Ctt6CSH-_4GYNFH7004sZeGdM9jqqxnmr9pUmGJwMlmVRdkOPNzrgIeq4_CghHSUuVeXBAVSRe8rqNMfl-OMzaFFauDirtG0PaLdQ5_G587P0zUnihkFGh3vCQR4qLqf20Do9YsWrual6Dmvx1AGUT2SnN6SjIDJlqvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ga9OK_7OWYcASMADEMTBrOtHo65xhqVuRlVyriyuIieKgMBFSikWC8x7ob3VYaCF8DI-z2rZf5xSLMPBTtg6Cz724X0m39A7D_RVvgrsozhSVML6KWZ4YL8_A71oOHBVVPfyxSpZ8j_O4BUrqcWotzYdmiipSKwW-jyZedlWSDLmK2sGOghRgKm-HNMoo8sSncNQQb5tiRzOkLJXeYxsAT7IA78gGyYRrgIuMdfSjZupo2SskptoHqQqB7_dF7oBeRXv9JHMdzvVwlG_rjM02B_6kNag7u2DpzV-TguI-iAaIO0m1BzLaY-vqIJd5E9h9WDLoVk7_nfCQQ_hnHwL3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaeQKVs07RrP5O1hMau-XZvJU-4r7EpLxZfYuwyi6EfO003H9Eu6sU9xSbRL-oqaBY1cT6vCUkzP3Vw6ppzANgaq559u1Ev-MOjzeVINWzXLtA_OI_cJTjpEZYm5wkLJVJnzT6ElxVAwwdzFZm1_QyR3QF6nov8m0g26eEGC_NEMpqx7oyzUOEN7xQRSyq7TIpJCikKuvmm_UYCBVAJwWKCcPIS0D2Fio8Hqw94oWUZlu_J198tl4WwAtUURGjJInVaRuDYaC_zURGQv0C5mPM2VvDguVxX4s9iarQjlTiMCFH3MJrGwHYK0XmszEHrbCQStwl6YfSdRNPYSYQdqWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cf72RLCLxGHhawacSt_fcP2q5FfcxoZ8GU3I7OMeL5fjYe5ooUBVTqxFdrEKsOd-gam3lJZ8xnwlvujB1ZxINABHajoKVIGsBcSBfawHeNFg2ImERgV-aTenJWTMbW_U2Ngx75OjJAQnjeW2D8u8muk9pt8uhXfDWrY3W3AS7x6hr0XLJhKcuZwcUbNU7VMYhqUKpBpEINIZUFImZvAcQo0pKXiwSs7YV5OeCstyWyCaUlOar0QVduI93kiUis_uKyAlj5eR65RdCmbcsVFY_CecZDY94qOMgzDVs-LkRQb4r2bo_hxKL0jOjR28c17558_X6DkPDl1hROF1u2VXsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sme9hhZWYJgxnqy-d8iPptHzp_oV6l03ViqVDQpGqr5vQAYpADVOIT_t_bEHMN70j3tj7FZxomlHZr75hoJvkBH2flNx9ZIh2HBvLXVAQ1afmEfqVlCL__uoOKfZ0kJuJPFCU8o4Glr-LCilgAvMIGLzYwiDhoOfUr2xBK402wfj5UU9ivb4hUBAXFe07aXT3V5mEZcXjST_KBCUh94pFUC0pP47WEurWZu-a8WXMwfyxLvxqT07JP0jU3tPsQ5Hx6-5ayUZTRSS4eTicyaEBqYi9LRz6O5gKgsxZouBv1MxFzCHjUZZEGDCuFODC3Ai_36uhyFinPhiI-Itk3rNLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
گزارش تصویری
#اخبارمشهد
از ورود پیکر مطهر رهبر شهید مسلمانان جهان به فرودگاه مشهد
عکاس: وحید بیات
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668964" target="_blank">📅 13:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668963">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CGDbwOuEGmnjtBQH5grMxbHCYlkA8vTZAtjrlvPR5xYftsb6QYEwL816G-MhYm5f2fTBD4wxa8K5PbjSRA8uOS6RuI-IxzW2T4cD7pini9XyLKP6tR9-QnydgMz9S6GecJnANIi3KaQqCmvA29e49rRHI_FJyqLfbhRmAhPzmc8iB8p2MdOXkC7ijyf5SH2YRdZWaCoOkj94Wh2gCm5EKdEw-O-Us-Rd2E18j8bbfJqG02LGX1LMkbDhJL0vtXs0HU0uvqIjL8cQzpsGE865sgMVOeGFrGdGKrKMcaFHu8GdXggWbZqfN1J-NBGJp9QhxlheOkbMK0mBfiOj2281bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پارچه نوشته مشهدی‌ها خطاب به ترامپ: trump we will kill you soon
به زودی تو را خواهیم کشت
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668963" target="_blank">📅 13:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668962">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SupiQI7PQF3A9jaFbuE_Rz1I023D8jTlGzRSzKqzeebZmTANNU6b-87cuMp4tg4ptTUOS75-g5PKWhPzkwUdygsG79ap4IYNn6i6pymogFj6lkFl_PEvRfc9QnnGDVtd7OaipGTFU4b-d-fM5k8KqIaqI-K7eS3qH0P8a1I9p2lSb0s_FiMozkQLV1tkBNoO83HX6Xr7YSTqAxXBiPSVLaoOQs-NUVeU7HouEA_8eqQ8hvjWs37wYCOpO4tG5qFwZKesb-daY52TxMY57LG-vEm_42I2fj1flE0wb2osrWg-LYr9KLBG81rWEIsciUj1JoFinElbpQeCdEuuYtKsdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بدرقه یار
🔹
اشک‌ها فقط برای فراق آقای شهید ایران
نیست؛ برای سال هایی است که نامش تکیه گاه امید بود و صدایش آرامش بخش دل‌های بی.قرار، مردم امروز پیکر رهبرشان را با بغضی در گلو بدرقه می‌کنند که تا لحظه خونخواهی در سینه ها حبس خواهد بود.
🔹
هشتصدوپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668962" target="_blank">📅 13:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668960">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U4yM9i1a0PSluikPZCOThruMC9i6a6MqobGpKQ49Dj9r2d3nqmbvu-4dVO1jtbNaxKnGa0TLEYppVPjrvpPHdKNeUhe-nrS_rdQaayX20UjSuuv7RXnCgPUoL8DyjJTcYWEsxOjc0AC6XXLOHNAROIndHHnbkG6jq3q1rpb-1bPUXSjyH6BWdhSQ6wm3Cl7F16Ph-F6zq69DXq_o1v93GS5N77eUHTyNt52f6sMEm2l8gwSWYNG239ZQFxAgeu1SqC2eoiJ4QzLkcg7ZancS3TrDJNiqQwFC1vm4-U7NOvKpK5fyOtHTnpnGTBc44KSoCga9Nqj_BMo-XFJndZqn3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F78n528NjnBMviwxhz6jyfI6rZLiX4A96XRE3rjFjci15NtcQAkJnF8pjxPHz84lkdFVpHwHKcwKMw6PD58vNsZ2vsjq9qYN1Jw4An6KJncAe9yShag6Xfr9oZX4itykb7rBIcoRkpf35O4s0hRLyAlaWIH9N74cuBgovgNjUEQftIuUuA_3Sd7x2MPRcK_uAWXyk-4VmSUdsAdqLawg4_nwj-T3oh1u0CNc0M3XIP8imKsoXbmm-eEIjVflIK-Ycvf77v9nlxv_sPTLb3UcWmYSMawlP7skVu6tmXIE1GxQllBk1CoChW59U4quu8Ck3qp5O7UXXd1uG5y763XdcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در فرودگاه مشهد و همزمان با ورود پیکر مطهر امام شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668960" target="_blank">📅 13:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668959">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
شنیده شدن صدای چند انفجار در بوشهر
بر اساس گزارش‌های اولیه منابع محلی، پیش از ظهر پنجشنبه صدای چند انفجار در محدوده استان بوشهر به گوش رسیده است./مهر
#اخبار_بوشهر
در فضای مجازی
👇
@Akhbarboushehr</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668959" target="_blank">📅 12:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668958">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔸
بر اساس آخرین اطلاعات دریافتی خبرنگار #اخبارمشهد اقامه نماز بر پیکر مطهر رهبر شهید مسلمانان جهان و خانواده شهید ایشان در انتهای مراسم تشییع و در صحن پیامبر اعظم (ص) (صحن جامع رضوی) حرم مطهر امام رضا (ع) برگزار می‌گردد @Akhbarmashhad</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668958" target="_blank">📅 12:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668957">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExKsS0Ry9q23MXdjIBsuQVHhwf89-A8Ll5SRMsBhA5ms7c4ck_iDh_92-L6FLsHABkblAYfDoHR0uPfKnFjRRH1VWa1SVTHsrh8T527NuTxo8RhRb5jX0nJBbHroLGwr-Zp9FY8Wh2lfdNfn_bX8Y1F-Y4L1GatgGWUPuXRmwKPp321sF9nvHeHiNm2t2bRJqStLDzVxxq2cwDv77HruLeUSpDYW0Akp-JdnYz6ub9zBXjJ1gXCR9YVeCCltrd1HuO9tRcOCMIgDMC5CSmBhfsKVSn_YBJJXBBcLZv21_d-zEh9nJZDby4kOdX-XDw0jTg2TGeDQSVn8Gln25PcJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اطلاع‌نگاشت/ موقعیت استقرار و مکان توقف اتوبوس‌های برون‌شهری در شهر مشهد به تفکیک ورودی و استان‌ها؛ همزمان با آئین تشییع و خاکسپاری رهبر شهید انقلاب
‌
‌
#چشم_به_راهیم
#باید_برخاست
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668957" target="_blank">📅 12:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668951">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4Hc6chBrPfeMvXORCrhtSXk4JyQmcbMBwXXqw3rT7PxAlQPK14hB86clM2Lgn8-RMNHy9dd27ak4TXxgdb8h6MB8d0cG6wk2ctUYFTBJeQROkrI6rVLUGHJnqP3ftri6UylInSIGKDO3H3K2cmBj39OU9nmelQsm-qrQ6IiQqL-18EsvpXNhqxQR3mnH5aYKY9Ce49JJHu4KNgiZ8YVng7vIf6T0KG0leLssIFfrlqZcumgqnv7yOBr2blYiWQtcUgY7PB14dAS11r1DHh4owLtQgwGYAgr5nh475OMtVz_tr8YD6C1Oz3Iq3FYRUs5fVgaP6yK7jIobdZlY9ncGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LKUBcE5ZJATGNgw51v3DlgDsC5x8Rx_7PiwgpM8iXY7pBt8mOK8s7Vxl6Bg3_X8v2PPgZW-v6Tbcq6CMF2QPhTPtFkKEkCyMSrY7pe0HbFvTe8IrZ4r_bs-LrirUeNLMkSS3agza_gBcumeH2_tqeQfmsScCpnNTqiGWTQkj6Eu-ufOPeSRlkVykSflLnytWoOCIZPYsARENeDwupK59m1yTnJBuAiW_iFtDgGBW4HWI1_Viw7BCql2HcwX7gtWpSy88RpaIwYTPLdacJ1b-foqLVhRKEp0cCkGOpIi3avIKPN6hIzDdE5580SW1wg5I-K-U7F5IEKH_MewNH8smVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zc2-eQw6jmt1a0DVmjSewMX5ldhk09gbcEgPxwV2E2ipIkZSlhxEQ7tFx477sr6NvmNzu8hOiDWqC_CUrhqq5uQPVJIzo8I5Y2w9ab3ZOxwIV9G4oNLOOflom1DDS-PpF1cfceBeQlmXoVOm4M8ZJ5Dmn7oLSYuK_Bo1fN68cfMAyUki860DiWEuH3b3j3Gr855aJE-IUFn7V1xQKc0vTXnWg5dncs6_tQz7p4p6wn_CQlUEUXZDO299uqxMgkfJxbLhMNPs8nM-9RUeSjblHKavKKHFu_xv77jrA5-x_thRi8zOv5gHGr1A43DoQUHZ-KzkYBJAWbHxy8hfqLaF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICiA4P67kI38sZlJ8c9U9vw1qyWVrXei5vskGfXmBP7mouGGzsq9P0KvJhc5bBVrKOoxqGOjSSaVZBqEUC-hX6fr9McHfyqCVCDDMU5-GTewNHYRHlUyEcIqyL_87R7lSz5S3cVT21Bi8y62xubH6Ayjm5mP6C8Yc2GuiSlBR1CEVK825pKbltNWIlQ0AiNxOBwE_hIlhuBVkDW1BU966ZJD3Jy-El9GKFqlncoeKcVDj8ip2vWlEn_ld7LRP-6JccTMLSxDp2_Ari_fLkkS0CCOWkrVdNQG3V-Tdi-RCEznVMGPvbiYagkXGJv1KH_KdkCIsCghM3FHCvEAYVmlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F4bNIkV_ePhcMaNKDSRPlBdMBGXdH-KWs-aHun7O_dJBh2XGOZNdk9pFg8bgmvV3YRd0Ax6ydlHaoGCLbfUCoIMmez6dQQLpkajyVOYtDLenzW5s9Tp83FS0x2awFT_H0xL1yfITNpexj4V91TM7yn21bxik0NrPnjbuC4f-JO-gl61cIjT_NTAimsoLoo39h5W3bFdgiBHVoLuZksY-ML9IldSMk2evMAsgyYc7MNyRNTWr8H_T8k1telPPjRjd7iOqZ1Z0G6eSW4Z3V6z9lWg-fYf-kiNEE49NLMjV81OUYVCUuchJtxrQWwcNZ296wDeFZjUx_yRlbUbmL7xGTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YAmqSshXTIFW9f5ZlQw3EgIBLIk0hBFm6hDIbEWBG3PXQ7uoyANM1cpDk9CfgpNM5IO5gN9NdWbHf0eIuEntvCbL6kYyMMQ-zWoBnxAZY8_eFkJk_v7eYHrgNC0NIHxd7s78JEblJU9XjqTB2fFovDt4lXjoxnD-j2ucevHi6OHv1l5YR_81wFsk0sWALjyQVNKvjo6g6hWUAx2FEhtRGgCAZsKhlyk_ZdEbilY-xxP8x-PpWTKKm3YT4gp6ntmZkrpCn9-ZTTQtj_IEgZ0b7HtXwrgqBNC2MSsfyzWg9Z099QQvPWs5EG6lZuEUaCfa0XdRwToX-78kQptr8-COnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری زیبا از حضور عاشقانه مردم در انتظار رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668951" target="_blank">📅 12:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668944">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKQwgprPVSyd6TY7NV-bppEaHLvb_1e9wERW3iE4x2jmHZ33WNcqZdYjwAg8u8dU7gyt8OdH29YSAgzLuIRCbhC2EV_RoPBbl0o54zVu_yqIqsF61bzqhYarfrobxfTNMzgpGnWogkNwPuwh2EkGgfghU6BzYcfslPWFhMJOKhJ9hk9RquxdXEb-3jewvUOwZmxSfo1vp10VWeyfoyCVo1Ymdo0m2cxVtNZkZ9ralk_nrYV4swTA1RKMN_0HFe66IehEd2UoeUYuT18LkiRjYoyh6mrwJVOPutyd0myi-sgtLq6XlnP661Vywtw_xA0BhLFC_HW73ozr2FxzvkpYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LfTaYj5WvlDI8Pd0TVmfubbangFyJtLNPAA36DIPsF8r7UR1OdlZ6uXFLpqlZCWi2gDZ2SrW8zAAo7ZQaa0v9CtKk3QHxo4JjqWG87XAiUnGxY1NshSZzhL1esqKGDmz4zXngm1pkdAtVzCivc3rD7wpDCC_QX_4UuMPn-2ayHnEfX2Qt8QaN9N5jAP_0v73GTTwKFha6HlWUpw85BaUNU5eYdTKwu9Q50ZE40DKDGX4ZlhGfXDw4JfnGtCKx2ps-JpNuKIIOFV4h3OKbysdhV81N910zw-4UiDsgjtCD04GISCgl12D8GVnd49H91mU6Vl8QM6eoJeTpgMg-Dr37w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c6apR1SkXiKlOr7_lgfBciZUMKoD2CiqKvxiXTtToIhpoolZPEaxUp7uDFX8OPqzUgesYgwnq3Lxjh4_2Q9ayGaVn1aEKfpAtBuXn8iM6VmVeS277eYF910PE0z2HxEA6i8Jq7NzjIJd3W8gWwIngsNiZf6LSZxSg4KKrF0QhAM8ZOunbC6Pt3_7EwwyR09353kc9Jvk3j-AjKNnVp3SBkcUXtK0LmWfQtOOv82KkdJXfdRxt95WOvI12apkAoeLnhznYlSwj3logT7NxbThGDwtw62dUwVyRLmZhiIPe2pcvVDj29J4tfyf9iA_L73ecWo8NYDtud7hSUflgILpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRTd_XrVTssZDkCQ2Jr8IzQWDZfTPCV0YC94KGGuduK60XpylGCohNtT4tURiwDwtBD9eCgsdnuT3erxUxWH9_lsWLeat_m0X5m3b1aUk4DcykM36_kRxVyTTpuMpIeZCwmBB-uvpkwKFKaC1LJulZacunDXmuk3X6hRihVnhasu-voprBQchuzf1A8bQrozdwystKufhGfTOXWQabLMOcHEHMgYxOkK7ykoZHQpQAXVLmWCYEInyTTxowr_um20giaRmgrlmjyvrANryBp9BstZhdZcy09YP9WiDfNiYHgreyS1yWYE4mm9YG6iJ0mszcYpTIQnoJyMyFnWWLTkgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GLeHUquqIkF1nleu3Xph3kgUKMER89Zy0pbp_yen2sACrQNgJ0OAzuD2i1uPRuaJ81rGjv2Lz8rLznXXeUmYjiuzIghFe0Wh3yCJZ5YEWLAk9zUVDr9ySAd_BLne19_JKtNxp7JKYCy2N6AmHwLE-oc3bNk3JX1bUdaWUNF4CnjxCvmw_23OXExkEVI5NLgs5l63b-OAjY6hatlUaUDBnDdLRPQHWGYcqYUb2cA7P4XPtvBMsNBevpq1Fnkqgx1ZDqj_lK4gbvvHOgsqo5HcPqV7untCnbxfsi98zm6NXbIZOuW7YWk3sBA7InjFBbU6OxQGsqrwCVh5dP9peTvU_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTc9YjnEMvmH2ncNeN0aJboDysf7eLyN_TDmW1VDlmniH9uGBGPZrk6RuSr3d3LnuAuO_0rUcgZ6Ln4WL8VvGxcy_xJ3lFxHAf5xtZZrTmpneuEsFK_rrxwzGY5Xy6T6jqtnyvbXifx0DpUOccOLSJih8qW_sxXvFRvgZQ9BOllRBfLM4hpbYSBqfot1An0sYcrrG14Ft_vKYUSRiJS6Ewc39mx6LF5PqPAsixTM6FlMTXiaHGXIBXOpol3BGwzIVe8E2Y5TDyBR23kxm5v-pdzEfHKZM4nDXNia6YOco7IOVH4ZqLo8eCwDQeBVtN6CPX4sn1Ank7LezMnDBMuUrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🥀
تصاویری از حضور رهبر شهید انقلاب در حرم مطهر امام رضا علیه السلام
▫️
«درس امام رضا علیه‌السلام به همه‌ی ما این است که ای مسلمان! از مبارزه خسته نشو. نخواب چون دشمن همیشه بیدار است و در شکلهای مختلف و در لباسها و نقابهای گوناگون و با آرایشهای رنگارنگ ظاهر میشود؛ چشم تیزی داشته باشید، دشمن را بشناسید و راه مبارزه‌ی با دشمن را بلد بشوید و مثل علی بن موسی الرضا از اول تا آخر مبارزه را ادامه بدهید.»
امام شهید آیت الله خامنه‌ای ۶۳/۹/۳
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668944" target="_blank">📅 12:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668943">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c36d5aa654.mp4?token=vzbYiferiC2hkq5-YGlaOZFoXLkJ9C4E8xOZkyLgjI4sl4gt2hFX13XWHnT-ERJID3ytB1cTwXWwlOIN1qpVWdEPfXEYLni6QJkuIxLPwtqtO9ZWviiZAZmL10_87cNdra7fgxE8A8u0dL41mRY7g4-fLbSJA0G6Ecf5xck_Kw08psut5-0G726FeBcJyndkjft3tftj4xZXoCR_XHZbipDKNugQgbPvtSjTrt-Zs15Lc0c_-CIQWb316eFNWgfn9N47jxmuq8Oufd5B6EiTHOnSqFSoC6vg4Y_Ar83vy_Co-_RBc_pLZ_mWeJWbWrriuxWD7wYlhpw1G5LNRNEEQZS5dvdEQDAAUn5n40jsaC-KLU-oN5myZzqDzmsHkHyBE2Fkjj7NzNPiiiLcP8UqSMKtslTFNZ4tu300RlmBZXvWwughw0xX-Wa7PcBmuJDzCdemZveTGHkuGPiDxlIKNxYOyPdPha1afl3U0bm79FisJMcG5RjU0JBAD4xOFUyvVrpNONfqQRyRxORutrmRG18hAmdg8sFHDf9CqmMTH8tBlPQkO-B2qlE7pP9gkgRcjbUMLf_m1YI6KIjl19ZswFAMz1NSLI_ViPzKYuMhqvnCjUbz2JClLfJ1V5pf5-OTs_TG9s7TjjC1I3jaf2DtIa3weBKLUCIGaMXlUNOoeS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c36d5aa654.mp4?token=vzbYiferiC2hkq5-YGlaOZFoXLkJ9C4E8xOZkyLgjI4sl4gt2hFX13XWHnT-ERJID3ytB1cTwXWwlOIN1qpVWdEPfXEYLni6QJkuIxLPwtqtO9ZWviiZAZmL10_87cNdra7fgxE8A8u0dL41mRY7g4-fLbSJA0G6Ecf5xck_Kw08psut5-0G726FeBcJyndkjft3tftj4xZXoCR_XHZbipDKNugQgbPvtSjTrt-Zs15Lc0c_-CIQWb316eFNWgfn9N47jxmuq8Oufd5B6EiTHOnSqFSoC6vg4Y_Ar83vy_Co-_RBc_pLZ_mWeJWbWrriuxWD7wYlhpw1G5LNRNEEQZS5dvdEQDAAUn5n40jsaC-KLU-oN5myZzqDzmsHkHyBE2Fkjj7NzNPiiiLcP8UqSMKtslTFNZ4tu300RlmBZXvWwughw0xX-Wa7PcBmuJDzCdemZveTGHkuGPiDxlIKNxYOyPdPha1afl3U0bm79FisJMcG5RjU0JBAD4xOFUyvVrpNONfqQRyRxORutrmRG18hAmdg8sFHDf9CqmMTH8tBlPQkO-B2qlE7pP9gkgRcjbUMLf_m1YI6KIjl19ZswFAMz1NSLI_ViPzKYuMhqvnCjUbz2JClLfJ1V5pf5-OTs_TG9s7TjjC1I3jaf2DtIa3weBKLUCIGaMXlUNOoeS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پنجرۀ‌ متفاوتی به لحظات اولیۀ استقبال مردم عزادار حاضر در فرودگاه مشهد از پیکر رهبر شهید
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668943" target="_blank">📅 12:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668942">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌
♦️
آمریکا پل کریدوری ایران با چین و روسیه را زد
🔹
بامداد امروز آمریکا با موشک کروز، پل استراتژیک ریلی «آق‌تکه‌خان» در استان گلستان را هدف قرار داد.
🔹
این مسیر که محل ترانزیت کالاهای روسیه و قطارهای چین بود، پیش‌تر نیز هدف حملات مشابه بوده و به‌سرعت توسط ایران بازسازی شده بود.
#اخبار_گلستان
در فضای مجازی
👇
@akhbaregolestan</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668942" target="_blank">📅 12:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668941">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4284eec353.mp4?token=TpVjaohuMcPkW0Q0B61uVFp_xhtnBPUrgX8clBUGSHaXU3h3d6RsIGgvuRHDVCy_qEW0uqYUrHCzFNug8VHflj_sUy_WvkNFzM_7_1jjGDsAHGITYCRuo7LCGAvraVr12czro_FDm7PhyKDiq97Y-2bElOqcHBJvGBsLzQIV6hUXlluK-c7pqklQiPGPK3lfPAT9jN7wuenkJIwjjs7heXBHWkKOjmFqBijiZE2_vgL2xGokbyfRj49Vzt7PTS-xWUMFvYQBkVRmWvzXFOAOAQnUAR36_3v0oQj1cJ9WYFXR0Og_-rXvZ5cDEmC8LoomNEIuZdc7FgWN_-gbb77Q3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4284eec353.mp4?token=TpVjaohuMcPkW0Q0B61uVFp_xhtnBPUrgX8clBUGSHaXU3h3d6RsIGgvuRHDVCy_qEW0uqYUrHCzFNug8VHflj_sUy_WvkNFzM_7_1jjGDsAHGITYCRuo7LCGAvraVr12czro_FDm7PhyKDiq97Y-2bElOqcHBJvGBsLzQIV6hUXlluK-c7pqklQiPGPK3lfPAT9jN7wuenkJIwjjs7heXBHWkKOjmFqBijiZE2_vgL2xGokbyfRj49Vzt7PTS-xWUMFvYQBkVRmWvzXFOAOAQnUAR36_3v0oQj1cJ9WYFXR0Og_-rXvZ5cDEmC8LoomNEIuZdc7FgWN_-gbb77Q3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان بیت‌المقدس مشهد و خیابان‌های اطراف مملو از جمعیت منتظر
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668941" target="_blank">📅 12:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOhWKg_2jyuIXc81ioVKqsjpby8b36mRY0pVSsiwgmJ7bt9s2S7aCYtONuP681P2BvyLKH_cDn4zvEpXr84YaMPdPCG0KMp1w6iLLuzrzwJYQ3XZUqExPpBwBh2ge5ap1aFdqxtVj_n_msy2HiuPnvbEE0HXvjUv6nz6DwpfHRj-9jc8ggykV_3smQBLSJ5VuNmyWGO5PkHscLIlTYM1FRScIYjyLzBr6QtxxsDT-pZ7kz7sxT1vdL3DcyHpEy6jH6sDSX4NV5885-zNryf47UvEEEJuDiJWi_nSzA00nE5q7pb98V_-sFiCLLjmhiOJSCSU7dpNO7V7jdrG5sJK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛
«بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافیست از مراسم تشییع در شهرهای تهران، مشهد و قم عکس و فیلم تهیه کرده و برای ما ارسال کنید.
▪️
سوژه‌های پیشنهادی:
پرچم ایران
ثبت لحظات مراسم توسط مردم با تلفن همراه
حضور و شکوه جمعیت
فضای مراسم و جلوه‌های معنوی و حماسی تشییع
▪️
آثار خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668940" target="_blank">📅 12:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668938">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار مشهد</strong></div>
<div class="tg-text">🔸
بر اساس آخرین اطلاعات دریافتی خبرنگار
#اخبارمشهد
اقامه نماز بر پیکر مطهر رهبر شهید مسلمانان جهان و خانواده شهید ایشان در انتهای مراسم تشییع و در صحن پیامبر اعظم (ص) (صحن جامع رضوی) حرم مطهر امام رضا (ع) برگزار می‌گردد
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668938" target="_blank">📅 12:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668933">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QdwXWI5YJP7AdgmuIspun_VZg47qi-c0J0A3buuIG8rk8yEtralYTlqcRYcpUMV8RgMLq3DhN1n1SveAkiZGcmSCEG72jAfyajtoo8aBlmMvfIIrIObknFT2jRVei48Gpv4I9SImKxGKoZYLpLEexnbe2KTlp1NqtAVaYwR5U2t-szhkCzE1t9QSvHoBuqCn4BUBNMQB1iGJgDVZiTRGauUZZVjUb8VamIMy_edlEjyaElXuwNhsv8j0drB65yhOt8dU3iRI_4Qoegt2LJttNU7FDB9Xw8ptKYaZrTIuIpIindi0Nbo7TcQGHIKPLD8bSHsvyWX2OA6VcP9868m5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxBFjKZcy4TO8SNGZokLp38sIDq2AkmO4XcpdttVU1Q4-V6KpOIo17EwiQE2-IFt23jfSSgnP96v6e_Qf0Jy3xZoplBLsNH9VqIYVw5583kALYGG9S_FWZ0Xo2q6ZGlvYGocSo7FwH-B14ELcqhgKYRgAE8EbtHGs6ViIbhm9COYwFX3Ahz_UOtRX-jpg0n6c0XW6STBrg0ic5Ly8Q1B1rhhXo-Q9nOQ4-aeBEXEs1WmRNBNnE2qHBkcI7AK2cGYVADI_R_NjcHqemmAktwLonAKWjWvC6913n3Sg0C4E5as6O1e5bzLs11czQPKVOcrd-1cL89KKEQzI1FCq6IPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8tp-kBvNftxNWDtB0gH6ZaXolYTCf4HptWKYaauMiT1yBBUv464m53DuOqJMEsZQw-OvcxEaXGKJY4XevuOK49aPS-Acq7JWcubBL4H4HY9YWoT5Bk4Bse6YLEeCi8PR1dPcmvJ99p2GBBSCvH_twjQFGcKh1Fkblw5tJI1rxK7OOEc-Ey9fhZuOTNFOmdtxhNvwr8IB4NZgfDkLkPAbBCAmw7TRL2MjaUQpVuSHjK4p1do8BgXpMlojM55Ffn6_7jjNMIRIGlk5dOfGIf1ZbLri-Wm8GRLpdw5OnHKljR3Fpx0BCqattnUaHUrS_oDVfHA4brruhfRvhL13GGAGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a44de5359.mp4?token=NWuTvlbIqAJalAmjqlQzEmCjNoUJNWpLC6yGWJ7KZ19uUcV9Fx3K6YNFbvlvxn61z1QWEW0PeIV39301tiXC3JXVFldqQbzjykm-QIdrm6_tH-M6KBPkFaG-z6obe0SiG_I7uET4q-O_NMyVSxkj6VTxhvpHKbjIxoQvciqP_OdX-08wZVXmUQxKbBM5DS8m2cOuNfskPQQLFm6YCTADnb4yGREL1rHhLFlLciwpDC4-MPC02GUIzlX31LaSZm7WPDfBVXvAU-IyPvcHXyAgZ4ei7mh7087FzNoEbjMFPAGSF5rSxdYFp-Hnj0JcdrQYYn1s2KMPSwh5zDEXIreDPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a44de5359.mp4?token=NWuTvlbIqAJalAmjqlQzEmCjNoUJNWpLC6yGWJ7KZ19uUcV9Fx3K6YNFbvlvxn61z1QWEW0PeIV39301tiXC3JXVFldqQbzjykm-QIdrm6_tH-M6KBPkFaG-z6obe0SiG_I7uET4q-O_NMyVSxkj6VTxhvpHKbjIxoQvciqP_OdX-08wZVXmUQxKbBM5DS8m2cOuNfskPQQLFm6YCTADnb4yGREL1rHhLFlLciwpDC4-MPC02GUIzlX31LaSZm7WPDfBVXvAU-IyPvcHXyAgZ4ei7mh7087FzNoEbjMFPAGSF5rSxdYFp-Hnj0JcdrQYYn1s2KMPSwh5zDEXIreDPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بنرهای حاضران در مراسم تشییع با محوریت خونخواهی رهبر شهید
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668933" target="_blank">📅 12:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668929">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnvx65oImwj5exnaqpD0jWpGXHMNVPN8CUQMpHww9zXC2me1mv7Y9EkoT3LD2yOCPJjpNVI6OYIVu_K6c9zReptkf6Pe_H06DYZgPmB1_sTaVZS2sgvjwumo7DOFbivjL3ohYbrWP75Ng5c9uZBhrd6ABryPsRk0kvg2XdvFek502y-00DMphAhYMsmsvuMf9TMWHXWLY5fHOL--zth-TV0-ttu6AUCUz6BWXuoheFJv5wcc4bSHn5Cni73ku5SGIpbTgt6QPC_FCjH63aZNYqV9RO-phy6WPEbezB-ndmZcKIWfo7_CriBh6gxdjgdDQ2dRyw9dpraoa7lokV1Bfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj6x8yF4zhKV9VqcqWigc2m-epnqsQUD70pGkFx-9rL16Pq6Ax9gIzXqtju0DRjKRqfiiT8BV_hlAY01kBRANcbFbdBoGO_SGqossr1B3SLxRdOsMhcifI764PURi0VfOlgrzaXFB9cBvuhwjHs-62Htpl62jRezxBULylO9TajixNdbG6uVUcmy1gMECbh85CTAlJy6J0hZFt_-tkKHeJHT_pra4Iu_zC_KDfvAP3odMEUQQrPs0dRqNOID1IvSe-FvFCQXDcKe7p_nfA2BfO-Ghxyb3AS4a425rBzNcfmPwoS_MC_qrzp_0GMu8QRle7R3xwLtrg-OCQGmQmyKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RbA675ec01C6m2v2WywSVpKvZn7hYyWJtbL1dVNgEjdZ6uLqo5BDo2tPpnK65YqTgNCYExvjshqNteQXMYP-6S0GKe4KxZ0994mE4rmmeRJvxObfmt6aCrAjhoZjO_bGiEzOBNPq347lWoL-PHYqrIvfMutaAaLZ2PwQAqBQ0HwJTQoAaQx2P06cCghKnhaOV8Im1UzPCORkICdVogS7gkOjS5wpM_LKALRwK_4Lwnea1_Ty-9czF-0taoF_qGObFl5-0fizYZfY_1oC0W6p9mQ0U5dypTyzJxJtopnOKcUjKg4vjf4SBBns5PCf9QGNtdvrvNiX5QxGGKxCGmwQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LINor7LmcFap6AGeSedNqz6csC4kTIp1L4_lxwZ-SWFuk6iraqR9LwJQhgFpfEZmzPuDgn6RoIhANmbmED2OiZUOn8iN9QyBy0v_yijfJl7kMFs38kr6Afj63YAOfAXVMeuS1m5QEHJIvNh9rKCh03mO5CEusqQPeaXGdvQvjfFEcm7U8cEQPXuH0BCPTM_JUx35nvBDMY4MBgSTBnwhN7mTp8D8iwSM3GOBcudwjct-sgjxp2gGMK_kmNfs7aJTx1n8G7HpJC17rCrMAWjbnoEodj3FH1UwnYiD6V8Un400e2ttykoOf5O9TvXUKHH9jPR_2x30oSfZdO3_we85Zw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تماشای جام جهانی بر فراز آوار؛ تصاویر تلخ و شیرین از غزه
🔹
شب گذشته تصاویری از جوانان فلسطینی در غزه منتشر شد که نشان می‌دهد در میان خرابه‌ها، مسابقه فوتبال مصر و آرژانتین را روی یک نمایشگر کوچک تماشا می‌کنند. این عکس‌ها در کمتر از ۲۴ ساعت بیش از ۴۵ هزار واکنش مثبت گرفت.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668929" target="_blank">📅 12:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668928">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a547a39aa3.mp4?token=JTljLKvEHEF_Xf8KVncNwWIqguGEstB6a2smIXSrXyKZPGSoM9vTYg6U2N7ReD7fT1rg1Rtd9WwNcHxVoZRyVQJ77xfMgi8wumCIujSX8QHc-53BtrYhBNd4KjsocWI0nwKx8JF6-xSL66dUXlUPYQHhCcItlXJ5sY5wgwECBDCZziJr900WnwoixWYtRslc1JgS1kbL_NzmkYk89sJkyqp-J0ujgx1UsKenJexdinHeHCahjHS6VE5utXA3SkeN7fmFwte0Iv-W2zgUz-PQSHNMBl738Nw3Q2--3-XGbWVjhtnrgVPoicIHZDqNULGgh0CIxGrdoEA0XP3ojYTvIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a547a39aa3.mp4?token=JTljLKvEHEF_Xf8KVncNwWIqguGEstB6a2smIXSrXyKZPGSoM9vTYg6U2N7ReD7fT1rg1Rtd9WwNcHxVoZRyVQJ77xfMgi8wumCIujSX8QHc-53BtrYhBNd4KjsocWI0nwKx8JF6-xSL66dUXlUPYQHhCcItlXJ5sY5wgwECBDCZziJr900WnwoixWYtRslc1JgS1kbL_NzmkYk89sJkyqp-J0ujgx1UsKenJexdinHeHCahjHS6VE5utXA3SkeN7fmFwte0Iv-W2zgUz-PQSHNMBl738Nw3Q2--3-XGbWVjhtnrgVPoicIHZDqNULGgh0CIxGrdoEA0XP3ojYTvIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر پاکستانی: آقا فقط برای ایران نبود بلکه جهانی بود
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668928" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668922">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/031e2575f2.mp4?token=b3eP-4RqlsynqAeCvatSocDEIrVzGWvoYdE4uL1af7yrYh1Z4miGuJ414MCwRwmToJQuZZeoDrMoWde6B9ffv3cGTd-09esdplaoh09MH4-O7j3OIgd2OXFZ_UT8tVQQoX_pjWgioPkRM6bcEFq-NxDiuG2I01aqctjJTOFb__CKfprgU0ttauOz7Ok1p60Dz-iGBDCi6vz5ZH1B_hBgDw7l1v0q_xdYrfKqPA6dbkzNMmVrkVixAT8z5chNI1OtO8SInl7rJpVvIL7uMtgixZHRhZ-Uk8ZtFx6LiJMRkTQDKv6TaSCmlPgWwH5Zsv5x_r0A86OM1b4XOT7GWNZdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/031e2575f2.mp4?token=b3eP-4RqlsynqAeCvatSocDEIrVzGWvoYdE4uL1af7yrYh1Z4miGuJ414MCwRwmToJQuZZeoDrMoWde6B9ffv3cGTd-09esdplaoh09MH4-O7j3OIgd2OXFZ_UT8tVQQoX_pjWgioPkRM6bcEFq-NxDiuG2I01aqctjJTOFb__CKfprgU0ttauOz7Ok1p60Dz-iGBDCi6vz5ZH1B_hBgDw7l1v0q_xdYrfKqPA6dbkzNMmVrkVixAT8z5chNI1OtO8SInl7rJpVvIL7uMtgixZHRhZ-Uk8ZtFx6LiJMRkTQDKv6TaSCmlPgWwH5Zsv5x_r0A86OM1b4XOT7GWNZdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کوچه‌های پر اشک و اندوه شهر در انتظار وداع با رهبر شهید آزادگان جهان
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668922" target="_blank">📅 12:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668921">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udd8hVfemCKUDdeb8ICEZMV96ep2ci4ezqDzu1OCWxhpjkuZ3529nHEaVN8jLfH4TBHvV_bE9H8n85Vq0wzkcxpJang1Ogb9j2tdIIebN86kUsV55s4U1FwbKSudk2GDwc2_RcxcZPv4qPiImjQeoSVTaWMRhK0wS8v8XBEE9Oc94bGOnovapiIgFf7bONOR_9ZNFjQyhoA27erwqjMZty0HI4HA_7VreIrt0n9NXcm8H5iuxZg4DNgXgH11-wIgPRXGne0e96PSyUM7-ESiccNm9wQ51Mm5TR5qMpv4eRXJGAAYH6PxkNGJcf_O7CyzMBL9svUSfrry3JdubXUXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شنیده شدن صدای انفجار در شهر آق قلا استان گلستان
🔹
دشمن تروریست آمریکایی به یک پل راه آهن خارج از شهر آق قلا حمله کرد.
🔹
هنوز هیچ منبع رسمی اعلام نظر نکرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668921" target="_blank">📅 12:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668915">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KAfn34cXn2_7sdP3bmatsQS2XRtBnlwQNv07g9A3ZYtqA5AFtRvsyy2NJY5if60-BIRYv2ncnHkZanO3lSPHVyR9ryZjMXhBVYKp_zuNaCIwkwHmDdnl7MQSOsHFReCDR39EGzmY7zPh3KTVcl9fMV7OQ0Mv_gtdTOEIDJJspi0oikvI4tg83rqPqZoh8093Ifdfw3ohl0ks19YP8y4IJAkmeIS9Gva7x_KtVt_9gHG41ibflw_bkXOZZj4IJ54ND2ExZASas3npVlXWI67H5Yr8mUxfAajDizZrBIgpcqeZyqVnRGY5nVjGOntCiwYBJ4NIqjzPtdcS3hsCl-J5FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r-O7Pus0zLIEExGLZd9EmBD4hU_5AveanRJNcFoFM1gLFO0r0VX0fQfgpcrr2it3u_qjUPCqtc-JkHsmGqND4gnQtUVlUP1mSknQCHB-vpngBNfl3v4G7lX_KVTusEhS1_dLLUKgMbsVAR19SKNjt1A_Rp3YFZvXVyG4gtSsnHnH1PnSnjDyKOUaRvz1kN2UlEpP85pX5_Rxf4Ef-noHEJ1dgtKfGfVehlSFfokwnIWu9njD7USsHlkepFaNB34l3nWXCVZRiUkrrnE_iFwOgIPjhxVM0acGfYfkjaVCHwnYloqz5pqBrdV6p5q-cuYtxSCJF6491iwUbGY_sAgVfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pnIz8vp8jKKkJU4krufUqR_Svsf47oDUjoUY4qS0ukYX03SfcB8L17cHwgoY0IX9eVjKIld-6ehhoC8WemNToNxB8TOZH0UiNU1miGr9l5DadA3xtkoFrgNgte1_8PNeaM2AjF8__PgjGNh2c0L7IhQIdVJi7ZFE7pWVOOCYE0Ku0wwDLbn2rnIas8sUrDI5A8Bl2AABmZsHi9kNeubkeDqr-XixlfamcZQVNhshYpHCLJGXvHPdFztBDigW3DiCfAT_NAVMltPbBj85DlkI5WOwQPDwoSIBSKzDwICa-UUlSAMwZLSFBmnJhMwxLoe470ukpHZZZiBlo3MFT0xo6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16cb8e8b1b.mp4?token=fXUR7SuYJxdv74VPaitoZOXmRCOJKVudbXtj2UFQz23GDjyhtBz7xTu8nU2GBfkYohJbPSut_8yiChGSqy6tCTWa4-GjymZGWUWgDdD6gy1ItVYRxyM9ON6mfqMFXJE10Ilv_Rhvu8K0743i_mQg_ILuTcKf08e6ArwyRtfHD-V0IJXNGtTtxAISifwQE8DvJeEyEveH7hssgphfQlDr4zz-vniqph-wkqPROG5GALJb60b9a4H6xTl0vExnnFFKFMRaoIcIdc2gGm7mqLtpRehlylLkLtHeWXq4f0HiA9L7LwaTkBBN0TJssXrGSN_v1TYKzMg2GUogKHcrAPKdJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16cb8e8b1b.mp4?token=fXUR7SuYJxdv74VPaitoZOXmRCOJKVudbXtj2UFQz23GDjyhtBz7xTu8nU2GBfkYohJbPSut_8yiChGSqy6tCTWa4-GjymZGWUWgDdD6gy1ItVYRxyM9ON6mfqMFXJE10Ilv_Rhvu8K0743i_mQg_ILuTcKf08e6ArwyRtfHD-V0IJXNGtTtxAISifwQE8DvJeEyEveH7hssgphfQlDr4zz-vniqph-wkqPROG5GALJb60b9a4H6xTl0vExnnFFKFMRaoIcIdc2gGm7mqLtpRehlylLkLtHeWXq4f0HiA9L7LwaTkBBN0TJssXrGSN_v1TYKzMg2GUogKHcrAPKdJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مشهد با پرچم‌های خونخواهی زائران تشییع رهبر شهید سرخ‌‌پوش می‌شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668915" target="_blank">📅 12:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668914">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=imfI_smVaCBvvrGzvvZY9DaU4qOpenEZAl9YvtkQ6P_wzb74bOqwWYHHG3woTpcKt0R7O401hXhgELPOtfRc5Y5ZplDXb9LEtWBdWWAQiyMcBETslHWaVLsfGEPvDBkZiXh4wS-jmwsKtSVk_Pw1vnnt_QLn0aS_Ue2tDrMY0aD7v5ropondlVBEeiDfC34CnYfUVooc3iNx-uxNhDIuHA3dq8p19pek8SL26CsL5VrTp5KnosZtwpo76j-Czj35vctpsCe-VkQERUlS7zgGOrOK-gKJfdwenkO1eE2TtdxTPgHqpq43FQEMjZGUY04Ghw5qiKYrQr3oatQmuADjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d6acd264.mp4?token=imfI_smVaCBvvrGzvvZY9DaU4qOpenEZAl9YvtkQ6P_wzb74bOqwWYHHG3woTpcKt0R7O401hXhgELPOtfRc5Y5ZplDXb9LEtWBdWWAQiyMcBETslHWaVLsfGEPvDBkZiXh4wS-jmwsKtSVk_Pw1vnnt_QLn0aS_Ue2tDrMY0aD7v5ropondlVBEeiDfC34CnYfUVooc3iNx-uxNhDIuHA3dq8p19pek8SL26CsL5VrTp5KnosZtwpo76j-Czj35vctpsCe-VkQERUlS7zgGOrOK-gKJfdwenkO1eE2TtdxTPgHqpq43FQEMjZGUY04Ghw5qiKYrQr3oatQmuADjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از همراهی جنگنده‌های ارتش با هواپیمای حامل پیکر مطهر رهبر شهید انقلاب و شهدای خانواده ایشان، لحظاتی قبل از ورود به فرودگاه شهید هاشمی‌نژاد مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/668914" target="_blank">📅 12:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668913">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
فرماندار بوشهر: حمله به نیروگاه اتمی و جزیره خارک صحت ندارد
فرماندار بوشهر:
🔹
در ادامه نقض آتش‌بس از سوی دشمن آمریکایی، شامگاه گذشته چند نقطه در شهرستان بوشهر هدف حمله قرار گرفت.
🔹
این حملات هیچ‌گونه تلفات انسانی در پی نداشت.
🔹
شایعات منتشرشده درباره حمله به نیروگاه اتمی بوشهر و جزیره خارک صحت ندارد.
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668913" target="_blank">📅 12:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668909">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wpgc2rwZI544dc5IVWNB-9E-TbovLJKDWaKiGoTdRsgbeh6S9IzlNInm7blY2VlWQbMPNSh4xThzCXhkYlcSIZywJTFANFpF_UzPIVkCbD6Eh7HV8NTdDsjesd2-YBoXtq0II_TZ9TMzNLZn1OhUT4zlQB8oPa2u8Lm9oDfCzNq6Fw1XAMA_epj6gN6aCHTYPd1nViAk1LjHWxy_uHls1eszuFQ-ASzspgm87ah12RUaVlR50Y6k2eT9DpgAqrQ34srQ4aa0-ENqKSW8nBjwY5pjozM2ci82a9CY51ctK2JJGGjHa4eoP8s2qQiAHBzTKWcwF-3xHZ_EtCWAQ73ZhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f-xn9eBny19oZ4CNDe13WRMz1L01vuvyzf3e2N6xWEIGx18tLoVnWSDAEm6QgUjzgeJuhJ944v0MuE7tTACg2kegqLLJPe-hApRppZDblrTGbHb_-ZdvNy9FLcdssLe7a1JcHwZKXSr4LPuJM0Wb4l45J1g8aZmijfCDs7Xc-dPtRnejeAkA7D3T4BqjSGK2L40jFBHBv_hgGEiwOt4G3c6ZFgb5Xhz2_2S5bqKAmrJ3yUxjmDW5E4R7a9zYDIODJbIGW7u6x63Lj5yKW46f0VF7bhs-ehnAIz3b4rNCJ8mGnblwx5KzLGtOAp1K7urOPzx-GSbEkebIN_MMyYnzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZNqF9WdmA1J-8dGV43tdFnpU0v9xjXA3-bzGpmgtWVn9_AjvmdA3XpdOVhi-paMWSHZZC8F8zSoNyItfsLceWrJWMASVA95vk7o4S9hyEfdVEaSvH6S7Y59cm8RTXf9IXin0atVH0ySezfxAGnWwtotOy9bxeN56-5XbapppOd-NaQfHKs6sIIWI9xBu4bXFSjHUi1NZ5uDaCsSeIR__2yofuPYTkCJ1yAR47mA71nc4sogNY_NKoiyDQU1Gs1r0NWVXOiedDMR-bffqyph829uX-ToRiDx6IJRoa0dKOcaCP0b628n4Pmx741qygSb3lhbZ_Roa6RBxelPzIdMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psb2Jol2tM5g1NCVMzbAj40th1I4cR-3jn9cV3iXI2yMoK3t7yqoTB9qOlHdKr4do1yD6zPYm9QAKqjnITGBhJffUas3eMTJkC16mipujObtWBCnHNWes9EcfzitAdIaIQHthJClxaK0P-CwVt2Q25a7RLTvzbTMuw-l11LVVTyx3dmpV1Ha3XfuGfnpfBsOyFusM0nlowTIkopCX6pNYzI1VhApH2CJqmEWD_u7-QjV1eWtPDPDbH_4nNqZzHq_ttHNk38vuhpAsu4_VOFlVOmu-3v7Q4snM5eDTMx0ggDXXF8Ztd7dQpO8A_DWPXrcFBIkoKLtu1sU0AXMDRAmYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اقامه نماز ظهر و عصر منتظرین امام شهید در خیابان‌های مشهد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668909" target="_blank">📅 12:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668908">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43fb1c4e7.mp4?token=JEvZ_GrFB4DfSaQHOd-MoPraHGPx27VNdL9u6Dc_qOeXEMFfHG5fKgin3zfhwA2d4yi2TXzKbuYt6aKxjIyztqndilqB_-dK3XZZcGAX3CuoKSFq72qfAXvcOWd9zy1mEeExUe6VhPsETxA3oNgWSfTDLB7yhdueHGETApGWlhfOYFzTwXs043IY9CBZScZefVSSVx73nsgvR0AH26mdCTcdG7mXZRAOEIHB0shXT9uCMtcd9-axWh31YLf4r__ucAQo9s3Ss4Ogg2pqImj5of5LzmzbZfb_6M42qD6sd4BEY4l4mcERKHELCwJ7gq6vp9DFe63RlrIQOHvZaI_MUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43fb1c4e7.mp4?token=JEvZ_GrFB4DfSaQHOd-MoPraHGPx27VNdL9u6Dc_qOeXEMFfHG5fKgin3zfhwA2d4yi2TXzKbuYt6aKxjIyztqndilqB_-dK3XZZcGAX3CuoKSFq72qfAXvcOWd9zy1mEeExUe6VhPsETxA3oNgWSfTDLB7yhdueHGETApGWlhfOYFzTwXs043IY9CBZScZefVSSVx73nsgvR0AH26mdCTcdG7mXZRAOEIHB0shXT9uCMtcd9-axWh31YLf4r__ucAQo9s3Ss4Ogg2pqImj5of5LzmzbZfb_6M42qD6sd4BEY4l4mcERKHELCwJ7gq6vp9DFe63RlrIQOHvZaI_MUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در انتظار رهبر
آزادی‌خواهان جهان
🔹
حضور گستردۀ مردم عزادار امام شهید اطراف حرم مطهر رضوی ساعاتی پیش از آغاز رسمی مراسم تشییع
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668908" target="_blank">📅 12:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668907">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e5f784f8.mp4?token=ggHi0mYJE3scBaUEGM_5cMLBtIR_LbtLgQNWs38v1qkO8RlCGbjSeNKWRnXs0ZBpGQOQjJOePXFaFPtnnHiaO3v94QCbfE3iqNdeGmanelE8Kx8osD32AafPFwebuX13aIoF3VOosgHLB4XnJpoRHeUxFSH4ioxdZarQ6uPflXNBUaLL_QKUFGBqiK2kV0zjiCp-SSEIBTB3WtMpX-hiY3Hh6THIEoCX7V9wdRIMFYY6wSG8SB2GtqqKM8TboQrsZjIHem9AhXFcCXDyl-LlsKGvQh1QDLflavrMBa8EgyPv8Mhu6lInZGXtT6SsxscapyUbNbFg5VlJCWdRNLhyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e5f784f8.mp4?token=ggHi0mYJE3scBaUEGM_5cMLBtIR_LbtLgQNWs38v1qkO8RlCGbjSeNKWRnXs0ZBpGQOQjJOePXFaFPtnnHiaO3v94QCbfE3iqNdeGmanelE8Kx8osD32AafPFwebuX13aIoF3VOosgHLB4XnJpoRHeUxFSH4ioxdZarQ6uPflXNBUaLL_QKUFGBqiK2kV0zjiCp-SSEIBTB3WtMpX-hiY3Hh6THIEoCX7V9wdRIMFYY6wSG8SB2GtqqKM8TboQrsZjIHem9AhXFcCXDyl-LlsKGvQh1QDLflavrMBa8EgyPv8Mhu6lInZGXtT6SsxscapyUbNbFg5VlJCWdRNLhyfYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ظهوریان، نماینده مجلس: نابودی اسرائیل و آمریکا و خروج آمریکا از منطقه جزو اهداف آرمانی نظام است؛ اما قصاص آمرین و عامدین در پروژه‌ها دستور کار نظام قرار دارد/ خبرفوری
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668907" target="_blank">📅 11:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668906">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f36ee3ed.mp4?token=hCxXVIoyqQ8dXWlId_HRr-4Vz03SJyU3AeX3K5C5tmrRMPvmIKvxXS-3R4S_W0OZKpBx1yrWFlVjWqe6eTtYoC2RoE_DNIHVKxGDcSiOpj67u--YsUwbPm1u3-BOKJb606tduUNPp_sTnJY8jTxd8JFwnVA6HS-QeSFlIb7_8jQNCskb57IqEWEW3GzP8E_FiU4uy18iboe-z56e3tjK42f-Gv1C5QDxeXUmON8Ja0W4WlfCYxpS29EHnn1nt-FjjrlfxhVC7qrqIfOOlHBlAp14qShTE6Ac12biFPiAb9Doerd_sCS2PgE42JwyPC16kOs7ll5a2LBzKW7TxUiAEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f36ee3ed.mp4?token=hCxXVIoyqQ8dXWlId_HRr-4Vz03SJyU3AeX3K5C5tmrRMPvmIKvxXS-3R4S_W0OZKpBx1yrWFlVjWqe6eTtYoC2RoE_DNIHVKxGDcSiOpj67u--YsUwbPm1u3-BOKJb606tduUNPp_sTnJY8jTxd8JFwnVA6HS-QeSFlIb7_8jQNCskb57IqEWEW3GzP8E_FiU4uy18iboe-z56e3tjK42f-Gv1C5QDxeXUmON8Ja0W4WlfCYxpS29EHnn1nt-FjjrlfxhVC7qrqIfOOlHBlAp14qShTE6Ac12biFPiAb9Doerd_sCS2PgE42JwyPC16kOs7ll5a2LBzKW7TxUiAEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حدادعادل: محبوبیت رهبر شهید انقلاب فراتر از مرزهای ایران است
،
حضور مردم عراق پیام روشنی برای دوستان و دشمنان انقلاب داشت
/ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668906" target="_blank">📅 11:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668905">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21c262c988.mp4?token=cUjD7Bvh0jMYoZ50eU4bvsC9G49JSTbebg7YK0lv4MYpAfZaz1ivNOXI_vIuuoRIJKEv_0CwlSDxZF7nWn5YmlAhf23SEPcdqSVFeYPYtfROSrPWkzARBqVEzA0K3gCaL_sTeQOf-gD6Dhj14GDpK7b-hi4c_0colSoEB6o00tKAT1yBnnyUR2cIhFsDyYZCnaTf7PayM7fsuREdelHd6mQBGt8wQ38vqKlXwU_WW7TRaBW8JW5NEEfQZ1YPljjSffRNzqQl3MvB21L3BJ-w_vzs8MnHzvSM359GhQINiwmuSHyxCx92fE6TQsCKhQIUyN6s4D1s4lAW7osucMUdh2xYGPOLv2ciOjX2gS2UDU2sDUyrqUcQBrKhFFgp4c-_EMaxiwR_8fXgpDwChg9YXFXgEdrRhtAP9ZVJ1WQ9yrNSvdv93894Q-hiVdIWdbkC01z3ARAnFjb8eIRWtMLq_vPufqyMkhGpcpsbkONOYpyN7gm4-2zrvfi4G7bAwxlzEdpGLARrT6hFpDsjPKCqH3MFxoriw9JIOulZluSI5kYcPG0NZpGaM1gDvYF2x8CGEtZoDFTdf6hkjSiNW9kv6vPGXiRW2Sg4g2HS9zAn186HQxYHUa2QTlwjU4XBGo9Ifhk7K8WZF38N5p6NpnwfuCic7vKKr9zgdOWtHNgVYpY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21c262c988.mp4?token=cUjD7Bvh0jMYoZ50eU4bvsC9G49JSTbebg7YK0lv4MYpAfZaz1ivNOXI_vIuuoRIJKEv_0CwlSDxZF7nWn5YmlAhf23SEPcdqSVFeYPYtfROSrPWkzARBqVEzA0K3gCaL_sTeQOf-gD6Dhj14GDpK7b-hi4c_0colSoEB6o00tKAT1yBnnyUR2cIhFsDyYZCnaTf7PayM7fsuREdelHd6mQBGt8wQ38vqKlXwU_WW7TRaBW8JW5NEEfQZ1YPljjSffRNzqQl3MvB21L3BJ-w_vzs8MnHzvSM359GhQINiwmuSHyxCx92fE6TQsCKhQIUyN6s4D1s4lAW7osucMUdh2xYGPOLv2ciOjX2gS2UDU2sDUyrqUcQBrKhFFgp4c-_EMaxiwR_8fXgpDwChg9YXFXgEdrRhtAP9ZVJ1WQ9yrNSvdv93894Q-hiVdIWdbkC01z3ARAnFjb8eIRWtMLq_vPufqyMkhGpcpsbkONOYpyN7gm4-2zrvfi4G7bAwxlzEdpGLARrT6hFpDsjPKCqH3MFxoriw9JIOulZluSI5kYcPG0NZpGaM1gDvYF2x8CGEtZoDFTdf6hkjSiNW9kv6vPGXiRW2Sg4g2HS9zAn186HQxYHUa2QTlwjU4XBGo9Ifhk7K8WZF38N5p6NpnwfuCic7vKKr9zgdOWtHNgVYpY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فعالیت سازمان مدیریت پسماند و استقرار ماشین‌آلات جهت پشتیبانی مراسم تشییع آقای شهید ایران در شهر مقدس مشهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668905" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668904">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb_3iooVFvwaCGDl0W3oUr1SJvO29BKD2KzRSr96Xstg_2L8kMm4IICWpRQB8Hgjj_BT6f1hF6qv7CswlRW1dzNVx14ZuneJ9-iXr0nhpPyNvjuHNbe_mZ9WlGm_ZslR_gFkRy9CVLRJAnOwMGhMUkD7NHAQDa-xGfsxv4zqDN3EIcYYunR1sUGlGWJMYwSqTad_vC57ofZA3fLXWQW4plFDdd5B-ez2y9hRLZ9X0IyjS6uXyOD6iP6BTstx2hS-yk38Jz5COzXTTpYDk8e521AENxhXkeo4ViGTqSXh-j2AcySzRtRiM0BBbzhjVkfh7qvf8wlxANqkVr3qpGSK8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کاهش قیمت نفت برنت به کانال ۷۶ دلار
🔹
با وجود درگیری‌های شب گذشته در جنوب کشور و پاسخ ایران به حملات آمریکا، قیمت نفت امروز کاهشی شد و به ۷۶.۹۵ دلار رسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/668904" target="_blank">📅 11:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668903">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
استانداری همدان: نقاطی از شهرستان کبودرهنگ مورد حمله دشمن قرار گرفت.
🔹
شورای عالی انقلاب فرهنگی: تعیین زمان امتحانات نهایی و کنکور در اختیار مراجع اجرایی است.
🔹
فرانسه خواستار خویشتن داری و ادامه مذاکرات میان ایران و آمریکا شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668903" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668902">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f854d7fb85.mp4?token=mVOiWP65dMNHS0JD8wqwiewaqrmLzl3Pl4ZaMpHyR1ysFoVjvqXUh5c_os4Iq3u4BfdyXVFRuB5tbVRNoD8IfZhjSNQ7TAAbZWC_xbPhwZ_S_wYNIMSKsCu5mCzO3WMisWI9KM27cMyFKVd-J9f1SBJBS2pmLYg_YrA9fpxfzkK1LbxICJeLAvsDfPhSI7WdqgHuBQdWpfjhSOjA09XZ0tCQmybgc35t7P8QgJTeltCBhmFWvehUywHWlZQsEnA1OF26y_ZD1KRO-jqQ8Br6q9zEl4dVYrPWn5hqKyg2VLbX6J96tpR-g_Mq_B1WcLdYjkDTNfq94ja-m5VEqGq4wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f854d7fb85.mp4?token=mVOiWP65dMNHS0JD8wqwiewaqrmLzl3Pl4ZaMpHyR1ysFoVjvqXUh5c_os4Iq3u4BfdyXVFRuB5tbVRNoD8IfZhjSNQ7TAAbZWC_xbPhwZ_S_wYNIMSKsCu5mCzO3WMisWI9KM27cMyFKVd-J9f1SBJBS2pmLYg_YrA9fpxfzkK1LbxICJeLAvsDfPhSI7WdqgHuBQdWpfjhSOjA09XZ0tCQmybgc35t7P8QgJTeltCBhmFWvehUywHWlZQsEnA1OF26y_ZD1KRO-jqQ8Br6q9zEl4dVYrPWn5hqKyg2VLbX6J96tpR-g_Mq_B1WcLdYjkDTNfq94ja-m5VEqGq4wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ ابراهیم زکزاکی، رهبر شیعیان نیجریه هم خود را برای تشییع امام شهید به مشهدالرضا رسانده است
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668902" target="_blank">📅 11:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c2cf8e67.mp4?token=lNxTftwEu55FrX3fWkvl1Pxlm8JnVKUnhUerBLE1yBv8sDuekL3OfIvHVukuCthf9_IDMPL1xczwQY9eXtbMj9Dym9572AJ3PyUGrYQtv-BgvxJBchvp0RA3jwDoKqvu3b5u-7BKRuLuR6Au285VDIUE9t-zC3hG30pwoL-qjt9lKuGr8ie0R8AQSKGBRKDPFN2j5iqRD3jFTNIrOOa2kEzaJLcw5_roKKG9u8s4ZsTRQVa31i-_rOey2CueVWGSoV_ThmjEF7uHjJvSa8voF0M2vRMoKuE-B4Klsj5PpBavAwfezwKBRhDcR44G7NRMuJVBwXEMui8p4We1JFer0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c2cf8e67.mp4?token=lNxTftwEu55FrX3fWkvl1Pxlm8JnVKUnhUerBLE1yBv8sDuekL3OfIvHVukuCthf9_IDMPL1xczwQY9eXtbMj9Dym9572AJ3PyUGrYQtv-BgvxJBchvp0RA3jwDoKqvu3b5u-7BKRuLuR6Au285VDIUE9t-zC3hG30pwoL-qjt9lKuGr8ie0R8AQSKGBRKDPFN2j5iqRD3jFTNIrOOa2kEzaJLcw5_roKKG9u8s4ZsTRQVa31i-_rOey2CueVWGSoV_ThmjEF7uHjJvSa8voF0M2vRMoKuE-B4Klsj5PpBavAwfezwKBRhDcR44G7NRMuJVBwXEMui8p4We1JFer0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم خاص خونخواهی رهبر شهید در حاشیه مراسم تشییع رهبر مسلمانان جهان در مشهد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668901" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNyER5I8oIegEM8a2uM1NpLMqR3T_1MSmK_m08e4FYG74tiLKdFtCu7JorC5ekdQ4ZTPkW-MsMFDFzHbZ4QB0hcnYTN6KbECcvef4B8tDbScF3Ihgsy8S-UTM25cDXoQ6BeZTEAaExGtf_s0L7Gy7q3-LZytgUb7D2LuQxcCPGflOnQ7gjAdTFMKFirYLkkqNVYNl0tr-wEwDzLmMhwvdy8GxQMAej1fGyqF6tHiBf_Nqe0ZHn-3Z3jfG937ra3h4t5pnZQ1MPZCYl8UjQONv80WSqdZ0B2Q1MfdNIKmz7HZK19lPIc53cv8kVyErPr1uOlDVw1PchDDAXkTUDuGDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره اقدامات تجاوزکارانه ارتش تروریستی آمریکا علیه ایران در شب گذشته
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668900" target="_blank">📅 11:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d69f5bd3c.mp4?token=SRkGcT1FhDnn1M9CGMcSnmbKBG5Md29p6ZRcZfyT2OadpfDlq3rYg3qva_pC9EFjbghIN5qv-JKIxYFO60872UJPamxg3FpOonKRMYIWwqc8JxWChPB2WwIVutGaFZ_7siRODVeY7Y0MfyID2-ninh7_kEv3BAcN1HgwwnoXoOm0CkvN1u4ty4rh8Z9dnH_3oGQu6FoDFxXzhM1_TqxX-wu9yxFJ7wO7Bt2JCuSaZd6zTQOni-SD9SzHQzClEG4Y-Pgk4oX1eWBWSAJKCXj3tdWBMc3IGVKzsxtuMxVSQJzIK1HGOmeVOh3Ugl-DDJpuRlsb1e147b1GGbPt24kE_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d69f5bd3c.mp4?token=SRkGcT1FhDnn1M9CGMcSnmbKBG5Md29p6ZRcZfyT2OadpfDlq3rYg3qva_pC9EFjbghIN5qv-JKIxYFO60872UJPamxg3FpOonKRMYIWwqc8JxWChPB2WwIVutGaFZ_7siRODVeY7Y0MfyID2-ninh7_kEv3BAcN1HgwwnoXoOm0CkvN1u4ty4rh8Z9dnH_3oGQu6FoDFxXzhM1_TqxX-wu9yxFJ7wO7Bt2JCuSaZd6zTQOni-SD9SzHQzClEG4Y-Pgk4oX1eWBWSAJKCXj3tdWBMc3IGVKzsxtuMxVSQJzIK1HGOmeVOh3Ugl-DDJpuRlsb1e147b1GGbPt24kE_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون حال و هوای حرم مطهر امام هشتم علیه السلام
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668899" target="_blank">📅 11:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668898" target="_blank">📅 11:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668897">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa01590978.mp4?token=nf9S0eLlHbi4lsMsr83MrOI6d1lM2wSlEzyHaVChtbqSjWDrhaLbkNCKN-KfC07woA1MrTaBEM7FvOVz902wP9ugqFJ50mFQ_Wr18BEB1pOBfb19J2jiePxR1rjgX-lWd9k58vHm9DivVSB2TDBxeSrDxszrz6Nily8XB7Y4nVxS9idfbVr8V7xHY4K5TvuM4CTzgIDBDTD1ZkU11a3ymwJldz-Ai19wtbhWhSp7zQIaveKtYUe7Zebv5IOV5haZF6ysY45mhE4yfjhqAo8h7UTDKDNzRg7RA8HKBMeFeYPPyfFqn7-ZcFZhSu-8C6pLJYE0iRrOnrONRLx6vknDOqjoI3As2cM3C-BorehLWJw6sEm3WEZM7fKtpxzhN23xywPEWpsqNFTn0E9qqiP1hu7p3gHGR13B8FwMN9AO81WxJNAUhQnMeV9w_XlSSchOEUQF9ED_bR4uRkgiuTa6igV3syxiGOpTZt8S17SVcMK7Ca8x9V-ALFro8Lq8xfPl7Mffl_l5o6B711CdtyovBL-DD3RZ8zSq6o2xG0F1AlRoGREV1YI883gSekJ4lcW5t15ExDw08KWSxdeLPkJZjPmd-HKxWDzap2dZifLkyqjnkpTq39ZVEOqxbXvoBY7CIPL3lSlPBVtY-3xJHcZvot8Sg2oBK74o6AUZQQXPf3U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa01590978.mp4?token=nf9S0eLlHbi4lsMsr83MrOI6d1lM2wSlEzyHaVChtbqSjWDrhaLbkNCKN-KfC07woA1MrTaBEM7FvOVz902wP9ugqFJ50mFQ_Wr18BEB1pOBfb19J2jiePxR1rjgX-lWd9k58vHm9DivVSB2TDBxeSrDxszrz6Nily8XB7Y4nVxS9idfbVr8V7xHY4K5TvuM4CTzgIDBDTD1ZkU11a3ymwJldz-Ai19wtbhWhSp7zQIaveKtYUe7Zebv5IOV5haZF6ysY45mhE4yfjhqAo8h7UTDKDNzRg7RA8HKBMeFeYPPyfFqn7-ZcFZhSu-8C6pLJYE0iRrOnrONRLx6vknDOqjoI3As2cM3C-BorehLWJw6sEm3WEZM7fKtpxzhN23xywPEWpsqNFTn0E9qqiP1hu7p3gHGR13B8FwMN9AO81WxJNAUhQnMeV9w_XlSSchOEUQF9ED_bR4uRkgiuTa6igV3syxiGOpTZt8S17SVcMK7Ca8x9V-ALFro8Lq8xfPl7Mffl_l5o6B711CdtyovBL-DD3RZ8zSq6o2xG0F1AlRoGREV1YI883gSekJ4lcW5t15ExDw08KWSxdeLPkJZjPmd-HKxWDzap2dZifLkyqjnkpTq39ZVEOqxbXvoBY7CIPL3lSlPBVtY-3xJHcZvot8Sg2oBK74o6AUZQQXPf3U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشتن پرچم فلسطین توسط یک کودک در مقابل پلیس آلمان
در تظاهرات همبستگی با فلسطین
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668897" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668896">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5qkPBAOWPtPeq8kcVb37PYy10SXqQ90Syrz30UaMhc8_0qc98HHCAEjDbBSVo9Am01i8UaV-PJFUlRi-ep24kNxAYiw4DonYMBkcFfgAKqPyGzisbfOgU6AogWCbGcbn1AD7SleVYgHYNJ068YA5LG9gY2-yrILgC6-NsQ2OCkTcgieqaVOu3J1sNM1TuYB_9HLr3xGLQAqC81uD6smOrpzGaZha95AiYN8iHdaRjz6_dHRhqrODRHmhnijb8QOiRsZFdPrLy_pfa9tmFGaancxAuuUc82XfHGEE_3v4rnJM4Xe6ja5PtVJSVciqweMQwbj8We7h9i5lB8qZhdCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پویش مچ‌بند و پرچم سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با مچ‌بند سرخ و پرچم سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ و پرچم سرخ، نماد عهد، وفاداری و خون‌خواهی امام شهید است.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668896" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668895">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزارت کشور بحرین: آژیرهای خطر به صدا درآمده و از شهروندان و ساکنان می‌خواهیم که به نزدیکترین مکان امن بروند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668895" target="_blank">📅 11:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668894">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آموزش و پرورش: دریافت کارت ورود به جلسه داوطلبان ایجاد یا ترمیم سابقه تحصیلی فعال شد.
🔹
جوزف عون از آمریکا خواست اسرائیل را برای توقف حملات تحت فشار قرار دهد.
🔹
تسنیم:
تجزیه طلبان بلوچ شهرستان چاغی ایالت بلوچستان پاکستان را تصرف کرده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668894" target="_blank">📅 11:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668893">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e94190b053.mp4?token=fJvD-EWRDOyjOVFsjysadEWi038wfluLgMjigz_IBpTy1iKsjHTOxPCVa9C9gQpTwtP7iPuA0Qg8L3sXv2UOqvaEZvT7dOY1krB3hEgyUYm-VoAnaOSMbIk9NsnXgRd0DY0ZeJYhwPGfKO3KVxzyiQdboODXhmh85bs9Hq6i0ejwk0op5fAP82uazfmgqnfpYra_se7FQUvWshq4c5N2V7ic1pDOXKcucKWUUSOs75YYxOmw-jQUq37fP6FYO7ZLuuZZmdSc16H4XhT6QXn-r6T9pFMTeoEfoUK90qO5DUWt2-455Pl0XJ4IqOv2XyPn48rST3je2lvu9-g35YlJlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e94190b053.mp4?token=fJvD-EWRDOyjOVFsjysadEWi038wfluLgMjigz_IBpTy1iKsjHTOxPCVa9C9gQpTwtP7iPuA0Qg8L3sXv2UOqvaEZvT7dOY1krB3hEgyUYm-VoAnaOSMbIk9NsnXgRd0DY0ZeJYhwPGfKO3KVxzyiQdboODXhmh85bs9Hq6i0ejwk0op5fAP82uazfmgqnfpYra_se7FQUvWshq4c5N2V7ic1pDOXKcucKWUUSOs75YYxOmw-jQUq37fP6FYO7ZLuuZZmdSc16H4XhT6QXn-r6T9pFMTeoEfoUK90qO5DUWt2-455Pl0XJ4IqOv2XyPn48rST3je2lvu9-g35YlJlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه ورود هواپیمای حامل پیکر رهبر شهید به مشهد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668893" target="_blank">📅 11:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668892">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
تجاوز مجدد صهیونیست‌ها به سوریه
المیادین:
🔹
منابع محلی در جنوب سوریه اعلام کردند که نیروهای اشغالگر صهیونیستی به اطراف روستای صیدون الجولان در حومه قنیطره نفوذ کرده و یک ایست بازرسی موقت ایجاد کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668892" target="_blank">📅 11:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668891">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1348bd0520.mp4?token=OtBLqAbBZDaQCh4GD8SmAR8zMfz6ULUeaHYSNpDkBVhCgll-HFUWei1xReQ4X_o_xPzb7-xHURBn72pKTytKEqfKDJfiMDWqum-LYDovvGv03FHxhBQF2VMD-ib55zjpfQxYD4SoBd8RJrEew6aZNeQchjhYd5IPkPJmOHOmkjeBcAaBny7aYAWtdtMkmbcKVFcv7BBHywWw9082A00dvmAwpHHVh2lfRf2ON9Pz4ToKbZVs1AEJRtzXKlJQKrPPJsbCaC0nXdldz40ap6mctBcBcc_zAJfjUxgad1vL3Ui8OO9CLrS5tOLkLF2hdCUP1g7pKx2sWDNGIAFKn6FXbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1348bd0520.mp4?token=OtBLqAbBZDaQCh4GD8SmAR8zMfz6ULUeaHYSNpDkBVhCgll-HFUWei1xReQ4X_o_xPzb7-xHURBn72pKTytKEqfKDJfiMDWqum-LYDovvGv03FHxhBQF2VMD-ib55zjpfQxYD4SoBd8RJrEew6aZNeQchjhYd5IPkPJmOHOmkjeBcAaBny7aYAWtdtMkmbcKVFcv7BBHywWw9082A00dvmAwpHHVh2lfRf2ON9Pz4ToKbZVs1AEJRtzXKlJQKrPPJsbCaC0nXdldz40ap6mctBcBcc_zAJfjUxgad1vL3Ui8OO9CLrS5tOLkLF2hdCUP1g7pKx2sWDNGIAFKn6FXbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل مرگبار در جنوب چین با ۳۹ کشته
🔹
سیل و بالا آمدن آب رودخانه‌ها در جنوب چین یک سد در شهر جنوبی نانینگ را تخریب کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668891" target="_blank">📅 11:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668889">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjGM672o1spAmoG58-19b0uI7br4febKKvNjJBAyMMQr-uI1jy9vh4lBH_yIdnHlHxrYiXbtFZAXvXeuQpGa4K8dkLivftgXGZay-Q7I7NLX0lGCnU-EJnyewYZ4uxYFMCiA_2q4G1mVSAqeQ02l9hUUv3jjmFYNEZR6gcO1ONhEnSNrQSsMoJC7qfuXPSyoahdLJKYfkmR4QmXYfKuQdHUn8vuv5rBxbbaCxwzmqhiBoRkvn__9e4W7sSNQTyriGo_7es3FjUNqcxsb5XZ78Dkb_ky_JKgQdaT-el4YjDKkEGXDpwryOhQ4skdD9lT5i2S5e-7lHSGQdKOSJt8AoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر جنگ رژیم صهیونیستی: برای ماندن در لبنان از کسی اجازه نمی‌گیریم
🔹
«یسرائیل کاتس» وزیر جنگ رژیم صهیونیستی در واکنش به اظهارات دونالد ترامپ، رئیس جمهوری آمریکا مبنی بر اینکه "اسرائیل" از لبنان عقب‌نشینی خواهد کرد، گفت: ما برای ورود به لبنان از هیچ طرفی اجازه نگرفته و برای ماندن در لبنان نیز نیازی به اجازه کسی نداریم./الجزیره
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668889" target="_blank">📅 11:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668888">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d1640fe5.mp4?token=RBaoaU0IEw4nJyldLQ_UQ0otcyEgWqsmgC9kR6t2dwsT6BgXk5gGkbrbZ8D-IOGnpDFyq9HGWOt1MQQO-ajuL7xmBn95xr9zkaihsrzi_CsV1Qu4FJmK5MGGcWgvFsusHocLty20bDWpqHZC8JpH1xtDbtJZLvYS76zmus5caSJuz6dzYsERp-PIIoosr9024m8JG1aTA7czA7AOtLzjitqWpl_c_lFaMtVf6sbl5qXlOB2pbuQfc4y-2TrrwiGNBR_LR4i5u7Ee-u0zG6TV1RIhJzuHha_yCwayZixWNcsNdFoorz-ibXLEsINocqwJNWKr23TyldizqbYw3XfLu1Uy4riV-NSXS6zAl29dHFLRxjabKZG3Bf2mWj8OS9uk0LKxHZl4135vhI03xAjeJpbVgE2M7-me-rIpgT2fXpJ5BIn_SO0yOPhYoSQ0eQLeCerBlECQpitM0G7CMkz7eauPR9BV04PhO-1sZTIqabgOsFTHXA_XBQYHKebQnr3K5nMLKMHt6b6ncoxYd3i2klHaSnr1pZmxCPIwFVGC5mgc7agVjU9pbWA5bV8J7rVybfqH9ZCJywPjUjm1eISXM8qu9qH7K_hXO1L0P0aXMtPE1un9wazo_y_fl_1Sq0KJRnq_tle4agclUZ1FKzsqIgtvCVQM8isR72SAXtmcZKc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d1640fe5.mp4?token=RBaoaU0IEw4nJyldLQ_UQ0otcyEgWqsmgC9kR6t2dwsT6BgXk5gGkbrbZ8D-IOGnpDFyq9HGWOt1MQQO-ajuL7xmBn95xr9zkaihsrzi_CsV1Qu4FJmK5MGGcWgvFsusHocLty20bDWpqHZC8JpH1xtDbtJZLvYS76zmus5caSJuz6dzYsERp-PIIoosr9024m8JG1aTA7czA7AOtLzjitqWpl_c_lFaMtVf6sbl5qXlOB2pbuQfc4y-2TrrwiGNBR_LR4i5u7Ee-u0zG6TV1RIhJzuHha_yCwayZixWNcsNdFoorz-ibXLEsINocqwJNWKr23TyldizqbYw3XfLu1Uy4riV-NSXS6zAl29dHFLRxjabKZG3Bf2mWj8OS9uk0LKxHZl4135vhI03xAjeJpbVgE2M7-me-rIpgT2fXpJ5BIn_SO0yOPhYoSQ0eQLeCerBlECQpitM0G7CMkz7eauPR9BV04PhO-1sZTIqabgOsFTHXA_XBQYHKebQnr3K5nMLKMHt6b6ncoxYd3i2klHaSnr1pZmxCPIwFVGC5mgc7agVjU9pbWA5bV8J7rVybfqH9ZCJywPjUjm1eISXM8qu9qH7K_hXO1L0P0aXMtPE1un9wazo_y_fl_1Sq0KJRnq_tle4agclUZ1FKzsqIgtvCVQM8isR72SAXtmcZKc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید به خانه خودت خوش آمدی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668888" target="_blank">📅 11:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668887">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e0d69b43.mp4?token=Ee-KLMSiFN7xYhL6nz0ZmTT4aRfUqGLz5VSZuZvF1NX5ELKrucXm33H7erI6eJ-GCsjWPMxC4K8j0hR0lswEAlR6nPqQ6iNWRE1GDWBAfXNQ1NpLeFv8F6lk30-cgCcKhXyedc4DkwgdMzvUIb6nyClvhhz08epn3DJDetDlNE9144CXSB4mwTgjzUF7luATDqhLBCbka47vPdvUgS3qwpI_5KdNIhPHC2rODT24wpKwgrzCmzZB1Hu35GNQmVz19OgmJF6JaqrSmtzHua5PJ4b9fTiQEVBS1EqErzscB-b6XF7KOH5ieQ2HIS5sMuIcCL5bmirPdTjT-Nfp2BbhHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e0d69b43.mp4?token=Ee-KLMSiFN7xYhL6nz0ZmTT4aRfUqGLz5VSZuZvF1NX5ELKrucXm33H7erI6eJ-GCsjWPMxC4K8j0hR0lswEAlR6nPqQ6iNWRE1GDWBAfXNQ1NpLeFv8F6lk30-cgCcKhXyedc4DkwgdMzvUIb6nyClvhhz08epn3DJDetDlNE9144CXSB4mwTgjzUF7luATDqhLBCbka47vPdvUgS3qwpI_5KdNIhPHC2rODT24wpKwgrzCmzZB1Hu35GNQmVz19OgmJF6JaqrSmtzHua5PJ4b9fTiQEVBS1EqErzscB-b6XF7KOH5ieQ2HIS5sMuIcCL5bmirPdTjT-Nfp2BbhHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از تهران تا نجف و مشهد، یک مطالبه مشترک شنیده می‌شود؛ «خون‌خواهی آقا»
اخلاقی امیری، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
اگر صد نفر مثل رئیس‌جمهور آمریکا به هلاکت برسند، ذره‌ای از شخصیت آقا را جبران نمی‌کند. ما باید تلاش کنیم در منطقه، اسرائیل محو و آمریکای جنایتکار اخراج شود
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668887" target="_blank">📅 11:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668885">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c47bada2.mp4?token=W24o6NWn_bnPlGBhcJYl42-OXV8Rr1yRdS1QXXcyTg6SW24wgCWJY8RZ38OWYKBEmG3RR-TkXNaXd2DIfaUQ5P6xKDfObIeOXBUrU9ATpk2VNcsm_jXeOWE6JvJqLMPmnmfGeBxeKMNx-hX-vIow989A4yeS33wnvtDLYmT5k1OUKIs1EbPzLc-HhCQtIRy-F7AkeFC_k6ODmvgTlhCXkIc4-dvVXr-A3xsoGM6S4TTVWgjfXbnjKm7hwT7nl9tY5s36lf1d1k7JT-U4T_7TXmYAwzOzcaN0413Uyus1Set3d92bJnYuNpCfpt-dlR5Nzh8BFsQ5XqINTdgH-JuhOE36Dxb3tWvWO_HN2zVd7IsntxlwaSZ7FP39S8tqdw-pDJ1h_sYO2etw5B0qxIJLSVTiKAy5WhflEuLzOnS0iGIa6iAntCEdVKu-ViI8UMmxCqYcoOFgW_AHMo_8t9pUlFmpqS9N1ijjAiIdmtMYeiQb_CYn3fYrw31gf2Ljj9OOvaN_QBu_oVlQq6YWFZVtFehHPxtsH_HYwdIMjg3N6H4r3aNsgWie-2NKEKnbNfffVLUFYorEboAPiU1Dt7NZDpu5NSnZcaCbREhNCAGmq7PougJbUdLdWZZWgbRINVr2c_2o5Lpv9jVxdPTFrmbOy7uprL72I0vsQjWYwoeqnt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c47bada2.mp4?token=W24o6NWn_bnPlGBhcJYl42-OXV8Rr1yRdS1QXXcyTg6SW24wgCWJY8RZ38OWYKBEmG3RR-TkXNaXd2DIfaUQ5P6xKDfObIeOXBUrU9ATpk2VNcsm_jXeOWE6JvJqLMPmnmfGeBxeKMNx-hX-vIow989A4yeS33wnvtDLYmT5k1OUKIs1EbPzLc-HhCQtIRy-F7AkeFC_k6ODmvgTlhCXkIc4-dvVXr-A3xsoGM6S4TTVWgjfXbnjKm7hwT7nl9tY5s36lf1d1k7JT-U4T_7TXmYAwzOzcaN0413Uyus1Set3d92bJnYuNpCfpt-dlR5Nzh8BFsQ5XqINTdgH-JuhOE36Dxb3tWvWO_HN2zVd7IsntxlwaSZ7FP39S8tqdw-pDJ1h_sYO2etw5B0qxIJLSVTiKAy5WhflEuLzOnS0iGIa6iAntCEdVKu-ViI8UMmxCqYcoOFgW_AHMo_8t9pUlFmpqS9N1ijjAiIdmtMYeiQb_CYn3fYrw31gf2Ljj9OOvaN_QBu_oVlQq6YWFZVtFehHPxtsH_HYwdIMjg3N6H4r3aNsgWie-2NKEKnbNfffVLUFYorEboAPiU1Dt7NZDpu5NSnZcaCbREhNCAGmq7PougJbUdLdWZZWgbRINVr2c_2o5Lpv9jVxdPTFrmbOy7uprL72I0vsQjWYwoeqnt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر مسلمانان جهان: اگر مسئولین کشور مقابل دشمن خوف داشته باشند بلاهای بزرگ بر سر ملت می آید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668885" target="_blank">📅 11:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668884">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb6c05a4f4.mp4?token=bDp2YG-TSOBz8M-1cvGUFDTknWc-0eOaCMlafkFsX98XMts1SbPCTqPSzxxLJmEntDNy9SsoSXtIV_I7HFBSsDTkDq4JZ6wW_70JOnoCq7-0_UnKtJden_hhyZ1TXoXlgXYuVvnJtlxgp-XMJCc3mPgp7xiVMWlvrFDXMhRMIknqYkn_6XzJDjIyxbRZGfD4wMyCrcErjoFU5xq-LdUxq87WNzLdBJW81Mqq6-N6T6bf20yo10Y7YJI5Ts0PymR33nCvAa9pypoIOVh3ehtoNGzYRieqYQMLaPUkAqDuF0N-dLxhA7Mc699USEgRKGm-cPJyztn9Xd1ReXHnh2d--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb6c05a4f4.mp4?token=bDp2YG-TSOBz8M-1cvGUFDTknWc-0eOaCMlafkFsX98XMts1SbPCTqPSzxxLJmEntDNy9SsoSXtIV_I7HFBSsDTkDq4JZ6wW_70JOnoCq7-0_UnKtJden_hhyZ1TXoXlgXYuVvnJtlxgp-XMJCc3mPgp7xiVMWlvrFDXMhRMIknqYkn_6XzJDjIyxbRZGfD4wMyCrcErjoFU5xq-LdUxq87WNzLdBJW81Mqq6-N6T6bf20yo10Y7YJI5Ts0PymR33nCvAa9pypoIOVh3ehtoNGzYRieqYQMLaPUkAqDuF0N-dLxhA7Mc699USEgRKGm-cPJyztn9Xd1ReXHnh2d--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از خونخواهی تا دلتنگی، حرف دل دوست‌داران ابر مرد تاریخ ایران به گزارش خبرنگار خبرفوری
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668884" target="_blank">📅 11:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668883">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5cafcd3a.mp4?token=Sx_G98-Rr_Gf88mJulUaDMozBpfgMbhtmshgBdkkwoJGNdymVsqabC9flkyAIqLS0lcoSkX-h9rFAX9rP4U8WyHA3TYCCveqEwIPbZrpg26ypeqahc2TyIHy6o_lm0lhsoG39KzVdo2_-cYPubMCGqaOnPsf3s3GMXCSWLvp6Bbl_gvkvimGKF8oc9ZqJMcYe4jxV-idXTTu8jv1qXey3NY6b6BGDvcQfTZLwMDcs7KWqE-oy1f5hRm63kYydUAriQ6lyXtXiMZdPj1zqMa2Sy8TbWFFoQWRGbkF1vGZBiibDzUzo9yMiCbDhW-d8VZxbsNHIqM5kwKCnI1scND74IWsgz8nHWcghI-pDGUeVabIWHydUNoSim-mbpzyjGgy1OrKo82kYO8RjTuEMFnIjsGvSxsC0Ix7vDMTAn1WGFLChr5L-gIlwTlmuGLz5sfknzOf08Qu9Z-anRq3kl00bEohDPNy6O-srMlEG9kkaqX9Oz58HCJ8F--SlSkCgSYmRLG7hLCJU6ZKt-ZOXL3dELu-2INeZHD6lDsZrAQVn3scEmsNaBQzzrHclYuoXh-5yduymkAPnzsDTIk6kUqCa0iLoJRImmSfqrhs2eYLqbpujh4jr46047G5WA45YV_H_WaBfNpyg9FsQZBeFIu-ONulXLXDtXytfSo9BXSlBsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5cafcd3a.mp4?token=Sx_G98-Rr_Gf88mJulUaDMozBpfgMbhtmshgBdkkwoJGNdymVsqabC9flkyAIqLS0lcoSkX-h9rFAX9rP4U8WyHA3TYCCveqEwIPbZrpg26ypeqahc2TyIHy6o_lm0lhsoG39KzVdo2_-cYPubMCGqaOnPsf3s3GMXCSWLvp6Bbl_gvkvimGKF8oc9ZqJMcYe4jxV-idXTTu8jv1qXey3NY6b6BGDvcQfTZLwMDcs7KWqE-oy1f5hRm63kYydUAriQ6lyXtXiMZdPj1zqMa2Sy8TbWFFoQWRGbkF1vGZBiibDzUzo9yMiCbDhW-d8VZxbsNHIqM5kwKCnI1scND74IWsgz8nHWcghI-pDGUeVabIWHydUNoSim-mbpzyjGgy1OrKo82kYO8RjTuEMFnIjsGvSxsC0Ix7vDMTAn1WGFLChr5L-gIlwTlmuGLz5sfknzOf08Qu9Z-anRq3kl00bEohDPNy6O-srMlEG9kkaqX9Oz58HCJ8F--SlSkCgSYmRLG7hLCJU6ZKt-ZOXL3dELu-2INeZHD6lDsZrAQVn3scEmsNaBQzzrHclYuoXh-5yduymkAPnzsDTIk6kUqCa0iLoJRImmSfqrhs2eYLqbpujh4jr46047G5WA45YV_H_WaBfNpyg9FsQZBeFIu-ONulXLXDtXytfSo9BXSlBsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاد دانشگاه صنعتی شریف: افزایش قیمت پلکانی برق، فقط قرص مسکن است/ اطمینان دارم مادامی که تا این حد سیستم انرژی دولتی باشد، چالش‌های این حوزه حل نمی‌شود/ رصد انرژی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668883" target="_blank">📅 10:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668882">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
سازمان راهداری: هموطنانی که برای زیارت و مراسم تشییع قائد شهید امت در مشهد مقدس حضور داشته و قصد بازگشت با اتوبوس دارند، بلیت برگشت را در اسرع وقت به صورت اینترنتی تهیه کنند
.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668882" target="_blank">📅 10:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668877">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWa5rHMdeXbNMEmIs9M3CpdUrf9b-JWmevR-aDfgy0DZvq7lqEkMDXTf024IFcBUMXruq_FqbxZAdIOzbDQafax7QJwxcNyfO-utexa9pZMfdGW_J38DgxzUumynC31umVi7zwP8gLAN6Rc2P73SxEcDh5xMeru0mVa0hsR1g4oa3Hb6CyiiRsWyLTiKaCSsntgC-BA7ZQeDSZNUheCY5peWftVGqSkFxCVmz522y0rcY2UL1IHlk_kzitxAwUsSiBUva7yyJEdnR_05YNK5YVydAuLCsDuI5MDjn-8J-8l0sJdddup_txIFm1Wr6fPdec137q5Vb8oI0qU-yKH-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5vSIqOfyyxli4_OEbhWjO8wVn6z5SlwYXB6YqmujRUSM-OY7zmkW08pPCnN1tRglqrbcjrhGHETl_Mpz9pUshc4Qz7ugoQaxvHMrTOUqKTe7s7fa077ox-BuKsaxx_AT5-CkhljVV4LBh9iuzdZNEWnsAjkLBQEB8MojDkuJ2yKMJofBstG0VZQlP-Y2uqNFhj5-V2hDthGwOD1LGL785Dmq7LMzgfxPcFBPMRs7z_OIGlSPVb9qeYlLwptA5ROsc8LI9H5-WrTSeS34-h30yYVIbOaz5PGmeidsJgIW-nPOYDAd5BSGzJEiSCJoQOPEM3QoIq73cDbqSh64jF9cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jD1gTV5SKU7qVlKkDO5XBzaQyxYq-c2u25pntdpgixOTWAV1KRWpYAgMFBkSkTo5VkEaGNgNaANGNj49O9cq2DoGuE_XUcWOM21oXpfJAsVQnxZKLiNKqU7K4jUcyY4IW6tLReuxHvvqGXXhAuK-eY4TeQzCeyGvU3M7vtkqunQYJUS4SSRrfmvHHQmLJrYGT4kAdCXr_dGE41ZdFxF_Fw2roY9ajD-mOnN8QG4jOMicT3PpU4MYCmxJsUEt1ddLlLHBJKpXw_kVnpztA7a1u9cDirL_WEZqzmZfOwO2oT1mx57Y2vuufB60_k5w9qELI51yJYqobIJ-L1imfLwU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XmsCmREbZpRi3gvJjQV4pc1SphNmMJNsV2pmB0Q_3O9hPZx8XhzTmcijNLTSH2l_Nac6W0GQo7Zvsgc-Zc34liol0foKQ6hD538KgFjzdcxNNnndwqLl_X_RZR5eOYfPRRdpAPh_3K9lARyc5yxzVmS2gUqeVrqvdOAKd1lderGeaKLRVXPRY8NsLBvzzLJEdC0IJxkYg315NxPNUeJfuh83xDRObAjDyx5vZt2N8KXokwrRShSYLpprg-Ss3POWjl7Ab3oon0_QkoHxGZXpe9TLRfK41aRJU6jLDrz6L0dPtIxRJxZDUO-StuUuKez485Auaorj_QmR1mBClApdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnX5_Z936DbQWa0M2P1n-s380GczLbp3hndMBXayqMPquvUHleFu_yuS_ZhvUYOHNNLteTO5hmM_fLayCs2UXavAiJjwYgTbp4MS-XdQ2sWP9ESGo-FWC6KEFVoHSYwQtLPc1XXZebcTCPF24v-p3GR162f9cU_eVD5tBm2HM1h_zdCaDBKoSOPP-6nlSHrIL4lMSGgChj0sTKakgqIMhVmUE0RAzBZlhArv-gczTmis4pmK6dwreyQNEYTRyaz75gYw9--MqDvOGJvx8Ez1Tx7VXOduBlE4ESFbg8lEjeu2XHocjCb7wIBL2UyDwn0mHBLxToJiL4XzzDxUwTC13w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گزارش تصویری خبرفوری از حضور اقشار مختلف مردم در مراسم تشییع رهبر آزادگان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668877" target="_blank">📅 10:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668876">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748fe9e2a4.mp4?token=YOXr0XU6wkApB58gc1igCeZNrAJTJEtqOlfZyTd5sOG2HDm_QUTg3KNcNcKAzIvwB7ty7UlEqNp8nF5WId4kc6COe5NPNz9W4OD5aLW5WzVA_-8x8dHmhCOfZ92GHLSyFbXvW_A7b6rLhF6gujWAeXyaCiDqZHxc7w-3l8UlV1KPIU65344cNr8O67awXwhXB471Vn2FfsZMV6EN6thkvQUFJgljXaNO7c4VW3VdHQqnQk0iK6lT5i13yRcZvgJCaIjvVpVVrRA0KdC1WwG21lLXIIbahgpMQWK2Sa2P6EE5xrbjq1-zi9oyllNvfsyX3NHw5NhkAp03KEIRBz6s5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748fe9e2a4.mp4?token=YOXr0XU6wkApB58gc1igCeZNrAJTJEtqOlfZyTd5sOG2HDm_QUTg3KNcNcKAzIvwB7ty7UlEqNp8nF5WId4kc6COe5NPNz9W4OD5aLW5WzVA_-8x8dHmhCOfZ92GHLSyFbXvW_A7b6rLhF6gujWAeXyaCiDqZHxc7w-3l8UlV1KPIU65344cNr8O67awXwhXB471Vn2FfsZMV6EN6thkvQUFJgljXaNO7c4VW3VdHQqnQk0iK6lT5i13yRcZvgJCaIjvVpVVrRA0KdC1WwG21lLXIIbahgpMQWK2Sa2P6EE5xrbjq1-zi9oyllNvfsyX3NHw5NhkAp03KEIRBz6s5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ ۱۱.۵ هزار نفر در اروپا بر اثر گرما
🔹
بیش از ۱۱۴۱۸ نفر بر اثر موج گرمای بی سابقه در اروپا به شرح زیر جان باختند؛  ۵۴۸۶ نفر در آلمان، ۳۱۶۱ نفر در فرانسه، ۱۲۲۲ نفر در بلژیک، ۱۰۲۹ نفر در اسپانیا، ۴۸۰ نفر در هلند، ۲۵ نفر در انگلیس، ۷ نفر در لهستان، ۵ نفر در ایتالیا و ۳ نفر در رومانی./راشاتودی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/668876" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52d862411b.mp4?token=g1VQLbVuXAAmQIJvjmLeOQCapX5u_Bo7Aqrm25XwtQmMqE94WbiLb-qvQwGV4wQAkxpfeZPn4tjjWoELKpYG6k56OLDZxt0Mw_xh4BeZWC4ShgbfkyR9ecwOudW2agW90LnGYyqaBy4CIfvQhMOiFLKR9CLe7Vo4zlXMW4IE2tJpdbioLX9NROp_XhCXH53ph-dEUpGseuMoLjs88LBYEIJrDt9_dnWL2Fh3ZUFb1n8UnorkfPmGnphDchtmfpP7fdiz3_iWbfai2pCzw_7gMEF_WwQ2OetaKb1Ahq12Xd4ay9e9LCCey83izH1jq3_O9tF4EuSeWgg44DJ1rlmO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52d862411b.mp4?token=g1VQLbVuXAAmQIJvjmLeOQCapX5u_Bo7Aqrm25XwtQmMqE94WbiLb-qvQwGV4wQAkxpfeZPn4tjjWoELKpYG6k56OLDZxt0Mw_xh4BeZWC4ShgbfkyR9ecwOudW2agW90LnGYyqaBy4CIfvQhMOiFLKR9CLe7Vo4zlXMW4IE2tJpdbioLX9NROp_XhCXH53ph-dEUpGseuMoLjs88LBYEIJrDt9_dnWL2Fh3ZUFb1n8UnorkfPmGnphDchtmfpP7fdiz3_iWbfai2pCzw_7gMEF_WwQ2OetaKb1Ahq12Xd4ay9e9LCCey83izH1jq3_O9tF4EuSeWgg44DJ1rlmO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وضعیت کویت پس از رسیدن موشک‌های ایرانی از دوربین های مدار بسته
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/668875" target="_blank">📅 10:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
پست بانک هم به بانک‌های فروش ارز اربعین اضافه شد.
🔹
العرببه: نخست‌وزیر قطر و عراقچی به‌طور تلفنی آخرین تحولات افزایش تنش بین آمریکا و ایران را بررسی کردند.
🔹
رئیس سازمان سینمایی کشور: مسیر تشییع رهبر شهید از تهران تا مشهد مستندسازی می‌شود/
ایسنا
🔹
شمار قربانیان زلزله ونزوئلا از ۳۸۰۰ نفر گذشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668874" target="_blank">📅 10:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
احضار سفیر انگلیس در تهران در پی اتهام‌زنی علیه ایران
🔹
وزارت امور خارجه در اعتراض به اتهام‌های مطرح‌شده از سوی مقام‌های انگلیسی علیه ایران، سفیر انگلیس در تهران را احضار کرد.
🔹
در این دیدار، ضمن ابلاغ اعتراض رسمی، از دولت انگلیس خواسته شد ضمن توقف میزبانی و حمایت از شبکه‌ها و افراد تروریست و خشونت‌طلب، از پشتیبانی همه‌جانبه از رژیم آپارتاید، نسل‌کش و تروریستی اسرائیل که بزرگترین تهدید امنیتی برای صلح و امنیت جهانی است دست بردارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/668873" target="_blank">📅 10:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63eebbf341.mp4?token=Q6c5uGVU-q14og-FfdLNT_9zJcSGJh0-ENWb846-2XGt49sOET4MvQTjsTQ3D-jHuW2WFrwme4a_SsPf9WMxi9I4nhN7tFUQX5F1S4sL9nOP40Aa_niMxPiBh67tNgVB1GfpP2YYVQzrdcBKoLsEZ5PsWrBir772IQy5Su8hSUaS2DpBMIf6TISv7vlg32B7w5EEyIdhKFbThFcIwXEVnXPjw2ZC104zNFPTz3zgutVni-7J_Ua9v5SYFXdH9AihtUw1JbpgJ0AFzzVeJb6p_53DDKMPojC8ctvIS2hFUh4DOnVX57l8vi6M_KD4E4TYZy5id3CJ-EiqlyhYjX_PqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63eebbf341.mp4?token=Q6c5uGVU-q14og-FfdLNT_9zJcSGJh0-ENWb846-2XGt49sOET4MvQTjsTQ3D-jHuW2WFrwme4a_SsPf9WMxi9I4nhN7tFUQX5F1S4sL9nOP40Aa_niMxPiBh67tNgVB1GfpP2YYVQzrdcBKoLsEZ5PsWrBir772IQy5Su8hSUaS2DpBMIf6TISv7vlg32B7w5EEyIdhKFbThFcIwXEVnXPjw2ZC104zNFPTz3zgutVni-7J_Ua9v5SYFXdH9AihtUw1JbpgJ0AFzzVeJb6p_53DDKMPojC8ctvIS2hFUh4DOnVX57l8vi6M_KD4E4TYZy5id3CJ-EiqlyhYjX_PqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از مشت تو تا آسمان...
از مشت تو آرام شروع شد...
بر مشتِ عاشقان نشست
در حرم‌ها چرخید
و سرانجام بر تابوتِ سبزِ شهادتت آرام گرفت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/668872" target="_blank">📅 10:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">خبرفوری
pinned «
♦️
حملات هوایی آمریکا به ایران ۱۴ شهید و ۷۸ مجروح بر جای گذاشت  وزارت بهداشت:
🔹
‌در حالی که آتش‌بس برقرار بود، آمریکا در روزهای ۱۷ و ۱۸ تیر ۱۴۰۵ پنج استان ایران را هدف حمله قرار داد؛ حملاتی که تاکنون ۱۴ شهید و ۷۸ مصدوم بر جای گذاشته است.
🇮🇷
✊
@AkhbareFori |…
»</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/668871" target="_blank">📅 10:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668870">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b40dc471a.mp4?token=W03VEdaw5FCMGB4rWwQnbLpM_zBmb6RkGtmPTIS3gSc0Kuulkru0mEquE3VQfJ9sUpMqLwRg0Qn2ibymKXvTBX6T0MWIweAaFnJBO7kGK3YBjICRaocePH2rSyyHR5n3IMQNUvo66txlZ49fSbhXqWomyWNw5YePewT7svGWcRQnKGQO0Ys3F2UHOlwN1zA7LWJM2y_MJG4nHWyCLSXg-k5bN1RhZ_9PkDN3ougePF533vzK8cjTAUjDCLbITRQqr6-8D4UVBZYSJvU5WZZRB_SMlA8-KAY-Pf-aiD2pzNZihBmxvIMyM6uc5KWYvRYxmGGH97cPSOS3KDt0pgF0lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b40dc471a.mp4?token=W03VEdaw5FCMGB4rWwQnbLpM_zBmb6RkGtmPTIS3gSc0Kuulkru0mEquE3VQfJ9sUpMqLwRg0Qn2ibymKXvTBX6T0MWIweAaFnJBO7kGK3YBjICRaocePH2rSyyHR5n3IMQNUvo66txlZ49fSbhXqWomyWNw5YePewT7svGWcRQnKGQO0Ys3F2UHOlwN1zA7LWJM2y_MJG4nHWyCLSXg-k5bN1RhZ_9PkDN3ougePF533vzK8cjTAUjDCLbITRQqr6-8D4UVBZYSJvU5WZZRB_SMlA8-KAY-Pf-aiD2pzNZihBmxvIMyM6uc5KWYvRYxmGGH97cPSOS3KDt0pgF0lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر عراقی در مراسم تشیبع امام شهید در مشهد: رهبر شهید با شهادت خود و خانواده‌اش اسلام و شیعه را ثابت کرد
🔹
آمریکا و اسرائیل هیچوقت نخواهند توانست اسلام و شیعه را حذف کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/668870" target="_blank">📅 10:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668869">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765487a4eb.mp4?token=OdiE94iRErEMXiOGZF422P2cBtkrJbadc7C370da5GxbNojbSpvo03Tj7QLrX4cBquuucD6pGRDoeWTG3MMiKOG0el6MH59D04KbkP9EgA3EGuhTiP4jQgwqM-j8o1BWQ2fEqsFFIEc9WIENS8tByfN9DOPzl8qPgPl_F9t0Gxb9eddPIvgFUt4-qmtKzHlpvXUagKAH9ukUWJQBMIP11ZIk_qELfeka_hb_u0EtKW_viUugoPwO0UFVdnBrVLgQnh_MeNekY5amgJLQxR_ACpn30aO8cMSQLpcUqB_LTmd_FqKMVwhWWxaYfK_ycfK1FG2LDJDE-UPWsRqd-TWvhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765487a4eb.mp4?token=OdiE94iRErEMXiOGZF422P2cBtkrJbadc7C370da5GxbNojbSpvo03Tj7QLrX4cBquuucD6pGRDoeWTG3MMiKOG0el6MH59D04KbkP9EgA3EGuhTiP4jQgwqM-j8o1BWQ2fEqsFFIEc9WIENS8tByfN9DOPzl8qPgPl_F9t0Gxb9eddPIvgFUt4-qmtKzHlpvXUagKAH9ukUWJQBMIP11ZIk_qELfeka_hb_u0EtKW_viUugoPwO0UFVdnBrVLgQnh_MeNekY5amgJLQxR_ACpn30aO8cMSQLpcUqB_LTmd_FqKMVwhWWxaYfK_ycfK1FG2LDJDE-UPWsRqd-TWvhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
غبارروبی مضجع شریف امام رضا(علیه‌السلام) با حضور رهبر شهید در سال ۷۰
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/668869" target="_blank">📅 10:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668868">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ss74xaqyHzR7-UFP1zpsZV6IQN2xd5ceKT1Q5PDFnyerf0TBNJz-zhlbahzABxcNUyMoxAepPYI70b8eDq13HTzf0JtED9kbQWofTfiCvpONJE_L9f6ANgvBc6yF0ct9WLcquSxxeazCAmpWp24CwFnlTnrTAYh-bGdkuFW2X-k4D3Wh402dYEekbuWNZoGD2wptaNw-lXXsUDMGfMP2oqkENJst1TCh5_HhskxqJwxwhS-6HnvsPfJdyY4ZsD6GV3_LuWPkOs0HmlIXo_ua2u6umBYU3fTqQ0Y9K_V-WTwDG00cWw5ZmV8NIjGCzgFD4ILWxOXkDz58ptGnisLtAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ما بر حق خود با اقتدار ایستاده‌ایم
رئیس جمهور در پی تجاوز نظامی شب گذشته آمریکا به ایران و نقض آتش بس در مطلبی در صفحه شخصی خود در شبکه اجتماعی ایکس، نوشت:
🔹
«رفتار دولت آمریکا در جام جهانی، نمونه کوچکی از همان الگویی است که در سیاست خارجی دنبال کرده است؛ زیر پا گذاشتن قوانین، زورگویی، ایجاد مزاحمت برای دیگران و تقلب کردن. این تاکتیک آنها برای MAGA است.
🔹
با ایران نمی‌توانید اینگونه بازی کنید. ما بر حق خود با اقتدار ایستاده‌ایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/668868" target="_blank">📅 10:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
سردار کرمی: سپاه و ارتش نگذاشتند تروریست‌ها قدم از قدم بردارند
فرمانده نیروی زمینی سپاه:
🔹
دشمن آمریکایی - اسرائیلی گروهک‌های تروریستی را در جنوب شرق و شمال‌غرب ایران برای حمله به ایران کاملا آماده کرده بود.
🔹
سپاه و ارتش دوشادوش هم در اقدامی پیش‌دستانه مواضع این گروهک‌ها را درهم کوبیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/668864" target="_blank">📅 10:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqZwJ1dB8_oFklLN_aB7AaS0Qm0144zxZFm22XlmKu7IO6108yoaQoNVq1d8bFdpGQcCnu13MP7oO81gipDiYEIKHoMQ0iV5K8UNuMw-ss8OEbheAFGBvTsaTsB-_4u1vnLA-CLMB-PBwzM6GOdBaYr8Fd3QCOslBZujUE4Mxhgy7yQc_lLy-lmyH3l602pUngjj3jCm5vJDUHgVRju4TUHOoFV-BQ0VJZihw3sj34k-w7F1ccFRKARiF0tFyBalqWsKsdN6DU7PUx6Fju72ysKBw-V5FKWecjEVTvCrIWcaYrku0dWBsyugj03-RQ4EboKO4-aYSLqo7V9Z0uvD4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد در مشهد: به سر بریده ترامپ نیاز فوری داریم
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/668863" target="_blank">📅 10:12 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
