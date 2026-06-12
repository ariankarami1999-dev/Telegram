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
<img src="https://cdn4.telesco.pe/file/sF2V53ozbzXl-taL4NuNsMvbPCuqRq4e8CHmZc1gn630fchu5wAyP6kpHjmyTL03rQdEIw7gXzuohdG8fPsDjLP9ytys8hBzI5eodnmLXChIlwongGojXctFNGAHRNWiXMH2qLXlU2sGudtY6xOKRHAC9TF1-08WYwd_hJXwTVIzV3-TqM4rhs162bL3u5NKg46c52s2rj_H9d-fXQ6Qhn-MqoYz9PP80pzVyxVIQP91NnXhE3m9tTIGEk8oCSTtCWYRNbrd-toI_nzhGrzWvh5Oggorovcbr1CMuUAU6UBR_ibrHRE3TMDvAMuvbZlm48YAAsZ6eVxds-WrfMPJ0g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 247K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-23 00:32:11</div>
<hr>

<div class="tg-post" id="msg-23309">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4ZUdA9G9S95p6pmUTuCFYPZi9mJZmw0s0L-LS6rBYrhQYveC64Ez0fhw5c2LH_uZfVCeAlDkQH1bEMVfpZjzRe2co474uKlDM7CVj7hVXs7XtfAHIFFOxx4Q9JLlqymHOMm3nj-db1dsQD31XxwyEY5whxVDrn59m0nmw3csh0oC8mFbuDK4sg-wnAuE-rJORDQ8rBUUNGKVyBQ7wnuO5Xv9df-ra_J58kh_zzXwb1WwsQoYHXSzoV-7t1lYzvtX7y8Y3UW1PWqsuzIigAgktgLXWHvtYmg9dJzKjtT78vikXRUTDkVYB9BJ5upmcBctFv1Mizj8CZvcGmvZoi6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#فوری؛ نماینده اوسمارویرا در گفتگویی کوتاه با رسانه پرشیانا اعلام‌کردکه اوسمار علاقمند به ادامه‌حضور درباشگاه پرسپولیس است و حتی لیست بازیکنان مدنظر خود رانیز به‌مدیریت داده و اگر اتفاق خاصی از طرف‌مالکان باشگاه رخ ندهد او فصل اینده روی نیمکت سرخپوشان پایتخت…</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/23309" target="_blank">📅 00:30 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23308">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5kPEWe5Cs4SjDdxENl4TEpYoHxFv15_VPK8DSIxTDMqucvuKUitznbWwfzm88F9B7aeGmOaWWTihyBt8dOLrOx_l1nRga_IMIjt2pZimesOvnQ-17EiiScVrkzZPwt4EwDdoT6JxXewaOYn2iYF1BFwPoUMWiYYGZA-egjQsj65FLel6wEUwF5TQHM1xF4YOs5uC9t1eDQT3NhQ6O1Vdf8OfvdvTaT4lLxs-QqSqY-fDTGNMVSNQx5ssP4Biq8DsraPg2orPcRXwNLpucMz1cFV6Cj0IDXVos_jBzscOzxR8no8KqUNctqxNu6h3JbHjLdnn-r9QgGxT2OGqqVRZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/persiana_Soccer/23308" target="_blank">📅 00:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23307">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTBNkGYUgi3nqCMLTlnhHz8hfC4bo588kcemZe2PLHYe4guWEPh1k_rZny1tsasufFd93GbS7y6ZWjXfOWYM_9QlNl1A0D4x3aIj4LpDMtUpZh-ZQT9u8hIKx9BvhonAzb0lW8CjPdgVPnCNlOWxb_IXa5Ei344xtwtZ_6TRlvfkCfv1c-TVxIgfxHFVPbKtPYNydOtSwVhtnCSOJgJrE57pRTK3d1vtw9Ce4gnA8vqmwMMxAxScC6yB89gv6C4PFeeu_fhBMOgNCOlrfOLkb-SHyecKuILa5uAnRRQsNb-Du_A3DE1BJcIlrgAfbar8XBgTs1Am9J8uuNBU5Fbh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
#تکمیلی؛ رومانو: نیکو پاز به مدیریت باشگاه رئال‌مادرید خواسته که اجازه‌بدهند یک فصل دیگر در کومو بازی کنه و تابستان 2027 با قراردادی پنج ساله به باشگاه رئال مادرید برگرده. نیکو پاز 21 سالشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/23307" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23306">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoqkCNRlTmke0NEEwLaUUxDxxTgQjBoAndRMOHLbtw9gSyPHJ85Kr1OQtS7Hd3N1NEaFKW8_-bUmFarT97yC5OofapapTHrqBsrpQgjn14dOMfGH1d2MMiNz6AJGos6tl3dWEfsHAQ3BzAKh0D--cc7mjxLOkByy8NT_zPIxiZy0x2Hu7kb-0z3BuGhYhIhyfRfprHNa68z4SaeDiHaCpVBq5kqV_L6c8o1ZQt1GltdVREHp8N_OSYU1RTwOGUJKX_JYjTuRo_5Dqk21HLscEQYy16prFnSowNWizFDKh3DpVy3O6rPrvPw5ouJB20qC6tf4x2Jxt6aFgzId17IW0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇵🇱
#نقل‌انتقالات|باشگاه‌فنرباغچه مذاکرات‌خود را با رابرت لواندوفسکی ستاره سابق‌دورتموند، بایرن مونیخ و بارسا آغاز کرده تا او رو به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/23306" target="_blank">📅 23:44 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23305">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8afd5643.mp4?token=MutqQItISm1EC9o_G5q7uNBJivh7FySd5q7nK8bfTiY-rAGZgGZqTCEJwQmIc2lgA-naqbYWUL_whFAN0hyH9wiYRVpQ8qOLkIII2CyAV8-7WJGAH-VtciZocjzlpPsvsYYJ9fAQKnqszK_7t0rm3rc_koQvn8XbOljOcpvqGCpHs8IZQ_hh8WNZsDRjilzH58qWiKvEuVhpMPPWt7aMuAUVuS87Nz1hMJVrDL5p75lJ7gP6G0Q0C7NkvRtgVHpLpp4u2p4X2e2JGefobdgezGUHg3nJ71bVC6hHYPCzr4CO4A34aUPkbToQNDggT36Eey1UdSL8U1kE3pP95xEFPSvjjA4Na5OxYTjx3cz_6XO6ywn1k9G3WTeDVQ8Y7vEKamTeGCBsBtp758rbeyWf_29DRkdiPgPU6d6xutYVf5Pn0WsFsyJgG47cpi1YH0rdnuBTnMiq3tIPl3goT4oGgWvHXf5RZ2bazbVNujpGGzQGdRpp2bjn0hcLhyZF9TUsQjMhZpFL7iou0x7_aAnRhlFNURZYMjjy79LdK8SYAQeMZAJPaKpkdc3S4Gcf2ACCXApuAZJRbFStuRaOQnjopz_Rgqm8Ng1pnl0UwV0-7fIWO30mDLj2vhJeLSGqBTrKvDFPE39G1CmbjVJggjmqIFcI69-1ZONKQbBGdcbtzX8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/23305" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23304">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه پرشیانا؛ مدیران دو باشگاه مس رفسنجان و نساجی مازندران در روز های گذشته مذاکراتی‌باسهراب بختیاری زاده سرمربی فعلی آبی‌ها داشته‌اند و درصورتی که بختیاری‌زاده با تیم استقلال قطع همکاری کند با یکی‌از این دو تیم قرار داد رسمی خود را امضا خواهد…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/23304" target="_blank">📅 22:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23303">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zrl-uNMaiSvWeI3Kw1yYR3SMVcTg_fIyOYBhh8aEf0zNiDf7nUgaWflNQ-WFmYfj9Fmw_gn_JI7TOWbrQr8W0qsK5YFfSQ0Byx4sMV4pE8PvYKH9RQfi1mBVW_x97V_o5YjB-hV9kibYFgjisWdB8MgSn75gr-aEKvA5d9Q4s_Cics3XNzGPgx1GplTFce76Yxh3_nC886Tcq5S4byrhf6svGIj40LcqEP8R8Am5vrCHdo2bxcH3vexFzY_xKMNaJqXoAZtyZ0Z0Wr1aXGTBhXi-ytcqrIR_EZ3e68uFAQde5U0QkKAYPekN0jCXJm69yRuhszQAZNfkqZNz21vsfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/23303" target="_blank">📅 22:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23302">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVgxPAv5tVJkOhlZE468VOR4SF-SPMgT7vt_dR4OBouYqgKGgvsdLBX_Uotmp1EY9lvyQKnKQeggGdboDIzOUe4br8rZX6wuUPN3jZ-URMSSVjQwaOn8vBEDILLm3t8mm2qbc2Ce964atVYIKjE4Ca36zZ5yblot8IJdjRr3Vkw68jK5l-vM1JB3wxnYTku8E-nTKNu11Al_hpiYLiRQdbSf7kmv83pXPYuFNQwDg4qkMaQ43p4Td-uvteMOzFbCiPqE5n7aCzkc1fyVM5aMiyu4WBcumsQ9XfaBsio7rVaNto38nxTY9PatrX3ORfjkHlVQG-mBoB-Fj8tbiYbVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌‌اول‌ مسعود پزشکیان شب گذشته با سردار آزمون تماس گرفته و از اوخواسته‌ضمن عذرخواهی بابت استوری که دردوران‌جنگ‌از سران‌دولت امارات گذاشته بود به‌جمع‌شاگردان امیر قلعه‌نویی بازگردد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/23302" target="_blank">📅 22:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23301">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNqgMmXRqFL7pSIkWVgVsjtJR5pOCqjvEULw0R5NHO3A3de5n3frovK5_LWii17I4AFuU8sipxvqKvpM2hQoHA6ko-QjElr_Dm4VecUvtW4gzDV-ZPbsn6grw6ZmkQvduIZwSDw00J02alvByEswfzavBQ5gXXgGjLBnZH28sTZCbScHipxcT6EedrEe5SBfFc6fYW8E8UwKhUm_o0-T_7h6RWVkYF0dkov-21ukKMZ62BDliBoh_at-ghTS6ZpNTzGSr34DiAA-djPT8WFznUpjuPyaA22M9pcgZek_fxEJGMonpGSZHzhGR37F_QTzeaNQOBQ0XNKQzFmc-o_9IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#نقل‌وانتقالات
|نشریه‌موندو:
دکو مدیر ورزشی بارسا بزودی با ایجنت بارکولا ستاره فرانسوی PSG جلساتی برگزار میکنه و پیشنهاد 50 میلیون یورویی به PSG برای‌جذبش ارائه کنه که ممکنه قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23301" target="_blank">📅 22:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23300">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PmDY6d-v3lkO1D8uQAywztmSAMtRZpmQvmy8Mbvf21b_TmnJwmE3uqxKXeWPE0FP87k4SZfb7V8cOaGKxR620guTuckpFsrr-yp-QQiffYsvNrb9bOErk2z4lElAVN_XIlSTi387uqubGAFzCwKO4_kGcPgYT8sBSVWwvdv6mCVZgaQ0_CaoPbxLQq9S9eGAeMb_dZnLTgh4kvuXYQLaZThPpZ9aUtElofl31i5IypDWzeAwo-fdfrp4HVF9JLoim9kXKtLhAy9e3r6ABRxcWU9iOKgUsnGWO2Zgk4f8_54kTFm8rRyfWY6JjbzGAeLr6ExkAwmnlxtGTfL2O2qYwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا؛ مدیربرنامه کسری طاهری هم‌بامدیریت‌باشگاه پرسپولیس هم با باشگاه استقلال مذاکراتی داشته. رقم پیشنهادی باشگاه استقلال برای دستمزدخودِبازیکن‌بیشتر از رقم‌پیشنهادی پرسپولیس است و الان‌همه چی به‌خودِ بازیکن مربوط میشود که کدوم یکی از این دو باشگاه…</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/23300" target="_blank">📅 22:05 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23299">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2c6f597.mp4?token=cxkWqnn43I6bZTwH4jmLhKyZfPIcG11IzYfpDeQz4Lu7YGXmvjVXCEIZbq0uUqVhj2FDstkODCUXFf-i_tPgIf3ghxx55C_t8ecsrYKyzXfIy2pC-hx1_ny-ZHdTo0-zTu5s4_pDDKHN15276QNzpYAgVZEkBg-FXvkAXteM8vfvjE8YcATG4uzrWN9h38s9nQT1zQ9fUfUOKpzIptzz6SXsPeL01iRaD_sA0-C6Y6C0hUiXto41G7nnr_CGncUExt4V7I8xlPhJA0HNmUG7PFCgeQafwMMGK4EJiOit0PPbT6GKqMOeWWVpaFu8KjglT2B4Lkvp9bAWwgezxwU7_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیدار کریستیانو رونالدو بایک اینفلوئنسر که بشدت طرفدارشه؛ دختره زده زیر گریه رونالدو بهش میگه اشکات رو پاک کن عزیزم. تو خیلی خوشگلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/23299" target="_blank">📅 21:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23298">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjA1qL0Ntk_uVzwY5W5vnE4tgNGfncDUxzG4HJNuab_cZxx_rouj0oYJRDC4DYjT5pqkeFWgkv9_H0d7azNtJ_9PJLtz7LGexHJ9Gypai0U8JcOzjVJyv8BoarrEWPrCZiZvX6cCL4ALTKzPiN1wsPzg-e664wcxSRDcKWvbYyJvbE0JJM0obX4Jc9aWKmX4UbqZrOEQShq4nUSeFHwifpA9owbxUUNYwDNmcnBPElTBAGffpORPUKIwVuaiDYjriDzhvYl3VnTsffSTqvf8_FYSsGN65eKhlpOOWZH4qs-rO5Ck2ttIMOTVW3aHzj99as98LlFdbzrPbxQHGrhg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛‌طبق‌پیگیری‌های‌پرشیانا از مسئولان باشگاه گل گهر؛ روز شنبه هفته گذشته 9 خرداد ماه؛ پیمان حدادی جلسه ای 3 ساعته با مهدی تاتار برگزار کرده و به اوقول‌داده‌که درصورتیکه باشگاه با اوسمار ویرا ادامه ندهد اصلی‌ترین گزینه هدایت سرخپوشان شخص او خواهد بود.…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23298" target="_blank">📅 21:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23296">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz2aNl6B7zkEuGBQ2DcLVQy09Nt7AC-oDhgXoA-ASvnhAR2GBGt6xULDjNGmoPigv3qu0EP2afxSOaU4sdnIgJz-7_wqYGmaqdVbdVwKpFpAEnEx938SalljbP0RyJlTJdVdi-Nrs6gCfdV3U9MxVRX25hQY4H947_1U0TlAq5rQ5mTsSJixgsiNO_txstMC1VmePx0VqKadt8vvFGOPoh8g4rSELDx1LrWHRgAQjnPKu12qGRbYBxeR8CdyMGXvr7LwOWBKm-eAdAgUfTXfjx2cL_QLNtzmbW3QMIs9RZUG_qff_Ffk0mUZScA5kGgMeUxK2g2xY7XVw4OpPsFNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hf186UZeTroH159ws62VF4IzpN4yiqz1f7jgGdVgxBFC7QmsRUMw36yqfPko2keXaep3PleGExBTFYuGMvx-MAI_ESG2rVXDU6bG93EePfIyR_DszXqtmyy41garAKTJxUHx7gz7Ll1re4ZwVzshdb2f1-bcCst_STN5p27ExqNaZjgbzkA5dVnWLTnA-qJd4JaThjJgdpB7f7lvveBQ2r8iP5boaaR6wmNkk0fxJg_5juQW7XYIXxm--Bbmefh82N3413T4TCXSX-Q6YvUtMKAqPsgjDT5g8NLLRBvpHO1KA72sFUHQicURVdjd2Tm-87ATgKD7yWoTagFHWaTOwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/23296" target="_blank">📅 21:27 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23295">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">‼️
آکسیوس: دونالد ترامپ به نتانیاهو اطلاع داده که زمان پایان دادن به جنگ با ایران، فرا رسیده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/23295" target="_blank">📅 21:24 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23294">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQvr_JHzJK9U_BqI-gnq7Ryxiwc0n-hJKKCp1znbROu_cNhOqITx7LpIB5RsmWVmNOljURBUlx7eqA-QXFKFMto2sEjZx8VRn4ReO7091gsWxT-mQ0N6YXKYG06VAyuAM5mQsFt_K5iPBJO7wxxRL5uzas7vw7kaRTUWgyRKfWomkJWhtd0F4qohSEI4FpbNluZXMc5Civokl2gmd5BtvKRGLEf5Xeqfjr20Tk5B8TUxjizoCme8YC178Pv9WJ2RWTjrfbWOYYn_NYEtL6jA0S_jofOjG1nZfxqUTUc1WuX-maO8gJJpLzBXx74gbAMD5J04Vi2L_kP5KqLLuXpUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/23294" target="_blank">📅 21:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23293">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b49d10c6a.mp4?token=FcgUxz2RHFBB_UXxraz14y9SMvOfQzboM1uLVJXOkH1mQ6eDhLwW7bD8u8UkjNNYkxbFSpDJ3eqQC0Zvz7B62RL100LIs-4_xKt06SCmk5a5cyaVLZ8Vaoiq7XWu4ZVKuYJauX4xeEzdT9NqpEyyjdArqKj-SfAua421VDfhjWA1zOS99sKG5ZtVimMN-FVnhSCEliG5LwMkB0j5FNUOBuUmYsUhs1-VAqaYBsFzHwgrgf2HVla_nINdoUBih25RZOuxwjQ_9n1266shcT5EZTfJZL1XPq1GKJQs7YhXNL6mPFQoCXkOoA4T_vu6PF0RLL6k0Ijaaa9PX4oHZ0QN_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اسپانیایی‌صحبت‌کردن‌جوادنکونام کاپیتان سابق تیم ملی با پائولو دیبالا ستاره تیم ملی آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/23293" target="_blank">📅 21:07 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23292">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EayyDHbwUp2Ti0oyMgZahpe6zbfI5peFzWXGweiNAkbSNTDltVoYFh_21BGqPAwVdkzw6NzXqDDcwowATSFIjJ9R7h3iuk5AiPA7fCMA6upU5NrtO32_WSxyKr-t_UbdMZ5OdauyV40VIbBZ_yvehyBuzIiJK6dLl1rh-U9na2uLp3RgvErR-FkE53RasDiGeoK7FoMdX4yCZKJRf7Vu4Q6eI3tPSPCG17alYEp7-6qWFLCVxdY_yClHzWjBMbVDmO5Hn1lyDmgpKRVZamqNdACcSRkqiOqTUdgdhrL6P13Ksp-4rltdciEai_HxSB918HwhPW2EVY5vbZ3bP_j_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گویا برنان جانسون هافبک کریستال‌پالاس؛ با لیلی فیلیپسِ پورن‌استار که‌رکوردسکس با 101 مرد در 24 ساعت رو تو گینس ثبت کرده بود، وارد رابطه شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/23292" target="_blank">📅 20:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23291">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5d5FmErc0ypnl0SNWSBppAKhEETLbTwT_fbH8q5RNrG0QlXmruQt5I0Zfivtoxg_TicbuEtivJkCetSxqIaQHQ27QsLi9voO4vZuTwPtp2by4VDHx87gxmCxuafVygwItQaBoFPS4DPnB0MGzrJZb5Jp3J4K0k_fOFXeWICRs8Lgs-t6VEW54sy1tah9C9Fnx4_3e4nKtez9R1XmLlhzUsuCSjsMsH60p4yRKV6x3VWjj_J1N4I9LP2ekx8JVIBEyZ-XHbrKmJKszlML4Q9N-6apsJwGhWX87RgzioQrLy6ihcFTvlQM342HAm-TFf-bSDMsS4yBDofbqiqaO4A1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌‌ بهونه اتهامات جدید توماس پارتی یادی‌ کنیم از‌ زمانی‌که اگردوربین‌‌لپتاپ‌نیمار روشن‌نبود، اون الان بخاطر پاپوش مدل‌برزیلی پشت‌میله‌های زندان بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23291" target="_blank">📅 20:47 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23290">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLJ07fZMpjUqIa4BsUpcd8Sy7O-2vhV30kgm9Bn2x4QGBRIGNU8BcFKoGabC0Dxyp2a6y82YbUIXJ6aF7O1er5axMTZgjtsxZfpz69ZIkl5v63VJU2GS77VV_-FHnbI9dSu5L03NXrvzpaOF_n1oOeEaOKdmm1u43LEaXBYFzFam6V3f2m_NBOoME-gTcT5iUTAHEvS0I58MxpUcW9YkqMpp7ypgHJpNB0GEaCY4ZgEjG8WHpAoe2qWs7IqRC1fjlchDVIgRSj0ntmLDDMncQYLhS-1Gf86kZNLzpLvgZrXzaodnYhp7q59MRTtE9CSlqhmp1Sog_4ifd33pZJ5lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/23290" target="_blank">📅 20:37 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23289">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJky9QgM8mtY1dn-aFQCQJ9cgChY0QY4CynLacVsCD_6DlFUI1Bkumr2jV86JbvMjgrvd9gbM8cEi8_t6AuPsJ-xmeqpS3klIxQXkDrboX6yQ1jSsJJvoROfrH9aq9VlY3g7cT-QJA9lmypgmt8bJId2-wF54ThkN-l8pvzsW6MoOfKNr6qHR0hozfCPJWjCQ8Dfwf37pVqO2A-KQ3tGqwmiseh8SjwN43axBPj1YH9LEzW9OSyYC0MO20ADd6gnaNL6gJq82HmWou_jnymgYksam22YR8lKNh1EEeC-byFdBixo3ZSVhBjJhJ_96gQIXp9RkVUSKscBCWYHp4fohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛شهریارمغانلو مهاجم‌ملی‌پوش اتحاد کلبا با اتمام قراردادش از این‌باشگاه جدا شد و بازیکن آزاد شد. شهریار فصل آینده به لیگ برتر برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23289" target="_blank">📅 20:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23288">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r06agJUP4QT64g63xhmysjV-5xe0VMYEZ6gIBT4ltVcMy-kQK-NlnlvPwkwk3ocQY9436bo2zTP4d4I9YGbJbZqGibWze5Hpwgn_qlVmk9eY820mattF1IGSx8pReZiM3DCxdSoVQ-_esCq5VKmEMUVbsZ_189bdk4PUdGSZxOfXWb33H7d50xd2LA0xo03-pRiTqTuJtooajnRy1f3crxbUGEcjghufmmLBAjRsidBxPooIv584WCp0k9k2cUHYjjSlESoMIP5Vrwnzsoae31WnYvPQdvT2H760cd0H5Yw3iQenMz7B024Zmq8_cLZGRBLfotHxFF4xj5wR4HlUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مدیرعامل‌تیم‌آلومینیوم‌اراک:طبق‌ صحبت‌هایی که انجام شده باشگاه استقلال ظرف یک هفته اینده مبلغ توافق‌شده رو به حساب‌ باشگاه ما واریز خواهد کرد و ما رضایت‌ نامه قطعی بهرام گودرزی و محمد خلیفه رو برای این باشگاه صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/23288" target="_blank">📅 20:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23287">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9VfSIJ6UlmXksjujY-991nZ_LBfbGTTLMTHSgRnK9Cu-a4iUyMXgaOhqien5Da9z98GeLxE7KQ5gzkbPF4se2HCLmsDXHeHZgqZzkTzIEtu3jTtNUsJi2Zts6BXFRPfE6do0pVgvFB66NxTpDsL5CS7oe1ihO8DyYpNf8sDYiMtfq8GRYcKOhy9YKDeVh6t4Z9cXKOqQawH7D4eXrj_M86eStKIi69vLlDnmg1dNinQgt2wMtlmO5sE4rZfPF-EXYNmzbUrbRYf3FhlTF1DHSczGX4nCSMluOzeOIjLPpg2zTXCR81Ul81xkaBqz-sXfIUUhMxaJue5HwrJFzA-xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛دوباشگاه استقلال و پرسپولیس با ارسال نامه‌ای رسمی به باشگاه روبین‌کازان خواستار جذب کسری طاهری مهاجم 20 ساله این باشگاه شد. حالا دیگه بستگی بخود طاهری داره که کدوم یک از این دو باشگاه رو برای فصل اینده انتخاب کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/23287" target="_blank">📅 19:57 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23286">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbDWPtvk1nMrpfRlwrkJVn2LBP6BPLyckD5P2ubZNiVhjBYCKF_kwuAUUj8uMwFTtWznybOAMT8gcs-uaFmnoTEJsYSSR_26z5kn0mrMC-Iod1hxt7k5s2JUV2e_gCTwWFWQx52uFXdQKkBb2aM28YEz5ihFRgAJ6aO98A6b_VN9IEW4onb7MW9JH9RNWOaeHJUPysYyuSuxXnFXCPN-HDN4uyOj-MM572_tuGz3hnlnF9z-ERrjEEs80z-kgE_YzZyu1MPpaJs6BUw_1iyEy8-A5CU4mK3ufGA_qEwWjPlxxbsHOmXQmW1u1Lr6EgFbm_XtsWUg1r2NjUwuiFWxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی؛ طبق اخبار دریافتی پرشیانا؛ مدیریت‌باشگاه استقلال از علیرضا کوشکی وینگر 26 ساله آبی‌هاخواسته‌که هفته‌آتی به همراه محمدحسین اسلامی برای تمدیدقراردادش‌به‌ساختمان‌باشگاه برود. همانطور هم که در روزهای اخیر گفتیم تموم توافقات لازم با مدیر برنامه این…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/23286" target="_blank">📅 19:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23285">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23285" target="_blank">📅 19:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23284">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46ef7ef7d1.mp4?token=onYCRk3x7d9-il1LrmXLWAFPSXE0yu_6FX46iQktasG_j3T_o6G9mWt8_Hhqmmg4K48NhfV8Nf3rfiVzxuHSflezkWWNgJFDIIXT9XiZmBmAUeNZRqthvojvk6DJCdAkXjpIF2DseWyOxSaaeKZFZpRd2LLMJugKg8gCcUNQ2_Ic7nI1iqabfAN4RjvUnrzKyE4rtIoQEIXs3PTiObjdH26uXWA-DgugmIleV-3sKVOPvTJdZJ7s0vLlsSxfzvP0f0NB3p7EoEWU1BiyJgKW-XTBY2LAnyJVjlMmDJ727M-W2pnYNa06SWrdJ-wNMCken8htB3cVwSouTHJr6_5p6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
صحبت‌های‌جالب کریستیانو رونالدو اسطوره پرتعالی تاریخ فوتبال درخصوص جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23284" target="_blank">📅 19:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23283">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/joHgx8ZAXmUIQgkjd2EWnM_rD9AzU3dXJJk7-C-K7JuXOXh6VOtPa1_8mKYTKzTNdoRLdA0oLClKRMCk39Lx7h1e_CwNc5X3CnW_rGu-rRrkgFU8qtIwIzLOKMzdOf0tXvPBg9CT-gsLkvzi-96_dCO_RO9urO_cJcmaWsQAVZjwVIwYhwxMgI_idYVL-EzGENTfV053tuPLBg1JQhmC1vTY5LaJySrQjHkGyUV2mNPs3CeHGw4HVgPHF0hI8m0hEgwu2kTrMQDPCKUhm7tv-4LCAI0VwNqH76_zWz7AVbk3IFzf9Oajl_N6h_ekFQzj6-Asiiln5NZFbFsT6Mkt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش ساعت جدیدی که امیر قلعه نویی خریده و در تمام شات‌هاش نشونش داد 136 میلیون تومنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/23283" target="_blank">📅 19:04 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23282">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64a2fd248d.mp4?token=fI3e1AG8tYM-AU27MMqO20c7fCvOuxZmv_q6adpB7j9mTEe6FWF7zkSP_05jHOrWSyARqUeTbkrJllokLAHF-nmdYJFNaJM3RYSjELTZm2v5SyOCJDo2LfgPTl86jUV0WgNK9JZ0KZvqjLnTKLPBHDKcWEl1YIKtrbQorgDN5db6cRusJNR2D442eW2mA0ob1MuLU-ocKke9PRC4V8H4FJnxgHx8I4T0ja_7RP-OlwuU88aWZzpFJqHZAnqGQKttFMg5Xwt6RPP0vI_un83SMfxu-UIW20HE8e6S3qTi-ZfVSoWCttQvdTwoGXqVXv3HkgUL-wweEUm19nkayZLQKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ
: آتش‌بسی نقض نشده داریم به یه توافق فوق‌العاده دست‌پیدامیکنیم؛همون لحظه خاورمیانه. یکی‌از دلایل‌مهمی که اخبار جنگ رو پوشش نمیدیم همون صحبت‌های لحظه‌ایه. مغزمون به اندازه کافی سرویس شده دیگه لازم نیس صحبت های لحظه‌ ای ترامپ و جنگ رو پوشش‌بدیم. همینکه بتونیم اخبار مفید فوتبالی رو در اختیارتون بزاریم برای ما کافیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23282" target="_blank">📅 18:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23281">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udslPFZC419yJYfpllK23VKvcK83O9n7vX0AM7AVoZri1MFSY-3qUtgBaObV6Sj28xS416w0dybNQFmfbI8jHiTZY0wQNZy-SGTHlUFqDe9uHLyMjzKxpQS35paUJsMB-Hmv4Gp-yI5G2US_yENM1k78gUcEeATW3TDRoTt8k-6Oa5NBsWFA-RVTOKSAstddflMpC1haqqe-KGz3vtcgJnS6JFP-mOC8QxmgEPXg3fHutBwXbKhpz9QHBXiagY2vmNt1gOCjMZt7yqqNKxLPAtgytv6wRzZ92slepwCCFRrgZTEFywZZcXHjexZkLxowStHr7wUoqmBPQt08xGvfSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
اینجابودکه‌عادل مثل خیلیای دیگه شدیدا کراش زده بود رو دیبالا دیگه شروع کرد به تعریف و تمجید ازش؛ خنده های کاوه رضایی هم داشته باشید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23281" target="_blank">📅 18:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23279">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d475f3d8.mp4?token=ezRc0qPVMGr_MYU119zSXT1x3J3_9m57HxzSv8mWkGp4mB1jVkKQAiylo52MP7VQtO-cpQntiScWpaB_MtRhKlruIrhPQ-36RSuGxwEtqMgdn8K_7wuLUGwV6PVNEiZdcYYjnAvZV8ZBdbIJnDN_pVzr9Xzdp_g_KlZ1sb_RWMHt9UhukPvxplEn8_fdGXEdI8tTfxlqMYxM_ehrQoQWkBIIFE_KCcw8vEOFlAK_jYJOTE00UAAu2q57--9LEfa2ql18LrmDTJS5g0Zvoow3aM2p3APa2ZABAqc44xAysvb6nVFOTY-TxFbIl19kMeCcr-Ldwe5EERZ3uT7urFoPOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/23279" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23278">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d34dfb18b5.mp4?token=kZqh_qLoSdPmMCUQoF-2DE7ycvYca0urAUmQzYwL-y0D3aNeOxgJolgBUK0bm6vBWFnrcx6h1eJta778L9oC16cWliQx1fT-fvTM4YkUwTMPvKF7y2rcqx9bGpoItz0W63kpvfTnDj9vLi4NzKLIFN-tvZiBaexw77gxWkosAIgu-dRErgRpe7NDgYkNFbqS27wQuzveGRLkxsxNppxm7bgopRpxG9HvrmQNQoEe-CnPXR9gaWHvRqmG7E50C7_RzAFhq-9Db2ZKZLV5ciDLvQbtKjkEbQ7K3A_cLivdU8WYzUIq_IAC-mqt3jdYXGgK50x3L_mACfXtrrfWDgAIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اثر پروانه‌ای چیست؟
یک تغییر کوچک، جزیی و بظاهر بی‌اهمیت درشروع یک‌جریان، میتونه در طول زمان زنجیره‌ای از اتفاقات را رقم بزند که در نهایت به یک نتیجه‌ی غول‌ آسا، کاملاً متفاوت و غیر قابل‌ پیش‌ بینی ختم شود؛ درست مثل این ویدیو. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/23278" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23277">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2HkpyfrML1aBF5Ras5LYOb_2AW59_xHIjUo8RMvEVQ_Y9S0wq7CVBRll1yHPxv8fvroXahT1jzKV-ak9BDKxIL8gUbjhDOdhvjIdamA2Xbg1lo31LmLNgDRtvO99RAUeTeLP1Fnro7ytm0VQSbMSsNvg2iZ2e2oKaLqwxEDZ_ZpGRlxl96MplYwN3Or8Jt9favRjI9KLuosqLEar42YASmefZA8pK6gwh-2mOoQ4zYS5Nap12hNwbHvQ5jUXXlGfJSnR4WjWv233TqFlhktTmYqqk9iNjMN-FpPhZDlzCUo-ES9oBB_K1kf9Sfqpf7gk_z7d0g3CpW3ztNVPnlcVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا eg22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/23277" target="_blank">📅 18:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23276">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRKxy5AxeMA3B57HKgNnmse6DpYUQnha5QUlpnUllmIrawKgF83_5l4W40MPKeOKB4VzDQJPeECyke8Pdzvs0-omn2_EexO4HlOvxUUaOl8suaxIm1bQi2ycCRmCneUT97pUo8mH4zr274Hvxnvw1inE0RTZNA6Lc2FwH2OkFaCwyZXPMmnETsimmX7Iz1gdds_s1pLtORODtCl6cSM0dr6Lm9PoSfgvY3RyBT01ATr8MIwUX-i0Xt-4E1FjQl-Km6-7HIiaZG7kqc18U0gIjYTe9wLdMhKLeQqiow3jDgXKhKf6eRwLcT349E4DnvRe5EewPJRS08D_tevnyGBEwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ طبق اطلاعات موثق به دست اومده پرشیانا؛ باشگاه استقلال افر سه‌ساله سالانه به ارزش 1.2 میلیون‌دلار به دراگان اسکوچیچ سرمربی کروات سابق‌تراکتور داده است. همانطور که در روزهای اخیر خبر دادیم تنها شرط اسکوچیچ امنیت منطقه است. گفته جنگ کامل تموم بشه دوباره…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/23276" target="_blank">📅 17:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23275">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9833527b4e.mp4?token=Nch8nuybe15UbPc1LG3ff6y5J68vRo8vUyB1Hw-G-xXKb3wyG8tQaNkOdR2ZOlIF1YHVfWPCRHXTGgtcey8xhmvTPXIBnS0eoueSNuXuRLuIiLOHjzABmf3goJheIxpyqsIuWoEWGuTGH3i0D1wDFi4JEULngQYgdc5NjbZ5iUbAyyVcECbhkoS7E6exVwgKsHFKlUxJuvCYANTGBcUnYWBK_Cp4cakPxLzB9AiHDLQ1JkUnZjScKHYu8DyeKh2pjzCPxcwGOQ8FoHQBgvh0lVVVfG-5M-oM5slXXHMc6C9wM9mxQ7qyZFV4ngN4Ce-uCZguqLINauBdFBEcOhYGew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
شاگردان قلعه‌نویی شب‌بازی با تیم‌ملی نیوزیلند؛ ژنرال ایران از تاکتیک‌های خاصی استفاده میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23275" target="_blank">📅 17:32 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23274">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnWKFrUKkjNPnrniZfNyWGNX5-mijc9w7okSqzQnwHfLtgl77oRlMUbkXGm0_PIFGR29L74PfHRC_2PBdXztLuMEk9ODZw9zhECiLhyCR1jow5NoFA78WXzn0nEx-AVcO--vSEQzw7jPWJ6s0F1Gci1sZTrWZ9yvPH5zpGowJMjd7nhN7UdErPn1tu9r4U-Oo_Z9Fv0-IkIpSqsY9Egd5TaeVFYEoLddnwrAECgu_e1E9o08BxcB5IALhF-LFLlFBVpaxdKxsQOMU5cDi7u_3b62dLrnuLK9X2Jm3lxGSIeV2SXpBbGpPF29sj9ol2NanXlEPC4LIU8OyiwHpTyVGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
این‌مدل‌پرتغالی و فن کریس‌رونالدو روی قهرمانی پرتغال در جام جهانی یک میلیون دلار شرط بسته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/23274" target="_blank">📅 17:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23273">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0ea01c2e9.mp4?token=W3Bi4GUeGvZM297VojDmtqY6BSPGR9qcxM0QryvQC3HV00y8xbNLriWmnq6X_Lj34pPyKNrUiMhMIl7amlsVVm7xhW-QoKXNzssgvgl8m0mTIYQenhnE-s6bLm6VhFVLMS6wRaWLBGLdUJjjgEAzvUU3KnW4WvRqRGd55iXzfHzEppnIJBY7-06EbC2s7_eGGHnS3d1ZRyOi3e5bgPHEAhj2ZYsBP_dHFicsZXY_98l06HybyEhk_ZJJdUFA3GfAvLm-1H4KfxefcQhFeXt1MQDaEyjeiovf6l4DCxbdscYp4g9hKgM6sTCvObXcFVvNLK_-fDBdqNwo4mAJ6CZO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/23273" target="_blank">📅 17:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23272">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRCWQpX8swPcRA6b0Rk_aPao99_63RIpZUOQAZmeevY9i3cm_xX1sHApj8vBb_ReCgOeMYt6R4m_e9asYI4qJSItga2m4GQBBOZHoj5AGvzRVc-4VhyttRceTPUHZG2HvqDMpcBpV0y6WC7hd5ppaKw5g9m9Xv6DPhHagD3v3Hnsrn9o6lA__A_McnHUrXivtxn5kmnLLgtemKRWq5POFs6TVj5y0ouI2sJXGSqUhf6WtMXuCdnMFYU5zuC-fPDGT-kpoUoQWciHUOgXhzlf8Cr0GeW8JYBHjhJJeOzUDTXBkgAEgRLP6P2-PU-tUq6m_9IkQ4OGa00T6DaTG21tLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23272" target="_blank">📅 16:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1a4HIan_gDMgdX7WkaTGsNjaHSMG41x-rmRwvLZrGsWpqg8ETj1vVWsXMx4NWCcg4pIUNUk2xt7xVKYvjxY0m5iog1eO8oVmq6NbIn6GlNZgO5IgYaFoIL_r-GcG7d6GJ_LxO-pdH1gteV_QkcWeog0ZaASMwIKoDoZofdnaR32JqLVMJ4lRp3Y_TyHmNgLni19j4l4HU5aEPdodR9Qc0uEkiJlskN5uh8bhohm5M-GBMA1wDWRjcFQZujjd7UTvuYlm1RUh2tKeux-8LenCmL4IRlFWD1SWWj19uV2z3QPztjR7sUpSzZZYcyVOgMVuCr1fmg8IymG9rD87h0oxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ITofklj1lr_Bslvyho7rRNePrQoljBRwq2qUkGluIpg5vwfSeLcMAg_qfXxYVnzw4bZXiEWBDHmfIbQnUsYQf9W-W9oFXiy8b8TDL599hRBFiNFDabr1N3jEFvyZ9vAkPM6ah2x0ubDZCToeO1bspqUV5Lb8R2uj0YePq1CNlC75xfC_L9p_9AffIY8VBsqpYFOU2tztRH98cYvlAz1MeY_mh5fD9ZqQbiq0oEIUGPQhi3VdIF1fEYgAf6krZmkKJ8fuOjrsrXSFrqik2ucoOCml-BCI0AS8zYhwRwaPzTcVDyri4DJZg7hQg9CKQsy-zvt5TX_bxo9jCO47Yqzs5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
هواداران‌تیم‌ملی‌مکزیک دربازی‌افتتاحیه روز گذشته رقابت‌های جام‌ جهانی با افریقای جنوبی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23270" target="_blank">📅 16:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1b43a439.mp4?token=eXugSQKqTiGM2bP9o5FjzR7wfkLr30M_L0MV96mxCT7xL1wZuAfxB1CmjbqFsa8K-AQZpP5DxOc6FQ_4RWeGvz7iJeaer64cX8BsKPGk7qcag56BGFzJesYdRhmna1n8xR0P6WRFrqKBFCYpgxd0Yi53htwS_xNQwVmMpSLY2s8nyPC4NcarPTw4dL1GCcw6nMg4fZX4sg1LgkqGgHiMbkrIG--GCRDiBm8RVrU0bR7o4U7pMMI7HIHrqpU06fKsLyZbF0l8--DoS43G_B0bMRsGKQvx0ybZUQawX_FYrXUdKUM1kj3mZEftnyxG3Ra6dRua0_wQIfVIB_LWS0efHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم بهتره برادر بعد از این حرکتی که زد کلا از فوتبال خداحافظی کنه و پشت سرشم نگاه نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23269" target="_blank">📅 16:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uziv-EEEJt6JT2xHd63Z7DzhHkqZIx8GgQUdWfNwh7_xR0TfkyDpkKy-sU3SGHN48d59OTo24zqsJVeeVv77JPdhzY-laahp6hj8EwFA5DI9giGo7U06GrPk1rZOADxDQKkRvaIQ_ByrOVYzhm8H567wFbwjPaKZPvF5udiIzZXCRsoLDXWQ46sYJENzyGM0wo8nlFNVNhCfS82S74pl2jXW0sNB2WHF3Qamz71bVLGjrRKbzen8CtETwpgpMRD2RTDnqWNAhInQZd_ZZ4_dAU7gyRcoB4dc_rUHEo2MTS13JtyQMEWuW1u-Mw81ve_pzJFZLDXc1VSKJ1VuV8FAzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همتون‌فهمیدین ژنرال ساعت جدید خریده یا بگم بیشتر عکس بگیره ازش؛ 7 تا شات ازش گرفتن تو هر 7 شات ساعتش رو انداخته بیرون که مشخص بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23268" target="_blank">📅 15:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEghjjt1ULikenVQWTqcaoXd8vdelEB7cFtIRH9MG_o-RIvPBnQohhjg7Me3ajZiwYXXyzgDCxoo6hnxTmx2fyTtNlN7jRmW3CmpfnRxfl1yWJdQYNYaObQBAFk-yn4Q0c77Us_rER0iKjHp5OJ1JeOlReJEPHJo0UjyVnHZb6Ir4vVnCnS_i4PW5Cw6IORlMIBEv1AZXP7y_O5IQhzG-oS4CY9ckCxO1Jr_TqARNYqyGGvfm3FiAdacChnX66mWQghilpy80K4KLrMiNM5Ny0dkzafgw_TLOKoZrzdY_IWWkeVnHhoQA2S5AfsCmaBR8SfxxszhpC1rcWgmg9i5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛براساس‌رسانه‌های‌نزدیک‌به‌دولت ترتیب رفع فیلترشدن پلتفرم‌های‌ فضای‌مجازی به اینصورت: واتساپ، یوتیوب، توییتر، تلگرام و اینستاگرام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23267" target="_blank">📅 15:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b4ac464.mp4?token=gPU35x6bacDSh_uvKAVLUEatyIrEo02VONdOp96L0BP0YEELOxgTh9x_UddnQdSbmGLLbtlFKXVZ88leO5Izyanb1DcLkwinM7HBmr3__dhimN3vEpWcm5m1QXbZsarb5vAaJeOUPSoABO6LKm1pzGNg30zrak7-SBUoE04cPClCYAO3GgpLlPq7lW0L5Ml_NkluiPWlvlnHYPl3lK2bKIhvqx6ZYlQUgyG38SAE2OLX06k_RukKrBNMLGqV3ZtYThuL8PZmPb07MQ997wV5bgUagSxjc3wvR4A5sUlrvliSwYb0bxe__805o5B4lUfMYaZAheiYGtY_PrKzPN5xuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درسال‌های‌اخیر؛
گولر، اندریک، دانز دامفریس و حالا هم برناردو سیلوا تا آستانه عقد قرارداد با بارسا پیش رفتند اما در نهایت سر از باشگاه رئال مادرید دراوردند و راهی سانتیاگو برنابئو شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/23266" target="_blank">📅 15:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAsokkGht3PbJ1KEAO3xLVm5xVZuc3n7Y6f7AJAUwWWUSsrhp_cF8SI9FHTCVgKPTC5A_CxqPCN9-9MboI2po0pu9hwU3lRJlik-ujL15UF0F5jyufeADeIYGXK0IB_VCPQdoYttv-sE8h8dB5pZ7BWW8ufYkQfUkKoZYztXZwdt0ISH38NiYluucxQKFzwAA1s58Z3HGv6dkrQLp4tEIMn5gpZWq4SBTXp0qdL-e7ybEVgAgg0Tt9IF2WzjBhpk8boWiesiverOdZTO-g13Ft3PfiL3ClZ5k7iieSQE228WT_vvc81YRDokZ0KisMXjXikoiGgEepBcrfW1A6nHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23265" target="_blank">📅 15:14 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/287a3c4809.mp4?token=ArSyxhSDCZeJszVgrJhgbcLwGvmpzMX5uK6WAcc_1K-kjESRjUsnz1Z9F49k2B_FQsXO00D2lvfliRZ7C6T5VYctDAJozlUy0CT39qgmwuicMMvXbOqRls_ygcuHarpaMnSGh5KyH8bf6lPdeo6kR6EI-i-dWOmtKEwhvCYsyKbaSr1OKcUd1WI8HbnijKstL4UHsYgI2iCwCZpyBWxWqHyVwje4loavxjBHcYEleq0DzM1ZSxyeeAXvmjbCYtJLfEHDmXsyi1oGzKF6nj1-JtlC_MbPQ341ax_88vtAb63k-0AkQ-CsXsv-hpxw-TOHXF34sk9Jyadxk9m6QucvEoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌باحال‌از مسی‌ودریبل خاصش؛ همه میدونن‌میخواد چیکارکنه ولی بازم دریبل میخورند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/23264" target="_blank">📅 14:53 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23262">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otMSS85PcolDzgCwL2FiR5Cx2M9VA2s8_TC8tbV-VZroKUUFqmOyCzKO05otzWJQ5d6UZgdjKNx20eSYOV8hT78XumIe_f3L8M9vWz8E4n17PIMIV_Cb3OM7cipg8hbbT9Ay_RAGb4qAiVt29TRVYkNKDbF2vPOU3G-XF0ir6yy81AOlrVwcXmERwwFZAdJL2BAIOYgVYImffVzUHCI6w9dcvTmgF_D_efBJSXtFws64XFNvyzWu3MuH7qYO4vATuuBi5Re0tBISjhatu9xtwioquTw5aEB1v-AXmkvPNd3CrqX00LKQ8cs35nnkRdMEmwAgZ-TyLEzXWa9sXBVt5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۳۲ باشگاه با بیشترین بازیکن دعوت‌شده به جام جهانی؛ بایرن‌مونیخ با ۱۶ بازیکن‌درصدر این فهرست قرار دارد. تیم های پاریسن‌ژرمن، آرسنال و منچستر سیتی نیز با پانزده نماینده در تعقیب صدر هستند.
‼️
نکته‌جالب‌این فهرست، حضور دو باشگاه ایرانیه:
🔵
استقلال با 8 بازیکن…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/23262" target="_blank">📅 14:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23261">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eeffe144b.mp4?token=etzC1XevbLQJ-na9E8Os7GLNTwWB_EOYEnc_HH7LHjLs87ooa60Jd0FyQQNCOWYiAlwVG1iJOIkj_-ZW1-FXsXIwqCw4JRvpibhWcg10gNJlNeye9vFVHttLt8mSQKEpEVoOPocQhwqqkK9cyX-cZgvsYqu1uiQlwxnl9blYo44Q37Sa083WSzB78KhWnAZ4iETA9JY1IQZGJn71ZuePi-wM0-PoPt2fLJKktCTIhmQWXpC-F0LGnQTcXnNk581n45hTBt1CYHcpu7ovhMRB6k4ddwZNUuZmM_4m5o3AYseGYy2ZWb_LmOzcVyKmexKQFY1cVUWCxii0sUUMNHLsUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23261" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23260">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjnJpFt8rY3KMM8Vfr1c4-oRzHN0wxARMsPazaVAW2OVR8JOKKnZ9CyL9PrUsoOEh8H3F2tZdocuwuGN-U2aMQKctNnbqMnBsvdj-VgZgLtHkjiustJAD84DieKqRo0ejv8WClI57djRMHvuczgUWFdcVMt3fVvtAqN058DmWUdViOx0enyCdGMfKAjRWM9mC1a0kUUjcQql_Xqz5mhcitZcbkao9oVy2POFAlOrRdGQ_X3bivhxoq12i4ZBnfDZiOuBSAgx7fWaHwlwb1tA-dzsiEV0jePiRT3ZGwTeNUO-whbXsrRT2HtSgqEsplgnEAewF45KIjhIdPhJbS4Ikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛دوستان‌عزیز لیست نقل و انتقالاتی باشگاه استقلال کاملاآماده‌کرده‌ایم و قرار شد امشب بزاریم که‌به‌احترام‌مدیربرنامه نزدیک به این باشگاه و طبق‌درخواستی‌که از ما داشتن فرداشب لیست کامل روبا جزئیات میزاریم. امشب باسه‌بازیکن مدنظر تیم جلسه داشتن که فردا…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23260" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23259">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7927d57219.mp4?token=HpYvolE5WZyG8a8wMLnQlBP1viS1LpX80PeZFXTka-afL8JZUMKjvaBRwkYfPGvMsU8ncz4O2nfjE4EkBHT6-UDgQb8vCBRltk_hxTgQsx1LJM0gIeaE48gkiFM7F0Rf3EIuzbR8NlA1e0OyNOhJoJKj2QZb3_wI38sYWfFRHyis2WEX7Nd8e5c8uTakmdfBqojzheJDznC1zdKO1h3uOuF1G1dKz_3OKtttbGFOgt6PDVzqCUqJjnICRUDdTtCeP1Dg9f1yoeKFV2-tiKPDig2wH3D6Eb-twUQ4iCywc8BmLjvpY-7osRgcDmv2KZVx_7le9tu4Cv9rw1jSRMgZAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23259" target="_blank">📅 13:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23257">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lRPkKrUt1daiT_VldpiTTaWgGld-YjkWhhKTIbsnldKAji6ExWq4Q5t0vEzrPt3EGEvJZ2ZI4i5GskAulzcfYKmMiN7wFC2PvAVA1v1JqQQK3kzLwD6-dfoczAFpx9J1k6tn5uslRIvhAK_C9ySi12PI1PmXlkwKJPfAMhZHJj4SQAt-ssgvciiarw3ANk1f9emnsrs-pSpCBO-rPhX5RnyGzWJOEhqu0W3yDVuXHJhUbdkuNMc1hCbf3D4yJY-uyoGIYMnuFlWvqzxWV7JFEo3wammlzsc_zPeF7wLWcDUsi0pv6qscleJjxiy_0x83H4b3Ea8vcIPe8369hLLMhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNF3kVTylwR-jrUqwAIqjkAv_bQijL7AQHMEq8_3slAkeIotEimLvo7gljNg-2HXPHXtZsn_EeW8m59uBfB-963nNHMgD4VdE54Qxoav1qi6Tuo_iK3NCtwV15urtLjl9oLFCti7CyzdodAVD9vJcmV4FslZB1r6mhS4Me1Xk1C0w9GsYd7LmA59n98VsGC3lP2KPL9lk09W9uarRdfXcsjchJxSo08_0FJ_aVdMMNz8JBO14mo61idXStaetZRUjaWDypRkUrZXXqsOLWWXG2M8PcPJRGu440gsn1Ucx265XuKXfS_R6IA9GVs6lRVJ0OOqS3RSGfOao1r46A6JFA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
به احتمال فراوان طی روز های آینده؛
پائولو مالدینی، لوئیز فیگو و رونالدو نازاریو نیزمهمون ویژه برنامه عادل خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23257" target="_blank">📅 13:35 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23256">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
استعداد ناب گزارشگری روببینید فقط؛
با این سنش چه صدااای خوبی داره چه قدرت بیانی داره. رفقامون تو شبکه پرشیانا اسپورت تو کانالن باهاش تماس بگیرند که گزارش بازیارو بهش بسپارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23256" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23255">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4ueYb-rjSchGzMSzErhpen9ClbFUbC_VNoouwFhEQsvJBiliS3-CCyvwqOhkv9IvW66yctTzhcuLQnn7WG63X0FlDmeD8jfLKdhDZb_L-49dw2zZqMi2d1xLUGY7cNZA9ngITBKaJJObM-gelFkjy0DvkjYbnHtLwCIUxR3Cu4ZvKRTvLfpFtl8ApkEtWSfoHYj6X5oAzAVGCCGB6cm6u_kbKvUApd07940lt-Oaj8eyuojpOyV9TNVVM2zfMUEV78Qar329lsubxaN1012jINK8aavgyRea5S8AT94CyNT5E2zkCCGXHGNNK3ew7y37MMle5h6BNCNdPNnCaxaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
خبرنگار کره ای پیش از بازی تیم ملی کشورش با چک درحال‌ضبط برنامه بود که یه خانم مکزیکی اینطوری خیلی رندوم اومد ماچش کرد و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23255" target="_blank">📅 13:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23254">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N87rOJcDp-EuuU3y1AR8KjTJf25R8TH7yysKbE34OqDlph9LZXLCmzqMGNgop4poIk4pB81pctBuANpEZWJaCxZeTP8lfypEyXT3YZbzXgaoEfkrGay-dv0hSrhxWmiWvmf_e41etzF1A08iO8beDTJobvclSIBUF8blcouIvbFMgyIR-nAu-pW5dlYgQLGgssPJpTUM1ndzN0ftICuxVmMXSmzrHCc_m7Q4scjx_e9tHdCgLYGNuawXBNdnZDWhpifdFE-0w8IBaPfYGPYoWzZUkqZe1rgrfCE-cQitvlc6930bZ65NZlw7WXsIrn51dtiJcwp9WFnNTauapOkPTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ در صورت تاییدیه مایکل کریک؛ مارکوس رشفورد قراردادش رو با منچستر یونایتد تا سال2032 رسماتمدید خواهد کرد و درجمع شیاطین سرخ برای فصل آینده رقابت‌ها باقی خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23254" target="_blank">📅 13:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23253">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/srKB6EhCk4Yof3j3i2RIeX4daVDN_rTvg0DY2FD6oyFRDYd38Yugapyz_a-CeAOOXMIzi1TcFUGgu-FFf7o2B1XNc5GO9yZZhsHqW4zmAj_Qvu6dpQo31Ajl3mwpw2CN3a0H6Pd-8IqlYo8BUnVMz9gDO2pC6VWWgKOdAR56RIq1QzXS_Q_X82TSO0ZJyHlccY-6FPLEm-T87m9rXVvoBloyg_jR9Y9Mn-ESZxl9hq3m-nLI98o2v2Z_KYRGdnyAgF5GtZsl9BzvvCh7szr4hcsaqSIMxrs58wPWlahz1SmOUDqFhfIlEnj6APm4VkDUyYs08z4P9kZjSof3FAmhDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23253" target="_blank">📅 12:45 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23252">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=SSI38-M0rM_uixRnsEtZIpuOMXkzl_su0VKitr_WpeLlyp34ouBf_a6AOL-fCANSJPeBgjZSwJMoltRS_LlmliVtdnY8n3VAuX7Dfok7E7CUMubG6p20undCTwZGs8fOgU-tmrlz2wdCRToqFC5rVl77qtlDuOnfZKG_JNWgWjCQfzYGG7UYhG4iIDBJ8_4cjIxyXiajhTf3R_lsGwvQTe2MPU9tj6fT2cZTN8n1EQPvJCF2fplZc53ybB8p7wDzbm7vRfDENDChfHzxJewSpvE6NV3ZE3aMjdpjNtLZ_VJSYkdlurnHcTAzKd7TmJhXzlbxwk_-rAcMZEYgSLpwBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d91e6763c.mp4?token=SSI38-M0rM_uixRnsEtZIpuOMXkzl_su0VKitr_WpeLlyp34ouBf_a6AOL-fCANSJPeBgjZSwJMoltRS_LlmliVtdnY8n3VAuX7Dfok7E7CUMubG6p20undCTwZGs8fOgU-tmrlz2wdCRToqFC5rVl77qtlDuOnfZKG_JNWgWjCQfzYGG7UYhG4iIDBJ8_4cjIxyXiajhTf3R_lsGwvQTe2MPU9tj6fT2cZTN8n1EQPvJCF2fplZc53ybB8p7wDzbm7vRfDENDChfHzxJewSpvE6NV3ZE3aMjdpjNtLZ_VJSYkdlurnHcTAzKd7TmJhXzlbxwk_-rAcMZEYgSLpwBoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|
هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23252" target="_blank">📅 12:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23251">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCWYXaBThtt7SpjVITGotZiS-zQR-zpdBALBS_4RIHOLEQukc-YPonwPl6ITOBdGLf34O_nZXIB3tM6y9ZblKpQ0EBCteQZ0pNyKZpmrRi8Mr24DxgYnKX5Yflw98Kw0FeTjF71LzrYk2yrXibolcoWZmxAIa973w471VRG-D9jSbWIY4d6mtoMEQghVt2FBMMw7v0QAhm-38eRZx5ZzjT6izTRdOzRwC0O46413oj5Ivx8-R2jMqnBrpGGOKtzDn7lnEqOvxlJR0RdmUhVFys-YdqM-PT1p8ETUtXWFqI_J8ANZQ1dsGPDxDw22B2w1QpCMZHHqEGatO7GC1LHgUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
خوزه‌فلیکس‌دیاز: یوشکو گواردیول امروز در تماس بامدیران‌منچسترسیتی اعلام کرده که از باشگاه رئال مادرید آفر دریافت کرده و قصد داره بعد از جام جهانی به جمع شاگردان خوزه مورینیو اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23251" target="_blank">📅 12:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23250">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLDHF4zDWephXEWDzFuEuLRnPGMscexOoJLu8H3VUnyhELo0wwJSAoiiiXhnPxVymrca7zfWjBt8GQNRN2wf5hy67xM8-ehnlYoan09T91um1onGmoIlPTjtZ8kx1wxYWig63PLNjgmE9nqnjOHfpyT5EjW3ItsYUSMq3vbTSpVBM2fZmx6l5aOUfZb397jfSzBQ9fzyfLolPe-mIF0q8_Da8sP3XqJ3cOONvPItT0q9LMOnQxrWd4UMLvm5KYG-YRu0s8xQWzcybUIhC4i6QPqF3T5fRUHGFEe_eLeKmX8zTG147yqVae6UGqnQnAJhTgC6PqGMIgkP1oXlFkxnwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/23250" target="_blank">📅 11:58 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23249">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LyxHI-ajUH3sGl32xF_-P1Hs1xrOdfk0x9g0eyKmWXeZ4nvuLrxuLLXUg-6StI514vl2e2Hul7m8xVRdJEqfpKSh_lyAX691xbJubBB0zpXghw-GZTUPUtjGISQwVGzfWpVPRmI2_YRS7omOtIWjV8hrttuDR68DRwD1kJzXSXIB-dgWX6AQfAe3prPn9ndx4HNG5Nb6C2vWil-W30XA5J-DgPkPY2TeG1XM3tFyXkwJxIyIEkCbU7NTdUKtC5bIWwKhqfCmFpEfb3eF7T60gLUJ0ZnIE1AbD-9NZT-xkJb3U6vH1-HPpWGuI3ensma19SHfdApNMiUPZxin0NZYiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23249" target="_blank">📅 11:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23248">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/733942b449.mp4?token=YITyU1vVDYMejiGWbfC0PXMZX4ElKrD-Y-VrukzUAR9cKG9URvgQ8FRBS24nmo7wgrz4lJMUUqreY_P6M7TcJPS8NbNGfoWXbId-dc8BF_G4Eeh4UhMk4oNc4MmC8nxTFTrdW8Yx1nFBHnKOPi35m_keWxTfefxxNSJ2-A7P1XJqaXz0CEtu_8SFkPR4-kmYWpL8WZk3R-E28GvTn7-zQlsTjJBJ2XuoaUW5vW_p9uU4f-7ycvUw2jbN0bXZrXlrXcv0n7SYYteHI7-3hr4yNi0lkcFShk29O3mB1_NZVKkSo7TcltIH7dpmzGPRxfsapf5AjTH8NsKsfYYcRkv3AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/733942b449.mp4?token=YITyU1vVDYMejiGWbfC0PXMZX4ElKrD-Y-VrukzUAR9cKG9URvgQ8FRBS24nmo7wgrz4lJMUUqreY_P6M7TcJPS8NbNGfoWXbId-dc8BF_G4Eeh4UhMk4oNc4MmC8nxTFTrdW8Yx1nFBHnKOPi35m_keWxTfefxxNSJ2-A7P1XJqaXz0CEtu_8SFkPR4-kmYWpL8WZk3R-E28GvTn7-zQlsTjJBJ2XuoaUW5vW_p9uU4f-7ycvUw2jbN0bXZrXlrXcv0n7SYYteHI7-3hr4yNi0lkcFShk29O3mB1_NZVKkSo7TcltIH7dpmzGPRxfsapf5AjTH8NsKsfYYcRkv3AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته اول جام جهانی 2026؛ پیروزی راحت و ارزش مند مکزیکی‌ ها در دیدار افتتاحیه جام جهانی و گرفتن انتقام مسابقه جام 2010
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23248" target="_blank">📅 11:08 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23247">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=ZGVdfO7D5WEIdurZj51bvrCnZ_Jmdg3yxLbLq5TrZ63bvut3rXmcDx5U_wACKa_4eAzhH0YiDoD9eIzC0y2rnzuf2QHGqVyNlQNQayHRLd8OGs93c98IH5drJpsXef4Cg_swUkRezS3P6SbGvVo2-rooBuPlkDPv42JNM2OO75YV-Kg30CS5oGYxDOss7NHPmg1SmFSk7l6Bh5TZdWBfymabceeyDHBaaQGDaysROp8Csrd6BMG6wwa3VegdmsbymthAt41b_8p-oyJ1Ew5UUnjD9URScmMwPs0qbvMQupyJ0pVP3YcHf1OCc3UKIimRZsnPqyCQQbk2PvZmpW15VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b63a3e61cf.mp4?token=ZGVdfO7D5WEIdurZj51bvrCnZ_Jmdg3yxLbLq5TrZ63bvut3rXmcDx5U_wACKa_4eAzhH0YiDoD9eIzC0y2rnzuf2QHGqVyNlQNQayHRLd8OGs93c98IH5drJpsXef4Cg_swUkRezS3P6SbGvVo2-rooBuPlkDPv42JNM2OO75YV-Kg30CS5oGYxDOss7NHPmg1SmFSk7l6Bh5TZdWBfymabceeyDHBaaQGDaysROp8Csrd6BMG6wwa3VegdmsbymthAt41b_8p-oyJ1Ew5UUnjD9URScmMwPs0qbvMQupyJ0pVP3YcHf1OCc3UKIimRZsnPqyCQQbk2PvZmpW15VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
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
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23247" target="_blank">📅 10:54 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23246">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=rpbsWdnAYBZ3dVk_Tj1A8WrXB5pEzJJ8TStkiWEP0obeMmM73Pd4HBHZMKGGaVtmSlkS6qxGwysfONI2yFWckT5Dcq3GHcrT5Z4rSyVMDAVBTovVnL8-aJ3BDJEgVzLuuKOok9wqLFS52qIHdP1ZdmM1K5bC-9ZH73wB_AbfBXRKirsjzyW63Utg74K84sQC0cLM0dOONRCocjZfor1mn5R2BGP2x8XJV8wADwR7lIfeMO1ukWX7vyuN8_C9JI_tFi_l9jaxoikCo0vzFLgie1zuJmOFhhAT2U_lSqWUnHbYpYsafDpHZlb0cV12yDcNZtJJ2pomBCR9Xf31onHNbGD4frFkiod8Svyf-os33WfaRYwJZiYLxvQXXFn3jwtVrfsSAbl6GplZHL646sHnjM7Tc_yGMOyoCwnRC6G7PTHUsDYfEYFn81RHONmb0IEXeRkCgRJMBb-Fsu-Ri00sB_TUFa-sNIhXZLiEpMG1lVgZVG88iMs74-NqfTFSoxWYr86n0dsfMvJao36QCl213EmQfoekaVikRwtcbYIXyFxqSaHZ1mUp14y3vJQyKzCp9ADIgpe42q2UVNxN12PpObS6q-q5NMXtaJLGVtbVPA97Sn9007f50oZQZuAhjhuHuU4TLV2U9GKBihgyJbrGv27dAm8lFPh3u--REpmp0qE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eeacd442c.mp4?token=rpbsWdnAYBZ3dVk_Tj1A8WrXB5pEzJJ8TStkiWEP0obeMmM73Pd4HBHZMKGGaVtmSlkS6qxGwysfONI2yFWckT5Dcq3GHcrT5Z4rSyVMDAVBTovVnL8-aJ3BDJEgVzLuuKOok9wqLFS52qIHdP1ZdmM1K5bC-9ZH73wB_AbfBXRKirsjzyW63Utg74K84sQC0cLM0dOONRCocjZfor1mn5R2BGP2x8XJV8wADwR7lIfeMO1ukWX7vyuN8_C9JI_tFi_l9jaxoikCo0vzFLgie1zuJmOFhhAT2U_lSqWUnHbYpYsafDpHZlb0cV12yDcNZtJJ2pomBCR9Xf31onHNbGD4frFkiod8Svyf-os33WfaRYwJZiYLxvQXXFn3jwtVrfsSAbl6GplZHL646sHnjM7Tc_yGMOyoCwnRC6G7PTHUsDYfEYFn81RHONmb0IEXeRkCgRJMBb-Fsu-Ri00sB_TUFa-sNIhXZLiEpMG1lVgZVG88iMs74-NqfTFSoxWYr86n0dsfMvJao36QCl213EmQfoekaVikRwtcbYIXyFxqSaHZ1mUp14y3vJQyKzCp9ADIgpe42q2UVNxN12PpObS6q-q5NMXtaJLGVtbVPA97Sn9007f50oZQZuAhjhuHuU4TLV2U9GKBihgyJbrGv27dAm8lFPh3u--REpmp0qE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مصاحبه‌جالب‌ابوطالب‌حسینی‌باهوادار معروف و روشن دل باشگاه پرسپولیس که اون جمله معروف و تاریخی رو خطاب به علی پروین به زبان آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23246" target="_blank">📅 10:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23245">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQeLUnlWJJskEzZwgpx3zxYZuVckE-rVGoPko7bCdFz4Ya38ZK_639JPrUipG__d2Yiq76AKrUpqkFDQotTDMGTD2NRDD-p0-fETv4obIMLdunaohdCs3Wnj7VcxRVU9piLlHj6S2ML5LeAcs7CTWQ2M9ZVOyZiX_fEnZjimps09IoPiwfEY9HoDUY4sFo6AXBKA-I3b7GuGxz4JsaNguKaJnnMHnG9MwV501AuBUnWvpGQYFtfKqquXyrlSMTPTx_fRt62gChzSMbaoDD_6pJkFvdm8n-owKKtYYB6yO7ZdRsjXbMW6EsUaF1aRKYPwN3sS7O7DMgosKQ6c0IndVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23245" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23244">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5655edf133.mp4?token=ZdHr9jQWbScRWecFTD6sktilUxhoTRKHWt8-z4c18JsgmMVcNpd05UzSd-fI7YcVqJlMjqCU1eOfovEa5DlbanIlR7r9b7CPO1WKqFlswTA3Xz12TUJkIa2ICZW0v94fKo_Jn7tcoeXPA63S2N57QgKhQFmc7UWk90KmsYh6ynVuhfQeTGpuV5eOwsRtNwQmP7Ghn2rtgaGJZEDB_U5huqkk0U6ccETvbMsAJr4G73p6EHaP41U84vO2Z6Z5HO6ZCUdkwNEEmy4MFlGFLQJtybXLwawSJIMmFMfRv-QfDZC9Qo_tXFotq8YzhP4KpzCIHaLSFE3Ekzw7PNB2UTzyZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5655edf133.mp4?token=ZdHr9jQWbScRWecFTD6sktilUxhoTRKHWt8-z4c18JsgmMVcNpd05UzSd-fI7YcVqJlMjqCU1eOfovEa5DlbanIlR7r9b7CPO1WKqFlswTA3Xz12TUJkIa2ICZW0v94fKo_Jn7tcoeXPA63S2N57QgKhQFmc7UWk90KmsYh6ynVuhfQeTGpuV5eOwsRtNwQmP7Ghn2rtgaGJZEDB_U5huqkk0U6ccETvbMsAJr4G73p6EHaP41U84vO2Z6Z5HO6ZCUdkwNEEmy4MFlGFLQJtybXLwawSJIMmFMfRv-QfDZC9Qo_tXFotq8YzhP4KpzCIHaLSFE3Ekzw7PNB2UTzyZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
زلاتان:
«مسی یا رونالدو؟ مسی بعد از بردن جام جهانی حجت رو تموم کرد.»مسی یا رونالدو؟ زلاتان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/23244" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23243">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5uHwKrUlMwQpUqS8oS1JZXRP-TbYoVbMbc1ryacb3cgQSKyLuxyOSOKyzkLt3JuzUmJJ8grHbwKOs8FpwixKNdChtBpgwl5oPqQz0srQ96e6kDnr1G0OsPwfYzC6olWtXwgi0tYnuJT9cVtUjIFTp9cYHzBuCrrZiLIzVL_QVPn0fIPeP9-JY9dAjGcKpL77_cS1FiVR3g7fxdQ7OIV83d6ThOSLzLmZh-KFh8pWp_856fDE2HX3t-oBgSRvJqer9xm4OasQ7Y2MdKGPdj9_QIXF05xPqx6Fq3rpp8S_i40G8U7SgQRY93eeauhS5qxnf5wNkr27M_4z52ihhj5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea22
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23243" target="_blank">📅 10:34 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23242">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=YqbR56_3jEzFGhc-xSXfKFhyLSkCEQ3MZGJiqxxl-BIDzYK01K1LvTqCIMthABmRzuvqCiL6IT7oX-oSVogx-MzwgBGWpQ_0sJ9JEsCoYgkNQwL8m589k6Rx8Qe4k37cT_1ODMPNN3464maWBMJqLT5x8-1zPTzAZf1gMuRhVnttfKb71v0FdipA0R0Ok_l2S9hUvUKlHunPCTbJM13nloZWgZGq5dJlivKNhzZdKWh3p75zZwmaAa1XXvCc42bw0PXZsYQf7mbkFxiid6vFT3BVZccQEdgj3ezandh393EGce0JgBTi3jHeEds9qf5lk0NI7rxBBK35-TM9Df5XLnIgIfRLjvlVoOyj02gyet1aY88R3BJRAU8bMogcqXB60jzWciuFf-gc0RBb3Jzv3vFQM4k2bpLwH16_3WVoDyCh7_NNNSsQaJMhqfK9OJab2rwzvYASrJW06CwOBKF79_9BCKoJ8oxCIScptSguUP33qi8k3DMqxjmDHCy_-JRQNhmTCucAVhq1T_t6lngO_-iy-c1v8-qHtW4JENCXxKs1zCPuXJw3Mh7gtLfI_ZkkQtlm-WO3uR4Wt0OrxHSEBw-84wQim4nfFvzIK2aIAOeP50M_l13YFyy4RoU6UyRce5K8e2uF7UT1w-0F8yf8QZGOV7NO2GdepaUtLSP4F4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0f934920a.mp4?token=YqbR56_3jEzFGhc-xSXfKFhyLSkCEQ3MZGJiqxxl-BIDzYK01K1LvTqCIMthABmRzuvqCiL6IT7oX-oSVogx-MzwgBGWpQ_0sJ9JEsCoYgkNQwL8m589k6Rx8Qe4k37cT_1ODMPNN3464maWBMJqLT5x8-1zPTzAZf1gMuRhVnttfKb71v0FdipA0R0Ok_l2S9hUvUKlHunPCTbJM13nloZWgZGq5dJlivKNhzZdKWh3p75zZwmaAa1XXvCc42bw0PXZsYQf7mbkFxiid6vFT3BVZccQEdgj3ezandh393EGce0JgBTi3jHeEds9qf5lk0NI7rxBBK35-TM9Df5XLnIgIfRLjvlVoOyj02gyet1aY88R3BJRAU8bMogcqXB60jzWciuFf-gc0RBb3Jzv3vFQM4k2bpLwH16_3WVoDyCh7_NNNSsQaJMhqfK9OJab2rwzvYASrJW06CwOBKF79_9BCKoJ8oxCIScptSguUP33qi8k3DMqxjmDHCy_-JRQNhmTCucAVhq1T_t6lngO_-iy-c1v8-qHtW4JENCXxKs1zCPuXJw3Mh7gtLfI_ZkkQtlm-WO3uR4Wt0OrxHSEBw-84wQim4nfFvzIK2aIAOeP50M_l13YFyy4RoU6UyRce5K8e2uF7UT1w-0F8yf8QZGOV7NO2GdepaUtLSP4F4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌جالب‌از برخی‌بازی‌هایی‌که تیم‌های بزرگ تحقیر شدن و شکست سنگینی رو متحمل شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23242" target="_blank">📅 09:55 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23241">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=MHCmQuAZUAP9ehrz7s9mV9VbTefUT1pbO3duIv9Tg6az30r7eKtEeBqfDaOqF_I47wK04HngyCvIAqOM0BUjA39CFAlK6Up97pZk9opsqSsuCOmHnSv8ObGF4g8k9cU5tzrCmzMlpwSi5s29KqFbLJ9Wqh-jO7ntPcAnO97oZKaqf6H4K2EmOsNs51kJlmWo9MkPtwCDPlVDtOqqmDzjwPnOA5oeHeuY-DMUEfNUZlJLyRNb8lfziUWwOFdn4OZYV6O9kJJVgjaL4ZZ7TdWm4CwMsDjdHEOtdPU1q5ZmfY1C4HuIITr-9VNQjyEeXkel434aAz3iaN-FXUwh7c35wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35493e0c7.mp4?token=MHCmQuAZUAP9ehrz7s9mV9VbTefUT1pbO3duIv9Tg6az30r7eKtEeBqfDaOqF_I47wK04HngyCvIAqOM0BUjA39CFAlK6Up97pZk9opsqSsuCOmHnSv8ObGF4g8k9cU5tzrCmzMlpwSi5s29KqFbLJ9Wqh-jO7ntPcAnO97oZKaqf6H4K2EmOsNs51kJlmWo9MkPtwCDPlVDtOqqmDzjwPnOA5oeHeuY-DMUEfNUZlJLyRNb8lfziUWwOFdn4OZYV6O9kJJVgjaL4ZZ7TdWm4CwMsDjdHEOtdPU1q5ZmfY1C4HuIITr-9VNQjyEeXkel434aAz3iaN-FXUwh7c35wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
مدعیان‌اصلی قهرمانی در رقابت‌های جام جهانی از نگاه کاوه رضایی و جواد نکونام؛ چقدر قدرت بیان کاوه خوبه. چقدر خوب و سنجیده حرف میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23241" target="_blank">📅 09:43 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23240">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQ7ZqnRisdhh0CUzlxY5ZpAhetPrX4NbXRdP5uKfd1F7cE39sglwQK3b-Tmlv-RM6U48T1Wl5hplWtbTvyBnPtMjnZDvwxq-DkNW1BBFApV7JcSCiDYzxTuk8jZkAnYr-AMUEPdvkLojF7Ks5I2oxd8sYxq-klcrnpSD0LbKCTr2QfWH0Tegkz-9LiRRS1qvgNPhWQm8X62eWmFzR1CdnD4gJmFyFKgztMVQvmbVdY437wGP3PDDbs5VqHcXxoVAm3AgVLjTzMFfKUg31HWphck2nRet4jC8qO_QnjriCu3MyOlbFi3iOzhvMdUfqWEiYAKmH1BgqTQmDzVIYX8S9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌تاجرنیا رئیس‌هیات‌مدیره باشگاه استقلال: باشگاه مطالبات یاسر آسانی رو فراهم کرده و بزودی به او پرداخت خواهیم کرد. اجازه جدایی به همچین بازیکن‌‌ارزشمندی رونخواهیم‌داد. یاسر آسانی و منیر الحدادی فصل بعد نیز در تیم استقلال خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23240" target="_blank">📅 09:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23238">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=uzU1j_JMg8Z2B2vbOMbg3mJarUEL5WtGuNBcVmlyQJFX5nppHf4x1hnJ5fF8NmMx_2LmzuO_NO4IHu0uXCEva1vPtA2BMFY2f1-8C_dfKiP1u6iGjZ1OqUHiGLEFkwz9X-SeFQr30GSzqxJuCHETp2SmnoHCqBHgxQnvF6F4WNpk3aowgnUgYpKxtVDBJ3EmMWVWPnLTp02vSSC0w2TudSem0D7zGONRwSQizaLOrWjNbQ866rSiWp3QsNbdSFFTPLkLpxlY3463uYstpMwic5gEsx0LOQqmk5lZeErFs1VnljFOBhWfruZ01zJgQ2jnmhTecyZNWMegseuC-OymYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57efe2f2e6.mp4?token=uzU1j_JMg8Z2B2vbOMbg3mJarUEL5WtGuNBcVmlyQJFX5nppHf4x1hnJ5fF8NmMx_2LmzuO_NO4IHu0uXCEva1vPtA2BMFY2f1-8C_dfKiP1u6iGjZ1OqUHiGLEFkwz9X-SeFQr30GSzqxJuCHETp2SmnoHCqBHgxQnvF6F4WNpk3aowgnUgYpKxtVDBJ3EmMWVWPnLTp02vSSC0w2TudSem0D7zGONRwSQizaLOrWjNbQ866rSiWp3QsNbdSFFTPLkLpxlY3463uYstpMwic5gEsx0LOQqmk5lZeErFs1VnljFOBhWfruZ01zJgQ2jnmhTecyZNWMegseuC-OymYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هنگ کردن عادل از مصاحبه اخیر امیر قلعه نویی سرمربی ایران ازسخت‌تربودن جام جهانی 48 تیمی نسبت به 32 تیمی: واقعا نمیفهممش. یا من خنگم که نمیفهمم اون چی میگه یا قلعه نویی تعطیله و ندونسته که چی داره میگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23238" target="_blank">📅 08:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23237">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spWUZw9lfVa8uy4hrZ4JPuDWxhpDqiGmdX2C2BaAlGepd_fKSRE8q2Fr-xVf_F9e48HapzI1oKQlyd0f-xjzgaYog19ToKoiEB6QAmaWsLXJl3EXJhPji0E1H_7QNi7T3g4YOJQ_rR6R-f8Eu1LI2J5YqftnZfhOjKLPw35WxFwv8Mqb-VDW36QpZF7UuWdIqGWCB18z_Squ9TrNEOerBWLEvgXbifq_e96aJw34nBzVWyvElnwIJ_Ydyd2L1jY9uoo1H0pmgEpPP270J_EOqjUWAWGvWwDrhenjaL1jqcmEoNaQUG5SQtXSfqVzIkZvz__2kcJtsoiTS6sI9HcS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23237" target="_blank">📅 08:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23236">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23236" target="_blank">📅 08:02 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23235">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3FfSJmgCZgSekeFNeYDMsqItIPxFEoMk7hSMcueB_DUStBOfGrXGHszr9vliyCnavk09J5YagWW0LIQ55xBsDXUn9cu8kjcIo2eWT9UweZr2I8_HE8F2kjXt74g3pJ5oXQuZGz7HPbXci6HaeOXOkVIYKMYpAnFdlqTOzaeGC3jP7E8ZN3II526koJda3EHZhDn12vczO6OtHTdfqTcWILP49_ASDgQaV3UTzVJDPS05xj2nsfvHygnF0kYqcSbrjWGXOaoW2HxIn7n4bg6QsoqzAqAFsUqZDaJQduNjXqVnn-FNkRKk-E6XWWDlu5ysHqy_dbJapmL3pQyXaG5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23235" target="_blank">📅 07:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23234">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rvoe9mztKaYEmmWfJqPD7KqeEfjkHxNyD_U2dImA2amDv8NBYEX0ZZqWiRFkvCUBw-p7xokoHeOgmNRgDODsIo5Oc3Dvol0_b0pAQKm3RNHZTQagiL8YtpN7tXBHdWi_a_oZLKG3zS_JYTSdmE05fGldFdEq-znzjQGVrpKEBmYpuqy_gExJyjpEdna1s2Bedxj2azDXE9rhdvpArZKDrytq4AuVqB9NrihnrlBJCE9YigOhAQckLaqB2pK9PIupFjKpBKZKWIIh4G-zJw40ZSc8_5D0Ez_b-DktPW9B2aotw63N_YWQOQ4zWjCRzNwIYdOPKGTIuimffKMn5aceSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
کره‌جنوبی برای سومین‌بار متوالی در ادوار جام جهانی حریفان اروپایی راشکست داد تا به این شکل کار خود در جام جهانی 2026 را آغاز کند.
🔴
جام جهانی 2018؛ دو بر صفر مقابل آلمان
🔴
جام جهانی 2022؛ دو بر یک مقابل پرتغال
🔴
جام‌جهانی 2026؛ دو بر یک‌مقابل جمهوری چک
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23234" target="_blank">📅 07:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23233">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=M9dzQ-3vBxr1JGYpFvIYelPG-JRGrjZ22TaTfYOGnnB7YV7dtUmGXn1z7_uAoWG0nz3x_YEQxxSV_Sr1lNoo08xpItWeIIulxVQr46YlXnaQ_wKTQAPourlRXKszklOY25JlBwPPe2uqCs_eNZXbWFsfKi5LSLST10rvOIwYxx-PqQHjIG-JJpCwTTMzx5uzaQCt2KFIL8NoIDr9msCRF4XgS-2UdVXKE-l9ud5WNI5W1wgrm2_bGySdduzcLyT9cQ0zOC4B8bHyqJ_j0vPM3EQlzRmTOa_IwvWy5usmXz28IObTEyliks9skzeaK9nS8xMYQXqgW7tlowHpn6NwJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d61b75a83.mp4?token=M9dzQ-3vBxr1JGYpFvIYelPG-JRGrjZ22TaTfYOGnnB7YV7dtUmGXn1z7_uAoWG0nz3x_YEQxxSV_Sr1lNoo08xpItWeIIulxVQr46YlXnaQ_wKTQAPourlRXKszklOY25JlBwPPe2uqCs_eNZXbWFsfKi5LSLST10rvOIwYxx-PqQHjIG-JJpCwTTMzx5uzaQCt2KFIL8NoIDr9msCRF4XgS-2UdVXKE-l9ud5WNI5W1wgrm2_bGySdduzcLyT9cQ0zOC4B8bHyqJ_j0vPM3EQlzRmTOa_IwvWy5usmXz28IObTEyliks9skzeaK9nS8xMYQXqgW7tlowHpn6NwJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته دوم لیگ ملت‌های والیبال؛ دومین شکست تلخ شاگردان روبرتو پیاتزا مقابل بلغارستانی‌ها
🏐
ایران
0️⃣
-
3️⃣
بلغارستان
🇧🇬
25|25|25
🇮🇷
23|19|21
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23233" target="_blank">📅 01:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23232">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⚽️
👤
ویدیوکامل قسمت‌اول ویژه برنامه عادل برای جام جهانی باحضور پائولو دیبالا، جواد نکونام و کاوه رضایی برای‌دوستانیکه‌نرسیدند کامل ببینن برنامه رو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23232" target="_blank">📅 01:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23231">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=i55k9z7U2rW9x0eDlC3EOB7LUUhXPywMMhY1uodhymuIUucmPzqh8sCGtywJB--Zj9s8dUHuYSVBOKjPwI8URUPn16tollqmdkLIoC_LyiHFz0VSzO4zXadweySIkaVJM0Zg6DXeOmz_vDiZQT36ZrDq_niwW8WoXaWUh9mzYb49zGciUaIGU6I7klhB3bnF_eIuIlv-4T9zWsMnQ69E014a1Hg-Xz-MYwbo9HSOcIHumhey7ToOSfAT8O9yvsCaLrZLWkGpjJcmNl_KZWxTPbT7K2KDIQt1GnHRQhKWqojzMvw4teRA-AN7fu6Gk90epqqn6C37w-WjqPNinc5kIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caf2ee1fc9.mp4?token=i55k9z7U2rW9x0eDlC3EOB7LUUhXPywMMhY1uodhymuIUucmPzqh8sCGtywJB--Zj9s8dUHuYSVBOKjPwI8URUPn16tollqmdkLIoC_LyiHFz0VSzO4zXadweySIkaVJM0Zg6DXeOmz_vDiZQT36ZrDq_niwW8WoXaWUh9mzYb49zGciUaIGU6I7klhB3bnF_eIuIlv-4T9zWsMnQ69E014a1Hg-Xz-MYwbo9HSOcIHumhey7ToOSfAT8O9yvsCaLrZLWkGpjJcmNl_KZWxTPbT7K2KDIQt1GnHRQhKWqojzMvw4teRA-AN7fu6Gk90epqqn6C37w-WjqPNinc5kIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل‌فردوسی‌پورخطاب به دیبالا: تو ۲۵ـ۳۰ سالی که کار رسانه می کنم تا الان با ادم خوشتیپ و خوش رویی مثل تو مصاحبه نکردم! خیلی خوشکلییی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23231" target="_blank">📅 01:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23229">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txAsCMEUaDnkUikLFU4ae8Vg4INREImWHmiADjnDvWnCTTNGqVGECardMWlN04bC7GL2ajuuqhVPoYdGyhvdI5yb_XqLsTekYlr9Sp0m411d1Na2-cIcHFQZxTCtHtgLdvMzPH5-fKdksqqLUKRCRg-9KHhxJfbrmO2RS4tHmEGyQMkrsH581AJHm6uefTQgqOa0qrH6srVrsQEIedL3YtE4_1xvWO22MdsHkfmPddUKAh1Y8QbqkB_ft0RcXD4kAhMPpFeTXkiyyeLBk_CDOMcNacSxFl92RrXqJnyx1eDm7y3_WAov4oMKzlUOTafX12Z2--6hCVIb7DLRhtIeKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛اسپورت: تماس‌فوری‌خولیان آلوارز باسران‌تیم اتلتیکو: بندفسخ‌ قراردادم رو برای باشگاه بارسلونا فعال کنید. فصل بعد در اتلتیکو نمیمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23229" target="_blank">📅 01:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23228">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuE7wXZQq_IU6Ss6aC1aQbREANs68ksMCHlgSJbwTOwPbkXUH7Ga7runeKUmUF3FKVdA8baqHRXPayWlxQiOMI0Ca8dfZdd0SomgJc3GPUwXWPuaphN--zcy01tfEwsYXT285hWPqQo8rCKQZzlJqTp_vroXEZDL9-jq3vOy9VNVdffJ7XclHQXQoBOmPH7Zis4NnQdKQAEXRpw3AqMb27Uc6Dw-1p3uggflTcN1c9DiNqMH2uzRm-EvaVEBjjSD6h2_90XvA3s0tsY1oOhWujAOBEmigGzEH_hXOn7-Jeb_b16GhFPfTfKrtpIt_b-f_TNG6EZIx5YiV2ddxxxiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
روزدوم‌تورنمنت با برگزاری ادامه مراسم‌افتتاحیه‌جام در دوکشور کانادا و آمریکا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23228" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23227">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSNCpxMSDgrYq7C6DAm4zXx6BeBzwsDg3_2PFmyi6YZquKx6MfTIQu6edWtrsXAzAnyEsz1rmFvlwIt_OH5oiLYbHmdXPhrmXr0xJlBt9lAJqdpTtQ9rAnDEoQHBhl0HDwa96i7HPw8ploaJD6aVewe-g9Al3w1Uwps05R5BQs1184TSHXDT6soXtgb7hpOjoBF4SnJ2C20yYXfblKaWDcgsusOyk2Be_oemUFuWto73MQRp_CbuR2RWT7_QPzEiZhhrtsassbqp89nb-h2pB7MMeGIib6XBk0HHWAWbI7_W5TSfMMV8R7nI5jEif12LayMDL1WMHNlS66jbFQ7WGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدارمهم ‌‌دیروز؛
استارت قوی مکزیکِ میزبان با غلبه بر آفریقای جنوبی در دیدار جنجالی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/23227" target="_blank">📅 01:22 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23225">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">▶️
قسمت‌اول‌برنامه‌فان‌جدید ابوطالب حسینی برای رقابت های جام جهانی 2026؛ عالیه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23225" target="_blank">📅 01:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23224">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZL60m_71aniaT2wgsSx7E7YXxhqjzkqwhubTpPrfmXOye6xZKxr9qUFeT4ST1J3Fm021_UkAZBvxmXPR3P2yel7T1_wgfkqTvtmqfW-aj517xr5IdJmlG7OfpG0qVZrUiK2x7eD-hI433BOYuyj5u1bXcGdKBcRKPtIbO3QMrFEAkRCWjSV0izHEfC07vosDciczAFrdbQ9yITMIwCXzMcQcH2X9TSuxrWPzTdgNJZr1DH-JZU6Yved1K-nAMYgDWGsSgZj7NGxIEDAGeAx45glKQhBLLe_h0lL38BuJQ2fAeQEK2L_xpCWSryPpEJGNk5z0Ba2zq9dByRgKcrDYzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ با وعلام رومانو؛ برناردو سیلوا ستاره سابق منچستر سیتی با عقد قراردادی تا سال 2028 رسما به رئال مادرید پیوست و شاگرد مورینیو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/23224" target="_blank">📅 01:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23222">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r_jiLrlcUFlXwwZ-dNpPgkKHCPDPluidaif2Ws63x8bkkZSJADjEUh_xc5Qir9E8kf8FLNThdn9-rLY7UlWHX-9hX93_TY4HY9e8Pj3pXkxhoI1U0FtOLIu-uRAsWSWDfO8HN7JXdaq5C2JxqZhL5TXjGwheoIEkBlRVPIdm3znTpX5ojplDfXLRTPzZUXu9HHzM1jo_wCyJkIEFMQCCv6rvv7fT5HelFOaICWROKU00UtyXIsADn0OQtT5SbsnARwbDTbxCJgPleJIRx_xcwK_iyecJb0REwe_YCdLaOuQrAvyvoMprf269-Xbn3j2vrtOUxTR9sZloIcSWd6ArwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7-3AvrDDdKhLxg-_5ldxl0U5ATZU61RqwESAD6U0Zzmnt6D1kZQPdJWxQMM4XRG0irVJRyssod_zDcbDyKKbJBdKEG-SyWildzmMWD4ZzVeyKN6nm_SEbme2lwbq6wbnESDtD-fjtQD6wIvOJpZw7SFwYCsNqqclsEKF1TnQCwoXjCMdksTfK-Wd2vpJSoC074zYIvbBdHFK738Q55ljfSJS_SlkDiJBFfBybvWl_Uvi_01ZJs0P73CWZkmo1RhFVrFYvKYHP2XkMJwEPbfXRxmvCAJ6Vvr3u3qRG6kMFUMPJkEzZSgFNde4XsQteUD26hUYI_jGCnFC4OktY8WZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/23222" target="_blank">📅 00:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23221">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzhrvv-WlyMC86HqnH_8qIJRuehHYmlMG95zOQfKrXKm1ht3Fcr-4XVzPEo9_SSsaHveyTkFIVbSpmd9FMQdRQinnhgQlrPXGCSl-EPmqLQGuQuTFBLlMUmgXpr6wAoxQ1H9XfAicV6YBe1DlWZubMolpmifrCNqMPrUp10VlElAVPrNix01ZLPMSs_PAbjShuxHCXvkkkTNeOE72FqsFFjFW9cP6hej-TxqeHGstX3mWieaU6ssb2aZhs1al2dP6m7-ZmzTZW6qP2mMeboRzo9rTP4ObNhYOKiCDXLhKa7yXEETkZMCmuP3d5jfeBUgR64Mcb0VJ9cDp_S40jDZEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حیف‌از این‌رالی‌دیدنی‌بازی‌بامداد ایران
🆚
برزیل؛ شاگردان روبرتو پیاتزا در نخستین گام لیگ ملت های والیبال بازی رو سه بر یک به برزیل واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23221" target="_blank">📅 00:29 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23220">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDmxyJFXZdVecQv0POFfrBcP2HAtclmtxIC5U9g-v7-d6yx_VNrV4qOipmz1ExH_ajLGdP8dOzwHZQ8z_BK_7uSEziujvAzlsnvGgEQWPRRP30h9nD8nXNPwkrFfBVRaZqtqbkMjLnPVz4_ypUli-voY7vY2DfmQtAYaeuNZspaOhtJsU1brnU_2-Pu5pVch7FoyNxCQbcN05KAdLOc7Rn-_vP7PXjioiY5meqLKAkUzEQed3N2ChzuuJj5qkU0oGd8a2-OOFSae_vaekJ3rB_CNBi2nCfkZ2sEJk8tAMFovHRFDiRBZbufDFtiikBbo-X7jJ0RtKygKGZVlnCPoDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ مربی‌بدنسازباشگاه پرسپولیس ساعتی‌قبل به تهران رسید و از فردا در تمرینات سرخ پوشان شرکت خواهدکرد. اوسمار ویرا و کادرفنی‌اش نیز احتمال زیاد پنجشنبه وارد تهران خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23220" target="_blank">📅 23:42 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23219">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk0Ug19uXtle1pSazyr2mQ-QSjGCV4vYvzFmvWJLT5AieHA4J9Nqr-eQmu4d-YQw0wPnxiQoncVM4lPl3O9mvG825Ot7dQbkfktBhJaCRpKbLv2smDGtDcjh1g4xnQb8Eq04YTnXU5gVrAvQN23vAD5nXad5Om4_LNpxvjXFLDquHPAD5LCqHwjik_ouiiFyPkpTtyquFbQtl8b6tPSYjI9_P9l5TfxIgSGPrXF3KvqrZYNRor7foTVbVRbExKz4_8BbDic0LS-k7n-xv1QU5zYgHfV6kGq6AM2CpMAqDUcJuGRm8ELZ6zLK9eW26kywI348xgZQm8rTbKMOxbhcRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رسانه‌های اسپانیایی: درصورتیکه باشگاه بارسلونا آفر 150 میلیون یورویی برای جذب خولیان آلوارز ارائه کنه مدیران تیم اتلتیکو با این آفر موافقت خواهند کرد و آلوارز رو خواهند فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23219" target="_blank">📅 23:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23218">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8VQNUl3zOMj1VXk0tu2TObzl5egLPIsQJMvYYwTuBYr4jhh7USlacdFJBHR1eTVY987HldUuI3HbDM6AH9gTkBIcz5EGbhZOpKCYEiz4D4i83V6DCIxKucJ0exPAfeRisqY6VFznr3HHUC3-deSaSrM9JC5qD38gTJ-hENWjBMKdkTk8Ptx8SEggou5D-h40ntOh89O6rgUQCNN0GDLe7Oxfc7pFhFb74XKn3QNfAItHSE1qvyXgO3zqwGEDlfvotahreXWLzRVTjHRrnAC_ApHwpoyQEC0ClXKou7_Jqt7O0uodl2vyYrnMu1bxV-tV_qPqjepa00rP-hLrGI_kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/23218" target="_blank">📅 23:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23216">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UM6gTlTWjhbyynONi1Tm736KH0VcgU4_LD2KRpYp19Vkq--vJoXp8mFIqFcY98gHtr--WK318z1vXzBPDKzOq9gpfRKwBrt0cTG2iLcGqI_3iUVmkN9DcEBKW90Uz_JI5XPgBFUVjZpbmmXTRS5Vy2WKXy8Fsm5sRyb1Z8BHLi9PA4yY4dxwbY4QR0BuQGoU92zWfbv476fgl8V3Xyfa7fTB8Bah9PwltDGWEo8OLWHhOUa141aZG1B62Wxh4j8I3wl-6npsJUWluIzYJRWv0WapZO7wtR-Ng3DYUNjsqIQ2Jcapw83gOQVFmpL9LQfQERmocnUsnR9rdCuGssyDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qq7JwqW90uQNf3jUyBiotyOOaMa193Jq0hNRyH2Lld0S_TdzNmB1Yno1wMd-pOp9dCFp6NG4gbhUDreW2ClgMvQ2C9Psxydc-3D2JSRRbYJmL0zQfi3cMcHCNfFHq41Rw2J6nzq3i6iV0M_jL1yjz0GeS3G184J-YbzZebwkBrh6RNWP1oWXWlcvqg4cZ3kpwPuIktAB9W_kmOS_QZ96c4pC-2SqtcZ4gWjifw2nBuo0Ieu3UYaUIRf1ZXSGm8VL5I2urQyYIHhGuH4MZv6-cFq02X2PUtABW7Ts8X_wVYCsN7mlXduWDO1yTYZCGfJzeztsVnIu3Cxpv791hiKKRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23216" target="_blank">📅 22:33 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23215">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-JZJxxn8kzSDQMftIxotYeHEZ-EsDFs5fTPJg-vXI6Va6WafjqnoY0sGNxia039AnGcJsOEPONpoyY0zT505hcz21HnDIWmHe8BPdKeMX5M40OYmtu8giYWsBIoEdcOBUCS5hX4EffhXSlXZ_jXFAAHhxN17UviysP9TIfweqbjBsg2uUQXZTsG6Q6-I_dGPr6Mhb4VpSpDSoKowi5avcyIAGRDo6IIy6lDbi-FCQ21x7D-b5CO-09wdUtzpX9htU-RBxbMujmZIoALwYr5FZqUTRL-Y0oGWv9GfcBYwm9Lvw8I61MrnFlB88OFFF5lYd3YL33dcdmhIONp2PiTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
#فوری؛‌ خوزه‌فلیکس‌دیاز: برناردو سیلوا ستاره 31 ساله تیم ملی پرتغال برای عقد قراردادی 3 ساله با تیم رئال مادرید با پرز به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23215" target="_blank">📅 22:11 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23214">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=FHAaPWL1d3X-_H-y6d_ekxj1slbkqbUQUhMvRbh0tFPqqWIHcUDM5T5_2cf5SvKkZr9yLEq4sQkdtiTtnte5UAbN_TdKqICC496UxiNMqcTOg0e3p47auiZTsBcE7NlJHnhsfKTeia1oBwUCk5vnp05M8Y-g8NzkPXdGCCzYnhoAdE0fG1wex3-xDZnobwzwzTnBUyeJIipn_81EJu6B61cWPjtdG7-zXj9KVm5vKx2KBi7vMJNLVXoHcyD4YqWCbB-GFOQ9CVP-Z6hJNd2tfCum5yxULBTu8dCbfrHY3xP40x1pOPJkJFhuTh2hoWqAvl896iDpwtd176xBtWEKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a0329db5.mp4?token=FHAaPWL1d3X-_H-y6d_ekxj1slbkqbUQUhMvRbh0tFPqqWIHcUDM5T5_2cf5SvKkZr9yLEq4sQkdtiTtnte5UAbN_TdKqICC496UxiNMqcTOg0e3p47auiZTsBcE7NlJHnhsfKTeia1oBwUCk5vnp05M8Y-g8NzkPXdGCCzYnhoAdE0fG1wex3-xDZnobwzwzTnBUyeJIipn_81EJu6B61cWPjtdG7-zXj9KVm5vKx2KBi7vMJNLVXoHcyD4YqWCbB-GFOQ9CVP-Z6hJNd2tfCum5yxULBTu8dCbfrHY3xP40x1pOPJkJFhuTh2hoWqAvl896iDpwtd176xBtWEKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جواد نکونام در برنامه زنده خطاب به عادل: پائولو دیبالا لامصب چقدر خوشکلهه این پسر
🗿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23214" target="_blank">📅 22:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23213">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
ویدیوکامل‌اجرای‌امشب شکیرا خواننده کلمبیایی معروف در مراسم افتتاحیه جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23213" target="_blank">📅 21:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23212">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCm45RBB2iHKOLYofk2YklnMGRuJuevBoi3TUfYM_garDoEIrPRbF_lMWDNiJ8JUmZ3lZ3FGrpDuIf5cwKV1M9Ow9JlInbzf9ps1JNU5D45NwhYxzt3R_C2xDUFH5gsdt4T-hRPI77EIBliEila6hn56ZSE1MesM1PaEwCYmmWFBnomiRJae0UB8XZKJ-hETHDrwjKL4xPtTnZSyp4GNS5Z9DodBC4jOjFPNRNskaAT0ElAHiiqkHsdMx2X6mLFT1g1imgJMKmm46FY5Bz3EzQ-LF5uO6BxJ-MZeQlT6fytAjqMM5xF4PgT_b1UHKO3YwZSJ3bOUh7HzeG_cJRgfNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
🇦🇷
صحبت‌های جالب پائولو دیبالا ستاره تیم ملی آرژانتین در گفتگو با عادل؛ برگای جواد نکونام و کاوه رضایی از این مهمون برنامه عادل ریخت قشنگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23212" target="_blank">📅 21:47 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23211">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLwu43oJg0qPhdCoNrF-RMjlKQNfCKJazonE2hat-OP7FKPd79J_TgrK6OQXyCvSbVOE8xrdw_zM3nHXfeF8GlkPSuEGa10HGtRjsV3uNEGH_exrUq9nW8w394G0545jKfEkgiJjYLqRmSHW_XBBsHprTLlB4RJOBytbxHQ5kHyXEDDaKOarCyy_IzMe2bSuR1VCbgQkmrRD8Ptq-SxG0KOOsp-dnYJvygsyuJiYF8eScBJUfhfTltz8p8LuzeRQon7Pb9z_WmcoK5kInjjq-FlQeNHqPGTiNRsOOzfxflGG-Np3SNgS2d98h2LPfBYBt3-W_5WP1s4_Z-aMYe6glQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛ باشگاه رئال‌مادرید تا ساعات آینده خبر عقد قرارداد سه ساله با ژوزه مورینیو رو منتشر خواهد کرد و رسما اعلام خواهدکرد که این سرمربی پرتغالی بار دیگر به جمع کهکشانی ها پیوسته است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23211" target="_blank">📅 21:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23210">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgojsZOYNoiDd001uVZuvpJHfkFTBlwFBgFki9aJIkaDuuW38RtxazC4jbrHfgHurDV307xgBJEVAWwxDsGqZShVK9savtYzkKVsw2RrV1IZnchxslr9Jp6BXf1gpmn-QUPBS-uJMbHDA0gNcd26KQkwbTKJF2E_4VywuqrZdi_njAi3fXt6BmiyqdBQoG2i_m6IcJCSM2rM3HTwT-paujYKOZ_ob2M4phCFHu3SnV5KbBHy3R0EBxshIHVVsvO45NShpaWOXHvHiaYfQCRNt0cG-AfmX1cjNthgpj2kl8bxwXP-ecuNc3KUhsuFNl8-SbeydXgCgYv3vi7vF_nbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حدادی مدیرعامل پرسپولیس امروز به ایجنت علی‌علیپور اعلام‌کرده‌درصورتیکه‌رقم قراردادش رو باتوجه بشرایط باشگاه کاهش دهد و قراردادش رو تمدید کنه فصل‌آینده کاپیتان‌اول‌این‌تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23210" target="_blank">📅 21:39 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23209">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=rSGxkodhytAVt2WrVzuP624eifmXYQYqrwnt-oYPEi4BlHU3Lm0SdtW6n_OJCn1jIBw4_JZ8wKx4yYSnZRmlOatYZSfNx1rSbZAVJNlt_P4CmCtT4HnRQ4_wErwLKaPQrQMDlmim4Ddy0TAuy42YwdoVDEsCRTIxaIX9gZUqq_dnPPHb_VLzjxQGqdPr4cMdOmKwFJLKPea-Sr8lqSrcho85uzpZSek1E4weMbHhgG8skNILRYVR1nLHmlwK-wsInXZ6vGUF-OWgrHHn0d6FAHnOoi7sKuWuKHLY3L_jZYfUwliEa8zH8LkNou9B3gahn1jq-HKy5jIYBCRzGwefxQbyudM11AQ5rHtoYycTW0ZejLeHU_3jqP7ph_Ry_NTQh-GPDm3sSBWzmsXDhr-DXzuKbcKWViKV9jfaweu4LkTAUHihQVOyOGXE3hgRUYGvSGYkw2bfNFZIxA4NY5rOC7zHHBfdbywKZlrTXP8dsL7Ne3HdR3HEVSbStE8hvJsZ3QsthGRPnZd_TAY8bXFvfkWhE4ii8umeDDtaaSObkw2wovt-9IkmTdK77vpMq39HMd6aas-XE6XOhS7qAhkW3ZXxMip-srAJYfE_CTufrYaW5AbK4w7yYv7WuGULrU81_-Pb5dummBwoB-uBGvWneaBIf3SRatVHFm5v-RRk0GE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0af0ad9722.mp4?token=rSGxkodhytAVt2WrVzuP624eifmXYQYqrwnt-oYPEi4BlHU3Lm0SdtW6n_OJCn1jIBw4_JZ8wKx4yYSnZRmlOatYZSfNx1rSbZAVJNlt_P4CmCtT4HnRQ4_wErwLKaPQrQMDlmim4Ddy0TAuy42YwdoVDEsCRTIxaIX9gZUqq_dnPPHb_VLzjxQGqdPr4cMdOmKwFJLKPea-Sr8lqSrcho85uzpZSek1E4weMbHhgG8skNILRYVR1nLHmlwK-wsInXZ6vGUF-OWgrHHn0d6FAHnOoi7sKuWuKHLY3L_jZYfUwliEa8zH8LkNou9B3gahn1jq-HKy5jIYBCRzGwefxQbyudM11AQ5rHtoYycTW0ZejLeHU_3jqP7ph_Ry_NTQh-GPDm3sSBWzmsXDhr-DXzuKbcKWViKV9jfaweu4LkTAUHihQVOyOGXE3hgRUYGvSGYkw2bfNFZIxA4NY5rOC7zHHBfdbywKZlrTXP8dsL7Ne3HdR3HEVSbStE8hvJsZ3QsthGRPnZd_TAY8bXFvfkWhE4ii8umeDDtaaSObkw2wovt-9IkmTdK77vpMq39HMd6aas-XE6XOhS7qAhkW3ZXxMip-srAJYfE_CTufrYaW5AbK4w7yYv7WuGULrU81_-Pb5dummBwoB-uBGvWneaBIf3SRatVHFm5v-RRk0GE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/23209" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23208">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/709c123d60.mp4?token=ongir_udcb1HOn6oVeWerWvX75dV4xab4F_hV0K4OQEckzx3DFU8Bt2Z_tSY9lZFDj2vUTyIngDY7AFkqDCf_Mt-DHK6Oo2RRz7fFNl8XTLyW2TbTdECXfhRVk79uJWHNAXrv3dJPUx3V5tSNhrNzCKuuCFvP_HJi3FpvwXnkWkdH9NUua5SqsmVmIaZHc-8HRqxVefjtzrdJfbAlvLmhLx05fhdXX7RYU0h5gw5P7Llon-FaI__xyIu6Y_1TT6pWUd1e_p1Y7pLRJnZUGMFVWkOqy-3U3CuihAHNhTgyMCvUa5ofDdfrtntROT1YtKe2ujSLdMdti12D7f-fmO-fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/709c123d60.mp4?token=ongir_udcb1HOn6oVeWerWvX75dV4xab4F_hV0K4OQEckzx3DFU8Bt2Z_tSY9lZFDj2vUTyIngDY7AFkqDCf_Mt-DHK6Oo2RRz7fFNl8XTLyW2TbTdECXfhRVk79uJWHNAXrv3dJPUx3V5tSNhrNzCKuuCFvP_HJi3FpvwXnkWkdH9NUua5SqsmVmIaZHc-8HRqxVefjtzrdJfbAlvLmhLx05fhdXX7RYU0h5gw5P7Llon-FaI__xyIu6Y_1TT6pWUd1e_p1Y7pLRJnZUGMFVWkOqy-3U3CuihAHNhTgyMCvUa5ofDdfrtntROT1YtKe2ujSLdMdti12D7f-fmO-fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل فردوسی پور تو ویژه برنامه امشب پائولو دیبالا ستاره سابق‌تیم‌ملی آرژانتین و سابق یوونتوس رو بالا اورده و داره باهاش حرف میزنه؛ صداوسیما هم داره با خداداد عزیزی حرفای کارشناسانه میزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23208" target="_blank">📅 21:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG0su7L_aNyMGptQG7PG4uTjvnmY16cv3sAvV6bctDOuuW-6RiNfuFwo_MvMOHbbbeCr3nUo7U1t8B9Sq0fhGOJY_D4AKhFIwC3R7nSGjjYojYxfF5LlPMJ8QE35tUso6FYIqxreAtqqGzLwqFHUwAt3_3XRlCnMcxU_HkxFUQKzcQnRsSaxpATQWG1wwio65FDPvq89FH9O0d9WwqHQz6JE-tQDrn8lbflJCkdqyrMjobxcMYyRBJYb2h-B2yq-C33CAf5-was7Xr7AqI6w6qXiDrp7kRowm4Vmrxo6dbT_MYR6tJ7kGxQtMrt7bIA72_a2A3TPsptBLbd0p_FccA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینم‌یه‌لیست‌دیگه ازشبکه‌های رایگان ماهواره که قراره جام جهانی رو به بهترین شکل پوشش بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/23206" target="_blank">📅 21:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVE3mrSrnpD5omPugUmnpDWFlKxzSXckfWp7qJjrywdtVXSwrjGsncJAWLlr8XTub_k6U8Ydlu0LmocZLNp-3U7ttfZxNHfQBp_VyRL3ctonViHXblPBtZ3Gdk_wYhDAaTmTu5gy2f8KT6RxEOVvTzbk1CM8guGoAhyr3sFZe9mN2JE83enlxsuZswOCeC76fq4wUaUcsyVOrdR8M5yxi0EkKE_ghtdjjajx2hS5j4aOugd1eZWp6EaCozVtEVQWITf0WsRSvjrsgWRm6RWXYBWbyQgFZbLnujxKf2fV2ax1cHQ9vQlL3KNHyAE31ijTcuiieEwK5uoH7-Zr0vaiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو: باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23205" target="_blank">📅 21:13 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-avjjvNlLN3Uo3UPwg0nxLTmnkfBOu3eA5242YT7NISJ4B6DIbaSP66E4e3Su7PPchRxZoO-1PRiyH7TIBks0oVGz6V8L3YPP9WlMHhN6hEdM7hKiC4rLDi2m3Tf-n0pu5THXY932PdCpgf2yxQX3StJcCGfuy7M3ZDitiyT8haRXbU3cka0rYafcbPxRAdEANLxp9UADqsdFA9FsW1C5rFjCS7yWqly7Gm4dTRPXvu7xMdQilgWNICHRR7vkNuaI8cm9EhgsX4NTP-t0rtSLo5ujHqWaCN8Af0_iuOpQrMUxrFGgINYIrtjQKxWlWiChA30lKrHdaC_xva3Mv1Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌فعلی‌آبی‌پوشان موافقت خود را با پذیزفتن دستیاری دراگان اسکوچیچ درصورت عقد قرارداد با استقلال به علی تاجرنیا اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23204" target="_blank">📅 21:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bor99wSTDIp_XaJVmjUQQp3maWOFvFVYJSqoJesNxi8g2GnVXXwZIUhyjzKB7k2EgGWQkNCEde2skyJ06D3E1_fx5gcXCM3EPDLGs1s7_pMx3AXvgccKoz8Q8IYoQvGY36APDsvlYNSBX01XbBcQIlXWAQWsIfe3JTlwmKvgDgHXqSIojpMAdeFLlOSlOA1qbGF2JgzblIIdYT0QO84vz7EkrTO-5ElYEHJZ93NJX2d-n8Sf7P9h6pcm9IrgZ1EL-By4C_XKXmQtJyEuw3-dO06h416XlqukmTf9cyRzx4T_re5FRK_XoA7Cb4j9sgakjytpVpQ9jgRormKinx6sWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
حالا دوستانیکه‌ماهواره‌ندارند میتونن اپلیکیشن My Satellite Aand Tv رو ازپلی‌استور نصب‌کنن و مراسم افتتاحیه جام جهانی رو بدون‌سانسور و با کیفیت بالا از طریق تلفن همراشون مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/23203" target="_blank">📅 20:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6U5zs6jetmqTaTlu4w4JbuVHVwCc3dJYCKN5tTLNy8dbvWprs4gw-yoQKrv0TBElPlbgSn2EGQbq-HtBeZVEcgW01lDJ9UVCaawkNeGHRH-evmgguHdrpN042YUpu9JnZn1yFcp7dCVsfYx6DZhRWTGP0fEUILo2KbpeRHzi7W8KO2ygpv2BjIpxyx_cQRbQiQ2iDkCMcvClZe8I9yYTc-MUNTP72GVlPQmRBAgZvpo3hlfOnOKh_myhJoy96gP-DqM1JKDD6Y3hdOkgzd1KKNWcwyRAzGhjkiD9M56vnzt6guni_uhbNfI_pXPbjqT0fRWAjxfTTa5J_4gWGZDdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
مدیر برنامه‌های نیکو پاز: ما با باشگاه رئال مادرید بر سر تمام بندها به توافق کامل رسیده‌ایم و نیکو درپایان فصل‌جاری به این تیم بازخواهد گشت. منچسترسیتی، چلسی، اینترمیلان به دنبال جذب او بودند اما نیکو علاقه داشت به رئال مادرید برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23202" target="_blank">📅 20:25 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEs1MOHcXT_KTu2bd3iXd-DHyNWXDe-QJNBoFKvDCHQalROFUJvdLeA9qi5WG62Hpbdl1ydQJxUPcOYuuZQB6AifmYsHp2Jqdy3Yw8qRJ4KGTkLwingXbqGaBQf9rOeNzsZvAQN2srS15MqKfztoZJLICvQ_rjcR6sJI_hQcPhBEQXgPBVGCkVWBbmCqUZi2ktajx_bT0HgZ4h4hrEM3T1C-jbbrOPLgtRir5ByYyupelZwF-Jf8V3dgtcPZdhKE4n30NS93306X2s-rFjcBZUrLhxEDo7sZRF5jn5qvIDGPkBAhE1BZzJucNklQQK5kYJ1Ak2gS1Iw60jgNhRisvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇵🇹
با اعلام رسمی فابریزیو رومانو:
باشگاه رئال مادرید مذاکرات‌جدی‌خود رابرای جذب برناردو سیلوا  کاپیتان دوم تیم ملی پرتغال آغاز کرده و به احتمال زیاد این انتقال بزودی رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23201" target="_blank">📅 20:20 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLnfScL2YDwJMLgowcbQ1K07iIAh4i5-fUzTP94C6Yc-DtqZz3LTbTriFFxku2SFkVe36GILC_kW9gQilAmzR_IG7lvDNAvMPjiK_9AOMODIApvHAQhqhrrRFNTSILuV3iFWNDvxuxnerBo2WMH5jI_xBVM40Yf_DHbHsvNZqIKVd17iBElJ15zKmZDfbdy6iIDQZ_NAeQezItmZ755D8FOKRmeupC_d1-PJhK36C05iCQ_mtSR4sxYapHhuqid40PF3APu1szF5thxrXUYcmtwHDF0no327wou0CUKhsPCUr1S68dwiuo9A_hKG9BbE8eZ4A9Q_18d9937ukmqvkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رفقا از طریق‌کانالای‌بالامیتونید مراسم افتتاحیه جام جهانی رو بدون سانسور ببینید. خودمونم سعی میکنیم در پایان مراسم ویدیو کاملش رو در کانال قراربدیم برای دوستانیکه نتونستن مشاهده کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23200" target="_blank">📅 20:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeNobIeoJCYmuIYB7T1a3Cg-IVop0UDmPzqnDQghvLqpzaLo2Y4G516mxUQ0XIBCJo5ORc4yP33d5JZ_TrJMD0-XaQTCJME0YRjRXrNubi7Cava35ldK6mW92j9ZvqndfVKFsdCGIeHk3EQ4BJWfNvNYUf29D8XD1-EWkdGM7TvIawsyvzEdS_s2vkP5O9JNcw-4zKPqf_oeZBYzrOSH3T9hakEsnUPoMq7aaw515U979RXJH458HXlm7ONqbGJ1kgCE4z8Ec9b31hpMGtKGr2RRegzLnn6kyGDLd8w6QGE_-xj3urwml4S_ha5bGUuFC2EmI2zHUak3r7XF91TGsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان: بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23199" target="_blank">📅 19:57 · 21 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
