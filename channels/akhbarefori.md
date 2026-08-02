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
<img src="https://cdn4.telesco.pe/file/SO-jp_AnMUkUBJiEIUtyrPBL3SICCV6L8EjpuJG5g9JpdV0paAhdXoek4AS8c8VUIZsY-lli-xqShMGmJK8o6JAbRi5IVn_rKW-vYeHLJe9qETyDVqEBI6ppUq2mO3KE1v2_R2CKn85b3xH6t-LsTHrP9bxpe4LlrN3GTExkZGE7iqOzk_eNbxEgeNmY5OLsldXOd3VjVG_sklmCLEeVtQp3hs6MFAIiPv_sssfavcUVZ-0D868d5Yek5wQAsimK5JzlB0WoK-O4ihd2NuQ93Zz1R7Xa9SymPcPu9x1QRAF5Dc5WdCzFDYRfmq7_X0vnhlrZWUZQDZGRy_HmqmcXGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.08M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 10:57:27</div>
<hr>

<div class="tg-post" id="msg-677632">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
تماس تلفنی ترامپ و بن سلمان درباره تحولات منطقه
🔹
ولیعهد عربستان سعودی و رئیس‌جمهور تروریست آمریکا در گفتگوی تلفنی درباره تحولات اوضاع منطقه و پیامدهای منطقه‌ای و بین‌المللی آن گفتگو کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/677632" target="_blank">📅 10:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677631">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
سارق گردنبند زنان پایتخت دستگیر شد
پلیس پیشگیری پایتخت:
🔹
مأموران کلانتری ۱۰۱ تجریش یک سارق گردنبند را که با موتورسیکلت و پلاک مخدوش در بزرگراه صدر تردد می‌کرد، پس از تعقیب‌وگریز دستگیر کردند؛ متهم در مواجهه حضوری نیز از سوی مالباخته شناسایی شد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/akhbarefori/677631" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677630">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf768c0fb.mp4?token=RFeJDkJsg797jdG6IbAlPDV_RapjrQSb6czCxgnD5ZN4RgMEtc_a4LZuJ69nCnSM1wO3CUsCbgzR0h4JZh0yAKQWL_tg0gpIKJHNsD82LTF2giLhUK5Sp4q_ivNgGQZM0F5gSkT4DtyUHZoddsR5vV7ppEptpJu6Gp8yYgy-Ek1BTz4HgpmuBx0isFc3735S364C4-t-2GaKj9uaxb7ZWgZ4NcQj2AwcNqUxUW7FjgvVQsKEFzGmDpUANtSmMMMvKbC31TvdZB44mX6WSlrllz7RxXECqda31GvyouzYA7s_GgswSfKyCotJ1Qm42GTDH45YHvBFSETlzqxAjnmksA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوقلوهای تازه متولد شده همدیگر را در آغوش گرفتن و می‌بوسن
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/akhbarefori/677630" target="_blank">📅 10:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677626">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ELhKovOmJFUxbjYTSYPN2xyoodtfL0NvLNExOUcOqGwjsfRTAHzazu9U_CwatfJZy_K9f5XZmfPRA2ArmN16nFgfsJeJqksgIQpaWJxEktW5H3IJ1tfk_fbLruio38VigouMb6mOa4nshiB42Jn4IYMY-CQuFcvL4IARw3R_y8CA31aU6XAoatAFzHrvl84d1UyxqdPsODFzYojqtlEsNuzNAS5t-XYPcYpdk9EBga_8RB-hfExS9USZq6FuVZ5-sEjIIJfOx-tS2qlNTCZNbduERkjX1XzTqfQl2Yo0hznFO4mviZJfIINC1WM9X-V2Rl6cDyb_esNHL1Xb9o4OCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HQjxgkDY1WmoqoUPRqMA7xJGX4UblpmRXp722-Zj-M6mxpsLDlMlPkPX6CVyi-iyELHVDMXEpm6eltanXRbxdwhvIZlxBZBpkPkfi8rP_FNGjyMnu18-dsER1pw0awn7_yTphPfGtuyW1X37fK2UZoic9P9B47DbOFa4AC6OhP8PRH6imNIMAlveqgDquM9LmsyHW-9Um8ZZap0OhO14obMbnuBmooxSXuQ9dvsbSTZlepdBGyGkrOuBNkiDqS-DFZdVFjfYuc_9Ao7NDpVC9DHdkaG4coUQcorSbWsiX1ZiGCoOC_qtEjZxp2vwFpd3tb2JBq_p1zChD6W-rakzIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ahHB5_1w1OFJMvHX_qZuXMkbLig6diSnD3l1rma3ZHEg28N7nJk7vJfVgqeSaGzgRxN-OkxnOkQKzTtz5EKZ5QDicvBOezjaBgWBONAocIZq9mYcflEPh5a6YTQMhwXxAlDIOTKKgbgwwnA0hr4lvTWo2DTnSL7bD0_Cj3nz6nvbBNv7cl5jIwmIZKOXacc7mfYm6oYL6ZtLeAtyU6myf6F9HLWaDP_fv0jJfiZrXk7o8Y9rXs23QejW-7n-6zHNQ6kjk29L1kNX7Xj3VwhrYtbBSsWu4v3BjZyxFEkjQ8dY1UvlUu-HRy-uR1QWqoFF9J6HY8vsNxO-8VCdawTI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fRLFBH_gkRnIL05Qt3NAKg9HWS_AHzCQmqPqcZ5kti08mWWwxRGKxfAv0NQiAF3x6TOcyDxMgWz9ibrq60FVnlOffBVTOgFYwwyd_Yfd3ODNmyQzCNZVoix1l6N6KwIO4ALbEL95UN0x57OShBAlyqsasBez9yOTfet8sjpYURkTIi-Q9GYv_hYY1tXqCXBRn3b-hsrUGy5q_UWQhfGiCBlOMj6E63oYyW7gHDitCejeWIpsybsZFEoZajSzcZtw_anOtkqqRz0Wd_yOQV_DJ5Zdf3T4TzEeKeP4VkWTofkm1dh7G8TBwaQaN-flR4jjB6_kmYwgphDkypUDslJ7_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ویرانی‌های برجای مانده از حملات هوایی بامداد امروز رژیم صهیونیستی به جنوب دیر البلح در مرکز نوار غزه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/akhbarefori/677626" target="_blank">📅 10:50 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677625">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vA2fFCbay2x2Cmz4VDenRrwu7WWT8h8tFecLdpboN9tTbqNTsJu8CmmbPgfKb_4RbNQgQJ8_xUa1kth8A89QspEk-gHVbEOQJH0CaC1L3n5BW_tKsojvDy1PtIzQ6i-wsaqigTTKk5CSeEL_qL8EKuO_Ypl1oaARDkdlOnahbhA4eIcXOBfj2s32JFzxzOo2XwPXGUJWCZYaguvNiSt2YZyhp1wonAcOsBvqLTkKHGalSot69FC85BlIQUUEGaiP3FIkOMBqhL_LPCwTf361IcbY21Iby3_oOrflsG2n4VoBqArzmuBIUBBHk5LXGVDH_rl1Zoe93G8YSzTSDO3rmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهادت یکی از رهبران حماس در دیرالبلح در مرکز نوار غزه
🔹
حاج کمال ابو معیلق (ابونبهان)، از رهبران برجسته حماس در دیرالبلح و از چهره‌های سرشناس دعوت و جهاد در نوار غزه، بامداد امروز به همراه همسرش در جریان بمباران منزل مسکونی خود توسط رژیم صهیونیستی به شهادت رسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/677625" target="_blank">📅 10:48 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677624">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
مخالفت قاطع ژاپنی‌ها با استقرار سلاح هسته‌ای آمریکا
🔹
نتایج یک نظرسنجی جدید نشان می‌دهد اکثریت مردم ژاپن همچنان از سیاست غیرهسته‌ای این کشور حمایت می‌کنند و با استقرار سلاح‌های هسته‌ای آمریکا در خاک ژاپن مخالف هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/akhbarefori/677624" target="_blank">📅 10:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677623">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NE2RHr22vpjzya1N0PZhq9PwPnYleOFw9Mit_N-Y74kglX3ft6WFRZe1EbFwEStVmMxubndWg7_sZwE5UM6brnKtKdAtxgiX0HE7pTO8MvfwcKzXhv7K2m2VrmbLDtVBGdIDvGT-_GjZjWzw8UdEKgVw5KU5_zE0I9nd1qXyElpuMENsJehKzr14hT_e5NEmPxjXixMdKnKT3n-cWoUiksOMAZiEiNoIcJNeYvk8wuRsm0qkjAFtNA1Wo1vnEDFT363U_5Yw35ad6JwmQ3fN-9fz4VntkWb9mZCNquC7pNbG-GjNbRvsM9f6b_VSGhkUW2AEnJhYANW0oaVlgdPhEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دولت ارمنستان استعفا کرد
نخست وزیر ارمنستان:
🔹
طبق قانون اساسی ارمنستان، در اولین روز جلسه مجلس ملی، دولت استعفای خود را به رئیس جمهور تقدیم می‌کند.
🔹
رئیس جمهور طبق قانون اساسی استعفا را می‌پذیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/akhbarefori/677623" target="_blank">📅 10:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677622">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqR4NxGG7VW3ig8QoFfuGWenwUV_hcrqWBvKVwI7LC6azEipuseqNEpt25jravMhLbvkayFFvIO7LA5arUewdICleL3EPf7yDIEe2dOeGmVMQ-EyBrKglmP3vzhq4MJ_gfuBhsb_KU_T3cp5ViGn07veoCwp4lYJIIlhUgWD3F_7G_XrGGJ3dPTeO2bSBOtfzccs3Bk-i_5YoFtnAWZN3LmxXzXFAfbVC1hzDr1gC0JwM6N1MD1jtkuNpYGFXsLpCZsK8QpsbIDEvW3oQnfKRfcn6IfstriTZDX57ZzyRi7eCn9Vq69ot8RQQRPJq-8FGcVlX_9tXWdduCrcEnVGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نشانه‌های افرادی که از لحاظ عاطفی برای شما مناسب هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/677622" target="_blank">📅 10:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677621">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
چرا از رهبر سوم هیچ صدایی در رسانه منتشر نمی‌شود؟
همشهری:
🔹
هر فایل صوتی لایه‌های پنهانی دارد که سرویس‌های اطلاعاتی می‌توانند از آن ابعاد فیزیکی، جغرافیایی، زمانی، سخت افزاری و زیستی گوینده را استخراج کنند.
🔹
آکوستیک محیطی و هندسه اتاق:
هر فضای بسته امضای صوتی منحصربه‌فردی دارد. با محاسبه زمانی که انرژی صدا پس از قطع منبع ۶۰ دسی‌بل افت می‌کند، حجم تقریبی اتاق تخمین زده می‌شود.
🔹
تحلیل فرکانس شبکه برق
: سرویس‌های اطلاعاتی با تطبیق نوسان‌ها با پایگاه داده لحظه‌ای کشورها، تاریخ، دقیق ساعت و حتی بخش خاصی از شبکه برق محل ضبط را ردیابی می‌کنند.
🔹
طیف‌نگاری و امضای سخت‌افزاری دستگاه
: میکروفون گوشی‌های همراه فرکانس‌های بم را تضعیف می‌کنند و قطعات ارزان‌قیمت اعوجاج هارمونیک خاصی ایجاد می‌کنند که مثل اثر انگشت دستگاه عمل می‌کند.
🔹
نویزهای پس‌زمینه:
صدای سیستم‌های تهویه، ژنراتورها یا تجهیزات خنک‌کننده مشخصات فنی محل را فاش می‌کنند.
🔹
زیست‌سنجی صوتی:
رزونانس‌های مجرای صوتی یا فرکانس‌های فورمانت ابعاد فیزیکی نای، دهان و بینی را نشان می‌دهند. الگوی تنفس و وقفه‌های میان کلام هم وضعیت جسمانی، ضربان قلب و میزان استرس گوینده را مشخص می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677621" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677620">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کارشناس عراقی: انتقال تسلیحات از سوریه به عراق توسط آمریکا و با هدف حمایت از گروه‌های تجزیه‌طلب در اقلیم کردستان عراق انجام گرفته است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/akhbarefori/677620" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677619">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
درخواست عربستان از امارات برای اخراج سعد حریری
🔹
پایگاه خبری «المحطة» لبنان به نقل از منابع دیپلماتیک گزارش داد که عربستان سعودی از امارات متحده عربی خواسته است «سعد حریری»، نخست‌وزیر پیشین لبنان که بعد از کناره گیری از مسئولیت در امارات اقامت دارد را از خاک این کشور اخراج کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677619" target="_blank">📅 10:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677618">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjOYVfuGT5Uu6P4Lu7az-ZzOwKt2mIqFhFONA1Ilnm_XJwXMyzV7dCWderhN1ysTAAJ10rD0wonkZl0j9TKMuBs1eQPM39vQXHB-n-U6mwQcr5QmnjlQOGU25K_N1RQ3i_ChZz0nv1i5ofgKrJKdvsCevZ5uNMoK_7hNQbMRjCANAe264qk9loacx4I1mlLNvYxwic6Y2nGE4ynvphjb4m8yxJVOKvvnFlVWpSkxLIV865gHrZMciGvBbQc5olEsyFcrQne38Y1rXE-gPLm0_qs5EAjkAxJDcjXJADePle2W1616oPFcSc47XTFaUpaSJqvg-SW1ZdmPu036euMUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیویورک‌تایمز: آمریکا با بمب ۲ هزار پوندی خانه‌ای در قشم را هدف قرار داد
🔹
نیویورک‌تایمز با استناد به تصاویر، ویدئوها و بررسی کارشناسان مدعی شد آمریکا در حمله به جزیره قشم از بمب ۲ هزار پوندی «مارک-۸۴» استفاده کرده است؛ حمله‌ای که به گفته مقام‌های ایرانی،…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/akhbarefori/677618" target="_blank">📅 10:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677617">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecSn1HbBS5Tz1YPer59PvFykwBcdj2-HvvHNE_LVXw1w9tPBHLdakcbh_p-UvrehhBXDfVdgAkhrAdC5HWjSFFTI__aT_emPbQuPk48C2FarbxiRJcx6PUtQr9-hYValExhh3J-Ii7CC5So3Xo3ywsVXZ1Ysk_0jZa2luygR9Og1J1_IT0La8bDa6qkusQ1PHzatzreXOVreCbkVR1h3Tnz3tYfpg-xHSpHYt-OrN1yL8b0lz4YgSxWxvbrYhj7fabefnBZOMaqbaCx82Wc0RCmyN37YInEWNBruSoQKAdSd-hD8C3QWRYaYNYKHswrdm3kGcoc9AGqLKurTYPeKOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس کمیسیون امور داخلی کشور: مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام خوبی برداشت
رئیس کمیسیون امور داخلی کشور و شوراها در مجلس:
🔹
در طول سال های اخیر اقدامات خوبی برای بهره گیری از ظرفیت های مردمی در برگزاری این مراسم انجام شده است. مدیریت شهری نیز گام های خوبی در فعال سازی و به کار گیری از این ظرفیت ها داشته است.
🔹
همچنین درباره اقدامات فرهنگی انجام‌ شده از سوی شهرداری تهران با طراحی شعار « یا لثارات الحسین» و نهادهای مختلف برای خنثی‌سازی فضاسازی دشمن علیه مراسم اربعین گفت: تبلیغات امروز اهمیت زیادی دارد. دشمن به دنبال عملیات روانی، شکستن روحیه مردم، ایجاد دوقطبی در جامعه، بر هم زدن وحدت و یکپارچگی جامعه است. رهبر معظم انقلاب اسلامی نیز همواره بر حفظ وحدت و هوشیاری در برابر جنگ روانی، جنگ شناختی و جنگ ادراکی دشمن تاکید کرده‌اند. از طرف دیگر اقدام مدیریت شهری برای مردمی سازی خدمت رسانی به زائران اربعین گام بسیار مهم و تاثیر گذاری است/ ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677617" target="_blank">📅 10:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677616">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
هشدار جدی به نانوایی‌های متخلف در تهران/ رعایت نکنید مجازات حبس در انتظارتان است
رئیس اتاق اصناف تهران:
🔹
در راستای برخورد قاطع با نانوایی‌های که به‌صورت دائمی اقدام به گران‌فروشی می‌کنند، برخورد قضایی صورت گرفته و حتی مجازات حبس نیز برای آنها پیش‌بینی شده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/677616" target="_blank">📅 10:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677615">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3682c72b9b.mp4?token=bEPFjC6lIXPvqQkoI06AB81eOTy7D9hwcgwBMY4qcX96Go3YzhgLnJArQdm72Kzj7E48MdlsvtAsdSGte2BeZKp3cTFVG57BpykBMEAtn7m2rjsaas2ZJlksdCJgglLAnRimKopr0cxMaF_rwW5qh-fACKqT_JJxf1Z2o7JEA2lGh_lD4nD4blaNa3QVdjCOU67lzBKZAEeEVesQPZnwUU9-c5O0L6AgbeOyHYeFhB4wDyjeyMbeJBzLAIi7Ij6QJYnIGwLbdMkxUSfKjTZuUkCRa_iQ4W5-6MEPHbm3e4Q14Vz92noFJeqoB18SOih9LUCDw2tggttr5IIE-m_gnGFXOaOmyWXTJ_gFUh527lKyeDx_hSVtkQklVWvg-9SnUTF9GTRFju7u0o2GhvezV8ETpS-YUGUpKE5_DUbJXGvFF5DDp4ZBnptlVLJ-seLDHGBmNW0WXrBbLK_CcPu1BvP9aaA5uf9tQoD6JWJzlQSJynBrPEP7xWLGu3WnG321YrK8czerBfb_Q5g_nUxfD32uyO6EtriY40I4TaEZ7TbmK9VjKuyrTUVdFjY1GJdiRLKP1fhomuBT1Ra3aCa7utSZnWT8hT7JrpoHlsTMI7iWdbkMfYLs2HeMIW4hFVIXzY2b8LwXEjR3KZPwvKADmOGL3vPIC3rVWu5ezGrP66o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3682c72b9b.mp4?token=bEPFjC6lIXPvqQkoI06AB81eOTy7D9hwcgwBMY4qcX96Go3YzhgLnJArQdm72Kzj7E48MdlsvtAsdSGte2BeZKp3cTFVG57BpykBMEAtn7m2rjsaas2ZJlksdCJgglLAnRimKopr0cxMaF_rwW5qh-fACKqT_JJxf1Z2o7JEA2lGh_lD4nD4blaNa3QVdjCOU67lzBKZAEeEVesQPZnwUU9-c5O0L6AgbeOyHYeFhB4wDyjeyMbeJBzLAIi7Ij6QJYnIGwLbdMkxUSfKjTZuUkCRa_iQ4W5-6MEPHbm3e4Q14Vz92noFJeqoB18SOih9LUCDw2tggttr5IIE-m_gnGFXOaOmyWXTJ_gFUh527lKyeDx_hSVtkQklVWvg-9SnUTF9GTRFju7u0o2GhvezV8ETpS-YUGUpKE5_DUbJXGvFF5DDp4ZBnptlVLJ-seLDHGBmNW0WXrBbLK_CcPu1BvP9aaA5uf9tQoD6JWJzlQSJynBrPEP7xWLGu3WnG321YrK8czerBfb_Q5g_nUxfD32uyO6EtriY40I4TaEZ7TbmK9VjKuyrTUVdFjY1GJdiRLKP1fhomuBT1Ra3aCa7utSZnWT8hT7JrpoHlsTMI7iWdbkMfYLs2HeMIW4hFVIXzY2b8LwXEjR3KZPwvKADmOGL3vPIC3rVWu5ezGrP66o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دماوند را با زباله فتح نکنیم
🔹
با توجه به آغاز فصل صعود به قله دماوند، از همه کوهنوردان عاجزانه خواهشمندیم که زباله‌هایشان را آنجا رها نکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677615" target="_blank">📅 10:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677614">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ایهود باراک، نخست وزیر اسبق اسرائیل: توافق با حماس کاملا اسرائیل را نادیده می‌گیرد و شامل خلع سلاح این گروه نمی‌شود
🔹
حقیقت تلخ این است که ترامپ به نتانیاهو توجهی نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/akhbarefori/677614" target="_blank">📅 10:13 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677613">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/442feeb9ec.mp4?token=UOhs_aYK-qxBcRx2Fh-tJjTLKasWGYKue4u5OcKB1L8vvk22JoHJCjvmamkQO4_DPhZmL8bL111x_RIaZ0Uv2idmRxA62krXyyvG4usCjHefPrSL5gxk1zErym50CQ8Gz1VS48p3KGkyLE86e5nHf4t4qR_TiIdAB-am_kmOfxoy9xvlAYisI4a7ztOdw0kBNEWIZRETAmO5w0_Hs5BNXSS03By5PqVxTZSamj9pBjjIOk2EEuMiDEyB87P8JSYGZVCnS_k1sbbxhOMJHLqp-tjjw5AociGn_nGyMr4B64RWbAAULq2gXoDGETEbbhqwY_Y86CJaYbVhQkN6YwM8Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی قابل تأمل از دختری ۱۹ ساله که در این سن دهمین عمل زیبایی خود را انجام می‌دهد...
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/677613" target="_blank">📅 10:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677612">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc59a098af.mp4?token=h8uMvmtKORwowrtqn8ueq994zcuq261nEpniqtW9b4666BksiL9P4M0o81aDngp2JycyC6r9BImIeDQluCCV6VSix8a7iuaRjBB0YH7yGuP1U-KpR7joE_A7BOUY3w9wo90hJywxyEy7mpxpZxFmMHPjn8eO4-4CR3ndk5-joPu6TXHWiXVjRR36XPxFzZZ5iWpcpFz-TzEbxAFLwqAhUgDjza5dbynMTPZjzEz02OmqvDZDfb_uuWMOeDb1u6JV6DomP6aES9LwGbhy1CIM_0ifLm3phKIuN9Iv5h9VHgJuXCc-leiiUyBjQzavZ_aKtuAwWxShavqZCwMzCxsk8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به سبک انیمشین درون و بیرون، برای بچه‌ها غلات صبحانه شیر و میوه آماده کنید  مواد لازم:
🔹
یک پیمانه غلات صبحانه دلخواه
🔹
یک پیمانه شیر
🔹
نصف پیمانه میوه تازه
🔹
یک قاشق عسل
🔹
یک قاشق غذاخوری مغز #آشپزی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677612" target="_blank">📅 10:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677611">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e17b7771b.mp4?token=oAZdoPBsww5CtDUz0rJMkPVZ5MHY4fc0N5hLZFp0ngtKZ9PZg9QIsOBS2ZcR4ib38opB-KTbEVMgTFkx0w4NwH_QM0BGoq2XUvXdwf-_ov2sPEyk6Yar-DHd4YP00PSpXsQc1MyI7RaccV5YaTRmqPY3RTI1SZocfWvPHdYxcdbYb8xDJrVJK1glWjJbkzk8bNpomteCgr-IrJ5nUbX8FRM17y1igdDXrm1KZC8i1QTXHb2rXAL7s3UF4dABmcGsJJsDhDX4AVLx6ui939UXRhK2L-GTJZ60uVK8B5RgNSHZ3zagPqps_gHGjMY3luoOH6VZ9IV2GCmkW2TaIcnXALg5Nd-IS8Bd5x3786-VF2d6o3L4eXq6qwZVrtOgscJDOxuIra0TStRFPviWSzkldhMWF1gpoVPcjD5y5leMuxxhhO2L-YgWvmZ1FCN872mdSCAom7_yTA9LVRz9ZQC3a5zWdYGDA1nui40LQMs-zXnIwUmrG4RjxmG_-vWVgM4hF0Y8I8xKcA7i6_AYABakTc0RsgO4LvvpKSN9Vvuw_Uhndf7VNcRLGvveT-axwBtwCr5eLirj2ngiAGzRZveH_jthVVI9aI-fdcwwiBJF7UnGabngNSWrOFJ92u6yhh1cd1orC1nk8bPvPDodEibLpZePzaLqbbQ0BLAckuWCtkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وحید شمسایی: امام‌حسین(ع) خودش دست ما را می‌گیرد
وحید شمسایی سرمربی تیم ملی فوتسال درباره حضورش در کاروان اربعین حسینی:
🔹
این حضور به این دلیل است که خود آقا دست ما را گرفته و امضا کرده است. اولین بار است که با کاروان و به شکل گروهی در این مسیر حضور پیدا می‌کنم.
🔹
زیبایی اربعین همین است که هرکس با هر توان و شرایطی، به عشق امام حسین (ع) قدمی برمی‌دارد. فرقی نمی‌کند عراقی باشد، ایرانی، بحرینی، یمنی یا از هر جای دیگری؛ همه کنار هم هستند و از این سفر معنوی بهره می‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677611" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677610">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
با بازار سیاه بلیت اربعین و دلالی در مرزها قاطعانه برخورد می‌کنیم
رئیس سازمان تعزیرات:
🔹
هرگونه گران‌فروشی بلیت، دریافت وجه خارج از نرخ مصوب، فروش بلیت خارج از شبکه رسمی، فعالیت واسطه‌ها و دلالان و ایجاد بازار سیاه، تخلف محسوب می‌شود و با متخلفان برخورد قانونی و قاطع صورت خواهد گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/677610" target="_blank">📅 10:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677609">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی  بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/akhbarefori/677609" target="_blank">📅 10:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677608">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMD5TgzK0f7mFWKpBhMd8_Dub5aD1TafYzSmf57M8OYUX-i-2Nd7cIJabaajx2xYiTUBOHeQHw8RmdwJzdaTNOXWRja1ggrgZbv9CYq002DgqA4HCyX6a9yXGTj0s4MyhKhhPRza6owsXXQfwa6kGSyMjK_eetcRUuQ-T8bOkb0xZsas4LMTFRoc5kp2NIv9FQFNijmuU_TdI9XEPmi7b9_bstFQe7mleNLU4PrqrZIJvGaSqpXklIyEYmSPRwvfxNsVy0HaDbCVmU3hiVEgf-LHWmsgh1L3giEqx0mrG5fxdF1QRb-mAAqAvc9jyE1sQ1SdTTsxCqT7rWIXBffvmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تظاهرات در اراضی اشغالی علیه سیاست‌های نتانیاهو
🔹
ساکنان اراضی اشغالی تظاهرات گسترده‌ای را در مناطق مختلف در اراضی اشغالی در اعتراض به سیاست‌های شکست خورده دولت نتانیاهو برگزار کردند.
🔹
از جمله تظاهرکنندگان عوفر کسیف، عضو حزب حداش در کنست(پارلمان رژیم صهیونیستی) بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/677608" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677607">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
هلند برای اولین بار رژیم صهیونیستی را به عنوان تهدید علیه امنیت خود طبقه‌بندی کرد.
🔹
روسیه: به بنادر و کشتی‌های اوکراینی حمله کردیم.
🔹
هشدار دادستان مرکز مازندران به آتش‌افروزان مزارع: سوزاندن کاه و کلش جرم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/akhbarefori/677607" target="_blank">📅 09:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677606">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
سناریوی تازه برای جولان اشغالی؛ سوریه مالک شود، اسرائیل بماند!
🔹
رسانه‌های عبری از طرح جنجالی جدیدی برای پایان بحران جولان اشغالی خبر می‌دهند که ظاهرا شامل به رسمیت شناختن حاکمیت کامل سوریه بر جولان اشغالی، در ازای یک توافق «اجاره بلندمدت» برای رژیم صهیونیستی است!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/677606" target="_blank">📅 09:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677605">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سی‌ان‌ان‌: عربستان به عنوان یک متحد کلیدی آمریکا در خلیج فارس، نفوذ قابل توجهی بر ترامپ دارد
🔹
وابستگی دیپلماتیک واشنگتن به ریاض در خاورمیانه، تأثیر زیادی بر تصمیم ترامپ برای عدم حمله به ایران داشت/ انتخاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/677605" target="_blank">📅 09:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677604">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/226f9a1908.mp4?token=Tz0vD-OH_eHRZ9gxeB4sJQOiXOIFyGEqY8ZYiLrSO3lAv9502sqhmt4tu4_W_gFwWKtSL8tezvjJ8FaUo3qwRwriaWTMKK8nLlMLcdAArbTUVWlMEGeytAm8KrlLvRNER9syftwSFwVu-MB7n6Vd7ZJfkgUQqX6lwnF-KgZJrrLfCfu8fS8bE-jl6QtAAcFzn8zmoL96lIiVrTjLBQNQVrCnVrJH6IVyFOE3G0W-9oLLqtrSeJQZKI0iT3rIX5ttTOjP49Q_JWcO32rVeurnmnmdv8hCpgqSw3eIZ_Vj6TJ-5aytGhE9zFJqBt1-TBXQrU_cvymVhk9DwmRZkNNZLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/226f9a1908.mp4?token=Tz0vD-OH_eHRZ9gxeB4sJQOiXOIFyGEqY8ZYiLrSO3lAv9502sqhmt4tu4_W_gFwWKtSL8tezvjJ8FaUo3qwRwriaWTMKK8nLlMLcdAArbTUVWlMEGeytAm8KrlLvRNER9syftwSFwVu-MB7n6Vd7ZJfkgUQqX6lwnF-KgZJrrLfCfu8fS8bE-jl6QtAAcFzn8zmoL96lIiVrTjLBQNQVrCnVrJH6IVyFOE3G0W-9oLLqtrSeJQZKI0iT3rIX5ttTOjP49Q_JWcO32rVeurnmnmdv8hCpgqSw3eIZ_Vj6TJ-5aytGhE9zFJqBt1-TBXQrU_cvymVhk9DwmRZkNNZLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای بین‌الحرمین در دو روز مانده به اربعین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/677604" target="_blank">📅 09:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677603">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlldt23hzkbfY9ABBK1mdEwhiLfDX9kJ_YyM_eZ7U2c9ElJAD5bY7toE3RTA9vYsaBKD54KKvfbbV5nyGjSkOvP-ML57OIoifqKA1KZveGqKxkj3B9OsxrYnrKoUehOENWblc9hcj0Pq916nF9J-a-nsDQxeiSJlv_IksQ41l-i-mgBik2W8LYbdtusyT52J0EAkFibzglgaENj599qxcWYqoEh5FJGzMiEg8qLqNAgdgu-dktKniaoboclz-t5c4HopL0I_GxZh6IA2tHp0Mp60O1IeD2FntOkDCRug81ciSIXJTfN4w1Y508BpO7rdmZSU18BX65UwtQcWqmqlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر روز ناسا؛ رنگین‌کمان آتشی در آسمان ویرجینیای غربی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/677603" target="_blank">📅 09:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677602">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
آیا حقوق همه سربازوظیفه‌ها از مالیات معاف است؟
سازمان امور مالیاتی:
🔹
معافیت مالیاتی حقوق سربازوظیفه‌ها مشروط به پرداخت تحت عنوان پرسنل نیروهای مسلح است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/677602" target="_blank">📅 09:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
فرصت دوباره انتخاب رشته برای نهمی‌ها و امکان تغییر رشته در پایه‌های دهم و یازدهم
مدیر کمیسیون مقررات تحصیلی شورای عالی آموزش و پرورش:
🔹
نهمی‌ها می‌توانند در آزمون تعیین رشته مجدد شرکت کنند.
🔹
تغییر رشته در پایان پایه دهم و در پایه یازدهم (فقط درون شاخه نظری) امکان‌پذیر است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677601" target="_blank">📅 09:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vHDZX1duMzutZ6XYyT8udT-zc2hXo62crdqy3DDvvVdE6OTlELVIUFHLHnBGoy80RwSfO-W3ZJ6D8sokBCdFsLmSOwVlmjffpkASGqdKpc24jkwDVIl11qqiDTiFt9tJQ1pEt38l2IrT1QgQZ_ooZRlK2i14Xb9wZQKj8JpPGtBe1fAHLTrpM3R16cf7G0IRyut9pYZ1M2DvYl5bB63rK_e2mfpSVwouRYIx_NlbGvrAm4hwhTt-_uc9hJ2LCfKd0dg3ieC6t6HFMLwEZgH07oMhhCZZZVCBFNipJmqfKWCdACloKfgO55WfIMMzQNFX-ueFUpt3RaL4vPp7cajtDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۱۰۹ هزار واحدی شاخص بورس
🔹
شاخص کل بورس تهران در دقایق ابتدایی فعالیت بازار سهام بیش از ۱۰۹ هزار واحد رشد و به جایگاه ۵ میلیون و ۱۶۴ هزار واحد صعود کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/677600" target="_blank">📅 09:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
رانت، مافیا و دست‌های پشت پرده در مصوبه تعیین‌تکلیف نیروهای شرکتی
بیگدلی، عضو کمیسیون اجتماعی مجلس:
🔹
مصوبه هیئت وزیران درباره نیروهای شرکتی تحت تأثیر رانت و مافیاست و به جای تعیین‌تکلیف، به هدررفت بیت‌المال منجر می‌شود.
🔹
رئیس سازمان اداری و استخدامی باید در این باره پاسخگو باشد./ باشگاه خبرنگاران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/677599" target="_blank">📅 09:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ad4M5qDHRfo1QyIcpS1LILAkdHyR21BRT_OhMqWqQOiIZUM8v_DwmFWmykX1awfnQJnSXzbGBjVHMBx-lWlJ4ps_faK88iXuxomopYc0a7uWmBqAtOPWrp7GqlqvbF3v7b0SXDb6C6WtCVMwZzkzYK39NHc7NfDvFDirQU9K-BQeM0rziR9p9HR8C5YI20eVW6LTEQzdCwIG7LWvdvq-rp_YCDPgbVTvwH2cEwKXn8vO6CbvlnApaWqhbHK8rjk8jl-WiiFpgk_QYq9l4aCfW3mb2qxRRWrkA6dpt5VzNgo4XHioWF1a8Bnf0KPCnYhcMDBY1s63oV3_-GbdUWttkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح فروش فوری کیا اسپورتیج 2025 کوشا خودرو
✅
قیمت قطعی
⚡
تحویل حداکثر 20 روزه
📅
شروع ثبت‌نام:
یکشنبه 11 مرداد 1405
🕚
ساعت 11:00 صبح
ثبت‌نام و پرداخت وجه به‌صورت آنلاین از طریق سامانه فروش کوشا خودرو انجام می‌شود
👇
🔗
سامانه فروش:
https://sale.kooshakhodro.com/
📄
دانلود بخشنامه فروش
⏳
ظرفیت محدود است و ثبت‌نام تا تکمیل ظرفیت ادامه خواهد داشت.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/677598" target="_blank">📅 09:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
اجرای انفجارهای کنترل‌شده در جهرم
🔹
مدیرکل بنیاد مسکن انقلاب استان بوشهر از آسیب جنگ به ۸۴۵۶ واحد در این استان خبر داد.
🔹
روسیه: از دیشب تا حالا ۶۳۵ پهپاد اوکراینی را بر فراز شهرهای مختلف روسیه سرنگون کرده‌ایم.
🔹
منابع فلسطینی: اسرائیل تشدید حملات و عملیات ترور در غزه را متوقف می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/677597" target="_blank">📅 08:59 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677596">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/231656c732.mp4?token=mGiGy-SEPdF1QaRUdaTVAu9_OC3VtxPPT16XGOkGv9_RSWoym7pX8aj7zG9id2osEvLdpYOBpXyT8FpmDW1CWtXBf9bD_sR0YZH31Azb9O9R_bRGEO6xBybLrl7r-WlyDsGYnQ08yJwVdngcIO-NeS9Q0BfL6YE37cQP5xMwFAAfpEJTHX0b1muvwIKnhlGux9etK4eXrFXI049X_0HC7ZC5jC6xEO_lzSPmfu0wtTGCbD4Z6nB6k0nhzEwvnGRV_06CQC5-Fk1CChxGrdO3gh4xryVICcgi0m8-b78zoJo3DTpCtu8c3VokepoH7C9b4vnYVorPthWd-CeIi9_nfl24OP0jxmW9RX5KmDg2oxcoWLkyMO65ts1yPw-may2GIpoaYPjhVic0jhwiFMwfS6FwqofdMDGulS2cjTf9abaH1q_ReMUcEiUbIqYJOhODbkDcEOnVe1lFZgcB9vI-eXR3Vpfra5N1NAIthmCGDY6Bmrqr6A_eggdFkqBM2Ij-wLucqdtV-WhF3KKkj-hMBHWiaj6pfiyj6D3Esgmb56HUzMmvOd4yJZNGFcW3EGJ8oxGwmBJSDWQQnB_X7mxXyR5v5Zh0UNqRN2FsvbxqFEFxc90LUifkXvt-tNUnwjcezI39Ad-0WBBKSMkyoEoeNAYigv7uMJsAxppyTDPcoLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چند ترفند کاربردی برای نگهداری مواد غذایی در یخچال
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/677596" target="_blank">📅 08:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس سازمان امور مالیاتی کشور: مهلت ارائه اظهارنامه مالیات بر درآمد املاک اجاری عملکرد ۱۴۰۴ تا پایان شهریور تمدید شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677595" target="_blank">📅 08:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15086cc29a.mp4?token=fV3hQPprrEcIgxGPwTR6LmKLemTUug41mEgaidyaLC9Bx9gCsGlUepor2ribnvvT-Hgk7axWu4yMUeauUgqvLPLaCLGNi23w6j5YycAKDADA_ykPCPfsnovE26xZeXAEz5gUU9Uw4pwD0ZA2sNSVlpvkj-hiKI_Xje1P97_DwxCweklZGKrtmQhB3uzr7-89RRjjFuzQQx2rNc1aoP2rlft_BAwy1Rk1lp0Gf3sMjgTrEFZP_oI188KCXBpGN4MoBUAX5WYJV4aELOnndI_gqmtrBkNWKNk2DK7HuGbFntS-Lz_rAEC87eo6NFacZpQ-ZVEW0zSeCbHTGT3kS1aB-6FZ3yE36kvSAcs-PATObOrb_R8_AwDtU9wrcFp5rPK7Hia3JJCAdOXOAq-DmIv_osn5W8vz6hgcvYSmZ-FtxYatRYP14dCOLsew-rY0ZcV-S0GWtUOsNC1WzVxM1Q5EBlvlkg8EKHejJ19OW1zLTn867OMJ3ZUvXr4JBAw-VshRft44FtzCyfnVa6B1Unv-z5zj0nQW7nYw-OJmIovCrT2wHNz-EshfAB_c9EBUjKNAIE7Dd5uRhvIRK8N-HLQRPgqZiP839NX3r0Zk2w_D9POxIwXHJvK6ML3Ra-CklBh46FhUt2WCvEDMi3mXgfMRUM_t3vLIxwIP8612_z9BHnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15086cc29a.mp4?token=fV3hQPprrEcIgxGPwTR6LmKLemTUug41mEgaidyaLC9Bx9gCsGlUepor2ribnvvT-Hgk7axWu4yMUeauUgqvLPLaCLGNi23w6j5YycAKDADA_ykPCPfsnovE26xZeXAEz5gUU9Uw4pwD0ZA2sNSVlpvkj-hiKI_Xje1P97_DwxCweklZGKrtmQhB3uzr7-89RRjjFuzQQx2rNc1aoP2rlft_BAwy1Rk1lp0Gf3sMjgTrEFZP_oI188KCXBpGN4MoBUAX5WYJV4aELOnndI_gqmtrBkNWKNk2DK7HuGbFntS-Lz_rAEC87eo6NFacZpQ-ZVEW0zSeCbHTGT3kS1aB-6FZ3yE36kvSAcs-PATObOrb_R8_AwDtU9wrcFp5rPK7Hia3JJCAdOXOAq-DmIv_osn5W8vz6hgcvYSmZ-FtxYatRYP14dCOLsew-rY0ZcV-S0GWtUOsNC1WzVxM1Q5EBlvlkg8EKHejJ19OW1zLTn867OMJ3ZUvXr4JBAw-VshRft44FtzCyfnVa6B1Unv-z5zj0nQW7nYw-OJmIovCrT2wHNz-EshfAB_c9EBUjKNAIE7Dd5uRhvIRK8N-HLQRPgqZiP839NX3r0Zk2w_D9POxIwXHJvK6ML3Ra-CklBh46FhUt2WCvEDMi3mXgfMRUM_t3vLIxwIP8612_z9BHnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل شدید در شهر شی‌آن واقع در شمال چین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/677594" target="_blank">📅 08:37 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
نیویورک تایمز: هم‌پیمانان آمریکا نگران شکست مقابل ایران هستند
روزنامه نیویورک تایمز:
🔹
هم‌پیمانان آمریکا نسبت به این موضوع که جنگ با ایران به سمت یک شکست راهبردی سوق پیدا کند نگران هستند.
🔹
هم‌پیمانان آمریکا می ترسند که ناتوانی در ایجاد تغییری پایدار در ایران، نقطه‌ ضعفی را آشکار کرده باشد که روسیه و چین از آن استقبال خواهند کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/677593" target="_blank">📅 08:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشاور رئیس مجلس: اگر آمریکا به کوه کلنگ و تأسیسات هسته‌ای حمله کند، باید راهبرد هسته‌ای کشور تغییر کند.
🔹
سینماها روز اربعین تعطیل هستند.
🔹
رسانه‌های عبری زبان از کشف و شناسایی جسد یک نظامی صهیونیست در نزدیکی بئر السبع خبر دادند/ایسنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/677592" target="_blank">📅 08:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obHxRoKFiDf9DKreeJvJJkn4f8WapzBoQ_cAhL5IgObsV7pbsNQC_9FAQLI7nFoMud3QdeqlacHSWoyX0_dV768-7BJY-wpNt9NFiCC5QsrFig8C7l-037vv08N-bZaXbWebzxccjEQz-eijDYDMgSsHdwlK9SM91xgrLSGZmFi4iucuKyz3aMyWXzMOnL4pdbxs8DncyYybqCYNoO5UkCFtkNwR4QOyNWvTgsb2SyClU2LX3W-xJfdwP0AT7WI1OYOI9gyHIE_ijIvJkCUPwN8NFiIWXUiy17Djo-2SvRceQ-qkVp49cfPwTSqqHmDEEJoCjuaI_iIuLJk7mGs1Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توطئه اسرائیل علیه اسپانیا با ایجاد بحران مهاجرت برای این کشور، سوژه «الفن المقاوم» کاریکاتوریست عرب شده
🔹
اسرائیل می‌خواهد از طریق ایجاد بحران مهاجرت دولت سانچز(منتقد اسرائیل) را زمین بزند. لابی صهیونیست هیچ مخالفتی را در جهان تحمل نمی‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/677591" target="_blank">📅 08:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
بلومبرگ: افزایش مجدد بهای بنزین ترامپ را به پرتگاه سیاسی کشانده است
🔹
بلومبرگ در گزارشی با اشاره به افزایش دوباره قیمت بنزین در آمریکا که به تازگی از مرز چهار دلار در هر گالن عبور کرده است، نوشت که این موضوع رئیس جمهور ایالات متحده را به پرتگاه سیاسی کشانده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/677590" target="_blank">📅 08:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
تردد در محورهای اربعین روان و بدون گره ترافیکی است
جانشین پلیس راه راهور فراجا:
🔹
در حال حاضر ترافیک در آزادراه قزوین - کرج سنگین است.
🔹
در محور شهریار - تهران بار ترافیکی سنگین و در آزادراه ساوه - تهران ترافیک نیمه‌سنگین گزارش شده است.
🔹
در حال حاضر تردد در محورهای اربعین روان است و زائران بدون گره ترافیکی در این مسیرها تردد می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/677589" target="_blank">📅 08:23 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba72b522c9.mp4?token=KHw_rTBEzRnQ9iGTKrmx3pP50xMsJY9WOFxawTjwI98UXaA4fvlOnAzLqBtneVCIljTLgxJTt2AQb6w1yc0v-y8jXlY_Mdg-Ut9fyQRM4mRZkT3rCqnTYghjVUHXZQG9niVh_0fZOhgIIfy7L5mGrOi5Wz9nRKPqtiiqIdIePLOIOB5bKXWzU8P0jnOuJ6Fry4KM9FRlwmO8Eq_pEqbcCcz-phyqeKdZZ7NsBhSr_wJ6JPn2eaCV3p-ilGSfZRhcFqE0-ytN1H4SFCl-JqmGsD89KsC6gdnCQSKhSR3dR2w8invmymjovzXzZLsopYYkds0GRawvcfh5JRZSn-ZHbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ربات انسان‌نمای نظافتچی با کنترل مشترک انسان و هوش مصنوعی با دستمزد ساعتی ۳۰ دلار وارد خانه‌ها شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/677588" target="_blank">📅 08:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
رفیقدوست: امام من را صدا کرد و گفت بمب اتم نسازید / تنگه هرمز آبراه بین‌المللی نیست / جنگنده هم ساخته‌ایم و در حال تکثیرش هستیم  محسن رفیقدوست:
🔹
وزارت اطلاعات حدود ۱۰۰ گروه نفوذی را شناسایی و دستگیر کرده است.
🔹
هر نقطه‌ای که از آن به ایران حمله شود، هدف مشروع…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/677587" target="_blank">📅 08:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f0205d5.mp4?token=eUVu2AqVJW78VuWiVSRMalOVLMsEIEQXm6snbE3gJ9x3GmBnZHfnROaSwdLiosflsDHySYAm2wSjozDSsg84M1P18UckyTeQAR_-VNAjHhvukTgNhabpxzTG7fumlwSUyx1jRG7R0f4gSlpByUnTIKxzqB0TO6abpz5pCeZyFZHrRjjlMjEZSEzqtcqkmeBuZb2DNj8HMjE2tSiD7Ecyi5v-6-n598WYDe2N95YuIDuuIZb8yKopchQafGjkKOL4iIgVoGgXuSpvTRmiCTgZog0FyBCIW-mkltpJMfOvjE46Be9Zl-TE5pFP7lTWsLGDeyE6CaXLiMf2oAUUnxlQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تخلیه اجباری شهروندان به دليل اتش سوزی گسترده در ايالت واشنگتن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/677585" target="_blank">📅 08:05 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a987ea5b89.mp4?token=v9ptQJ4BoxpnoSJ8RA1fB7f5Oq2cAUWkD0KyTRh9r3lkg76AMP5J_8itmmC_YNfA4g0i1eBSty0KQLK0CAOVrwzg25srPDmsvBZsn2nucfFKB-0_9RmeSs4p1J5R4DaO4UTa-4W9QajYAXjA4s4F_XunN0neCH24ca-DCvrWUbiK4aEkSsBUYRjgTbYKB_uS3g75m9aMFSKo5U0zjLbsD2dkLe6DvQb5PD_IJ6QGO1ejk8_vMhFdIne3c_TltJqEudjgxcZ2Sf9FOdQ9w3ml6hZ4lvjlQv4uesvNxm3GrGUgHFePRodA7hV6WF4xjCrGBPkoSKs0-QVdm2WhhHnveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فقط با یه صندلی و چند دقیقه وقت، بالاتنه‌ات رو قوی‌تر و خوش‌فرم‌تر کن
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/677584" target="_blank">📅 08:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0xrgMdPCFfXuwCUUmjCgvEwk-ufVDDybDuSPFoYGysHCKJYm3nN0G5VctndL-V70tyY7oB5j9qUOictUSUhsWp96IP7B-HVW3b2EsQwL5t2RpaDUB6yr2GULIlmLzX9x8tb9hCwv8kO56enD3krcxxGqjnUgNcaDvwssRRDQEBKJqgQqK5oKFV9Z_8NJMt8r76O8TjNWFxUGmma4Klia6rird1gTIhPFxf9OiGaO10cNjwYcW6Tj8aMANR8yrUZGyTpGgvHGbJUfObTyZNBKoI3iE32Tv0NQoJfMcfioUL0S1MYGkulg1bQLvhswJJAD3AlrzR00_809PuG84xMSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8hlhdIUHOdDxIR-bsATfHAzlaVtKdp7k0ZjLJ1zm4xnQ5kXgDT1D9ymfUzyFpO-aRiwj-Z21xhxUCtUCO7G55diviAMMP8Z7Od4v-I7vH_ILJu3dPy-5qOyD80ZiADsCZPmiVONl1DBKrROEbKaRxQmEiy2KMkGdIAg0FRHc3MaPCHwKy3Ef0JPwebr05IagsxS4Nik7mvrBap92ryE-EI4LceWB_NadvEl3k0NEIyX9PJk99fgDlf_TkAfXxIo7Vf9pokt_umisB7zIrmSJe2wU4GMWcOlHNH-c_-iUdxskb_nK3AiLkY-Iu_rkR6IGTgmALNUgWh6pUZbcxEa5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gIQI88XNBf0mt5Rm269pIrALENXg2TaTqj4Bq3Z9qZ4NdyKcP4KMYUnENgDxnVF7m8SJh_vJsHKBMCLgJW6vyA3UNR7rxlUMNlQJaJrdkVlK76iHf10-lhO_WI3RHCBm0_Rpo5fudy3Dz_pnxYySztx4GjbnVDXLWskKOSczzrM9uVM17CjssaxtOEp18c5DZ_VFf8IJcaP20w1vUiWNd1K7BqiAC_28VAqs7NaZBmIqk7cvWF2usQAfQO107HNCW4V1-z6VT5cwkzl2gkbTi6xEXxpIXCDmlUB7-ewH1UvB9K2Otf4rrZuWVJH_uqzq16zw48LdnuLVnPxi8zbNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qS5mgFD9qSQAgibhozzn1MWO4EfV-vZxgAPWfFSaGD5ELrB_q0auU7WW-x5IS3Q86hNswpnL1KDiRaDmOsee7MFkpSOC0qD4CXkKdWrskEHsvPuaVNOGkuIHMk3YX77BXFZkPPW7t34RqWIeNBlO6a5uImp5RJd-TFjF3pjM7utjGaUEc0m2meT51uGe6LGdjFsNomN71-8jpQKESmInTiIlNrG-qs7OLVJEha5NWI8rMAkZRtKvh8u4wld6F3129QKs0_UolWeGciBiIZYP1LZ55KRRRk_auwjhyIG7E04hSn42he35fkK3CpVVtxYHBQcAgbL7r71zezWbexoP3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCNTVAJxDH2s1MLl0uc9mrOZbEH0vVnoDnFEKERJ6UjNi2F93dh_i7vVGR-rPG5rvKjhDOnjjzG2Lk_aYCoRQR9z0nWSJ2ZP_FagbDnx9AkLlA3mQ9L01ZpPw1Liep6uCAdXgBu_PR5hwgO_HYdbexrVPPkQXj3ROz4tX6GltO-6f9Wl65Nq9uxFOYcaXoaW4skXDlIzR9YMJe_XPgpNALzpG98cwRuezntctki7NID5j7cMmKZ0F6Dbpg739KyD12ebvrFcXMlcryAvgFBMDn4WFUOFw3L4WDjQ_E4vpH38hL8SZCxbdDMh4-gRxNNpd2h6PQ7nEByjQBB4-w72DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS8OIuxiypYDq-ah91Ab4sKhOluAw0H6I2h4ybW8pB--hpsF3HbrTIkFF89aGgA4cQz92yr3_pxHOBxkydTL3BiHB_0bH1ABPhrdXIyYz4aUmUusKrH3ab1C3fxGUY5S_mry8vAjjfBjwLZVoPMWHy8vUKIcKmccHmHzC542Ih4pLPhOfL9FhuP4THA11-FC0VUW3eI1xdrqoR_TL2uQti4OlJ0q7mAVlOoVNg45gXHmP-rNCaWrZdHh9ftpA-BL_sUIjZbNbzMOyyCWSJTRxJkkyLgZiVBeIY6wZ310y1U6aZFJ3YD0TkYr1Rv5R0NFK_ZrMUZlB7o-VNnQmyDoqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j1ag60hqz3kED4F6bMDjuUxR4aqYIk_A_nSjbnfb6Sgk3Wjd4ACE4UFqKcEVTHMaUnipWEQ8CVJMW3364hDU824qp-VC06WYAB4oyhEgj9MiGnaNemMF1vNLqoZiSrEbJa0Y5AYNWnhNUN1EZJdZH9COz9wqIpyHOdXX-0V1v9CXDwsityqELr1MYTlUvtxqLh4fRGvE-aRdD0rUQR-IfJqqXpeU1wfW1WB6zoEdAMxp5Vcx7N-uRLuPSEuwx5IvK7GAxBF8rSWFNFnLGAvlg4cyQ57P07G6C_I0IL8vYOsCjvDquqAkuYEXp47z2tpH2nloCGLkpFrlga4iLmkddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gYWE-gIeqGwkdXHzBi8X-L1m07-Qiv_r2FZMduQJWuplBDYwAM19_tCpCZKCK71G3YO9K-zR7G7W1pcMV2XhgGeF5aykNY2C5QfwNM1EFycOpsaBqVKaPETvqZgBpczWupIa8VF4dhlGtSLOtATllULSuVLpdY9FGttZtHEYwc6dk1fglKO_YYUU3dCZZGpPLHzjIVN0JtAM0jdptYMHZjfeRur9xQqAh6LDGLIVqzcu6zny4DALq84Pa_gPNl0U6OzU_x3l0Cvfiovf3luoQu4fa4KitJMYENT4Py9Wjm-PwdqCuvXCTHvmanULaFNmT2-FbMis6FUuJ0QMNi1vAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTD8V4-lNO8cISMZQPpRlxZNqDEEbzcKkpSQTe8N72rRmJatiqRCfcG-FG2MV6uL1TtaDNHSf0F2physDFbPq4OGwpWFzrYUdfUg1G_cn7lWOqWkN_5Uue7bcuz8PhkpYzWs-IhqyiOyEBsDcpkzwENqO9S8rMXMOdeRy8QCqXOlHs4rR5fjgOXivjkXbMwJ1rP0JTBw2m3nMcjLQgExFfEUqmspp3sm4iCyiZpRk9W5bWtp9mVSslR6lC8zb8E9iNxvDdstI8KXaUF9ZYykFAwxFi1pb7ksTVTJTfA3vbhXNNse-XIQhJWkM-7fDG3B7VBkh-rRaSDGNhkC2jTxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B1997XKkmBsOp9D-5yIBFqW5ol6kCFk3HDXLGLouF9RronSlq7-ma0t_nKec_M3wF76wBG0V60ANyL4YGJ6Dj1OC116VZ3lu_n1E4BFjs9KZ8_70sQUKWRK__UiUR7Ev1m2DRx_tCDx6D67ERgFn-U4K80aPmoe_nwsiaEoGeFC0DBMb4An_EDaOG4csU3NgYDU1k-YQwqNL2Qc0cV1CksOYutxsJ6bUCDBoVGR0libOFIB76YRYpZ8uxHkPAtYpRPq4LSdUhYb2OXhHjCxvazuZy85Lj1woCgV3tnVDBlf-L9nthUiiK3SpyeUJrQkN_b4aRnt9ggWQfV6YgYvO3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
با دانستن چند ترفند ساده، می‌توانید هنگام خرید میوه؛ شیرین‌ترین، رسیده‌ترین و خوشمزه‌ترین‌ها را انتخاب کنید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/677574" target="_blank">📅 07:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
تغذیه رایگان مدارس جایگزین برنامه شیر مدرسه
وزارت بهداشت:
🔹
برنامه «شیر مدارس» به «تغذیه رایگان مدارس» تغییر نام داده است. اولویت همچنان توزیع شیر است، اما تا ۳۰ درصد اقلامی مانند نان مغذی، خرما و بیسکوئیت سبوس‌دار نیز توزیع خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/akhbarefori/677573" target="_blank">📅 07:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfc6fd47bf.mp4?token=LuzU75zzjm6xx-9Hvu-K93kwxXAfMa0nE6MEVWKw-V9nCW8ZK2mqQ375PL815h4zKloPXXd9YpgEDz0C0EMoPoau_LRAt1xIIbjp_au2liMKKaWkT3cfGaGhQuTfx9TZ-sRu37gXicj5AjPeEhuLI_37ZrFrZ0dv1NJxJ8we8rFPz3qdmpohPSUNelD23C_i3Jeeti1eYaFYTfIEMwflqJmNb84cNQIDCqDJN9OcA1tKgajb7X23fltcxRMVpTUaA800Nvbrbh4RBxRcWbGIYL8bSxmL-W4eY-lzQsog1czhtkwOkPYDtp-VrpfXjUQ2mU4cJaCo8Ye1_oC9WIIOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfc6fd47bf.mp4?token=LuzU75zzjm6xx-9Hvu-K93kwxXAfMa0nE6MEVWKw-V9nCW8ZK2mqQ375PL815h4zKloPXXd9YpgEDz0C0EMoPoau_LRAt1xIIbjp_au2liMKKaWkT3cfGaGhQuTfx9TZ-sRu37gXicj5AjPeEhuLI_37ZrFrZ0dv1NJxJ8we8rFPz3qdmpohPSUNelD23C_i3Jeeti1eYaFYTfIEMwflqJmNb84cNQIDCqDJN9OcA1tKgajb7X23fltcxRMVpTUaA800Nvbrbh4RBxRcWbGIYL8bSxmL-W4eY-lzQsog1czhtkwOkPYDtp-VrpfXjUQ2mU4cJaCo8Ye1_oC9WIIOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تظاهرات مکزیکی‌ها برای قطع روابط با اسرائیل
🔹
شرکت‌کنندگان در تظاهراتی در مکزیکوسیتی، پایتخت مکزیک، با سر دادن شعارهایی از فلسطین حمایت کردند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/677572" target="_blank">📅 07:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677570">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OAvgr72ctDnep5MRflaUjacLKADbMKFbVYHsNW0DqJid_WBHBBD0SVumYrEXQjVX94n-rNQ5nA7q7XsSl7ztrjpNpDj6yOiEgp1Lhad6lQhQA0ZCyFUxz4EIlxxAkhfYONJgl4vcUQpxgAUu0rZZX59JSxZAaHtU59Eef64IgVLHlAjlhwGDeIhkIhWc7GWUrf-atfdfwKNVCQdvkIO-ZJ5YLAx9V8Dje2ssx4CPMCfFYWtBcCPTAJZYJCdPGRwSWwDt5VjQ3GhpA7yhBv4DbLrIosm3dmwAHR0s1b2NOi4U6OIUH-DC73TK9V4qU3zBzmf5ZJ3jR8XFNpZ9prnmuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjhFUhY6MYA4ZDi00olywJBF3nQt3VXC0FXKkdPI57LXoJE74GorlbcRxS6zOsgTqsWO1JGgFnfhsndMttwBUJYAwmtZvyRk-CZumjHRhIE6new-yZtp0MJyZN40wv0WFu79ijTz9otFARkGjwUKqdYoqa3Xv7GqjLJQqFhsmxHxMnv9fOxG3uWXmaX9AehwlM6afHWTreLT2zGV0Kl41p2Sm8khQROJbcGbe3lifpPUGD9iClbazAjWS4dRxeJfldrI_BtS7cxTFeeELOELl1c5_3urmdQ8cKgCWcBHfJL1upGHGjiJuqPi2i1Yb8t9iLNiEav133_TVA6xKtJTtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سدهای مهم کشور چقدر آب دارند؟
🔹
براساس آخرین آمار از وضعیت مخازن سدهای مهم کشور، میزان پرشدگی سدهای مهم کشور تا ۴ مرداد ۶۰ درصد است و در ۶ سد، درصد همچنان میزان پرشدگی کمتر از ۱۰ درصد است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/677570" target="_blank">📅 07:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677566">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f86c80e059.mp4?token=j_S6xzKTX8PLsYLpfGMLwo3I0Bcjyj2qrbpKNd02ydFau_pCZ4lK9IODCM15JYkggyrRUGitHqNdS9e918tIROn-4-nqS5cmvcxymC53UreSO4iOJs4HL2ZCCE3lGC0st2alyNVXjeyMzBw5Fj8Vw0GyPVjFJeR6H5u6Q5KsiieSR4GFCEN7hMiOnJi5EJmMdiBqc4AnxXW9jXsj-OkxSWl2fkTAQIOc_msrJdpaAeacJun8zvuD7GttcipdFQ49HxZL6d4Ru0HwdQ6HutHoZKJH1pDo6pSG5u0xyQA_Ff0MXLrEZfGlVFv9_jfNxelVAm6jaduDR3BDL4cj7wVh5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طوفان آتش در شرق واشنگتن؛ هشدار تخلیۀ فوری صادر شد
🔹
در میان وزش بادهای سهمگین با سرعت بیش از ۷۰ کیلومتر بر ساعت، آتش‌سوزی مهیبی شرق واشنگتن را درنوردید و هزاران نفر را مجبور به فرار از خانه‌هایشان کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/677566" target="_blank">📅 07:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677565">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggyaFHQzrp9gzTTXTTHX9xulpd6vqA_hxr6SA1w81G3rw__sDeKlzSyVx_DH5J5yrI7oyVyNSI2H1sa8FZqysNQTX8jZa4YTzCWRGckxldPuh5L0hDCBKdaXPAcQK7Y_k3H0tEcAgPpZazs7gr6KjVdGlatBIZGVgMBC3phntJtjiV_0zL1TOllPoT91fha-AnjIy-OX4iAkX9KmT5njyvgAaZmy_6mFZKuEOiamhx6XHaMUgjipxhwzvbyweoSAHidfOrB_KCwB50NwuV0axMzpiho55P0Sqs3Nhxa4mars0dMzIoZPMy3Uz_TK9877ala7qPQoeoZ_eJWloQ5tHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای نیویورک تایمز: گسترش حملات سایبری به سامانه‌های آب آمریکا  نیویورک‌تایمز به نقل از مقام‌های آمریکایی:
🔹
دامنه حملات سایبری که سامانه‌های آب در ایالات متحده را هدف قرار داده، دست‌کم به هفت ایالت گسترش یافته و احتمال دارد شمار بیشتری از ایالت‌ها را نیز…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677565" target="_blank">📅 07:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677564">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">پادکست کافئین | فصل‌دو،قسمت‌ده</div>
  <div class="tg-doc-extra">عین القضات همدانی</div>
</div>
<a href="https://t.me/akhbarefori/677564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
🔹
عین‌القضات همدانی
🗓
در این قسمت، بزرگترین کلاس درس تاریخ را برای «پرداختِ هزینه‌ی صراحت کلام»، «شکستنِ تابوهای ساختاری در اوج جوانی» و «حفظ اصالتِ درونی در برابر سیستم‌های مسموم» مرور کرده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/677564" target="_blank">📅 07:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677563">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc1795597.mp4?token=SRqp3NxO9w_IOI5x_wzi1ypG26PfiuFn1VVlYe9MB5XMyiyQWR4o-zUY-M40GKEIwfwOhJnvytZflpe4tRIWhwmTdM7DAAsJbceLTXCR-ixjTXZ1qubREvJj1KDPnoDNGTxuGJO_nPu-4FeVCgQGYqLsjvY-OvcjIxwV6y7j68zDhtOCzSt5jla9gYXAX8yJV7OCcrbCAaBfxxDQtHIDyFdLAJvQfxrW1cZrftmZeYR0f0MUamUofQZndZ5KaxpWWHN9__PZ3FlkdsdvJaolZAHslgJK5MXQ0F_wFTU4iv1FCJGujbasDki3zi0VUu48EjSHU5x4Zsun5MC_Y55wpLOPtc5mzR9Fij-JfY88SIoAdNZQmOAxPlznV5gomyXkyjtljch9Z62Otb3u31c3rHzh60mbyqmcZ6w2T-6jf8jb7oQakJCTnlKuTRQBBnm37WtV3n81ENICZGeyy5Koa9pzy-7o-LNY-3ySMcLnvCjOAL4CRFJyKRIHALbWJTvv1GAsoDOVFaD8QbCivGu-mAGIDeu42DDlUfQj6Ipd-YaA2Y_Dm7_s9QuPW0TPqzfjq8pRwRlFxp9IqEWZX0jXtFxMaikj5pq2FLSBZzGnb7u7ncPoCcVDnMl15AHRqzfS4xgcgAklPU4ziHKrmciCZ9zmW_LiYsa9XDwAqwiJ2g4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عین‌القضات همدانی و جسارت بیان حقیقت
#پادکست_کافئین
| فصل‌دو،قسمت‌ده
☕️
🔹
اعجوبه‌ ۳۳ ساله‌ای که نشان داد وقتی یک مغزِ مستقل و جسور، خط‌ قرمزهایِ منجمدِ سیستم‌های متعصب را به چالش می‌کشد، چگونه می‌تواند با طغیانِ فکری‌اش خواب را از چشمِ حاکمانِ زمانه برباید؛ حتی اگر بهای آن شمع‌آجین شدن و مسلخِ جوانمرگی باشد.
🔹
هر روز صبح با یک شات غلیظ از تاریخ، آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtu.be/hwciVLCsnpI?si=Sn7kIHdYXQ8FWRVS
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/677563" target="_blank">📅 07:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677562">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHvn1hoy1_qI04jev1SUQrv_uRu6-V3TD_Zlar1x_h2MWMDjhRnRQkUvBata08qgMXpJwCG2DQzZ5E4YNnbrOOCS7sFBv82FFfymiAJ9JksxirEkCoQvRHPv5QPE3ZnHfBGpRAAuyxnBN8Ufm_TFHo3HjqhKsKq_j3OxWBcsQwcv0WfArtZs_lr3GSt30vPotldbYfycJOoDTxLNtEWMup0w4YakG2R9n9HOMPLbVhK9IVBfogK8xdalp-nPkVZbeqfcGx063dwAllHHTqmS21E5cdoUA4dBuC93r1GIh068y0o0chtVml67CQfLx1hmPl_nWAMsczM-0rY0JJijPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز یک‌شنبه
۱۱ مرداد ماه
۱۸ صفر ۱۴۴۸
۲ آگوست ۲۰۲۶
یکشنبه‌ها
#حدیث_کسا
بخوانیم
⬅️
متن و صوت حدیث کسا
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/677562" target="_blank">📅 07:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
ادعای
منابع خبری به نقل از مسئولین نظامی: ادعاهای تروریستی رئیس‌جمهور آمریکا مبنی بر اینکه ایران خواسته است حملات را متوقف کند، صرفاً یک دروغ جدید و یک تلاش مذبوحانه برای باج‌گیری از حاکمان خلیج فارس و تحت فشار قرار دادن آن‌ها با تهدید است
🔹
چه او به تجاوز خود ادامه دهد و چه از آن عقب نشینی کند، نیروهای ما در بالاترین سطح آمادگی قرار دارند و برای هر احتمالی آماده شده‌اند. اگر مواجهه اجتناب‌ناپذیر شود، میدان نبرد تعیین‌کننده خواهد بود و در آن زمان، همه خواهند فهمید که چه کسی قدرت را در دست دارد و چه کسی کلام نهایی را خواهد گفت.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/akhbarefori/677561" target="_blank">📅 06:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
ادعای المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت
/
موضوع کمبود ذخایر موشکی عامل کلیدی در تصمیم ترامپ برای تعلیق حمله به ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/677560" target="_blank">📅 06:44 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flb3iM0STzAChgJJLrdcwCa7J8AS_i5wtrrpi3bGfGLKaUeEbkQ69R56yqjbVREAcoBSTnDjG1M_cbHhZVcKcEtz0B4BNLKA9PO-wadv9VEIVJrTtgGQ4MlZag62httEfCMQ7BX08tSs4uJ-Sp0MNNrcpA6HMhk5GmkcCGwtJ86AYks77iNyfZp89HvQVh9rQlzZDPrSFXnlT6daaWAFbkPdubqTh5hp74aLPQlzneUPyQaEt2txCnUKfPcfa3oIL-orbavaiG-dgiv4aK96NtKz1od-qs3egB7lI9JwhTYxAE1dLSHg9UlONkS8_ap0zaBNkG8swgQbIcXmhPuvqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای خوک هار: من با لغو حمله به ایران موافقت کردم
ترامپ:
🔹
ایران و دیگر کشورهای خاورمیانه از ما خواستند پس از توافق بر سر چارچوب‌های یک توافق، هرگونه حمله را به تعویق بیندازیم.
🔹
این توافق شامل بازگشایی فوری، کامل و همه‌جانبه تنگه هرمز و پایان دادن به تهدید هسته‌ای ایران خواهد بود.
🔹
با توجه به این درخواست، من موافقت کردم، به نفع همه جهان و همچنین برای اطمینان از اینکه ایران موفق و مرفه باقی می‌ماند، حمله را متوقف کنم، مشروط بر اینکه توافق به‌سرعت حاصل شود.
🔹
ایالات متحده در آمادگی کامل رزمی قرار دارد و برای اقدام علیه ایران آماده است.
🔹
اسرائیل به شرط دستیابی سریع به توافق، در پایبندی به لغو حمله به ایران با ما همراه می‌شود
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/akhbarefori/677559" target="_blank">📅 05:46 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
اعتراف روبیو: ایران هنوز موشک و پهپاد دارد
🔹
روبیو، وزیر خارجه دولت تروریستی آمریکا، در یک اعتراف به شبکه فاکس‌نیوز گفت ایران همچنان موشک و پهپاد در اختیار دارد، اما بخشی از توان دفاعی متعارف خود را از دست داده است.
🔹
در حالی وزیر خارجه ترامپ مجبور به بیان قدرت موشکی و پهپادی ایران می‌شود که رئیس و وزرای کابینه تروریستی آمریکا بارها در اظهارات مختلف خود مدعی نابودی قدرت و توانمندی نظامی ایران شده بودند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/677558" target="_blank">📅 05:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677556">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba29a66c61.mp4?token=ZlIzSQCfB1l5QpPJzO4YxWiY_mjH_QoAjPDsDkz-aquejNGoth_gWYInLmPsoazN168IOKSpaDg64FRIbxdaKXIhY8nI2li5qBfcYdxPRivnMqYlob3eeuwQ9kiCtHbv_SKvmU46yNLIovDsU6AUVsT2sPUkJBS5FhLd_vw4sP3SKpX2c4e_7Lk9AIQJM5wm_itzbnwXlDU8Vi9RYZA4c-DxBkg4JpOpxnsqLWmpwH9YjO3iK8EjOIuZ3mhXF6S968FjjL2UoBLQq1uZPd3GT0OjxqR88ZqeS18DKYJZfynpleuFn2R9z6vvzYqKXDrb-Plp1DGNvw06BLyeWchoSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba29a66c61.mp4?token=ZlIzSQCfB1l5QpPJzO4YxWiY_mjH_QoAjPDsDkz-aquejNGoth_gWYInLmPsoazN168IOKSpaDg64FRIbxdaKXIhY8nI2li5qBfcYdxPRivnMqYlob3eeuwQ9kiCtHbv_SKvmU46yNLIovDsU6AUVsT2sPUkJBS5FhLd_vw4sP3SKpX2c4e_7Lk9AIQJM5wm_itzbnwXlDU8Vi9RYZA4c-DxBkg4JpOpxnsqLWmpwH9YjO3iK8EjOIuZ3mhXF6S968FjjL2UoBLQq1uZPd3GT0OjxqR88ZqeS18DKYJZfynpleuFn2R9z6vvzYqKXDrb-Plp1DGNvw06BLyeWchoSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری بین نیروهای یمنی و نیروهای طرفدار سعودی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/677556" target="_blank">📅 05:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677555">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRBwzgwXzY7nQyxv4nD9Ggja7izOt4NXSj-kvQ5B8vkGyfc3pwsn05iloVo9X-XBrPrJ_oYl35sjAXboaR7gp5tZZDbhW3hcxhMIn8F1dPvYxyGmQI_1b_Ykz3p_AKAFl8PljR9sBcO5QNm2dYFWj1hL85o3CidzTi0k3wgqO-J_CldczigUUOodyh2uNPXrmcyLMUXy-kXcuRVIQdZnh2XVTC9QMw9d7vvJYTJOh7mwW4C0-oE6fx6R1H5X4ctQ_cohFkm_hEnkvOFtmXoP8h5Q20maQfFoV_gLJbXOO0d_CbOLMdXOLoowmvK30mrLp9Ed7zJaqmQCfCnjAHnhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیست و نهمین پست سگ زرد در ۲۴ ساعت گذشته
🔹
دونالد ترامپ در ادامه پست‌های رگباری خود، تصویری از جلد مجله نیوزویک درباره ونزوئلا را منتشر کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/akhbarefori/677555" target="_blank">📅 04:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای اکسیوس: میانجی‌های قطری روز شنبه در تلاش برای دستیابی به توافقی جهت بازگشایی تنگه هرمز، به‌طور جداگانه با عراقچی و ویتکاف، فرستاده ویژه کاخ سفید، و مقام‌های عمانی گفت‌وگو کردند
🔹
به گفته یک منبع آگاه از این مذاکرات، این گفت‌وگوها پیشرفت‌هایی داشته است، اما هنوز مشخص نیست که این پیشرفت‌ها برای کاهش تنش و مهار بحران کافی باشد یا خیر./ انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/akhbarefori/677554" target="_blank">📅 03:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ادعای آکسیوس: بن سلمان، ولیعهد عربستان سعودی در گفتگو با ترامپ نسبت به طرح آمریکا برای حمله گسترده به ایران ابراز نگرانی کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/akhbarefori/677553" target="_blank">📅 03:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
کپیتال وان: حساب‌های ترامپ به دلیل شناسایی تراکنش‌های مشکوک بسته شد
🔹
بانک «کپیتال وان» در یک پرونده قضایی جدید اعلام کرد بسته شدن حساب‌های ترامپ در سال ۲۰۲۱، نه به دلایل سیاسی، بلکه به دلیل شناسایی موارد مشکوک صورت گرفته است.
🔹
کارشناسان واحد ضدپولشویی این بانک پس از ماه‌ها بررسی، الگوهای تراکنش مشکوک در حساب‌های ترامپ را شناسایی کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/677552" target="_blank">📅 03:22 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای رسانه‌های امریکایی: در پی درخواست‌های وزرای امور خارجه ترکیه، قطر و پاکستان مبنی بر آمادگی ایران برای برگزاری جلسه‌ای در ژنو، سوئیس، به منظور ادامه مذاکرات، فرماندهی مرکزی ایالات متحده به طور موقت به مدت ۴۸ ساعت، عملیات شبانه خود را متوقف کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/akhbarefori/677551" target="_blank">📅 03:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
منابع عراقی: صدای انفجارهای جدید در سلیمانیۀ و اربیل در عراق به گوش رسید
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/akhbarefori/677550" target="_blank">📅 02:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d85ffc549.mp4?token=oY9jtBKzwMDQFRjw1zYQD2-tYs98oL-5JMRkeMY1L-L35Lrat8JJOrTHvm72PsDlpFfBo1OVxpVGXS3E9QmZ6MaAXKUaFVe6zNRlXvvEpBfb0Ls1Lhe_e2tmzkYhkfaOo6_o1YrC9_MXrzP341pZpZCrMC9f5ecnPY5rAOec0ReI9eehk44KTCvhoh8qrxsYq_eurRgosbCupxlSaIq0-7gVGOkXG5vt3UwtTo_jhGRZqOnXxx9StfTZS22c7fAuiyJEvGk-e7KRHf9IWUrL-R3SmKzPleMGJdQaEHFddFgrhHxXmvTVz0ig4Yqpy9u3BGDFCrCXGVUlBqb51BFfbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستون دود برخاسته از مقر تروریست‌های ضدایرانی در سلیمانیۀ عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/akhbarefori/677548" target="_blank">📅 02:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b60f221b6b.mp4?token=umgMP99pKjjlTQe9MTDUA_8F897D66OMD2DRONahMTg84LGCPz3NrrZJKgd1fd87UBXsK1rP-WRto8whjToKLWK_gv3v7sd2o2Zm3rW0JI7_6XnJwAPYok8JXUqo3RB_HLGploEQgdO2iYpN9TfmKzRWJYdpNeEaZTNIhukCYJm9MU-mmHirN5gfJ16kZUkCWdCuwOsRG9DZ_ELkGj33EImGWj7Y0GNU_0v1k_AQuvVu_cEibzsX419rz4MEWCy5ouRbUu_xBq6k7S022XH7gdf3q0_JFc1rw38Sk560E4hDLwy2grvfx2QkY1hwXUGfq36XazmPIhatoufIVnRvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b60f221b6b.mp4?token=umgMP99pKjjlTQe9MTDUA_8F897D66OMD2DRONahMTg84LGCPz3NrrZJKgd1fd87UBXsK1rP-WRto8whjToKLWK_gv3v7sd2o2Zm3rW0JI7_6XnJwAPYok8JXUqo3RB_HLGploEQgdO2iYpN9TfmKzRWJYdpNeEaZTNIhukCYJm9MU-mmHirN5gfJ16kZUkCWdCuwOsRG9DZ_ELkGj33EImGWj7Y0GNU_0v1k_AQuvVu_cEibzsX419rz4MEWCy5ouRbUu_xBq6k7S022XH7gdf3q0_JFc1rw38Sk560E4hDLwy2grvfx2QkY1hwXUGfq36XazmPIhatoufIVnRvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرواز پهپادها در آسمان سلیمانیه به سمت اهداف خود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/677547" target="_blank">📅 02:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/akhbarefori/677546" target="_blank">📅 02:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d948585bf.mp4?token=chSxA2x9El1rad8ZpBJDJj2RndhVzmi6Fv4ybeJzDWI05IFPvVxbaAelMY-OPjwUnNIQdIG22z9NI5o7xpFh_bnkc47zostjtk4OkyqsooGJQu8pNuStq9f1tc6UO_qqh8Xz0e-F4u3h1HnlqL4-TSNqVkU_DQnuODVuvYN7SrPr-9FRUh-V0F99UwofofIeUNj2XdwrTrKf-exfFqjrBjStZGXoyIBClVOfIUdOfS72-3txawp_yThedNzx6MCz2NVb8SIPx_bbeRieTHXDech9128K5x838YXui1E1Xu1XNl1zJzrttGcoOn9AnTwPeDJ2bNGTER2IEG9DfaZHvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d948585bf.mp4?token=chSxA2x9El1rad8ZpBJDJj2RndhVzmi6Fv4ybeJzDWI05IFPvVxbaAelMY-OPjwUnNIQdIG22z9NI5o7xpFh_bnkc47zostjtk4OkyqsooGJQu8pNuStq9f1tc6UO_qqh8Xz0e-F4u3h1HnlqL4-TSNqVkU_DQnuODVuvYN7SrPr-9FRUh-V0F99UwofofIeUNj2XdwrTrKf-exfFqjrBjStZGXoyIBClVOfIUdOfS72-3txawp_yThedNzx6MCz2NVb8SIPx_bbeRieTHXDech9128K5x838YXui1E1Xu1XNl1zJzrttGcoOn9AnTwPeDJ2bNGTER2IEG9DfaZHvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زبانه‌ کشیدن شعله‌های آتش از پایگاه‌های تروریست‌های ضدایرانی در سلیمانیۀ عراق
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/akhbarefori/677545" target="_blank">📅 01:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجارهای پیاپی در مقر تجزیه‌طلبان تروریست در سلیمانیه عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/akhbarefori/677544" target="_blank">📅 01:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgS7JgROEyJ3UxTlziKDA4m7fKwHK_GMxh4nYD6A8BFbwpw5-_A14CzqiIvkt6SxC-TYp8l9jEuo6UH6STa5BEXg5m9fXNRWTCYm14ypa2AXyQtrYYOMZoOjLtEvLhOwf7ORT68lDCOhvU9CJlQPSWlNOkNCDFjUA1rCFTZKMfdhXmHxJ7ZlHxdH-S5JBdXK-LTRWBmzjmfN0x9kgeRNJMnK2JlXcsc1C1af6S1-1W_SsIkb5AQkaDfn_0ADElD6asv3vMjyAKOTBPs5iYvS1BeEW9BHuyIGxj68lKf_XTB43h98tX6L8g6YWWzL59wedQmeAotK8vuqTZrT7bbIKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
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
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/677543" target="_blank">📅 01:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY21ulq2bo8rqMreM97TTLrnsXzIb4JVALNXu9EJUh5Z5Wo2PUcz8MFg6-mKfNfT336W583k9_dk8tmZafRdWMDmNv-k2o5QYNtPSklXwtyxSYIWWB-DDBtfZnRsgEzzVNmmsI_g_bLLmKw0ZTCGsbVGFsgiAekd4163HuLm7kr-G771Is2rFd1eDA1VCFRQsV7F1WdQMA3UaqEc6zB--BwmCPohn_jfyVXlszBfnBay6jUoswjEbYJI1F8o_CkgNuU3lHN0TQeJgK0dJEzvx0RHFi_FBqOB3iNAhPNV7yhORchFx6H0NLYvuwJple2KS37taKEKaSmw96C3KbUW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو سوم آمریکایی‌ها: جنگ با ایران ارزشش را نداشت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/akhbarefori/677542" target="_blank">📅 01:39 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
وقوع انفجار در یک کافه در مسکو
🔹
خبرگزاری فرانسه به نقل از پلیس روسیه از وقوع یک انفجار در کافه‌ای در شهر مسکو خبر داد که منجر به کشته و زخمی شدن شماری از شهروندان شد.
🇮🇷
✊
@AkhbareFori | Linkظ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/677541" target="_blank">📅 01:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
هشدار رئیس کل دادگستری گیلان در خصوص کشت مواد مخدر در روستاها
🔹
رئیس‌کل دادگستری استان گیلان با تأکید بر برخورد قاطع و هوشمندانه با جرائم مواد مخدر، نقش دهیاران را در پیشگیری از کشت مواد مخدر کلیدی دانست و هشدار داد در صورت اطلاع از کشت این گیاهان و عدم گزارش آن، با متخلفان برخورد جدی و قانونی خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/677540" target="_blank">📅 01:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677539">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه: لایحه کنوانسیون دریای خزر در انتظار رای نهایی مجلس است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/akhbarefori/677539" target="_blank">📅 01:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">40 Rooz</div>
  <div class="tg-doc-extra">Mohsen Chavoshi</div>
</div>
<a href="https://t.me/akhbarefori/677537" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
۴۰ روز
🎼
چاوشی
🔹
موزیک جدید چاوشی به مناسبت اربعین حسینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/akhbarefori/677537" target="_blank">📅 00:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDRA1vdwii2NE4Egh4LI4G-tKc2ZLajNeZTPR_lDMgzBiGpmzTTyFRSD1xyHuVnOCGd2fRTxFw0nKXBPKsXyPXITiVJE8mPUjq_xzZJUtDg9_J2NgPq4ho6tsxOpoaJe59tfUNavFWl5DM3u3eiNhfUFJGh18FmQ-AOq4voEZkaN4JjyhIvkCQotkjfL769jk666IFYKs0FUTMt-oua-CUU1kxdtOWYuU98r-St4PXIi7p5IM8O955lbJQeljW-40etB-oIrLlgfmK52W40WOs4HYmTKtrqVhbsUhOMo3NyxQNQC9mm2VWVaq8XFAtZ1QOaMnre12-XNY4FJwvewFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزارت خارجه: تداوم محاصرۀ دریایی و حملات به اهداف نظامی، غیرنظامی و زیرساخت‌های ایران، مصداق «عمل تجاوزکارانه» و نقض منشور سازمان ملل است و ایران از حق دفاع مشروع خود استفاده خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/akhbarefori/677536" target="_blank">📅 00:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AtVXEL0pDbX6YM5B5JM0ryxA6zrBXA34OCVP9vqfWrYIB00iAvha-7K4-Ru0Ba_jv9qLQvdlDu-tSbdSjpVXCU_iX_lBCDEbFEkstJqZ-D2fvUGPlZt9i1bfTbdG80ZrD3fKXaSyXFFmvLSiKkTHGCSQ_JfGyw6PikobN2FzElaWIaVSaKTKnRoNLAmUeFe4cNz9NovS1KP3BWYDtAllFK12apqqp-Dq2Dw32c2dH2D47tHz7rp1UmrFCzi4CWs-GwoThGUsGk7s9Tn0hC5h-junnx30luXE9B8qXRgZDAuP-JcmPDW2llFb3KB3e9mHS9cU9WmckcRsNk_XfB44bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تجاوزکار می‌بایست با تابوت برگردد
🔹
طی روزهای اخیر تب جنگ در منطقه بالا گرفته است و به نظر می‌رسد آمریکا قصد دارد بار دیگر دست به حماقت بزند. آمریکا اخیرا برای شهروندان خود در منطقه هشدار امنیتی صادر کرده است اما با این حال به نظر می‌رسد این هشدار صرفاً محدود به شهروندان آمریکایی نخواهد بود و در صورت تکرار خطای این کشور فراتر از شهروندان تمامی نظامیان و منافع آمریکا در منطقه و حتی سراسر جهان نیز در معرض هدف موشک‌های ایرانی قرار خواهند گرفت
🔹
هشتصدوبیست‌وپنجمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/akhbarefori/677535" target="_blank">📅 00:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf3TMCj2DuLiu1YuqWHMyB5XKAveI19nbSDStKmmd-h1lYL_Q6ASeBzpGn77uCtRUTBjt7bdceXi40T9InCNkpaCNHdc1fxQCQBnYc_t6jPbAAwzvMrRu5-gbwOFI0yUhh0sSDmuO0bImK0Cr989sQ_IfaExq82xL1HjyIAWVUos5zm-uioMS65gAlcWammf8AIi0thLYKDsucjdPKkZwcMUvYPifFqBHBTEiV3KHKwEXNLTzqTEF1ZTuyNF4lg7Hv-oTi8U6ZUd3GroL4q2BmqH6E6vlgUqsvEPJajGAaNbUAa71--Xa2MIsGxLBnXoJjY0avCMFys041YupEL4Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تعداد هواپیماهای سوخت‌رسان آمریکایی در رژیم صهیونیستی همچنان در حال افزایش است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/677534" target="_blank">📅 00:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIXZ76Jt2R0nJ6SdLEw3-0IJ3tgUzpmheI2Hr49s0GJ4gpfyAm2iUeG8xnusCYoAHGlcEXuNO9cwe_AlNgVQJ7Li4VIGN8dPhL8h032YLS5F8tPOkaw5LX8aEjFGN4_b6nO2pc0tZW1QfbwHdkaqvOduXNn3CbJF7iutmfvTcKfwkyzVNUN7kH8PaxO43a0XFoaQHNbl1DBQWazAdnvJbibLzcHzLAEbNaqQyFBSIkb9i62uHPaJNFaPuuZak9kGHCeSnP98o9v3b24GrWmXUVq_LrsBNKW4B-N2K24j2SKnbzcuVST0nJAWboDeZGB-MXF1k6FSz92eK_S5hzN9hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دو سوخت‌رسان آمریکایی از فرودگاه بن گورین برخاستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/677533" target="_blank">📅 00:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677532">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq4RhFN_8xrTXSj3Pbwh7AaFPpGnvM-eUKtVSWblsL09fubDEHaLuqpnsBfL8pyIqSsQ4HxnkpNDa6x8IvxIsaDdeFEKxlOys2sucR7y4XwzA2qTABfIIjk1dDZ91VjptdiX-equtZT1W-il-qSzMw3pPvj2e28gkAV6jnVOu0G0d5JxEGLBXQ4bfrNyk5j0QFeRdrGXp3eeJ9-3Db_jV_y8vf5rmybTm7F4gfPkb58KqqI4SW_fEJj0QNFvp5ExHaxldfdRWneUt6ToKv66cCTMupDicHfQkwfvV5Xsq3V84S-l6WE1JdPMFHKWgAsYjhMu3K6pioUAenkfGWb-pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک هواپیمای شناسایی آمریکایی (آواکس) از پایگاه شاهزاده سلطان عربستان برخاست
🔹
براساس داده‌های ناوبری هوایی، دقایقی پیش یک فروند هواپیمای آواکس آمریکا در آسمان عربستان به مقصد یمن رصد شد.
🔹
آمریکا این هواپیما را از سال‌ها پیش برای جاسوسی هوایی و به عنوان رادار متحرک طراحی و استفاده می‌کند.
اخبار لحظه‌ای جنگ
👇
khabarfoori.com/fa/tiny/news-3234810</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/akhbarefori/677532" target="_blank">📅 00:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677531">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
آماده‌باش سراسری در بیمارستان‌های فلسطین اشغالی
🔹
منابع عبری زبان گزارش دادند همزمان با افزاش تنش‌ها  در منطقه، تمام بیمارستان‌های فلسطین اشغالی در وضعیت آماده‌باش کامل قرار گرفته و به کادر پزشکی نیز دستور آمادگی فوری داده شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/akhbarefori/677531" target="_blank">📅 00:30 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677530">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
کاظمی: برنامه‌ریزی‌ها برای بازگشایی به‌موقع مدارس انجام شده است
وزیر آموزش و پرورش:
🔹
سال تحصیلی جدید در شرایط فعلی، طبق برنامه از اول مهرماه و به‌صورت حضوری آغاز خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/akhbarefori/677530" target="_blank">📅 00:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677529">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چند پیشنهاد جایگزین برای گران کردن بنزین
اسماعیل حسینی، سخنگوی کمیسیون انرژی مجلس در
#گفتگو
با خبرفوری:
🔹
افزایش قیمت بنزین در سال ۱۴۰۴ نه مصرف سوخت را کاهش داد و نه وابستگی به کارت اضطراری جایگاه را از بین برد. شنیده‌ها حاکی از آن است که دولت دوباره به دنبال افزایش قیمت بنزین است.
🔹
پیشنهاد جایگزین این است که ابتدا باید سیاست‌های غیرقیمتی و عدالت‌محور اجرا شود. انتقال یارانه سوخت به کارت بانکی متصل به کد ملی، صدور صورتحساب الکترونیکی، توسعه سبد سوخت و توزیع عادلانه یارانه انرژی می‌تواند فعلا راه‌گشا باشد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/akhbarefori/677529" target="_blank">📅 00:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677528">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3af1f4879.mp4?token=TE80ialzJ5eakYfzxrunulnId8naxacv-BkB7fLYPJ_tUqmKSDolB1eBm8a5XhRGIWroBoDhhMmIoAPLBVnmYFyiV0XNn0sYanttr4sZQxHSGUrLer_fSmzaJQw8hc-DrTveNNVg-dFUhqGqA0t-1ulSYykOaTpvtaxTaScxu51biUhyXVZLbBFqtSeP76WuoJaEh_4PyPvlvLtcVGzITljPldPkf9wSQvYgU_tYw2WcafgVnwLb1rS9Eb3xpUss9DocrK4Uoy3LFXfCO9RAnv7WoDomXdZYF1wN5hYwP9cP095h4tJ0lpBX9ZEare5_RQ-xwvt2YTAKk_mamtszzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که سوژه شد؛ شکستن صندلی کنعانی‌زادگان در میانه مصاحبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/677528" target="_blank">📅 00:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677527">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66cf7e52d7.mp4?token=Xpi18RNH83g7ZafRstbJY62pzEhF33qMKjMrKmjPZW3x1zrqkFeWRSrWRBopX86-XMk2W9lmaQAMOwYHr9BtQ02uUamChwY7tkMd0TyyPEs8Xq-tsfyigXiSmWtfW3_e_bYlPeI5OYdBbsB9DKrYqz1Hg7TM6r4nWrxCdAsp-Ww8LiF_aqQvwXGEtuUd5ExyQeL6Gd3AzlsJyqx2YW7QVRJsxw0Bks5UIU00P3cOlSVM4WOnv9Y4L-Pc20UhRq3ApjlY1Dwp9ij3235OdDEIMlePmqTyKs8k4eVWc8vPOl-JXEAGEKyPRk7QptcJ0pzypMBquDrsI_X8e9IdLk7UGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های اصیل ایرانی؛ هویت بصری ماندگار در هنر و معماری ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/akhbarefori/677527" target="_blank">📅 00:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677526">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVXaagVgm5wyGmqob0_iZs_yrdtHeL1PCk20g0aq-iAu4wuDlhYCmNjrkikLmGLFK2fsVPLtJ_6dee6kE2ubIggeGnRMch22UnN14_cisced3G6-cgqdlrwTYsgI53dRWrLIG6bseCoOIzBJx7nB1Jzm34ZNWi56GDrs8V0CInewD9WqH8qmRD982Z67D5_L7bP4e8Js_f0squyMxXEWttFN02FJgC1SCisTqpBS4JQRmXBgMV__tSa_sY5RY4_5UwSqwr3p8IjlsB1FdggQ0R3MfXNllQTkGOIh5jbYv_f9iz5RCGP_ZvnBCTat9gJSvRPfgngxEQYAfGxeWC3E6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
هدیه سفر کربلا برای ۱۰۰۱ نفر از عاشقان حسینی؛ زیارت آقای شهیدان به نیابت از رهبر شهید انقلاب
✨
‼️
کافیست عدد
۲
را به سرشماری
۳۰۰۰۱۱۵۲
پیامک کنید.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/akhbarefori/677526" target="_blank">📅 00:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677525">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
ادعای المیادین: اطلاعاتی وجود دارد که تأیید می‌کند گروه‌های تجزیه‌طلب برای انجام عملیات علیه ایران، از خاک عراق، در حال آماده‌سازی هستند./انتخاب
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/akhbarefori/677525" target="_blank">📅 00:09 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677524">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de4ff1be5.mov?token=l7FU43D-ZT66ZShEC8qDBojgIjcuhsgnhgKSXoJ_MvfV3gEFkAkxx88PYikCQ0trxnY_kzs7ZBDcfrj47GOsTFLf1av7OAWBclqirQ2GSQXp4E8F94IoJFGuxHJvVu8eBO5hyzsjezR-LpU-6x9F1HQ7inNbE7ZPhLE7MckOmIW4I1v3O0jacY6SVIfnBML04okssImsw4PKve2hQ63JOYrH9ccSEhlc_fdOKNQ-IuFYRHFhAsN2c3cPqoI64IVV9PYKvxmjZY78pDNM-oAk40KAYLSst2G2-oS2lxfAl7HqvTCovfmWfZF1qjr3NRez5Mz1wuBW_c46fqcP7Ilmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم اکنون|یک بمب در محل جشن تولد ژنرال الکساندر چایکو،فرمانده نیروی هوافضای ارتش روسیه منفجر شد
🔹
چندین فرمانده نظامی روس کشته یا زخمی شده‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/akhbarefori/677524" target="_blank">📅 00:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677523">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
نخست وزیر عراق: هرگز اجازه استفاده از خاک عراق برای تهدید کشورهای همسایه را نخواهیم داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/akhbarefori/677523" target="_blank">📅 00:02 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677522">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffPRpWRoS_FpV3aBwYvH_83pJTph6gitqX0NyasyCuIhwV5q6m-1nchpAs3TTAY2-u6VO9T1uic6KpxzHEMJrqs5Tk09O8RJXMch_DrUu8-ti-DpPeStHbIsO2uqJzSRMjZRh5wT0i33tqqpDJ8LbjKmHYatiF84UchTag6VKY65r2GkaJ2GX_vkUWKDkMaqDnmC4YkWjtdtsKhshHowjtUikYojIxazDLDnYQm9npdD8Vq0phdrcJiEQFhb6dcZ1L8e6nkuSmGXOqVTdP7InGuZL6qU9pke51QXHxp1NJA7ZJh0M5Vo4FNFrHeXoK97WGRlIaM38i0Yb47TPnmt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/677522" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677521">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را ازدست ندهید
🔹
🔹
جزئیات تازه از احتمال حمله قریب‌الوقوع آمریکا | نتانیاهو: دروازه‌های جهنم را به‌روی ایران باز می‌کنیم
👇
khabarfoori.com/fa/tiny/news-3234810
🔹
جنگ ایران در پیشگویی باباوانگا پیدا شد | او از چه گفته بود؟
👇
khabarfoori.com/fa/tiny/news-3234757
🔹
هدف از حملات احتمالی آمریکا به ایران چیست؟ | مدل جنگ عراق تکرار می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3234815
🔹
افشاگری تازه مشاور پیشین احمدی‌نژاد از حمله به محل اقامت او + ویدئو
👇
khabarfoori.com/fa/tiny/news-3234644
🔹
ماجرای درگذشت فرمانده بسیج شرکت ملی گاز ایران در مسیر اربعین
👇
khabarfoori.com/fa/tiny/news-3234640
🔹
با نصب اپلیکیشن خبرفوری، از خبرها جانمانید
🔹
https://B2n.ir/jb2310</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/677521" target="_blank">📅 00:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677519">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
چرا ایران با هیچ کشوری قابل مقایسه نیست؟
🔹
آمریکایی‌ها در مورد ایران اشتباه فکر می‌کنند و معادلات خود را به غلط چیده‌اند. به اذعان کارشناسان غربی ایران با همه کشورها فرق می‌کند. چرا؟ در این ویدئو ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/677519" target="_blank">📅 23:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677518">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
الجزیره به نقل از منابعی در وزارت امور خارجه ترکیه: هاکان فیدان در تماس با عراقچی بر تلاش برای پایان دادن به درگیری‌ها و تثبیت صلحی پایدار تأکید کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/677518" target="_blank">📅 23:55 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677517">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltrqJulzUWsgMzOAsI0iSCajdaR0u1eu6capvO5qEq0qJ3MVLUOMmqvXKlKXoMkFtG6aUYTxkSBwOgw97nvbw10rBmgNd-OhfJZU-eSbuxfwuh0hTFhK4Ix0mzggNIA0ClIDq_arOs6bhNrhUn8uPnMCM74Zo-me4LAxX_BocjpBIYBK_OHl3P-aGdfJrqQA6EN7Ujmu9eiBkn4fehkReXz0bXtH9XCj0l5d_YSPdw-BX1WpHyHRHBPqfbprSuCVJ4oir372Ri-YMHlyxSNRJg8joXgpPOYyFkgwg_w5Wn-bmqnsRJzsRFqQ5qnSmZyelI6i_GNWckOAEei0-i5kPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هاآرتص: شکایت کارمند سابق از همسر نتانیاهو به اتهام آزار و توهین
🔹
یکی از کارکنان ۶۱ ساله پیشین در اقامتگاه رسمی نتانیاهو با طرح شکایتی حقوقی علیه دفتر نخست‌وزیری، سارا نتانیاهو، همسر او را به آزار و اذیت‌های مکرر متهم کرده است.
🔹
این شاکی مدعی است که فشارهای روانی و رفتارهای ناپسند همسر نتانیاهو در محیط کار، سلامت او را به شدت تحت تأثیر قرار داده و با آسیب جدی مواجه کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/akhbarefori/677517" target="_blank">📅 23:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677516">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
باج‌گیری ۳ هزار میلیاردی ایران اینترنشنال از مدیران بلندپایه اقتصادی کشور
رئیس پلیس امنیت اقتصادی فراجا:
🔹
اعضای یک شبکه سازمان‌یافته موسوم به «باج نیوز» با جمع‌آوری اطلاعات شخصی و خانوادگی مدیران بلندپایه برخی صنایع بزرگ، به دنبال اخاذی و سوءاستفاده از این مستندات هستند.
🔹
بسیاری از این اطلاعات فاقد اعتبار لازم و ساختگی و دروغین هستند.
🔹
این شبکه تلاش می‌کرد ضمن تخریب هدفمند مدیران و فعالان اقتصادی و اخاذی از آنان، در روند سرمایه‌گذاری کشور اخلال ایجاد کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/akhbarefori/677516" target="_blank">📅 23:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677515">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=vAMCZBo1VsO1zlpsoU2BE-GsNZL7Ezlps8LNHSwqUjfywlSoO8jWwe4xh3WAss87Z5krzlWaZG5Q8Y87RoEe86w4V-hgzzZZs6yO9w19kRpOfALOAXvEH2RX_oxjMQGUjkxBLsf6DiWCQ2t-3CLQxc76dAyA-YUiBH9hZLGelYxW94RN4zSEaOuts4Uay2C10A_KnPcVTE9o1e6FM6g0LD0jWcU8irqMf-6l1PFozGxKjVpOHSqpa6Unx_QqYb00xx20NQQuU_EznlXGhjhCklIHNQMvSW6wiJpIrpMQzkjG92OKgnOeayXFp2GbhNAIT5ya5xZtf7i03n10_NXe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/f15c065ae0.mp4?token=vAMCZBo1VsO1zlpsoU2BE-GsNZL7Ezlps8LNHSwqUjfywlSoO8jWwe4xh3WAss87Z5krzlWaZG5Q8Y87RoEe86w4V-hgzzZZs6yO9w19kRpOfALOAXvEH2RX_oxjMQGUjkxBLsf6DiWCQ2t-3CLQxc76dAyA-YUiBH9hZLGelYxW94RN4zSEaOuts4Uay2C10A_KnPcVTE9o1e6FM6g0LD0jWcU8irqMf-6l1PFozGxKjVpOHSqpa6Unx_QqYb00xx20NQQuU_EznlXGhjhCklIHNQMvSW6wiJpIrpMQzkjG92OKgnOeayXFp2GbhNAIT5ya5xZtf7i03n10_NXe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سقوط مرگبار هواپیمای گردشگرها در پرو
🔹
به گزارش خبرگزاری فرانسه، در پی سقوط هواپیمای حامل گردشگران در جنوب پرو دست‌کم ۱۳ نفر جان خود را از دست داده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/akhbarefori/677515" target="_blank">📅 23:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677514">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
یک مقام آمریکایی به خبرگزاری آکسیوس گفت که ایران در روزهای اخیر بسیار تهاجمی عمل کرده است و برخی از مقامات آمریکایی از میزان آمادگی تهران برای تشدید جنگ شگفت‌زده شده‌اند
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/akhbarefori/677514" target="_blank">📅 23:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677513">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
شنیدن صدای هواپیماهای بدون سرنشین در آسمان سلیمانیه در شمال عراق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/akhbarefori/677513" target="_blank">📅 23:30 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-677512">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بدهی دولت به تامین اجتماعی ۱۲۰۰ همت شد
احمد فاطمی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
دولت حدود ۱۲۰۰ همت به سازمان تامین اجتماعی بدهکار است. در بودجه ۱۴۰۵، پرداخت ۲۷۵ همت از این بدهی در قالب اوراق پیش‌بینی شده که دولت تاکنون آن را پرداخت نکرده است.
🔹
بهانه‌ای برای عدم پرداخت بیمه بیکاری وجود ندارد و سازمان تامین اجتماعی باید از هر طریق ممکن و از طریق خط اعتباری دولت و بانک مرکزی، بیمه بیکاری را پرداخت کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/akhbarefori/677512" target="_blank">📅 23:28 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
