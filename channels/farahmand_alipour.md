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
<img src="https://cdn4.telesco.pe/file/EV2MqBw1UVHiVE985kcfIKpVREe4wNLiDznHDuk7drhdh2seC384itudXtYEokGSo4bL9VnDJI9MMZd8o7LpFfh0_Z0nOwUDuuME4b0yaioALblflBX7BsLnXiX6BFhs5HnWjvCX_KRAxsk6KxYzcX05PM8bIORt2RHJkmJsoTyUndNhDZCY3GM9cC97l75lSambeShB9wYfT7jeyH3vhdsYzPMLQC9dQqjkXcH8cQ_e-MCyJNGBWAHy8YqbnsfMiY4IfX8kNCuMuREbRN6dpZuGe8fTutx4YFWxcut_1TyvTEZWVcFJLb_mmKFQGDCWRxS3BjEsqVtVNlrFCCAAtw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.9K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 08:42:55</div>
<hr>

<div class="tg-post" id="msg-6399">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g2jvxndXuOlDQ90AS4zSGOMX9a898jsjr8sv3dRWPhb-jHNTbppzu0wHR2u3nPPCIa2kQ13MAftcNDA5C15hlyvmWitzWY-eu5RHfFcUgM_-OrcUBVGu6QTlicHiP_ZXgZJMYGhUO4IdyB-X7PjZf2faOOJ1FEd4fJObt5xlo9hhALXC2yyvhJfUD0ik4VSFoGM8J2UDoggZ4X4qVj_UlnIDP40Y94GFlWbt62bme7hvhZEq2JH_LbPiEt2y3krTRG5u7epc2cfL3tmq3QG-7bxrQhJo7ubGcsZJqj7U2_MeDTL9sHbZXsumbwdRCtc53QSWFFSSzrXOpRVrO3-ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دائم میگن اگه جنگ زمینی بشه دیگه قطعا ما پیروزیم!  این تصویری از عراقه و نیروی قدرتمند زمینی ارتش عراق!  نیروی زمینی که پشتیبانی هوایی نداشته باشه وضعش این میشه!  فکر میکنن سرباز آمریکایی قراره مستقیما  بیاد با سربازان ایرانی بجنگه. بالای سر اون سرباز…</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/farahmand_alipour/6399" target="_blank">📅 08:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6398">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9aPxx-ivjmeebdwMhUPzMmBWJpkYla_Xuv6QeLWSjWSFrJE7Fwmjw9I5b1cjQ6sjBTkwoFBS5FtEj6_pHYjXXpBxX95jsrcHb1EWMdeTRcEQTkv7X9t7n0eYDRxyV1ngsecIv1Dnf9RSFCG8wU9lG4BXqRLFAJ2PEoBxp5b_sU53LzjLuR6JdV_5673tscO_RQJgqGMd-VktOu8ZCvziRkGq9tDjcsXMr6u7CdIcoenWluSpdFHKQaG--jG4mCcaRrg86CuTCz2N0XfXniMAL96cKLLPt71EgktRMnFBo3zt2VrDMhap-XfekVCdHTPvNEppxJyg0hI-rMmGSjTlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست! ۲- اینکه جزایر رو بگیرن،  اتفاقی نمی‌افته! جزایر خودمون  رو میزنیم و بعد پس میگیریم!   اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/farahmand_alipour/6398" target="_blank">📅 08:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6397">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">۱- جنگ زمینی چیز بدی نیست!
۲- اینکه جزایر رو بگیرن،
اتفاقی نمی‌افته! جزایر خودمون
رو میزنیم و بعد پس میگیریم!
اینها قبلش میگفتن آمریکا جرات حمله به ج‌ا رو نداره! امروز میگن، حالا جزایر رو بگیره هم مهم نیست! قدم به قدم!</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farahmand_alipour/6397" target="_blank">📅 08:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6396">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TtxaaGa2NHgdANT6h6NVASJI_uCrr1X6OkpWbWA_CK2TIviPIeIQi9MYYFHKuUsTXjpvk_aw3gIi3rLa0ff6Y0NNlI3wHEBrzWoHd3UsB56U2f2lp3fCxKlG4YqQCDPar43PzAd97dUIEZo68MhH8gdcYmSbef6POekZynlaY_8dhhEP_sIAPFMahunBSlhAKjFzFg4SDajTLxbimArdzwLWd5mmG3oJCoGoUd8MAgnMXjch9bVJiJH7xW_i80VfxW_1C9qg-i3j1JMo4aGqclXhmzcwLz8dGYsAnUuY8-UD_JGqKcdIBMIbgkLT2IvK2K8l3JfYr7Vmm9ped5j-HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۱۵۰ میلیون دلار
هم براش هزینه کردن</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6396" target="_blank">📅 21:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6392">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YDyfFjTye7nEyMKk_CTVYaigurmUBdJjjq25DtfPE9NSbgCmj3Mctf2Cx-ExX1liX1ZKNZvEDaRerfTiaLg3o9htunliWUtKSM0-FLKk4q2BsaQfPA_ZrYz4Gr5T2fZDqXf61zJumnnWWv_dIPxdQCpD4GSD-kok-n2Ad1vnBexqc7mB5DLlM45MdpTDeCLqWF5aYx_7E-mSpY6SG12qy4oc7xj1fkZyHB8IKWm7xpu1nBBbKBObX2zWcYHU9B1S3zLqwPXzbIvvAfd2FtuPmNyHLFsSmfDnqv9GJfcrYmOU89E6arkeWWbkowcCrMIwlAaZnBe32z1SJEgK8PIJHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tq4FFCiSrLHABNGk-4kB30QMBZ-uszNP8idHLG2880AavKf_iydTe9v5LrH-7aMXbtUsTinNvvT-IHgIhyHOpyxsbgVcwhI9RyF6VU0DBDMqzjBzTc7OXXJYNWme_-mXideRLGGdBusb9wjnbOaLJ0NEtUjDNBLQux55aps9rr7ca4UbGUMyyzKRasT_nBpRh1plOy7Q6ZbomlpzlPy8r1GKVc-JXS6zL985Q1mOQgUgK_loHpcP86zA_VFn2DrWpgFbtqR2Q-Csc1kElIFi9z7NKWsARexoOOpqe0RpUlRNkBwUZ4qYwN7QsSQ5KCgfXP2ap70spGmpr8g5PLqO3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTQhEZCUZ4qWZcT0th3x3TDgLdupWpnF63h9KEvI-llq1J0B2FLubTq7cHBD65DjpuWHZsTE3WadJg86WRU_R6Eny64I8tuMPJnpKewW5MEXp7Rm4241HiSjci8_k19RMY4vJqD_GIqYr3630gEn2dQtV0TKv75nULaPuHHSOrf5eU5-tVP-7QwQ7jaAsA0NjUplR6gULfuqLkT-YdfS50N0kPq6E3F9Zxy1i1mWeuEDspN_uJAwijN7xM5BF5-RokNzKzntgK7PwLDN2mjTC4dEDJ4zr8T0eDbYgoGgitoT5Lc0ELGJ9IE7OngdfSPKBVAUfn7oZ_kgWnUrge5sVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JwipT02uG6P8hl5vwe9yOk0IBbKqvGpT7zRYYGaHm6V2pYh1SJ7DoFG4X_sn2b_zFinp3KCWjWtQI3OfbDEd3zrJWj7JwpxQMvrIUGa5xQemRKYKJgq4VuBEyMM7WEkWpLDXnhXGAgP0pgHV4cpXqZvkX0DWFWkhiW0aHcB9MIAH1528tsvWh6MQUtvXhpQTYDiNK401IyeCr4grpQEL-25FB82ay-N6djXNfuS4Ny6bZirRRGpyPF3jJ7ri-Jw4gv0zH-V8Z96T_v9IkSuHOagbOeGjBRvtUmuTnl5qB4e0tCeyauqoUEtyKSK6O7BTtxenoj18bWrPe8zJyzd-gQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری از ویرانی فرودگاه بوشهر
از این هواپیمای مسافربری تنها دم آن باقی مانده.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6392" target="_blank">📅 19:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6390">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">میگه ۷۰ سال پیش ما در خفت بودیم
که وقتی اسرائیل به مصر حمله کرد
حق دعا برای مصر هم نداشتم!
اما امروز باید خدا رو شکر کنیم
که از اون وضعیت به جایی رسیدیم
که آمریکا و اسرائیل مستقیم به ایران حمله کردن!
اینها از اینکه به مرکز فتنه و جنگ تبدیل شدن
احساس غرور و افتخار میکنن!
امروز با مصر قطع رابطه هستند
اسرائیل و مصر دوست هستند،
اسرائیل و آمریکا روی سر ایران بمب میریزن.
زمان شاه که در خفت بودیم هم مصر با ما دوست بود هم آمریکا، هم اسرائیل! معجزه آخوندها !</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6390" target="_blank">📅 15:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6389">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند. نیروهای سپاه پاسداران…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6389" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6388">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIranwire</strong></div>
<div class="tg-text">مراسم خاکسپاری مهدی توکلی، مدیر خانه عکاسان کُردستان، خواهرش سمیه توکلی، روان‌شناس، و مادرشان مریم اصلانی برگزار شد. این سه نفر شامگاه چهارم مرداد در پی تیراندازی نیروهای سپاه پاسداران به خودروی حامل آن‌ها در جاده بانه–مریوان جان باختند.
نیروهای سپاه پاسداران بدون اخطار یا دستور ایست به سوی خودروی این خانواده شلیک کردند.همچنین پس از این واقعه، از خانواده قربانیان خواسته شده علت جان‌باختن آن‌ها «تصادف» اعلام شود، اما خانواده تاکنون از پذیرش این درخواست خودداری کرده‌اند.
@Farsi_Iranwire</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6388" target="_blank">📅 14:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6387">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ORx1jh5LsI722c8zsmqtOIUrvwB7tJReM8fIN2JSlIXnga73Oja3H7AG7mkN-nEti7VwViQaaFSn_bM8mTXHKFzI9b3Wm5jvtoOG11-VSToYxfAmVEv6txd1KPZS7D2tMaIEBIiBQlUJwAmUzTd41y_bHbWYbOQ7gJO-_ptOyI4p-CcfHnBY5g_szyBXMSMFVpyjlY0VxrZ0bntoyvznT37EJ-1LM3Gpm2IEAqhUuh8u_5gJYjFZcM5eCtigLu5_Mtfo3ixkX9FJZg3Pr8pgKzSVvwFrUkZ5ptux6S7CdxKcrjYyKdYf7t8zvDDeMvXLqyLt8oYKIklv3IdHhVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید آن قدر آن‌ها را زد تا پدرشان را درآورد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6387" target="_blank">📅 11:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6386">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‏روایت اردشیر زاهدی از درگذشت محمدرضا شاه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6386" target="_blank">📅 10:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6385">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ue28OWgnPLlukqvma0A0ngcWlMs6EI3Qi0Bn46S9QVNMzJTIZE5Sz5gAQhJbm_1534G-SRvEitXDKBWapj1nViKTCoQba1XCM9yj1VuijvNY2emTA8iSmmvtQ_CEctnOjqRs2Smsc8LZG12jaIkregOX2xvYSbDEwwdfXsU5PckQe1Yqlo3h15Y4p8ACUS1XE96Q_V0auQUpSzunqhzRLfZP2exPId7qVGPY4RK7tUsEKQIT7lP8zbVw8N7qEpFveHiKRu8PLkNyOXj-1teUV6CL32IwgyeadEFBpGTt2PkwTm0tJbOT8aoI2aEheP7lWyOn85NXRdpKbLtIg9Oxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لعنت به ترامپ که ۶ ماه بیشتر بهش فرصت داد! تا یکی از اقداماتش،
و حاصل دو روز بیشتر عمرش، قتل عام دیماه باشه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6385" target="_blank">📅 10:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139cdb38ba.mp4?token=sJlReZHoGbPYDHalIcyssPwwsNoHZn9WnQ6z1S8rzgDNkmzpa7108QZTgANwno2Uj7rKIOYT335gfqdJjWQwfWgsJV_bZyk_gG9tdO9xaQ9OAdM5Iht04d4BLl7YiA-tv8phj77Ccg_RP4qASIodi1P0RaDmTzfY5Lx3WfCl_5qYTABr-LJ0qtG4lSOLTEVz_utykvZVzMm-UmZgc3OZkr-jjfbKz1gMLoje04HDDqlk3nAflNsEuU5UKfwY5kSasRD22yypYvfuUB-5JDwoPOrdoXXok6e95R4WB9MIx8BJJA9Y_3yaJAkg6SPnXnkTrfiQLy3nsriM0Gfnh52E2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همزمان با اذان صبح،
دو جوان رو در اصفهان و در ملا عام
اعدام کردند!
ابوالفضل سپاهی و امیرحسین صفری.
مردمی که تجمع کرده بودند به
حکومت جنایتکار جمهوری اسلامی
اعتراض کردند و درگیری‌هایی میان مردم
و نیروهای سرکوبگر رخ داد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6383" target="_blank">📅 08:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9dfafddcc2.mp4?token=omkuBje3klJEnX6kOcjSvHTgtzc4ls3NVBYwAB-f_Y3SB2ZtXiU9TSNSjHHQ_kLhSojilZxAf6pUuX7SJR6xOHGVCOB3-MJQV2lQvTnIbZAVxU61IwwZFuNPoL61ccFm8T8kLol45sdgKbyv54mXHKKr9CYsANKPVq_6g6i-wgxQCFRGMEZ1ErtiDzBWOJE1Bi0cXbowkQNL_NMZgmFnN2tjCwrLeVZrDWiP5QGPbPGjLx7oOFvFT8GFeEQJyKd-feZ1wPSee6UABijhseADblpRh5tdFlJzvEmVVrGSUN6PFnsW1EY0f8Y-XKpz9JNiUbAoNLO1-hcHadTORY-RaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرزوهای خامنه‌ای : جوان‌های ما تا ۲۰ سال دیگه همه باید عربی بدانند.
https://x.com/farahmandalipur/status/2081803094522757301?s=46</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6382" target="_blank">📅 21:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">جاویدنام مجید پوررستمی - قرچک
۱۸ دیماه ۱۴۰۴
قلب آدم هزار پاره میشه</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6381" target="_blank">📅 21:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ به شبکه ۱۲ اسرائیل: «در حال انجام مذاکرات عمیق با ایران هستیم. اگر موفق نشوند، به اقدام نظامی قدرتمند بازخواهیم گشت.»</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6380" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fdlLF1PqfzAuZc4PnNdtWgvWGTSseVtw18uVVQE3XIp5rvFLeriCGl15-xQmHZhDaBLbfiyO6VycxEQxOKte79TEMC1xbt1nbwwPCjNMN7BdMLfbasx_VLl1HjWxhHaT2hkBg6PHOrbGYBW8QUScy9r30VbmCLIiANor1Gv6BTIIWnC6t29cVcjsrbm2N6QUnZ6aSq9bNIfPVrOloAkWvn2Mb26WlWeEPeu6uH7VGpMe3i5mNm7s1RXgdUAf1ovRrhV768PjfcVqYVF0HMtcsoGsmbPxOe2lUknbP7Pf5_9hI8mGiWe_yfM4U1d_lqBXLWPBU_uhMj2ceqE4RvagSgKqccMuQiKG8lE4jBXrCxLZRZLsPSa_PTURQP0bBESXmEQEkDlh4kNX_vUQ1egmnjQcHWWVjb6L9Rll5nmCTaQRUJHupJMQeXIS10kSAJXKguCUAExlyS2LJz9vWjwBwgNw45-_gyjw6n6Cn-VwN0-YhRVS2UXEPum49n6LKHKqIE9gd-_3k-AHiZxcKIs5zBKbk2voSDw-dgt7cqE5AHLxQ6IqczP0d9yUdW0HxM6UEEKeiiAgVG2jE0J_8hfd3qdShxbE1aZGv1IKIP-rg2Iesj1KM9q3te-ZOP-hP9eC0tE4uH7O0Wn6CsZqLZOcjhad-sUSIShVuIHRmttftH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ed1a3118c.mp4?token=fdlLF1PqfzAuZc4PnNdtWgvWGTSseVtw18uVVQE3XIp5rvFLeriCGl15-xQmHZhDaBLbfiyO6VycxEQxOKte79TEMC1xbt1nbwwPCjNMN7BdMLfbasx_VLl1HjWxhHaT2hkBg6PHOrbGYBW8QUScy9r30VbmCLIiANor1Gv6BTIIWnC6t29cVcjsrbm2N6QUnZ6aSq9bNIfPVrOloAkWvn2Mb26WlWeEPeu6uH7VGpMe3i5mNm7s1RXgdUAf1ovRrhV768PjfcVqYVF0HMtcsoGsmbPxOe2lUknbP7Pf5_9hI8mGiWe_yfM4U1d_lqBXLWPBU_uhMj2ceqE4RvagSgKqccMuQiKG8lE4jBXrCxLZRZLsPSa_PTURQP0bBESXmEQEkDlh4kNX_vUQ1egmnjQcHWWVjb6L9Rll5nmCTaQRUJHupJMQeXIS10kSAJXKguCUAExlyS2LJz9vWjwBwgNw45-_gyjw6n6Cn-VwN0-YhRVS2UXEPum49n6LKHKqIE9gd-_3k-AHiZxcKIs5zBKbk2voSDw-dgt7cqE5AHLxQ6IqczP0d9yUdW0HxM6UEEKeiiAgVG2jE0J_8hfd3qdShxbE1aZGv1IKIP-rg2Iesj1KM9q3te-ZOP-hP9eC0tE4uH7O0Wn6CsZqLZOcjhad-sUSIShVuIHRmttftH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این سخنان «موسی خیابانی»
فرد شماره ۲ سازمان مجاهدین خلق
و جملات و کلماتش دقت کنید،
اول دیماه ۱۳۵۸ دانشگاه تهران.
انگار همین امروزه
و جملات یکی از سران جمهوری اسلامی!
که داره میگه
«اگر ما اهل چانه زدن و گذشت از اصول بودیم، امروز خیلی عزیزتر و گرامی‌تر بودیم.
اکنون هم که وارد این میدان شده‌ایم
باز حاضر به عدول از اصول خود نخواهیم بود.»
یکی هم اون وسط فریاد میزنه : یا حسین!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6379" target="_blank">📅 11:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8tP1c1DWMTEAkYAftndU1EodvlDawCTfCfG_ZOc96_GrTOE-ZBDocdwEPKKPmy-CfW1GAsEwZ33aUv0GmXB_OqLmCQso2IVVqJWqIH-kU1Kh_B9AGMDKds66UDOoh23IXMNdSPRoZZGK-qULnUg2-rYdRLvO4Zkt12M8HhZ3ulKW7YiKrXnW5ZtIoJ7sWdHqw71t-ND9CfIldHOizcXX0r2ekWPN0qMqQo-lvlMDABfJ7Re77TsDics6afyAYpZA6nSOz1WzX-P77rbJIZBDiUQLSpGa6z0wMG858DYu2yZEMLM-7RMfsOsvYv2pMkHvgIwuraMlClsXzchfN7M3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو راهی آمریکا شد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6378" target="_blank">📅 10:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3c95e2d9.mp4?token=bH7P08ve_MXLdEr8LyxGUCkQbZAIzfOt130_BFeXkrVUpcUj9Sp5kL3f1QLt30r0W1DMP-tp-_BX97ulV2-9u-3XGqyVdijd8nLdjw0wPjPwvMbU-Kn-Fg800GXqUFqjzKw2ITgL8h8tit7ZEMNem8T5jU7ilTPhRPrA7dfeyOXOFRRySnB5Mvgw6-2wfOZXRS36Wd3Dnf9NiIBl9l9zyZgpugODJYKPVyhyWT966eq2iKWaLKAnRPR99EHoCqm4V8tTwpiBqZBb1kn-_j0N68rROqjT3VXUXq7h4-ie4c21qb_gkp7wpV5nzJMLptKDXgFsPAOvzEX-QYw59Z0LCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله یک پهپاد سپاه به یک کشتی در تنگه هرمز</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6377" target="_blank">📅 09:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AF-WUXnUQ6Z4_CrSK6C3RdPEES4KyfrXSNeBnDaeHgcICKFss2cU-QNT4p-o5yW1qEvVCL1RRYgHP_DYbRb4k9E4SRb7AnkO0_j27u2lxY2fxnoNgJN94M1wmuX5AiyxlwN9eHfG7fbmaF7rG-R6ARa5kCFba9fwa-F0z2F4fbHznpV5DA1F45kb4ozehrHD3XUxtObDfDCmW18Umq_CwIMIbo61sYaHLNoLIMQyKm1Mc1Rl9u4yYxHl_GC4thJRWSI9Ctu_nG9Tlxmo2YmstwUslwIAzO7CMWgiHGEH9z841JTUZfMUQ-xAy0r8eGZ2wYhJTaY8zt6Bm12ptFRGBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«مسیر ناامن»
منظورشون آب‌های ساحلی عمانه
چون از مسیر ناامن میرن، با موشک بهشون میزنن :)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6376" target="_blank">📅 08:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6375">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">۷۰ سال داستان دلار و تومان</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6375" target="_blank">📅 08:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6374">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diUaDXvPnal0vQ2REeWbtSOLFn8aQnwWBe1twdnwadl2YxoEKCVNWC0KDDKz18YE0yMQ6tsS9KttJl9XtHmswWdpdXMQs9SaBv35pbXNEm54ZOvEFDO0FY4Rr1K4fwXGt4UBq18w1HmARHrqPUWTU9rNcO3_I9qTgcsl5Q5XbuP2l3VVgoMkwox5uLn13k9bghQpJfbs8Taseo1xvAdQDO42stuboner50mzptRe08_OuudgtGa_EdzCY8-P5fBzls6c_S018iwZ0O_4TUCMzc_hN789tJ5NjhBeQx4ylbHrfTHLFa8Y0pC7vM4I0QoSdWpEMMmNTtZW8lHUdOc1sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشسته هی طرح میزنه و منتشر میکنه :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6374" target="_blank">📅 00:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoLAxPKtM3nzpqwTZLC5hY3vbWMEmW5EYEhMnQNDm1fqcWIPwW0HobutvHpTiNdyY-BM93L7JzHaG-2W1QqwapJy8lwaGqd2nIbZtJ8qDMpgkUG79cK9zhnRlLoJFMj5Dj2lOhwtZyD1josEqhiyUY4-xUwdzN-COA1vInmVgGFpSZgOeY8tJQMyV1sxxmZfLQquOwyg1WliNqxKnh4gGfgftFjlGXHyFVnCGZCbR8s9HEaSMZCqU-rQvJvJwCbVA09RdyuihDZcMJ1bbmHsdwhcZyW1cS5I8n8p5kIDnyvZ4di2DFpXHDIBBMamiHbE9-AluvI2_ssmeZtCJSSkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QragmgcKxpPhNdTSGM2-XVJZgfdyrxx58bePot4R-dd6xxrDou8NvLfG-PT2Jw6Hml3zCXRZhcFG5pdY-LqTOFlfuOIj4lSKyTmmg6hzHxzJCwSoIXJJJCgTiCuxfuZSGVOP0xfX4uzsIvWhcFkYZJuH92VCfDRbQL2JHyd44ZhpYmdBIH-Vddfgr-WFsRvTOz-uD5lDPjqub5z50CeJzVLzghawUqGtsiDGbLvNmzkRkfh75LBRBz-Pv9pXwhHyHKWtTOjVWIYZK2ofAQ3ntkdDPn_G7T_iRYedcXA-2bvV7tsQE96FoWIVbDNKcb_aE5ysxQ0B3bdks_GQCyKI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKXRKNYZMCB9tFTxGpTVqk5TfCbH8suu4T1Q_AJ3QHaAnTklzZV80D6yWFkuudG1emedovQhjiHZP_RBB4EfRjek5y1fHSLxGVFpwj8zXBVJPmmvC44sIX7a2x_ZVH1xH0B7GBPpGKuYNP0SG06zNG50PyXgkifl4IY7lXltvzB9V9sYzOwTdP6HUlff6jM5-Y0UxcVTZo-Hr1RUP5sEKthZ7ZYZDLky-k9TPo4JGsGvsTi7xOUF5T6_sAZdZSVp5ux2_N6rQxCHbC27BcMFkiFFY11z1ReApisMpsOPdyfcoUE5-Rka8AMAfeLVJjQWYa6vz8pviPO0_6hqUT6cnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طرح‌هایی که ترامپ با هوش مصنوعی درست کرده :)
حمله به خارک و تصرف نفتکش و… رو :)</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6371" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqLA36zwnReJBM_sl-zdcnFLoY_tEt8lyvKA2gkE7gh1Pl1lcSJlQrESd8tOQXMTnU9V3fdsPluU0wYDT3PwrckYk8Ai2s60vQkoLiXLx7AWfPCc7mtfMO1leRGPcpoK_vfaPM_aS7NyHws_okPEVnX9M-1z1iHGbQMYfnbAtLC4tyJV0V-_c7gnu3G0q_sIuDdPcxxO60FVgmuObenWpVw7ltSihPUj_HRKxYMDFNyjuAZbk8Vjxb8YK0F-yzxwS4351FAjQcrkITY3rT1Tw65x_CBsT9F8jZz06cyhpG-x6iIOAtYv12NJVt4_zwVUK7yXHb0KhY37kwaLhFkjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامه منتسب به مجتبی خامنه‌ای :
در برابر آمریکا و اسرائیل راهی
جز مقاومت نمانده.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6370" target="_blank">📅 21:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6366">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRVA0tSt2A1H_l1rJ6gWcfvQswxx89E1AeYJE50twtk3WFrgpnrxUr4wML-LYNPR4yR2jxRYTsh_sMyXYZbRHE65I3NomGTmGyn_7kvm60VdgptPgoKn8l26OXkc4N8rm5WAFBviKUttTskwzTsDv95HQi1l9VsmBFqVgke3rIilC_6FALNttrEVW1Uxy25eBh8-hitR8XzqJwWs9_SnUgi0tKFeWj04HdIkJmmeNDzFEh9xDqh2iZ2DAcwSVSVlfcjq3kTMR2KzvvjJc_6jFbYiPvK8jHEEEG4ymIHTfWPw68J6jGahCNhEKu944DmgETmMdL6b9loThFpFJYcVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nlv6fkaYbN0JckB8PdCY2PbBPRkSrhvCXjYAFJjsTrbkruL9x_m67cUEjl-EByQaEU9nz_lSxpVcvXLIZnD2mld864XHqIahN9CAjqSwNnsJJdAEHzuMv2AI_GfoMrKFVNfDUYrUs4kJszxzhYhXePN_3P-uXVcu6p05Q5fxG_kgd-y3RuDR29INDJc3XyYEO-qFtX8lhxlOw5YXwkZPdvctHMmMqyadaoj-YB0Pmh742e7NSDPKxehLtAazINv8WrdUHU7JZEBtBgSH8yESHMxn9H6pjvd20hZ9uMtkw1ctoZwqwPhHHbLs0Ofh9irT1Euy3AV6UawZxNX3yJTs9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gt7sOTfqJyf7Ou5wKCgtbUGj0l58U7Eag7NZ0lrSsXF061A6TMpf_HmGspPugo_vm9ify0r2QZQSBN6eTjdNlYSp4eH-q13_hv82rgB2oPbQP9zdU-Mbi-AFZNNPqoIS-X4n5iWLGRozjgJ5Y6yz5FSA72h-QQiMZtRTpmhjdMiqyAMBYFG78NWrWf9dAT0T_mLSsPvqiNP0AoxAuARddx1es0dOCAqKXLsOD-oi5T_uM4YA89BDPx-CyRi5-s7Eer7LNo5VNBSKeN7aChs_PMHiDCJgmAxFjmZRL1e1to6aDn0i90F8nF8h999xk1agOi2rl8dNppB4eVSnovpRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DkLISPxNpxYWMgGWnFG3lCB0K5kazOHgZiX41gbbcjBlY0VL64tqJ7xe67f6uFh3l1dfta-NdJFmzACbayX8lFBpaT39IpRNW-JdhNfaLwet3HA23R16H3gHVsa0DnmWYkhTEiYZt9KeZTnBCkYiF2kmTYcbZvG8nTywckDBI7KMaQtnvMD00HWVNEBtc5rdwnba2U8yTg4QlPsCGixHb8eKvMPy_aGZXBx9awT5udftNun-Ly4x9qKhwNB4F8BQUi4F_D9-m5bJbbiQAXUYcvG8pHAJH-gpdJ6jOWRc5AtksYPD6BJfHoQ1Rjy5uqdv_Sqi9ohqfTg9qgeEekfkhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جنگ اوکراین
تا دیروز افتخار میکردن
امروز نوبت انکاره</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6366" target="_blank">📅 20:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6365">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">۱۱ سال پیش
خامنه‌ای با غرور و تکبر از مسلح کردن غزه میگه و اینکه باید کرانه باختری رو هم مسلح کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6365" target="_blank">📅 20:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6364">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkEEdF9OL011KrerXXCC713wijG_u4QpiqPH5EFMjgLOa-NTmENtWT_sHAnlIOlp1sB9ZqqsYNKEcyJPJvIZAyzOhMDYbqhcIU4C0eHd3EVH3MZTX-s6UiD6XvSrsnsagwoNyKJdgVR6zfOk5d3jXVLFY5wmfcw9Gs2abtMsVXv3Ctg6-746ItQmoej-MBvUJxDTvDl3NVrzQVtjUEU_KZ5DkLIBm1JmXxpXtc5MrZ4lHa_4CX21UtuuhTtpK1QreI-SJtW4IuqStv6nzx7XUH5N_GKYplp8w0sZrpjBsYIQbZnP62HW1BxrF5gUthHYcu0NajgyRfNwZFbCGqZr8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6364" target="_blank">📅 17:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6363">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxJireQUQR6crzuJv80rawEntPZ8Z5WfdmyxcqFIU2pUyMKNR7GpDH0DtsUBn_g-KcrSKPpMM14rNMyctJl1dMF5erj4TnTVCI_Bn7vLlSKekA3peRIAgHC8WL7o6ClT7ubZSTdT1orqMGNiRwOx69Ccf4bSPPiqT2m9qgUVJntHIHNYUg7a85DfV7wCqqEO973Dc8dm7fNVAomlrHSFGtxtPVroVvPPBEtI0F5OLFyyQ4uZ9Avldqe-wUtvswwy77kgkgGtKP4GJF_OHhQ6ke-ijH0oXxRHdgicpOmO62M1OWgte_pUuly22Gv_YsNKwlvCnUWkt_wlwh7LrxOl9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه‌های حکومتی از برخورد یک کشتی با مین در تنگه هرمز و وقوع انفجار خبر دادند.
مین گذاری توسط ج‌ا انجام شده بود.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6363" target="_blank">📅 16:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rdN5ED23n2sV2FDPAHlG7y9iFdQvucRaoYzyVP03ThR9nxucpqBcBWr2newoTOio4s2E0HXIUV5osaUxL9BATmVH328XaZcCQ7cfRfIy7hMqgsme5GWDIjakB5eyOMKPl_fb9t7hoM8TdLjUI8JOIA7yIZWfpokBTq3DkpuV50X2tORm0Bl6wUREC463SGWI7hEid2_6rAm6YcQ2UAGoTguQEdq9Q3koxTsWWJ1oSjSDDBJhYoeWLwKjzJxi2_Dx-ROsm1uIerV8IXSCC2e21v_3VV8bvdhVRev_EIsJ33b9gi8YLbhTuRtqVufSOW42j3amDa-JanNxR3say5uw1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oxk5caku7fSoBNSTzzW4OQD4dlZQcFNO05lTJYx8Smrfvk5lZYHsGDWGjsUvlxvqDzigrja2pn29Z1KVHMe9GQRM7S6QwWi8kTfNyHQ_QycOI4D_2s7-o_gkuSe0KrX9kuNP7YnK-n6-XJzIIGSKmkWv-dYibV_BodzQreQ8pHYWv6vJySqkrFiMZppDc_gRFkhS4URPpC97QrYUQ_ehe1rVvmQzqEPFLjv1Bh3_7a9LjZkMg-QAMrdJfzlCyWQFko9Off0-NHttokzHRUQsEUsHaGaXmLMirOfmwp5ClA7s5Q1mMH_HHg_rTAJYgv99U88m2PJYll3OT89WFIyXfA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینکه بارها نوشتم، چپ‌ها، با اینکه گروه گروه توسط ج‌ا «اعدام» شدند، آواره شدند،  نابود شدند و ماهیت سرکوبگر جمهوری اسلامی را به خوبی می‌شناسن،
اما نوبت به تقابل جمهوری اسلامی
و آمریکا که میرسه، یهو مصمم و قاطع
میرن کنار جمهوری اسلامی می‌ایستن
و ازش دفاع میکنن،
این یک نمونه‌اش!
به خاطر اینکه برای اینها مبارزه با آمریکا
مهمتر است! اولویت اصلی است و اینگونه است که جمهوری اسلامی تبدیل به یک متحد میشه براشون که باید ازش حمایت کرد!
و این روزها خشمگین هستن
از مردم ایران،  که چرا کنار آخوندها و سپاه علیه آمریکا نمی‌ایستید؟
تصویری از پست ایشون و یکی
از هایلایت‌های ایشون.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6361" target="_blank">📅 11:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عراقچی در این بخش مصاحبه‌اش درست در خصوص آخرین روزهای منتهی به جنگ ۴۰ روزه صحبت میکنه. جنگ ۹ اسفند شروع شد و عراقچی از مذاکرات ۷ اسفند می‌گوید.
اینکه جمهوری اسلامی در مذاکرات به هیچ وجه کوتاه نیامد و آمریکا را به این یقین رساند که مذاکره نمی‌تواند گره منازعه هسته‌ای با جمهوری اسلامی را باز کند.
عراقچی به صراحت می‌گوید که چگونه جمهوری اسلامی تحت رهبری و افکار خامنه‌ای، جنگ را انتخاب کرد.
(با بی‌حاصل کردن گفتگوها و عدم انعطاف)
وقتی مجری به این نقطه می‌رسد که جمهوری اسلامی می‌توانست در مذاکرات، مانع جنگ شود (که می‌گوید باز ادامه میدادیم چند سال دیگر…) عراقچی می‌گوید : تصمیم گیری دست من و شما نیست.
این برنامه فتنه‌انگیز ۲۰ ساله هسته‌ای که هزینه ۲ هزار میلیارد دلاری بر ایران وارد کرد و حاصلش فقیرتر شدن مردم ایران بود، این سیاست ۴۷ ساله دشمنی با دنیا، این دشمنی کینه‌توزانه‌شان با مردم ایران، این جنگ‌ها را هم به ایران تحمیل  کرد، که عراقچی همین جا هم می‌گوید: مسئله ما زیرساخت و تاسیسات نیست!
«شکست در نابودی تاسیسات نیست!)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6360" target="_blank">📅 10:58 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام فرستاده برای «شیعیان» ایران
میگه اون روستای شیعی لبنانه که کاملا نابود شده،
اون یکی روستای مسیحی لبنانه،
که دست بهش نخورده! چون رفته متمدنانه داشتن.
این هم روستای اسرائیلی (یهودی) است
که با اینکه تحت حملات راکتی حزبالله بوده،
ولی داره زندگی‌اش رو‌ میکنه!
و میگه دست به اقدامات شامپانزه‌ گونه نزنید!
چون - مثل روستای شیعه لبنان - نابود میشید.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6359" target="_blank">📅 10:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6357">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FYSUaXr_w3RGq5pgw4kJzox4wGhAqTZvuonBLStEWod9boR-tTAgMraZnneEt9-SKZpG-Miy5jHbYpsswmsmycFgfsMScP12URoX0BzhRYnYVSE7Hbl-I-WcBUfAoO45bTp2FJo74USLDpTGh7NtV9juyloxN3B885bi2HtOngQGOczSg5U_tgDSUUrawzjqXsyTKKc304o1siz7ubE6adwwjl0AdC4caja3wo7Ut8q9hU5WMX86iLEpWyj0BkMRH1jYulHo7DFIwgILP_aABI2cJc0Qyy6PNz5n3NaFmKNzBZNg3aBmjjwSbPSeWJ8WRAiRFwyg36vxUmwpHc1liA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gBIb5RSE5JCcSgWqhCQ3AsdORPT-oUG5YC_so-DYPfo1UR8LNdMBPx2Pa2xdsmw9VJVxD135NygBR_o-HEFhFj2MwDCfxZF0x2lcmxLxX0P3d-b8VXZdNJyUQugyI5BlNHjaBZRD4Qrl6ThUY3vD65F209hBRXVWhiphdAi-Txf3KrTOtmUBS2J1t8URRFcyMBiuBby4JeD3VxYAZ32OHcRKlnP8J5n10NGZfoLZUuZmo8NJFZ7-prKAoosTvl3_jY73DBoaGbFQA50hLoiZLzoq1PQYMFj4iL7idvy6I-UauKLgWOMvdjYTUWYHUDEwZK_FRmfvjLsUGCUR9MlRaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این متن رو کامل بخونید.
در  بخش سوم می‌نویسه اصل این
بحران ۱۵ روز اخیر از اونجایی
بود که کشتی‌ها از سمت عمان عبور کردن و جمهوری اسلامی حمله کرد به کشتی‌ها
موردی که ۲-۳ روز پیش کامل توضیح دادم.
جنگ رو ج‌ا شروع کرده و دارند زور میگن به عمان
بخش ۵ هم بسیار مهمه، در خصوص کوه کلنگ، ج‌ا در عمق این کوهِ سنگ، غنی سازی میکنه که حتی با یک بمب اتم تاکتیکی هم نمیشه نابودش کرد! و چون خیالش راحت شده از اینکه غنی سازی‌اش متوقف نخواهد شد داره رو تنگه هرمز هم فشار میاره. اگه امریکا بخواد برنامه هسته‌ای ج‌ا رو جمع کنند، باید هزینه زیادی بده (جنگی بسیار بزرگ)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6357" target="_blank">📅 10:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6356">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ثابتی میگه تنگه هرمز رو بگیریم‌ (که بخشی اش متعلق به عمانه) بعد بقیه کشورها از جمله عربستان رو هم مجبور کنیم از همین تنگه عبور کنه و اجبارا به ما پول بده.
(عربستان سواحل دریای سرخ رو هم داره و بدون نیاز به تنگه هرمز می‌تونه نفتش رو صادر کنه، ثابتی میگه:
۱- تنگه رو بگیریم
۲- عربستان رو مجبور کنیم که از اون بنادرش استفاده نکنه، فقط از هرمز استفاده کنه و به ما پول بده)
شهریاری میگه خدا رحم کرد شماها قدرت آمریکا رو ندارید.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6356" target="_blank">📅 00:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6355">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‏وزارت خارجه جمهوری اسلامی اعلام کرد حمله اوکراین به یک شناور ایرانی در دریای خزر در بامداد شنبه، موجب انفجار کشتی و کشته شدن یک نفر و مجروح شدن یک نفر دیگر شد.
‏همچنین این وزارتخانه افزود،  این اقدام اکراین میتواند آتش جنگ را شعله ورتر کند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6355" target="_blank">📅 22:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6354">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">‏ترامپ در گفتگوی تلفنی با شبکه فرانسوی LCI:
‏«اگر از جمهوری اسلامی ۱۰۰ درصد آنچه را که می‌خواهیم دریافت نکنیم، قطعاً بازگشت کامل به درگیری‌های نظامی را مدنظر قرار خواهم داد.»</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6354" target="_blank">📅 22:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6353">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvSSFieyNkQPEAePqBodlYCgqIyl0OiQV9VlFZb_5iEAXvgGQsM-JrP9oNETSVAzr1PJuhCf_c-j_vqxnJu9-uQERNMyAQysuft1MZnejEx8Hb_dCQ8tRlhqTIiGzBZ7I6zVGXRiuVFeDhgBJUmR0gY1EcIRNIPYczLydtcIUr144hHwk8c3-M9TXRu7c9sRvSZWe0vRBKEjrq_kMRlHUBZwJIDSZGXTnFsbzFQGgfIHotpMJ1Q9UJWBvKYVigYDo97dO8vndYmmFXXKohAJ61a68UltHWVgisqtV1lDx9pd6pdmmlU5flJVb8WBp5BCJ8L1kCwB4B88oTBwEztltw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اجابت دعای هر روز مردمه</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6353" target="_blank">📅 16:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6352">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‏فرمانده سابق سپاه:
جمهوری اسلامی و انصارالله (حوثی‌ها)  دیگر وارد چرخه جنگ، آتش‌بس و مذاکره نمی‌شوند.
‏حسین کنعانی‌مقدم، از فرماندهان پیشین سپاه پاسداران، گفت که‌جمهوری اسلامی و انصارالله یمن دیگر وارد چرخه «جنگ، آتش‌بس و مذاکره» نخواهند شد و این الگو، به گفته او، کارایی خود را از دست داده است.
حوثی‌ها دقایقی پیش نیز اعلام کردند که به تاسیسات نفتی عربستان حمله کرده‌اند.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6352" target="_blank">📅 16:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6351">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=JOC_8MkkwHJn-2LbdITzPo22886krLEpnqazLPDiDdQysqRDWWhhGjmlHsrvlUq0GQ-7tZ6iiOD3gzIW6OzvqElez_eaSUN4LyN_bmuO6mm2MUQIetIEEAqKk6V2G9pNfAtsm9YI5n2Fb_N0AxQxjnAwTy5xTOT28OIuSrNe39rozjd3DTSDKfjhIP6nWkbgskeK8eww3KtgG7JYzT8cq-JBzCGzYwFP5rGi0V3RKXuZHqclel3j2dc5LmkQNdFjlmNy_NRgaZ21hWRF-frH8ib_Q-3fjolEpvEj4KkJoFKPY3Xe4j7KQfNV0R7JtKGM9NMVxRC2xt8sw3VKrkcHcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad32a14512.mp4?token=JOC_8MkkwHJn-2LbdITzPo22886krLEpnqazLPDiDdQysqRDWWhhGjmlHsrvlUq0GQ-7tZ6iiOD3gzIW6OzvqElez_eaSUN4LyN_bmuO6mm2MUQIetIEEAqKk6V2G9pNfAtsm9YI5n2Fb_N0AxQxjnAwTy5xTOT28OIuSrNe39rozjd3DTSDKfjhIP6nWkbgskeK8eww3KtgG7JYzT8cq-JBzCGzYwFP5rGi0V3RKXuZHqclel3j2dc5LmkQNdFjlmNy_NRgaZ21hWRF-frH8ib_Q-3fjolEpvEj4KkJoFKPY3Xe4j7KQfNV0R7JtKGM9NMVxRC2xt8sw3VKrkcHcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله موشکی اوکراین به کشتی حامل محموله نظامی روسیه برای جمهوری اسلامی در دریای خزر
زلنسکی با انتشار این ویدئو  در توییتر (ایکس) نوشت که نیروهای این کشور در حملات دوربرد در دریای خزر، شناورهایی را که برای انتقال محموله‌های نظامی مرتبط با جمهوری اسلامی استفاده می‌شدند، همراه با یک ناو جنگی هدف قرار دادند.
«با حملات دوربرد در دریای خزر - از جمله کشتی‌های مورد استفاده در حمل محموله‌های نظامی مربوط به ایران و همچنین یک کشتی جنگی - به نتایج بسیار قوی دست یافتیم.»</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6351" target="_blank">📅 14:42 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6350">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5K-CgCT35sCzjYUiPiBhWeGn-CojiSTvACz2o014-k4OXwKFClOVDpPJKsxjyXT6JYgDHtX03-IV7OUhoR1rbd7TBLV4intl-_ohb50JQISBEO_BHMIy35YFr8LF5ntJ_MxRNlYPBYCYr-HmWK0p4ZSPW3FQTiIE4MzllFB1-mo41eNTAN3zfhimXUb_d0CLOToCU6tIiZyYhBMLl0HJLvwQif3-RgCZy_qtJyYO69f7PRlU45rlf9h5F24fjJDnVH7-xZkOHwE0MsC4dCxr9Cag9y6KVlLnt1CUbwtaxMIlTcRw0qGmmJ9NSPTBJ8fZk0Y0w19gaZ18khZAZPlKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازرگان می‌گفت ما شب می‌شینیم با اعضای ارشد حزب جمهوری اسلامی مذاکره می‌کنیم، در نهایت به یک توافقی در خصوص سیاست خارجه و….. میرسیم فرداش می‌بینم  در «روزنامه جمهوری اسلامی» و صدا و سیما کلی به ما فحش داده که اینها خائن هستن و…..!  بهشون میگیم مگه ما این تصمیم…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6350" target="_blank">📅 11:37 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6349">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSmhiUMenQOWqyYhrMMSaR8AighxJyquyelvAgquwWZyIS3JFuzAZXigR65Qd3Fm0hxx3yWsV5evRcLKqFcAIgb5F2ER-l9QL7uxK3PtrZlPrhCEPuDm3bDQsPcoKGI01dZmc1GaA4kwI14eHRy7mxYKtT4K6gFLAbb0e4KCCY_X1drJ52W5vuIdz-Qy506Rqw8i36TWF4HSXrTLhkuMHHGJcSt2Ska16WlXivI07XY_DKT15IduwkFeQk6r62Tkg4znTassaNc4V8VSlz32WKFUWTjLyiQ5EIpajxgq5gyT4IWgCErWTpL9z3L6hE4N0hLBjq99JbNI7wL9Q0lMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خمینی بعد از انقلاب سریعا بر دو چیز  اعمال کنترل انحصاری کرد!  یکی کلید زندان و در اختیار داشتن تازیانه و دوم: منبر و رسانه!  تا اینطور بتونه به راحتی صدای دیگران رو خفه کنه و روایت خودش از هر جریانی  رو جا بندازه، رقیب رو از حق‌ دفاع از خودش محروم کنه، مردم…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6349" target="_blank">📅 11:23 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6348">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef2tA1bvsFUYh9oysMMeju-cTCC8mPwHIzWiGAiCxH6bZ3soAxXhmqTNRpW0bEd633lsRCE6gX74AFUJHklhLH2PO9XF1rvWocu3voQDZI9fkAE9oZREtpaRJ4EWlBGvkPwnhULJjV5A4eul7G5vytKwoRZlfELrVQiYIY28zX2T8V5V0U52GiBLHCuhBesIOekqO90vhp53QlZwykFNeKDiBNdadWxIKmG8L87ayh69FElkyjXuHFUz_A3f_EJ1RZTLQr143OHG9-gmuX6fhT2-mfH9swBLNs0WavlO73bQu4oPrcSKFMNe0hoihgk5eZSwCnMe3XHQNq34nApd-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو روز پیش صدا و سیما،  بخشی از سخنان پزشکیان رو سانسور کرد!  اونجایی که اشاره کرد که خامنه‌ای در نهایت  طرفدار مذاکره شد و کوتاه اومد!  وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که صدا و سیما مطالبش رو درست پوشش نمیده! و میگه یک گروهی خط می‌دن به سخنرانان و مداحان…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6348" target="_blank">📅 11:21 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6347">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دو روز پیش صدا و سیما،
بخشی از سخنان پزشکیان رو سانسور کرد!
اونجایی که اشاره کرد که خامنه‌ای در نهایت
طرفدار مذاکره شد و کوتاه اومد!
وزیر خارجه‌اش ، عراقچی، اعتراض میکنه که
صدا و سیما مطالبش رو درست پوشش نمیده!
و میگه یک گروهی خط می‌دن به سخنرانان و مداحان
در خیابان تا علیه «تفاهم‌نامه» صحبت کنن
در حالی که به قول عراقچی،
این تفاهم‌نامه، بهترین تفاهم ممکن بود!
[همونهایی که موشک به کشتی‌ها میزنن
همونهایی هستن که این تجمعات رو سازماندهی میکنن،
اینو عراقچی هم می‌دونه،
همون‌هایی هستن که در صدا و سیما هستن!]
قبلش هم صدا و سیما،
بخشی از حرفهای قالیباف که مسئول اصلی مذاکراته و رئیس مجلسه رو سانسور کرد!
(یادآوری : هم قالیباف و هم عراقچی خودشون  از مجموعه ۳ پ هستند! و باهاشون اینطور برخورد میکنن!)
این دعوا از اول انقلاب به وجود اومد!
صدا و سیما شد ملک طلق
و منبر اصلی «ولی فقیه» و شد چاقویی
علیه دولت!
حتی علیه خود دولت خامنه‌ای! وقتی
خامنه‌ای رئیس جمهور بود،
رادیو علیه‌اش یک برنامه پخش کرد و‌
رفت گریه کرد و قهر کرد و…..!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6347" target="_blank">📅 11:18 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6346">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=R88BKWewHZ2UONatM-dDM3lY5cPqAhZYBteGKqi6r-L5FSbVchTMAUwT4oGT91R0hWYtVcDAL-GX5FSlm6GpiIV8EksMBfvPcCmziY3undrkkAyVNIf1KAPvRRR68ZR8cb5-dg41QxOWsWyA4koxNAQ-k25RW-Yo0Sxk3ggmBZNCDLV2OQcNGbQ2_oo7cS7kxqG5WqFEzEeiHh4sRzIXovd1zEKYpzSsrZpkQ-8aIpWlYW8_xtnRORI82qtfENElAlFMHippSIGFqCWmG98N65ImcgBB1ruGHcZoviPREtQgzx0jRQIODknZaHJuIURxI8MaXqDQEBr1PZ2Whpjb7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc31ec63d.mp4?token=R88BKWewHZ2UONatM-dDM3lY5cPqAhZYBteGKqi6r-L5FSbVchTMAUwT4oGT91R0hWYtVcDAL-GX5FSlm6GpiIV8EksMBfvPcCmziY3undrkkAyVNIf1KAPvRRR68ZR8cb5-dg41QxOWsWyA4koxNAQ-k25RW-Yo0Sxk3ggmBZNCDLV2OQcNGbQ2_oo7cS7kxqG5WqFEzEeiHh4sRzIXovd1zEKYpzSsrZpkQ-8aIpWlYW8_xtnRORI82qtfENElAlFMHippSIGFqCWmG98N65ImcgBB1ruGHcZoviPREtQgzx0jRQIODknZaHJuIURxI8MaXqDQEBr1PZ2Whpjb7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری : در برجام ما به تعهدات
عمل کردیم اما اونها عمل نکردند!
عراقچی : ما هم عمل نکردیم که!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6346" target="_blank">📅 11:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6345">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gG2cNTlFailsUpJVRVizPDFxy6gjlLyl-l8CZCb1Q3k8CuA-uJPVE2RLkGbJyH-ytqMyEsNyaFBqbPZ9boH0r4R_lFmrWHhA9SkEeFLRQmUxnChDEhYz0HlK0gp1eebNd_ql6g-qmymFBgIw8NDVlf_lc6dd_OeZHGjaSfmZzgNoZWOmk_PLf9faa9ozEDZye1f8qYNC7kj7tla_jB6XDQQo7pP7DLjxevlBn-OaMTc6xkqWTHxMKmiQPfGQgHRwTkUEbgl4JvQ2MxW7yMEiOQ59Lek1LDgCqmNgop7Arn88NxGWg7qjstyiPpqFDTaFEqgCoRUmerj3djS2Y6anaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ‌ «در دوره من رژیمی که زمانی قدرتمند و هراس‌انگیز بود، رهبرانش کنار گذاشته شد.»</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6345" target="_blank">📅 09:03 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6344">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=bEWCjw2UiIwGnwvLBV6POUH-eHRxe95peG9g9ob84aK70PVh5sSdEhPbABn9sefqvuZvkNKmQfWJP2RHRczEH93HE7YM6yMSCnDVEqWlc6mF8lxK2nRBzg0430XN9-nOX2djf9WgNs8_vvOJeEZNClYe9twGdKR_6IR7famSoBVzPCjed3WvMIur_EUX1v0akCjbCECDAz9P9eWabkNEeRoBK-PQBeDKjNtoNVtx-eYtcESsX4E5XVrHwmEc2Qju9UPzcit3TAO7WUKRuWnwHiSEuBxCFK9D04Mc6WEwKv_uB4IUgi1dlRqVqJeob_1dW1tbGjk_lJ_kzwtxUCpH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2f4e943e0.mp4?token=bEWCjw2UiIwGnwvLBV6POUH-eHRxe95peG9g9ob84aK70PVh5sSdEhPbABn9sefqvuZvkNKmQfWJP2RHRczEH93HE7YM6yMSCnDVEqWlc6mF8lxK2nRBzg0430XN9-nOX2djf9WgNs8_vvOJeEZNClYe9twGdKR_6IR7famSoBVzPCjed3WvMIur_EUX1v0akCjbCECDAz9P9eWabkNEeRoBK-PQBeDKjNtoNVtx-eYtcESsX4E5XVrHwmEc2Qju9UPzcit3TAO7WUKRuWnwHiSEuBxCFK9D04Mc6WEwKv_uB4IUgi1dlRqVqJeob_1dW1tbGjk_lJ_kzwtxUCpH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در سراسر این رجز خوانی
نه اسمی از ایرانه، نه دفاع از میهن!
نه رستم تهمتن!
شعارهاشون اینها بود!
تهاجم و حمله!
تا ظهور مهدی «در راه فتح فلسطین» میخواستن با اسرائیل‌و آمریکا مبارزه کنن و حیفا رو نابود کنن.
نه در راه ایران! نه برای ایران!
بلکه برای فلسطین!
https://x.com/farahmandalipur/status/2080726571627774147?s=46</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6344" target="_blank">📅 22:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6343">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZSm80nZZ4SsD9JEn4ZvGehz0hFjzVBnTZSXTkW-dqZsL-S7Gun-JlsGYLqMY5BlnvkwwMbhiOnOzro_pm7CKJcagenOy5XE7TOREE72q26_yhDjbz7ef9skArBP-cGb3opP8u65BSA48-e1dITr9fPs7MWKw0_9jSDuF8pv8Dc0wbpoxSZOqRUr4y5I_cZDJ1JB17B9js77yP2Y9JNW4FKhHHgYDWyJ56AQXSD57ezsHUjLp6uHLQd3L0ZKhExbq7sc0cqZi-oa6qzENugTObKTTDIaL635rwiWtaqMxeEBr4Vxa07prWR4b1RxRICXFbRCnHDi1Il3vernO73V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حمله نظامی آمریکا به ۵ استان ایران
۴ نفر کشته شدن!
فکر کن جمهوری اسلامی هر صبح
با صدای اذانش، بیش از این تعداد
از مردم ایران اعدام میکنه!
جنگ ۴۷ ساله جمهوری اسلامی علیه مردم!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6343" target="_blank">📅 19:38 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6342">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عراقچی میگه توافق ما بهترین توافق ممکن بود
اما به سخنرانان و مداحان تجمعات خط داده شد تا علیه این توافق شعار بدهند.
همه می‌دونن ریشه جنگ‌ها، تحریم‌ها، تنش‌ها، انزوای ایران و….. همه از خود اینهاست!
قبلا هم همینکه در بیرون به توافقی میرسیدن
موشک آزمایش میکردن و روش به عبری
شعار می‌نوشتن!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6342" target="_blank">📅 19:35 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سپاه خطاب به مردم منطقه : فورا تا شعاع ۵۰۰ متری از محل‌ حضور آمریکایی‌ها فاصله بگیرید.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6341" target="_blank">📅 14:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVGd7k0eOnHKBgcBky8IMN-hm7MKpdf8Kbht1CEkr-6h00l6LBQ_2gNAxxztKqHoGxkbb-uDyCTRZazSEJoBloyMwLLHkI_r5azo6ZTpZB3XE25GbAeXr2mBWuK6fhs_7fAjJ6iVfuZx6G1gcMA-9wTOa5fuMydabdk1RUu35qO4fdoHefdz1W80ZDK_MW-XIj9BkTcAlwRGCEJez66eSMcGlUMP_gsub-ezLxsITO0qml2pHOSpDZTkjkTEu4bSbfqTHNLJHmaXhXULqvkmwSu2ky4utMTnUmk--D58Zoa0Y7O60LmF8-zqirwWX2mjHexMKIM6Ch7Ct7i4NYfJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه دوم روزنامه کوریره دلا سرا - ایتالیا
حمله دیروز گروه تروریستی حوثی
به دو کشتی تجاری عربستانی،
حدود ۱۰۰ میلیون دلار خسارت وارد کرد.
ترامپ : هزینه این خسارات‌ها رو از پول‌های
مسدود شده ایران بر میداریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6340" target="_blank">📅 11:25 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07c232479.mp4?token=P4FIeabHZsvlKhCrwgFGZPfJ7sK9DNifjutf0Eguo5h_VMerEEGXugnviA45-u5JWavG8Jf2WY1SoVzERZ_PgdGLrir-l_7ZlCeE-e21DHKoOe8gCphTHBKyyUupRGsDT4HV45C29yPJxlo7TVpeGtvNL-bHKnDKMIPXXkQjlZEPkuipR-mAdHLb2two298jIeVIc4Q1nPPymiMy7s6Y8JJYhBqA6CTFogVhKWAS_adwvCxw42BQUW0Dq59O2ANSS3BqeN87Jxy8a02W8AHUU3T484mas2YpgY_2EvUDt5GgYxv-kVrlzwshQ0tbgZ_ynceBQxH6uhhnFB1EIf8wJTDVIqmzij6SfV9k364CHe2b60ZBnTqbY8O5a8U65arVP3olVswkvbQzR4A6MoiuXoh80jT5ROXlMNUfd9Tw9sf0Dw4QifA8iMipeeivbxXKXwBqKdodIuDRmcEtziu6vZa2qZTzn7sLzbTbM6DWL_b3CrvdCDdp87hHV0cRhHH7L-t2aU3ZRSPaQy6h02-EFKF46T9camBfsPX8dNwitdfNReKCwhXTE18yLWg28ntGMRd7ggimAjQ31FbLqjczx9sVuop5kwRFOggd65FlX2mWV0O-AKGo4ySphVQ3PYghTSShdFsqOPCxs7KHEuFrSjOHwd8C7tzho4ZbuxwysK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07c232479.mp4?token=P4FIeabHZsvlKhCrwgFGZPfJ7sK9DNifjutf0Eguo5h_VMerEEGXugnviA45-u5JWavG8Jf2WY1SoVzERZ_PgdGLrir-l_7ZlCeE-e21DHKoOe8gCphTHBKyyUupRGsDT4HV45C29yPJxlo7TVpeGtvNL-bHKnDKMIPXXkQjlZEPkuipR-mAdHLb2two298jIeVIc4Q1nPPymiMy7s6Y8JJYhBqA6CTFogVhKWAS_adwvCxw42BQUW0Dq59O2ANSS3BqeN87Jxy8a02W8AHUU3T484mas2YpgY_2EvUDt5GgYxv-kVrlzwshQ0tbgZ_ynceBQxH6uhhnFB1EIf8wJTDVIqmzij6SfV9k364CHe2b60ZBnTqbY8O5a8U65arVP3olVswkvbQzR4A6MoiuXoh80jT5ROXlMNUfd9Tw9sf0Dw4QifA8iMipeeivbxXKXwBqKdodIuDRmcEtziu6vZa2qZTzn7sLzbTbM6DWL_b3CrvdCDdp87hHV0cRhHH7L-t2aU3ZRSPaQy6h02-EFKF46T9camBfsPX8dNwitdfNReKCwhXTE18yLWg28ntGMRd7ggimAjQ31FbLqjczx9sVuop5kwRFOggd65FlX2mWV0O-AKGo4ySphVQ3PYghTSShdFsqOPCxs7KHEuFrSjOHwd8C7tzho4ZbuxwysK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت وزیر نفت دولت رئیسی از تماس موساد با او و انجام حملاتی در ایران
🔺
جواد اوجی وزیر نفت دولت رئیسی : ما ۱۰ خط لوله بزرگ و سراسری گاز تو کشور داریم، تو یکی از شبای بهمن سال ۱۴۰۲ ساعت ۱ شب موساد با من تماس گرفت گفتن امشب می‌خوایم آتیش بازی کنیم‌ باهم،از من پرسید ۳+۵ چند میشه؟ گفتم ۸، بلافاصله گفت همین الان خط هشتم سراسری گاز رو زدیم، ۵ دقیقه بعد دوستان مسولین بهم زنگ زدن گفتن خط ۸ گاز کشورو زدن،تا داشتم لباس میپوشیدم، موساد دوباره بهم زنگ زد و از من پرسید ۴+۵ چند میشه؟ گفتم ۹، گفت خط نهم سراسری گاز رو هم منفجر کردیم،چند دقیقه بعد مسولین مربوطه بهم زنگ زدن این خبرو هم تایید کردن،من تا رسیدم سه تا خط اصلی گاز مارو زدن.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6339" target="_blank">📅 08:24 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=azLQ5jtklW980M8etOXqiUXz6MdAphgH-dQjW9brCG2v6wyW3-vCJmQqEfDqgblPpilv_NQa40rWtLoS5nTWlKYdMgqPhsOieI-gFgZRtBNrG9jLpMMFBPSOqkdSS9QRXoc-wRBm_BNxwydzgQZlryJ367sxbMLmM21ebOWgLxHjtckdgDy43KIhvLzBrwwwUFD0zp-0rBILKrtl14h7v4UVdKKWan0Rx3lktlfMjQFk5i2F98NI2F-2TfzWkuuHYLvXCpmt1v3jVH6mgy4HOEM-TgQcVwI-JE2QSlQRCwXZMbiwXV8pu6b8kUJ-3VnzHO6i9yX9I15je_uTiC4iFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4193f544e.mp4?token=azLQ5jtklW980M8etOXqiUXz6MdAphgH-dQjW9brCG2v6wyW3-vCJmQqEfDqgblPpilv_NQa40rWtLoS5nTWlKYdMgqPhsOieI-gFgZRtBNrG9jLpMMFBPSOqkdSS9QRXoc-wRBm_BNxwydzgQZlryJ367sxbMLmM21ebOWgLxHjtckdgDy43KIhvLzBrwwwUFD0zp-0rBILKrtl14h7v4UVdKKWan0Rx3lktlfMjQFk5i2F98NI2F-2TfzWkuuHYLvXCpmt1v3jVH6mgy4HOEM-TgQcVwI-JE2QSlQRCwXZMbiwXV8pu6b8kUJ-3VnzHO6i9yX9I15je_uTiC4iFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب - انفجارهای پی در پی در بندرعباس</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6338" target="_blank">📅 08:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wB1QeF4qZ3AbAIF50rU1J-hgAFhvG737P7c7Ereb11XUlRNvzLKGgh9eHhZSjgoIJ7L43Y5B2iL-Pn0sSnH7cyUipSzEYRJ0Id40Mjm4OuEKLgp5aoBi2NVB2pL4o7sqclgakDEqV6QAQM-sADn70wsMyI1KgjJZH2HcWHcspavYpGRbaI78Nzna7TPlzbQ5kuWmB5IaAEpQjhDE7m_qSlYr03AEooyhDs23Wll7SZ2rYDIsZDdf6uE80F7yHXDnxGtBGzUzT72Tv0PCrzJVzR9TS30386ezgdYfB3fY39xjfT4SQZR5vR4v1x-E358jL4sq7ZEy8Plzw4RmOpfAKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید تازه ترامپ‌: از پولهای بلوکه شده ایران، خسارت کشتی‌های آسیب دیده توسط جمهوری اسلامی را پرداخت میکنیم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6337" target="_blank">📅 08:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6334">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=crZa5J080QWv23CaQfuswnfIjN7BJqCMJICzI2yIE1i0MT5AKzm37l5aMXX3WMzqPNLUOBs9wHTgh5_CHO9eIx3QOof1zCQReiTIY4Zhg5IaJJMBY3iaxQGRiA6jK62aU6MXLxcU2kFUOzFZLB87PaxiH4I0W7LazwvPeCDeQimZ7q-ZQO9dcd4ABa5XVo3HtNsqrtfNpHDxVeTyqO8P3Bx52sWFFfhpWsgMq6xi9l0dcmhtg2-WqHBx8G_TOg2dYpsiRJEQpzdi7KsoDeyu-sGgWnvxHJDeBTJ89dkY2Qh0h4uroQfORgdLlnRyVBZ5kTUL22cYveIHBMitrTUGEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d84604bc5.mp4?token=crZa5J080QWv23CaQfuswnfIjN7BJqCMJICzI2yIE1i0MT5AKzm37l5aMXX3WMzqPNLUOBs9wHTgh5_CHO9eIx3QOof1zCQReiTIY4Zhg5IaJJMBY3iaxQGRiA6jK62aU6MXLxcU2kFUOzFZLB87PaxiH4I0W7LazwvPeCDeQimZ7q-ZQO9dcd4ABa5XVo3HtNsqrtfNpHDxVeTyqO8P3Bx52sWFFfhpWsgMq6xi9l0dcmhtg2-WqHBx8G_TOg2dYpsiRJEQpzdi7KsoDeyu-sGgWnvxHJDeBTJ89dkY2Qh0h4uroQfORgdLlnRyVBZ5kTUL22cYveIHBMitrTUGEjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نصب ماکت آبگرمکن در مرکز تهران</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6334" target="_blank">📅 22:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6333">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
ترامپ به کانال ۱۲ اسرائیل: در حال بررسی یک حمله گسترده به جمهوری اسلامی هستم؛ حمله‌ای بزرگ‌تر از هر اقدامی که تاکنون انجام شده است. به تصمیم‌گیری درباره آن نزدیک هستم.
او در خصوص احتمال مشارکت اسرائیل هم گفت اگر از آنها بخواهیم ظرف ۲ دقیقه آماده می‌شوند، اما برای آغاز عملیات جدید به هیچ کس نیازی نداریم!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6333" target="_blank">📅 21:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6332">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏هشدار سپاه: هر پایگاهی در بریتانیا که برای انجام حملات علیه ایران مورد استفاده قرار گیرد، یک هدف مشروع خواهد بود.
‏واکنش سخنگوی دولت بریتانیا به هشدار : نیروهای مسلح ما آماده‌اند تا از بریتانیا در برابر هرگونه حمله محافظت کنند.
بریتانیا به‌صورت شبانه‌روزی و در هماهنگی نزدیک با متحدان خود در ناتو، آماده دفاع از خود است.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6332" target="_blank">📅 21:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldQQNbbNkb7yOXxR6siW-tqUFM2BzQM_uMvZMFsH4-l0rWWTK65aEldakfUVUJ9ovlDcmnDFgt1lN43xyhmTSozVw_AlK0Rr6867GQQ6-iRBYK-NzbzLxImlDtUexMNEAoclH4t26pivywiykw6Bqr4fuAnNnHaBlblWsHiHkX57ZkCS7Lo2b0e7qfBnlIMY-fJ_Aqx3qz_bS__-fBlKgAUi8cCsYE2CIdMQCZi3od3T_dVmFYXIwQtYo3tlhMFBBPAa6-AJ1u9hJ9NH0cjzCwErZJg97c-MJrcbv3i-wvwR2Z4t38VBwiye_CpuYfhWR1TA00UiNjhAT0ZhWQvRZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضرغامی : فعلا حرفی از مذاکره نزنید!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6331" target="_blank">📅 21:22 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AeJZqRhGRzr5aZZDFAC3HTUkAhUr27zF3R_f12kkwL0Q7F2ww5qiQ-dEIfQ3IJ8FZQXK0wYZyqmvmQpS8yRIKP2JMcI_I3ArmPY7mVffwo7hHTEoA10mDnHeaZppPVzO1140TaMyOd5R09vy5vNihUGCDm20A7wKlzVq7hy34IpTYxZPFftUO6oaIpdw6yuwWLCTB5hnmS2WqliPeySMAxFjUozAsiwE354JHyLGllfco7Ej_zdznXBRQcDghSdquEsVQpi3YT4hSlmaLVeq537rYpr_vyPopmB3HWj5IqDxWhxkBaQ2XSvCXN7Y-gUPGTC3i0jWtpR0xv414MGC-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو حقیقت محض
۱- تروریست‌های حوثی به تحریک جمهوری اسلامی وارد این جنگ شدند و به کشتی‌های عربستانی حمله کردند،
پس مسئولش جمهوری اسلامی است.
۲- حوثی‌ها ارزشی برای جنگیدن ندارن!
اینه که ترامپ مستقیم میگه فاکتور هزینه
حملات حوثی‌ها رو شما باید بدید!
و این یعنی بازهم ایران باید هزینه سیاست‌های جمهوری اسلامی و نیروهای تحت حمایتش رو پرداخت کنه.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6330" target="_blank">📅 18:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcGYF1euYihXno6cpzZgynL9I83RaKPZiZgki2hjVaygHYFTb19mWywgEBArG73j2CUoNwcXSwjGQbj40I1_hCVLoGnRsuc6iEmNaVZ3tJPDKIQq1Ca8t15LosuRgAFgEdkRAbZuDlvbgu2HDCU9sORc3-UTnY2w312qWvWrB2J6EavX9BYobqc0XHUYBDbmKGc-6hFUXiDJoJjjUmFy-ILST_t4a71SUPPzc5lLV_f9gQiSEzjbBJC2sPjq1SpvDcQd90aShrnc90PjL6YzgMhGKyJg4ptWpQhb_K0qGP9r1EH2eg2lN-4x7X4_Ugg3dCTaG1ZIlrlxKUc_aKoV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاآنی، فرمانده سپاه قدس، با ارسال پیام تبریکی به «خلیل الحلیه» نوشت: «آنان با انتخاب شخصیتی که نماد مقاومت و شهادت است، بار دیگر اثبات کردند که همچنان بر استمرار مسیر مقاومت اسلامی تأکید دارند. مقاومت اسلامی امروز قوی‌تر از همیشه، مسیر عزت‌مندانه خود را ادامه…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6329" target="_blank">📅 18:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2JV_mvOd6NVjvsR0INXWVoVQehSW5c_Sq54h6uR9Fl6T3swD_KC-Dwj_9wW5BbOoYXSEd50hfCDhx5HLx_hpfz2HM76wlmtZXj22qRJrBdmy9jw_n6Uqb2bT9J0OVl7VPp31Fbclc8ubAawv_4FABTFT3SrJy2akPKbkYegxPOwhoBDB1kb3uwCgXr9Z09Lkc14CDnsaoYhTuXg4nteTyryL9iUIf0ebrKlPAJUsPoBEniv7UP_r2jZjgRU3jinAE-6kfAhDeOfvxx6q6EQYuRAP_QobusNGAdMBmTxzI4GmnlMit_4DpfbKJBQNDVQ10YuUCJMNZ6gvdz00HQw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6328" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dr0mez_9h7Qwxxn7R8JSVELfXN_KpV0VAoVqyFbcpk9NbrztUqwakrNAN4myz7dVa2eTUCcsVbhwGgyYhC1ZjwTRLUEvdI2OxKUGOgNjtf3pv-W_laHnymkw6D5by7gZ55Ckof2EqPuVjis4DBDbR1JFXjVsIbbKNhUUalde0sRBBRPgyveHef_fQUnq-UcGNVlhRvM90EtlrtIDiBAWv6cQvnJw9495stooDgrdiK60mFoSvCBZrdHAmuDs50volLDs6gWfl1aSbH51RXWvZ06O5ihOLWpXVGJkKWhuTHQEsz0h2GulC-9MFxmLtl5hpZ8rgKLY7h3Oko3ZmODaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6327" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=nBvbrQutBDLRacV1DuWBDgZBZzbXjFAcY_iQ9pnQHfug4J3RiL3nFhCozJm3gl4Cb1nERActlAcZIAWg-d7DSArXnyriNUuOef7bGB-no_vhieq51j9aIlViBrHXry0uy5ss2Bpe_uCRk6otZiVkZBLJQUoiUYZ87Gmu-GQnssujkNUORLyhVwbyQFwqa4Lju1P5LCXgLc0b1iYi4_Ljb6PZ6l7P4R3Y-ABlnndxIEdrEIvMn-0aStxTSe57TUGUrgktwWAvevU48Ti1Ql5dCzbAWr6bg7ZNorug8ViFqvIGOLszubkLYlIDZAXDm9DpU0qnfmDeZsNGQBcxD6yTaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12a0e4dfce.mp4?token=nBvbrQutBDLRacV1DuWBDgZBZzbXjFAcY_iQ9pnQHfug4J3RiL3nFhCozJm3gl4Cb1nERActlAcZIAWg-d7DSArXnyriNUuOef7bGB-no_vhieq51j9aIlViBrHXry0uy5ss2Bpe_uCRk6otZiVkZBLJQUoiUYZ87Gmu-GQnssujkNUORLyhVwbyQFwqa4Lju1P5LCXgLc0b1iYi4_Ljb6PZ6l7P4R3Y-ABlnndxIEdrEIvMn-0aStxTSe57TUGUrgktwWAvevU48Ti1Ql5dCzbAWr6bg7ZNorug8ViFqvIGOLszubkLYlIDZAXDm9DpU0qnfmDeZsNGQBcxD6yTaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدال لفظی دو نماینده مجلس
بر سر تنگه هرمز
(پشت پرده دعوا : شهریاری اینجا داره میگه
که تنگه مال ما نبوده  که بگیم میخوایم بدیم بره،
و میگه تحت یکسری قوانین
بین‌المللی است و زمان جنگ می‌تونیم ببندیم برای فشار آوردن و….. ولی مال ما نبوده)</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6326" target="_blank">📅 13:36 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNdIwjRiznCd5SfnKxq9JQn704m6CL2WB48K2DS1YDCCSQQbraVO0TVQB2lGe8oCiJCYfbLBpAJ8syybt4Wz_D8neWS9MpGE5mhMbjXdDCu1XQXmgsmS1eJSjnFcEz9qsJz3lINcCuRu_u7jwbUl4vjv3DKjYXVF-oP-miE4tY-hhDlvIcJ1gMkQ02HfCbHdjWRT0Aa7RkuZT8-h-L4Xo_wfWYqoZwUTy0CQIXGLMltfVAB2R8zkxmycwCtga98m1qD_K7kteRuRwL6laawm4A3ehYfpxxRLLrk9fBxqU1M9CtxONkvIfWS89JBblhRUmxTDe537ZZZmvyIrDVDSDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6325" target="_blank">📅 08:58 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iALZnsR0ybIagoj0A3SuBARJfLnIUACyNbPo3Uz6lb-6QeqM8OfKAFza65kI0VaIFLLvXfKlDLebdSt-dg-j3rKhxaUX-Dvc8ILdehJLmQp5_XkNqt7jBfTomxy4YpISSPRjpK4Vxf8kEfJym-sF6QrhISuP9eN7K1qwIYVn6kzXxd32lyavLLqzTZyMhYY15v7g37aZrHIMkb7OwEqOhyugJJ1gbs0figHcgvieTjdYlKfegLkdYvJVdeRHdSZFtLUF1OhcZl_Va5MBUsWDK1mMR846X5JMDHm6J2a_yjIM8wQuILiqswUqHNpXoJk_q-Q1ZrTzDBKLrBPWxKXbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در یک تحول تازه در حملات‌ ۱۲ روز اخیر
و نشانه اینکه حملات وارد فاز تازه‌ای شده.
«بی‌ ۱» برای حملات بسیار سنگین و عمیق
استفاده میشه.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6324" target="_blank">📅 08:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ارتش: مراکز و یگان‌های آمریکا در پایگاه‌های الدوحه، علی السالم و عریفجان کویت را هدف قرار دادیم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6323" target="_blank">📅 08:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جنایتی نبوده که جمهوری اسلامی
در حق مردم ایران انجام نداده باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6322" target="_blank">📅 07:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Scl0ZieNrBfOuNknp_5xvd79yvW7Jm5ZgEyrFu8vdvQAmo6gYkRvoA19ze0e9apVsNeoD1Xp-FCQchRu5r4i-xXyrgYwx7t0q0A0XsnJMOmVHIERBHiM8C2TsDghaxHtK07ahxnrCLofcq8l2bu8ULozBPqJJIOoRL740nznSYktUoc2IhiQaqweWcFq2Jd0Z9ZV4JvvwdAz-hBznuo2oHpCFdxNkECEx4hn7OgXXgnp_UJJo2vao31zQFVqq9x9Rc0HcQsoe4QITaztelBl25bbTpJZ2iSzbRBXlI7XSKuEpzNlUOsyjaRNhXBMJielgBiTLvTdADLTHgYv62_IoDd7dlGNK3KpNoctK0ICmoIgEvxgyXxTBag2MCezbFNJbM4VE7gj02-JhFBbLM0iGNcYQBgH33TxnZ1K8Fzsp_vOuOmlO56be1IByFIFD7p74EXz179v_6ejUVAvB8n5X_iZgdkVEGLaakDTMz2NwpOPpIcIj4_ew3QrZktHt9RUl5AaeuMA76i6PSsXbz-KqlbNLk7klxUqhAf_5acNG4Ac4CTrM8tUO7NXdGAKQy_l-_iywxfpCdYa6F3qsemz_5TSusWilBZ0c97cVeP4GGpVWfTxN1KykUZRGmtUXG5lPVcT4WKAij52YEd7mwSoRgoG4-H7KTHEYVnVqs54Cec" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ac20eb0b.mp4?token=Scl0ZieNrBfOuNknp_5xvd79yvW7Jm5ZgEyrFu8vdvQAmo6gYkRvoA19ze0e9apVsNeoD1Xp-FCQchRu5r4i-xXyrgYwx7t0q0A0XsnJMOmVHIERBHiM8C2TsDghaxHtK07ahxnrCLofcq8l2bu8ULozBPqJJIOoRL740nznSYktUoc2IhiQaqweWcFq2Jd0Z9ZV4JvvwdAz-hBznuo2oHpCFdxNkECEx4hn7OgXXgnp_UJJo2vao31zQFVqq9x9Rc0HcQsoe4QITaztelBl25bbTpJZ2iSzbRBXlI7XSKuEpzNlUOsyjaRNhXBMJielgBiTLvTdADLTHgYv62_IoDd7dlGNK3KpNoctK0ICmoIgEvxgyXxTBag2MCezbFNJbM4VE7gj02-JhFBbLM0iGNcYQBgH33TxnZ1K8Fzsp_vOuOmlO56be1IByFIFD7p74EXz179v_6ejUVAvB8n5X_iZgdkVEGLaakDTMz2NwpOPpIcIj4_ew3QrZktHt9RUl5AaeuMA76i6PSsXbz-KqlbNLk7klxUqhAf_5acNG4Ac4CTrM8tUO7NXdGAKQy_l-_iywxfpCdYa6F3qsemz_5TSusWilBZ0c97cVeP4GGpVWfTxN1KykUZRGmtUXG5lPVcT4WKAij52YEd7mwSoRgoG4-H7KTHEYVnVqs54Cec" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">- رئیس جمهور سلام میرسونه و تشکر میکنه
- باشه</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6321" target="_blank">📅 07:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
در جریان حمله آمریکا به مرز شلمچه ۲ نفر کشته و ۱۱ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6320" target="_blank">📅 06:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">مارکو روبیو وزیر خارجه آمریکا : جمهوری  اسلامی تفاهم نامه را نقض کرده و لذا دیگر  معتبر نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6319" target="_blank">📅 06:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65da400742.mp4?token=LqQmPQwh432HJ7LnEQ26qtFjea4cHkAyalW3qE_7zvuOWbx5cD752e_8IylSyZe5EW-K_8VLjHhSSgkctTtuy2lRCbFUMo-1Y7kU_VqQ8HBfklcyNojTLa4AQ6enrrDe_3famCsM6i1So8sW8MLatnDj_BzcuMsZmquLaDDDbKHmVKukFXHLWvdZdvkrkqAayJz6YPepcHsRTnOcCNJC-fRG4o6HwsIRRpvbDliuTCUEcfueZaOFYiOYyL321C-5GL91ni6GjU-E-gfNpeFRSz4XkAFCJ5MyLu0LLe9l59SaBpksLQW1sFyxPI_uBH9W9kGPYnTK6NG493UscYNUuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65da400742.mp4?token=LqQmPQwh432HJ7LnEQ26qtFjea4cHkAyalW3qE_7zvuOWbx5cD752e_8IylSyZe5EW-K_8VLjHhSSgkctTtuy2lRCbFUMo-1Y7kU_VqQ8HBfklcyNojTLa4AQ6enrrDe_3famCsM6i1So8sW8MLatnDj_BzcuMsZmquLaDDDbKHmVKukFXHLWvdZdvkrkqAayJz6YPepcHsRTnOcCNJC-fRG4o6HwsIRRpvbDliuTCUEcfueZaOFYiOYyL321C-5GL91ni6GjU-E-gfNpeFRSz4XkAFCJ5MyLu0LLe9l59SaBpksLQW1sFyxPI_uBH9W9kGPYnTK6NG493UscYNUuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون بابایی که با نخوت …</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6318" target="_blank">📅 22:41 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiyA3h5lu5_if_EG-xbFblhXDLH2AafXZkyq_D4m6rSSTzTpe95mhPWHxBD-hLAQO4qJiPInlhL9PZeD47p13KAjLYza5dlstu0oF7yxvsPFlABu43igmw8zmcSKzti8461HJhV5HONP6UOi2DNt_F9Q22iR9HIV-kWKCWOB0V7fmZg8e6KfZ_Tm9aM2aYRmBb6-2o-eutZHhZjO7dRDplgScR3o45-KPLr4d-POIgSwIjK3bYrF03tXFdH7uWmFzR-a7tK1_S7mVWma4ujute0F-npGzJmrHH5whEL2UhH8FtERlo2Q4Q7PmLdpchHn-piaptnfn8xtDKopuftUvkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d716a2e5bd.mp4?token=RY8iORhWeianzhFDk1EeJxrAeIpPD09KiR3AT5-U9YZRzrGqmIMVMK17J84sqYwYp3Jts5i0Xq3p9-LO5aAI-IR-m9wKqJOVUNJSJX8kY2Y7DaU7RQfyywauAtDHMd_wY5X-tCdiJcIH9xB0vZlzvfDFSA9ivS-9r7QfTtjMJ7RY1BUajvCbhxsiU8QLkNKUuN-aZVnE__B7ohY3ymyQ661m15nUBUjWUMlDST4AAXAldiXRIuvFkHBDLiUNASD7jBqr5b_WcKD7wjLYtJ1oGOJBQclTbP5Y3UJ4VuWiBj88JmBKVTqaXZ_n7qHBDkMl-f4oZb-i6wRkRTy1fS2KCiyA3h5lu5_if_EG-xbFblhXDLH2AafXZkyq_D4m6rSSTzTpe95mhPWHxBD-hLAQO4qJiPInlhL9PZeD47p13KAjLYza5dlstu0oF7yxvsPFlABu43igmw8zmcSKzti8461HJhV5HONP6UOi2DNt_F9Q22iR9HIV-kWKCWOB0V7fmZg8e6KfZ_Tm9aM2aYRmBb6-2o-eutZHhZjO7dRDplgScR3o45-KPLr4d-POIgSwIjK3bYrF03tXFdH7uWmFzR-a7tK1_S7mVWma4ujute0F-npGzJmrHH5whEL2UhH8FtERlo2Q4Q7PmLdpchHn-piaptnfn8xtDKopuftUvkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن روحانی ۱۳۹۷
تا آخر هم افتخار میکنیم به نفوذ
در عراق و سوریه و لبنان و…..</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6317" target="_blank">📅 22:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTyEQ-k0FoKUonYBBY6rFDLd_QdpfdndLnAE9Pz7LedPhFltAbqHzAh_B9CuAksloNZlp6mNWlFx3b8l-W1JxK5SnQ7S40WxnnF9Ea_gR2swZfwRX1qQZm1JtlbNgG2VMaXUzaye6tRAevcemlbknmzSIu_FCpsjedLbsDs2ZgJahZ3pzjkdfQpBHlK35DCOSUb_M0qEyqDXNbUxUqUisSwsIYfAbdoJxXbyklr18ynU3sXSDh1KUeAq0TFLlpXt2k-lEkyrbfajreIuz84r2wo024XSGv_oGzai1L6w4TQbcUlPRwd3Dg8_FbFT7X-K1oj1SO3746aG01epszquiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏سخنگوی سپاه خطاب به شرکت‌های کشتیرانی‌:
مسیر مین‌گذاری‌شدۀ جنوب تنگۀ هرمز  [ آب‌های عمان] مسیر نابودی سرمایه ی شماست!
قرارگاه خاتم هم دقایقی پیش هشدار داده بود که فقط از آب‌های تعیین شده (بخش ایران) باید تردد کنند.
جمهوری اسلامی رسما آب‌های سرزمینی عمان رو هم ناامن کرده.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6316" target="_blank">📅 22:22 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
قرارگاه خاتم :
تنگه هرمز همچنان بسته است و اگر قرار هم باشد شناوری از آن تنگه عبور کند صرفا باید از مسیر تعیین شده [از سمت آب های سرزمینی ایران و نه عمان] و برابر ترتیبات اعلام شده قبلی تردد نماید.
‏
🔺
در صورت عملی شدن تهدیدهای آمریکا، نیروهای مسلح جمهوری اسلامی ایران اجازه صادرات یک قطره نفت را هم نخواهند داد و زیر ساخت های نفت، گاز، برق و اقتصادی منطقه مورد هدف قرار خواهند گرفت.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6315" target="_blank">📅 22:16 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7exleTxrVEYGIi8S_XAb5fJ2Y4o_fIZQyaQsRVNqX0k8CgNDrWZo2bE-VFA9qylt8SAL_13VfidivREAwt0yOUWHT1a0ofal9EdQoZEbSRw2FnhpoJEHFM6onWUd98FsNHlyLjOv580ZNcXrvQYp2iMw8tAl6WLbY3HXUieEwBYnUPgVn2YB_266Dy-HMWiWgtAiWW60ZTSJxW8715Q90z81A0CF_tyP0ZAtqxZL1T7xHNxTjyjw2XXxlNzDvY9ls2JvjfTeGPORyW8AA9Xv2dcWIrtYIgP_4HHpTqyQ7DMeIfWvIs1Ooy4c8zcJhDf7to4qq297FwNH1fjQE5OyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6314" target="_blank">📅 18:06 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2dgDCdbfEP0QWZWkkD7qrM_QRBFi9JmMIjgS91_SqJnSIQ6JkolmeRtdADcVE33HnQuuAihE0gpXo5vTy4vD3xrV2SCOUWWumW_LyotqNGrcrjkd2WXXr_kEuQvk4ZfKJT0lXZ49VazyQx8txURA04tM3cU2ppfKdOjaqB_575Y_2-tSMRbRwHCtCmRqHqHQVN2EeRFDLJpj1ZKQfLlm6NcS71RsTMSM8aLRhRyBUDzf5P0k9yaFrs3_GAo7Da5MuOZsbVrb97oh4bk_EXr0GkFyehE8YW1-TxHiHqMSJ1Bn8Z6RTmuQj0d8yILSe8Dcs_9C6PrACk6MjTVfZAYuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تهدید ترامپ: کشتی بزنید نیروگاه میزنم.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6313" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
شب گذشته صدای انفجار و پدافند هوایی در ۱۹ نقطه کشور
تهران،  بهبهان، امیدیه،  ماهشهر، سیریک، بندرعباس، بوشهر، چابهار، کنارک، تبریز ، بانه، کبودرآهنگ،  همدان، خرمدره، ابهر، زنجان، دینارکوه،  چوار، آبدانان و انارک.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6312" target="_blank">📅 08:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6311">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=T2hvx4r_F5ed3riEUw1KEruOE8G4Me_YU3XrzQa4noITLckaxTQCN5x344Oc6xG4rheGM_ElSwexATG_Ry8SsJijSa4Pxjs6e3S7ekwsNTlzu16kuHuHHh0MSkWnajLfcKE6U9FEVBY8VMc_6YiYMoz9Undcr04KOfqHeCczUT6EQb6BLc8ARQvqFdykfEfJpe4wmfOjjEQCW87Zmwaq19IsKSWxtr6bXlne6FOV5Q_ED6kPvMySNBNQ5PL2Ew2QdY5xHELTb5keu7gED_r9oATc0BZPe6zXi4b80mJde2-8nf-3eBy6hOKRqpqp45nlJxwEjHe4qbAMdyGMu4YJhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9577aecbb9.mp4?token=T2hvx4r_F5ed3riEUw1KEruOE8G4Me_YU3XrzQa4noITLckaxTQCN5x344Oc6xG4rheGM_ElSwexATG_Ry8SsJijSa4Pxjs6e3S7ekwsNTlzu16kuHuHHh0MSkWnajLfcKE6U9FEVBY8VMc_6YiYMoz9Undcr04KOfqHeCczUT6EQb6BLc8ARQvqFdykfEfJpe4wmfOjjEQCW87Zmwaq19IsKSWxtr6bXlne6FOV5Q_ED6kPvMySNBNQ5PL2Ew2QdY5xHELTb5keu7gED_r9oATc0BZPe6zXi4b80mJde2-8nf-3eBy6hOKRqpqp45nlJxwEjHe4qbAMdyGMu4YJhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هگزت وزیر جنگ آمریکا از ضرورت
برخورد با جمهوری اسلامی میگه
ونس، وزیر خارجه با ناراحتی به او نگاه میکنه.
(ونس طرفدار گفتگو است)</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6311" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6310">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhOTePQ3zW08QfBVtEqitWicu1SBBNvowRSjlzvxZPyzW_sLOwAGUXT1PdOGZKCqjYuoGqL5fYQTGJ8kqJFydEhUTR7xp9iPEHsa7g7ZgwYlqeZ5ndj3twpYzVnqDxU-2wxqrF1dyhu_HgHnn0-UZI7y2PFQCwiEO0_y26dFXJNVv6-HWEFEPHbjf3epWhk9sL6dYbL89g8oe6EY9H6fTJFsz4aXdjuLseXa6Rqj9psL92lqLZ4zxzIxdoRxXYQiLGFo5F8bK1PAvp8x7yDbZKndcEXdlRA974jitm1ovIf1RUfNFW-EaJ-CAqs7tPmsozPFIk0KYQkKhR2_23eK5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اندی برنهام نخست وزیر تازه بریتانیا که از دیروز در این کشور قدرت گرفت، با در اختیار گذاشتن پایگاه‌های بریتانیا به آمریکا برای حمله به جمهوری اسلامی موافقت کرد.
پایگاه‌های «دیه‌گو گارسیا » و «قبرس» از مهم‌ترین پایگاه‌های بریتانیا و مشرف به ایران است.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6310" target="_blank">📅 00:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mW_IwHFbp0O_Vf9RTx8WMPuArlokcNEyNZdOTysNvm_Qw-MAjpbxMRqGh0e4xoB6hOO0hU6uVs_wDCXIFW9EKGjlQIlJdFh0s7CAwd_kb06TIwU7IUnqm5ncajvLHy7OFNJNQLGFuXpeSdbflisRcDkqELU3cvwWdPlh9rTuXkazHQHMgqNNJEr2aSOEQN-4ly0BBlBZ0NOrY_Mrz1Be0MYJECU6zEeEaz63VueDzHA5jsD-cmdnZYkSqQtqfvvFOrw25AwqaybTmQLYo-o0y_7omIuXJdRiJvRFbmDV7LDShSg5_AZJsHP-u1ZJmQlnlGchU43rOGgMoH7IzcLXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8nJlrzrc7pJFK7vBoEV9MHvroeWmFsUf1UXZXNyOmypvFF_W1xnITnR3fCbGQ2QebQCXpGpbVY4W76d_OcLRyI81fu1a-hBz5bwTQVD6-iWE9_pmzklWkhHvEwMymrBO-aCsqReVMpxsHeahA2DBKUFl0WDF21pv9wgnh1tBm2E_-xd2Olmk_ZBrVkh0a__omGpVgl3Z6cwbHO-pPPic8f0SZ_KFwruRd5zBppTb0MzNjkXT71KHqePatzP-OR0YTT6HfcCSZlFu37ciXRzQXznn_7a5keGUvEMDxA6fA5Np-Lbi0tWauO0lgi-sxc5k6LSUp3rcY2aIHsazj3qyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسن روحانی رفته خونه لاریجانی تسلیت
چهره زنان رو!
بعد همین ها میگن اگه ما نبودیم داعش می‌اومد توی ایران
داعش ۴۷ ساله که در ایران حکومت میکنه.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6308" target="_blank">📅 23:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
گزارش کانال ۱۴ اسرائیل :
جمهوری اسلامی به سفارت اسرائیل در بحرین حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6307" target="_blank">📅 22:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdBV8vlH_dmguIVySyGoB9tbxFkkxzEB_-WJvb3_nh5LkVDV66_5TUzlOXPAf7aCAeGyZ6tUGWEndzSp_tUkZij3gYmdOTf3cU_qvfacLvZrCYFquEw_QtyiohRBbUKKT0M33il3_jIECFWHGqbmAx1H6dMjcgTMwK-tzVuvs22gK5pSUo4klp0Awbtm7JW10ui54iO9NRx-9kUTd7VZXLPQ5T1oI_ZGZO5-UxdXY_BnyS6wcKT6uDFnULIN1A2K31sgdG0cMga2yNGXWYfc5LCX5_3ApR1uG6Au9__SVAReq1K-whnA-tVKaD6mQHcQXnzOPQpc9NR-pTRl-CbT3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موقعیت کوه کلنگ، در نزدیک تاسیسات هسته‌ای نظنز، گفته می‌شود تونل‌های بسیار گسترده و وسیعی از چند سال پیش زیر لایه‌ای ۱۴۰ متری
از سنگهای سخت ساخته شده است
و پس از جنگ ۱۲ روزه،
هزاران سانتریفیوژ به این تونل‌ها منتقل شده.
گفته می‌شود اورانیوم غنی شده ۶۰ درصدی ج‌ا
در زیر این کوه پنهان شده است.
بازرسان آژانس بین‌المللی انرژی اتمی هرگز موفق به بازدید از این مکان نشده‌اند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6306" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=A615eGeWKlHiWRstt2TOlYRUHbiKbyiHHtL05EhW71dmsqZA_hMiTIJwv50UXvkc2sccJ7K4mNbRDK7Qor9ttjLifR7bng8iWsl9FZ5N9A6PLO_Ky3WXrn7aPRk0_pg0TX435bafP5QQ0kPRCoZgIVu0YHR7Px4ejvxt0cNcgcJzfk-9jUDfAakopx6i3mhCsB7NekJx_7KaCPgr4-B2y43RzwutHzhwcN_O4TgcBRv4lzAjvq4G5CCFZEhT1kFOQkZeRqQTPVBKcZyqkoQl4sJNucTqrmm6tn4tb17FK4DyuOqPgbEAdWVu7Ep_IKY3DyhLSvhEhMg1-OKozzlsPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3814b8c91f.mp4?token=A615eGeWKlHiWRstt2TOlYRUHbiKbyiHHtL05EhW71dmsqZA_hMiTIJwv50UXvkc2sccJ7K4mNbRDK7Qor9ttjLifR7bng8iWsl9FZ5N9A6PLO_Ky3WXrn7aPRk0_pg0TX435bafP5QQ0kPRCoZgIVu0YHR7Px4ejvxt0cNcgcJzfk-9jUDfAakopx6i3mhCsB7NekJx_7KaCPgr4-B2y43RzwutHzhwcN_O4TgcBRv4lzAjvq4G5CCFZEhT1kFOQkZeRqQTPVBKcZyqkoQl4sJNucTqrmm6tn4tb17FK4DyuOqPgbEAdWVu7Ep_IKY3DyhLSvhEhMg1-OKozzlsPzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🚨
🚨
ترامپ: قطعا به زودی و با شدت زیاد به کوه کلنگ  در ایران حمله خواهیم کرد و هیچ کاری از دستشان برنمی‌آید.
‏ترامپ در دیدار با رئیس جمهور لبنان گفت: «ما قطعاً به سایت جدیدی که آنها در مورد آن صحبت می‌کنند (کوه کلنگ ) حمله خواهیم کرد.
آنها به دلیل سلاح‌های هسته‌ای در این وضعیت هستند و سعی در بازسازی یک سایت هسته‌ای دارند.
‏ما به آن سایت ضربه خواهیم زد. هر سایتی را که آنها حتی به سلاح‌های هسته‌ای فکر کنند، با قدرت بسیار بسیار زیادی خواهیم زد.
تا الان زیادی باهاشون راه اومدیم!»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6305" target="_blank">📅 19:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=jvNUxTTuATmhKRJnvzL6FpuqCKiDM92WmTgX3bi6v8rbXpt_Rl9Xd_gucqonzoVhBRliMQfJWSJYGhXKp_VcWg99n2LXi5lTVnlSPOQGyGuM_Mh-y25Dc_PS1odyJ6c0-2TOolKF2Nwt_mddUQQLVD9YCB-zCqijo0yS8PhpyL1hqF5zLf2TtHBWBUVxPZbaDMBWrj5iQw4qtYt8tXy5CLx2xXSy_fJ6ZPD2TZNpkfqVLaFOBeBthAXKpGxSC-NflQLRWYdRi3OikkrhEYjWNo-vaCHkws8Clr8T4Y22YCiiWsXE_X9j71tiJCwfydnDS2HzoADESFYiDtFELMH3zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acc280d27d.mp4?token=jvNUxTTuATmhKRJnvzL6FpuqCKiDM92WmTgX3bi6v8rbXpt_Rl9Xd_gucqonzoVhBRliMQfJWSJYGhXKp_VcWg99n2LXi5lTVnlSPOQGyGuM_Mh-y25Dc_PS1odyJ6c0-2TOolKF2Nwt_mddUQQLVD9YCB-zCqijo0yS8PhpyL1hqF5zLf2TtHBWBUVxPZbaDMBWrj5iQw4qtYt8tXy5CLx2xXSy_fJ6ZPD2TZNpkfqVLaFOBeBthAXKpGxSC-NflQLRWYdRi3OikkrhEYjWNo-vaCHkws8Clr8T4Y22YCiiWsXE_X9j71tiJCwfydnDS2HzoADESFYiDtFELMH3zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
نخست وزیر اسپانیا : «در تهران، یک خامنه‌ای با یک خامنه‌ای دیگر که بدتر است جایگزین شده؛ چون مجتبی از پدرش خون‌ریزتر و دیکتاتورتر است و او واقعاً سلاح هسته‌ای می‌خواهد.»</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6304" target="_blank">📅 18:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CQQudLh2vHdC1ByjWhCGTvzsVtCrRZCPoiQCDlV6AYrXf4BCREpnEMGBh1u7RvXiPbSu-rMv60ObDq8v6WiiKCW8y5D30vzi2cn_GO52fQqjIAesabbc3P39PfulmcKYZiQeRidS1_GliSJJehhhDHh2c7MLHlUyAQ42ObaYVkfKR6uN_mW1Tz_VE4wvDtCPH7x1aJoplvn4aRZuufe7zEW124RqPC-4_Rs63fzizhlBprHmQEa90z5N7wLMF9prbG3KeCd59qx2wL3feHeufPdLjqoPEh61kJ-qI_5bXldDUqf7KYuerdejMUn25IB5HAWlzkr__6VH_Ku23cnA1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403aadedf7.mp4?token=CQQudLh2vHdC1ByjWhCGTvzsVtCrRZCPoiQCDlV6AYrXf4BCREpnEMGBh1u7RvXiPbSu-rMv60ObDq8v6WiiKCW8y5D30vzi2cn_GO52fQqjIAesabbc3P39PfulmcKYZiQeRidS1_GliSJJehhhDHh2c7MLHlUyAQ42ObaYVkfKR6uN_mW1Tz_VE4wvDtCPH7x1aJoplvn4aRZuufe7zEW124RqPC-4_Rs63fzizhlBprHmQEa90z5N7wLMF9prbG3KeCd59qx2wL3feHeufPdLjqoPEh61kJ-qI_5bXldDUqf7KYuerdejMUn25IB5HAWlzkr__6VH_Ku23cnA1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا که این روزها دارند
پرچمش رو میچرخونن!
می‌خواستیم ۲.۵ میلیون دلار بهشون بدیم
برای اینکه با ما فوتبال بازی کنن، قبول نکردن!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6303" target="_blank">📅 18:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">در مصاحبه عراقچی
حرف از تونل‌های زیادی میشه
که سران حکومت به اونجاها پناه میبردن،
سایت‌های موشکی‌شون هم،
که همه در پناه تونل‌ها عمیق در دل کو‌ه‌هاست!
جمهوری اسلامی فقط برای سرانش
و برای موشک‌هاش، پناهگاه ساخته!
ولی برای مردم حتی آژیر هم نمیکشد!
چه برسه به پناهگاه!
اینترنتشون رو هم‌ قطع کرد!
خامنه‌ای رو هم غافلگیر کردن و الا
مثل جنگ ۱۲ روزه که تا دو هفته بعدش
به «کمین ‌گاه» رفته بود، به مخفی‌گاهش میرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6302" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qtqprIis-zZOoRLpebOVKqiZjqt_cA0EnryXJ9KUEqD-h_fepuQTdhps6MHpHjBlg5cradzyi7FTpr7TflcpEdJkzeqVmRyqvDQPrbuluM3sgiabTxZpo71EnzFq4FewnfGlYN8nq0Gp-0RLyI8GvUwTaxCBS9ohbMYibLcu-hK8mYhkkl_51sxcVu7JAejeasWWw6sfymm4vJ6JkI4r9ku1rQi3x_HItuWeZuXsAqQVp8ZIVTeEctxi3GDpKmSY0exYXsFGHEjPyQXSv2F0EhZB_sMuZnzKbZTeaWRiwtV82xg9FvTggl8lCd13GejX9tluP2tkN6cpxQVdRlJCeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با بازنشر تصویر گل‌محمد محمدی ۲۳ ساله، که امروز به دست جمهوری اسلامی اعدام شد:
«جدیدترین قربانی از اون ۵۲ هزار نفر  معترض کشته شده.
وحشی‌ها!
کی قراره دمکراسی‌ها بیدار بشن؟ (نسبت به جنایات ج‌ا) »</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6301" target="_blank">📅 16:52 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6300">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MZqI_4B1jfKNZIhAHP8IbL1Z4yCF6hBBs6dF5xtjxiaZjtP--gzqlmA0ZrGeCDuhJZCM8gFpsRx0vD1CMhiun_8eF22ElW4UOxZQZtc4y25Y9jnNCQ_n8YHeTr9gDx28KWImp-1Di2SrKLB3ioJc7jGmdKpGi6U0wUrzyfbeoyoNLTVQcn8spEFBqCdUOgIRiBgmWwLfyareKfVlAhlgm06ckKebVLF7SI9sv474qqVzxRVnTFzbcOfC9VDTEzdF_Ee3KL5n8iZyE68dtgRCkzTFstcVpSbZlZ1yIrbCJgzoHxVAy1ClBSVuAfwNcXlNibEhqsxKVRxLa_u-gRbGCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46c8806804.mp4?token=MZqI_4B1jfKNZIhAHP8IbL1Z4yCF6hBBs6dF5xtjxiaZjtP--gzqlmA0ZrGeCDuhJZCM8gFpsRx0vD1CMhiun_8eF22ElW4UOxZQZtc4y25Y9jnNCQ_n8YHeTr9gDx28KWImp-1Di2SrKLB3ioJc7jGmdKpGi6U0wUrzyfbeoyoNLTVQcn8spEFBqCdUOgIRiBgmWwLfyareKfVlAhlgm06ckKebVLF7SI9sv474qqVzxRVnTFzbcOfC9VDTEzdF_Ee3KL5n8iZyE68dtgRCkzTFstcVpSbZlZ1yIrbCJgzoHxVAy1ClBSVuAfwNcXlNibEhqsxKVRxLa_u-gRbGCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خامنه‌ای: ما دنبال اقامهٔ حکم الهی هستیم! ما هستیم برای تحکیم دین خدا! برای رونق اقتصادی و… که دیگران هم می‌توانند انجام بدهند و در دنیا هم انجام می‌دهند!  بله! بقیهٔ دنیا دنبال ساخت کشورشان هستند، این‌ها برای تحکیم دین خدا!! پول و ثروت ایران برای این خرج…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6300" target="_blank">📅 16:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6299">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‏رویترز: حوثی‌های یمن در ایمیلی به شرکت‌های کشتیرانی نسبت به بارگیری یا تخلیه بار در بنادر عربستان سعودی هشدار دادند.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6299" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6298">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
جمهوری اسلامی امروز دست به حملات گسترده‌ای به قطر و بحرین زده.
علاوه بر این جمهوری اسلامی به دو کشتی یونانی در تنگه هرمز حمله کرده.
حمله به اردن هم ادامه داره.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6298" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6297">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=pThnThfgctJi7U0Bp6c7igKlq6pL4or6jLgQfKJtPwwtBnEwv4iuV3zS3rutFeSVW5BuIP27g240pwUDKCabSFWXLBNr5M0oUPI_c3Z9PYy9CXhIwCk9aNZoiVngxIuPJSsiJbrefT5lAlZjAYTX5tCvRb7TxWOR3XzMDaFVlAnc5OJyzjG6I4FzOvXJtzKsGBsLl5aQ-bh4Frgv93K0qCE8G0P3LlvhBWN4lZhudSlfmO0NFeDHuPTpW5y3Xa0EXfjh7K8z5rcTNtqo4Rts8QNw-TxZyBFemohz_AeWx1xbdCwhABgDlBlktU5x78QsGkE5gJJMPc6ElyIwX_W2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb0045793.mp4?token=pThnThfgctJi7U0Bp6c7igKlq6pL4or6jLgQfKJtPwwtBnEwv4iuV3zS3rutFeSVW5BuIP27g240pwUDKCabSFWXLBNr5M0oUPI_c3Z9PYy9CXhIwCk9aNZoiVngxIuPJSsiJbrefT5lAlZjAYTX5tCvRb7TxWOR3XzMDaFVlAnc5OJyzjG6I4FzOvXJtzKsGBsLl5aQ-bh4Frgv93K0qCE8G0P3LlvhBWN4lZhudSlfmO0NFeDHuPTpW5y3Xa0EXfjh7K8z5rcTNtqo4Rts8QNw-TxZyBFemohz_AeWx1xbdCwhABgDlBlktU5x78QsGkE5gJJMPc6ElyIwX_W2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«آتش‌بس نظر مجتبی است؟ »
عراقچی طوری پاسخ میده
که گویی نمی‌دونه این نظر مجتبی بود
یا نبود! «ارتباط سخته»!
خودش هم میگه مجتبی رو هیچ وقت ندیده!
اصلا معلوم نیست زنده است یا کشته شده
برای همینه که نمی‌دونن نظرش چیه</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6297" target="_blank">📅 11:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6296">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=RC74HrV1-20MsIjYXMggRHI4LG1uGgC6ap5gTH1p8eZXUyMVL7hUaM8SyCAQ2sWOI0h69TVaJ-aqbUt8rRwbdinCD8SQ7sFCxRmPTgbM9GNkcZEW2s9VJ6nBK9ddL_GMT78deXx2P6Y7QtfNFJxWad-Je0iTkqMOihdkyfmMiMCKPs9rPPN8zp_39tcRXWndwEfpEOiYClZEUcpRxQbS1Z-8NEg7CigmZbyUp6JU5xiyH2v1zoP2b1ko3cmdC0Jb8em0jUBR0RfqvhjQxEpfxFZYy6u2pPj8w0DSgEJpb4bEyHOFRW8dOOt1sgNAsdMsbPhf3nSadcYRBxbU_Au9AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/011fb08ef0.mp4?token=RC74HrV1-20MsIjYXMggRHI4LG1uGgC6ap5gTH1p8eZXUyMVL7hUaM8SyCAQ2sWOI0h69TVaJ-aqbUt8rRwbdinCD8SQ7sFCxRmPTgbM9GNkcZEW2s9VJ6nBK9ddL_GMT78deXx2P6Y7QtfNFJxWad-Je0iTkqMOihdkyfmMiMCKPs9rPPN8zp_39tcRXWndwEfpEOiYClZEUcpRxQbS1Z-8NEg7CigmZbyUp6JU5xiyH2v1zoP2b1ko3cmdC0Jb8em0jUBR0RfqvhjQxEpfxFZYy6u2pPj8w0DSgEJpb4bEyHOFRW8dOOt1sgNAsdMsbPhf3nSadcYRBxbU_Au9AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکرمی نیا سخنگوی ارتش
‏به روشنی میگه اكر آمريكایی‌ها
بيان در جنوب ايران ما خاك خودمونو هدف قرار میدیم.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6296" target="_blank">📅 11:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6295">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=urb9WriQtSZkoUeRV2UH-MNZyDsx7lC7KtBkOASjXuZFhCWkP3mr36l4hFX52ryhpVYTWNdrpKhkJQgqxt48itVng2BdOlcsdYRnjXsBaXdkVOcmMfUPn0VJLbwG1Z1q1aQGEyDNU3Y2210K8cS40j7XFiRbjJGDnEdJY9UXF2a9Dlwj5XzEety6OKH7mq7WHqrDRfG7OhiQ4f80zsScnS331z-KrRqoTd4RsHjOsKChEe0Wt6xDAyOTWPgr9iW_3yDz-cCkB88nXmNd1VtlNKY0Qg5Jjt-Ya4deZxR27pCtZWrPuaYzKgqrJ0pN-K4lZ5LbqiHo5MEr9Y-OzcdPLpC9cOBteUUdDHAs3IgqQ06b1VAFfgHS2zRIFMXkd4xbJ_CTrZ_tPl5vELyNH-3yiu8nWh_TyXwkzBsIiMM6BSWdLYk7f5JPUXJCmNXlK-1kedxHRp1Br_pdaiAtYlW_auDb6H5jKzUyZyzeut1rDSFr985rZ0valcUahNrTxmKrxSaaUvX1TSxRK4OxYCTZ0YxfH_MOpD1v1OQSWnarCqQ_TL9n6WBs6pw7yj6DKuTMyt3F_VloOTShdhBmitlVBQPqkZRmjRVWWuASvSXI961FTTsE0kGHxv33AjTYCPTVscUVOPfIvN-dKSdLLrj-I15oF_GKcjW7ZMc9rndwXoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bd1813e8.mp4?token=urb9WriQtSZkoUeRV2UH-MNZyDsx7lC7KtBkOASjXuZFhCWkP3mr36l4hFX52ryhpVYTWNdrpKhkJQgqxt48itVng2BdOlcsdYRnjXsBaXdkVOcmMfUPn0VJLbwG1Z1q1aQGEyDNU3Y2210K8cS40j7XFiRbjJGDnEdJY9UXF2a9Dlwj5XzEety6OKH7mq7WHqrDRfG7OhiQ4f80zsScnS331z-KrRqoTd4RsHjOsKChEe0Wt6xDAyOTWPgr9iW_3yDz-cCkB88nXmNd1VtlNKY0Qg5Jjt-Ya4deZxR27pCtZWrPuaYzKgqrJ0pN-K4lZ5LbqiHo5MEr9Y-OzcdPLpC9cOBteUUdDHAs3IgqQ06b1VAFfgHS2zRIFMXkd4xbJ_CTrZ_tPl5vELyNH-3yiu8nWh_TyXwkzBsIiMM6BSWdLYk7f5JPUXJCmNXlK-1kedxHRp1Br_pdaiAtYlW_auDb6H5jKzUyZyzeut1rDSFr985rZ0valcUahNrTxmKrxSaaUvX1TSxRK4OxYCTZ0YxfH_MOpD1v1OQSWnarCqQ_TL9n6WBs6pw7yj6DKuTMyt3F_VloOTShdhBmitlVBQPqkZRmjRVWWuASvSXI961FTTsE0kGHxv33AjTYCPTVscUVOPfIvN-dKSdLLrj-I15oF_GKcjW7ZMc9rndwXoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها، ۱۹۴۴
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6295" target="_blank">📅 09:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6294">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها @hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6294" target="_blank">📅 09:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6293">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=lhmY9ikqFleroTqglk-vn5uF9cZ61yjp5LrPtjrU3qYwFJa9-ZqoM78gwt6XJP8H7nKR3DkCBm4YHa4zMZhD-bDHYD59lqLEUZg_XFHC6IwEf64Dtx4x0Zbf7Em1aJ9Az1rbLyrg6L0MgJVl4GDYC0kSE_CJV0hH3WLcLY2o6n8rCXzjm-bkYtUnj0C6MzMBJReYEc95t4ZXB-ajqwfdYjTc7mgSr7gZ7bITqbpAbHo2PJ7LCcb2B1HyEI-CtnjzdvX88R8UK_iT-lvtcQvLqjKqUZRYHUAB2aBBjukGGIWJUIHH5IKHtYBT7yzCdR-VjwfFnMUmiMS2YqNSEYNA6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59eba4787d.mp4?token=lhmY9ikqFleroTqglk-vn5uF9cZ61yjp5LrPtjrU3qYwFJa9-ZqoM78gwt6XJP8H7nKR3DkCBm4YHa4zMZhD-bDHYD59lqLEUZg_XFHC6IwEf64Dtx4x0Zbf7Em1aJ9Az1rbLyrg6L0MgJVl4GDYC0kSE_CJV0hH3WLcLY2o6n8rCXzjm-bkYtUnj0C6MzMBJReYEc95t4ZXB-ajqwfdYjTc7mgSr7gZ7bITqbpAbHo2PJ7LCcb2B1HyEI-CtnjzdvX88R8UK_iT-lvtcQvLqjKqUZRYHUAB2aBBjukGGIWJUIHH5IKHtYBT7yzCdR-VjwfFnMUmiMS2YqNSEYNA6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به کشته شدن ۶۶ کودک فرانسوی بر اثر خطای بمباران متفقین در جریان عملیات آزادسازی فرانسه از حکومت تحت حمایت نازی‌ها
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6293" target="_blank">📅 09:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6292">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=TuouVVkQRrOQGUoDmB4hxfgUsjA3tCYfy-wszxjvlSj4iCNabX3mnybFVGTRyQEWSHDnQJJiHqUO7NhOmdCx6xvsI5MccpyjTbB1H_dNnif3vIo8eXFZ5iozW6x2NdnglIYaZdV_c6TgXBGbACk2e3lg_576t5v9SbX-iLNXNRTtRV2ebvyaOXcfPKNlSRBbU6_jOhHQLloVbuXRj6_IHXCYKn4FcTbVgaDRnWrU7UGYYeBsLsYdlbToQYRFpFKZsATiBL3nBhduCgekbuz_qjxoo3tpqgunY6lIqa93-jQ8N9vkoM5TuzQ8uNZHa90PVXSk_8xyBsJoA2_gNFDz0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba53f516a.mp4?token=TuouVVkQRrOQGUoDmB4hxfgUsjA3tCYfy-wszxjvlSj4iCNabX3mnybFVGTRyQEWSHDnQJJiHqUO7NhOmdCx6xvsI5MccpyjTbB1H_dNnif3vIo8eXFZ5iozW6x2NdnglIYaZdV_c6TgXBGbACk2e3lg_576t5v9SbX-iLNXNRTtRV2ebvyaOXcfPKNlSRBbU6_jOhHQLloVbuXRj6_IHXCYKn4FcTbVgaDRnWrU7UGYYeBsLsYdlbToQYRFpFKZsATiBL3nBhduCgekbuz_qjxoo3tpqgunY6lIqa93-jQ8N9vkoM5TuzQ8uNZHa90PVXSk_8xyBsJoA2_gNFDz0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.  او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6292" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6290">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pucAtUexl046yL3YRqEOe1sJLTq2qY2LG8jai_zlxXkPR3hSnKm8GHKPM4HXZCKrobY1kbEOgTdGcGpO4E2xs7LRnApYYD58aYhLRkMU70uDgJoSx01cWNkAJ2X2rNSWgLqgsKUOihyyFVjiPpPG4F-UvAL9rI1GONLh-HCl4w_KWLhse0h0UjfXQZcgt0kNhHvjYXGikJpzAPGWGY2bcEeMMp34PQmj7PW48-PvagqjW55lpWO1AisPwH7ukZGOA9bbqxEjNMABxfZpgNIzFvdKE6bYLv3sDiqh9XCbt_7nwrBb0HCIM5q9n_388rAaLHHndrMz9SEak_6RrANGnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه پس از کشته شدن «یحیی سنوار» رهبر گروه تروریستی حماس، این گروه «خلیل الحلیه» را به عنوان رهبر جدید خود معرفی کرد.
او در رقابت با «خالد مشعل» موفق شد این پست و مقام را بگیرد زیرا که بیش از خالد مشعل، مدافع اقدامات یحیی سنوار بود و جنایت ۷ اکتبر! که چیزی جز فاجعه برای غزه نداشت!
تصویری از خلیل الحلیه، رهبر جدید حماس با خامنه‌ای. هم خامنه‌ای و هم یحیی سنوار توسط اسرائیل حذف شدند.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6290" target="_blank">📅 09:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6289">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wxquyn8N_Rc04CLuWNgkMS1U2leKwoUUXyG6cBrmzJ0cjmZEBryASeUYDdYG_j5maAWfXU28jTpWEBrRIoRXjEdWwdnxJl3BN_BpRF9NHjNtc3TXxl-q_HK1qYtJMx0lRqMoWDDOkw4uEnDltsMGKL_2FxpemxoAPAHMgkC5Q2dauEqmIDBA5d5QbPj0nNbxuYaOx8_-AT6d1DkVYwL10avbCqZA7NHEWYYNVU7j9Qok7KHP_9bFW4raBZK-bvn-s3HWV72jq3ZI8c4-E7doyFzJLbJtaXUUoRJ4C-fCjoNO_ebwS0oHuwNBBdyMfa1NsK3YdyJS3QhXOh-NO7TVAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزیابی اطلاعاتی اسرائیل نشان می‌دهد جمهوری اسلامی پائیز گذشته هزاران سانتریفیوژ غنی‌سازی اورانیوم را به تونل‌های عمیق در کوه کلنگ منتقل کرده است.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6289" target="_blank">📅 06:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6288">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یک ارزیابی جدید از نهادهای اطلاعاتی آمریکا به نتیجه‌ای رسیده که ظاهراً مطابق میل ترامپ نیست:
حملات اخیر بعید است رفتار ایران را تغییر دهد و جنگ در وضعیتی از
«بن‌بست نامحدود میان جنگ و صلح»
گرفتار شده است.
به نوشته
واشنگتن پست
، تحلیلگران اطلاعاتی به این نتیجه رسیده‌اند که دولت ایران احتمالاً نه فشار قابل‌توجهی از موج جدید حملات احساس خواهد کرد و نه موضع خود در مذاکرات را نرم‌تر می‌کند. این گزارش که توسط سازمان اطلاعات مرکزی آمریکا (CIA) تهیه شده، پیش‌تر در اختیار دولت آمریکا قرار گرفته است.
نهادهای اطلاعاتی معتقدند واشنگتن و تهران در وضعیتی
«نامشخص و طولانی‌مدت میان صلح و جنگ»
قرار گرفته‌اند. همچنین در یک ارزیابی CIA در ماه مه آمده بود که ایران حتی در صورت اعمال محاصره دریایی، می‌تواند
سه تا چهار ماه
دوام بیاورد و تنها پس از آن با مشکلات شدید مواجه شود.
Jonathan Panikoff
افسر پیشین اطلاعاتی آمریکا، درباره این فرض دولت که «حملات شدیدتر نتیجه خواهد داد» گفت:
«این ارزیابی تقریباً به‌طور قطع نادرست است؛ زیرا اولویت اصلی حکومت ایران بقاست و حتی اگر این حملات به مردم و اقتصاد کشور آسیب جدی وارد کند، باز هم حکومت حاضر است این هزینه‌ها را تحمل کند.»
مارکو روبیو
نیز آشکارا به اختلافات داخلی در ایران اشاره کرد و گفت: مقام‌های ایرانی به آمریکا می‌گویند که خواهان توافق هستند،
«اما میان آنها و جناح تندرو تنش وجود دارد»
و او نمی‌داند اگر تندروها دست بالا را پیدا کنند، چه اتفاقی خواهد افتاد.
هم مجتبی خامنه‌ای و هم قالیباف آخر هفته بر ضرورت
«وحدت»
به‌عنوان شرط پیروزی تأکید کردند؛ نشانه‌ای از اینکه حکومت در حال بستن صفوف داخلی خود است.
این ارزیابی دقیقاً در نقطه‌ای منتشر شده که وب‌سایت
Axios
نیز از آن به‌عنوان یک دوراهی یاد کرده بود:
ده شب بمباران، سه کشته آمریکایی، و در نهایت این جمع‌بندی تحلیلگران خود دولت آمریکا که مسیر کنونی به بن‌بست منتهی می‌شود، نه به وادار شدن ایران به تسلیم یا عقب‌نشینی.
به تعبیر نویسنده، جامعه اطلاعاتی آمریکا عملاً به این نتیجه رسیده است که
«گزینه دوم»
ــ یعنی یک عملیات نظامی گسترده و مشترک ــ تنها مسیر نظامی است که می‌تواند وضعیت را به‌طور اساسی تغییر دهد؛ در مقابل،
آتش‌بس ۱۰ روزه
تنها راه خروج از بحران است که نیازی به چنین عملیات گسترده‌ای ندارد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6288" target="_blank">📅 06:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=UubnVM7gadLtNX2bzlLeJnG_yFe8iwNJkiGSDbdDaQInDh8C1xtqTLH9WwxvUZhbn0NKZGMoaka8oX-1_NXBOzmHjQzEZmBPhO64aPu4C2HNvrRBbS4HHeMU_DEK5veLWl04XgAHTStcJNriAs0DCmM_PtEJYVjdEKmFBoDzbnVo4OVaer9L5EQ1bIB6wmv729J7HEj7ONbCyP9qZ8lcyvegoVtfcHaWkh5Tf2uXYiJIO-hlO0Plgiky739U5rEj3twpQffWl_Fnu0OuLWZFwXtIWEU0-G62vR4N173iGRHXqlfxIhwIkv1WIkjnHENPQ_4O3y0g3LhcC9zMiFHI0Z17cip4iNTpiTJ3UNQXqGU_9q9wQ0zWxbsdEiy9hTymAP3FTI8JRP6I382dMVaXM6z9TYas57DM5hC-lW9am4llXICnwPg0XHVkwk8P45H6QrbExDT30TDYSuJwnF0bxx0MY1gs_LH3Dj4xyXn7qPdbWZqoS2qMxJLl4DnUzbSBhlYmSsC93UktYMw9QpqDjBDL44scvt1_kPs3vO16vkPP5cgwhPvzo3CKVnh0BS4535L5sG0bx8oQhmEWPdBNiiUovROPdDj5YJPiZRnJN_j1z0mstYZb4yM-MrkgyxPN09YST2ktfO0-UWJFEJGTdxjPbBHinTCDus95JfA0DEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=UubnVM7gadLtNX2bzlLeJnG_yFe8iwNJkiGSDbdDaQInDh8C1xtqTLH9WwxvUZhbn0NKZGMoaka8oX-1_NXBOzmHjQzEZmBPhO64aPu4C2HNvrRBbS4HHeMU_DEK5veLWl04XgAHTStcJNriAs0DCmM_PtEJYVjdEKmFBoDzbnVo4OVaer9L5EQ1bIB6wmv729J7HEj7ONbCyP9qZ8lcyvegoVtfcHaWkh5Tf2uXYiJIO-hlO0Plgiky739U5rEj3twpQffWl_Fnu0OuLWZFwXtIWEU0-G62vR4N173iGRHXqlfxIhwIkv1WIkjnHENPQ_4O3y0g3LhcC9zMiFHI0Z17cip4iNTpiTJ3UNQXqGU_9q9wQ0zWxbsdEiy9hTymAP3FTI8JRP6I382dMVaXM6z9TYas57DM5hC-lW9am4llXICnwPg0XHVkwk8P45H6QrbExDT30TDYSuJwnF0bxx0MY1gs_LH3Dj4xyXn7qPdbWZqoS2qMxJLl4DnUzbSBhlYmSsC93UktYMw9QpqDjBDL44scvt1_kPs3vO16vkPP5cgwhPvzo3CKVnh0BS4535L5sG0bx8oQhmEWPdBNiiUovROPdDj5YJPiZRnJN_j1z0mstYZb4yM-MrkgyxPN09YST2ktfO0-UWJFEJGTdxjPbBHinTCDus95JfA0DEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودبار :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
