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
<p>@persiana_Soccer • 👥 385K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-24984">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HU-UpIwdF3zcm4e-0CCkxWLcjW9fzpozzt6nPPytcnnmoOHvHYgo5AlRNT0X1P455qB4F-brlIZQ7zbXD16NcwItV8xHsQhmOa586NafcoQYVVGL6AF01OaF5Kd59fn5oghpdib3aHqBw44VLNLMZMYiEKxGjfB6CeORdnny0oeY0PwAzYNj1FJsRjSIlwj3_nW2WNanfI2WioG404T2LOhDWL8Jn_91i0ZvPNhGlsiwi9kcqbWh0irKWeb8QgxFREs1JbCsOpdBwgFjMLBk_KdmtI8bmMRWRdSiBVbGW5L1F-_L7JcSXkwmMee3Gq66GRx4C3YatffJo_Khelz86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.58K · <a href="https://t.me/persiana_Soccer/24984" target="_blank">📅 11:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24983">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdOyIubnmliPcK43sACt5tuo9kKEIHoV60eYK01dPKFgo7xZGTOJdXDQJf6AinUcDnXRXRsRrtbb8_0WLH9MnX0xEjPYPPXx2j3H42yG57z3igWiWfdBuwI8jmvowRZSmUB9ldu2S0r3Si-_vETBTYZvD595JTo4kqHfXzZmQVKbxnGsrXi2dwjqRzxek9ZA-pH1zP6nwzY8MLGBgJPkWDW775-joiPB9y9fzsqwsyCzQn7kSxyyRl3kKNh5XsXHH_FYZ-kMCw3qtrPz7G0r-HqXXWB63ZGaGra3BReCjt2DugfqjjKX0LNUm9YJSSbYXkGWrgtWoAiAcjV_-gYxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛ فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/24983" target="_blank">📅 10:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24982">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpYQpd4Z_h17HwGgm_vlZA32y2HSG7MaWnpA8sjDvLLR_y7v1aOhiL1lH8iBWF6aZ2b3kb8Wd7QxnUZHAjN3-flgcNLyN8ajH3m6fnCmbHE5IfT8s9kfvlgqazmArEoO1f7R5ZFt9dKOYllxDFTQWa9P6V0_U6LHmgTjw1rYlXq7TrSiO5s5kyilK-7UBZGHSMaXRSmLydmhcl2rK8ffaQEKeHSyC7K2oHlAA3D9KMxDCK8EmHZIczHh2bYYCYLajeE8MwM87oAc5ZQaYttyg7wRp3Mafl_nJQpK8QQIP13o_mPPnwEl5o4WM-EqGSezz7kk_GoAapmh8xINTbtSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌داستان: امباپه‌‌کم‌عقل؛ رابطه‌ی کیلیان امپابه ستاره فرانسوی رئال مادرید با دوست دخترش، استر اکسپوزیتو باروشدن‌خیانت امباپه‌ کم عقل تموم شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24982" target="_blank">📅 09:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24981">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRmdm1uPOM5rRHkWowlWNvGnoTD80oIouWTsY-quLyCdpJ4NcA5U6L7asBVftCtnJ3-a5xTJCT4xkXnqv0BysnYiZKy11xguhBBaeiUt26eBcxslaIILx0GgudK1MbIHRuiitw9xOrMuLMMF1BgceAmxS1KAOs29Cz1AABJwTpLJMxty3umVSb0ThUBqFAPRn1KDAmL6EWs69mGTE7Ynu8g81jLI766_fe9wzCd5tWM7skCRL9XcCOhKV8awpeNfICLbdS-B5KdmDmJTp6crWXeMubQopOij0eWihbLW_jdK3niISWgvwn5E6HGlEZSoV4M5E00A8RkXpUNgMCkOBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌دهوک‌عراق به درخواست یحیی گل محمدی؛ با سینا اسدبیگی، حامد لک و محمدرضا سلیمانی سه بازیکن فصل گذشته فولاد وارد مذاکره شده‌اند تا درصورت توافقات نهایی این سه بازیکن با تجربه فصل آینده در لیگ برتر عراق به میدان بروند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/24981" target="_blank">📅 09:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24980">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=VsMNtbhzoMTUAFAo6f5xTPHNkan4UNq3ipb54mxidB8wD186GSK_eS-hfHEA53n8jlj13rLNv59lXdeoNjKh88R9jGAkmnsCE6alrWD1J7hpwLIytqRGQbaxa98vEW0Y_gbED0G_egdgT8KXnUWQnai4fnCi5nwdzj1Ysp39mjIJpC2qJz1iSKfjXKcG4IiIkq3dw5Xinr2QDfN9QoUh3ps9u077ABAXCZVrOSOju9RQzDBFUh9DCaOGgPPiLe0gCEpHJZDEE4gSp206GllQ2cCWN1BeDqP4kNXmPHXdUVtRB6AzT9Pnb8HqCwiHplh3jcfPpY1MaGnNoBVJUPf9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مهدی تارتار به‌حدی برای نشستن روی نیمکت باشگاه پرسپولیس ذوق داره که به پیمان حدادی گفته خودش مبلغ 20 میلیارد تومان به گل گهر سیرجان پرداخت میکنه و قرارداد دو ساله خود را با پرسپولیس امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/persiana_Soccer/24980" target="_blank">📅 09:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24979">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDRrnCg7pM0S7HmdHX1Ul8Dd4bnCIEOQ8Q8CqGgVwg0-UGbajiqxXeXUnW_PTVo_ii_A96VeI8FBEPkGWgibYL0XruUfrHEWRvaWMwdyQynnbdSbaVxmvoBdCt5-3uS40ZAUd5vDAjEmDEHjPRONYN6BO3ntjQPfWMn-kjm8hnk7gOVSpeLMUXFZXLph-YugBX53zIRDc1O18MoRz_54EBPXau9CWnJ7KIx6_aDUdLIcJPW7zbKbKM_il9lV5SFMFmLJvSKvIIVYLb9RCyZJYWcYSnZaRkfawO3qdiwQKEJljfcsB579rtiW_nnsI6RmSnOAyxQJJfFZvGa-C1oq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گائل کاکوتا هافبک‌تهاجمی‌سابق‌چلسی و استقلال در سن 35 سالگی از دنیای فوتبال خداحافطی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24979" target="_blank">📅 08:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24978">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24978" target="_blank">📅 07:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24977">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHHxO5KBnvtJSNWhwAC_8Lta3NoUuuqk0ICkK1KTBTcj5Dov5v1WT3Q8Hj5bAEV7fZhGM7GwL8aBCc_T86_t8gF6nwb8yv9KjUxYk_XKQ4K02bee_O7J7yxqfIaKTx-j2bxZePKdBd-TWIaQTJCz3cXcBZVZTsWiln8W4dly9I8i2xgbRv-iJFT1AzM37uqpVhByHXI_ps7RVCOFuArFI7H90IBRHhvramMMUe95m5tAqhaYlrIbx7PSGWcSHkmTnEq_z67mM3tY26r2ii5eBvs4l-a2qN8Bvgj8H2HfOn0QeA-gIfQenkDLGEZAtwUvUBFIHHUmV-P2J29FFv84sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌مرحله‌حذفی جام‌جهانی2026؛
فرانسه و مراکش در یک چهارم مقابل هم قرار میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/24977" target="_blank">📅 07:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24976">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24976" target="_blank">📅 00:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24974">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fs0cpzgNs6BwDOPPznL5uOQj2SHuSfFVme6fA5Lc_QmMe3UKV6rtmroMOMKFCDvKS-iwSNa-Z_FR729-IZBBJJIU9146vvlEGes1CMTLaZ0ooJ36kF0MLeBlAJWJ574IMiWozVg1lXbmeGjKR-OumT511hHfE6aR7cL-HwPWxj5jKqTCiDRtMR2_rUSq8AHi79_zyWClBbUXoxUYmdLFEK-B8Or00bFwrDNvzq3ehq-ENWCSa_ojbZEQf7tUtKcfLqwd8J2cKCG1qJVgUWUjVAM2UtyUhznSBTwb0GDR21R77oX0qHk6OAsduzDogEScOTwH3C50-c_zE9pdHfz2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ گزینه دوم باشگاه پرسپولیس برای سکان هدایت سرخ پوشان مهدی مهدوی کیا اسطوره سرخ پوشانه که مدیریت باشگاه پیشنهادی سه ساله با دو دستیار خارجی به ایشان داده است. مهدی مهدوی‌کیا از مدیریت بانک شهر حدود یک هفته زمان خواسته تا پاسخ بدهد.…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24974" target="_blank">📅 00:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24973">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vO5yBqTVBE2sm20Gn2dHqnv7TIdzpYHLOYlknWz869D-_CAnyMG2ptkbvEpkZXRBNz8X5WL-aNYPGksOc_ywjvaOhhMcS5YVE_pBSOtcyVEq6pLH5R8ailGmBGSVII0KWQ33i3trdpMC57V811BW1IZQdnbQCjaOq5tD0ex1_nukJHQdLhxnEC6lnVdLK6T9BQbPokCBqjv14-cV7ERuXNN13CTCTBv2uEEahWq4a7RAo4qolZxdf32pqNmIHPjN0VGwf7taeFNXbYpZvBZ146tgNmyLA5xBF4F3aqYIP2eLyBvc2xnUh33z8wneRjrocXTzWVpQ3WUft03E7VbgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارها‌ی‌‌ امروز؛
از مصاف فرانسوی‌ها با پاراگوئه تا نبرد تماشایی سلسائو برابر یاران هالند
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24973" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24972">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdMH_NIDsspAZrlQy8RerpBR-Cl6HqA6-e-Z1IYFMUHKJKfiTZKKvgMJjTAO9Qx4wqEiQlDZeZJEIEBTHz6Z8yChtDF8Jwjx7D2NSyfj73XmPeOSOdhcTPvVq58vB94Ov7cFRJKUlqAgpDbPn0Ld3CLUr4L8uzbb-V6qrRBJwq8NVlqcRQD89W41iKrlV032j9mBn7mLG6Y1Qn0DTWZp9FqFijr_Ac8oiragTeWaEwc7YMTC_rHHgKi2_9zu3KyJHjwZdxZpsTB1ArJuEJFQpXAZRDc_qiEACAwWAdQ-YHA4flmix7uRSl9prLkAdvhrPQFH47WS6f54LDGU7TaaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود دشوار و نفس گیر یاران لیونل مسی در دیداری تماشایی مقابل کیپ‌ ورد و برد قاطعانه مراکشی‌ها برابر کانادا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24972" target="_blank">📅 00:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24969">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNqgkvMUhul15PXaRNTNu_AvJPBfuEcXEVMZeAAQH_gie1If4LUdhwH5dB3eZWzsrrDLEwk-kRsggZYaNV_8wJTfj7U1XYTjEgE3SPUOv2M84-CIMYxWDtsjGKps5B5Wlhuzy77nzCkMvoy0kx9d8cy9hP1PHY2ZjxbyfNMSejMlLvVTT2pGonf1LBsjX8_x9QONvPqlA4Wb8SvXfxqw6-6213XEFa5-XfpOqNSxVTsWBHmwBA-fKh_HnF-0pd7gaLWJzsQig3EjTjcNFSefUqMGEmcqVb_9TdoZ_fQe9T2u9jlrQ8-mzgM7Q0CLjnZY8CdPPxsvQ5HGGjN5Y7BaNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الاهلی عربستان؛
ریاض محرز ستاره 35 ساله تیم‌ملی الجزایر از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24969" target="_blank">📅 00:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24968">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDL0LB70NJOFzaXs0iIy36eAE8QqsaQSvkL2adBqt24Ei3OF1Sk6bR7ObbDGcteAr8jsfIu6HbcajcopxfsnRXIpZ1y2BZ-ihqAcp55Uu8B8pkXOz6_zwtUvJ5aMg3bzXPbGhdLUFIANLqps4i8af_d52Ru1D79-qPbtyD05tL1eloGFSvGWxGZ3YkMI12kgrUuXp3SghpCSzjGvxySEd7txWF2kFGyY-npVyYGrFe01MjfoZw6HmkzRVHxN-DCD1ABDVbbJzEyLoJEh5y45VSi_Uti6knFEyTTvATkgyMgLwebFXt2OBMt3LZskWFfCbAzr5GZxc-oGl_OWBIh0cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24968" target="_blank">📅 00:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24966">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQbPyBUYqaCsvFw390eV1aIVkLiSzXVTPtuOAJV4DUtWbzSKKT3kbbJgx0aoTUtLF3_hHWu3J64FgU148YkUAEdWCkvGGKFDysmsyClnjq7BDvTVXr3HvDvOROcRTcZkY7JW9lAOGQ5v_NxuGqIYRy89guX8xgku_D8UvB2nD_Sn8onVdyI2TDU2Yx3pXHWD2oi6RnIsKAneCXs_iJSQ5UY8P5K-J0YlJWoPAjzuvuBYYZtnKpfq3qi8Bn10qFHWqZkJ_kKJpYr1Z7F4QikA21L0ohJDTgbXtaR-0Xn1yZC2mKru9R2EuTIGCqwEhKH-pGgzkAE8H7PmGb7qMKjVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه گلگهر سیرجان که اخیرا قرارداد مهدی تارتار رو تمدید کرد بندی در قراردادش گنجانده شده درصورتیکه باشگاه پرسپولیس این سرمربی رو بخواهد با پرداخت 20 میلیارد تومان رضایت نامه تارتار صادر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24966" target="_blank">📅 00:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24965">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pnlm3DCZgq-QU8dSTinAKWwZ3XRK3gKieW7Foau9i2bFK4SkkaLeIjPB8HHfh1tsolHmecAKot7Pwn4k62NozMxdfkZHG4y2YyEocvP2v_zvhvtUAiNhR2pM731rrJRTMrPzBnmueWlf4XkzYmoB9wT_QouFTwDbeoMac0RrE3RoH_-CXMMg589GzeK1HYyf5qj168oUXsOzar2z4AoRFxCSYasRQ-CRfOmetrY3vUOGmq1YCjzLzaHdYMYtO0ecAXAri2ysO2m5r7OmNCSE8GKZanKa42CSQaK6wngWB_f5mQwHfaVlSDGtFU2OysaSVYPgLY0KRxFoPpM-9YysMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24965" target="_blank">📅 23:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24964">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCqVlt5rACVvAvD4oozXQyYb0x1SB4r148h2_KQMMPepYe0q8oGeARe11pQE1jAnMEG0rXts2bSEhZJiXS78kCOCw0m1t1ju8A3wPoYvcw9mUvJYlySUdW6zVj0MwfosrtjL89-MbV0NmxGuTHcjnFosjr772bxElo32-yWaF-7cKMiVy7kBW-pfRRzWNmCDaOJrcBUUpXkaD7g7z-StLuDfVMYcAiIJk5ePeXJFJbClzdO4UOBaFMdDsZdoxqwTFSEepWARNnXlPhEGHue_UxKO9hnW4VlX1G18gb1xr_hK-aN3oe4dbAE8obd4l3yUpmi8gG6VzM-wliucFIiC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
💰
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس با ارسال نامه‌ای به باشگاه نساجی رسما خواستار جذب دانیال‌ایری مدافع‌ملی پوش 21 ساله این‌باشگاه‌شده‌است. سرخپوشان به مدیریت نساجی اعلام کرده که 90 میلیارد زیاده و تا 55 میلیارد ما حاضریم برای رضایت نامه ایری هزینه…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24964" target="_blank">📅 23:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24963">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBcKyuu4zBK59MLdfUOCITTuAOZoYQ0y84bbG5af_Smy8t4Aj1swZeYJPYuQOGdMyCxmKRT09TIOugGVS45rEhxvxF4UJRCkkElCfIzbZF8uaP5RtyIkfShBj1LA3j6j-d7RLV3jXLtKT0N70lXmz603Ogn3ytCXQHGT6V33R9zX2b8Lwx3eqjVT6Q4Nsv-rEXZK1A3ZJ7cL3x03QimH5WrbFXVT7pXGRTGwgv8uktQbzzi1QPKIAtju6i-AT3rttLi3G046UKUrEoTlsSUinEaNvn8xmU4y4xZTmkwzkxrnCizMfc8FRu7VVQCuTCvgVMGB1jwUmhr2yY_CpUk32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
در بازی شب گذشته؛ این هوادار آرژانتین کیتش رو میندازه برا لیساندرو مارتینز که براش امضا کنه، مارتینز هم کیت رو برمیداره و با خودش میبره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24963" target="_blank">📅 22:52 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24962">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24962" target="_blank">📅 22:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24961">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akvAmE3H-pdfeyY_1LhIbg7QDxDmMZ2riunh7LfzDz1qu3fWxvTnToRxQgylN1WS5oa8YMbS1MrhGkomezXKgZq2DYmrd8kvzuCVZoN2CInL6VKNXyptAPDEOR1CB2F6IwCtz1R2HkxkVYCM0CnKHnyjXNPCg0OCwFwLPUP1l4EcFZ9tfeXObtuDaOyI3pLYmiQe8WZwGbn-KK2q6SC1pW3r3sLqbgEWkF1bVGAWZEWmJKndM4txwi5I8CJrWHiakdMKEGoJVxn3A3CBfq-uK7rJm07haRjfl8VkMWItuyP0fGVwGuq2nDFP71X3gIxAIvlNTY7F0qHFf7YpwEofLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24961" target="_blank">📅 22:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24960">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCBLRZt8NZhnfrxj1bao49SdsmDSuCtXyjWQAtYPDVMAD0TfnFDtLnml-IEUnFVUM1D-lLYOur0wGoh0ekcnvvEaZ2G2l8oF2MGHbCoBQTSRxkGIIdHtmRTHqg9AoHtG4odME1YNkH7bV3utN0gLU8UR32ZtjYLhV_AT3U3F850Kh5D4tSW2PKoMo7lQ7tN95DFvO_Y7Mze_dqVjICXqnsCr34UK8UT1lHOWxMSq7CjHELwTRU9sm6B33zjvuDT_ICnezcr3BrSZIOOkfuakJKhXgSRPCedqn5WXDaRHgrB2n6_997m-gqyT0z_wS1kYyjcUhm7KC6U7_5mE1z-T3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروه رنار سرمربی مراکشی تونس بعد از دوباره از عقد قراردادش از این تیم جداشد و در حال حاضر سرمربی آزاد بشمار می‌آید. کاش بشه ایران آوردش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24960" target="_blank">📅 21:56 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24959">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SOT3PEnKf11SOXOE7aWKqo37ZPSyFDkgLRPS5Iz3QHfHsN6TTHuegL5eNFEVfzoSCwn6QEQTOec_13I7PzX4TcjUs_wSkQB5uaIuSq0QOqF-brgDWoxq1-iibvI6YAxTuvazMHZCu0Vu_6ME2MdPuu2kZuzmt_7_5-9VsBoc7iHd8Ez59C-iO8r9HWHjC0xQrJZ_QZavZvYx5NgXNf9-gksCmTJjMqi3qTFo29OaoDVFH_nFT7WHHxawRuYoDtX8_hpJfzAottMcqixJRyWTbRhWiByhZUgcwJ3dbCDHvH5KDEEd4I7AsPI6N73mJhAQSqDQg_Zm1qKCmDkH1t6Fnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇮🇹
🇧🇷
بااعلام رسانه‌های برزیلی؛
کارلو آنجلوتی تصمیم گرفته بجای پاکتا مصدوم نیمار جونیور رو در بازی‌فرداشب‌مقابل نروژ فیکس کنه. نیمار در تمرینات روزهای اخیر با انگیزه بسیار بالایی حضور داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24959" target="_blank">📅 21:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24958">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b83yXRAY30HV66FGWv_qtGw9hTdjcCd9IskvrY2OXc7KkpGg7sCm8evvbCNYqm5Fg1zfEtiL9dNpXzWY0ZNs8qA8mFzkcic35D9moWNFNkbtq_Qbwm9U27j841fnLSYX9bUF-sHtwBTgF-MvyBXN2Wlsbc5VUNP_2qfRCjmXUD1aFyZPLV5n7kOkeC-TqwblMPJuBFoSpGFkfbphaJEPWzJm88fzHgacVnvL1WtVHRXtOPgPMPm71UkbLzembMAOnk9UBjiP-A2hcgjvs59Tj2uPr1myZlKjVSR7DBxwA5R5eNfW6TQIR-l4nlIkS-ghMaYoVeP73skTLpjFzLTalQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
منیر الحدادی ستاره مراکشی استقلال امشب در تماس علی‌ تاجرنیا رئیس‌هیات مدیره استقلال اعلام کرده تا روز شنبه با خانواده‌اش به تهران باز خواهد گشت و به تمرینات آبی ها اضافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24958" target="_blank">📅 20:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24957">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkBPWZnXHgd9-jsilGZNh56uW9gIDXnK0Bf7ZypaqY3mWhKAPyyMupLVaDGCNpGpqUCgN0mj145eLw6tCiIXYq0UPoQGc2AVRKgyy3lPJRDNpK1h6bqmw4XCTd_eD-1NCgSH_Y6D-eF02u1k2PzI67roup_USA6azr36E236QcqvArVbEaIhPuLkct0mRpKFR_XZFK_RHIz-HeUCTf8TkKfRAn0hXm9DbUfjwydYHBAZ8f1O-X5ICCJ_v31GlhhTM2664xnigyZjNYvTjk7pG7vvab-rGfr-75o9m4FV9BCUFeSV-j7F4u7j7cs711KZgnv_L3NhRyUL8trK9nf8Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24957" target="_blank">📅 19:36 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24956">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUHDU-qVb8ONRU4KmdpaLKx6G6Bqbl4KYgsq24ScWvjO5ocHBxpNP-VcFFB3OnKk-8SiLGEXFpCTHiIc8IniCg2LVLvLbxw0NDfRnywbrRJy1i1F0fIpvQF6MHFLI8zucHp1Ybjb3aIdfJgvKGITeDOeVOr-7mAaHnZHXUPepnuQ1Ex-rwqd2l9Ln8XJnPnMQD8yM0yx7dKNKnLAZwW36gdJ0TkxyYu8ijycxBjVBNKhsaQxXmvPNbrLeTN4gX3vW9C9UplPTt_EIqTD19axwAZtXtvyRhwXXo4c-u_gRvNNnQy9xf3VEesx6QMTNcl1ikeIgIpYO4B2lWZMsPYNwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گلزنان برتر جام‌جهانی در پایان مرحله یک شانزدهم این‌مسابقات؛ لئو مسی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24956" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24955">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‼️
خودزنی‌خداداد‌عزیزی روی برنامه زنده جام جهانی از دست جواد خیابانی ؛ میگه اگه زنوزی اینجا نمیبود همین‌الان برنامه رو ترک میکردم و به ارواح خاک پدرم دیگر به‌برنامه برنمیگشتم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24955" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24954">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24954" target="_blank">📅 19:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24953">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S00h6jPYYWVmIWOzv5obzvbcyUho_c9Cblle3HNea31HgPN--8Z_Ca663-QKTSCBX7qnaDdccsSdVq76_iCe7_SRTUUYLMZcIkPO00hDGbY5sORh6hMENJ9fp0sUwKsEJurBs5Z-OFg9QpgWkvdC6NHtcBqQ1Fy9ES3T97L_YR5bLMfO7rRpsK6qYFWROU6-16teyj8zs35Mal6thXhdH93kQMsXyUuKZa_jP1iJ_9tEf6Ks137aXuE-aqvHcR6o9Ncpj-W70MPVOhSeleiWSlJXzVweNjr7z3_xT46mXdSDzeojLf8fqDjnVpvertKZhf8iLZ0pLzBBQ32BrQ5chQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24953" target="_blank">📅 18:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24952">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3jYE9xWhRDkcvGL2nG0gRVht7C_EU3chDj3u0deK5LIQZRZoCQpXIrXxgD-vD8k0mgSz4pCKSBnVDi-e9zyRuVj0o4WqsjGfzGR-Z5x-rvet2HuAIEmBKeqeL0NlooSrRhjE3q2gpYBbMIy-TSii6TyGbSZ4fDToHZ7saR8aNrGf1fViAMWh_G9ddACsXmmtOVwfFuuTn_OnaKln2GW_ipEAe9k0jdgIuMXk8vrKh82fGsHQIv6GQK7LKhY99OwBXGuAger_tSaEmfof2S4iWyUZvcynytKhPC3RYvlBJMiRwlNNRChgGsMR7KglDILn3i5XcUWvLDcgnrc8YRR0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24952" target="_blank">📅 18:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24951">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hwn-w0f_Gz5lBtNFKc4qrTTwLy-GZQKpcFr7nKwWd274U1Z4O7VIILtHAbno5wP762Cb4nIm6W1yUbATt0prmFQ7Kuj0YfsUgoAjVLs2PGrkuPjtty3hu0ZIfS7airQoVWNegFUWqzQmWKAszow47SLxg59VOty7uw9aJ4FR0XpMynT15tbLlrTfbTOPh81EApp9GC80sAUZiZIb60WRIUV71mcYzJw2VombpzO_3jtkMln5jlFKMXTqXe-f2uwFF-ZaMhxSGW0Z924PIRJdbNY5bV3l3V4Ui56P3jBlXPncEthzoVSm0Y77AYM8E48rbfE1UL9iKg_Fjnzt0cKAbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا
؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24951" target="_blank">📅 17:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24950">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHKA0HM4ClaVBPKchLy1824XCLGKsqdT4ScOUF9kb-v2i5MpQrnqVkUg4Jsdq4a4Q_E1Uo35s8GTYYVB-Cqn_O4xaiIsEanWRyQPzxL6I3-mfhgUHOzJFI2U1HnZusj-y-aOZnd389pmmBma9FsO9cwETsRLbl_9AcuN8k5XASKG8HwB0OjlY_KnUq5gtbH-yTv5ae_UbvWqu0TDTrpvLvfIFH-kxnCHJXgv-k-reoQmR-5s7bMS8GutxugumiGxwVAxQpDQP8ipLXxYaq9StngS-DHtMOJrDb_mN6H9BgNAPXgYNlxASlukbuJSQM15uQnBwcj-V0-TkOzvJmyjtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه‌پرسپولیس‌دوگزینه‌داخلی برای سکان هدایت سرخ‌ ها در فصل جدید مدنظر داره که سعی میکنیم اطلاعات دقیق و کامل درباره این دو گزینه بدست بیاریم و امشب یا فردا شب بهش بپردازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24950" target="_blank">📅 17:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24949">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxRy2aWfiosgiC0Ea6pJaUOH1z1vddU0yNvUSPNTeWOh_gdiiYDdljrekMbcwWTYkAJUwwo5If1cDI47g8f5ZrWvuC3AaWfTAEtSsqqXqCMLfSsOA5lf57JRUeZmOhW9CM9Io8ZaETniH996dsGieyFw-AigWSil1bvln5TBgZqQhvKFHcDKwZoWOhbtWF_xwDMZIG0nQF8tbPILIvojJykLKn43kzNUrKgJkK8lok7I-4KxD1NVB5uUk6TQpF7O5oOPNnBTP7hBq7-PG4xPss5yldD5_VIix7Glq2mnYmZXmTmNZTvRcFyszLbs582Y03eayPIxKHc-CXrwu74CXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وزینیا ۴۰ ساله در جام‌جهانی ۲۰۲۶: ‏۴ بازی، ‏۲۳ شوت مهارشده،۱۸سیو، ‏۷۸.۳٪ درصد سیو؛ مردی که ۲۵ سالگی وارد فوتبال شد و از رانندگی اتوبوس و برقکاری رسید بدرخشش مقابل‌آرژانتین و اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24949" target="_blank">📅 17:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24948">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZi0O_3UydGnl4WXyRMGHNQFokY3StAk4o8btMyRSwfRPLhxu46enAA1OFkzZLWK2BxTrDSZkd1NoLx3XvKzl7maEdd02MWtD_Vc5heUJB8H6SPfJG6L_KZJJUlxKzWjjbXdyj7-86gwi0H9lZdmQTdpiWQU7g14RKEfS8ckMEJfmKOocIUcEjhEeP1J-ntXvK8n9Sl4zeBFnJVLaKsJZsUFcLgZBchfJO8t9GBCdNVkxWJN8jyvo_tSQ2y3AY1DcBrfjsNkiPw7dqGR5xZ_o41lSOSvvj5QBfjNbxXxT06ApA7DOS836jhHo4SkqGzMV6GKcZCg1K0oqBRqcAoPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
15 تا سیو مقابل ستارگان اسپانیا و آرژانتین در جام جهانی سرنوشت یک بازیکن 40 ساله که تا قبل از جام جهانی تنها 50 هزار فالور داشت رو تغییر داد و به رکورد خارق العاده 20 میلیون فالور رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24948" target="_blank">📅 16:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24946">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOV1nlr54NAOeiHiaC1rdBwL8vhc8Mlx-ZEckWtqFgtQb9sBR0odf1KiehcaJcTNQol44b8FrutN0C5C3prHhhIU81-xjNf0E8HK0flWZY9r_iMI3zKNF3PbR1JJfz9MQOy13cdNNK-N7lgz6Zknuxj0Chyk5bi-YVxcGvxcopmkmusA30jHY6UZtZWZ3-au3_FAk3xGPwL5-Tkb81KhDxuRBrDnf9Ul3jebAf5Gbx_-6CW8S5NNBZnOuX3JG3GoAaaWHmDmwuVcs09gy1elCNd6q6daTgrf_iy6TiCYbS3ASrXhS86hpg_yBrv7JjBfNZC4-zIIp5UbkT9soDkjWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ShyNF8bK-m70lRZtGZz1ynNeZoCDA31m9E6vb_OVrcpvnBLk2Ns_s0J04mrww11cbSsFMiFZKulTF6oGhNgNbBdr__nTa7pjTV8R0uQ_n4PmK1hW8OgAHshA-wbzcxRteJfoaDe_UQa3cOtCpGN7OCkfEbtBf2Q76XoZOLFc7ONdWw6Dp_H6P8gW_mAPU3b2885Q-lBcfdqzGoNhPdvHmXoRERxxhib_GU5URZzo8Cp3Wag2bEV5XkVgfZmL6C3RgOilYcK3BsgJU-4raVA2qHIEyOknvh2PYKZgiDAIU9ZsrFzhSqn4v0EXZDy7P2q-EqMZN60y-y9IH75Dcagi1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24946" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24945">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHbk0V7_bBGIxrJFq9xAtsDsZyLzxD9qL05Z6hBNgetJDqBaCrF82ZG7E_gPOuvh_rtp9I7ea6NURYw1-JEOLOPlQyuIVrvs10cxXjySN903rPFgoGsOz2dXAvBwAfqP3VXTEfclc8bfC6S2aehd4OxZyU8egCY2E0T8w2nZklUMet5v1_ssSBRjEXZ_JDrP3C8XTDyy2E8gMEJSqTYo5aF6_Ahmv9RiDAxY8UOUsrY2xFossIsWxAK5TyknaBFqoUJ1OOwD-VMgO8ApoclATlMtTvt2jAQNnCh5Vj7xg8WbahGwXWuVAWIK0gZ7vQvicJjqPichCegU0Zet5kRNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مقایسه تعداد گل‌های لیونل مسی با پیراهن تیم‌ملی آرژانتین در دو جام جهانی 2022 و 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24945" target="_blank">📅 16:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24944">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6umfEEuCemEuDYKi27LcNS5RIvMbLxyJGGqR4tK0sYhvRIvNAUSXGjhzQ_m1WwU6FF_2HIdDTARUn_0PLajJAFKRvCMgw11zwe3v1yzptpGm0T3uSXOgh5bGpt3VKsLeTnOucQWQS56710i9s9yGhsV1_OukrAIVrvtcLrgAmAZYK0tYk4J6CDLA2Ii4qum5_JeVRv3l-tk7IxSsgFhi_9xGgjn6FFi8BcMKHVjqkQztt8OAARQUFKT_Y3VDygVU5N8fWRupHAFMmR5Q0J7oJYFkYkC3uWBFgMQJbd9zl5CZQEtEjaUM5Gws4uwSaU48aNQ9-rbpkXeennpGgr4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24944" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24942">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC_MFDO1_WNolpQ2oXRfA4DnwOr2LtMQy1olDxvGmuQP0UKzxJcPMy1SdUntBHhOZg6bL5bwb2kGC4Y71hRKfw2aQwXLJGePG-aBFu6ppLWIpGHvPbKlTCkKl9HrdG9wY0NYVqlXuDkdedycZo4pfjCHo9Vz96sddIH67wlZSLrt3OSkOzQIi9gjeS2vyI1sFROF3k78mVRN8VE94l37ImHArtOeKLRK1_vVxmNkacTyThPEuGavukCOzwGzQI4kGVMVMkVorLWI1SZRMj32WVR0srAiwF3ZMHigJc0W2p159FEMTXQSToucRHOcz_9KaHj1LRj84MmN5sEBY239kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
#نقل‌وانتقالات
|امیرحسین جلالی‌وند وینگر جوان فصل گذشته باشگاه استقلال خوزستان با عقد قراردادی به‌مدت ۳ فصل به باشگاه سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24942" target="_blank">📅 15:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24941">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW4-kBWttoWsNCy5nm8Eqc-kM7a9Uq-eGuRnnwr11VYhdtXhTOZf2f4uzcuFEOrNcdIfIk-_ZT2bKYq-ZvF9u19G1BoYdu7WHXA_vn25X0mW1a-mJxPcehVO4ATXVdydDB-IfzN1ESFIpbeqi_24cJvU7a4k89C-JMJ8YHJl-7NsSnqMD1I_EI2ARM6Z0KsHPZT4F4hFzKzvFf_rMIAOaAIybxp1p1gtipGEko7vtn8QPjqfvSGCd6AGVceJTmtIVN_Lh6GfUqz-QiiDEnfXWmag7MY7x4pdJEZBpl69ualpiyZ1Up85AIB4B42CwvyL0X2EXxqY3zA2nN13zePskg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مقایسه تیم های حاضر در ⅛ جام جهانی 2026 با تیم های حاضر در ⅛ نهایی جام جهانی 2022
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24941" target="_blank">📅 15:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24940">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fngO9RN-IsQcQ2tiEuJ6xb-qTf5IpP4VwVZyZXnmAfNpcfFqhxyxBljJ7WDyBmSpSdKFuQfDZlmQfHKZLOuG6DmyTVabL1UyunI3-Tz3MBxPM87Sy6_K4dYwK2DZmHecJxkB3rRLfmAMGjlOA95-k55QyGx5Nj2ukN3ALUVV7BtJjBHf9-rsb8vUXR3eX2my87JzUJt8ufd84fH24taw0d8Ru46Dyr6aqodlhCAUDO7bOpWPJ-DnIkMATaMaFw3RuJiU7UYm4Io185JnyZDCYMAAXuM5FyWV2q_ZFZ1UuFJXxk2AyzXeaB660zbHeUCgfOcUtYyFglwl94KO5SRCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
همه از عملکرد نه چندان درخشان بازیکنان تیم بارسلونا تو تیم‌ملی‌درجام‌جهانی2026 حرف میزنن ولی کسی از این حرف نمیزنه که این نبوغ فلیک رو نشون میده که با این بازیکنان تو دو سال اخیر ۵ تا جام‌برده و تو سال اولشم تا نیمه نهایی چمپ رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24940" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24939">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BScMlZE9GpCIjQcPgHyRPRXQdxBkiBcHssYb3DTr9U1E6Ra8-BsjKLLDqgZ5_z6NHU4SXB5RCx_p2fai-eESxA3vQHmli8f-enpWnkOoG4AzFKNbTW1oUYQukXy6JT9N7fK0MpUc7wqj-KzEIofBUEn458VPJvYXCw8O_psok5lw4BsWn9Bc_IrnDuxZCZORo1xy3qQuR3G2D1DWGY4wEVHwC1kJ1u118w9rrsbPbzAlIceYmDfaJWdg4rPl-mavyP2fCxZLwKyl0kaC_A4g8L-h6J7mkF8yve-J9Abef2qMhsCkQGGvN5oXB23xDUq8pOnod2vJn-jMVe5XWJNnBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛ لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24939" target="_blank">📅 14:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/snUjs1dhureCkVLdLUg_zvrBos7Qn_GY9Hhq4K46KCa88Z-kIICZuaN69uZRY-vKqbihqHgsJvWDqg4JKSs1Qmd0vVasji9DX2aQYpoReU3zIFKSh1kO5HPsjNJ3fHha_nV9wWVG3TMzJ6bV1vz2E7-ECW2YQT9YXToqRGRjtf7vn8fIRPiuYaRwrXigKes6PUM2AJdbe32J5aG0hZg5NTejoK1JBMLAqQ69kMeUVnuSMBTxWNb8nLUKrlnza46qCykApF2_A-3ZoZ5Fq1xILaix47RQ0A6goFwMr7e4HrofOzJjKcy7A5c7lBul1M69SYYn3TGVodeUyhO1lQKt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OtMSda6OwtPrRq3EgZTScCQnV33hpdya8d_JMA8aDRD3ypgf3W_Tr5bR4fH2G_dD_Vlpe-iBXWBsmXjRpvinKkxKf1bDPvGU8lZcEHJIUrT08uBqS4aoUTk89W74KmNyxFT_jkJMyVjtQw2k2tRTjFQs-HpfXIZYMq54zYagvTbMKxwJ6GYv1Wu0Hbrd-oJiVoaZ_xNjwg3ipakrBib0adx12mcDD-NqT0YvMXkSiEm2YodLfx3OxDk6_6-6LXNeDdgsfAM6cspQgjnwdozKzAfrWwAGTaJkDRj3KzYaHrre3b_d118xNkoxfqRgj2qCnSjsYXBPqzUEfPvmHsX63g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
احتمال صعود هر تیم به مرحله یک چهارم طبق میزان شرطبندی ها تو سایت پلی‌مارکت:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24937" target="_blank">📅 13:57 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=Wyk2a-i95pFUUNQU8BMz2e6mRxWU1Rjov-z3MnNHI62Lcbk7T7sDbbzsTrfa16B5o-E0hybE62p8FRiMx0wozLgzkoZ3hnr9jRIAhvdKVx4AjHaaC8UejzkBg6ywEOMuweyyYDd37yEuCFmD-nc7GfK16ONa3IRL4__JEL5Q7vggQliIY3FcOEvUBuwgt5EcG0Og6iZVbj73_JiKrwT3qTlx2jXGAg0xQmjE6zixcGKQ0hGKevIbKTnUab71NKUqF4fHwfVyrMZOSLHi8UfQqcqp4X6WDB4XKMZjzvwurY_kqujohT_Oia64NpRoREU3A_e_au_EQqHT6wry5wU8dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbb73e166.mp4?token=Wyk2a-i95pFUUNQU8BMz2e6mRxWU1Rjov-z3MnNHI62Lcbk7T7sDbbzsTrfa16B5o-E0hybE62p8FRiMx0wozLgzkoZ3hnr9jRIAhvdKVx4AjHaaC8UejzkBg6ywEOMuweyyYDd37yEuCFmD-nc7GfK16ONa3IRL4__JEL5Q7vggQliIY3FcOEvUBuwgt5EcG0Og6iZVbj73_JiKrwT3qTlx2jXGAg0xQmjE6zixcGKQ0hGKevIbKTnUab71NKUqF4fHwfVyrMZOSLHi8UfQqcqp4X6WDB4XKMZjzvwurY_kqujohT_Oia64NpRoREU3A_e_au_EQqHT6wry5wU8dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24936" target="_blank">📅 13:48 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMtT5G6b3JXpt56N-r9s0jajdLgBXCMuBuCuNkuyG73HVgPvkffMYFvJ7XVi7d468F_Kseu1D5Ivj7W1G1qmRkZsnbY07gvXqJseFF4fk8yi_Dz-d4INerV3MNf8DFNqGJHdMoRPojEC-xlat2owIyRbqVIEHUuYBtGIA_YuIQxPVelLldFZftHgSLxJlo29TseTeLe4wELQaMH9S_yO_ZVp8A4VABKWzSa1InB7MTrjSq3BLkcikpE3EQR3BPpFTRZBdbZ8EQq1bZD9y4QfHqj_w2DEL10nhVmfSc23jpO2ELncxIGqTDR7ety5cjPNY0EBeuzoepsr3SfUBCG8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
دیگه با استوری که‌شخص دراگان اسکوچیچ گذاشت همه‌چی‌برای رفقا مشخص شد که اسکوچیچ دریکقدمی رونمایی با پیراهن پرسپولیس بود و هیچ درخواست جدیدی نداشت اما اختلافات بین مدیران بانک شه  باعث برهم خوردن این انتقال شد.
‼️
کانال مردمی پرشیانا هیچوقت خبر رو از روی…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24935" target="_blank">📅 13:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24934">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQ0t-vShW-wDEUmVWD70wbr9gdBsNzIcFpd_b3zQurftiln8nJljIhRoDYPmI1ec2npa7ZUzjH9wwLx3IT4Vot0GgrdjQCf8h5OuTnik4-u18GtFLbsJK5R8LKAhAcsoIbPchlvfzI53sYdillA0f4VojvRP_6g1yGu--M7NKqw7pXYuweTZHOSG50ZjFsBVd8TrO4wTlztl17kC0WtV9n-yzmOX-67y5IxojuCZbmI6m7Qr9aXF57ijJDvwx6_DcBAfl3ppUopz2b_FQaadL_jprTRzVibhUitgfaqsVGzQ6qztzZAKFYmIQpM_isv6W8LzQLoDoi3bYtGmj3GzYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24934" target="_blank">📅 13:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24933">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMsJQfPDDcsoU5OyjToNaofTmM6nQ-_Cdd2XTQSQOGlo5RS4O0kinYOJWSwO2FCaqNnQakp5lf_CpvLO74mdZ_5HziwQsdkFPQDT2FxZzK-0WFMAUVeSweH4Y6qyu69D0iTGMW4_hl0WuzPLfP-QGL5iUtYKSqY3YQ3dhiQu06nqCNkNNj8oia1ajs0BgmkAynzuAgHR_Zl5SKRltd21SfoKRRWcUkBP9NnsjzaxcnSCesTFtwDeNwp4degOLq0nsrhLlAyEVTkr5dyOZdbHglrg1tN9TH7bzPnDYboJkxL2RFWe3mDjovN92lQYPjnnlxy2cbQiZcFXRRh3H059tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24933" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24932">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9iX4uImYElAtMpBXvWtkQce3Tb5fQ6S97I_7rbmdrUQPzYrzy5MqchlkvtRkHJYPz2cXNh0z2zeNaBond1jnSw4yPFrMJK7u5r8EIuyyYxRq-1-WzVzKxsgxH0xGFRa-9HaPa8rxtSpw4Mm3DdzPl1QjdwLg1zI5PkIoGGp64cFlVSxZLNnbL1VonY4XblHBkOEyNsm7JJoHzKXlI5xN5lDFcpCara_iTupsbx4SXWIDGTohZVGfeY0Z75xxHgvmGsqQmGu68XSafEqv4WBQFBAOJ-YdfKiywtqpcexZLM2Mq-hxmPFwiZzyKJhcE0uYltSDm3rOHRVPa5wD9ZWSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کادرفنی‌ مصر برای‌ضربات‌پنالتی پنالتیای کیلیان امباپه در رئال مادرید رو به بازیکناش نشون میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24932" target="_blank">📅 12:59 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24931">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cmfqr6WsaAn4b8gAFKtycFiub4e0MesRn7zA1P3li2TjZLl8TEx4BTAifc2f_VeqYnEQrceaka4lUiJdPdXrttYeJGnQIxqxz8S2JgzmNtJ_WwI662f68qBSDPIqs9jSiBOMKswri4K4ogK4jLVsn1Dv8_mR_HwoxD4uVeH0pQb1piV-z-jX8l52d7tX-J-vASXAa-QbNrPNkMBBWwOxJi9v9HOiUuEMj--hlIO9Acx7kAAP0kKR99NBA5SHmki-NjQZjS7sGt75nUwNLvDk-Z9Ij-RbL2nnbEaDgsj2DAABR6n43L6ZS1QD2FNJ6UIY6_jaNKGFGXqvY5JByGxNfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس:
هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و برایش پیام می‌فرستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24931" target="_blank">📅 12:34 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SwuWN0pkS27uKWB9m2hVDJWoqXvg1JF5g8KwQZkLhfQ9nDhRUMVDfHD-Ah4U1f_-k2QAjihB0eO0NaZb_20aRXnzz2ReOLJQinOgpKk2CJ4XIwoJzSIw7HAaauYAgD-n8uv7IlEOdGksAQyKl3BSHDDktLCAHG6UTcUcsxKiA--EH2YwPakOxjWX6MfAQD73Rx3BGmTLZgwWzmVR_VeOmVzQohUPFzmVpenyn1VpJ014r1RrTI_8NV81ce2cUzM_u5WXH-OY5jvclgQ9u_NNmM67FTpKWtOPkENCuHo_Di-W-UoWM3ui9jikbrSy6B8uhUbtFsiadF6N-up7rKU9Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cfc13f85d.mp4?token=SwuWN0pkS27uKWB9m2hVDJWoqXvg1JF5g8KwQZkLhfQ9nDhRUMVDfHD-Ah4U1f_-k2QAjihB0eO0NaZb_20aRXnzz2ReOLJQinOgpKk2CJ4XIwoJzSIw7HAaauYAgD-n8uv7IlEOdGksAQyKl3BSHDDktLCAHG6UTcUcsxKiA--EH2YwPakOxjWX6MfAQD73Rx3BGmTLZgwWzmVR_VeOmVzQohUPFzmVpenyn1VpJ014r1RrTI_8NV81ce2cUzM_u5WXH-OY5jvclgQ9u_NNmM67FTpKWtOPkENCuHo_Di-W-UoWM3ui9jikbrSy6B8uhUbtFsiadF6N-up7rKU9Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇪🇬
در اقدامی جالب توجه؛ مربی مصر قبل از ضربات پنالتی، خلاصه بازی‌های رئال مادرید رو برای تیمش پخش ‌کرد. مصری‌ها این دیدار رو بردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24929" target="_blank">📅 12:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=T_uCJY793wxSWGfK-DCMGP8kQVvVtdVfRgvTSVReFeytxcnup6JbMqMnWNscXMkx7fEArucpRp62ToJXoUL_LPanCuBsue0wSeYNSKXCC0vU0lX6C9HOO6dMUqHWIXJxDdS9o23pW0_CuL60zbvfRhPSigB43GqsFiQbbzXDSB4IBs37QQi3uJip2clIvTXMTWvOhRwRR46pYbfRLXAgNdABSJ9n_O2rxERI_gokfK9bALXPzPiENH7XOTd-9fTWCXiqgCzzo-24ewWPPHF6aqMg3gTipjdIsHhC2r6T59hm5NqA4e80YOVDxYQAabQ4SV52tfRX9pu6IR-9tBcp6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c33bd6932.mp4?token=T_uCJY793wxSWGfK-DCMGP8kQVvVtdVfRgvTSVReFeytxcnup6JbMqMnWNscXMkx7fEArucpRp62ToJXoUL_LPanCuBsue0wSeYNSKXCC0vU0lX6C9HOO6dMUqHWIXJxDdS9o23pW0_CuL60zbvfRhPSigB43GqsFiQbbzXDSB4IBs37QQi3uJip2clIvTXMTWvOhRwRR46pYbfRLXAgNdABSJ9n_O2rxERI_gokfK9bALXPzPiENH7XOTd-9fTWCXiqgCzzo-24ewWPPHF6aqMg3gTipjdIsHhC2r6T59hm5NqA4e80YOVDxYQAabQ4SV52tfRX9pu6IR-9tBcp6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
در بازی کیپ‌ورد
🆚
آرژانتین؛
لوپز با یک شلیک باورنکردنی دروازه‌ی‌آرژانتین رو در دقیقه‌ی 103 باز کرد و بااین‌گل‌دوباره نتیجه‌ی بازی به تساوی کشیده شد، ولی آرژانتین‌ها در دقیقه‌ 111 گل پیروزی بازی رو به ثمر رسوندن و به مرحله‌ی ⅛ صعود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24928" target="_blank">📅 12:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3Q4DnPiAiQtKAwIJEruAJjlHNEQCu162-GkGc8-R0LoulxjTlgcBbH0toagrMQek_YGHw5tqw9_SMNOZEPJ8YUNofO-oWW49SriNu9kPAzGmZURw1H2DneJz3t5hbboanyZA65tVaoj_xfbTr2K0_mIVvC3uqC-QywWi9IY_MURocnzv9kRB0B22fhz-_LPxMnLE8fqATC_SWcjvyFrf-geN2L0p7gjlFVPeHKrm1FIX7A5drkjAtgrIQxyW4pRmdICgMJEUSjw8RbKpLwc5Y-AzVROn5QfXB7Hh-8DIyHFY3vZKhWc8s_oFRorDq7zhI2Ww1YwtQdJnWRVCEhGBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
طبق اخبار جدید دریافتی رسانه پرشیانا؛
تیوی‌ بیفوما وینگر 34 ساله تیم پرسپولیس با باشگاه فولادخوزستان درحال انجام‌مذاکره‌است تا درصورت توافق نهایی شاگرد حمید مطهری در این تیم شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24927" target="_blank">📅 11:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-WAHxCRFiDzTv9xsm_GErmsq3oRynJA3K0wXjtrbyO8FpPKgDRe02-6kh9rivKa7ORAzof3t9HAxbh2I8sgS-IjAoj4g2rdnwwjEsv-IjmfnfG9ACL5wXN665ozMZoNB5Os6gspROK7y69npBR3GdokhgFscp4qUV5k7auNzd0xaz-mlZ74jtc3t_2jNIFc9pvcEeOofU7mwCVu47uexLmz4KESVXuP_-B6kg7dvnLHp7BNCed7C1sLcRwzQXCrlSoo-ChPBCa5WQ8YbhuEwnsAu8p18FUU8Do6MPc0ufdepxxaVKOoeI9JZIHE3s2x4sivt06U-X05RsMwoizu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24926" target="_blank">📅 11:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAByVTJC-57geTs9V2BnjD-MPOeFClY7DzOBVC-zRuMQ-D5ttbqHeNr2rO1pWrQ36eNbDpBKm9bGZ55qmadczVlaMop3U5VdRrUMcTl-eQii5pBccbNb2QKlnVoqoX-X9K6o8HQXud7Ucufugy_eQcTbfLJNvH5_b0ASYUD_IeTUNyPnzwRwWewBCwAwUzT4d15Zja8d27kXUp9r9eGpUEFSuwFfGPprA37vwQaz3oP7SuhmJG6BS74C4lTdfMH8Jaxllud1y2ywn2l9J5C5-uD91TX5j7buRsZZ5oBqO5oB-0jpbaqBjf-jIill_rP08-jR2OZxkxtetECBcvl5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛ به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24925" target="_blank">📅 11:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24922">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sPHbkYeJ0oTu6fSlqkQ5Zb-YEWdXhbgAmeJYj3LMlQDCdg7Of_3rnw6Cm4LFx_JFP7NYiK_FC4IKjxPLXlCYYIGQQwf7S3QgD4R2jODyuxc8cO4ggdyThaqfZcqSCpm5S6nbK1gjAyE8Osm4Xwi8EcQnq9pg0e30fXHY87v4H7wOQHFXV-PKJiXJSiLwGYulYxsLOxp8nCZMMOV_Mf0U8fpBSe6ohT5x40XwgZHz09buEbJ4KDyrn7R2FLrng0u60-Dey14hK11n2N8kb4QbJY6zWCyaNXgWWjkPpCtG-Ur4ZtzXJSXpf_jNdRqqIYuORkaAF1eY7V4owruKTaYSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24922" target="_blank">📅 11:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24921">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTtKzMYlVlW156gf7itu-3uSSZyIdpF4YIH-MjW8UM9Ws9RTvGTWY155qYnEP2tuv2_9yTxTTi-XjKr9fMBg4T0JOo4EVjXH394QH9I0MfPg3_SpwZx9umlKjTUrRico4ILQk7Xtw1bOJogd7hRlVeGAlrYeXbBqp91f0b4w3DpaqbDE0EZ67qHimRJY7jmjFu__VLYN6szAVB4EkbD6HPkC90TaAS1PO1n3C8YHcqDsBjogOCdknGOL3OUoVJXH1m3lEyOn6qHHRAoUFJCI84jyIVrDIS41ZRmAPvZP0B0DfdDViMf81_E6QBghXcRtnD2hSFcxn-deolQ1nezSzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
طبق شنیده‌های رسانه پرشیانا؛ آلومینیوم رضایت نامه محمد خلیفه رو به 70 میلیارد تومان کاهش داده اما باشگاه استقلال قصد داره با 55 میلیارد تومان این دروازه‌بان جوان رو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24921" target="_blank">📅 10:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24920">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLwgj2P_cGxbSdhLRL0RNIvwzqxkjtxTqf74pu8w7SX2tuoFisYwbHRBUmVEvoHvktUHdL5wstzj7AwdCAuaCCJNjFfXYCuguWwzEoeDLXWUHOYB_skhPfKuAKnu9ISdkjCYjsU6lMpmDmYObBVDt-jqcr4u3ucxbgnETRPo8JFEQYY4u9OS0WN9hiXRuej-JUTeMa-OHVW_GAUmNuk7UXo-mJEv82BPp0BMn9gYNBl4d3tgdKp9OXFL309mFFJGjCSWGRu_B7-VC1_gUF9MNY5Fp6yKa3dT4cYWLOhUTRl9RENQBKAU95TOLegorCZAkpIaFdN-F8xXfQVNwZZevg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24920" target="_blank">📅 10:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24918">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ks8BlAfgKuYRIanSIZu1ZnO5irxLxdNIzHigSWAVQtBa7dV3cFG90kf0gnC3_ndW3H3-UoumTW2hjAsztHZgDRr-Jtt_0cc4ZC8PjIW8Bwh4zo9zvm-WagHRu9IT4AHaVcZXVQyg5MxKvHSTPY-g0XU1LUf0Kfq1ZKDq_zQsYK1b1jB1Rb5NVYbNUjq_Ff_Xfp0ZV021P6eP23lYNL6E1VU5tPks0su0oI50-qH7b3BCAq9hWY3l_YuOofUkbsEH_y5iSCey21L4CWe5mUOdV8lfLuDC8VEcRkR83ys-wFDh3_6b4LtmSmTRWS1yT4YWE1R1d4A5dVDMNpJXUwrwUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24918" target="_blank">📅 09:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24917">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=XbkqfZn4eLddd_scJQIe0h1N3tMQVIWyBpxkSV-ExWwK_NhcQHwp1-hGHX_qYMwA64Cv1Bnlq54Bwea8TBkTbFNXLS-zUJ_0ClHFfEjxQaQs5RlfHTHh1eYUepzYsIYs6Cq_m2LzjHnmQgY4BsoA5HS79MzxtgzBEVrt2FJJFUP6WH7nqtLMjMHTB2-CwOMOCvtxnI5hXY-dsExEWh3NAhmyvhMkuXaQ_kqgC-HPAiABF8dFAzPtq2vdrBcInPin8XuwuJxbiuXB-BSzcrKrxS_EJ27olCHFdU2LyPqc5N6-zeSY5ICN54J_b3MgHAuwPldGH0e5SBQoJYWQDrc4XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef17610d75.mp4?token=XbkqfZn4eLddd_scJQIe0h1N3tMQVIWyBpxkSV-ExWwK_NhcQHwp1-hGHX_qYMwA64Cv1Bnlq54Bwea8TBkTbFNXLS-zUJ_0ClHFfEjxQaQs5RlfHTHh1eYUepzYsIYs6Cq_m2LzjHnmQgY4BsoA5HS79MzxtgzBEVrt2FJJFUP6WH7nqtLMjMHTB2-CwOMOCvtxnI5hXY-dsExEWh3NAhmyvhMkuXaQ_kqgC-HPAiABF8dFAzPtq2vdrBcInPin8XuwuJxbiuXB-BSzcrKrxS_EJ27olCHFdU2LyPqc5N6-zeSY5ICN54J_b3MgHAuwPldGH0e5SBQoJYWQDrc4XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
هوادار تیم ملی الجزایر که علاقه زیادی به لیونل مسی و آرژانتین‌داره‌ودوس‌داره این تیم قهرمان شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24917" target="_blank">📅 09:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24916">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbvUgXO0fLhY2E6QACO4B_Jg81ZGtBKEQLYWEXYxzNOFINkZVxzyMXcNNILivNP5vui4t9I2Iw2hQ8z7ChiM0yYCFUNajIXLej7a7qgezcI0q0ECFhJcH_xJLthjihe31t8gGKm5p1aPqHrYuDK4d8eO2kTRWZtjJkSIQFJ5WAdeMyqsYIttCs9pefxm4TFsh2AbqcH2LCGDxZ_TtrgDWVkoeWyufiv7lCFX5i01ANZOcYVpOAQyy1ImQN_9O2Sog0uF7E81c3vgnjz74BdxUy7eoTgwSk78PFARJt6yQsXuRxBigk8NbrM2YxwpyqLMwL9n51-utq51otAQIaccQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مسابقات ⅛ نهایی جام جهانی مشخص شدند؛ لیونل مسی و یارانش به صلاح خوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24916" target="_blank">📅 09:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24915">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbuCZg7fOGTL-OWKtmkRaUJgMF5SoGK8nQ4rboazIQIoqUy-I-e6dlBQm4bEhOTtVl80s4IN1a5SjLiONUYMAungvgMuggaIQU5kHc4HPCSYr3j567tQUzDgwaru4payJ0TB6Ht_DQPjLYLL1tocrF4wAIib7iD1jESM0um08Ks2HyxABsOpQsh2OUgmDvGdUdDXOqa9hJbRkVzOZns9Iwf5YdRJ0gItUrPeh-y7maJAzCaqiYo1i1mueKK37mYwXTXI5-uFc-aMDin6orIWDDYrEh2ePxPSE_H_MQHh9W-Sa94x6TEgkLxuhDruW_yTHwX_rVyOZiFyOqGYayjO9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24915" target="_blank">📅 09:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=DZKtphQJsJ-MaV3mYBziSIMd1xmIvsukk11W7zU0W87_EWTsL4T0TfhLGashcFU0Ajtw-VqcoJv3g8uHbvrROqFgcZlUBButIo54wXNwkMGj5E19QgjxSRKsqIkYnfJsh7y12j2Y7MRol7cY6qmmrQIv7GqY4DCZlJVI44DUah1RP2dwNTjd17u3TC7rzJDUs9EILsAIUzNDiVCcnUVRtD7mrL1G4d0MpP3_MaGaxarbhkRBpZJE-orJlZkwwF9SoIpYXYBtL6YET4XPg-a_IeMlBWmL6_PluVbZeS77fF2QazPL3RZEMicVkyXDEiiDR3h_GnrLQU8DScevBA4JUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=DZKtphQJsJ-MaV3mYBziSIMd1xmIvsukk11W7zU0W87_EWTsL4T0TfhLGashcFU0Ajtw-VqcoJv3g8uHbvrROqFgcZlUBButIo54wXNwkMGj5E19QgjxSRKsqIkYnfJsh7y12j2Y7MRol7cY6qmmrQIv7GqY4DCZlJVI44DUah1RP2dwNTjd17u3TC7rzJDUs9EILsAIUzNDiVCcnUVRtD7mrL1G4d0MpP3_MaGaxarbhkRBpZJE-orJlZkwwF9SoIpYXYBtL6YET4XPg-a_IeMlBWmL6_PluVbZeS77fF2QazPL3RZEMicVkyXDEiiDR3h_GnrLQU8DScevBA4JUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6xTK6f1w1FkHCK9Bi8K67PIlJEVrIvaofeQANq97z49xbQ_MOVPBtMc34nVO3k_0EFmsjwmPFnYxIPxs6TJHVHU_ZmuLznJngp8iFG-6bzxkmGrLQbHpfLepxudZ8lGKaozaNEWcKGlZMA-8WtQ5vpsakqHqViIGx8ZgWjsJo62dhQny4vpFol8bfFmSu5gfH8afAe2lNvMp__-CpzQPEOy_j68F_3O_Mak4oFz5-zlio9ySmf647rnk-Fdf5jnKV0qEZ_0nAg6Ou_WfHFVWfzv2uSI_7pw0mGqU0cxey-VmMj0_6m7Wirp7crkGG7a6xWx_dk503WnLBV9i9MtNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0Sr4Z0nA3OS7frEiAk9w7HiudKt5TABajSc_mj6TBDDQWQT5XJkP-H6rIS52A4GkuDlS9i5-xw3A5rixMTNfUDNL7zO4Z2UQXfmzSpmnQO9GoysomTHUjCBLtjk574X7-aJ8vNJEmtnknrN6oEmqggMMOVwTGnulkEtGWlYuCMHpWCHWJrLLpTVVx_BkK83rjUXFhn0y3EG6ZUjVsttk1iXF7k5jRQmp1qAzk9U5MLKO4HpHOH7E2KBFaxsII4AHvtTTsGhGIGYDw_LjXKhDk_t0FdxMCenlA2mdO1RFa8wEPE209Agv3K6rWQDFiOOwNe0gI9Ez2tL2JY2G0e8LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9CZXa224pnobyPzBjTjnghVZqElRpCmEMHiVESTQMbykvNalima0ohlMANhxZF-YQjQ9kTnQ2JQr_xbkdW1FxjXPM-Fck9F7rTY2bNmmPL5EcoPoL4Wc2f8tare8wuifiUOg9XIASNjeewrcuseHQR7j04hitss4NvSrlnMSpQ5HgkOHtln4elGrV7cJckqA6gOI7y84t4cBaPwslA0NoelEK11tSnJY4RtdtFMywz4umwBG75EQMtMD6Uq7t_GqEDjcboNdxLOF3hAa78k13aExcOEsyA7bAGy5ZNED5zJT7t3_ngOpznoZ8xbhVO38QnaRZdivMaAKa8GKUVZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNOaODXHUXcj3cTOzETF5QJsweVzB4aiNU_tywoz89LJwkL96loP5niVqdmH4n-nFuJzlhfEmm_fKoL9dye40uSLU2P5WGO_0jhr4Rhg189OC6UfUSbLi5xT8Z71imiFTiYcMabzoOBn__iOuPZ4pv4Zac9WKtVXn31XZbHlK3_Z9eGy2prsL0Ydi2m0L8FxE8dA7mCUI-WRMlup3EmvZGTyGFacejBYAeVXAFw9_O4i2yKQ-NjxCwjbF6f0K6vYAW2gBGMs4TgvKa2JGrFktaxgj24csfHWSOg4wlSqsXZy3Efo5O-jvztIA6JDf4H6zMPrQm8ivsNMPs5zBCQ4vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoLVfLThr3qguFZPqOYb6heKfenzx5C2hBtQtpSzo8fpPsxRUXexW-DfHZ8ngYRuybcI0e-N9VsBpJel5ZR1mGarpvRWAwBOGDY5HT8Nle1Zo7FVmJUdoCenH3wkL_xRyHQJ9z8B9IhIPfXG_5ufdM705wHcuHO9VOfZFLMkjk3HcAh5ARCnicVabx7lQqxJw8IyMCNZowU9IBg8_vCwhnOIHIt7Q6fI28-NMO08waHZFDfkvRMd3ASqtliln2YOZXrchTL27F_swYcFC45q5WFg226EhgJmwYZpTDkOBVBh6Cw7j3HBu7X2uvjwCclm6zBHc-16mXhxNmrIvlOfAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=e3Fj6dWZDLWWBaCU-qeKPcD4HO5Xp5WlaY86lux1aT4RVbe0W60Eax2TZpSuC4zST78oD7lRsfYFuMS7zd5pXjjmJNMdgeNizTasRJHz_5qHuhuiJZMF1rXEijNKnx8v3i2bRWzY4MDIq0ulPhyLjMI9Paq338PSQgEkI7PVjIOOd-FIUwg6Zgm4vuRDEQe3fBbSztR1H0wHpua_Xe_QNth_645OSS4mI31iRheXLqSjYiOkq4r6Ipt5OcVYyoWcXGXyU71o7qfqm3oaU8TD6VH3sVczW1IWUkifUQ38Xrep0Aq8eBI9q1xBofzOB8SVYKruLwL_4kqG4AytnKw0WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=e3Fj6dWZDLWWBaCU-qeKPcD4HO5Xp5WlaY86lux1aT4RVbe0W60Eax2TZpSuC4zST78oD7lRsfYFuMS7zd5pXjjmJNMdgeNizTasRJHz_5qHuhuiJZMF1rXEijNKnx8v3i2bRWzY4MDIq0ulPhyLjMI9Paq338PSQgEkI7PVjIOOd-FIUwg6Zgm4vuRDEQe3fBbSztR1H0wHpua_Xe_QNth_645OSS4mI31iRheXLqSjYiOkq4r6Ipt5OcVYyoWcXGXyU71o7qfqm3oaU8TD6VH3sVczW1IWUkifUQ38Xrep0Aq8eBI9q1xBofzOB8SVYKruLwL_4kqG4AytnKw0WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3u0EwQHnsNsEGJms91eqs7qEpeqhqqRm56Dlrdjj_cC7U7qHpltt_tqzFGp8hNimNKknY4saXHiV93GJv4-FdvUhmGiDFjY-RHLYO0Jt-R3LtA36c2d2Y36U_jACFuttnVEDuIBW2tlyRF1Sm7Jbg2FAFtoRFHoTpL5Dy4Ch80GoVNpKpoQRkHjGX4U8sRm5D_9boT9ZooGbLyvNsQecEA5qO8qQhfuP3w_x8D3i6udZL5azYA9M2ZaT5gjDi30Xm6njWYSxJGkFwe0Bi19t73tUSw_kEATb7yiU25MF3ifHPfnHp9XDNLvTMSfQ_GF5HLC6ajK1SheP6Ic-GVxUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnXjWHmkbYA5gwTVksNWxjuwYQEEF_5qyBGXEeX3KVAd53jmPqRIxUU9GjhJmxT6jGDJhtMelAIdJpO2Uc7K4t8hP24YVhkvRQuSbeg2db2oRDUOpCFYx8XOu_4on74H4M4eANMvoZIRRuSauWfu8KDFqSANBh47E6DLQSMdBmIACrt2t-6_L_UeV0ol6x8vOesqMQMgw99Rz913_g79a9cfQHY2gvE6Sh9LnzNbKPRfHkNEDkxsz0YaSbuBo02egAN_VerC7FshqLh29b4fMlOeZR1tQFr-zjB1tEXFJpGXUuL9dyxYoCuyXHeAUaLgMuKIXoumBrUcTGs-K2GljQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evWh5l3S6HwTc8CU9alfLWFhl6uInUnodND6c-NCQ4_OvdQQUYqhQ5CCwXnWYokdNlL9_Zos01Fvgvw4kc5DyAptlrfK3n4XcModTC1idIyvazlaCHJuYfzfmn9d_FQsehklZBGqm0bX4eXKtVnHldbbU1sdvLOhag0xnCepYSJ4_Dp7U_3eVrVdYUBwN_NgXcVSe-dftmnKNhbE3g8SWXJUJkDjgKUcs7OHaUFs51XHCPq4bCX7g6vxVUZzi4utnW7I_euWDj7UJFuXtUrMIU5d9mRYQ9P0A18P2nlpaAq0bV8YZ4MpPWEFMjZA8RVFMqRmD3jjURplf5KoCXQOxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giBJe3SGjdSGkvi6MZBKuzJU_7bKjBDy30oMJAIm-ZUjeN29n8687KN6GSK-jpQuPPIiSOo1cQ-GqjX_pg34tsQlmhYxrbTMkgZM6dBOR8fr6u0ZDdHokdXMO9P0UuIpx7yDqz7vl4PZiL8p6W-ZZSqWgqJHxdl6golOrA3oSiBvQlv04auI7UGOhXvCd4-9p_ZLMelmrzJcBe-zdZFIsl_QOdT3KdOyQL4OYwxSN2BpjSOuLYCxBPauImOc8YW_IlOTGP66XqHlqVlmsR8n0263aSN-wWYhWCTXI_4kUjOVeu9m-dELswWIvmezS9fWGwjMQBzllxF24qzEWewAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1edXQZWXvNiOo4FNXi02Uw0Kz-0CL6NPqMmLyWAwnOc1c-0ycOtGJmpNr26P7-RmxCHB5tS31wF96bf9Gf6sCpvBmPSKfhyA9S3Dd0r-0wOq0SbLgx4F0dewjJcUGSUB9V4O7hVciMtiU4Qs35ZR0Y_ZLBWf7z5Pkvx0Kb-xj13woIUT65nEMabDHvSkXZdJwojuCkQ2UpNVENJ3tANEdLcH179Swn4Ew1O5wAVTnuWTXOxWadIaai60lZWXy4v-1hK0rvBtxQeZ2vPHHRN94m5lEHhe2ieOArnCpSbiJgSwt1ng1JfDR_JsR9-HPoIpUiuwd_So5cbaer5Xoa-ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ErNQu1bEOT0-sEyU5pflv0qEomT4S9hnQRMk7EcVgQy7y4vauD6PuYQU8FDfbxmT4In8UPyn56b_lPvVKYUQ0YEIWh6pCoARVahCU2W0BEFJZhwhiqSfLNtQMvD-8ay4QNDyfnXfg95jjilfUF-gQGqKdj0e1i8dEs_Zo5zyeUFrg8vGwzWOvWWlAs9bQuYkh23sm6soGsn0e2OGgl0k90DpC8JRLopbmc_JvvlxIyxE-aWHaaMxJWl3PUhW5bQLZVGMEGok3lUj1h12zRzs5NS38psxNuMUpZ-JtnH4IGat9xjEe3MW1JnDncbi38wDqJWxgs6Omc2_UZgEX6Me_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=RMFutJe7Hj-jlysLyO69WyNENvfcP7RGYA7ZIwEJLJLy30vXcUcmM7ATBdripCJJKR52ElFBVlMukz0z1FdfEP-XEI-1M0ykpnsgJzbceMYwZzGSq4qkmYkSThDMwyLzbjiq-d4at9LvhaNTS_PyVyoSms3DLaQkGAzXTS2IehDr7mh1niVkF-lzp1ueIWME3aBC8PNC1DkcQ12Bxr1YBM2c_6WhvqmqPHSNuyfXUPG0KhaZyvUbdob_Xlfy3ca9_vx72kJ_LE_eaMPrj5H4-IEA3ukeoY7adqHv9Gw8e2Yd0yEW2ub6eeCSzBK6M57zDgHYzxDJTzqG8PUdhK6Yhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=RMFutJe7Hj-jlysLyO69WyNENvfcP7RGYA7ZIwEJLJLy30vXcUcmM7ATBdripCJJKR52ElFBVlMukz0z1FdfEP-XEI-1M0ykpnsgJzbceMYwZzGSq4qkmYkSThDMwyLzbjiq-d4at9LvhaNTS_PyVyoSms3DLaQkGAzXTS2IehDr7mh1niVkF-lzp1ueIWME3aBC8PNC1DkcQ12Bxr1YBM2c_6WhvqmqPHSNuyfXUPG0KhaZyvUbdob_Xlfy3ca9_vx72kJ_LE_eaMPrj5H4-IEA3ukeoY7adqHv9Gw8e2Yd0yEW2ub6eeCSzBK6M57zDgHYzxDJTzqG8PUdhK6Yhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bh_QRN6HpLlBIx7OFwvy9JqYysJ5cdp4y5ME_h1hH9zQs-EsmiVlq_DILticYhA2nKTc-mVBR1xorVNw9cJIOsYoDUfNscXef_P_gMfFsXsW7alLcdYsTGaNlBCtPw51qrKmrMg1O4dox1ASDGdSU7Fglg38dO2o3okfs6qSQleglmTyzdDx8Xv7rSWwlEz4lGfaQmQL5OF00Jtt5o_6WW3FR49Cmy9BGklno8eRUcpQZMXnyDArglFqVPo-K6afMsiGQMAElUBuOmhliOhyk68iKEwLoD4mC6K2QpOS06weOoILy8ZBx1OJ7aIGOi_ovf5_3iFgfB8liVYWDgbd0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riyvHPUwfdUVpa7gEgKHbnshWOHLapqIdNO8Y123zFEp8fAyNdv-acGzwrLqZvYjbCIVvYZwxH-0vgaVgpz0mdaKJZ1aJNBDHMCn0v4nRwhnD0qk3gKyemURVU_b3bdjd4sLRbz9y5hVpzJ28-tysTtZRW3xoMwwmeENLvNikaT7_k5w3VXp38ER3A647YAdxb1OORoZ8Jq30Mdr4W-xBP46IPQXdDal4HuvDmyyIhiWiRL-Mg23VO4-vPiFJA6Zt-NM6w5UARaOaoNnYlzdwkMvHWD6WTZpsaxgeSANF_eavLEx2R5adwmECbbTW3GB5uAX-7vYF5vRW0x6pS_EeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DsH0jGtCODRv7z_W2zUZdv4AW7602bazsSy5MPFU1dvVWZWNoxCU6WOATtKLTxKjnL-wmddvwQ1tMWpmXF-_Qo4RoOQo5FpfBhAhYUVrIoYtJcde6RtttU6uNVsoG36optmMqWp5v7BCOsXRIeQ7m4FrNDw6FduKKf0viOSbBNBINHzmpuqNSgiga5C3XYvbXD2qdBKfCeXG6zFGbmLyCrx0YuXwZH2b2f9ZPS0cgfAXyb4LTagImvEA3hO5i81lVu7Ac1in4uqxVdqTzXqqSkudF6brSJun08KRezDovfXWFVmwjQark6lvncXYfAmLiP_5pzwRW439J84sxY1VKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYUcv-NOhT01NqstsMW3kslK7_KzY7C1nGBlu3JcRtoCknt-H-7cDkzrg01p5QcN4X2K-ofQELog2ZY8I5ZONDCJSI6F2zmrNpZrM1q4UxyZlvFK9cNtfxjXZAK9zE4t51ruu68vZhYgKG9bFaRkTgYE9EiD0RCVIEzRb4XSfUdetKzttMq7kXfYvBOK11KVgSXPssdB0o7QQZQ6xvY4_D8n48kvxlt6WVcBux3F92_T3yl16pO89a2-0BTQ-yoNeK0LYjfWs7yvHtzqJTTz8tnCgbcrH6Y02iXJM3Hs_DQWX1_vfx6kzJ9Nwmmjh0mMJ4enksbJLpc_HFajtMAm1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvTtqc3Oub2Pbx-pYJLBQledXodTt4nX95KZ880OgNY94Ne2OZHUl4gqEToDzb9puYThgKrukfQe0OsAWTvwACVMZDfn2K3Wj9gLWHQxKN_dge6aCxIRfcDnPcVv-lOFmbnprPVi6ONbtep_uF9TP9vk-XoNbL4Ud891lPF2zX-Bt7YlR2yLm7ZZicNmUPodQ4vv52pZ3_gcglU4g8HmzhX_85t8tq559384Rh0kjJwAZuRQqMeLiMEyHRkS-jAppwHrYdX-zoVGQ9zukFIijM4Rhc4jYy1SHxpsy_vrZPjxtQhGE_Rf1sR33G6np4FL_vRnnm-122Y2edgDCTJJbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti_iUl_oGJoQ7CrYbuYl3rseMrv6taZBUe6onAd-qMbFEQghXjF8Lbu0LuMTgCoD06keffiaEnoqM3o1a9tIwRc5bKAn1_1v7de2mvKgDxBHA1EGbm0J8DUEVAJrEpZCt66ZSAtAfB8aRAlNvatKsFxuUThy6nWyw1xAcuZfSPrz4vT7o6ayM7gjvxMDf_56VT704wTe0VJlw5UlKRsqEKfjd6od7prw9QhfLaVjokBEoGwE8Cg4hqUIoOA5dXTHKvJceCbva90ot2JS2m8OCz7Xk-iihHALK4Fl-PiCE0KrjOTpWpwfB50nSKI2-GP2InXh5vbvOXP6sE824ZcoGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p6ewbFiM6-xEXxp-3719_YDyWNe9MKHx75BktltNjQWZF49_FsR2nvV3L2vCGkTyMyJFBKAP1DWJW14qOGgL6LoyJhvKk8iBvvt4kWOKFoT4JuRx9CRua4kMI57T8nYKOn5krJjGxPu1-5iCzmRwPdJIKDpaOIIMnhWclXDvRzXbaP6CpgaUb48VcWwkxVFMram_aycqa9nLD8GadDhQOJDKxrzAmpCyUpyJL8jHl6rel3z47yjV-jymAmxV1doVAePBMKISJIXZHj9Kd0zXYFsI5hHfI7VvYZvw5_cswAfzcdgGY3TBSKiqhcbNrCNPj2stsgpi-P_QCwMlBnlH-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L69g8d2aZbEWj005S4-t2l101VQGkU6XEV3QUfNqIcpKyiZVawSckBssa-VkVj3SBZ2XYx3aC-xBuEhh9UAoVJt6amFtcEibOK57ulA96780VcyUXe7RyYwEkB56X9Fowf7tTWdv_svnxheIE6hky-sWyQToktiJ0J11br6c3e030RWHL0KMphMTeAbch7fLj1Ut3C80ekuVWB89ZsVwgj1YEXK7OpIHVPg4cHoOGTNicdDCOn4zT9drfaut9gGywgxS71EnZqqQJgdST1ik-PLBP8NHAZu3IXxzpVjDgfjESCOcbXXyiCnDTuyhHhke8VjvCaPPsv8jFpdGqDMUaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEZYQX-RoQF4JckxE_cwLTe7STj6VMiK1ld5vBpjERaDGiNd_8wmoyUqUw5S4qsId7Cdl45M5FTrwxHyJ0u3hPbObISwB4xBkCE6vuh9tJUczkNlcKvbkfoZ3vqxHyu9CqycVBDlQLc3iC2R0WbsA6UY_5y93SVr2-KhzBqH51H9QEutW-rIihHd3CIABQTKY-h_an_GUfvyafj1oJ9yMS91jTASLqHRyXRuunWsh9RvT9r2lSmPt17PCXsYClbYjyZ5iDxvMQkN1u9IvnN9Rifv-xOJpqO1FUp6JlaCTvSjkMlXa98JgJnYfZfuLNrvg5I6E7gD76NjHZ4FexV0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=RJyBf8L_3U6STcMdtphKQhYN85PB3LaBlIOfOLNGq8KcQSZd6yjZxggJYTa56sz6DECjamODTK7Q3YluSkrSUVp6z23Du3BsQiOJ4yoYEBhylrKKtCetCGza36lz4AleLleNo1PuGLXx3eGz2CKJJ-SqjLlNl9-QuHryHU7DOsNkruP0I0_Jh0Uml48aHnBSJl8TNzD2_rzQ5CFhtdPSmnGkYE1VKXSoOlaK56KfeMpWbpglVN0bfC749THs0g7howXDt-OagvL-yUcEekHlfATSaQud93wIeLJwc5cjfsd9KKbuCVg7hc7OmUq8y9ZsDjNQZdI6xRjF-9J4RAryRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=RJyBf8L_3U6STcMdtphKQhYN85PB3LaBlIOfOLNGq8KcQSZd6yjZxggJYTa56sz6DECjamODTK7Q3YluSkrSUVp6z23Du3BsQiOJ4yoYEBhylrKKtCetCGza36lz4AleLleNo1PuGLXx3eGz2CKJJ-SqjLlNl9-QuHryHU7DOsNkruP0I0_Jh0Uml48aHnBSJl8TNzD2_rzQ5CFhtdPSmnGkYE1VKXSoOlaK56KfeMpWbpglVN0bfC749THs0g7howXDt-OagvL-yUcEekHlfATSaQud93wIeLJwc5cjfsd9KKbuCVg7hc7OmUq8y9ZsDjNQZdI6xRjF-9J4RAryRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jx124QX21LkGaJcEvg4ksDdmsBi84CCml9KTjxoWQ20Dne1Sht2d_S_DqHiBaPFfbswoYtni8FpK853wntlr1OsYQQWZabyvYnvI8S7EMiJwqvDXej4K6p4Y3xTBMmqzf8PhRaWN2j2uE2GYiEYCPsvx5CFHL9XVvdrwXXhxdmc5SroQbkpTKQVW5kaakaMAp893ImV6MsU9eyFda5Gt1n-bTSXSucS1vp78SKjI2ZwzdkCQZ9RNuCZPdxyf-8OAkaEU7onoPKIt4_MQa9waCSlRA0e-RBmOZplzaWsQFPnUAB6x-n41YtlC-E_-fuY4PwMrFgy-wwfxYVc209-SpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9SZkd5sLApzOZ-r-ZaWEht65m2UY7g5EdetJ7R1ySYCEYbTfcyUSdWI6hyS3sSt-Fqp4fqyWE0zneb9n23MH3iokn8sB3NU6F6yAB3BwD9-30uIsNZ-BGKoNEzE_KBPg2yjKW7REH3kk_1WYo7EfvCjF6cY4xv7bCyg3TSF7JtqOGntWEqXraXEsokfT8005Lxpla00alvRTovARRCk3gipeAHyABJ-32sjqv1l0ZBY0oKhh-zNg5aub2-yMpZet4hlIevt16S5_QCm6ZrezZPj4nsxHvMgwcJ4TWtTBq5l1Z6tXZphrt9aH00sXxnf4FvAM79GvWs847B3DebOVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coHPI7hhHPyz5Wn1QkDdu3nA3HUPHcXUVGZ2RilU3QW-q0M4BJq_tljrcaJRhNfneqSW-1JUpQzH7DZ4hpOrb2AJmdPxjDbRExNkWegI7AUbvusrDm8vyuekG5Wc5o3b28vRYdBe0kf15NZV-XjMLjuraFpNio_PLhfxSP-ndud36zHhRpc6tPmMItUIaGBeLqa2yUpDQ7ON6OANgj6RMNoyb2DHI5cKj4TFlAxTY9HyE3FY8fLdsDW2m3iFvtI5jDOE6bAG-1kEb9N3qE2OV11uYup0xqJiWn3gKI9GNnlf0qwspdkyKfPQeHqJ8k-9ZCXJkntg2SyxytSh2sScPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=eo5jG0Wxh_iP6aaPLIwNautUpJVdtkcHoY2eMPRsyC9OCcCvexDlvs6owlhZDRLNBe5dkcNvQmyLZKmWE0E3GVZ0WKwJXNqK0W0yaNXQiWKK-fhf1OhwelGRisrxP_5EBb9FwRc5giHWY4jdj-2BU1gdjrfwQOq3uaXmUgdw1KOJtPx6279Ib77yrcd1xBB56WU8O8GwOZRasikwSSiBNkRgEVcWqwzb4_eGSE_-vz1UcK5oB6EWHOSHi3xHVONcPtCHC3ojTu-XgthZ0rjVfnDGFbANRl4RR0_R58sOZCCbwawCV8ZeE3PGNHpdOgOW4g2uEwQzOqoMGnWh34nbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=eo5jG0Wxh_iP6aaPLIwNautUpJVdtkcHoY2eMPRsyC9OCcCvexDlvs6owlhZDRLNBe5dkcNvQmyLZKmWE0E3GVZ0WKwJXNqK0W0yaNXQiWKK-fhf1OhwelGRisrxP_5EBb9FwRc5giHWY4jdj-2BU1gdjrfwQOq3uaXmUgdw1KOJtPx6279Ib77yrcd1xBB56WU8O8GwOZRasikwSSiBNkRgEVcWqwzb4_eGSE_-vz1UcK5oB6EWHOSHi3xHVONcPtCHC3ojTu-XgthZ0rjVfnDGFbANRl4RR0_R58sOZCCbwawCV8ZeE3PGNHpdOgOW4g2uEwQzOqoMGnWh34nbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhIuZm4gy19iIpyXGjfaO39pYwesW_G7KtIIXGwMkh8XsdfotseGuZU8O3FQGdaC6bqYni2PymHWgmdJgXbjKg2pC7LsOJZoeIuy0mHVw8a7uR-SvjucFgzlYOfnewLIWXkyvv2hp2DyqKdXsNZ1KpGVfShemgY-GA86Zbgk2OnnzvAjxzMjNY_KLAZ071qu7pN88NQqokjBQ56FpWPqHjNUbSPg3w72EIGccTJbW5Xw2OnUUSVkwrTDA1LxMcemtUfqZUSxZ08RjS3WX8YL1FjRNAETDz5rh47IqquvnCmYxFRA7r0p4rnvgANRzfc0o2hJTsCErNOmSO-Z6j5Y9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=uaJz2vNHj-x3q_jUqp6uoYsAMl3j78mpb5JepxkeZcMFMP7QGV4az8xJyfibGh58RFGf-EzHCU0LVvJiNQIPbwZC-kWQOeDClav6i5QtZ59ABNn89fDSzNr2eBC3TQcSn23XrJJL6XZRS9u0NX6pQ8oujygNbngxqhkRh2qJHf99o8PlnuIaWBMnmUkh1kblUgh2MydA32WMAaa2DlXiAb5GWRfhLsmoTK9YyB4vQYU9D02HKeA2KKFebIYEhKvm6g436tTIkUp0_LcLhi0_f6wLPC0cPibOf4xefJgGNqOUQmtHn7NUtfzm3YxG_gowKxuCeY_RPiS2zMoNHl3oNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=uaJz2vNHj-x3q_jUqp6uoYsAMl3j78mpb5JepxkeZcMFMP7QGV4az8xJyfibGh58RFGf-EzHCU0LVvJiNQIPbwZC-kWQOeDClav6i5QtZ59ABNn89fDSzNr2eBC3TQcSn23XrJJL6XZRS9u0NX6pQ8oujygNbngxqhkRh2qJHf99o8PlnuIaWBMnmUkh1kblUgh2MydA32WMAaa2DlXiAb5GWRfhLsmoTK9YyB4vQYU9D02HKeA2KKFebIYEhKvm6g436tTIkUp0_LcLhi0_f6wLPC0cPibOf4xefJgGNqOUQmtHn7NUtfzm3YxG_gowKxuCeY_RPiS2zMoNHl3oNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paPNS_A0eUZRGINmrEkRbk5-2FY5KRW-Iohh0fKLmRKhbzkzicTVy8EL4QN6WezYYhu8n-LjeCVjAvuKnrbQnZ_T6cWNl57GzFIfAS4pMzxwY4w8_J0aFYM0Vhcp9EvU6khdYMWLuqoCSQ4Hmoe2vfb-mWVRuxfbdIJDgt32BZcDqoOESfxdL7uaAuEUjIjEkMYDWcKfBDgeqy5aqyScTzB1eu8gqojziLvFhMSGgqU895O4Ks9jwZDHRVLH5YfqOwfvdLPbe7HFYFM0EHftysXTefHZG7s-rUu2dar7TOorpOTqlR6lSerBH74m1gamHhyED-1wGnldhqV4EtNsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=f3xq9W56ccWPylLOqaI-7PUtJNq7NzGfdAPurh9N1D42bkNusJ6XIFc661EUnN3VFowHsqpFLavbTCDXjJSOms8wTwqepSB88PF-E2gQU_B87S1hmHCfLRuxwuFMm8-sLbCzyMnLnvHD2yAlbMQsqFekepq0UgfWtbe2Kcm7gqfyxTA3mCpcJqSjEMRleaJVoZv0p7zxhw1JsjTX8rN8yVqgpzzbmE8Zctj_cr6pSVH8D49qugIlrTkOd6TWIz6Pfb8b9c7xCc-TkYMyy8a2d3ILyZDu-nguWW5EumCwGOA753Ekgbe6j2fztoB98_SxPcocuHgcSdxN81gYcTFE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=f3xq9W56ccWPylLOqaI-7PUtJNq7NzGfdAPurh9N1D42bkNusJ6XIFc661EUnN3VFowHsqpFLavbTCDXjJSOms8wTwqepSB88PF-E2gQU_B87S1hmHCfLRuxwuFMm8-sLbCzyMnLnvHD2yAlbMQsqFekepq0UgfWtbe2Kcm7gqfyxTA3mCpcJqSjEMRleaJVoZv0p7zxhw1JsjTX8rN8yVqgpzzbmE8Zctj_cr6pSVH8D49qugIlrTkOd6TWIz6Pfb8b9c7xCc-TkYMyy8a2d3ILyZDu-nguWW5EumCwGOA753Ekgbe6j2fztoB98_SxPcocuHgcSdxN81gYcTFE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=kJsSZ4BgMxQ0ECWy1HK_6IUWDwB4V4IsnQD02xQawOaXaF4_W6MesNdRQjadKRG_5f2tFgeSPtnON1h-JRe9zLp1IMu81Gbp3eYFzYmQd3NRj6baKHsJMBX_rEsNgAQJtSOEUAXZ1J5MT1YA_a2tZ7mBYwx9odw1BemXLt1VIpX4I5RSfYaosqWH72Ay1nIWSjPpkioqr6nzXAUBysUD7qb2N5gJQ5s9aZRLBnnCDOPKnCt6rVC3Fzgg0S5kpkCTnmWSx2De5ZCbdZ9Ivn-aIJ59rCUSCT8zuMVSF2mR0J7dbiGqNoAcN2T5MdTB1oj6GvjBvVriOq8qnc4WGlXAy4wzBx4g-bzDQ4D6BOJi2VZvbwcQ7GLgq1Y4Ie72zNneS_ey1ibcfTSP7gPrtel8Rdx5Zjf_hFOE2jy4sxF5HseS66n9xkMZwUjYcZsO6bMEW5qvIooJV-cDkHxOu9b035Psahk_dYsTTVwItR8jbUphzDjLtOGjQhjbgziEn6C6o_7yghGdrKvUgnceE7p40rAaLdMslRFVaqt2krv3pY4okoh6vEWH8KMALp6g_y_KWpQESgz9w08ivbrGhceO5K0cRfkxyNPV0dz7cCHnWBZtj3CWm4BN6ILASgI0OV8w5kyT8bCf8JumiEBJ61hGQXtYRe26p6lWMSxYXGZ-uA4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=kJsSZ4BgMxQ0ECWy1HK_6IUWDwB4V4IsnQD02xQawOaXaF4_W6MesNdRQjadKRG_5f2tFgeSPtnON1h-JRe9zLp1IMu81Gbp3eYFzYmQd3NRj6baKHsJMBX_rEsNgAQJtSOEUAXZ1J5MT1YA_a2tZ7mBYwx9odw1BemXLt1VIpX4I5RSfYaosqWH72Ay1nIWSjPpkioqr6nzXAUBysUD7qb2N5gJQ5s9aZRLBnnCDOPKnCt6rVC3Fzgg0S5kpkCTnmWSx2De5ZCbdZ9Ivn-aIJ59rCUSCT8zuMVSF2mR0J7dbiGqNoAcN2T5MdTB1oj6GvjBvVriOq8qnc4WGlXAy4wzBx4g-bzDQ4D6BOJi2VZvbwcQ7GLgq1Y4Ie72zNneS_ey1ibcfTSP7gPrtel8Rdx5Zjf_hFOE2jy4sxF5HseS66n9xkMZwUjYcZsO6bMEW5qvIooJV-cDkHxOu9b035Psahk_dYsTTVwItR8jbUphzDjLtOGjQhjbgziEn6C6o_7yghGdrKvUgnceE7p40rAaLdMslRFVaqt2krv3pY4okoh6vEWH8KMALp6g_y_KWpQESgz9w08ivbrGhceO5K0cRfkxyNPV0dz7cCHnWBZtj3CWm4BN6ILASgI0OV8w5kyT8bCf8JumiEBJ61hGQXtYRe26p6lWMSxYXGZ-uA4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiShpjK0E4drEaxgLe9eUsxcQK2iSqnOU7HrVE3ufRgJVmCQ1UGW_4WFnJIvgRn7P2y4a0sHcMj--NxOJmY-0fent2ClQB0lkjNXR4Y901s5z-H4Wh_7Qx5dNUccjiAmAm_4mnd-RPKAswiBOtvkLp-CpszxdTZbMUh0Jg696J1tGpJofgHhiVsbSv_oQWmLhYCF7qxG_ijhYaMFU035Vlm0TxDrok3iOkFq0e6KUhdoG_Kf8h5D_ING6G34pmfem3edn--DTxsszv3BPzmGC2X-G2ECzUMqU9x0h1xRe7YGRN3UtG4diByQR-Td_w2sOhWziu2xvTbZiHoXCi1lBfVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=aX5sjIzMJeFRePL6yXI4ctxjrlGL9yM88Xyi6xak76ErVVP0WncZHvn7zXD11_u8AfAU7nW0lSapA2oVZ1g1iy_EcRpXVZbuRC7xqTOgAEaQ-Coz64rgMDmoQ-zzDhlZ5-p1gCzqwXi7W8sx7ZVT6u835RoJ-T7ytmM2wua2ovnkC64vxZtHkKI56mWiuniBFsoROUkwHDiJROOj5GtdlOFus66EQNDol40Iz_2q9FcDgJhtnKs2fvrFuiUayjABhl_TqtOovzWhDyO8hiv1WSM1iXJvTjxW-hgrd0vSCDAAqzEbbZ0YHEWspC-PZBwV1-T7BDmWdor8SPTDlECoiShpjK0E4drEaxgLe9eUsxcQK2iSqnOU7HrVE3ufRgJVmCQ1UGW_4WFnJIvgRn7P2y4a0sHcMj--NxOJmY-0fent2ClQB0lkjNXR4Y901s5z-H4Wh_7Qx5dNUccjiAmAm_4mnd-RPKAswiBOtvkLp-CpszxdTZbMUh0Jg696J1tGpJofgHhiVsbSv_oQWmLhYCF7qxG_ijhYaMFU035Vlm0TxDrok3iOkFq0e6KUhdoG_Kf8h5D_ING6G34pmfem3edn--DTxsszv3BPzmGC2X-G2ECzUMqU9x0h1xRe7YGRN3UtG4diByQR-Td_w2sOhWziu2xvTbZiHoXCi1lBfVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g7U3_MYzfUE4r4hwlOuC7VgsODD9ZuDXMBfeoDfsxTOa9azNYMye-E2_ZwaeInTcqFIAI_qtK-stv57Oh8Ba_U3UWWTRYgDKzMWK9OmkFMCWzBpA4slcn9fpCtdK65oc44A8q15r0WFwDMvhxZeEZz7O0PipoDqMcNpiN9qwmiOE03tKaW9lEyqhmAeQC8z56-Dbd5YM7Cv2LDDA_UzbUonwvsj6pWvCINYeMcv86ilNCNtM7dPYN4gGBGAKCU0Ar0U_dpm9QUhhsL9up0MssL7q440bQ0HEi7E2NGvbjLk9IUZyRE6MRvhEIC5U5vtzMmbGVvekjYlYkUvfJfSSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=XhHfwQwQ0WjE_DND1LchXp2pbF66v_6lusreNCWWBtPeNmJ1HYAIdA5vow6vK9w8qI3nh4Xrlrq6LXjQ9ylFOAWPkhpvPhlHWlAEFn7CtB7oVcvhw9nBRJk908l6LFmo-1DykMvUTfuMBWv8AVPc50mqSyfd81Xf0EvaXljnmwOcmlkwKUjXAe0odjg1ouLwRj7m4IoHcQWOYAs_GJi7sWmHLyUt0YG-q06RyeuvoYJf5bOW-xsSaXrNOpJrjSor5ptCUuJY-odKVMivcJZAfvSOzXtqSTda9MMitdhjcBQBodwcF03tY-2aTrG6Zm1OPCKYFesiB7eAA9qgkxhCYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=XhHfwQwQ0WjE_DND1LchXp2pbF66v_6lusreNCWWBtPeNmJ1HYAIdA5vow6vK9w8qI3nh4Xrlrq6LXjQ9ylFOAWPkhpvPhlHWlAEFn7CtB7oVcvhw9nBRJk908l6LFmo-1DykMvUTfuMBWv8AVPc50mqSyfd81Xf0EvaXljnmwOcmlkwKUjXAe0odjg1ouLwRj7m4IoHcQWOYAs_GJi7sWmHLyUt0YG-q06RyeuvoYJf5bOW-xsSaXrNOpJrjSor5ptCUuJY-odKVMivcJZAfvSOzXtqSTda9MMitdhjcBQBodwcF03tY-2aTrG6Zm1OPCKYFesiB7eAA9qgkxhCYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=jBPW-tUFjHrisfWY8GoXWOUrgHM6aEC_VC8UhO0OmboyBaycwraLlJGDbXfEo-feHurHGm3WVOBTtX34LqQzlRzC1wbMguaoVEK5tdDJnFM2olEcmbFx7P0LrgAHO2y_oCk4EuGd9lH8qqC-pHi4W0fRahc4nlxDfKhM4l1mfY9bkBLEya6RvbZzEnShrrRT4C6EH1lXDxFcWMeROvu3ZHIcqDTf3uOGUcmDAsQbGV6svuppN7DjHeErPEc7FzyRhrp02nFfcvnvwFPhjGsI4st78uUn6Bhn71vAXKnQs6qESO2pACCtTABYw-NoKwDsQICDbJScS1Wc6QhzJ5cA0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=jBPW-tUFjHrisfWY8GoXWOUrgHM6aEC_VC8UhO0OmboyBaycwraLlJGDbXfEo-feHurHGm3WVOBTtX34LqQzlRzC1wbMguaoVEK5tdDJnFM2olEcmbFx7P0LrgAHO2y_oCk4EuGd9lH8qqC-pHi4W0fRahc4nlxDfKhM4l1mfY9bkBLEya6RvbZzEnShrrRT4C6EH1lXDxFcWMeROvu3ZHIcqDTf3uOGUcmDAsQbGV6svuppN7DjHeErPEc7FzyRhrp02nFfcvnvwFPhjGsI4st78uUn6Bhn71vAXKnQs6qESO2pACCtTABYw-NoKwDsQICDbJScS1Wc6QhzJ5cA0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=Wp-Qp-MwBuwchZnw-rc9SQ_mZzYnYcGMUf5DPJWZBEr0Y91pFoMB2Ik6XCa9YNEMfOt7JcNmWB7i6WMbRgZWbvZVZLoDN-t4qW8Lp9-ii-uJwnd1zkt523jJCC3TC5GM0nkxf_XLQmwxzZ9ajFX1Cltopnrqri8Ehx-FibzeEOMtpD14XF3QvGPlMewjBpR2dO_cgkd2Ad7eDPmB5b3nfNnxduG43IDL3Dsl7v-BO_pI-BZfhBCobBFVNCPK4h72QqFGPKelhOSwStfUZ_DShEWZUAaXHXtqmSfmlH0nPafyt6FWpXVbl18OIr12iE319yopUs7x9X-HZpm9qH8pNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=Wp-Qp-MwBuwchZnw-rc9SQ_mZzYnYcGMUf5DPJWZBEr0Y91pFoMB2Ik6XCa9YNEMfOt7JcNmWB7i6WMbRgZWbvZVZLoDN-t4qW8Lp9-ii-uJwnd1zkt523jJCC3TC5GM0nkxf_XLQmwxzZ9ajFX1Cltopnrqri8Ehx-FibzeEOMtpD14XF3QvGPlMewjBpR2dO_cgkd2Ad7eDPmB5b3nfNnxduG43IDL3Dsl7v-BO_pI-BZfhBCobBFVNCPK4h72QqFGPKelhOSwStfUZ_DShEWZUAaXHXtqmSfmlH0nPafyt6FWpXVbl18OIr12iE319yopUs7x9X-HZpm9qH8pNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ac6tZwwY-RLLXdVz4-fGIIuJ4lScFTpojC2X2KVhUKq0dRaBGHxjzZxs7L3NVAJglA3caum2dlAw3XbhkAHiW-8evxFZYKUkrovrBScj52jMasDEsW42GMwhEa1ub-OtOrMNhYM26_6K69JrgEgFgObMGDXXpWHSakVmyUGC2wWbkXLT358WDInwd1CgrbWpkU5E3kVN_Ig9m55hCOP6UnozD77tLIQsQzSrlXSj3UB8NTtQD4cRYqXTxc3cahUW19bdyVmYOqiXIPaW0JWcNMTVWfgLKmz_QoiBV-z87qfmVG5bzLi_CPiHyb6Ya2Ub18MKgf1euwNcMNt2IYvAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
