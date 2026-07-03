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
<img src="https://cdn4.telesco.pe/file/sY03fOO74UUqHjBwbIYUHnNakDRd_FWvEc3vMxQWpkj93fGTSGMN6vRgHYzTKCR5bZSoPIw45Dcr1iO9XknY9TmLARE62SAylc7G1tQgTTkjPsgZJ7TB9-DrkDfW8ULn3A5SsrC9cijMMOHJ8qRMiYSNOj5P0L58VX2KILWL99yM8BOqIBYqmea4WY-JnYIVUVUW8Pfsz8l1_Cgahn6nF4MRNM_eZu8GV4TvQoiCBs1cs8xGHvObU3hHGWzRDCu2HL421TSTJo16cNhU7Fl4esKuoKTM3yvphoHXKrqxsdmdsxf_H8CvYk_bkmnpMZq0D2t407-vBp2iYBMlr-pLdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 364K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 18:07:48</div>
<hr>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=EWRoVPcJf6sx1wpfACFXUx7Du2ek4Io3MbqAbISc05DiF5m0uae8Ap_59ZC-T-GoZWqQLOJBA6ZZzeygyvoJSv3qjcMWFE6gVR2fsEE8QeUXkJ5H8M9KO62RmK6-R7vYH--zSy2MdOcU5kAnvwyYzJIG8wPMF2ZWSZKM6c-cTJ3hDSmpQQUxZwZ0ZPN6wNoLIdd2ubnxdRUwa8ChbXXwXFIzmbsAhnKSPIBNKxemMXxQ1XeW8c8jr2ddifDhZNpM4U_pX4YBmORrqhKE_kR2ZElHY1WOVhy6AEtnnt1gEyRyKVpwTOvDcSgRdCbJIpqX88a8YqO7L1ky8SS6YxreWDbM7ZKY2gyMti410XKgvIccjhXo12oBxxIHZdEk-5MCCHmvvlt6T3sGFKIFklwXX0S03erjg-tCImFZME7vILBYH_3NYZ-OIdxyCxtElEOBuBiVYZ3MZrpuQ9Nqek8M2BAEtFhjHlx-j8Nl_UCj0SE5bQ_CCT7sgBIcLqaJhApbA0A3se8Q4WXCxjc-7eDHHbqL5cwlkKnmqWcim3X958RJ12nz3k7sTGiFmkf2TEJM1XVw_LpcKs2oI2UdXxnPz9CitO8ZMoNEYBTELZYLr6hUReaL8vT_d4DQ1koGzOfcbzghtq8ZAC2F2iHxJVOgRi19-BT2OfuKbuumRLDg2fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY-UroLZkx0KzP_JwOHpGHwLFNZkBQ_3uxkOsJxW83JfdVllHsH250KxJ0RK0YyRHJlNFzL04RnAA_t3AvoO4sCDPAKUZJobFJIdrUKJoON30XjywATzPEm6kYKe9gzJMaWGBEbGYUUiZ7kN7UwT8BBZO6jyffcMWmhxxyqXmjJJdLBBhHqh9i_So6VSKsP55lYvPE4UjjKkS-BeLc7trUvE_JhntGSE4tmDFvfC5uEzIv0rvitH-V13W8UXrFz7F9UqiiGOaM570eESVltpOotN5dqVb5oPwTmqBolOWaPDllzAde1a8XWHZOXioZ-k6IGKQ4GBZWGBSpkyGxgEyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=gh9hdwss9RTKakFXFKtwSZv2Aew_iuO0qIoXojk9rMUCQH8ZMv5GwxRoxxfu-wkz2LvpQwOXG7WUemwVeB88SXnUEbNA1BqgLH3_7Qc-6VnxVYdpMsBweGyf4rg33FVgvpa4yJaHjRnWb7ozTawM7bfIgQpZFVKaDwmajgPhVVwJUIcwaENFwtsKSlCfQ1OTjh4ic1VhoPGLAUbyS-g-TviLWulXGB8QHaDVhQzZgzF6Orih5oPSDNbON56NgN-1oZqpwYJj0mQe7zV_MtGZHEc3-UAyhVzS3IC7J1rNpkjQxCTKnp0BgclMPlSMFLbEf-2SbY3DvCSBYP5F0drNBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OytFMgiMnjfHsr8cdy75rZ6poEAt1v3ka-BI6Q8G9WRjhhlsIOiFTk5QegOjRYPLHLn1QUfcY7KM3aDSbafV0JUfgOr5XLfbJGsY9Kg8kwGjLZaIQtO42wfr-YpiesaYtwkYxQygD2oy89-MQH2SxNy8R4FuDOm-yJGPdeLNBCzgiQwj-kCXkdqQG8tOWo0wgYtkHPrSyPRn-Ut4G-klaoSJJS64bha2phbk3-nTfckti-bLGaWj6i1t5AgDpUUgUDA5HOmtzHyIPJlBkvMbXvn-HQO6bVoWxU2ELKsqZUMhARrCavBe9QZpbJHQgTNBd4TECXENg_qk6XzqKRA9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=q3ktt_NlaTFhEv6LfnRs5fDyJ24A0yUH3uqZ0lC7oSK1bR5rLPXWC84yRAbGfAiQvPYG0I891UWMCv5Eyb3YcwFwH1cDCLGlNeALZgMpwd1EvW_fm8AAPHIdMoZ_7KnYt4CsPzQSCaDX6Psnyjh6a68qpH3Tm6-r93DQztD3GLsimN26vhDDffjwfq4ZZaZzIw02vm95Y_Sjxh2TeOvl-x2RFN0ShmYjObnkLiaCYQ81G6DME6GYjVN4nHDcDwdFeOQ_zQnv2A5tup5IHFPzVmfaHOpCqXliyO85hjfPqd7aWAgnSPX_-f0QOVgZLjZIxEhJH0y57GunN8LZp544QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/et5SPxGSstU9yMwrVUohOuD81Tge1cyhqLfD-JCNwI6tYnpmxFiZVluFmZlLnEQjv8tJX6YHfE1j130WMaqQ_GXyvoqr8ZM4DuKzJ6rKNBX67AuurZXPVEWm5c7_69krUYmsKxVefWk1HkRF_p2DUJ-xYQIrq1pR63R4_x4I5RCJCqwLrI0ifCvovyVEE6z3ZlEd_-9CJ89KConZV2E31vgErIFzeqG_r9Q4vYZrCFRQpMp_F65IC_S1hLtLPI3pNQ59JXHHzdwWGncnvo4QlLxSQOUeUb2b4_IwRw6Y1wASM_Ru5YVyzggyKZ3_FU-5wF6HUaf-mKnLtZ6FZ-wFTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raw_V3scxhgMPK32d3vGN8DsVKKfyzX5EA1fALNuAMj4i-AaJwXwHaYJz-idojoKf39tGkiRTznG_j9Sf6P8_XmzHP5Y0wxa0HaZ0qOQjEI2pXrY7gJ5YjTg3asqaKhg9Aujpac3iAYUOF8upa0ohqzEKxMPjS6AHQj6pm1Wf6LuMqwqrMlXsf4eBVrcxY7GON04DxE5f18JKKgit4l-QEjDhqXVjubUbTZhkQVR3-u7PVKyeMZumLBjM3ih7e_AHo8oQ10eC_1rVFl-6Yk3pt2bchQGIvepW8O2_RPP0-KsAN8vInLWlHl0Mf4_9QnoL7Qt-J3HwjbCspr5sXJAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzK9tjm8ijbpG3UGBlluBRWppm3mmrM9ij9b_VauIOhYD0gpNSoDbjB5ApRPQwEklaBPZGPj-HZ1fU0CFFNb7iQ9EYsL3V_Oh4sw-cTpZ6BL9-KTgJjrGHeSZQbavhzCP8nzZSW-i1MevaMuU_rLls-yr-2CAu6icIqyrlDu6C-CyZJg3ZAKmAAEJdpTlUgzpCAXqD_BW-MUDFGNlD7wMaojpEk3c4Q-z8KajAFYJn-ty7iwKYcB2OjMJHJKRaIZWfFr90JXooG4UlaceFXQxDX58G1bZ_v1CfQfG6G4No85VOc6VhFLR-HPtm_U16D6VlRFaQI-9LI8N6cOTBPz8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=vL_D0XeqzhxamSp4Ptk0dP-h0ihwgk3DTabnm3uJy6hCIE0uRf8TjdV4jcHQK5qGjcax4NwOxvIYHCiFpHpEw6ReummJd1_-Kcw6fYJlLyFjm7K1bim2L1FNeBsxXWp7Ys8TcTcI2Nb7DEL92OX58zLK1hYtrgz11hDOKyGSHjSsxhiOORvxHKxOJP8E3sc5pHkgXSlFnOYUXzgIZAKMnH_rWCE0Y0kcnDPanhi5XFo4zTgQeeyvGoyGmYBqG5YyRf_P2S81Sa04wIcJ4ULnfyBRXl0v1S2WH-wv5hCck1p17cYF7vnN_BskwC3lBuoAbqRhH9_njwwn7BIOJVc6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcevOrDPKtSbAQ7cHxSHRTzCm81mwmIHs7ZXl9f_GugWj619JQ0U429LbImiNh2DUklhUmTu-Y-WfXKKIRd1J_DiP0p3b-hScCzd2KWdB0aKkwXTQPMYCMvBoox2KSakr2Nu1CELlyC7ieLp03DBynNZj1WnaZetmQ2w1pRpd3bAdGTPsmQcX4TWWVHLrMV72hxYeq5M-DY2fx-Zw0HIsj__2MzFaDjOVP__kEQmK2PfFPyPTcpTg7u3NEbxcTZRV9CvB-uDbt8eeDnDIVT1OEN03n7hvItsY7Hiiig3bnmZnnw61i1yLNWWnw4NtH3LpwcA0iIbOxsKVVALA6mMLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRSl7x7bo8zqZysfbyp0sHOYVG4O2JCxcopm4Y18JoTPhPyKFTR2AoCbfymcY__Fj8wSEC6u_w2XnWsrHGRX2cZ4Qhs3f8yt85WI1nl1d0Tkp3Sz8jRBjnyYVMKWHZSkIyhCtv3-CXXT3rXqVr3pt7alEKekl23Aen3PXnRUXFaMGgZujVTd5QALgBimfRnhlOSbSonqJ9sPpFgrHV8oha2aRRJ0Zy1y5EEIlFqCXSO2N2mCTeU6o5lUrLq-IhdMeoGyMQvthsIXAERvOSlGpcnzbIGs-p5I-DZmNYsWfFixchEtCBzD14ETipYRbBpp0fA65rCZnAXF89xpSoOLNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/py3wHdo2OsPdRRU3hUUWrUKdPYgMthjhG7sC2drsqb5Wk0y3MBkR0Sy0LYkHqOrX2Gqx2l4mI6NUKwXvNbX0YUURY5o2z0z6iIVQbbfNlFovsFoGn1KONpatWI1dZoqEDlikO2YPA3Mzl4p3lwaZNgnAGpkJqDYL5AgAM3V6dl89FmhXfRzoaG0QCVLPJh7G1jP83FUN4tJJfzFy71Ozqtqhk-NIfoSS_3bIxvRVvow2BncjR-X9G_b9dMCktkMIAoTyBHxhNRrQ3HfHCuOBe4-BJB9lRGnP_mTBP9WTdxJWMzjij6cfxtFXbS4Ba4eHqigij0ShZFHo4OAIXNMuFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhqwdVP7f9epjtHbBWvFAFpB3aqept9TLqIwluw54_sohdRd2cxo-bqDJ6sUaI7kuvguC0Ol_OhUWdoXr7P8ZFBSLGZjCWeDZx4iJ5D_lzTlTX9zObBBSCe_PEd4V22KyV_IqbuEo4vX9jltFMymRzvlmxExGNnH0-sUShZxzMBspd3XkeOhTuMEHncFhWxOxoKb6IOC96podfB-K5w9BRrJC2iAzEPoOu8p_4__ji8LdcnBcx5U2Jp_uGItzP9pLCmV_aQsJWSBDSCfER9FA9fIN6kQWkVrRC-cagpj0BeAjj9CEDj9fd0lzhdCYXZQcfZ21j6hQnlw-mF0IWJW9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjhgvK8kvbb6JM22Y_Z_2vsexBlT29RCJndJ70dKo0i2qf-W2-dbgLMaMoyoifUk8VR-LVgLTH0UyKblvaI-XKG36gxQOnKR9R1VZi_zpoR2sgfmWmSWep547fv2lmW73M2DXCIoTNmUY6a-uDWa3N102AXMOyynAtXtsRIjoWd1ncpclzp2DFCTXQPfkRPhx8AMRT4JyxW8ZNpmYBFvi64vvt1YDEBhDZBfHonrWDjyQ5mp_tSe5cQhgkcI7Oclsk3YkMUOJB2SgB9LrkeC_0SFd3KVXXArYD1fJvg2Am2zjETIkoSHvXRA9hQIE3UgHjtOGW8fWJ1tCTh2TlS2Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kJ9vVu8EoXm-GXTXCptmzcGmHc9uCCkBIGqjAHiJ3sBHyvZyThnSjx8oKxnSV-hgGAH2WN0ksVW0PRTuSYgRcQQcTcT4WAmXAUYoD4WBRNIg2mVut9JCIwnc-c-Q8rphNXR-rQT-a02SUfHZS-ZMJYh5f9fKaCQSJ5H2Sa0S9c5G3JrzhmSNFgisKKfpBiXi27X_XbnXHKz3E-i8wxWYyrvJmQKK9kPsI2v9zyDEvslI1sci9GhGqiFi_11-2hLuU2Xitd8oEUc1s9rdhlPsol-pL5Ukx_YDKypaijG3mxwSUcvXPI47qPuVNL2sRXZaIvyfF-I8Hc6erxe_Jiu_3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=W_rJYewke_RRQ8m2Gi07rgGm30Qc7CHVVIP1_1kw5Zrfi_ZzKwB0Ezhww_ZUwox-6pf_lfcdgxrA5c7HC-Bz2DePbXISARl3KxO4Ip3E6O7OBUOUWci5wzCBc2kBaEVL85NzIFIV5gHTKZ8JsBjZ8fA-qN2ZWdO9TS7pyqi-D3qRhTdwDW84JVdqzIa_vTBqNWBodABj_A5ULRT6h--qyhXJaekQ7WzaVr-a8XhtPV2Zcimc48yyoL-RCon9Z8X2rsNG52xXV0t_u6b864yqmOVZzm-5i8K9GLCddqh64quFxlBYsPb94RP7RT-gxfQMoCmTErcYtV0YlHbVsDTg0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=v0WWt1U_w8izlAU84P8NRqHfAESVs6NoV7HwID9kMmWHEv-zc5NeWr7OuO4HVOSoWqn21mzpwECihsWnwZFTSZ-xyTw0hxPryss65AqVLWvPUozSWil-94xiJlBFwWOK486I9Ktmc9LIw1dcFFqbFaNdjNwHJQv5s59YpRy7G4RG-dXSa8LirQFd3tS7vjTvxooiNsyVatpvyD670ASAomRkwMPBwVdvfnsX9SOD_gGF1Lc4whoHwZXSx-Aq_zhs23OlT73ahkzC0lYL0FgOTbc4kMEPNa3ZAthwRxgpS1BNxcFyJcTuO3MVJzqOJwLkwXp6RzQZPb6KPo9C_f_TOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B42rBsp0JGdN3eNIHIjf-4iCU0YjrLWXw8_Oh4zVW0U6mNxRU0uB2_ZjASmSA_gB9CPfaPJ15nMFe1Pqi6lG0robeF2cmCSMMYhcM2MIn0MuGNT6gY5oAMuTsxTlucBRJmcUuoh7oW4D6CcjCHd5X6caSRNk4skWGZVtlOfjKCRhfZqY41OEdSIKqESZvG8UAn8y4812_b17MlbuQSd_yLuHCd8Km2fJM7rDr6zL9Ql-ltk2MGEVBH16suyzn6U16bxaC-Obc_vTnBDb_R3lmy8XvkHnjfNGlDT0NmcXYrKudm2qFAYZojHEosXWDHaKa0ZGRTAk3uNJNc8am916NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C63g1KuXvvgGV83-iDi5n5V2P23NUgxW7tRFs_YCWTeWnLUFB2HItaIt0X5KB0z8-hB8h7a7QSTQ6XYAfgv21oCQLiA7wllc6iQBTsjPx7z8THaUxlubuTGQROfnxV6UzJ90rXblIEwps2bMv24RrtB4N3SqDSfYBWqGHpNjJMuWchn4DjfffvAl_MbhbhbKaot7WInvhJCWmLPbiL1zdfOsnfwLzzfYgFKpy2UPRiGKaymZ4Fz7w49WkDPbpMeLGgweO3WXc_kC657a0IxC1RsjsIwY1sK0w63K-0hDPcEuilOnfkkMc2mnt9e4ja0Nnk8ytCYiGJQslKuHNG_Wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=LX7C0Abx0G3VvMRx5gDxIFBuCnMVPaO-VLX8WxXoI8hfeN73zTiwgP566ZnGt4cs1W65lrX9nI0xD4_-TXX3AbJi833LGFfqwFXqhuTY9NaSMnmBXXeI8ZYP-8mVn8w0ufG3EPnejt3rgvJ__GSAOU5sec1iXwvttbjE16GaQP4nOqpOvq3HZA8bEgM1nA_me2jbUOhxPzUK9wGpzClV5hWXbovA_5SImkH_8GmmDz0OpVnHh3CNFRHZfD-uXokh_4hPD84J4JMKE4UWg3be2PkQQvFsrfN8Gzo1S5orc3Zsz2q_Smhdke0xrKNeMSvHld0Lq3xEFYVbSxFzAtcEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bs-bB-wbG886vxUiT4ddDtEmbkzU36vAn-BsD-jD1BrZaE-LiXAqYQWZLsJtomGF-IuMq5eD4uRqSaC0GypLK4MPVM_UuSgLo843QHj4CiVn9fNDlRp0jVcnBOL9zraeP4t0y9M4AViUH6c4OndjTVPpQWgYgu2D5ZL-LpBOe2ge6y_ekCjraEoYZIU5j8etPIbzlZVkvfNPbF7JWBXAmFKIDC6qVpXCqBkn2Ae9K_bDNVe_xt_8P7786YjLWAEdq68kaIRWQdd9pBtY1guvtp7sAGLryqg0AB-DCmKtw0zyzmDCNfPpMa8vgFwmiFp64_mxLN1Myfq2nAa-MdJ11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZJH_DdQV4R3BEI8f_1c4yrnsa5qB31rX1HyE7fkniEJQ6fQKlrbE_TaFIREJ30Qz0r2Y7d5dWByGLkLqJQoylJ_FgBpRQSnmI6bEhGrVT1O7mgYHJ6dz8WwIYwDfjEpqkcIPdafPfAvgRdnEoLzpypdikcT-sL6vo-mtPOrYDJ48rJtJCtrr_LHPO2iivrlvARE23qmWF7Hi4JacLowz0mnDW9_Qp1d60vRaVD1v62rFJReWKhbNqAt9R8v9yEO2ERZ1Gnx18XxJNghro0MB_V5-bbMAun74lT2_W3wFpYg5VCO2WWQeRWALRkVhL2VVTBvOHB3ZLv-9KdOI4cu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vGCZjKyBcg_Gdd0KFk0souB46flbXx1E-9W4LF-B2DaDMD98BtxQn8qu2isPz0pw4Wn5NpaVFP12k5hzm25YUXIT2453OQYS-oHRsefl1rnmu4Cg21fIKpkFyw_dyer66TckgHJefogBHxPuf9cHJlLVuX39DaijvwSA3VeWfnNy8wyO1e-qajdGt55O9kI-ieq6RP9S1c2vGuKuxW6VEzOUsHASkqtv1PGDmWftVv6MlL6Yf7n8bfJnjzaAA5PMh2sjW2cD4EDjYlQBak8CYxTQC_RgcbxP6ONEazzEQO-799P6o4ofgpUZ26D2IKPz-Wt50WDfJvuBzeeu_zlQlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fr7U3ar2gEYMgYUr2F_9mu8gby5XQlnE4KRXeS3XnOniyMt0_Hj-JIc649u7A8GgPtN_joEn1GkFkeo3EvdhD83iFSIRu3RKwajk7WI4TMNqeFfjNR8Mdm10M8K_WWbmFb4Hqdozhed1P_VA-ykY3h5SysRck9gl8Tzf0FouCImGlh7lxZUb7vOSr9HEJmP1AV_K05hxPjZMvuFio4p28eFSkUzOwgAPyTsogZQ2v76v-m7cRO_sedEwHaeLr5AuUfQphQjQjDgZzrsG_lyG2pE1RuNF4x9HuHSmfeM7S5_faskIS4x2SWSW85IRyRbWGK1oiJTdO6du_EzQUc4bCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=PgTy1PR91JDNTIGH7jpwM4_aVrbI4fogBlabGGxqSiZEE_GuVPhZnp2EcPhEZG5H0h98aoSYc8mpFs6_IuAeawmr7B-2hFoKpxkFcpsTxu5IfTvEiJMV4zk7GvjNuytsVERhtkn--KOUIXOFMcFm-TCZVFr8Pxs_WgioUyoue_smPME49KRGESjjMmd3bd2Pkv8BUrMqI5VLl3Je0YNw4_F7QTMBszPFvWi1ClZdriCDXJa1jyWWphUrxXYVQKHlXDZ8xrS9sEPHqM7r5Y-KsTudKkinzzB67Q4o7XBd-OjJZYzSOTSYZtUGQBy0u-44-cZaro7gjeITBZefx-TLSEYlIMXlUyVlUcmWWsHKzu9F17QuFbHIhkSTQLyoxGK3MjEXyvXINuc3VHxuOvRLQMjeYjHW4H_wIObxUIUYkXT754vpE8A08tgA1krwf0ANy25CJ93KWZmWIgiDHzhYV1y53Xa3Vl-OmbCF1gtFl22PuG2k1S_feoVECfizfO19Jo7tfqnZ4A90-9Lod4K-0ER5qCP-HeeMPvcAKYAriQC5RZu1bzoT4K5ZcB6OPOyhNHEXpDwnp5VnsBoXfeICmmq6BjOSkm5TW4hSTj-80myyC-yxLk7LnFUdkaukDhzBRjAt33FAjzzE06T_8m5yyoALHoIW90LDX59rRSI0RKY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqhZU6uHNZm2T1QY8glJbp5e2ury-RwlfvCdAebu4WroGSm_SW4FZs0HSiVdZ11fIrI4RxPN4byPr0V05_gcfIewDSN8CGAxGCN7PiLX6YTZk-SFVOvDy57wJnR2CNNfuQj9E_-2EUO_5e3FgM0KEDWlZfl3Lk8zrZpWU63vjf2NmphqwXUqzEOZFk1VaH9qtHeEpeoDaWZB0OMFlNXDiy0-qtV96dAOZafcgLJUKZWZFNKIKFlZV3cL69xwthWJq1e89pxSG3sOI3P9wF_lkEql4_pjc1tiUCg-EnCm0qO3THcJEa1J_H1Lbj47ixqvYg6ZfZWGgTJ3NpvejX4euw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anbSbDZktwwjSk6fK6Tbjpk7ZvTr25LzIuUTsMbFZVKyB_ffy6CnRn9mSOLP408mzumr1Y7-CC22VkNpZBHPbE7UQarrA5nYHNFXBc8iJL5kkynZc_HH5VCD8sLXoOX-eoc7hT0pFXBiRCib7dLY48Z3HdyKO7AzwXwlwXp-sLjAry1dnRCoI9ZLnbHJ_BF7SpWNwEuUjQukizbnO5u5tV0tYbZ2778R2yridNBLzRycgKLuMzx5hVLU-NFPXQiL6TRgRTmx4lLNWgHhCE1Wjlu-IFIgZbnhwoTUtvSBbYz9M75kgqkFhELQ-MWR9mkq9I2yVGLb7ZXsx-39NDzd7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swlr9SIaCrOQF4UWOreEPwTOScGoYV4mfQplUWCmdAG6kmQY5eEdMQO6EcTpGBPtJ-LC0PbaHxOE0FFlLD6gZPaug1g_y3p6fCc3bUR8GXZZeGlYEDKyVURd60m_574EXzCtIjmzJViOTvUQTDRAN2IcQ9Cni8joMovyvkK9omDEfPa5O2ot-vLUeHbOkXIkGCLs5XRFxi1QZRPvmQOaGv-NKOnrO3jsY75pfVrJjaSHbs_VpeywgFRrd0nNI1M8r_MWo3BRBJD5UJ9iwIGxL8w8nl4b092Ac4suMa7QNAWbV3ad-oLPXb_06FOQ6uVHMCijc-v58qzAOyRJ-uJJ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSszuRasUzDwaXcd5rvbUBMJnSKuIA2bWq4gT-H1VwRo8-y-G29EYc7KrFI-6SgFg2RKNakwr4IudiMMCP2c7b5XE_9EzZ2HV0gD69655uaZX-svIZRh2fe90STIjQ39OvpjoDP5HVsjWUD94_3CyaneU-aXpSBZHw1uh4LV8EvcB8-z6Gkp3xBUsaFBVwwgaU_f_kNXBhwImluhHW2PA0ldOfPuplZRpLGhS9z6WaPJTQBHqwbTmaux5CxwlM2cB1GO2M6v71Xqg1mC-p_lcXH6zPljGQ_giumfqwkWfq8ijVpG2IoHFPJ-toZIqHx_uOsGrlDN-NtyKP1Ft3Bukg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rhlfyFN4w5VNZgcNv_nLHkhFxVRbdMgnqiOEM7nIeaCEQ3Cci3QD7dm0GasCFY2aQmRVlnEe3AJ4fXT7cZOgakLWFC8HsLGa8blwNpQy0Kbe-0Ikw3eFSUyo8gbwe2XkDfBcS-d0ubhEYyDetCpvuqNrfi2Zrkv2g67J7bW4iyBEm_Hbityw5pTkMxiMRnDOaDtjD1Ku96DkYQUXTuTqKG3BOfvJHgy32djmyK9HDLA6wDRM0JzpkjhboOA0i0K1t-F3cWWj_rTijwP99Ld86_GAmkE8XaQEnrcyZT9CGziC2NHi9ZpA6fM4niYV7fVIKjgrjBk8RsMhv6GmIB39kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7obYrE9QaPA8RHXYJoXsFBK-cZsli6iNpfGOwgcp_4EZcJRPpTvKek-VAif5d9VdeMo2uy1GSabKi4AdKfRLQdZIa1FZqG7tmrJpd1BQUkNCuaZvMPC05kFfhdtqrk13QeAoEwlh6VmGhgMv88CN7o6ZhG8ATjpcN3AjjS4ePWk9vsheMF6YIo1mtkBBtljSXHiiPh62iUdVnkAngYkqwtwz3nqC_I6AZtv1T1d73uwoUBxzfVJJRD1iDCVsUTxpHlQNlRlI6YNbPpcNdqGuZzDlha47k4ZocaMSUB6aC70mW8v9ZuoKGIbGXNdaHyfC379ndgkNy4jxpP4OHlg3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJBVsizyo42xLXzA_UQpkcTB2bRySIkRoEiyk-XOzuXQ6xQbv5EfdsxIRG16UccVKT2T64T6mqFSPF37NbpjoFGV1vFLKopxO3Bi62P9B3cfyVpi8U9hpqrHmOd1DjQMw0Q499hAUgyZeHQvHzg747Cd1tQorkSR0goQWs_CjCj63tBhdHdqKZ9N2IOx0UERAuVWgG1zpaRfRb5ZRXmNW9eoFKF8vE44Z1rjnt_kAMHw3QR4Qwx3F3pLjvdCw-x9qG1H-huWRlghLuhQ9mEBG6v56Ye0RJuwbk2HUmdWL9T8ySkYQ33fVv-HRiEhnSMxX0F5DFoTU7WEozjcucKCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IveLVxIkRFWqDIHcD9BdEkyYDSRARR0MMCoHVPZhoNhlYi2rv8bdBY8PG6z0MD743krKlna4GizF9AZ7YBWMtlldR1K77Yl8tLMXo3Wu0Wyj1KehMIRfnnQzRMrD9yJq7_V-0dEnBoji5FcztB4ZeQLa6fO3dAfpZccrlI7tQgMEPsff_03AehPznD56mQ9bjdCMaWHnkNa3j4ni57YwId9o3Nt27j0LqlMJvvb_PT82sYTgYmB-HkHRduqmpaWJ6DwLUTJJUdVUC_BacjF7wRainrZ_rIiR41PtkPBP-Mvre_ZNerlquqhZyMDWqj-LUl4IPUJfotGLy5-jW-WkXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHah2uFci7llZOIWj9PGWnNCytB5gMh4A9tdypyRm6dkR4pBSmAtdi1VwThcoG-707ZjpbdJeB2h8ty5eDLL7eyu0WFn0Y1pqSmymcX3t-s5LCcyuuUts1YXt9XOR1sqcXi_TF2mIQhit-ZVSsro6uav6BC6KItXm2Bf1EcvWGo_Q6lK_QIcyYSAiuLZUAhSfD1a01y8CDIFBY0sZWAd4NZ1ZOWQBDjiHmufnbAlKdNnLnXUguzynnAQmd4r8-1Uvp_X8MO71xNgdWm2VMEwO3uvh8GGHWruF6d65rBgKp780_4AGVQCOxW00uKpl0LtTNHJu4s1oYVeHWnsP59RUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpMUbnRPxeADhStYJHPn0kzoveY0QRLt9yq5jK_F_vDKCF5JT9nwgM_pNwezEbOEwnpdY0oIl1LmfVe5EGyM5ItSIomYDyNzOsR2I9GNv8HZrnePCRT40pnRIibVf1O9tDYqlvwYhxNDo3T4jX5RGL7gGPlIicL5nQPGBtMwHPf4ofSOBtcMpdJ2RrPi9tzRbyJ4xkhoVTjPRLlYw1jwA3AIF6HgSgANQgNAUMAwxSMkLiTTEyknRcXt1rTboB-UQ9XQ3WUMzFEwi5NeIov73mPpzuhJW2gz4dGcijxhlHxh7jnm7mtmQy0LqnF8tGzTfk-LBnNmxBGqZnZGDH2SMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urla1w1cbqsinJtWVP2WnUeFHeZ6GSya3qqcC12mrnBU8Z5UQC4lgL1GfECPwlVajP1QRt0-Hpz-xzzQmUMUP00PWrW7i3OG_foQSvYphUcaKL3UcypjvH6YWNtAj-xDFFT1R_ie_yaTpyoglCbBdyOM28MAon5diwkAGk8hFjGYNBXDhgPyCfDS5xGXbenOLQKxdlgui0rCNZ6X1vPfUm5sXD7RQw3ZwehDi4zxhrOHQzX6gZ3KGX9plPmQ-A3XdT7Ewg7TovbNEkH8cj_wth90SFLRAOLiRqC1Izbm72EROtamRmm_hujM0Gpc8YosxLmkvfeBIrmqGMsVwRXPwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=iIYJCijMXqZ2llf6vtlAI-bpYf7shZ5LP813XguGTPLRqEV2KhceEbN099D9YSzMGLy8e8JDHWmNQIXpeJwPGHM66DMgX97YDIcVMrOMpW5OjRkdxz2ZokDYkogzjM5xmEHpfIucFXz07TvdDp5wNrlzDe2GHMFFXGSwP2ulzjoOt8WdBMiba3_zWk-Ep-56n0PBPE35hPXKVaApC3ZLLQgiUphk-jm8SrwyN_h8fVRI1oAWfvI7BQ0S9TDokcm2ZF05yoRTMEXspN0S9EBSFLTnD058m4ZSHZhcsqRDP9xpWcGHb7n1SmJYxTYOweFhfYi1DTiuJnv0G38_mE4YUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFIaev2IFnXMFqSafUiyhvBLbrEZmHi4z43PVwVP9wmtLfyPWLFPgnZt1ijqVqIgA_irwLjQBH73LVCLbj1WOomeoo8xWXWrhBd6j6uamAX6FrRtF5kfNYAeuBrksJeyWN1z7DZIoR2by_384f3nV5ZzuD4Phuz9q0nG50HLC_K4c1pRfH5MfBIcHnEkF8wUw7MZtrCRaa-rnX2jlVwEVntDlOfgqTNW4sIFSD2RwbFhnso16nAboJYLCqzoO7OJO6Uc0MolcImyny6IOI127QE5pHW2aJ4RDCJM7111jNrXqTsSyAAV7El3YTFiD9_jEo5B89lFMI0D6CJteeqwdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=MJWl1-dQfea6Qs6m8fWMSyWS-X-8dp8Srsf6P4evrX0_n4O3o1TYGHPm36paerYupdci8NxdA91LAqzd_Et-9f88GaTsFCSZbTAUk46VLrg7Sptau45vRCHbWIGxVGRqtVomLlwJ6OO-UQtr65BuDRTsD8qRw6mWrrkhtIWwzHZBWq7GKkkHOtJ_BRyMNXTCM8IXyy29dHk_aJUvnO3ET_UrfgRjRKwH_Q0Pz3xoZ1WdInbF69Gn2Tqvey12RfgoA-78gFGtklBe6qSIz7tNIyKMAmGQu46D4EGFJzkDSrAE7G00ObfdOsm6sgZaU8fxkkaSIKcnbBdDch1FLYxVTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=MJWl1-dQfea6Qs6m8fWMSyWS-X-8dp8Srsf6P4evrX0_n4O3o1TYGHPm36paerYupdci8NxdA91LAqzd_Et-9f88GaTsFCSZbTAUk46VLrg7Sptau45vRCHbWIGxVGRqtVomLlwJ6OO-UQtr65BuDRTsD8qRw6mWrrkhtIWwzHZBWq7GKkkHOtJ_BRyMNXTCM8IXyy29dHk_aJUvnO3ET_UrfgRjRKwH_Q0Pz3xoZ1WdInbF69Gn2Tqvey12RfgoA-78gFGtklBe6qSIz7tNIyKMAmGQu46D4EGFJzkDSrAE7G00ObfdOsm6sgZaU8fxkkaSIKcnbBdDch1FLYxVTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK_HfSTVVhI_MDs73deT5snmT2vB5wVxa0R60_axxqlsg-PTdLHnzdpIBjrW2uHksQw57y2AloK3H-3gcUi6OB-yxXqUJ-_Y2PV6hXZK_w6bDCvyhEmzskUImssvrhxzukQQTJYuMYhP1YEPgVAur6BRomL0GCvDvZYKr0RbdeOZWYT9blMndqc1Suw4vwEyUuPz2YVRga9Q_Bv1TAfK-wGbGqmV3D_AplpLUjsdXlj5HZ6g8cdZdoLtl9vO3f2DImM-ymalr4Q0XAc6HemHnF-oi_XXH-Lq2GdJHiShZDFLqR1WUw3FzeSi_xTU14GUVNM3PhvKNYytiId77szitw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvnP3TbPIKGfn55KonGhMOkYespjZj_0uirOO_oLMleKBB8jNJ3tp-Viah299LaOebIXs6Mwqnfv5s1ml9uVnlXT7u4bS2ntgAeyGKp4SilkQq8_w3lC77SJb0YZXvhWFuVgkFTu3uQPA6RRBl6wv7G0HqhSYtner5DVsE-5ecTrRD3sFBBK1R0pC0_VTj_qf25mkJ5o37t3CwRn2_bTONBWDo4TEcTc-iB4nra8xAeS4c-FUE-4IH0Ki-SoPmONb8w_3FyH1XTdlu23z8y3SU4BiGxI8d1NNBAy63gneBNyhDvVs6aUmiW58bYaviF8iB-biPhAWWFEzj5KKGfMpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdB-I0YVe5p7hQMHTM0GARecNw96Du1NRy9XVtMdYhwJeKBZX_-LAPNvcXaZSfVQxKf6i3xEaZNncowFAq-C2FCMjoHsMPDy_Tbtmb_ehwj1gML6bqjRgUyzcB5V54VrO0XiURD1faSaLqHpy8pEl4pUiiGhih7IF-hGk3lt9rRAWMzhl-ZcgXFt33krifMPdjS_uGuVZt1LrH9l2FyorNf0mgQfLM5YRW6Ki6sJVgBbGtkhQMhFW76zO2lyxQJ8h4KTB9YB1Rq4OK1nbdmoC7OYauuvTkr_DN_vyrJxBFQUMIIrMaMBSK8TZlwsMQx14G-yGngtewyQaNRLEX2oeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24821">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtDRFVBi9ijMOGpe82BCFVaihCi_UogxchFj78rB_b7oyyOlky65f7HKxt1jtQ-LWZ2V5EhrOtW3iOm5931juyUKvqksN_6GV_0IylZ5_BT09_93aL3hRPbv3DYTFbWd3YfEfq2UxpRY-Vuv025VxdShVUvV3gTNFIaxMuMMyULBb-wVkDxBU2P7rGzpBw4nx5nHDEsT_S-8TWKcm48LQBNDPsKkOvFV9I8LrcVJDqepnVBbuLMhuNdkv1myK2Xqtog7obXXWhWVCQh2RAo2CkVhqA4-G5mFkKIqdyK_RcWyvcZ8Qf7COCU7GRoy_nqdnTTuRWpkvdV3GtvxoF_tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24821" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q85NlLDtW_zhNr9x5K67OWMN0L0YSl-btSHr8X0IiCKOM5ve3x8A_gvBMiC6mgXmey6ARapTxmI8sSURPkmodz7EstXT9mTtIMuZNagLZHkRvXrhR7EFiyiWv8N8j1xaAZDzWLF7qLFdFbEHUm3B9Fnlu8WRMiF67iLpOgwbE2RVOU8p5Iq3y-Z_Pciwq2UCcnZnfnMWkfvPTkHdWMLV5SrGYKGdVAuRgry67fm3OyeK_dsg7-J2OCF3PxdhvSo7z7XxjP7GN25PkkfdvFGoMWVpnP8MVH9rK5oWbXNexdj9QR8DmCR4VTppzJQQuE2nd2fv8Ml4l7-BqQiAiCKZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZpKeVy7XaRhqAEyWL2NmkGrjmw9yWmAneX5asjR_wOZVBfyjNVPZT5bu2345443xtOnq2W6MI_un2vkjrJHpVRxcBUKPvwSK3joL2tRehgW9J2JfNB2MmD3PfWrvv2gHn1_66wafqDAN-KEWRGIy07KpFaarLS0tGbluWnQuSJ0by1LbKplr4bCJMLZHeVqGZU2NUn7uLo_7xeV_Mu1bovB_sGfydMh22eVy2svOljyyxE0pDCOE2OQbJlvJFF0E7zW1cAIbVl-GFkiD9voZGUcWQqH8s2Y414gKroARcnGm13DRei1K2z-TUpn3w0wZ4_3Ou1F49Hmtk1N4pzUELg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LBwskA7v98LwozgAKSm2cyLf9_69E9aNFbSvDGIB00Y0JP4YICHLezwexQzGWk-5vJKQuCKI32mxQAbVIGMrs0j70RovVMNRoXMjbsV6p6AlCwHRSSx4Bb3IAOVe0fdewyxasILsBhG1Cx4rf7054Faoaj2IQqrMzTK34tMBmW-GUgLSejD9oGiMl3yn_mgGtlCSJOPehv0gSu70c7fO3K1df-55Roz_cUnQcmFRmHo8CPtFzOnf5-egWU3RSwIh--uZIw1DbFUcE3edbVjKKflXIvdDi0GYXbX2R2v_IeDGoabmZVWPbDtO71ZNRYj4IG1AMZPIug1ht0kAxvr4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QwFZJnVoUOLuntQw8epm36Cd7aFwn9TK8KLrPNOvJqZZoukRg5SXtTpH9FWq1SOKjpTxnSVOWk2VfKEY0MwgqWDRNFJQ87SMSZ3jLrAccdP9irDvHrDlxeLuHJ20W_3lY2PwZPd9RX6dsFJyCBW0VoRb2qDobX67qcpZ_X4KgIB1aPU6PEe9X8y3gOWnZwT5cLKrmO6Xpie5lu8SMdHeC-wRaJy9Zmm70Nw0Eel_7A-2_82jyfpfT_drFCqYv2zXBYeVVYb9KrBBbr-RmR0v-oV7Pwhk8agzvkqvvoZaSWi4dIz3BrQVe8ldtewoX1Vo1-_Vl2dGHz2HMaBEPo2Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TkQ9Dl2SQsI39-KChvfrx5CPMexZpTEKVq0XmJ3mGZ05I9IsTfUGkZpTwocYdvUEdVpyOqiFr5ZttV29qsqbBeH-FQFoBkg1m1rERSxqtsCMzfiU0wPnrEt1tTM8vSec5zbEF9X1X037PsiV2pl7OzutpR2nfP6-BNyOPmUhWVm9WLcgoEcOd37wzdf-qLosHlyeR1vG-lPD5MlpeWw0AxYtS1Cu9uiAAu-XTjFMRBqImgnr7nq--1IJyJRJQg0QifchFxwYRgQFOdQ07zHPnUk4ssJsg4K8BHIN1E594wkrQ3rrCaC4pSKDXUnBzPKzn3IPANf4JU715hUTa2Z1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QioJObC3iHI_495XsiB2KZb9WOUdNyq4IPqhJxidDbu7YmvPOXiX9ve9173woQt89UKYXT9bBaObf9ArOi61adya2pM6VVtAvW35JFGYNtLd-rstc_ZWbSmQeLkLwdG-picPLoPf0-dlNKf6XFQocQHdcrNakt1d8qzkiT933P8rmjmO5KYMarFwzeFKk4S4xpa_-EAYFyjXBFQ4g-BJDA8IPGH5YKp2m4ljSdp8IBMkoHVerD2g_4BLNYe7XnUKA5zUHLpWJt9nx3YjXbSak7vXuuQ77lSW_F59ibwtQpwxRVIfYIh9NLa23WJYZI202p7r4EkuddjiWH2CvCgu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-DDvmgC45e01SQPfFQqZJ4Pc33-lXeSLcqQjSzd5ShZhB_uvfRegt4FC4bwYex0ENL1KznOCbI5-H5rzkDb9bUkiSfQ13FjjyqoXJyE09yT6aq7rUpi-Rp6c2X4p_Ss-kZSMSyIFSyV9tET4lObLcMfATXIgAnFi-YJue7XCRJbRCdM8QQU9_GgNB5Ve47FiHbPiR08sBJoOySygZdzqU2WQK4qfcae0_UdGStQaB4sRw5W_6JIEzCS1kDNxOLiQapZeGUqXa_Y6QtYiA1uVSGyNcQvZgQmpa33qD7PXR1MYlNMOM2XdeNUK310WKTbWD3EBPp7THbqe46WoUyW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T13US7LsGVhMkubU_Lr4TH9_aOMHEd5xxzRhpVmVXAHEDcH0xmPKfJE-N45xPwjjlJhMHZK5-Ug3Jc0uPXjE9QmBNHctcDJFZaGmv1CbBshxhC0IoNn3VMoY0I45nZtSN_Wth9jEpHIAu_dGUDiVglEvFW4r6X5tEWBYW8GE4MxLd-5ljYJhZaOvP7CY-SCyibY-pc4UIXthn9NTYEdyaeboBXcOEpTrIiouyzVV5GB-tcp-ff8YIwjqcXQVi97qfGxrVaJDIfObXaermJ2JHBs7TrM7PMAJ6GzZu6yONUfKfWVt87mEElphj98UgrMAOfsO9vo2-DWI8n0Su0Bn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q999psRSudkRJR1kdMvRcHNd23DfV3RCXX0eABKxOB4hVVeDfzkyThb8lGlVt-1P1_lVPuqyYCGgEj87Zb6JlRk3qWx-1kVcENR5KcffegOH9MW-jjKlyq9IBTrIlHdCD6_T80XmqLOFEfG6l4rsWqeFuWW5LJWhYKPQVuxS1uy606NG84udkCV2e4I5CI70SHOakF4pmHGLkEa9mweLyVUEw-7Om-yFiVvTtZt29P3nXbmNv1tqEsbZI7z5R2d8wsWimetRUYgeJaiSAVfW2JG_HOsQWuFYUpFiq0HJCtSisRX6N2guA4Fijcfb0ojfUMEFZQzN3GULUZ7l51nllA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXVgItI3ENZiRAXJUOA60hlzaVJ67flRHUJx-sBm8p8WdaD-qe_gFD-cuFfTLA1ZMyYesJVl4HvuFgeTxLcFQ26i0_h2qh_A2v319qZpY_C_ZSAnnPHO6uushHr8he3HpZUZQCmz5Hnspuch4KI5PPY_pdWp5ScgsNo4CLrqXF5CfbOW2JIl5tBYb-A6LcDibSE28ZEc9puPev-grbX_KlxnVc2PqTrLYhXIEPdZDP9tsIQjnJlvmVGLvbBcajxSQMjC3HiraP1MWWtyMMGJi5-hAm1wOjvs-Rgtij-nrjtrIzDoUUpUwoT2SfzYmKiI0Z7GsFEqoH7erxJ4I7-f9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE6kgerUyqXhu7LEd5Z0pfOnBzKTk-qsnVBZm9KQvJACbnfV4z_P0-mz5uhXhK17K1GBmye3Q2ZqApQB-duyGktS-R_-uEBS36HvserEISyA6QTwQUDxIS8xd9DYJWeYLeEPkc38bc08qosa1fmsDy3akoTku0CW2I2maAcykM2HRKttQUn4PXPvz9yOALx9OqTYiAdDYkitqm7sUvTnAuffYmtYoM-SGU-cYWb-YKq-6_c_8DtEFUsPU73RQ1mW4nw0lwIl90OyA7Z9N4vDx2rNITdc3ojR152jQ67lWaYjqw4xp_FZkPUTAaQ0HhBAflL3D_I8op4lZQ8Ssx4Whg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/obpniTPpEYt0XsjQ7A-U4u_NoPtCRbU38zA-8sIjgOzHrr2LlKilfkdF5i77gt2dY0jOb62TKfXDewryHbPnj6xfoIjMfaZ6ZdsL_9q1QjMnVT86H09lljO-p5jPwWxKGN0F0zV0QQOTMTYYEHSrLD5BS76ycWjw_IKdnPN6s2t1qs3SbqJZPE1bQbU8r54v3b0Ukw_POl57BlAcH7CWeUv0eokZHRsNtWEr2W9Y3DEbONW3p_YBYef_UPNV-d0C2MlDwImwcyRJ6Dg8oNOkvdw-G96pwTBJXycMM6CaDI-DDRHAuZEpeMgAiC0BPN_9nRZSQQ9KjQG2TCRcuBx1Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=f1jXQrYMMG9Nm7p4sGxnQ9CTH4lv_vojD5xHQ3tuH5EDV61k0FiFljvrlm6d97ZowVr_-XJu1bAiQXNW8aGy3p8LGi2OquuUcz0lw44U9UeHKW2wO2c2Eh7LVsrOqzHLByG0vdWBB5-eHWQC9KwWF63kuTHTxP_BTvz8Vc8DnyFdaKL10RlcvyTKjTdl_VjHeIfoAqt2aPMl5Flv1_21NEj_ikit9l3AaXgZM5X-cXX5-Iri3f0fLIkLr-SI4VcBjkIqm4T86z03eIomBaPXBKDcKYX9bXGm5jHa0I0h4h2lpdRytZZO96oUNrqQXo6vHDEYsG-WOe1e-tjMzPeabQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=f1jXQrYMMG9Nm7p4sGxnQ9CTH4lv_vojD5xHQ3tuH5EDV61k0FiFljvrlm6d97ZowVr_-XJu1bAiQXNW8aGy3p8LGi2OquuUcz0lw44U9UeHKW2wO2c2Eh7LVsrOqzHLByG0vdWBB5-eHWQC9KwWF63kuTHTxP_BTvz8Vc8DnyFdaKL10RlcvyTKjTdl_VjHeIfoAqt2aPMl5Flv1_21NEj_ikit9l3AaXgZM5X-cXX5-Iri3f0fLIkLr-SI4VcBjkIqm4T86z03eIomBaPXBKDcKYX9bXGm5jHa0I0h4h2lpdRytZZO96oUNrqQXo6vHDEYsG-WOe1e-tjMzPeabQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNW1rPboVnmOAdkJTf2l7i0Qbh2ZJt6Y9jmnRgMa7Nj-mcIpiv4MrkySaAkyeOgDuTLtc0AeDmydObyZMVR4hG41UzXtU7eFPBObK6hRTFsq89J0f_Jlwwr4xuhAY1F3iG9R6DezJQ7SL7u7twS9olC0Q3tjLfV-aCNDaU5vYWmC8YkaIAeVzPD0lPM1Db5IMi5gOv68www5pjOAip-YN1kulsqnnlnPdw31oRzkBagt5tdYFMVH4mVZrRhnJa631juyhyKy4sG5Hwvo2cMC2ByiAZiA1M6avt40aIomLPiV93P_J8bFVKgMg--J2fBw4ocTV3dAz6EHEz9_GXODtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=FGudrLVXPJbNGMQMI7YM9_M21-6fEGdqkxNNA8gdd8o6mosBMVC8cSZFhffOsvFainBlV71lPbSkuDWvxwTFyWyCz1Xn2_blfFN7umSiAgkAwwT2HbLNxxNTErhZWi8FrEkCIPh0wQVPgbUuPP2KoYyounYuaaI3y0DPbPXjVUwyBEgCzRfQKXXmDkoiwfMT4gDzO1XFnE_rW2Ew4VoDqMxscD7LeBqpkaFOSdkNemC1lvwt6DHwVoHrYZHNHy27fQqlqdtz9Dvd5kr5J6oxXmmxP_jXGmFPjGAF3CU51SNDBd9Ew7PZz2EPTKLf7nEN8BTcb8jUVHODkbDJ5LyK8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=FGudrLVXPJbNGMQMI7YM9_M21-6fEGdqkxNNA8gdd8o6mosBMVC8cSZFhffOsvFainBlV71lPbSkuDWvxwTFyWyCz1Xn2_blfFN7umSiAgkAwwT2HbLNxxNTErhZWi8FrEkCIPh0wQVPgbUuPP2KoYyounYuaaI3y0DPbPXjVUwyBEgCzRfQKXXmDkoiwfMT4gDzO1XFnE_rW2Ew4VoDqMxscD7LeBqpkaFOSdkNemC1lvwt6DHwVoHrYZHNHy27fQqlqdtz9Dvd5kr5J6oxXmmxP_jXGmFPjGAF3CU51SNDBd9Ew7PZz2EPTKLf7nEN8BTcb8jUVHODkbDJ5LyK8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbrn3eWYdl9zFk5fynFUiow5gKbMJBO5-T3o5RaJAoRM8gv7xL8UNCBLYcLPDtz4KfWe0Gbwk3abTH-mKiSUp-jkOymlHINqPXAy3vUZOzBjV9QCTlntaal1emWMujhXwrGf5kTw7eMJN2oniFs9WX1tKUUd7uVnRL5mxJCPZfnBpO6ivxYqfVJ4R2Ki5ypwkxMB_uXHprkzbXkJM02TzAwQu-sdYp3epV8cfJJiak9ml32tYfLPf_udHA1M6huNZu8AdCL0VI9jKAH9lEkZPBS-Rdv0FcpGxNkcioHaEA6u5auqxMew1H8VoBc96fvOM9iVcMBvevSh4Xyg-_bfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=cWfsEOieOH-_jMazuqw9OCynwfKFhFj02uxHSXsFPvp2bt4RYihDVA7xDN0xUKuLyna_ZKoSVTMNVJ3GktKiKQv9IFTdElRlhOi8TRDGSu_-L86uNbWN2IP9Ozg6Y9RHP1ubhWLMaeSolToL0MLajRvgJfNiL5hZ1Xzhk22B3Br4V8FHlXyfCozYBxhyhxzifbjmObEjPX-DlkpAI6kC9PUG_Rc5B_npw3z_RTq9p2gz1DRFVHxmKrNwGEupMr31kwzwN5vTndrWLxnhteCPcdMDddmDZ1cTiYGWui1pnjc7HxVORamk23UTa2-BJ33lexfjQ1oS20qSvoDkE0aGng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=cWfsEOieOH-_jMazuqw9OCynwfKFhFj02uxHSXsFPvp2bt4RYihDVA7xDN0xUKuLyna_ZKoSVTMNVJ3GktKiKQv9IFTdElRlhOi8TRDGSu_-L86uNbWN2IP9Ozg6Y9RHP1ubhWLMaeSolToL0MLajRvgJfNiL5hZ1Xzhk22B3Br4V8FHlXyfCozYBxhyhxzifbjmObEjPX-DlkpAI6kC9PUG_Rc5B_npw3z_RTq9p2gz1DRFVHxmKrNwGEupMr31kwzwN5vTndrWLxnhteCPcdMDddmDZ1cTiYGWui1pnjc7HxVORamk23UTa2-BJ33lexfjQ1oS20qSvoDkE0aGng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYe6z7uv-IVM-ukdGsk6flF_8HwLFCDtGVv6Ss3gSPVcE4F0x93yA_IdXZgBl7_GbDK84g6BDehrvECzPOVFv27TuvALrG_PSrKXLHUjrkaliWjKE6d3_1Ulb9Hiqhh63BCi-lBv5m9J3gkM_TzOtpESMClu8S9QKuT7NqIYHjQXhG6SswYVwWBK59AyoAJttj4Yfy9OWlk7tm6as57FM5ub9WboRTVyA2eQ0bQpVwvdOOR37BYB4Ar5xsLeA1ZWt3J49vpv8WIvd01pdUw7dFmDENnCn1Ss-_apX_P4IFb8xwreMWkgBG61-SMUYqyx49OK7kHbngCEFvEDpL7v3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nj4jM5mqY5VcSjKE8LwjYb7HC4isPHse6R0Zl5DJ0146obgVKubCcKuQKaejczQY2KLdiLpLG0liT7Itognve1RISZyTEvMImmmq0t7VGXwumdAXe4beiNgcmY8OV-5w1F-p7b7EgEcDkMfyIJ4iShJngYCQrq2dBN8d3LXIfTi9_T95X4_iaZpXkHyDbDGPUoMwvG-5Xfw9MIDU6rodnF4f5hnVPHLfzIiDEwNfeFoSyHuFnQE-OD1XaKECYfPvYN6tfJ0cEK3S-_enP07AWN1B39bjrWuYWtBSok9RhT3AlGx69ieTj4WTuC08DjNjLlxvt-LSe91LpRChi94pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzSkf0-IcHp6btXNbfM3idyrABaewEw9wXJp7sVQ_-qooOZ5NVMkkq_z24lUe6lMqcCa77lJRtHDuQr7JgdzlHLYRMnAvmFLiRW_kQhSDlwR92s9oxjLGV6lbA81J368BUTsh6p6gGVUiBGuHLv8VHzBqyRP0Vf8_Bxi9Ce49yHOx8n3Dcu89sQE78CA9oNNmrgx_28PhOCMPivpChikaAv9DCt1WLW-9iR7Ayeox4aoHz9qJVv6afgG-HEm8oMUYWqPI_ChksX_zRsD8ANgsCwDGrJtBXkskhD4mRe-hni2yRUqmcYBuwJXZ58AVpP9aUAZ9rkME_4K-pVe3gnNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=PoW7bhdC5syj4BgD2akel02J9HvvutOKB4ouEtlATnoJwpMmR75lz3P13cE7bgWIHF08T8XnmkF0n8_kPdlLcKphq5pL20oNEvsCG-lgaxX4jGNTPj-Z8QnDEOJK1mucxK7STRVxSgVvKe4S6M5MTu5zlv6GEXP1dk8ZwWk64MdUkLif2o9A6p3h3CDoz2OtbLYra5tKjwS5ZXlDiJIb89KjjrvbwUop9KEUv9eOXElgh1NiYbrP5QxLQWWgGIz3uOgJONcA4c6SWVLzcnL60wrf6aLbujxF7dvs8-eJPP1WifQW1jatr_pt01y5yKD6_U7Qb5NomJ2HrhcvNkyDVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=PoW7bhdC5syj4BgD2akel02J9HvvutOKB4ouEtlATnoJwpMmR75lz3P13cE7bgWIHF08T8XnmkF0n8_kPdlLcKphq5pL20oNEvsCG-lgaxX4jGNTPj-Z8QnDEOJK1mucxK7STRVxSgVvKe4S6M5MTu5zlv6GEXP1dk8ZwWk64MdUkLif2o9A6p3h3CDoz2OtbLYra5tKjwS5ZXlDiJIb89KjjrvbwUop9KEUv9eOXElgh1NiYbrP5QxLQWWgGIz3uOgJONcA4c6SWVLzcnL60wrf6aLbujxF7dvs8-eJPP1WifQW1jatr_pt01y5yKD6_U7Qb5NomJ2HrhcvNkyDVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPWNgom_00r-Lv-QjC_JN2vOLAPH2r0cjsvV3ll42wyPyTMrw4Jj1gsGGYQARfAO-c6-t6s-fo30AppXG7LI-cw5c4sHo85TXrgGuN1weB8-WfjVf6xoq7PYs0lCB7PqSOgayx3NLDUPHyV3YLkDfhpOUKAs9qZqofZ_5qK71ImY04lN3zGYt-WMTu_KrwpBUoEuIi8gK8KBG9GbLq2tb5wIHWgE_HqN5IQEIEpg9IK4KYRd6O2mUIY7prfeQY8GlW05nJ6DNx2Jhx0x-0V2V0a4kBXnnTg47KZACmOIuECOCphRkyLfD438wzUwLN7HViA1Lbp7jg6qp57qcPzK6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKAMKa2FTjTvkCyltd8G728cxTQAKhQW9LVgEZ7aT87ryNzS4ug9XG6X7mUx4gl7cG10pFB6aiwmp4db_HoEkFzqJyAEz6EWD2OT1rtbICva4g1HdpHENbl4dO0lDGf4_2aBpa95mkvjEWj4ZDhoO_6ZwgElgrnGDXJ2cyRlRhrMSPt_dQUdg6wzXJ4AVzexQiHIagIi94mA-07Pe0iAl-hxErlCrZJn3tSV1GeFiYmwkmT4PLO_QRfgcLEa7TPuUMRVppTF7Elh7CmV_D0s7ueHrGnZFF1PhklmVA9fT4PkfVrWcKoDXd-gP-SnwwbjK6pG16aAhC2DLsWaqFyXKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-4mIpHkb_4JuLrTK71bVf3W6fkuDFAtBO5dOfJpZyghk3XPktoRR4Nf0S6i8ImHx6FiSawD6lQpLEqqCYzT-rvsxHcbYGDMAXZPJVMKadovFjmlhsXB8Wc87gS3p0Hn_Qgm2pmq8Wndt-ZZG8HCcHpwrU1WdwFEOyuPbX_yXzS5xd7AaDzNGOPfI8PpTaTYKhFAfAk1-h1JbfKJv_U0JgMrAsLGtZas1z5WyOQA5J8LWky94QpTMvNVUvh46xn8p89q68cbLnm3guPXBNwsC15ZeZUWnkN0tHbuuJqxAz_9qfepbGU67XVZQKnertEXiHDifINRbFEJugEemLuO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpBZ3vAAd5t5LCq0MaUoS3eYYBVGiBg1cdKwJhsz9OApoRj2bq7ydCTO3KZb6_V5aUKjrSROTL3vvu9M_FB68TdOTBbWy93_mN9DjNcU2sG3XkywOPvWKtQ_KdTod_uaNajNwGOhVvf6lHIc1nWYBvKiAA4n5rvNFmqSBpVAGMq8dbKtkuKLNOZEVs_M9SBpx7_H34yVALycRAcQI4sWX69drOIIZxXs3_I5tNwoShbRZ3IwiCBInsrwWOyx2nYeEvP0i4OJPh9DwSYj37GriF2A13y6gGOgT4ZiyuTig4MlknL34vdlGo8aWKSx2t84LGI938GodaN-97P-8YVjIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBHwSv9T5pL4zLGto8bbPB_Eu4SF86PCM3O7GXwgj7gYj0-Wc7PPcnzbYlFGMDBGl1nVAGy0B4pDfiDodZZ2hWUh34J3j6GEn7cJXX96qpwOEHZ_axmMYlLn8B-ZE7ltTfquuy2JN7Jmq5etvx0jocwLoZoWqcEWGHFb7sowPKWraMKhDH5s6lEubI8vXCYfHzT-dBnVBAsuu-zihYJo0LwKKaNW6jQVPVZYFGcmAwvb4-ylLZeHTEY5B_qW-78skT38-jAQnAZkyzlMOBxQyQg1KJxJIp8QD4s4UmkWwKM70_hCLB2sKnSLKS7stsyTAsueU4K2kw-lh7wo-iphnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J165VqWA_AJR7T3XTgWPGIyxIeQc_9rYMlMq-Qhf1q7ofLaWVw9ovAchdD5E7Vb-BSsrx_1JQDF9icRy8TP2yJ1zE9lHKhGJNUWujUvISiIZZ-PrPvuT_zhGFbLwIgfGaobVheWKZIfeQtqnRICVtZVSr_aitejX2kyha7Ltg8ls7C8uDLeKTBdreEewwlVVW01YNfNfV_aKjavrt-ygawSh8gcuEjzxQ1nJBAY8g2tpycA1V-FQPRVJHhrOOmy885NdDmSlgvDl5WfAlSN8h1M2p7tWfCf2bOiWFzky3PnPCCkpvRkzMAF6FhvdXGs6meDKODX_BHIQfzfGmrvQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVu_OljmuJ-U0TEWbTHow9qUlSocCk9V-0lOpk-3s3SpXbZAEHl53BDZNpXtjYknAx0QxXf8vdFOLf-5svqOksKKWB2lzquvDIfsbgxh1cBYCos4fkQlRisBvtEUAOMCvbt68YRF1xUfD1mvI6YSgJbP2GNrdLTW3ngP5zX3NZCEEW3_5ijL-ZGF3ewy1IonsQ3vpal-0fgELaLSOMoW8EjzDXaNuX_payS3Vm-ttk2Ubn8BYlH9vCQmQNYr78oujSIwR-Mli5cSooeJ3XdVfPMRjkzPRdSDf5pqbbeL2P5Sos3Kh3gf9QOF2NFAg89BupLEvJ-CyvEZc3HpFuCPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGOG9N4WuaqLhMKFH8xYqWnIE8PVNGqnSJhVLNHHs2lZyf9kqahbwGdT_HAYPFJgFAb_u8hwdj_5jOBrn5LdPJBu3M9b16EiDRaeqt4klh2nhh2bnIHf0mNJujttWc9Gkzl3Gv5pGiqJp3qv-qyJ-6F9BIBS29K_mBlRdLlPX8h0Jr-d1BtMUS9vN-fX4xNjMOSAeygDSSBo9jJsdf9bkDyHZIMpdnnpDVpJzqIV8TnQkLw42LshIRm5k8xYmwEPECcc01_qKMbtFVj5DXjZglp9f6XDqRWcmWxU35M8k56SqeufVxUhUvvfnGaDvpN0ryNy_es0DSM0Pub3fH80RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwQ_TvXOkHo50rqgJWZ0_0BxgqLLFoebqjQS3MZooAdqAGqfO3-URZgdWkpFt8SnppLjB8tdz7BjoloTaLMeyKgUi3EWs3a81DWm5EqmRJe3AfJOTYZQVxDrdo4OctN9r3KCNssduTmaaiHGebZcx5OmXqEu8tq8yjYvUFblyvCehrnR6raGoxYRSD5xcALPZhmIdzFScqRUxwJajyqIPCvB2qSF1z-AWSBZDwaODE3htTnGzGEdlVJ3vANXZmrSRFsEpGhqvqtgS9kQsjIkSF0rCmxlqX6fBUvsnWUKIOrVKahLZvLyzGiRvi8fvRDdGu5lZO5Y0gBPfiJ_PnMKgbyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwQ_TvXOkHo50rqgJWZ0_0BxgqLLFoebqjQS3MZooAdqAGqfO3-URZgdWkpFt8SnppLjB8tdz7BjoloTaLMeyKgUi3EWs3a81DWm5EqmRJe3AfJOTYZQVxDrdo4OctN9r3KCNssduTmaaiHGebZcx5OmXqEu8tq8yjYvUFblyvCehrnR6raGoxYRSD5xcALPZhmIdzFScqRUxwJajyqIPCvB2qSF1z-AWSBZDwaODE3htTnGzGEdlVJ3vANXZmrSRFsEpGhqvqtgS9kQsjIkSF0rCmxlqX6fBUvsnWUKIOrVKahLZvLyzGiRvi8fvRDdGu5lZO5Y0gBPfiJ_PnMKgbyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbvIU56rl0WYfltjERJWE4iQXpLXQ1qCzxfqkZCLjXtyRSIaVpDrA3MZvzi23pl_nW1hdvm4uAWchZuaA1ml0G4TTXNunFprQyKm_C1ebBMLIdMsC8aGVYu5gQ0v7K0J9JPhOi4ieJ9fHfYWoV8pT3DnYIZJvu6hnJx3R1ceDeBiqbUTitH6MHRWeuHX-earT7o71ue3f1t-fWqeAg5pdrWtDx8QgjV4lbByXvKIbjBqPS626Dosf0Goyrj3A3Lp9jH4zXSraOTc5DwcovmrQMKIU9Ml6gNQbaeb2tcj7yZbpppQDjxr9wxSAr8A06JEGy9qnOTyH4Mlc4IUWqocPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFyGxNZBhswo0dw17ZLcgmvJqD7Tr3-TTvgHEYIw0GsEustFoaLx1BpczPXkvawLW7GOJSVfFrJx-wAodgy6AfPKPUK264jJ5JFfXijhV25r6bxnCbRbvLQTh6L0a7qynL1UI_MnGvB3LytniyiIX57YX00JD-mdg1Negun3bz2w2zBhxII3VDimO6Q59bwXJm9q2GlXd0F-40kaP_FMJK4V11WNoXqw-L2g1jTEN3jZ8BgdAGvP-citPnTlycGKel4wZpPwuPNOH8-ruf_EhGsa9PyLOGtZ4Oy5PwChGmkwlJMTU-Phiei17Y8kgKDtPyMLz1_fM4xUMkN_Nc0LkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=d3HwyhaSOQ64TwPpvDxo-r7eSPNTBnyb_I3GUNl-nHBrTtuQ85Fa72_LtgcQd-Znffkn9nqHLuYn4vQm98mhIpyhFPFJ0RTslup6P8vBZqNNzXDKsR2RaaFrgafG2lmcvl9pAckXW8Vw8ayJWDYb2XILNzeSYS7JZcpx7-D9Ap4bHHQwQm6lPHLaxfsWtYCksaQ7iwj2yoUK9yNM1yyj8uOxUoB6hGtzqSgj7zek4kxPyKa6ij-_W9jqQO0tcu4lPb0z4qqPGFRA_Mzf_tN4t02CCgKbjqoxm4o2yOQd8XMoCd12hYil4p9YbgojEPCasVSa4J6HUD_DiCbiHyM62w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=d3HwyhaSOQ64TwPpvDxo-r7eSPNTBnyb_I3GUNl-nHBrTtuQ85Fa72_LtgcQd-Znffkn9nqHLuYn4vQm98mhIpyhFPFJ0RTslup6P8vBZqNNzXDKsR2RaaFrgafG2lmcvl9pAckXW8Vw8ayJWDYb2XILNzeSYS7JZcpx7-D9Ap4bHHQwQm6lPHLaxfsWtYCksaQ7iwj2yoUK9yNM1yyj8uOxUoB6hGtzqSgj7zek4kxPyKa6ij-_W9jqQO0tcu4lPb0z4qqPGFRA_Mzf_tN4t02CCgKbjqoxm4o2yOQd8XMoCd12hYil4p9YbgojEPCasVSa4J6HUD_DiCbiHyM62w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIP1BJNnR_GAbAf-blFLmpXlos4OFssixr554I06z7E-yX3U5ytuD1aDhcfhA_5mBMWeVQcZ8wj1OnwoJl3EEu-I0nMRYQGqyNJHaD1O8zm-3fVtVkXhUB7hs1iqyZx7gqGk5HisPalp7Qj0Ujdzyl_BMYyhRAQmecPUCRTFcEhmZJ8bQ5WM9mukkQcwWNeQHn9jgsZSmvNV6z0UWg2iFtqA1NJPQAyeQBnRvjfTFXATXKPx2lyPbVHlizAYPnAduR7CC2mFlv5quCPYf1gApArONTaFS-eOJ3KwtLBauqmLDqKZBIPLyK498p2NJ4mEksZLh8e3MsvC1G7oww-H7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuSuqsvEYhsvDYA6N04dHXXt-XGYeVeEYVb51Ja-K35n8yDM86BL2Sy3iU9402kxbTYCuQcGP_uvMt46j9MEdIDuKRh11tvYqIYXSQl-UT8dW3BChXS-YhX_Zbr0qyF386ouND8IPHWt73DhSF6Ig9ZtR19YMm8Cc7MCnBkMvKwrQGHTUmVEjjbT9MbQYPz3QSj0kwnKu5DS6ZLZdz9izd8W7eO1RNJTjEQYHeugaSCjAEU2o6wbYaVVM6ureLuRBSBC_CKjUJO5aiLWUyEnPZW-54Ro4cW-rZk9tGyx7XoDXxh2DkEAC8iI34ygBFAzjp6yKerWDqCPq0oWV0l_xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Sehho-31QYtm4ai3G6nx6cTNj72nR1PXz8VqVrQO-HvW23aOJQQtukadRNLjiGk90d2pcVvrBc21OVkr6zYlDN6ceCF34Y6RbKTxgQjgfAucIa2i_-QqztilEFIxLfjZfuxwkEODSrLiXrNPv0RDDWf5nV1Bf7rvpXg64RcfrNZUHe1BCnocugC0RW-GZCzrW40RVEhRPA7boTOjMir0yLCAtI3dqC5W3Md6Bc84EfWi2hiFz9teEjXknhodgPTa4aq4SCl3mDJiMtakCQKRi6zyTPR27oRLGr22uvXhcRq_hekd_vA1af1sTcW1LtwIKnru3D2LH-x1EB-1WcuAnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=Sehho-31QYtm4ai3G6nx6cTNj72nR1PXz8VqVrQO-HvW23aOJQQtukadRNLjiGk90d2pcVvrBc21OVkr6zYlDN6ceCF34Y6RbKTxgQjgfAucIa2i_-QqztilEFIxLfjZfuxwkEODSrLiXrNPv0RDDWf5nV1Bf7rvpXg64RcfrNZUHe1BCnocugC0RW-GZCzrW40RVEhRPA7boTOjMir0yLCAtI3dqC5W3Md6Bc84EfWi2hiFz9teEjXknhodgPTa4aq4SCl3mDJiMtakCQKRi6zyTPR27oRLGr22uvXhcRq_hekd_vA1af1sTcW1LtwIKnru3D2LH-x1EB-1WcuAnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AOcwVvIQ6gaf45xK9SZlY7IOpHVV9ggJlUu-iqntm-e--U1B9Q3rHzpvaD_dnhQ2-AKE8LRJBbt7xbRthP7UUNYhMm3XZBBJj11QtXFucGYs8BkFKwl1T8g0iQp-UBK6Rbl9vl5MLPpFK6jeVDvksMd8B5i3hMBet9a4ITRM44rO50ed8c2UaUJBWKMeQNLeSFctlwEb69QUhWRJ9ywZKgP22pUzo7VlC7kTTBLOAScWPVi_G3QQimKnj75THznpKSnam12kjRAjlRjJCNLxqH88dQXshhcjguOl-OaM_SHv-9HUaz4CNpl82nuQKejdoGVVD8PAzmZaiaC32R1pBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=KzQjnhxyHg_2Dvo2EDJax2yiuXqlae4FdNEbyfVeHXLswYSMF8IqEEA-s5Nwe7RkTwBt6IGx0HnXBxAUVhZhSV0TqOJOCTc2R3xbRm1S4mXEdFbkK4DvoOhO5Xxgr4oQ1wHVJCFWUu-TYNo3T8ZKZX1MmOSvtyMKeoJfD_oDcmBc77eUBNzWlbWnEldBHZQMpVQaTmbxG9YTfa30r0fZKbqT2J47XcpkTLMAbYio8jq4mMNbxmcuZBrRbcSL5wushWvG-sFq6Ln3aJlguwz7oHKbG7UAs1K97SQBLsj8DanzeBFmmAkbZo4YdJUjWMYfKd2-pOrZM0Ghcl74-KaMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=KzQjnhxyHg_2Dvo2EDJax2yiuXqlae4FdNEbyfVeHXLswYSMF8IqEEA-s5Nwe7RkTwBt6IGx0HnXBxAUVhZhSV0TqOJOCTc2R3xbRm1S4mXEdFbkK4DvoOhO5Xxgr4oQ1wHVJCFWUu-TYNo3T8ZKZX1MmOSvtyMKeoJfD_oDcmBc77eUBNzWlbWnEldBHZQMpVQaTmbxG9YTfa30r0fZKbqT2J47XcpkTLMAbYio8jq4mMNbxmcuZBrRbcSL5wushWvG-sFq6Ln3aJlguwz7oHKbG7UAs1K97SQBLsj8DanzeBFmmAkbZo4YdJUjWMYfKd2-pOrZM0Ghcl74-KaMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0QKWsp9JVqhjsMGQyDbRMCgLWRNeSTxCmefH7dsF77i5tg-zW6p-q5-Dia4KKzFHfmspFrSIUJsi33xSQJZ6fVsFIuEklT3YyV-uMbYDj17nF6MUB6GuDBq0HaRQc5yZXEtVuQ4rGoCtM9tNwvUEXhyNSBHsZmMne3G1RBZx-rksLJpr7rlktrNi2tFf0NW0JQ50PWIhPdRsb7yIMGTRE5Wp_NPqAYuZSAsi9Hyvj3GIJmIQImGfdobKc2_3Lx1msL1nNwwcRzO8XfpKqq0JiXixMEeDkUdY53F0N1Q-UqUcsHqyEe_pXl0kozQCEwGZROptlfzgG46UrWIp6YAEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FpGHDoARueT3xr8AwODxOsjaS7KePAzuCqPzaqcj8pdxaUlTRl-RWBJJIZXTo6qYFpRlCuG_0JvhZtWUVOgDCjzRf-fwjGElA93fiHUa-1KYjImYd-NE88bWNDSCYBhZNKABQB0SQU0OVpUptGcUrpUA3XGZGPz_hdoRWAgl1FhNy8cQbnJgoXtO4iOM9oROWgwxwoi4CqUd2AET8rBBMmLpNc5wdHmdNjoh2frMz_suKPOxnz6D7ZV-xFURpSXRTQl1kw6JOD5c17L6LBVLh9PgX381vLEcOgpGsHCp_DTVmqIxBr6Q2wwrgvqxn-t0STwKA2hLkVqeYSMVM_K1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=nc8Cd26iPT0-hNYjsKRZEFfqcyXuY7mnWnFNzlZhapvPZs5shQPSlfA_jocHry4ufNyXTN_DvH6N3qv6ZKJqVo7ecQf6hkuwwbSqX_-3uB82XRlDU3qzmdyYZZlko5DW3zCOEf1ZrPEeH3KZYkMbFEgmUJxBAiLwny_DF-eoPFXNsCFfIeVgWivnPuBe0kVy8sAXlWnUn8whnc_jdKqidzd84gLhPE_IFwWbwLtCoA-I697BxeOCla4uyT6qhEvRoNuBJiY_EP8WoZjTae3TjNWPU2xUnDqWKmtO-FD0wR3cxPOFVz4w7aQaXG7-zmIHGVCCdCDDTI8kffHfBDqM3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=nc8Cd26iPT0-hNYjsKRZEFfqcyXuY7mnWnFNzlZhapvPZs5shQPSlfA_jocHry4ufNyXTN_DvH6N3qv6ZKJqVo7ecQf6hkuwwbSqX_-3uB82XRlDU3qzmdyYZZlko5DW3zCOEf1ZrPEeH3KZYkMbFEgmUJxBAiLwny_DF-eoPFXNsCFfIeVgWivnPuBe0kVy8sAXlWnUn8whnc_jdKqidzd84gLhPE_IFwWbwLtCoA-I697BxeOCla4uyT6qhEvRoNuBJiY_EP8WoZjTae3TjNWPU2xUnDqWKmtO-FD0wR3cxPOFVz4w7aQaXG7-zmIHGVCCdCDDTI8kffHfBDqM3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=WV_wA5IucuW6WK7tYB-Se27A9Sz7m-82gUuQIGcKlPF7wodtbrUfMNdu8GAaVzPF660UqFKaEIndtGuY8JhN2BMZ49mLevbP8UJZ5Vffx_XJpiTtFRmzKo2RruBkSj-gpRLHVnu23qYENab80Thlis3u9znVcFc3VczqBrk0p4XQXIVTY5JYhrPPOKRK0Hoi4OloMEaVNiuzvwI9JS7dX369SVxwO5jK2LJV5I7zI7re33zcyd1UNbBIoi3kMibKdOHtHUb3exICMPng4aypT-JEJgPz8JyMAVTkmVAmqEfnxZaaBm4he6duErNLaI0H2Yt0laEpNriLbGvMwRJnbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=WV_wA5IucuW6WK7tYB-Se27A9Sz7m-82gUuQIGcKlPF7wodtbrUfMNdu8GAaVzPF660UqFKaEIndtGuY8JhN2BMZ49mLevbP8UJZ5Vffx_XJpiTtFRmzKo2RruBkSj-gpRLHVnu23qYENab80Thlis3u9znVcFc3VczqBrk0p4XQXIVTY5JYhrPPOKRK0Hoi4OloMEaVNiuzvwI9JS7dX369SVxwO5jK2LJV5I7zI7re33zcyd1UNbBIoi3kMibKdOHtHUb3exICMPng4aypT-JEJgPz8JyMAVTkmVAmqEfnxZaaBm4he6duErNLaI0H2Yt0laEpNriLbGvMwRJnbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LvDyttysmOwANpLhsiKijo7BnCq7z5ycx81ZR9fIIAQ02QBSVmhsMnJ1vME7ZrK3a4O2a2nv1-uS0m9ukIYjhXqO12RQQo8cAo8yvsMU48u8AqPQj9e-15qWJr8rTz58gaYNAm4gHRLjXWLtcslX0_aJBYMwohwn2-A93geYalfQxmvPr9EIL474e52TpbOnCq0_UhdRE7aCeOPDGXdxn4dK2tL0yk_r8neeaeV6e5CLc3ZXmdJfqjuvt5RutCojKubIDXQusyulauw-Tm-VfHbZ1bQ3t4srmIV4uwSbynY7lqxFKs28vHbbUYQHJP7M__NTIihK1wVJyucWR7Lnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVu1zO_oWOfAtx5MTJlKSQN0J6rhgsElSkgF_tOwDfBs7jdvywex5b2PP1o5-ocNTRJewtB2YEGp_5Ro8KwtGNAnRUK3PmW6n50nJhFsPDswWErTNHqN8kspThvWImKu7_GCP7DGkUEi4u5aER2ao1540RXdWZYBgCYpwoAB-4eBE2twADeeSK-2CBhoeRI4fg2rXjTiBg-rUzAlDt25MIEhIuTAlQ3n6OE1hTgqhZPDUmyEj9XDtrT-HBbOowoWVE6MxSX0jNy8dCRwMlwjqV25IlhrUTnGAzTriuxHQH5nm5ClSYUTvdBfGTfM-A8K4Bf6DzEz6gbQKJllUPJm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFv6NEYBakMCjhtxL3BxYMEEdJLlnOgskedOQIxvAcruDCAQCAFjK2AUO62tppWnMf7sMHdJM5o3FshjsBqSw5ObY-Rpsz9MLE0DIGbveb-DhkOFwksbSqCiTPaB6gGpnlJIRxdsiGNmephw0mMcCb79VAejaJlJfaJ8KLEjoOWShgpf-FvhAyrUpPxeH_zBhJKen9gPPP4Tsmkk6qy3mTuNeMtX7Tf9z262B0NyHq964e9l8i9NYVEfgtmoAt3Y_RHY19ofXbmWUN79bhnL2Q4bpCeKYoe6SQeU6X7IsvON3cSE4-tPkbRoG2dcrHCZmocNUmNo4_qmQindMdSiMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=O15L2lioPJcbs-jX5e58ykVXt2_ffLkxIQ4tU0DKDqY0rSpiOd6hOAWGscWhmJfPCYhBD7k-wH6fq-Nj640hV_0WpK4z-VuQXE8YmV2r3mbReljxTPAZ5-s5hev_ztlmSiJSbTm4hDCUZvwkn3OgvyVU3JaJEcqAv3mFF4ZTq3el2aIAWXaInIIiF8nNm7Zjq7o0ZIt1bTWt3jujpLXiuVrs8cbXyt8XmGoLDno_5H-EH9ibeE1Flfh2g0l7Fz-zz_BSPVtj844JmC4wpBYW2yUjyRWgR__iNFFj_5e4g-vbK5oJtrgwVLPJlLv2DKSiVGEMwpfAD3sE1XfNATqygQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=O15L2lioPJcbs-jX5e58ykVXt2_ffLkxIQ4tU0DKDqY0rSpiOd6hOAWGscWhmJfPCYhBD7k-wH6fq-Nj640hV_0WpK4z-VuQXE8YmV2r3mbReljxTPAZ5-s5hev_ztlmSiJSbTm4hDCUZvwkn3OgvyVU3JaJEcqAv3mFF4ZTq3el2aIAWXaInIIiF8nNm7Zjq7o0ZIt1bTWt3jujpLXiuVrs8cbXyt8XmGoLDno_5H-EH9ibeE1Flfh2g0l7Fz-zz_BSPVtj844JmC4wpBYW2yUjyRWgR__iNFFj_5e4g-vbK5oJtrgwVLPJlLv2DKSiVGEMwpfAD3sE1XfNATqygQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sv-1XF86678-1IoCuAyA6rZ2rKb9_sZZyYBjHjNw91dmDnmdugE7WlAQV45moN6TdC96o7PBUU3j3pQYNZHq6YjjtezEccPQAAs-LzSntnCTm7zdWJGNUABYlG_1pZziIjlPNtgrDhHj6CbXQ3GWJpIGs2Sh1F7WpISxSlmsXROGfhRmyaJg9V2DkxO4X1ruATTDo708rjp9clHKWE2z_JA2hgRvxqR0LTJG9C35KDmlOZvM1b-OhWBt_v48s-s0Zsijk6MTG4jUUTuGYpF1ceONnr7uhEwPZB91wDO0--upvuamrsYLgev3wpGOv8GG3Gb27wJpFJkRyAIRfOfiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=CNdonpDPib2gLWr2ldj3LVB6ekt9t4KpXgB_EQ2qwUMbkNO37AvWvUYCOo6_Bl6CBHNNOJdeKXb46wJAtYw84hqzVYLjiKtcU3Mpmag8PLMWpqA2fbpouYx2heQecMxrU3l_Pv81uY_NGnV2ElWPyIoVgGRENsuir1D-L6uGQ3GapO89wZUJnKQ-3_sAX4nromtHlHETC9JNZm97Ww3S4VP-UzbiHFa_NQYZ4c8x1K9WW4mlqjsCegwLRg4GQlQO6K4r4b92ofbk2o5GGglIkKMx1QLipIM8xAwnS7G7E_unaGokKWuZrfIN8-sRJXHkDwl4Qu15FmpD33kL9BymCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=CNdonpDPib2gLWr2ldj3LVB6ekt9t4KpXgB_EQ2qwUMbkNO37AvWvUYCOo6_Bl6CBHNNOJdeKXb46wJAtYw84hqzVYLjiKtcU3Mpmag8PLMWpqA2fbpouYx2heQecMxrU3l_Pv81uY_NGnV2ElWPyIoVgGRENsuir1D-L6uGQ3GapO89wZUJnKQ-3_sAX4nromtHlHETC9JNZm97Ww3S4VP-UzbiHFa_NQYZ4c8x1K9WW4mlqjsCegwLRg4GQlQO6K4r4b92ofbk2o5GGglIkKMx1QLipIM8xAwnS7G7E_unaGokKWuZrfIN8-sRJXHkDwl4Qu15FmpD33kL9BymCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcC3bB8JZQy1jfRvdWGc9BI-QAKFS58DX4g0s5Gm1P1vo158BLjW-EmwIP3w2wJ1Zy0OkjvrH6RdAbRsmWVG3osQ116t3-N6kt8Pl4CIw8SyUAYiESmuxjZ3X2UUbIFqjpDL2h8eTYQN-H61lU4ZaIKligRCtqepRWZDii5XTU9k0gIjkY0C_H-5qW1fn8OKFKqN5XoANdFhNhABRavXi9X3n3vGqOKu8SjzDY7gN7gHuFRfWpQ-IYpzKchcZZ_m2fTPfuoplCatr9bjvYojBVULw97UGAiYyKM4e9ePqk3sMoyUv3Q7-Nh3x2JXilLpCTR50BHvz3BTtnDsYrxagQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=M26zT5tr7sP7k0o6m764yEcarZlIC7kt4Mww7hagoV2LwtB9JM6t8wFdc-5busn9DXZwzr4PVCQEHzG8wIZSGi8NXHAl5zVaa8ofSb2-qLZgyY0Aw2ONwZ3TLWJDL8KhiHwn5pL7Ypnn6V8IfARCAHiZfOWZ5w65YXfrIjSlvRKw8QmzqrdS8rKAbziuxaQTui0-Wsq-9Aggz38Av12coaHvXNdSSBXXvQlILSes4XC9L5wOdztFAXwsVTikIzqeQlv9AeoB-dAdbklfsI7_dtIGY22zqaCfdlH2MKg2PezidG-vsjzPJsJHReEiiGknoKBwGnyUwcXBsXgN0wHQbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=M26zT5tr7sP7k0o6m764yEcarZlIC7kt4Mww7hagoV2LwtB9JM6t8wFdc-5busn9DXZwzr4PVCQEHzG8wIZSGi8NXHAl5zVaa8ofSb2-qLZgyY0Aw2ONwZ3TLWJDL8KhiHwn5pL7Ypnn6V8IfARCAHiZfOWZ5w65YXfrIjSlvRKw8QmzqrdS8rKAbziuxaQTui0-Wsq-9Aggz38Av12coaHvXNdSSBXXvQlILSes4XC9L5wOdztFAXwsVTikIzqeQlv9AeoB-dAdbklfsI7_dtIGY22zqaCfdlH2MKg2PezidG-vsjzPJsJHReEiiGknoKBwGnyUwcXBsXgN0wHQbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOmLD4SXeKmhpVIoSa1OuL7zNR9R13_onVorsIst4CQl5QV2ri4h86kz5SJqAluu5meitvbRKWK_8jxbVIpFGvul6H9wSBLLYdrlO9eNG2oMOK_YMSTVeNx7y7LYps2pqUlImD035OROeIQs4REgq7qG6rnfVgeT44_I6PdGahVTdYYmcKqbfy_5TqM43hPDpesSnJPfbWJP6ugvZ9FhyKfEvCWMXE7yZFhy41Sy5z3HJOzO2tdxOR7SdPv389_wfiJpG17OWXeU3pYcQzZXKNXf36JjtP2QGmuB22AOf9APBpjqwSBuVZZl0NCDMadAeeYt0p1F4mBvKjqMTX_Lpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvFTW9cJ-eXdkzSVv5-E4AZ-C9XFY56wWuq9j8M6MieLFTitwuTnJo9Qykq8XX6zpIJbR1FYkgN8VGCx_fGAbsztLnP9wX6zSLEArxOh7ygx1rYj8eUsXn8tohoAjwyxb3G2FRP07OeMipuW2zz_rdCKCqgGddwp02NxCc3wX2EKud9AZlLtMO4t1UVUsa5rjyEHdMYkNmuAMwSqNhiRGsvGO9Rq9CH7tHe0-Ui-XQbD1TqzB8Fh0waFO-AI1CIRHaFSwHajZ0f-TIc1kuAgTcSZMN0yE-_76qc2eFtEu2JQTVBx5GK8pkFbSz7e1-MbTGXRmlGuEeCos8EwtZKe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NtSgW72bc_HfBgNHv_RJ6ysdYETOK32nrIP5ADQJp19XyExJ49iNR5YjDWOCiidap-yl5RS-cddSfq5eZ1_pLPDbtmLNOZVRVxjwzabTh0tzpvQDmNDi3pzvyG-q9Ekwl_jnc53Gbx9EZh0kXrXIq2Il9OqwxmNZe0AaY5QD2wvz3oRhMyCsrVLVjcsUsCZs9WGpJdkOh5-We0ADqWIaXfDcJlqTO02U_TMQ18SYjF1Vy5Rchi_3FKCedm5p7J0IaJVfHRa_B7glkCitB8kR9J6ncRiGNbkOltNP8zsPuYvyLzAyyOcntuvLlnsSXlgzFlvhPdkLjzvTrxMGRJVbWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq5deyrNzKHnV2eUgTqEhC-bEs_mkFqpnMkxvkLA31RVZmydV17djwvNeZ6RUpMr4tgZK2dmSN_SUd4gdcjVbersny_zXdh3cR8i1hZqmhVAcwnKDm7uu3LBkxxoAijvpyEgH3tRELr5_ljovsCZIk5V9JgV1wGKpKFEWittTMwA_LWSVr_CqMRRxuzk09_2qHXZ9nivT9FpQhwWIgm4uMiig7n3oxT1sBE2sogSIoy0HvXBBcPnxRFzqlWnnRAlCClCxMI1BANaZmzu1hq6z710tBWnhsP92m5zrWqtzLmtW5ndGanI0Zf-D4CaN4GaD58AN80oT9QWYiTsU5RI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kszjpF_l5Z2GRwoqm8DJpxbk0XoJ3LnAyq86wjcRL0oLntmy2F3qgZCUE9HwOjnMA2hAp3cSBQB9m0l4KRSyhpVb9uCVV4KbIOxDS6dPanc3hOKzU6Y-pvj22iNCH3b-5l9eqd30PEaFeEsiVH520G_evP3QRXTCvDhApXN5-5Ts5IXmm4Du2ZwBPtkTlpiaL7T4wfVpFDLa9Sc97BsDMtKB7JkLoo7oRc_xcpSHCwDDxKoR7_fn-Bt1GiJLjSVOF7vQa6I-Voq35IBS487bu_py-mgoq3OowSPTY32wv5N8DGs1bi5wMcyjS9iAeNXdOnzgCphXos9KYxVfsdukCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
