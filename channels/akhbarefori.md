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
<img src="https://cdn4.telesco.pe/file/m7bCQLEfXHB3TCwQgHen6R8sfZ8XWSGlfBfgWbKqP7KQ7drigxpzcb86KKN5P1iOzueWl_7twW9QnzLsmMXa_JfvJTC0Q_tKFZVnc4TWOP4snIDY02DWBPgzoGmE3ks5WuPcdcqcq1wr5-b951ELjR57nL3iMdnKiTsmswV9CMCc7d4v2U1LEWBrLfMAqYiuNeCDF-qhkfhPlXMxs8TNtEjNg5CvxPfM1I0tH3XZA5ngtVS9aJz4bIyU1Ni_FDLWyfx3foVrfVOyuB1YcG9XCxbOv3sJApkHu1ZfNVO_su1CkxxZG1q2Z2REaQqE0-PX_IkC1hlHsSUIiEyLrsuEfQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.35M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-667458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AD0Ypr6kHDQv60QT4Z5vgfqVntQNNZ-5PQ2Xo7kyknLUGGeQLxgtao5Tu6kzvkz1BcTLqgX7T8-_SM7-_PpG42QwMAWlkrjZeVe8TibdQfFCxMMQh4HFN_fAl4sBPkZ0N7iWcMRe98np7ho26CskrHakUL7Lc4naai_9B9k0g8Tu886v2XvDZGFT3DtFD1-Ps7w1gdQbJ4we80On30eI4mO7gLDKnQXHCOEn5myFrEX1p4vm807pOEKBC3rffaZTbmKIM9IRKkcYUHQFpoOPG61LCq7-3iTybDmaSR6knbZKHcqMxyh0D-NeawEdH6bSu-8ZVgmDXFrND8QCOHSNWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عبدالرضا داوری حضور مردم در مصلی تهران را ۲۴ میلیون نفر برآورد کرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5 · <a href="https://t.me/akhbarefori/667458" target="_blank">📅 15:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
جوکار، رییس کمیسیون امور داخلی کشور و شوراهای مجلس در مراسم وداع با رهبر شهید: دو ماه بعد از اعلام قطعی جنگ توسط شعام، انتخابات شوراها را همین امسال خواهیم داشت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/667457" target="_blank">📅 15:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b2cc71a3.mp4?token=BIjyVvZnAd_-EUHICDIjN7WQ0b8Csw4Fii3Mn19rrASTabAC5OYrzMCKACCdtMzmcBLOVhXEtDlaSc7mWaRGwzWv5adx0CJPylNcQFmOADH6NTkoGozQ0qB-2XTUb3urbvcw6Bt9xzl7rUDL92ka6GBPAP6GHD6-9ywRKMF1kAL4OXUDNk9ENO25v0EZMEe9F1PZ8fU-XRI32xtYyPHQy-MNVyIxO8u_PEQiNFiaEj-AFCazh7q11-iYbrT-A5ZGIHYfunce3tgxS2j-INnVR-boRKEtwUIsoTUTWxKiYJyrO3dhirye1B464GzmkL3CChPbn0Sk6tyMF88MtI-hOYUIoPXMMdbsi3Q0jwPGakmkZgJpFXWB3hW_LUzLM6fhiqOXJl4T0bRVsNzt-NOA-kc-zfV6N-OgAXqPcMkLNwmfnkQjqgPyZOXKu8RQQOiFPuh7VsPaV8zYFPrZlRzL5QIZ9TuhyvOpJ32xL7D5H_Vuq-szrpFi4HcZ6dXqQS8PqKy_esiJ4TT1ZwwzVlp-rLiHysnYRtA8lYdOt6VZYG91JXckgSKLfXSa0TYtiaLCSRwkdVpEITxAxFCr4P_VLKcYGBo1AdPhwxxLuz-QLh83lAkPOA2Zifa9IAvErViLyFmXdW64TcSAXrYgy2oFg0zAJbKarBWY68OTN2Tp5vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b2cc71a3.mp4?token=BIjyVvZnAd_-EUHICDIjN7WQ0b8Csw4Fii3Mn19rrASTabAC5OYrzMCKACCdtMzmcBLOVhXEtDlaSc7mWaRGwzWv5adx0CJPylNcQFmOADH6NTkoGozQ0qB-2XTUb3urbvcw6Bt9xzl7rUDL92ka6GBPAP6GHD6-9ywRKMF1kAL4OXUDNk9ENO25v0EZMEe9F1PZ8fU-XRI32xtYyPHQy-MNVyIxO8u_PEQiNFiaEj-AFCazh7q11-iYbrT-A5ZGIHYfunce3tgxS2j-INnVR-boRKEtwUIsoTUTWxKiYJyrO3dhirye1B464GzmkL3CChPbn0Sk6tyMF88MtI-hOYUIoPXMMdbsi3Q0jwPGakmkZgJpFXWB3hW_LUzLM6fhiqOXJl4T0bRVsNzt-NOA-kc-zfV6N-OgAXqPcMkLNwmfnkQjqgPyZOXKu8RQQOiFPuh7VsPaV8zYFPrZlRzL5QIZ9TuhyvOpJ32xL7D5H_Vuq-szrpFi4HcZ6dXqQS8PqKy_esiJ4TT1ZwwzVlp-rLiHysnYRtA8lYdOt6VZYG91JXckgSKLfXSa0TYtiaLCSRwkdVpEITxAxFCr4P_VLKcYGBo1AdPhwxxLuz-QLh83lAkPOA2Zifa9IAvErViLyFmXdW64TcSAXrYgy2oFg0zAJbKarBWY68OTN2Tp5vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر رهبر شهید: برای وداع نیامده‌ام برای بیعت و تجدید میثاق با امام عزیزم آمده‌ام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/akhbarefori/667456" target="_blank">📅 15:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
سیا: هوش مصنوعی «سلاح هسته‌ای دیجیتال» شده است
لوفیگارو:
🔹
رئیس سازمان سیا در اظهاراتی کم‌سابقه، پیشرفته‌ترین مدل‌های هوش مصنوعی را  «سلاح‌های هسته‌ای دیجیتال» معرفی کرد.
🔹
رقابت اصلی امنیتی میان آمریکا، چین و روسیه اکنون بر سر هوش مصنوعی است.
🔹
همزمان با تشدید کنترل‌های واشنگتن بر مدل‌های پیشرفته هوش مصنوعی، دولت آمریکا دسترسی به برخی از قدرتمندترین مدل‌ها را محدود کرده است.
🔹
به گفته رئیس سیا، حفاظت از برتری آمریکا در حوزه هوش مصنوعی اکنون در اولویت نخست امنیت ملی این کشور قرار دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667455" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDaWkNhiuL_YPPZy2xPP_ROqvmvVhRpUz0eTeJRCQhzTp6bkE6WOppjgPBDy-VY7PCADxi17NYhd_2hcPgh_FM7K1Pp9IsBkjWK2aV5fWRsQyN58WiwsHRcvJdiprfu7RiA8sFcOnCq-X0JM72GsROltUdGDtMeQIo3Z6_fJP6ySGBoycq3y5v5dD1HYhyKQZBFJdMDkMPiJGsgmvMLbrKSUGdzqFJO4f88vl1wB0ZoqaWBv0jZ7qomxpSR56OFaCwynirUU3KxKbGHnNgFTGEMZm03FRIlVo7lK9uMr8sLSmVAM3KgZ5_n2xV2Fg_0dM-eY_1oqNmjkGvKARX330g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازدید وزیر ارتباطات و فناوری اطلاعات از موکب خدمات رسانه‌ای همراه اول
🔹
سید ستار هاشمی، وزیر ارتباطات و فناوری اطلاعات با حضور در موکب رسانه‌ای بزرگترین اپراتور تلفن همراه کشور، از نزدیک در جریان فعالیت‌ها و خدمات ارائه شده در این مرکز پنج طبقه قرار گرفت.
🔹
وی پس از بازدید از بخش پایش و تحلیل داده این موکب، با تقدیر از حضور پررنگ مردم در فضای مجازی و شبکه‌های اجتماعی طی ایام برگزاری مراسم بدرقه رهبر شهید، این حضور را باعث خنثی شدن جنگ رسانه‌ای دشمنان و کاهش فاصله میان فضای مجازی با واقعیت جامعه ایرانی عنوان کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/667454" target="_blank">📅 15:20 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667453">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
استانداری اصفهان:
فردا سه‌شنبه شهرستان‌های کاشان و آران و بیدگل تعطیل خواهند بود
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/667453" target="_blank">📅 15:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667446">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SscTzt6-1-21xwd_Dy1SDEpk5gqROgFPqH5czdjgcKl1nD2_7T0hN5DeAY5ZvHLF523r3-OoGEJLaKlb39zX7s8cGtnmxEiAnpl8UESrBcTbKCrYuRELWALAgZKyQBZzfALq5voONX0yAT57UW0tCNBxNsCliNerVc9ezRZDV-8BXqt2tJp0j9s05wn4eLH4s6LNRzDVi0DLulPYese3Ox-xcWNEYH7fHIXKMXPK5Y-DCQTV31oSGSDaD5_4MDsFztA0FlV3pcJFAJ5ObEgryafQo_bqFIohDlDwhpwg4m_hfyVGNqCGQUeVNV-ph8jFwYWZ4RRYEHASOrMN5phAWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CveorGCcrkn4aIwnic-Kjt2fdqri3JlPZVKLv8-aHzOTxmgRGcdT0ez3ftSS9VgjHkfXIAkhtAAY6qx1DDm3uo90cDydqzghKRkFG5vOusOYoV2Z77eVON_GQpB7AHZ-5pVJTLbntUfVzKa0vzuGrhu9GXfychHl5NELSM8uYP0g2u-TnQ2RfV1wvVvXYJMZ5EDD5MYuHW3bcPzAQXnucbZ2e3lMpBbPt8mvSaoAmQrye08s5G9G6hG9l3iFY38CEQXtBmCUt7QtFzCj7DmUW5hb8dtlNOA1nXsChHlv_vz1YSRCnnd-2UN1kKjbXokK0QFCTCLsWWtWwzIoAbErww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxvNpeAvHybZjY7ioBC8oSBdWmbFY4y0OinQhLJb9NN9gq_prI3xSM24enElzObJHjQCfS2gz3KQdPY--k6ELkgprY8hDVSBEMpBbt3LhSlJVO3mAC49P12USwGeywjlmK7nQZam0xSMwVPmrkYEx8J1CpTZ2d2zboLNRAHM0n2eYtCodp4PKWhqzl_mV-HF0RXOT608luivRMadV1xLv31YrVrVTey7xaDi1yvSm__J89yXRDhr0r2koVNm1bRQYy6-lay7B2AYQBG2hMuyBBkKdJ4SVR68WkaKm9D5vgTsADj2cf7TcL4L9oIxeQaQuLQ4AooQM3MAzgYNETajHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MdeY1dGhFQ__PthQnP1vYnokfNPgcCUGKO6d22TmncGgwb06ieJeAq_mBkwPPKhukubL7efscO_1rtkLCU34VcWpTM1-Fcz5NQxYNQw1PIWzMGI-FTGuFHY6oIFgbJ8gAl6ln9X5wbhDKQzbf2IsB_twPobn0-DwSZesovuxVEihV1M-oVbtMpgu35NfBLcBMSLHgEVRmdF9gg1n1kPV44AddA3uBrXoVrpbAzk5mLR6B9h7GisDHzC31IRi5jFDK-RNR3hFMsBiPzQCuWsjRVJVDAboRwWqbOwfZueFAGPtfurMXKl5kUt9esanX7mHPgkmu_xMCNdu0YjondX0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzFXgl_ycdDUwlpeLQoqMDNBGvYKb4qqjrbnaliJNoaqN6_2B1tOYynooOX52_5AtUlBGfhcRNS8QNNGrhxexBHMj6MIX-X0Qtu3DNAZoCyIRxIGHNl1iZlrAzY-5u_uIw194nX4902WiZ8MEf4e3MYFMJKANzYksZD9yeVLjITvtqq0T0iXYfNF7pq79OmIoYjzqQLxdKEzz7FSamH6bz9YBtKBBERTOflE50HqIytiAG5nu9nI3eZeYFz1g6RpX_5BYIeZNvM5QffL2tXSneP5gU1TYoNU6TPeK4ya-GXy3kdMx2dB9oJOR-0tiGXwXzbn7fJUhT8aj6dM0Gkngg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T3aykSQmM9R4JBipkGzTIR8XYqQE1MtXLxFd442qqqKQb_3VSHlF1FHm0GBJMI7MlUs161M6IHP0dD1eDLrqOAAwCWgDt92AZ1wx0x9nh-lRbvq3GIEKyHwvTVlI65rdYJlkO_1cChv0CtRI-fBV6_CjbEjVG5PcEg7jXuoukRGfrxsvPaSQwczY0U-zyuOObDDCXgoC4_FWW1PdR1FRTmIqBQcaoxG3vQV8QbIMpRB_9Y7wFVdvjcUHclviJQXBLwIJ81li9ejPUdf-mppQYS6_7rwTAirl2UmAUn312PJWmttAmJfYdST6Cs8qzHGY9bcwPCpxc9kU-e3jX75PEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i1FaSEhmNzXHRIQCGd8OqyWqwDVM0VMM1PL_Go9fuoIU15XRo2j0YFRkgwIZr_CSqXkjv8GNWQh10T1jm1_vF4pU4tIS2GzsnpaHNlHw5MsigTFKq-JrYCc4Bdic-ydxewkwzU0ypDWQ5gxS77Y_QbwlUXhBlnMjQs9Z2UjsHaZVN6Fvb-ngdK6jYuxA0V1Qrnj4k0vQudfSuYd49u8EPQkYsxFSC47TVgQA75wByOeZqBM7x3FsXKggtT1Fl2kogzbikRlz48OHg1tdZJNlUD0DI3vWOv4nLGd5wFgkczRRgUwpxbsIRxpX7h2Fv154j7YOIo7VPGJOKll0eR0FJw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ایران کوچک، میزبان زائران آقای شهید ایران
🔹
امیر اشتری، رئیس سازمان فرهنگی، اجتماعی و ورزشی شهرداری کرج در
#گفت‌وگو
با خبرفوری گفت: موکب این سازمان در ابتدای آزادراه همت با افتخار میزبان زائران رهبر و آقای شهید ایران بود.
🔹
خدمات فرهنگی، اسکان، استراحت، پذیرایی و... در این موکب ارائه شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667446" target="_blank">📅 15:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667445">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f6aa542cc.mp4?token=S1iQRdownBcuycwpW0bjAZ82oBT5mnYuwqPAqJBdi0aH7VewY8q749XxIFqnNJdZJOJEgYDKa7uSL3CJmL7yDDu_AaLG4FWWyeVLHcAropD7JFkZCBAm7uxKgNoWwPuwmdQ4QIZjbS_7K1ydu6kcO9qBBvzO-nDryCxgd7qxotQU1NjWNMOnTfIxJIt3fztitwJs5VVEnROrSb-DYzWL7qzz6WfBx1kSLs05uW1JFuUKWOtI6ubCadjuq8xax-lhmNW1wyffeUpBgjm67rjfKQgQN1UTSgNlsfNsTsIcmiYjACG9SkIlyMRyxiEj3GRsobWSwHbjWYB4hx3NUsYXaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f6aa542cc.mp4?token=S1iQRdownBcuycwpW0bjAZ82oBT5mnYuwqPAqJBdi0aH7VewY8q749XxIFqnNJdZJOJEgYDKa7uSL3CJmL7yDDu_AaLG4FWWyeVLHcAropD7JFkZCBAm7uxKgNoWwPuwmdQ4QIZjbS_7K1ydu6kcO9qBBvzO-nDryCxgd7qxotQU1NjWNMOnTfIxJIt3fztitwJs5VVEnROrSb-DYzWL7qzz6WfBx1kSLs05uW1JFuUKWOtI6ubCadjuq8xax-lhmNW1wyffeUpBgjm67rjfKQgQN1UTSgNlsfNsTsIcmiYjACG9SkIlyMRyxiEj3GRsobWSwHbjWYB4hx3NUsYXaDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار لبیک سید مجتبی در تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/667445" target="_blank">📅 15:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667444">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
حرم مطهر طبق تمام سنوات خدمات خود را به زائران ادامه می دهد
مهدی شاد، سخنگوی ستاد تشییع رهبرشهید در ستاد رسانه‌ای هلدینگ خبرفوری:
🔹
۴ مسیر اصلی منتهی به حرم میزبان حضور زائران خواهد بود و به طور مستمر تصمیمات به اقتضای شرایط اتخاذ می‌شود.
🔹
تشییع پیکر شهدا به سمت حرم انجام می‌شود و نماز نیز اقامه می شود و بلافاصله تدفین صورت می‌گیرد. در مشهد وداع عمومی نخواهیم داشت.
🔹
حرم مطهر طبق تمام سنوات خدمات خود را به زائران ادامه می‌دهد و همه صحن‌ها در خدمت ارائه خواهد بود.
🔹
از صبح چهارشنبه محدودیت‌هایی در بافت مرکزی حرم مطهر محدودیت‌هایی اعمال می‌شود که بلافاصله بعد از مراسم تدفین به چرخه حضور زائران باز می‌گردد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667444" target="_blank">📅 15:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667443">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
موسی احمدی، رییس کمیسیون انرژی مجلس در مراسم وداع با رهبر شهید: در تابستان قطعا قطعی برق نخواهیم داشت و در زمستان هم احتمالا قطعی گاز و برق نداریم!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667443" target="_blank">📅 15:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667442">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b5e671d06.mp4?token=tP9-4gm8Zn2hW2AA_B7D2Bqg0Nxhcs-dVaSrbUeG-OFKcVdPMdsE1GVu_sxpsgrZ0SF732NaFzvH_7w2vX88COOQhPVY5KONVLgUJdp0picOuByS_pznfAyuTtt3jRzeLYsz4FNR1SBYDMOaWApu8rgyM_hFSU0f4EWrGjvRoo95pOoHEXRAI7aZ5petLnVdDIga7-XIPLW1ZXeSnL772nEbvxzBI-guoBoeEe2pwP27OE78J9d0mgeGHmY7nmEBDGryVMhG8NQR0HVXJtS7621haOViJjDs0Pn3UB5fYjvr1LmoVk4-MuprWa4nMABy3d7yGJCo1fnToTU-Y14HCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b5e671d06.mp4?token=tP9-4gm8Zn2hW2AA_B7D2Bqg0Nxhcs-dVaSrbUeG-OFKcVdPMdsE1GVu_sxpsgrZ0SF732NaFzvH_7w2vX88COOQhPVY5KONVLgUJdp0picOuByS_pznfAyuTtt3jRzeLYsz4FNR1SBYDMOaWApu8rgyM_hFSU0f4EWrGjvRoo95pOoHEXRAI7aZ5petLnVdDIga7-XIPLW1ZXeSnL772nEbvxzBI-guoBoeEe2pwP27OE78J9d0mgeGHmY7nmEBDGryVMhG8NQR0HVXJtS7621haOViJjDs0Pn3UB5fYjvr1LmoVk4-MuprWa4nMABy3d7yGJCo1fnToTU-Y14HCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمری مجاهدت تا شهادت
🔹
ذره ذره این خاک و پرچم ایران زمین، مدیون تو است ای پسر فاطمه، اصیل‌ترین ابرمرد آریایی...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667442" target="_blank">📅 15:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667441">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">رهبر شهید (گروه موسیقی بین المللی ماه )@</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/667441" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">موسیقی اختصاصی وداع با رهبر شهید انقلاب
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667441" target="_blank">📅 15:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667440">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
واشنگتن‌پست: ایران جسورتر شده است
ادعای واشنگتن‌پست:
🔹
ایران از جنگ جان سالم به در برد و اکنون زیرک‌تر، بی‌رحم‌تر و تندروتر شده است.
🔹
پس از ماه‌ها حمله توسط آمریکا و اسرائیل، رژیم ایران جسورتر از قبل ظاهر شده است و این موضوع با ادعای ترامپ مبنی بر انجام «تغییر حکومت» در تناقض است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/667440" target="_blank">📅 15:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667438">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTHhZKKpBVguahHS5l1lWW22eO1m5hn-RByRox6hQ5aTj04pA8iv7BQ6ekxCO03DJTRXknaSIrv8bLMuNe7KfGyxO6HJXBlUDugt1FnX8hrbZWNob3ECbNT2BJQrqNQ0_P0avUMNzz9ATlqV5SvgFZBAKbxOT8DuRYQ0prx4XLEJMzGmnXdJ4rm5VgEyDGPIRaLCLspk6s_CAETm5aqYlevJ8vuSUwoMwk-iy_Fh5U2yzk_enPzXfYtQseGxqvRLhMsjUQeoW5BDGPAagyC5W78mi6tYf1qJnI1yOqmBQqKbrSy0SElr-gHj9MQRerx3-ZREX-0mq_O1mT-qSR6Vsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمدباقر ذوالقدر؛ دبیر شورای عالی امنیت ملی در مراسم تشییع آقای شهید:
🔹
ناظران باهوش امروز متوجه شدند که یک معادله جدید در تهران شکل گرفت؛
حضور میلیونها نفر از مردم با پرچم‌های سرخ و شعارهای خون‌خواهی در تشییع رهبر شهید، پیام صریح ملت ایران به دشمنان این سرزمین است.
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667438" target="_blank">📅 14:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667437">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=J_38ctK--OTev9ukq5nCY9IzqN0rct-baZXsFptEiN9yceU2R--rzsd3Iwrx05H1dZDWlNZvLRp2uS4D-5f_4Dm4nYvURPO_p6UtqsnZ_az1EQF8hOGpuUlvUUeXpd1_rt7c_Q7M1HVgPonqRvXbXXPdAwFGe9giqEOTgKDvWefLo6OeEb_9S19lfpXsKnKuT7UD0yWanumZBP7n8yKqHeSMnfeW01JQwicHR8AEGXCLVnn86mg21ngoaUNs38duWnC16YNYLehVjKMAG99G6q5wKBA2J0rzyx9S8iu9o0qzkHAxiu3juI30MxuL8OJ6_aaQnLiq7y8I804jW3v8DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d12c6b29e1.mp4?token=J_38ctK--OTev9ukq5nCY9IzqN0rct-baZXsFptEiN9yceU2R--rzsd3Iwrx05H1dZDWlNZvLRp2uS4D-5f_4Dm4nYvURPO_p6UtqsnZ_az1EQF8hOGpuUlvUUeXpd1_rt7c_Q7M1HVgPonqRvXbXXPdAwFGe9giqEOTgKDvWefLo6OeEb_9S19lfpXsKnKuT7UD0yWanumZBP7n8yKqHeSMnfeW01JQwicHR8AEGXCLVnn86mg21ngoaUNs38duWnC16YNYLehVjKMAG99G6q5wKBA2J0rzyx9S8iu9o0qzkHAxiu3juI30MxuL8OJ6_aaQnLiq7y8I804jW3v8DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آملی‌لاریجانی:
حضور مردم دفاع از راهبرد عظیم امام شهید برای ایستادگی در برابر استکبار است
.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667437" target="_blank">📅 14:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667436">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادارات هرمزگان سه‌شنبه تعطیل شد
استانداری هرمزگان:
🔹
تمامی دستگاه‌های اجرایی، بانک‌ها و مراکز آموزشی استان هرمزگان در روز سه‌شنبه تعطیل است.
#بدرقه_یار
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667436" target="_blank">📅 14:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667435">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
روزنامهٔ «پاکستان آبزرور» از احتمال برگزاری دور سوم مذاکرات ایران و آمریکا در اسلام‌آباد در روزهای ۱۴ و ۱۵ ژوئیه (۲۴ و ۲۵ تیر) خبر داده است
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667435" target="_blank">📅 14:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a3a2bf9f.mp4?token=WZm0JRuOGTmvKHmnSG8DEHYL1Zsbe1tgDYx-c--sQ-cbUvSOXh8m3IrZipVwYcqX5IHHnqxW_6j7n_N5ECRVg9Hmm-7X7_vpZU23OYJwgsidQFmELRUSrEFTREasMkjqO4WIkpZbnTIHg6jy7_6U588IKJfxPA4Y9fH7hbNsaCrMj6zrDrk96G403QfH1JncMn7ixhEIOtz9KU2UFWowsDbpdM6MNqE35YkJQ3_O0HDnLlHnhLzjqhVXsa1KN_D6cA9nQjjoq4_T-IE8jWCx34PN6y9yP-5wJKC00XQsAU5HO_4l40nyw5Io_3safio9piHo3ZnZucXX_WKMT1ds5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a3a2bf9f.mp4?token=WZm0JRuOGTmvKHmnSG8DEHYL1Zsbe1tgDYx-c--sQ-cbUvSOXh8m3IrZipVwYcqX5IHHnqxW_6j7n_N5ECRVg9Hmm-7X7_vpZU23OYJwgsidQFmELRUSrEFTREasMkjqO4WIkpZbnTIHg6jy7_6U588IKJfxPA4Y9fH7hbNsaCrMj6zrDrk96G403QfH1JncMn7ixhEIOtz9KU2UFWowsDbpdM6MNqE35YkJQ3_O0HDnLlHnhLzjqhVXsa1KN_D6cA9nQjjoq4_T-IE8jWCx34PN6y9yP-5wJKC00XQsAU5HO_4l40nyw5Io_3safio9piHo3ZnZucXX_WKMT1ds5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیژن عبدالکریمی، استاد دانشگاه در مراسم تشییع رهبر شهید: حضور آگاهانه و وفادارانه مردم در واقع یک رفراندوم عظیم بود
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667434" target="_blank">📅 14:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
انبارلویی: جنگ هنوز تمام نشده و انتقام خون امام شهیدمان را خواهیم گرفت
محمدکاظم انبارلویی، کارشناس سیاسی:
🔹
ما دارای نظامی هستیم که تکانه‌های نظامی و جنگ نرم، نتوانسته است این نظام را از بین ببرد و صاحب‌نظران سیاسی و نظامی دنیا علت استقرار و قدرت‌نمایی ایران را در این می‌دانند که یک نظام پرقدرت حاکم است.
🔹
در مرحله‌ای از جنگ قرار داریم که هر لحظه ممکن است شعله‌های جنگ شعله‌ورتر شود و جنگ هنوز تمام نشده و در ادامه این جنگ نابرابر، انتقام خون امام شهید را خواهیم گرفت.
🔹
نتانیاهو و ترامپ اصلا عددی نیستند و تمام هیکل آن‌ها به اندازه بند کفش حاج قاسم نمی‌ارزد.
#WillPayThePrice
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/667433" target="_blank">📅 14:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667432">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sf9-Z4Yeudfvqq73WlKvHtDEEgv44ckTFPrKtzfglZ-K6CuvWVx9uoA_V_3tOzYC0d9FXCOoOcbcN1dRhIKvALx4PZdh5r5pV42dzKoT54ATOtaJFTbWC8MP6ince5ktBJYAydWQO4y9jB1w1phgm_RfINvFoSWqfbADpWCqzuGZ7WmNkC7nXS2ZLwIWVJs57CqMy-8I2oclRY31mVziqOyJCCBGXkiloPWwNQIFoLqCUro9KjtipWlBBAaiZZHx4vHK3uFsxt4PMxp6Q3vfekimiFde_PexPvgzmocHKWj7LdDyNijrEklI56tzyYtnviA3_IxQkYDmJ6Tjbtx3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور عراقچی، جلیلی، وزیر کار و رئیس سازمان انرژی اتمی در مراسم تشییع رهبر شهید #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667432" target="_blank">📅 14:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667431">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTTA1RO-YVdNN0uCLX33641ay4BnXCfFfo_fNe71qhIfNSN0bLoNsERojfE0HrcIfw2ybuu6NEw8ZlauMhUhhJ1nFedUQIgvsjdfg7rE5Spdes5012EWKra_HS71frbZj9B4FA0z-1Y-M7j7vqrMVSlf5sXvW-wZfpRU5tMDCosXiwJvdO7d_WY0k3dSGf6iStU3OBGdlxV0ohLrX6v7mU63BJzf0e1SIs-5-fnMsn8NAdNgfTY1gv45gfaDpV2SF81FGguva3OcudwMNpYJdhemr-__8ppVoRMtXPDQLzMxH5eLAixu-CI6asAIP1N7qJQg8yqY5A5K9zoqj0eRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ تجاوز و فشاری نمی‌تواند ملت ایران را وادار به تسلیم کند
محمدجواد ظریف:
🔹
بزرگ‌ترین سرمایۀ راهبردی ایران، فراتر از جغرافیا و نیروهای مسلح دلیرش، مردم سلحشور آن‌اند.
🔹
میلیون‌ها نفر برای بدرقۀ رهبر عزیزمان آمدند؛ رهبری که همراه خانواده و ۱۶۸ دانش‌آموز در میناب، به‌دست بدترین جنایتکاران، بزدلانه ترور شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667431" target="_blank">📅 14:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B9mV_MR_F1CK43T5i8eLFw31A2CkFWemQ7DRSEusR02sm2uD_6-lj1hKni5RvknA__kCfHuPGwiMw9j65xfPDG-mn6j5Cfh0LJ6wndO20O6JdXsgfx5BraES7WXUaG6M1uYi3icy0RiOrVMaXNOkOl-9mi-KyjeoPTJz9WQXghS9TxPbS8IFpq7iVSz2HyHCEhXWI0xMWnGCRezYPaYAUDIF23Cz1FC-gXmlNv4-zrsmFFQJBtSuh6zSYVlUULiEsm6hrbT8l_Q7mS8l5LDEzEgivFGPZQY26K9gs0K8FFvpKCNnKQSh9yKHOxGQ23UYETu42v33SNuOh28oqcBI7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/otu4lZDE6iDl5wHruQod2-8cCVv7f4ExkOyY2DbqmKHMp7A7Rujq_JxymZMbL8RS-3Leqz2L2HG-50c4lm2Exn47Z1xl1OySnVZx8qOja7-1v7YHdq2ZD1_0vZdeiU8NIvGk6t8jS5cj3YPzHqQHDpBQUzP2PpmK84BI8Ob0-XM5QTyyWD1mlW1ENpjXyAm-h9T4iYTWPqv3hgROjLzMpSlL4_YXtjp7e_nDFYin5f7UJe7nBsZ88QYqhu9UX3Z0gUaYpTNAodR9SS7iIxi3KREnz2rkeZpjI8dKlcyGKJvlY2cdIpXsOt-9uuh8MVVMz0IEN0-VRK1lBGCyAwj6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kr4sHDaHzVlvpxO1xM3INn7IX9MLcJXP4kcQM1nZr1brbOofFEaEAY27rgElyso-LdqigXDLBVpBElQq218Why38RjPR2XFKVlU3DVTmaGJFEhxbOyslzaT9rQTBXjSYx17w7FIjPdmJcts4bYrdJ1vrFW59ziFiv-zONEukvi2fW7L5lL1aXX9j_Ac2obP9LunI7d_CypdLWO0RKfz21-Hi6YB528QEZwoLOCmJwYjuD1s3nU_PoIlh-Q9jJ5EVtgDFo5Cq2cxngUZZfgBSO5DA38t-wndVH5648_Mfi4ilxHm8ponFfmk0S7QW1SWQpmipXgIPf9G3ML4E0aCPjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FeXWnWTFX7SipjiwEKyNJOs5bCYJdQVsZGsQZieZb4XHIXjXULMCrCpjxS36QXm5jJWLUenCx70LriARJIG9UFnTuJTcwGn6AGv5FfnYpqBin-7Rp-6IIPQ-beMabL0tEcVMC9My665pTgWOqV4PMtLNG-NeiXmih5fQfTd9vkGqlNHa5jvP1VZwxj0p8fvOKYmSjwtY0hhBUVJ8tyQQ7dKvwQGJwGpt1BY1XQXKMM91T8MCMzwLUH8yukCxdsF6YWtnB0Pw1bfJCrRuvM_koCqF1MkzGZkNByAszkWCciq8Q-PUbPFftYYWkn30eAcMqxXaNd4kbjykNgNqPOjIjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZWhxtbRGpDgfqQR-bHCrrPJsQ_Zqtnh22pwcWjaVGGlhq1cRFhWHECJj4YM7GHQ26MRHNLHcYf7JYCgVclXrObX7znp0ctxU5XnQ6NHj3xeRh674efIWU847KklUYC2n_JXlTnwcbXG3-ugFAMKjPizvTIC6KCSTQGSfuVSdfOq4ty5aRQTqo_A4WC3UyCTJUZJEBjxv0M2wvsU7v_cIqxY0C5PAFuW4HjYj5O_2m8q3WErP2YB4tnkNY_2hqUV6qUWcnuuIfQdcwVq-slDL8onP-7KR2jZDGXF9DmkWRcfyAuDjj25XTB6prSuvCUO1eLoS69Iov5gbKpj69yFJ3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند خاطره به‌یادماندنی از رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/667426" target="_blank">📅 14:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667425">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b516a0f9c.mp4?token=CMpNWn67OHQBa_v5hKnn77v1mq8rbadabhXKcgQj2yT6SCZZVCv5JKW2dU3wAZT6F-dsXbKhR3FOZn0GoxSiFs0vQJYE1ng0kLGdgOEbXo8apMFGuPgRxm-YnemekCX-3Ev6FiatdJYk-WBvt7dLg3TveWH3cad6TXoTpvJ-MhqdyBMeHU_bXMtZ5hp1uUkEVMU3swmJqMkvr5_DXNXPcCCVFkLn02-73U2bKqyhJsZKlt6JOvcl_HO3J6OH1MVqIbev0IaI9VfalPM9SIJrbUNMLf2n1BubLkKNNg7o5j_vjbRaWdhAWR98fvaOFqnqe2dLx_B_zLf3bZ4eOr1eRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b516a0f9c.mp4?token=CMpNWn67OHQBa_v5hKnn77v1mq8rbadabhXKcgQj2yT6SCZZVCv5JKW2dU3wAZT6F-dsXbKhR3FOZn0GoxSiFs0vQJYE1ng0kLGdgOEbXo8apMFGuPgRxm-YnemekCX-3Ev6FiatdJYk-WBvt7dLg3TveWH3cad6TXoTpvJ-MhqdyBMeHU_bXMtZ5hp1uUkEVMU3swmJqMkvr5_DXNXPcCCVFkLn02-73U2bKqyhJsZKlt6JOvcl_HO3J6OH1MVqIbev0IaI9VfalPM9SIJrbUNMLf2n1BubLkKNNg7o5j_vjbRaWdhAWR98fvaOFqnqe2dLx_B_zLf3bZ4eOr1eRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زائر کاشانی مراسم وداع و تشییع رهبر شهید: دوست دارم به همراه خانواده‌ام شهید شویم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/667425" target="_blank">📅 14:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667424">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
حماس کمیته اداره امور دولتی غزه را منحل کرد
🔹
دفتر اطلاع‌رسانی دولت حماس در نوار غزه امروز از انحلال کمیته اداره غزه خبر داد تا اداره امور را به یک کمیته تکنوکرات منتقل کند.
🔹
دولت حماس با اشاره به اینکه اقدام مذکور در راستای بهبود وضعیت داخلی و در راستای منافع عالی فلسطین است، تصریح کرد، هدف از این کار، کاهش مشکلات ساکنان غزه و گرفتن بهانه از دست رژیم صهیونیستی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/667424" target="_blank">📅 14:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667423">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f86ba91fc.mp4?token=nbuAZU9om0nUvEAD3-tetwxKIwKl6Nb6jPiUJCK9FcwuhA9QG5SAUjeftmdUXPBgMFRA6JO0bihso7qB_-fu8cLHpA-R-exS7tZrpakyJp7H4qudEBeu6xfA_b1bmsVTKrPJy-YRzoHqqqVIj5Y4ul8fN7JjetIWu8ZlrIHGO_4AbxHK-MOkYu8qgIGxeQr1JzPjrLiLpqEXsp9TRM7Spm8aJhtqAgeLWXxwwPuGAsNyXCUyiATV2S-HObqqL0MT_Tu_rB8a6XZUsQSVb30T1K_NGapzKtwGwrMadsCSDyUMKUw2NUvF-5NFcxvvm0j0z4spi3Q_ANcmulUjiR149jWopJKKSK4QciM266LJTZK5XSz8PyVnPfDsKq9xgbMOXg3HudUnpcJb4gwddgdmoi470eZNRg2ugSQDg3AbTuG1CGYiTYGdJZDroZ4_RN6Asv60OAEJAaQ4qx3huBOM6-Mw3ZTda-cELAs8PiYo7tKJYXApoBTHr8y9oqlTsEu_4nsSQT-lURzucGbpB6IO5C8gVJSwv1CyMMyta2iH-_YzmcpVxLsUG18bTDnanLjmkus0D_sjPE8TIqjK_f5W-ePoGYf6c1M0fSo312N6D7WAFhav3mJAr8TUCxyXALQVXPf9UV_mEFYOIh0ch5l3GmX_x65KmqPiH75N9xp-sYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f86ba91fc.mp4?token=nbuAZU9om0nUvEAD3-tetwxKIwKl6Nb6jPiUJCK9FcwuhA9QG5SAUjeftmdUXPBgMFRA6JO0bihso7qB_-fu8cLHpA-R-exS7tZrpakyJp7H4qudEBeu6xfA_b1bmsVTKrPJy-YRzoHqqqVIj5Y4ul8fN7JjetIWu8ZlrIHGO_4AbxHK-MOkYu8qgIGxeQr1JzPjrLiLpqEXsp9TRM7Spm8aJhtqAgeLWXxwwPuGAsNyXCUyiATV2S-HObqqL0MT_Tu_rB8a6XZUsQSVb30T1K_NGapzKtwGwrMadsCSDyUMKUw2NUvF-5NFcxvvm0j0z4spi3Q_ANcmulUjiR149jWopJKKSK4QciM266LJTZK5XSz8PyVnPfDsKq9xgbMOXg3HudUnpcJb4gwddgdmoi470eZNRg2ugSQDg3AbTuG1CGYiTYGdJZDroZ4_RN6Asv60OAEJAaQ4qx3huBOM6-Mw3ZTda-cELAs8PiYo7tKJYXApoBTHr8y9oqlTsEu_4nsSQT-lURzucGbpB6IO5C8gVJSwv1CyMMyta2iH-_YzmcpVxLsUG18bTDnanLjmkus0D_sjPE8TIqjK_f5W-ePoGYf6c1M0fSo312N6D7WAFhav3mJAr8TUCxyXALQVXPf9UV_mEFYOIh0ch5l3GmX_x65KmqPiH75N9xp-sYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برزیل از جام ‌جهانی حذف شد؛ نروژ با درخشش هالند به یک‌چهارم نهایی صعود کرد
🇧🇷
1️⃣
🏆
2️⃣
🇳🇴
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667423" target="_blank">📅 13:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667422">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
اقتصاد ایران برای چهاردهمین ماه در رکود ماند
🔹
جدیدترین گزارش شاخص مدیران خرید (شامخ) از تداوم رکود در اقتصاد ایران حکایت دارد.
🔹
شامخ کل اقتصاد در اردیبهشت ۱۴۰۵ به ۴۲.۳ و شامخ بخش صنعت به ۴۵.۳ رسید.
🔹
اعدادی که برای چهاردهمین ماه متوالی، ماندگاری اقتصاد در محدوده رکود را تأیید می‌کنند.
🔹
شدت رکود نسبت به ماه‌های قبل اندکی کاهش یافته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667422" target="_blank">📅 13:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667421">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBQAw4LTYMdfbN3cb7eiwqaZnVpWgFqPlKLYBvfaZPtC8kIa-kLtc3-HyYL54vvjmyz6afknn3rsiXH4WnwxmAQEpV6160XZGChSwZLYGyYzcM-R7XfIsYc5XLrfkOXZsUfkDRGe-r5bOUWhMcmvaP7BUVI77fl02QVqiTghRtyD00D4X_JqaM_dp96XX-px9pEp3a1zTTGkrQMmnaeOQR2HimyuACzB5kw9ugX_sD9-696iNUsg486d-IIjTD0OH6zreSCKirv8o6k9za_EpwOIUhf7Z_Mhlddi7MIZe0rEjTm9ZmKm87ORAoYDdmPH1XVgCvew9SvSM70LICe5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنگ آقای گلی در جام جهانی
🔹
مسی، هالند و امباپه با ۷ گل زده رقابت سختی برای کسب عنوان آقای کلی جام جهانی ۲۰۲۶ دارند
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/667421" target="_blank">📅 13:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667420">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سردار حسن‌زاده: طی ساعات آینده خودرو حامل پیکرهای مطهر از میدان آزادی بزرگراه شهید لشگری را طی می‌کند امیدواریم طی چند ساعت آینده به نقطه پایانی تشییع برسیم #بدرقه_یار
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667420" target="_blank">📅 13:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667416">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HnibOjOOfU02wpdNr9JCdLX1TvqKgPFGhDnZ4a5xk1V2xRSltdeJ-TzHKJ-Xuh3NhEEiuHWXfUi3N145A6EEby2zNGmXugnFhshDCRlLm20GNVyxYcIfPXmSfkX7xPGhiS0jdDhCVboazCPifWe8nIEmYCu87BuIlUyryNg3BLx9qr2jVVpJgxIYOzMIP68hAPB_ByRJeY0byMEdVdfZEQgifv2cNokN65Zw1_ERbBZnAEupH9abQj3qwI0PDcUyXbzz2PKpRmgy-JInsy-GJoVy1PqsNKNYw768vA5y-T1o53_0svfHCapwiLW0crytU0C-E7SyjMaOJldkapYJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cCEQOqhFPb0hnqgoquMEsWsFri96hMoM7N7K3VnD4sbdWelBDuEKVEU3ALdat05hNs0z8Sl5nI0S3IlMLULouEBw5QJVF5tuHf5cNboWSueTw1EdJajeKEmh0ua-euLefkf_6G8syngqXUXgROql7i9M2A7MRYOnwsqlkxGpHuelVSkcZfcXv28JS2PyOpIs9vsMz01U5b-YZ8XOacnphFvJ4CYr9h-YeC48HOPaydJBLCZTSUB4Na2NrZ1703SZDVmFyr0iAi8opb9ZIK_pv-HDcWrWOFPbnwYv4V1s76eZ0pgZeoj3omkE9_xAacUcgsft2ttNpJ2czyKGRRhGtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuMP2cJuqOoT_aTW_x_U7EBvfjfeUIb93ocOvavpyjIJyoXlkpAW5BaSLWOj87ybY5IzySClV1G0T_j9_KxFiHttL2PkJFbaPeAY_brV1xyLxnerQWnTe9NMYudP0N8u9e7Gd19FBC1vAXtriHN-K3zysvSZb-PqEQ7ybGF1n8lm76Nn96Vv4MwcIkUR0NCbrya8kYGwzuMUj2PzxxHLMZbVVALxY55U5IPVq7LqqurgVtd_94DG5CIZcJkav0Lu12SPu4bC0x_y4WHryIFAg-aXMMN0hE2oJ0I4jEHkft7BaDJJEh1PKlDeFMejxHeFRvsVGklB5Lo-Y6U09uaZlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DshX6D96_DSifmRbZT4LbFdb1J7WlvtV0Pa8VTvQBfw-CgwZ4Ibol8_Ql7ExY8Vyn0PgVdHZiEiQA3Qa4oBX2JIDP3eduPM2bWCOuHrhjR9B4zw2yR2KQPxa-Vov1kAOcKDkEHaK-1IMwrA_jxarjQk9tMO4fPNJYTOhVMGdwCmb15yvq2w7hmBpkElS1pWp3-HRoL_gYH5IerI0ltQq9mK4xvEuymAs6h4sNXXuUTHD69KAnFCWZHESRYPOxleqoTo_vgIgMGJ9pb_FKUgEFlr6tjPgvTUqYu5oFMn2lT86D4W1Ayt3GDpy8AuSDZH5rs7K10xJouGk64IxPqk5Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور عراقچی، جلیلی، وزیر کار و رئیس سازمان انرژی اتمی
در مراسم تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/667416" target="_blank">📅 13:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667415">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
سردار حسن‌زاده: طی ساعات آینده خودرو حامل پیکرهای مطهر از میدان آزادی بزرگراه شهید لشگری را طی می‌کند امیدواریم طی چند ساعت آینده به نقطه پایانی تشییع برسیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667415" target="_blank">📅 13:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667414">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0hSvuCgWELxoTU11v5fqtVnOzvXk1k7iWm93WwduoNik8Lmkz6TW0q8LcHeLFniPFyOFiJ2RJZ48deNZfcYsCoyFzZDmZZFjBHCx7lYhlNJ7PuT-JEfhPHXzSPfE9hBNVNqcTB5s2fG_rgRlKKj0zqQVnLN_pEwwiKnE8eXryYg_dE7RqAtd_vJRcKs_mHw81r0BbnRxHdsJslb2ReFE0AhgUTmlOTpqCxHihvCrEGuBOeXXOZQ6-QuHDgmPPF79sNpSf8WY9jTYB9YhYplcs1jA7eOggGSg1UE9LTVZWeaFjyznUiuHuxpMy7dK-4OkedRP9I8nCb_sP0LIVWtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمله جنگنده‌های اسرائیلی به النبطیه در جنوب لبنان/۳ شهید در حمله اسرائیل به جنوب لبنان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667414" target="_blank">📅 13:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667413">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da0d86991d.mp4?token=vj69X9jtan4ium-xwp9wXagxn-za9C3-vbVC7YWMghXa0ZYOSAi0jUyoQuLieO1l8y3gQJ6kc2EHfPeEAQV2bX-vjA4NzNlIbX2Mnphu8UYIYF4XQxQTbGUmDYrMdRyHC7AkmdEgUWp_8D6MB-ERAfBh3lOtEoeULlkZS-yQob4ST9zocSy__-or_LGYUCdz4CoxaaSqdtlKQ7fMGp1rxD4NcpVpe9YkMmQbAbuStKr3lLYBSW712ZtTc2FHuLPZDac2mqk7LNyYl-h85yZfNpRPcu8yVmvRfbOtS-A0sD2UqWNKNgZRJILYN_pcHWuks6Qg9ogjZv6M2x4aSW2ibA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da0d86991d.mp4?token=vj69X9jtan4ium-xwp9wXagxn-za9C3-vbVC7YWMghXa0ZYOSAi0jUyoQuLieO1l8y3gQJ6kc2EHfPeEAQV2bX-vjA4NzNlIbX2Mnphu8UYIYF4XQxQTbGUmDYrMdRyHC7AkmdEgUWp_8D6MB-ERAfBh3lOtEoeULlkZS-yQob4ST9zocSy__-or_LGYUCdz4CoxaaSqdtlKQ7fMGp1rxD4NcpVpe9YkMmQbAbuStKr3lLYBSW712ZtTc2FHuLPZDac2mqk7LNyYl-h85yZfNpRPcu8yVmvRfbOtS-A0sD2UqWNKNgZRJILYN_pcHWuks6Qg9ogjZv6M2x4aSW2ibA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از حضور گسترده مردم در مراسم تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667413" target="_blank">📅 13:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667412">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a5afdb0.mp4?token=UQufAl43kkQ92Y0Ptxstacuredzm2R8fXoArBSlfhQkRNjT6iKXDHAbpen5zeCg-1ZJ1BTSyTMhyoHtFQeEfAI-ocCSKIbSgoklytRzbZLwRsrDxDanCvDS5E7fMV0yJc1BDLn4qIBBPaCPNCEJXcQOQrp2Wb5W34W25kOR5G_XtrpT8oLL69jJftytyAoOzjAthujD7NCQus9LKHll4VSv8bhbzgVUzSHQdbF7F3W6YxzxwEjvEEfjV2YJZsIbJPf4po7ouEKkuk-idoMqnp6nZ6US1nd1mHbYrwOS8HT6BMPgEhxHIiTcsAYi1iyoxMULHZhzEgnuzUUsp41koqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a5afdb0.mp4?token=UQufAl43kkQ92Y0Ptxstacuredzm2R8fXoArBSlfhQkRNjT6iKXDHAbpen5zeCg-1ZJ1BTSyTMhyoHtFQeEfAI-ocCSKIbSgoklytRzbZLwRsrDxDanCvDS5E7fMV0yJc1BDLn4qIBBPaCPNCEJXcQOQrp2Wb5W34W25kOR5G_XtrpT8oLL69jJftytyAoOzjAthujD7NCQus9LKHll4VSv8bhbzgVUzSHQdbF7F3W6YxzxwEjvEEfjV2YJZsIbJPf4po7ouEKkuk-idoMqnp6nZ6US1nd1mHbYrwOS8HT6BMPgEhxHIiTcsAYi1iyoxMULHZhzEgnuzUUsp41koqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بغض فعال رسانه‌ای یونانی از شور و احساسات مردم ایران در تشییع قائد شهید
سیسی فراکو، فعال رسانه‌ای یونانی:
🔹
خدایا دارم بخشی از تاریخ را زندگی می‌کنم. دارد گریه‌ام می‌گیرد.‌
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667412" target="_blank">📅 13:21 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667411">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a6109851b.mp4?token=M6MpTCQmA4VYkCu1juJ1HL8Z7cmfArGvfxFhF-eGoG24Tr8K4a6B94l0aev7S4ItVYi7vitMrtmyGPDDGUK6o2rIRv2VLcsidkmkef0BfFOArGp5nCtFGVFZmi6p85FjTQ9kEdcmYq4Ht7Wo944WdEB1ikTyHIHZ6QOnhWoiUc07eSf5-O0CmwV2d8fsUw6ptJB50JSFfGhUwl_wmvQQ1--uFhVEw5UykIV8DMWUAMSSSzVV3jFwDUW4yDZfHXes8fcNeuJu8vIS3N217FdHJnyZWKypByu8Hywow_lWwfb93zu4euFfN-7MgNiWSkHQoggUYshuJhh_gn3P_hkVSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a6109851b.mp4?token=M6MpTCQmA4VYkCu1juJ1HL8Z7cmfArGvfxFhF-eGoG24Tr8K4a6B94l0aev7S4ItVYi7vitMrtmyGPDDGUK6o2rIRv2VLcsidkmkef0BfFOArGp5nCtFGVFZmi6p85FjTQ9kEdcmYq4Ht7Wo944WdEB1ikTyHIHZ6QOnhWoiUc07eSf5-O0CmwV2d8fsUw6ptJB50JSFfGhUwl_wmvQQ1--uFhVEw5UykIV8DMWUAMSSSzVV3jFwDUW4yDZfHXes8fcNeuJu8vIS3N217FdHJnyZWKypByu8Hywow_lWwfb93zu4euFfN-7MgNiWSkHQoggUYshuJhh_gn3P_hkVSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانش زمین در شمال هند؛ چندین خودرو زیر آوار مدفون شدند
🔹
بارش شدید باران در نزدیکی منطقه کیشتوار هند، باعث وقوع رانش گسترده زمین شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667411" target="_blank">📅 13:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667410">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7F-M9lutkP9UA8CyLrvkJGYQYNg9MBDrzgTT2yeytTMptLn3FxN4uSZaZYYJQ2o4deoppuxQxfaXoEkvvm958s0CiFm2R6EWB40yEIv_SmT0ypEdS2BvM3AAXp243rk_0h9sA43mo4Xe9f5HKlsj_MKcA4Kj-BXFpH2FEePt0uSAvkpSTOOToGJVj2Fdyk5fIU3o9ggK38MYIV0xTkns6RuMZ-ukJCJ8Q8nNnbzQGMJmeATdSTOwxgMwIieMh27RsVrG3s2qTA1XBsYHLsk9lnPijbahCP4fRioO5b8RxRCsweKeAoSFYgvC_qqtwbY582eUL9qL8k2iX-TEZ3E0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور سردار قاآنی در مراسم وداع با رهبر شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/667410" target="_blank">📅 13:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667409">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
بانک مرکزی: اختلال جدیدی در خدمات بانکی گزارش نشده است
مدیر روابط عمومی بانک مرکزی:
🔹
تاکنون هیچ اختلال جدیدی در شبکه بانکی و بانک‌هایی که پیش‌تر با مشکل مواجه شده بودند، گزارش نشده است.
🔹
سامانه‌های سحاب، پل و پایا به‌صورت عادی فعال هستند./ سیتنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667409" target="_blank">📅 13:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667408">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f852cc803b.mp4?token=YgvBaz8aV2raVESzLhurGLAvEyz00IcgoLf00Jl2GDpmqJs-vg9KNuG9iHmukh6lf-BU6KesE3XzfQT1rtL7H5KPs4wJPPnowmVrxzrnQJSA1GXvTRnPmFAGx04E2cTcjTXeRVQmIjHxHMQbq05TqKmTGggld0JULuZ3HcKb36DekaFUMgLsCCHqHK0bWEpCKmIW3TG0P118vVHSIj6cfZPK1zYLbp3bejnMrNsGN8-0VUa-HS3edoMB-Lj9DSDkeDAP49j_T2KONOeWANrYdlXNxpiKI_m5vtr-qu89pGOQPbOKLy7LKQJomKmuRhQ9VG7F2zV-MV6sCAZjW-e7sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f852cc803b.mp4?token=YgvBaz8aV2raVESzLhurGLAvEyz00IcgoLf00Jl2GDpmqJs-vg9KNuG9iHmukh6lf-BU6KesE3XzfQT1rtL7H5KPs4wJPPnowmVrxzrnQJSA1GXvTRnPmFAGx04E2cTcjTXeRVQmIjHxHMQbq05TqKmTGggld0JULuZ3HcKb36DekaFUMgLsCCHqHK0bWEpCKmIW3TG0P118vVHSIj6cfZPK1zYLbp3bejnMrNsGN8-0VUa-HS3edoMB-Lj9DSDkeDAP49j_T2KONOeWANrYdlXNxpiKI_m5vtr-qu89pGOQPbOKLy7LKQJomKmuRhQ9VG7F2zV-MV6sCAZjW-e7sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه شهید انقلاب #بدرقه_یار   #اخبار_تهران در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667408" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667407">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmC7uHENUOwSBc8cXGuJ2WcVhcNAPXXJpUxhoLn0bKJLNUd5k9CW5_p7bmaDlxltzOaHc28HnP7CMsBldV1lIJzn8VBwwR0Vf558LZ5HMpsH23TO5tnLyvBh9pSRF1DC6K2Tl5aAEv9dELysF2bQma9AHFd5WkqIAQfUOKokP7y_spCiGIrLC4NYgVSTGYsDejCUHUfRB1JPON7v48FASvWbevuohvs3nGPPevN4scFJO6IKqQ4Raq6TQDx-hxwZQLoE8Cs7qNv8dTFf3-hXjR6hzJ88mlZ9gdXUOASqHAlo_IA4NG9gXN17vkguHdZ561uyeRCkzPFD9mnVEjS1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گروه‌های بحرینی بار دیگر وفاداری خود را به رهبر شهید انقلاب اعلام کردند
🔹
گروه‌های بحرینی با حضور در مراسم تشییع رهبر شهید انقلاب اسلامی ایران و نیز با برگزاری مراسم تشییع نمادین در بحرین، بار دیگر بر وفاداری خود به امام شهید تاکید کردند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667407" target="_blank">📅 13:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667406">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
تمام ایستگاه‌های مترو تهران فعال شد
مترو تهران:
🔹
به‌ اطلاع شهروندان و مسافران گرامی می‌رساند، تمامی ایستگاه‌های مترو تهران و حومه در حال حاضر فعال و پذیرای مسافران هستند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667406" target="_blank">📅 12:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667405">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
جروزالم پست: اسرائیل در جنگ با ایران به امارات گنبد آهنین داد
ادعای جروزالم پست:
🔹
اسرائیل در طول جنگ با ایران، سربازان ارتش و سامانه گنبد آهنین را به ابوظبی اعزام کرد.
🔹
این موضوع توسط "میری رگو" وزیر حمل و نقل اسرائیل تایید شد.
🔹
مقامات متعدد اسرائیلی اعلام کردند که تصمیم برای اعزام گنبد آهنین و موشک‌های رهگیر به امارات، پس از تماس تلفنی "بنیامین نتانیاهو" با "محمد بن زاید آل نهیان" گرفته شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667405" target="_blank">📅 12:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667404">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4baae5a.mp4?token=PqMxOELwdy-veI8QBwcj2qgdojl8xDKqCiSvat8daAGOU9VA67d9JDFp4koWj0sALNvty46X0pEePI4G98cDLIzSF8TJojbdDAXzDg2tbDmDC8UH5dHHpsk4Gfr4NFgY-XJPb7VO6uxmm5FPjXnUKi-KPkVM6rxDxQObJ2uONcYNqa9Zc4UNQ2kBi4WrASOkDWSI-RyPj2RPR1En-zHi2ayd5B4YzwR3HqRHkK8YGUrpX1W9yDisbK0k1_QDzzfoQJweeuXOlahx_dmA1yYlBqv6nWCDYALcEb7IzCOX4pjpgfIbOlfeyCfXnZmZ2KA3smuZO5clU-L0eqvfNbxgoggsx12xiS2cDqCK2OkPpJnbnt4y6ZDQntAEtH7oVIrd7O_dDfiOzOajzQ6COyBx7G3gT7Ne0Dg2Vjte6FmAuGCJbhgAQS0-euR91DQFy7911JkBFh89P4UXIGpug5Ij7cI2D0GULz-1hqoKcpWJqfs9jtwGsd0viHIs_-bnxrTM5Z2Nzo6jrR3xfaAUtrCAX7fr0Uod_OEESgT70IQWNtudBFvhZfws0tgglDF0-Irtzht9BHVlDGerULOGI2FwxK-UGWxu5z8ezdaOhR4EhcQwWyAlPEX8y56-bUKCpkHt2Kfl8doXq8Uq08u6Uk7EQ56YMVgyS7RZEwPgvL36qhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4baae5a.mp4?token=PqMxOELwdy-veI8QBwcj2qgdojl8xDKqCiSvat8daAGOU9VA67d9JDFp4koWj0sALNvty46X0pEePI4G98cDLIzSF8TJojbdDAXzDg2tbDmDC8UH5dHHpsk4Gfr4NFgY-XJPb7VO6uxmm5FPjXnUKi-KPkVM6rxDxQObJ2uONcYNqa9Zc4UNQ2kBi4WrASOkDWSI-RyPj2RPR1En-zHi2ayd5B4YzwR3HqRHkK8YGUrpX1W9yDisbK0k1_QDzzfoQJweeuXOlahx_dmA1yYlBqv6nWCDYALcEb7IzCOX4pjpgfIbOlfeyCfXnZmZ2KA3smuZO5clU-L0eqvfNbxgoggsx12xiS2cDqCK2OkPpJnbnt4y6ZDQntAEtH7oVIrd7O_dDfiOzOajzQ6COyBx7G3gT7Ne0Dg2Vjte6FmAuGCJbhgAQS0-euR91DQFy7911JkBFh89P4UXIGpug5Ij7cI2D0GULz-1hqoKcpWJqfs9jtwGsd0viHIs_-bnxrTM5Z2Nzo6jrR3xfaAUtrCAX7fr0Uod_OEESgT70IQWNtudBFvhZfws0tgglDF0-Irtzht9BHVlDGerULOGI2FwxK-UGWxu5z8ezdaOhR4EhcQwWyAlPEX8y56-bUKCpkHt2Kfl8doXq8Uq08u6Uk7EQ56YMVgyS7RZEwPgvL36qhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
وداع یک میزبان دیگر با جام، صعود سه‌شیرها با کمک بلینگهام و کین
🏴
3️⃣
🏆
2️⃣
🇲🇽
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667404" target="_blank">📅 12:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667402">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ntArcXCEe6A6CwjYB4OWPGI4cLuhAFDDzyOEmULduw_sL6md3kof87phSrnYDk9rGQ7us-f2p59xJAsnUCbuqCQmvBTKSMIVXiS8SSLI_ay9FJYLB6QCn9cNNEpiYaiOfzPBPji_vUo6zVJnus13hfPjh5DJdCLh5C45ZEi3WbeukQ7T3026hwixC6EaVIkhHrnQ-Wy2iYoZIVqL-4xnOw2AQXlnfwRo5XlViIRxC412rkGlJHQTp244ZhTUiZVa0_BwqFuBoh21XPim_OonPBOmG6T1_U4T1ijEYMhdqJe-y50qgWWWrpKBl6TK8sHONQy4ga5cgo5R-cuWw4IFgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XYhWvtI-4Iv6spr1H_weggWIMgw66ZcJkSGGSCdr4dfywol42ga0P15N3dNEw3ht3dVnQl9P-7L0BISsI8oPHy4OVLDdRqykOXCLrrQY9rhCGB2sGcVFMcCYqpFNHY2iCXMuvvokmQe_imFoCTV3CQF27SJRPt2wzgE0kQDBX5dQHdngTXg8Swg2u5F5DpJUgQqAsDnxfwczvlmj5IQcPiYyEuLzc9wr8Q9tyEEOzZlqUlpT2i4Q_sgsO65GzqcMYKGgLcETZj9D0ErLO_msCnGsuFYlvndZczB7tkQ2n0wJwgjWWqfqjt1Qx7tIKGz1PXsrSp0lGhMyLtUI-FLArw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
حضور رییس کل بانک مرکزی در آیین تشییع رهبر شهید
🔹
عبدالناصر همتی، رئیس کل بانک مرکزی ایران، امروز همراه با مردم داغدار کشور در آیین تشییع رهبر شهید انقلاب حاضر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667402" target="_blank">📅 12:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667401">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
ظرفیت قطارهای تهران- قم و برعکس ۲ برابر شد
راه‌آهن جمهوری اسلامی ایران:
🔹
با توجه به افزایش تقاضای سفر برای حضور در مراسم تشییع پیکر رهبر شهید در شهر مقدس قم، ظرفیت قطارهای حومه‌ای در مسیر تهران- قم و برعکس در روز دوشنبه و سه‌شنبه (۱۶ تیرماه) دو برابر شده است.
#بدرقه_یار
#اخبار_قم
در فضای مجازی
👇
@akhbareghom</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667401" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667400">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
پزشکیان، قالیباف و فرزند رهبر شهید انقلاب فردا در مراسم تشییع عراق شرکت می
‌
کنند
🔹
پیکر رهبر شهید فردا به همراه رئیس جمهور و رئیس مجلس و فرزند بزرگ ایشان وارد نجف خواهد شد/ مهر
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667400" target="_blank">📅 12:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667399">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f4d7ac8a7.mp4?token=f6D5rDERfb6hso1KM92uzqBrNc3aV7WNdGqZatqWgpbMZpjIpiu-sU5rEbFIpp61QRFvG-eshzhseddsOeV73NUz4_rnxTMS9YXMVy7s3TSv5rsdbPzDj_y8zwmX2gY6G70w3mlzuj7jALvTKXZpyYO7vveE-TE1NG1TckZn1p9UK6ljhR6qxyt9M8X4NGHwadJn5I9Ysb2VdEpwaaGyTIkUQmd5Sp2cCmotxvPCSodciLNn2BN6ZMNaB0OmxYlax4j8WEIAcki8XMxym_3QFuL6fZRLKCi0Wvx-jeHNq1Q16I66rZA30QnWktAEwoWB3bvfpwn1bdVeOK1ywVlsbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f4d7ac8a7.mp4?token=f6D5rDERfb6hso1KM92uzqBrNc3aV7WNdGqZatqWgpbMZpjIpiu-sU5rEbFIpp61QRFvG-eshzhseddsOeV73NUz4_rnxTMS9YXMVy7s3TSv5rsdbPzDj_y8zwmX2gY6G70w3mlzuj7jALvTKXZpyYO7vveE-TE1NG1TckZn1p9UK6ljhR6qxyt9M8X4NGHwadJn5I9Ysb2VdEpwaaGyTIkUQmd5Sp2cCmotxvPCSodciLNn2BN6ZMNaB0OmxYlax4j8WEIAcki8XMxym_3QFuL6fZRLKCi0Wvx-jeHNq1Q16I66rZA30QnWktAEwoWB3bvfpwn1bdVeOK1ywVlsbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اینجا نگاه‌ها فریاد می‌زنند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667399" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667398">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqMoroUkbxDojMT6j43lS-nxr6NQ_qLLhvuI-a5cqyBsPmcNQQ_oLy_AF2iM_QYjk_kgB4yRvpF6eeudQbc95XA5_vKOXGYO3Y12YvaDZ0OZB6uizC45YoTxhN982u_E35hWVStNTbCfQwRD-bs2t3w6KhKvMDz3VTvRZBepioPhaE4xKdGPy9WO2y9XopTzPU9xLPW6cx25dUBpt2FaHbcqDZNf04qAmNaP2kFuOwMn-169mSJVR6r9j2hs9fNEXv_4otoNaAGFbz0zepZFz0UBjy3aP_LJuYUsto7owU4jTfheWe-L_IR_kCipV1AzT7NIKTi7fwN2NGhb_CQ-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دندان‌ها سرنخ می‌دهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667398" target="_blank">📅 12:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667397">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meo8OBEFrJodp8qU4ED_qANs364IcMc2F_mxTOUeykUK7vighNEm5JWypXNxh8FXwpX6NgfPMzgnCVNgkezwciYKtM0PmvgnjsB9McoGuKFCzBxcC9MzUOGCImnujykO6XRST4OXDl30SgX1XaaAcp66hIsj-ZkE-V4Gfol62PxQZgW1s5GEy-6aI0yJio0L7tire_eWrmir5q0nIj1F73ww-tz-KFB8qi2pB7skfJ6WxTaksJH9f_dGDWA3m4vJBxzPnW0Bg4NNvF-ir_AlNFzrU36sPAo-2q_vgezfO4Ty6IK1Np7jR5MS6_B44cKiLS6Qx433CwRW8_LSoJDnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/667397" target="_blank">📅 12:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667395">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/911ee91e07.mp4?token=G6jBQ1sLlBVfRv_PVnJ0LcdZBEyUB4ikrkRtED6tAiz-Gl8SWPyxQ295Esrkh1JGer6DvajM-11Kk0SPKV1vD2smw4onvOa7OpFxzeSUhrn_9AUawjJn8tFH-pIuZkg2BgI2tyOzKgk9dyghhHpjWnPzOHmN7XOPIMy1i60aR5Bk9SpFf-WtoOur-IzqjM0ZYxYE4Z9MBNGVYM51_X6KaFujauX1_5_QqZ6lYnQH8JWLpjJZEcKd_YveHKtcpX4YB-O7gDfCJ34A8o1pezxpVptlVsMACmfwFnaDWbeveihzzJOD1laju6RvJ3i6pu8DyjKm75yzQpKmrdSKo3qwJXYmCfXdIaCC46cxEZvPeMl-1OaM0VQMMyC_YAmStorRgSY-lpQnOTuPCl1E0lIs_i7Aas1DG977lEHdK_SRBDF5EaOBj-2O_vq8qAG0568uN8vA0GZVuwJ6hoePI8f5orWXt4KMdRZQ53AUXRusZEjSEyvbStxuxEwLeXHL1E5hFcPro42LWb_9h1A9K2eCqL-PIWovb3670n82uiLWrJgQi35FW27nddF0XBLt4Fn4Y9yL30NQVrghQ5CWAvv7ohzwmUHSVl4qmJ6mn0xjAFNqb_lMnf7WyXMHhUlQn69Qbr4eY_sBEnFCtALg8AszWU2eZNS1lrNxu1Z-jeNSVzM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/911ee91e07.mp4?token=G6jBQ1sLlBVfRv_PVnJ0LcdZBEyUB4ikrkRtED6tAiz-Gl8SWPyxQ295Esrkh1JGer6DvajM-11Kk0SPKV1vD2smw4onvOa7OpFxzeSUhrn_9AUawjJn8tFH-pIuZkg2BgI2tyOzKgk9dyghhHpjWnPzOHmN7XOPIMy1i60aR5Bk9SpFf-WtoOur-IzqjM0ZYxYE4Z9MBNGVYM51_X6KaFujauX1_5_QqZ6lYnQH8JWLpjJZEcKd_YveHKtcpX4YB-O7gDfCJ34A8o1pezxpVptlVsMACmfwFnaDWbeveihzzJOD1laju6RvJ3i6pu8DyjKm75yzQpKmrdSKo3qwJXYmCfXdIaCC46cxEZvPeMl-1OaM0VQMMyC_YAmStorRgSY-lpQnOTuPCl1E0lIs_i7Aas1DG977lEHdK_SRBDF5EaOBj-2O_vq8qAG0568uN8vA0GZVuwJ6hoePI8f5orWXt4KMdRZQ53AUXRusZEjSEyvbStxuxEwLeXHL1E5hFcPro42LWb_9h1A9K2eCqL-PIWovb3670n82uiLWrJgQi35FW27nddF0XBLt4Fn4Y9yL30NQVrghQ5CWAvv7ohzwmUHSVl4qmJ6mn0xjAFNqb_lMnf7WyXMHhUlQn69Qbr4eY_sBEnFCtALg8AszWU2eZNS1lrNxu1Z-jeNSVzM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لا اله الا اللّه
؛
هم‌زمان با اذان ظهر، پیکر آقای شهید ایران به میدان آزادی رسید
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667395" target="_blank">📅 12:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667394">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b20b319fcc.mp4?token=HvNCB6Uecl9urpcohvLbEWpYr5g4LpSdK_kIJwj5o1kJroLAlw3ry6thiOlmBdvfQNKPolK4lx93Ex8YnnAMN6N1K4oc0mNp2_jzU7-ctVGM3Z4dGOLrL5BpQyJMT0AbLOvmKB2g3cKSQEvdOwfFwf1-s4lWT0YiUykC_wvxuK-YDTKMkmkfBLqiOVWU5KB1BKlOqRTLYmSdeTMwcUiSyOKq6auxuEF_IpegOKHFde1Sy-6tguIemQMpRD_w4mkFNQTZ-DdxXIyKCeFQrI-Ur99-GkP9MhyhuRlbPo-6y1JFf_98Lsi8ca8eYmT_PCJfZwdlhMk_0neX8l2FRBr1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b20b319fcc.mp4?token=HvNCB6Uecl9urpcohvLbEWpYr5g4LpSdK_kIJwj5o1kJroLAlw3ry6thiOlmBdvfQNKPolK4lx93Ex8YnnAMN6N1K4oc0mNp2_jzU7-ctVGM3Z4dGOLrL5BpQyJMT0AbLOvmKB2g3cKSQEvdOwfFwf1-s4lWT0YiUykC_wvxuK-YDTKMkmkfBLqiOVWU5KB1BKlOqRTLYmSdeTMwcUiSyOKq6auxuEF_IpegOKHFde1Sy-6tguIemQMpRD_w4mkFNQTZ-DdxXIyKCeFQrI-Ur99-GkP9MhyhuRlbPo-6y1JFf_98Lsi8ca8eYmT_PCJfZwdlhMk_0neX8l2FRBr1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جمعیت انبوه عاشقان رهبر شهید در میدان انقلاب تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667394" target="_blank">📅 12:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(El Nv)</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ujsvGyiaSTabesVhhnlsReNBZ9hJIimyLpqKMg4ogiZcoYmmUfnGXTrB-bfJOTloWOG6mylxGUfnJUDReI8VPr7tNO1ISeXDV9xYW4mexjCykNtkAlgkVtht9ZxjyKwif98UVsWwA9-kZKg2KJ8KTlFEIQs22_9ZAQTISm6tm2-CqKg5KfcrS-BoDHlAkeirE79ANZJL74QkaZQ8Ru4YG1ReU36Y2WWKUY1RosWmkYrSxlFtQm1hufKZ1AhUM_-3GMu2KuK9I7RIHBgY6aD8ooG93o4tR5Meax_KMLhRVVqUe2Aq85Nabm8kl60n_O3DI4fxFeouSG9__g1AhABNnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EzL-yRYj7wYKco8aBVE0IRb206gl3WGKzUv9HyZbJp4ctrKXZzk7tdx0Zab9GxX9Wclnl_sC-je4hF_Pu0WqEanOkAP-diUr7fVgL9Whi23QEx563IWkn69n6zvAoIoAIC9Cp8rVVd2OM3V_WLfjvB7C9xP_3P5S6kfnfoLqBV4CNU-zNcPiRVWY8iNZhf94Fd5twVO-gYMCS5q7Zf03-QZma9WDX4I5ghlc2P_MaLoN0s9G9tZ2KPUd7PV6OVc2FuJSHtTIvwV8bwB0X8SWVPatuRx9nY7SJfDd-LoeBOUQ2MbhNYshs8nQfRbLoHjl7MipVv-Uwf_3ottfBj4nsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/moWdSE_lO5FzTCw3Ud0ZjjQjAeV3L4lfcE64nAi6lSPs4rcFOp5NxBHhOmADSTZdcoJ9H90HYKETn_4YYcMKsG2S55yp3QF_ARAXapMf-hW1zCpEzTkFWDQZCcSnLfc2Qu9NU4gMcESElMbXETmWOH2FUoU2-IIK7YwE5SHpc959KBNLT3bIbPKtqz2Yo5AuOVUlzIHz769mOG8tR_kdW2oWmuQe-Mq5cM9Lg0HK2CFVlFl1galA9F_Wc64Q9-UV1TUqqwjB-PkKbe3idTvqhX3qCLmBi_cfHfwxW1r7nw388voZuscOsErZL3cfH_dYDFw8eGzqZ2SsJixL1-gSag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f5Uad0T1fSD9fPbWjeBShQc2z5IvL2YTKGmB6PkgIzEpZhC8qvjGCkJx1hgzN08XN1WlVyb5YyPIRRZy6W-g6kWt8nzLJtpsuwdDg95Y5ATKqneK2nOTKylVGC0McTGxYosmTeUQ0EF228LCjS7rV-0BP4YuNI67zhRW6qmDcWqya3A3u9DIId9OtgSpSdTYn51UhldX0_kOIGqMXBRVhiUTo96PmMHZJ2QJyInrxEcvCwkoX0YRSW9qC6OmqiHQWxBe6j9aj6aaRfNm73vB_LvlMfhk9JPS5nyWf4xNyZpaCNwSIWFuffhHd3M7DMtVWnxnAjQ_Wq1M1cVKIsP9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NhEVzb8kcTYFu50ifrdlez3xkrHUuLZ6KJ03WpaKlyO6EfDIn-F4ywvY3v589jIDJ07FzGXCnvKhXS3aJLJC5hhpUGU6cTkoK4A2l09X3mRtVrVA53tA4lOC2IZZLlMbOI0nvhqdcurR8GWZaB8L1Oxr8a9isSuQfC2Oos1QRSdLegsDJRA8toNOARPlk22ciFbr3GL10lfWPtaBev1J-ZXOiPHn6KJ2CDMQgFKFPxkLz3UndsLCCLnwze995pwtQH7AuDtZb9mEcOg57n62HVcQDmdaGRF6Zz1lTwwYABLgkwIer_-rsy1tph2qYi2ovJqgpCG4_xpHeZ05tjnfeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QowQ4ZPF0Lrq4NoIXbAB7xQMfvdUbu4AyiR_bO5xpfleW9gudnabga5ch29xwVE3UMYpXH9S5fLGLk6n4oI7_1oSo0p2AkN4z0p2kjnDEh2MkYbBSuiziB3J9MjBuWy6nYOe_9uP2daY7JIiJ86vQMmRNh7rn9bPmxeD06jIeiZHyJbMlHiZ2hP454KP4uLfiHnbrqBBE9tLAVtJvAz1FIRfUz6ioLRHAnrKCYHjPkz3QW7qmA25jGRmV9ChvXj7uyk4xEBykZi1etkMrwAOISgcy-XW-JwLJONjEnVzVTf__B6AUrA_3NO0F5J40ducgu34Y-wGwOlaFnNJ39-UAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JUm_nBlhXVSo9l6lXZ3vLAN7nAOX1ssLluMXeaXRdw9n3nxCEhJ3wQ4wC63W7SRxLb9ek_n7R5IgrqnKem9UG1PtKf2nm5BXhmcUkpbuRyO_drGWQiKVGFmGSnICyCizEZ7nLu9Fwq_hk_Vl5Qj1uilfBhYgPea04ZGKoAvs9Sx3xGmwGkaKXJ_E2WEKhUJKOj3rV-ZCHy5OSjgJIuWFtoxpa1ezLebRg6JnheYKBBE4JVOy0r-GUHGzBJcGpW82ePHOwtM5jCOBuEX_1lKUMu92KjHX04jNScCfLUDEhWVBPyR3bGaxf8WynCgoXqxoyxKZMViY6cOp9g2pKF-oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KnhMERzdn10yL5aKv7dvTGdvsVMTjA7Tv6LQWfTIuQMzi4VD06R4VTH7cjqC4z-kO3ERclEhRJx5yXhnorYHmafIRQhu5AIeWL4jwZN-BlQxUBeOoRuudW3rxlt10eNZcOxNnstJZKYzIBsOE_Yp5nO-IQZR29z1fqFgmgsNHRebIEchoChB-zIfIrSHg24MadfhRatMabGX7xkjaBRCHsGtPapJnRV00ugD61qu2nGXjlNYLrTQPiV2Axw3Gp8pwCi53DeusKwBG15ws3rWaTVGhMKVXFuCOAwW8WP9AgYfCIclk-16EoGJu50UEFALZd7PBCR6k0aB6cN20P244g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EYlUXqxh-3AT4OwFYp9-M9uoZqP6JOxZHOMYGbeT74yf3Sy1z3Z_4vNQegqPoQF1ueJIpMOwi4ccMowMW7J4FeOvpRx6vvOgFevXf9kuvJgx4KzXbwL2EhNA2kVqFll_h0yZa4VnfAMtCK4Y9N_za7bQV-0H1guq6kqodY9i_8crzE0sbyXORwq4ziMqVexSaq4X3GH4b8pGN6PtARE5aOKZENvPH-yAyJkpujaj_FV_O45yiqGGzRRa3_UtpB5lkzmXwqwtlv7UbRgWeyardO1sb6jWKTw7BqF6asxtu1buLRVe_KsYhqngwW9Y0mIoyvXjg-ryw6JzTKzBCjYVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0JEV6z5XcuyzAZeHxESg4s2YtK-hTDJrKD-xAH6cbVIzVFH1rfYk9yzqU_rPQanSTCjicd7KTphC9OykVO-9Yhi7IY8U98rpjXzlp6pFfvUWHm0IC7jE2jB6eo19RTK59Cvk3MTlJZ4swyD4xVKpbV2DqUemh5Rc3F4PbeRoy0Caaemwlz7rEnzq6Oe0heKPH7wool2HPDxVJp90Nh743ONTAG33J451qF8ePA_GOu3RYytWS0z6fFL5rl7kampN44xs06Iayh058Ow2cikIoZ7uU5OFKcA7FWD52KzAwKTCIE5pCtA5kUcTG8ZKJUfVXRHfUvM_bC2HvotYCx6jw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚫️
حضور مدیر عامل محترم بانک شهر در موکب خدمت رسانی بانک در مسیر تشییع پیکر رهبر شهید انقلاب اسلامی</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/667384" target="_blank">📅 12:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b259bde98.mp4?token=rdz4wMb3j4EsKK83GG5EoG6GJtMtPZcFy0TD_pujcf47oe5dI6iXtUZkd0ILWrn1VYd8-G79tarbJEDNm8MoHYQb254uzxa2U73D_rgsBo8z8Yhr0ptlpg9pOlfHPyNbJ71MvZNWkyLf6GvB1CSh4jcbvdrTF8hNWjHFfok249mt-Mv-Ye7Imqoj8v85oy9V2eutwkCQ5PRoU1x5N1-pqLn-RqHMezofEa9uVPk4qC4YoxLQ_boQmElHA0y9V_WvSFxtY7NaBu4VB351W2er-ysg_PcUqcTdzWO2wPvX2HqUYIAx5O3_TtEgjwYFWur8WOAt7YWzR7yY9oTD1CVqzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b259bde98.mp4?token=rdz4wMb3j4EsKK83GG5EoG6GJtMtPZcFy0TD_pujcf47oe5dI6iXtUZkd0ILWrn1VYd8-G79tarbJEDNm8MoHYQb254uzxa2U73D_rgsBo8z8Yhr0ptlpg9pOlfHPyNbJ71MvZNWkyLf6GvB1CSh4jcbvdrTF8hNWjHFfok249mt-Mv-Ye7Imqoj8v85oy9V2eutwkCQ5PRoU1x5N1-pqLn-RqHMezofEa9uVPk4qC4YoxLQ_boQmElHA0y9V_WvSFxtY7NaBu4VB351W2er-ysg_PcUqcTdzWO2wPvX2HqUYIAx5O3_TtEgjwYFWur8WOAt7YWzR7yY9oTD1CVqzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مسعود پزشکیان، رئیس‌جمهور در مراسم تشییع امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/667383" target="_blank">📅 12:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1ccIfmGihQtO-g420aPW3CBcOxu4wbNIoZZAx-MMjrt6AD9Ep365fQrPNkJ_v5vRTwguiox8aCuDzCf6f0Ct9WlkEOTSpDkcgGZS9EvJQTITKAXBXVdwnvVlKvbr9bc6vUGPI-Z_v8F-owPShYHhOSCWxD_ye97LFmvBgE7t7oZuImcMe8T3ufF4NFQpdYTWupehul3MRDl2TR4gS8VwSH_nAxJ_os0DD3hgRX-exwN4ksGuLIWfSRuUWXSidvRROe4KPup1pjHcsCA7jW5NpYpSPfXWRIBzMUrViMN6LHFZEstNBDn3ElggEqMyBYUvTUDKPsTgsZLZa27bOFDsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۶ دوره بازداشت رهبر شهید قبل از انقلاب
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667382" target="_blank">📅 12:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210ffe32cc.mp4?token=IV8IurX8Tr3IPN3x4PDjf9hoisbJQZpW01r21mxX3XWUzesCD0lUA-1cA-Kn-pJZEzVKPudF9YTNL-bPFWPRIBJRedzaJSgDdDpoyg-oPNrmx9xV-QoRNnFPUlMA6i5gXMuprUqjkQXyp749lT-Cezwgd4kL7sK0Lr5LfbxuC2x0uoYPs4bgmM5MNut667wWo7FaHAHsCYMN0bsAJioDegfeWTnPCVU8TMDdPjTuhLUz6AXsH6EL7n8LuITMyEKwlp6AQZrb85EJEec50yq28rAJ7U4cbylPDPbI0GNqZEzJ6fYPlT5q6gspt65_64qYgKh89G_aExYrpr2nB-la2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210ffe32cc.mp4?token=IV8IurX8Tr3IPN3x4PDjf9hoisbJQZpW01r21mxX3XWUzesCD0lUA-1cA-Kn-pJZEzVKPudF9YTNL-bPFWPRIBJRedzaJSgDdDpoyg-oPNrmx9xV-QoRNnFPUlMA6i5gXMuprUqjkQXyp749lT-Cezwgd4kL7sK0Lr5LfbxuC2x0uoYPs4bgmM5MNut667wWo7FaHAHsCYMN0bsAJioDegfeWTnPCVU8TMDdPjTuhLUz6AXsH6EL7n8LuITMyEKwlp6AQZrb85EJEec50yq28rAJ7U4cbylPDPbI0GNqZEzJ6fYPlT5q6gspt65_64qYgKh89G_aExYrpr2nB-la2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش ویدئویی راشاتودی از حضور میلیون‌ها سوگوار در مراسم تشیییع امام شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/667381" target="_blank">📅 12:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
وزیر ارتباطات: رهبر شهید نگاهی فرصت محور نسبت به فضای مجازی داشتند
🔹
نگاه رهبر شهید، استفاده حداکثری از ظرفیت‌های فضای مجازی برای ارائه واقعیت‌های ایران به جهانیان بود
.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667380" target="_blank">📅 12:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AbbEA_bvsMZk4o0DQn9aXuCqxFCauicSE11EgoFe9GhWybidwbZoAihj_7NBnPeaKznntP5RLFZsLDhSzQXAf40lJYUgK97umX7K3OYKtb5FdXqz_uwEFZc--i68whX4DvFsrPN3CFlYe9LkO1x0gM_fVUxaJszKFkBv0HMwSfV6jnfqS0-s5iurc5fBg49fhm3wP83RrUUZo7I7TGyR8NNZymgOh28J5TDUngGpWrcdNis5wufZaV4L96uJxJvhjvFCVkvH0vBXs_KA18vYIQcJ7RiDFzS6nWmtGdk9pXV9cC2DUhSCBlAtsUHkvavJ4R52CEoGpb3PN7Z0-Ah2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای کره‌جنوبی: ایران از ما دعوت کرد اما بعدا دعوتش را پس گرفت!
کره‌تایمز:
🔹
یک مقام وزارت امور خارجه سئول: «ایران در آخرین لحظه اعلام کرد که حضور هیئت دیپلماتیک به دلیل مسائل مربوط به محل برگزاری مراسم دشوار خواهد بود.»
🔹
به نظر می‌رسد ایران تصمیم گرفته که از هیئت‌های دیپلماتیک خارجی در تهران تسلیت نپذیرد، زیرا بر پذیرش هیئت‌های عالی رتبه از سایر کشورها تمرکز دارد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667379" target="_blank">📅 12:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkJ97DM4tqCQTL4vpPgfsMf_2SeqtxhW-J1pkymPidUyaSZEmOXY5MHJJhyW9oCdshmdSjSDtFNyeHVWUQqVetjEND9dIrfcNPbTzmImxV1bZydufzwbRX6xo-J3ZQFmeElQvlnGYHAvR3sV7YUj9BwXskKqKPBxMUY54IrbAcFn5nvkFKyneew8qXWK7f8qTRstpTopM8X8TJERMcql5XTKtEa798Fgrd7-8wMCyG4nErSlthbd6X1COM1hsNl-HlHVtHPSj9OGZie2EAFrPqteIhyD7bUSj_C19onLJzHXMaDvZX6RlQzdjzK_Yzu_eF7Fxgjp6WDdgZxV3oBpCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمای هوایی از خودروی حامل پیکر رهبر شهید انقلاب و شهدای خانواده ایشان در میان جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667378" target="_blank">📅 11:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/add20b1cca.mp4?token=odq5liNTf3TGXl0EctorgCoKvszgiTZ8IExvPaHqOoqiH3RWDMXi2Am-YCC3do6uzlxv3btQzhZafAJIlAXzvKWfXz2nJ5F7TPdaBBiU879QlfKKvPxt-LtyTCUhOrNSIL2szI_ozTmfgUhunGTzYFFP2sBY2DcU03ZZGVy2x-Uf8rmuYhH1C7hN0SYe2Q4Gz9nIYOWXefgoevdHCovbx-0HWlFPTZYkc5WAJNIkyprRI2P7TFSS_IRuiuYsHeV94v2P1_jXrO8DQoB87p6ZXfGeeAKJOPv66dA8Uer--LzCZIIiTzl9DYQHoVKkuZlgss5wkntor5yX5AQpgVAUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/add20b1cca.mp4?token=odq5liNTf3TGXl0EctorgCoKvszgiTZ8IExvPaHqOoqiH3RWDMXi2Am-YCC3do6uzlxv3btQzhZafAJIlAXzvKWfXz2nJ5F7TPdaBBiU879QlfKKvPxt-LtyTCUhOrNSIL2szI_ozTmfgUhunGTzYFFP2sBY2DcU03ZZGVy2x-Uf8rmuYhH1C7hN0SYe2Q4Gz9nIYOWXefgoevdHCovbx-0HWlFPTZYkc5WAJNIkyprRI2P7TFSS_IRuiuYsHeV94v2P1_jXrO8DQoB87p6ZXfGeeAKJOPv66dA8Uer--LzCZIIiTzl9DYQHoVKkuZlgss5wkntor5yX5AQpgVAUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل کم‌سابقه چین را درگیر کرد
🔹
در پی طوفان شدید، آب دریا در شهر «فانگ‌چنگ‌گانگ» چین طغیان کرد و بخش‌های گسترده‌ای از شهر را زیر آب برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667377" target="_blank">📅 11:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB7ceWVU5l9PebpOtwV4i3gJWMa4-F0sP0Y6NTCvbeWO0NUI1wBjodnUlU986nu7H_y4_dg7LKaSUII6b1nMQdx3jwKMc1KYkFEJBhuyurG1h_ehZLthtsT-pYp1OObjxqxxNqquRz6fobbv6imsp9ogeuPxTFYk3bdVaoHtOmiUkdE3QBSSKeohpeZ6VExclgcLbCmXP0rr9ynyfhRvZQZOY8CfvzuRGDdZAa4Jj0QAriFp2sgrLmvb6jTPv418QVWUtHpzmlk7SPWmbjj8rbTcWsIl8uemM-lfj4h_CQ5qJo8LrLYQ9Qvh7pdoHMhYCoqUg3fahDThhKu8lXJb1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نصب کتیبه‌ مراسم تشییع رهبر شهید انقلاب در حرم مطهر رضوی
🔹
همزمان با فرارسیدن آیین تشییع پیکر رهبر شهید انقلاب، کتیبه‌ ویژه این مراسم در صحن‌ انقلاب حرم مطهر امام رضا(ع) نصب شد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667376" target="_blank">📅 11:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667374">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
دبیر کنگره حقوق بشر آسیای مرکزی: بزرگی آیت‌الله خامنه‌ای در جهان به رسمیت شناخته شده است و رهبری ایشان نماد استقلال در جهان است
🔹
پدر ماتروسوف مسئول ارتباط با جوامع اسلامی روسیه: آیت‌الله خامنه‌ای نشان داد که تنها هدفش رسیدن به اهداف الهی است.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667374" target="_blank">📅 11:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667373">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=YHAlWI4TwrluUVRoOY1erf3q-YHnpmpKkdJ_PUk3of_RhLWY20ZNQsdbNI5XzqD_0dgNIj1nVDA_iqCxI7AXTaPmDGKdjiDO2p6AlUuUB32dmxD3RCu3xfUHP0x4IsKPn95IIOrjMSj0Cwi0q0H4-9-hEblCaWochvtcTd_jJEuckk_jgaQAk6OrFPhWZ0OzuuT8sreFfH9Dh5Hk-lHAPKNQVJ7RVtqVBcEl6GBoxIMiZqQKx9NJulozITLM6E_kQLRcH40QI3zul8tLVgxQsAC8bEnalgHKk92ryZED3E5KT3WJCxjBfBVL07dsRYZBvVPaenQkTenRC-rzdQa_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b9555d366.mp4?token=YHAlWI4TwrluUVRoOY1erf3q-YHnpmpKkdJ_PUk3of_RhLWY20ZNQsdbNI5XzqD_0dgNIj1nVDA_iqCxI7AXTaPmDGKdjiDO2p6AlUuUB32dmxD3RCu3xfUHP0x4IsKPn95IIOrjMSj0Cwi0q0H4-9-hEblCaWochvtcTd_jJEuckk_jgaQAk6OrFPhWZ0OzuuT8sreFfH9Dh5Hk-lHAPKNQVJ7RVtqVBcEl6GBoxIMiZqQKx9NJulozITLM6E_kQLRcH40QI3zul8tLVgxQsAC8bEnalgHKk92ryZED3E5KT3WJCxjBfBVL07dsRYZBvVPaenQkTenRC-rzdQa_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پدر زهرای ۱۴ ماهه در مراسم تشییع همسر و فرزندش به‌همراه شهید انقلاب
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667373" target="_blank">📅 11:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667372">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYaIvqz-auKl5VR5ZEYk-ahOAArBuwNJgq6BXxHkFicGEQgtNSnyF--2gZ8C_rFWluZkWI1BrCRVpXxNh2_jKF2vVnp6DzhYLq8nMnth5F4upzqRlenWpXh5pJeslRE1KyJae-7uYPk1tlzeYrnn-WqKU4rt2a8dIPcHea4MMaC0dYOQ6yYG1r4xen0vM4sOpOgZM-ihCAHkJV9znnfVrWCgoFPaVaORRPhV9LYMDUfXxbkQfKLSZ77ARt5ZCfnyuo9yBHva1qLrjgqDtk8Lw8urvSudYCYZbKWY7bMitqEF8OyKgMVrLUzaOZvucxL25aIpxsXtb5yg3W6HTwfwIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
شکوه حضور مردم از نگاه دوربین/اینجا خیابان آزادی تهران است
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667372" target="_blank">📅 11:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667370">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qllD8rAYNjjHzkLOFa2MrmC18ZaQ2abpSROE350gYeqTWHb-GuMYqygTVmNRdgmayLTJjH1_viZXgbfXpcotDAirvyeSyTF2LAPoupWP-ZbQ1wxyoZ2HtxXhi3dxvfa_aEaKfJ3v3ug0TfYxiXd5TVwQpuDReFFS8UZwznAnFJTGGn9dF0kPAAyh8CHPTVqJJgfNstFGyAvnX6VKUZ3oHvHrdw28cEn8mPov90RdhZ_f49K4Dc4fgikcYuDAtaopDZ-eCgIo69KzUyrUfDpjfUN9eltvKvrFfqjw1HxDs1ZVFpMOOMQlzOwCJ2hRnaRlERdvkAdTFZ7dvAP3bzPz3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲٠ میلیون دلار پاداش برای قصاص ترامپ/مرده و زنده‌اش هم فرق نداره
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667370" target="_blank">📅 11:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667367">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8044130594.mp4?token=C-BknVv0XeZr-X6EVHTLB9rw1xM3_pH6coDchHHs4tMFs_dZoDzaNA2drvop61eys8-F4TbfesNDmeOUvG1L7ILLiSjAKQO35g1afE0p-8FBPGv6-CIj5-CPgmZyy-BhC-zXDIHMt-913alEWqs-YOdb4ILpfHZqP_LWC61l-Bi154KaukC0C59rOvqNTA6P6Tmx9YI88tYZXwtuX8bx_jGjQzin7wdL25ANYp64Fi4Juan3yaUP6pNrmqbnnMFLWno2ALS35BKkSekQn7_-PWWEhEsmuL5i8NORBR20X-GmuLjP5bRxymkIaAfK9qfSV5zyEzgdNc985IlrQJv0dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8044130594.mp4?token=C-BknVv0XeZr-X6EVHTLB9rw1xM3_pH6coDchHHs4tMFs_dZoDzaNA2drvop61eys8-F4TbfesNDmeOUvG1L7ILLiSjAKQO35g1afE0p-8FBPGv6-CIj5-CPgmZyy-BhC-zXDIHMt-913alEWqs-YOdb4ILpfHZqP_LWC61l-Bi154KaukC0C59rOvqNTA6P6Tmx9YI88tYZXwtuX8bx_jGjQzin7wdL25ANYp64Fi4Juan3yaUP6pNrmqbnnMFLWno2ALS35BKkSekQn7_-PWWEhEsmuL5i8NORBR20X-GmuLjP5bRxymkIaAfK9qfSV5zyEzgdNc985IlrQJv0dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد لبیک و انتقام‌جویی مردم در وداع تاریخی با رهبر شهید انقلاب
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667367" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667365">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5925dd4ad1.mp4?token=EhJ2XHJBZXYRX5TjYwRFUrYeK7OX-NX5jsEtWG-aTTiJqxRHXirSTLOl1SkdWzxoeMYSbRbZQ51_L92bU4IsKywl80VbCN6HRFFCONriLYo0izEZ_alKBc6NwjK8aNCBDjHLUlWb8UgLz0AEbAnM78yyxPFjv0FbdkAEP4ruCTZ2QdPTg1TCtzYx9VrUDtGWsbCYLfOy4B6PioFKeMFvTbzxmlgMgM7iQ8XhNCZlyt9_2BQ-GrNYp-sI1VXa_pPqcLGxbU5gjO7ig93jNrIlZ-5CX_wx3JrwXAWn7ERcBRrQOfAWFimeXuDBmYA3gMO1MXZ5B9TItQlxougq4gkq_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5925dd4ad1.mp4?token=EhJ2XHJBZXYRX5TjYwRFUrYeK7OX-NX5jsEtWG-aTTiJqxRHXirSTLOl1SkdWzxoeMYSbRbZQ51_L92bU4IsKywl80VbCN6HRFFCONriLYo0izEZ_alKBc6NwjK8aNCBDjHLUlWb8UgLz0AEbAnM78yyxPFjv0FbdkAEP4ruCTZ2QdPTg1TCtzYx9VrUDtGWsbCYLfOy4B6PioFKeMFvTbzxmlgMgM7iQ8XhNCZlyt9_2BQ-GrNYp-sI1VXa_pPqcLGxbU5gjO7ig93jNrIlZ-5CX_wx3JrwXAWn7ERcBRrQOfAWFimeXuDBmYA3gMO1MXZ5B9TItQlxougq4gkq_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پرچم بلند خونخواهی امام شهید در دستان مردم در ورودی میدان آزادی
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667365" target="_blank">📅 11:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667361">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3920eff16a.mp4?token=qbJLlyfwVOAATh0rwhQN0cS_oW1N72WClw6hQp23oeh-Flm2FJx8v4Jn8dy1-cVMJcquZsXdYrPbmoyqp_WVf6Dcnf2CKbjfWOewcRIuTN9F9qJrCG1hHnGw9bdbX9JhA1kXC2TzQqXbqLrf7FqTxJlCnPpW7S9Jo9j10RZsRH16w5LqrIBQBuNgvw4TOC-Io3hVPh4ykfGkO6ft0-1vtmYUME-HL15UbE-o_mqS-hAMW_hsPVwVj86pqQwK5L0eo7V2i9pVpLxNLNWVX8ptGu_Y0MaECo3SQby4ROynfhpzCxNDWYJeAYwJ0OE6HSpjGVU9DR64m1QH0hi_BkiLTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3920eff16a.mp4?token=qbJLlyfwVOAATh0rwhQN0cS_oW1N72WClw6hQp23oeh-Flm2FJx8v4Jn8dy1-cVMJcquZsXdYrPbmoyqp_WVf6Dcnf2CKbjfWOewcRIuTN9F9qJrCG1hHnGw9bdbX9JhA1kXC2TzQqXbqLrf7FqTxJlCnPpW7S9Jo9j10RZsRH16w5LqrIBQBuNgvw4TOC-Io3hVPh4ykfGkO6ft0-1vtmYUME-HL15UbE-o_mqS-hAMW_hsPVwVj86pqQwK5L0eo7V2i9pVpLxNLNWVX8ptGu_Y0MaECo3SQby4ROynfhpzCxNDWYJeAYwJ0OE6HSpjGVU9DR64m1QH0hi_BkiLTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قدس الاخباریه: ترامپ در مراسم تشییع امام خامنه‌ای سنگباران شد
قدس الاخباریه:
🔹
در مراسم تشییع پیکر امام خامنه‌ای در تهران، عزاداران با پرتاب سنگ به سمت پلاکاردی حاوی تصویر دونالد ترامپ و سر دادن شعارهای ضدآمریکایی، خشم خود را نسبت به سیاست‌های آمریکا ابراز کردند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667361" target="_blank">📅 11:06 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667360">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راز آیاتی که برای هر هیئت خارجی در مراسم رهبر شهید انقلاب تلاوت شد
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667360" target="_blank">📅 11:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667354">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VoXV7sMavkKQACFYVDWMNHMhuvzaQ9ZSw7z-VRpZWxXKp-d7QFWDFHyr2Jy9PMGmPhMsS1KTITzrW9JtDTTOOPSDS4WtQg4xWG3t5W-g3KgJgkFHyAA7GtXntQ-RioTY96-3H4o1FdvKJ_SlGuSILDPQb9NpwGL_VInbue2V5uxCi1CJdwGz76rD2DBBIf0jO0GU1C53DpaMLc8QSVkH3YZEqF2v0DfXD_E2Pm6WxBfMMg6mR61nOqqgLrcj486bI9o7JKmoAt61I7iuUxKT6LJvgGAPqBqIA74QpD0iaWMb3EmNyUTV-OxN2_vaIPcrstf8IiG1gGSaIAKKSbXX9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t2tDsrQ4lp3SP-gMq4azT7XQXM7RMmYmvD8eUD3_eIFGWN12Ez7aEIIV7Fjg8c4KP8ngdgN9ld6UAjBd4j3x1PZiQ331198HwzTvZJJACakTzz-unvyF8YA6pnc6x40zuCrQaGgNfkFKBL6PDddCfwME4svPr4QQwZnweHB2xWf04WlyGyQkMTRO0xomUu_VKzACS7-vR9K5Vd5HmFbrFWqRO0c5uouML1zNwwovvBxkuQc4B82LrGxvk7C2iAr2QbI_wmC47V0zZuKDa2GtCPtGgNL6WfHT0hBi76gJZfrgiJAM8BBsMm6aQckPxARo8nayB2mxyhMu1bcDPeQL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMBx_W0iFeNH2qAlgQ7MwmtJCLDHuSGEsGK-8nP3CZu0Dv4TjyXg4aGDB_bKKBVwsQbOc1vMvJUd61o6yw6iTV3BPAEJU4VN8Iexuoch3loDvmlcb_bnOH88HV-54BwhUKpJg_4j4FWgcWsQikf6GToDqFIftn3c3gpHLKf8kaT6sWq4uLEsZQSQI7osF5Meba8QVB4vveBWE4VRXtg9OIlTa988GnMkiH6pBXMIw7JKmi8NdECbrilY0Afb__e-vj5HAeqjyH3iFN6R1eZ1QAw4HhWdmjyVBjf4_rs5H8gMHpw2s3JKevrE4NDvRJHWSCj0K_Ff7OcSRufeJLpSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/icOH8ygo1HNs68R1YeffoaFU5YMu5LeHAbebYPDMLe3cZ1rl7Dy6E4EroDhNffcq-t_NavzI0n0auJuTfwy4K_4WZbj0BCAzcd4HP458kYbsS9Y01-TlXVmsdaqCETf8kUvJPggp2cABSaanxZkgkYB5_YbDiV18q0qV52oOYVlFJB6Ggo-bijpx8AaPFrYuTZ0vH4jQgE6RlHxhKWmNkgQYhlAMmYoiUs8Ut8jXiq168Bv5gqdm9hdygs7pM1UeNAJdNc5nQ-tYnEeW7lVI_KV_YmbEgLTy-ilxy0zAxncyFM5i3FaCFbN6wVgwgcxD1LI5wUxEWdY1n_rSBnDrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cJmKbLfXtfdbkgc5cYF8dXad_rEXZtlVySrMoltx7jnC-rX6nz8xnto8RCWa1AEOoiTzzHX7WHgZ4m39xjQwWxWvmtBvgFBWCCgcBYPsLuzGuS_5dIKrneAftRgcPAc_Uj6OSWfMJWguyEndeNU5wzmvszRjfbS63pu0bzsZTJUSpYQwcVsJBwOqPZ_-y-_qYJhxQnKyTndh6eWXX9XUdtnhiwmTSQT0A_YUqlyg6TJRqraoaGqPCzbxke4Ztc8JY6Obcqqx_QIeye97lxNGbDuN7DIaCZa8Wl9GyrrSDuO8JUSA83ffruPFY8ScrtbI1B7wABT3qiXjOZdrd0HtiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rp24h7yi5wtl_ZPMtMeloyp1Usyqi67fXNgsmMD_P5HQzdJ5dmAR2IZSQuHGSxQHdyo3GnmK6o4oVK1KiqEzHBWtgCcw-THlXWLi6jzNTlbvHV5DC21fknjJk_6SCRK0QlSGHi3Dd3VDDOgqj-cIXTZC_QIihx3B2XnaRTeAe5fBjJNJe3WZQr4cKPOZ0pzXXj2qBBRqW3CHL0laIGBW5_-Cpjov1-h-yGRk-lU9RPR-T0Kj-kh89czAR8lOz8q49j99ftO9o3vfAuiF-sP1dqlJxyn23IvP5weiRMUiPdGFPWKa8cKek2kjrFDearizuJb5VGw5wIkCnFcw2J2Znw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پویش مچ‌بند سرخ
🔹
تصاویر مردمی از همراهی با پویش مچ‌بند سرخ؛ نشانی از وفاداری، ایستادگی و تجدید عهد با امام شهید و نایب برحق حضرت صاحب‌الزمان(عج).
🔹
این حرکت مردمی همچنان ادامه دارد...
🔸
شما هم تصاویر خود با مچ‌بند سرخ را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667354" target="_blank">📅 11:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667353">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a8e16d83.mp4?token=dBl9pophggVFeGPCLbBKg3dIGuwIJ6pvUfIq2FixK46M-BXl_tlbDH5ujmYn97HRTufLTyQv0eH7nLDCfY4C-UaJUMyVgK7_jbBGYBnDwTWWrscKBKUJVa5cqQJYYZcZaVd17ezwlCCC5Qah9Rg8qnDfIAaC57sJA7wbOIhGdP2y2FRKn9WOB3UBVLQH9FYPRFnliGJ-H2Ccte_UphagoM4Kll9W2cDoKZyDmCQWLqELfMgWEe8TK0FK9U4VbPE1N2g8MkahNEyds9Y_zplNdOttkd00YoWdYylkATwUv_iyliK5BSmIkv-WmK8XCNrQ3M2DR7pnhKL6ym66m40siJnyeKkWHiOzR_w68y8M4YTs5c8sJEf41X-Ip9mOUC0RgQ9kbq5V5wyxdIGFJpOMGPAVEQvjWv5kM4jMTU1svqt6LqENyEeM6C8KYRRhs-wsOtIQ9IBwHAHdSRsBG9t84osIkRHbBYWHAc6UPcViSovBqkqx6seH72gCTbQQzVWQqO-Nohea3ggjVcigs5V1eyg-O2mTufdkwg3mdsj6horiDgwNXRILeZaGxj2Vgm6gSVG9_7vx7TKZtVpvhMsFo5mycaoJn4Hn2-dZk0FMSg9M7MX5wmbnaLs5s4YW2v2RHLEilUhtSdBpRr3684op1mimkOpXmKAf7PW7inw-BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a8e16d83.mp4?token=dBl9pophggVFeGPCLbBKg3dIGuwIJ6pvUfIq2FixK46M-BXl_tlbDH5ujmYn97HRTufLTyQv0eH7nLDCfY4C-UaJUMyVgK7_jbBGYBnDwTWWrscKBKUJVa5cqQJYYZcZaVd17ezwlCCC5Qah9Rg8qnDfIAaC57sJA7wbOIhGdP2y2FRKn9WOB3UBVLQH9FYPRFnliGJ-H2Ccte_UphagoM4Kll9W2cDoKZyDmCQWLqELfMgWEe8TK0FK9U4VbPE1N2g8MkahNEyds9Y_zplNdOttkd00YoWdYylkATwUv_iyliK5BSmIkv-WmK8XCNrQ3M2DR7pnhKL6ym66m40siJnyeKkWHiOzR_w68y8M4YTs5c8sJEf41X-Ip9mOUC0RgQ9kbq5V5wyxdIGFJpOMGPAVEQvjWv5kM4jMTU1svqt6LqENyEeM6C8KYRRhs-wsOtIQ9IBwHAHdSRsBG9t84osIkRHbBYWHAc6UPcViSovBqkqx6seH72gCTbQQzVWQqO-Nohea3ggjVcigs5V1eyg-O2mTufdkwg3mdsj6horiDgwNXRILeZaGxj2Vgm6gSVG9_7vx7TKZtVpvhMsFo5mycaoJn4Hn2-dZk0FMSg9M7MX5wmbnaLs5s4YW2v2RHLEilUhtSdBpRr3684op1mimkOpXmKAf7PW7inw-BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نزدیک‌ترین تصویر از پیکر مطهر رهبر شهید انقلاب در مراسم تشییع
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667353" target="_blank">📅 11:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667351">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=UzQU-CoriXsuqBuLZr9fGyZUV4dE9ZIEp6L6AUDdz32tg0J8LCUkNmhhf_5SisYeNQyue311XVMLA1y2Krc6wH6-kVHCGVoi3zrEW_-Ukyod4JSsLthPfj2o1Gb38OQF1ws5bdEZobzERzl1jx7rCJAh61emKWMqIjWpuFJYb5uT6EuMvkvVONy8NGTOfqeyTyoIWlt798AQmWSJlgrvsmVzJ91F7fxn-dZfwBrGx0GYch-TPmbcrFkk_OThQlhqtCUWQ3P9m-K6BVWBnomWh273VoO3Pt9MwsCrT3a1cl7BQ36Uy4wPwqpPKBrZLF5tVJI2fdCPJ4eUNTrM8XGMzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a0deb299.mp4?token=UzQU-CoriXsuqBuLZr9fGyZUV4dE9ZIEp6L6AUDdz32tg0J8LCUkNmhhf_5SisYeNQyue311XVMLA1y2Krc6wH6-kVHCGVoi3zrEW_-Ukyod4JSsLthPfj2o1Gb38OQF1ws5bdEZobzERzl1jx7rCJAh61emKWMqIjWpuFJYb5uT6EuMvkvVONy8NGTOfqeyTyoIWlt798AQmWSJlgrvsmVzJ91F7fxn-dZfwBrGx0GYch-TPmbcrFkk_OThQlhqtCUWQ3P9m-K6BVWBnomWh273VoO3Pt9MwsCrT3a1cl7BQ36Uy4wPwqpPKBrZLF5tVJI2fdCPJ4eUNTrM8XGMzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۲ میلیون سفر با مترو در کمتر از ۲ ساعت
🔹
همزمان با آغاز مراسم تشییع رهبر شهید انقلاب، در کمتر از ۲ ساعت، یک میلیون و ۹۷۲ هزار و ۳۲۸ سفر با متروی تهران انجام شد.
🔹
به‌دلیل ازدحام جمعیت، ایستگاه‌های میدان انقلاب اسلامی، تئاتر شهر، دروازه دولت، فردوسی، امام حسین(ع)، توحید و شادمان موقتاً تعطیل شده‌اند.
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667351" target="_blank">📅 10:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667350">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8f1356ff.mp4?token=ajKAejthcxqOWS9MbSG2hjGZixEeWOz62BALBqdfK6GRKzsF8SZlRoo_ymYkPc1CkyFz9s9d8TuHHdLkEZ_-xqa41sN0DZkzVC6TxfCCOvhOVwaaiPauBV6vW2Acb8OvZQvil63nu_PXAVGUTrcdK9_KEput3UcJrTtL7dl-gP8t9HfmKfc9VccDRxs5DlOvA2pV0hHp2EiQ6VuiB9w80F-AIQRiMkRLBD9V4IZt86WOWRJ3pZFjBEbIj2CaUdioN_GKG8rxuHAcecRiQUt0EAtG5v-0N9A91WAdRcKzaDh3C3OywBCfuvoU9eBsbac49betRJKveX0PH9K19BmurA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8f1356ff.mp4?token=ajKAejthcxqOWS9MbSG2hjGZixEeWOz62BALBqdfK6GRKzsF8SZlRoo_ymYkPc1CkyFz9s9d8TuHHdLkEZ_-xqa41sN0DZkzVC6TxfCCOvhOVwaaiPauBV6vW2Acb8OvZQvil63nu_PXAVGUTrcdK9_KEput3UcJrTtL7dl-gP8t9HfmKfc9VccDRxs5DlOvA2pV0hHp2EiQ6VuiB9w80F-AIQRiMkRLBD9V4IZt86WOWRJ3pZFjBEbIj2CaUdioN_GKG8rxuHAcecRiQUt0EAtG5v-0N9A91WAdRcKzaDh3C3OywBCfuvoU9eBsbac49betRJKveX0PH9K19BmurA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شگفتی بلاگر ایتالیایی از جمعیت حاضر در مراسم تشییع رهبر شهید انقلاب
🔹
بلاگر ایتالیایی با انتشار این فیلم می‌گوید حضور مردم تهران در تشییع پیکر مطهر رهبر شهید انقلاب باور نکردنی است و از این روز جهان تغییر خواهد کرد.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667350" target="_blank">📅 10:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667349">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
کالابرگ دهک‌های مشمول از فردا شارژ می‌شود
🔹
از فردا اعتبار کالابرگ خانوارهای تحت پوشش نهادهای حمایتی، نیروهای مسلح و سرپرستان خانواری که رقم انتهای کدملی آنها ۰، ۱ و ۲ است شارژ می‌شود.
🔹
مهلت استفاده از اعتبار کالابرگ خرداد نیز تا پایان تیرماه است.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667349" target="_blank">📅 10:49 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667348">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b3669ba8d.mp4?token=ZlMmHp2SlfsMYmwuDe4SaJegpmqtp72_il-XFgK2kjQVWCBz6jdpmr_HftqyGAd9I-Jg-VlxfoGgwS4IXvrh2pEYCQUjYDgqJCqOKZNEkqLH4t5tESU-YHCeQ2oK0oGmN8IUl3f4_KKw8osq7sV-LAWhIez1U4RleN216gh99yDLtkzUmi-dbWhXmhzVHz7MlSS8ZURzVAQ-zj-2ajxCqLzh3bFdI50jC56v4y_6z62pKhOtjs0ZmrCcTj20bC6pOUpFrjaqWnE8zxEkPcOUVwL-Sa4T7BbbcN-jV2TpBWNJaEm2F5Tljn9vArjUREgTmCHiSu907dKq2paew5GHhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b3669ba8d.mp4?token=ZlMmHp2SlfsMYmwuDe4SaJegpmqtp72_il-XFgK2kjQVWCBz6jdpmr_HftqyGAd9I-Jg-VlxfoGgwS4IXvrh2pEYCQUjYDgqJCqOKZNEkqLH4t5tESU-YHCeQ2oK0oGmN8IUl3f4_KKw8osq7sV-LAWhIez1U4RleN216gh99yDLtkzUmi-dbWhXmhzVHz7MlSS8ZURzVAQ-zj-2ajxCqLzh3bFdI50jC56v4y_6z62pKhOtjs0ZmrCcTj20bC6pOUpFrjaqWnE8zxEkPcOUVwL-Sa4T7BbbcN-jV2TpBWNJaEm2F5Tljn9vArjUREgTmCHiSu907dKq2paew5GHhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری: به دلیل ازدحام و استقبال بی‌نظیر مردم خودروی پیکر مطهر رهبر شهید در میدان آزادی متوقف شده است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667348" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667347">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYhGxxu-n4F0UcT-Ebx9hF_T43IU3x79_cQrr5HndD1OGJMx_J9RT4nc_EQOBuPzaDjW_cTz5FSYd41Y47_FaJury_Onoql6RvleYEEqRz0CItXk3-ZWkysL7h2-yKXe6oXZ7s0h5-abobNjtT7MPVaiCLFjwbuHz6WSMSV6YgncLIeRaoBC1pBXreVg4I54Sc3BM3lt3HuYa070zzMvOXkb2K_d1VGqk1eTLR_JF-SDYtb2SII0KBSmnWEMJ4BVcGx3hwtHZxXZ0dewnVkALktHsYGLgZY37iYyeyu6pxYGmgnMJQChn4Cq7augT-i2Cxrlh6NdG0A15Ci5-UhdVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور اسحاق جهانگیری در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667347" target="_blank">📅 10:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667346">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/952e0ba2bc.mp4?token=krVSKiwjK4GUR08lt0zwmHp4oqRy_Aq9FYuDsATNNCb2fR2rBNxUyLUsZkqm6vcFTU9fNlyvdtxkywM7KisSRgkoTje55zQ3Ay_-AGhZrZZ6_PKcqWK3Ef0elDU9vcTogCipV34gS0rga9Fe6XmDu13_cZ4PMbPbcKaHEH9wOCdWw_Gx-HYUK83kv0tQ_KyojFjvao2MaF8JOtTG1bidHN7o3BluC66LT0mNQ8GRXGw9W7n7g7Sm1toQoS0HmXBNoDHp7MGbxlA7eA-SEwLsAgNhP6k6wChdF5sAONcp4CauicuOxHYqkPF6HKXtApMy7r7HcspDGlJsrPmIQl936g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/952e0ba2bc.mp4?token=krVSKiwjK4GUR08lt0zwmHp4oqRy_Aq9FYuDsATNNCb2fR2rBNxUyLUsZkqm6vcFTU9fNlyvdtxkywM7KisSRgkoTje55zQ3Ay_-AGhZrZZ6_PKcqWK3Ef0elDU9vcTogCipV34gS0rga9Fe6XmDu13_cZ4PMbPbcKaHEH9wOCdWw_Gx-HYUK83kv0tQ_KyojFjvao2MaF8JOtTG1bidHN7o3BluC66LT0mNQ8GRXGw9W7n7g7Sm1toQoS0HmXBNoDHp7MGbxlA7eA-SEwLsAgNhP6k6wChdF5sAONcp4CauicuOxHYqkPF6HKXtApMy7r7HcspDGlJsrPmIQl936g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب خبرنگار رسانه النور لبنان از حضور کم نظیر مردم در تشییع امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667346" target="_blank">📅 10:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667344">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f51e24ed2.mp4?token=WbPvZljHeZq_jZHug0ZdGFcjCgrVaCNuuC7zlV8KLHoL2swOdsUf_esBFbxgfQWd7Rjt4bhaiDS9DT-GD4GvjoNpiHi7pWkyRI9v8TrbmKkDtzzti97FlEybxmCtX5lPDDGKUELx7hgQatajD2PixLoNdSqV_aW4C7r7fXuz5piqGUyBOqZAS1cyStKByF-3wp03Bv1PbUE67a1cMn-AsHbuVNU2jU1ktQG5NBBjoccwM3JpRG80zHl6_zj99iv4fM9fp7QsTgzYTGwPiSAcxe0FASWr1mDNNg0SR8RDMeNPDH2UdN7MYR5dOW5uZT8-2CUo7nk3V2BEKPRRaRvBcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f51e24ed2.mp4?token=WbPvZljHeZq_jZHug0ZdGFcjCgrVaCNuuC7zlV8KLHoL2swOdsUf_esBFbxgfQWd7Rjt4bhaiDS9DT-GD4GvjoNpiHi7pWkyRI9v8TrbmKkDtzzti97FlEybxmCtX5lPDDGKUELx7hgQatajD2PixLoNdSqV_aW4C7r7fXuz5piqGUyBOqZAS1cyStKByF-3wp03Bv1PbUE67a1cMn-AsHbuVNU2jU1ktQG5NBBjoccwM3JpRG80zHl6_zj99iv4fM9fp7QsTgzYTGwPiSAcxe0FASWr1mDNNg0SR8RDMeNPDH2UdN7MYR5dOW5uZT8-2CUo7nk3V2BEKPRRaRvBcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیت الله جنتی در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667344" target="_blank">📅 10:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667343">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed1NbkmABWtF9SuSxbnIcjSVEI_v94TaseTszmn3x6n2KIz-n9RYW0Miq2Gk3tqM6oZYNJBNy1vRQ4qJC6JuwPSjjEM6KVdm8i2tD6IHBQetixGcn1J8y8z_Zc5s9GMF7Mng2EgWjfGZL0vmq1UfARJBzRkWcNSsCcfbUA_nkkdQOa5RAB7DyfP149SuR90oLAA9k01oCbvE7RYGaUQGFVNekVE-9_SHWyR2-ypiLnHJvfsYrKISO2F14b7f2Aem-zw5wAGT8-WcYVPMQmuGfojLmXedKwr36R-8WxYGN2OdgeFNJa7h5SOd6bi3GUahRk7m4c5ChqQ04CYaL4QN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانک‌های مرکزی سالانه ۱۰۰۰ تن طلا خریداری کرده‌اند!
🔹
بانک‌های مرکزی در ۴ سال گذشته، سالانه ۱۰۰۰ تن طلا خریداری کرده‌اند که ۲ برابر میانگین دهه قبل است. بر اساس داده‌های بنزینگا، پیش‌بینی می‌شود ذخایر جهانی طلا در ۱۲ ماه آینده افزایش یابد.
🔹
تحلیلگران معتقدند ادامه این روند، می‌تواند محرک بزرگ بعدی قیمت طلا باشد. ۹۲ درصد بانک‌های کشورهای در حال توسعه، طلا را سپر دفاعی در برابر ریسک‌های ژئوپلیتیک می‌دانند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667343" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667342">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5hVrtZGi-5_sM0awT6yTvVYXuKAwsXrHLT6v1rKmmXs5Dqb4_C3BLc8dJ7JNQ-ldzaajedg4H5H3OR_lSLfbLYEmTC7m0d_HTTYWGbLpZSA1h5TGZOESkYl4RPzR_pDxu0OG9A2azeQDtSpUoPYxmsS6ehzrMkfNliv0TbJkdqMuvRhBCWA5yB_FPDPaoxsdtytKhPIEuXPt2yNZ24h2TAhr7eeWEeUhvYgQrDWKasIbxaJheLtaDwGI9c58cC03MqvP37Zf3R8Qq5z8u8Lsg5MHZMXAjZbTp-BAhiaRov_NoPGWX_oGz3iTUvtiQU5Vu9ZNu6gLHgoOy4y8ZvRWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور محمود احمدی نژاد در مراسم تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/667342" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667340">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسازمان راهداری و حمل و نقل جاده ای</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGDgfVXzHjc4CPutjsJOGPaAqvhJrLS39pOcKYHzAfRhOmXxgOx5cAHv58hNAOSSuUqYVmduhJDTpoYGoGAcwat-E-IezSZeNpgW0KbhydtRjCpvSdKeEbFAs3G8yWyH4p_cT8NRyjU9SnMaNNXvX8WBN7uBrb0dmDp8Uz35PeLBhlnupy09r5b4_A1TO9d-BlHNzusDSlA_rrxgSm7heScg8FXNYZUmKUyxwosKuwdkUhDVB8h1EV3VJSddUVodbPUGOo_QWQM39ziNWLi9bDkG0-MdIKXmVLXnjjkpaDXHOizjhIkE-7NeSLU8siEaJ1DMD5nea2ig73N6d9PTNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
اطلاع‌نگاشت‌/ مدیریت لحظه‌ای و هوشمند سفرهای جاده‌ای در مراسم بدرقه باشکوه قائد شهید امت
‌
‌
#چشم_به_راهیم
#باید_برخاست
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
‌
🌐
@cheshm_be_rahim
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667340" target="_blank">📅 10:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667339">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26d1b7fb3b.mp4?token=P2ETJL-_sGvkoI9sF0uSIVwhxOvNnvN09WKxbuWugA2dhCnZoVYVHy0t0BQf7vNIHccneTZwQlMgwNDo2oSDV9bpXFVXXXtjGm8c3Q-V6DbiO70GcD3lcY5dOOlH3L7B8g77XHXs89LcotvU-D-bmFIzY665EtKmjZkvmYnMYIoSJ1BVVh9KAoO-3H5x-DrspS7JTWlhifwJgAnTxX07m-g4d26AKyZy9OO3H3IxaEtuJ3B0Q3tucpxj596mzZ9D_-opQvYOw1OnfVs2tyFxdi_vmdI1EyVlhr_jUuTHXnHEgRVUtRm7JKmj90dOSFc1LVel2orwpfMSdU2gLStIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26d1b7fb3b.mp4?token=P2ETJL-_sGvkoI9sF0uSIVwhxOvNnvN09WKxbuWugA2dhCnZoVYVHy0t0BQf7vNIHccneTZwQlMgwNDo2oSDV9bpXFVXXXtjGm8c3Q-V6DbiO70GcD3lcY5dOOlH3L7B8g77XHXs89LcotvU-D-bmFIzY665EtKmjZkvmYnMYIoSJ1BVVh9KAoO-3H5x-DrspS7JTWlhifwJgAnTxX07m-g4d26AKyZy9OO3H3IxaEtuJ3B0Q3tucpxj596mzZ9D_-opQvYOw1OnfVs2tyFxdi_vmdI1EyVlhr_jUuTHXnHEgRVUtRm7JKmj90dOSFc1LVel2orwpfMSdU2gLStIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ قاب هوایی از بدرقه پیکر مطهر امام مجاهد شهید توسط مردم عزادار سراسر کشور در خیابان آزادی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667339" target="_blank">📅 10:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667338">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
خبرگزاری هندی: آمریکا ۱۵ کشور را از حضور در مراسم رهبر شهید ایران منصرف کرد
خبرگزاری هندی (ANI):
🔹
حداقل ۱۵ کشور در اروپای شرقی، آفریقا، خلیج‌فارس و آسیای شرقی تحت فشار آمریکا، یا به طور کامل از شرکت در مراسم انصراف دادند یا سطح نمایندگی خود را برای حضور در مراسم رهبر شهید ایران کاهش دادند.
🔹
گفته شده دستورالعمل‌های محرمانه‌ای در این زمینه برای سفارت‌ها و مأموریت‌های دیپلماتیک آمریکا صادر شده بود./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667338" target="_blank">📅 10:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667331">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3106edd7.mp4?token=KCI6lvqg3BOjeAhee-tHyTg6qsjjRxGzA7fK6TwfOuQSDMLHuKKy68UNpGsKvRgKihMFtXJSvJaxKTv4bvIDTAvO8GjNj1pPIteoqw6shYtsFLoZkdLNf7GqTyg_yXDe7LQRoY_aMhN7ZiKkwZYAtd0tyZsqs1LpRyC_HPrqhG5L1ecGoPjAsY9TGVxfbH2U05Eo8GrTz8iPY-K3jWEbhafaDwLoz4EBsy9wE-zt3aQoitkGKt3dYjT133D-aUqpesOE2Qr5u-JyWbClygfWQ8qTbj6_x9VKMc9t9r6aP20NfaJtdwxGH6OD41MpBtQuQ0zwpS5xFlzKoZMsw7y34g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3106edd7.mp4?token=KCI6lvqg3BOjeAhee-tHyTg6qsjjRxGzA7fK6TwfOuQSDMLHuKKy68UNpGsKvRgKihMFtXJSvJaxKTv4bvIDTAvO8GjNj1pPIteoqw6shYtsFLoZkdLNf7GqTyg_yXDe7LQRoY_aMhN7ZiKkwZYAtd0tyZsqs1LpRyC_HPrqhG5L1ecGoPjAsY9TGVxfbH2U05Eo8GrTz8iPY-K3jWEbhafaDwLoz4EBsy9wE-zt3aQoitkGKt3dYjT133D-aUqpesOE2Qr5u-JyWbClygfWQ8qTbj6_x9VKMc9t9r6aP20NfaJtdwxGH6OD41MpBtQuQ0zwpS5xFlzKoZMsw7y34g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل کالج تا به ‌حال چنین جمعیتی ندیده بود
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/667331" target="_blank">📅 10:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667326">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P20FxI_uusMmlhllkkOhXry7YfGKsOprN5myEd5bScedpwwcvROUIglCkdDIS8jIBE4UPiXC5JRKAiNmWXdo0hlm6020vjTM43fCyAh6oRHg5kTEaQr0u7qStg2rgOgxli0I2iO88aXhAqAyDyPQpszVs3dV4yJZ2g6Q6ULLMrpc-pRMc0GRySoSDzhQp4KrzJj2Em0nQmYoXAMh81i6i0rS8yGFtMaDUQKC81hcqfSiq8m5N7MOQnsCgEuzMO5VUZ7d0Y3buqZ95APpF3GeR95T5EZT95jaWfPq4pXraQIYDchyvfRO5FQBS1A-hx732GOqIzkT0ponsJBPZu7dUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGDyCM2Jd08-IZY8vQOyJKa-IId10KcOOyajHPk1Lt8JSxei4YExMJA7DvOQYEK05ZWMfdkcUbZMGyrXjUYOHsj7dpJQnroJOEr0ZQkg0G1OefMwKqSS_0UVgfdk6wZ1I7gMyCQ3vhFSs-0Gzi-ZCSrFoB9Vbi_lOVyQGewD4t6wx8RNkmuK7r1lc-u_D5XhcG9Y464UqnpUTLT8cApX_mPUfZjHYjHdr6uyttVMNTH6IwD4CJo3486FmADpLWpkRvKZZAhNu0dUh-8kZhkbijuiOitp-yAaTG2yfpwhNdaULWckWiZk52Q28q8GgUZJpt7x36bX2wPRA6SnuY8TFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uWKPU0Id7Pp4nZ6TorCTv6XAZipIv0zx1GRZ--Jq4c2qrxJhvIzaXIrI7u1Jxtw8uVO0LD54vZqh4U9qb3JyeMx-bNQOlaUDHa-lGm-jvfj7BIIcMAmNfwblxf-n9BanTGmqTkndUUzQ0Dl-zQjeUHN0ZpUJ4gsdNMFG7zdKhzd5olpaOsaEDx9ioeLc_-Tr6vGWQJAG9ZopUqj-M1E0TjncgV8Ud78IqFfjCw4V6JXKBIWiZP_iGCB7AiUdvwQI6XTgzpxXSCh435SRQJacjm3kObsEURinmmeeN3m5Uh8qIL1N0EVsvrKJPUQ49Ximw86e7uBMVEjM_52TNoxl_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TRhMB8S0Zp_61aNU1IZlCj6wUXrxFCaO4sIuenBAlXiCUWmipWZX79ww7m6112N1UK8yqClcre5wcBlRQxkwIf-92_XAsR1cFR1IXfFOoS5SlhfJUlZt-zZdbkFwhidpfGDREteMwvs_3Pyi6_36uAa27v1_UoaAKigE67mvKNZiFU2IHqwptb4gs7CxYgtToekMMxaedFchszG6LmVQmp8ZNEtvMhnXLqgj6Tkd5rxArHF-rSxw2blPkadIIsOokhCZDcG8V5Drk0wS0Ci8ubRy39g9HMEFdI_ZbPZ8PprXRhFJZFL-1CwMcVli1mkJdKAr3Tk5-zOjiZf1GRc8TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jtABg0QKh1gyuLUHwZ4h97UsFThOnt552kCEXen-8swY4a3YDFTVef8DzDZHhLEj9mrgLsrze0uQ0lPbmhqXezf2xa0TtbcmLM3vanWJt31UfZ4xjxHgil9eR4uc3vBgcJcsYEUTH6vbmkWTHUKcgeKw_PxXXP45faLCLJtmtrB_n_8iNaiebFeV2Q5gwgJODT2it6NN_bclAIh8IRfBeYd2BF7O9ginmHMAZ0i_j0JW7Vk_a2EoZ0HTO-pBen8gSOFg_hXKg8cnmySdgCDQPrSogGIFslOHJCfMlVIJIBx0MXberrcUf8HbZwFORv-r233IdXMi0hwpd6dmRLkedg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
هم‌اکنون؛ تصاویر هوایی  از حضور جمعیت عظیم مردم تهران در تشییع رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667326" target="_blank">📅 10:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667325">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
شما شنونده ۱ دقیقه روضه دلتنگی فراق هستید...
🥀
🔹
روایت کوتاهی از دل‌هایی که در فراق رهبر امت، پر از بغض و دلتنگی است...
💔
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/667325" target="_blank">📅 10:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667322">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=TiCtcpdoKSP9-fIJTZqzRhr6hv631mypeCM-If4wSUUP3N5RUSJXr7g8TuKxHadsajhBOU8twKYO6jyNvT_54n9tow670Rdo8auh5flvTmgPO_g7Xwph3edLsQNeFbVC96dnbBoub3kd_3HSv9XIm1qpBt9WNH8_SW-KWJlVLgBi-Vn3lqKimW1jt3NWLHOgh4URiCrpBOVW5D6SxrZXVC6MEddY1vrKNymLNU3x297XqBQGYJKvAcC1lfUZVyFqV5xla-PI5Pr9dhMp3XQbsllDFsyW-KCTkprSZIkuvxTS5PYUXdeABkXbt0i2HI_d8LCaxD9i2kkZiyWTf44pGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa4bd5f908.mp4?token=TiCtcpdoKSP9-fIJTZqzRhr6hv631mypeCM-If4wSUUP3N5RUSJXr7g8TuKxHadsajhBOU8twKYO6jyNvT_54n9tow670Rdo8auh5flvTmgPO_g7Xwph3edLsQNeFbVC96dnbBoub3kd_3HSv9XIm1qpBt9WNH8_SW-KWJlVLgBi-Vn3lqKimW1jt3NWLHOgh4URiCrpBOVW5D6SxrZXVC6MEddY1vrKNymLNU3x297XqBQGYJKvAcC1lfUZVyFqV5xla-PI5Pr9dhMp3XQbsllDFsyW-KCTkprSZIkuvxTS5PYUXdeABkXbt0i2HI_d8LCaxD9i2kkZiyWTf44pGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مردم در تشییع آقای شهید ایران به شیطان بزرگ سنگ زدند و عکسش را پاره کردند
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667322" target="_blank">📅 10:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667315">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwveaxKNFJFws3FwqZiNqNV150Q3nBO_5AVnhsTMnPw3q6xTaMptd2rFo_YGNcFEDkjh3U8xRcc3gHcLd9ZxQB60GV4hydYRRFawxw4h8MEPU7a8HOOqHuuIHqEi8AQwt8vLYpmI_N8TBTjI0jBwXFeQerRsOlCCjexmgtaHj4LqSZVN4an4clD-X_7oiZGLrv_C9OdflFflXOTtjSeVIt6TmDBDoMIyFKtLMhhrHoUMmOca40RV66QQ_aMmL0JQ013hgwN-9q3XJ2zQ6yrLHzxurTNol32tKW-OC2sUxM_iQ9LKnNxYQc7YkxzwQKFHlc2_92VHCUGl2m5V0oVWEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZOx4kvwLvi7tgZa1vSkYMALK12ogvHLVDDRPUyvaB2dbXYg2sXqC2_KzEHbABDvIY-r7RT8Qu0Ap3PIA1rX-BP4TWQNeavp2FKi_3GQzYd15mkN85TZCkTLS5Hwba-9kXe61cy1GO1KSOch-GMeO6wqlXH97KywO0zO2-jWVO4B0whNN-Ib1u0i13ZPGmZSlPGOqbynNtzVv7hv_CKTPokHVqw-vKyOCeeSh7Dlsiuim-ksqtPcaeQETCoJoETBWHwDIDKLYAYSea3JbO2SaLfk1KLkSvdtTAURrD9MON9Z13IlJrGGYvmbscVx5QncFh92rLlUAKruDLyexIgbGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVjfmT8JJyci1h6qnZf89pYBbel6I73W5RF6hPgGxRgtkCJWXrov_Dv40V01xOvDM49fyzkqn7pZs_Hsha2iXADojIB5LRxbwJwJw-uDqTTyLhiNctJ1RDKPcQt_gyDqDm4aFRWuHw211zUfs8xE7_1f0lHRnLF2FAPA8qObpGxY1qu10kkD7OcFGoq9SE1WEDJEC8YbNXUpkY5la3rHy--pqL3ZWrJdkA8Ogjurz5fQu-fAoWkS_Gb8mvz7BZ9NskU84SSROpFm4bagQ54n-on1x1wAOa9VWk9VKJKZPZLf4wscmnBcbHJJM6sMXO8zHHDEYnjI5MotOlol3r9D5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mXMv_uig4nUmSlF7dCw9JgQGULBnREqkvPg84QNyPyDirvucFNG5A6yssgwbaOKavGYizpFgwjIZgxsODDxshHAPYpPrl1w7yTj037o6ICg3MA9mxuWR1Ro7O0v_iuoZVqiTcpj7ZzgNsIn2YHEq5caCz1-fMKUiOBIwzlHQNmuYrNr3W6NPr6kIyJYvoKW6YxG5Eu3fT85FTRIEauhM8K4qDENMbfoTMgv8O8a17PZcd7weGLVzT4O22AHEXSpwd7Zz0asNWJWGz90CJ9J_BUfYx_82Fr3t3mAPhAL2VMsLb1kxiSrf9uunphP2ZDe4GbhPN4e4rHfILXN3O38iNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CbTZhlXyZbegHva2k-Bw2H0IcqLmemdMfMS5lWZYYEasfnUr5I4sE_njUzKb72hwpB2-eq1-mU7TeY9odIxB7jy2-qOPUaBEWNsYMTLqujBA3iXSw4wzu2dt3aInsQVd3gfY243qBaHx7bLL46kmGiSv4UwyHR6cJ1rkBrUMAAEeYdpMZLYKF8crvqEn814ngd9pBG8uiZeroXE61ddMxefILVaE1FmVnpBgxMvW8fZuqGNgS-U_Ehe46FfR0KHwqxuq_iDhn4Qol1YIVYdaPrprnfwSyuWTcUvT1i5HuxB9wwpOljBmtbrP96z5f-uGOXTtaBEVSun6_6zqeXKFYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab365b2d7.mp4?token=H6w675Jti-ZXIAvLAZzZPW09ZW-XNQ5EPsCtSPrsX1xSxxVshjVm9VIRbTFr4SJxQRUade7ylMsRQsOlq2wQRRlFAJK69U-hZbEcZAM3VMpsmV3SMfe5DkoYRMtsWTHqV4ae_QMiVX3GzCqGbymzv4gREOhn90LqWfhYWt_ra75POBj0SR1nqqm111rQzue5vSn7HcLjw8snKRSwgvPFY07qQva8hBUnmT3XrRI3cspWnruIA47BMfI4nZrTDsL2Q_Zjgo-pWmnFL9SQEP27jTzez7im2bcOajvho2jcuoVHhfKEz8OY661rYQV-_FlbzRMC_8IcXRNVi1JlwNyJbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab365b2d7.mp4?token=H6w675Jti-ZXIAvLAZzZPW09ZW-XNQ5EPsCtSPrsX1xSxxVshjVm9VIRbTFr4SJxQRUade7ylMsRQsOlq2wQRRlFAJK69U-hZbEcZAM3VMpsmV3SMfe5DkoYRMtsWTHqV4ae_QMiVX3GzCqGbymzv4gREOhn90LqWfhYWt_ra75POBj0SR1nqqm111rQzue5vSn7HcLjw8snKRSwgvPFY07qQva8hBUnmT3XrRI3cspWnruIA47BMfI4nZrTDsL2Q_Zjgo-pWmnFL9SQEP27jTzez7im2bcOajvho2jcuoVHhfKEz8OY661rYQV-_FlbzRMC_8IcXRNVi1JlwNyJbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خیل عظیم عاشقان رهبر شهید در میدان انقلاب
🔹
تصاویر خبرفوری از ازدحام جمعیت عزاداران میدان انقلاب در مراسم تشییع پیکر رهبر شهید
🔹
عکاس: فهیمه فرخی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667315" target="_blank">📅 10:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667314">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8bb0513b.mp4?token=LMt2nBQXmqV7CT0Zmn_-8Z9lNVajQL0O-2Rx8_X6QU3as5YQII76wHXXHyjxgLHc3roKCnlBSoljhYvDWxbhFLI0_E2UjPZVmZ6ecUoDRpJkg17hs3GnGKFRVrvktXgxIxGEhRBbmCrDZ2ArvsICIEcSWl4bmFb9fcx_5cmJORi7kyTxeHiEjHE4IEZ0SHlu50FV6NsFLyckLoDSJODBw95RM1-D59le6RKkl8mAJn8e8wlnJHu419072edB4UZK38F9GDkMJVajbRkFR9e_GijZklM6plrDspssMZdWb9f-XUiEABW8NLQrUZcDEMZ80PXokJweUNYvOUhidik--g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8bb0513b.mp4?token=LMt2nBQXmqV7CT0Zmn_-8Z9lNVajQL0O-2Rx8_X6QU3as5YQII76wHXXHyjxgLHc3roKCnlBSoljhYvDWxbhFLI0_E2UjPZVmZ6ecUoDRpJkg17hs3GnGKFRVrvktXgxIxGEhRBbmCrDZ2ArvsICIEcSWl4bmFb9fcx_5cmJORi7kyTxeHiEjHE4IEZ0SHlu50FV6NsFLyckLoDSJODBw95RM1-D59le6RKkl8mAJn8e8wlnJHu419072edB4UZK38F9GDkMJVajbRkFR9e_GijZklM6plrDspssMZdWb9f-XUiEABW8NLQrUZcDEMZ80PXokJweUNYvOUhidik--g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی دیگر از  تصاویر هوایی حضور بی‌نظیر مردم باوفای ایران در تشییع پیکر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667314" target="_blank">📅 09:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667312">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b5806c9c88.mp4?token=YgnL9CiVuJoSvGCtDNg7aLRLY7TQtPz8X33ZgliByN1GVKTEGQ3Ejf7LZafNg4H3TkIymcqwkYZxC7QOL7jHgz2f2WWd3McPDE0EIIzMRf4BXmBn5zd8Wp4cQF4MEmXho0NG86o0BhstgjvL9VutmoviWvVu9tum0PqBCUVEwcWAZUIKwEj_23yn1-5xKC5jN4ddTMSBG8HP0KfS6G5a1EIpdnfs1f_41siDM_-HPNVyS3dUP_xZK0BAxK1yGd-HM4YK2shrXsFdGG2LtN9pG4lSHo-jwzQHmqcn9EmB34tZjStz9AxrD6aFEral-5PgprKyAhreU6DKy-pDwGA5FDcA_Nf1j3TyM_agfsvcntR7xewHINvy8O6S9ow6LCNJApB9SrAlqueNIY-FHosWOcjsGK4cf04ywgw9aoSofXz7nO-1NZOfiuEEU3HRpSG9SQzUpqV2faMg3ZODINNyY6bliNZKlve2uiyFQzVz1wDZcbMShhhSyAH9azyCd3BiaEFGwKYLZkpwO78ErmG6HZBqbUaz_kS3eZ20e5ZEUY6Qp2-PF50sL7pHJ6iZZOUd2z7a2uGRo54B_9BMXLVFVlj9yFfRPpESh_qah8ybnzbYkVIwMfzYQZyyxpxMNsOlrzUW6MslKSXZn83sBsluev75SPXmy4Egmr-jxTmEvc4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b5806c9c88.mp4?token=YgnL9CiVuJoSvGCtDNg7aLRLY7TQtPz8X33ZgliByN1GVKTEGQ3Ejf7LZafNg4H3TkIymcqwkYZxC7QOL7jHgz2f2WWd3McPDE0EIIzMRf4BXmBn5zd8Wp4cQF4MEmXho0NG86o0BhstgjvL9VutmoviWvVu9tum0PqBCUVEwcWAZUIKwEj_23yn1-5xKC5jN4ddTMSBG8HP0KfS6G5a1EIpdnfs1f_41siDM_-HPNVyS3dUP_xZK0BAxK1yGd-HM4YK2shrXsFdGG2LtN9pG4lSHo-jwzQHmqcn9EmB34tZjStz9AxrD6aFEral-5PgprKyAhreU6DKy-pDwGA5FDcA_Nf1j3TyM_agfsvcntR7xewHINvy8O6S9ow6LCNJApB9SrAlqueNIY-FHosWOcjsGK4cf04ywgw9aoSofXz7nO-1NZOfiuEEU3HRpSG9SQzUpqV2faMg3ZODINNyY6bliNZKlve2uiyFQzVz1wDZcbMShhhSyAH9azyCd3BiaEFGwKYLZkpwO78ErmG6HZBqbUaz_kS3eZ20e5ZEUY6Qp2-PF50sL7pHJ6iZZOUd2z7a2uGRo54B_9BMXLVFVlj9yFfRPpESh_qah8ybnzbYkVIwMfzYQZyyxpxMNsOlrzUW6MslKSXZn83sBsluev75SPXmy4Egmr-jxTmEvc4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار العهد در تهران: ایرانیان خواستار انتقام خون رهبر شهید هستند
خبرنگار شبکه العهد در تهران:
🔹
ایرانیان با در دست داشتن پرچم‌های خون‌خواهی، خواستار انتقام خون آیت الله العظمی سید علی خامنه‌ای رهبر شهید انقلاب اسلامی، هستند.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/667312" target="_blank">📅 09:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667310">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e090af8ab.mp4?token=D03qNstf9PRZb_B1b4XQ98y-rtTrO3AmG0QwXtBypEXJTH7-v-TQlRzoglPWZcQOLarr2wRQblQa3EkG_lS5hZZgDpntFNfQYJIPuoCJ2t3jm3Mb4kWLGDT7Utu2XfytGmkrTjhKe6bdEf5Xqmde0kOMfq82Ml5uxgAItN73VZK5M-Z76c06BJP5EVMXyfHQD4LxmYLbVS657PRvI-8Mv9HZrq1Fj5dMlBfvSZvszk9aJROAxyh3PNdhDyxun5zH9MlNirgafVBnuvHTRWeQ5jQ0QUyQZLcVan9XF0V0NWRb3-geOzaVc0oX48JmO0YzjdkbEjbOCWYE1R9ElDrO0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e090af8ab.mp4?token=D03qNstf9PRZb_B1b4XQ98y-rtTrO3AmG0QwXtBypEXJTH7-v-TQlRzoglPWZcQOLarr2wRQblQa3EkG_lS5hZZgDpntFNfQYJIPuoCJ2t3jm3Mb4kWLGDT7Utu2XfytGmkrTjhKe6bdEf5Xqmde0kOMfq82Ml5uxgAItN73VZK5M-Z76c06BJP5EVMXyfHQD4LxmYLbVS657PRvI-8Mv9HZrq1Fj5dMlBfvSZvszk9aJROAxyh3PNdhDyxun5zH9MlNirgafVBnuvHTRWeQ5jQ0QUyQZLcVan9XF0V0NWRb3-geOzaVc0oX48JmO0YzjdkbEjbOCWYE1R9ElDrO0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از تشییع پیکر آقای شهید انقلاب در میان سیل عظیم جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/667310" target="_blank">📅 09:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667308">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73797f7d52.mp4?token=bJoVQKV7W_urdvvxqtkWo9REhXUYxSMbVfKxAiP8tJHwzzWetG2GiSNlNg11lyhp795dkDi2c0_lq0RoKyE5exEZ6aZnYOyWrAU4ltVw5et0ZHrvPlN0uzv2piMs6HfBPjo3RR_UgjdpI9AiW5hRIj_KUtQ1_ZbwX6z69VQ1wsoCAVK_bz_BHkLS0DId3BeTMFYmipD47UkCNaMGNu8rnMoJmck4ybLy307V8Fn3eMNYtmhjPtwLuuBCrIrmP4Hat9ztExAb4fqA2KOy01bYT2V9EXyUBhuScsiV3gnMoJ60rJj-44IXZQgcc_60lvkmcYZp8rf36kXkyvH4uFZmDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73797f7d52.mp4?token=bJoVQKV7W_urdvvxqtkWo9REhXUYxSMbVfKxAiP8tJHwzzWetG2GiSNlNg11lyhp795dkDi2c0_lq0RoKyE5exEZ6aZnYOyWrAU4ltVw5et0ZHrvPlN0uzv2piMs6HfBPjo3RR_UgjdpI9AiW5hRIj_KUtQ1_ZbwX6z69VQ1wsoCAVK_bz_BHkLS0DId3BeTMFYmipD47UkCNaMGNu8rnMoJmck4ybLy307V8Fn3eMNYtmhjPtwLuuBCrIrmP4Hat9ztExAb4fqA2KOy01bYT2V9EXyUBhuScsiV3gnMoJ60rJj-44IXZQgcc_60lvkmcYZp8rf36kXkyvH4uFZmDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمای نزدیک از پیکر پاک رهبر شهید انقلاب در مراسم تشییع در نزدیکی میدان آزادی تهران/ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/667308" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667306">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d5593cf4.mp4?token=pw3M_jPX5iKvCA7VmOHJvXkxqlmqoVLLpn5pS3xuoXmM4pefwkda-2zzCDwp9PXVMFVvS64KjZN3y8dDYmohge9y182JflR6dUH8G9fVDJMHCQSYqZP6BgSC5XMWgWSZe33TT2MAoma-0C4TLPzihHeDeKkLZChucuIYuMqXljk2vh8CQMr7gA4i9mKg-JyRMIC5d7mNnrG0StsibSiLOA49HvszdyQDVdv_1cwyfAGDpi5kZbxHIlOunIq4WSqcumoKnpu6WQ_uQpUFVrSU5NGM82-IhzRCFF9aQMqH0txNSn6QAWtE13bC2kcrOcJia0d_bxTm0uW1fyPMtrEEUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d5593cf4.mp4?token=pw3M_jPX5iKvCA7VmOHJvXkxqlmqoVLLpn5pS3xuoXmM4pefwkda-2zzCDwp9PXVMFVvS64KjZN3y8dDYmohge9y182JflR6dUH8G9fVDJMHCQSYqZP6BgSC5XMWgWSZe33TT2MAoma-0C4TLPzihHeDeKkLZChucuIYuMqXljk2vh8CQMr7gA4i9mKg-JyRMIC5d7mNnrG0StsibSiLOA49HvszdyQDVdv_1cwyfAGDpi5kZbxHIlOunIq4WSqcumoKnpu6WQ_uQpUFVrSU5NGM82-IhzRCFF9aQMqH0txNSn6QAWtE13bC2kcrOcJia0d_bxTm0uW1fyPMtrEEUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فریاد الله اکبر میلیون‌ها عزادار در خیابان آزادی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/667306" target="_blank">📅 09:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667303">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=KLom69jqMSDUvvBkxJS0RG3hIxOwHpRFnh2JhdO5oROETpi5kfsOcgHpXsWKcKHm6i_IwWeyugWZnJHEhgf0otaKF8ozMeRDWnYivzh0vFLHe7_5BJjz6wEwgn-UbwDCAm70s2tY8B4SZ1KDzWsfrHVay2GABaKL1X4JcKkfHGuvIeIgNN0Y6BLW-G1PI_G0jLROsQpoHwzALe9txIlzATHrUdqA6tFoBZt2h0zuezALjFu9Zfi0ibBRAifh7xy5i5qZZKXZzFc7zBNOwkmyHEXbAXdP5u3qNz2b9JA8j-a7sdtZwVHa8wkWgzGG905ToZaT2KvQ1SB2dxdOlh0xAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd5fbb61c8.mov?token=KLom69jqMSDUvvBkxJS0RG3hIxOwHpRFnh2JhdO5oROETpi5kfsOcgHpXsWKcKHm6i_IwWeyugWZnJHEhgf0otaKF8ozMeRDWnYivzh0vFLHe7_5BJjz6wEwgn-UbwDCAm70s2tY8B4SZ1KDzWsfrHVay2GABaKL1X4JcKkfHGuvIeIgNN0Y6BLW-G1PI_G0jLROsQpoHwzALe9txIlzATHrUdqA6tFoBZt2h0zuezALjFu9Zfi0ibBRAifh7xy5i5qZZKXZzFc7zBNOwkmyHEXbAXdP5u3qNz2b9JA8j-a7sdtZwVHa8wkWgzGG905ToZaT2KvQ1SB2dxdOlh0xAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جای سوزن انداختن نیست
انبوه جمعیت اطراف خودروی پیکر رهبر شهید انقلاب را فرا گرفته
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/667303" target="_blank">📅 09:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667302">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d1f796a0.mp4?token=XIQrRhKcWHqndRwEzMhYjZrUgoYw82LhFRpy7arzZ6-sFe6pWDZ8OUaXucNGNeHKJwcTRmi2CwwP4jBNPzUDtEhezWyECrwXK_m92ZLdDa5jjJbzncg4-v15SsJbtSZMbwdbaogJszQCKLV8wYd57_I-P_T6NZ1VVJaM7D0oxT1V5GrG71DzywOhHSulDGfgTll8WcsYI4_Tsyaz1vEwvoH4pdR-PrnO7OkgSAqARZO9t7lydLeg7Al6QdUDwrVogDNh42H0o6mh2uTH4-4fEapQfmbMzty03e2A5eRnRpIU3GVlPJ1NgqYzRfeoUGFjUtTuMOMDotM1jaXjOyx86IOm_96sCF7Tg1pRcFU5QlkutU9mPDa6bBnmwOxOQf6WuBUlFzloZsw_07-gSQ7FI82HiETHE0pVh1oWB-d3iffLmImgYTx0g32HK2oqtzYKhonywaQhAb122BU7gyv4W3ns5my2Vdw-d6Q_LMlurbUuk1xowfmwTKXB5q21todgTgxVhkfY7Bumdd-jSdzYSZEJRg1goPzGUx0mEkLGnq3YIb3YDse-9BjQUnkWhj7-pMmlebE_yL7HuOxUFl0FCQWln3Jl6fzsxayyrglDRIgrFGzcH3M5ey163hFj6IaloLl0ARV-vCHCryH79k-6255itCcFw9FLnXilSIrqlwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d1f796a0.mp4?token=XIQrRhKcWHqndRwEzMhYjZrUgoYw82LhFRpy7arzZ6-sFe6pWDZ8OUaXucNGNeHKJwcTRmi2CwwP4jBNPzUDtEhezWyECrwXK_m92ZLdDa5jjJbzncg4-v15SsJbtSZMbwdbaogJszQCKLV8wYd57_I-P_T6NZ1VVJaM7D0oxT1V5GrG71DzywOhHSulDGfgTll8WcsYI4_Tsyaz1vEwvoH4pdR-PrnO7OkgSAqARZO9t7lydLeg7Al6QdUDwrVogDNh42H0o6mh2uTH4-4fEapQfmbMzty03e2A5eRnRpIU3GVlPJ1NgqYzRfeoUGFjUtTuMOMDotM1jaXjOyx86IOm_96sCF7Tg1pRcFU5QlkutU9mPDa6bBnmwOxOQf6WuBUlFzloZsw_07-gSQ7FI82HiETHE0pVh1oWB-d3iffLmImgYTx0g32HK2oqtzYKhonywaQhAb122BU7gyv4W3ns5my2Vdw-d6Q_LMlurbUuk1xowfmwTKXB5q21todgTgxVhkfY7Bumdd-jSdzYSZEJRg1goPzGUx0mEkLGnq3YIb3YDse-9BjQUnkWhj7-pMmlebE_yL7HuOxUFl0FCQWln3Jl6fzsxayyrglDRIgrFGzcH3M5ey163hFj6IaloLl0ARV-vCHCryH79k-6255itCcFw9FLnXilSIrqlwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ را می‌کشیم
بنر چند متری در دستان مردم حاضر در تشییع امام شهید:
🔹
ترامپ را می‌کشیم.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/667302" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667298">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZtQIHIQqubm533_pTQkk752ikHnu9iGgGQS-N1gruhKKehZkQ7TEKubKbYtPZd1j0tUms9p__d0fHa7x9aG75KNoBOyP1UiOSSwa0BYc9wr4H-sNHfK3GklHw0HY62FKrKEHfWa45i_szMqPsMf50XVMGvn-vRVU-5lXH2HKDZvRCAdzXwQasiVDnPxglSU6tqsP-KkMmZD_nTlr363_8EK9oZsZabFLnGy6DL1S9bieOL1IzoR-5LY8HdVNtEDqDg3Eiun8kWQU-RE4d_r_8nRYZSo0JHv5aw40T_xum3VgFJwQpsxiQussLil65atinGc3EkCcrvUsovRKDq5s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XzoZ9LlgyNp4WfFyaGXONo4jJM1SuQOX5GnVsaH-sGYLZSSRCi3VVujSMobMtUM858yUDw8zyBChJm8OAzk4PnMPqNJMCEN3dDEkq63vgAPfMW-X-8sQjmLEWsy48HZoosGO1zN68hE1aBDd5fXGHwif4amp6O6GxQys4upGtLoXtT6I8lbLbYnYOg41-kRCAfuknsE7jpPGFdZlmRtRcNsRcfmmrv2ZYMTPDaspZUur2KmdBe-N_FvmqWg02kpezpt5RVvB8kBfO8UWp3uS_u0ftfrTENCMzHAffPn-9ysr5Q1P1TG__dDc-YqKTCODKhywlHZjB-mgKHDHi7eBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UXyB2BsHZpw5k_mAGRM3T-mJ-SGbw_nlF4omAUQG2OknbbQEVAQHcBjETyRK8-fXJhqNPV_DLAjmVlr7pk6CI8esDGhJsEDDBkLRidtaZ7MHEwFMXVFWRS82Q0p9lyIFzV6zpqRz0-XIR61L6zetVSZ2wqKVfEf2UgJnfZuehsUMVsGUbyJx_0gfUIt9gVSO0gECEHDyJG28dTNbq1VmZi4wEX7V4OPZng02YeAGYvNZeWB0Z901wzApsbm7AYCVbOhrBnqFeumZFeY0G-qsAhinEZZnI-h77pvl9HuIaTykCT1kSzq8uX0_9lCoSYl7wptFhbcg9YyN8gp_9oB-dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GahSwBeY46rq9fGvHZ8AEMyBj4gcD_OkLxMbexoJnOBZP3QFIrzK9uYIMslfQRwWdeDM3mftxFy2gSzh7NJ_WoA42EUOQDx_Dtd83R9DbPqVduIPpzb7Z6aTWk7P4C21fqrZCRzctHa9XgwWTUpo6DHpdXluLVC_OierRzzxhpcsG3tsV3UVGCP0uK5vuMWMsydCyPUmlhU-hmSvBWLH1Bi_Nb350_-agkdiKVNGKIkhm0oE6S_6EvJwOaF454uwfSRxBH6pZMJ5WfNtVbumKyauHvzBW5VnWNzlrH5g0LSLzj5-Pw5Ol6QHh0vs-c5vbLNj_F4GTtT1HpJZNmnUgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خودروی حامل پیکر آقای شهید‌ ایران و شهدای خانواده ایشان در میان خیل عظیم جمعیت؛ تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/667298" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uftA2Bxd_bCyZ0L63v16f0Q4OtnRVqzdxUXxW4DD0kSel6n6SmbKJnYvlZ2TT-uEyo4Yocg3274mm2P9EL-p097MqpX6qZ3zUpa6OZGZQFmjYWdBcWGDhxu4wNhkpy5N2O-cJTn3rq2OI550iwkkb-nrpVzDWoxsNNAhITWbtB7lrsC0btjkRcvoV8lyx8pzPV7AGDMB5O5Wkof0gOYbAy86p48mj07qolM-q5hi-dCfWcXq6RCvRWbtYajmbxu1JWX1nVTxImwP2s4GPuPME2meSKuNQUhhCkURFiZsprmoutOaG7BxBM4YxyQXRzq-D6_i4Tp0FfI4Kwy-LS3AkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CMESpaoXjTj4Nhx6r_t2RXAcoXHfq4T4riY7AwEnks46-kObnxvkNZDgTF6c9_NAexjFTU2wWnDYXQRYVJWkm2ZaB6qBzUpRq8F3pOLC00WvFvilzWijxtcTN4K6GXh-YtZUUDsbnCtzZPv32LpVrbyjeH8yLqFRYrPU5o2nMSyCec4ZwiPVq_yn6ZrpDjqrd2sk3AGKkNF7JTV6iwohqaPG8nx-NvPfSvPuRCliigjJr0FLCHeSIgH_vSHjjyOt9eWPXXIDfTy9lQKx-XKzN1UlhOGkrOPB4uzLP_-jQXDGUB9qTrjNcLMUuUQCn1VV3-aE1UJ5VO_g7_3Ucxvm5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/PQnGwAXLUGpqUdC1QkUFXWxRKEp4jb41Vn3rUl93vnnfcrpyeSMgQG0zrFKn2IRAZN-cGEoeAnXCq79FVAR07oRZPr8XpXmZ3hYIiNPCPuRivJia4qTRyeEjgfaaJRFjywkgkpmmaNgK_XfbBVdC4mRgE5xdl62jXr9RPdoMLES2akPcblxE2XBcHFW5CKTOqTMkTfqPjRWp86_89o068MeQI8Qlq9kpdD6U3yg8MM1q5U1wkMwRIljmjd5DRJVR_LXpNiuR9EzfwyTRGwQaBwrHWO5yHjzE0NoIeZrFYtxv0zoQar_ivq_GCnrrOWR26APjxARVgroHaymvAxdSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NlyXEbUpi7YAu6iBo4LlVcXPUY6EcTFlJN6D03qE1D2jIuUl2EU4fRaYXpyA-h_IXKc8MOMLmTw6ElTNyL77tnP7G67mFjWyfMxAG5jf6Wwo9cfsNOoDo7HFTIUFHBVMAGLrO4NPLIAKl1DNFkrIcrWm0SKyCfXMje1ELQj8uNSsrRxinFUico4Lp_qPzZ049UpAZvhkWU5KmlKXY8ngtgjrdOX9I4DUyQSCJWzUhK_dO_AKTDdOg1WnnOlP8-vvVEfIsFirIQrgupDRc78x93vRkfn95KMpDLmYOQcj7FMBu40WtBW3eYN-O0Zd68WEX05NvrE6zaPD8ttjPycvWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iIxucdciCo_Aeu9QnOZGXw-Ultb-_gosuEjEPJjOw8tbrxv6Jw1rBM6snyx0_FHkQkgEbMqWGMqPn-FyjX6TitfZ4eVipZdw_j6dUZN9kriEo8zDqJBcscGq7Z7h-_rLcknY5CLNRoC8Kz-Sa6V6voJgbeArYBhUMrrJNPYnJRa-TmfTvmo1uBMxs24Jea_vEzXJrdVvHUTPMbeDt4njXq4ndX3aIxpxM7i2PidTBl6IOEcGbjffC3Bcrh-2Lfz6Lljx6GUEHMERjiw6j247LE2I0HJ8JNtkNbAdLrILm2d1nGUvUDGoKkp9j3XWuEFrTXWm1OSkuYYkTT3helwiUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/k9FLekvGpjZuP5FhJjKPBlHh7pL0dB5S2HAin2K3kIgJ625EFNMWanBtSejqygd25hHlxdlAZ4t1Z_rQAiwMS6ZaH3zdhHkdoGlBa44YhCBkVMyLuxvo3UvnCYeZd-maZKn8WVXJmioZ_mIfWxHraFBZ1kjd1MHC0m2RcYRZy8ak7OKA-r2e3aEoWBtM8qzbmsL2-pUsNURHWAgTc4Np_Ew3qUMBW_6CBtyhThxBpL1UMFUProPba29MZ2XWf6U2ivbIYe6C6LLmturXVHcNENTOGzlaqz79YeY9qf2Ag-I0xJiXv85VoFX9VUR9Ye_eA5mksJTtItiEkXUGGm-BGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qYQRGwlJMA9ssuy2X6U61G3VvQ5HL3_mlz30xI7ID4GT1Un2jehfRWrESn01rtdx92udQaANBvrsejyTRtF1us40JqfUpeb3QXD7ZIgkPwjxrNbmc1alpsFIvoAlfyQ2XAnQEivrdGN27iCsZ1OFT2JqjKECMrEnmwPgMgKmq31yaoyliGn92aJfj8iradUN5mLW-7mJbTS0GTYSbewmFh5tORYuzI8KicdiLgBMiJj8KIXFBUuCL2r_RNVASlmwlZvLQW5UFe6Cj8HsactGwr00UD6MVwqnSCy5g1HG8nIWNuuH5Um3GzFzuiJNREI0vSc5iXdhbVVL5yRSLTVS0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aeJ1p843mZ76gigjCA9-7DZWrmaVB4-4CdY3m7rwZwiy2f9pSwoVKgXOmKZ4STYMdWrKs9UuF_L2hrf7UjAbyDqnKy7bw8o4ykpJjotsEt9DaMYTTuxZWYqdbyj5hU_EORjPW_u-5jLhpAvooZEJN2fm0J9bgZhm8Xhh46E2B5iVLFxcZo4JKXNhGE5imebzRbyL1eo_dZo3th6HlP2A5hDx1ffoOJ13dg4LlC9l1M8DIlXvvGTjlo6DRlBs4j3gMT5G9SsIaRfBSok6aBfq6pa5T8xIl8Qm6pGj15A8Gq7L_j7z3zMHVj3N-I9ubP9El_DWaAv1g_8VyQdKIk1v9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tmVXGKydV5khbq_k7yYmrz2NerzfID0qLqhrDoP8pAxiaJDHVtTE999K_uVGtHsKtMGaQTTHR-jEpV8rlMIcxUquIWZyyOcj0qO37s2f09rvdmmLrKHgUvbBhzmlkGwDo4AW25OLOTyrAqu2czPj3m6gatGalsYQG-ty7T_PUBYKIkL7pQxgx-GTjH0MjHB-hk6T-pBKRGVbxBOW5-iFoWAA9z4HhDKKH2KK8f4r3BgboQs-pW93qxSVMWmScdy168eL6BGWKduIVUQZ9nzCpbeQAAkXgByRvfVGInaXdzIzoZqTjqPTNRxjHfdUzpjy62BGj6l2b7r3eHZxt9ni5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I_R6ymXsEsFyx82XS12Su6WHcVkM_Kj4FGZOLot0U9TcsG2tbCCdBJR_3-HCgyQlrPtXHrkzCvbxEkJbdLXM94cG-Nm_Rspw8nfGYRs12VlnewVb9qX5yvrrVEDEr0_uqzwXrigX_so0WLrdsIedDaof5m4PgFubOU4LhHmnf-ixHp5O7dg7i7IBnfqPReHjOWf_hjJ0meMIPwCAqTGkWVkzrHFNoPyjkcjlJVCfpy4DNq8vk-A4GB_alFMqn8512eo9FGk-Jzx97HAtVi4BvMnUm9pgzBTH-gwcvb_2VjHdqOBZ3rw6SbGVCYDcZ1EyhNmF2VXmfH7SxuvbesmTgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
انتقام، حرف قطعی ملت ایران است
🔹
مردم در مراسم تشییع، با پلاکاردهای مختلف اما با صدای واحد فریاد زدند؛ «انتقام، حرف قطعی ملت ایران است». هر پلاکارد روایت یک دل است، و همه دل‌ها یکدل.
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667288" target="_blank">📅 09:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R3zXmg8rQSamvWEwU6eqpt90Bg6qYZwlvuJBC8FH1Girhyd4iXO6T161zKkWTHVv6BMdFsARtyd457D-2V6RKYFES14CLlTevBSqfYfbcD-qzMgj6f17vWKpF-7U5L6XQEaJRY2nz1uP4uLkrpqwCVSt_sJTcZP0HTLWtjwXrgZulsZW8qRZTv5Cd_17OsbHjVP8nFtPbEM1SnPGY_o6J6OeElkclxdbmH5LKJZpcEIfEz0sYqgGvmrERlTsN3ykx8gmQBrPTPRYTFuvWkMUY6g__YVYkuHoIF8HVz_WNjTRQiCEMp4PFh7ftBktFS3cpYFfNCRDOmTl-3-7lEMZWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خون به‌پا میشه
بنر خون‌خواهی مردم در مسیر تشییع رهبر انقلاب
🔹
عکاس: سمانه صالحی
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667286" target="_blank">📅 09:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667284">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=d0uQ0crFduPW16I-hKucD-a0hkapGFAQ0ODktqH-tSYBE3M7cM8he5tH1UUOhkrlYFYmphmZ1_r52IcK59B-NP9pk00VEfr4FS4awdYUsAT9ODJbCr2q65N72d_LhixNbOhnrmvtUWVMBjulJi3pDgURr8-RQ2w8wMYRFSoLLjOyvqmQ7U652NDZ2uOwlXwven6MYQ7Og-ZDLB2V9g7UCLP-Sc52Zzdf0YOl9LDVFR35ERjyc_Fug6V1JqyJ6As48RwPHVXyTOFwG3F5s_zao74lOX70qq8Dyp2w7Gm2ebOOFIAWkXeZaqfEBlk6v6OsF8cbTdQ76c-bLJJJppHmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5771ea7f1d.mp4?token=d0uQ0crFduPW16I-hKucD-a0hkapGFAQ0ODktqH-tSYBE3M7cM8he5tH1UUOhkrlYFYmphmZ1_r52IcK59B-NP9pk00VEfr4FS4awdYUsAT9ODJbCr2q65N72d_LhixNbOhnrmvtUWVMBjulJi3pDgURr8-RQ2w8wMYRFSoLLjOyvqmQ7U652NDZ2uOwlXwven6MYQ7Og-ZDLB2V9g7UCLP-Sc52Zzdf0YOl9LDVFR35ERjyc_Fug6V1JqyJ6As48RwPHVXyTOFwG3F5s_zao74lOX70qq8Dyp2w7Gm2ebOOFIAWkXeZaqfEBlk6v6OsF8cbTdQ76c-bLJJJppHmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماشین حمل پیکر قائد شهید امت در انبوه جمعیت زائران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667284" target="_blank">📅 09:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667282">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c3ad72e4.mp4?token=sMiL438olhmMNuMHlbu5bekWVUhUd7HDkEjM5xNEIWxtfh_Qkb29Y_wqDl_QH9B-ikoS6gR-73O1kRtZv4-Fd6I0CExc2Nxeiiz7BEsQEXRRm293Vs4_57YuONFBfJLKmwFuVLDbE4N6mdHhElI0JwdOSPD-jfVaYxTk47HNV59VAdzyCUq2yPrUW3A5Ri9Dw0dfXV91vPsJNWvkQSZhfTBU5e-U2SRT9MHL553mYdAJzWMeuJqhQU54XwNb9Jh8WdII8eePT9AoqKtbq0SnJylJ0957Cn2NCA7sVxBKjeP1hg62ykBRn8H16G_VodWxExytuEWhZL3ve8csiunAoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c3ad72e4.mp4?token=sMiL438olhmMNuMHlbu5bekWVUhUd7HDkEjM5xNEIWxtfh_Qkb29Y_wqDl_QH9B-ikoS6gR-73O1kRtZv4-Fd6I0CExc2Nxeiiz7BEsQEXRRm293Vs4_57YuONFBfJLKmwFuVLDbE4N6mdHhElI0JwdOSPD-jfVaYxTk47HNV59VAdzyCUq2yPrUW3A5Ri9Dw0dfXV91vPsJNWvkQSZhfTBU5e-U2SRT9MHL553mYdAJzWMeuJqhQU54XwNb9Jh8WdII8eePT9AoqKtbq0SnJylJ0957Cn2NCA7sVxBKjeP1hg62ykBRn8H16G_VodWxExytuEWhZL3ve8csiunAoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون مراسم تشییع رهبر شهید انقلاب در تهران
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667282" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667281">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba60ac675.mp4?token=rLc0dirike64MlBntG8hDMJ6R3-40zKsGwjVljHcBVfJcC4eAfoe1TpPn7rxZf6XFQdMBLJyMAyK0b-Edr5PwnZstlz8VmXoVz9eCqHw9gLXCVdc1D0XREHpppgCwiuNYuqejPISTqgZyTdhpMe92bBOgEKszCC0EUIcZ0v3dxBWLgairEZqAJdCI1A3oE2se2fL12ucClpVm9cDm3Lk6FhkqxOmiCfHe6nULpM9s4W-odcVZMxaR5WOkj8r4KEkKJ7BTDCvtYcKCuB1cXN8KoZStMYeOMzG-F4bYNbTigtm-AJTu4qaO9RzNMVSIwexsNTvul_N7K0jjr5SEl6VjqseUxySVa45mW5nqcg2wcsELYsJjhIuyPxw2ZwMzhIYhMtVtc4TO2i8fQJGsVhrV0BDrmK2x3ZJ4kH9hWy2Kq-pQLCa6ZQVl5Nuka4BtgveQoy5-Zlhc4Etu6qKSOImSi2duQ0UjAtkw0ClRcdWhq3t_6BWU2iI3kgKmL81aG3cA6hmRbJdkJ0a4sLGjDKgYe3u_HqIxeNHH9j9rNqxFvVIqvCrdqBS0dBDAUyncyBGT59X8k_B1hFXcWdfWxjWE0Mkct4xfWD7R7xWGjsdtVZDMp22HOPRT-DFfUoPN6MjqNRbXOxrl12mqXSR0cmbniWwHRsRmzUCb_eOM2Bl_Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba60ac675.mp4?token=rLc0dirike64MlBntG8hDMJ6R3-40zKsGwjVljHcBVfJcC4eAfoe1TpPn7rxZf6XFQdMBLJyMAyK0b-Edr5PwnZstlz8VmXoVz9eCqHw9gLXCVdc1D0XREHpppgCwiuNYuqejPISTqgZyTdhpMe92bBOgEKszCC0EUIcZ0v3dxBWLgairEZqAJdCI1A3oE2se2fL12ucClpVm9cDm3Lk6FhkqxOmiCfHe6nULpM9s4W-odcVZMxaR5WOkj8r4KEkKJ7BTDCvtYcKCuB1cXN8KoZStMYeOMzG-F4bYNbTigtm-AJTu4qaO9RzNMVSIwexsNTvul_N7K0jjr5SEl6VjqseUxySVa45mW5nqcg2wcsELYsJjhIuyPxw2ZwMzhIYhMtVtc4TO2i8fQJGsVhrV0BDrmK2x3ZJ4kH9hWy2Kq-pQLCa6ZQVl5Nuka4BtgveQoy5-Zlhc4Etu6qKSOImSi2duQ0UjAtkw0ClRcdWhq3t_6BWU2iI3kgKmL81aG3cA6hmRbJdkJ0a4sLGjDKgYe3u_HqIxeNHH9j9rNqxFvVIqvCrdqBS0dBDAUyncyBGT59X8k_B1hFXcWdfWxjWE0Mkct4xfWD7R7xWGjsdtVZDMp22HOPRT-DFfUoPN6MjqNRbXOxrl12mqXSR0cmbniWwHRsRmzUCb_eOM2Bl_Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یادبود شهدای مدرسه شجره طیبه میناب
در میدان انقلاب
🔹
این کودکان معصوم با  موشک‌های آمریکای جنایتکار در روز نهم اسفند ۱۴۰۴ به فیض شهادت نائل آمدند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667281" target="_blank">📅 09:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667272">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gSVnUTxWvjDMw_Hgf0om3O6Y6Xqv5-FbAmUdeIYgZ3TnY1lhFCdhoC_IaUmdXoPe2Ca-PvSZdYXoDVd9eLzmNghWIwoFcN5wRdB2Q_eZ2KQCsCVYDAQVXnum2GQlKyVcLpmFIHl1l3gEPuvC-saqJGp_LpPPWSJs-J3eWKF2xfkNRpfNQ5BI448I8L4ywJWSpPsW_lrmz47KEreAnoYhxjI9cNfCGfvXidn214bjUc0Q06RVflzFJh34r6eyp8K_ayaJG7Iktq0UtDrwLrTB07qnb_zcDV3ouOz9BcpKb0OafcEQu-KKvIjrZRPShi9oFw8c0uMpN6jQkHWXZUT8xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tb4XbXk6s2DW3vzhGQO5xzMjj1BHbAGCunT83ah8Gch4DrrwH732mn4ew9p6Bb_KFf8FIyKUyKxuehcuwe66_zqkRoMWpc8sgudZ6xlFfv4Smkq2dvEwAJcS0rAVirDid5X94_HFIYzpwQXwgr6uGAgfBIO1J6eISVAe14MWhIp6qS6bG8j9L8EuPd8YEKVybIQ22v86aSStiMGxtay9NS6mzB_vgH3XPyu-0HA9WfbEwbwJfvnWllGZ00B5IxQTlq2BLkO_GxHNVhFJvX2FuohjKwb2FIzqx3M964wGFKdIkXZJNNTtWAmmgArku8asNsqbfpPbp0yWwBA7uAhuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSCGCYPxrpr3J8thEJzYKRSLpUDm32y71YUZsCo1SHPGVPGpVFWWUipkCUB9fptvfsN_dd5rPD6NwRyN_rbnvh2W4JqwpiqjX1CjMtBLS5eQ2PGLar1RFndu6UIzJtzlvEwpfSvgTjzJmW9kSownzR3mEHhAwLkAX1Tdtzhd0QlvcqMOqI3hqQbWOlhkk-tav81xhkDn8HNJPIoM5Tbvut5XHwfkqiatRBI5ddjYq5KAgiS_rJu83FisPn6D67mi4fdtTLm83fUS0lgQT8_io7r4TGhsjfzHNg87sfdKs0DmZDMZ5s-Y7-WtsVkaea3d912Q35avEHzYqvjmiSMWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LLqj3msu-MpEifyeiA_PSjirVzjNVzV0y46Pci0q5IGk_O2pobBhPUN8kSIOjQ0EO7kbAEjfw9Dfq7fV9661pWJ28BW7glBeR7CyQctB4BD-RqFJ_7JPwnApwRJbHDnS6_EENKHvIuFDiLZSRwEs5-uxgUnAZHKav-9PYECjFU8l0nCzNujyTFLnHb9_ED-yehwGk6xm9z3H6UERR9FMkgh1ek6jlqY08iM_coGYPEGQK4FCyPRXWoWOUxbTlYi7HmHUT9nOqyLySMjhLw6xTmO46cXI1nBugUyAVs3vZMoTdEk-nzL4Sp5AZ6czZ_5q-hlubflCcK2w3vk3t7hv-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HKH0sf_KPiGxKeD26NK-xG5Dy3iP0_WbRz0m3MGyEdoIkfb-1mrTrQoRwMUHVZhi8WzzO5VS32W5P8QgKpBkKRCiCehVpmHNWHq_jZ4EPUwpA0edGXyQZZ37DhYMcqleKMqU6MBUYTC6e-X7tkjm0Np86a8p3P1F8xgsxhP--a_dOcELIfEaq-8wlfW_SVBVLFPUtYBPg9LkOKoXajJ5wjQA2CjKsCP0u6rYWpEb2QiEViMA0a4TpziK_Cnvr4TBJF7D6ZIF00yN937ZDusuGh0N7epiF7t8bcawGX4x0-Y-rFCI-tmAB_3k7IfBHc3tNb1L-appRRzbP-OP5d2W7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9NnhjUPeD4YXLfP6F9IbyvXWxiclcPMWmFEjEVAi-0HF-wnhCL1mOam94OM-zoWXzXXq3kz0UNL7hco9hRwmRBUgsHg_my1GQUIRiHXpmSo7-zno5hkXpBjB2zKi5erENJM_oojSpdz2uPHpk_kGuHaty3QjL9Jj2Q31QeS3F-vSY68vAWCpwuufSOR51SsG5Ed9A9ZqUqGOPvN0VaWlt1v0ZoDqlnm1MZFrInOduslRldruKwPLcb1AboU7OlkL7Q4WOQAjqF5nylmxh5QSh9a67S3g66Xq39-Xb5Sgso1rV5OmLbxkxtRjRAWIWCiE79G9SttOyJCgaYFuZJkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3i2VRgLCHE72aKW7PqoQqIxI86goUzRmhiWEfi_juDXagEatOfg92jdfQkpgYPb7WXe4lbe7TAEC5F-C4N30Pkd-ck5dS0a9-8sXnMVpJBndBVOjfyBXdQNl9kquuhNU5cPWGz8CWWcfX8ym-EUzqQ9IESUuIjQJcstm1N_vuJ3Zbub1bNOsF1Gax9ijeCoSP_nfg4Fbeig1Yo6YCuJWKOv1izsL5VhzrEjISvnxWElSdWxJI2oIDgQTnhexgoJE4o_9WeDHBsPZR1LIGeKhXdqVIkwuQ7rz5sptE0-Mo3ObMzi9bJMISgHhg6A9si2zsWk5hyStI7VQPIZHFewIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dqESiPVTTtFeb8ZxYsL1_1zWFtP2GF5J7BiNVgxVk2jAhZh-IUOFfi9OJHipljA1jDahunEt23-L5mCYd6TZnUuBaGlbxlHRkoZ9rWaDrcmplsFSMlSpHS9sFhAVERlS4KWq7xIB71qMdO4IoT2eDIz9NWO6lEzD48g6XBuief8ufPoBTRKZbr5AyICQcjblw-aV-1wyWo7b5D5DIKTKHQ__dtcBcdFEIfH4xUL95BYSCVyGxF_qSF84oozYnfq7TiAqYsvr6h9mexv4QFOzInhgxZlBUCveo9e0v4rNQ5cKvoY4HJNRMx8BKT3T8LWmTkwmIdoNTIjKex7bMXEjpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B-lojSd-ZfUPapIEbdXJJhykyQ6iBicXfyQcPocPSMb_z5BHrmEbtA6oOXOJGXnRN42h67v67zx4js0HzxiaKyLog29TPEd0jq7HZQk5TsdkLYRA1p3gT_l3-Ve7bdQG2aONroeOgFaaeNbnRjZ4Jxlt_RhIMKF1kwCrCYjaGZgKtINJTW7odWoN_Ccxi2pE8iOdfqC8VInKw0E-7r8U6cggVqN3i5E674Im6eBltUTHV5I60PB_qLFizF0vOsf2ZagLHq-SCuXMPKmyEI40OeREMDheHoRZFnD_F0mmk9dNbcl9u8ap44tjjvzGj5F07rRKHs3-RNM3j2mUX5ZuqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از مراسم تشییع پیکر رهبر شهید
🔹
عکاس: سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667272" target="_blank">📅 09:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667269">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c88bf2348.mp4?token=O9AzvF_piDy0A_7AnyRCP4eqyInBHfwvy3bZwkjWgzAxRF7zgfy8_c2Znu16Og7723vX-FDmICxUl56HIHYBDh9QohsKUYwFs_45KMgOglao0mA_YwclldtDi0yAPjplIcq5myXGllQ5OWzUrWDnU9_DlwYYlIzwDRid2iUs8L8Oj_w5kWIcBbs__Oeo4f7E9ewNTsAeIyfNY0HtgHc0PQMr1_DmyVzqrBUZ2Rw21VEJdibhovrt1z3gLj7vw0_5WJk1OT7QFmG78eJjPx_DrOq3Zae7CD4AzybN8MBtJxrwjdd4GQgeo1V6gnzydrLFzol9Y0UhE8CkXi0TRHk_wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c88bf2348.mp4?token=O9AzvF_piDy0A_7AnyRCP4eqyInBHfwvy3bZwkjWgzAxRF7zgfy8_c2Znu16Og7723vX-FDmICxUl56HIHYBDh9QohsKUYwFs_45KMgOglao0mA_YwclldtDi0yAPjplIcq5myXGllQ5OWzUrWDnU9_DlwYYlIzwDRid2iUs8L8Oj_w5kWIcBbs__Oeo4f7E9ewNTsAeIyfNY0HtgHc0PQMr1_DmyVzqrBUZ2Rw21VEJdibhovrt1z3gLj7vw0_5WJk1OT7QFmG78eJjPx_DrOq3Zae7CD4AzybN8MBtJxrwjdd4GQgeo1V6gnzydrLFzol9Y0UhE8CkXi0TRHk_wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قاب‌های ماندگار و بی‌نظیر از تشییع امام شهید
🔹
عزاداران با لباس‌های خاکی در مقابل خودرو حامل پیکر امام شهید سینه‌زنی می‌کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667269" target="_blank">📅 09:06 · 15 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
