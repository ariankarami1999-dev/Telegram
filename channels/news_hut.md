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
<img src="https://cdn4.telesco.pe/file/hIuGvJSyWv7e0pfT0duJG5ZKbWz1UJ47rSzSkhdTTafNlcq2NCdhPlaoyoqxJiAXGfzuKj1hBWkBhNkPAshTSIJ-OJG8Gb_zWzKs3RGUXoOaeZGpugzuAECazilHsIaZN0GKqFWD2pSKdib8O_p9_7aNnJ_iaQg_YvoeOnqGjd91c4ixQEzSzZ5SO4n9YOlUolfJmODdHo-Xn1eJ-lCO5l-FfI9SCp4QCLdvSMKM4DQJCQoVY49wPhYm8cXRqqdj4THEGDCMOUATxBeu3EwZpE3zj5OsVUI5s6la5TwL_iATw302ssiPoY-wUwYjfxmnzp0deFimXp43qg3IQVsXfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 223K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 05:29:52</div>
<hr>

<div class="tg-post" id="msg-66405">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XclirMHnNPE9R583h4viXvbz7HW7Q38VvbEQbTGyYbC_BjT5jiXKfs3I6fmdKWZ6wBki7BB6T5CgISULXMk2kdzOqxCEGigC8IlFT_goZxGtVGVgvmHxnuTz2Hju-50FYu8OyZn1ZGjlTAXdSQXzp2ti0nxHspzgOMUApW5b1ParLuCdlFWOWxR1ht9MYsVwxrXsR8hgJ9SKu0tMZacPaoiAXUpLwRv9JNiF99fAL1Gsy9IsUCDGflvRJWm8w8JZjTGO_ric1M_zrTpmYLiQ0CMKSiF2WKKOrAc267yDNbtd0725NZffoDyPqqNF73SNErm8de8k0Sv0FUQ0ksFxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQfNUPLXqF4oV7Bvp-w6z0zeq4wq3hvi7L-6v8jxDDV71jujNi1sXzqLrSMFR1jpfjQ0STbBEcRaEMa73Ds8vaHg3SJgJCfYZkhcOd79lxnlzIroqHTXihidpV8CiCgKhW6WR2GnDqzfkX93Oda-bdgIzH4DZfIDVECdFVTnkKNY_dky9kosnDuxFSI9pKqgpTVYal2oySZBJungAZHhn1sGfDYzMG1BodmJveyqXobrkx7fJYSt466NmQxs0nHVu6yw44vJbORwHskBnSZWRfckghJzXoC-lzMhUO-mpbMtPlcoHHe06MTcVm_bxPxBietwIICYoqh3RQ-0iOuc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CjbCnIU9n9ZFYxSLASrCAmV0HyP7Y1DlD3kKEWbiSg5x0oFzsndcvEKUW-aMfdct5-Md_OiH976nNSLTJoU7E5sazhpwGpQYmcWSdAPEsJImSoG5T-44uXZzo79qBACDZe3g_HhZD2TJ7KALv1kHLywiRqZEm0X2_-2GI-f3Hec6t2689rT7qPoohiYw8FLhnJMEsyBJjhB-g7OWCjeq0ZxPUjcbrClDNkVGGgmiexldofdF85m3_SucTXQK8IXh8DgMFG12JtM4E8jQccHpOdoh5yLseawyGtO_ZitjHA79aDQ40JbL13jDJsFrk_dxyoizAy6oB13u1n_xGvlQ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد  @News_Hut</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/news_hut/66405" target="_blank">📅 04:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66403">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8QaVCiSgjqKt3lQNkGke4WP7wKPCum7YPspOz_5vRPvpstcqyTq_zrrVmbxOErTruSgZugM8HuQhLki4SjNCYSBPuGpkz22zKMNwOW0LfL41rri8ng7f-Z2a4R06K4hi8NxND4cKdJHlf_h8sm6F9nWNi8LTZbcniF0vKJQfdV86BMvRYkhXPDy3NKt2tAeqzWm-aAunsCxfOMggPCJHsoRY1xazl-sJhe77BpialtfVTafOugdThvsM0Ba22G19xkZbitMPpW2g4wMhzNnKKr3ds4Pd7_Fb8u9BNnAxFSWf3wOCHzv5CuTxWy9s_vqDIuYmEL05QiCr0FffOm_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be88e9229.mp4?token=nHIaK4wej7Vu5wspzeGM5Viun2Nacq3O7HsRiv4bXjMDvTDSghkE_j2BSLaOYWRf7qcrKGVNAZm0OqsgPq502Ia3RWAMlghQiDSIBnphANYZkaJ19uqVUnt5zpMEDqh153BJQD5MK1ZtDD3DmlsojvqFmgAv-ZZ8yWGgg4HulV2XnAeJB-wPgqolahrlVnsDLnAMySHnDEdn00r-KaMqk4w-wKYR3kwU3CmI0X_NkRn6RAvudh0hC-bYQPcvlOUVGlL8fIJGL0nIrhA3BTBcZOZTF5ogJ0OnJToANUH5THn05gBw2fhUToqbzq7CNIb3Zov6Ic9KRkFs-nyo8l3dQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇺🇸
#فوری
؛ تفاهم نامه صلح توسط ترامپ و پزشکیان امضا شد
@News_Hut</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/news_hut/66403" target="_blank">📅 04:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66402">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/news_hut/66402" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66401">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/r0yFpXdHUEN-PFI8WC0-o3kibSmjTAjugpFZTY-mgkF61uBSj1MH9LRjzFl3L_3-dlSbrumV7A1aspc-iStpMjz-p0BjUi3jQAAYuznFe0TwGJHbhhtkohMAZ6yd0bGhdkCVGBQvXae1BwOBIuuTBFDmT8pT3xVpiMW8u8_VKJ4iM0ZuLPRABBpuWyQfw8S8daxZ7iYocGp4d7cJOFZS_Fe2A3vFnqgoC-rLR9RZKqZ6VCx23eCX8Tsd3roHrGD7bTvTDFi57J9DEUO31WEskkzLSIlF2aOwHk8V5z_SsyLneVgv6QI9E4EXPrx3LhJ8WXiyCrXGxxINuuaPQ19WJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/66401" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66400">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/qMT9zzcCutRbQ6rO7KjoShWi0j5uONoM76s1s-IR2Grq41urFIFcgfIpFPYVSrj6ueTXTNorPpkBosJLjXJmYHlisNGcy1xIe0MMuA0HeFAGU-Gfs6K5rP49IBkPehOxaI_q6uKFLLZQuzwqHHhHC2jPU3qUcvIWUwVYZUqWXWPyK-c9WTqzAGDU8n_f7mbXg4pGbP76LEs7ZAeLXd3d-HQ2kbYiip2CXJFdzax9qw9C-aqcrwnFm77ogE8BqOQasZx9jitEDaKkqGvoG8H-BGFit6enxblmIpbZbS225SEKEaJvDj0i7xHw0o5wDVOMQxycUccmoVhm6bmXQj-XPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/news_hut/66400" target="_blank">📅 02:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66399">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
متن تفاهمنامه جمهوری اسلامی و آمریکا:
🔴
1⃣
توقف فوری و دائمی خصومت‌ها بین ایالات متحده، ایران و متحدانشان در تمام جبهه‌ها، از جمله لبنان.
🔴
2⃣
هر دو طرف متعهد به احترام به حاکمیت، تمامیت ارضی و امور داخلی یکدیگر هستند.
🔴
3⃣
توافق جامع باید ظرف ۶۰ روز مذاکره شود، با امکان تمدید به توافق متقابل.
🔴
4⃣
ایالات متحده بلافاصله محدودیت‌های دریایی خود بر ایران را لغو خواهد کرد، در حالی که ایران به تدریج ترافیک دریایی را باز خواهد گرداند. نیروهای آمریکایی در نزدیکی ظرف ۳۰ روز پس از توافق نهایی عقب‌نشینی خواهند کرد.
🔴
5⃣
ایران تضمین خواهد کرد که ناوبری تجاری امن از طریق خلیج فارس و خلیج عمان انجام شود، با بازگردانی کامل ترافیک پس از عملیات پاکسازی مین.
🔴
6⃣
ایران و عمان درباره مدیریت آینده و چارچوب دریایی تنگه هرمز گفتگو خواهند کرد.
🔴
7⃣
ایالات متحده و شرکای منطقه‌ای ابتکار بازسازی اقتصادی و سرمایه‌گذاری برای ایران به ارزش حداقل ۳۰۰ میلیارد دلار را آغاز خواهند کرد.
🔴
8⃣
تمام تحریم‌ها علیه ایران، از جمله تحریم‌های ایالات متحده، سازمان ملل و آژانس بین‌المللی انرژی اتمی، طبق نقشه راه توافق شده برداشته خواهند شد.
🔴
9⃣
ایران مجدداً تأکید می‌کند که به دنبال سلاح هسته‌ای نخواهد بود. مسئله ذخایر اورانیوم غنی‌شده از طریق مکانیزمی که توسط هر دو طرف توافق شده، حل خواهد شد.
🔴
🔟
تا رسیدن به توافق نهایی، ایران موضع هسته‌ای فعلی خود را حفظ خواهد کرد، در حالی که ایالات متحده از اعمال تحریم‌های جدید یا استقرار نیروهای اضافی خودداری خواهد کرد.
🔴
1⃣
1⃣
صادرات نفت ایران همراه با خدمات بانکی، حمل و نقل و بیمه مرتبط، معافیت‌های تحریمی فوری دریافت خواهند کرد.
🔴
2⃣
1⃣
دارایی‌های مسدود شده ایران به تدریج طبق رویه‌های توافق شده متقابل آزاد خواهند شد.
🔴
3⃣
1⃣
یک نهاد نظارتی مشترک اجرای یادداشت تفاهم و هر توافق آینده را نظارت خواهد کرد.
🔴
4⃣
1⃣
انتظار می‌رود توافق نهایی از طریق قطعنامه شورای امنیت سازمان ملل رسمی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/news_hut/66399" target="_blank">📅 02:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66398">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛بقایی سخنگوی وزارت خارجه:
تفاهم‌نامه به‌صورت الکترونیکی بین پزشکیان و ترامپ امضا شده. جمعه هم خبری از مراسم رسمی نیست و فقط هیئت‌های ایران و آمریکا به سرپرستی قالیباف و جی‌دی ونس تو سوئیس دور اول مذاکرات فنی 60 روزه برای اجرای تفاهم‌نامه رو شروع می‌کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/news_hut/66398" target="_blank">📅 01:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66397">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
سخنگوی وزارت خارجه جمهوری اسلامی: متن توافق با آمریکا نهایی شده و به امضا رسیده
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/66397" target="_blank">📅 01:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66396">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac08f5fbc.mp4?token=VryyjCSujXnoxkOIvFpUgOfe155ZaG0y9rF3xHRYTfBGCFpe-xi5TcxqBOPtEgTIJwNuhe3vg7MfV7h3j-OJAUs4er-nadh8bbDZ05GbykhsqPz_Q8GTQUV7WN3tq1bKgc-JbqhhffcVLNeYd3wRmfPFOZQMyxVBxUtwuM-Zh0N2N4x8V7KUpnCkZPXy_C8ib3TRxoq7GqFF-8L1v5vvenAXE0D6rO6ZkbWu3C6VXW6u_sb_fl85_Em-GhHF3zKKbrnuDTgCTwR-zoKY3B4s6PGtStpPFEzuA5JlbtQ_UbAF5gTJXEMQ9IGoyi7FVvon6rkoxbMxeIllt6Xaz-FUEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
به محض اینکه آتش‌بس برقرار شد، دیدید که دشمن در خلیج فارس اقداماتی انجام داد و ما بلافاصله پاسخ دادیم.
آخرین نمونه آن حادثه مربوط به بالگرد آمریکایی‌ها بود.
علاوه بر این، دو ناو جنگی دشمن که قصد عبور از تنگه هرمز را داشتند، مورد اصابت قرار گرفتند و دچار آتش‌سوزی گسترده شدند - موضوعی که تصاویر ماهواره‌ای نیز آن را تأیید کرد.
از سوی دیگر، هر فرودگاهی در هر کشوری که جنگنده‌های دشمن از آن برخاسته بودند، هدف قرار می‌گرفت. همه این اتفاقات در حالی رخ داد که ما همزمان مشغول مذاکره بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66396" target="_blank">📅 23:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66395">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df75a39b35.mp4?token=SxTdCOcIk5mtPWcOiNOhwADiARJXjWGiP1N8KzEhy9C0oxIzWPP77v1jCk0PIXmWP1bZgn6rFPx27Za29P_wVmf28CJH6pjR_M7njUTeDa8xkp0vsd3MBlOmPCI_-p59gwEH4ZTn_Zp4vHwvCziJEUSulmB8DJRZQAsJrXvVAQNNIGimaL-zAezEVbjNHO9nHCCovGdPW37xMkcUndP5t8oHbUAEEN4HuZplTrMFw8ZmiLW7b9gtfutx6q3xjOSXouyhZ4wk_vCXn2ioMy4qU98C7dBfXkxLZ3v2F6_Sy-9cTXrRsfCWYdzYV4paWnkJ2R-O16wrfMRRsKBqbBdnXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏قالیباف:
نه تنها خودم برای حضور در تیم مذاکره‌کننده داوطلب نشدم، بلکه واقعاً از پذیرفتن آن هم اکراه داشتم. پیش از قبول مسئولیت مذاکرات، هر کاری از دستم برمی‌آمد انجام دادم تا این مسئولیت به من واگذار نشود.
یکی از دلایلی که نمی‌خواستم این مسئولیت را بپذیرم این بود که دونالد ترامپ طراح، فرمانده و ناظر ترور قاسم سلیمانی بود.
سردار سلیمانی برای کل جهان اسلام عزیز بود، اما برای من به‌طور شخصی معنای متفاوتی داشت. آیا فکر می‌کنید برای من آسان است که با چنین فردی بنشینم و متنی را نهایی کنم؟
با این حال، وقتی دیدم هیچ‌یک از مسئولان فرد دیگری را پیشنهاد نمی‌دهند و پیشنهادهای خودم هم پذیرفته نمی‌شود، مجبور شدم وظیفه‌ای را که به من محول شده بود انجام دهم.
ما قرار نیست فقط کاری را انجام دهیم که دوست داریم؛ بلکه باید کاری را انجام دهیم که وظیفه‌مان ایجاب می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66395" target="_blank">📅 23:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66394">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6d42bdbd.mp4?token=WnMWSLshpEH2-BapnvetjTBD-kR8W7q-EDI0M3Z2mZDfjQo0Kgu8QkLceZgJb06NDA1Clhzdbupjj2pE4-L6W7JwcoV56A_ROnalV3uGg57br1kw3G39kENfJBu8RIjPXE7iclB6wKKxAZnmcZxNBPqdtQRQ6rBk4it63a9lspb9WzYFAZDKWnmxPT2N3pE7cehSMfVAUxSTW5XvCkJ2DeUnkee34QPI0e8MDbfyHuwd6qm69crIN1dZHCaNYAC6fUnXvw69w9KYm5ZoL_R-bKuMeVLDIKICHNs1ic9ZyaqXF17U5eE6N4p4KxtvOpPU78l9VyzKv9jlR1VYkW_aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
لبنان بخشی از جبهه مقاومت است. طبق توافق، ایران از جبهه مقاومت حمایت می‌کند، در حالی که ایالات متحده حامی و متحد رژیم اسرائیل است.
بنابراین، طبیعی است که وقتی آتش‌بس برقرار می‌شود، باید در همه جبهه‌ها، به ویژه در لبنان، رعایت شود.
باید از مردم عزیز لبنان، به ویژه شیعیان و حزب‌الله، که در طول تجاوز آمریکا و اسرائیل به ایران ایستادگی کردند و نزدیک به ۴۰۰۰ شهید تقدیم کردند، تشکر کنم.
در حالی که ما در شرایط آتش‌بس بودیم، آنها به جنگ ادامه دادند و همچنان تلفات دادند.
وقتی رژیم اسرائیل ضاحیه را هدف قرار داد، ما ایالات متحده را تهدید کردیم و اولتیماتوم دادیم که خواسته‌های ما باید پذیرفته شود؛ در غیر این صورت، ما پاسخ خواهیم داد.
ترامپ مجبور شد در شبکه‌های اجتماعی پست بگذارد و به نتانیاهو بگوید که حملات باید متوقف شود و دیگر نمی‌توان ضاحیه را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66394" target="_blank">📅 23:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66393">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed9265802.mp4?token=EpvaCiEXMga6ST4abIQJ_q7WOt2xftEilgM99KeFgohpP25c4vuKwFLoayW2WDgst9a-bP-SG-vPpwEP0JR6WJvARaR1sbyc620XJMCtiIh9FecBpjSG8gF-EZhf5dzxw5nUVBYCjqlmEG1FbFxORS1MWeJiW0qD-h_nZjH9gVcEAla0h-NOqBBiP3EF3IEnc_hEb4bBhAq-2KjBT0e182Q517PY17fAxOIBJJW6p8ZulSlHnq7JrHgQy4pZDHtW9IymOM853IAQZNjzKKWrtrrREzefeq_7vKiLjSoTu0wF2zEFcSlmJ39JMxkZivPOJh3QhaKFZMi5w0ezoIvuVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
بدبینی و بی‌اعتمادی من به ایالات متحده از هر کس دیگری بیشتر است.
حتی اگر توافق نهایی حاصل شود و توسط قطعنامه شورای امنیت سازمان ملل متحد تأیید شود، باز هم قابل اعتماد نیست. تضمین ما قدرت ایران است
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66393" target="_blank">📅 23:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66392">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afb769475.mp4?token=RshAaI4BMryv8AQs1-6M3TBTcNa_W4Gc5WFfcUsRy3qNYncf8W9H_hxopEkqnL9dXzohrVNx44aJ_DLkjjkGoMOAnECpxhoyZQ4iyA8GHIMDH8Rd1ZUkfBxceUIK9XsZAOugYZPUvR0BYjQXv_k4S5FpaxsKHUcjVtIE6fJtTQ5iP3tD1lFpNIZTjx1juvDRtCQMPXCXZizpeyfb2-hfcwrANLTW9WoxHPvm9V5u2wD1O2x4UKZtAX3h3D45JCIenoniUlTIJ82A9mn5XSR8wtMhVItMG-JsX82DmJPLEMd7T5wLjtVOfeRlRpgCXr4m5XzZFrryv_EBRG3vAZy1ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
ما بر ایالات متحده و رژیم صهیونیستی، که قدرت‌های نظامی پیشرو در جهان هستند، پیروز شدیم و اجازه ندادیم که آنها به هیچ یک از 9 هدفی که اعلام کرده بودند، دست یابند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66392" target="_blank">📅 23:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66391">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a462c62e6a.mp4?token=axNQ4FqxcGEuRKOB8m3JeNp1zGvORPMVcv70b7QUTQ4ijg5qnYb6xFGD_oT5LH-AAMEqW9RVXRnzLTU9icGnJKYVXcQItERZ3pTjFrhl5pBg4UX2sCNxUqOlb0_uR4VxkvNAzU3mpYgzS0pxTEHLltKMh77t8jmnib_UR0hqstjb6ZvhBkysp800R_S5SIeYZOggkJAA8OOMdk-0iiVNEz6why71s1FvooqJEEyGFvkvamgmoHk7pBTzIOdWxi5KPOqEJh7P9_MLtAnGZEhT1vpVWdpzVrtbU8bQ1EXxHHGXR2-_S-Atcz6N-7c_EVlJnEggTeEKGxUtiyIUtxohJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
قالیباف:
تفاوت بین مذاکرات فعلی و دورهای قبلی این است که امروز دانش و دستاوردهای پیروزی در میدان نبرد به عنوان پشتوانه دیپلماسی عمل می‌کند.
در مذاکراتی که به عنوان نوعی مبارزه انجام می‌شود، نه تسلیم وجود دارد و نه شعارهای توخالی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66391" target="_blank">📅 23:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66390">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0UhY4FjdKvZlVF6Sh-inuefri5dvi5_hGgFGH04teDmzJOvVN5XtdL9AAVOO1cgu-pPAwTIG8tbaUheat16BVBEHXyaer2JtUnhWV4cFqECmrh5TH6c4WMkvBE-FoKk6SaFMWELP1iu-ESNlOTccez5vRijPNwGECbhMPcbRoqEtV86imqqfIuw6rbEoVRkW0v9BnCsY5tjD1G03URTj22hgbVBwmf9IhmEfp5cCPh_D9AHyCzdmwO7guGLRTupcEQxJZ4FuvGWwe4fMzGY25EoidhBnL20IdC7x8XTRPaYfwCVAC3be1RAzYVzCqGyfizLJsQzoDCJP64N1iLwWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شبکه خبر:
مصاحبه اختصاصی رئیس مجلس درباره تفاهم‌نامه پایان جنگ تا دقایقی دیگر
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66390" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66389">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d9400b7a.mp4?token=GDKp-XkRRJoXpmKiLOnujoHvAl4hPxdUBRpvB26gG66GhJoqPWU5-mbVlYpj2XJUbIAqYmalauhlbmjyqyPRuhztP6E-cmsaJryqnPH_khcJqPSPIKVVduueBJLsmmZ2Neagbd05Q_v5CeDEdcWzC7-IPCYzl58EZvAceaVECFPHboqtrYOMq-57B6phnf2-G83bsHXBUXpaSrEez4D4tK4g7YBGACMbjYEFQPuPRrXfDP5QnV1ZSQeBEyjHrEQ1ONZa0hz1lwdfqAZcNOEAbDa9pPc3WHDUsvCDLhpeeXKrInooYAV_DNBhmiI-3NwzbdA8W02mdKL6bWr3-GmzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی گسترده انباری در سن-سن-دنی، پاریس
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66389" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66388">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkpEHFhS8tUeKasqd1LXL-FOdbDmH1wiGoKzGPVuWgHvEymV-k9DxEbOYlIUuPb03ghkVUJyDHxv4OXGzgxPgNJzzvwpYNgs5cyMsJ-2AEx4Ve-UXyfGbTJoGDsj07s9LDEzPAU4n2fdJWirQOFxXk3-2MnOUkBz1uI5I8-BrnuYsWg4XbvLUsPPhIRL5gVfx4A_gY-nguzhlqa9QJwA1AkqosYfJAGauJCK3k_iiYgUvYzzELK_xNm3v41b0DRO57GsDSDra7GbbVi4b3Y2m4DQJgKudJ2XO4HEUYP7aBYU0tKflG4NRx9gjHWqteH9b993gRwDkpVi9QQOol43YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیندزی گراهام: من همین الان یک بحث بسیار طولانی و سازنده با ویتکاف  در مورد ایران داشتم.
بعد از این بحث، به نظر من امضای تفاهم‌نامه برای ایالات متحده مفید خواهد بود، تا جایی که تنگه هرمز شروع به باز شدن کند و خصومت‌ها با ایران متوقف شود.اینکه آیا ایالات متحده می‌تواند در مورد برنامه هسته‌ای و سایر مسائل به یک توافق قابل قبول و قابل تأیید با ایران برسد یا خیر، هنوز مشخص نیست، اما من جنبه منفی کمی برای تلاش کردن می‌بینم
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/66388" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1096f4de.mp4?token=L_aKWg4ppGelskHK-ZMo2_0D5TDyX-vaOV-CcNG7VBbhYbHRH0oQVDoOau8n1CX_1AVU_uA8J3_rQVQEi0m7WJsbatRVgTWI_JWNIkDBASpqW35uH63UmKA2FI-mNjxarPJ7EcEHLP83VO672_MeJp9Yh6GNlAdNgn63ghjnAwHgHGm-6_YQXfnfmeNs0tF39_0g7dIaRgZwJXoRKN-wniEaEyBMq_XzGdO20H2SUHo1hs_NDLQqLIppYQsloZal9jT7xwoVNSFNkDWUGpTXSA9Yrqwy6gx1_e-Y69FxVvMJn6HUy-ZkHoTAR34oLSxmiDBOHgmyzqUV7orhtWdPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف؛ آن روزی که من پا در میدان دیپلماسی گذاشتم گفتم:
من اینجا آمده‌ام که هم آبرو بدهم، هم خونِ دل بخورم و هم خون بدهم؛ اما اگر کسی فکر کند که از مسیر امام شهید، مسیر انقلاب و عقلانیت ذره‌ای فاصله می‌گیرم، هرگز!
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/66387" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66386">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ofAMABWJMfav1n9nIVF8e7fiNnO7teoVPPE-KILPU6I-csGEDHXnL-vEgnpB-_I6rDYw7nh_krdKC-YpCc8veN9-psT5uiiDVG5Lr3DUJct8XSLFMDFicpVGlzBflArDzcUjcLX4j5uTsuZg9UWd-UML7CTU_uMdOT44O6u9tz3MiSUmMnWwS4TcQpr8iU5VX1DpRuFc_OUsWxT3snpFifCfWxaOdDY9VsmxgPsLYSd1-rW0FFFPmKm1onJ0YYHDcC_9XpYVE42oVq70iw8MDRuClyHzjSYANAMvPrHng8PcewSF2a0-8h_A_Pg_igOFl0PC7P4-S9nqqkUvrLL2Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a579da34fb.mp4?token=ofAMABWJMfav1n9nIVF8e7fiNnO7teoVPPE-KILPU6I-csGEDHXnL-vEgnpB-_I6rDYw7nh_krdKC-YpCc8veN9-psT5uiiDVG5Lr3DUJct8XSLFMDFicpVGlzBflArDzcUjcLX4j5uTsuZg9UWd-UML7CTU_uMdOT44O6u9tz3MiSUmMnWwS4TcQpr8iU5VX1DpRuFc_OUsWxT3snpFifCfWxaOdDY9VsmxgPsLYSd1-rW0FFFPmKm1onJ0YYHDcC_9XpYVE42oVq70iw8MDRuClyHzjSYANAMvPrHng8PcewSF2a0-8h_A_Pg_igOFl0PC7P4-S9nqqkUvrLL2Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
وقتشه که سنگر رو از بچه های لانچر تحویل بگیریم و یه زندگی خوب برای مردم بسازیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66386" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66385">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=odRwzigoYXY8DPIbRyfRDHKoEbslaDst_7fuErwK6aojxcRDJ5ffWjaK1cQhYwMyPZaNYtHZOxoNn0m3VfE8O6mBsh8wVtY-as71xa-58Vxeb7VUar7YdqkThGRmABzHE9rj7t6i7eEBhcpxNrA3uihn4vgS6x7jY9xPzb7JKc2Fdt52DlpLFD8SWtHrIH_lQS-BEzgk8aSAIlHNQushWnku9oE6__k2GSEx8g9bGA8v9bltcG7HwhersDMX1XXovu6B0qjPfZFSkvWjydIqEgdwrTeKWrMnbIw43j00MA9Bh50q7eNs6RDJpXBghK78eR9uNqLaNzX9WHIMfq9S7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c7f8ec39.mp4?token=odRwzigoYXY8DPIbRyfRDHKoEbslaDst_7fuErwK6aojxcRDJ5ffWjaK1cQhYwMyPZaNYtHZOxoNn0m3VfE8O6mBsh8wVtY-as71xa-58Vxeb7VUar7YdqkThGRmABzHE9rj7t6i7eEBhcpxNrA3uihn4vgS6x7jY9xPzb7JKc2Fdt52DlpLFD8SWtHrIH_lQS-BEzgk8aSAIlHNQushWnku9oE6__k2GSEx8g9bGA8v9bltcG7HwhersDMX1XXovu6B0qjPfZFSkvWjydIqEgdwrTeKWrMnbIw43j00MA9Bh50q7eNs6RDJpXBghK78eR9uNqLaNzX9WHIMfq9S7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس در مورد پرونده اپستین:
ما نمی‌توانیم فقط به این دلیل که فکر می‌کنیم چیزی اشتباه است، مردم را تحت پیگرد قانونی قرار دهیم.
شما فقط می‌توانید مردم را در صورتی تحت پیگرد قانونی قرار دهید که مدارکی برای اثبات تخلف آنها داشته باشید.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66385" target="_blank">📅 22:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66383">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
سخنگوی وزارت خارجه جمهوری اسلامی:
در یادداشت تفاهم ۳بار ذکر شده باید جنگ در همه جبهه ها از جمله لبنان پایان یابد.
همچنین بر حاکمیت لبنان تاکید شد و حضور ارتش اسرائیل با آن در تضاد است.ادامه اشغال اسرائیل از جنوب لبنان نقض تفاهم‌نامه است و اقدامات لازم را اتخاذ خواهیم کرد.
یکی از بندها تایید میکند که آغاز مذاکره و ادامه آن مشروط به اجرای تعهدات است ازجمله توقف جنگ که شامل لبنان هم میشود.جنگ بایددر همه جبهه ها از جمله لبنان متوقف شود تا مرحله مذاکره آغاز گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66383" target="_blank">📅 21:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66382">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=cuy3s-8KxW_FQAVhSa-xMTM2R9uU5tuAHOcX7sRPSPZI_tOEOQts9ZK1SpC78FmA-XOJgewSbzRN_ptXz3L5WDTcR7zzm_OpXgcsBYi06eVuslISlx8xKrPmkVfeDLlveXx3Qm8Mz9Z_BpYbYB8G_D3vf_oioxvZxR_vUesydSiRs7t6pgEkY8tHTSJoE2EnoTa6yXH0bYJHEagPpn5rTbEVfgHir22i3pxytI1ZqLxr582RhA1Y7mWwFkxekqMy7JzmtIM4AgpYgi4hCKh6sDwhd5bJjQyOAt1UEE7R4Jlm2g-s3U42hNwK-J_0W7nt2HPckhyKj9XCSvl9N-tU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a620bba5be.mp4?token=cuy3s-8KxW_FQAVhSa-xMTM2R9uU5tuAHOcX7sRPSPZI_tOEOQts9ZK1SpC78FmA-XOJgewSbzRN_ptXz3L5WDTcR7zzm_OpXgcsBYi06eVuslISlx8xKrPmkVfeDLlveXx3Qm8Mz9Z_BpYbYB8G_D3vf_oioxvZxR_vUesydSiRs7t6pgEkY8tHTSJoE2EnoTa6yXH0bYJHEagPpn5rTbEVfgHir22i3pxytI1ZqLxr582RhA1Y7mWwFkxekqMy7JzmtIM4AgpYgi4hCKh6sDwhd5bJjQyOAt1UEE7R4Jlm2g-s3U42hNwK-J_0W7nt2HPckhyKj9XCSvl9N-tU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره محمد بن زاید:
محمد در امارات متحده عربی یک جنگجوی باورنکردنی است.
هفته پیش بمب می‌ریخت، گفتم «کی داره این همه بمب می‌ندازه؟» امارات بود. او یک جنگجوی خوب است
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66382" target="_blank">📅 21:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66381">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQwlfUFqLnJQKtWE6w02VXWzxJKiXFRJu0nEONjJpeKvGqc22h3MXPUkq74KFbrAMmZl5l-Y49_OInzao19Ofp4nN4lNj2zZnUF7Q2GN_5lG9j4R76wxcpOvTU2gMXFmOTUMxj4JXy8otPiavkc4zY7a9E6DwvfAAvGycyuZwzu-oxJ3LZhZ6Fkd2fVsWGA4H6A9b-DG-O_IcgkC5DrIbfHegJsBu47usNeLV-V8fE8azzxxwPNkhrnhqnpHSum1wJcaveSL7sNEvonqEb50onlF25pfdJAJ0lw8GxvC8wjXJhNZOHDRY1buZ_aCtE-N7F8qbErwQiEiLys5-ys5vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛الجزیره به نقل از وزارت امور خارجه ایران:
ما در حال حاضر در حال بررسی ایده امضای یادداشت تفاهم از راه دور توسط روسای جمهور ایران و ایالات متحده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66381" target="_blank">📅 21:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66380">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729c69207c.mp4?token=UCg9UN8MoMLizITv4XCzqM3waDN0P1vv3A5PUIxBkfJYwq_fBFkwq1ahwfxHe6108SxfH3lJn85hBtna4xzXRoNaQxkx_RLccs43uildfe4Yvc7zgpWppjckEvmP4lysuz3738ZFM7RbrojSfjuqQVV3ep-mvm6u4TuXyrb2t6-MDj0T9E1pZoHg7xVMQ-gurhofjqfcslFYokGIpa1ZE6HJwtsRVBKsIr4IL1Re9tBLnJoZg91MwUpjj_QyLq3uu72bgO_ClpCF-zslBcv2qkTIqQa1v_CiZacWTeEC6ScqAn_vb8zdKLzuuOnL4mKYoAvQMlf6K-qL9j2oeRY1eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
اگر آنها به توافق‌نامه پایبند نباشند، یا برخی موارد حتی در توافق‌نامه ذکر نشده باشد - این یک یادداشت تفاهم است، اما ما بدون نوشتن آن، از برخی موارد درک داریم - و، اگر آنها به آن پایبند نباشند، احتمالاً به بمباران آنها تا زمانی که به آن پایبند باشند، برمی‌گردیم.
می‌دانید، شگفت‌انگیز است که بمب‌ها چه کارهایی می‌توانند انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/66380" target="_blank">📅 21:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66379">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
#مهم؛ پس از روی کار آمدن مجتبی خامنه‌ای به‌جای علی خامنه‌ای، #سعید‌_جلیلی نماینده‌ی سابق علی خامنه‌‌ای در شورای عالی امنیت ملی عزل شده و #علی_باقری‌کنی( برادر مصباح‌الهدی، داماد علی خامنه‌ای ) جایگزین وی شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66379" target="_blank">📅 21:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66378">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=T0HIX0gmJr21MV4_6bUrnwTwqoB0o2bo6xG-zP3UkFJuA-r_Va8h7NLXRrcycgJaPld5Ub4Qb3v03wmISNSSCQKeG2pQrp0JMlFDVvUIVvgteq4U_FaZiJaR5UW1Q3DZY7pDN9kZ9gPM7BycO1dczIgkp4kVl-nkeXY-R3KXDFqxbfc6SgAd2rpvHvDCpM-laZXgukPyRV_6DYyk9UxovOBmT6rEoxUahCj2qRQlUr8VCbI72lA2vynz0d_h8TLXCR9FgqQoxpVgzChf8kJoyjfukHjo69pOel060_xu1EerrpdNN70vyJCa2MF2fRIVwkEEgwhqxfdhKXoNfB-epA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533e14dcfc.mp4?token=T0HIX0gmJr21MV4_6bUrnwTwqoB0o2bo6xG-zP3UkFJuA-r_Va8h7NLXRrcycgJaPld5Ub4Qb3v03wmISNSSCQKeG2pQrp0JMlFDVvUIVvgteq4U_FaZiJaR5UW1Q3DZY7pDN9kZ9gPM7BycO1dczIgkp4kVl-nkeXY-R3KXDFqxbfc6SgAd2rpvHvDCpM-laZXgukPyRV_6DYyk9UxovOBmT6rEoxUahCj2qRQlUr8VCbI72lA2vynz0d_h8TLXCR9FgqQoxpVgzChf8kJoyjfukHjo69pOel060_xu1EerrpdNN70vyJCa2MF2fRIVwkEEgwhqxfdhKXoNfB-epA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
مردم از من می‌خواهند پل‌ها را بمباران کنم.
من قبلاً این کار را کردم، چون می‌دانید، آنها به یکی از وعده‌هایشان عمل نکردند و من بزرگترین پل آنها را بمباران کردم، معادل پل جورج واشنگتن ایران.
اما ما آن پل را بمباران کردیم، دیدید که
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/66378" target="_blank">📅 20:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66377">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=DTCvR-nl1uBKAi2o5PgNMn1oVGG-_GeLarTZ0I6FQhn-NUQ7_GjxJYFd6DsFtczlvY356URfGQLWzZ7gYNiYmfv9H59oPZUbxW2KYZoIGH4eD-1vTyhZe-X4G7gdGLxVOxh9NS-fTvZ92Bg5o1Vt-dgbjlIwYgiIILV8eD_R1qHiBYu9WQK6JEzd0pwnMMUlIZLA9G6NYwcr9nedotDhgSllLaKbpPsfSFyUKPrNu9y2gt_Eq_k3kkAgpFJDFFh0rEk6QCibYbF3zU7-IhC4xz9IAxKKRvu-Ee9j7B-dl6v5qgy1J2Iq3S348bcs5vRxyXKonhlXLU6Dkg49pnlIZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea27fd13ab.mp4?token=DTCvR-nl1uBKAi2o5PgNMn1oVGG-_GeLarTZ0I6FQhn-NUQ7_GjxJYFd6DsFtczlvY356URfGQLWzZ7gYNiYmfv9H59oPZUbxW2KYZoIGH4eD-1vTyhZe-X4G7gdGLxVOxh9NS-fTvZ92Bg5o1Vt-dgbjlIwYgiIILV8eD_R1qHiBYu9WQK6JEzd0pwnMMUlIZLA9G6NYwcr9nedotDhgSllLaKbpPsfSFyUKPrNu9y2gt_Eq_k3kkAgpFJDFFh0rEk6QCibYbF3zU7-IhC4xz9IAxKKRvu-Ee9j7B-dl6v5qgy1J2Iq3S348bcs5vRxyXKonhlXLU6Dkg49pnlIZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پرزیدنت ترامپ:
گسترش توافق‌نامه‌های ابراهیم چیز دیگری است که امیدواریم به آن دست یابیم.
و من فکر می‌کنم اگر عربستان سعودی پیشگام شود، لطف بزرگی به خودش می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66377" target="_blank">📅 20:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66376">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0cf6ba4c.mp4?token=g9v5qE0lufVhTVtOtYh4A0Ctsm85pjP88fuH1jjVy_hB3acExX8ntc9bQNnn3OgsroI6yqTS63_g-4J8uOik3ogZMb6Elts31BgOk2K-Jw0UqwEMKaQBudukBPkS7KYXMwW-UnpBX6m6KUGDFizfnmvVoQxmaMXZYlhdDMj4EJJ0T802D0GzB9YY8o5iBpmFkR-mV3yHOQeZknItwJZxeC0ou8RKHRAH1TJ71N19DthAEdykANl5SVMwEx8UsZbDkSZrEMKf4hSz1OMnV5yXXIM7na7elORXnWDQ0O5qgEmU_cOfNej2pMVXf6gTIEhTGTCvSsHebjD9hPBiPIYDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد اورانیوم:
هیچ‌کس نمی‌تواند به آن دست یابد، بنابراین مهم نیست که ما این کار را به سرعت انجام دهیم، اما می‌توانیم آن را نسبتاً سریع انجام دهیم. هیچ‌کس نمی‌تواند این کار را انجام دهد. و اگر آنها این کار را انجام دهند، ما با موشک‌های پاتریوت به آنها ضربه خواهیم زد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66376" target="_blank">📅 20:43 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66375">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=aC7Y-tbJ242BSeEzHqATneotmJGMhFnO5KzZSGUutn9C6lzrf-R0zB5s0uyXZ9RmCqTLDgGp8fugtCUK2GeRHvpjlVUcgWQ4caHLVTtUHYHBHXp91cil7CJbZtFcph4krN6CHZNC7USVLh1ZJiCejaUfR9iW_7BIZSzzUI1786nKIgyqeM8erKlaamd_BFvHvPKOfIYBKue7Obw_ANdQpkMwhVBKaV1XX270LgGuzuauhOAEZqvvZwlyUFXGbOMqZ5Nyn2vqOefWPlVMrrAY-4YdmLMNyN0H7XARtnVe8js3nefinHsrPsF3GUwkEXBc5StMgP-LCRr0fGZeoz24YQZm3-5oN1jLCw0RaAXbJMhFfqOPv30k4uq0yLmSJ-wzXLkr8JiCZ6zWGqgix0sGpKPAZrD5WKS4ZHml1S2jnNj3KQL9aAaGerWZ3yzT_ERook4-e7zDUUj8PC8MLLzPzRv_fQ37sEJMEOWVRoK7PvmrJrwplIbJ5GWqpc0QWxtr6n1vwU_TNRb4XqsNG6cPIPP9Qmc5cc6LHRIlfhULCqE_SXIfTb09p0skcwmvnXCr7etS29Gkf_H8fNxnQbzZewGT-Hhyttv4m4XTf0due3cD8tl7hAmavAAySB61Dm3fHNvmFhgva8F-l8Vui7NSqYy0C_9OTA9UaPXGX6ybALg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07c3e1404.mp4?token=aC7Y-tbJ242BSeEzHqATneotmJGMhFnO5KzZSGUutn9C6lzrf-R0zB5s0uyXZ9RmCqTLDgGp8fugtCUK2GeRHvpjlVUcgWQ4caHLVTtUHYHBHXp91cil7CJbZtFcph4krN6CHZNC7USVLh1ZJiCejaUfR9iW_7BIZSzzUI1786nKIgyqeM8erKlaamd_BFvHvPKOfIYBKue7Obw_ANdQpkMwhVBKaV1XX270LgGuzuauhOAEZqvvZwlyUFXGbOMqZ5Nyn2vqOefWPlVMrrAY-4YdmLMNyN0H7XARtnVe8js3nefinHsrPsF3GUwkEXBc5StMgP-LCRr0fGZeoz24YQZm3-5oN1jLCw0RaAXbJMhFfqOPv30k4uq0yLmSJ-wzXLkr8JiCZ6zWGqgix0sGpKPAZrD5WKS4ZHml1S2jnNj3KQL9aAaGerWZ3yzT_ERook4-e7zDUUj8PC8MLLzPzRv_fQ37sEJMEOWVRoK7PvmrJrwplIbJ5GWqpc0QWxtr6n1vwU_TNRb4XqsNG6cPIPP9Qmc5cc6LHRIlfhULCqE_SXIfTb09p0skcwmvnXCr7etS29Gkf_H8fNxnQbzZewGT-Hhyttv4m4XTf0due3cD8tl7hAmavAAySB61Dm3fHNvmFhgva8F-l8Vui7NSqYy0C_9OTA9UaPXGX6ybALg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
💥
پرزیدنت ترامپ:
هیچ‌کس سخت‌گیرتر از من نبود. هیچ‌کس سلیمانی را نشانه نرفت.
می‌دانید، وقتی من سلیمانی را هدف قرار دادم، مردم فکر می‌کردند این بزرگترین اتفاقی است که در خاورمیانه در ۵۰ سال گذشته رخ داده است. این بزرگترین رویداد بود.
او رئیس ایران بود و مورد احترام، اما او یک نابغه دیوانه بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66375" target="_blank">📅 19:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66374">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9392768ed3.mp4?token=g6X7saQ1vEbJw6iBXbgW6h3hWKwG2grXfrNW0UbQxpkel7z859dyERraUJMNeYkw1QtjJDi-xeA5NE8tzYRbbzbuxv29Xx_GR0ygjSNlliAua5UCLZBNAWIxQA3QsqffBhmq9G4QzdoqVyX8knD75I7wGMIP50SBE5fkFgiS5zNJNZRQRgW_kZqR4RsWVRCl9HyxWMm-7BZ0loL1CqT8n8xcof8g9SDB-bENsKyn4h4o3canFjD5Wq38xe5HE1ME2ItsdJeTt-Zi1ZfnRcod-gw2CfyYS2iAplN2Eqy6zXgRJ9-Yc2sjpBi6atCFqM8ATXazDOW2e0dPDl1htVn1IjIN0rz5QVqY_IphPgfLwdPzZVSpRuqvrFURmo-6UeMq36IifbFNpFAjhNVHozm23JKJtnCFo0CdVlJ9WVjk4_gvREvLGl5nPqsUWUAcJR4M1B3h6axIC0qkGEXvcT1QtmNpsQyUDhH6PXxK_Mqp5u7yNxYqeMKKKzhf1nqJ492MU-ETE35cMqvwJp6AArVPihH_5trFNY-JSfrwk5Ok9FEJx3X5BrFQOtyg201rXQRLpyRAy1wwsYohKrIcSWvJ1DEORykX_lfmPHROtLSIFFGn6g1XBYkP7G3_tO3KjXuYhbb4c6TLmvTyQs8lD-ktLWwwJntl5nxMrshwpMxcUmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ :
رهبران جدید ایران باهوش هستند، بسیار باهوش.
آن‌ها بسیار کمتر تندرو شده‌اند. فکر می‌کنم آن‌ها خوب هستند و واقعاً کشورشان را دوست دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66374" target="_blank">📅 19:44 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66373">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885ecefd64.mp4?token=uwZ5M2MYmVVd-z49B8IF9wzTwaCwcddtDmqfkpYqUw3AB5sHkHP1W6xvb2zUcQaQ1tv8_i3IoC09axhFquR0k36CvKh83dPAS0wbudvttIqn6Y79Enx1T0MmIH4BLW8O6OPO57yA4m4uMroUbvgZhiCoXGWd9IBTiP3DniNApMkcvZjfaTbKwG7s1CHF3mMtXPNZ12k5_nJGFXhMmGcMzWFpVI95btoCJRXqPUrlbfGa4_7CuDCeOI39Mmk0CuO60HzfQVpNu0RAijPTBAjHtEgVIruEn8a9vvST3JHFKXjmHfiwp_oe6ZndK7X_VFa57NjO80n7Ygpo4a4ld-aTRX5jpbK1gxQZ_oTrOGYzu_X8YAYOj31SeCJPwG59moLb_dsv2OOFNAXd3gg2ezz_xB8zviAcbeigzors-Cg_ZVy_EPlTgP4AlCcHowisHAnE6SPYSLzLAcRR8f7SIpN7SxLZIQTxAu7YoZcarNRXvw1UkOYQYMbvYysX5KgFsXPzvmINb21E9G93MSaQECf6bOvx0YQl-xhBXbiUf4qQ0_KtVEv_m3mz3yGIhZ3HUKxKtXJ559Jp5WNIqC3cokgYl9zz76nAepHufSEo3qQ-ecE0ElajHSirBOQjaWdfO7bDAv5TqBnTlWsGxSOxid_xofOCw4NTPAI33q2-GA2dp9s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
پرزیدنت ترامپ:
روز یکشنبه، ما به توافقی با ایران دست یافتیم که به همه چیزهایی که در نظر داشتیم دست پیدا می کند - همه چیز و خیلی بیشتر. جلوگیری از دستیابی ایران به سلاح هسته ای همه چیز در مورد همین بود. این حدود 99 درصد بود. آنها نمی توانند آن را توسعه دهند یا بخرند. آنها هرگز نمی توانند سلاح هسته ای داشته باشند
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66373" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66372">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/news_hut/66372" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66372" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66371">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rezbhXflGnYGZIGlMWpczoc8CsfIw9EUz6uxUQiebe53ShhCrDo87loeNL5cut5IjQ-kbkviTpm1KwYabEiZJoi9RVZuLZxr7j71kHQ8a4QSglexa1gI4JBtyLFF-WvGOCeh9Sem981FyP5BKmfHRe4Ecznqd4v4RDkmYoOV0ISay-1iuCeZE5enSgaSYN8mh0W5EqS2KP9qNltqP1BNKaWzUoUcgsHdRu0uRSljcb6TcIWAih1xFRHhL8HIsD6OHXZgBww1pbMafXdouJhiZH3niUuxEJio-dIRuLglcbwVyIfP3NFEtGkyXCvRsjKd5aWcOl7-ULti1ZQKS2m8Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/66371" target="_blank">📅 19:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbJaO9sdIEW_mFr2xQ3F66-EbIFvoWFxmW4FSmRoUnTwy5zz9fEVAPjmqool1lzjlleMR4x-aXwFQRWoaqDO_RL95TOnS_s7HKdliYTRkRZ2VlWLDipiTgIptRDkCTTggxPIrahfxdWBjL7VfDKGb9aSWw0uaz5jna3qknAjQVhPBzTvKGlJmudJPkxaA6T6uMcvk71ngRH86N6-U20dU4G0hvezN8vzNaMv9RrfmbtvKx0o_BESCkyYr1QvA9jeZqOM5h5EJSub1vvSDSMRZLmvshk-kYdF-tyIIxE4yRoRKXdPbA-1MCQqBekntR6xfv5DjXsstfWwqaoYF_q40w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توییت قالیباف:
تعهد ایران به همکاری برد-برد که بر پایه مشارکت استراتژیک جامع با چین بنا شده، قاطع است.
در جلسه‌ام با اتاق بازرگانی ایران تأکید کردم: ما مصمم هستیم که اجماع استراتژیک خود را تحت GDI به نتایج عملی تبدیل کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/66369" target="_blank">📅 19:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53224e4497.mp4?token=dPqGNq36F_QB5mNPKZZmjo-ySbU5Dh-jCOuUcanP3oUOBOHjEjw5gCaYSCAsqJhRZ-kJC_dcd_dN4UghR9peDNGWMTp4gFTYGd8A4Ao5U7CIeQvaU6KsPkuIOmTY3M_0nlE6n4lYmmMV6ApsYgXWc4zmTqNSFAUfeHoJyTl3fC6GLYgBgmot9qOaptsqXUlOjFcAMl3KnvQypRW3_IF3JvPlm9s9HCp2fYYZnpLBMv6kGgPkp_I_UC94YMa6ZF1p5NPcZEm85fG2zw-tvCkRN6mOQR5O6pLjgAW4URj96WVGniI8cWWLsLSa6A317LCVxnJYmXag9S-bUaksIv3CJ6sb2D-7JnHErVQIuixLu2pVpGVcg8L0CYa5wUsj5AzcSA-8NXWeB1QR2B8BwVSuRIfLD5iQIzTBaxNgXCeOz0LmHXNSkvy6IOLiCqmWW4edvFEL5tng-TV1ZvY_euEj4L55tyKbtSWHUhzW3oJHjHV4-N09e34VISvUynDjx_YXnr76KDwPHNKQ1_xE3IUCMq5BA3HVUUkvOEzTPlRsLuUdV_odEMf00f7PW_vAzKWqq_q1rqm9dkH-ccPEDJzy0p1n4cAUfKZBumzYNPJBeJ_19AjaepXULuCNDJKYMtbxQHphdYXLI03UbQnnrJQg_semHru51g87UtxxZ3my-sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53224e4497.mp4?token=dPqGNq36F_QB5mNPKZZmjo-ySbU5Dh-jCOuUcanP3oUOBOHjEjw5gCaYSCAsqJhRZ-kJC_dcd_dN4UghR9peDNGWMTp4gFTYGd8A4Ao5U7CIeQvaU6KsPkuIOmTY3M_0nlE6n4lYmmMV6ApsYgXWc4zmTqNSFAUfeHoJyTl3fC6GLYgBgmot9qOaptsqXUlOjFcAMl3KnvQypRW3_IF3JvPlm9s9HCp2fYYZnpLBMv6kGgPkp_I_UC94YMa6ZF1p5NPcZEm85fG2zw-tvCkRN6mOQR5O6pLjgAW4URj96WVGniI8cWWLsLSa6A317LCVxnJYmXag9S-bUaksIv3CJ6sb2D-7JnHErVQIuixLu2pVpGVcg8L0CYa5wUsj5AzcSA-8NXWeB1QR2B8BwVSuRIfLD5iQIzTBaxNgXCeOz0LmHXNSkvy6IOLiCqmWW4edvFEL5tng-TV1ZvY_euEj4L55tyKbtSWHUhzW3oJHjHV4-N09e34VISvUynDjx_YXnr76KDwPHNKQ1_xE3IUCMq5BA3HVUUkvOEzTPlRsLuUdV_odEMf00f7PW_vAzKWqq_q1rqm9dkH-ccPEDJzy0p1n4cAUfKZBumzYNPJBeJ_19AjaepXULuCNDJKYMtbxQHphdYXLI03UbQnnrJQg_semHru51g87UtxxZ3my-sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ درباره ایران:
معامله‌ها شگفت‌انگیزند. من تمام عمرم معامله کرده‌ام. وارد معامله‌هایی شده‌ام که صد درصد قطعی بودند، اما اتفاق نیفتادند. وارد معامله‌هایی شده‌ام که هیچ شانسی برای انجام‌شان نبود، اما انجام شدند و به آسانی انجام شدند.
پس هرگز نمی‌توانی درباره معامله‌ها مطمئن باشی. اما خیلی زود متوجه خواهی شد. فکر می‌کنم انجام خواهد شد.
آنها می‌خواهند امضا کنند  می‌خواهند به زندگی عادی بازگردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/66368" target="_blank">📅 19:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=iO48jucu2FKkK1l7RuL2N6hJ4k7--pW3bbmp2PN9w1XQQLIotF2KL3Ji7YSvJEQCB_6ZcVQHT0H11ARw2GYb_ovWy1rD1DmMSPL8voYoE1AIYylEfg50NoNRgqdtBUHXTnA5BuHeqJo2ve1C5HnO3M7hJ9vSIMF_nKAOb7l0Ullza0B3KN4gDuv60wDcabY7Nm5cLq0lFxYPc45yif0GUw_k8Cdpa3A_einsAFJJb3oBrxqfDfI2uaac8v4CeKZsnQjj8MLxdrjySGFiD9GSGbtehhiHcQrENXqoxxYU8njtvqVzxraV0cc2UTx9xNrShjfRiM5k-Rz14i_kpvpXSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ca2e02c1.mp4?token=iO48jucu2FKkK1l7RuL2N6hJ4k7--pW3bbmp2PN9w1XQQLIotF2KL3Ji7YSvJEQCB_6ZcVQHT0H11ARw2GYb_ovWy1rD1DmMSPL8voYoE1AIYylEfg50NoNRgqdtBUHXTnA5BuHeqJo2ve1C5HnO3M7hJ9vSIMF_nKAOb7l0Ullza0B3KN4gDuv60wDcabY7Nm5cLq0lFxYPc45yif0GUw_k8Cdpa3A_einsAFJJb3oBrxqfDfI2uaac8v4CeKZsnQjj8MLxdrjySGFiD9GSGbtehhiHcQrENXqoxxYU8njtvqVzxraV0cc2UTx9xNrShjfRiM5k-Rz14i_kpvpXSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار: آیا می‌خواهید اروپایی‌ها مین‌روب‌ها را به هرمز بفرستند؟
ترامپ: ما به آن نیاز نداریم، اما اگر بخواهند بفرستند، خوب است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/66367" target="_blank">📅 18:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06239668e.mp4?token=v3QoGQJG8pEE1jQ7k1sK5p19RpM-3kAbnEBUxZZZHKgNvCwXhn-K_SVY6_ADmhaGj4VxbXbHvZ6T2NKDNpFcHYFLRr00V0uB5mTpYtTD9TT3JzFAq8cRIwtYd9vSublFHo4sPa25ENzPSgMBfG5ogttHeDmNuDKbKir0TIrmWt5W49nJdwOdNzyIJTRYDeyA3RqA4iyw-kMUvIF8ZOvzEdxCUxDsAZ8jJKJ_UxwRIoL67HZVXN_BMa_dOZcCpP5-X20sZTymaOfI2GcGV9604qq1Wl96YGbS8hYxsDyaI7ojTX3-2BVNt8xRD7G3OiyIHSxDMYpVuZiZ5yyJXwn5Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06239668e.mp4?token=v3QoGQJG8pEE1jQ7k1sK5p19RpM-3kAbnEBUxZZZHKgNvCwXhn-K_SVY6_ADmhaGj4VxbXbHvZ6T2NKDNpFcHYFLRr00V0uB5mTpYtTD9TT3JzFAq8cRIwtYd9vSublFHo4sPa25ENzPSgMBfG5ogttHeDmNuDKbKir0TIrmWt5W49nJdwOdNzyIJTRYDeyA3RqA4iyw-kMUvIF8ZOvzEdxCUxDsAZ8jJKJ_UxwRIoL67HZVXN_BMa_dOZcCpP5-X20sZTymaOfI2GcGV9604qq1Wl96YGbS8hYxsDyaI7ojTX3-2BVNt8xRD7G3OiyIHSxDMYpVuZiZ5yyJXwn5Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
خبرنگار: آیا می‌خواهید اسرائیل عملیات نظامی خود را متوقف کند؟
ترامپ: من می‌خواهم اسرائیل بتواند از خود دفاع کند، اما همچنین می‌خواهم از تصمیم درست استفاده کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66366" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj9SYhI3i7VJ6FVGHUJUDOBsPJ7U7lEBJCku3t3Vkt4kbH7usXLOkRCTr6NnVM2p9sotgVzXjcd8x_5FYZF4EI44dm6VuILlbFgAr96I0YqwevDvTvU-fiSTeDj7aB0e52gd7S9L-jrjLbyzLHSKRoV6DJTn9bC9h5EaixqvmyIggxbx2KSpMA0MIIsizdZQ4MENATLhi6vGjCpe2Ox8FN0JovvpvTsU-fIsXMDrwrB19bImNtbM7Bza5rL5OpcorzlB8xZZMsCEn4zKrOjPkrFR6JBd6CxIDc6PD_TWliP6RrCdZq5jxsE4zUdtaJDgYQcqWoq2Qec5J40VG_L8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دولت سوئیس:
بیش از ۲۰۰۰ سرباز امنیت محل امضای توافق ایران و آمریکا را تأمین خواهند کرد و منطقه پرواز ممنوع برای تضمین امنیت اعمال خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/66365" target="_blank">📅 18:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6LHxBpe8Bi29WyyqkvlfKaC02hXsQvAXBvxocC2f5VEBM6LaEmoa89on6HvZ7Go6QXJlsvzQqgc8yVvwLG21U66Y0fnQmKAH6HQ_pO7upATplw6eIbQ6Nro7O7vkqqTrEO1wmXhIDuZmfF3oLQelEG-WoV8osOsHMRWNu1YSUyfYutms8P6y2twdpJZaHFf1Eh8JEka6jRJlu1bMqn7FiGiTXDZvOrPkLex--Zfdo8y8yeGw-TbtGEXbqrwWqGnLXvJA7_dE2l_Yrj6BanbeNG5LWvLl8j2syOs45ziNbPscL5aLQ1FgT8SJS53WgsH4ZCyugUUDNKeQdympUBJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/66364" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JycpPWlTNygP2ZIZgZqsSDKyPugBf1pN0xw2p-Z3WXne-ezz8xqhI6ITgjWq6ZRaVNR_O0oPyp_kMM5VrK4cIi_Ehu3Ev9dXOzVpMuy6p_x_ysWq1pvVIl9SOyN8gpLsvrsqYA19eqWKjQbBziosdeqLoYYRzDT9etb3_Bl-InKK47tZT5fa93GGQHCZEm2xylOt07HMcjiigmjEE8a1tgsJBV_E9gwe_NmWjbdgb4ntIJr2KG8siITdkZ3ZGvAUaWwF_xBpmBOdiOQbqcAXBueW00kwN8kBLcpFdsl4zeBFMv3WbbpTRRjwCfxRGrlC_na1OSYscvpX-f15jhZ4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ در تروث سوشال:
۴۵ دقیقه دیگر از فرانسه یک کنفرانس مطبوعاتی خواهم داشت. سپس برای شام با رهبران فرانسه و دیگر رهبران اروپایی به ورسای می‌روم و امشب به خانه برمی‌گردم! این سفر موفقیت بزرگی بود، اما چیزی که بیشتر مردم می‌خواستند در مورد آن صحبت کنند این واقعیت بود که ایران سلاح هسته‌ای نخواهد داشت و تنگه هرمز فوراً باز خواهد شد! اعداد و ارقام بزرگی در همه دسته‌بندی‌ها برای اقتصاد ایالات متحده با تعداد افراد شاغل بیشتر از هر زمان دیگری در گذشته. بیش از ۱۹.۱ تریلیون دلار در ایالات متحده سرمایه‌گذاری شده است، کارخانه‌ها و هر چیز دیگری در حال وقوع است، اما مهمتر از همه، اعداد و ارقام اخیر بازار سهام به دلیل توافق بسیار بالا هستند و به همین ترتیب، قیمت نفت در حال سقوط است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/66363" target="_blank">📅 18:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a882497b26.mp4?token=jTi5Dcg_KV376eYzw-OaTM8pziN_DDBspo_PHBJCFFYzQadMekJkE2uE3ONTX8-y2qrjMukWlelF1LBb4IyKL4ZwGG5f2hTnbB-QMYqvxtW6eqdzolarJY3SlgawTYPGagVDwK_RW-Kmt3VT3E4nms4-D04V1JYT9X-nBqPkJ_UGym6CnILo2NsTBavZC56ZvmCr-uSkMsGFXyEpPm17j3TMpSsFE2EuxwDHQgFgk00t6QCcuMiV22DawKkgvSQuBi5yXb9-Vts6Eq_56MKo5FGFoVXIyxGmnTrS_OYpVGESai6H1dC7moLjCVqyC-x319LGgkrJpY6RAYeoTihrWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
نه از دوست شانس آوردیم نه از دوژمن
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66362" target="_blank">📅 17:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7f967b0a.mp4?token=Hsx3YVBtI1ZSXmezG9MRu7KyEzx1j171epQcd6BxtH9fyN_rJs6p1YQXTbSRn7wHUR0ZzK73zceTZd1HtcoOPaj6zNkL9H7hG4LlNh5HWvmhVGt3SDyYGDHuZthqrvD1q8vQQSGX6wRTLPU9lWr3WPeIcPGqK5nnVBHaIBJZ0BNN1i9-G0dF2XyadhnaQ2WlkkxxCbg6MFfnrxWtQTD93zSL0EKYsPuz00L1oUKVpipCF0MjaTs5kobe71qonUOls2-RabxAcpV0knNooaXQvsdbbkAy3tY8ZWAfPZlu3hFJOg0410KBsvBdWvsc18ls1pR794Uz7AOYTwmSK8_AUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی: «صرف‌نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود»
شاهزاده با رد مشروعیت هرگونه توافقی که بقای رژیم تروریستی جمهوری اسلامی را تضمین کند، تأکید کردند: «صرف نظر از نتیجه این به اصطلاح مذاکرات، این توافق پایدار نخواهد بود... بقایای این رژیم هرگز در نظر مردم ایران قابل قبول یا مشروع نخواهند بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66361" target="_blank">📅 17:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66359">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e17877e6a5.mp4?token=K-qYkvRhgsjMfPVtJDGMnUfp_VMLWZnVzWEeQUh-cBndx7kahsQXsYXMyaEtlwOrGfZK59TkvXVL9viomOcqCeXJCk7sHAdNDHoOmnH10JCVju_E6jxoAN5FWRZJ_dXpv5g5c5alNx0IqEnE24PXSN88qq0Aqt6BpSSzqHvi1-dXfrEmzyOXpJV7gXwBqrkb80SjcAeez0jH_k_ytwTVTjUbfhh1h_UY56JV2eF2HKlxNkXTWHZ9t7T6jEbZY65IcUChgW4KdjUPO573RTYQzE5lhRUeq2QW9jRf0XdVs5ThNo28D76S5cMBuRXf1r7ZUlyHSLXIew_MxWC9kafEaFMS3jExAOHMJhsvvXY3tM2sOMA26MTfnDSwYr9J5_saFVgA27NjDHXVl88kMCeH9ZUve9pwiPIZB9H34fnW5HkEPRUA9vxYxD_LC9flt80s-4D2v_8ACD2TuiWtjzc_YCi3SBt9BWAxTQI9mphjZJ3iRfvo4zdU2c5iOTlv-8XztecKvt4xXoZo1P2svlIAJyHOgA5xJTX_gr9_5zbgcF01yUIo6TlMvVpJZ4NvjFO4O8hdrzB1woWgZo4ENODGurQr4iHl4Pbt147qWWcfJ5Da4a8I5oMfCz2b9b6949DH4oHml9mgDBl7SLUt7HS0XcJllPAvs4ndfe6bde1lzaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای وایرال شده از ایونت های شبانه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66359" target="_blank">📅 16:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66357">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sl3uSPtskXzNgUsIvsQjgC-J7KgnGN83yiVHewGMfJ6LwPuIJDgo6q5A-vNalccuhMMmXEhHd4SNcb_TSAFeZ83LsCVA4Ff4f__lYfTNTdcNOb9keG5G_L1lezPLXN1FdXNB5Zb8gR1q5su1GrE7Nm8hv5MS2HWD6IV9zt7jg5BBpHEPBI8JercZDV6Nwli2beTIXG4aA4twrYHtlQV0PfVfUQSHHSCwnVu33f36oUj9J1mwWbNks8sWSKo20UjXeMlux7qqTvXY0H_GAGOZJwU9U_m2KEkJRlvOpH0de8xr8wWQPCgKJAU8isJI8P7KL_Tho9G_ThxeltUrOeJTkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/145629d21c.mp4?token=Yvud_BAQjTTMUiiFI_emQbzFd-QjDYSMrLGwiokDnxRpFhKJ5GwjLk7AEm6TTm3JwswcQTv5VJgxWQYS6MxI0dWSM5tp_rWrscLsxxi89OdXagc83_SFalyIQkM3ZNPZ03T02xfWmfy_x6gWb86DrbRAs-SAyuIr-SYOPxrKUoZkfOZ4hQT_cbtdAmI3ci0CdC65YIKyEy-SdOtUPWW9voRac0x7QpyHfFUz2HRiVqKi5_-VRkHOCbTida4C753ZCWUg7BdAwp50Gk-IOUwba3jDqeTuU30GHFMGZAvUfwKSrGjmdbgPSqTlFfJIdAmGDWhEuvRK74FJeYFOZaHGoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جنگنده‌های اسرائیلی مناطقی در نزدیکی کفر تبنیت در جنوب لبنان را هدف قرار دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66357" target="_blank">📅 15:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66356">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2f9733be.mp4?token=nA_pUY5seoJ7GHFJFcjpUjGgd16hqiKcPZMMU_AbDSPEL1eYL5SR2Lc3yHKXcwgJ1O4zQEHhx0GfYPPFw8ygf4aLeDAXCUS2x4qOy8ZKL26njVn4pR_Fqn03S9Mn989tXirWaSprZSrXg_TWp4gTLS3aGVHcEnIQ0wB79A-ejLBDQYykr-SrlHrkGPPpV-vdegI7UPaCNwAi83IudeYRfesIL9zjdDO8ZGhyU_kmTGpjqliieG3funN5iDs2lX8sTy2urUcueTkh7tWkXR0NaHsg1Arw-I1cTVB8o61oc_t4FBEHBSWZRF4MIWh7iwK1lN11SyYOCmVDfZ0n6Yitcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
فراموش نکنید، هیچ‌کس تا این حد در مورد ایران سخت‌گیر نبوده است.
این کار باید توسط کلینتون و باراک حسین اوباما انجام می‌شد. این کار باید توسط بایدن، بوش و بسیاری دیگر از افراد انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66356" target="_blank">📅 15:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66355">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/048f0eb68f.mp4?token=Rhmu5f7-tCnpzu-izB787TijPfxYyoinkdB50ioRG6gEPE7vrOgYHrYBpARg2S6W8xrmg3UwpVi9svvj5SCbFynLlOBwYxt7UppjXK_HCe5PwlAdKd7wmw_7LvW-Mc4TvjtVnMw7RupT4LktbObWO5Aj_jwI0Bl6yQJM5fKpzTshT2C9EEv37TnxMTIwP80Zm-SNvGA_U4Bu3DZC49kfJqy3aHWpptqiX4cnff-KQ3_ttt1MkHFfJASmut0G2LFvMY_2Tdord0e8WgfxNxpHleS58W7Lv59ZsyDQC5cUbQjV6d1_zln3mK6Y-W-P8LbhyUrhO7i_aXYveEb_OFT2jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: نیروی دریایی آمریکا هر شب بین ۱۵ تا ۲۵ کشتی را متوقف می‌کرد
دلیل پایین ماندن قیمت نفت این است که ما هر شب کشتی‌هایی را که شما حتی از آن‌ها خبر نداشتید، خارج میکردیم. دو روز پیش، سه روز پیش و حتی یک ماه پیش، ما ۲۲ کشتی را خارج کردیم. به طور متوسط هر شب بین ۱۵ تا ۲۵ کشتی داشتیم و هیچ‌کس از این موضوع خبر نداشت. نیروی دریایی ما کار بزرگی انجام داد و به همین دلیل قیمت نفت به ۳۰۰ دلار در هر بشکه نرسید. قیمت‌ها به ۱۲۵ تا ۱۵۰ دلار رسید و اکنون حدود ۷۲ تا ۷۳ دلار است و حتی شنیده‌ام از این هم پایین‌تر آمده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66355" target="_blank">📅 14:57 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66354">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7384906c.mp4?token=CMLyp7-i9p8NUczICg6FC5RZk183dVsF5zcgxeoWDUsbeVoyKIjyWZH_Rq0X82tTsJjU2ufjakbsrgkpta5NaSfjdZoHXvOm_weeF2jdG02WSOpvgE-LQ_-nicRP8qbjjN895qZ3WlNFug1g2DpT5Rmk85kGuyyDVltyud2ihFKlPtiadzf1qw9HZccCsaU7aHioC9wjLeNZoHMqBqd-bDkvTygG0wAVi6r4VodfkEoPM5cOwL9GMNGOmzJ8fFD20IKaVMP7uRdlXAM-7dAFNUHwi_p25dBHMuQl0z9toUyqIHtJS0cg3gqhA3VqmbrnfDeqiJgGQ9Th5b8d0IUBbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: «می‌دانید ایرانی‌ها چه کار کردند؟ آن‌ها به اوباما خندیدند و به او گفتند احمقِ مادرجنده.»
پرزیدنت ترامپ با اشاره به نحوه برخورد رژیم جمهوری اسلامی با دولت باراک اوباما، گفت که مقامات این رژیم به اوباما خندیدند و او را «احمقِ مادرجنده» خطاب کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66354" target="_blank">📅 14:50 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66353">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=fe7Ok-Mh9ca0eagoJWiHukJx5plMR1BMaAcftsJ7k7-VAI7SV4GVc6sbddCF6RX8Vjc1o8Foq_WGoGXheMB0kiu2HFj28LvhgTeZObcZR1Z3VMIksjP5_7qoJGHXSxzQUFmI84h2qGAD79u3CDf03K13xUseqT5AXc8x_bggmUXiMTtluGDaEA3ENRhtfiLnbhHRcQjTtCUDopDAJCD9i7vLSHNpVLrUlbLwq_88IjSZNJXrqTa38AXVRsVOnLaJcNwxyvg7gsaWFv_A30jRPybZPq0eV1o_qqmZQ2uW2d5sQbc45gvVvvXr8PFMcFMEBXnHC8yiSz8eb1JfwJGQfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bba81d7fe.mp4?token=fe7Ok-Mh9ca0eagoJWiHukJx5plMR1BMaAcftsJ7k7-VAI7SV4GVc6sbddCF6RX8Vjc1o8Foq_WGoGXheMB0kiu2HFj28LvhgTeZObcZR1Z3VMIksjP5_7qoJGHXSxzQUFmI84h2qGAD79u3CDf03K13xUseqT5AXc8x_bggmUXiMTtluGDaEA3ENRhtfiLnbhHRcQjTtCUDopDAJCD9i7vLSHNpVLrUlbLwq_88IjSZNJXrqTa38AXVRsVOnLaJcNwxyvg7gsaWFv_A30jRPybZPq0eV1o_qqmZQ2uW2d5sQbc45gvVvvXr8PFMcFMEBXnHC8yiSz8eb1JfwJGQfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ما مردی به نام سلیمانی را از بین بردیم. فکر می‌کنید اگر او زنده بود، این اتفاق می‌افتاد؟او یک نابغه شیطانی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/66353" target="_blank">📅 14:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66352">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff72e5160c.mp4?token=X51tyiab_TZM2rs1wL5dYeTE4oaBg8Zhq4oeClmWzUJToIVMRgp7T4l2_EEreDXhv_OTAWgD-QfFKmasbYHaaI2VyGS10a2_Qgw1vYunqMrbyLdzf30NK91A8TcxgzSNnY8P6_9SHqiBV46U2JIbyTu7Q1ArncMbNDiH5gMIIjfj_a22ThG7I1ZSg2MpS10biYF1o37mfgNNrdNBUqJP4kCd4YHf73A-9t3LiudN86tL1jDUenBRNig0d6s8rv0jb7FyIOi1z16qL54GrJnycz_NtiS1TrzcspDZ5e6AuzDQLfd_lSRfB0wbqLa-FKhXxEwAmTFZSXkvJ_-fX7Yfxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ: بازار از توافق با رژیم جمهوری اسلامی خوشحال است
«چه کسی واقعاً خوشحال است؟ بازار... بازار در حال نوسان است و قیمت نفت سقوط کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/66352" target="_blank">📅 14:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66351">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=JlTWPlajRRAXD1LSGLzjstHOOUP3xZufUP17ymL7WFEkaXPZfQLmMxNGQGyMxjNdrEUjDmq3XV1f0xCE-FTNzktydv6IQDiTuJGfdbKP6m2W94Nl3Mw8rC04fnts7e4aEHJIdJcegU12vIbDmNyaTOfE1nrPW9WUgxcFxVNssjDI9948WZ1jNiTw2HA5J4yaFumPV-EadxwJYFFz1CvoL51SbqW491il6AR94xSeeCURs_MsYDIIz65rnbeg_rBtmNEoUjcVRCR12xL7cntCaLfs7Tgz_qnkDiunq7YvnJkQPeQW_n1kYLr7bdZTzGh1OJMPggvnrntPqYHs022Ptg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a231223e.mp4?token=JlTWPlajRRAXD1LSGLzjstHOOUP3xZufUP17ymL7WFEkaXPZfQLmMxNGQGyMxjNdrEUjDmq3XV1f0xCE-FTNzktydv6IQDiTuJGfdbKP6m2W94Nl3Mw8rC04fnts7e4aEHJIdJcegU12vIbDmNyaTOfE1nrPW9WUgxcFxVNssjDI9948WZ1jNiTw2HA5J4yaFumPV-EadxwJYFFz1CvoL51SbqW491il6AR94xSeeCURs_MsYDIIz65rnbeg_rBtmNEoUjcVRCR12xL7cntCaLfs7Tgz_qnkDiunq7YvnJkQPeQW_n1kYLr7bdZTzGh1OJMPggvnrntPqYHs022Ptg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:متن نهایی نیست؛ این یک یادداشت تفاهم است.
اگر من آن را دوست نداشته باشم، ما به پرتاب بمب روی سرشان برمی‌گردیم.اگر آنها رفتار مناسبی نداشته باشند، ما دوباره به پرتاب بمب برمی‌گردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66351" target="_blank">📅 14:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66350">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653e74d56.mp4?token=Yg2382s4D_ieH7UGaHFtKN4AbhuGbzLK8rPE-1FBMd6VKY8pcXuHws87sN_EhsTvL_Hyr2aLCnLMXWCBd8PRhbIbFiwOgTJuV89FKnUGJu39Gm-6s1tDJHhUhG1TgyWGEa4BbP_ChmzIkrJYTKggLPcbeFrWw5YZu62fV2fLuj0PibKD5BDj_VHVmqu8XkvS6oqr1_RJWkK6nwk2ATwXS5eE-i8pi2KACoN6ZlrKk9nGsJFBzeYeN5PfP4Z4DhEZbXlchYVuwwNVeBPa1j2YUMB_k0nxTE7gcrsCl9EhU0piKW9Xme6wVW0gy9qL5z8iZVBKe4Ae2nusExlThbsZPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد توافق ایران:
هیچ‌کس نمی‌داند این چیست، اما توافق بسیار قوی‌ای است.
به نظر می‌رسد اکثر مردم بسیار خوشحال هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66350" target="_blank">📅 14:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66349">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=hy0_k7qtnv0sTjTE0LgaxoDkGIqC7jrQGALazpKpDGhziU9JqKnS-TKaxgfooDhbz57q5If50Nt0NOxlwJZ9gLhNtiXc39GOo7NApRd7jfqQ-ySdbPl9WGiw0Q5PSrzMVBiA4nn6SHrgT8ch8vLSt44F2-lgEQo-yx2d-kw_dRiFd0GRrwYWdMnZgDaJ8xOVjtuAAuVWZJcMA7a90LeV27qs2awgluUXhK6VHnWUTXlU68RvzXaI1r2Zxxg83v3EDimUK11YV8MctltYFsNiH7ASQjlMGbXRZrJkfD4m5gk8sMfx4gpS4Sdp-IE_6keSLwj6r51lFvM7waOzZaYATg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8de3b6155.mp4?token=hy0_k7qtnv0sTjTE0LgaxoDkGIqC7jrQGALazpKpDGhziU9JqKnS-TKaxgfooDhbz57q5If50Nt0NOxlwJZ9gLhNtiXc39GOo7NApRd7jfqQ-ySdbPl9WGiw0Q5PSrzMVBiA4nn6SHrgT8ch8vLSt44F2-lgEQo-yx2d-kw_dRiFd0GRrwYWdMnZgDaJ8xOVjtuAAuVWZJcMA7a90LeV27qs2awgluUXhK6VHnWUTXlU68RvzXaI1r2Zxxg83v3EDimUK11YV8MctltYFsNiH7ASQjlMGbXRZrJkfD4m5gk8sMfx4gpS4Sdp-IE_6keSLwj6r51lFvM7waOzZaYATg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یسرائیل کاتز: هر کسی علیه اسرائیل اقدام کند، بهای سنگینی خواهد پرداخت
🔴
وزیر جنگ اسرائیل هشدار داد: «هر کسی که علیه دولت اسرائیل انگشت و دست بلند کند، چه در غزه، چه در لبنان، چه در سوریه و یا هر نقطه دیگری، می‌داند که باید بهای آن را بپردازد. اول از همه، آنها زمین خود را از دست می‌دهند و خانه‌های خود را از دست می‌دهند.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/66349" target="_blank">📅 14:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66348">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/831548d977.mp4?token=GqRAw5eUyNdCUL1LHWS3gSk4XFS2LWpiHykAES30MQ8Vqo7YAOfv0KmuwKbRDYqQfwB603MAFLhTG8OAj1td5FBA1SpxKVigJUxqb_4OZU9YVxq0f-7-YRaeja-IugrAnedchFgRAZ06euNWyJIjF-enghsLo2TRGh1K0YGgQ8DOVMotEGKt2N3gs2ucM9XQcqG8kpV138iqvpHYsL7Zd0ox2M7XmkOBVGzSRHRGznndcYFIf8RhGaR9SczlXwuUR4cis7GRMAFthEvD5rlhyM3LVv7TbqTqXHMJLR5mUJHICP6aT1JbSoUOv57Jbz-IX2g-DEyJqzN8jR2aa94JEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیس و دیسبک بازی مسعود با خودش
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/66348" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66347">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=T2tnRbtGnb9wAS4asFqaNQw9fOiUPA6ppGB8F5q0oYuElL5jM069sZ1jqY7bTN1vw3ho5M1ss3DwxGUOHD8567O4inj9AB5GOp7gKFSwp9zVjPuqtkHzWlZ9OL9QDno06UYtwxA0_DttCWTzldbHrqwflup-GEP9DFLWwXfXj95pMhQgZ6TyAgf2kKl7NEdl0bE23KxP6Y5ik5kAE-O54tvvMq5DK71sdt36mz8gn6MBX-w5DgOXfEBou32Fv-rctyehg7nVfAg6k-tdsF5V9nNHcD6z_66mNTbOXAxMyNWIglhHNMm-puDqz6m4yPX2fmjoO64Br1wY8IryJOnmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51823a43bc.mp4?token=T2tnRbtGnb9wAS4asFqaNQw9fOiUPA6ppGB8F5q0oYuElL5jM069sZ1jqY7bTN1vw3ho5M1ss3DwxGUOHD8567O4inj9AB5GOp7gKFSwp9zVjPuqtkHzWlZ9OL9QDno06UYtwxA0_DttCWTzldbHrqwflup-GEP9DFLWwXfXj95pMhQgZ6TyAgf2kKl7NEdl0bE23KxP6Y5ik5kAE-O54tvvMq5DK71sdt36mz8gn6MBX-w5DgOXfEBou32Fv-rctyehg7nVfAg6k-tdsF5V9nNHcD6z_66mNTbOXAxMyNWIglhHNMm-puDqz6m4yPX2fmjoO64Br1wY8IryJOnmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاوره اخذ مدارک دانشگاه آزاد
واحدهای معتبر تهران
کارشناسی، کارشناسی ارشد، دکترا
با استعلام
💥
(
بدون پیش پرداخت
)
💥
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
👇
Telegram :
👇
👇
👇
👇
@irantahsilat_iau
Instagram :
👇
👇
👇
👇
Https://instagram.com/uni.irantahsilat
جهت ارتباط با ادمین
👇
:
@madrakuni</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66347" target="_blank">📅 13:45 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1725e10790.mp4?token=mbiFLrvKoGNrXzpCnZZv7sQnu2GLOhIqQrNxbqciuOm6efV1FT5YkclzPv7_OTzTf-UPkcrkfNnBV1NPze0sRqd96kFBcSzCAxcH05xp_0Z25BDNk7UkwNYC1uepgxn11P9D3C06t8CqZ8VOtDQqe6S05kxSJXgoId794E6CPJ8vjFuYA9tAaQ5DA1fMOXN08dGqJGzL_3sVQcnkUrNPd4oSY-KcapiCbDG880n5Mbq_jTdkCkkD3sSGJmKDsiKkAEsYe2t71Iypc-FWsSm2Ae8dKRnBWiHBAT5veCKdVCz8We9zaLEMH1x_Sr-6AzKHmhBrbcOCG8C114kNgT9AjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1725e10790.mp4?token=mbiFLrvKoGNrXzpCnZZv7sQnu2GLOhIqQrNxbqciuOm6efV1FT5YkclzPv7_OTzTf-UPkcrkfNnBV1NPze0sRqd96kFBcSzCAxcH05xp_0Z25BDNk7UkwNYC1uepgxn11P9D3C06t8CqZ8VOtDQqe6S05kxSJXgoId794E6CPJ8vjFuYA9tAaQ5DA1fMOXN08dGqJGzL_3sVQcnkUrNPd4oSY-KcapiCbDG880n5Mbq_jTdkCkkD3sSGJmKDsiKkAEsYe2t71Iypc-FWsSm2Ae8dKRnBWiHBAT5veCKdVCz8We9zaLEMH1x_Sr-6AzKHmhBrbcOCG8C114kNgT9AjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
بالگرد کاموف ۵۲ روسیه برای رهگیری پهپاد انتحاری اوکراین بر فراز مسکو به پرواز درآمد:
در جریان موج حملات پهپادی صبح امروز اوکراین به سمت مسکو، یک بالگرد تهاجمی کاموف ۵۲ روسیه تلاش کرد یک پهپاد انتحاری اوکراینی را در آسمان رهگیری و منهدم کند. این تصاویر بار دیگر نشان می‌دهد که جنگ پهپادها تا قلب پایتخت روسیه کشیده شده و مسکو بیش از گذشته برای مقابله با تهدیدهای هوایی به ابزارهای غیرمتعارف و واحدهای هوانیروز متکی شده است. حملات پهپادی اوکراین در ماه‌های اخیر به زیرساخت‌ها و مناطق اطراف مسکو شدت گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66346" target="_blank">📅 13:36 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LmibpWQr3G83fwf5_okYzi57nkdXuGoyBs88c322TPWh3VPSMVUn76-wLm9RIOWli0R2_f_m1APUbQk4vKeJr2A5Abx4B3lN71yxFmp8TAY2cbh9LOEGzpPeLPYXHT9m5AMz8OBnM2uSVlOTj17Z-yzj9xNJHlnWtcykAr7RNrCb7YMDsUu56vW0OehizNlGKHQ490BXNlLIoxUB_PFOD8mxNYh48rJpoM9nFOhC615vd7yEQWz1Xpu_OhRzFNWAGhOdsU7uZvFvFO4jlmMld9sjZ2YcpIj9F5y5myUfq1kQ1S9pbsREMT86Zc_zw4S-xEwe726nZC5lAnMeIEsfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت مارکو روبیو بعد از شنیدن خبر توافق
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/66345" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66344" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66344" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/puEhE-MVSWiPLAsoi7a6Qmru5jUrIJXQmJ4FjucSiIhS3pMxKlip0qQ6MUkmVN834S5aklnqmznjkF2V9rqUklh78TNJ8gF4VM5Fz2nvKuTNHyrcwW4GVai7sWnKVeQfK00GAKno4fAquJfoYBPL0HESnYWveBcyOvih71ly4fYG9WhTzKQezJjHwbtW6eZ4DDIzuEfZy41ahrUAblvXciPg_aTgnqZFlva7wNmBKENtwkV6nY-iDWer0hMbJ5qXVh7l29DQSPkYkaF4JFsQvcVYoGzCjBTEaSsjlBEqcj0lejOk1OYYIeOK4jYW3C79bYT16mUE5XrZdRRaJf_QRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پروموشن ویژه جام جهانی 2026 آغاز شد!
🎮
World Flight 26 یکی از بزرگ‌ترین کمپین‌های 1xGames در طول جام جهانی
🔥
برخی از جوایز اصلی:
📱
iPhone 17 Pro Max
💻
MacBook Pro M5 Max
📱
Samsung Galaxy S26 Ultra
🎮
PlayStation 5 Pro
🎁
و هزاران جایزه و امتیاز بونوسی دیگر
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66343" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5hoF35iOmMKQBOWN7QLzd_220VOVCJp0aT155lp9Ey-bYjMX_vCL1yUQS0TePAEP24CUJLApFQBjfNW1q1lpxNc34bB7O8mDitTasY5jmWZmYN4BH5JQAg93ZrCxneciuNLCeikPJecB4JRgbg2DAiUN0GE3_-n0IftKeFsjEYpazcXJPWwmT8k48vUAe1qc30aFl70RreP1mjxKsyEsHmk8JFCQCD0aJcdNO9KVtRbriH09FONf8Wi0CpXo6MWoIwAsVvdJt61AFeretLUuV3mlw69YAUXzJ2npmHp3lLf0nrN7JpThpss8vIn4PIHdBp91m8nH4yBrfGyk7q9qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
شبکه ان‌بی‌سی به نقل از یک مقام آمریکایی:
رژیم تروریستی جمهوری اسلامی با وجود اعلام یادداشت تفاهم با ایالات متحده، همچنان تعداد زیادی پهپاد به سمت شناورهای تجاری در تنگه هرمز پرتاب کرده است. بر اساس این گزارش، سپاه پاسداران از زمان امضای الکترونیکی این تفاهم‌نامه در روز یکشنبه، هر شب اقدام به پرتاب پهپاد کرده اما نیروهای آمریکایی موفق شده‌اند آن‌ها را پیش از تبدیل شدن به تهدیدی برای کشتی‌های تجاری، شناورهای نظامی و خدمه حاضر در منطقه رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66342" target="_blank">📅 12:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf0t6ZcOL7MI_-14AIoFDuwFRKti1TJdBGRB0NQe_dsux9h67nVvED004Vss--xXneGxvpgygIoGuu2Yd9g7acZ9q3Vqb1D2_wSoqUi4YUptpnzxF8fTMU41jj7m4ODVmXjsyKZ3eKoz7grir0_cj8NhTM8TEwKJPC6h_dRVrkTKvpg9Fu95d9nvg4qeTbJGatSooCsHH-JrJvQrK12cH8pZpWjtTe5QIqvdzr9gDOO5IXgOElRiyvdw7wxeX9CUJXMp73fBC4XCBFDghDxLkUCvMbKeU2atHNDuiVfUdbsPlQHgFNE9lwK4Vdg3b8WaJj9EZODk1nZF2VNPK1cMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تغییر چهره پسر ترامپ طی یکسال
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/66341" target="_blank">📅 12:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=JEQ-vVLXovd8gU4PVMjNfJcVMPxaLoZ65EH4XMGyUdHXxaFWuCekoWDf8YZNMy41VxSbHBEiFgnwwPWiagzT8YBsNDJIxkr3ukIugyR_AYOWCvpMUYwvvVkCCAb4KGR0N2hvRQyJ9BfjoNqwv4Q_gFtocI8apycfNABASumq4SM-cT7cqQiss3QNVrchKLkLRYgd8jVdygh22xRojW2iuDyEFgVFL1khBPg42sMAAAad0038cjDmkFkPCYSpt1zGuv-BTHcZIQQelkwFSiDaCd16B2pee9di17EyubIAbK9VZU5TGzYhpE3DJZFHvcwfiygPwff5Cf0FwgBlUEjBpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d976a7f361.mp4?token=JEQ-vVLXovd8gU4PVMjNfJcVMPxaLoZ65EH4XMGyUdHXxaFWuCekoWDf8YZNMy41VxSbHBEiFgnwwPWiagzT8YBsNDJIxkr3ukIugyR_AYOWCvpMUYwvvVkCCAb4KGR0N2hvRQyJ9BfjoNqwv4Q_gFtocI8apycfNABASumq4SM-cT7cqQiss3QNVrchKLkLRYgd8jVdygh22xRojW2iuDyEFgVFL1khBPg42sMAAAad0038cjDmkFkPCYSpt1zGuv-BTHcZIQQelkwFSiDaCd16B2pee9di17EyubIAbK9VZU5TGzYhpE3DJZFHvcwfiygPwff5Cf0FwgBlUEjBpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تداوم حملات ارتش اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66340" target="_blank">📅 11:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=Og5vg2rX1jYrhCiN4e1JUxng3YdRVU7Rdp8ronljbae0AJDgRGU-tLfB3M0EfP07R-YEKRKNPY7nYCvMuRHXYwI6VVB5MasSdkDjlPAHlo-MspwxbxUfEYQWVcbmgRvseR_CeHmojK0PrMnnIMxuad6IcYqRQCI336oc1a6PdLw9GCWcS0XumK3-TrTQMHAun7mfTBxIKXk1lSjvpc5RuhFETrtWLVXde9PGESjQUhbT6y9U3T7d43s2ajd7wiG9sIyiEFpSnCtumzXmvKkHMy4z7yNs2bgvAiQJzAKBQ0gQcGUIDel6mf9G5mPAoQs4zASkQtTEfL7lmjrrB1DdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac69a7be8e.mp4?token=Og5vg2rX1jYrhCiN4e1JUxng3YdRVU7Rdp8ronljbae0AJDgRGU-tLfB3M0EfP07R-YEKRKNPY7nYCvMuRHXYwI6VVB5MasSdkDjlPAHlo-MspwxbxUfEYQWVcbmgRvseR_CeHmojK0PrMnnIMxuad6IcYqRQCI336oc1a6PdLw9GCWcS0XumK3-TrTQMHAun7mfTBxIKXk1lSjvpc5RuhFETrtWLVXde9PGESjQUhbT6y9U3T7d43s2ajd7wiG9sIyiEFpSnCtumzXmvKkHMy4z7yNs2bgvAiQJzAKBQ0gQcGUIDel6mf9G5mPAoQs4zASkQtTEfL7lmjrrB1DdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
مایک پنس، معاون سابق ترامپ:
به جای توافق، باید اجازه داد نیروهای آمریکایی کار را یکسره کنند، تنگه هرمز را باز کنند، توان نظامی تهاجمی رژیم ایران را از بین ببرند و به مردم ایران یک فرصت واقعی برای آزادی بدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66339" target="_blank">📅 11:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=k8iNzULD4gB_Z_21N2h6CRGSQLFjyabPom-G_tkx0IgusNmt8c2MxjwUxNJet5mOxzRtrH4eA2jJX_Q6WU-3MB_Z_L5AK3Ad8ZtzKDCqRaOavpf13TxjgcQynLRbkECO8brMpxvHyHV18sW8eNgjT5CVH3ZtbPr8453XdLmuwVP1jTT0EC25Rbj7vIGjns25_5qNG8PwGakuP0CKi29loSiz2KsMc3U1bh6mMbO_hmfJFbAV5GPu8huqoRsWegyWC3XvBlw9EI9zVhZjv1w-G9eACqZqryOwOoUFGMQsaJzLT397-BS-udguRIWGLBln8hOmcUh90HqgxfsrhBcD7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82ba759cb9.mp4?token=k8iNzULD4gB_Z_21N2h6CRGSQLFjyabPom-G_tkx0IgusNmt8c2MxjwUxNJet5mOxzRtrH4eA2jJX_Q6WU-3MB_Z_L5AK3Ad8ZtzKDCqRaOavpf13TxjgcQynLRbkECO8brMpxvHyHV18sW8eNgjT5CVH3ZtbPr8453XdLmuwVP1jTT0EC25Rbj7vIGjns25_5qNG8PwGakuP0CKi29loSiz2KsMc3U1bh6mMbO_hmfJFbAV5GPu8huqoRsWegyWC3XvBlw9EI9zVhZjv1w-G9eACqZqryOwOoUFGMQsaJzLT397-BS-udguRIWGLBln8hOmcUh90HqgxfsrhBcD7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسایی نماینده مجلس:
اگه کسی ذره ای عقل داشته باشه به جانشین شدن فرزند رهبری میخنده.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66338" target="_blank">📅 10:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLfmSBLvNATsl0LFV2bVGMbivLQCGvuZKEQ8RJ2cnOQvpGDsWqb6kAE8NIXepaeOI235MUd_D-kSRWzjtSJBQRjd957_ynfSyDde1UyfScFLwvQBVzm6hMC8wRXodGyXzpiPGK8oxIVluFyzhKhTX_Oc2KoN1RsMvTkJCeW_uJq3wTO9HQA4gilMZN9GPnXLW4BtZrK1IsFCpi4p7TVveUC1KHjvgpg1pQMaNb43ka6zrHDc-bVzq0V2cR4DP1lF8tE-D6FE1ADbQFs9vYE1T3AZoIf14Cfwg9LtLDHAZHu9UWeL2uH1SPyrVvdzrxFPWzmFxUM3hy7eGTbzTtmncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
مجلس سنای آمریکا طرح محدود شدن اختیارات ترامپ در جنگ با ایران را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66337" target="_blank">📅 10:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=Rzq54CEgP61T0zq0sbE0Rf-fUqM42iqquA-fxI46ou_ksyME546_bxieHUh3bZtE4QxpeWRd4wwtyLJmXSGITSpCJ2tRSmUzShfi_81SHbq6jk3Q9ZxSMISbpKnB7K80mV9hIxz1idaASPkb_4asTOjfTlBut-kb1Xh6BoEUFeNhybGEfPOXXzo0_4lh4H3313LnNFatvRZ6XNNwV6OfLfEcpA5Ku9kDf57X4PmdFaQjVd9XLqPVpD5M0KOQt1xCXiw-bfCqqT-aBr_7JQKg07NafJi75OWM4zz2W4Mk5vKF0p1JvBJCoL4c7Tmxy__xI3l8gq16IA3WPB4AQO83HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d9bfbe9c.mp4?token=Rzq54CEgP61T0zq0sbE0Rf-fUqM42iqquA-fxI46ou_ksyME546_bxieHUh3bZtE4QxpeWRd4wwtyLJmXSGITSpCJ2tRSmUzShfi_81SHbq6jk3Q9ZxSMISbpKnB7K80mV9hIxz1idaASPkb_4asTOjfTlBut-kb1Xh6BoEUFeNhybGEfPOXXzo0_4lh4H3313LnNFatvRZ6XNNwV6OfLfEcpA5Ku9kDf57X4PmdFaQjVd9XLqPVpD5M0KOQt1xCXiw-bfCqqT-aBr_7JQKg07NafJi75OWM4zz2W4Mk5vKF0p1JvBJCoL4c7Tmxy__xI3l8gq16IA3WPB4AQO83HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی دی ونس درباره ایران:
اگر دونالد ترامپ به عنوان رهبر ایران انتخاب می‌شد، دموکرات‌ها همچنان می‌گفتند که ایالات متحده باخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66336" target="_blank">📅 09:34 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/555366529c.mp4?token=gSMMYkSye3VXiccd2tCRNy9gQzIiHS91zYyVTp0CcV34XKwcaOtOef1QkJouj-hg6FkzaUUgiBMDovROmLsV06GUzJOwOe8OhYFh9FnIO_fNx40LdDeo9PcVe2-z1a-nPGRNtztYFmCFsVwNuvjIhTT4A805Kxin6614hrjsIcrRfOZn2pDN_AnBbKSdVy5D1h8SFQq3wQLqXsFQXA8yEKFmuXT7aS-dX5Vb6Kf4yubVXV3bXNSAD2jmVwYT0bf55CY5Hhc7ndgPkjz_mm-VISmV0UJITkIdKBbKxESoPE3fjXpQgPHT3TN0ZD94CLLyXis5mR53U1LHxUXhY4KNVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/555366529c.mp4?token=gSMMYkSye3VXiccd2tCRNy9gQzIiHS91zYyVTp0CcV34XKwcaOtOef1QkJouj-hg6FkzaUUgiBMDovROmLsV06GUzJOwOe8OhYFh9FnIO_fNx40LdDeo9PcVe2-z1a-nPGRNtztYFmCFsVwNuvjIhTT4A805Kxin6614hrjsIcrRfOZn2pDN_AnBbKSdVy5D1h8SFQq3wQLqXsFQXA8yEKFmuXT7aS-dX5Vb6Kf4yubVXV3bXNSAD2jmVwYT0bf55CY5Hhc7ndgPkjz_mm-VISmV0UJITkIdKBbKxESoPE3fjXpQgPHT3TN0ZD94CLLyXis5mR53U1LHxUXhY4KNVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وقتی نماینده میخواد ثابت کنه زندگی ساده ای داره و اونجور که همه فکر میکنن نیست
😂
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66335" target="_blank">📅 09:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66334" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WGqyVnISGWV8xDyeV2tZWCJHft7EYDZ3JmCBZmGkTZ22CdWz7lw1YXdJ-Jbawu6THHXZCdjtK3aZyIH5EYWolZby8wKvoAk6B4OXJPx798Eo3NQHRa_nSr2SKoInjDV4p-2bcwCfgte121Hi2_mTdNC3tdv7drbO02bUPiFVsQNbssh0Guj452Pt1Or7WnOWjBhV7N_nCD8jNJ2t0fQM67t-_p4_16H-rxcQV7dM1a8J_FIZJzAfyNomLi0sHvy76EefrElf3je9i5Gw4m0LiEXWe-m8oXlRqNlcNjmaVBk2KwIJ9l6NSayt-gMX7h-1EMbqU4RRZO43t8ZD_3WCXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66333" target="_blank">📅 01:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66331">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
به ادعای باراک راوید مفاد توافق ایران و آمریکا به شکل زیر است:
ایران، ایالات متحده و متحدانشان خصومت‌ها را متوقف خواهند کرد، از جمله در لبنان.
ایران تعهد خود را به عدم توسعه یا دستیابی به سلاح‌های هسته‌ای مجدداً تأکید می‌کند
ایالات متحده و ایران متعهد می‌شوند مسئله دفع ذخایر اورانیوم غنی‌شده ایران را حل کنند.
ایالات متحده و ایران درباره غنی‌سازی اورانیوم و نیازهای انرژی هسته‌ای غیرنظامی ایران گفتگو خواهند کرد.
ایران وضعیت موجود برنامه هسته‌ای خود را در طول مدت مذاکرات حفظ خواهد کرد.
ایالات متحده محاصره دریایی را برمی‌دارد، از تحمیل تحریم‌های جدید خودداری می‌کند و در طول مذاکرات حضور نظامی خود در منطقه را افزایش نخواهد داد.
ایران ترتیبات لازم را برای تضمین عبور ایمن کشتی‌های تجاری از تنگه هرمز، بدون هزینه، به مدت ۶۰ روز فراهم خواهد کرد.
ایالات متحده متعهد می‌شود دارایی‌های منجمد شده ایران را پس از اجرای تفاهم‌نامه در دسترس قرار دهد.
اگر توافق نهایی حاصل شود، ایالات متحده نیروهای خود را ظرف ۳۰ روز خارج کرده و تمام تحریم‌ها علیه ایران را لغو خواهد کرد
.
هر توافق نهایی شامل برنامه‌ای برای ایجاد صندوق ۳۰۰ میلیارد دلاری برای بازسازی ایران خواهد بود
ایالات متحده به ایران معافیت‌های موقتی تحریمی برای اجازه فروش نفت در دوره مذاکرات اعطا خواهد کرد
مذاکرات بین ایران و عمان با مشارکت کشورهای خلیج فارس برگزار خواهد شد تا ترتیبات مربوط به حمل و نقل و خدمات دریایی تعیین شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66331" target="_blank">📅 00:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66330">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9122af9759.mp4?token=kl3IGyeUVhj4PCRl1MoobpWIKrgJ_-A3iXzJdMVWskZWjsOPj_avnCnVkUjHZgB64tPVF1A5WT_it_I3vbPA0AJ4Ec1Mtj6mAvx_ckCri2J1F6WPsGjlINBfKLlzn5Y4fcqbm5M9KYaFKykbvg7H6iZ2rZpRJbNTel16lzcEnnlsoGY_94Z3b3Nq9y2wUJEJNBZHQfKhg6PBybgwXvEt4GONnNx9ZV-hbPyb4F5uHSpnL_uoZrFqDL_VwCFT0eQkyqCQTystPzKZjMN2FpP949B3JsLui6GdrNV-Lq_kn4idrcxLpy2QYtJlqwesV2qEbri8qswXjjXiviG-VN-68R6ILtxbVqAhnFyhtmpOfhNE_zQoqKqpL130TSAAod7xAO4JPaaG2fLF34Bl1mEAHwoQvdGBDijbJ558PKZruSis8vRjGzHbyYFK-AQLm4rCwLXRN_Hy262YFPyQS6TFWV93TO_oHYSjV5tqHm-ePuvp0xzeXT49KEwxx1B1UeY0YvB5Ro7HaRcITbGTRphKeD5iYN-DMqb85K9AfrOD8OJ8Z4CbwluIKdZRWikOqbT7NHi0o9swLut5TZto6chazFfIFeYFI6uxRdkXf89iG_ybJwncJijitJM3Sp0N6RxCVJbBjEKa2vtBQnBNuK2eOcNPkKBneRTsfj5PPKTi5yI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9122af9759.mp4?token=kl3IGyeUVhj4PCRl1MoobpWIKrgJ_-A3iXzJdMVWskZWjsOPj_avnCnVkUjHZgB64tPVF1A5WT_it_I3vbPA0AJ4Ec1Mtj6mAvx_ckCri2J1F6WPsGjlINBfKLlzn5Y4fcqbm5M9KYaFKykbvg7H6iZ2rZpRJbNTel16lzcEnnlsoGY_94Z3b3Nq9y2wUJEJNBZHQfKhg6PBybgwXvEt4GONnNx9ZV-hbPyb4F5uHSpnL_uoZrFqDL_VwCFT0eQkyqCQTystPzKZjMN2FpP949B3JsLui6GdrNV-Lq_kn4idrcxLpy2QYtJlqwesV2qEbri8qswXjjXiviG-VN-68R6ILtxbVqAhnFyhtmpOfhNE_zQoqKqpL130TSAAod7xAO4JPaaG2fLF34Bl1mEAHwoQvdGBDijbJ558PKZruSis8vRjGzHbyYFK-AQLm4rCwLXRN_Hy262YFPyQS6TFWV93TO_oHYSjV5tqHm-ePuvp0xzeXT49KEwxx1B1UeY0YvB5Ro7HaRcITbGTRphKeD5iYN-DMqb85K9AfrOD8OJ8Z4CbwluIKdZRWikOqbT7NHi0o9swLut5TZto6chazFfIFeYFI6uxRdkXf89iG_ybJwncJijitJM3Sp0N6RxCVJbBjEKa2vtBQnBNuK2eOcNPkKBneRTsfj5PPKTi5yI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
❌
جی‌دی ونس درباره ایران:
🔻
ترامپ هیچ‌وقت نگفته که هدفش این است که رضا پهلوی را به عنوان رهبر جدید ایران منصوب کند. چیزی که او گفته این است که اگر مردم ایران بخواهند قیام کنند، عالی است. این کار خودشان است. این موضوع بین آنها و دولتشان است.
چیزی که ما می‌خواهیم، توقف برنامه هسته‌ای ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66330" target="_blank">📅 00:41 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66329">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
جی‌دی ونس:
🔻
فرض کنید امارات متحده عربی که یکی از بهترین متحدان ما در منطقه است، بخواهد در یک نیروگاه هسته‌ای در ایران سرمایه‌گذاری کند. عملاً بدون اینکه ما بعضی از تحریم‌های موجود در سیستم مالی جهانی را برداریم، این کار ممکن نیست.
🔴
حالا سؤال این است: آیا اماراتی‌ها در ایران سرمایه‌گذاری می‌کنند؟ یا آمریکا اجازه می‌دهد اماراتی‌ها در ایران سرمایه‌گذاری کنند؟ نه.
🔴
برخی می‌گویند خب، شما به ایران پول می‌دهید. نه، نه، نه. ما می‌گوییم فقط اجازه می‌دهیم برخی از این کشورهای دیگر در بازسازی کشورشان سرمایه‌گذاری کنند و برای مردمشان رفاه ایجاد کنند. این چیز خوبی است، مگر نه؟
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66329" target="_blank">📅 00:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66328">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=aqNMQ3kYvJgHfMoACDBcbus1TgBzdZgy52VsNzcHj-fOLQAR9R6jpmLrepi5058uZkXdCxPzOjwUuSQhddlrFntZtOwOo-P9INSTbIkqIjaOMbcwEXLzn84HUy9NT0Ay1FnMs5lts_9eUAi7U5JWK8t8HcuZP_EPf4Ll1zjTHsq8ieoWfhh_Cd7B49f-C3BSH6GED56AgowiYVAnsuzgwf-NAvVsdVLIZmk7rwocOAjmTmtlAEziKLgMGKnBvAVBDm6qbYqyYeas0kOmeVla0CRtotLeNf1r1M8oz2K1NcrWKI74IaKRBCiH7UxQSLAdMt5jpYhCE6rkN8havTe424i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/400d2a3a78.mp4?token=aqNMQ3kYvJgHfMoACDBcbus1TgBzdZgy52VsNzcHj-fOLQAR9R6jpmLrepi5058uZkXdCxPzOjwUuSQhddlrFntZtOwOo-P9INSTbIkqIjaOMbcwEXLzn84HUy9NT0Ay1FnMs5lts_9eUAi7U5JWK8t8HcuZP_EPf4Ll1zjTHsq8ieoWfhh_Cd7B49f-C3BSH6GED56AgowiYVAnsuzgwf-NAvVsdVLIZmk7rwocOAjmTmtlAEziKLgMGKnBvAVBDm6qbYqyYeas0kOmeVla0CRtotLeNf1r1M8oz2K1NcrWKI74IaKRBCiH7UxQSLAdMt5jpYhCE6rkN8havTe424i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🎙
جی‌دی ونس:
🔻
یک نفر گفت - یادم نیست کی - که این توافق مثل اجرای طرح مارشال وقتی نازی‌ها هنوز سر کار هستند، می‌ماند. این حرف از چند جهت غلط است.
🔴
اول اینکه طرح مارشال با پول مالیات مردم آمریکا انجام شد، اما اینجا قرار نیست پول آمریکا خرج شود.
🔴
دوم اینکه ما می‌گوییم فقط وقتی از مزایای این توافق بهره‌مند می‌شوید که رفتارتان را عوض کنید.
🔻
(البته کسی که این حرف را زد، سناتور لیندسی گراهام بود.)
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66328" target="_blank">📅 00:38 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66327">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7276198054.mp4?token=aaLF4SyI2R903KBreAkEgN-X-Xl5BlQOW8r-dI_MFBmC8zoqsvXbX8aqAeKjHgnmF3rHxTvV-Dju07CVj1Wqp-vZJSKMuajNKw-j7sdD4G3gw1BRKeGAp5_LzQg2TTnRHXapkU_KBWaFb6dFLQNUE4XWbby4vxYpU6uBmwmn8_Bq8PP8UrsqqdpAhB1WlDxzEXtPiutFdPvPVq8oWEYqYo5Mzz99Zg8_l7iNHfyK6ulAlDTXuTEPmDBJ5S6kJ_Vs99SG2aW0RjMIHGOL2DHgrHsA1tF9XQyfSqd6RoNN9NU9H1A_aSg8G30u_uiOdGs8iVAIckNduRILbavnxmNa2ArVw7M3i_6rO3TNZGhSIWDwMfUrQ3lcXf9KGBAWH09p883v9aonHuwywIeo-2FpytFALV8BS1cPLY502EPprnC-TNhnTaJUQr0lL_XToCR255eCOVqpCKwOKffoPf9ryXFf4RCqcuyHZ_EhJdzv1sxq4_9MMbUS3S2KULpCeYhprqezEF7IKyH-AQ8C9gjJBK5Qepg_nvvMW2QMSf2uRvubMfOzgWnY5pODOUhTlDHi3lkEsu7H1E_t-DhxTqY_dL5GraM3ctj6tvyeF1NZx8BI2TDLR3vstFkkVVWzzuXUoDpEot1inr-eqO0KnlJEKnCWJTphO97zlOJlXwUDTG4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7276198054.mp4?token=aaLF4SyI2R903KBreAkEgN-X-Xl5BlQOW8r-dI_MFBmC8zoqsvXbX8aqAeKjHgnmF3rHxTvV-Dju07CVj1Wqp-vZJSKMuajNKw-j7sdD4G3gw1BRKeGAp5_LzQg2TTnRHXapkU_KBWaFb6dFLQNUE4XWbby4vxYpU6uBmwmn8_Bq8PP8UrsqqdpAhB1WlDxzEXtPiutFdPvPVq8oWEYqYo5Mzz99Zg8_l7iNHfyK6ulAlDTXuTEPmDBJ5S6kJ_Vs99SG2aW0RjMIHGOL2DHgrHsA1tF9XQyfSqd6RoNN9NU9H1A_aSg8G30u_uiOdGs8iVAIckNduRILbavnxmNa2ArVw7M3i_6rO3TNZGhSIWDwMfUrQ3lcXf9KGBAWH09p883v9aonHuwywIeo-2FpytFALV8BS1cPLY502EPprnC-TNhnTaJUQr0lL_XToCR255eCOVqpCKwOKffoPf9ryXFf4RCqcuyHZ_EhJdzv1sxq4_9MMbUS3S2KULpCeYhprqezEF7IKyH-AQ8C9gjJBK5Qepg_nvvMW2QMSf2uRvubMfOzgWnY5pODOUhTlDHi3lkEsu7H1E_t-DhxTqY_dL5GraM3ctj6tvyeF1NZx8BI2TDLR3vstFkkVVWzzuXUoDpEot1inr-eqO0KnlJEKnCWJTphO97zlOJlXwUDTG4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇱🇧
جی‌دی ونس
:
🔻
اگر ایران حزب‌الله را تامین مالی می‌کند، ما اجازه نخواهیم داد که مجموعه‌ای از دارایی‌های بلوکه شده به ایرانی‌ها منتقل شود
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66327" target="_blank">📅 00:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66326">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=M-ABrBl4eCQzUUF8l1-32rSNU4a9zk3tR4zJ8PfCwh-V9Rgg3u29L2ndpQ2UJMRsXLoIH0GCfDc_yOihanwBSC5rl3-Ck4wR2YFazR7wLRef5Qpfoo4M0qmBNU5adlk3VECQE2BOcapgeVcbJRLU6D6o6zq0EGuJZFnWd-zGsVQc3Amuzq2Bq0pXpWytzKCURl4ISOkxIf9XvhgeqYKprVxoVvdTimd2DR75l6ho9hqKuieJGK7SR_BjnvgB3cznox_OFIunyt2cXeLoWlGAiixE2q09byBPV7R_tRs_CkeSWpls4cZRuXJOWpm9EljHGyAO9VswIKWZ_-GZ-BoeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b2573c92.mp4?token=M-ABrBl4eCQzUUF8l1-32rSNU4a9zk3tR4zJ8PfCwh-V9Rgg3u29L2ndpQ2UJMRsXLoIH0GCfDc_yOihanwBSC5rl3-Ck4wR2YFazR7wLRef5Qpfoo4M0qmBNU5adlk3VECQE2BOcapgeVcbJRLU6D6o6zq0EGuJZFnWd-zGsVQc3Amuzq2Bq0pXpWytzKCURl4ISOkxIf9XvhgeqYKprVxoVvdTimd2DR75l6ho9hqKuieJGK7SR_BjnvgB3cznox_OFIunyt2cXeLoWlGAiixE2q09byBPV7R_tRs_CkeSWpls4cZRuXJOWpm9EljHGyAO9VswIKWZ_-GZ-BoeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوند و تعریف و تمجید از ترامپ
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66326" target="_blank">📅 00:15 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66325">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=h1D7AP26mpuyVBFmXQpgZRY6czTXXCVgq8VmpVXxw4cNCgQUPGNemzlJmlcpe-32kw-UZ7l7jhERTiIEmatvjUiBhaDJx6piUTuj2g53Z_NPpFZZ4rM44RXaj51Brppbxv4WxLhNnHi6RKCPIwWrZ2q5TRiqIH4x78j-31N0dF7lwILWalgSrInrTHFt5N2zmqMxn-OTE4Lif1slsbXgpT-QTuJmfhNKimOTPoGY05zj3g7qtPxJxO5bzNHdWDXk23PBGcC0HxuIqTPMGWuI_1pgrxGbU1eSRm2bVqoU90FGrlnQj-W48leMMqj1Nc2wW3XuHrHaNBiRURTVfKszaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1190f45b0e.mp4?token=h1D7AP26mpuyVBFmXQpgZRY6czTXXCVgq8VmpVXxw4cNCgQUPGNemzlJmlcpe-32kw-UZ7l7jhERTiIEmatvjUiBhaDJx6piUTuj2g53Z_NPpFZZ4rM44RXaj51Brppbxv4WxLhNnHi6RKCPIwWrZ2q5TRiqIH4x78j-31N0dF7lwILWalgSrInrTHFt5N2zmqMxn-OTE4Lif1slsbXgpT-QTuJmfhNKimOTPoGY05zj3g7qtPxJxO5bzNHdWDXk23PBGcC0HxuIqTPMGWuI_1pgrxGbU1eSRm2bVqoU90FGrlnQj-W48leMMqj1Nc2wW3XuHrHaNBiRURTVfKszaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان بازیکن تیم جمهوری اسلامی به خبرنگار خارجی:
مسائل داخلی ایران به شما ربطی ندارد؛ مسائل خارج از فوتبال، بین خود ماست و خودمان آن را حل خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66325" target="_blank">📅 23:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66324">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=CYqhCkDPXOiQNaKO_rkhS8LLk0BEGWXzyEUSeaeLTslMVD3i8uABtudliMomGBIDc7yHvh0zkk9_JwDcjE0SsFEZK226kWVnY0Hv1I6urGfkbYs3Cwb3XKt-jsKR2gJ5XD7u3OZ_79RleeHfKdpUfVh4z4XlaBPU76-peCXmtkg93lKe3EM0GhCcbZmsGFOQ4fRSNreGYg9CARsMre_ZBUWPONr45-9d_lThKAe5o47Z0Rb5gjVEY4mE2CFmBcPHvgXi-wpyTVWkho_rLG-oB-aUqAHhKpE15KyCFwQAmqq3OtmUS7CGA7kCQcTbP2rEufluLa6LnBNC3AtKPe2eYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fcce5ba4b.mp4?token=CYqhCkDPXOiQNaKO_rkhS8LLk0BEGWXzyEUSeaeLTslMVD3i8uABtudliMomGBIDc7yHvh0zkk9_JwDcjE0SsFEZK226kWVnY0Hv1I6urGfkbYs3Cwb3XKt-jsKR2gJ5XD7u3OZ_79RleeHfKdpUfVh4z4XlaBPU76-peCXmtkg93lKe3EM0GhCcbZmsGFOQ4fRSNreGYg9CARsMre_ZBUWPONr45-9d_lThKAe5o47Z0Rb5gjVEY4mE2CFmBcPHvgXi-wpyTVWkho_rLG-oB-aUqAHhKpE15KyCFwQAmqq3OtmUS7CGA7kCQcTbP2rEufluLa6LnBNC3AtKPe2eYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرزیدنت پزشکیان:
مشکلات خودتون رو خودتون حل کنید، من سیاستمدار نیستم من دکترم، برا سلامت مردم اومدم
😔
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66324" target="_blank">📅 23:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66323">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=BxA431plYoNbjczpNgyAamHS4dRfOa9RGz2rTu_7Fg4pOeOUmIPfYxGYOVlo_ZQw6P63BCcNrV_KeRajmem9gFPm0pIFBa5hWgRp0566pq4S1gQKnCXsQwMLBvj7OZcFIiia78tGT3cfMq1APeod47HmXBF7jJ-aEpKwRGBeyLdT0f32DLOzOvtZarEEbxyPb924gzE0TkEnn_-Toh2A6XH3HpmS_KAa9h9PwfIMEQDpHzIVlkUQzKwWiYJP_Mdu5efWoOqCzM6DW0YWEdnrHdDz_G7jGqy8EApz2JCMb2yDcN0yH6ehp_TMrK6AGFOpH2HcwFXuaxwhH5gGpTArrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9ab7bce46.mp4?token=BxA431plYoNbjczpNgyAamHS4dRfOa9RGz2rTu_7Fg4pOeOUmIPfYxGYOVlo_ZQw6P63BCcNrV_KeRajmem9gFPm0pIFBa5hWgRp0566pq4S1gQKnCXsQwMLBvj7OZcFIiia78tGT3cfMq1APeod47HmXBF7jJ-aEpKwRGBeyLdT0f32DLOzOvtZarEEbxyPb924gzE0TkEnn_-Toh2A6XH3HpmS_KAa9h9PwfIMEQDpHzIVlkUQzKwWiYJP_Mdu5efWoOqCzM6DW0YWEdnrHdDz_G7jGqy8EApz2JCMb2yDcN0yH6ehp_TMrK6AGFOpH2HcwFXuaxwhH5gGpTArrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عرزشی:
چرا با کسی که به رهبر عزیزمون اتهام جنسی میزنه مذاکره میکنید
😂
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66323" target="_blank">📅 22:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66322">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
ارتش اسرائیل، طی دو روز گذشته پس از اعلام پایان جنگ از سوی ترامپ، «۸۴ بار آتش‌بس در جنوب لبنان را نقض کرده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66322" target="_blank">📅 22:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66321">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
#فورییی
؛قرارگاه مرکزی خاتم الانبیاء:
اگر ارتش رژیم صهیونیستی حملات خود را در جنوب لبنان متوقف نکند، باید منتظر پاسخ سختی از سوی ما باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66321" target="_blank">📅 22:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66320">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=H-ylLrz15k59d-LH_ak-tit-R5KvvxE2bdgKheJJk5UsdRviC_U_fKjH8-r3Cn7IBLwHfZS_3U8aiS3e_G4ike9pE85Wk4j0W_UuSlnkgn01QkSnEFdEBriDpYKU8D5WINqUaY2IPzIiqsTT1zto7e89IqK-Zej7SNYixHBDVfwx12Tbe4qk7renr2hMwdigZzf0eA9zJnNx2NQa9rx105PJchrDbBPxl5Ei_-WvvEKsTMHdjiNvxk3FIMJYufsITASZGc0lDA_5ieleAxZzedCop1dXEKrMA5bQ5rY63JwH3cIZGY09eZHIA-CzDxm8icByIW8S-enps9fcGLkOVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e376d329d7.mp4?token=H-ylLrz15k59d-LH_ak-tit-R5KvvxE2bdgKheJJk5UsdRviC_U_fKjH8-r3Cn7IBLwHfZS_3U8aiS3e_G4ike9pE85Wk4j0W_UuSlnkgn01QkSnEFdEBriDpYKU8D5WINqUaY2IPzIiqsTT1zto7e89IqK-Zej7SNYixHBDVfwx12Tbe4qk7renr2hMwdigZzf0eA9zJnNx2NQa9rx105PJchrDbBPxl5Ei_-WvvEKsTMHdjiNvxk3FIMJYufsITASZGc0lDA_5ieleAxZzedCop1dXEKrMA5bQ5rY63JwH3cIZGY09eZHIA-CzDxm8icByIW8S-enps9fcGLkOVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنوز سواله برام؛چرا خارج شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66320" target="_blank">📅 22:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66319">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRp1YfxT6IK6RGOB5OVC8bwLMLJ3u-WaMJebP_dkhVmgqXtTYDe_3u9QqTDrcrIKGmLI-DRCdski_Ts8cpyPxjwab83P6zOmNHRU6YhNx8tXZHyu26Uma4uq3XSwtrSe-q5f_rd5QzBtfqizN6TBHVLuKlLHP8TRCctimG3Bid0CBVjL3wbBw7i6BXNaCSU98DhH8AxjYxt_GTpN7RxEAvhCnAzBNAcemFo6519dEUz1kcd4v4akU-vKoJ2hU1kIx-cxzit7VKtcCCo3LLskxRjrUDzfXK62XnczldjaeM5r8Za6jQqOweoC5Vio8FCRzSpeBvc6n1hEYC4Fp3UEaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نفتالی بنت یکی از نامزد های نخست وزیری اسرائیل در انتخابات آینده:
توافق فعلی بین رژیم جمهوری اسلامی و آمریکا فقط یک توافق موقت است.به ملت شریف ایران می‌گویم که امیدتان را از دست ندهید، جمهوری اسلامی رژیم فاسدی است که سقوط خواهد کرد. نوبت بعد که مردم ایران قیام کنند ما ابزارهای لازم را در اختیارشان قرار می‌دهیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66319" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66318">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/837293596a.mp4?token=k0rFmAU_k74YdzJIlGHQ1bOmGTvHDP3H1w1CDoW0bYvzYaAAUVOSsRDlLRqtfcOMRfWRjFvZKoauLXbqKWUDHrzPNo5h9h5uTFZzW5y2IGD2cnXaXHx3PC6jtEWVhZYY7GNVk7ElSf0XT8RKbpt7Z_vbxQzF7dMkeNJG2LLOX4B2rUYPATmHU9pjI4KwWoi92biui6NKwLe4oHh5YadHiz5doces1vzWUuGFvdoSdId1NfNOhypwOTRvdrNOrDutchG4Aggtz1yo5oAqLGCoQrpcahtW96sx4rOmD0OhXb2u1h4607RfypD4Lvnlh4TNmtorxwzubb10HL6ZmDhtnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/837293596a.mp4?token=k0rFmAU_k74YdzJIlGHQ1bOmGTvHDP3H1w1CDoW0bYvzYaAAUVOSsRDlLRqtfcOMRfWRjFvZKoauLXbqKWUDHrzPNo5h9h5uTFZzW5y2IGD2cnXaXHx3PC6jtEWVhZYY7GNVk7ElSf0XT8RKbpt7Z_vbxQzF7dMkeNJG2LLOX4B2rUYPATmHU9pjI4KwWoi92biui6NKwLe4oHh5YadHiz5doces1vzWUuGFvdoSdId1NfNOhypwOTRvdrNOrDutchG4Aggtz1yo5oAqLGCoQrpcahtW96sx4rOmD0OhXb2u1h4607RfypD4Lvnlh4TNmtorxwzubb10HL6ZmDhtnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جی‌دی ونس:
اگر مردم ایران خواهان رفاه بیشتر هستند، رهبرانشان باید پیشقدم شوند و رفتار خود را تغییر دهند اگر این کار را انجام دهند، عالی است. اگر ندهند، ایالات متحده قبلاً چیزهای زیادی به دست آورده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66318" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66313">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozSYJDE2AUtKqX7Dhw3vawvpFh9UzWKFBJqeNmmGysBwfuo3mSva5yj8QmpJ01TIZ_DZvhupzsnGpeAgb2haKlV6BRIlmMwUzXvJiYsee2yhQolt4Xmx2goaDiQ_C9XfNKOksRsQPFUtFhduBZ8VLhm_qBQdu-inxu8Wtb5s_KqQYVPHSoEsqm2PLc9FsZOLTCqhupPSDU4CIClcvZtzNGCOX1IS_gZ4bZOP_XsNtNDkBBzFynWj3iZH-E6v6oNIhk7DVHemNYNozDPopUIhjSsfr54mMZSleZ6Rw-GUm5mqNygllhhYOFsJUYNq8RdSpTlcj-xLMkFY_Z3jpgJmOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
زیر نویس شبکه خبر:
حمله پهبادی اسرائیل به دو روستا در نبطیه در جنوب لبنان ۴کشته و تعدادی زخمی برجا گذاشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66313" target="_blank">📅 20:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66312">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuxSlkGVqQSqglwGtKwYpP6Rc2F6c6ohHLMrAF_b10doiQxbIMI7mt551ovRxKf5uxFiWbedtx7MkHqP5OW4BStkWMnc54HE0ns0_kzbJK490A12n_HGHBHqTTc-tJ8RqdB2T2ZTKCvlc1pI7ieJy_BWdWG0ZQJKpBU9DsU74peAS8kek1JPYRjvucPx_oraSIfiEA-5WgtEK9ujArXVnMMgPZgQlGk58b6z2DW-LglP_TKLe3ZS1_0N47PtqrigFX1VQ8gMNc8n4SGQeoDRdZDkaZpbbmQYncFQ8fedl5qZUOpjhjccbGr9t5mOON1ZTgEIsauuwrxFgom8Z4JcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اتاق جنگ اسرائیل:
لانچری که به سمتمون موشک شلیک کرد رو هدف قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66312" target="_blank">📅 20:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66311">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6n-Uw8GYDdenl7jldMd8C_pDe6xFGu3EwmqFy9h_d2Go6v0RS9ooa63kBKczbfoYxNsUXcVHhKVaJGcOFgYt8Ih020kjyj5NJDRuihcy8iDhqzd1CJSz-wKsyVSioefcriL-ySbfC1CzNIZteT2jW9hV0P_5l_laiwiOgAZ-0_hfhJi5Rnff2cLCBd-Fzri-eksP1wd6_7Yd8OB5vCYbn33zk1I5IyOUrMFKypgMMZZ0vz4OjSXH0rGG61he4aueJNw-iKwvSDBB9TkklDby7fmS9NJTYSv9gJLRZS1zCA-T-R7DrA7JNf6ncPT9vp6w71Zlv5G9poxBinptOeSYeAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c47f7533b.mp4?token=f7385ysPiZEwGoEq5-BhvdKicJ4NcTQXnknhf2UvrtYtc-fQzNFN0KkcOBRlJTNQYoFc5paWMO218iGDM5BzwoFdNpmuWflWzNTfQgSkt1M4UeXFcrMLgQbOvVco_FZa8VSODpkIISnB6ya5ctpFshKx7TF42B1-8t7WcxElojqTH6JlqzRmc3E-nmlLeeYBgVCvvds6xJUxpiHQEQNhsHMAWMrkfiBaiOx81j7tXijDlSS8rLbjTMHO8SBIEZL87It1lYJLU83I3jEZ5LGeLVrNiLXwTPiPwORFcJ66MaNjrcvikrPtj6DQ1cDXG7tFxmfCcwEse2evayB7Wug_6n-Uw8GYDdenl7jldMd8C_pDe6xFGu3EwmqFy9h_d2Go6v0RS9ooa63kBKczbfoYxNsUXcVHhKVaJGcOFgYt8Ih020kjyj5NJDRuihcy8iDhqzd1CJSz-wKsyVSioefcriL-ySbfC1CzNIZteT2jW9hV0P_5l_laiwiOgAZ-0_hfhJi5Rnff2cLCBd-Fzri-eksP1wd6_7Yd8OB5vCYbn33zk1I5IyOUrMFKypgMMZZ0vz4OjSXH0rGG61he4aueJNw-iKwvSDBB9TkklDby7fmS9NJTYSv9gJLRZS1zCA-T-R7DrA7JNf6ncPT9vp6w71Zlv5G9poxBinptOeSYeAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه ای که سپاه داره لانچرو برا شلیک موشک آماده میکنه و ایشون هم شروع میکنه به فیلم گرفتن.
واکنش سپاه:
😡
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66311" target="_blank">📅 19:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66308">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OG7WLH3LSqeyRqHVPF4L_pCMz45Hc7K3pUwV5POthKz-BgAZCxPQYJLgCXJJHJsGY1EGERk3HzdN3xg-PynsnxmrdVYsCITGYJPhFUhLZqS8ZiUCK9NEMFuYk5wmFJ4Vy4I1K3VnpqkqWXVSddCdYJMm6cCWxPt24O_i07uASxXVmC5btvLLu45D-NWEZb1B3oUFPeTtid7JuRoXwTzmu4CXhGui5gP5mOaLe5T8XrkC8nnCJQfK2ch7aFUEhsDqr4CldP_m4BgCBnszZMEN_Dh-cG6FstSQwh-R5URvARTar4APXKw-LdSrJh4gzQYLFJIx1kmRt4pCkP20Ba-_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فاکس نیوز:
اف‌بی‌آی یک توطئه تروریستی گسترده و چند مرحله‌ای را که قصد داشت رویداد UFC Freedom 250 روز یکشنبه را در چمن جنوبی کاخ سفید هدف قرار دهد، خنثی کرد.
به گفته مقامات فدرال، این نقشه وحشتناک برای "ایجاد حداکثر تلفات" طراحی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66308" target="_blank">📅 19:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66307">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvBiedGQigUjdkulnvDuy-uH3WZilkHDU51-FjuLv3u2F7-YkbNmY2Iw3t39U_LZrNtr4wZl9Vh3xBO4zepvUTkPdU5DywBboFb_HYo_QPi3B2u-cvHpiK_9ynBtdqJPReN9X9XqwwrLZYH2-UDF9N6QpWEs37OkM0T4hhCLbF-gUyQo5bRcZu8Bqsoh1caSDgm-O4ePfEx8RMPRUQK0VpXLiS4QhjJp3gcRwgP_sVURmbGkhhXvkAnZ-qzV8WnUtT2tm609gsJYI-pJpILWaQVUy0_dMj98G1BbvIWTioz4oKyhRr4o5QeiZMnFGNbPI8sR-xRV2O2Z7zsBkp55Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارتش اسرائیل، منطقه میفدون در جنوب لبنان را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66307" target="_blank">📅 18:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66306">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=nGqY3li4hhIRPSnk5J6xWrQ35nid3LWKE6tdcXn4l5u7O2g6paU7LSixQn6UMDj1KTDKzLSWFt8f7l1Lkz7Po5HAB955gNl8U2Jnky0KueS9DShfxJlvbGu1RMDvQc0PVEwtF_t3IgiN88VCURcWHKjwnKiqEDYO8Si9Qyo4Ksi-7a7HluGu7vkPTPrnLG6iKfxlYiltG_C8rktcUxLrpb5WI7jHJwOQeLOGY3SQAn_sXMQpSWulsVt6qUjifSG6v3-or1PsPRbrAIogw-htG_mQptcrQDzHr3YGOePAtJNUQdSVSqMHrZ-YianE2sZ0Za1DqSxkzoa2lgzLXAeWCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc0108dd2.mp4?token=nGqY3li4hhIRPSnk5J6xWrQ35nid3LWKE6tdcXn4l5u7O2g6paU7LSixQn6UMDj1KTDKzLSWFt8f7l1Lkz7Po5HAB955gNl8U2Jnky0KueS9DShfxJlvbGu1RMDvQc0PVEwtF_t3IgiN88VCURcWHKjwnKiqEDYO8Si9Qyo4Ksi-7a7HluGu7vkPTPrnLG6iKfxlYiltG_C8rktcUxLrpb5WI7jHJwOQeLOGY3SQAn_sXMQpSWulsVt6qUjifSG6v3-or1PsPRbrAIogw-htG_mQptcrQDzHr3YGOePAtJNUQdSVSqMHrZ-YianE2sZ0Za1DqSxkzoa2lgzLXAeWCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
ممکن است شخصاً یک کنفرانس خبری برگزار کنم و متن یادداشت تفاهم میان آمریکا و جمهوری اسلامی را با صدای بلند بخوانم تا رسانه‌ها آن را به درستی پوشش دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66306" target="_blank">📅 18:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuP9703lSSAe5IwUDmtW-4Wq9pLhMt9Wrc0Z9qVyWt_WL0FMYQPIJP77t-ZJIhpv1cC17TZcQHJmAS7N5nD51bk07Ll6AAD7xTisqubfAGccPmfcgGphC4WmjdR_pkGzySXP0cZPV6JbyKt4SqtfWmXiVuW6NNdAXlC5WClaexfRwiq7zCGbI5pVqOwM2P5T5kWnFOO2JFhbFZI2G3b83vuHW3vjvAjdmlFeJJGipmSgNNK9J-QyzVUwGr5qoZqrklesT57kYCCov9g3Un9H8lfwK42DuG-BKEKQ4shUf1iqdVdVFmijyRHAszFDiDiM6OidSNJu-G7PWnf_qJLisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت امور خارجه سوئیس:
قرار است یادداشت تفاهم ایران و آمریکا روز جمعه در بورگنشتوک، در مرکز این کشور، امضا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66304" target="_blank">📅 17:48 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsKp38HBx1-f6xR-EiYlUbc1LBl522DT-8i7KVuLtqwQGthU5u2R9nqr7TH3wRenVookjlRBUgfGm9hfBowB4wMUI901V83OSBgcxp1ctq-M9HZiWyI8wWxbDOc3iAcYho6LNDwkrn-IPooaTHF4zT9iwsXQoMCI88iX2FuiJ3t_9FubZNthtKyj_wKeuWg1yhlBN4jooQpZbYxj4OvZJyBl_NkwIohYnGTefR_caQhjRowng0TvMUWYEKJ30okvtbW5P5qbvGbkFM-zwjlGbUfjgmjZmIWnpVsPARJ6t5MG102bqgQuoaqHGgJjbL7TY1hk1yOeCVAjYOy2A6AenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر تیم جمهوری اسلامی که آمریکا و اسرائیل ویزای جهنمشون رو اوکی کرد.
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66303" target="_blank">📅 17:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66300">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=CT7vZW-VC39GyNurLm5WoGcrbufXFEb_k8Yixk_ewF_oKJZC4l8Gfrbp7Aqi5664bTGqdvRm3A7TE_wLwhHcHsrCOszrlYhAQ3bWBfj6lpGze__ASD55zg8j11yKLIxnp-o8JGE0-nEOi4WVCrxSvheu5V8TD8ahCDFwDp1-wp-dm3-gX4G0sUIgpLhmzrws9nlwOs-H2Nxz9-7bi4-r7HB9pRjmJAlyEQIinhn1_rp4NxZCYAXsqGrlmlLXdtCTAVOBn_hPA2-0n2Ch7PXFjd69XE5HyZSGfRmkRuLp5r9IZClc2EbfcGahPyWIN2BwfqUqeFyZrJri0YK4AYNiIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d1538e700.mp4?token=CT7vZW-VC39GyNurLm5WoGcrbufXFEb_k8Yixk_ewF_oKJZC4l8Gfrbp7Aqi5664bTGqdvRm3A7TE_wLwhHcHsrCOszrlYhAQ3bWBfj6lpGze__ASD55zg8j11yKLIxnp-o8JGE0-nEOi4WVCrxSvheu5V8TD8ahCDFwDp1-wp-dm3-gX4G0sUIgpLhmzrws9nlwOs-H2Nxz9-7bi4-r7HB9pRjmJAlyEQIinhn1_rp4NxZCYAXsqGrlmlLXdtCTAVOBn_hPA2-0n2Ch7PXFjd69XE5HyZSGfRmkRuLp5r9IZClc2EbfcGahPyWIN2BwfqUqeFyZrJri0YK4AYNiIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگام بمباران بیت رهبری هرکسی که اونجا بوده کشته شده جز مجتبی.
مجتبی همون لحظه:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66300" target="_blank">📅 17:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66296">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fZYjvv-MgQV88I3nolsUWPxt7_ueP3445dajF7Z9jofZmNTy6Ow0gg3VpQETZULj-viPvV5xxoxSxd0j-ajHMeE9nXLxIL9_NfY-npD6WHjOcit696Y6_RxAi4ujDsPPl8XkamuOHME-n-SKea0kW_CaKUxiJTab-07O266-JVYqvC0JtnAUmimDeQvMviN-O4EkN71tdDio9FVbxGKQgWAx_ZwZgaCAln0YuKqPejjNSYMVqvw6pgQZJRGK1LNIDOijEOiwz7TLtrbsl_pS43PXT319RbgcVfdS7zfG__PErzHCv4ixj4L7XgfpwWjh96rnm1xaYrChpXNNH48eCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6tMfFUlxbBqccGCx0GZ062i2fhmnxQS9uNQVNahDO4HZdfQbNJm41aGraIAHs_Ff-A1jmyZwck7TBrWIeZwrP5aNEwI7335SZNEqrtKFuiB78qNX6IohOe-Dw365bswjHH19U3Wz6utT-mTNhw1zRkj0CQCBJp6HiGVaV_vTs2np2iCMUfgz41StiLLmwWDgkF6gSsCOJSK5a4R9tRWS8KvMcN9bHc3DMR0DIhSHfLiBU5YH4HBmzsXolN9pBQxrc9RFqwxPiWX4u7tn7FO_6SSroWlTx39KG3651dMqTz9CW9Leh1VuHARQyo59azbghyI-EwFC6x0xjnYGm7Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDEQO9DD5hatZpFDzKGQAv_l9QTOg1lR9t_oT9E7UDMh4tyiACj87v1l3GSP5lYFdglEMVDJMJ5cdj1Qwi_0RnOnHH2pA9xk6JBfXoctfDrsvOjsycILHOWJ_cP05mFPbv0-1qR3VzNUcnmuGIIYt--CfvC9nQqNJqOtjJJNsiInwita7Y9dGUN5YPSqlUNpk0JiQYY83XR--DtKCPayfTRWegRDUG2OD4G7lxIvQrLFdpX-uX1eGb1MWnE-kpa9rRh_AK8EUqo9IuOBug-1ycKMlGDAwyQ9UCdsMMcxfLLpX0mOFcfQ5-bqMybZydVSrHzwraC61ZG3L_x1Fi7--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKdZQuPPhuCawShM-TmMfft4YGfRmWCUO2cq31968d9QnK88aFE3A3T9nNrmyHhDB2TW1K2TJp7nZ9gHNJGBJ7uiBoDxpiYBOVjK7zAoAyr7HaIovJtPWSVVZhfWXzWgBrX4NQIh0x0_DvEfqUuYRqZzBq5sKE6HXWyTAV-OSNHl8umx-JsUmRgkXuS95sj7YemzXU5IFimQ-l1X_GQi5FGn3Qek56aDiJVQPuBrcevQjvVfiByrlaj3uR2k2h32E2TsyC4zKF-1TTDtAXB83BkimEHfXrwZk4qtdRBRyiGrYNM6Go0QKq7EeyZcy9WTgdLEDb8LZBrbeN9jdIwpLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ویتنی رایت پورن استار مشهور آمریکایی دیشب در استادیوم حضور داشته و از تیم جمهوری اسلامی حمایت کرده
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66296" target="_blank">📅 16:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=Gkfpa5jkDUs-eIW9_hEEQe_2SjS9AYbmCVYFkjydq0p9y2yWX5NRImiMSi6psHvWhDyiDtTSd6pSi5eFju1Uyx2KyOjugjIYKk7yoepdHnKLQzODIv6nAJ3bpk01H6WSD76ojnK7GCKP39Fk--NJvATC6iMPtdFqfnkhjpAw2Z-nbIiUXX1JZ5UuMEeJ5lL2qMmb_Mls63B37TOc3Rlpc51LQHeDS9zj7oTtzPWefBm6pD82kwtEqVtgtFiKr5oLxczRiD5CKPfi9BQ83_HcsPWyMRBRwfYQC4ljYFmPFBj-Duy2_Vo0S0zeQSJrMJ7sSLuAAfMj6b83U9JzmKKb0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34b0ffff.mp4?token=Gkfpa5jkDUs-eIW9_hEEQe_2SjS9AYbmCVYFkjydq0p9y2yWX5NRImiMSi6psHvWhDyiDtTSd6pSi5eFju1Uyx2KyOjugjIYKk7yoepdHnKLQzODIv6nAJ3bpk01H6WSD76ojnK7GCKP39Fk--NJvATC6iMPtdFqfnkhjpAw2Z-nbIiUXX1JZ5UuMEeJ5lL2qMmb_Mls63B37TOc3Rlpc51LQHeDS9zj7oTtzPWefBm6pD82kwtEqVtgtFiKr5oLxczRiD5CKPfi9BQ83_HcsPWyMRBRwfYQC4ljYFmPFBj-Duy2_Vo0S0zeQSJrMJ7sSLuAAfMj6b83U9JzmKKb0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استادیوم فوق‌العاده زیبای مرسدس بنز در شهر آتلانتا در آمریکا میزبان بازی های جام جهانی
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/66295" target="_blank">📅 16:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66293">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfOrH9czKBJPAEjOy2e8NmNSgoPmrXkeOom_fRjMN0E84uagOXS3wa4-Mu6OjFw7NNTTWutDeayhtXFi0maY5REL7p6IWpRwu-UI5oV2i8viXKIKE3ZSDn2rzQLIjkyx6stJzQt4vCvK8zb3wq_PKOYWTtQG7Kfl_5ErRIXunhHucR1ueoXKJvCNexJGTs17E28y6nAn1t_NwMWDyLuBDoYcZ01NHOg32QrFA-0vmRC6nMP8ikaKaOLccVi0w0XNriGUZ1YUe6Avs1vucRY4h0zrD_-8OrUUDIiiBOQD6jRByb552oOb29L3HOIXgLaX8GAE5Y7P98qJk6ZOS8PXhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شاهزاده رضا پهلوی:
جمهوری اسلامی هم‌زمان با امضای تفاهم‌نامه‌ «صلح»، دو تن دیگر از معترضان ۱۸ و ۱۹ دی‌ به نام‌های جواد زمانی و ابوالفضل ساعدی را اعدام کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66293" target="_blank">📅 15:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66292">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=h3wsHjVndiRfBLWXrDwbiKUkZ06M3_-6cIJIyYr-aFVc548l1gSGI8dd1uYtGARyFQyivLWZtKNwe-KWrbIAPItwnIPQo-Wu-g4dh8vlMCxZ-Olp6JWCCfQDvKJhGsOqPyN5mo9MImdtVQU8sFZRBzMYe0phEO3Vckm3vA55bNOoAs-KUvFb6xF1awrtwVZiVXIMxPh0lbp51eQFmqKPloyswBYFneb8SKeZ7f02XqTBXk-2td46xlnbavROQj0bhbLORgSai_SxISzPcHZPLHxfL1Vd6JZSyCm4fftYi3-tadHXkrVp9t_soc2PnXLmnHov7bgIogKtya-7NnfSZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52f8c1feb4.mp4?token=h3wsHjVndiRfBLWXrDwbiKUkZ06M3_-6cIJIyYr-aFVc548l1gSGI8dd1uYtGARyFQyivLWZtKNwe-KWrbIAPItwnIPQo-Wu-g4dh8vlMCxZ-Olp6JWCCfQDvKJhGsOqPyN5mo9MImdtVQU8sFZRBzMYe0phEO3Vckm3vA55bNOoAs-KUvFb6xF1awrtwVZiVXIMxPh0lbp51eQFmqKPloyswBYFneb8SKeZ7f02XqTBXk-2td46xlnbavROQj0bhbLORgSai_SxISzPcHZPLHxfL1Vd6JZSyCm4fftYi3-tadHXkrVp9t_soc2PnXLmnHov7bgIogKtya-7NnfSZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انتقاد ترامپ از روشی که اسرائیل در لبنان به کار گرفته است:
لازم نیست هر بار که دنبال کسی می‌گردید، یک آپارتمان را خراب کنید.افراد زیادی در آن خانه‌ها هستند و می‌توانم به شما بگویم که همه آنها حزب‌الله نیستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66292" target="_blank">📅 14:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=b7fyCpKMClWat_bsV4fIFhaBjjtSOcJopkPbGp0BVtfR1GYq0g91MDEMpl0N50z-4gsli7tHG3mP-l3I4EdE9McefowqlDjk9Qk9nTW4psEpM0Q3Y3kfHXkTHup0jDR_5fY7OwI1Op4UwxaZ0pS2hWh--0vmNBgKMgJF8oxwfsJ3UE4KgO34OBqgQ1IYbMnxj-rBPDoD5QfeFBj3CDDnC2j8HorwT-oZPwV4RMpZ40I99jlJ1R1mEch5D_8jJik_0_C7oHIpUBmvbBRfdK2tc3RRPC5FSCmSXQzyas933n2C-5KuDx9ul3W4iQg7YxoIUBmwk7croLnIfSCipSZHMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db26cc81b.mp4?token=b7fyCpKMClWat_bsV4fIFhaBjjtSOcJopkPbGp0BVtfR1GYq0g91MDEMpl0N50z-4gsli7tHG3mP-l3I4EdE9McefowqlDjk9Qk9nTW4psEpM0Q3Y3kfHXkTHup0jDR_5fY7OwI1Op4UwxaZ0pS2hWh--0vmNBgKMgJF8oxwfsJ3UE4KgO34OBqgQ1IYbMnxj-rBPDoD5QfeFBj3CDDnC2j8HorwT-oZPwV4RMpZ40I99jlJ1R1mEch5D_8jJik_0_C7oHIpUBmvbBRfdK2tc3RRPC5FSCmSXQzyas933n2C-5KuDx9ul3W4iQg7YxoIUBmwk7croLnIfSCipSZHMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
در توافق من، اگر ایران به سلاح هسته‌ای دست یابد، منفجر می‌شود.
در توافق اوباما، به آنها اجازه داده شد که سلاح هسته‌ای داشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66291" target="_blank">📅 14:49 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=QgGgZDSWbgHTtjiK62x5un5_2ZlMiD2O7uZuN3_QoNYLml8D2CC2KH3Tn8YaCbqn_7I6uhyKQjrO5p84zWpZozivhtPG2G_R-P3FXftrkJFpzx8d8HsNiUQmgkCGSAbHrqoT6rYf5-Xp5XewB8RKb9vbq9Q7ond83geq_N8vjOjec_hxq5D545qUsWYHwVddcfbNTOi8CBL2_vpMWxNMYyJE3a11gT74Cy6WdJaI5nnqnLyNueWCv1oV8VfYmfguCRAn_NibH_G5iaaAYd9QIxRSAI7xpbiLC7PlkfPoof13EFhQPu7kpQfm6AeUefVIWniL2g6HcBQoNMZn5yoEeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeee1ba07.mp4?token=QgGgZDSWbgHTtjiK62x5un5_2ZlMiD2O7uZuN3_QoNYLml8D2CC2KH3Tn8YaCbqn_7I6uhyKQjrO5p84zWpZozivhtPG2G_R-P3FXftrkJFpzx8d8HsNiUQmgkCGSAbHrqoT6rYf5-Xp5XewB8RKb9vbq9Q7ond83geq_N8vjOjec_hxq5D545qUsWYHwVddcfbNTOi8CBL2_vpMWxNMYyJE3a11gT74Cy6WdJaI5nnqnLyNueWCv1oV8VfYmfguCRAn_NibH_G5iaaAYd9QIxRSAI7xpbiLC7PlkfPoof13EFhQPu7kpQfm6AeUefVIWniL2g6HcBQoNMZn5yoEeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
گروه اول و دوم رهبران همگی مرده اند.
رهبری فعلی ایران افراد بسیار منطقی هستند. تعامل با آنها خوب است؛ آنها افرادی قوی و باهوش هستند.آنها رادیکال نشده‌اند و به دنبال کمک به کشورشان هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66290" target="_blank">📅 14:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=Pc088JEAcFXCSmra87Z5Bdc7bn3MFPL9_V7GcHoYD3b06kRYZ8rhzF7QaeGlL8gFAdntjsHMToi4sNOSFrqVFxLZHBHTC5BHcB5WuXfhwxHa2iTLcrFhJxIHBwENP__UWX9q2lqobe-ll43pessAO_W-e9mASTWRNfbaTTGP6DCp4dcn7jePOkDS60XLfDpXJbBNSTs2Ar_zHRVYwiQKlQPskn8DZkEnsnHKVqxR9apR4B9aC2l7L7ba7_EcY5J-zrAhWuBOlQOp3UoJw3nWtPFzHS_S2iVQfMG5sr8MtV0gpRGCG1Vq75FZe5m3YPqUqrcPO7_6jXgoV3FTxMPGmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/059a9cad8e.mp4?token=Pc088JEAcFXCSmra87Z5Bdc7bn3MFPL9_V7GcHoYD3b06kRYZ8rhzF7QaeGlL8gFAdntjsHMToi4sNOSFrqVFxLZHBHTC5BHcB5WuXfhwxHa2iTLcrFhJxIHBwENP__UWX9q2lqobe-ll43pessAO_W-e9mASTWRNfbaTTGP6DCp4dcn7jePOkDS60XLfDpXJbBNSTs2Ar_zHRVYwiQKlQPskn8DZkEnsnHKVqxR9apR4B9aC2l7L7ba7_EcY5J-zrAhWuBOlQOp3UoJw3nWtPFzHS_S2iVQfMG5sr8MtV0gpRGCG1Vq75FZe5m3YPqUqrcPO7_6jXgoV3FTxMPGmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‏خبرنگار: رژیم ایران همچنان به کشتن مردم خود ادامه می‌دهد.
ترامپ: بیشتر این اتفاقات در دوران رژیم اول و دوم رخ داده است، خیلی بیشتر از الان.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66289" target="_blank">📅 14:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=trQP1jBRYC1wbD6phDTwhsQG4NOYyopLfPBrZFPlZTWJCmpl1Epkx_mRqxvhDSR9UBmBEVvOqCKXIo7-H9T1-FUnGX83dL37GT7F_yTRO0xhQnfRvHuk3igrCEeVlE3nXFHK9cDY9wY3Tffk05e8mYJ1mvzK6uptrjqwR3TTV8QDiBu1QZ7DhR0VwCNHQv3Z31yfHomPVyCz7lkbAnalRZpIxEjPj84nlLzl6VsfSVpQNn7a5YX1VINw22fIUaaUN7izUp3kwzh73QzpK6je6uTYT0B4q6OHPuCQYfAy8VKMTpo08gLuPqP5bM51CVUUyfo7gId52NYTyfIF4BETOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6ac4ffe1.mp4?token=trQP1jBRYC1wbD6phDTwhsQG4NOYyopLfPBrZFPlZTWJCmpl1Epkx_mRqxvhDSR9UBmBEVvOqCKXIo7-H9T1-FUnGX83dL37GT7F_yTRO0xhQnfRvHuk3igrCEeVlE3nXFHK9cDY9wY3Tffk05e8mYJ1mvzK6uptrjqwR3TTV8QDiBu1QZ7DhR0VwCNHQv3Z31yfHomPVyCz7lkbAnalRZpIxEjPj84nlLzl6VsfSVpQNn7a5YX1VINw22fIUaaUN7izUp3kwzh73QzpK6je6uTYT0B4q6OHPuCQYfAy8VKMTpo08gLuPqP5bM51CVUUyfo7gId52NYTyfIF4BETOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ در مورد گرد و غبار هسته‌ای:
شما می‌توانید این استدلال را مطرح کنید: چرا اصلاً خودتان را به زحمت می‌اندازید؟ چون واقعاً ارزشمند نیست.اما فکر می‌کنم از نظر روانی، ما می‌خواهیم آن را به دست آوریم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66288" target="_blank">📅 14:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77169efe09.mp4?token=BV1FBA2EGLkfLcl1dU2fazboz4FY2jaOn036pfClK0wBn5C37xCte1qW9Ggxvt73XlibOb2RjO9tPgaVJBmlIpf0E1Z_45pEWNZol_4px1Rz6JpXncGDtk4lqBQTma5GOdCSzmljUlWrEMOMGgW3ebnkKwNxr5KzmPb2pkZwkATC-7QToTXeYb110iXkibZv6Vod6It3MJ0h4yJf-FNYE58Z-rU9aISueZSmfqDsn55EOP2Swzwa-TR9y09gXMpu811_zUW4o8OudrtDCHIZQJqall9rxd4llvw2omCjEK4GCVejyCOnj5SO77H7_mje0m0lF3K2dYQlZvwZ4BHyUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77169efe09.mp4?token=BV1FBA2EGLkfLcl1dU2fazboz4FY2jaOn036pfClK0wBn5C37xCte1qW9Ggxvt73XlibOb2RjO9tPgaVJBmlIpf0E1Z_45pEWNZol_4px1Rz6JpXncGDtk4lqBQTma5GOdCSzmljUlWrEMOMGgW3ebnkKwNxr5KzmPb2pkZwkATC-7QToTXeYb110iXkibZv6Vod6It3MJ0h4yJf-FNYE58Z-rU9aISueZSmfqDsn55EOP2Swzwa-TR9y09gXMpu811_zUW4o8OudrtDCHIZQJqall9rxd4llvw2omCjEK4GCVejyCOnj5SO77H7_mje0m0lF3K2dYQlZvwZ4BHyUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ:
ایران حتی یک بار هم به ترکیه حمله کرد. من هرگز نفهمیدم. هیچ کس قرار نیست بفهمد.
مشکل این است. آنها افرادی کاملاً غیرمنطقی هستند و این افراد اکنون رفته‌اند.
من فکر می‌کنم ایران اکنون رهبری منطقی دارد
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66287" target="_blank">📅 14:30 · 26 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
