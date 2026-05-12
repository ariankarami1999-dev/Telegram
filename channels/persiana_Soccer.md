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
<img src="https://cdn4.telesco.pe/file/PvrGVCWlBJJOzJi66SX_YqOGAGIG6wsfTWFWppR9XlUBDKIyJUUOI9bblA23GJvB9vPnFT3O6Q0kJ8zckvgAGzfjd1VkjIfaGJE_hJuOxuvv0Xv4pJpkoVUQBoAEazhG0khNGrrKMGB9mHzJWcfW4BP2aRkKfP2DRVoEh47G1dH-koqjwqG_Vs3FX_sCmKfa1kV5g1QnahWOX17K2SP5zLa5-KKEuwr9CgqTXA79wjpdXnO61E2oQ8WqNb4VZv2lphZYAB03QRu0o0oZHH6bUK4mPsLAdjb_NGAlCFxWMXnFo9wqxqm1bcqESm6eMulMz7d3YXSmE67rCxcYmeccQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 215K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-22 14:59:35</div>
<hr>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LY3fcbPK46eGraC9ret7kxRLsHKVyQy4fzG_0UHoEqCeLGPod1KB_Y3hf_gkIRSzKi4zACrYDieKXtyRtheD1UronIoR7B4sH7KinLhNCbXb7e7Yl-L8yGvTI5RZpD15MbsRwNTnddr6kllk4UnpBznF9sJeB3bESsHqMVHQJmHhJldwu_mWSFZtcePiwr8y23in20zqEMocNrdmeUhWkwUPDvfJdAM0c_ghIem8p7f3043T4gWMsDCTxcE9AqN0eO8fn0o-Ky6OxAcEKUoMLkUVPDMluw8M2W2PzUMjCk_lI66mcSGOBUd5xXBLXxidJ1I90glD_ZNCHmDCSakPjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC_FycVwSOqgOXIuNg5N-KPxYAohg9fepCzllkF6xDaoSZbzpk5lsDFBrj2W8IK0rVVPWFaFA3dFaaknRk4iAONgrZ-wQ8DvvqBqmt4AgOapF683caqrhaBZNx2udj3CJBJnht4nuZox6k-P6ukKyFSOEAiKzJTaU5-Cs4zHdTduA8MqeUO2ZI6u4yeLYRazJn00g6vFYs2x5AXY77rw_0HTaIOw-wSHqgTjhkDY1HtT3oTLDblpUTezXHa8JmrLMv8e3RjSQig_85Sigte0c0TGSNI5jzI31rPRO8CaVtMIaGyoPNcUBCGinxyx59p4K_N5FP_HZPxhfq4IVE5cPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8-mg_dzQsy_A9jOpT6pMuKIIMCIaQFPTbnXITUIpRsvdbKsouvcgM-AyNnGw9V2TEW7nLa_lN_wtCMujLohZbv2TYVzZJYg-sWwH2SwyqTAMRK5y7sFUuUGr7C0LfY6UYy8SnYeYAM6PUBsaSQZJtMSPE8yPgf_d8s1yI_G8D0n7U_DL0SGtJG4MxMoWfRIwmmU9hgVdnNDkSXFQUpun7XRZqGUWF06bbn79gWMurMzOCuzZ-2ULkR5cpp_IzfVMSwP52nbyAHljHRM8zmm6qX5s_40MYAMWy-Sin6g3AtnpTSiv5pBYrOq6XY-MCEqnd69SgMb1glwnEMQMv6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOjokw0nIMRmFc-Hy91sdr2j46YQwM1Ccetg4SaAZFGNUVaFoeiyzrMEuguWx0DdJ3bBjlLsQ1xn8StIZOh3WMad-UNUbvt6C2LPCXlOXot2YTwtFYTyiroFUFwHmimQThiJbXQcRPCmXA1519En3RMcgLK_4at-IAac53zq3rElje8cmAdkVF-wHMCTRrfZTaSUJHJyyH5K72NyLBPYHUTnK9fQkiFXvHehPQO2kFdm-gehpNWpaGWDwlH-YpN4IOx3JxgKoclKhIh9a5kdvT6vy_v48Cnf6bZIG8kzbX1fTUhfQovN_79GBGRAtzkSqt_EHgVm22081dtn7BxOAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gm7uFOWoSBcQc8WVC4tqaGXV5LZdtqPEigmnyh4_GaY4PPyvszOJhewfCOmgHdWcp6luF4ja6-WbJ4B1mowSmD5RHPftmyB3eIOA8eVzaml26mDdQnkj0dEX3R5-1OXcJ5WRoQwZg7zI3RyLNUF8KWmdARzWUqt6566qS9evOVsbxi3NdrtLHhOxwb5Ru_soEmDo45sIWe6Yfp9pmcrGHTlVTXcAd2aQCRfMBgbKbMTmq0egprM-bctKZt34LtFpScT0geViCePMZOjhBqaq95dCuuCV8iDDHuPBu4cP5o_ky7cm5V-cPlrXJe1CM2cVlZ3dLeZaFKVx2LEpXGJJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dtVoqU4kAtaUmscdcKEhyAFwEkKsimzna2ijgA6czmyp7OahbY4yfjq3snwl4Ttxq4z0FM9oLkaQ23X5dp1sh17HRJErcGYBM2RJHDsypk1A1BILAyAWXU89A0SjlftngB7lrVXYQ2HvSyGLyx9CCJppmDNRS4IEG6ZrzrvbBJXAF9gLp_F5p_6G1M_Qf13Cl2w54xe9TZ23yE5SHxTteVNNOw3l_dQ6PrRM-zHc4SXgD4B8GI2u8XpkvrPnZv5LQ2r7H6DeuhxwW60Y0I-3hTDLduCZ6Cfc_ou_WYR2iiH4PUVz4zPPjP6TpB0BsYXzqEQYq_raoEbVvpNo5miyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQthSwXs3Q2NG9WSa5bPjLP3ZJXNVlx_4g92haCOFSKuphbnNexPTopo6SXzwX4xM0jW_3wJToNPEw2cejpxxnq7KTzWK8ORCnjjDysW1dYMBoal6AIYsNkpINNgWsa7j7VrD4iprQy3cYwFchXwKYsMCIwuL2mMWoWrPAyhSrbrlzqF0HT63d0pR7EtNs7Zu09MwPQUKAkJ69KXqfxlMSBDUwqnY_QmDm0Pw2nEGksiqWYE78MR0L50dXeLYYum35QZ-AY1D-2601ow17FM3Et8FWN56vWIRNFKyzz3uNDW8bljFoCIb1d1WCChVIuAFxooaNcHSovtWIcH-BMDRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkaFtF-a4cvtJ09C8qMy7shLZJVYHPGjhNOLKffln7pTfqHCnPCp11KQEwVJIEqS9zgFZpkCjWERv96GURHwxB4fqulzq2LMiTsZPZv3mFOD6CMnRBOgjKP6CRSadVxhZ4ZXDnqc0ENJE6f-gYIFfSg5Y-c4oDxr2xfRf2J5hZAKlp4DXwQbrCbRtQFHYfDo1HzXpt0ioLvLv8lIljA7mtZMA-5ADlDwYyG6jpbEfRTIKMBsQ-5nnwImhGK7Z4SHi5xvieaZMKQckE2ZkKNyjDDdmYayy9005skdPMBMAjhMtBdbXRoWSAQ87_4I7WOsmRy-pljEDyXs0k5UhTtILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=lqf3DlQl08tsLZ4M0FknOIh3GTol6QsVU4A9NUk0XEHSdREEs6VxI87dmvvv7S3a-lVfyHflMlnobxnEZJ8fDvlXKc2yaSH0f2R8anlEC5eZcwJj-Cd-Z0SaIuL8rtAqq8ZNFE9kv-qnN08QmGkigIPwW0fRQZHovA0hg6aQmSIuaUqOvDdmVABiH50hdb-APiVPBhlmrCAkvvFtioitnw8DhNZeedKi_RQle-PX9-iKkUK3azAKSxcCIBKLvIf01kojlOai_HyVA8B2o31_4jKhsBNq3GMRdWMmwJTcNykoEiJEDW6s_4aXxJF9T77N_ft77HkvaquvII7vu7EWxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgJdeK89ZqHkIgKajFqjnLE1XeIN0lyCJDMvAq0RSnxa3rAwulYhzFsZ5pS2YJI-sebADmn1Zh0CSOS3K34G_Uc_IzI-eOEx56jHycGxIPwmMAWhy5zuzM_wBCL3qVW0pX8bHjnVucmoGKaIiesopXtlkBbr-SbxBGltE1ivlmteIKlP2FXrUjWYo16yvNLoEEXLgRda19_9VBXdwZool8wdd2i2YZkt1xR3HDRLOBusaeLYwR0negxwvuYvVHkWOzASGGmqokBcmfseZfaWwfjslO5Lx4XfK95H0ufNy1NgA9Z9vBvSdS4e6EzJBX28cogCqktE2kIV1quD1rDXyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLZl-qdFce9ho89qHZqbvusgOJwMuf1zjCmrh9NU4aG2c_8FrsF_WnRvCegSwwj6ffIhFLe_6F07c1Bsi__NIWiB9XRxV7AxCM4tqpcTFeZmM2n5CcLRWivTGJUWUpArYcx96FR5jiwzomTQc_boVI7bcXZQ-Fuu5gsB1y7z_ZrfnKt8VERzQdVblk6NbkKwwFQWVRK6wIdOxsCwKQKMlXsbGxIxgnfYtrv5VVlAWaq0OKhJUdX4cxCsvVW_feyb0TQIEyDh79iRK9tO7sC0bPk0cbMGtEGtaBRWIDS7rv9UgmQkUQvJQr0BtCqQ6xUpPleRT3u-a61DH8dk0ZHF4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkbTOHtIgbkJpoK_3mS6dgm-FyMKpqT72-NdJkSArBMYHs8_z_Jfv565rY7J4OL4pPUQwI3w3XPge3IVJNd9XYDtWw-vqE7LN5rs5mX2DubWF7LQMwWPisBwT7yYKWeXIyi-k7KA8rMZNxJ_Gn3xcdCDO4k8W_vifg65pGOBUiOg-KUQB6fkPfksuR5K5udmU44PETFk-E3LAHB3WP8jwXkZ4yBfgthzOMF_K9jmoML_mB_Rt2O1XWnczAkJIDKBh2y1RWHxVKzWlturcUsmvL7trUU9R6eZqQouRQRei5oiNXV9ZFY2WhLzTMAMjuUxSqQxKtLjFLSXhWZ1C2HG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jz5evn3oGafMeKDWZGLbp0X684XcnRBtuXQgDN6QDmUjMNuuM33cSiYvYeZ-xuOFZF4s1_t8_kNN4-S-WKRmLtkrjYCiOWQrgWQLn2x-8MjUXgBT322oGuTIo0AbUJnqodoFZ9sBLRot22Q2eyByeGtnE-VuNt2X3WQOBrJhW0Q3GfFe-6NxfCG1ziAmK1pMEzxX95wZ0x6SatrSil5rHIem4DoTEVvRRvFs_Ad68Z55fdZq9Ws8CyQz9kH3w6-8gWZNnFe_be29sg5p0Ol79SDOV3913x5kf3d7OLfol1j19oP9833i66lmjBAgG6UpsbYV1vTOvAHUq0tWXvj3vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlybaoHG-bCNpLc0sz6FFEvl3lygdQRImnYxaf4B3cFL1pQOmkymlW6dQgxse3K9q0HwScBFK5Rkn3JqWDX__8vAvU8e2hpV15jbvRfepJOARUweBoel4q0CliHaAdRk9TZ5KcjM2wXHWtY_Rr4YpJyS8DTaPi5wuCNrZpJbQHc38tbxavLEH45uaTOpSsFwz5B5tS01v4hDeOxKMIefvaItBbgS3Upk3uwHhsUdfFOhfNNFBfy1AzmxFHujuC3BcA_wDZuMBR_ED577RW1GqXFs1gWkn7GEKrl3P_-qGzwNlxsXE2yYjInRUP8a7R0sBxPkS0G5Q5hToiJaX7cs3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMwHMku0yUJyVxyLSXopNoApi3ewq0iGu4q0CltadjhX3uH9JrbTNTtZPhZz6DqNUHfNq00qiZy42uwGF7TtLd6E3eYgeINsNCiA0nBzAIulo95erAg77l3Guj_vFNtCvKiuzMHjeJTGHlj3Qc4OoOCUDwNHNT6P1o3JCOC_cL6R7P9gxDghQpvuXp2BXtbpllnCRbYbuKg-4vxr0Z_aQvo2dCNG2sB1KWODHowEwPah_wRp7a70YVa48P3QgqObm3BecRy19EJInHB7J5DKxJKUQ9zR2n9kQ42sj6aEGXNahOzQgtOE1MUNhEpKH3ck79FXePq0TySrmuf9_zx_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EwVIdoDGKd59uZ0tAf4j7HkXiauO6UpSRM5Ow3zsyqNJHif6Ma061tLYKYrDMqWEUOVm0RcULzWH6xDafLaSGV31r8UBjBj4zDRfu-06QWQPUTM87oKUpSadW5t6ThmZEqYlPZLT1cbVKSeqOT-77eKkPzFDZvbCOqBShYFYXnX_i4skADxb7eFrm0Mqc7eD2xQIltc8eer-p6psGZ13lso5yOao4P8avgBHnbNTUs4UrS1YeLGe_Lh2or-gaZ1tDFjMbs5u6AtHzWoLviDdE0B3t7wWA15fKLxc7eRo_Wa0L7sksunlj-qkBzPa0dMgi8ASpXmprMvp4R5lmMLuEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8YxN1_SypdcujgqZP5RPgLBEFtwHl14ztyLGT8cIPWqKgzwj0wG1tn-lYeIyYn9txX0u7CTjKRbsHBXEjE_23Ya_0f82uoXPbV8CVaOI_Wa5Sv913D_Yo3FI9EP4k_EmEpy5r1YdATg7vQR-AwYsDsKU1JwWNZ0kjbKdL5Wf_AFD0zExSvrXl7cafp6BdshV9LpYq5Woyj3pRy53OV9-JmRlwKaCGslV_lkx07tdAO4huG8ANJ3PunDrb0QAEgPdtvSsAq-RlRScIVCA112kcrGKv0jZRoIiuTWN9kG7evEKf66W29VLYI9AMLuXWH371cBO7-O6jxP84VFWF4OIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZD5iA6A8HDl-fTZIMz-i5p8Vtr4rpUipdBrLwzvFudB_67Ojz5RMs0Ki_5lY4DDHNqw3pRLXXEKPfZR0v2Wun9d0nNmeT-S6G0qH2AIuaG-D0V1rMamc4FMAwsc3VTZi9e7w_iZtaPP9PVrE6tQ_N_XcrMdQ67npSyVPiTDNs6RptK014UNNA-Pp6i-QSdJq5XztkRM0qFaST2i0iru2cCrUkPcnm0Sjs9qMlijvlzpqeThKrVGeUIcWLJ3HiDgpdwo7JihXydAVRW0YSWZT1WQZri1JtEGUDhieehJacg-fPlDpRQFts_06xSeT5YFuYjP7oN5y5QuoYDLPaosdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5mQcTPFfFovMMnxEbZEKFivCE6yNpL11gRv0RXSZSpxm2A9noXU-gGhGdJc-21wcaKjprPUTws7oKRl4zWzh20dqJqPz5TeDp2s4cDTriMifEtAcqsB0rlRxNyJVkpWg0oOZpTym5098zWSMzsAiW3TwA2o17x2ujmn77np1lq32zYrAeP9doyJg9GKPXFyY1q2ox-xgdu0u9hvccuUNQWrVgIB1WAnRRcmH0s183OzJ2WPkjkjPyOjCJBq935RKo3VB68bPJH1AplH0TQSINFfDbg5-V6PinUmv_MF4gwqUd94EfixMHy4fN6qIGOzWzqTleQTYR1C-JdlfIT2xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nepr68OdEVec23fWZ-ViqVEFW-5_iDJ0gHSna8t5ZU5w5V9_4O2tJl6hr4cvsuDeAMfE7_zUu4ojhoK39wWCOnR5shtqjiRndOHuHr_g2p1gwgMlsHuHJbyo6B6zWOtjetsmjQZYFplo2upPGyU2sWvhxl5aMLC-ocMtEsRojO5z_UvNii5uhhksBZTqmdRR6El03N5ed3-2rSXmrhScms2i2uIuJVSwUzUAoC6rfaW0-sFoRhjU77u1xYNasMSv3I5l-VwnzZvc71xfCmutahK1X1nV5vUuLExabUW6l72qWpG8mul0uxeyzDAVH7Z-DsHm6QulrZT0XdwmLQDpDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6BeGg2lqhiUorcdKv-t5ICG_GMWuim6CNn_SW-sCNa5IFLWtBk5p9PvR7AzK5-MOpGM87j9abCRepH6J9c3YGh5UBtmAXTNKG9u1DxxpNvm9BghsBxR_c6O8PJZZw_mD8AmRcnK_GWFCiGGljfxNfpw1tDHA1-BqizySfl9KjDkYE95uFQ1uoOE58KfmwB6Qaz_p-dHL0JlbCT_5qPfEZfnvOJwDcGeBqDrJi90PO-2wTQfABlilCHJT06UPhRGmGDYERDswYgwX-NHFrSVd6l9sDuzRHx3NCdSLeoqfnHbM2-Oa6xH_X20qBAvrrRgb5DPkN6f3gvJvJ6fRFBA5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MM1u2ek-E9dc_6Vx4A7GQ8CiqAh0fo8Qk27k7d7lBeP2WJiwFt-VW89fDPcqR8YWFI_ctJCH-iqJjuB1twOKL8LZIeK2P8UB3dm5Aw1NFTioZUEADUWJ_JtV_QaXbZklvukJveGxmnIJ2_JPvBXj07QgdbRckdq9EHrX_PuI2fotlXpTFmFDmzs7VtrKWh3WWYRcB5xtRH3MuSrRWkNmkQBMnc7mg3i3wIvVmgJpvQ_TKg2amux1V6nMc6wWkXWPDgOH72v8KLQryG52YhZ_RArE4rvJ1vg2099Mw8RmkaQsQmCbEyfPWUyXaqfcvibJb5-uAgDUmC6dVbewCmZkKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckjvSNCGI0g4H-KkRoTdicUtaTrWZFPM5EUueQbY3LKLrekOD0CjOFKNzaiqmEHHAo4_raRVip2Kus0AXHJsjQIpyHzC33XBaanNXy1WdmciZcZXYZ5UsAEyRviJVzuQMminsyemZsOPoiB613Quo4b8zBBsNdikyCoJLraZ6LP8g36kcfsCPOguAs5Oa59e35RyfwxjCHIf7ZFasDFnW_gck4s08ogoAJTPtvo4YxO0wdSKQzdzLoxSMSVC1NsUvh_IGLeSSLwYYQMZtagfFRvvF-kHBPujiUS7tSz_QEzCiJkL5LUSaw49bQ78Oukv0wQH9KbdmWR2Nn3tk6KLfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLFtWAxESLfISDlFpDz_TpYOT-DaVbDCwai3CS7-1BipNlHXg8pDMYlUkjRmzHaTVYeNbRlt7oju-R4f3urVFjLdb_olYMSEupfNREmpRHa2etUOIW2tAdPmzRQMokbodXd-wyvFBTortIM729NDFbdGWwnkFEeycpCo74JydzJvV-qiclJuQwH026W1UJyTaPN0jjrVyLRIroQBxLZ6CKoXYS2MNKuiJN2P3RB7ejslwz_dlTcGi03bdSe0locRkjLm27HqRRNrB-YnpdiX0YdEGn2vL6KRm1JOSZePqcIGDT3fwwQPhU8-N6Jc5l0Wv8Pv0nfRaUdGf2YJnEsShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1-vMU7k_gI4IQPnieaB4UKO8VOrtXt-XhpS6JLlwCJEADMpW0DaHzHciUj9iQI1Fb-sii8y-VEw5JeE9w6YqDn77kIIO1qxDLyApeu-JaUJixQQrhOpZ7ex_IWROIwoORADtI_XRB6LeksGDORBQQAXd6bGTovZnoMOgr6LeVovVur39tYgkxinnkLy4jI5eKo4lnjljv0fPVe9KeCD2BTh5vcit8J8Ffc88F5pb5NWTnHf8Pe-dgMTSOVul-h0AeOiSU8cvFNGkxnRvHge8wPT6rSsTsBklCJ-iwhtwoj2L1TJnH7b1grbAAdOLqKd62QHcuyQE2sd8xPqq5WJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSKB0YdQyxawWzZjGQublhmWd20qHREKMlJ5lqa_0NS5ce1zZZRsuWygA7ogg44kZ8B1tdkdDZRHPAMYwV4FdVT5r4Fht_Aw_TD27rkdjT_7SmbissBOJhxNpGge1Xrzh2mwFZFSwRYRo6mrDVayO4lKBUuPS686VizN4ODg0K05xn2vgHS26TUXNzxTcwKwzgsJ--VWCtlnZfSNLPQXagIOeMWJdNbgZgGyCM4_R6ikVWn9lfm80v80jCQ8V-eXfoqeRV0DQyjEA4hxcZNBCls_MGd__XCQpfFxMUrz6ULY2G6PIiFsOkb8ZajPekj0-J61pR0zl_2Cday5su3RwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0lp8Z43PmDmdR8f08K8dcrVl0tQnJLRUIkXGUVrWd7Ssw1lO7pfNWUaA7H17bbsI3i52JtfimoaAleUsisngVDGe3q-IPRyeYJzTgwI3LmLAWRvLBNLCIakfeGMKdpdBM5Cgx9M8jlUPX4pkXRh6ol8FOGqnMwieTYvcCAfGNS0PPJvkFcXfzqV12wofl7qMBRJ7yXOI77QXyqebPmbxFGoSiI69zvH-k1689OkXS78xeQe27btmuehRY11pc1s2wQhIPWu4Y0Rs_UE3jv6h1ABstcZvW3sFkGBo0R8CDtN85oZwwvUbqXfig14jTwVVDRG7R5EvqqAJaAqmMWKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5zvIDnlTRWjQQLJ-hUs_hz_nhUCHUUudw1m8C02mqGKPtkupZ021GFKTrw-HHZ_FNgosQc1GDz_0DZyfCk026m1z4a69z-IvU_Pu4wu3_F-4ciNs8as7F4TWem-L0S0qeJ38-kWtO0UOjdl9zHE7VMAs1fa8cgxPlSwY0thlESURRM3ayi1aSqV1uHr7RsG2mn77v7iwrwYJhTD4dIJiw1hEem8nFqLfgRzZuI8QqE8aOAtmw85dmFVhcrLAG-ytxxISUSFF8_AClRmpot_Llsfy9PRz5z76Dfo8N07whsiYbcdFZ4BY_pR0mr8-MU2-DhkWpM1r0-WMJCe67SCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq9Jul8UzPKXKJyGDZBVf-cDBiB3J2-wBKH3J7m9xtjtZR_a5Uk5NMTwuFn7GEgd9eYI1MqX1l6jd1BafBiHsoPW-wdTRyZ5hHrbSPxw765sC-54lOXZ-hEkxx_CtBXK_F8dSMDu0gNjJw3UVW3cTs-Du_YCP4PMuJpwdseV2yyjahx4sTbHo3yJSGEtswK5H_CCZ_MtifpVzo4XyY9arqw19HCPCy1WSIXn7HUGPmM6ekVqTts-DkKIS-VU1q-8F_yru_ciVgo1vlwnK5X0JwcmT20qr4FYeSfmkc4ZdP2AUG-fZJ7CnT27bLLyFTlUOshuuiLp9XzBotYPN1N0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_EaOyk_T_NKGi30FMFoCWlD7W7aJRhmwdO0pKW29_meBNINJAjtOge8P3iuKeqYsI7uvgjs0DPmCajUMm6Onhx1N1KqKgolMuPecCOrxgD9log-LZiYVERK_P5HgvGgqAqFFhKEA8EeteFr-fQg4Q4GITCiR1tN9LpJXzrNoRanZ2hCYsObDHOxmyJAUm1EfXlHNltPwJjVXO3hw387GEEMI1z1RynPWK_8h9M31NN1c7r4Xr0ioKLr5eCmU_7McgfRy3RWnrCK1rxU0IR3qIVQmfeOuD_6OToU9WvGRhZ1zVIqEpwH9pbbF1bLl-FNfoOwby-Pv5OXy9BVrddOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jo43SdcjN304IzBz1tuaIizGSBuP_VOoWphB1Riba9BeLd3iFzlpqRGxM34vAb8G54B3_61PWGU_I8eNIx9yAd_Orf8xQNrJY3CIb5uz_BcZcCVB07jkwtC1VzSH7bEQKrqNvo7VeFbXzuKabvm3EkqPqIvPJGmSQ_m-TNZle_7Oyj30E7mX3VQq-2D24GT81dWyeHvleFk3n6h7chJYXqhalHAD9m9HSVWCUUTxdeGGFLH2cxJQT853Q2-p9ijkPLKZ9Yoj0GufOhu6dF7U0MfeBhh2OCnvTv7vj4_Xd34l2bVSw_0OvHcWyz6wuk53RyrsC4leUOMxJrtstSaxRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqCCynJgeGt2abELKytb6miDhbgU7tO1mJn0r-S9xpSij836XP6DN9cevP4Q-v-UVxBDrvRH71nK8-dPzdJFs1cwktUNhQMLyluKu5yGpqQq5DP5Jr7xw1fo6mgeccRSxctJdxCM23p1dph5NLuGWwhQiDyX4A1YjDO1IBvijEFau25tf7KPYlxNyMQ4J7toLhV9RM4VuzSJLU7eADGqPeqxbz330Nf6-aYL7xP5icLARgdyWBetpHuuEvkCPwU4iKwv-V1HyXzmzQqdCFhRssn94QQnccQEqWJGV0JJramwYexFITbb-nzG1OmCAMC1z-AxqP3DrEJTo_tfMKWm0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=VHlOrIA_hqG9tD6-a-Tjr8mCJg4b1LXU_CJCkkSf9LdAJKTpDU2NYsfO5GnbM9Q_vaFJjJtrhKEjV2qXBLufwZRXMco2HISn3YAigvVB6wyZHqtPbJCmaIxO5hKHBwRSfUuL9VkAo_eRQBjgiqBNRm53KmXDVa3N-V1Y2Od_0dgcNV8bkCGHKFfOofM1sSKEVL6yURCEWFO-LkaO1Vu3CRYB1Gjboaf1uUFNCgKHV8l13szPfDObPobGDPydLqzz0Jz0O-nW-0NUMkGAvX6hcv5xf3RiNA8_KDBWKyklN5ggMjWtY3ArleLEGPR3Uw8M5vAw9_BCU_xXd6_z3f6QyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFyuARl2ePHuaralyWOKY-7qZXfGTW0rARLK0gOoD2ii-eTbKG5Q2uMPgPnhQQwpX9jn-R_NDKvx5mSSROGxxQaU_zXYqXW1Ei1NiFHGiFwhcFgDZvR0J_ey6KNZF6IM3A3BSESYsh0_8LNMJCdxi_yJWAHAdLETErkYoBge-ZhZuVwC1GDzTjKS7i5zwbQqFPQUHYt8rAhe713Lm8DNzZvClNMnBSRkpQS9XQmmmmhVuxuQmlFKgUt3y7yeunUJSE6ccUVLP7HfWXraZIhEyN_UL_01fr2p1KYQxPub7FqvR6g_2i3caVoFHmIrD7DLuNRx1tWZlgE_n7oOMKCDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFRFjhiAz4vzMf23YcDN3w-spr5Dy-QncpjEAe-DkBax0g05JfBt2alepe4VuMfbyScYh2oO7q9uhjm6iGXXFeRObK46rZSj5Q3xtDAfGAAoDl_XOnCv1mP7VQSV6clbgx5OWcTGSbKL4VAU67L1Cp6VxB98PNN9mEV9s-KT5FREKbXWtcS9-qtcVek74c8-2qWe61DB7J8hnwdydkdv2Uhns647OAunq_psCq8cBCECISrQVMjIOogD4cPDbIxb8mUHuHGZ4ad0psZejV6G7eU_aGWkbd5mL1666bmcXAqT3WDBo6ft3Dc1IFC81mKvKU8mQfq4SHqgW8ixUw898yzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=dK9SYNWcDwUbHirZFn3ViVtXgfGEifHt3MT6MbqnueBrFdQGrgTbCUnxkJSfzJH6f23e62PVNRbm3lLnXH8thDmash8EoQBivkU3Jz1x7fH5hall8ACTJxKsrmBOmPAt3roINFWlHujebNX_djoeGnt8rvv_HDPoLdKk6xpQ3_NK8w-kSH9NktnmTBNGG8JE5oJcT7842cY5ETur2zq74-x6Iyopauh2I_A1Ppsm0j3QxRd1gXylzPIrl-v-4sEUUgSJwoQy0tkJny075pxpj2jv7QVGC1pUGqoytXWlPEMYVuVgh9CU-aLIFkXajQYhxxJNF0G3PJJjzlvfJL2MFRFjhiAz4vzMf23YcDN3w-spr5Dy-QncpjEAe-DkBax0g05JfBt2alepe4VuMfbyScYh2oO7q9uhjm6iGXXFeRObK46rZSj5Q3xtDAfGAAoDl_XOnCv1mP7VQSV6clbgx5OWcTGSbKL4VAU67L1Cp6VxB98PNN9mEV9s-KT5FREKbXWtcS9-qtcVek74c8-2qWe61DB7J8hnwdydkdv2Uhns647OAunq_psCq8cBCECISrQVMjIOogD4cPDbIxb8mUHuHGZ4ad0psZejV6G7eU_aGWkbd5mL1666bmcXAqT3WDBo6ft3Dc1IFC81mKvKU8mQfq4SHqgW8ixUw898yzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoPC-1ZNM_aZvZ-UUWYdDcGYZJADzw5KxEW612l_12UUeieIBmE3VIuSEWgG_rU68TpvNScZ0w2A9nhyE0bZzXHpTxP_DLDrc1V-Mnk1Rt-wK5Y6qHEFHqfZeUkgr55C4LTCfQDlvDS2R-ongHU9fCZdQczNUc4eUN-RQ15ArwWY84-Hy9fqYuZbA8eDdruc8IOXUsHzI2s4zorole99lNfBqpdJT4DvwubBenjXeADK0mmS4ouscM0oBWc0jFGUCiFuqVeEVNBbiEkhZh3wl_eDNxrdDa_71-xto4zbRsAUua4SKJ7GkAiz35b-dMvtCs5B3P6R0XBH1v2jJckliA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW5lbZIErGgblUfNTptz3uqvD40NExL_CrDhEcINYJ4iXwNzRv8tQ66-WzcKiFBZT4RDieU7avXPwp7iVVpY3zwAujmwGqkqguT-KCJbeZjgvL33F6W4fJgW71HAbPEnFNWi6GhdaEO8EOPblB-2gB98MHVCpllRr2V-T0oBaoUCF5UfpgGndYzH1psVpcnnrhoG95YDfwPt9EfVm-LJOP22ZkdOJ7JD1SI7tF9YssmxJla-rO9Iej6c3q8tFcgmU4btDE9o5phXgIuULgCqp-J1cMJdxJiAhi6sUggskDSYNfbK2Q3k5IrESY_1ciNwfBX13ABial0w5XQ-CAEo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz2Ib5rqUHRxn90iHcoO4LBNMQlqcdXCcY2hGCdDP8YANz0QNW5EKVuO9TPr8hz1zjU3a8lj7regCoRJrpUyb1F0lIlF-iDHTnUyxxjZcnhGYsATRllYEC5hqQXYxmLrm3IyT479ovJkas2nKmCBHgSfme1lyl_X81BYtGPn9f5J0mVr-o8urMiQcs06yM2LHokdsisc9EVbQDzYPHGWc8f0prz2BPrEqDjsti5rhW2VwjCa8a6S_D8zH3ygw7eHwbSKmscVQG2v_-bJql2_nqnazdThYjrwsCbamKy9p6wZVUaT2TBv9ySlKlXibFS9PJrlak5-Mwp9MespczZm6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uOVyEmq28GseKVw_PAa363HFAAdQeo9c8Mx8wol3vONXC-Gp3v-A_JonhirtO8nqS0zdM-tswZHM8JjVwGfT0hR_ImSmxr3pyHsj_PwkOSwrRo9GMd-j1-2tziEwXANtjRtFffXtjIIZjHDoJgyld_lCJgdqatvmVDgoSNbJQWK-P2L7nD7jem07S8JlSB9cPvW8P5O4QAMwmW9f_0-adg7bqgdQi_6KMRN_C96mZ-qt5Ew-FTJwQssf1jKuXZ7jtYFefiMbgK2e3wTRg8MqDyiJxKalyFclrMz3G_CKLpDM0E3cZy5Po1TvDMFhd1ZtJPDCKGNN_380zXD70aCMeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0thXY-fvsnr2xUb37Dqks7zb1BR6_jlbTXtJYGc7APH76owOKLr6w8p1rlu0WP7fhf_GVaSNbtFYt_Z9DctkZV0zHuhhUapoxsCIXF7_zu2RcJKrvVf13DXiQVYcwWaMeVIJVBOMVoiIZtkw2zcnbmkvjTLGSpezh9hh3krwFQ8YwrjEOya3QXqAjkmE8Ulwz_wUevF9YKSPm3KKFmcFJjfYJYNgUJtjBTnRATf725Y74t3Ma3saCi-BU4iWbPRAUxTYOc-Bh0lZggPygrlV59r3-2NEJ0e5NWjGE3QA4x-AYZvRtsbtg1tZqNLgp4zbqydvWkyHifd2gwZk7slKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJmgjmlHt_zu_qshV0n_N2CELyi7GSrZJgLqTN9UaC1eoe26UJeq2ja57UjKw4l2bxKJU_32T3NB65se8hRqLBIhwicPa5ZvxavGBnaA_rCSxjWTTT6HHeJnwvyP3ItJjnswIOr7014-GODwWT2AQyx3A7uyuJsJvKVoHrX4vY2WTjVPrf2465lFWPD4vkkZGs8XEN5Eka1OfE1C7x8KuHHkcsY-pFfKRLgywFQG-Lbf4j3P2J_KD0YTvvvI_WaAD0O07rnGRUGjNpYNBjoz74oU65nxLs9hIMZhtPRim23qDLScCH8tHprcLc__NkQkG_7dpVc9unlLwq4UzbczAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2d-KcFudliRPfT4O9oG_J7msLojrEPH0lmo608F0HKoaxLL6zh_75I7G0ksnMGRr6mwdGwEFNVcyU0fKnFEaV9BB99nF4a9YF2FxdCdbEzfw8uBQgytE_m24q2wzP-K1NtjacLfa3OJJQXbvKvNfTsSGwn8sMaspTc1vuEycap9hWRoE4sQWGl0oZb2zd0N5qlB_0aFSHq3oKxsISpmcfBTwZN_Sn7I6W7VV50t0vDgLE0GMdTBGu5YTrhg5Y9qQaaIrUiEoOYT3vY481x9wx24Ut1oQbWR0kyS1ME-FV8NGGOsBTFcOBMA8YmU9ttTrlIelBQCDzdb6kBbubXtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4HnfWR0t4thdLR_OPTuZ6mkTnZTLcl2LFQR7iTR7RL8dj1BnDqVkdnN3v3V5whZ09w9cjuRW-Zc1DQXn8mV2qXF9AFUtnG8BN0svWuDAY9wTJanhsqO4sLGMiOiHcBIzHGeyUMHGKMKqqEpLMX4TNdmx1yAFp0Rn9MZevLxmr-glBvREhvJEfitnNCvMe2-9a8OLeetvEp7UAMpbm2MLWpUYeNY8O_mxaWiFpr1iKQrzLf9TwkCAltW2QJRGlTBIBX7NtqHwJfyw_90HIjGgDkIveueLah6l_xMLUhw0CXLQKaBnDPEYeWrl6EWrSvcF8n82yT8Y_6YT1p5wgOgBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBArmkw7XREHOJt5LPRO8Ma1HiBF_xp16t7Wtgrw6cDNlAUBAaUJixY0xTKtfZfIMSZnNT86JALDANlY9VsW45r1yvjvyf8fHBs0EheOp1Bv04sfQwTl02GXXobI7e7utkmeSw5AR0xZwKK2b23TdEfYTMYhLq9Cv3NDbDPdlISdMT4AaIWWlKet2SLNvB4gCx2jXITeCKgG28EzE_QlaU2-L9aEllKdH8yQEarJ-RJ0He7WvTUtx3PD5ZaKt5q16Z1HpKV87-0Ez1b80igx0FqhKSSrbhgOoqsSAs_sUgNkc9a5x6o3xf4F6nt4RHgxfDBnW--qLtO8KwDxfPzhhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pn0AOJ_m-jAebtrppF-vp-E-wlCRVX2WquoCA7f9_nkYGbGsxBQfFbxY-5V5QcqBVHU3gcZIvJu742UmrzvB21YJ5OVf8icqZR4D8ff19DhBQ0df_McboxV49Rjv4zoFif-W-Hpg_EuFlp5wJcqqG-DWZCTGa5-5Ffxh6dftyV3qEW63zKM6ZhgkF7vNww5SjfTsWNBONlxxYWaPD0YxA4elUBh3uMg4JR7Sh99UL3SgoIJ4HJqA6mgxEvk3sbBM-KGe5ZhTOSS7FNYGAuwmopRpA3X5Fw-K6fITNi9gQQAOf0ntCA_hy9Sxz6tp4CCAbSDLfbj6ni-mTLr_vZ1bLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUFN6LBcLhYuxngwMVJhPRnBDKkx4k0Q92I0uMZ5qyDb7MfhmNaUM0VCzP7fxw2knbhD4bLkiBk_SJfLn-ykPoKeKZsG3UlUMcHhez9tMQJHi7vrcJI8oDyofEGVdiU8zfMBQM6E25rK4ekwoReM6URES0kjxQ0cWhjxG18SqeB0pVHmegPAJ3gUrv6JuNk-TOj_aEDakXQw1w2fJ2D6pfNPjAOX0NVOj39WTKmVALp4Ren493EkRbB51TVZ70WXapvQcDGlu7TOeqE3Nja4-D2LLAs2sUqWeDq8e3Bv7q-NjXxHZdGLEiQqbR-Dfbu87uorppPB1izlsOJRaK2kWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Pmq4qcgAbTx08n5bc-APaBgV3FDF0hIdw_SxVTxLCy0cvOnOBnnZYGmOrITfHDh7cfJ_xvvjXex7j2ii2ATpqgjq0G-tPBmTwojMDEd_1sKfBuvJB1-95sYH6dklKHSwSLeO0SmrlAAa6uypfBYq_pHcpbQobtWZjKm5u2Q7E2dqAYPhubRL60RgnIlClHYtZqgKfyW1WANyIQLfaJ-oiCg9vpkvyPJVa-cHThXCePKZbN6-qbzACvhttLM3HNSAD70qCXTAkYndHti8hgU_-vspJkd0ry4cx2a_97D9AKrZmT_D0xBYjouQqt4czWBedOzJbMan2Y94CubMw-kI0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=Pmq4qcgAbTx08n5bc-APaBgV3FDF0hIdw_SxVTxLCy0cvOnOBnnZYGmOrITfHDh7cfJ_xvvjXex7j2ii2ATpqgjq0G-tPBmTwojMDEd_1sKfBuvJB1-95sYH6dklKHSwSLeO0SmrlAAa6uypfBYq_pHcpbQobtWZjKm5u2Q7E2dqAYPhubRL60RgnIlClHYtZqgKfyW1WANyIQLfaJ-oiCg9vpkvyPJVa-cHThXCePKZbN6-qbzACvhttLM3HNSAD70qCXTAkYndHti8hgU_-vspJkd0ry4cx2a_97D9AKrZmT_D0xBYjouQqt4czWBedOzJbMan2Y94CubMw-kI0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZ8MErY_zk2XxgK5GMxYE2uVXZ95E6qHTShi_6mgPP3GF68tTioUesbIbVMliZ7zHnVuqqYBWjXscpmtQqYDi0yhM9ODpnRo8IQ4OHp0R7uh72dQUQEBUsogM8u6UirDjqLSSShlAhkGwVul1xpVaPBkfYCauv4xTz_4JOgZQwvgIhR9HRelKOSFvyv2bof27LFMfRhVRNuW3fmk2YDH8GpTBlUPXNbqG8ceyd_cBBL5C63WtB2ei_o185AQdvun-BYX9LVN6AY_Unb9WqKSV6oJDcz41QOrxut5e-TI_HDRBPZjq5ozxbmtw2bAV1qAT84KGS3-PQRCQ5D1c62mCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLYWdk-oJVR1QsSQbu-dzj5lWMaX9mye1y4zvA-6DiE4XutfSzqIUC_bLjumWo0PGMSo6Ehpug8qMxPEsmdaR2nowEq-ZB6-U4YlaweVm0gigPDYjkPGX5SvJuDK2brTzgE4p-8qFupUL20UOVyFpT-1QlzL6r3c__IavqPnpdAy2hiPhbGCQA4oWvBwyHUoHQTsgUrUquOFHkfvPSLjPOr3PFV_RtecBNIiClgoh1rFMzekfBBGutdlf1pCfkC8pjGbJ5Y7ojIEg3SnSEhGsfqOsGZAh9CepFqIfJnwkzxJ6Lc5r59Qe95cTTJ5abib3U6yynwJwOSDdcLHEXfbfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uBHYHdH8VNdyLEIejyE4j9N2MuxztPW_I0x-VpyUJCbvFLDQnHSk-5j-_nyj6kHBlkqRBXm0bZl_bY7K80ca9RrpbRwBcnxYHCDlv3NGCiW7JKn15vHB2aCc5uFn9FL71HBgzrqfncjp2pWCe4t9g_XPIcLgLWMzp4thbQJ3NTFXWaERLX0gTkf1emm0lKyAY1EJ-htpb7eu_y-cls0gp0vR1lUteQxXQLdXLWFOjS8slMHzcyxxpFl8B75tL9_1WeEE8pL-iHJC-j_wYHz1PlN6s_4aZulVrBE_zja58PE4csyH9D8ssmWSv_SBFYLZdW6DXZDAvOWfQBhgC2_Rvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGy5NTNFWvUu-Y5qkoJLewTwXmLUnDXVLi55zMmf63CnEy1SztuFIA_dusUO6Cf6L5JHQjpZ7WMtfucuZisfVQw3BNzWFS8WmDAfGl5zgMt1Eun46_dLF04DTneMEYlypnQgDl71_lCaNdw2JNsjZ7DjdDLvp-Gtm6ey3pd71afw0QtxN2zhCngXuKmN3GS8LXlwyCnsvNiJHziLaDMKNk73zWy5aZeSfRw62f1HlH85tNdPsJZ2qUEcweGIa9Gutr_JGCr9Y_Yeo4RUoamp20QTKkld_egJLPENRhouadjysHay9WZ_m2VNmUSikFfGFpnXyHbfOLLFyoHPr1MvDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITVwCMPKPHfaGGmyvSYSVIw40X7RLC2t1Q-4sIjcvDPNcfpZcRNawRxAqp52DreZ2b5r0IXDcC1REQcXnLtXajlRJymXgQS8O-CyjpLzWhkNYUUzxiurESu2_ZdqBWosSfQIYkKXB_oV2O5ECZeuUEuMqGO0cFe0m2ll5QvvWrp0SArjADMfU2y3Vslm0e9C91oSvtooGXFEzeEAuKeHv_pwxjTYltlbzJ0R3v97SQZQKd8ew7q9P5LkCeX8w4AjRmYtziKpum86Wsm5VYbrJUsCz49Y05Fli1xpAXokGo79s09afbmYE2rRsmEDLg68jety8BFF5FZ5EIVbEiM-Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVQPUlTKK4nxAlXeEgHrSpBXg6mQJ_vxtsjshL7S_mMCSCRz6TW5FAFGkpSIWQQdgCaAO3_FPvWR-odQPQOaPRDew2s46kXYmRJ1NpmhMRIwY2HyzsVShOJUcVzlxik3f3JNHkCJAO-IFTttJFdsDTXGgrOKwVNt8HYXxt3Dy6xdw2XCW-STd0Eva8uGn1-zfInnYolzL_sVmsG4G4qgQT7ZhzNp9e5SK8BDeI_npezbwCuGE6GjGzRuOzYP23uyeT7TjA87cID99U9Gw6WfVz2gLRNsMRMRiG4j512cH4BdhjIA1YwHkd3WG5UTMdia1HMiSZzRVOXx8iIyIm-6eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-5oAVWaPvqrPtAGKCSwYmPo94AS6INFwy-QkYu9f-Ett6RLy35JdEQb3McqR5g7EACoPoLGHbsY4LepxPSCquok-aXDLRJUX8PpJzuWm5-uESPhs9io2ezQCEBSozFH0tyoM2B2yOOUpemLIMGArbLfdIbMm0Ry3twd2RFUAW7KYV58-HzMafGrin1ZHWC7nm6WZeAk4Q5A3AyDuV_ToXwSa2SvX6Kv5kXd7fmKqqrr9n58HK4pVCuqDBXNQXSpGEtNxl6kpj7A_lyxerQkAdBLEJSEjl74M69Wm_UgHWPOZCiXr_fRc6LD1ijRmXH8HV5YpHwMfy_Zk8mcHYYnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ElTi6kE2ANhmu3t5xTT-hmTiUgwjIq49HtsVKLwKH7cgy8gw8g-uMKE--yIRE-C4B7HRlwiZDFhy9tjN_t_IiieUTenklpC8Rg-FX2nXr3WK3eGG52cWDytgdu9RaV_iR33qwkyChvIApUMu8P4OEgsTRAyafr4XzZCqtpA-FsGyHMlY22DSEoO0B1NuvfjIXbmwn-EX7Q7ap6A0Ot3EjXJYn-h0IZf1YKP8SLXbGj7AjBtal5rqMJiYK8t3u8qOFz8YlVnmgJaWSWnQXqQSms5F_cktEzkqHH8YdeNlyCkg0O8fOh7ytkN5WAgwaLKAqNTbV-UFdzKabVIjQ2HLCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=ElTi6kE2ANhmu3t5xTT-hmTiUgwjIq49HtsVKLwKH7cgy8gw8g-uMKE--yIRE-C4B7HRlwiZDFhy9tjN_t_IiieUTenklpC8Rg-FX2nXr3WK3eGG52cWDytgdu9RaV_iR33qwkyChvIApUMu8P4OEgsTRAyafr4XzZCqtpA-FsGyHMlY22DSEoO0B1NuvfjIXbmwn-EX7Q7ap6A0Ot3EjXJYn-h0IZf1YKP8SLXbGj7AjBtal5rqMJiYK8t3u8qOFz8YlVnmgJaWSWnQXqQSms5F_cktEzkqHH8YdeNlyCkg0O8fOh7ytkN5WAgwaLKAqNTbV-UFdzKabVIjQ2HLCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=iCfv4TZeQpOju93aAoyKmBUl7vafkhxkNZPcRE74-qGjGZpaXAeXE-A5QGi4b-1OAXd94xs6pSaVaizBmHajmpL5WBGshsq_gnD2i8I0AqXKtq7xRLBa06a-BByJcSDxL3h3YZIQTj7_-157vX0aarAEYxyZ7HOxlBT4ZNNZUVGTrBGBDo6pO_blVbBJpfzyZjiHY92OdirNwJbgvO21UjhcUXHDU4yiLd05JS6dJNUUpURjhuG447in9p4cU2jU_HTWG0C0kkogiXCjmatdvLjyUf7FzcPvOV0WsexI-jmNAzwzKN3XtVfE9gAFSg8nc94R9z-OfSlxmc2AMd3sXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=iCfv4TZeQpOju93aAoyKmBUl7vafkhxkNZPcRE74-qGjGZpaXAeXE-A5QGi4b-1OAXd94xs6pSaVaizBmHajmpL5WBGshsq_gnD2i8I0AqXKtq7xRLBa06a-BByJcSDxL3h3YZIQTj7_-157vX0aarAEYxyZ7HOxlBT4ZNNZUVGTrBGBDo6pO_blVbBJpfzyZjiHY92OdirNwJbgvO21UjhcUXHDU4yiLd05JS6dJNUUpURjhuG447in9p4cU2jU_HTWG0C0kkogiXCjmatdvLjyUf7FzcPvOV0WsexI-jmNAzwzKN3XtVfE9gAFSg8nc94R9z-OfSlxmc2AMd3sXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4sla4rQnnNyxm7e9a9cUjg44ifnez5vDqC6nmQNyPf4-cdCqgRcBccEbCzrvF4svEgDRqkkdYWkQ1P0UJEtMrRzb4p0BhaXcZWBXWXl7-oWGMCyEj6xeZotERgXueYbQTS96qN2h3OkcCLSlkujps6YRdat_M1m1_ypka-flv6MEW1au6xSJ0s2LlZy70Bl5mUimifncLF0Mjonwy4XJXSsak1YGVRLX7PxaiyhIQ3yNp_KqbC5r4SMYp6BtNTepvSw3p8pCEtmu2jbxAiBBd8w4aJCNTjugKI9ZpyjidiQKpOjhb5MkUoCpdtdG2UtPVEhRMTulChjVebIucdFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KfvanphqSDw9hTMj2hub6eV4zAGf07yFYYiqT2qSoKPuioz0R40F_F6bZfThGWLvBUBnHU7zcCPQWRI1mdOsnUwZ9teysru41zBPBJ_r5aYqgZSZeWCZuGnLi0bSYZDODkt0cu9JYVmVeZAeIVeelOtJ57whX4XJNB1oKX7YkOLAOX_vTLpKuKrxOPkMoNZwh4Oqcg9PbR0jndTh_Ao-oig-vjfbSKkA40kaYM7p2638Xdu6dpRGmtvH-968MVvsmG4TmIbQzpJr8gWvmuRkfHS7YrpAfR8N5w4E5OnWEDrPZhmsk8Eu5HAvnbuL5P8P_CCnGAwnZGQp3VsZka0z9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6Tk4ypXgy_9FO2y1rS8iWe0TkTCDWbYO-ZHyuG9uu_f3wiX1_P1myFTKeEErvUiaHdfg_p1DjzTmJRt6VbKOLJzS4yJImR86dLZV-tiAc18TUx5BYChrqWgqOAu0k6kdFFCQ4WUHHjbjB0K4B5fYNBI9vyjvKGp-MDK6_BHF-_5w3Y9Z1l87VCzfC8xW-tXVhdlWUDSUqnauJnd1cBf6RMR2IVpd_IhURpWrOXRSiKHxUv__3QBQgbmfbaLzCf9kKgcoLaMh3LMyW2r1kyBLGUrb0Tw6IYVOuM90tEuCPqdQn8zJy7daDmdBsYur3pRd_lI4qgYbiTfg2P-qVXjNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ch3hJn3lxFbpv3hFPTjNgZjeLhK1twkr6a4XZYj8R5Ol372lYKKEMDTmqpcX56YB4uvtRoYOZgm-GbDO4z4__vpvfhsQMUoFpckFK0aB8VbfkkVCnnUvax6qUUdm_ddLIMtxK_u7ry3aW5t8Wgbr5bd0ZGOlKsF7zAZFVWJoPcjIp-P77602YX5YA6Q_ftGmqCnLxZXqDivDK5AbjzZVwpNjG2xay4fxJIQ4a9FASBOmLaCogtanSEpxN4QNxykGmqgVN_H8fxPXp7OGX1TupkfopcxOT2yQlxYI5TAYpTDCV22xgj5oTZ1l419FflWhzdCynJxKq-aIcgozcaMoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjl2XgzXriqLII82VvMuFul1Hu7V6JeTojyJLGYKrRpAzFJlioXQBFXjuhtaxxo34pxR-NcW3RHn4iZzm-rPuPfShF6yLtPgt16Z_e2u6r-pwzeV-HBv2QuzMaFXXnB-nwkWXSlSOKDkRw1Yug7q4kZkCMAA24_yp4ZxpVymo4o7eAQwic4P0lNhrImNEFUjJAg35vjf5jjHhXvlOVo39k1L4afQO7591eKlvysZmxGiqyxPNEZgoznMm2ENNrF4vyJnoli9sXj8Dnr3hEHW-Rx3Hu9WrzK0HpuOcmmvlDc94WRE-iL8WYgJmGAYt-VANyjRdVKXDGId33tKnSpjnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETPF84uhi-70sjY3eajW9QYyGGHvFmicIZAhSkknUnCpMb928ywVV2X7QhhJB5t_ZUS_-xhh23QoXDd2skPnFFXxdysJ6W3MWJahtjRoQ032d5vepgGCzNPAoNtleqcOv5SWAvJ2B5XV__NVKR0v2JjPFpyjhjOM5M5avxjM_v1eKCcTXvLcHAnUAw8_5CNNJCaZm9nE-k6v710XmHIbCKPnqBmOoilPt-DD_FzPw9WZeeB4_Qduj3EgTf2AcYPn4RPFPYxxXWjWE-ZHiJC1Tw2mgBqtAk2Pn7bu-xhR-AlPAsa8IWsHbB5ne70idpol3-OTbP7aFji4PZj6VJoidw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=vgPLmtkdBTjrEvT-xap9IW9qzEMzp0HXost3LmECfwYZXruqW0eIF9_EzbTbGxsuKhfz4hsLGPxy8gdBy9Hau2laAvWNuwZEVLOT2UD_uu9Q3vsAP1TUO_4WbZLudGO4OApAvRTaMqNDIRKq-KzGnpvGd3AzTzXfhClgLKj47SSw1ym836NpMWjD7jHkW33MXUMkWWM7CoAOK32i4occK02YkASgo1YAAX3XyxEA8IF8EHHKqWOUiZqGLOLOSKIjvdEBbbRUaIjtQmSsSKey9ymGyYRsGEf1-ho8v6f5JHsky0zpAvD_6vmQEFEKRzxDc41rvWrHkgbB2CLBJkzBfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=vgPLmtkdBTjrEvT-xap9IW9qzEMzp0HXost3LmECfwYZXruqW0eIF9_EzbTbGxsuKhfz4hsLGPxy8gdBy9Hau2laAvWNuwZEVLOT2UD_uu9Q3vsAP1TUO_4WbZLudGO4OApAvRTaMqNDIRKq-KzGnpvGd3AzTzXfhClgLKj47SSw1ym836NpMWjD7jHkW33MXUMkWWM7CoAOK32i4occK02YkASgo1YAAX3XyxEA8IF8EHHKqWOUiZqGLOLOSKIjvdEBbbRUaIjtQmSsSKey9ymGyYRsGEf1-ho8v6f5JHsky0zpAvD_6vmQEFEKRzxDc41rvWrHkgbB2CLBJkzBfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7If4mfNeIM0bHhxsyYY3-eohkK6Q9WP_cvVvqf0OtFizwgFV38036h6SBcQXEO33qhwEy1UV9F_Nx-HUeUue5bQRrBGKKiASdkZ5pyB1msapUxcmXmekImpCBvKupZY85_F0QIZJuPSuFMEkP2pPuKjFzZQd5G74dmywf4gtH6a18XQgAoCHE4OaxwI9KDQn3WpvtMyDpdH_0n4BWWdXNG19lxVefpPw0BC4u0IJaEahDi9SzDxWlk_ipvsYeeK4XWJhRxrs9MolSmxdjfCoLU3Dm87kMkZuVxYCZXxI_0pNQhYELZ6tKKCLGqzlH69ZRgriUSf4B_DmFetWBgG4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFik9Fvw5d-MO7mCG0r-VRwrgGdwpeL-BZWUtRonMH1FdMyLw6f0-Y1AzEygOBZL2Nu4qy6x6QmbUMf81osi73otdwzPhNWs5tdUMyPpnvNNU-GcDReH6M-NtfrqyLEcZQvswFO_fiAZETEnLra_6tN6_9qoqC_f5uHJK4Phsj-inl_CgHvOa67cPWmktWpB_oKHmngBbZJ4sOrz4dRNcZOG4QkpqzdJNis7HFjMVq03LZFg-Cas9QloGXvNFJc4t113xoyGDcShSSdo4c2MfDyT5Y34Boh4141yHB0Dd4KI7gV64T8Vyy_n-C04crytzlJ6vOOXVXXNiDCucWNUdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtF0-ExeELpXXOwwmi3uNwg5TwKvQQfB-qTkXZMlQkd-lZqmc9nZNHkgdq56XFOSfr9wIVxMU8bOSY1lYYqHpPUko5FDPlbcvV4D-3tAVXzv1uflvj1IHezoZu-t9x76v4YKaTwpnX5bSFru7XTlzzzCgsccg3UQC7mfYI5-WjrkE7vzsWrtqXgtiX_KMwCa5A3kUa0WBDkwDTmWV2DjJJ4a93xzFbTPF1wIVYhhX4Uf0hN0C77KxvzmAtCqWgWZ4j75sZHbceQVMIUvim2xa3DzcsdbzLF71cz3TBH6pwpczGd7SDoMfvgPCCQoZUXbyIFyqT_wE_MPfs_ZDtsovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcSCZBQRFkgjm_xhtWIG9Os7VIf-iOJQyBkj7ogShvPoZ_J8RdDt7SRLanjCkifDClUpX55lyaqm3fYBooO581VYDka7v5xUWV5Om2HditU2iiWYyvnFl4sC4YbNTxmPidUf5EpsA9SbwwZenGiWAp1GApfzx9bK6Ak0CmMatZWtihhk7wFRcyUbg2tZufcFXIk4Zp-gV8KQcULjJ1-lky95TZ0S1HGWW-dbtANJpEv2vkOwoU2So0xfR3Yu5ajqMOQ3DmrBQwu82XJL_oxajtyZEYMKg5w1NAirm0wq051nhoy1s3B5Da-9VNv2Sb2-21nohaM6hRjn9EEOmed8Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIptBJuZMMHC_LHhxpn2cXDL6WmVa0k-mYC2oEsXpzSwF8iruDdTQF-suN0wSy-w8-WpkDY5Sc8rOVis_ZFg_6fmWQTeR5-azPOsk2Usi7OSr7r6PuF1nHABOnuhKxVcy3_SRgG_0SejzDgDNYolIcQPPIbrYhc7ieBWlhePvscRfAEyJ36q2x60pv3K25arCm2jNJVAojm5A5annLVAQMjzCeWrPpc49I5E9uzvDaCzMaPK5IKeJB6FCo8JIy-XJdFiBN21qOl_rZ-h9lZXltkPIwylN9xD0aRGybYOEsLf5t4sjzZryn-c8HGR9KWodBJRTJL79dIYkvE5DC9gyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPhNQILR7aU-Ohab0PD3QU7X4f46o-b8IWpAs1VA2BU9whgzSwLqxd2ogiqce1XKgaN16T0QnKC8TmDxwCnbevuCmC5ZuO97DpA3i9FE7xKsb8nojuqOealIpnUZxLriYB5o1-iBVtCiqPLBamMnWDZYfk9oVFRzgPDhLMWffrbKvY3oWwLkWFH2f809NDhpn_2Fjd40gBJ1hZdlQKuxhNrm09hV2KMv67PiXzOPcXY2K1WLUC0CKyB1zSDoDF-VC41Ds1EyeSTTHzcGm5pmlGA05a8iNgi-mGzMAAzUgPZkJkONtkSdf47zmx6xObYXvgN4-XYuMzS_9vzG-X4boQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0J4gx7WPULbHRi9AM3nGKy-8bI0q8HU2xaublx4u2LUtdeG4JuJGHPDM_znsaqZKH9SzIA96r5v8KTHXfybXYOB7cmyTTFJZZwf5sEnVYVw8YzaaT58XD5Hj4V9ZN5nlF5M7-4WIX9ZSQ-xzSuIwYIeFKI1Zehtln_zjV1mvY4deTL-xc62HeY7Qo9Hkf-nP-QczuS6u7ZzOb-x17UwD7JJTFN7g4lEejMkVZTzbO65KhilEq9JvCGDfxXDqK1BGL2IDabJV6eAx-mKrLpVJ2bbBNcpyRZopz8v9nxpeW8y-6nJFQYvQL_5wOjuHDK1cUNHDop5qixgL0HPg-7zTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4Bcz7RkClPelwnmcWizeUIjuc_iik2_expi8QNSOTVzUpeJ8NJq8EMfP9peLIsUqi4lbDanp893DWMR4MxSOWsqJXuBorUZ3lHcx-U36AfMJbtAX6wILi0k85Jpjni1-Relu2E2iiC7E0GU-ZrNDMcxwz-Hq3_tmHa13PJC-zfd4RugLohiIF9Ih9NM5HM9GNY4pS2UdsLySRyfQdgMF0m_UTPn7RYs05dF6OZ5MosSojr2k47up1XRZSro6rjOynrqGcM_y83KMBcsLhDe2-9Cv9o0GoSKh_u7Ypd2Qxzf3QOmenLP1xsmWS4JYfEfjQDEB0EPfpmZvepmGKhJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSw5PdkKGptLDIdddtX4H4G4Lf2Q_LMLThZXcuC6iMuasm_UEAi6R_FqTHat3gjRy-_5Z-Itwlkzy43wxoMCpjA_I2DTJDJV6JDAlHvCBr7PnhNg1U8xWBKtTO8Tl8q47O5HwFsdrD-4SZ6LtWkbffor-L2_MfoFtYY3H7unF2o94kFY5QqzyPx2PlmCxW9q5A7S9RkBVvxKi1OVQaTNNVFN7VtVCmAgUNnDjkk-mubcMFR7LU2sjfMNsfQsXk0lTU_rRpk0Gz2FNYvWRPrO9Npw3UzNTPzVP8DyYY9HIs_SkFT9gAx-rLLtLvBnOuPuNkVirguxlAKjnyFYtpcLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛باشگاه‌تراکتور به‌دانیال اسماعیلی فر مدافع راست خود نیز پیشنهاد تمدید قرارداد سه ساله داده و قصدداره دانیال رومجاب‌کنه که بزودی قراردادش رو تا پیش از  پایان فصل تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/22008" target="_blank">📅 09:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ceUwnmMSAD-1wEtbG-mtwEtFXMy2jfiUMW3eekWJSIai0uYdTlqNAXWX44Yyh9hr7LZlFqSjzHszG3VuW1LMkMUbF3Jld91TmSZFeJwHWI--XKit4JWTQw6iGhujZ9m8rGtaMkFoiiOABRXAiBfz3jzkW5kAHeF3XzYU79Xb-PN-cWLUflxbi2XvzRPyJzBVOWf_BERx5tBUskNKJmw9sT3JYhKIraN44RTApPMzjk4Jcz7338Pc4q6wsE0Qucf85OOlIZiiUjBxTmD7oQfnRG0oqycoJuXAFm5eUid5Zy2aDMwCAxtsrSuZvtnfylrYjpndR7pOueSTfkecookpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرانکی دی‌یونگ کاپیتان هلندی بارسلونا به دلیل مصدومیت از ناحیه همسترینگ یک‌ماه دور از میادین خواهد بود. کیلیان‌امباپه ستاره فرانسوی رئال مادرید نیز به دلیل مصدومیت حدود 3 الی 4 هفته قادر به همراهی کهکشانی‌ها نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22007" target="_blank">📅 09:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=g9QY9z7WmnqJr6dYY1Zv2kT_eQoMQ3vsttXW2vp-kzjOL3jnspjhJmt4L718nQpHJ8At5-97yx6gPNpeu6y9omsVfJ21qU7vh-qJLvFrjWd8oY8G-dkWeiwZSYa9bvqF018dc9sOBWo2Hhop2Esdt8WUjRnKYPI4dUtXTLBbyoEQAMgG-dQqdkhBi48Pgg1ZKG4ZUOj2YQBKoYXseYAUbaAbL1KFG9_MrDjsI090fYwPFrMoWHEMsHW--QdUdGW2PEMEkjpqhCExCV5qy5DX0cAzenGyDfnOkme79-zjLRUBX5EjjLhSnFjLKLx6ubyohtlxZiSciSIF0DE8-4B9klgA8L9PxvZwT7yrvLDFLZHHi3cNWKd0Y1wfSpwA13BnxU8Fbi1R4yui9SbEgp2Bbv81wuqU8t37yZENlgfh63yJapPPmyY95hdDK5L6gG_XVBrWXetLJb0U917vUrmDRxLSTRfw7pKQfV58jKCX9ScrbabZhfHK5wvyuhRLA5zW-rfGj9IH0zwiqHALIz-c5-BrQ4A7qcesDWwGahj5AQPitept6-me56n2P72uevzNpNbIhpJsMf87tBma-IogBdqgV1IZuDSIVTQuK98vlmPzMjk2R-zNjmwaGCaqGFMGk_1j5TpfSgo4bO0stRA8UCvaWYAhkqSSFbGWcBW7Qek" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b2fb0d06.mp4?token=g9QY9z7WmnqJr6dYY1Zv2kT_eQoMQ3vsttXW2vp-kzjOL3jnspjhJmt4L718nQpHJ8At5-97yx6gPNpeu6y9omsVfJ21qU7vh-qJLvFrjWd8oY8G-dkWeiwZSYa9bvqF018dc9sOBWo2Hhop2Esdt8WUjRnKYPI4dUtXTLBbyoEQAMgG-dQqdkhBi48Pgg1ZKG4ZUOj2YQBKoYXseYAUbaAbL1KFG9_MrDjsI090fYwPFrMoWHEMsHW--QdUdGW2PEMEkjpqhCExCV5qy5DX0cAzenGyDfnOkme79-zjLRUBX5EjjLhSnFjLKLx6ubyohtlxZiSciSIF0DE8-4B9klgA8L9PxvZwT7yrvLDFLZHHi3cNWKd0Y1wfSpwA13BnxU8Fbi1R4yui9SbEgp2Bbv81wuqU8t37yZENlgfh63yJapPPmyY95hdDK5L6gG_XVBrWXetLJb0U917vUrmDRxLSTRfw7pKQfV58jKCX9ScrbabZhfHK5wvyuhRLA5zW-rfGj9IH0zwiqHALIz-c5-BrQ4A7qcesDWwGahj5AQPitept6-me56n2P72uevzNpNbIhpJsMf87tBma-IogBdqgV1IZuDSIVTQuK98vlmPzMjk2R-zNjmwaGCaqGFMGk_1j5TpfSgo4bO0stRA8UCvaWYAhkqSSFbGWcBW7Qek" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
​​
مجموعه‌ای‌از بهترین‌کنترل‌توپ‌‌های سرمربیان در کنار زمین؛ دود از کنده بلند میشه و از این داستانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/22006" target="_blank">📅 09:02 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6BOhPULt2FzqkXCsaQ5f9reKvaBM_aZ-BhVCv_5bFtXmOxwvhDVmRw3crDctc1Es0wlmVY2U5xVcTMhPrknHuZ3qSiQgcVxWJb67_3zA_1vCPGkjwSayn1VRktz8-ao6pVtTP-EpACtZiCweYKFZGEnA3wNfMiT_Iy_-Mt8rdPPDDkF0U67TXCS2PimKz583PjNTrf_sqg6SkJni9eCs_Uj55SE994ad4Utx8x-SsDeTLandGh4dgWdqEphv-h3063f2-OOtZN5ulEFLPZWeXvlbXgYtMJvpp2mCWF3lDZO95O6kSpyun6CUfjkfnLsZKzjqrkPglFSR55GmPklHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌‌امروز؛
از بازی خانگی بلوگرانا مقابل ویارئال تا دربی درکلاسیکر آلمان و دوئل شاگردان اوسمار ویرا برابر ذوب‌آهن در اصفهان
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/22005" target="_blank">📅 08:04 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oh9PEDm8ywkfDtjvu2dQis1PqaI5CwySyi2ToEBWeeBei0_vCpQG8gwegOcVY3oxOfBIGiuFB06Wr_B7tahQLbEbN151e8IQ0554gIDtEx1Lu_KxRAjLc4hPC0z7PaerI7gNJXQUtkMC_kceTtI8E9pcIC6EYDo0RT1KFSbWGyVVepcaPvieUmmir27G3Vm08eXHP9Jh0_mTGUYM2a0AyXMMfSeG2X3YVOnOeI40ahszJAw_aIZjEtsCdyZznvgN4Cl_59MomfvldVdzunxVsOydVDoDCkLZ_cMXvffwO9ExtdR4RhVbRhF61SIn87ZVahTP5pbD1jMmrO3X12lsOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌‌‌‌ دیدار های‌‌‌‌‌‌‌‌‌‌‌‌ دیروز؛
صدرنشینی آبی‌ها با برتری مقابل فجر سپاسی در شب درخشش روزبه
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/22004" target="_blank">📅 07:59 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veVH9DKF0Xu3LGr5FPx74EbMNjOXSdgGRTAYMyo6AhvvwoSiQNJ5vlLXVU01neyy9Nsi3RWnT2r8ORiYP2ljSJjY3AZl5GHkr5GIQ0SBnDS_CHDTXK17gdrdtkZKmNggVaNIYuoQcE8kqEcdkf9LlXFyVsi4I0L4JUzubbYETrZWofltLM1u97dMGSsOIFDtGoSbEGPeLBr3EindYDu_g1vV3LxE4yT3lrJemjerFO5-Xz4V5WGiAQgh6XCFGYtLOxzRdPA8MDRo6C73NtAyS_M9eFBSaKyg4gzjLco6t5MoAWDY7oBBN0ZWyvxk1PIFFSbgpMGJM5ZjFYZUShEbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارک لوین فرد نزدیک به ترامپ: علی لاریجانی، علی شمخانی و پسران شان دریک‌ماه‌اخیر نیم میلیارد دلار 500میلیون‌یورو ازایران‌خارج‌کردند و به‌روسیه و سنگاپور بردند. آنها از ارز، پول و طلا استفاده کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/22003" target="_blank">📅 00:21 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5bP5BR3dX3X3a8Qt5NKtg9-WXNwy62BGatUXGP1KLHHUPi3_3YqgFvNtnN0b2L52tv5d_Fw09NrXJhR818f4DedbeHi2Nbggi-AkbG67wrZh5Cn5l1rgdlAkdsp9gSV2ct-WFVtLSthxq-2NRj8sJUBFA0vPfXCCYkbd_hnMES39WYiQVVo7Fxri1LhdeM3UCefXRgjHmCfhXFFBoZuWIPWNGobkPc4kVwyBidAF1cEhWF4B1O4LGnMLX1QiVmziL6i-u8dZJ7UX5_Jh0HFTTlvyE7HvrH7r-uH6RrFaZAGLtt7n2fB5CsWCsM1PTW9JkOroSmrDXw-76I99QpuqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/22002" target="_blank">📅 23:57 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGjlNxlcq6RFXOxP_mZJum3YLFFuXJ38M5wLH--ErD_pQdLlSEt6aHJ6qj9O0qfFhIi7JjwQPOchvHpen8DXIRApPe1WO_r_CEBqzHv1hUhO-kLbGjt5TF1Q_yEpxM93aAdwLnyr9wInBTjlF9SW9cxlB-KQ3I_Y1BN-GDNk3jBY2-N38pJdxNJGzhCP9weqKa5_plop_fn-xJu54lTiTY8cRPADzXoVcCjwNmte3sKTqjkAqG4dQxJkSdYGypq0EymayKPwQyB1eGnnTtaJTOMvSmFwTvC3GvCdjx9LhvTer236TAoEZ0UmeOLIqELLtfGgz_5TjjO-ChsilfBAXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌اوسمار ویرا سرمربی‌پرسپولیس؛ سروش رفیعی و امین‌کاظمیان علی‌رغم‌حواشی‌اخیر به‌لیست این تیم در بازی فردا با ذوب آهن اضافه شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/22001" target="_blank">📅 23:44 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22000">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=q4tfbEn8q3CRbuKV2HG5EusfbI1L96u_rvWVE4tjTO5D1UAu1vC9NpEL3Usob_fOPdjAS4CfwAZ1dM5a4t7zrca1B8VCO72vIre0Pz7xICaLu3wweL_JuMlm-MmPa-lysxbpovT4ix6juqJe6Ymg919GPqVWRwzGEGtmRZ_UQiiiLhk8Dqabx0osufwYDAQgYWwPWpwu2Yr7tI-vI4ar3sgDQsFWpPtFsLQJV3cb6MIDb0pqLCZ8JBaZoZLQjn8XQcFfThEA0QaGDAsZsWRUoUdxNGCFpaM5lVGwla7veNGzq2fjRpR3W7Fj2gpOrTde6oTbwilHI8OW1tDlCbSsYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f5d2a00f2.mp4?token=q4tfbEn8q3CRbuKV2HG5EusfbI1L96u_rvWVE4tjTO5D1UAu1vC9NpEL3Usob_fOPdjAS4CfwAZ1dM5a4t7zrca1B8VCO72vIre0Pz7xICaLu3wweL_JuMlm-MmPa-lysxbpovT4ix6juqJe6Ymg919GPqVWRwzGEGtmRZ_UQiiiLhk8Dqabx0osufwYDAQgYWwPWpwu2Yr7tI-vI4ar3sgDQsFWpPtFsLQJV3cb6MIDb0pqLCZ8JBaZoZLQjn8XQcFfThEA0QaGDAsZsWRUoUdxNGCFpaM5lVGwla7veNGzq2fjRpR3W7Fj2gpOrTde6oTbwilHI8OW1tDlCbSsYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لیونل‌مسی بازیکن‌سابق و اسطوره تیم بارسلونا یه‌تایمی کاشته‌هاش حکم پنالتی رو داشتن و تیم‌ها به هر شکلی که شده میخواستن جلوشو بگیرن اما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/22000" target="_blank">📅 23:38 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21999">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_R8tDNy-1d3hO2cgo4w5VzZvH2h4cEi0UOQSSS41yOQ2fd-gSwmYgrLwHjXa9g8_6Uzahn9tliOZoCg_6tjXyDerkxfBS40scYfMx8FpBqhdGOaFCBUoBsGajGvoGTnsrBjIlfoy24i3YqQA5jg9QdEhP_Hsi2D96MyDzdjk4Jh4s5xWMOtqIPBD0xXp56IHDC-RKYKgquhbLXkYvZMbbbXxGVS22NWYIO69pSkP3ipqr3XE8z_SiUjqbVwQHTu4_M4cCYHsI4hNDWhdQa_BPaDjZI42fUl-yyyEHn9RcOyTa9deJ8ltDZRB9Z5d0tMK3rYL1ODXzfL5m1RT0ucDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
سعید مظفری زاده مدیرعامل تراکتور:
🔴
از سازمان‌نظام‌وظیفه استعلام گرفتیم که اعلام کردند علی رضا بیرانوند سرباز نیست اما باید تکلیف پایان‌نامه‌ دانشگاه‌اش راکامل مشخص‌کند و معافیت تحصیلی اش تمدید کند. او طبق قانون مشکلی برای همراهی تراکتور نخواهد داشت. تراکتور…</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/21999" target="_blank">📅 23:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21998">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=Fif_qmMeiBWfHyGI5RuGHJM1H0rzpX5rmykTHjU_Q1fhI0ArcLtrxrToyO6vveqvGsMwDOnfoWfv4irCsj-_ZgfgmFoQ-MC7HPtOMVPovJhMPEr3c4Acj6gG0TN54l_p2fkC9YAe2Gzk6vyUFSEhFhkB5uVDvMaPABUKNHFfaBUF1KF68JAGOk07jsNfEU0-hGNYHNhvAuG10hIn7CUnrnBUTofoGcXsDM0LNqmdn8XFnWcjp661WJVGZBF9NXqpirTwHRukqmKLfNosZBUoC9yaSJk4u50jCGRnCZdtTIVUom8G-444V3wg4qEeSGT-JscsuvoXG49pzarV9vcGqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e402c3a8a8.mp4?token=Fif_qmMeiBWfHyGI5RuGHJM1H0rzpX5rmykTHjU_Q1fhI0ArcLtrxrToyO6vveqvGsMwDOnfoWfv4irCsj-_ZgfgmFoQ-MC7HPtOMVPovJhMPEr3c4Acj6gG0TN54l_p2fkC9YAe2Gzk6vyUFSEhFhkB5uVDvMaPABUKNHFfaBUF1KF68JAGOk07jsNfEU0-hGNYHNhvAuG10hIn7CUnrnBUTofoGcXsDM0LNqmdn8XFnWcjp661WJVGZBF9NXqpirTwHRukqmKLfNosZBUoC9yaSJk4u50jCGRnCZdtTIVUom8G-444V3wg4qEeSGT-JscsuvoXG49pzarV9vcGqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
مهدی شریفی مهاجم چارچوب شناس این فصل فجر سپاسی؛ استاد گلزنی به تیم‌های بزرگ ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/21998" target="_blank">📅 22:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21997">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194acea631.mp4?token=IYHA6_h20WeWYTsxS5W27w6nn3eR2zIECwYkzqtWwmDv0r3e0B37MJ-P9qBCMIhweXr_K6PVbwBInMb-m1navu_f7_slF0VGs4aYgspbaf4O4kaAY56BNZWKFjV9OOmNnbo4q99O0YMrksOs-wJxyYlFP94wQOQQ_23J_7ztwUrndnz8kP2_zcnAi5Kf_Go9KFtp7yt0ds4FRzOmW3SGGps9_jRQPvWTJHNKR3n-mtEiAf2w4P5ka7tHRVH7-fUBe_Z-YQhXgN9Yv3FYuc-Eg0yLyurReC9TRWBuaBRH3mo7Xs8AN6Xk6-a4sK5I9gUl-9LQ09sMYKBurxVHsRlIRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194acea631.mp4?token=IYHA6_h20WeWYTsxS5W27w6nn3eR2zIECwYkzqtWwmDv0r3e0B37MJ-P9qBCMIhweXr_K6PVbwBInMb-m1navu_f7_slF0VGs4aYgspbaf4O4kaAY56BNZWKFjV9OOmNnbo4q99O0YMrksOs-wJxyYlFP94wQOQQ_23J_7ztwUrndnz8kP2_zcnAi5Kf_Go9KFtp7yt0ds4FRzOmW3SGGps9_jRQPvWTJHNKR3n-mtEiAf2w4P5ka7tHRVH7-fUBe_Z-YQhXgN9Yv3FYuc-Eg0yLyurReC9TRWBuaBRH3mo7Xs8AN6Xk6-a4sK5I9gUl-9LQ09sMYKBurxVHsRlIRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش رضارشیدپور به فحشای‌ناموسی عجیب و غریب گه در صداوسیما جمهوری اسلامی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/21997" target="_blank">📅 22:35 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21996">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KghwchEGGTkt0chZO4iDLXNg7b5fYySwLuMphy7m9aRdYxJTWe2_pxH3ezNuBQMChhfooMhbTFRe_xLoWIOM8d7QwvYHvZL7gq6YlOYNIuxkUWrCdmB5yDQ6GbqPjac5_uNHcA9hteNwlrhL0Dv0xD9gyPcL6pmKjexn5WsIMxd8ofDjAPzAzNU4t2mytKY1mysfM-TmmXmEqug2dekRYJFpw0bIa7cUIxBP2o5E9dvBPFCiWrXqTNF9irqC1X4naHdgAk_ZTwZr7mnkgBJyDrHr9KXjqFRRTfs2zGIJOjQoAwnd--nqctJtgHVpVO5PTRpl5EYRJzrofpNfWjh1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
نیمار جونیور بعد از گلزنی‌ اش و شادی اش به سبک وینیسیوس: هرگز توهین نژادپرستانه رو قبول نمیکنم و به وینی‌گفتم که اگر دوباره گل زدی، همون خوشحالی رو انجام بده. منم به احترام و حمایت از وینیسیوس این شادی رو امشب انجام دادم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/21996" target="_blank">📅 22:21 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21995">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bebf41053.mp4?token=etcEi7Gmhe4Yshx-_NKB6Ajgh9k0f0e5SeZGIxs4KRJGKR-fvSkO7LvBKmWKxieG0dpQGW_cV8pokDR8-Y79aAwzX37HKLYE6fm-LUBGqKHrF7DtqqED5O1MCoRDKiTCi74pLIBvGIEl-uUA8nLbccVPhOEmEPdeIHbvU3oLjun3rO-8Hr_mrbl_Agi7ylF9w6n7AuiH2Z4E-Hc3TETxFlr6Ax4Tg5LPRJVZsz5aji15Zyr87SjICfO-vtWc9omGaljFzAFQk2AMqTxlhfYq8JMWIZXqjcEopsw01Ap4l5gaFHhBi-pWNN98uQ8LJ4EumqdeCypSfeZ8ChEQqRGDyruh7QfPPhPcW480HskfGk3U3mdwOj3-RUTUnap2J-XYfcBGakKRuGoWIjGwCffmt8YksMpThBO2YM1TOiVEHo1OAPyhl4CR-ZLi2v0lEmhxg32bQMuCNdlRCSKaHiJRmOyi-g4YjUHFlWEOgfuSiz3nSGn1vE-AC_icNhzgj1KMYqlpHgKSlEW-_zDg9R9PcRHePC5rI9sLZPJeuPB36ieur01AjOYgbQ1ptI2uVsX69Of7Ny89cudkX_ytMOYkpf4TysfsLq4V4uF9W_0jpoITBftYKEgJoUoVZWWFVcgdOOFP-uPTORWTMvkLfgBSrLk7gsqmhy-d38jcJscl4vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول رده‌بندی رقابت‌های لیگ‌برتر درپایان دیدار های امروز؛ سه تیم استقلال، تراکتور و سپاهان یک بازی کمتر نسبت به بقیه تیم‌ها انجام داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/21995" target="_blank">📅 21:59 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21994">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=hmJRvhFbMZ2mfHfgwxDqJa_jB7QjLImvKzq6GGJauOcRViwYeZ7hmZMrYockrwxBApTv9kPCm7QgxetiHfsfn2meDmzGEZ5TszOdzD-zONtt9Q1-EhbVIrOocctPUgQ42efnftBkUh9RugbUELB8qGqLyyEGa-7TdNsSqGXYpq5XT4u11ubSXXqw5v0LUv5__N6QdlAHaI0Ggw9lUruV9y2mOAsevB5NwYppeljdTUMsZKv5YTZIkLqRaoL23h2jNINv1G5JdxtE8u4mN8oSM3ramhz_zPy9D9ot6Y_tlNKudXJcgDBdm8OSSjOd0ZcbkRCc5Nf8oiRW1bUi9nkWEYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1529297a6d.mp4?token=hmJRvhFbMZ2mfHfgwxDqJa_jB7QjLImvKzq6GGJauOcRViwYeZ7hmZMrYockrwxBApTv9kPCm7QgxetiHfsfn2meDmzGEZ5TszOdzD-zONtt9Q1-EhbVIrOocctPUgQ42efnftBkUh9RugbUELB8qGqLyyEGa-7TdNsSqGXYpq5XT4u11ubSXXqw5v0LUv5__N6QdlAHaI0Ggw9lUruV9y2mOAsevB5NwYppeljdTUMsZKv5YTZIkLqRaoL23h2jNINv1G5JdxtE8u4mN8oSM3ramhz_zPy9D9ot6Y_tlNKudXJcgDBdm8OSSjOd0ZcbkRCc5Nf8oiRW1bUi9nkWEYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد امروز پنجمین پاس گل خود را برای این تیم به ثبت رساند و گل‌‌دوم‌‌فولادی‌ها که توسط محروقی به ثمر رسیده شد روی پاس ستاره مردمی این تیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/21994" target="_blank">📅 21:45 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21993">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkfVjJRvEKjhNnaN7irrr-QGDclyizWKvz77O4a4LL03mh3L8tyKq9f_6m7Y6uzAaZXN53uwTK9z7Ttvhg1ilyLnbH5k84ClN5GnFC4L-ekdm60P8rdQcwaPgYybl84GsqOT8DFEQgFj1563PYUJwI_ScvaZG-Thx3ahFiXZgCkCXwFM_60vMyGKJEtTQzhxLupy8f-8TJM0yT4DksbY7ofHSkdDTO63JkY1Fzj1sW1Qud7wVD6zdTCAp3fvrdg7xxCqgayH_ACyuENsnlFPYFSqRMNCDC_3l_uWUXflaFugtJNpuLIjL-x6pBeDrf42ugltvsTGqYBHBH4uKQ7Qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
#تکمیلی؛ رامین رضاییان ستاره 35 ساله فولاد خوزستان با ثبت 1 گل و 4 پاس گل بعنوان بهترین بازیکن ماه بهمن رقابت‌های لیگ برتر انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/21993" target="_blank">📅 21:39 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21992">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🥅
🟡
🔵
حیدر‌ سلیمانی و تورج حق وردی دو کارشناس داوری
: دقیقهٔ ۹۲ توپ ابتدا به سر حردانی برخورد می‌کند و سپس به دست او می‌خورد. اینگونه برخوردها اصلا هند محسوب نمی شود. اگر مستقیم بدستش اصابت می‌کرد می‌توانست پنالتی باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/21992" target="_blank">📅 21:32 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21991">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxekZEf_FlaXpUuyw5L0xnTadxGTX65IrwbEUk_LcPKmBuPi4FI1ZpLfZIf2Rw5uxxVtntYOoWcqw6i1uW1Uo4hFrkYr-iP1KsdLipM8eX6cuTt4tli3qmCKcG9IW-IxL4w6ITbsSW9FP8dx-WLTVVlP3yFMcQoQly4mw5QWyaWTpYzCYxZw8iGRJRZrwViODhfiWSOwlYN3l9S52Pr_5EFpghmcrNJ_win2CEfYtITTQIMfwcW5UiJNOkxYKIHO525zOlHFQJeAzY_L_Sg6KvFyUnGXSdvzbD0uKf_1-DOcOBFnYWbwtzmmjsKIkffvylYtH4kIVwqkkNjHlu9iqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌بیست‌وسوم‌لیگ‌برتر|پیروزی سخت و نفس گیر آبی‌ها در تقابل مقابد تیم شایسته پیروز قربانی؛ سهراب بختیاری زاده با استقلال به صدر رسید.
🔵
استقلال تهران
2️⃣
-
1️⃣
فجرسپاسی شیراز
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/21991" target="_blank">📅 21:24 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21990">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjC3Smr8ftGnItu8uwwzXfYYDhNyWxuV_AdkhUlhDN1bnT1aPYbafKLvLYOeQZhh5Rjbdsrq_EfZNqBw2Xk7UGBUzxsVI8r98G-7uaVnYaFV8QHXew2xEd43u3XIKYOgdUjmhuXJ_kPgLMt-dQgY7sZSyrhdGDnFu9syeFSpZTbqlaNPgc6MUkpPJKABMmlx6cK5ohS2olZ_ejx64oZnfS16t5hW55CiOT9WdEIWU54ghvgRmsIWCGW_xnRA-gJcpu3wqVCChj6v04jI3Hch2TK_Az1eB_4w_BM1WG3Q5fx4ToSwBscJVlZ1HVkwpv8S_izLX-HmC3o4Swu42v82Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بازی‌های به تعویق افتاده سه تیم مدعی قهرمانی این‌فصل‌رقابت‌های لیگ‌برتر: سپاهان با ذوب آهن باید بازی کنه. استقلال با چادرملو و تراکتور با فولاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/21990" target="_blank">📅 21:19 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21989">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fopsJHbNILNI8g-VRPw3q8Lg3q0NspXAhWK9UYbhhnDBbl3JZ9PIrzQ1Bniv5zxGbubLb6Bfp4NpZaX_ZYAPmGf2fcaIgaXDntG0G_-XUnjGNqTDVIk1X7nTDg8y3SIGNHVVlg7SIer797AKaahKZpHJaJLNOBKRijaZ9CrGFJFp6olzUAjCbsuxtkMlvHz1lgyTZH-oRgJxmgljGENxgG0dJnnC0VnORGx8XXw9aElLXr_fk2gUYIr63tv1r_qBOmUOOes8DusYSQFbvppL8Nra-o3kvd-wouC3LKVmwh22U0iSsqPDHP8DpCmnct3schN78Na1Td79tfQzgf5WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌بیست‌وسوم‌لیگ‌برتر|پیروزی سخت و نفس گیر آبی‌ها در تقابل مقابد تیم شایسته پیروز قربانی؛ سهراب بختیاری زاده با استقلال به صدر رسید.
🔵
استقلال تهران
2️⃣
-
1️⃣
فجرسپاسی شیراز
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/21989" target="_blank">📅 21:18 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21988">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrlaeqG6LL0YS_7E_69_6lMBMXFaYG1i55pgxcYZLXGzn6Gvini3iOsJfIAlejEYHdIBQM0sJQ0j0z-G_P_mCSyOjkAdkzkXCz5HuJ5K9KAVV8fQe3nCFbX6OVcf3eGsT5XCKQ8v2S49KYz4Hmy0n3zylKJNNfxsQPGu2eHUvQP3PUA0zsIxB56WvjRWvJdfqXIOyj0Nv0TwYIpmFUyAp-HTS4IbHtq1P7oU9LyLncR8BRpmHN0saMtQpjN8dD_NJb33IVt-LRt403VdsEkwmxjFO3OUAZVh_cDt6PHYfI9buUTHryN7Pa_WjXSIl9ss1vtN43M4xLpVJoxXLFczIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روی‌سوتی‌برگ‌ریزون آدان؛ گل اول فجر سپاسی به استقلال توسط مهدی شریفی در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/21988" target="_blank">📅 21:14 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21987">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSGOUzYeiouDXBrAiFnlRC5Qr51CEkRLP5ew6hf1Hzo2xnDYppT4UdQvS27g7nVe4_dHj-b9uoIbC4FNKMQr6EKDqWfGDmndHfSMsmDyO4lwjdhqUEBYArrktrnwkQOg2ctEsoNhKwttFMcbpjQjecTyekznRpEiv7A_4W5MWGr_rE3fjdNf4SK5G4x1yCpS7FBkLbjniXLicGZc6e3SC6izJonQkDH9RmRT_LX28Y4LaHA4RI_Xgtdi-fj39_1s3t42jag0J-CaP1lP1_YmNkbJN5v0fRjtKU9erdoAgkVRcR_y_-kI9fpFyJWSjj9L8JJoJDMJy8r3vVFin1mNbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته بیست‌وسوم لیگ برتر|ترکیب سپاهان برای دیدار امشب مقابل پیکان؛ ساعت 19:00 شبکه
📺
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/21987" target="_blank">📅 21:07 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21986">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b8542b16.mp4?token=lcOO15MJbH93_7kmQLRx9TbNTO5AIc1AyDykNgg4NnqAlnemE68N0Ts5bGpsO88zF17koYOt5DW-Wd1afyfzSsd5AKO0mybpD0PBoiePvjrUcYS7VrgcaUg8S3vCb7NEM7217-MJFgghqRwIUsSlttL--oL3nt-8uXb2hvt7zQuGXcHvhBW3GmXeOW-IEOYJWoKjPdQHL23o8b11pqk4GOHlohi6rRaQqkm6BcAP4C-fFjE7KAt00jWJQ5x-KqNahrgnhwueb-TggQiTBYYYwDiw0Ej-yTBgykVHdSRCJjJrVR9_AyCVT1iSRBivnEnjj3n_9PqF1vFRC0zsKS5BwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b8542b16.mp4?token=lcOO15MJbH93_7kmQLRx9TbNTO5AIc1AyDykNgg4NnqAlnemE68N0Ts5bGpsO88zF17koYOt5DW-Wd1afyfzSsd5AKO0mybpD0PBoiePvjrUcYS7VrgcaUg8S3vCb7NEM7217-MJFgghqRwIUsSlttL--oL3nt-8uXb2hvt7zQuGXcHvhBW3GmXeOW-IEOYJWoKjPdQHL23o8b11pqk4GOHlohi6rRaQqkm6BcAP4C-fFjE7KAt00jWJQ5x-KqNahrgnhwueb-TggQiTBYYYwDiw0Ej-yTBgykVHdSRCJjJrVR9_AyCVT1iSRBivnEnjj3n_9PqF1vFRC0zsKS5BwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روی‌سوتی‌برگ‌ریزون آدان؛ گل اول فجر سپاسی به استقلال توسط مهدی شریفی در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/21986" target="_blank">📅 21:01 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21985">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sj5c7tddYiyJlgJaqOodmaQrrWmYiINQFMl1EQCCdnb4lKT7m33Cqz3EMcx6vtw4H1iHWQn5r0PzzWJLvhBhl8eyEsjDwkehem1MnhxLlVJvmwzL8hrrebY8j6fQ2lZLjXQHJQIPdVdNpeQAqFCfYP9S4LoMapDMnoTkX3BW1L79wKEDaDB-undeCZOUNMiGUY0iZ1rt7m__PbgE_a64oXsZKwk7solspcAlLOpLopoLNkOz7KydB-pc3R8mpKh_zTfV8oenzOT2Cv-bcCJsxfxxtPVlBzhPTCEZe7qEbY77Jqr7k-elyaL84AAXEof8cwxE4eISRT0pEp38Mh2diQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا:
فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/21985" target="_blank">📅 20:18 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21984">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM_DVXMjOH0VQbe9gHELLnbl4Xo-IvrftPiPkl94OhCInyhY07u-wWPoDlSSA1AdrbHZNPXf9x9oC3deZZdmg-VfRZjgK4S5mxRqtgaSs3mvNDZ16zIe2-jaQ9vVY-WInvptgPl2zNKpxVYSDL1KWWOVKJlkIRvDeFHIeYKydQPhi7eaeYWeYXNKhTCHUtxgRtFnpka1gCxA9i2pTsiTqeBlrlEQaiZi59fcM_Q5cBQU0KY2UKOFLMwHtiVERaYfdpBHz1rXqof__NstfRSuconPRSFgtfK_BcR27QBiZOcRK-AAPDbHHsYnD4Wt9ZTNuI36IVCw3HnpyfadgHgGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روی‌سوتی‌برگ‌ریزون آدان؛ گل اول فجر سپاسی به استقلال توسط مهدی شریفی در دقیقه 45+1
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/21984" target="_blank">📅 20:07 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21983">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec8f58a19.mp4?token=dqtkIT9mghKZiwYzB_y9Tvr_heGs7Kg7CYhtcHgGMb_Q1bX4VjD2WT8ODm2Teo79z5HZi7rfVSbnZsrpvekjotGTz6UlfMU-Y9xexucr2oQloWJuQLF_OhKM2P8gOW0bSdNhO9q0C2HMx_uJl3QNx0XPfnPe00BF9Mbhdvz8ev95d5AuiGd3jxQtD2akV6VwkjW02bpR7VjWQOaU3Sa_CrzFzLx15OGztse0EQvgl-vw0opD1RhsrKMThBqW8b3EHT5YEyMiaPTpa4g-yyM9VAcvMY5e02DMZin-oFK0WCb48KFJehvEkZSMqC0z62aJbxET14yfdrWlspqC-HZH_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec8f58a19.mp4?token=dqtkIT9mghKZiwYzB_y9Tvr_heGs7Kg7CYhtcHgGMb_Q1bX4VjD2WT8ODm2Teo79z5HZi7rfVSbnZsrpvekjotGTz6UlfMU-Y9xexucr2oQloWJuQLF_OhKM2P8gOW0bSdNhO9q0C2HMx_uJl3QNx0XPfnPe00BF9Mbhdvz8ev95d5AuiGd3jxQtD2akV6VwkjW02bpR7VjWQOaU3Sa_CrzFzLx15OGztse0EQvgl-vw0opD1RhsrKMThBqW8b3EHT5YEyMiaPTpa4g-yyM9VAcvMY5e02DMZin-oFK0WCb48KFJehvEkZSMqC0z62aJbxET14yfdrWlspqC-HZH_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
سوپر سیو آنتونیو آدان گلر با تجربه استقلال روی موقعیت صدرصدی گل بازیکنان فجر سپاسی شیراز‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/21983" target="_blank">📅 20:05 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21982">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1009f00a2.mp4?token=HYQnYu4FSrF2-vBpdP6_BGfDfeKojxO-Cl7EyXif5k5Gfhw7xl-4Z9ZGEkWD1iO8bLFgbx6kiOaDgxeKV00BDI8mZ11mRqWVb17Mvpearjzgd6Y60wqWyfr3900KE8quJ0gK6wtf5HKMJWvyAWKgw32L21mh1bIJ5Ohnyjen2MKeveKs7lILWTl85UYDkk0Pr0_0E1YhwQiJoWoGwVqSKV0j7j-0KY0Es8gkbTXCT1wwN_-Du_naL4VqDJF9OMTARmaM7SU1-B1oCCT8rqksWqHBxowpnLi7fbS_wFNd4fBcODfHR-8M8OYY8rVdybdWs0fCUFQUHRB5RYGk0PMBTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1009f00a2.mp4?token=HYQnYu4FSrF2-vBpdP6_BGfDfeKojxO-Cl7EyXif5k5Gfhw7xl-4Z9ZGEkWD1iO8bLFgbx6kiOaDgxeKV00BDI8mZ11mRqWVb17Mvpearjzgd6Y60wqWyfr3900KE8quJ0gK6wtf5HKMJWvyAWKgw32L21mh1bIJ5Ohnyjen2MKeveKs7lILWTl85UYDkk0Pr0_0E1YhwQiJoWoGwVqSKV0j7j-0KY0Es8gkbTXCT1wwN_-Du_naL4VqDJF9OMTARmaM7SU1-B1oCCT8rqksWqHBxowpnLi7fbS_wFNd4fBcODfHR-8M8OYY8rVdybdWs0fCUFQUHRB5RYGk0PMBTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گلزنی رو اولین موقعیت جدی؛ گل اول استقلال به فجر توسط سحرخیزان در دقیقه 22 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/21982" target="_blank">📅 20:00 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21981">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45c831278a.mp4?token=fnKq5TDaXw-XMA7s2Re6K_oQUehkTOR4e97q0Dt880PA8Yf9ZgVQ6T5Ydd809pbG5q13Iq4zuiXwHnnzks9GQkGexjjF2G6QigMYxuHwPJRlQMiNJ_PDhbh3FGcrlfFejqbFJ5BIfqVZCaG5gnU2HAjuwJZMTcCTd-6CpXD7XSLRp7jl-HmtP2YzqnvvuLnYVccMFWM6Uoy0DJ0wALkiKsiIly6sJQmZ1jOeocJtmJZgU5dS2mgHMF_HNi-xKneVs9bhT89bx_hIY_nSOsNL4E4xabEyuwry3_mwrXPWcKPZ5h6COUOvT2SRTw9QESlDH7JGRup9GepPoDJxXRtKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45c831278a.mp4?token=fnKq5TDaXw-XMA7s2Re6K_oQUehkTOR4e97q0Dt880PA8Yf9ZgVQ6T5Ydd809pbG5q13Iq4zuiXwHnnzks9GQkGexjjF2G6QigMYxuHwPJRlQMiNJ_PDhbh3FGcrlfFejqbFJ5BIfqVZCaG5gnU2HAjuwJZMTcCTd-6CpXD7XSLRp7jl-HmtP2YzqnvvuLnYVccMFWM6Uoy0DJ0wALkiKsiIly6sJQmZ1jOeocJtmJZgU5dS2mgHMF_HNi-xKneVs9bhT89bx_hIY_nSOsNL4E4xabEyuwry3_mwrXPWcKPZ5h6COUOvT2SRTw9QESlDH7JGRup9GepPoDJxXRtKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
گلزنی رو اولین موقعیت جدی؛
گل اول استقلال به فجر توسط سحرخیزان در دقیقه 22 مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/21981" target="_blank">📅 19:40 · 08 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-21980">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5kb3fawJ-E02F4OdDIA4sthjSveHhlesgSGPO7LVhacHBnC29V3xSPn4aEM89GRiDG3VcZQs08noaWGP1m7rFNeS0db0h6LmMyuLaRadHU9U7o2bEXPJeDyKSEpWmbo2_jgiw7eE1hMO3kQc4D7GZwTt0fir9GStW0nWawnFQ5u3HJpotUNFwr5rvvJJdhkEzRQmD6xjnFDD-_u2BvPKO8six80oOBkCNcCkxmDgT-Od1-OiCI1unpJT-5cuDUUYNbkQ5caLBDwv92DdVZU_r3bq8t50Ogq4U9_YiT4KrD0P2Kfd-C0yoJsbPYQayWm3XCJ8dm8gW7O2_LYoFVHCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی‌قهرمانان UCL از ابتدا تاکنون؛ بازی‌های رفت یک هشتم نهایی 19 و 20 اسفند و بازی های برگشت 26 و 27 اسفندبرگزارمیشه. یک‌چهارم نهایی روزهای 18و19 فروردین‌و 25 و 26 فروردین. نیمه‌نهایی: 8 و 9 اردیبهشت 15 و 16 اردیبهشت.فینال: 9 خرداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/21980" target="_blank">📅 19:16 · 08 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
