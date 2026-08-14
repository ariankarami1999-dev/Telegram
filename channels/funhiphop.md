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
<img src="https://cdn4.telesco.pe/file/mx8GcXtAhVdSzQLYhWFAigUkwdsmLCPqp2TfDAaB6Q4fTOK-K_Kf3M6EgzHWKWxBMbRXks5WKspsWHvVlpO4cXSosm-OTitviP7KJoaIITwjOYSggnjH6y-xpXdGafzoccOkKJoqbicjyvxuLiJRaCjtxRlCF6bgd5SsKA_4hFpwxmpJzCP1s-JavHDLbc9rdemvcPKhlbUJAcQqsVNaVPmxYKopT6Yivg1sr6C7QV7SAqC8Th3GafGX27rVa8H124sS3k_28SgCEQf9LiQUxh1Qn4cNqU6oN9ybe_Ry1B-zdvdAp5JYUCa76cvQUdFDH7I4egEhjQSi6m4BjNiu1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-23 21:42:30</div>
<hr>

<div class="tg-post" id="msg-82206">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop | TemSah</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/82206" target="_blank">📅 21:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82205">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4BoPa_Nx72GD7iDDifBwYpvMfviscBn_s-Z7dySAk11oUEIP93HKTwYXYUeVsV1C6-DU34xFfRLRv279p9b5iYecsBdQDnzcr0Uz5Z9DMXGnBvJHUtMIkINhHezHDLz4HeSvPEgREwO0j4ft1OKvCqKdzbMFP3oKwzdJd5CDKJmhjqqsZlyiee15EoooOi0fIXTrUfMPAJvJPZHjb-9f6LSnvuCRpRKMqlFw5BFgl7BdynMlw35BbOAIz5Xqs69_1ejH5-IQWJq8bwqNr19UqxVLdEQ0gcpn8mxjD0OEwIyG2x9WLvnEAGHA0iszrPEvCDVQJqsb0fnIaKdS0cJSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیارو
🔥
جذابیتو
🔥
گلارو
🔥
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/funhiphop/82205" target="_blank">📅 20:41 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82204">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjP7FnZ4xIO-T6SESs4JvmKaUT6xA5aGAA7Y17eNqxt-jODbGh2GV5f2tIj2RhI4jHmrG1Pr_eoxhJSVs945QKR7nYkSuipbnpQ_n-VWR34yvrPdVv1xB3s3sqSQ3AtOxSwmsVej_N6-b3uNtRxLWWDLTzmtgxbnQAUyQCgQ5jSHJePmSrIyk8vumc__2JNO9Tb0Fsfnqytqp9UcXa9vlM_nKnEQQATsZ8_TSGVIRUJpoXvaUiv2-MDzjNv0ET75WqvU32vz0PiLNN8yqvVdAH_kLuawD8hcB5NLIwPk6fGVRPlBx7PKxlWjaXPtgMVwIC1_QibtRrQV1AKeYEyLSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
از نسخه افغانی دیجیکالا به نام افغان بازار رونمایی شد :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/82204" target="_blank">📅 20:35 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82203">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtxJQgoK-FAr6nnKeaVcjvte_yxUfbERzejn_dELsu4sPZKz1KT_eHuePwA1CLt_7qS3C9Evmykrz0FI5ZMuN6rqAOwrpdNqzR0nvfZNBFYkHi7209q0G9d3BGVed6Oa97yse_6SmL03F_QfJBdkgtDX5gxrPyQfj4ibeYxexYI1ec0QFAAiKlQxmHSbOPA9vGaEE7FBZQuno3rcTmmY3dF6VGlzH-nEi_o1npAau6brAkrOIneRQXrQRnbmP9kJ36mwyzYLm_OxwGCOLplfnoVBIz1eYvYrYDvjJmGZX_oKufGsjc73nlP280mzL8vTShdRExWLdiwpYOJ3FQyYqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قسمتی از وضعیت جامعه از زبان پرستار بیمارستان :
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/82203" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82202">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrwNa7_Ay9thTU7DGStL7AHLuiXXqgMnBE-ipV1ItGaURAjoi1F7g73xby5ZpNqWfODGBwYU_sIaZrLNKnqRxRXdWMKaOwv9Cx2XxN9PeGXMKNTuiDrUCkf8D2scb-HoDiCxNbt29zIFJDEVSmm0xg40GitRs1B8nEMJH9m549_JzFYg2Fl4cp15B7lqLOnm7LwcpJdkISEH62l3Cl6fnF0PUxlMjOMKpvvNGrm7fUmmp3UzmWTxx4tjyXotd38UVLuWbe__XUtACEsqekT2TChF_0JeksLahBM9CZcSN2YSNFrdcn__pxyczBki3EDoS1FC3HAF4jZzKZF1DNOKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
21
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/82202" target="_blank">📅 20:33 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82201">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ بزن که باز این لیگ کیری ایران شروع شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/82201" target="_blank">📅 20:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82200">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">چند روزه اینترنت  ایرانسل کشور اختلال شدیدی خورده
یه تست ازین ربات بگیرید خیلیا میگن وصله
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/82200" target="_blank">📅 20:08 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lyNEjtOoS6VnOnU11kvRCcU6PieVd6rlOWxJa__dxcrSjNhRC96OmdGxr-HGKHypfSGx9tAVrRPKkX2aERpXdTU-q4c0WuoIP7XfkZrzOady6dbo0eQy-ryXvvkTWK40ameiajv6LK69cB2zeGxMZQFD7HK2k0cNFJNWpxF34OShB9EFZ-8MLAiuIByJcZZQ1kuuWQLC4EMsAiHnxEc3XTUjY67KDKyKzD5FBBmZ-mP5tXrp_2mX9GUYi3woaVeBAVxycX2sG2LydD_StHbNB8WQdJYprgUOQ8LP60SIWxiYarN4FIIBcUlafg3bZR8dbcwOzvtRl1fzpTF0mbw2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/82198" target="_blank">📅 19:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwtyQHazrOzNs-gdkhKJCCYp66wQzvCFsLWqJMicG8Mx2uZQacNPfrZS5B3eUCy_4VwJdPNo53rcgxIat-OeuBAn7Bv-nGL0OH0o8CaliQhYi7MU9SXEq6Wc6e8lQ-nGzh7-XjahG0RQPYiqU6lu5D4cJOEg4dD5SqElgcBSkecbGlZ2diNMZQ02xPkP6d3CvugRbP-GF2Wj9m74zRax0oHr_8o-b7CcRvSLexq2CVdaHR60PDLle435hXbDzq3nKCS575LVtLSpoKjhu2HiwIDOiNArQmOt3dgh-KWuKK1Yfnlx6nXD4ut6U48wqrNYKp-zSaMYInzYJTDnyq38nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه قهرمان‌ها شنل نمی‌پوشن
بانی بلو گفته موقع ضبط فیلم سوپرش با 1000 تا مرد تو کمتر از 24 ساعت، وقتی یکی از اون مردها شلوارشو میکشه پایین، بقیه شروع میکنن به مسخره کردن سایز کیرش و بهش میگن دول موشی ولی ایشون که تحمل همچین محیط کاری سمی و تمسخرآمیزی رو نداشته فورا دستور میده تا اونایی که مسخره میکردن رو از اتاق بیرون کنن و بعد به اون مرده دلداری میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/82197" target="_blank">📅 17:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DI2QsH05peT957sztxVpoB2-XZenqcxP25AqQ6utKkw-HPbeZ5TBK1quvvQtB9WdpbcFXJzo2q8VjoCtm7FQPEZMtUQWa9oeV73nhxWcDxSl3wF6hgGHm3Lq6SCRggLIvF1RR26DAV7iagPelnp8X-ziXxBzeJqrlUet9s4iQRb4O_eQRwRXdAyFGx7IxiwGt9W16MOLkyQ2Twcc-bY4msKDiagq1tr9FLgVOTBDq9AKAbmxo66EipzVqhbX55kiTH7omg_7G7wFalsUhqAYESrn7iGBKKGNiZ0YTfYw1gA7SES3P9QOmRb_GCGJpdSqj-L9Acsl196-w0fBUtG5yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس اکوادور ۵۴۰ کیلو کوکائین کشف و ضبط کرده که تصویر هالند روشون چاپ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/82196" target="_blank">📅 16:09 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=mtaPvXSy-45DMaIe-0hMAk0CgCvfTkQqrFFJXQ5ql8JF51JBolUQ2gQa_DKgAQDeHkecFqqsYglGt_U8_3bRWQhH_XjzY5TvbM5CkFHV7G6zZk5w7b31_5tLAgU_AHBblvi4ewCqFjeUQzY1juY4VYc9dGPL7IcGYYPwOUcbIMK_G8MISsjoWguW2whKZrXAZE0-yVwqIyeigQGlIFDf8z35NLlTFpcLeno_wMjdsJ2ApSXQCr26V5hzyWWIVSnGPpKpzNx23vpNEpFZloPApLpRFju3Y6j1jNMFGoWePJPFHsWgkvDci9dQvvVmKTyxMkRLuMJ24QF_gYz9fkS-LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a38487cf4.mp4?token=mtaPvXSy-45DMaIe-0hMAk0CgCvfTkQqrFFJXQ5ql8JF51JBolUQ2gQa_DKgAQDeHkecFqqsYglGt_U8_3bRWQhH_XjzY5TvbM5CkFHV7G6zZk5w7b31_5tLAgU_AHBblvi4ewCqFjeUQzY1juY4VYc9dGPL7IcGYYPwOUcbIMK_G8MISsjoWguW2whKZrXAZE0-yVwqIyeigQGlIFDf8z35NLlTFpcLeno_wMjdsJ2ApSXQCr26V5hzyWWIVSnGPpKpzNx23vpNEpFZloPApLpRFju3Y6j1jNMFGoWePJPFHsWgkvDci9dQvvVmKTyxMkRLuMJ24QF_gYz9fkS-LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدایا ببین من نمیخوام برم جهنم، ولی یارو اینجوری پوستر درست کرده حق ندارم بخندم؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82195" target="_blank">📅 15:10 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بنزین آزاد قراره ۱۰هزارتومن بشه، فدایی حرومزاده رو دیس کنید همش تقصیر اونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/82194" target="_blank">📅 14:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVpN681qnhXatnrUlPZV3w4U6zoUrR68QEdkEDmYKP73xDcdli7N0fdYape2tDNwXsw-bnvqf6SuCqx5cY1egnwk41W7Gz2-WrjLTYJlV03ZGqv_Iy0P0c381Ly6vVtqZ50BuS1_q7siv3ka2i_Yw0U_dDgsw4mQw3q56RLXhjuzx6dw9emVQiIvqEi3r_YkigbxOruTHztcER4mHGQUTBHXcMmPvg-dpCoADmBBphciOFlvF2L23mxRFRlVlTHBHlSOzo6NU-rpqIfvTm2NSOtmnzEUB1UDljWggbZO-EKrq_tfZUElMh-HcREvKCCpyNec8pkTa6bJtvJdhlOiOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیش سال از این شاهکار گذشت و اما بارسای قدرتمند اون دوران با حضور مسی که نذاشت بایرن گل نهم رو بزنه
🔥
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82193" target="_blank">📅 14:26 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو اگه منو میخواستی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82192" target="_blank">📅 14:06 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">7Khat – Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82191" target="_blank">📅 13:20 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Maye Bede ( ft. Hichkas & Makhmase )(2007) - @SCDownbot</div>
  <div class="tg-doc-extra">7Khat</div>
</div>
<a href="https://t.me/funhiphop/82190" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بخدا خود هیچکس یادش نبود همچین ترکی داره، بعد ممد ازش سمپل کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82190" target="_blank">📅 13:15 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82189" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82188">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iRybU_5qsPnsqtd2hbuKzv9UnDvCaOuEZHxNecUiWha0zwUfPcRkeUavUTGQPyu5kcAJcrpobLJU3SL9a4fJGbVhfr6-jvmJSiwoAuXgcD1QVZ1O1Xi4EdwPB6iTOUCVaQqVPvfDNY1GfT84oxw-n1f7UY5uGPsm-A9y-GZVlPQAe_0KP6p86K_DjvOpcHCftxnW_35n_eE38TaTnALL1y6e5Z8XNcaWwJKxqS_XVkplcuJIGSVRXUVZKbRPPqDIqPvW_J9NjFH4hQT-QgJlYPhj9cE_UvGeBY0G3rw5Hhg54UcpHSPc2XPun-w5TsK9YIHHGDTdVCWh8yOCyKzgCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ممد تونی به نام "مایه بده" منتشر شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82188" target="_blank">📅 13:13 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82187">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO0X_RTtRlv4yLrKhqkyAXo1Zzx0Uiv-GARgs_XNyxrcfKXJkZou5pBdpdweSjyn9I5eqb3NrjPszj-OSnXqTR2GenSJsI5CYJxxWEqE6YQkXDYoygEI91jXlqbbOKtg68futtHqaqyg-mjW1IGuUnT1wwyC3l_05C7KBTvDI8poDce3KDe7EzH4hn6SR9Apw0hFtizYi0DPoNRYlbGvlSVef_6rtDdgZvONrDj8LWoupRwA2gWbOxuXJNBYuDS6dQcKpl4oju5uinLuAMlp9wYDj7wQpo7F5q6W61Mxg64JmtgVPiQl2vkxQ2l9azFnqGG5maHjZcufOlbZ_fa_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد روبیو و ونس  ترامپ مسائل ایران رو سپرده به این یارو که در عین حال گی هم هست و شوهر داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82187" target="_blank">📅 11:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82186">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vQr4sD3iI3jTZ6o91qU5SNS32cPBkdZ2Gmw2u4ZppcAUshm014pzxtbZhF3RD3e398-3SMfXE4AEM9WcQkIZQdfBx10wV2R1zF-Gtf7VYrwQHY4KtwegXIEoGFj9PEUw62tC73ZkeAxMtoth2lEzJMva0ulvMTjILc-1ucmokfjmpL2lUTIr0kJDrM5Lm_Dn5lPy4h9MM2rWjiWyjGrF3OVdPcXyS2LpL9FFilMtmOyNvZi5y677ozk2t4QQJbyyMusi3XvCtnrMTvprUTToJcOrEJh-0eGSaKTviMYQ8eWZINHRKBqfWsPz78bUj3pVD-xXgMei_Mmm64qllJ-qsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون یه پلشت بی فرهنگ کون اینو نداره ۱۰۰ متر جلوتر پارک کنه و پیاده برگرده عقب، ماشینو ول میکنه وسط خیابون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82186" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82185">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkKAB2c3glLYDpT1OUpY018g1qi6fMHmJ8iajTJAj7ua5o1O5VOE-tDoSxgE2o5lHYU5o0_yRtyrxv9lSPxEqV1ZQ5JQvupMi_OG6VyXNVqJ5WzT1-xVwCrVGAjGPyKp-Via6XoY63tFAKyQ97YKCD7o13PjHbccFe5rIizUWkV0tYvh7EaBR2c6I6lOhdBnxkn-NJiKb3EtsdTyUEprFXshLQuzCtGDeS4Uu5l4SYeTHCbSQQmxcqN0N0atM6lmJJ7eOVxRggir9xxnBV9JoJFCW2NLuFGaeXwCcBrLh_CCY0-vquxIDFqyo4Y6Wuz04hrXxxO7MeTUw543Obne-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تراکتور
🔴
-
⚪️
پیکان
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
جمعه ساعت ۱۸:۰۰
🏟
ورزشگاه یادگار امام، تبریز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز+
📊
نکاتی در مورد بازی‌های رودررو:
در ۱۰ تقابل اخیر، ۵ برد سهم تراکتور و ۱ برد سهم پیکان بوده و ۴ دیدار نیز با نتیجه تساوی به پایان رسیده است.
🧠
قبل از شروع، سقف مبلغ و زمان‌تان را تعیین کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r23
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82185" target="_blank">📅 11:30 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82184">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAgK5jTyzYRRaus0TXczZlGj3axbra2P-ytfFWx5P3YNMIsiMlOnEyHJWNqUHWv7mfHNUI262h8aKENBKkHPuyGVq9yh8E0TUJo3Lj-hUN8cwFEhv7RYcXY80wDv86wOrfVctiNvGsBPDGIMFH_Cgd2V_xMjVerC3M2ZmRIv7VbthhYiPFBbQ8J5jPTfYQzPSszNbML6juaKdYrUL3aQva6qNg2GA70XQzCIzeaMx3pMK__oXuuz_o5xqrvcj_acOuEzsba-WDCkYsUKXG6zgfV4atUrWM6vk16_FsSyr5y2X3tQjzRKR2Cm_zMu0qYD0JS-F4RAZe2oRvX__EBv2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز بیشتر پشمام می‌ریزه از ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/82184" target="_blank">📅 10:54 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82183">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j791efj2N-kkCVcH43U2dqPBDb7ZeoU6ZwiqrhCYuJjoz0GioennyGOrst3Jn8eRCkTvhF0PtUHGYKUFQMKqdShUsXZcUudmkR6Zo-6Emv_9BvIlugH5N_kMGsBtm07ywv_jD0mfOAHLbN6wbcV9cF0wtyM30-teluqW6e7F43wKIRzUOTfxcdbmCm6VrLhxtgNa070GS7caJv-UiM3W-fJQEDkGGbkrXRVBlqvWNUt6AKUeUwrR16v55oCs9_PCaKDhck3sCGyzMC6Cg2iOA6twU8IuaTYWdt85QMAxP7SIfsYEr9hDRSj12PBsBOD_DCr5eYEu9TqYM1oCT2kwyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا که جای مغز تو کلتون ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82183" target="_blank">📅 10:39 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82182">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82182" target="_blank">📅 04:44 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82181">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULBhW15QCQwWP_JeqTA15N4BVQlzX-DJitX7Oo56aLTtV0K4lXWMrJd9-1cWT88JUh1CdntrCrAb9Ik1ggBRqK0cV-CMgnvgexv2jPCw00N1PNbIzrtsWTP4NW1N67hOxsyLLbs5CMYLw-2OYJ01S4GNFEChoEA0G4P_nwHCVo48nz3moLAhymGgVj-48kAZV4VSoOnkmJFLmTTDtilxDX_WMteMH_SqF450Wt91uOgimt2AU_XV49e2Qn4I9GyOEtUF7JdXu41oR0mIvjnJADpsJBItMauu0cM3koXLauntsRTYHkhRjJ-z4_veqdcuEx-Qswz1qBK7AiS-XaAcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اگه رستوران بزنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82181" target="_blank">📅 02:51 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82180">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBOKQHctaEEN1CivFE69SkS8YhScBVMzyaefIQyUCivesjgMDOQD9wNcPIomIBVLGI7ykfSPMlkIEXdVeAvEI_q0GPhLkYBlyWvM8dRhWH0nYgtV2Z7wWBkzEBTwIUAAvzWsNHxXlDVcdSUfbjNbliyVHT2FWMVu5x1kRUd33Y7ZkEUA1EzvRAJGe6mUzcPjfwmnXlLf52r3CusSGJORgKSqbgyC0Q2Oipv_lYI2w2I19kTquCxF0opcebx-_UjW8sHr95UnTg4iOSizwfg_JlHMktfUYw5KTLpIdoaGd9c6cG9viR4_TsmHVqiIIXcs11H30otu1yFtxmwndgc1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه شکار شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82180" target="_blank">📅 23:50 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82179">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQTQGmgALQLnPYBOv_BznuKEvDe-Yx6ng7rfdZqgKwS63P9KXRh5UP9oqTeX-YPYB8eOx313xBoWYOhFwJS4V39d0REx631CTzcHcXX2-Q75zyE_E-F6AbYwu_LjzEZvV4EuBLPzys2ai0xIYrdsXeHkfvAAMKk8c0qn84QbQD2oftarctJYQUuRRpK6bQE9mbcHhnG-sgXnoiv826wsUwJFxV71oeKNhjlkgDDcq_QuKNaS5oGtRz_kO7WfFgFLoZsjBj_EqDYKZ2cphlRaNarJ9Jjw0Lkd0lAFQj4DRQ1gjeynGDQ-5wG6RmbzY8JoK2sLdROk2WRl6KpOjWoREQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیری پلشتی کیانوش  @FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82179" target="_blank">📅 23:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82178">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5782494606.mp4?token=YxpJwdZfzl5-9JRJQDkt5OZw0zEWWxZohkhEz6vVxBhdwb5ZtAacy2FGK6YLoAKSde5tKJJKMP_pAxQkjtSz1eGIHaURiIB7xhO9bag1LnxPXwdIPTsa0akBsBmR9qjrYKqMhihFI7qlW5vDkC2qcZY_vWOQ0M7ku5AQuADogW5xKTCXjINAB3qH1J2KdPx3iqdno7iZpp2xuDSCP_xBl8UGXQZVZOsqLk2-6_oCgCdcoJ63g2f0DjI4VODuEWjkqedXlzi59by-S8N3z411T4xv6Osc4v82_-YA_Sm7gU6J2gVoO3AVmslzJeSEm5ld-aFRmiFrOI2kozD3yPPqKGmEtZbKvo6uuMV8b9BhLIhFK-giJL1YW4evdF8S52K0C4-ZcW8EK4ifw7LZaIXusYoHGgx1CZI3dY2lGv0iXHocCRRwTJjpPCMESRYIrZwWTDOT2Bwz7JYawrS9ulzNnD3az824j73Qr6Ch9eAhI4MIwvXQoqSTbmArSMMNbRLC_YCN6nPHWHQLQSiNUUz5_6KxoesWZRCm5UUx3B_UQ92jU1QcHwVohrU3tRZ6CQotPmJhUexI9tbzlf3p2p6YLv6WKBNc6695nfnep1WgiDSbFQ2JDtTOtNvJCTm7T_FrW85EOQ3S6YapB1sB6K9EKkrL-4Z1svqEM67hvhtEf1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5782494606.mp4?token=YxpJwdZfzl5-9JRJQDkt5OZw0zEWWxZohkhEz6vVxBhdwb5ZtAacy2FGK6YLoAKSde5tKJJKMP_pAxQkjtSz1eGIHaURiIB7xhO9bag1LnxPXwdIPTsa0akBsBmR9qjrYKqMhihFI7qlW5vDkC2qcZY_vWOQ0M7ku5AQuADogW5xKTCXjINAB3qH1J2KdPx3iqdno7iZpp2xuDSCP_xBl8UGXQZVZOsqLk2-6_oCgCdcoJ63g2f0DjI4VODuEWjkqedXlzi59by-S8N3z411T4xv6Osc4v82_-YA_Sm7gU6J2gVoO3AVmslzJeSEm5ld-aFRmiFrOI2kozD3yPPqKGmEtZbKvo6uuMV8b9BhLIhFK-giJL1YW4evdF8S52K0C4-ZcW8EK4ifw7LZaIXusYoHGgx1CZI3dY2lGv0iXHocCRRwTJjpPCMESRYIrZwWTDOT2Bwz7JYawrS9ulzNnD3az824j73Qr6Ch9eAhI4MIwvXQoqSTbmArSMMNbRLC_YCN6nPHWHQLQSiNUUz5_6KxoesWZRCm5UUx3B_UQ92jU1QcHwVohrU3tRZ6CQotPmJhUexI9tbzlf3p2p6YLv6WKBNc6695nfnep1WgiDSbFQ2JDtTOtNvJCTm7T_FrW85EOQ3S6YapB1sB6K9EKkrL-4Z1svqEM67hvhtEf1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه عزيزانى كه از رفتن خانم کارولین لیویت سخنگوى كاخ سفيد ناراحت بودند ، مثل اينكه ايشون مى خواد بشه سخنگوى جديد كاخ سفيد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82178" target="_blank">📅 22:07 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82177">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUvfcCTVCeca3X6wdIjnNg_GOrWbIrWoqJnmLIs7qcFeOVSSMs-h3Uxi6BrUGTJzsF7SAf1-GlEyKgfZP1UQKN_jWpefkqekhxZ7LspZYweeXUNsYfiE8-5_KHUyutqiYNeKcz70alZkRXVMFf2npV8oo-y9Q_2WkA3Owv3Ln6F4eHuthisOPsMdP6tsJmxkwA3neF7o79I6zql1a5ADYo06UKoKo94LMqRhf85TPCeDcKCnE58YaShEc3jT4vbkdF_GbkcRxWzqFBY_-68_9FE-zi2kOklZP5AkfI92p6nYK-Bnw3gogwpz4Am6OU5MPoK1AfQW_INxxN6e9ftPCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "قبلنا" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82177" target="_blank">📅 21:00 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82176">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403c217675.mp4?token=SoFj_sUsKPYy4I_Vu5oFMTXYSvwNXYeym5aLQ0xklKWXoAa-KOvLPoF1puo7BJCrMA58s02EUfeICRdZzsqKZjfRlAlO1d0iY54SW6fiKcawLxTvkR18EzacI0smnesToAyMrHLwEDOxdvyLgvxe36DdvPKwMPbx6qlDzR5BSbvqeswKtdUOUWfcyVHKYB3gKe2m8yxSWlv_j1OmHm1Hoj4IlROny8UVWlMp-zzvNdiND1pA3-YOZqk4cLBEEs634ZyeMXpW9Oe7PKek7a2GOmis12ZMdR4DyFigHPohBUt481AAQRXQwK2_VCmVN2NN-OM7XyZp4VNdoygiTwUTMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403c217675.mp4?token=SoFj_sUsKPYy4I_Vu5oFMTXYSvwNXYeym5aLQ0xklKWXoAa-KOvLPoF1puo7BJCrMA58s02EUfeICRdZzsqKZjfRlAlO1d0iY54SW6fiKcawLxTvkR18EzacI0smnesToAyMrHLwEDOxdvyLgvxe36DdvPKwMPbx6qlDzR5BSbvqeswKtdUOUWfcyVHKYB3gKe2m8yxSWlv_j1OmHm1Hoj4IlROny8UVWlMp-zzvNdiND1pA3-YOZqk4cLBEEs634ZyeMXpW9Oe7PKek7a2GOmis12ZMdR4DyFigHPohBUt481AAQRXQwK2_VCmVN2NN-OM7XyZp4VNdoygiTwUTMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آروم بخندید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82176" target="_blank">📅 19:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/erjiLW0trWdjpOKOE_WsQ0DFlFqIpHzwVVxEzaciGg2IQpgGER6mdktsVnFnEAlK5SbFEfUC4X87wDfsNW9cnwbQqaY8GeYVAruR_9WisljVJTWRlhQaf58QtMOZ8O_kpMNhz-wa5Fhw1sL2BwpiQShhH75r7QH0LfiTAbJtDlxNt2maoVgisUtMaSKRLtyxD_daFr2tyHPq27zvyrlpJYjV9CjwwGd7ADSBlD0vgPI6nJPl3HiCM_q13wk41PPfu8pMPFRycikc_yzB_cwmK08WxovaVZL1wLp1j3t9ZjqhfY_CPX3_4ebVblSYbQuOGZO7o1JumyO2yCq58UYi-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lIk8H9opCVlXf03OqLwZyt_qAAR7J8GBrmw-lCFDJ9luhaLS0NI5Z8BsT9SrRrfeSnBAiDXbfJSWUGaLGtKGP4EuqYiqC_7eofmeyUOk7K5BpQVpDVes9RA_zDZvJDkDSM98SPWBUXpmlrfY4DJ30BbS5Nh8qbkDqsD1BJpBVFwVk5JUyTWVQEBAlfC1JztSlOA64GIlSK2SMWZwDv_5TqQqbGlJLbibtuccha85ED4mHbYJqxEHx6-bRBTQm4h7ZHubAm0u5YrMvTwtgATP83F6yWdvixzLfmPGbd-CYiH8zMBdpMSgFNF-TXUjHAU8q_yW6Vurtf64PYSBwQwN2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hWdSY11LvNgUVb7K_ITL3Sx0B51uJqeMzQdNK92GMWWKLz1tq_2EX9Mt6ri-KaZ8qAVkcE8zJN4OONq1jZGKJg4qrktdDWgGv9wlFbYIGnmGd5nBR8r0EQ5B6EwmcWnT7BGjzlriYSHU-itgvLhkegD62vllzCso932IWKWqwlHEF2XJ3ydi1_Ygy34sUsdH2Xf-jLuUDWQy-OfLkdYrwzWpgl41gnm7bPjEcl3laxwPzRVoGlGM6q7aCP-wZz60CGsGOzxlEW0-VNXPISu5OydHudGhVqgfMARlIWRQDYsW0lDpHrUMZgyupnGP4av8kRF_BWB9_ghRkWYilBoAnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQzZONZg92OOR74LjwxVknmy7Bh61-O02G9IKScDSJyDddoBZt9TzsaIDdeakE-MuUAxSJPRWQu-3d0ICDRvYDXnrcXP9CDKqHGwpqSuBMg5Hsw6QM2qVmwDR70NEV6aH_5knk-O3kOVLo1UeoCFQ41tuEFMUyBoorHZK2QwlypIdIipXVLkxmFXYSHCwEynIkd4Vn-XFAEdWwGVG0VTdMdcugb4dHZ1Tj7P5bdYHFt06cKqpf15U25M07MWLTPOFwNTISBgyy9IRfHOHk1WlFqnecEzd_RFTsrH3M5wuSsnG4f-2joZdrH5eN6rPopU8jZO54KkNsq9qIp7H31d0Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=ATv8IM57MqnUNPPmrhnGvuIapkaCLDuiRKmXgLy9-sUp420QNJHcnefIY2uXzCKMRPjGXEQ0fezsYWNVGYXMQKBLw4tpipEOePnl73skgee0G2X1zB1RQnaguOCFkabrwqnFWx0NY0auhOHRoZV0vaRXO_mbd3vr8ybmR26BzsIYCzDog_GrnPK4QPFD5R5WrnjdiSuo6jLhjl_PldJlvmAol2ekfEhMp33Y1Xx7Vsf5yFDHtvIrufwdDPNVTNPRQ6ckWY4I88pO3vug1RgSdZD9qeh0RJaoV_2tTI3buAT3M9Ju_11obHTK169LmLvT7ZpufGyjbmteaoBre0VMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3aa705dcf0.mp4?token=ATv8IM57MqnUNPPmrhnGvuIapkaCLDuiRKmXgLy9-sUp420QNJHcnefIY2uXzCKMRPjGXEQ0fezsYWNVGYXMQKBLw4tpipEOePnl73skgee0G2X1zB1RQnaguOCFkabrwqnFWx0NY0auhOHRoZV0vaRXO_mbd3vr8ybmR26BzsIYCzDog_GrnPK4QPFD5R5WrnjdiSuo6jLhjl_PldJlvmAol2ekfEhMp33Y1Xx7Vsf5yFDHtvIrufwdDPNVTNPRQ6ckWY4I88pO3vug1RgSdZD9qeh0RJaoV_2tTI3buAT3M9Ju_11obHTK169LmLvT7ZpufGyjbmteaoBre0VMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامنتای اینستا واقعا جذابه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82171" target="_blank">📅 19:25 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1OUNdCctK-pBgBWJbitCw59KKFumLi5LibYGCmyf7g2Wu9OstVltCLHS6fT5kcNn6lovqkq3KDklT56DGxcjK_mgYq2FgWwpB9obttnVtqhrFGYCisuNHWEtnv9zO-q2KDjtH2uSaQWsDRoV6CRsWrD5MMHtRl0ya4jOTJz-wSgP3nidbXw7QWAZZIjqDILIkkz8bStUnmt6SMc_BVKJ2hH_1RVKyMksq2Ee1Wyl-0uZTmCHuHsJKgIlVI0VIs0FItvHh4dNHOIiP3uYu-2A9ZaNIGBi1ch-UAXOuS461Da--MmJts00Otmfy5oMg3MdUETb4inlRoaJMvV0dndpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودتو گول نزن ارسام کیر کاگانم نمیشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82170" target="_blank">📅 18:53 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">پس دابل آلبوم و این کصشرا چی بود
این چه کصشریه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82169" target="_blank">📅 18:26 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بزار جیبت بیبی</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82168" target="_blank">📅 18:19 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82167" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eqavna79RBn39z8Ct5z6YV6jyYPlyts0MBUcyIwOjIWeVtnPb5i9mZswquTrX0XXjI80wXp5YPDSy7eDCIY16qe6eeRSI5osbk3bkBNUWcHZsaC0uX_wRiRHFYPdi1BWvygNDg7BOyt2vqoy2wdwk0w7whnDpUM0pNDY4budasZB-Yr4qPAC4wJLNntv3sbR_yZmSDHvxUZpGRcP-JAO-Crrqa68mLMFl8OtUAZSxBzx-Qx0HQC-ciZEPPJ_BavM12ugClcwXx4gNr9RZJuhkibLD5wYRXGCFgy2zuoIUSMxZfqwkAem2_lYJDl5K4iMISIFAVO8N5_vkSDIP6XL1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دکی به نام "بزار جیبت بیبی" منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82166" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9rrH9LIZkfErzwlugbICjeAx-3VowmQpCpaJEptq0b19LGd5sNRb7U2A0DzBrXYhMx0ZGVFrsiL72ikkJCr7VnIn6L_RvOTlcI_Y9_2lqOnF3uxERmWaQGnEmqoJOIDQJTiDe6A3qvLmrbpYB2_FTZ55lXSFhWj7U7U0w7HWfERqVTGsSKas3jjzlY5AYQfEoRygiF043muBTQGP53TGykBxx9JCORAtcXmgNMbwvpitUnG025jUGBVqjlu95Xgpy1esja4Yx3h1iQxn8nc0vxG_4bj14kv8Yx3VQ29hCCLm226d07aXEpHNIRsMW5E3uW-dJ6PUvGXMOhBb_rVwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r22
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82165" target="_blank">📅 18:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82164" target="_blank">📅 17:55 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkd8XasV-4rrJn_YQKgW_Af3WjR9SVig59RKO8riSoiOGKZK4m8zFXergnkKIm-9r21vqyBqyNiRQFrMvLwJ6cOhNdw-QOJ4zbksS3t2hThkTnS85-Qt0xZzSQRzNyBmIq01_Xy1cHNk2vX-4l22Z1BaXHnl9_6VvzvSj4eX0k6fjKs9DZlmzbyS1xtz9I6rn9awFaralb55gfu4bNYWVcYrDFVGLGnf5jJAtEkYrTqbTmOOsBCndAfz8bBw526DFAv4Udyj4Q8MSZlbBRrbLn4zKe6KBy-_MrDQUzSKKJ3CU3iba7dKLjQIi5jPdqdOP1-607LmfQGAVqyAO0iNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاور ترک جدید دکی اینه احتمالا
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82163" target="_blank">📅 17:54 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=NgDGnXQahnsWogJW0J8lJiukD7Yjt3xoLWdUadDyGVI-5pOq0TAs99VsVzLZ1RiuKPnfCkMeaaTYO3VcsfFKupktx8okFzFl3kZPIWffsJA4zJArnYXHBgvqEDTWUm3ANs-YKLZlaLvZ7-95Ys3chOGnEAVdkf2uxFMT8NZouvdks_-0SPiTjVYdfAnpfIlRS-4PaaPkNnyQRf3xQuTca5sP_LCVgBJrJL-xPX42xwheFN0LlPJU2r1MFSlj8c1c7S2giawQzQjUPv7MQspBwVV4ulnx12K8CdFA-U0RvY4xT9CI2msqIl7MslItm_PiRYf1eEpXgwijcd5EUz82sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c7242a55.mp4?token=NgDGnXQahnsWogJW0J8lJiukD7Yjt3xoLWdUadDyGVI-5pOq0TAs99VsVzLZ1RiuKPnfCkMeaaTYO3VcsfFKupktx8okFzFl3kZPIWffsJA4zJArnYXHBgvqEDTWUm3ANs-YKLZlaLvZ7-95Ys3chOGnEAVdkf2uxFMT8NZouvdks_-0SPiTjVYdfAnpfIlRS-4PaaPkNnyQRf3xQuTca5sP_LCVgBJrJL-xPX42xwheFN0LlPJU2r1MFSlj8c1c7S2giawQzQjUPv7MQspBwVV4ulnx12K8CdFA-U0RvY4xT9CI2msqIl7MslItm_PiRYf1eEpXgwijcd5EUz82sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/82162" target="_blank">📅 17:11 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82161">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=e_hODKDz-FVEZ3-TKyulgBA-TVDMZbaVRBBhH5yqz5dhbW8qX_cL9r0JitYrtVn6URHIUEJjZDHWW7ZzMGfa-_TAAW46zjxKiCP9wzRAZ9KYbC0BwYdgLOn3rg_GdpNtpxV-o8AaQupb3FD-jWR-0zNBm9g1ZChJ7BX_TYeasUwp97YqiTS9z9GlXw1TWjjRBJIul3eTmmQkxL-L5b8ebHcq5bHALbCTpiD9EMrCf7hLFSTQ3qlO5E4248piTWZDQgx-fJbTiNR56L1u1Dt4F-DiOsD_FKpZOsHbhk4dIvgi_ZfivfVNlkS5WQG9Cs4G36RMoQnmgq2LVefyA_h03w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a59034baf.mp4?token=e_hODKDz-FVEZ3-TKyulgBA-TVDMZbaVRBBhH5yqz5dhbW8qX_cL9r0JitYrtVn6URHIUEJjZDHWW7ZzMGfa-_TAAW46zjxKiCP9wzRAZ9KYbC0BwYdgLOn3rg_GdpNtpxV-o8AaQupb3FD-jWR-0zNBm9g1ZChJ7BX_TYeasUwp97YqiTS9z9GlXw1TWjjRBJIul3eTmmQkxL-L5b8ebHcq5bHALbCTpiD9EMrCf7hLFSTQ3qlO5E4248piTWZDQgx-fJbTiNR56L1u1Dt4F-DiOsD_FKpZOsHbhk4dIvgi_ZfivfVNlkS5WQG9Cs4G36RMoQnmgq2LVefyA_h03w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بارتوش کورک
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82161" target="_blank">📅 16:06 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82160">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">سیتی خداست، هر سری که تیما اون پولی که برا رودری میخوادو میدن میگه نه ده تا بیشتر، خلاصه قیمتشو از ۴۰ میل بردن رو ۸۰ میل
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82160" target="_blank">📅 13:41 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82159">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IsnRbfI05GclzhAAtvLTHLB9nrVAsSGMkoBLDcvid0i54qy0m5rIXONfXiGSru6R4GocKoETTmLmmr4AAni11mlwzsT3wjdFnhld_y5py1SgBbNXYYSVARga-Y8Tq1Zj30jknWhh1Ww4YtBzuEoaWtkSQdruAdSKEbZcTCAU4GjSMLna9IvCS4eJMmRgty2uEBbCdE73SvXD5ERzmlt_BTuxyc2mBYIbXdi6mPTc2XJMwixqn5FmjfLu-34GJFkPeziJUb-LLCU37KEreAl8q9DyJiX1NsnOrB8T0EHVM143qteR3YATbLk-HFSl0Sl8U7M1ifKIpP46aFNxbPolkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویرو هربار میبینم جمله "آقایییی محترمممم" میاد تو ذهنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82159" target="_blank">📅 12:40 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82158">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaVz4S98tMsFy9EFT72e_uS4bba5DGKhOWnlgDmNWEz1-OjLvs5_2mk0UvYPu82wOLrTGdvB8T0eiQto0RLsZVVIvM5pqUIZ8gi-fdJGhKg3_NsAktqMCWWTQKfJ7evCRfMEZgAmx9-4PVtBhbvJsIKimIJOxMsb9E5pgoTGFg-ARvDI-CrtisC1Mddy9mu2Nc4NEXHti1Q35RuHMK6QwQ6H5uv-X7tUkF_CRWOKHHpf-L9IbbayIInyPJ8Y0OQP08XI_T2lLuuLIMc-io4bbZYP63IxeRbZg-nYMmt5gXqa8QgpbhvfTXmNS9vx2s7tJokXmCZBXa8ATS7OK4pKvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خفه ریدم تو سلیقت
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82158" target="_blank">📅 11:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82157">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=DbPu5mLSAZf0f9w5Mr5mUsPjNb0HSmlFKnTNTVSM8BJbEtqW6vaQgHpdcxW7NaMF44reZA40FhJUE3oN4MQrKQDhabJmRaqeoETzcPLs8q1sHyWqA9yvDkrVkAN7dv45JnLtPo4gXwOkjdARxe24l9sNmJmEWsjqM1KuxPywDcepI-kXzmqzZsKZS1-DRFpRTZRpnDgRkTQ6UnBQdYv7wByqIs1TNnPiVUcIyC1jW469jAhLa6LsHV3Il_-k4WP8VBaxsJ3fqYyDrUkfgpNj8PcZFjyCqhqJSxnTeQBs_4ahJTUP67gIClyKYeWelji933KN6p4A52fg3iihbyIiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e23ac6b2e.mp4?token=DbPu5mLSAZf0f9w5Mr5mUsPjNb0HSmlFKnTNTVSM8BJbEtqW6vaQgHpdcxW7NaMF44reZA40FhJUE3oN4MQrKQDhabJmRaqeoETzcPLs8q1sHyWqA9yvDkrVkAN7dv45JnLtPo4gXwOkjdARxe24l9sNmJmEWsjqM1KuxPywDcepI-kXzmqzZsKZS1-DRFpRTZRpnDgRkTQ6UnBQdYv7wByqIs1TNnPiVUcIyC1jW469jAhLa6LsHV3Il_-k4WP8VBaxsJ3fqYyDrUkfgpNj8PcZFjyCqhqJSxnTeQBs_4ahJTUP67gIClyKYeWelji933KN6p4A52fg3iihbyIiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سم آلتمن مدیرعامل OpenAi:
احتمالا تا ۶ ماه آینده، Chat gpt بتونه صفحه نمایش موبایل شمارو ببینه و بخونه!
به این صورته که کارایی که در طول روز با موبایل انجام میدین رو میتونه تحلیل کنه، مثلا وسط چت با پارتنر یا رفیقتون، کمک میکنه چی جواب بدین.
یا اینکه سر کلاس آنلاین، جواب معلم رو چی بدین؟ حتی می‌تونه تماساتونم ضبط کنه و وسط مکالمه کمک‌تون کنه!
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82157" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82156">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tu-SSRXZapPILfvYy7Fc7WxHM3H_-TNXuD-xcrtzv1vTa43JXQX8A0G7AkFrfc61Ffo3loG9XWsP-6awOEP6KOWLZNa2u-bzTWvUSW1B9CtF67LUITBeGs95XwDNg27Nb7fmKbyMqaZJuGDR13suqgAq-wdGBY4oj2RJIH6zq6ONT7TdkJbu8R_ofxWqy9RfXa0PXJMOAi04RwCgmoStaGdCC7UyjNeVqeh-Q-AqUQiaaYLUbV4rI_sVdCpTESYpgoHNPo7TlgfFeBG7CYXLSrrJvTwFIFlzu7MmxYUMUhrnBopQQ5FtsQqIrvsqve-3dugSt5RuGPqaMjv4NIzZuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا صد درصد بیمه ویژه پیش‌بینی لیگ برتر خلیج فارس
🇮🇷
⚽️
با ثبت حداقل ۵ میلیون ریال  پیش‌بینی میکس بر روی رقابت‌‌های جذاب و تماشایی لیگ برتر خلیج فارس ایران، در صورت ناموفق شدن نتیجه، بت‌ فوروارد با توجه به مبلغ پیش‌بینی، در هر روز از رقابت‌های لیگ، تا ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/PERG100
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r22
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82156" target="_blank">📅 11:03 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82155">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=TpOdVZmDFDT8J3Fc4dZ5jg0PMDnEb-9ROuubf2_dvTk75lF_Wi4Zobf6wUqQO8S_LmHf8qX4I75BG7l-cRRQfIMDhX_zYxc35JQoSsw-vfcBUvim5JZ7-MysiAQ3VZeJcdNmmNqdhLgD_MUv3cWRTX37knGMmnC2W3-dyl3UMUaUSY_EQoSwJHJJcEKB-C912yn9qKsS2-9C9lbp7akwjSepuz-awqB2ZdnwvgmcAcyclVBpCdti3OylqrK4J-rHmmFwofpDG8_p8OxblOon1qNjJ0GadiyNjoNeJpiLahhqEe7U0vlrDg8G4gM2dJLuq2X2oxwT-eP0WGV4ZTy30g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b33fe099a1.mp4?token=TpOdVZmDFDT8J3Fc4dZ5jg0PMDnEb-9ROuubf2_dvTk75lF_Wi4Zobf6wUqQO8S_LmHf8qX4I75BG7l-cRRQfIMDhX_zYxc35JQoSsw-vfcBUvim5JZ7-MysiAQ3VZeJcdNmmNqdhLgD_MUv3cWRTX37knGMmnC2W3-dyl3UMUaUSY_EQoSwJHJJcEKB-C912yn9qKsS2-9C9lbp7akwjSepuz-awqB2ZdnwvgmcAcyclVBpCdti3OylqrK4J-rHmmFwofpDG8_p8OxblOon1qNjJ0GadiyNjoNeJpiLahhqEe7U0vlrDg8G4gM2dJLuq2X2oxwT-eP0WGV4ZTy30g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال شده باشه اگه سندی چت کنه چی میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82155" target="_blank">📅 09:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82154">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یعنی نتانیاهو با اونهمه قدرت نفهمیده پوریا زراعتی آدم جمهوری اسلامیه و بردتش اسرائیل و باهاش مصاحبه کرده ولی چارتا کصخل تو توییتر فهمیدن؟</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82154" target="_blank">📅 08:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82153">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">درکل فیلم قشنگی‌ بود بشینید ببینید بفهمید تو چه کشور گوهی زندگی میکنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82153" target="_blank">📅 03:14 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82152">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=Q27CjRzx4c_i5mXLNG-h4_MyfirnywJGGAg2VCIjXELiQj56HFVSN0rSYX5byEMBvY8MXwc6soWLB5ZWnCWqw1yb1tFGFXrXaezUW8Q_pEf8Orvwb3nnts9DZuA-WqmwbpsV8ThBwIjhdl6AB97osAf2s2VesS-QGWSNgiSZB4366VYRnzbpDA5d_RcU9bTFmbhXwOJ1my1pXcDWi_AOYRJz6jfkNRx91TgDJDYafPtOdLKXSUsmYYqTTDX4x0uPPZOljIz_zrYiHo9YZEOpcv2bO6RUXZF1YWbRgRX2c7-TAJwc8mrKsokgHwID4g0t3gWlQV7q-o9uMdkN_atuRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe5c5e708.mp4?token=Q27CjRzx4c_i5mXLNG-h4_MyfirnywJGGAg2VCIjXELiQj56HFVSN0rSYX5byEMBvY8MXwc6soWLB5ZWnCWqw1yb1tFGFXrXaezUW8Q_pEf8Orvwb3nnts9DZuA-WqmwbpsV8ThBwIjhdl6AB97osAf2s2VesS-QGWSNgiSZB4366VYRnzbpDA5d_RcU9bTFmbhXwOJ1my1pXcDWi_AOYRJz6jfkNRx91TgDJDYafPtOdLKXSUsmYYqTTDX4x0uPPZOljIz_zrYiHo9YZEOpcv2bO6RUXZF1YWbRgRX2c7-TAJwc8mrKsokgHwID4g0t3gWlQV7q-o9uMdkN_atuRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82152" target="_blank">📅 02:52 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82150">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بیداد خوبه یا همین سه چهارتا تیکش تو اینستا خوبه</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/82150" target="_blank">📅 02:20 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82148">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFxnZZVKRNhQ8YNlHzwLSbC3C-q8jEh0hoHeq3YkLJO_4Vg71-S31a-rFcwAckpnpHsIZN4tBOGjT3GiBV9DvsxlfplXqpuw40gbrwQazUkwqIUzj5s2qW_akc7ekIJFIQ_tE9VA25m2bvHAV72WqCnTvR3pzp1JTc92-YVSfgMVokhiC7K-1xR-OF4pKL0X7ceGeGKz1rn_LsUXNfUWKP1Bbnmkb21M5Oyokrd1xkXEzrVxJu_uIK9E1INEBc9vHYhKv4Oxw3apIElHX4f9pePF6OOjeDzM-UE8tYO75kZGuiJaAcgwZoHnblN2-ubh3Ln3fI-1oeb2AvrYWgXWMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=Cqhut3N7YcfGjk0lSdmw8nVC-vFJNvdJlMHTzW0YXnZaOj-BNFXvJUxYvsRnPUA7Bgv3h15MVqu1Sk7Tm3lwhGupOH9vdm3_8gE0bOf6XnZBOUxjcRZAoP6vo3saxUZM8dpOV7jgwGcQfpUiTjEFKq8P52K2BsSl4mbar-6Akka33VahV_GqOF4WJgpXMI55Y_g4kj_Hyt71BAi2fGphI5SA-8N1yddKuqdhhyRgCx5oVjjVLSp51eLwjLS-nca2E2cquPtHgozGFfeCSIVGpIjU1LBO3cYVOTUBrj6SdD-4Zfs0QukEFfrs60z2BF8cdfY31Mgt74GEKHuBI491KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf0e2ba89a.mp4?token=Cqhut3N7YcfGjk0lSdmw8nVC-vFJNvdJlMHTzW0YXnZaOj-BNFXvJUxYvsRnPUA7Bgv3h15MVqu1Sk7Tm3lwhGupOH9vdm3_8gE0bOf6XnZBOUxjcRZAoP6vo3saxUZM8dpOV7jgwGcQfpUiTjEFKq8P52K2BsSl4mbar-6Akka33VahV_GqOF4WJgpXMI55Y_g4kj_Hyt71BAi2fGphI5SA-8N1yddKuqdhhyRgCx5oVjjVLSp51eLwjLS-nca2E2cquPtHgozGFfeCSIVGpIjU1LBO3cYVOTUBrj6SdD-4Zfs0QukEFfrs60z2BF8cdfY31Mgt74GEKHuBI491KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئال بعد دوسال جام گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82148" target="_blank">📅 00:34 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82147">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umr5fqNh0o9Oz2oDE3pKD07inYmLGtljblGpFTpiUrpG3d2EwAIaUulqeYspYbJUaoxHn5TPpn4LspyL-ETR7zHSN2Lqt0vt1GVFyl1PoU2r0Tj_gjf03Z9jYLLi28wHcVq1w2ytrjhJHkK7vylSFuF3DoBB_kV6O5Cywc1DAh9MH8uG_iPYC4fNnmfgtpm1lx8NER-0F93ztpSf_j7s5pAlWFPiQVCkxUfj3i6gnwo96JBlACMYGaMJR7YwVByYIUAFdgByy6kYaoQh2P-woC2ONOAkU4jmzcEMD6cOw-d9Xg-NnR3hz_R_Jw9Ux3jZ1cENfGT_aijwnL_ewHQL7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اوکراین هم عده‌ای از گیمرهایی رو که مأموریت هلی‌کوپتر GTA رو با موفقیت گذروندن استخدام و مأمور کنترل پهپاد‌های انتحاری کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82147" target="_blank">📅 00:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82146">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پاول گیفت تدی تروریست داد بیرون
🎁</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82146" target="_blank">📅 23:08 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82145">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">کیرم تو توپ طلا اگه به کسی جز کوارتسخلیا برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82145" target="_blank">📅 22:52 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82144">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9VdPw5RHgbDjER-gHmOolAqsghzrOULAhOaPN_Nd0UGyz0bHkN-jjLagy-pZz-YAwQTzZb3WpSR3v_wFL3tQwShVCeM24yR4jNOj7wrDAPPVvJMW9Fwx-h-TQzGmZjdUfpEQC5pup-YPm57O2-gZmttESH7_ZIXQn2tz7BhNq8KtXXVc5J2Gz_1IbWNCsp2bhG_FXrqTXCBI-CyX5bfJxfRvKhZAeBtfJeOnwQAFZtbL5VHhr3n0WeOyuKkx3wKOBUMy1pLU8AVTK8YlCMiuP1AB5DDIzKYvrA9rlUV-ue-8xaSUWsx4FF8ryxcPyN5gUaBiuoMJCXkAB4sWg-ROQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام به قدرت جدید فوتبال ملی اروپا, هلند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82144" target="_blank">📅 22:45 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82140">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">البته ما کی باشیم نظر بدیم، چین برامون بنزین میخره</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82140" target="_blank">📅 21:58 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82139">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">موضوع سادس، نه میتونن بنزین تولید کنن، نه پول خرید بنزین دارن، حتی اگه پولشم داشته باشن بخاطر محاصره دریایی نمیتونن وارد کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82139" target="_blank">📅 21:53 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82138">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تورو ناموستون شما دیگه حتی با افغانستانم نجنگید ممنون.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82138" target="_blank">📅 21:41 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82137">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">داشتم فکر میکردم ماشینو بزارم خونه با مترو رفت و امد کنم یادم اومد کلا ۴ تا استان ایران مترو دارن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82137" target="_blank">📅 21:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82136">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">قیمتا دقیق:  نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان  نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان  نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان  نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)  پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82136" target="_blank">📅 21:35 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82135">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">قیمتا دقیق:
نرخ اول: ۶۰ لیتر بنزین با نرخ ۱۵۰۰ تومان
نرخ دوم: ۵۰ لیتر با نرخ ۳۰۰۰ تومان
نرخ سوم: ۴۰ لیتر با نرخ ۷۸۰۰۰ تومان
نرخ چهارم: ۸۷,۲۰۰ تومان (نرخ آزاد)
پ.ن: فعلا این تغییر نرخا مربوط به ۲۰۴ جایگاه تو کرمانه، بقیه جاها اعمال نشده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82135" target="_blank">📅 21:33 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82134">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82134" target="_blank">📅 21:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82133">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82133" target="_blank">📅 21:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82132">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میگن دارن سه تا نرخ بنزین "۱۵۰۰ تومنی ۳۰۰۰ تومنی و ۵۰۰۰ تومنی" رو سهمیه ای میکنن (۱۵۰تا سه تاش) و نرخ آزاد رپ نزدیک ۹۰ تومن میکنن، حالا کاری به این ندارم که ۱۵۰ تا ممکنه برا خیلیا کافی باشه، تکلیف این ماشینایی که از زمستون ۴۰۴ تولید شده و سهمیه ندارن چی میشه؟ کدوم کصخلی میاد به ماشین ایرانی بنزین لیتری ۹۰‌تومن بزنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82132" target="_blank">📅 21:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82131">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صبم خلسه اومد این ویسو داد بهش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82131" target="_blank">📅 20:27 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82130">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مگه دیروز تو البوم فیت نداشتن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82130" target="_blank">📅 20:26 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82129">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">کچی میخواد به خلسه دیس بده</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82129" target="_blank">📅 20:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82128">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gi7WikjbhxUB64lv8Rnxl9eIK-2Nl71kLOKNkC8Ac4uigAZm8RnoedEa8XbbUAKGfEY7GWRh3T4g0tZU9yrTgDJZkZq19szeN5NZ6avbGSauXdkbjaEaWcHKAL0kJf6eHL_eLjG2qDZB3nuY80u1noIhE6ZgiEXOiks9e2AFiG7W0e2EGh9XS6WiC3JHZnAu6sRxEPxDXmkQGBZL_cK9rD8N4OJuBRioa5UJyDa8CEyjNp72eIZmxRWJ_g5dP2imfpEOXxbCLrRrJZ4S9gsZUfnH6VbHB18tXXv_SmGRVlCnucjRfcpKDK5Eu0nr0rLqDMnimRRQ2auN58uLGIbgfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادت باشه اولین چیزی که توی استایلت باید بدرخشه، موهاته.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82128" target="_blank">📅 19:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82127">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=ij-zBcBxZjO3nurAO6AADpwyQDS8Y3rwY5Rk4F8l8ybTu6vkVvgta8PLETQotZ5PgnJZb4JeIG4dHnWbKiTq4V3KwNn3UIqZWmneNkDgPxPINAlvmucOB6szNnHY4KhdVEZXYOQSc8fUJXuHYU-vCbJgydNFM7BNxLXdSN5rlIGkoEDagpAn7N0EOBoVbb7J2yLYiAvtPlNk76_crJmNi3cwwbEIt-pjj7oj5D7EMQJab-xQFxCn4Mly70B2nMrvjUtcObyk0RXa-1DCcLGdiHEQFQ0ceLLEQKT0rfFKCnAIDi4Tb7FGoaM99gOWqveti7Eb1VJOpgxH0YNcJTFjig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4765f0c41.mp4?token=ij-zBcBxZjO3nurAO6AADpwyQDS8Y3rwY5Rk4F8l8ybTu6vkVvgta8PLETQotZ5PgnJZb4JeIG4dHnWbKiTq4V3KwNn3UIqZWmneNkDgPxPINAlvmucOB6szNnHY4KhdVEZXYOQSc8fUJXuHYU-vCbJgydNFM7BNxLXdSN5rlIGkoEDagpAn7N0EOBoVbb7J2yLYiAvtPlNk76_crJmNi3cwwbEIt-pjj7oj5D7EMQJab-xQFxCn4Mly70B2nMrvjUtcObyk0RXa-1DCcLGdiHEQFQ0ceLLEQKT0rfFKCnAIDi4Tb7FGoaM99gOWqveti7Eb1VJOpgxH0YNcJTFjig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
زاکانی، شهردار تهران:
موشک مستقیم به طبقه خونه مجتبی خامنه‌ای خورد!
خانمش (زهرا حدادعادل) اون روز سردرد داشت و نرفت مدرسه، موند کنار همسرش و نهایتا ترور شد.
مجتبی خامنه‌ای خودش هم مجروح شد، ولی تو اون شرایط دائما دغدغه نماز داشت.
با وجود زخم‌هایی که داشت، خیلی مهربون و خوب بود و توکل به خدا داشت.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82127" target="_blank">📅 18:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82125">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAvY6gFVqdhBEBwnYiR2Z6Gt9-Y6A93ZP8LNgIyDCDwK26ycLk1OIfl7cUrvAXHRGh1ezI9_BDxl-KOxqj0mLuzkPE0v-sbSchBRHl7q85QkjHfLp7vmpbwCb_JTFIXn6cQd-cfbo8B9Ku893cMNNzAEDc1ufMZqIZB9Kr4kyi_GKmZ3wq2jSyzsYmkCqEWhmnPBo-HYto7BzWzkAgUs5fIB1b1ivsp7ib3Xa1dKT9gofDB_e1Le9yMnlTAPiOIhq2wySH7P0PYuTdEETxuMuvUldMXrjJwHWUgJUnV_4iuURx-6q2qXHtTQmUZdKa93iDU5t1cW5LwfHkGUwGFrFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلنوشته مسی برای پدر:
اینکه دیگه نبینمت و نتونم باهات حرف بزنم، واقعاً برام سخته. میدونستم روزای سختی داشتی و رنج می‌کشیدی، ولی اصلاً فکر نمیکردم اینقدر زود بری. هنوز کلی چیز داشتیم که باید باهم تجربه می‌کردیم.
همیشه دوست داشتی آخرین جام جهانی رو بازی کنم. چند روز قبل شروع مسابقات حالت بدتر شد، ولی من ادامه دادم. رسیدیم به فینال، اما تو دیه نتونستی اونجا کنارمون باشی. دلم می‌خواست قهرمان بشیم و جام رو برات بیارم… ولی نشد.
واقعاً نمیدونم بدون تو چطوری باید ادامه بدم. حتی نمیدونم تا کی قراره فوتبال بازی کنم. تو از همون بچگی همیشه کنارم بودی؛ منو می‌بردی تمرین، بازی هامو میدیدی و هیچ‌وقت تنهام نمی‌ذاشتی.
خیلی دلم برات تنگ میشه، ولی میدونم همیشه یه جایی کنارمی. راحت بخواب بابا… از اون بالا هم مثل همیشه حواست به ما باشه.
ممنونم برای همه‌چی. دوستت دارم بابا
❤
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/82125" target="_blank">📅 18:40 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82124">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiU3Y173BX9HIdmCLQxe8Fp-r06hr83WzNkQScdKVdoQei2XxML4AWmXOdkfLNF7mF6LZ7UZD7_1qFM-_coIjuSAISjMzOhlLY4dFnLlYjCz4cf3Z4RjsUtnos7BILe1FKQMVQcbQSsvnBKgfSCzCYC_Zbm2h3RUw_3MlQs641CkYZTX1X4DXsLd8uDp0dFhsslEBlP3o9XweLeo9oL_Qx3Kt5AaqtrToCPhdwy0KB1i3-xqUoJKHoY3Jld6yB2z2kKH-UunAbChGgkLkd4YcdG_jopCzOh7xGiC-36-uWmgm-98VOBxiUhCPyl39896jvCoqf-wYLhV7NhUB4eeaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر پوریا ادرویت به سپهر خلسه ویو بده؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/82124" target="_blank">📅 18:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82123">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-ZEPjPVwL4OnSwFsgWqqfMPThA9w6ksKtY3nSg6aFeNITvbWHG7UZLz03SGPDnPz0efxrXnt-i_DIdLHGHnLer1SseXta-QRnaRFt--yYoIZieAAvdcwnkCCDvS8h1Nz8o2D6acrdenp4Ra1LamPhmbAW5k2v-fRDULTjGwBQSuarkK9Rw5EmPYWklph9yPdwDrLeXbrDZg5DcH2i8gcf-unI57LHcZNgMZTFEE-0GtPPXKHSG8bUxZQ-H-e5i3veZhRXbcHTS1JNSwrNTx-hhI79bM7JkMR3ogph-xUBDVLAp3tk18JWnopM2o6ippyeyiuTeSI7f4iih7FvOrig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی دوس دارم بدونم کی این توهم هارو بهتون تزریق میکنه پسر
پوریا ادرویت به سپهر خلسه ویو بده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82123" target="_blank">📅 18:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82122">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVV52j09wys293fccbsx_ieJUeehK8ZJ_NBmnaP8yHqGcton82x2fdzvDni-i3PRNy-WzIF8kuQA8oWmMlgFiCAqJfRhtLGo33iYqxfbHLZJ3qvZmwTeo33fq6g-l63Ad1YE6qGLFSOL-0diqFU2alhbGZ_P3BFKwlZdlrlkYZ437-H3u_DtW6dFB5G-jQG9ZPA5I1DlPyNLXCavtU-PCckjTgZMvL2_oxAwwgkM7OIUZZEeYpuQX2XuqGgv3XD-iLJXrvQAxHy3yphBFfN62H4y4wOeE526jE-4tjWtLe9vsZp_nGa0lUtjiNCjZPFSzsW-vXawTOZE3xIwN529GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راستی، این یارو که چتای ملتفت رو پخش کرده یه ریکورد هم از پیوی مهدیار پخش کرد که بهش عکس یهویی داده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82122" target="_blank">📅 18:02 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82121">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.   Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/82121" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82120">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YMFneadi1R0tnEbU-xCsKHFuaEvjDNwa7W_onHt2ZzTjZIEp6YX-zDc8VbkGrqmLAB1OSnQSGruQtCmpA-9EidnvwweK3hEHCt4tRmYtjI0W0ixXpy2C3_Ep0fQt7uywO1dQ-8_QOBIUfSm6zdemg6JBeAOZjGl82pNxlDDkhV1t5yvL2XQ4JNf2tLWLDia7rtSEzoRylEs3qikNehjQkxiNsmiLong5RqqM5YGiqCVrdzdrQogWxdiyoQJqF0zuLwbiHbmxzIjTF2feN2lYFT8ZXN_Y_tzJxuM7oEz5Q9buviKu6n0J2PLnlbcvS952HA1FGghvtehzHysXndwjZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید صادق به نام "گواه"  ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82120" target="_blank">📅 17:50 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82119">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خفه شید عشقم آقای واحدی ترک داده</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/82119" target="_blank">📅 17:48 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82116">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8y2LTIh43qAyeztyEcEJTc-EXnFfBh8sRHHUK4gpL2LY_JlMs2rdYSvgo3OKN_-EpyMCeHpNUJ6NxhAMvjepIBule_nD0qZpirgC9H0srCpuLwBc5x12tC9BBmcknUMtZHu7kdSHoqmPc6No_o9AbxGOLp4oFLlFtbkqOc3rKHVAIfDjlVh2BXjBhld7wSDhBKt4Zz3UQTFHD5PyrohOMKzDo-K45rRnUR02zMpgO5Esj9EUcx8yHnIUFXXrnqh2KG3JhDDaC6PsI-60P3UrSEJI7Y8epypB4JyIHkGhAPqviCAXNBVLQjV-9tJYZrFwiZzl8cXNlQqijehLb9mHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز ۳ تا اتفاق نجومی قراره همزمان تو آسمون رخ بده:
خورشیدگرفتگی، هم‌نشینی ۶ سیاره و اوج بارش شهابی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82116" target="_blank">📅 17:28 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82115">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcPT2Bg6_oi1kZzsvH87WlKLQDsPs0Id7Dc2S8OS2ffJU-6_lKX60Oqz09eZK0lgKRpIzTq8g380OhiQ6BNqif5m2mCpQF7jcE21SjuNE0emsnigzBZ9mVUil0-amfPcV_U4Y9Gz03e0yAGhmcCqT3ubfv8km4OUVFySwU-DNicsVQRq41O31bdxseWDhXI_zuNP_THgmCsDPTqZr_SyQfJ5EODzuKmHdlmFVdTGOBNgKPqJsDZbCLogaL6OwsTsAlJJIXvd8EhUbN1em-D1m-GltmdjBa5eYfZ_tsFCnjbri1pdOsobCzackUASRONLzNZXxNv5GUz2IwYNt1Xj-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو فنا و مسی فنا باهم دیگ دوست باشید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82115" target="_blank">📅 17:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82114">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUJ6bE0u0aAXZ0DJ7UrPxEBUriL25SiD4T6BPa47r-dWSZ4BxD4e3ROYqPOB7F9EJMDJW-HWKgJzuliFAXiDIW__TmxVaR_sZHaMeWawtv5sfp7PmwTisCH5jfJImfITJhaIYJu0uIqANcqt4fAhPiremcbD9ANBF7QRHAnQdb3POJp97rdgCgmTLkCi4BMmNqAeB_U804pmT_eTj38ItrzoneAOXv7J4wbz9wuWE3mCTojrt4dHdXLgx0e1uCAZtbXM8DZsrj34Nqxg_KM7aSxkMzaZHbXmjpMCeUwAjJIwRJopr81l-3VZajCTo85GgcsrGqLL3UdT6DUJJXN7lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خورخه مسی، پدر لیونل مسی در سن 68 سالگی بعد از یک دوره بیماری سخت درگذشت  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82114" target="_blank">📅 16:57 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82113">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیروز دعوا سر این بود که کی کیو فید کرده، تا خلسه اومد و نشون داد دود از کنده بلند میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82113" target="_blank">📅 16:37 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82112">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">زاکانی، شهردار تهران: موشک مستقیم به طبقه آقا مجتبی خورد؛ همسرشان، شهید و خود ایشان مجروح شدند.
پس از حمله، اطرافیان قصد انجام اقدامات درمانی و بخیه جراحت را داشتند، اما رهبری در همان شرایط نیز دغدغه اقامه نماز داشتند و یکی از حاضران از آرامش، مهربانی و توکل بالای ایشان در لحظات پس از حمله سخن گفته است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82112" target="_blank">📅 15:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82111">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ویسای خلسه یه جا خطاب به خشی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82111" target="_blank">📅 13:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82108">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزارت خارجه پاکستان:
پرونده میانجی‌گری بین واشنگتن و تهران را نبسته‌ایم و امکان تمدید دوره ۶۰ روزه در یادداشت تفاهم وجود دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82108" target="_blank">📅 13:15 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82107">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uP2tapPJmmE85lw53uBxlnKk3ozsOYDma5YZAMzcb1OV_kstNWHB4_ooBPJBVrOceQXCPdkPrQDV2-PaX7gAs_1BTakWVUtputKhHXnk9gxRjrwKmVzaC0W7hk5mAgKzsIH-J-OAEwuNnNMkEWYHxU-Gcglv_xjcG6l2lqEeHXu025iWu3fLpOukqoYNzeESsPxYnZ5eze12IIWX1cJNe1TnJt4aZyyCmYKkzO8M_Ot7-9sS9MiANEvxi85KnzPz7YeGb9pUOcIjSykd4oAOe8fpaPsgcbdrLkYuReRUPKeVViW688wI1P0XyvgoYYhKNcKvJNF9PWQqOBRZVTfHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به مناسبت عروسیش یه قصر چند میلیون دلاری زده به نام خانومش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82107" target="_blank">📅 12:09 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dW7wfWnZSyiudgF4VFR1BEk591gYN92BK22RO2SLBPEhSoPRU0DScI7Fy4EoxpSrM0NI2PGztcyBprSQdZSBwCcGGU8QpFgtHg1fgbjvLsM03ZIxa_yTzdZF_HItkY-ztTvMDwLIDMSzrpU1Zh1QMYdMGUKytEmXYk-2EXhbsSa65pu11SOCoaCk7YB53CrQmUpLb_4UyY9O6sRVbavImnMijtnrjHewH2ApIxNnnIcpSHYTuNnolUmWLxzgiP_eULlk12mNZhef0ESdLSc5cv7P1cA8PD5Hyxor4sGdKkwIAz7xv4_lNQoGu8lnYSuVhJzWPg8h9M_xpld5jM5MhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKMTWej1RKuIDI9qkfnYuW8JoWzohLku1GrjRCZunFd3CNAvcHP4HfdIfMK88hJXDtycjXCmqrPvqrIxOgyXkhdFj0k7YgbrW7nuT8uR6U7Efq7omViLR2f9HApK-1bwEmPTsIcU9WxRVtG4g3WkYgcOpqcyqITQeGHKf4HNtkZHKmzBVj9Q6axNglUCUy5ehdN0Cyami9PjZmMoGCRtyj-nN_KnE3UsRDCUcyH-SFAG0ssNXjfU-cc1RAP1LwYDuHxS7nP4ppfQEEglak3gLrKEDMEvJfhbyiN40DsjUxduAojjR75AysuwvSHkvRFKr_Mud81vtOL_TnaPxhOm7g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پسر شایع نسخه مینیمال خودشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82104" target="_blank">📅 10:16 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=LOm-VvcQ3HWP9eVKW8X-k8ZxLGpnNdNlnIoMZTYbUOp6w0Tcf7UdDpsTW9IcMVGPry1zz3JpVF8B2AWVYJkVLm6qJy2ynDUOFoOxrQrQFZq8dfto7CbqP8mFMiLEvGvf22X1kl4mX2sHzQmsp0U6zb6eP7UXj0bln3NdemiItnBVWEKW9zW2mICv-0cqCxW-82r2uJUL6xZc3lXYcpb54sGDNu0VssqLzS-_0TCXLCeM89hpEC-VzNG0rEikZ5L_YnLy3lX6Wr8i__xwTgtAdSRnJZfyzUUMobA9E0AiMzQkQZSi9OLz4eKE-DXGq3wiVoAaEoIOcoKFcxiCsloxcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be999c32f.mp4?token=LOm-VvcQ3HWP9eVKW8X-k8ZxLGpnNdNlnIoMZTYbUOp6w0Tcf7UdDpsTW9IcMVGPry1zz3JpVF8B2AWVYJkVLm6qJy2ynDUOFoOxrQrQFZq8dfto7CbqP8mFMiLEvGvf22X1kl4mX2sHzQmsp0U6zb6eP7UXj0bln3NdemiItnBVWEKW9zW2mICv-0cqCxW-82r2uJUL6xZc3lXYcpb54sGDNu0VssqLzS-_0TCXLCeM89hpEC-VzNG0rEikZ5L_YnLy3lX6Wr8i__xwTgtAdSRnJZfyzUUMobA9E0AiMzQkQZSi9OLz4eKE-DXGq3wiVoAaEoIOcoKFcxiCsloxcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تروخدا یکی از دوست آشنا های این ببرتش تیمارستانی جایی درمان بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/82103" target="_blank">📅 02:29 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کیر تو بارسلونای بدون فران تورس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82102" target="_blank">📅 01:25 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82101">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم دیگه نخونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82101" target="_blank">📅 00:14 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82100">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">چشماش دنیام بودا
دلبر بی ناموس
🤙
🤙</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82100" target="_blank">📅 23:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82099">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlMndw_EhMaABeFitgvUgjXTbXQ51PotSV5kDzAo7ExehWh5Fvp2qCn4HhXG8zfmXC6J2sMR0y2pBWqKc9y9T8Ta0MgvFc_zrXUs6UFAf2PtoZGiVG1Wq1Gqdy2g92ov4fzrfsexthEuoDE_fUzMOyQYgZpfU53i2zobTz9qOY3XkrAxPQ7oZxYClfg8n0uV6ZooSAVxrNSx7HWS8omnjBMOnD7zJhPWbWv2Sxwt4n7Zh2JKLPbfAZcrpFvhceRHLKBbiP1N3vVG6Nw9YFNy0vcRfpqsKb9b04J4MIMdCkVt3BD0Yrr_eYSu__YhO_MfHVnqRVmIQ_aeHASEpSTlaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس فقط یه کپشن "حسبی الله" کم داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82099" target="_blank">📅 23:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82098">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNoah</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1pn11jD1uzyXt2sxnc-QHWgEPHw53omS8z0EtT9jeOfS1ujbN8-ZfXytn9PQlM0EIuzdioimcorBAiHYw-MV87IawCr3i5WF6OmITBSLikj56XkxvKZKwLr3fc-HjlsNHptER2QLU7D4TsvMI2vh7RsG_AxSSeu5ucyMcaCB9aS1mgxuKcZseBGt9Fo6JhDjtLnk5P3nHrMx-l63MdVZWQgzT5P0XRvag-nTMMhbRk6km2XAWhuvERFEuKvs1ZJgUijsqxNxD4L7gDNuP0HwoD3fnqSR0OmYN4Ldsx3O-qWS-qvMA1tp6YyKd-5HbYeCrNeFHhK-oW9egejvN-NuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو حرومزاده یعنی چی که اسپید رو دعوت نکردی به عروسیت، من بت زده بودم روش</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82098" target="_blank">📅 23:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82097">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1sHmuAc9iOdLcU_qhlTSuE2GqUPmcQQQ_LW1Rz9cm4FIv3HdhZUV1GjY3m4u4UhRoaOieS-2stCx49uJF-whdXk477GtO2SaqwItOVpPwuGQA0P7B7cbHLhO8dG4KuIvf2fLOjxkbogDZBeaqdYaTOSSS7hOty0FrYOSeTsdk238xux-yeNoVdxqgsqO0mr18ZaQq4qJPJRnDwoay9DdUzp2-vs26GTlbS_wuZ1It5hTyfI-n8EZ-kYunHw5MTtU__pOuwmHM0TbYZpJJmjlkpi23851zu_quqpzQTdfWNaDJ4l_p0yAuVgCH-lexCgoYmDWtdPQVcwxn3D3-MDzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این رسما دزدیه‌بخدا</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82097" target="_blank">📅 23:03 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82096">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رونالدو و جورجینا به قاطی مرغا
هیر وی گو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82096" target="_blank">📅 22:56 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82095">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuCBDqUirVusdj4NpBNd9KUV4ngrf9jLCUNL-EpCxHgxV-S53vaP0Jy5raHgPlzhdN8cHeUqvNgA-VZSainduxX46-t3VZ2dYv_jsVIqEOzRh3_Kh7xC_62DIhzSE2W8KicQOqtLEvByEHjKVCO44WKC59sV0q9GawpPeaCtsQWlaQWu0OA6k20rDo7WD5sHKbmGS5AFM_tK0A8ODbapvv2IBUravYKZI0fBH5xsXr9faVXgVg127UzEypxtq5-dFfm3tgFPBvKlsT9-5klj4lD3GMnNygrukX0UNVP1B3w60D4HwwD1SMQBvHlGFrFWlKi1wC6TNru6o9uGB66dQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داود کیم، خواننده سابق کیپاپ از مسلمان شدن میگوید: صدای اذان در تمام خیابان های کره شنیده خواهد شد و گفت امیدوار است بتواند به ترویج اسلام در کره ادامه دهد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82095" target="_blank">📅 22:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82094">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82094" target="_blank">📅 21:07 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82093">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آلبوم جدید خلسه به اسم " Margo Zendegi " منتشر شد.   SoundCloud   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82093" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82092">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mB9UJ_ldFbRcPKtLECazr6L-EyddRnIQYeMQO9-suhEHQ5DMcRQgB984aqzRkgNgLonb5t1HFuywMwob9PQPcAWUWr3YkyB97wiC9QPOclwRSr3m5L_fdYkEpVUJgiC50A2KrqQeZWAp4ZP5dPxpSxaxG02O_a8ppqFGlVlMlmqw_GdNZ0osQnD6lxq7CFXrxVXCO8oupqWGFR49hJbb4NVtD_MPu9uH9uovz_drKxFs5nurmNObUK0s4PEyXtCHPLeUkq7meNbZz6heTbtwHL-5ORw9HJi3Ol3ZDrJlHlJgUTjiQjSBy4eAmkxzl505osyjLWBdYJ1PIFQQv3cZBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید خلسه به اسم "
Margo Zendegi
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82092" target="_blank">📅 21:02 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82091">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_tcCZybPAirNmI5iFRw_n5B3dhpKOm06epDyz9yAjO11_2aEXtoSOQO4nhhkzy7AviCjyHI-qvz_EkVpL8xOD61wFtZ007mJnvMAdCgh9FuwyiQtXdLd1MbpmXIS6J0ZF1Nqs71HNOE8iucbrmfdvRJ7AhBy1lUu8tE5tDOc74fuir3PhYIw1hi2HkaIEvBfMgXSV9LXJsfRFGY5TGfyfOIpqbESgbReJVPqtYA1nOetvo90bbIZ4AnzGg7-TG-c0H91wMGYX-9jvblTEiAOsyNQfMM4NhpeOvw20lNkitS1u82fUsZPGaISs9M-ll8ycfKV77gNTx0_-GwiW8N2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#ایده
#تتو
#مهدی
#پسرعمو
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82091" target="_blank">📅 20:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82090">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrsdmWExVf6KCsiNk4t5xs5ZU6GR7swl6CO4x_YMc3SmORgpj56nQvBu8uOviVWx5PWteZRYz3wFg5zTZweAWK0Mj3RKtyr5mE-PqSXFp0W1Tc5CSpLasLNt-8iZrzbaUSCJb9I2VZg1dLjvyjj3kqB_y7DM-5-d9R8gBE8MNyLnQWUJrNOwKo39IsKMTyHs3JXKaJ2U8tF3-wFP0cup27aF1O9EdffcUKPPkbgXz5t3ZPvfN_OMdOC7zVsDONNbZSGgRBZrLhoRUVFeNvFMiIDBkkaimWpMZni8eUqs47QqKuw3RiZVGnTbTpMjSmf59PzR1ItmInWny6e5HFt09w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علم‌الهدی : اونایی که داخل کشور میگن جنگ رو تموم کنید، یا بی‌عقل و مریضن یا منافق؛
فکر نکنید اگه جنگ تموم بشه آمریکا دست از سر ما برمی‌داره، حتی اگه همه‌چی رو هم بهش بدیم، باز راضی نمیشه و در نهایت وارد کشور می‌شه و حمله زمینی می‌کنه.
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82090" target="_blank">📅 19:45 · 20 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
