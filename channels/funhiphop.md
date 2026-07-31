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
<img src="https://cdn4.telesco.pe/file/FwMbNfb0YRK5Kkw3STtzOUI1UI0qPGYSPc0YFo35a4GV0d15W1TRHU3huPKx5RS6TOW8j79_nvfmcIOr1kOHY2FOfgZEGm3esyOn3OgH784j3D5C8g_VgtrELnOwkzQPjqIoJAEBsWFUzIlfjiJGR-zka4bYktWgq_CPDiOQG9ZBWXOhFMeWnaaq64zbvwSTjLEz965Vfh87TUjQnrDMpnGhfGp3abHnfKzQQVyU3s4GJQBZEUHrUC_cJaE1xlzF-ubH9Qgaebgo4b15clP5D06b49dEn2wujftBBhscnljvA_b1OEv4RDYM_20icnU38osiYlB1aXPAWeUXDTlsKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8_Wan5D_ReetptSN6YKibw22z0RXSnL4WnQulzksTTMd90jUzHvjvKnz9aUW32tjBfBHJEh9jLdbx6eEFttUfG_kiMM6_0YE97aB5iDLTExYPCgZgoPy_K3ZnygrFY7xycHOdTuXxwzpRWmmOB7OFecgK6Exsdcyn05YLLvGF-VuLHhcQGr2R4deGFsXw_QbR5YiaEPpX3PLYestOelfzEBtVyagOP9WdbjQUotX6Ng5KRJOkerGdATNnU9KGXJeY3KJozJvezZ7SoLA2F6LW44BajoYvi9OFvJwjv0QCErwCP5f1T2t6k0RuJxFx00CG5qBe9bBK7v5FSVafoREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFUWObYEUHFWvNL0BQz3IzvBAWupgaHdKBCRXZP_gqwdol61FgUJCWAEnpwNozsJ1ngzhvObCFg2dl6n_7OH_ZV_vLAXA2JjyNM57NPy_uGRIzub7juvAu99SGVw3tR9oUcATjHdAjUDB6mnZqVZvwdc6YP5H9hPEmUjHDA6olWmdzECjpyTPTcqk4KzuNuOpfe4vpZGPyVKvNS46RhM2moG1iZ1wqKfEO4nw1um1k17S3h4rkEy4jGPFvDXyPel6aCMKj2vWuUrJ8BOH9SrjkhfPmrkn3Z0IPJpvUkip2s1I5bRC7F2j3yRVz8cy5NJ1AZ8xT7FRL5QQ1VxrVnCXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvsmp8kDBD0I93RurBaukJP-ujodWR3LLl4IIXZJpuffZJU3bi8qU59RUsVjB6mwhf0dHm7Za5Ai4KyZ4H0sX-WIy6S2yN3ppV2gKMVdTcaJzYFYBb0QfpymG5t0NcVX-JpnEH_sM47yu6yW5B5DS1SEekSi6IvmY618RMEqQuEbhV03DfFLbPR4RqOiP0kccxaG4Y5iysqNHmTHjg4Pytyl3etBzSzG0jmeh08urUnBeBLGTWgJ9joPYwFDJh1ymocRXq0BRi5VSzC6YU3ewJhKS4ZXWwEVqzrYe6DXT330a007Lrz7I1rDgFBVo6LlKVU7a-z3GTKpGM1SDWEVrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ao4B4vB_SDqNGVshHEsqmJXdvapmKf_XPY65D1k8O_Msc1fqmPPsqNdSOuUVHtXqIY5jEH7AP24awiJJORZLj5jiHzjR7iCs3hpBhnCdojm2VI3j4redWGpzIQdMS1bsTY05uWM6e6npSeN9mYJg3NizyRo9VX0Yf_5Xgt-bsvtKiXnKSs1P7aqPhmK7DPHPuarhoNo_jIs94AJWPizDujjeWOtA9o7_1IcCHgUA4govbLjEiimpoytgYtAYN_FIzlXSBmtBrqCdAbvQm_s1g__dfEYJoDxG9oHVsvM0AwsJ2kwRV1anh2FtZeOcIKQnG7giAB1tE16oDxs7lidIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RHlTF1B3fdTf9tvFINdU4armj9prefj1YF03aent8tHB_oZcV9ZeZWu-y9cRXmYhYVOPduZaIB2H0vDKq6Nna2rXlyBrOOK78PblsBP3Hee7ATGdTEifXlqn5K4L5AQtK_idR_h1HW0E59Df46bgE0wPsOIOLELSjUzS_6cmFD1dXpDfFK-_d217To-9Jgvs4aEMpE7ikIIAaF0P5FVxBeWbBCVsdgsOp9jhka1ATrgdDS6OoddXQGGBn57NnjrpTLFTVAmfIqcQa6oR5qYSuKm4vOYC68zI7dMPOLyvcFvsHoI1eP09yBsPZdRtYsrxK0qW40TRL_vc7hyOtW0f8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GMtu6cFMLGPOVOOizdvJBofZDikZUU2XViDaWbg5fOGYUtVK760BEs3m15Gf25esuVfpWOD855DL0BZ-RUxXwtO-gt-eY3RdNq1m8ZmkEB7FODGdUfqo3ndLcKb1o2YvJfPsaY76yUkOedbksVmHXn4jmC7qMfTAh2dTblrHBFHG6gBakwe2MvuomfGBSDracO8eBVPpETG2E80gg3Ig9GBhKhvEY_yTiNLE_41q2AyjtEfarNDVARf_xUaB5S5V2-1WrqNZNX5pr7rcXURFaGwqUzdXF9KoXr-DQYgtkXEbFmhu7zyBw_-aKTRoRTG1phsWc9stqPfQBk0aLcimhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMJvIefQcaSLs3zV_drbpssAdjJpzXtm1fDmqtEf6kyQgmKtON6XK7MKu3h--h4nTxQ1pP1hxi4CRQ4848HFdwVmdRHY1yvCAaTq02NyLRsgPfMt-Vp7o_YL6h9g97oMhJc3enQyWgl-4V_SUpHlF2xUxeguVwS4jMbtRHrEp6fdmz7No1Nq5EMN5Vqy1zqJnhohD0-q7we1jBx_uBLDX7dlk5B7EcBbptRjAjofQh0HTEs_-I_Zfpfknnq0VBRt5-NaI4Z9IgVT0OOBXLbzoimZKujNwafSPRkuUgVHVYvmV5SXurJVO8ciQT2o2rGSKAo3IgZlY9VZ0Pf60M8eOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7FNfH6fw7y3Oem-H9V6El7FfNwMN_NoTMW6i_FDRl70WS-_KyKQqKOKIqEgdip7M9POTy41kTBUIkT1YGrMfjPbKn11gyn8KcGlGX2nuHyBKlAmxDJeQ7jjakcSXif9IKFab5OXvLnauiElBYUcowsQWGTVime6v3UdzNPR-gQe27bA4ybcz-GYzuPr7IuCEVqexiKvtbB2tvBT0vXqI5m4K07G7o6sB2cyiTxoe3v7Aq0_46CLfFUvzhnTmKotqFDguvnbzfZlxlOv7HOk4WUxcTJXYylnz7Mt3WNxcwexpXItl1ZtRw511IbbSrpx43s2yJBk_YEF_iz5MXCgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEIy4qIUlJstEQ-m2UbW7CKohM4OSH9SJBIU4J751Rv8OClvDxX-xR4NBBLQxu3kSz2DyVQ-2g_jrGM58L88Y6GEXryM_TRB1-3QzrAhkmqF5zXT7SYyxBMzDKUmF7eMmcww7zhP2z9NVzuTnlM7fkfnhtLueuOQeh9hU-LnRbP0NNLvqldokDYUNgeqs2lbOQcT13rUnhNjxrkXqZDohFVwAjVuv-AISQR7z7pWicQ9fernMDAKb2wZqcYWtDPGnNPpHGnRrn529yi14Ar4TiofZgz1OCTANwN4D7xTLPpL_u8qUhOTv4Fx_sDA1xQOChSQzMQNajQ-sBz8knF8Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBd9Jg4WzQrt47_qFxTrwBunhGfgG1USCNZE6bwhMWxxd8puk_KCBAh-b6VdZ7kL3OOta5welb9JJoLUUfM5wEqHFJpyFwo4-7n1ox0n11l6N9UDRBE8NLFvFpA4mr9leWYbDtO9MBxfbJFnoMwJlzBf8w3cUYTQp7fyuJB30ewrpVUVfNijzoQli0NbtGletcwqKfXwcJBzYu2Qptxfgerv7sdz6-g2k8vNuDLues5FkUwLBGfF8OEH4VHeA1voYo_7UGaHVNOm_mY9rQJt-PSaKOZK3rY9d-mUC1FAHd7qCYz5M1ZLLkM33N7UPERIUQOFqIL95qTrmXR90CKwBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMRSjBm8C4O34uq8DYzBKndV3LU9Zp_zuYTCNUHj8FrtW7EAma4jB4VjFjkXlmGRFgBuHZ4vR4Qrr3PHOhdCyFKcgFKJn0H25arj2Ax3ypj3gCldw5oYi6c5AZZukQDShIkKw3M0QpGoxhNxrod3l7KJSmFPuky8lZ332UbWoE2qJIig2lh1T_gKysN18qXcvG7Y_DNK6nQFctomCAXKKVqU9AdQKa-P6_Mp0i14lfjHBtGI2DxlvDHxxhXl8WvOgp7YRz-gmGmxmn0Otrbsb_Bv8hJLM0aAT8W5FDYmrpuvgN3-G5iTY4euF4T0po3mP-HiB4igzwTTCh6WgXtbRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bs2sN9GkFekfSMmkBuYa0sOKgEEIvGWwtxRrlsx2rHK-e-6vHDyfJDFvtOB7ndLoAKRlE2Wsh3yqxRrzNQ-dimWkoAzye__JvYjLhyZKBFqOFCkzowsNl-0bod-_ClVjWDtCIoXNKq4VDwhc1ltI4EEWYyDP_-9aQTMfT1D50JJ6Z4XBYCF3CGdVjPYjpE7WNvTq5TwKSnKg5gVQ6w2PLv5Fgu_EU9WbfDMhY84-PmfcCaDC0IrZhtUdN-p95SolEIQJrYwroQGDTYnSYzfmy6S1nziIzhz4cjTZ0Dr4onNsTGcr1qoYyhOU53IxVrhMZmati-vyORwOdp7vNzcMow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=o9gOj2eLRvhsR7qmxJ3xfZQcYchlEDXVu6XAm-tToRp0fPCJP46qfgBXdtpOnfQAdCpmM4ux8qF_jCzzT2wi8LDu64u9ssfrTzl7Aq_uqmpkFlRK-BBp_B7U76sMAHduJbo4gpPsx4SN4ueb869vFEqdjcB4x2WSsYkuYpYyznAK1uBIBcqL3TZerZp6kAMp532MD-ua6fGBLF3M7CjQ_9maVz7hX1OKHHGpkvapAMMPASkfo7SOyy_ign3i9Dud9UOdIeJBnDHqJsOtbB7wcZbDw6kl--nW7hR02XAwQVacIQndL7UzPT0aIuvlDFbbvnCt5yJSHp2nkYohbW9mJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4FYUBirA2gUbb1su0pI5-FVSnN-klhg4yxr6Nwxm5dm1tbw_O7McDCgqn3_iMyHNxhhqBNOX17LY2XoCEYfWg6sqRfcxqaLmH9HD7T_IF2O7sTKvqNl8wqjPy-fR2ipeONhFLuEaVZ7HEDvHJ0_7Q6-WguozNGYF8B_4GEVqBzEiteufnAEgmwWWMMUiXDX1L2UUfsVkG2cSO-yrcgzA_iBwvNPNWKZ0gOBxSCWCTysnmzSojarFE8TlBWQ6PuvDeRjCYIXrn_BzG5tgke2fbcEzP6ePZpFloPvO3bppH8kwiKqt3w9IySMgJWRvZDAVQs1-fo27FpQq90tdymZRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=M--dgxEGlEzWSHaVlx3MQNyctmrmsHl41JFEO0b0cLcqPuOCgTaGaAfZIAibyK2sA6JL53RgJPNMkZA5pwSpeTHhiieNMVoWXFrNFeBP6EWS7X80fCbfUfN_L_fP7pYOm7KJnuyqjqGmeP8Z1Y7IgDn-ls6XqIVLrtU6FmjCHXv5iMghMQqSiywz9bCjdWgPsH3JygxGaHorBFB09032yRWN-rAOtLmGrlFUzaZsiQoxOLBFYcP7peDFEFB1BZ41x0xx83DQ42ua6nHyfjv4s_8B3TuxzX9lXdb-DVdMZ8Qtb6Oc-2w8_MHgsjYHB33jCYtbopPG8FqWp8z8D-TPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=M--dgxEGlEzWSHaVlx3MQNyctmrmsHl41JFEO0b0cLcqPuOCgTaGaAfZIAibyK2sA6JL53RgJPNMkZA5pwSpeTHhiieNMVoWXFrNFeBP6EWS7X80fCbfUfN_L_fP7pYOm7KJnuyqjqGmeP8Z1Y7IgDn-ls6XqIVLrtU6FmjCHXv5iMghMQqSiywz9bCjdWgPsH3JygxGaHorBFB09032yRWN-rAOtLmGrlFUzaZsiQoxOLBFYcP7peDFEFB1BZ41x0xx83DQ42ua6nHyfjv4s_8B3TuxzX9lXdb-DVdMZ8Qtb6Oc-2w8_MHgsjYHB33jCYtbopPG8FqWp8z8D-TPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=egd6A86aBC_8zsX8RRRca_nDY-tAlcmoD0NF1QV0emwkLAMB9b_q4V4Dey3-1jW5mTCek0EtDSgc9txbw29FiSnBGxgq36FaUNQ6FNS63C6IE_bL__Zt2HEKJdEcUiX9y6hsPWwmSEf5Q0337mre48y6U_VEjOIxhUOeSDcZhIplS5RjgXOlRne4b3rWvIWHqRAp4tZOW1ksYYOW-8-ssdvM7tl20TtunXihvTKBcrGgNXudYDEsi45pyseeEDTZ1KPl2A7IoITw8IyYuBNxGkfVk9jtSnVPwh1I4fSVCJPxRsnbcIK5xkKFHfu7CgzAW_lnWYUUV3l7p5fikA77E4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=egd6A86aBC_8zsX8RRRca_nDY-tAlcmoD0NF1QV0emwkLAMB9b_q4V4Dey3-1jW5mTCek0EtDSgc9txbw29FiSnBGxgq36FaUNQ6FNS63C6IE_bL__Zt2HEKJdEcUiX9y6hsPWwmSEf5Q0337mre48y6U_VEjOIxhUOeSDcZhIplS5RjgXOlRne4b3rWvIWHqRAp4tZOW1ksYYOW-8-ssdvM7tl20TtunXihvTKBcrGgNXudYDEsi45pyseeEDTZ1KPl2A7IoITw8IyYuBNxGkfVk9jtSnVPwh1I4fSVCJPxRsnbcIK5xkKFHfu7CgzAW_lnWYUUV3l7p5fikA77E4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdjWKsabt1Q9xMujxe2Tsq9ckhfFeH50zsDeelvHOeNm9TPs6Shc7he6maqv_YrtkIS44Y4jgQmaCD_Z7dag-c5J0hhjtC6EcHW_TvCmk6aDUG2oUMPpDK_eg0aT3TJj2F4PqROHlUBipJWY6cjGlFvih-B97y5O0A1xdh8QCXPmrD9aSpIWvebPxYup1IHktW26EtGtFxc3Ac8abQbEBc8eQV-wy4CMjReHFli8Ht1OLGknn9MYEMCdTWXYua_2__8oJQJDqMn96VwAaZJ78XfbXcSakIZjOnqNsuqxrUbSR0XH96jeTen9FrIEdh-RbY66tZ5zuB0xa0jQFr2cgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTqP-ljZFj6zrnWTl-PUEV-NkSSz2v5vyPXEVVUNCfAKSvvzq2aKZxZhJhR1Tmz06eCJGamnQb-yc9eWMUXSnMien5G7oZ1fOskvwUxfl9JribTzpNrr9lChoT_24sDBoPahB_XHEj_xybjem0yCIwl2XWWmXueUXI6JK8_HyiWLlvswCwd5XnLy4wAvhJnTIAQ8B_pKwf2A5j-ojNrZoY4HwVSV6uK03kL657EhJib3F03oIXkqhZvEOcnScrSki-AKA_senGYK50ZnDYlu0z4pMbbCr_NOtu013ZEJoVkGzvZ8ku1tK1QSnPHWFAyJNWw49zChKhtbR8N0ppd0Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=Ac3cJD1xL_t0gf7AAd53aJq3RKRQTkoI-CJxyGr86df57xsmppINqnxkODO1w0zJGmS7NW9JYain3vnO--wXBxngScWFnCdWP6UqqTOT2SX--dfKZ9Nh4IaMNgniSG2mh3dlj6csnlA6--L3fQlzncfXz2mQi4PfQ5Bfu8ktIj4Kx7LFG4ASbWUcJ0q7Tff8q4iR1lA29GpWg5CLbqAmAuQFCTeoODaigUoAJw5uRbr5H1L4Ai_GFJGeG2thG6tAlOuuZSjdoNK6Q78p83QjMHmTqhHlIRyQSNxIJRplP0A2aQPJoqawr7TwcY7lICAjXDnkbL9PAVw60CSJu3SRx7TX9QKuw8tKyW0lpmM1wsspEGYDtO0F76JNsfidRR-lQRRvtQc4xhHsp5UquHRKr1JbqBzN9ZAsskgdHPeqcvQtDdVVYBr10p0kmd8xx22u-mZckU4vt6DMFeP2z_9UxNX1gl4RMpY6roBCJL_7_X28Ml4xQa5ZB9NRQhXPy5jYlfTf1hsTVXC6i_rYMCQYdc89lbQKIxOh_0V_g07DJ2aijWJzsGwG_RKlSZ0fzmerT_jlYl2fTSfWeCPmQwZWVqWq3Vlw-742H0FzIPrmUhD8kNwCkc5YQAlMDSBPYWD7crWXKAaECGwxFQ1XQDdytL5towPlMXpwSL7iam5emwo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=Ac3cJD1xL_t0gf7AAd53aJq3RKRQTkoI-CJxyGr86df57xsmppINqnxkODO1w0zJGmS7NW9JYain3vnO--wXBxngScWFnCdWP6UqqTOT2SX--dfKZ9Nh4IaMNgniSG2mh3dlj6csnlA6--L3fQlzncfXz2mQi4PfQ5Bfu8ktIj4Kx7LFG4ASbWUcJ0q7Tff8q4iR1lA29GpWg5CLbqAmAuQFCTeoODaigUoAJw5uRbr5H1L4Ai_GFJGeG2thG6tAlOuuZSjdoNK6Q78p83QjMHmTqhHlIRyQSNxIJRplP0A2aQPJoqawr7TwcY7lICAjXDnkbL9PAVw60CSJu3SRx7TX9QKuw8tKyW0lpmM1wsspEGYDtO0F76JNsfidRR-lQRRvtQc4xhHsp5UquHRKr1JbqBzN9ZAsskgdHPeqcvQtDdVVYBr10p0kmd8xx22u-mZckU4vt6DMFeP2z_9UxNX1gl4RMpY6roBCJL_7_X28Ml4xQa5ZB9NRQhXPy5jYlfTf1hsTVXC6i_rYMCQYdc89lbQKIxOh_0V_g07DJ2aijWJzsGwG_RKlSZ0fzmerT_jlYl2fTSfWeCPmQwZWVqWq3Vlw-742H0FzIPrmUhD8kNwCkc5YQAlMDSBPYWD7crWXKAaECGwxFQ1XQDdytL5towPlMXpwSL7iam5emwo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/P8nXIeUPYk6Jcb1IiYe0S7Q9s3FNlltzpNiy_BekrN3gJqxV81yJ5PWCu0IfvMYfodz6hw5FPZhqQ8C2AaKP9B5HhJpNfiopDYUVMrbhJA6vWfXI865_bGXTOeh39iRHdzdfh8-wxcVit_mqy8rfNXBKsn7tfnpOEzUyo7vhHrKvj8Ra0eoZg2tplpOXdOUhuhc5kDaXrEahsZp4JaWqLoo-uDgAC5PqeZQYOc4XKBbn6FnDzyYutbNH5iScZ2w6YaXVJfdR5uqweqEk6XYakDawCB5XFdAz1h8ucK5SPTXLRNVaaoTO72ophDG3ag6H7XBWOxhahuZiCklCHzvF6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1MwxW4v-8GpxOeHcY362kwrjFosY6PndwQQjrzYk4SQmK0_l8OT01yPECDC5WIPLrC2ElS6ij6hoqhxo3gNs4QonrqHJLFCen8rhGx-r3RGgvVNesLmPO3kaqjg1ExQkPv1Jtyjib-9KqsLdWI6U5vN0Ru35995IEZog_ReMCQhdo4iCsTIh-Ayrl95Vs-VD2rx9tXXEdxx8fvyvoARHxGLp9UGYyq7ZWNCYsiKBMELaxiJPvvPX192yalWPv-WXZ_TT4jr6rY5HXtLiXlRQT2-lXEPtAAjHByLEB2wV6nLsvCMOXSMkCiJguRcuJBaDXWIFd6qcnBhuQi-LIBYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a72oMhMwPzzFgu08PMkj3ghockrdv7E8ceibWW5dJbsbjZD5eansAEZufYdW_H3cLdm6tDHxSFKXGEu2ciwjzrDQ7wz8rNG0uFTkcCjOp4_vd9RPmWqdeS8ve08XD_lM6NFxRwveNaIaBVPKIhzfNmQScyQQIkwV_mnAcAbBgNl1NZp_hx9SA7oeOGUsoGBmdmgQ0Yl0-Q4EINEZPhI1jfFO42_q080iRT4u6wTdmNZHpnn5A6yNsN0V-FUSbmMiRaiPaOxLVcBYTgOctI1mc6o1ZAzC8mELqGEcBgHI4s2Rc4YYP9fSaQvNh23Vs5ctH_61geDEdWEjwNY4SvGenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRj7a6Gsvn-iBvuNxrqQ-l0oL0-bEYcLTSQ3CWWVaiY-qrmJnUwa0b-ayY4aB_Z5Sv2DBnnaKxBS3iUXCbg87eX2ik681XLuIajZealdnuKEGT8Tx05J5E7jkSN4FmXwfjyEKWV7y7Q_z-Af6UnycDW2njklk9g8cKMRJLC_oYWvVbXgrbHPwRAanC8Y3ho_j9RWZmnlTdCiBFSf_G9Zr7kzD00SYVrLFwo_94WN-3UeYij7ydJTUGVqgaNPJzLHW6G633fiAN_TBL3Lj_5XP_GgMEPRr0pW-rUaQctmqChaBuGnD1nMYGfbIT2FyllANshQ4DCVR4rU3VozzBDijA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxkRFqVDwV9PkXjMtBCw_jXhjsPOKk4rh3CabcJmXnCovWvpxg4e4VaeRiASrErfQUbIU0pniu2HR7INSjOZbrcWa22aq-BGfKLPsf5bmZfhI3vmMWd62ZPS0zHini23R-G7iQmbghQ_por8UWTz8t6c2YeMp7pJa1ogibXvmLR8xHpYmD3eNkXd9B03ar8MfqXMBxEkHjSV7IuM1AKP514FLuXIhsNp75Jp893dilMq33EQS6bkCvf--EAPPJ4HnOJBpTAoHsOhyP5b3es2Jdb-vWkeeX7sU_fSh2mg35GdaL1A7XA_Sb4jDfn7wWXgQ-UZwYy5Z_I4Orm0J7betQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K5Me755hXo3-8_ybi8s19PvyqjmAUKfnkwVjLu9z45dUIFRlknuUml8NWZCbPqYn6Sn5Y8HFsvaxZwiodqUkzAqWgiGgOOG1eMb_CuoG6cKglywpGA_D66FEYy3NpFhbqsavrczwXBujc3jW144-jHYNAptAtRS2-buPF53XtY2eL8lCGcdVT50FfJZkC_M26guev0HtlocCPXPx7b_Sv4kmzOSMvs3lrvZq3DkEE22gH3VcGthBXPNXbmQFjMURXJHQ5IWn_m6a4E44ISOZ_K-pc1F0JJ-wH1mjG5dUF3gvfh8fOUdcW_qRqZHlKYL59184oue_SwXTGflo_gCLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81544">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD8KIWYHa0kCWtdA973oH6FUi7lkp_pAVZiSDti3-AsdHkxx-AdUGKK0CqeF4hvfYrNR44pjDxbSvXrtwKzjzjXJk6EbcpuUyANc5_kjfNcI6_AKx93h1oycAae0byEvs0ymZKsDq-xygVeYGg-uN0ne-X6KC4BDpzhahRB8ViR2Lpt6ELvLPLPe-CnPKIuZ_IywZ0WkO99DKvzJLALp5Ksn6YweiO3yI591YMloWOblLOpboVN6bihObGEY8e5G47rfQbbjUWRwAbK1DrGiAXy5jYHVA30xTtf_URl9nrVUXsrCOAiWwNJL6iD1mQe2F9AtYVH8q_wmESSnOVGRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
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
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81544" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgkqiS3jb6hxvoIeaWp0CgnaJrBlFZ4--iX03k2pFzXhvyqk6krjwz_RfmNw8nyaXDlDgYhUkov3D3ritaG04SvEDKbe7N-fXfEhMMRTsdrqnLHjdlaHtcmYI6870a0nq4nWx2ZmhZIp2OF5_AxE2A0rlwPWBpMToyPJ7xiqmsxZzNKTHoXrhpyfEtobvNwcCyE9pMsgweXO6u2tFUzOLtOULRA9nxAkZxXk-Op7G5n1MTrRFsjUDxIHue8ZZeufnS9A3DfCVIoizoMvAVb6f7HOHF3nML5ry_XWoBsxm0bzyak9F5iVLEDmUlYyxPjCVn_RadTAi8CxNaGB7FUvzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81542">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDLSnqRE8x3mBWs9f6ULbB6oBdIBc7aI3Q4yT2BijBJvT5tNSuTpCPwDaaJayTMiKjIIFTRg1xaHn7Ux0HnUi6DhK5ie_08gWx5IYcehfPZ9QKMXw8_HqKMfqVU9HXnORv622vTAoGHRpPrDTkg9mg8M6WPHcagLxoEG6xedu9wIhlb0hM4vmh3hQLlnz1-8nNpDqLoWshJBU32SPiRfao8HaKVMpXKdikZMFRYjrUK8lo6kP55P-ZuXKATb0YYy8QJLoyNYn0uuyjYAaiWSPkpSrdWT8FXNnAFPWmkCoU5zC1ZwJb03iPWhL2SPRHuT6wuPM396peGjOQRHJO3MXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گلشیفته چقد ترسناک شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81542" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81541">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLdKTKymIZTVj5RT_Slmlbtr5qQM1SH_6sCezHtprleiaghbHUbDKX4VxT9SgxAL58Tyz7qkw2u9uhEnmDibqPDQRyT3TKE4uqPH3soUCCX6A_8aPUHlOnL5eh3f_pLkWVXyloRRld9Sto4HPlDZp2S3RfkflF9dCGrmhU20X3emPEsBhqEaI99AZv-MMJNJfZkBvNX77jzVPRqBokNJaQ8l4ep4VQBs57OAWY_6Eg6ihoO4x1nXxWI0xg6G-wEgwycrq4W8_ynvZkOPYg5j2MmB8705BH0jZeFcPE4BECm4M-0eKQdRNwu7popXfrq3odXAG2tPSus0yYJEcONojw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم اعدام بنیامین نقدی، جوون 26 ساله و از معترضین دی ماه صادر شد.‌
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81541" target="_blank">📅 16:56 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81540">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCyFOZ7jgzVJ0c4-dMqmuoO-v9YPrncutc8VjVlHJXppqYh29ENIxSP5gh3df7yYxlsJDKAL0txlj8wjG0xTE0G6t0zLMAzvk2-UD-AAWKyaGORgps1Nb7YuDymhFoj7rDc4_TVoalYboteI0k11j5Z3SXfK6tvDd7yt4-Q3Wqbj3YqwWcVDy0WnFQWLWrAtgk3_NFEPC_6Ws5FCEz1a9NH6szG-IxTfttJ96MeZAGRbYUgyi8oAR7-P3cnAVF8A_UgsBFWhuGxgXEBVWSdcnGKmgwLQpvnfKna7tC4EN95jMUI2yQuDqLDk3rzM1JWPYou2pBVpHoU8G-QLLXuroA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج افشین فدا بلاگر مازنی بخاطر استوری که برای سه جاوید نام اعدام شده تو اصفهان گذاشته بود بسته شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81540" target="_blank">📅 16:44 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81539">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">از نیرو های مسلح درخواست دارم کره‌ی زمین رو منهدم کنن دیگه زندگی کافیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81539" target="_blank">📅 16:30 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81537">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4w3JqWySjLujjm5N7sSTFKJ2hXGw4Vmo3J9DXRqMHmV9c6ejbUgxj7fTbFbBktZN4vrvuLVgUyqmtWuNoJD-bWO-xsW4xDDvBXLIFeTwuL4Jd3I--jtX6KVs4CP4Zw09_gTcwvGNRdps-no8XNizl6TsGE76K85iezBLUhvZ3XrGOXTmuVtUnutHPyFbbyE-n8dr2Fpv9s18q8HIfiBGGNfb3VzGLAPDowxsiLVQze3VBdH5ezoZF3zgCm35ogQlkDHwIBV1S3QP3cbRXeMToRIO2R18Pi9lnpwNCeAijc2joQM5dB4M06zlBkn7aey9jHA2971tOngSfxjSHpIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفرود سواری در کشور ممنوع شد
تصویرم از وضعیت یه پیج آفرود که این تصمیم دولت رو به تمسخر گرفته بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81537" target="_blank">📅 16:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81536">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اشکال نداره چین میاد بهترشو میسازه
🔴
چین گزارش‌های منتشرشده درباره برنامه‌ پکن برای تجهیز ایران به سامانه‌های پدافند هوایی را رد کرد و نادرست دانست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81536" target="_blank">📅 15:47 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81535">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCwX-dkyABdBf0E7UvS8dP3R7dsz4fCgLJMNFIX8f-SgNpnsFABmJbPi9zkGa_XM3ddAVJ5_MsLW1PE1w-6aP9LeP_FnMo4UOzaS4ZOOwK1qc6waIgWffuNFfoQv3efs4GN3Me7UutWYZxojwnysx9a9AUAOk8gFfjt_SBZR_RRuOdHOPjZeZeDjo3fSZNqrkstdCJElPyIo5ZJTqdKbjYM1y-vUhEsHKMBl0gk-9eFHKkEnEV8D8EIUY9hys43F_bLHbszrkrbKPn6MXAvgYTydKBqfuUjOq3vFGm7XdyN4AELyb6QWGL37f7P70Z1fY8BGSdfbjELq6i9V7aHcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده اید؟
صداوسیما: امروز صبح در پاسخ به حملات آمریکا به ایران، 6 تا جنگنده F-35 رو زدیم 3 تاشون کامل منهدم شدن، 3 تاشون هم خسارت دیدن چند تا از خلبانان جنگنده هم کشته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81535" target="_blank">📅 14:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81534">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J29kHK3qwdDcDe-jcZi5XzLKlrFNcRSjSBA49b2Q_G9cQLflzbpIvLk6Fe4pkiSPT1szS3XTmPl0W6kOmKH36Zby8XNsRdcMI2bjSbeFnE8-GDrZ_GzixppKM2Za4A1vmrlRm4M7dovz8qPiDkOaPrpe6fHSRFBbuaH18NvOW1mkg20B1I0ce_b9CzjSeJRJhdOh899CZPbhP30u_QVTYt4x8piyeEV6J_reiYiNohnkbumcOYlIQY0iUWCxfIupN74EEnLDYObOJLNA5OVrvN3y7WJJwIG0m47x_nf6AWpaBvzprZon7xCaB50noqxFEV0vqubz2RxbYpm5ANGKqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دایرکت یه وکیل دادگستری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81534" target="_blank">📅 14:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81533">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=DipWZcYPtbVvmeu2tmSQFXYpUMuHWDpOw2GuT6xZxrcjECB1kI0fQ6caoZHPEgeZNckktQxDOgAgqvy0wBFRGbAb_vXW2W-fF7QTCis6Wm9myemWh-mQLNSsiY0UNK2NTfyoAz8Rym7-NsGXoimu4IuUaGLZ4A71eocklyJX22C4VxiKtZTGcPk2UDD7i8Tr-g5V_gSvEwnVp7TLcCN0qjesHn_2lZC2er2AnV6AYG1n_8HoO--FlcRVgsTJYdb2b5L1iB6de5ZWWfNzp2Vr61xiXy1pWVD2yuki0pjxJ3VVIAvYabOq0PBLOy8UqXyliTY4H3XNnIH5F1AxbHM1gBjwbSzrHt3denv89fNZE5XXkqOU0Ho280PM4MMbSj6ZkciW2H22kTrMKxCjE7IXAz3dV-9-1EJjqSyhjXJGGhU1o1Rt1wZepwYHU5CEsFNZJyYaZbzob5fbO7EhnGtmvaYjNUZS70GD5ZXckRFf6PgBxB7J_qzBmZTewBw5EcIIO7pVod2N9gaN9am6F_gMZop-lMZfEbgV5JCSJPg195y8yNUozFUT2Y046ba7em2XfybO71qCepXuQm9o965FS2bbMIiT7BSaSkE70c-Fn2707nlcmIX0B8ET-ST9IUKkqgH8RKCL17cbzu8yYBd_GqO15hQngIoezTR1Kg5L-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/533f3ca2cf.mp4?token=DipWZcYPtbVvmeu2tmSQFXYpUMuHWDpOw2GuT6xZxrcjECB1kI0fQ6caoZHPEgeZNckktQxDOgAgqvy0wBFRGbAb_vXW2W-fF7QTCis6Wm9myemWh-mQLNSsiY0UNK2NTfyoAz8Rym7-NsGXoimu4IuUaGLZ4A71eocklyJX22C4VxiKtZTGcPk2UDD7i8Tr-g5V_gSvEwnVp7TLcCN0qjesHn_2lZC2er2AnV6AYG1n_8HoO--FlcRVgsTJYdb2b5L1iB6de5ZWWfNzp2Vr61xiXy1pWVD2yuki0pjxJ3VVIAvYabOq0PBLOy8UqXyliTY4H3XNnIH5F1AxbHM1gBjwbSzrHt3denv89fNZE5XXkqOU0Ho280PM4MMbSj6ZkciW2H22kTrMKxCjE7IXAz3dV-9-1EJjqSyhjXJGGhU1o1Rt1wZepwYHU5CEsFNZJyYaZbzob5fbO7EhnGtmvaYjNUZS70GD5ZXckRFf6PgBxB7J_qzBmZTewBw5EcIIO7pVod2N9gaN9am6F_gMZop-lMZfEbgV5JCSJPg195y8yNUozFUT2Y046ba7em2XfybO71qCepXuQm9o965FS2bbMIiT7BSaSkE70c-Fn2707nlcmIX0B8ET-ST9IUKkqgH8RKCL17cbzu8yYBd_GqO15hQngIoezTR1Kg5L-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛ بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده! مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81533" target="_blank">📅 12:55 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81532">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTH7zMkOvHwY1HBg-0fZ66ScLdXjpRdqaFNNSAXP_q0A5LHUdv5VWCJ_WZHkr0CMWYZ-s82areGbU6FJziW9wg9dib4ny4nECvF5zwOSVO-IjFYWNysiB0-6gjZ4o8zAdr26YYz4OrGwH5IKcoSjaz3f3P_C1q5nAe6pZRejzTZfM35kUsEZW94GBkNCHt4u8k9Q2kNilX4uxlF2lL4OKNfx3BNbkObnwgO2EXhAoQ7mActuiKvIebXMNc8DaijVsJujJclfD6ifQwWlcOrGYVcRkbr98KVotwZ2QZwe76wACzzpdkj7F6NzdiqiQl69OZO9TuXgQFNgo36yXs0svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
دیشب مامورها ردِ نوید زیادخان، همون فردی که خانم‌ها رو‌ تو لایو کتک میزد رو تو خیابون خرمشهرِ تهران زدن؛
بعد که رفتن دستگیرش کنن، این مادرقحبه با قمه به سمت پلیس‌ها هم حمله کرده!
مامورها هم اول شلیک هوایی کردن ولی دیدن تاثیری نداره؛ به پای چپ ، پای راست و دست چپ نوید زیادخان شلیک کردن و این گراز بالاخره زمین‌گیر شد.
این مادرقحبهِ 36 ساله، قبلا به اتهامِ "ایجاد مزاحمت، دعوا و درگیری، سرقت، ضرب و جرح، مزاحمت از طریق فضای مجازی و تهدید به قتل" زندانی شده بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81532" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81531">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0oxBAqU5Rg9If0WffBl1s6Xg8TyiK6PGEc4hXQzvoV9npZ4hsx86qUf5KSae5YuXGUc1pv5DM3UcToxVd_HiJm1-6_F3GAOAVuSEDRUhlwQOhfIGlZa3E4F5ZONR7iQCYGDzJvelD-bP9axG3vaz0u52ChNff1AHCWkcDnoOAP5ELKkmgYT_HgobMDtqj5ImIjwV4fFzlvzontB3QvtINXEoakzAy6fzcWenxpfXp9JfGIbEzvnu35NliX-ecEImTCFHjtbNsnqlz2H2OyRoeSOicFMPhFA2i0mD_IyCSR9WLcF0p1c_6zWU0qPWHdsFtaXul4uAX9oQpyxzMdCRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بنفیکا
🇵🇹
-
🇨🇭
سنت گالن
🏆
مرحله مقدماتی لیگ اروپا‌
🇪🇺
‌
🕔
پنجشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه استادیو دا لوز
🎲
با بیش از ۳۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بنفیکا در ۵ بازی اخیر خود مساوی نکرده است.
✅
سنت گالن در ۷ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳.۶ گل در هر بازی بوده است.
‌‏
⚽️
نکاتی در مورد بازی‌های رودررو:
در دیدار رفت، نماینده سوئیس موفق شد با نتیجه دو بر یک بنفیکا پرتغال را شکست دهد.
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
r8
💻
@BetForward</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81531" target="_blank">📅 12:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81529">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یک منبع آمریکایی به شبکه "i24NEWS" گفت:
حمله شب گذشته گسترده بود و تأثیر قابل توجهی داشت. این حمله تقریباً دو برابر قوی‌تر و گسترده‌تر از عملیات‌های قبلی بود.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81529" target="_blank">📅 10:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81528">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81528" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81527">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81527" target="_blank">📅 10:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81526">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خلسه از زنش نیلو جدا شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81526" target="_blank">📅 10:15 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81525">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbFDddpG3qdYoUbdjG2SGfYE3JJAmKLYMXskOdeMvKXH0eafxM7A1Nr67YulKy7e8ahS5Ye6H3sHHRsBOMJ3-pdEAZy7afN0H_7GQWxIpD3upYehO5LI-0nQK7XJlEGJmjbKuqaN_MOwF39RoVWCsVm_lLhupRnQ3NrW75_1iDrYv4PK9kr8VGwNqW8r1pX9P2-ZuU0uly5T2A5QgUD4Fo9L0STjwwuNaIw0QSuuYuGrja-tLZ5Jmt78oeglNiqL9qwEOJnlVbLvzKWm4fU3J43VcZ5g6feGC-MI3iqLlRcfnQyJOtE1J7GSLl_i6jTcBAYOJQuzBMqyWsa7JEqXBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کیرم تو این اکسپلورم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81525" target="_blank">📅 08:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81524">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینکه شب گذشته آمریکا مسکونی زده احتمال داره یه پیامی باشه برای ایران واسه جنگ های بعدی که احتمال داره رخ بده، که امیدوارم کصشر باشه و این برداشت صحت نداشته باشه. (اگرم انقدر اورانگوتانید که فکر میکنید آمریکا کصدسته و مختصات اشتباه به بمب و موشک داده و صرفا اسرائیل نقطه زنه نظر ندید کلا)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81524" target="_blank">📅 08:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81523">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ciWYnekREVS1s_t7ArTYTzk96AHfIstLKnnSBH6e3bV4klqfn1YmgBms2KPhD9oU2Jv_K83Tr1G00XKMmoyN5zBxheDiLIZrLd04AH8CljCFSaaSivK4cRI6Z4gVyQO_8GDSuySpWwXQIqY_2146XqYCU1dA61pd_Slgbv64_cHEjFsDn7eQKpu-8CQ1Z9qfvQ6VTndKh6D_QC4UbPSw-8xjeCt_7wkWpk0b_NEGf3MpgqZsv5_iy9lO8vUW414owpby70nJWHoOKXkncpQnn4HV2VpPI3iRbomN6CaJWX2Vv60xcy9j_qukw4GGzN6k8xmm3Vtu1ZXNhoYem_Tekw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b757b219d.mp4?token=ciWYnekREVS1s_t7ArTYTzk96AHfIstLKnnSBH6e3bV4klqfn1YmgBms2KPhD9oU2Jv_K83Tr1G00XKMmoyN5zBxheDiLIZrLd04AH8CljCFSaaSivK4cRI6Z4gVyQO_8GDSuySpWwXQIqY_2146XqYCU1dA61pd_Slgbv64_cHEjFsDn7eQKpu-8CQ1Z9qfvQ6VTndKh6D_QC4UbPSw-8xjeCt_7wkWpk0b_NEGf3MpgqZsv5_iy9lO8vUW414owpby70nJWHoOKXkncpQnn4HV2VpPI3iRbomN6CaJWX2Vv60xcy9j_qukw4GGzN6k8xmm3Vtu1ZXNhoYem_Tekw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متاسفانه شب گذشته هم:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81523" target="_blank">📅 06:51 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81522">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نتانیاهو:
نمیدونم دیپلماسی چقدر ممکنه اتفاق بیفته، اما نسبت به شیوه رفتار ایران بدبین هستم.
اونا همیشه دروغ میگن، همیشه تقلب میکنن و همیشه برای خریدن زمان بازی میکنن.
آیا ممکنه این رفتار با اعمال فشار کافی، از جمله فشار دیپلماتیک و اقتصادی، تغییر کنه؟ باید این رو امتحان کرد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81522" target="_blank">📅 06:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81521">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تسنیم:
برق برخی نقاط اهواز قطع شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81521" target="_blank">📅 05:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81519">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجار های پی در پی قشم و بوشهر و بندرعباس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81519" target="_blank">📅 03:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81518">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بوشهر آبادان کیش
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81518" target="_blank">📅 03:42 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81516">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=NS3N-jhVT0qC0QCfdbpuDPAT2x2l9m_QjP9l_HB3DfyUk6LUJtO05YFFFtVaxRNETV9zyrfSBiP1w1uaGTetGX_WJVbCxuO5gSEp-Q--jg26nJ7eUiQC3k1yzQZq3cauy-JBx56T0ZrxBOqk3Qk41Nu3IMDrHPgQSdeTelv2hFpv65UQjsCAFke95zGzZqK0Pxo9Oy_oGQDArCAKIiZCf_YVhwRZlPGisT_eXb9PeW60cCEH2KPE15bYjndrt_Vcluvbco3awxv7tgIJhjD6YmedRY4cd6plNXDHZsdX3grg-fBuairO-McJIXsBQ3SEdhCoNJJL8CmYnFymU7fmrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a76739cd9.mp4?token=NS3N-jhVT0qC0QCfdbpuDPAT2x2l9m_QjP9l_HB3DfyUk6LUJtO05YFFFtVaxRNETV9zyrfSBiP1w1uaGTetGX_WJVbCxuO5gSEp-Q--jg26nJ7eUiQC3k1yzQZq3cauy-JBx56T0ZrxBOqk3Qk41Nu3IMDrHPgQSdeTelv2hFpv65UQjsCAFke95zGzZqK0Pxo9Oy_oGQDArCAKIiZCf_YVhwRZlPGisT_eXb9PeW60cCEH2KPE15bYjndrt_Vcluvbco3awxv7tgIJhjD6YmedRY4cd6plNXDHZsdX3grg-fBuairO-McJIXsBQ3SEdhCoNJJL8CmYnFymU7fmrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان مراسم اکبر عبدی، عادل فردوسی‌پور در کنار عباس صالحی وزیر فرهنگ و ارشاد جمهوری اسلامی نشسته بود میخواست دستشو ببوسه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81516" target="_blank">📅 03:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81515">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81515" target="_blank">📅 02:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81514">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Game started</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81514" target="_blank">📅 02:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81513">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">بابا کصخل بمب افکن نیست که رادار خاموش کنه، سوخت رسانه</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81513" target="_blank">📅 02:29 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81512">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">بخواد بزنه ردیاب سوخت رسانا رو روشن میزاره که مهدی ادمین فان هیپ هاپ بفهمه؟</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81512" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81511">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حاج زدن حاج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81511" target="_blank">📅 02:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTufdYDLtZM3fT92AIpIgwgy7Sk3VSwVpabkz4C5qC6_VId0WZUJS5w8k_abb9vjII6-B3VaDH6-U_1Z6bI8wJWoL4lYGvW8IM_UEIadQLj2lK6Ygxlqq19-TgABVIC6vGNqQGhUCc3s-pisDWKqyrzcgm1CotJlSBSFiUad4dKqAYgcPhvPDFB0BORT46e7EcVkOOVzR-fl4CYKPFGfLBy-GTJ-UPd6xHuwZr8VhF3shL46DSzpvFKrQlF1hn4MXzOQQ3fUypMlgsNFT_26BkzgU9g30ehxhneEqEZGbw8XpyS9xuqrPd11ipN5hAw0Zpcl99zzOyWItExg8tjDNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KqQk10Mr20QkWJjbwf-dQSla1KULktzuiKIivtt-siNFRpWawg69ByfkDAr811K-8Unt0g4ptTLaWtNgDX5SEbA0EdXvWwGdQUESgkRqp-bVUIpQsjO1j_WeOBguU7KRoCAZlmQ7Qp0_1HTubfA4EX-5eUnQ8UXE93rtMqjojd1efbGHnDy-Be2H_ObjQbbajYp5ZLTBO1nQVAYo049NxQO5biqt4QbH3QbL_ulXNQv_QJJzzgXwiqr65nzfcOsBKKUHHtumN54TSy6PCDNMEFcUx1YJsgMKvac39zFLYBo8mxU1hyO7gDiPtvtf6UNcamnT4dzun-TJZOMtkPqWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOUnB-7kG1uZSoB23TZHL6tS8lvTKhnDsiXjj-JpY_Wd1NFR4kGOtOYXEWm7ShCHKIFpnAYpXOxC2ktHRpO53k7k5CcZ-uNP4AOvogh5e7TvuoaQSKqbrT8tSG9y0_nmmvWW_3_ctfTn63ii4YpPHPQJ9G-Fb-BBCNCac4mthT68sZJZ9AwNZcgtUfblvgdu9BNVXwJ4O8KAWcg6WM4x0WxsdSm5AW3VuqqWAPErYsEB4evowvfZ4Arxx5ov5tHvmpghMtJSF3BF1LY736IpFR3dAMbd8RbPcecbABN0cFsNO9n2gA01MRae1gBpNVxSi824l59wOrP8Y3DMQqeeCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyzujJzMYgbJhwJOa4IoGWJ1Y-rg7iaZGjhjz5sY3q2WNH_LmnZynPmXzC55OaOrOm8-kWC2g3EefvZGTCdytm0-ZinaBXwHgxjCrGDWCTcpYd8K2qwv3hMNVRkakjsieoAd9WkEuiOFVcfCISrTSFtNQq4r_HW_LTF__RHHJUoygQxLW-I8bZZh4RvZjQGR71EnmU2N4Raz2VBDmWd5N2l0kUEyf3lvnmyTtfBbevhdbm97_xFYr_xhhXjhDmibcjLHVlhX7uEF0yGsb0nCY2fhpuF_7OOjiMt30-IQvmelYxQqsN5J5bY9y78R1b9Ve_L0R-2yZzbWf-adkhzjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNbEj0yPIfLFiWi_BLqfhXAsUT6Bo7VyrJ63-mzHKLo7QXUlglqMB4bjh_P2uLWEwzbmF9RSHpzgE_VsFfqutBcqZ6mPij0mL8QR8amC5sWUWf5VlTsZ1kujQUvlKUKTZ0_kE7gKRUCH_HAlbajcYBKMhOYDbgXuYarwi7r0ym4nxGxVVB9vv-EAan1yo3N1yTAu7sLJul3uhg7hBUAEzQeThDOuxCMpnGLlFzYL70OgLN8mbj_oBuAg3TIrQDv6GTiphy9lpUBfraat5erK0qr5KKmf0DrHixV3LgpwoNh_UqXWjskPhagUWysl6ycz-eU-6LemXsnoaac83t0HQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTC8VLjlHkaJNY34qk8LyCTeVKc8dMJ-hniTomoRroh50lbesZ8i40tpNHlPum1iXz1klgOKFhch53UWAiqQTgD1877zaal0iZf7m5fhZaKdg-0vgew3rsf_q0EG7DrsaDiYiEyaNF4F5-TzF3pTLZi4reQueasgfdyywNAochrJTlDk1kHMuyrt1D4CHQPT-NPwS1Up-ATxyn33eRY6heVBvyOKtk_C00P1wFW14u_LExdgnqougSOfhBVb_H8teyJLU5KZYq9Zpv9I-dTnVNV8YJvdUuw3zRPEuRrdNllLuaoQ6GjqzIYtmFNhTq3oMVcy0_4OsO5nskcJpN0Ztw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbANZsCO0vouHEnm_Kb9OaWFipT4gf_-UylRpdAwaOkiIDlBdxxoMA0VqP2JMQsbsWcYu2dlvGpDRGf8JQGVPTfVWIsNBPlwbK6BP_ef5HhVt6ItTHC2f7Q9-Fcope4MKv611qFAa0An_PcrIr-taxEb-NQYMtEda7EI0OEoVHNCbI4i43qaYi257nXmPJ_4jC5vC5yJugJVs5XRjgUOXMo98yCRNQ8DR9S_UxgoIyMaIdz1pueQYf_45yhFKQaES5E6_GxZ-uqDPw68iXrro9NQ1E16DD7vciZriny74QFV9ZtdYUKX7aIFFz441LO6el6BYyZyNxxJyfaVhj_OUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hsz4-02NF-4MFUQHeffTynKprJ8CRg5M3GD6vOt1YgMgaQe-vnfO3QXD1zt_wZBN-td0ieT46d0XUpd21-mVpreQTIYU82koHziZAt0nbH2bxHx93p3UlCOC0ssssK8AZZgYH0aB6i7Y6CDw98Uw9kSFEsdBDT3II1V8c2KkFC0kEcoBQUBNwYNn5bsEU86elpgXdFVgtd6egG34X3rvj5gWGKu1ufR_M1ab-SV7U99cA12oBlJgqC_BzPV0xwHiW0VnM0anvOuBAzGgmGbUGT0s15lb9gZvCWE1X14vVO7CXFVFzyhtDzTFz76YOGC70dt1yR6utHDNhDLD3wt31A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAj2j6oQ8k4vl9zZiW3rxEUv3f0H9272sJJTM-Dy4COrg3NepF-me9rNLuXyc568PxqkM8wJWUC62ajVbbFsOtvn-F4Qb_8lYNzXt22yf1C7RRG7p38CXHML2vdATo2e4pR0axrFmX4C0Nq0c0EjEDpQ0jbz4RIcmXDb3EQuiQ0qANJjqAInvzF7AHlXCmy2qzcRurROk9l5InxFgoGjievxgzHM3BZWCHzke-1c4Jrwoc-cK0XyjzIgPRK1HbxGhUxXd8rXpnJzNqR-OotXeEn7YkbqYfRIU4QAsevDP-2RF3G8nAwp-dM7O-tFe0yR1cOaT7_FtzC3QiXqZR_seg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAtMktrPsFrATAiLnVkHaBlzq3E12XSvbFFoAIX5q_X6uWYI3iIOC_7lFtRyfcPAXoFo-bsu9HajwmGX4RkKQ-q2fRIw52aN6mTjKBNFSvyz_qNPFQlraCr-mLSlb0trRoZzlEvsNEGUUIus2mJKQ4qt8NLF-orcWuWBs5W49W-gAk6qCxW9Pt7ZDPw_OSCYglJ41UxDoXkW64Ne8uEi9mcw0dXNKkz9eU4zlW6S3CvbQrt0RPc-dh-Wc0EMBXCwj6H_VZHTgbQdVUI1_lKWGUCM6rfqEcti2UH9qb18ekPGlFmG2WLddrICAO7AfvyYjmaS3Ftb435aAxcaSKHyjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8xRUHsWCeJoE9PQyFrcZXZDlRhhApQktd7yGBfwK7UhDxRJs061mi7l144cQ2_o-Y1fLElXUZ0CWEFA5rwLDyxpOFDaPSOatUvX5hXawscwYf_2XSUffYIzIsjYmPgXTIP3Qr2Q2hIDOV-6xpbN-XAzoCSe3A2EU0gSkm_v3WNvQ3hkuzUSCoNei3O9bigcSIcEuFnd3WEnCQRIzvO3x2z7IdmcHVuXOGzrtpA9eW3RjYCvMF5pwDS8GKp6bqRLW2meZdPPdfCFrfg7e1B3a5heDPA4maH-BdC8lpKbzO8sPQGPAiJP6Ij6K4qCJGjuiaNPaq5izznWo3a0vJBGhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjaPfPLu4vh6RBlzW0xbHyzt4QlmU26OsvDhzSAGnl99EK4_PCw4xvpIlDtMd_S8kgbTmyelaDUUESYJgqGeut68CQ5hkldCK9Jg6QclXygHHAB8smG2y_HctMj8X_SdPp7sByuq952c4IPQqvGqFZrpZcpBVdt3NnEaqC7RogGXrN1XS7cOkdOtCioJwUPKb5oUIWsMs9WvTkg4B0UMaAqcyLIGw98RKaY6Dhhb56jnsBhOeSrSlgKisq-PZoOhpeF2rEG3PISS5JIEfRs9uzUwXiDzvkPOcGQmrFZ6Pug4t82kzodUBUPvozn6X0Jijhg6uDoO-r_k3ScygJZ98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rI4dHPRVJUb3-o6tqPuEle77nrZHsJA_e0ARG5TgvH2MNbY69RHfrSu-OwhiY5W0Sh4U_wDxaL6IHa8ZkqIgknphPZYLeHJkrhpo36HxvHtTFQYlP-pLEM_ELcHZ28FXfFmyMFP4nlV1ln2JEGn1sB65nT4BfNRuAyE_5i5bebd0_wDH3DZjFxlEHZm8l7X7GV-KujbiOAs3WlMi7dUyLOpmMo8_dhwl6YbDD9DabI-Ysb8M5c224yqRtpFZFQutS9X8JdS7_qps41NUmwpjme2hbQK6AgcMpVMM9MCflua-5TwOIj-4Mv_VqBIXa7yqna3MgtVEtBZZDwEjQvyQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vEJh7JB9oItXrbQKj2_Y8s5EVusgUuphVmk3rlXwP5pez3PGOU0ytVuSgxUsUV9ShjzVukYVW_4IIKrsJA_PamZ6t2fDf-RpvTwOmOrEoFtBfqP6vu-rYUS4rCl0CP769RsnIlfoR4G_gUYCQE5mk8q3assWvxunki9Drsz7nGXQmNHRthuS_mS1ue8y_GWUKPS8RNeaLF5FCCxMgpChvsihUrLCM0dcNQM4VVSIoKGGgDzQhSBBk2P14esPXv2xDyDVtb1GuFP0RwCj4W5r1frkYuhY8DX7EEbm2QcRg_56SgMPfZjXYEAHQ_3uJjK2eNv0FpY4i4y91uMPTDOr6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k31huC38WwVd2xQJ_4c_UAaKDsVhr16F1O8rWFhOHvBGa6uD9_rgVOWbej81krHAoBTfLmwkmescssfKeW4Uma0BNHqF-tAue1Im7rAJfYQOhqRq9zb6xfzG7QJSChUMWwSi5d_y0tG9pKEvPGh_wHUFwlnwEzrPyJB5vHzlUEwzylkpIP45xy9U_gefaliwPQPFsfJYXHLQ640g_JSK8M2f1pBKwJS5Mz1ulvo8hoJJbzxY3b6QDUEKL3sBjTSWWY51DRb5viCoRjkiB70j-FhJJ2xyqgiv2V1V8bvljGWoymK27AcrTyxJxnB8Y6X6nUSGrHoNf5XBLo9bLi_OtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P2jesNRbnt8gLYtNs-ohslkCVNcHW5cqrG7wTwcYlK7WPC-m5k5tJs_XC1_w8_gPeU-kHTZQ2zjhj2ezRMVfPPjbG6qLHvBurojShhbnn6mSiTyaY2dAXXTjyIuLhL2yR08ZTeraKRUACJgRQzYOmRNBQxma4JD8hPQ2VK3kQFpEWv-lHN7SbyfASA30tNkMB7Oh87rUGFLYDPI-wzpOXWpob2SmlAYCQz2jHTitnNC33xoRuwA5I4n53mtI81EU0U0mYmB3P-DGqJdl-l4iz9E0B44Kro5OAjYm_Az8e98ygwU8l4qJvZTHxPOWjB_1nJyO8jZ7SuPJ_OiofklxnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/irJ5K5bqUn9PWWXfA_CDtO7ts4Qgq8eL32gdxRvzmtoxrm1Ew0TvRa4juqhMppvCpOxTWNxI891SuI2Y38foYOJIhY5qu5ao5vlUeE1S7bX9oNQZ28TtVpZD14-lqLbEKrtRs4O7AT664ejJc0d7NsQOsI7pmosI9JzQiB_S8n2cv591ywZhI0JFr_ek8gIv1Dxi57sUF9cM74ydv8RglYU1d62XFSy1tMoc8fMgvVUCeN4s2ot_6d-LUp0PWEJRHzsdj-le3lZhJEUkgqSyR1a0vVSJ0DLN73tlF__77I9-iQsULhNPLEixJaHktwHDeH_7h0c8jVWzBvqsgDc4Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
