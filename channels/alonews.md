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
<img src="https://cdn4.telesco.pe/file/YvpQwkNQREldzQAtgSwaqaxZ0gsUzOaPoWmu8aVjFhNAhG6jP1scntY2wqig8F7UwjOfkCYu4CWvT_ImlWIy4P0wBIyBEEPSJ7aaTLL4XeWpEkypondiyRLSad2zLp4Ybhab23pmJRNZLf_s17lF7O5xKLepyiBthM-4yI0FqDNNwqVYGR5tdcs1whQNnJiqgdV2PKpxYbJ6oPf02PvGzosiv7RzHoOCJ0Lhjhry5Fu0qBCDXWOm0wX2CyL6SyAY23bK9imliDliotoDSo00Kq1awxipRiTfpGM2xyVqBjUcpPsHK-R2Qj5ILeh4KReqmpm01_7htFFE0bVrFcPJUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
<hr>

<div class="tg-post" id="msg-149774">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
ایران سریع‌تر از جهان پیر می‌شود؛ رشد ۳.۷ برابری سالمندان تا سال ۲۰۶۰
🔴
بررسی داده‌های آماری نشان می‌دهد در حالی که سهم سالمندان جهان تا سال ۲۰۶۰ تقریباً دو برابر می‌شود، جمعیت سالمندان ایران با سرعتی به‌مراتب بیشتر حدود ۳.۷ برابر رشد خواهد کرد و به ۲۷ درصد کل جمعیت کشور می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/alonews/149774" target="_blank">📅 00:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149773">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dac306d37b.mp4?token=QFL_H31zs3Tb7C-5717ZZ9tHLl7oIFbGkoR7401Z-VZ1nuvoruZax6tLEC74HLT7M1XmAEH-VPNYxhQa-jxnYjI7LgIJNX0JyClbxYPY8EUD91q2lzCmL5JDeciYfxOvX_dz-kyxu_4QozoGCswiK94bDyf5zGCY9VGoEkmMEeo7jLF4bsUyDlynPZQ9V_i8tN2f--aAm83zJ-TSH39_qIVDN_T4f2ywp2zI5bTtNcooXpgqEcJ4ZmSWuzyFPmYIrTBKBGlr0croPdH_YHlkwphED8aoECckePutK4XJriARWNL21JjOmOn4J83HBJKXgLgMFT9EqzbKdIcUbN0MOXni5Fo_G3Vwh7nJrqA4E1jkW10nCLdVk2JAcERrh93AxbyQ4lJSBdTmkLORV3D8BT6N_3qMevE9lXpAvbU-WVcVGZ3z0GRPZ4uZyTLPFxeXPVnpvoiJfKTnBqDrrW3HMp9PFGpN9_9S_xWDAEargbdjfoj1b0oROMqdX_O3yYyx_xu7_z6r7xs2wO22R2lO9fy1W-kUW-8AMs7a8KagltRZe1_AOkloMW5BsS9GPUl91GC1IyrGWwAatKM3wXfacJ7sBMs3COn-P7PPRsvV-axmTwNek9uTIxL4_AJJgm1NWsqDtgzM1WwCekVyEstr50wrOw5G4N5up3QN-nIGwEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dac306d37b.mp4?token=QFL_H31zs3Tb7C-5717ZZ9tHLl7oIFbGkoR7401Z-VZ1nuvoruZax6tLEC74HLT7M1XmAEH-VPNYxhQa-jxnYjI7LgIJNX0JyClbxYPY8EUD91q2lzCmL5JDeciYfxOvX_dz-kyxu_4QozoGCswiK94bDyf5zGCY9VGoEkmMEeo7jLF4bsUyDlynPZQ9V_i8tN2f--aAm83zJ-TSH39_qIVDN_T4f2ywp2zI5bTtNcooXpgqEcJ4ZmSWuzyFPmYIrTBKBGlr0croPdH_YHlkwphED8aoECckePutK4XJriARWNL21JjOmOn4J83HBJKXgLgMFT9EqzbKdIcUbN0MOXni5Fo_G3Vwh7nJrqA4E1jkW10nCLdVk2JAcERrh93AxbyQ4lJSBdTmkLORV3D8BT6N_3qMevE9lXpAvbU-WVcVGZ3z0GRPZ4uZyTLPFxeXPVnpvoiJfKTnBqDrrW3HMp9PFGpN9_9S_xWDAEargbdjfoj1b0oROMqdX_O3yYyx_xu7_z6r7xs2wO22R2lO9fy1W-kUW-8AMs7a8KagltRZe1_AOkloMW5BsS9GPUl91GC1IyrGWwAatKM3wXfacJ7sBMs3COn-P7PPRsvV-axmTwNek9uTIxL4_AJJgm1NWsqDtgzM1WwCekVyEstr50wrOw5G4N5up3QN-nIGwEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
سرعت تورم برخی مواد غذایی
!!
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/149773" target="_blank">📅 23:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149772">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAKN8MbB5q7mfjb88OfuIebNy7ewFFgHrqKay1DKqZRYlIDfiL3Mfeb3Y4LakJYulwzd-7b0FAdbYAMVCDSuDu8NQ2HBmc0uqFRG0BPTKc_HHC8MJyj-Hrq-kBtjKrDjPl4l1CQ9i7BQBe06huXnrsc5eK6bLBM_W4X3vVaervye_RRTUI_as9oCmhUDby51X1sqnRv6Lsa6jh-lKEC-A1CcYjKI_v96gN9WazMmC0HjIniwOT3vGjoMU5iR-ZT-zsQbaR5pOiRvpfYTBdrnggXDcw-MhD_rVbA-CUloX4y3CA_Q7W30hB-ZMitMteQlmLfLMG2niLHgGF1Ik-iPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ بار دیگر نام تنگه هرمز را به "تنگه ترامپ" تغییر می‌دهد و قطر و بحرین را از روی نقشه حذف می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/149772" target="_blank">📅 23:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149771">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bz6jodpb9F9hny5SbTr6wfWUJgqveb-PRDVNpsO6wSmVOR6Q8KnHg8q0PeyNyt-i5qVP4GP765f2OLAn4yhwjWhFrs1YcswhRM2ROVUnc31ihCYssdlJsW7VhYNTPDfWnut9QA8MYMnPaJXzGzkNM6zOuO9XScMNS2p40ExgNkL0JOkT9Um7qVslQ_0BnDlRtWpQUCcx9RWrhMTFVAFKCvxoYzNiWe5jZiyWMXyOxhkRW7D7N_p56Kce5F-_SXpfnIV4gAa_XPObo9pGwXCNJklsdtb6x9r5WHoyAeOBRlPLYdIhziLFEXkbP_3OAveFCi5S90V8sm_ekEQyZ6FPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/149771" target="_blank">📅 23:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149770">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
گزارش صدای انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/149770" target="_blank">📅 23:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149769">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tDjuzJGqyj7DFcYNHeZuF59lPssG6cyDAfnW2R_TCN-uemuNimgW_FI-6EtgCWm3WVQo2a--PJZsyzE4ZuBpEGen4YZm6QbACsREKP84i1LF3SknDj-dAIbBfLWYRaey9O8limhyhSX0ZK5ieZ23ZSJRxdk9uuSivQzz4OAeDlP61dJ1yfn3zoiKe-4-TjVu5rULR1bgQ_UyUF9Q-0ibyBIsd3ZTPdBGqe7izaVOkG1TSWcV7oWdVgfxbKellOyyif9ZFQOM-VFtqGtGeMi-V2hneBwSN4BaeptSXX9V1NKK8WysVMwxStvkoe3xUaRhUsLUoT9on0USnMDVj_Pwyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیده شده در تجمعات شبانه ترامپ و نتانیاهو، خودتون و زن بچه‌تون رو میکشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/149769" target="_blank">📅 23:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149768">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ایرنا: هیچ برنامه‌ای برای مذاکره با آمریکا در دستور کار این هیات قرار ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/149768" target="_blank">📅 23:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149767">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
عارف،معاون پزشکیان: نباید برق و گاز صنایع قطع شود
🔴
برای عبور از زمستان به همراهی مردم نیاز داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/149767" target="_blank">📅 23:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149766">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_zMnhnqoyDvLOuNIPM0eBamhhMlK8ompj0K-jNsG4OPfYlfQs9CX6O5asT-n4C2VeC4-Py4FJ8RaP6OxZNWXI3Xkm2zHPZfu9B3TX3ztZaSSpRgMTCk8znW09J0CFo7R6eaXr_wzC3ih4PMg0iHyrZNsdUoHLylEzYTfsl32OM7lxNAyJSwnFOfI7Ojsg9QVEwK6XC_mz7ZIkexOuyo0zoksL2ZBnXAvooeHp2Y7u6TlwZ4tZnzBVrgJZiVaNhP9rDpiPPw61AO_udxtv8SrG6rO-GFGfGwnWoFQEV7wsRKRxstDTeGcgumwy_JtLC8kODxXoWvBShljtn3AGy0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
۶ فروند هواپیمای سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/149766" target="_blank">📅 22:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149765">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
میدل ایست نیوز به نقل از یک منبع آگاه نزدیک به دولت عراق: ممنوعیت ورود پروازهای ایرانی به فرودگاه بین‌المللی نجف قرار است طی ۲۴ ساعت آینده لغو شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/149765" target="_blank">📅 22:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149764">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vT-uTUhNxl6rYyoVQsvBaPGBLjLuRSNbmqvlQh5Fp69wfe4iKAUhaUaMBFE62x6LrJlbjJPj6VoKi3UyasSIr6QOAjdQoAP9QwqVeBKn6O1YpKoDLOB-GyBnw2TqFNtmUC5KeD4gKkqrFQWUfrZGvSXIAxDkQa1tCqHpaI5hgCZgISwbgsEa9CdXqHEq8OFyGiaYRu-PpVwVj4rl1rJHrZVX_QJHJveeMPsalX0lWVGKojyNAlzyra2zVbev-rDb-q67_EUGylJXC1L_ULIEuk9VlodshbklHXwRE_VoKakyrWM3Cqy8uJHrlgEO4esejNea8m2eKfWMwBUMmZ9iDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: در حق من ظلم شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/149764" target="_blank">📅 22:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149763">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/149763" target="_blank">📅 22:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149762">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
خوش چشم: یک جنگ دیگه در راهه و آمریکا قراره شکست بزرگی رو توش متحمل بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/149762" target="_blank">📅 22:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149761">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
کانال ۱۴ عبری: نتانیاهو امروز برای دیدار با محمد بن زاید به امارات سفر می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/149761" target="_blank">📅 22:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149760">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=j0UeHi0bnHVk33XR6Wk2lWSnw2khomlUToLNoJ0gdPTGfQs5JqFHLPOOvecKmQpsyHz0j0eCECXqH_r2G3zTC51z9zZm8zq3iOM6S8Adc2-WUHPgjmQ_B0hODzuKL4Odbq6zlohu2IRZbx_9wT8SCcJtKdQCF7rtf48kH2lRsSdJrDj7zAdiz7g9BHWXDJFkORaba8CMaDFpWWBxjI4GkTOPLPXftByCXHu-FWa2UVf8nXhR7G246cBf4KgW8BMMAo53yf8PDJPui9pYrpQTC5rAS-lBwO-MweZvkm4y_6SJ3sKXofz48Abhr6xbMCK7LjggNKmkU7zaR-AM4qgWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c75d2b725.mp4?token=j0UeHi0bnHVk33XR6Wk2lWSnw2khomlUToLNoJ0gdPTGfQs5JqFHLPOOvecKmQpsyHz0j0eCECXqH_r2G3zTC51z9zZm8zq3iOM6S8Adc2-WUHPgjmQ_B0hODzuKL4Odbq6zlohu2IRZbx_9wT8SCcJtKdQCF7rtf48kH2lRsSdJrDj7zAdiz7g9BHWXDJFkORaba8CMaDFpWWBxjI4GkTOPLPXftByCXHu-FWa2UVf8nXhR7G246cBf4KgW8BMMAo53yf8PDJPui9pYrpQTC5rAS-lBwO-MweZvkm4y_6SJ3sKXofz48Abhr6xbMCK7LjggNKmkU7zaR-AM4qgWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی وایرال شده از لحظه تصادف
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149760" target="_blank">📅 22:16 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149759">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=Ad8x4Ro5tHtR_sFI6Lp92CIXsp6ia-mNBA-rTTk_Dc4241OAVkdauxb7MtJrZFmXSPRq7b8BsYWw-8_R07Ykr_F-zbHjxVOYnxWswD7IvaGVYEGbn5JbBDs76cS72--L-99ECdE6Z5hPCLXyD06vzOq6j4LWBpx-xu8ZYk-JFoctCwOsMPLAApcdh0wIwejUpTTSFOCGqQeaqnMrBwd3mqGCq0cOyRzsO1zRVr6DVYLvtfzxefgx7viN3mjdQMn0_yhVVx2pDk66F70H7q7Z2gFpjJdk8hqg3KM6zm2pS_zZxwGdlmNkTmWqzhfuZ_5ZLCIowv_uZUZwsvkj3wXI9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e1f47427.mp4?token=Ad8x4Ro5tHtR_sFI6Lp92CIXsp6ia-mNBA-rTTk_Dc4241OAVkdauxb7MtJrZFmXSPRq7b8BsYWw-8_R07Ykr_F-zbHjxVOYnxWswD7IvaGVYEGbn5JbBDs76cS72--L-99ECdE6Z5hPCLXyD06vzOq6j4LWBpx-xu8ZYk-JFoctCwOsMPLAApcdh0wIwejUpTTSFOCGqQeaqnMrBwd3mqGCq0cOyRzsO1zRVr6DVYLvtfzxefgx7viN3mjdQMn0_yhVVx2pDk66F70H7q7Z2gFpjJdk8hqg3KM6zm2pS_zZxwGdlmNkTmWqzhfuZ_5ZLCIowv_uZUZwsvkj3wXI9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: ژاپن چون انتقام نگرفت باخت و الان برده آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149759" target="_blank">📅 21:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149758">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">وزیر خزانه‌داری آمریکا:   به احتمال زیاد، اقتصاد ایران در دو هفته آینده فرو خواهد پاشید.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149758" target="_blank">📅 21:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149757">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_9302DtsxDQHEFnqB4u8iYFakTvcA7mEXzICFOFMbyfc1rhMTyffpeM2UiJc1kJ5Q8YvmxcV2WPWmxdXm3xjTeXgB9huGjzuHF8k8Zk7S0F-2A1XdPkoAV8msUZdc2iRYJr_9fYZlobW0DqDW4JscJZEzgi7sBBGLN6DtqZfH5jLVioyKbA4Qhsj4ys1KlRcKMMeC0vPWK-T60VQJ0wgfmib-2jbyH98J23icQlo0Ozfym0l5Bw0K9Q6ZwNebGKuzOMhU4jJjcJI8PE5QGOwKL2G4CH3npRvHKBr8ZnktBTb-45I-_44IHOL0xTFQ4HTM31wgen5sqPMDH-WVL1Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری وایرال شده از مدرسه رفتن یکی از کودک ها که کیف نداره و به جاش پلاستیک انداخته رو دوشش
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149757" target="_blank">📅 21:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149756">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
اسرائیل از دیپلمات‌های هلندی که در رام‌الله فعالیت می‌کنند، خواسته است تا ظرف هفت روز، مدارک دیپلماتیک صادر شده توسط اسرائیل را تحویل دهند.
🔴
این اقدام پس از آن صورت می‌گیرد که هلند ممنوعیت واردات و فروش محصولات حاصل از سکونتگاه‌های اسرائیل در کرانه باختری، قدس شرقی و بلندی‌های جولان را اعمال کرد.
🔴
بر اساس این تصمیم، دیپلمات‌ها پس از اتمام مهلت تعیین‌شده، از امتیازات و مصونیت‌هایی که توسط اسرائیل اعطا شده بود، محروم خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149756" target="_blank">📅 21:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149755">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بدر البوسعیدی» وزیر امور خارجه عمان : گفتگو مطمئن‌ترین مسیر برای دستیابی به صلح پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/149755" target="_blank">📅 21:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149754">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل: مذاکرات پیشرفت چشمگیری نداشته و میانجی‌گران از مواضع طرف ایرانی ناامید شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149754" target="_blank">📅 21:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149753">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
گروه حوثی (انصارالله) تصاویری از بقایای یک پهپاد "کاریال" ساخت ترکیه را منتشر کرد که توسط عربستان سعودی مورد استفاده قرار می‌گرفت و امروز صبح در آسمان استان حجه سرنگون شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149753" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149752">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح دولت تحت حمایت عربستان در یمن: در عملیات جدید نیروهای ما علیه مواضع حوثی‌ها در مرکز یمن، چهار کارشناس ارشد ایرانی متخصص در راه‌اندازی و پرتاب پهپاد و موشک در مرکز یمن ترور شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149752" target="_blank">📅 21:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149751">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: بار‌ها می‌گوییم گفت‌و‌گو می‌کنیم، تا نگویند ایران حاضر به گفت‌و‌گو نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149751" target="_blank">📅 21:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149750">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
تلگراف: پلیس ضدتروریسم بریتانیا در حال بررسی این موضوع است که آیا تهران پشت طرح بمب‌گذاری علیه پایگاه هوایی مورد استفاده آمریکا در جنگ ایران بوده یا نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149750" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149749">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5MR2mrMgccog0RhRYnBgRo2_6czp0JW9zO0oat0qRfE0E0cmGsoStj1Bz9bGh_6C9mO2F4TH3Sd9vVqrTM6NnNIONbWMp2Ww875PvTX5p8CZyf-u27y0XzyD_S_7mVPLybSF5WuZ5coQGEam5JgdI6k_r7xq9dg1SSju1nATfdVKUBXhfBS-e_mu_GiahYFMkXTmYAQzcxHLD7Q-j5cWLpK3AhmZVAzsHscAoDe46_iQb1p92ZGEenWikIvPMA0LM1igYTKIveUC0zrS9X7CYnFiaiV5t77doMot1Lso21nPYHYH_Xw7sFRqBnuBgMYfvNiQr3FFtgfDxKnBs9clQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان قبل زدن زنگِ آغاز سال تحصیلی؛ یه استخاره باز کرد که انگار نتیجه خیلی جالب نبود و سَر تکون داد...
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149749" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149748">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0be3641b4.mp4?token=GzUYWxlGcsTj03ZRbHlC57rVYZnRAdlVD9rCJN5PcepQt3Dhp0INcoeDUxrHnSmOJlwrzqwGJxA5Q228Rjwx3uvZ7Jy9ksjoomWce_topL_ayS7t7MUnehUWykxCyMzgI_JFYN68JemMUMtQsiiMzH2r1DlzczL1MYdmKHTmsaYtjMhMt3hZDI8YDIKe2VNH5X9Z2Ilz-dvMpYHg_ZnG9edz8lAUyDE03AYyQp0fCTBBZ6zTzHeu9JMU1rNNqrvP0rPIS1PhMudBZXwD3iHdIcNMsjBSa9GixNuQdZO0LKRFiC4wI-isWoL_Zee0ht1R4QPnvEgciq-cWRBLK8FCpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیل گیتس: هوش مصنوعی از انسان باهوش‌تر است
‏
🔴
هوش مصنوعی فقط یک فناوری جدید نیست. این واقعاً یک رویداد تکاملی است.
‏
🔴
ما یک گونه هوشمند خلق کرده‌ایم که در بسیاری از جنبه‌ها، همین حالا از ما باهوش‌تر است و در چند سال آینده، با سطحی که به‌صورت نمایی بهبود می‌یابد، به‌طرز دیوانه‌واری از ما باهوش‌تر خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149748" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149747">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hq4SbwuXaVi590Jx7uDzZ_2F6_KL5KaQeP8O2LzdkTwZlhkVhwI12okOWTDKW-N428PMswMEJlgdR_SFUeVG8NoSh36HLe2ipfK3GM5TdyOtD7qNh8BKiZUpJrwVJTNMya11FZ-6ra-dOh-Iad9sZ7bkrMxJNke6on86YX5phtOyiNtzqiiifdutpfkX8Q5FT0RN9Ey_y5zse7GLxL5c78qQiTWTw3qnhBAD-HwO5XSb7V2rteQrvN-v16JY07_5eTz4mAmrqIuFlrOUSgczkIKrn6pAH3uk30ixAuMJ7z2tPLT7CmLWs6jpNGNxkhG3muKqT5LjbvQJB6oNyS7-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بنگاهِ فریب‌کاریِ آمریکا می‌گوید ایران کنترلی بر تنگه هرمز ندارد، اما بازار یک اضافه‌بهای (پرمیوم) سنگین روی نفت کشیده است: ۳۵ دلار بالاتر از قبل از تهاجم، و ۵۰ دلار بر اساس قیمت‌های نفت فیزیکی.
🔴
پس یا بازار احمق است که نفت را با این قیمت‌های بالاتر می‌خرد، یا دستگاه روایت‌شویی آمریکا دارد سیاه‌بازی می‌کند.
🔴
برای کسانی که حرف آمریکا را باور دارند، یک دستگاه چاپ دلار رایگان در تنگه هرمز گذاشته‌اند؛ بفرمایید بروید بردارید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149747" target="_blank">📅 20:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149746">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
تریتا پارسی: مداخله دیپلماتیک با رویکرد سنتی چین همخوانی ندارد؛ اما اگر دور سوم و ویرانگرتری از جنگ آمریکا و ایران رخ دهد، شرایط ممکن است تغییر کند.
🔴
اگر شوک‌های اقتصادی جنگ به سطحی برسد که چین دیگر نتواند خود را از پیامدهای آن مصون نگه دارد، پکن ممکن است برای مداخله انگیزه پیدا کند؛ آن هم به شکلی که واشنگتن ترجیح می‌دهد از آن اجتناب کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149746" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149745">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هم اکنون گزارش های اولیه از وقوع انفجار های متوالی در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/149745" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149744">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1bc066b31.mp4?token=JhxPeFdFe2NC2CIaMg8RpSQU_6txiwWbMImztvcPvg0zokte_n5RMDX4mYmBeEmjR31SkAKaQs-ncj0UMVxr6fcDnD-3LWAjlSlPbMDR-mWEmxNEgbV1JAFGe_K-msi_b7TWZlJFVRuAkHko6fQm1TwHFXzpwGoYmiQ7jRmV7ABR0S9UXLqPqLnH-oOLzhBTw0Nqtsr5CItk4f2NMFEJVQ3-DF6ClHK0_ScukC0QrYaiStvhNZMpuRrgYkC4ZyDyZIsNzUvmfWTbKKCBZ5cquaHY2Ac08XjdVndvtpLnlTUpjjDDj8mC5z2_cbREOFUAYrnux_Y3H-et2qGv57akhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مشاور جلیلی در زمان بایدن و با دلار ۶۰ هزارتومانی: آمریکا ابزار جدیدی برای تحریم ایران ندارد و تحریم به سقفش رسیده
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149744" target="_blank">📅 20:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149743">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
یک مقام آمریکایی به شبکه سی‌بی‌اس:
ما با درخواست ایران برای لغو تحریم‌هایی که پس از ماه ژوئن اعمال شده‌اند، مخالفت کردیم.
🔴
ما می‌خواهیم تعهدات مرتبط با هسته‌ای در پیشنهاد ایران گنجانده شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/149743" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149742">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
فعالیت‌های قابل توجه هواپیماهای سنگین نیروی هوایی ایالات متحده در استان اربیل، کردستان عراق. به نظر می‌رسد عقب‌نشینی نیروهای آمریکایی در حال انجام است؛ مهلت تعیین‌شده برای عقب‌نشینی، یعنی ۳۰ سپتامبر، تنها سه روز دیگر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/149742" target="_blank">📅 20:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149741">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EI2_vIrtb6R941QV-U93bcXecdIihNPOSTet6X-Ziv_UNJ8HtKul_DAm-XL6t2ubagK3M4YAEHzDgzogOnWoR7EXm7iyWOJzMLxqLkzS_UKEvoN6JU9ZPnSN-AtC73gbmub8OGYqBf69dX-QCADQDO8jw_-DI2ebVGJG9-nyr-akhBE0uqXO3CbISZJP6HvpISVzgUxAdBus2V1kfGkPOyZFJyqIJUFtTQIw_0ifNBRescHk3xIOgsMJiGY0kgA3tQwOq0iIwtZIlQJv29FgdCoQAUGA_8eJrEFMJYfEwhYwV25gPg0xM_HNe9FmPq4y9bl6YaqMF0Xde6JhFNp4Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو بلوبانک‌ بیش از ۱۰ میلیارد تومن پول تو حسابتون داشته‌باشید، از این کارتای VIP از جنس استیل بهتون میده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149741" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149740">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/149740" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149739">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سید عباس عراقچی:"جنگ راه حل نیست. این موضوعی است که باید از طریق مذاکره حل شود، و ما در گذشته این کار را انجام داده‌ایم. ما اورانیوم را تا غلظت 60 درصد برای اهداف صلح‌آمیز غنی کرده‌ایم، و این در چارچوب تعهدات ما در پیمان منع گسترش سلاح‌های هسته‌ای (NPT) قرار دارد. ما هیچ‌گاه پیمان NPT را نقض نکرده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/149739" target="_blank">📅 19:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149738">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f59c715ba.mp4?token=qH8XXFEy91pbNZ6O72kN2Ct_3qoFdmvLsNu2EXMm8jh8mp_NhxUNzOr5mw0giWFFiSdrFkzgh3kZobDxDHpP66Tuf8__-nTCnPb7-BblFq1-DlYABH31JC1Ix7S3BIvoZLdcNib16kiTPQzY-F8r_txMLRUZTAwMFfZhgD9FsLoGumagPFmLd7BsSAYeI2lDPErBC7Tg4heLtj6IHO0J3HgFMB9em5kUQLA8tYA2PiTkBk5PHpCNabLHQn-Yb_VQHXf75dcnKEyEKqJ7DN1CbxPW3jGcY5h0z9-DgZohF7QkSemC8ocFVz6G26npzRilB2rsJey9iqfxEXxabE7hkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری شبکه NBC: «رئیس‌جمهور ایران این هفته گفت که ایران، نقل قول، هرگز به دنبال سلاح‌های هسته‌ای نبوده است، اما ایران اورانیوم را تا غلظت ۶۰ درصد غنی کرده است. این میزان ۲۰ برابر بیشتر از غلظت اورانیوم غنی‌شده‌ای است که برای تولید برق مورد نیاز است. چرا ایران به ذخیره اورانیوم غنی‌شده با غلظت ۶۰ درصد نیاز دارد؟»
🔴
عراقچی:"خب، این سوالی است که ما در طول مذاکراتی که با ایالات متحده داشتیم، به آن پاسخ داده‌ایم. اول از همه، غنی‌سازی تا ۶۰ درصد غیرقانونی نیست. این کار همچنان در چارچوب معاهده منع گسترش سلاح‌های هسته‌ای (NPT) و برنامه صلح‌آمیز ما قرار دارد. ما این کار را برای اهداف خاصی، از جمله اهداف پزشکی، انجام داده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149738" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149737">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9056ac4f3.mp4?token=Sms6zHDwgBtXNqcMrkGthEccZvCbPu6cWPj8-0mWlD9hTTwq4Uc32r7zkDDqyOZkN13tJ6inJl_HESWWjKYYbBjs9g_jY2LfpiQhc024LqFI0mTL63lFmvXREPm34l8IphdAAjmqRpbJ9FgHs3vxYHCTWTFJOdRYfhSa9T5UCfPw96LsNQOcH61fTvYzv2CXU0GAy5Svpr_LDD0VvbOYI1orUONOVYs22QYBJRwtNvlbqb4bT2Vhvl-Yzvwz7YNScA9anoWwqHR6j0H3gwMZcpbU5KFS5QV_kILxfDLH3Cc6icDTDISm5k8z7E7RCvgiLIZYluyu2CZ9bhMHWw9Vow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: "آیا به پرزیدنت ترامپ، اعتماد دارید؟"
🔴
سید عباس
:
خب، ما به خودمان اعتماد داریم. ما برای دیپلماسی آماده هستیم. و در عین حال، برای جنگ نیز آماده‌ایم."
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149737" target="_blank">📅 19:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149736">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36b1c0d3e2.mp4?token=ktLPuhKKHyRkcvbbf85EZR9M1Xw334EbxY5DbzYnsDX0i_p2-kslbvpEil-r6bl_iMUpSZScFCXZ5RQRo2Bga6UGw55mir8OcwFLqYq8O07CQ9z70MaI9Z19WwJml-hvnGSFFx_UVXXhb3hVb6FQ5EJqSxd-oP6a2Fu49QZCc8Nw8LRHZFFHq24BAyifVeRJfjR30PNx_p3Da3k8YgjPQ84FQwQ0-YxqjBuffhBoYtGXHyquODI2Z_rfcyr5eZ8NLmW8tumvVXga8cA0PveBNL3rPJAuyF_zCssaNJdlMl7I0_AJrW3VZ8DEl4WHJd-bghld427lNZq8LsGqKP2BcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: آیا این درست است که ترامپ در حال آماده شدن برای از سرگیری حملات نظامی پس از انتخابات میان دوره ای است؟
🔴
سفیر ایالات متحده در سازمان ملل:  چیزی که می‌توانم بگویم این است که رئیس جمهور همه گزینه‌ها را برای اطمینان از ایمن بودن جهان از تهدید سلطه ایران از طریق سلاح‌های هسته‌ای، باز نگه خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149736" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149735">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3SBPKPI_B93QNhuNn8n3L0mSPQIQTGnuIMtJyKu_UfUq92W-fis84WJkUiJvuFo1Yb3ufvJjq11H_AjHAzIFmnAYDG-m1wrFzxXkIDDb3ySqcubSRkyaRFVGTNEiyFsqFjAiwkvElGIPMbSP9IDgTt1WB78N_1qlgg6jJDvaKIyghI3hGe96jGVowIUBYexKQ2xP16fJZCMB4-sz-Vs_yVYX9QSZKHjzaO_cQrGFJhyDrHYs-pJsT1GwdGxOGnTk4e0e4qGWe-gJR0YXpeLX8W_VxC-MfaU77pEp28iWWuwJPekY8L3EDJR6AfrWMU1n2NZ1KHmTUdlrICzqfa8vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : دیوان عالی ایالات متحده آمریکا هرگز اجازه نمی‌دهد که میزوری یک پیروزی انتخاباتی داشته باشد. آن‌ها به‌طور مداوم، تاکنون سه بار، رأی قضاتی را که به تصمیمات صحیح رسیده بودند، نقض کرده‌اند.
🔴
از فرماندار و از همه مردم بزرگ میزوری که به‌شدت برای عدالت و امنیت انتخابات می‌جنگند، سپاسگزارم. روحیه و عشق فوق‌العاده‌ای به کشور ما.
🔴
من میزوری را به‌طور بزرگ، هر سه بار، بردم و نمی‌توانم بیشتر از این به انجام این کار افتخار کنم. جای فوق‌العاده‌ای — همه شما را دوست دارم!
🔴
پرزیدنت دونالد جی‌. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149735" target="_blank">📅 19:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149734">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا درباره ایران:
ایرانی‌ها گفتن در صورت توافق، تنگه هرمز رو باز میکنن. ولی تنگه بازه که.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149734" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149733">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIReDPeYxSo7TL3kKCeiJwPSx1R9pLSlHgcc8c7ouVba3BSH5jhLATx6ixbpR7WTugWZ1WFMxx-uK48q4l7urjCvCpav5H-2wCjHIM0BBP-BuMjUnVByB4qwzbr_zkIeyTt3-7Bf_cBE9zpcj143IHWJCnkAl68AHCSi5u3un3tw8R47tSr26JeKfRpflXcTow8rjdqlTlwCrSCb9iL_k3Ve1wPDaYj9KlspRvet_wuabyF2Nh6GA79GA2NgkUTQYN6HzNJ-DNk7ZjR_-eCIc30LAEiARBLrcL0PlhOzM1vm4V7J7NOEse4qt5HwBvjeMEhXXeyQTGUrDgWlgbEmoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: «همه‌ی شرایط در منطقه» شبیه به «بهمنِ ۱۴۰۴» است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149733" target="_blank">📅 19:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149732">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
اکسیوس به نقل از یک منبع منطقه‌ای آگاه از مذاکرات غیرمستقیم گفت: میانجی‌های قطری پیشنهاد اولیه ایران را با هر دو طرف در میان گذاشتند و یک پیشنهاد مصالحه نیز به هر دو طرف ارائه کردند تا آن را بررسی کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149732" target="_blank">📅 19:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149731">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: توافقی‌ که ایرانی‌ها می‌خواهند مدنظر من نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149731" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149730">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
اسکات بِسِنت: ما اکنون یک رئیس‌جمهور داریم که چینی‌ها به او احترام می‌گذارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149730" target="_blank">📅 18:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149729">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2cd8f35d0.mp4?token=fADH2v5cRN8DAdrTrhPBomGIOyF8sa0Isd_A2znuZyhIO4wbWqH4Vua3jz7UE5M9BBuTRyx-O8HAB8Cc6lHqY5Ibk7vnU-LYCXPXobndm1AOuGkUWbKe4Q58WCMFtt653g15Is-OPYLuDogEIo0iLGqwDJn_bjXMPQRLKl485LS3KB2i6wJBzO6YpAEbAx5ncHx1Yz9nN5OB_82v0Rvl5LGllDOmvNgGB2UEY-iceuaAEx3acu2V-ZIg0_Qd7W_Ditr63CrfFEHUct4Ry3R8cKvpUh3paxjvPb-Y5EdawbPLkwHta7EDFzc6bq0X5B1YY-njKMW1j35yzdY6nk6l3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2cd8f35d0.mp4?token=fADH2v5cRN8DAdrTrhPBomGIOyF8sa0Isd_A2znuZyhIO4wbWqH4Vua3jz7UE5M9BBuTRyx-O8HAB8Cc6lHqY5Ibk7vnU-LYCXPXobndm1AOuGkUWbKe4Q58WCMFtt653g15Is-OPYLuDogEIo0iLGqwDJn_bjXMPQRLKl485LS3KB2i6wJBzO6YpAEbAx5ncHx1Yz9nN5OB_82v0Rvl5LGllDOmvNgGB2UEY-iceuaAEx3acu2V-ZIg0_Qd7W_Ditr63CrfFEHUct4Ry3R8cKvpUh3paxjvPb-Y5EdawbPLkwHta7EDFzc6bq0X5B1YY-njKMW1j35yzdY6nk6l3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: ایران تنها دو هفته نفت روی آب برای فروش دارد!
🔴
بعد از آن ایران هیچ چیزی برای تجارت ندارد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149729" target="_blank">📅 18:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149728">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
اکسیوس: منابع گفتند انتظار دارند دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149728" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149727">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
باراک راوید به نقل از یک مقام آمریکایی مدعی شد که برخلاف ادعاهای خبرگزاری معتبر فارس، در دو روز گذشته هیچ کشتی‌ای آسیب ندیده است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149727" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149726">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اکسیوس:
منابع گفتند انتظار دارند دور دیگری از گفت‌وگوهای غیرمستقیم میان آمریکا و ایران احتمالاً از روز دوشنبه آغاز شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149726" target="_blank">📅 18:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149725">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚀
کانفیگ v2ray نامحدود | چند کاربره
🦋
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
📍
نامحدود _ PLUS
⚡
:
🇩🇪
🇫🇷
🇮🇹
🇸🇪
🇦🇹
🇦🇿
🇵🇱
🇹🇷
🇺🇦
🇦🇱
🇦🇩
🇫🇮
🇳🇱
🇺🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇲
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
برای اولین بار در ایران
👑
کانفیگ ها بدون تبلیغات هستن
🚫
تمامی لوکیشن ها قابل استفاده در جمنای
✅
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
✍️
…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149725" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149724">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqboUD4bDyDregTcDYoJMseXA89wekovvfzfAEmcfaVYxO0R7tfPgq-LLkmrNIxHM_mbE2aqdsDBe-0hFvOKhKPupW82sSVO_FHob0HSsnoGH2jjHZtMEtKKwFYjSuGZH-mOYKCit6koHs34AwHaSm7D5WTz1ouBlklLf3PrL5vQ5JLFZgZLkXGxZ-JmhsrNz5rZ0KcxQrmYoqnSqDR5e1GJvmvFukRbp69RkTin46gbFYAUHhuyfd1xfUp2Ppbu2l6kKWt7JplO24WMLCJtw4tVOWvLTlcdaSGznUkwYbm7gEHmBYwKyKL1AnH9z3RNjAhYHaRhmTViGU1EzpYYAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب آبادی خطاب به بسنت: جهان حیاط خلوت شما نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149724" target="_blank">📅 18:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149723">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7baea2c31f.mp4?token=chALGb7PdHU3enSEAbNi8gZWlfkAC4hMKftq5qI_LrgHwGID-I6IsM1fM3j1Kb_zAz6D08rIZpco4GpU09Q5sY2zPCvvNPk858Snq9PhkKmok2oeRHsFqPjPB69wwQUIXT70nJGGuF9mZL83R3EEF1GF4Pu-y_bG45GAbSQKghQMaumYYuMB-_w9IK-5wqpwtTHcW4bkTu3fmgf7qnYcAQQkkBRN_oceHe_kFhTyDmZflKq5kIniBG3M8rjvJBsIdrnCf8u8DPkOCn9-Ib8DC04MwIs-zS4Ha0o_E9Qc3YDtVkpFaImuAEuR6n72dTf7gE7gfZeJaFm0ZDd5WI5DbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7baea2c31f.mp4?token=chALGb7PdHU3enSEAbNi8gZWlfkAC4hMKftq5qI_LrgHwGID-I6IsM1fM3j1Kb_zAz6D08rIZpco4GpU09Q5sY2zPCvvNPk858Snq9PhkKmok2oeRHsFqPjPB69wwQUIXT70nJGGuF9mZL83R3EEF1GF4Pu-y_bG45GAbSQKghQMaumYYuMB-_w9IK-5wqpwtTHcW4bkTu3fmgf7qnYcAQQkkBRN_oceHe_kFhTyDmZflKq5kIniBG3M8rjvJBsIdrnCf8u8DPkOCn9-Ib8DC04MwIs-zS4Ha0o_E9Qc3YDtVkpFaImuAEuR6n72dTf7gE7gfZeJaFm0ZDd5WI5DbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی : در حال حاضر، یک طرح بسیار منطقی ارائه شده است. اگر این طرح بدون دلیل رد شود، این اشتباه آن‌ها خواهد بود.
🔴
با وجود اینکه از رئیس‌جمهور ترامپ شنیده‌ایم که این توافق را رد می‌کند، ما همچنان منتظر پاسخ رسمی از طریق واسطه‌ها هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/149723" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149722">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40858e6d1d.mp4?token=gHqfE-uLdO7YPLhG3Eh2mW-HYhar-oCJ5N2ph8FZh7FvlOjlFnd4t_ffoTVR1L6L5RXCIx3t0wtpp3cPDsc16H0RqmvtId8Coy89FwKjPYUNGMJzkvFwBazbC22vJxWXwE-wXJip9Lqsk14u2AgQYZ335IKcnYs0YAI7fatdG3vkxehIZ4pCBsvrR9mHCvjrEM8XOOhW4F1zeUlqoKjH2QnuDATf3ot4y9-pyC3vZCMAg0fhJqgmPL6wp42sTje9hA_9OPNRTOK06O6FsQJCqgnsiBpiu2U8psaewtJzGQtBF9h25F0tuLhMQd2hFAxyFPQ8XEGiuxWe-_3QDVVzjqfcr-IRIzWTEb-qrRRNQnN00lkIaTLZmyqyaHDmLJbtGYI5ZG1WPoAzs5TEFzHWPVvxAOw93qz9u0OnT-sfWEQEDgA4n6KHSINSC0s5e89Z3DHK5bgKy_nWs2vKLBpUR5I2BsKobU6UWQZoPr0yQOaW2P9zS4XxLvSGEZWPGqNMv0Ja-z3Io6uK9SyfOO-2ge7-a7Km0OkkQu7p2pu9LJoMZXC2rmUgCcXmWb2dsNngAnYoH-AvF_rtdcfIgEWCmN9qSeGQuxB3yP3f5cDrDLdDCVykka1h1QyLPJ5ofu2tq1azpbO0_AhPUCN8gz5x6VWm_I1WEXqnPdRC78yDPjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40858e6d1d.mp4?token=gHqfE-uLdO7YPLhG3Eh2mW-HYhar-oCJ5N2ph8FZh7FvlOjlFnd4t_ffoTVR1L6L5RXCIx3t0wtpp3cPDsc16H0RqmvtId8Coy89FwKjPYUNGMJzkvFwBazbC22vJxWXwE-wXJip9Lqsk14u2AgQYZ335IKcnYs0YAI7fatdG3vkxehIZ4pCBsvrR9mHCvjrEM8XOOhW4F1zeUlqoKjH2QnuDATf3ot4y9-pyC3vZCMAg0fhJqgmPL6wp42sTje9hA_9OPNRTOK06O6FsQJCqgnsiBpiu2U8psaewtJzGQtBF9h25F0tuLhMQd2hFAxyFPQ8XEGiuxWe-_3QDVVzjqfcr-IRIzWTEb-qrRRNQnN00lkIaTLZmyqyaHDmLJbtGYI5ZG1WPoAzs5TEFzHWPVvxAOw93qz9u0OnT-sfWEQEDgA4n6KHSINSC0s5e89Z3DHK5bgKy_nWs2vKLBpUR5I2BsKobU6UWQZoPr0yQOaW2P9zS4XxLvSGEZWPGqNMv0Ja-z3Io6uK9SyfOO-2ge7-a7Km0OkkQu7p2pu9LJoMZXC2rmUgCcXmWb2dsNngAnYoH-AvF_rtdcfIgEWCmN9qSeGQuxB3yP3f5cDrDLdDCVykka1h1QyLPJ5ofu2tq1azpbO0_AhPUCN8gz5x6VWm_I1WEXqnPdRC78yDPjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد حادثه رخ داده در پایگاه هوایی بریتانیایی فیرفورد: دستگیری‌ها در بریتانیا فوق‌العاده بود. همکاری با بریتانیا شگفت‌انگیز بود.
🔴
آن‌ها قصد داشتند آسیب جدی به پایگاه ما وارد کنند، و همکاری با بریتانیایی‌ها به نحو احسن پیش رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/149722" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149721">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بسنت، وزیر خزانه‌داری آمریکا: چین کمک‌های خود به ایران را به میزان قابل توجهی کاهش داده است
🔴
ما اجازه دادیم بیش از یک میلیارد بشکه نفت از تنگه هرمز خارج شود در مقابل صفر بشکه برای ایران.
🔴
انزوای اقتصادی ایران به صورت مرحله‌ای اجرا می‌شود و ارزهای دیجیتال، هوانوردی و حمل‌ونقل دریایی را در بر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149721" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149720">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
وزیر خزانه‌داری آمریکا: تحریم و انزوای اقتصادی ایران به صورت مرحله‌ای اجرا خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149720" target="_blank">📅 18:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149719">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
عراقچی: ایران آماده از سرگیری جنگ است، حتی اگر اوضاع به "روز قیامت" ختم شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/149719" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149718">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbVnzKnIQnEQaRPoEjrLKrIErbh5WcLley0TVgkKBaawWff2a6mhSS0KSDaYXFVXNkmNXIkm8fzWRCXmoDwNvxSaZ0zdI11Ko8hAX4FFXlI7BPlyCa4CSWtL6zrAktgeas7JHo4qYURXNTsf3fmIFa-pwBmbZerOJh-C9_4id5ovkWD5JVpg81ss4vnbF2SyRoDW_umB4hlWtSdIYVfpUAHLEQIQcWNoB9qJaDspehsdOjkzF9FxuD3UK4c3yeErv_LdWap9QkVieKNGo3Tds6vwmXEOWzR7pGINb3oik5Ufgw9u4ps_QYrlN3wRfLTy4XUPrDtt2uwyfuTa-RkfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرنگار cbs : یک مقام ایرانی به من گفته است که مذاکرات روز دوشنبه میان ایران و آمریکا لغو شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/149718" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149717">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
پروازهای ایران فقط به این ۱۰ کشور همچنان برقراره:
🔴
چین
🔴
روسیه
🔴
ترکیه
🔴
افغانستان
🔴
پاکستان
🔴
ارمنستان
🔴
بلاروس
🔴
تاجیکستان
🔴
ویتنام
🔴
مالزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149717" target="_blank">📅 17:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149716">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
خبرنگار الجزیره به نقل از منابع ایرانی:
مذاکرات با آمریکا ادامه دارد و ایران همچنان منتظر دریافت پاسخ رسمی واشنگتن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/149716" target="_blank">📅 17:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149715">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
عراقچی: می‌خواهیم پول‌ها و دارایی‌های ایرانآزاد شوند
🔴
وزیر امور خارجه  در گفت‌وگو با ان بی سی: از خود می‌پرسیم چرا آمریکا پیشنهاد ایران را که می‌تواند شرایط را در خلیج فارس و تنگه هرمز به حالت عادی بازگرداند، رد کرده است.
🔴
اگر آمریکا اقدامات مشخصی انجام دهد، آماده‌ایم تنگه هرمز را بازگشایی کنیم.
🔴
این اقدامات خواسته‌های جدید یا موضوعاتی از ناکجا نیستند؛ بلکه حقوقی هستند که خواستار احترام به آنها هستیم.
🔴
ما خواهان پایان دادن به جنگی هستیم که هشت ماه پیش آغاز شد و می‌خواهیم پول‌ها و دارایی‌های ایران که به‌طور غیرقانونی مسدود شده‌اند، آزاد شوند.
🔴
به انتخابات میان‌دوره‌ای آمریکا اهمیتی نمی‌دهیم؛ آنچه برای ما اهمیت دارد منافع ملی ایران است.
🔴
همان‌قدر که برای مقابله با هرگونه تجاوز، حتی اگر به جنگی ویرانگر منجر شود، آماده‌ایم، برای مذاکره نیز آمادگی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/149715" target="_blank">📅 17:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149714">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بلومبرگ: ۳ نفتکش توقیف‌شده از ایران در راه تگزاس هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149714" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149713">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
حملات هوایی سعودی یک برج و ساختمان مخابرات را در استان‌های ذمار و البیضاء یمن هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149713" target="_blank">📅 17:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149712">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
مقام عراقی: تعلیق پروازها با ایران به رعایت دستورالعمل‌های وزارت خزانه‌داری آمریکا توسط شرکت‌های خدمات زمینی بستگی دارد
🔴
عدم موضع‌گیری علنی دولت در مورد پروازهای ایرانی به دلیل حساسیت موضوع است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149712" target="_blank">📅 17:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149710">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpzHfq_x5-Q1Q-qsqOVpK9I8lV9IpATPwlAl87itxKFA9f0jp-vAo7dujlcnt8DSkVg2ky8C2kHRgv44IvZdgdIOwvgFmm1ooKs4OsW0GYrhl_WwNal2IwSoLQfiKn5_nXP5bULJ70xXoGonMt3MHv_xe0Rx9iFVE9IC8jxJ9BJMl4fA73Fu2IxqWnZHBBsV09dsrAThKGun4VCreM2htGv9K8g1vZWokkTZJJX33JIXdm7uOIH08-zG27xfQCs5MOHFCn1Hnla5K5KB1DMpuZIGZIbnFDHubtMaVIscooKBRHCYdNA3cY2D3mB6raYF1FRSUEIK1PfKS9zF2Z3tRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NZl4el0uT7vb10o3El3ewmSAqbf7cnquI6sevpLs93SYOEaVhSvAL9ujsJlNeD3zahkf5q9bxE3S5ZCFeqqIU6LUlEqKiVDwFCkdMkM1kg-FTkYnJxyHQHxfssWOHZzC1u8r9RdCIjsRlXQTRtwXjZujTNU5LBW2BesXb8BZIei5XgQtEfbLMGSYPpwcgEFQV0jeLD_CCYNdZXCCmayB0R5e58Z4F8XuTppASCHoIio_oEOGe1SCvgR7QKl8Ns39faaxALhvrNZH0nDhL0hQ3gN-SwmH6DhMuxMkoWELK_mYfyla1hNE6howm774hNGmhFOYSuF45UYX3OnNuJWPGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیماهای تانکر سوخت متعلق به عربستان سعودی و بریتانیا در نزدیکی یمن پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149710" target="_blank">📅 17:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149709">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bvbbv-T7A6faO2ik4NJPYoJ2-IzCKylxhTW0mflBkgJsboy3PItB2re6U58R5S9pdsCec3uGeNggcYDv4QxKxFMRLmsUe93BKZCPmpaRccnNEGWf2p01D1J1WEkMoGBB1zkluv-bKJpvYDA_iBMbXIm-dQDFckTgTg1U5aXke1xLK3l0sSr89uBo9CoroQIHDvQtV0W64O8IcG0cM0kU1dduW6B32kmnyWp4ATP-t42ld7HLTw6yAXurIVmDs8mBJcVBGdXZW0jmIqcCrAAhEYxRzXB1PoaYH-rGdCtKZhc_lAkkiNnPq0j3SUHZ60n4TtEtNGuUHMOBIRJ948awrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بعد از ماه ها تفحص تو مدرسه میناب یه چسب که روش اسم ماکان نصیرزاده نوشته شده پیدا شد و این آخرین باقی مونده از ماکانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149709" target="_blank">📅 17:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149708">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011bddf1e3.mp4?token=UK5DMbILef9ABcyP5EqaGsw06GDWZgGWFpElYQBEwlXmTDzXb5mwl7ciPwf35pBkEBzNV_eDVNX9Q0t6uhh3UPk6i7aatFaHEHWWWDYQUafW4VDmMNDgeiVcSE3bdpf1MrQbYebSr8_FG8Jrey0zmNss-JoK1w8C3PgdTirOvNBLOQzRarRaEUCUyug9cVDt232CkcoVAPMtTmQVlRsyyCHN1CL2MWQ-_dEbbsfL9-cglMVoKpJLOcHnr7AXiTlD_sceXEl6VPlOjHFbraU0qFEce0vseEXcHLdIsL7upNgz967kZPHj7ZvjpaDAZetWQ47O6NJtMee3EdN3eVHOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011bddf1e3.mp4?token=UK5DMbILef9ABcyP5EqaGsw06GDWZgGWFpElYQBEwlXmTDzXb5mwl7ciPwf35pBkEBzNV_eDVNX9Q0t6uhh3UPk6i7aatFaHEHWWWDYQUafW4VDmMNDgeiVcSE3bdpf1MrQbYebSr8_FG8Jrey0zmNss-JoK1w8C3PgdTirOvNBLOQzRarRaEUCUyug9cVDt232CkcoVAPMtTmQVlRsyyCHN1CL2MWQ-_dEbbsfL9-cglMVoKpJLOcHnr7AXiTlD_sceXEl6VPlOjHFbraU0qFEce0vseEXcHLdIsL7upNgz967kZPHj7ZvjpaDAZetWQ47O6NJtMee3EdN3eVHOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
ما بهترین آمار فقر در تاریخ کشورمان را داریم
🔴
اکنون میزان فقر در آمریکا از هر زمان دیگری در تاریخ این کشور کمتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/149708" target="_blank">📅 17:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149707">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پلیس بریتانیا: پنج مرد بازداشت شده‌اند و همچنان در بازداشت هستند و پلیس مبارزه با تروریسم تحقیقات را پس از اعلام وقوع یک حادثه بزرگ در نزدیکی یک پایگاه نیروی هوایی سلطنتی بریتانیا هدایت می‌کند.
🔴
پس از گزارش‌هایی درباره سه خودروی مشکوک، پلیس به محل اعزام شد
🔴
این افراد همچنان در بازداشت هستند.
🔴
85 خانه تخلیه شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/149707" target="_blank">📅 16:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149706">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2380fb253c.mp4?token=L4USCFu7Hg6SYjG6zb5Kb4atr0fdAJ7LnKDdP_CTtjs8ghTlI6bEE-Ogc5KqVdHTSzaroSWFWoZ4c7YQ0RfckV6j84V1tVcImenzPFSZ7is6sgRYAdY3lW_FhJixEf7zRgfOKI-i5ogoELCL-hsJTd-tLpo3Hzk3DnqgPuB-p_tkSgNUJehGoIbNf5KHoOyOa3J00ivRnM2XTpF2uqZ-lprheq6XjykrAgpJqm01Gz2k_qbxEZWmBqTqHRGAEkDeTRpiQxs03jwzxkcsrM-aLUYWsBDg7lSVMm6_bwrwcsOapaancCYPoXJ-PmRMSS65mTUu1axA25KV-4wS_Jv-jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2380fb253c.mp4?token=L4USCFu7Hg6SYjG6zb5Kb4atr0fdAJ7LnKDdP_CTtjs8ghTlI6bEE-Ogc5KqVdHTSzaroSWFWoZ4c7YQ0RfckV6j84V1tVcImenzPFSZ7is6sgRYAdY3lW_FhJixEf7zRgfOKI-i5ogoELCL-hsJTd-tLpo3Hzk3DnqgPuB-p_tkSgNUJehGoIbNf5KHoOyOa3J00ivRnM2XTpF2uqZ-lprheq6XjykrAgpJqm01Gz2k_qbxEZWmBqTqHRGAEkDeTRpiQxs03jwzxkcsrM-aLUYWsBDg7lSVMm6_bwrwcsOapaancCYPoXJ-PmRMSS65mTUu1axA25KV-4wS_Jv-jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی دو مدرسه تو تهران؛ دولتی و غیردولتی
یه ویدیو تو فضای مجازی وایرال شده که دو مدرسه رو کنار هم نشون میده. یکی دولتی و یکی غیردولتی. تفاوت فاحششون نشون‌دهنده فاصله طبقاتی تو جامعه‌ست.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/149706" target="_blank">📅 16:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149705">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‏
👈
عراقچی: آمریکا در نهایت چاره ای جز پذیرش شروط ۷ گانه ایران نخواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/149705" target="_blank">📅 16:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149704">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMCZLceKzOa_skUlklnEAvezGEV5tppSdyusjcM3o4AJDTIvKaU93JC1l_U5-yUr9xoNG5EBLuAIygsXo00EjEYAFN9HFFC0MDHla9fPjen1X0u8GCORZJNpAYajH8sxD3fh85xT3798EU4KxaLon7Ncx798SNoTAQjehIDSmRek0XcSzSWi1rriTbvR_7bA-nyyL8VR1g7ByKXIHg-DTxiNj_iw1ApUbxBDMzEO5mb83tghSvDFIFIsxZVk_t7vdUbQSxilAWJGug6vcsDSJEzt2J1L7wu6i2H3Sf_Wr4FeQPdII9fIB8kBfoCRwyGZWj5Mf88Z1RW0i0JJDYm7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از متحدین ائتلاف ایران علیه غرب
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/149704" target="_blank">📅 16:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149703">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c70d8cb102.mp4?token=L7FliKasY9gJTk4ny3ieTSYWoHJ_f3PWfXopjQlasBlO7uGBis5Pp89bfGph1CMRnTWrzqwKO-pw-flnwmNlisMDc2P_HevPXD49bSlpTvaX8Izq4zFnEqIyAQlflJGmVXpiHdaGi91hbgcCnDBMrmMNI6asNCUmUmKgdv5lMZwG_LGf9Cj-COBBYnh9HiD3bk_Ic4-2Iklf8HNAhiDrvde3_SYL6VwwAc689_EYXMo_1H5Tq8jyKAvbpj_a6o7WtBxQXx3en51LT7209vE0oc7C4sPrkabxJivr-Qtecx1oHnEZoV4jELwv_GiI4wDMRi8kh_VIFGJHt-tqSVCj0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
قیمت نفت اکنون پایین‌تر از دوران دولت بایدن است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/149703" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149702">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=dntolP2KNgxG379jjyiRSJoJeRLs-ILV_KHKzhjD45fYBZTMoV3g4H2WAA5_80ma96zEMLLjstwn2Fwvj1uFDiBdIvNvCScEi4glsaupc0Y29eryp0wkUKlqMqWYpklTLHkY5r1Qhq9IcqKd38VEF2YOF0pEvseM0Cb7zrbsqizlIbElEzf_r8FJZGRBMYWvnnbbOhY6jPKt8aC0_1CiRrejUZFDQ_AZQYH92ANyi0Neukf4ILt20JniNfMcizfVEqyqpyKzf3mu74Sjb1D4CzD58dyopm_nNi4CY1-ghpLkrCKw-QE25d17o3UyObcloCLME6aUS8JbPHhVciJ0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c275c1a77.mp4?token=dntolP2KNgxG379jjyiRSJoJeRLs-ILV_KHKzhjD45fYBZTMoV3g4H2WAA5_80ma96zEMLLjstwn2Fwvj1uFDiBdIvNvCScEi4glsaupc0Y29eryp0wkUKlqMqWYpklTLHkY5r1Qhq9IcqKd38VEF2YOF0pEvseM0Cb7zrbsqizlIbElEzf_r8FJZGRBMYWvnnbbOhY6jPKt8aC0_1CiRrejUZFDQ_AZQYH92ANyi0Neukf4ILt20JniNfMcizfVEqyqpyKzf3mu74Sjb1D4CzD58dyopm_nNi4CY1-ghpLkrCKw-QE25d17o3UyObcloCLME6aUS8JbPHhVciJ0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
شب گذشته، رکورد تازه‌ای در انتقال نفت از تنگه هرمز ثبت کردیم؛ حتی بیشتر از میزان نفتی که پیش از آغاز جنگ از این مسیر عبور می‌دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/149702" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149701">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=IOx7g44GP4Y21DME3JLaJueUAvfeKJrNVfcs4JeS_GQgVYqVSc5g1miqLOb7TFb_I1whI61yPe-DhaMSiLu4a3qofjb9VZRLMI-jHpSIYOZeZQFp3qxVF8UtmBXHWFhCgwhyAQbM-FK5Yja0A-2_fhUV6i3pHvtujvZGNBRwIK5JtEsI8m4GnLZBMWIlspV5_AQ0Ck-_Rs0RxEjJabSN77Oinc8v7_7VTEDVImGW_S5lsXRscUrjGh8qFEgjzsXoaaKqZ54-eN50fBV5y6LAzjirpC74ZnJDwm-mM9sPtEtxTTTp_nazPiTKqVvVAzC-rHSLI-iIevT1KqUDRj0mkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a495b9a3cc.mp4?token=IOx7g44GP4Y21DME3JLaJueUAvfeKJrNVfcs4JeS_GQgVYqVSc5g1miqLOb7TFb_I1whI61yPe-DhaMSiLu4a3qofjb9VZRLMI-jHpSIYOZeZQFp3qxVF8UtmBXHWFhCgwhyAQbM-FK5Yja0A-2_fhUV6i3pHvtujvZGNBRwIK5JtEsI8m4GnLZBMWIlspV5_AQ0Ck-_Rs0RxEjJabSN77Oinc8v7_7VTEDVImGW_S5lsXRscUrjGh8qFEgjzsXoaaKqZ54-eN50fBV5y6LAzjirpC74ZnJDwm-mM9sPtEtxTTTp_nazPiTKqVvVAzC-rHSLI-iIevT1KqUDRj0mkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:
به محض اینکه ایران تسلیم شود، به محض اینکه جنگ به پایان برسد، که این اتفاق به زودی خواهد افتاد، قیمت نفت به شدت کاهش خواهد یافت.
قیمت نفت به طور چشمگیری کاهش خواهد یافت و تمام قیمت‌ها پایین خواهند آمد، اما قیمت مواد غذایی به میزان قابل توجهی از زمان ریاست جمهوری بایدن کاهش یافته است. تقریباً تمام قیمت‌ها به میزان زیادی کاهش یافته‌اند.
ما حجم بسیار زیادی از نفت را خارج می‌کنیم؛ شب گذشته، ما حجم بی‌سابقه‌ای از نفت را از تنگه هرمز خارج کردیم، بیشتر از زمانی که قبل از جنگ این کار را انجام می‌دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/149701" target="_blank">📅 16:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149700">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/tqMsLAudRUn9b1bEriXZAzQ2gGuDP8AMmnnoQW_oaAXGYOhGPGBXrwkiSZy_FZJmtmACgcIWwi7pISYLveiNkf6f9cpJSvPpo-tSlMP5-_TUfYe54fliStXW4rQnBWrz_voaxRXFZbtkI8r72p8Wy_LZoeSv7wsX2GwxVdfzh_qncoMd2fnWAGRU7PC2-QAkJBCTlTrVOfTi_VkDz-My7_e7MmTXIZV-uBE4PBaNgWEeao_p-euMiI4KRaNh-H_XET5mZaEXfcvnPnNp4vEyP3thoBOTKHYqXaURPQGBIMUn8JSdDm-6pnbJlMFKXkVk7Fqpn-tr7GGN8P3OIhARwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فاطمه معتمدآریا بازیگر هم به ایران بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149700" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149699">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdZiH0ENmW_VNp9lUj5BYY_J3w4SlqAWOeRr9G8IqNV98wCswaO5hbzycyZ59m4VIhwxlHLx34qvmzEowkmGkWnvR7lv3tF2fUML1yEtLFXcYnCjS75SrFemHUZnw-2o8DgN0998Bu6XV3pcmDByNsymMnNn95ZY2iVU_OYm4dYCzDB3Pm2ga-FVyBW10g5-Hr5HFnlu2DLswajZenMlJugOQpwCp_86ShZBvsdyjaEWvXR_0s4xVIlpesVqxhcXuHoRTe_Stp7GA3MBbtuj2PfgBuvR27lw5v7A9mLBBsANPrg_L_CpliRScLoCWO-ncOvEeP16tN_gF0KGNvegIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: هیچ‌وقت در تاریخ آمریکا این‌قدر افراد شاغل نداشته‌ایم
!
🔴
همین حالا افراد بیشتری در آمریکا مشغول به کار هستند تا در هر مقطع دیگری از تاریخ کشورمان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/149699" target="_blank">📅 16:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149698">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHpnr9lWZdm-xjT4vZ4wUo9KD_RSqGu1qVYs5w057j_8CorJhwzs_EjUZBaVmvAL9HVQ981sE0hYxRm7LTqJZB9lHCjDj0YQjAb0yP8JfxIpDBeziKYBs90Po13i734fBqcMQB6S2McHKhIhYPYamj5kpin3uCVEM3LQjlZnk8lyM3lRlp9C0rQ4ko2I9qcrtj566nT58Ss4FLg1h555d3uTaTGybETeGlNNpOtCGygaEfspGrKV3CF7sWq9b-4AEZbt3cMNjRC5b1TBZ1Ldy1DhJ82xv02q9gQkZQupa4r51cWdx6RNWw6OiZKqn4NOS7BEuHsLH-Ric9waUrh36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
قیمت بیت‌کوین به ۲۰ میلیارد تومان رسید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/149698" target="_blank">📅 15:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149697">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2OG4RqCnEqPms4WZRAOIYkcUlrP15vXKIpquRXjvfqdZB4uvekJ5xqpa5OPj_qMGr2MXkDpulJ9ZgMxAXWFtz6zb2Vj2rrbKRbZXNYCqMh1TI6zWRxE0hy__h_ZqVJ91jTFASfrkJy7BPA72_MRQZ4EkhyJAlspz4jabeb4tYyj0BFA891Nd9kMGXJlxgRAnMRGS53CdvVMHpUnDqJgyz1bgC3F6numH6FaZiG0Y2QWrDaqzood9BgSCErkIPPP4jHUSiOMOO0RdlWtjAKgu3TB4Alw9mYxkroanXFpbbiF9MHunGHtlHiiabId3_p59pli3qLXPYry_XrYPh0Spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برای ثابتی هم پرونده قضایی تشکیل شده و احتمالا بزودی اونم محکوم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149697" target="_blank">📅 15:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149696">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
طبق گزارش برخی از رسانه های خارجی؛
آمریکا قصد داره با فشار آوردن روی کشورهای پاکستان
🇵🇰
؛ افغانستان
🇦🇫
؛ عراق
🇮🇶
؛ ترکمنستان
🇹🇲
؛ آذربایجان
🇦🇿
و ترکیه
🇹🇷
مرزهای زمینی ایران رو هم محدود کنه و محاصره زمینی هم به محاصره دریایی اضافه بشه.
چون الان ایران با وارد کردن کالا از مرزهای زمینی تونسته دووم بیاره و اگه مرزهای زمینی هم بسته بشه؛ عملا هیچی دیگه وارد نمیشه و به یک زندان بزرگ تبدیل میشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149696" target="_blank">📅 15:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149695">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9ujvBXYhKFnFUCKaCzc5iQErc5dDlZxzKU-4uKH4zSe7r2w-25pdIHgcM_5UF-j-1jduSK0TzNsZNFUOCfMHBcvxmkAGXb93Kn7LTGnd2WjJWZ3Kv7yuwWOgwYkXg0RaQ75DZ8UzlpC7rJXaFBNceHl0tfGQpKOhIQaryxgMPB0HyLGySpyrgl0vVCbf9jeSMv18jGjnIvpfMc821j6mlX8QROYa5YguYP1nEMS08invShq4zXZ5iAKeoZBfg4WgI-1iNwDzEVxjIC4qPH6yqI4lOhIkR8mwuTT3v2AnjjWamX1GUmvqIz9XHUDgMiH4ahhA-5gqyDmXuSHuG1QLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی بخاطر شکایت قالیباف و چندتا موضوع دیگه تو سال 1402، به 10ماه حبس محکوم شد  #عروس_زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149695" target="_blank">📅 15:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149694">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YlBGM6qUkVRDLm4eSgmViEHReaEH_2N8Bs9nCSMKfEXxeHOT_RL00qa51FsGRmODKHO6kx80mRKFRdxSooz8m7B1wv615dYnPQ9i_DEKp4zN6hPcThtdSOdC7X2kOUqVCbrfeHQcQrq3U6Cbk3da9bmHhVydBQtvrBeixcIegcHcVSL0Q3HP6Ayxb7nKR5wQW_z2MHzjWmGx3SasivO39UgG0wWYiN8cK1UcBuPdEa1ZwI1YopSX60Xg3nXhHjEjfc4rR5eWHmUmLpjMv6VLaG9YmMnd0fgh-3NXRy6zGyMCGnPISHCCDosgoJeHnhOmBcTmWYyfbcpGyK91xq9xzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کامنت وایرال شده از مرضیه حسینی، خبرنگار ایران اینترنشنال در کنگره آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/149694" target="_blank">📅 15:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149693">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
فارس: شب گذشته ۷ کشتی و شب پیش از آن ۱۲ کشتی هدف قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149693" target="_blank">📅 15:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149691">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1b5myHa9edo-44KjyPPHUKQT4MP_EcL3XH8F8TWaJGAXF-4wLISkF-NSF_qaloOdykuWV_JZYA5nG45mo_dKo9Ev1SSNEd283RMe_QAJny_-pt6GrdZF0lLIh_meJPsPnKJfh8CKJivZZlai2obWj_wvE_gPGNe06kUQCelumz0ud1tKb-afDZnicqHDbE-i0T8T8iOA7z9JbxmzJzRrOoMj9ruk4msk9d9di8N5hxcwwxX4R5DXO2-9esbjPIWCjxF96HDjtdJYEUNycD8t1TX_6C_6LgO1MW3q_LkvT2bM-MI3cUXbxwxXDd6DdYftKDMqi3AIdfmDCR85bKzEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777e744fd9.mp4?token=bZ1xH85KtBk-qkJDaOeGah6gP5vSmwabs9huphWdIh5mtmiNybRiz7pDOTtKguKIe9k-w7sth5gO_4wWPCFR_aL_oEHBImT0oxteW4PN07S1EleLoNy7kvDa9KgAqYI7dyMwbQX3Hb_uQJzMho8j6AgbUdIgtANSbpTamykwN7SaMh0BD9QS11kV9t0PNl88a_b0k5RJ-ezxiHu1sdNccaEj51aiWKS4M04DRixP4syzpW3aL_bPH9i7FceaeCT7hF7HXltop6ham1vUqu5AFFEpmCfsN7qBUjidd65i4gZzJaZ2r8ruD4BBM0deOBidsnKsg3jN3VYoDIRuKfL3XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد بریتانیا
🔴
نیروهای امنیتی بریتانیا در حال تلاش برای خنثی‌سازی مواد منفجره در نزدیکی پایگاه هوایی فیر‌فورد هستند.
🔴
در تصاویر، یک ربات کوچک خنثی‌کننده بمب در نزدیکی چند کامیون دیده می‌شود که احتمالاً حامل مواد منفجره بوده‌اند و به سمت پایگاه هوایی در حرکت بودند.
پایگاه فیر‌فورد محل استقرار بمب‌افکن‌های آمریکایی بی‌۱بی و بی‌۵۲اچ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149691" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149690">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فکت  فرودگاه نجف رو جمهوری اسلامی ساخته ولی الان هواپیماهای خودش نمیتونن برن اونجا.  [@AloTweet]</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149690" target="_blank">📅 15:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149689">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
رئیس دانشگاه تهران: در جنگ اخیر ۲ استاد و ۵ دانشجو را از دست دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149689" target="_blank">📅 14:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149688">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/149688" target="_blank">📅 14:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149687">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/horhjTpjvgqpe2lX_D1zs3Kvb4ME1Zzh198YhGYVEDxBq4atg9Y2NoWFmeVq_YXodNRj3yCazbyyB0zm_8j42lhaf5TG7242feBEwxIlAOAU2olBAj0ZB5kviMaoU4pT66twRFmkOyd_6mqjXTwYSAb9RjHMgxgbeWF1mlcr8eA6vZ_-q08wNwpMie74FHiZ9XbVlv84OoZGdas_1eggRTK0zQ3QO7xUGdR0PgTjJovDbh17FWJm8eyFCOw60AZKShLje3nU8ONfhEJ6-TPJ6tlJGIWmbHEShijISVNhgFaLBDrWdECX07bxAb8KVV96DRiQu-ThaFFNC0w3kerqjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی قبل، پرواز ۴ هواپیمای مسافربری ایرانی به مقصد ترکیه
🔴
مطابق گزارشات، باوجود توقف پروازها در مسیرهایی مثل عراق و امارات، مسافران ایرانی می‌توانند با هواپیما راهی استانبول ترکیه، اسلام‌آباد پاکستان، کابل افغانستان، پکن چین،‌ دوشنبه تاجیکستان، ایروان ارمنستان و مسکو روسیه شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149687" target="_blank">📅 14:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149686">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رویترز: بوئینگ یک نقص نرم‌افزاری را که پیش‌تر افشا نشده بود، در هواپیماهای ۷۳۷ مکس شناسایی کرده
🔴
بر اساس این مشکل نرم‌افزاری، ممکن است خلبانان هنگام فرود، به هدایت خودکار پرواز دسترسی نداشته باشند
🔴
هنوز مشخص نیست چه تعداد هواپیما با این نقص در حال فعالیت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149686" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149685">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
فارس به نقل از  یک منبع آگاه نزدیک به تیم مذاکره‌کننده: پیشنهاد اخیر ایران [به آمریکا] دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149685" target="_blank">📅 14:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149684">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نقدعلی نماینده مجلس: مهدکودکم حضوری شد، چرا مجلس حضوری نمیشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/149684" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149683">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuqgLPVpa9DfziswAobXxF8oai14uRENuRdPUeln5Cov_sGG89tbCdzkUIdSNitCW-2XH_aISzN5dRvQDLV0Kacypu0k3lGdfZ2anx1f8BWt6CTu2oeB-BspAVrBpFXPDBL3ONDmAiGxUFikLlVcqgV7HMHbi8izTRxQY4N6w-paK9BquJASiSls0F07dmhK4IYD21HDNfOFo9Shac1rcoC1UzjyOE6TU_jOhyfI1eLqdS15_aWltbFZI4DVDeXVhSusER336uoQ7191oSugkB087CaCZ0-fwrroYHVNj50jmfZMyFVEnnKGgRCZIGei9KuxuHFeJpIeBRUie7lxeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همزمان با حملات هوایی سعودی که به کشته شدن و زخمی شدن حدود 50 نفر منجر شد، یک هواپیمای سوخت‌رسان بریتانیایی بر فراز دریای سرخ برای پشتیبانی از هواپیماهای سعودی فعالیت می‌کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149683" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149682">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IobZEBAhuDtoWQJfRnAHDOFFXL-Ml_cukYma1m_Y4hamUec8K5u0PUYycPHNshPqPptXrK_k7OJvNgWfy2DsHT0DnwXUVGH-GaCdNTQlzcQX3J14GjN97B-mvX6pqfxfpOAWimJ5vAT9rFMPE0oW1NoE3srAet0PIunZU-bSxi8bTK2doWS7kVBq0MWPXd6Clea1sjsFvaUS4Hr5B1wdJ0CgqgdKss45meW5nYcD5abKXbvmOifLOPZPljxH-4zl8288oAFddFMqv4ZXslbuzd_nR4ZZCb8UBi4uJDUAXb2jaAiEisze1oMtu_wdftI4vcUccrvDvpdovrrDeIViPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه: شکار دومین زهپاد [زیرسطحی] ارتش آمریکا در تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/149682" target="_blank">📅 14:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149681">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
وزیر انرژی امریکا : روزانه حدود 13 میلیون بشکه نفت از تنگه هرمز عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/149681" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149680">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LR0iLBUR-nDq6iE0HGlZVXbhpsb376DteF0moU7wzr7UP2FtCOUwWQ_37XHa3GSOtvZeGzmqHV8tB2gDHsy4cpp4QX8RYX_iGytpE2NT6qCiq1PQueXDzAh72CJO1ozj6TNFRRd8DphaZ4yd3HEYdlXDEK-414q7H-ThVzgJToESTy_w1hyxY8w_UpJ49ZrRW8rTkaH-ysjGzv234cfVop0U3qa88M4sX2pIMg7gRg--n8VNpRDqcGG_Fs3E0z10yLSpxYEnWONvu5zvM5nAGqmaDx0bAdMpLVf92o1L0hWz___7nLf-i4uMoQC8jPcAfHo8cnkKIYwE3T9RmPcjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نامه میلی گلد به محسن رضایی: بانک مرکزی یک تن طلایمان را نمی دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/149680" target="_blank">📅 13:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149679">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بی‌بی‌سی: در پی اعلام «حادثه بزرگ» در نزدیکی پایگاه هوایی سلطنتی فیرفورد (RAF Fairford)، پایگاهی در بریتانیا که میزبان نیروی هوایی آمریکا است، چند مرد بر اساس «قانون مواد منفجره» بازداشت شدند.
🔴
هم‌زمان با بررسی چند خودرو توسط متخصصان خنثی‌سازی بمب ارتش،…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149679" target="_blank">📅 13:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149678">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
امیر حاتمی فرمانده ارتش: جنگ هنوز به پایان نرسیده است و ما باید برای وارد کردن ضربات قوی به دشمن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/149678" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149677">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099d500c99.mp4?token=PCxKxnS3H_ARlcngziyx9BJCilL9lmhn9JY7c145F1wT-dMQiWnCRzS8mi2GBwffWPfH8BEWDcAIrIVf5xZD2hrvD7QsEBXXK3StH2TyGZR8MDJDNtPz-AIeyc15VGvBiw6JEODwFSX-sP2bwubjw-m7FAkpTASmPZ8VWAs5QfM2dIYbQRt0LHyqPanMFaB2ELNAkNEspII92Y8KiUaFoghfMN9uSQDT0QNy08dIVLu9QeR4JE0yA5jmW1faOjQV_tzbfI-gYjKwwk6k_csKBEt-QhLut42Oq-eBl8JCX_N8ZcX14Jr5JEx5_Tz_OkT1fd8oZt1F9-uJLOFjGabUPBgIOCF-7quH7dAx7h8QpOPVKzqW-TV72K194uYfBmZB9z6rL06pSj-xpQ9HExeveWiLtdWRVn1Vm40cFion6Jh80FLQjlJiuPvIl5hmclqoa8J4jqQWwO7kl-R8fvZZSEHgTD0Qh2fNpofTcU7auvYzIz5_VTU84HUD3dwf8Ywqa_6EZJFpiZHnepm5bF1Fb25Bl9sgtCzZXopgk9koKKIy1u0KBcsRWVuWQS7hI2_7JJ6lE9dLH1_nIZ6RfTWuAWXWsS8GkSrCZGdMttbTX409jC2QHmkWUnYtIDs853nSv61eVMKnxUUWy3aRPjtr-ZkZBtbBLogVzoYx5eGHL-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099d500c99.mp4?token=PCxKxnS3H_ARlcngziyx9BJCilL9lmhn9JY7c145F1wT-dMQiWnCRzS8mi2GBwffWPfH8BEWDcAIrIVf5xZD2hrvD7QsEBXXK3StH2TyGZR8MDJDNtPz-AIeyc15VGvBiw6JEODwFSX-sP2bwubjw-m7FAkpTASmPZ8VWAs5QfM2dIYbQRt0LHyqPanMFaB2ELNAkNEspII92Y8KiUaFoghfMN9uSQDT0QNy08dIVLu9QeR4JE0yA5jmW1faOjQV_tzbfI-gYjKwwk6k_csKBEt-QhLut42Oq-eBl8JCX_N8ZcX14Jr5JEx5_Tz_OkT1fd8oZt1F9-uJLOFjGabUPBgIOCF-7quH7dAx7h8QpOPVKzqW-TV72K194uYfBmZB9z6rL06pSj-xpQ9HExeveWiLtdWRVn1Vm40cFion6Jh80FLQjlJiuPvIl5hmclqoa8J4jqQWwO7kl-R8fvZZSEHgTD0Qh2fNpofTcU7auvYzIz5_VTU84HUD3dwf8Ywqa_6EZJFpiZHnepm5bF1Fb25Bl9sgtCzZXopgk9koKKIy1u0KBcsRWVuWQS7hI2_7JJ6lE9dLH1_nIZ6RfTWuAWXWsS8GkSrCZGdMttbTX409jC2QHmkWUnYtIDs853nSv61eVMKnxUUWy3aRPjtr-ZkZBtbBLogVzoYx5eGHL-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظات اولیه حمله سعودی که بازار تعز در تقاطع الماوية را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/149677" target="_blank">📅 13:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hc7L8JTpvOdeas7TEi14_IDW79LoR1xspG6Vr-li9s9jveEwmTgulCLbAs3C3VAwPw8SNqg8oK0EhYyRUV9FwTTjfSt6fodbtAB7LdZDOYDfa_3mx3B6zR0LdAaAuvvdhhRem74hNDwMux_t7_ggEoadPvVmE-w3OcHGSFqxK3Y93tR5aUwRzIeMbs8vreWeakH16GFrMr-Jn5m0vg7ekdsm03R9M2E4JlvhmR6HdFjoapU241ek71_u3-N2xj4Ry8p1FJiTeH6XT8EeVnCKFpYRI2DpgwsnBbWaj5LdON2xfxVKcmURYLQ8lSxiyoqAMQTBB1wzX0LmohvF2q5M5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/davGPmHTBZuna1BHNA0BbCAedxpVSNmxgVrqVkJ5AdHO5SCf62uT68QG2_I3fYoF-gKGvHLWhUEF5SA5S6zdxGyrEFDgf8wD_5zK4K6i4tz41o1LruWLvl5mM4mZH-lLL6HyQZUmDbFpHIAH9-Kx1xnHrZyFf86mhg8qqvFIj97XMq0fB0QzldAjPHYu8rFWjcJ6-5Df6r_iLTpzWNl8PaoeLvxYNNQOoZozRYp1KBeTJ5zIdTfN3rv7npGRQkSie5drj9BrmHW52Rf9h_kDPJlXnOADl3Lxn-kv07AyW0MdFJjErxgyNOMhxXlAo7IUGFS0KG_JZe7CMW9eaUFRnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حمله‌ای هوایی گسترده از سوی نیروی هوایی عربستان سعودی، زیرساخت‌های مدنی را در استان تعز در یمن هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/149675" target="_blank">📅 13:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
نیروهای هوایی عربستان سعودی با سلسله‌ای از حملات، فروشگاه‌های تجاری در منطقه "المؤسسة الاقتصادية اليمنية" در تقاطع "ماویه" در منطقه "التعزیه" از استان تعز را هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/149674" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
حاجی‌بابایی، نماینده مجلس: ایران باید با قدرت [مسیر] انرژی را بر روی همه ببندد؛ یا همه یا هیچکس
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/149673" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-149672">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841e48be90.mp4?token=bqFHE1fobmCTX-aBOjDphiK6EMBfQMC-hv6nG40s96Eba0ZU37gy5tyMpEp9w5VXLQwInUvp_L-ubCn5vH0ZDZEqe5_8pr7GrhKw1rHy-6r9_-htYBfnMHwl4NSXlJPWpPVnqmbHU76cYNLWyoGOYcnD4WzCprN-uhzjZPHamvYT0EZkE0l_8UhzEBJ5_acwzvSHkrgjT7UcuhQTOMCywP2XX_ADXXPfl1CEZGJNweug4YQoU6_ZXklIR2oTrhEGSFXKAxd2R3f2nvkgmY8UvAxEjQCJ4oQqbg8OVOwFiWtpJ0OFmwOhkH9xq3WEGmE16f9ksYBFFEhtfTyW7dRyTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841e48be90.mp4?token=bqFHE1fobmCTX-aBOjDphiK6EMBfQMC-hv6nG40s96Eba0ZU37gy5tyMpEp9w5VXLQwInUvp_L-ubCn5vH0ZDZEqe5_8pr7GrhKw1rHy-6r9_-htYBfnMHwl4NSXlJPWpPVnqmbHU76cYNLWyoGOYcnD4WzCprN-uhzjZPHamvYT0EZkE0l_8UhzEBJ5_acwzvSHkrgjT7UcuhQTOMCywP2XX_ADXXPfl1CEZGJNweug4YQoU6_ZXklIR2oTrhEGSFXKAxd2R3f2nvkgmY8UvAxEjQCJ4oQqbg8OVOwFiWtpJ0OFmwOhkH9xq3WEGmE16f9ksYBFFEhtfTyW7dRyTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر بیشتری از حملات هوایی عربستان سعودی که استان تعز در یمن را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/149672" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
