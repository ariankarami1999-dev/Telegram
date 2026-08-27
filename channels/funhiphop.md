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
<img src="https://cdn4.telesco.pe/file/T3NcP9L-cD9bcASjsCtvhiAJ5ZfWIcsMp6_bAORkdv8yqOt6tkC6xYK9B_F7-Njtp8_y1ht53tyFTkuwFM98vT603207Yuu4dxubM5K-jZ-cPw39wPvsxGJ8J6EpWiqGYTC9WhvQxCM9Y-MKYHgCVVidVNoJHn8K41QhAiOyTVhg-7siU3suvDXaEfjEG3naoSXw5iO0UaZTSGImwFqgFN-DtdpAMoHPIRNlyLHeLNUz5U15Q6NxbtxdvnlNgePZ1LgqfgLNUQKFz2nrf3spQDxsKuHfzr-K7UslEJJIEI5szAa_9u5T9EZaAzrBGW3c0S83d5xp2w8o3I5PAAtlzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
<hr>

<div class="tg-post" id="msg-82661">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShirazVPN | شیراز وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI7LzHaa45stZQJ9KwYgCx8ypUepk-fCqsYW3p9aPzm2Z1kbiA9F1AnpcD_PMKH_71s9csAkDgZB5FJeXEFpksrEvQDyv3UoqqejnZzY-A2vLYeYpaqG7INFPTeleWr1nmySW1kqYBbzVTBU-AsNfPbuADkzBEJCnZbCIaEkjUbxJAVuxIGr8bzbmBr7zXIyn7BHli4xpigpFE0hbhPea7AL-Is6doqXMHqpyojtjuO18MypfmUXAJIp_dqOUVHks8h4jZ3H264koqN_qTpoMqCisHk7wskEH1VwjAp8ubJuxQWtinMFVnXsDSjheaMnSkbrWHCGJ-W0vLkeZaxRiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
پلن نامحدود فقط 180 هزار تومان | خرید از
🤖
@ShirazVPNN_bot</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/funhiphop/82661" target="_blank">📅 20:10 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82660">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojmTvrDISY9La8vs2Xw6bXrP6UY331USeNgMPHvuL5qX8cyfupvfDsJdyZ2QA2jt4NqZVBGLLDZ8gpTSLt4sIf7DKs7WA3xk-rXJdnxYMButNja7tu0h2SvpZluIa5lJSlshaZ-NRwMTIutD95v0UE3khk4XHtRswJD8SdVXwYaBSP3OSgOsRKr-xX9NRmzzIPHpaOAVX2R7UeqIvqRYt5n2tDZ0HdJkYykx7FkC5rpqe8tcrTlhndqaNO8MUeJpTDtucWjCUw5_e-BjmDD6CDu9iTeO_JA0lgwCTNl5Dky_pyyk0kGf7JVp_SDXtP2nkZz7Vp6iQIbndITtNa1PqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/funhiphop/82660" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82659">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بارسا خورد به سیتی و پاریس</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/funhiphop/82659" target="_blank">📅 20:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82658">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlsiCDEGeuQE__mknWIzAE0_YQN3IuJxKaTmZeeWrjLHg-3-SZ6ViLDmIKJtGyUCjTdZ2zuNozOLCfL32pl_tOor6sdHFVX7Krf7snMsjeByP0z6sIHNbE_iFhetTAwjyZU2Z68CCUgtkHSa1DIgYvZN013T6rP8gtWnFmqOUVgRgL4swNgmvatGrgZd9wHVpkBEbtddaC3AFQt8yzB74Duh68K1DPXp0j54X-S_bA-xj2TaWiEFEVXM_rJchN-2gyKjo7SbNr6ION_zokDOgHKgrJkkmRCIzKv6o9P78YCybWqjpsNTMLhz60mSFu5XPfmZleUQ3oDmNMke2ZU8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرعه رئال تو سی ال چقد سخته</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/funhiphop/82658" target="_blank">📅 20:03 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82657">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بارسا بخوره بایرن بریم برا انتقام</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/funhiphop/82657" target="_blank">📅 19:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82656">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-gunRMoXQQ76bGhNikUcrs8NfkG8zCIuNosZrjKU3Z9yO62-I7cqV_y1gHohMpWxVWfc1qsAGWYkHyg6yvHeGRLbyv39Rsmgnp4HRSzmyjWiMVKupF4EkQDjwzj4lcl7p-Qs3e0uo5xDzrOWuPBSA7ypw-CSrdJFVup4V899rqcqZmsxIq3lcCdL30E3puiT1uAJ1pzyRJvE4ESYmT9wR4i72gMBXeTz2fNSIHdUgOjhghEDZKiMKu4Sx_0rnjfe2z1-gHXOEwus74R25kTRUyog07apJec5kmF9l1-BGeh9xpIigFbJhTYSJ5G-Ez9mCHCuGmwzIwV8yFwDLnjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/funhiphop/82656" target="_blank">📅 19:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82655">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17918269ee.mp4?token=mODrqNxHJy8FZHiOvI-GjpKT42Z7HoOawOXWAuECEr-DQaYvz7AguL_HBrXHU4IllxiDfeHV6Pn6w_Y0tXn0_BsaiblFEaRnrRaYV5M1ITkNr7yrro01KOud09prcT_CTwK4nld0eQhcnIo33t_AvWzQD_5Km9UFe4IUtirRmF63g_Lzr__HTPrY3nPU5B7VgMVLkT0oyg8WdntRHN1BywwMaLxzYqkhcZfkLSx_w7UdhMlLiP-fhTVhuU-ZNGXWmYTxgdklc1kJrsT6J482VAzZzrh7HWLK7efJUf-HzqInKP0VIlH4_pP_yd3CW6Y9CTRW2toGaG6nzAJAbB7uAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17918269ee.mp4?token=mODrqNxHJy8FZHiOvI-GjpKT42Z7HoOawOXWAuECEr-DQaYvz7AguL_HBrXHU4IllxiDfeHV6Pn6w_Y0tXn0_BsaiblFEaRnrRaYV5M1ITkNr7yrro01KOud09prcT_CTwK4nld0eQhcnIo33t_AvWzQD_5Km9UFe4IUtirRmF63g_Lzr__HTPrY3nPU5B7VgMVLkT0oyg8WdntRHN1BywwMaLxzYqkhcZfkLSx_w7UdhMlLiP-fhTVhuU-ZNGXWmYTxgdklc1kJrsT6J482VAzZzrh7HWLK7efJUf-HzqInKP0VIlH4_pP_yd3CW6Y9CTRW2toGaG6nzAJAbB7uAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داش علی تو لیگ عراقم داره شاهکار خلق میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/82655" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82654">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4APL6aRUcmDP6gVbj_acDiKKTJC2oVboswsczW3FlJTxbsAHtH_yNBNlDUG34DQMosRXJOgmQx1hyaaR-g___0nnZcihI8GcURxnshnU8np7r4JrR-P79tBUrlne7VUNONgc7AXR0ErMJJWLRV_HfzF9K65UGi3tE4H_UrZyVp6LsZpH5MUiXccDRLTMlNLmjdUySQEOvcqeSoZkbROzxph5C6kE4RscnFcdyHjrAzq4xxnMkKa6SIcx5ZYiZXXCxgtBzwCrOHIhaJ3bSwXSsVZ8P_8q_ta1yE1CytF8y9HvUDPDOFHQqt7Ett6fKNGrUKwfVjC9KhhbeGkQU5p8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g5
💻
@BetForward</div>
<div class="tg-footer">👁️ 3.78K · <a href="https://t.me/funhiphop/82654" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82651">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKd3pl3U49TwPI6KP-J6Otpt58Le9Le-6S_MGvbn-RSK072ZI6imvua-lrqvdCLNAUm2r4PcyHLc6qXXlMSkYzT_DSkb0CsBq99-zKWC8afTc_udmYvzdUg2f2-dik4W5dczNhlV3ybIxuGYc-WJ6A0HFMH-vFeYgMBzmUZ8nebgyfoLxA8MmG6sOC8P5eKXT54WFPS70rYphoKJtyjIPq7Ob9c2O30EkYtN4KQwJwkUqNUj6bYtsRfrUxALA9XFCeKmAAAt2h9VytVZdNdJHs73C9pIEJ26xe20w-deeoEok74VgZmvfJNanOQCYDaX4qmRlexPvEXiErgjg5ZTtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی این خیلی جوکه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/82651" target="_blank">📅 19:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82650">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">listen to demo</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/82650" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82649">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/lNm-n6TiIXi7kBE0H5xINPSwDGS_ZZ_ztRkgJ_UekHp6E1wgjBzqesOxKdo4GRvI5r9gDK2B6Xoxua8yfABdaIrqsr8T6EYvjWqO8ObYyMDa1nNxNOSYhTYJwwTf2zltcqm6ATV02svR-pXpOLj0bun2Dj9uw5lk_yPefVJUqOkVYPQX6gQRHsl77Lj-wCT4PKolM7IgtYzAxXZAyk1vgFXHxoXzN7iutu9VKE42lGM34rD3PKZvehvFdHhvk__nORXr7QpaeESLvlMmpN9hO38UOQcSM7OvmxeRWDNTiU1L1dFpuKsTnR4jcPWZSw6KVXxvF2TmXAmVICnYUNgIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید زبر به نام ثاگ لایف با همکاری سعید دهقان و سیامند منتشر شد.
SoundCloud
🔸
Download
حمایت
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/82649" target="_blank">📅 18:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82648">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=da1nY0Y_IBXxdUgYVI8BZb0cZOQlNRHhbWGtqosJv9HZFeEoO0POnoLhgPeXRzbIFcoUvgc2oHxwfRc5SKPeLE62Qk4hCKAGdd1azHix1rkLj7hfyOxkcSmmK-iDx11W3DV-sPLukzbHY2YGUQq5UC3q_bxxzDq7KA8KTa4DnZBRNZU9iJlx8TMCP5-j5T1I1hnUwVkFDiMKudfrQDPFySpSQRb2JByrqZ_6R1CCm_ueywYcNXobgGE4ZnBxw9vouYM_8s-wZmO1hvjx6OujN2pQS9cRVpICoTTqSx1PI-ymKJa0Ka9-4sfYGR_2qxCd13eTi7PHDjG1Itc3PD8tUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6cb16ab0b.mp4?token=da1nY0Y_IBXxdUgYVI8BZb0cZOQlNRHhbWGtqosJv9HZFeEoO0POnoLhgPeXRzbIFcoUvgc2oHxwfRc5SKPeLE62Qk4hCKAGdd1azHix1rkLj7hfyOxkcSmmK-iDx11W3DV-sPLukzbHY2YGUQq5UC3q_bxxzDq7KA8KTa4DnZBRNZU9iJlx8TMCP5-j5T1I1hnUwVkFDiMKudfrQDPFySpSQRb2JByrqZ_6R1CCm_ueywYcNXobgGE4ZnBxw9vouYM_8s-wZmO1hvjx6OujN2pQS9cRVpICoTTqSx1PI-ymKJa0Ka9-4sfYGR_2qxCd13eTi7PHDjG1Itc3PD8tUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/82648" target="_blank">📅 17:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82647">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/82647" target="_blank">📅 16:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82646">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">محسن نامجو برگشت ایران.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/funhiphop/82646" target="_blank">📅 16:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82645">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PWrEplOE6XYye0rlE7jeWH9XuhEdbR8TzC3EmceN9IaEddMNdcTzpkkq6hCrPEFs2h_6sVAez57W17MWKyTqYX7Yaw3MsME7CeRm__X4DUCmtJvDnuN4RGtGrG1Ohrg_2PE6MC-D5iDXeFayEN4MDXwdmBITZq8eVzBQS6gmpRb88LXsfRu106xLtFrNCDfFxVYI0zITQcn2L4M_Gejt17IRvi3rkTT6bQCOq8mSmVcCNmszvNBjQpx7tYxGOmkWzPOFp7QrFmjofIVJ-YiSOdAIWILkPOS_xViQ_WUlo5-h3NtivJKiIb5CZ0yGN2IVzbWymUiugGGg7qJx61DhQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73b53927e2.mp4?token=PWrEplOE6XYye0rlE7jeWH9XuhEdbR8TzC3EmceN9IaEddMNdcTzpkkq6hCrPEFs2h_6sVAez57W17MWKyTqYX7Yaw3MsME7CeRm__X4DUCmtJvDnuN4RGtGrG1Ohrg_2PE6MC-D5iDXeFayEN4MDXwdmBITZq8eVzBQS6gmpRb88LXsfRu106xLtFrNCDfFxVYI0zITQcn2L4M_Gejt17IRvi3rkTT6bQCOq8mSmVcCNmszvNBjQpx7tYxGOmkWzPOFp7QrFmjofIVJ-YiSOdAIWILkPOS_xViQ_WUlo5-h3NtivJKiIb5CZ0yGN2IVzbWymUiugGGg7qJx61DhQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن نامجو برگشت ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/82645" target="_blank">📅 16:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82644">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82644" target="_blank">📅 15:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82642">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RBoosEnRMfvTXAPtOgtQWMb19ysdbj8jHKGaDkbxpOUyOLZHVLd1FanZk84DyOvkWkvAySCjFMVOYw_4HGPQt8JL1eS1FL0WiRwDyUf_1wi_YCtirbp23WsyGOGpi4lEWzO5qzB55qFddkwe4z3pIg35LnCTW9A9RsoQMoUWUdfrDjeNCbGPQQeI8Ky0EpNcg1V9YD6yrjmzgNepka2SBpWahIt54M5jPM_cieCnkwlR0z2zWDWZd6nm1vEn-WNYPv-VIQbq71-02NeiLuTA8p9YuxxrYbXP1huE3GYaHHrmdBl18EDwfbMlWcMH2y-5SyduqZwfSAGM0l4KjJHkXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auw6MQZgB8ujyKBSOxNcJvhhwKVrR3AlpteotzvaAqNFu47Vmxz0Kf4aZ3BXQy1se3L3hmCo7WDkgNxA42RWAuRmDxCkOoyBIo43nJwLc8Hp6it96GUwFqBN_Ny_CnNh_RXla7EbYVNf_F6lgJ8pKhpH8de90n8A1N7_DXrjLmFOfy7oR_jQxnCEiPwV-5YD3NueD6GiOeRUFxNRagKqOi2FbrY0c4EnrB6CG8TEpajU8BSrOKpMiN5wiq8I490cTB8u5UUcmekcTMAAGgnXf5mexvOHrtL3k-GbIlhMmZmXdY-M7pWUUrummach-lEX4KodfKvCH_TvDOlqoz0ENA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پاره شدم
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82642" target="_blank">📅 15:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82641">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=kUepQC-LG6rn4bB1U93VMdUudjTaOzOv1jT4hUgIUyi1tVYgC0WWW7EW1O_1D455mWy3hzA9w4CgyWaz4S36LuG8Je482-PT-YF2FzDdeP8BhovSwdIwF1UmqsGkJunLO0CfqzKRYRpMUF0C48P8J_sqDVMAs1g0Mutjin7i8jRLAFuu5hJfrtzwhVw2macTsNlZxr6xOPFklsgyo-P_LIFuLJB5qOIKsHkKNcoRz6AxU2gleJQkwXKcnD9pzWcYk04KkNhKMg3RfNtKpKyHMNtwafa9Rb6Fxs9vs70CpNlL48asimzanUCZ4JO9TegeEVjYKR9jF2YKtEzkP1Uvfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33d8214fc7.mp4?token=kUepQC-LG6rn4bB1U93VMdUudjTaOzOv1jT4hUgIUyi1tVYgC0WWW7EW1O_1D455mWy3hzA9w4CgyWaz4S36LuG8Je482-PT-YF2FzDdeP8BhovSwdIwF1UmqsGkJunLO0CfqzKRYRpMUF0C48P8J_sqDVMAs1g0Mutjin7i8jRLAFuu5hJfrtzwhVw2macTsNlZxr6xOPFklsgyo-P_LIFuLJB5qOIKsHkKNcoRz6AxU2gleJQkwXKcnD9pzWcYk04KkNhKMg3RfNtKpKyHMNtwafa9Rb6Fxs9vs70CpNlL48asimzanUCZ4JO9TegeEVjYKR9jF2YKtEzkP1Uvfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82641" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82640">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQNtX-uk8k52FzLgLMOUlPpZLDMKqLw_yMYe_Cpcp_Ii_CAngxIkOOHPf255bP1Q2GWwh3re-iJvHVIju3cEAsE2-OKwhyCzJHWWr9e-ywVKMrvn_rYnEDAcSLyfDt2J8Ke6gRRkkNbOZZmunghy1eZcEpaP3qqbJcgkoDBrLyF_xcC6psS6vKN_vgAJHEa9HvPMejgYXhYM7lrMhLfP1ji0pyaP_o8BQtlZJSllYpbKfoO5_Rs3X_-FmJUm652ldDBill_pSSuWO5hWYdgwWwGAeXYTWW4r-vOdcMAL-GNpT9Dg8ilpSSkKr8cLNIQbAZl6_uisESbgWpx3st_vgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی این که چیزی نیست، پوری سه ساله قراره پک فیزیکی فیل رو بفرسته برا خریدارا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82640" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82639">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHH5oaRVboec0BXqFcdL2-pOZoZV1434W9GCqwN00xngccIYvluAmiqa_NGYEM_VqPxXy5AVTgVEDa7DNMOzqyseFoeF3gEbZmUYSWjjTI9p4fS_S1rC9WH8rhWVwIFL8KEZoM4LklMKg89sh8zu4znkSAMZdmhpkR6tYJazH763SyfzxvBAQs17vu3T9EkXGHWyztKVaHRiRJbDrbBeGxgt5yqYFmg-qKa-V0rxZD0zTiaotuIF9uJfFajVZI8yAukGghtf5jiizPiv5roPQrzVlumtYcLKXow4DIFqYhpEYjjRmbuxJ4T4ZuRJBXxCZj65J6_QPPGeKMZckNGfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیا میدونستید راب استارک تورک بوده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82639" target="_blank">📅 13:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82638">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سبک جنگ اوکراین خداست، اینطوریه که ما که چیزی برا از دست دادن نداریم همچیمونو زدن هرچی دم دسته تو روسیه رو میزنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82638" target="_blank">📅 13:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82637">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.  Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/82637" target="_blank">📅 13:13 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82636">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mun4C1eXO6xkQkwopp4SjLHZuDniG4k63Izm8CWsLkNtgcJ9uCc9qEpb3D1am1uHbT0ieK06a9rpqFL4WfY-DK1EIfD9Swgn0padx-JMManh2cEyfWuQasH4GgtOC1D_51LRBo1u4opLsJ-ron2J3hgP5YajAwmNuAmR5rkz4hXXJ-XkLSO0raDOduFLNLbbqVQ3l7N0Gd_qVNVdISnazJDS7eNIZh7nKbLAbkmbzrPBWp_0HCO6qg5PjffQ1dIQWmozDsVLfFoOkxV1M2ChV1wM_qTJgAgVWyKH3e7TNr4BnJiAW0sWV3J1f48XgUhhXfcxHn0CgJkACTToJJ30Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ویناک به نام "Concert Type" ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/82636" target="_blank">📅 13:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82635">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خدا برا ماهایی که تتلو ۹۸ رو ندیدیم محمود ویناک رو فرستاد
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/82635" target="_blank">📅 13:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82634">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=PLrf-XP3mUoLZa-pwd4ixS6BSXko0ex_jBSnCC7eW4eVOU_uoGTKpLm0o7HHduuliTRUiTr5LrAnfEHhskO-pCppLr4X-mjJjTTCuPguRCxDT0Ui2ZJNztL_1zQXyl1UAtyJMbXQSNYSQL6H50WRh-CVhnLvYbZlPfqKnvZAS1TLVYdTXYSPEdLXIQZ25gIbrmea-5QHmyP4MscmwlzBJc-LeJb42e3kmh5ei59yF8sLuCLQLmhc5RuEhAKZxakzPEVc-lk5r5IGfNvP0cz-6RZUhZXMu1hPgJ8Wfum6xX4Sh3MLnXCBA9qa_sG5yAPiqeNeSYO1-yuzpRw6koMYtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d048ddd9f1.mp4?token=PLrf-XP3mUoLZa-pwd4ixS6BSXko0ex_jBSnCC7eW4eVOU_uoGTKpLm0o7HHduuliTRUiTr5LrAnfEHhskO-pCppLr4X-mjJjTTCuPguRCxDT0Ui2ZJNztL_1zQXyl1UAtyJMbXQSNYSQL6H50WRh-CVhnLvYbZlPfqKnvZAS1TLVYdTXYSPEdLXIQZ25gIbrmea-5QHmyP4MscmwlzBJc-LeJb42e3kmh5ei59yF8sLuCLQLmhc5RuEhAKZxakzPEVc-lk5r5IGfNvP0cz-6RZUhZXMu1hPgJ8Wfum6xX4Sh3MLnXCBA9qa_sG5yAPiqeNeSYO1-yuzpRw6koMYtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/82634" target="_blank">📅 13:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82633">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عجب چیزیه پشمام</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82633" target="_blank">📅 12:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82632">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ویناک دیروز اومد گفت این پنجشنبه ترک نداریم
شاید فک کنید خب ترک نمیده بالاخره یه هفته، سخت در اشتباهید چون آلبوم داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82632" target="_blank">📅 12:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82631">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ماشینا شمام تو تک استارت روشن نمیشه و بخاطر بنزین بگا رفته؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82631" target="_blank">📅 12:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82630">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82630" target="_blank">📅 12:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82629">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">اگه پولتون زیادی کرده بیایید چنل بتم باهم بگاش بدیم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82629" target="_blank">📅 12:21 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82628">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبر خوب هفته علی گرامی و سجاد شاهی آشتی کردن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/82628" target="_blank">📅 12:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82627">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=LpANucrZt3yVXpYT2ajOVLsjCGhBvAeGK9oJJIGPwFcPWB1gJRhPlwXBwAR6KujOPAq3XPoDxWsPpnD3G2Jsqu39joDXlQPDk3nITh6tq88PnPnuA4rlZH9WYH5ola76VmWasV-VgCtY8exiSBYiXa9-a3OUQYurbubzOI3nsn4Rg5cM3HWaOX-_b_YofWECb2OVXbKoHNCr9tXGsdLMW82EKNv84TseDfSSs21cE9d3jCJSydVYyy_j5LkbTDGQ0a_niGQc2vpPE2nJlVmTM_haJiISg5vVUKdDqX4a1DaznpNJkTME2kHPxO6oZCqfY2eemC8uoCjqBy6iXPSpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7ff60b305.mp4?token=LpANucrZt3yVXpYT2ajOVLsjCGhBvAeGK9oJJIGPwFcPWB1gJRhPlwXBwAR6KujOPAq3XPoDxWsPpnD3G2Jsqu39joDXlQPDk3nITh6tq88PnPnuA4rlZH9WYH5ola76VmWasV-VgCtY8exiSBYiXa9-a3OUQYurbubzOI3nsn4Rg5cM3HWaOX-_b_YofWECb2OVXbKoHNCr9tXGsdLMW82EKNv84TseDfSSs21cE9d3jCJSydVYyy_j5LkbTDGQ0a_niGQc2vpPE2nJlVmTM_haJiISg5vVUKdDqX4a1DaznpNJkTME2kHPxO6oZCqfY2eemC8uoCjqBy6iXPSpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوب هفته
علی گرامی و سجاد شاهی آشتی کردن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/82627" target="_blank">📅 12:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82623">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQvoKgA9rMRfAXyadBe0l5cyYbCZ4c3GTUTRF5pYkGjHTaR0Osu95-12ABXEQUnu-q6OLvNc4w9FB4lFs-WW4YhA7uaw7g4DiA99btUsts6ElchqT_rL5PBf09NtWX5fe2AwRifWpnCCqY7YXh_MVgIwy4zOnbbXRDXFrwsTs6YcQoJU_jI3wIdfky58s4kOtZU2ALx2_v8p6WhL-MDEQgKcEWXKPwHPrZO41BW6ML0MPTdai_KPSzYWPRb4a6fU4r4TewaKy5nPiVPyYrqJmlWmBp7boovM228CB4PR4V-l0QYXWRhydpfz1Qd-DRU1FCiiMDP3jXMKxWEwvZjSPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pDj2paTnLXNGERxuoopayetMULQudTCEq9QtUd0Ql7bl_GC7xBYdaFMzAcDYCpIdWWInUBn10mOXmtYi5S5Ummpl1yxQHXe_7FC9txDwg6rcxzKw5lt9bASJUD1Yl8FW3G4OzLiVU2eHQZGQetygunvhuG0mWpHcCNRZZRC8TE4Fg9S6JzT1Db9L-fklVdBjsEt5cmgOiALAZk177CV6699aWT_nxbWxcidt9WCqF4VHVRSdHTKyEGfntOhT1HDdil7k9vpez2u963fWvHuZpGWlpLBsiutjXfrs-kUj_Z9ty7P-3kgdXZurxa1rhnF-fSjv62PrTYEYrnIUVYH81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fvsxp_NE43IqEa1vruff8p6Ee4YMKVVdmwX80BRVzSa0wsld27qzkx4pR2aUhXugs8tj9MAHn7UBfiHzgDsUxyuh9Nsb6Um3GWeqKj6lvmh9a0hAZt4lspW5Gwwcdc4dA2v3tQv-jsm6aYdtrd27xZhaQyJAc_MENTzFF98tJClS9SoKpToiKUboXsK9V_y1dHrJJ19tjoPpeo4zXHSPlBePvgai_sTMGjJtnVGghz4CT32pT8Vurqn6Ym6bTwWDNImMELTuJOJIhz3_epkjoeU2oNKa9huTCxO3Q6Sx0FnxQRCqwrR3uTNPKHteL3RKZq1i_q5EcYz6KUuEg9hOpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUI2xeOXVsr7bf7G1dwrCVZxx0qC8TxETVeJ3xXNkEkCyo2aPr0joAUU45kfY4qFeX_b-7KKAw_zNwCtV-7nOqKZ2QVa0Cy0cB7qyhfbtNSg-vQQVXCk6J7UI35Q7a8DeXFpW_lfsAlelARappF2GKyPnc5cq2vt_3NSsC4SPrwZoECgE7OH_J6cI8qOMq30qqWfbrxuIRWYqstxCiSbIoJSampVSkupMc2ONtyoIMhg8s0KP3utMAVC3PloJKyOw9tnNvdbk5o6wzx2KaCt7VzUPOhB5OoYqkIh_dqcCjvluShOBnzo8opAyQD97-7PAtaPCzakfn-egxgGNg30PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ماجرای ناپدید شدن دختران نوجوان در تهران و کرج
در هفته های اخیر تعداد زیادی از دختر های ۱۲ تا ۱۸ ساله در مناطق مختلف تهران و کرج در حال ناپدید شدن هستن!!
همچنان از هیچ کدوم هیچ سرنخی وجود نداره و طبق گفته منابع خبری احتمالا بهم دیگه مربوط هستن و ممکنه حتی یک نفر پشت همه این ها باشه!!
زهرا متقی ۱۲ ساله چهار باغ البرز
ندیمه اکبری ۱۵ ساله پرند تهران
هلیا عین الهی ۱۴ ساله پرند تهران
زینب سون قوریی۱۷ ساله پرند تهران
آنیتا شفیعی ۱۵ ساله اسلام شهر تهران
پرنیان ۱۸ ساله فردیس کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/82623" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82622">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KciJay1TOwkpYqS9JtjrI3KvtP1WSpjtArAeoRhMGibeeQkXnnoPCNEpb4YBYL0zpm8Ju2uEvezXJBvi0QAfNpz_-gmGCd7c7bItrVULTtG2GaGq1C1mf2Eo5jzuPCHCNIfSGh6hhHOCPRihBKDUM2pCNLnykyZnDuCyrrCEPXglTFDzfAou6dm_r2rDadqf-NkEdGM4s6IHuFOa1H23_b0As2TU7FxLSCbSfV9FlGua0oXLflek1a9AfX023t73dwHW3KjJ6dj-vjk6aKPqP-wmRXW_b-zC14goi9lg_UsDGdvGVd2i8mO6AI0y4f8S8gVEPcnNPite2boc4eelDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بارسلونا
🇪🇸
-
🇪🇸
اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
🕔
پنج‌شنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوکمپ
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
با بالاترین ضرایب پیش‌بینی
📊
نگاهی به آمار دو تیم:
✅
بارسلونا
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
اتلتیک بیلبائو
:
۵ برد، ۱ تساوی و ۴ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر بارسلونا: ۳.۵ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر اتلتیک بیلبائو: ۳.۹ گل در هر بازی.
🧠
بودجه‌ی تفریح از بودجه ضروریات زندگی جداست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/82622" target="_blank">📅 11:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82621">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_eoc-PNO6_7XeRI6a37bUiP85ly8UTv91fXR66xJ_tHM7kfLV7WukYgIcgWlxHaZ03o9cjY79K9_ITKd6yZPE35KLt3Jv6IdC2Skp8-H2bB8rYc-MzlcvzNV281h7G0zd_mPlT8bwICQj6DHn9iACScJ4AJNmfnRXX5W17mCadnps3y4mc9bxTwsjc3tUb89ny4oV6wfk05jO97PaRILicDV-sSV0JisQjbBcEBTAzK_YPen-j8uniIu07t6AQ7S2vpOIGGX3kNov8ojZA2c-9kGCQBTI91_uMCGjwS6ZmP6iTBfLc75NVECvfLPonZ0ZpN_UWgP-Z_CWh6G1TtWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام صبح زیباتون بخیر. 8
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/82621" target="_blank">📅 10:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82620">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82620" target="_blank">📅 01:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">امروز 4 شهریور زادروز کوروش کبیر بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82619" target="_blank">📅 00:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82617">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/82617" target="_blank">📅 00:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82616">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBKDy_HnQYd2ZAElrZ-GFlHb7HxH9rk1pCnUbcu-BTHtS5C51fWEB1VxbEW8domdwNLVPptCZxMB9-1tpYt0P1YH217bK0Bcg_A8zHYB7nMkTPyzTqzx5xB8t0q7mBS0m74i8GFeXPjx_CniVpHvFxfzSzLHZy_xbzwhV4HbE4QPx35XhcJV1FkOF1CEHHU_RNvPnNw2JB51BEbTX7erLkI1CebjcnQSfDZQYR9DTSiuO18EbedE7hyVmuepbueXB3x54NC4u300XV0mmNHmY59b6bX6UbXqNlDSK5JVFbkurCgVldaCQg49RIjDMmjlDctRWcFO6wgbWu0zoJ_atA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی وزارت خارجه خدا لعنتت کنه با این جوک بامزه و سکسیت، حضرت آقا شاهده که ترکوندی شیر.
فقط دفعه آخرت باشه لطفا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82616" target="_blank">📅 23:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82615">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mw3MiOgCquP3Swm2GLBatQnhPZXIsuWZ9K3okokM985fTeaKpJBvYQlp1Zj_roijPEo5i0lVKnBYSGuzW_hkyle0T8-xHpkDMFUK3LyQDyKBH9LsLoTB2rCpNZgU7mk5Tne-xWRsW1Wh6uryYhz0sJhW0DRGUVA1CLNrHYdiQEV0o9Lcu9GuwE-yZJX-cGXb4ppz4Txhhna3Iwo10tMFaWokgvz2pv6oVGGJZKApL-9P_1WyjzAJ7MUG0zjsx_U26o41UYnplKF1S5oexcJY66fHLabnsn4Q0owj94Has83W91FzDgQrEc6DU0BswX8tbkbgr6jMuGBl50hzqgK7Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناراحتی دیامونده از بازی نکردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82615" target="_blank">📅 23:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82614">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">رئال جذاب مورینیو</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82614" target="_blank">📅 23:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82612">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT_yulVWVfBZFU04vdEsyHqvMACYhTKiJZbjagesrIJIrXM54GDO25HGavP1CjtyTS6WGSZw1YuiGLvMC-_9p1rBPW_7K7jF7yXaQGwKNylw8KeNY6oIo0tCkkeAWwnElmpAg86L5x6Di2ILjsAoQXqDAAs_CfDSntBQYO_CxWwUGfGgmNqwTDHp2I09kyaHekCYNXMDbrM5bZ9NvPbkHZr5dWIvgZXaKLUU_KnFa98Vlyoiza0RHMhoKf9B6G0oIu01di0WCwSkOmUf18J8N4m-Q6HgbJpRJvLJNmQWw7GHeIqaimdrBQObgnxjaKqeLeUr9BO3v4YHL682YJc2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه فان هیپ هاپی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82612" target="_blank">📅 23:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82611">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR6Vag0cQRYJ5f8RKZ-SVGDjZfk5DfRbejNo8hwiaB2UDbDH0ZJBcEOXX06JkB8pTinG_g9M3Zgw0yqFlz_pyvSzrF0a0gVwzkVCdR59C6D3ByAW8UMJgjz7Gq8yHAGqRK60KohdRprwRc4YMt52BlPMEZOfsR19SUtf_Jx1u3DNnHA_G4dxds_L1D3hqp4Kz2gyr2AfpwPTk7dqW7tUnqxXaHCVvYh2C7tYs8LYWN7gnzO3AKP3nMgKXxQG7ib7i5df-Lhe3rziXyVNJ_PBAFyPXoeq8z0_PBroDYB40Q114L34EjXB7S_VnAuhAQ9LHRnzJe6WV165th6stfdxRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهلال از وقتی یادمه داره سالی سه تا نوک میخره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82611" target="_blank">📅 22:24 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82610">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQZdxnZbWZ7XKxoIlUcjkYPbTDsNnutaHeX2zlIRaIJLWKcgEpdsibJ-HRPrJ_XU72oVZ8UqUhrVO4h0hWoYM0pygy0_E7fyXtDTvUL13xYaGb-Dfq8ZGTAeszTZ56BsoMXSxFSzyTPB6uw0XAToktFjLysLSNxR1JEcF6-HowSiJKW7ohjxeb_LGkSoYD3GPtyxDUzHu3di7is19Qr6Tinnbkeumrv7khC_DkG3GLr6BDNjAikgO6Oz6W2gFc7dekNFtcnT6bp4-Jnu_7Szalh9uQbVNkyCxuMsMcHNjjntknhDWDCFrTitOMznmd1sHfla2lJxTahJ-NL3ulHdKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت کشورو ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82610" target="_blank">📅 21:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82609">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsOcfFPqRUqD4zzyFAVM3WPtaEjaBBdY9H4f_WNY9y2eUh4W3OmiXK0UizY3GSqzI1qrlRbWvSB6WSNYdfBPNxqpyyFGruN66zD9jjBQxnRFxzMKUG5NxALVf5HUHRcE2Kgt6PU3WhcRHUJDUu2v8fk6JkRLNlVkKr-WzH8qYXCbjav1uOpOknp_9gIE_R5JJnX9peLkddYnjI45MzG7Pk643TWWeGOTDX8hXScWN4m0LsYu5Oc1PyAjCGaZL4vg8qKRLGuCr7Qmwqjy9E478DCZ5gxVN8wl0ey_Ueyr0tMZEfz-OzL4dzaAKTbxT_xddccsIGRzpW9ItB-7yZ90NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس یاس چی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82609" target="_blank">📅 19:51 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82608">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=P6mB03VLSGPLkRYnuvs0IqMrT5ScIdoi82OtWp5gTyxu-CR1bHucRaJZSlzSwqOlmHo10xVE8XtKS2K-zIpLmMbeu4Fb8SR9jgGbG6nXAJaZje-AqLEpvoIcRVizObFFHfgmjboDE6wao-W12apQOjgKsDIGpivjmHl1w4EBF6MmXIsWCCjxkVfJbcUvN1qPRokkuO8Cf7qJTsZhZpbPaA638GFkFx_F7wQglyNPPPZfavKUsdZeBbZtdbaKdoc14HdBfSvxhYDlFQgzdJBp4Ru8uRMLP1QRwVW9KSvK9E6a_SnDYjT6USjcYZhUxkLjJux1OHewpHdUvBamTDkdbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a262ee6c0f.mp4?token=P6mB03VLSGPLkRYnuvs0IqMrT5ScIdoi82OtWp5gTyxu-CR1bHucRaJZSlzSwqOlmHo10xVE8XtKS2K-zIpLmMbeu4Fb8SR9jgGbG6nXAJaZje-AqLEpvoIcRVizObFFHfgmjboDE6wao-W12apQOjgKsDIGpivjmHl1w4EBF6MmXIsWCCjxkVfJbcUvN1qPRokkuO8Cf7qJTsZhZpbPaA638GFkFx_F7wQglyNPPPZfavKUsdZeBbZtdbaKdoc14HdBfSvxhYDlFQgzdJBp4Ru8uRMLP1QRwVW9KSvK9E6a_SnDYjT6USjcYZhUxkLjJux1OHewpHdUvBamTDkdbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش، نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82608" target="_blank">📅 19:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82603">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZxQ7mFQZMjo1wXpLlZ6TtFQAd7XxNmwPp1gpv15EoXyDaEoCJvpcifya7tIGOl6zEAcauaHsb8tKXTpAJkuizUGYtlaXuk08EiH99mscsaY_w-C7qL0gHbDZA6eVBemj8tuWkiCce9ug52POTiQzK5W_5CF6k3WEaVgRvSny42zWYZHXrW0kaMAl5u4odGI0YQLhbTOKu38LdYQSst8Mtg5ZZfyI6EqgRe3wgm4SoBJM5z90gupsBhH_Fk6MFXU4X1eoVDCGsXtvd7xSMOxHz0RHAtRfx062fwCSHABwcaoVmxXsGrjpXs4XYAAdNlBApf6xMQqmDswvVZoP761pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/omlsPJfJt9i5fN71rZv_pb-Yp6X4eLeUxFsgUP730rWYqB_LduMGAoA3YGlSDhmANIitnDrXA65USVWaAXWPVZMBjBoPssISL67KTQJ2wpDYXnCJMgBywGGNSMjdgqSLbfbNHMZg-H0XTVlyiTIhiqc4xd8MwqJvARechYLE6oS4L6MHWLQieDuxuGxqbk_Wey6lLSN7d59XKS_wuLfMA7ZPRmomqZWZJX3E2gjwxidRTwVponyWAWQtL1Z8MIL8NseaCvXC59i949FYWC_WZYCYQjCdgOZGiPSyQ5RSb8hDX_JkLceRzS5grwnzDO-IJAxEY3nld_vEUzY8U3TLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qnmZ37fTTNCGL63lUIIdYNONsLBliKZErmNrNEe4xYWJWQ7z-vGFx0jb5_e_shFCs04Hoo9EYeGP2ac0QSLRxt-NgdyMfU6Od7VVZ8bK4zIr2XQsmiIo7cdg7jyLp_xBcVR7MvETF_P5rpt_aBZmL70GWR7Rq0Ufo84ADbgUfinMzVOsKU4kGXC_fpnYYcq360Yju_tGyFO1idMG9tICh9APEAMcLz8bQlREfQRm700cHuECSrjyBWJMowoHPepedGkfN7PWJv_wZ8USbdr-1lhY6_7imdUu-o5JVUw3mTptK8F_xNXBf_MTSyxhyzob38SY_FDWUWaYmlKC_HI0jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IsGmDdcgmTlBz48EqqX_MbSjpvK6HXb4hfgkq4ElvENjMwqgxQsrXPzbcAaLhO9MVhzKePKI2KyCHWmxmEX3G_SOAPL8nASWvLcIb-49dj97M41hnxLVHabJql8iwzRCS27o58gjn04wumgSWOpzvKqSyfBXXXGKaGnRTZd_5qeaemgNS1eg1w_yM9w15J0U1SlfuFUV7C6h5DoL4Qm9vJ0Jq3InoFlLiY7linUQjZXhsSMo81xDsReaxCI5cZbRpG5JTbu-3u2UMCpr2inNx9SvjMRpla6BS_UZa47ylLlYuGIXhN2sDzXPivEWa-ZyMxQGcJKkTW3EzYHA3BFbVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=tzzpAYAMY4yQFEOAEVZeXbpDjBlJo3nwXoEDhicmkNHQFGUbLlSwm9M1tDO13flOjjDZ1Kadqaon1Jd5BYOpQzZaWSFaQcUzF02x6B-RlsFJ8-yiBeKXX74HnXHq9nGMXBQRvHlrijjkWc0VkLvlu3Tiwi1KHtJXwMfwDP3bDJOxEUQIS-p8Hkylv2qbil7VHVMZMNRJTqpzMHqQ5BeM8VTtkt2c_Sr0_oiE5xhHe-rbTPiXvDuxwRv5nn5rVR4kjZUgtrO9M1FQuad-Vcx6jTx-G8it8o4hc1ZhrcX53joeT-KEG46gfp3Usjkvp3k_Dya2lFNgkmelhmliZTQEYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8d5151d06.mp4?token=tzzpAYAMY4yQFEOAEVZeXbpDjBlJo3nwXoEDhicmkNHQFGUbLlSwm9M1tDO13flOjjDZ1Kadqaon1Jd5BYOpQzZaWSFaQcUzF02x6B-RlsFJ8-yiBeKXX74HnXHq9nGMXBQRvHlrijjkWc0VkLvlu3Tiwi1KHtJXwMfwDP3bDJOxEUQIS-p8Hkylv2qbil7VHVMZMNRJTqpzMHqQ5BeM8VTtkt2c_Sr0_oiE5xhHe-rbTPiXvDuxwRv5nn5rVR4kjZUgtrO9M1FQuad-Vcx6jTx-G8it8o4hc1ZhrcX53joeT-KEG46gfp3Usjkvp3k_Dya2lFNgkmelhmliZTQEYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبر خوش
،
نیما تکیدو آزاد شد
❤️
💘
💔
🥵
😱
💋
🔥
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82603" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82602">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhgtKrxS-PV6KllPn9dMDG3cIwrWHUKkGLHbm4GuHjNouz3HnosQsDvs9VP3YWaEPwe0P_tsvsaNOXwDVwF5t6rcDjnf4za8HEk8b6UCl11Xz19G9WwePUzCYdm3lQmyAuFiCp9Rihg_ib5dNTa5t6bJHwfLLzAORjzF8jEjOIr7VXatCs4gJ5UNI8qeqHUaPWVo9piJHiN-W7mR6McdtR0c-Z4f5Zql0-i8G9qGHAc_o2ebBMA7rU8s2zjC9EolKVk3fHFFY3Q7V3X-eGylF0rHJUiS6UyeShRnxxVBU6AWkr5itvMG4iAoQJmn3EFeVa_kEriSAuR0mNcuzWEqPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
رئال سوسیداد
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید
:
۸ برد، ۱ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
رئال سوسیداد
:
۲ برد، ۲ تساوی و ۶ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر رئال مادرید: ۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر رئال سوسیداد: ۳.۲ گل در هر بازی.
🧠
نه گفتن بخش مهمی از استراتژی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g4
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82602" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82601">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=dcrdKW3CiGUoH8LhVoT0imMZqP9CfbehDEb3ms2a6TKBKj6werp8wxjjM40GzSDTjMFtvVMp-Pyhpxevkf70uXXgBJjz1xzG8vdPGtE8b2qn-OCMe5Oe9TWkGrFH4X9_yipS6SGUaArnhMG406wXjz0XNeF3h1qsWgTJMqBUdEb5a7YNkDJNCDniX8pLXBBuyAVsapsVHzS0UVe4a5HcHED4m-Nk2BMmHGksq3yyUweGYe4Qoyyap3KTpxQ9W4LL_MxypX1bTzGTuhDIKHJSLhi6GApctSvZoNEIF1bNF7jgjofHiezqSMbImU_jOy44WeeDA6vZUPwmcWbAemY_6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27e5d7bb63.mp4?token=dcrdKW3CiGUoH8LhVoT0imMZqP9CfbehDEb3ms2a6TKBKj6werp8wxjjM40GzSDTjMFtvVMp-Pyhpxevkf70uXXgBJjz1xzG8vdPGtE8b2qn-OCMe5Oe9TWkGrFH4X9_yipS6SGUaArnhMG406wXjz0XNeF3h1qsWgTJMqBUdEb5a7YNkDJNCDniX8pLXBBuyAVsapsVHzS0UVe4a5HcHED4m-Nk2BMmHGksq3yyUweGYe4Qoyyap3KTpxQ9W4LL_MxypX1bTzGTuhDIKHJSLhi6GApctSvZoNEIF1bNF7jgjofHiezqSMbImU_jOy44WeeDA6vZUPwmcWbAemY_6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از یه ایست بازرسی بدنی تو یمن امروز وایرال شده و مردم جهان که زیاد با ساز و کار خاورمیانه آشنایی ندارن پشماشون ریخته و براشون خیلی سوالا ایجاد شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82601" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82599">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZY-0r7YtxaLADRqAmqyAh-aBgGqCXAsL6qzplEARhRbnwWcxV2HTX7wJE_wk_jJspfLyZQqzxoC2pGmXxPB2wPQfjLtALxa2rHwCE8rMw6NLzaEHSA2gdcMdQlKOGLDDBpkFd4L78OU3u2TdmWdGRJT-3caA1-vRYybOm7y6MGxSmyId1pFliIpsQsBT9VZ5pMjrf2kDNQFx-0r6Qi-M1DbmouTJPA1flulk-Co685mYqVVdGqUuRJtvD4rCPdXFEmhKDoYfaktB_uv8zWBQOz8duMmbw5pQb4QMMqdrXd_PA_6ysgTTP34s2-XRaGH_DFF6EK8N0kEw-a6SWiqOpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bE8b-8XHzfZHNq18uRuzqy4ji0BKWRhZtpIXfFDk4Td6vhxpHP3iyHT87EnyQ30bCElvnh97dnSGNfTGEOpG4ywmVjt8xzq899CSld4PzHq2BMy0RwwymCrMNw8w21pQVAHVIN2Pf7oDdZgcgJtOjuX1VtMhwn1RtGNwF3dTTczuz6dyzuKK_lXGgj_tdWWKajVRSyhH4vww5RUgMt9RYUpgXrZgqcVnyBxipoSCMv-ROi5t330RiRWxfBQbOeULu2hA89e73Um3so4Eb3Mk8X-qovc1LSgGuPCWekobSED-CAxBkAvz0c-BZ1LE1dA5AhD38s1NIwKzrGNe8R36WA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هالند با یه مو کوتاه کردن از غول کصکش سفید تبدیل شد به کراش نصف دنیا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82599" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف: مذاکره با قاتلان رهبر برام افتخار نیست و برعکس برام خیلی سخت و امتحانی سنگینه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82598" target="_blank">📅 17:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ریدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82597" target="_blank">📅 15:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تو کافه بابک زنجانی اسپرسو ۷۰.۳۰ سفارش بدی ۶۰.۲۵ میارن برات
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82595" target="_blank">📅 14:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Stc-NQmbyLsqFMaB65enmUSZLEbymiBUHcyQO-CIghv1G74MfwArQsDAI0OA5SfV4iDQrYYQIbyQIPX_3wncm7QrNiIN9y3NPrN4hgSN9IksiLpihM7iupA0UODlfbIqxPMq__MUuP_mxYPkvWAKuWCMFzEAOBSpFRgwu9WPWlqqfvlOggPQwUiFVpazkca6YAeZQl8zkND2PedfenF7XkhchorfOl0_hwcDBdEYdObyezyb9e5ahOrlBDP5KMVtwXRk7KjD52cbTVwg5iU8mCgo9dKdErqct2r2w2zddKZfbcNJ0yd30R3uoxtELAdd79hFZdhVipYb1FWLfYIP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین و آخرین کنسرتی که تو زندگیم قراره برم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82594" target="_blank">📅 14:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">این پیرمردایی که میگن روزگار خوبیه، ما قبلا نون نداشتیم بخوریم ولی الان همچی گیر میاد هم دنیای جالبی دارن حاجی</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82593" target="_blank">📅 14:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82592">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIONwI1YukA_ISIssHc5th9rB7rJYkbV0y8V7APyZ1Lpv2Z53S0kNv6RhIuh17D4obtlqh6bJnKo82aWxslpM1v_4cyuLbkbgpu1Mcs8eqIk3zeya6o5TO4tYKKadPU7-jCdefHDr_hlUx2wWZgkHHGGN4orC1gk3ia1xfmp5DWA35Ryzd4B42-Z_GWJcKD0WtNX7I6HRt8ix6UE2qpAn7QB_CZLQa85jHjtMNyfNBy2gqU0KVW1DESO7T6y9k0BoYpIpc2PBUcaygFssxI4X6wP1k9ch9gzpy6GhIb1VN3M5ojUApZpbhO-0yoTEQebT1pI8187mqgldBbczsz0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها بین این همه خبر بد و ناامیدکننده بالاخره یه خبر خوب آوردم براتون:
قرارداد سفیر برند رولکس با تیم ملی فوتبال تا آخر امسال تمدید شددددددد
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82592" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82591">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtLHYC8KlmmNG5u24N6UpHVEw8NpxASVpH0Pl0dDHxgrwlW-KGI4K9RBOJLhvUDKWRd7RnNHgtkhI_AIME6o4BTsPn91WCJH9a_kDMxRypsuc0OAQ-rO3hJlIu6cnc2IBSXm6ef8Crewpd5m2BkuzX4GmctaUrsM91Xw6SigaS8XuzCIUXBmnkE8Yq3oaVrjjxXau4mZRyM3K98K19WkLvPzY2pH9BepEVjW_mCHwAS1KBfv3_FYh850ONcxzRAlnJ3yoKpup8B8_eDiq8CB5xowoLYJxSEuKxMpYVv5koVv7boZd5QjmaehRTkW2wdD-d1_OMV-0KGgPVqQiExkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82591" target="_blank">📅 13:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BySXmZ-Z1eBcejlFXCBx584zRljtPr1i20XUUpXdjZ6Xvmm6AdaCao0M_UtYAc1UafCoSWLdmGo0tVKjqgXyK0ZG7zxgdiC0ybLMVJJltV-6n80ZrgEt3fV9yuO75v8Poi466hbIZD-qif6nof7V9mLol4MsSejc-NFfJJfBw6_wf-RwGuKWM9PIib8wzSnFQSb5IbS2B2sotcTxK6tOxm03mwFt6-9IJOGybeKcpxwQEByxdU_z0ZTPTt4Q1UEHpjajKgwUazeytMq9-IL3JLeSNJB7ohFeiYiXn4qG8gCGxUqN4S9-Jnpo6qifrLfDM3k9kuDDQ-IHuHYpdGsLLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حافظه تاریخی داداش سریع بیا پیوی همین الانشم کلی عقبیم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82590" target="_blank">📅 13:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKfLjuC0FhKRcKh0s5H4mmSu8S2P2pMNZCl0gZwt3XcYdBWCbspsSWQftxavB63sXoMm81OaIJK72VgI2vtQ_0ApQ6WZELgPcsScNaBA8EvZ6JqHJs0Qfsrmano6kG263UGfR5NfifFa0uYvF-LyOYMpL1MSz1k7qWVqs4PFOaCJ98BuyRMjRBiRSf_7Ls4ysDHsMoJWe7NwZz4gA6gjd0RjjxSvCB3aEICzqJS50K6zkXMFGClxzsZZkuEyVgThftrbS6V66rduo8ScuYmKV4WwS9m2XZww3N7cXbhAe_H3flVwIZWr_CViOkzoSDXwEafxbUYzENYEUf4BFUo_IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82589" target="_blank">📅 12:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzihEgT5IdXAMDjID22E3NoJrQwB5ob032vMy3RVFx1WsR6hATjNVAD0HdyqautTL_wfToV0LWoSE8jzFl5jl3VJJaRIfuScoB2nmhH6Ht9daUlfX-4mAb8wxVdvQZcRXrlRWL0cR0OUOZmwUbbzcuygtCr-94MQ6Psm-wNA0j_Foto7vEAn6PahZ7f8MXZkGHLnnrDrVmYbTKlo5zYQyXXP-Je3ONl3BzxY2FhRUIp9v0-ITL_aPYdnm5BjOE9KyjTaegFBJ14b7eu7Tcx3zy6WLpE1nEysNVrhFg8rh0jfZje2WGNhFNLAHrKlxSh2iGHcoyHeSi9bv8fQDyrcRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان به دلایل سیاسی اجازه ورود به خاک امارات رو پیدا نکرد و نتونست به سفارت آمریکا بره تا ویزا بگیره و نمیتونه در مسابقات مسترالمپیا 2026 شرکت کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82588" target="_blank">📅 12:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDIVtT0DvYA6jXhi86JFqRiP57f_zYcCf3fh4mI1ACGPbqB46lR59dVL_vKNy4PZBw2Qs0tHFfiyFeXKyJTcZ-TRsa8FKCkT6AsIu1XSfkrHT5VGsQ3HbufBa1Zb4zexeaiAk_F9QaF3omidIDx_q4wEAd-FuMZGClxleY_6cGc-HWrWlXXkdaUo-Jhcn50lhz4ozbhPajmJCEYNQ8sb1CTdE_BPQhdn-n_sci83HyXZdhSi-Rwk4DmioeRPHt-hQwafJ4ex-zqfg9r5KxIXp3tY0eCmxWxueow9EycB7NuDiXoQkL4wNXc7uKjTjMulDqsddv6hGFIXStNsaGxSUNCc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ef19c3dd8.mp4?token=EdGCbkx3btq4WYBRoZZgo_mph5lehjF3GKE6_ldtZ9BnjEEanoM6J92Nsax0Y3G46EEo1UiFWw1QrJBNbnaikb0B60speSBdEIJkjbYQLT8yMFUW-XREKp7X2ixgPZUCZL6ErkIZD4864pEqkSfFiaT3I2QnWygq1DHsm0cKrKTjcl_gIXPbt3eY32be5C8FVLMIQgxahc0Jy-RQK5iYU2Ys5n3kWfqS2zRCGDjt06o77P7HuwgspXPdDN7g2_j1ri4Y80KydTvvOYicyK1iW6n9Ehg2l83y3EC5gVNmalW2JmwbvMZJzUB5NJj2JjuI-thFcJoyknhlk-ngsi8CDIVtT0DvYA6jXhi86JFqRiP57f_zYcCf3fh4mI1ACGPbqB46lR59dVL_vKNy4PZBw2Qs0tHFfiyFeXKyJTcZ-TRsa8FKCkT6AsIu1XSfkrHT5VGsQ3HbufBa1Zb4zexeaiAk_F9QaF3omidIDx_q4wEAd-FuMZGClxleY_6cGc-HWrWlXXkdaUo-Jhcn50lhz4ozbhPajmJCEYNQ8sb1CTdE_BPQhdn-n_sci83HyXZdhSi-Rwk4DmioeRPHt-hQwafJ4ex-zqfg9r5KxIXp3tY0eCmxWxueow9EycB7NuDiXoQkL4wNXc7uKjTjMulDqsddv6hGFIXStNsaGxSUNCc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در یک حرکت شاهکار مهندسی پارک لاله نوشهر با ظرفیت 10 نفر افتتاح شد، مساحت 307 متر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82586" target="_blank">📅 12:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82585">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=bHNLySZzpP6vI7HtmxoiZdh5AnPcJgW2p9SVQt38h-DH5-zILfXBWsuqk82FMO5GzODKFMICiAlEbbJFOoSFDFsadafHCefov-OIa0UMARQc0QUOIJw4vDcnF2waFQMWPuY3yBTGFf-Rp3RE5_keMIdvWQ-d6qb4RQ-ZLKVGF0_QvZLmC_o1Nn3tRcNXTTU-7KmVufAUCoS_HpwS0zbANiE_hP37RQr8FUVWj9Z_skd-qcFEaN_FT3OPsgbVnaHVqUc5erLk2yLAnL-zDTQekIcpq4MLGwmno4zzrQ54rTHf2FtBO-Gg8_NTLbs4xRj3nSWyxMLNQI1-GPW1BvokRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/090cf184a9.mp4?token=bHNLySZzpP6vI7HtmxoiZdh5AnPcJgW2p9SVQt38h-DH5-zILfXBWsuqk82FMO5GzODKFMICiAlEbbJFOoSFDFsadafHCefov-OIa0UMARQc0QUOIJw4vDcnF2waFQMWPuY3yBTGFf-Rp3RE5_keMIdvWQ-d6qb4RQ-ZLKVGF0_QvZLmC_o1Nn3tRcNXTTU-7KmVufAUCoS_HpwS0zbANiE_hP37RQr8FUVWj9Z_skd-qcFEaN_FT3OPsgbVnaHVqUc5erLk2yLAnL-zDTQekIcpq4MLGwmno4zzrQ54rTHf2FtBO-Gg8_NTLbs4xRj3nSWyxMLNQI1-GPW1BvokRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو تروخدا
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82585" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xxp5wkWl3dw8lZ9QImxJX8_P3Ip3rfecCzO6qki6obdNxkQBeTv7nbw3PlQ6ud2W-jXCX-z7RIZjnXsOZ_EMhk7ho1CKa6O1SHr4ohj_lFv-DzPnVz7W8Hol-hWZVJmRauXKOQ2QhT7CkJpnwwhFMvVZWQGLF5FVT_s7QptQlXjm0cEaumx2-AQN8GmAzKpaTyHy1zaY4i5vOtcsfhI-Ifm5PHRi1p6aLDBRBUrwrAUONpB0Ag1Zv6cIRx4LxqWHNjn8C05cVFGAnf7gSrHxfrMeNLiyRlYBTwKdPO7LWFJE5Ep4bvOktUccvUY3ojGKAMbndNA28vJNs01I0mqWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
رئال سوسیداد
🏆
لالیگا اسپانیا
🇪🇸
🕔
چهارشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۶۰۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید
:
۸ برد، ۱ تساوی و ۱ شکست در ۱۰ بازی اخیر.
✅
رئال سوسیداد
:
۲ برد، ۲ تساوی و ۶ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر رئال مادرید: ۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر رئال سوسیداد: ۳.۲ گل در هر بازی.
🧠
نه گفتن بخش مهمی از استراتژی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r4
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82584" target="_blank">📅 11:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82583">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMvFwIslB3CBjfGDTaPWHPVj4J5bIZgOYt3pP6L1UnV67qbeJsGOAKTFTnBdncwzqsFwcG5K-giauL_5ZOS6DYnfVYZUjszvG7ZhaYE0AeyoLmPjXv2OEeZg-679Q6_V6M78gbTiTKNbgVlFRBZgbs7nviGs5Sh54m3qy6viVQfMtt_ZnQugnqsJ73kSK5dZDmH-7ZCiA9r5b18xq5uZ930exRuNWr0m_mhRUqMtZE8OrqOoK0iK_LQ8LJpvXovsw40F6J53shY-nvO8tHbGQp3_8PoOtGsz9DHrmbQYj20r3c_eVyuLHyLmAk4KhRq5EG-UOTMPouAO2kFtS69etQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد خیلی بیشرفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82583" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82580">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNTWt7FHxw5Y5D580nYlq2qNpbd2qR7v1NEBk1yW_kSeCtO6eyrtom4zwgK57JSsmjoh-08d6q5FZ-MfkXF5fjtaqdKSAXLis4vPU14Js_flEZzMzmeVfbhcthq0x30cEyj8bwFPgiNyCllz0rBL0jfV9hLp_ZUP9meYMyfRTrwstrclCg3CcTMmWaBGijVfWYFh1QJpB73VvG41Ix3uEoebRD-N7XLY1qLxssfX4f_6Ov-p27bdq1d4-eMoNFl6JpFYY38mcIkktXnzVm737Vy3nF8gfKbP5sZ-jZ2y7JLtTNQvCLV4pMpUxJPWVSH9DFXy5h5UFKOyslZ0KyfOeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qFwcjvW8Khvz7SkQCieTH1NVRtiBnWu56Ugfw6GyCf_rkh1Dkz4tOhEGlmS4ESu_EAPsYm9foq73OEq1zKoZFDfEZMEVw8ghPYaM7ilgICGYDyyI4kHxf3ijPHc5CX9Fsud3NYEqOxq4wllIGAdrAMde_N9B1Yw5gVp6XolljZgq-smBg1KICgWwuxWh6SaWmUUi4dpZtSlaMvub_T8Iz0vayM5M6rqEuithQY9Ibn1hAKOfg7IlCaeXe5csWaPY252l0EUlO1CWRNZ0sw1Mdc2f2YzW-2cBYBSpndpU68N44LpioQ1YqSv8Wl-1swfE2Wf17gN-BIe8I_AEmbNqhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/thOUzlqJzIoRmCqyQqeKMy8zGnPvcup16pkK5grRyc2UTl2XH9ElxuaqVbLzxeuYX4sDdU5vtZn8_abbMLJXtJehuBIzS8asnNU0BLQY8a3hw_8KyrYCvCog5S1wm6_403OQQapSMjOzeuTb3y41VMmplJvBT4aSTMiqS9eDf8hPozQ8iAhOTi5AIaRY7t4sIdpDCWb5-aUvt97MZyaafEUI7626QlCbREfwn--wEt1s_TKG0hBIv_3S8ui0zuxtqO2mYgy6to03lHbzo1KJ0NbzD44Lpo1oOhDOBFcD5HeaJ_towuo-TwyWd-JYNC3MqB1Gbje6mrENRVozNGy4ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82580" target="_blank">📅 10:36 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82579">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_FQfyKlcQCKvcIBBM19096UumaMt53NJdyl7HOBhZ4NYBQq-5_6aEBSdG2Wp3qsy0wxFoJWLnCFsLPj2ba2iGnAAY7zXlOH3m2NIDNPhRaKLQ-G3VwRtnD-ELk05RSBC63lCQqXmmnQDHdyo9f4O8C66Vum8gaLvUzq1JyksjvQHrThar1dDoVoXRKbLYO4NUKRcOGqDUPzvKVKk8qbjC1yA2Qp38pQuuwSZ3aLR6bzjHdDORXvLMosSr5wutpNA55yCLvrXPDf0iQEBf9_YwaGNaGhk94fwfS8z8zfbz9T7MIRsA_UX2UWtD_t5acY_GvKBZfBu7fT5l7eOY2LXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو وقتی تو دی ماه ۱۳۹۸ گفت هر کی ناراحته جمع کنه از ایران بره دلار ۱۳ هزار تومن و طلا ۴۰۰ هزار تومن بود
خودش سال ۲۰۲۰(۱۳۹۹) از ایران مهاجرت کرد و الان آمریکا زندگی میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82579" target="_blank">📅 10:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82575">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XygKEvPh-Kh0AIMjpHjFRh87Qz9HtKQC-Tu6yIeDWJMlJiuRx9-q_ob13pafCRVBUDJwRCH7Vyndqt5wu2wBk7DgVh8yvcRFS_HTB68oKrALE0hn6RjmJurVshsIo2zZel3pXaFcBbx2Av5UY23kgqRfYlnXnynm2ZMxGJhpUo0_5DzgE120UPMK8cKEjMmw3gmfeapvUkFi9nGx1h1FD3cJPy4_xP0Ygn-MQ4KPjKbn3_HMD96KvlZrhrA4jFVSseghrDz_F-J5ewynPhqZD0ajjU1pd1LiqsvLxYwTCc-oKhz9oZc8OsaGEOnCsATIu8-2IwvBrWLpFVRqyM5_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم ۲ ساعت پیش پست کنم منتهی برقا رفت نتم قطع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82575" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82574">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1d7_rl-qIIDeBcGeGV-yGEGehpHAIS1WN_TXricCiedn7YBymLe7Xz0Rc90KZ7xJydbQnTANOJieM-nJpF68VKY5u3C9qDJQJ4Yh10m7ivpxrETX4CiY5AGbTMXERMQ1yBipQ6BXUqzVLuZ3rwB5daXsazMkYKC5mKYDJYWkPvVy_eYObn13CiN9pve03agqBOmCzQdFohQ0DVUs2zx9NAn6gXu36g11R6eHWywbSLPlAxkHK6UanJ9NnU8WudvtJLmMwTcgbHty6SXqm27ueMphv21dJ8jCftrsWfUtNgubO_LRa5VTjtb7Z-bgOKWOWEg5u4xj_ug8sao3g-Bzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریر تلخون تا اینجا کلا دوتا نقطه عطف داشته:
یکی اونجا که فان هیپ هاپ تصمیم گرفت مسخره‌ش کنه.
یکی هم الان که خودش تصمیم گرفته از تیمارستان امین‌آباد تهران دوست دختر بدزده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82574" target="_blank">📅 23:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82573">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzYo6RbPYdXHn_ASzkBq8YCC2D0krLtwBVEuRhVaZJAynwe8LGy3-WQSd5eSTGEQnaeLF0WZdpRqYV6WaXJmp85acqnAVvPZPsT__Msk0hC-TUvOU8xM1XrxT-oqFP_KeoZlkLuZBwwQRK5dYdpsyjXD3zdGB2lhHOImg32_Jlz9JQn2NYj_mrfXeaRi648tdiq9z0WErqZz1BDp7K6N6OSXBHJsaJGGY3OZnYr_xBZAAsEYvl78DwgUAQqRRl3kkbWa6oX8ETCRo4fjH0xTtlWnL6k39jL6HysnXwRtW_e21eEejw99tmsaY3ARehVtYOfgqflI4wu-wFNHFHAmIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهره هوشی اگه عکس بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82573" target="_blank">📅 22:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82572">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lvw0JicCGQYJf-S0ei6X35BysmhAcaCXq-XwCANR8e0cd2Bk7I7q4tq4pQXUa1O59AD6tq4YBR7PjeGG891sy8ehBl4uJRmpFo4eDIvAubEx6RaQ3NTgkeHnd0o60CzOmvKtrF1TQYhWUHBY8a5Yo5nM23FVtqicPeRrSTve_GMjU-0A5cNw1EvMYK7_XwWwXbNaUz6DjLy9vqHG0BvWB52ifmJLdOE5RTHB2QCS82wR3eqVJ3WFlVdpGrIWOuSqUW578UfRxfy-IrSKlBV1W-GS6IfHiXwW3txOqwzXSPKQiQdwcDqu8i2wzlxmhJ1VYlROKHSoDJUfPAHOo1FGGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82572" target="_blank">📅 22:26 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82571">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82571" target="_blank">📅 21:47 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82570">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKB1ZMzaj_YNsupvGdLXarW8xJ4cKc0KjtORPUbEa7_fOKoolk1ndQspadj4B5ow9TbgSKlmBJg8dqCEML1apc5fH6ijtepCI7vPQbY6dHGyIxriQ56D5Tf49KFtEMwyepbS4R_6GAZ_8gfU1qSo7XYrTVzpfagMGiYjhrZugwxeYcT1qtbBBQ8BJZfcHdozDtFxsUYjWKUTZ5Vu1uOo1jHxE9QK03xIVcMkWB0YjdW30v_2JCpuxvfPfJdOErFn0MLXui_tpJchHgtB7BeeoOPf6K3WBMqbOwn-syx6pSgY4PUjBNqmcbDOjEzc1RU3t17QK20NyWmR7Mxx5fabNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید داریوش تبهکار و بیگ شگی به نام "Vice City" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82570" target="_blank">📅 21:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82567">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(blue)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49661a4016.mp4?token=hdBTyjVILLQClvmP0YDSbooWfSmKrvXA_QpJ1tq2e7mGiEdK7pBK2U9d7TQOaENgXFMhkF-Y6HDB01YebFLveAU5k5Nckl6_HcuEh6Zp3U97xMcmr8fjOeB7CtbTruMg5hmCaehA7rYkyznCG-Tx3uXNfRAKZ0m0N1wot_z6LPuORzoGJSz_CiqK3I6961A-DK8tM0XbNZ8L_G3898iWAB8ZHbyQyWti1djjryfhLMGs1x0NMnn3N91omp8m10aX5dmTJmsN5wXpPXlSfQsCQKB3ei49tmZm0kIhWAW87QbfXXtGqf11jwOsyzw_YNspB9806AfQHVpWdawS-6ue5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49661a4016.mp4?token=hdBTyjVILLQClvmP0YDSbooWfSmKrvXA_QpJ1tq2e7mGiEdK7pBK2U9d7TQOaENgXFMhkF-Y6HDB01YebFLveAU5k5Nckl6_HcuEh6Zp3U97xMcmr8fjOeB7CtbTruMg5hmCaehA7rYkyznCG-Tx3uXNfRAKZ0m0N1wot_z6LPuORzoGJSz_CiqK3I6961A-DK8tM0XbNZ8L_G3898iWAB8ZHbyQyWti1djjryfhLMGs1x0NMnn3N91omp8m10aX5dmTJmsN5wXpPXlSfQsCQKB3ei49tmZm0kIhWAW87QbfXXtGqf11jwOsyzw_YNspB9806AfQHVpWdawS-6ue5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#Mews
🗞️
“ NITROUS “ Don Toliver’s New Album
Coming Soon
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82567" target="_blank">📅 21:41 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82566">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=OO0zXwxOQeg_nZPKYf2V0xBLBGGZOU5xul_oVr8Rz4dMd-MeW3_toas2f0ERVMDPDiaoNUZ4TOP8k7gdJ19WmSI8iRCLUyMBkvCZ7tNJLe7lbQf1ykgnfbZESCLA7P85HSHPRecZhJIf-JDYfGPBJez7PtZWHLV_Y2--s9STiWrhRsxrNcuHqpBdybGq9q0_FRHqZlY65aw42q_nNt2TDMJltm8GOt7aX4DbXc5SwBgwpMLfdI6pn-5enpKm4Vd1ZkuB0sGp5dhOfrzBmDZ4JSUubUfLp2eCv2VXk96pHghasn9eADYK41ODtOqwaEET0X8ZcmvEenRU1hUoCac3GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024532bfe.mp4?token=OO0zXwxOQeg_nZPKYf2V0xBLBGGZOU5xul_oVr8Rz4dMd-MeW3_toas2f0ERVMDPDiaoNUZ4TOP8k7gdJ19WmSI8iRCLUyMBkvCZ7tNJLe7lbQf1ykgnfbZESCLA7P85HSHPRecZhJIf-JDYfGPBJez7PtZWHLV_Y2--s9STiWrhRsxrNcuHqpBdybGq9q0_FRHqZlY65aw42q_nNt2TDMJltm8GOt7aX4DbXc5SwBgwpMLfdI6pn-5enpKm4Vd1ZkuB0sGp5dhOfrzBmDZ4JSUubUfLp2eCv2VXk96pHghasn9eADYK41ODtOqwaEET0X8ZcmvEenRU1hUoCac3GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی حاجی پشمام از نسل جدید ناموسا اینجا ایرانه؟
😜
ناموسا تهران کِی انقلاب شد ما خبر نداریم؟
😅
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82566" target="_blank">📅 21:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82565">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Xyvwef9_C2CTVoq7vGhAYvy1z0avIaE1j17xMGlaVkMcACbFFy-Fl-0Rs1Yre4tA1FnNWW01XgNe1ivX6xMEO_zoSCzApUanusfkC3ns__oU9ijjTSYcMPkc996fQd-SGOOrq_GPm5rsh0Zn6oDpOnB70XuDt6y-SModwg95y0K8fTnpL9yoYS_fKVXPK4loTpbfwT0mcOOddDf1GIsD8B12jO79r0q7fMCjBhvYU16SdbJAAD8rCdPKXWmLoouQzH0CeIyNqAEvBZgEiKohja9qb00jIMyC80-ja0jYdxKyLXmFijWsvyaf3ZUq40inHYV9WgAgKMe9GNwHeEj7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bb65d06f1.mp4?token=Xyvwef9_C2CTVoq7vGhAYvy1z0avIaE1j17xMGlaVkMcACbFFy-Fl-0Rs1Yre4tA1FnNWW01XgNe1ivX6xMEO_zoSCzApUanusfkC3ns__oU9ijjTSYcMPkc996fQd-SGOOrq_GPm5rsh0Zn6oDpOnB70XuDt6y-SModwg95y0K8fTnpL9yoYS_fKVXPK4loTpbfwT0mcOOddDf1GIsD8B12jO79r0q7fMCjBhvYU16SdbJAAD8rCdPKXWmLoouQzH0CeIyNqAEvBZgEiKohja9qb00jIMyC80-ja0jYdxKyLXmFijWsvyaf3ZUq40inHYV9WgAgKMe9GNwHeEj7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرات حسینی تو ۵۰ سالگی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82565" target="_blank">📅 20:55 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82564">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSB4t1haJobShZkCSvP8xIEXTYwF4f3cZ3S2UMPLR_ymPk2Psn2JMjrdktZMcH4lIy-lxYjuUGLy8aGX-_vxZGItWCJ-lCatnwnSY5rwJzmRcxoD4rK7YmsVMVzyC1HIKI8RYOKMXEy3f_vsXnDv4Y5XBnABgRtKAGvXPhKpdUGI4R9if1QWwG7bI51TekPP9XCLG3vkbXcUbs9C4mF1exky_BpRutzciHYwoYA5KAxfjZsOmiSxOvsotpu1hGABz1zCcODWu-nKRkCoX5mGFQsqdnAORPf5gQQfyW-dgoj56UEsXDkgkrmk0JGwKN8-O158sk5n9TYjoUeVF9JIqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشکل ما از خارج و تحریم ها نیستند مشکل ما مسئولین فاسد داخل هستند
اقایون مسئول خجالت خجالت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82564" target="_blank">📅 20:27 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82563">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کانال 14 اسرائیل:
ترامپ به تهران دستور داد فوراً کشتار مردم خود را متوقف کند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82563" target="_blank">📅 20:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82562">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82562" target="_blank">📅 19:48 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82561">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-i3To1m2GbQ90PWXroSvPHM1U2WR2bovmhCymP_UCvf9Flp7_j6rVWkg8WQnkMhmFQd3zWrwlfuUE1SNFNBl9alk0Rav_kr8avyW4JbZ1lXCUZb4zx2EyOLZtuPc6MIpWlIzbckArefQU6JaSjN1XsthZsHD-WEftEt_8ZYe1VYryOVky8Txy_xs5gkKtCX1GJIRJ7n-IyI1ynirdxeFXmbx7ix1OVdXOKu15Br768OCFXnSISYRiiuZ6e3HW1DfTWSPF4k4pZjBQkgrNsVJw-onyjynSClco0aDqkbUsSi6FbcEKGJzpGLSXjUlrmIh6kY3udjbyJX25zXo1zLfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از زیر این توییت واقعا گیف های شاهکاری پیدا کردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82561" target="_blank">📅 19:46 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82560">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qe-nUJAtJHgLxwirJRXGDQX9Ra4I5EwmQ4s515NcX_J98PsZW86GlC75yqVMTvlgeACg1pb8H2VbIXFo1RrtroCi1BiUI_e5iu57RIaXbd3Hr3lTrkFBmZwEaVW7NEz5eVW-LPDtlv5TVlnOIU-CdGhBTRlOcAFOuRwEffee4r0H0kQtL2lQPjuh72ixt55sms6HNlENhF-yfndc3-XPveSy8qN1PcrddFwV3uAXkWUYs5IS1lHigGtJ8Zo2ixLWOtXL5DKK5SykM5wnbmCC8qzjBpgBQ4ukZQWHsl3W9kf5YylDJQUoqRgsR8rPUN5w29zHKBB91fxPST13cOoT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرادر آزمون دیس ویناک به پوری رو پست کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82560" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82559">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به بسنت باید بگیم عمو یا عمه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/82559" target="_blank">📅 19:21 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82558">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvrAkBZA1uKYQHcJw6Qw-oMgdv1VskYVFF4RrbEBCmjksRfUlxeDle5WUErJB4uIEgGSxXMGw2XTiWjClxAjplkYz8qlu0Zu7AFLa-Y05Trp60YmWlPOa0f1a-EEoY5SvlRcWAMtSFOqN-QnvXgvCPM6gWCxY0V54H7einZJkAPhEFeGOJWYc6goE2sfL3Wl-sXinNzhL2-LOkSNXMjrXy7RdP_5Nf1YUuitbIa_-Xtpjjic2SQtRlkNioWFEwom8TP-mSd_Ued0yzwoOlwL_tDNU88m9mdIVtvZLD_Os9GIdOFNeKb7GjBv57I4qQNUQhKuuLPcRpJc6nrMxS5f3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویسکا آسایش ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82558" target="_blank">📅 19:01 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82556">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SpHKkzt46G2FZ-pnnCkOkI1tLsz3cSA1RI-2yDFsD1T5ujORXC8l7DnsUja38VNQ5djNP5a4BfEBGGJ4wTulWtUGXF1AF4LZqcBD6W8ZDjI1_FB4umvJSs7WsY1NFlGuGjBlS9CKNOdq5BwlqrdWAXYNhsUccyMYy04Y51Pc0Hr3GOVS27Jl_LCEm153MoCMhIc1GxMzSt-w1jXJLeR-ZJcZVQ7i_savSF51rY9eULFGNLYskP5BS-5823o6SgYFadKXhWCDN0szCEGOsc4MrDssm1tUzyoopp5cA9bApQGyU700C0yWyMmIcD2KedCyRGw5iv4xjTd5YAY2eYBInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام HESOYAM ریلیز شد.
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82556" target="_blank">📅 18:35 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82555">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ترامپ:
همین الان از طریق نیروی دریایی ایالات متحده مطلع شدم که تمام مین‌ها از آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند. به ایران اطلاع داده شده است که هر کشتی یا شناوری که مین‌های جدیدی در آب‌ها قرار دهد، فوراً و به طور سیستماتیک نابود خواهد شد.
از طریق نیروی فضایی، ما تمام مترهای مربع تنگه را زیر نظر داریم، همانطور که در کوه مکوش و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند، این کار را انجام می‌دهیم.
سیاستی مبنی بر عدم تحمل مطلق نسبت به قرار دادن مین‌ها، به طور کامل اجرا می‌شود.
از توجه شما به این موضوع سپاسگزارم!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/82555" target="_blank">📅 18:11 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82553">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=MkBndWKwUSeZr7YyF7mMJA4P3DEDWQ7SJlE7sn_qyd9PyoZdEULW7sCUeTvyyEqgyyTNmWFi1C7BkdAhMDTneH87N-CSmuTDXxHUOqt3TgakoptCsEoN2hCHi5eTl368UVgvig4iXQitFeOtoXzPfQMgyl_yTrt0hDQXoU7N3rAFD0PkVUJ814Y-yfeHKWb27oNIAWugxM1wEzYlMSh71N4vBusPCDb_8zXSXo8xKdUXdFQxi-YNC37H6oNHIi8or51NXA_TsTdgt9644witP2BvuQ5aCD3Y0_TVX194BYfBXj7LkDMWWe-oWc4s3VslFCpDSMzuEPIg8Bwlra4DtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ebe602ff.mp4?token=MkBndWKwUSeZr7YyF7mMJA4P3DEDWQ7SJlE7sn_qyd9PyoZdEULW7sCUeTvyyEqgyyTNmWFi1C7BkdAhMDTneH87N-CSmuTDXxHUOqt3TgakoptCsEoN2hCHi5eTl368UVgvig4iXQitFeOtoXzPfQMgyl_yTrt0hDQXoU7N3rAFD0PkVUJ814Y-yfeHKWb27oNIAWugxM1wEzYlMSh71N4vBusPCDb_8zXSXo8xKdUXdFQxi-YNC37H6oNHIi8or51NXA_TsTdgt9644witP2BvuQ5aCD3Y0_TVX194BYfBXj7LkDMWWe-oWc4s3VslFCpDSMzuEPIg8Bwlra4DtzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایع فازشو داره ها قشنگ.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82553" target="_blank">📅 16:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82551">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vf4xzIttl3TezY5OXyIQWPrGmG4aDfO5ZtYMprf42K7D1CyYJesrzvHv_u8HBLoLY1oSr1NGXzkiUxaZsIa11Vo5LQgXboLcyVxRa0R4EpOoH4k_DFlxV6jeUYRLwsVEAi0ucGHYYYWY74FvlDArYOmNrLXB0CxILb_8iVmV56pJ3RZOyaIQyvTXXm7r8Vt0Bm7ebNFiaPUr_BUIPMjzJyr5Bx45aOk_b2IZvr9hWbua8T-_tNsIg5szZ1L3xyufebcjdUOuZo0IeUVA-0i-tfxTtuAKmd5_rfJbKY51QCZkuSYExqYUgCyZmtQC2uimdeO4jfSI5NZTHmvau3MWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باورمممم نمی‌شهههههههه
پسر ایران بالاخرههههه برگشتتتتتتتت
🥹
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82551" target="_blank">📅 16:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82550">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=vd6s-FyFMwZHGxULmgbPcprzawu1aSD8vi-9PKMNfa04EU4Nx_-pZSndCEKyVOJLg_E9V_x4OmD50x4gP4LrRG48hvuLLPTuqdwign5gJheToS2RWNGJl1DCNG2ShaSEItXkaQOLMKhIe1Mo5CQFZEslMLWeEHVIimAM3S1Z2h9SDHlaybaWw_lz8lW_r_9EjkzlSMDfc1Ntr6Xlwj-GvoIcf3qd91mqVH4YxSyeqm_gP2Yd0LIhemFYYOT87wMx-RBar2RPEnRJFqmVoYI6iXGLPNCzipjaDlcu6h2k1LetANkC3Tmvm4lUIbGsD3RT-jMISvvxxBoDt-5Kre6K5A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/adacd9a9d3.mp4?token=vd6s-FyFMwZHGxULmgbPcprzawu1aSD8vi-9PKMNfa04EU4Nx_-pZSndCEKyVOJLg_E9V_x4OmD50x4gP4LrRG48hvuLLPTuqdwign5gJheToS2RWNGJl1DCNG2ShaSEItXkaQOLMKhIe1Mo5CQFZEslMLWeEHVIimAM3S1Z2h9SDHlaybaWw_lz8lW_r_9EjkzlSMDfc1Ntr6Xlwj-GvoIcf3qd91mqVH4YxSyeqm_gP2Yd0LIhemFYYOT87wMx-RBar2RPEnRJFqmVoYI6iXGLPNCzipjaDlcu6h2k1LetANkC3Tmvm4lUIbGsD3RT-jMISvvxxBoDt-5Kre6K5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب این الان یعنی چی؟
😭
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82550" target="_blank">📅 16:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82549">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoQe6dSMW0clKiDb1XXhCpezg0nSpC2v6ozq_rL8kF6hLLBB6Jd0e7Td7mHLu2XmVoLHxdaEWla6GoQhtK8dgRdeOPfJOXq941doiaT7rO1dOSGfVPIQsFmz6RNQO8Zo4755HwZMb_5_tQVLB6fuyYQtKRJWhaLWSi24ev0dsUJcWmD47fBxs-sMDhkPCSXN-7_AmosifL8XYy7jNX4QeNE5oKvXd--rEljAvtlVz7QVMLsS25PDx6ePb3jyzt0su8osHNcZpX-RZWLkMuj02S1YupemAOEd5sVHLij-sRnFYkXMahYQHBYMx21QhekUNPBNaWYWSErP9F-MHlQoTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۹  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82549" target="_blank">📅 15:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82548">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUWRgnfsVG8wh_YaUY3D3PCqqrgUr4HWjI5Xo3i4xhGKJnCQb429-2UPuvwuFqh4AWduCzGjxsLNCEVmzI0UgqW1f8RXSh0s0NRKSdOfVNAR66DxLf5Jj7V_2C6d-c_xiaJZCRUwIGLVKYimlHCDa2CCBahQpji_q1S4xgFlrxxnawuFNmVHka0Ufk1mH8q-HetIdFAa1T4JBwjsoM0GfsjWHmG9rPhEwBI1idEUxvkcb1vYHitzIMeCSvLwSor19FL_gBDnNzxd0z-QOp7Na75kYftivFMHrTW8Sop4NxAS3zadwQzuY9JBGFpEhYpSBx7Cy0X9yZSaS91-9cIwiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یعنی دور جدید مذاکرات؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82548" target="_blank">📅 14:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82547">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کار کنید حال کنید حال کنید کار کنید و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82547" target="_blank">📅 14:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82546">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZJqxttPIXiotETICoouq14MYzf23BDhXZK5aZmWny3MURI_K42OZ0DHQWAZEYP5g0G2sJ3UNwZD4tSohhmBjT9Ma6pPWiXo3lxYZMXDxZp6juj6wJyErkHlQbB13cflhY9jRvOKr-hNHmI6U9kXW-ZouHCvRZ3GpGtEKXPVsKkVqiEjIJ0SNAEFKCfVFuCit6fUvqIwQura1wPF7kP4-MnoavI5wNUMLOROqcUVy3_6k0x65pCB_nt6wdgv3_aOHRJb0_QYkaKX9YNd6FWV5tbxy700vBaCRTgaPt_lWZI9ug_WSeojxuaMKgZhtZllaPEWycK0grpeq89-FkR2fEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عکس دیگه از مهدیار لیک شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82546" target="_blank">📅 13:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82545">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=HPBldJTbbPc0nrjd32Od5H0c83Y9t3NZfc6XW4D_xaMmOJuYUqX_UiFGh6tdmKdGHpEKkjPvdH7DE5HpEwNRLRwdIC9EC1LYynTPMzS-vVBQU6qeivuKMODM6T977DbpF5JMeK9TENg01z9IVYN3B1soL8gfXKQwD2nApa1sWxVvmITRP0TybB9k81TrL9ChIxpM5PMew03IvdWN5yGIJQmcQnZwWMInSeYDfWAnrcPGEbBHxib4CAQn-sMp6gNhxz7kwz0MIqXWt1T5PHApfyynoesvbD8MqCqVKLL1mBVAYi-06klgpG0AQZXwBy6s_yNilEuwdHozrY8_ZFAmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9968bc181d.mp4?token=HPBldJTbbPc0nrjd32Od5H0c83Y9t3NZfc6XW4D_xaMmOJuYUqX_UiFGh6tdmKdGHpEKkjPvdH7DE5HpEwNRLRwdIC9EC1LYynTPMzS-vVBQU6qeivuKMODM6T977DbpF5JMeK9TENg01z9IVYN3B1soL8gfXKQwD2nApa1sWxVvmITRP0TybB9k81TrL9ChIxpM5PMew03IvdWN5yGIJQmcQnZwWMInSeYDfWAnrcPGEbBHxib4CAQn-sMp6gNhxz7kwz0MIqXWt1T5PHApfyynoesvbD8MqCqVKLL1mBVAYi-06klgpG0AQZXwBy6s_yNilEuwdHozrY8_ZFAmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو عشق ابدی ورژن آمریکایی یه دختر ایرانی به نام پارمیدا شرکت کرده و اون ته مونده های آبرومون هم برده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82545" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82544">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=nNoy52JWOd21dIh6HmtGhJ_dKZeZOqUySUAlFnGsCXUhBruUiwn1UVnyQYz6m23F36zSgQ2ZXliZ9n69GW_auwz7NIbzQAb1NyCwEVCY7SgpqGvs72fyHN7XORpg_o5aIZ0CaWQu0FpUrTVsMdp3wvT9LGbzVk95xpLUzb47IFPgOYnAWIwg4w8za8LJ-WkLJrM0OITcuAjtILQ01z-FSAEw5RF8O2fAluR0MdZkfzQuHFv4gmeWXuATIMp2XBSYAtBw2dLdK4_-0uJiLL2lHxcQ62zitJcHni17lxLKTFtNYN7cdhehGsQvWPhhsfrFBDkgVAMv4Wg0NXBfoLq6nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec8056f1f9.mp4?token=nNoy52JWOd21dIh6HmtGhJ_dKZeZOqUySUAlFnGsCXUhBruUiwn1UVnyQYz6m23F36zSgQ2ZXliZ9n69GW_auwz7NIbzQAb1NyCwEVCY7SgpqGvs72fyHN7XORpg_o5aIZ0CaWQu0FpUrTVsMdp3wvT9LGbzVk95xpLUzb47IFPgOYnAWIwg4w8za8LJ-WkLJrM0OITcuAjtILQ01z-FSAEw5RF8O2fAluR0MdZkfzQuHFv4gmeWXuATIMp2XBSYAtBw2dLdK4_-0uJiLL2lHxcQ62zitJcHni17lxLKTFtNYN7cdhehGsQvWPhhsfrFBDkgVAMv4Wg0NXBfoLq6nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این روال عادی ایرانه، الان دو روز دیگه باز همه یادشون میره تا دلار ۲۵۰ تومن، اون موقع باز جعفرزاده میاد یه ادیت میزنه با آهنگا محسن چاووشی و شایع سلبریتی ها هم اونو اد استوری میکنن.
پ‌ن: البته خود این یارو تو ویدیو حرومزاده ایه که دومی نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82544" target="_blank">📅 12:52 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82542">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZ9CGlpJija8HwH1c3XH8h_jguqA8VKSQzHT_tFUcN0ug9_8pgdgn3AZInF2Opu_XspqrO-fhzEOGUVRJz2c3TFOhbmE3auejmffZUUOI1YPpqoZDpat4ftkCOf1n-5B7iTT-zSBOafZ09RqiWM8wB3jkXJXVDwS4QhFuVWQoys9dRe1YU42CWUbRm0VKjQY4PnSUdEFdCG2i3nLnm2mv2t7ChHDivzW0UVkV34VbV34idZHeEokbcr8IOAsMlLb_fbFl31aRwt8gjp_KLaMzNjKl_ruQEpcEyfMlmT7qAN57SbY_Ql9ZggbP18JQyGz63XG42T6h9NZUD2mL5UXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری نیویورکر:
دولت ایران به گنگسترهای روسی و مهاجران آفریقایی در کشورهای اروپایی برای ترور، ایجاد ترس و آسیب رساندن به ایرانیان مخالف مقیم خارج پول زیادی می‌دهد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82542" target="_blank">📅 10:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82541">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBJggOm5WpGq0mfEA0WMlqlaTy5nSzv1blDVNnvvVL3-m5GC94ApkBCSeFxkgzU7gC8xFTHgBszWzv_SlWA5HWKyDT3TDZxjU5_IV-M5cfVehxP-gEk58uVKXpolnKsEvpPYoz7CvrCwlrIL4qmH82O4xYob_Fxr6I4sX9sI9kqIKOGteuc3QEnePseZ20WA1PAYDaPfn7_87I-xaqgnsxnSJm-toZ89Wl9SBSzVbf8nkkzWScLEJjVYTWc_XwX4PaPxK-L7H2DAq4ztd4q2txjUkZPAgVX8AlaBO5Hr3d_oqrAjff3L_eRch6guIwoNQfb1D8Fn5HCm9olyZb-vlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82541" target="_blank">📅 00:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82540">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">همین فرمون پیش بریم مردم تا عید رفتنی ان</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82540" target="_blank">📅 00:17 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82539">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA7upt-EsaHqSv9-fk9Gb27_bCxgOHw1WaR6pXD0zU05AOTCmc5bP3hE0cX38kEy51zIQR95fJ-s6TB5FCxHabpiLMAa3FXNym4-ZQQwePb0iSGj3tCSv8pLTpfuv-AwTyNUUbgk2c2CkskRyfdqrXXGK4tP43uosAYmKvVqgQoKt1RqI9veki01KvB-cEtsTyCzIBAsLk-0JA6x-k9sleNOb2kgM5jyjtlZ9lNc_qMCZAVz6SxYl4bXtQRILUU_iZ6DavYfU7X3lHIGoH_K9TfNXN3d1Th-c1nvJCrhtsiGDB1zoRENSo45H9WBbnloQ50WdwsqfnurdWWRJIAUoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکای جنایتکار شیطان صفت هم تا ده میلیون دلار جایزه برای ارائه‌ی اطلاعات از سرداران عزیز سپاه پاسداران انقلاب اسلامی گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82539" target="_blank">📅 23:59 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82537">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">عاصم منیر حتی نذاشت حضور پر مهرش تو ایران یه نصف روز بشه و چند دقیقه پیش از این مرز و بوم خروج
(فرار)
کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82537" target="_blank">📅 23:43 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82535">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gtfqRnWLEGV8FyiAFE5gUxTaZihROjLA2bsdiiGBSzZc0hhLwGt-PEfjhXmhg5b0rG4qb5V1RNvd2CVeRzcrwJDDyU3XIDVpcHzeDAbl-z_EZn6-DoMM4O5xt9xCYBYDBww4j3698kmoh3iMbXLBPWZ_YgGXPu01yVNoOfdIRsUZ0RcNXg5BtenS_Gf81YMbcgkgfL0dJFRJqvQHSqg7h_wox3GUY9reFXrrtC2buY1I3FgtVAQHLGGn405K8ylDRHgb2W8TaNv8StQyZfD_xR124nckt4M61K6mIrtwL-QLxC8Q1-xwogNuvP2zxcOXpWNRMKg9pFMKdqI2ZB1gxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fpKfo0oemml1_6f_TTR7FVUVp5wZLY5y0S0D6jAyk4ewD50VJQgLuJEci9GeYY0If2gjgZ4a_c3PGtYKjaFNSlDabl_F5x5b1tEWwMG2w3nNtI8WnUHeHtKkFJBaFbswjVHkYcVHVmpl3B61jzX-9zo85TAvH1GPdOoCGV6oBsVfCTMlbBdaV1pNCHXBtdZ1YTqXd4YWKNj3xBG88asPmYeMm_YxeQ6EbpjJE9wCqhgzI1WaqvDPwEjsal4cldiik3p2thRFbnT5rOyTvTxqA-EOz3TK9FT1hqfFza3d2mn5_LI0GugeIyYb5Tb95zZBWd3YxSmrDcmC4wZIcii4wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به این بنده خدا واجبی دادن گفتن رنگه مو هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82535" target="_blank">📅 23:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82534">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=hBq1ObNBqU74ujPVxo7uqVqVfaiYFEZCtFqD6Ws-BUKxd_up539z0qHF6-gD5xkXmqpIdYWQ4xuhy_fusORK0hZoplLpDJdKAmtBcWSWtDbDGNXuWIshiit6ONiGa5G_ZFrCx3XCaaGBhoaKvI5leYHgupWSSyHA_ZC9gU2Z0k-KjEukYaNbX4AjNRzzx5aKLfDCkd6cSzXCO44E_IMJChRXK3iQutLhVnCv-0YPBWxyXEK60T2K9Qqyc2FFbPy3894d7IlevMo5-MUDlwvB5x1V_cwFNOGYeiZDuPrRaovmaDGoVUHd0utL-d38k6yRryk5x7Z5wR75rKFzH6xpIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41ff961f21.mp4?token=hBq1ObNBqU74ujPVxo7uqVqVfaiYFEZCtFqD6Ws-BUKxd_up539z0qHF6-gD5xkXmqpIdYWQ4xuhy_fusORK0hZoplLpDJdKAmtBcWSWtDbDGNXuWIshiit6ONiGa5G_ZFrCx3XCaaGBhoaKvI5leYHgupWSSyHA_ZC9gU2Z0k-KjEukYaNbX4AjNRzzx5aKLfDCkd6cSzXCO44E_IMJChRXK3iQutLhVnCv-0YPBWxyXEK60T2K9Qqyc2FFbPy3894d7IlevMo5-MUDlwvB5x1V_cwFNOGYeiZDuPrRaovmaDGoVUHd0utL-d38k6yRryk5x7Z5wR75rKFzH6xpIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این محتوا مربوط به رپفارسی هست
‼️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82534" target="_blank">📅 23:02 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
