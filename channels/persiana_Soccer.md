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
<img src="https://cdn4.telesco.pe/file/Wa72znTc0EAiX1Q8iXwNxy3w_zHlndu3ObAUQKA4MG-C1kxsL0LOidTFuojE5rkx4eoK5p-4radGtz0bUugbut2t5ZPdac8MCaaEXdcrcscvfq5g6x12FMhYrMwru0mYBSbTqCH0GRK773fCkTAlOCeeZr8eSkgYa7zPUD0JbN8fJu-PJSEemJW0YuI45VJhEI6g8774upu0m_4n_AjoMxwmF2MzDBbnATW-2h0bFMv8gljjuT_G4ndRzirxT23jrijHlsyGsxfhaBpoKRjzKyV5MYg0bHvt6yz3AECC994SLXAam39sHucohv69tNOHkzqSK0Wo5oL2u5ziTEMm7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 521K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-22 11:03:22</div>
<hr>

<div class="tg-post" id="msg-29652">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال در روزهای‌اخیرمذاکرات مثبتی و فشرده ای با مسعود محبی مدافع میانی22ساله خیبر خرم آباد انجام داده و قصد داره با او قراردادی بلند مدت امضا کنه و نیم فصل به جمع آبی پوشان پایتخت اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/29652" target="_blank">📅 10:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29651">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/29651" target="_blank">📅 10:45 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29650">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5JGkW2507j5ep9vBAAUnbCvAr4c0AqSMdGqzw8RW2qFfjojuT61cGsDM8X5-uhW6XYWB0cLVPCRpclvjxOt3iSsVE6cHq5yCqOdr3k0tjidD6swT6eHZ4SqyTsRu03DsgBChzhFwq81VmJS0CukFxCK5CN1hQm68LL3Sporx_cNIp5EG34NtyU48dnX_Go_boYUqydscclL8-n8KBl8qTuBaieOyPsAYDb-SdZ-XAm628VU2km7VmV5nPh82Wy5_W1sI1yVPl_wrEaepNYZ6bX45M9FSFUp-I_NA6mDxLD-VNOwPk4LVfU_LdLwPSF3l-5BoexPW3YaZ4fzxlE0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌اسپورت:
یاسر زبیری مهاجم 21 ساله رن فرانسه‌ که‌این‌فصل‌قرضی سانتاندر بازی‌میکنه که در این 5 مسابقه پنج‌گل برای تیمش به ثمررسانده گفته رویایش پیوستن به بارسلونا درتابستان‌سال بعدست. بارسلونا از علاقه یاسرِ مراکشی به این تیم آگاه‌ست و به احتمال بسیار زیاد برای جذبش اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/29650" target="_blank">📅 10:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29648">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
#تکمیلی؛ محمد قربانی، محمدجواد حسین نژاد و مهدی قایدی سه ستاره ملی پوش لژیونر هستن که در در حال حاضر در تیم هاشون شرایطی خوبی ندارند و باشگاه‌هاشون هم درنیم‌فصل علاقمند به فروش آن‌ها هستند. به احتمال زیاد هر سه به لیگ برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/29648" target="_blank">📅 10:04 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29647">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379e42f937.mp4?token=cB54zHjYSI3yGrz7NB2xvDR6mOyMXVOO1RnsiyXwMELGgD9IoMsA1cgZD4E02lb9y4CBVgagSQXOSZNzwYLR6gWrIoU3OBZHw9dhDcOyjyuxHZUtwQssGfQk6Ro5voOczyKfjM3PxM8y-HjtlA9iGtEOmJandNLeRvMeSrVMtZdsOghaSParUUKqZ54lKRIp6COp-wlZzl1v7ZFnlmskP1eIPohSDNr30bEcmMmfj3dQV7G7CR5o1p03hH63HWSxizwjDOS8K9-sZCOtB2wMqbfEd8dEL0PpfPavVCbaIXeUddInT7JI5kTCCw_33QpbGJGoA7d94iyqhIeghPLkiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379e42f937.mp4?token=cB54zHjYSI3yGrz7NB2xvDR6mOyMXVOO1RnsiyXwMELGgD9IoMsA1cgZD4E02lb9y4CBVgagSQXOSZNzwYLR6gWrIoU3OBZHw9dhDcOyjyuxHZUtwQssGfQk6Ro5voOczyKfjM3PxM8y-HjtlA9iGtEOmJandNLeRvMeSrVMtZdsOghaSParUUKqZ54lKRIp6COp-wlZzl1v7ZFnlmskP1eIPohSDNr30bEcmMmfj3dQV7G7CR5o1p03hH63HWSxizwjDOS8K9-sZCOtB2wMqbfEd8dEL0PpfPavVCbaIXeUddInT7JI5kTCCw_33QpbGJGoA7d94iyqhIeghPLkiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آمار آپدیت‌شده‌از عملکرد کریس رونالدو و لیونل مسی در کل دوران حرفه‌ایشون در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/29647" target="_blank">📅 09:52 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29646">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=gl8Mo90Vbeav-c8cHcwq3Pn_NyMijd-BLb20V9pH_njjYiH6U1_ofE9jxrde2MD8EjmvaI8k4rxFLUjcph111r11xZX3lGHc6U9R-scNsNPdT8F04EksJV9w7T8EFZ_vpK_9DxTpX5GHzQa1OpAPBKqnrqQOQFuTiNedulwfRjUjS_ApLBCtH3h2XwhkMqfCEmBby9llr8G2VDakOk_kLJBqzMe1EeyOhkMkhrbyQ-ECCTLaGMptJ5Z7irnK9ht9Z_tQMrzdWcmjVGI0gWbuvgxyH_-tCHBMXZf1br3Csy8tukc_blH0eazjBPbF75wpjIbMjZhwTMQxIF4HjDY8GIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5a250924c.mp4?token=gl8Mo90Vbeav-c8cHcwq3Pn_NyMijd-BLb20V9pH_njjYiH6U1_ofE9jxrde2MD8EjmvaI8k4rxFLUjcph111r11xZX3lGHc6U9R-scNsNPdT8F04EksJV9w7T8EFZ_vpK_9DxTpX5GHzQa1OpAPBKqnrqQOQFuTiNedulwfRjUjS_ApLBCtH3h2XwhkMqfCEmBby9llr8G2VDakOk_kLJBqzMe1EeyOhkMkhrbyQ-ECCTLaGMptJ5Z7irnK9ht9Z_tQMrzdWcmjVGI0gWbuvgxyH_-tCHBMXZf1br3Csy8tukc_blH0eazjBPbF75wpjIbMjZhwTMQxIF4HjDY8GIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌احساسی‌لاله‌مرزبان‌درباره مردم ایران پس از اعلام نام او بعنوان بهترین بازیگر فیلم ونیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/persiana_Soccer/29646" target="_blank">📅 09:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29645">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLiqUl8e0VE7_meqnf-U0GO39UY8mmxe_n5o39gKyRkPUhCUO9fPfrLV-2HKgy92CeCxJQ49A22NaPOkRrP3LL_3RZ1xi5AZKPY6TK6eCPbbCXIdIvcUkWe2Ig5tN7zaBdy-i2TwQkm5K1r2kFexZ_mO10p_Sha-WmunAodeZUloH2Ru_eNJJ4ZTQ0DKwJdQlGeGdMP1ow2Y_FxGWk-hsvgKehIgki5Yi31XfaqRuVta9EHMcWZoPCkEwbeDvbVy4Vux-BjpPkp3LD2rlRMc6-iWPqFVdLOnpJmwSKy9HNyS5Gg8NyPUS9vnoQE3bWMTAWx14gtCMvSqSdPDRYATJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مصاحبه جالب و عجیب و غریب مایکل اولیسه ستاره فرانسوی بایرن مونیخ در پایان بازی دیشب
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/29645" target="_blank">📅 01:31 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29644">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔵
ستاره جدید الهلال افتضاح هفته‌قبل رو جبران کردند؛ الهلال امشب با درخشش ستاره‌های تازه وارد خود 6بر0 التعاون‌ رو شکست دادند. گابریل مارتینلی ستاره گرانقیمت و تازه‌واردآبی‌های ریاض دراین بازی موفق به کسب هتریک شد و واتکینز دیگر ستاره این تیم دو گل و یک پاس…</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29644" target="_blank">📅 01:21 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29642">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWR1ezl5azbA0IUEepBQbb5pc3OnilQYM6c0RS03QaOg73RwPGSUt04PJ4Hd7Rl23qVHWK2CMPR8hnQkzXM55qR_3MJ5Gt2Ac1X4Gqc76_uPIGQ21KRQMPNqJq7I5lMZvrS3j3l--GhycU0jPliMiX_6l4P8c8wtgi-4tJdEzGl5iZdWeLonHdP-MhP4Ifi-XmLpcl7jmislE-LfcNOVHVIzhxweoeCBR81lbRU0MiS5mHmvNArkY-XfiXfeys60k4onq4LrUznWXq2BuSFkVM_BXcn9EdCkga9urAlq2EqGOmub9CFDOCHu1w1CCS-5sVW6CghTrmWMjxkv2oFDHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛از دربی‌جذاب‌شهر منچستر تا بازی بارسا بالوانته‌برای‌تثبیت صدرنشینی در لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/29642" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29641">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROyy_grIL_iwd-ylw80wB4_JG9pyqu911iALxzTC7a5OhXrQ_VXCOGUuiofN77zBnwIX0h22Iz5lI0IhmagbBDw5zKJWrNLWdY7dnPmKG-RNAPYr-Q7mdoSSEPJHkwMdbpslrMaHXloA64okVOSLjW_ZWzZUpm-9oz1BDpFvHbztj63zMNCvmLrM9-jBzzJIPf1hRUvdddoRztd-P-bvuTymTwFQkUmGmMxicJhCe5YU7Y5djBNMqj3EG-bNKYcX1XwKYKd_8lNAPeaYgMhrdNdXaM8uXviCxvVzbQOJkWSSnFCgHzsmMj0EBPEod74I-uBKvqZm8a2AqOIPXGhNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف همزمان لیورپول، چلسی و تاتنهام در لیگ‌جزیره تا برتری پرگل شاگردان خوزه مورینیو در شب درخشش کیلیان امباپه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/29641" target="_blank">📅 01:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29639">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJKc20Lx7O5GCX1PGycQoHHc7V0w7irI8H8zb-I6OCSAjy7GqZnXFIm0yTzJApMkoGMxIsrOv_qqxlci-yJB-qtDL14jU2bLSVoBp4H4p2bu0rzOBouzTvOZvxIruYBVjr7TJxVbT6C1p-eLcP3dds38AxdgXyZTY-OYHl7IXly5DcVfg1g4nPd0BK71m1CDv5MxTEad0mqkjKk-75h-fce-X4T8Lcn_wPH1QvX2CclvHSW-IvAyapVH7Q9mjnCo-BfDAgmavGtZMrHj6L9n3VqdRk2-Mpu9eryvprwYh8BCdWyd_6Bn3Z6rrPDYDR_rXwkPCuxaUHCWTYZHaA0t4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
تصویری‌زیبامریم‌میرزاخانی‌ریاضی‌دان ایرانی و استاد دانشگاه‌استنفورد روی‌جلدکتاب ریاضی دانش آموزان ایتالیایی؛ روحش شاد و یادش گرامی.
🖤
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/29639" target="_blank">📅 00:50 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29638">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02bd31b46f.mp4?token=YnnSDhRCydSfDv0QbA31wwyHgG-NKj2OZGSDl_AXDi5oV6-8Xn0v-Pc9OlLTykZKibbr0TTz3NhZUElFiXAKeM2QQK5k7-7nzjQbCamUrn5GDGWqolAzrmIsqAJYQ7sFPAFkaW_vSz7ZZo2Xb1Ft1t0ZaZvu7E12sQ2pHC-liNueu9nxMVMUZf1beeDmUYpiWq-Gnk53VV0DTWRUb5x2r1Z7izVf0eCAMxrp6UCgzgIhZ6WQP7mikSoi2WYmwI0UFJ2_eFdK0ZdsA736aNsA4VEl0X5y4K6Usly1SfSAY6k-ilHpKML3boALFwd6a9ftBUIs6CVDj7c7IPTEVvB-xLoTqTvl37svD3uR7VFAndKQuXCuGEptj3coXOoQ9xUhPkC76wc46lG28YyWMCZpa6eoPuZijZvJwlqA-brEBR3Hvny2vKydAAWLCV60UibQfDVl-wpDfPFrqvDG4ndDV5ZaydLvg6HzG-0mY70vpqVJNAAK136rQMIkEiYXrb3CEeSS89boTvwLh8Il3bzrp5xG7scvKEpCyL-Q8qafwOS2aUFTBc0bLr79lxBNJ4vhfST0AGm34hskPn5NrinhFNV_FknR1gTPMzVSda_RIvF9ZZB1aSDyoDrNsTCvILyUIJY9HYPmiLh1Ovr4SULdEc_wCGf9oHn9A2TE7zW4IxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/29638" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29637">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TswQVneMtTudrcKXM5N9OVvXUoarEKFK2xPp44_dD3iVWPdY8-dVYtNj2foprWDSCnncrBHizUN8R84KNDbGHCEINosLpN2rNMd8xRoOgfLvjMxec3DM-c6r4NvGdPJlrwJmuDvvZ7rxNGLHuLA2LUhia5x-2m86jtvCBpNyJriMq0GBpMOphkF-mwk-t8BuVl7iNu_6qAsOycdBrBWz85j-z0sPlleRVJok4gvyU9Wt6R0Btqxpbm9_FP-QNBw6Jr7gDz4Z8oVo8skz06rL9xI8rDUVcj4QHgO3wavqRqPW2wUinOD19v9lCN2l6eLY_ukFDkpqV2rKWVclCMn_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/29637" target="_blank">📅 00:34 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29636">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EliCtPb4gwaQAmxBRED7SGgit58NBu_41NYR7ylauDVWJ7cnwI4YFP-qaGU4jHNrFh83JXAWPRZc-sfZszDeCX5ks2gXdVpPiVyRgmC6qE0E0eKAzsAarGTvA-miolKpT8HxsdID_vnUksyp_54BpVj_0F-fBp9_HRrhVnw5QZoj9ymZHYD9Z73uhHXSsBCPldbGPNbIRWM7SDp-PX5p3pSL9OmcAz1FyAQQgAIUlT8OkTOyHnJq796hjeiDvlbNnqaKH5a2U9iHnvziQZ1jwZcc_DRnT8-YQG6I3sbWEfDf9MsRQncfT0uUP7d1YBFSfEFkwtETqFsyksMGXaKPWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
حضورپارتنر وینیسیوس‌جونیور در ورزشگاه سانتیاگو برنابئو در بازی امشب رئال مادرید مقابل رایووایکانو؛ نیمه اول رئال سه هیچ بازی رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29636" target="_blank">📅 00:14 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29635">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCGr8jKIpBx575rtHIvYT9YQ1pgesv-UTJJeHkPk9upxmAkRvCT49n5t9wo67tbEcRS4S_tPf4VzYm8fGwQzqoHiSZqhQ-zU-t-mYFY-tZb-dPgcHp0SLzZNDDRRzjlHR9gXOWmVc7EARxVTcYM-dgS-8eH5aBDTNJfPuOqE5Cwl4ZbGlzKmFaPo9cuLMsN8ADPh3duVzQ4drcwfTDYSrTIbInZsvIe2S6rcOsxZsYHNI465rLeO0M48DHk3d019DU3Ljwi5bdQY7a9h87M44SdySWLyzEt3EHbbm_-1-O5HGGPn9yrMU_XL0OrWvFw6aFUVYQxkU6xokLapDOsetQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
تایید شد؛ بااعلام‌رسمی باشگاه استقلال و با موافقت سهراب بختیتاری زاده صالح حردانی مدافع راست‌آبی‌ها به‌تمرینات‌ این‌تیم برگشت و در بازی روز دوشنبه با السد در لیست آبی‌‌ها قرار خواهد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29635" target="_blank">📅 00:01 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29633">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjia5uq-MhhS4ftW87KkhZ74bMmfzDC_efNZtJ8U-NSodqyq7y3gVm2Wy-SCtdg3G0V9FJoDLJQjjDA38pdgpEp8XeFZZSBiW5n6zmX1jfNvXqKBg39anddg3UjKexgB5VslW-ANfxzmYT3JqRTjUFb18fk3X0-N_PCLXye7INkqvLCaLQ_nwBBGMmWEk63rNIxz7Yox5p8x1vXiHjagv_AmBsGz-cvMZ-PBfHeWin2ov0yQiMtPuB4VWq4IR91KSA4ovF3DhN8gDbt9Ccih_VFKUsOoHlHG6xuLGSZcoh56wffgZ96AAoQYvbEUzuFYE1huxUq8cnYvx4dgq6RxZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛قیمت‌پلی‌استیشن 5 پرو دربازار به 310 میلیون تومان رسید. بهمن ماه 45 میلیون تومان بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29633" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29632">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdKM9QU9ZxmBA2W1dmAnFUwXYRlKK62vRPbZQH9y8zGG36_WYjvacURzJRJm-Kw-mhjgm9LRNo-UXIu8cQiXl6AIWECIqqcUPb4QuQuGv3aGloItjqx82TpHI4s6PvWNu0lmdboUaNuSXjOx-veyedDPWaWoRpvBnzn7VueU20oeL9ZuZgmAVCFiQBys_dylpirt_z3XPM2XzrMPtbfEiYXoeVBVuSwiukAsIqlnMz-HTUAAAftX2RCYWUXhD1KpUEZ67FsOOkpKOImyXNekkNvKaZFcbCilqYJrot7eaYDlDVnEkzJk3BGrY4lBe9cLWBe_B-m-IDxikdZRIeJaIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
بااعلام فابریزیو رومانو؛ مارسلو بروزویچ ستاره کروات سابق النصر با عقدقراردادی دو ساله به ارزش 12 میلیون‌یورو دستمزدخالص به السد قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29632" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29631">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UKYotUMAuukXjsXYc0KcTIcodDMywiRbJ5DdsX9zgzf51v04vI8P4Xgb9PhI3N6Oiyrg40cJDcdLnTzKDibEc3AsvknNOyQ3ezyDj5l1WyOCAs23lkTQzhl-nfkRdIn8Gu05qZF5QnXPLaBNwgMOgYus5WPl0pwdzBknRHrJf5BzCYZVNdyTijv99rofZyj3s3aaGPiRHy-yNMU7AdBTZEplOmWhCAUbN4l7af9jZkU1otRS3ZYKiuksMyMmy0mW5s0CzB_uj4NOoUTEwWkDym6o1uyfIIpAs_GKA5FUkE1c_cIzcfvgrCvSDSWMvKi44_DY02jTVlEuAmUxLlWG2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زگیل و تبخال تناسلی درمان شد
‼️
ویروس‌خطرناک‌‌که اگر درمان نشه تا آخر عمر داخل بدن ماندگاره و عوارضی مثل سرطان ایجاد میکنه این ویروس
❌
HPV یا زگیل نامیده شده.
⭕
درمان کامل زگیل و تبخال تناسلی :
1️⃣
زگیل تناسلی
2️⃣
تبخال تناسلی
☑️
زیر نظر سازمان غذا و دارو
☑️
بیش از صدها رضایت درمان و آزمایش منفی
⚕️ آیدی  :
🆔
@hpv_help7
⚕️ لینک کانال کلینیک
🩺
@hpv_hsv_clinic
📞
09212046421</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29631" target="_blank">📅 23:54 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29630">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vOe7GecJu46yKd0Uofh8kvtUuDRy7VerEZHYLdUq2yrbyYqbxJlqNnkcx2oRyn5aP_MFkk1OaGQ1095QXSnrEEDN2eDH8nbbd_HCjCQuT1CXoELyViPFx1eD1h8QsimZKnZ13zsiYkKXu_KOvF_-89P1y_4qkFEmLjMJHP3Ae-mtkH5T53MTbQXz3_iEPSY_km6WxUTXRziXvby3YEqXYYgT-feZD1ifl7UWAc9QcRdAJJi9uI5x6pQUfkKW9Js4giI_JyhKGff4xpxO7GqOu9KczmfqJ-z-ac4mzVlcdi8KQtBS4CSMYAeykFAG_ddtWfNEDBLYHkvFEiKqWgqsyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29630" target="_blank">📅 23:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29629">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CC959Taa003IPFySKAz8BQRl0W3BZvvjrR_9R_-Oj0hBBtfTT9l8wp6MeyotBZBxcUzPCjUxM8B3OfMmP4Dz0IWnx_aVxQqYRtnU_F8gMqFCC0McW_e9qbSbV5QV2pGOg7s3fkVR1o7y4JDtMBwy-YweZ_Psoxv82T073sJW50ig7XhUy4q2h1tJWKRNX4kutgU9F9g3RanmUDB49ztSHcGVj3JlO5DvZs9CnKGDdvv_y6uNyWB102E8F7Xgvmu8oWCmGpGDGoD-XnLrALxArsgPnIGJcetEtLAO7u5XN8gSmj1KaVKyBvAVMALUJzU5N0CuFICALtHEVxc66nsv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛طبق‌جدیدترین‌شنیده‌های پرشیانا؛ باشگاه‌پرسپولیس بامدیریت‌باشگاه فولاد برسر انتقال ابوالفضل‌رزاق‌پور به‌جمع شاگردان مهدی‌تارتار در نیم فصل به توافق رسیده‌اند و سرخ‌ها با پرداخت 150 میلیارد تومان رضایت نامه این بازیکن رو میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29629" target="_blank">📅 23:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29628">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u8G7Qq5EhO_k3HE4pzsYikulMUivk39sS0T51vC0leg8N8kd-wqWyzdz_VcBOt4XFbUDoUE7Ro6fYAv7gUGrpWByaa6i9tx9Q7SUSm2EZX1G8d4UD9L23EJKgWIDsbzkT4AUeH8U5XKIwfFaOBvnYFj7b1MhOgH_iKxBNDO2C26a0fxqKeamzkBIZZ8O2_B25Nr3kkBfNiAis3NzlI9iofE1J-9PF2NrbGbDXSQ5_fSop_VlybCWlzSFQ49UDLif_91k0WV65FZOWQ7K0EFuY9sm2A4EpQzizBXoSlSDNE3hV6VW_hQPhmMAOLPCcs0mZMDWbzYNkbwsodmwB-U3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌جدیدی‌ازبهترین‌برنامه‌های‌هوش مصنوعی برای تولیدمحتوای خفن در اینستاگرام؛ این پست رو یجایی ذخیره کنید به‌کارتون‌میاد و برای دوستانتون هم بفرستید که اونا هم ازش استفاده کنند. عالیه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29628" target="_blank">📅 22:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29627">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ownGveQDic45xZKjX5sXRoLq_5slhIQZ02dcApUTwrtjzSOjzgUEYeYkL-ejUqo5phIoco7szlBZo6zB5MJRxkjc7FaUOhsWHbAdShijKf0E4RzwERF1R8BxyNGzaNAI0n59pkVaCZTcif8_zZkotKcrAQnPKMid6BOBI7XpwOmuLPQg2c3iT7dMejGprmZ0JIygK3aXquohNEiF79XcQGLVU_elWvhdd9G4Fu896vBfy0RlQPB_toO9WzziW6Bd9llW4NToSh5W4FJ6z7S8W_ywWsSfy6vHRMak5Oirm2FixrY0u5hs8yxU77bFmuio5bo3Nf1tayHC6zHAV25Epg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌اخبار دریافتی پرشیانا؛ باشگاه پرسپولیس بزودی با پرداخت 250 هزار دلار به دنیل گرا مدافع راست 33 ساله این تیم توافقی قراردادش رو فسخ خواهد کرد و گرا از جمع سرخپوشان جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29627" target="_blank">📅 22:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29626">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZpOdX51eVwFa5pIyZEQ5zNPVqqONHPil7qcRzXL7bENx4r7YE4cXADlrOIPUjjy5HZrhaXbGix0iijkX89FgOZda8JJYy5Qw0w84PVz_Fy5kTGBTMPdrgcZ-Td1nhi1P_9rVqc5tusDMcQsM9Ozw1ZyKPvW4ZxKj9rU2bVV4kaWyLg_lIrQO8uKDlYc9ogp1GmoTjKiZlh8S5dbtsghL2oqGfYeIAKAZzMCU4sXGWHgr6Ygm9lEsw282Kv-antcVb3CXRfCtpkCLObUzmmooNXcCUt6PxQAOkI_SVByhSbrRgaJaOLhBvXaS6Fx2ErnUHvCWzmjuEnnpbzUApMUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛ بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29626" target="_blank">📅 22:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29625">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2989e9b119.mp4?token=DyKnrB2gPhAmHjb0cKA-mj5IFlBtlVwkIXNsxtOK-L9ML_NlC1UGTdlkE1u98jsDQkMcRj5JHjhh0lu4BZwyo_7AyMjgZ2zTgHSqQmqpViNAGJSRcJhKHFK8MTOYW_BCZRoV0iSu93n-6BOp7116ExljQ9nRdDZZi9VInZLUwtn7rEWQ3M1miGZPqx_npO45eALV7e4OZMwHZsT13QItJtBEqJB_1pbNT6m7J3GCOsuR-jaIUyiOdyl5JJkp09jC9GeA_UxgyJF59Tj7ra5MYRsK43c0h70VPof3KF94Igk47fKuiTiA05gImMECXd473EvImS5X6CKfsrtd_OWnLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محمد نوری استاد جملات قصار! شاهکار جدید ایشون درنشست‌خبری قبل از بازی فردا با سپاهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/29625" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29624">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKn08gmiGcQ6LEN1bIgIkBt60YVa4j-qEIUkceWJcgq6nN8r53RsYbT4Q34lrRQ3SfG1frV3RcRknZGCMEo_GlkVIh3snj671a_z2tvM5e0jdPGy_wnuJHeJKaW74oeB_mXnK1bUyTnRKibxnVnICAEjnFiRKVrrauIsF23oykWWtQTVHaExuYLXaIuGUn6SvzlB-R3hfY13SlidaoA9afl8cUkQciarZmsdVYc7tCl-FrfMSx3D0n1iEkMG68pvjA1BwosXknMIFbbMzoJsPyBlVkPXlDaEQH8cNidWUiTXwAfQAefHbTrxKS41BYvD--FFw8dwoGTtAyxIenFuyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🔴
طبق شنیده‌ های رسانه پرشیانا؛
بشار رسن هافبک عراقی پاختاکور که‌اواخر آذر قراردادش با این تیم به پایان میرسه از طریق دوستانی نزدیک خود به باشگاه پرسپولیس اعلام کرده حاضرست نیم فصل به پرسپولیس برگردد. طبق‌پیگیری‌های پرشیانا؛ مدیریت باشگاه پرسپولیس اماده عقد قرارداد با این ستاره 29 ساله تیم‌ملی‌عراقه و درصورت تاییدیه‌مهدی‌تارتار این هافبک تهاجمی خلاق به پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/29624" target="_blank">📅 21:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29623">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRyOx2-SG3aCMBdt9mAr-9y0fud04g7cZgSJJgoU-NvjIdPESviSyXs47-WEhCaNau_dxnbhQnlTTKKQ-S9arEfNxsUDGHBGlOzrfPBwCu_iHIxqovBEMupSjDkCoS1KAas0eDX51FYx6uuNk-TgddnF-7rsWSP8wsT6B2t5gucxc-LfIXyTXCdejiLpEHUUHVcgYfl9QQK-muZC7s8XPKqaWVtntjsipMzMfGYOOXRwB3m62ZHklGpuznhkfXnhAK5cawH8JnarZLfHsc_3NqYIQk_3G3beEdEQ4OiSsCg-Jc_bEcZt4WCIXU6xRKuqb-XCbf7hAyDTSNsQHKEh0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گواردیولاسرمربی‌سابق‌منچسترسیتی:
برای تموم تیم‌ ها در چمپیونزلیگ برنامه داشتم اما هرگز ندونستم چطور رئال رو مدیریت و کنترل کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/29623" target="_blank">📅 21:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29622">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
توهین به پزشکیان در پخش زنده صدا و سیما: شما خودتون لیاقت ندارید صدا و سیما ببینید
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29622" target="_blank">📅 21:48 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29621">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfLSkqqO6vMhemse6qGacwrN1bnEvXhXBt1RUkpCOs9KhImG1-_HXwF9C485yatBmxf-Ja5AsEoH5rhQxHlh5fAm1nCzT2oWzpYUAcTUGWlej3wnxoc4HEiwVUtCpleNk68lb8YN3PlZF9RI9RHJmCM9sdps0dzbBW6I-XFGgVuIAO3QlWuYmCeGFPb5RQYt9ialQvzh5D_21pwWAR9yVbW4CNoyHz1ej6835NagwpSyuPlLQiUmPwkxb8pgHDHYQsxOZJhWWmVFH52sNDMA_aTBCXBxz5A9uP5ijkJV35-gyIqObEJjK_4WtUzM8ijNta4q8RcCWCsB4FdORDwwqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قیمت‌امروز انواع پلی‌استیشن 5 با دلار امروز که حدود 223هزارتومان‌بود؛همین کنسول یه هفته پیش 190 200 میلیون تومان بود! قیمت‌ها عالیه واقعا:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29621" target="_blank">📅 21:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29620">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL-DnRkEooXNA4SGjrQE6Rc0mFx3jLGa3BF4IC8bymZ-1q8EvUQ67Y9OGemNZrA2fx1rOHT83-rnNfCjTYOejaA1HrIdI3FP4g0TqUh7l2oRP8dTBP9Dg5Oj7oaAmZfYLF75y3fEy9uIGIuofqKJC0ohRimfkXloG4X_m4alMaCGUFeEmr4i-OLMu2NaJG1D-sX_6A_jEQWN2wJ2_nGcPojAYNWuh7zl-narRiOUdNXpq-uuuSThVrz_mNkmACY5_qVc00cK8mg4vXWrHQ2IHpOMZRkSz4Lw_9-P4Lp2NVeDeh5_fdILS5AtZkfc89JpNeyFkaD6gc7_YiRe2Tbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته پنجم لالیگا
|شماتیک ترکیب رئال مادرید برای بازی با رایووایکانو؛ ساعت 22:30؛ آقای خاص بالاخره‌خرید140میلیون‌یورویی پرز رو فیکس کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29620" target="_blank">📅 21:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29619">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHkN8c2jWx4QPEqtl-UBImkRRMmIScmEVq1GzB53WHzaSCKQ1wGpObfbsx2EnQDmEaX1m0IaCwa2C4T_g6aWdMgcTo0hXeqbTVEBIXD5OvO4fvgGrC5KNBRBjKLnjCTsKzG52VvgcXMek_nyaF_H473oOg8_VqrC4TeSgOwMTF580x2jL-S2natAeUznbQeOuwjKmBcLWdWH5L0xIcIAGk3U-yrCsxy6K4ydgPPiHEArG2ZEeztqkZZrug6sIj-rK8erqdD4YZjOCIruJkPmuy78l-ebHx7YGb3Fcv9zdJLKrOeW-nrkOWnDPxupYp_0AoMCni_QoIpuYS_zaSWJVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛ الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29619" target="_blank">📅 21:01 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29617">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWWmC_7JEIHb1Q1OWTG5ocfn7_RKOixI8ecIgGqb7wxE3D5xoZbuEqQcrltB605MnTJh_6TFbWUCjtjMW-yQonze0STQvN0Vzm1s_tmNoujzuLFhaFjbuwvkfDyyi4IKAKJ_g4avp5RGceqXSUv_ZCyWxiL84Sh2fIUU8dsZ0kcwMDn7qRgYPB4oD53HGFCf10Toeswo43F1cDgPNvCsA-l8C0ZEWeu6LlVPN8GLKGq-K7Jvj0-wWj8GM0nIk-cU7uqmUnaXOemeYiLbU9AdtX71NxqoD4xhvWThbeSozWcxymLxu20dcUQwhz5tLkg0a5RM7Q6smnB1xpTdD5y7aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29617" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29616">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuT2acNcIzHPgniOyVV6LtFjbPTn5U4Q6aNcfj0sJeKnCK855bdE5JEuQkw2CebGAUxMKXCwkA2KuNLYnL5-fZIzi6u0oR1fRIaal3YVFFkgtv__BfQPZalVOXrARUlGBrevPJ5k8VfDzL5S1s5ObushPNQnya1zCrlhQWGTkbosMPJDhcYlMe67qOT-ln4kR2hNlr4e_JPgOXetvLNrFxWyld3scMa881seVXZQEmypUQasz4y78x32EZnoaoX4SWlJtEM1s8SxtYyHXgdxPG-njmwu-TwK0e7THsfcZvHvvU_6svtA8hXNinmEnhavAbJgPWl7eig6QuJzPajWhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29616" target="_blank">📅 20:17 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29615">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6942e2257c.mp4?token=o_5ngxnpHMgxTiNddG-a1cwFVoXl2TXYgw_xvyk2JaE9ROBNgTrQNw_9nv78XbvQUqXvZPoI0-m8y9USrWMas7hOaiUjSoimqoeVZFQ_3Kb1IOJ003Ak3d47W0MqshPyyUF7KRN2W0qimkwX8ZdglWAuxymqqFXiz3pI9Lx_NR2UoUoP9uvoUOMmrPvUn0pNdm-7jv-MStG1zq_PutNg8MReyGfQ8csFXJ60SyqXz0QqrudfD85iHpHlhb6z3bI-t2YEXjAFtiEOOFEj3NwfGICkHkcPLNUWq8GVHTuYR-fOp4zTlNRT6na6w4-J9eGN7CTYLujOnRnInRNb38bzVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
گردوخاک اللهیار دراروپا؛ گلزنی دوباره اللهیار صیادمنش ستاره 24 ساله لخ پوزنان در بازی امشب.  عملکرد فوق‌العاده صیادمنش در فصل جدید برای لخ پوزنان لهستان: 6 مسابقه، 5 گل زده، 2 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29615" target="_blank">📅 20:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29613">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tT6havQfxjxr9tkuLTrmq2HtYjCAfSrHyPXYryhbDQqHmK9PENrI0QlEvkOTFgyJlDTXz_fqg0V8TMw0FnBe6Itq82EDrIY1FdKu6m57uW2kvR1lYqLZOEUmnloK591HPSCMyIgRQBeSiRr7XFyCnHhcIbF36TTwFSGRkpLemxPaGbWwnZQX59tJhj0lDoHNIvMU0Xe1E-82N2iuQNl2E9cWSbYvs5dwW_aWhz2AKvNUdJogGxO9tqhB6sZJo0bdLYanOIXRC6vOmMnk8uwXLNK-BEMKycyS0lMy58jxFSq-kxybaTuXX-WbcEoHvAR5uzbOoliy4_eqS41Rw96LKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLfdCT0u4dI8H738pjEK1jp17JpzB5Fb7L_e1PPmWLOxr28haozbwfJI2CIMCPqyn_QJxe6Eq1zOR1dTitu_HdyEIvc9jAOvYjNVfx0J60rvadLEl9HbD3TM8bLHpxuHgkHEik4wutc9yZ6AkSHNfKOm_LYsn9YyLU_BFFOOPbz5wvF69K9nGrlLA5qWy1V7ho6JewprsjllgfDoIMZClCOPxjm7a4caFyD6Hs-k2DPJzfQ9rix99nq8RlPVDHIdXaMz2m3CGiz9QMap5PvljX7qkeMaW6qbzrN4BNlvVe4u_tBP0z8kDPI_dWfr6tWzYiqqDFKoG9O7xQ0DDqNwtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
عملکرد مثلث هجومى السد حریف پس فرداشب استقلال درچهارهفته‌ابتدایی لیگ ستارگان قطر: اكرم عفيف: پنج گل، چهار پاس گل؛ روبرتو فيرمينو: چهار گل، دو پاس گل؛ کلودینیهو: سه گل یک پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29613" target="_blank">📅 19:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29612">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
سرگئی‌جاکیروویچ بوسنیایی رویادتونه‌که 3 سال پیش دریکقدمی‌عقدقرارداد بااستقلال قرار گرفته بود این‌فصل سرمربی هال‌سیتی شد و این ماه نیز بعنوان بهترین سرمربی ماه لیگ برتر انگلیس انتخاب شد.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد هال سیتی در فصل جدید: سه مسابقه، دو پیروزی، 1 مساوی،…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29612" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29611">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzI6MhehLPJJ2pvuJKhn98-WUM-7zrK_Ogr1hzJP5q1cb_NuXcqZRxrmi1mjGW5JqoOpUXeikq0rcT2GnAvhvX4TACeJZA_8Ja_wOi79K8pRv_bXoW8aoeLj2B9X87u3SSCf0ccF_AQmdC_sohvxyUFN2SWS7lRqLenR71N1XtSmDlhFU9XloaFFsBxgFdPTA_R1tW1M5H9TB2gFYOWYm3vYcTlUTa88J028Vb257mrwsWvbUOZdv6HEM9GOssPXER6UzYuvNPH7TxkOBGjNe4sLxomL2Qlg0c9CULb8SrUrYZkv81uvSGZpGhy52gns8qOowJPh3sdVxTLbatnVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرصت سوزی برگ ریزون لوئیس واسکز مهاجم بیرمنگام در بازی امروز این تیم در چمپیونشیب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29611" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29609">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdC85qbWZMQG1pJhLaJKHfimzxGMNG6s5UR3GocSKiACeo0xoC3PLGyyj4VA5xTNP8jcHM33sFyzAL8-8KRpx724FxNOp7nM-9flZGpX9MEwKeMEAGDK0uAnkhTbU6d3AUvm5qKKtI5sZwjv1nW97OB7e5RUgYm-9h8mwxFm8-Ap-t41fqR4f8lQIWg1xtmeXhnTR6TmiT5FqjZFDjXhhsWBFOXiIlVE9iEyQaUXY-2tBOozMhFrx-TjLpcTFddrcXTDZiu89H_IbTUKeV73mTG3J8sKPMvP7xDugCvQuq2xpw6JEWgxhVOPGMJW5WbHWP93JLflD2b2OML1dnedug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نگاهی به آمار خیره کننده مهدی طارمی ستاره 34 ساله الوصل امارات در دوران حضور در پورتو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29609" target="_blank">📅 18:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29608">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFLD-2trte8EFScTgX6vWJaDfI2JBOEILWHIjpSCVZEfIDZ8YkSgBl03AqJqQjfxdY1mFfJ7z6UE9fpirC3L8paG2KpPOasyobA0kDtVbiva3ylcrLIbHV1bj9FT5U8q-qyFTNQkfcctLoXdG67ZT1PB4uaXH2V1FhiLKSeMdmbvqCey0Og4j1CNQJEWxiHoZTtkpF6PrLvLK0bA5iNTRrAH7YIn02mDdFSCow8eQJBD_6BkREpKl8-frXIoQYg2HTwHtBS41WuEmDljweQhNAlNsDpah14ZXoPLfaEyvUevx7IutY_HQI17DMqP6AfZ9dnfe58yKylK-tN3UVqreQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ AS: میکل‌آرتتا اگه تصمیم گرفته باشه در آینده‌راهی بارسابشه فلورنتینو پرز سسک فابرگاس رو راضی خواهد کرد تا به‌‌تیم رئال مادرید بپیوندد اما اولویت اصلی پرز اوردن آرتتا به سانتیاگو برنابئوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29608" target="_blank">📅 18:21 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29607">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇦🇷
ویدیویی‌فوق‌العاده‌ازکاشته‌های لیونل مسی فوق ستاره سابق بارسلونا و تیم آرزانتین درمستطیل سبز
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29607" target="_blank">📅 17:52 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29606">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1Gbneqv_VbXrcwh9B4O0ax4MH628kR4JSOwRLyURks8FlcAFPfqIB4lKFd-cL9NElnQsk4e5wQKO7E1dhQTnGGnFg0RcQWIAfFwuSg_h84CTfiaSpy5_lIdOzuHKyYNHktMF_FEQ1XljwW3PmVYzzAq5zLBWIU8hh0UVtj8EFs8xgIHsdMYUf3PwyYU8WHX-9V7bzLxXrA8B-mBKm5JaWCznh5DUOY_CSybXHq3XkwnCD6E26rDxnJTFRN7loe2rilIB6hHqIqmPTNtGPGQkZ-rEHK0utd8g-lDq452Kpa3OW2k9ejEEHHP_-IgE6dqC2QklX-Y1Tm9LmBPcPOptw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
پرواز تماشایی برای گل شماره 979؛ گلزنی دیدنی کریس رونالدو 41 ساله در بازی امشب النصر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29606" target="_blank">📅 17:42 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29605">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckQ_i44Cseb8uHwThRoWRXsGhBJdzIPcb9YxRNqUxNTybxGKvLVFoiNsCwxpKXzEFW7cTMkfdo6aws4irdLqYMYOWBKynwn_vdUwTAOLpWDbFqU9kLQzaJTpbs3x6y_EglLm3_lRBFYRhrpmPgPA0al8zfhk5gl3DfgJVPrsld1qXmKKiCpnZZvCfZZi_rfENsXailOKxjsif0Iegd6rpNzhKmBIqygPEeiJRGgXA-4ehJLNmtCMAp07ovTZJwp04G3zu0MASZCIjuSU85CHYpk3UloYfgFKZwFCdGNc3vpGMb3zV5ghFKe6sVrEEdtchhDKWAzoRwx5bJFoDKFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
برگاتون بریزه؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ مدیران باشگاه سپاهان امروز صبح به‌مدیریت تراکتور گفته برای صادرکردن رضایت نامه آرش رضاوند علاوه‌بر تومیسلاو اشترکالی 50 میلیارد تومان هم بایدپرداخت‌کنند تا رضاوند تراکتوری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29605" target="_blank">📅 17:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29604">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBfLtu7wg0qJc34JNoZDD9hCo07NI-S_YL2m9jvtn8YH91qPDTQQNZXNUJVnZ9-4uwO8c838DiVRvfKHt-GeaUgjSRExR9P5TULkl3dOEVN-O_5OzQr-1q_s4y5Rz6uQzuRPxxFlqAsqu2Gbb_a9CdihFsrASVxiHBP131FDFlUmWdOt9Es9Fzdoo4VDZ-joXfoYz6BpOCzofp45F0IPEklFKU_2n3ASWKVVSh_e0c5YlcdbUwSY4nnm6XS8HzA9xaUjr5XKB8vYEzrgEsOY9UFTipDcKavRQcdswG8pctYL8kvw61RkOBHJV4U3XRamnUlAF1tnrqcULt5wHpk2RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
با برطرف شدن موانع موجود، کاروان تیم فوتبال استقلال تاساعاتی‌دیگربرای دیدار فوق العاده حساس مقابل السد در لیگ نخبگان آسیا، به طور مستقیم از فرودگاه مهرآباد تهران عازم بصره خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29604" target="_blank">📅 16:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29603">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pD67VcC34oZYj3UvqMeiTr_DW7PRWQeVahl25Z2CMjMoa-weTwAvO_sgcIH8U-e8YYeoFCFr9oHUh5woTVsdLqtOW8RdZtv8l-vlMQLnH5EMRQICtgGRPeHFxFLPHPvXbwZWYgb0p0zxzkq7lVA8AmzZwKat88VFm0ki8zN-6Qo4cc9RwQfytsOcbO6d0bLnko4G92hKbfMBmbUNdY90qVUdMBBEIT4wCjZJn_uF1TddT3hl0fZrmIGMRVXv-xxRuvMxvLftMsQlch9JXCFl617NGwn2fAxaiu2PRaynsYU6xVEqr1Lox6fFV_6A2UdVyAbGzHM_kc14D5e1IOT16A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مقایسه‌کامل‌ودقیق دو سری آیفون 17 پرومکس با آیفون 18 پرومکس که دیشب ازش رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/29603" target="_blank">📅 16:23 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29602">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=ftSFWL1iPLq9JyBGcOvfeApA2msVddK4UStTqPnFyFgWJ4_pvbzj7BKi7KSrzUjI9Zkazk7panioJxBWLQldja30-O6AfsaD0WpR9vBxVC1bD_djGOt-lretKl41q56z8iNQUYKfLSVxVgDZFNf-XldiLyFK14yrDlL5rHEMnIKk6BBYwZ_cxaCqh0NqMZbM1JCEidAyWIStZathd7SMlcVrsz_nzUTzP5QWOkouD99nQEMC4nmf2JbC7fchGsRQ4W6zERW3SEnXn7VmzNrxxoYknXpKc0KPqTM_UhBNSf-fbdDVIcXcGMIA4ZOiNjMQLFklAMng1P44MvcDSj5zPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abe26c296f.mp4?token=ftSFWL1iPLq9JyBGcOvfeApA2msVddK4UStTqPnFyFgWJ4_pvbzj7BKi7KSrzUjI9Zkazk7panioJxBWLQldja30-O6AfsaD0WpR9vBxVC1bD_djGOt-lretKl41q56z8iNQUYKfLSVxVgDZFNf-XldiLyFK14yrDlL5rHEMnIKk6BBYwZ_cxaCqh0NqMZbM1JCEidAyWIStZathd7SMlcVrsz_nzUTzP5QWOkouD99nQEMC4nmf2JbC7fchGsRQ4W6zERW3SEnXn7VmzNrxxoYknXpKc0KPqTM_UhBNSf-fbdDVIcXcGMIA4ZOiNjMQLFklAMng1P44MvcDSj5zPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ویدیویی‌از اولین‌پنالتی تاریخ فوتبال که کلا 0.2 ثانیه توپ تو دروازه‌بود. دربازی این هفته لیگ MLS به این شکل که مشاهده میکنید بدون اینکه توپ به تور، تیرک یا دروازه‌بان برخوردی کنه گل میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29602" target="_blank">📅 16:13 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29601">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLFnfI9zvMwdyRfrEfjBP3rv4OzJt9wio0tYdmFXzBuoZxwtMHf4pNnGpw7UYuO6X_eGRh3smIbHx6Y1HcFdDuUsFhum6ZztLWJM0iImm4O1ZQlCy92FZR7hT2ynsrs4bHAqvPbfls_9dNyJ67gIZupU3qYiUIS2_pofFqBWIXEQza3c1DubJxjNtBiaKg5pqqeohLGVsAY2ns0isFARcoHb3g69PLFIqBJMqhC_jomHyCxjdmrt1zg8OZznK2eX7V2boR2gbmGSLDkVxtRLoYDcWk1joDj9zmuJNUqPuHKRAZd7sYCf-wyeHnEZ0ACx4XjMlBaeWqVJDzPmopPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یاسر آسانی ستاره‌آلبانیایی‌استقلال یک خونه 75 متری در غرب تهران برای تدارکاتچی آبی‌ها خرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29601" target="_blank">📅 15:56 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29600">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDK2KVVoxFzsNC4UMxqz5wVB8rSQ2avvfIJs5cVCzbiij6HzO5Rznfaa3_k_BdUgEvzdp6n1ceskNAlkvewaTEAD872tMFvp2LdYWCkfqSY8hE9si90BQJttgGRPZywvOmTvOg1IL2n3eF3A5sN5Mlegh5hAXinALTgDU3DCgQLsCK4F1KLZrJSGoUxWdc3HhMYfnEDOB-Cj_DMW_QeYyX_SipDQwHJRA6Ka0r4CWZ0SyAWHPldTEVfl1mQAxWr6r2pQEY063HkxnbpIiSAae4RNCf0OUP91kUFq2elxHXkkkG4TLE5MuR26-geywzMgQ0yUDQhULysIkZNcAgPrsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29600" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29599">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnNsi_LFIjVcJqWyYP_3tKT68uqvGNvdGizXCBoJaADk5f5c_Pt6wCnp7poiqAVErxI6LXwHUjmk9kW2TgrBnWTAzzLL634H_ke-J_2CJEwbr3_G2vHPT5NIv2uXCizlXwRDbXk2g_f44gY89ppr2Ul8HoLWoThp2Z0cLH-JNiE48NkA5aDvhTMOwOp_z-ocQF-Vlgq7ookPR86RjO2hG9ScV9dNE8-CdzUFI0TPuzMgoCEx2kpzXua0PbveTqLhetO7Qi9clh3ClfvS7kwUvMkArD5PGVMO4Yw-CGWO25xPEBMFvl-Ytrq8O_MD81vexNV6z_c0frXwMFRopX7y8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ بارسا در لیگ قهرمانان اروپا؛ رافینیا و فرصت تبدیل شدن به بهترین گلزن تاریخ بارسا در چمپیونزلیگ، بعد از لئو مسی افسانه‌ای.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29599" target="_blank">📅 15:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=sy6RP0fNQjsmbKLOoAj-u2EJoJqpbwM-1XOI5xkBtMQeJ2iIDmGKzcNe1vZ48FvAjW6IncikHY3kisQrcdZ7ygriKWzb8DR2ydzPBGP4EwI46ViL2vnR2yHiMQi9ntuHEYVdDisHPLm3gMWwpRAe_iK2VqdQox-VfKxUxEK_NqgRLtRybwy4HS_Rm-CwQ5L_NDgRVRPqjqLGtNshOJG-eqvcCHmVqhXxdJ5N6sYy5hMzAL6VE5VgiusHoxhAQNpo3vRsNO_QS8rkqMg8YWKdeG0wVKaRRtVx1hgqW4lMh5NzcVkaQnZ5xBPcqvB0BVHX5heH7TxRkLSIctnFV-RlgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2a23445f.mp4?token=sy6RP0fNQjsmbKLOoAj-u2EJoJqpbwM-1XOI5xkBtMQeJ2iIDmGKzcNe1vZ48FvAjW6IncikHY3kisQrcdZ7ygriKWzb8DR2ydzPBGP4EwI46ViL2vnR2yHiMQi9ntuHEYVdDisHPLm3gMWwpRAe_iK2VqdQox-VfKxUxEK_NqgRLtRybwy4HS_Rm-CwQ5L_NDgRVRPqjqLGtNshOJG-eqvcCHmVqhXxdJ5N6sYy5hMzAL6VE5VgiusHoxhAQNpo3vRsNO_QS8rkqMg8YWKdeG0wVKaRRtVx1hgqW4lMh5NzcVkaQnZ5xBPcqvB0BVHX5heH7TxRkLSIctnFV-RlgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان پیاتزا بابرتری قاطع 3 بر 1 برابر استرالیا درنیمه‌نهایی جام ملت‌های آسیا به فینال این رقابت‌ها راه پیدا کرد و در فینال برای قهرمانی آسیا به مصاف برنده دیدار امروز ژاپن و کره جنوبی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29597" target="_blank">📅 15:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enYgacD_vaSRo3EDcLT63jMCy1WuVj-kh30IiKNGMkrH200CBT9EiYDpf6EQk_YsBlUnLL-tVRB7kD73pbaXKJdipJovFnm8-ow4UeNlByhoqunInlt8jlajkrDHQvg5jMxQdVTigqHnVtZelGMerXsdSEHFQiyhhM7QI9YP7XanvCX9oUNSEc6QV55-JYUI68OKWL3wOy1zLEpHc-d3ddyXIkjjoKBBaaz1cKvo2zginyPe1bNHMtek-ceksLO8YedmtBNNjTWB7QQbVb25M5uVZX2R7Qfmc4w0wV_J1FU22meHvDW2RH57W2w3KjSVFpimm3axxBfGg4KUrOqngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کاریوس دروازه‌بان سابق باشگاه لیورپول در کنار همسرش دیلتا لئوتا گزارشگر شبکه ایتالیایی DAZN
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29596" target="_blank">📅 14:38 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ly-MlqqOFTCplic6YHqayRUKC6dKDjAikMZ4DHUsklDfsXEsbVlVWg0X6Vi3xNOeWdd8svi99FmZTnPhEp_fDLUgFLqDh2YwTsP1DjH2u2T0FX0ugMVyoJDF-kzcu98UmI-EbuegdBUAcvQSvwkhW2eKH2meH9nYhKkY_fDaX83R-VPDLqcwHNrqxBxt73XqfKhVzQtiuL-ccSlxmfbthvXU0z2nr8c2H5w3F5NhmxWosdn9dCDBdRrp7gDpNwcn4D0yhpyUUQTgqjrv1T2y6drA3vIhLA4_0a9j-KhPitvFRgH89BWedttD5ySzOH9RjUClK0ho4OpYuAVe2OnfHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌ویدیواز اول تاآخرش‌سم بود از دست ندید؛  مهدی توتونچی تو برنامه‌شبکه‌ورزش نادر محمدی رو اورده بود رو آنتن زنده بهش میگه شنیدم میکل آرتتا دنبالته که تو روبرای آرسنال بگیره نادر هم کلا ویدیو کال رو قطع میکنه. بعد توتونچی میگه آخیش! پست ریپلای شده رو هم…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29595" target="_blank">📅 14:12 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVosc3-oUBCxNNZjZy12fVvLT2PEMSTWzEk_la8TAmfVjzfZa8jQZnJK2HWxPfa8BK6V8TNFAelLbX9gUk5rcexi3B6ocwX_Tq7NRt_rqpAyRb0W_bJ_Sc7dQugvMTW_vcHychZ1hqmIMiekBm01YMnjajqlVuy5B_mjJ9Tp9wysiKcob_dmvOh1DPLw2YapHhBYt030YRtQGiE6knPVPOwAfQdWa-bQ31MgkoevDhrDirkmQtfpEd9Xdxmu1Vclx8mbCv1EeW_sH8lI8ALtG-OFBFNzvLYkQ-KUJB9-JDSw-oo3sCiFPuXFb1aTibxD9-GPJ1SQQbquDxDtUQcwaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟡
🇧🇷
طبق گفته رسانه‌های معتبر عربستانی؛ ریچارلیسون ستاره 29 ساله تیم ملی برزیل و سابق تاتنهام در دو راهی النصر و الاتحاد قرار گرفته و به احتمال‌زیاد راهی یکی‌از این‌دوتیم آسیایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29594" target="_blank">📅 13:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGNwFQxV1zJFFCY4boYI9YRJ2iaeAmGs_nuDip1gfdAiqIDelkC8FWciVpu3O94T8YveF1tcqZYsyXVHU3xNu7Dh3VpasAsBBZ834MBoo8JJMLcwgdUq0raFjM0D3zK9CzM1KZygraqYZhB3sbOayu1aLsjqdQ-W9TGP9QGaouKBzSVIHbSDvWSzMfSIfOIwguryEqJU6mleb0BbZHP1u1MdNmG5_KixVywErmfE7Iu8XI9zMQU9QktUcfNEb61pnLk8VbtC_ObvEY3KbPZ0Q4OMwtwUJitDvv-SRGAYLoPFfb4AxL__5AGc2c5ZI1TgZcWVPeYZRyBuKN9jN6qHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ بااعلام‌پزشکان باشگاه تراکتور؛ پارگی رباط صلیبی مهدی ترابی تایید شد و این بازیکن 32 ساله رقابت‌های این فصل لیگ برتر رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29593" target="_blank">📅 13:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29591">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره جوان اسپانیا و دوست دخترش همراه با کاپ قهرمانی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29591" target="_blank">📅 13:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29590">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbHlxiTr07U_dAHgJ8nmIeOAbmft9VWwz_ELVZgYu2VJ27jfzheirXLcdK2CHeun-aKB59QtbmH7fzqxTl7MKVCJULtzrct5cBwR-kTux_CrCdirNQoezw8C1NEgejeK9hrgOTTNnOAFSocUMnJRKnjty7Mi4TzFoCjJvvD-EW3k-Nl7yrKaldV770f0jzAAtvRzkHLl7uYlfICTcn2-F4NmM74gWhe_kKHkX-pphiEP7Wf14XfS8XdjcUL15UCMN1WwpB5iJnNMif-7oU64A95sWxo0QTBc52JGREwBaM9HONpiwXs0Ab3ZsbZuZNJc_LIHmO_KN_LV7lZ-GJnkbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان،…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29590" target="_blank">📅 13:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29588">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JerLE3QY3x-1qMQpanQW2a1fkAD9OWRz_MrjZ4KBhHhKmViO6W9XoZVHzLOsOjdiYSuNz5-WIS9X4ITvCKJ02_0TumFZFueIRx6NbU34Z8Prab1BvMoj3WnOZHOatlwYc1AZMl0eZZR3JuH92nofv-OdnvtTZhYPV0pnDX-6GWJ9Cgst-YwTutM5PM3_G4b4v3e6HsjHCEIn6RckKproUmTWIh4qtP59i-u3Yt4z0IhO28_wIfgiKJpsLJWWF1SZOEniQvEYB3h5JbRwNG97mP41FfUuZSGSWTYs9dyyOxljL35dMpodkbrZqhIQy_x0RNvwyuVdLwzlCFoSm3pt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
معیارهای رای‌دهی به توپ طلا؛ عملکرد فردی؛ نمایش بازیکن در طول فصل و لحظات مهم و تاثیر گذار؛ موفقیت‌های تیمی؛ جام‌هایی که تیم به دست آورده و میزان تاثیرگذاری بازیکن درکسب آنها؛ بازی جوانمردانه؛ رفتار،احترام‌وشخصیت‌بازیکن درزمین‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29588" target="_blank">📅 12:43 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29587">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRf6idoGRZ_HLcRfiHCn8sSIc6hWCOEI7WAj75-7SjGaCyn6E6mKdfmwmgRREnju6_RlWC62679yMBuN93FVM6zGRtE4mHaK_4gen1uXw0q8x5gNgqiqfljhytMTN1smu4FAWGdaG3KwAdrF3LB4LvoLGO21pY2_itI2ovcT9H5Mnzr0sMHPn_sdJnJ1Ocbi3Daw3hahg75y7ybs95A0n9kdypUpIJjFadpDkxPI_6GBqreKP5ap45cpnu8ReqMF8IkUzIkTFTPM8mQ6CqVvbHyqI9g8vOH1BSpQ0_rluhOW46znD2APizlo5e6Aw5r6IGsDRRe7NmXjiz3QSbRAiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
برگاتون بریزه؛ امیر قلعه نویی سرمربی تیم ملی که تاپایان جام‌ملت‌های‌آسیا در تیم ملی موندنی شد درخواست دستمزد ماهیانه 15 میلیارد تومان از فدراسیون‌فوتبال داشته و شرطش برای موندن روی نیمکت تیم ملی در جام ملت‌های آسیا این بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29587" target="_blank">📅 12:28 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29586">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=qWwAei4pxKVgY4ilRmhTyh71XTPwY--KnfSWVrFirlwfz-ZONhbh8b61TiF0cWdxexnuKUccg2M2V7h06VEEEHfmes468e7fy9cVso7EwMPbG_ZMxFCjSEz9wYI8gdREnymSm8paxiTwc_mWRoiXyMf-Rf4WlBm5KCCixcgaZjUam9JBjdmta7WimxOc0kV14BiQDxh6NvRYbRFXzutuJnVZX22TJQtHw4OA01n7ViD-AePcO35Mo0zsXRwOx28t7Loh2kmgwksknHnQC76PTN0G8tKWXxL1nC2QXKaMiKPvDGHbKG2lghm8N_6TkXO-n7NtUCb78dEzsCclOd5yQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3e03b999.mp4?token=qWwAei4pxKVgY4ilRmhTyh71XTPwY--KnfSWVrFirlwfz-ZONhbh8b61TiF0cWdxexnuKUccg2M2V7h06VEEEHfmes468e7fy9cVso7EwMPbG_ZMxFCjSEz9wYI8gdREnymSm8paxiTwc_mWRoiXyMf-Rf4WlBm5KCCixcgaZjUam9JBjdmta7WimxOc0kV14BiQDxh6NvRYbRFXzutuJnVZX22TJQtHw4OA01n7ViD-AePcO35Mo0zsXRwOx28t7Loh2kmgwksknHnQC76PTN0G8tKWXxL1nC2QXKaMiKPvDGHbKG2lghm8N_6TkXO-n7NtUCb78dEzsCclOd5yQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تقویم
؛26سال از این‌خوشحالی عجیب و غریب محسن رسولی ستاره 19 ساله سایپا گذشت که با یک حرکتش روی آنتن زنده شبکه سه فوتبالش نابود. بعد چقدر بازیش خوب بود این پسر. یه لحظه نتونست خودش رو کنترل کنه شورت ورزشی رو آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29586" target="_blank">📅 12:09 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29585">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXmAtPwGdCvpFMvpDgY-LfS6eHW-sLz4CU19_R8qu_CVYUxeFrcEamhNDgNHhfzNFtPNDAM_H8apIMSWkQJZdlIeCfCxZ9xFhHPYnv6cm6Srv9hRjwDFDl9P7pJcBwnTsbi7PTibOU2LrDYLYC9svM6l2_cOhyn3rKQVWphsfbuc_KAH4K15qmE_Jdm56S_iJ53j0pmB4cN42CwGfNErwkcLvh48UUpfHMiPlv2millUCvozpyKnkLQy4AZZY6Fte5TEp4YK6crQaaLOZrBW-lsN4sbwWBqPRJdR8WHWUzDW8GPrv3xrIGms1e7CGjuglwakF4rjhYZAw-rssP6gCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛ فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29585" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29584">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGHlB55JQP4JImA7YfB0NssyuVL2uZmof5fPSBFXQYjF-wrkA-gtk2JiWJJGESP7iVkof0by7R0MCQT5iEUq1uAl4q_G_WO-mI1jV2nHDT2tEw0-EI9TwkxrA0pCrr3tBl15b0hEFwvV1t9gJBeopraIj7ebvPDfkDsAoAH30FQ2Uhp7xxZ1x68PujVpanDkOrN_n48vxwXIGcyedeKU1KbNdX2cgNNW1ahdvAfdtNSj7HgHAAHC0nBlHLbswKiVA5pMjH3JOO6WgE_j8G6ghHiv1gVwl9hykGKA_G3PfIruPFno_xR8lxsxdU6Sm4CUEWspXTN9TrEIARMVz8DTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
باشگاه السد قطر حریف‌هفته‌اول استقلال اعلام کرد برای تمرکز رو لیگ ستارگان قطر و لیگ نخبگان آسیا از رقابت‌های جام حذفی قطر انصراف داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29584" target="_blank">📅 12:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29582">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
فرانکو ماستانتونو ستاره آرژانتینی رئال مادرید که مورینیو به پرز گفته بود اعتقادی به سبک بازیش نداره و قرضی اون رو به‌فیورنتینا دادند امشب برای تیمش درسری‌آ هتریک کرده و نمره خارق العاده 9.8 از سایت فوتموب دریافت کرده است. ماستانتونو در پایان فصل به جمع کهکشانی‌ها…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29582" target="_blank">📅 11:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29581">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBnzjYM8-V7tQ2O8zLoq_rB_SYUaxj2IZS63clFrl_tbv_akXHTJ_fHuwa5g89HSuu1TCW7DX3ZmvBkceY_mLERo3mfC3UKRZaBECaarz6S72LvTrjpXWZcKK6K6qHsMFlXkqde3RKFwceDGkGbqntLoHaWU7vzcMINQum6L61hQCpMm4k6C0hvgXEY1_eNKjFGyixvcULO5LcUsizGVQa26jdGwC5drHQ6M0dYtplyIK6laTZbGgRVZfdzLvEdiIVPwfl8T_OWZqsfdz59Bv6bYk_GwXNGm73bn-mJFSow1pp2WLQrRDulbNLpLqMYKEaigrzfFyQDB4eCrVSDUSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
47 سال‌پیش درچنین روزی؛
اریک آبیدال ستاره سابق بارسلونا به دنیااومد و با این تیم به دو قهرمانی ارزشمندچمپیونزلیگ رسید. آبیدال سال 2011 هم به بیماری صعب العلاج خود غلبه کرد و بزرگان بارسا در شب قهرمانی این‌تیم در UCL بازوبند رو به‌بازوی این بازیکن بستن و آبیدال جام قهرمانی رو بالای سر برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29581" target="_blank">📅 11:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29579">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af01699be1.mp4?token=lmVOmBZ6K3UotWaMgXl3kQGkw_xSqEwreAW--xJ3_uM3_EPzkAer3jk9mZqfvbwq4NTapRLFI4zQ1XvT937yed3Fj0kC5-kQV_bSLVGgh6dCjmWvkRjgaKLCBGwmlUIrk_UNGdD4I07HpKRI55ImhG5Ok2809fdFx43OXRQ2spniDqKtzO9t09M46s7zFit-Zu7KSUoL65gfnTUmuxxb_z_AX8dKngGsJtNbw5UKPVPA0j3bpYZrjVZ-bQ1VsQRt2Oc3rJJCF9IB6HP4-iymTGtktT1l6mclrKHnEly-w7rkaO3bm0KNCq6LENPFxZk08G660pYYTRCRVT0TCNilL6CAfFIPLNJhibCkwn6F4eaGof582f5K2EH1C9XiGnpDHrZBHgAu9U0CwFsqIjnnSC-FKDow6CBq7mVLOS5kg1MBVXwOQnKd8-mpfwAt4VgCc_ABwBwQLAhTGrs9bK1wR-4LfgrMQArNPDe4XOY_FDZGzSPndOT9CDfyKQjYO17C5MhioHbNMNc4pSLDomLEYutu7fEXu-HI4sxTQ7teRlhRM0_xhwFu6CHwwtiHgYV2vi4Q8sJBaKpIrH_uCeyVzl89mdk3AGlg7f1Vvbyh-laKFdl2AoAG64fZEWfsTk84Nnv_z3keLv5eWCr8FgM4B9lPAnNMT8LrJxkkE6BqeSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af01699be1.mp4?token=lmVOmBZ6K3UotWaMgXl3kQGkw_xSqEwreAW--xJ3_uM3_EPzkAer3jk9mZqfvbwq4NTapRLFI4zQ1XvT937yed3Fj0kC5-kQV_bSLVGgh6dCjmWvkRjgaKLCBGwmlUIrk_UNGdD4I07HpKRI55ImhG5Ok2809fdFx43OXRQ2spniDqKtzO9t09M46s7zFit-Zu7KSUoL65gfnTUmuxxb_z_AX8dKngGsJtNbw5UKPVPA0j3bpYZrjVZ-bQ1VsQRt2Oc3rJJCF9IB6HP4-iymTGtktT1l6mclrKHnEly-w7rkaO3bm0KNCq6LENPFxZk08G660pYYTRCRVT0TCNilL6CAfFIPLNJhibCkwn6F4eaGof582f5K2EH1C9XiGnpDHrZBHgAu9U0CwFsqIjnnSC-FKDow6CBq7mVLOS5kg1MBVXwOQnKd8-mpfwAt4VgCc_ABwBwQLAhTGrs9bK1wR-4LfgrMQArNPDe4XOY_FDZGzSPndOT9CDfyKQjYO17C5MhioHbNMNc4pSLDomLEYutu7fEXu-HI4sxTQ7teRlhRM0_xhwFu6CHwwtiHgYV2vi4Q8sJBaKpIrH_uCeyVzl89mdk3AGlg7f1Vvbyh-laKFdl2AoAG64fZEWfsTk84Nnv_z3keLv5eWCr8FgM4B9lPAnNMT8LrJxkkE6BqeSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما روز به روز داره خفن تر میشه! شبکه دو یه کارشناس اورده داره از خاطره قدیم میگه میگه کارتون میذاشتن زیر کونشون فیلم رو میدیدن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29579" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29578">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwFSwZi6I6qoNkhUdBYB2UCNJsm0BP4cOo2qxxir6O9iQ1Vo-Memk8qWXlm4bT4W4UVjc1CM1mk5gNjdW-hat7xOxUlcVm6oxL3cgOj9NoUxi12jKm16NELZkgANyWTCX9GO7Lt3lVnFmc0f36owh5R-vklnSMSx3MfM_mNQTDxdw-yn2FeCiHQhPG5zKj96ObuGZGmfPPTw_boPnHQxBajPrGPjFswDpuSgx42yxWPwC1tfKzgimlKPyaVhjIq80E-WUa8Sg_Atq_R7zzqTPucPXTVCE39O1RiGoiqztfV_F1Bd_CJo4RPHdAlBMFzmhLjcHa-_v3vfai1o1tvPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29578" target="_blank">📅 10:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29577">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0XIdjX2Af_cYqgzCkD1CeIzeVi3eom7fYgAbo1qDPT2iS5Ljph6y464Ps7wl9z5lso64PF820XYhlCo9kPREcswUVJvH9iS9u8sD6O6jvp03N6JDtAq25DkfihdIT7ULfuyU5HFMJ-T0aJJhHDQ6Gn5jym4CJMGJm2zTvoeHYf0QYu5XHtOo9VHxEHvHPmaItvQUACoHnNVEEsG0Q4xx54tMt9W0Z-CQh7t4qOnEjaEcQTqAAMAmm1bxVz3JpxF_sBpUKPVokuRaiarzsojlaIq9E3IuOS1G1ytYCxWUoc9ufjbFz3qVLr2P0zFYvJcSvyhTTtlzcvfHD4HW1YGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
باشگاه پیکان از باشگاه استقلال به خاطر استفاده کردن از جلال الدین ماشاریپوف در تقابل اخیر دو تیم به کمیته انضباطی فدراسیون فوتبال شکایت کرد.
‼️
باشگاه‌پیکان‌مدعیه‌نام‌ماشاریپوف فصل گذشته از لیست استقلال‌خارج‌شده و با توجه بسته بودن پنجره نقل‌و‌انتقالاتی آبی‌پوشان، حضور مجدد این بازیکن در لیست بازی با این تیم غیر قانونی بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29577" target="_blank">📅 10:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29576">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=FcxxKef04yUMeaT8nHIs7qG0LnZ8LuriqS783GLzgHguzeeDeKtQKCtI8VroVi8D2WtmwTQ8IJ9d4_tkXcc7ChpKSBw9fH3GTeooJPeaWPe1V-_VixUzQuo0_MN8MG1XMOIr5c1BRdhkSq558MI821LzaQy-zJGIhclQUruKiWSprzzbveGTAG8Sh-kpXEVFIVqwcY0KtdJOWOCM-EoYQyjlZ72hUCGiEGG-EfA0wqlrM2No_tJjsoNdGTiUXaxZb-vOjhejysAxUACtdF-PSVgpSimE_HhOYcjBSFumTtvxwuZ-F6HbhvBV8HLFOPZlDB6PiHJ5Jbdclef9tahwQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6157fe5afb.mp4?token=FcxxKef04yUMeaT8nHIs7qG0LnZ8LuriqS783GLzgHguzeeDeKtQKCtI8VroVi8D2WtmwTQ8IJ9d4_tkXcc7ChpKSBw9fH3GTeooJPeaWPe1V-_VixUzQuo0_MN8MG1XMOIr5c1BRdhkSq558MI821LzaQy-zJGIhclQUruKiWSprzzbveGTAG8Sh-kpXEVFIVqwcY0KtdJOWOCM-EoYQyjlZ72hUCGiEGG-EfA0wqlrM2No_tJjsoNdGTiUXaxZb-vOjhejysAxUACtdF-PSVgpSimE_HhOYcjBSFumTtvxwuZ-F6HbhvBV8HLFOPZlDB6PiHJ5Jbdclef9tahwQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
دوس‌دختراسپانیایی کیلیان‌امباپه ستاره رئال مادرید در فیلم جدیدش بنام "Drawn Together"
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/29576" target="_blank">📅 09:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29575">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=JwTmvyWfuO555lHUFNtFyZVAvxTucUz1cGoDfjQo8c_T5OnmIptZd4-1Y7BIHmN_AQ6gU-iQGiesOwYSt61daU-5d7z9U5mtxA4Agy7SwWZB_CBnZs0V0KFMT9rFaDJfIwNOXvqLqHM_XdJSrPWqL6oSUziFnTrdTLejXjk2YYusSQ7i2Q3QN-DnGz3LDIcYH87qJ2InHNOki1NRetkCZLbI5HCmhcAC2rw_TWD-gT6tEk93sXYf5rHvSeCn39RLeAzlCLDn4-5HJZ6wsLTobs04327JGyjfDjJ0fMRXrT1Wi89m2wg19mJ1LRAIQApJKbbhf3fGGlikGloqTI7Lk7zuUpPj0AvQxgQDuCWma1NvoiaeRRxQKJ2AOLGuK48l9p2Fqu5U37g7TixmcrTHVpVYnHPcD05rY7FQU7DNjTme9rMREODrSCxVV878rgh4JDMnr-vNJW-8Y7-fOHZwyrZcwR5kwQX0Xq8Jx_wVyuRqMAy0HIx9BrZ9YXkQF5BXmtxDzkZebBKiEZmuikhKYhuA9Z7N_h1bvL_oqFV01ceJt4b825XR64YSQv0S-EAVvZQNKq0yQutT2XMffrMtoxq8v_ilGS41L_bMqNf4s6oE6nCC3y1GAiv_I4Kl_2iCYxbdXdqJ-dGFQbxLlrJVicc1_QKyVL6LoBrKEPIPRj4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2108b760c.mp4?token=JwTmvyWfuO555lHUFNtFyZVAvxTucUz1cGoDfjQo8c_T5OnmIptZd4-1Y7BIHmN_AQ6gU-iQGiesOwYSt61daU-5d7z9U5mtxA4Agy7SwWZB_CBnZs0V0KFMT9rFaDJfIwNOXvqLqHM_XdJSrPWqL6oSUziFnTrdTLejXjk2YYusSQ7i2Q3QN-DnGz3LDIcYH87qJ2InHNOki1NRetkCZLbI5HCmhcAC2rw_TWD-gT6tEk93sXYf5rHvSeCn39RLeAzlCLDn4-5HJZ6wsLTobs04327JGyjfDjJ0fMRXrT1Wi89m2wg19mJ1LRAIQApJKbbhf3fGGlikGloqTI7Lk7zuUpPj0AvQxgQDuCWma1NvoiaeRRxQKJ2AOLGuK48l9p2Fqu5U37g7TixmcrTHVpVYnHPcD05rY7FQU7DNjTme9rMREODrSCxVV878rgh4JDMnr-vNJW-8Y7-fOHZwyrZcwR5kwQX0Xq8Jx_wVyuRqMAy0HIx9BrZ9YXkQF5BXmtxDzkZebBKiEZmuikhKYhuA9Z7N_h1bvL_oqFV01ceJt4b825XR64YSQv0S-EAVvZQNKq0yQutT2XMffrMtoxq8v_ilGS41L_bMqNf4s6oE6nCC3y1GAiv_I4Kl_2iCYxbdXdqJ-dGFQbxLlrJVicc1_QKyVL6LoBrKEPIPRj4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌خاطره‌انگیز و دیدنی از عملکرد گرت بیل در تقابل با بارسا در فینال کوپا دل‌ری فصل 2014
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29575" target="_blank">📅 09:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29574">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
گئورگی گولسیانی مدافع میانی سابق پرسپولیس و سپاهان درسن 35 سالگی از دنیای فوتبال خدافظی کرد. او بزودی در لیگ برتر مربیگری میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/persiana_Soccer/29574" target="_blank">📅 01:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29573">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdHrvaLXdxlxPWMxUxRW2Mo46IRAEGHnXDD20zlrcF4_ruElSFjDAZrMFgv6FfAuyzrPr_Y49ZUyN9v2spVmXYVHOGONnUdEC6J3kUhotRSf4LoVyc51trP3vIz89GjIFLsqKZbqGguH8iOxqn7Y-2LtMZzCbwXGpCKTwaIqgupasmmH9cjGM3_COZiNHtWRlVwyVJb9j1U5n1WVg2bcruG51NwMrhZ_OChXyWwH5a7dweewNBqgWSvE9Wq8ejX37MXh-leUPY99VFPkBb35fQDsHiO1XyrAcIKWdXIEx3I_Qyi-Owj4fK_UZ4PIYFtO-dvVa_qOAk_DUY5G2oPDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادرمحمدی تو روسیه‌تبدیل‌به‌یک‌سوپراستار شده و هرکجا میبیننش دارن باهاس عکس میگیرند. همین روزاس رومانو بزنه: نادر جون به آرسنال هیر وی گو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/29573" target="_blank">📅 01:29 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29571">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLXeScrYntTA1X1zqxfNB_lwtvdJr5wEROLPhQ7oqcl-AYfEb8M4ZFPCfjMmfK_QtKlVBRIEbirGuZftVRyxmuNSeeTY780Dq9H45S8UOsLj44VwOHhZXTiEj9g_xH2YhVqFZxjFSWpucZ-JCMPx_0JB3LtreLvb5-Gk06cEJEm0RDslN-mXD0yrA7iiFYBUb9o2bLqRIsq3OqHfjhsYhzt9UZUjTLuRUocILiM4bAATLeFOz8okEXfXkT9w6t26k8P_ec4bkV-yAR1ntmo6tXiVkNd7lC-17qm9IVLxdSjYMGhnEgYoOODi_7kp07H-Vq4rDQAg0yKou5ap8ARseg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین گلزنان ایرانی در تمامی مسابقات در سال 2026؛ سعید عزت‌اللهی با دوازده گل زده در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/29571" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29570">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKUjF_Mx2yJgQNL3bhB6oonxsPKJQIGBNrfxsQfOnLFeg2LhWh2jqclT9onTEptTiBL1blQWn0B6Q30r-dcQUJPBfsXvWhG7FGyWVbMr9Sz94yPdKocwcahlQkM42fb4YACWKII57rwq0exgsSEQMPQ8X4mMu6PtSHMi4NKf-qX6bohcrPTP9tVhS0x-zcmAD4W1AZNYm5KTB_m3P-B1QWp3LM6Dn8Fq6BG6SUMFJKAOatAhBjzPIFSjDKYzsDFi1uZ-sCgXj3GS5I3n7zWrAXDwkPklxZv8u3oxEaP2soeVw-KQdpRas5V0Lhty9-37904iwdi8lnSNWjtay7EA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری زاده و نکونام سرمربیان استقلال و تراکتور به شدت علاقمند به جذب شهاب زاهدی در نیم فصل هستند و حتی صحبت‌هایی باخودِ این بازیکن داشته اند و به احتمال زیاد زاهدی در نیم فصل به لیگ برتر بازخواهد گشت و راهی یکی از…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/29570" target="_blank">📅 01:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29568">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5QtMYBafJ-mdfw9X8fUjMjx3jbptyWUHUZf0wTfjXBeOBI21UWkImtfUU1MAx40DG9KjIG3jtt-MZLou6x-W2CsJNyC2mR7dY1KRXK7-inH4qtpv7n5rVaCHs4HvMI8mvtXvWWxgaLyfWuUJtNcwCRlm0FExlq-E12h2hqr7i1e_hkLR3MdZFn69RsaFz_2se1yIZN-4KiL7ATHgXmupASkE10V0F_01PViM7HMcSpzFF9QExVG7GxdRTGuVN3yHQvecksD9edDrgHQksb0rhmZe2gW0uIO3dLLSgty8R4egfFDi7aJ4MZKIINwOA6t7_3Sh6T45O2vCptR_PuRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ فرانکو ماستانتونو وینگر آرژانتینی ۱۸ ساله رئال مادرید، با قراردادی قرضی بدون بند خرید دائمی به تیم فوتبال فیورنتینا ایتالیا پیوست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/persiana_Soccer/29568" target="_blank">📅 00:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29567">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbnRQGvIakCW8MZuJe4a4ClJYCiqheWQ9tmrs5upv-AXR3WxCFOYfjGrREf54yDuRPmmN1oA4p-JgzFwtMt0nrJxmd335P0HjQJlBgCc91AC_LHDXiN1HpP7h77VGTHqyfoFP-15AhiEAFkMgr-QUwPb7CMxEYemBDKtsKs4BdqSOuD86EMVmAsDPcL1pfgM0pofnKwI6H9aYdQVbQx-lKIRfPzINzgn7HB2D54kPN91ynqgL0rLEJ4k1SVh7J3JyWibj-Q3PK1OFZHL5gYx2rUsufGZqzBE9-r8e80xHfFg96B7NX1fPkyEIHhc4GjKKPoJb7yl83jzhs5Vu1BGdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اوستون اورونوف در جدید ترین پیغام خود به مدیریت باشگاه‌پرسپولیس گفته اگه کادرفنی به سبک بازی او اعتقاد داشته‌باشد حاضره به‌زودی با حضور درساختمان‌باشگاه قراردادش‌رو تاسال 2030 با سرخ‌ها تمدید کنه اما اگه تارتار علاقه‌ای به ماندن اورونوف نداشته باشند…</div>
<div class="tg-footer">👁️ 82.5K · <a href="https://t.me/persiana_Soccer/29567" target="_blank">📅 00:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29566">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=E1o1PnQ0HgyquDIHhBrlYcts6bau-J96rUzTraK7Z0Zu3vIK5RpuJXbLQ3mSDQATqn85hd6ad6CXJ59qD2wPP3iGPB5czfPZ7tsfq80KU-KHlRtaD89RzMOCe0dvhNXVq4RUdFS8cdyaOHXgH2XUjCqjgFlGNJHjXBXZFZr2WlwiSwLauhRIkZG36wncLEXqLZ4DhWMZyH_PbqUYfovDOL9yHD-SApHnLvARpaAC_eSCZsnvQu89dQ1_s3Ix-KNjcybvt3iOSxIy-eQ0BcEK22-SUE-GuA0IklrAsR99YieumwnHEPv5qYYk-z1kEVsLf34S2HZLWzg-vGx0mHZTcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a6b08f6a.mp4?token=E1o1PnQ0HgyquDIHhBrlYcts6bau-J96rUzTraK7Z0Zu3vIK5RpuJXbLQ3mSDQATqn85hd6ad6CXJ59qD2wPP3iGPB5czfPZ7tsfq80KU-KHlRtaD89RzMOCe0dvhNXVq4RUdFS8cdyaOHXgH2XUjCqjgFlGNJHjXBXZFZr2WlwiSwLauhRIkZG36wncLEXqLZ4DhWMZyH_PbqUYfovDOL9yHD-SApHnLvARpaAC_eSCZsnvQu89dQ1_s3Ix-KNjcybvt3iOSxIy-eQ0BcEK22-SUE-GuA0IklrAsR99YieumwnHEPv5qYYk-z1kEVsLf34S2HZLWzg-vGx0mHZTcoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌مهران‌مدیری‌به‌گرفتن وام‌های‌کلان در قسمت دوم جدید سریال جدیدش بنام «مرد سه‌هزارچهره»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/persiana_Soccer/29566" target="_blank">📅 00:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29565">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQW2787nEhHJwnkWIc7bUKS3k39tRMRatFDK37iFIkEYvX_pZUktl66f1GrENY-hW8iOVi3zNX-QADqIArMjVIaW9fNRwE29jGZF9NviJYMxkJ6kaLUyTnfNN60t0TFqPvz55Dl0aMcIrghps4ICbPmp8HTvszBsJyEo6N6dGeNkoCXnRsTuYDSFNH-0Mgbhc9UM_T1yoUZbjxkmiFNuMAW9Ex14zzI0LZU4cziOtm_zmIhO4YL3AtDCQDj-r2Z70pVAyPrjQTmWcUFUn3nVDJodLrbgQF0Z5CUV6-HTvnJ0hJFwaylYMAtgSRA99ZTZNw36Stivd15_kHjCo9jQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛ از جدال توپچی‌ها با یاران گرانیت‌ژاکا تانبرد رئال‌مادرید با رایو وایکانو در خانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/29565" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29564">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZXo6tPV0_kVdsYEDZ8szpvunx4U-E1KhQntVMaC9LUVKQUdIxX28nMHZrYfXHxnDgZhL3agHAhjZd064ghAZAqyl20X4bmJu5LWid1t61KQMRLFJmdFxBBh7FVYeCaKJafT1J3Jeq-oIcJI3Tu0nR6ZySBMla1YDkmz-NxPmBoeJ7oEoachXQ4raZgzqcZUHqsN3gPX-NXpa1JkUMl9tm29CsyaNdDIjElGFBVCYv68YqwXLqAnJVOFHdRbAw6vR2vg2f6Sfg58wKrE-4RPuLKbW6c2jz10Ewiz_xz8y5n-ZfVblfuQEyuMllR_z40NOr4ZFzdq6XnZ6sakd8LLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شکست شاگردان مورایس برابرالوحده‌وبرد اتحادکلبا با پاس‌گل سامان قدوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/29564" target="_blank">📅 00:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29563">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n7xCEbJNYSYujOaHkuTNZBwFee9ebCkz_5qjgEdKUtihsfBMNQ3HkgWPhZtLAtHN2P3JOrw3jlf3tQ5G-axJbFZZ-zQml3hcN48y05pBV5yVFEIV8cexsYIhn8IELcZydNhU32d_tnajkgCukN3tEtbETND4eXvNoOx89q4Cs9vTeVX_KMQbZba2Q0jxjpVG0J5nXttjEZDyFSQJlw3b5fvaCCL3XTRWwuPdtDqgIuNZJjxOmaYgSKH0RKXPgqWZxO9jcA0QsJ3JNU4j1GmNauP391f5A1sG6LMKTZHyZhGZ4wakJARoAHMcii8J7CUGnziw0Sqwg97fJQse1G2W-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه بیرانوند بالاخره باز شد؛ گل اول استقلال خوزستان به تراکتور توسط رستمی در دقیقه 54
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/29563" target="_blank">📅 23:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29562">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlsxjQNotr0Fk3Vr-eFUrk3Wo5kNAsZdxFZF8d7S9pcbQWoCudk9cOIb22g6LGbEfPN_xnTuWWlaeZYNbG81p-SPybKkeYSgdWO9cPVnmsYGXPzNU2vwxr3U4vkymcV_I6BfzClm03cXq65DdllBbB_Ivg0nXEmfx0iJrrWtPYbIlwQX9fZgX0tNwQ_faDtdTmBRlIiMJ9wSszAh0zQsqjXhGViStT7GpSLtsn_RINJCEuKYz47n9XethydhiUms9LwGs2iinJPoFz-VZ2pjeKDOBkdHC3U6ElEA-XWW_08AgTWDJoC4-GmgSInbtLRSu3_UEPxeKzHMKYLXWF9i6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رقم دقیق قراردادی که نظری جویباری و محمود رضا بابایی با فابیو کاریله امضا کردند 1.2 میلیون دلار بود که بعدش یکطرفه فسخ کردند. حالا 40 روز فرصت دارند که با این سرمربی برزیلی برای پرداخت یه مبلغی توافق‌کنند درغیراینصورت کاریله به‌فیفا شکایت میکنه...…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/29562" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29561">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY8fbAGK6BcHLBe1RSHqhchLsUpT_QhfDbustaO8nJH_te3pkmlW7xh5mfZJALxt20i0K85fVhIQgKVi9VvE_kQqDXq7TnqVS8AWYel38e_jt27OwlWzTqPq48DLE17cDxrMktbzJNMo1DLhqLDvQ6nhKLxNK3p_HY7Yt_wmyGAYbyHrxZ7hhlN2s2HGM5uz-17MhvqANQfl8SsYnatss8ctn_miRiIFHR4F8B3gOnoAucWyonHZvMmvqCjPrB_k02iNgum3D-NkM0pZkIRjZG20bYSNF8hmZwdv9lOq8PkfTSjPzwJAR0zO86j008wYbar8AxirzZld0hlx8iZWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
عملکرد فوق ستاره‌ های فوتبال جهان که اصلی ترین نامزدهای‌کسب‌جایزه‌ارزشمند توپ طلا 2026. امشب‌بایرن‌مونیخ بازی داره ببینیم کین چه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29561" target="_blank">📅 23:11 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29560">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JF6V6ja0i94M7urI5bLwcasTs3vmCYhRjlB0tYrcuFBRq8N2VjYjlI9VKAaq57H6z-tTthHXCKa2Q1EsHU95AdU5dPPUmprhe4-UPxbyKGkD2lgkO-3jaFdaZ-KHQW5b6B0NyhODZKXjscMkLatDLQA_b3KQ8Bu5JhQiCHQFM9NHjBhaBig_Lq88SV50u4NP06z4OYKEVCbgCtQSOSBjyR3rF81H72rdNHkFr-AlXP_VgNMW-J7TwFcYc0GQNDBo_ep4ye98QoUlzGqxLpo5DfSxB3VOnJjsbxoqBdW-s7jPPOU1w60057FgK3jFgF2sJuNW4iuVLb-4JkGOCjYniw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/29560" target="_blank">📅 22:51 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29559">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3ylZCNM9wX0tqGGLxGw1oRCBvzpUsVrBtL9qQfOY_-vUX4wK8-k2Zn44CIYqeZIkWXnJDLiy-U3aRtjtWPMjRvsfr-eOQZqgJ-dSBrEwvxeajmTeLP2pjFBulpN9IvZxk63wWlp1kzaHFuN1Zvm8dzeqW3qzmVHMCvZDQHgyC5NB6LrL4q5gPdVJPQulLXKw6MVxeQSToF9gmIdw-5XZUUH0LoWU6PVSwJ7-1byZDy_KfJxLrrKLkqHoY4rdfT4eUR3N5yjZj5ME_PqARQ5c1dq5oGL9ComKzyjHWO9bm3tJDs2QbsaDizxxpkI0kMGUAzsKliaTI8JFTLSEExDGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29559" target="_blank">📅 22:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29558">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=sQJiwxjbiAhsJmZQBP0bhN9dvmU9IAj_rc4l54CiqBj1QGBx7EIbrrhFBbmW8w1YAbM4wWtg4BAh9kMnm59nEpnacGlfk-2FKxPvcpNWa4AIOCh7dnR3gZT5Ut0BGHnKZc0jVcPbCMNv5X2RB9S2RWE7Smqy9bf0i3ZbKpW99Qztz8ZxZ5u4Tzp9Fvdc4udpwBb2IotUm3b78zLsW4xPuZI4aq-6AUpMggzomJfmRIp79Z0GLI-w84esrTSVjBXTQylgwbBpocfKARLLWWmWzx4mpTs9_BBUWALjPGEFN-ZGLl_y3g83Wtm2ZIuPdUMOF87TE8PAtRio9ftI3eN7qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6e36c4c43.mp4?token=sQJiwxjbiAhsJmZQBP0bhN9dvmU9IAj_rc4l54CiqBj1QGBx7EIbrrhFBbmW8w1YAbM4wWtg4BAh9kMnm59nEpnacGlfk-2FKxPvcpNWa4AIOCh7dnR3gZT5Ut0BGHnKZc0jVcPbCMNv5X2RB9S2RWE7Smqy9bf0i3ZbKpW99Qztz8ZxZ5u4Tzp9Fvdc4udpwBb2IotUm3b78zLsW4xPuZI4aq-6AUpMggzomJfmRIp79Z0GLI-w84esrTSVjBXTQylgwbBpocfKARLLWWmWzx4mpTs9_BBUWALjPGEFN-ZGLl_y3g83Wtm2ZIuPdUMOF87TE8PAtRio9ftI3eN7qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
صحبت‌های‌انگیزشی‌رونالدو دررختکن النصر دربازی این هفته این تیم؛ نمایش یک کاپیتان واقعی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29558" target="_blank">📅 22:29 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29557">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeSRkEETdv_I9cDcBXo5bpdJFLI_LPwDVHSR_q1MdFI0eyb5atnw2M2g0I3UAoGRP1eJe1WcXjWN4aqcy6XcNFHO4tz4k-zvgDc1Kh8jshyc4Y92Nc9VzG2KypJS7An0Zn_E0fcYvzG7vy3nzykH97hEIXA9kp-sJLR93WL4GRHPYjTL0dAKFryTU8oMAS16xgxUlHDCu1KX2UvaxtZ2jBTLYQN1yAUXadjIGMVTlOfpsq6oqO3V9MO3br_GZGt8SS_Qj5XA0VOksHXUaxVvcY_dAV2rlhgf45e3tcAU7_9c33LtX1ZoYK46jNXecE2b8bq5s0lc1vQfgmtcdtO3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/29557" target="_blank">📅 22:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGWecTS4Qnlhvihub6eK-66hnWFTNv68Cmd_yiQUpJ9K52x8tX7YpzwHZyElXNAX3JNXQJT3SIFoNBldJZ669v8vgu1fTqfF4gx30o8NgwJ9xkPgUTDkyj63sLOqUIj0MT55pY-Au8HoOK9iKQEu4yQWt-3iBk2_a_H7g3DhN_fJrofccFeTzct6G40u_g780ySq0EnmISgY6Sg0ugE9SG0oOrYVjTcD-dlXG1ZR9KPHBq1OXySp60GfReT4ogTNnULew4s5iJrAyyLgFOZYQtypEzJGi7JojDIlqWihwoD8lfhyQVeTtlAaN-q7VtTjRTrhjikUVdJNNMQ9-Goa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/29556" target="_blank">📅 21:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o07O5RiDvZh6W8zJJm__jCTznVpxspxZuQceXHDgBsAuMIsfEKH2jPBng21nXb59uSiPjTTR1jrOtqv3heoChQ78TNJKDyghyht9tI_VlNxoftgQlvOv877Dc-L6ZyHvM1uMFcb-vB4PBv0mzgqG88Lq3qKnpG3GSbUW-9-EHhL-7AKtk3jRQ3O6nKR0o5hXMT7WTr2imnfJ7G3YW2LgpaUSk8rnbRU8NqlhibRc2E7sVfbRq4lE6AKyOPEdZI0l0XchoLNtN6Oc3bbs3yUlT1CQQ0l7LAFtm7gYMNJM2ehiqTEGpajKOtkCFtv5km1RFIITkpGw9EDA1cVQXKQyTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/29555" target="_blank">📅 21:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29554">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=o8AqTGvQlQGCpUnwIddbaqvb2YKCTM3IHLgKjG-6C3M7CDIHqyBwVvSw65WGZUSnhH4v0LfMvQbgiOLM1sLPmmOtlZPyUSbEfPxbt4d0w5lgncF9X-4O7-Q-J5Y32Bh53aGK6oGB_A8dmLDpqFLsrOU-eXHFIwtOYgBpGJ0wUyn23di1KRNiWE7IoPCu0ejssXiWz6v6YG08rarBwLO_oZ4nooF0q_f_J0mQ9dB9FVyrLQf7u7U05LkkI7HSpjM53P1Ey2gWz-pH3RYGb3lhLI_SV5i5-Ix-WNiPf7zx-xipEWnT8qhKxJWigC-mggzPi296rn61vVLs6jDoXx4dqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e054a17dd3.mp4?token=o8AqTGvQlQGCpUnwIddbaqvb2YKCTM3IHLgKjG-6C3M7CDIHqyBwVvSw65WGZUSnhH4v0LfMvQbgiOLM1sLPmmOtlZPyUSbEfPxbt4d0w5lgncF9X-4O7-Q-J5Y32Bh53aGK6oGB_A8dmLDpqFLsrOU-eXHFIwtOYgBpGJ0wUyn23di1KRNiWE7IoPCu0ejssXiWz6v6YG08rarBwLO_oZ4nooF0q_f_J0mQ9dB9FVyrLQf7u7U05LkkI7HSpjM53P1Ey2gWz-pH3RYGb3lhLI_SV5i5-Ix-WNiPf7zx-xipEWnT8qhKxJWigC-mggzPi296rn61vVLs6jDoXx4dqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت‌مجدد مورینیو از وینی با یک ضرب المثل جالب: "تو فقط به درخت‌هایی سنگ پرت می‌کنی که میوه دارن. به درختی که هیچی بهت نمیده که سنگ نمیزنی. به درختی سنگ میزنی که پر از میوه‌ست."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29554" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29553">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=bh2CEvSE7EjNjBEl2Zc9IFGFZqdabTUHSK7_nj9RNPcgDLlEDUroOdM3wHUtUoD-sKlOVvcLzxBve5S_Pbk_0jfQRwNXnrlQ1ZvMyxMDPgVvJzIQRI-QdA2Ovnr0x-RhH7axb6E1ZzoEFdI1AFFOTbY8m0Vr23wb44G1A5upG762MEeTHao5myFJfgd5w41W_Hy38dAKGnVjKT1WQRRs0RWDWAlh4erfFwIuvkfLFHXq2J-vB0G8CeiYyQu73aAjyKVXCBoWkRRhymz-zBFWTr_khXmHbw67zZOIDL5nsz8QbiLn0LOylsfa6gzKZLZ-PbRoTyCcJSYKB7y6PSJugQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac2a8bd0b.mp4?token=bh2CEvSE7EjNjBEl2Zc9IFGFZqdabTUHSK7_nj9RNPcgDLlEDUroOdM3wHUtUoD-sKlOVvcLzxBve5S_Pbk_0jfQRwNXnrlQ1ZvMyxMDPgVvJzIQRI-QdA2Ovnr0x-RhH7axb6E1ZzoEFdI1AFFOTbY8m0Vr23wb44G1A5upG762MEeTHao5myFJfgd5w41W_Hy38dAKGnVjKT1WQRRs0RWDWAlh4erfFwIuvkfLFHXq2J-vB0G8CeiYyQu73aAjyKVXCBoWkRRhymz-zBFWTr_khXmHbw67zZOIDL5nsz8QbiLn0LOylsfa6gzKZLZ-PbRoTyCcJSYKB7y6PSJugQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29553" target="_blank">📅 21:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29551">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZaV7kU8X0WY7G-SJF0qwk0ynmAJWbE3lHiD5vtRbw_jkCvnS8oMiJJihDPNHUANsy80MJh-7WU0hcXu8HHP3S9dydqBmdW5sKwotig1FnBRdWbit48Mre-khq2UhRKdH-rcUPVb26Zx5rWEpJJWMDOKOXwq3jUUke6M_Qt05qHlFZnDvY-qd00mbLKtRUis7yYtCp9KBYSGgfvczbbu0waO6ZX0bjK0ZQOW3PnyBd2c7QU1vtCQwujNlFdu8aYQMFD3fN834rBW9GWUyb3TXrXfeN5_atVTRfh8ldUlA9DeEvMvvhGRqb3x1ZcB0hGpHJJq-QMemdZdzxRX3srTuuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روشنک‌مسئول‌مسابقات‌لیگ‌برتر:
بعد از فیفادی و بازگشت تیم امید به ایران بین هفته هشتم و نهم بازی‌های معوقه هفته هفتم را برگزار خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29551" target="_blank">📅 20:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29550">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‼️
کارشناسی داوری دیدار استقلال و پیکان و دیدار تراکتور و استقلال خوزستان با مارک کلاتنبرگ: بنظرم باید برای پیکان پنالتی اعلام میشد. هر دو گل تراکتور به درستی افساید گرفته شد و گل‌آبی‌ها هم سالم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29550" target="_blank">📅 20:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29549">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiIhwuE0a6Wf3J6F9AXOs_i-yTKXBuorwvq3xF-1Z_BGmItcdPF6U96B30LoNLOP667MCJQM68_YHhWK2hrTnpeCDqTeQ1xoU44ATutUUobsfk6qHcHl4nyayrFyNsFKmw1y3VupAaMsqKLy1XNBNrdhDtTzu6F2Ciq-x2kcEctxbzyamr0DXnxfAWUDJ-irRimfxgod-bvmPpawFA_iLvOXRc6SwvDk4Y8-Pq7lu_dWN-3E049bkgPuspHoqk-Vqsl9lswTKlV6iWBi6TC6hCLe95gcK7-KctSvaHGOG7DnIoEwsdW-3CkQfE-21rHr-1wfLTvMPyIITajKxR2xLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نشریه‌فوربس‌گفته کریس رونالدو هر پستی که تو اینستاگرام میزاره3.3میلیون‌یورو که با پول خودمون میشه حدود  910 میلیارد تومان پول میگیره. در بین تمام کابران و سلبریتی‌ها اون بیشترین درآمد رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29549" target="_blank">📅 20:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29548">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHwDR-SL7BOISoANnJelNj_ZHJCOtW_TmVhZC0epllHsLVLBhXT33e-YVEFmI70lmtbaT4AdJAnuPxa0IsIIfAZBDBkBT8I7pEbN5qSmsvzZE38M9rgFBvw-1bsYgGk6-CAsK1WNLVY0vCBs19740tBO-etpoBrWFN2Inuh0mUE3llp1dO2oNzY0oTqYPgtx30FH62wFzg6aPPA355uP0b8BDLCFdehUYVycwOWxI0KmweT8efp4OriAQNgQ4yOAa1B-ljlBn7kbnsE5RJNzZ8ODpQlEQemKZNQyEBrIJ9bcmev1B56DB38dMMwBr9NCiFLyAi7SxHp14YAiNjXePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
#فوری؛ فابیو کاریله سرمربی برزیلی به فیفا نامه زده و اعلام کرده من پیش نویس قراردادی باشگاه استقلال رو امضا کرده‌ام و درخواست غرامت میلیون دلاری کرده! گویا پرونده استراماچونی دو به وسیله جویباری و محمود بابایی راه افتاده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29548" target="_blank">📅 20:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29547">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8kFjXKSCUZZi1z-g-bmLyQ_LPfS3OypsL9jlQGnAnwtDM7kXRPP-gwbS-Ac7ItlYLybIqZ-fcaWE4UlUH9SAOtNW43OFnfK_Rmin_e_QNnCW7NXPQiFw-F9n6GvJinpSRSSZVz87ZpomODu-kB-1NNoHFZTGCJAPWaiV39wopKIOqCxmcroKNesud47bZRf4QvOyjjSq9DL22LERDnYQNV8e3GJwD_PsqcT4C3AWXFF8Tkq76HZ19YWBKRYxDf85GT59KOx5ZXaa9ZCzLPFY66-GycCRTNepNDvkVXKm32uFEYkf5tTUXPP7X0m7XYCHGfJoMUVSi92ago4_IeT0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق‌ستاره 29 ساله بارسلونا با به ثمر رساندن شش گل و یک پاس گل در چهار مسابقه بعنوان بهترین‌ بازیکن‌ماه رقابتای لالیگا اننخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29547" target="_blank">📅 19:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29546">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4ZvP14XwzSE3MNHBCQkGDMZRGAey-d2puhCd8fdJQqNDWzleod7e9QmFX3iqnucWAEfR2nVlDnoThBN5yQti2iPk42q-wrbzKDhLIvgjB_r-YTrOhZjUHUCg7WF6Xt2iTUqYjxQsoA9XJgDhn-qAuRgp1FvvWjBcUdPDnXIE8p23faRfF9Cz0s1nYDVHB8ub4CXOEni0wOAVTm2wV1A2Lq4V4Cl3h7nDwp_9B4NGzMoR5UJ-g-nen40q9RqzJnWPl7_3mbuz7lcV4wYGBxBlZaW2_SPAuHtk0nZ268_mORcJF1pTwuiPuBracVmm0YpO4vlrwt2Jo-jve46RRcugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
‼️
علی نظری جویباری مدیرعامل باشگاه استقلال: هیچ خطری باشگاه استقلال رو در پرونده کاریله تهدید نمیکنه، قراردادی که برای فابیو کاریله فرستادیم امضا نداشت و فقط سربرگ باشگاه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29546" target="_blank">📅 19:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29545">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGfRVqcfnb3JaOrvXq-P2RbYXOseoJu-59JfNJjkj0B6B86_A-Yv6HiO79OsVfQcwIPA8EaWTvmaX6YDB8n87uQoQ90UCBWpdXV4XsA2I5FnSDhGNAA89B93-SGpCEaB3AwDAOi4j7D1ARC_b0D3_vczCQwOSklZYeWDvvRuTz_3ZsbMC0BhQMIF5HWpMuD_Rzvw59Ood3ur-C0jWBahGVZB9HB81zldztpgN_Xt4vS3PzhjYXvkLlY0e3xH-wSqvIECsa_IvDpUHHVMYFz8PNNw-Wdks3fdGfIArTqFSKaJ1tj6OFZMoKCKqly3d9lMxitQqVHl6gmbK5kxQfixyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
گئورگی گولسیانی مدافع گرجستانی سپاهان بزودی قرار دادش رو با طلایی‌پوشان فسخ میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29545" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29544">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmEh9ednDwEOVkk3E5puL1cNNy-lMGeQv47XgjGJW3KnZpYmVoIUEEEd_jb3FMJIAaNTj3zYrh1aIU27CRDnMx4RkVlhQ1R_vyp5E7X-Mal1wX0HndunK4EyuBJcv5Xm-gdYK9wM_L5F6be_B6RsvCH85ovEigs8HZbtfhvRvNg7RNiuzNkCN7d7qL7uPe1AfcXfLU7fSJJ-1ZpQ81O9szaHMviWiF3zjRXT7x_t-4zjXK15QPMgCdrbe3AfrG3N1CngPUXcTDZRGxdgolvtsChzz-m5BxwyfwxwJsx4fqd_6CuoFWxFMCvDENXqr-5TYPAcJaemeGAaJPdcgEstUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریهESPN:سسک‌فابرگاس و میکل آرتتا دو گزینه‌نهایی‌فلورنتینو پرز برای‌فصل آینده رئال مادرید درصورت عدم قهرمانی در این فصل با مورینیو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29544" target="_blank">📅 19:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29542">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOQrEVdULhoME19dp6RE_gGKGJc4SgR6ryYzrtECRPG9r_g_g0J7yEKN-DpRslw0m8h_Ot6zrJVg7NRySD-txS60eEeKFEe6sp_H6J_pvKJJ4_S3qKHCAEtp1y-FVgXrHvJxsEfdmc6WD37Y2_Cle09mefN8lPK_qI6n0NdmnEoYbngzROVKn1beeN7PnrZy7QVDNWOA6BvjLpwh5_JsnGdldXotIzUWSdysI7-qZi2C503eKsgS-8CeCzgnB-cVUtmudMH29kHPl839cZZuL548OsupMTmR4nOS4oZIhpR1ON0HRR8oBXcjjoZ8QJykGth8ca88K634LKA_DVUSiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت برگ ریزون؛ تیم فوتبال بایرن مونیخ  12 سال و 9 ماه‌ست که در مرحله گروهی دور رفت لیگ قهرمانان اروپا در خانه شکست نخورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29542" target="_blank">📅 18:41 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29541">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJNSMkQmpzSmJyxSvqTheTapUVXEqJTHj3N7isKefJ0CuZt2M0--VxDCjPKZZxseKkOx9INEtUj94-NxgFJTO5TDYyyqvD904PDud3sTPBgTl12AQDR3baY5bTLRM0i-mL3_gq_cWFCOIZLnshKUEP6Tlt4C2EFXLgAZLmoDdDj-UI58UsKUYfEaZFLkZxje9Wz-wKlgzpY4PZmVlpegfuM71Yej_bva0yFOA_DryKsYlt-CbkX7-__tFhT-F11yKVo24yZ3Sd7KO3-Znds9mbQOwZjUddBYSQw6CnBweML6Vh6cTBCJuZZCsp_VZA_QzLPk98tqjmb3Pjaa9zoDEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#فکت؛ ازشروع‌فصل‌گذشته رقابت های لیگ قهرمانان اروپا تاکنون‌آرسنالِ‌مدل‌میکل آرتتا در وقت معمول "۹۰ دقیقه" متحمل شکست نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29541" target="_blank">📅 18:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29540">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CygI58Da1RcHhtU3CP87Wd-7CgeR7-EjgVSOecdMG8iWEzDAQWXwOacRrThKEb4lv9pkQiZbk5VjaS8PwE4_y9qbSvuOI6H2vKnjfbhurBvXc-14XOxG0W2Y8FcqFx_Sn4Q8eBzb9bHS7Lq53ueqYCYp9PJSfkLRlnOTofmFwil1iCA__wPLyJIY14ri5x6lCPP5HzgYsOSPhfLsY-JzsfAbkQcPevpi6rDGvjiJdY7xqA2Uo5YXruQ8g-aCFpZKxuXz8vgClSdsGYQ0zjaViEusFstRrZOJ7tJQ4gZ-0DuA5LwZtLXf2IKUDUl47ZiZK3kZV2pr2bRt26rb-Ici5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در نیمه‌نهایی جام ملت‌های والیبال آسیا؛
فردا تیم ایران ساعت 10 صبح به‌مصاف استرالیا میره و ساعت 14 نیز ژاپن به‌مصاف کرهای‌ها خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29540" target="_blank">📅 18:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29539">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=liabT2PSR-fCtyZ_-aZxOPRFT4l1j1F_NMNY8se9NZSKFwVVU92B8oFSWYOtIUu7Ih4B6ipMhf4qtqlpUanqdQnGE6g-b6CDJUOZChH9ySF-nGQUEy4nOsLy76yo2DbiDszRuF3qYbFxmF1dO4DFrVYorpS-5Xq_aCIVGyjILN6PvSGIW_PWWQBlZl_T5HIgD2zhWvbPlnIUm6MoG0mNnkF8WXWy7Rf-l4YY4CopFOYg2rZ7B6KshZvEcegalf6suVjJZPeLO0Cn6z1MAKQ5v8Jo6dwNMKv3grWm6J7zGl2l-kvXRTD6NdTfaivnGmFePmLnxI5dBMujbXwECGLV2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57bb43418d.mp4?token=liabT2PSR-fCtyZ_-aZxOPRFT4l1j1F_NMNY8se9NZSKFwVVU92B8oFSWYOtIUu7Ih4B6ipMhf4qtqlpUanqdQnGE6g-b6CDJUOZChH9ySF-nGQUEy4nOsLy76yo2DbiDszRuF3qYbFxmF1dO4DFrVYorpS-5Xq_aCIVGyjILN6PvSGIW_PWWQBlZl_T5HIgD2zhWvbPlnIUm6MoG0mNnkF8WXWy7Rf-l4YY4CopFOYg2rZ7B6KshZvEcegalf6suVjJZPeLO0Cn6z1MAKQ5v8Jo6dwNMKv3grWm6J7zGl2l-kvXRTD6NdTfaivnGmFePmLnxI5dBMujbXwECGLV2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌زیبا‌وتماشایی‌ازدفاع‌های‌جانانه مدافعان برای گل نخوردن تیم‌هاشون در مستطیل سبز
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29539" target="_blank">📅 17:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29538">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYIk6jN-3BrRZyMaoGB1j-YEFNGfVr7vIo1tDtTDQnVRYoYhf0QQpqm5wTrwtkw9e1eOFfhcXaeBikuYQ9UMvYr5dcnk_18SEwTewbIHdzejGRGm5IWshvqfeVb4zLh_qbv1-WVL9olKHZZsT4542u6WguVLkTSvnL7iZQSUnPotABMNWJd7ttczNr1ojRvlwOLWRjS3CUeYs9p8zUMnrq3yWn-Xw0RIhX10O4dRcWonwoXdLMrX6_kZrNaBwmRFzHKlTRrJZn75a-d2-eOLEK2O80haxtDBzd3RqBBuWq1PTis_ihSJvxcEHzKf7dAGNoguNROt7dDSWz6ORDMr_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌مهره‌های‌هجومی‌استقلال
🆚
پرسپولیس؛ تیم مهدی تارتار تاپایان هفته‌ششم لیگ‌برتر با دوازده گل هجومی‌ترین تیم لیگ بوده اما استقلال سهراب بختیاری‌ زاده هم عناصر هجومی خوبی دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29538" target="_blank">📅 17:27 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29537">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=TPkP6Bw5tBSL1p2ci85LtxQ1tIq8fBXhtIB5R3SOULUy7xlNgpOELvlO8erJHOPL1gwj_0zBsDxJMzkame5gXM6WBIZk-d8Z_6MJhcvMozfZ57Dlj2e4l7qdwdSaCXAzmcB-ta_7srDukpcgHGEV6PSt6-wm0TSZ3mwvS9LbKJaTMJMASDxriWZ-ZYXJaPiMc3xL8mvmoNVdDDlOUerpFZNcjBZkwUAqb10LMqg_6iUrzC76YxVPyhVlZtTN71d5Jv06ca5wMw1g20lLsFZKqrI1ZuQG48Hw_jbGxnbBZlKK8pImvmMW7YuqBsPWGYhDO9KvjJBIXD5PR1UrQ32uQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dddf4f36.mp4?token=TPkP6Bw5tBSL1p2ci85LtxQ1tIq8fBXhtIB5R3SOULUy7xlNgpOELvlO8erJHOPL1gwj_0zBsDxJMzkame5gXM6WBIZk-d8Z_6MJhcvMozfZ57Dlj2e4l7qdwdSaCXAzmcB-ta_7srDukpcgHGEV6PSt6-wm0TSZ3mwvS9LbKJaTMJMASDxriWZ-ZYXJaPiMc3xL8mvmoNVdDDlOUerpFZNcjBZkwUAqb10LMqg_6iUrzC76YxVPyhVlZtTN71d5Jv06ca5wMw1g20lLsFZKqrI1ZuQG48Hw_jbGxnbBZlKK8pImvmMW7YuqBsPWGYhDO9KvjJBIXD5PR1UrQ32uQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گلزنی دوباره شهاب زاهدی در بازی امروز جوهر داراتعظیم دررقابت‌های‌لیگ‌برتر مالزی؛ این نهمین گل زاهدی در تمام مسابقات برای این تیم مالزیایی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29537" target="_blank">📅 17:03 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
