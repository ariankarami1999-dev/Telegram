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
<img src="https://cdn4.telesco.pe/file/ssDHd6s_djXWaajl1LAI4_MlYBwQRQj0VEKv7ISYDGdPUG6qgk9Lgai81jzGsn_Pb1R9Y5V1l9dcjbxKBOVkHd5XNfBA2vDtGD-hlYylTk42MVg529VS-JocyhaLU9j_0EHoIrYF1FIwJwuZC0JEKAeKI6G6UZ0zHGsK5532HrenFI8lvDgjR1sX8nYuRjvRjQU7BnpP5YY6uzNFcqY0oldsiJm1uSQp2X4ZGnCp3-nk7EVeHpRMkleqKvbr6p2S1xFTthq0X7pUeBQmNy5fnzlUpn2Ez5_ak_9SBPQLAndK0AcDOVYRD1p9XpIjLtwcvP-Yaz2uITSF4YrFftZlYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 246K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-23391">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2397e7f715.mp4?token=YHE-4ra-deD6mSHEJxqv5K6nvBfShQGgSSOdlkDg9gyoXSePTMZDQDnTzGPw77SPhvFcTMon8EnkNwdXsTLAe7tuyMFqKw7HD0cUp0J7u5wBIFrFi5OjnLg0NCyvciCcsnLSC4v-yr_Lk4BZD__HddTGkvdyCI7aFCvvCW2mO38TSqu2rG227CaYp4wVk0u8wwPit5nYtnrQHYYJFtdT14X7ymMqQaVsmHENdacmSUQ6o5mvQfJlGXOrj9Fir4EZVKRnMiicx6bxi7L4pj3aPf9UDf9iNuz2gYUeqVO7geZM7zL24R-hderOwzmiX5lJ0YvRxKhFUD_srKEIanGZ4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/23391" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23390">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roTi8GiT3mIWhCH2chGWiH9T8AHioj8nWKbYmy1TPybaxW-CdySNcDjw0gZa5-3JhEI7AdRgN6FuKnK2Ugjev3d4felVTrpATIH3XWrB2B6f6begyl7-6LN4ijxa9N2zETG8MxWliUerVgrzvixOFHMtMs5v7yjXirVo7Y0e3CtKVWS_ksZQfDCoF_HHHPWUwtbT8n_KrT9FWDUNzTLvm9HaJ39QwGjqA7CnzYiX23L3r48GmwgsZTRwc-c-3780XeKQdOUfpjPtJWewlgrtBp-mOFgEN87td-IRR4VogvWA3lwewQPjDt1pFJvY-IyOpO26ph4nuwguoRoOiQyraw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
فابریتزیو رومانو:روبرتومانچینی سرمربی السد گزینه اصلی سرمربیگری‌آتزوری است و منتظر تأیید برنامه‌هایش از سوی فدراسیون فوتبال ایتالیاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/persiana_Soccer/23390" target="_blank">📅 23:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23389">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BAq3bdhOu_B4_gAzUeYqZdMUpH3zlZMNNCVocODozLxSf0OR7ruGRS4GDq9Bi9YW5BpMiXT9QF9UWIcSl_9-3ma8LDPHqJnQsNpirr4lXgutkOHrbnmc6MDWrT6Xqh4fKQukc0G24imh2OVsBeErxRIwvAnDhtyb1Gg7_YzFA3PEYk9zmsd6l07j-opTdFeiAgT05SESVZoQYmaIbFRWI9u8JGprwYdGxLdn86XVoFc0AnlC9H52oFqeekFd0PekWum_6gnkxH8yesBK-cQU2lDnA2YVZ7B3fZGw9y0RZG2-VUwlE00lcHykRid_nTpZY5IzzZ-DjPf8zVbCDRApdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لیگ‌نخبگان|پیروزی ارزشمند و شیرین شاگردان روبرتو مانچینی مقابل شباب الاهلی با طعم کامبک تاریخی؛نماینده‌امارات‌تا دقیقه 75 دو بر صفر از حریفش جلو بود اما یاران مانچینی در واپسین دقایق بازی کامبک برگ ریزونی زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/23389" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIv_81HjvkvbA3otrm04MZ7C6DcgVqGeyHtw2UuLWvuH_Ra3N9erpOCq49cmrNla3m0Pj-yeC73RdpttK8QKoPIzwlrBpbzn8O01VLRTsFyI4y-tzxc5F-aM3eK9qqbQb3gLSTDq_tNlZuSuKYnf0BDKB2ehGBbW1rtOaRvQ8uPvyVHi9sGnl_StseyFgvNwd-Vo6i46VkANCvyzr2FO-JLxIQEOTPqJrxgVmThaRq_b_mDJ-WiiNbY5FprJKw-HhnK6XTmUc7wOKEcrXfvsqgXDoSAwPbku8AP2VaTk-0s5aPiJl2UKns-jFkSZhpGMKbf5i1diT3lKU96Gx7E-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا #فوری؛سران کایسری اسپور درتماس‌بامدیربرنامه سید مجید حسینی اعلام اند قصد دارند این‌بازیکن رو در تابستان بفروشن. رقم تعیین شده برای فروش او 500 هزار دلار میباشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/23388" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/721a3bbe01.mp4?token=qk9i7kP49dnXsYqcfwY3xTcXpFiHfXCUUyK65B7TA2FWc68KihL_J_Fzvv5Q9olZjHWX7PqWbA21z9ZLsQc9ykKd7GUcvk14JOC2S7WI1TqvIxxZ3pDVZXI0cnk4N5qzYQDdG08dmY9nMlB3GJVkiV1RX_-Qvn7YuLQ7UV-MGhURS1H30QcdJaEUtyjFUXOB0vJIeF-k98CWoqZnMHtCV4zsTXEzOobtIeOKX_4kWUnju07VdETDtPywDQTen5iPT9LuCtrpOspEN8a7vjd-gkLjSUy3JKpEHhsv1VSZs8IdQODPjrhVA1N_umlkzLZrYkAL2sJWXq16zkeGXBtnzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
ابوطالب حسینی تو برنامه امشبش به این شکل جواب محمد حسین مثیاقی رو داد: برو بمیر بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23387" target="_blank">📅 22:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3cqZLqwoD5rZjS3PVu1UF5h36KP1NK4szkIcNBhUJAX6W6Ld8p7tEGWjv9lQ-K5Id42T4ZIsuUnsLGPUPuAPS9BruYLis27yRZPNkjb6hN76XjwOqa6SJc6fbmZs--vx_j1zTetzGICXZuQYtQNMIsx6SrtDClMLe74c8bBTrClUpX99rR9Z02cZjXRwaLANHRuo2-AS-TSBbnPzZkkNSIXzBbnRn2EO0c1FlJG60ninj82JY9O0thlZheqxgk1D6aFOHKgWNpX8TuWfJxPUcaoV4UCHO5E3Vd34-ZAByK2_6wQkGssF2OkVMuLvjgjZazq2BiIfjW57jCbSivLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‏کل رقابت‌های جام جهانی ۲۰۲۲: ۴ کارت قرمز
‼️
تنها مسابقه افتتاحیه ۲۰۲۶: ۳ کارت قرمز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23386" target="_blank">📅 21:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9c572c731.mp4?token=kdfDD41hKy93_I7Bz80I6zG8F3UohJVP2VwTrEbiCzfx8bL0J_YO07r31h0lhF8TqraCF3To8G5BIfCY9u7sG6owOg4x93DXmd8dxVeXPVXaDQnffyCR4HpQbG3PwnN6rhc4hRNafgLrC5wxlSkOQG3G_HnN92CVO6UAZqjf_Z7GXLbELZo8kJ_dPaukNFbpZGtM3ziIbKHZW4vpJpTN7bYe0YPr86xDeB2FwCe_cE-u5kT-Y4qaib4raF-jBWykvDgPiapBAw9cES9in0ahkjT0rk5IllxSaCb0WuBE3E-BHvsqzIBx6WZXXhS0p6lT25Aq3ddz-dC-zabByfKlvIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
شبکه فوق العاده MagentaTV شبکه اصلی و رسمی پخش‌کننده کامل جام‌جهانی ۲۰۲۶ در آلمان که با گرافیک‌‌های تاکتیکی مثل هیت‌ مپ، آمار بازیکنان، موقعیت‌ ها و لایه‌ های داده روی تصویر زنده، دقیقاً شبیه‌بازی‌های ویدیویی این بازی‌هارو پخش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23385" target="_blank">📅 21:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23383">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQXHo0Pe3EhCWzrVsJHe4tYdFLB4UYciiO4hvLctPfBejaIOzqI5Hsmq4wCxAE77mkeA7pIFztQzNCcKXbXVu87mGeIR1Myt9eSZC_Ew806WO3SXsLAWfAZyN4gnDaCr1YC383hvSamc28_QvHY5nGU3plJl0wP-kzWjWsvC444pg6G2zPbyGNrQNN-08MkXvJdyvwMFvySbAYCgmaaCxf3k2Sx80tSJyQtFoS_zFQfEWpWyyBnlj-e0HTW2oHZU5-BUITjX0-RQ6erZIBD8hFWHW1G-HAhae4apweaMU0vWVNu7sVI1zWb03n0wkwvaskV3jOQvCEwDDs6l5uYbbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجید جلالی که یه‌زمانی‌میگفت امیر قلعه نویی از ژوزه مورینیو بهتره اومده رو آنتن زنده میگه تازه بدبختیهای فوتبال ما بعداز جام جهانی شروع میشه. مثل سال 2011 و قبل از اومدن کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23383" target="_blank">📅 21:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23382">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX97SgTpD34vqIb5nCn5w-QP5OQ4QwLet71K2PhzbldMkFICS_q8owtivc7CIFrADXZfXh0fWrFoi1DjprCsVHebKjLFPG9WVukwDJGaPekPE7YdQaQ9CefIw5spjK7yFdl1-JhLKLdB2EQ6WE0LbqKdTYLpktaCLNP3TPZjy04I-nLuTp6Tz4bRoJbyImQ9ZDDPDEHQkCQyc2wKNruRO07vjYD38Dx_sBKyYatjs9BXa0E1xFkJ2E809ltKlaLl6-Y-NDGlG9u58HaaULkJTqAMXCb06FFTCKz_5hi4g2HS9HxMRq7N61t9SEGW54wMfzx7pXvLOXjS6m42pIgJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
دیمارتزیو: اگه بردلی بارکولا قراردادش رو با پاری سن ژرمن تمدید نکنه اونوقت سران PSG دنبال جذب فران تورس ستاره اسپانیایی بارسا میروند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/23382" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23381">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c77121522.mp4?token=VlU0FkusqrCs7NB65lqNyxlNIJ3Nv00h0FZFYpzNZ_XE2DW2ArYjRbqpsFM0Gt9nwApae8fP1PYc7wm205cmAfZdHmxyaodAaaSHOfuZ0kIkp_XXf7gT2U7bbHdP8Mn6DiPjMo2wI-e0BNyt2uOhDivr-t9L2eOpkh7swydLYh_qMqCUSJGld0tObjv3GthnwyaMlCt6-CyVD5K6JtYo_T9s_OquX0kASfojC-4aIEjCI3ImI-HXNDGaaNurIzojuTbWkUdwnMhCwkNQ3dq0dXSFS2NGq_y2kF21VAvsXOvfk-pwEXWxZUPyGMKMvP-HeINmcOWM82vmf-h5m9ifRIohNVVAyGK_Zt8CK3oIzULfxNI7VVWVyNpmkBFVV1xRaYM17JSe7ODOxzmqIabVwoKk869Ng9sjEP1KOM8029DmBtyL0fqZZsc5-528fJS1wpp3krYSnMrK30Ypdn-hNP_GthwL1JYVmZAqpWoQZiSvz6E7wbzOGRYG4NxztZQ-u6e3UY6cV1BwtRF5ZSBJhQFw03wnP-dKiycHxse9m3TwQiEOzq6bqQLrBJFJYTM-EnVW2_P2UADDcS40KamC06D-YdxdtlZ2gsoCtyotjs09VmQTzNsucvAjWuUGBlCblS1cu5pmsU0MBCbXBTUxFZDPF9RNABsIjZI4lOOzAk0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نوستالژی
؛ بدرقه‌تیم‌ملی به جام جهانی آرژانتین درسال 1978 قبل‌از انقلاب هر کشوریو بگردی از اون موقع انواع و اقسام پیشرفت رو داشته بجز کشور ما که گذشتمون از وضعیت الان‌مون‌به‌مراتب بهتر بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/23381" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23380">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiKgf0nbQpPIzz7m7TnO_zfhYiMCEmtNco9LWV10EK5bA99xmpC5rkTIib_pevGbhPPaFCZ0Y65taVSI0HUD23h_ophaZpj2qJ9_F1-hHSn5ATpJhCbIWXp5HqBtyJJyrf8xwl9FuKxjbDyeIkDDFe3dVfPQlKsgOlmAHaPwqT4sRWNwLr39Bi-DnDuAOoRWg0lUdvy8NvCvekaisS1EoUe4F1VHpl4zXe8qBTbknPmQfjyZWp2RDUBXABS7UFLoEuqpcGmDqhZXGmmS_n1_OXH-WUMnzsrzXfPU-LT-mVKULfl7jHXKt_c-lPkLt2dRLqNaiQcJNa0jEUcVMQnpWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵ میلیارد تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود :
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/23380" target="_blank">📅 21:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23378">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n9Ch3YjKdLM382XOzgWN5341kypVoBIGwrzHT0MOOu0DRPjdXxWd9LeQ1a5xQPBP7zEkYOp-tTIQnIBWTgR7O9T1ExMuq6NATRclgw44L3mP8szNzEAaZP5cLaz8WFO5c5mFx4fSwCswX5-VckYQXeBVickHir2WqQ8TKC9qhDtbpDF-hJjQ2Tf9AiU098JHj5A0jgQLqKSzm7AjUWaa6MXmxejJGHl1s6K23oCQ6_4bzrQWGRXzbx_3GgPV9992FT91rkBoaeXBtV3TnO5RqAv93fDFbM6eIl61AuPGOGKTke-ETyIONALS7tVQKFVouFHm2LUdSRViEhbRWvwoeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NUtfMzQN8hzCDafmceMnFYiOuOomtSBIBGh5865G8AL4dfI0r1LpA7xTjbEB1XuhQ5DwG-L0mVsDv-swRDM2KsanJmNzy-u8aHO_u3DjUt712u116ovuoOYCkEY7L7MRzXKP2pD9iODN3SDt7Y82dgQQB3TzqEtUXGPiMPbnRRuU7G80CnrUjMMIrUTuAjdjyL7gMMjJPP13lTvoWL2YCwcGVEjCJ_ea2srA4fBkdThfPF4ZErYW6NvXG8RF9NdkliB7Y2flaW-RIZEdr6GtudXxhSnubjfMBqCamek5vHuH65DfIMuVbzPFXWS-qAHIxn3Gs4szoPl9FlTX7-hPdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026؛ شماتیک ترکیب دو تیم ملی قطر
🆚
سوئیس؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/23378" target="_blank">📅 21:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23377">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7731c5d007.mp4?token=mrnYkWm2fZFDqF2MbvKTcFsg6qJX3Akvxw5znWNvI9eZhHMU2WU9eYp0OnlC6t48oJZoPs_bl9aAMDfpwGQWWTKkAq06svR1c6VqFFy66Vp7vXJLV8SMa8oQsEpZOjVQYzgdGKcZThswjBILZdDfPcgr-x1avUTpJ-6dFI-P4XJ6zZa-8fVeIV4xE20noiEoayL-FEsUZSTrbjMPbnRbbcOkZwdelXliIKpmxwFFCbJJX0IngarfYf-3JTAYcBbvubH0cNIcX0daNusqYQ3ld1M7D0Th2srAK9U1vmV6nuZM2Hl1AK0KHeGl76wIU-WAp0xmbFIEzv5pT7TNrW4_Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌ شنیدنی‌ و با حال جواد نکونام از پنالتی تاریخی و چیپ گلمحمدی مدافع سابق تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/23377" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23375">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41d438c27.mp4?token=Hvv52A-jjEw3BTKG-gKinmS39DVyqiGINDqm8_c0mX-zK_n5sFJ68Ogs6gkbGGjJnR5MMeO9SFs9ndLB8N38aNoNQLeLcwHaXbV_tVIdkhFIPTELuMW2AsKH8L-4emxUrUC2XYMrZu-xN5udiHm-FD-M4HtZgyjkxO35oMZUtUtqdaUI9I_IBCvg8CI4UJIGi6oyCwVAj86jHyEDB-BB6hJvgEWougrtVfb5Z83VIRRJsHJmOTOYAq3-ZaIVgywYoKeV1pURW23hPzZWGL4pjiG_Tt4MjEFV8ExkUP7_pKELR7t_2P5VyeRrUDI1LDhdeG0NUF53kNiqU8u68ihhPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇶🇦
هوادار تیم قطر آماده دیدار حساس امشب این تیم مقابل سوییس درهفته‌اول جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/23375" target="_blank">📅 20:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23374">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1639bc56.mp4?token=jdYGr4xU_2oBYc0m2QI6fOdTOg7-5F8UrvAmsrFsd_uUzrXcm30h4ENX1cr7BZ9n1z9-X2aaHfN1ELAOglNj_x6sRub7AMd1UB6BHlWAQ8-3rn3MgcP7NJZfi8N5YmlIPge0RZKhglh9hwFezhJfC_pRY7Uu9RQoM9vQYMFGJ0pGng4VUXj5d6MgeRvlJlZDoc4Umlz3aIRpufb3rrQcd6wMa6XBve0Vd7YiPDvzcyelqVs0jyCGdPCwk0dH-mp8Jsf8qGArTgCGHqWLZ_k7imkv8dOrwnrIyj5kU8bBCRw9SlnPOiyiPeJn2mFw9NdDnxor51lPK4A5NLNw1rPj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
مهمونای قسمت اول برنامه های جام جهانی
🔴
امیرحسین قیاسی: رامبد جوان
🔴
سایت ورزش سه: خیابانی و خداداد
🔴
عادل‌فردوسی‌پور: نکونام و کاوه رضایی و دیبالا
🔴
ابوطالب‌حسینی: علی‌پروین مادرقحبه برو دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23374" target="_blank">📅 20:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23373">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa708e81c1.mp4?token=oH04QkpUIccJn9f2Y3TitqTj-apYVz7TavjZIMWF4RbFXfRM-tyqRoC2bakj874t8FJEiLTsbTgBgpIRPI1X21yBFf8JUkV3sDEqgJ7Y6Ls4d_J9M8SYr5wTsb55Q5BkpDBlCWho-E_K3dBHcdFfeje-_WyjJfT3EA03G9ciJQLTFpv04w8tJ9pSTtFXz7fWXjoOg2lauHl5LK1NNZKkdSulTjrhlnT6tict9w5Hrk8XvpWLvKYleMK_C5GTiSNPbyAUMTrgmPwNzC2A611k7yykUlSzh31Vdla_H_0eFNjXq7tcPvfaX4npBFsg1iYS3WnQhg6TiFnYqygtw0aAfQNFMcPoqihMkoEZWlNxd4IuQa_UgRAGVwquSAVZo2TtrvO1Kr-3HIDMxr2ZR9CXVvwSFsJGwqMgURy_-lSUiJJfskZ4f13lm1sKSVy9AKqKqCotAkGP7Gs5kmG9moC_Bu_uFFaxlxfTQxxgaJbRnROoHRKgeT17q-OfDcP_KG0R5VPgtYoIlsI8E3hwf2RrAmuJUjfC12yzy7tnRyq8Unajl8nI3YiZ_Txzk3lZDMxogKID7fwNHfMsP6IsR-mzo7yQXo28xAtsbCDcfirnsioZYqRQpqMfndGpIWp0VlAEkg_0aWxsG1aH58bZD7OMX9qeXF3WHfyh06rf-H_Iz6Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
صحبت‌های عادل‌ فردوسی‌ پور درباره یک اتفاق جذاب و متفاوت برای‌عاشقان به فوتبال و موسیقی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/23373" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23371">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5hhD01Pi-gKDQyZ62ixROmhr-BG4zdqcP__phb7GaqutQwTqNLp1dYPVKE2mDcGGVbaNSk-u5moNvAfihUxloxSR-XMzSLxBztwsQLkcxpv0DUnVOyb9aVUkgu-tbVXtgDHTRm9O9c63l9f1IIBS3zpcWm3YiZ0HKgTXCXWzamDewIvSV3WaaSGnqooT5AOeU6v3EVYHgy7Y6JB2jGDcBZ56930WOIu8ISto1uIh5x8_bhpPh4koKUJXSjrpeyoN_C4f5r0OZs1e3TSks-gcOkkBcOQxuJiKhRaT3enF3z-fBzMMszn3oLY_HjAG-yKJPR_zFxfYuCjwqpy9o1ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nc46dKayW0M5hUXUliR3FjMeYHO8FSmANx0mF8u17ekzD82Lslv_ymGn-40kmI0pzQukA2PRUEEvbLIwNYXR15uWl9Ave1N-DLoaq8HNT1W2sslP2S_zLB7GzLje4J4ZFcz_lMwu665aa4VSG1oir0S_YllaxHzoiptKt-0C0qj0F0JSUy5A9P2ec9ys5U1KZ94g6oU6ZEd8l9x7sGUgLytYvAurrAcsMXPVobHTMm8o5oYIekU8ccJnd7UcAFWc2zBqI9a8kPXcclWgTtu6kMKwwwVhvAQvAgeM3ZIRP-pmXtw4kvYb6ReZJ20ptoG_HLQzEIyJVZhABFQE5Uje2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/23371" target="_blank">📅 19:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23370">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0PQRikBRZJkBx21kW6fCQDff0s7Vyv_Tf4Umyq6lneVEPZW64cxXZKQPxkYhckisU4JBX3t9pV1Eslm9wogajdV7XaXh72eDBH9JHroXWj4Mj4kCYlFyDozOUOIw2R9KApITFvaNYI1S4ehMNK75V_9erirGcl8Ls4GmxknFiWn0lx-3oxjkRDR5ntRE-iBFUB3am5vWW-38hw0sX4OOmY5W11993OdJd2xL4gUs5J8Q4GZPEhaMF-gluQcqxpW_NHr5x1MyJtT-iy6GfWz1uDw0dRHSDYFAp1jHAwOEqSdIr3A0I3SYktMAbS5C4jdFCL2T7Lbr287GIb1_0fUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/23370" target="_blank">📅 19:08 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23369">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOW9tOIu_rBNmzYwKA-D5z92iKeGTbJSSmltlBvQfZEIwG2SZXbo4_qy8usvA7cInQZzJyipq9_w1tJaoXAg3rsa9UsH5VzPa4qowXMgFi7LQRyktQ-lWhIl5NTkPSSVQCTkVC1SMEKe7_u_OiN8OjrRr1siYu2CJSr1kshphikn_hSeeY3bhhl_6ay7Jj2aEl13DRtN3U8BfDB4Ri40SGI0r3K1zdaI4-dlT3fLOFFh5XUiPziSENB9KIVjEcQgxoDP1GkMThZwU6TSTIyHdZWxHHEAKFJAr99SKq8eDYGNd_v0CUR0UVwoYu4IHRt-Wei9YY-Cpgy-K0CoNrHuyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23369" target="_blank">📅 18:54 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23367">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdfIzUD_yhq3ZMGlHzQjlmy7qX84YiwwrLzTm3Mdw2knlPi3U7t1a1s3F6oO5duSkMpg560Ld4oHiz41ucleiTUZAyojfYApprKr5QGAI1l-6AGTe29WVcK_AO0lxl47fppCwqYYa-Ypfxg66MvN-E5-ixcyPp-ayywXEB4dEGfSpdqeqgyyuAN6hGHFko_du8pghpXAVVHC6eh-x4QIMaWD0w7wWi7OP4xzkioEpcp0nM3zCrLeQW2skF0PO8qZcfP1T-jNYsQMvgRXr-lv-K75-MCYJ53q5n8EXPHCQIKBTEnlrc9q9AffNtwCjARq13MkYkgdnIJ_K3Ljp7_CWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iTd-Ipbieyrs3Gygr66kDeeV1DwGgQVDPw7Vnj-QtssB9kI_eExyAGLY8fHGGAcH2OfZh8lVFU6WhRHq5JtqLMjhhxHghLa5L5AOewwvuzgmB05iiypp3RfjNjYb64bvUIroAqxlWf8x93FWxJ8sY74MX-_8i3pQC4Ysz70xNiT7p7R3CJ3bejwZVSFWaqdZaZ-V9aRcOrK4TKuZnatLDKh709sQzkqV0wICKkF4ZUEgqpSG5IKVfq6Ctx_N9KMDkdhbNjYujdKmhhj2hyEmjDHcjEvNjULsAioa1T_ViEkfSJFvNjDzywtkJk3yHSMv4SnMSXN6bzA2HYBH4IFJ8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23367" target="_blank">📅 18:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23366">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrC_R-Hyq26EnHqyOPXl2dWtQlpNVOuyD--wiLEiTq71teY9CDLKD-QXYbJYOaint235rgPMukZNzcbC94T8Yat6a6yrLKxL9zEeoRN7vvXsyGuQMFD305-QbiBHIpu_bRiJpoAeuCQe3XM2xUlMZJEGPOoR1iFixOxkhFwYwwkXczm8NULBeFoWxtppbikeGx4lWv7huqMP_PMRlMNG9GD0oBwBYTTixo3-5VwMiyChITux5FzGnNosLdOOvJeDpnFmC_tT6jghfQOopgv5JK1BJC4UHITEqS8xurM57g_PYZCrE5O4nmjdF2UsJaMuU_LQNJG97UzadA8N4CYazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23366" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23365">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=v9t8tKfIbgoHOqLt0hSWWTY2Xd8GKEYalhFxglgljQaP73DXs1z-Ouettaon092vMZ2ufof7mESpS8_R5LbT4AI3gZaaWXxdbTo-tBLbqMsi3tT6DEtjAl8sCt2mSD3iCwMKYxs-K-lnBLPShkBkQeYVDxrMCU6PDnjNXUhyttKQj23UptwcLkYwBnhsl4DSUS_DLP1N32zUVP5N9MLzxnbtNSp1FMbdPWbYo4Fa1NyKFGY50O2MTTZNJT14g04HFYyD7mwB_RE2uMpnrWRNiDb6W1UEx-O9-4ueGNAgl4y178jI957okA-mHmlrahZicXmaPJFnjLFK4Z_5-gzdBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bcdb77cf.mp4?token=v9t8tKfIbgoHOqLt0hSWWTY2Xd8GKEYalhFxglgljQaP73DXs1z-Ouettaon092vMZ2ufof7mESpS8_R5LbT4AI3gZaaWXxdbTo-tBLbqMsi3tT6DEtjAl8sCt2mSD3iCwMKYxs-K-lnBLPShkBkQeYVDxrMCU6PDnjNXUhyttKQj23UptwcLkYwBnhsl4DSUS_DLP1N32zUVP5N9MLzxnbtNSp1FMbdPWbYo4Fa1NyKFGY50O2MTTZNJT14g04HFYyD7mwB_RE2uMpnrWRNiDb6W1UEx-O9-4ueGNAgl4y178jI957okA-mHmlrahZicXmaPJFnjLFK4Z_5-gzdBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
کره‌‌امسال‌بجای‌کیم لی‌هاش زیادن؛ البته ۲ تا کیم هنوز دارن. لامصب ۲ تالی هافبکش‌شبیه هم هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23365" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23364">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله طلاسی | پلتفرم خرید و فروش آنلاین طلا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFM2ezaaEjRl9kR-VnCSMFSkI7u_uxiV6M41aaMoCdaqWU4-jcp8A04RzKDD_dToYv2ZQzp4uTXWtzA6ILaF1BdXgXMFOF8eqD98VSaVL_Bo5gLxZjMOtxNwgDrQFOFKFMZwwj3dymVQED1pid4bqtiwveDLZ5jnpFt7GWJdrlFpeccdBi4Da4fgR1JYjRlMtWC19MGnH2plp5EqKaaCvKVLhlzwtQhY71so_4l1kPp3RrEXwxYnz3_opQmennLXkMs2zDnkO4C9VShfhJgXdt2OC2xYdHUwJi5dgQsvWoG9zToZQUigpMhAfbu5xB01lG9Cx-Fk2uXRQHqHwoBKzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط یک پیش‌بینی تا رسیدن به جوایزی که همه چشمشون دنبالشه...
🚗
پژو ۲۰۷
📱
آیفون ۱۷
🎮
پلی‌استیشن ۵
این فقط تماشای جام جهانی نیست؛ این شانس توئه که از هیجان مسابقه‌ها، جایزه واقعی ببری.
⚽
پیش‌بینی کن.
⭐
امتیاز جمع کن.
🏆
برای جوایز طلایی رقابت کن.
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel
🔗
https://talasea.ir/sh/kel</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/persiana_Soccer/23364" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23363">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8WJGM_qQLG0ZpqGHTOF4DruZtgUT0V2SMYERdulOrEVHcxiZQDrUcYLKHURpPJnB_4WaCu3kDdduFGcvDU56K4N1zWO-54BrBzplmRdnUeAxGVkPgjyEDnjVXARxAt7h7Ci4klwCi1EzKGM7QqIuqyIU40TobvMY4USysgr0CGY5kmX-yWZdAVN_yf3qGtnQ3u5i2N-SW-Bw_JyDfxENXw0ndT4lH5em1Yys--nPUfX2uBb7h9sGx2aJKHRCViZkDg6SLfCtZVTjPb0J-3pBlW32OJzknd3WI8vtbDDhUSCJqNKFa8w6xCB5SG7Ez6f-LcsdGzRPxYloqupAiilAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/23363" target="_blank">📅 17:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23361">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObcLwAgIxaM_ltiVkRX7bPplsen5rj2W_yrL25pWjp-S14vTaXqVeWq6UGDrOtdlEX-eoeOpcOLmThAisRz7vRtGKNZhvQmdwVZBLocklJPkt7xoYe3FuGgmmdAhij0b7YyjQAX-DmkpxuoGquaMA1OssJ9sNZUnvQ2RdXU94orG1xEJZcgugm969y4bi2Z0u9DyLb-cnTuxXmDkjux5vPUdt8iSOZ9tx6QIq3aU1Ju6acyY7xIbeS9qrq5Vg0JhhOS_DJfPD0DpU6j_3rHwUJ6aaRTe0-JsgrdSMd5b2oD9zjgAdk017en9oHrGnM2ZTezsqKmiiYvYR351_D4PBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
👤
علی رضا فغانی اسطوره داوری فوتبال ایران به عنوان‌ داور دیدارحساس‌دوتیم‌ فرانسه
🆚
سنگال انتخاب شد. این دیدار رور سه شنبه برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/23361" target="_blank">📅 17:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23360">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IO4We_L4ZPYaYcF4-jR-w0QQo9SPfW_FaKUXwdymXFPPfnVuI4nsu8edrM9zsh1EdvqJgJ9mvTYmmVQcRiJSf2M94WbUgiXmYIb1fBRX7Gv7w3wI8fTsvTYfBbawVpJMYFqLfb4KX-jcamULhcCmJO_3YUsLFwW0J18IAcQEvAdYGzQdzqMUWsbVoHQYGsDX71SkZx5koVvMpzvaT-vrcVZ0ilpETTtSnDwmm0ERbD9I6LvbJcVHrSaTlC-8c98MUVfrh7s8xiDCQ20iQ-5Xsx6plX_7Y2YrhCn24Ls9D8TsigrGS706SbFQTAlraVGGrxRTyedFG2aYH5flWUHLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛طبق‌پیگیری‌های‌پرشیانا؛ رقمی که استقلال برای‌عقدقرارداد چهار ساله با کسری طاهری مهاجم 19 ساله روبین‌کازان پیشنهاد داده. فصل اول 55 میلیارد تومانه و در فصول بعد سالانه 35 درصد این مبلغ افزایش پیدا میکنه. رقم پرسپولیسی ها یه مقدار کمتر از این رقم باشگاه…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/23360" target="_blank">📅 16:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23358">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o_B1_Qdq-7pcSu43Q9i9mu6X-rRQOx4LkrC8NCxjIDmsyZRUzv-q81B6J-MIrr_CI04TzSi7dvNfqfaN-455iFwGlGHsb701ObyRPI4EOd8B0nL5QYiYxxMW3i3IUXhxMg0cXMTGbjmAH7BaYQQSY6lWJ7CtyO7_tpwiXQC6tx1tEnVgtl1S6u9OSmScaB-JutknkjaXmT74VmKVjTWLhNd7RcSR7YNIGPEaYef_5WJY_9kV1EdfuClTdQzOyDR1YbpFXjSE9ZM1KMki92orNC9oVIE21DHQN3oQOF3ombZE5kHlddchjuyhvjnhoxYEY6bkQKO3kklDsBWWRmUYog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WobKySs5564p0N6vwzBOT-dC4tSlzI9DQkgn_sbAyw_1GIyaYw6ulhBXDQoCZzOlAfZ5xq1kJdHPP3PnE3dDwTTxejtZTgIgw-lM4V7vvHjKi17LsXXBjkDe4d9BYLhwS7V3DnUCwzw1_qMZzfLxQTav5-UU_k99iUh3Mewvae3F4N9ICKg9SoZTOCLYezKK5uLTwyv-lgyfJv4QpJX9T05nGg4X5gcZpaQW-WAv6UdaxF4YyI6pCQBABVl-jEetZg1jkkeWIVw7k3vwjKshtLzubyxm13xfgBgWiDKObbQxH9BYO_waF6oLMEfioMmrewHzUl-Y_riyDQOn9xHW5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دوست دختر پسر 15 ساله کریس رونالدو: من رابطه‌ ام با کریستیانو جونیور عالی است و شایعاتی که منتشر شده کذب محض است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23358" target="_blank">📅 16:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23357">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRfDWALqvLCmuVK7hlVJRHTVZ9MKXnpepi0xrIRKl044iB2rUuyjAsRa9woPrYAfTmTSHSm9LgJ3y3L3ynlerFkADveff2LNSJh9k9mVxzCeeFrhbr9VZ7wK8qzI7Sy9pQk9KT3K-9kMh0cnBFP2ryZdEO4BK1KQ3-9U7RhLujItvTOQdfOPOhbyCZomrldDPNV_fe3S-LsTtxU9-FfU4fKdGkHxXZFe0asdNhXB3jZ8LN0ZpphCqOVheDxW8aAgGZErp1atJpqPrqBioujsEwRk4uNPcD5drSoJqC03vIJ90UrUKB8RAZhBNQr5wg8VAw29uRmUkiP6R4uvQ10BRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
#تکمیلی؛قرارداد یحیی‌گلمحمدی با دهوک دو ساله توافق شده که سالانه 60 میلیارد تومان دستمزد سر مربی سابق پرسپولیس در این تیم عراقی خواهد بود. دهوک بزودی از سرمربی خود رونمایی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/23357" target="_blank">📅 15:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23356">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKsFFG_XZw0SocvmcsV32r7Hi_wBEKKRu9VbADV1RXJRX8mwhg9zHHlm2Q7mmklUfPKtzTheRaeEWKwJhi9guJr4396iXcYdEZcNhi_X_sMelitxSBOPU-OoBUfJAvo3Jr0nFHtqhMnbR1KGo49mCozBgd8iT-s82H3m1gOEOT_r6WxxALr_lhZdwmnht-LLZ-G7xub0noCqRnNVkDl8Q4renfnJEzKx-BAnkZDUpxFxcM4moKxUlS40zgI3t9BOhbV8Q0R09pQpSr6QK1P_vgL8DI42dF147MBfUlgQoFCPy8HBVdXxHFCAKbVvS07jvmgWUbzRwwXxsNqgBCEzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇸🇪
سوفی‌رین‌مدل OnlyFans میگه که ویکتور گیوکرش بزرگترین طرفدارش‌بوده‌که ۴.۵ میلیون‌دلار در OnlyFans برای عکس و ویدیو‌هاش خرج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23356" target="_blank">📅 15:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23355">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBsll-nDpWZtPUPdZjc6KqPez7oo1lMRqzvIMUuuGCeaMvSs4Pn65CVe3A35hQiDH9GnpELr_sD3_QkUbGNsZRQDjIOiddQJLJzX40lRpDWdVDLCQ6mfhc84B1up8mtcAP2kcHoBg64dwdgJPFicmkigSuhAJsiobbBuX3XuZSC7G_KdTwNbUGlL9RYs_t3NrOkAvMM4ULrdcz3uwSe8-qzFPcSoGLZ8bzukL3w61qRrl3XQdpeGNy583QYBZXTkNgnyDRcaa8xY_1Z--RHrjMk_JE4VsJ0cLzo6sqj_YaUhyW26oXE_d_WZs0qkGaTJM0VtF035GRYayKt1sMptFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌عراقی‌اکسترا از انتخاب یحیی گل‌محمدی به عنوان سرمربی جدید دهوک خبر داد. دهوک تیمی درکردستان‌عراق است که در فصل قبل لیگ عراق که شب گذشته به پایان رسید در رده دهم ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23355" target="_blank">📅 15:31 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23353">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JWkPvNqSPd9MVgh1WjySjMFyaxLGqbO2iZARcw5yJN-arLK3Rm9kwCzLNCUCjU_B0lXySI4l4jEZAQnJHmsq4sjXIzYiGPjw1TC-z6EhvGYo_ll85cgeaZRhfANz6rLeCvt5xoOBZJ3eKWWd_mDjXe_5lwVVZBNjBDSp10tMe4mkbjFpexAE7PC3pcAHz7yMokanFMQ78d946XeFJzfaXPqRIt_ZKvggZewL09u2-dNdvWGqwmPa2WIyToTr4cGdevNcxj0Q9N63kBAjjusnZcz7cNuQqXr9wWw1FORytORlbOTMbhuzxO5rSUCeJo1_zmJCtaduisKuzZa7REatng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n85_65G2cEEPR30dQi1ZwrU4K4hO3DzBh6o77oUUTsFrLWeKpH4Wmi71uew4OVDX-9ZDQW4tf9_rNm5KNCmUph23BqI9w0fbknqFW7TcC07W1kFYaX-C27yRr8ejcGpRx7rIUkYau-SWRvNzCS-9GUIic6hZAw8Lm7ppJ2i7uEnKBaNme4c98n31QgjS5NYnTT0QM86ENjlGChGP_G1tcbUDjQbl4OEpsysv-1AsnIVzld5r8rDCglxX-Tp70Y2pkDWPZd7YrqYFO3pvrLlkT57PACMoD68Yx0am0fHK-hr5RifNxi04bjYm94vrv_JmTUXxInEOKkhtobAEVA9XOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نگاهی به کارنامه کریستیانو رونالدو و لیونل مسی در ادوار مختلف رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23353" target="_blank">📅 15:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23352">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvFH58eIvFKZ0k4t0VPV4hSzIdfqCFYf49BpXCmKeNNQD-zOxgwfzN9NMNfcd_TQlskRmveUKeSbICFzdBg0M_OmOdqlgjoZb6H9yv9kyO6NDFgK5Db_20cNQRAL-Va89SRYpvboOu4SZ1cQRgWalomiD0Xzpri8xkfEZsr5v49awD76GuAHirWCHrT8A52L1wNSJG_H1g5pdagco37Tm3o6pO2tEdKYTtorgK_veYYjmxQ_ENn9t-VMlC8C-38ScoAhbLwj_cS5j0OBqPy1vDwqUD-UUnzZoQxjViJJTaBp2oUinarl7dSHowxkZp2RtF1MOmmRl7DJI4rpighyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ‌ملت‌های‌والیبال؛ جلسه‌‌مهم پیاتزا با بازیکنان جواب داد؛ اولین پیروزی سروقامتان مقتدرانه بود.
🏐
ایران
3️⃣
-
0️⃣
آرژانتین
🇮🇷
25|25|25
🇦🇷
23|19|23  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23352" target="_blank">📅 14:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23350">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/llKaVyEhqE1FoGGNMd6_DpRP_nCU1u6vjYfvUdaZrHc4KCwQfsZOgSoBEKSnY8ufGEO8RJDSZol-wjVIk4nHsenCNXNmJrMB7MHMezdtGTZg6b1cim78sta1GaGN-eDSgPsZvHC-3E3J9f061bxEfaS8NHrHWZx7uKV1pMw4fiqXnyGMIfPUGdfqfSsMEXQdVieMi5qJdWgUQ_fLhiL8WPRKOLjuSkuCCTdbH4AFyw3HTLSTGko0pS1iiYGXuIRWHZIzkOR53nw85s3JNAUAdynafZVEVi_of9ZoEskHh_f45OiL1RkxAn40_Vytx0oh6PQNJeiMlWlF0HeUG3GXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lHNjMQ4rkzEqZ-SeLDEUBvcAetmLD7SjldwKCJlIIYNv9wM4xnAE4zkzSi4KT7jGcj_NUC_CkBvAxK9SQw11RIswTYVj510QVuHCqJzK9WR0nzvAh2ebFyH58oikLeOFVj714Q6MKEr8YWAlNjFGIqJK8YqUre45NxnbM3yA1j5LDlCoho5o38ZmFGQYehHEf1y8iFcE5phOA3Ygp3o5RXjwPKVSVDya0NexMKBDOGsu1jkgIG48cfvRmxvUafcR-Z6_FOn7SpmIukcT9QAXOL6l20lM0wRiaOVOFy6xK_Jq6k7HTUGi-F1sT0od8b5WSNLy7ztgMT0bGxza4ovtrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇬
گزارشگر اختصاصی بازی‌های تیم ملی مصر در رقابت های‌جام‌جهانی 2026 ایشون هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23350" target="_blank">📅 14:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23349">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvhzARrFMTCCeGPi99dKsO_D4PNnivLitZxcxPF24jWt_lClvIwFh2xv6wCFtHH8KehJqUnBDdnRQIs3pLrBt4VVJZBOf9o-nWKdkwRy7AZTsg-O_WgJoIUTLwwD6hNUSmSkanSGPL2kB86Zff5DNZtFwIsDAesKdIgIfSfvcfAxNcjFxrg5oeFvSFBgGSy1eMIoMaJzV3OY1-3wolADmcDRzNqbsRIe2c9SPsFPv6tbvP29hT2_hb_nXaVPHAyis-VmVeWH-PBir2U_H9DK-va8oo1mD-6EbBrWBk1gX4-DU6BE29XmQPdZWc3RmOfqe0Dc-EJdFdV4t6N_6Pz4Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23349" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23348">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=oWSFqFkBloU3fAINN4hXm-WgcvxEke3vEL-PJVIcvVQFXhy0I1nfWFflFqV86LfCr5oHyYTvvp7qedjCVuZBytS_1KMSmtJi_e6AzmKi-FrQlzmlWlWfBBMF28Vupm-CEIvDDHz5WYj6FXV-vnM7XkJVu73XPBcDtLVoE90ARDgHT9Usoxa1ggfo8Bw1nOTmQ3W1PUyXNJx5Vq5I0oT3oFXNjYYs0fp2CxBHXU-BOpvqHjscTb-XkxgC1xRfTBaq1OKIy1Kmt8-1uWEM2Olmn6q0Yoif7C04iNgwxvZ-zSeSsict9nBG-XPHyaF9OSTqOQa2t6JXREk43jlt8ySBvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ad2f53b38.mp4?token=oWSFqFkBloU3fAINN4hXm-WgcvxEke3vEL-PJVIcvVQFXhy0I1nfWFflFqV86LfCr5oHyYTvvp7qedjCVuZBytS_1KMSmtJi_e6AzmKi-FrQlzmlWlWfBBMF28Vupm-CEIvDDHz5WYj6FXV-vnM7XkJVu73XPBcDtLVoE90ARDgHT9Usoxa1ggfo8Bw1nOTmQ3W1PUyXNJx5Vq5I0oT3oFXNjYYs0fp2CxBHXU-BOpvqHjscTb-XkxgC1xRfTBaq1OKIy1Kmt8-1uWEM2Olmn6q0Yoif7C04iNgwxvZ-zSeSsict9nBG-XPHyaF9OSTqOQa2t6JXREk43jlt8ySBvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
اسپید یوتیوبر معروف در حاشیه بازی بامداد امروز آمریکا میگه‌ رونالدووپرتغال قهرمان‌جام جهانی میشن؛ زلاتان هم این‌مدلی بدون هیچ‌حرفی بلافاصله میکروفون رو از دستش‌میگیره‌ومیگه برو بیرون بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23348" target="_blank">📅 13:45 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23347">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ga7TbquLLegFeZIqvIxQjQ9qvbkVQCDoiAUX5sulR77suGgriV9oKI7GlZAEdwoWorvFIMdeWL0v0ZmmnSWP1tOPb296UXSq-iBeg_H2up9Gq9z9uo1JZ5I1kIoeL5gQVxJKB7vWH0QS5Ql8K0MaCCkN5S9uxNhkCLZ11wEHkAKFubEv6XZmOS4OYejNPAH7Zok67HDGIKKTEV_62Tscg82sFnHUS1fckNLY761s5JjibbWYYEvL9C3kpaMv_gDbxr1KvVndaj_1hAkzFmJSqQcDS2GoQzwuXlbHqG4sKbKtQzy2K2ArSRBH0HG4t2zxbdpHSwX9iSlwWzJCx7ZJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23347" target="_blank">📅 13:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23345">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mO9sAuSFBYtAuYgV9j-v1U5xkOH1brDUWC45EOHVLv58Dwgd0wqxfq4oBERkWKCfAFvbk6lGcGKeHBBLxMjOIot46PBeVa6yj3q4A9PWjSTAzLzEQAEhgRZqrrs3eyEC3tXF0zx_T6_Ld4VW7khRLGs95JVjTalOl63bw9Xsj90mMB0a7PMeX1TwHo6V0wkiiBotfDgIjOBq7O6KhV0LxybWMjCe1cliI9Ow5ygURWb91gu9deovjSuAs81TV3VfuWoUyrYGk52CFn49XVisRdSMlnnK42ey4ujEpj5S6G_4om_qLtU88Q6ThawU_OUtVsOsQhuP_5kRHjYCjD9d_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqv1RK8_EfQ9CmDSHL52XT0eX9lbiU0m58B372w5tMn8kgvSVdAvs1sS1aBB1cr82t2C8tkZa6rOmOpApPfez-7QtGA6wg3FqNE6jDQjQQRz5dkrP4LlCs1uQpAuME_BP15_SiOu8tMQlpLAWXcUTKZppGIjxCXWKL-ZeBKjx8k8U1AYwSuRJaqn0G8dungF2fg6KrSkRPjoPDeh6L53sfcHQdss2fIRpwS0QfHE8-3Vvtz-awgaJfSFVquH16WjRvCVooW_-_0s97xeZmKsJQWiAtreVzDSCYXb4GDDxDcwO8tm8jmzHFPuAz70_VOujcrs-pWFcbjktK4OPu1dXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خبرنگار معروف باشگاه شاختار: بازی دیشب بارسا و پاری‌سن ژرمن فوق العاده بود. انریکه یکی از بهترین سرمربیان حال حاضر دنیاست. همچنان معتقدم که باشگاه‌رئال‌مادرید قهرمان این فصل لیگ قهرمانان اروپا خواهد شد...!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23345" target="_blank">📅 13:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23343">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pt7phgTKXi4mv4JY3b9WNJmuWDpMc7lETS4frnHdlUxDbIaNNLam_j9GrDjjBY1y_yzv18FYf8YlS9KaCcgDM8-jjfI7ZuIN4kidcEytFS9ES4kRuTJNR4ce7fWwFgUj7hiG_HoNul8DvQuZTpNtwKqBFkBlIrBxgVd6ieDcpRrjRjTQga5c3EXMsXvGtpbfxvJjy4flDeBeP4-1IyRrGpDLaleDfQXXU4J1_-Hd26qxIsGsL-SdwsweGcnOuI8js7tLA85QjCxATkznBhhzFN8N_TnUptLnj-iwWQyxbF2kCxhHUvi6wioNYV8zSdbUPaSHOWj9xBe5XxPCC88hjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23343" target="_blank">📅 12:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23342">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/antjQi95tlf1KY1n1Rze4cisay02XYb_LUWPaRmYjGFkEFUiIdO9mvTjgmPc3nR0dXLnEU6d7BjzhP1X8paED5KHfN-omeHUiY2Jm5kYoNom6weLoRT-hlkKGzDSMDKbBal479SpVmJhVyzBQE1zuB28I1PElfArXV1hJYfJoVSwJSJuifR6b2hy-7aAXEwxEuYaehUIS6bM8G6QTFGGxEXZa1Mt9G7EEUq7J85aohMoKeZrfJLf169Bbmnmm1M0iU0IhUEdISmgp6dhMxX1oRiP5laCVz49UApyTP_TKNN-YgHsM2BviuuuPVyY1tRfKAixa-5-xx0avOmgvSJlvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیف‌وتجهیزات تمرینی تیم ملی انگلیس در حین انتقال از فلوریدا به کانزاس سیتی دزدیده شد. بنظر میرسه که هری کین یکی از قربانیان این اتفاقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23342" target="_blank">📅 12:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23341">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YLsf0sDfSLZbT-YdCjyShcV_ipoaNLu_yiE3kxzCrsLVyHYQErXE6kaWv7JmPZwNqC1ccuCIc8TQ824-qIHa9a-YFbNeqDD7xV9Jcf1GQQhl3NjJ9NOzCLRVJKhxa0RSJFPLbxINkk1LDzEXG9bkxL3fPDa8wY7HP2Sdu4txQSw_7aNKTcTdcndPmCRmfghUliNsi3P59P9mSTQITI-pkhcanTcoAxgWg_tmhZrd-3ChLN36nCtWV6mih-wbo54QVDnsZzK1KDxqR-jqiZojZaI0fx24TLAUWkbpshCCjm4RKq7y-ym7af58JrTkaz1We7gOWAr_7QbyDPjxJ32tRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه سپاهان برای فروش محمد امین حزباوی، آریا یوسفی و مهدی لیموچی روی هم مبلغ 220 میلیارد تومان میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23341" target="_blank">📅 11:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23340">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HXi_u1Y6HTH7JJpE6hl5OKBpzpuTBRA6wMpGdtI4nWAzv1x4PWGY_NAZbPrZKTn38A4L9eI4rfBX4MpKIH3JpdC2zGTLXbHpqHxgNVrAqmh93KrocouMJ9We3si0x_K_JTfUbT-ha03-1hNTeEmL2rOnKfvC1wDWt-L8A40KZKQ0aEfppP9VnwqTVVyXK6Ob6Y4XhogszvbWrVnpZI6O6Nnubl1kamIMIJ29PTsp84SNdDjWv6zITb9UJN2rOq9JCiQ-iHGaQAUQXCidu_eG93iJJYK_KThVEIpU_nAr0rph3euS8D3_yj572b3E1AznLQIK2AEZG4KRgXuI63-evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
گل‌های‌دیداربامداد امروز دوتیم‌ملی جمهوری چک
🆚
کره جنوبی در هفته اول رقابت های جام جهانی
‼️
هوانگ این‌بئوم با ثبت یک گل و پاس گل و آمار بیشترین تعداد لمس توپ در زمین به عنوان بهترین بازیکن دیدار کره
🆚
جمهوری چک انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23340" target="_blank">📅 11:29 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23339">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0hpJOkfV-Wi9FJR5BdnS5qRZZ4KvQvGn7O4xOq0PNolZcmA74PITe7Yu2LmQKtyht1bQmI6Jbhfkex62jO8tGZ6708wSNR-NEdTmX0btdkzPG87zE774KUkO5BDpnvpQ3uCYSjGPsJICSeDvzskP2RukS0aHEveBE8dvQfaoEHbSWdcCve9G9-gYxi0aRQsQAq7O2y4ZwNnUQb6Wc4Kx0pKVZsfTHcNXc1M0k451_xk_dCo8Rp2UP_9UH2KeeHRVC4rLYTrVVFQZ0iax2l7J4kn-DWREzd9RzPg1GNe8DyVJMydc97XULurhhzh3V3bBYdilsMVW6qfhM8XzPP-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
10 صفحه برتر در اینستاگرام با بیشترین تعداد فالور؛ کریس رونالدو بعد از اینستا در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23339" target="_blank">📅 11:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23338">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vaeh7v9_p7-dKI4tXHYMTUU5Packj47v81QpDdR_AthzKVjBMhqgWu-pGg73k9eAdpKlXwCMCMK83s02oJKbGkNJz1P_fgNyn5MWBix1l7gmmmm0opx30SympGxzmJZruxQpNIHPekCh1b6hTKJfMpiQg7-u16ha-_Cjv3x3ys7FjCfEOCUBpYpa9wOhoHeQSNDBuSUroAihF8aMpEbgE6-GPJ8pkCM4QhypfVuJ6mHy_Om00MAfHnQ8hyzBtaDtU7MN5aqZbn-Agk81mYmqLhDiFY6BZO2WbXU2NUA0BPWu8kPDKISgaaHclQL-GP4g6HzqUI3YfIi5eUOyfMdKMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
محسن خلیلی معاون ورزشی پرسپولیس؛ بعنوان سرپرست مدیر فنی سرخپوشان انتخاب شد. نهادهای ذیربط مجوز افشین پیروانی رو صادر نکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23338" target="_blank">📅 10:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23337">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgjN8E9V3gjEHX5gHjdw_1cqIc7OanzK_wKJ2pBXRD95SzQEjjDgU-J-fgLKyJ1fMy4JGKJ0Tf10senO8VCCKrothZt21toTL_tUG7JaGa6kZWeTnEEp11zCmm_ULHLybDN6M0SWb_WnzDL4pfgj8U_BMywZGO9qXqnRaBTpolO2gwkRXN5xsnZRFCQYjsRiKROp03tJwbuNqwNosNfF3NPEkh9i6LjxUAnpsZb2kx6MB5IiXfWeFhGeaNPJJnhwWaiLRKLS9LodBBSiAJ7qJJh_jSWKqF_s2K2KmwC8nhIuEmuWIg7GVmm0HGXiUkm7Uecp0DVp6j-vAp50yoYCLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23337" target="_blank">📅 10:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23335">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29987e4127.mp4?token=GDnpxDBHSpkWyA67A8HQO08iROso5vNX8uvpq9aklyZIFIJhjkDfIUe2V90F6ztHfRehZ8GyLwsh89WNNyaZAF8bImTIbjPl5WoAt0P7BsIheWNNZWr9heoPireL4qrUILwaN8ZJ1w7fa8QsUStUb7fueCTkDK7pAUT9dYBLNPiD5IpH80Nlf8no2kKErjxCepXODspNVGfTkjxfu5MmylxBY7vCyJx06Yc5bwqRDWBW7HR4DLArj0DdYX9bvfsxctnM5KFK9Qx0YAHT7vtCtftZ_44XHe_GYs2NKNR3X6z6U-3vHEMAGM4yxvZusE5GA1ayaKakGT2l1vvbInb0AVeoqS1gqeYq467MnQAHe7TU9n-1q8vX8LiDmtgxn8ND-E1jZFcG4VyVAKgN-NnwOLldyQ4aZU1KiWEgAf1jqJdUEIPrZwGzfrez2JLI8AiJvlXOPt7Ws0v6luY4_hjEl8DAtw3TayHSZzCP-KCEz-Go5nEzxjTKLi-CXfpsxgoh2dqoYcIR-WKepxueE4t6lENUoObcHz7-XcC_bwhitxvBFcldjVGhWlumZl7CFUBMUlMrmdthfGzz_LBffKMzMSCSsBIUHBlofkOHwcYOuloUWKKQOLI0QLw4zoreqoM5-y20f0KoRyHgb4oArvaiENHAtSy7Mj9OK5PGZE2ljwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29987e4127.mp4?token=GDnpxDBHSpkWyA67A8HQO08iROso5vNX8uvpq9aklyZIFIJhjkDfIUe2V90F6ztHfRehZ8GyLwsh89WNNyaZAF8bImTIbjPl5WoAt0P7BsIheWNNZWr9heoPireL4qrUILwaN8ZJ1w7fa8QsUStUb7fueCTkDK7pAUT9dYBLNPiD5IpH80Nlf8no2kKErjxCepXODspNVGfTkjxfu5MmylxBY7vCyJx06Yc5bwqRDWBW7HR4DLArj0DdYX9bvfsxctnM5KFK9Qx0YAHT7vtCtftZ_44XHe_GYs2NKNR3X6z6U-3vHEMAGM4yxvZusE5GA1ayaKakGT2l1vvbInb0AVeoqS1gqeYq467MnQAHe7TU9n-1q8vX8LiDmtgxn8ND-E1jZFcG4VyVAKgN-NnwOLldyQ4aZU1KiWEgAf1jqJdUEIPrZwGzfrez2JLI8AiJvlXOPt7Ws0v6luY4_hjEl8DAtw3TayHSZzCP-KCEz-Go5nEzxjTKLi-CXfpsxgoh2dqoYcIR-WKepxueE4t6lENUoObcHz7-XcC_bwhitxvBFcldjVGhWlumZl7CFUBMUlMrmdthfGzz_LBffKMzMSCSsBIUHBlofkOHwcYOuloUWKKQOLI0QLw4zoreqoM5-y20f0KoRyHgb4oArvaiENHAtSy7Mj9OK5PGZE2ljwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چالش جذاب هوادار ایرانی با کیت های تیم های حاضر در رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23335" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23334">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c684a93218.mp4?token=te8j9o49bH46aga0MBdWhekQ4qUwZslASUuNYXfT_zFMcypPdXmEWBDEkPDqn4IBIEUWXFQJUHNqO1-ePy2sncDez7klv0tOUL4-cBJ1eC2EqsPOXu_Sb_rvRG6G0lMwdGDBQI0qFxaH84Jais3tc-cavCDsldUccv9SaCSP9UDWslHgMLxIEFzk7Z3Fybc4cIRCtce0o50TTZe8ijmXsXnaFpVnn47z9w0FffejVVHt_zNdgudCxZWJfJCnMbNC-MSpcud7V8vDhTcVq0wC3CG4EE4NgeZv0qMD_SJYztVJ5xdRD3qri6UrdWkPtledBB_1eET7dBBJQV1CMueAeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c684a93218.mp4?token=te8j9o49bH46aga0MBdWhekQ4qUwZslASUuNYXfT_zFMcypPdXmEWBDEkPDqn4IBIEUWXFQJUHNqO1-ePy2sncDez7klv0tOUL4-cBJ1eC2EqsPOXu_Sb_rvRG6G0lMwdGDBQI0qFxaH84Jais3tc-cavCDsldUccv9SaCSP9UDWslHgMLxIEFzk7Z3Fybc4cIRCtce0o50TTZe8ijmXsXnaFpVnn47z9w0FffejVVHt_zNdgudCxZWJfJCnMbNC-MSpcud7V8vDhTcVq0wC3CG4EE4NgeZv0qMD_SJYztVJ5xdRD3qri6UrdWkPtledBB_1eET7dBBJQV1CMueAeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
بازیکنان‌بایرن‌مونیخ چندسالشون بود وقتی نویر اولین بازی‌شو انجام داد؛ منتظر کارل بمونید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23334" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23333">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">💛
هنوز توی MelBet با این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
بعد میاید سوال میکنید کدوم سایت معتبره
❗️
👀
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
✔️
🎚️
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23333" target="_blank">📅 10:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23332">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGGFIHyNKWya78H_iNjubKofHl3gGIF7EF0y_fMO7eXwAIlLgQxgrrFPKZVmi66VZyzBknWr3wR4-pUVNkHq-eiHpBfNAB4ag-wUMGdtLRY-kpgAX_lKDxSFbbgtUzSpPHTh5bSlw3PGcssASNw8PfesZ-bg0VArmKTwqzP4rczasXayPQ-Y7aAgvptrrYErPzMHPSeiIWaBEenVE4VIVbGDD4FRSx18-Su16x8NsjmdJ9lCVfcgQO1t13e06zKphnNsq-oEyCKE_QGUswUfgv7BwMyIeymGlaZQCNZ_iIf843kiXrOBXmORDVVV0dRw25HPh_SmSqPqWzprRimhcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ باشگاه استقلال طی‌ساعات‌آینده مطالبات یاسر اسانی ستاره آلبانیایی آبی‌پوشان پایتخت رو پرداخت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23332" target="_blank">📅 10:21 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23331">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">✅
هفته اول جام جهانی 2026|آتش بازی یاران پوچتینو در گام نخست‌ رقابت‌ها مقابل پاراگوئه
🇺🇸
آمریکا
4️⃣
-
1️⃣
پاراگوئه
🇵🇾
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23331" target="_blank">📅 10:11 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23330">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFppIbLwu49JlhwK-d74kxHXNAuB-zaoZjd2Si5YYfrpA4h_B_xMz68pCi-cxnZHzEhNo0O4ZTEU15Q6pf4lTsk3l6yxAmliLYHbePiyOJYPfOXxpfcAi0CuMCV4ndOTXsAXyLdSQf5YHw0rfPJvmVz0cp1MuODTyiZygOk8taxYr7h4uCwcnYzV9S774l6YvsPgcaPZNyHtYauUiO202pbKfOyfGLzsoQACgIalEue9ISXVEzGZXe6nxvQrKWycs0hwUK4S462PGvCsU_o6MSdaqW7hmCVdvlQY7AIole28QsgbmRW1Pnf0_miApP0h1GNqwkby7xkBd5y1ZeIu6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23330" target="_blank">📅 09:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23329">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=J1epWG-nQyu7wLmORj-t5soAGznt_hxG2oeMGOwzjxILfoa-BXhKp8vcFFzY9X_95HXp8YwJpJpvW9iVGRD6ksO9pDWT_4Fq856FXBR2ypt6NvjL6SEKBnI0dOB1LxmQMs8NM7vnF7pPheVVKCjddqJ5CyyoJeqB305qPHz8cvYilVpsfogO44LqLbJRFI7gWOU07aaEzl7b0F6tcM2sr1peqlRcKVulBgh2vMYUKORaIs63LrtnMQwbcuD-OOkW-doxfUvNJYlaT62q00UeICV25IAgTJLIm-3FliXFyrIkcrMnRcnHgG1R0tt0tneTYeoMAlgfRU5KQAIRNy88bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291a03c3c.mp4?token=J1epWG-nQyu7wLmORj-t5soAGznt_hxG2oeMGOwzjxILfoa-BXhKp8vcFFzY9X_95HXp8YwJpJpvW9iVGRD6ksO9pDWT_4Fq856FXBR2ypt6NvjL6SEKBnI0dOB1LxmQMs8NM7vnF7pPheVVKCjddqJ5CyyoJeqB305qPHz8cvYilVpsfogO44LqLbJRFI7gWOU07aaEzl7b0F6tcM2sr1peqlRcKVulBgh2vMYUKORaIs63LrtnMQwbcuD-OOkW-doxfUvNJYlaT62q00UeICV25IAgTJLIm-3FliXFyrIkcrMnRcnHgG1R0tt0tneTYeoMAlgfRU5KQAIRNy88bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
تیکه‌سنگین عادل‌فردوسی‌پور به امیر قلعه نویی بابت ساعت دستش در مراسم پیش از شروع جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23329" target="_blank">📅 09:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23328">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=FZvVS9WHgVHnuJi-p7wPSAmu8PZHgPxNRkoThNaFbXeT4MOn7w4kn2tmtwFkCiJbEh-VVR0TVqbmQ9PT-c08z0Wnv15LENnMXHIdy6zkiiAO_l8zD081DkESrwVPSbJ4R59kjNK5ke8zgrU4i6YJ4UTIhXz2ExGczJdjcdLQyRN-ypRd23WC-VoFovyvqbfne-XC3KS5uHLZFUMhaBfYRioP-IC4tTa7bdzKAaFZutYRm8LJ2FwdOGtyZUMRz5qjNbHoKiUnMLqrLikMbHR9M6v6QFNy1b92HfR5jt6A2unj0gyGPB8ZMTUdksc7ApbEDO045D_bND0tzmFW_aPUR1LYVVGn5tFEEsIeMs6SqOihGPDetB4HwKIVI0_-YlE_4sP7EpUh7KE-VDvtr17MhwxEZ-gomYxWRBl_wb2pjyvJmBjLpzSm0IyFEuinzMknBxG4DuPVfDCjfnZIa1SeLPNMs9v8PcLtQTMNNnYMS5m50QWSN9vNsg16fi39xp6NTvyExXTOLx4gjB8Hl_sV6QIhVtYjkBQ6sxt82AD8jkYjZBXIpdJ-qlCsqA2FUJwiv9YtsKkxDTN1CqTyndqXGf0GIbtVAyyXghpmSg6ptQ-zHcUQThozo9ob8c1IxJYiDIQr0YX86pTzsmQTOKBB5_yaIY3UfxBzjjSohgB7bLc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5d11f7375.mp4?token=FZvVS9WHgVHnuJi-p7wPSAmu8PZHgPxNRkoThNaFbXeT4MOn7w4kn2tmtwFkCiJbEh-VVR0TVqbmQ9PT-c08z0Wnv15LENnMXHIdy6zkiiAO_l8zD081DkESrwVPSbJ4R59kjNK5ke8zgrU4i6YJ4UTIhXz2ExGczJdjcdLQyRN-ypRd23WC-VoFovyvqbfne-XC3KS5uHLZFUMhaBfYRioP-IC4tTa7bdzKAaFZutYRm8LJ2FwdOGtyZUMRz5qjNbHoKiUnMLqrLikMbHR9M6v6QFNy1b92HfR5jt6A2unj0gyGPB8ZMTUdksc7ApbEDO045D_bND0tzmFW_aPUR1LYVVGn5tFEEsIeMs6SqOihGPDetB4HwKIVI0_-YlE_4sP7EpUh7KE-VDvtr17MhwxEZ-gomYxWRBl_wb2pjyvJmBjLpzSm0IyFEuinzMknBxG4DuPVfDCjfnZIa1SeLPNMs9v8PcLtQTMNNnYMS5m50QWSN9vNsg16fi39xp6NTvyExXTOLx4gjB8Hl_sV6QIhVtYjkBQ6sxt82AD8jkYjZBXIpdJ-qlCsqA2FUJwiv9YtsKkxDTN1CqTyndqXGf0GIbtVAyyXghpmSg6ptQ-zHcUQThozo9ob8c1IxJYiDIQr0YX86pTzsmQTOKBB5_yaIY3UfxBzjjSohgB7bLc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
طرفداران‌کشور‌های‌مختلف حاضر در جام‌جهانی؛ از سری جذابیت‌های بزرگترین رقابت فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23328" target="_blank">📅 09:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23327">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⚽️
ویدیویی‌بسیارجذاب‌ومختصر و مفید از مراسم افتتاحیه رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23327" target="_blank">📅 09:05 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23326">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYMZBrsrgFgnqxpK5dRYuwF0mnXGCZLvohhCFdVcLDJjP8SH96ahPiXNz0DQhuzgkOlEK2ZadcYCwpMt6Cscm8WYFxDNtBZksDvKYlV9C4RNeNFNmmj8GBjnwY1NKETgfijiMS9Tuv7TwN4IONISaWvGSwBB-jzKNgdQzuO5_IczHBjLNt1Etbw2cMKTbgynZdOh-Zu9LHYrLSnVwkirket9pf6Tj-tE1UMnF-Iq2kWrmpbhH9tq7qcBwcGI4zvA9kO6LGGZvNPKiXPz6ceTtIgUjxe74DQUQU8lmju6jFXIKHQMAAznSY6YVYydnlEhj3bOmRf2HFIthrmykkDlTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حال بازیکنان تیم‌ملی والیبال تو بازی امشب اصلا خوب نبود. این صحنه دو ببینید. باهم تعارف میکنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23326" target="_blank">📅 04:13 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23323">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gdsli3eHifidqjU-7TVyAQ-3TeDHuQ-ZpuzLvRr9-2i4yN2F_JZiSypFNfwlZJaNHlEFFxDMjsnjUBDkEAV0Cdexzf0YtYFyAe7AMp-_gyYIwQzU9hnzhPkvVPvWm1earIbCTt6vIjWqDRePBKktjxcJBni29GuSPHWa55gO-7hBk3lY-cD_va-T6PIXY4wbRClxl8yglPOCVe6RceS0OeSGFbA8Q7F7addWnui2PItPcCcwlnIRktJTBkJEVe6vFZK_KkWVhYbmP4cz0mfVU_V6a1widrv7ACqsk6gY1AwlbM95yrx8RJd6_i9qM4ezKiTa0cTEbY0yRpeSsNbInw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ceMkVNwQS8PVMq-jRhTnmq_p87bASoa9tS2coJKszp1EVPkClVrAK8JnWT5kb8e-xOPj1-4Xn9A40pfY2nIV7fKY_VV-fvWdBOFT6WatEm3mLhgJWj4EvSUEDJNiJ6sQwv3pGW3EtSjhJ9tzp8bBpyYS1fZkRXrPkumw8n2KIAvgkampwWy58s6dF3LMlfqpPUd2pb42767ioobr97Nr19m_WHqSQEvi0_xPpK9TLewP48LyeJJjIH_pHRCDkUJCJZ6pLyHk2jEHHqtNbNOzp9UAGUcnZ95az3VD6nRkpHWu1qiSpAzPSXrciB3XkRH3s3-4vC0zgrR5WWSN88j2Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
امنتیت بالای شهر تیخوانا؛
در ساعات قبل رو به روی محل کمپ‌تمرینی شاگردان امیر قلعه نویی یه جسد توی صندوق عقب یه ماشین پیدا شده که در حال تجزیه بوده. این ماشین هم توی پارکینگ محل اقامت شاگردان قلعه نویی بوده که دقیقا رو به روی کمپ تیم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23323" target="_blank">📅 03:07 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23322">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSQNTuvFZvONcsAaxKNyWeFFjrfDMv6mQa5rrZMKNto2iUSr9Ja1AMHWGzAq1lmZhCxMh3B90zxf69u9BnPlFl4LP1P_N4Lsc2rhhUEsH01xJeWk3WC3VJsWWv0pxLsV8WVtsLzsyMl59YBANUKtzIRvxm9n8eN9JKerZjNyXIc-aKm90w86i61GC2wpStR9Ji_KavEPjSA8GFEgkwkriDOGDOZ0AneHp0Ki7XYQCbaOmN3LcgqnBQQFqMJGNwNAMiaba5IIopGfhvvJ60KhjQcb-3alqhUgZmErVJsLBrI2Q1WXOyrg2ayy-ObJWi9pSZZa9SQCqh_TYjrgIJTLDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
👤
بااعلام‌کادرپزشکی‌برزیل؛ مصدومیت نیمار جونیور رو به بهبود است و این بازیکن از هفته اول جام جهانی دراختیار کادرفنی سلسائو خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23322" target="_blank">📅 01:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23321">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9_1f8GSrrIylwvFMmnWCcLBsEDEA1AdefY8O8vSaW4PC5OvapRMwZTXBigLVN-xRfSt9ohmjx1RUxDu3U7poJvkQz4i5ALpMzb4cZageKrjZ0sp83Uxk7KvrGuxMbCjgy9EJpt-05qyUyoiMkzYMIh8pPB69d14RngDO_NVQkOxDV6DZBEdpBg1sa8Ezf1mCNqMRiCE84DjjgfUtS0_5UsFhXW_jRpE8k6GBjnNQ_geOy4F6hxMFsL22fpHPDuOc--z_qcG8Oc1Qk61xxgi-OQoWnRd32STGDy3lSCDReG6xiBveKoQJKdOuyRIg1GLQQqEzjD_dpU64CsNCU-ukw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات|نشریه‌موندو:دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23321" target="_blank">📅 01:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23320">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">▶️
قسمت‌‌ دوم‌ برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23320" target="_blank">📅 01:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23318">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMbTKDUNCk7zu6UDHs8GAD-yy4cmy-ZL-fatCDD-UhIl2NyXF9C4QYewrrxIoXj7s766y4gCBcw12V7XnkRWlv5YrOuAHIiGSDRfhcaGKGqmdS_BJAukUZvCRmfIuyrE1dX93yi0X7IJMrVnuQ6qnWsarNudBLAKgeZrtVGMOzp1i-DUg3WLE2hx9xF2C7-glZTz7Nn0popOm1d9X_nQ8q8Cp9R_PLYVsvZNcCoBG3dkdkhTJcFUXYchERRFrw4dnJzmC80Kbw7ANbMuDR2RYjPhySIl3q4fMQXP2XNUcgIEMr8tBW3KDuYeVErMFHa__9NBldiIMTk7gQMtEGNoLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
ازمراسم‌سوم افتتاحیه در کشور آمریکا تا‌اولین‌تقابل‌جذاب تورنمنت بادوئل فوق العاده حساس برزیل و مراکش در بامداد فردا
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23318" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23317">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpVjuSPfLj14LyPZUUz67-9uJ5Wn1xMiTik7-FpeCuQ_7PE03n1Plh7Vlp-huUOG4mlAs_kgUrxHpjt1MaeXVHqmhfUQzNa1i0IWEN4H5rQyAbUyoU4BYN8Zv5o8aD7sV48v6C-J7BhTekQcPGNzvtZJSIX2ndHgnCaQDBaKRWoezRL4jQ_6Jk8-Vgxx-Hx4Ku8RlcMY1Y5nV4gF7LMuMIoZJL0PtgC-HNDFX20UnMl4wXnYmU-jMIWdvxTzDF3L-h5tzau3jDn3W4riavgxJQehZkWnyPJyRmc3Rfn9k7QtojLtQqlllSRG9bBr_YkEJpwO_qpAUexCafNUN4heQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری بزرگ کره‌ای‌ها مقابل چک و توقف کانادایِ میزبان در مصاف برابر بوسنی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23317" target="_blank">📅 01:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23315">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o2Z_qw3CzwOTCGxPj8OYQsz55lMu-c7n0Qvr8BEaHuRBOmVl7ygStRtTRuJKIZlaUVmQRRLls1EpmBj1E-LlRTkgkDccYqjYGoZGaU1lgA2uydUeevqw-fLFT2RdR1ELUA-xhJfvc7kUqZtrdypDUw7SiXFegAa1rkLSzVC9xbOVHdRxy6Zi7Doe3S9g6Cw7uuBNBGHQbZ96ik0iLttDP6x6oMSog1kGs05kLK4mfl-7u8RO-njyXDFrrjUV1ua9_ai0DD7TiEBi_J4dFLn9BKs86wmu0wGpo1X3TAtjgkRcFJgVtWyqeZHFAtm0dJggZf80SDVIPSbK6jgLR9NKVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RndO9pDoly5MoHZUzPY1jmvmDnGwEaZs5GgywTqAdJbZ7oh3HERqFim-otocuBoyInbeUC9G9BlJMgZ2mgrPueFZ2-6Qkcp1_DzZMRghk5FEsvcpry4qZXVHmGF8bfoAoWLjmBMItI96rC9d8l3lGz2M7kklT5UqldpDtKL9PWpqH64eQpaRaGIJWFMNVNMWCGpgbMdZ4rC-kVs04a_5VvzW8vK3a72tWpd7c-hR-aD_mPET9DAlzkHkugvS_AEmr9kQilee2oTMIej8pBLE3kepPV3w9emA7mC6W1AjwYDD00v--7R-Yw0Vgx_XVyaAiOnztWUxYBV4SoY9OVQrWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📹
شات‌های‌جدید نادیا خمز دختر پاکو سرمربی سابق تراکتور؛ ایشونم بعداز اینکه اینترنت مردم ایران کامل وصل شد پست هاش رو شروع کرد به انتشار. حدود 70 درصد فالوهاش ایرانین که اون سه ماه نت نبود اونم پست نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23315" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23314">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLFza0kzAT3FNOk4UNrF2SFW9QGf_1YUGaShYMsXmyGGzlIRvq9kJahnlqICAOvf1kU5Xdn0cYBV3ZZNXLaPpvlK5lt0ulqtEnHsi0F9yPt-lzA_VLTLzJNm3m-tC52Tn05zFrECM9E1LQyNPASSWGgPu_lyp6M4uyXb7eQTmADB40slO67Y4W-M0klfEyq7RCsooMomz2wtwDR4BQvz66LAYPA0BD3P5C0kpubMsP8FgWNw6s1wPzRviWc7XFm28g5bh_u0frRI3HvhZb9p-f69tq6JeyrCMkMpVEt1wYFWHPeRvYMAbD-Lhtb-bBrciUiKmoi7oKisRnMM4UnLfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ رونمایی از استایل جذاب و گرانقیمت قلعه نویی دربازی اول ایران مقابل نیوزیلند در WC  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23314" target="_blank">📅 01:12 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23312">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS1tA61HUs0hNLwTWWILwelTwkLbxFnGl9BAizcP_BtFRzY9oj0ggN1IKxKZR77oMrAaAPwltBAuyx9JJFSMAn4h7vDgQ-3prPFODywnCEydFJt-CrktreebgMJfXYCizi5fbMCpdP4P-V9fN17gT8s1ICuO2S0eLGaPx364Dbs1TQPOtkdLBb-6WC-QlsXkZsiRX21_jIrq_n27byYqZyfeliUQsJwVGIidLmOAtD4VXWO6088CAR8ZQ4GOv3iT8kKGkjjBTjhhnq__bWielzobt-8PYiRZxmdATnQeParT7Hd8nyJcpgwVUBNpSImAThTD4EJC59Db51JgJZrTYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میثاقی‌به‌منتقدای‌تیم‌ملی‌روی‌آنتن زنده:آدم مفت بر از جا خالیی ......تره! همون شعر شایعه رو میگه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23312" target="_blank">📅 00:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23311">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=AievMmoQ6_KK5oYeLGG6QC-gDeE9CTMzjvPLIVvvoPYluOPwvFno18NX6hEvWGtAjq4nu_l_XWEUGORP7-cHe_Vdh5WnZYxFwvoiIcGYsxdbvTr-I5aBljNMiNtbG1QaqZ30W6RIVyXi1D1gYyoruuI-KV-_lpltm2DMd61ftCENtyhgd3v2L56jKNVMgJMKAf1MuDMsjev0lC_o3lZFKn6IO4noMDuPDQkd0DRNpGH9-50S76UzbyCl4kJGosSpp8nAkAGZ9kuKLf4PA3l3ZXHNuz1PfPDlJ8Qt_-wVMLxyc8Rck6K2lKsYoHvKXyxlZqjZOi2Q06UvvynnvIR122saaRHtEVjJqtDPOC-yXQdQhaXL2USG-UzYyNb-dkoAkrVKoZPJx8M6S2zOZ9NkYJPfWgdyGNLD9yCsRIRbzp2ccEEpP-FOvXqGtKJOpNudcjcgPVs1mnsb9LDV1glcSVsHDxV1LSJ5Vlfx5BbCIzuGqvc_XC8p3iTUZCP9ZC_kjKpA6tr3PlEepGHh-R7r9_vg-HepfLBX85vjJQSwAsjQfKyQxeP3GxsqYowTaEO9349E6dQA4CtMFXYW-Suil9Uh7hTALUspyuwxBj_U-hb7l27PyFj9E0l2URnLG-rA_bSR6VXo48-Q2XixwEusyjEgRmKrpnbsxskH1V9bOjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e109d357.mp4?token=AievMmoQ6_KK5oYeLGG6QC-gDeE9CTMzjvPLIVvvoPYluOPwvFno18NX6hEvWGtAjq4nu_l_XWEUGORP7-cHe_Vdh5WnZYxFwvoiIcGYsxdbvTr-I5aBljNMiNtbG1QaqZ30W6RIVyXi1D1gYyoruuI-KV-_lpltm2DMd61ftCENtyhgd3v2L56jKNVMgJMKAf1MuDMsjev0lC_o3lZFKn6IO4noMDuPDQkd0DRNpGH9-50S76UzbyCl4kJGosSpp8nAkAGZ9kuKLf4PA3l3ZXHNuz1PfPDlJ8Qt_-wVMLxyc8Rck6K2lKsYoHvKXyxlZqjZOi2Q06UvvynnvIR122saaRHtEVjJqtDPOC-yXQdQhaXL2USG-UzYyNb-dkoAkrVKoZPJx8M6S2zOZ9NkYJPfWgdyGNLD9yCsRIRbzp2ccEEpP-FOvXqGtKJOpNudcjcgPVs1mnsb9LDV1glcSVsHDxV1LSJ5Vlfx5BbCIzuGqvc_XC8p3iTUZCP9ZC_kjKpA6tr3PlEepGHh-R7r9_vg-HepfLBX85vjJQSwAsjQfKyQxeP3GxsqYowTaEO9349E6dQA4CtMFXYW-Suil9Uh7hTALUspyuwxBj_U-hb7l27PyFj9E0l2URnLG-rA_bSR6VXo48-Q2XixwEusyjEgRmKrpnbsxskH1V9bOjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026|توقف یاران ادین ژکو مقابل یکی از سه میزبان جام در ایستگاه اول.
🇨🇦
کانادا
1️⃣
-
1️⃣
بوسنی و هرزگوین
🇧🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23311" target="_blank">📅 00:40 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23310">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKnPddsVipQZKEH2XSljwF0e2v4bE0vfxVEAc9E2DcDk9qxfl2WXIO90zyTur4r9Qq9NbWKLNglCgNDNWBVhmZUzdJvy3gCGUv5p8bolHL1N0JlLbjtLlWx15qncbi_YhG7_NGCkUPVf-dgfal_k3jR_vif5pJ-Rc6WVOivXwdOFDOfja_vEbOaLcwki9jU-SNBam144zz8W-R9Gj9WdsI2P_OR_T_w766j6csKDdMNqkh_I-0dJaGZnvXIrkkRk3qxBM-EOBVPQHRzev99fMCCIrk5rLp5eQXxbR77k0qVIflZhMST9VRUjawokUNmzt8FCTqFcaJddW-qd7Z5bAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول جام‌جهانی گروه B؛ شماتیک ترکیب دو تیم ملی کانادا بوسنی
🆚
هرزگوین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23310" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGUabK9qfKK6hU2BqQy33VORG-dmmcn0ifrQZAJCSfoTD4eSHhbhPAw8RTlWonLaFj3VPFTHOh8iVZ1A2PIZP1gdIDPjuLzdObMR2hNURYWhqS1tvOtP5OrdMTgx9_vHP1LFKozW-ttj0Xfxh2BORl2PSEBInmRur2MqL7tmcPE1fFwV4rRPTV95MeqNmw-55sd_Ml5g0-n9verBLitmPN45kxtnUv_Nf09uvnAXOYfJb8ePbTENthKo48bX-FpmQMecKGPo5MEOASBSoEXB_ku8S97bxcdgm4t4-Gncl_RtFXbUOyfXOzvXJ2Co_YjY1Fa5aQxx8GYan-LFUBZ7Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWXtG-MpLKuT1C_JaRMDqUBHzfs9ngqGNgoAH0BeZaZnUAssxNP-BN4vBZPefE6YpVyghlhlScxTwHH41vQWWWeJ3uTV-aErBlyS8NTuwFNyJ_aH0j_hhFxqk3Auc2CMvxHFhpYnm3ZY45u_f7il1fKqIMU1u_ugSAkM5spzbTGcCpMbBQzoVL8SHhyQTFlcMjnwkJKWtyL03SM5eVWmQrzYdo2BfZzFkx09q1iDw99qKHTQBukxMgASxLj1f9DLY68V_RFh-fteHWRO-_wVUGN8r9lfD2c-i7HoSlcZkPTvLSVOdOXjD8W415dvgOdnnnlgCyXbmoC76JnDthWy3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bILhOHhURfjVUvI-AwizNysWBcRG3dT03tQH8FvFtFv5Y-ihVlZdiBl1-0A0Hs_MKXNmYezPkgsuW8rjWloUofuvZUWQ_ClVJEvNRXybubZaL-p7AxzsDkZHarHoqo7UnI8CBajtsC_sKrb0Aq_DiX-w4-frdv07d37By7kLpe0gvowUH1PRlV9IJz-znWdNgmpM7hNqhR839KtLfJ5BAqPUgesuy7_Tvrde7aYJyrhGSJWRXQ3yv0DsXaFZeyE9yovmnP8kn5Ky5J23OVUoRIphGxdCLoUnSNiTe1ZYikYTNB0yS8DNftqHJi3LKDY8Lnp6o7ZmcfF-KkI-F8pcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfJWoClTic-QiDdb_U8kZaICfy7F5jP8FA-XFf_acK-is4G0NsO434znSnvBxI8ZM-zN4Cwk8_cnCFbjziLjRe-rA6yZ61JIQyMRbGWWCB3BgBVKiGqEw9QtVEPmApB-RNgpkrkElEgtO5puIbpqe68nFaGvRw9xSelKaA_2LdHKp0y4uaBoOS4esS0bBWg5UaZVBVICAJGchmYu_1K33zBq9LM1hw6Bip_ScU-LFipfSXwKmvOuCwmJQiEysB8kD9UKGloimdPfQCUYoJi5v8EzmejIkOscIF5usYp6uQDFcuaJNtoh_JMsjtbbiMalBZM901yLh1u9XxhnRPLzjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPTLdrb33lumBZETfJz7brnWGPrtUbwzvoD4i5ew96OVehdstGhbgeaYDA7F5EVxbGIRPDmVX-_97NlduawQrCf9MEnDnlcReGM0W0pB_kaMBS2ZieCMwlAbnrp-1cpwMOrfwUxEc_AxPHtdXf1Da2TOzjqBtLkYI6q7lsMucEr3DUNS_4SFN_J9t-zteTk3LeIsVR1mrgFpo7EBtibTOPJYURxAjBDbtHIjlQp6qvvqcW6FfRHU4t-jp7LIlD8Ldl3ro0EqGD7C_om7F7tjq8JoII9rp3rlUq5vQv57AXvt6XS-ToQWlCZqe1HIh_8nojfsz4GHgJ90zHPWcGX32454" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPTLdrb33lumBZETfJz7brnWGPrtUbwzvoD4i5ew96OVehdstGhbgeaYDA7F5EVxbGIRPDmVX-_97NlduawQrCf9MEnDnlcReGM0W0pB_kaMBS2ZieCMwlAbnrp-1cpwMOrfwUxEc_AxPHtdXf1Da2TOzjqBtLkYI6q7lsMucEr3DUNS_4SFN_J9t-zteTk3LeIsVR1mrgFpo7EBtibTOPJYURxAjBDbtHIjlQp6qvvqcW6FfRHU4t-jp7LIlD8Ldl3ro0EqGD7C_om7F7tjq8JoII9rp3rlUq5vQv57AXvt6XS-ToQWlCZqe1HIh_8nojfsz4GHgJ90zHPWcGX32454" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5t-k3U7mqovG-J_DJW_AuARPG-DqcdjHjJOMFwuVp1oWkIs-yqMz_mGyb8UF8ReBQyx81lsQsmK6a4jRDOY62cEln3MeKRuJkipg_1htZ-C8V6289BdPvc1BX6IJe8zOemRD5hME8aRMlIWoH_sqjAfeLo3t15NYbtyI8Jje9QAJSKyb4pi5qePwMRQ4MEL7SL2gXSb7W33Qz81KMp3aoUE3WuJLvqx25RnrUqN5ZsJ_8zUXFFIFYS-V8tUVEl-O3UFECx5yywlqmBkoAe-O7tyH9nIMMG9bALtl9C4U9wU99NAOc46FyNqUDjvbZP4ys_5XLxxykBvc8fVeZ3Sxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-LMG2L53yvxmZ4b7OfJ0GvWuqRXMorJ6p_CKhgg60uPExW27gt8WcmyAuYCHdQmQEq-eN5T0t8_b298nUH9u1bb_fMHBEaNto9qDKfXiB0QypKojXe2_GD-gMWwZDf4mIPm3sjkvWHyu9F9ikmy10Z674KWe0byLIObSRGOriloEFQj9bhOBiaQcl3zFp_yd0Wz3yGXf04y_ryPJg1coLYbA8yPFh39P92Tath97xuo1pwO31xtyLwY7Fwr3hAzEV7oaLEUwFZ4aOknuzAuQcncYal2VEPgADQcI7vCycHdbDGS_VcCoN0FF2KkUjjpCsYQKR1o9c0V49q72NLwKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGAmqZ1aSOmZBFzdAbSJ3zH08FjiNY6S9TNnFpJrDiJibqt-7A2ZPxpOOBRBPJGNNcf2FqaMQOV4RxGaoHF081r8j2Q7SKz2cBQZ8GIuuyV_ywban-JnyilVQUoNylRvMB4CBzU2WAnj3RiYtPPmZfjkLxhzI4xoncvHcexUdgk0rmsRwrt7lrpADPPlLwdyxyFWHgb17gky9egdKHpA1wJ3AieFc5GecL48m_UZ5NGF2Vk9oHuNBIL6B4So2VgI9CYCSOTwBhH9dYC_vPiPW06qReWPhV_yqnlclbACar0IEtj9JP_EvltZC-1aKfS_y3rpl59gP-qEtIekyJcpRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqKKepBXZWdEVNRr4C-AIRev54B5CcpXOcZDyVRCWKtcDYe49QXH6txjFoZDYF709opLurkRATw3Zq4OEQsKSHECRpX_Fu9giX3DGFQsHtb_YFWQN0cCt8MKoZvTc_mSBkeesJ1T75_jRrIuxcipLtpJfX40vV7zu2RnN7mZY390aiO-c0SGpnM92VsojKDv0l31NLaTjJKHakfQz0BPkcUiRWl8Nax03-YgQdBbQwPj1WoBeoXXgwWWa8S72kgl40bkYJYZWlmEi6RVhxYvl0xRpPNhA61nzfFYgxFgi08f-hHA9vu6E3DU2Hg7O9Xh7hKeV62sctD4LyyqsePu0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=IbkvxMZa4Ma3IwWD8tVdgQjzGvK_j3k0yudQ6qVYISwj5NURwDCsPkm1Audg-Pqke4B0QxWSw5tueZNfCNqdj_ZonPpW5gfn8SFHgwqeWOh8I7Q5rPwzzBHXl56r99GQwRKAhOUTA2UaYpEJDpl328dN-GsWIodj5AK1uRGrvXNpZFftbDlV2aGtVrsgvJ8yPyxmacFin2yBBYwQcT_pePpv9oEzxNapCSO5fy18_xa5eHFfzpTc0JU7FqJfh6V_x3IC6itHMJXA4-YGV2adKBNFm_4YzHqp0QmtmgQbe8fVlEN9jjY2aO47WkdhnSZ4sxSZ9PoqCscWAGDuoiFR0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=IbkvxMZa4Ma3IwWD8tVdgQjzGvK_j3k0yudQ6qVYISwj5NURwDCsPkm1Audg-Pqke4B0QxWSw5tueZNfCNqdj_ZonPpW5gfn8SFHgwqeWOh8I7Q5rPwzzBHXl56r99GQwRKAhOUTA2UaYpEJDpl328dN-GsWIodj5AK1uRGrvXNpZFftbDlV2aGtVrsgvJ8yPyxmacFin2yBBYwQcT_pePpv9oEzxNapCSO5fy18_xa5eHFfzpTc0JU7FqJfh6V_x3IC6itHMJXA4-YGV2adKBNFm_4YzHqp0QmtmgQbe8fVlEN9jjY2aO47WkdhnSZ4sxSZ9PoqCscWAGDuoiFR0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ys6HBs24ylaQ512sf_KOmezywbrKUH321i5JMcDzA5jXIBlxz8_dt_vHOFh01ApHNrMqUwzMpE0Xxsh4LbPXD3V5tZHnSAlyglBTDX9bQ1sdDBt-YEwmINJ_e9dcsTJ9t_EyP5eDW9HYiot6FzUchSEMqWEU0S4_w0O1U9aHzI-WcYigH-mIXvIjWtg_KVYnC0EM7eEJDEEP92ueY9_OrEuknIJUvd_gfGA8clohiCnr1VbQ-oaJWiOYOi2qQivDOeGcZ0gLD9NQs06LElkhfJSR51Nm8wPfjCHvRX7BhVtH3sr7q1sz3Lu6gzczHMuXG0yVclF7BOhQ7tO-7CGx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F7YfpdEnwATTwmm6oM7soQRBoZzvH5ZXAxo-3vrJgSkT095RRaaiOHNGk9sWT8IHYrrch5nxNFQ8XThdoH5bXsQf9LeFDlq49iByazD8j832h6lJc8oxUxFffpdzT3XjCRH_narY1jpGwx3xxp5XZIAu3PCdQGb-S0kCd_6PeA5rdqFEp6W0NFGrFgzvh8urMn-W828UxTJJPrXYAeeFGRZQx6D_8XE7SIOnzfcnGHnzrXFtJE4WQj0P-SJbT8GHCXrVsjZyujAoEPP73feeblLDUy9qUBzetBtZNuCTuxndAZWjLKpwSQ6Q5ixITtrZd4Vv_tUyFSThOAIWvQOG-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkY_sBVla2fTU3b-qx_NfPhTKwLrphhC5W80debHfqrWrGXYYv9Bm8RxJ-oeSDc2FuSMoKsZ9buaQP9nGEde3QZtnifDSeM9ZmwizhaPNXYF7acK1QpRZXd7DHRA95MbMzPsmbDp4KHGuYJkvjq70oI3ZkgHTPa-zsbGUiajt09lb2PvNSmNj32pUD-ZbElH2C-8JPNYUFVhfDw9EQ8BORXhmZcIdS98_n5guN1vhcuHhi2K7B1zjq_rnmv6vzYiy6mqXP0tucYW5yJPXnz3M9_Xsa6eeof0A5c78tLu0DRNn9Lik_gvoBgI46IPhYs3PsGVtxNLgAB-7DkfRkZdaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bI03t9jXNQwWRyEMlb-0LvQd2PValgKSJBJDl6Fe4kfgHLzEaw-SO_ZUrDo7wLU9o_ueQsnC4q078g4SHYDVfj0hbkMFM2EJp78SfRY45T-peNtw3oqo6dlyg-wVMb7P8WXLYvb7YB97RRtoyLkZBl9LoYltYsRrm6m5z99atDDxYYWO-I3dXblVecCS5pJ2iNldjFiNPzGujrSojlwxKPEFOzMMlC-hiIF8IQ9PjIKrhV_RlcYZYIAaBhtboa6yqpntMZp4EKb5NSrtqyWK44lMT2Fhoyb2rHJWWwTVKunp-hsstQD6twnAVh2jqdBjElrkvdO1c1LHlicH_hbF8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=a6UQmbAg7cMoz52V7ZVcfF8anD5WsB88eAIIV9zkBEzN51mwGHaZZ88tboP7RGGmfiaZGSjcS6tgz8v2RLlWjzmNKCrPc2XT8gOc0jzbkk_39N2VTYXXjsRl63rGvpHu9GGa0Aoor9umE8fWEnWH8LyETZCTplEdKHMnpBMu6vAeUU1sYQ367ZQO-GNIJdRy4X9EOb8m8aAowd9ihDx_wc5ue6lZist2TWKQElRuJTv0KEZ04EAcIgxWkJa9IAWPePsBWsBIaD-aR4RdsC_lX_9meV84ze-yLBc-0jF2zrEMv9cTe-sjzaBQf9nrH0bDDvnYIdd0O7psiqFFexp4qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=a6UQmbAg7cMoz52V7ZVcfF8anD5WsB88eAIIV9zkBEzN51mwGHaZZ88tboP7RGGmfiaZGSjcS6tgz8v2RLlWjzmNKCrPc2XT8gOc0jzbkk_39N2VTYXXjsRl63rGvpHu9GGa0Aoor9umE8fWEnWH8LyETZCTplEdKHMnpBMu6vAeUU1sYQ367ZQO-GNIJdRy4X9EOb8m8aAowd9ihDx_wc5ue6lZist2TWKQElRuJTv0KEZ04EAcIgxWkJa9IAWPePsBWsBIaD-aR4RdsC_lX_9meV84ze-yLBc-0jF2zrEMv9cTe-sjzaBQf9nrH0bDDvnYIdd0O7psiqFFexp4qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YR82ogBOtYM9r2WwCCFjafdMmwx_aQvz5-7Mlv5Tcftj-x99M3eaW9uprQH-v0iATMjqzKebjeRlFKAk8Imez8RwG17zPHIt_iiJImHuEKf_DDDjIiA0r7WX0kqEe8aXa0Tst20vWyYvHjjGRB2SJpn1UlignQ2IjWb7-nKxBtaBnwF9vurAZIZRMBtm1bZ7XBlKUEXxpmo7Lf2xJH-QU8I_0rhjbNgWy4-B0jrF-v94fSLFins1dj1s1Fx0JxlH0ciL2fj6DKS9vBShVXpS980LtcjUUIndo2wzWFNzn8Cb-8fypFnzO66n-Fdm5UxPekejqlaKyYQfdyBxEY9I5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbRFXYVLx5N6goz9RnT2UCw3F22uNq2JkTFiOIY8177UTrjaNkxkbSXJaH9EJMps8rKhqIeuYBk56hBNVBN84KisV9cs8B4mkCXad68VayXba4iP3jZDsyURx-JydOrFHKfzuVER2D3mbUtDGcTYSs8hAKY7sQIOIfbH66hGvBITe_aP6o9PCfpjD7gJHc1c7OlZWygCM6f4qoaNLK-n7s3sPN24FQfqcgmucCmc5sUoxoFyPzAyZPrKYtmOga3yu8KwPTyeYTIhZ8d18JVIY6sw7fpWNUPAHh_-oW1lOCK5pYC9NB9-U4-N8GrrNvjFOsZ0jAflMs4PqURSF657Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydclj6tIRs9SnKQ3SnzYqDjO3A3VUzjQ-y74xscurXlRvPs4MYd2JoJ1DZ8vM_jhGOAFiS_4dPAVVYiNb7SL0yogVb1_g1nNXCRiBLnguW7Ijfb5Lxj9aZRQ1UsDyknCcM4Y2rwEsHe7Zz5dhuwRiW-0Cp8TqWkLuhsa-Vyq42Fgtxr9t-utjW6XDm5HPcbDpLIoEVa5CJwvnav4Pb9mxo3YQfh1wGp28Y5a5YtIUU7eIy-3RRYgjk7Z8jkc3rtfm5J_gcfT3QzwMYsz9tFADsDPJTxcDfms0TBAHyXXQZfKmDr6W57fADK8bt2-nFvTghGCwaVaastR-DJ5LAj1DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGlinbOG0WUI4i-cAzGC49nMJmDsHZiuf-2sQNH1T7R25khDiOsYIWjoOUb1qfgPHNQ06P0_Yr4toL9ybahwFxVsDQvjWzFNll8ZlbxGuBLoI8fy_MP_xFjjHIGjlSqfonEN1afj-zeAk7gCprU5Xqq4CciNFG5WNX-aViv7NnhTh08w2NAhLCvuBM9b1Uaczm8o-93aDLMJO-FhOAFSTcUpHQqoe6WPd4sjePE519c9bHsv8rf0VxtCP5aJ_YhX_9KvLooV45IN7MyuI034W5ydPRbi_cyQnyxnmeADON4eOeR1ZjDPs25zPuTlQOu94Y8r7v8nNcyK8TOXbXwvEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULhiwPrsZaZsTwCkArHsdc6qLIliWyCshaEbfyOfD0-G7J5rkUt5d1GO3uy19IDkDxjwZUdaW24i_FzDXpdVuAQ9T-Sbz8uKTMsPAjcwF0p1LlA1ysgx3eXEC60mHBN1JvMdeVkKfvRAXKf2RcBRKq7AdjHKbGcPoLz-jpvLcQXpdaJGgL6wg6Mvya3HDgP01cR1baCl7SY3dyKabDcMDFzRXo22Tow5M4Fo8qtKD8kOLWlIhiLlGrJhzx5_3XODmWbACtfJl7BBW-Iss7DTlOpNLswyhJVMOvved9SFSCagb2sKw20VyivNRcE28F6A1IqgHi1o_4LRDfc167HmIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saD0DKdjFspWUA3zqXQqBfF341J6bj9Pp5SjyIoJeQ4rjRSbWWiT1MRi4UhjaTmH0oC9NuiKhw6sKoKyGpZBRhEL_qsY30jKGTf8x3hBtrkn1oU59nxPvJTuJogBRW8y7nrClhIf4BnrqGjgjmqBrBKjJYv5bXq1oobI7bYf3qjCvIiJCKk3G9Vms1hl1TO7UyTz0Yy5FvV1-r_65hjETHuf2YoQYsYJH0yvOEazh6HMMJnqwQyrZS52eY0-LYwvELZj5WmX-Rh5fOtixJ_Gf1V1J-oEO9cgSbST0g5jdjUCgK2hG0MMy09GfsWiwbLu1M9CX6O375wgw3ZRU2Nn7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZ2Rrv_oo4S9qjUQLIIZrX7VnEM5j9OzDoZEUL-U99YyR-nbZjW1oPhu6bDAlIy6v9wjXYH9ObrYt6KfOkKJtHu3zZBCBwOderoeWj2ysZhQnZYjESU2qREB2copyTdFnaagoTcH4caSkBB1XRqtHY58TcBP2R3iRXHpvEw8IC0zO4yMJKIaZ6lTMwnGUD_RDRUr_r0O5nM_QrUMhlp0OOEWSi6bzuE-izs7qvugFFtXuoEvjaxnRgqyiGq6FzLdUvPUQkHU_1rdyQt7kXqA_C7bqb1fzuaWU-G7jbxpJ5KRsHTtWxuUAi5smjfA3CseORTZZGG2miRQ4n7Hlm5OrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=jFqEi6ImUWQyKRuhR82Gc4eNBGW8mmbQtCGFPCvXCkb0_y6MueQe75Pg-fq_VKRGysvSH_qKFzaXBAs63rycNKqRM8HYsZq5udJXTqrA0eLW8fAVtQiML2rHAJpBdciZBdedhNttCdTmAaJZw65iDb5nRF6hwHOyaHYfo5TXrULrHtBSUb7blg0tmkjetwZgU1k0iX6uPFfLnTV16OBeEbkWi1es9Rrpb36rHL3P5SYboNYnxtN5OYJot-IkZNUudjvMGmdeRydHJcXSzrJMmN0l0c5_BkSb9olkHW2H93p2gQ-icN-oQVifc56-YHvFT1INYp_6yEUBfUZB0e2C7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=jFqEi6ImUWQyKRuhR82Gc4eNBGW8mmbQtCGFPCvXCkb0_y6MueQe75Pg-fq_VKRGysvSH_qKFzaXBAs63rycNKqRM8HYsZq5udJXTqrA0eLW8fAVtQiML2rHAJpBdciZBdedhNttCdTmAaJZw65iDb5nRF6hwHOyaHYfo5TXrULrHtBSUb7blg0tmkjetwZgU1k0iX6uPFfLnTV16OBeEbkWi1es9Rrpb36rHL3P5SYboNYnxtN5OYJot-IkZNUudjvMGmdeRydHJcXSzrJMmN0l0c5_BkSb9olkHW2H93p2gQ-icN-oQVifc56-YHvFT1INYp_6yEUBfUZB0e2C7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYWduesbkZ7nIW4FDCU7spJ8KH9ocFS_2yGPKOZujpy1IUokdKCSagG8V4prWCkZQQCcNHQNAIB-siBEx_W8HAcjM3dCD5a5WS8o98lYGcrOOwEnOFfScGKDW2nt08brKTthlGTnF4D4dIPenT_4EzLC-pa6U7pu_fEvD_90ccfStLu9eoLaTqACXyzVLIdKCLzfpMB-vvRUYkM23-D2ynpy6wyGrVgtGm17MCZhmi5mx5Gxja-i752z_A1yu1Z1k132yTwCvRKQY1sAKYNPYWuJJJUdypBmbm69ozi6dRgsEN-kLbhWRGHI-JxC8L4QvzYPNJTOcCdR_Beog_p5PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=eR1ht9hgbqV_OI4i_hvzXVKN-sjc_7YraK11yrn4bLzrLfBWWReDbtpsd-PDTMjrpsFUAJkXH1ol5KyMCGeBM-ZGyAVfpPqqnTnobaveYCcC40lczTqR93caz_eVwmUPH-bGV9bh9Mic0631Y6D96Uy2TcHH6c_Rg3Ef1qKEuKTXc0WkhygrRKmTf8t2GN8AypJyS2Zucp6uKHyBZD4P0d2gJ6ogQxdhg38Ltoms8WBhpOjEYjeRvYf0yZH0YZjnbjNzUCTkU7f4-YfsvOlzTvG43met_hfvpENMlGYYru7sLAaYkQ4Wr7bn4KnxomAd5irDHykZZZLawZLY8dXWHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=eR1ht9hgbqV_OI4i_hvzXVKN-sjc_7YraK11yrn4bLzrLfBWWReDbtpsd-PDTMjrpsFUAJkXH1ol5KyMCGeBM-ZGyAVfpPqqnTnobaveYCcC40lczTqR93caz_eVwmUPH-bGV9bh9Mic0631Y6D96Uy2TcHH6c_Rg3Ef1qKEuKTXc0WkhygrRKmTf8t2GN8AypJyS2Zucp6uKHyBZD4P0d2gJ6ogQxdhg38Ltoms8WBhpOjEYjeRvYf0yZH0YZjnbjNzUCTkU7f4-YfsvOlzTvG43met_hfvpENMlGYYru7sLAaYkQ4Wr7bn4KnxomAd5irDHykZZZLawZLY8dXWHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZXiG0bpzalrLCTAPqJ6KiQt1wvBGpq36FjRuZ-CeVhxeSbxEvjl6nhPFxOS5G2kyNqa6wSraXOUaWonPB-vN9wnxEUIh-nVr1yufZVs_FqzSoFzOraT49v2YYj6no89FaDrJ-gboFHZ0WQsKIa3EDDJkcCK7iNkzCg2N6cJUkY0YwyALwehpoHov60OR3Xp6S-Zywm4I-DTGDhiJhGM5V6bmhPWC5LokhoEm3j7fgS33v88Ckgjto4P4hB5DE1nHLWRHExjOgq0XRT8h1rb0ET9ejODwtbBgdH6Jmv6ca3gHfm7AJzccKn6O3o5MsKMo27kOQm4Uxkbv0264QV7rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ZQeBdGDjQ87z0ySt4A3HftFVjvlka83GNhftmFowT4EF8azzt35FSPukAAeNUZq-DKtYsl6XKkAVK06pX_r9p_xNmY8kzE-4_Ozj3YAUsXeOoTO5pZ9Ge1dTO1wIOgFlugRfBsKbfUNHsx0yfAWgxePLhhjaOQTXb-8VUiRhZFoK_Solp_sHEpjU1JwnAmyHiQtru4FFADYkRmdDQ9Pa03LMLbtEKiT0H2aVTxWCVaVv75-V7IdKuDJ5vvnYtgY-7iWltEr9zA59CTbQqe3L5WRrF87Mv7hWtq703DwS5_m8zA4BQzuQcWCbSs_1Xb8iHVBWS5leNMJqLxNMBRyGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ZQeBdGDjQ87z0ySt4A3HftFVjvlka83GNhftmFowT4EF8azzt35FSPukAAeNUZq-DKtYsl6XKkAVK06pX_r9p_xNmY8kzE-4_Ozj3YAUsXeOoTO5pZ9Ge1dTO1wIOgFlugRfBsKbfUNHsx0yfAWgxePLhhjaOQTXb-8VUiRhZFoK_Solp_sHEpjU1JwnAmyHiQtru4FFADYkRmdDQ9Pa03LMLbtEKiT0H2aVTxWCVaVv75-V7IdKuDJ5vvnYtgY-7iWltEr9zA59CTbQqe3L5WRrF87Mv7hWtq703DwS5_m8zA4BQzuQcWCbSs_1Xb8iHVBWS5leNMJqLxNMBRyGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=WWdQs63Jp6bXzDTtMrzaU_ksAGbOMehrkEc5IWA5hTXlkUfEsEMpJrpqfJ1NOmrp2rHk_SxR0fRZnP_r0jVGv-XSiALlFpBLS9l86YT7HYVlkix41ghbErJQpijou8JdqRzf6RCplk8BGT4_RzIhRjKy2zbeVPKbeoCxdO8hnUUe3QsOhDE5Tj1E53uqP_1gAMxhRCajjP0EXjuQGmw1t_0I34wMnyn6-ZM0Y-Kv-IP2ExstGI41QjlRgbXEs8yQg18CJwha85onMZTcBpVOVTp6Zjh71krI_b-udK5R036U82Tqez8NGL7JmKolMUP3G1LxgOXton3eRrqRz4Qepg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=WWdQs63Jp6bXzDTtMrzaU_ksAGbOMehrkEc5IWA5hTXlkUfEsEMpJrpqfJ1NOmrp2rHk_SxR0fRZnP_r0jVGv-XSiALlFpBLS9l86YT7HYVlkix41ghbErJQpijou8JdqRzf6RCplk8BGT4_RzIhRjKy2zbeVPKbeoCxdO8hnUUe3QsOhDE5Tj1E53uqP_1gAMxhRCajjP0EXjuQGmw1t_0I34wMnyn6-ZM0Y-Kv-IP2ExstGI41QjlRgbXEs8yQg18CJwha85onMZTcBpVOVTp6Zjh71krI_b-udK5R036U82Tqez8NGL7JmKolMUP3G1LxgOXton3eRrqRz4Qepg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1f2VGWDMgX6zObX5nXxpyB4uZB0Tpvlnu3eujO6KNc_eJzOgQsfOpTgHXbWR-8ktRdvLnZ0ziXgjYxhFWAWc2IRAtvQMuRM6_8NjyQTfIcjXGaTwvFKDg9D0s8JeQ9cROBYtRqUfLCO-0s6LvjCLHvf_lqVfp1WZ7N8kjO4YJRJr5tjfy8e0iZ45GB5Cm0MHTym3GyN-Ii7xZyRmyQVbo-FuAAudRCUQJWnglo2SyFJG2lef-UW7597bv0pU67c61xGnCBzEs-F6VFuQuPwwuaQkfHBFCKb7eNwqA4J-__jvLh9URPegSng54JKRjWviz8c5vZy-N9-V8HR_iPlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=OAqSZ14uWsQDJmd_cdBmP-P4WXUXcoUiB3f7Tr4J6iCKZS9b63Zbf6EPiwVzEz7GQ--AVR_nZs2GLlJCox7QhUTtrxYKLRQa2QVo5EnlxYJyiQc9VikzcF9PUpmG10tnSU_CZwdUo1FXQmnI5QMErULN6Ny7MIQkrr03YJOWuFMQEVQg1sOXxVHCX_4FP2DPSgUTBjTHLSSWokbAVPaJBOSINuUWctxMSt-86G_1YLQv2eF4-YHms14Yvd4htu4ysTjiWPR5naR5sgIJNPOJ4LojeZKTEYloVjXFDdKAzVTYbrJWN4dBm3I4TAHxC2wU4GrFIUBOqHg4dc_4WaHnUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=OAqSZ14uWsQDJmd_cdBmP-P4WXUXcoUiB3f7Tr4J6iCKZS9b63Zbf6EPiwVzEz7GQ--AVR_nZs2GLlJCox7QhUTtrxYKLRQa2QVo5EnlxYJyiQc9VikzcF9PUpmG10tnSU_CZwdUo1FXQmnI5QMErULN6Ny7MIQkrr03YJOWuFMQEVQg1sOXxVHCX_4FP2DPSgUTBjTHLSSWokbAVPaJBOSINuUWctxMSt-86G_1YLQv2eF4-YHms14Yvd4htu4ysTjiWPR5naR5sgIJNPOJ4LojeZKTEYloVjXFDdKAzVTYbrJWN4dBm3I4TAHxC2wU4GrFIUBOqHg4dc_4WaHnUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIFUPt80cVsFjBB-m72VBzpe6BS6PZRpUi5JDuIdGkdlxfp-Zh3vkf3UAzfJpWm4W4cryNpFFzMIl5750zsEZcTL_0UT0iBbx6ScbotF-70MrDCHx5tabtymYUoa7Bp8do6wMML4nCeyH29DyS_tBKi_-sWOepRrxm-VxK6e57xvdpo-8Jo5Wg1K5wrYQcBv2lYO_efbdkDJlCU6sJ36KJLv8msQ4stKd8T-6P3R9jDxKn12fL93xHaj1s4SvJDTU7Hb_3wPJUbG0MFhtDDezE8SyIg00I8etEtiu0-RwDn8NVdWvGG7bavYX279IMr9hr-nqYIDsXTwx5Agsqc0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=k_pprqApCE0uelxab6cnA5eupNlmcWqT7L3Vbj4ySecFFsnm7x58dTOuJKq0cJ2tU6mTV53d5gj7vkh71PzNLU9jZx40RwsOOBLqE5VakRO6fX_-EloBXR2XS5ia6QSKh27vOt8R-bt0PQz0mHxlT6l5Ynl-PkqjTiduxGRRws8a7zMfWMhQMBkVm-vp6vzgz9t9uKxYYAwpK5FiYwuluoleuGMziPPsFpsDXVXiz3mQH4ZY3p3ah49wHSS7w0Fd6-MDcRj63tdJSGFvg6M5JqA-OmvDg5Y7eySFT9kFuNly_vtAPk9Qq-zfNSTEv6eueNW0BBdzRGyLUl3Mnaiifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=k_pprqApCE0uelxab6cnA5eupNlmcWqT7L3Vbj4ySecFFsnm7x58dTOuJKq0cJ2tU6mTV53d5gj7vkh71PzNLU9jZx40RwsOOBLqE5VakRO6fX_-EloBXR2XS5ia6QSKh27vOt8R-bt0PQz0mHxlT6l5Ynl-PkqjTiduxGRRws8a7zMfWMhQMBkVm-vp6vzgz9t9uKxYYAwpK5FiYwuluoleuGMziPPsFpsDXVXiz3mQH4ZY3p3ah49wHSS7w0Fd6-MDcRj63tdJSGFvg6M5JqA-OmvDg5Y7eySFT9kFuNly_vtAPk9Qq-zfNSTEv6eueNW0BBdzRGyLUl3Mnaiifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQxvhVBm_miuTiSzaoH7_roaI3FSMCpB4vay5-q9StRg5QNHdUZpqlYeUTf2RciM6TXgdtghDvDKNvDKtvEVdfEfWWHoqJ6vPuSd4YPDxqme4kQlikf3g1htpanHwwlkC28TPrH7x5BIyoNyq7GuzrBVdn0VMcbJARoeONie_zwk_xBjbaAo9i2eHAP5-ipkITNOXSxjG5bL4m918-8NgHmYQxGI-2BWgGOQT9QHNMmF4YPEM0StoRsvSkpTfU2ialFPGVoEnDiS8Y7aq7KJbBIP6ADqoL4a7o91VoQoA6SWttmJggBKI5LWhSD0UoU9v9lal3xWzZwmxfdD2Dc3WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
