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
<img src="https://cdn4.telesco.pe/file/WBzt2zUGlmcITvCdpAhzq3bbONodZEvLiZioWT2xcJ_ftTkxDoiMmeSEPr1iLurQyq_kRuoIG37squRxOUfB2BB4zKcVYX5VQWDjO4UixvsN6ZvJAVOia0fDVx6rWCBkifsF3L1kTVKX2GIis7oviniXTDtzy8WolvHF_yyR9m1KENEHmi3EqXyCtDNLnXH-87ZgERrdrdhaVwzYkSQysNYFtF0xDDsedcXh4kYfL-PCMBIZyerMbDcaeprbOpYDVs4X74CGAsDxz3nYQnDHBaxZYo42MJbGZNleXUVhUx8dax7VYNULG22ips6zc7tPVbaCqMjTMafkDZTMfnevyg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 378K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 09:00:04</div>
<hr>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDRrnCg7pM0S7HmdHX1Ul8Dd4bnCIEOQ8Q8CqGgVwg0-UGbajiqxXeXUnW_PTVo_ii_A96VeI8FBEPkGWgibYL0XruUfrHEWRvaWMwdyQynnbdSbaVxmvoBdCt5-3uS40ZAUd5vDAjEmDEHjPRONYN6BO3ntjQPfWMn-kjm8hnk7gOVSpeLMUXFZXLph-YugBX53zIRDc1O18MoRz_54EBPXau9CWnJ7KIx6_aDUdLIcJPW7zbKbKM_il9lV5SFMFmLJvSKvIIVYLb9RCyZJYWcYSnZaRkfawO3qdiwQKEJljfcsB579rtiW_nnsI6RmSnOAyxQJJfFZvGa-C1oq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd8c901fa.mp4?token=aepufbKeNiKlMYl_yNTp3AZuSzMpUM7UvGutzFDrnEO6oGyuFUitnjWlFUwPidTWz5QpaMboF7yViFEmMpXjww2eKQy2seoZyNRvIvvCIzzIUrhKlLJzUiWENzA6g77Xp066_N16OmmIzOc4N8au2g6q5xUAFinLDU_7h7gS8y9L74nuSX63xkKf5k_IMKfbzjBQKlBu80ybJw7CCrY7vOEV13MEKmdP6Y613d-QUOIDHGscTAuE09G-XvALZL9Oew6oQqcFQtcj4DHGaNlVreFvrKIuyT1eTLNJjQXCX9v42DV1XNMhtcuiiY_OG5FEOLCwcUXoAwGfU78k0mV0cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه خطاب به تیم پاراگوئه:
اگه لازم باشه دستمون روکثیف‌کنیم و وارد جنگ‌های تن‌به‌تن بشیم، این کار رو هم میکنیم، ببخشید که این‌طوری میگم. ما اصلاً مشکلی با این قضیه نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHHxO5KBnvtJSNWhwAC_8Lta3NoUuuqk0ICkK1KTBTcj5Dov5v1WT3Q8Hj5bAEV7fZhGM7GwL8aBCc_T86_t8gF6nwb8yv9KjUxYk_XKQ4K02bee_O7J7yxqfIaKTx-j2bxZePKdBd-TWIaQTJCz3cXcBZVZTsWiln8W4dly9I8i2xgbRv-iJFT1AzM37uqpVhByHXI_ps7RVCOFuArFI7H90IBRHhvramMMUe95m5tAqhaYlrIbx7PSGWcSHkmTnEq_z67mM3tY26r2ii5eBvs4l-a2qN8Bvgj8H2HfOn0QeA-gIfQenkDLGEZAtwUvUBFIHHUmV-P2J29FFv84sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5736be2a0.mp4?token=GezN3ksoTu6rNwnp01shMoZMDusfd0yKil5tND-FbS9cXhnHhLICGAEoPMUwrZFWwcsJStz_MVAaQu3FfQF9oKlu3zCLSZzlA9es029n14NAXBhtMpvMx4rhDRrsTAqnS4bs0QsQ8jdnMquQcDVmbRNWXAwxn8oyxQD1Vmez_n-JkyvL_GHMwPyefwOHvLyO8u9hbHIcHyOkVUBjW-nt2Y6lDjPqDpulqpBJHgCI4WD0mdLBzREuICncjV1SnTFVBr_HPRnLKHGPCZaxj55564rUJk3e9dqhYJOn7ryouRwuaEMHYB0_oag-9NpXXHpySzdzugRhNHkixExm6txj2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
👤
این‌روزها ترکیب جواد خیابانی و خداداد عزیزی خیلی‌سمه‌خیلی؛ از دست‌ندید. این بار خداداد به جواد گیر داد ولی دهن سرویس کم نیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs0cpzgNs6BwDOPPznL5uOQj2SHuSfFVme6fA5Lc_QmMe3UKV6rtmroMOMKFCDvKS-iwSNa-Z_FR729-IZBBJJIU9146vvlEGes1CMTLaZ0ooJ36kF0MLeBlAJWJ574IMiWozVg1lXbmeGjKR-OumT511hHfE6aR7cL-HwPWxj5jKqTCiDRtMR2_rUSq8AHi79_zyWClBbUXoxUYmdLFEK-B8Or00bFwrDNvzq3ehq-ENWCSa_ojbZEQf7tUtKcfLqwd8J2cKCG1qJVgUWUjVAM2UtyUhznSBTwb0GDR21R77oX0qHk6OAsduzDogEScOTwH3C50-c_zE9pdHfz2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5yBqTVBE2sm20Gn2dHqnv7TIdzpYHLOYlknWz869D-_CAnyMG2ptkbvEpkZXRBNz8X5WL-aNYPGksOc_ywjvaOhhMcS5YVE_pBSOtcyVEq6pLH5R8ailGmBGSVII0KWQ33i3trdpMC57V811BW1IZQdnbQCjaOq5tD0ex1_nukJHQdLhxnEC6lnVdLK6T9BQbPokCBqjv14-cV7ERuXNN13CTCTBv2uEEahWq4a7RAo4qolZxdf32pqNmIHPjN0VGwf7taeFNXbYpZvBZ146tgNmyLA5xBF4F3aqYIP2eLyBvc2xnUh33z8wneRjrocXTzWVpQ3WUft03E7VbgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdMH_NIDsspAZrlQy8RerpBR-Cl6HqA6-e-Z1IYFMUHKJKfiTZKKvgMJjTAO9Qx4wqEiQlDZeZJEIEBTHz6Z8yChtDF8Jwjx7D2NSyfj73XmPeOSOdhcTPvVq58vB94Ov7cFRJKUlqAgpDbPn0Ld3CLUr4L8uzbb-V6qrRBJwq8NVlqcRQD89W41iKrlV032j9mBn7mLG6Y1Qn0DTWZp9FqFijr_Ac8oiragTeWaEwc7YMTC_rHHgKi2_9zu3KyJHjwZdxZpsTB1ArJuEJFQpXAZRDc_qiEACAwWAdQ-YHA4flmix7uRSl9prLkAdvhrPQFH47WS6f54LDGU7TaaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqgkvMUhul15PXaRNTNu_AvJPBfuEcXEVMZeAAQH_gie1If4LUdhwH5dB3eZWzsrrDLEwk-kRsggZYaNV_8wJTfj7U1XYTjEgE3SPUOv2M84-CIMYxWDtsjGKps5B5Wlhuzy77nzCkMvoy0kx9d8cy9hP1PHY2ZjxbyfNMSejMlLvVTT2pGonf1LBsjX8_x9QONvPqlA4Wb8SvXfxqw6-6213XEFa5-XfpOqNSxVTsWBHmwBA-fKh_HnF-0pd7gaLWJzsQig3EjTjcNFSefUqMGEmcqVb_9TdoZ_fQe9T2u9jlrQ8-mzgM7Q0CLjnZY8CdPPxsvQ5HGGjN5Y7BaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL0LB70NJOFzaXs0iIy36eAE8QqsaQSvkL2adBqt24Ei3OF1Sk6bR7ObbDGcteAr8jsfIu6HbcajcopxfsnRXIpZ1y2BZ-ihqAcp55Uu8B8pkXOz6_zwtUvJ5aMg3bzXPbGhdLUFIANLqps4i8af_d52Ru1D79-qPbtyD05tL1eloGFSvGWxGZ3YkMI12kgrUuXp3SghpCSzjGvxySEd7txWF2kFGyY-npVyYGrFe01MjfoZw6HmkzRVHxN-DCD1ABDVbbJzEyLoJEh5y45VSi_Uti6knFEyTTvATkgyMgLwebFXt2OBMt3LZskWFfCbAzr5GZxc-oGl_OWBIh0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbPyBUYqaCsvFw390eV1aIVkLiSzXVTPtuOAJV4DUtWbzSKKT3kbbJgx0aoTUtLF3_hHWu3J64FgU148YkUAEdWCkvGGKFDysmsyClnjq7BDvTVXr3HvDvOROcRTcZkY7JW9lAOGQ5v_NxuGqIYRy89guX8xgku_D8UvB2nD_Sn8onVdyI2TDU2Yx3pXHWD2oi6RnIsKAneCXs_iJSQ5UY8P5K-J0YlJWoPAjzuvuBYYZtnKpfq3qi8Bn10qFHWqZkJ_kKJpYr1Z7F4QikA21L0ohJDTgbXtaR-0Xn1yZC2mKru9R2EuTIGCqwEhKH-pGgzkAE8H7PmGb7qMKjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBcKyuu4zBK59MLdfUOCITTuAOZoYQ0y84bbG5af_Smy8t4Aj1swZeYJPYuQOGdMyCxmKRT09TIOugGVS45rEhxvxF4UJRCkkElCfIzbZF8uaP5RtyIkfShBj1LA3j6j-d7RLV3jXLtKT0N70lXmz603Ogn3ytCXQHGT6V33R9zX2b8Lwx3eqjVT6Q4Nsv-rEXZK1A3ZJ7cL3x03QimH5WrbFXVT7pXGRTGwgv8uktQbzzi1QPKIAtju6i-AT3rttLi3G046UKUrEoTlsSUinEaNvn8xmU4y4xZTmkwzkxrnCizMfc8FRu7VVQCuTCvgVMGB1jwUmhr2yY_CpUk32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XSlFoStaTyA4MFtka6b3wMlGAvF2NIqahPXqddcD7MTTN6ux7s1T1w4SgscK8Iby948N8StXeAjerhEmiBD6aKTomY8CJUifgHTp_nrBUi7hcECa73btaBtVSGOHoyylqJK3rbK5b6lvst9HrLx7R2YgaA_9gp3YNT6SmFriodwV5rAmzR8HAzupJXERCnv-6FJwLj4I0F-pF7TANHaWzqib9VTxB9wdxkOxxOoqP-WLFFk8M4YvQwlXbKuEGbwPYUlfxZXr7MJd_OMFAA8243eBlrzNZtvCL9AuJfzgxcYlBCYsh8NRyYoTUf0hh87zNvAU8iV5GNJ5VVkrfZfXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک هشتم نهایی جام‌جهانی؛
پیروزی ارزشمند و شیرین یاران اشرف حکیمی مقابل کانادای میزبان و صعود تاریخی به یک چهارم نهایی رقابت‌ها.
🇲🇦
مراکش
3️⃣
-
0️⃣
کانادا
🇨🇦
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akvAmE3H-pdfeyY_1LhIbg7QDxDmMZ2riunh7LfzDz1qu3fWxvTnToRxQgylN1WS5oa8YMbS1MrhGkomezXKgZq2DYmrd8kvzuCVZoN2CInL6VKNXyptAPDEOR1CB2F6IwCtz1R2HkxkVYCM0CnKHnyjXNPCg0OCwFwLPUP1l4EcFZ9tfeXObtuDaOyI3pLYmiQe8WZwGbn-KK2q6SC1pW3r3sLqbgEWkF1bVGAWZEWmJKndM4txwi5I8CJrWHiakdMKEGoJVxn3A3CBfq-uK7rJm07haRjfl8VkMWItuyP0fGVwGuq2nDFP71X3gIxAIvlNTY7F0qHFf7YpwEofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCBLRZt8NZhnfrxj1bao49SdsmDSuCtXyjWQAtYPDVMAD0TfnFDtLnml-IEUnFVUM1D-lLYOur0wGoh0ekcnvvEaZ2G2l8oF2MGHbCoBQTSRxkGIIdHtmRTHqg9AoHtG4odME1YNkH7bV3utN0gLU8UR32ZtjYLhV_AT3U3F850Kh5D4tSW2PKoMo7lQ7tN95DFvO_Y7Mze_dqVjICXqnsCr34UK8UT1lHOWxMSq7CjHELwTRU9sm6B33zjvuDT_ICnezcr3BrSZIOOkfuakJKhXgSRPCedqn5WXDaRHgrB2n6_997m-gqyT0z_wS1kYyjcUhm7KC6U7_5mE1z-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOT3PEnKf11SOXOE7aWKqo37ZPSyFDkgLRPS5Iz3QHfHsN6TTHuegL5eNFEVfzoSCwn6QEQTOec_13I7PzX4TcjUs_wSkQB5uaIuSq0QOqF-brgDWoxq1-iibvI6YAxTuvazMHZCu0Vu_6ME2MdPuu2kZuzmt_7_5-9VsBoc7iHd8Ez59C-iO8r9HWHjC0xQrJZ_QZavZvYx5NgXNf9-gksCmTJjMqi3qTFo29OaoDVFH_nFT7WHHxawRuYoDtX8_hpJfzAottMcqixJRyWTbRhWiByhZUgcwJ3dbCDHvH5KDEEd4I7AsPI6N73mJhAQSqDQg_Zm1qKCmDkH1t6Fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83yXRAY30HV66FGWv_qtGw9hTdjcCd9IskvrY2OXc7KkpGg7sCm8evvbCNYqm5Fg1zfEtiL9dNpXzWY0ZNs8qA8mFzkcic35D9moWNFNkbtq_Qbwm9U27j841fnLSYX9bUF-sHtwBTgF-MvyBXN2Wlsbc5VUNP_2qfRCjmXUD1aFyZPLV5n7kOkeC-TqwblMPJuBFoSpGFkfbphaJEPWzJm88fzHgacVnvL1WtVHRXtOPgPMPm71UkbLzembMAOnk9UBjiP-A2hcgjvs59Tj2uPr1myZlKjVSR7DBxwA5R5eNfW6TQIR-l4nlIkS-ghMaYoVeP73skTLpjFzLTalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWMrdfcb4j5sFhsnPHManqwOArAgvtwVsL6-mmgbwx_wpGtBgFp_GvrXNjpZATOatMOb3DNGM5T8lNeoB4UPbwP28IkxQvzAe1HF4i87yJ39CRqZGSb_dRH9WvFx6DesL0cqh_Mwaga-eZQgfvTNfFibI2IFLFUCpgn5LW8CkAo8WYWzm7f55e9_kpWtp2uR11UfaxAV_ak20Z8b50sHPcS3XXwIFNedUTV0lRHZAi6vYLLdxtwuesvFZ3zYOaievtZVQFPI1ulY3frK2Vxgpar5MQpU-wizB1KoyY9TeBkxqSXkfJ7YP2G60NrWUwRbqTQnILK153Cr2lQL6yb9Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
کانادا
🇨🇦
فکر می‌کنید کدام تیم برنده این دیدار خواهد شد؟ رأی خود را ثبت کنید و اگر پیش‌بینی شما با نتیجه نهایی مسابقه مطابقت داشته باشد، در تقسیم جایزه
۱۰۰۰ دلاری
بین برندگان واجد شرایط شرکت خواهید کرد.
💰
جایزه به صورت مساوی و مطابق قوانین و شرایط سایت، بین تمامی شرکت‌کنندگانی که پیش‌بینی صحیح ثبت کرده باشند، توزیع خواهد شد.
⏰
مهلت ثبت پیش‌بینی: تا قبل از شروع مسابقه
👇
انتخاب شما چیست؟
🇲🇦
مراکش
🇨🇦
کانادا
شركت در قرعه كشي:
Https://t.me/betegramd
📺
پخش زنده بدون سانسور در کانال تلگرام
🚀
برای تماشای مسابقه و ثبت پیش‌بینی، به کانال تلگرام ما بپیوندید
عضويت در كانال
Https://t.me/betegram_official</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu7V35d2qkRc0ODIqSSfB9NCYfXXFUycfBjYFNr29n6X8PbwmKyTYSZaThbQ5NkOHZ09NT4rzSfZXoDZFAIu3kYswMUCQQsTfQ0PWBN-3PM6v4mRRzDxYGlkgPAMjHc2wcI0EE0L_HHjNyOuKj9a7WNsGFqyVaDZUcINRdYlJZ3LKkL1Z_zZ1_rsPUuCDkiywxDRJDiNkVLa0S7_y-e3-sVPjPW07IkElbUA80mozRsT6jFbEYVb0aiJKohOION3OTYdLqcjS42mZz8sqq0GinAVgUEmok994lAcyfie1lx5Ld2B_IcfshCAwXfyijtqwTvBBXH1If824pLEHjtT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3jYE9xWhRDkcvGL2nG0gRVht7C_EU3chDj3u0deK5LIQZRZoCQpXIrXxgD-vD8k0mgSz4pCKSBnVDi-e9zyRuVj0o4WqsjGfzGR-Z5x-rvet2HuAIEmBKeqeL0NlooSrRhjE3q2gpYBbMIy-TSii6TyGbSZ4fDToHZ7saR8aNrGf1fViAMWh_G9ddACsXmmtOVwfFuuTn_OnaKln2GW_ipEAe9k0jdgIuMXk8vrKh82fGsHQIv6GQK7LKhY99OwBXGuAger_tSaEmfof2S4iWyUZvcynytKhPC3RYvlBJMiRwlNNRChgGsMR7KglDILn3i5XcUWvLDcgnrc8YRR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwn-w0f_Gz5lBtNFKc4qrTTwLy-GZQKpcFr7nKwWd274U1Z4O7VIILtHAbno5wP762Cb4nIm6W1yUbATt0prmFQ7Kuj0YfsUgoAjVLs2PGrkuPjtty3hu0ZIfS7airQoVWNegFUWqzQmWKAszow47SLxg59VOty7uw9aJ4FR0XpMynT15tbLlrTfbTOPh81EApp9GC80sAUZiZIb60WRIUV71mcYzJw2VombpzO_3jtkMln5jlFKMXTqXe-f2uwFF-ZaMhxSGW0Z924PIRJdbNY5bV3l3V4Ui56P3jBlXPncEthzoVSm0Y77AYM8E48rbfE1UL9iKg_Fjnzt0cKAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHKA0HM4ClaVBPKchLy1824XCLGKsqdT4ScOUF9kb-v2i5MpQrnqVkUg4Jsdq4a4Q_E1Uo35s8GTYYVB-Cqn_O4xaiIsEanWRyQPzxL6I3-mfhgUHOzJFI2U1HnZusj-y-aOZnd389pmmBma9FsO9cwETsRLbl_9AcuN8k5XASKG8HwB0OjlY_KnUq5gtbH-yTv5ae_UbvWqu0TDTrpvLvfIFH-kxnCHJXgv-k-reoQmR-5s7bMS8GutxugumiGxwVAxQpDQP8ipLXxYaq9StngS-DHtMOJrDb_mN6H9BgNAPXgYNlxASlukbuJSQM15uQnBwcj-V0-TkOzvJmyjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t03jvoj_Qi-uEerQ-IvXy0uwfP8iRjs8rwn6ZR52_1iAxF7vJVkQbJeU1gl-W5r2E_fBd2myeDMv6U6vVXVFy6Rl3nd5UPn2GhU59BmEvid1_r7jD6xhxVHjIUFyGopcSfV49x75uI_Ie0A-G3tdSEtIVddLL40h_bRW6b9vczZzDPUUsy9OSqpK2lgBXCJhOxnPJ7fAbLVmvFyV3hQJ-8O443CW0e53rJdV7wwz7SkKL_OtZchPYDtAFTCeXA8NfE6-B1iy3IU7tJ0Svy13q-aBonM9wPRNIIEwJu8hAciS6isepFY28XSraTc9W1mhMY910Hwv5-UFRHs9cXk4JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShyNF8bK-m70lRZtGZz1ynNeZoCDA31m9E6vb_OVrcpvnBLk2Ns_s0J04mrww11cbSsFMiFZKulTF6oGhNgNbBdr__nTa7pjTV8R0uQ_n4PmK1hW8OgAHshA-wbzcxRteJfoaDe_UQa3cOtCpGN7OCkfEbtBf2Q76XoZOLFc7ONdWw6Dp_H6P8gW_mAPU3b2885Q-lBcfdqzGoNhPdvHmXoRERxxhib_GU5URZzo8Cp3Wag2bEV5XkVgfZmL6C3RgOilYcK3BsgJU-4raVA2qHIEyOknvh2PYKZgiDAIU9ZsrFzhSqn4v0EXZDy7P2q-EqMZN60y-y9IH75Dcagi1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBHAg5hiaBvfhs26vcN6ivooHE7wSaTd1SrA6-mOuVHGWQM9Q0R6ZM90mYiI4GHHPOAvSMhLX1uKOvVsu_8kJOgopRynwy45ioEBkMDQUF8GR75oqjKF_NU3d4EuHL-0wgjTBtMx5IxlCfp17c-8gAiqppx3rACH39dettSgRNzUnasgdewhfMkXDVc-KwCI7Vkuoc1rihvKGpqAy3E4VUTIEprMeUqEcHEJZ4Q6oPWemTqgyXrzv_yMYt9RtfeF0Ubvt0QDC1WrKnFkKoFPRSqVIplrh1xty0O4qrcdWM35z-aDYKXXHGV_x0ACmvjqfIAiHBhR3OArALH17HLv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRpi4C-ulGoKfO7M2uQdbB19FfcrVVl2YbMO17jK3b7oqwqQ-wPYxmCAxizkTlc7CSYWuP3bjxYDV7XnGiN6oqSQKtjWI1Yf9Qiho2RTlnIaIrUGDp-ZskmEerl-mSGbt-hOKB0qb0qepCs4BYgkWQmn7LGZq_pdASNQ4SDxCQjZVCZYEBxx54iX6PxNCyXvxPZk9wrG_0Lxg0BztEKJFzNruiaejeNEXMepEN1v3iQjVtvz5DB4AdiBGgCx2PcxDBRznBMqsvxeeIjY1GO3B1hdqB9i7D7FgwbOkOF1rXVt5fO9F4hpBsc04Z0Kcc4YXX8R98ZAwb41JF_F97vSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC_MFDO1_WNolpQ2oXRfA4DnwOr2LtMQy1olDxvGmuQP0UKzxJcPMy1SdUntBHhOZg6bL5bwb2kGC4Y71hRKfw2aQwXLJGePG-aBFu6ppLWIpGHvPbKlTCkKl9HrdG9wY0NYVqlXuDkdedycZo4pfjCHo9Vz96sddIH67wlZSLrt3OSkOzQIi9gjeS2vyI1sFROF3k78mVRN8VE94l37ImHArtOeKLRK1_vVxmNkacTyThPEuGavukCOzwGzQI4kGVMVMkVorLWI1SZRMj32WVR0srAiwF3ZMHigJc0W2p159FEMTXQSToucRHOcz_9KaHj1LRj84MmN5sEBY239kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW4-kBWttoWsNCy5nm8Eqc-kM7a9Uq-eGuRnnwr11VYhdtXhTOZf2f4uzcuFEOrNcdIfIk-_ZT2bKYq-ZvF9u19G1BoYdu7WHXA_vn25X0mW1a-mJxPcehVO4ATXVdydDB-IfzN1ESFIpbeqi_24cJvU7a4k89C-JMJ8YHJl-7NsSnqMD1I_EI2ARM6Z0KsHPZT4F4hFzKzvFf_rMIAOaAIybxp1p1gtipGEko7vtn8QPjqfvSGCd6AGVceJTmtIVN_Lh6GfUqz-QiiDEnfXWmag7MY7x4pdJEZBpl69ualpiyZ1Up85AIB4B42CwvyL0X2EXxqY3zA2nN13zePskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fngO9RN-IsQcQ2tiEuJ6xb-qTf5IpP4VwVZyZXnmAfNpcfFqhxyxBljJ7WDyBmSpSdKFuQfDZlmQfHKZLOuG6DmyTVabL1UyunI3-Tz3MBxPM87Sy6_K4dYwK2DZmHecJxkB3rRLfmAMGjlOA95-k55QyGx5Nj2ukN3ALUVV7BtJjBHf9-rsb8vUXR3eX2my87JzUJt8ufd84fH24taw0d8Ru46Dyr6aqodlhCAUDO7bOpWPJ-DnIkMATaMaFw3RuJiU7UYm4Io185JnyZDCYMAAXuM5FyWV2q_ZFZ1UuFJXxk2AyzXeaB660zbHeUCgfOcUtYyFglwl94KO5SRCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXE1gGMEHgaLwHQWlsLxGz-6GBvL_0kiMyhv9bO_5cTYQArNwIwMIBOPSDxPph1C71X0pZgy9qncUOPwULUFLYJNwuYxvDzxjX6mDDQfArLQzcI_BiQSRLM2fg1B5ATF3UEJ67TxqQIppxwxEgC4CJ8YTv-G0D2Jd9vy9YV11HxXDhosMTi4N6PCazKyI_GW_KPrXdisbCnM29Jeal_fJuNia-M0iqURIbwCknrF03RD4q30qqMUls9ak2ccV2ZM8hOYqg2Av1E8_0Mx9o9qYgjBT0qiqj6RAjLOnm3gD4nQvEn6mSZV68jK7f64FRqVncqR4y3WsXIboNmsV-2IIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sccALvc9-T6jjHwWU5p71cx2OXnex9kQheDnAvrpC9epDcnlGcRZ5lhgpaWa0LJVqcLX3QFsjMgjCSdQVBdgKRE0eNWl4oWdCnGDwftAC4Y9sBez6Oue710f48Z9p_S7jcbGXJPcnGK5PzK4Qp8BrAn4DKjDoR8FsuKgfcsynf4_L7D-6vF4qS7zT9iHbDw2TFlm4VL8noRbbEtX2tsk0PPkawmGZ7lRaeLnGi_mvI5WtPTJcMKjAJki1mVWiGceZaVpbaBwIPTgofe6I0xhSqYHd2pqRa0KmthrVzjJuF8xDy7N99nUihWb9Mq6E2Tp9LU2xD2Kff0NdVQ_YM6ESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lwfr9swOHVhP0XTvkiU5KUvLDDXugluz9lYH1IgAH13gJoNADQ-4xjAMRyyF606xMA9QROS8qZcbZSY1ikYQnQow5QY7DruUUGgZScT01hhvSSGngNtAUmXmmeLEJyu07i_ezYLBFLau1RFAeouBJde_NOTHRySOZJ1dxKSA0ap6MJyzTl8gXXSnZf-leMaJFKcjZ-W5Om1VvKT-5IAje9A8QWv5k8mi1piBa2d5XysUJRXavHliLpfr1itL3VmxMUKzxaM2g20cnfgIDxN50N2PWJTy9kUD41t4G4XfALPjvhvxj3tUfcE1jmTSNoN_tKWXW0f8NX1_nNCeqe4MAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=JaVGH0aw7Nk4jRMoXyGkO0D-pNEhSu3CLbWEh9j3xr4YjE_3nrwTRx4M_qC1BmcQdMo4lwVcUA4P85C8S963sFCaHL-qblolHgpEZpBQ1sU_i1Z6jhvptEtQZbyfweIvQkgpiLwM7NArAyMCfGukASdotLZ4DfIzoVdWzAfwzbWyn_hMHxhGoSGG3dJH-1JgNRBexl-tc3yQqzk3-KgTUCr77DGmR8vda7htCuewMqmfnwOVph33gJlauyHeJF-mPNSsanQaRJzhwuSXuwEclSfQ62oCa_O1BKTDicsNcpXji_K678P8EmDJW-DabKrk1IuEDqU3qfT2GLcsiGbf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_ljl4K7hX-2_TnGbMLbRY6bEN0aGgJiCALo0tig8Iz13Me_zkKcda9tiVp-zCY7MWlG0akIkCh_HdfvURrBJfkrdx1qCI2Y5EqwGIiTuzwkMfQHRne4IJ4Yodqbn5iMrxnmuTomAD5jQql2roN9kTk8FEC2DiXXvrYA6PmI-IvVmJAH95gJS3MUntIAMmYQcbslGYK7piF-LJeSnxD27y3tAtQGDj8bw155Ys7mGh0hOZpZ2YoX-CsjpOpHFNvaLMYaLc69av4BTo8qV1uqI-iel3e9zpB_gpdhyM4QMeSWmtFnxXNbIiaRby0d5Qovu8pHnCk9bYw3U0SQB8awRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOIszfgXJ2waMuzdk0uQBCRb2PjpNPzIpOIyTa1GklWVXGJvcBls2KoTXLbYAmtA0-0FavtMrGq9jYLqRguMdmJVLgRYyCDoevcvtdRvdW_0Q5jAO0Q1Im7OxdhuMRF7ft9fVj8l2ZrE9eoAOk9WLpALXNuHd5u8Hk_PW7zt9i9aa5925v8BHJ0WZ6rv3as3aPgsBOIvEIsY0WdtzwPcnMUAPYTLxtdtJAXMky88Qo4k3a2iZXIDF3Sp6tXlIX9J13LR70M6vOthCadSAHCRE_YKqbFZRuj42KgeARdO7tYZ_nvv4rp9Jz9uk-o6JojT42slMpkyzMQviS_v2fDxsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEfqi21UmHZtUXTnwOjsAQSFl8vigKbE3hPDdIbEy9BlDcplovkT8xPoyLYQRiPKMUqeXxrZWx7GKm9Idl7unz5MWPkkMTwgh9OmD6HLIjLolxyR51eD8h9-rpK2sxNStO0g-fBfiOdnMgc13Zilhq13H-2Dskv57Gnc-iYFOiOQqDfojnFI7xk5KTmxq_8b4kGXrpzBtMfDDMceba88Yl2ikk-o-aOWalwGzPRs_CRdafq824aP1APrwHH0jLo5RN_Tm5T1vlIDwrU3d4qbLGqwMtHmF9O-5_V5y4foaohdcpyYqAsjtD4Ub9crSYFnC1RF6WZZ2qrpKxJJ1ipCQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbWS1gFEePkdHU8NOkxZlWJoOciUdRaIDO6doBG9NcycpflKC-F8kfIjI899LHWl3usO5tvD2Hq63nFK2BedW_H6I3y7v4EfRFF1bE4RvyFc8NBxarcwrDSe3oEKxkzpEs8XiyvhljuEFmUSh4RXNUJ7B08aCZFvnl39xggMUqioGNIB0476icdrmdeuIhsP6QM91OUzeYVOU2EQt3Atz_DrP68NCIBvTZq_Q8-OxcXDsBUiXixCFhISe0BMfyPVVJqVNFjsvBJqkkNw-SBQZJSjI7HT7dZx6N0AdnKinUKmKZ1Eae89nAzfOG1HXyBOH7NzC56-SrhHe5mvecqktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=uywF7BCbu8OguHayGl8De6X2l4ovpFeORxYapwHV4tpJkurFMUZtMVsvjqRhu7avE3UDPQIY3dvgKABr-20D-fXd0CXsKfUrhTucvYW8HAXxbPqdAyhLK7ND3H-HXcfTJbuGsCVGRWLd4gf3Ohx1kd4FpPDHgJl2doudF5sOnpeQZ18s-PlRZNnLsOl9MvojkZ-bTQXwBksZ8YlFmL2VF9xzSruMbQMp4zhfqmCe49JB2o3ubw7TsCn9vVzH_kC3hPPV36HnI2rsZC0y01FtY_hMES25KAgbb_ZfytRNtcACQ1WtsaMFyEg88PmsQd-OVgk6KHqit_tkWd6FER_O8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=uywF7BCbu8OguHayGl8De6X2l4ovpFeORxYapwHV4tpJkurFMUZtMVsvjqRhu7avE3UDPQIY3dvgKABr-20D-fXd0CXsKfUrhTucvYW8HAXxbPqdAyhLK7ND3H-HXcfTJbuGsCVGRWLd4gf3Ohx1kd4FpPDHgJl2doudF5sOnpeQZ18s-PlRZNnLsOl9MvojkZ-bTQXwBksZ8YlFmL2VF9xzSruMbQMp4zhfqmCe49JB2o3ubw7TsCn9vVzH_kC3hPPV36HnI2rsZC0y01FtY_hMES25KAgbb_ZfytRNtcACQ1WtsaMFyEg88PmsQd-OVgk6KHqit_tkWd6FER_O8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nNZeb243H0bvbCw8i3p12bs3Vrmt0E5ucGwjELVCVEfWpgxiIW40-22zgRY0FnrOo96r2LhW0MJ5e_CODk1_zmqUjMMDodARs8AJym7FyByPIZ32ddenfBg28IRVlRyz37Itjzar5-DeXbm4tzYfwOux1xpzCQP0zXX2L_kANIbGxMXI3p9ncbO8uXLpJPcYDUsHlz2EaHD0wt9bRxQyQEse55OWW55kvub18nEd76KIA42SYgY6fXEmT3WQEuatklmgAUPDt3lsz483xmit2VFArcSbj0gnZMRr1u-uL_Eso2OiynlG8vv4vvop_jb79W9Q5DsPErzPElDWrs4WbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=nNZeb243H0bvbCw8i3p12bs3Vrmt0E5ucGwjELVCVEfWpgxiIW40-22zgRY0FnrOo96r2LhW0MJ5e_CODk1_zmqUjMMDodARs8AJym7FyByPIZ32ddenfBg28IRVlRyz37Itjzar5-DeXbm4tzYfwOux1xpzCQP0zXX2L_kANIbGxMXI3p9ncbO8uXLpJPcYDUsHlz2EaHD0wt9bRxQyQEse55OWW55kvub18nEd76KIA42SYgY6fXEmT3WQEuatklmgAUPDt3lsz483xmit2VFArcSbj0gnZMRr1u-uL_Eso2OiynlG8vv4vvop_jb79W9Q5DsPErzPElDWrs4WbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JgPTBBHf75ZRcU_f0RYfQroLeqJqF0y_hc4qOHGcwXrmCt2RBHOP08keVGcnB-WFERrysxSX2qLRY_mddUwSM840MBTY5hpCLl5PWJsXL9Fuzk5T_ZZJtVjE1sd-hnm-Akx2YRwmx6BTIKwnwYK9zQ_Jxaqub5F296DoEXZ3s9QIvyltYke4YzWzihVa13w1J9xS7q6-S5VCbCbP_EDNKHYLS9oNO8vtG3Akv5l95Wz_8w9_ZOEUGtqydhXB0XXyC7NYwbyWuYzRsbf0oHUQZgJytwEdFGloJUSaEnoQlzJ96tutaCWXzX3K940l7WBDqahO7nNyT042USmDyT8LDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O85qee--oDlE6zTuPqzSzF6Sackc_cmAQkqKUsS1ZIEeEVPJCX-XOfXhS15YUrsbue9G4HSZTkSOxe86XGWRHQzFlBgs8wcq5ckG-6qxstzPQYF5bNLmKf15ErMme8EpIPEt6ymHMNuR_SCLbnrYkgRLtDwsQqg4nKSjYnfbC54-O7G5P9BNX91KS_ogtGE39PW6AEe4P0CzwU3jTe7xsE3ZxfIZDkXod_1Qxmsi42htyzbs7RBXx991OI3FkCoxtmYSMRC_ISmVP145fSz5MC0nV455XMMeTjAyNs28_wsJRoezsoygucdntW7GrLDjiiJySHNZF2qEpd3xlD8gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb9pcJhstbYgHygbsJHgqu7AhwbKtP5ZEkFekG7eW8F3mWoimsyFU9JCHRqhlbA3vazhsDPyo97068T7nHc_WDzi1IbF5Fs7s0PpEuiR0pUCv0CkD3dZUIPBmI_VlCpJxhz0Irt_gWYKIFRqCuzW9XZHjbDbUkIKA1nrLaNdT1MQe2PH3K5ddnsxRbu3vTIrF5J9t9sn2MudK_qWcfYL1gWq_-gVrBvT8thNcsFeSJFSXrsTJ9xd45Non0SwwrJTt6SZy00I-afkemk6QCiAMv5yf91kNor5kCbQFqH4kERCIrsGPaW40yrRV3vjNts0rDGOjE9bjdTfzZVWmMl7Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJH-d08DnyOzupvK0kW3fVI5RzLAEMjv8jCR86QPGVVle6L7w34ag6-5wznUrg6BcYCYi-ncndyUridOo8J_fQh4ntl6PhJ2f9Bmu_k8yFyd_AFAA0cVIIGhhvGN315klGElb77Ca1VMJ0djXr_Jeyy82Ha0YcSU8SzlFLE4ZweQGImxqH0sb3eCY1KUxJ2C4nblgLqQC30qQx6TP461kbobkA-XVgk1X-xG5ODOgMv_Pv0jHYQttxNyIuAVIBiGNhoJRQBiZrVl8Nn6yVJJfGgMd48N2vC-zIs1Sl6Z92YCAef6MvCGKa8W07cjtfVoxbbiJls7UZodnpY8fVmz5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_EgJ3dTH1Q6Wl2EG6nFxtZF3I_3Xhgb7NZnrnwIzRqwuJ31jF57NvhG-lNlhM6Asc_GcKTa642IQE-q4l1gJTGpPpoK6QeREePN52z2diwfRAjbCgBH-x5dd-x7KqAgiuQgBfhkQDNreXF_mOf3RRfwxTiuIrusQTA8eJJjVMsl1qV0GaqQwRn4It1inMxbPm4tm8x3Ea5CsZzmm5imcQlgCHzWERGETcEwTLWNYKsinYHSPCFZ4-NdzkJX_xP971flyiDYnyzZY65TXXUkjDn8Zf-T4P129nypEGATyz7ZZNyekVs35MFeNPLTiM4i0x7YHt6FZkd6DDSWHvswrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAKfFHh9SkBgZHGXQxXk81A4jHSiu6r-6KVJqCnRIDWqh0W2J9SYtnS1b9XeV1lyZkcK5fFPSYxIyEQ4rzTZn1I4NY1dRy0Ms47wVtbTkeWu0yPbS4cLec70HsLYii1ODvSn_Qtc-kc65G5DNi86TXUUFgDkntgGjB_0A6VzJjODkkxWqL88mD7HC2S4aDLcAD6AD3FwTC9cWu5XeYsAczUSAHRwSSgmCHoixkfoNoDBzh59Ho5ldaIumWvsa_PY6Ubo9FQLKeQu_znSDA9BVfEiclgairaaNXPmhAjAd5UZ8USt2-bglO0pPFZA94b92Nf0Qa52kZifV_d6ADyqLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmdhwolNoonDrgLp3ZNl-E1rYvNZccjiSRMqP6b9dbU5rDBojofzkfBOTd6Cy1wiDi76N5dsxHD_E26FCXJtJzcSfLV0i1OZ1Nh2Bh9ldzLwdkwOJRiq2c2HOqObucy3-Giy264UttiBQL4N9KXUZ1xinJVzdrfHU-cp5KhxoeDV32ScJPBViZEnhSFidpus2lvRjscKQSQFPkHefHjmpFOV6r8UR6LsSSbOw7-HFXTQQNCtRhxC2PUnk2PGrqN9_m-qLLvUMZQZWh2q4nPN6ISYZ5OS_Gss56W7KwDTbCLGZv5O9tbUlyM6wvQrcgvzT8Jg7aCBEOjsEK-ANyhuPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=vZce59_IKC1X4LcSTAL6v_q6XtHX36uDV2nttrO9zXKzZF1DMI_meO2Acpa9tOoC1PNjmj6H_teGCZc2zYOqcb2Qqnt6jzs32UOb03O8UJ1cP0vOibu09KMgMqucZvV2osfeXGngilaxMDE26wb9mQAAJRWvIonKVC92f7lHajjddWYmb-7S49nN4YYTWbuYFad0_3h0IaE67E7xq1u-QEGHSLE7LcrbV82sjgcxxXjRWt-dFZ5psn5ZWS2TEjHHAABnVa5BIDiEjj6l3SDiKNcewhjqbNO4ckTkfYJYQjP3ijXk3nZGIAoMqO4JDS1_OafDLPcpnqIuNFbej5OqWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=vZce59_IKC1X4LcSTAL6v_q6XtHX36uDV2nttrO9zXKzZF1DMI_meO2Acpa9tOoC1PNjmj6H_teGCZc2zYOqcb2Qqnt6jzs32UOb03O8UJ1cP0vOibu09KMgMqucZvV2osfeXGngilaxMDE26wb9mQAAJRWvIonKVC92f7lHajjddWYmb-7S49nN4YYTWbuYFad0_3h0IaE67E7xq1u-QEGHSLE7LcrbV82sjgcxxXjRWt-dFZ5psn5ZWS2TEjHHAABnVa5BIDiEjj6l3SDiKNcewhjqbNO4ckTkfYJYQjP3ijXk3nZGIAoMqO4JDS1_OafDLPcpnqIuNFbej5OqWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbvUgXO0fLhY2E6QACO4B_Jg81ZGtBKEQLYWEXYxzNOFINkZVxzyMXcNNILivNP5vui4t9I2Iw2hQ8z7ChiM0yYCFUNajIXLej7a7qgezcI0q0ECFhJcH_xJLthjihe31t8gGKm5p1aPqHrYuDK4d8eO2kTRWZtjJkSIQFJ5WAdeMyqsYIttCs9pefxm4TFsh2AbqcH2LCGDxZ_TtrgDWVkoeWyufiv7lCFX5i01ANZOcYVpOAQyy1ImQN_9O2Sog0uF7E81c3vgnjz74BdxUy7eoTgwSk78PFARJt6yQsXuRxBigk8NbrM2YxwpyqLMwL9n51-utq51otAQIaccQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOT1zIDhhzKPJ84gHp8dpVMhyzAn2uRK7Geb8yg45Yw50YBD37_kiVqOeGmOvw-LBd6QmVjoRXbahD1U21AluGAfKp9MRU23KJcnkAG8EvMqDxMo6NuOT0njoPiGMAz5-NrVD4NXOtydqZI_mlzDt8-WZPugP7Tz2ZHUN4zJII2Z1m9M6ztvDHDP1SnLNYXzHXEwVUiut0E4G-KrxvDQFzoHz2L_pELExGU3TK_Mnv7E5-bLJRLztqf0Tu7J87w5h8GPm-Ya3eIUVFGWoATKCsyFN2_Tod37VVgEy2FAa5ZeNfYwelTfDkPhW-FggSL9rSJjUI8PuKMFeiI-Q7YWcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Uwl9w5tYO6Pt98GRT4qNiC4Xqz2peKFu0GTx0_3BaT4OC_iqkwuF6QjBCWVYKOFBTu_FWpKGdjf-14I-id1IWj9g_SPXNr1IhZ3UubejGAHV7MRitJ0i0gVFdP0IJORJs0OMDScuccWVuMNcPgNqJIx6BDnIYqx8VCkgoxyTI43u6nsIlN8CadINb9AgmRFy0T6G0fy75zAAabeuk9wuqg3VHoohOGgpJ-2NVTyXt5FlZ-ks8-L2q8RACtiXJ1nVD7hAOrrAUlgvveyiaJqiB2vcfqGgf5CYJ1nRZ_ITnLFt7iQaQeMxjMeZmwDALGs15f4hciOTMndMAKQuXoKdwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=a50XN71xM2TtISbnkxaLfBXyx8ufm_EtqnRqzp_d35RUTsR4Ye7sSP8KEBx7fMziHLsglR0Vprn2EJD_AX74WVbLzR7mEPUOIz7rIDxvvcXNIY5hk8kvC5CMTyXrL3gtmvkKMpuIlIK-who1me3cOORcWK97am4J9UX2v6vmKTJr3g5FWoUTsTkGII_1TKy-7nEmGti4sewGKrkRVBdV6ZN_RB1WuX94ZwwKT5ju2-xziCNag9VtpCWJvgZDmdjtcSlq2bTiXCHtala5zNUO_UlxbiB3eys_Xm2z_IdjNaBkqQZ1AytoADHBEH93EBIBRYkZBCsDqIPBS0SUkvqK5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=a50XN71xM2TtISbnkxaLfBXyx8ufm_EtqnRqzp_d35RUTsR4Ye7sSP8KEBx7fMziHLsglR0Vprn2EJD_AX74WVbLzR7mEPUOIz7rIDxvvcXNIY5hk8kvC5CMTyXrL3gtmvkKMpuIlIK-who1me3cOORcWK97am4J9UX2v6vmKTJr3g5FWoUTsTkGII_1TKy-7nEmGti4sewGKrkRVBdV6ZN_RB1WuX94ZwwKT5ju2-xziCNag9VtpCWJvgZDmdjtcSlq2bTiXCHtala5zNUO_UlxbiB3eys_Xm2z_IdjNaBkqQZ1AytoADHBEH93EBIBRYkZBCsDqIPBS0SUkvqK5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvc0J3leS_dIcXRvacTWRL7LTmNMJuEBCJxd_2gaItb2UR4pZ0mZwTtE5v_g-xHbPF6s01m-IZvKt8tfmGHfxZyMr2heSZ0wZ-kvakADf5prERdx1xFHbvQ1VhgyXgkkpRc8YHvnXiueDQLsuRz7QDcyKNfTPaHstgWmTrs2t1wU2gSWOmKkPQkwQR9LdTg5g9XJO-mO6jDNPfgqu9moEa1KYyFNT5EgG5HX5Ktn5h8gJgqJo8ao3H54SyziGZ0nqN-NmxjDndi5ghFTg_NZ-4oaxlP8OnSicDW8ni5N03qDNhXpcaZJy1Z8fUrzGUwcDHbMSB5nS791BJIUnfnbMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4NlhZvil7KxKmip6vbC8VSiRBp5CeOblojmRYaw9fPf19mAAVmc_eiMPRWXQsIuWBdQa0P0JR_56PQqozY22v0gymhdfKLxrrI5uPcR6veHIxMwPQQMOQBq4OrWZ6JWQWdGgFtPa2L0fB3pXjBH6I2EVZ90lxe8txOldmeN3DIcq0bGQo1iYjkfROkTBHubQ_sR48Cdbmq5LYY_tweAYXE8dZHpJpJixVfzeo6BNjRUKvmrepgB9dXhAysvnNXvGTlabYlKMejafnRRw2PmpOlm3na-sl7aTjFWEtuhgqlPBqaAD4G5xPujNvn5SFlZ9v1eg6IUkOrAx4ad4iIMoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLcGvOATrDvDLYVxH-IWNqklINKM1GGart1Yp1sX59LgDwOjBy35y27dd2QazTmBSEhTKf9FzAOUAqpoXf2kat8cyb2UFO0nTEmUgQFD8Tw8nl05NuIdJV3_fiFCSQRttNFEJFEDQo-l86naF95Z0TI5HK9ETAHPsALFwRheLOTiSguOhQJr__UsqznduWmSEPfwhw_su5ATt6m06c8NhSHDEAuIy_eulFm6lAEkU9eYNfAAKVr7QPm3Yul2o8YwiR_uQsYUFBpE0evxTH1RdtjCA_bwk4frA1yPNrkxFVvgJa3iWcqusg1QK1M83ufQpLCQRQOX9Fpvucg4QQI5Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNW5Pi3J-MDPlevGQQZt-OTwaWWUUkypxw2OXzsU8LSZ8izWKO8_C9e-DyJ5jhp8-5Y3l0LfGOHDHDIda6201yWQaEUQnq9SI_dXU9oilPBqZ77AyWKIT7UYDWjYFCmQiol3EGjQgaWOMwUZS5-rjvpUWa5HiqYkC3l9CkmHAKYa09QVIIL-f_y75Z8E0mnYAlMzGbdEX5Z69SVZdU-tjgOjU8x_ZxufdAVseGUgUV0rgXJ5jyawUeLH_qPI0cgwelCG-G6pJ6_TGGXw-Ag9vSM3Chn0krFEH_trnMQUu-hKPJ162ddIC5dajZDmWbi9q0UcgtLO-wiXhrQdChgpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tz64Enmd7txAcpXQzfCY66bHG9x2aggnKNvLzi7R9jSi-pFWmfRWllVUDV5KAcZ3WWBIpUQnHLYjJrMbqNkGlL7qxfnm4JigEIcyQDEGb-2CL2VHP72N3CVXYtFPD8YoFGrfiV_Rx894xmuYckLndDaTzBhUCG4nOvXFTSilEsXZX5vIK7PKq9K1UsJi6GqUd0ofuacExojnyvi1P6n4WwBNt-3GGnfxsHPRgIw_FPqPJ8XZ5lT63Z8pumPNlMYHZKOOZUxSSEMqV5DugJvwKYKVSLy_6tYwRKDBvlgwFR9of9ZWVTWSRMENTIfA-4Bok6ZpNRncg-AhjOsEbBZ0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=L5d1TBpb95f-lnUn_IdJ7ImRA80Nt67n4_e_0i1ueV1gT2frUq0z0O5RqCTsdNpKnVrAi5HqLxcGbsBTWi4Dcg3SJVlZuea9qMMhZB5CuXWv_LZLRPXkt7ABDnBd3rBFZzZitWa8Nh50eEP_g1Oq20Xx9S6YC5MJh17mjZnbdkgBAYMaqrkRoPOAxpYFDnM4v8STfC0QfoHAt5dtXj6B5uuWNt8UF5xH4yxNHfpUcgCda0X1iID1W_KFGkGvUaZ6cKrGGcbScbR2hzklUA9aoBmk5Zj_ykS8CY5lhtpDUmPnTbQ2xvdEBjd09GDjtfFP7FytvfX4AOMmcmAVTYfyAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=L5d1TBpb95f-lnUn_IdJ7ImRA80Nt67n4_e_0i1ueV1gT2frUq0z0O5RqCTsdNpKnVrAi5HqLxcGbsBTWi4Dcg3SJVlZuea9qMMhZB5CuXWv_LZLRPXkt7ABDnBd3rBFZzZitWa8Nh50eEP_g1Oq20Xx9S6YC5MJh17mjZnbdkgBAYMaqrkRoPOAxpYFDnM4v8STfC0QfoHAt5dtXj6B5uuWNt8UF5xH4yxNHfpUcgCda0X1iID1W_KFGkGvUaZ6cKrGGcbScbR2hzklUA9aoBmk5Zj_ykS8CY5lhtpDUmPnTbQ2xvdEBjd09GDjtfFP7FytvfX4AOMmcmAVTYfyAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPAf_nSpMEEV5YPNcFVcwAs0-kkUyFf_ytKu641jpikpvAZQUXeuSQVJgcicLzzPAy2ng6lqfHdf9DrcPi5Bodj-Z0Pg-qegp0jMN50KG-zZD486UFbssQ9SrHKlFkMr6XxGCKPAI29AalseTK2tLpE7-up78lgPO7JsjZm2SqmXHKVaNnA3HhToRpKR-Jlsv4ojpsswXRSgyDObZr-tDlxT_08l6YvApQTxD3bVTj6_8RJEDrsont8wZDAc_MgOOcRDpQPjpupjhZyT4BAiZFP1W422hsGW_1Zhl-Awz1qxj9bxqIHniKdTZ5oBj5Dn0SYMpc4z5l0wNQ2OjugIBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exIxaAaHV-idBLmu0wLiYbu1dwkyMwoAje1g6RiWlL2wfZlRhK7Hr9qK5hkAk4WTvG2Cur9xgGcbdw80_ya12S3Dux5lksYgk1pataB18DhijqiYFiV8be7fIuaP98c8a13eJe53BfSI8LTgc-2b68sDr6neUptfUc1fKo-TcfJuwd5r1DHaYAfgxA2pIl9oUvoEMYvzuUYAO73YhZ8UAgTXN88BORpaVbxuorIbMySD5WvoNxX7JXJpmuxmxeL2Gbk5aI1CUERZN08BsVx-U6Iq9m9aQJlyAdfwlsxnzGqn63L69L4NJG8dEljRRiCLX7hfT-YZyEwDX95gA8G1dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpR7JzbvjsrywUnA6MUZL-R9dlS-PARvIyRYL324wus8UydlG-BxNGzxiKQ16ST0FvmRteIX6eLEwBFvFoxQhxSL13Ay7Sg_56hZs2zP8jF1Pc07CGfaM7HrpM-AldUTg6G0DF0x1J4p_bdMtUFBRFdnq5tUvnTmYaWKbnI5HjZXxgDuiHxSY8FA8G6zppYgxBHNmIgnkAjAnZdRf2nNxgFfSshkOhfdD4ikwq8W9mvT5oOQGjJOXr278s1zsewIltmR3ZQvFFBgGMwq5hyinaqJ9zBs7ePXAHfquY3yBQ0gy32Kt7b1QZpsryXlWY2sjzqlfsnFHEuqCGyF1dtKLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SekLFD5BZM6X54pXrRi8nQP7ewRHxAXZw3StTwUk1YzY4d-dMLJCibuuTQz99AJPp-WKeoJlR6XPN0q3yBzCgHI35gsZVSYwjr55B4-4h04kUurPxQ5ELTc2xJw4uzy3AAtMSS1bmekFcjfSZ_npaU6aGQj6aNytHF8utlELWvYfMom9Zt1HZ8UulkxExyo2xu6TMNndjqBt582qRDdjn9jrfwEscHE7A66GOO4fYbmlXv-o2dapuOq9Y64LElDrjQ57tEsGcXby5Vlr3IoGU__x9uwp9PXNGkoWV0RV6UlNeGrwo8Osa-fKtIk6feBZT7n2dDXAEfcPLCxFkzxxgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTFbIfQThB5xdYAVDJM672nxwHNa66iZS6vm5Z4Cxr0wGsON0gwDWx6xeAFYeoG4wxm-lcUE6exIFv2AZ6pDD5q17Nm9kIM3zJuAG5tai65HMKvvw0Urf-aw6xdPGo4uhFz3B5Th-MhwIXOwt61ueTVi4Pjc_w0Vdg-CIoMImKvJPzSYlaelGP9R2DR6Jgjb-b_K0uVEqvWOsV-CdXlzuKlJlcwpn2UIq2BxWdt6RUBPovO64wbUOQX5X5ii1Bgj6PgiuXJrFnsujC9l5D_FL43s0CIVBv-0fyL7JSodAq4kWE6wBAxOPlAskPbYjWYwGTrvVSxOaLKzGUjqn5PeWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXKQiy6aQq1GPz1LnaxF6u1hR_OO0LmAqorJrH99afC_IbBhAAVafeneDP0IkIqW2FNuwRHNOI0526SY4wlbRssid57fNLnmyzJp_gGngK0pJZygcP5kzkBQh2p6OhtEv0zPscdctgEtX3izlQHHaxsIfvw4OPC4p57oQjWTJyN2BcJsCFYhPgC_FJGQwSq3kRpheyhTisLNlz9w3LVlAp7OZ-m_Rpq0WHpcaSkAMsoTfsceG18xcIl40TuUqjPM66lAOGq89JQgJzojhfezN497oqpKbd1T3uGYsxv5_L1oSEnJxXwMn6MBHvbfSi9CD7Fh_LRvxEh7zKM2JKQe8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=QjMpV6FgfCDyeRL3nY-vpOHyJkdy_XG4Um4_6nQ8FHYUWgtakSYT0s-2Z4NM5M-s8lQImWgr9V_ahO_MrboTnQ8pUinZzr3phKuQpDnOXCAkysXgrvK1vLPtp5HwHMm07bknRIihfljCSyXgpjenF63xi03ekNpy8Ai17Pje3TXRX6m7wFIQsM71U67ACDJXGp_PdimJbfBzBu4XMmDVRdkGQOhgx0HWbuROlZiLhqE_KqJKfdohOaPGdI3VR3L4EtgtrCelMQk-rgvrcEIg6hilmq7U13mvLKF7X4ThjVuhsXSvFCVxgaExzOH8rHBWjA117RQMmdLfVolMxjCjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=QjMpV6FgfCDyeRL3nY-vpOHyJkdy_XG4Um4_6nQ8FHYUWgtakSYT0s-2Z4NM5M-s8lQImWgr9V_ahO_MrboTnQ8pUinZzr3phKuQpDnOXCAkysXgrvK1vLPtp5HwHMm07bknRIihfljCSyXgpjenF63xi03ekNpy8Ai17Pje3TXRX6m7wFIQsM71U67ACDJXGp_PdimJbfBzBu4XMmDVRdkGQOhgx0HWbuROlZiLhqE_KqJKfdohOaPGdI3VR3L4EtgtrCelMQk-rgvrcEIg6hilmq7U13mvLKF7X4ThjVuhsXSvFCVxgaExzOH8rHBWjA117RQMmdLfVolMxjCjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kvs4vwWbV_dOXJszSPWU0qxC02vhZyonK1fgQ2DRqlktf5H-M0Tbb_ITxQGxy2K_SovbgGYiAoqzH_jMvyVyYrKqs1I2Au8798EuMKhikos0ivOyQuOJUMQTUL-K888C7f-HceOwfLl-Ds2oDKhCaGROdR0MfK2G7SgyvUzi776oGLAYr49hyvMngV0rmmKOYhvko75yskZazTe-MijQ2WvetN5AQRFT3iHiDXPJwbFwOWhmlWV6N6sFsLcCEdJ7QpKo6HJL6DfkU0UnHLcSDRTSl2VlzTM6szKj877CaEzYSZ5gn6E-xIfoAu_-V8z2TfCo08bLeO2uQvYEfmpR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4zlbnQUJBZYugFfdIS0ExUGn030Gp-TWiDPT2BD-f9TrOh4A-KhEc6gWGINcMwUAYB6KFBv256x6tQaEaezhf2EHej_1v03OshdhvifnfLzJp7TdeTb63LIRjcX7m68Pcox00aIdl8LwfAJjMQqrq3A9wVM4TVA-_GB4NdKTkR9LtK5CcrruTSxfQcf4szM3tc4fibc1ApYQSz8aVzjRMJD_2t7ofLJIdOQ6cVsxmbpy49x9d0XvCGU1HiFEkNe1sPgXM9Mn4EG-MwdxCg5aBTfu3Vnjb8VRXO2FfI9rSjFlkx2vk_8_JoeQMJSeTkRLaAJ_GyzjHZ8gIH76Rxjew.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcaapgvDL3NR30IGkkKdHneUWQNkQbusmDP2bj_9hcae29FWXZ-vd6SFVBSuST5ruLxOkTAaZgmJo1gDRjCkAQ9GANLojp5rkGLuiTreG34rwdWLQ23B51BkfztO0Jozpi51uLXyJjRKf5R5ijffXnL-0t4b73Hvr7qyrJ5yN5fdVGGge2qr53nO61evUZz7lwKImYlF1HnGuYsp5ot9kzYkPIQdS1huccFkTXzhNq9L_ltt7hZ6dnEoZH4gyrSRWOYtHJGMbW1B566w1NhkAsmnP77KyUb4plmfZQ6NlSs1oN_EWJoTIVnuyHUa98i0TCVdwMdUljeNU6y2qWtWww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgDopqB0ge536AyrooKstjwvpYUvw-3CsFmayiAPoYjgKVwNkVzyPNHeTZtV59pYU8v_EB9JATp1HSqHYtdUPTid6Zg2GkRfpKRyAHJ3rj6nfZDCRPZ1zdZpWFG9BRcGUm-Szy9ahrtmBFRwh3WHbKQg_uKrKc5yc9IDrFucSRQ4kjpcu-_0oXrlkLpi0utmrad98n8VDATPoRmahuHV8olnqoJxBAurSFKDwCJDTiLTa4zrsTOpI9gEKBu_cAgydoNLrZMJV0HJKuRMNGwEzw3tvVwIPv6cjEkDgWJ-q9pWTuphgas9ZTuD9emSY7mULKBldlClVdsjK3fFPRo8RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjmojZkZrvS_oeNYCFDYlcU7_5B8dVFznwLLTjWJ8TtUS3XoERD2YLOVTZKQzzFrP_ZtM0GU9MAoiYlVdr5DmF76LRN5KuaahUvyl3OuoKs2ekkfobyOIPbYmYH3c5RGwZMvT-qG8cu-TSTA2HJ_BYfXT8ywTIYZ91UqbHJdqpqoM0rYFcEk5YS1311w_G5GBvStE60OI-A08oHg5Jzan5D72FxWlMj13dmGj4roiKMUw4-p2lPLFN5iJXWTnuY9aZoy9BNr4tlz8jDx1psIsci9Ej1sQtFRgYrF7sekY5CbCF634s-SyM89sSDjqsWUXZqPYwXoOijV_Z0ARX1EBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1ifXfVyR7C0VuCGKN8GfKjFHABzNDosKaha66HbUjuVOKaBjAJRdzfO2wggz1Ua5Qz83xPnu6s4HPsIMJW2z_54yxGGha94skHBznDkg-kMEgu2q0unFRAE91s1TdB8ymAz2PlBDCAjiHJH2F-AKRdQ6tcsBTRVfRIWNGiI_DHSx65GzFm-f0U0EmiyAmikYLjyBsrpCE3O8PJusG62BsJo2PSzQDYrMp_uWKbXgY2rUJqaeuiK-YjSbOhl5JqzNq7p15IzEoXxhm_yhaF6UFK6RRjEmU6FDPboWlh3ncmhxZVBLfPIGXbu0F9CtqbPXhCfys4s7GTUMvDfJsKewA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrdym1lnsXFlpp-BCwRHXrkKfdTiWwqom3ieJ87H_SbhcWdh-JkWaJ6ZoCYla-jEsfxz42jypchtb9lbtoPxPGt_lz4jKuO8aLlxne2lLP89lc6XMRjwYLOBrnIMYNVc5uOx0Is1M7mq5MTtvH7DlTBzHmKihb1tnLjdDlMPQh6_DH73B9Ewz7yEJti2e1xMTG6Ly_Q7z0JdUJgcE-fxLivrc2vSf-CvP8mLZXv-2-j9sQLuZGdDjeFgjmlkHoX886YpjOvXfoeBUIf5imiDgA8iM7DOWHLzW41a30LKCR7KtL69Jx_EZvrc85slPIpiZ2Efrpr53V-I3RDa67uJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApSFE56uKhfNRu2gzno3yYTDJHZTteeiOGiGOsqUjoG-MsQZHVUueqppjn8fKco-cxbVPpuFgJlMvw98ogH2XkAAWM-IXu_IMevxFbygfJbCaDMfaBGJmIPzbZwb7splsJj2t5OFoMYO8eRJF3Cr5Os2gYCsry1TdleOd98gQERXB3Nr1wh5MO-OZWZqNiiD-EobezGzm0F0ws2ATFsNqdEE27TYqBKPX0igJ_z2VFMFsS0vFbHFRt1gbpuX2lYcHzWmvQRU8pmZ4NBcrrd2m92KO5nranlHOZdguqnIQwUfWt87tps91as0OrOpEvtejNTdsyHRFecu8-78PWguvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=BrijKJHrHrJu8Rt2hjt0vLyN6qVLA4kOKwBqNgwhGKDM8zMAe8Pdoy9a7kEV_taDHu9dMbkilSrgaXqzBWqLliF4KrKrNe7yQfEpz62P6eTdSuenzdnzuNr-IosgXFIztFAsOpnk_qhVkiaYyQdOsDUGTVA7Kn6b9a1g902nc1yii35Cg1id2OSocrKiG-4vAp179Q3-mQp1pch4xMjqe6oSwhpTl6zNMo2i94eWN1k3BcbmpuIVLixhjrLWs98XNbd0xNV0tnGsBCN9vHnBdOnEmRZzHstlqRcCraQ8Dn17KEmYUUuLmqq6RfiUBHPlA8ihMOFui3sclV37DHyzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=BrijKJHrHrJu8Rt2hjt0vLyN6qVLA4kOKwBqNgwhGKDM8zMAe8Pdoy9a7kEV_taDHu9dMbkilSrgaXqzBWqLliF4KrKrNe7yQfEpz62P6eTdSuenzdnzuNr-IosgXFIztFAsOpnk_qhVkiaYyQdOsDUGTVA7Kn6b9a1g902nc1yii35Cg1id2OSocrKiG-4vAp179Q3-mQp1pch4xMjqe6oSwhpTl6zNMo2i94eWN1k3BcbmpuIVLixhjrLWs98XNbd0xNV0tnGsBCN9vHnBdOnEmRZzHstlqRcCraQ8Dn17KEmYUUuLmqq6RfiUBHPlA8ihMOFui3sclV37DHyzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR7h6ArLE2Z82CWL0L-45IGTzm0EUHNxM6aP7mlcubJCmY--BGZsgRaroB6FitPuhokIWGBcKGRTaojONiXGK--Y_9m1wKrA8ue-VoxkK8XpwSxL2cBPSMxvXE_Zm1S-bggsV2zl-2s8MEFcMZMuRnH1zxa6U7YPCo98CcLpErpwUZ-LAgv4chP0Rpm8g09BLenod4KaTiIxDyMpwIvhKm9oiCGBrflNc5zgdmD_9pODK4L-9oZsQeaLvxdoDN9bv_3eeoYJd_MsM3TN33-RDKNqO_Ih1As_pGhj573iugAQNz7s0r5lbELgP0Wqt9fanWFmBnnM7HOGx_7gQ6KF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VF1REwig0kX6GvYsiYw1NEkMuLkyUjg_A59b5C_pQIg1VLH_-lnsChi1pgmcTCtQ3Uu8kG7Y64JD3CoEQ5XyW2XLELn5sK3FLiSYGC8b9RrX8YVhWUmWwOILEC0N-21JPbZFTLtktmhnIAdZWxXbvhunL2FRTqkal1qA7_cD4tVDFf-WyYKvmvZFR7Iy7COYkkBOCZvhmHRdMv5wLMEc5iIq1PK80omH1kMpzpBvd_PIk_OZL3RdkKOK9bnd6comgglMutVJ8z8FFHKZ2HuetTa6QqaUXxsOBwyc-k1Gma6pZyrjYpeJXIF6xiPw9pElfykCMWgIPc_AHEm9Q2rr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDT9fBQpI3QnZO3i9kBaeFb-O6aTbDIO_RwwXCu0jEKiPzCuaQcIZOoxi0-wDCAy8_hqMt30x4eKQxSDyETxpwBB7pVZJ8gFxvcxyZ4BYScOgANuekfrUYBLRfHC1SYpxHnDAnXWG-J5jyUWBy6PA1odOTD0LxF-06gpdHKV25z_l2iHiis0zS7KpVCUkB_ts-pztL_qwW7taTX2oj8dwAGBJYuzYHidFJ9IFSCblTiExyuVvuOtOiT6fGpWeCfZnuBoMHQ2Bmevl_RznvLr5we2ULPL7LrBNOqJjpiSMYbyRfzmJUt71E1LY3eXNWF_BjjbYfDL5hVvVWsztE8lsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=srNxzJyCC6bQHBx9GH3bVgjzR0efvwcQLwxAzP9zb77-TJ03QHKWIxt8vOJ9UuNzp_zUIjSWyOgfdypDEpyI3ZmL7wVGquvEFTUYOSvR47c1NF3hE5AbvVFuXxR5QfrpWYxwFmWsZj-CkITyNmpffY5rR6-w13p-XQj1SD38c37Tkat7mhXRYdmqCeHKRyUheOlGJsr-J17HQr8hQhrSpH6IB9AzBsJrUv4WnpTxJ9ZwpO-tKVtwCIOKBGaJ-1vli0h9QVwrTB21MgjamY6qaXhHV7v5wBqUXEp3UZRlXwy5hbJzJWTeJOYISWJbWXk5IGqzPMRgAcVjRIaHJ4Ayfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=srNxzJyCC6bQHBx9GH3bVgjzR0efvwcQLwxAzP9zb77-TJ03QHKWIxt8vOJ9UuNzp_zUIjSWyOgfdypDEpyI3ZmL7wVGquvEFTUYOSvR47c1NF3hE5AbvVFuXxR5QfrpWYxwFmWsZj-CkITyNmpffY5rR6-w13p-XQj1SD38c37Tkat7mhXRYdmqCeHKRyUheOlGJsr-J17HQr8hQhrSpH6IB9AzBsJrUv4WnpTxJ9ZwpO-tKVtwCIOKBGaJ-1vli0h9QVwrTB21MgjamY6qaXhHV7v5wBqUXEp3UZRlXwy5hbJzJWTeJOYISWJbWXk5IGqzPMRgAcVjRIaHJ4Ayfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHjShJTh-HJcFr7Ff8RDi3xfN8E5tWpqg1Nx4cb4WV2rf0phxF3M6aUX7i9F3vrpWwd1jZm7cCWOG6iMrrB-HIp2RRqdQeW_6Ry67EXN6MpbpwFPbslXQYcAsAm_B27dsvF-Hv478a7OuqDkuLz9k3RsBMvKTnDFrJ_DC7RktGNNVEwzKKZiOgRPCfQwu9tKNQu7UqyEN3me_ldpoVa_9Qx1iW8DLnVbISW6A82psVpWRpK3S0beF_oW331CTTqfBMfi47KkGHbk01-bKWdSBVqqPpEWTyNuz-CrtSxrXU554hygtA5XrFyHRb3mqJxl2l-MhmFVQ7SFGgDVg-x5ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=TPZ6Ojy6rAEWFgvuCyLZ-lilMo8aUAMYArIjjPrX3bA9l9I9CmHHa0H2zzg1cVapNGKB0htQWnkzVY-9HZuogUQ35SasS10Y7QfRpESrli0JxSvdC_EAzY93MSfYXtqsx85NJe6xv1D_G17Cvmxcdi9VNf2XI1Fu3Igm8n581NaADDwfVTAzMZSpDBZCTiaXACARM0qduBsGahRGIxDRD2aC4Cw8e1-58EPGEav93ZiSdNmZxvSb2bze1vQXps2xmuRop8KZVgTO3CGYb2UwBU5vm_f_5st_7R34t--yRgE2BAIT3ZfmUEUnGc01hISGxEOjim59iqGqdkL6IEr7WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=TPZ6Ojy6rAEWFgvuCyLZ-lilMo8aUAMYArIjjPrX3bA9l9I9CmHHa0H2zzg1cVapNGKB0htQWnkzVY-9HZuogUQ35SasS10Y7QfRpESrli0JxSvdC_EAzY93MSfYXtqsx85NJe6xv1D_G17Cvmxcdi9VNf2XI1Fu3Igm8n581NaADDwfVTAzMZSpDBZCTiaXACARM0qduBsGahRGIxDRD2aC4Cw8e1-58EPGEav93ZiSdNmZxvSb2bze1vQXps2xmuRop8KZVgTO3CGYb2UwBU5vm_f_5st_7R34t--yRgE2BAIT3ZfmUEUnGc01hISGxEOjim59iqGqdkL6IEr7WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbdrJLaRYWWgViz6K4snwELObXAq8QgIXbADps5EDGk7rmQ-gqIRb5JeA1IyRL0eNNPqltbYFu9woY6qpirpOxQwP-4mSwInJGWp9-rAopPUBM0nJDfn-WAM3oL2L8GgpmBtC4YvUytAfZFyVrdbaxZiuVjfwstIK4U7UdYMUwPf6TMwQ8iyq4f2K6aY6ezfpKhoOz2K5b-9kjs0YUekIkenxDyOE1waXDJi06ZgvCDrbrpRu6EQPZ8jtPj5BQNVjtMpapr3XaJw4G3JucJsRIGj4Bq9m36YASfVVYe3LkFNObGfUXkyY79mkdPKwxONcIOkoO9bRxVXuDRWr3MWPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=A4CN4cx8NtTYiK7At8No6az2sD0HZazgD7J6Cz-uMrT2Tcz-kS7dmz2zm_ZAHvzwyC-uqV58Li5R_PpTPoQAzPMTKJ2A5J6cLEq9T0rLHjCnk5zLDI8E0gEo-71XjxPAtSxTVbcKy61NVfpJRrtTJZulEhfXhxOE2aiHFXtyM0eJsL-IXUOQqLmmPNQw9JhmESLXB2al935gdDsBOGSSaoUIoTv8RWhWJ1VPRhZc-rGMFfgOei9vp3mDqKIvwjE-BX6FAO8NjL-SRYyxhq5pkg8TVDoHibiBVg_o8gFqQDudYL6G40JqhTKTFJdG5UvF7-XJnJSW0Lq5ZPRDIvSRkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=A4CN4cx8NtTYiK7At8No6az2sD0HZazgD7J6Cz-uMrT2Tcz-kS7dmz2zm_ZAHvzwyC-uqV58Li5R_PpTPoQAzPMTKJ2A5J6cLEq9T0rLHjCnk5zLDI8E0gEo-71XjxPAtSxTVbcKy61NVfpJRrtTJZulEhfXhxOE2aiHFXtyM0eJsL-IXUOQqLmmPNQw9JhmESLXB2al935gdDsBOGSSaoUIoTv8RWhWJ1VPRhZc-rGMFfgOei9vp3mDqKIvwjE-BX6FAO8NjL-SRYyxhq5pkg8TVDoHibiBVg_o8gFqQDudYL6G40JqhTKTFJdG5UvF7-XJnJSW0Lq5ZPRDIvSRkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=aGJ_XZy1LivX6eAo9Y6uKAEEOjJxM_zPj925hc4jXHUIaVFGGStSoCNgxsB1nSay8o6p59vckmFTrM9B-dCJc4nq_D7fQVe6mIN6c0XndfL_Popjc1lgcD0rYsgqzsBMjnu-Goj6VMh_uqbagnPcgJIdLytF06XA4DjXqSiAYZ_QG3x3-P2KRyRd0H9xj7VwWDrmxP6_jMZoIb398HEGJ49gijYQ3o7X65rcMeJ5k8yNRpNBFbWtdXQNKm4wkIkqYsNPHnIX9sjsOH2aI_af2kS6hc-0ShCoR0Kv48cei6_DCxHSwaFWTBT2ojxpu2t11fHv6Wp7SpYcIOoIqP0ZWEEKbqMWM0qp8UUvkxnu3x_oWfFFhWo4cBlMFXU6CAztvuTp7zmOcbEYw2U0hBdurJeMV9539d5dwQsfbM-yjaU1o42X4MpYCnkvxjh1pfxA3o375pozQDilStGQ-ZteBgc635kd1-879Iwrsm5AHLA1o31iL-3ZB_iz7iwXXrnpukRv8EqQWwUyNh1J6Ul4cZh4DV9vLjUWw78QMYxKnEvo8F3pa53PGmbO4QbyJRWOpl3PSw8ZX1DM5BRGkMv11amIx0TG_9sexNL-tgDtMdAOgbSEvs-_uWaS3hCmJarfNgIKvWQnrzbV0nmoiCzTj1M5EdV7MdSRhQohKbbwt-U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=aGJ_XZy1LivX6eAo9Y6uKAEEOjJxM_zPj925hc4jXHUIaVFGGStSoCNgxsB1nSay8o6p59vckmFTrM9B-dCJc4nq_D7fQVe6mIN6c0XndfL_Popjc1lgcD0rYsgqzsBMjnu-Goj6VMh_uqbagnPcgJIdLytF06XA4DjXqSiAYZ_QG3x3-P2KRyRd0H9xj7VwWDrmxP6_jMZoIb398HEGJ49gijYQ3o7X65rcMeJ5k8yNRpNBFbWtdXQNKm4wkIkqYsNPHnIX9sjsOH2aI_af2kS6hc-0ShCoR0Kv48cei6_DCxHSwaFWTBT2ojxpu2t11fHv6Wp7SpYcIOoIqP0ZWEEKbqMWM0qp8UUvkxnu3x_oWfFFhWo4cBlMFXU6CAztvuTp7zmOcbEYw2U0hBdurJeMV9539d5dwQsfbM-yjaU1o42X4MpYCnkvxjh1pfxA3o375pozQDilStGQ-ZteBgc635kd1-879Iwrsm5AHLA1o31iL-3ZB_iz7iwXXrnpukRv8EqQWwUyNh1J6Ul4cZh4DV9vLjUWw78QMYxKnEvo8F3pa53PGmbO4QbyJRWOpl3PSw8ZX1DM5BRGkMv11amIx0TG_9sexNL-tgDtMdAOgbSEvs-_uWaS3hCmJarfNgIKvWQnrzbV0nmoiCzTj1M5EdV7MdSRhQohKbbwt-U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiZ3QjN6BTCzqLmuOI3Gqx2BlRklLw_3bNqxCR5HCWLQWb3PKLGlMhuThONV1_F_FC1NS9tNu3LGFCVXf_sONgA8sXT4lXFmKqpNCJzdat9AZEdmyFAdWBR5VJgZLYQBT9ioLn4o9SM6Afcmmrqohkg2TBVRLPjOQTP4RWm3MG60yl-aBylMCXzcmNGyCgaBjwsADItVU14mUmcvqFObqJLHeYba_0P2eTb4HIwHcob2D2qmk2Kre95Ify9dMI4qkRG_DQhQ9NmAGdEcBVhDV-6yaKfLVmt1QYv2L_5pV1XxeEQBLUli6hQ76lmbMy8suHNl_upWC0f-lMZPk49skC2k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiZ3QjN6BTCzqLmuOI3Gqx2BlRklLw_3bNqxCR5HCWLQWb3PKLGlMhuThONV1_F_FC1NS9tNu3LGFCVXf_sONgA8sXT4lXFmKqpNCJzdat9AZEdmyFAdWBR5VJgZLYQBT9ioLn4o9SM6Afcmmrqohkg2TBVRLPjOQTP4RWm3MG60yl-aBylMCXzcmNGyCgaBjwsADItVU14mUmcvqFObqJLHeYba_0P2eTb4HIwHcob2D2qmk2Kre95Ify9dMI4qkRG_DQhQ9NmAGdEcBVhDV-6yaKfLVmt1QYv2L_5pV1XxeEQBLUli6hQ76lmbMy8suHNl_upWC0f-lMZPk49skC2k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQRjgzw3HC03WAdN_LI4zHrn2hVoPmcvkgMjKR2VV3MS3F8gA6ZPIOWC8Yx5k0IlwDRzqQjCyr31x2qKjSpk6qlpv-28MzuCBV58BpBxbuR-cDjk0tKMmS5mehViZPAtjTQFljcuFDs8uZAJxmzWLgzA7vuKuKip0ozfnAVkdkyR6yJhNbNfhppmNgs3mj8Ctyd-6xsXmLLpch3fBUX-hEYLa1YaOKpJ_37jI99wQbN2dVgn-fuRENOra_IdncNZoMykvbVCqf9_B7aNQrcvGZVkD5s4KdXw0zWvtp-KY3zLIqo5Lxil__6qz_RSuOLsffGCsPYJJ7JzEGAgMW2_bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=a-CpPYWzwfgnBvtAockF3GgRDW3VHptAw2POXqUmLkOQ78L-vao0nLZ9Pva0oigsPHm7dbitnOXBg9scNXZgZ9e7oZdeOec_CWrXlHdQHj77fBB3vhEQb4Vw28XxHW3MhmMA38anhIsukGp7kZU2try9QyVo2HkrfTGoUi3AewvQ_Kow3vfWiRvLSrCb72_3THHtczKTxCcNyQrDmOEp8ivxr5Z3vpAEjG1p57PzzG3Tt-lUnEShdU9S9m9VlXQS8t7Sp9g678EKLz1YtW7XqMQdaYlLumOCOgSRN0ET-ctgfSBwW33z02-yT5k6QRt9mC0LSmntvaLZCD3bKxOK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=a-CpPYWzwfgnBvtAockF3GgRDW3VHptAw2POXqUmLkOQ78L-vao0nLZ9Pva0oigsPHm7dbitnOXBg9scNXZgZ9e7oZdeOec_CWrXlHdQHj77fBB3vhEQb4Vw28XxHW3MhmMA38anhIsukGp7kZU2try9QyVo2HkrfTGoUi3AewvQ_Kow3vfWiRvLSrCb72_3THHtczKTxCcNyQrDmOEp8ivxr5Z3vpAEjG1p57PzzG3Tt-lUnEShdU9S9m9VlXQS8t7Sp9g678EKLz1YtW7XqMQdaYlLumOCOgSRN0ET-ctgfSBwW33z02-yT5k6QRt9mC0LSmntvaLZCD3bKxOK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=tncqDXxQxzU61a07tX5g6fMqBmTEC8_LEocPFJ0mNXqLDJbQl0SG6RHBXB2iqPdCCwv6uYIQwYF6PRrUAhYlAOKv5SjPNNeiMnssDmqEA8eHo-Jnmk8DzcukpA0gLzGMNVLFlDqAxLW3FJBPVMo3BD0uqgQH-ZAEuV5wcNeZ3tV-MYXoy6L1nzgm-zFgTqgNfqnMTwzfPr5_zYhm7DBjeb_aLqqu9AftXSNWng7_BDzVke6gtntoGhccTYZ2sQHL42YW5oxSwZMXL7809HZljk7lvUJobDp6Ioeav30SZ_cMhSnoKASgOFCxoD_vEaF0EhkbRl4j5cdKLN7W0VwH1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=tncqDXxQxzU61a07tX5g6fMqBmTEC8_LEocPFJ0mNXqLDJbQl0SG6RHBXB2iqPdCCwv6uYIQwYF6PRrUAhYlAOKv5SjPNNeiMnssDmqEA8eHo-Jnmk8DzcukpA0gLzGMNVLFlDqAxLW3FJBPVMo3BD0uqgQH-ZAEuV5wcNeZ3tV-MYXoy6L1nzgm-zFgTqgNfqnMTwzfPr5_zYhm7DBjeb_aLqqu9AftXSNWng7_BDzVke6gtntoGhccTYZ2sQHL42YW5oxSwZMXL7809HZljk7lvUJobDp6Ioeav30SZ_cMhSnoKASgOFCxoD_vEaF0EhkbRl4j5cdKLN7W0VwH1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=eemjMwGndWb7RVQKo2Dy3XGf4A5h6LD1b25UYZabx8rNwyR96gIlUVBOMoRn88tszmZB655fVIVViC_eO3gsouKMVwlgXtExgoOIPprhlv1cJEZDSDhiDQP_XSCfsgUcpVAy73aspneODmbKZJN501NToMH9-eva9nf5CkE-ftNFSyaID41X6LTKTUlTtN5_XgijXT4Wz1iRrjOlUfjjHDwYMCCQTlixM2dz0Dv_ljtB-o8SgyIFjj8b5qk4jf4rWpr4D8zwGqU0v_zj27z6BNB8ZzkDSg9fxGZ74wsQAT5ydoxDE08pWRiVFmmfIi9UfIfitsmV2FGjlxtM5c6pyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=eemjMwGndWb7RVQKo2Dy3XGf4A5h6LD1b25UYZabx8rNwyR96gIlUVBOMoRn88tszmZB655fVIVViC_eO3gsouKMVwlgXtExgoOIPprhlv1cJEZDSDhiDQP_XSCfsgUcpVAy73aspneODmbKZJN501NToMH9-eva9nf5CkE-ftNFSyaID41X6LTKTUlTtN5_XgijXT4Wz1iRrjOlUfjjHDwYMCCQTlixM2dz0Dv_ljtB-o8SgyIFjj8b5qk4jf4rWpr4D8zwGqU0v_zj27z6BNB8ZzkDSg9fxGZ74wsQAT5ydoxDE08pWRiVFmmfIi9UfIfitsmV2FGjlxtM5c6pyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tf5oOue1iZ8ZByHnyDjqA47xwN-FpkNsDWZAEneLK2JEANn6CVbwUjdKK2P88j5Ef3GdJs_uk3FTFL6Bx-Ga5x4xUcdEq5b0MZFBJIi2t5uHWRDLIwMUxm3YvN7aZq88-e3HvA2FRD7MbenCFsL7niciQIsvHIiR18-fLucxXOkMsBJ7T2OcDicK4YZxoBwG6Eb_sbtJ9O92niQ2GUBtdtoWIrElDo-SHAcwYNsZ7lptJ3ZaN5oiuKCSMvP6W4c_8-iG7oabyZX1QCW1RpANQhvX25kku_qB8CiUo8L5X33q_UKVEFYBsytJekcB0KnJUnMwGxA4pgf0TGaUz8DwkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kX-FaQA1eVaSabXTqEpwEGTag1KJE_oJe0IpxCvqoC3eTIiPrmsEKRmk9B203UbDnV1ciYCnJ2imuWoVciORssN8hsGDl1PJE_KpcwM5M2OJNGNAgneToMFRLIK5v432HPMELBcNZM2vcbdUhV5e5pfBuyvPpInFZmwlsLmhZqJU7XwrlaWbCyHTlKcLmWxAB7dUCGqZx0oUNuyusOtU2rm58snH4A3S_ydeyQVXAffGM0eW7eiwgiUbumea5ffuRfgjo9gbT92jubdsLUvaQQQWS7KeAvYHIAshWiJS0CwSuN_dH2S0JG1d5EoRwqQW3TSZ-4BWXy5GgSvU5xFfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNFfL88g6_DJdHclbR7Q5KbTwcKfLb_IIqpFXkQX-YSXgpPMgksNT696mBQX7FMMYiMJuz4KPZ3WWbe-Il0fnIJmTcJtVfazMeEG23dsHMqjBoGm-uBLCRi1RdYHsfhS4i45lwwtu9c_Xc2s8RL-u07rmdI0N_x5ZrIrlXPYCzi5HSNDmImL-eraBJyMEaRm5Y7sctf42BWA30ABn-0i5yAE7n8y8cVGXIKrlK0Z7mNXWaMBPSpxSnASw-DfXj12R7veckJbFAw56rlGx3l97RdR7ybtdnnJotpychRzlrmbnafT-MVVpx3b2XsQkC7yUkD6dWYO5wk9SJw3UEbf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WnousM5KPo-nZHX91EwQskI924NAT-gFAzRcVIpp5CpUcP3zmvH3uMdXMc5yh7fpApmdo4YwITvfJv-_GqvqM8U6HV3kiGt8pQfdzY6qooea5wdvg8VJbKbtwCtgTUWvC5cZ00-FojERmRqqHuPJI7hZs5fZgd_50Gt0lSvDVB_GYI37k8SuRp-hlTJNBcbr5vzmx-uO0AzSfG1Q_k4855fyGwPtTmo4Bgb8B8e-oTHnCRYE7bYKraPG0SDztrR1cmIUkzob20TKeFqKPGZ_gz3qsgJfmSIpQWdc_2sKku8FI2oHSgwWwCk4_E7WvKmZ67uGlePksaWb46kwXkdkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FcBPDTV2C4W1Iuu49VSZbbDj5T6XkU19mTzET0hnQius5B7GHS-bUEZ7seXBMf-NgJyXdo92N7Za8lpKM_aY4tiYMpZitZHbKAhxjMg1FnlrgDXL8AN6Wwr4yH0r6GaS2i-RqPq6Uu3Tg8LsdLepxSlapu_Xq0bdBuFycrFFx59mADoPOQMSKEAlAB9kl3DWnC_qJvfzP8VBIqEeTrnloxqcjdCIn239vsL3NZmlXQ_k6yvlEYF1h6A0AUimoT0PdoMlPSTiorob1zjWizv2F_Tiu81ggRTIohlJUCAwntpsClUorLp0ZW4juncpDSCZaerx4XZ92RhWYadFtk8aqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkyThGIee6Qs03HMUB0cC-RoQ78n4Dp-rY6mF3UUVib4c1iG3Pvz7K9ipUcp6QPyLnqz202NzgZdSIer6Q28dExFE3uTPSjmYLrPjIcMrHsEwAltKURLjOcQvndZQWs6b2aV6s-QpGJj8v2yKufz8D8W3hH3eyCEM1DbneqL_jjPlctc2j_Mv7R5v3b-lzQ6x1NyFi-kKycjLp2HCM4V35GOaHOuzGiqe2NumgN3jT07zm9ooDNSPWNsSYgyRYnpkcgmLE9E6fF3veVlExyFiXHSFENoqe7A9h29vfEpYF1fndvdfz2M26qEjN8UqRMxwKJF_zbJWxfy-mZEB5RcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ZKqm42RQXsG2ZrnAx3ENng_X1DdXhaLhFQaVcC1OwRNDRL0BSex2JAYw7e6-4gCo1jXCPE3kmegmMyrZAfEi9XbY_rL5Pe7nRYdGsH5AQoxpMhgGV-fyUsosf32lnz7r1XnsiPyOWP9VKv44M7dqEuw6Y5vS1XvT0we6oly1AGFIq2Gssb6vuMftXrx-nn_Ua-4-Nd9QFGBK9FhJctrqjwJVIRo9Y0ljwVI511z8PDfUeehdGd5LCRCoEh1jipRX4CRTCslb12fYhcsY0XgT3XocO-at6knkGFF8kTT5b2_9_U1pGFtfHz1eWprjYMcyQs66-19UR_rn6vi8rrQDSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=ZKqm42RQXsG2ZrnAx3ENng_X1DdXhaLhFQaVcC1OwRNDRL0BSex2JAYw7e6-4gCo1jXCPE3kmegmMyrZAfEi9XbY_rL5Pe7nRYdGsH5AQoxpMhgGV-fyUsosf32lnz7r1XnsiPyOWP9VKv44M7dqEuw6Y5vS1XvT0we6oly1AGFIq2Gssb6vuMftXrx-nn_Ua-4-Nd9QFGBK9FhJctrqjwJVIRo9Y0ljwVI511z8PDfUeehdGd5LCRCoEh1jipRX4CRTCslb12fYhcsY0XgT3XocO-at6knkGFF8kTT5b2_9_U1pGFtfHz1eWprjYMcyQs66-19UR_rn6vi8rrQDSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
