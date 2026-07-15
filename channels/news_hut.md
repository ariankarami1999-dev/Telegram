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
<img src="https://cdn4.telesco.pe/file/HgkoQVlOyRrj3YgIiyBX1ZAUiF7bDbh8fW_S10At4-li5FNmrdSrgjlxr9heuiCmt-RiJmfAEuC_mJRkXfnL4sIDto9Gpak3xlBY9TSSDwv2vFO9dAKabIqBNsQAr3j7kp5jv_bsWQ3celvuTdUIWti89KTIj4G7HyCTPh21Jx4OP-TLyVWgqoZbfDTXuKUFDVJNCzT_GbA4m9eWSeL7WAxsMoFNw9sEcdYgTwgoZd6UETxmPp2uvIQxBJy5pbw8NjFUJudH_jiwBOdDhfEeHBWMPSWxlkoRHmXWLhrBTPncWLb-TF5dJXjKw2JTDA051HhJJh8RNNGz0eKidst52g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 172K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 14:36:21</div>
<hr>

<div class="tg-post" id="msg-68168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">علاوه بر اینکه سوالات یکیه و باید همزمان امتحات گرفته شه، تسنیم اومده گفته فقط نهایی دوازدهمیا تو روز ۲۵ و ۲۷ لغو شده، این درحالیه که دوازدهمیا اصلا ۲۷‌ام امتحان ندارند و یازدهمیا دارن!  باید منتظر واکنش رسمی اموزش و پرورش باشید @News_Hut</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/news_hut/68168" target="_blank">📅 14:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mob3k5bTCFsYS5Lw6jMlkYTV6BkVwbphH5EpTBWgk-b4FGqv1okbsDBGonMdia6sbs97Xb3Je-Z3KR6njnPU4D5eVlbtHFY_f0sBAcTmr60mcBiTdfy5_sFa7LMwUl3XgzZKBrchtGcTwUcVV5WpEwAUNnra-MeNM9-0StHsfm8dHOtxTwX7w13A94GZa8Cmvq4NXNF99eBVhySHgz50uPzuUYZGBCr05kd5KDdKyPfHokgy7j14RXjGWccxKChn4JSSoVkjkijq13vDq386TNNvRcZkzYDqI4EwSFsBxrIFdGOU4idXjdJFvlm02rUAbYkhNMMRL4x5vDHBrgYd5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چطوری نهایی رو فقط برا چند منطقه لغو کردین، کاش این دو روز کل ایران رو لغو می‌کردین تا فاجعه‌ای دوباره مثل میناب رخ نده... #hjAly‌</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/news_hut/68167" target="_blank">📅 14:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce063673b4.mp4?token=gzfBSuBd8qCsD1gm6qjFONEVJ12y7zrp7ruBtSzsfJ3QIos9Yi9KiBpEyxNnuoGEeY-AV044HtlVHEh7Ak59v_1O7QYPtwGejaH7KuRtPb8wLwI6foW3MZAMtSi7lb2IZdqEAW0hT4-yVWprhtwxzPcdLiisFiJkNCVvrPoX81DVulnY-aMjfOGVw3zThs-JmyN5PAQd63LGdyBY174oJuovU2n8n7kMXBXr6_sVlykLVGYcE9JeC6VwSkGFFSOlpvpd_onfAtn3f8d8etbS82E-VM1f8ksrMmJrcUiEV-P6D9KBZ-dFQVH8wBhoOsLjVij7GJZNILzehi3tZ7Qhjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
خسارت وارد شده به یک دکل مخابراتی در بندرعباس پس از حمله آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/news_hut/68166" target="_blank">📅 14:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
#فوری؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.  وزارت آموزش و پرورش:  بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های…</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/news_hut/68165" target="_blank">📅 14:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
#فوری
؛ امتحانات نهایی رشته های تحصیلی پایه دوازدهم در ۴ استان لغو شد.
وزارت آموزش و پرورش:
بر اساس تصمیم ستاد عالی آزمون های این وزارتخانه و با توجه به شرایط خاص کشور در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، امتحانات نهایی تمامی رشته های تحصیلی پایه دوازدهم در روز پنجشنبه 25 تیر و شنبه 27 تیر لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68164" target="_blank">📅 14:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vTREpeG0WWP1u_9yHIJyRZ8bnr_v8JluCYPU5_Q1lw_CZHkaH10aTqy5yl5df8DyChhY2HrRIq22TlEE0tvdXB3PWS4NsThBv72xvf1HkCs7WT0w5R-A4co8ja0vYFMvf8Vb2tKaKGcXQ3dInkk2GnZSUUm0_TOZrcR_nB7cw4uPc7vgDO0Rn_hg0aVebKoV1JV-zNHlgSn1eMVTrFDZYeZ0UZkQZRSbyijCOpv9AzqcCrZmL6TTaycIlYtVvhr45H9EinAvNIpxhc9MMh3OXldd9UPaw0xrTRRF2CKRY8EaBLoVN608fO-MLzkC6QjQz8IaEHtBZ-lEcPlYEidDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۶ صبح به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) موجی از حملات را علیه ایران آغاز کردند. هدف از این حملات، تضعیف هرچه بیشتر توانمندی‌های نظامی‌ای است که نیروهای ایرانی برای حمله به کشتی‌های تجاری در تنگه هرمز به کار گرفته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/news_hut/68163" target="_blank">📅 14:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68160">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5ulyIA5lgEjKoVDcgr42_Z8UHT8ZC9JOBYKfYRC8cZs1Mjgr8fMVilKXmLsniOXMdySzOiAS5qmaiIhN63P7eV8kIsE_gLahIjdp2yXGW07XlZOWMhTTPg-IHQl5WTQ9ifidtNJuAqRORwPfQuwtuE8b1EGNi-iL_gmm7OkmUMesn5snSEgjvTlGbCNgEYoHMrTbGBfJrBPnCwEZrobIO1dWjXTbxkhhdLbxoomUo0fY3doOWTPviVW_ddqAmMi2rVq3uIREBrIWq2EQlP00zzfpbcGEPKXQ2o_FiBzG0l5XFc8Q3c1vbxBZmzHTY84eniRMStSCRnUGd1DOMoqww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xqq6frW29p1hT0w_pGQZ_gAl48N3MdaG4E2wM_sOuZSirvXNJNBN0zVWyafLktktr2h_Y-b0L-xABv1YfthG0HMbS8tJL-CYCF5HlvG7ujotFl_SAfVvzAJd8WRSL9_MxEB3PyCWvQH3T1x2VW78WAyH1u5porKKxWj5_IXDsQ685wKlR3xmCZHnKhqvLguxhKmnx-QZ0L9JjFq8scyTxYUcYXeS8dXrg4-_7czo3LS2E_H8mZBrH1K3BZ8XNs706rmxZZUIOGtgHxqvVrDGRYzqIA1BOhSfSWRvF6Wq4FcLylDiBmoAmEadP_mo43IFVmczZiFahTkIOVytcYI1lQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a57f3aee50.mp4?token=qmuglpwepclI_3JhYCaTIMGPcCVPbc7KxpKOjJJSTNezzfFCftgktFwmqa1POlpYn_C0Fa7L9fX-XwizjLX5_sYJiWxNZq3XBc5nDqPoufy70PGjtbhO6qZ1TPDq7NwOwB2RheF-3DKSn9zBcju0tG8KsV5gLrmBSCpC9XAMkOEPMlm7PhEXiZ8sRJE3jhMm_tVQMCYFD8MvX9jh2gIRiEOkwRUP3HcKChd5jY69JhW8iQi1Nc20V54blbeObEqLYD5RpG6XbwCJcvK_R3WmeVAr-RzTwCQ_jZaC3XADDRV5cC3ku0fZdzFbAIiqs_cWohF9Ml9nVC0_rmXJTiS3zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/68160" target="_blank">📅 13:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68159">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgl-FE-AId9EfE33vkQmh03MiX3Zm7SO_EeRRybQJJWz4aUOnPc01Uo2TsRpzuG5hmNny0SrOjFS9VI2ZBeqLN-QpZpAvv-tQI2SbVfUPU19CpmgJAyQOcdidJ0iHScYVnYYbPod3XomQxdX2uqIPW4VC2bNX4A5tIgEKRAEuOMgbJ_WH3Q3IOh6vGSY07IwlKjHrSU0jeW5syn1rZAcAcGTEEdZOOBcX2rXkI5ljQnd-ygsWaKtA8p2KxL0tqmteO7Vkf0M-aQO024L2_bmLOEukYV-nhBuAB6sEfJ5TRcT2ascs2rgb0JUVvdVmdbVvtj-OdYr5CIL1jQ7Yfbhgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/68159" target="_blank">📅 13:27 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68158">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSb6YbkDsdjsf2xE6FyrG54zwlSnCPYREhjz-fdJWdRPJDmYgyv9WOsCKCd_gFQ770U75nLd3WLtDQHsz5Ve8aGi0rt9DxWtF99o-YqVmuIzpUtGX5e_Ql4rPSXQFqw7xigekGtuJ_HmFgor9mUeYrK1yLXs9VGNT1X4rxzKENXPdvEkrZirNHPkHa7KrmAauZo1a4Lk888E1CEppoCtXVhjjhXwqZAkUaVrcvJvDKeUfN4CDvefzgjiSd1MEQWsoQtleCwDdJvvVqDyAGjy_P3XQl9tMdmNL19TzNDgXIgmUQ0ELAvBIvQNdjp7OGf8-SyYpskqTF7Raaa6fkhFAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرِ داریوش فرضیایی (عمو پورنگ)، بعد از تحمل یه دوره بیماری، تو سن 90 سالگی درگذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/68158" target="_blank">📅 13:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68157">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
امریکن گات تلنت یا همون عصر جدید آمریکایی ها
یک شعبده بازی توش انجام شده که حسابی وایرال ‌شده
👀
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/68157" target="_blank">📅 12:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68156">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HigEvfNcOpDvQ8F5xOj1O1a_pSiUeyskrQAejw0ClAQwxuob4r2GpshxfGT-PIhz_-ZVMPUINVux8aTGBk2PbjH4wUuosXJofZlWRjpLiW32WKFnTvrLuryi4iZCJGVYCdBkZDTShgfIeLlTLNWmEN_0gzHSDHsEdNUsYUlK9SeVEedRLN--QKKhyOJnB44qTCjN3wVTvnRcaPIHEGnu4QMZ2V27t-bNhistwy1GXw492uTLwtCRI-T7p3_pCSqHC6WR8NLdiln_XMWcRbyH3MJb6hrkEuJY08svsxyVUD8EESYz36qGeaRueZTCw4rKS43rBqYwTg8A7GfQSFM3RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ا
کسیوس:ترامپ در «اتاق وضعیت» جلسه‌ای درباره حملات جدید و گسترده علیه ایران برگزار کرد.
به گفته سه منبع آگاه، رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای را در «اتاق وضعیت» (Situation Room) برگزار کرد تا درباره یک عملیات تهاجمی گسترده علیه ایران گفتگو کند؛ عملیاتی که دامنه آن وسیع‌تر از حملات کنونی در اطراف تنگه هرمز خواهد بود.
به نظر می‌رسد ترامپ مایل است جنگ را تا حدی تشدید کند که خسارات کافی به بار آید و در نتیجه، حکومت ایران تنگه هرمز را باز کرده و خواسته‌های هسته‌ای ترامپ را بپذیرد.
ترامپ این نشست را در حالی برگزار کرد که ارتش آمریکا برای چهارمین روز پیاپی، حملاتی را در منطقه تنگه هرمز و در امتداد سواحل جنوبی ایران انجام می‌داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/68156" target="_blank">📅 11:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=cGK3KcLhkagVsxufc7PRp3MXYn-zZvIBTLLC5LCgVFz4iqa0DG5_-Agp7bfaWBxi7xUO_bHfS2Kbdm2E_qxzOhTcLQr08kxqk6s55hV--gLr_xHIsEpfmCC7u_3HHl-09s6Sc8qdQlfkCz9DMpC0aDuuznIqBFDTvUPMMwclrrw0xm_PuMzqViniTBLei3iUqFX16rqqy7J2M4RCSWRAu8HAU9ur11b8zJ24XBCvxLjdT1P1EJNkZNdgLbzAriBpgNuYiQdSaW9rhjFiVJ1IQxxVzQJqrJkb1hdZK8JOH1Qtj9nlsfndliyPoUBK_iHfVJaofSdcsunoKo3WEL852g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5c420396.mp4?token=cGK3KcLhkagVsxufc7PRp3MXYn-zZvIBTLLC5LCgVFz4iqa0DG5_-Agp7bfaWBxi7xUO_bHfS2Kbdm2E_qxzOhTcLQr08kxqk6s55hV--gLr_xHIsEpfmCC7u_3HHl-09s6Sc8qdQlfkCz9DMpC0aDuuznIqBFDTvUPMMwclrrw0xm_PuMzqViniTBLei3iUqFX16rqqy7J2M4RCSWRAu8HAU9ur11b8zJ24XBCvxLjdT1P1EJNkZNdgLbzAriBpgNuYiQdSaW9rhjFiVJ1IQxxVzQJqrJkb1hdZK8JOH1Qtj9nlsfndliyPoUBK_iHfVJaofSdcsunoKo3WEL852g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه برخورد پهپادشاهد ، به طور مستقیم به یک انبار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/68154" target="_blank">📅 11:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hafYOvjm1eOj1FWsKpJS8XgfbGRccZ0B41cRwjNNl92hexsT_uBgG701Sg4yWieX1yajNIQrlmTYQ12PJ4oMj_KIWs0LCqj4WF-uBMOQlKRAjzOTrwHZdXLKGFz5i824_nwx16SDymkA3F6C7fKQGokApBkxgKjeWYa-7NMAtGIPwSDGbR7Q5EV4F5t_-FvcQGREBg8vuDQDHVZp4YJMOzw1WbdiOQNPFeBBfPyWsBwr-zh3WWepgWW1MofkqiWIr61VqE-MRc8-Q8O20sL3Dx0RNHj6TqltfJ9ysmkRxfkCYJuB3fc0srpfbJk64HhQ2YTyZ0vtIzMP6MBiVNQ55Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل بچه‌ شیعه‌ی آخوندپرست
🤯
🤯
🤯
🤯
:
#hjAly‌</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/68153" target="_blank">📅 10:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=HIXR0dnSR2I7Cfm8gbK_llraoIyrZTRb-4i8T7hMo-x5ySPtOvuNAVIKqvPMexhuH_k0LXVG88JOfqGEIVodXtkS2gtIAAIBCugCyrFGQYgBfQ_xN35ie3eCW4S8NQhDmRdg2V5zLvaHiaWhsipQBfxAYeDn1_iqjselSW_nF6j0pxypF4OmQXd9oZsJWOW-P54PUvDE6_fwx3FHwXlVubQEcS9O-q6yIYMxNFPivuPKM-7WwtMcfWomMUFam6bm0BqwysOY3R8Gs_JfZ9sXwNEO7Ywq_43W1P0sygATFjy-LBm5p8XeuTxjZ9N2zQDHoPrVj_Om3EMCDwMEiUAVnr6_1oNlsFg3jaCTkS_uib8sl0PAD3BKs0LEWvytyHdj9YXKciUlBRy71LwAkggtf94myugIXng4N-6gxWGIaPm-szao88PkEVMYeM2m7z2XnJikyMYcjZleTXbOva4bEf-p2z-RVd8ln0dT3s-Eb9IyqWzg4DwNfYW4SvTnSF5ihYygrPwrFG_uE6YNoXDmVwxFwqVjAywO_xgIhdUg5n4naqjOSkFzMSwRAPNwqbzBgP0VxMWuo9xujrGl3ElqjGgdQgD7olUN0ZfzfsgBBCIJMs-Hbwlta0Q3lnPV3hX_8jlC16A1Tpor3v2zIEwpBxhP2f0RU-YMjKI0EX5CB60" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31c4cf4b27.mp4?token=HIXR0dnSR2I7Cfm8gbK_llraoIyrZTRb-4i8T7hMo-x5ySPtOvuNAVIKqvPMexhuH_k0LXVG88JOfqGEIVodXtkS2gtIAAIBCugCyrFGQYgBfQ_xN35ie3eCW4S8NQhDmRdg2V5zLvaHiaWhsipQBfxAYeDn1_iqjselSW_nF6j0pxypF4OmQXd9oZsJWOW-P54PUvDE6_fwx3FHwXlVubQEcS9O-q6yIYMxNFPivuPKM-7WwtMcfWomMUFam6bm0BqwysOY3R8Gs_JfZ9sXwNEO7Ywq_43W1P0sygATFjy-LBm5p8XeuTxjZ9N2zQDHoPrVj_Om3EMCDwMEiUAVnr6_1oNlsFg3jaCTkS_uib8sl0PAD3BKs0LEWvytyHdj9YXKciUlBRy71LwAkggtf94myugIXng4N-6gxWGIaPm-szao88PkEVMYeM2m7z2XnJikyMYcjZleTXbOva4bEf-p2z-RVd8ln0dT3s-Eb9IyqWzg4DwNfYW4SvTnSF5ihYygrPwrFG_uE6YNoXDmVwxFwqVjAywO_xgIhdUg5n4naqjOSkFzMSwRAPNwqbzBgP0VxMWuo9xujrGl3ElqjGgdQgD7olUN0ZfzfsgBBCIJMs-Hbwlta0Q3lnPV3hX_8jlC16A1Tpor3v2zIEwpBxhP2f0RU-YMjKI0EX5CB60" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آخوندها عُمر طولانی دارند و بیشتر از عمر متوسط ایرانیان زندگی می‌کنند:
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/68152" target="_blank">📅 10:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1084df804.mp4?token=i3RTp0BtuWG-JnRzeXQcAfoanTiSaPlTgr4j2IogXlyB_YrK2XULdymb7JDJCbqkFWqPpBYu8l0TxnplwEQfZSzGg54JXfHm24qn_9i1tLkjm6zjUXXF_w5maaEgxu_m-39eRaIVejfh9wAryzdP5TPfHmhKS7UdSbeHEJz8S2_lselV8nD4aqU77WUzSb0S9b0T-J4tmp_lk05AmTHFVQdnr-eJbUCD6TXqOwvoxSrqujzaY_eblI9Hj2aDRa9oEH7CxMEu3TQyPmR4wSK94Eyss-TU0OFjbeY16WGUhAw4N4Hc1aqzfT_xoWp_De8lri7QdeNqHayEPeh4dyz9SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیش‌بینی پروفسور جیانگ از تهاجم زمینی به ایران
:
پروفسور «جیانگ» تحلیل‌گر سیاسی مشهور در گفتگو با «پیرز مورگان»، مجری معروف انگلیسی، پیش‌بینی می‌کند که «نیروهای زمینی» آمریکایی از اوایل ماه دسامبر در ایران مستقر خواهند شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68151" target="_blank">📅 10:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XckDtsiGtTUQto-Rogrdam5DkJeUQRS4Xyti8ZIzOvrDACp9ZwfWmUeV7W_UQWnSUsBLAaMO0tKNdQLjA5l-oHMWD4SONSmUof95ctv7-ny1S5tOWSrdafj58oQjzP5z9UEyP_iVTFNg5Nvtvg3axsJ74ypXTnHNDYBfhM2PlunnJRDwwarJOti8Oyn1-FBBfTWMnaHuraGxaVtvIgn0HM92XSwUvEu780r7H9yHL8LSVqJyLQOHOQfVTMW-TutlSI2hjrQQ11JlIoHezYyPSXJLcNJcGG-FlzSnlm7glwIhKYuqv-0UF9RvXz5pfdzz4D-b0oaDWZnD-qzR9MkoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ: کوه کلنگ ممکن است یک هدف احتمالی برای یک ضربه بزرگ و سنگین، درست به درِ ورودی باشد.
کلنگ گزلا (یا کوه کلنگ) در استان اصفهان و در نزدیکی شهرستان نطنز واقع شده است.
روزنامه تلگراف پیشتر گزارش داده بود که تأسیسات تازه‌ای در مجاورت کارخانه هسته‌ای نطنز احداث شده است.
این مجموعه در عمق ۱۴۰ متری زمین و در دل کوهی به ارتفاع حدود ۱۶۰۰ متر، موسوم به کوه کلنگ گزلا یا همان کوه کلنگ قرار .
ارتفاع این کوه تقریباً دو برابر کوهی است که سایت هسته‌ای فردو در آن ساخته شده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68150" target="_blank">📅 09:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93235f7cc4.mp4?token=NCqFi2yV9S7g9eYE4-57nJRNXGhifJMhwWcXxiZSNDLOevu9Z9p-Nf2d6_oeYu1nsEpiARa9lc-oPU9iue6iAydbdVUJqMuPpt824wE_TPzmPGh4KATQVczxBXR6cpl8T5yLQyPW4uwcVHaKp2YmP3190BtjHKPIEwP7hsfr6aFl8yfGMe5P3cgqkN53ODTLKoFZYT_4LoW74kxtHrlM1edETmBKZLp1bKK6mKreeaIJAImvLCQpFw2JlCfiV517207qFrQvsjToB7JZWmhu00DzhZkaeBxRWMLmeszSSv8YD6l-ttKPCIWCTT9wLiC6LO-1vwM_8CiMAPdF2ZqLcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
رسانه حال‌وش: شدت انفجار به قدری شدید بوده که در لحظه اول حداقل ۱۰ نفر کشته شده است  @News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68149" target="_blank">📅 03:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده  @News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68148" target="_blank">📅 03:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68147" target="_blank">📅 03:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
تا این لحظه ۲۰ نفر زخمی و ۲ نفر کشته شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68146" target="_blank">📅 03:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a28218ed6.mp4?token=tVSK62kVAl3JAxAYtsgkZJOUQNGEs714xKnngdJD04yuyM_bZ2dR7BK-rlc-Gv2XAjQv9Mw4Fn_jB6Pz5-Y602PAV_5AKCZgYfCbrmRp5H7I_9JN2T0G3l_Nb57nud0mscfDqXeuTGF2h7a-Us4nG-h6kVNb0b4eIfJaKqi57-ROB2nfzgR7Wr3PGpbAKEJ4zRP5COmzy4mWMtNkPQZn55FQrdSwt7xT12fiGO-JLMwmNfw5lDD06iwrqHtEYw8OjBy14-ir8ABwvYm6dvgEavWHFloVBHFppY3bTlcLDJ9LZXAihmKnf5QXXHHIOZ526HiTGW1RF1B4tN83NSP66g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تلفات امشب نیروی نظامی در بمپور
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68144" target="_blank">📅 02:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">حرفای امشب ترامپ رو گوش کردم، یجا گفت فعلا نمی‌خوام باهاشون مذاکره کنم، تهش گفت اگه تا هفته بعد نیان برا مذاکره پل و نیروگاه‌هاشونو می‌زنیم
😐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68143" target="_blank">📅 02:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">از تبریز دارن اردن رو می‌زنن، جالبه از پایتخت اردن تا مرز اسرائیل فقط ۵۰ کیلومتره، ببینید آخوندِ گنده‌گوز که ۵۰ ساله می‌گه اسرائیلو نابود می‌کنیم، امشب جرئت نداره ۵۰ کیلومتر موشکش رو اونور تر بزنه :))))
#hjAly‌</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68142" target="_blank">📅 02:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43530d8c1f.mp4?token=U9fWYpOhdKEoV8LLAB_jrDJZFjW-PUYLbqKTEqTzfMKaJ-uAX2Q5Y7TGle6s_8EXv_oeLiWDGj-58oMPUYyJzdJbNeInOidU8zi5dqVyzTWzmbipqUKzuJC0pFq1J_Og7gVpduBn501ISnNQBi2ud3jZk6GMekOQsUMlDFyEMpiIFrxFz9pk1CRQJ938UybWXtfIBpGM0ePLIicfE5wODL6CYhHs38oTUEWqfs6VTn4ZUDFEScS6YPopWppy-sxKUSd6Ka5b8Rt0ED6uyqZqYH5c6a5PXEuycvxOz_-sTmdps4pImBZwXnSSXNBZzEwZGaYPbcmmOaj3rJHhGAv4oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68141" target="_blank">📅 02:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68140">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/453748b7ef.mp4?token=aaRGCekMwjqezy6n04xyoXdU-5uBH4lhVh7-tory4dI-UNkGoKRv4hQCdIfI5NhcvqqqqfBgdD-dvSVyjZuOsXUL8YiNXcMrUWC5RVbFCmHq6fYztfw8FDpEHVaRfQBXE-fcyuxXoaELc-t0iPrWAAGyGn8DIQiPGywvmWTqZ1wLWDAS2xO1q5VFUEAqdsG5pEdTS0F173UT5DU-wDe3GMJ9MmvugNI95o0erCXsu6Sg9gikVCAUQ7UzpWzkRcZPMMEFdX5lTy8AIs34BKHHaDz9iXKJDIqhjt_azCuvGK12HCT7RMX1rKq2fdCHgC5NBDhtRp1JIb4KAIDRj5xIMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو ای دیگر از شلیک موشک‌های سپاه به سمت پایگاه های آمریکایی در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68140" target="_blank">📅 02:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68139">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1073ff30f0.mp4?token=OZB5EphMn_S7aVJbMh0m0SYRN2E53VahSTs8s1zoKGIEQqzPhdR4JMrY74u0J1uZrBmfgRb8J3PnRWUkJEw5U9_461XOjEGdIWD6mvhS00k3tIZGPdSF52J4sp8yYYIHH79zGkYRbuXQMtDhMr9Iu2hFF5urhhhMt4-znZn848yS4NUOh6BgHpfnPtkcGmg31v6Z8-TEZTq1dt9zrB1VMdEuCFxQh9JTJnjs0bnRoQZihfE1PnIlAEci88HJa_XScSKYDr4LAcVm-YXGGutlLu7srZLlG1tRg3VKxEsRTXqDi6-fcJIDdEvL72w_vniHNEqZhnrZa9mTBtH_f6pTMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68139" target="_blank">📅 02:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68138">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
💪
گزارش های اولیه از شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68138" target="_blank">📅 02:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68137">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=l9KYibH_UoxOV9jbR8_FceQ3-03X5GvZD0SOOnM0s753dH4EXC0ItSJddMb1TRMRrH8tpywu-wEgZ6Uxx_GMXlLx_q4T99MHmOssO1CDuar520mtNeYlejjIMNaPZFZ4jvGLltBOm10C7IFcUiQwXx2ypVZNVQraOHfAtrvU108TEZsnSWufGPWmH0s6e-iUrLrvr_gVBPdCv0yK6wyJTlbTfaRpJGBvfKM8fa3rMUz0NFlYVbnH2Fh6YJw2VJ1lZEmJ7tnWeJaoLe6AFG1mRXC4y-0d3KCyFsib2BA-Vv0Ao9buKlLrLaFZx2zux9r_-LFYWiomy4VWDgrtdHSZNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/682a3eeafc.mp4?token=l9KYibH_UoxOV9jbR8_FceQ3-03X5GvZD0SOOnM0s753dH4EXC0ItSJddMb1TRMRrH8tpywu-wEgZ6Uxx_GMXlLx_q4T99MHmOssO1CDuar520mtNeYlejjIMNaPZFZ4jvGLltBOm10C7IFcUiQwXx2ypVZNVQraOHfAtrvU108TEZsnSWufGPWmH0s6e-iUrLrvr_gVBPdCv0yK6wyJTlbTfaRpJGBvfKM8fa3rMUz0NFlYVbnH2Fh6YJw2VJ1lZEmJ7tnWeJaoLe6AFG1mRXC4y-0d3KCyFsib2BA-Vv0Ao9buKlLrLaFZx2zux9r_-LFYWiomy4VWDgrtdHSZNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا همچنان قصد دارید جزیره خارگ را تصرف کنید؟
⏺
ترامپ:
خب، نمی‌توانم چنین چیزی به شما بگویم، چون اگر بگویم حماقت است. اما کار جالبی می‌شد و کمی هم خبرساز می‌شد.
⏺
مجری:
آیا احتمال عملیات زمینی را رد می‌کنید؟
⏺
ترامپ:
می‌گویم نه؛ البته اگر شرایط اقتضا کند [رد نمی‌کنم]. گاهی اوقات به عملیات زمینی نیاز است، اما ما افراد دیگری را داریم که عملیات زمینی را برایمان انجام دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68137" target="_blank">📅 02:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68136">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25d7e536a1.mp4?token=RFoFrEsuiwi-m7Ti_dxPbVvpxI4rH2WlVIY6qgv96PvT0t5mJgApjz76bjc0PFbAmMO6JdOe_o78GJ48NoCmQAHfPiNjjvXW5iNWdcp8ogQvzI5pvsxVf1G_lb-_HLXXe_qiHYQoX7I_vowwy7s6WUDF4izDikBWvTY8dWOec1Us_NYlCKnWuRsrJKip3dvxaSoWfUoIWStGw8s7NPRcYSRLi6SM_S0TUIEr-pxW-3-g4k0Y9acWB_ZH51X9XiJH09yZR71uqVAQnMpTwSAtZGPYYfywuYBkUhfCuGy1Wmq4vjxLeGVg5d4JyyHgJ_ZMBQmKcbgoRcSP-wt-xaXRtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ما در حال رصد «کوه پیک‌اکس» هستیم، چرا که گزارش‌هایی مبنی بر وجود اندکی فعالیت در آنجا دریافت کرده‌ایم. ما دوربین‌هایی در اختیار داریم که قادرند نام و نشان شناسایی افراد را حتی از فضا تشخیص دهند؛ این دوربین‌ها تمام بخش‌های «پیک‌اکس» را پوشش می‌دهند. اگر آن‌ها کوچک‌ترین حرکتی انجام دهند، ما بی‌درنگ وارد عمل شده و هر اقدامی که لازم باشد را انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68136" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68135">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3f1669520.mp4?token=BqB_iTGIMSHXTLIx108o-o8lN859KkIGJtKsdL92VW0GK1hjUE6MFakgzr6JkI5YoX3LJklAk25OhgkmTZYtfaXq0ZuLLdeeD98HpJ54a3XAFxQMzvfyApVdgYk-HXd_93_Bp_6cApLwfIMqfWQDzbBJImoG9iKOniLAE3DGy-8T_j2uJzncpjnzQkbkusvrHzX2H_8jzMgZQPYx08fnShDHCjXJD_1AKX4RgQrhzcxyums7WYTE2drxUK_QXME7x226TgowZGPAkFb7St5F_Ajl1Va77Pp76wJ8CmnsToPh-l-tuTOxDjAhHgND2latb8jqc3hqPjdPD0mG1l7_Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
«۱۰ فروند کشتی روز دوشنبه از تنگهٔ هرمز عبور کردند — کمتر از ۱۰ درصد چیزی که معمولاً از این آبراههٔ حیاتی عبور می‌کند. وقتی می‌گویید «تنگه باز است»، منظورتان چیست؟»
⏺
ترامپ:
«اگر مردم بخواهند از آن عبور کنند، باز است. ما آن را برای ایران باز نمی‌کنیم… الان باز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/68135" target="_blank">📅 02:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68134">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
مجری فاکس : آیا انجام یک عملیات زمینی محدود را منتفی می‌دانید؟
ترامپ : «نه. گاهی اوقات به عملیات زمینی نیاز است.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/68134" target="_blank">📅 01:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68133">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbabff277a.mp4?token=sM5KE5Xo0OH0-_7tYrzAe5j7BhNBFqMQsOoY7JrhDteCNyjCAx1U29N_CA6ao4vaRoNM1MCZtOpN_4geGe1WrEz7Zt6-3HfvMisXv-au87d6XfeutOVjCQqZqzBsuiQJtF17PralL1Ene4uyCykv359e94Og6b3tv8iaVp14Nj880ZLDkoaHflg88rTsUl2EvqyiJsPodv1GRZt_kSgslVxEyyv3ncM2mCpSCIA8uZo-u_G1RbZTQUPNP40ERUR7aqQTVMWVoTI-2ZpHpxEZZ8MDsBycIRLlLlCeI7ujPG-QPPSgY197jZ08mTHPTRoBp4F-kJMSLKbqYVgCkMFeqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا اطلاعات خاصی وجود داشت که باعث شد تصمیم به آغاز این عملیات بگیرید؟
⏺
ترامپ:
ما می‌دانستیم که آن‌ها خواهان سلاح هسته‌ای هستند.
⏺
خبرنگار:
آن‌ها می‌گفتند که خواهان سلاح هسته‌ای نیستند.
🔴
ترامپ:
هر چه می‌گویند دروغ است. آن‌ها دروغ می‌گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68133" target="_blank">📅 01:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68132">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=RVW3LqkhZZuoJQ5_ECWwweu3aa4l3BGXiRQrGbu3saAWUXYdndhr9hW0lsGFPigaL2-5g5KUoxHtmlyVtHKOYNmSqiaaX9MR3HZibO0F4j1FXMwhHxTg6m6SNMUtXRHntXnmaRKTJwmsAtlimwPZYPQB_Ihr7gKNT_WLFlsV8JaIcOs_sVwoKti7ElZgirCzA3QBotO0J6d5rLgQHv_TKER5XLw--_W1i4s3_w4fspLggQ2FNhIbxCZWhGQ-tVzAIvpTq7qDwt_z5qdpataDSd82r5eajvs_6SQhjhJaR18EK4t3DBG-GW3c6swWirKKPCEG3AtK3MKYKJ7JE-7ftw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f31387d.mp4?token=RVW3LqkhZZuoJQ5_ECWwweu3aa4l3BGXiRQrGbu3saAWUXYdndhr9hW0lsGFPigaL2-5g5KUoxHtmlyVtHKOYNmSqiaaX9MR3HZibO0F4j1FXMwhHxTg6m6SNMUtXRHntXnmaRKTJwmsAtlimwPZYPQB_Ihr7gKNT_WLFlsV8JaIcOs_sVwoKti7ElZgirCzA3QBotO0J6d5rLgQHv_TKER5XLw--_W1i4s3_w4fspLggQ2FNhIbxCZWhGQ-tVzAIvpTq7qDwt_z5qdpataDSd82r5eajvs_6SQhjhJaR18EK4t3DBG-GW3c6swWirKKPCEG3AtK3MKYKJ7JE-7ftw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«همان‌طور که می‌دانید، ما پیش‌تر دو بار به جزیره خارگ حمله کرده‌ایم... اما در مورد تصرف آن، اگر بتوانیم توان آن‌ها را به اندازه‌ای کافی و عمیق تضعیف کنیم، این کار را انجام خواهم داد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/68132" target="_blank">📅 01:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68131">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
حملات به ایران ادامه خواهند داشت تا زمانی که من بگویم کافیست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/68131" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68130">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=WIVsqfRIHi_UxkYN8T6jf3UlPkCl0sLojfRFlJG3_CZuEdQAsI6BkimBPst3LEEZofeoAwsrtNJyUXFWQP7Tr7bRPBC0sGJZrio7SoirS1Bmr83AGZAid50W0JGaxPYNLk187jdoeIweEa6-YWn7U0-cpIg0X3VUwME23NhrTrpnGhJXMPMkJDm4P_qsvq9vF0bvZW6-7tw-0Y1nDUhV57qxDKCZRC0jusVmnz5BXvrT9mP_7QMeyIGI_Lqcarys9QqYtzg3FF88_kE8CQmMUr0nOLmZ_19-bkJ10XMlwbxLh53jkRb9rH71IHYMoOPCUiFSArlL8muBQ8wJW1CSUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f264ca5d25.mp4?token=WIVsqfRIHi_UxkYN8T6jf3UlPkCl0sLojfRFlJG3_CZuEdQAsI6BkimBPst3LEEZofeoAwsrtNJyUXFWQP7Tr7bRPBC0sGJZrio7SoirS1Bmr83AGZAid50W0JGaxPYNLk187jdoeIweEa6-YWn7U0-cpIg0X3VUwME23NhrTrpnGhJXMPMkJDm4P_qsvq9vF0bvZW6-7tw-0Y1nDUhV57qxDKCZRC0jusVmnz5BXvrT9mP_7QMeyIGI_Lqcarys9QqYtzg3FF88_kE8CQmMUr0nOLmZ_19-bkJ10XMlwbxLh53jkRb9rH71IHYMoOPCUiFSArlL8muBQ8wJW1CSUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«در نهایت، اهداف حوزه انرژی در ایران را هدف قرار خواهیم داد. نوبت به پل‌ها می‌رسد؛ هفته آینده سراغ آن‌ها می‌رویم. ما تمام نیروگاه‌هایشان را از کار خواهیم انداخت. تمام پل‌هایشان را نابود خواهیم کرد، مگر اینکه پای میز مذاکره بیایند.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68130" target="_blank">📅 01:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68129">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36032be115.mp4?token=vAKy4emQerhddhfUPlsuJtOnp5IV0ITYRK7ZUatEq6nkzXdYKV6ucSHCFEyBZkaCAAe-DOlt8bVyutEdOWn5aKyownKN5oglBmU-gvJ77X_LkEicT5J02uQY6Nz8WuFjKkiloG3DvnigvzkI8aeY_NG94WkDLa70RwiuHsFX6vN0yrKxLvaihY8Vq9mP14B6hQ8MPd_jUlR53NgztqZDBURfDqEoM2aAyAXagd7iJ8VC8fKt60hxjcSv5K-7mRsLnOLYMd5w4mLa_QPpcFXSSU4B-PbBwWSK71kUZ5qu7qyDQYEZGplMrB-ZdrcClN6nCTsP9WC1W_iLK2SXlAXskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36032be115.mp4?token=vAKy4emQerhddhfUPlsuJtOnp5IV0ITYRK7ZUatEq6nkzXdYKV6ucSHCFEyBZkaCAAe-DOlt8bVyutEdOWn5aKyownKN5oglBmU-gvJ77X_LkEicT5J02uQY6Nz8WuFjKkiloG3DvnigvzkI8aeY_NG94WkDLa70RwiuHsFX6vN0yrKxLvaihY8Vq9mP14B6hQ8MPd_jUlR53NgztqZDBURfDqEoM2aAyAXagd7iJ8VC8fKt60hxjcSv5K-7mRsLnOLYMd5w4mLa_QPpcFXSSU4B-PbBwWSK71kUZ5qu7qyDQYEZGplMrB-ZdrcClN6nCTsP9WC1W_iLK2SXlAXskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
خبرنگار:
آیا جنگ با ایران از سر گرفته شده است؟
⏺
ترامپ:
خب، گمان می‌کنم بتوانید هر طور که می‌خواهید آن را تعریف کنید، اما قطعاً ما داریم ضربات بسیار سختی به آن‌ها وارد می‌کنیم. آن‌ها باید ضربه بخورند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68129" target="_blank">📅 01:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=fN36U7P5S7rilTXZoVS4qslTuFbrHhsl3zoqCHoGhnGhq-YZi9yo5zTrazF4oAcB0-EEcMCqncAfPmtnJVjbWjkw5295pdUhrZeUZ93KE4pD3SUhbMrwaoQj4pExthfV8f7cD0dC4wSNY4gsjM7J9BE0ex7V05rICyXscGeCqCMr--s_4Bp4mx8IViLLhp6ihJJjnSdDGfa5vk-MT9-ZE8XADc4lzPloQPqwNpk4zCuGHaZyMPkAB20a-fZifXAuSJd27qwmbdT_5lfHOUCxLoiRlX3zVfUdqi_qkEYCK8YuiM_rzoN-orBoWIOoAHXvjK1Q5C0J996Lbeq_sPXIOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4323d3fd2.mp4?token=fN36U7P5S7rilTXZoVS4qslTuFbrHhsl3zoqCHoGhnGhq-YZi9yo5zTrazF4oAcB0-EEcMCqncAfPmtnJVjbWjkw5295pdUhrZeUZ93KE4pD3SUhbMrwaoQj4pExthfV8f7cD0dC4wSNY4gsjM7J9BE0ex7V05rICyXscGeCqCMr--s_4Bp4mx8IViLLhp6ihJJjnSdDGfa5vk-MT9-ZE8XADc4lzPloQPqwNpk4zCuGHaZyMPkAB20a-fZifXAuSJd27qwmbdT_5lfHOUCxLoiRlX3zVfUdqi_qkEYCK8YuiM_rzoN-orBoWIOoAHXvjK1Q5C0J996Lbeq_sPXIOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
‏ارتش جمهوری اسلامی:
در مرحله هفتم عملیات «صاعقه» محل استقرار جنگنده‌های اف ۱۸ و سایت نگهداری تجهیزات ارتش آمریکا در پایگاه الازرق اردن را هدف حملات قرار دادیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68128" target="_blank">📅 01:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
حمله به جزیره هنگام
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68127" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
بندرعباس و سیریک بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68126" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68125">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=YaXGdzfo3mgNSzyPaSSlhtmpcz-h4SRvroH8x6UlctLi7gFxIaZRzKYzYH_te81RzMINC0drG66H6vJNaf6CNuc38TzrSDHV_6ABv2vlKfxpgFaOz0nzBuYoGVEycAr5siGACxsOmKmwbjuc4M1nyIzD14SBqBTjHB6-GWPYkj3KyljD1lLqWIn_eMWBtNAqU8qfXqExVX_YHWemJsnZK5YycWCnUNhmygXW4xFD9JW_zSeKLIIbDYnv2EE0xl-edVfZWNUZDYWLxILeERR6liaDLPf3LgMXet4ClNmGvWrNuH7Wa2gq1bvn3qvJnqvQtucV6EERv1szkgEWWRkucw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dddea8a9d1.mp4?token=YaXGdzfo3mgNSzyPaSSlhtmpcz-h4SRvroH8x6UlctLi7gFxIaZRzKYzYH_te81RzMINC0drG66H6vJNaf6CNuc38TzrSDHV_6ABv2vlKfxpgFaOz0nzBuYoGVEycAr5siGACxsOmKmwbjuc4M1nyIzD14SBqBTjHB6-GWPYkj3KyljD1lLqWIn_eMWBtNAqU8qfXqExVX_YHWemJsnZK5YycWCnUNhmygXW4xFD9JW_zSeKLIIbDYnv2EE0xl-edVfZWNUZDYWLxILeERR6liaDLPf3LgMXet4ClNmGvWrNuH7Wa2gq1bvn3qvJnqvQtucV6EERv1szkgEWWRkucw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
هم‌اکنون دارلین گراهام نوردون، خواهر لیندسی گراهام، در حال ادای سوگند برای گرفتن جای برادرش به عنوان سناتور کارولینای جنوبی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68125" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68124">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.  @News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68124" target="_blank">📅 00:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68123">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
انفجار چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68123" target="_blank">📅 00:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68122">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBiDhTe8fIeu8-V5GaUYw2KnldOwqYLsgUogaBiJEblsyIysvLokHEzm9lf07hNQJw6A_mtQzSYiIJtVEHa214FAO-PEWnZDDUDXmV40lj1veJm_2FoVsmj85c_X9Int2Cw_eZoahLAamGNsB79XvdqID1sgElsHjrARD3ZI7a9RzQc-_-neuNN-G_ng0XqGf_GapPU2mEkNDcBSORKpCskLlVKw5vcqHKj9R589iXzcBzy9sjoDbcFQ9Hj_B6UEOMpFdgu0yGzQC8TjZmVgj_x0Pch2WWLamlc02NsgGETwhB9GLg17XkHU6kRSRD8eJUfvQ3zE4pp1liDbSEEANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اسپانیا با پیروزی در برابر فرانسه راهی فینال جام‌جهانی 2026شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68122" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68121">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=cV8kUKdZz-W1kPbMWKfO1wONHqhK5reWi-tZa6vk9KSQJf4R2ORIDH-i74yQdn_V36tewFyZGSpW2fGU3hc763GwhAdP7BKJ33vgKOvhAiKP7BtZmAzoaLE98AjDhnWncaqsYi79QctQP-F08-lDvwTZslgkRtxTn3zjleUxDm75Pf2PKzRbPAl2_ZIrQG6qO36aLVt94EP3v_bKZt4zI_TlsYge2MwShtMJLmYvJ5hxeVVzxktuIe_CYZPP3jjUXdyyzvhdbF_cGCaCwW6gzVyrHgFn4i6WnO8Dd5I3L2qrvPGyO5MoO2cqQ7R3M3OWpvHAGSRuyw1FlDng6oRUVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a5f1d44f.mp4?token=cV8kUKdZz-W1kPbMWKfO1wONHqhK5reWi-tZa6vk9KSQJf4R2ORIDH-i74yQdn_V36tewFyZGSpW2fGU3hc763GwhAdP7BKJ33vgKOvhAiKP7BtZmAzoaLE98AjDhnWncaqsYi79QctQP-F08-lDvwTZslgkRtxTn3zjleUxDm75Pf2PKzRbPAl2_ZIrQG6qO36aLVt94EP3v_bKZt4zI_TlsYge2MwShtMJLmYvJ5hxeVVzxktuIe_CYZPP3jjUXdyyzvhdbF_cGCaCwW6gzVyrHgFn4i6WnO8Dd5I3L2qrvPGyO5MoO2cqQ7R3M3OWpvHAGSRuyw1FlDng6oRUVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران تنها جاییه که بتمن هم به گا میره
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68121" target="_blank">📅 00:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68120">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjgaoN5NZxb__9uwiS6F8yAdcwBWT1V5matoIEKhjqF5exTIMNYSPy_cqugoOlKbixCm-_7ZSGLVoa9MjpdWtXDByZtOLagTLCfp5ddjLaVWpznRE31BwayJ9PCarjliLhtlW9M6KtiFVKpISlglG0NQv9Jvfa0FbaWmMmxp8Qagezwb873kltU9IBgarAb-Dis5wJKpkfSEALZLPWeSUcWKH4wQploc8BsQUqtwkQAcBBzXQkuVcsfYM3ASmFoG6QqznQ8DhuZ1JMG2LMZQlRIpROmLVWRD7YmfVLeOgE_GSpqPCqpQ-kyGWg_io5cs_ejxYfc8PFi5Rz36d5Rn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
نیروهای ایالات متحده امروز ساعت ۱۶:۰۰ به وقت شرقی، محاصره دریایی شناورهایی را که به مقصد بنادر و مناطق ساحلی ایران و یا از مبدأ آن‌ها در تردد بودند، از سر گرفتند. در حال حاضر، بیش از ۲۰ فروند ناو جنگی نیروی دریایی ایالات متحده و صدها فروند هواپیمای نظامی در سراسر خاورمیانه مشغول فعالیت هستند. نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68120" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68119">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68119" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68118">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=Bb-FfYuyjtUqmJbuIwMOq5TBqzu8n98FH8pq4nFBpKxrqeIu9NhM9MmEIyluh5dSKfg1q60VfVco5A4AB9z7A7hOnXnmtwqi4yD9pcAp9vT3UPUjjo6GKFUUizqWEekRzK8Qhm0YA3fweZTtqhyOx1B6wa0pSdzY-qBrndO7ys5YQveuPCngX0eG8adqHA9jpMTmGDGCN2hHJG1bmr16BU8YAG68tZz80zcor5mQMFcBgNfHTF-ijdHrk8LrQlXAWbok8TR_XHvKIsfeg-Rp9wcCw7UBTeOlVhhMH2li4uCMIKj1z4NrCJCV9TLgJWhiPZalJhG6Gh_GJuay5mlbtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c993da0a01.mp4?token=Bb-FfYuyjtUqmJbuIwMOq5TBqzu8n98FH8pq4nFBpKxrqeIu9NhM9MmEIyluh5dSKfg1q60VfVco5A4AB9z7A7hOnXnmtwqi4yD9pcAp9vT3UPUjjo6GKFUUizqWEekRzK8Qhm0YA3fweZTtqhyOx1B6wa0pSdzY-qBrndO7ys5YQveuPCngX0eG8adqHA9jpMTmGDGCN2hHJG1bmr16BU8YAG68tZz80zcor5mQMFcBgNfHTF-ijdHrk8LrQlXAWbok8TR_XHvKIsfeg-Rp9wcCw7UBTeOlVhhMH2li4uCMIKj1z4NrCJCV9TLgJWhiPZalJhG6Gh_GJuay5mlbtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
علی خامنه‌ای، (19 دی 1404):
ترامپ که با نخوت و غرور نشسته آنجا راجع به همه‌ی دنیا قضاوت میکند بداند که مستبدین و مستکبران عالم، از قبیل فرعون و نمرود وقتی که در اوج غرور بودند سرنگون شدند، این هم سرنگون خواهد شد.
⏺
🇺🇸
دونالد ترامپ، (10 اسفند 1404):
آیت‌الله خامنه‌ای ایز دد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68118" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68117">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
⭕️
محاصره دریایی علیه ایران آغاز شد
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68117" target="_blank">📅 23:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eBEkV1uh9KxwMFYYG-NwF5N7omdUjMUH-LILbla9DPuExrwz8cmahm116j8s23m5gfbhWJesMcNtyEThPn_JQ5j6RVPcuFaWmQZTPetm9kGkL17gAQOBG0rjDHdVD9CkGRdDRPnb1oPvmzTv9X0A-sou_rNdAJpi7EYIsv-3wg1pt40ick9bq-yvt0170TCzH3e9xxE8j4md0Gb3DPWIe9zFVQGAaHs4_7xRKpUsJVch-JvooijqqOCRE1ZzmVr3MToEqgJ2AaH4JP3PjtxHxi6eUxkOS38-P9UCbATFc9XZ-x4zD0Ph14GbwhsOXvsSYuT_hkxlQXlZFgD4BzkbLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L2pcUE83FEYTVVvGW_NOAEhIb2bIeNVEiETO0LN2eLc4vGAATZg4ifkz9XGOr_Z9puLYCk6wGjKFauvXNWW50i4LBVApXEpd5eDJDv9d4Dxu8BhvrIUsI9TFn_Lxy3l4lpQdIsuch0d9vTAhxojS7xU5wY7RAq1XRAAUbkTNZeENcqUXiyq-GMqZDMjWB3v0Ihoyqd67A_iMabbgTfL4xXw8h1cs6xulNl2R8dFay-WoVQ8yVh6iHcBNLuAIrtc7Nyp_Ty2vkDEm1GgauAWmMCM-LCO_hny-1WqZfW58e46jh3KFVZjLXdrehoWcRD8pHPpmCq0h38L-eO9WiBYykw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تازه می‌خواستیم نودای نیلی افشارم بزاریم، پس هر وقت بابای مانی لفت داد می‌ذاریم #hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68114" target="_blank">📅 23:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
سیریک بیش از ده انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68113" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
🚨
انفجارهای جدید در خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/68112" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
‼️
تصاویر جدید سپاه از حملات موشکی‌ش
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68111" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ماشالاااا اسپانیاااا، اینا بیان فینال مسی راحت تر قهرمان می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68110" target="_blank">📅 22:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
سه انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68109" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68108">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار سنگین در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68108" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68107">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68107" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68106">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMani</strong></div>
<div class="tg-text">بابا نکن من چنلت رو دادم بابام
😂</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68106" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68104">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from⁪⁬⁮⁮⁮⁮⁪⁬⁮⁮⁮⁪⁬⁮⁮ᴹᴬᶻᵞᴬᴿ</strong></div>
<div class="tg-text">مرسی که تک خور نبودی
💙</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68104" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68103">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-yr1dCBUX-jfIrhRoQiQC40sP9qGXnktT1Tk0f0ktIG0ewf0mW-kq_mnKC6H7X3w1HYgBkp2_DbXxNLkjgRjw3b4W6_fKYlzFquXezmQVpHpYD663TK9iM8OAKsf4FzaApd8ZsZB4hhtvnaO8FfaOIjqv4KnsT6PuaNIEnKlCjX1Eih4-uj3_OdYWwQiwjd0YHKIDJvrMXmvcQwSrx1h28ThEQ3Li1Vq4RLdn6tegr_G7lDVl_3Kr1fa7eSAfczc7ui4iNfBU2PcFNPd03xvzB-58y0G0M7qVlZijYgxqzi3Lhw6zXGSkS_H2Owpuv0KjKEvuBGj_eSbSsgUdYO3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68103" target="_blank">📅 22:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68102">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⏺
رسانه‌های حکومتی:
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های دشمن آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68102" target="_blank">📅 21:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68100">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k5gj51waBw1OQ-wPx-TXYTqmanYvKPSGVs_w9XnUZHqknfQTbHlawRDPeZZUscDoxDCOhiP2I-6B9xc9cm3WiVVAcJy732ewob-uVjM3sVVKyZQiSMK-L3HIUDQBeB_PC9pL4eqd18H2YXfNsfxx_YCFUZv5oEFIsoqZEEdPJVdPhkiWtz-QLHJHrEOdIJk0Pxi8kR2spAyIHB_EIH5Q56V9LSNiLy1VkqBHdrub_1uIINeRh-cH967C1VaiGrkCaFjwbZ3eE_7QTeGjeNpMT2hths7jZpkQiv7PIezcYQVp7h6d8wkjibnYadtyQu3qnROJ8mm0OLHdqdAdrSSBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GQjykNXoi76GMxrG18VY9-3KzCyDPNEXCgLCI5-Wose0J6Cd8puolxn2aU94hbW7opDTVsdhaKwwS3cO99sb_51o8gX1xHn7vnJ_XXm4iszN0C3EVVxwHg5BOAE39yVWd0x3izkUYnFYUvfVMYRBGpBTdchXaSSfwSf_8zq6Q830GpV6jLTtvrIr63dtClfb9YJZhEzvYWjb8LGSHQO-qc4dXEv68AzyYLcIg6imIV-SJTOkPfEEwyJmH1u1PL34ErvkPkf9H7N7Yys4IEPRsIbEkcYo_Ef6V-xxBkHV3kmfxXTrVGCBToq55yvYcleMPbvhWDTTCXqgXUecKSVlRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68100" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68099">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx4KrgbEO4LeaMtVdlKnmWEBBJ0eqHhFdv4Y_PFqJ-ke1Ht8zBu3alA0MGmxsRBHtwyF1CVusjhrtrth3qqS3KKXZJ9DXaNUzEM9A35NT0uTVMJ1RUA68JqadRpeGfkjuUHeJm1pyIESuvc6aT7cs_tqvfsc7aTvPBppJzquXCC4ZPoGbOZU2Tfb18iygXOlX5ObY1nlYKTF-K5S4U_ctSO6yOSuCed_P7UdzxEY6B1KSAFSEXTkw42GZMZ23Kv_n5_vYIxN389x7okjD3VccQqEPlbjP5gtlZGYty3NWjLn1eAfpDXip56VV7ihhT0W8rXsYCGkgzs4TeaKzRRqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
پزشکیان:
‏در تاریخ، جنوب ایران همواره نماد مقاومت در برابر استعمار و پاسداری از استقلال بوده است. امروز نیز مردم نجیب این دیار با صبوری، ایستادگی و پایمردی، روزهای سخت ناشی از تجاوز دشمن را با عزت پشت سر می‌گذارند. در کنار و قدردان این مردم وفادار و مقاوم هستم.
همه جای ایران، سرای من است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68099" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68098">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUhkWvP7g7-q8FycZCRurIOfVl4rze9NthAhkMDHGHMzNEEGaepoj0wZfmewQE1Z9yKjxC1u4WpTyUC2MgfgVaSL6wp8GbCKehE8D5eYvyB9fMz1QRd_V9znkzuuiDCg_Jc3MUHXDeMl7bOk1KEI3RSo32AQGznZNQlzHcT_AQwNdivT1AjtqxiPS4b0snTRMcDDfAjGByl_EKkImxbBXu-UMpLH9ymeNUsJy8mJhO6k-4gbxbFPSl03YvqiCUGGhnMGsDahPR9IhCUfl546pHHLlo6YE1O9z3OIEliTF03p3aDR10HfENs7SAuGY6PU1-EM89ADRn4KXWSjSIbofQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68098" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68097">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=RFFh4Nxr76rFWAq9rP2AYPkJygZptM1eeV8vJpKeVRswPLCaJ6E7lq8E7YJqbf44U7Qnn_bwq8lAiCOpZCYGTK33rlStWd9Xg2CnVL6M4NV21F2xgVQyi3UZblkheg0gphEc5sPQRdT-XF8JI59W6eJHMMzhuWXdhvsBKx_DGGJGt_NyrGzVyY3dT-0SrOW5D0Y7Wqagf0wuB5hA1LWMiX7oiPxY0MU0JBZVM5vv5tDo_qtuWL6QdZ6qDMGrAa6bK1iPxPqeJtfqo3LqKfW8VJPTLGc5BjFHh8tsngaw5GBjYPAroobGZFrHxv4G3UQfXvT3VOOs9WmNoaCKHu9vJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22e49214c.mp4?token=RFFh4Nxr76rFWAq9rP2AYPkJygZptM1eeV8vJpKeVRswPLCaJ6E7lq8E7YJqbf44U7Qnn_bwq8lAiCOpZCYGTK33rlStWd9Xg2CnVL6M4NV21F2xgVQyi3UZblkheg0gphEc5sPQRdT-XF8JI59W6eJHMMzhuWXdhvsBKx_DGGJGt_NyrGzVyY3dT-0SrOW5D0Y7Wqagf0wuB5hA1LWMiX7oiPxY0MU0JBZVM5vv5tDo_qtuWL6QdZ6qDMGrAa6bK1iPxPqeJtfqo3LqKfW8VJPTLGc5BjFHh8tsngaw5GBjYPAroobGZFrHxv4G3UQfXvT3VOOs9WmNoaCKHu9vJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68097" target="_blank">📅 21:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68096">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🇮🇷
دقایقی قبل سپاه پاسداران به بحرین و کویت حملات موشکی و پهبادی کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68096" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68095">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امروز، روز جهانی نود فرستادنه
🙂
#hjAly‌</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68095" target="_blank">📅 21:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68094">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=LufB6T9uC2L5HCTzX8UsuHhn9aX7Xw4WXacc7NXEhSyOx-rH1Y2HOfqB-fmAQxu1mepptBUh4EziRqmt3dKuEvI5enkFkni3_AC3XrLDzlSzCZFpArk-qPtt0I7SUlvPOurdQgGNLAkM2FG0RRBrljQVjQQHUGuPw7IiK3fSL5olgRUiXCGhW5MpebkjIZtEQxj_6-jEijFlnbUjuUfR4Rb4YnjYgMWGHUcdr3KnIlDoAuW4cSOVbBRfeqhtyaRpygzdL6uxAG2rsI6mvjYbbbJ5I1eRvJR40trvpWCuq9h2xjXX7lnQnUWtnnDOnk93MUgqzFTgAUbPKxbnQomsdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f9cda20a0.mp4?token=LufB6T9uC2L5HCTzX8UsuHhn9aX7Xw4WXacc7NXEhSyOx-rH1Y2HOfqB-fmAQxu1mepptBUh4EziRqmt3dKuEvI5enkFkni3_AC3XrLDzlSzCZFpArk-qPtt0I7SUlvPOurdQgGNLAkM2FG0RRBrljQVjQQHUGuPw7IiK3fSL5olgRUiXCGhW5MpebkjIZtEQxj_6-jEijFlnbUjuUfR4Rb4YnjYgMWGHUcdr3KnIlDoAuW4cSOVbBRfeqhtyaRpygzdL6uxAG2rsI6mvjYbbbJ5I1eRvJR40trvpWCuq9h2xjXX7lnQnUWtnnDOnk93MUgqzFTgAUbPKxbnQomsdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سر دادن شعار مرگ بر سازشگر در مصلی تهران
صداوسیما هم چندین بار صدا رو قطع کرد
🤣
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68094" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68093">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=S-6f_Xi7IgBatQDxeTX5Tj9HKPAv4JNhTZQJyVqP_X0kcuVTxmSU27Pp_PyJcJkeD6dqV9rUNmCfCqoqhTlpxGZe27u60yOlz9RmDlUdwmtqfih0kJNkf5w9tn3jNMy_56b9RTPd8M6QmqyFNUBqQFVZ2NiHo735Y4Wp5F1B0JQMDjCHV9uo682OaCQ4jKKZTUU1zQ4fSh-DAozkH65qibN3stCzi76EpDyHXFhcCw6x4P3Zpr_rx0xFKDwI4esGaDPOPbivV4yDJ9Sub8_raWw8_Rhd1xl_i2WSLy9HQdwcMS3rqDG6QXbZDzasSjjQD9Jw7I5o_0MEG63RVeF7Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d01c7f855d.mp4?token=S-6f_Xi7IgBatQDxeTX5Tj9HKPAv4JNhTZQJyVqP_X0kcuVTxmSU27Pp_PyJcJkeD6dqV9rUNmCfCqoqhTlpxGZe27u60yOlz9RmDlUdwmtqfih0kJNkf5w9tn3jNMy_56b9RTPd8M6QmqyFNUBqQFVZ2NiHo735Y4Wp5F1B0JQMDjCHV9uo682OaCQ4jKKZTUU1zQ4fSh-DAozkH65qibN3stCzi76EpDyHXFhcCw6x4P3Zpr_rx0xFKDwI4esGaDPOPbivV4yDJ9Sub8_raWw8_Rhd1xl_i2WSLy9HQdwcMS3rqDG6QXbZDzasSjjQD9Jw7I5o_0MEG63RVeF7Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تعجب ترامپ درباره تحقیقات اف‌بی‌آی درباره مرگ لیندسی گراهام
⏺
خبرنگار:
«آیا می‌دانید چرا اف‌بی‌آی در حال بررسی مرگ سناتور گراهام است؟»
⏺
ترامپ:
«نمی‌دانم چرا، چون فکر می‌کنم او مشکلی داشته... من شرارت زیادی در آن نمی‌بینم. می‌دانم که انواع و اقسام تئوری‌های توطئه وجود دارد. فکر می‌کنم اف‌بی‌آی وقتش را تلف می‌کند.»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68093" target="_blank">📅 19:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68092">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=pdN2akl2g1pNNGTbWJaRO_YnyV-1BMzDt0ElSe6GUmTjaWJ12pf0C18qW-4JUp6xCnM_mRiPWejwmwOUy5HlMmippP5nIxPYSL51gBDMCWVpkUpSLm2_jqpehcbbu46MmIoB0dI25xjLsT-mZgZ2_9Y2JwGt5j2DvmOGwziJG7RziT0qd_-Ls2VcDZ6YFgFVQiV1DztdLpSWZ_1-tibNmxE2XiufQ9tCnQ1CpnnHFCVXt-_qRUSCT4yQJNu2t8oILnKwz12YHKHHtvnkQFL9yZgVmbsoEvTWPCtdUTyDSMRCQCWTQU_ilzpEp73zYxh0Cq77_C6uoZb-dRJlUDiAew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1047876eb4.mp4?token=pdN2akl2g1pNNGTbWJaRO_YnyV-1BMzDt0ElSe6GUmTjaWJ12pf0C18qW-4JUp6xCnM_mRiPWejwmwOUy5HlMmippP5nIxPYSL51gBDMCWVpkUpSLm2_jqpehcbbu46MmIoB0dI25xjLsT-mZgZ2_9Y2JwGt5j2DvmOGwziJG7RziT0qd_-Ls2VcDZ6YFgFVQiV1DztdLpSWZ_1-tibNmxE2XiufQ9tCnQ1CpnnHFCVXt-_qRUSCT4yQJNu2t8oILnKwz12YHKHHtvnkQFL9yZgVmbsoEvTWPCtdUTyDSMRCQCWTQU_ilzpEp73zYxh0Cq77_C6uoZb-dRJlUDiAew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت
ترامپ درباره لغو عوارض گرفتن از تنگه هرمز
:
«آنها (کشورهای عربی)گفتند: "ما ترجیح می‌دهیم سرمایه‌گذاری کنیم تا عوارض پرداخت کنیم." و من این را دوست دارم چون هیچ‌کس نباید بتواند برای تنگه عوارض دریافت کند.
«در مقابل این سرمایه‌گذاری، کشورهای حوزه خلیج‌فارس مبلغ بسیار زیادی در آمریکا سرمایه‌گذاری خواهند کرد. این در واقع خیلی بهتر است!»
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68092" target="_blank">📅 19:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68091">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
شنیدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68091" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68090">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV65ccaC9phWJAMiVXm97lJNTrhp3_PER-zTpDRGCQ84lftF9OI9tXSLnwto1NjlCLE-MGReI55YfxeiGouxUzdOlLpnLgLM62p-OjDSOz-pg22T-3-MbXp-_yFBvz-crbHPpH_rzPjLMEx4l-uhcRV6sWuA1UlqLvnbZt-MU2eLr6i5z3oJOXwxcIh4YAhh3CLnhxbIpuluN-95uOIBkQp3d-RvpEn9VCaTW4RdVHw1Dlhwv8mlbV-e48mcggJMFrtqyljC-pL0slSAscw8BpnJF2vNEkOuo_WuXVKIxNaGs0EjixGk-yYG4NXLbauLTuyAieFH6222tM2_4NLd_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
به لطف قدرت فوق‌العاده ارتش ایالات متحده، نفت بیش از هر زمان دیگری در جریان است. درود ویژه می‌فرستم به وزیر دفاع، پیت هگسث؛ رئیس ستاد مشترک ارتش، دن کین؛ و فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، دریاسالار برد کوپر. به واسطه تلاش‌های آن‌ها و تمامی اعضای قدرتمندترین ارتش جهان — که بی‌رقیب است — تنگه هرمز برای تردد تمامی کشتی‌ها باز است، مگر برای ایران؛ و این استثنا به دلیل رهبری دروغگو، خشن و بدخواه ایران است که کشورشان را به سوی نابودی کامل سوق می‌دهد. بنابراین، ما یک محاصره کامل اعمال خواهیم کرد، اما تنها برای کشتی‌هایی که به بنادر ایران می‌آیند یا از آنجا خارج می‌شوند، و یا محموله‌هایی مرتبط با ایران حمل می‌کنند. بر اساس گفتگوهای بسیار سازنده با رهبران خاورمیانه، تصمیم گرفته‌ام که «هزینه بازپرداخت ۲۰ درصدی به ایالات متحده» را با توافق‌نامه‌های تجاری و سرمایه‌گذاری جایگزین کنم؛ توافق‌هایی که کشورهای مختلف حوزه خلیج فارس در ایالات متحده انجام خواهند داد. این سرمایه‌گذاری‌ها عظیم خواهند بود، اما در عین حال برای خود آن کشورها و آینده‌شان فوق‌العاده سودمند خواهند بود. همان‌طور که همگان می‌دانند، ما در مقایسه با هر کشور دیگری در طول تاریخ، بیشترین حجم سرمایه‌گذاری دلاری را در ایالات متحده داریم؛ اما این سرمایه‌گذاری‌های جدید آن رقم را حتی بزرگ‌تر خواهد کرد. ما شاهد سرازیر شدن کارخانه‌ها، تأسیسات و تجهیزات به ایالات متحده در سطحی بی‌سابقه خواهیم بود که میلیون‌ها شغل جدید و پردرآمد برای آمریکایی‌ها ایجاد خواهد کرد! آمریکا دوباره در حال پیروزی است؛ پیروزی‌ای که نظیر آن هرگز دیده نشده است. دوران کشتار صدها هزار نفر — از جمله ۵۲ هزار معترض — توسط ایران به پایان رسیده است و مهم‌تر از همه اینکه: ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم. رئیس‌جمهور
دونالد جی. ترامپ»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68090" target="_blank">📅 19:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68089">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcyRZ2erm3DRH_VNF-L77uz3WFH0-_fluIuGzwHz5MCY1LcaNzgsXiw5MPGt1If88qeE6bOAZfznsPt-BLuUePmNzgjGFbWITAQfoiRZ7crXn77-RlgHxU-rslc2kn0MsM1S07dYmCbnHdP14MdkIcypwx6rbl1h2rGwys5eEMJ_7k3rCO7K73zW8JT5oZ8ZNO6WfYN_mBEuTQRvvLanFOLd0M2Ivk3pZLzVCSe4uLzvrH5W4Arne93WIJF9ilLiOF5taoNMEEtd8nAV7Fb0e4RZ88PWye1IR6FbEImxFNSy7y5RWUF5VFXS1VWmcN6dScd2XWdLNijC6TqHDr6Dew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ پستی از کاربری که متنی از مصاحبه او با روزنامه گاردین است را بازنشر کرد.
کاربر : «وای خدای من!
اصلاً نمی‌دانستم ترامپ این را گفته است.
آن هم در سال ۱۹۸۸!
جزیره خارک را تصرف کنید!»
متن مصاحبه ترامپ با گاردین ۱۹۸۸:
«اگه من بودم در قبال ایران بسیار سخت‌گیر می‌بودم. آن‌ها از نظر روانی ما را شکست داده‌اند و باعث شده‌اند مثل یک مشت احمق به نظر برسیم. اگر حتی یک گلوله به سمت یکی از نیروها یا کشتی‌های ما شلیک می‌شد، یه بلایی  بر سر جزیره خارک می‌آوردم و وارد عمل می‌شدم و آن را تصرف می‌کردم. ایران حتی از پس عراق هم برنمی‌آید، اما ایالات متحده را به بازی گرفته است. حمله به آن‌ها به نفع جهان خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68089" target="_blank">📅 18:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68088">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=Lp58nvpOzt-EViptYnbURHyAxXHfTDpAno6BRzHPmu5nwQmALio40SwZ5jl4ALr7iPukcIky1R2uxzRfXe_ywdEZ9UEsNHgmcHEqTwBHD9Wi_Aaj5TmIxjym6bbhRFhNnpqmH92xHnPnUw8kdpglKbNjPTQMjlhoQZ5QdKTyrhlPueWnEx4Th4hSOLkf-YkuNAsqMoNugqeEG6OOBpZUKYRGUOco01kATWDLopS3X5hPyj7MczOhfsvRU013YGNWsouEgwOVS26xqQf9qwFTSpJfaCUSZgCxJjCtbPkUdiLCC7DGriL10OQ5I-Hhqt-A6CSv2WLqf9-KlaQHmP8a-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d70b0c17.mp4?token=Lp58nvpOzt-EViptYnbURHyAxXHfTDpAno6BRzHPmu5nwQmALio40SwZ5jl4ALr7iPukcIky1R2uxzRfXe_ywdEZ9UEsNHgmcHEqTwBHD9Wi_Aaj5TmIxjym6bbhRFhNnpqmH92xHnPnUw8kdpglKbNjPTQMjlhoQZ5QdKTyrhlPueWnEx4Th4hSOLkf-YkuNAsqMoNugqeEG6OOBpZUKYRGUOco01kATWDLopS3X5hPyj7MczOhfsvRU013YGNWsouEgwOVS26xqQf9qwFTSpJfaCUSZgCxJjCtbPkUdiLCC7DGriL10OQ5I-Hhqt-A6CSv2WLqf9-KlaQHmP8a-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نظر مراد ویسی در پاسخ به مخاطبی که گفت باید حرم امام‌رضا هدف باشد:
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68088" target="_blank">📅 18:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68087">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی شبانه به ۱۱ شناور در دریای آزوف — شامل پنج نفت‌کش، پنج کشتی باری و یک یدک‌کش — حمله کردند؛ اقدامی که نهمین روز پیاپی از کارزار حملات گسترده علیه ناوگان کشتیرانی روسیه را رقم زد. نیروهای سامانه‌های بدون‌سرنشین اوکراین اعلام کردند که در بازه زمانی ۶ تا ۱۴ ژوئیه، به ۱۱۶ شناور روسی حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68087" target="_blank">📅 17:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68086">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=vTFNq_q4K7vksDeObCi2i1k4egUmnNM7X9eYk9qHo-S-8RQ6bYy6xkQEMeuXbAj84ibyNpMrwi5y8XJtC08Rbf0eZoU_Sg_Oct253o24DQATh1H0l9gndDuOWZ7ZYBs5RrIKqYuCPcjwYnmVJAsmE5pklu7RbAwq3GsmUqIOHiGho9C0aZacz8Q56hnwmoQANHhOoVm-m3F4hh0kgRTvoPGdko-K2uqeKPSwOZl_7ZzdSir8pQprvUX6TOe99KnzV-XsbT9mDwglUqA53C_SgyB9rSVQpRIhknTHzv_ngTGJrySG1TC2C4n2bVsmSmKgrqlSeKftWD2UwPdrDFoVRnXtZNJ8XXW4rujFiVFx28wWRCV3_mrQ_pOuNysqiVmmO1v4wfvzmcQFaK8k4Zb2OiYtG4dDswxAwZxNEEpuxprp2WaN82Heo-CSospRrwxG0yj88Fvx7m3l7mINPWtAo9JuWLRRVRqelp-fl4mg3C9HOGTNILxBsLpg37QPFw8JElW6f8axWXZDdTD6sCyXEdpzYsgD_NrR1dqhzmSZBTFVq5gQ7-q6oZ3-g0TzuyRvPxp_TwBSFE_daibx2lk870fiXr5fW3IHC6K6dQxZvvFrmGknS3K4jZmcSQmMkDCAtx_erhf8dbXP-DgOke4xMrYJIiAvkG24zekXbfeIP-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc10f2868.mp4?token=vTFNq_q4K7vksDeObCi2i1k4egUmnNM7X9eYk9qHo-S-8RQ6bYy6xkQEMeuXbAj84ibyNpMrwi5y8XJtC08Rbf0eZoU_Sg_Oct253o24DQATh1H0l9gndDuOWZ7ZYBs5RrIKqYuCPcjwYnmVJAsmE5pklu7RbAwq3GsmUqIOHiGho9C0aZacz8Q56hnwmoQANHhOoVm-m3F4hh0kgRTvoPGdko-K2uqeKPSwOZl_7ZzdSir8pQprvUX6TOe99KnzV-XsbT9mDwglUqA53C_SgyB9rSVQpRIhknTHzv_ngTGJrySG1TC2C4n2bVsmSmKgrqlSeKftWD2UwPdrDFoVRnXtZNJ8XXW4rujFiVFx28wWRCV3_mrQ_pOuNysqiVmmO1v4wfvzmcQFaK8k4Zb2OiYtG4dDswxAwZxNEEpuxprp2WaN82Heo-CSospRrwxG0yj88Fvx7m3l7mINPWtAo9JuWLRRVRqelp-fl4mg3C9HOGTNILxBsLpg37QPFw8JElW6f8axWXZDdTD6sCyXEdpzYsgD_NrR1dqhzmSZBTFVq5gQ7-q6oZ3-g0TzuyRvPxp_TwBSFE_daibx2lk870fiXr5fW3IHC6K6dQxZvvFrmGknS3K4jZmcSQmMkDCAtx_erhf8dbXP-DgOke4xMrYJIiAvkG24zekXbfeIP-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بخشی از مستند "عمامه صورتی" که در سال ۱۴۰۲ تولید شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68086" target="_blank">📅 17:03 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68085">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=e08Zw4Q97OAQWK8Qj2baUHF9Ulmkb3ipMWAlk4PJRP9uKTCLuoPVzZpWlkvtJCIux_PA5wv2ebHPyzTWCYaTXAZMPJBrFtmHAPfl-l1vorSa6ix9Gb2XGdu1__Aw1CYBGD5-wXUd7nJgWzKQd9tqFWYVdyYKcfYWK9w3FaTCqmEaE-wqvFTTFRhb-JkvfJspqhzvNA76ZDYL7LTHJHeqTFAsJ2ZurclqbBOk6F8vet-Xeey3y7W190Sy7As0nxiBkdEn0J505QwuGzQMvpgFSf8h5FdgBlzeAyrqAlmg_C6zmJh4nM209_yVpkyqgZ8sHdco43Ku-drWZgpwSKJePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3a6a36a19.mp4?token=e08Zw4Q97OAQWK8Qj2baUHF9Ulmkb3ipMWAlk4PJRP9uKTCLuoPVzZpWlkvtJCIux_PA5wv2ebHPyzTWCYaTXAZMPJBrFtmHAPfl-l1vorSa6ix9Gb2XGdu1__Aw1CYBGD5-wXUd7nJgWzKQd9tqFWYVdyYKcfYWK9w3FaTCqmEaE-wqvFTTFRhb-JkvfJspqhzvNA76ZDYL7LTHJHeqTFAsJ2ZurclqbBOk6F8vet-Xeey3y7W190Sy7As0nxiBkdEn0J505QwuGzQMvpgFSf8h5FdgBlzeAyrqAlmg_C6zmJh4nM209_yVpkyqgZ8sHdco43Ku-drWZgpwSKJePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
سنتکام ویدیو ای از حملات به ایران در طول شب منتشر کرد.
در اواسط ویدیو نشان میدهد که لانچرها در فضای باز هدف قرار میگیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68085" target="_blank">📅 16:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68084">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTeGLYcQf8LLf8hplBaK3tEN-qUs-kbhaxid-Vy8WXVzIi9WGA_kuKd5R4Psa1Mrj87DGoq0hhXphaDVa1sDxGG2RCq_kv0qRluTWW0F3IzW2WRfsBB2cHegjdVnhXOsYwE2XFNB8q5FnmJRCEREU6CrGRO1UFKJXn8pSlKf-iaoJe9CFI1sp5d0RZXVZCFCKZLGvEosyWPN6glF73y3MtLEGQM5dXjgyk4LwCcPKKGgiPH4UDOXLf6tlI2SuU_R8eA63_JoS6G1haqLbYdN55d6skexrAhoohFPhK9NFgNDM7wtqfDQz5GddByhuzjL7hk616kQ-mQnL3o9M-62OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
دیکتاتور قالیباف
؛
سید محمود نبویان نائب رئیس کمیسیون امنیت ملی مجلس و ابراهیم عزیزی سخنگوی کمیسیون را که از مخالفان سرسخت توافق بودند از هیأت رئیسه کمیسیون امنیت ملی حذف کرد.
عباس مقتدایی نماینده اصفهان و از حامیان دوآتشه عراقچی به عنوان نایب رئیس اول و حسن قشقاوی از دیپلماتهای حامی برجام به عنوان سخنگوی این کمیسیون انتخاب شدند
.
بهنام سعیدی از نمایندگان نزدیک به قالیباف و یعقوب رضازاده نماینده سلماس که اخیرا در مناظره‌ای با ثابتی از توافق با امریکا حمایت کرده بود نیز به عنوان دبیران اول و دوم این کمیسیون انتخاب شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68084" target="_blank">📅 15:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68083">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=QDMcYNh0Tu7wOvHxxKp4xUNTbB4PUzCrgyOMGI4bwGm77ZxwKHGN3BaMvRVJrA1kgLgXhvN_lG4YSqaokSxcGqo_Wpo35a6p2BmxqO3xh6SQxAGBBbuSfYTuM6-kCsEzEYIwYcAJETXMmvIEUmjGEJVeMaJWN-3Uxcco6QV58kVyPEnw8kQPT9hVUoCUQe3CCdLYKbxZWGu89DmfOCsfExS_Q3Hp0Zf-TcJv_9ontsFyzcIsi_62P4-FwxxEN3CQ4hKGOCt4fcVWJJPKQ8xq6ElsNtcWDvmwmAoc1Wp8M2C8A_V8CPmTjp7HDuOHqgb1S1nPlA9CLBsNG5Le54XiYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311dccf46f.mp4?token=QDMcYNh0Tu7wOvHxxKp4xUNTbB4PUzCrgyOMGI4bwGm77ZxwKHGN3BaMvRVJrA1kgLgXhvN_lG4YSqaokSxcGqo_Wpo35a6p2BmxqO3xh6SQxAGBBbuSfYTuM6-kCsEzEYIwYcAJETXMmvIEUmjGEJVeMaJWN-3Uxcco6QV58kVyPEnw8kQPT9hVUoCUQe3CCdLYKbxZWGu89DmfOCsfExS_Q3Hp0Zf-TcJv_9ontsFyzcIsi_62P4-FwxxEN3CQ4hKGOCt4fcVWJJPKQ8xq6ElsNtcWDvmwmAoc1Wp8M2C8A_V8CPmTjp7HDuOHqgb1S1nPlA9CLBsNG5Le54XiYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده(سنتکام):
ملوانان آمریکایی بر روی ناو «یو‌اس‌اس جورج اچ. دابلیو. بوش» (CVN 77) عملیات پروازی انجام می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68083" target="_blank">📅 15:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68082">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaG7scSmIhYYCmYosIzyDEB9JL1J7DC29k1VesicZ25iqCzhQrI5AIOdijSGVudU5uvSFbOskjHYktES-kGKL--xIrTtPbcZRTZsDFe7DCcjaoYIzoQ_9gosjs9Tk36dkdQbdAlL-EyxvXw6XfuALia6gyqqXmVFm__UkDP7niSgbTFfcaL17piYhoU-pBSNkUJaq6o8c_AWbe_CjaMj0vQzoUryqN9YjNEjyGDLTmVfM9JytOflbVTVRUx53tMwUOmmqOORPwiIPxtFe-aHVH7oVSM3lmMtMhySfHaV1cz8_nq3gohnp9OBnaA6CkPPAfp-f6_4gSyO_BYaI5n7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لبنان و اسرائیل مذاکرات خود را در رم از سر گرفتند؛ در حالی که لبنان به پیشرفت در جهت عقب‌نشینی ارتش اسرائیل و اسرائیل به پیشرفت در جهت خلع سلاح حزب‌الله امید دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68082" target="_blank">📅 14:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68081">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=iaV9LPKet66QMrzKd4Mb5roxIi-IqHzUqP3fSP0CSRqw0b_Wu0eF-__dPGvOZwE4jbxgyc_j-8443Jc5JcWc9s5_b-yyhUfQ0Oqf-REd_ZRJAT4TOPi0B0OkRdkisgHBAx0emWGKzK1Xy6Uwpg_5yzD-hm4jhEGSVz0V-_sN0YBpywcrohclqcm5YdZqzGrzwtUEl_vJP3fvcDoFQHlkDrqPynQpjeaWng_4d1lkONXmMlhEBjkUOpoCwYrKaWZF27Lmbd_LkzcD0GbyCie0veAsHOePoas1BI_eeEGqGDJh7GxDrflF8ss8mO6bQxfaTNMrI2dAHqTufzLJkCa_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fec092b37.mp4?token=iaV9LPKet66QMrzKd4Mb5roxIi-IqHzUqP3fSP0CSRqw0b_Wu0eF-__dPGvOZwE4jbxgyc_j-8443Jc5JcWc9s5_b-yyhUfQ0Oqf-REd_ZRJAT4TOPi0B0OkRdkisgHBAx0emWGKzK1Xy6Uwpg_5yzD-hm4jhEGSVz0V-_sN0YBpywcrohclqcm5YdZqzGrzwtUEl_vJP3fvcDoFQHlkDrqPynQpjeaWng_4d1lkONXmMlhEBjkUOpoCwYrKaWZF27Lmbd_LkzcD0GbyCie0veAsHOePoas1BI_eeEGqGDJh7GxDrflF8ss8mO6bQxfaTNMrI2dAHqTufzLJkCa_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:  اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد. در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68081" target="_blank">📅 13:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68080">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
معاون استاندار بوشهر:
چهار نقطه در شهر بوشهر مورد اصابت بمباران آمریکا قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68080" target="_blank">📅 13:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68079">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcTjBTRaT5QSoR331OM0URDTrXi7vZ7HgMBA37BVbdJDGID-Hmz5H_WMFN8Cb8xR9XOjyBL5zA4XVmPRRYHJ9gYxRAmcFPvPXjhsb-q7S8QIcM3zr7_n5xGWKmxkkiuwPWiLyaHlRzSns8N8xQCzM6_f5KnLXlNf1TPzcxO11OmabCymdAiNL8PR5QnxNfQb3shQ5cTXVCUscbhLG_2qGXdlmj8MeUlLBYZyVyeJ7hcYtPxzmiAUbttyM8N1OhsCWlnCNGk0uRFmNzYQ6UJi4qbHLfRtw4nGAFnGFvrFelEAZbdH0XPOKS4H0YxKL4aUkgcDlIypWsrKJQGJwBW4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
نمایی دیگر از بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68079" target="_blank">📅 13:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68078">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ne-tHI1KKOSXUG8Qav2-b9GZ9btGsWlyw7CE4j07iTp0crPPXYqnuwq2HqAHaNl-Adh0aoJ1qKuwIV8KKoqwK7U7rZqyh9rAC57v3K5RF_XWgi2TN-_-0RH1G9Ve-OKh3k0fXqQ5E5sbSsjbB_sd2QCm95s1E1G9I7D7f3RVAPqa32FH8MNx7XHgT_P9vQo3vjp7ngXhf7hYHp39f2Ox90L8ZEruDn6TLYzlc34RikXfsLXVdaPHoFiO4zbYwWijmR03ir1Y-xzGizgFPZrlOE7E80PDyxWa8WU0--9wpA_oPYa3VnJA8qeFguoRlkf-rWgj5wWilhCRS4jaFQdqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر  @News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68078" target="_blank">📅 12:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68077">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
سه انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/68077" target="_blank">📅 12:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68076">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🚨
پنج انفجار در بندرعباس
@News_hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68076" target="_blank">📅 12:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید در بحرین
@News_hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68075" target="_blank">📅 12:47 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
#مهم؛ گزارش های اولیه و #غیررسمی از حمله سپاه به سفارت اسرائیل در بحرین  @News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68074" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🚨
#مهم
؛ گزارش های اولیه و
#غیررسمی
از حمله سپاه به سفارت اسرائیل در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68073" target="_blank">📅 12:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68072">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=lr6kUBrfcgMlPd4Gn01bzoP9MXQR_n_Fu-mkO-Eej8JaKe6N3NAwnvQqoMhgB4I-cgNs4dfDW_R5la3HCqTlTvOo6KqcJwcN-ODbBbRJcCx4ZMCQ6UHINYZ98qonWlHDOPr1SzWXcQMh1iGYKOcjvR-paq-kgvDNeFDuTfTgJj6tu-P16cIzPFDwCprxvli3OF9qhebEE9LHuwFBV6-3lgDlu-VKk2O5DsGsPGAJsfPEkkHsmk8Puh-uwE2IKDXnh7KH1uelhiM3skb2fOloyEa7ekFd1FLaRfAMendmH8ZHsG9BaXC6IQPzoZFWa7Fo3hYNRm9zvAJZy4xE_kWYPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e106612ba.mp4?token=lr6kUBrfcgMlPd4Gn01bzoP9MXQR_n_Fu-mkO-Eej8JaKe6N3NAwnvQqoMhgB4I-cgNs4dfDW_R5la3HCqTlTvOo6KqcJwcN-ODbBbRJcCx4ZMCQ6UHINYZ98qonWlHDOPr1SzWXcQMh1iGYKOcjvR-paq-kgvDNeFDuTfTgJj6tu-P16cIzPFDwCprxvli3OF9qhebEE9LHuwFBV6-3lgDlu-VKk2O5DsGsPGAJsfPEkkHsmk8Puh-uwE2IKDXnh7KH1uelhiM3skb2fOloyEa7ekFd1FLaRfAMendmH8ZHsG9BaXC6IQPzoZFWa7Fo3hYNRm9zvAJZy4xE_kWYPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداسیما داشت خلاصه‌ی یه سریال رو پخش میکرد که تو یه تیکش اگه فقط صدارو گوش کنید، فکرمیکنید صداسیما در حال پخش پورنه:
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/68072" target="_blank">📅 12:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68071">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=vkbhI2cx7nWp1JQoLkaiMBU_E7H4xnAISZt0qj0smDweyYm4blmgnGjfBFrNXYXoSxvQBvTnvyAwItHbQpJiv164ARYvU2aUXs6bBGkNVME542VIqgNElG2pwz-OHn31qPZCZdXKy919lXnrBFIpO5hmXq8OV3rL1M8HctDLfLXVuI1m24tDHdBLAXAZ51zAoXBIBxf_bmwc8hnh3BBI0J-vENdFdboEdSceHlqCMseXYOj12S_UIfS0hjQM9zI7pcn2WngzjSHiEqKv9UQacoFc6CX0cWKdQQxHafj5OttjZX477Joo09dPbV2x4UekgJiB4ZXAokYHzFhAozT9yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0c3704c1a.mp4?token=vkbhI2cx7nWp1JQoLkaiMBU_E7H4xnAISZt0qj0smDweyYm4blmgnGjfBFrNXYXoSxvQBvTnvyAwItHbQpJiv164ARYvU2aUXs6bBGkNVME542VIqgNElG2pwz-OHn31qPZCZdXKy919lXnrBFIpO5hmXq8OV3rL1M8HctDLfLXVuI1m24tDHdBLAXAZ51zAoXBIBxf_bmwc8hnh3BBI0J-vENdFdboEdSceHlqCMseXYOj12S_UIfS0hjQM9zI7pcn2WngzjSHiEqKv9UQacoFc6CX0cWKdQQxHafj5OttjZX477Joo09dPbV2x4UekgJiB4ZXAokYHzFhAozT9yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
چمران رئیس شورای شهر تهران به سوالی درباره قطعی برق بدون اطلاع قبلی:
اگر می‌دانستید دو روز پیش چه تعداد تاسیسات برقی را زدند دیگر این سوال را نمی‌کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68071" target="_blank">📅 11:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68070">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI4TP77tw3zm86Yo2TwsbXgKlqDvt3PWUVURscz4TdSqzcdfh8GW8ZvCJtHK4UwC6m7M52ZMjw8qg3htXF3vYvgtrGBSsYmkrw8823JdVJfIOHEoL1yuu-qWNuluj6uBhP8ezISBcy_EAoqcQlnWmPgJfQHEQauFv5Zn-cjrPzlHXpDg08b7uFCU45OYsdluMYC_jdYVUHXfx_iEslp4lyn_KC_GaBe7soWdyvNQqBz9AQUyTo1Fmodwt7akpF7avtqLlQ-kj9HwP3ihq4uYIlCQ0kYhkKoRjDbebVC5MPDpHgCxZMHXFQiOLoCgpZDDiLdQqbC-DOibBXQkJX_Ibg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی بریتانیا:
گزارشی از یک حادثه در فاصله ۱۳ مایل دریایی جنوب شرقی لیماه، عمان، دریافت کردیم
یک نفتکش گزارش داده است که هنگام تردد در مسیر جنوبی به سمت خارج، مورد اصابت موشک قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68070" target="_blank">📅 11:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68069">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=UX99kL79NN3s0rYmHHQj78y1A09G-blzBju3DUbvV1I5TWHFyi6tMzVE45c33ticJ5DAO1-eny8IOXGB6MzVHVLUBe4rmQ1ZEwMsCNK1lzspiZZP2Viu7X48-tGKD0OOlJRmjf4ZtZVCmfsF3JjqYpOOW01cekJ9AlgkRAqHSaQQaskxPIPXYARJwqH9E_Xa8LgRr33VEmpxqizBm8Nauk_9ysDzpzJWSKBGQaxXgqexg62Gg8IbxOjJFPE_Y8uiAZak-wzqXwOP5pCoVmm28Jek4Ua9EvwgIs7ubPbjZgirhrUZrVan5zr1pMdnEUTp50PL9LmHJf4RdOQurlnWmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cbe780cf.mp4?token=UX99kL79NN3s0rYmHHQj78y1A09G-blzBju3DUbvV1I5TWHFyi6tMzVE45c33ticJ5DAO1-eny8IOXGB6MzVHVLUBe4rmQ1ZEwMsCNK1lzspiZZP2Viu7X48-tGKD0OOlJRmjf4ZtZVCmfsF3JjqYpOOW01cekJ9AlgkRAqHSaQQaskxPIPXYARJwqH9E_Xa8LgRr33VEmpxqizBm8Nauk_9ysDzpzJWSKBGQaxXgqexg62Gg8IbxOjJFPE_Y8uiAZak-wzqXwOP5pCoVmm28Jek4Ua9EvwgIs7ubPbjZgirhrUZrVan5zr1pMdnEUTp50PL9LmHJf4RdOQurlnWmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراد ویسی،تحلیلگر ارشد اینترنشنال:
چشم انداز موجود تشدید جنگه،پاکستانم دیگه نمیتونه بین ایران و آمریکا میانجیگری کنه.
جنگ سوم بین دو کشور تو روزای آینده شروع میشه.
اگه اسرائیلم وارد بشه یه لایه دیگه از سران جمهوری اسلامی رو حذف میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68069" target="_blank">📅 11:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68068">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7Crtt0lLG3rwh_eBuzhdt-6nhc_-Jhy5EzMlkISHghZ4gBUOp-1FeHJFTCByIb-audNONY5ysdJJ6a4xNcESy6ueRUPyzFmeRjCaUmFdQ9tS3icv6dGEY8n3rO7ad_n7jjM9gn4lUgNa9zCZS9qU7vgXlF6hT1yt8lRb7FjZmHCJN79cmni5SJba5nOeDEOMPO98DE1K8cokZApexcLlLNG4zWIDZe8aSWIFgRjqTgR4Z2VCYuUKVgubxffb5zpL21w3kler5LLm5wILlS4E3HsIBepNQRxqkb2IPzX24hvRdoPdHr9PnWIyvvXoGLsfQ0A6BtsKBQ5-IN5AfWwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده:
تامپا، فلوریدا — فرماندهی مرکزی ایالات متحده (سنتکام) آخرین موج حملات علیه ایران را در ساعت ۱۰:۱۵ شب (به وقت شرقی) روز ۱۳ ژوئیه به پایان رساند.
در جریان این عملیات پنج‌ساعته، نیروهای آمریکایی با هدف تضعیف بیشتر توانایی ایران در حمله به کشتی‌های تجاری، با موفقیت به اهداف نظامی در نقاط مختلف ایران از جمله بوشهر، چابهار، جاسک، کنارک، ابوموسی و بندرعباس حمله کردند.
نیروهای سنتکام برای هدف قرار دادن سامانه‌های پدافند ساحلی، سایت‌های موشکی و پهپادی و توانمندی‌های دریایی ایران، از مهمات دقیق‌زن استفاده کردند.
در حال حاضر بیش از ۵۰ هزار نیروی نظامی ایالات متحده در سراسر خاورمیانه مستقر هستند.
نیروهای آمریکایی همچنان هوشیار، دارای توان رزمی مرگبار و آماده‌به‌کار باقی مانده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/68068" target="_blank">📅 10:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68067">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=A5jx_u1XdAMaSFVvroTUzdRCjS0hDY9NlmVJvHksMsA93W9kTMpqT8ngyr6rLGi44xjLmlSEOnzlWvZVE0P-cOT--Rv6onpch26pLH92T8mj87vPiMo2M5TGC-xUJITzhT8Uen5NBbbVcslXLQzx9-DPadPG7FiHk0A5rVrQBWKKwA2zeTY7QKpvd_0qtqSZ_Slo-ffsyxwcSPj091ILEl7k-7l6FhxdH2agx7c77yLlAzjKdyi381-zRSNU1VWbqOXjubAjDG_v4a2tT-XWeX2lD0xAqHbg2gz14ZCDvZWZvOno8_6sc9BsgOU3Df_s6qFIP1CEQfQXf21EgE5hHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85107a3e8c.mp4?token=A5jx_u1XdAMaSFVvroTUzdRCjS0hDY9NlmVJvHksMsA93W9kTMpqT8ngyr6rLGi44xjLmlSEOnzlWvZVE0P-cOT--Rv6onpch26pLH92T8mj87vPiMo2M5TGC-xUJITzhT8Uen5NBbbVcslXLQzx9-DPadPG7FiHk0A5rVrQBWKKwA2zeTY7QKpvd_0qtqSZ_Slo-ffsyxwcSPj091ILEl7k-7l6FhxdH2agx7c77yLlAzjKdyi381-zRSNU1VWbqOXjubAjDG_v4a2tT-XWeX2lD0xAqHbg2gz14ZCDvZWZvOno8_6sc9BsgOU3Df_s6qFIP1CEQfQXf21EgE5hHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اخطار پلمب، مانکنت نامتعارفه !!
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/68067" target="_blank">📅 10:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68066">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSGoWtZ1Lj9sASXmLUEsJ7Tfm81YrbDiL1FgyvU_7dyOovW-a7HKt3T6l4gioSvY7s_j4Vl-5V0YVYbfh9ASeUoxLGGdegOK6rh0b8W2gcdw9hBb28LKtt2autAh5O7PIDjP6IVpmKq5HZDUZmYtWoeTmbdO6JsEBJ8aRY08EbtPvxwfDD2Sr4FI1HBhcwrSBa2clgqXLunlSLRbjVajjjTwE_0Xl5Q6D3pKZ5lwE-b0AzMTmJ5-Y5gd9DVvykIcug-1P_3WUGG8dxU16QEP_Ub3cG_vEumLBHNhIQeICC_W_jD9O-6lFa56BkG-U4z7BWPddj6taVk0lawX9OCMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‏بر اساس گزارش نیویورک تایمز:
اسرائیل سال‌ها تلاش کرده بود محمود احمدی‌نژاد، رئیس‌جمهور پیشین ایران، را به‌عنوان یک منبع اطلاعاتی بالقوه و همچنین گزینه‌ای برای رهبری ایران پس از تغییر حکومت پرورش دهد.
در چارچوب این تلاش، مأموران اطلاعاتی اسرائیل در سفرهای خارجی، از جمله در مجارستان، با احمدی‌نژاد دیدارهای محرمانه‌ای برگزار کردند و از رویدادهای دانشگاهی به‌عنوان پوشش این ملاقات‌ها استفاده کردند.
این طرح در جریان جنگ ایران و اسرائیل در سال ۲۰۲۶ به اوج خود رسید؛ زمانی که مأموران موساد پس از حمله هوایی اسرائیل به محل اقامت احمدی‌نژاد در تهران، او را از آنجا خارج کرده و به یک خانه امن در داخل ایران منتقل کردند. این اقدام بخشی از یک عملیات گسترده‌تر برای تغییر حکومت بود.
این عملیات در نهایت ناکام ماند، زیرا احمدی‌نژاد تحت شرایطی نامشخص خانه امن را ترک کرد.
به گفته مقام‌های ایرانی، او اکنون پس از آنکه مقامات از تماس‌های ادعایی‌اش با اسرائیل مطلع شدند، در حصر خانگی قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/68066" target="_blank">📅 09:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68065">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5SbpA5G99b1rDI4cq2itCvn6lGvyYlW9dzM-LOU_ePbmD1QJMFQ2DW9Br4E1FDZ4NXFpQx7r4Pq9aMq5O5LrFKORUSYJDsWGT7U6B8T3fS2mpAoQQuI5gq2bdHh_xOdPC4sjEEol8hGT48tXuXaGxP2E2U4UoCkhZ1cuUOfmh0e3j-jlzWJsQ5JZHWIAjEMfmjytKTkoC3hK68gZ6UMJWgd9wNjTF9ROXR-R0N3C7rc7nzjMr_gijhyKiXIUcobSHQ6i4KAI-CL2ryoIDzjqZUtR5U0odSVPG-YQVkzkeKwjej5Opo7D2MfIG1BE_ryUYiWOUZbfocnrMZXqk4bTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
وین ریت 80٪
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇳🇴
وین شد
✅
🇦🇷
⚔️
🇨🇭
وین شد
✅
حالا هم دو تیم فینالیست مشخص و در کانال تلگراممون اطلاع رسانی شده
⏳
🇪🇸
⚔️
🇫🇷
‌
󐁢󐁥󐁮󐁧󐁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
t.me/bet__gg</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/68065" target="_blank">📅 03:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68064">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=rgCgCJnCtopqlEh3Ii41IOC3vZuyDoQJgdVHiFVmWLL5SjiTA4nPFJzxkSLwr-eITqFS28HDynICcJAnBNnzxo4zqYhgXP78A_Lea9ki2FOwbZRTBT1dteKYhmG8ilGRD4nNlIBt8uFAsgCD-CCeQCsjtgWN_8LwHarN-rzrL6GzqZy7VDFnviKpDnQwrDrLwjF0ojYdr3fDL-1DvhlXwYJ-705A6UytLMoAYpBx7UJCkwatktHIi3KbNSYSijBhmfYqoMUvr2X_XWurHIPcu7jbtPECvM5UbP8MOIzk-GzlFLgSnpAXPbXttH2E-mh3CTOwb5fc4gwrtclbEfQ2xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff9948d46.mp4?token=rgCgCJnCtopqlEh3Ii41IOC3vZuyDoQJgdVHiFVmWLL5SjiTA4nPFJzxkSLwr-eITqFS28HDynICcJAnBNnzxo4zqYhgXP78A_Lea9ki2FOwbZRTBT1dteKYhmG8ilGRD4nNlIBt8uFAsgCD-CCeQCsjtgWN_8LwHarN-rzrL6GzqZy7VDFnviKpDnQwrDrLwjF0ojYdr3fDL-1DvhlXwYJ-705A6UytLMoAYpBx7UJCkwatktHIi3KbNSYSijBhmfYqoMUvr2X_XWurHIPcu7jbtPECvM5UbP8MOIzk-GzlFLgSnpAXPbXttH2E-mh3CTOwb5fc4gwrtclbEfQ2xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدیو ای از حمله امشب آمریکا به بندر‌عباس
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68064" target="_blank">📅 02:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68063">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DlvOC33nnzW36gyRdOgqt5WvcQofsKGZQjZIzjzPeZGADA7b2rug7suLroNoZul21U9IQ6IsNMfuUHFMkBZBUWIwyjGNv0jzZ-KltWr--YBRWCbP_nh-Qjk0rP7TraYmZ3ZMa2IPeIbHUdcx-ME6rqfLs_1_CX614-Q-apTP2ywV5MtZmruFNxjAODiCKeAhv6Wy6lNYZiadHtqOY5g-k1HLofML5VhXSCx9mMVna4iItAJsqQW_qblPd24H6tKw6v1aS_4x-H75a6CQ6Ncu81sPh2c05WDe6SWQ1Ke1-9vnl6Csfo0ljpulZCEC1_jKRT7KSsjXVP5IwWzvM3P4Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75534f5fa6.mp4?token=DlvOC33nnzW36gyRdOgqt5WvcQofsKGZQjZIzjzPeZGADA7b2rug7suLroNoZul21U9IQ6IsNMfuUHFMkBZBUWIwyjGNv0jzZ-KltWr--YBRWCbP_nh-Qjk0rP7TraYmZ3ZMa2IPeIbHUdcx-ME6rqfLs_1_CX614-Q-apTP2ywV5MtZmruFNxjAODiCKeAhv6Wy6lNYZiadHtqOY5g-k1HLofML5VhXSCx9mMVna4iItAJsqQW_qblPd24H6tKw6v1aS_4x-H75a6CQ6Ncu81sPh2c05WDe6SWQ1Ke1-9vnl6Csfo0ljpulZCEC1_jKRT7KSsjXVP5IwWzvM3P4Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
انفجار سراوان سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68063" target="_blank">📅 02:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68062">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
انفجار امیدیه
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68062" target="_blank">📅 02:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68061">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
حمله به سپاهِ سراوان در سیستان و بلوچستان
@News_hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68061" target="_blank">📅 02:42 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
