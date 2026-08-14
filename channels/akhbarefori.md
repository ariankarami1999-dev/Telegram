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
<img src="https://cdn4.telesco.pe/file/jqRLReb-Sf6T5r-cVPeX-o4MqvxanT6ox0uT7__ptx-MBmPzLmQJYZYVdbH251QaI-DInTg_DnxERcYOyWyRm9lw-8_8gR8PJB0mW0N6KqspXiXYdVbEQnzIjnnMndO9qqFJn0EG0ae1SWv6s6w-sAhLuvLHX5VaYTTbAHjKYUO9YnyKSuAfJRQO3puFWrWOpNvphXwlDFez9eCuLQi4URgANsPmEKsbDA3VX-LA1lZ6dtBzwEuKeoKlLPVwRaoxh5rxBzH-NXgTDIX8yqegHaIkoocn56cG0IbDQTRKD8NjOrJ5SCnq4scN7f2twXHnitmAnerJfoT2JIqWw3q79A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.18M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 22:55:34</div>
<hr>

<div class="tg-post" id="msg-681242">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
توضیح دکتر پزشکیان درباره گرانی‌های اخیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/681242" target="_blank">📅 22:52 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681241">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812f3d2ee5.mp4?token=KtLyfj7FtBLvl35yZQDhwBZXVL1cdkLNfgoG0L4rsMpoJV0oYBttFCcQVlZIOqBxpGY3_QCVArkeWu9XjnbTPTojVmIKXLH3wRLNHOkqpPUWy4faehlb98z_nlN6UsyaRjuHLmCUuT1DWFyesiU3iZF6htCVQX_ZO_wuX_dpdZYVv1UwoHBkUdQLC2XVOqEVJrvLI4TwJPMOVMPSf6-_nfixhUmm4uAiboY6S_JZomPbPxgcWafVH34EJuwyFzgOULk-rkvzm0YoDhMhVvxQzSdsYX6PaxXmrYQA-DSxWB2TUVFQlGixc4g2nclN7mowvqVpdY6swC1WoQ080Nzzag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812f3d2ee5.mp4?token=KtLyfj7FtBLvl35yZQDhwBZXVL1cdkLNfgoG0L4rsMpoJV0oYBttFCcQVlZIOqBxpGY3_QCVArkeWu9XjnbTPTojVmIKXLH3wRLNHOkqpPUWy4faehlb98z_nlN6UsyaRjuHLmCUuT1DWFyesiU3iZF6htCVQX_ZO_wuX_dpdZYVv1UwoHBkUdQLC2XVOqEVJrvLI4TwJPMOVMPSf6-_nfixhUmm4uAiboY6S_JZomPbPxgcWafVH34EJuwyFzgOULk-rkvzm0YoDhMhVvxQzSdsYX6PaxXmrYQA-DSxWB2TUVFQlGixc4g2nclN7mowvqVpdY6swC1WoQ080Nzzag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: با تمام وجود از نیروهای مسلح قدردانی می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/akhbarefori/681241" target="_blank">📅 22:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681240">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOaY8gOwDL2jWzb_mNDTmlsURjhzwdE3EHR3mq8bgPJGv0i1Nvj02sDZKYxPDkuNabIpErrD1aq6YXSp3orG5Yvob729F6cgm33UUaxBEQ0V-Plb-PVF7YelA8Sg1E8AhUYFB3Ov4DbvnNY47XCcHg0XtAK2HitwceirPV7wHnWhPx6eVLrtB3PVxuH6qjHla_2FG2vs-IY_1uDYxf_85XjCaakOlAY8882Y_7yvtIYRMVJIJN2gFBUy80W6qjEhQ_Nb2kOE5CGRHRM8BKsYazyv-TKhlZgCdrcRLYnNqfYE0ZDweevKiJKEKinsUmaowaouu8PLxKpySJzCMfV6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خورشیدگرفتگی ۱۲ اوت ۲۰۲۶ در اروپا موجب جزر سریع و شدید اقیانوس شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/akhbarefori/681240" target="_blank">📅 22:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681239">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba1ee16a57.mp4?token=mLWkkD2-qVfygtRIYJj12bhq37IiexTzNNTQjaVJZ2vWD6b0BhX8k5rjDDJoleecATiBKOZ6HOETZUZelOzIGMcRHNklJCLhdC4scMD20LnOUVdCygl1NlTliZykrZ8Vcldfho1VOtDJSdY_Sz-7Q3FZydWSWsehMM1QPFabo6jlc0JEI5S0Gm6eC3Jv-QrMQLEjw8otrOk1zEfyU8YkjGFJi8cZVyHMBHFsZFzYSmQVS1XWRu8fQdEoh0PUPfxXTvAu59ydncQ8Zcu99XoM90UJ6j7lWMmP_ti7fTjUE9BRz0L2i37w4fOryIaGahzH8TUGUtVbiM4VABTuHyPQIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba1ee16a57.mp4?token=mLWkkD2-qVfygtRIYJj12bhq37IiexTzNNTQjaVJZ2vWD6b0BhX8k5rjDDJoleecATiBKOZ6HOETZUZelOzIGMcRHNklJCLhdC4scMD20LnOUVdCygl1NlTliZykrZ8Vcldfho1VOtDJSdY_Sz-7Q3FZydWSWsehMM1QPFabo6jlc0JEI5S0Gm6eC3Jv-QrMQLEjw8otrOk1zEfyU8YkjGFJi8cZVyHMBHFsZFzYSmQVS1XWRu8fQdEoh0PUPfxXTvAu59ydncQ8Zcu99XoM90UJ6j7lWMmP_ti7fTjUE9BRz0L2i37w4fOryIaGahzH8TUGUtVbiM4VABTuHyPQIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه آتش‌بس با رضایت نیروهای مسلح انجام شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/681239" target="_blank">📅 22:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681238">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: تجمع نیروهای سعودی در المخا را منهدم کردیم
یحیی سریع:
🔹
نیروهای مسلح با کمک خداوند موفق به هدف‌قراردادن تجمع نیروها و سلاح‌های متعلق به دشمن سعودی و همچنین قایق‌های جنگی تحت‌کنترل ابزارها و مزدوران آن‌ها در منطقۀ المخا شدند. این عملیات با استفاده از تعداد زیادی موشک بالستیک انجام شد و به‌لطف خداوند، اصابت‌ها دقیق بود.
🔹
این عملیات منجر به تخریب قایق‌ها و سلاح‌ها و کشته و زخمی‌شدن ده‌ها نفر از نیروهای دشمن سعودی شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/akhbarefori/681238" target="_blank">📅 22:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681237">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ddfa3587d.mp4?token=VX1oTkCWz-THWwF1NDFl-0me6pqhc-0FKp_3EC5Omy0YsLQESh7QV5zwcFp90mNH-osKMJ3SsEpmjgYJxcuxf5liT5kXrAgcR2Ha3hCZIMNUjm19-GCdmbj0V-1h91Ifm9nVlBhCA0WbxMQAQ3N-8Y1F5RnZDkmqa3qv0ryWTPuRtwc1Qit_Rpuwx4GSICFwhDwrDIhHNRfepTrk4qc1dLp7YANPZKSp30VTeoiJ5aSLwcADwk1Z8eD-mB4DM0xxC2AUp8ev2tLgOr51oEKNCpfgRiVNQ6SXBHXyzZMZCeYj1xtl1X1q6mfc_VDaSh1TbRUiIZN0ws5rhLD8zlONWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ddfa3587d.mp4?token=VX1oTkCWz-THWwF1NDFl-0me6pqhc-0FKp_3EC5Omy0YsLQESh7QV5zwcFp90mNH-osKMJ3SsEpmjgYJxcuxf5liT5kXrAgcR2Ha3hCZIMNUjm19-GCdmbj0V-1h91Ifm9nVlBhCA0WbxMQAQ3N-8Y1F5RnZDkmqa3qv0ryWTPuRtwc1Qit_Rpuwx4GSICFwhDwrDIhHNRfepTrk4qc1dLp7YANPZKSp30VTeoiJ5aSLwcADwk1Z8eD-mB4DM0xxC2AUp8ev2tLgOr51oEKNCpfgRiVNQ6SXBHXyzZMZCeYj1xtl1X1q6mfc_VDaSh1TbRUiIZN0ws5rhLD8zlONWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: تفاهم‌نامه آتش‌بس با رضایت نیروهای مسلح انجام شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/681237" target="_blank">📅 22:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681236">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgohRrKuUrndTSk1HbOURzkbdWdee-Ml93LqJJaJscpVJIik6t3VQrk00CdNPAEIYbOY-3zTJpc8OHPloU3oMpWGH7tLvQ-4KPwjL22IoyTM3Y3vx4Z1J7zvmaD3FJI3MPt0Hwr7EasK46jZecFaK4R9XFi8YJxNp_M04jH0yi9QuL3c-k6v7fj65TwJA8L3uPntP8SodwRHG7JPqPapsofuWrQBYuia5PwquKF5rMrsVrq_zf4m3tm4yBRR0w3x8mbvIkrpTrMKBvLuKU-v5OvOew3AZDDrqBlWn8sfdl0Z8_cGJ536s6lDNSNAto7xMpusgU9cdndjwnKtRezbnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر در پایان روز اول از هفته اول با صدرنشینی استقلال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/akhbarefori/681236" target="_blank">📅 22:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681235">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aec64a1c85.mp4?token=MzUTNDnQ3GWyRGr9FWdKbdMDpsGMTaNSYtkG3gyjDNT1tTP-gTPVVqTRD45b5xzDlNfROoskgSDKgjIq6EJIxaEo4qizL0oReXwD--rFzn_kJB26F2iZ5g2hrLCfQu1nSUSF2E_L5pIwfU3krq0BptPwMf4AVD-bFvre-6dBD_fhudARyXidJ50gmuKqpDfvGQ-yHWOAKDf289oVvYDusuMX2uZ2O4cDg6G_BE3qETe8mebrcLt14j8qjgvddMohpBZg4yCfMoDyER6VtqmCE6YN4G7sI91DkF20oZKxwAaJ4qskkWXtjTJIDoZw7tMgsKe3GWs3-vK73gfiG72ECg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aec64a1c85.mp4?token=MzUTNDnQ3GWyRGr9FWdKbdMDpsGMTaNSYtkG3gyjDNT1tTP-gTPVVqTRD45b5xzDlNfROoskgSDKgjIq6EJIxaEo4qizL0oReXwD--rFzn_kJB26F2iZ5g2hrLCfQu1nSUSF2E_L5pIwfU3krq0BptPwMf4AVD-bFvre-6dBD_fhudARyXidJ50gmuKqpDfvGQ-yHWOAKDf289oVvYDusuMX2uZ2O4cDg6G_BE3qETe8mebrcLt14j8qjgvddMohpBZg4yCfMoDyER6VtqmCE6YN4G7sI91DkF20oZKxwAaJ4qskkWXtjTJIDoZw7tMgsKe3GWs3-vK73gfiG72ECg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خورشیدگرفتگی ۱۲ اوت ۲۰۲۶ در اروپا موجب جزر سریع و شدید اقیانوس شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/681235" target="_blank">📅 22:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681234">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
فرماندار قشم: آلودگی نفتی سواحل جزیره قشم تحت کنترل است
🔹
ارتش یمن: مواضع و شناورهای نیروهای سعودی در المخا را هدف قرار دادیم
🔹
وزیر فرهنگ: قدردانی دبیرکل حزب‌الله از تفاهم‌نامه اسلام‌آباد، نشان از هماهنگی دیپلماسی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/681234" target="_blank">📅 22:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681233">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOgzx8UTP0QNoCfYweErOPnAsVo_tm_4pKXx2Cl5oVMx7WGMkwASG_b9Q76Q8Zg970fOw8sJSCBI1FaAjHzlNS7h-ajNA4RwMnBoWsQEwP9Z20Z1yesZn6uiNpa2LN4R72n8tEMG0ioWyDD2_7OZqhWnklCTCjJywJIq21rL5CTpqr1bsHNeG_1Sm3iDZ86AZMNHsRouPJsuqFuq9P3e7Gjc6VLfM-dFhrJxMeKXZ-SidZvhiKKG_w1HL31a9Cv_zNvONQwUSDt19CQ3zfr7p6oZpNaXKI7oY9OAx53JsY6pOao12KWkUqPrRoejxyufzgVTNJYNOoYKqQv6Orafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
طلا؛ یکی از پربازده‌ترین دارایی‌های یک سال اخیر
افزایش قیمت طلا در یک سال گذشته باعث شده این بازار بار دیگر مورد توجه سرمایه‌گذاران قرار بگیرد. بازاری که علاوه بر رشد قیمت طلای جهانی، از تحولات نرخ ارز و شرایط اقتصادی داخل کشور نیز تأثیر می‌پذیرد.
در این میان، صندوق‌های سرمایه‌گذاری طلا نیز توانسته‌اند بازدهی قابل‌توجهی ثبت کنند و در برخی موارد، عملکردی بالاتر از انواع سکه و ارز داشته باشند.
این صندوق‌ها امکان سرمایه‌گذاری غیرمستقیم در بازار طلا را فراهم می‌کنند و برخلاف خرید طلای فیزیکی، دغدغه‌هایی مانند نگهداری، سرقت یا اصالت طلا را به همراه ندارند.
صندوق «جام طلا»
نیز یکی از صندوق‌های فعال این حوزه است که با سرمایه‌گذاری در ابزارهای مبتنی بر طلا، امکان حضور در این بازار را از طریق بورس فراهم کرده است. مسیری شفاف‌تر و کم‌دردسرتر برای افرادی که تمایلی به نگهداری طلای فیزیکی ندارند.
📊
تصویر بالا، بازدهی یک‌سال اخیر صندوق‌های طلا، انواع سکه و ارز را در کنار یکدیگر نشان می‌دهد. (
بررسی بیشتر : کلیک کنید
)
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/681233" target="_blank">📅 22:27 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681232">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9zRtbTdllM8_7kOePhktjF7xvieKAsZecLC3URDjBKUMNXWRH0aWyfuTv2BxrywEha9Xrybu7LWHrtGRJeeomZ2rG3BF3coQwzTeFO0By_gzKbxCwUOBLo8_ahF68V85i278iHjOrSiWiftoWa4IdozKNPYTApWJ4ZTE10SqAc-isTXzbXgyubjTFDi5bXZ7F1-wVjCC-lZ1AxUd-5lsvJaYow07-QMHuIhEZeiLfa29h1_5MX-uN7YzneY3OVp6GmUi3KT8HXovsdZpZVV1bFrX_UPWM4DeighAzG3nX-2K5la-vyvvqiCSqGwf4X0i1g44S2z3Um_SsKXTcrvQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: دختران وزنه‌بردار ایران با نخستین نایب قهرمانی آسیا، یک «اولین» ارزشمند را به نام خود ثبت کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/681232" target="_blank">📅 22:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
باراک راوید، خبرنگار آکسیوس: نتانیاهو بر اساس نظرسنجی‌ها در انتخابات پیروز نخواهد شد و همچنین ترامپ حمایت خاصی از او نمی‌کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/akhbarefori/681231" target="_blank">📅 22:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
کانال ۱۳ اسرائیل: آمریکا چند هفته پیش درخواست اسرائیل برای بمباران اهداف ترکیه در سوریه را رد کرد
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/681230" target="_blank">📅 22:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4d9eb2a5.mp4?token=WRDpKZ0IX3V0_s1KyJwzXif5FhgwLLg6yUC4BklKxfxOuVFrN6WT_CwyKhwmGMobF_DpqHuu0C_2W9e5bhvGuC0nlg_gMB1c6YZG7O8LBp2MlYBaulHtc7EWENS_352EQmG0zH1db8wTX3EmTpKEJs2GLqwX6g9-SnbyGMsjU8KigohzFMvjYU7dpqIoUdsakVRDH6apzUCXietJXxfWUDPSPAbMxD5QKroweln_YWwRSDBfmR7iZAPWu78CpfAyf07EzOYcycGW0s9DpDHLJ3sbpPNqKfaYbzSj8JNtqfhVTDgAHpMYlnWtNkm03tiYntaf2GsZzGPJLBk5AiKDjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4d9eb2a5.mp4?token=WRDpKZ0IX3V0_s1KyJwzXif5FhgwLLg6yUC4BklKxfxOuVFrN6WT_CwyKhwmGMobF_DpqHuu0C_2W9e5bhvGuC0nlg_gMB1c6YZG7O8LBp2MlYBaulHtc7EWENS_352EQmG0zH1db8wTX3EmTpKEJs2GLqwX6g9-SnbyGMsjU8KigohzFMvjYU7dpqIoUdsakVRDH6apzUCXietJXxfWUDPSPAbMxD5QKroweln_YWwRSDBfmR7iZAPWu78CpfAyf07EzOYcycGW0s9DpDHLJ3sbpPNqKfaYbzSj8JNtqfhVTDgAHpMYlnWtNkm03tiYntaf2GsZzGPJLBk5AiKDjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات پینگ‌پنگ باز هم از راه رسید
🤖
🏓
🔹
واکنش زیر ۲۰۰ میلی‌ثانیه؛ هوش مصنوعی حالا پشت میز پینگ‌پنگ هم حریف می‌طلبد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/681229" target="_blank">📅 21:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GjCrF04ymYYTufSC7_n8MbVVJ2J9WbeXSEkeUTneoG7s_qqo2euKjBtg9cYjwVZ-_RFxT7aVHkY5HJgddErl_KLTTcalkIUYHcH8Dc0ABlq4YuLUXDu1cms5GnPbIHpMWoOM20wLNudqVbIJMaediGVVG5-zT5ZF1Vz_oWv2nxaXEAIb0DUlcfmFP_CGV6ZHpAu6m5WoGBEsuFCCzaadCWmWufmm0CsJ-vQfn1ijDmSKKTwY4iedioGhAkc-AR_1yeg3HjCta3hz5ua-JcLE5BTE_XF5tA24oNVwRSPdrV1cqAxF3rsDGDT9Fu_gDattXM9pRWcODN1Q3UCPfJFdmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی تماشایی از ورزشگاه ترومسو؛ ورزشگاهی در شمال نروژ
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/681228" target="_blank">📅 21:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/693cd8d045.mp4?token=Ik5wOS71hjdOKuVLLbgzRS_kNWb7N4-TgynEcbZg0KJDmwPbMmiczZQidfS69U4KiDSFH-cBdJoiBllAJSZYH9jV5TbQiJs0-rjyy3-j6OzDd7bTIH4q8eeH1-S9paaxaPEpA16VZ8uCsGCR-MLQ5euKdvWv8d6BAIT-V6VZMKGzSOjuAA6wZu3AfDN6hQUsiDS5gT92jXOI3i1FeYFIP6l4c1YxJJJycIFb2I3fwJQvPPiL8rh3Yogq-m1xjQjUm1oPY77JkYCbrarT8BmSktjZF1evcQDkYXZmo7q0xDZwt5boxWKwvlpF1KonS1HcPztyTeSEIqVVsrZSshWnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/693cd8d045.mp4?token=Ik5wOS71hjdOKuVLLbgzRS_kNWb7N4-TgynEcbZg0KJDmwPbMmiczZQidfS69U4KiDSFH-cBdJoiBllAJSZYH9jV5TbQiJs0-rjyy3-j6OzDd7bTIH4q8eeH1-S9paaxaPEpA16VZ8uCsGCR-MLQ5euKdvWv8d6BAIT-V6VZMKGzSOjuAA6wZu3AfDN6hQUsiDS5gT92jXOI3i1FeYFIP6l4c1YxJJJycIFb2I3fwJQvPPiL8rh3Yogq-m1xjQjUm1oPY77JkYCbrarT8BmSktjZF1evcQDkYXZmo7q0xDZwt5boxWKwvlpF1KonS1HcPztyTeSEIqVVsrZSshWnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی عظیم در هتل۱۳ طبقه در ومبلی در لندن
🔹
گفته می‌شود این هتل محل اسکان
پناهجویان
بوده و فقط چند قدم دورتر از ورزشگاه ومبلی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/681227" target="_blank">📅 21:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/935af1a1b9.mp4?token=M0nhpCfst1eSeP-UF-IvCYvH10bPCO-cXSg_qKoQAYOHk71PGnr_OkkBdrg3uqyt3JIoWd1UYhkMLhmypKESs64YQ_Qy6zMNEPbcAxp9zGOkk2uVL0moag1FzczH2h1oULvYSE3g6d_w1eou6nEA_rjhC2nadJM61hoHOu1udGAgbqsMII1lKcWmy9HSV5qI5deGnz5EdGyQOrEoyM5q_MYiD8qhP8zOb7BVEnQiD6w-VwxQxHjYhHWd0djS7TnvYJHvy9IDLnpc6Oz1uV_xWXiV5zL8w_8w1RI4NlMobkCi4OO3fJZg06vUW2OelUtmLw6F2mOaF3U-sWEcnKyh3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/935af1a1b9.mp4?token=M0nhpCfst1eSeP-UF-IvCYvH10bPCO-cXSg_qKoQAYOHk71PGnr_OkkBdrg3uqyt3JIoWd1UYhkMLhmypKESs64YQ_Qy6zMNEPbcAxp9zGOkk2uVL0moag1FzczH2h1oULvYSE3g6d_w1eou6nEA_rjhC2nadJM61hoHOu1udGAgbqsMII1lKcWmy9HSV5qI5deGnz5EdGyQOrEoyM5q_MYiD8qhP8zOb7BVEnQiD6w-VwxQxHjYhHWd0djS7TnvYJHvy9IDLnpc6Oz1uV_xWXiV5zL8w_8w1RI4NlMobkCi4OO3fJZg06vUW2OelUtmLw6F2mOaF3U-sWEcnKyh3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارگر ایرانی در عسلویه، تکه‌ای یخ را به سر و صورت خود می‌مالد تا با گرمای طاقت‌فرسا ۵۰درجه مقابله کند و چرخ تولید انرژی کشور را بچرخاند و سهم خود را در آبادانی وطن ادا کند
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/681226" target="_blank">📅 21:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681223">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a7WqyKEWdoql3WIDgYquFKwxiEdnYBMJZNluv-HmAXQbtxjRw_UmghfTSGg12w7-9wOELnEvwNERrXV4elo4yY3Ri5qXXg_iHFhHii-5DV8aAWrGbxIOIiR_Ayx2SO6Eaco652htYUf1dH-0C1a7paZaINyNO6sAjnjccYkyIZYv0migDJGzvLjnNQ1TuAzku-KUkzqvqplTj5Xti5rQQomGBju9aHxz1PT1EtopbFxxzfzrfL3aQhYS8uJe97xlkdboyTSLW4DKTkt8rIEsqIlOaJHa8eAnXQVYmuU-BCMax0FsS3u2pXPzzdHDGqGbYWbBd4csEDpn_eHi4YWbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y3xG9fUxb2w7ZkIzsfY7-nOZ1bCoJ8Tpv5UZqXggrraFMNKKsV4o6UXnT-BwMRAozJ1j8wYDkE1xhhCsYXWnW905cHkFwBzq_W_lBK4zd5e0BgPPr2bKfiU3uHDIai70NXgVe5agEf8FQi8LsyejWEo0k3zYVxwK93h3hHj_Bf_n1o-ncc9qedO6rHCKOij7ekjMbGHl5qUSXCwxtVl4kd6RPC00aCrWDzaVwesw3baNhMMIYbuU89DlINA88TGFo0X61YrB6kfK68TVn2C7dHGy2wvg-kfw8jNoULnIf0UlU4P2npQF9AF8ze8CVrcfKMHAbbqpDEKps2LMnvesKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyJwDvlIRqKQRfweWAaGJzWAZBGw0Puy8mvn8QsLKFjhUNcHgCbOE7XeiM8RpWufE9ns3oRq9Nvyusn8AwICZbbOiMbw-YYFQDm9Ywqi75MygUvrUaLWMSWWPQGVCOStMUWXluZgj4HUAc7UZoKWFUaysi9dKW4Hjpza91VhEqMuiRZcv03YD29PnPk62QvhZTaIOHbhMpH39tpqogFODrdCU4Yit_7f16_WbhBVwcXrb3sCap-TPsKVu2N_9lkzQywNffPjdaKlB9FRGQUz04PAsUVj_VM0xcOW1SD_-pCHmmTx7VRUf4PIWFzAlFJVDaoXvyYyicHkARgXRdSDNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جنگ میم‌ها بین روسیه و اوکراین؛ از «یخ‌زدگی» تا «گرم‌شدن با آتش پالایشگاه‌ها»
🔹
روسیه با تصویر پهپادهای شاهد، اوکراین را به «زمستانی سرد» تهدید کرد و کی‌یف در پاسخ، تصویر پالایشگاه روسی در حال سوختن را منتشر کرد: «با آتش پالایشگاه‌های روسیه گرم می‌شویم!»
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/681223" target="_blank">📅 21:31 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681221">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b7dae5bd6.mp4?token=M7OH0XNU69pkonLr-umtNRJ6j7Cl79PVLTdEv0pYznMX9c865s8yHhk8VESoOZ0111srHzxvVxzTem2Vcu8ibb_VS-MxCg4pCfQAqQ0JxeNqJ7HkaMfvhNqF4qK5SY6sEKn1B4sOJspZUUhHceQK1kwk7zp5rjHLiOXzkmIDA1oQxAOUNK1VUivVafWFirfkJT3U06pnaEhCeXxlzEyjRofVtdMcFBm0LvYeRxsC6RgFfaCfwHIt5EUwgyrMrjlsZXc4TUr2Ckqu6fb8rmteb_Ln5UvsPAzGwtK-opjyH4bT74WbswTAVTYBVtASajJsXIVfN1e1AzOou-hwb6sYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b7dae5bd6.mp4?token=M7OH0XNU69pkonLr-umtNRJ6j7Cl79PVLTdEv0pYznMX9c865s8yHhk8VESoOZ0111srHzxvVxzTem2Vcu8ibb_VS-MxCg4pCfQAqQ0JxeNqJ7HkaMfvhNqF4qK5SY6sEKn1B4sOJspZUUhHceQK1kwk7zp5rjHLiOXzkmIDA1oQxAOUNK1VUivVafWFirfkJT3U06pnaEhCeXxlzEyjRofVtdMcFBm0LvYeRxsC6RgFfaCfwHIt5EUwgyrMrjlsZXc4TUr2Ckqu6fb8rmteb_Ln5UvsPAzGwtK-opjyH4bT74WbswTAVTYBVtASajJsXIVfN1e1AzOou-hwb6sYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم برای استقلال توسط اسلامی
🔹
استقلال ۳ -  ۰ مس شهربابک
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/681221" target="_blank">📅 21:24 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681219">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb9763db17.mp4?token=JGaqLNxQFGYaUAXoTibD_ByofuBJTwSEGTRe_Dkr0vUaebLin2o0L8Mx_tmkViOXbtFl0PcpRLWnkfZYpzC4qxScMKu3-73Kd7rWx4NzoWIa0v0o8MMGLW8qayBxQBLtUTC3n6UiSVmEBwhqynm7aDgHp4m2_axnjM1pxJ0lrNUdJjbIAlBR3_OUoFjj6xr2lET9kwLblyi7peXeB1VMPFm388cVB0TLHClLDZd0b7Yj0SSqjufxqx-njwyZ_LL7nwoc-Ln646Bsdsg10ITfJI0J2WOHZc5CZsR5KUtTLcJZq1Hm2u5_ouG3dJTM420RZhiVjkwLlx82S017Ry76zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb9763db17.mp4?token=JGaqLNxQFGYaUAXoTibD_ByofuBJTwSEGTRe_Dkr0vUaebLin2o0L8Mx_tmkViOXbtFl0PcpRLWnkfZYpzC4qxScMKu3-73Kd7rWx4NzoWIa0v0o8MMGLW8qayBxQBLtUTC3n6UiSVmEBwhqynm7aDgHp4m2_axnjM1pxJ0lrNUdJjbIAlBR3_OUoFjj6xr2lET9kwLblyi7peXeB1VMPFm388cVB0TLHClLDZd0b7Yj0SSqjufxqx-njwyZ_LL7nwoc-Ln646Bsdsg10ITfJI0J2WOHZc5CZsR5KUtTLcJZq1Hm2u5_ouG3dJTM420RZhiVjkwLlx82S017Ry76zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم استقلال توسط سعید سحرخیزان در دقیقه ۵۵
🔹
استقلال ۲ - مس شهربابک ۰
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681219" target="_blank">📅 21:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681215">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Opq4Ogmru1FZNUWX0Jw5cW295D19caJPk7KN-A7bhN9k-DCFqYGIUU4aF2qEx-ZiVQ5EQm1gNn0BKS7pEjZ-PBN1Gc3Y6uj2Ujx0UWZun94R5zUocLykFtu1_cm2p-D4L-iePxqKcVZtf13MQ8py6eNdkBqSQlfPJPHcdF3-zsMAJDaPJlVkAFUITHIIMpwVzPJD5P-rv5BPKXZWOiTSJOz0B-ifv-bJRanOZN4AkIuKAbsi0-rrRwu1WHtZnaMeQa7xR0V0Hd4r93hKb3p0E4H6pUK2LJ-yn-9frYwtmYyJjqvFLPmfKbnleKxQF_wSRJVAMIKgn8wGnHdSRonc3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyCTCf80ebHpQyQ1eTAoXpxVVeIwCSZzCrhMaPnOQiFKiTR-6MFQHdaqaN7dRvYU4oAaod7_D0I_qBDZRS6TpPaxkwkg6IeVfM4fue9QfLmLtS-WGf5RqotcKuGd1wOHAB-T7X45ghv6vXEra9VlFPsSuDdWGIDM4NQ1iOcJZk6cT1sVQ5XRDZqVV0vbmd2al3-fhrjbVlG_3pnF2_YHAGGy8UXGhpsqxNDR3_xLSu_QTd85J46zYdWSywsl_UlHhJ_ydI9tJzesmmieqxG_dMYdYoJzH8Y-HmKbzQPnf7AKmHNNjWYEXUih2e_gcAvayaagXv2cKhuIlDUwHaZVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmSfRRc8PeNHuddS3R1K4f8wzSaDU1PIMtBRrUPoJjxs_HMDEvYdACAhe7J0m5fOuRowW_BJI9meDPjGIWlE1qArDUBcQIE_yVmNwsea-oeUSs-rfp6znR5e2QezcpXK9g1iQmBrDLSD-FmgUyuiZvcm852pjNNgdG9fbbrYjYOsha_eLjnONjVPxxJzBeUrsgPN-Vl2HZHSL29U8EbGD4HawTLg8LQuw18pAoMVE5aTsPdHAVwN71QdPgj2z9F6h2zX11yPA6NTFODFD4TuTWM4bjcxPTd3nK2HT7ohkI0Y3o_hi3NWyu-VDmX1fniOcATqcD4wD3HHReEtYVMI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/faL5b03DUnnClor_Pj575lJ6cuKKbBGuGndIG17p6GxqaCDuuHe8q0fPKun1OCmoHKZSP2dH-rMaiwVDwv5XRanQwLqDXTje88qBuTYoviji_w4SNzHRp_HZToeIio1LMJOOW6CLUhQ-qe2TvNDlHGCL9YVsANXQfrPzPALqHQZGBXoaukcno1J_BoV4E7BwrQDFkJgJBp3hkkoEsf_V96UO9jJaeC557z6BwN4ZFLg9NXaUoppf-xOHC1yBIAmfj_y8U7ChDZy5iCdw-LRmFUhMM8HSG3xz8ZdntX5DKvcSvA6L6kW9NwJ_f-HaeXjvID_NGCg9u_RK_chfXot5CA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
اشتباهات رایج در مصرف دانه‌ها که ممکن است تمام خواص آن‌ها را از بین ببرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/681215" target="_blank">📅 21:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681214">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cafdd78c9b.mp4?token=NWM6gPE97ZzQ6LpubHxyZ_HqLRnHgmwZgWZtyWnZ-wTt_PgyxTUJTfwPo5sMWyaZcnLw7XukJMQMkFGKjxInbnYtih_69Igc0Pdx0lSYZpM4Oz88KKyyF4MhTky7E-HYpJUquoGt9IESrXskgg6QITCpPkSiAjwk0sGhf95biRYiBXhb6Z8PVMPsWbxutEs9qLM4TIm2VbI-CxJCXL8K4R_zstSY0zNp-wBfc-4UbhJIY-gyG3uWVJJI4Sh82tC1bRcsBdn_yi4O8dB9PDP1hjW5IXY7svX6_-IYm7wDGIx3dO_DSkw11FLSrCsSSAN9VG3VYOPrOaJUbO7GYZntHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cafdd78c9b.mp4?token=NWM6gPE97ZzQ6LpubHxyZ_HqLRnHgmwZgWZtyWnZ-wTt_PgyxTUJTfwPo5sMWyaZcnLw7XukJMQMkFGKjxInbnYtih_69Igc0Pdx0lSYZpM4Oz88KKyyF4MhTky7E-HYpJUquoGt9IESrXskgg6QITCpPkSiAjwk0sGhf95biRYiBXhb6Z8PVMPsWbxutEs9qLM4TIm2VbI-CxJCXL8K4R_zstSY0zNp-wBfc-4UbhJIY-gyG3uWVJJI4Sh82tC1bRcsBdn_yi4O8dB9PDP1hjW5IXY7svX6_-IYm7wDGIx3dO_DSkw11FLSrCsSSAN9VG3VYOPrOaJUbO7GYZntHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دو پدیده فضایی در هفته اخیر
🔹
تصاویر دیدنی از خورشیدگرفتگی از دید ساکنان زمین و تصاویر از ایستگاه فضایی و تصویر دیگر از بارش شهابی که از داخل یک هواپیما ثبت شده‌است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/681214" target="_blank">📅 21:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681213">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
سی‌ان‌ان: نشانه‌ها می‌گوید دولت ترامپ از جنگ با ایران خسته شده و دنبال خروج است
سی‌ان‌ان:
🔹
نشانه‌های زیادی از خستگی دولت ترامپ و متحدانش نسبت به ادامه جنگ با ایران دیده می‌شود؛ جنگی که ترامپ تصور می‌کرد تنها ۴ تا ۶ هفته طول بکشد.
🔹
کین فرمانده ارتش امریکا به طور خصوصی به مشاوران ارشد ترامپ اعلام کرده که دولت باید راه فراری از جنگ پیدا کند زیرا گزینه‌های نظامی روی میز برای تشدید درگیری می‌تواند نتیجه معکوس داشته باشد و بعید است که قدرت هوایی به تنهایی به اهداف ترامپ دست یابد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681213" target="_blank">📅 21:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681212">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uq1HczK848c7g6LH8BDqXcnSS_t-JkZps0gTXUqUB7FoqOSuS8oyFXXNXVJQFQJltgRafCie0DtQ_Xt1C3ZWHjWb_jojMB60yIxuEPPmxXKaxjwae0mJjxRnwuGUAGh3FJhO9iTCfTtdHH8wM3m5zZuLcmRchTLZaEH4S0kbALVlWuBXbibcMB7oKI99lx1cAbhfi1HR0uG2VmVFEG3KSXj2LIfdECvTDHurYGnbNx2sP_JQ1uHMfwZmGX_CmwuIj_bY82uWcFGbdKe2IKiVqmylivx237-XxetwPgR76ImAhtk3dFQcEt7pdV6Oa0pRo5wtK3Fi7ngxgniqXaAXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش مهارت‌های ورود به بازار کار؛ مهم‌ترین مهارت مغفول‌مانده در سیستم آموزشی کشور!
🔸
در این نظرسنجی بیش از ۱۷ هزار نفر شرکت کردند که سهم روبیکا ۵۵، بله ۲۸ و تلگرام ۱۷ درصد بوده است.
🔸
بعد از مهارت‌های ورود به بازار کار،
حل مسئله، مهارت‌های ارتباطی، سواد مالی و خلاقیت به یک اندازه از نظر شرکت‌کنندگان در سیستم آموزشی کشور اهمیت داشتند.
🔸
این مسئله بیش از هر چیز، نشان‌دهنده اهمیت مسائل اقتصادی در آینده کودکان ایران از نظر مردم است.
@amarfact</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681212" target="_blank">📅 21:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681211">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12961fee27.mp4?token=hN4SIlsnS5E3SFcD273efGmQoQTt3NT_QChAswv7B7ximFACwPRT3-YWiJ37NR1yHuhDfKc7erT5szGjlf6RllPi3pc0Cw_0mBV3pOI_8qpP-KMrtJPGyZaIn7mDEwzS3US033K1uG5jOvmJ8-GLPrOW4qElwF_MZC-fV3kdC5uE7Z4ZtMqbLondkL8sfDXGteq7I1ejhWP1Q0FwT7pTpYsa4FofQuRjUhis-H767iSaN_IrvBzzmx1Guoe3y5_N_RVZvp_Ki_QXa8ZbnQrE-eK9klUgM2YCBKSCsYA6sOXhLez_zgzeEvbb-osiTHJ79iybHhjy9G7wPPmHRyRQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12961fee27.mp4?token=hN4SIlsnS5E3SFcD273efGmQoQTt3NT_QChAswv7B7ximFACwPRT3-YWiJ37NR1yHuhDfKc7erT5szGjlf6RllPi3pc0Cw_0mBV3pOI_8qpP-KMrtJPGyZaIn7mDEwzS3US033K1uG5jOvmJ8-GLPrOW4qElwF_MZC-fV3kdC5uE7Z4ZtMqbLondkL8sfDXGteq7I1ejhWP1Q0FwT7pTpYsa4FofQuRjUhis-H767iSaN_IrvBzzmx1Guoe3y5_N_RVZvp_Ki_QXa8ZbnQrE-eK9klUgM2YCBKSCsYA6sOXhLez_zgzeEvbb-osiTHJ79iybHhjy9G7wPPmHRyRQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار وضعیت وخیم در ناو آمریکا را رد کرد
🔹
خبرنگار: اعضای خانواده سربازان نگران شرایط ناو یو اس اس لینکلن هستند.
🔹
ترامپ: نه، نگران نیستند.
🔹
خبرنگار: آیا استقرار نیروها خیلی طولانی شده است؟
🔹
ترامپ: نه. نه. نه. به اندازه کافی طولانی نیست.
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/681211" target="_blank">📅 20:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681210">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
رسانه‌های یمنی: نیروهای انصارالله بندر المخا را هدف حملات موشکی قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/681210" target="_blank">📅 20:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681209">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
حمله توپخانه‌ای عربستان به روستاهای یمن
🔹
شبکه المسیره یمن از حملات توپخانه ای سعودی به روستاهای یمن در مناطق مرزی خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/akhbarefori/681209" target="_blank">📅 20:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681208">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841c0b8f3f.mp4?token=B8Oi3uWuttP89SoovlOUi3hE9rwL-EfssiRY0ePJrR1KNC5rKyGBi8hHdcA4Mb240UMffbztcZ806VaJ7bmOg4AhSOmjOsU4-64EdEF8O2mthLEdNRht275vZ-6zp3YM3jGmJECK_1UA8lfUpcvGkkQFiJITE5yZQIDvyCaZB0mQUf20FqYWAJ7Zz10c2exFcEVll4jQbEEV_T1dQKBePcnQQRw06kqeZzNMUfD1vXmzd9CREj0Sb7mOhD1kSwcp9FBCwFWNHDzl09loavaH3zMV_wgsEwlOGPk6AW5WcIaxwRkGAyX0IskjYzKoVuswye6Y-JJtm6zxH41KwBBzBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841c0b8f3f.mp4?token=B8Oi3uWuttP89SoovlOUi3hE9rwL-EfssiRY0ePJrR1KNC5rKyGBi8hHdcA4Mb240UMffbztcZ806VaJ7bmOg4AhSOmjOsU4-64EdEF8O2mthLEdNRht275vZ-6zp3YM3jGmJECK_1UA8lfUpcvGkkQFiJITE5yZQIDvyCaZB0mQUf20FqYWAJ7Zz10c2exFcEVll4jQbEEV_T1dQKBePcnQQRw06kqeZzNMUfD1vXmzd9CREj0Sb7mOhD1kSwcp9FBCwFWNHDzl09loavaH3zMV_wgsEwlOGPk6AW5WcIaxwRkGAyX0IskjYzKoVuswye6Y-JJtm6zxH41KwBBzBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به مس شهربابک توسط سعید سحرخیزان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/681208" target="_blank">📅 20:48 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681207">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
هشدار زرد هواشناسی برای ۱۰ استان
🔹
هواشناسی اعلام کرد با توجه به فعالیت سامانه بارشی در آذربایجان‌غربی، اردبیل، گیلان، مازندران، گلستان، خراسان‌شمالی، سمنان، خراسان‌رضوی، کرمان و هرمزگان، احتمال بالا آمدن آب رودخانه‌ها و آب‌گرفتگی معابر، صاعقه، وزش باد شدید و شکستن درختان کهنسال و فرسوده، وجود دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681207" target="_blank">📅 20:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681205">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4560c67a4.mp4?token=HTCPea9S_ViOKtJiADBo0h1g6oYCZu0Vjoo7LIfyrnlAvtE5j7F9ITo1rfhyD3JRJTQY4RlEPkERVl3-RdiAPcPyOx1sRDAKSZyI-OvxugyN3UOalTTP8vI2oKkpjR7rTd-oB8skL7V1d9D09wf0XbcCPcUaie3pU-G0MIb5_sFudLeMcJ0gW9P_y9FKfLUUpsjMIyHBgTk6bmdg-H6o_-uLzOagcHlhOThSrSelE4UwigOyJVEgAg8n7VA5WeNETuH1sgD1LeFGKQFzFZbxRwz_jHxCroLsjScBMBKZ0t_CSy3tpYZsya_YbDYrGpY_4WIvaduyWerrVnzs1zDG2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4560c67a4.mp4?token=HTCPea9S_ViOKtJiADBo0h1g6oYCZu0Vjoo7LIfyrnlAvtE5j7F9ITo1rfhyD3JRJTQY4RlEPkERVl3-RdiAPcPyOx1sRDAKSZyI-OvxugyN3UOalTTP8vI2oKkpjR7rTd-oB8skL7V1d9D09wf0XbcCPcUaie3pU-G0MIb5_sFudLeMcJ0gW9P_y9FKfLUUpsjMIyHBgTk6bmdg-H6o_-uLzOagcHlhOThSrSelE4UwigOyJVEgAg8n7VA5WeNETuH1sgD1LeFGKQFzFZbxRwz_jHxCroLsjScBMBKZ0t_CSy3tpYZsya_YbDYrGpY_4WIvaduyWerrVnzs1zDG2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آخرین لبخند باستر کیتون؛ ستاره‌ای که تا واپسین روزهای زندگی، مردم را خنداند
🔹
کمتر از ۶ ماه پیش از مرگ، باستر کیتون در آخرین حضور سینمایی خود در فیلم کوتاه «نویسنده» (۱۹۶۶) ایفای نقش کرد؛ فیلمی درباره ایمنی در کارگاه‌های ساختمانی که بار دیگر نبوغ و طنز این هنرمند افسانه‌ای را به نمایش گذاشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681205" target="_blank">📅 20:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681204">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
کانادا ۵ مقام ایران را تحریم کرد
🔹
دولت کانادا امروز جمعه اعلام کرد ۵ مقام ارشد نظامی ایران را به دلیل اختلال در تردد دریایی در تنگه هرمز در فهرست تحریم قرار داده است.
🔹
بر اساس این بیانیه، افراد تحریم ‌شده در فعالیت‌های نظامی، حقوقی و ارتباطاتی نقش داشته‌اند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/681204" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681203">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjzoU3kQIO2sMX4f9Ma9UdlE1o53uqqgaCCda55aHO5FWTl0SrEPbwxQWSZYstIdn9VSKEiyGXDKxgmNUOraM2w3CFuAGVDd4ZF3UC6q9ra3dpJk1of9HvlhOsq5zt-I-oM3h-N9rQSD_j3uYigPXiqSL2X4de1RLJlPHOBQ8JIMlSW9m93op7bEHKYnGvINX7n-_7OJN3mz3DXpGALgqnFNJscQ0yu7rUGSh1UHLpupdrP0sWu0cQ68ivdrxvBnTfdASvNu0OCfUEzXkZ856PjwuplqDhoe97fKKnCyBG4EdEMC7qJ0zZ-VAouzgQfSOmrcGnVYpd3a_AV2632Skg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چگونه فیلیمو «بدنام» را پرمخاطب ترین سریال تاریخ شبکه نمایش خانگی کرد؟
🔹
پس از مدت‌ها گزارشی بر اساس اعداد و محاسباتی رسمی از تعداد مخاطبین پلتفرم فیلیمو بر اساس دیتاهای مدیران فیلیمو و سازندگان «بدنام» منتشر شد که نشان می‌دهد پشت پرده این پر مخاطب‌ترین بودن چگونه است. این گزارش منتقدانه، تحلیلی رسانه آخرین خبر را بخوانید؛
https://akharinkhabar.ir/cinema/10970209
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/681203" target="_blank">📅 20:36 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681202">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wu_6h266GGHkgkCnScuDRxBTWNUVAC9Uz8Yqr7wYURg7CC46IvLsIwbK-WpbOnQCGKOa0hK9KokUplGmgdU9oK6KlsXbP36u72OSTXNg_AKKpF30Jc9nwy5KToxIHVd4DCWM1Mnc05UCihvjBk50xGNReyE1Bd6dragshBjjztM6GulPE8OQhw3IZF2PqU26XEQUEZsv1Q6pASw4lWMu4SX8OctueM4pAA5hrXKO2aNmoY9Mn-YqSGlkbd5PRRNL_Rj9uRTZexbj776ytkPN7AXSzSaYVjvPnAoHIrdjxiLHfLQezC9q0Yx4W__MeKOab4vPrsUkHKDkSMEoeJuHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: در هفته آینده منتظر اعلام خبرهای بیشتری درباره ایران باشید
🔹
ما اقداماتی را اعمال خواهیم کرد که در تاریخ انزوای اقتصادی یک کشور تاکنون سابقه نداشته
🔹
این اقدامات ترکیبی از انزوای اقتصادی در سطحی خواهد بود که جهان تاکنون مشابه…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
روایتی هولناک از جهنم؛ وقتی هر گناه، عذابی متفاوت داشت
🔹
00:12:30 در پرتو نور امام حسین (ع)، رنج طبقات جهنم قابل درک نبود
🔹
00:16:25 خودکشی پایان رنج نیست؛ آغاز سخت‌ترین عاقبت است
🔹
00:24:40 پاسخ به همسر خانمی که به او نگاه بد کرده بودم در طبقه پنجم جهنم
🔹
00:32:30 آنچه در انتظار آزاردهندگان حیوانات و درختان است
🔹
00:40:30 دستی که بر پدر بلند شد، اجازه ورود به بهشت را نداشت
🔹
00:55:00 سنگینی حقوق همسر در ترازوی عدالت الهی
🔹
01:03:45 راز انسان کامل بودن در جمله‌ای از فرزندم در برزخ
🔹
قسمت سی‌ام (فراز و فرود (۳))، فصل پنجم
🔹
#تجربه‌گر
: سید محمد موسوی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681200" target="_blank">📅 20:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
هزاران عضو قابل اهدا، به‌دلیل تأخیر در رضایت، از دست می‌روند
امید قبادی، نایب‌رئیس هیئت‌مدیره انجمن اهدای عضو ایران در
#گفتگو
با خبرفوری:
🔹
ایران سالانه ۳ هزار مرگ مغزی قابل اهدا دارد اما تنها هزار مورد به اهدای عضو منجر می‌شود و دو سوم مرگ‌مغزی‌ها با ۷ تا ۸ هزار عضو قابل اهدا، به خاک سپرده می‌شوند.
🔹
به‌طور میانگین ۲۸ درصد افراد در ایران مرگ مغزی را مصادف با مرگ می‌دانند و در فاصله تقریبا ۳۰ ساعته رضایت می‌دهند که در این فاصله، اکثر ریه و بخش زیادی از قلب را از دست می‌دهیم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/681199" target="_blank">📅 20:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80fd0c3d40.mp4?token=m-TCMobSmMqZRegr06BtOjlAADIQfmdDgv1R_RIpWihRv-relPF-hNmaxFiue7dQjOYTjc5Hge2iUkIV0ZnjpX31MezO54p1i6zrn29KtnDxv3DlTIw34OXGMFreVaqu3Voa11t6dq764UKfC9aFDrpDSLpNBvHBrmEsVblUp2nbzYbU_YzoXZM2mVynnCVsACBsQ7ukduHzqoEyA7tUYAZ5xxkFvQspSWXepULV1evmOMuIHY4ecWBDdRolk5dOSLhZ8CCoFbOY7pQmmyatCk2bHFXGUiA47bZeMA0aQf4zYDTskFcunE3E2neiv9DVsEY-NERz6180U0rVRkfTdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80fd0c3d40.mp4?token=m-TCMobSmMqZRegr06BtOjlAADIQfmdDgv1R_RIpWihRv-relPF-hNmaxFiue7dQjOYTjc5Hge2iUkIV0ZnjpX31MezO54p1i6zrn29KtnDxv3DlTIw34OXGMFreVaqu3Voa11t6dq764UKfC9aFDrpDSLpNBvHBrmEsVblUp2nbzYbU_YzoXZM2mVynnCVsACBsQ7ukduHzqoEyA7tUYAZ5xxkFvQspSWXepULV1evmOMuIHY4ecWBDdRolk5dOSLhZ8CCoFbOY7pQmmyatCk2bHFXGUiA47bZeMA0aQf4zYDTskFcunE3E2neiv9DVsEY-NERz6180U0rVRkfTdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
تصاویر ماهواره‌ای از خسارات به رادار AN/TPS-57 در پایگاه هوایی الظفرة در امارات متحده عربی پس از حملات موشکی ایران در ماه جولای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681198" target="_blank">📅 20:19 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c31f4579.mp4?token=UE3ps2CdGTboZ1GLfbJbrlYu434OXaMFQHtkBpojcDxN-xQK2zxe0jYPzyNrhcbeLOkiuDC07B0QMrYgAfhUQXlX7Ulhi-YRMUtnyDEVQckrCku6-aiaHsMOD1Ma6GUV5LvLpLuvjqwT_P7Trxxrn8tkL5vRf-UYPTuLHLlBCJajPuO29iO6weKzpc5Vs6P90eM0zaR_cujsWQGj7XjxCWLfvpdi70wX7bz11KKKv_627tt_oNCVztB3su_gyqYYJPdYTmy5bi87C2vHZAG8wN0Bb-3zekJP6WGuqPfMTsx7flujzP_7qpi45Nlqg1nbus7s1bdAsL-6W1ADpacr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c31f4579.mp4?token=UE3ps2CdGTboZ1GLfbJbrlYu434OXaMFQHtkBpojcDxN-xQK2zxe0jYPzyNrhcbeLOkiuDC07B0QMrYgAfhUQXlX7Ulhi-YRMUtnyDEVQckrCku6-aiaHsMOD1Ma6GUV5LvLpLuvjqwT_P7Trxxrn8tkL5vRf-UYPTuLHLlBCJajPuO29iO6weKzpc5Vs6P90eM0zaR_cujsWQGj7XjxCWLfvpdi70wX7bz11KKKv_627tt_oNCVztB3su_gyqYYJPdYTmy5bi87C2vHZAG8wN0Bb-3zekJP6WGuqPfMTsx7flujzP_7qpi45Nlqg1nbus7s1bdAsL-6W1ADpacr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول استقلال به مس شهربابک توسط سعید سحرخیزان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/681197" target="_blank">📅 20:18 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
ماجرای دود سیاه در جنوب تهران چه بود؟
🔹
انتشار دود غلیظ و سیاه در آسمان باقرشهر و جنوب تهران عصر امروز توجه شهروندان را به خود جلب کرد.
🔹
منشأ این دود، آتش‌سوزی در محل نگهداری ضایعات پلاستیکی یکی از شرکت‌های اطراف خیابان انبار نفت بوده است.
🔹
این حادثه ارتباطی با پالایشگاه تهران ندارد و نیروهای آتش‌نشانی در محل حضور دارند و عملیات مهار و اطفای حریق را دنبال می‌کنند./ مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/681196" target="_blank">📅 20:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681191">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/micLE1iJq3RMmh1Ndg8zaUXZ0XT3etp3d_YCbKpcmiw9oRU9-qLtagviBd6qGXSZ6Pn4-NzcSfrN6z1BU23JEQYIRBXoJS07e4dIjjRaAJVihE0Klf0D0PRekFE3-SM0mrpLQkWHr1vOBeFdYP5BWa11_Iz7Bc0bvh6nSWR415-MuoISthYyqItooe92UI-GPVb_8oKGF_I3EjYBIntpAzgm4S8uOKdVxqlQ7w28DsIDYzOSBUIC2yK_JD6JyaUKzK6ISqkX30ErVrdt75IBsDV8hhh1gFoIvfeOXkwqxL9qkY6Zj_L2oT_Plm4AvrLfT_eHaxL9fzKnsEl96z0FKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBiH-f_HV9B4uKpDLTJ30apSp_RNaMDX9SY4cBcXiyMgjMe8D0W3Leh6NKPFS2QtfsrSomzF3s0Gl2yPw3KTzns8X0KeYQr4GVqvlyNC0gr214BRcxEQygRhtyaD_GP_O78B4Z2H3s0G8TLisMdPAqKRQit7rmkxCskit9-zdUGru5NDQAYvx2VPsyt6gPh3UyNfWub2ef2diEK1ga0ZOYnO1NnmIriBghSe_jCDSJYy4u2ENDafsdpOzrfEKPODnxJ0UwYXkAjQANT_U_9kTCQCGAZocJoplNOmSkjCLU6IkS6N9jgOzokuX2TByb0URyckfOL3gwXZZAwI3U6p2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ckqvm700yX2887HCRR7cDSUxqSqRq4pUgK0fZzJdRd92kB5Rjhfs7soW1AGgt7zBFctXJiAkes4PbLI9eYBxHfJPCjxJ3XzgIrkAfz3Cm0XNn-mqB2zop1FV4ujFnh-G08GjCGkmrKr2S7SwzLqqLifhQkGX6wbNfqbxgV_gJ-lmHhxbg-jMvYUTnEvNhEik2OPtzNmQgMEP6DR4cO9Ycqhx6mmXJRpbBxnPwEXtc7a41MZ_nbCAI85XLwatBI61utOc0XeRlYBm9s7SYpCFLE3zPpqAkLOoMYPi2yqjywLLoHk28Rv5xIemcq9LuS2QH9TcWEX3ie2dyqNcPTAs4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxW1_XtyVJEzYbscPRyIht8wO-Mllhnr9780kbpdPk-8EFc2Qr4CUt4K81CjrpwLmWsLWbHF2yN2e55yp_3EEqa8tGebI66UV_Gvf5vQQ5cFDJRK_N0kStcVrpsNI9CVfzsI8EqRv5MacwKpsAog_9B4U6-rlsUErT1F_jVbmKMlJm8A3pcG2BTVWe4Yy5C5GoRdyNFMDmcQVPEY5XGvOEEamAg5R76pFvoxz3R08CR1QopYL1og0wXL9Y6tKI19OCi-z24Vwn7izqD2x-VddNEMWPaRTRxYjj3ZI-xJSz-Yr9eFQwUIaUM1yyjOqzq3ncP0q_L7nwoiLuoluPExmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
قبل از شستن لباس‌ها این راهنما را ببینید؛ هر برنامه برای چه کاری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681191" target="_blank">📅 20:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681190">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
حادثه در کارخانه سیمان در تبریز با ۲ فوتی
استانداری آذربایجان ‌شرقی:
🔹
بر اثر نشت و ریزش مواد اولیه سیمان در کارخانه سیمان صوفیان ۲ کارگر حدود ۴۰ و ۲۳ ساله زیر مواد گرفتار شدند و جان خود را از دست دادند.
#اخبار_آذربایجان_شرقی
در فضای مجازی
👇
@azarbaijan_sharghi</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/681190" target="_blank">📅 20:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681189">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزیر جنگ پیشین آمریکا: ابعاد واقعی خسارت‌های حملات ایران به پایگاه‌های آمریکا مشخص نیست
🔹
وزیر جنگ پیشین آمریکا با اشاره به حملات تلافی‌جویانه ایران به دارایی‌های آمریکا در منطقه اعتراف کرد که هنوز «یک جمع‌بندی کامل از میزان خسارت‌ها و فهرست پایگاه‌هایی که در سراسر منطقه هدف قرار گرفته‌اند» ارائه نشده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/681189" target="_blank">📅 20:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681188">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af072972a.mp4?token=ebM5NhS-mtoSmAMJPY4R4ptwaMD91R4y-anpp22ppzJ25vCb-wWElDJGh8B0upxAQgbEhKCHrLpms34KADG8NC4AJTfE375JiL9D1SlU6Xq4if8acbRZV1aqluTEcq8UpC6ltjEfOGdMwHZyTyQ1Iadwc9tw-FmYl4C6sNAZZJjBjXJwpLyx_mXLmpqKOaYhAiqW3gMfJGujlPUWAZFM9tlQcZjQpJEcnIal1fjeOmRO6-1C8OcRsOtjETWZ8a7dpHYRAoMIHEqmpdFIisQo4rJePgKXldBBQPhIKWl8lVePzksxXgXBiZHUs8b15pQOQVzA-xyn94RUQEnO5Zn4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af072972a.mp4?token=ebM5NhS-mtoSmAMJPY4R4ptwaMD91R4y-anpp22ppzJ25vCb-wWElDJGh8B0upxAQgbEhKCHrLpms34KADG8NC4AJTfE375JiL9D1SlU6Xq4if8acbRZV1aqluTEcq8UpC6ltjEfOGdMwHZyTyQ1Iadwc9tw-FmYl4C6sNAZZJjBjXJwpLyx_mXLmpqKOaYhAiqW3gMfJGujlPUWAZFM9tlQcZjQpJEcnIal1fjeOmRO6-1C8OcRsOtjETWZ8a7dpHYRAoMIHEqmpdFIisQo4rJePgKXldBBQPhIKWl8lVePzksxXgXBiZHUs8b15pQOQVzA-xyn94RUQEnO5Zn4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رسانه‌های یمنی: نیروهای انصارالله بندر المخا را هدف حملات موشکی قرار دادند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681188" target="_blank">📅 20:02 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681187">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/024cddc0ca.mp4?token=Qxw3aZeeh2bqEAfd0d9exfX6fVVSBBVAQtZGZ6hjJ4O4nOIMMoUfExnr-SU294UXyGYIOeTsDHMIcHZMRL5E406I3DwGBOyb_XllrrghXhBzSU_ODh-T2Il8JCp5hA5IV4IutALYJYL4uVKqOaHSMCFe1bYMj__0IKH1blaVFa_csjjI_jq0AIsAOZHdFLbW2qcGHqsB7d914BWd23kpVIrLbpWvmCeAxlOuMqWKHR8wUBSqj3P2EGQNoxdMFt2RvTf1eboFxNBUjRCQc90_1QRtgiGTbalZrjavZ6p25_-cwJNSyvjFSX-NBJG3U5oJyxUEx6Ep4yvqUW8uoCm7lxGVcf8CCnWUIFB6rCyQmj_-Gdwtj4kqnfn3bcMI2Ah8AIxsHleymrCvTho0PI_bnD1yWetQHzrBPYrz-LHXPaBh1MUDLjz2AJ5nXSLZ7Wd9BEXDe5YVDnFfmualrAhNaQctZXRhrRHLKD2Mrm4Rc2eyqNmviYDH-k8v3d-vU673Q1J3Xy4BSH84GV16m5Oj8z3x_K5OpCapqHc0M08K-ibR0p4qQrOXN-UxYVefOvIXO2YTsjj4sfvG7jdA16yiGGE5EoAcTdzjPIR829xcfG6HIQdkBB5UttWRiJvAZ1fxW6AZ58WQQXJefP3835bDgPcDgS2lDRZVpBcxMGrf7gM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/024cddc0ca.mp4?token=Qxw3aZeeh2bqEAfd0d9exfX6fVVSBBVAQtZGZ6hjJ4O4nOIMMoUfExnr-SU294UXyGYIOeTsDHMIcHZMRL5E406I3DwGBOyb_XllrrghXhBzSU_ODh-T2Il8JCp5hA5IV4IutALYJYL4uVKqOaHSMCFe1bYMj__0IKH1blaVFa_csjjI_jq0AIsAOZHdFLbW2qcGHqsB7d914BWd23kpVIrLbpWvmCeAxlOuMqWKHR8wUBSqj3P2EGQNoxdMFt2RvTf1eboFxNBUjRCQc90_1QRtgiGTbalZrjavZ6p25_-cwJNSyvjFSX-NBJG3U5oJyxUEx6Ep4yvqUW8uoCm7lxGVcf8CCnWUIFB6rCyQmj_-Gdwtj4kqnfn3bcMI2Ah8AIxsHleymrCvTho0PI_bnD1yWetQHzrBPYrz-LHXPaBh1MUDLjz2AJ5nXSLZ7Wd9BEXDe5YVDnFfmualrAhNaQctZXRhrRHLKD2Mrm4Rc2eyqNmviYDH-k8v3d-vU673Q1J3Xy4BSH84GV16m5Oj8z3x_K5OpCapqHc0M08K-ibR0p4qQrOXN-UxYVefOvIXO2YTsjj4sfvG7jdA16yiGGE5EoAcTdzjPIR829xcfG6HIQdkBB5UttWRiJvAZ1fxW6AZ58WQQXJefP3835bDgPcDgS2lDRZVpBcxMGrf7gM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایتِ فصلی تازه از پیوند، هم‌افزایی و نقش‌آفرینی همه سلائق مردم
🔹
بسیج، سال‌هاست میدان حضور اقشار و گروه‌های مختلف مردم در دفاع، خدمت، سازندگی، فرهنگ و پیشرفت بوده است.
🔹
امروز سخن از یک گام فراتر است؛ گشودن میدان‌های بیشتر برای مشارکت بیشتر، پیوند ظرفیت‌ها و به میدان آمدن انسان‌های بیشتر.
نه تغییر آنچه بوده؛
بلکه کامل‌تر کردن آنچه هست.
https://basijnews.ir/00f1KP
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/681187" target="_blank">📅 19:59 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681186">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f000cdee.mp4?token=FLjz8LwDkBU6LaWNZX6yB7jyQBePDN8opwH_ei2nQ06-g9wDuJe6__nKULaHFtzQaJaaTRHZ8X9Qqzx2jvqiTDOxm4TcMoEbjgD4_MLJw0oE-Aw-dpuJUYJkBEJz-XuL6XWp_aRmPiXBXPWcbFFP0xaL6d_XJjRpwoDw8-MITQYv0aJTh6OOus1G1N1bx3kR6D5ptoF5fjYmEvmlBR6M29y35pfzIlWCc18DUoyMuFKTxlDM1BIvsfofWyHbNQXYPfBr6mzA2600l5GfK85LY5ncAeRRsGSBRJlJFaKgTGchD6W-UC9qjzpsVK-77zNJOEtXLuZgPuYQwnR3NnKCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f000cdee.mp4?token=FLjz8LwDkBU6LaWNZX6yB7jyQBePDN8opwH_ei2nQ06-g9wDuJe6__nKULaHFtzQaJaaTRHZ8X9Qqzx2jvqiTDOxm4TcMoEbjgD4_MLJw0oE-Aw-dpuJUYJkBEJz-XuL6XWp_aRmPiXBXPWcbFFP0xaL6d_XJjRpwoDw8-MITQYv0aJTh6OOus1G1N1bx3kR6D5ptoF5fjYmEvmlBR6M29y35pfzIlWCc18DUoyMuFKTxlDM1BIvsfofWyHbNQXYPfBr6mzA2600l5GfK85LY5ncAeRRsGSBRJlJFaKgTGchD6W-UC9qjzpsVK-77zNJOEtXLuZgPuYQwnR3NnKCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم قاسم: اینکه ایران نخستین بند در توافق‌نامه اسلام‌آباد را عدم تجاوز به لبنان گذاشت حمله دشمن صهیونیستی را مهار کرد
🔹
۳۰۰ هزار نفر با توافق‌نامه اسلام‌آباد به وطن خود بازگشتند.
🔹
ما خواهان جنگ نیستیم اما هرگز تسلیم نخواهیم شد، هرگز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/681186" target="_blank">📅 19:47 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681185">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
سفیر پاکستان: اسلام‌آباد به تلاش‌های میانجی‌گرانه برای حل مناقشه ایران و آمریکا ادامه می‌دهد
🔹
امیدواریم این تلاش‌های میانجی‌گرانه ارزشمند، همه طرف‌های ذی‌نفع را به یک راه‌حل عادلانه و پایدار نزدیک‌تر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681185" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681184">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0rV50ubk4BCUqBMaDySIUoNPV0SgI73QqXf5N12G_EBAEG9iTNgCRYC4b936Vid-E8UiMuVYyqh8LKLKUrxK9Jdqehil0Fe2CElGGoHp4K41e7fRi3om8x_32ajDd7k_MRnnb7oTcc1GgVVmtcWj4cbqXtwZykZNTv-Wy8_1qRWNMM-NHI103s5eg0hGkix2hjD7FRQn6pUyE7haF7eiu6YE8sNCx1cXJjwutbmHVdjglJavKNzKVhGviRVfvkEwJfaIxKPsndL3yFWlEv4Iebrx1j5L6GY222yB7Z4xePSRxalbh9T5nHBTI2AEOPvjQaTyIDTirSqTjNp3YK1Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اینترنت در آستانه تسخیر توسط AI؛ موجی که می‌تواند انسان‌ها را پشت سر بگذارد
🔹
کلادفلیر هشدار داده اگر روند فعلی ادامه پیدا کند، طی پنج سال آینده ترافیک بات‌ها می‌تواند تا ۱۰۰۰ برابر ترافیک انسانی شود.
🔹
رشد انفجاری سیستم‌هایی که می‌توانند به‌ جای انسان در وب جست‌وجو کنند، قیمت‌ها را مقایسه کنند، اطلاعات جمع‌آوری کنند و حتی کارهای مختلف را انجام دهند، می‌تواند چهره اینترنت را برای همیشه تغییر دهد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/681184" target="_blank">📅 19:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681183">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02c7c4f5b.mp4?token=irwW5rCmnKTXj0D0jE93KEtSizZnQw9z3K4UaHfE2nV_QqOlhZUpAad1Bu5l2oqkf29g0fju_63xPCchKpYt93jbHXkatOq5B3EJibr0jEwhXbKqp0TuTguTWbh-rjRhpxsfbEzQ1m8b8OjOuAw6i4CPmt9pU0IXThSm_vaXNROzh4PkumM132D2QZMoANVbfBpdHZOJeSR18BkR7GUxLdxY68iZPiQjsgehjXVd1ukSU58OT137lG5hX7HvR7LGw7Sb7SiulIKfN_sXmEYy3fEIyuIcxUg5z7xq8XB6WzxX7Jkx2LjGOXUc3_P4Rzo1pt5MYN6fKaL9ub8CE13lhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02c7c4f5b.mp4?token=irwW5rCmnKTXj0D0jE93KEtSizZnQw9z3K4UaHfE2nV_QqOlhZUpAad1Bu5l2oqkf29g0fju_63xPCchKpYt93jbHXkatOq5B3EJibr0jEwhXbKqp0TuTguTWbh-rjRhpxsfbEzQ1m8b8OjOuAw6i4CPmt9pU0IXThSm_vaXNROzh4PkumM132D2QZMoANVbfBpdHZOJeSR18BkR7GUxLdxY68iZPiQjsgehjXVd1ukSU58OT137lG5hX7HvR7LGw7Sb7SiulIKfN_sXmEYy3fEIyuIcxUg5z7xq8XB6WzxX7Jkx2LjGOXUc3_P4Rzo1pt5MYN6fKaL9ub8CE13lhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: با همه وجودم می‌گویم که برای من هیچ فرقی بین امام شهید و رهبر معظم انقلاب نیست/ حکم، حکم ولایت و رهبری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/681183" target="_blank">📅 19:37 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681182">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd324af27.mp4?token=Xg4Djgx0y4djzOD7EN0FFRcxWChAdxSmFtRZcs94KNbzqPNze3-Ki5lnR-ewfynRxPLQZN4qYDHeBXZT_HaWpkIWmTgLCQ9nQHrgysr59ld6JQmUEOtv3AdG-humS8lX9NrSglL9tJG_QtO7O9cIx2aMwmYlFHvT5u8k6tkKmh1scrZMXRmwTNC_Fl1zynLB_1wg3SjVVp65St3938Mva0QRCdq6PlVz12s3-0Em9SB9DRdFlHtN7NUhFfgoZDmWxg5U9FwhLtMb5iMJieGJMLDRxmlrKaPbLa97Sf1FRNdjFA53t7sv5JCbv36SwxvFopmOcbf4az1hG8MUaepCJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd324af27.mp4?token=Xg4Djgx0y4djzOD7EN0FFRcxWChAdxSmFtRZcs94KNbzqPNze3-Ki5lnR-ewfynRxPLQZN4qYDHeBXZT_HaWpkIWmTgLCQ9nQHrgysr59ld6JQmUEOtv3AdG-humS8lX9NrSglL9tJG_QtO7O9cIx2aMwmYlFHvT5u8k6tkKmh1scrZMXRmwTNC_Fl1zynLB_1wg3SjVVp65St3938Mva0QRCdq6PlVz12s3-0Em9SB9DRdFlHtN7NUhFfgoZDmWxg5U9FwhLtMb5iMJieGJMLDRxmlrKaPbLa97Sf1FRNdjFA53t7sv5JCbv36SwxvFopmOcbf4az1hG8MUaepCJzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قالیباف: امام شهید، ما را با مفاهیمی مثل شهادت، شجاعت، استکبارستیزی، مقاومت و عقلانیت آشنا کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/681182" target="_blank">📅 19:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681181">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/365ccdeb06.mp4?token=TSxeCKhPoNB-1wOgo5VnxhutszNGRSbyx4lVuYiVrfBv8gcSLdI0DFipL6-Ksyw3jFXzKXT752-ZwjOyeL8FPQ4nGCBQOzeomFj849RJo8y4WFOUkKprt_O-mc_GtBj4g0UjoWeUPNfaiV45VjNdYmlCFZorkgizDuBOWU9BPjRMsusLWRJMMEEsJk66h2fpXoy_SEznGazTAQMLJiXaGu5b-yV4MgrnSLieEO2d2hcGQmwuUlz6RNrzKbdB4MvvdL_xHblBaBoIntjqtANlp0mI1Y_Pu3gzscMioVioyB5K2FLjtqcpVWePs0ksTOJWLxrtA-G9zH5TGVqrp-HaV0nP9aaW0C5wOkFM__yAEgwGgmzmWUUPx3ybunrI1nv69d27WlBr32L8JdSV_-ogsE5q6BcfsXdJm16J5EwdtFfSJNe8rZpUfleHVpa_LzlL7gtOIP3Fr14piPY2usRvpufNRpdd-qvHnwagKR31f477W3gf1iVKB5FP7BtRWo4Yxl1N-2h2940AOF1Vsl4mod1vI3xzAd554u-6USE2iVx__nym6iC5s8B2qXTEULssxbINOoqHHNTS_E_NAbxgblEZ3IA-lFXjD5-fXQiNNBk7N4z-XTU-nIDQ2FNeNqppGB6_Uf9F62upbFKTc3LOTsNKgPh16uWYyYwqe1cHwDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/365ccdeb06.mp4?token=TSxeCKhPoNB-1wOgo5VnxhutszNGRSbyx4lVuYiVrfBv8gcSLdI0DFipL6-Ksyw3jFXzKXT752-ZwjOyeL8FPQ4nGCBQOzeomFj849RJo8y4WFOUkKprt_O-mc_GtBj4g0UjoWeUPNfaiV45VjNdYmlCFZorkgizDuBOWU9BPjRMsusLWRJMMEEsJk66h2fpXoy_SEznGazTAQMLJiXaGu5b-yV4MgrnSLieEO2d2hcGQmwuUlz6RNrzKbdB4MvvdL_xHblBaBoIntjqtANlp0mI1Y_Pu3gzscMioVioyB5K2FLjtqcpVWePs0ksTOJWLxrtA-G9zH5TGVqrp-HaV0nP9aaW0C5wOkFM__yAEgwGgmzmWUUPx3ybunrI1nv69d27WlBr32L8JdSV_-ogsE5q6BcfsXdJm16J5EwdtFfSJNe8rZpUfleHVpa_LzlL7gtOIP3Fr14piPY2usRvpufNRpdd-qvHnwagKR31f477W3gf1iVKB5FP7BtRWo4Yxl1N-2h2940AOF1Vsl4mod1vI3xzAd554u-6USE2iVx__nym6iC5s8B2qXTEULssxbINOoqHHNTS_E_NAbxgblEZ3IA-lFXjD5-fXQiNNBk7N4z-XTU-nIDQ2FNeNqppGB6_Uf9F62upbFKTc3LOTsNKgPh16uWYyYwqe1cHwDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم‌ قاسم: توافق‌نامه جدید، حاکمیت لبنان را به آمریکا و اسرائیل واگذار می‌کند
/
هرگز زیر بار قیمومیت آمریکا و اشغالگری اسرائیل نمی‌رویم
شیخ نعیم‌ قاسم:
🔹
مقاومت هرگز تسلیم فشارها و تجاوزگری رژیم صهیونیستی نمی‌شود/ دولت لبنان باید مسئولیت بازسازی جنوب و تأمین امنیت آوارگان را برعهده بگیرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/681181" target="_blank">📅 19:34 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681180">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هر پیراهن، فقط یک پیراهن نیست؛
روایتِ یک سرزمین است، یادِ یک نسل و افتخارِ یک ملت
🔹
کیت جدید استقلال خوزستان با الهام از
خلیج همیشه فارس
و ادای احترام به
شهدای میناب
طراحی و رونمایی شد؛
تا نام و یاد کسانی که برای این خاک ایستادند، در میدان هم زنده بماند.
🔹
برای پیراهنی که فقط رنگ آبی ندارد، رنگِ ایران دارد.
بانک ملی ایران، هوادار استقلال خوزستان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681180" target="_blank">📅 19:32 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681179">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0QbuzXp7AKmzBQIH4SlE07Srwy8PnJ4nyCGn00TZZp3VpXYycRH7Xjn0xCoHWyGEER-aFWlxm3q3FPyRCivF1DGPu3CRW2-DsOlhdhjlluOU-g-P3CLF_V__-3hlpBmc1_GV53jCY3kiCWA9GJ5NX6rkenj7xfMkeX3Tl3hdWpqbV-e5Yt8qeqniJDyXO_TAbjnmXYbxzySRMlFPSJcr3dzYSvCFW1znqDu7tPqopvm3risLWJdUSEaxnvxiUBMjbLOVauUd32aU1QsN6DAiO8vbF-aeJJWLrwBAG8tHwW4vzgydMi3TYvuTckBKWjRkpy6FAVx00L-zhdwYR1cgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نوسانات قیمت نفت در ساعات اخیر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681179" target="_blank">📅 19:25 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681178">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
شیخ نعیم‌ قاسم: دیپلماسی بدون فشار نظامی نتیجه‌بخش نبود؛ رژیم صهیونیستی تنها زبان زور را می‌فهمد  دبیرکل حزب‌الله لبنان:
🔹
مقاومت در پاسخ به شهادت رهبر فقید، حضرت آیت‌الله خامنه‌ای، و نیز واکنش به ۱۵ ماه نقض متوالی توافقات از سوی رژیم صهیونیستی، دست به عملیات…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681178" target="_blank">📅 19:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681177">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJ1M9klfWQoRc2TA9P2JzVK_pMJiynC-7Z3Z4aa09H-BCcpz-J20t3qrOs_p81XrKJJ2HGDwEBKJKHZlVSd23UmKTA111IFXFcFefvTGXhiant0MUbGBAeCc0ijS-7YN3ECh4a5_zU_1Tat1HJMOEru6zXrReB_iq_A26TQFM-v8xR-Z0PExMN-QRC-kEz5Y0FPcZC9IKGeuT7VNvJjGPaSiQj22TcF7LISYrqOflnrw_ryf-sCiz_aEDzqwN9SZL4_polDffVX-mTtTpWtJ93H948EFV35-VXPSi4TvYKfOwKPR1dsoHCMMXZiSBVT1A_CgPuY6c-SepFAED8IHGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنوع اقلیمی در کشورهای جهان
🔸
بیش از ۸۰ درصد از پهناوری ایران را اقلیم خشک و بیابانی تشکیل داده و مابقی آن شامل نواحی معتدل و سرد است.
🔸
در مقابل، کشورهایی مثل آمریکا و چین تقریباً تمامی اقلیم‌های پنج‌گانه جهان از استوایی تا قطبی را در خود جای داده‌اند.
🔸
همچنین کشورهایی مانند اندونزی با اقلیم ۱۰۰ درصد استوایی و امارات با اقلیم ۱۰۰ درد خشک، از یک‌دست‌ترین پهنه‌های آب‌وهوایی محسوب می‌شوند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/681177" target="_blank">📅 19:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681176">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d1f1a7070.mp4?token=ELplWMzacA4JiJ4qS_bjKd_IakfrnGCuI66GobclIudET1aGXG98em5_CmOWi13VPPzF9EMXOCfSRdRIXe4O3rV7_ZZ4LQw4RkzOEGpMXO26bMyQYH5U4ve6xR7_Id4VRXvLOx6YAc9GDyTlrIcWRJ69xNfNb-z5J8BTowkXdiSDbCgFY5ZaXcawodW_wNehzHeuFxEYBCe4FjnTCOYT7tWNtAFx0DGXoYoQJgCRQNIuInUo9AGqvxrV3pe6ryol0xCSkv4J6MGaD_uhPCw4zdLUG8zeTg0NzDxUhJcKN59t-plJxhVcMvKqav5Tl_5IQVd-9FVio3BzlLkzKDSGwRfpRHdiero6rnyMuvFa8kwGxVzyTrHf7MMGw3DtDEtb9hNtzaS8w9rFqR4QnJJ3C1JyofKECFU5uIWA1U456i06Wq6yPVrYfKOSiJJ7P2cVT5tSAgUxWluURlU9bNci4JzgbMaaB9Yrcjx2CbSl6MlJAyjdC1SdhpbjAY8hDivQ4NJ7U13Lylz0Ihzf7V6_F27TjZPvh9wSBBsTCzP8oZSzKR40Zaxb_fzKXpxxZb8fYxrz91p6dSPsjPVsxIPM-hL592mkqCFGV-Z6IXDUrmCI2i9AoqnA9m0SBui8grF9zuLRy-Zq9Cu6z2TH9tcRacu14-EiKTXH85WZDXWl1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d1f1a7070.mp4?token=ELplWMzacA4JiJ4qS_bjKd_IakfrnGCuI66GobclIudET1aGXG98em5_CmOWi13VPPzF9EMXOCfSRdRIXe4O3rV7_ZZ4LQw4RkzOEGpMXO26bMyQYH5U4ve6xR7_Id4VRXvLOx6YAc9GDyTlrIcWRJ69xNfNb-z5J8BTowkXdiSDbCgFY5ZaXcawodW_wNehzHeuFxEYBCe4FjnTCOYT7tWNtAFx0DGXoYoQJgCRQNIuInUo9AGqvxrV3pe6ryol0xCSkv4J6MGaD_uhPCw4zdLUG8zeTg0NzDxUhJcKN59t-plJxhVcMvKqav5Tl_5IQVd-9FVio3BzlLkzKDSGwRfpRHdiero6rnyMuvFa8kwGxVzyTrHf7MMGw3DtDEtb9hNtzaS8w9rFqR4QnJJ3C1JyofKECFU5uIWA1U456i06Wq6yPVrYfKOSiJJ7P2cVT5tSAgUxWluURlU9bNci4JzgbMaaB9Yrcjx2CbSl6MlJAyjdC1SdhpbjAY8hDivQ4NJ7U13Lylz0Ihzf7V6_F27TjZPvh9wSBBsTCzP8oZSzKR40Zaxb_fzKXpxxZb8fYxrz91p6dSPsjPVsxIPM-hL592mkqCFGV-Z6IXDUrmCI2i9AoqnA9m0SBui8grF9zuLRy-Zq9Cu6z2TH9tcRacu14-EiKTXH85WZDXWl1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شیخ نعیم‌ قاسم: دیپلماسی بدون فشار نظامی نتیجه‌بخش نبود؛ رژیم صهیونیستی تنها زبان زور را می‌فهمد
دبیرکل حزب‌الله لبنان:
🔹
مقاومت در پاسخ به شهادت رهبر فقید، حضرت آیت‌الله خامنه‌ای، و نیز واکنش به ۱۵ ماه نقض متوالی توافقات از سوی رژیم صهیونیستی، دست به عملیات موشکی زد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/akhbarefori/681176" target="_blank">📅 19:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681175">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be8a99796.mp4?token=d23khuuGxpgov9qOm415qSP3A-GYKjf8L7Oc6C9l_zn8_mT9hdl9haFnQag6FCxBxNTq5MRZLev_SiFgrNq45NFDbPvJVmbW52ZSH0PumphRfA9tQ3pmskg7wMK8ZvJ-yW0cI37lBj01l0HJLzQnzc5XUcVFXeZu9hk6cHXuQxE8ViYe57SZcsQ-eQ6faDVx6QTa7oFHDXkRzq6Ign6JsbTBMB1lDe0gusjn4ogakQOJ9A126YgruHdv8BOgnbbw5V07Sel_S-iHSlP3URRiDLRuEG4YV4F4ADQwZ5GWmTfcf5tU2OTbXArefLMxLhfeOOC5xPjl82jISfLUEP30HG8XhXWJimPe-ph0X-WTLqi5OiRpabpSHN2Bk_EpqQ9fVyIEOIS48Uavz3OYp773F6_rUD8ldyjhxwUfDZSMoIvMCk4zDFyqow3Bo3vANgnxFDpBdJf7mnP4emCsFJGYw8gcIsLBUn3N3Rs2atGHq3nug1rXwshchFmPzhiwWBIj_x4MK_RO5GRVFUwDeDYcZe8KJ6V9NEUhv2XejmxcaRtut7kiDNi2HxIzL_2BLmUH5OGorR-1Tj7jW7nKmxwsm2utxtsBSqJU5GAxFoin2xECN78IPlSuvAfx0rETNssMK-wiapuWQiaDumtFU2F74B5b0VH2xobEsXNsKRncp1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be8a99796.mp4?token=d23khuuGxpgov9qOm415qSP3A-GYKjf8L7Oc6C9l_zn8_mT9hdl9haFnQag6FCxBxNTq5MRZLev_SiFgrNq45NFDbPvJVmbW52ZSH0PumphRfA9tQ3pmskg7wMK8ZvJ-yW0cI37lBj01l0HJLzQnzc5XUcVFXeZu9hk6cHXuQxE8ViYe57SZcsQ-eQ6faDVx6QTa7oFHDXkRzq6Ign6JsbTBMB1lDe0gusjn4ogakQOJ9A126YgruHdv8BOgnbbw5V07Sel_S-iHSlP3URRiDLRuEG4YV4F4ADQwZ5GWmTfcf5tU2OTbXArefLMxLhfeOOC5xPjl82jISfLUEP30HG8XhXWJimPe-ph0X-WTLqi5OiRpabpSHN2Bk_EpqQ9fVyIEOIS48Uavz3OYp773F6_rUD8ldyjhxwUfDZSMoIvMCk4zDFyqow3Bo3vANgnxFDpBdJf7mnP4emCsFJGYw8gcIsLBUn3N3Rs2atGHq3nug1rXwshchFmPzhiwWBIj_x4MK_RO5GRVFUwDeDYcZe8KJ6V9NEUhv2XejmxcaRtut7kiDNi2HxIzL_2BLmUH5OGorR-1Tj7jW7nKmxwsm2utxtsBSqJU5GAxFoin2xECN78IPlSuvAfx0rETNssMK-wiapuWQiaDumtFU2F74B5b0VH2xobEsXNsKRncp1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیر همستر ۵ ساله؛ تقریباً دو برابر عمر معمول همسترها!
🐹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/681175" target="_blank">📅 19:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681174">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
فرمانده کل ارتش: تا آخرین قطره خون از ایران دفاع می‌کنیم
🔹
امیر سرلشکر حاتمی: این قدرت ایمان است که می‌تواند یک جنگنده اف-۵ را به فراز مواضع نیروهای آمریکایی در کویت برساند، در حالی که آن‌ها از پیشرفته‌ترین سامانه‌های پدافندی زمین‌پایه و هوایی برخوردارند،…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/681174" target="_blank">📅 19:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681173">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا هنوز حساب‌های بانک آینده تعیین‌تکلیف نشده‌اند؟
هادی محمدپور، دبیر کمیسیون اقتصادی مجلس در
#گفتگو
با خبرفوری:
🔹
پس از انحلال بانک آینده و ادغام آن در بانک ملی، روند تعیین‌تکلیف حساب‌ها، بدهی‌ها و کارمندان این بانک به دلیل محدودیت‌های ناشی از جنگ و مشکلات سامانه‌ای بانک‌ها، با تأخیر مواجه شده است.
🔹
مسئولیت اصلی پاسخگویی و تسریع در این فرآیند بر عهده بانک ملی و کمیته ویژه مشترک با بانک مرکزی است که باید هرچه سریعتر نسبت به انتقال حساب‌ها و تعیین‌تکلیف بدهکاران اقدام کنند.
🔹
تأکید می‌شود با وجود زمان‌بر بودن فرآیند بانک ملی باید با اولویت‌بندی، هرچه سریعتر نسبت به تعیین‌تکلیف مشتریان و نیروهای منتقل‌شده اقدام کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/681173" target="_blank">📅 19:03 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681172">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fef4881ef1.mp4?token=c6gbZnbmXGNNBiu_p-Fz6L5HSwZgUoI_IH5z7JXIKRyeh38cLpkUx3B37-OixC_10dlH03BlETkvbJp0-Yg3aWI4qiklQPOFSh8dMXuqa7R3sK8ZQDRpDZ3EMEyl177QcZtYgo7icjX3lMQV9dsF36KrcLKDOI-bNpF49pZo1Ne1vVSM6HmrS5bFP0TX-bSq6j3opCkhdY-6lIfqvnjkFhCR3Ikcd1NFCECP4Wu2L8D0zrZh9Kf65GEaIDps4FLrbMjl21ZAhbOnClsGEZcYHpwLSrjCtlys8rl1cwFAMLbfWUD5XjPVSrwgJ3MTCswlrTdEuWo4bjpSAwnEcnFKAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fef4881ef1.mp4?token=c6gbZnbmXGNNBiu_p-Fz6L5HSwZgUoI_IH5z7JXIKRyeh38cLpkUx3B37-OixC_10dlH03BlETkvbJp0-Yg3aWI4qiklQPOFSh8dMXuqa7R3sK8ZQDRpDZ3EMEyl177QcZtYgo7icjX3lMQV9dsF36KrcLKDOI-bNpF49pZo1Ne1vVSM6HmrS5bFP0TX-bSq6j3opCkhdY-6lIfqvnjkFhCR3Ikcd1NFCECP4Wu2L8D0zrZh9Kf65GEaIDps4FLrbMjl21ZAhbOnClsGEZcYHpwLSrjCtlys8rl1cwFAMLbfWUD5XjPVSrwgJ3MTCswlrTdEuWo4bjpSAwnEcnFKAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اولین گل فصل؛ گل اول تراکتور توسط شهریار مغانلو در دقیقه ۳۴
تراکتور ۱ پیکان صفر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/681172" target="_blank">📅 18:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681171">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzUFFqePNaUL8ztrvIDCRAVfJ3KpF0zuO0vi5aPHaclxKq7gfwEklKf5-xAW3SwDGH_FpGhJ7r0q5zkXhPuUCvqMrQ96wGZu_SV_eENEstRsnNciD8G_PWUd4xwe4iqvOwmqHRknzbQ6hEnqQxglUC1_4fEyPIRcxTmKO1qS5fUcBXc-kblrxCPxHPLsD-mSRps0em5NkuhqcufjcxZVg6IHb76_6dVHNRCgO-AZME3PYynLtbwJGKu0TE6R_de1n6YUyqobygyxBgrX28LDZCyR2YTYlIaBllA9I52NIvslMAOhRg6Ufp2CTN4Q97XlWC6mha6GvCJsk0YZAtX9Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/681171" target="_blank">📅 18:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681170">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z07TzBOPw3gi6YCAbBsLrH-ZcFa3afA0I_X2rta_J9dxPSOpa9mxO1LOvghX2TK4JW-35qbsVafEGNH36mVGJenTnMtK5P6s6tep_pGY7EEzrATXcqh1KsyBfEqR2TQ4W0k-kIfpo3C2OSEvS0xsDQ2vAc2qpaBp2cs13A4CktgAAO2ETK5tqwqOpoBPZyWuvOrudnAia-L4n7kIDmQVuIZEv227PzpchNmssiytMFmCP5IZr1BgPAc_87HvTv_otzp8i0C5nY7njf0YXONZyWxxlHIm3BMAE_NaSuus6q1-cm5iByXpI-8lrn_ynGHrp1uPGrvEAqy1gKanYCagoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گوجه را ببوس! | نمایش آشپزی با ملکه پاستا | نادیا کاترینا مونو کیست؟
🔹
نادیا کاترینا مونو، که با نام مستعار «ملکه پاستا» شناخته می‌شود، یک سرآشپز ایتالیایی، نویسنده، کارآفرین و شخصیت رسانه‌ای ایتالیایی است.
#چرخ_زندگی
تجربه میلیاردر شدن با آشپزی
👇
khabarfoori.com/fa/tiny/news-3143141</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/681170" target="_blank">📅 18:38 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681167">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UcCcokoF6PBB8WayfFQhVXpF0LzhRsajw4tLMcQwZClgRm4QNhY5zqbby175APhqs7QxFISvEvGD0EIaPcZ1XXm-EWEURewmawE4OfS8Mh_Z1RNYEXLQurz2zpqriPqqK_7WDfOnlEJw9BPzLDM1hy2XEFoQ9WZafre_Y2a_tAj9lwT1Tc36dUIbDZLlhGVWCPuFt5eNh-p-zCM4a3bcQtVly-q5BOe_YgoY-BHt6bWAORlE4v2fmH9vlkyxSW86ZzbSj7sREzOWK-Tq89SlbWtjzKdFHLQMV_pSATBJ1AqGet2rBxPDlduBrVKfkDWxe-P-aILU7g5L3fYCBBE_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpXUI0h1S7wrL_TBayxX61KsarmIAL2WnoboRlmGCgPtWGndoAcO4wQ4PuQQRl36FCgigWOOUB5KnoED7qNUrsYA5N_yz1AteKEQNO6FzhvEkfsFCswdDqCaSrmONe-HOYJJ3cfQi-5qr1I_yk9IeBOkY9vbJ0CnLNS6YsM4VVu7gQvnKPkNxhtswt_4G1Lihs6QvMqknf34HfxL05x4ptvlxIuVtw4LGtGvdCI1MGBUeHXec24KogJBBPS5Gjv261URtXYW9ciddJb3BQVIgKdpWOm9DzqYf4M2E1850D5VZv_hHgGteEDsqyADOvOlGQP-heD_dmDzI5kmlOAvnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
جدیدترین تصاویر بارگیری نفت در خارگ
شرکت رهیابی محموله‌های نفتی «تنکرتِرکِرز»:
🔹
داده‌های ماهواره‌ای نشان می‌دهد یک نفتکش غول‌پیکر «شرکت ملی نفتکش ایران» امروز در حال بارگیری ۲ میلیون بشکه نفت در اسکلۀ آذرپاد جزیرۀ خارک است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/681167" target="_blank">📅 18:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681166">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d719e28752.mp4?token=GnPM5TuN1MfRughp_RKTumYPrBIJ0ZncHrM5QxDvNH1dALYi_brbj3DgsZMvR3nGAJHPWLxKt1gSpFzLER8ectZqRf5a9GzApSbk_q76rsoBhVDAN2AeL017xFslxk4x7Dfx9OIkNxwooIccn9TocF8HXB1WNCLhLyuCIKVD5D8WuKcsT51Ly9zAcr5dtnksCxo5fJu68mlLiGQbKPOkpIeeyTXko6AXj0lzPGSpmSszZvnPoxImckkbd89POYDFq9F7GKCLKCtG-W2yODcCaqsXfHbltFixT8n-t6tb8Wy6sJh24NDWFcpj0opIgVNGAeSIE3QhapD-8jiyMZmbZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا دبیر، تیم ملی کشتی را آبیاری کرد
🔹
علیرضا دبیر برای کم کردن گرمای تابستان، ملی پوشان کشتی آزاد را با آب پاشی خنک کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681166" target="_blank">📅 18:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681165">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
نظرسنجی معاریو؛ آیزنکوت از نتانیاهو پیش افتاد
🔹
بر اساس این نظرسنجی، «یشار» به رهبری گادی آیزنکوت با ۲۳ کرسی در صدر قرار دارد و پس از آن لیکود به رهبری نتانیاهو با ۲۱ کرسی و «باهم» به رهبری نفتالی بنت با ۱۴ کرسی قرار گرفته‌اند.
🔹
در سطح بلوک‌ها نیز ائتلاف…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/akhbarefori/681165" target="_blank">📅 18:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681164">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c58a8ae1.mp4?token=UMslw3NQ7SGQeCAnSt7lZbOn_MJnpiuSdBNYmoWkw-nAMfYnYj8CInouLkKDYnrfgZOvQQZTHVRe6k_yuLgH81oDpqQVfCx7CaRBod_Y9wwjLgPSJd9aqQ-4TFJNHCfN2etsx55COSYN_i9ZvVTdCXaP5uvYhQpiscuyhXftvsQlUPGwovJ6u-nRgTn2us6d6d3jWFJ_dbs6pTirlCXV5R9NsC8Fvi1kO-jRCd6NPDUtJMn_EVLj8H-oN98tI_35jUjEsaRs898fKnIAUhY8B9kyOCvCnj1RWyblCDt-f5yX9LtzmucDmrcRJ6-i_UzmA-BLnOAEbbHVKop5AKP7kZYxYMwBkLJqY_hJSW-TCAOXhHyuqpW65LcCuXV8kwlifhCTJKsmakXXNsNzbrC7NaFn81yGoxlFbdslygNQX0cj4nVCmMp5vJjEGfGec1FKo4gC0joRxcI7OpGaZzPJsBdLdX67IxQQXegiAncI7c0-dwLDkGAsS9r33TGfgX17HFKqo83I5ampZTYemQNoFBJp7Hxk3poT5J3rhPviVT7RV1TAeD--Nqt2UC4AybJOzRLOW2fxJHa2s9hBKjSrDluO1GCJIFlzG7ipmgq_HOoenTRo3hw0t5WJPUCbQ9HuberYrVu0nVINS_qtlF9ha3WT2w7rctLtJpvXbwojzOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با جان خودتان بازی نکنید؛ هنگام شعله‌وری سیلندر، با بستن شیر فلکه از گسترش آتش جلوگیری کنید
🔥
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/681164" target="_blank">📅 18:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681163">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
نظرسنجی معاریو؛ آیزنکوت از نتانیاهو پیش افتاد
🔹
بر اساس این نظرسنجی، «یشار» به رهبری گادی آیزنکوت با ۲۳ کرسی در صدر قرار دارد و پس از آن لیکود به رهبری نتانیاهو با ۲۱ کرسی و «باهم» به رهبری نفتالی بنت با ۱۴ کرسی قرار گرفته‌اند.
🔹
در سطح بلوک‌ها نیز ائتلاف نتانیاهو ۴۸ کرسی و بلوک مخالف او ۵۷ کرسی دارد که در صورت پیوستن «خانه صهیونیستی» به ۶۱ کرسی می‌رسد؛ احزاب عرب نیز مجموعاً ۱۱ کرسی دارند.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان عبری دنبال کنید
👇
@AkhbareFori_HE</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/681163" target="_blank">📅 18:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681162">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
پرداخت وام ۴۰۰ میلیونی برای اسقاط خودروهای فرسوده
🔹
رئیس هیئت عامل سازمان گسترش و نوسازی صنایع ایران با اعلام آغاز اجرای آیین نامه جدید نوسازی خودروهای فرسوده از هفته آینده، از پیش‌بینی وام ۴۰۰ میلیون تومانی برای دارندگان این خودروها خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681162" target="_blank">📅 18:07 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681161">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lijzYkcyNz4taeOCWaUf9WypYMSVhKConhwkcg0TULLkOpx5VUukKeV6dELwzz_CARyywseKR_b1IzZybEWeSpYrsuodSrQkjxLdInT-fskfxWwI9-ot6gNveEQsNIidDht6qWJZjCrG8NL701uu-U28EadKhum4am7mrNpD0u2D5M0ZS9lSuKh6K11OX6AdQJEYg6tcolQhkn58Udbe05FfUMrmAp86w22qNOVoKL5FtOAnGQTbzcYRmmGxqBeTWil4EoVK1xkX6CtWihlH2gbSKtXZIeW7v8OtmzoBiNMA5WzFNfHnvAKJMtE9zs1hk1YadOo1VFPX9iFggOJDpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هرمز کابوس واشینگتن شد
🔹
بسته ماندن تنگه هرمز حالا به یکی از جدی‌ترین نگرانی‌های آمریکا در بازار انرژی تبدیل شده است.
🔹
واشنگتن که پس از تحریم نفتی اعراب در دهه ۱۹۷۰ برای مقابله با شوک‌های نفتی ذخایر استراتژیک خود را تا بیش از ۷۰۰ میلیون بشکه افزایش داده بود، حالا با افت شدید این ذخایر مواجه است.
🔹
پس از برداشت‌های گسترده در پی جنگ اوکراین و عرضه ۱۷۲ میلیون بشکه دیگر در جریان جنگ ایران، حجم ذخایر استراتژیک نفت آمریکا به حدود ۳۰۰ میلیون بشکه رسیده؛ سطحی که پایین‌ترین میزان از اوایل دهه ۱۹۸۰ محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/681161" target="_blank">📅 18:04 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681160">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fPsHvI2CkkxKO8PAo8xQono2nyUfFZYgxNvuBAJgSgM6c3TFJvBPE6my4O43h0Gi6ishdd_Dpit-CNYksLBOZuJ_I7aDM3nDafwY_rZarI2b1wzzsQcL8w2jsmyuzltpy_eajl0pZP-Y_hF9ovJsY0nKFklcznErrAe5JL5RiiJRtS1x8e__Wz_MlE7wueglZhp9Gvcb3ZeV95dlrE3agdkA_VViF0dQwCVcqKRkwiiuEoiKlsZ5u2D2d_ibKeK3wN84ky_T9bAHETjyIeJmuoRtWP_PmKvU46RQ9BG3q7NshmaMNGRFSKmylDaKCnVsofDsjg3MvUcRSuWKekT6Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لگوها این‌بار وضعیت بحرانی سربازان تروریست آمریکایی در ناو آبراهام لینکلن را به تصویر کشیدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681160" target="_blank">📅 18:01 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681159">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
ورود خودروهای فرسوده به کلان‌شهرها ممنوع می‌شود
معاون وزیر صمت:
🔹
خودروهای فرسوده از تردد در کلان‌شهرها منع می‌شوند و نقل‌وانتقال، تعویض پلاک و جریمه هوشمند آنها نیز ممنوع و اعمال خواهد شد.
🔹
این قانون شامل خودروهای شخصی، تاکسی‌های اینترنتی، ناوگان حمل‌ونقل عمومی و خودروهای خدماتی و باربری است.
🔹
گفته می‌شود که برای اسقاط خودروهای فرسوده به دارندگان آنها وام ۴۰۰ میلیون تومانی پرداخت خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/681159" target="_blank">📅 17:58 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681157">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yyi8HT7kihALyeEBm4CvK3BxmLq5LdGkINV50S3GYSBiyqaElUasGMZRKBSfBgdY6QFA9dI73Ljt6_oD-H5VulmN-XIcZjGTUC0aRvOMWCcXZ6kbg1CdXGwgjYuZpdkSN5EV9WqsmRJ27FXA3k_SyHjnyxPjD6qofGhgF8IZutita_Tme4NdTLSurlJLgW9jnSSuvmshFVVdNQGuqHwpeyQwzAOcb0rIPr_RUNw_cGJ7GcAJ0VdoAydngMwFQwQS3pwT6sbp2ZeMgTLiIXSP2tCV7lktulkRVin3fN7Nqb9u4UQZZPatW20vNs5WjhlTQz2Ik82CIyoo3i-02skbmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این جنگ‌ها نشانه آخرالزمان هستند
🔹
در روایات شیعه، از جنگ‌ها و آشوب‌هایی مانند خروج سفیانی، ناآرامی‌های شام و درگیری‌های حجاز به عنوان برخی از مهم‌ترین نشانه‌های نزدیک شدن ظهور امام مهدی (عج) یاد شده است.
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3237515</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/681157" target="_blank">📅 17:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681156">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
عراقچی: اروپا فاقد جایگاه اخلاقی برای موعظه درباره حقوق بشر است
🔹
عراقچی در گفت‌وگوی تلفنی با همتای یونانی، با انتقاد از «عملکرد دوگانه و مزورانه» اتحادیه اروپا در حوزه حقوق بشر، بیانیه‌های مداخله‌جویانه علیه ایران را مردود و ناامنی فعلی در تنگه هرمز نتیجه مستقیم تجاوز نظامی آمریکا و رژیم صهیونیستی علیه ایران دانست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/681156" target="_blank">📅 17:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681155">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5tJE3aHmb7hx7JSM1jMbh2SRPg-vDQF8WhgpccPvPCy7ZpzPZAOcUduMmMXrjhi7xI_9I5Rd8xPQh8f-64y5RgCE6ICwFYj4cvlJHITUyZOvC0WyP3rjmQSHkzHEu45QQ38O_ZcKX7mSg0E3mZd23f78zqcFkiwZJYJUarTALLCz22l9fTpRjNwlGTjwjyWp22BrpMmhPf1J_L4O4YbuC4XrFOjVPx0k0yNfgmBBMOKu0XfnkG8XcmF7jmoKG0qVJrJd51TPQ2vTEI3jjzEKC3XhkjvDJSdXzks9j1QpE22QpyZ1GEA0qfbHrvwfIysxnvtF7oS0lAm7l3_w7PclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه چینی: در طول ۲۶ سال، این چهار مرد به بیش از ۱۰ کشور مسلمان حمله کردند و ۱۱ میلیون مسلمان را کشتند، اما هرگز تروریست نامیده نمی‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681155" target="_blank">📅 17:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681154">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افشاگری نماینده مجلس: مدیر شبه‌دولتی ۴۰۰ میلیون در ماه دریافت می‌کند
مجتبی یوسفی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
یک مدیر شبه‌دولتی در خرداد ماه ۳۰۰ میلیون تومان حق ماموریت برای حضور در محل کار خود دریافت کرده و با احتساب ۱۰۰ میلیون تومان حقوق در مجموع ۴۰۰ میلیون تومان در یک ماه دریافت کرده است و رقمی که با حقوق متخصصان واقعی صنعت نفت و گاز قابل‌قیاس نیست.
🔹
در اقدامی دیگر دو مدیر در اهواز در حالی که به جوانان بومی خوزستان، سیستان، سوسنگردی و باغملکی گفته می‌شود اشتغال وجود ندارد فرزندان خود را بدون ضابطه در شرکت فولاد استخدام کرده‌اند و نمونه‌ای آشکار از بی‌عدالتی و عدم صداقت با مردم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681154" target="_blank">📅 17:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681152">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnce98jukoyB0AIL-JXOMlWOwdjNYw8zHNLLX-ln6THIiUOaWj625T5KNI9WNRh2mFHjaNEsnFKsA0xt--6ofpV830IL9DVQ729jAgoHwNyHvK88ZR3eNJuZYh7UciKwGn4A-Q87cPqdgAuH7eZ75mriXNww7dGKA8viaWOojjTWtFnzd6GS7P-1LC-Qcqrfmu5FwxFcmzp-igf0glopoE5EA4u5aBj76jGJN3SkeBvR3e7TdjO5GWnyrYclKCzLM6Cesvi_8kt1UacIkny4mqCaQb_qfTd-uiJOU820aHA6iESob7swJK-P3TZYVoCiJMDWy9Fi9hqVeloI3UmK-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4M4RenPMoWc0LF0hH_7-DsoQOp8oiQ8-I99VSENgWmXvAijoPobi4jAKeIiQ9VhtbR3PkNLoHVNJ6_TUHwFCHLbGkdQwlPsI1j7ZrbFxRKLGh1WiY6ldcRoI6PGgRLw7uMofXQTooc-hpJbcRgrpKCgfxHA6qHjI1AFZaz4jWrZmZgnaWCP9wJoNlcR3fiRmwFr76Gsaecj-XXBnyXYLj8-EY3gHz3DhD_F4-K6uSc1p0JyuTe_VWEbW1We_kxlTT6zw05oJ39snJizmcPIhu4nOn1rv1cUE9MjOn4-1b4Vfg1X3qCDZ1JiXmybFKEWphWOrxv7r6OTDB1aql3XxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یک روش ساده دیگر برای تهیه میوه خشک در خانه
🔹
یکی از روش‌های تهیه میوه خشک، استفاده از ایرفرایر است؛ روشی که برای شروع در مقیاس کوچک می‌تواند گزینه‌ای در دسترس و کاربردی باشد.
🔹
ایرفرایر به دلیل نیاز نداشتن به تجهیزات تخصصی، امکان تجربه و شروع این کار را…</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681152" target="_blank">📅 17:21 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681151">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سی‌ان‌ان: هیچ مسیر واقعاً امن کشتیرانی در شبه‌جزیره عربستان وجود ندارد
🔹
کشتی‌های تجاری در خلیج فارس و مناطق اطراف، با تهدید همزمان در تنگه هرمز و باب‌المندب روبه‌رو هستند و وضعیت امنیت دریایی منطقه وارد مرحله خطرناک‌تری شده است.
🔹
فشار در هرمز، مسیر بنادر دریای سرخ عربستان را تحت تأثیر قرار داده و همزمان حملات یمنی‌ها مسیر جایگزین را نیز تهدید می‌کند؛ حملات به شناورهای مسیر عمان نیز نشان می‌دهد ایران توان اعمال فشار بر مسیرهای جنوبی کشتیرانی منطقه را دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/681151" target="_blank">📅 17:16 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681150">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29eaab8d0a.mp4?token=kG5FkHiYd3TzJXP9cH_2hdI0E6IX2D2QiWCECfaYVO8fR6Ihiat0hC7fUv1pgh5k5MuZP_T5fzRwQHwzscEzu_J67UdDiLgDi4hXDyhSmm7ldNyPJi1VW11lBnigvqwsImKboC41Img1yjzyqkK6cCph26i_uoFmlHU6yi4gOZ4cyEYS61tvbBKw2FC1DBOMwDVnvP_n1eiRNNsGLM79cVD1ELvdF7odgJkJXa68xcEfgUtTdEKVlbNsQEwcTlxmjhVQKv7RVAlqSyLrs94dEW3vetcEliM2uCaa2Yi30cklDyIVbkCD11ponxwL4CLbVGmyNP6JU31Pn89iWL4J2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29eaab8d0a.mp4?token=kG5FkHiYd3TzJXP9cH_2hdI0E6IX2D2QiWCECfaYVO8fR6Ihiat0hC7fUv1pgh5k5MuZP_T5fzRwQHwzscEzu_J67UdDiLgDi4hXDyhSmm7ldNyPJi1VW11lBnigvqwsImKboC41Img1yjzyqkK6cCph26i_uoFmlHU6yi4gOZ4cyEYS61tvbBKw2FC1DBOMwDVnvP_n1eiRNNsGLM79cVD1ELvdF7odgJkJXa68xcEfgUtTdEKVlbNsQEwcTlxmjhVQKv7RVAlqSyLrs94dEW3vetcEliM2uCaa2Yi30cklDyIVbkCD11ponxwL4CLbVGmyNP6JU31Pn89iWL4J2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخعی، نماینده مجلس: بخشی از قاچاق سوخت، «رسمی» و با مجوز انجام می‌شود
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681150" target="_blank">📅 17:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681149">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
وزیر ورزش: وزارت ورزش وظیفه ای در قبال ساخت ورزشگاه برای تیم‌ها ندارد.
🔹
شورای تامین استان خراسان رضوی: در درگیری دو هیات عزاداری در مشهد دو نفر مصدوم شدند.
🔹
ارنست مونیز، وزیر انرژی اسبق آمریکا: ترامپ با جنگ ایران، آمریکا را در بن‌بست انداخت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/681149" target="_blank">📅 17:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681148">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
ساحل شیب‌دراز قشم از آلودگی نفتی پاکسازی شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/681148" target="_blank">📅 16:57 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681147">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
طلا از ویترین جواهرات به قلب هوش مصنوعی رفت!
🔹
گزارش جدید شورای جهانی طلا نشان می‌دهد که تقاضای کل طلا تقریباً بدون تغییر و در سطح ۱۲۶۹ تن باقی مانده اما ترکیب این تقاضا تغییر مهمی کرده است.
🔹
این گزارش می‌گوید که تقاضای جهانی جواهرات به پایین‌ترین سطح از دوران کرونا سقوط کرده است.
🔹
جواهرات تنها ۲۷۸ تن تقاضا داشته‌اند، در حالی که مصرف طلا در تکنولوژی به ۸۰ تن رسیده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/681147" target="_blank">📅 16:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681146">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z66LeohsuY35PCft0wa3PrdGQvP96AOdMncZ_-kZP3zalLL1t2Gu1zCRillxk_pQ1a-gKZJXthQV7U9Y-NOJOBv_3IthRErlV10UsfJ_CdgpYb0DkOYIxbOng3xNcFLLzQ5_mixrPWIEV1hRn-C6LRbKDUMFc0SK3gTKlhMxVRSyDaz8dLy6JJAUGRL_pHe7gxxd4ISrbwhHKVQ1c4GboWdse0yvmwgMgPt9hLeIHEeeS1jybPGmDRXSspE7Ho9mN0B4kd-FoaMwUEzjrb6gWHDffItp9pbq3qpdnl1_AeYKJLD9uq5pNKiWnj9wDGFiTE9xuQmJDsKZYUlERAFFVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پایان پروژه تلاوت کل قرآن کریم در مقام‌های مختلف توسط حامد شاکرنژاد
🔹
حامد شاکرنژاد همزمان با حلول ماه ربیع‌الاول، از پایان پروژه تلاوت استودیویی کل قرآن کریم در مقام‌های مختلف خبر داد؛ مجموعه‌ای که به گفته وی، برای نخستین‌بار در جهان اسلام با این گستردگی رقم خورده است. انتشار قطعات این مجموعه به‌تدریج در بسترهای مختلف ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/681146" target="_blank">📅 16:53 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681145">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e043d4302a.mp4?token=l0wMvotV6P7mCver6NtFCvlU3tM4Wiwqra-yfZmE04sYcrGXKr4O93BuP8IDjMSazQBSCBNcIvwh7YAFfkRT2nZ9CLUFY_9vhRkfvEOXazdWISbbzBi4FeJ4jDRMyyAFOTeQ0xzicMCNwcytBC0RuOZ6DWtceEbqzumb-CXaG2Jte0CIitDCKocrETq6Sl8UqgEuGwvdjb22YcL1tBESn4KP8teGfz6d4Wkv8QbI-mmnqMqllD4gzg6GJ98zVBEBS4qBv_cJ-eV7lrQdmM5lVbX84PlNsLo-LDbm0ExWJYn9CgPUfIFqYRzmioMKzfXxYbgH1WBtg8sA6HKxGC0ldg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e043d4302a.mp4?token=l0wMvotV6P7mCver6NtFCvlU3tM4Wiwqra-yfZmE04sYcrGXKr4O93BuP8IDjMSazQBSCBNcIvwh7YAFfkRT2nZ9CLUFY_9vhRkfvEOXazdWISbbzBi4FeJ4jDRMyyAFOTeQ0xzicMCNwcytBC0RuOZ6DWtceEbqzumb-CXaG2Jte0CIitDCKocrETq6Sl8UqgEuGwvdjb22YcL1tBESn4KP8teGfz6d4Wkv8QbI-mmnqMqllD4gzg6GJ98zVBEBS4qBv_cJ-eV7lrQdmM5lVbX84PlNsLo-LDbm0ExWJYn9CgPUfIFqYRzmioMKzfXxYbgH1WBtg8sA6HKxGC0ldg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مسیر شگفت‌انگیز راه آهن دورود به اندیمشک
🇮🇷
#ایران_زیبا
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/681145" target="_blank">📅 16:50 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681144">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
استعفاها در حزب نتانیاهو در پی رقابت بر سر کرسی
🔹
کانال عبری‌زبان ۱۴ رژیم صهیونیستی با اشاره به استعفای چند عضو حزب لیکود نوشت که تنها لحظاتی قبل از انتخابات مقدماتی حزب نتانیاهو، رقابت برای کسب جایگاه و کرسی تضمین‌شده در فهرست لیکود، منجر به موجی از استعفاها در این حزب شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/681144" target="_blank">📅 16:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681143">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
سخنگوی کاخ سفید برکنار شد
🔹
دونالد ترامپ، رئیس دولت تروریستی آمریکا در اطلاعیه‌ای رسمی از برکنار کردن «کارولین لِویت»، سخنگوی کاخ سفید، در پایان ماه اوت میلادی خبر داد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/681143" target="_blank">📅 16:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681141">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH9apSm7QrcxKe8tRgtsQTvQjxXAdMf1DVZrNqRIdY6SnJsrjUnZHx_lIxGqSzIhenKh4BoJc1tshcdKb3Q4rQLjk6MGqls-pd-NDqDeXBxSU9G0Z-n7LnLgifuphY5fAjdVi5Uc3bjactfb_0Sgwr_uRKzj1B-p4W5umqkHICxPMBSRN9y4wjTvR5-QBAhmAUPuHK2HewiSvlAJDJkqkIcVs7A9ZX7AczjnD_-xz4vnqQmOBDBKDNS_UhALhHvCn1w_PxnZvQ-VNyquJE6S27yEYfqCubmnPbCtvQH3YA0gNImq1os3bzPJy0v_C3mWGcxtc9OlS4cAl4NjmH9h2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زنگ خطر برای یوتیوبرها؛ درآمدزایی سخت‌تر می‌شود؟
🔹
گزارش‌های تأییدنشده از احتمال تغییر شرایط ورود به برنامه درآمدزایی یوتیوب از ۱ فوریه ۲۰۲۷ خبر می‌دهند.
🔹
بر اساس این ادعا، حدنصاب تماشای ویدئو ممکن است از ۴۰۰۰ به ۸۰۰۰ ساعت و بازدید Shorts از ۱۰ به ۲۰ میلیون در ۹۰ روز افزایش پیدا کند.
🔹
هنوز هیچ‌کدام از این تغییرات رسماً توسط یوتیوب تأیید نشده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/681141" target="_blank">📅 16:17 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681140">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsVDZyQumAOv_8VkYcUqbPc05egb-LfuEbSB8rOPAsaVHu6h_kxdP3PDV9hsygbTlU6d1XiPRjlkU4Lc1Uo0bX9LezcgEdX5kltkBkYc0jHuC2785_lTSbjRK0CljVmccovlxbJeoVu21M8OTNkkvJz0UHcacIW86jJ09dChEpg8dRrSBELRgRsL7jHX8Xr6z3gxD1klJHUbfCZupF4HNLe2K85Cz7oCwAyVhdOipoIylDKYUQv-I4dnB9UcrMuaL_oXsBvBT-476E8eJY9AxpOyt1VA6GkZLSHdQeRY3oaFZK8Q-zBF9akNCkqGwAuVCQegQdPM1ECjdGvAOpZ6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مصر، ترکیه و عربستان در رستوران تحولات منطقه را بررسی کردند
!
🔹
وزرای خارجهٔ مصر، ترکیه و عربستان سعودی در شهر ساحلی العلمین مصر دیدار و دربارهٔ آخرین تحولات منطقه از جمله تنش بین ایران-آمریکا، راه‌های کاهش تنش‌ها و تقویت همکاری‌های امنیتی و سیاسی گفت‌وگو کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681140" target="_blank">📅 16:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681139">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال رسمی باشگاه پرسپولیس</strong></div>
<div class="tg-text">💥
از نسلی که ساخت،
برای نسلی که ادامه می‌دهد...
پیراهن جدید پرسپولیس؛
با امضای تاریخ
🙌
❤️
❤️
@fcpersepolis_club</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/681139" target="_blank">📅 16:11 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681138">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ_M0ktuP4muDWE_Z7G6BjgPeP2JypYYTlWKbZ88XhYu09t6PQYSiy8tTJJP4kSIif7VLId0YtEcjg0fuZZmMmREvqwZ7e-kg6H7DhtrSd2_Kgsl_8w8Tv3uTUTdpA51NAa4WgoLPbNgF1harmE0-8lTqU_s34-nkViEikDi2k7xLcjqP4C6QsErMCJTdBT3ctXBLzSNyPe-eo-dO4MxcpVNNNHe0HHLBRCd7K51urBMiwgofHiLNF91GNAEvn__2mR0ROlWV6ICblUk6hb89qFuDwMK9oKKeQCMZuHxFe2FEzlMWMbHPTSUQPCRaqIKFlibK1_Tmit1zIKz65NFwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موضع یوسف پزشکیان درباره حملات اخیر به دولت
🔹
برخی شمشیرها را علیه دولت تیز کردند؛ آنها سربازان شیطان هستند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/681138" target="_blank">📅 16:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681137">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک بحران بی‌صدا در موسیقی ایران؛ به آخر خط رسیدند!
🔹
حال موسیقی خوب نیست؛ پشت این سکوت، یک بحران آرام در جریان است.
🔹
۸ ماه است سالن‌ها خاموش‌اند و هزاران نفر از اهالی موسیقی، بی‌صدا هزینه می‌دهند.
🔹
اما این فقط یک تعطیلی ساده نیست…
پشت پرده چه می‌گذرد؟ ویدئو را ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/681137" target="_blank">📅 16:05 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681134">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
عملیات حشد شعبی برای سرکوب بقایای تروریسم در صحرای غربی عراق
🔹
نیروهای حشد شعبی عملیات امنیتی برای شناسایی و تعقیب عناصر فراری داعش را در صحرای الثرثار در شمال الرمادی آغاز کردند.
🔹
این عملیات شامل جست‌وجوی تونل‌ها و مخفیگاه‌های زیرزمینی تروریست‌هاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/681134" target="_blank">📅 15:56 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681133">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اول اصلاح مصرف، بعد اصلاح قیمت؛ راه توقف واردات بنزین
محسن بیگلربیگی،کارشناس حوزه انرژی
:
تا زمانی که هزینه تولید هر لیتر بنزین داخلی حدود ۸ تا ۱۰ هزار تومان و هزینه تأمین بنزین وارداتی حدود ۸۰ تا ۹۰ هزار تومان است، نخستین اقدام منطقی برای کاهش فشار مالی و ارزی بر دولت، باید قطع وابستگی به واردات باشد؛ نه افزایش یک‌باره قیمت برای همه مردم.
امروز روزانه حدود ۱۳ میلیون لیتر بنزین به‌صورت مستقیم وارد می‌شود که سالانه نزدیک به ۴٫۷ میلیارد لیتر و حدود ۳ میلیارد دلار هزینه ارزی دارد. با احتساب ریفورمیت و افزودنی‌های مورد استفاده برای جبران کسری، هزینه ارزی تأمین بنزین به حدود ۶ میلیارد دلار می‌رسد. ⁠￼
این در حالی است که کشور تا سال ۱۴۰۱ بدون واردات گسترده اداره می‌شد و در سال ۱۳۹۹ حدود ۳ میلیارد دلار بنزین صادر کرد. بنابراین کسری فعلی الزاماً مسئله‌ای غیرقابل‌حل یا ناشی از کمبود ذاتی ظرفیت کشور نیست؛ بلکه بیش از هر چیز حاصل رشد بی‌ضابطه مصرف، خودروهای پرمصرف، فرسودگی ناوگان، تضعیف CNG و کمبود حمل‌ونقل عمومی است.
راه‌حل عملی برای اصلاح مصرف
🔷
احیای فوری ظرفیت CNG
ظرفیت عرضه CNG کشور حدود ۳۵ میلیون مترمکعب در روز است، اما فقط حدود ۱۵ میلیون مترمکعب مصرف می‌شود. استفاده از همین ظرفیت خالی می‌تواند تا حدود ۲۰ میلیون لیتر از مصرف روزانه بنزین را جایگزین کند؛ یعنی بیشتر از کل واردات مستقیم روزانه. اولویت باید با تبدیل رایگان تاکسی‌ها، وانت‌ها، خودروهای اینترنتی و خودروهای پرکار باشد. ⁠￼
🔷
اسقاط خودروهای فرسوده با منابع صرفه‌جویی ارزی
مصرف خودروهای فرسوده گاهی به ۱۶ تا ۲۲ لیتر در صد کیلومتر می‌رسد، درحالی‌که خودروهای جدید داخلی حدود ۸ تا ۱۰ لیتر مصرف می‌کنند. دولت می‌تواند بخشی از سه میلیارد دلار هزینه واردات را به تسهیلات اسقاط و جایگزینی اختصاص دهد. ⁠￼
🔷
الزام خودروسازان داخلی به کاهش واقعی مصرف
خودروساز باید براساس مصرف واقعی محصولاتش جریمه یا تشویق شود. هزینه تولید خودروی پرمصرف نباید از طریق افزایش قیمت بنزین از مردم دریافت شود. تولید خودروهای با مصرف بیش از استاندارد باید مشمول عوارض سنگین شود.
🔷
آزادسازی واردات خودروهای کم‌مصرف
نمی‌توان واردات خودروهای باکیفیت، کم‌مصرف و هیبریدی را محدود کرد، بازار را در اختیار خودروهای پرمصرف قرار داد و سپس مردم را به‌دلیل مصرف بالای بنزین جریمه کرد. واردات هدفمند خودروهای اقتصادی و کم‌مصرف، ضمن ایجاد رقابت برای خودروسازان داخلی، مصرف سوخت را کاهش می‌دهد. بخشی از ارزی که امروز صرف واردات روزانه بنزین می‌شود، باید به نوسازی ناوگان و واردات خودروهای کم‌مصرف اختصاص یابد؛ زیرا خودرو یک‌بار وارد می‌شود، اما بنزین باید هر روز وارد شود
🔷
هدف‌گیری خودرو، نه عموم مردم
سهمیه پایه یک خودروی خانوار، تاکسی‌ها، وانت‌ها و مشاغل حمل‌ونقلی حفظ شود؛ اما خودروهای دوم و سوم، خودروهای لوکس و مصرف‌های بسیار بالا از یارانه کمتری برخوردار شوند.
🔷
قیمت‌گذاری پلکانی مصرف مازاد
به‌جای افزایش قیمت همه سهمیه‌ها، مصرف متعارف با نرخ حمایتی باقی بماند و تنها مصارف غیرضروری و بسیار بالا به‌صورت تدریجی با نرخ نزدیک‌تر به هزینه واقعی محاسبه شود.
🔷
توسعه حمل‌ونقل عمومی
واردات اتوبوس، تکمیل مترو، نوسازی تاکسی‌ها و توسعه سرویس ادارات و مدارس، باید از محل صرفه‌جویی ناشی از کاهش واردات تأمین مالی شود. مردم زمانی مصرف را کاهش می‌دهند که جایگزین قابل‌اعتماد داشته باشند.
🔷
پایش هوشمند انحراف و قاچاق
مصرف‌های غیرعادی، کارت‌های سوخت پرتراکنش و خروج سوخت از شبکه باید هوشمندانه کنترل شود؛ بدون آنکه مصرف عادی خانوارها محدود شود.
🔷
برنامه ملی کاهش روزانه ۱۵ میلیون لیتر
دولت باید یک برنامه دوساله با هدف‌گذاری شفاف ارائه کند:
* ۷ میلیون لیتر کاهش از توسعه CNG
* ۳ میلیون لیتر از نوسازی ناوگان فرسوده
* ۲ میلیون لیتر از بهبود حمل‌ونقل عمومی
* ۲ میلیون لیتر از کنترل قاچاق و مصارف غیرعادی
* یک میلیون لیتر از استانداردسازی خودروها و مدیریت ترافیک
با تحقق همین برنامه، واردات مستقیم ۱۳ میلیون لیتری متوقف می‌شود و کشور دوباره به تعادل می‌رسد.
اصلاح قیمت بنزین شاید در آینده بخشی از سیاست انرژی باشد، اما باید آخرین حلقه اصلاحات باشد، نه نخستین تصمیم. ابتدا باید واردات را با اصلاح خودرو، توسعه CNG، نوسازی ناوگان و حمل‌ونقل عمومی متوقف کرد؛ سپس درباره قیمت تصمیم گرفت. نمی‌توان خودروی پرمصرف به مردم تحمیل کرد، امکان استفاده از حمل‌ونقل عمومی را فراهم نکرد و در نهایت، هزینه همه ناکارآمدی‌ها را با افزایش قیمت بنزین از مردم گرفت.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/681133" target="_blank">📅 15:55 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681132">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی: آمریکا به فرار خود از منطقه سرعت دهد
🔹
آمریکا را تا شکست نهایی رها نخواهیم کرد.
🔹
امنیت مردم ما را به خطر بیندازند، امنیت آنها را در سراسر جهان سلب خواهیم کرد.
🔹
آتش‌بس را در جنگ رمضان آمریکایی‌ها التماس کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/681132" target="_blank">📅 15:49 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681131">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی آموزش و پرورش: آموزش در سال تحصیلی جدید به‌ صورت ۱۰۰ درصد حضوری است؛ تقریباً تمامی مدارس آسیب‌دیده در جنگ تعمیر و بازسازی شده‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681131" target="_blank">📅 15:46 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681130">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
ادعای‏ وزارت امور خارجه کویت: ایران به دو نفتکش متعلق به شرکت ادنوک امارات متحده عربی در حین عبور از تنگه هرمز حمله کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/akhbarefori/681130" target="_blank">📅 15:45 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681129">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📍
رستوران پدیده شاندیز
وقتی یک طعم، میتونه فاصله‌ی بین گذشته و امروز رو از بین ببره !
👑
⏳
وقتی پای غذای خوب وسط باشه، ماجرا هم عوض میشه!
😋
📱
رزرو و هماهنگی : 09153181815
📍
آدرس : شاندیز، نبش ولیعصر ۱۱
https://www.instagram.com/padidehshandiz.restaurant</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/681129" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681128">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TslVcvz8559YgM-7qVGtB4wQNszUP7WmfhgObXsou5Sj20R_G0i8TQGZPYt1FAaVCSj13bIXn1iQfzAUuD-q7tld_wB8zGWj6ie37V-RXqqIRUFeO-7A5OJU4g728e8cvqIuuqZZGrUmeR1kSlo-DYJLdocK1MZTNVEbURl-C6PQjnMyDUv9YqdbzEj-olkYlfBEmc9EFb55YzEjF_tod0cgAb6vP_hjnFnseZxEIeMhVu_Jr2CNXDQgKZwu4-N4GvGtIglc_6cDBxLLCPBz3I1hCbQr1YVKT93Ed58a4Yt2ejIKYIa-fR6iOS8RBZXwiKIG5uYzANJEI2mH7Jshag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
منشاء بنزین ۸۷ هزار تومانی در کرمان مشخص شد
▫️
خبرآنلاین نوشت:
▫️
پس از گذشت ۲ روز از موضوع بنزین ۸۷ هزار تومانی، حالا مشخص شده این طرح مصوب شورای تامین و ستاد مبارزه با قاچاق کرمان و استانی بوده است.
▫️
از آنجایی که سهمیه کارت‌های آزاد این استان عمدتا قاچاق می‌شد و به دست مردم نمی‌رسید، استاندار از مرداد تصمیم گرفت کارت‌های آزاد را جمع‌ کند.
▫️
با جمع‌آوری کارت‌های آزاد، سهمیه این کارت‌ها در قالب ۴۰ لیتر سهمیه ۵ هزار تومانی به کارت سوخت شخصی مردم واریز استان شد. برای مازاد نیاز بخش اندکی از مردم استان هم استانداری درخواست کرد بنزین با نرخ پالایشگاهی در جایگاه‌های سوخت عرضه شود.
▫️
جالب‌تر اینکه طبق آمارهای موجود با اجرای این طرح در مردادماه، مصرف بنزین در کرمان ۱۲ درصد کاهش یافت و صف‌های بنزین جمع شد و دست قاچاقچیان کوتاه ماند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/681128" target="_blank">📅 15:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681126">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JVmV-lIZtL7meSEAUktDDwD6X6NoAdykP-o48OEMPD7ZB4PHjagA6kWdOkEliCVrUiQ-RY93UOnyvEcw6qeNCbtp4wZhFI9mAtc09QnNMZA9itzURDlngAqGh-NitO4o_bxCakcXwek9gXIgodWjq3mhNkbT-yUp7YovHpGVLjfMSpOStD3zUMzrZf1-LuXxQjJIf-kO4tpjwvHDUQcWP6TgkwTH0lCUJQHjiBPvapcxjDgTHDDshhjvLKlOcUI7S7JygTrUD9SrYIul_aWA0ghaYoXEUnJbBdjbMJwpKwyK9IMwTND4ifsqHxYSiozVy5nyBpq9wGjdJFGJX4Z4ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارس: روز گذشته ویدیوهایی از برخورد تعدادی از عزاداران در مشهد مقدس منتشر شد که در آن چوب‌هایی به سمت هم پرتاب می‌شد
🔹
این فیلم‌ها بلافاصله با آب و تاب فراوان در رسانه‌های ضد انقلاب دست به دست شد و به نادرست القا کردند که این درگیری در صحن حرم مطهر امام رضا(ع) رخ داده است.
🔹
بررسی میدانی نشان می‌دهد که این ویدیوها مربوط به فضای بیرون از حرم مطهر است. در داخل حرم رضوی، اساساً اجازه حمل هرگونه چوب داده نمی‌شود و محیط با بازرسی دقیق کنترل می‌شود؛ بنابراین، نسبت‌دادن این اتفاق به درون حرم، تحریف آشکار واقعیت است.
#اخبار_مشهد
در فضای مجازی
👇
@Akhbarmashhad</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/681126" target="_blank">📅 15:40 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681124">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mj8Rn5vLvpWApt8RB0PIbhP08rS9jTqz3jXweCwFHrm65WpAeSVq2lnMUFDvn7rbZBI8oVa1oXnXG4vbKgWHpibash1EuGI2YFMsH2hGLEsKlMyVDAnPGAtlIaGKzBS9OfcQikK3qAo-JmdNAvpU4v-8KLZarTe0BBdGe1aQONhYzOQjyCwIe5j8G5ilixYUjEhiL101Th8m3pYTRVKN4TVIKaqOFusGAg3Rrf0vuN-HrWcYnYYmjjRoXjhclFS2HjLRo7CrWlzNpVNDQt3Bu0B9wSkhAAVsN_mzrVbd6H3QJ1EFFNlheE7SBJm4R9PU9VIWufwQTF0ZymqKCY8uTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rR9lLTdehCauDrjV6WFjv6a1fzSHFwg-T8NaBB5iUvuJBEc3jE25MwZ-KqyyNCsaRCcuIhNWm0UY3Lw9edv83j_CV6lmMchyzR88HAHk69w-mgn8HZPERHpzG65uOaku2wUIt7DOzKjXOD0cCMSAb9kdjvX5PA_m6j-WTLaj4dMdw1so2bhs5LuMpC0JzxZFs02QEmop70ggjvbExY9lA_nw13-fYr6F9CVaNmWkN9H8hjkf3WJAGadfK-5P5XLHM-qN1KCKxXtCQR5qNj2EI7PmHUog0El6KhdsDdk80wVECMLMparbtheVaG2LeX3FpRmrJ6lAwcK8JZiTqz3vPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میزان استفاده و هزینه ماهانه کاربران ایرانی برای فیلترشکن
🔸
بر اساس آخرین نظرسنجی مرکز افکارسنجی ایسپا، ۷۴ درصد از کاربران اینترنت در ایران از فیلترشکن استفاده می‌کنند که ۶۶ درصد آن‌ها از ابزارهای رایگان بهره می‌برند.
🔸
۱۸ درصد از کاربران ماهانه کمتر از ۵۰۰ هزار تومان برای خرید خدمات فیلترشکن هزینه پرداخت می‌کنند.
🔸
در نهایت ۶ درصد کاربران بین ۵۰۰ هزار تا ۱ میلیون تومان و ۶ درصد دیگر ماهانه بیش از ۱ میلیون تومان را به خرید فیلترشکن اختصاص می‌دهند.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/681124" target="_blank">📅 15:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681122">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNn-Y6KdaZXkkhdfUepz4YoITvk3VHPY9gyPyruB9icn9sAiiRMVisFCooqktrWJt1ZMPiIl0e1I27Tt2ENkXGevUsOdT_NcDz_3XWRFPO0w9lUvD0LbYqVuwwP6WYUwQb6WAbj-_CERk9D-1dfEJZxuKCcqHOznA4yzy-aj2cvPo5dyleYpji2aU2gLAVrv806_X2i00ePPGO2pHgfpD3MG_AACqdvV8C_61YwfJhKVdNizSyUr2ZBKTiCvXi4iwHRGvKKy6EYPHh-31w1jusEXgN2A9kbZgyAy4fl8o0moekgBCsoOX8wCsUIRBWEyuWy_iecPywReNXUYpSa9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: مذاکره‌کنندگان به توافق با ایران برای باز کردن تنگه هرمز نزدیک‌تر می‌شوند
ادعای وال‌استریت‌ژورنال:
🔹
ایران و عمان در حال نهایی کردن پیش‌نویس توافقی برای بازگشایی تنگه هرمز بودند که به تهران اجازه نظارت بر کشتی‌هایی که وارد خلیج فارس می‌شوند را می‌دهد، اما اجازه نمی‌دهد عوارض یا هزینه‌های خدمات دریافت کند.
🔹
طرفین در مورد نکات اصلی پیش‌نویس که یک خط ورودی در نزدیکی ایران و یک خط خروجی در نزدیکی عمان ایجاد می‌کند  توافق کرده‌اند و آن را با آمریکا، کشورهای منطقه و رهبران ارشد ایران به اشتراک گذاشته‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/681122" target="_blank">📅 15:29 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681121">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfLYzcHXrGcH7VjsTN6eqSgCNcqEu62csX2m9yek5vBcrOZqbD2dTRUjcDU3LfmchOijZOrW--9x93wavi9ec4iwhp85tqHQR6YMPwZL8pxsPBW2ZjAeG3bSZYIQeoCOQUGgftUHm2IfNrjAfk4NyyfvVqcezyuOqVq8yZxv6fMsnj5MnwUG6E0jdNdm-nE_PTh4N1X4zm-fXMNWvW6yIWK6egb0u50Nu2BYBewKdmvAmeVz4tXWayfbUBeWjaUUq24l-TP65DwCLp0kuS1OTdxKddCJbhrip-in6PQgI3jWEQzIIc9DGS5RI0AJSioGBR5qIBNqXgwkUdTDWBuvjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توضیح رئيس مركز ارتباطات و رسانه آستان قدس رضوی پیرامون ماجرای منع شعار مرگ بر آمریکا در حرم رضوی
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/681121" target="_blank">📅 15:28 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-681119">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa699bdd56.mp4?token=j_VxKRFA2Y3Senk609xQn2k-fuUjes-xPp4qcFcPkkNl9Lc3Tq6HzShd-Hh4F6B_RxYEQlEsTe5gHmjS3Zx5thhmYO76GD35Axmb_IVeVixOfvOW1koyIOT-F8W7xjDkZw7SmWThaSytob-OWoamsEGs_AQTmoE6tn0oQyKO0uDLQoj_ay0xzdLPKKEmlgK6xOCg4vf1SOBHaRHdr4LRAfs8y55ob2rhdF9VOSL7hs5r8dTa3RtBNs3L3PwWgJg7N8wzXOzxQskachXvjFUrq8LhMOOVSwntjMnTU0Oyh4sgkhh0CtsQIHsxW6AbvvEUdm5OUsJ3STWEKM-4oEXWPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa699bdd56.mp4?token=j_VxKRFA2Y3Senk609xQn2k-fuUjes-xPp4qcFcPkkNl9Lc3Tq6HzShd-Hh4F6B_RxYEQlEsTe5gHmjS3Zx5thhmYO76GD35Axmb_IVeVixOfvOW1koyIOT-F8W7xjDkZw7SmWThaSytob-OWoamsEGs_AQTmoE6tn0oQyKO0uDLQoj_ay0xzdLPKKEmlgK6xOCg4vf1SOBHaRHdr4LRAfs8y55ob2rhdF9VOSL7hs5r8dTa3RtBNs3L3PwWgJg7N8wzXOzxQskachXvjFUrq8LhMOOVSwntjMnTU0Oyh4sgkhh0CtsQIHsxW6AbvvEUdm5OUsJ3STWEKM-4oEXWPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هموطنانی که در خصوص کالابرگ، پیامک احراز سکونت دریافت کردند تا اطلاع بعدی به دفاتر پیشخوانِ دولت مراجعه نکنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/681119" target="_blank">📅 15:25 · 23 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
