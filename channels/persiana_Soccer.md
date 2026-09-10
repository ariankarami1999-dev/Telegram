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
<img src="https://cdn4.telesco.pe/file/GE3yq8bkQ16p5KfNgI1Kp4BiaWvo7k82pOjoAtIfgr7CN_3e-D_u626RTinhoyhxxvIOD37Xu5BTiOoHmluS7jeCeiZScrC_OIWsiB2LHY6f3UKXcLef9kLtd-TJiE3VbtxzSmat7FKUqHvjkh_SS706tejLDHlzq6WVutfTtiLr1_5g-5V2_PeDSER3hsoW5zVw1CGif_BMggM3R24N5QGKJoNHJvFiJDmQzjS2RFOcBTlIAaHrUbpIW7YBmEtddo1HbPqGmqv6om9zPC1otoRkCS_IKZtBgLmxg1Xl8kybYdnXEaPoCOMMZC2sVA585RyybcvPRUf0hPI9dG2gZA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 545K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 09:42:13</div>
<hr>

<div class="tg-post" id="msg-29413">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhWWOEWUl0wFlU1cHJ33TRZB9tN8FeCFRuDVYvDUxZFz5VBuyXNr2hqFg1gMaJZD8X8JU9vBHIaOQTWuPE-UGlg-l1e2J5VIhHfEyqBymKOLeV52sWjqe1GntwXDoSjcc4SZgt-h4at8QJzGwklOIqJBmf3aAt8_Kl69dKu5g9nOAIf6a0Pqok19Ax1b3QqgwgbO-qfeCKTrUBHLfWduVnI8qf_wwqYqyj1feuRB0pqEI_vIEjDn1Z_w38h2jEjLCx1tW1RG41And_dp7_tGssabpj3-_MramvCxY4K9YwS_i2foLdKHS3XIMPWa2czoEStJGLgyY1KO3FsHZpvXiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29413" target="_blank">📅 01:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29411">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUu-SG__aIE-gZth5H5vhVU0TluQFP__O8qtmXKF9ujQSoSJOUF9XdjzkHdBw16FMZUtX6EVpDhpAjnSIAy5xbcrrHs3PQk9qPTxjaXKaH6B90wXPTlap6PfyaBp_yP4C8LX2xNhSixEDuiv6UeIKVTz91Ocng4flkyhv7a7kFaBhPHgT9VcKh0fve4VrGTJL5l5z3pck3l-s5M3JXCSoG-qZqT82ndM1oKUR2ao1wjW2jA2KoJqrvIBzQzRMyNzjK49xUScSuKBTuy5VfaFcGuxS-EKiA-LcCBYZht_nb4E2QB4iCpyP6IVyE-3x7ph-3NbG9s_ZQf8bwBVHdsp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ شهاب زاهدی مورد توجه چندباشگاه‌لیگ‌برتری قرار گرفته و احتمال اینکه در نیم فصل به لیگ برتر بازگردد وجود دارد. به زودی اطلاعات دقیق‌تری در این باره خواهیم گفت. حتی شنیدیم ممکنه زاهدی در نیم فصل یاغی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29411" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29410">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1208f58f58.mp4?token=Iu0hNR6vg9kzMmEBcxfyln6nARfm92Y0pkiSUfn3iDcizoVrqiiL7y9n3rW5W4Kyw9VgFOfefsCpb8fTDDs3_vcDuCdQOdQDx7ZPBbUaCyJQqfFWObOqL9aK1QX8xDOwGshO82gMAKAKkMp9mljeQMa1QlQfVk2uZMrPyuh_krZd9T7kP7k4Rdtvf_UXTZD4xZX_dkhGi2pLOZDKcQO85X5gepuOPEuDccJZt2YfKt99AXQJ-kyMzDHjuz5ZurY9S_g02GuMC95n3yF9qXHv3CYgiubdvFPzwFPERiqBNz-pPRforO0Iu7tDQkFydrWXT15NHmeuNFdaS51plBU6MTaR4DZyawfDE_vUa55V3KCxBttCdCuJXP13in6tQsDv5oJU-198Dq_Lxxy2WSIMsp7nsuhePLAVRODLfU953ZeJHSIRNLQE8evT75azmMaEfcIo3RsV8Z4ofdCnlZQcuaAzFCwah-DvROfhogER3ulj5CYMR4Yt9griZcLJhKucnOYabht1O0yDm-QBAGGOOZOTWZs7wUtUe8U9ouOyOs1trOpR0-hJM1r-fayArrg8jczFd7zyNM_SDlkHcqcoHkp-I2zWUDF01vmcJFwHwheIo1wkhKURMpF9CgovP4VwQdCVUyG5fH8zzB1_xWeAI22UyzpQODuNf7eyPFKs0Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/29410" target="_blank">📅 01:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29409">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGCWzH7L_xJyFpkNsFfazWxQHPa7VkzZ24heOIuwt8M3sAw6YqbKhu6qRJ2V9oVp0vJg_MWHC9YkhK0C9aMzBsP2HF83fDjjYsrLqQEwkmMMBnliiXM9Mj7x6TpH_z6BJAniNRwlkIKxEDpKjeT8cSxjZYQF2kLDPDv5bk-iwodkVHncLIDeshnJApdL527oRyw_LtSlig0spnZPMhmg8zgr5GDkSez2lCEcmdTqqcl5y-4aC65g0yyGBmWWveY6Wdz2FPl8ff0INzbOKP_QSe6w6X8SEfS0aTWjE-6hL6sjWygKkjxtrjnvWr1F15VGPIXgv1CTq3Ci_vK_kZ-8wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#تکمیلی؛درباره محمد قربانی چون در لیست مهدی تارتار قرار داره باشگاه‌پرسپولیس در نیم فصل بار دیگر برای جذب او اقدام خواهد کرد. رقم تعیین شده برای‌ رضایت‌ نامه قربانی 1.2 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/29409" target="_blank">📅 01:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ZKIsbwe1XKsWFg7jzO_X0XbLRNPtIe3xIO69bMaWAMCSB8DR9QajUDy0IOFK4Yi7EJRdqbR1PCARYUnUPtUR3NV6zRCLyuHrEjzV2CejSRRa1q2koPjYh61MNSfduqD4UODwzQVscownnFdU21JktVpZ3LuNcOy1IXCc3vKMSUrMrJf-mcBfnUVeAnMtAwHLk5pG5LATVW4M9kCYaorN8L_Ah5AnXeUrNc1AR6FcLH9ry5Zn2algkSUegEE3ajnXpaUUlLjdW3reQgLebXaKdPfzUrisiPyO1muu1nvFAkjqL0zdgnW3aNf93_6vgIoAb77-7KZNz55o_4i0Fwmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌دیدارها‌ی‌‌‌‌‌امروز
؛جدال آبی‌ها با پیکان و نبرد یاران کمپانی باپدیده‌نروژی‌فصل گذشته چمپیونزلیگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/29407" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29406">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgJMa_nXMuYw1vUDGPH6EK6qZZ3jl4Yu67QizZaZ3_DwhWUnxzu9rejkblV7yu3GRnWiuf8cbdELkb4r7WxZs3115awxkT1_7_XC1GCQlCX0FimMwwnHBM90NqGW2Ac79u4CFqJOepKR-z0DL9P9L0vV7cKB264r-CT2AT3AX9_2kRFX112G6NApVWdp00cIPI1WbPQnef7MGDvJ0LABbg06hAETnI9LcRKEjIHetvb-uvkAY5zpqkAo7PlnIrHxk-mPDov8XqEjbUsGA7AP1S3_NVvVxZl8MD4GYFOKjD975YbO5ZxK6oKSGl0GkBKuMsX1vkbW64wTj-fKhokaYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردارزشمندلیورپولی‌ها در آنفیلد تا آتش‌بازی بارسلونا و پاری‌سن‌ژرمن مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29406" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29405">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MWPJMiQd8TszbfIPpxRtijPXHOcmvx3ABt2mmVH3Nt63eTd4juZBBCLxQzLH4rWF5kbmeuMTUHFRD_c174UNuxogUlaSXTLUR1AA-b-6dO5Sy4ViXxZkH1ysK6x1XC_z1VRNtkFhEjTZTBS3SACwB_txzR92jarMEdqdi6lfj8wP35lkNGrcqICueJfN8IupOKWg4rcAIOd8onvFLPINT8M8fMxRRmkC21asou3_u68E3d1cfTweQahYie1BbwjqsDsy5Kmb2Nis_z-0vobl_b7hjOlHawW5iyydmP9fi8ge6KaNMJujyZVd2AtpFTLXo2eZz7mcN8djM6id3DAbtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
درمرحله‌سوم‌جام‌اتحادیه‌انگلیس؛
شاگردان ژابی آلونسو درحالی دو برصفر از لیدز یونایتد عقب بودند در نهایت به پیروزی پرگل شش بر سه رسیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/29405" target="_blank">📅 00:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29404">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇪🇺
نتیجه کامل دیدار‌های امشب هفته نخست لیگ قهرمانان اروپا؛ از آتش‌بازی آبی‌اناری‌ها در نیوکمپ تا پیروزی ارزشمند آرسنال در ایتالیا وبرتری لیورپول و پاری‌سن ژرمن مقابل رقبای خود درگام‌اول رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29404" target="_blank">📅 00:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29403">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdOzZ_tu4DrFt8nHj8-kxfNRh5qwajORmxfXIAIoDVkToiwP3SJGWeSOe_7nXVv_eARkTDtgl_SMSje6p_h74w99S_H2WV8m2oFGLC1Xk4tqdqw52SCUmsA-I9dKJsvO6CcH5L6ZIRmfDhJre43lQY2d0bL7V7PHmvHQlrHFDy6kFbRpPSACc859GRnmWkxRQrX3CMHprGFtb-G4_GrN3rzafvqgymF6peYHTdKb1gRcKh6dBAfjd7qNB6bVDNJ4T3x8OXg6tixFgrOX1KdSP6WaFZsPsqZ0Jo3hzZL0xqwF8IXVa670FVy3dvWdO4GWve5exaeucyPpneBNmxaKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29403" target="_blank">📅 00:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29402">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hllMlVLKMf-_x-FiByp_kQEgnkHRaWAXn4wzyDzX6C4nFp0W5-RnYcwL51FXBx4ovvlbD9GKEJAZOwaDEx8H-hybhGVcWlR-tBn2e92Eh-3x5K5s6bRsUcrcXo0BozOBkJRlj37JVK7B_wXmGPASXm4Hn0l0XLmcaVMIA4PeH7AA4uUMUvRIhvfoQ03QLHhut9gv8ydCYF0Pn1ujG4JVu9tPQjdUY4tfx7njIqcJUuUCWTCNTXaMVT-zwV04x7kjCVx_IZzobuVTvnQzCwCoqyfxm-5Tjy1eZjgSFLHTRtF7KGmTS8HLqIgSLgFWykDzWyuDv3McwG6gygkv1pHYvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇳🇴
#تکمیلی؛ باشگاه منچسترسیتی انگلیس برای‌فروش ارلینگ‌هالند ستاره‌نروژی 26 ساله خود در تابستان سال‌آینده 200 میلیون یورو میخواهد. از بین دوباشگاه بارسلونا و رئال مادرید هرکدوم این مبلغ رو پرداخت کنند بند فسخ هالند فعال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/29402" target="_blank">📅 00:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29401">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZ398qbo-C1PneaLxriVTRaICgBggE1het8uYgAlh7c-Y_zNqZj6aVDb8HeXnk_4M_kisUS4fLE3-sn9m_6ZTXHE8_rgRFIoVzNsI0G5klpxv7-6xEr8HKO8EF7ozVAT5SXd63MG_uOWIOjEMOAV3SA6GWVIPpSOYm3h6Nagjc2F9qi8DKURyYf-MrK-fkJuJBPwtDn8MW9blmN7k-wN72CZY4MfQY_J68zT7UguJxJVpsShxyhcfMWt7HrCFmVScH7me9JwDm3tuGIk7N7mzjU2zfNTZk1zoumgN9Xroyxfn--m-2SVHpg6P3c4yhmhTmAhJ-Dxi1epv3RLr6lRHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
طبق گفته اکثر رسانه‌ ها؛ این آخرین فصل حضور ارلینگ هالند در باشگاه منچسترسیتی و لیگ جزیره خواهد بود و در پایان فصل راهی یکی از دو باشگاه رئال مادرید یا بارسلونا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/29401" target="_blank">📅 00:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29400">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a8082900.mp4?token=vOB7Z1uzXphqy3T5Hv4wHUorgVBjE0BVTUa0XoNhx-B_zHTOa8kXusXSIKRu6dDO8YdPQ_-5wwZ_4tCReGAxNS3nfGbT652ls8CpMFnqV6wn1d7TfgWPXNMhyVyfNEW9pENUkNGDlYTiJ_cupof_VehFCvBzDltn-84EkVoZudiLf6mIUN9mAo7q-k9Nj73uWr-YfKMrdzmbgrfrDq5LYF2bL7vx7ZnLViVnWRRZSpsONMgSNATlhjxek8Q-yAguMJkmhyfsMVdj8D_eWHqk10trLcjKhyStd-2MH95J2yqTeneZFgfRs2pD4ifmE3JZH-9Bdxw_Oi2Cq9Fdjw0gFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماجرای‌ازدواج‌محمدپروین‌باآناهیتا درگاهی عمه دنیس اکرت مهاجم ملی پوش استاندارد لیژ از زبان داماد سابق علی پروین: پروین بشدت مخالف بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29400" target="_blank">📅 23:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29399">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjQiIH5mlgQYBMt0ScIgLWsDe13K6AO14VAIYrnvUYvuOLgyQaefFUs70O6zhSPbJVDVS9yK2-qXDIjl79_17mjAT_9pf-jY2_mdmYDR1gSrO4QMnfFBRdWHVddqoEi5FJaH6xywL3VotzL_FRILIVZ6FXd20oyrzgIRGE4K7BJrvWJtH5dHjg-zVFWWLbmlkJVOmTpbu0tJy5p5U8LXmtKcKDheJz3TxzFECKj4vNYzbPdxIu_WcMXJR6V7IWfhGyTJxjASyWjkjhBme0sW1A9K3gksWMI3hYrKDMfwCmw7kjqHHQHLG723OAXg7lmGIvkzIxwZEcIrtNEZkyUIbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فکت؛ رافینیا دیاز با گلزنی مقابل فاینورد تبدیل به اولین بازیکن تاریخ بارسلونا شد که در پنج بازی اول فصل برای این تیم گلزنی میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/29399" target="_blank">📅 23:27 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29398">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2rzAfCjsG5MTE7iVIuMbJBQhggtPW1O4RyFTp9NVl7Zr58PbzK-hF49wcMtBCYnGZcwG__b9zWaEWt0d6t8L3E0dSvCld8v_LwR_pfHgiWM2Qy0NUzjrkA05G6HXcIQTyrFJJAqGZwfyKfBGtO5FXsSjhLl0PyqagkIl4UeNZpkSIpRHVnPIMnvbJxaNa6GtrSKMKiZgGU22gckW2njvSU81d9l-VuAHN2oLj8LG8T8PlGG-Ex4pn_MQQuzBtuJxZIKmQp1I_yqF2nS1QuVlLgt2ADOCw-sCWmiGLdxl-Z05776fo7CdApMO3S6Iz5Zq6PvPK3E-urEghlqZBKn4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ لژیونرهای ایرانی حاضر در اروپا:
‼️
علی‌رضا جهانبخش: اکسلسیور هلند؛ الهیار صیاد منش و علی قلی‌زاده: لخ پوزنان لهستان؛ محمدجواد حسین‌نژاد: ریوه آوه پرتغال؛ میلاد محمدی: ویتبسک بلاروس: نادر محمدی: دسته دو فوتبال روسیه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29398" target="_blank">📅 23:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29397">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TidER_c3xPHfKbffVsEegA7VQJWYiYwj7j6SV6nT7h2fz-ERFsyFV9FUyNVlVJOXkGvYOHgBoXzo5c42w3ll5NAZV6E1HerOf3qtiwndM2TX_C3iHBlsKU6059UV-OBqriVODjvpWzturYaMzwB1LF1Wwq-EvlR76cAgQfebfTvWFHvV8tCw3Zu9NcoSn578eLk_bPX-AWny1FU4Z9nNltWll3Uzp8xIwE2rhjH7JNEg-f-6NmOrpUAI-VX5orF21qKu_iYuHiGC_R4VQALCQKzyDKBLSCQUvbJXGX40rT5TLqMPfNRrFLnEgfw4IVYAY6G8NRXBbU6Bq3lOw-SPmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نتایج درخشان و خیره کننده بارسلونا مدل هانسی فلیک در این فصل: 5 مسابقه، 5 پیروزی، 22 گل زده، 5 گل خورده، میانگین نمره 9.3 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29397" target="_blank">📅 22:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29396">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGZIpEL-VDVj3Pq2vYWP9HJ1oqpWvJv4CHNdSr-4ysAIy9Oa63q9TIE8vtz4axHFOQW7aoMVs2Iyjar0mIc5t3G7kTUB-xe1dhHHhMGqqz7LhF5PPB_xYtgRY0PujYBRRitt7NONjpTlezPti67rfo1KU_NM0mWopxpbdmN3474bjxeS2r0z5WlV6NXj7xEzdSFi8kLjXqyn1U9cDJfY9bU3TtKnDsFOEZgZ0lGGzOGyPOZnDngtrY8E_iZn3pFrJpRggpm71merN2IKWZu8MUtc8jpothO4cpgqpPVoB9HGg2qsBdzfSLFzTrNqLnq1KfiY2ZmoBzYA73I93fkDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇪🇸
در هفته اول چمپونزلیگ؛ شاگردان هانسی فلیک درنیوکمپ آتش‌بازی راه انداختن و با نتیجه پر گل 5 بر 1 نماینده هلند رو شکست داد. 22 گل زده در 5 مسابقه؛ عملکرد استثتایی بارسای فلیک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29396" target="_blank">📅 22:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29395">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHLyr7MHJbJ1qIQAujBe48Vjqbh--URTzYTL0xZUnvgPcvDNUf5ufP9xOMdvIX__7ORJvDC36knzndnP8e3vgnSPrZm-bCkcmtq_-FVhh-ZWB1BTBWkCX2cZCjIghEHOPiqyITmClNocEJeJiBwlueWdygwCpdPgJBWQkAeINLrp8-UO5Siaw8vs1EvnftqdV5wDgDpjaO31MaYWGasJwzfl1yGq9jITpBAU_HPgj-nz7dKpRYd7LnYSUgHAPw904hpxaRlEZWy_DD2hwkWO4onmVZ01cpeyGcbEatlJNExtPY00UqFxOZtE0dTg8fUw7wUHUi-i-nyuSFXPQGmnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کاشته تماشایی لامین یامال ستاره 19 ساله بارسا در بازی امشب آبی اناری‌ها مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29395" target="_blank">📅 22:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29394">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adadb2bd3e.mp4?token=T7l72szkelI0BW_lmgAcvnGIl2K8hC3llM4Xnfyi97v1GelpWbM9c0ETlKeOBUX3biuhqraWAKTLSOekLN-DxveXoUpulqiA1CLzVyYNaABdaXplh8EpmqAxYwt68HEh2zI4xZDUzsphz19-Gec1V47vLaqHnI-Ks46ECYOlXtOVH7Dq0t1MJDk-pLs_9Zp3sCPkJ-R3irYR2BcXO2rvPYZga7-aof9dkK0P7bS0Bd9R4dotvrne_pg9gw0w-bQSxdXB7lQCIhc5jMr8khwymMMnW222CO5Q4t86bDph6uSuL-6qddgbOIs46a2Mb_8iYo4cXB68KmqXgwWLfOd50w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
مقایسه‌عملکردکریس‌رونالدو
🆚
لیونل مسی به مناسبت قرارگرفتن لیونل مسی در لیست 30 نفر کاندیدای توپ طلا و غیبت عجیب کریس رونالدو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29394" target="_blank">📅 21:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29393">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135ac654e4.mp4?token=fkDZ3p17jmBSMPE6-EKJ8PkQtVCl8dYNKK87XCIiXnEfUoOyRspnDuLv9IuFC3kiLDFQDfzLYb-aw-v5bfg-s1QaWhO1CrM8UJsIQN8NGbQQBKq56vsTXn40j8qLJ-DyvnpmKePOuq2tHF-JYVfLxLLUaMxvHb965Y-HCjja4lNCDlDMnsc-PlaNh7qQOfHF1NLyfl27_v-OdXIthGOKV_vxGkTSolVJqEVqrlFQhTX0frDnhCNUfsg6422xxGwafS1Bo4-Z0Vygbo3TBcpvhl9lTLTDUCbJpiF2VA8_ox_LToUMa1JrNa1oG_7hz3Lk6xtcF-BFcqflcmDvGqEKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
سوپرگل‌استثنایی کریم‌آدیمی ستاره 23 ساله تازه وارد بارسلونا در بازی امشب این تیم مقابل فاینورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/29393" target="_blank">📅 21:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29392">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8GS55aZG-GnbfZbOHr_Ch7LvkkEs0c3gfs9rjrqv7srkdEuQu3-Zkj5rJa-XOcnSw8HkwJI5YzGrCmtLQhZRZmbsyvOLrubTFfAqfcwypH3EhtAgUi2Hpo3Mr5_7thaDQycAAXIaV7WmYX8Y9MgXBo_bDuG4hxi8xBhzRgBcVCjKsJXf1ADRGc5Sw18O5rSO_bpvRdWpHNMtlVB091JOi-mNNlKqoxjGfHg25tCiAZgfrwQHO6hldGK4hEKKWg9J75In7ZfnguidCUp3YAnvwyN_fqZPFfvQr9pIvRjA6cI1W1LHaMSZT5oBhJyeJpDzSpsBGVnYSWfkSSdE9Tnbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب آرسنال و ناپولی و شماتیک‌ترکیب اتلتیکو و لیورپول؛ خولیان الوارز بالاخره در ترکیب اتلتیکو فیکس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/29392" target="_blank">📅 21:39 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29391">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a9709bebc.mp4?token=BF3J8Tnw0hdHjDapINdzpT1va7Xis9NEiMJ04V_VcLMGDlZ03iB_S9JFlocSGHd50DDg_7N_d8bUCReNlflVPzt3doinSrJXbCK5c-D88IcOwG9Uhz2UDKWd57VEZVQQa6Q9uSfj5ItVjmvsTonipI_wETPj1TjoKz6Mc7a3dI5FJWMbjRKKeTCKjBx0VK-M0KjOS9PqlDjoV7fUMr4uodwsubThPlonZRuK8EH-P3BXQGt5by8qu2nGMf6mtQ4lGGfjBTfbRl4vigEkV5CjvcJPmENOJNvB0tQVxMcYcQn3DhDMRqF1N_dORqzUyUNWgcB96vlrPkZT0wC5bkTbrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آرش فرزین دامادسابق علی‌پروین:
بعد از شش سال جدایی هنوزم لادن پروین رو دوست دارم! بت زدن ‌هام رو بازی‌های فوتبال باعث طلاقم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29391" target="_blank">📅 21:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29390">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KymZFUbrAriaByXA6HRbB2yxl2fCCynpuMWCtp_CrHjaFwQ0glCANs3CsFxPdyfsiYm79X7voPa8l4O13jLvFqyvtCV3V-vsfC1FQWGEW2P0Rp6optd4RukkhfhPn6M_VsHeOPzmV2R4-KNShdrtoTNTkR3A5HovO2NRLnm4pMDfrpGeYBSzbnJuBkzDdCJNiPNvxpZzpeJF3Mf_F55a6gpv75EvlRN4daETf6jPmijkeMLhbNldqFCVHWWwi3hvRPI8w5GLVgJCNWy0FhpjVApuUeCP0_j_qwZo7Lnz_HfS6gAfmOReDP54iunSN8U7NBh7Hn5LHDzSq4tjkX-7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29390" target="_blank">📅 20:53 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29389">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/448238a183.mp4?token=cmrVQMn97WoqAFzpyjRXYA38feZ2SgcfiKuk51dXhq1nB2PATlvht8xeAWeGXKwOZUOoEBjfRmXHf5cOOIf9aPmMwfEGHvRYQqYcoUsNQ7SpNCJmtMcqJFwFMKB0XtwVhu1YpSbGQW1TPkqZv-dnf3LSuFrhAEWsQv4sxz35Y_2lwkNGBl4O5DNW1lN01xfgLH9kZOnMsDQCVfkXu3fNBrYrwx84mHQJybT7on2ZCHIsuQnq0m33m7b3KpNy4Nb1mLz0Kd3nba6qPCZ5skOiSRUTym-sAERkBiom-iCTJBgpXxgPS2Gnh8O1dSbquiUvr7ZYjKG_99nPsXO4tns1sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/448238a183.mp4?token=cmrVQMn97WoqAFzpyjRXYA38feZ2SgcfiKuk51dXhq1nB2PATlvht8xeAWeGXKwOZUOoEBjfRmXHf5cOOIf9aPmMwfEGHvRYQqYcoUsNQ7SpNCJmtMcqJFwFMKB0XtwVhu1YpSbGQW1TPkqZv-dnf3LSuFrhAEWsQv4sxz35Y_2lwkNGBl4O5DNW1lN01xfgLH9kZOnMsDQCVfkXu3fNBrYrwx84mHQJybT7on2ZCHIsuQnq0m33m7b3KpNy4Nb1mLz0Kd3nba6qPCZ5skOiSRUTym-sAERkBiom-iCTJBgpXxgPS2Gnh8O1dSbquiUvr7ZYjKG_99nPsXO4tns1sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛ شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29389" target="_blank">📅 20:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29388">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
#تکمیلی؛ پیج معروف 433 سه پاس گل دیدنی نادر محمدی باپرتاب‌اوت دراین‌فصل رو پست‌کرده و میکل آرتتا روهم تگ خورده که این بازیکن رو بخر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29388" target="_blank">📅 20:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29387">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_iCbwshzwJqlJ3VUwMQa1d9AzjoFvCWn9dqioXwrNLj0mGt-hLy-4zSIGnven-3_YIpEwcQlMxhNNLstYHjRV5li8ygnJYza-s05qomKm1Mz5pFxXjn2DPhWgC8Xi947C2Q7zyFdjLUROC9qFkAgdm48Hzri6Xykua_jdDFYgsmKcFBgY6v1o28jyi33lCEYsl5klq_cJfXf3GrRIhhjI9FfBStOVTCJAWzGCXNN152IWTdSLxv5QXqiLq2WiSB-Z2tVqeCK75dhBUpmfzDHXBSXJeirIIpjCPAf-e39MmpFmubsqlbUuuzpcCLC2AxIbKbhocFdch028MYbvj5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
طبق شنیده‌های رسانه پرشیانا؛ سردار آزمون فوق‌ستاره‌خط‌حمله شباب الاهلی برای جام ملت های آسیا 2027 به تیم ملی ایران باز خواهد گشت. بازی های جام ملت های آسیا دی ماه برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29387" target="_blank">📅 20:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29386">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYQ7kXPNXRzxO8bXoSjE84sn1pacXfq2OCrUeOny2A-JT-QtDJ9TTgahFoo7Os-XIUPfcFWggpVPnp00LL0lq-GN90mj56sAQHL5Gsw-z9v472TTUcN3kUN4Rhd9nXhxxGl1covbOfDpxWuR54HsxU7WQCBK1R7_4xlSoRXHRU0sjvS4aCTA9Lsik0ocn5f3D8qDRoRvWxP_pnJc3RHyERueqsYEhnqfgc3nttsosUw2YdmYDp6K4y_XeFUq80laDXwRsC1xzV7_2WoJr6E8i87b1VdZG3blZzRbnp8PDsyO59pf-rKf4bM0ARpg9_oD6N-wG8jPNEGFVDw1akC8BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اسماعیل کارتال سرمربی فنرباغچه در نشست خبری قبل از دیدار فردا با آاس رم: «آاس رم فعلی قدرتمند ترین و با کیفیت ترین ترکیب تاریخ این باشگاه است.»
حالا
ترکیب فصل ۲۰۱۵/۱۶
:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29386" target="_blank">📅 19:52 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29385">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlQqoohh6whSrs5JtYcR3d7c-BuvSblfdoPGuMl4QkPqL1xyY08HqVopLX8ZbHtTE8dh9XSQ6A3q-Rj6iWV6dHPmMugf_bvja3e_HYxgR5naovi8Yd37xpbVzyo7_5RTDq-x5RkkmS4d7_DdZhP4QvPyc3D5mhDZGwlSK23i4oYAlmkGh8NzfQ6CED9aMBQEqKaqDkAZLCOTYTgn1pM9gvEnMlKSx5SaNpWkSijYQlYmgrP1TyD2DW2-WaH3L0rMHm4dNXB8DMjKxb90ZDiCp8GgavQQBc2CHfVT_Qg6nk4xLi-j8bwBsCaXKqwEF2Jsg3-_botE6bXF4ARkfPCsaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛ مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29385" target="_blank">📅 19:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29384">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rM8e0Be2-z8LOx4_Y3KNjqhaI5sU-X3NHSKau5wa0D2e_-zdDBdIbuknhN3XgXsVdelmGaePbpbtqm1HN_JnST609OnsgxaHeM9L8EI2QDVf0pu41Mmd2wTY46NbURlxWFXSSTVL5q1GTn39A-uWkWysDq1EaJMc4hQB55Nsfuf_i6bAx9k22kRgFBzxNP6swvtp5xkrXDH-kRnsZqPgKK-QJ98I_rudF_RjN431D_NYKFJ2mdpsdx_CiwDAuAlphkVgvQzrTLVTW3i4hB5shUw8lphET4ydSLofP08Vrdqk1WtHzm2MZyzH54VfcyY3hlGvaOq931HrV5o-dqr8Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا؛
شماتیک ترکیب بارسلونا برای دیدار مقابل فاینورد؛ ساعت 20:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29384" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29383">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3hv0ywSTFqRLo99mNobN8dk9BXD1ztau3aFZz_tx_F312MZ8Xvhyb2gtpulKqCWF5oUYo3UBDG8e2zgUZhpFNOkU84ii8so5u2ecBiGiGh90tXBKta9xBm1Kf051-ZqDGL3ictaXf_lQUQ1U_82NBzlQR1zKuIszq78FHmbcJDmSfmUvBSOwegdz78jgCbtnXJOGZ27GzMcsXXXE7XGVJNcAcG1obwi5lmhKYYGMj8pDADhAM5XS2Vnr-hoHq8Rlp-DET9_5c7QXTAC9zYccRpYUGzhq-Gal571Xw5WYrgCbD2GR0mCyLw4cVglgIGI-QmZ_NNchq23tipjvDOoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/29383" target="_blank">📅 18:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29382">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtUYFPErhWm_buH4AOvM3zYJ-XL6AO_JZAm8BV8bjkVqvHXM3It8ZjAnvGuZc9CBMd7R97YRNMyDoyRI3djsiVLCXW0X68HSUIzi6IoNyLfCF2zBg6FSCSDuRApi28fz2BEUWo7OdIglfu9rd8vsMyTWnJGRq2hRRjqgssvOm9mLEQhnxrTFQN45_WBD-96Qbxm9NSmhXRfhCspncwP691yhOSOkOZKKm-KIDoS3e78T3sq-juC-iLju5qcFxE6RNOWLmXe7816wjDzdjTrZ24L9oyhInJdE0l29DyxetcFq8RfRFQFej4KelySnJJNpysrfhwBFG0ZehHpV8xKQ8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/29382" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gnwlu6dqFI2QsWQB_hwdSsiOcUrKzx_8poFjv_zH36tl-aPqD6LPU79to6fCswh1j55-s6LPfomvbWAQ0kenjxectfnVK8zCzRb48y9v3b2DmQI0Abx-RlrIJF7LY3N9DZ5euwxKenNpVRAX9Qbt623TuovsArgjJe9PNh1V04Cp0OVVJ6HeSa7KXiC2JKLXgPMm1fQIwcT6WNck8b9CWwb3-XZsp0CRWAzG1jY5OPd0ahG9dxvtjNH-RHGcM9baG2oQbU0OKcLfSQQcADeB0ffHAXohUH0rA-rjNDk5N_LXH6PP7PsIjOgAYBWHwT6HC6DvQArzp4E4grn8XReo4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
لیونل مسی و کریس رونالدو آمادگی خود را برای حضور در مسابقه خدافظی کارلوس توز در تیم بوکاجونیورز اعلام‌کرده‌اند و بالاخره بعدِ سال‌ها این دو فوق ستاره در یک تیم همتیمی خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29381" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-4YbP9ZnEDj1iw4EfHWY4yGRmLNp51pt6Kbdy0s1kJQK5ALlIpMReKhSHZ8_GM0kr1teVYKeKr0kH4GC7w-Inu1wZi8oJLQXBuJFvHFpxneShMspDzjU5t0DHRZ4_2Ez-nJTkJCDEs5H977jJtCqjNt9pNScKYufSDclm_RffeiUvehSIY65XAOKAN3tX84FOKKepUoUq1k_-zFbkQaIWDydj4Df1zVqECsZWgkiFqI6QX_blQ1UPRXIbQyjrTBwkr9PTKi8awDriDowLnSjxfQmcRuVTH3nE1Ascl294YdXgGfUh2gFZQaMgwCVMD5u_TZu8BlhBxF9rrYIQyfsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیورپول
🆚
اتلتیکو مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/29380" target="_blank">📅 18:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYQIM1eO7SdjJV1ZyICbXxxIBdxncsSDIQtZ2rINk2lpI6Cd9t1tMUR5amUldexCuWlWhlTUP4RLJTuV2U58tG0dFBpByN8i5JiSMBnhJebFXdgVTvuvhkXVYLKRUiu8S5ntz-olcqhebk3i01iGHWTkBHfQUz-v69RUf8wwjNCFSSGM3Fv0oYgjdsuWoIC0IgDW8rI0z2JEKg9Is4L2F2jfcfxp9c4OMixHcMUfK-7Ui3guGPITHwmDHASr5hAlH7LS3isjAVlT_yuqnKXSCy106d8Ka_8ssmNUbvCRuqB9zpMc_OSqZqBW_s9PjRVjhNR0UT8GeXgMhJ-yKZf8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌بازیکنان لیگ برتر تاپایان هفته ششم از نگاه سایت متریکا؛
مدافع مغضوب کادر فنی آبی‌ها در رتبه سوم! علی علیپور بهترین بازیکن لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29379" target="_blank">📅 17:47 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbDLfDpqlCN94zk4rOL6THLo2liDQaQ4Kbt5hIJZY7O3KEZYwzltb6vzJH3mKkhy5Z2VZ4E-NAsF9D9k3EOowbHtArzvWtKQTjuHda_fysTcyiV3DI-E9EFcYPcAKk_OwZcaZL8uFocOF7hHwkbWqQ53UNLnlFxDhi7DiyT_RK_zt6bkgzxBH62SUprSJYGxNKqxs7INf-zr7awA0DFeBh1OUxxCjK5a6AutYm0TdD2wYc69ZlKepF1dQ-CNC_W8qYQm2MNn2YtPCsjeZfmT-y8Nycd7YWeGH7m7eUkh-Obq1VzJKQ65_DhExUcJAylMhPuwXI-ukBrhQHTgHWB_XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍏
💵
قیمت‌های‌احتمالی‌آیفون 18 که قراره امشب حوالی ساعت20:30 بوقت‌ایران ازش رونمایی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29378" target="_blank">📅 17:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaCCu9F7l1kicBoy-qmvcZ1hjXUjjpN0TcWlqFxVDG1U5mkbqEi2-2LW_QARR8A1g_hXNleb8aJPtAaOI5bF5y-_mW9KiKzezlInDlrmZWATt3MxPmvEFtj1b6LM575u2Zil6dXEU8AgEo7RRh6Vvp2lzeUccagjkQaX_tP1m73q56fLL9sfDVBCwjZtoH9zHuSuSWLqeESJDvIxaGUjES3916aEkJZzySf6TRYoVbMdo2RZUc3fx55N050wtGpdDOFCBIP7GleLRuipvAVGmRSgxK0htnvcmTDSuoHFxs4ZOsOdJd3laSOkc7hPOOWMHGDfSVMn0ir-N0euFW32HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردشکنی جالب پاریسی‌ها در تاریخ توپ طلا؛ نامزدهای نهایی کسب‌توپ‌طلای فصل گذشته فوتبال اعلام شدند و در اتفاقی جالب، پاری سن‌ ژرمن، فاتح لیگ قهرمانان با ده نامزد رکوردار شد. تا کنون هییچ باشگاهی در یک سال ده نامزد دراین‌مراسم نداشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/29377" target="_blank">📅 17:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29376">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHg3cQjnbwa9t8qWQEXAAv5S6uuuChatlWO-1YpFMmV0gEVqDRkpHQsEBE9J484WDwF8sn959G0K_nFXx-GlsdWj1zF7VC5YHWe6xDjOF8UPiyYIxihjXHFYR8lUx42ZVbPTkbG0zZMXt3Rpia78Dl5yJHMMX3fVz5eqxuTx6GnM2RqIzJH1SRZv9bxzxF8ZBvMfPp_6ZnfhYuDfSSTbfsDRMkfPyLYupbL7dMb8KmJ6iuqYvdNpxPNv1ejRXu81hyF_VYkoUWITlMyw6-rhruCJiKl-RaAQX9ETbiVxNL5UbfhzPH8uwmXz70_HK02XJrwCATN_wYMwGQEeUSUNNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/29376" target="_blank">📅 17:01 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29375">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jH9G88Q6QFQx62by5HAlzbzZ6f-V7nnW2X83jrPV0IC9Gy5IkKg1iwT3Jgj_hUq2ehx46YaVLJLM_Axmff6QHwfWp8RP6KXls9XFuCfpVoyjVM-ODjpWFoOQKUCvSgPyQKrYVDx2q72JOUlRFKEm7Q-Iylvjqgad4dUa8NYgq9A-IaK3nAWmeGcbtt3B-NayAxrWaI_qSj3ueSeup3Ap0mcD2Esam5kO26k6Aj5ythENkfUQLspZnZmuo1SKgtXZ-yUaXQyaJvz6ofIvZJxriK-rX8eORZF7TkVRa4xK0DIwvV43kvK2QMg3c0Y1qvLXw1cBL2TigS1OxD4K1qqkPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛همانطورکه‌پیش‌تر هم گفتیم؛ بانک شهر بزودی تغییرات‌مدیریتی‌درباشگاه پرسپولیس رو انجام خواهدداد. باگزینه‌های مدنظرخودبرای مدیریت باشگاه پرسپولیس درحال‌انجام‌مذاکرات‌هستند و بعد از به جمع بندی نهایی تغییرات رو انجام خواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29375" target="_blank">📅 16:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29374">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SotgEW-pUm-wf93PlyD5xb4Wn4RYDgkp8eqXNbTdu6A1_oKQVcc1iz9veb0KO4PywkmOawHKL57GEXjEmHCoW-tlG-BJjUiQ5GgLKo4zyLVV0czg8AI_UEAmD3crP3DFomydtAlwFBbClT-Zft8QFmfA8OHpL8tmNjeaLtN3NcSiEP8bo16GSnTnJ1KI5mppyKXeJA56BjN2it592HEzzrK0rQK5-4TgXD8BgCO-N8uefXkOovzTZ2FUyJdRrbhdzwDy8vfXEOXGXIMqbD2LEbjlkifCvjZPYn8xbVeEx0kOzXbCW_O0bFTeUleBQRe7rQmfrv74w2IFM4XS5MJ4og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ برخلاف صحبت‌های امشب پیروز قربانی سرمربی تیم آلومینیوم؛ باشگاه استقلال مبلغ رضایت نامه محمد خلیفه و بهرام گودرزی دو بازیکن جوان‌آلومینیوم روبه‌حساب این باشگاه واریز کرده و بااین‌دوبازیکن قرارداد پنج ساله امضا کرده‌اند و نیم فصل به جمع آبی پوشان…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29374" target="_blank">📅 16:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29373">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1N-WbMqJloSquF5SiUO4flBZSpOgCN5jg6V18610qJRNc4nka_bIVm8lienD2RO6a6gWIiVN_nwRahHtyEBD6H3qR6sv28bqan5Z3rLpbSCxWzUANDlu2-FcanWl0ksFMTfxaMOB0XdRuCQwlDHxlCWYiR6OO2WXQ6bD-KSNcCbKFneGjmOXGC1KTI9dnf7ozsd_ZD0Yz8yE0Zb8OTwQFimvmDT9e5KD3Q-VphIekTvZO_wJkDU1bvQ0ZAI075I8MwN1Z7LUFg0-zpFKrryeXMVDATtjo7IYUenVuaX2WjfqANN3KljEoxOG7lcqzhPYGzXUnuK0EekoxhC3FVKjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
خبرنگار معروف و محبوب شبکه DAZN ایتالیا که مسابقات جذاب سری‌آ پوشش میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/29373" target="_blank">📅 15:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29372">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALJQZybElMpwd5QFOEg_psp8e9MvnwAbyPTw2rWoAnvuAjwJPg_3Fc_UXuQ90O8PyjVdTsxJBD7dOQOV_Y0hQ7yjdfmG0fx3JTebdW02Oe2FLg6Qn6JWBdbQ--ksvHrg0r71ehcv-12ukD7Jz4jxYi_noivbE39M32XXx6hpr8xD0vKIko_Msb9G7gN4mn391YeAbzC1rwI5jnCxLlV9Vy8ZqMj_99_dTSgBhV-NpuVvQUBqbVRthlD7D_Y3tPicRocj3jsDSx2lRY1ZhFHrcyCKJDnRsZSoVhb8Vw9AG1L7hfJCInHL3V_ckkV0Tlgwy-sDDYLwy7nbR9Sx9m0-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
داورهای هفته هفتم لیگ برتر مشخص شدند؛
وحید کاطمی مسابقه استقلال
🆚
پیکان رو قضاوت خواهد کرد و بیژن‌حیدری‌ مسابقه روزیکشنبه دوتیم پرسپولیس
🆚
خیبر در خرم آباد سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29372" target="_blank">📅 15:32 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29371">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjWACcOCBoy6tneiI_Vi9vP9SkUumwAD97OA3eZiitZ9EYGDNH7OkFNHbjF08UYtUdPfYdmhhwxbky8W2soER_iC-V3vtihGH7oFyKAqlcoGCWM_W9oWu_gXAm6wr-Aza2bJFhqFsRoCCNTXbHa6EhcCsP63w62p3QQerA8HtIe59nhbI3DIlO8R3_2GNdNihyP1vgYH6COs6iODLMA2fN2hmObjSa7dmHByF8TaoSeIOqqDHLQs9yAssQRKxWKKymAl92rLgnAr5Y8scDUiQWCgV39_6Wkh7Ju_YcZCkVQcFD8Ycs9IRsEuSxPo28LrdAUaKpMnvnxpe1JH5Pb_Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29371" target="_blank">📅 15:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29370">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0vNJi7DZ0d8GgAN4uDrUKV_znoOgKUu0DrJI-am5ObVwJvV4pnhyc0CLIYrTIneSllTlw8sMuaWNZHkKpGOkXhvezIJZRNgXkLGLiZTmss2_SBj2AkbbwkW_sYTSzguKPgc-fiNT5AHK8Ucs_HcNttBzPQHJyNQPTffAlOROm-JiElHlxdpxnUN4_xS1bi_1M6RpCtUBAELQuIyoH3g-nOJnPJTstEqI2gskvtq9HtO22G0sWXe48fw9dIrLuOcvSvf1SznBQH8y5UTC24P6GbHymodDCMfC-KKi91acmL22yub3FLUpyamJfQP-0iPcgi1mxLBvcMLwcHdEXqdFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29370" target="_blank">📅 15:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29369">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTLWtUK_Z53O0bzBxv3b6WWudHO4Qs3BG1YBn4yhtCUo-1F-12IiM36KTS05j-b7YoddX_xALlnqr6yPz-obL621xNZ8EaYsIwnwB4BZn-ffbBfH-eQFiPiSa9ODhmQxf_yrlPii0S65ovlOAgbBCzme9mooljMq58m8wD52qGQmoGU9MwwYVhe84rpjTKJlZC_0Xq0p2i9Ejvf1qyKYFY6JUN5V-E44z7lH81ZFPOWHKevOs70cHuIweK8vMyzhEUuOm8goZdWOIFYzrTd9QYHzlDWGQKgC781yRqGZZaGUXuZ2SLKgPsQGl4RdG9PpTvMqwR8_a4brmXQup9lLdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29369" target="_blank">📅 14:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29368">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMAJwSgzyiQmvjFQ_cn2PnSLCnHYSm1E6xuRYCKFG-CeLzyxW8Etc8iXTPq2RSUWxAwzGr9l3Chgm_V2eEDkIL8NQhAk6kYkTZgta9peQ6HkAHSzCMNTIS-Ng20HyaI8vMLQxI3HpRdWpsZOJJPB-CzoGM6iSndphiEi76lQmiSshokwnbFqY-uYimAYOgWFVFQ9bsgkV8bgPkL5G2uMtZhrKv5KQBuyg1M_e7CUUWQ8dPMzgBBaoX_ggw5J5S7umkL1vqfgYIY-BdJ9oc-70_d_s5FDcrqytyLhYHuBhfijezk4ur7ef2QaTcPSooiy1AKYgEeTHN_ZzAuVpKcu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
لیونل مسی آرژانتینی ساعاتی قبل با خرید 100% سهام‌باشگاه‌الدنسه‌مالک این باشگاه اسپانیایی تو دسته‌دوم لالیگا شد. چقد لوگوشون‌شبیه بارسائه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29368" target="_blank">📅 14:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29367">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk_q0tU0I0Zl6J11qzMA5GjRBIfF_pRrUJa7uJDqBhBvOcyDqbaiUbrVCw1IxB0dYj_I1CyJZH_KAxNrLWKuX52Bb7L22wImX_g2C3cdQuxzyJcAFoE2uE8ilM5FvgLrOl2Ac-C1OkCz0B2ZPLnYhD6aMLAgjUnESn2LYRvXT3EHXAfMxcO3vTMn9wl0mIECB_rSYU-JnQEaNMJcjOhAQY0P92n7dbuW2ktyK9lVvBXEDywVi6ouqBL_LApDfPZteITubUW14Ju9GQ42Q7daHsQOLCgPZVdDrIkV2BLXgPabSZSd7mhEn428T_1ZmNIx4BfaCMFYormLx7ALZgW4xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29367" target="_blank">📅 14:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29366">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXxWcxnPv3YdyShoGve4G7dUo5KdCReZ3on9a4d2AiO84VAM6kcJh3gZnmj2oZcjL2J_Km2rQlw160gGQYgwEVZ7tyCXnRHyluArcfJ9OHiiK9Hlggvqu3BJaqz7NLKkXX4nM15XY-UVxqbPHuzmGtPzklVe1ozxAxpWn9TwnGlprc8Hu4ett7V_dlNhQEuGmQZIO0iBexKAgPUBXZlCNYty0vdQyNN2X5U-VlZq0hSkEKw4Vwd4asGZ95vjp6prNKXVcp-5cbfNzOX1wOzMXSzWhn044CzPZivnxNZphYgyZCbpdMQw-9HW8ENS12Qut_r6Akg7fCwdZX3_ASBxew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جام‌‌ملت‌‌های‌والیبال‌آسیا؛
تیم ملی والیبال ایران درسومین‌مسابقه خود درقهرمانی مردان آسیا 2026 بانتیجه‌سه‌بریک موفق به شکست چین شد. شاگردان پیاتزا بااین‌ پیروزی درجدول کلی‌مسابقات در جایگاه دوم قرار گرفتند و در مرحله یک چهارم نهایی رقابت ها به مصاف تیم ملی چین تایپه خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29366" target="_blank">📅 13:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29365">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765da8fbb9.mp4?token=mofjB3P5iJVz10L4Tc6a2snuVa_BdTXpvJCOKrS0l-FcX0WQ1N6L2IozHTRDvzZMVA2xC8CxAcMCidjmUscBRLZO1ed_VFAiIJczzjGsm6Uhz7bWS_-eBsM5bBiVEq4OTJDF_6UOWbN-iXm6G0GSHLCuK46Mlg9vauw8AyTXJ2CrlNkK9P-ahUSh1t2fk9mUDABqGyjJSvsqLi1hPVn1y9qbVIg10WdyUOxcbMvXfz-t5wmkVr_2-vi0ZjiKnRLAHr9Qc4we5j9i2Vx7oKrzw5gpg_OXokccSWs9KSH9w1wyE0XBkoChp_58sXpuFwxZLDGGpwPWdgBX9h3r6od0dLq2ibqPBS_MiF3AXnm7jYUmnS947s_6NNDXoIVNnB-y9xncVnzmYHqWDWfrYHh1aJDhKHi--71S5wCUL0HTeTs8h8jOcSWWbeVXNHZVVqZnn0LKhSVf9G40AcFURhww9diEx5abvNSDcBDQso08SgzCGnB5XJrImxQEsnoRqb-2vwX_zbNIfybgjOL7cKm3UySTRUcOpNxsyX7fkOktMGUq8rVzf3NKUYzR33EOB9iX68LYZXu1ZofP9awpO9QeVtMRuptGDHg_vBnYl8bsUxEvWcceFmQJ_uwUQgPIzpu3rv9J-RUhzYaPJOdZJCIrv5ypKz1iS9UAQZzgjBfu-1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
آنالیز جذاب و دیدنی دیدار هفته اخیر آرسنال و چلسی؛ میکل آرتتا به‌این شکل تونست ژابی رو ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29365" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29364">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3eaf66e2.mp4?token=iYvquS9p4WDE5chQK3gwSh13bmNNXq9t8_jLRcZ7FYm7elAtPt1N2hbfX3GGnAPYyQCKRMj4mbhxc5rLnyyrJSO7zI_GcrOnvEmEIIW9grxF0RigiZeY0BxervN7AyaF-UC80RoxXCC9Zx-9K_Fxob3jl2wpymf9SRfX75D0Xwy5EHtOFnO9meq1XFqHhJFOxWlrrBKm74cV6p_Wx89mVnYa-X56YDHFzfR9211IzkjOk6GYHdD7jjIEFwVWATcAjWh3SpYpKIo3o0u_H_dJQxOmFXWjw4PRXpmWsQKZQDVppJj7JEyU2SjABI8resOvJfHmPHPl46y3etlDfyQcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
فاصله‌امتیازات دوتیم استقلال و پرسپولیس در تمام ادوار لیگ‌برتر به‌کمترین حالت خود در تاریخ 25 ساله برگزاری این مسابقات رسیده است؛ تا پایان هفته‌ششم لیگ بیست‌‌ششم استقلال تنهابایک امتیاز پیشه. نکته مهم این که در محاسبه امتیازات، کسر امتیازهای انضباطی اعمال نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29364" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29363">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIPJKSv93f3kl9ngxy02FV0cRaVacZvOCEAw64Ct9b3Rbk1hrz66z3BmWveWgftqcchVVAJR43hDLoNTRMXjBNC7TyWh7gqLzMNiGn4-Fn8LY13SfAbQjyjVMaQJL59ygdABy_oas-3VKkYwGOkw4YWTBRs5bp0Yv4qPw1NyEzVCq87D4wBZWGomOGsvrvosmT6GkMrJfkg3_e3Fh5DeQGbI-J8YU4hZV26OOnQy1pj9clNzjp2Gd-DioebmzKiICq9fxnYBX8j6gHwWoFNZmA7fRCWfq6wm2U9Z-sNZow76zNKpAt4KQUOQS-wxdp5iMILVea3dtWrPN2xndAQn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
بارسلونا
🆚
فاینورد
🇳🇱
⏰
ساعت ۲۰:۱۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29363" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E45TW3jGUvLtZ1FNyHVjmYa6hGr3xiix_rX7wamE22JdwOajXe0mFViBW1w8wrE0RM9YNrG_jLvDgFUWbkAxjCWHwK2-Y6dh6M1k461Djn5o7PM2Igdy4eQwJol78rNY8CHlk7g_88-kJNTjSsvP9FZkI1KS92rFMpXti51Y3JPq54AAThhirpwlNElope64MsZCWXVw1vvXtazPGbceTc3a85cuUVNWxC7CyvsEr4GBvkMNO6eDhvD807pHjyDG363LXvSlkrkgeRUPq5x5Yem2pWDzOXFuYSblZNJLssEmmkZT2Fldf3seozCDnqRTJMlVt81l1pVrRsRLP7IVI54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1617cce66f.mp4?token=f4q4c4E1fRuYYFiX0ibs0cMi5JZa2zV9LQg4kY0xroZf1wnc_C8yro8ICNZHJVGguQ6iaTbJaoGpN56eV-1N_bWb6qiKnMS_L-seLO5EmuZb2f6Obo5xJInkJ_uqNZsPJyA6F4YVSMQ0e2CvmeowDimHIvMX8RjJ8lUU9pLL7U-DoVKMHMQ6L9Zo5jZy-MKQP_CWyX5aROF1kej2586XtPzGgS4FDkTcba484YAfCbGmP92IYtl2cqN9zl12DVxU4v-WqF8Ec83mUn3LDcEMsbe_MnxAdlZcN3LCh6wpVEoY9GtJ-YG6W4nQi9Xg1YnSVqUELml9lzugyb_qJMH8E45TW3jGUvLtZ1FNyHVjmYa6hGr3xiix_rX7wamE22JdwOajXe0mFViBW1w8wrE0RM9YNrG_jLvDgFUWbkAxjCWHwK2-Y6dh6M1k461Djn5o7PM2Igdy4eQwJol78rNY8CHlk7g_88-kJNTjSsvP9FZkI1KS92rFMpXti51Y3JPq54AAThhirpwlNElope64MsZCWXVw1vvXtazPGbceTc3a85cuUVNWxC7CyvsEr4GBvkMNO6eDhvD807pHjyDG363LXvSlkrkgeRUPq5x5Yem2pWDzOXFuYSblZNJLssEmmkZT2Fldf3seozCDnqRTJMlVt81l1pVrRsRLP7IVI54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
عملکرد 9 فوق ستاره‌ درفصل‌گذشته رقابت‌ها که در لیست 30 نفره کاندیدای توپ طلا قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29362" target="_blank">📅 13:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29361">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/732028b756.mp4?token=C0Lo1T7GLjlpwF-NyiZQhM7tQrQmgGPTm62hUGARSz6rL3Kcva_yje_ykDq_AyqEv-gi2WVpDgHe2v0UlgMhDOCS_alVaMKcZR-FQhoLKfUs6Et0EGQB-02DNE-6DEFAFhaXnzBcFbP--EI4u8pdubg9dVOENLo_Lq0dndkYl0rk3KuwMYtfrTimywbzdv3qsKRM2UGpWUQVBtwt3cHjRI2RtSN_yMW5hRRTMg79Ha8UBZYFGqmdNeACzqzmv8wtwBmUKPGCFw9QOZ-O7-lVA48sIznnXxz77iI7-jhjzLfndHnD2OcrAFMIm2pqIMz36aDnaiwkKqoITVfPYLo4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/29361" target="_blank">📅 12:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29360">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvVbIw8kJvBWITnX7L6wG-AQZaYl03_rk5UfAvYLWZ9HB6S5bfvl4rDGZ0rnBYkKKNoNN3tagx5bfSLNRZVGWg_6N1A1m6nJMVPkqMiqtP0_NbgJZiE7_Ff7-68Hk2dCKnq5FBbMP28i-hB4nHawvO7U2oDa81z2crAhHN4pytkjZH5GNb7uvsujfnqRKxrBVsYSedURd89KPLtVbCJG9yGnw2WfZSh9KSc3fOkx2TEhA757fViOwg18X9CdUgi4GCge3iNoMDeq8WRB-qfwSAx1MQ6FTdfKoNov19nDKiA24_BLGss50748n6o7MwuYipg8ETTXOenQ_r-nBT5a4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
برسی عملکرد خیره کننده رافینیا دیاز ستاره برزیلی بارسا درفصل‌گذشته‌رقابت‌ها که یکی از بزرگ ترین غایبان لیست نهایی 30 نفره کاندید های جایزه توپ طلا در سال 2026 به شمار می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/29360" target="_blank">📅 12:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29359">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx1qSiaNPzXwTeO1C7rGuNBVOHtCAkrNkJn3mLJPZr3Te0GugDYFJ6But5gYNAmeaUvywpDad_csUsb3WjhqHkjC4DW15AVlBLv8UIVWW36rlyMUwwHqPkrp_dUHNe7j2zam0mQ91E1vEe75mFFTgUokTa4r4tjXjqxNm7PvBE9ETyVgnZShBFUjBXvl4zcFF_jjO8Yi2m9luGrZrHqF_iYv8t9H8W47puwvb5s2bUJInQV3T9Zn064JPFPYKOj3XVid0PjQHf_uRBk1cR-BkMuh86ADr_S-cuWogVFZ6ahPhLO0rRHkj7N96mqg4UjeqTFhPFSVOOg-Z34ltMv1Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29359" target="_blank">📅 12:14 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29358">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWoTfodHNhnbjm_4q5ob42UOvXMQL6DobqmI9qTBcbhDC0dr_JXp5q790M5EcxDa5b9hXOJ6kRTChQ7u1Z7XL08LKQ6IfhFCQ9NAyZwkQeb4M_G8I3L07BwZHEkaLbyUkfMf3_Lq7QgnMUj0HshM2osBEuSPN-Qhu0REPUfMYyFBC7has_X-YKUYCVv05cIxDkWJDqoLKoXraoBgCjpM4JAFDujiRXiQB0qDPsiiWmlKUWiN1f6OVnisw3ODiLwt8mTrxGcdTLQ-cR0jASud6UMwgIZxDa9B9gcDB5L-x0DsJ1rC5z2_8VRrltsqJWXVN7yOep1Z8YAZ1HQNM1ZeSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29358" target="_blank">📅 11:40 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29357">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9lGTPngVfdEg2419ZdNyrwGH8ryZSViwFgaiNYYuaHjdANTgSNXtBJogNa83v5ngd-S3D5BTEZ4zL9haMuqNiKC4pXFvRf22KBhRNxuwvLdfCP3iuzOCs949ZY06ZGmbYk-wBqk_WULzLfVn1g8PnK7S27LXQ3acS0L-9k-lp62-ufA2Qe9796snFvsinsr0NicCR4Am6bXnOIeK6MDah2VvwnL5RGGMHA4ebfsjHH9fLmTeixu4Rq8o0uMGyvCwpebc3kgFV8Ez1Cvpt7d5jPg3lRHwpyP0BVc9mZdwmxPKud06VQcy28TiWXWNd6GW1B8ycNt2dLXdleeAc2Q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29357" target="_blank">📅 11:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29356">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k86kzhfm03Dc1RKOgQhic1Syv27LJWs71tqldftT_SAiCsoIoVPLyQk4mBILxbSexZMIOogYv_Kd5LCoyWj90fBjCnyMPDYCUyQG-wc2Ow67A2Alq7gVBe8F3vKGZ4gbkpEg0yI009Y_AZGNq6ySQwDpAZayAPirCk3yhicm_kfgyrvfpJuAJgEzfdwpcqJ1Z5CxvfNPyyXwQxC8F8s4DP6OndNWCLWU7etPLpc3nRN1M_yKfse1PdnnxUZWgWXQNsBoj_YzmCvE76JBpzofdtaOSJ67_zyvqgeTekksZfeZdo00swPN8l0erxdjc-3GjBgxZ4wmwS2SDdiZvxtnvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇨🇴
با اعلام‌ رومانو؛
خامس‌ رودریگز فوق ستاره 34 ساله تیم ملی کلمبیا در آستانه عقد قرار دادی یک ساله به ارزش 650 هزار دلار با باشگاه آولینو در لیگ یک ایتالیا قرارگرفته است. شرایط‌جنگی کشور باعث شد که خامس از حضور در لیگ ایران پیشمون شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29356" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29355">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeLOW1XoNCIFBDAzhbAs8jNtU91VDqkbXBGpwod0v2dJbrHQP5iVDV0z-VQXSVyNba5t0bBBIWnxqJIxLd55n7VYZWR9oLWe6zkFkNhX7y3tpVPVJAbsW_P6VG8pFPZTkFlkcJ7oGrWQQ395GQ1GtNwe77UF-hHqx7MkC1FnqwdYeHc0WcpdSe0oPdvWoM9EBHVZT044dXyOB7jEfqm5yJyqXjkV0UGZ-cMdyurzMd_26BMbzQiCtb6tlc4MyKVlZvRvNFbZrkP6k0I69R-K5RROyrIl3gbk7V88ROPwso1PDRnTJlZK2TREW8HIy3Vzcpg3_rMZMAinpsAJbPI_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوریا شهرآبادی مهاجم ۲۰ ساله پرسپولیس با دو گلی که این فصل به ثمر رساند به دومین گلزن جوان تاریخ این باشگاه با حداقل دو گل تبدیل شد. مهرداد اولادی با ۱۹ سال و ۶ ماه و یک روز، تنها بازیکنیه که پیش از ۲۰ سالگی به ۲ گل برای پرسپولیس رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29355" target="_blank">📅 10:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29354">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=RWCwm8Oupe_SR3tFPBy4g_OOKXRJUGSE9gs0VXfmQiU4uNPKK9VOF5x04UMwippMqvs-JARlcJthmC9KhNuCw-HZPYcgp6RzrkMN2uh4pXC4OsbJWrse-JACT5rrMkc5iBEvSAx5W-oucye1nI0T4I8uApIb_klOulWf0Wn6HMlRa9xlgCLpOPRcIKwG6mdqakTARGmjdzdj1tVQt6iqtceg1nh84GTZZBWIBFEnkeIiktDGpshdHjz6e0Xms-IVorHxPnmCQHTeAy-LqUdpPLdQIA4GJrnDqVoi907FRPM6rgML4JcLJUAzucviDj76FGKHufAFpT5rZzqpujzhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6f5a93d8.mp4?token=RWCwm8Oupe_SR3tFPBy4g_OOKXRJUGSE9gs0VXfmQiU4uNPKK9VOF5x04UMwippMqvs-JARlcJthmC9KhNuCw-HZPYcgp6RzrkMN2uh4pXC4OsbJWrse-JACT5rrMkc5iBEvSAx5W-oucye1nI0T4I8uApIb_klOulWf0Wn6HMlRa9xlgCLpOPRcIKwG6mdqakTARGmjdzdj1tVQt6iqtceg1nh84GTZZBWIBFEnkeIiktDGpshdHjz6e0Xms-IVorHxPnmCQHTeAy-LqUdpPLdQIA4GJrnDqVoi907FRPM6rgML4JcLJUAzucviDj76FGKHufAFpT5rZzqpujzhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمایت تمام قد خوزه مورینیو از فده والورده؛
جایزه‌بهترین‌بازیکن زمین باید به‌کورتوا میرسید فک کنم اهداکننده‌جایزه گل والورده رو دید و بقیه بازی رو خوابید با این حال فده هم خوب بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29354" target="_blank">📅 10:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29353">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHfYm6ntHuYuxjJF4pJf8zY4hKdbZ6mEu0BLjE1YPpVSMfyjvKO-xBS-rxvtes2IJ8VfrsVv9MkLXAB9vHg25ChsNWo7leTcRl2CkE2T8viXcq0ootCdkS6ADzO0EFFLjKRic0aVOTKkAAeRu7uS5I_cbsTwdm3f4wU-K104-gcPAqDBWnex9rAmlnoUW2Cb-_Z0r0zEG-gd6tZAtOU7xhs5jBGZ-G4PLzxSaYAkWHBY5gKgrLXP4YfujVy2qX0mYT31ch8A5rvzewcoXR17Lf4Bvmy113YmGQCN1Lb2_PlCN9k4SJ6dna8E37gQ5qzccNk4PqBH0Yyfryxaiw5YGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛بعداز درخشش ادامه‌دار نادر محمدی در لیگ‌یک‌روسیه و لینک‌کردن او به آرسنال توسط رسانه 433؛ این‌بار نشریه سان گفته میکل آرتتا اگه قهرمانی UCL رو میخواد باید نادر محمدی رو در ژانویه جذب کنه! قطعا درهر بازی 3 4 پاس گل ثبت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29353" target="_blank">📅 09:49 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29352">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDx9D_LaYd7FlUFCywL8qyo3iQ6FyrQFtBPl51cPTWIP0Z7cuHnTretyOIrpBIIL62e04XNn_3Ro9KKp5hV2aMuPcqIAFygUOZi9FLaV-ZDEUdKL4m8fUcaePaZHoRn-9z1A9zytSDHNkFIPfGwEDGANd95DXp0qSnh3ytn7FW8cVr5wDmLiMqt7bP1o_kpctSg_SKdlPNV12eezEJt-aC3d6HUFrOqLlLq5-_LLLNpFmVfyR5sD_J898UM23V8RQo03sxQV-MyOxVVl-xm7bz_yKXJ4TpSYyziCPLg1MpRIjhyhIIzAUKkMtJJ84CKoNyVI49iiaUASw_gGckm0Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
فرصت‌های‌برگ‌ریزونی‌که‌بازیکنان رئال مادرید در بازی امشب و بازی مقابل بتیس از دست دادند تا اولین شکست کهکشانی‌ها در لالیگا رقم بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29352" target="_blank">📅 09:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29351">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL9nhpDGb0YIouHLnN4AUelTQDGA0v8uQmOrjRJtwiFHL9Cg0BiuewON9RH6-ALhMwxVaHO_N7PAOwFaPPaTireO_oo7e1pDxW6hPvfPTwGo5mwqgGA6b1ktLQuBL0uKDOe-AIl286mWzxpAJ6lneXhaY4L9ta3Y8OWt0W6eSKa9sPRGLCLdx3WHW7HMUriwukTxXBqKPmQ0PCUomc0D8KCOQuKw0jxQxOGp3hlgNaAf_G_Wf7lQCTewIGVkous99_TWxefAUukNzmZnHxJFjUi_HKWaqlT8Ri9bThWcc6FJZfW7R8WkfNNJ7YYchK7wxm6vSX-Lu2yYa_XG64mNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تاکتیک‌ این‌روزهای کادر فنی اسپارتاک کوستروما درلیگ‌یک روسیه: نادر اوت پرتاب میکنه یکیتون بزنه توگل؛ نادر محمدی چهارمین پاس‌گل خود را با پرتاب اوت به ثبت رساند. چقدرم خوب میزنن تو گل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/29351" target="_blank">📅 02:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29349">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cHNzGNcittgksNOG2v4S8UawcMquwhHzD-IYgRKitoh53UIUOQlEO490YpS1MUQ4QMQRqZ40DnkhRQ0DR54zlX-1LswBNqkqKkTkBR4zdEZm8kBpkS92VYlRTJoBk_96dlQqPJmylG-sCU5zpevxv8MmDGtyDTquKBfCMEG7lNiYjoprrVf93qBmOfywtTwdtaIlnqGwrl27u84fRwdffXLQnLamj5u194MlrARLhWNkgrkAjXTy28jV3ihb_XteLAhN2vWnG4HV8wcQDVKFO1Mu-M5fnqJZPVouPh_MKeO57g1p3QNpcjXfTc2VkeW4Gc-lkTfMWIy0H5gDu8FJsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ ازجدال شاگردان فلیک با فاینورد تا تقابل لیورپول و اتلتیکو در چمپیونزلیگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29349" target="_blank">📅 01:20 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29348">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kO4bFwf8XbVPPyPubkcnYBScewmgULezo4VHcpkabdq4dspQdX6Lm5eXeUvaShj5JOBjbpUKOFau4N8m0rDz2UHHQKZ4daSuJOgqWLr8H_ZzXncFWLXI5TOeDQS4uhCDl3h7r9LJxaxC1VYHnBznMrk62EXnnm08Zq3wpnD6Uf3vbbRsd92vhQ7PxPedlNt9v4PerO8fUHeXu2dy23PLLCq8KDBhIPsuJuAhaJOBVK-jMauvBl3DZwQly_EM_yRN49Gbm7NUye0XC7FPAaiYH7sjtHqus9aBM51jDEMinXY6xYtsCdxVaVh_kqjYriyvSrZFswXnsvBrFrJo3wiEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
شروع سه امتیازی رئالی‌ها در UCL و برد آبی‌های منچستر در شب دبل هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29348" target="_blank">📅 01:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29347">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqgQ91h8I_JgFDe7TqbxEKkDpH1gJb78DCjlxYiVyaxm19QUKn_FC9_u2yl1lhAt0Pd4Pv9faPcDq4BQC5wQfCp4cWzYaCPDv3KlC71lfB8Nt52byjiEiWXFxnERzjed9s64Uc6_EpAZSmyJHP2uq-8aJVpt7lYZrKS1mqKcNyA2IZm29yVOwUU7LufuzrdUoAkjXmNXwDxpfEbCbwM5mEtkiIGEEJ0B2mqZAdWfSKAXCeDD3_ycsp9HlJ2OVleLViCB4rtbcy8d0D3UdRHqAjt_fLKma8jCyEKGSBuNUDKU2uXdlnaFJSlNS3GRlR6BCPbDb0t-rr0XGe4KZ6Rn7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29347" target="_blank">📅 01:04 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGzeL5f-TJEEMJzKtltmaD9SkyVkUt9FDDy0D5wkWu7L3rsWtOsYJohKW0arSgRRprxBBB7LIZPycpkxbThwQ_NOzCtqhjf3BWkQxHmjxTu_Kxg5ezsUchv02bvq9cQ_B9mt44HUh5npK9U7EUankeMFBJyXNeBf5Jb5HshR8xtLS29clarOsyQM4Jhy93ATMSh-FXPrFE38jH6OneHrGhSusjn0_oJoGZ404qDYgi4OkjIJ5MwlA6mEzeHksAuoU4o9aken8rlVKf__tY8wrkFw7LnQlmrWI_ec2B-y-f-Gt74dND5ru3CRY_Ir36Tb3_vF3leS55-zQT3iR6qx3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTsW2UtFtUgSTtL2a77Zh_qu94A7a4PnFNciBFKlk9b7FZj4_h9TaRLLlRKQk3tg3jpH9TxusGOrdqZG9zR9zvpFVfwNdCvPA_RpssHHocg7RQuGqWlSsZiIc0FriTl4GuCzsAhXVn24Aa5gysRazEgJ7YZUdiKZ8xbEFaJ0PYQSxN6VN9XOyVsbhDC2jMS-Q5fzXQW4iVNaey-6jdX311B0qMvWIdgOZ2bsQXSNsVn7PQbYKccN7EkW1vCwghSG7WgT3ATBxSwcwHuRogeJi4rV3kTIDmPLk6o7I900nNBtLsoWe20rSpHAUG6qvvPOR6K6d2wkCIy0pPQn7wfrOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جک‌‌گریلیش‌ ستاره‌ سابق منچسترسیتی و فعلی اورتون در کنار پارتنرش؛ اون اوایلی که تازه اومده بود سیتی بیس چاری مست میکرد فوتبالش رو به چوخ داد الان باز بهتر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29345" target="_blank">📅 01:00 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnJVx3sof3o9IbAY3YISfcPlVM-MllT1nnPKTZ3fTJIdZMG3M-P-ti-rIf81E420pyjoEmQC4PFrSWB7zvQJfx1z4paO4bwrRezRKDA99S4llmMIEWOFRuBi__cYeypqwZSsURWlv3p5kQSPSwSIHI01LqpV-oe8dCJ-Nnywa-1Hajb7PDkE4mAGcGfcdl_ympIqORRk9v-9BMsBgsBnaU9dazjcSEEAOBdtaUg5LgM4GWU5SmMskAiT8Obkr03ZvQku0mrwJWSqj0MJ6F5dmL2UKmhEmoV0D_FSjVT1XgnxLZoAYx9mGyP-qLurA_YcnzsKpZPN9uu_yIMPY5Ybeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
در هفته اول لیگ قهرمانان اروپا؛ رئال مادرید با درخشش کیلیان امباپه دو بر یک از سد اینترمیلان گذشت. جالبه بدونید مجری شبکه اینتر که در تصویر میبینید گفته بود امشب‌چهاربرصفر رئال رو میبریم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29344" target="_blank">📅 00:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_cWTmOTJ6ahs_SW1ZfIHUvCo7UjRpIvpi9llqB0KmbPtJsXzfzM7eUgqkNgUibsX6gzIFgCaAi86KXxzxi4lNzqLM_jMDVALac0aNtANVWjn0fsVZ78Mk93nbzPLw6ieHWU45DE7BT7yv3mbGR5Uar3a5_e_YRmcnbOyPaaguamLJiuDIHKO3iSfZtpQ370PgYY5MUjfLjuzio5k89fLCDAcDH8AbJAxInOAbrle8drE6CZneM24nTpMvx5jvuBBnEMieQdQYbZ55juj8aNLLIdmrxDBsEWrNX4XG3bMzH2ss816XjpXcYw8sHoeNan5eISxJjMDZMBLe1dN-iwfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
رکورد خاص‌امباپه باگلزنی به اینتر؛ کیلیان امباپه در اولین بازی چمپیونزلیگ در دقایق ابتدایی به اینتر گل زد تا با رسیدن به آمار رائول افسانه‌ای، پنجمین گلزن برتر تاریخ لیگ قهرمانان اروپا شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29343" target="_blank">📅 00:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-mKqzEd8CzwN2o02t2dJg5EWMTeQb9PMhOcTdyqr832Ak-i_-AZzZzDZa3YLt_hruyIE-du6G_1F3CZ53eqcPoTkwdOUa-Hr7CDE07D_ij2EMTdfVSWhpg-bidwuig-BOb3IYuDdx_xBsufiTYvPFuWZ7Pxv0Rbc7dPdpwmOGYuaLuupYVyaCWxLufwvtE4bT2NcAvnPq9NuAsfS6ZXos5n8ecv51vf6J1JioWlDE2rZ2CKWIuLaoMeIJBiJ5HZBIyM1LVmhlqnAOkxBVVV8gf7O8WqFiPpfRewMnX9fF-a88g3Xdz86u1OitOpObxBk22WeZqNg0SJ81Ki5vHe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Vnf20d_doamjt6252wwrAZrloTqnbo0SEK2ibCnpd22Z0vJporfgS-nKsxDqktI8ZTEtCyzCr-OnrfxVJG2Gw4uTo8AmmzFiEUNwQ7wSmk1bxcZeHVjJNWN6n07KR58ZpinBRdFn6_i2oKmZ3OaLUG2SzXRp5muBNx7l2S-OOfA8H_FbNVf30PdJBUDf-qavhMhNsS7t33y65ncNoJWVZ7AI0CTa_hOKmD9Ub9O4slXkASDtfQ4XtUMbSgv5VxtdtETIB8eCYG0E5GDjaQdezRwPvsrHY5nGl5XJHOioU5Sq0MZnv2hsk_xD0aWSkWxThFjAaQV_IxEbxQmd8yVHpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=Vnf20d_doamjt6252wwrAZrloTqnbo0SEK2ibCnpd22Z0vJporfgS-nKsxDqktI8ZTEtCyzCr-OnrfxVJG2Gw4uTo8AmmzFiEUNwQ7wSmk1bxcZeHVjJNWN6n07KR58ZpinBRdFn6_i2oKmZ3OaLUG2SzXRp5muBNx7l2S-OOfA8H_FbNVf30PdJBUDf-qavhMhNsS7t33y65ncNoJWVZ7AI0CTa_hOKmD9Ub9O4slXkASDtfQ4XtUMbSgv5VxtdtETIB8eCYG0E5GDjaQdezRwPvsrHY5nGl5XJHOioU5Sq0MZnv2hsk_xD0aWSkWxThFjAaQV_IxEbxQmd8yVHpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ok0-gF_7oYuaHvlKEa1YO4B8wFkLPFo6tO6bOMsOozjqgGjnjRog0r7hj753KIo1QFIukBxiq7i2Sy9T8iKtbZ5EqPlkS_2zENO6zRc-4eFip_cZmFxiSGBFVwMbfEiACZ-iBrslDrx2JOxxO6S56Fdk8xdH6mTgXaIm9tlfs3rx2EnQhraB8DmyKka8shNJUXB8GWzxgrUU4R3PnpNv7s3Nxw5_vR2VCzYXPaRJUtFd7qFlvzeh2gtpuR4B23XW8xJ7R694VNNlnpOZCwW2LI5izd-SPltk-70Rn9hjm4sNqH-Uzon1MiipYrJJN9hfuGg-bDlCMzYQT7e2y1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gJNi8eEkVObucZthWrojo8DQwd6NT8VKEMaL7j7MZGFXeVGUY22L3YHHx896e6wU2cpAdtmbqM6pBp08cVbd-vGSa_BfP9woQ4HzEFbe409A2-pbc7Ljd5jpPYHl5EILccPQJ573BYHM41hhYp8xA8qeFe5kvoNUOUECjidJR_p7D_6LRTciTiO5MgIfV0JygufeZl2Tfr6dnN1uRjBjxv0du7MpBlcL4jGEc5t_nN_N67709N1sIbuOXsmfCfTzTdrXHh-BF59J9mG3YoOWPJTejGJQSOs9qG1NBUkdr4q7cxOHK9Ar1L0elgbC2uPMdTrgQgzE29CzzWT84yej1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXD8_DTgfY6L4_KJC9LcNcrqmZN3q_d4GnefxBKY8X1gOsyp9fL86a7GWsEhn2CSGinvFMIbgsF--95a3pKsmMZ6CGkJHnbYIlph63WtjbDpMml24kjbjRM-cgEPnuLUvl_Wy_OathgGwlnb3UZpxNykq56LdJfaUfwgVIJ2ef9Qxlwzku6viKwJn9084v790cye_hEjLylOehsG4EgzTSx-38Kpn1vk0XyjX6JpbP3j1Xx4H8MiEQVbxKYA2G2CC16eie0XxMhSQkVlpws_cDA3ArPf212MgNYvB4fqAepV_fXrH2ZtDG73lNy-hOMf2zRE4cW513h2Op4Xvjmm2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=HHipnQUUZMS4L7PGkmMTz9W56kTRDay3SxKaKo88zoiqKHnbWFpgimm9gwlSPj8wKcjunFYCirmE_06W_k8cSbpZxiUm9Q1AlHjCPuyx7N8PhofV2_VgTD5_mxAWJOGi885EstoXxe-frliIwa1aJrL6-jyBMTBbFGxQ5gwnUsTzbyxP-2HHiTMC-wJlcI3Ou8xkozAaBmkd1Kr2L7NC9ShsQ-JgGP1JMCi08Hpa6khdHNJEKwFkds5cBaof_9ZVBq351HR54tEalmfAPnPEyu555ihLNLfr8oDAoPYCJ51Gy2ir3hrszBHDr8FfW7jLz4epzZpBOQ4IOn_vDGiWrTDDhs40R75Faq_R4yXJGiEUgGSfw0ysJEmZOnZ_jDXrTKvS7-TN3-u1ptDToqVTWCr8ZbLVsPf1CkbuZMx6ELgQZiWXEiNu8mwfwvz2UyxPxgJ313KBjWEwPwk9-HLNs6kag0XFN7o7rST_E3e9nPVlTBXJQws_lesIXA8gHjaVskEjWA8K_adZh0rXP4JjR-DwZ4AvmXZBcHde0YcyxD9oDcEij7PXoGZz-u_OQbRN-pGiW4emZHTD3fe2z8U-biTgnT5IMEcl9D9cDt3eys94EKXjOVET7WQnKutS5HzP03TalfdWBOV0SHADaJsNq5x9QtQ5Lex77jeGrSta2w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=HHipnQUUZMS4L7PGkmMTz9W56kTRDay3SxKaKo88zoiqKHnbWFpgimm9gwlSPj8wKcjunFYCirmE_06W_k8cSbpZxiUm9Q1AlHjCPuyx7N8PhofV2_VgTD5_mxAWJOGi885EstoXxe-frliIwa1aJrL6-jyBMTBbFGxQ5gwnUsTzbyxP-2HHiTMC-wJlcI3Ou8xkozAaBmkd1Kr2L7NC9ShsQ-JgGP1JMCi08Hpa6khdHNJEKwFkds5cBaof_9ZVBq351HR54tEalmfAPnPEyu555ihLNLfr8oDAoPYCJ51Gy2ir3hrszBHDr8FfW7jLz4epzZpBOQ4IOn_vDGiWrTDDhs40R75Faq_R4yXJGiEUgGSfw0ysJEmZOnZ_jDXrTKvS7-TN3-u1ptDToqVTWCr8ZbLVsPf1CkbuZMx6ELgQZiWXEiNu8mwfwvz2UyxPxgJ313KBjWEwPwk9-HLNs6kag0XFN7o7rST_E3e9nPVlTBXJQws_lesIXA8gHjaVskEjWA8K_adZh0rXP4JjR-DwZ4AvmXZBcHde0YcyxD9oDcEij7PXoGZz-u_OQbRN-pGiW4emZHTD3fe2z8U-biTgnT5IMEcl9D9cDt3eys94EKXjOVET7WQnKutS5HzP03TalfdWBOV0SHADaJsNq5x9QtQ5Lex77jeGrSta2w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuaBzf9dW5Ejo27XAKlvA_aGJ6t71SVW1hpCvhUIZmlXhLWudi9NZQIiSp6GObBuZ_LxUS7iRt9Au2XzTX7LdAbtV1s8IhwpIwdqJgGkl51hsKTpFd-pOPunJJyI4jZaYW0QDZS5okpsCqCTc7BwWzDUe49sv-GD6R9mNTRn3OnyMjWRyixqegdw9vnzLn9YR3jrkzlLpkQD5s3fvw0Vjb17zn_mwZi9Ko8TSXk2OYhmD-cz2Gyt0rAsOPtBwbQZKJXmXjukL6WzmNEyKnxexuf50JuqZ5kzeirzjCqLdST3uS5CDNqEepXVCrlMv5wbXNpMgp_KegCbKjd1c9FKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8s5aqVK9GgHbASZttL5RAtt9xfgX4rZ00T7LB2glDneH4G57oKZUBtBrlOtFtpy_CZNhXOLmCB6Ur0asx339iEEqZ2YZS1vJhx6PwUv_1TdbWgTHfOdUUBHWadxCo0dmxlFbbllN2N6LPNWf7fWidsJ-kKVmte62OaX3jHJy8jNiIFMmJX-zakUwk2cCztdAth7iZKNO7G6IlI-NjWclh-ECVHrcI2CliErZx0MlN_8ZgBrQvsBIRvrGO5STF6HYr-P7hfF8Q3uq5UdUNLrtCfXvUZHRj2OVTVaHhOVPrfEF8_Gg3XC9RObLfGaxXEB1w-q4TIeZM8_sizl8QVc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-8NvyPXBl9rQWSEdMvXGpIiEbXUbGHYisKNpJBfx0C50NCmY3817dKKeMFYxmD9qvBVueLwECYMhumFY-ssJKBDnRH-kvSQ7QVVeqmyTBFUd_d05w3DsfncFYDC2_LiEaPhxI4L4MZhmGTNDTM37Y-pLAlnxIJZ5ss7vo0oaF6pv29PQ8iKVrUfJIgkSz-jPxF-vdC8DKqQAtIVJcX45CJ6PLS9W4NEZEvFexvWxU6LOG0bYnrEDt0aUIPGHeAZy5ar-NEoKH-rhSM2Yjqmxz-zZ3Dyce5zET6MPjdxZp6z60VFjSwT_tjXu3ANPeB5sbYKWAWmeDVVizRlxl1Iuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSqTR59OTbQa9lHvVkIQCdZiyHxZb0et4euR0VPcZNBz0C9Dj-i5MSkz4CF0e89LmvB2jlyBuvr__QzdYLwBf8z9kYAc-nyuqZvUIQ-phuyL6w8nIcpdxcSA3OgumlhFgdfLiFwexvSrNm131EhscGcY_DSiKO2BEkvGGum5hHb677pmt3VJKhJHmXUqnxKDkhuWKJ-zfcPMs1rqLeOYSfM7FVtk7r_xNRCWxS8VjRSD0EprRdFXe34AmrKobXMCvKxWACdz9IR1ykRChATxrJ1nmYur5CinfcrIGL0vTdL70aobVyEqPc_-XoG90v2YqFGRlsma4UCBc43P7F3j-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTR7NLtPdqvx-PfDsm7F3HLUppcy77fw1XhfzkjXMxeumKDPrT0t3us3QqkoJuSf1HqB6ntwsC9RJwJV_9_BZl-faLYbcrSpTjvBJr1mx4jLLyuQvpVQhDcY6F2qQdcNzmdL8E6Y-mWioOo9532a_9BjqpgIFmPcQtnIdZPjfLbDx6hBL_X71dwpXIfQBOUnbgi0hYTfCxYey2bkm2Bpi2NB5XXRyt2hOvcKX47pqorMP3Rq2_qxe5e527bLdTlxxM5JDQH-OO9EOKcpWvFC9-xBS735-RNMac-G7uCFlKcrVMQ4hDTs7nNxJFNn_0E8LsZ56YOBKXDJJdinuMVj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=ZdAF3X9rSSXko4lxLW9RSae1ndPScRenjKLmKa8FpfKgd8DDK856uxEdHRfmPvndzrRJOoEqdqCe7xevyeq3fWr8ssu6YeqqTz1-ki3KlHF5ecIpjDYyDbdwdxnr1QJdKRK0S6UVqkvVai2XZDZlM4RTUKk39K-NWWiZFmmdD1qARp3h2g4QIOaIs9QlBRb9M6eRtEWAlIwWaZ660RyhGJFjmikME-v7HOA7e4ll0zTjd68d9vFdtIP423b6IJtkKBCS515c3Pqnn1dGewI-0xAZX2Bc-vMAWEVturFl1sMyXjJ2ZEtKNSrOymEY-J9W4RKbgrKPPu7D4bBW1SH_8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=ZdAF3X9rSSXko4lxLW9RSae1ndPScRenjKLmKa8FpfKgd8DDK856uxEdHRfmPvndzrRJOoEqdqCe7xevyeq3fWr8ssu6YeqqTz1-ki3KlHF5ecIpjDYyDbdwdxnr1QJdKRK0S6UVqkvVai2XZDZlM4RTUKk39K-NWWiZFmmdD1qARp3h2g4QIOaIs9QlBRb9M6eRtEWAlIwWaZ660RyhGJFjmikME-v7HOA7e4ll0zTjd68d9vFdtIP423b6IJtkKBCS515c3Pqnn1dGewI-0xAZX2Bc-vMAWEVturFl1sMyXjJ2ZEtKNSrOymEY-J9W4RKbgrKPPu7D4bBW1SH_8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WAoohilh7eMd7S10-118bk94bWSIl40WTAJp6YfSO6VnL3xhA18xHDkmcbib4gHoMx6M96_1fQdj2cuWiDJ0BFSteJPbWZSFA65fcGQlx_VBJ5mkdI8WtnJmE1yUX9TzGvupJXpIXlMbgqjyDfaqfEukxTBI136yiMaXQSuN9r73SMe4RzENZL9fBGsiiAdainOQCssLEt-o0ToBB3lPYQ1o6YWF9yUUgB2NuKAU4B42POQusAQDKJQnxjzoYZY2FqLZi77f83hf5Rrmx1T9-C_phtWrd1iXVr3C7N0GIGax14unmuHEScC-LyIrwaWxQZC564Wx66uUVzQUfC7Re3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WAoohilh7eMd7S10-118bk94bWSIl40WTAJp6YfSO6VnL3xhA18xHDkmcbib4gHoMx6M96_1fQdj2cuWiDJ0BFSteJPbWZSFA65fcGQlx_VBJ5mkdI8WtnJmE1yUX9TzGvupJXpIXlMbgqjyDfaqfEukxTBI136yiMaXQSuN9r73SMe4RzENZL9fBGsiiAdainOQCssLEt-o0ToBB3lPYQ1o6YWF9yUUgB2NuKAU4B42POQusAQDKJQnxjzoYZY2FqLZi77f83hf5Rrmx1T9-C_phtWrd1iXVr3C7N0GIGax14unmuHEScC-LyIrwaWxQZC564Wx66uUVzQUfC7Re3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFp-yOQdR9FEaHNRcEurohh1Nl1oiJxHO6VEv7E1EDNaKdNSlJFHbEt3bfuXg_GAcgPXn1m-FncHqz_gWipEhIyzuBzV1OuCatuxVEUW8nvWpWFZw81lx0_tMjANCoGo1GMQgeCmhfkeg3kpk4tGMRzL0MKlWzrVWBFrY2E3Wq2e9baUmwM2U7VqJMm6Rc_PPhqQDF1LVv01Lo4pjPC85qJqAKFA9PBPIvf6rj6g20imgkoFAQlkC-mw6EairyqIr3U-TsYQskk8OGd7p3cQaXhzy_0R37xJ3P1gUAmUhm3yGyGrfqsK9Yjpqro_uC_FXthdSiwN2iW3qd0fEnPk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgaKzbeXBx2TQffuUIzD9tXrRWZ5qs0QzVmW17EjjgVFWYPWKde1oMkjIxqw8LRhPjaYMNz5H24Oy_2pInbeTdgmPJ0TWCwhIm-TG2qhfsL8t5iaxVwbWshPEHdDA41GdSvQG9jx6wIBGFX6ECwF2Rd6mZ_rWf2kfDOY_rdhnhH5fbJDB8Y8tXgQ7be3Zk60eUTXFXbcs8pzXcNv-zv5jJMukPyZaLIxdP72K8Q3GIC9TQiPf8EvAEbiklkLuzsbozHpmXCJgwGsilFDV-mqiAoALlPdl0h1_R7ZIMWDtG_Cp7SJO0F5hWl79X61tlhEHARzUCD2fW8u6e1L_sZPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcHEif5tvxQ_j-z2Oygx3r6NgE9ERFoB3ouXOkvEk9SkVjwDpMzYesEe816uWvoDYpPAx_KHlLp7J3zjpV2i-_0l8BRnWSCqiOrcr9lCFYZLciK4Gx4j94WHMZeffbQisqenmrVw5llcJf5vCP0iWtnyg2HxLD6xtc8BmYmxgMzwLctihpSLPCA9HizFYWt096OoSFoDb2mdxI6GuwDlgK6mtUrSk28wFxiVRVWluRySuxwOk2FajK14JIB59Wp1GJFebOghK_dvazfKp7aMqqcZkP4bvBXwU0KGZ8K777-9hr6g6xxHiNyvMP8DIb-gQkPgTtyN-WZA9iIcGpwPVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYJrjVgbONyr0iMnop2gDIVbe7ZkzWH9NpiPLj8DoPABqmo1MnQC6ug0s1rJWteJP2EJSpdcLcRtI_lAnOXcB0lDvMvCIGk65NUJPaAqfqFcnabtL11_LQAnF9unSqGxwOdwq60qStEtzbxpFefed1cNq0i8RLhkM2t34955wuGrydk1oYZhomu_D2I7rQorZibg154HK6Lab3G8tlftkHz1cCT5hL8HHLvM7t2gRoOhXL3X8cHQcPxbdfYvs8zN3Q0P8s_nesJXfafolHTXvC713p5k4v_LEbmV7JepZETxwlHEHY8XJGlhQjbPHOXUJM9YX6FhZDFsVCCjWXD21A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hqUtZ_QxprfUvDBUdvctgmrrF0gWAAJwON145ySVT41u9B4styxnvQYZxJ4ihiBGPVkQKbx1hqLeCMwYJUYAciI8HFNyN-uLFkYXOE58dfvLTWe-J3WgZQP4SfXFC2V9L6639-fdVWeugebH9opxs5Ru59wpfvpwcPWXC1QVm9B8E2MxTkawbZlpDlByLDqlfSdSWlpw8evnOEuuBZD0-szbqIFy5OtQOPN2QIputDHCzP-imCefR1TSDU-CdcpbSqvZPV6xGVCAW09i3wIvxle07s40BRtTLGGcnJa3EzPl8y0EW49f55mA-TMCS8z3zrTm9JkTl3qQ0Q3yJhzm_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hqUtZ_QxprfUvDBUdvctgmrrF0gWAAJwON145ySVT41u9B4styxnvQYZxJ4ihiBGPVkQKbx1hqLeCMwYJUYAciI8HFNyN-uLFkYXOE58dfvLTWe-J3WgZQP4SfXFC2V9L6639-fdVWeugebH9opxs5Ru59wpfvpwcPWXC1QVm9B8E2MxTkawbZlpDlByLDqlfSdSWlpw8evnOEuuBZD0-szbqIFy5OtQOPN2QIputDHCzP-imCefR1TSDU-CdcpbSqvZPV6xGVCAW09i3wIvxle07s40BRtTLGGcnJa3EzPl8y0EW49f55mA-TMCS8z3zrTm9JkTl3qQ0Q3yJhzm_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYrweJOR_syPdZgz9TirS3x6jOgtXgMMv-bXi2SgesHrkMhBGMNFQh_fGLr8g-uIAKYY7SjSiYCk80w0xxDg_Geb1b1Ya8jQWG3PPgbTKKMMZrcoMRCO_UG1YMz7_gspJsbPBfb2mgOkIZ_jblq4nFQxg4kvnR5mutSkjKu0vBEh_UgTXsqkO_jBQf9GHzGd9jOkNuYugGI-RibzEt8u8kqENNayV85hamyyV23qV1I4dzfmJCArYYaT0L1d18_NH13xIWs5iYsBBUW3BgUaLyzONSTptOS5CX9wsa21sB_sHdHSapOOIHTol4j6Jz-9H6kZ54H_RI1TXdGD61ndhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdirSVlxiao-rXWpn_DkJw-QtBIlb9ccgkUxDmaHcjS9ncV89vdV41Q_vj6qIOEBtDzSdx-9TVU7cZbMnW0OuZ1qsWQsrKechT1ps9jej8ZAo8rLK4HYd1Nv5sDcFigpH9vM5GwzDC52iNB3sF31peOfIQ07PA5MeqWnM-_2AV3zP0N5TjfibbEtJBt7VNFIUhb8edYg5pNzb08tMhcxoCXuI8ciCssY-ZHtospXl4tS7n5iQjpbxbPbZBBx8TvZGgy98QMw2Wo9Xnv-5nEnwtGiZE1mAEtsB7VNVtWC_pdRr2Jx4a8T41YNZLCGc5Kc1i-Xk_OT85HuYaa3fca9tRVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=GA63JsFfhZXRMRm89ILGQqNRyG2HTYjh4YxH54985oLAYsRZbiaFXmooUqn5GTb2mc-TsBknAJK0jNFndteLd3wbvfaUxPcmVag9eLVEsKVG_HsUGRCybc8mfKMXu7Ztc56WHxsVIsZlLqYkJ1UvGTkv5gVnoVHBgdLPA7mBNsl0hd4_vog38IgFYwzStSqR_ZdNcrIbP9X8S3v3P5SV6-vt4paFq4yB6B0cUd2QCdtZFrsXb9DhdH41H-gBpFwYEAZ-xBaUVjoqsG53P0tRVY_B1JEpfOM8i_sH_KoIQdJBz_K-CRDax9SPKy0yVZzpJbWNgXutMgIJmHOyllfzdirSVlxiao-rXWpn_DkJw-QtBIlb9ccgkUxDmaHcjS9ncV89vdV41Q_vj6qIOEBtDzSdx-9TVU7cZbMnW0OuZ1qsWQsrKechT1ps9jej8ZAo8rLK4HYd1Nv5sDcFigpH9vM5GwzDC52iNB3sF31peOfIQ07PA5MeqWnM-_2AV3zP0N5TjfibbEtJBt7VNFIUhb8edYg5pNzb08tMhcxoCXuI8ciCssY-ZHtospXl4tS7n5iQjpbxbPbZBBx8TvZGgy98QMw2Wo9Xnv-5nEnwtGiZE1mAEtsB7VNVtWC_pdRr2Jx4a8T41YNZLCGc5Kc1i-Xk_OT85HuYaa3fca9tRVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtjjuBobx6sbgjj2QH1yJuvTZMlcKLr-UfVxbDF8f9LKB_ph8m9IvxjWb1DWIXNdX5bFa0cRdVgq2Ad7zRKdllkkCjEMmG2smkMzqjuAyz4QYxEKRDjlJzth1EFTW8peZjro8KS4zspDg6PnrncB-QRLnBeCqEw8Du33ht-Wk2pCTk7oc7mCmA1FdFxZiV-yHgPjzbxD4HPY3MDc3-XLuy7o99abuQTM67zPNawHZR11R75qoYIDFOprslH9NUjv5c_gsEC1t_EHp3nfEYBEejtkAUMTLyS2iXzKDA6EKKHXUR3D2mUbEq1krZtTyGXpLTDqE0aMjU_fTro2KjsqJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tB-rBAnvmgBsZUx5le65h3w6RTQB0ggV7qZgfWPplfa59j-17-eSiz1ib3Nrpf1RiF28rhqU4J1Yfzx6uhUuZJVVU5eczrNalEJFvpC6gwdoz-1_VqdElXlHYAtr1GPJfNEok9ZQh8Lvoo1u6nfpzjjgTMWZ8PXh2fr8MsT5iBsJu4SoubYU2hnrTktJ3dV4mDI63axh4yeFkToiwJBFcdcsmBlRcPi1tIv0CXo_o0gCOCcF1eLwr-DTUcjW1lHSLXtN-sqoHiS9rNTtsf7fwRlelCBMJrPzylV_fQct7F36k4mb6nN0gLqSyIXfvctfuyYq-q09jX4J3XhRtqQE6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=f1J6eGkid_7jI7Z_VubuQjoUksnvIk99bYoQzYywZQwd44RlPXLnmPg0GYlx4dlGde-Rg6VoWwGANyS71E5ij08kYH4hky79-Hf5WVVjbBFcxZTey_JEe_oSU-ezS0Vs03XmzXRdyaldi8pOEqKD21imDN42JviQLSS5O8XyaEdnAyMT3A2wgKS6oDqLstWkbdSkN2mB3RM0AW4haLIDrngyjp1e49T_c61V4FWgCS-OWliqVeWX1FcbEa1hLfwmfUqDuKyhadEDWdr77QE06uf1xp6Eg30iNkDFesblA95uv_cqgg2BPj8Lxi0muu9cJXsvIWT0uc8-XsdPYDlHbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=f1J6eGkid_7jI7Z_VubuQjoUksnvIk99bYoQzYywZQwd44RlPXLnmPg0GYlx4dlGde-Rg6VoWwGANyS71E5ij08kYH4hky79-Hf5WVVjbBFcxZTey_JEe_oSU-ezS0Vs03XmzXRdyaldi8pOEqKD21imDN42JviQLSS5O8XyaEdnAyMT3A2wgKS6oDqLstWkbdSkN2mB3RM0AW4haLIDrngyjp1e49T_c61V4FWgCS-OWliqVeWX1FcbEa1hLfwmfUqDuKyhadEDWdr77QE06uf1xp6Eg30iNkDFesblA95uv_cqgg2BPj8Lxi0muu9cJXsvIWT0uc8-XsdPYDlHbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=Q_bpy_wqjdZhykFl08Ypij4iAcy-iRB4920wZcsUcO4a3_oS29V09WE2JlhCJodQ4cSfPjOVNaOQuYZvjD3HeEaXEM6JTA3NqYZAoPdBREfe2nx01CkJ7_MdyTZz-SgoCegbzG99Xw6SusCX523skCZ9zKwhDBaUBTgqhGqE9PbDWq_xsGGH3zH4eF3_Vs4UcIjLgwl9bnIwQe3LOxH1NvIu5FFDeoPJ-qcgnsm3seyBSuIi9UG7fQYXkW70Kb9tJVHZEUU1a9ve5XcugWnDQPdSKQNP6o9dsUY-glM9qYUkqTjF7UAUEIzy6knwZyHkLXxISLv5E7ct6wseKY3Ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=Q_bpy_wqjdZhykFl08Ypij4iAcy-iRB4920wZcsUcO4a3_oS29V09WE2JlhCJodQ4cSfPjOVNaOQuYZvjD3HeEaXEM6JTA3NqYZAoPdBREfe2nx01CkJ7_MdyTZz-SgoCegbzG99Xw6SusCX523skCZ9zKwhDBaUBTgqhGqE9PbDWq_xsGGH3zH4eF3_Vs4UcIjLgwl9bnIwQe3LOxH1NvIu5FFDeoPJ-qcgnsm3seyBSuIi9UG7fQYXkW70Kb9tJVHZEUU1a9ve5XcugWnDQPdSKQNP6o9dsUY-glM9qYUkqTjF7UAUEIzy6knwZyHkLXxISLv5E7ct6wseKY3Ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiClUJ7JOkY0uvlIUmQ5Un12-b-Ur0LxIPRtnw_qSgnRl7q0CbfHeuCFgTmQTGZJHCEoITpfgXS7Lm9pRG37nbW4NbGmtjEgRIRhKDTwYE3k3OA7HKDoIOgTcZtY8L7S1Cr-TwqvGToTxFZu3HR8G9tFznbRRljP0ZFyEkhO16mAlTMUp501yW0GpTGYLc-xhAaL_0D_bLra903-1B3su4ZBeRbBVlMcPyWDvhpEWBiEsm73wgeECTeDnm6pmkyBcXsApHFYEDHRjYBslIJ5DPAbYfysjWcJxbh5oZn2TT34GVMBZsDGdmoApcH3TUeie9h15ATnHWEvFiwfzZamsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3yR30dYZuM8sKKYXI58Mpx6u8tJkk1BOPILSeZhlQIdtbWp3UaKGJvJcWxWPYRJ4k_mNNOXpQMWbcIfyYvwAlase9mz1rYtpfg2TE-P01RTmU_HaEXy2vCo7VQZ2mzvf-IkiedJzGqgLSt7aYtP-Ojb4Jl1-3gOvOL5MKrLefaIhyx-8mpJZbJTFG8NugjZ6Uwe9cieN5NEc3eTs8obXDBSRwJRHxxoZDlcNfRnVxdeB7alFVwsm_W3ag-kXG3aY0fak9iPe1RrFc-WF7m_65Q9BJvcDmPlE_vtRnn3lVp7w_keCNHXZefPMh7QdLbwv0cd727vE2i5r3RRcpgiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPUDen_aPnJhBDITYH2439mz5RLMFxxj_FzLlrrcPAoFEcq4R3rBl4aJfvDsaRFDQHPHaV20YNlmrLyJwl2ZpAZ0ghq0i-NpfAIATTIwEk5HGPaD9TAwQ4O2cVEWDP6qo0S4NrhsgtuUQU1ZyAg4oaTTLQnLHzP6j5b1EBKthJjtz9ddwah7NDmJxInHU_Ld2YzntagKIZt4dTZEOqlO7XmPnElB077HrZnG1Z_lpimYrE5f0DjhymCCfyEut_JE4q4ZIF-y8zXBr-cYZ4IPfLNk8yMCDmWOXvb-oQb_md0S8H6TCgnF9sGavvBYwmPCzozkTNiiy52DcKU1Mh9_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx-ZieirrPr7QBon2kYvVCOjk-stGnrk-wWEirxHdI0LJHqKJAhbjPwq2X5qiwXRfwfX7jHRKKrKPN-leOnguSwdMFuJk5dyF5GMkuWYokfQys044XsdgvDvA-K0PVdsHFMZ_28r8AL8N9E8-oTislwvMOWEICfB7L8c8oHPWRgZrf9gc1hFTIQ0XSF5ZjgmMReRbG64fVh9mtYI0GJav87yfLKsmyJdYIBiYVUZm9vifTgVGCfNFR5cjHcJDlwTeNG_Ng6bndPjkM1orGXvouSyiSHcy2u2fKlQVzhqmsinvj_e7-o4LjnLQRWVweY9Depd2RoYupLyx9rwDp9bmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZWVpUJzugUytmw1nnepCp7hnDnAV3fNch-WM7fPUen0WDvt8u3yDkRQmGlfEz5fgBnNHuPztHjNLaVmua6ZKzvyBDJe4JYxP0wFyvYAKpJOxLVnOJZJBPWgNSSasUrwyVsOa83_ewVPsePx3zEXX3MyFyERpXxhv5lU_zf9mJmjrd74TRX_enuI4-3GfT61Ll1MPSZxz9IQd3FI_ouLwfE05ixXOx9wxgFZTtKcs6muz2FkzJHVNpmOt2NC4jlB0675NNMcOw0B1A2rsRyBWaP45Yct_dAwnFx3YdI7eprC4oER_rFDlRkvXkm2_M76Sxik0qSVvpmgWlIeTn-PDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZkzbzVVrqaAVezMxP37D4Mqb8pLX6Ukz5SXjYCOSZppuMZGpCfjo3UmMv1ejSN923Vb0VomnJ9pbGTxkjHIlEC-FvgV42Z31rrBdLICg3BXg3zlbwMOTcaRkHr54tKAw1b6qzYGnDlUfi5Y8quKzdtteSj9nDyMzSY1v03R79xbeIG-TFDsjtiXkLYelJe0RNpdPXP5sgRmz-o-oPMUEK8015R9LoDiEx49RTxoBaHZAj3HiGhKuuGkuSz_Xc5D09kyNbECIAfgEnUdAmKFMTLubtjcE9LF-emDChv1uBucxddAXaWmJuiJR4g7Bn47arhflxKbtaT0n3KgENr-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=P1sdj1YaY_JQBBqel81uWKfzY_Q5LkKgctFeXreqaHgNTijPkpSgjx4b9Mw7HoCwtDwhjXhANUyOpfv96EfzONJCUVYOsSh1fuV6rYk4HWe4cUWfKD-W0QgK1yLBWNgyLO7MNUBGwpm1galJ72o7eEhW4XbJEVuU9G9Rn-HT_xNPFEsUfr_be-CembxwulTTy52gV6ojTsTipxLUbZxoGoBOLUn6mKjsRjX6b-NGrrcC1HhXN7x6UZCGGt7piRJVX5f6LYIp0XEc6DaAy6pCQvvYhC4JKCluiK1Co8M7ryWAyYU8i6OwvnzwG0CV0anKURi00sZYN_7wq_eKEdXoZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=P1sdj1YaY_JQBBqel81uWKfzY_Q5LkKgctFeXreqaHgNTijPkpSgjx4b9Mw7HoCwtDwhjXhANUyOpfv96EfzONJCUVYOsSh1fuV6rYk4HWe4cUWfKD-W0QgK1yLBWNgyLO7MNUBGwpm1galJ72o7eEhW4XbJEVuU9G9Rn-HT_xNPFEsUfr_be-CembxwulTTy52gV6ojTsTipxLUbZxoGoBOLUn6mKjsRjX6b-NGrrcC1HhXN7x6UZCGGt7piRJVX5f6LYIp0XEc6DaAy6pCQvvYhC4JKCluiK1Co8M7ryWAyYU8i6OwvnzwG0CV0anKURi00sZYN_7wq_eKEdXoZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
