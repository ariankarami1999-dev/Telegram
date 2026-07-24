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
<img src="https://cdn5.telesco.pe/file/oCRfMHctDv52afti7MeH-h-_cA5m1j7NwspSUXMNMLQHQNSGkUCnqtozIL96feFaNMHLkUjV3vtRkwoiG_8aVaO3nWjHSxeGYPQEfjXaNu6wyK5FgncfrifKt_lWrIAeKyJufjuGv13meGpcxED2491AgyrReStQjt9OZuP1CwJN7XKEUSHe9HTaKnv-zMzkf07atj89DgXUoOn627D7vDAle6Jme-wGCe2XOxi2Iq2rXY8EInYSyOan2lZ54Ex9XfC7Wy8EQMBv9zfNdO28hpNz4wxk9azZa_59zuiCFud_zkzEWDt0oxQgGe9Npxj6PSt73zQ7WYzDMH_2wBGAzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 534K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 20:31:06</div>
<hr>

<div class="tg-post" id="msg-101804">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpImD531ym9jpkB9QMNCA9CfFX3SUQS1ZvvvzQPPNragmer-tZbz4OstlRfP__thLUc6qr7OpcKTLMEvWkHzQ_fJJ47VzbW-LuoM2Ih6GELHn9gGOe6dJxcZCv2voW7eRvjOA_A39vry8ZrEvPCtz9lRrDttFO5RkB_ptQskb_4lEziyPjZMTf-HUIlcvvle7C1S9PtuI_5SrzVaLpICb6SfgHvG0_AVPFT9d1zt6BUbFVx1eAcv6fYrf8BiHI1wsXh_KQnrIQjwcUjnpTbudAt4Y_XZXXpCsOxlT4viu_onxYb6OGsNonUTKSVUUxcWW9nuFJ97dt-q8ncYKK2A8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
اسپورت:
فِران تورس از شرایطش در بارسلونا ناراضی است و تردیدها درباره آینده‌اش، احتمال جدایی او را بیشتر کرده. او احساس میکند هیچ‌وقت گزینه اول تیم نبوده و باشگاه ارزش واقعی‌اش را ندانسته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/101804" target="_blank">📅 20:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RkcUSJPywdAajBVBt0LBGKpnOslQw3d2gWhJm3y92NN-9-PTTkeknTkfoVfWgLKU1SquYO6OsiL8LxzU5T4xxBx3I5CMVixtAr8it2UDFP5KWoXEJ7XIbv4kpIYp72JgIMr3MzhJF63SyeCeOJlVdpyibrzXN_upGHIAgSDrDvXyneHnd97owWuVIaZ5epd01EBWUP3cMpzhqUIcF59fj2DRg1CaTnnRewWk2lfJkl21-ZqZ07r_4uLCr3u8TdzgZTTJ79NB5ZcvaAKN5O5AjxiT0YCOItkk5YFdCxLvoZf1qRgdGeL0v3IKKN4T6cwl9OyDrRGdN34Ymsm-_tmFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X9SLn0myP8JiKbG_qF6fA2GYEhc8tbKS6tsQUyjwYIR5cyc-haf34YY2vJ4UqetMP--abVcZenk9WKMKVVLPsuREAGoR59WCpWpsGFsf23ZJpkBxcZgX1c-5qL6_gzqiC-s6WL5AM4-wfD09mJSjnjNZUOsbZ_bsYfrFIJe3brTe7r-tCcfND0Fp6qeNPitR9zEXQkUjE1lejdRMNvWJ3NTagb0qXNLwBxH508Ilt9dDqAJbTD0hWwoIqygFXb2giPWc5e2W9OD1Jrm6KD7NCWuhgNRcTAAYwoMhER7VfUxZUDaCz9MVQNa1n-lsURc8E_D3WbNav39ROEm_MrJnfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدن سکسی‌ای که فرناندو تورس ساخته.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/101802" target="_blank">📅 20:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FajfY-5QDaz6m6yY6s06MIWWPtxh5fFdI_FC0dnRIDusHz8tvIx-N3DEdi4bU6kqhqkGd8i07j9bLFjVkvrHa0QvUJgfE-sS6dzqOSIA0-GbE48EvZwPWWErd-dj8XseV5Y7dy1hnGFEq45m0R5cEaat1_9AjPFZWJLoIXSvpfoDbVijCXt9dB0rXajzQ901hapfpwfRCXlB5cb4hK-w91Zss0sMjUkvvq9698ZyLMSJjF-Sgouu41l2JStXBY7dGK7UcCTeLc2j8jrhemTDRXseJY6c0us99sHeSteQqHQJUUEipBPFXo7vnRTfMvMbpOHVE_HonfjD-zjMS8M06Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لیونل مسی در چندین بخش آماری بهترین بازیکن جام جهانی بود:
⚔️
بیشترین دوئل موفق: 60
🎯
بیشترین دریبل موفق: 28
🅰️
بیشترین موقعیت‌سازی: 25
🎯
بیشترین سانتر دقیق: 20
🥵
بیشترین خطای گرفته‌شده: 20
🚀
بیشترین شوت از خارج محوطه: 18
همه این آمارها در ۳۹ سالگی!
🐐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/101801" target="_blank">📅 20:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYoeN-9h9KLX8z72DC9XwKCPZUd5dgRgLvpO-nyXSUvpUd8ynbutZiEBIukOPdb_F1bsGG7KZEw0aJaTbgf8V1gba6HehzbawAa36zCMDqjLEjOOOHwZJ0F_RlLUayYAQnloAQk9VoRG_iqI-PRegvmCj2fg_aCIIBaLUH1eXog_h39DmcvJ9P5cwbiDv_LHX5v9DA0XWPIg0DL-_mvBWdiKwZudLrxiTXt766zuQBs6ANykRQU7l1yM6aZJ5WSPlCjsHHKcp9eV6NBmdx8vw9rLeo_RvksEYOf_rmvvmEm8jtFv3DMxzaT_o4iP9NcOsJlNiSKArhJkdneBT20ftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
✅
الاهلی مصر اعلام کرد که روز ۱۹ آگوست در جام خوان‌گمپر به مصاف بارسلونا میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/101800" target="_blank">📅 19:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oyqw_xrrU-0-tM6kZorXwWoxh5JHTR4Aez_BfTjbT1iw6lkyNEhIsuxS0aX42s5UtgV8SYBfT9nM-0uUgrufYvTd8EppHYXNjr1BvApYWnVvnFpLyxfiwHe5IcMkNoHkRFVWEZDXJtzsRe_V-zQjVbpBSVfIFo5S89RCi4Le6FsM9CxqgboAWQ5dZ81kNI_YAbqoJIjqVBqzRoBuu8nqyiyWmdR7LSSyniYk2BH8dp3qewpPv1Z8oNaD8fRNG_VHI2C31VQXDikLxwSIsJd49qtIrROGnlCZxSLF2r-A1qBN1JB2Nc-rLO30FL3YeNvTeTbbhoy5VIvauKEelMt4cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
لئاندرو پاردس فقط ۵ روز بعد از بازی در فینال جام جهانی، با بازوبند کاپیتانی بوکا جونیورز در کوپا سودآمریکانا به میدان رفت! هافبک آرژانتینی از ابتدا بازی کرد، ۹۰ دقیقه کامل در زمین بود و حتی پاس گل پیروزی‌بخش تیمش را هم ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/Futball180TV/101799" target="_blank">📅 19:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PC_J6gGFX9scfc6dFd0AW5e1Q7gg4tL34dY8Kcn58gPrVZAmmuwnd1hftbMADkPRy5Vd7NzAKxIpRBi6YB-O8ikEdiEOkdZ-W_GRjyUF47W4BLnjQpW6KGzG6plg-eLFAhBxX2JF0KzI-cZHAhOSGW03tIPbs9FYOmbGoarxa9uu_T5AeVBK2ahAhI8Ztu058yirLfptMVgtpYs1iTYrT1KcYL7sxvvZXEiJ90D2WZ5RBYegkhievykP7ygTTibn2LT5g9Eku97wp9vZBq-IypU_jJq4nEqJtBVqeMLF9JDLBwZhdJRZmen2Lu8txclLmmF_B5fyxcnEP2s5xueQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
فابريزيو رومانو: پیرلو به تیم ملی ایتالیا 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/Futball180TV/101798" target="_blank">📅 19:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101797">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGotLQSyOfkqnNoUMEvUoM_raBjMJapylDhu-CLfLFV4aq54TzIK7DzoyFA_frkveJ8ny0_7Ni4ux7UcoNpLHJ9zEU2P-udpDM8W-xGcbH0-4AUR8C-saIsP5JII8MRBsH6ATA88CHWJstLZHZ9SMIbZIcMABRtgdYiYhhE2_kTFr6Efl5M8WoF129jXjcdkCMd7QPdxMQrabjoVkRM3J2mSGNeKnqYqO9jJTOmVaWWrNt-TZrp_GzZpd4j6vwT3sfIqVSOzrVe9XNvO-frarI0NPmMMmDpW3jLRQn7VvKbrl4MJkNzYCivMHyFmKolB_9ft0l-AmOq_Cj5fu5GcOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین امتیاز ثبت‌شده توسط بازیکنان لالیگا در هر فصل از ۲۰۰۹/۱۰ تا امروز (با حداقل ۳۰ بازی):
2025/26
🇪🇸
لامین یامال — 8.23
2024/25
🇪🇸
لامین یامال — 8.01
2023/24
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگام — 7.81
2022/23
🇫🇷
آنتوان گریزمان — 7.69
2021/22
🇫🇷
کریم بنزما — 7.69
2020/21
🇦🇷
لیونل مسی — 8.52
2019/20
🇦🇷
لیونل مسی — 8.71
2018/19
🇦🇷
لیونل مسی — 8.48
2017/18
🇦🇷
لیونل مسی — 8.68
2016/17
🇧🇷
نیمار — 8.52
2015/16
🇦🇷
لیونل مسی — 8.46
2014/15
🇦🇷
لیونل مسی — 8.84
2013/14
🇦🇷
لیونل مسی — 8.34
2012/13
🇦🇷
لیونل مسی — 8.83
2011/12
🇦🇷
لیونل مسی — 8.88
2010/11
🇦🇷
لیونل مسی — 8.76
2009/10
🇦🇷
لیونل مسی — 8.65
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/Futball180TV/101797" target="_blank">📅 19:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101796">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVQHCcx78PpN6lotQPJM11Hp_aPNe9kJGsi1yxqwGUsEYiSgqUWCwyQkrH7XOLLmasmgRYI2aOi1igpygeBG8LQX5S7x8cMoSuGeAGBHh0Ac_3jiWfom7Ffx_JOk1LT5d2YER9kJl8wrjPnczIUz6o8lu3l1UwoNd9N3zNmQrmrSRDzH0bxPSpsGJyII4qZ0RWGDgvX9ix_mF--TLalgotRmPhBqGl0PNnO6GoIrnBquxAqTXZGc5PnFs4O6pm3SWjc-7qVbDOGJ-5FiiL7vNzmuyKUlLM1NkaqbkYasf69UMINz0xaEc-_rQ0RB6d1QZzsD7BKyBEDCZwNx_be5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💀
مثلث‌خط حمله فصل بعد بارسلونا: GAY
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/Futball180TV/101796" target="_blank">📅 19:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101795">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrDyMCxWa_MXZ32hykJ3kGDrLWXHGOUeIZlhXbQki0rrBXTixQbgq9IEtlr_lfUN9iYg3KAJaXnmnMh-fpvjISR2QUSULRv6f0dSbcHF33gUgZgIbz-iDhcFLR6DH7i1aMm5P_jWEXNNIIOBa454Z2Tq7fHqPaJl11ULO-V6vGRaakt7KeTSMTHuo6kTC1jHc3Oihibw58WHcKtOHEYlejBnFewcTwpCSo77tEL9wMRJG0YsKTu1Sdhystl1r1vtCnv6ZzBFnoCUxFnz91A5SIXh-Xo50itJY9Rql88SmtC9xu6lncI4-Uf8tfhSkFuUc5v9imiiOF_gLdnIzqT0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
⚽️
بیشترین دستمزد هفتگی در سیتیزن‌ها.
💰
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/101795" target="_blank">📅 18:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1da4d2bb8.mp4?token=pOq796Rh80xnJeArCobaPZhNobOP7uZpOKANCReScw2_J47PqoeDPjen8TPPT_DnbB2H-1KO5P1epbbNuk5f9WUTsZV7vneapyiuIAVIIsUTGuPDuMrNYLH5oj1R3DMF1vsPXgo9fDLnrmXJNxWOpA8AkXyEoqjk7CJK-V_XaGxNTxWy1hc-Ot6KeBvrCR_cZxeOIoKl8Hy4kw8jIP9oqMo9-a1m2W06XJo7SLeVwUVClcCaLM0daeLLRF6n2u2O0mqZ3LV9ORNIb0gu-L5-j9RPzGj7qmgQPTXX2g9BRKCZ3H3_RmQRMTbk9P8pP338dvS2P9iJ4u4lm-FafLeyc2g5ULSZ_xvSJ3WGvJThB4eUPchVlR8LK9PEakV74iaHRntQVFB6AM6A3pjDXbuOQ66ONMtb5hfRN6oJSPOlXrXIITaS2iEKLAN2o5aDrtyTBvjetghk6FL44q45U0otP4bvoaqPHlutrUgPv-UnlLJFBaBQr_QiGbgZksAlj9kqVCAsSSovN7cDR4aKqZeVHnDNULq5SY8XD6yoRs9cgsfTHL96toe_022CRN7F1SJUjSbTI2rXkZ6BJ-ho1Ip1-rVX0fTXcRG2u-byoBQMm1VYfdMNK5yFKWMAbvwjDzulFh7NAnIHu_hNndcQ_SAqRYrEV0kTk0QFnKjjETQbtNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
▶️
اشرف‌حکیمی و امباپه در کنسرت بد‌بانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101794" target="_blank">📅 18:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b632e2b27.mp4?token=l4vh2cTPdYkcSNqoRql7WBLFiJ9PVr4UA7CnglN5IxzxRxvAkEGwSQ_Fooq7fbWvoJxoLUwcC4OCrgUdgTMqgEXxrxWJ9ES-9AV4tOuOvZoIgGrSOnPw3HvMCcjHz78Uykc3GJryM3IRCyt6YTGAuyisNwkTauaZG_Gv-hvM2u3UpqtgbSBmy_bnz0p3s88AJnoh7bxleBB2iDOplOSgyH-G59PUlU-fjZ1I9ER2pYEgP6cON3MPCa4u3oCtMaKKPYpKEjhHlWdq3uCq_plMNUoZPMG5Mk97XknHkgn9VQPA-0ApO2wi19kBZOULnLmnZervfrWSt0HGawHEvbOJyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسی همه چیش بهترینه، حتی میم‌ شدنش.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101793" target="_blank">📅 18:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e74ccace70.mp4?token=d4EVW9-I23FNzzx5qKU2lA7-gBnvkbKtArYroSytc5ouHntWB7EA6wvf6BeYnGzrPoRSU6YRtppAHXX0ROEiR5VhE07pA626Y35rEMuY0PPb8cDoY7RzxqCVLpPVpiLTVukf6zkq6qGy1OtkQ9tANoz3Qtg_vPFpXKaSTpwCpicA_xHCtF9K0LrkCdAsM7B11Ei8j4D-QzHUAJAVHrgXq25t-_5jqAL9UXaFb69Xue85yOmg33Bt_rUHzGVmzPzzgyWjYq7K20IACkNSP0NTJ6fg6rt1qV3BroRPCSPYXIXKarkSe39ILnvUjlA1LZosAIayY2dY9pNhkJCfOEB1JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
🇮🇷
عباس‌عراقچی وزیر خارجه پزشکیان: توافق با آمریکا بهترین توافق ممکن بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/101792" target="_blank">📅 18:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYT-e6E-u-MQjy5jlesN6aYjZUy7UV7dLQpMyZfNtlAiikbDHp1BDBrnt4WT8pD2SjnCK3Ezxtg3T0iB2S48B6gZ8PjuSV2Z9yRz7curEit_doV1m_FWcUZoAorl_B6A86fjyO6VzcuYshyVj1tuy2-XST8_xPwDjU1qFG3U6KEdakusTuD24iFwRJ5sCR0gth06buRh3WOkxjA1aiboyWbDebDijPWp5dcbru8lHjtqlas87rOldCwYxBPwhcAAIvr5k3AytPy8U_L4h8uXE7-9u2nHMupPXJS-EhsOtwppPJK69OmalaQHp3d6u4l1O8dQCeBrIVQ2fEGhbZkKFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
💣
💣
💣
💣
💣
🇪🇸
خبر فوری: فلوریان پلتنبرگ: رودری اکنون به طور رسمی یکی از مهم‌ترین اهداف فلورنتینو پِرز در بازار نقل و انتقالات است. مذاکرات با نمایندگان این بازیکن آغاز شده و پِرز با این انتقال موافقت کرده است.
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/101791" target="_blank">📅 17:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👀
یک استعداد دیگه در کارخانه لاماسیا درحال ساخته شدنه؛ سال‌ها بعد اسمشو قراره زیاد بشنوید..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101790" target="_blank">📅 17:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeTRckbG8rf501Apoe_jADIbMkPG5k6Jua-PY-EnkCDOs6HHk6CY3qoCpZ6zYHWE7IJldiBkxwDrOBqKEBPVE9ir_22wb7uAsYlivdRCyv7Ihfz5Sx3gkHavJFG9K7yvH10AzPG3IBO-cerMq2qk6XjtFiEd6U0A7Il1TM5au_ehYPJzeWyYrYuCcbA_wyt5CuLYkyskDcrhieguou3z9mWveARJwh7NtqjHNMKAyye2zDYYa02617uDVw9Chqp7vPovzDkvp30PgPoNKoE41i6ToDuvIW3TMfVIGGw_6_RriLu9y1BmOY5Yacux49jszUU-BDREAPFQ3JYA90PDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
✅
رئال‌مادرید به رودری اعلام کرده که مشکلی با عمل جراحی مربوط به مصدومیت غضروفی این بازیکن و غیبت برای چند هفته ندارد و تصمیم نهایی برای عقد قرارداد به این بازیکن واگذار شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101789" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFu2W1LxLl_tyNaYbEjhCnmc_PvM5h1NNvzARypqy6mlPA8uBJ-8Ea1eZ6Sa5WJUVqxL8ofGUVAXgjE7CR2mZFlHo2UUweNy0gIB0UOYWR2B2QZTkN-8pd94OS5sRqcwrzlmclHfAFRQa7MmBbL9_10KVcn0_xCjgeDQRrFf7R0A70KpDd8i6-Pn9A41GWMWHsTFXf707klsOGlXD9i1c5BMKJFIfyNvkCZiTWRbpzxvz_9oH5mdiUgOf_zE6G3SPJ2Uzj_iCxI7VbmXzu3HWGSkr-ZU6HtiM2BjBMM1DzRkicZkDlEN2DVDJ4kUF4QRK-CbJVjQ6yRW3mQ1AluPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UoLvPhfTBXH8cDlqwfcz8vaanrVkQHHSMT0rynRp7kx_ZDQgN01gnRty_xhdz_ACvHDZX9VCNnMb19dWEVRsM5VrvqnXMUYAwO1-BKDPxr8OxDIacXOoiaZU50S3H3igIwanC9d_hwegItgh6DCRXku8kDLjWMTdTATSFF0SoZ6Tb-4hdcXa7i-cQqOoKUiOlQgrDcyAlD1_P-H3mUhVYiv5HuOXOMr8TfWY5gPmYjFQBlYciJ3X75k1fSPVm6l8Ym6Sf8WwNPwjl6qSBH5uFS8KCcOJGzU-a3TBxtLn7XHiwettTWfhqBvmpZyBGJ_hUJtY-jfy6fAdNnXOoCW8hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مشکوک به نظر میرسی هالندعلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101787" target="_blank">📅 17:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzLDowtEaEwmYu3s6WFGqSZfioBM-EK6Cx7NMSri2YxyoBPqrWV6E9bXkM3oWdc7Ik2cGsWSUb1_bwFz3gLHLEqEXYPSjQtIF444adA_CgBBEtakfQWXiDSIvK6N8RprY2v6gSwKUb-pIS3hIyXqXv3OoJi2nxOOcitCz4DDnTsZNRQQMcacAEfKlCGV0vtZgEiL9cZX2y-q2Dcn6NhSBlyimeAzOBVJxb4mEgFxTNsG0--VHSj0hqjqh1QYNFPVC82c8NYJziPfd2ilLDlpzt-i6y35f8A0l1IqS7JBwXLDCXC4GZvI_8ItS9OIL3yhTRs24QfxSeZugBdJSzviag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: منچسترسیتی با توجه به شایعات جدایی رودری، مارک‌برنال ستاره جوان بارسلونا رو زیر نظر گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101786" target="_blank">📅 17:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101785">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101785" target="_blank">📅 17:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnoKGlEEvvZ5NJFspNoAQjhWZrDLmQ0UtXD8-pauxgeiwt3bOBCyD-ju3orc08yW7d3AL5Z4ZUG7mCry7MK_7etdT9Z5raYcVxQGVM8ovKWp-VN2CaSVKbwwTQ-grSdo_OX2YImWoKwx3LquG2v_yyG-lQiqPhOljFqpuQPF1-lrOs9cZk-zvXGIVsYOXSnVL2e5Ov4uq7W5XYlUWO9AFzsCsjZsVmo9eHBOGM5zxqHEfm2-bCI0EK22v6rMX-H6tGxj7hQBoRzBeIsTGoy3JsaQ22wGIkBZlY-tzp2DGDYZpV91kJPX9YOM1RqYwFlL6N9tRMRSUKBHnLJTxvfx5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇮🇹
✔️
به نقل از گاتزتا دلواسپورت، آندره‌آ پیرلو سرمربی جدید تیم ملی ایتالیا خواهد بود و این قرارداد به زودی نهایی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101784" target="_blank">📅 17:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e1ed1b860.mp4?token=J4QWih09MHfgPTyYr-n9u9BKOZMSTHSIYTeOrZ9HIc6CS6Kg6pJ5DmQp-rLjDKfNhlefaAXW4WwTLkn7-oE1nMySypOzKlLbJ3kIIXPhCTzrqDtkb2Od_sV9VQVPkwWF-wq4qK-DLU4id1FLsyhcPgpWRwoNEjtQk6UFWrWCMLDoi9hyIynjlA1i4oWlNM_7A0MpprLRG5jLBogHpBQKqro-GAm3rVqKbIbDh8PdiJv2dn9TKa2nGq7FlreaM_sm_x8B6ZObctOAZHUJGo3TVX7gWoASXR5wKlafqjTbuT7IN9s0hT6oaVPXJClWY5tB0J9faN4VebO5u5eDsQZ1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
مهدی‌قایدی ستاره تیم‌ملی ایران: اگر میخواید عاقبت بخیر بشید، بچه‌دار بشید
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/101783" target="_blank">📅 16:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTBsOkQ3od8OpQnPP1ReSA57N_P4zA3cvX6E4_47rWgDICUfeLa7aJrbZNsGNP7IhEFkjc2m8YI0jyblU7GZ5ZEPEYJNP67esFSiLH80IQQoxE8xh_Lu62c7a758Bchakh0hSIhSjnsHWm9nlPtfhXKhn07a7U5gPF8p-dkmHqbMgzJP1MxvIhzXl3H6-XpB6D_qyLdKjwvKBhG9MjOILTj9d76UC9INFTLOLEXx_G9Z-xp7uXZQOVx039tgOrkVF1wx7ykvg1fu0v-T672sw-ebn9nPQZ9toxoRE87TdmSDX3YXe8s93BW-SSExcOmEJetoy7j2XXHRt4I-6C37WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avuIHVUerGqT3mSBMqqFQ2qNcGXUK0jQ9y8RZ-cE2Ml-6M3feHXBNZoN6SRInCGz8gouE5OFDMdbXrG9w-wWwx39akZszjcEWwcmkW5wC7AcwNEwsR8tDIj2G71UDUnFbPWO2wsSWnU1H-9SXlENDSFZHtHwOiJnVxAYtz7JjljRF_wpuJ1LNu4wN2S4OHP7ZKGB_Nl9-K0ifnC5fPgxg7TMiqheqrFqgEKX7TAEmeK9QcfMtbpq6RO3mujyzDWIg-BTgCm-6Jy_Ygyxohmt0hSV5wWQEovHjw-gAhrGSnY1a_tpJrCWB04ESEQ2ssMrFZtIddTqQbsWPiSImF9zow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
⚪️
امروز، ۲۶ سال از جنجالی‌ترین انتقال تاریخ فوتبال می‌گذرد؛ لوئیس فیگو، کاپیتان و ستاره بارسلونا، با فعال شدن بند فسخ ۶۲ میلیون یورویی‌اش توسط فلورنتینو پرز راهی رئال مادرید شد. این انتقال رکورد جهان را شکست و بازگشت او به نیوکمپ با استقبال شدید هواداران بارسا، از جمله پرتاب سرِ خوک به سمتش، همراه شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/101781" target="_blank">📅 16:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnAkUc-nThOo_Ybm71LUIaP_S2Z8WbRq8UfLzEq_OirViGJ9XR06foOk8uc1PAzIZtH0T18fxhGusli-_ErHw9k974m70MAz8o2umKBohhGMkTlDtdrIzHcqKdh0D8ANGJmppAaZ1R2BnK39RN7qU_-9ZlQ1C_oGRz2c9u6kWHbcx5ImRwpjqvt0WyZIAU2uzem6b9OTIVpO_U0KBW2HOUf8qYpzPlPJd3ezlNLuT4pZFbmgkoaawOwd1Jo9IbaKr65LHIzS8cH2-RvmV5LMSxVpwtJAhSzob-8qQKMDhR0tqiKgjiqxpgZvSqY5J6b7mPIalsjymUzjuH3_rKizgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینتر دید کسی حواسش نیست رفت به یه تیم از دسته 5 آلمان 16 تا گل زد. دوستانه نیست این دشمنانه‌ست بیشتر.
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101780" target="_blank">📅 16:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f574b376.mp4?token=T-PHeDxvqe-N1-ysGLI6GTbSkqq3KrBJUyzlLiBOrSN_6R_l08oDEpKQZzbyzQplXyakoQV1IpjejStcsCFYb8laXZZ2ZVnC7rNwJT19t4WQAoYCnc1GOX9QxquEVwzU6P8BJis8kvd-VDRPjPAfWAmj3E1QfEkmX-vB3AZK-DSJrUOQWFW62t30__T6PPPslV4lLbDRdd-hDL18eDjuBXqrN3D0A6GnirJDTFygAodgnADkviALfYxyLG40spNXWs53JRADDb9SYf21yFZRq66Hael1iJw2qLJBVmpSRRrBcoW4HS_sAfvi-To5nZ2JN97YHl8GCvP2ByJmT8qfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
برخی از سوپرگل‌های لوئیز سوارز در بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101779" target="_blank">📅 16:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3068c762cc.mp4?token=WhgJV2xcVNmNCvh6dbPDlWbwRCR7NGQiomw891BE9Hs01JUd1_XqthrGDcSXfE7SbkOoAs_G0g83DIbIuTmIHXeMLOgClZzd1KR1AEd9v8NBe7EdBuIrUPwVXHO0RhCKhFc2D04C3dJbP_L7sOE9h4z4EW9NI4IAqDzzL3ynoEgKdecfLSn5hPDdJH4Z1DgpSRs9OvkAAIRjSG-8voL785cGuH7MfR2-o-_aKOYKz6q9rhv3Ot6MVUTyunE1PoDOTLcfJAABiF2qYKTYsCQtFNLTkXvLq2FHUMMXABnDUKpyg5iuRBOsyww5ST34go0yEngBYRWEKbIU3mlyrGo5TDOD6wexGj-0mOcKbhf7U5qksx-PWkX_eZRPyQh3s5X4MNfKVaeY13HvyvTu2Rt6P_dsys3tQ5AWLP7cx5Mt0FLG8_zzxNoIaIZx91HYs2Bq-fZ_Zi5h6imYLC5732i_l1bbRAkqwIiOkDrH16fo297plfAnyikTgehRVD646SZEmcauXYawE8TzSe_rCEMpogBxFGpo3fZ04sO4wx4lqOJ7iw3Kq6wo6NhE0KsXULxNptkDHf_Pjg3x34h4ZGQRasMdhUObzeneNbbyC3oC6Jj9BaGu1zuWVZnOFxrUBxBcaYFzYIyStjJ_4FWUaNmCqw5L5j2fqVMg2_CCrTP8aik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
چطور در لاماسیا، مسی و اینیستا می‌سازند؟  اینیستا و تشریح سازوکار خاص‌ترین آکادمی فوتبال جهان؛ استعدادیابی در سرتاسر دنیا، مطابق با استانداردهای بارسا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101778" target="_blank">📅 15:50 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">▶️
👤
به بهانه تولد 49 سالگی مهدی مهدوی‌کیا ستاره سابق پرسپولیس؛ تمام گلهایی که در در تیم ملی به ثمر رسانده را در این ویدیو می‌توانید ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101777" target="_blank">📅 15:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfurPxkr3b3GGrFzNcrw5UewEl_jYP9757ujNvUnLRV2hbQD6PnvKtS11LXsRaRyrI82sZYc-tLWOG6CrFXTdM3eSD9qfRmMD5p8Ka7OXDwbRa4vPlpYvtdRKHUTQg9TcH4krxXTEG2Nhdro54r2YL-jx3or2-hI_GzOXDArFsUXHm_ZDGP8bLZtNAxOyjBSCpgZ2uWZ8TS0hN2-i8IxpOoqKJVNuyUxrhSf3fwDGQ4I6MeMBqUDsoPyloh37i4YvknNagheTB9T1ndAk2fkEmEuJvbIpwPJxr5KLCsf0orN0Iu2VFR1ERMkCeVZ7IWqKUF2PFDVg2MFzszi2cqY5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇩🇪
یورگن کلوپ:
با چیزی که خیلی مخالفم فحش به خانوادست! اگر به خانواده‌ام توهین کنید، من می‌روم. اگر روزی فکر کردید من مربی بدی هستم، مستقیم به خودم بگویید؛ همان لحظه بدون اینکه حتی غرامتی بخواهم، کنار می‌روم. من این کار را برای خودم انجام نمی‌دهم، برای شما انجام می‌دهم. با وجود اینکه دیدم با ناگلزمان و توخل چه رفتاری شد، این مسئولیت را پذیرفتم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101776" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz2sQB_9XbpS2IFCYHNB4glIn5QlaxpZCTvZd1hID2IVMohFsprEopYm8RhotiOvIYQeTe-9kDWqwtzpXRgx7cb2UwCif4imS8vSdLiKwXj3XX7I2PqYl5nnd2VNjoEzdDVh_yLD2o_LA0O0MddM45z-E9KsifxJFVvL732Z2ADvh0OEIH_AXk9UVDx_XGVP_zaT4na2FS4T4t32P3pHw-qULSlqlE9Hi5ePz7-JLwdz0Tw_XGutHeKAERDs1rjVLacWoIMRH1_uvzd7kzkqcvivj0mcI5BpIEJrBmPrUa15qqsoB6-OLx7xIHwl4oZ27AC-QjdMJc5lTUfcbmp5dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
دنیله دروسی:
عشق من فوتبال و رمه! اگه بازیکن رم نبودم، حاضر بودم همیشه 10 ساعت با ماشینم سفر کنم تا برم استادیوم و تشویقشون کنم. هیچکسی هیچوقت نمیتونه رم رو بیشتر از من دوست داشته باشه.
تولدت مبارک آخرین گلادیاتور رم
🎉
🎊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/101775" target="_blank">📅 15:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfxP8gb1t-vA6Eah-xdhVtumuSv18iS7aiaj4EaxyvPFnBmj6hsOuHmcyIYdtKqDXQeSTOJ0wNwC31stTxLIeiYz2d2Hcawik5-RW4wizrYNYroWfj7IPDo4wJEIPsjJXauHVCwBlWr4LBAH_2XcNWKEp1CiYhAfD4ceaL9d9BeVHUnBDgp7fSOuh6qzgg4ezptuIS5jKPONFYrzTD0tjMgGO4blns7HZfGgaWqA3iohK1tHqhGK4m_gTLexZJZOAKA4FdDi-lBkPrVSGXhvkyrtmsSpodq_zx3viASj9npCeSaCYBAsCHCU0_FcdXN1bTvN-1VoqQ_yihMdr1ycfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
قرعه کشی مرحله گروهی لیگ قهرمانان اروپا 27 مرداد ماه برگزار میشود.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101774" target="_blank">📅 15:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101773">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/clueHMXRwImuQOT7jECUiS2sSI9KyajBws4zMzuOU7di_HH-zTfgV1VsNMegsGf71CVq2lGRN95e0c9dmq7_RGCxg6RvBKImR5JpMwKW3-cSSpsnFTecwn2fR_7LlfvZi7pgTzy3gt0ZHmsMUgvtNjvx4y3Kx6vfo4niPMe9UWb_DaLIAH2zjozplrNHHrgwZZtgr-iks7fA_COGUEL2ADoutHs8msj95dakRBgL08FsXJJhMttJNAKccJQ3rmlyw3UFNTxWQ5LH4e3gpw-NH3Mnt3tMQZ4VbDasH6xUyvDV1wk1wBEVoD5ZYDB-eWlwKBTHfcQJrR4axd1uAKrqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
📊
مقایسه عملکرد نیمار‌‌ و امباپه برای پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101773" target="_blank">📅 15:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101772">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZk2dWg-5cR5S753TyFKFgrwh1sSjlX1UGvi63GZFkcvNy92DOoHaigoC_ay7M4_LMGH_4Nb4jKpU0nszgoJInh4OGOk0PcEEmniUuvoHWi3FLtIYzuS8XewzQTCbDw5WF84gLVvz1roGAjxzoZF9PTplVWfPB4H0H18-xZUrQb5ATPyXmrNvvAuGQSkMJt_YqokQXD0ZS_xaRhqwBZ5vnlqEUVibizDTm8Su6iGMLyhRF-ZHdKHhy6fMhxSRkixbO_j7-x7vYrr6jOSJ0zmlFXOHoXOk2T9dUHKJoPtniufH-F6YFvkYko2WWSZr3ZVQdEoE4zI18zEoQ4epvvzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101772" target="_blank">📅 15:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101771">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVk1rew7ouBTwZkJHy2bdPCBeOd7wU4Se9eu95wc6dLuZk7lzD8Fo34DzmOrUWpArsTFBE7v5TOqy6eQVSCRUWgYVC8gUiliwecVkH7YjqEJObMlgJ6SYoNSca_yLlcptn2204WVCbbtozaUl4k4wkN2R8VznE8BFJCpjuT53_PRfLjnSqRxmNj4KItr44ikIvO9wCm4xTryzico5e7SX1KfCIBdNGC5jHS38va5o0bwqGWQhvKrgWvTH6OLMzo2OTGmvNHWQOLU5hts9SPDGjrulMriR_GM6n1VAZ20Vv8YUBcvjeOQsszlAku7612UbuZcKCd-m0LLNSAjqlJoxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
اندریک و خانومش و بچه‌ای که خانومش بارداره به اسم کندریک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101771" target="_blank">📅 14:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101770">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmaI17uaAk7T7jxuNTe-cegAhxTm9iCQL2hjrebPTMGtF-ihqiopGy0D0gy4Ree05S5QPSZQUHP6eyXtAtKMP3nt_dfznwjdMGzDhIha1dCHBhls_90GZ3ycQi_KhgibUwnba1Gdnb9gj-GXL_uI7M-r_udMTGpC1boWEScFYoHQ9xRGNMNkgmFAccR660-mwYStyoulgniEMeyosGAri-KyJsyWPPHhVlii9LqTDHuNrggLCXIuYAwCML-4GDz0W_ZV5on63AKKje1Vpl-7hE6Y6LOVJjZgvkJzpuzexJ6kAyvQj8stcIl6gGHWUYj3b2BvDO91k-og19aza23iPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🔴
از زمان پیوستن به بارسلونا، فرنکی دی‌یونگ 416 روز رو به علت مصدومیت از دست داده که با این مصدومیت جدیدش احتمالا به 566 روز هم برسه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101770" target="_blank">📅 14:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101769">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/accd9e1667.mp4?token=RFsmCP2SwT8lF1giaNRU62B-VM6PdNLr5dH55JbfRxdL47zPeK6qhbDH_vyHzm2dpPKVbq_Qnb3mi6-ZtdH-B2jz3ECWcS27nRt2KUwpSJTQhUDkkceqmnfpnOK8M0nKGFKU9Q2B6S5Jwon3GxRvow8ChAivf76rdlyhSle7N01hAtUz2liXfLjZwtgTsbUrcZ-2EVYt2DruRR4j4bFV_fm0VjvgF_TXoHRbKkBn6UbzkUj7XXPtt7XREyKYsovaPMKPwvtSbWaS5dAG3w_djFaylCHQrOqiJ9tfr_BVdpbxxRavd8sUX9j87zDoXTWRa-59yVJIrXI2BUQfO4k0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
در چنین روزی، ۱۶ سال پیش، ماریو بالوتلی در جریان یکی از بازی‌های دوستانه پیش‌فصل منچسترسیتی این حرکت عجیب را انجام داد. روبرتو مانچینی آن‌قدر از این اتفاق عصبانی شد که بلافاصله بالوتلی را تعویض کرد..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101769" target="_blank">📅 14:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101768">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b6580c49.mp4?token=rhyyiYW5TwZG_7FwBZm0_Z6WbLBvgmYZnGPDsqTGkgcsdtc8l9y8qYriRBCeOfbyjZqaRU1gL2ejKKDG3SqSUU-KUflGhGeMPBDadxG8VS46L9nVUTIzagIgf2fG_m40b6e8awaz5pZ9fdcMqVkio4af5n_pbyOYIiwHQRnwQEUZLvGicjQkZXAbOkiBDpISfagJPixmH_u5Nr3ZLG10-eRIjlXIMCcLc0D2-pUsycZhrMyMStuv9PKGztOcImnVDtLOPAfaSpXd9j3u0Kddy1hrUpwu5wO8tBzDSnj8_zUFk-FdMdV5KPbIPtfDId4nWkeFdgMaGEqWqb6MNdQbEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
کدگذاری به سبک قلعه‌نویی؛ واکنش قائدی به حرکات عجیب قلعه‌نویی کنار زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/101768" target="_blank">📅 14:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101767">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhpcgCfdosoUdpGnn2bEYJNnZk6ySyBKPZu11x_Gb19UC6KEAix9Ms8EaTfm7tiwEBjgxBpBewze_khKr_ZSZF481uhpx77ULGpghpipRn2Dac8EeokLmxbZYoMrnjbpjp0ug-_lVDuu-nJp0DILoWhfGUZkaA2v84ib7bdzNP9VRr0wzsD91rE9vYk0PR3c4KZ38EU-DZquMSX5jQ7LGZ_UGLdcXrPg8UXUvDGXVm79QWc2YNtSLDyIsoM1Qr7QJQwMIrTS6gcjfllzSWs_WGRHyon85apCPxd-RJ9JcsebrSz_agZFwu_Uv7gUwrIVvrOEGDj6wpJ5fHepB7qRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست‌نفرات چلسی برای اردوی استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101767" target="_blank">📅 14:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101766">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f65adaacf.mp4?token=ltonaENLPwoTnRjhq7MWU7hwv6DlqhbcKYXK8SlWEtCugMn5YOzw9bDavLr9ICJSdcKvNuGESxtqW3-iEQmZMaRFORIwB9EY8xCFBZJYPqiSvtzwZR1RZmJcuw_FbGKkG5oc-WwmcgEICgtMk8NWb2WMT2LlHMf75opI3AI7y_b0kuj6rFrrJ_OiShNR980dVBA9kOmB2LsC3IpvNI4gn7TDCtIpVE6RaPoLLMobkXAA4-Si-uC9VQyVCm3Tu06AlINbdFSS2K45jRv-VJImC7Ry4blM1bw62Heiycywq7NNdGXfedZ6nRzfamZHGHgNYEI2DhJONKC-YTmUPCxX6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❌
مصدومیت شدید یک ورزشکار در جریان مسابقات مردان‌آهنین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101766" target="_blank">📅 14:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101765">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ea14c8f5.mp4?token=sFnRmRh1xmYOvJ7JYBWAdFILhexNPVhvcQ-HxSYG8rUzKAv1eDrWV-dxYJhH-whWUYbnk0ZX1au-ALdwGZTUjJ0JjzeTYaXW0sAlAc_494Ew-96CoqMj4UmVgVT8QpRPLYbISJKAr6pb8Z1s43aX0dqAxiI3_NrqMI2-_YIiT8SKmnWDffz7ir66sOBT1Cxj8P2idWNpG-Yn4lLOoucossj0YLDH_pxJKOaXbxdi4QfmEqfL_t5nWvI68R5f2pu7TlbUWgHGADGxFCrzkLqJkjQex_kOuDG7yPoR1V6NcbVl3Gtd0iwpmXSxy-K_wYjDwxJGZU3Do8MtKGlHKJcT2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
😐
افشاگری پشم‌ریزون اوجی وزیرنفت‌ دولت ابراهیم رئیسی: موساد به من زنگ زد گفت ۳+۵ چند می شود و سپس خط لوله هشتم انتقال گاز به شمال کشور را منفجر کرد!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101765" target="_blank">📅 13:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101764">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a128d814cf.mp4?token=Y3s-6xbjrIvS5F_KqhqFcf02JvvNvav4QADN4HEAOC-Z1baBwl291AyO_9oQHSKXllM7A_TS4GMU4SIj48fjGnk8gwABiiFhhBZrp9t7L5DdwpVPWyLp7os7CdGSzpLSDIFWXPXdYKKXNZH1IvehjXUET5Ij4twq8GEY0WJ61inMYKQrCvkvppltK1y15crZoq8OHQJlrtKpvSlhGdn4YpticxE_8WjZ70smBwGo1ZlBxamn4hyjfzNtPb5gBvrkl5FWD9t4bqiVNBPwvqrZCjhVSOR6AsVJMXHPTXdKHnX-kOg_b_L3B1Yr8j0sIkQ5fe3tvwXa6OCDCP3GQekXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🎙
پیرس مورگان، مجری معروف تلویزیونی انگلیس، بعد از باخت آرژانتین به اسپانیا تو فینال جام جهانی ۲۰۲۶، دوباره رفت سراغ انتقاد از لیونل مسی.
گفت: مسی فوراً دوید سمت داور، مثل یه بچه مدرسه‌ای که می‌خواد یکی رو لو بده، تا باعث اخراجش بشه. به نظرم این واقعاً چندش‌آور بود.
این‌همه از «سن‌لئو» حرف می‌زنن؛ همون کسی که می‌گن قراره بهترین بازیکن تاریخ فوتبال باشه. ولی توی فینال کاملاً محو شده بود؛ انقدر که اصلاً حس نکردم توی زمین حضور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101764" target="_blank">📅 13:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101763">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uo7dPkxJHJExPnczQqFzZDSBXrlNZfvtHOB468fihtHcDVVgzb3lGDiEUaVZnq6LNPn8btUabfNCtJLc1zV5kbXpDpblqs0tr7tCUu9BxEGxuH3sar0gCET1s4rQCoVtrtvs_5pYrxnCWZL9xbMghTgk082eimqQzqb6lsnaEPC1w74PkkCeQVeLF7p4z9z_S4BHO0QBO318M9v3FR4dTOAvAzEwa1QWzgBxyYIP1975xV2RjTYdZxkCOaYc5EC2lBV-YI2jhcu1ZgmENmoS8dikFqD2IFbp-bVUFg2zy2P4SaofvbgCL6W8vt4c_JWdmhfKK9Z6V7wLpkHGAodQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🔵
براساس شایعات منتشر شده، قرار است یاسر‌آسانی تا فردا به تهران برگردد و در تمرینات استقلال حاضر شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101763" target="_blank">📅 13:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101762">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/632f699042.mp4?token=B5PtDtVGmiaX4EzxzWXSqU9ekpidDAy1dwLO-odKdQu3QYzRBUXn2mtD4hX33hfGQ3yLm9pHR3tfjefIiW3QKtE6eK_gqIu6rNzC0O-leIDQ91N4O__b4GQMIavaTzdM0tn1oH8pXHKdKLA59xsx4QXCri06wv6PxZPDK9WGK4NlF1sCgxqIx8QPSHmzU90_Jo9EUBoOmmj6sBXbxXF6UQ9L1sfkvNNOrzR4nX2Fs7DC0acmZtEy50uxSkdDxPDMusNdZtrGHYwFLzg0m91_qjr2f0V9DoRdhRtnBLmD-gDaUpISD5n1-6t23MIqUh7ip53KTH69hB0-aBYED128Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: ارزیابیت از عملکرد مسی در جام‌جهانی؟⁣
🎙
لوئیس سوارر: با سنی که اون داره، میتونست بشینه توی خونه، اما با انگیزه تمام رفت تا دومین جام‌جهانی رو برای کشورش کسب کنه و تیم ملیش رو هم تا بالاترین سطح بالا آورد اما نشد. فکر نکنم کسی گله و انتقادی ازش داشته باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101762" target="_blank">📅 13:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a535e73d0.mp4?token=EMPcfzSSFpOIX3BRp5D1Iuh2TfuFHS6Fhh1-p-oU2gxPvetolk66kQVydo57KxbKJYYCHV7ixJf2HuLkXcchm8J2ejcVkGDgDgXoQ_RCI6g34MaLNaVWqOpcLeFqsztVCUXIbhph38-pZ5wp7L3-g6Gxl7m3aHXBP0xSEJChR0BKPHp2IcvMq-vY_t4IhI2gJjJbWVxsAcJk4GMlnuqM4qyiLNZ2GcsTxkrLVOcszeWFhoR3mxuhh_BHRW_eYzeZxaDqgQ3xHSDAEQgngqVWhMPSjFXbw3u457shrVzdWrwXJgdT_QJAyHaBaJE4G0eN3w_Dlk3V2vI7eMFnyR70fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
هوگو لوریس درباره برنامه فرانسه برای مهار مسی: "یه دستور ویژه از طرف دشان به انگولو کانته داده شده بود. کانته همیشه باید سایه‌به‌سایه و تو شعاع حرکتیِ لئو مسی میموند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101761" target="_blank">📅 13:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adad22d87c.mp4?token=H6ZZUWMFhIIN3VlPquU0RVs-rz-RyUBjOGaJV-S58ISBLiW5Sc-6n7qtFKAIW_0A6f_WLVxadqSIVaoxoOY6a2ewqiOJSkRiSYwyvMB05o2J68DTcR4-Y6dMkLxGI4-XorCbVYPy8re557QfTcOcOgte-pi_o58eFvqYO0vYoxcpfJvmOhVwHTyP8xp0sG3fvdQnh3ylDNCTOkOzvCwzco_D5rCDJ6lXVz069ibYF-jYYHALkdpdpJ2bA34KO_zI-au3zO2zIILh_z2KUFXukyWN_L6kQ1JT7xxt841-Y5W0hYUk4GCeIU784ArGz5Ky96zwBqSyfcpxAzMpdpUcD4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
وضعیت استادیوم فینال جام‌جهانی که درحال کندن چمن و بازسازی برای مسابقات فوتبال آمریکایی هست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101760" target="_blank">📅 12:39 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHavaanr95a53tSubLZaaEMUmhbHP_Lkuyf-KL4bOIbi0CNRlBcTsxoYDqqyJ4vbQQnV9juRKIX9vwxA4YlMF31wpzLaaEdw3Q0zB4q0okpWFzfddeGI4gwvFVYNEBf6hdQtev6dFf16fIuxzceKjXqkPmY98ORqfjJ7u3vtTdF23sQf7xnzaKVclGZILTujmVrT0SKYs-LcR4D3YpV1BVxCH3471ubIKAK7sfRN0R7M_vMVzTp98O0mpP1O2ttAZnA_Jn-mgBVCo2lExUFqQr5ErLWN9jo3DwfcI2oOVSXR3X6o7YJ8dWocUAlE_LvX7Fz3Oyi0LcsWOI6aJFf4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فدراسیون فوتبال آلمان از انتصاب یورگن کلوپ به عنوان سرمربی تیم ملی با قراردادی تا سال 2030 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101759" target="_blank">📅 12:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIfVj12b9W-qBv1Wzxszh7x1IJz6j7f4bxxf8IkMPEVIPkbNIZbGpRpHAAsAOzPQxWX3mgv_d1B44NCUCuQqqC4i6oGUzh44wbqTvl666CrqRkUHOnX7CWC_T9epORyMAlh3vqxtpagI6TwUsP57i7tOH-BWqLma18A5EzkxKC4w61tfStAKifhVO4nlHhcacKyiDFtD5mbctCy4C5C5EkbEG4IDo2INdRkmqx1HnjNyKEHx4hNdCOCPi4EgTzxglsQViiqF_eU2oeg8rRaCM8-IqANmqPEUwOICol1oah3Jnpp2xOEH-CqEfxtd4z-OcmKEHsvtxAqkOk_XzZbwNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فوریییییی از فابريزيو رومانو
🚨
🚨
🇮🇹
🔺
پپ گواردیولا پیشنهاد سرمربیگری تیم‌ملی ایتالیا رو رد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101758" target="_blank">📅 12:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d513714e20.mp4?token=evlQo7OIToGBuvHs8kOKkHu_hXMiAmgwdBZc6ddmtRG4n4UER2C1r3z7JLnzw0kn6zRykjvLzSy5tNHy6a1VL3CWsvDBHmC45FDA0CnMVT0MSJWxCisqx4e1FC67T8wrYmjN3QkHHnxxjeiQG9W7Lxgy2rKg-iB2zl1qHIz8mYZSCUtM9t9_AU_qd9RKugYt9K6VOjQB-CYf7rsh_47MpOVUC0I1861ik3PMVHKhhd2rpCwmjUrgVPvZoQJiU2v4tXfAXz0JVCLhojaJCjDhDNTSVu7FH9KJDmUn3Nd69IEcwLuS77FZqmIPYkYkZnFhT2Co8SHdZAeULyM9uN4lHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d513714e20.mp4?token=evlQo7OIToGBuvHs8kOKkHu_hXMiAmgwdBZc6ddmtRG4n4UER2C1r3z7JLnzw0kn6zRykjvLzSy5tNHy6a1VL3CWsvDBHmC45FDA0CnMVT0MSJWxCisqx4e1FC67T8wrYmjN3QkHHnxxjeiQG9W7Lxgy2rKg-iB2zl1qHIz8mYZSCUtM9t9_AU_qd9RKugYt9K6VOjQB-CYf7rsh_47MpOVUC0I1861ik3PMVHKhhd2rpCwmjUrgVPvZoQJiU2v4tXfAXz0JVCLhojaJCjDhDNTSVu7FH9KJDmUn3Nd69IEcwLuS77FZqmIPYkYkZnFhT2Co8SHdZAeULyM9uN4lHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
⭐
فوری از فابریزیو رومانو:
⚽️
ماکسین لاکرو از کریستال پالاس به چلسی پیوست. 𝙃𝙀𝙍𝙀 𝙒𝙀 𝙂𝙊!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101757" target="_blank">📅 12:22 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=e4TMYTdMc2De426WorTynCRtNH1TcZkdm65jJd5aIUgteJkjIi8slT72qHNUzEED5TqNBtSTjsKp4q8kbeAJzRUUt-Z9rcMX-ohqig3BihDqSVTNgRA20t-uBBEhKO_uTaZ_GPNvUeYi3w5Qrx7-HjwD0sSE2LnAhiBc5YRU5ES5ZBUkeT-v8iM8118h_Si9MbIepDrrCXWlPem-lYQaNujJi6wCUuUF-_Qpmy4Ium_o9s1W5-BkuWOiCImwYTPzNiXwbAmRU2Q7d7gFZNXXzOnw11NsKmNrIudqK_1Ugh_jRUx_HyJF2AP6tu_XEHug7kHdaKJvyr6mChv1GMpnNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47d5bde5ed.mp4?token=e4TMYTdMc2De426WorTynCRtNH1TcZkdm65jJd5aIUgteJkjIi8slT72qHNUzEED5TqNBtSTjsKp4q8kbeAJzRUUt-Z9rcMX-ohqig3BihDqSVTNgRA20t-uBBEhKO_uTaZ_GPNvUeYi3w5Qrx7-HjwD0sSE2LnAhiBc5YRU5ES5ZBUkeT-v8iM8118h_Si9MbIepDrrCXWlPem-lYQaNujJi6wCUuUF-_Qpmy4Ium_o9s1W5-BkuWOiCImwYTPzNiXwbAmRU2Q7d7gFZNXXzOnw11NsKmNrIudqK_1Ugh_jRUx_HyJF2AP6tu_XEHug7kHdaKJvyr6mChv1GMpnNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🤯
«لی میژن»، دونده ۲۵ ساله چینی، در حالی که تنها ۸ کیلومتر تا خط پایان ماراتن دریاچه هنگ‌شویی فاصله داشت، دچار قاعدگی شد. با وجود خونریزی و شرایط دشوار، از مسابقه انصراف نداد و با اراده‌ای مثال‌زدنی به دویدن ادامه داد. او سرانجام مسابقه را در زمان ۲ ساعت و ۳۵ دقیقه به پایان رساند و موفق شد حدنصاب لازم برای حضور در رقابت‌های قهرمانی را کسب کند؛ عملکردی که تحسین گسترده کاربران فضای مجازی را به دنبال داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101756" target="_blank">📅 12:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101754">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqBWT4_cRDr3GTNIs3q3sXifufC4TQe9TiaOO6_ieKBqDXKimbuS-KCYhm3iIaMlWDd-k5NaoermbZqqNGmRok7N8M5JN0sc2mQSL_U_J0KPcldPUMGLOQrTeaGYdZZ5rjOgsdrU9MTSyFr3pE34Joe_M4LfkqjKuYaY_VReLmDhJBSrvw0jPr1WUp6tdrqW1z_5YKtKLeGDMOht5TnphAcy6IM09d7A6o9-d8VsGH3MglZPuPlUpK17aPfCQWMPCX4WCaI4BjiRjMIQIap8AiEO4Z-715LUYUCIQT50DYm1Xzr3YD_87bQfnLq7jra46wLWqFNvtrN3rVtTRkOdfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101754" target="_blank">📅 12:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101753">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=h73ceEShK8cFqWkW0cSVvwUyjdzb-F5HxjOl2upMe_hoAIrAqwm3091Rm1LsuGtWhOPeijiPNsLBl117lKPU5wtw2JjGZwdsIsIKrkzcV0I-vwFC05CJ6IhbAPLhoBN-nbZQ0c6ARkidaCPwcGDzvoBtrume1nPM-LAtUwKw16B-R6wvY__kUgog0tz2jg-yBbA2s-JhsREf-bm9p_NQctZpUcOibiOgEC15qoqhKIqhulXwjsHB4Ni5jesJZVSD-0k2aVYjuDXQ39Z2LjvVS5gNDoFdiJQArV7C18Pk7-HybxOOq08lv9jsthL21JNcgZPYiH-nwY_FHzv_yyK0-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60409e4f3e.mp4?token=h73ceEShK8cFqWkW0cSVvwUyjdzb-F5HxjOl2upMe_hoAIrAqwm3091Rm1LsuGtWhOPeijiPNsLBl117lKPU5wtw2JjGZwdsIsIKrkzcV0I-vwFC05CJ6IhbAPLhoBN-nbZQ0c6ARkidaCPwcGDzvoBtrume1nPM-LAtUwKw16B-R6wvY__kUgog0tz2jg-yBbA2s-JhsREf-bm9p_NQctZpUcOibiOgEC15qoqhKIqhulXwjsHB4Ni5jesJZVSD-0k2aVYjuDXQ39Z2LjvVS5gNDoFdiJQArV7C18Pk7-HybxOOq08lv9jsthL21JNcgZPYiH-nwY_FHzv_yyK0-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
انتقاد شدید عباس عراقچی از صداوسیما: صداوسیما مصاحبه‌های بین‌المللی من و استقبال مردم عراق را پخش نمی‌کند، اما شعار «مرگ بر سازشگر» و روایت‌های منفی را برجسته می‌کند؛ گاهی با خود می‌گویم شاید اسرائیلی‌ها در این روند نفوذ کرده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/101753" target="_blank">📅 12:02 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101752">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK6U88tAN9G1AEsWcQudYsMUxp-PL-Ya4wvM0oaP_CkH7_4_cmrrh7WjDAD8qlw3fPCF8g08MfyPqTN-z7EvVa0nvun1c_eXYqt3_1xghSIq3jtiey3FVwNFTUsiZbasqUuTwlG-BqULaPNnarOfSSVtXHU0xz9gJocU3EV0hkxOGvFqDnZk8Kw_IjdIQhEbSR6G720eprsWZ0waAx3QYvqG_pIYCY1XUZDQbG2DbeV7qQgA8mO10wVo7LwMe6PhPxJm6YvU4ixmqE9ycgXDDk8yiBUN-Fls3hm3vpV79QwMUSDZHFZlMvbh1ZXiJN8WTnhfCU5D0_gZj86yR_UR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
فابریزیو رومانو:
اینترمیلان تماس اولیه با نمایندگان کریستین رومرو برقرار کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/101752" target="_blank">📅 12:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101749">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3u0in84B-Q3mTi36zQie2pgaqL1XOaB-ZqNE0J84UNpOCBc932Q6280gsrVCq19OU7fz0YkQc2soYlezs6sOlpiKVK8wQCOzZk8rlq-7hAFBMnJezuAJwB0GgJdBFKTigDVV6b_vebbXx3bR_4_S1iQ5c0f3w-eKlMsK3q06y6w138b9JiZt86IJCoAJNJxHRrCjng1kS_oyAaSMi6XLI_2pHLIQtmHuIqivhn-RlAad1d-uk23_8zUQvSKepUkgESdF8R2xtyFf67-1UOpm4Fz2BitPtTwPGMdG2IoKZe-452YNnJG089aWCFI3ED0XWwxQqMH0qUUPl8762NWug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ien6WpNXXZ5UJVkiQQ3gjX57k2IgRhpnHTh5E-gd_E6RuethfUOaspunc9Y9LPVxaRgiR9YuzkOhKVMFkT7ntAw1AOddl7N8x8h0_nu3UjPsuGAkc-zJYKWKo9M3tFR9bTPrGBNbX3vjyvNpNjPa8nL-FzZlu9gNZ0CMhpUcREkR6fyNevV4oqn-BuoS_e8jT4S9XM4BIuGs-s-AMqcn8Kd3m8kMBM1jfkWhp0aua0kkDtrGfa4iuvWKrzdJ2rnnfQChXikO1IBzeQUcdtGCJc-lm1GrsUd0-fkyfk7fnP8GnsbByLiyD5LWuQ4zOAty3KKh9rtqoP-p65YNlXaL8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qtF59rLPnm2wLsfoVMoKNfY4iaPWLrgNcEUnEfy-fGcLKlE5Tkj3wevwFKjN8kQL7zeWwUHuO7wSVr7YrBIHYQeos4R6MNvv10PwbzlGQiDBq5cQSOJsvZ5e811yILejKqtInbiPmBVFykrSa0SW6LejZVywY12BpAhj_yEHgZguRgYIOFMJ_rprJ2qNgqehjWWuXgSna77OSUHBIowRxMH3f9k-DAkP7N0c7FilJSS_yJQbR4VE5WIYAUdFB_B9dvmknPAXtJgDbmRKgYdcbnJ2mgE215jlyMVt2Qb_SwYiGLh-bp4-Km773LNtm3ms8A-aqt7oHGJU9tzrDhAT9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔥
⚫️
کیت‌دوم فصل‌آینده باشگاه نیوکاسل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101749" target="_blank">📅 12:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101748">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbrdhjMK9BIiQLMQl3AEsb62gOEHBQX_57sYMHKA4h9nlbGUL3PC16er9c66iqrm4UNV5rFKXMG3KUmu5NY81MQnFkjv_vIGeRBfc0IfI-xPnj4R8cQve9nm9GHXpdYAK5pkHAJW2xkiDRgzTM08yqn6J-BHiYhiIWPTNo7ep2ciHZa0_7nDbiUiVu-nDDTkuV7wW0sTYTB1sTrj70a9SZtyO-cXbBAYGwJk0dQkzVHoYmKkjaCSXsxqU0XxZjNGfD-dY-VKDbj9S89gKxYoXxABVhItmH-Jm7nC1sxNPXVPQlXotKUwJSiFGHpGpw1BiYXVJSZ3x8NqjlUD7MRELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
لاگاتزتا: فنرباغچه ترکیه با ارائه پیشنهادی به ارزش ۴۰ میلیون یورو بدنبال جذب رافائل‌لیائو ستاره میلان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101748" target="_blank">📅 11:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101744">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpmO3Lp4C9XWRkTdqt7S9Kdck-y-IRIQHWVgzb00JWHpvvSq3uurEAFMDq1xi0fmEZHOmGTjpDHeOLCMLAEi-tjQnL5khmecKuALNszfmSPsj6jEXVDyOWl-CADCv8X9lFEajmkrxjPlk80v16_uDmlRgVTiZ8Joq461AtOwWR3AlmwQkfbzxk3Jcnk8-Q033s0Qu-uAksMmCs4-MPY5yOgguqnYbbPmp2CQfW2LtCUngHm693xjU_88VZhSScwB8-EBH_RMDNzj8KaE8PuGtCWnrYREB5Ly1oDXkN5TIZ9DI7ObnomVAvykaXkTlE4Uy5r2iqNSXs_QS6luFASRMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qI1vfVy2sQ328FxdK39L2FgbfOY7MBmHvAR1CspZhPqb9jMR2JxJBm6nCscQH-I_6mtbUVSfxY-tDQ9L4I6RYZkh4IqVwtn_xlrV55NPRPvKLt1qR4pseON623Ne8b97Rj3zwoi1x6dNi_Sg5qIm-zrRdTfm6c1MPRsohNRvrXmArGABgZYujQc8gLhgY__WfJVq8TLxpHnpsf6T6WA-EWfwEV86N2ELE7xQNM2JHqrxA_Y2WkDF_jpBkIZKL7-xmI2W6F6_xZv9hpPdTDsrLamhCryHXFPI9AToCDBPj00M7x786VX36C6whFBkd7QaJdWkDvJNPM8lRVlL6HfOIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Acc39XDXYBetclkBKVU5lDIXlh7XgAfmNQsk2xkmhI4VUj6s9R9wJtX1lMktVTufm8TZOXiPnm5eTjGnYHx5JmC58wTaxZdY4e7plUDBB6gz7tQaqckp0YklG5vZhwzYUyyqAKcAAq9MWAfNW-BHZnDhg_iVQo4Tc3PNetquM2CYmw8OLWzeValpzyj6s99fNvJ-qCIZdVD8yFxtHHLyoizAQ3TiUXZL4ovRy8mInBXegYabFONHprvb1GEp8-d58_Tq4dWMtU08ISx2PEJCV7qhacFsAiMbiOBm8TDY7C6OyQCFXX223bfRBwgPmpLVZvzgv70oYpj0n9q8loh9vg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم فصل‌آینده باشگاه آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101744" target="_blank">📅 11:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101743">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=WujEp-W98e7O1yZ1JztRUpQeu9j0ImK8HqUXFLr1DGsLSoSIwKDsyL6yAHqxeqYN0wLutmTWXCNx1ih1uPY8g5w2KOAwCgl758o3zG2co5udUnIzbMFmjFWCdJLn61mnkPHQtqVunSr64uckKKF0uMaXf-wuY58BjqT2E-DSuF4RVUvnKou8GmTGbSeXXFnz5a0-eS0mcX2rQoYpZo-2xFleEM4T1nWoDRimBjWQQxSyml1MJYRzR-RpoOZ0sTPFioPIQn-9cx0vLmEY4B2W3tlslrgG3rOvimNNNXcJPDgqWLu4NZ_xcES0zs5h1xaD7JlP4-lgpfROdHs2DLOCzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a0b08e15d.mp4?token=WujEp-W98e7O1yZ1JztRUpQeu9j0ImK8HqUXFLr1DGsLSoSIwKDsyL6yAHqxeqYN0wLutmTWXCNx1ih1uPY8g5w2KOAwCgl758o3zG2co5udUnIzbMFmjFWCdJLn61mnkPHQtqVunSr64uckKKF0uMaXf-wuY58BjqT2E-DSuF4RVUvnKou8GmTGbSeXXFnz5a0-eS0mcX2rQoYpZo-2xFleEM4T1nWoDRimBjWQQxSyml1MJYRzR-RpoOZ0sTPFioPIQn-9cx0vLmEY4B2W3tlslrgG3rOvimNNNXcJPDgqWLu4NZ_xcES0zs5h1xaD7JlP4-lgpfROdHs2DLOCzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
کاپیتانِ اسپانیا در رویای پیوستن به رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101743" target="_blank">📅 11:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101742">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=dQ988uZ78pA93loFpBttfDQMyGySWjqyaWnnfw18fyv2rlw3a3bwi7j9d47g1IrhEBbCfZwT7RyDRwLR0W0Jg80blKn09jU_nV1u7ywWiRvo7yuXkxN4CJ9TM2U1Hri8ggRGARojY96Dj5wi3nu-nkQn54YhkLTucsFV0HROO5W4QT7N0R2g77Ew1ngjq2HGiUuByuII_NMx7kX05eVZl_zcKLPBRr9jTvM-YmDtK53gyYyS-ffO0_-4ZX5EP9b4GrzREEmpwT-AS7RYxAyuAAz2ywdON7SReE_Y2-jURIQEFb-DBOzqIR4cYX7zeWferEiuGnyaAMMKvXGtMWVRGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc95b900a9.mp4?token=dQ988uZ78pA93loFpBttfDQMyGySWjqyaWnnfw18fyv2rlw3a3bwi7j9d47g1IrhEBbCfZwT7RyDRwLR0W0Jg80blKn09jU_nV1u7ywWiRvo7yuXkxN4CJ9TM2U1Hri8ggRGARojY96Dj5wi3nu-nkQn54YhkLTucsFV0HROO5W4QT7N0R2g77Ew1ngjq2HGiUuByuII_NMx7kX05eVZl_zcKLPBRr9jTvM-YmDtK53gyYyS-ffO0_-4ZX5EP9b4GrzREEmpwT-AS7RYxAyuAAz2ywdON7SReE_Y2-jURIQEFb-DBOzqIR4cYX7zeWferEiuGnyaAMMKvXGtMWVRGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⭐️
🇪🇸
زوج طلایی اینیستا و لیونل‌مسی که از بهترین ترکیب‌های تاریخ فوتبال یاد میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101742" target="_blank">📅 11:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lb-1VcOKVpwKAY3CZr-Mc9d9b_3Iq-DEl7_W2It0rAZp5lRT5zr2SBtE4wWJpZuDeLrJdBhGsHfQZwBZM8QLNT7U9UGQDE8YqUvEqV6USy1DAXom3OibKhPY9098lSXxsCvjr7vlp0SCEgyyHWcPEIIPn5ex5CdiNywZoJEQA6TV25_0x3hifVy5SU_TJNxz-BECeT1oaWMgGdAU3rh5EZ0-TzWVT-v2UzpEMd311iObt6CZbD3dyDK8r6nEdPIrBS0xQADVZLBHPB0r-NU7E3JlG5_EpIe3EwnNOylFGM-Fu_R7TdgelfQp5r4ubRRIUWPo8OwCHKsYEswrq0H-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XkprpcwzVCjw20QChOEnii4aHt5H-nr9_ZTydxuA7oqPyNVnn-CPdImflPP70pSjNv31rrr1m22bpgbX2WcE7xVco2WZ93RH1WclXybyHkSFBHymtBVeCFsUZ1rz1bkPkiMtrCPkKdYSeUMUfN4yIcaKgYJEK7w5sA5duQg1bMQ7bgUIfHPdVcxZ1egVg45ohdwS1phqUUWlCdWap5Baycazcdo_FHBAs6z-R4VWwalRvGBRsYf5lfF3uZNbWZU-Gmr-wImN2vZNoQzNAScQ0Yk_UjJX-w16w6gN99U6gDt7eolzZ075fnRrgBxNhSh5HlpSND39QoQ5SCde2R-bIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m6MHLZZeCXTEd804Zy2FOKWin-kOcBXm5t5TlXWTbmV3UdU5TzUHQbjx11LsrNHxYv0CyozsoQVg2pmicw7n9G3vdXN2W3VDl5bMw3dkp4UwgyM8X2nXfVFZXHLYcNzmKB35fh9MYnp8IvqyGlj34IrI61nSvurpuSc7wYUGNkl5OLMA4TzUL3r-SytiCd_xrk0uUSAcRiexyN-sNpqy_pDRbMBPOjcFtNI29sLBusdxirL1bJUWcpz_WRzbqZZ7PooxvvEAb5O1fK1X6nRNtUW0F7eU6w76pUIr3QUuhr0jkOsP-xAjPjo6qXAwuKpSU97aObkBy7kg-FY2t3jT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/raYDsj4VrIQC8VY-81TsCTMzUiZLi8hSiOkRThR_a2oIsvrhNzpOJCG3Jg5sT8PkPZCKkg-JbAoKo-TQ4zPar0LqRwyyYXmMZejU1DegQKOeIY90CC3a6OB9C94P3uQGOyZUG_OlGoHHKnr95i0CGdzjcJc6CZVPgMpm7uw5089M5gIUmkBPoRC8Ux3w7i88CrPmbjTdARIvZWKdh0p7PeVp3xoMYQ13rf290X3qUzJnSkadGWLAxJ3IVDLwg7jbLwwsh9epMK3mzK_JIYYF9FDkTdYwkfZjm201pMCa33lHb9D1kQTmjhmkieXkBzmxS0t4-hdyLQnyB9UM9sXSAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVvi5HqyZPzfG0to6e6PLN-cXLCiy81H-wqre_oKDcIhJcZ28yYnnIQc3Uxq-8d9ufDL6zQAC7gGOJoAK3wJ2KIgsTRtSOAhQJkIfztXEDlCv0lN-RlJbrmssBp65bDyOr3EK6AsASXzB1yn9YMoQfbdlDCv1XYJ-Z65uhXJEtlgK526nf9N_YLOl8XpCa2TXaNheqh7NWobxTtGpezGBTOSBtRQXmU1qErRPZCFzJWIBCZ_1cy6q7aVq9DHHn4ubWfSlMv17qs4RZDRrlq2ft3q1ZB5AjzKfXCXeyDV82jdAnCPdtBF4Fevr4AkZgVYr5avi2jU-fKASpL09cGj9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E23OWoJ7tFaxypS-OuRRZLzIZ2rpAvD-dGtUFwRVScNMkZxRRVYkNRpxJ0wNNlHG4_1VtDA8a7L6lNPBpErzNCTibFRCDP6q49GONnfeABhr14rdfjUNLVylZgdKsGR6YnZOPxzrlaFGiRt16cUvLVNVq_lkB1Rq7KNFYrw7qXj7MunVjV_Ho0J814o3_XBcB_lUYXw4YNsXXnvkbRFE8_4PVA7wKWbKOkWZ5tHzNSLCx4kKYpYKSZOtBwuKorpOeHm9Oelq6CygOCxHzQ3LXQQLLh2NimrH3wco9eu9PBb9xvoiZ8Fi6fo_Fl6sO3c9CQ6CRoZYqsk3hXJVX0JWfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vF7qfozXegUDOqhSM_QYIXQJHY_0rKQ8jQQpD0q9cEk9RN5-IcdyTwnTrIPF3KFC1XMeSgayBZTKsbsK8VIiw-K0-2ITVhkgPfder_0jM_lqjZQqIo30vO9peybFwacCmBsUFBh9W3C3IlMoqEpwWdf-nyNbSmUD3BZQGsIsNs9tt2_j-4fBihz5SB_H-7bKuT5rteeonmdf7gd2hrZeaM6JvZicY_6jlyrkDe0I121xpR3HwU_B5YgBDGkYzMGi2mlJ-DNmy2OguXA0mRexqKVyVns0SIOqXNOrTgQNCPfJlAPzhvxHcBdsCBYylNKr4BHWpmsoJaGAL-zpSRciaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iCL4JUcS1d7ymHwhbE1a0F8KEyiqWSPzz6zMEQaAelopBbwrXuI3bLMYbYgXPAP3iKL1_99qZLuw6K3nYACKh1q-uySYBPvcMSCKM1c2gNmcrtihsj0Y-3OGchM8rNFWtKJUjzULpBt7_OeVp-b0WZBUgdYcx2OFSqAhvqmGi2aWz8zDSwEAnTDfxK9Od0hVogyAYE8HN4uz1C_n6lBj9PYL31iw4LHIEQ9nixk-xamDaU0M_wuYAltbsVLQfzM9uNTKtuT5K6KflVOIbk-px-EMk5wg1ir3qiGgEsA8FqesZeBbFwak52RX7j7oXWB13_byuA_fwykZ-4pxnj18Jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🔥
کیت دوم فصل ۲۰۲۶/۲۷ بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101734" target="_blank">📅 10:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=hDlC4oS31kF4tniETCIn2KLnwIpUqXuq5Gq5Xlpx2bEuI42Dz7eYASFtVh7OGqpOW_IIjdbhS9JlcXR9lh4_QnoRI5YsZWlYwUH3iWuVy-gvrhukOxjGM8XFDP6INBrqT-q2cN2q7cq7yAs4Er3dqcBlXvG-z51VEHDi6cXq4x_8tn3RarqRWcYYVr2kTgIPuWRs4gqBwvWTZQKlujqBhTAm2e9toogfNxSr8jcRHB4GMxVvRHYjbVxx43Rb_xJCMJIR4_ylYvhhR05zGHgRc7OTGUC14a747JRWIs4ZkFjhCLNgFnyjqJ9TnIJ8p2yBArT5rEOd9S1MfKtsirJBom8h36E93aTuuKwX_gmAnGo4A4fspumkDcuv4PD_A04GeBa4YRU5_PMSCz71FdGE6ArcSYazvIM4famzgOFXyzfIHYipenbZp6k4RuvwMnV_Zpsr5OtwmzpuI0TXQ0lngvvr8McZDAp6xntZAtfw0ZEjNCApeXacC061vro72xnWGi8geJYhdywi0f65ihplodRczXDcmVNspEtF9MCUWwTweCZpicpLgRVqrm8lpfnYeT1usGdd6Jzm_TnXc3HnygeIx1wJP29Vfy6IYsPH-n3yhEdgg0AWMI44afSBiT0qMo8-12NqyQbVdkJR01ln-eBnEKTOr4qGHG-z0uW3fhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae0f2a4c9d.mp4?token=hDlC4oS31kF4tniETCIn2KLnwIpUqXuq5Gq5Xlpx2bEuI42Dz7eYASFtVh7OGqpOW_IIjdbhS9JlcXR9lh4_QnoRI5YsZWlYwUH3iWuVy-gvrhukOxjGM8XFDP6INBrqT-q2cN2q7cq7yAs4Er3dqcBlXvG-z51VEHDi6cXq4x_8tn3RarqRWcYYVr2kTgIPuWRs4gqBwvWTZQKlujqBhTAm2e9toogfNxSr8jcRHB4GMxVvRHYjbVxx43Rb_xJCMJIR4_ylYvhhR05zGHgRc7OTGUC14a747JRWIs4ZkFjhCLNgFnyjqJ9TnIJ8p2yBArT5rEOd9S1MfKtsirJBom8h36E93aTuuKwX_gmAnGo4A4fspumkDcuv4PD_A04GeBa4YRU5_PMSCz71FdGE6ArcSYazvIM4famzgOFXyzfIHYipenbZp6k4RuvwMnV_Zpsr5OtwmzpuI0TXQ0lngvvr8McZDAp6xntZAtfw0ZEjNCApeXacC061vro72xnWGi8geJYhdywi0f65ihplodRczXDcmVNspEtF9MCUWwTweCZpicpLgRVqrm8lpfnYeT1usGdd6Jzm_TnXc3HnygeIx1wJP29Vfy6IYsPH-n3yhEdgg0AWMI44afSBiT0qMo8-12NqyQbVdkJR01ln-eBnEKTOr4qGHG-z0uW3fhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🏆
تمامی‌گل‌های کیلیان امباپه در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/101733" target="_blank">📅 10:40 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=U9qiCsU09TN7Di4-5hjXSmjxd4-iCRSbrOd54ZcomOSXpf1yX2B_k-WMSd8FgH44YW2iYyKHBP3NdiBBXGbRtQAXFES08RhXYJroFa0TB_UfsR0yX9ptx3VG47yThE6DVkTUDWhgcIH9yGFMulSAgCGtOK_EYqbaNufkmVfw39f9zQQMIZ97nwgrKS1PDTUq1byoTGkPWDMg9L4E1VDcodVotdRAeADQUH9QaVPbiU7VVfkXQK0OtZXowDPEsJFeSVh14DhlpKmkfW5y0pWXFDLlkmvaRTJuSL3OPBFG_DwrggE3GJncO2vAxEIyB5DClXVF1wzGdKDrN996cdnh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eabdc39afc.mp4?token=U9qiCsU09TN7Di4-5hjXSmjxd4-iCRSbrOd54ZcomOSXpf1yX2B_k-WMSd8FgH44YW2iYyKHBP3NdiBBXGbRtQAXFES08RhXYJroFa0TB_UfsR0yX9ptx3VG47yThE6DVkTUDWhgcIH9yGFMulSAgCGtOK_EYqbaNufkmVfw39f9zQQMIZ97nwgrKS1PDTUq1byoTGkPWDMg9L4E1VDcodVotdRAeADQUH9QaVPbiU7VVfkXQK0OtZXowDPEsJFeSVh14DhlpKmkfW5y0pWXFDLlkmvaRTJuSL3OPBFG_DwrggE3GJncO2vAxEIyB5DClXVF1wzGdKDrN996cdnh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
تفسیر نام اتحاد کلبا توسط مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/101732" target="_blank">📅 10:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=EgGvIEq1V38kw0PFjmzy3FT4nb5bDT_7SdiOSN4kROtSU1sg7nb21-qtttryN85D0Bh2RRieO_amAIsuB_HWKLZo6r3DKHZFKVh1jHX9gOcE0RA-srpNynL2UGEdyid8K9C_kcpKBVYqpERAXC1w9RizPVuO75ypIcBWu90DHfJKQeBiVYwpb02j7LNa77ZAdYWX3buo7tfUR7Gg2HtjjPjtYXUZTlVyeOIWaFl6VWl0aZUyLVM5BkV2owWxxpNBJMvEd5OTX2r5c9wXeBtheDjj6wVwBCSr7BFScb9Z_UJcUH5J0mVHlibyNy7BlL6aUqGuoZBqgIIqZ2O6jkZfmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e10a696be7.mp4?token=EgGvIEq1V38kw0PFjmzy3FT4nb5bDT_7SdiOSN4kROtSU1sg7nb21-qtttryN85D0Bh2RRieO_amAIsuB_HWKLZo6r3DKHZFKVh1jHX9gOcE0RA-srpNynL2UGEdyid8K9C_kcpKBVYqpERAXC1w9RizPVuO75ypIcBWu90DHfJKQeBiVYwpb02j7LNa77ZAdYWX3buo7tfUR7Gg2HtjjPjtYXUZTlVyeOIWaFl6VWl0aZUyLVM5BkV2owWxxpNBJMvEd5OTX2r5c9wXeBtheDjj6wVwBCSr7BFScb9Z_UJcUH5J0mVHlibyNy7BlL6aUqGuoZBqgIIqZ2O6jkZfmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇦🇷
صحبت‌های یک‌آخوند حکومتی درباره عدم‌قهرمانی آرژانتین در جام‌جهانی!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101731" target="_blank">📅 10:01 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101729">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8pEmz3dpK24aGtPXeHHXknCYaFXJUOO44_M5SpR04Mc2tBKl4jv3IrXT3LVDx9-x5C0Ub_vZ_-1nNdz-G0cJXQ_ie89EmW76GDdkQJKPHsBUnWutkZeSr2NDWCC7YgWme8iNR-kZnN6ZIv_y0b6qauBhHG92pQ3Eq67pLcsLx4-kOdPHIQrnGS0oaQlAMfN_OrKtKTLj5azl4Zd7FBSo-qMxDaJ4zh7HOVywU-gfjybMwf5xmlSsEAh9yKSc_LwZNtRqyarDs_K7a03tTpGNbX3DE4cQzROGpPriS1r1dRYFCxXg1H9MbUQn8SJls2iHqRJILaKum2gvJutq8a30A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boMJKR0oPe0sMZ4ipNlfaqgzLIdz7fqzomxUTQshdIc0BenjqnlQNRJZGLIJ5iiGRD7YUabD5ryGgHA_ppcUftxN2xWeRopZt2RQ13YmFc66oOzhdY1dkWZR8aLkrmUmDdPKaZ8XCsJstNIgSZZt7k0knPVADJMq9GExUR_R3Uc15rGetAYwuYCdbjsFnB89ExaU_OGmDnQwCn8S6DClbBYXLhbWd7-P-TrTpmL6chtcGIM30hGl4G_VEWudVnX3IE8f437BWLAmF7lRCNQzhWyT3B3lJxSEDt7Ep1M0SW9YI5qChIi8rgygOSIKTCidi7iZYdoMZiyXob50rz_qww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفته میشه لامین یامال، دو هفته پیش به دوست دخترش یک خودروی مرسدس کابریو به ارزش ۹۰۰,۰۰۰ دلار هدیه داده
‼️
این دو نفر در حین خرید خودرو با هم دیده شدند و عجیبه که این هدیه در ابتدای رابطه اونا داده شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101729" target="_blank">📅 09:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101728">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7ciDXFeixBefJ1q2HE5Ddpy7fmiySokXlVew7sWOqYqAILgP5uLECXrOqGJw9rMg0ebZlNJpbOXvb7f_FXxqsqB3NlXqwphlSjZyWkZ89uIIwJUhfdGPbJIFdXNKlYCCMYCwJ1Sdgv0tALETxJvc8NFbby94XZNZlW-QwmT2NcY5EWa_eVBPmBPb6XoU3ictcavGQ2A9OwH9m1OGW2CrQXrGhSpInnmNknCT6zE9kyjqZVID0LsRaYtHaCIEdiW55vnperxXIgnRhoqd1WneKOT7Lq6wEQC53RL2V1F2BqJzWzVfv5CgRjmKtB6mAgCrOf7u6pSMCSQoR2Zrly6Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇦🇷
پاردس: آخرین بازی ملی لیونل‌مسی مقابل اسپانیا بود و این بازیکن قصدی برای ادامه دادن نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101728" target="_blank">📅 09:37 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTlfUfom9GJDJYOeWyYDsc0EkvuKNrVWUEAfXti585XAXiHwz6ddVYwUeg6IO1eK7ZB1znIcXt7NV1g97iNIrWjjpbPI5P528M7blFuuNY80septgCO9AvFPmLze4qQYMA4_fpHclsx8MI0pSdnGzr8-rw3dS4QtPuShVEPWJsabT5FV9fMcDydYYX2NKNceWtmlmw96Gcg5BCkGsL2JFMXcDXemymkiOM-urK77kohcJxaBSDW_sgkln6DXaKWjQ-9IeqkIh6DOh55tmvnpxpTYa7s4wpPMvzCnb_QZUpnEvnhuErrVx9SBQQh5UnwtZEzj9FLMXa_ezmIyiqmD8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔻
الکس فرگوسن: "آیا منچسترسیتی از منچستریونایتد پیشی خواهد گرفت؟ در طول عمر من، این اتفاق هرگز نخواهد افتاد."
🔵
🔺
منچسترسیتی از زمان بازنشستگی او در سال 2013، در هر فصل، جایگاه بهتری نسبت به منچستریونایتد کسب کرده است
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/101727" target="_blank">📅 09:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNYHjU8cLgHWjkqfh0DSAwjR9PHru-Am59aL11qcqoV2JhqPbteG5VaINKvmthSP6K7uNMccHl2ClJUFlTBbI2EiiiDwbYdVkAvIIT9N8Y9hBRDhq_3tgT22fLyeGRxSpmTdRNMr-AANT1xqE6H0mjDucw2FDDTsR-Rum9Ra28VPqF-iBr7OLOlruekg8pkFOZyyQzRgvd7cA_miRwY8TTbXnSMdMJkvXDq_hmVe0nZ9jCZ2x4gcVB7tSulRP1GDWP3GG48BKxAdAh4WDWfOPpkOx4BIEwycv9wiREiqmrndPttbEdmk51qC-nNMvlIiqKQvkHbPPJlqAwGK5sjAVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏟
✅
تمامی ورزشگاه‌های میزبان یورو ۲۰۲۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101726" target="_blank">📅 09:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6JDiC-c_jkVNKp16BVLbCAN9Y1ZzupC-gKDhf2PFCOdGmOG-jqJp0gnKYSM6TkHVO1nMyB_82cxBg4YUfNalzVkPx9FHYV2RmIQuFZMCNbN24F-k6PRFMwqZJPDCPEn0H0fC7eR3HM6ZoACrhMhBOpcc7vlw4nzh71x1H5sSXjGI38mCoP-AYRnckwnP8vgjybwttJYGmxdqjOP0NwxufG9sQ4UfDJU6F53jevh_nK5vHsHivdQvq4V6lfOP2EJZoscFh-lB_QVmTCzg58TNERTstKor7JpNXdjxtYQI2-jpb7P-4RYAmavuuk9fNFoWpECaWIYZhhTSqtBVkHzxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇻
👀
کیپ ورد در بازی مرحله گروهی خودش مقابل اسپانیا، 0.28 موقعیت گلزنی (xG) ثبت کرد.
‼️
جالبه بدونید، فرانسه و آرژانتین هم در مرحله نیمه‌نهایی و فینال مقابل اسپانیا به صورت میانگین (Xg) 0.28 رو ثبت کردند.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101725" target="_blank">📅 08:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPbLZJ-460VhgImiCSyLcZLwT0Ksc_hFe7UUYTGtB4YfZLDWf7FzZFoU0ERUuBYGBgg64_jzmdkXZmPKvyUpK6-T2MzU5g1okfrgjZ68mjqnSiLccpaXKezlIF3_JthVqIXcFsfT9bN7Z8LSvxJ2Nj1h2YN7TMRuK9N7r5lWVW2swGv9pYSnVMg3FGr8y0o3l3F_ST3AvsNz-AXX335OedjX2tLZJ2TE3ztmIgh9HWS8iU340dJrMy5zZwRI_E_DihrCkBuavU_0XTZbrIaYnZVqfRyPDnQ6qt84MJlmhkPufO0ApltQ9odXUfrsxHVuVb5iW22yJAfuukdFmuBedg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
🇫🇷
آلمان و فرانسه میخوان درخواست میزبانی مشترک جام جهانی ۲۰۳۸ رو ارائه کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101724" target="_blank">📅 08:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2s-m0NG1vCHpBPh9KlmEZs6oj_Yxo9Pb_Lk8NepK5uajP8HHMdAPtjb6jStBkraCo93rWJLXBHEENUaxylBU-lL5nOeuXxY3YZjYyzYJfGz_Wje21jWBQZLy6BoLQSF5zjFe1dgNpIBxvqCeRelyI2pdQyWU3Qt55uhEoQ0hcBZbrwM26fVyvJiGJVR8OAbT9jSrhU3REqiUZA4UZt48wsKgMvObs3dkrobBwEKsc4MlnCwWCutkV692D0kyF6wn1sB3-e6CptI0THN6gRHw-EXKS-mVP7-sTB0W4-DvYGnEb4kjs1w9CMPOb-hpq8tniL27ZTV2CtHgLC7ty_faw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#
فکت
؛
پشماتون بریزه که بیشترین مبلغی که آرسنال از فروش یک بازیکن تو تاریخش درآمدزایی کرده 35 میلیون یورو بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/101723" target="_blank">📅 03:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=BJo6NT4GoGEUq8Tmk8MFNYFLVjnNGMUZQNz-vH3-hgFMKIjQTIaW9cg9Wprb5-s1QP6E7QTn5j3RzH693KvXuTQ_vzzImjmU5rCz6_74oxiIziRTnnXawho-nZi9-KMcSBZWtvpc8hlfiR2DKev5H_jf52Ze_TForNhYL6XnGgF90qaQeJ2Q77_HndsIQR3MyJRXb8T-onkWWKBQPEND8KsJArloZeUy9SEgOKmEUD3YiU5Hd8OUKojHevuJdXfW_1C67lMPRv1LeYKs7KkkRwWTU1KvwGh1WT62k9Zd5IdxSUXSSGW0fnRzJ-95mbTl2ff_cCUlBkM_myjf0nLw8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729338e3ee.mp4?token=BJo6NT4GoGEUq8Tmk8MFNYFLVjnNGMUZQNz-vH3-hgFMKIjQTIaW9cg9Wprb5-s1QP6E7QTn5j3RzH693KvXuTQ_vzzImjmU5rCz6_74oxiIziRTnnXawho-nZi9-KMcSBZWtvpc8hlfiR2DKev5H_jf52Ze_TForNhYL6XnGgF90qaQeJ2Q77_HndsIQR3MyJRXb8T-onkWWKBQPEND8KsJArloZeUy9SEgOKmEUD3YiU5Hd8OUKojHevuJdXfW_1C67lMPRv1LeYKs7KkkRwWTU1KvwGh1WT62k9Zd5IdxSUXSSGW0fnRzJ-95mbTl2ff_cCUlBkM_myjf0nLw8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
اهواز از این زاویه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101722" target="_blank">📅 02:54 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=k0n3f279CsqXeO-cY1LpIsJ5i271bU1Z2hntXSt4LxL1p0xxkZLI8rFAeg2gTKHvJy5CF9Wu8mOmzq5lyyowzWlZ3e4_RsOHAhnuspMlgWITz95V3OihXkZoI3TL8P_xjEV4nKzDRIURJ49mtwhEagdY0s7tlH6kOgd0MwGybN2q3iwEgzHCzc6q2J-Uvw38Xw4Tp5x_XHSzVPKBmWYG-Ym7N_7Ccm_4vMGQAUcycpwuRprcNnAS5p65SiwwQci0N8OAs-Ncdy0vY9rxn6uV8BXoQMzG4t3ZKYvnsQM6EGxMiAaonmWvzvvH7i57RkGLqlrevQD1WTZTFb7Bu8oEfDqWGe6lQEXvulMFxDU5NiwC2shllKsXT3z7zwxyQaf2H54AEiRhZ7uGjmBEH7Vwh4tU96ecdEZzVTSzC7zqtldc9CkkYn1ksqbqpaYl32-kkoEdQvJjVObiYhtfPtKIMhh1XsxXbsqKxMCiD6y_PcU7xUKMHZ0JWofTvkEZAz7K3hiuL3ohxOFOqOWBF8dvbTtp-zuo1v8VY0-9alBdy9IhYgeHNQK78QiQ1Ee5NPGXuQi13_zjNn8I-pGzi3I7eFf9DRw3WSNa7OUlYerqMEFhuJU1GAx-RfCy3qL8Evsm9UYAoYjRkLAFegW4b6TEj1YgEfm0dq6h_dQbbgxI368" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb56b99a1d.mp4?token=k0n3f279CsqXeO-cY1LpIsJ5i271bU1Z2hntXSt4LxL1p0xxkZLI8rFAeg2gTKHvJy5CF9Wu8mOmzq5lyyowzWlZ3e4_RsOHAhnuspMlgWITz95V3OihXkZoI3TL8P_xjEV4nKzDRIURJ49mtwhEagdY0s7tlH6kOgd0MwGybN2q3iwEgzHCzc6q2J-Uvw38Xw4Tp5x_XHSzVPKBmWYG-Ym7N_7Ccm_4vMGQAUcycpwuRprcNnAS5p65SiwwQci0N8OAs-Ncdy0vY9rxn6uV8BXoQMzG4t3ZKYvnsQM6EGxMiAaonmWvzvvH7i57RkGLqlrevQD1WTZTFb7Bu8oEfDqWGe6lQEXvulMFxDU5NiwC2shllKsXT3z7zwxyQaf2H54AEiRhZ7uGjmBEH7Vwh4tU96ecdEZzVTSzC7zqtldc9CkkYn1ksqbqpaYl32-kkoEdQvJjVObiYhtfPtKIMhh1XsxXbsqKxMCiD6y_PcU7xUKMHZ0JWofTvkEZAz7K3hiuL3ohxOFOqOWBF8dvbTtp-zuo1v8VY0-9alBdy9IhYgeHNQK78QiQ1Ee5NPGXuQi13_zjNn8I-pGzi3I7eFf9DRw3WSNa7OUlYerqMEFhuJU1GAx-RfCy3qL8Evsm9UYAoYjRkLAFegW4b6TEj1YgEfm0dq6h_dQbbgxI368" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو جدید از حملات سنگین به اهواز
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101721" target="_blank">📅 02:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=DKZMdx7TO9mSMTfHEx7OPyr8dzzNvkS7Qm9qBDQ-vQ4qL-nptpRLefT5xH4QDnBN6iTrmlXl7wr-ZGR4IJnnISBxy3kdNGLqZHuOIrhl7Oyxc_N-DUxFQsQVDK6NQIXS61FL9wLoL0EkyqUdL2HXammbi12y2urjNGr4GLjV6TkqbovLJ5WwiEXLCEptCEF68e76Y5PXEA3H_jZQ6uURA0CVZVqtlrGHhTNkB9VubFeiq-BNZQ8ABAqzl1apUtcJt7NBH8iKtiEnk-Wk88FrA8zzgNtzA67j52CObmKx6kowktHGd1jwMFvqyo_l_-O_6FTQMtOHCh2bSCiVZvASOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213a7b9392.mp4?token=DKZMdx7TO9mSMTfHEx7OPyr8dzzNvkS7Qm9qBDQ-vQ4qL-nptpRLefT5xH4QDnBN6iTrmlXl7wr-ZGR4IJnnISBxy3kdNGLqZHuOIrhl7Oyxc_N-DUxFQsQVDK6NQIXS61FL9wLoL0EkyqUdL2HXammbi12y2urjNGr4GLjV6TkqbovLJ5WwiEXLCEptCEF68e76Y5PXEA3H_jZQ6uURA0CVZVqtlrGHhTNkB9VubFeiq-BNZQ8ABAqzl1apUtcJt7NBH8iKtiEnk-Wk88FrA8zzgNtzA67j52CObmKx6kowktHGd1jwMFvqyo_l_-O_6FTQMtOHCh2bSCiVZvASOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پشماممممم صدای انفجار اهواز بشنویدددد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101720" target="_blank">📅 02:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101719" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=iYQ-uRda-zVjsLTrbwQiuFHi5mA-O8KKQiEO3eU07whHvyT0IuJih_8nU3fASJsMJtdJHdkyOANEFXKascXuQQLYcGs1q_e4aixe8oZvh6GL6JklBGS4lJwe9Mc7-ijDJTfTs6ZErGA_GlOZ0dSkSoxdXKcW64TwxOS74DelSqjjW0b_FmGUCcaBH-cL0QVqd6-Py96Z8GEvyrGzs0NJAJ8Y8F4KO0FUmTNVq10hG1sSXwlR05V1x0tBjr9JWoqdf7GQIsXRXw2cscEgvnV-S5KPnjdG7NBCKeCxeANyb629l4Mb1UJwswuRgIe3dyses5ulOwVbjlWx9fvcBh3xiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a6c0f6a9.mp4?token=iYQ-uRda-zVjsLTrbwQiuFHi5mA-O8KKQiEO3eU07whHvyT0IuJih_8nU3fASJsMJtdJHdkyOANEFXKascXuQQLYcGs1q_e4aixe8oZvh6GL6JklBGS4lJwe9Mc7-ijDJTfTs6ZErGA_GlOZ0dSkSoxdXKcW64TwxOS74DelSqjjW0b_FmGUCcaBH-cL0QVqd6-Py96Z8GEvyrGzs0NJAJ8Y8F4KO0FUmTNVq10hG1sSXwlR05V1x0tBjr9JWoqdf7GQIsXRXw2cscEgvnV-S5KPnjdG7NBCKeCxeANyb629l4Mb1UJwswuRgIe3dyses5ulOwVbjlWx9fvcBh3xiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انفجارهای سنگین در نقاط مختلف اهواز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/101718" target="_blank">📅 02:44 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T4kvMlB6mOrbUH4xHHD0gWDEeE6jbZJgz1rkgiB3AhnLs7W7EmFDBqGP1c8q95OZw4BYcIbSP0S3BbWPT4CX33nzcY6i3G6aUbfxFxcddbPAr6P1EWzgoZoMWpEWxe4q2AQTalXcpLHUpuRU8yhLkrtkzO54tvwOzx6a-l75PSOu6GgibqELZq9CX4r7AiXA9ouBJfkBtB--bqoqQe7hOJAW-43-Xwa8EIJ7CMUIguCApm_WRclDEldepusrT76-i5cX_bgv5gBwARk0d9d2dR3ixJpZONZpD5WLCGkdrfPlWelzyCbuBAWh-oxylR8-A1QPuCpaW86Da4Aq81-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
✅
کریم‌آدیمی ستاره بارسلونا و خانواده‌اش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101717" target="_blank">📅 02:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101716">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=AzNPRVoo9TrR7F-zDhUUmj4K40tLzTqiluk728rAQ_lENCdj-aTf8ZJ1mK1XZUYi10B-llttipjTHFtsy6Bb3cM0dH8hJbWS1SXStxpAXf7ox6AXdD0-xidM4cpINrtdXh9vI5XJlfLx9-FDzGRGwF4rMDqz0fjTVMsvCJjU7jfjBX5cdgl7LxpQrto5Wyw2zVGpIzuHx_M2sOFVRdrpNT1eeELKempDZ1iY4Jp7jqV8V75ox4w_dN-PmrmTs3aporK2He17hGDL9003e4tF2iWms2ocZWPjRT3y-PuepsfU9EiDkZUrQKrRAeXEVBENyXGmT61qErk2WZfJdwYOjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db91c85c7.mp4?token=AzNPRVoo9TrR7F-zDhUUmj4K40tLzTqiluk728rAQ_lENCdj-aTf8ZJ1mK1XZUYi10B-llttipjTHFtsy6Bb3cM0dH8hJbWS1SXStxpAXf7ox6AXdD0-xidM4cpINrtdXh9vI5XJlfLx9-FDzGRGwF4rMDqz0fjTVMsvCJjU7jfjBX5cdgl7LxpQrto5Wyw2zVGpIzuHx_M2sOFVRdrpNT1eeELKempDZ1iY4Jp7jqV8V75ox4w_dN-PmrmTs3aporK2He17hGDL9003e4tF2iWms2ocZWPjRT3y-PuepsfU9EiDkZUrQKrRAeXEVBENyXGmT61qErk2WZfJdwYOjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت تلخ کودکان در‌ جنوب کشور‌ بدلیل قطعی مکرر و گسترده برق...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101716" target="_blank">📅 02:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101715">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCy_Zp_mQE5kOQpzTtRBGAw27fIV66ESmbxbRwbcLvyBa-v2r-muGQbTdwlouuiQVo3K1HnA5egUl7aHlyOYeKrwlIEi71tU1fSBAsO2CiU9i3n_o_rJWA7YP6oOGKW5Zizr5GarHZXXl313YQ1Ol8ueRpNSRD29n7gQgeh4JypHGTEozvfm7T2sush4vNcCM3UaGoBTeM9DTNLCxAlhyrBebPGElMr408I9MRqwA8eQKAggRUTQ4yJnLtXtJbanNdrcs6xVazrSVh12T2ZC-niKczs-DDqYbDRCqHULMKfUxWqmGnRAFp6cW8f6dNnNCF4svMz5pIzee5QeEoK6Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
❌
اوتامندی رسما از مسابقات ملی برای آرژانتین خداحافظی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101715" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101714">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqM0MkM__3mGP0NxGa0TMlwoh_mmfV1O1yugQT8X-Kv3zncrxxIVbLuwvrXIWmpggEhctgoh287RlbM0aYvk4AX2NUH8fmIF9DiI_8iMWh23wq0o2q0J2Fqiz4TR3MNu4TfP7eoDK2g95rab3g6KUM6GUkjYdwz1LRoKCZaWH4xNX1b3uXNyyCKmmUb1DfujmJscyYNen1eEXzQlAs5_Gswnon8YIx6ZPG9T6JbaAqkKVQ1qCCt-WakUVEfa3XFLvS3lJiEDHjYXFxQWcBfEbGsgIKbqBzNJRF_qEURon9pcwnBrZDSRESJIvK-UEF4ZgzkyTSK1vqyiCkHYMy7SUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101714" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101713">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=n9Pc9IlcEr-4-ltd2y_BFzQ89MRbdqQbdqbrOsjKPwAqMqLyyVbiUPNzq5bkb9KIExdOb9d4pb2zJV-9Mx4J_nIUmQlkJZwLNNpG0jSvmuvhaPe8sPIyATRSEEkaVmiU2Y7HLyGLDDHNLdBf60gqRYTdpxjyreEzG0C5FVWJzrez-AsyL2SvM3HMODCRo-9g9q142KrUTDQO0LcvX4sOot3uWlYG7Hfp9UE7Vvs3AQQaGjd5rGMPCsnPXizSu_h7WA4yKvbPIZv_ZWyu3Y5VV95Omy3Yd3CBRw722e-r_NkbHGNqgucU18TvkABPlBbramoVCHWLRoAmOlzAF0aysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f7d69dd9.mp4?token=n9Pc9IlcEr-4-ltd2y_BFzQ89MRbdqQbdqbrOsjKPwAqMqLyyVbiUPNzq5bkb9KIExdOb9d4pb2zJV-9Mx4J_nIUmQlkJZwLNNpG0jSvmuvhaPe8sPIyATRSEEkaVmiU2Y7HLyGLDDHNLdBf60gqRYTdpxjyreEzG0C5FVWJzrez-AsyL2SvM3HMODCRo-9g9q142KrUTDQO0LcvX4sOot3uWlYG7Hfp9UE7Vvs3AQQaGjd5rGMPCsnPXizSu_h7WA4yKvbPIZv_ZWyu3Y5VV95Omy3Yd3CBRw722e-r_NkbHGNqgucU18TvkABPlBbramoVCHWLRoAmOlzAF0aysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
نیمار دوباره در برزیل جنجال به پا کرد! باشگاه سانتوس اعلام کرد نیمار به‌جای سفر با تیم برای دیدار کوپاسودامریکانا، در برزیل ماند تا روی آمادگی بدنی‌اش کار کند. اما ساعاتی بعد، او در یک تورنمنت پوکر با مبلغ بالا در سائوپائولو دیده شد! این اتفاق باعث شد خیلی…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101713" target="_blank">📅 00:47 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101712">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=QOPMEKJKp9EQX3H2oipo00EWNkvfDfExFb9OHUbKc1XwGUTE7-w_lEl69mzj1kCAyuXj4KSGnBfs6nzqpQwPZ1WvMjIZ7S-2zNkvI0OEQcaP15SGnfDxTu-XkgHg8bpT_XI3Ir_GT2uk-JOtCV88g4yjRh5Av2IwWvaXz4Q7ylBhY0TuaXINQMGB10u9MMMZhc6L7dnRR6rASCt1wLzzKpjXE6EBI5ixPQzZep6LMt7Qa_nnfDbaM42UuVEKRRbdVZFJMPQ4YJllleKR63MP_FJs4cTTrNCtZqQZY1ZyrUyBkwasFRyhTM1edkwp4x8OunUf2Tk9HuezUtryybtsAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24deb1c503.mp4?token=QOPMEKJKp9EQX3H2oipo00EWNkvfDfExFb9OHUbKc1XwGUTE7-w_lEl69mzj1kCAyuXj4KSGnBfs6nzqpQwPZ1WvMjIZ7S-2zNkvI0OEQcaP15SGnfDxTu-XkgHg8bpT_XI3Ir_GT2uk-JOtCV88g4yjRh5Av2IwWvaXz4Q7ylBhY0TuaXINQMGB10u9MMMZhc6L7dnRR6rASCt1wLzzKpjXE6EBI5ixPQzZep6LMt7Qa_nnfDbaM42UuVEKRRbdVZFJMPQ4YJllleKR63MP_FJs4cTTrNCtZqQZY1ZyrUyBkwasFRyhTM1edkwp4x8OunUf2Tk9HuezUtryybtsAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇸
‼️
🇪🇸
یه فرد فلسطینی رفته وسط اسپانیایی هایی که قهرمانی تیم ملی کشورشون در جام جهانی رو جشن گرفتن، پرچم فلسطین رو بلند کرده و اسپانیایی ها هم پرچم رو میارن پایین و پاره میکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/101712" target="_blank">📅 00:19 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101711">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXv9f22GRXOOAI9043xcvJI-Y7wx-kjjnmkmmWxjEG8kpN8VuERMM3a45rhEAbSfhXXrP7SxCjpVVevUIbPe-bE3otlii2tSBnXycN1MibnksywAbOMEmmesq2cOxVEmdsHB39f5a-CSCsTyfBv8sm2TOK3OGJ73id4oBx13DmZTE1O9xGz1mf3D0kQlnQoIep98EV3JfXKdslmC9TovAU6MBEoINQwajbej1mMlpXmxrkh36h6G0pMVbZfT86YOOaO2lxbUE24bXPyvKlPltnzHPbkEGEFiib4tepJbIrYrgB1fmF78TSXuro_L8364_2ObBdKoqesbAqSt4yYs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رامون آلوارز:
لیورپول قصد دارد وینیسیوس جونیور را در تابستان آینده پس از پایان قراردادش با رئال مادرید به عنوان بازیکن آزاد جذب کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/101711" target="_blank">📅 00:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101710">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fygt6jOPxLXsRgChkFfNrECF2t8rtB7sufTSIonY_LIj-2sM0WCKUK_5vS6VjVt-JlWJDq27hXUIThqLnig9ffsKEnQUeaW-M9DTb_CBWVoslaxQ7_Jw60v_fnm_x8hja-qgVo1KS26NliO8v-tX2NNC7ZVlLOxHC2BN6TWabRIZDNBcVWFx1UQGLjRhTSI_KNKUlOmbDyfOmQWBmSq8xXL7y53WRT5a3g-FRV7Zt-Yk9Q9OlZYUWTLy1XsUFabnXh4-jCvX6rqYjfE2TBChUtrYeB3KRfeXaF8BQTKGRhhgqL929VhLQpXeVD9U8opA2uiV9K2BSzkIsfzBYZ3dPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
ارزشمندترین بازیکنای دنیا تو ترانسفرمارکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/101710" target="_blank">📅 23:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101709">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5766dd6b60.mp4?token=SBa1dIZsokwqItbRh_-GqZtf7YYfBr4wIHCVUHduGaY4uEotOphcvUbZg6cIegoVPzWR8gCaa46xEi_jQATUW1pr47PZ-E-pr7pFoL6G3MRZtP1yXqPU-f7cpnDZb7Rjubo8EupDMFNyBPKuflWcNOGWD07iGpo4xbl2I2ABeiPDuVamShYHQT1akuDbGFobY4HsCWIG-FPfmdGz1AJhJHzzP1CQPRMOCY7PnTTKXBGSD-4dFzTTVei1JDLczP0xo5dun2ONMqY24AxEN6e22n1v2xOlVCZDvjmgcuJkspWXeNQSjZDZplH-y4hcJ9XgJDC3voFJ7FrNsMgOjgFe7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
▶️
در سال ۲۰۱۶، مرتضی احمدی، پسربچه افغان که توان خرید پیراهن مسی را نداشت، با یک کیسه پلاستیکی پیراهنی شبیه لباس ستاره آرژانتینی ساخت. تصویر او در شبکه‌های اجتماعی جهانی شد و به گوش لیونل مسی رسید. مسی تحت تأثیر داستانش، مرتضی را به قطر دعوت کرد و در آنجا با او دیدار کرد؛ لحظه‌ای که رؤیای یک کودک عاشق فوتبال را به واقعیت تبدیل کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101709" target="_blank">📅 23:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101708">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=DM-BelDlhnigO9t6UVK1Bz7ozsB72PW-OyTWN55eF2yT6OqK_611CSBqi4kUCKIv9iozJUoBCtsadHSEduz8WUQCNIQLU5jrOuedmvWBm4jpPVh-zCXLsr2Tou2ot-rMotx_7ZKtYVlgdvGXqf8vCNYW6_uCBogsbg9rm81KomuK44feAkYJwuQioIEf22bIQRpHGvttZGCX4foBOD9krl5U2bb5k3lqrh_8EyW2h8Gv2xLOOMcgTgbFZltA8d238sIBC0a7TM0wAE19UTtbF3DbKEIBv6mrbOqRLUo-WwIlWXtlfH6_FBr0o0i8diG8C9xx0cltFwMRqiKw9IBXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b758c8add.mp4?token=DM-BelDlhnigO9t6UVK1Bz7ozsB72PW-OyTWN55eF2yT6OqK_611CSBqi4kUCKIv9iozJUoBCtsadHSEduz8WUQCNIQLU5jrOuedmvWBm4jpPVh-zCXLsr2Tou2ot-rMotx_7ZKtYVlgdvGXqf8vCNYW6_uCBogsbg9rm81KomuK44feAkYJwuQioIEf22bIQRpHGvttZGCX4foBOD9krl5U2bb5k3lqrh_8EyW2h8Gv2xLOOMcgTgbFZltA8d238sIBC0a7TM0wAE19UTtbF3DbKEIBv6mrbOqRLUo-WwIlWXtlfH6_FBr0o0i8diG8C9xx0cltFwMRqiKw9IBXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لطفا هوش مصنوعی رو متوقف کنید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/101708" target="_blank">📅 23:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101707">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rn_BPKQNlih_ms5gxiY-2cmZeuvnuQEY8VCfYBcCsQQlpP5sq-GcASyY6liZpV5JU_pv4tL5_DYaBmtv41JJY_2vB1mDKGKdS4SwlR9PxYxp1ervLbFHm2by8aUnRuFVSVpdsmKmYMMihVwVGFfeUoXStAfhenzgH4JB2F05RdlrdQrSphyZ-HwyRIFn5UfvYyxf7-pZFsu13aNS17ScCXhjed_taFiRHJ_FOZIKyKHw9W4lbujpKnZMRinPUNngOT4HBjCmePGZvVrgTlaZduvtlfceMPPvjSxo3_-Gpu87pWweoTfHNl5sgTyhwWJZJUA4StWAzyOJkw2yPLnI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ال‌کلاسیکو فقط یک روز قبل از مراسم توپ طلا برگزار می‌شه :
🔵
⚪️
۳ آبان ۱۴۰۵ : بارسلونا × رئال مادرید
📝
۴ آبان ۱۴۰۵ : مراسم توپ طلا ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101707" target="_blank">📅 22:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101706">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jh00173R8gy2PEQI8PABohDChg7fGvc8Cqu4X32yPRkfX3bfipks79bInkQt6cWbJWvxNFgaJPP7I8ry3Ms9zFPZId3XG3SZ_6mcVbn8pJ1_Px0a5bqISWZps3qOSvUoEEeuaYQfO2RuauLfu-h6vO09K6iqKTka8ihDY_WmtH3_iextRU8YWLhcCGqHyTjhMH4lKm8In6eO1-Kvwvy8rFSLC4hZzbbYW1xr0jg009U9JkZMrSUhmOhQeIc4igS34Df6mWZALkSKQ4vTx7zz5iJ2g6PQTkwR2grL_LXiGfgfH4JbCneAAW6AryG63OD7i6adxuAWfdkHa_Tskf3K-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا درباره اینکه چرا همه بازیکنان کارلو آنچلوتی رو دوست دارن:
از نظر تاکتیکی دقیقا میدونست باید چه کاری انجام بده، اما چیزی که واقعا اون رو خاص می‌کرد، توانایی بالاش در مدیریت آدم‌ها بود. همه رو کنار هم نگه می‌داشت. هیچ‌کس از نیمکت‌نشینی ناراضی نبود، چون با همه عادلانه رفتار میکرد.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/101706" target="_blank">📅 22:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101705">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X02zvWrI2si_Dwl2FQg7In_pzJH1UMxDaF5Lwi5wuHRxUJhQAs5HrMaXnerpzvZD5EcON07tYKaql7he22tU-6lpzW0M46FGK5NSRetl8aw7q8nF6mHEzCi1Jeo8pMSM5-DtXKQhHqCyBmdaiBJDG4BDtljEnZ-WvZ24TQS2yltRS_zIo7az8aRG-AiRbvYWz0LP5c0znbLl8NDi7dma1H_Pj9aJqHk2Zyq4-qwyoAR2pPa20L-W5_SocsKeRiDE4EVPqSQ6bB0XpzzoQsW4f7oBvHRdI58IlPoQRb1SZqMcU8EODvPLVFotiDY4z1hm_LUpSXTxFhglqgqZLPPJrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
به پرتغال هشدار داده شده بعد از خداحافظی رونالدو ممکنه بخش زیادی از توجه و درآمدش رو از دست بده. کارشناسان میگن فدراسیون باید از الان برای دوران بدون کریستیانو آماده بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101705" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101704">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🔵
پنجره نقل و انتقالاتی استقلال باز میشود؟
🔵
💣
همانطور که ۱۱ روز پیش اعلام کردیم، باز هم دقایقی پیش که از محسن ابراهیمی هم ( ایجنت و معرف وکیل ایتالیایی همه کاره پنجره استقلال) پرسیدیم ایشان اعلام کردند پنجره استقلال به قطع باز می‌شود.
✈️
🏆
@abitajsport</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101704" target="_blank">📅 22:18 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101703">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0GRtTNIFyTx33WdclxNlph7cDXA42OoER4khwL2ZUMsi7myizFdnsEca8AprTbmYF-JgxAktYxKYgL743KzPRQO1NkiEAlvsnCOgDOQPCnpqbQ44IVtPxeUFJISPOtG3eWkEORFFtruy79Q0GJoVhXAV_CVubifJfphfFl863RKxf-H1XegUPKwcRiiY5QiMG-FWU8MsYWjxMqktH-aFk9b53hbpvOxysB-q6MCttU4gQFsf8xxFLEQei-CFdugt4KdqOZQcdjJG6FHL5mrpvqp7smrIbWwMOOSAO30Y5Qcdoz68ImqvIUGjTjd0wHGMpDuxebNO8CkoQagOONz3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه هنوز شانس بردن توپ طلای ۲۰۲۶ رو داره.
نشریه اکیپ یادآوری کرده که چند بازیکن قبلا بدون کسب هیچ جام تیمی هم توپ طلا رو بردن.
✅
کریستیانو رونالدو در سال ۲۰۱۳ بدون بردن جامی با تیمش، توپ طلا رو گرفت.
🇵🇹
✅
لوئیس فیگو در سال ۲۰۰۰ هم در سالی که جام ملت‌های اروپا برگزار شد و فصل رو بدون جام تموم کرد، برنده توپ طلا شد.
🇵🇹
✅
گرد مولر در سال ۱۹۷۰ بعد از زدن ۱۰ گل در جام جهانی (مثل امباپه)، با اینکه به فینال نرسید و فصل بدون جامی داشت، توپ طلا رو برد.
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/101703" target="_blank">📅 22:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101702">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtVJnVm5-Laj4WQTCpeBi65Mw7klKdYL4CHSSOAc2YWZhT114lApwYmgaGdtCBkVLbWzBJwajuy8vX-sUMtrucmLuVP1Hb-qsWELvNBSyhxo9peinfInOvUISEHcTF2WEXgtyUkSkZUvSZgQ_LQEJ0mhk6qRJ5D0Lu5-bKK0CrEuNSyu-q2286zNyHlK4hJlpPKHJ2lovniJ8-IwqIqO5jTTaSTUppi5yQdYAkDntvyfx35dfITNi6qRpVJ1LkN9GZ5QjcS1tIPdFqA0yMqLSIM9RAX-s0xcAfJ8JTCY2Gj7acWiVDgDiRlaNN2SVCkVpe39r-HViKRIkKCrUUpzkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
ترکیب منتخب جام‌جهانی از نگاه فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101702" target="_blank">📅 21:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101701">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P_Af2FutYW2wl2KaYcFSZmZrFY4GkC9ppBadsyFdNeMTyYYZT_mshMsQ3qY0_w6qRMeNp4SmE0-dpTocDhwa_n2TYRFYCZe8xUA57BDbtYkRpntQX9_0Q_B1S_F8PGXJ55IeiPiwCdzd651RPyQOyF-Qrg4hpG4v87wHdh-neTWhor8PA17wT0mdG_xzeRPoLgAnvFC7eH_nKycvCGQlvtKv39Gn2pgMiMf0LZxiqGsBq1HOevDNBeNclIY6gCs0nADCpGkTQTgAJVDvJXNKlJIj9f9sfCYSetdBW7hYMhfjROSg5lizRfbv7aZASXxV4MdtP_oaM9vtDISG-MWQjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنخل دی‌ماریا:
رئال مادرید شبیه یک تیم ملی بود؛ چون در هر پست، یکی از بهترین بازیکنان دنیا حضور داشت. هم‌تیمی بودن با کریستیانو رونالدو، بیل، بنزما، مودریچ، کاکا، کاسیاس، سرخیو راموس و په‌په واقعاً چیزی خاص و فراموش‌نشدنی بود. هیچ‌وقت کامل متوجه نشدم که برای بزرگ‌ترین باشگاه دنیا بازی میکنم، چون فقط داشتم از فوتبال لذت میبردم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/101701" target="_blank">📅 21:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101700">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfGmX6WK9CaNupbc1hM7Yepg5Xq13L5PsRWwTxUxUov4g6l3sbKPmb4vSlt-eTJy0nkmoRjdChqa_h0SO6q1hizbFRG9C_hGDwpoG438YboQeXfBPNHAHvncVsv6E7WModlTdfcoTOfafdME3gTpprhkK5YYFyjv8hWHNHbWNYxKuy77Vjy5A2c9Qdfg8r1RrsPS19VYyxsQj3WT9rSKXe-UmfueRRRKUXQPYCgBEihgBOkz1DV9sTNpPpw4L-afnpokee_-f4XAF8Yaiurflc7Snrm42pRYOjHa0br5GwSOfpN7zXGSO9e31U0sh568-fM3_TQFhyXRaiXvRrwNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
بن جیکوبز:
🔺
چلسی به احتمال زیاد قرارداد با ماکسین لاکرو مدافع تیم کریستال پالاس را با مبلغی در حدود 52 میلیون دلار نهایی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101700" target="_blank">📅 21:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101699">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gc1D_vgkWN4uKlArvdiUj813oD0gZPKbh9SNJKyuq0iLYs5Fq14qkUY0fHFw6DUfxOU80TzgAqfbn0v3buuWdmgy-sP14ea5N2padtiEW9_sOfeI2K3CJLqYgvEc_1f96Pl8OSBpgcJIPcWAU9K6UvSklIoZ0P0MsScBJf8vF94z39abJtBvsHghEDCpPgPLFwmR1AuEfs_BbRQZRm4lHP41eozJzcMGl0FxYZ0fDvEZ_1Ozt-7r5SjAFE1C3lM-QqCLeonQgaIa_XnfBkTPdhMsWlUYyYjs1rCjk_O9vY9FnWy65dFZ_uDrP2MvRH1jxccgyasLzMJiqS08lteq4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
فدراسیون فوتبال نروژ قصد دارد بعد از دخالت دونالد ترامپ در ماجرای فولارین بالوگون، یک شکایت رسمی به فیفا ارائه کند. این فدراسیون نمی‌خواهد این دخالت بدون عواقب باقی بماند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101699" target="_blank">📅 21:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101698">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCvYIHWOxPOCfJ2kN2VKLrZQqN9T2XWKmOxf_n-pwTUazZGGNAiMe6HjujVZpaWgjIl9y55G8f5djbatzWkgRipcT61psYCfoXCfAbeZR7Yz5Tg7G2pbnLh2vK2Sy5EgKOk7BYT0B0ofdwSSXKIZkp2LuwFQMlPHNLIJFk4KScRGwFuQiSkEY6gF3IhNF36z68nuJC-Mye3rP0cGev9AdfKdRK9sC0nagMRjGTnq6OoYH7KtxXiMnOP0bPnagP1zaraqxPtT39nYVFN37X8EXPnKO3W1dxPWml2hFEGMmBc9V_L_Av0dIaNTWlx9bdbp1mIyFe3MxsTB0JaDQ-Iwzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آنجلوتی پیشنهاد فدراسیون فوتبال ایتالیا برای هدایت کشورش را رد کرده و گفته که میخواد در برزیل بمونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101698" target="_blank">📅 20:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101697">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpvEEvzgmEwaygUg4ZuSCWaIPyCZGm6rlFUTvE4-GDQ7sMlQmOmhYAHLol-0W3TQFUrxUwS0fx3i4Ts_TmUih05N9JNpmcmlidWqhYjQUyYga-IFR9nx0XugBvPizGaFneZNMW88-buXSwrvxN3lqUcEOir0kIWGiXjCt99a8nihj4F9r1nHbbihmCaIbApvvOxKsYk5m-3joM-QiBXMgxPvI6S9h4Mb6xFITYmZ4mgWThvZHUkfhKoE63wEqywRWRCcus2d-kq-elHPeEHE6wFaGC1jOSkMD6LfKadSZ7OIGqHtOzgyxbZ7Gj-_I5KID1weTL13AXykJx4lTyElUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
لوئیس دلافوئنته بعد از قهرمانی اسپانیا در جام جهانی:
بعد از بازی، بازیکن‌هام به من گفتن: ما همه‌چی رو بردیم، در تمام رده‌ها. حالا دیگه چی مونده که ببریم؟
🚨
🔻
یادآوری:
این نسل از اسپانیا قهرمانی در یورو زیر ۱۷ سال، یورو زیر ۱۹ سال، جام ملت‌های اروپا، لیگ ملت‌ها و جام جهانی رو به دست آورده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/101697" target="_blank">📅 20:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101696">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIUwqzfDWjKwfzlE6ixVjqonIsWd3_deky5SdzFW9cb4njS38i5X_g-6mptKSCvEOH6jCPrtYOE79ic-RfLS4xiGfTaqAefJnj1l16XIQiriCvvLzXVw-hQ46cbpKMieLdv1geBcXakwND6kC62vB9oxMO1uaadtdKZ7BzbheM6efBiGvjspaL69_zwhm6qBqKRJtpxOzUXBPefCa2sOWHBQ2oJ5snqus2yF2qTrUwnF5XxDtGNT9xk8iawSkLhjeQRzVSlF5RCEK72Ll2EwCUdFLgk34EIdB0YA_AXfhVBJrGS5EoDMweRz3tGHJB3GQNV_uJ7TwLz48GtsY7iSyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمار در کنار بتموبیل و هلیکوپتر و جتش :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/101696" target="_blank">📅 20:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101695">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PK3oJqiE7p-BME095F3or-3EgK5UvNLP03eHIXIhNWMimJBw1ue3aAb2_FZUrKB_1f-eJ03vgbIP2-iOGjpcX56gUJPdXHdUXAk1cV4Uv67-wcVupnJQTgzKpC7mXcKq5QEpNBPF8zkkZdw4jHiGrtI3ouUkHo_CCr9zYWlQZ1xApyfVLVdmEqLZmT8g_L_XhzjlS9-KAgC_oNGF_vxQ9QGRlIZbU9Qy5s_fuX4IxFjWOXmKHwltKWEpLrajk6uw0tyuekl9rHT_-QNila0gwRZ2aIKThmj4RfXqZP5_QAw0rbISIf0kMUMYhjkcnH-cPfugl7t_r23pJCps8QJyRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101695" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101694">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSQYrDrdwueSUY4PgwPLqY2mWEq-Fi_eTIzQA15apDUxxTrg_plObYectEvjU9sJ7O0vM4R5FUZKXhGRgbizIbz92wyQlh4o3IOrRMFxWZkh2QWmVi1TKPfEWt47YJ6OGHaoh-3FSOmSo45ZN76IqrdZDO_yF7r2kqvcV-xWrnwSzVKNFkpOams-viYkGYxVlyxNq6FnjukPIfEx-OPJJsbyUVNbDbNBOKJxQEFKvL1itv6dqQYm_ruAA2XoChKNo-I06rH5UCyRwvQf8e91k_Vo2lMBI8UYaZoC5AwZBzz9gnDj_1ZElpNQ_mgfWcS0k01WyM26uy8sBMcJx8EPdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔴
سامی مقبل خبرنگار معتبر BBC:
🔻
باشگاه آرسنال قصد داره پیشنهادی به ارزش 70 میلیون پوند برای جذب برونو گیمارش به نیوکاسل ارائه بده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101694" target="_blank">📅 20:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101693">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=CKVuMhDu7VZ64NRGcBnssWWwE65XrrRAAqedjnrQW6nAzl1Cng6fswVsTopBeobtE2lbJeIRrdiMKskkPp6c1G5IG2YZhwo0RdLy6sVFbhPMLiHtTrN_vBz6yx9b_oF6tJBv2nycoUxlu6I6cH66Pq20xByrWSHMR9aiOcFfgx2kQZmSCnkf1jNW-3M45ui-X0W8IpJ3TOX1fBRrH7eo7q1PyWOtj7Y1-4tbuNCcMjGtGWt3O-4cpABDmu7rqc4Gz1SfewfYTNntVBL2v2sqYLwZ4TEmRhiklUuCVU7DyLxPTs52F_jcFtIxZGHcozv2NnQzFX2wBIHZtk_c7bRUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d00c416b26.mp4?token=CKVuMhDu7VZ64NRGcBnssWWwE65XrrRAAqedjnrQW6nAzl1Cng6fswVsTopBeobtE2lbJeIRrdiMKskkPp6c1G5IG2YZhwo0RdLy6sVFbhPMLiHtTrN_vBz6yx9b_oF6tJBv2nycoUxlu6I6cH66Pq20xByrWSHMR9aiOcFfgx2kQZmSCnkf1jNW-3M45ui-X0W8IpJ3TOX1fBRrH7eo7q1PyWOtj7Y1-4tbuNCcMjGtGWt3O-4cpABDmu7rqc4Gz1SfewfYTNntVBL2v2sqYLwZ4TEmRhiklUuCVU7DyLxPTs52F_jcFtIxZGHcozv2NnQzFX2wBIHZtk_c7bRUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اون دکتراهایی که دکتر علیرضا بیرانوند گرفته
😀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101693" target="_blank">📅 20:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101692">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm9Q7vTIfacdpCxw1Z5qkGrl5H1bodyVJ0DEZzNRi_hXPnpW5d1OKpAdbbew6xtOwJS_-knsnMQLNeJLkAJ0MF30BOUtZ03BndFk57JjWioWwMvxnT2ar3N7TUOLHa5VBH4RjuLmx5BVuXHSK8tbYP6JzuoXw7Sz64-KyKMMrdTpasLhKW_q625PAVMFltjMJ0Pyz0D8felojb1KSs_NonFkjD4bgIfxfTvDIok97ouS3B5od1vTHVtWf2CrNvp4c2HugOnOzJkeK79PCkJXC-ZCjmCJk-PMxum7hbO53fJCepu8hGQvsW-leD7eKew9FmcPgyIoptZfxnbnDf0YgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیتی که همه رئالیا رو برد به سال 2013 و اون کیت معروف..
⚪️
😃
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101692" target="_blank">📅 20:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101691">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hZs2ZG12tfHX3QbF3rf0rYDMSvNZf2GMzv2fkaDZMZ_fLgRnEXkxbVvLJhUdhs-6Yh4EmMHaY7V9Y5bFCqvc06wVh3zDfKHk0UvpGMzwV6uZWXfBwNKe_xOynsMoqVZ_OSCFHQcr_Qvkc55TrW2cLzcurCR22CW3gmoovK28rCHL5VonOW6mSpqHx46ATRjzrfEqMUmmrbyECaxM5D-kqdn4Iho7NmfEbpFsPMUbqwM0a_hKDm9lF3fTgAJgAxkKfh1gZ197Kx7bww2K-qGzusZh0eROeX4RiP4bzew9sFSwRQAjGtrgMLXx1ZAigOaprXp8Ew27LEpbXAxfKtGpjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاسمیرو درباره پیوستن به اینتر میامی:
بی‌صبرانه منتظرم به لئو مسی کمک کنم؛ بازیکنی که یکی از بزرگ‌ترین بازیکنان تاریخ فوتبال است.
🐐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101691" target="_blank">📅 20:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101690">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfsaoRrkzEnTol1GRtEa6OjF2O0smUHlgjiDOsGstxLrLs4JUJEpnq58EqSE-YTRADXxG7EVb-ft6HSL2K5hCPFVWrSJlwS1lwgeSB_RhY6zMrGlwb5ED491phmVp8e0ym4pm7JPIgvRFmhczThPXQwNnWMmGnmiusX6CeCwOScNtfe8Og350vLNBdaKZjWuj8sGnc5f06bxul6VJnwr2iqUEcGsvCkoJOWWH-Wz5fGETkjSifeQ7kZizra7OBFInzVTTYsWMWvLHJrppRzRWnlmgAHaT9tZ2eDHey6iSqFyjk4o9WkOt6lYvHvZoSEJ2DOvtRTahXJKYJjy7ldSbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
فوت‌مرتکاتو: پاتریک‌ویرا اسطوره فوتبال جهان بزودی سرمربی تیم‌ملی سنگال می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101690" target="_blank">📅 20:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101689">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQMzkvg9lzxiwF25-fPXi2FPodzm7v3q3FWbRBUPPzSlrSs1F2KnH_6PxL_sU1BYJv2TnyBH3gHqKZemAj2nvzVzetKAA9UmGcnECHdyBZ8gUwj7rxHU8BQIKRwi5mcmet1RV8VDWigQGzg9MSjo2mKDt07IW5DZhPKhdca0pzyiIfBlLA_Wf8rg2reOW39I52kZJRw1OVtBmj1B8_yQK47flDiPKEOhZnCrSYOV6Vx2pGENNjv-mSnmHXKtQyAUG70LO39eEQmv1-aum2EI1mdqeO3l00oPZGkG6Lyja8HCz61LdKwR2v_hOEtIfcVkbTIZuYDtx-IWGXLrYazphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇸
❌
#رسمیییییی
؛ باشگاه بارسلونا اعلام کرد که رباط جانبی داخلی زانو راست فرنکی‌ دی‌یونگ دچار پارگی شده و ماه‌ها شرایط بازی برای کاتالان‌ها رو نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/101689" target="_blank">📅 20:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-101688">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbESD-v_X5VZ6SRDIYZTlDADrdbWxdMAbg2WqIHjiitd3YBoDCqKL5ih-SnQUDB8uvD3di_kb9lqyniM0snR7zG2Nbqpi-XyszU-Iv4EZE--Pmwn9eqSeDm6II70L2I68NP-eRUPa2Fkcy4y1H5Q5G7EiC3uZtx4aQ5Lx5uWKJhS-svzhRkEUDhXyDJZqLptYaJd6U1u1MvbRanEOYeJjqAEY6G8fJlxk_2BQt8cfVlF0Ak4CcGHsSWpi0euMW7bzyzWHep3pzqedqjvOTz6TpXXqSwH1dv60SJpljOZt-_PVN4eT7POfph-54TgEzWCEw5genjk8SpGy7VnFVzBwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
توماس مولر در مورد ادعاهایی مبنی بر اینکه داوران به لیونل مسی در زمین امتیاز می‌دهند:
🔺
"در مرحله یک‌چهارم نهایی جام جهانی 2010، ما مقابل آرژانتین پیش بودیم و مسی دقیقاً کنار من ایستاده بود.
🔺
توپ به سمت بالا پرتاب شد و به دست من برخورد کرد. داور بلافاصله کارت زرد به من نشان داد. من مطمئنم که این فقط به این دلیل بود که مسی آنجا حضور داشت. ما 2 بر 0 جلو بودیم، بنابراین احساس می‌کردم که داور فکر می‌کرد:  بیایید کمی به مسی و آرژانتین کمک کنیم.'"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/101688" target="_blank">📅 19:55 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
