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
<img src="https://cdn4.telesco.pe/file/injPJ0msUHQK2sQJ5CHZdNuy4qxVxr3UZPUw_sZXZdx-rRSCltrl4ZSegl0zLgutHRjM3eTn_xm6QlezEUqiujXkZFn3TnzBTKd3xsDTRNjYvDRT5iQqfY41gUKQfqOpvk3SNisFzLHBtGPAfq9dv4bgMERmW3NIOF_kBp0jo7hCZhbO6UFjT_t1KB7QMrax_AEk5e-EO3geUJkkLwWUMf7sBbdYZi8WB0_flLBRUxJmJHz4CjHpuOec1D54oPYKb_nYbFxJoepylMtumPBc6ZFO30EFz-M1krDSkTEtsa6PJ4U3z0uZq0jgz5sSLqJTuRHRm0Azyqd6yvOGff2HBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 464K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتارتباط با ما:@ads_Persianaaهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-23 01:19:55</div>
<hr>

<div class="tg-post" id="msg-31589">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBYF16d-sbAPoAwnHle4uealeQTz14ltDESa7oulS5MLcuJ5ngoYxEsYHUnGTtUIYPtzxXcoyG6Wfu120aHw4gbgrTIjB1CWLjYN07MUxjb053_h5eaOPJi1sXxUL9JJ4uJhKa37QU0rANzbnQN_95BdH7J_IwwQAvCJQ3DaBkbeeCeNdslNLfB098wVIfjMhFkbDiy6bDP6X1qXwS_04A5hRg6PscJJ2pOJT3yo-y4X0v99zmu1UohB8E8B2vsYh7ORAVef1Xh3nzjIfH8533mxqsm07XF8yLa8-OybbNMUR0GLzfle-Prxp7QYdGjkFPpxUmcV7XIArXO_OkbWGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ از بازی یاران صیادمنش مقابل بایرلورکوزن تا مصاف روسونری با تیم اتریشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/31589" target="_blank">📅 01:15 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31588">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAuQuaZQ4ksqq1F4-Arh65b39KzBHT9IcRHxw414GTwDHBllMgVFAvjOeHsPcHUt1aXwsNrz9QKzBVj1u-ODAu543weGs50ZMqBb8CIuSIWFj2BIaGdElw1a2MSiboNwjwc5UgpdvCQp8BlLurCXDXsRlTVUqWGRjeYBd_7Pp4wsur758QsalTQA2wNnanQ97JdeQXdFEp_CCDTmslEXgDPc5K8zAboOZ-52pUY1XSQ11EY9EeoHr0wQVUY7D4cFEql-p65n_vQwKUpXGmWF1aPkkMcCkzHu6c540yaNWeD26jPib_QznkxAOF5ztO3y62z_jMe9JktKCRF42CBulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
ازبازگشت دیوانه‌وار رئالی‌ ها در رم تابرد ارزشمند یاران انریکه مقابل سیتیزن‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/persiana_Soccer/31588" target="_blank">📅 01:15 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31587">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r9SqDuZLcrDpVGSHjtCUJkLaJM-hjfBTs14OP1fec5wrQx7baF1EvN5hrf1wkgCsBXdKP_8x_kd_u6T8iSAnKVydcyCNPyd09wHWeI2gW5-5yUtqU1q5fTBx1Tiuz--YJnA8D5fR2SAFsDa85BZegLJRNkIm2KNln53GBO9E6ikKX2cVwgUArD2bLVEmYrUFZaKbOJ9QIma75vHuXKggXccKng8oyYNGAPrESaFIbW4MQbisyg0l9E_NZrBRPmoflhaQRp-T60ojyCSToixx3syPiJHCI6pKZ1_QHdjEpBhKUmfK47MuQSkLT2UHrwxjISrwJHgDQtpmKhsbaJdKYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدارهای مهم روز
پنج شنبه ۲۳ مهر
💥
بیشتر از ۴۰۰ آپشن پیش بینی برای هر بازی در بتگرام
✔️
شارژ حساب از طریق کارت بانکی،ووچر و ارزدیجیتال
✔️
۱۰۰٪ بونوس رایگان بر روی اولین واریز
✔️
۱۰٪ بونوس روزانه واریز رمز ارز
✔️
تا ۵ میلیون تومان بیمه شرط ویژه کاربران جدید
✔️
امکان فروش شرط های خود
⚡️
همین حالا ثبت‌ نام کنید و و از بونوس‌های ویژهٔ بتگرام بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/persiana_Soccer/31587" target="_blank">📅 01:15 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31586">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇪🇺
گل‌های‌دیدارفوق‌العاده‌تماشایی و مهیج امشب دو تیم آارس رم
🆚
رئال مادرید در لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/persiana_Soccer/31586" target="_blank">📅 00:42 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31585">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqtqMtb3-h0Fjy_qvaGfenWehldhZ1Jye9n6pMNpSQ0N5OUS0IjljOrdwc9SoF5zpXaq476TVICzcf4FM6VXfsqcdTSy3QyGGZXYssfLdtkBqLn7fsrCnJ_DmfMdBmOLHnKHvAUFGcQU777ABvopQ2Hgls5PsIO3MvoIkbmg7vfrqEzKqxu7ZeJVhpjdARhxlbMtYHCuVevFz_cQV6VBAWwtPyZDy7T6RvUyXHvZ1x4H5AaXdHRxZqLYqUsuEHSqaxXFlixZ2cSOKj3U5ThWX3T-8J1-vLRy65HLTb6HUslnuZYDbnWpU1Wy00XlWFOux-H3-hndgoJlUejoyTPYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های‌دیدارفوق‌العاده‌تماشایی و مهیج امشب دو تیم آارس رم
🆚
رئال مادرید در لیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/persiana_Soccer/31585" target="_blank">📅 00:41 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31584">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">✅
هفته دوم لیگ قهرمانان اروپا؛ پیروزی شیرین و جون آمیز شاگردان ژوزه مورینیو در دیداری خارج از خانه مقابل گرگ‌ها؛ رئالی‌ها بازی سه هیچ باخته رو چهار سه بردند و با دست پر به مادرید برگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/31584" target="_blank">📅 00:34 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31583">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtqIWbG-t93SklCBHVWZpQfuGV1uQ1YfTBHCVev4h_hun4hlAV3Kor3PS5PqzRb8H7gijEQorh7abIE3TnwWOsaoMjN8sdKj8m7rdtpntH-AVgL15inTc5BOm7-HzaDMBYxpU-63Sdd8-cH7hcq8qSyBa61TXPtTQXJJDpk1QSRY_mBisaZ56VQpBRl8jrnlT_tnpgYEaGZh_i2DvmwJjrgfrLa7WPN1S37RimhhqTeyoL8ePOXxIl4_dRS-8CSLPTAvLopJTtohN9XpIOWiULmmmfSJU3CwHd8Ihd65avJ_7leLtXc2Ct_aSUJUle5mC70Gv2VhjusE2Yn6Fr3Dpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ قهرمانان اروپا؛ پیروزی شیرین و جون آمیز شاگردان ژوزه مورینیو در دیداری خارج از خانه مقابل گرگ‌ها؛ رئالی‌ها بازی سه هیچ باخته رو چهار سه بردند و با دست پر به مادرید برگشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/31583" target="_blank">📅 00:31 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31582">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU-s50QPs9u07v4o6VTMiAKFrGYS95yCw789U6a1hh1fK49OVj7Wo2Ry1WrEuX4U-f1xz36M6u4jqHOIAG4p65BQphhv5a6qvvNo5urwKJc6YR6DDq5Bya4MeZv0_Z6mlNEU0Tl7XJf4m_ARB3PCDVAmcfU9q8drl4f1VyKRtamBjbgumIH_AvG1190uU6ubycv5WvOimv3KGCr0wx8H0Qsv222obrcUA6i_RgEAnpBZSAnICd6NIbeilj87mb_5wNPicD59tFc2ucTTG1RNlvb0MwoYe8htKyFS-6lBWDbOFS8udZaDf_n_p7WtcHQBo15xmBfH0Ks-ftMk60nx9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک‌ترکیب رئال مادرید برای دیدار مقابل آاس رم؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/31582" target="_blank">📅 00:27 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31581">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC_Pu9GQrK32hjE1p7LK9Rh8bdS0kfbPQ60APCRIiIqZh2UdtL9xjpJxGJo1-Rz5gOFA5u_m1cWHFNFwxNsNKcYGUXPrBgXVoTePJdzfUIPizFUUukwgumsKtQDoYDd3Bl2VrmaBjDIG_kiDvV0IsyaPchHJzNHpbBfnnKlXKD4JDR3LWG3ZIvI-O_NINZ-TJb8WwSXUGDExmkqnzzI80FWIrgs9pmXVh5k4XxY1VcQ34X0n188OeGZ9V0YqTpxT0gHBs3DDKBldAQhB-TTM6o4EFmebCZAKH9pBfeoixWMfxtWLVOy24JTk1pBlSpjZU0R-KliUjTaf_IwT3MGMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه گل گهر سیرجان رقم‌فروش مهدی‌گودرزی هافبک تهاجمی 22 ساله خود را 120 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/31581" target="_blank">📅 00:19 · 23 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31580">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtNwRpLAPUhzJx9BPfRaTZaed-sPGcqjd1BcZb3JMEKs6gI2tdmRibNYrC6Xa3DDcOCpONobm4-O8WSGuRF0nT7udR1P12TjSVdosKGrIrN9yovxPX6EIAcI5pKxmulXjNsGDy01C-CRcJV_YjBVEuvURkxIRRcgUjUPdi6ejskCtrifJwxG4Apx0Pp9tv33BbBQZDyJ8B1SCjXOEd4QbHLrWCbLfWb3hN7K2fiCPT8QeLg9ZsIPonIGaTAc2RIUhuMv6zdEzIPKBuZUAAcIs8H43F86P-pceXqo968bxUnoFGmfGRqnZd5EeAjrnvYRwVw0r-IYCh7ZNCCqBgu_7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت جدول سطح دوم ACL در پایان هفته دوم؛ شاگردان رحمتی باشکست دوگله مقابل نماینده بحرین عملا کارشون برای‌صعود به مرحله بعد سخت تر شد و خیلی‌بعیده بتونند به مرحله بعد صعود کنند. المحرق این فصل درلیگ‌دوازده تیمی در رتبه یازدهم جدول قرار داره امشب تونست دو گل به گل گهر زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/31580" target="_blank">📅 23:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31579">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnExZueVZnF151scc6osV-3ro_gvMTUCGbp9pWTDp76CDdJkiC2P10bBwYVLAM17YaCbsj0gdA3eABIPjlnRiGwkyzmeMljAR5VM4R7uoktXQOiMrjbD2H-S9YlKd8mGLwPhFwZomsw0zUaKkWZKtESPxAZln5PWNSapK5BNILHtdUJlsim0KGClqDVDHrBxfJI6hsbWT43ElyWGKe26djTWPcY1BTP-IPFOmrYDKeEouzqEJ4n7DfOmgOG_dpk0fgD1JjwOkjmCtg9rlRydJ5hLPfloqsUz_XDO2Lm0RqEIAfUC5c8K16YuzBcwegtC6OYZjAqjoKz8WLpQYhRXRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احتمال گران شدن ۴۰ درصدی اینترنت از امشب؛ بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت. همین رو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/31579" target="_blank">📅 23:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31578">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQt2vbdRqCPa_iAVs2-Z1OFtqoqO4OoK4RwfmTgxdOG6UGEU664zPSYEDo1SnVn80ZXLHE21dTjZNZbCifX1IPrPV1GsPv5xXtwmIJ0MESpRrZz4s_TZPpQFUBrCv6UsN0G__rOp0TEVR205B44AvDdGSB9oR3wtlxgb7eJalIRsDW9geEea4s43pWrmnWgj0t0YXj8ApPnOBJkJz5kD2jL_lAtlckYT_-hzKkUK8EBLPhW1reqL9r2-YNStjhZ3wEpMdD-vcCBSbV6228l8jIqQQ_Mdgw5dsx8jmnzo_ZTFwjx5lsMSsF3fGKFOzc0V7zqabVYUlCg8sdsblZ-K6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم چمپیونزلیگ؛ شماتیک ترکیب دو تیم منچسترسیتی
🆚
پاری‌سن ژرمن؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/31578" target="_blank">📅 23:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31577">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocGBluvYMogIvqEIR_qcK3snVLRFAtaH9NMRAEu_I6clKL8PBwRnvZFfvkgZUqCTXTzXDgv4mzEcS1mT5MZ-o5dJBgEWcYd3u7KL_VzNtw7MXf-ya2Bn3xzfSF_zmPQsYeR5tO51ZahNSW2BNNPkoew9-7DWdMuyHh4F3NYyWWqZ9sj5BMBI4LaCCHdv_4j_taxpXQboh7HmuweRDh_gzUFJJwNkjWqgGx66p1rPj3fDcpLWMgx8Yy21ltuYj5zIVfh-N0ffPrqOQDy46P_U-CHnt5qtCXhnscccA01viWDFAE1nSDjxbZ5T0FDuoBwMg2ahZM5epWBy0Q_uhRPyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
فرصت سوزی برگ ریزون و عجیب و غریب تیوی بیفوما ستاره‌پرسپولیس دربازی امروز با خیبر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/31577" target="_blank">📅 22:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31576">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199b3be53f.mp4?token=k6wAy8ITm67at2_cJfpiGisPVcKaJk-dEQnhx0j0-L0jhDrPqTzQkylJLkViW8-qJUwjjuUo3KEZx5P4zoGEfviRKuTmG5tq54kwykLh4_zJKeYnk0DiF_k8uIuu6YBTxwXgevBEBe122fxG5OzlfHgrtWVN6EBKFi-y8wn0vR_AP_TpFtnGAUpHrTp302AsmCTYTCzLwrXu4YD_TePvPCbxMpEhHjTVeAtFGn6Ww6LCGotGyWE9_e6u5VggBtC50mCOxrRjb7QMF8qap4GIELO3hU52UN2gItiY6Pnjinsxb9PIW2NV0282Pk314T9DpwOGCvUGqD9KtaHINHzbHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199b3be53f.mp4?token=k6wAy8ITm67at2_cJfpiGisPVcKaJk-dEQnhx0j0-L0jhDrPqTzQkylJLkViW8-qJUwjjuUo3KEZx5P4zoGEfviRKuTmG5tq54kwykLh4_zJKeYnk0DiF_k8uIuu6YBTxwXgevBEBe122fxG5OzlfHgrtWVN6EBKFi-y8wn0vR_AP_TpFtnGAUpHrTp302AsmCTYTCzLwrXu4YD_TePvPCbxMpEhHjTVeAtFGn6Ww6LCGotGyWE9_e6u5VggBtC50mCOxrRjb7QMF8qap4GIELO3hU52UN2gItiY6Pnjinsxb9PIW2NV0282Pk314T9DpwOGCvUGqD9KtaHINHzbHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول لیگ‌برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر خرم آباد
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/31576" target="_blank">📅 22:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31574">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUZ-VPvliVUW_TjaUF4GpTsIIilT_0L-kUp48LF7Co7PrRPXmsK6hkpaFV-NQHaEyASajU5OjpyHIqihltaymE8616jc81r03PrAKsyNz3Vmkm2cTXHE_UyjdA0kj6lIih81FELasV4-Cbvj6mmAaLL6w2Q5eCAH8x8tRx3Qqy2lT19rAlMJWlvf-peeIH7aF74b4d_-kfhZ3ZNpMN4Pr-hc4vfpHs3IpQYSwjlz-8Ol1e1cILUJTksVeqHdXODvHS9UEZ0k7339y1NgLmurI38eshcyQJtbk78DoHNR28ucn9uvKDXPyX7tudwfLS7qJSX0VFeJh4TrAzW2XK2t9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JoAo-ZDPaAQOPSvgO14kNXd7z4ly9ccp9sc04ZUQhlRCS18nKHof0x-iEPdodZFF99lnjnjfgq1O3upix0LLsyQBLnUzoytUssao3RG91phIuSze1tsd09uR4SmrwVw7Ty57lbTcPSXPxSZM0ut_GJjrLxTsOWPSogp2FgwQFGrT2l_P54B16wN435ZSE0CtVvvGQS2M5n_ZTcfOSu9c5FCOPErdslYSZpbHBx6iZelAZf-0AkkESPAOGdmm9P2t_S0yKG1Tv-KsTXpRzgcHhRz2nnzKM2q7iHCxDFLE-SP73f8iTq_ZdicPcEahCojfVGGMeFeLNB8UUX0XPR_5EA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک‌ترکیب رئال مادرید برای دیدار مقابل آاس رم؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/31574" target="_blank">📅 21:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31573">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg5tBOj1SG9CABWysSSmhBPNf_5p18wd7AivQa0Of6qi2weeNKRmcW1rU0vycptdRsRPks1x909lNjspmmnwAM8SWhTiY1Rrs5fMgKplX56pMTNCoQe7LfpK0CdvNGaQYSUpkNBOihrCv9x7lDXYHilFUxT2xN87iFmNd8zW1uPVErukfn_RYv7XPj9b0HWi0_Q34BwZUbLOjuL6mVZkTjGTaYKVtXfPIWk3qU2DioZmRFX3f51DmrKFeDL5jxi3jlpAj0lMU-0nSH4moTP89fAo2WVPBEV9Sq0HrHNc4fXR21eAgthNxZJVK8_Nx_zHDkc9MrEMwwPUH_hWZgvdLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
ترکیب منتخب تاریخ رقابت های لیگ قهرمانان اروپا از نگاه AI با حضور پر شمار بازیکنان رئال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/31573" target="_blank">📅 21:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31572">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec824b8766.mp4?token=KEo-3U4TwmJJHq-3wtTJbjPJfqDw_XcHYtGNqNqbeUePIl9Udtmb4_ycL4KzwDcGV31TNmsmgUvBF_ihFRcessdbp4i9PM9ulOGzWjWkIwQ7AHx1fRsjQGcq1WZJ4jrI3UdtKRi9w56VP4qESCYk1hZvpyQ2rSgL4zyGK7qSiutCyvhYkV6wynPSS6AqmDOUKtR4OYkfyKAStQftmdYo3XzsdNxsD_koviLlB3QpldNZuipOtQuddQvvOfdXhTqhUvaw_is0YTGFMbgCIdzetDvpxbrp81eAu3xNk2p7pYPt6ucBiZkoSBOziDqeVSApg1TSDRsCmgQuTsHApHOVWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec824b8766.mp4?token=KEo-3U4TwmJJHq-3wtTJbjPJfqDw_XcHYtGNqNqbeUePIl9Udtmb4_ycL4KzwDcGV31TNmsmgUvBF_ihFRcessdbp4i9PM9ulOGzWjWkIwQ7AHx1fRsjQGcq1WZJ4jrI3UdtKRi9w56VP4qESCYk1hZvpyQ2rSgL4zyGK7qSiutCyvhYkV6wynPSS6AqmDOUKtR4OYkfyKAStQftmdYo3XzsdNxsD_koviLlB3QpldNZuipOtQuddQvvOfdXhTqhUvaw_is0YTGFMbgCIdzetDvpxbrp81eAu3xNk2p7pYPt6ucBiZkoSBOziDqeVSApg1TSDRsCmgQuTsHApHOVWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
افتخارات آرین سلیمی و کوثر اساسه دو ملی پوش تکواندو ایران که اخیر باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/31572" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31571">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mquPEYfAFJ_5in1irh7jofU0bPzVJfsRpAy9qxr-J1vcZMzZbiifGG2ynhjRM3pNifupcgL_BQzzOH3BXpFgzNr_VN1S3qwRcyW_aq5UbadlZ3jUaMpTG7WftIKS_y2QU6irtK6-KfoPNRdn1NLhmO4UfWQC5PEH-p8Adalec3it-DfNYSBmf5YOC2gi6Vrxy3aVz717WXMISmO-Tyb-pvJupuwrb6vbEdpgRPgjV8EtVoZthpl5imE9InyCrPunjWh7ZPK2LCT4WbfHM1qhCdiS5C_0HWKVNMSsC4g5zNJsrgUB_BGhFQ_dDURP3Uip-3_P6wg4m5Z6rzKGs8VIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ستاره‌برزیلی رئال مادرید به دلیل کشیدن موهای سربازیکن ویارئال چهار جلسه از همراهی‌کهکشانی ها محروم شد. بدین ترتیب دیدار حساس سوم آبان ماه با بارسلونا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/31571" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31570">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMxttup6aLUhJjZ-NczjvvYtvUPndlYR6_oJFhoVZQDTZcuvto68Jkb-tuZ67NGFQh1U_5xlysGSWqes0NZvgqdFTKnZlbu6HUrRqCxXzpmpVrsPh0gC_5uf-UPhoG16HvsA6en4ZY6ougdIbix3D8trSrOJymu1lXIOtJ1Gb4OIdn6RLiTgsmsoSqfJuDpTDS8FhZxt83bMdw58j8KEitGE8yMp7Zu4bcrc8_R16n1yJ5s1vsCDtVQuOA4dDKUn3fU38BZlVan-p0l8l7PH-hpqGEQLWvxC4wGnoCP5MGpQfpAfHV9KArg06cwBce3qK2YkUeSF5-8OcgcbW1U3Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ قهرمانان اروپا
🇮🇹
آ.اس.رم
🆚
رئال مادرید
🇪🇸
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🛡
تا ۵ میلیون تومان بیمه شرط
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔹
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/31570" target="_blank">📅 21:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31569">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGfnbluMIHsNxRj5oVCLsCROQQ7bLb2fB2ujn9zIaNRKq5X-XRxoP0pPWzIKJh1dgSnd96X5euUV-z2uc2tAE7AGvVLlcsLN9l8kUEV-z39oJcalAq5RC81ILRh3ULrqqRbOeM_o8SCDM15iEngtaxlf-rz0uazaNKffjlyBsSyFoOYU8QafqsRPMnMyl-FQ05PvUDMrlALYJDLEdzyXI3CW-CXb6uEVy3mLVWqajWoHQDkZaKz43oqsqrzg7V3HY_1GzXPDmvo1bTKBgFYY3jFbpcOY4ii0cmefHBsq_ooqbxjB8hkVqRaCTm8BS6fzV3uUjNDRoZckqQ71aM5YJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ نشریه کوپه: باشگاه رئال مادرید به‌کارت قرمز وینیسیوس جونیور دربازی این هفته با ویارئال اعتراض کرده و امیدواره که محرومیت این بازیکن برای مسابقه الکلاسیکو آبانماه بخشیده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/31569" target="_blank">📅 20:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31568">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuguvMs9MXpigwRnbZGx4aTRRQgOv-vscXcFYMCFeKhvtz_VE_cLYAiItjK0OH9YIBy-XRJXNOsC5cAhtk1D6EuCQg8FpIxWMb2QXEjf396Xiui0WwM-O8U-sSp47H2H0o-Z-F-X0zXK_XLH8gsjcz1Ukv8Njyc-KhIMTmEhL0KZXud_lS0V35mik9JS_w-VcPhSH2h3MAtf75tcZcHZojmyikMzgCZ5DBfioaVYJmEs9B0-AVfIMRUmRcVIznvUOzuSF0g7ieggMMqMG_U_jOXBNdRsqped8Te2p4_YSTf6qSIcKId6CdNshXNVhwHLS-jH7TGhmQ7xiU-O1m531g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بهترین گلزنان تاریخ‌لیگ نخبگان؛
آسانی بالاتر از رونالدو و فیرمینو:ریاض‌محرز13گل؛ سالم الدوساری 12 گل؛ یاسر آسانی 11 گل؛ روبرتو فیرمینو 10 گل؛ کریستیانو رونالدو 9 گل؛ میلینکوویچ ساویچ 9 گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/31568" target="_blank">📅 20:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31567">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFb0tDyheyJGAQnAEk7nW1lTnTJviW9bPjZbJtMrE4Z8YYt7sgQ3DQEkj3br3SexoB14VPTiosm-Le50qJhGlf__FzWy1Gq-Ud_ycEswkFmv-ePa9_JqWf94cm-MQueismG1yzS4ruGdQdV30B3715RMmPJPPiOEwplF7-yCImqWEi9mjopRwlPlz5z3HlPufVQV2U5hT1L7oYGNMHlWeBMLN1pNTxBdW8iSCE96pFOy5pjQFj7tOnkBMLWiei-r-YvIaLJv6sCBwYp03GqS8rVy2EnG5AS5F4Z1_2yBz34BVhgFjjE9BjOAAwILNRaFnW-G1Wf19A7M6MsoF6g9oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرین سلیمی قهرمان ملی پوش تکواندو ایران در روز های اخیر با کوثر اساسه از قهرمانان تکواندوکار ایران که جفت‌شونم کرمانشاهی‌هستند ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/31567" target="_blank">📅 20:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31566">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfzSE39QO6BYjWNyilil9fx6uFIy6uZrQb7zB3yGFkxuAs3Ij2txQaxOzfdiVWZwB1kEwKMj2WOLOEyrZNXRw0reJ3LcSAhpJeSRTI0XOWx3rSmf0fX_9hTHMIY4dmucZ00vFYLedH_GGEL6c2xdewdAUUPA_fIamGRuqIa30xIqWW0_y8o8mO1fc3k6FPsRVKrlQb7GwtgSA0oN0Ug0xOLFsaltsjQUaeFolGYGVgcn9LEBoa29I8xX5ZLDoljO6RocZKiiDZYPcBmJdEoEgJ0J_PfZcR9aTUEJZdvaezUlDM7i5N4ZajcV0j10LOldoe3kIihOGf25K6qfoLF3zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه شش دیدار آینده استقلال و پرسپولیس در تمام مسابقات لیگ برتر و لیگ نخبگان آسیا 2027
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/31566" target="_blank">📅 20:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31565">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0UFbi3Xud3buUghAOBjM61aU7RZv1lACiSKusaayb6JWqfNEcNXCVrrveboliOlCS0dD0bLpXwEa04FI8ItnXZMPbjjJHObUri2p6n9QTrdFDe3AogxKVFjmg48F6XdHe3hjyqu2dAnJK0kmZ_1P7Ejx0EjCh6gb_JBoELDhR0ZLi9ZZLapnG1ZT-tn-pD3IWTggvtSIN8gIniYnaCNwIC1pYFaBrsREi5N0xduTTJiN3youoHjhVlV_XETSgjJbvuJrT1iOyAPHRd75iz-4FWt87fE6930WCf6whPh1SyNuQzq1ANnR7BLS5zbYwGIy3JSddM6LGlYi0RaPJ3n8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر خرم آباد
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/31565" target="_blank">📅 20:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31564">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmATrMNimuNQw0AWlZlSaUq_njv4SXsblu2Gmr2RRKxEjIJVXqGAuRqzuqe6cXMgcjTbyfNoC5psXrFJTtGhQ3MS-Ve0c4ZhA8BeOs8CI_KOfDy5874JpTS_zTpW_DORBFAjxxBQEDJejjdL7MRlXN-zKljMRIB3d2yBD0m0dswbtMMO9cbikLUj2geBux3_ISjyBVaF085pMk4_n74o4PaChZEWBFU2C9SJhOxUTWax4M-IIHxNRRhWRQgBFdJJNrioOJnHx8P0yYEugfiOzlEpJsbWfmDpwm6akw7MVCE4paa2nQv79aBNpUYqtnUFrOJT95ssWu04s3AI-3TzLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر فوتبال ایران بعد از برگزاری بازی معوقه هفته هفتم خیبر خرم آباد
🆚
پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/31564" target="_blank">📅 19:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31563">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjEtX-0lSpyTDJzajZhw9bWNzkUK8o4YGI2OeLDaY7yMyQQaYPJOBx8wMQWvpetINmBJPpGkwp5ghP8k4EuKRbY0ubk2LVTq6hhr0iFGDr6LtwFFCKjJwv_X3bUzECLQFOF0w5HtS1F9Og_59jyFdSI4VVZ2viIWuFNVTcxjioA-IWArpdTHHp7eStc1w1DOKKMETHLrah5_5adDwiuMqB0BDwwifDwG1fGRMSTLxzIZ8q7xzcHIM5dvwDDm9HAO392txpH69cuj9lm5Y-ChHLHAV-JN6pwfBqA2DnZrGGjo9ewVDM7OAUwL2jStxVlRXJhVH0URFOeAI-JL7lNLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرین سلیمی قهرمان ملی پوش تکواندو ایران در روز های اخیر با کوثر اساسه از قهرمانان تکواندوکار ایران که جفت‌شونم کرمانشاهی‌هستند ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/31563" target="_blank">📅 19:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31562">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfyC7_XE9lmO-MCp1jiFlnZlHD6zBCqZsLajilvG7F_0SrGKUwQeoiVVe1R5AeEOvu_WX9Ra8B3Safk0NQ2WqzF4qSVs4mqpr26l5ckHdDnh6l9wTre09eg6ybMq78fzQdrq0J47_2gXb7tU8V8UXY_dzGVyH6Plpa2808GYg21ZOwGVvudO54cMiOvEWC7-Cb6VH27mqrirONXW_yUzMUaIz1p6wks0KPuUjVnXwjL9f8s8NzhKPYw7W6fU4c00gsVWm6K0ANh-yNLmfOPS672x7HpmJuVUOEyuqDjHElNGNHGP9JeNDymRZaPc9tWht1DbdN0LzK3R403G2U7Afw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شماتیک ترکیب پرسپولیس برای دیدار امروز مقابل خیبر خرم آباد در دیدار معوقه هفته هفتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/31562" target="_blank">📅 19:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31561">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b787TNN7q01FN3RBS5QKsBFc1ukMfSkWGYAPFktSsjTkrpwM8n-jdu5ENtcG4oDmSSlHM1paEbfriuZwDbWxyo_3AVQEEYWTD-pmCb-A8oPh9flFn_Nf5ORdAsKZlSqdYLqE9On_nyPHvvrrhCb2UAG13OTxcPBGO5idzygKu0rA9iVxpfQBCLi4Cb68HhOSjDIsCgd1Q1RLyaZ8-9m92Kd7WzguwV5ddCUUCRc2KYmvb2CLAESODFYupZms56jyGaMGTdGPDnrE4kKN_3QEK8tF9wK70LsTGvTJ-3yqJuPWV2_rbJDbAUNwaom9OHmelAzc8JDQCmbyw-fBCzf0RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمید مریخ رسما بعنوان مدیر برنامه محمد جواد حسین نژاد ستاره ماخاچ قلعه روسیه انتخاب شد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/31561" target="_blank">📅 18:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31560">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f16cf41e64.mp4?token=UqkbQc3SttmO0otUjugaQc4Nsb3UUkhpdTu_laWDcLwQ4p8_LCUWqSxqkQ1r3L6KyRD_4OFu5yoyhzMDi2aNrlznznhiFMBy7U_4dlphDSaYIZ7xiHtcSpF3uGC47Ixr4mIfjTMJy-QdsvOBqw6VSu2cJ3uf6ocqXP11HTfgI1U6qDyejAO1-o_5dfDxVWLlCjpnawGcFh5wjF01txsfeiach8gEq2YCGGhfDbr5QuQo7L7Xls_n8OXtbwP1BjBEjPjR6WGcBQ0iPL-qxUJs_KchNeYQWdFCwxXqO3s2piKLNGWpXu1cJA013df38xS3J1UBd_W8xSkWTXt4GHVbfAFC_86e0tV4LFd96-1ssoOi5p27hyP84D_-BXa8ZTfyuJVaG5974Xwgk7BS59Lh7Af03zbcRZDYwn08YypDt5SGi2u6qvg1peRq8KRgI4Cgze6vvPTIpM1jDFTXE7tf_IA-08MU0g59Q7AvXS26STfpwKgQL_tqAdQAtPxeLslvzHAmjKoX7RvqvOTpdPJA7dEeCuVoPEH74ACqOytv_D52xKjIfdLh5GM7Cx1B2Hn71qX9Fk5C3NhJ8wpb1DboVGxJClFv-elZpsi8yfRi32g-tzGoGiJAhq-gTcZESI6yciTAU1dlwljYU7IiJrGH8nlAV8k_4eXDOMfdSXffiVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f16cf41e64.mp4?token=UqkbQc3SttmO0otUjugaQc4Nsb3UUkhpdTu_laWDcLwQ4p8_LCUWqSxqkQ1r3L6KyRD_4OFu5yoyhzMDi2aNrlznznhiFMBy7U_4dlphDSaYIZ7xiHtcSpF3uGC47Ixr4mIfjTMJy-QdsvOBqw6VSu2cJ3uf6ocqXP11HTfgI1U6qDyejAO1-o_5dfDxVWLlCjpnawGcFh5wjF01txsfeiach8gEq2YCGGhfDbr5QuQo7L7Xls_n8OXtbwP1BjBEjPjR6WGcBQ0iPL-qxUJs_KchNeYQWdFCwxXqO3s2piKLNGWpXu1cJA013df38xS3J1UBd_W8xSkWTXt4GHVbfAFC_86e0tV4LFd96-1ssoOi5p27hyP84D_-BXa8ZTfyuJVaG5974Xwgk7BS59Lh7Af03zbcRZDYwn08YypDt5SGi2u6qvg1peRq8KRgI4Cgze6vvPTIpM1jDFTXE7tf_IA-08MU0g59Q7AvXS26STfpwKgQL_tqAdQAtPxeLslvzHAmjKoX7RvqvOTpdPJA7dEeCuVoPEH74ACqOytv_D52xKjIfdLh5GM7Cx1B2Hn71qX9Fk5C3NhJ8wpb1DboVGxJClFv-elZpsi8yfRi32g-tzGoGiJAhq-gTcZESI6yciTAU1dlwljYU7IiJrGH8nlAV8k_4eXDOMfdSXffiVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ریاض محرز ستاره 34 ساله سابق منچسترسیتی با عقد قرار دادی دوساله به تیم الشمال قطر پیوست. الشمال یکی از حریفان اصلی استقلال و تراکتوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31560" target="_blank">📅 17:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31559">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM7jYuaFwOXpQqqBTypw1q0r2A54MWApX5hgjVlZRv25SiE2sAsw3QjHgu0ZyF_5fnUq6hXvTvcIa7p7Z-c-o6cNquenGr-FfeE5qnMSZ1HpX_Q_zrabjuxSw5ot5nz6WSRMQ5Xnbos1Wg8sxXyi_kRTBESl7FNP4Zy56H6ErI16W1uM63fc3ltah7mpC3sGyhnuvC6uG0Vv8QyEklEINFSrwXDCrUey2YbyKQFdiPucLOKVDyqV5Tpj0-JPZkvSXSGtDzHT7dlN8_cRzDdnzvwOqukejDoP7wMZ1Y5uoHUFuZHSmyfr_OFJDrBojkNERNo28qjfql89YCSw2VK5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احتمال گران شدن ۴۰ درصدی اینترنت از امشب؛ بر اساس اطلاعات دریافتی از سوی اپراتورها، تعرفه اینترنت از بامداد پنجشنبه، ۲۳ مهرماه، ۴۰ درصد افزایش خواهد یافت. همین رو کم داشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/31559" target="_blank">📅 17:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31558">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh5Otgxr3IhpJVPvqI7fK22WS74n6p8_wjDloFaX5FCCjYmBqumlz62S4WIlZOJfXTP_d3t4VzJcblVFUbmKkbGuDsRGFMSxlWNlG45THRbrF1Ernn52tLWWievkKLS169XpffHlDl31aCf2MEgvblzb84zKXonknX7IrHdVISXp_tCrWowcEePv5tntUTK-f50psRKT-npzG4HoC2SW33uhPzOavbLhb04ruvUDzf0h5WXuAHBnn4WGC2Q_RAzGRCfJ3OanuVb8BjCQ3ZuuoeFHMTbA7eHw4SXAOKhLWHCFS0oIn6cEDArWaAawUhF3_cdSnGYWBLOzukYM073XQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کنعانی زادگان، ایری و بیفوما 3 غایب پرسپولیس در بازی فردا عصر مقابل خیبر خرم آباد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31558" target="_blank">📅 16:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31557">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjrBJWiRwXJcNigbbIAYn7GWP-3I_rQyAL9IlcwJaulziNA_WBEShiZkp44OlvY33-KzyEpTORMNdcZTKYVAM5wgBwb2vWrOnXT3rQbAHf-gaczec70u8NGBeJX4YYV-JZDDmAN5Z9SOi9a1EnYRD_0xxObK9jzRwXKPXxPwInKRqtwOIa-neI0qwsUEOGFDBlPyQiDRM9l1CzFRNyTWZ60zw3kucg--rZ9kGqiILeoomFkjjsqQDbBfjXWRRk35RmafvUd_U5jGcsFUS8vAFRQIXApeEp0pP1tGp9fUm-hGOpgse5plD7z1rvFDdlMOlOrXjEKTK0NGAO2zGVtkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ؛ ترکیب پرسپولیس برای دیدار مقابل خیبرخرم‌آباد؛ ساعت 17:00 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/31557" target="_blank">📅 16:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31556">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwV_zY5IDgmIf7GcSb5jlR16iLqmNTiFQavvsXapCkAZG2xTmz43CFLIxtPCzk96gX7sJMCSEcedumrozwERpN41JKx0DjUScDlOmrG9lDxHC4hi-r_dUUhSz5ZTs5OY_HO_7M3MUFSH8Xw6TLloRob_Waydh8KyU4BPRSCoa3BeTrLUupX_GN7Ya36L_A4LYO_sqCvD7gQGbG7j0Zn9P9FJbhKkNBarF25w-UpMXy_9SofzkHLtvEz0yPnONE_nViGFJw1KLT77CmrSY-GLDCKhzHZ7nxxuzjx0lxu8egBjnsO7GaSTJkvF7HulsrGUkpCEuYu8x9Xnz55R8JcnUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31556" target="_blank">📅 15:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31555">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYrGsHYp6XFWV46Gf1ryxNuQ9HtFSbImTIEUt9lPKJpVAhgO46Cell9CDphHJ9Tj3GQZeVUh70OiN56-vT1f2Ui2Rpdi2QdxtWn6Ug4YrdZOj1kWZ7UqhQBQYIp4a6Sd2du6y9HE_k221q1IghvHkjDcCEug3U-1OHJtvi6VlSuzOBhwC77iz1nXrVKY9ZGn0Qfw3NI2qOCbqjO--JF6Z2EKWSKXmtcsht37mCGbiIdccds0v5X6PrHmfck_hmiBlyyJJHNez3WrDKtaD9Ok20vxkfaedc6xzSiwM4nfDNTJs7yWl4GIFdJidblrs85-Dfmfx2qPVXu-2WlSx9_HdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31555" target="_blank">📅 15:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31553">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEQl2F5_fzBOmur68Y_l2CrlubVNpkQsDuLDRF5BlanIzEn5F1--CEt_C4zCwJ6kEjyCKUpT1D01UgHcxAneW88t8WAzbiiaeVxxKytlF7Gb4wMlS4CsVaeqW5c5vrqavirYnlIOAxzuEO8tKSXx2f_D-5Yb1ZpUWOorw4W7oHS_sa6uXgfzS-6b-tGimZFvv-0fQR2p7UzZGTabT9bOyiOOb-gO2C6hFSfqRNxLdgFDhyOgukBylj-nsaU5Y2cDwAfhNZUG8g7qLFZWLTkspKbI9jbQ1ipx3sJUp6M9485ZkNc9Rxr7E2xiI3uhs1_3CMC_Jloe1gSggLbt6W3ijg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-Jrc4NJ5ona-pCinWMoBoGN5GntILemUV4AT1RMWVFV5YuFsdzIh8bJbWykVpgipRgf5TLdGdXMxFOKXRk6pSZmISD7sGI659a_2AEj4EP-BsaNSoOoWkbGGG2XFccotPJrpkl7Xp1Uge2-Z7n821ZRO8l4coPMs6VRnbt2Y05QN5CdAhw4BnnxEPzY_FzymVapt3j71XB-OuxWAV2cFXFzB-JPsaggCBN0Zb3kEvtA4ylMrECZdUEWkY1xDdB665zDQEk44k6jEoOcNxibqcEeRFsvI45Mm5hhNDzZ3iq4vS-Kl3IbT8HP3wYJkZUH9ltrQuge-2IE0E1j9GgDug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/31553" target="_blank">📅 15:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31552">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/31552" target="_blank">📅 15:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31551">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIodroVAA3_wdq8qZYP4juvFAF-fIJs3wWKnG3hW9t_-Hg9sXgHYj0G7DNAj-GykNsZQRf0QUu4g1BVbNUKK1f3mQaVuL-YHeMvra2MDGg0x-EzWp13re4d2TxEKIXtMD_9J7ahWZJ_6ukqdU54rlg8da86ycTLKQbfdr5jP9m10mpjv6p7bPG7Ki7hyEprsuYLyMUan2TqsNrL5rDJrxatGVAq3-5FTiwyQWX3QP7gfKMg8gWxE4sGVFuerhwN_jngrZZx_joY9pFf4_XqMqgFWXQlKDUALk4Z16kT0tndCrF7Jd5854oq6nQKN0cQRRtgFIyrXMkYWrJnnz5_QxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/31551" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31550">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bkg6I6YkdpjdRUYjjelJSjmspmtOlSTmk2eu62WQrnTnuNxgBg0wtuKu5WciZT3ih9C1k557GJ4x3-EtkJhvC73WJTf81cIqwJI46wIkO19cefQ9KYnnzLyPCjtyACnuY47aBVm5pkPvOggRgtNJCXb7_I1CkW5AacP8fKemjvCZR_aW2SXY3tTeaUzolexZHj3ifsbWuj-B16KHseSfxiW20IXgzVPqndnZENc7cokFM5N3tcvIPsbyO1aUefnqc9BNToPvWc2hoVKtsgt-UfZ1HVgXjPVNmzWEFwafEr7AtTBdsyPBB4jE2Ie__dmkA7a1LE6sncrTPspiju28GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31550" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31549">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNxLO1-iPiBek8Q3H7jgZwNdNVaAKO56TQLPBFUxtjRhqiJSVff7919VcSv73-4-5tDpOFPqGs7u7rGmWdoVMTgzA98uFEuGbG9Ep-2OlxYj0_J3kX7WU63vxSpRlXa0rUxnZhv0UH0uHix5rCbrp9TZONpKn8zAM4M1njkkf-YNBN0I8Mikt48cJtJK-TCttGC0DnItQIi2b-fu2Mjklad8TlM-JTb5dDR-AQvEk3mlQoeocEBS4CCS6gOGSNMjzFd7RImBYHQERL3SdvdQSV6yskeOUwNjNCvHA4DIE_QrNeTz-wHHLWc7phmbpQikwDuwrzpxw-a17zqnvQl6jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
هفته هفتم لیگ برتر ایران
🇮🇷
خیبر خرم آباد
🆚
پرسپولیس
🇮🇷
⏰
ساعت ۱۷:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🛡
تا ۵ میلیون تومان بیمه شرط
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔺
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/31549" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31548">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
🇪🇸
هانسی‌فلیک: یامال واقعا یه‌نابغه‌ست. بعضی وقتا یامال پاس‌هایی میده و بازیکن هارو تو موقعیت هایی میبینه که حتی منم قادر به دیدنشون نیستم و اون اینکارو حتی توی تمرینات هم انجام میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/31548" target="_blank">📅 13:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31547">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCEemtce_91TOQuGWIQMXFNnqLIyEUl0pYej6XavRRHeFMCwS2TK_vTObvdEm0luoxAVEDVXrjOTzOuIIjTwZXMmL-8JNpLOV7aFHOfmHLZdX-tGlAUpQFySTK7pnJc7cREGT77ojj0rxxOKMJvlYwixF7UH5jYdZMA8Gen31Cm36o0S8npmZ5WddY32WymCLv0z5MtBEW3dQdPFq93hqEJDtkfifX6tHZOBOs_1xOjEqeOkGABLQQ2vgakt7UgW-ACtIc0nx5r2yoMwqsVYzo6yvUmAoNnlDi6YZEKtX_fxe3kulwm0N3FxnRuq6MMvaeZQnc65sTxW4qzKaIt54Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب بارسلونا
🆚
گالاتاسرای و اتلتیکومادرید
🆚
منچستریونایتد در هفته دوم UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/31547" target="_blank">📅 13:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31546">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDdk6Y_viNBjJvLFSjYuhgal3Nbc0iFo1_hprFKdOqavYTIBDVa0aSMKB2R6J3EjUwFGpUbp6JIm0DW702w4Ql6BldYtQDO-1sRSeaRVnNTGqG2emrmKZxZSJtNbuhgfT4gk9Nzlde4b_kLhJM9szZTcjxVfQPykGUOyG_9BR7FnbBMwgZm7wqYo0NEoDhwQP5Ud8H92J1S_CfOOQuN23gbjbFWKVcevNAOX0o11YS5Z1KKi64JDWcDKHP5R_dp9-4nZw7y86_IvaAjc6nwGRHyHBCCLuMg_Y0PuYA91BT6vbaLCazy5u-IKdVLjtZy8UFynsdub1yMa5gyDmn3bfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس‌رونالدو: اگه‌کسی‌مسی، پله یا مارادونا رو ترجیح می‌ده، این سلیقه شخصیشه. بهش احترام میذارم. اما این که بگید کریستیانو یک بازیکن کامل نیست، یک دروغه. من کامل‌ترین بازیکن تاریخم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31546" target="_blank">📅 13:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31545">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iNYUTK5-hC2N79yLcLLzn-LMYIPxYHWa8xnAidsSpzQpm0R_DNjVzxYcH-Pyk4oMvWknQVtTJ1IE40grHPvD-WZZnNK7I8cRhvNzkKgMZ4lDy8FEmkDm0M96rxLqdXzxOeouwcKhfjFLpgkAw2YJ8wwes7Ox7Cas2hkPmXI3MRJHJtsSVQExyQ3TFof9LOHW2fVMR_vIwBT78vGbxEHIsiWxv-W_fmaB9M7HgPXVKAdViGMYtvdjUqbGEa7H5oUGa3aQu_Hg2Uy3miO6pwcpvE8zPvh4LJyqnOTx2BZ2L09-9K-fhogdKgxHXGZ8xTMv5-b3cQopa7Hvy8aoqcbObQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31545" target="_blank">📅 13:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31543">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0kFPqAodvh2sURpk4_Z6yqafwI5HIqnmAnsCmLcGNCWUlK8FFItHYB-zwZuCqJ_H8WGAsQIx0d-C052XUFFU05aLjZcWrYgKXgNDqivlO9jAnkIJAe2A-FDT0xXo-S56_K9lsthUbAnD5-uWmx0MjoYCtxkpkmM-sRXzA3hAooPSiCEeaLN0Xs1cnRVwUFverVAjZj-AwpDXy13xoSO0iuEYTEqCmpf3RxmBHj8knPid7FLWFIrElaPP9UHp5_5kMioX5QApr8_zwb0F5z3AO1CfUSg-kIu94TvsgxMEzSZVAc1OiaemYaZDRKGQOubUuxZCzCDiIFmIK9T9ZNqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OK-6fvCdqpzEn-ukLKqe9ZoQYs2rEI-8nuX9zsdhd5JMwyyNzCG43j58TwAfKQrF7koGZDdS5cJzj4t1Wq1ws1T3QCUuh6AgUX_TrHe-awFEB3Xwp3xgGZ3D6DWup58_NI-dX9eM4UZzcji4Fi7XYYQnocrNwa9yvIkHA3YCYMP-WAcocA_hut_zx9ok0MBYSohTeGs2c2Zz36x2N3jehrweU2GnO_1uVi0NJVtTPIFVxlREJtFUuNxntoxLZxh6r_NMaCbSyfebID4b7Fh2mtg_6K1GoyrGlVIua43dPBLN8bSAw630vQtLzP2O3y1zrS2izlNH-YHceItbiq9JOQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
👤
با گلزنی در بازی دیروز مقابل صنعت نفت؛ اوستون‌اورونوف ازبکستانی باچهارده گل‌زده در کنار گئورگی‌گولسیانی به‌بهترین گلزن خارجی پرسپولیس تبدیل شد. یه گل دیگه‌بزنه به تنهایی به بهترین گلزن خارجی تاریخ سرخپوشان تبدیل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31543" target="_blank">📅 12:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31542">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kHYZg6Ww8Nkf2r7F1VOBwuAJofVPhD3MRLh0LXuA91ra3kHc58Xwwf7jjJABY4wLUyP8fix0yj7Ftp6ZXjXuhBQAamAAa5ltsosZLBV9_SuD2VchNu_lzH3DYXqJs6sw41qkzVdZyBNI3xxhoTkVu-0MLFvgPnLexCcRaRPLgaISP0tWxIidsaXIV8aiLavvPG1Xfk6kKDH6-LOkwtHQ_Ubt43UjaLxrArqG3b0ChHGmgEfphXXTrLsHBUiFdJsAQQGojAS6bcWPayMmzW9kjDY_yDi6ZmixXHWeGg0kTmBn7SWW-pVqUdXH_IGhlnjOVmqDmoprRd1HVVD_YaQhsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
واکنش فلیک وقتی تیمش 8 گل به بارسلونا زد:
‼️
واکنس فلیک وقتی تیمش 4 گل به گالا میزنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/31542" target="_blank">📅 11:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31541">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=o2H3vCAKhF2gwj8WID7ZOFNgNE1V09fWh72zJxPZ3q4bmBBPBG--0BKsBKm5k1cSX9zpOoQjJx0EEqGB0kaGtdOgGEAIXPS25wfUvrj655SN-jxLmtjJ1JrDoZYuIZkSxgh7-TWRJ_-fkHFzyM780T4TzmcXEzUzmPRTFHknjvKJNMw4jJ36scjFdPOlw4LD-0qBoNmfHFS1gxC-Rp87NisSLukmu0SsgmiCpl_e7W-fkb75zCtkKdsWX1fwh672J3t__yXySKsPlkeC1EUYmo9S1NPmoEYutsy6c4BR6vd9t6DM87rdb0H6osSA21sX4As-_Mv7tI6GECLDNNbB5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b689cf97.mp4?token=o2H3vCAKhF2gwj8WID7ZOFNgNE1V09fWh72zJxPZ3q4bmBBPBG--0BKsBKm5k1cSX9zpOoQjJx0EEqGB0kaGtdOgGEAIXPS25wfUvrj655SN-jxLmtjJ1JrDoZYuIZkSxgh7-TWRJ_-fkHFzyM780T4TzmcXEzUzmPRTFHknjvKJNMw4jJ36scjFdPOlw4LD-0qBoNmfHFS1gxC-Rp87NisSLukmu0SsgmiCpl_e7W-fkb75zCtkKdsWX1fwh672J3t__yXySKsPlkeC1EUYmo9S1NPmoEYutsy6c4BR6vd9t6DM87rdb0H6osSA21sX4As-_Mv7tI6GECLDNNbB5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌پرشیانا؛وکیل‌علیرضا بیرانوند که رابطه نزدیکی با علی‌تاجرنیا داره در تلاشه که قبل ازرفتن علیرضابیرانوند بخدمت سربازی تمام توافقات لازم رو برای پیوستن بیرو به جمع آبی‌ها انجام بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31541" target="_blank">📅 11:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31540">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K69YvptSPvnNuugL8qUtDc_gfzY9XRg_O8Ng7eE0tbvPfjeksfZg7burOrm3l20AnVGVQdNWqKENsMpVZxwg65pWVzCIwmXbKLDYbPTJO7Ili50Gk2-ois7jVTSYztQi4q1AJZRWOznc5WgsVB2CXWZxA6onSjtoPeLzJuFJr_NHKvGdjkWR7TWH4QpAptQID3bpOLJCEZiAuuj3iC1bx0oFQLnqdM_HQwlt2rLGhe8GnXwf6mSFNO_Wlz8Dg5tWYen3H8XQu02kwB8RDG-9en9A0xVYdd_BCqagj8y8n9d2_rs-VN6bTm9LnYFWRnyzU3a1usDVkJ8GylG68bfKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد استثنایی‌بارسلونا درفصل‌جدید رقابت‌ها: 10 مسابقه، 10 پیروزی، 43 گل زده. شاگردان فلیک سوم آبان ماه به مصاف رئال مادرید خواهند رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31540" target="_blank">📅 10:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31539">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETHaa2GVSu89goRugNh9U4yeAQdJdup5Kp53JhN-Onyi2wkIFqWsimaYMe6dax5Um3bv7WTpsKmJlnj05QY5QZ26NHKJghsCwqcbJsbxGb6OZwF6PX8At-k2R5P8iQ9vzT2XE56VfY9g2nHrYcLfIyLD5KCMaCyDhRpSfQhIRDLwoO1HPUb1ifngh9nvjxlSZ7-YKHPPmRSdvd9HF6yqJ5VNmlFM-gY-5pjYDpTNylrWTHEOLurTFKN8MYaRGClBjnsm08_JFqhFgTHVUWiPPu61GIIgw9XqD7zrMEJdYyiVkehQNiggLayc-cvV1aLnR6DfyG2yIYwAWQDxZtYtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین تعداد گل زده دریک سال تقدیمی در تاریخ فوتبال؛ ۹۱ گل در یک سال؛ رکوردی که انگار برای شکسته نشدن درمستطیل سبز ثبت شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/31539" target="_blank">📅 10:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31538">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSx1nsiE331kBLqDe5dnuQZd2cpQzZThSPxWwdkk-w30TUkp4wTcYtWm1bUjduxxu92FU1B75_JkLWJ_PoFofPmBmlSIsrRmNEYiQvcKFFQhqrE8KxKbzePoyCwa9Ze4GBr0L4G0T9CYHtWDtbDUfDNQL_sQhSRt8j2zmJB48EUsRxun0CoLZjV_jvNreEZjl_66_wtQp_1YUagXSjicT2PcEO-3cyjPjYhO46ZEH7aTZZEjHYWxIYW8vXifmknpahE5KhgoaN_y8WEHLDj84HRPFZmwp_rAumTbOWN7ptcjeZ3Ep23hq735Iwh_SwFTFE9b1h8LyMWIamYudd6ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
نتایج اسفناک منچستریونایتدِ مایکل کریک در فصل جدید: 9 بازی و تنها 2 پیروزی؛ شیاطین سرخ نیاز به یک شوک از جنس آنتونیو کونته دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31538" target="_blank">📅 09:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31537">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxYfKrTNIC7Ohfc9SPFtxJ_vr74n_SNJuI6MK7Gs5G2gq_IgLuPcnGm0OKTktZHarBC_vjhYie8xaP8tdLHxZ14xMzH_Qdl5AB-IgX85LWi7lRw0MK97bGBAOYRNeQgunyQwHXWQamp98NoK4zOaD-tLkwrGmUdsqo4hQC2xcbq3vmtTzbKSEK_y_0hkUZ5mpm7tHp_FbE8ccfKcC5-qp0mrZ4cw6pQXmUL2KS_aPT7a04KU7_Mj6eQOozWa8iQpCSBMTupLl24QZpU7ye8y0OTJro3ftbr1Jn4jM1EE-vtmjVzjQy7YEBBC3jcDk66j6vBaxTIjWPDBwida8lkceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
گالاتاسرایم نتونست نوار پیروزی‌های بارسا فلیک رو پاره کنههه؛ آتش بازی ابی اناری ها در خاک ترکیه با برتری چهار بر یک مقابل یاران رافائل لیائو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/31537" target="_blank">📅 09:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31536">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXzo5uDFR8kqU6wy1mKde3KOM-Ok2VxQD3-1GrHWNLwQSLV6lRPp6YavA1MgVqpwIPSVoJ7o6J8NflBi-Nv8r1fzFtWTYR2UNvEoG3nDjCJ8PQmFwm4IWdYTuNZOQuJIVneJ1PfgWkqg4BiNuFCoUYnzMkJ6AYL6tZf_PZU5KeaRil3bCFqUKhiiJ0PfZ2pviSmEn3GPsLcyWUP4LPTHz6E6Y7x7rsapBQfqdpJUX1hGuangM5hsb2I1ESyPR4sQZ5PWTbTfgAiVIDdZM_8zVrTSYdw-ELiFJN3a_388AIEJL5rcb722FF06fiG2LpmdSdls0oKuijjH4K_bLVbGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛جدال‌معوقه‌پرسپولیسی‌ها برای صدرنشینی‌لیگ و بازگشت آقای‌خاص به شهر رم
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31536" target="_blank">📅 08:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31535">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfpCI9CKbghREU5ji3rsXg1qYFA2-9OIYO07FNgZNHE-SK7JgwJHpPK_19HHO3IdgGjuR0sB3nVaxQ4JzKx2QlRx0T1V_OKu0Cj19_z3p3WTOVNSAwQVgQX180gEsfW2JdlACQc3baNghyyafOiwIK0T__Z2ctnAxgE-JpvDnQ8SM83uMx6XKvrvLCM5zdn7fQUn8lbIhA1acw9dT9OcSLefMntTtDPFY1Z5lm02eI1w7Lb4qBEVrcg3VQiZZhltkDTYdQghUO8_fuCk5sYxLe3gsyTlx7Hvj_yj-hmq_rmY0JXPGo_RkPJm9a6s-FKasWSvcqyCpPyaDA0-JwcFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از برد قاطعانه کاتالان‌ها در ترکیه تا توقف شاگردان کمپانی مقابل تیم نروژی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31535" target="_blank">📅 07:59 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31534">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHUG7BLX31LxpjzjEYnKKROmFBry8MBJzmBMVaBHd7ZuPvopKpK4VgOnLqJ7_ODybjL8LMK-O9Ya13YZ-gdZcejWgKhygBslpO2VpcX99B092wyZDzXyYqOSFIdPqFxjkGz7pEMe0oFBbpJjQ85nlAvxZNaCrBjfssSXi9d2KdfD1P-3c5XEHDwBeOE5j9JZYw-bhQ_BoFavE82jqpcx1TIcOYIzZ41eR_8_-arnlqYiHc1IFW7aFDrgfhjefnF50Qz22ZE2mbJqgyG8J0u9eAAc04XsPX0oIb7kXJrrAaTAibXLSbEBzkcxFDA412Idaz7eEwqSyQB4SeE3kPuN0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پنج مدعی اصلی دریافت جایزه توپ طلا؛ امباپه بالاتر از همه؛ لامین یامال درتعقیب ستاره فرانسوی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/31534" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31533">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zf4hxp2z_lc6dEXz6jvAs4Pk8nv1AhgZQJKUWiaWvneKfpGbGeTPAvxmx_qdYHfls6Qk_Z3VA7wC18RkNE-esCFF1cYg5g3F_OGhOA1xr1jqq7CzsDNLHQFN2WWCJsItF87Xx73PGKDRTAxu3n9tZAZnxNX0IZjoJvp5trZlp6cIU7yK1aRiCfkiDfDqsmytyCYP0kYg4xt7I_FNmAVoNAc1-SJ4KbMM1VZEqZxUL8ldygkukbz-sCE5v6n8vBczqDeZFkzbOolyDq_hkgmSYSBSeXdf3NpKpzsrsqR6B487XhAVij-dOu-yGWFSLokcR8nLfBFpVDxyBTHZTcjPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ نخبگان آسیا در پایان هفته دوم رقابت‌ها؛ الهلال دوبرصفر السد رو شکست داد؛ شباب الاهلی در شب درخشش سردار الاتحاد رو در عربستان شکست داد. آبی ها با پنجره بسته در رتبه دوم. شاگردان جوادنکونام دوازدهم‌جدول‌رده‌بندی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31533" target="_blank">📅 02:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EglD5yXrp7v9E1hiW9fvph7sOISxsvouvbFjVMw0JO3oRdWSljy38h0qCMTXnFKLdC2_JJ9QVhE4MrzSbAO2xI-DpAcKjMGHzAr4CDFDqnn7gvW37N-DCL2o16JCz3RqzCg5hu3ocsI_2wDwL8AGKBglQtubZEsCmwcd9IwPnYQfiNX5_oFwh5v2v3OLDGFr0_cYrFHYLeyO33gQuMFwSwSaBxgpCzs70McIQTQplc-ebyp1UzUV99lQrGX2XNcSIi5I5fN9g7BTRtCE-kVPT5HQ7SxU6dbP-ZVQZFHvN4p6oORm7KrwOpATxvOyPIwFfzWRElmwQFJGz0T1aSfP_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31531" target="_blank">📅 00:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">📊
نتایج دیدارهای امشب هفته دوم لیگ قهرمانان اروپا؛ پیروزی پرگل بارسا مقابل گالاتاسرای در خاک ترکیه و شکست تلخ شیاطین سرخ برابر اتلتیکو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31530" target="_blank">📅 00:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nudUS8FPn5j2fHlYWW9VQkhRRnrIHU9at4ZvKx_GUpRZm3XkCui6_SywviO-gziCgiivnD4glODzKWn_rAIsUuOueHpS-jUNnsfWcOsrFHodkikxU9RqKSSEZ2UdvRz0nfT4OrpIXQIr3BsO7n0CkJO4W3LXmOPH06gDu9JrdMhBA7aahy39bMXLwFfBH9cTuFMYzlQq-kU60CD0LxjIw8j0SjNwUgZUdTOB7SAdKjU5LvGpjLjKsqAqu-tHfKKjoEaEgoE7f9CeMYNCtHJ0OARa2zvaRQWhD5lfaHkEvAblnW_FDPoeNB4ESW4VQ3hRDH3nG45Bj6ZFhy1KaFjVJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌نیمه‌اول‌مسابقات‌امشب‌لیگ قهرمانان اروپا؛ شکست یک نیمه ای یونایتد و بایرن و توقف بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/31529" target="_blank">📅 00:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTvMWFvoLeDScfaGN6Xxk3atS1yxvWoPRd2fnbL36g96bW8h7j1Dmw4vcQMo63iH9wJr8wNdgvmAf14KKGLMaVLhC91GByxK6Cl9Usdr17yrJ8byUkUJ4GBZQLMI5ZbK1IYpPI6Bc_9jEWcuQtFdiLdGcVwgPT7RkZnBHhLQRy-JgWP8l2ZzN4pN4Z05n7YtbrpC_G6oMV8S61VVu-7I5G433HdxVPF9wcjPvqDHsy3Wycl_HcR23VYjzZAN9wjdht0J02JAIaJc3uKiayPm2onPznU3Vru8PDvPGVLEYxXtcKczzgK9bsZgF9eiTSxBiQRb3Z9esfnYx2xdR7IDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31528" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAjGXUl9HwYrkwETkD9ZvZbWfHzBs-yiR5-FYT2bPoyYXg_sQ7C-Q6XPy1gpkbxmkzzCpp3NfnWhMwsBDZrZcRGJXzmN4mwG6Sk5T_rRUb-Re1MQLyj3XZzYdjfrE5EpsIYFb9Vz4QhNXZGplPT8nHLOThLsZ5oqXR-0rf9oJzhKhuGACgN_J4FsyN6U-0iubjLUhVa01kEuamNNbtqEge1UwME2Qv1mweNr75eiElN5Rh6tN3uWksTEiLtBmCkir6TW6UzXqvNdiODsMR8aO6FCtaKTJXBlUN79IvQ5Ds2XN0yeuQq8wZ0tpvjLwH4DsSses23y7UCqEQRtN56uew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قول حمید مریخ ایجنت یاسر آسانی به مدیریت باشگاه استقلال: در نیم‌فصل یک ستاره خارجی دیگر در حد یاسر آسانی برای خط حمله خواهم آورد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31527" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH6ozNS8MLAOzo-ZZVEE_jz2Ldycvuo_E1Mm7WuP242fltR-BSE6pqpp-qPwTc20rVQ5JD07diuDPb4FcAiJyJxTcNa65bzysLv6OYz6Km7uTiIkjNFQLdOmgYtCnBlbud3OwwxMhrRBoCd6RkUM2qrA2ZZ45yyMA9mXv37sGtD1E28YQv8Lki0Nb1moGG6Wg4JD5-DKDw5d2G9AuS6NO_vkDuYdUTjc7cO_Kvwh0ZaRAjuf9FS-w8pml25saUILVs5s_lzs1mB4Ta-qGXwjoPT1NmsA4C7Lr3VeQgF3n7m2fJNmPrJkieAYF2A-zrHo_7fu2LAOihcqXLUYdAAYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دبل‌ تماشایی‌ سردار آزمون مقابل تیم الاتحاد درخاک‌عربستان روی پاس هوشمندانه رضا غندی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31526" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6tC9NzU-MVWvtsbn5ein2X6pkJ__v4npKRhAFdctun1a-jMF8OLIDrCvDt1R0_XdLVccOeKBdAfMzdXW5haD4vMZtrNem6AffP_Pm4yjt3lhOqjCq2RWMKbEfuHU9Rxs_9iH4moQpo18XDqQxXELnUAw1qLb-VsDDlRnD55G7RusvZ3uq6mH3kD5eTGiKTs7n44iffCXKoCB_HVaHpqy5lWmwU259Fa9P4jO3tp-rqFrEe1b_yHleSZErv2oZdD8ob9wOZQrIH15B1_nNMRDoK94DbOt2MyxZRI2r0Ns4Kq7iYLLQzsz6-uw-PxE1vAzD9V67rkvxFcm2047Ox_pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31525" target="_blank">📅 23:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31524">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lftTXJoKCfIygmI0MuEG076ukNN1MAp1z32yYS6-3BQSeCGXmXSuR4-pCyLfH9Zh_4rnzOpPLXhl8WN7DwmuIFfxa4Bw1k3egc6T5MHdy6oKPqd92hObW-6a_n-YoyJxG9EGNFcA1o0kmBZP4itiLVigtuYdS3fSh7fF3Yb46mistDyX8RacL32SlH6OMu3X8ru7PUxmOewM-np6GseqcIUDDYsrm04MDx8c9q7JNnCdsAzzLeuFA9uJKUS1FZ5TYhpnQRc4fl8fCyN4aPUCTD8eQpCqVFZ3IMyZLKif20VHfqvQPozdsyfJiGxkPc_HqebrZ6eUO4OpR3j9UyrXFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی پرسپولیس در بازی فردا با خیبر خرم آباد؛ تیوی بیفوما دچارسرماخوردگی شده و اگه به بازی نرسه به‌احتمال‌زیاد اورونوف جایگزین او در ترکیب‌اصلی‌سرخ‌هاخواهدشد. کنعانی زادگان و ایری نیز دیگر غایبان پرسپولیس در این بازی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31524" target="_blank">📅 23:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31523">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e058158de7.mp4?token=Ejfm_Tl0FESQDw3WrZJSrLm2lImhhYrO5SN1jFbnLN57ChLh-UAjtwpD-kP4tvIo5SfEs-ydhOUDC57-aUcHgzU1xZQPuhT4DZq_NPXSp3oDf8t-uRZOEBR9Mb6purHiHfJXoLOseKX7XlclSxJdCY_Znl-Ylr3R5eoLaXdXQAkyk1cptOi6U34NALRH11GexIPpp3ofz9OGgvdgkoL4UFZETEiywQciX31nRDHIIHqKCYKG11kypNBYWoMHKQjEWj0pzV2k98HvLbUbFaHWmSt2vvw3aPqU2cI8rMqD0-IiFlriWInRGsnaIETPvZmlJlCJslsHuF2mLpRQEhd9YghvueZrjItSGUk0EFrWFpz5wTUj33HsO0-CgPHAUmaFFFtbUHwRKV8gw34O8OIKaNYulS68fl3O3Js68c7mMZg_q74YVoM_ZmOxXJ2ZF4PcauoB62zEeC0JJ2ICAyF5vWb--x7PH3UdvqkhBaghBD5UFxlGc5uqzz9gs3ffagHbdk9RooyOzfG5wJnujYSLjHYJoO7Dmaf1tVQv7O4bbjwmtgrXuCfZesX0FPVhIZo6lWhZmXJe5QlTx6ZygRt2XgAMqW8f9hcRejSLLkGW2TN1fmpMMJu5KZcSQ7yT_rbASdUS76zRvCIf44F7326rRGhu3Irhy4OHXipRRA0sUkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e058158de7.mp4?token=Ejfm_Tl0FESQDw3WrZJSrLm2lImhhYrO5SN1jFbnLN57ChLh-UAjtwpD-kP4tvIo5SfEs-ydhOUDC57-aUcHgzU1xZQPuhT4DZq_NPXSp3oDf8t-uRZOEBR9Mb6purHiHfJXoLOseKX7XlclSxJdCY_Znl-Ylr3R5eoLaXdXQAkyk1cptOi6U34NALRH11GexIPpp3ofz9OGgvdgkoL4UFZETEiywQciX31nRDHIIHqKCYKG11kypNBYWoMHKQjEWj0pzV2k98HvLbUbFaHWmSt2vvw3aPqU2cI8rMqD0-IiFlriWInRGsnaIETPvZmlJlCJslsHuF2mLpRQEhd9YghvueZrjItSGUk0EFrWFpz5wTUj33HsO0-CgPHAUmaFFFtbUHwRKV8gw34O8OIKaNYulS68fl3O3Js68c7mMZg_q74YVoM_ZmOxXJ2ZF4PcauoB62zEeC0JJ2ICAyF5vWb--x7PH3UdvqkhBaghBD5UFxlGc5uqzz9gs3ffagHbdk9RooyOzfG5wJnujYSLjHYJoO7Dmaf1tVQv7O4bbjwmtgrXuCfZesX0FPVhIZo6lWhZmXJe5QlTx6ZygRt2XgAMqW8f9hcRejSLLkGW2TN1fmpMMJu5KZcSQ7yT_rbASdUS76zRvCIf44F7326rRGhu3Irhy4OHXipRRA0sUkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شباهت‌برگ‌ریزون‌گل‌تماشایی یاسر آسانی در بازی امشب استقلال‌به‌الغرافه به‌سوپرگل‌خاطره انگیز آرین روبن در دوران حضورش در باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31523" target="_blank">📅 22:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31522">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3P_I-y8Apdm-aA9h6C2CbPdzbYDi8nuE4dD56I0iCjBXeA6MjbL4k4-UcDM8aFYG0F628IzG4BE00htZ5MnHcsnbDUJ_ZP3fnrNKeYAPXh9gC9Y3oEHjL2s84ucp9ElNe3hvH26DsudHlnB5gTSsyffwEknDJyETiQnY_-1J7SboBc_3EQXaneBVsANVKgncKEi8yU5_pjzCKuZWvRc6ZZxyWJ9gQbYo_zMPhcWJ4yIFTb0GfjFfggnvhdw8JVGYgDfEo0lvtU6wkEBID3vvR4MCpd7LopkNOUYwjWmWHNezjgS79sb9NBCqXI6fOsF9GsWE-sDz2q6IKKO0km8Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دانیال ایری مدافع جوان تیم پرسپولیس که چند هفته به دلیل مصدومیت دور از میادین بود در فاصله 24 ساعت تا دیدار باخیبرخرم‌آباد به تمرینات گروهی سرخپوشان بازگشت اما به احتمال بسیارزیاد در بازی فردا در ترکیب فیکس حضور نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31522" target="_blank">📅 22:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31521">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=M3QiqDY6vmZshmwizzbxlOH2dswXKkHGymKLqMIcPgBhLXXC7DvPoy2isS7CtfvezREoywAIcEmtA2rnGhTNqBoRsTfFYQcqTek3P4XzU_gVLjh-DiSXKPpSUPuZRLEtfW48oRoNl0YJoBqH6USbx8KYTMmyH9PAukZjkr7R7i6RP82MDMjM5OEpIyAHOWdP4teDqTG-4npj43VkBTB9sMjx2RWkIuhxXNrqAOX-V5q953XykJngGLcfjEAcLznvAamgGKEifkk5mLDHf05YqikALJDp_X-hiWJHA7xqTestcnvikAKkFoQCoMOlTYElCJ4aVZ35e1QC2UEgdz0GJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d9d3f2c25.mp4?token=M3QiqDY6vmZshmwizzbxlOH2dswXKkHGymKLqMIcPgBhLXXC7DvPoy2isS7CtfvezREoywAIcEmtA2rnGhTNqBoRsTfFYQcqTek3P4XzU_gVLjh-DiSXKPpSUPuZRLEtfW48oRoNl0YJoBqH6USbx8KYTMmyH9PAukZjkr7R7i6RP82MDMjM5OEpIyAHOWdP4teDqTG-4npj43VkBTB9sMjx2RWkIuhxXNrqAOX-V5q953XykJngGLcfjEAcLznvAamgGKEifkk5mLDHf05YqikALJDp_X-hiWJHA7xqTestcnvikAKkFoQCoMOlTYElCJ4aVZ35e1QC2UEgdz0GJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گلزنی‌سردارآزمون ستاره‌ایرانی شباب الاهلی دربازی امشب‌مقابل الاتحادعربستان در لیگ نخبگان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/31521" target="_blank">📅 22:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31520">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/559d04596c.mp4?token=RUYdzVUwvEmDYOTg18j3KFyjJRQk7pKtLuww7co1lN25n_XdBTaHug_dKzpnhfJiC1XG0k6YoLvx5xeJSD-r7bNm_1w5dN5T4elxitpZm7mCrLQZvyqkH33DDRfI_P3EIaedX-yngacrKJ4PidrYNQb9ieyiYmQC05T_KFTg72HGDgg4QG5VzQo2WtvfzjDplPsXKxKUmZ2-XUc6s-gdhfrW23Wu2UiulonNXFYr_Cj30Rxnzt-3UXDkLMjIq2W-W1M_thSYDAp8PZUN1wv8TI-pa-RBxSQu5TUHCywMd5xhsAC40zFRXH467eyDhugRDRHObBaTuYmrjCQS2VxuAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/559d04596c.mp4?token=RUYdzVUwvEmDYOTg18j3KFyjJRQk7pKtLuww7co1lN25n_XdBTaHug_dKzpnhfJiC1XG0k6YoLvx5xeJSD-r7bNm_1w5dN5T4elxitpZm7mCrLQZvyqkH33DDRfI_P3EIaedX-yngacrKJ4PidrYNQb9ieyiYmQC05T_KFTg72HGDgg4QG5VzQo2WtvfzjDplPsXKxKUmZ2-XUc6s-gdhfrW23Wu2UiulonNXFYr_Cj30Rxnzt-3UXDkLMjIq2W-W1M_thSYDAp8PZUN1wv8TI-pa-RBxSQu5TUHCywMd5xhsAC40zFRXH467eyDhugRDRHObBaTuYmrjCQS2VxuAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول لیگ نخبگان آسیا در پایان دیدارهای امشب؛ دو بازی مونده که السد فردا به مصاف الهلال میره و الاتحاد نیز از شباب الاهلی و یاران سردار و سعیدعزت‌میزبانی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31520" target="_blank">📅 22:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31519">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9hKOeCKITAlycHZZWce3_KfshsA_swGOTiHmkT4rRLFHmDd7iMU440nMryhs6WOASRPWWVc1YcqhIAdP0eUh67f-7dUIjAL9RtnmjbjW0M037e-o11J9ouEfH9wBcyV1ai32jw-1jid7J8Lejc-pqqXPcyjbkatzrKDGN5RKno6r1TUlNkudiG0epf5wzy2Rb75Y6Vi301JIcY_gZEz9B9y9tyad8TYsfTVJUFFZun-dWD5EqTuL_QYhI0E08J1nWCOPatYCdpWoruB8ZP9jnv69nYha_EtI3dNDFkVR1pnTXk8EGaIPjzJygh6Mko0hAHr5ruqavuxcOf5cWXoow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31519" target="_blank">📅 21:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eugF-_avbNpH7nrvjeBU6i87-4p0hCrAWeypzS4qGfHhXS6hQtf3zXQAl-t1HE1zbYRA3yI-Lv1hDfIL0rsmGjnOuXv7IziwzEQIPY97MR8zrTgtVPCX1WRQNTR5XCQnxhFjoitq_JdztFhXXNRdAXDEeIV0bRYUO_SJGr-6i7g6XVo1N_aBSphrEDezliefsXKjDqmY5ukqx_BG0E851sFY37NQlkpop5U2Tcvk432GXr4BXBGOlJVNH4wsq3koY8uKQQWBo2DRWGT20YUhLmIToV05meesV_i1sQcxgnsc90kyn1VvrAL-JtqMf4GZcZ7IkMC33j2u2NCsBNONMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nBh8-BUYgUqgcc3OJT9yD8C9PNKb1BiYeNa6D6bupoodo5t4GJGRndptkMMOQ6CYgavC4Lw6bV2ze4q31X7W-QtIxSM559lq33r3hdjajIJ9HEfQsSStQr_FzlkT55oTy9t6CJQ0rk_t5fqZeaIf2_Kcm4zYkKxgwHSd4S1GKcnObRaqygxchVxJU7WTjoQRxlc-gF36SemjZ6cTCY3DFV3nJsoxNfvGYtezPBFzC9nKOoj7GOJvYh4kH7-W9SBqT3zv3YgWclpRhlJdB-ggG4HKoXM5NuNW9vWrRoUDEKwcv_28FlMNqtNnC4w8ahVG2_Gs9VTLWY2GgneTcdGXFQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌قهرمانان‌اروپا
؛ شماتیک ترکیب دو تیم گالاتاسرای
🆚
بارسلونا؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31516" target="_blank">📅 21:36 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31514">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qulsg3-r9IlW2zyXL5hrCBZU6zLQ-VfREskCtouv1JFFMsh6ePmrqg0PAUY1chD3UabqjS7npifotnbGI6QBFtefJ1JzfmQUIsoI4T7p5n4woiiId82w1kC-dy5rzaq2snHM9PVn2xXRP9SGOofRxA2kcHGnuZyJmvkAVP0GCOo8ZwTBcoVsL3W22tmUjk2Ip2zdYbbVybr7YXzoQjeXP3VVX-klPoi3-MWAbhK6DNtCK35VO13yh7ukUiCxrsVSmsnh7AF429o6vkTVR2_DNktGrOBI0WQFCmUE0Y2VfcemlwfXblrPmDW6cBVMeaL_BH_iX3J9Wf4MxJDGmYy_tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJz0KVa0qdUvq2XPSvRAAUfyZ4YozIGHuobCINgDg6bQN9ld23Zozl1Md5bO3g8F7hj0ZKjGxhacQMqEwj6oZmsTnm4d97uJ-ZlX2wohr9Ovqj3mxXbGEHTQDS_D4JaAp2V6WkBohViu0u7lI73w4GsBpwwhPLtlSjfoQbTpQu03a8atotqMqZLaGXaMpIXd7Q0izHU7sCDT60iwxxOjk4h8nxsIgqRGbl2HfrDU4mR2jfktHhe1ueCmDSDo5ZpJnUHkth8QoqrhwjS7GR3LD12twMT5wyGLnTOErMfVgwNAygoab8I7R6PbG0QDs_gdi2iHpS5HClakRpw_9pHlYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
کاکا اسطوره برزیلی باشگاه آث میلان: وقتی همسر سابقم گفت‌که‌میخواد از من جداشه و مجردی زندگی کنه من همه تلاشمو کردم که اون بمونه ولی دیگه لحظه ای فرا رسید که اون گفت: نمیخوام.
‼️
اون روز به درسی از زندگی رسیدم که میخوام به تمامی مردای‌جهان بگم: برای موندن…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31514" target="_blank">📅 21:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31513">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMufhdsQvsa9MM72Zc0ha99k9i7cRsc1E2kiLBkTdcftKaLnUM4UrvG26acx8LzqrrFTMynfmdwH_BVaZs9kRX9Q-OA7xK4c1oDRmgck9-DW_SS1yMcIWS_0EtwAJglxnuOKovbOMcEHU-h5tjTfE0aHmh0h_1AzrfK6N8uhqBTg9p9SY_GfImZxDi0rTyKJRPrlBz7Vpngeiml6i24uxAVuTGzSTnfI5E0JI3VMeCPbAxSIvl0KbcN0UUwcrTaQqrzAw-iCfqKWVx7Ga0RfIUM3YErjmm-1iAcK3kHbDnPSzDJaJh2GKjBLOo6IPaLFcuxzQfkfsOadQK2ycis1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31513" target="_blank">📅 21:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31512">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00694d1532.mp4?token=UKDSaiLoe55XpHIRAaPq0KhGZzq2LVRY5V06aI5FTMkWGaFK7vwAQkuA4bP4L1qghTTw2eU2A2Mp9IArMhEC3RhXVqYb7TcOSeg7g2RFdtTN_cRohaMX94GbjKYqqqbb9UiQAPM3nlhsxkX7Kut4pFEUjSTyWxQKlqQ4R05H3EX7zL1pyneTAVsMZiMPppTH3JkDLeWYNsmtw14UB6WSDyOk-fLoEsY8SbGFh4DyzQSPS2yCMVExQwaKpmMfJV4ELbpF-svEzUgOz-8FbinVEF_sVphrtqJugkxFFk4vrZjUbX_N2TOjUINHDEAllAljdzKlhEJhmQotefnBJjMjGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00694d1532.mp4?token=UKDSaiLoe55XpHIRAaPq0KhGZzq2LVRY5V06aI5FTMkWGaFK7vwAQkuA4bP4L1qghTTw2eU2A2Mp9IArMhEC3RhXVqYb7TcOSeg7g2RFdtTN_cRohaMX94GbjKYqqqbb9UiQAPM3nlhsxkX7Kut4pFEUjSTyWxQKlqQ4R05H3EX7zL1pyneTAVsMZiMPppTH3JkDLeWYNsmtw14UB6WSDyOk-fLoEsY8SbGFh4DyzQSPS2yCMVExQwaKpmMfJV4ELbpF-svEzUgOz-8FbinVEF_sVphrtqJugkxFFk4vrZjUbX_N2TOjUINHDEAllAljdzKlhEJhmQotefnBJjMjGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌امیرقلعه‌نویی‌علیه عادل:
خودشون برنامه‌ دارند و مجوز گرفتن‌ از اسرائیل مجوز گرفتن یا جمهوری اسلامی؟ اسپانسراتونم که مال جمهوری اسلامیه. تا جایی که تونستی تیم ملی رو زدی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31512" target="_blank">📅 20:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31511">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/actF9ZLCDRfyPAjZ5ZiLqreTQ5JnGXTtqHW3Zi-sy2GH-Ekr5Z9P6pRkYYpmDqHLC1kJLK1bwpBbquQbCylJqoi0A_cPATIowUQ17s47EbCaj4k_V1--SkvWNLeDgMK6FgQrnWf2PI3rWI64EH-NvL9J0BT3xukwgZhzZcy-VvrMKdkbAcvZDzjdJmxwafWk7v9zGi5nSmWl_wqyjl-_MMafgg9N4C8k0j94xFEftf99mkqBPmLV31q-smv0FYfZR_r9NDeoIurSjf3iIXrO7MOHZ62Uwr1M09tfUANkznFXRMV-WnoOGLBtOHC3Y9C6bN7ui2Fwc4G_MvAw8sR4BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درصورتیکه سازمان نظام وظیفه پاسخ مثبت بدهد؛ علیرضا بیرانوند دروازه‌بان 34 ساله تیم ملی با عقد قراردادی تا پایان خدمت سربازی به تیم لیگ یکی نیرو زمینی تهران خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31511" target="_blank">📅 20:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31510">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=GPoVZZniGDc4CQcJ3ub3VUtNVZTBHmX135FMScUft-XbK8muUFxebqlcbPxZ9D2C6iMPIpIMZEYJrtxTAVXli5-R9WmWK2dUCHUuMuQC6twvV0mxBjS6kOh8d242KyNidmDMOCYt-2iMTtzz7ckD0aWKepA0Z065onS9WnZBNeg0KDPAyz1FATk5Vyz0uCVWKXe_9qvOgq4LGZPbLF9mANx1Cadnm8o8Ug7Ttu_ftb9Nm5sTjEQpph6JQJ3Idk9prnub5yxSBmMnhjQ773IdcHdvUCUK0KI_W7aXq1zk-vJhkJ62RtJidEcpSZXsz9zpt1ROwPJ97O9aJOWDFrzDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c7f86dd8d.mp4?token=GPoVZZniGDc4CQcJ3ub3VUtNVZTBHmX135FMScUft-XbK8muUFxebqlcbPxZ9D2C6iMPIpIMZEYJrtxTAVXli5-R9WmWK2dUCHUuMuQC6twvV0mxBjS6kOh8d242KyNidmDMOCYt-2iMTtzz7ckD0aWKepA0Z065onS9WnZBNeg0KDPAyz1FATk5Vyz0uCVWKXe_9qvOgq4LGZPbLF9mANx1Cadnm8o8Ug7Ttu_ftb9Nm5sTjEQpph6JQJ3Idk9prnub5yxSBmMnhjQ773IdcHdvUCUK0KI_W7aXq1zk-vJhkJ62RtJidEcpSZXsz9zpt1ROwPJ97O9aJOWDFrzDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31510" target="_blank">📅 20:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31509">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpag6kZCi71u_Blr8QioA9g_s4BUGZgo5JV4q2WlN8spsXQBW-iSZjXtXXwJHPC6pe9QscvS3jcGFKdvR3aX3QyTMGt_hyxdQSdh0c2l4ERjbiT2CWHjIoJLEp3fX8WTSGQufiHq_Fqet0YVyY21FSXsNqs9nixmIySGRyWsVXHfBagJvFjC1eMXeyLwCBgEz1cw1TPreNVOLpvi1XDC-oHWmqED0vn4xIYsIkvwxLuQ_ZTWSmCQl2OameazFeiENREOpXUjmoRZrR-PXw-O6FMQtIQ4bFzB8clxhEK_x5DBNYms5bTPZgtYjYZhwxDVusNuzg32WUNniz27E5tDWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از نگاه بیشتر بنگاه‌های شرط‌بندی؛ لامین یامال فوق‌ستاره‌اسپانیایی بارسلونا بالاتر از هری کین و لئو مسی بیشترین شانس گرفتن توپ طلا رو داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/31509" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31508">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🟡
🟢
مهدی رجب ‌زاده نیومده اولین شکست فصل پیروز قربانی رورقم‌زد؛ محمدخلیفه هرتوپی اومد رو خورد؛ درخشش فوق العاده یادگاری رستمی که پایه گذار هر دو گل فجرسپاسی به آلومینیوم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31508" target="_blank">📅 19:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31507">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">📊
جدول‌ آنلاین‌لیگ‌برتر درپایان دیدار معوقه دوتیم سپاهان
🆚
ذوب؛ فردا در صورت پیروزی پرسپولیس مقابل خیبر خرم‌آباد؛ سرخ‌ها صدرنشین خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/31507" target="_blank">📅 19:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31506">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwcAnQsdVDhJfW0383zWO81KkXmHugyNIW34cQ9cxW-MskWA6f-0wjUtcrhUySyp04VuoS8OtqIvUT-vDCozp70QxXg67pmoTuDZy6QCEeaxcyR0MqA6vK2_kllA52Y_MZiWo7PpLaF-Wog1Q6z3A33YrMUljR4_MNvPddA6vOlFx1sRko_aZpIwCIsEjSueDD8w747-0PDjVbYLf-bcM1b1IJySnt_gMTN3VDp0MWzeVki5osEp11q0G73DqRlWWuz-s5pxGUAs2TNpRmvIFYZ3euVX5KuDCVg-YOtPXOxY0vpvkCqi_HHx8HjY1HKbvWW0fpezSeR4RoVLsqyJXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی با گلزنی به الغرافه به آمار ۱۱ گل زده در ۱۲ بازی لیگ نخبگان رسید. او حالا بالاتر ازفیرمینو ۱۰ گله و به تنهایی دررده‌سوم بهترین گلزنان‌لیگ‌نخبگان‌قرار داره. ریاض‌محرز با ۱۳ و سالم الدوساری با ۱۲ گل زده بالاتر از آسانی قرار دارند.
⚪️
…</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/31506" target="_blank">📅 18:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31505">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL1p8bP6s26whkNidj0-yDedYNrCyS_zOzFHJ0593YthQxd7q6FHkHw0ts0G6bfwzjpR39cK5MdFUdTWcSdKFSfPAqPr6i1TOZBRf3TTDTn80SRIQfbjOOn2LFNL0Ps186uF3dUykaKBs8W52_KMS30QzJCx15EnW6gp-zHy-YkPDcVJvgzh0nOMdWsPfJBGpDkc2qQ3xxitoP_muk_NnOwRqjduas5peBzFxa3FgX_-pKjyVUc5o785_W9WfZE7Vp8HFaEr1dS2lZIaJaQoE3q2evFRIXBj9nKIYo6L7FDjv7sKrl4aFg-PJeyRZO6RqZEP3jkiCbSc0sHNA8lXHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در شب برد دو بر یک سپاهان مقابل ذوب آهن در شهرآورد اصفهان؛ سیدحسین‌حسینی بازهم نتوانست برای طلایی‌پوشان‌ موفق به کلین‌شیت شود‌. سپاهانِ محرم نوید کیا شیرین با این پیروزی شانزده امتیازی شد و در رتبه چهارم جدول رده بندی قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31505" target="_blank">📅 18:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31504">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟢
🟡
گل‌اول‌ودوم سپاهان به ذوب آهن در نیمه اول دیدار امروز دوتیم‌توسط مهدی لطفی و کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31504" target="_blank">📅 18:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31502">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQpBDDY2kgOUidfp5somk_H6WKUhYb_Kbo1pUF2IWQlNjXhi-aqdLtx82CZkmo5KJPYgmU4wjSnGhtAWhFzu0nWImntHplZX6cxOz-XOSVlLGsLIS2GLHXJshoGjNQogUNk135kHYUfoF0Jz_2AxzhYkWAzNqs5Nylvq4S8aW_rVKMqk0_8MQdCNXrcLrsvegYYBqeIzc11A9vXvbzJd1I8vst2uWdGTh3dudPpgU1gLhMFtfQR16QP7P-zIBHIa3W-s0nNIhLVFQs8nkFgjU-kMV3JwMKbxwuPKdHGd4UQH8dLbH4AW6TsDBE1j3Pv7pV7bO_tS9YuXt6pHpvX45Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجری‌شبکه‌رسمی‌باشگاه گالاتاسرای ترکیه هستند که گفته‌امشب گالا نوارپیروزی‌های این فصل بارسلوناِ هانسی فلیک رو پاره خواهد کرد و پیروز خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/31502" target="_blank">📅 17:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31501">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uebIoAODX5_aZw_HN-mCII_ixYVoyVGm2iUQUYrA4e80cZ8_qmmN-tdhnJBB2Jw8l5iEPzgfkeW5L5g6k6Fv2IqNuew6rCHN2AOIqDYoZGe766nMNqQv8b7TaGlufquW_BItbEzBFXy9wrGdpK-_i5sC8ID1poaelLGez6kyb3EMSFrciB95bV0IPjPvOMNfht_JlLtyRCaCFUWyTidsQNt3FVsX81izfN7w0Yiaz785Um_YZMCU47TE7DSNkaW0vviGPcMLoYuyphUWoptL7-w3olgbfLrOTHYPan0WiUh5jwUNXxL-dFMZUK4o99f4cMP67vT9SpZ5a5Oobkhl1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد استقلالِ سهراب بختیاری زاده مقابل سه‌تیم‌مطرح قطری: 3 مسابقه، 3 پیروزی، 7 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31501" target="_blank">📅 17:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31500">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=OA9UM75hSQLcdZZTtOrJKr4L31H92pzJ3YA2CcBpvipDylU7Rpzi8M5fAWFs2XMT-fZZLQMGSf9LX4nSHepgZLAB1cSnarfUF2Zm3Pph1PvnOLNLUTL7HfoFhoLuIkW1_Nw3wdDo232tk3t2X6HCOE1pNM3trfKr7sjDIV2jR3nfQP-rEccC3FkVoYnOi16bVP51gabUQJZ0kXe4-kwXQu_A9kDWnf3E9iF5bmGM-V6O9S_yUJhgovVKIgCGY-zZmU9BNQQeZ_0BQeXd9yoiwoIaXPA0rY6TlnyJpjhiVo5O1BWg90NpHzE4wAwAhR1j_8BlAEKwGU3j45FiHdCk_ngsGbqAxxobctdcM4kTk1Bkk-tu13yznYMiADvK9gXuD4cO8QOcUdYaCwpum56eVV16Kf4qSgcirALI2aVBpNpckr6V2m_HaqpeNDeVX7ij0JE_3TNmuYJw2XfR-0KFOpg1YhrL6AgxB829WWc9N1x9hk_YKG-4WITE-_l-dbdl4FAnoitfpW9oCn5PA1_WTQZNjLfYg1siIzTAN0E2iBVzIIevy3w8DTcD_nNc6cBeqKBYTvYIjH8Pvktsp_kOakJtKc1Sv7xWTXCEXEwfS1VvBOWZaPwTUg9XRhUf_3kl6iD-UwkwWUw9Qp7Se417h61N_-ehRBVCLBkou0J-dPY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6451b4b3f5.mp4?token=OA9UM75hSQLcdZZTtOrJKr4L31H92pzJ3YA2CcBpvipDylU7Rpzi8M5fAWFs2XMT-fZZLQMGSf9LX4nSHepgZLAB1cSnarfUF2Zm3Pph1PvnOLNLUTL7HfoFhoLuIkW1_Nw3wdDo232tk3t2X6HCOE1pNM3trfKr7sjDIV2jR3nfQP-rEccC3FkVoYnOi16bVP51gabUQJZ0kXe4-kwXQu_A9kDWnf3E9iF5bmGM-V6O9S_yUJhgovVKIgCGY-zZmU9BNQQeZ_0BQeXd9yoiwoIaXPA0rY6TlnyJpjhiVo5O1BWg90NpHzE4wAwAhR1j_8BlAEKwGU3j45FiHdCk_ngsGbqAxxobctdcM4kTk1Bkk-tu13yznYMiADvK9gXuD4cO8QOcUdYaCwpum56eVV16Kf4qSgcirALI2aVBpNpckr6V2m_HaqpeNDeVX7ij0JE_3TNmuYJw2XfR-0KFOpg1YhrL6AgxB829WWc9N1x9hk_YKG-4WITE-_l-dbdl4FAnoitfpW9oCn5PA1_WTQZNjLfYg1siIzTAN0E2iBVzIIevy3w8DTcD_nNc6cBeqKBYTvYIjH8Pvktsp_kOakJtKc1Sv7xWTXCEXEwfS1VvBOWZaPwTUg9XRhUf_3kl6iD-UwkwWUw9Qp7Se417h61N_-ehRBVCLBkou0J-dPY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد ستاره‌ایرانی جوهور دارالتعظیم؛ شهاب زاهدی از ابتدای فصل تاکنون در پنج بازی سوپر لیگ هفت گل و در دو حضور تعویضی در جام حذفی نیز سه گل زده تا با 10 گل بهترین گلزن این تیم باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/31500" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31499">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlQKEUsxb33f9TGMs75j58iqQcQJkRU43FiYnjMRpCsueUguRADZCEU0kSh5v-m5w70NezaJ47liJYnXFw3yvOOBeyVb7_Bdfn-7ivMzCqVYt5ir2QjGBjsvcKlfa_qB6B9U9PGeioauwMbF40vTO3dgqkuZHO1f2tp4lo1M1TJVa_cuFu6ZQX-7B3PA2J-KbDqYkeP_dbWF-ebCddA30nWG9pjVc0A2dauP43qrtMOOhVz16BEgb5D6HTSQqLiUpBTNl4lvfeIA7CiqSJAgDozZb0LPqxuDZakAf9qbl_tZrI-i8jyudyMx3-C5OUP5JV90CrfuoLHTgy3dlpNGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شماتیک‌ترکیب‌بارسلونا دربازی سال 2022 با گالاتاسرای ترکیه در لیگ قهرمانان اروپا که آبی اناری ها موفق شدند اون مسابقه رو دو بر یک ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31499" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31498">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بانک تحصیلات ،بانک  مشاوره اخذ مدارک دانشگاهی. واحدهای معتبر ایران. کارشناسی، کارشناسی ارشد، دکترا.‌ پزشکی عمومی،داروسازی،دندانپزشکی
پیراپزشکی. با استعلام.
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
@banketahsilat
⬇️
⬇️
⬇️
⬇️
⬇️
جهت ارتباط با ادمین
@tahsilat_azad
@tahsilat_azad</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31498" target="_blank">📅 17:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31497">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Shi7333hWhMituwibBZKqun7ez91VJSSWq8tqZN90w9UadSDWRXAnIOSoKS5mgQ9x0QSRGQE3Cpo4MJJjZDmuFaRPbjBzX6zdTDX1KggZ28Q4Ti5ZZKTooAG6vCMQDkI41Pt-WA4GqDRLwvTTZsLd5x08Ca2MTcneYpHJuLPQF9FaxNJu0Z3ma2BvDGKdW9XxO0pIW6_KqMA7v5ZFOBNWSNtsIJywQxN6sEYqjn9vY0naKYhY-jDLXKl4_3_tLLImQt9tz1Jkd8gxajH5n6uYRzk3Mz2PnW_8k_8V_-kJ6M5gO-Qo58tbP8kSU3xRTgl4-zMHJQ_22EOfXVj3_qWcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیدارفرداپرسپولیس
🆚
خیبر؛
ششمین تقابل دو تیم‌است. در ۵ دیدار قبلی خیبر سه برد و پرسپولیس دو پیروزی کسب‌کرده.تقابل‌های پرسپولیس و خیبر ۱۳ گل داشته که سهم پرسپولیس شش گل و خیبر هفت گل بثمر رسانده. اسماعیل بابایی، ایگور سرگیف، علی علیپور،اورونوف و عیسی‌مرادی گلزنان تقابل‌های این دو تیم بودند که در دیدار فردا هم حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31497" target="_blank">📅 16:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31496">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=WVcopouTEJbTXNf8m8r5u9Wr0Z9vmbsaNCPGAHR5cHk9sBTR31mH9odNViFXqQhCcLwO-h6M8elj1rVkatLNCbvzjWQeYlocKHG9fJtCI7rvsubdEAZZLJVt8To9UTmU6Y-sVfCxzq-vi4VSJI4ai4h_SsWsNBTZykyu1bqJijtlogIU0Ke9OwNH6AsAuJLcntLxN9qi82ZV7ZKXtfCRqJAoeo9VH7N6Uxb9C5ID4kXCGGHGRjGRG8dlX3tfo8ko6Mbs5onYsPCQxb7Xsz4iPlF7kk1JVlA7LAaLShpFM0R__fW2ezQZuIJHJZkbzb3594YEuMI9XCOOVZyolU-x2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e5fab635.mp4?token=WVcopouTEJbTXNf8m8r5u9Wr0Z9vmbsaNCPGAHR5cHk9sBTR31mH9odNViFXqQhCcLwO-h6M8elj1rVkatLNCbvzjWQeYlocKHG9fJtCI7rvsubdEAZZLJVt8To9UTmU6Y-sVfCxzq-vi4VSJI4ai4h_SsWsNBTZykyu1bqJijtlogIU0Ke9OwNH6AsAuJLcntLxN9qi82ZV7ZKXtfCRqJAoeo9VH7N6Uxb9C5ID4kXCGGHGRjGRG8dlX3tfo8ko6Mbs5onYsPCQxb7Xsz4iPlF7kk1JVlA7LAaLShpFM0R__fW2ezQZuIJHJZkbzb3594YEuMI9XCOOVZyolU-x2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
معوقه هفته هفتم لیگ برتر؛ ترکیب سپاهان برای دیدار مقابل ذوب اهن؛ ساعت 16 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31496" target="_blank">📅 16:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31495">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMhuk44Fk5cgsHKN6txFEiXrgo1m4U5nKKs4fEXf2YGA_L8GyUmddW1sce5ADQWFNwxa-fe8_5Dy4AiCh-3K00cMMqXJsaH-3gDGdWU0dI3gvA-q0kN5oI1jemvWgd6bSChq5f6r_v2KLn3xgFFeapeYCRe7lZymcq8jng6yWQoco07NqqX3aBwNqILmTcJBxGqR2tP1CHgVLZJvb8y07sXEAZi3OZ5AEC0iKwX3teOWVFi1bNw8DlcQMfdlF7SKKH1YvCtxgy7OcxFBW7JouGjRhmxJTprjSeXT-RCyRvlRh_Bwba1bDsZOEYBsNEhkrSeVcmDq5lOMIgzNIKGPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ یاسین جرجانی مدافع‌جوان فصل قبل آلومینیوم با قرار دادی سه ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31495" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31494">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6JFABWpJetFTY9nmB8YErV_2rU5a3BgAqcOmIaQVoy2nWGVylHdlov5jN375ntamICe4cMRAt4tO4MJIRX8QWQKXrMARPuGKVgOLCQxR1dA4VFMNGxYAwjTwQzIrLZ6AAE58bLWydK-q75OY3fGcoqKRgeGRk91cDP9CsBpe62QsA6FY9EBEoaLdXiFgOJeKlfwPGHctW_pQnkdQEEUkCztyZwYaKyercfu9ubdRdQ4mwSZO2pKLZlA8cRHow_mPWRv44OGyhAnGZg4Pd485sSULrljWn4RZEYbTB40zGG4B3iSKf_OtzpFVP_F--M6NHE7WdddeCEatjiy9PQ-Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
دانیال ایری و حسین کنعانی‌زادگان دو مدافع میانی پرسپولیس به دلیل مصدومیت دیدار روز چهار شنبه مقابل تیم خیبر خرم آباد رو نیز از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31494" target="_blank">📅 15:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31493">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayG2j6sVuGghDqjiohN6VYpY2pTGzntJa0UjMUAAHVLpNglULX0LIbvhKOGqkmcCbhNfWNjBm_qyVBlCGJx5G_U84MlRcaJLEg3t1djbIXY52za-9iNXcKVSQahsCTmIzee-c2BpDcK5hlfy_WVVIopuQYlNZfm_PuyxG_6ShT3vDJ3iSCR9fgBhgnFNJ8MPG2fcwMFvyPZXSoFZudo1BlPQejUUPu6POkPPiDUq1pe0x3e9eu4NrKFpfzykN3HZI8WiFSRLe4dBHWyz3qFyFpSYP3OuYCqJr3EpxZ1GRCs1YZIOuozwDSew0oPAXfTU6dRZ_9NxAA4z_fjsVkCAIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ معوقه‌هفته‌هفتم رقابت‌های لیگ برتر که قراره امروز و فردا برگزار بشه. درصورت برد پرسپولیس در بازی فردا سرخ‌ها صدرنشین میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31493" target="_blank">📅 15:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31492">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAZgFIw6zqNn8lFNpvyxjXEadBeH255_H03Pz1g_K-maVs8abtIBPQ79S4PEo1QaROYZxjdzY1ELYj2RCcMFRD0_Goh-LvvgeJgAOxvJmWucyYQ3Xvylj0hBCou5WUdWc8yE0r5unc5xD1JbmatZQF-Y37TEE94ZuwVvd1lwq4kno1pCNOi2BI_EDrRtUj_rt9vQT0ZARla857DkkUeBpiHhUvRuGjVOgevHK1Jx9oqoBEXTKmW1hc7P0s49qr1iCS0-RzVidPrnmmLSiztbCaRD3KogbIt8yiMl3ifSHbCYJVjA_a4oO35CWSoBI6pAT6bHC6hrZ6af3G_8oLBbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/31492" target="_blank">📅 14:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31491">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4pFC5tDze0pV3DkGI4Devb2hK-KsqzN-e0fgyWPpbQ4zYDKVvpV3EIZXBw9ER-kI8SidrA_RBtAj1ryFaCom8ct-g0vn8fx136c3zjVIx0PXjf_uq69adlqCU2ldfhvM29LK_ypIx2GXtYH41h9ZpMhh12jWWD_f6eUy8lhQiLoLlYhHWqR181KbuZD5NvsRIl-fegm5Jsveni9rbAy6wu0R19_qcfCC6kOYsEDT7u0DReMD1hWpBcVKpRZhdJHUNJIydLqzQbMg7BzvWCHwl5HvC4hMRfnEYM15r2lBILfz3aFahE1vB9CWIOxL_KOzrP6_osFTktFyykTKld9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادت بدش روترک‌نکرد! جواد نکونام سرمربی تراکتور: شرایط به‌گونه‌ای‌است که همه چیز به سود الشمال است. چالش امروز ما مقابل الشمال شرایط خیلی سختی است که برای ما به وجود آورده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31491" target="_blank">📅 14:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31490">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LL9JroUbf1uW7O_0XibXwO_MB90xJY7iGWQptpucH3TYXf_dv5nOGmAO0k1kDHvul3gzaLeL04vcnh7wil0MZIWnSPQGOOGPbHrE5evgXUz0MP2ZLI6mpB6h46TSk9vF7LyALIwUruC4rEyPsej7m9mzyH4zaQIPtUcLfV7ClGpnf7Lgro5Dt_MG2IqvKo_CI3HyCspdwsjTe_PyynNpd_VHALbWBPoLoqW56IcHMZ6D00dntFy5JCBKw7DpMUYB30lrv2XAjOTtBQeKaIPkDHQmgwsy86QKBXvLw5ECKTjbE2WLW5-41QlTNCtpyWLeWuFqJF1wGBrhGLEh10fiIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تغییر زمان چند دیدار هفته نهم و دهم؛ استقلال و گل گهر بجای یکشنبه روز دوشنبه بازی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/31490" target="_blank">📅 13:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31489">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0hvihS7s-rpvY_X5-_d9FIKTCEkklpOmSr72uX4UwSwVaH0c4wXMtApG3vtFFaNJ-D8-ZyCK8Xha_cRLiSVwB2u2XUQhLBzzLlwGtumSqNUHFzfVtdjbC_0jlz8K_i1u_m_FLmDEoj-VJ1xI7BXLi2iJ5FZZKRZ_OQFzdOtFtfHqUsbqQrS7A-EsUTXHegtF7KBC8wk8_0oqgdv3naLL2RbN-6sQVjHJi2bEszkRhfRvi0Abxc-TO4dfxFBb4yQ4B764M1_zbhcg5e1OTPpvdy_wJJdQ5CfczrhGPWl3DShdGk8VDB_V8ZcGmw4mlmDPyj6K9JMevPBCmQ5yB63mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛سخنگوی‌نظام‌وظیفه: باتوجه به کسری‌ هایی که علیرضابیرانوندبخاطرمتاهلی و داشتن‌فرزند خورده سربازی او تیرماه سال آینده به پایان میرسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31489" target="_blank">📅 13:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31488">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpmaPiMmEoz9huvkDrUq90tmCh5QOs1vm6coU-9uWUzQmJaFxp2saume55sZ7Wi8RlVzKPPX3dMuHjhuIt3vx19TeIHlB5nPItRpuZ7YMpsCK4m1Pvj27EXW8M8LtnQ9RBfEwt5zQrqzu0oMl6hcVCI78TMFpPxxTxJLakReGWuE8c7dtSiiawZyvgxL9bV6pco6HlngnXk_Y9JYth9CxSpSHjbm0lfkN2S8_Qqz0734k02gBYQZd2XmVE6Y17YKnHOJNoUJZIJB_52MIRM7JIA_v4OB8HQjZ0RLiQftLnZOra7bEadN3dr1GkqDrRuNkZI-KIzjluIMl0p_cAtThg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درهفته‌پنجم‌رقابت‌های‌بوندسلیگا؛ شاگردان نیکو کواچ در دورتموند درحالیکه تا دقیقه 85 دو بر صفر از وردربرمن جلو بود در عرض تنها هفت دقیقه دو گل دریافت کرد و 3 امتیاز شیرین پرید. زنبورها در چهار بازی اخیر خود به پیروزی رسیده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/31488" target="_blank">📅 12:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31487">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUf5LRCLjhDXrGJQSrbpfBBu3xXDb2vvWB-VxEmQPfwvM-CxguIdebUoprWyeWMEAp_uwBh8m1KJpJ4ZE_qJYYStbaC9d0M_JktBScapUK1d-20ZaorplkcP0PJh9ErDfCbivvyNyL4aEtM62_ghEe8r3XPe8jDoq36SnK6Sv-YYET2RSttxRLyR_348XI8mFHPX6RiLyd8eiV-VniVbrmAmS1G0J9ri1m04cVaOSm5SOfVeH7gyDC0v_ERnzFEyuqM3PjHR4Tt4C0T9SO6qP3QpgOiD-dtPbMyQQPfVyKnzZKh5heCfIlRIX8nCHRHobHhtgJJcqqWV2x46or4-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکثر مسابقات لیگ برتر مصر رو ایشون گزارش میکنه و برای هرمسابقه 5 هزار دلار دریافت میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/31487" target="_blank">📅 12:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31486">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s6i08acIyoqhePAHTdBSkDfPTEIzQUuFSGRbHL800A_KlTc9Vp3yoDQJq1Djf9q8pf8TJH1tBq3i291SQP3QKBUo_an6Q0Vn92Qzidsvtno5b55b-i5xrOrQm07wRAjmsv6zMWCdx_XzAse7KRpLYjtXH3MX7ByBM7NVgTXSsVf-ycWN_t0MWAwKyxiHCNGzTD4LhPdXYd5QSsM9IwrMgn2XluW5yDwqf52WydW3S6Jku-h_GIydTZa1cYnTRn-NP1YUbmxYh6IJ0tXLoYYdwWZ_Ak2Jl9foBrJCXVrA7loxXJHsNhUXndPl1XaF-Hmh3odgFG_eGbMdlzKidG-d2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسیرسفر گلگهر از سیرجان تا بحرین را مشاهده میکنید. پرواز از سیرجان به تهران، از تهران به نجف، از نجف به بغداد با اتوبوس، از بغداد به مسقط عمان، از عمان به منامه. به همین دلیل خواستار به تعویق افتادن دیدار با استقلال شدند که مخالفت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31486" target="_blank">📅 12:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31485">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=qRujffSq9FuMRyyXxVujwDdCZe8wa944SWgO0gAFTlynUBtKpZeYGdl9NeD2ykByELOAwZzlbRaei1EyOuE4WKNZoElfKL_3ncLT4hjxiGMKjFTqIs-e4hir4_fUE9p9JcyYzYrF-pNJawxA9D2BsW5V8WA3cXGB9qrBTsKUJ21G-BUv5Uq6mdR5WpOvKTI6Uf1IhP7wPM1qwTcvXGmiGWdEVKWiiTbwTd2T5fcALhqxJ1EkS4CNCcSruavOhicVH__P6h2Orj27a6WKsJB4p2s5_cWPlBcz2uhR3BIUtRs7t24Q2McBJs2WcAY7Gxo0V4UE5Fhd-SJLZykMYTMGbDqYgQsQiwMM_vce9ZbRcGMZyJYaU8Pvxgpp8MaV1rVY7nRO6qqeHGRa27HM3PVBYi9XY3zX45i0iEneBwA3i-agYb8aClrzW_0Fo1Zo_heyoYIsxopAgs-KvUxVrBVzmgy7VgeN2YRBlcXpSa-1CKjqdE6J0-O0cUuAwiqTovqCVg0CB2Get7bhzGzfd3-i6Kv9TmxY8akPaIK99qiFZLniteujRzWGYrPg5wFi2yNFpdPFV__WaX-GZwv44phNmqv7lODRAAMa6SkLBxeF31-fSgIKgplXCtkYnN3XQtx5jS_pf3lQq9vstu8AwtaFujwUgK5_b10Mwh1Ls0eJEMI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e001dfa4.mp4?token=qRujffSq9FuMRyyXxVujwDdCZe8wa944SWgO0gAFTlynUBtKpZeYGdl9NeD2ykByELOAwZzlbRaei1EyOuE4WKNZoElfKL_3ncLT4hjxiGMKjFTqIs-e4hir4_fUE9p9JcyYzYrF-pNJawxA9D2BsW5V8WA3cXGB9qrBTsKUJ21G-BUv5Uq6mdR5WpOvKTI6Uf1IhP7wPM1qwTcvXGmiGWdEVKWiiTbwTd2T5fcALhqxJ1EkS4CNCcSruavOhicVH__P6h2Orj27a6WKsJB4p2s5_cWPlBcz2uhR3BIUtRs7t24Q2McBJs2WcAY7Gxo0V4UE5Fhd-SJLZykMYTMGbDqYgQsQiwMM_vce9ZbRcGMZyJYaU8Pvxgpp8MaV1rVY7nRO6qqeHGRa27HM3PVBYi9XY3zX45i0iEneBwA3i-agYb8aClrzW_0Fo1Zo_heyoYIsxopAgs-KvUxVrBVzmgy7VgeN2YRBlcXpSa-1CKjqdE6J0-O0cUuAwiqTovqCVg0CB2Get7bhzGzfd3-i6Kv9TmxY8akPaIK99qiFZLniteujRzWGYrPg5wFi2yNFpdPFV__WaX-GZwv44phNmqv7lODRAAMa6SkLBxeF31-fSgIKgplXCtkYnN3XQtx5jS_pf3lQq9vstu8AwtaFujwUgK5_b10Mwh1Ls0eJEMI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش بینی جالب بازی‌های امشب هفته دوم لیگ قهرمانان اروپا؛ ببینیم‌چندتاش‌درست‌از آب در میاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31485" target="_blank">📅 12:26 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31484">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7kBwuzEru8MIqx81eDUHozLnHI1dqNmmcbNMC4sGRWFEpccEM7qx9FQR3D5Cam2C5XuHn1qBJ85RN0z593WViSRJ-myMHKk86Z0G0vDNUgrHtDEHOt59JKZK04tfPW4QEZUG8u2Uh_y2FZNKnoI0U0pHsHhoahZZWGU-4hbiL6XFYBsUU2FjylivotQQ8ECQI3Ouyd_4fP6aNRHoPTBOVD6_VtwzAh-wLB46rZH7Wcgv7FpFKRPdkf78kBwvxx1J_SYWq4fYBPG9-MsL1Q9yPfouKB7YNc-B9n38VlGADMR99gqVrJaEpOMp6hkasKbXzieZpvaY8s52AglT7u4mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام رومانو؛ دنی کارواخال مدافع راست رئال مادرید با قراردادی یک ساله به ختافه پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31484" target="_blank">📅 11:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31483">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kr0drrjz301vbhAlQQWtMAyWRUX-Hz9YQhaOIuGEIKJhZZqTZGidpAKtxBroA0KBwPlOkBEuebuXxgx-1fbQBJqEgyiPITJEWgRt_mN24uVwptTCLIqKzfmQ-qtP2UwDGhze44V9ieB24WX2A0Mo18TgtH-xqOnJSOCrRXi5Cq8tpeyBnCvedRyer2Ru_VWW5KgCmcTr4-YedmbnrUXaTF_QfVFbaw8U5mj-maGX4ZUCPZ0Kyf7RK06_OrQafASfee951EUFynw_IiR5GA5syECH09l_OUxt-jBLokiqGTWhJrY-VoOt64Pptmhe6cYvO0EB_NHZCXM0FeEmi7tAMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حمایت‌تمام‌قد کریس‌رونالدو از کشور عربستان در جنگ با حوثی‌های یمن: جنگ هم شود از اینجا نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/31483" target="_blank">📅 11:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31482">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBQz8Z0tM0ZdL7vB7qyBiWHmPshxq5-elzia3ibCQl8JJ4RGzQgRvCRDA2DmDh3Z1Nw36WalMGf0cOW60rW4gxHutBUBIr2cHHr0MIbjh1rxR5mxXo_JgdrsIDloWlYe3ihe7Rd8BjmY3Ha4X7KN1dUmOzvlaOIDwvIjifTXj8npMrerG4voTiDnXd703fz5TI3B--k4GLV-V3Bnv5m77H4UXqpFQ7YV_Gi_BvnJhbP0qFPUlCGlO2UB7Ka4xEbdt2hXQGufo4Z1DyYiAnErQHiPy4aBYA1SrJEjMbn78uRCXBrKVKmrI00ezUHgNoqzc-JJNIX9IazHshtSrrDQwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بوسه کریس‌رونالدو روشمشیر و درخت نخل نماد عربستان سعودی و ناراحتیش از جنگ تو عربستان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/31482" target="_blank">📅 10:52 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
