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
<img src="https://cdn4.telesco.pe/file/Z78h1wQn5tDrchqtg4Yz0Bkx-wMdPgIuOTETZtTWt11oMJ0Kufl9pM7lg3uGAxuswBPeWK6vFvVNZmQQQ9V7DM2omv_27kdRwiraMHI2scF1WFLxZjakyrdxiboz5fDOlexAF7dDp_m7R0vAaIw3y_fQAJk_Hpw9SWH1p40huxq6HMBtrBmYCisBZ-II7FCBpdMnacDA3AKnt55Nubbw4QLC3FkI33fiP9raoVOVZszdC2pV1nPcYKW9DJKZERnyGG5tWyl5g-_6tdOxsD7uXfjLIf0QrDIEQWlmZEevWAQx-56cVjgymZRJELk_A3tQUJiB_NUHCHhkx_HFxUfocA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 422K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 23:52:11</div>
<hr>

<div class="tg-post" id="msg-25176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBSaCDvVU_dZ1bbQs9RPPwEQZ0vQM-TOLJH_R1hTjX2Fyeohjrfv2Cm0L1GVI6OBpGZ3CP9F021aeBDS49VT21RSWGg6zM1ky5Vs6SxNbDlWIeaLNTVST84XWaDaZPXnVgFLVqZxt4n-avolVwVhtfTgA36G-a88JBGNyCn2JBBNvgExuz8W7t390iLuklae5Dm8MfEWJ_BOM6saRqLPDRG4YrbSDUzMYjmfa4CHA1iJaJ-L2YAB4P0s8QY3LN3MLAGbwJIamgf_06Xx_NqGHZQuxztINeVkqmmp4A3-Gx2G_Jh2Uf6OrjA_hOGo44s21vrpKcarZ8BAW4cdv4ZNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#اختصاصی_پرشیانا
#فوری
؛مدیران باشگاه اتحاد کلبا رقم رضایت نامه احمد نوراللهی هافبک 33 ساله خود را 800 هزار دلار اعلام کرده است. باشگاه پرسپولیس نوراللهی رو در آب نمک قربانی قرار داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/25176" target="_blank">📅 23:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nu6nBctNXkuVfC7PRwhvv3V__Tmk51WTuWxPupeDBxAGrIRfgj0Rhn8ZUxSDu12sB4U9vdC4MkUrzzMjxtt1S8qJJ95aqsq8qisKlHMgTaQIp1m4UqhU9plt6Nu2MxVy3aSPLf2akV6ucatFW4jJS8Viudfxs29N-0jd0cwezse7r4RgxKBFLK3QSDwVX1xSRPo4grqSPLFtRrI-7uclioa8EF_JH7itOqFSShye_xQUDagqJZt1UpN5_imI_yfGTUbYY4bQ8HgMGw1t7usQZo6BRkxw5-2ns11C5r471nSbRyS-CWGQh0DH41tJEpfp4hXkcF1GG_0QXp0f3LZezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/persiana_Soccer/25175" target="_blank">📅 23:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdSogmpwQvoPWoF__nmzXljdB4AmDKV4QQg7w6Ij0Q2gv5ErTFhsbKyAsyCaACuHUw7iPQxOr-AvFI71_-elpqNDyUk_0gAUz281-VzMYm4INcSHllTXufA1jHrNvlTKmP-EJmp38wpWc3jn-N5Rj5Q_YAk7F6DmGm-VJZF9D_WBshHv0_wTs_MPt8t6CWfP2IzGAV9LqAhCzguQOlhAUkXwL3zMbQn6oZam2wT7Na2np8s9wycNIL1J-vKcQ4H5FnazwLbVWRMU5W3GKWjGPHysQdI-xseMk9qDakxqoPHcCgK36JwlfR9-LCsyTGq71Iw7AZXgUpFIvqAxwmtUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/persiana_Soccer/25174" target="_blank">📅 23:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vXoACGSJ4KA2dHO3RvYT-LdbKJiPfZbvAgBpir1Fa1ObuTtVRtMorRwJh1Gdgfr-jRQfm0jsOivDSI_aKGvTqGlvX0dvJ5hIqZ09c79BxA1VHZ4G6OapT9dutu3l1R_Nel1uK1DsVxPhj5c9DCguCKQiZgqi-3Eqb1pEh9-nQsXKAl1ABcYeB_nX8jdQEMkGWRrSssTGBij4-3lSfxYCOjGMIPZry0cITmk2fbqGtftKA_wIAsgWfI4a6EjBIIYpV12ih-crZF-krSaeuMpn46ulhnjw7vpNqJ8mgpxSYv2r8hf6wgJE5yQngYzMbSFFBibIPY2iSsWwUyKmrWOlfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/25173" target="_blank">📅 22:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nl5Bc0tUmuT-_bLjOpNx7rscgVe-ubT1-pEwVMIdfk5KAMz34fmXJVk5OdX1y3eXK_MsVJVkxjWM-npvD3kahWkIt6w7HUx2PfO6GHJ32Aq2d3daiS2znH-LNgzY347QO1hmhw1zw0PdEFU1IVWltOZ0W700jKf5U6QO0U1hLR8m2U5g_AL4uPAp9nC0UH2jcaM2LFvgXPfmDKa11hYk_3pJN3iUsl5w9cGSYabKoOJRVB1mvDfTfKvPtijnwzBMsCtm2LL4ajzAhitoXg8xZ37k3UPETlesrkYgCvfx3FJ_6RwdaWgIOskzhoXDfC7bWW_9iM-JHyQUr8mqZeYPmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده جذاب و دیدنی امشب دو تیم آرژانتین
🆚
مصر در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/25172" target="_blank">📅 22:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی 2026؛ کامبک جنون آمیز و برگ ریزون یاران لئو مسی به جام در تنها 14 دقیقه؛ یاران محمد صلاح بازی دو بر صفر برده رو سه بر دو به یاران لیونل مسی واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/25171" target="_blank">📅 21:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl2qsNJMBs8emrfkYcGMhJ9wrHiqMbZx3icni5rp3jNyGpQ5hH6kAIffqwGfv28Y2gjWrwxwHUzUbvSt5iJdg8_w0zAAV29Dnd5Wg-d0cByGTNocieR8zHntDksgf-t1mdbKbrbIYV8qqYhaNthKaVXeP3vgdZOoNflJ2jtRCcEOB-GIEYL90vucCLvflcWYdHEEKyxvmcbrueInzzlFra_5W_6v-iKhojGpXH1H7hbuU_IQVjqXwE6I1KWZxfAmeu-sPQOsf6FEXhadp8y16FeuU0ZzVSnMWN0gHEKy5phXctzZGzYwAOuKFU1zVIucty2mzaa6GMqUc_rmx71G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛ لیونل مسی که نیمه اول یک پنالتی خراب کرده بود در دقیقه 80 با یک سانتر دیدنی برای رومرو گل اول آرژانتین رو وارد دروازه مصر کرد. این دهمین پاس گل لئو مسی در تاریخ جام جهانی بود. لیونل مسی در دقیقه 83 گل دوم آرژانتین رو به ثمر رساند و بازی دو بر دو…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25170" target="_blank">📅 21:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0uMJDpNcrN5UrvSH0vtkH56DQgz8woy06T0b0S6aR4tyMJV6SX2p_lfSGKTt3KHK9rw4PA9DiS7XXb3ucQDP5ss7I6HiECuz0Rar-S0dkdMU-vezyUei29eCh-V6pcb1hFfPtnpveJ4trm952Cs0ABwPVgBdTXLGbb4xb09cQzVDi9_kv6XpFVjJyBufkGBzgh13g0qxRw8-_52ToVx6_G3lt1DtVPefRSa02hN6kubA2aAoLsyYeotfZB45oUP24xznDYwDrFZ39rYiqFotDnEUWSGZI1hxtl8P5UaIkF5VHt4eCdgBgR-QiSX9mRunddpU_EYRBuAD0-hz17WMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
با پاس گلی که در بازی مقابل کیپ ورد داد؛ حالا لیونل مسی با 9 پاس گل عنوان بهترین پاسور تاریخ رقابت‌های جام جهانی رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/25169" target="_blank">📅 21:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZGZ64jq6wTdRMfItnMveCJO0vhXo-n1FqBteDytEKd9R0cRJL_0V90h3sqNv1CWdHl6c6vOQ48sghVe7_2tuITDvkmoMMjxMIvctHLqhwwFSIVCntQVBXfso3cQSKRQumF7f-iZ6jyDAzb8rsh3qOtuI4SytIx3MG7ggLI3H42UZ_JgODgbUyxYFueC8rJ_yariBWMv1N6-xxrAIGvyYzRIZNRaR3ds1dGmft9HLCCMdUkCvMjAI_Us1rekNuXs-u7VFUqsuwE-uNXTwY4ToyWt4uD4vUlCZVtu7NVJCfHXqPiyTqFHnBrtmPMJvb2O9sNg2_4L-4vYKrb9dCQP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ لیونل مسی که درتاریخ جام جهانی 8 پنالتی زده که 4 تاش رو خراب کرده. مسی به اولین بازیکن تاریخ‌تبدیل‌شد که دریک دوره جام جهانی دو ضربه پنالتی در جریان دو مسابقه از دست میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/25168" target="_blank">📅 21:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EevuH8qBf3x2t_6cCO5UJ5AgG2CtfBzYhNfRuvteBF7b2Bv5QMik29hYBA_AfI83-RA8nNmBlxc1iookMdgfHFTR9EOIVG9r1skijaLRyxiDXbkm0Pw3yT_0g-cf7tmsO-SP9HN8KnTcKme9aR1IKQPQ6rdqRSqYBCI2aYOIy1e_o8zKcpYOAqU18lRqXPqrLPmlnSS8FpuYjEtNOwxbwLgY2o-QyBGxEBS8lKPYkmw523lMywQicJuMhP0jSVProFzAhYn42aeIF58TnBQw0Lu7IiBBcVTRF-Qgd1yLlyB0JTXY0QKF5hclqI-tkBT7NyVOX-wFberEX6JSjorZOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی‌تیم استقلال: از لیگ‌ستاگان‌قطر دو پیشنهاد مالی بسیار بالا داشتم اما بخاطرعلاقه‌ام به‌استقلال و هواداران این تیم آن‌هارو رد کردم و فصل بعد نیز در استقلال خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/25167" target="_blank">📅 20:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25166">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQ7TlaiiKyG2ckC_ZgcD4Aek-109X4wCBjEJEF9O7rAx3omoYxAnfBhcNBzjVhtH-NEbeCVSkGqWK2X9dbc6a29riYqe0-WLSfGbBSjf4IXoIS1wwVwvtmJP-yYiKGWzdPCAxGj-vnwoV1uiqsBf7jmirvkVCpBGAU4xS8NnKqWZHdr9Wb0_Pp-Y4uRwWiOWT2iqfYXMmd56wW-ez8FRPDNeUN4KsIQtXdoxEhN9a7S2vN2FL2-jG62K_Qj0UaFSWTYNItzTDlBxpnV9P6nm7k5CTxf9RRPzrmiZxz3jdhqswmya96Y2GIL0HYaAU9bpI-S99MYY877wNz0nrSQytQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیگرسریال‌تاریخی «یوسف پیامبر» درگذشت؛
حمیدرضا دشتی، بازیگر نقش «بینگی کاهن معبد» در سریال «یوسف پیامبر» بر اثر ایست قلبی درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/25166" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25165">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rB-y4QwN3W3inBpLygUDncdWTiZNk-Fst2AHCE6rUdOsQi5iWOV9xwuUOG8IUxylolOAjOCA3wbqgCH7j1QtCD5PR8jduoVhyrJz1YKPiGiqr1fUU-MzIZRWwT17bLdtCX9a6_zh93MyNUUEb1EppAZr2J_zVfFf_1c0bEBK8H-rVKLJ_URK2eiZ6FPFegUdRjUDyVcC25rMQ7up5zgwmlDcm5Xzch440oaEq91fjNexs75BO_I7bTUR4Y4gXkANolvRGN40-VpbiwYWO4bWLk4FKbqHwvtEsfV0hgtqe19rqqBcIW-jJKGh9LdN0QIAOREIodAMhIvPsmOsog3Trg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/25165" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25164">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/089d3fa449.mp4?token=ptPfkLacwm7d2GTV_2f43gGNfSGj00mZ-01XiVKoHjvlKwu8IDkDmHIch_FkY2HjxF-KWaPDoa4SrYETLHe2vn7Tj34opuwCMp5om-2DNM6Wp-P0SHMy1NyfFKHh2_be0g5TZ_bFUBQsRGiFuGhdfS0wz6wxNV2q4kag2U5pJsEJTLiR4PwNTbY_vWHz5o7Wbk383X9NVBFMGd4g_6Mrqxgi7Oq_ehqtTlchyVWjwf1W9maBQhYllslOLExB_qYXMOKwXAin7P0cG6L2VsByj2a2OztYroQPMuKvW5iAEqVyxHDjPwTCphwyUnA3uOuv4yveeVw-M9VnxxrWHIfF4Ev-k_8vbU7LiKp9wr_8ebitIdfU6I_deA4o-Z6VKac5Smdeqk__VfImGD7Xd0y9jdE5deLfA67tBR2IdzFDBNlFIBksvj3PoCPeYKgnhNW7wRyjzv6sHNbJLNOJxxbSmgoVBy0QApZOWl1GyuK5ZViVy2VQt6TV5826duNZLjONQPRTwvu3-jYg4y_2TVeQjZss8YF26nLCoAq3OGWn_kRnGVnc1WWOvYvWeUtnHddWU_r0cjKnaB53DeV9_1KfLZSSZYqWwSl2DYWBc9Ih2ewRvP5KmVABgR6viR7G3MzltYWLbbvqxCwjqwNRsk7f41sKGBS9H_95XNTZiVhsT3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
پنالتی از دست‌رفته لیونل مسی در نیمه اول دیدار امشب دو تیم آرژانتین
🆚
مصر در جام جهانی و واکنش برگ ریزون اسپید یوتیوبر رونالدو فن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/25164" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25163">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyDeGUTAgeSvXlsqqP1762C7XozoPjbg79NUcS9eAzdgBehXp27BAxNlZ07ha_J_o0ToooSvGrmp6f4_v8FmkkXo6YcWoIGHoA0EfpwP7eq_dvEC-WJ9S6XtHV50FbBv-LKc1fF5b2heiSgu8xitZ4rmsgyK1ku8XPAR4bkReEIn84TPGbWjhZPpvx-Q3hYn_lMRp2lWEkJwZ-OYnWgqDnXCaz-dz_hgpLVnxn6qf0_Baethe3jcwDEDrZ34vlQXj_0DBM5D6ifb-UzRGt5YedV7Fr_Qj5l50By57SD0nF0BseSbhE_at0RkXQtZLDISFitTqmYBzdD4mAjn5IMCfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/25163" target="_blank">📅 19:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25162">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnBMyirs-eJR9rAec7KbmUtMjj5t-4TaXBGecmAd8S3aQdYENueQuTNF-TENTrsDoSnoKpMohFdmGL227Naf4zFHDrPtoPD4ckKaXueSINVl41EO_d0QTSwPz1mccI4YE_OTjHYHVxa-nvmz-yv3uBejeks5mEKKdj1osrp8vtgYNtmwhSnGQubBdLcFfgAgXBVPN3nXmOcH4_oQlxynbGSPJJOK7gzQryGv2OOzjlTb8AdV9a8NFsOB3lfUL8jB27-JPKZk6xhzDSufOjuvYIG12FZXzS54XA5K00bns_h3cJhhNx0NQ84nntwZ-M8FS5crw3LLRxKPJFtH_ukCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
مدیرعامل‌‌تیم‌ نساجی: برای‌جذب دانیال ایری از سپاهان، استقلال و پرسپولیس آفر بدستمون‌ رسیده اماتا این لحظه باهیچ باشگاهی به توافق نرسیده‌ایم. رقم دقیق رضایت نامه دانیال ایری رو به باشگاه‌های خواهان این بازیکن گفته‌ایم و هر باشگاهی اون مبلغ رو پرداخت‌ کنه…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/25162" target="_blank">📅 19:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25161">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rl8xIxNC0Lkx4rcE6oSu-QJ5LLI_AfT3qYmfX3ek38cRjmw7rZGmPdSSrF4w7XTASGnjPXtoWA0oYaUjrZ3FyfIGKHQGSZkxUHoDTZpkRIpGfFDR_gM5ABo3U0x6P4EXHNPENAxPl5jksZz3V_C2aJEoat2LgaOdzbc0Tl9opMK5no7zS-32dSBY_eG_tY_jeqxrTk6Rev345FHxJfA0GgI4wxBv5iBL6fGsRHq86Rsj5xcuRZ50olCQ6LywRvh6R5rIz24RdF5V3YHNlRGQIPfPIAQQSi8WR2chVxfWXRTSRsHPkshaebTg79rgyqH6QQJ9IerTe7EV7RWsXUq5gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25161" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25160">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2d97c61ff.mp4?token=ZGtWPrTp5-YeGhmEpFGUzXyAmIJQ8uOLtnmkhV3bOsishEPP_95Cr8gatcZTk-OUJA_wjc733EBkGlLMuAY8C6MWgbZXRLcF5_tUXKLQkMzxdIzt2rszii2VgiERqXm6UPuwkxTwcx97jsKvErp3UcfPtZAoQ2FtW9UC9pmXknBw4zE6m_cAX-8mPH2AxOTF1GZV3wziPvDRxcD8bu8Un8qzwJw8SzS-gXH-oDIJmedui-CEAHWPBKsUtNw_zRwZgsF85hMMR50nH6nwLF8s6MwqjyJV5pnzDyDgrNVWgpmbT_sUdD-1DYi2ry4r7GI-DoQGg1kuNgq0i-UrECiP6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25160" target="_blank">📅 18:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25159">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99da3bbab0.mp4?token=nfPYHGEsIPDbY0yDhY6aWozDhoCkUHzmkDtWEGabCrO0OMQI1tHxaUM2DAu4UOSTSkze4jk8o0yhVzcvR2XHrDBGdodhv-u0yRc1ld0VUO0EtTMOC0de9aisMp7nxDERwq-oaVB7dU9LYnWtM6ua8pMaL3_n6jgjODkCCKwrys2bBx0x3YK4FngCdsrPX7d73MXM__AfXUP3zLl0AApWCjpAwyNwDLRBS-I0L3Va3Cm60iNJbIndadFBFzXGV51JqPz-GNwUxD5-IBEOrA8cc8V0D_AhPtbQWpmBvpPbze7Uhru3lch9L49jgFwoWQ-IAJDo26kH5IFZQrOCZrpZmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت‌شب‌گذشته فن‌های کریس رونالدو بعد از شکست تلخ مقابل تیم ملی اسپانیا در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25159" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25157">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5loZ70G-xM_A9SqhA2H1OeTDXJBMSDTuKZzd6kI4uQC_PHEu5FT8mVQJADKRFbimzfWn5oVCDCxQhSfpdIkrJKKXyT_UoXKQr_G7ajth424F2kVKm62wde5ruO1DsMiHKRvNWGPOq9g7ENCsaVcYv7inL50G5a40L95k80nRm5lJswdyzRqkePuXgMyXLydz5wO5hHzSwYn9E0PQPR34Rdu-TllFUxOfGxj8_IdMDBbT0v6w46mwyNPr0AD1nygJQn30iNNrZaDDtUc6-bPlmdxoHedgZyOgbkLPFIpIw7_I1OWosYkAsT0FBwit8Ah_c5SNpzbrZr7VD9ikO6V1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ci2eRtTDgwz7OeCC45fuXPSNc99vpNUQXfUSivEYHMENorscxIGw5ya3YY_xEBQQSQQoI_22_mRKq3OSozJWJCPIj3jzOM4d5o-GA7gTFFv5WOmmleFWOYREHjBEp2_sE1w98EGfhXU8_gh7oypDq8wG58GA_PkjUDEc4VxtKYJM9QtDlrStu7Xs1wcxLgfp6ralCGlv6x8-Kayp3s5PipZHBq3EpIHTKhpmOYZz4kid-QtsYaIFfxndkkc89hgtqgMUZPCgmbOT6fsTPxrscfA3z-MenCAJbUQyXZrPcBaQ1ALplBS30yQyLjWfuna_3y8RlYnL5QFHOUJwLDeifA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نتایج کامل دیدارهای مرحله ⅛ نهایی+برنامه دو دیدار باقی‌مونده این مرحله از رقابت‌های‌جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/25157" target="_blank">📅 18:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25156">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWMJjmWZ81wNp4-z16n86RmAfbDKMsVTlIpJg3nGKmZWzniW6noasm9cblYDdjfe8CWkWSX6fgGM2gZCCBhaPWRF1ZPV3olnyYQ5OJOX0zRi0z8I_M9S_LhqFApNtZV1IYUx4GKUNsqNChhgVEnMVImMryw-olRX8UbwNIq7Ppzz723ZjiLa25COi85YAhM88vG_x8QngDu4rOrhjk-WKB-Er6SwLad5fCpFOpYk9Kre5f3hIF8_PabxLfSq0Mg9BdHR4qCNDxnD7LRcAWe9490h8Zsf2_6nC6q1f_GrEm2l3FxNH4sJQWxP7-zTXM5cMhkZH-By9gLssSOOVoNVfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25156" target="_blank">📅 18:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25155">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6llFZw3zUjIeNr8UWLqwyOF2pFtxvWq6aFhfaatReuGhMOrA1kRwdsDv5YC1b_iPc4eJy5rEu4vdqJt9vGwfCl8od4zJL1OlK53_1sDPFPd3CliR7l28sPIe3IBYR9_6K7R-e7Vdk2ka71GVLpejMLJFk2B6XG0rW1Tymht7bN8XY-vWEbAR2PXZ0bWmIx6e52MB0h05BBofSNF3Vs_68YNa7NZ4Y4t0p6YQhqVv34sY1DFsFE2Jwd3B16psYTvYHktlN9LPLPKr3fV9vGNkFFR1910NxJhdJ9oYV6S_Lt20xswAj7ZIS8h2UtN95wlaz0M1Zrt7VqOQAmwra4o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
👤
#اختصاصی_پرشیانا #فوری؛ طبق جدیدترین‌اخباردریافتی‌رسانه پرشیانا ساکر؛ محمد قربانی ستاره23ساله‌الوحده امارات ازطریق نزدیکان خود درباشگاه پرسپولیس اعلام‌کرده درصورتیکه این باشگاه بتواند بر سر رقم رضایت نامه با اماراتی‌ها به توافق برسد حاضر است به این تیم…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25155" target="_blank">📅 17:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25154">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVINSLVCnHlNkyS10b-Dyax2lbwdmq1uZIu4bXFJsY4lx45lk2tck7HGjQHwY-5j1D4Ka5gaSzKE-veizqLPtWKFewo26JASwzkBX1gBQ21xeXq5SjLssFka1Suld38gwTUJasq4H0yYN4UMqrNQHBncuTRmmOo2QEZMjjAHHyeRHJ28v3jlaTyWH4k6qdBVedgej3yGd7pn4yzwyFZHSoKFzMHx2c_m2l7J564V_fuMWszyDLebZnKH974mI08idhnN2CG18ukCWdqvJ9iJDNy3QiQc9u5b-JYqNLngAdhLM2slgwBjOZ7gbdQCZZ8l8-ZG7pUYWf8NIQA-_By9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25154" target="_blank">📅 17:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25153">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fem9yK052MkTHKyfxCwtbng8brItZgt7KxhYe-J3TV68wE6D9Izjuy9zFUsl-N8fs2-E5f5V398LVrPdtcRMqrUCgC1haLHGv5jmOUy6EwbnQB_SaTakG9tPbaklxe05EZifo1mtBhB1supsaK3Fe3Pk9HXRO2hIuxGSeq4jMBwTIIQfs8iqOF4IQFO_eDOBmu0IFiof7p6orUvT4pef0vWNZbd2sQCycpNGgwdezZKwq8V9etwDBpwFFcC9hU1dhskLwIFB2zP0OYQVtQi3hxVO8oZDD3Jqm5ZOzVrwRbhd4DWBHkzRoViHOwNKjsSakD0_8FUovC3a6Y0z-qnDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25153" target="_blank">📅 17:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25152">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Njp67P2i1Jrf2p0c7Yx-CmGlkVprkbPe9WsALC8-rtL0Jy4JBxU34pwdTX3GOV_Maphg29_i8-hcWuqpWBsEbudwr5sq2msu_A7v3GTB1IedvOIlppEPto_jbaqPwwFzT3vUNzmLv98CEeEiDlTPCwSKYu7tImRC1br5bk16jB-LXi5w6cGvKRgffE7XBpGyKAj-e_3_pWVtAVvTFmx3utd7zLTKc-7wyME5gMJdvxWY5xUfXDCQKffWt38pSKx7h38PgoacOapFuUEMjZjfgUA9gowjhgDw93YFUFRnU69AKwSnspnS67vk6dsj1odnnP7p4ikRwNjEcdXwOp9LDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛ امیررضا رفیعی سنگربان24ساله‌پرسپولیس مذاکرات‌خود را با باشگاه تراکتور آغاز کرده تا درصورت توافق‌نهایی بین طرفین با عقد قراردادی سه ساله راهی این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25152" target="_blank">📅 17:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25151">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1npkiGSwXr6iELeGPdK4EnxhE5-o6FvfpDHVmyNd-ArSsox8WYlzT7UNLhwSm4N_n-znKQs7AtgNgWK089VyF0SLuyD1BhTp6a0DfZxsmQEkbYeMShbT63YeFjqcBsOsIKqfN5AAnXEqamcWPuuuqk5HbBJ4JfNmWIONQls-prN_zuHxuVzqkwqPJCSgbpTA_uRIEynl57yxFyyZwtMd0_W2pHHkSpsEGr-DwkkwIFe7nt9HKGdTu4WhQpXE9HIKGDr6bCSvaD-3Y3NXJ_KvnHpmCW33X7Jy-nSAyJtLWHe-SE4y8ttfSlC73PVz6pmYQEEKHDQBq5QP6p4zLbvJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
#تکمیلی؛باشگاه‌پرسپولیس قصد داره که یه بار دیگه برای‌جذب محمد قربانی یا احمد نوراللهی تلاش خود را بکنه و به زودی با ارسال نامه‌ای رسمی به باشگاه الوحده‌امارات و اتحادکلبا خواستار شرایط جذب این دوستاره ایرانی این دو باشگاه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25151" target="_blank">📅 16:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25150">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBlhzS0cH6rbQqheMfPe1L9y1ledzOa1Y_8L25ndGAv_QH98F3_xknOgcJmLGsVCXTg4hA6oACO-TL6Nm3_2GM5A9bzXyA3Z2GhAO03yQLw-bQ-g9g8xCd5yp_PHYK_Z4OQsFp0SkbHic4mFb-Kc-FsGz8Xm5ZwUuNw8X0qZUOW3eLKnK3kmRaIUdZdV2K9HzjR6tXhooDE1ZLZqaHl1ImAoQv144tsIkFIbsJ1oz61VYpYQxAaDzfrHxWQOWDA-JVmsK1GrqX-mEsKcuKt0cj8njWZAUDbZ3qaS17NKsIJKDQXlD-eh3DLMUvaz5g-wrDXJw4nEWPFFOKrvs5GhxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
همانطور که دقایقی قبل در کانال دوم پرشیانا هم گفتیم؛ مدیربرنامه‌های ابوالفضل جلالی شب گذشته مذاکرات‌مثبتی رو با پیمان حدادی برای انتقال ابوالفضل جلالی به جمع سرخپوشان پایتخت انجام داده اما به عقدقرارداد منجر نشده است.
🔴
نکته‌مهم‌اینجاس؛ حدادی به‌ایجنت…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25150" target="_blank">📅 16:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25149">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKc5rp0BkK_8C8de44PzHxdDTfV5PQXzyFdWY7NuSiKs5mhmCcQyv0EVEH4_iM0t8Qjh04S1slMMVxw6Xvs-Rx4mYZpDycGOni7S4X8yTeb9JQALVxgUSYJxPcj8Hj6tI2JC7lHK-yMz3IjPHr_sjOIq84DrPt6tl8Ipteqzb5mLNBby_SPajr-i_LbHW7xC1k3DLZJuxCWWXuJ-ba286Y-oAbGHbuxEuQScmYxAtUc_TSmUeCbiNEzFML2pfseC0qLe-deJ0RAPjYGo9TQJBozSNrljd3zl4w7ipGOB03EDSd_OYNzWAyZEQqQzahUGkhwEOp4KM3RWVfeh5F5C1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
امیرهوشنگ‌سعادتی ایجنت ابوالفضل جلالی با باشگاه پرسپولیس مذاکرات‌مثبتی داشته و احتمال اینکه ابوالفضل‌جلالی‌مدافع چپ 28 ساله استقلال با عقد قراردادی سه ساله به پرسپولیس بپیونده زیاده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25149" target="_blank">📅 16:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25148">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLKs_hA9V_72NYVe2r5_Fb71cNMTWa4-SKuqfxOgsYDQB8v645g2KnTpsjBCfxGu3PeFqvz2q9ONJvsvEIYvftKH5_6vhRjIOAI7zpkjpCDx4DVMKeAAQdAIlCzqfCW9mFRYS6D7sfRLYFRj4m21zNDPuo7nbcMnuBJ3rOFBjD_sAsEjybFsd__GT4pnZCcCw3UgH8dEQyj22CkmlZlERxbzK0bewYLfEp7R4tJs-L-qGp4bD9g5JtHv-5w887T5QyfoXZCF2ZD7yZy-v7hY6opw8ozsfgkkFr8w0jQqQ0C1lmGJbe0a5DbjZw8ZCOreRHtr4_fXUmo4yQDnoNkSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ستاره الجزایری فصل قبل تیم بانوان الاهلی عربستان که بهترین‌بازیکن این تیم شناخته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25148" target="_blank">📅 16:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25147">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYjQaExiMouKcnC-zEKvFnUGSGF5VAsdq65j6Mri0nznG2YB_QbrXer39atmlM0pZ3nMCrSs_8sKV-OuqT2j_RKFbesssJhCyJlptaV5rMrJZZDhar_cy3gsTysxOa0Qe5i2uEFM1FWpRwgkvEVIrGh_cbe0-3hLonHQXfSJCSHonWe6ehW3XtE0g_zEmNTxkWdZRlMVlhVVapBwXGh-KQKZm0wkbxsDvvyrFqTY0sEb3zJDKPN8nzQy24IPBI734QSMPh-rH-lpkVSgbWwm3kcya1YeFuQmxh9CgRm9VVKUOK0j3DXFMS5QZCZDlKGkwSemW2xq1yoCZedrln4BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25147" target="_blank">📅 16:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25145">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brntzDjJyZJtRxCaps1eEQQNMKZkoF1COAwJAPR9e6a6DDFwqVsuQjJlAhO-KoomFYHuglqw-UVXzSqQ6s5qAbp8ci_S1hv1HB6h1qyw1yJ_n0SSyXIXmmovjKicWi00-pZA79_W_XN3zj7usnth11xn3m3EaQ8LdNuzUGUaJxvkwEJCGkPGjwSHIPjlnCiwZ_jvq1F8QWi6sWDLDmjKHwlqIeqiO4vIu8A7e4f_ztKlLTpqeifufFrgDqpBqWxCCewuYZsxP3Gcev1N0XbIXLlthcjSuG9ByrU-RJZ5b5xyEBFbtNN9f4JcbpgfngEarl1r9axiDwXFIimQZPKgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جعفر سلمانی مدافع‌سابق‌باشگاه استقلال با عقد قراردادی دو ساله به ارزش 300 هزار دلار به الطلبه عراق پیوست و شاگرد علیرضا منصوریان شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/25145" target="_blank">📅 15:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25144">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-e9OI2ijtG98DnQsISW7pJUyK42OET3zOJn_RuQ9zhoVvIPzYpfUMX2RjGe1m8ZlZMati7khMc0bhLPgafF0vsD4iSDrgINU33mOYGHezlOZorb6obsiqm9Y_VoCQA2JIJ1oyOHM06oqRu_3_fLsuDKZnAaYtcMBysThqK5J6-rKIX0EP3KTzrw_FnZS2EYCgP1-75Tdbk9Pvje74-G6rHk9tv3y6D9_xAuvRdK-k5yg1QRt-mxXAsH8q5rOpcvZ6BlEWBi030wuWPbZtduyX4mrMjFxPGTqlb-Z19Dl78mGPQRhLAVHOaJZUaEei0OlHhGixtvq1qt18RR5KjVTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25144" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25143">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cImh8t_lHvrLUM9eZ6ofg9jbKCacP1-wsx60u9T2mOXh5GZvi7FR_omKAtQhz_ahuWPhyk6F7-AOfWGR6Z6AEdVOfgFB0rlubzMN6IZl0_WtrutyDwTfnvaHKZyZebV2Ep9RWIwvLAL0d2dxv7Qpk2U4iHyTeX75WXKtuDI4hctlPXm0GDQ5O8AOo4T2uuImCHy8zebKkpOUN35ChjyOKTcpUOmxCv5BYGMIxjOKkz7PB1ZCVeTf73UzEg8MpdCv6dglgBcKwSo7TguNAcYySdt0u_P2yF-IA_IxoWlNtuUHwbwAsFO3R5sVEnUEXR_2UeF0_XPWBxYQ0Jmbh-hmVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
پوریا شهرآبادی مهاجم جوان‌گلگهر که مدنظر باشگاه استقلال بود و حتی‌‌مذاکراتی با مدیران گلگهر برسر این‌انتقال انجام‌شد حالا مهدی تارتار با او تماس گرفته و ازش خواسته که قید حضور در استقلال رو بزنه و به پرسپولیس بیاد. شهر آبادی بزودی تصمیم نهایی خود را در این…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25143" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25142">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpbdcKr8hrmbnHmU2wC-xL4gVBh0GAiGv3tfxYJRfl6brH49ZEQYHAi47f2RQjUycOSLBkjXKlUJyUtPsP0GC4DVc9-UNjSyig3j6FPU5paz4WiyxXLYaSuhmU7o06UXojxUwI5yXEMvLb84K1XpivyyF-lsvacVLyNZnqNsM2B2soe_BJDbgvHr8Yx0Dj9tCTZUG9oYtwb6ksaTLT17GbO7OwOkdmmgiNSuZjEehECW3ToNVmMHhidsDSRR3Dcoal9EmAXujUBJzziyweri-apAQBAMaGSBFfyjS_RZHYFs7yQSW1fWyX-brqMtr4GMMBw6bOmXjEggCWCO-uaDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25142" target="_blank">📅 15:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25141">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AB-BnIn-s_1xGzAw7eo9i0gJuwasEBi41ksakUHutfce-LDTogvcSI-O0k_tSoPUWUeIDS8qadQaBPxLkn5jwejy_7xWPiyEdldpt5Xk2IXYiJUMtf11BqKsT_chGdH8m8BqsCgONReWI3QLh_6_SfFN8wv3OIRDnmMsUYfx7VdzARJ9qkW5HYCsgl7hexR-F2PjrSqEuo3I9TtxlWfV_q-peT7clLhJhuzlyRVKKE0HDs5Crgk0aSOArKK9E8dYt_Y7EsgS-3LwaMA4u6YXujQHE7mO282bNDz2VSLGPQivCiwV5SLGN0JkyvXIIaX1gRCT8IfCCZUP0pYj_2hQLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
قضاوت‌های‌علیرضافغانی در جام جهانی؛ دیدار شب گذشته تیم‌های‌ملی مکزیک و انگلیس در مرحله ⅛ نهایی رقابت‌های جام جهانی ۲۰۲۶، نهمین قضاوت علیرضا فغانی در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/25141" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25139">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMmQ5Pt7n50ot5VPe6Fj5Pqtx6J3l11F20JO-Yp7tsTXVeBk-1MWSbnURuFgO8hryEZ82jESSaAtgl_uw9y9a3TuRNh68yhI15YlbzcTzuYb4NsyMB7vPFD0RB_fGjFc6WAjoiKElL_41MZR7dfsd3pL6gNao6e_j9iCIAwGr-o8QJeXjQ0ZzfxNet8hKvVx3Guu6Lax-w9KLOwoomm55hEg8i6CkCqg7cmmJVBR70mOw5sM3Y5SZPvYiTXX6_FB3v6LLcDsEqLNl7bWpL1fIqoK2cc9V2vKI4OLvYLPAjHnVwtjgWNPo9ZAs-Yn9zXeI0kWmJhLy6-AG41oid-kPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DuPOsPr-8uD22nCqOkUobfGA1Vz12wbuMj6mItTU5ykRJ1EIwhS_ma88KQtF-I5p0Pay9bdy-nz2uz4-J7ocmWxrPDftmz-H66p3zdanZ2B4KrBAwaGemHJQjguLdOP9sTAeU6tiBb5ch1GOLc9M_kay3RIT9kVKFpmTsrhpmDRQiKqXmIhKrfetLU0kv9a5yi_Gmk6aXYt3wkVuGzPdjx0K2zlpeBmi3sQdKdWdgooE5ZAfJRcoW3wIAb_ilTeLe90b0E_OQnDuci37vjXgFvq8Ahi1zWwimnboH4jNXIUuCcUhQr6eBojoyEWXKltxT_59JRjZHeS94PR2KCXhbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
تمجید کاربران خارجی از علیرضا فغانی: او لیاقت سوت زدن فینال جام جهانی را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25139" target="_blank">📅 15:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25138">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EW8W9j8fZftw98ZuFRdkq4Jnbk72bPxNEnokVqE8b9-QIMfD0dkECQak5kx-LW4ERVQ4wEc8iGjPiXAYcNn6NuC0g4m92c7qbKryHD9PliobzvpO1Sf6qki0JmbjPJue4SkEuJyRkX95HJYJPnIJw9dQlrAyCLa5sjyPTHxNZMHNnmTF5nZIQjOv2-8RZq5CN5xwiwh5Ez3tc_xJmGN3gK4kfsGM7vBbAA7CKDP5dWz3YX1gOIVcxzFnA1bdCC4lTv8z5DDV0Tqle4CL4i0v9oLpwzXwy_m2LS-ZsQd7WFrZK_JCXr-lw_3YHvBPnjy6jOX_OowUJS38f1oRYOigaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا؛ یه‌خبرمهمی که باید بهتون بگم اینه؛ تمام بازیکنان خارجی حاضر در لیگ برتر که حمید مریخ مدیربرنامه آن‌هاست قبل از عقد قرارداد باباشگاه‌های‌مدنظرتمام شرایط‌فعلی ایران رو براشون توضیخ داده و حتی‌اگه‌یه‌درصدهم جنگ بشه بازیکنانی که با حمید کار…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25138" target="_blank">📅 14:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25136">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSVFu6PpaLdg5UIKWVtja2dVpGFCNPo31-7sq8pS4rkPMQu792-rqVSk3n7Gb-KeVLwcHJn4iA8lbbbHVNmdCluO3Vaiqx-BAuy8uL_LyAVWUdKesf6_K2iRd89PSYi1jZOGlggEt1JMLu8idjh-P2Fg3z8bxmLbGOBqppXk3pGZ1chpYIjK8fD9kSgIxtGMK_cbpWt7Db583HNQKYMXxWiJhmio8hTQ_bEIRCrECfKqZ9TtSHh_DhkYfxzXp66qJyqwc4hH5rjSFOQOKfr81lAfTRsi_632YypbZDqHcEpMtkgRgVZsIBHEmJzPSA0nW9NOEeSpCGgwtN2_fKz4Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=L2OiSRv3xEEcFoIuvAIMepTcFPg48Hvj9uG-PaJC701iAHpWVdpQwQJoX6pPr_74F9JVR4MgiHKodw8A_WngjwY78jsxAjFwSS0ll3DZQQqBWfr7iOjhXcSO1jS1xD9fOY1-asHjeZ7FoTs4eF1L5mqPU6unoVuz-7g3Io4PkWwPjmUyroqmSc6xD0ldbVYg_w1CUjepgeFeVGhgSoF77o6mP4DmiGMd3-TAm5CMHeFXLBIQEs-HE4sdN7JBBPPBEG6Tno8MBaFDa_zMNb0N2o3JfjyCwwvxp3dcCm6yjzLTtsGebb2iVwL0_aK4Me__JLPhlRhezTe0bTpcibvYiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09c18c66aa.mp4?token=L2OiSRv3xEEcFoIuvAIMepTcFPg48Hvj9uG-PaJC701iAHpWVdpQwQJoX6pPr_74F9JVR4MgiHKodw8A_WngjwY78jsxAjFwSS0ll3DZQQqBWfr7iOjhXcSO1jS1xD9fOY1-asHjeZ7FoTs4eF1L5mqPU6unoVuz-7g3Io4PkWwPjmUyroqmSc6xD0ldbVYg_w1CUjepgeFeVGhgSoF77o6mP4DmiGMd3-TAm5CMHeFXLBIQEs-HE4sdN7JBBPPBEG6Tno8MBaFDa_zMNb0N2o3JfjyCwwvxp3dcCm6yjzLTtsGebb2iVwL0_aK4Me__JLPhlRhezTe0bTpcibvYiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو با جت‌ شخصی میره توی قصرش، یه‌دوش‌میگیره و استخرمیره تا ریکاوری کنه بعدش خاویار و استیک رو به بدن میزنه و آخرش هم سرش رو می‌ذاره بین میمی‌های جورجینا و می‌خوابه. این وسط فقط ما بدبخت بیچاره ها به فنا رفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25136" target="_blank">📅 13:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25135">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHyx-UQwO-kI05cRM5YqLTFi3km13vRpCFU9YTlZaq8gTLbDdzxySwwijttGYY71E32_rvXKYE7zXEyPCiEsMT2zIHrAxxO7w1zAp_4sJhYlJ9OnvLBNRTQuRvjPBpq3loRlxwYXMFR1VXeCYxy_TLPeJiGbRmwKGVoMLLdDMcdxnPcwhyD4E3uvGXix7UM_lWl47MBy5qoimoJzQ79uRRKnxcpZzGwiKlpEPLA1FzqOctlFVexYI9TpNqvgvyGWtO0d3oYNr_0IpyiAr9EBcZ5LXfxqHoxPZChkTU6MEYhnBgVtyBm2BKmd6Z94bHi1iKqwlwtiZGnssf3MEaW_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25135" target="_blank">📅 13:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25134">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkhxBdIZSRbdRsep2Z1iYFy3vVKX91omXOuwfevtfaHTHj3jnreRp0uoUsLPv4ZTivRmQdJQi5JtbgOYVWsWautiNiWaRGdy0zNGFbvBlFN0oPV0LaLU_P7zHgqFvT8Drr6SMFD4f6wm61bS5wQPLwSoYIm5kuEgfw_BtGjK6iVhXAJkRkV6RKfgYdsA-o8ZZYIgEYMgmhWLNiaKTNf4V1jox8hneHzBOzI9D1nHmbPR3JLUnuaZQi5mvjTGMxBRywf7phC9o8GJqrueuQ-XFPAiufWmnAdWw2aZyTWp1bCYDor6kjCog6aBmF8u6tQWTHpvE7IJ8a6GMw07553Fyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علی نعمتی به باشگاه پرسپولیس گفته که از لیگ‌های حوزه خلیج‌فارس رسمی دریافت کرده اما اگه مدیریت باشگاه پرسپولیس رقم مدنظر او رو پرداخت کنند به تیم پرسپولیس باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25134" target="_blank">📅 13:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25133">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYc23uccF12V43H0_0jOweb-6mDlaMDu831THNOI3HPS5IkcR4a1kgoiO45TGXZH1N5k874xj0yKGJmD8vXFDlDjkMxf_MS0fcIlOfRyPpS6zowZOItjGj2EEycuB83asiuugit4_FvdPJJgcuerR6XTSnFxch8HuqnuLnN-1G_3STMF-EQni-4joN4HE24yD-wkgkzirf2xeCbSfnSvZGCEkvrrWetFP0zUAIdlJXHm7Xl39dWyd8dcUowETNfqCPE7fVRiwStF4ZM7FGXySGNuLJGll02V2Vk2sUOuBzobn8Y_-7yVhewJNkxn1SI_74vhMquC9C1TsnlxcHbU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25133" target="_blank">📅 12:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25132">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYp5fwRjP8chE-kWRPn11kio4SF5jRB4iE4OVmvZEHgTFjbq9DzttjKiKOjhFcQq6M-Y203lnIOAkuKVz_nuVGQDACO8hPjZpaTS8zY878wn3iXmesy-OXE4aix5XE668eRDrj9W0qw5h7qt0wjC9QgKpwx41V5HpQvd2plzljmzs2wk_9oTpoC2KltO-GdTuUBN_iLBS-5jQtI57-gcOpteNoMb6MgPw9l-VmARgc1oe_KjYfHoY7AQ5MQBX4Xxhdz3acz78p_QjPAkPa0dcpx3h63iKaDtG44D54D3ZufwYVLxl4_WjXrxclztKetnsiAIfPiP3VXyUdqh9m7nRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیر الحدادی ستاره آبی‌ها: آماده بازگشت به میادینم. بزودی در تمرینات استقلال شرکت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25132" target="_blank">📅 12:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25131">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS8amzV6NVMH8oVwVD_FL6hXx-79hER8l021ue31diFrxhhcsnCybn3-vO92IU4cRQHTyTTQcoYcSyxXuX8braOTih0-b7z5_aLTb_pUkP_InbmsAOxFPPrYwRfnxfaCm6lN7HZIhRzqiWwEZTp8da6D5MudGvXROQHjkbRplOC3xdcTLiCTFJihSyAfp4cTGtANE4Y-iMpz5zfjMmUv4XY8TX5b3Qci6pQUFzxclebItkw4crSam8HM4yhU0pMYYujpUTkqOKZm7t4hwBe3nPICrVUyTZXJxx5rmMD_pENX3YwK9VDVP6-A3Z4nMSovbgKyi3s_ngvc7jDVCESdow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
مقایسه تعداد جام‌ های گرفته شده تیم ملی پرتغال قبل‌وبعداز حضور کریس رونالدو در این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25131" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25130">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHHEKXEulq-9MLBKUPycN1Z2CeLwX2IJXqH2g7SgfE7MP_uk6XVKJJsjJMw4vGO519MClbgI7RtvBymbDAB8cBvKfWPJ816N-jBBM0iERWXeqilLOxjZSOGpkbjNF1ZCV0v07HpkN0jXeaFsjcV3Y4d9sSBzsTf_xdM7JfJ2t6X1qLpkzgg8uz6LwK_uMelyiyY2HDt-4krxZ6cXBf2V1xRov_wCfTMsb5ASj-xTU7cXSRuLUcIfbseAJXq7pbiiYSFN3qh_CDm1tFoBwvmKFVIlAEYy-Fn4WNw_yRxHeh1fbE3QjlQungCC6A910o9S2WTyuJUu7lQnpgPmopMIYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25130" target="_blank">📅 11:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25129">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS6TI02M_H0Rq20XkJDx0y5wbCwfUDYN4nD1aszMTd1fwN8z0IMv5trxtff1XvxMoosIdP0NRNxmM4voYPXerBraBWvG6lLLxJFuCt1347mGy_mWFIMX4PpSYQ0CFpAuzJ4MJl2aDf71GdfTMiEsMc_vHz5lbyVdPpqe2dXE79iFgMkegwlxm56hwdwzRbpDIlLiWkKSLh9UjV1uwlKVM4-jQLuVLOM6Dfbo-6Lxz1MbvSoWdQmv4dIdMKVks8UhUCrFBeENr1oljcwFQCiY53gF8inuU8D_6qBoTEEMeYGRjbyD08Jq83iTU_uJP5sySi8xdXrHskZWUQLLNAgYMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ باشگاه گل‌گهر با محمدرضا اخباری گلرسابق خود وارد مذاکره شده تادرصورت توافق بار دیگر قرارداد ۲ ساله با او امضا شود. برین ترتیب حسینی در سپاهان موندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25129" target="_blank">📅 11:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25128">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glLiba5bIE5jNru7YE8l5b0tAbGuu2PeRB6wxKf0s0MAXzjUai8Hnv8A_5YFWHmBiq_NGeZ5ahd7Hi62zSuSiPNhuf--PGY3J_lhbDpGnrtzUm_YIlUo12ZTBGZJ6818yXh9ojbh0Q3mnU4nuCEmgpOuAAwUV1YmysMlv_dRfDYDgH58QyFanYfI9-rsF9lxZuaw2y39HgMOJV3tfEkucRf99NhxJSek_NHd7jt1dGqCKaYdu7fFHp_IqTaZTMrajQ0pZ3W8K7T7DF1CoZqr1fKTZYfovpD6SwEtqVQTfJ7_uy3cNAXZ4D35ozJP09I4ZMcV9iNxBZBfrgIW7TA7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ایجنت محمدقربانی قرارداد این ستاره 23 ساله به‌مدت‌یک‌فصل‌دیگر با الوحده امارات تمدید شد و این‌بازیکن‌تابستون‌سال بعد بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25128" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25127">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=sSeSaZxU2i27-rMtGxOIm9BoMmg0nB2L-RcC7iccFNk_XeT9d2gC_IOpuWKzsnvAaz4CB8BhLqWgzSZFRUG_lqA2G6rJmt7pmf2LyfmfmENY3fuwmZiKXhUCfDhhqdSPRhg2tQwDVOBAPpsxa3j-t8ysOQhcp3zIK8r8VHxchHYX6_Y-rCOhVuIscudDa_3qW5o0868VDVs-Ti9eu_aVC-SJgYSuOj1qccn0eIfIED3bOOvs4cvYh9JrxAOJcDZPp9brbhBGksnVshzS1ssx_G_2sl6VDOWwXzJLy0pqzDPs-vKekxi3SEEzvJdTGnyNQ6h1x96mdGXNAs6bG3IoZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6dc32dceb.mp4?token=sSeSaZxU2i27-rMtGxOIm9BoMmg0nB2L-RcC7iccFNk_XeT9d2gC_IOpuWKzsnvAaz4CB8BhLqWgzSZFRUG_lqA2G6rJmt7pmf2LyfmfmENY3fuwmZiKXhUCfDhhqdSPRhg2tQwDVOBAPpsxa3j-t8ysOQhcp3zIK8r8VHxchHYX6_Y-rCOhVuIscudDa_3qW5o0868VDVs-Ti9eu_aVC-SJgYSuOj1qccn0eIfIED3bOOvs4cvYh9JrxAOJcDZPp9brbhBGksnVshzS1ssx_G_2sl6VDOWwXzJLy0pqzDPs-vKekxi3SEEzvJdTGnyNQ6h1x96mdGXNAs6bG3IoZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
از داوری در زمین‌های خاکی هاشم‌آباد تا رویای قضاوت در فینال جام‌جهانی با علیرضا فعانی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25127" target="_blank">📅 10:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25126">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzPKBZ4MzrnxYLicOql5WSo6WzXhKoR9vXTrF3bfsMtIh0ghG7CZHi3QY2L9Wki-lzoCU5azF7x5TWGkoXxlGf0SQNKTJbRxezN8C_VllNfDfm6BE-NmU1uatyVsxFxhtY8EzTn-Gj98GRi_3kWw1iHBTrob8nJsnrzpgGLEvgcSThBrKeVawa8XAVrLxiCQqu3bFFiiTWVB_OgKuEGfBRUSHp_jfUDVqEgRjckToZRH4WH7xGB5s5U4I6OaOTmTSqhzR56Qtpm8jmdPp_sXQ3KDacJyMawyRprXb4EzihONon6RKVPG7bnthtgA3s62HdV8qntbLi8sQJilhDt9vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلاتی‌از دیداربامداد امروز بلژیک
🆚
آمریکا در مرحله یک‌هشتم‌نهایی رقابت‌های جام جهانی 2026؛ حالا هر سه تیم میزبان تورنمنت از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25126" target="_blank">📅 10:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25125">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=MjHNcYqqmXqOQdVQwos9JX2QBJGQ9yE-WO14N5Yv7QhTTcGBJvPLLCA1pSgP68eQ_fYN9KeawrUH8QHA6j-eDmv_ZArVNG8A6py2qhDZP62Oxabkxnx3GB5_NCMjWrG77DYwyuCXdT_qZKXt4xs40q7C_jSOhdO8MH_EiOzYjQZtEsBWs3D_XjCNiVdgNt0Ar3Tj9ThIQyor1jKD-2soWfbR_p_DuhF7iynjMFVKyghi3EyPULlLZjOZHIelAEVDXMA0j9GVmUxVz8i6BNb9ESEVKcRbXDMXvA0uDzdW-OdLzZoy1IiCqlRXswPJEuculGGZwE7GfwtAzrVIVz7e5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc836c41.mp4?token=MjHNcYqqmXqOQdVQwos9JX2QBJGQ9yE-WO14N5Yv7QhTTcGBJvPLLCA1pSgP68eQ_fYN9KeawrUH8QHA6j-eDmv_ZArVNG8A6py2qhDZP62Oxabkxnx3GB5_NCMjWrG77DYwyuCXdT_qZKXt4xs40q7C_jSOhdO8MH_EiOzYjQZtEsBWs3D_XjCNiVdgNt0Ar3Tj9ThIQyor1jKD-2soWfbR_p_DuhF7iynjMFVKyghi3EyPULlLZjOZHIelAEVDXMA0j9GVmUxVz8i6BNb9ESEVKcRbXDMXvA0uDzdW-OdLzZoy1IiCqlRXswPJEuculGGZwE7GfwtAzrVIVz7e5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نمودارکامل‌مرحله حذفی جام جهانی 2026 بعد از صعود اسپانیا و بلژیک به جمع هشت تیم برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25125" target="_blank">📅 10:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25124">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=uf73noIvBqpRbENinBpoXCr1paMHi7fadUR48VTLU-h3oZx8ltJxSc0MILtyvmxin8-PqV6QP8LUljqrGd-qWFrF8Gkx3LctW90CyJIMQvKzJ3hT978zOgfjNNJAWzf7IdjooCS-ho25TdPEa8sp2afRTHsIRtroWuT0PhsRUUXwrGIrnPQJjW8ew9xbSzrZLdxVArU2HUSf2EqTlNNzuCFmfvw75DpVaXbdV4RaZBSg4RW4D0jlLJO_MdB8Xo8e_6_SVXEobUE6D6AaPwK-JfEzjPz9Z5u-qEfagvPDjwS9nSddkbilMw-h0q7olzOSYkea5BOO9-GJ8iyTQncSpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b3a80979e.mp4?token=uf73noIvBqpRbENinBpoXCr1paMHi7fadUR48VTLU-h3oZx8ltJxSc0MILtyvmxin8-PqV6QP8LUljqrGd-qWFrF8Gkx3LctW90CyJIMQvKzJ3hT978zOgfjNNJAWzf7IdjooCS-ho25TdPEa8sp2afRTHsIRtroWuT0PhsRUUXwrGIrnPQJjW8ew9xbSzrZLdxVArU2HUSf2EqTlNNzuCFmfvw75DpVaXbdV4RaZBSg4RW4D0jlLJO_MdB8Xo8e_6_SVXEobUE6D6AaPwK-JfEzjPz9Z5u-qEfagvPDjwS9nSddkbilMw-h0q7olzOSYkea5BOO9-GJ8iyTQncSpYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25124" target="_blank">📅 09:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25123">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=YnJEbYNGcaOLX0co-P_BnEazsoXaUCntBlLSEkG1zCEWfNQrD1WL-m0SXEArvyuJVV871KiMGLI-zA1BpQl5rKuPT9j4EK8fPRmKozhx5c_rfgXF9Rg7uclp4lyOCUArlhBTSlzmIdq9-CPinHUU-fV8YJL0sm1GQdfKd8dcWX4kq-hBKUxl5ILlC45_oDFVsf64eoy7Gx_O3gN2ffM6s_DUOEhBToW3-c5cbSQPQ64w44Gac05Hr0EOqbix3shCT83zkcuRXpwSX9CM8wmIBM8QUy2JOfiZStVpduFA90T2p-H6fdJW2j3yWP6QbEOAiSCZ6jIa4XjqHot-EChqtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2fe49d1dd.mp4?token=YnJEbYNGcaOLX0co-P_BnEazsoXaUCntBlLSEkG1zCEWfNQrD1WL-m0SXEArvyuJVV871KiMGLI-zA1BpQl5rKuPT9j4EK8fPRmKozhx5c_rfgXF9Rg7uclp4lyOCUArlhBTSlzmIdq9-CPinHUU-fV8YJL0sm1GQdfKd8dcWX4kq-hBKUxl5ILlC45_oDFVsf64eoy7Gx_O3gN2ffM6s_DUOEhBToW3-c5cbSQPQ64w44Gac05Hr0EOqbix3shCT83zkcuRXpwSX9CM8wmIBM8QUy2JOfiZStVpduFA90T2p-H6fdJW2j3yWP6QbEOAiSCZ6jIa4XjqHot-EChqtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
داداش دوست دخترم فوتبالی و عاشق فوتبال تماشا کردنه؛ حالا دوست دخترش حین فوتبال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25123" target="_blank">📅 09:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25122">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFXactB6cbmPBy7YQ7YVgT85RYMLS64gGY5oUNhBqqdSDIURplQ696XOyjEykkNp0abERgBOrHV9lfYvFnXH92fXlFN_kwPP0Kgqv-g0fmFZVsQg6bKcG9md9FolTlCZOV_xmJlcXPv1R0oBTQN_DpAbpM5jpOHmroJOrFVgGymjJtN738B5G3TWn2EZOss6QSgl1u2lLrjqC0va92diUdt3LsdNFPRO_49QxbyOo01dXJcPlSua4TG2spbDKZAJlY7iClAS-hJOBfbYw_41bJ1WhBvT4hM2Q5vjuyAm6Ru983IE0fGogHI0zL6OS2NcZ20VhbSjz8943Cv7-pOztw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25122" target="_blank">📅 09:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25121">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FV1-spuNb8yKRqRLlfUTIMqvrJ8vYnlUYTTWEbJIKUdnq84Ksbcf3iZo3l5tyoVavuFF183wsR77prxgbFt12LZtQLi3kJv0xxlh204FyeJnZAZSig7KMmpuTSzO50yQpM6DGr7XEmD2lNhV_4eeuO8X3IgIiYBXmHons22Hl5IDRHVV_H2Vhg1ldMGkI_0uIhmugTpE9sFLeM8afoOEpUjshT994ou7pteAw-sqLfTw2wG-0rZ3suU6CfM0uBahnuCH9D5sN3KQR_2SqjnEPPjOR41jj0gj47uQK9aBoxFy3dIRbrObaTNfUeYz0OU80U1te5UDr_6I7HaHe3bNOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
مهدی تارتار سرمربی جدید پرسپولیس برای جانشینی دنیل گرا در پست‌دفاع راست مجید عیدی مدافع راست گلگهر رو در لیست خود قرار داده و از مدیریت باشگاه خواسته با او مذاکره و جذبش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25121" target="_blank">📅 08:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckMHyII5z3x8Y61xp-oJ7Ik-LoVDRTAYChB23XA3lQj_s-tkjK_acjUAqcjxH-kiLmmZo5jebD1VBwJCAdd-7L5mL5j7ZmY1u5qqfCQr5tUgd9-7f0JREb6sDaEQxMZXuZFv-TzufsT9Hv8FlUz4j9IZzwRkbMTi1bqDW7VTPvlPHFKq2EDuidhRDcKRxPV9vpXCcfhRCQqUnPtYFZMaHnuB1SMU5rJo-NzIsXiZ6z1_PbG0jCIPO1BH3Q7c0F6icpbk3raQx2sezASuzZYbrfM9uOXjvXdQqwxfw1tbxiuA_21ooBLvd8JykHo7erP2qpDTeSTXQSvOddr7bFqO2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=W6VEq05Emc-1ScVbo-Rgf7aLTmE-E_Da7juW8u9eusD9h40e9aVZPos1x6j6IJmYcU5z4bncExB8zgRfszM8HR50iLaYHRK72qlkVYdkuchKBAorhRrsB_WY9gFLVthAjHdFembUKIdkJ_rMDvvMZC_G9KdVgBPbgga21yNBGVuLo-uxIU7vBmviWLjRNTZpCzM8_t_FMf9w8CJdYQMQKqkQSkt1LuhS7cM7dL21BKesPHkYKWjVc6-EVZ-Dw7-inkiqBerRWSlR5jTHJA8uX_XTJoTz8K286zb_B8GSDbyligQetrLT0hNjjilPQzlnLgA0DAL8woqe3UJQpG6Vxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=W6VEq05Emc-1ScVbo-Rgf7aLTmE-E_Da7juW8u9eusD9h40e9aVZPos1x6j6IJmYcU5z4bncExB8zgRfszM8HR50iLaYHRK72qlkVYdkuchKBAorhRrsB_WY9gFLVthAjHdFembUKIdkJ_rMDvvMZC_G9KdVgBPbgga21yNBGVuLo-uxIU7vBmviWLjRNTZpCzM8_t_FMf9w8CJdYQMQKqkQSkt1LuhS7cM7dL21BKesPHkYKWjVc6-EVZ-Dw7-inkiqBerRWSlR5jTHJA8uX_XTJoTz8K286zb_B8GSDbyligQetrLT0hNjjilPQzlnLgA0DAL8woqe3UJQpG6Vxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ0knxaYTTlUBzSu6eiWjl_LMip23oRqnsqUB8GB51Bv83HNCCb0NbPASlGtNoNno0X-axvpHiYMY3mzSJiP2uhR2au4eCgLq3sjquMqjPJfPKGku8IbapqawL7o9d3EQcsvzwSMMQni2_Gi2GPf8qY4jVcRWu3yAUEQ36lEvdK1mQKYRFQrenNAhUIt1_F7CtM3Y2PGpMsQwL-HX62rw5APywMfn8u2KoQGPv24ReswHq-L1UxQVI58698chlJ6S5v6bjCrvx60085yK754VldPPbZgDm2ms8m1fquJa-2irNX8ufYEz681AcWsca8dcTCET561KqnbZQxn5y7YCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxXgXs_1R9t-yLSLTRGFLInm2atf5Q1QuwReh9aXzCgb-BbdF69SsgGIAX7DEGRsqeZHCF7O45xkJAs23VCp2jhQavXe9vnnoF0RiCgnaIg4sce4J8tmubnSWM30o9pIv86I7__MYJtN_sTzV1tkVcc6cNZwd1yN6CHQTzv_gaEEWrYIDIzAK8-z7xdbeBJrXFjXAcFi4ItinMVC0iHYXl44DY-xYPNtFO6xDGFSC7FM02jceBZFlZqwCVXVfbNMfrmY6M8HXN-C90XhxfchP8uUf5EwKL_0LgltgR-KjdTewXkm5jwrrMAfvw7itektzXNl_8CAWuz0UaOqJcsycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omydpjS819AYR8GAKQPPr66uQ8NMBvTFfCfA9YSvMDXsbOLHwC4ifhx26dQwpDHT0yfYSxqnHxo1a4-kaWw86LyA6uMbs-1PL6xyol3qzbzvf3zby5oRYJnc5mJBwx2mpS1OQV1NFQWqlxTS4OcM13hzhLGDK2uUSk2fp5UujYzwSKbYKo95FqElAImZLW9CtOmVBKYq63hRFPyy_ViKJemsNMclYpPqAIuc9wAuidJbGqc7ER_iwBk0AOX9zmpalCDsgNaDz_djnELp8R3h18zhH-SkaYyKLNcOEfE3Wj8s3qo0atzuGOaVqFBYz4X5B3I2ASBBUMRL7I-96uCOrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC3URAF5s9LH1GlbwSIvNSCKcRYCLNKtBKoqvIRKW-_YRBAev5QkEsmW1SZD2BquANYFHaIKENmIBEORZivyAevNdwH_PmZ12aXaBgP6XI6ia2PMDjMozDaanng8kyQExpOzxaIj4hYMSIHCyd0Nhs-cyYsSpRJiECbp9WqZOOspHi-40p1WjqOhszRmDiHbij6mdFNTAqOBrPYlVm7EHt4cDsxm6wmPnqcPxn4pxCIk4JNX0-_rTGH-1prWt9GIZJYzz1fZKY7JzQ0-4d_mMMN6dy3GrqDqS4Gvsyg_jD8dXCaGwzpnG7jAsX-cfwkUh0LZMiGteqWWIg2OBAJqOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tK7BG_JsUvLgeBay5IFgiE8Nug1_jFWU1_CsTq-Amfi7hmi5mYPHcVdbTmFA5uxAC_MKm352MDmCr5sfjvsds6DHTAD2ZIynOJv6rdVNsBrU-onKFNvoO5WNc9_mRXTDJG6IJ1vjuuHrKIGOMtxMzlUgjlxaol1Dh7zMopBMvrZL5ll_qhNHA4yBIa7r42_cRN155rtS4WeP-CzDGOcsibORMPC-nX6w95q6R2Zs8WO01Cr5BMetVPeJihtQej3tZfeTVikFNYZt6IesHhCyRcqTGOYBI21jqotCMaUdsoy-oiqjjtmw6uWQQX5GGzb-P7yXNwAGG9c_liheUTV_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwexch-laytEmSTQ7ldgPzDYMHNTqm2FhgX0jUXkZF3OI2aYMKuHtAlDcq3VrVTdDf3pAsHphcKsotdbWmCOWuNiYEQgYP86sHJ34BYzuVQckK2wKJlfkOzys-ooJ2lwPIpdZi6owPpHTDU5rBKCyIWWhLGtbPbMUFt3vvL2MhCGAGUhotvScXOsy8xnIsCfweM3-QCA6rrvrPqvn8_yNjtL3Q5Bpwbh8_1_0bKnPdTEEJFZfckuQmOc4Y7nNnImo3XIZKVuOuCd6pKfmb_YcUlyomLul8K_jnBkzb-Ww4-kVCGj1_f9AWqR6JjFV1fdoA2ZvDliq5fTUAK1bvAxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=GMFCimhXeSqUujBWJbiu1KWn6TO_r_BQcyg9udYgmjYTXUWbEPz0tTRxHAyjWgpdre0VbYb50UgE-u5jtZV1IJq3cs9zZvDVVB582zOwqDCT5yZoPSHkSxZxWzsnOQf5vFy6RflXAa4JZyq34EMhus3rsGP5INFJd1KATc5DabLDkmBlMOXUpkGUuYvMfK13no6B9dg4H5wGmVSb05-C6_RukvAzmVK-GZDb-yQ7z99k5J_kmRsZPgxaR6eoonhYumIyeT5RThQa1MKd5Bw0arZAxA8qEYVr9Wq3fp8cI7GF7cpn6ZTIjs38H4iCDbjyEcPkdCCcdV5Jb6qh0C33aIuwhBXOLxVEcyr2SJ7ZnGEHigslBCwTOIRhDWfShMyW5LKwu5IgQP4FeACkppQRQ2WGQukRCk36owVOcW1G8bifemEabwZIPbwPlS-wXhy6SqWrxTYbs4f0Qo5spvs9hAs6ml75L81rOx6Nit2ycDGzaEU9L2C4kXkDbVP5kGIXasddV_njEyUzC0v_CrYpKsxMh9BLt_IOJi8dHpDc_mnWTiowxgB96qMPA0diNyIqFNxk2wq5nlowcrwEDGq34NSoT0Ork-5ebqMmwumVEhLksD29-plfb85atJeODWtNwzl1zK2bj072qmm6LSWtCEgfhCjG80CdZc-q7vhowCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=GMFCimhXeSqUujBWJbiu1KWn6TO_r_BQcyg9udYgmjYTXUWbEPz0tTRxHAyjWgpdre0VbYb50UgE-u5jtZV1IJq3cs9zZvDVVB582zOwqDCT5yZoPSHkSxZxWzsnOQf5vFy6RflXAa4JZyq34EMhus3rsGP5INFJd1KATc5DabLDkmBlMOXUpkGUuYvMfK13no6B9dg4H5wGmVSb05-C6_RukvAzmVK-GZDb-yQ7z99k5J_kmRsZPgxaR6eoonhYumIyeT5RThQa1MKd5Bw0arZAxA8qEYVr9Wq3fp8cI7GF7cpn6ZTIjs38H4iCDbjyEcPkdCCcdV5Jb6qh0C33aIuwhBXOLxVEcyr2SJ7ZnGEHigslBCwTOIRhDWfShMyW5LKwu5IgQP4FeACkppQRQ2WGQukRCk36owVOcW1G8bifemEabwZIPbwPlS-wXhy6SqWrxTYbs4f0Qo5spvs9hAs6ml75L81rOx6Nit2ycDGzaEU9L2C4kXkDbVP5kGIXasddV_njEyUzC0v_CrYpKsxMh9BLt_IOJi8dHpDc_mnWTiowxgB96qMPA0diNyIqFNxk2wq5nlowcrwEDGq34NSoT0Ork-5ebqMmwumVEhLksD29-plfb85atJeODWtNwzl1zK2bj072qmm6LSWtCEgfhCjG80CdZc-q7vhowCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=ft70Mjht7BmCZq7r-30LoCZssDeXixxVxoqRIptullb51mb2gUpdvo4dOc3jt273XfKjYWjFBGt2I7kzJDL6PuVrX3Sp1YCdcR4PeNF6uZUa9Um8ZHR0GbnzwfgOs1-MHcePuBxQb8zEbS5pVcIuHvO7wgxJCQqEWrz9bS1v0FJ4ehUjQGCGBK5T26rXa3BWFpoNNsSJjW86HdvOTzdGljtHfMYEw1GcMEVh6p5Nq5ZUl4DWQvqqNjzQ072K6bFqOR2na7KpyV4UAbDghyu0W0u8mfCRqK4FGRQQuz9qRM6wrV_mip6kNLhub_9-6BOSNWV41cqyTwhhqwRZrDR6mzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=ft70Mjht7BmCZq7r-30LoCZssDeXixxVxoqRIptullb51mb2gUpdvo4dOc3jt273XfKjYWjFBGt2I7kzJDL6PuVrX3Sp1YCdcR4PeNF6uZUa9Um8ZHR0GbnzwfgOs1-MHcePuBxQb8zEbS5pVcIuHvO7wgxJCQqEWrz9bS1v0FJ4ehUjQGCGBK5T26rXa3BWFpoNNsSJjW86HdvOTzdGljtHfMYEw1GcMEVh6p5Nq5ZUl4DWQvqqNjzQ072K6bFqOR2na7KpyV4UAbDghyu0W0u8mfCRqK4FGRQQuz9qRM6wrV_mip6kNLhub_9-6BOSNWV41cqyTwhhqwRZrDR6mzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sux_9J5WyK0zxVtkgJrUyTMcmXaAXhsj6V3osxXI431xG26L3RVEDFGAHw5tM7WqjAvL-n4raaCEPdJmYatS4nX6-4N6s92Wl-3sDLCOMww3PlvdowS2YasY6GiTXMq8qEqp5z_AEeYvfKcjVy1uV0Ai29CpHJvCbJMkNex8QoUE1xtyPqp3R5Njj4mFOxGARnb_BqBEwkS-sp31YhfcQhOVb3ChgvwFTvbbDZ7qRSOb75qZyjesSnoHopVO4oJl5rjLw3TysrjX5yu_aKahXzmtVXD1Nuc5sKVrChgknBYwSTTl-KQyHuSCC9YFpp6KzSY6RdOfrLr7c33wjw4R4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mlN2lODSuZsJjMJa4GLpQcHkjRlUS7XEllUQ1C_QfqV8BfCWqX_ekGtDOjiimV0gIdREyyuKjXOpSN5D4wejP0BpaNEMbqJLG5x-Ri8SHIBjdHolyZzyPX7QwSXNywJBSRDBn5rZf5KLFp92GwdvN9yjdTkS8oW0r-BsdHjrimztz1ZudVjba-9jVDuvhBtPK1VglnKpzUVYsOiwyglhRebSsHmsUwOBgGcuSvAtCdwshqJ2D8MzBrQCKCZJt2oAccA_sL3CYb0rqxFfcqgiiJG72XKw1a_zW7tMevm2dTGm1ham-HGM5R7sr0pCjEhFwXyUMDtYw1-NTcYM3gLXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvHkcogFCJ3JepAYsiLO-vtpAcGAQOTPg_mf2U7_l76q3s5SYZ6yyKPut8DnA9DrvB1nY-FrNHEOc2Gk7L6iGEi-3VXyf6eGHT-si09gUAGqqJynptIfXJT8c79foPx5d9U-DvEx-JenbOz_w18cMIsoWz683kMQK74ke_skLfOvSC481ZJBLQQ1Y9adTfIzx29I4Sso1nxxi7NcU_wVVf4nu_hKhjjAIU-j1xOClaVmeQH_AYQKFcjYWLC-seQyPblFgWUhQC3qeCBSodCJJKt67fkrihJKGTPlcnt6-IVk5gVnokDsAOVHBvF484G29dA2g6o6TGXxVVdEsCWaBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqEVRoB49u4a3Y6GecfMzY1kdEWFKCmfvYxekvy6wrtcbe6P94kTaKsSo1ut-SQlCvsmL4WnP96ai2NTN4aRhMMwXMCxtNtkKHKoo0dAuqLIhla4Jok8U1Udh4dRCjNjUxYlr_oF68NGqLUjjYv-PhiaX7AkilOUdXvfGqNI5SXcqkJMjwC6-ZeHwomuWQubzBx87F5efIdXd6jNqlxG2Lhf4Jm3LRiFWySYNmvJzDwd2_0WKHcLO7lWz2niagbk4Yc1-hbi2Ym3kEKugNk3OHmXHssDj2SGxRz6IcLLxtoU3STtItyD-XU_iYzCsLyqUQEx_eme4TK6ic9aC4VNHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmiWx1U6mdpYUYB_6gE7ls4gz9GLdP9rx8zUhtNtpxhz0JFMYtuDE5dRB7WmkFL3t3tW7Dl0CicQvVwZbbY5Kq0uJ05_gly29TxIaUKh0C4dB1VDpfEpOjy_69p3Xlrrom63IYPKwlxgptfVMeDqS4kHrPlQMuBpLGNPuSMP6hk1bcZzWT9lSb5IgzQXAVk-VYN5HXcV6HK6aQpby69a4opCCNr6t_Zw7x2ol7_ARDnkDKDO2ouc-HO8qDSS3wPkn06DWek3isbeHGzwi8iGxU8Qnq95BtvBFuYsKuudfdZaWeYd-b8b-tJiRvY9Kf-Ob6q31X04AIz2QNChzkzpig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llelHaCuOCLeOQwuBH5Htg9B-M3X6m9f2F1nAjV0ZT7KEhvLhXkHxC78Z4eD5ogmhXhEzohluxkstlgkmlisHiF4Ylw2kF2RMzqNaKXX9bltbhlDUvGKSOsdV_YL7auMXtWKoi87WbTYivc35Xx9nq5z0zIqjJ-5V2-osXkGJ5U6wFYuDo_HsWjBIKnYPJDKhJsHX071JakuxtmftReZ5sdkEu_kJU140a_rw5ppTMwuNd4rUxulxMaopb7i64usgzofEMJbMNlIBK4jkkKb7PucFdkfUo5RS3_HAE8RiIG55a-iCxwRmNJcVdj54wijp6rZKnld5v2SyY84Hm6Q3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB3xIVOqXri-3bBsgaBYfaueFUK7sU_TklRa3si3j8ZieCIgHVosPQH_I-Q6SdSTEOWk5AKCvLgUad-46eSVwtdEt-RfpZe7LfLDL6Ycj6S4aZxlKwy2-GUfVl4zzGmeuutfxh77ya0XoNSB_7BKi4N868gKTDKqIdUsCfJALSdZAQ_lDJQhuk9bIXoQXigUTn2J7z-luwpJLBNkfafPaXfz-e0SOgLk_JvAN6wZ4_s8AIY2ke3OOBM42A39VF6SJ5z_QKObJD_YloG3dIl0DyjAVJOP6TqQsNBeGkRnvnr743V48QjcPM3mMXaYfDFPxvvC-deKTSDOiw0d3LGsmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVUnNXQktkaUSviuhVGgFy-mLiAwuwkdrlzXqdMSwUcIcTWFZ6bPPfOTdYsC-gp-j_W-iAGN8btTXwMpsiaxDU1fIvaKdp9HuewzEAq9NPDzheXx_tWDcksxMZV-fWKg87xPFED15oY7MmDvuvFeEN3WqfGZKuqT1dNR4gKj6s30nzN5IFeGPKIOy9G6ir4ElEwb76mprxjatZ-U7UWSF397CBdeDiZZEX2tLz8t2WHUepRZRN1VlnamDMdSOoIEKYVB2FsMQRhRIY153U91Dh0kjsRAECxVN8BStiZPC3x_Yia0W6rQ9hIPM2KsP7FtjBmp7EZKv2OAPuIrv23Cmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JikEcQXC1VfoRfPvL4gh5b9WKhojR4DXGS0Ps5JUY2Xlx_65vTEUhZasy-kNi9juGpSmJ6HGkYbN1W37MWtkyo_YcGabPFjR6_dCvKjebaFPPSxdrbflkOHKyeEEgO8FzPzNuWInmUTsZuB6fyvXiMPM6Bq-DEfRtJ8GpYDzjGH8cjeWwv-n9Hp3ASYD6qgSj1X_Saf10-40Iej2vaEa4ROAK82y8ogtxnLOQTPcTX-uKWzqxeHMlz_NCGTXaOgZEUJcSsMsA_p-q3NQe1RwQZfTTlB58bcZwydEUjNto5qTo1AHbVVNDJIOfsS4ZcydtfwGNAhssgZ3bVUrCHPIaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaX3iCuLmJhXE9_LQWgJnif-4U5mQLqsEkhR8Cr1aAhMRPU0g8eI1gqlsijhe1GCtIp1hSDaIJdN5mh6G0IMT434wBCl9aJMehdIULNFElj5hl8Y0rXRi27VyLZaM2vju6ow4jTAhe7anLNlB0WF3cyLT7QGilun1_RMs5FMSk-iT9dNBumyqI7swcdbMISnR0byh_q8eam_dbdAueQrYRBwO7t_MOSn8GQH0mA79wBM-DLZdktnSYOnOxKOh4ICJ2Un9DjSOUiTUbEdSeAvINBzpcn_GY8EAKX7qhwQ4qkKnBBKeJsWW68zICZ2LwUYZTAHM2hrgnBS0gcTtlkWmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQoZL29pfQOBulpzvIYkJdsSOLBM12SBL-oV0z5tl8vZ11pD-t60D5LtnfVtXNBiYZ-CDGQYpHEuVnL77mVAxI3xhBriTRveWWQYsr2MSQrv1U09IhwXU6Rn67MQx--2huAU88LxznYrLRk3GB5Ihshs8klc9igjdyt_Rt2tzlnWuVtakr-BMRmPFngQSUdUH9dN1mdLrC2b_0RQRG0CDfGh4084vJF92DBgSef1vevevJT2A0G2bk7KzADH37JZzNX6O5itxRouq94_TkA4Jet1aR6YPF5Oe6jSQPphzmFfmlOqA631eO-QMkrUARCpD-p_eieF4fIo6zw6b3A0AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXRzfb1xAHqm7tzqhk-RjwhNd-p76c6UtFhiE8nW2RvOzIS7Ho8i0974t-rtWRp4gSbwuROABQqYFlGYud30kJPBB1xhyebS14miHdAyhX-5pjTTbal8WFsv2WZq23fXo54mpk3Ilc55FXLGu2FfqmoUOpiu2U5yCBofa9qLCdZhPHW57h_JHnw_ZcLNIwv7FdWlJwehTNckKXR3KdHt5iptD4I67ftp8MOwC941I18-MAqHB0SDKtObYAFA-C-7ND8l9vsKBqyK2JD7JEKG3QaRkxs0nM7lCGImDSdJWqHW5wTjjU7NyzlodIiVmpUYGZBLET8zGqfL0UtyIz18Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1iQN7JYwzRA5GDR8rzcyZklslZq3at1P9GfVgVxNye6ik_YVniy6TTYDJ_Ih7hanNnJZn5QRKoIkZfHjyYSn1LXHfqeMbZWnuvzdUHsKur5_GjavSMeHdPk2Ba0uP6fQ5xT7VpUHOb9yO6LwLuXaAh5xGqCPc1eyxvL3lCIalWJbVk_ZU9QA6gaOq2QFFyCYs89xPv2FHmjA9MAtO4PE-x3fO_Vs-8-tc8cHBF3wBpsRQ6GWh86EHViRSFToqIkxw49Gm8-b9UwnSt-6R3XDehWtD_wowWm7WcudvGI0KAgKp9RzmhmbqXn5IO76EdLOZN0Qh0Ncc17KP3XrNNXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DdfSD1tlsxScKc4uP2tMZEf16IQOpOljR9GWdZvsv4qWqRsq9Obb45xXKZlC03VO0NvitjV7kNpLQU0Ma4MoJGF1yy8KvdispqEvRpe1Fw9xcGKsma59TZ6Qand-pNLks3-5Wf2kc0K3bB6uF8FDNZbfn7CxCLErIGmZKUWr66zgqSvXReu1vgcSgjHCj_QitHLzePbHdVuZzebbpEaegDoIUJsDJDqH_h3uiF2JwJmoeYolDV7_ISmRQu7C8iXB2zBk4OgS6rLiyPa4AQUg3O9yaNr34UAC6yGMkHtlkeiOwKcLPLb_YXP-FBZWUu-65ITLLk_SF0ov5moPudgwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UenkfvwGhNUzXn8orywJf0VS7AKAGnTNks81GXzPJj5wLMSBEzSpM5_sdAQjGf9W7xCUK80aHN9tA4WAXn-3HfMuIVmy3-lkKfnjzGix1Qbw2f0yq4YkZrpusiDkSWD1b5p2R7PuAmNh6JoKa4ybLJJCvmkxe05_yP5biBL9-gci2RZ5rzf5QBLREsJrn1eKq9Gg-gdXujMjyK_CfCllzCU3pPWI6my5MO4AbyB-UJdSAyRFQW7Rw0nU8fGRovwPJF7adTTrYxyzHhI8ITg1vHMbO5xy4D5zkB4f94qIQhvNIpkbmepnhHcQJsEzUTtZwpBO4GbDtN8-HrjFGs9HXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT8stpuPmOidbm1CRjzfSmQuz97y_Wys1onVnIhl36_bsnxNNYJ0exfoHX03Td8S8WalO-1FNStqxn8jyB8mgEZeI2wkSYP1K85npMhJcAc0aNED3VrMuQha9xpzmoJEn7aZ7xpO7CY8nFj6fkycnHzb5PqRKbQJUNQ42f3BhsPQI9JhNVaqEhEFTyhN8RtVbDZQrbaWuEUP_4bm_uiC3PHkSWshUaF35qANfA0Szf-YW9uTVKYHmKrdK2KUT5cYporxFaMhTv9ASkTRJBrGBu-xappnIoPLOQkB0G8BLtfpXm3EWoFVtPI8LgdBpXNffzf7hgrOuu-5sar2HrCyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1f5FBsSWvKVDJrA39RX2K4DUmMzM2NjycHw1qBlx5ghdd5YmM4n6nO75ytsSk05F8L3QMOZ05-w09RGJ8DnlAzIZYweo22n8oyMhVscQPTlesOfde5KiXdIZBR3G-aO0ZmCIBI0Wm2MK7oNqsCir_O3c7errmPl3kvPTzUGLzEvKVB_qf1vtd1_fb6FQ_1sdrXLbDsgG_VcZxYHSx6vno4AablYocUUBFZp8mHdyLjcoUvlcA6BT3U0dAQjNrrLXoibbXGM5YJ_niZxsp4pidwWnnb9u4S_SJyrwpheuSuGE6-l3KhGCvc07rZFX_k7RxRwwJ5oWsESBj-xdq4pOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=vRhjfM3N1wGXmYKY4PttYyvFno-CVyK1Igr3ey2nazt3VH6nMFmzEhhinbRAKjyaBmuJcwHbrIOcG8iNqZlepTxYWvrze_HcLbe8xxOpwO43wmEvJcTHsL34x15NivE0zfxZo6dwpdiTOQsm7hEd4wxVZR2Q3a0biwAQToyi0HRACjcn8-VDmerw287SokpFEUgkqkpd8fpMGkHAcK3qY8yj6xrowvlus9aswczOkCcNR84XCGkbOV-e11jAiJEQK5TSojdDbqw9tJ4N4XcoQDslsoJDh8ndIai6U2gNk24yzSNjOd7I4cFZMc0CCVKRsTWsDxD_mIpWjHwn9gXeDEQLuCF3mYD6rOjWBAKiTeg8_M5_wVWDSlrorZ7qRXEjtLgM0WWCG2uJRZ7rQRKL4Xy9T_OnJCuaUchDrCJn8wN8rjccInXzslNg_FDxT6K8J0xOEymC75jRrDIMHQFuyk3g8akdH4OVYF1i1XOpG0BjJ1VumqGmuyDm3gZJf45K7dlKQ66VaAPzGN4M4WmyT2Mp1CBG8DjrahBkfWFedQYyEAX8B619Q9Kccus6WQOfaWy_BukDXfhD4i_NyXGM-Uzuy2Umw-h5U2RMAP4NMZcL4CC_ju5kLv-sDmZSRKFrwFm0gKuhJxaS3D4KMb5iPurVdX34D8NPlI-YwgVVFZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=vRhjfM3N1wGXmYKY4PttYyvFno-CVyK1Igr3ey2nazt3VH6nMFmzEhhinbRAKjyaBmuJcwHbrIOcG8iNqZlepTxYWvrze_HcLbe8xxOpwO43wmEvJcTHsL34x15NivE0zfxZo6dwpdiTOQsm7hEd4wxVZR2Q3a0biwAQToyi0HRACjcn8-VDmerw287SokpFEUgkqkpd8fpMGkHAcK3qY8yj6xrowvlus9aswczOkCcNR84XCGkbOV-e11jAiJEQK5TSojdDbqw9tJ4N4XcoQDslsoJDh8ndIai6U2gNk24yzSNjOd7I4cFZMc0CCVKRsTWsDxD_mIpWjHwn9gXeDEQLuCF3mYD6rOjWBAKiTeg8_M5_wVWDSlrorZ7qRXEjtLgM0WWCG2uJRZ7rQRKL4Xy9T_OnJCuaUchDrCJn8wN8rjccInXzslNg_FDxT6K8J0xOEymC75jRrDIMHQFuyk3g8akdH4OVYF1i1XOpG0BjJ1VumqGmuyDm3gZJf45K7dlKQ66VaAPzGN4M4WmyT2Mp1CBG8DjrahBkfWFedQYyEAX8B619Q9Kccus6WQOfaWy_BukDXfhD4i_NyXGM-Uzuy2Umw-h5U2RMAP4NMZcL4CC_ju5kLv-sDmZSRKFrwFm0gKuhJxaS3D4KMb5iPurVdX34D8NPlI-YwgVVFZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBjYRxMLjChOBNmktRWI4_Ew9SDoVm-O7rg0gQ4Uy5lCnqLgTB-7fgxlSLrnFRC4fVr4_OHvlS7TCxUw30n8f7aztUR1K8ZfmVMJVza6D0u06SF__K7CFjQ1CwShuxFf0hwz0N9WATyi65EnLYKsYnuvcD9CCQfb2-2IuCDXuimdC1jlPeUaNQQ18K9XbhhIsWvUujfnBt2BiOfbKYdcqbNWTCX5S2PFBkrzbkFRAjZ2Kb6jcJvarLOEBN5Bv9aN6jFcP9uGo04Y5WazgcGIDEzxm7iteqSzY_sPcLv14xPHgMOvsJ8mq-58uJ2HYInN1QlYBJEqVLPxYHDMiK_9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex_su1fXjZmatbtDd6Bc-SZEkYDX7ni_I-BI--zSoQ6L5kHWEOfzW-l3lb9DzMkdeYSWvappTCi9sFPWfn4CGIQ7Yo8hERCV0fWPyFPhWo9dLID_CXdNEJYzUhnEjHiNI-BQH1mNMCInqycnYrGbNxDHGxZCvd9BDr14qY-eGCKHkXqxp20FPyrJH-RAgpa9vQfZslS8t1db2JoL54tTJwPImwJAnzIubkGBsMP_mjocJEgGxmav5Al7j4mp-3ZE_07YaKc4zP4A6Wx3tZXLIwAZx9sis9RyPaeSlB0sEh35ydsY2vNFLkGXCS0owyyAdEm8Aww6-1TPqP_1-S-6qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTHazJy-sGbVxdUNG0h71dZwQU2V4PSSDfgDuBmtsfIPoPE656-9z61kobSY4wf4O_P2JqSpMyT4xJOqgu5WITjYVkyNymzmMGWf6oj74Y1D0afu3F9ISMTk6__Tc8rEX7GA5RvLcIYruQ432ZRsQZ5tsNctKOdcP-ULhGPv7q-Xb03TYHx-2GtZ5JDl5BCPpHNfwCBajAr7yYMV35PN_8YLtwn74mKU1ihKRfcWUG6DeRjj1xk1R02vgSPl2eHbbMKMKn7D4Q35nV4XtlH4u0RzcSasX0HtEJCOk0ERX_GTO2IHPjCC5s18kPxkWfXgBbRptlIYqAttgRZCjouEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE-X-naD0ZP1EWqJch6UK_9ugdC_oyUDWh-qkgghGXhwHxv5zL0XxDqRAv41tAsAPmmlSYtwRSjIIC2S4ZYz2NRlqwPsR44Ec8mz9AR4RSfbvTut7zSVfx1ucNXu-_tmf1fQ8bcy_mf7a-I-qfCKe7Y309K_SMrLqjIPCvQwMJHtfygPZSjkErcjRVqhzvs-KrUD_E1lX74dy9rMNVhz3ynbX-CCwRVGbK_yZg1_EupMJwPD7jgUDG4piEzkQdEoa-RkCLem_wraUM14HwpMrzWvKCwwxsmGUfgkrDLgENzEY5sbNsk54nEw8LRarOjp26gVQxWqnDHsmXLw6pSD6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ob161cD0EsJqdSvSLlkrByeN1lbhWLC5UKozClowoFxFTESnQjGCy1Ck6Q5rtmHs8tT424p0rJ_dYwzi9KI_JDErZdgAJoUa3Nguxv-kqSg394hD9FKQ09h_Ibs6e2-P3nPMyGqBoAs9714tyNBgnca5K6CsnyToO4tDa9FciN5woKfLTSvpBQFhYx3OB6VZNJwBAtD2UNEXLi02AmVrUMd1CmYlIfcx9IvXVRsvh7Z5iiP4mjr2WYveaJAYwFs9k2YRs03ZQAiC80fmjZQovIf8Ga3qJIhPn-lXwvqvFfRD43bpjBtIbvVH8AKjkg11pxnoEGTRHUBcApQyDUDFig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdSmHN_4dtl_dLxsHRBks9FawSoHS6tpCwwrvcF1B0McULS0gtPxS8eT_FXPWCSt370CbYFz1oKXDek9nZdQ7tTyc-KJTHauJ-pAz6TNSOisF0UetNJsTX8CE9rmmDRrJww0mlt-pn40p2hCrBkQdGsDiI9TzID7Xw5KKGTyQTK123ejC3RWZ7yfFc89pbWihojMwJaS7c0w25fXADJRflD3KZ43RHltgPtio-m0UtQFD5XoZQlEFsgbF4fAMKM5FyDBiEcmmKk-si4MUs2sBBYnMlnQm6F89oOkFzTKg7ty54wHmXzDCE2To3ITA_um1XB3HbO1-HjpUlTmTplF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXzTz03NFejGAWo-STjcgfxqvgOPMQ7u5SO5CHYNS-TGN0SADLLtrjGzInzWri4DCxJzWkeYJSoZfAINoBFHgJ0MJ_aPgTeJu0bl4fKozpQq7BBFPT2Y0ValnAH8iVZ-Ce9WeOZNCi-g3iQJ9xqipYJF4BCaEOTxpvDSNzOXBzbXSeR3NYDh9uoCrVb4jLQZjn3v6_bOgN2i7yebLnKqe07jG63HWYpTUHWIpzJHIwPY8nyx0Rgi40nQyIQ7DhXokIG3919c0e-gfUFP8g2LfAnU62pitWC_z2qyzvTNAtH02WOQSnWbig9Gds5Ao9hJei6qTzv-Gj67dWHGAnr3mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S30XVfLwN6avvsNtfrndmm-M2LuonkEwoOHlxKGmrFj5tZF-4-3fcch3_5X3pAVmfzgLTUvZ4-Xk8w91UlzprscFCvA2JfBtW3oHn2Ha0wEX7MTZTl__6ugnIWatTAbABeJvPZdK7vJL9VdjRayiOITieqdivyCdUOe4hBsyKBuJrH1oGvDOAWB0l9wKUa5gwNjSBVg0afiBNHd6V9wPKn-RI-EBA1ll-48dJ2iYmAjuB4p7iFEg3YUF8rc-IL239bBN6ZjmPaQMfVB2J12kwPJbx5JWd6eJ3i8I3gzHrs4_oVTXYOr1lovhkMcfwsOE79VU3IQQI3T8OSCatP-Unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgmfd707WoZ_vcpFkXQRpDQYIZkcshfZHYbsWnpOYhRUiWpv4IXQJD8PaZzhpYf7qtgwUCBP4dLO_3TFvSP46EAS8sTLwLQLwMjaffkZZQ5MslrS_4jk3RmMoOPM9PFXqa0n2fzA0a1OhfBl54ODxn8QEJWY2gW_m8JKOOL-LpfMaIUWX5wHxex_63JvHQPO6tqwLe6Z75raT2T1ZJyHgMKad5ZPtmHChmMlmusfPlkBvg_cTgfGPw9_z74vMmEUXjrNyVQpnCAnu4hnJH4nNZLDyWPfnsKFPFZnrZFHOQgQ1GWHJrisXsf7_VkxoRqTRMbHloR0iPP8bHfJqtTXQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-cw_MqNxmmFkBx6Y_sVVUKLKnI1ceBNNM-QJ5YZtowDaeXGdRyjZkDB0bnUQue52_USTjB-xQ91CKYXRMFNUEqpxD5cHAUvUKn7wg1O3O8qTmXn0sxvCM60sEQFj8ubPZVZVQEa7c_whrZN8edjaa4EsfLUBOLCzajJ-2YBbLx-ZZW7cjyO-_iYXJOgMgHRL5-45Iksfn6RPTua_5EkHCzi2vVg8rIOIkgHqzf7Bqp7qZKV1hLXUud2DGe1gRgZlOnnjA5Jwb5SX3LvGheEYRkqCYMff8h99PPKDlXdJqrMhWBUIpalhmKO5dTFKGuy0xm2gidAKOZtxyHSR8AxKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYvSqPs4auUrApT3hOJZkVoruLDTNLl6Ss-aKym5AGjbEEG-q0fvm2X5__JNdTzja7a7PmuzCmIwPbxIoPEz5eMSGstKfGxF0Iicu8b6hx890Fbo-YVMPJLcn1UIvguxC7Yl8WqD_A-ZOpXWZJuhZ2AZP-vZtFlYGpRWXXeqqo6mqrqsfENsj8Z_24hJw12jT4mw7bqj9MuWHyD5Wyitpp6EqnLboNR7FgNzCGVe2Hd6FUiKspijhT4-CT-aA0vJF97Xg07YapfcTqRfJpZNxgg7hkPvnk9SJqhOnVI0HfVzUYNWbxCiOqef4bJevTsAp9-GIMyrTGLSF8l40YuDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1KZjy_HW5MXVRqqimaJnDeTZoy05t5JJ14ZdkBvI8oSXEA42IH1gm-Ym6_CkzVWC0YfQqW8FWi7tTnppTZLNhZ_Ypnip4r46kdtE_5_eAk5FSXzxdmxFzBhm5QbOTpPcGeDCWqgi1TYQ4b-TMh2uQgrWYa0CHffquZoXeJ1qbnRE4uNP3wI-Jhoi9Tie3V6PPbsIqfFc0PDmF32LCfDiRRQfML5tPkm9R53ceFewLlefQWBXqRcRj_xh5U-9W5Lf6eiT5WIUQrE8JgRZDpaZ6IzW5og7oO6oooJMjhS2ddLqJdiyPFerxd5dPeLFxlPC0x2R2tqIXH-k9m2pnbmZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhTm04EAv0Q3soRgBU-06EWOUwHlc_BZE_yCBUd7INgjWFPktH7sMCrqoTQgtaTBueM5--41BV61IrE3dZ9cmygfzZkJF1CMNnYAK4IX6TvyfPW-VBB47LswEviP0SSXk6Io_xyhlG1fHh6wtRqQeMGcr3vKBS0ZJoZ5l07R7_IFuVSYq5fXxowBzRFGJ0fP1e_XuNIm9h56zVL3dWUakLEY5lIAcksD2pNCN8yWLaxxEReqfQ21pPd5f7yTo6JLr9URnqzP3zeR3l5EEB073puSaEikeSDQjbT0Syf51b-1iXoDQFKWjD4eL6pvWy0iFJYFBXKnY8V6CIURU2dlpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=KAvxaPSUiqVJXC2Wb4ijvq6ogYvg9IzhKP4i1vEqBGT0fPummyXKJOP5cbNcW26Y2E23r6aPYOYPVsRnW-Fva0Gxa_au62LrkVfsOBcscsgE-teQQZcUyhvBe5rk4E4WCQ9b_0i7ALbp8e9MhOZO8WIZzTnNPNemfJsVRf-RfvBBO7ssq_Q10JsLta6Fw0LuGAcY_FzXYYT-KoDFX-OSukm8XKgdSNWB7TmAmvTWnn8F8_7TnVZkEPfFPra8tlK2zvGY2AA-2RktXgtPX4iNdIJaIHeYOfVYtx2JghSGHtJyLI7oBZmN6vZryG2AH7fY7gvNMhAGluqQz52YEiWH5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=KAvxaPSUiqVJXC2Wb4ijvq6ogYvg9IzhKP4i1vEqBGT0fPummyXKJOP5cbNcW26Y2E23r6aPYOYPVsRnW-Fva0Gxa_au62LrkVfsOBcscsgE-teQQZcUyhvBe5rk4E4WCQ9b_0i7ALbp8e9MhOZO8WIZzTnNPNemfJsVRf-RfvBBO7ssq_Q10JsLta6Fw0LuGAcY_FzXYYT-KoDFX-OSukm8XKgdSNWB7TmAmvTWnn8F8_7TnVZkEPfFPra8tlK2zvGY2AA-2RktXgtPX4iNdIJaIHeYOfVYtx2JghSGHtJyLI7oBZmN6vZryG2AH7fY7gvNMhAGluqQz52YEiWH5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ignzXgPNf-HM8_O8kwKkGDkRlPoovtOQi7QvuK1EMXGS5oq6d318eiQEUn5D0Sg21vwwfGw6s6kb17zMSGKix75TQ3Pyl9smSGu351s-yJLc09aTxENi3PI0aJspYzMZeGxMPEZZEbOxTPK_rqcy_ROe6TQy5easMR2RDofAGhZL7LyEJdeu0aKWcsShdHnwx84BkonVQ-FVgUmCovH_IltO9YZCp_bmntPxAtlda2kZtixHJVIMwY0YVVF65q5D7OQ4PBeojC6WNR_JjOK7Qnce5-1kprPUY5osuqFGO1qjIzIZNPxAhOnE5RvfR-twVj_bjgJsTDdqbESzkBbhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cqxb9JN126rlHGcSxM7qb7hJO_uESH4SM9kIIEh8nrqdXUidpN49G2046v6yubWqQyjksq_m1PxFnCohcHDu16Nzu-jc0S_lbEvvaA2lncW-7cTUcUTjFXcO3fco1tb8GVIwFTuuxUn0tpToFVB3gonSoNMlXWRt3Za1_Ckq933x7aa68KPe5KHRo49lE0PBT6a4_Uz5n8vxkxcgv32Ue9Z_S4hrClg6mJL712o_fXPbNCXqoy48R1XbXzZQK-yngadOCPkDwJ54wbRrS78Y576PQU1GZ3qemV8gyaPxXbuO6zS9n0c15qPp2jTdlsBmSUh7sPL4WF-1YC1Yr_jy-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfQKdee_iVB5mLy7M27DdDVtmH8FEnXkhNW6sN6BtnLX273GmmcKzZ6nN9ioPvlmt5CdW6AjLCv0tAkP7-VTUYPaQvmtEvqSeHX9Og86jg9hU5oFEJdB6qbTxXtRc1jpTGwIBLePCVVN7Psn14EMA_oQpCyMrxeHekv_0gLbAAvqyh2fFRgArMDgPmOc8bv7Ou5hoFRFMJ6W4tI_KNfz_ds16LwQ3SYhPU2BZ4StQIVdsW1NvY95t6xrVBXPcv6QQeAWTizadwjW3fL6JUNZEpYUP3q8rTzJZQjmkx06FwrFV00p-xAgycMUNEmVh2hiYMrT_dEqFC1Aw5CJg1u9KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVxtspbVABGVA4JoZ9_s5AoegDI8GfMZjRp-XWRW2f3WGZXaYvRAWGjBnqD8bS2Z9JjAH-mE94_bg2Er5EnWenlxO9qt2M-98yxhDbLkVvcu5D7u2zp0ADIaT8ufnhawsXDTaWyZerDISsd5CMGUg6IwWwAYVH9jJ38zFnCEk94xEecu9EBeJS6JzGPyzra0i0uzSovV6pYkzzrdVjuh3gj7WbytF3BDXzLcKMMVYCQIW5X4_Zwmh2e9iFMCgb-ji_QuqHPBgcW5WSt63D7PWTqZv3iM-ijT53xVmnkNainbspxJywJG9smumeoaA2ZL90WnJ0z7bW-OG9CLf8CCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUDenlBamLP_TK6Nmyfa31e4va04PyWrna8dtDxOAKhK0ljHKfUiye5uJDzgbhKybAu29uAIm4sUAl4mIVa8UtDF_8Am-XyNYhy_A52G94QE1c-FSt0BulavIAHD4lmqWwS6aq_TTSEvQG1lNh1NRKYRZsTv9UfG0f3krF5q-CF4qnPSyB-IRxJ_PxvPsGeXTpO2PEPl9UqWG2Mx3fgK4ngIFVI_H618T-Wkaz28WWKimA3Rb1d_FrUeTMYaMNE_ibHcyBECkphPIIYAg9LgBi6pUBQoT68EClu2wjiuLZRYmAtyKIjxei8-24NtY8RyCYwqkq2gK2Khl0ifKGUcxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7IZsHl3GNSYzExHmQU30Q4cxzDm0Mlwp5VW-eYMOLgouIXRegef7Ca-lmsHUzEXVeoUFGsm7lghVioguXeEZbACm8hwU9NP_z9f6rfl1Uhkl5jWobcnyHH6NmU0Ip0Z7EESJGstRzATMCXvApnQ-e8SD9CAJMpnD8l6YXPinunBX1eKDW9a5sjBbelfVNUHcLYapi24aohSdpvhlqk6AYsTiYMvFhTXqQi5rOD67wZy5__c6-qcpyqSpxl4mYddy_er2xTc50GAopYiB0Q1O9OTV7Srf9I0a98lJaVkLg-Lb_J_dX8x-RriMx2qJWx4uqukc8Qy4yszJol7WJ8XbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0UupTC6OEEIQPpv-urfwJyNQT4It5E6foOgvUV_ekP8zStgceA3LJEzaoVfvOmYnxw0WafEBtkmsdoG3PWPvbDmmHvJlFY6UMH3EOEQJ34QTKb1LTkIa8i-y74xyeBv-B12M1s1iixGKPrKsFwx0qnVvZUL73fJTQIOo3wQItNJOKU4P-me4r_XTuGhmNHdui1Hbk37TEaONJkJp9zOtFcM_3g1Be2rbkbFFNEn0x0KstZjJnvXoXcRGh6NxyTHLWZ0TpDM1T3fd2FK6l4nDQNzAo1EQGSUm-Yh4hLJgEMvcSKk0ygt43ZYEslxxhE0aLzpMUB6-JVWaZaOdzO5gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
