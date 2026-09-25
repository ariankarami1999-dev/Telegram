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
<img src="https://cdn4.telesco.pe/file/VTowa2YT4JSguY_UEIRY_83e8fAdAX4v44whZpun5wcs48GhKwWLWs2bR9q8LeaudBMKFlZu2VYzVqQBR8MerMGe3dSWBkq9HWG4M7DZwdV7MB2cEC-v1ztGIbVOvlJmyotDyY3bIa8DuSxYBIhVU5nBcwI4J95X15JndBzyeFKT8G8tPdChe-qsLFfVSEsXGYScBA1j5ahRiVPQLyIIr06ZwXdM7qEi0U8a__krAFk7biDnTvFm85x12ZGXRnKFogl94AfbOkS2iC8udDRPk6v44yohFRESkqupz5n0axXtbhpITh62dsUHjhHXk3FoUWWcRA73383e3qL4KNvrjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 450K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 15:32:00</div>
<hr>

<div class="tg-post" id="msg-30415">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzjMrSy2WPnlLzPEdMGX40iaaolu2IOs3CcrO_LZJWvcABLw2gDDCwpx2-9XfYbgHklQXbYLmOu3h_SJA2l8jaGBEC-6ekzBP3362_KUs1dZinr3w6vcKQhm3QeGzj1E5FXQ-_60uLIPn0NGWSURZCLgGUBEWBMhVay1jq4K8J3MKd3ZH0n-Ur_XIQN7dea-Wqu_bJYGocdM0KOXC47mLqowEN2NC42AqMpxBIxiNg__SSWyVPlYdWzU9koUI9m3SrRJGxq-Cp5vtvXg4ZSQkCuP-AEdNZ1MC1RgKUdvdbG3n2LSzJ8yQ7Gv9zuJBNLekRWDk1Fni9KQqrV11XdYNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P6SWRgmdev0m83fg2VmCN05IKIvZEv1CEoTLdNeMONO3cZMaEjROz2ePVd5s_2tUkKjdL_WyaA0--K0VcJY1eXHbMet7kv9tQI41nlCgBBCxKD37Cox_32I62fh0KTxA3Wg-PZcLjBvgG5fjyngXSnE94LTkGh1se5sMBf05nNrpAmLjLt3l4Vrlz39ieGF8J06sSIqAqc3kt4LQCTYAZ3KPopsItYv34Yb9BXLTEAo7nbzV95PslwCMif7vHvBPF6gh59A1puapOskSjOdxq77CVP47y_JDzj1AYOZI9Qhb8SCXx11pnslz977XjgKvPx4iswd2Zkzeq3WOwDMBvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
انتقال سهمیه بنزین به کارت بانکی از فردا؛ نحو اتصال کارت سوخت به کارت بانکی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/persiana_Soccer/30415" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30414">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9587608d.mp4?token=vXZ4S2vti_eg2uryoFKr1u48vd1lgRYKFfs3asTGbz0Odu7A7BBRj7kqiuzuh5dYDdueDVfOxRhLrp4lVZRDlGlCG_DSmNz9D8zEjoa2FEVsu_-9Xir7KjyvcO8kPvc_o54aN7XsX5hit05EjhtI-303wRvvA5W-BN13hRmrkHLJ7IcyjEx646B57z1dHPuSojCZLrQRN_DDomuQmXnTMENQGmoCetXPEhwPY5lctR-W9WCNCfAMmlQEgPY3xtGJyP47MiKcGjfif6QzW9DFz8-2ZKyp3xG0pSuWlC90mZ9dyAQvxmtwGPOU6s7RgEz8NvdlnG48qlVsIhg3b-0IeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقاد تند جواد خیابانی در برنامه زنده برجام از فدراسیون‌فوتبال و کادرفنی تیم امید بعداز شکست تحقیر آمیز مقابل کره شمالی در بازی‌های آسیایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30414" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30413">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=FHVec2TEkVG6Ysa9PGubFX0NkA7ib5rVefQhWpZCNCb27rjoaI4B1DSogSFDjBcAmZY206gBiWLBL9JpTYApY_Vihl4yJGvM6DMQ6DxCHKRBDbZi2Xdsn8M7-n3U6j_uHaLz9khDJY7iClHBj6h-4zCZ1GsYBonE-vdgDTYuGq8Rb0q2UWEtnanWL3IQJBKHLj0HadrdVW9p9vxmLwM0NzDrolhOQA5yCaLk_lOSuQirNNzRcTvew_NT1LOYA7EGgtV7kCgLiHZNRWvfl3ZTV-QAajR48M7CQkyGiSDw9FHm2wCl4RPIvQemfYQNLStFvOriewWU1Ga0vaVSFWx1xDGsNJyZxMIFu9I27Xcg8vu1UqCbiZ8cDgBpqBi4DXw0Zdxta_JAqA_3XWTgjciXFgRfNL-VUrL8Uz61M2HLzUOHzltY4i9FdJ8w9RyT0O77o3Tdqc2NMev-jRBNtu9KHHdvrRtx-2U74xa_En-IDbj2Mq41uIOLKab_PpDMY7TMkhijhvdYW85m2vuB7E1I5g8JKxBLJXqNKk7tyr8gFdoLP0IXlmPrxCkqdWqFFkWQx5vVFDKYfBt0QbzuK2hoYXqhkDmANjNfyl-2AZZ77RtTy61eZoLHArMPtsvywalYK-nqOKwiWd_uTA8GO9SYHc8KYjo6zALoKT_9cPNLGHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6521c21a5e.mp4?token=FHVec2TEkVG6Ysa9PGubFX0NkA7ib5rVefQhWpZCNCb27rjoaI4B1DSogSFDjBcAmZY206gBiWLBL9JpTYApY_Vihl4yJGvM6DMQ6DxCHKRBDbZi2Xdsn8M7-n3U6j_uHaLz9khDJY7iClHBj6h-4zCZ1GsYBonE-vdgDTYuGq8Rb0q2UWEtnanWL3IQJBKHLj0HadrdVW9p9vxmLwM0NzDrolhOQA5yCaLk_lOSuQirNNzRcTvew_NT1LOYA7EGgtV7kCgLiHZNRWvfl3ZTV-QAajR48M7CQkyGiSDw9FHm2wCl4RPIvQemfYQNLStFvOriewWU1Ga0vaVSFWx1xDGsNJyZxMIFu9I27Xcg8vu1UqCbiZ8cDgBpqBi4DXw0Zdxta_JAqA_3XWTgjciXFgRfNL-VUrL8Uz61M2HLzUOHzltY4i9FdJ8w9RyT0O77o3Tdqc2NMev-jRBNtu9KHHdvrRtx-2U74xa_En-IDbj2Mq41uIOLKab_PpDMY7TMkhijhvdYW85m2vuB7E1I5g8JKxBLJXqNKk7tyr8gFdoLP0IXlmPrxCkqdWqFFkWQx5vVFDKYfBt0QbzuK2hoYXqhkDmANjNfyl-2AZZ77RtTy61eZoLHArMPtsvywalYK-nqOKwiWd_uTA8GO9SYHc8KYjo6zALoKT_9cPNLGHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های پیمان یوسفی روی آنتن زنده درباره حواشی امیرقلعه‌نویی و دعوت نکردن مهدی قایدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/30413" target="_blank">📅 14:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30412">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqwhVniZK4Ce0b-2jkEF1JkWhKaNsjUOC0AZqqM8dE20MZf2EiSewqwOeVK3o3fDNvgt90dkmOAxexcp1wLsI5crCrTDZHN_8qFa0M_1UjVCjLpUnVOua7hTu_9H6M8qM7zFI7PHnG9n02Bzxk1PZuDBuOS3Ts7FrHhx03eBo646UuM_L5Q2TW6DQ7zmjIqdn9Rq1MGFtkFomq574yx_qv3lZNkMy7fIkrxOORmT1HqSzwocM38lRYrz5jbHmtFtQd9nOMRmfZ3S9_aJkKuJFbpeW6r4AzWqIt493I5I27MsP-ogF4pgfUHqrdfn8jzJdYS_MdH6ZHyQLPA9EXObxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30412" target="_blank">📅 14:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30411">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgxSV9UAuhnxzRuBEknW-ujqgIx40Sg4_-zGKVMYKqTRpvsUzudHcXAhYxMMi2mLu1p-CFzKOLClsNHifMdE4pMMiGFy4lYhdTA_S3pQ3Ukkyd8L7Lfjw7unEPpf2aS8dn1_eM6jGTaqppziivrO2rtxEaUF3WL6J5eH650DfduNrFyFwOSGGO9cuzI3iIOQkCU-1y3B1lG-rppjyRdTWR3K2vUwu5shqiB-C0qfK2n79yS6TTjgz1WiJVqf8eVxN61LFNqIG4feAsTc2rLYOqAa-Of1sOe0eA9hqIdU_IWzkPiFZnJzyq3EyOiadD_S25ay2mhHKE7tom1sLkbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه سپاهان قصد داره درصورت جدایی مارکو باکیچ از تیم پرسپولیس درنیم‌فصل او رو با قراردادی 1.5 ساله جذب‌کنه‌. مهدی تارتار علاقه‌ای به‌سبک بازی باکیچ نداره و بلافاصله بعداز فسخ‌قراردادش با سرخ ها با باشگاه سپاهان قرارداد امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/30411" target="_blank">📅 13:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30410">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVPXnbEyWXJukJkSUvnptTP1BmbdnsIkID2UHRWGqKYK562P5XCbMnw2uXdDegtbC5A5g5hl5szvtV9MuQIz63kMyrlCwT48Vi7j7Yt1PgG0sgWySzwZ8qDWCXxm5PJWR6aR-Sx8dFKCYTnE-oOHH3wrEcUrAjxyvIit3QCybzWTvLyajwxZjIsQQhFbPAyPG1cCHx4glvjVA3glhcg_1p2mIulOGCnMD29fRd8WYwbbFxmKMk0nBsamDcukNl3I4kbMTlKr3L9-AC6Zpnb9Brc9x44FEMg_HGVjSl9aWIROlvhfUh74p35r7Sj8K3ryXQu8ingSEKXSNbCvQUEFAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج 4 دیدارمهم‌امشب هفته اول لیگ ملت‌های اروپا؛ از پیروزی خفیف پرتغال با گلزنی ژائو فلیکس تا توقف شاگردان ژاوی مقابل آلمانِ یورگن کلوپ و پیروزی شیرین نروژ با درخشش ارلینگ هالند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/30410" target="_blank">📅 13:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30409">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyxrXvq08QWydoMzFTCpI4jdIfKQBpb8u7JSIHHQhS64VGKMY0lY7VUK8SzEQk4slM49L7X4BkPq3QVQ1iS4OOdWsC9oa_l8fmH2wvd57W3uLTHaCJ7p0oumedh5soQBGyfyvKC5XKuywmBwh4zHcs6AUA5L87ZvoRjHJdZEJmAq9aLSYluPNTtzUUxeIn6o8lg18JHWufn2kwyH5WlMIMjr-Hcl8sl8u0orqwORZia5RHGWtr0IVflrdHf6c1v_q_Rq0l12sJdnvBypzWKA7Ictd2IDDfQiIsA-7Ny0L7hh5H1V5aqOjl1pyItLs6_GSmIXu5aHyFapf8kXmFW9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/30409" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30407">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLg2wivdnaP090j7ByZAi3BeRnU96sQIO73u8_7vsadZIJGVM-XfTlBCfguJLQu8sHC7eDTMJAmVtmuM8mtnjlP3T98XdBkcBh0Fq4brnl-X9Ke4assk8PqIE9rfqNg6sOjSRTgF2jeUuSYmlRbY1dg-cEaTHRms_N5SpM5FP8rPyFJ205HjpM9JxybI3vV9-YflMjkw7G1Wp_ADYNJUyRDxEMTh35rCMqcoiIdG_Simae906Bdj4Di4yaYy3JhE2Bl1x_3hkIqrnpObo90Ovis9q9gHuVC-rvbpgHUJKPqzuosj2I_JgYK-CxTYxX9WkQYqLEvX7d4BkyPyk92RPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30407" target="_blank">📅 12:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30406">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkjCTRHZybsmgHQ8WwhdPQhisLp7QqHEXPQYaAFrPWElzX18b9Sx0B-f3q6rnixqtMDsDBNuzghlDOMs-fJb8hpQZJMFWvHARRBfWJl8SA11486llGW-7957Gkc6Y4jcp_R4f7SH8keaSFNWAPAKRfhbdqGXQ8MHuQRNTgJUP8bPHOVp3rbQY4Sai2JECBQBEoRgRZ5dYnQmChfruV_T5CpBHGYI7untu7FmzcUVuS8L-_ewLhoa6Q5BE0tQVNRPQrOacIwvxY3Vu9QPuPBgss3IMJ-U-5SxZoX9ZEo4gWLGTQl6UFq5fInFJT_BopfaPo7mbh7uEyz2nAOgj_l52g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/30406" target="_blank">📅 12:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30405">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH4wtyXPJJcudCTM8MHWGUFU3xvWNWX9u-gTIhgsZh2T5kyziwrXc2_4hLp62sXiTTDrDbNXDeJ2HzTvy3Da88NP5oFZZopr2Wh4l_l2ASG-5e_S0ljnoCXLsGxnOSZPUKgr-wM3qSd6nJ1QRA1JlRdeVknrAtETOMGcs-BLiMJk-S06390KSrmwADM41o6D1tHzWuAbCkEdp8Qt1sxe95cJAohjyHRrrsNz6IaEAF3W0njE8jH6LjgjlfGr1DpVGn5TV4AKQiax26WhE_3RzKs8tp5dcalcBvQupVpZV4L7YyhnJ5FrXbWA5F2KioD1OC99f1VY4io7X-6NZO2dLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق پیگیری‌های رسانه پرشیانا؛ دستمزدسالانه مامه تیام درسوپرلیگ ترکیه 750 هزار دلارامضاشده و دستمزد فابیو آبرئو آقای‌گل سوپرلیگ چین 950 هزار لار درسال ثبت‌شده. جفتشون‌هم 33 سالشونه. آبرئو در نیم فصل بازیکن آزاد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/30405" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30404">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdQTG_etdGqxZalhoEf1sCNJT73oWIuszhJPw3aJrp5iBn0J7JSx3jn8odqDfrgimHWNLw0gq1kQVfmWNFm7GBtuU1cD-aS82YWchxIVqLtk21Pfodylz4oEo4RzQoQvmHxxRf3tEHgJHOEX9xlkuKUPDjnOuaRyVq2hHhYjTKYEjc2TTjelG1ZFyOQITXEbBb-OTL-8eOT83Xz5IdKXgWvFo2E-CQG3zMY6DY8lMFiHZ0UIdE3CAHqicmwuG0TshAgP2KZT3tPDNiXUYcrtHyJUzQqXFAzXLojMLUsgTNrESvYEdFgzXzJCra4z_7ptZgsuAxMATxuEaLtl9lZ3OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلیشا لمن ستاره‌تیم‌بانوان‌لسترسیتی: بارها گفتم بازم میگم نباید تفاوت زیادی بین دستمزد بازیکنان در لیگ مردان و زنان باشه. الان همونطور که لیونل مسی و کریس رونالدو در فوتبال آقایون میدرخشن من هم درفوتبال بانوان فوق العاده بازی میکنم بنابراین نباید حقوق ما…</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/persiana_Soccer/30404" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30403">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYPimAVvxhqKgHYX65rR_tzowMuPXmL2xhcpOECdc53LjbCShp6kN1SfGG7hkcsqtVRgjGLWewpyE5SE5baPsPlJl9AZmsdEvpa_zBQnsEfgv-MpLCbGxLiX7gBjB9TPWY84hieJw10A-F0U58WK42i7NzvesS58JyNMn1s5LHVkz__qwlcPdypjT3CZ09_94oZImYV0U4K0sJjHfbQ0opTL8mgZ_PQmKXEUOx8hfr5nFx6RDKqgUXEVZJLxr4ce0AZ0bPPiiwT71zew8PsRPUX2elXq6Wa7rDONsxYoXQSDsyf1aw6qdZAggAWEazlAdUsMr8657ALtcw7WFtWHww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
💥
جمعه‌های انفجاری در یک بت
💥
🔄
🤩
🤩
🤩
بانس کازینو مخصوص بازی‌های انفجاری در یک بت
💬
پشتیبانی آنلاین 24 ساعته
🔈
کاربران میتوانند در روز جمعه پس از هر بار شارژ حساب کاربری خود از پشتیبانی بانس
🤩
🤩
🤩
کازینو را تا سقف 30.000.000 ریال دریافت نمایند
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r3
🔗
https://t.me/+xNPVsLewpb4wMWNi</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30403" target="_blank">📅 12:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30402">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9xn8fpRkZVjbsATJEK2VhtnIcMuDQtdKsJeoOi9O5eLBMCOG4T3A_QmlWwpdzeVHvnf4j2dqwkKHFw9CdtS9zHlMjsOJq2_Q9nth3hfULE2WzLPNmdWBVvHTxhnG4X5K9z1YBw-lE63Pdi80Nekrp2BPF85sdZrbS-flsJcjbClo70mzIDVXl2YboJ-sDadCHRkTutqJqxokgWrvcL03ScGheXu5sn1RZPXj2BsY77AqlUHQWSTS_jnfetp88P0WI767m_FyhU7anZq4nJCsgn1gi-lku2YcvlwA--1dM5SZNowuwKpah--gd-6LEH42_O-HJbdCOyOITtDI6zlig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/30402" target="_blank">📅 11:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30401">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638f1de447.mp4?token=N3ptsi_jK8HtHVvw-r281QFsvOp93vgRxR1Mq3xPZq5txO_p0PwGU-a_To8ZMyCPTTgkT3lprYgyIWi23mns_zaxKwoc7mwR5FXO-LActB1wLzCpyUv55ZJKxLWgn9BzUoa4pCCJe872t0BTMAKW3qCjXm9wdZSw1xlcQqMH5_UnA0bolJt5VVRCGP-DNz4943Gtl7tiHjf5y_LiQfIEo6tKc01AHOZfMbYOtgySuysTqphQ6L8BpkHfhpFuuhHGXx2Ub_sL5AnCATEXgvpR1y7dJVsXW_G8purlA07SHZLwYnLfpK9jSWG01LPbCRmCD99X4XQW2n47Y_uBprT4cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638f1de447.mp4?token=N3ptsi_jK8HtHVvw-r281QFsvOp93vgRxR1Mq3xPZq5txO_p0PwGU-a_To8ZMyCPTTgkT3lprYgyIWi23mns_zaxKwoc7mwR5FXO-LActB1wLzCpyUv55ZJKxLWgn9BzUoa4pCCJe872t0BTMAKW3qCjXm9wdZSw1xlcQqMH5_UnA0bolJt5VVRCGP-DNz4943Gtl7tiHjf5y_LiQfIEo6tKc01AHOZfMbYOtgySuysTqphQ6L8BpkHfhpFuuhHGXx2Ub_sL5AnCATEXgvpR1y7dJVsXW_G8purlA07SHZLwYnLfpK9jSWG01LPbCRmCD99X4XQW2n47Y_uBprT4cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رافینیا دیاز کاپیتان بارسا
؛ صاحب جدید شماره 10 تیم‌ملی‌برزیل؛ این شماره سال‌ها بر تن نیمار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/30401" target="_blank">📅 11:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30400">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aL5CBcPSPt3hCp4BQWwz-kFIddkOr9yialdgX3shUfLI152GW9SSmnS7bzA7Zcu1wpxuF_E8IG36EzrsrcYLrrk2QD_hgqrSaYyI0GVJMhYlr7xPVwdFGBug3xJ0V55_v31tzjqtmVKioXpnulAx-1hSbOxkx766jG3_gPImWsUlnyva_hudUfCHABKJM_kSigtubdcmLxH76Nr7aSEhezVXuy2ijkObzRTTVYYsUXCoPPxqoqwCchbh9ukWFe8M8YBzGFxY9kNS1dOogRGjfgriZZnfy8OpW-AVJ3iQw1ocs_8zytom6OCwP1Y78_NAw5VrIQxIR1s-Nur7J_fAEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیویی‌کوتاه از تکنیک و مهارت‌های خیره کننده جیجی‌ گابریل 15 ساله‌که‌ بزدی یه راهی بارسا میشه یا رئال مادرید؛ هایلایت کامل عملکردش رو تو کانال دوم گذاشتیم. پسن ریپلای شده رو نگاه کنید.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/30400" target="_blank">📅 11:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30399">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/649db87b28.mp4?token=T7LLt5dmm5lt4JbkUG5SBZGBdu1kcOEnv_PML-zfyx5M1VdTDKa3yo1wnVd-AsclqvbS_hSzH0MD-cmyilk4FfoeTh3EgdXGOxMkaonaPgst2uLnA5n9WKiCZqx2qXeVcDx9skbxGP44dre9Yebhy4BlOrvF3yB-E-ENBig8r2hipn9s72_pXnln1F8-yB9FpHGfzbN9R82VB7qqgbTj66IWBFTSUpOeOCg2zf0pkkQWQ_KlW4drWLAXeZeqc-84c-zVGc4pid3Th-6HjKD1StUQ3_oeRec2fLeyMJZWhhtSE0JoudUQD-S-5SRMSaqHa47hnY94KL-bFDnJuB4SGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/649db87b28.mp4?token=T7LLt5dmm5lt4JbkUG5SBZGBdu1kcOEnv_PML-zfyx5M1VdTDKa3yo1wnVd-AsclqvbS_hSzH0MD-cmyilk4FfoeTh3EgdXGOxMkaonaPgst2uLnA5n9WKiCZqx2qXeVcDx9skbxGP44dre9Yebhy4BlOrvF3yB-E-ENBig8r2hipn9s72_pXnln1F8-yB9FpHGfzbN9R82VB7qqgbTj66IWBFTSUpOeOCg2zf0pkkQWQ_KlW4drWLAXeZeqc-84c-zVGc4pid3Th-6HjKD1StUQ3_oeRec2fLeyMJZWhhtSE0JoudUQD-S-5SRMSaqHa47hnY94KL-bFDnJuB4SGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30399" target="_blank">📅 10:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30398">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxAVk71szsbWae3IoVtvxM9x1zG8qFZoqnD1xDIGbwX6g8_C2e2oyZ9TfuBAYc9SO5c_v_ziVkayFL2vtb4gHNYEJ-uMyUNE3zmpcmmc7D_M38hH_zC8OVV7pNvPbWTFKUnF8z6LpAHhI4eiMSTtLwiMQU0fmWGBOb0-fj7mV-KE2xfjPunKyOSK7HEyBJwhqKsKr02-ktBPPXH2mLLZIvpNJ0wiHKJsv6hInEs07ZtnIcYoMbqikiMTvtmUTZt1uJPjFl898K_rH19R3e7mMxExFKr7URiiu636n-IdNVQQiqZrqxzvmz4Ka-D5zgpPTc_KsIktIBTi1dBXBOZL1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/30398" target="_blank">📅 10:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30397">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=sLHUTSfZD4hG5bgysmN1UFK-AO4ool8-bhMEEWGMjdJkDt7vXTaWuyKCNEr0xJ1mezYZBYyLSapPqlgtkk3oMStG__eJ2_EcqhrDelGqolFq3RvUwmhflZpnN154gPl7_dHaQannNfJYA2uLDeCIodIWl0r6zCRlqb_eiidKvnRJFFdzNiV_LJ4RDxMOcAg2Vum0ni1-ANyXJlJsw0uzsca_u9XWPQOaO4B3TjUMBy2snJJ4Iq3YlVmlro5gWQ8hrUkuQnRYVAg1FcFasO1sPLVaCr4PerR87y51Bkuc3D1LR5Ao0fmhq8s_APMiHm-oVjkhmz5dmfB7JNm9bVfxYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/698f9deb89.mp4?token=sLHUTSfZD4hG5bgysmN1UFK-AO4ool8-bhMEEWGMjdJkDt7vXTaWuyKCNEr0xJ1mezYZBYyLSapPqlgtkk3oMStG__eJ2_EcqhrDelGqolFq3RvUwmhflZpnN154gPl7_dHaQannNfJYA2uLDeCIodIWl0r6zCRlqb_eiidKvnRJFFdzNiV_LJ4RDxMOcAg2Vum0ni1-ANyXJlJsw0uzsca_u9XWPQOaO4B3TjUMBy2snJJ4Iq3YlVmlro5gWQ8hrUkuQnRYVAg1FcFasO1sPLVaCr4PerR87y51Bkuc3D1LR5Ao0fmhq8s_APMiHm-oVjkhmz5dmfB7JNm9bVfxYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/30397" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30396">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAyoNzBpKMhdg70gnq-KhPxavA_8ckgYPCBGiFyvn52OBSqPaixd85WqQt0LIDYxp3t7netbLOZx9vZIVTRii8obXVIFr_iv5seVPVFPAFQCpbml3VHgLLHQCrwyA97dojXNkP2oVW2rYKfWdiFuRbLdnulQocryauFCui2THjV-e1TuRlZKZNslMmIZSJDsdAQ6Qi5U_lchHtpPbeH4sPI5f3tICavmM1kVhwQrY2-87Ao3lpi2wY1a_fIvZotfa-hDKu1NM_FPuBGh5GZbUa09hQrjYwjbiyVYPhF46W_kvjfItiY9lvPgtOFcmJ9snh04mfZLeCB2NoQJes-_KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/30396" target="_blank">📅 09:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30395">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpFizNMN4LQ-yuUvftsggGkDTqxV2DnIeWBVoxeASimT0kI3sgSTbb6Wzx1ij2EQtVTcFzIHAfCNQcpjMzkedBKIsBkWuKmTW1J2vgwd8Nsa8xkeZEJDloVPN44aEBdeSTVZcsz3WQRLYBHAex49x-kDS46aedrjxxMyuGH_vf5GgkszmGUnLpCJpo2pb6edDF2sz34PGvnRagpKuQISDv2U3KuEw-Pp5Bp6EgqJg1xJOaFy2aKrcngIt7Rk9fRj80q8EhrZY5ereRXEfd4QZq9UnSFbXKFjpeosjl2qC8Cq9xCI6GLE7137O0obJaaWklCVYLfLWY-R12u-psIv6pl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da1f2ad337.mp4?token=hoQbFphHE7kniR6rp9heuY9FC-iBDYLRaGGqEbJtmadxciF2d8AlQiprwy6oM8q0fNz9g2cZObTU-Otw_inDFQiJFHNghPO-jUS4XqVg-IA6c44CtrsYsEO-t-8nFvqBeRCnXI0kM0gn8YEElza3jPeL1iSMRdoDpMRAsDiEf9xNFKqg1rnLpjD2m2voMSvJ1udD55u9kytgW8oJld5xuPwIxWuzmOdCSGxi1YvyL1NDUiWFnrPiMkbj5wLSxhqGs1imGYLi5l_eTO40OqABUF3nQ6bWKWrxY75Da4AiceFMU2nUKAKMbG1mEGlV4-DVsMnOgyf9jwDWuGEtLEWkpFizNMN4LQ-yuUvftsggGkDTqxV2DnIeWBVoxeASimT0kI3sgSTbb6Wzx1ij2EQtVTcFzIHAfCNQcpjMzkedBKIsBkWuKmTW1J2vgwd8Nsa8xkeZEJDloVPN44aEBdeSTVZcsz3WQRLYBHAex49x-kDS46aedrjxxMyuGH_vf5GgkszmGUnLpCJpo2pb6edDF2sz34PGvnRagpKuQISDv2U3KuEw-Pp5Bp6EgqJg1xJOaFy2aKrcngIt7Rk9fRj80q8EhrZY5ereRXEfd4QZq9UnSFbXKFjpeosjl2qC8Cq9xCI6GLE7137O0obJaaWklCVYLfLWY-R12u-psIv6pl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین‌گزارش نیما تاجیک خوش‌ صدا بعدِ جدایی از صداوسیما در بازی شب گذشته آلمان
🆚
هلند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/30395" target="_blank">📅 09:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30394">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4ATHqovkTTf-XbpXlltdNMme5E95UUalwQJcY_2xgv1n0HQXYU7ue1Btcbr-udOext5lzqtXkY2K-CKPQy-6lfXhGqA8sMeIfZkFkigMTiKZs8ml_SaCUyYZ8XFzKz6IYApLUMtEu54RKuUQhBHfz_I7IjE3vPoSg23OsYuaG8XbgNA7O_BgqV1eX8r0MkfROPVoK6c4FES3rbHE7RnZdPHl4FcGWFTsq9j4gUtdcK9FZaWXru8BBmMf-NtwGZTEJdBFX-XVclHWREYzSoXQhFr-qrdWPK8_vRROOGucjDRw4EZs2zDZ0Nnh8BzsoKvX8PJo2BRwiHLKYSTpgWgEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30394" target="_blank">📅 08:43 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30393">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCb2CsaErRkGTkpfc_woMBGqXnlNtNz8_JUQkaTjURUOQ5ukS9SBMTLWMR55mzcHKhAGFNDZzHTkuwhXN1hhIDaLNBPl_3PSQR7wv8PGpwG3AQOo9Y-O1xU86zvRt3NZL-U7BvFOElLbG5l6v_GddSboOur5lcPZDLetxCPMBmbSlL9eXee5TayRXSKQj50Yz7HCP2RvYLPEp7HZtcnqDGoY6PMm4TVqnrfNWoayejJBQ0aDlruZrQhm5LvtLe5vS_EsCoU-zeiDE4Vt4XVWRyxPVNkufffFy2Wzzp1FvrJC7TcLrVqKbzAMVcegXpkMfVqKS0Hts41n4nh4Yg-Izw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ جالبه بدونید ازبکستان بعد از 6 بازی و 5 ماه بالاخره طعم پیروزی در یک مسابقه رو چشید. این‌بازی‌های‌دوستانه تاثیر زیادی رورنکینگ بندی فیفا داره. باتوجه به برد قاطع‌کره و ژاپن‌به‌احتمال فراوان در رنکینگ جدید چند پله سقوط خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30393" target="_blank">📅 01:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30392">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=PRNVCF1p-abuqvO3V0vs6WZ4wUhbFB7JGYAUeQzc_oiWbJ2xzYQjNH0KJfCC8bhtRzn_mj5fH0w67rNOQCJs27hS394KvBa1CTBkYxTCq-42JTP8aEqh7JdVQSor84pg22X06xUBrDwkSoXRU97xVKYT7gpeR2P4uYbpZis0zZubBS7gQeleVLyJfcsF2iBVCf4Ta4L_kya_Mk3q7xsz1YxofUW9pPmRyWTmWWtvGG2PUE_m7bFl1xvJT5CtfIu-fP3De7b07sRMW5lJDDLtgjy6lBiWY51xdvTgJEFAr31jssOkUYYHimi8EsvCs-f72GaouvYnan2Y63H9MLrmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57e45f06f2.mp4?token=PRNVCF1p-abuqvO3V0vs6WZ4wUhbFB7JGYAUeQzc_oiWbJ2xzYQjNH0KJfCC8bhtRzn_mj5fH0w67rNOQCJs27hS394KvBa1CTBkYxTCq-42JTP8aEqh7JdVQSor84pg22X06xUBrDwkSoXRU97xVKYT7gpeR2P4uYbpZis0zZubBS7gQeleVLyJfcsF2iBVCf4Ta4L_kya_Mk3q7xsz1YxofUW9pPmRyWTmWWtvGG2PUE_m7bFl1xvJT5CtfIu-fP3De7b07sRMW5lJDDLtgjy6lBiWY51xdvTgJEFAr31jssOkUYYHimi8EsvCs-f72GaouvYnan2Y63H9MLrmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌از سوتی‌‌های عجیب‌وغریب پیرمرد های تیم ملی در بازی روز گذشته مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30392" target="_blank">📅 01:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30390">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIqr4Ckl2ESjKyyv7cpN4bleTgPtnsGB5xHaRIvOfphbHVrbbwKCxlunl_Jq2h29LC20eanDFvii5xgc8iGAhDkiLvWvmhhOQxpZUQOnoK-NcTNYzM5Wl6qVwvilpmYZhIlHsvZYAujVVMJNb0qsLo_KOPAVyDspbKRH1ZlmfyuNEsvULB6Z8lN_nKjU1IsR2OhOZ5MvnamctmzQFGqgtvAIlFBpQRa9-sjo3AHSCE0PCCK8IhEg5UbtLnp3g2lzuirH_MMgByoeqA0Tu6A8ombyhEkamWdsVQ-_P_0C9CV3laWiniesCLbHyUIjU6rIiAV-26EnrPZDP5iuxGBI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ ازبازگشت زیدان به عرصه مربیگری تا نبردخانگی لاجوردی‌پوشان با یاران کوین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30390" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30389">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fe9dfFf4wJdebA6Z43fe1TMAWLD2gW_bGfLK2HabYxS7LUzBmrRvyxYePuykIoAP_F7My00NzTQBnX2nG1zfRmasBGgMSAmCiHEUPN7tCm_VCfnR-xjuwvM7NNdYAMe0pFRmw9zub-jLe-SYrynURAtSR2P3HIvax2ykHE3X-f-Z_LQCyLnf2o-3OWI652gofR0sbVlGBkxbkjqB4DxLRZe6YqinUpiU_DqFzy4lzc2xfMtWE6Xb8mdJoNQKClI931kGfHnkiub0QXJkjliOcSOd_A_MFgZGsgjsYZgk4cDpe1fd6Rdn739cd_-hpSTkaQr4Sh-5x8q-F73YiLd5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
ازتقسیم‌امتیازات در تقابل هلند و آلمان تا برد سه‌گله ژاپن و کره جنوبی در شب شکست سه‌گله شاگردان امیر قلعه‌نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30389" target="_blank">📅 01:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30387">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDQ6bdr0SW9rTzRf6qIrD-FLVEYZvOJVxdb1xB3q8U7PXplFbkuMGGp9EmsnTAZFvBD83lm_C8UQliTdG5UCkesDeDDTYo1O1I6v9Ube2BuArQAqfa5idHdonH1pnq9tVPSm1XzV4bGIcrlvUec_OMIPEQ507ZzXJpUptKDmtV9J7IhcMInaOjP3mGE2qj31GxBvb-P23m2fsDNa50eHGoQLHI_zdKkfmW8-LljfSfbcqJkqeYh4VYYV4qA8Vg6jjOiMJnIBtQRXg0BsGJOHWF71-hGGZZVqfqZebayo6jd2GKFiWBNpeZofXqwOjoJB_4SKVsUhFX41poQazVz3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق‌شنیده‌های رسانه پرشیانا؛ دو ایجنت نزدیک به علی تاجرنیا رئیس هیات مدیره تیم استقلال از صبح امروز تماس‌های خود را با مامه تیام ستاره 33 ساله سابق آبی‌ها آغازکرده‌‌اند تا در صورت عدم موافقت فابیو آبرئو برای‌اومدن‌به‌ایران بلافاصله مامه تیام رو…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30387" target="_blank">📅 00:46 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30386">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9hfZKfEOTZKrUuy9TCL-2tTES4HzttqabIwhL9wWDl9vgEu1v-7Vu9bMP7tX75fx3r_16_NlPfizP8qITN5kNWpWxdHbqkmyvKZCsHnmdvhW6swmg4LF57rDYZyMHBo9bv1AVxbDpi9YJouyhni_pJdkp7e_QO_yHSf4-Fg5tjJxHE7lh-ZviMrk7Jn8QUIZ0pv3fuR9S1caq9tFlMlaUMN8XnpU8ReLSJ3JjxvIfljD8XAq5SyYYMI_zzrjJO8enJkVc0Ly6bm9dyzRtyPLsdrnviyeR21m2xLmAT7K_JHgYNjJtrfw3piom0gqh3pyQbBTJCb0qhYYaIw86HTJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30386" target="_blank">📅 00:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30385">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy06ro-lXNhRu_5K0TrEMpnpregSdnUbPuNWy2-VdDPborG1kKasbBh_GheFkze8aQ7ZumW2F1YXSrA9UyCrdDVIF0436cvjuiGQglCMjW0Iq51Wai47XYIYrmZAXaWIoUtEPVEFhyjxmrA48FneHHedjuJxXXIPPsys_8zMPMsfhiiuUPUa2yPoWtFj3MdNqvbG11n3k7DIfZXZ9KUQ_2Do6yFxyiIQeG8l-Mn6ZZlyChHhEXXAm2XUX5afCB_wh0foEIPcmXrZRyZRFY7LLMeASBSO9f_dmpAHd-3iIOfO1OO6uXEkpMz-UChQU7n3aZ3DtMSQTYfHmiX-tbvKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
گلزنی‌تماشایی‌کریستیانو رونالدو 41 ساله در بازی امشب پرتغال مقابل ولز در لیگ ملت‌های اروپا؛ این980 امین گل کل دوران حرفه‌ای رونالدو بود. البته دقایقی بعد این گل توسط VAR رد شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30385" target="_blank">📅 00:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30384">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN_d7qENt4y5AfPsG-3W0BIuqa4TfDkE3fNm0pBVbEWP8tMKIxM4gqoGWzDwTkxZxctzwn2EhWY4K-Zh1ej48sGSkw2EJijs6j8tv5jKy2UI1xEtKkLBLpqRXVNeCASKYZyaTpqxtoE2PCnF_JMmphfz3IlGBtNztg-HIxX8LHx5AVzId0G69VAVjK_hywj8wnBDFZ7qmbHR_ilwC0vuIDkxlZHiPFzWgn8lKQPKGQVP5LSEhI2bofIxK_lQb-JbfeP5uV3sKeH5PlHrWM9ZBvcN61t9RwRI8BA9tFFBZwZ9UOMAZk4xHq6JI_49aGTrgfq178oLrT1HoWZF8Qsu7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دو لیست‌متفاوت از تیم‌ملی؛ لیست محبوب امیر قلعه نویی
🆚
لیست‌سیاه‌امیر قلعه‌نویی رو میبینید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30384" target="_blank">📅 00:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30383">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-8cz8IrY2AFo6zGuNqLEwHHIIddAAUCv4YggfFnkkTWWGqnlSRuI3w-hBKRAHKyX9ylrLxXKMLv657Nn9jp8fDDYWxIrlvPDRqPz1WKX7jClIHF4TcdwOKBp_T4Ln-dS3WGTM8S-G4JAh-LvaJ-eHu3VMsO-d9-usomS9tsQWxRPozU1e9rv1RCNmtXSi2x5DOOZTTx1zRiR1ifmdW74Oibn6Hrtzi5VMRNEN5Ue6bBtmiVTBCvIcIwwqLgFq_WxhD3_aVm9RCLuEki4gmpnZW7777ptaVFfXJs5THuHwX8BDAa7PGiHl2YhnfZG6orDghUZCwLLFHk7uR03Dw-EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30383" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30381">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=vg83aN2sn-jiSQKvDFD9slP3OxATLxAPA3f4x-YUpiKghACp5d-Xrafr9FpWq9buW9UrucobLLg8-cjTBFgTFQmxyu7vwyKZ2VpXWsDWR5iKCcpW1oYXzs_8MhMUo-2SBTXwhU-8C8tlsE1Y20_BgW5qGd_2El5K9x05bIxkb_gIbwSCpcw36lDy2nNlcRA7cW8_c-y_9aOPOSzBhwe4j-MVdOIASXI7Okp04AMDBatQVMUavYeK1P9Cd--4bMejSv_l8zNz_NQpaRWiNB3P-DEyTlNISaNR3-GBdp0i5GqbaWU7JJsJfPj4mOZc2XX7vNZ6zC777esciFzNJRg-Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56e908efe.mp4?token=vg83aN2sn-jiSQKvDFD9slP3OxATLxAPA3f4x-YUpiKghACp5d-Xrafr9FpWq9buW9UrucobLLg8-cjTBFgTFQmxyu7vwyKZ2VpXWsDWR5iKCcpW1oYXzs_8MhMUo-2SBTXwhU-8C8tlsE1Y20_BgW5qGd_2El5K9x05bIxkb_gIbwSCpcw36lDy2nNlcRA7cW8_c-y_9aOPOSzBhwe4j-MVdOIASXI7Okp04AMDBatQVMUavYeK1P9Cd--4bMejSv_l8zNz_NQpaRWiNB3P-DEyTlNISaNR3-GBdp0i5GqbaWU7JJsJfPj4mOZc2XX7vNZ6zC777esciFzNJRg-Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30381" target="_blank">📅 23:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30380">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpa7eu2OgfVQcLJqtRECNk2rsQTnBRLWx33-_5tkN8zaaNK1hBjTIuoEagUiZ1ayXAqeFUbok12NTbZ30w3ZFSQUXGApehXZ-pDCJ5CXr4T639JGuPYAX-bvWtQkETxcfVyxHKZN6NavGmqRBA3nqW70BnBGbIXKNtYX4GzdaYDrewBtxOubNM9j3H2hiTEI-RWddOEPpZbocXXu-hTpJmpP2uApqWpSQNf05Kd5STn5saigsvBfFFLKxKreKPlJHS4AaTeRiYNyQ08P1ZCNRRxJODrkbhl69x9Z-C3azMuavhfM_sGVEAE4a5Wd-Q8xfDDfFN5_kQ-tb00MVem5SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ابراهیم کوناته مدافع میانی رئال مادرید از ناحیه رباط زانوی دچار مصدومیت شده و ممکنه چند هفته روبه دلیل مصدومیت از دست بده. مدافعان تیم رئال مادرید در حال حاضر: هویسن، آسنسیو و رودیگر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30380" target="_blank">📅 23:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30379">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luKTsTtQVlNvHCQqH2V-qAB1jhglkwmC7akW9XkaPeIiPOth_3TPNRLw7vWrlBGdG4lo53YXgjiXWx94rH3rTjhT8T5Jvgnkf688wTmk3NP6hyzSXSQoTVQAO53SYbvZsUovb9thGuuCORGjDkDWrC5KNGbQuV8mOy2IN6RDwrx-wev3I13R1Lyqy3Z9xXHP2Dtf6SLpUoKpZnutmHfgG5VrlV2jtDIBM2MTOvysJ3d3nTociVxtuvDpJRF6aIt17h4H9v1Kgudy5BKXiQuE3-Cj9wKFJtyU2ezJKC63AdtkD8A8xVNT8tGBTgt-L6K3lcRiztQR6wTSJ0CousMNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
اختلاف برگ ریزون دستمزد مردان و زنان در مستطیل سبز؛ دستمزد کریس رونالدو در النصر 142 برابر بیشتر از گرانقیمت ترین بازیکن دز لیگ بانوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30379" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30378">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSIeKFJr4BxDIWM2UkEolMYmTJlNBZkmAx7UadvTR3gidWjvzQLPjTzWGcygq1dkquf4IMdsVVv7IClPhPI5mZauq9zON4HuF6vL-SJrGlniGdRHZx1271tTwgJRoOOOG5NsyrWOJ-C8IoeJNKK72uONDUz7nF6-G9vW-YRiVZInjw7KU-e6LTxjbO9rgfo74d9Z1MjvK804v7On46r4SpgGgeVkdTqBO_YB9rn8gx5Q894ZB-9HU8POpaa9GVAVptk6z0rghdq_npSspdSyXWkSflwSA8vI3uYyxc7Qvw5v0135Z8R4HvupvtldLA4EutfiNbM7V7dQKGqMG6nt2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30378" target="_blank">📅 22:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30377">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LXlF1Y0MN-8f2hXfDq6fSH6pbpN9_V9w0MLegq906rUAnPeZX-mDhxc-WvAUMMhj1cshwZ8RnevfMydzN9TFAZNIy5LiKXSJinN0Rn38N3OfCJ9100UJ416all0527nx8MquRqVxk-U0HUXDqvTD9t28setvZKbtKexrZYD5bJiGQtquOGuQLjNwdnjtT_disfkfutTZFM1qX4RUCjFjY_opTMk1cqh3M9bYFFYODdEOp2t5X7wSFSd19e50pVRhEpWuum1DHQI-D6anWqaMf8q6vYhq1VMcaxZtzElsxFvlayeAUNVCZE0oY0X9gmem1cAKDCMOWnPbXT-FJDs-JFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af2ff5c23.mp4?token=FB3pFNKYRx86oU2haMu-wIGzvJnI9oWiex0GYBxFpMsu5rQAkkKqKFpTQuYK7Q1pHh09z6auiSDkk6Ebe30YSMslNiXQL7KfskcpBJe5oWpneEH45sG-sfjDppdW7G7KKW2bIYW-LNOnmKArVhRA0OTJSqcJMZkANdzgPhZashKT3O6lC2A-dGlhYW3Scih1q9cv95DZPLgP27c0YnpbZf_gwMMbmpXNLyh_jUl6p3v2v_PmDAeAdZi0iIX5GYlA8JHZfQDjr7DMwbsz080bxtvRGJiNanfVMmX9L4N3xlf4QHJeq1tHEK3FjYdJftiSM0A6MTboD8lAv2-I2Z65LXlF1Y0MN-8f2hXfDq6fSH6pbpN9_V9w0MLegq906rUAnPeZX-mDhxc-WvAUMMhj1cshwZ8RnevfMydzN9TFAZNIy5LiKXSJinN0Rn38N3OfCJ9100UJ416all0527nx8MquRqVxk-U0HUXDqvTD9t28setvZKbtKexrZYD5bJiGQtquOGuQLjNwdnjtT_disfkfutTZFM1qX4RUCjFjY_opTMk1cqh3M9bYFFYODdEOp2t5X7wSFSd19e50pVRhEpWuum1DHQI-D6anWqaMf8q6vYhq1VMcaxZtzElsxFvlayeAUNVCZE0oY0X9gmem1cAKDCMOWnPbXT-FJDs-JFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌برزیل‌فردا دراسترالیا به مصاف تیم ملی این کشور میشه‌. حالا اعضای این تیم به محض ورود به کشور استرالیا بااین‌استقبال میزبان رو به رو شدند. همشون زدن زیر خنده‌. قیافه آنجلوتی رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30377" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlYDU1d620rF3t-1-TKywD_vsw-03StIgzqb3w1FXxa3g844AYDuyJzUTSGVxmX0t9V-g64PqGdq3RCyDy6EJ5PpTIRjscFX3QeKdcC-ZgbGR3l0iF-BTvY-SPKsFJJNOAjWF29Q-rVpckFeHYLEH_54F-CcWBwrpoUB-uhXhfuMYoWTVcMVqyM8zQGmoVzHN_IpMxphpoQGGSx5BnTIpOp2qjo1yzmCqZkg1U-rE7Oc0a3ipueUMMQQUTztMapTXqXvXBztCeQuwhs9Fy_4yhlQ6bjeKtbZKzmuXnY11Wad0UaEkZUBNNmiZPdMef5HGm50jOXx5RsSBYP1GVROOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtWLF7WGJDUxhTHuwi9XUOfvpuVMHnajN7pXXZvdNOZ9HtkksWRxJj5mUDjsTg4ZTghbWIV4GrmE2rO3wv3Zu8bR--FapRe8yo3w677FmdyKFqLgpoQ3391fmKJOElivMn-vy8lKQCz1Pez2qVFDWejcvCfCvIigGHkH-z085B3OWhCt3g46LG3787AyXwoTWHe5ULJ5Vt2bE6nSAHGS1dUeMwQ_goRv2unc5WLTKyGgJK4eYz9ScuW4ZYHbdhQ4m_Oc3FoolSxTQqMmQVa069lf52V66vjsVo4-Vw1OsO6pTVZSBUEUQeWWkbqFhMqx6GWOOtTJRpHs3agb9M5cSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته اول لیگ ملت‌های اروپا؛ ترکیب تیم ملی پرتغال برای دیدار با ولز با حضور رونالدو؛ 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30375" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwc6frSPrTV-ukV-3x-13MzM9VEsPQna0bbu9plMexGCR3WpJEPJAP2J2wJosr1Ts-C61EudpFUWawp7oR071pAdiqoQjsrmDO4-a6VR2cSqkEGIhS8jQ2esbFYtXe1LFHj7dt0DvGVakjuRl6tqpekGviFle6Q6amIM2uy0dwcyG9oRwgu2v22IFK3duYVSleSeV7EP2ifSlxtSOvX1V1oBmxkJ_wysEkWDRCDYEV3atxnIQ0O7silmlLQxf_MBriEluOtyR6doYL4YMQMv4drVsXIxmiJ2R6S34Opm6gb8DA0nUC5kMtMgTtTooYfkFzY1eVZTMnkEpzqNSdMjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گزینه اول باشگاه استقلال برای تقویت خط‌حمله‌آبی‌ها فابیو آبرئو33ساله است اما درصورت عدم‌موافقت فابیوبرای‌اومدن به ایران در این شرایط خاص؛ گزینه‌مدیریت‌مامه تیام است که‌رابطه نزدیکی با حمید مریخ ایجنت یاسر آسانی نیز داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30374" target="_blank">📅 21:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG9l9J6y5RgkxvEsIPc3DG61CGNci8vRMDj1e6oqd6KMZrtLB7ohPiVpQGft9Mxmr9gDJpbVQIDvgUww50Z_kvnn9uI78XYxSCsvX32c4bxWgjcwKNgVz3L7l7P3qJrN-TAniunop7Hynlevh3Q0kfXS0ZNlDkBO9xiMArvkNy2MuWOcTdsERJ8HCCJXMpO6j_NZQefuqOJ7jKQo-qI1tDqHnxl0wqRISXX_JfI7BoqpFcheA62i36mYXFdvPhglbVr26rYFywXGCkcKl1Iu7IacH24P5DK7ZSeqM8qPkHYTyZVfJJsePvTUzy-zrM9emP6RHkd6HgZpGUihFmS7rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جذاب‌ترین‌مسابقات‌ملی دراین فیفادی؛ به هیچ عنوان این هشت مسابقه دیدنی رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30373" target="_blank">📅 21:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🏀
پرتاب‌های دیدنی مژده نظری ستاره تیم بستکبال بانوان ایران؛ با دوستاش شرط بست 200 دلار برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30372" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
صحبت‌های تند جواد خیابانی علیه کادر فنی تیم ملی بعد از شکست عجیب مقابل تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30371" target="_blank">📅 21:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‼️
گل‌های تیم ملی ازبکستان در بازی امشب مقابل تیم‌ایران به این شکل زده شد؛
گل اول روی پاس گل دیدنی احسان‌ حاج‌صفی37ساله، گل‌دوم پنالتی دادن بیرانوند34ساله، گل سوم فضای خالی شجاع خلیل زاده 37 ساله به بازیکنان تیم ملی ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30370" target="_blank">📅 20:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30369">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDLg6grbCo9_UZApCTwCWnUCO5HSjsXoPoi4A-RD-e0DQV4XOAWr-ZGpn7hy49kvjZfPDSuUshE0VsAv71OTco6R_IpPhFB9QAnpCUbg9stxmc66pbPw6gO_xXu3rLNiuR5SaqzkN1MU52OWbAiIn2U9pf67qqIykoAyG37MeWpaYHJCHL6MeB34zpCA5MVSgra9--BZwhvOCubQBq09ttJpMkvzskP8e5DHyXZfEVDvLtuayLsPOQLMSs_HUz0tFgij99M-SsGHEEkj6sUxrUBIrxMa5D39Rctv0l_IOgLU75vua8Jmt3PW3PqgS2MMf-VL8dgTAuEKdPLYFZLMkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در روز پیروزی ژاپن و کره مقابل حریفان خود؛ شاگردان قلعه سه تا از ازبکستان خوردند. این نتایج بازی‌های دوستانه تاثیر زیادی رو رنکینگ بندی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30369" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30368" target="_blank">📅 19:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llvhhQub6LEN-e8v8-ENEqAI34IaEXbt3mDh5rBCrB5Vah7TVRG_wqF1Ocj2jAx8hiUe9iNg7Snq8Z_NazW8-7Wj59kdfogfcplILnUOuUJKL65vl_1qYW5VcbDt95ccfMsqGk7rH4Q8YGO1HP28DA18DHRWMANqkUnmE_3FOkMSUJ4k8LS6abhs3R0sySW4wz3ktadac5WlyA9KuyOUe7I4aRa3ywUXT8-IbGRCylXQJr_hNpGyaabTpoP8YNsk2SCqEUSuBqarRsTbEXvDyCGUP8u9dcP_D1mEm0VFqLMDmIYAxACdCp1BtAQvc3wjzHycfvMrTHbwvshM0nJVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
پوسترفدراسیون‌فوتبال ازبکستان بعداز پیروزی قاطع تیم ملی این کشور مقابل شاگردان قلعه نویی؛ پیروزی مقابل ازبک‌ها به حسرت تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30367" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EM_fYMPmNyhWOAajCtRlkDr0S8CC4eaWxSHqarKlRGQa0SZIn6mUNBhaJ6PdpngxJDCs6t9KbBUbckvfoVEndwD1VO6a0__HUGfzQR5rY0Fs7_SnIcFSJgc9jMS82RHZ_TYV1fCGbfWtE-umHE9AIjxDpNERYTmQ-VqKKxQeUOCnyodn-iAwv-t_KNbpk7wuUnGHL2ryw4Rryy77WWrqMP7M44gqAf3oXplebCzqDRFi7_seWKYJz4lP_8T3rg0l4ahWt4XAftLzLNNccoOAnv6BUYeYybyZbmavJWiFi-hBHjIjlFl2TJ4AWEoqFoB5zZvNJIL7WTyWbDns_0sbDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇺🇾
نشریه اسپورت: مصدومیت مچ پای فده والورده تشدید پیدا کرده و او 8 هفته دور از میادینه. بدین ترتیب دیدار حساس با بارسا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30366" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30364">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkPezIBgXWVxWe8p9yF_8Lv_XHfxtqIGjxtXZYIH9l0nSOYB8YrXOeBsFJG1zyZWpHk_pMwo0Zbu6mg15kutOHFB-kHycH3VPdHObMwCX9h7d-XwFXntNkzcdchYqS164T_olSH2eXuWkVxl2QxN_slVnoQhzxZEu49pYHNEY8cqs59ojO3RYKxKNXIgjJ6yJFuYd1vVNa1eSkerR0inTPCuJphHn-ydcGDGB7CcrajesLoC72rphMWDX721iQMV-d25Kad1_gKp6I8-szJ9o6ozXMnrg5ycSXnZeqJlQ86ClFZ7KHF6JkQGOReS3jCQP5zvCunxtgjcUdciQuxomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
حسرت ژنرال در پیروزی برابر ازبک‌ها؛ گل سوم ازبکستان به ایران توسط نورچائف در دقیقه 95
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30364" target="_blank">📅 19:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30363">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=Dcc1byb8VfzzK5qeNqD4UEQew99-3EjgBZwWaFai0kSa5yvFOLqZIug3x9hcB_M8H2PXsZEUqqiNbIbBilHrO2gc9OJHEYgbQBdhqWpOgozx8oO4KIyfHyfDA49m-IoML9buBfeF-Qt0qbHrvAqupoSrg5xKq6wC9xNR3JpS4DGoWU0UoWxvNjeJTh16mkIfrACtr1hY-bSPFEnSigNbVQWd8dCs2EwHpS18zWjSEp58phQKKUV2nth-ZlZcA-jJFu8wVY8PpKg3AqPhDb1ryVAC248R9PgpeOpOQws6G1Ky5rWTscX6E61Or1gbpOXSmCjrWti8TPsDADlHG6IQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb08c9fd45.mp4?token=Dcc1byb8VfzzK5qeNqD4UEQew99-3EjgBZwWaFai0kSa5yvFOLqZIug3x9hcB_M8H2PXsZEUqqiNbIbBilHrO2gc9OJHEYgbQBdhqWpOgozx8oO4KIyfHyfDA49m-IoML9buBfeF-Qt0qbHrvAqupoSrg5xKq6wC9xNR3JpS4DGoWU0UoWxvNjeJTh16mkIfrACtr1hY-bSPFEnSigNbVQWd8dCs2EwHpS18zWjSEp58phQKKUV2nth-ZlZcA-jJFu8wVY8PpKg3AqPhDb1ryVAC248R9PgpeOpOQws6G1Ky5rWTscX6E61Or1gbpOXSmCjrWti8TPsDADlHG6IQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
🇺🇿
شاگردان قلعه نویی دومی رو خوردند؛ گل دوم ایران به ازبکستان شومورودوف در دقیقه 58
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30363" target="_blank">📅 19:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30362">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eved6mBL14oVBD_mFkMwAw8n6EJJ-Mjb74PgoESQE_Ayu-76-4XcRMRCInJ7h6UBUHe8m4adg5q2fPzg4MsJq53xvSh3a5AYJtfJ5wueFEig6wH73YQQ1E9gAqAUlukHIDEl1PP2k0l3osSZ2q9EUB5em8kljBhFuMjyUC2uWx2kpwRl2fNen7i5TtB9Rv39UPrXyG5WozjnoE3s8q58xRLCoxsgMtYsjqJIDA_Iv_WcfeKSHxDesxMwGjGaQYWYsd3rdVxevoeRcZvBY4e9zPK2V-KoNy076Pik43ihNApJVKK59PHKhKLu1hnnVpDxms12L8ljnDuooYIg-AtXEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
🔵
آیتک سلامت و یگانه اکبری با عقد قرار دادی یک ساله به تیم‌والیبال‌بانوان‌باشگاه استقلال پیوستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30362" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30361">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401621b710.mp4?token=FbatSvuJpGW6hAOFIul7FnvyNm-z2wyZd1Hlo3Syq_aMZE8VVJOpBbtclLjB0l3qkKZeWd5OOt5Ha76WXXqQDEmk1etXWhzhaucGBvi09Vqux49C4yb3nFlrI1O9UhlnDXUFJwB_-87Rwyd1JwQuL8k0UpbqPlGiRlUFv8JwtmugiSvNeHiqUD3avgxgCPIjj_5Zl7DcO0GF770UeUHwXe-qPepfIIkuAolTaRiLCllINWVMpjt_bYWFpSRfi4JhKV8fUOgpwC9aAHHGsniOFcIE59y14yRwKOR6394pDbh2SMETBe_3iGBmvABTPXM0JNNbdT508MNOeLo2ur0S7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401621b710.mp4?token=FbatSvuJpGW6hAOFIul7FnvyNm-z2wyZd1Hlo3Syq_aMZE8VVJOpBbtclLjB0l3qkKZeWd5OOt5Ha76WXXqQDEmk1etXWhzhaucGBvi09Vqux49C4yb3nFlrI1O9UhlnDXUFJwB_-87Rwyd1JwQuL8k0UpbqPlGiRlUFv8JwtmugiSvNeHiqUD3avgxgCPIjj_5Zl7DcO0GF770UeUHwXe-qPepfIIkuAolTaRiLCllINWVMpjt_bYWFpSRfi4JhKV8fUOgpwC9aAHHGsniOFcIE59y14yRwKOR6394pDbh2SMETBe_3iGBmvABTPXM0JNNbdT508MNOeLo2ur0S7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
کاشته دیدنی ستاره 36 ساله ایران؛ گل اول تیم ملی ایران به ازبکستان توسط رامین رضاییان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30361" target="_blank">📅 18:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30360">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=B0KdLZOtOcpeeAwdPoWbgV94hzSrvWFq2ovju68I-IsIACHoiNCYaDQ6kOPQg09laVjcNbEKBsmPMGssWfakHrB7hNNBYqj1PtC6NGKRgxqlVvo5dVyz8DJ-OAQaJ0mZ84i1iYEHSb5FxazULmdyjlKLTH57P3FeWa2-cSHJZaXrHH2mYMzuUcBO2f-u2SIDactIViWPPRrpvi8_g1UGygsaq9O82FrVcGMLl2E1yl9w3nG7wWu79Q38U5pmqoT_S2ddYyIAK3Noe8ddFzyZfP35-c34N3x8qKz_gLNGfqg1g7APgvvL30Nw9N8mmzUZg8Dqo-pbtyXRwxcuNRtqhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b255c08c.mp4?token=B0KdLZOtOcpeeAwdPoWbgV94hzSrvWFq2ovju68I-IsIACHoiNCYaDQ6kOPQg09laVjcNbEKBsmPMGssWfakHrB7hNNBYqj1PtC6NGKRgxqlVvo5dVyz8DJ-OAQaJ0mZ84i1iYEHSb5FxazULmdyjlKLTH57P3FeWa2-cSHJZaXrHH2mYMzuUcBO2f-u2SIDactIViWPPRrpvi8_g1UGygsaq9O82FrVcGMLl2E1yl9w3nG7wWu79Q38U5pmqoT_S2ddYyIAK3Noe8ddFzyZfP35-c34N3x8qKz_gLNGfqg1g7APgvvL30Nw9N8mmzUZg8Dqo-pbtyXRwxcuNRtqhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30360" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30359">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StF9Lwql4D2kU1hWScGOjl8jhWMgVO4AnYOjGcjzfqebGKIC0zNOerYtVGkdgouQhbb1To__NZFQi84b-B6hthEg_CFqhyJrns_wMR3nAAhYCKPA8HNz4r_F9SBizP_SHRamjLo_jZhouMooy5BLPPRPsUhkdNV7SyvYDeF5_nQB49AsgVhtFb_EBbEjvPLcwqgmb6uB3tYweSznXtC3NkZI7QQRGwhkg0v24QvPi9_9YEPCYgs7qrI6HuvQspSEU9L6A94v8QmitoFf3DgdJH4j-KllaI4sboBFEOoC9UIqXuyd8yZ3ZHHw3-3zYt_aEIXhdJc_9T2InK7uaqJtqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
شاگردان امیرقلعه‌نویی اولی روخوردند؛ گل اول ازبکستان به ایران  توسط شومورودوف در دقیقه 10
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30359" target="_blank">📅 18:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=NZTtuley-a1Xe1aAJlFa-0d9QzhOrQgV_C2FPeobZc0P0pLWamgaiek_Fuj3v3usfS_TmnqqyzOHkfMr85FScA1h65VRFml6U5PHvdWHN_gm3l0DbE5GcR1kHzxuGVG8cmVRhUwsUy__DDjG-iwDJcUfktCc9ZofQLQh0JmbRVI9EqMYWHI9mPm00FXf78c-dFUosFWufP4ZkTvolljY3UHqSrthaVSIVcIeSO87XluzPOW9ghANqdwgAfIXHis6rMcbdIKu76V-2Sn_u2t7Af9p71tykC_qqdT9iHK6aEpHOLedgFvB0garz6HibG4TCth-PEQtL0FXybniUCgsHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1995a5be8a.mp4?token=NZTtuley-a1Xe1aAJlFa-0d9QzhOrQgV_C2FPeobZc0P0pLWamgaiek_Fuj3v3usfS_TmnqqyzOHkfMr85FScA1h65VRFml6U5PHvdWHN_gm3l0DbE5GcR1kHzxuGVG8cmVRhUwsUy__DDjG-iwDJcUfktCc9ZofQLQh0JmbRVI9EqMYWHI9mPm00FXf78c-dFUosFWufP4ZkTvolljY3UHqSrthaVSIVcIeSO87XluzPOW9ghANqdwgAfIXHis6rMcbdIKu76V-2Sn_u2t7Af9p71tykC_qqdT9iHK6aEpHOLedgFvB0garz6HibG4TCth-PEQtL0FXybniUCgsHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30358" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=Id01VbwfcCaBgb15FGVPpZ2oCu4ZFqtGKBizPbE-msUOfdpRfboPgd_DdArwGdnzyyJagRKOWPar4ww1foG8hIrIxR1GQ-j01vvOGtUA9dpimTX9DX70sqEbrYg3e3Cgp7lG1ZRy2gI7vAahLzcYJ4_VJDRyugwJTamt1cASi9TC9uRzX5gYtCgtNwjlW8NaOq6i-QWFLtxZERexJCSdby6OPKwWNxvKS4HsKkg6mhg3wt6RR49limlq6WQn1T_c6cgTt2-wEhuZoo8MV7887PCg0mjb8VwB2HUVhYOqsGz3g4Meo2HVACjs5WNPY_LTavpe_U6aIOY4KcFflYCSgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3181370a.mp4?token=Id01VbwfcCaBgb15FGVPpZ2oCu4ZFqtGKBizPbE-msUOfdpRfboPgd_DdArwGdnzyyJagRKOWPar4ww1foG8hIrIxR1GQ-j01vvOGtUA9dpimTX9DX70sqEbrYg3e3Cgp7lG1ZRy2gI7vAahLzcYJ4_VJDRyugwJTamt1cASi9TC9uRzX5gYtCgtNwjlW8NaOq6i-QWFLtxZERexJCSdby6OPKwWNxvKS4HsKkg6mhg3wt6RR49limlq6WQn1T_c6cgTt2-wEhuZoo8MV7887PCg0mjb8VwB2HUVhYOqsGz3g4Meo2HVACjs5WNPY_LTavpe_U6aIOY4KcFflYCSgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوخی‌های‌ بامزه عادل‌ فردوسی‌پور با لهجه های مختلف اللهیارصیادمنش‌فوق‌ستاره‌ایرانی لخ پوزنان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30357" target="_blank">📅 16:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9QG663NvjmYx_ff-UdgD09h94OVRSa_LyEWpRsFCnY-7-y8rZoqlYXcF2fQuy6o5BNwiM7r--EwZCgkVv3E4RtGaVPzgS6VS7tE8UYp3poy8bbIuw4cW2j33DzN5WrOtyTdIgln7GU4IAlJ98HIVVW0JkG4RkpCa7eXAIcX_bquGu6zenBsv8oCMnPOPsLp5WNpBvo49QYiCFyTKxGLtaE2OfDgS6gmLXlsU2L7Ztkb-yY3gg6IVcPJt5wrk86_Exa_3VvsVFg1EhNYqMFiAQg9_vrZLSBnlmcsuQ2pJWXrehCgmRXXkEtnWc7AAuOTwic1jnL8rRY_YRYl8mplmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال قصدداره که برای پایان دادن به حواشی پیوستن بیرانوند به‌این‌تیم؛ قرارداد حبیب فرعباسی گلر28ساله خود را در نیم فصل به مدت دو فصل دیگرتمدیدکند. محمد خلیفه دیگر دروازه‌بان 22 ساله نیم فصل به جمع آبی‌ها باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30356" target="_blank">📅 16:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmuTZr1PdJEGPMjujVpGC8JGHGH7NVefW8PWxrsidGzv-rQR1lRdE7krlGKj_tYSempAWgc6FESWbX3gzKAmQextj5kNL3nm_49_ZFU3hCZnZ0OjUYVEuHYxx79JKcDpTNkInI6MtFCGRNTgijxgzSkdWXEVHh2lz8c4R8dVbXCRyVSftGSZN5FraEEwN6Ut5HWljyJqX1ajeTnm2osqXSWfQnbxDu5eTkHcPAHjSz4P26ddO9lAEgfOSg-WPdzRmVI36Jnl-HbTNGXYJ0yTOGseCXfxNKyzAC7C0hZY0fXynHrquWkVYod7mNHGs9bStCMDGn6jpA0gr5mGVHCU3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دیدار تدارکاتی؛ ترکیب تیم ملی ایران برای دیدار مقابل ازبکستان؛ ساعت 17:30 از پرشیانا اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30355" target="_blank">📅 16:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30354">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=ULuMS1sgy96bjRp8rZ2VkMlW8Hai3eLbnC4N4gxmieFsIRWRnA-Uemc1J7B3mDkHhL_IJdqQra1VA7To1YtWUImFeIwKuesgACgw83_7fomEMC--6vdHc8j9KFerQAovv-7k32qg4CJTOAZhNAhqujOpv47NEn_Q_p9HMbTmBlDb1pjTztBpzgPmQcg91gRPRFzd1UTKgHdePeP7veSuwloUMNO5tFQD3VfX4x0qpINC79FFH1qYUz-OrUSUiNEBgk2ZVEfILffwg4SfmbQdVxqdJL2b7QDnQOVlPolRys91gfZPA0S9JjYCfISRJF0bO499U15C93IbZi7h7QWF8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c61f1d20ce.mp4?token=ULuMS1sgy96bjRp8rZ2VkMlW8Hai3eLbnC4N4gxmieFsIRWRnA-Uemc1J7B3mDkHhL_IJdqQra1VA7To1YtWUImFeIwKuesgACgw83_7fomEMC--6vdHc8j9KFerQAovv-7k32qg4CJTOAZhNAhqujOpv47NEn_Q_p9HMbTmBlDb1pjTztBpzgPmQcg91gRPRFzd1UTKgHdePeP7veSuwloUMNO5tFQD3VfX4x0qpINC79FFH1qYUz-OrUSUiNEBgk2ZVEfILffwg4SfmbQdVxqdJL2b7QDnQOVlPolRys91gfZPA0S9JjYCfISRJF0bO499U15C93IbZi7h7QWF8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
انتخاب قابل تحسین آموزش پرورش برای مراسم آغاز سال تحصیلی جدید؛ خداداد که الگوی خیلی خوبی برای بچه مدرسه ای هاست امروز تو مشهد زنگ آغاز سال تحصلی یه مدرسه رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30354" target="_blank">📅 16:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30353" target="_blank">📅 16:12 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30352">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX5KjogQtMKSXHhQp-sA71Iyc8JzRk7aId0RyaRpB0wX5zfWeGXcdsptpwHZQXs20x7wP9hRERWL8bbdLYyByCgCEHtyelZmqfn1t6wvfLv3gsbgQST1NRTTrHsgA0QdQMU9TCErSI7ZMlooZCvB49TVhjVlLL1cQtD9ODpq_o7tEz17-tENw56GDEIKnJWn3zPerz0RkppfghgW6IBXCnsNLoO7WbQYnXBboJjpzXsXr4zE_HfAiOs34v5mUog6o2MV410A0ilMuXHznrab5zK15syYZTnRdDitijoGgp54OEnikFtheeNAHyHEoAxt8VFzQy-kzGRaQGHCs66uzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلیل خط خوردن قایدی از اردوی تیم ملی توسط قلعه نویی رو میتونید تو ویدیو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30352" target="_blank">📅 16:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30351">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWV1CVy6tRJvUhHUGwgtFx-7uxLPtfG397ky0KU_KH0P9IUxf-VLZwJ8ZcbJviEt76M5qUwB3JYU22vaXn6YUPMmfO67_l2UgrzdJDvZDattZzymY8EjYEB8m8ngQy8JPTHlm3aal3NuaERn_LvwM3_3ZOnaCbX6yGldFN4VtTltASQUt68tNpZpT7sVHVJpMm9Zl8TMaQnn6otglZV8kpvTs48BVZoaRmrNyC2KULwsAWhYnGgOxGxoEDooylLzH9xOtRY-YyyQ9mUy6XLcwh2W4LkrrKfCYvcNglyn6n6or4TpvuT2s0SZYYih4P6UPGIsG435Lr47u-VolEzWGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره:
من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم منطقی به نظر میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30351" target="_blank">📅 15:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eCKwgu2gPBF8rFLpWUTvIoaC_tUeZrODAW-0JG3blzZFmIg95PHDShvBskAGvldvOfYyee9O1fDehFByt6uq3YBO5H6rsh133c_bTjYpoPV4LL8rFiGucFtd3XA5CErUFTRZl_q54vcL0-E6uuA2IBFi5Bp5N4mE7l5itKkGMenGGUB4XjpnrQU-hnYENDkmvxo9S0JwliXBcuasn-teVfMdaA7HtXmS6RdqludCYhgVcv24pMud9rjWdsrPCb6JyeV-ZSfKmefIe0ICw4fx8VwWWPaSf-N0jLp-ImYkJE_jpH5ZWn-n4RWYZSd8EI4FPdpOTG8rlRTSyW_Q6yvRpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گروه‌بندی‌ فصل‌ جدید لیگ ملت‌های اروپا که از امشب استارت خواهدشد. این فیفادی با فیفادی های قبلی خیلی‌فرق‌میکنه. تقابل‌های جذاب یورگن کلوپ، زین زیدان، توماس توخل در پیش خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30350" target="_blank">📅 15:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHx--UC9Giq8IaWXOQSUwJFkvzijtaTFg2tE1zr2ggHc9aHWUBxQfHT_H_EAHiR3Zjc1eTx-gm0Z6eU0XD-DFN7_zJAkSDlY9rh29pLINZtdJZ0tpjRSH_p4LRenCXbnT9Ojs9CG40qJSEIFxmaCO6YHeei1xENQtx-uW0qX1ic6uKqLw9LFhctClA8sf-hr-qereF7CmarnaYL5RGTjEsS-gRuXHSrCnLNvotuqVfs7kkDHbfTHBU8TDktGB6Uhmt0K7Jm1rYjMCGdHUfzSia9CbpVBjLu6kbNL9AyGx5yzGGVwB5YNRuuJSnzX2wj9yBzHtoVWkN8v6rjVMXJ4bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ حسین خان عبدی بعد از افتضاحی که دربازی‌های آسیایی به بار آورد بزودی بعد از بازگشت به ایران هدایت تیم ملی امید برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/30349" target="_blank">📅 15:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQciuXwv4ww0izGPdBOPQkjEjKh1uCXR-ebB1F1aHRHF2NmVeLJTkk0OeN6oPTt6VwBZ_3BtNnjbCIHSOFfrusjShLtWc6EqwGbfauF8XrMjRQn7XhmzQd-_RI1ehz63990kyrH7O4DDCBxbVezhsdig_iSfQrsiQytzgFnFcLfNQ50b3APt-bFwW0vhf94e443M6Kb7Af8gdu6keR6HN4bJOgZXOOJv0bEHcfKCybDz_w5k_KCSarUSQBJuA_7o_0W7yY3V_lzmf3BnYUfw4xB5slZy-LqndHks8xSqx6JqlNF4oth2aOFdXCjeNMQOAePkyhlTmpv3AjOGIWdftw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
فصل جدید لیگ ملت‌های اروپا با یک رقابت جذاب آغاز میشهه؛ ارلینگ هالند با نوزده گل در صدر جدول گلزنان تاریخ رقابت‌ هاست و کریس رونالدو با پانزده گل او را تعقیب می‌کنه. رونالدو برای رسیدن به صدر به دنبال هالنده؛ اما مهاجم نروژی هم فرصت داره که فاصله رو بیشتر…</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30348" target="_blank">📅 14:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30346">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwTwONVUH-fSqBztufoxSmVgk8YSW5DOv2CtC0XVeGXw9e7toPj6-ES-fEgUSujE9S6y8F0JcyFk107l1XPG51crEB--oPfWXpTRVyRWAwD8MdbozhID-mFEmtmx4-J5aAdL05bpVU0CQcMvWlDXmFlaqYDTggYBtuLC-Ojm7j6kAzM3mBL_4O4EO73Khb11Wr-2pUyJNm11r4m7iDEjukiKV6ucxLuk0_jIc595UvI_iv6f4aahGw_g_qNhZ-rIfPAHHlR3kTwTsdoBlDmCIEDcW6081FKr07tQdYf2kUJHvrTZ5YABJ8wpmMPgDUSoLqrnCzV0rurB8rQkDPdNIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره‌کننده‌وفوق‌العاده کریس رونالدو در سن 32 سالگی‌مقابل‌تیم‌های‌اروپایی در چمپیوکزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30346" target="_blank">📅 14:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30345">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqAHdag_T3mBoJQdI287dZzqW49Zm1sfCki3b66NdTgov1fQ5Lo56xKm-mokfM2VXmyrBfnMC3TP_BtqEz3bIYs8zJ5_fwKBqo6c0KseX3FwDWS3iUBUOMa7YBk1B06UnbRsbGTaiPWnFbAxEK5vmGnjbpGc22sFVgl1ZbTQIILfrwqsY7nF2-dDDWjHVnwjCU18yReSKEgXUkhYKYskci9wnhx0I2f8UowY0inV0jEAe7jpId7vPXnmISHJisKosvUXsm6kFbfnEDEaW33duVU3ZvOzbqZ2nQtM_4GPew_nHzSAdfY-JzmtR9KHemeOHUHDA8wz4VjF9CaobMqJ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعود بنیادیفر بعنوان داور وسط با کمک بهمن عبداللهی و فرهاد مروجی نماینده‌های ایران در جام ملت‌های آسیا 2027 هستن. علیرضا فغانی هم به عنوان نماینده کشور استرالیا حضور داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/30345" target="_blank">📅 14:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30344">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jypTeJtDv7zzDEaJX3w8a59jufSYscIcTj2ZFWr5cT7aeNRw0IumqhWSWEoPEnOIS3bsR2DPZqv9xgJQbQ0g-8VL6q58bhRZClffWvOoy_kYzZGis7OWTUQ_Eol6IAX_TrScGML6V6mCDQ6-tmQsqQtLy2dd72IUII2VW067472SFcjHMXYKJDamZfeU7xDNSkahMX6OAWccQxom3X2IEJ_g0mvcEYGMag3zi6LdgdO19UkucbB__wukrX1VEKvzp3MOrkWuMdeWVyKud4Omx4JMbi9m-F7Xrf28kW9tSBfsGhOBCpEaUX9McNo0WcLXNHqd2j7oyjdjVvcteCHdUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیدیه اندونگ برای‌عقدقرارداد 2 ساله با باشگاه تراکتور درخواست دستمزد سالانه یک میلیون دلار کرده و اعلام کرده هیچ مشکلی برای بازگشت به ایران ندارد و حاضر است با تراکتور قرارداد ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30344" target="_blank">📅 13:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30343">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r612a_T0-CRBJpIJPpygErDmVXtVSq0_NWu-Yc2OwWvwgo-rSQfUg7YTHKFDM12Grzqbqc5vBcFmCCCnGupu671GfJTImTPYfwaKsvYJavCHJNbVyWMsH0Qmm5ew1Clqd7NlyLm3fwVvqB9jWXNi-INjM1vwSHtqQDmXdd569I-r41uQPxBOm71UyznTLhVsQh2cI71JJzybceC-5hR436HPuPoC4n3soOlKubiFI0Qpe2bJYgrZx6nWHsP9PF1sO0MB3yEIZKnHTMG-vtlctLf396ePStKmzB_T-lPtftMXvDeTySGNuKv6w4L6ToJVbfuOVi9V4NkaZw3r2yhF3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
تیپ و استایل متفاوت بازیکنان تیم ملی فرانسه برای اومدن به‌اردوی‌تیم‌ملی این کشور برای فیفادی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30343" target="_blank">📅 13:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30342">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkgMIEc8Gyqv9r6ts4uzMAvO1h2V1W6XzA61grzBsT8DS2vNZ9zAQdYbf3cP76qJQxIwaTQEk-qL8QHhMImvRni-SuVrNrsZ3W-VNLymQhEzkiRW_1i-NGKunq6XW8bktE7Nn67t3irEFSPHjjDxNUxXzl6X7Z6bXsYHY_3iVaxZUvy7ZP7QCy224t-c0nq-ShXqWz26PHXNhhaz3wkx24V1anZn6znIOd_f1muno5Sfud9OBe1_P1c0L70abQIBXN7OdNrKKaPcMNKG5Wgon3bOLExS1eQM9rigYm-47f2TMidNXChM_SFtVKYE27lnTepaj0bpfWi3N8itN601LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30342" target="_blank">📅 12:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUwBw69Y5LKkTuY05KxW9Qrrmm8Qjt4P4Awa1tVdq4u2fgqzoHvKfufzJB-2LP0kaYo2MPGTHYAMX-YIBRwLbmFWMLApmrFba2WZ0e0vNucg6MaVbm-1MPrEpGuTXbl_KgEC_Veyu3Ckmx7ioXkxEyeYX6vNXldb6DQKFEQY875fWqyyGg8GjiEaARfWp-m-cKNni8dmevylNXrUWOUd9CidJTS-BqjUr6cPMC2EM1cPOM9Oqc24Lgdd1fBNEDQr4432T7W-O-gPPZagyFZ_R-88u6ui3NhtiEyk0SbOjEhcy61l8ANmg1gXJVYTjZKkqbrmI2-lRDbD5R-renYZ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئالیا:
چهارتا مربی عوض کردیم این همه بازیکن جذب کردیم پس‌مشکل تیم چیه چرا نتیجه نمیگیره. مشکل تیم از نگاه کارشناسان و پیشکسوتان رئال:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30341" target="_blank">📅 12:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30339">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOcCsjo5PRtXWkIKKmHPtiJe77kBl_YDpQQmhc-JdkcJOPh6o1vNrVFfpH1ZNRIOe3-Wg89t8k4ps8hcMrYCGomXaywKGT3eHZdaYe3IY-EyNpTH8QZY_kgmg3pvwuMBUMiJ52a0HRczRRSjy-AjWa5nIWyFzX5gLhSGp1H7JB-pgZmuwSougZ-qHenxURh3DeYhIIBVG-0cmrOY81k_3EMcWXoDhB1hlkVZR7WRzSDDN-PvOirsbUpT2EA9W-z7ZcinIoob3knwrFLmtSm6vBnKYIyZOgojpORKXkF7nm97iWKstIHROL8-ygnw_qIXapGVjB6Gkf6IOlKCgSmlDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛ تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30339" target="_blank">📅 12:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30338">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v26SOXdyJrBX-qiKabgvwoJxOB5EL5FZErt5Ar7MEA9T5dnX3fZTlSTD55rNWbZDgfndrQIctimX4okFRg6DzDjZ3hB7suKLl1x5h2YuHRa3L8E7RNWjSgNnTvswLzP2HOQhS5UR3zIox4goL0DHguPPJT6iBMo2j6rB70qO7FEU6Wi43IvqmCdDhHJQkAMJSfisW3h6hiu1vTdkTzKhqVzb9RSvj-jJnH2kS2mxW2q9NW71PU6lQ5XVGJgiCzz5UgN1ppJLjqjYqn8ezIbDCFQjjH3zyjW9WvRf5MyGcGWappwlqJSKq_8aOVNfllRB9W6n0Pegi1wtdZzOM2_TFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طلسم باورنکردنی تیم‌ملی‌ایران مقابل ازبک‌ها؛
تیم ملی در شش دیدار اخیر خود نتونسته تیم ملی ازبکستان رو در هیچکدوم از تورنمنت‌ها ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30338" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30337">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLI04FhlYdg6IPsT5AzhGbuVGFSzUyyda1k3hMuaWFg741rlUGQ4WwvcIRf4s7yJl_G8pxDmff9sTYhd0aJ2FUqFTypo5ip6fDpzHssdK2_ZT-ikyr4_c0XH70wgNXyL2ccNKBcEcXmQRxadR4F6bfMDOl-WJhvxUPNLQ57yB8IXdceZSSTvwn-DledANsFSoIkkT4BQkf5UO0YiJ57kligD23rt8-2kpO0PI0kjcOrJwt0pKXVgfVmGg6i2N-B4NihkVfvw93iZ9i0wpiPEnx3ZBpMTiii4VOj-gtg2_2StYtmu9rSPsL51Tt4KrzkkWpJekqKyePgILJjrLI3GGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
#فکت؛ رونالدو 101 بازی بعنوان کاپیتان تیم رئال بازی‌کرد که رئال هیچکدوم ازون بازیا رو نباخت‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30337" target="_blank">📅 11:58 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmf5QJ1zdJLGV9vh6vnvS0tgWgdZQnTRRbl83V8OcF2WwHbLWyz-NDkY3Nu9OzQteGhYSFmy6W-NO1VezHZB4-AZnK3KxXOWeUWhnhRTRiD4zKenQ9k2Ap-gUVTMHe19wscSLvzyYX67G0uepSIsly2QJQxQlvTq7nXJcnzh3uR-_U94DtSodIz97usfErhEo6rc03wYHXG-M4tFuO4DxpeM0lvJeeqiRftk24mZd-RpklLHKCvu3uj-ZKz_ydD5dABu6VS_p_TPLzD3t4p7KuPOdyiXoKNrv_xulVUasxaUYZg6fVizgA3cO1_V9Ro0O0OdMPJgq40R4Q50Q1IXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر سابق سپهر حیدری: من زیاد اهل فوتبال دنبال کردن نیستم اما در حال حاضر بهترین بازیکن ایران چه ازنظرفنی چه شخصیتی رامین رضاییانه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30335" target="_blank">📅 11:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsacJtO82jvaFSDYdXwrAXoznOMRwH0AsRY_OSa8eyy5mF0PNmMWXYqNgMl8PsXI-Hw7RbJhoNN7Gvg3K0L_gIvq7IzEvLWJoOpPS8ZyszwWGLGGVgJDh80UGW8q79nW5mYLYGt2AtasI8u90uD3dmgPidynZPPZiaFznnM1VVKEVeAxZo_K0OwwCtxTy-Ae-JGOxYYc68l9AnRzIxwbUzUVBTF0rk6ij2NJpWK1eaFSAFeAT2dv8rozOJUej1h5_f0tNokkcIZ1cfAUII31c5sYqiDi7HKpsYbQ2pmQlRU5M810rlfFvGFs-kfGVji0zFNz-QbkDx8Kh353i5UAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعد از عدم علاقه مدیریت باشگاه استقلال به برگردوندن دیدیه اندونگ به جمع آبی‌ها بخاطر مدیر برنامه پر حاشیه اش؛ حالا از تبریز خبر میرسه که ایجنت اندونگ این بازیکن 32 ساله رو به مدیریت و کادر فنی باشگاه تراکتور پیشنهاد داده تا درصورت توافق با این باشگاه…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30334" target="_blank">📅 11:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=A6ILuA1jbu8ZsAkt4tEZPGF7MSmwoOOjzRVa-fE5Zp1zDl5GSPB3RlD7F45tz59HtBbqabK1Mw-Bt21vcKdfeX3x7uqbC1aDflojY577McVGvTYNP92-trfN_pG3LvCFLpAKtcmM2QlCViT2O6qu7e84HZaxxUlnYq9hwYJTgx7PTtkiE6DjYaQQqv8y0YvvMhNee1iUGodeJt8iA3_7dRo-Z6RetouCTQEDvw7Sw6QgXUgYdgbXIBbsvxx178LIvQz4s_NEYW9Ab89za_VTN-nEChnBG1-ofAzp_GFXr4TCdc7dUABg0hG5II1HADtAoSVBmGxpd6HncLUSa7FfHRed9pCOmVgoc6JKRHH2qZtaJQtIt3BfAlR4AmA3HLG3LKYar3gZAzAfzoU4OMrEOir6_qxxSG2HzCxp1lIivvDZ_pxDWqHFkL5ELf_PF9V4-5oIshmq7P0ro9TStgxn7Q-oxReJVsvIEJIiU0dleqZbNQaXPJM9PEh7qIJGeTXwJ3uCFBGzscOzRTDk8CEjkmIZfEaoqDXvGY8elsMnlq4FZ9bptU8hLfqqJV0lI4gkbLspTH7waeodVCMhGVJUZmwX_5oLvAXDQ3Zdhzfyy27FEFIg8V9U_IdJCjTCtS5NFJBdzcRi3na-cksVT-RR6n53KjIbgGdHTHRDJg-oPCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3db773d12.mp4?token=A6ILuA1jbu8ZsAkt4tEZPGF7MSmwoOOjzRVa-fE5Zp1zDl5GSPB3RlD7F45tz59HtBbqabK1Mw-Bt21vcKdfeX3x7uqbC1aDflojY577McVGvTYNP92-trfN_pG3LvCFLpAKtcmM2QlCViT2O6qu7e84HZaxxUlnYq9hwYJTgx7PTtkiE6DjYaQQqv8y0YvvMhNee1iUGodeJt8iA3_7dRo-Z6RetouCTQEDvw7Sw6QgXUgYdgbXIBbsvxx178LIvQz4s_NEYW9Ab89za_VTN-nEChnBG1-ofAzp_GFXr4TCdc7dUABg0hG5II1HADtAoSVBmGxpd6HncLUSa7FfHRed9pCOmVgoc6JKRHH2qZtaJQtIt3BfAlR4AmA3HLG3LKYar3gZAzAfzoU4OMrEOir6_qxxSG2HzCxp1lIivvDZ_pxDWqHFkL5ELf_PF9V4-5oIshmq7P0ro9TStgxn7Q-oxReJVsvIEJIiU0dleqZbNQaXPJM9PEh7qIJGeTXwJ3uCFBGzscOzRTDk8CEjkmIZfEaoqDXvGY8elsMnlq4FZ9bptU8hLfqqJV0lI4gkbLspTH7waeodVCMhGVJUZmwX_5oLvAXDQ3Zdhzfyy27FEFIg8V9U_IdJCjTCtS5NFJBdzcRi3na-cksVT-RR6n53KjIbgGdHTHRDJg-oPCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری درخصوص دعوت‌نشدن برخی از ستار‌ه های ایرانی به اردوی تیم‌ملی توسط امیر قلعه نویی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30333" target="_blank">📅 10:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqULPCMUV6oj0LYilRzz8VXr6fJzCuW_6j40538D8ySXGUl-5mPVZhDjWYvZr6KPiD0qtTH_TgtlW8vvyTpRuRAbKx1ImNqq_u0tpXtz1MVay24kjONI815USvbMrZJlDzG8UiMtn_Erox3sZwTJ1aP8EA7YqsEKmeuxz3RlF2I0D3HpwxG8Zypfbcw4v_eO9ijoYwY7Y9T-8Vb-MJZTBh-ITvnJNJD77sIPGGo7QbSK1HIp6l292LmZYTwE4-um43Iq042REG2cX5GRygIpXwxS2KlkNHI9pY5xKDL1lUcoQ9kQoGrtCIqJNFwhGzLXvrVpqCpzOCkbRqYqGzRQ8fRgM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f00468324.mp4?token=D1VW7CTrgX__VunShBmtNYuiZKr1uzebmAaPLTqYk4wtDzSxJGbJfp3Xj-62R-P_RgKNdgIVFH8CyRO0iELUN1OpVlPrFzY08rgY1Xh2yZf6FehdqVaJ36ol1pfnJwoB1alsJvqYkzwUxnTwtZhR--ufx93f7lxwdQQZw9rJ8dpxe7q2Yp3rTBHZBGEe8lPZgfwGdLV3ufLIlaYUKaQZJWYrMfg-e12h4fVkGr9CQQ06tokuRRnpNxjRV_C1xbgJETcBAMfmAzlGEM3ie1kARPNyCpPch5Z7EFUJf-k7C4g8NdRFZQoRj4tf_uvbR8_a7Uy1OSQQFO1P6E77g6yqULPCMUV6oj0LYilRzz8VXr6fJzCuW_6j40538D8ySXGUl-5mPVZhDjWYvZr6KPiD0qtTH_TgtlW8vvyTpRuRAbKx1ImNqq_u0tpXtz1MVay24kjONI815USvbMrZJlDzG8UiMtn_Erox3sZwTJ1aP8EA7YqsEKmeuxz3RlF2I0D3HpwxG8Zypfbcw4v_eO9ijoYwY7Y9T-8Vb-MJZTBh-ITvnJNJD77sIPGGo7QbSK1HIp6l292LmZYTwE4-um43Iq042REG2cX5GRygIpXwxS2KlkNHI9pY5xKDL1lUcoQ9kQoGrtCIqJNFwhGzLXvrVpqCpzOCkbRqYqGzRQ8fRgM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های محمد احمدزاده سرمربی‌سابق ملوان درباره سختی‌های عجیبی که در زندگی‌اش کشیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30332" target="_blank">📅 10:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30330">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xk0fxA9h7_BgUbuaNdhaSCeMS5-MmjNqLyi63YgEvX6kt7oJkVz1tS8xtxAwseZBRhNKme4ZhKjyq9-nK28fPuh0yb8arkojw_3IN1PhMOYDTGYcBYqjWBgKGgHSztGuk61hFxmP_CvVnnltnFkbLbi2kbTaLl4WKLWtj29Pt6CpJaOGGCAtDnqkqEtVMG7XKzLYgfmZFndDUu-EyY3HBLOPOzIPxs4HtfgeNQGyzaouJ1b6qeh_wrDMiJS3V9DrgcAc8QyAk6uMB8GbJjD047wkTyJJBkKCdTRnqbYp_Ru2xcughgWf4ciMvx2q8-S-yVdsf6xFn4fA9bXfHz-zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYq97D81S1MOIRxWcn1ukKjOZVDxcqOih9QA1fdJri2y3UKckvlI1RS15uEkkJb7L2ROEbwht4d4vZ5wk-EezRQ7IkaDb-L5KEGzr4NBwW1sNOlxftr00pwqkSh3gT5To5VO0tRCfFLbWA3hNJVK71qUOu29rqSOvEwo7GBzdLPwBCknHOfbhDh-8mCy9B0U2XN2B3LQ9sU9S_vDpYSKL3YkcOmvjWkNWAffVUqXQMwcDewOtATkrMsBHTYVieWzB8xNH6WBr_Lw0sYxLKb0_iXElW0r6bD6OZ2VIdmuXWKJ4_wwJCTKdGfiKi91U_8S1BLnbaXxNrk-LrFL_Z3xFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
فلش بک به سال 2012 زمانی که:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد 85 گل به ثمر رسوند.
🔵
پی اس جی 86 گل به ثمر رسوند.
🔵
چلسی 87 گل به ثمر رسوند.
🟡
دورتموند 88 گل به ثمر رسوند.
🇦🇷
مسی به تنهایی 91 گل به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30330" target="_blank">📅 09:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30329">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=QVZZL2Z9X1y2KzSOZ0fLZ7WHrTqN0aMPrD-hgnl6j9crEKFycu_o8Jkyjt_uLj0Wdmrh-gTioSDjaZMZPwRCZKxJrRtC9_J7JJVR9f2VwbZg1y06tgMinorn9oTzJDcLIAbTRu3XjzwghBuLF80dkWWkFsK7YEXmDCwNGWLDcBL_lalTfy_2l1MS7ia7wVmuCJ4qgjy3UQpfNpt-uTEBit7sSoqEbAfqV_CMyVzqZlawIUan_i9YtvReRsaDVdkWBGfqUxNGMureB-adoOtaWx5RCgglkETU8RXE4SVeekFFcp63KPNpKt6ofvQUy-ASISGteR6dpJ60QVjLF6KwPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d79121e6f5.mp4?token=QVZZL2Z9X1y2KzSOZ0fLZ7WHrTqN0aMPrD-hgnl6j9crEKFycu_o8Jkyjt_uLj0Wdmrh-gTioSDjaZMZPwRCZKxJrRtC9_J7JJVR9f2VwbZg1y06tgMinorn9oTzJDcLIAbTRu3XjzwghBuLF80dkWWkFsK7YEXmDCwNGWLDcBL_lalTfy_2l1MS7ia7wVmuCJ4qgjy3UQpfNpt-uTEBit7sSoqEbAfqV_CMyVzqZlawIUan_i9YtvReRsaDVdkWBGfqUxNGMureB-adoOtaWx5RCgglkETU8RXE4SVeekFFcp63KPNpKt6ofvQUy-ASISGteR6dpJ60QVjLF6KwPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30329" target="_blank">📅 09:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30328">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQEGBO4Bq5icQErrX26XYSQ-JJaD2VNF73CnZkxSyJ1_kU5Dk7aWObXCSXQxA2WkSHjYD1e8VZBEIBF2ZGGsTRkiB4dctj5FmwyPF98tJ6vtQUqYblEXrwokTdZnaz5jb93iNRy20FEDlyn-welOmKvdJmD7po-hVKlTiD20PwCOleyQlGygdp33MdQ_UnPOtjrRENqHnQlm499GXnncHXQDLBjRzXL1z6HGqdFBq4ttOz-vN9KMpdlGbAcHIK27NIR34_8M7aWSeQ1t4aK17vteQ2_WZ7gcBjVbV7egijTw957Ss2uZwd_AERvUaUIwiSrTTWDHslk_9RgkmUK4hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب ستاره‌هایی که علی رغم درخشش خیره کننده در دوران حرفه ای خود توپ طلا نبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30328" target="_blank">📅 09:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30327">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0Hm6yu8Zav5B9NbGDMJKm5EXqKX_Yz27vxN056cp0D8pMQe8-nsGzYiCF3VMO5mI0rO5btgLXkcJa9hiVtkqi8XfGUlfkVrFYQkb-IWtAk9VgG99OtIgQpHE3VsBGrCPvj-JHmJXCkGzjc4t3qvqCYChQnz_UiaqZKMJp7xQxBHNQotepuHN3zepXYP2c_e1UWG9dDzEld1FWos4Wk6I3nY5HpA9xoK29c-CZgtovqqNmzNdv0OoJxSlRmrru2j31znQwKbZM08BLdT3a-xp0sggMKLfKZunG0mn542LgULNBnVOHoZuwlMiNt9tKXFlSbqfWy-nsoVgpAo81Wkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای آینده استقلال، پرسپولیس، تراکتور و سپاهان در تمام رقابتای لیگ و ACL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30327" target="_blank">📅 01:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30325">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VN9B1zg9486LeUAwJXpSz6TvxGm9yaeKsq07qOViA-m_bjOamWBwoDDSJQls9ztVfJzrRXqxqE-_WjFEniAv0M56ZCt5E4MjkUo0kGwEc4cPC3YtgHAcdDtVYDu6lydkBtg8KixbW85RdmeiRnQrJPoCXwz1ZWbajHr38MUAPbbuTM8Lpu38hj-t8O2VPioGwJCcxkfE2FxGyRl0gBCeKBVgKM5lTmQBQEuSBaF-NJOFJJIdyW6UlNDZne98xlgHkmXe9li0b-OmaNcKmWQgZpeikp0ORHL1686C2zfWmyDKRTlCOQsMyvKlZPR9oWA5yqbAu0noYBuOcLPnnr_Sxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KBcT6MCPv9yC-7lVkht3spd7Bh8CVY1fCxoJUy4aUTW0Odm82Y_iecCys8vBurJXr6TxUzKG543zl-kUs8mjcR-3NTnVTTilXgnn5Ho1nApDyMYNP-tpIAVt24Fr5afObognFFLlFyJbOykRk192cjd4aGwwnJhFKJ0Tt1CMlYRNmZ-KuHx4c0bkBMn-q_StkQF43f3aDK2EhTMWGtQxHVxsIgx1zOVdz_7CansxeBHXOl6Y0lPSmdbODOILq0COVzQjqR2Dgq2vYBRAQbyYWEO-FEPdOmznj8ELITmJgD2uopv2yxjbn76Mwp-b5rNeluaxmht4QuU1O7Ff-jiMIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آخرین رنکینگ بندی تیم‌ های ملی پیش از شروع مسابقات‌فیفادی؛ اسپانیا بر دنیا ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30325" target="_blank">📅 01:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30324">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=oAsqefyG6EyJ66oG8SHrnOsjaFBl905eChUqqw8h3JYOAengKxL8Xgz7_PiFycADyj4B7NL5RAkNjKikOnNQTgUl95aNyRp1lEfV8Y2GiqRIrKWaXMVM_MMC3xIXd2TKqOaHTHuGnfsE1x20aSGfx9jah8NctaX8xNClqsreu1drqkWIwQUgFESEim61Uv4hZh6MSPPeJt6DFXKPFxLCCwLy4apUF_kl0pNfMyv0Z6Tu9hudyMkj-Xvp10PHIZEjbtzhDLtRF442svgBw2j6Q9p12exa8XR4zsO40pJQ7yXMEof4sZkHlWOyv7S9LvX69To5iFHC5rgvreSFiy0e6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbc5ec9105.mp4?token=oAsqefyG6EyJ66oG8SHrnOsjaFBl905eChUqqw8h3JYOAengKxL8Xgz7_PiFycADyj4B7NL5RAkNjKikOnNQTgUl95aNyRp1lEfV8Y2GiqRIrKWaXMVM_MMC3xIXd2TKqOaHTHuGnfsE1x20aSGfx9jah8NctaX8xNClqsreu1drqkWIwQUgFESEim61Uv4hZh6MSPPeJt6DFXKPFxLCCwLy4apUF_kl0pNfMyv0Z6Tu9hudyMkj-Xvp10PHIZEjbtzhDLtRF442svgBw2j6Q9p12exa8XR4zsO40pJQ7yXMEof4sZkHlWOyv7S9LvX69To5iFHC5rgvreSFiy0e6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های عادل فردوسی درباره زندگی سخت یان دیومانده ستاره 19 ساله رئال مادرید در بچگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30324" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30323">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=vOG80uHQQFVTQUFGQJKHZVJU3G81PVWdekEByDBKcL7Du-_DltFB5qTyf2ehZL-n3Nq5-N2OXcwdi5SJZ9VSwIW68IcMkzmu46clJO1XtoiwIFbnAgNoevoRAvMxo7rBowZ9LobUY6b9K_FAJqwYrQpltcVfR25YL-kPw-0PDhnU54a0wjY6_HsPZZqxva5yZpgtykT5EpiYGGYAFNns4d0xQ5TGSA5Oel_-gJ_M363TLHEWG8d1_jutpTL0s2JnFnpoXLW7MZPoZZAxJ7wShqdYxRoixRAwo3AVmos5Y5TiXdesb0ozwfpmVk7BtcZRkUBUYw-gueE8WGvt-O8fPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ec3996d3.mp4?token=vOG80uHQQFVTQUFGQJKHZVJU3G81PVWdekEByDBKcL7Du-_DltFB5qTyf2ehZL-n3Nq5-N2OXcwdi5SJZ9VSwIW68IcMkzmu46clJO1XtoiwIFbnAgNoevoRAvMxo7rBowZ9LobUY6b9K_FAJqwYrQpltcVfR25YL-kPw-0PDhnU54a0wjY6_HsPZZqxva5yZpgtykT5EpiYGGYAFNns4d0xQ5TGSA5Oel_-gJ_M363TLHEWG8d1_jutpTL0s2JnFnpoXLW7MZPoZZAxJ7wShqdYxRoixRAwo3AVmos5Y5TiXdesb0ozwfpmVk7BtcZRkUBUYw-gueE8WGvt-O8fPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چالش‌عجیب‌وغریب‌امیرحسین‌قیاسی در قسمت دوم برنامه جدیدش با خوردن آبلیمو با غلظت بالا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30323" target="_blank">📅 01:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30321">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HS9g0GYN45B7tCkGwMmfuefSZyU2CpK0PtHnSGCX_i0tyvcR6BWuHhlzZE4FMp6aheJtxTMnehx4Z_StNrUER4uGvJovhfOFx0xTYJNqZEQzQ-4YozIi4TYUyd1WPaIXj7wSGDukw8Att5E4HHjvuk3h_z2Pp9pOimQ90bKTcVLqaEgb1p-VJU3k7CfiKXa3UmEYkEYEpuLaZW5oVrCf0Jn70AtRe0sXLBQurVlH3cCqICo-ixd1DvT1u-mgdO3rgN0iqStLsnNYwKKnBWzNaY40iNpLdAAQ7HJvXY-2vR6nVA_kCcl-eK1z0JQazMypPDNIGN5nfTtA8fzLC1GhNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شهریارمغانلو مهاجم‌تراکتور توصفحه‌اش این ری‌پست عجیب رو درباره سربازی بیرانوند گذاشته!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30321" target="_blank">📅 00:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30319">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iS3O2JWdIumdpYZouMccrPXAiyJQWmm2w6x6loJr7sizYqRgyU5oGXmixwnYf36R00iFycFcL-r5w3Q12ceSWhNq63-w32IBpm3huflSZVjf6qKKI9uMMwGcmbD-oTiQDJFmgD1By8mm0jHbf-EUY7vdccLTXlf5kndeczNiXl23ekaI33Pyq-aYKLH67ZOTHTk_bmRnRVegnqT0JP-zzYzFR6oLo4YpsIgJDOZWGmd6gIwA3qtsUR4_TEjLoQ7QW2vSFswYx4lfnUNyu_IvSO_e1sNDv_WPkCbKoEOzyHfV5g4_H2KpxozHIQBZ7nJtJ4gzfJpDJnYyDR9zgxj9MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل تماشایی هلند - آلمان باتقابل‌تماشایی ژاوی و کلوپ درهفته‌اول لیگ‌ملت‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30319" target="_blank">📅 00:22 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30318">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igohTCrUkANpqeFnsr7xn85leWF6O0_s45bp6mMb8dtkOyS49DnOcfB24aDdwrCb0V2C4kCWJi2AbsBZy21ecgxCq57_Mt8RM-kS4yrAtCJ3bmGO_Uy4NS37o-wNOAAOCpAYj2Kih6sYT8oKanfQl8x3zulyzCoR0Ssz1w7_cR0wnrge9K1rANqV7X8MBa4pshHP-3khGQznEKWP4h9fl4rXQCzJGODvDRGWdqDqNP7n1wHtjJwyI3ekhRqintlEiiWvM79pcpOvhN5OhX7CX-yFcbAxC5urvZ-1a4kFBAB5fLKtlQPhgWoQamVm0Z1NMvJgr9vWYeIt8qqQq49yAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌‌‌‌‌‌تنهادیداردیروز؛
شکست‌مفتضحانه تیم امید مقابل کره و حذف درمرحله‌گروهی بازی‌های آسیایی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30318" target="_blank">📅 00:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30317">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aj8NA9EG72GuuNcu8c5e-SiYhLQ3DY1wmYK_xyj33H1Bujm_jgQtycZiRRYLLRN77vJRLhLR-XqRgkrPo7MLi628vy_rsmUuJpL8urucWdBZRFBMvM__XCwoDagWs9WzyKjDGhJP59qLwGfiQGOHVXp78vjGnytA6Vr32dlb6YcehbUAMmuyeFtAKYBo0nucpzY0O6f5mIhmJ8C9pMriw_aB9Jr1YVHXPDpQsgtBtGx5FQ2aV8jf8fVriSKO32FwTGNK8Wmjwh7Ueuaank2QDV4WcIrt8YpEMhYi_3im1MDUD9U9Z8-M16HW_2-6BjRU6DWTcT_4BhUWYmbX_nBTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
گل تماشایی ابوالفضل کوهی در بازی امشب نساجی مقابل استقلال خوزستان روی حرکت انفرادی خود؛ کوهی درآستانه پیوستن به سپاهان قرار داشت اما در نهایت شاگرد مجتبی حسینی در نساجی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30317" target="_blank">📅 00:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30316">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=tVDdoFSY9V6qyV3z3kYOJwXf0WCy68debbCazLEERR1p3d4espmLXAIXbedZCfR1VkeBrSEGWtn1J-_boZl4vJwx1PcoVVvvjGBS-jq3IuHHwVEzlUFoeF8C3mC5IuqozUiVvFX3bbrTlYPfbhR9iyk1KnISCJxyMgj2bL1TthtMwKUHpFp5fwNqx5p7tVkXCBX4ux5-enKAHEylc0YQ5zKAzyRPvGps575IEV99bCIEHxpzCAuSgMZKABTnHZqeVl0Ojnel04uBxbpvJW31wpALGryoYd2jntodKjSdP2g9RLbkclVcd3iaB2CJmv9uiM8HGMzKsbkU7TsNGAx63RVW6__gMg9T8qyk_dADNNlkZIxdCXKITYmIE0UJdY8HbpPFTotjqpg7OvjYHz-PEA8oZlfeX6F7rIc1rwKOZAFEsF6IdCXJu25CfT7W6LbTkuaFyAwoAFE0xB1elMER1VhLYmLNCpcA2AKGLqO3kNrpifDequMf_8bWjjTVEXeLvBc2vbUSx7ZNHaisIqt3dm6gNdGkZWrE7mqKmw8BuXtP6LNp1l7yryavWaqxhfWnrHM2iHYVXR0hmiuos1RpX_9COHd9lhwX1-98Y04_Yeffe6oJ3NgIHO2J_v-k2CwOEbT8dE02FjlqcwvmVfxf1dnEN5YRgI0tecY5uQOIDvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/991e17f20e.mp4?token=tVDdoFSY9V6qyV3z3kYOJwXf0WCy68debbCazLEERR1p3d4espmLXAIXbedZCfR1VkeBrSEGWtn1J-_boZl4vJwx1PcoVVvvjGBS-jq3IuHHwVEzlUFoeF8C3mC5IuqozUiVvFX3bbrTlYPfbhR9iyk1KnISCJxyMgj2bL1TthtMwKUHpFp5fwNqx5p7tVkXCBX4ux5-enKAHEylc0YQ5zKAzyRPvGps575IEV99bCIEHxpzCAuSgMZKABTnHZqeVl0Ojnel04uBxbpvJW31wpALGryoYd2jntodKjSdP2g9RLbkclVcd3iaB2CJmv9uiM8HGMzKsbkU7TsNGAx63RVW6__gMg9T8qyk_dADNNlkZIxdCXKITYmIE0UJdY8HbpPFTotjqpg7OvjYHz-PEA8oZlfeX6F7rIc1rwKOZAFEsF6IdCXJu25CfT7W6LbTkuaFyAwoAFE0xB1elMER1VhLYmLNCpcA2AKGLqO3kNrpifDequMf_8bWjjTVEXeLvBc2vbUSx7ZNHaisIqt3dm6gNdGkZWrE7mqKmw8BuXtP6LNp1l7yryavWaqxhfWnrHM2iHYVXR0hmiuos1RpX_9COHd9lhwX1-98Y04_Yeffe6oJ3NgIHO2J_v-k2CwOEbT8dE02FjlqcwvmVfxf1dnEN5YRgI0tecY5uQOIDvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برای اولین بار در 47 سال اخیر، یک ژیمناستیک‌ کار زن ایرانی درمسابقات‌آسیایی شرکت کرد. هنگامه هادیانی؛ ایشون درمسابقات رتبه خوب 13 ام گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30316" target="_blank">📅 23:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30315">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6BynmiV8wd54f_-a_nM92rQTbfshxj9SUbIBb3cBSL2JfaFq_rLoyH7JnLRxWzKUNCrgsFngqOpzY_0Iy2YHJs6TsIl_Xm7XnBIYLPpHo4AIomDgSpbVlOpHC5L1E9FyqFJaSHghqupmBW-xgdbW9N80vlzj1MozraeSnpq38mYLkVhtmsBGL7UWD4Ya4yyFDnsfkhgpBa2KXt4e2dw1dicCZxmOc1bJIte4sPCeZgP-TmKRPG5Zu83zPbYwj0XrRRtvlb6iEe5va8U6TAqOt96i0UcjhHW7gPUDYPawuuGwAx1d4g-rZCBOZ2kgZByBzuDs_aLk2kWA9Vad63k6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
صحبت‌های کریس‌رونالدو کاپیتان پرتغالی النصر درباره زدن هزار گل زده در کل دوران فوتبالی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30315" target="_blank">📅 23:38 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30314">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgUcXl7rfmIlpJ0prDpsG0X-pggsT861jdcKHwiS5JepJWElR2fBI3T8fHKTPKB6ZyP9T0U3lu5Blo0QS6_wdGjL9E4XuBiip0miT1X8NElFZ19Ju64XSBafcr4QblTSB_F_aOmHTgDwC5bh7hRkLOkmfcsSB6oQa67Cw0f2Q3XsNFADSEfjdFR_3ZaARcco4ix12AzP82aGMSOiE9GcEiZV_d0kqCFxJbvnQa2QA4-j_576gXVVBJP0cuPiq6n9cAZ5crIzpozNeLQtgbct9z0bWDs_FcbbGsO4tq2NkjjhVxY_zCifvbdb2LuQoG6PIUHt8yBhGOB3Yfjhof62Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/30314" target="_blank">📅 23:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30312">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laPuc3OSUF8HuATWMeBy2Ag53dfj1GnGUPkrhyW6MC4s_7Mlye54KZy_Azb3RaEkw4rGmabRH3zqxkNiOBf7Ch4en9vI49_9crHr6xug33iJ7hRBzHwMoCFY9JfYqRgXWxcFympL_8mubeFt3tTK4N8zupvraFBD34hSOd_yhz9Ci4PKucaDs913KJQVPKIGVdxnUWTvgd5ruDrc7muceUGVMtEYxcYYVRmeauab28Qufnvu7pXikwwHCMod1fH3CrHdJapPHTmnIQCkySj4J6N7bEb1OVlloeJmWghoYf6eQ2pgV3X0YLVJ-_zg9d0sIaClOJCWpoP8ptdUTc6GxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
اسماعیل‌قلی‌زاده ستاره 19 ساله استقلال: باشگاه سپاهان به من گفت یا قراردادت رو پنج ساله امضا کن که دیگه حق تمرین با تیم رو نداری و حتی اجازه حضور تو تیم آکادمی سپاهان هم نداشتم|قلی زاده در دو تقابل اخیر شش‌امتیاز از سپاهان گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/30312" target="_blank">📅 22:44 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30311">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG51Oy8nWMkJ6mO---i0nbCkLMlp2oE0D-xpUE4jMp3SJGEn7E60UI6Y-f2COCLkFmiI8OrieJJUXZZOXtaqOxyuh8L0gi5P5JcVpWyhMKS5n2LJoUuJRHuPS454p93grQ1F1NZkXMu86ddUrg1d2b_iLSOvS5goN3X-H7EfAlHwZfyNCVarx4kt0rmgjIh7NgbcEPSia0_2c-0NaGgP3nMc7CRfYVIK41gQMm8qxhNq4oxB46ECZPGhaRV-bO1EsOq_mYeNM8k3glP7vQjXHzHJ-Fk-cvf5007eXs98ZN7QnqU4onlqNT1KM5VQ-Wq414N1t5-QdsuJjTSLVU_Fqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30311" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30310">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=ZKR54jcr9lTMB0byRKyYrlF9bOkp1p1Jhh1Ix1PL5Kj6Z_SS_yJHOsIv82bGh2ISBl3yKrDnEGmOuvDfVxHD2nZEwl6b_fcqfFaBaFKNByLV58sQDw6eMjqo4n_a2fXSHcynvT0AiGkGRYQ4jmLywBrJLBV8oujQW755peE1YCMq-sBmjFqRwT1OGyx434jXLpqZfFQ8NybX6EVi5GR2DKiq7MV_DvNIBadE_e7cbxwXhQpA8ohqGuZ2wO82GZHliK89ZSQNqtJtw0hTyFaY2oXJ7v36Ub6cxBxKEmz24pC5fBhVT4-Efr0BDXXJ22XKVmNkXaQjWnsh7Bj5es7MtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec82d980b0.mp4?token=ZKR54jcr9lTMB0byRKyYrlF9bOkp1p1Jhh1Ix1PL5Kj6Z_SS_yJHOsIv82bGh2ISBl3yKrDnEGmOuvDfVxHD2nZEwl6b_fcqfFaBaFKNByLV58sQDw6eMjqo4n_a2fXSHcynvT0AiGkGRYQ4jmLywBrJLBV8oujQW755peE1YCMq-sBmjFqRwT1OGyx434jXLpqZfFQ8NybX6EVi5GR2DKiq7MV_DvNIBadE_e7cbxwXhQpA8ohqGuZ2wO82GZHliK89ZSQNqtJtw0hTyFaY2oXJ7v36Ub6cxBxKEmz24pC5fBhVT4-Efr0BDXXJ22XKVmNkXaQjWnsh7Bj5es7MtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های خسرو حیدری کاپیتان‌سابق تیم ملی و باشگاه استقلال درباره حضورش در سریال پژمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30310" target="_blank">📅 22:26 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30308">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNIZ7riPz2fTDQaL7P8eXzq8fH3YdnaytxZmp3on2pSYd8oZIfDAe8d_p3vzcqOAavyUHSgBl9ynvw-4aa5DeUEepaSKlrPHZrcS8nNQy5-BXlc3cZB0q04FAZooxhAFt24jaStl3zKmXkOVd03YL_IuBsViCTnd0SAT2HFqIc70O2Rc1CqtdHKsJB6zKYy3o0calt7qkdXA0GMwgIZA4txhHRXFbxilUHhBFGOYDFylUAuBYEcy_I8sRA-pzwrAi5PQo17Z7CR0bHegwHS5haiGPxKM8hZWy3WcWQBekL1V7cJPjFKCsBsDmEA9T3cDEEtOH2yBtrIqt2Up2qw2dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرامریک‌اوبامیانگ‌مهاجم37ساله‌لاکرونیا امشب به‌این‌ شکل گل پنجم خود را در فصل جدید لالیگا به ثمر رساند. انگیزه‌وچارچوب شناسی‌اش‌خیلی قویه. این 414 ام گل کل دوران حرفه‌ای اوبامیانگ یود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/30308" target="_blank">📅 21:56 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30307">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=KZK2fwloc6C2ReXy9Qzbno3wNeTaNGpw16easR6-_Afe_-ARaMxX4SfaHOEBplHUkDGIWahoEORrf4Kwh7LY5-H8VlpViijJ-mtHOUJLWAx8bY06G7v1DTrXGdUvjFYCoF8WLj5sWx8p0E3lbkFKy6Ck-xY0zuzaXdz1lsGMO_SVnJmT0iMgmywnWwdVX91gAEUIuwk5hyHCEdJZVGH3PFiWfBBu0U8QhMt67laZLi3sLfImb2BASDKH0HPWFTo-znaTQc-xnx7g0FOOdtQ-AHdNkBdVS6ir2dnxzxEl1RFrzR0Oi-uyU0MCqX6ciUiDWAqpubOiETHpKey_dAQSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa37c71dc1.mp4?token=KZK2fwloc6C2ReXy9Qzbno3wNeTaNGpw16easR6-_Afe_-ARaMxX4SfaHOEBplHUkDGIWahoEORrf4Kwh7LY5-H8VlpViijJ-mtHOUJLWAx8bY06G7v1DTrXGdUvjFYCoF8WLj5sWx8p0E3lbkFKy6Ck-xY0zuzaXdz1lsGMO_SVnJmT0iMgmywnWwdVX91gAEUIuwk5hyHCEdJZVGH3PFiWfBBu0U8QhMt67laZLi3sLfImb2BASDKH0HPWFTo-znaTQc-xnx7g0FOOdtQ-AHdNkBdVS6ir2dnxzxEl1RFrzR0Oi-uyU0MCqX6ciUiDWAqpubOiETHpKey_dAQSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
کریس رونالدو: ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30307" target="_blank">📅 21:46 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30306">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibeCbO5FA-m3fiUDjxY0ZSgBco-Q9iIW1SKlYeY3bYCQoH3Owv908etYYZpXH_ks9KURdEJXZ-LW7BLEVTFmvxbJhG94kfKMm8e7gjYUdAHHq6B8RNOQnDVUsBeNoWTBlPpSpfa3wloy8OTRcO2CZLhu2nIy-jxtOOnb18skbDnFTeICT61UKE53I6XTYShlG_LjpfZSXaf_7_QHGcs-dZIzTLF3GX-CgSBxIyw3U0XkVLYszRnSbvkmIYetfpRecq5lJR5CcFlFBsTP5JH1AKEbDCebRXYKmUP5rSB6WWT8lyNRvjh8VY84WYjBrFAhKSXyOGgCNAErdvDf3bXmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بهترین شروع مهاجمان بارسا در تاریخ؛ رافینیا با ثبت ۱۴ گل و ۳ پاس‌گل مجموع ۱۷ مشارکت در گل درفصل ۲۰۲۶ یکی‌ازخفن‌ترین شروع‌های تاریخ بارسا روبه نام خود ثبت کرده و مستقیماً پشت سر شاهکار لئو مسی در فصل ۲۰۱۱ با ۱۸ مشارکت ایستاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30306" target="_blank">📅 21:17 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30305">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oBpx_sxChJZioLaoDnkP-kSxJryItJbXXIiGXGCWd5pmrLNnjtk2tKesM0ARgEugRfyrlskBWtoMoL0zclJ-Pxf_ufDbVlF-VX0-L6ml6_K_6M1ph-SvTmEZ5ppVv7PBKxc-M3BqkBCCYDl0JXOzvK3jIjCRAzx-KUA9EFJt9eW-oz29SKVEvSa8w1cdQ1rUZZwIC0sl0vxq9vcljPftqScre_pDKjfnIyvla9YO0J_e22tnZ4TfP_w2C5CLsSlC4tqRxe4bZGo3kd4a5nuY7kJvmD0DeJ5t0zqPHij874sdbgsBHp87QHiCPf3XzM10UZ__OCNZkv-tuw4TEzogjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو:
ممکنه‌این‌آخرین‌‌فصل حضور من در مستطیل‌ سبز باشم اما تصمیم نهایی رو هنوز نگرفته ام. اگه شرایط همون چیزی باشه که خودم میخوام ممکنه در مستطیل سبز باقی میمونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30305" target="_blank">📅 20:58 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30304">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
موزیک‌ویدیوجدید ابوطالب حسینی با بیت کاگان منتشر شد. خیلی‌خوب‌میخونه لامصب حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30304" target="_blank">📅 20:48 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30303">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=n0CoJWE4hyhHECx--Yuu1NDJDMM6-Ivye9n8MrdT5oIIJESuXMLdUegNbB5fldljHmgNvR812XEx3aNuetef0tsYJbC-HZHOOfmzE6QovelZe_qdgthf7-GOgJWLNBLQZmf80Bpcq9UwLCd3skGOFmHaMr3cAkQ1gjB2nYu_fGyJeKWN3exS0YiySS8ZbckgROIvV9c6G1puztFk9n7X9QLuhq8QPwJB4eKiuyzyczOo199-lfZaYAp0boIK4_BjiKPAexQxljzI7199j8I-Av2pr8s3f8WnIeR_1wNMTEhwt17-U2853UUVTknXvki6EbE8xp3_fGgfn5nyd3vqnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e4918be83.mp4?token=n0CoJWE4hyhHECx--Yuu1NDJDMM6-Ivye9n8MrdT5oIIJESuXMLdUegNbB5fldljHmgNvR812XEx3aNuetef0tsYJbC-HZHOOfmzE6QovelZe_qdgthf7-GOgJWLNBLQZmf80Bpcq9UwLCd3skGOFmHaMr3cAkQ1gjB2nYu_fGyJeKWN3exS0YiySS8ZbckgROIvV9c6G1puztFk9n7X9QLuhq8QPwJB4eKiuyzyczOo199-lfZaYAp0boIK4_BjiKPAexQxljzI7199j8I-Av2pr8s3f8WnIeR_1wNMTEhwt17-U2853UUVTknXvki6EbE8xp3_fGgfn5nyd3vqnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه10دیدار اخیر ایران و ازبکستان در تمامی رقابت ها؛ تیم ملی ایران فردا و از ساعت 17:30 در دیداری تدارکاتی به مصاف ازبکستان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30303" target="_blank">📅 20:39 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30302">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=aVMfpnvlicAuHRvudklcyeFMVd7OPMhZZzH7-10tHVvjgB0t4DKfGT9Q3SEqmJJGRy4y9WzMJlkeiYsi1MWz2nEoVeOS0RHzS5jVcOOE7z_O_hJSw02JKvYJ83vRRAUWmgeJFDBLICoSICppMUKSbztv4s-8b5h_AhwSNIefhCsXLTm160HS6g2Gh1ms2PhmGWKfPMSSctiYcVyJbiezVL8LSJKXdlF9zMOQRYnLJ-p03C3q5iwQ_f3WyzpL-OQEup5xq_PKf1a5ttseYI9wSS9xwiMeTbQQdxMnR9LkjtSBzbRWVC2yh2VoGjx3WaMCZrISxLLthMLOXY72Lcs6-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecddff57.mp4?token=aVMfpnvlicAuHRvudklcyeFMVd7OPMhZZzH7-10tHVvjgB0t4DKfGT9Q3SEqmJJGRy4y9WzMJlkeiYsi1MWz2nEoVeOS0RHzS5jVcOOE7z_O_hJSw02JKvYJ83vRRAUWmgeJFDBLICoSICppMUKSbztv4s-8b5h_AhwSNIefhCsXLTm160HS6g2Gh1ms2PhmGWKfPMSSctiYcVyJbiezVL8LSJKXdlF9zMOQRYnLJ-p03C3q5iwQ_f3WyzpL-OQEup5xq_PKf1a5ttseYI9wSS9xwiMeTbQQdxMnR9LkjtSBzbRWVC2yh2VoGjx3WaMCZrISxLLthMLOXY72Lcs6-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطره مهدی مهدوی کیا از قرارداد یک میلیون پوندی اش با تاتنهام که بخاطر سربازی او لغو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30302" target="_blank">📅 20:11 · 01 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30301">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjgsasu4nQsTk-ae3zqlFzmhqIPN8FGzE4tbb2PQhjNpmkKq3BsMpEZ2Ctmi1RTMetqp7S2-VUYw8GNqtWl7sDLJrTybSUkP9o4Qx4QQbWxwAVzNkmjzkGrdanegeyhN4OSsNWHL0WGfnkVJ0vKX-tFK9ehzARL3w4Y07OJFkmGWnewR5aEmBenbsM3Px4RAfpj2BTvAu-AxsOCn25qye_y9LzIJD6MnfJ2yCN5_gLllcdDlsq9N6u01IPJX4o4QQdQ835GLg5BK1oO5-AzBmxFp66s124MXxiZlrBrLsiXyob1rgG8eAjzOh14njmWPw16jkij4LM3JdHB6Gz1vLYA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe814a720.mp4?token=IDlpA9hUxk0tvs9JtjHVJd38IjKmSaYzgqgL6ybWYBz0oz6s1pCcn6pvOFKTIpwrywtru3cYeAehBqefsc5lV_U7tC0HRbp6Q6LCDZ2z18ZC4G4FnxUrkOhTs5A3ZrxnuXtR21_Yyx2UnPkCtN_UXq-rYFS5mY7ODb9SJB2qNGUQIQIWT8jh_u0hfOzR3VgMWNfmvBS8Q7cB_Kw6VApK6_PQtcSx695e1h2oceTlax4J-G_jvP3roedbx1dJi8oo1zgZpwpsTZgXgttlK6B6n-g_MbVmKjBOFe4_19xSp0W_vy-PCN40KwdnA75qZQIUMxSh8hSmWmuqkG9sKYeZjgsasu4nQsTk-ae3zqlFzmhqIPN8FGzE4tbb2PQhjNpmkKq3BsMpEZ2Ctmi1RTMetqp7S2-VUYw8GNqtWl7sDLJrTybSUkP9o4Qx4QQbWxwAVzNkmjzkGrdanegeyhN4OSsNWHL0WGfnkVJ0vKX-tFK9ehzARL3w4Y07OJFkmGWnewR5aEmBenbsM3Px4RAfpj2BTvAu-AxsOCn25qye_y9LzIJD6MnfJ2yCN5_gLllcdDlsq9N6u01IPJX4o4QQdQ835GLg5BK1oO5-AzBmxFp66s124MXxiZlrBrLsiXyob1rgG8eAjzOh14njmWPw16jkij4LM3JdHB6Gz1vLYA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنالیز دیدار هفته‌قبل دوتیم اتلتیکومادرید و رئال مادرید؛ ژوزه مورینیو به‌این‌شکل‌بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30301" target="_blank">📅 19:54 · 01 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
