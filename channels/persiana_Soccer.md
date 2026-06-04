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
<img src="https://cdn4.telesco.pe/file/nzACfbbfWWuyfUW4wktyxUZfm78Pu0BAtQnk6gccbfvKiWAVG85Eh0sJolt7qcdkfMJv2iARB8jX8xLN9wbjgri89-X9pzMcDub6u2T_tbN7gaA6KxJlDUFw7MXQMvbnmbY-hfJBUx7pR5GB8kSAUrtfpBl-MsXmNtk9tBkXAkWZSz0H3KUM1q2XkFD5r-xfYkSP0yUUc_3N-KWzQxO8-2OoVuKfQ_FErAVcJLvjk9GDVo6PzO740p9t3mKXbmyjFNZplS_iHiSOvK1SX8-YZLeFmyl5Tx_vb0kxdgn2_G7lWXadQu8ndDBn8PRyPZln-0ShpflkeSK902EHNAwEVw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 174K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-15 00:38:51</div>
<hr>

<div class="tg-post" id="msg-22795">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqOKxXa9wVQV4jUaplZZcwONtW9a7Ur6MNCPFdrxdhyfpMYy7a6jQ-CT10f71aM1-5__OA-F5asQvS75EJHHTbLuIDjvVm3GC55zslo76iEueqZywbznTpsU2xEWbl1gHbkShPrcDzXAPzKeYdatq60Bc1UUPxiTc33yaqmNHXiOUUkKzFLIi_Y9IQ7riahW1ylpj8GXe031mmZkbxYZ4n-zaHXhj3JyAd-V1iR5on0dyPSszqzl534GAUFBvdsNfmSb-Z1UtDYddp-PEgZU6fiNWIv-HQuOIHFA0o2Q9Xz_YQBEUetJ48L2inUqOfFvQ3yXL82UAFDE_h7PMnq2wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#تکمیلی؛ نشریه کوپه: امشب فلورنتینو پرز میخواد یک خبر بسیار بزرگ رو اعلام کنه و ممکنه بسیاری از هواداران رئال مادرید سورپرایز بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/persiana_Soccer/22795" target="_blank">📅 00:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22794">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">⚽️
تیزر فوق‌خفن نایکی به مناسبت نزدیک شدن جام جهانی با حضور ستاره‌های فوتبال و سلبریتی ها
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/persiana_Soccer/22794" target="_blank">📅 00:19 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22793">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PosK5uF_ZQgheceuU1eNpupBbz-rN2axQMTgkCFPch0yNjCXTdwwfn38cRBXDER2cUp6VuY-gzBghl-F7IbesyCl-tHMa5WY5vELpAAXqy4j08RYoAWZ4Hq_5XK9nad_R0t7XZ4_s4YJu8pFDHvutuibOm06DLFfMDJPNsxzZvYZ6pOqVdT7Uv-kLfG5Tu1BQqyA6oKX2DivxxJDjx5sfbQ2NUqZFgJgNjdXNs6F1KYtNA-7PklcMKP5cRNcjhhfTLv_f7FjzG2TkGfeYGX_et5hKDd5dhb6DR5Iea-IiHNsyPU-_3SDKVqUfLcI_QFbY8oHMHCZTHd_-nygN0cswg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
با اعلام ایجنت مونیر الحدادی؛ ستاره مراکشی استقلال فصل‌آینده نیز دراین تیم موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/persiana_Soccer/22793" target="_blank">📅 00:14 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22792">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRwKK7UQD571U1lMhehBKOQiGQtOaLMioaLHVRd2iC2IbwtdPShBIUQQfxMuqCF5hxwK2c9-9QjWcDBItzSj_0WK_yxxO-eLwAyvNDbF6ATRchsjSGluA63g4lfmX21B43323H69AELVH1_UJ6kOPPnQx3HJtOOaFvvqjfvJKD7aMJVJ4FjkX-i0UY2IGNadiJqEIY8Q3J_DC0CUZ4hB6dxXaQuU3EJhBfoox5xbaAXmarqbxMt_XmUJOHWfBIsB-Q0fUFPmTBdFynqbyquQ2UHU_2lRmwIzTP1H5HWe_-boGC2ApXl_RKB3uN7d2e92sy1eQP81WSxdSkbst9bo1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
آموزش کامل بازگشایی شیکه‌های کارتی ماهواره که مسابقات جذاب جام جهانی رو پخش میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/persiana_Soccer/22792" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22791">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAalfEhbCeZ6i9ow-fkBBew_WLd_f5iZuAzAOkbsXESrDqUua7QJaYIUfavLyCmT858iaL55ZXG7ceeG5jIhoCUDuqFAYGwA913isF0OY4PQMuoGmapX0niz8V81PsPOPY8sJIPn0883VZB7pwm87LdI4QukPDRDhP_sQRApA7IdP9aQVxL0BRABVQIbYqy3L1m8jUF9q5Xeh1uNr0hmJrdnzQpFRY7w1ukGW737G8OBJCFmu-9OorVhRVBZwDEnaU33-AULKjdnjn0Lky1YdAPOfCfX5Mr5KkPA-ot4o2gh3ano4yIlwXudMn93zsv5wBIn2fk-0rfZVPhWOo_94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین تیم‌ های تاریخ رقابت‌های جام جهانی؛
برزیل با اختلاف در صدر جدول تاریخ این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22791" target="_blank">📅 22:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22789">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hV_xgvh28yPofX3yn8KECmBMd0R7i5_FUEhBKual_6jzpIxBDBBRts5OQ_uOsGZz4KMse4YtNbUS7r7vhxS_nz1-m6zEsKzP36p3nxrLcj1aYppp4Kgevi6f1j-AvtRqR4i2QkCZ8OdkKXWKLK4fw71Ypy27L15_wmF8YJiX4Mh8anKpKm7uKCI_fMetXLapd3lkXZI2FVl7CK1x6nU5vhnqyszIknI2zk-u_5ibUsjg4wJrTag9LcvZlQVLmvaUwdAWU1YZKN2z37Q_yQHmlbn47CJsAPZFt__zdw1BPUT3GhFg0P1ZaZAqOIUQM_8hOvjj3hDj28UbWXSCJY9ofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/psAJW9UY_zIOVe75PNnVDHD0dM8yBterz2emVX3awoO94GlrYW65dRpZ1C9NnS__FX6HYuZir52UZLGvsgtFvNiZtyS7-74aMfZoRUQmRi4JhC7El-wG7nNYM-FWjVN4c4s9J5ipC7bWQn-hiXEYpZjXpRVm-0ZdRhbV6Ekat0sGsW9UfAo8h4rf3QmLoc1wa31T7lcrbN8Fq1RoMt0mfSgOfg54-W6KFTkWZAIwKEswdeR-yqqWiGAaFxwZtGnTCE_-RMm8fI0Y8Aq9rI9GSu0Ta2z3pwONpfHCYp0lq3-qiEy4YA5DBm7twE6ShfOjuRvbKde4Ry0MY7yoxIw0cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بااعلام رومانو: آندونی ایرائولا سرمربی 43 ساله اسپانیایی با عقد قراردادی 3 ساله رسما بعنوان سرمربی جدید باشگاه لیورپول انگلیس انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22789" target="_blank">📅 22:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22786">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31e7361d2f.mp4?token=RyR-qQjJ0AmS0k5i4KubuOEbd-R6B7HUjXeazwl2MmTeOYv8a0nvlxBUtKfcorHlnsQqN5C9ZfBwXsssOd_3BMI-IHTMgHC855grjrZU7LmjS3jcN-mjNayWo2_FT40-6DfrRtPac9ouT0SAT6FqhCz3IIoGyMCJQg2LkpME5JjjFFzG0zQCbFn_RZUHHZWqBjmeXNxKjeYWAkGJkLT0l5kBJkasfol_d4Or8WH905KLPpycyQQelDfMvZrDm62LOX-ibK3RQ995WUTle7iCIvJ-MCe7GrJzOEMMzVkIBPYzPEJ5MpMD4VGg2Q42iuLqTqkFfptozD-pISVRzcNRcK6M_DLWexg4rakRLAiTqoNu1KKGuaKitGc-THj3lEkNAhgPv5Z6sveTNF_vOu9q5WQb6txuK5-1qlMy16pWCIFtFyaxk0Ep7X7x19qLpFyYQU-AmbW-FSbfimW7pEkJ9EQ42vPdZeegQCeLyDoonDIAsZoEDzgLPIYr7izJ645hYDHLEdq9J5z8TCt65Qtb_PzWcFbcIxadm1Cz2vkR1V3tZ8XEGyzty2Svh4qGx6UtY2PcnYfF-n16WLM7pWMJe1ZddOgw8SQtoC2NCzwjDk842G9-Kz6mRXcIUjmkaJj7VOktkJuaP-ALtXTHd5sSPYNlM-0JuuTzyov5EW103bI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
بمناسبت شروع رقابت های جام جهانی؛
بخشی از صحبت‌های شکیرا خواننده مطرح این مسابقات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/22786" target="_blank">📅 21:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22785">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d39ef7da3.mp4?token=uUpkaqHsKnEz6ybvuMpuMK4DgUesJX2TMa6pRzxjYYsvpE72LwzL58_yxuKzTswZD96nziCoxeYPW8PvIDjm-MSQIki64rtzu7muVRBoTeU7Z_dSaa1MEjIddmRgX36yJ9TRH9dyWCTshF6v5nd-m65obrlwvxofrHtvI6IB0IqqrTlcPt7o6iUXjyrNlXmloTLu3uzI0Yy2TrVYOkR6REXN_AFYZUJPVH6EkvFB8fXne5aGE9rBjx7F-tIL47onVdStRG41vVw_urCEgiZBp9MCdYVCeSriNrtJcm1awlN5dsX2iI6FmxGq2ORoRN-rRa-U4WcEqX6lBUPZonVc_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
جمله‌ای که تمام راه‌های فرار رو بست؛
فکر کنم‌مهدی‌طارمی هم‌این‌ویدیو رو دیده بود که جوگیر شد و به میلاد محمدی گفت بره مقابل تیم ازبکستان پنالتی بزنه، که البته اون پنالتی‌اش رو خراب کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/22785" target="_blank">📅 21:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22784">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twFbsX-Y5X7TwrYtV1qyNLJ3ve9cn7fBh_kRb7bvjy-AtUqrke_XG0y4SuelruO40CVzeVA80naXUO9HQWFUVB8vn5oPqQTpZA9j9XNfTDlE3p0Af7kxRgKX8iFlBqIzf9irqeYECYSh2VipctJZkUpASMoUg50gjdPDMwxOKpX19Hz22e0IhvUpLE3LfNKmexob2jaRoXPg81duAs_ypCgcPiYSfXRmrtVFlhHpSSQlaDll3JPrdqIETW_6T2OE5eCuJ9xsl1pZiNn4GS3GNtThoy70HxknQIhhIYy5iDQ2oYyfw94bQRWD36QMr2ROp6y6g7jNR2UQiEXvVWPGhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22784" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22782">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hdQRm3WVc4YdJ14I6t-KfvFfX0w_vYhUi2SDLGJHHd5He0pgq4obzhNcJQaPkbRaNc2Hn2v8o63KDdEduOkH4XRlOgrHcRm_-fRGe_5vlpJ9dg5XvS3dGknJk8aS2w_uhzZAS4slFIwVfkwZhnXvK47WDMIWH7LYBrb5EG_YeXQa6qwwhSWP0DSdF7W6lFHa4qYYGZKHSfDmPwnwlxUW-b3tIa9CXrV8ZiR5DbllB9Mk8Tt76QyS7no2jESbq6yuCHWlaYnGUuXyZrJCa5OVuWvUw3fDdRNYcsRwPrbbuualtS0SgDz06EB7ZWAgHNp23iaKCjflDi8Ou_XhGHGgJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0agdOBIACggOh1nwVXtjoljW7TckiXApYzHLEZ_RFKHckYgklWt7upiHKmaGgyIRvK89C94B8OT9D1zxeTg2lhXKYsb-77c_B1QAUKaqZqESwe6xnGg5x4qTE5ZXqpJtvcfha1sD5NREwwEuk1WLPgqJ8PG4CCZLkFl-pBYh_gUaMOv7fe2I-xRheZJaJhaK3_W9Xtou9HCf5Lk5eF-GtBk5sR63Sg32VtsIRGCP6PaW9z_4f_MEcaSeCfsrUjYUwBzJflnrIIN2YXZCuWlx4w6hEITs7WyhC-wmwbTYs_n6JBUiZAAt3nePVrE3QVdNpBat_4eoHvWbibX6ooUZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22782" target="_blank">📅 21:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22781">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZyIzlqugKbMCXbNZE4v8VAXPZHzAmhHMw1KCeD0CY1I1YZ8lxDoZXrpYfELSQt6r-ddhDZto8Dt3XAgF3XUjMNdKJPPFUm8-8vsDIBA_1aHg6i2j--It96P6TR9soHTe4kR8JFJ9qsNIT5S07SUcwxauxH1Qv7xk8-ndnp_iRMK-bGZNjspOorOCYkTKHRBGVXDUXY0syIjjZgeE9BCZRU20vHiQR-69VgF0qu19ZCMS5m2AD6t9pwccNKYPZnZnVnSmSDuRoLp6RGh8a6x5UV7B5CLU36z8WE0vhfCvHzy4epkrCmhk_Pq1JGF2owk0kbGgev5aDeMnEAZUJwkWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇪🇸
تیم ملی اسپانیا امشب با این ترکیب پر ستاره در بازی دوستانه بمصاف عراق خواهند رفت؛ فدراسیون لاروخا ابتدا قصدداشت باایران بازی کنه اما بعد از قتل عام مردم در دی ماه پیشمون شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/22781" target="_blank">📅 21:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22780">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5xIOES4Dl6x47GMbgJsXpJ-7tlnBXNjoaOambanPARKfYWd-5k6WmsoRSe6GN7Bp8KfR2PWbkuSxt9z99xa81hihujBliV1Bt0OTYUnDi59bWnlfN6INyNHy0ITrpJMsN87UryIKBVJGke70cKtKvg1u24ObsSMXNDNhYaTjiKhyamKUWTEOS6EBP9wkzH8z-2bPENOiXq585kb7ts2s1Kie8Y33h9Xr9GnfpNyUhrR_g-dmoaWP5ApmmjjBb_td5F1tGdxwCAekyJ3bxXkpg7L6g3GxuPdRceZuY7WNhvn-gjEyy1I2O02ERuhygwQavsn0X4Kk0fZWp9_-eKC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ ادرسون سیلوا هافبک برزیلی 26 ساله آتالانتا با عقد قراردادی چهار ساله رسما به منچستر یونایتد پیوست و جانشین کاسمیرو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22780" target="_blank">📅 20:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22779">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⚽️
اسپید با انتشار آهنگ جدیدش برای جام جهانی، هیجان بزرگ‌ترین رویداد فوتبالی را با انرژی همیشگی خودش ترکیب کرده. اسپید که سال‌هاست عشق خود به فوتبال را به نمایش گذاشته، حالا با این ترک تلاش کرده بخشی از فضای جام جهانی را برای میلیون‌ ها طرفدارش زنده‌کند. پیج‌رسمی جام جهانی هم اعلام کرده که این اهنگ در آلبوم جام‌جهانی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/22779" target="_blank">📅 20:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22778">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdQhK1aFOrI1_aZYpaiur8-hN3icgTP8G99c7SufynRcegIkmWRg8askP1Muhp8GAGnB8LTZIWbxiDpb26bnVsHzgpw_m5GIQnA9S5g_UamlUgaJtXU8pH0THTdMtgm4KhHW2PUSe-EG4oI4oEatB8fFlHek8bW7-PV_WOj7ipT-DQyW5CnncTaSxA-D6dmv3FXKzImlAAXCb_KS7PI9tDLI4lzB7zm4lbJhdK1WzSijBQwX6cCSp0F8jcVjGrKSUQQCpy1E3SFJFtD5dHyWPV4Vr1uPlA22cNjniVCrte8TS2_o-RUOxaEYbdDY47sHYLwz5gqevnO0fqU4_u_f-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شوخی‌جالب‌روبرتو پیاتزا ایتالیایی با عرشیا به‌ نژاد: من 58 ساله‌هستم‌اما چربی‌خیلی‌کمتری از تو دارم!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/22778" target="_blank">📅 20:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22777">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPmbuE9xgkmQ9SmhDPYzctmTO86Tn-DGvWLlXm2qFuVroATyWk2MjTMOM9h0FVuMm5ASfrZm7VYRavso0MQrUo3Uq9mPlqA8tUnUltuss3KxEgD6p6hcc4P02mTEJBL0mhvWrTGGV8vy6HOMMRLZp8qN7GRjUnVDvb4q2KYbGaPLToYJnN9bqDRcJy7I9mheMF8tEkzHPK48NZdnl4mfyy1CNRDCreMgERDj5c1f8n_xyrozOaJqNbTxJbbCh8_yJdj-nlhbx-DO_o3xc2aVy3I8rlLWmWufqaF23QNFVS3QIUEUn8pN0QtKYNaurefy6EnXDOPZM9uXhw9OxLImkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22777" target="_blank">📅 19:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22776">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nXWta7Eb7QPokg6GKVPHy0jFojaaEViiDpG3mNZuRHa-nKmA35rFAjOaq4nUIpR141db5DHDEbrqi_gqet0jaPlPesWUHDNv31TdPESYSJ828a98-0Eb4P4OTn0NhrcqUYkssGfcaLjFSOs17UweE1YxAksTKkZ9rnBlBlSRdHBqRrWYpnvE39t4_z3HjqWuXwBO_slNFYCxobPwvvcL8rpARoWYPqtuX7i-V9I0FIDsVjfUdn8tNGntufK1QjlLRzd4OEJhCZ3by7KizDm0BJe3QRZz0DlU5TMJiaN6_NMT-scdVzZYBWGmJk_1vZxepHFdTMKrWb4RYJBuIsvEYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ فیفا تا 15 روز آینده در مورد باز یا بسته بودن پنجره نقل‌وانتقالات‌تابستانی‌باشگاه استقلال جواب استعلام آبی ها رو خواهد داد. وکیل‌جدید و ایتالیایی که علی تاجرنیا استخدام‌کرده به او قول داده به هر شکلی که شده رضایت‌شاکیان‌وفیفا…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/persiana_Soccer/22776" target="_blank">📅 18:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22775">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrvMj5UeRheQaXP1yU03qA5Yy4_T8NY1H8Q046UuwFjG-wyaoIRKBLh9ZgSV5lWRc6WWzAQjAApS__FSEaE7fn1danME-IaQSgo0ssA_adY-9DPVUCYczVuloJHx63LNFKI9T4g1GiWUOI7cUBp0S6qy3bTHT_VY7eRONPaNF0vC4bpl8i77I83V8Zkrw37FhqNJ2qzjX5bsd-7zUEyIlTFauIfYOs7GHKMWAIbl1qsZGbl07haHP_JMapNku-p7lIl48cAUptj2x-a2efVWCHfxIsPEWX8qr073wmlubPawfZFAxAFxE150bTnEFavto6WWBM4omZp3Jo4Ia8AMbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/22775" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22774">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2zXmYv4UNtVEVlNhs7y2epldHE7SvdkJ-RzVXBtb6UnYpSciEwg4jPaGRiQ7ldKeXDe7Fa7IaAH8Y0lDGYhd2XVa5o5om087yzOU-loOtdo4XVfVjtHKDguBa0jpSd_Uifcv4ADwF94P46K815bnXL34AKCjJn8hEkTa2hkzLge9ug3Pt874L23y3sw2JXC2Vw98B_Eabf-4Iy8Sfa3hwyd6SPyEKWCarhx-j6iBKXl74Tff5V7OagExX8fVpi0ubsDQhnE1dSOPy7js-fgomlAms5wmn9taifH-VIAQRFb5eEBpEqHa0PgaEv-ulOOzdW1WUSAU4rEYHi92iSXBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22774" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22773">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcZR0u8nTo_tmX9BxagFy2VNmiBjC9RuBxOhyPKDYjHq29SRPzw8ek3n_vJWi52HFtWoD3D37rRvJzOwKvuuAZLxxSWvYNBrJVzRhSqSObdzp7g6zepGw6KD595V_BQqHbptD7D0260Z7ukq9GlqUYo5pxIUggHA0U2q9ucxfu_iBR02rbtose9c2ANiz3EptvFn4IWUF4ZHhIgAdGQZsOt3jDBrEO3Ezt6GVa6sHhuT3rIGVUGssgUKt2JxJgJ2go7tF7Oj23xDxK75N5IYYz7h5pWlt7GiHOVjnwn9RBWsqDO3lcXbxFcnPtIa7YvRXueP_rZnygprJ6fCxU_vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💳
در
#رومابت
میتوانید با کارت بانکی ایران انواع ووچر و همچین‌انواع ارزهای رایج حسابتون را شارژ و برداشت کنید
✅
🎁
10% بونوس برای شارژ با رمز ارز
💰
10% کش بک روی تیم محبوبت
💰
100% بونوس خوشامدگویی
🎁
20% کش بک بازی های کازینویی و انفجار
🔥
پلن وفاداری همراه با کش بک بی نظیر
#RomaBet
📣
‌
#بدون_احراز_هویت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
14
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/22773" target="_blank">📅 18:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22772">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c00997812.mp4?token=M1lfS6KbeL0vbcKz5HAR1YCW6PMKGvchMeTBm6ancwsf-_q58-WirQeiR3ixXmkF4pxZo-LTNLmDoAsfsYLBFnOBnhCM_lBn0drsATMpBjkCNqluI29xNL0DDf7oJdLRFBT8Pv0yb7Syly0IUIS_NdbNE1KK7mkmau00YCXlgBX6j_T6unpYJto6KN-hROYGr8s8XQPxgZBgPJWZmAzZxfsenogkUVEWlXiG9-BxilbysrpVN39_oEP7xo8CcrXw113INJPdQzfK3hyfwHRvdV7RXhJ6qCcWMlWJvzTozUwrO-SRhEyyV7NXR5WbBnf7x9XgsYZ19o7A6u5sAN64mC8VqF2jV-ocrTsYPUWrB6ysHhoV0Ta3bYtPccbyysI9oh6VblsTGGa9Vzui-PkBtC1Jq2zCGJkE73dqzoIKM6ngRJ8_fD6J2fi1fDx2ypxn7wGKWvDYNMfTfHtQ_X1n2h_JLo_nE41RBLZE4h6U4C-3IEkeCMwoqCDDYPzOZqmBD4PNBXo9CNsLDgxUlqAxDDpRD_dvM3ZxHXyoVhNu-0OpQyMUmrXD0f_-6Q1eaIbYPaehBpx4Z5rvCokSseahykf572qwKbN4v3FmOSQeURRBPpYe1-E8fKWhP3jXbETVeYNG7F44VAjh68NVySJ_NSik_P-UG3nrjvLa7iOa2zk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
ترکیه پس از ۲۴ سال بار دیگر به جام جهانی باز می‌گردد؛ تیمی‌که با تکیه بر نسل جدیدی از بازیکنان مستعد، از جمله نان ییلدیز یووه و آردا گولر، هافبک رئال مادرید و با خاطره شیرین صعود به نیمه‌نهایی جام جهانی ۲۰۰۲، وارد این رقابت‌ها می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/22772" target="_blank">📅 17:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22771">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwGUspRx7xEsO2AjvO_frLWkiKG0m0tul-Au72gagZ0Md-uY1rcahjISIbhQ4i_8r9kR_CK6oBHAMr0SYd_vDMjNJYadOUF3wNgOiJ3uk3zH1ZtUGvA5ra8YfLbK67_pCGbrxXebPsl9Lh27gOYDfxtFPCdEdQmTT47Xl_Avwnp11PTJHkZXsbMuaLOPv-c3swkyNMotaL6i5HJz5WgEi8OeugaAZzwQiPHcgrsH4vzrxtoZMwHLnHlvUmfmxy7ZMo3Cee4YGpG8OjpfEP8WKt0lvES8fD8xilGdxv6jRCpZRrwY30Fh1Pj0GYUB37Z5_HM_pMwCw-bAAoENDmc3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22771" target="_blank">📅 17:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22770">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10d92766a1.mp4?token=cPVjOy_BvUU2Bzeo2zPMZBVw-yWE3UeLMOXvslRu3XmZMX6_smFrtybMH984rzUzasahvsttP7zdY0oudewMiNz46Jeg16geuKg23wEEbdGwhA1G4P6RO49NIGxYC--a4tgTWKptZHggINyenV3ARtIQbTyRbxEWEKDOThArFK4cfX2bpOQU3bl1EyuIBjijGNLNrt2nHBUyaIu_-DiwOwltM5N9aRWAWdjCy0AfDUAslQsz5GlAiPxoBQQz6QKgkV7Z6inf-bxgA01QyR4TYOQgw1l3yW8QCu0-ZQl_M7Z8T15V3qxbzqxam8cICblLXZUAKLGpQkEI6IeQ7x2Id2_1q4fkvrxmi8yn0zlc20IzjTOHcdJZe2beE7Pdj84YBX4sjB0cNyoDR38NyBc1rLEzMYCOCLECnUG0vpq5Zs06QpeebkV_4rmWi8OoAg8EyW1F8RnoplPGu9jJDs9JI5dR0_8gMHC2TltTNWmFoTak5J19AHeG-VrEFJBFwZm1-veCr0KBFG-Wf8tVsDsa95dDVrq7U_hQgiaqDuJn5oO72drjPZpBKTUpwuh2v8huiFObkUQ5Mlyv6o2-qntxqkZMoYC_Z7z-8bH2LgR7EatJu6HvSuVqMpW1QoDXPMbnF8vC6OSR1L0HbGVuQRaEKfLQBba6sr3NEx_Pj9DP9YE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
مهدی تاتار سرمربی گل‌گهرسیرجان از طریق دوستان نزدیک‌خود درباشگاه پرسپولیس اعلام کرده درصورتی‌که اوسمار ویرا از این تیم جدا شود حاضر است از گل‌گهرجداشود و راهی تیم محبوبش شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22770" target="_blank">📅 17:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22769">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQmt-KCO99QsYt_WmYdsrBwjF0-j-bD7h1X9xav2-dWOnVkTmIN-91HW0Jet9k5DH-4gV7tOKKFLCOUQjRqxKtIZA3t01hSmZehjl_nV8fIOlcGni8kQqFh2Gl4PJtEpnjon2WHlhj9wNqE-Nf7R4-ckYn6rTuhaJHWhDi8U5sQCmNqX_AfLbIEPS6OS4Pc47KX4timMLCxczETCZgo2zkqxacVgiS7vodBMHPbNlE1c5HS3u7F_RxOpp1TdUFAZF11LXYD9rsPS0BBa4BEf4RF-MEhXZ3SQcgOP19DtFq-K5xedweyQDm46L_Q3eHzCl8xKKJU9tKovM-EZ8xGXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22769" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22768">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Brajad58XsQu_voyhH4E0enBj8jp34PbnLK_fB1qV6U5aHOeHZ5x9sL7tHVPxNk5JYdTn6aIF9JEAb6KBWruy2RErIyEQSrvMK9pYH28UqHjwh2ezo0Tg5qNlQ_p1uZgpVeK9r-tHKtZUS7Yff5fRq3O32mTsoqyLX7vT81G20A7X0EIvh02bboOgHcTVTqZKJKf9XWnth4ZLUd8HQlggUMwRlEcdeMA9mRe_ccVeXIAIay8Ryxb8obVHHxU5pUHxOPQU4nfxc-ue5cdewj-zioP9QWp1DrlRnrj_Lzj6RUSxij9-ChNRjB-mWNEgcsdsjq6xmilKBlJ3QuRSHs-0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
یاسر آسانی ستاره‌آلبانیایی 30 ساله استقلال شب گذشته بدلیل‌عدم‌پرداخت‌حدود 3 ماه مطالباتش به‌باشگاه خود نویس ارسال کرد. هلدینگ قول داده تا 72 ساعت آینده 250  هزار دلار به او پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22768" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22767">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q3QuBfFAldHVQbNf-cNoQEqhmeD1PyhX4cBMUgmqzF5vM4cUpgK4vQtr0XqsH5FBwefbEPWWM7dUpjkFb5fGZ3vOihQ-8RHKdvBmJJ6zoYTgtb-dwGgjeWNUhOMLwcG9BN1fSd5WHVzmMV7uxYGmEXNNX2xMxTZFu0RthBtt6QpgKr-0x-_L7sRFvDQMo2YwyCx3G1cnRwBXRmnhJ32pDx8ykFseFxgsO38at67VueOfLY8Er71ZJba_eq47EMg-6t-vxDQhxIIGZarPqo_OFVykMH7dvtAYU8aWygHFaXSsM9qfbqGapxAUwmZDxyHcsrzXzTX7fq2jTwgPDhn-Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22767" target="_blank">📅 15:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22766">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCcO3RAWfbm7nd2K6_1nzAyJiT__4qQWedLxb3MUXkVoqP8RFnoRCip8kpXpxk62B12uQwm8p5qZO_FdTu-ARPnY88UeMgr7UW-IN6flcXoMHH85RYN84o4aYMroXBpqt8NgSPNsnHEYkrKOn71zDOhaZd4QwAH7Q7BlmK4MwGWm_Smmsi0z9BTkHuHTENFQuChbcIMVWcX5VncTat_QRl72isBjejxBr3vMRTpFA2zCQcUyLNpATNBf7NiJCwMMt_h8jqF3cO04N0Rhk7OjAYFeROft54mAzzoWVftyZ-KbxjBQlqBKTuQ0b6uGmttsCJGAv0GSTyyuKPnwRwfqkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
علاوه‌برجذب‌قطعی‌کوناته و دامفریس؛ ژائو نوس ستاره پاریسن ژرمن و یوشکو گواردیول ستاره خط دفاعی منچستر سیتی دو بازیکن دیگری هستند که هفته آینده فلورنتینو پرز بعدانتخاب‌شدن بعنوان ریاست باشگاه به تیم رئال مادرید خواهد آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22766" target="_blank">📅 15:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22765">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔵
مسابقه جالب بین کیلیان امباپه و نیمار جونیور زمانی که هردو در پاری سن ژرمن حضور داشتند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/22765" target="_blank">📅 15:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22764">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qshhBdHY3mFxrS-O2739Y_OhYUiuLZY3FRpCqklgSXIybw5xz8K_e7FhUZ0_i3ucA16bpyKcrjZg4oGLCDp_YIcAB4F57dtBV2PBsv2umuoyo6YYOZinQ-mjMMhENhKeDfmBh0fQNmXXTKlHvGEyEWRLfmDF1uHjCeczpacvStLfpccUQmRLfAxpZ_l_mf_QFMW_DPBh4BCGILLlxeLBw7AUNVLOPbqTor0PgGNRqdcbg3jrK4MZFSVmIzHYLFLZl4Cu4_3bTEcW-B07h7HnF5JmHw0_R2r_0wC1MEIgnku8LP3NHDAfeFVAvk3mep6Z8OSyLMhw6fUDr3bNNANkPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛فابریزیو رومانو درلایو اینستاگرامی خود: مایکل اولیسه ستاره فرانسوی بایرن دیگر هدف اصلی پرز برای تقویت خط حمله رئال مادرید است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22764" target="_blank">📅 15:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22763">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsElsNA9V7CFN2_D7p9Rx0q3xo2ibCxGzG_Gv3axFj2_bkd8rMRNg0q_5iJntNqOdb5WyVzyzWyNSKB3efJN_DuFDgyXagrb2TbUQaieq2Zx-oKJcp4z2JWGZ2GX-Oc59Nc-rblOye9RsfpX2XOeue0znSoJ2L-1XGNbhQe5HzTeei8TU-wXBcUiRjs0uHWsmKd6TRyvIf8xl3gPlkCc27M3Be6xHeX-d_7spde4A3VrWcGa4Tsa4tP66ulSGM6qAfw1iXhPt9_AcKHuf9hdFsZg2NfLYZsq5GmU63j3UtsOpdJKWQtzFUnlUkUC8YSg_eUajZOayVFShyM3VJalaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این چهره که زندگیِ سرشار از خوشبختی‌اش رو درکنار زن و بچه‌ش مشاهده می‌کنید، همین چند روز پیش برای دومین فصل متوالی تیمش قهرمان اروپا شد و خودشم یکی از بهترین فوتبالیست‌های جهانه. عامل موفقیتش هم نه مربیش بوده و نه همسرش، بلکه فتحعلی‌شاه بود با تصویب عهدنامه گلستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/22763" target="_blank">📅 14:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22762">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qXJY7nXhfLduGfduPaTBgxVjLVqoaC8LG_o5Q3eYLUxNL47dyBntYGpDAmIzN8V8WQL3hnW6UDY5_ERppSYqs0_1c3HAkrFToOQ7EVpgMzDEjh92kR2SlVouUx5bFDjh0mUXcNeZvG7m7MqQhuiQ5gVWrsUjvwQacsRIEjmpgWZCkqYg8hhO--EmaEg4I6m6Bb-TyDkw4OMYD8OJ3NyZ5l3vDj2bCs9-cnHfKejd9pD0bQeuuSkILb4mC8gPzA_waWPyUaIjRBMRRRs_HXNpboCqatqgH1xNHfo4kyn4NSreorTZOesMANOBXsaHT23jhGbn01vLAGmdQEeSRW6cGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
رسانه‌ معتبر اسپورت 4TV کرواسی: دراگان اسکوچیچ سرمربی سابق تراکتور از باشگاه استقلال تهران آفر رسمی دریافت کرده و احتمال بازگشت دوباره او به فوتبال ایران وجود دارد.
‼️
پ.ن: اکثر رسانه‌های‌کرواسی خبراز مذاکرات ابی ها با اسکوچیچ‌ میدهند امارسانه‌های حکومتی…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22762" target="_blank">📅 14:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22761">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5zh5S6T40BoQ6_xAA-uyy6bskTf8u3wdihExntiV4wMQBichMc7uMzIib4o6TnmtxpsRztVLpPEVyissX2CMLaVQreeNiOmxpsDJKnrvT40L8MCiam20GSjfEJruRFA-_9RYDVs56EU5LjX1E8lJcVJxYMz4bwpRAxkKkLdCfpCXuoYhRMoX32gu_9BoTqy_XtDNAuh3FjxUdijMQJ7t-wWxHTK8IEFZ5NXqMZaoTlNfj7lklIkUmOkvGJk97dhcuZpRlnodsRAU-AXoLPSbAFtHoz2svw3-OA_A-7C5gT59Kx9gY0QmQzKcZxOfG2bcVw5lBvt3a89rYzcF0mF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ سرمربی‌کروات، موفق‌وسابق‌تراکتور از طریق ایجنت ایرانی نزدیک‌به‌خودگفته درصورتیکه تکلیف مذاکرات جمهوری اسلامی با آمریکامشخص‌شود و دیگر جنگی رخ ندهد به قطعا لیگ برتر باز خواهد گشت و به آفر مدیران باشگاه استقلال پاسخ مثبت…</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/22761" target="_blank">📅 13:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22760">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKBVoUBmAUHj-mw6KeQBSjp4axi5xEOwYt-EZNBDa_I-fqBIhZ7eB0oThC0D6iiGKAyIbyoouW_aZKaZXTZAF8dx7DB21QJ3Qp_8rxxattI2YY5EHWxpoaliRQcEOor4LZeVGtLoa827VqJV35TsTvRcBfHQUgof0CI96zp9WMRGAYQcbpQ8R6ikYCABamM31OpOU2i2r0byZMPnskv9GMXoBQByQz5Mn26_4WPY2Tr7XYpE6Obj31x3lasQIEWKp9oxkRkgo-HKFQbOdteFygPkmzkI3eiXsjLkWRbr7Q0RzKCYNwvFve2A8Q_H74-Ti4enebarXZUcWAHP1PgLaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ اسکای اسپورت: ریکاردو کالافیوری درلیست خرید مورینیو و فلورنتینو پرز قرار داره و حتی مستقیما با او حرف زده و به زودی پروژه عقد قرارداد باستاره‌ایتالیایی آرسنال کلید خواهد خورد. کالافیوری خودش برای پیوستن به رئال اوکی داده.
‼️
پس تا حالا لیست بازیکنان…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/22760" target="_blank">📅 12:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22759">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyQNvHAGn7EtDGTvCexcHvbXmOy7D-p-cTiPEyZ6c4qqAwuKmsODZ1jPOlfaTchiKrqIWZNU4zTripJz6euLf_Ny4eQ8L5hsRvzLyNQe-MtrdLu4VfuJNByBPrU8_dTbtmODnzEUHi4jSRt2EqQuV491NCzAdno3HQz7jHnmhwaJhXYPGXJ9wgHh-o6gyHAKwjbTYigVYLi_PH9a0tZ-j3cIpR0wPMi99-9pqhNEJhbReWBkkmIujKqWtnshxXPWiUXV_i1GsBM2ct_Twyy5zsMTw3JOAko16oSeb_31uk1zlXDSoyWmSR-cdG36-8AcM1YdFTwK1SJG8JfCdxRhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باشگاه‌های رکورددار بیشترین بازیکن در رقابت های جام جهانی؛ منچسترسیتی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/22759" target="_blank">📅 12:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22758">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee451d1e8a.mp4?token=Oo9lrWavcUpljtup8Dn9kLA-gHMXNxYJPmr3HvAyO9CtNLofvZoURgm1ezF_1mkjJ0_SkXSf6Veyh8C01OBGT4NkQyKKCtXP7tO7LwFcxR5v9VOWer7hpZM5vQBrKuheuHJfyfC1LPd4EA4JiTQWjhUll0bCVdA6Ld0wU1d-jztzYNExd5ba6HWoNb2oYAXYUcXW1RpWmh4ptCGSCx7wF6p7vLQqyzpxuWN7DtKlEg9pts1YWPMcoIQcYD2MipbfpZbDtojRLhGlh2ZqaVBSWAWxEm5fWzwZQBYEw39EWbf9FIgQODau-0f7zjVqEXQOy5DZ8bBHFwTPIxJ9g2vnSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
تعدادی‌ازسوپرگل‌های این فصل آردا گولر در رئال مادرید؛ شلیک۶۸متری آردا گولر مقابل الچه، به عنوان بهترین‌گل‌فصل رقابت‌های لالیگا انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22758" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22757">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9TX1LHEZyjhPgVWJxTZQFdE95nuijtCOhHPKbsU9DdCUd6RKuQFbEN3baogCC26FDuSLDU3puLHzas9Z_pVlwNUDLVzTZH2bFkiR7xncpdb5GRkwZgkMyqyFE7AwiIE23bf3Z43E_QIEdtUyn-UItl6JU0E-qOY-blXR81xi2O5o4WHvigjkyp2_Iaxr-k8miKfjn0egs1qQ377HWWwyQa37jR3HNm2pxYPzeBF9YU9XNQwGEZJq6NXk-iYr-NpkhdBOrrsZDzXnTR1Vkl-xpYVoP3HAqXohAtliJMiHf74W9Xz3cKy2oW1wUG7wgw-4rNEqL_hs3jH_Iag6tcZUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22757" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22756">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrtF9nQNuU4HSqnZltANiyKGD8hysm0E6SK13uf2mRxbXd2nE84hcwzPd9lnYXviGcnyCNt6FiNWfBYaxQKq9ct9mjEdF7kiNEddARZcMasmZhjWhUBsOVuu2_mguaXsm5m87LiVqotOkIctDSSGAJ8hV4U5oDyUPb6ZVwewkZ4S0QHxUwoTHskUbm61wvmrktrKrM4KmNvu9H77u14ZFvLnhWxJNCKR4oqsvmSZqdjAmTE0guXeqAadO6OTzMJPi6_08LMBQmTBd6rajB8eCwAKWh9hWyvqC14Deap694yG8Vbx0QAf5FDKcedDITROHsOLsLIVYL-xUNEwmmYmJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یادآوری
؛شبکه‌های رایگان پخش جذاب مسابقات جام جهانی 2026 که از 21 خرداد استارت میخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/22756" target="_blank">📅 10:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22755">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuoioPIeykGZ1hY0jBvs6pwbPjWR3SKXvus1CnMZVKdS7lxUe1uWla8xidf9vFJd_yvE0xmYi-OyP-ongYgoRa-rlYXyBOUkaWwdrUBJlbNuyNGItfouathxSKnZOvQuoIa6TX11mWDxt2_t5jk4ATKIST0wlYWJWun6HAdY2IB_7ryKrZK6tw0lk2NoERcT7iLMHY52XHQGLhISi2lEN2zDW1FGIKBE-RB7k48OOUhcZBlXCLhFURTpNQ0_L35knT_MAEcF6vkBl_bn_dO2yrqFbeVXs_VFmHENy-4ZYhJNp4oxCGylQdfzjx-IQww5YCZFQNXU1JfZTgo1Q6pKJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال ایری مدافع‌میانی‌ذوب‌آهن‌که دو فصل گذشته بعنوان سرباز در ملوان بازی میکرد قراردادش با گاندو ها به پایان‌رسیده و بعداز جام جهانی بعنوان بازیکن آزاد میتواند راهی باشگاه جدیدش شود. ایری هم از استقلال و پرسپولیس پیشنهاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22755" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22754">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede7c22d43.mp4?token=Y_N-WFbDz5rMhy05zygG0rq5Bwe1gv15BE_vxhQdRvTc89_9Y6sEDEFICK1Cuds4_TbmgMAnRhZuf0OpfIKb3Ns2EBGVOuK48h5AXzwOnP1PiFgIZk-1hnx6gWCmtCcaeD4r7GhRpBIImOzNhUe-5EnIwHiGi24j-GkFYA70A2yx9HcUazGQLJoHT2hcpjVq6AGYmxij2CxlcdQt4HczpahEtPAYsXzgLbdxqxjNO0NOiknjBH5XUbpG9q-OrJdPF5d3z2ICeneiEF5B294p9WnGBWZCr82vda2Iz8WvDPCptNrHrQuOaAHBcPohxiZdvwHs22P94GyxYfgEF6FT1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
تکل‌فوق‌العاده‌مارکینیوش در فینال چمپونزلیگ ونجات PSG؛
ولی‌واقعا برام باورش سخته که فقط 32 سالشه، فکر میکردم نزدیک 15 20 ساله داریم بازیشو میبینیم حداقل‌تو ذهنم 38 39 سالش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/22754" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22753">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔺
بانس‌های فوق خفن مل‌بت
🔺
🫴
100 درصد پاداش اولین واریز
😀
100 درصد بانس یکشنبه ها
🎁
100 درصد بانس چهارشنبه ها
🔹
هر روز 1 چرخش گردونه 1 یورویی
😀
3 درصد باز پرداخت نقدی
😀
بانس شرط رایگان 30 دلاری
🎩
10 درصد باز پرداخت نقدی کازینو
🎆
بانس هدیه روز تولد
💵
و چندین بانس دیگر از جمله بانس خوش‌آمد گویی، بانس شرطبندی طولانی مدت، بانس 1750 یورویی کازینو و...
💰
هنگام ثبت‌نام با وارد کردن کد هدیه Sport100 بانس 100 دلاری رایگان دریافت کنید!
✅
معرفی سایت و اپلیکیشن مل‌بت
💛
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22753" target="_blank">📅 10:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22752">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUQFJ-9uuCqlLYfPEcp-7EH7zxFYj_7-IXB-5p-RDq9QiI-XBndH0FKOV0OsbLRkVakqKY5NTfFFS5lu8e80XnfSlzwzX2drNg0owNJwICfBtA2UCFvI_b5ccS-i0RhAg5XlRBGzXVtBxIqEGqMl46AnNkaIHkSxb9ZLowuzwfjlJRvCYwTVGMG0XrLA-wA2uR3sgG5CR7198KPLxcfLZ4jnnrMBAxnw7cWl-zu2X96BtYC3GEf9bKxjEjxe67uiouhYScB5l8pWA6gaU9Gs9tFSo6s0ZQX7RArbDhYchOLb37MSYca56aifk382QJ-EDzq1vpBIXDMAE06clzThLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
درسته برزیل از سال ۲۰۰۲ جام جهانی رو نبرده، اما همچنان پادشاهان بی‌چون‌وچرای این مسابقاته و با بیش از ۲۰ امتیاز در صدر جدول کلی قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22752" target="_blank">📅 09:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22751">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq9drA3_-JPZEsYSdwxL3qTL8kea2eLphzWhfZ23s2hE1BUOEyJrjENNYI2CM4vzICECvEtmdonso37fmcGXZkZf4fxFPfkhi_ksvpw9okdT-gBl7eg5jjChMuIxs7azpo62uem2EJmD83yw_kp1-TPoIt1wwhPFSoLg8dAwDrpY8E55iI3P1cH9YbGEwr5zNnakMWIm7TgUSPazcb3Mgrgs3h5soqOLxURrP2twchX-V3cWh0d-m83WemBgzSQ1uLrjKNu8jjYasaPpHAIII3bUd5-pU86LXHN7CkRqDmUvYL3Q2CJYU4J34aeO21T0ulssNsEbn9fNjmcYcArmsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جوان‌ترین سرمربیان جام جهانی 2026
؛ یولین ناگلزمن آلمانی‌ها با 38 سال سن جوان‌ترین سرمربی حاضر در رقابت‌های جام جهانی 2026 خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22751" target="_blank">📅 09:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22750">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vG8BDgO85I7UKQh0f44ousN_cCXiOFUMXBRz6QSqMjvYoE8ZETPLVPianmwYFtRVZkvVCmtE2xgMc11k4B8kjxHfT18PLkwkYHg5YguchKXqGxkOsvYQC4Y1VAmxUST3rwQFWwhBoGc7m6yHN82EvHSEKjbDlAQh7q4VpAVwsaWoo8FEV8OH4_wbzB9CsZC6jna5zA1M9WWcsaJgtkCWY1iIvBcd-Q_szw_Y4SomyrwhfuxIke0LsEEEv2ALiwGSgirHxO4gwpU31oCGWE64eKPdUs2M751RwYx8WWa1IUtgNHWOt8isPhq5ZeAOmamppCeANbWNnawuBpsw3Q2vVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22750" target="_blank">📅 09:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22749">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG_eGwxLOUdaUVBZMzM2kgf0W1O289OduMn8qtPOpRPG6TTsdzXTYIcpTShhHVK13Iwxkh5qu6NsbJYH9V9Bm6IVdAEwyvYmYqF2HSorjNJvvOuPmCKpst8Oo3IOkQETk5ULspKKnEgY5dSS2_w7TeSqs-mGzTbkWinPaMc6Dwwbz3OWLawsxw4aqj34xl02eY86lQURavZ45xVoSyRubb93sIS9Lle1FNuL0MO9jeU6rGonZa6eeuca-3OSP_mTBP1oW0cEyZHfdwOlrVF56bwMZ2NEOprK2d0hbF7pbkdPsyckMJJO6BbIZ33zsIjDKmihTvKmGiHfx5nsAdrhdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
فابریزیو رومانو: رئال‌مادرید مستقیما به ریکارو کالافیوری مدافع‌چپ خوش‌اتیه آرسنال تماس گرفته و میخواد این‌بازیکن‌ رو بدرخواست ژوزه مورینیو به خدمت بگیره. احتمال این انتقال‌جذاب‌بسیار بالاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/22749" target="_blank">📅 02:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22748">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bImS85j5OBQmk8LKQh2SxG8tzJnc68Gq0510faU0NRVDckX3WPehTTszzp4Bq2rhrf8bMqFITUOmD88hZtAZ_M9iEbLOppOdWI7CgBdWOuVtCZ-H2JII7w1rMxUu0Bbv2A0jdnXvbOxyxAT8H0xlfGnJhOA23IU1GPgfmuV4DjBP_Bo28JJH4Sj_9BH1kiRAu1Q95tVqWur4lY-jD7A5YvQFE5IBm3t_PuNEqJiiDmGs7Sf75PFQHtV0ZDDXUUEhQ7CdO9SyRRB1PD9tSulNn4tF-0iYhyGHuw0VklNHYyufc_CGZHzvsGRvm217T192s7STMz0WNJVFTljIsTn80w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/22748" target="_blank">📅 01:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22747">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjacaY3yNcYS6z5yucr0dhlzis53eUNU1PLpmxxfwLmCtl6m52WUDRsmTeuKrohWjhXJxaJ6DSqusltDDYdr8X_X6I6X191nHn-0xYd9OkvlAVJsI2MR-sjdXhsghbyxKQKQv9tjfarEYK0PVPyMfL1DGyGy9obJXhYBtZQ7G-blJeiBXgzxa0TwqtmOdF1OEoWgOa8IpUKcWPMMEsuv-7seA0VzR4Q3MvMvaezWiUYvj5RktSju-51iUZq8B1TyLaJ16UebuFUJlLNUyVT27Pl7XZRlD_15niJZ7L6hO2xqMJisIFyVM4EbHg8ZFp11CskwtVY_EksQKbg5KmGWaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ مدافع‌فرانسویی بالاخره به آرزویش رسید؛ ابراهیم کوناته مدافع‌میانی تیم ملی فرانسه با عقد قرار دادی چهار ساله به رئال مادرید پیوست.
‼️
کوناته در ژانویه خیلی تلاش کرد که با لیورپول توافق کنه و راهی رئال‌مادرید بشه که سران باشگاه انگلیسی اجازه ندادند…</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22747" target="_blank">📅 01:27 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22745">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekglw4KWN3DOThu0yXXFzcw8XnF8e-HBD-D1Qu4jE_tHMEvZ0x_wFkt0r3E2Puw_RupTye5IuQMCPHjV4hs3pQdr6FI--5LD2P5mN_Dtfu2P2WgMIb4Isti056jgRSRzGHWNA9oihTjeC3J-15yXrIllwwXQ24Zj1q-NjLpSdSVSQgVwLKVPrw1hOPNtT3JL9Sjpc3lH9mm9HfLPYpW-i8A0voYkNfFiBwF4UV9hbG2sgObue8LmnT78IQ0ZcYWoWFyErISHDCh8X2NbdNgg434dxAktPFAJIXO4tOcRxN_fN0HqGchhvvTlgHtuus0JP8y0vyNtCoxiDXAwiobXMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=imnpGkilWRf2CnMeWpNghEB7HISVFWJvqGHKwLJmrsh1Yv9yVAvX_Vm-LKfY1oXAb5rJ7GG7azrxfXmjQZXd4c2rCavdPp8YZlFJ0kvvlEUg-AQJVHy3XOvJike7GhfELwLtw8FU78a4KalZS2i1NT0DYbB5Nq3az6bFjBh95P2PUpT8nubCgMZ3qPEjkALXHnTIc6z9aK02z3lru3tzxw0exUo0P0Cg7rWKa92CSj4_RE0_KjeeGdKqnEZMrDhXda7LemH4jBCPoa99pKxIntPD9sSak0tgdxdOrb1tAHFnXpLec61PG73Xdw5StHXowloWzrzsXcNuo-PzC2MUhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a98b9e9ac.mp4?token=imnpGkilWRf2CnMeWpNghEB7HISVFWJvqGHKwLJmrsh1Yv9yVAvX_Vm-LKfY1oXAb5rJ7GG7azrxfXmjQZXd4c2rCavdPp8YZlFJ0kvvlEUg-AQJVHy3XOvJike7GhfELwLtw8FU78a4KalZS2i1NT0DYbB5Nq3az6bFjBh95P2PUpT8nubCgMZ3qPEjkALXHnTIc6z9aK02z3lru3tzxw0exUo0P0Cg7rWKa92CSj4_RE0_KjeeGdKqnEZMrDhXda7LemH4jBCPoa99pKxIntPD9sSak0tgdxdOrb1tAHFnXpLec61PG73Xdw5StHXowloWzrzsXcNuo-PzC2MUhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22745" target="_blank">📅 01:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22744">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2GvkU-jUZBkQkdtCy9hFgNyhjjLFMGF6vznxevYrNMEXBlxTf6f75Yw7QhWhVMWy97m89RONZrJvDPZLh53gVpXm54v6nqVzz-fQAgi_0DhVsac4zzRm8ZOb9HdwEPSe3Eb_hq-Pa7KCN239JqbvznFjoIsb_oLWh6Bs-g4yPSb5znj9WjbmT4qEduhjAcFz6T7WIBKHMTyVZqmdFSKMwyTYQohexfsk610X1oxFsPHxEWnajqqmPKoiNCcTTr0c3utWw8QoRAxhdUxc40awbcNGscgrwrhQvj9N68pjAtrbuTqB61jc8JVFLo22RyiuKquIccenmBkCd2PIb0Yvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ انریکه ریکلمه: درقرارداد ارلینگ هالند با منچستر سیتی بند فسخی وجود داره که بلافاصله بعداز انتخاب‌شدنم‌بعنوان رئیس باشگاه اون رو فعال میکنم. به تموم‌رئالی‌ها قول میدم رئیس بشم هالند و رودری دوستاره سیتی روبلافاصله رئالی خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/22744" target="_blank">📅 01:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22742">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTaAN1n33StPX0Fj_e1uMVrFnS6Y6K-2E0oJYSJg1DAZIaFGBl1ipNXKjVL3AFuBY_7mqQzQJ73ri-9fTG1n6Cl816exRpZPr_LoclDwL_iN2QIDuvZEXVBRbRYEaZV5yuAPU49ERnPBPM2LjfdTUm4xOX-PzGq0FSKz2T_NSYZHn10a_CF9Hu1jHpIp-1dFezonYHD99LiKPDLLTiHn7aUKUPB2GRJbqxtf3cgnHbEtPaCVdf9amaTUQOyChNCNgbEaOjfqxw2h9pbojb89d6pYtzjpi2jyYhwHM85FN9NEhjUAWUR_Z1r-_24mTgLn3kan7Hzs5wTvuGPVRdFmzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از بازی تیم امیر قلعه‌نویی با مالی تا مصاف عراقی‌ها با تیم دوم رنکینگ فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22742" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22741">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVmkeAfssHyy7iwyf6PZP1YJIHlqyU73DUV83YyhGqecHPEZMoy4uKqCNyz9bDIAfnkNdMgnwOUZT4XiAeFKdSJT6iKiarUl_uIrbHOjdUV3Fc62hOphJ9texGSA2SP-okDiosHtmL_jzzl8i3NVYP7xcZrgjmH0SM0P-LObywEv8TywEHE7q21gFIcVs4xsiyUeQ2EipqIjBWCRQxvwzeHNyTwl7l8AUDy--k-OD2ZeUIW1mFy9WkfSD65NJTJwiFt4TLpLTJ7eqq9ar8cmiOENVP8rCiLhjjNG4BjN6UMHg0Ldx8tDefhz1N07qG1RQ1O7xUF6nQUwZCFyKkROkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست سنگین نیوزیلند پیش از آغاز جام جهانی 2026 و باخت غیرمنتظره شاگردان کومان در دیداری دوستانه برابر الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/22741" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22740">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDxxyx0Hj9yQ-qFNiNZRV1Twzil1BatAUp854_PhiN5fK2DY2MTVoadVHpkzGo-f7oQDqAmqTxs42AD8kqzCpwMIz6z7VlRS1qOKjDO7xqMM2E1zZh0PhhyQNcH_6iyliOcyCuOKN6du7ke7ZLXBRHfSPXWLZ3aiE_7Z-P0qACTdiD2z2Qy7pH9CeOMyYGwhJnejruQ6glUMjHnd85tL_W4Tpjn6FYAuXxAqOjlmBIPfed4OYCCVnQemv4BnwbGFSOX5hNGC-FdDmDPebzDAsfT0TV5NT7nmPgipowqZp5YhkbKml6kBI2fealPeUYUpphCLrSY20khAtIz8W_2ABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/22740" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22739">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QVjkAujL-1Kelqf4mTwmxLAcr59kWVl1WQ3tqtvhQyDIZkvc6EkID-FP52h4bLs3gOH46lGICpZ8Z-Zo5meJkSGpHRuW-iJvHU9yysHT4_0Folgtx4w2hcBhDBPZ0Cf7Qjk7BIcXy3dJymLqx_glcqe3DykBRBrS6aaW-sS8vWmpjkwzp8U_ZUrYje04Dfq07y-PpV9wzmWU4OI_3UgBp9aWbvPt91acpKFUbbMXCSZJmgALRvhfOCLcW_3t_feFDzjn-CHHlMfHiuXGu9Ela3vT28YGCn9Zb_OANAaFn1vDW-oYnup4rZMHRqq5LRbUQmRimvQ1X-B93ei93TSZ7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛انریکه ریکلمه رقیب انتخاباتی پرز: اگه در انتخابات باشگاه پیروز شوم قول میدهم 72 ساعت بعدش با ارلینگ هالند قراردادی 5 ساله امضا خواهم کرد و فوق ستاره رو به برنابئو خواهم اورد.
‼️
همچنین‌سرمربی‌مدنظر من مورینیو نخواهد بود‌. همان مربی خواهد بود که همه…</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22739" target="_blank">📅 01:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22737">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2pSsvvY1BbveozI1rY4-85TovLqdiWfDzzY0fSAzatXn2ZmAvOxjTdBSJxhoez395i1Fzq8ZVHcKv8C1extcvQk9W821dOF2o_UtsEbMHTPuf-IkktjXxwXyaw0dUxBOwV79G7jZRMY1LgD3-XMvjftPJ0brmNH-o1cNPxXGZRl8rL9vrcgb4nHkrh0twdIar1JZ2xYR7i2G9giifihJp4DS4wwtv4ymf16lnmZAAmF8aQED6xbP7AHYa_gLW1NzvMaMeD89DIiyt3Tb4OBJI9YhyZvKpOwmF-zazvl5SD4ViuWSUeFu8wd6AQG-2GLhsRCHtawE215r0MCg-hx7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ 2+1 رونمایی رسمی باشگاه رئال مادرید درصورت‌پیروزی پرز درانتخابات روز یکشنبه هفته آینده. بجز این سه نفر پرز به آقای خاص قول داده بزودی چهار ستاره دیگر جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22737" target="_blank">📅 00:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22736">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1314be179f.mp4?token=Ok-gh1ZyD3ImPqhrzKnWk9E5lwfXozIVGaNDHv3d3sEf66pVetAtMCqA_6WnCZuxcWfEoR4v00Mb0iy3sBPARyozx41kp-t-vdWs-Gz29QDkjxeuDRBu1rsmsO_4Ha8lHf390EOCvo3sBKuJnBx2-BuDUZ7pfj4JcNR5jrm2IaKpIct_iBo7ce4aeYcnWemygzL5_zvE8G1V0J-ROYnDt0Ehlu2nCq-qU--JQ6HF29J6-xFuYaTyEC3fId-ux-a0v-rgGp5QM9o08z66An62AwyfU6X4EZnF_URoisufX-AVvuuRp2E9D3SE1tNbtsMfAMbDv0jqpIljjJK_Kga1lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1314be179f.mp4?token=Ok-gh1ZyD3ImPqhrzKnWk9E5lwfXozIVGaNDHv3d3sEf66pVetAtMCqA_6WnCZuxcWfEoR4v00Mb0iy3sBPARyozx41kp-t-vdWs-Gz29QDkjxeuDRBu1rsmsO_4Ha8lHf390EOCvo3sBKuJnBx2-BuDUZ7pfj4JcNR5jrm2IaKpIct_iBo7ce4aeYcnWemygzL5_zvE8G1V0J-ROYnDt0Ehlu2nCq-qU--JQ6HF29J6-xFuYaTyEC3fId-ux-a0v-rgGp5QM9o08z66An62AwyfU6X4EZnF_URoisufX-AVvuuRp2E9D3SE1tNbtsMfAMbDv0jqpIljjJK_Kga1lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
اسطوره‌آبی‌ها50ساله‌شد
؛فرهادمجیدی ستاره و سرمربی سابق‌استقلال وارد دهه 50 زندگی‌اش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/22736" target="_blank">📅 00:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=nNRwyoeGwlb5h4yTm7N7vuTr1XILeMjMe8tTImJHw1SpylApQLe-hrqDYUP__hH04s2OjDIif0udzbotChGW_DEt5FSGklKbZ-n0XJGXPhctOYnToUSVSP3VBCXIZp4BkddsP-KGSQQstVYi1FMq4QUHzSTtrM2eQQHqtVxtD0bZlAjBUvlU_I3wkgVtwwV-mCgzrC666Qb6_y2NJuuiDz6ghp4ETWbpN0S-SPFQ6vtes7jOg-wyCm0a498zamkmlq1zDPDnPakl1Y_V13kRBiX6Q_8X9dRKGa0dUG2dkafC2M_0POir4UlcY5-H8C7kLn0a9yUkC7FLAXnH25rJ0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d55442a50f.mp4?token=nNRwyoeGwlb5h4yTm7N7vuTr1XILeMjMe8tTImJHw1SpylApQLe-hrqDYUP__hH04s2OjDIif0udzbotChGW_DEt5FSGklKbZ-n0XJGXPhctOYnToUSVSP3VBCXIZp4BkddsP-KGSQQstVYi1FMq4QUHzSTtrM2eQQHqtVxtD0bZlAjBUvlU_I3wkgVtwwV-mCgzrC666Qb6_y2NJuuiDz6ghp4ETWbpN0S-SPFQ6vtes7jOg-wyCm0a498zamkmlq1zDPDnPakl1Y_V13kRBiX6Q_8X9dRKGa0dUG2dkafC2M_0POir4UlcY5-H8C7kLn0a9yUkC7FLAXnH25rJ0jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پیروزقربانی سرمربی‌فجرسپاسی:
امیر تتلو یک اهنگ داره اول تااخرش فحشه ولی خیلی خوبه. قبل هر بازی مهمی اونو چند بار برای خودم پخش میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22735" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA0dgg-r2lyKd525AX6QWpRDvhPDpfP_8WOwyKwsS2cOm98qyNTEij--yvm9WatFI9vXLSBACoiKBb_pSpxG8E--lpJsDJw3QMuczNK7ORXpB-U0mwqZgaR_avoB-ddwKYDEclcYOl2-xqlWd78mlb9z7XkNakq-nHryiv0JqkkWJGUH2pk3IfVc-cu7graBFSucMlCcaKL048cKyqQgUI68bBIITyEw6Vj5tbg_0poztI2OF9uWZ9UJn-UZYeI_91_-SiBbSXnitS8vBzk58m8Ae-fwVWuNZNAuKMZ2tuHre39MJVOJvJAtMisoO0ZQUBMpCdkeQbYrze70sdPVzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فکت‌های جالب از جام جهانی 2026:
1️⃣
۲۲ قهرمان جام‌ دراین دوره حضور دارند. حضور ۴۴۹ تیم‌مختلف‌از ۷۱ کشور جهان. ۳۵۷ بازیکن حداقل در یک دوره از جام جهانی‌های گذشته بازی کرده‌اند.
2️⃣
۸۹۱ بازیکن برای اولین بار حضور در جام جهانی را تجربه می‌کنند.»جوان‌ترین‌بازیکن: خیلبرتو مورا از مکزیک با ۱۷سال و ۲۴۰ روز سن.»«مسن‌ترین بازیکن: کریگ گوردون از اسکاتلند با ۴۳ سال و ۱۶۲ روز سن.
3️⃣
کشورهای کیپ‌ورد، جمهوری دموکراتیک کنگو، ساحل‌عاج،کوراسائو،سنگال و اروگوئه هیچ بازیکنی ازلیگ داخلی‌شان دعوت نشده است.» «۷ بازیکن با سن ۴۰ سال یا بالاتر.» «۲۲ بازیکن زیر ۲۰ سال.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22734" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2KT7MLlMFeopcYccwifk_Gbp125xmCn5fhxTfZS8ZM80mCZ-jF9Z6YpWFIMXWya2MXMrOIrD1koHXyShpdz6T7RoaU4ztFLY5xnNSDHJdNhsLh7pXsZQCi4wYMMTrn4r-XGcpS2e9zDueY88C5h05W8rNtIbPap-hemkL7GbpYYe6LuuZ9ONeTBuudS16O1ikxRTEMsEas17BAX_FTl5UPu0k5N1aNvZ7D8Qg_Mm6aonHnt2k1WlOaPFr68Wf407GJjOLuO7Yq7XakjxVxp-gZIV1d7n5HmJGcKL_2a3JZi268shXr6zK9I5KVGSE5ynYsT4or-Y0Zc9BI0m3e3JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد دنزل دامفریس با باشگاه رئال مادرید تا سال 2030 خواهد بود. او ساعاتی قبل تست های پزشکی باشگاه رئال مادرید رو با موفقیت گذرونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/22733" target="_blank">📅 23:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxjgeW8E7qtWMgQ1LB_RGA6yWIMVmci9ZV0Fo25xgRWU1VS5-gdSN37g6yIwURLRg9xIemt_KakGVdx6nJ0lJ_dOeZr3LUKjaF7C1FLyZLfQ_-EODcPr98v86PygjLpnAOx2nFX0ybnzZSIkeyhi-oh7K7TTiCEnJ2OB-mYqhp8vmjJUfhPJCL7DGaPTBJaF5muqlmYh3q2gt6dghIUQ0D8Esp7Oa_AHvn8qZ5rGqqZHiJRH5gfffUmmOM2N1Y0mk8P-_vvaxud5rQCgHox_ansHSsJL6N3DOapW2kwcEGCjGmHWmy-Z6Wbn4231ddOOEWpYZN_FGbDFwfV1O8Jnxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/22732" target="_blank">📅 23:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=OGBDv0FOQIBNIzkEStKEQTZzQp9XMekA4H2aC_3P32p8yRo5ZDuFe8H62TZDVWx9sJN-YIpitN7hwqxRhSxkdChgc0rMJ1pRCSlnsegNdASEMKI2rPq-NXfbU3zVL1_lbWMrx7ikXf9F0fNJA7IdJ_Ewb2M5F8yQ8-rmTwqTcOBw6dLSQJ6d0qEKNfD6UVGqda9K9IgcOZZ44R_J4gVDgSzOXE5VbG_3HaYyFgvgQZkwiv1lz8lt5CCq_tDh2kcCXBJ6GM3vGf19Gxn85N38qeCC9UoeCwInccInNJEZagy4PmR3Reay3h8agOnSui7nOq-5ApCjx_jd_AbCOEl5Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddc4505bc.mp4?token=OGBDv0FOQIBNIzkEStKEQTZzQp9XMekA4H2aC_3P32p8yRo5ZDuFe8H62TZDVWx9sJN-YIpitN7hwqxRhSxkdChgc0rMJ1pRCSlnsegNdASEMKI2rPq-NXfbU3zVL1_lbWMrx7ikXf9F0fNJA7IdJ_Ewb2M5F8yQ8-rmTwqTcOBw6dLSQJ6d0qEKNfD6UVGqda9K9IgcOZZ44R_J4gVDgSzOXE5VbG_3HaYyFgvgQZkwiv1lz8lt5CCq_tDh2kcCXBJ6GM3vGf19Gxn85N38qeCC9UoeCwInccInNJEZagy4PmR3Reay3h8agOnSui7nOq-5ApCjx_jd_AbCOEl5Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ژائو نوس ستاره‌تیم‌ملی‌پرتغال و باشگاه PSG که در 21 سالگی‌فوتبالیست‌حرفه‌ایه، 2 بار قهرمان UCL شده، میلیونره و با دختری که عاشقشه زندگی میکنه؛ برادر در داخل و بیرون زمین زندگی رو کاملا برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/22731" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oErOjhMRS1CCt4Q0c7UWfreuXEZNEczOi1K6-DRPdpsf9nuPzNhQ0xKM9sYTFvmiqyoxWQ73wfeVfRDe3ojXf5eLnVTJp6JKL1R7mWksMGssoCSQCYO2VR9-ljcpdQN7CZu_4G4cyU-PB-EmtJ_xthKXwiXBJSgtcGLnbbq2k64Nhf7GhcSjVRtUdY-FDzfD_VedSxVH5vy2Yhoc9nTRI-Z_UGpHOqUKKduhJq3S_Yw17hl--23aZ9Sjiy9vsfQNCK0MiGiP7JUO2pJgVbYuoN2yp3j_c4EvQisu9wqcaMKIboOWeZx2_qD-eyGzRYmK2ijQ2MT89U7ds9kNPPgcPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییرات‌جدید در‌قوانین‌فوتبال برای جام‌جهانی:
برای اوت و ضربه دروازه، شمارش معکوس 5 ثانیه‌ ای در نظر گرفته می‌شه. بازیکنانی که موقع درگیری دهانشون رو بپوشونن با کارت قرمز جریمه میشن.
تیم‌هایی که در اعتراض زمین‌مسابقه رو ترک کنن، با مجازات روبه‌رو میشن. بازیکنان مصدوم باید حداقل یک دقیقه بیرون از زمین تحت درمان قرار بگیرن.
وار اجازه داره که خطاهای رخ داده قبل از شروع مجدد بازی روی ضربات ایستگاهی رو بررسی کنه. VAR همچنین اجازه داره کارت زرد دوم اشتباه و تصمیمات نادرست مربوط به کرنرها رو اصلاح کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22730" target="_blank">📅 22:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLiqoiRf5OLj80LQ01EjbV2KB5cVmOv32Go5667x4PoPwfpKc8KHU9rmJ7e4jBWkTOSkklwscHephUESR9p7shGNCgbsbCa3wIcw0NTq_RMzpqDP06W3rSxa1seOXx8zyFXdrX2CS-pZ6137cJtw-iPuILJy7gtXgmIu9KXJHvNauhFU-_f3hFDUZlzW8Cyc2IiIUuWAimVfQ2WOTHqAx6yQD_H7O-KgBhTfBNbwvA5HiGlD1UkPBM8lPBQgNiWQb0oRNaGeugKpdF6Z64NAgjl7ZdRDnuTYxVaemQ9f0veTv1R6HaP1FS9JLWklGxtXT404U8olEXr7a9mklU4Acg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برسی دوپیشنهاد برناردو سیلوا ستاره پرتغالی:
🇪🇸
اتلتیکومادرید: تا سال 2029؛ سالانه 18M€
🇪🇸
بارسلونا: تا سال 2028؛ سالانه 8M€
‼️
ستاره تیم‌ملی پرتغال آفر بارسلونا رو قبول کرده و بزودی این انتقال به شکل رسمی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22729" target="_blank">📅 22:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22727">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFnBrkyG23-Kz6QLLL7iDI9boTI89-bfAGaoC7bhST54S1L3C5t9cRL_WLhoPZP1tEZQBYNYuLdjlACzwwedbvhRwLhExrZcY3zuXDVPpbDbO6mnXc3vXWJwqklCK2ivBuap4Z0yFkkUMdTha-BHcOh28mNgLLNOif1TwDkV7wKUnkuYvJ-7yVJLpub-ZIhp0xAHAhIc8GBfNmv4_XL3xTeDsG73JNj_tOEOOaUXwmlu51S5_KSCDe9rofjN_At1-YlCsT8k_SnRpJW1myLKbsVSCMnEmfGcM_SF04cOtBk8nBgSFXJgXCMrdp3rXCcC9kMj7dhaQzJP4psdrVwLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#فوری؛ دنزل دامفریس مدافع راست جدید رئال مادرید بزودی در تست‌های پزشکی کهکشانی‌ ها شرکت خواهد کرد و سپس باشگاه به شکل رسمی از او رونمایی خواهد کرد. رئال هم همچون بارسا خرید های پر تعدادی خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22727" target="_blank">📅 21:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22726">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTUOSKW_lqOBbZ-G9I5QjZEckugmrKl3DGLq-D8QhVHtaz0_72Z4Hv8TYno4gf7QifXpWFocAvWuZR_HneE_0H8zIv4MbVjJtLfI0um8I-pylk80odheQIYmyVD3IEP6Yrt6zUufEE-MUvGU6eja4H9CWYBPdDJ_e-pTQ5ALD8t8uyQbbUfmrkanJX-nEu4-JrWH0xri1e86AOUDAOWEqcnK84i8TNrxAY0STLC2tY-wQgF58_e27QJeZp13C5NI_KXpOQ0kbhbq-d_7t2Yk4-_if_icM-1BxmdPZ3ZmKAc-E-V32jmyL_grJDRDZLXcH0fwzyWNBuJ21qYbpw-lOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
طبق داده‌های سوفا‌اسکور، دیگو مارادونا در مجموع ادوارجام‌جهانی باکسب نمره ۹ در سال ۱۹۸۶ رکورددار تاریخ‌شده و‌ تاامروز هیچ بازیکنی نتونسته دریک‌دوره‌ازمسابقات چنین نمره‌ای رو بدست بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/22726" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22725">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCtNYgbUqBIkXL6zEebA6_OdUtITQy-fWIelkgLeQWnovcYo4go1K1IcCnhuvo9hSsdb_Swpzxh0GhVn3ieFowEPt5-QjwTYm9DCi3wwXmJRGcFom04FLdpPdbG0q1oGERnoeIpzZQlBPfddkJafeEtNVs6YK9vIx5jCsuVK0jUxnHFH2_AS388hSD9qP9vKv3WxdOUYN3aHa0djKIxvT-J5NdxskyGCcjPUm5mcvOYM3Pqr7gBc8-NS8rW23wqYiL1RTkcreNIdt7jPAMRvENYNX398wwWKr9z0c2du7vCux_2FJfV5xMUHaZePXku7wp_FEDsRUwJT-IsX2YlZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیوید اورنشتاین خبرنگار معتبر انگلیسی: دنزل دامفریس به احتمال‌بسیارزیاد بعداز انتخابات ریاست باشگاه رئال‌مادرید باسران این باشگاه مذاکرات نهایی رو انجام خواهد داد و راهی این تیم خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/22725" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">توپ ترایوندا آدیداس یکی از پیشرفته‌ترین توپ‌های دنیاست که فیفا برای جام جهانی ۲۰۲۶ انتخاب کرده. این توپ میتواند در هر ثانیه ۵۰۰ بار سرعت، جهت و چرخش توپ رامحاسبه‌کند و داده‌های خود را با اتاق VAR به اشتراک بگذارد.آدیداس‌معتقداست این توپ می‌تواند بادقت میلی‌متری و زودتراز داوران آفساید را تشخیص دهد و به سیستم تشخیص آفساید نیمه خودکار کمک شایانی کند. این توپ بدون سنسور در فروشگاه آدیداس با قیمت ۱۵۰ دلار بفروش میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/22724" target="_blank">📅 21:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22722">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXC1KjVBoUdzifj_u_DrKo1SUE7LyOZQg_KsWPEf9F1s1b_d4SZmvFX_-n9ytoAwR927NGmK_ugLPd_ROQQtdNfyuTgbyKEn0caQDmA-39DrySmJ4bzdd-72rU_C6rfksx3Qz5H_ezbXMBtrkyYrEXMzFNtVoF9j5RnxKB_xQ5BqHOh_c79FDl6aO4O6CzOcWL_ZNCtoYAH-l7fk_4chrkfuZnJspoyXSiiqqy_vNdkQiZZU0eOdYqwVfLjIgU71o8s47rKHuvOkbFYgTJo1CoAFP8lsHGv2Rb5b_KDEafm15qVmNUEpHuAY7zVmD9Tt0-3rk31HDDAnAoccZX0aLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
لوئیز فیگو اسطوره‌پرتغال:به‌جرات‌میتونم بگم که اسکواد این دوره تیم‌ملی‌پرتغال خوشبختانه‌ یکی از بهترین اسکواد های تاریخه که امیدوارم با کریس رونالدو بتونند به قهرمانی جام جهانی برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/22722" target="_blank">📅 20:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22721">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLeH_-Tf-pFg7VapFCREAvjkGypfkfDCtn3gyYof4xdRpcadLdw1q5YrQhvyeDeiMSmyNvzW3zh4B0MPratmA5P5dgSphkbi2OQznn-tXyzsMIplSSkHGt8KK5wLB7x09FjtYW5I3HAaKWDCm1PusXT8vbse-Jffnc40ee0O-OpUHS8KA_-yW5zbLQavzMl2O1wOggWRo3vg4wwsbuhb84QNmJAyO2RZeC5V2gl-HwosQQgLoT2HuMXRF3r-OrCvqzgl2VF2KnbW_iByij8c8r3L6YkP35k0NXMhyN_4sFp6vZBneLya5M6anta5n_QRSXpOkNi8q4alsdpNzrgLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛اتلتیک:انزو فرناندز ستاره چلسی به سران این باشگاه خبر داده که قطعی میخواهد در این تابستون از این تیم جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22721" target="_blank">📅 19:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22720">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LByHbBDGr9flbZI7lM7VV_0zMVdWL9ONjoWkv-qNgPqdHmC4FheHL7StwVtCCmqalZrgFxJQJtPlBfk8bzpe3-iExadEGulTgaFZf3ZtcRMifEx5p4PH7WKI67LrTmtUJ9HaOqaA4lJMlAeUEUhxnXWnJyXBykStDWuphc5lHhsuYhLXoz_pFOfZRlf8gIXwCmYDVcLdsM_clt3aQeY7U1lLoivxDd-QxzPkRCJkOy_iOq42BjzDMqY2ajVpO4j_8A1c1V73bATkPE922wrbd6qpssRPrAsM9LdMJpO9dgixLY0P_h2iGAwTYuUEPWH3_EiiVHHP-rW3diBklyqYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌آمارمثلث‌هجومی PSG فصل 2025/26 و آمار لیونل مسی به تنهایی در فصل 2014/15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/22720" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22719">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS1k8G6sTqNARDRz8TGJXYWv7sEfF0L8me2y11rHmWxzpBXvWnJAusgrSMCkp_P0wxDyRv0R9UWSo-NSGdcDU5yJy59zGScL-rmWTLUYfocVmWNVlr728g9Y6ABRVaXw290YblNz3p3-8Oje_wqGqjAnQO7I0xHxeSshbSjBvIAITF_FbR-TOcGsQopR-9St20COQVSfYyiZWcHQOqz1gbcBnoCl3Z8t3IQz9CVSwsi1qT_BbY--qgpVyWi7IzeFH40eB277THr-Z0EU72S7DIZ_TOER7JdB4xcuoILm2sffV_ZWjJIbYPe1l8xtBTmvBI6wetqCXWOTvxpxYixLSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22719" target="_blank">📅 18:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22718">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2qPZbQ9Fof4Zdf02947GSjkSOR0vaM3_ozfsV2WBjbHLPAXW71WRtMbW9te6y4AVn6D80ie0R3GdbCy3gSm7UVxERZeRR0dN7vHJXxqm7emjA2R4J3lNyPQw7AecUQCOORJ3Qs0KwIpKBvOuVW7c-mbtb5wu1YIeCP8wwfgb1ymgrDzbCbbWoEttw-iSPbRJ654ytrvw4VkYJO0u9DkCONT-9nLSuiYvx_XsZ7R1shKwFnvpXVXDp3qyzgHwQHnpxFrQ099Kt4RG83wHYSuPQWYhjRr1R4xSHnJfFaT8-A_WtDESq5BDGAqCnYbmWvZ2dccJX94O7qLMd0-3pev4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
|با اعلام رومانو؛ دوشان ولاهوویچ از باشگاه یوونتوس جدا شد و قراردادش تمدید نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22718" target="_blank">📅 18:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22717">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiyK_Ovrh9eO99Tf8vDluwCBuuCaMqfxGHgbra-5RqyfxXpT3bLNPX9WhBtRsYnPnAQJVq4hUVd1Ln9p2bIuyowUPUaA_QMc1ofC2z6Tix_klh-c2QHxvY-YpxLe2H86aZwMyWJzbCEXmAN222xGwTWPMINEvoYjYLxsAUMNgqGj1O2psHNS1cx5mOYYBhTbPs8ufrsvcjYx0iHBpFSlPLG8iYdKZNidPwC-ZbZ4jxJkJU2UbsUh-cM5NoHR2WtmdJaQQKCMq4OCQD4z7bQ8eU1_wfVqSpk5VER8vbGtu3KFBG3qn6KZe-ZCvrA92ZsluNZ7DZT6u9oyJr94pb8d5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپورت عراق با انتشار این پوستر؛ خبر از عقد قرارداد دو ساله یحیی گلمحمدی با دهوک عراق طی ساعات آینده داد. هنوز قرارداد رسمی امضا نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22717" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22715">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHtO4n6h1UcxnrQnCcuY78jixFjag7xYREZdN355xf0H4rVKS4SWPoi7b8cDjUjpfEfjPz90CeCxPeskPzkUygXZ-aLWMDAoGscthLfMvvAWanyMllbDDpMzgrnHfvjbEn7ukjS0vZJOImYffRINUZww79euGWdffsIMJDLIdWh9Y3qoH-abPKODN4ghqN_STvo888GVnyqAkHuzE2Fmlv8rFT4vm5d9gwfND6J_xQRpXfYF4a1CVb7MKDgC4th6JScBY0HDRAZxTPbaJM9MRhBQ7USi3F6PUX_N7V_xI_nK0xg2VZlrEHroST-6MKLltIr5L0Z_mDC4IqkTvlpCPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dLnKy2DKapdrsawQbFSWoUfdfUVU1cNg9UXn3VvZX-L5emGXaA-seIUFD-Sc7ZZVg5J0FGLyvCQKDBPBJs7vgK4uFObxf-XqWAuhY4YL2yAsqHQ7zcgJPFYy1DUvZlSzGxPxRUd8oW9icNDak7EwMRuiKYcCSpsxE7a8S2_scbozu6BZ30decLHCLdnf1cw0_AoNBF8P5MiEa4oxOvtIG_FxyVkaBKvemxCJW3rucTHEO-27SFazs-51zJmzDXDkH1gKFUQST8DoRXJ449z7km-jSt1icbrVF1OteHXl-8ZEj9UfrzPgbYzXr0B2rVEO966olaPMJOURZH1VB6Vsaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇿
🇮🇷
ترکیب احتمالی تیم ملی ازبکستان و تیم جمهوری اسلامی برای رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/22715" target="_blank">📅 17:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22714">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=V6ELIBPz1eivc1b4l2M_7wSVKHH10Fd6ivgOZlOOj4lmUKegNUT9kGPng3Hwf8V4SKjRZjfuj4vcFpFK6-jOFTJztYA_0avXhBdB_FQ9BNQwCBiTLhJOEvhFyhCCCo29GcfH7UNCJjdWNBbrKHb1Z115rJ54mQOgN04n92O9cG-j8meCukFGl2g15mvY5M9NmxdTdtcuh31KVcNq2Ia8rzNNPmb-4-NVQnkRVc1PLACuIl1Uj_e3fUAwEQE8EYaJIYUPh8jpJjWgsT2dPM3VXaM8Biq4N0JEVo-zXjA57FkdusS15HQFILunMe3DweWfZ4Eru8SKqnstEABP64BndYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e93182b0f.mp4?token=V6ELIBPz1eivc1b4l2M_7wSVKHH10Fd6ivgOZlOOj4lmUKegNUT9kGPng3Hwf8V4SKjRZjfuj4vcFpFK6-jOFTJztYA_0avXhBdB_FQ9BNQwCBiTLhJOEvhFyhCCCo29GcfH7UNCJjdWNBbrKHb1Z115rJ54mQOgN04n92O9cG-j8meCukFGl2g15mvY5M9NmxdTdtcuh31KVcNq2Ia8rzNNPmb-4-NVQnkRVc1PLACuIl1Uj_e3fUAwEQE8EYaJIYUPh8jpJjWgsT2dPM3VXaM8Biq4N0JEVo-zXjA57FkdusS15HQFILunMe3DweWfZ4Eru8SKqnstEABP64BndYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ازشوت‌های فوق تماشایی گرت بیل فوق ستاره سابق رئال مادرید در دوران حضور در تاتنهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/22714" target="_blank">📅 17:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22713">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8-EpX_5IIhGdtkcs-H_2QlCkZ1CBwLS6SyiLza6XY6p40FlRuA9_qqpiddp8OPK4_nUze4oOtu2isKvR_Vn9zNlK9jOC7VrHYceWP7XtCAw0PLwGemAjTfyNAk1PQGcSDgQ7Fm2CiNrzzmRN1SNnYTTA2NtT99m-aQCz4W3Hjiiqk8ZrzkhLxTq58JsbfwdBHeSeh0peSuSZZLKunw0cNZF8Nq6exrq12evbdj8nrxnsrht_7gpW2SExx3k75ZSaycELEvb28wUrt-XcsTEZG2Lj9wnh6mMCZnItjdUE9D0E8LQ2uxh8JX4SpTbsJXlFUvFbqiTCqZo02nEEKUdgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ یحیی گلمحمدی در روز های گذشته مذاکرات مثبتی رو با باشگاه عراقی خواهانش‌ داشته و حتی توافقات لازم بین طرفین انجام شده اما منتظره تا تکلیف نیمکت پرسپولیس برای فصل بعد رقابت ها رسما مشخص شودتا درصورتیکی بنا به‌هردلیلی‌اوسمار از…</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/22713" target="_blank">📅 16:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22712">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ay6T7o5THHD-zDteLbP4cVmpNmFlJpOHVPLhpB7prNOLkOK-iLmCbs0PZOS-V8D712kzAiJTA18rDf0gGL8wQx1wUlDfDcViXGV0ZTPF_CAfY56E_ojGJURbBad5Qn0VY2ZkZIcoSdZ6vF0rwANDjU2c6RE8Bl_-pj9krj0FRNVeFH4reWoHPrDAspvgp68irI-AzpQn3yi-cPJbAcQi08NMjL-zzU-wyIGqva2fVdEYP6K4MZh2_NtcQg-aMslSmWSB7iMQ-yG0QrPdWOkSYJQW-cpfoGLVMtghMxE1hj7_96fxaqerOfHCmCjwC3f1hGpQWJPqLurzWIUXG61dDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/22712" target="_blank">📅 16:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22711">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=p2adnb0y_8UMrv0pz6_pPvph_mD3hoA27f1mwe9ILtxsOKqBCoYfukTreFl-jlAamKUlmkeyQer-TBUL2sj_G_9UWxoK1mrVRfl_zelj0h2h77PeXG2qjrmL0CQeOrnGV33IU3LIz_F7TnOAsRKiHZ8VAMlD4vGeRXRsI8PV68l-n5Pr---3B2HwNHt3WWjXYvGYbH3jM9JVA-5mkXKs4LxDfdklfx4eK3KPJD3Wvfje8Gql9Gvc66kXqpObLcEnXE7flcf_xPWOA94pNG7bmN2FNvk19v5l84wbiE2Rq6QaRv6e4qBjFVnD1m3jnOPSno10I1fCGusBXReYv_SoqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6cb529dda.mp4?token=p2adnb0y_8UMrv0pz6_pPvph_mD3hoA27f1mwe9ILtxsOKqBCoYfukTreFl-jlAamKUlmkeyQer-TBUL2sj_G_9UWxoK1mrVRfl_zelj0h2h77PeXG2qjrmL0CQeOrnGV33IU3LIz_F7TnOAsRKiHZ8VAMlD4vGeRXRsI8PV68l-n5Pr---3B2HwNHt3WWjXYvGYbH3jM9JVA-5mkXKs4LxDfdklfx4eK3KPJD3Wvfje8Gql9Gvc66kXqpObLcEnXE7flcf_xPWOA94pNG7bmN2FNvk19v5l84wbiE2Rq6QaRv6e4qBjFVnD1m3jnOPSno10I1fCGusBXReYv_SoqYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
توپ فوتبالی مجهز به هوش مصنوعی که به تشخیص آفساید کمک میکند در جام جهانی استفاده خواهد شد. توپ رسمی مسابقه می‌تواند داده‌ها را با سرعت 500 بار در ثانیه ثبت کند، به این معنا که هر ضربه به توپ تحت نظارت قرار دارد.⁩
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/22711" target="_blank">📅 16:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22710">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4ia9u7AHRknAli0lIlIrwEO2UxXoB140-qgmuMm1An1gbALJeSX45r8FA-w_Py3_t_o1tGQhxhtpAdZLfnit6e8im5bRV5IcxKVxtQb7rfZpX1QrjrCzvstDQX4Py1sLKLtPf-lJ8UDohOTuMXEPg2XrLWBKPgB33ILtM98assjaSL8X1PKbyBUrkqIyCpqBLiTG0PH0IpfRUy6_PQUltVMNTXNUbGXCZQ2byQ1UXr5R6sn7GDQEcFyvZOQmXgN5CqrbdYgzxrxOJOE_ZIkrsN3CV-C-yAc2rbox7vhC6LcZJ0DmY9bkRhrCDUha2HnPCqXaczhFxPWZBEk245aZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
#فوری؛ بعداز توافق‌ نهایی با ابراهیم کوناته؛ هدف بعدی باشگاه رئال‌مادرید برای تقویت خط دفاعی این تیم، یوشکو گواردیول مدافع جوان منچستر سیتی است. پرز به مورینیو قول داده بعد انتخاب حداقل پنج خرید تاپ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/22710" target="_blank">📅 15:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22709">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwosDG0UJqerGA5AScWYjkm0xlBfts534xr0RnSYEwta9cTjLd_PZJvF414gWhLy7vsJjD9xFpXttdWRjPhKoUJjRNCdd__LuJUCbYDXFICkvxikOWYII7zNV7PQWjvr5-GdidWnR8J_0jJzAatpoujneiEjHLChEx2-3uDpk3nIaYe0fRK4C_iczfywk7qj0IZ-KT19FHyBnVg7km9Sr3SLg-7VrWD4Mw2e4yvP7Hpk7aJx61CNMWjlcQvTz0RyIl4GMNSkU0PunlPl6k1u7xpl3L4rcx7QxtnjiNzYJ2eSGtmuF6tvIiDNPMUtEK_ouNnaEPb2E6mhMaNqEfocBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باحضور دنیس‌وسامان‌از تیم جمهوری اسلامی؛
لیست کامل ۲۸۹ بازیکن در جام جهانی ۲۰۲۶ حاضرند وبرای کشوری بازی می‌کنند که در آن متولد نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22709" target="_blank">📅 15:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22708">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBNQS05VAUSXYSW8qFg4QQA_1KsJnTr5rJiW32nsgf38_-KxDUcceg7-EyQ6db6k389w6dV4QU9I7jaYk0wPqYb65fkVZoVhMRvcjYcOPcSNKTF-Op5zo0EgoKMtp5pq0u6PqYKLX6ORPFO1YKglfBpsnNCWvMUF2aXJ93NWcbsJEzkzfdqgfSzRRHgs8FTmXOMSncjKfQwhoPl8RkqW3r32XpOcAo54nAV7x5QEoCO-5jRa12vRsisWCX314lP6SH3dIK75vsMQW6X39FvwJBJDMfrUbTna236gSLjpF4IeZZWXU6Z2rPztqPsJNyWs3f99V6XBqs7HIbAXaxtpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار هری‌کین‌مهاجم بایرن‌ و عثمان دمبله مهاجم PSG در این فصل؛ کدومشون لایق توپ‌طلاعه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22708" target="_blank">📅 15:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22707">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSS08IQgL98pUcdPL3mqMEH6apX4BwCKrIVLdKYSFmrvMl8HzvIMQJwNQGZMJRxjKfjPICkV6gafTISuzwWbPMF91gorfr8XGsKXnivuqyb6N8BtoLsdPjs3rt9JjXUESmO87lMeMw4ICrTlrLXKW8PE64HGpC4ABDqYzA3b2eENyopCKtkWuWPiQZhPvVksjzwlv4PWMTxXBTck-4jN-tR7u17vQbZ0m5Q-tlbwSyhDIe911hArI5ermMD6dIt1N47Df-Hh60sSqmJqtVMha-_vbaOJ0jUR7nqs4QGmHvd5SYyWMZwGegpIweM8cT1E4W3XQgkFgnpW0PQ2PAtLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔵
راسمون هویلند: امیدوارم‌که باشگاه ناپولی در پایان فصل بندخریدقطعی من رو فعال کنه چون حقیقتا دیگه‌علاقه‌ای‌به‌بازگشت به اولترافورد ندارم. برای من بهترین بازیکن تاریخ کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/22707" target="_blank">📅 14:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22706">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgt2mmmIcTZ8fgb_Bm_2LSvbg8B-5glVnGxRMfhEUDg2mKQrFC8V85g44k4QpVRYsY5CXGSWVLWMDgtVscCN-6AkQPQDa6ydgNQFi6Ldu6rNOJlUAkpXJZ8YqmHY_gDQTA1jILp1oJEkMD4dsirUK0NDB2YYC4aZVbU_XoKykMx36LN-3pJPk338gwXcZ9n1DrKYZ5scpTRmfd6IRxCdEwJD1uH38UM-Sn-lynsV0dyt0fxWJ-JEGPRvKD7CIjl1lQxE3TZrtw-s-S5yrl8ZwgsXZ1GSYXhHto3yNT6ZUC_Cm5nVXVLop8Q44qMmeMNY-pfVRlRDrSbM1gxWFBMOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💣
#تکمیلی #فوری #اختصاصی_پرشیانا؛ یحیی گلمحمدی علاوه بر دوباشگاه‌عراقی؛ از باشگاه تراکتور تبریز آفر مالی بسیارسنگینی رو برای سه فصل حضور در تبریز دریافت‌کرده. مالک پرشورها قصد داره یحیی رو جانشین محمد ربیعی سرمربی فعلی این تیم کنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22706" target="_blank">📅 13:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22705">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=pdxJacgMXJLnhK-B_EZpOVaugLII9RyCt4XYMSZc6_ls34oZ9rTTRL9uevj_0IMgdmdgxL3ZyXNnuTVwXFTaLOC2AfxSH_dpSPXjeP_1uM8Di2eFoXYJ3yEHvMCuxkM4l8EYp50vc_1bvsNmQlaG9KwFCa6jQDp1CCX6UYRWai3yMnmZnnJM4bwZUscXesGq0_7P1-OfQS8SyQCSKd4A6ByCN6m6if5-UNstoiII2Yo0cuCV6E2P5TfCTdiR5Id5NPRswvkp9Yv57rAqK1Hw_KAFU_GAZIYL4IKKNCUyzI7SwOAe_4kjfcC34j9iF1vmirbiaFnFi84jOEqGJYOL6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e0818cf5.mp4?token=pdxJacgMXJLnhK-B_EZpOVaugLII9RyCt4XYMSZc6_ls34oZ9rTTRL9uevj_0IMgdmdgxL3ZyXNnuTVwXFTaLOC2AfxSH_dpSPXjeP_1uM8Di2eFoXYJ3yEHvMCuxkM4l8EYp50vc_1bvsNmQlaG9KwFCa6jQDp1CCX6UYRWai3yMnmZnnJM4bwZUscXesGq0_7P1-OfQS8SyQCSKd4A6ByCN6m6if5-UNstoiII2Yo0cuCV6E2P5TfCTdiR5Id5NPRswvkp9Yv57rAqK1Hw_KAFU_GAZIYL4IKKNCUyzI7SwOAe_4kjfcC34j9iF1vmirbiaFnFi84jOEqGJYOL6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تکل جسورانه تیاگو پسر بزرگ لیونل مسی؛ این چند ماه که اینترنت نبود احساس میکنم از همه چی عقب افتادیم تیاگو کی اینقدر بزرگ شد، آخرین باری که ازش ویدیو دیدمش دقیقا نصف الانش بود
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/22705" target="_blank">📅 13:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22704">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWwfb2NgfKpzKVcc0_06qvRhhLIbRxMa2xg3nqjUypmw-lY35saWfEzHNsjawVfImgpWy3xHZMdUd81hG-tj2XK31Rtp8jKgRg4RgSBSrkyMeR3ZyE8LR8-1xrzI7sjhQhb4lwhEcqT4-alDynHpCVzcc2LGNHrL96IKJ8kRp_VLEYcyClZtyt9hpQ24_EniF2IRyWDyeq-6zdnW0BycC0kvWfkjqlAyHOHydCX4dQHqOkRYcruLMF2IzKM_5_49VHDhet8qH6RHSQOhruEFtFLBj5cyQsigiXOzB-bYxMqA_Uh4Zz6iJIMttiNnjBY1GIB92uyj1Thb7DHW3zM8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌انتقالات|رسانه اسکای اسپورت: ژائو نوس، انزوفرناندز، یوشکو گواردیول، ابراهیم کوناته و باستونی‌فوق‌ستاره‌هایی هستندکه‌علاقمند به عقد قرارداد و پیوستن به باشگاه رئال‌ مادرید هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/22704" target="_blank">📅 12:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22703">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cL_rP-f7aICcYZDeWr3GU_-L0EAaVp2LdNPW32IvlIRGnfyc0MsLgg3C8Z6FPHYY0DLrzQhkLTbtbmA7cjCmaUf-ExOHUE2jZ33TfxCnKl5OxtlB_WID4P1mZ514ML8m0Ub7oLjgoN57w4OhaXOCZSXSO3Tv-qt9MRevAxWyewanAbkQaug06jTF22LsJP6tGZiatl_E0Cjf4xYMrJQnoNZ9q4PDTPJFnH9y87nTvB0qk3My6cqJn87geMECIn24Zek4CED9UsZDkrrnPxpSrLCeoWSVTdGlkrUOOEBfOwH281Ds9GJGLJUFPiC0hdG2O2V0B3QGhaQAZxXYOj7VLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌پرشیانا؛علی‌تاجرنیا رئیس هیات مدیره استقلال تماس های اولیه خود را با دراگان اسکوچیچ و نماینده رسمی او برای عقد قرار داد سه ساله با آبی پوشان پایتخت بعد از جام جهانی 2026 آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22703" target="_blank">📅 12:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDIYXg3-X2D-__-bH8LVsSC2XujnCuxVO5f-dy-Ys-AVJyuoc6Vfa-jsA7aE41_v67SGiWBxKTw00WVYjRIO2tP9vAzu2kCE-BsDoMx5d6oAv9hLhhXzbGi-qfJlazmJzqlc5vL6mFekxWyixwwClLmpD839hHRkUM69sn-5AhXuoPppsko7Z_Tb3OitSmzfAT25yY8lljSsxMmeCdWrBUgFCrtoNEOsLpbZXigLHWihbiV0c3PASarGHPC1XBseNbJG6raeQJi9ylSQ7YpI13S7sC7Epr5Ak33ZuJcmGXBrznynVr8vlVm34bfdUeAOmvRPcGA9bbprmAX1FYrBNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
هری‌کین‌درباره‌تصاحب دوباره کفش‌طلا: ‏«این یک افتخار است، به ویژه که فکر می‌کنم فقط رونالدو و مسی بیش از دو بار این جایزه را برده‌اند.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/22702" target="_blank">📅 12:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22701">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVUUaMw7Phk3e1-85kildJyXMtdju5h6yz5IsH20jtz8iOa-mQcb7sNNSPpKs1o3aRKdDizy9SHBFyJlZyD8NfM_3LAe79zcvfJs0Ub2RT8Z2eCo8w3MD8r5FwZm9bVcbbRKHTncF2SEtEs8eIBV1uoxHmV-WHjgC8OewbCbuq9E6yz04Z2yFVYwPmzUrwytSNITkxN84ZR9AuIJofzTlbPL0ELGOd-H8go8NpQU3E436ayQ-lWbZMAHvFy2MpzLVla-QzUNh2t7qIEEsPQ5P7HtBAXCRp9xZvt94Zk276vLIswgxidBObifEIPB7AWTrFTGD8F_tl5MkcqHuPznQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن
🔴
پرسپولیس با 6 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/22701" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22700">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=DFqhgHzlUiXIhHyr_foYrjVN7iJ3Qm3r5FB3YxTTaJd0718INa0PXPuhEGfmHU_X2broWupEl0E3JWIdAwIrDIt82NEpqPioi0yQEBx3x1uLubZBsKrm-N6qpCR694bEnJXl6uWzFGc8ceO0jmS3B6-vV9-Hd1fWP92vkKYBPv6ri5Ie-_YCBewwXuy8lgdJN9Dt9bZ1AfhKfcznHfad3C3-dv9N2Gl3xV59TemMMdkRF4HzUEIW_J9Vr5tRfNq1f4NU28go6vUsgxUUZv59B6iTl0-w_VxAshLkF6vOcQfhkbLt5Ew6WVVShYKiTL9-02NIFG4stQCmXHKKr8EZ7VYnFciqH0ZSrSrY4R2pcyfRB6WeAekwxoXM7RNyABcmpBIYZPNzKkMJyIuRLSWWAEcO8iDNeiMNpf-DeHKJgQCC3I6OeeShm4uNQuKdig1mPPbMsFxHpN9zKYAl3bmIOu4_eHH6E6srz63SZq2ByAwITQHhUMJIC6Cd0tVHQGpbO5jN7W34UHzSy30CJNguzr-pOaEeoGem00SdRdmpVLyH8XuxTHcIZ-UQopwkv3YWdqFeUuComJT5y3vrEI-eUey8APluv9Azdd817lMNcnn8ioPnO5Ke-39Xke-iDutvd78IKJnBZ1VbK9WIdzwpsygiqBajLnrwXA4D35vL2wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c4ff2b5a8.mp4?token=DFqhgHzlUiXIhHyr_foYrjVN7iJ3Qm3r5FB3YxTTaJd0718INa0PXPuhEGfmHU_X2broWupEl0E3JWIdAwIrDIt82NEpqPioi0yQEBx3x1uLubZBsKrm-N6qpCR694bEnJXl6uWzFGc8ceO0jmS3B6-vV9-Hd1fWP92vkKYBPv6ri5Ie-_YCBewwXuy8lgdJN9Dt9bZ1AfhKfcznHfad3C3-dv9N2Gl3xV59TemMMdkRF4HzUEIW_J9Vr5tRfNq1f4NU28go6vUsgxUUZv59B6iTl0-w_VxAshLkF6vOcQfhkbLt5Ew6WVVShYKiTL9-02NIFG4stQCmXHKKr8EZ7VYnFciqH0ZSrSrY4R2pcyfRB6WeAekwxoXM7RNyABcmpBIYZPNzKkMJyIuRLSWWAEcO8iDNeiMNpf-DeHKJgQCC3I6OeeShm4uNQuKdig1mPPbMsFxHpN9zKYAl3bmIOu4_eHH6E6srz63SZq2ByAwITQHhUMJIC6Cd0tVHQGpbO5jN7W34UHzSy30CJNguzr-pOaEeoGem00SdRdmpVLyH8XuxTHcIZ-UQopwkv3YWdqFeUuComJT5y3vrEI-eUey8APluv9Azdd817lMNcnn8ioPnO5Ke-39Xke-iDutvd78IKJnBZ1VbK9WIdzwpsygiqBajLnrwXA4D35vL2wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استفاده عجیب از گاز اشک‌آور توسط ماموران در بازی این هفته دو تیم بندرعامری و شهرآرکا البرز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22700" target="_blank">📅 11:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsubnEpVgyJri3yEq--37fRvvSOHEq9UZEs9Ta90l39pETNEikQy8bfy99enU5nk6a15oeFT5DoLkHL6F-oHWzma_eonMKPoWSsTTmIMA6JD_2NRyOpf_4X1y17q9C1FLULrxtnrQzGBBMn6dkckfPoAIYmyAzM_c6eC6JjSbQW7mAWThrhxpLlernGEhYxaOkgTUY0i29DRma3pFlGyGIAeNOgDPHFx6S0AueBc9adyrFg43J3BmvFX4wT2u_Yqjrpx3mxcerMABfQ5vGQWBVv-CwVeqzTWGkqIwzNXlo5ny__yFAYtN1lyRN_kqbWJhUjxqKxTG1p-C7pWYi2GKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه پرشیانا؛ دانیال ایری مدافع 22 ساله ملوان اصلی‌ترین گزینه اوسمار ویرا سرمربی پرسپولیس برای جانشینی مرتضی پورعلی گنجی مدافع 34 ساله سرخپوشان در تابستونه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/22698" target="_blank">📅 11:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خلاصه بازی سوئد VS انگلیس؛ بازی‌‌ای که زلاتان یه سوپر پوکر کرد و اون گل مشهورش هم پوشکاش برد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/22697" target="_blank">📅 10:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZbyf3lxwvh7nCamnxp474LEew4Vj0F9HXYqIKVaOYuiStgy2-a-GeLy-ybcOM158Bs7WX0CrYA2f4_6Ox6Bio-U-ZUbgKfTq2TyTd2sqMf-NFTo8kfOa1VLlV_3vPN8dH1TNGdu8zXfl9vY3lgHXjSxgT__5Te0gGht09kU_6YSLwFE-5JcelfTL8Q-RDxGBSr2Plj4TcxtuJNA7DbbQgU_QBVBFvu4t32oVySx2095lSLbTlMj8LtAvQm4rEPQ-qLy-J_JmKfDUW-DLhH8i1B9gb5OPNzCFbZjYJ2lD-YNZ4unmXXLdGcU-QS2oesrCf3pp6Xkfn7CwYqeR2Cs9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسکالونی سرمربی آرژانتین:
مدعی اصلی جام؟ بنظرم تیم ملی اسپانیا قهرمان رقابت‌ها میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/22696" target="_blank">📅 09:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRnlS8Fy_u4_NICR1jmKqUQ85PtMwrEHe9ozOVA8lWzZAy7VGLM8932_glljRWSVjciXQdMF2wMOs-DHVfOaw8vm2qJlHOjWi0YSx5RkD7kgIYk4SBvThOmTn00iMAZPgNgUQJpNTww-_IHl-GwtRpjIQJRvYGE3mtLs6CCp8n5gj8vdwrCZ8gXdfbq8H2SwxfM593uaFSbxlVsanKpZV-dUuevycfjZ1c0IkIk8NZJi38yzMJzX0RNyL9IEIFbUJV7E9gauypvD2Vg3eae_9TIG6zO6gcs_THWk0Xwo_n-WvTyKrad4ThbKlKY60rTX1g6Me69kZ3BVCH9nKS3Zgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اینفلوئنسر برزیلی کارولای شاوس لباسی رو که قراره درجام‌جهانی ۲۰۲۶ بپوشه به نمایش گذاشت؛ اون با پوشاندن بدن‌خود باصدها برچسب از بازیکنان فوتبال این لباس رو طراحی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22694" target="_blank">📅 01:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJKIDVNfw6ozB2beFnpH3q_3zgGfPBr0YS1cMxjjd60I144NvOhcrFkBdnqRYOL621EBnzAmviG21Wxt5avJhDgRA2jHa9ZFugpR9KPftIHFZz4LbaubmX7HHLk14DEwrabCn6InNOfHML7u50td2O0ngZSv6QH12EZncsyHndgIfvEfhkNRygfo92O4Y14dXeMTmtet6r_u2rU6zt9wQR7Xy-Hv4j2cSowLRM1nvkm8bEHEdTODW-FeVERlR4NPBnBjTn-hgohkaZ8Wief38216vYGA7XoUj7_WaX7qgfP8t-1G6dIJ-1Eop0CpnkzS6_jEu5uLw_Xn_jMPWEp0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدار های‌ امروز؛
از تقابل یاران نازون و کریس وود تاجدال دوستانه هلندی‌ها مقابل الجزایر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/22693" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22692">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_ICI_eNea6DxvZLo58NKEWLg-knUFIDuQqZ2STbcd7QCN_KMEGE03s6QZtQAvD7X-fi_XQEQnREvLErOgG0OxwIHGus9q1TlzvF5veFVFiW49YKGgL04kRBeUJ9O9n1bEXtem48Ri-o3FNCqiBDBHPUTWZ6WwyHq9wd6p7x97bw7lnybgtqeJeBQvfyRuIpNOW92KLWG_5FpXGs5zppZD9-4R_zRFEb1ufTPHKOhpDEBqIkwFKR474imLWwODuc-OVD9LaJUyQIOhiGR2jXnQQfZ09L0-O-pWsU_2B3JG9FgqB-odNhBsQbk9ACc46KSZpZSs8hTMmO-sZHVNFpTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج‌‌دیدارهای‌دیروز؛
شکست‌شاگردان کاناوارو برابر کانادا و برتری بلژیکی‌ها در جدال با کرواسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22692" target="_blank">📅 01:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22691">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d_tUSkOPIDlwk1GIpY81RhUtsUX6oBZNBfK3dEfXWqfC7E8OjWXDT5-tderWIzDZRp0Sp_S5_Q-0dGMJdHqJN7P1INsxbnNgvrCtkOkVkQK0iXEgUZLg9SZoa--yG7NHk3EAQhZGJIcS2DiY7dAWx5EyXFlzq-Q_2Mcf2lOowhYfSqdJ2ac-HPB1DwCTW4BIBiQpywnZ6EikDYPALkt6peFIvbee0o6Gc3BkqKVA3knI-EVeEJF2P3_4bx3b7XFiSGmgffBYq05fawp71dhCvcQ7QK4z4vQlfNUZ8KYnv1SNDk0J5T6z2k5vKvot66UjI3CmlzGYGsEuPjsZpfQYrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#نقل‌وانتقالات|ادرسون‌سیلوا هافبک 26 ساله برزیلی آتالانتا در آستانه عقد قرار داد چهار ساله با منچستر یونایتد برای جانشینی کاسمیرو قرار دارد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22691" target="_blank">📅 00:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22690">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnNVFfQT93vgBIUsBb-R-mqhK3D9snsf5PEhatxlGNP53g6ImGthw9UK30qFNciO3X9-RssG_rswF1MKz4ff_h7P7OTrmXaEZ-vSuVoFYIBayyAHzFWSx37yFb8LQH5wTQJZv7zfjY2lcvVXHSiz91VKqXs0hCUIz-Vu8TJ8LX8WhrOWN6YvdQgiWvC4RqxdBTZBP4FNlPfgDTJGvIW6wkoUC-sRLixqEz1fCxnTHsnbXoscZWw2ZSCy4ipey0OgyLConRNvYikAy0iZUeH3C7rVXBBfB-4M0-jX23I0GmMijARq3bR2toH1FJKLIsgvyBSjTcFr3Ges2D32X1I1Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22690" target="_blank">📅 00:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22689">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=Ce5P8gPRMn6frLIxiS8HfXHP-xw7LRImSEKGgdIAhpSBg5ezr2Cik6XpZDdLLJ0mILd1MVbjiaPzziJa34z7Yso61mID6Zd01Z3xv6HXElQgsPGcejsTLWfHZObrh5ZvKRbmmq5MiG4T_Ze41H9PuYPtlkNcGOb3lfuFpxHIlwiecBtaNaD99hfYAcoaiWpzcQmuUe_A-yCEtCtV7PxR_tuHEP8bAORD7GjSPvawJ89KMIuJnuc-I5JWaByohpv85GEgVh8JD4YAywuILYYJh7zIIOoJBmU_qj_m1oerPaesylYDL9o3o42Me0XYUQYNA6n5R-ztLu9cSN1_HdF6fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a506ed7ce.mp4?token=Ce5P8gPRMn6frLIxiS8HfXHP-xw7LRImSEKGgdIAhpSBg5ezr2Cik6XpZDdLLJ0mILd1MVbjiaPzziJa34z7Yso61mID6Zd01Z3xv6HXElQgsPGcejsTLWfHZObrh5ZvKRbmmq5MiG4T_Ze41H9PuYPtlkNcGOb3lfuFpxHIlwiecBtaNaD99hfYAcoaiWpzcQmuUe_A-yCEtCtV7PxR_tuHEP8bAORD7GjSPvawJ89KMIuJnuc-I5JWaByohpv85GEgVh8JD4YAywuILYYJh7zIIOoJBmU_qj_m1oerPaesylYDL9o3o42Me0XYUQYNA6n5R-ztLu9cSN1_HdF6fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه عجیب از خوش و بش آنجلوتی و اعضای برزیل؛ آخه چه‌وقت دست زدن به اونجا بود.
😒
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22689" target="_blank">📅 23:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22688">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/niyA-OAK8YkwkMiMnwWv-QHUUzcLkhFHjXNZ3WR1McT9UymemYSKuMqJG2h0KOirRDIJxPSoFjZKAkSa0L9Nzh2YwiizINPAeSwrkpDujX2xpfw1Qv8azv-rIZnT02bE7ctRrzG3T3R4SS5yc7DbCZHI8LutEcYJaoGRRwDR8RuY-8xE-QE2eozOz-pSPlrBQXK8RlQGe-6tDQbUnsfXcqoS-1EYkN1ln1FVnBfLhw5uJpoLnI3U890oCsXCYYeicBFCqVn8m95aFkl3h-QUt2bQZ7Qr-38_cUyyNMvNmop8DzLkTpR_QPtuD2Ae94me0foIPKFTG_m0fUkz_QmhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رسانه‌های عربستانی:
باشگاه النصر بدرخواست کریس رونالدو پیشنهادی سالانه 85 میلیون یورو به برونو فرناندز کاپیتان منچستر یونایتد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/22688" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22687">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA2sO_L2HgaMkFlrF-ZQc88J0s2xHkiyrWOTHVzucBhmZGIdOV6nvC1QBNUoKv0uTBVu6_jKsmnvVS_krbXBHYK3l40UpleQ64QwlFuc6mxjUD8G0QDLd_uqajaxCggc8fm8z4bFHyMru8VlMhnYMOjArOXjCwzcbvjWEKkBKFcBMs-CkQm6JhizfT7UAbJ8RlGzVSwDPVNhCvoaqN6n9o-v6KAkNwuUEYHHzWVVhMKkngfwJpr8b7rUj3hutgw9U2vXo30F44tJzvxpRUYFGbFoIrNStZBoRoZ31RFphs6h25NstWTuoyouLkbydSfpcjkcKDmESLMIAOJek_RRdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌ملی‌بلژیک‌درفاصله 19 روز تابازی با شاگردان قلعه نویی، با نتیجه 2-0 کرواسی رو شکست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/22687" target="_blank">📅 22:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22686">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_nCab3c9R--j6dK5QnNBm8CNJDQEiK43rVyO8T9WcdnEpOyEWX5bXjQhB3yuNpyiVrHvEmc2OL_JjVzpYRwKkQslVJ-JrdNs1MOe9BtHWCQ2KQexBVeIyYNFZ9n985hdyPc0NsR0sDqSXUa-tbLQdplfs0_gVNS5UKpKp0LRxMkVnpDtPCSPhMAreol4OmIap8RaVhxJC_KvqpFxg74gadgC6Zk9GwHLgXy9llDx5hX2rAxVM-HYI2Dwnngwh9PwSM0uVzjxV9wMNepPEcrCse8R3OSH9v2OkbNDosNnAREMsI9H3H8zEYYZ5WYi4rQST63Q8ysl-qmseP9cL7rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/22686" target="_blank">📅 21:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22684">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5291786993.mp4?token=er6yIFXOmFq0fwc6D9WchZxH2uLhLZ0UbdZNtNp5cJmv451p6Nopt34iRyk5FK9R4NSVFQo8Elb1iVIFde9hf6c5UgkyxnPQfEpax8IdCu9wLcoLiTTt4ebX63fAlbWjqrhqlTnUyi3BC2eoORv7Kj5JUIEFNzIMY-NtL67spkJSJeV0UBXeLRxE1JmOc6N3zRwhEnNR5USMLwIr4nPL8KEcloAvPOAA1GrJpBNLk0BWTeOun4NnxPOo1voWqGt1FFZGBbhhIeCfJ0-xDLfU2lwXGbnArGu5XZgo2-wf1tGPD4qLWH4wxv_RVMcVxy6_3F6vIz1ntv39VG3DpMgDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5291786993.mp4?token=er6yIFXOmFq0fwc6D9WchZxH2uLhLZ0UbdZNtNp5cJmv451p6Nopt34iRyk5FK9R4NSVFQo8Elb1iVIFde9hf6c5UgkyxnPQfEpax8IdCu9wLcoLiTTt4ebX63fAlbWjqrhqlTnUyi3BC2eoORv7Kj5JUIEFNzIMY-NtL67spkJSJeV0UBXeLRxE1JmOc6N3zRwhEnNR5USMLwIr4nPL8KEcloAvPOAA1GrJpBNLk0BWTeOun4NnxPOo1voWqGt1FFZGBbhhIeCfJ0-xDLfU2lwXGbnArGu5XZgo2-wf1tGPD4qLWH4wxv_RVMcVxy6_3F6vIz1ntv39VG3DpMgDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بدل‌های ایرانی لئو مسی و رونالدو پیش‌از WC
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/22684" target="_blank">📅 21:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22683">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilk7RvXI9Yl9OF9MyvQ_--HUP143yHrn2qqslPpOC9ySt9V3NcP_xrXfkAOZHCfl3VueVx7Lg-is2ihzIq-tb8dzYsHKkRG9QY8q1r3vl1VZs9DlEYj0qRQ8G7bcvvr8tKh5phJq9Osfo_E6hVguu0tr1VpCGQr_JREa94zl4jMc5dZqrCvikXwnM6udXYZOaMxvbrvnxvE7Qj2vh_Fd7WzYCErXfVRdgvenc0dTp4IlQvmTG3vODDT8zK7fehMH8YyQEHNxbNSIEnJlul9sHCAlWx7Qqp-CmCyB_5oR2RLHQmTuFHpVDogRSUWcKNKWQZCZZfVRPXCQDlj36JTavg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
فلش بک بزنیم به سال ۲۰۲۰ و شاهکار پدری درسن ۱۸ سالگی که تونست طی یک فصل ۷۳ بازی رسمی رو بازی کنه و قیافش به این شکل دربیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/22683" target="_blank">📅 20:22 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
