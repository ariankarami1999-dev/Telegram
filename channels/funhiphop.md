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
<img src="https://cdn4.telesco.pe/file/mxW25Y1ywUnuUX-nnTxn2KvNbbjS2Kd3JVzOQcrD2Aa1TF2knDl44Dsiiz_zmtXuWxJy3OBg8APUflVwGgIQSB5Yq0mwOnnH6bEjF7VPX_JOmHYDIIVqze_9wmVIf2-P3mT9qQoEjrZBzhQ9jMimmGACEBKTXIyBuTk7Y2Zij4lQkdue6J2gN9YEPHudo5LIwSuYNKVWAwM7ruE9jk2TwL9YCCt_nHeqA4WjXV_5ouJzn88slvPFn-CYlzoF2-JUsm2Lidbmdyn0IKxL7kO9w9YH4OFteVRNci7pdSYGYLosnwYKmBBIaspeoNyrm_cFP-A_e98LrN_ZgmuepScGeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 224K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-13 15:06:30</div>
<hr>

<div class="tg-post" id="msg-81773">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">باز تتلو از تو زندان داره ترک میده، واقعا دوست دارم ری اکشن اونایی که تو صفن تا با خانواده شون صحبت کنن رو ببینم موقع آهنگ خوندن تتلو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/funhiphop/81773" target="_blank">📅 14:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81772">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">اسلامشهر صدای انفجار
اصفهان هم چن دیقه پیش صدا انفجار اومدم یادم رفت بزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/funhiphop/81772" target="_blank">📅 14:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81770">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoaQdLyIrHk-BILDTXVF9SWXewo1lYbqSvIp4xTehVswoxXiBxXSxSBTqpPQnNs2elbV7Z5ezgx7UpOgGcS6YpkMns_mohd5qJcmJasTQJitUCsc09oEm10AqzaV8lKMskmWI6nsmlWfLPrJ1VCobX3NgX38kjvj3GWtd1lPruTh7MV2HPfKTCZJ3IqXxmQyvdPhOm70iHSkBxzV_B60a-qKGv1X07PyhnZjqS0o894fy2heIdjLkepMTrBGZy33VCzKcYV5dG6xEzjBEVqqhlRxG_W1So_2vdQYeKSxn024S5Hs403zFZ-u7xRUHUkFuRY2ZLvy0zBr9yBLOViBzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا صبح قیامت بر ۲ مرداد لعنت!
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/81770" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81769">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/81769" target="_blank">📅 13:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81768">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجار منفرد در شهرک صنعتی شمس‌آباد، جنوب تهران
ماهیت انفجار تاکنون مشخص نیست و هنوز تأیید رسمی صورت نگرفته است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81768" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81767">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=Zg1cayOo7OYrT-vNMH4OPLNfmqBwFrRWkktS53DdpwZRNT0CHMoGHTEH6VUGiPcjpj0IlCcrVDyT16rmK5SICpRpaPRW-mA4hoB_S0RhaFZFnmDBkghgx4gIgxLXUpr_iXDq059mbiAfoNOfSNHIURAaqqi3gBgv2CVCj9Go_M0-WB8foDeCrwv1TX3FyzJb3J_9RcD4tOpXZo2okGqfvQzlt8jWRhzozSCSr_LX0mt5WTgMdcpRop2xLImq3FrMyJ2N1J2x6DOx01arPwKxp4VmK1Mf8hgPYG-8aLcP--R6O1Q90qFbE2OxP76OzyUT7hLdH2rbNqbDBeWcq4vi2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f145e00b.mp4?token=Zg1cayOo7OYrT-vNMH4OPLNfmqBwFrRWkktS53DdpwZRNT0CHMoGHTEH6VUGiPcjpj0IlCcrVDyT16rmK5SICpRpaPRW-mA4hoB_S0RhaFZFnmDBkghgx4gIgxLXUpr_iXDq059mbiAfoNOfSNHIURAaqqi3gBgv2CVCj9Go_M0-WB8foDeCrwv1TX3FyzJb3J_9RcD4tOpXZo2okGqfvQzlt8jWRhzozSCSr_LX0mt5WTgMdcpRop2xLImq3FrMyJ2N1J2x6DOx01arPwKxp4VmK1Mf8hgPYG-8aLcP--R6O1Q90qFbE2OxP76OzyUT7hLdH2rbNqbDBeWcq4vi2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81767" target="_blank">📅 11:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81766">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">آدرویت داره میره سمت استعداد واقعیش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81766" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81765">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8a-CuXDr-47bN2susXe0KEx_X4MbjR46OfXJvEvTfzqRF5S-lJvHtdqlxSG81F3gBzG03mTrAvfSoaAZbyeCPc4aipTfQzahhij7F2mBuI7aMK0kYxU8NcHwSLhwgdElywipvVoQm0BCqtTAm2Fsu_mEQvg57zWxZbeoBjsVt74TE_NkhaZ7_FGVlnSV_Y5ccJq_YKqTZJJSEj4U8PV1ZNPZsWxhYAqQ4WJH9iuDedxyYdYxzocIcTCyLh9rxt42xHuH4guKTTFf0XwxNLqY70wcegl5KLdOAJqwvOPpl8IFDRKzWr9b-GmlwAKvBPPD482MfY_txxOde_q5AVDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بازگشت نقدی بت فوروارد تا ۱۰ درصد
🎲
🔥
با حداقل ۳ میلیون ریال شارژ حساب کاربری و سپس ثبت حداقل ۳ میلیون ریال پیش‌بینی ناموفق در میزهای کازینوی زنده، ماشین‌های اسلات و یا انفجار در طول هفته، بت‌فوروارد در هر هفته تا سقف ۱۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را به عنوان بونوس نقدی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/WEEK
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81765" target="_blank">📅 11:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81764">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=EwmeswfXc7vOmE2RlLpRnvwwFpTBlYGNRhCvNWBMvzqaHfuk-ein57pveTqk--DmfMJmhVX19ZU_wWJoXWx1s6zkRKRfMCtdn12d2NWsidv5624zjhZwmzBR_4imB2RgY-ZLCrg4kaB1FKcLaF-9sNpDPZbGqwXxwXVsPpkTsSh-1FvVL9JVglnKadW7KMkNHjRqd1pmg05uKDedrzoqKwDV23iH6SaZJSex9GE9-u9mUBg-hoye1dWmo5hgwshaqV48VV7rKeuhVNiYOM8Rm8Lw6HQqPXbCzU0VOQbBaFklmYyPQGoZ37kwcdhPnsqsUqxd4E22FI9Ci6cLkOVNgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ac04ad8ee.mp4?token=EwmeswfXc7vOmE2RlLpRnvwwFpTBlYGNRhCvNWBMvzqaHfuk-ein57pveTqk--DmfMJmhVX19ZU_wWJoXWx1s6zkRKRfMCtdn12d2NWsidv5624zjhZwmzBR_4imB2RgY-ZLCrg4kaB1FKcLaF-9sNpDPZbGqwXxwXVsPpkTsSh-1FvVL9JVglnKadW7KMkNHjRqd1pmg05uKDedrzoqKwDV23iH6SaZJSex9GE9-u9mUBg-hoye1dWmo5hgwshaqV48VV7rKeuhVNiYOM8Rm8Lw6HQqPXbCzU0VOQbBaFklmYyPQGoZ37kwcdhPnsqsUqxd4E22FI9Ci6cLkOVNgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایران اینترنشنال: پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81764" target="_blank">📅 10:29 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81763">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kk2wL7e2e0w6Bvg6jKwnp-Fy1MSY7RpV47G2468SmVwOK_XiKR9KwmKLQ1Wqe2LQN1ldZOHAYeOBw9eT9g6752Vfrbi0DB_O8c5K4ZdFGWM155vc4hcZxNmP4Y4KIekunPsABDPPAn74JkfaTUc2F9jYkUEhTKpC4bvTb1Dgx1zzScfwzOiWeOhjQWJEFecDkVVwBOVVuzPrNZVcCwfdaiketyxdJruhMJssFOd1llaJfpfl3dWurYljpPfOSvzrwk-NpT9fv80cYkq0gpuGc5BmhZitcjNIywSgqtVoU0J0ALRfIyetvoqgZKdVlYOd3tMhHzDHe1BtqGQXvxDq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلد امروز روزنامه اصلی اسرائیل است: «ما را دیوانه کردی»
‏ترامپ: «من حمله خواهم کرد. من حمله نخواهم کرد. من حمله خواهم کرد. من حمله نخواهم کرد.»
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81763" target="_blank">📅 10:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81762">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDObaUmY5xcyDeKm5oq6bf-yo7J-aZLRU-i3HVfP832L1u1sQa9v2XttVEptIM47T_aGb2CauvxBx4l3q4-jzAfMTa_9YOpXnxfqVMQAzAv5RWbZxC9GzgckiviozDT0wqpIGEpDfVuGlu1SsPPRvkpOP7F2BGkpmQ-pNAjeU2eUl8PJdo8puTWvA132TZYidR4230bJFI5Zmt27eIcRZ23HUDLVBTMOLZCwpwcD1PxEaNBAmFS5_xP7Ar7vrEZkPQS1eJ1HIpqlwAEIYrA8zq8yC9oSUrv6_s_crPepCmb4wdOKfp_rA2-CAH08u31EP5djBdSsxbLFolztM1yrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی اینجارو نگاه کن، ایران تو تاریخش هیچوقت گنگستر و مافیا نداشته که تو دومیش بشی، به خودت بیا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81762" target="_blank">📅 09:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81761">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=QBmPZ9qqWCawSDOSEIR2yuNE2DioMVjTKyFMR9qemZjoSd53F1CJdl9ZsHIyAw39uJzSU2bHewPBYsesX4ZlBLBBYEBCgV23yN8tyOn0uAB2iySiHEEOJ8qQ6_AiITPF_I9W7Uj4c3t5m2Xh_3cWR02q7RciUG1TFPuBJBLjvMlF4i6PW0F4jnIjL4947mHcdNIx1l6qIdXDvhy8i-UpsV1ax5EnYMWgRclW5aWx5eB1b4ux5oh5TovZJXYC3DFUqRH87i1H_4BTuphnTw5QGZkIGbPY4UgMwZsVQUPSzDKUwWvHSuG8IHX6_dD_HVGIs_xfo44740Fd-mhtxMXhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b42dc58af.mp4?token=QBmPZ9qqWCawSDOSEIR2yuNE2DioMVjTKyFMR9qemZjoSd53F1CJdl9ZsHIyAw39uJzSU2bHewPBYsesX4ZlBLBBYEBCgV23yN8tyOn0uAB2iySiHEEOJ8qQ6_AiITPF_I9W7Uj4c3t5m2Xh_3cWR02q7RciUG1TFPuBJBLjvMlF4i6PW0F4jnIjL4947mHcdNIx1l6qIdXDvhy8i-UpsV1ax5EnYMWgRclW5aWx5eB1b4ux5oh5TovZJXYC3DFUqRH87i1H_4BTuphnTw5QGZkIGbPY4UgMwZsVQUPSzDKUwWvHSuG8IHX6_dD_HVGIs_xfo44740Fd-mhtxMXhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81761" target="_blank">📅 09:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81760">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ایران اینترنشنال:
پزشکیان به احتمال خیلی زیاد می‌خواد دوباره استعفا بده و احتمال اینکه اینبار دیگهi حضرت آقاA استعفاشو قبول کنه خیلی زیاده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81760" target="_blank">📅 07:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81759">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81759" target="_blank">📅 07:41 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81758">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">دوستان خیلی پولداری که از سیستم‌عامل iOS استفاده می‌کنن هم مراقب باشن دستای ظریف و زیباشون اشتباهی نخوره تلگرام رو پاک کنن چون تلگرام از اپ استور حذف شد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81758" target="_blank">📅 05:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81757">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLnNC55u7phsQPyzf0z17GYb2tzBqQ9R0eUczOjaq4cqkb6w-35SRjJmGz52UD315Z11md294NxzQGlNEzRti2td4DWig4Mu_-NL1TAwUAqHsDDyrUkOTgliOjmBYH-g7rNo3iDnsuajln54kXGhlF4G8rjL4n7olrVHXpTpHlUxCbBfzjulzuUPb5hdeV1ddfnW3TRxCHfKMTXRG0j9SOZIM9yX3_ZG4qytTXGkfws2YArXIZDFb00PlYjyxd12ZKQxJz5Lz46GOJRp3htv2ZvjHlPOmMRPl4VWxOtXQZaMxWGy6bxaP-ZU08Dvy2QdGSRF5gnp7VFSsiaeK2eYQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد. #بماند_به_یادگار  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81757" target="_blank">📅 05:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81756">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامپ مادرتو گاییدم تو که بزن نیستی فقط تایم خوابمونو بهم ریختی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81756" target="_blank">📅 03:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81755">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDqq2V-lEQnz1Y_Jgho4jYE-iBHJNyEqrbHu8iNXoY3UrhZGK0cfQNF_W1KXY43bWoe05d8j6YTIdGG-C-0W9A3hc-UApnALEcIMnQNqN0Uh3o8lMHmT5fJvthGNSZwbc96TY6ufxkvS7A8-nBgXO6l1sXuW_0kAoIA1Zw6PHoMSOxaAvHIDzZS9UWuYmUiTfiECLWI35HcEYXoJwUoi7DlDjtbitj0bGBfgz3Yp18b81HLu4_OT2GOgdqQMM3-nXTFp7zRET_FKdBNdEvyKhMb_b4EILL09SBi5tW76simg3EKPAhzO4Fd9Iw5_lbHpgRTzsmyH2_4oNjrg-J-ceQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصخل کسی که تایم زیادی تو خونس خودش نمیخواد باهات ارتباط برقرار کنه اصلا که تو بخوای دوری کنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81755" target="_blank">📅 02:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81754">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محکم ببند درو، دیگه ماکان بند نیست که بهمون حس ناکافی بودن بده و بگه کار اشتباهیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81754" target="_blank">📅 02:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81753">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBARNR6ZWMgfTjsNH4gWQWmTFLFJ-MwVYE8PF-WaWbcXMJ9HcY_EmiGjSJGG5wgyJEtNJOAtP3mrbo-a9XL77LeZDIdb3EZlRTHjZb69_zRZSsDCXBxJx0rjHloRET6rrVKwx6Ozi6HIhGjkzf0bqGPaitFxrBe25mqU80ul2nrojWSdGMD0Tw_KF3C4OHVHoJu_XNUowSm7wnNCMsjBVlN3qbe3vSpJgEhMsYFIFbK4XSfmA2XLA2VxGRl1-fJrP9eB6G3BMXPGkdjQDgJPqhedwk695O_ddMw3LdPHjhdtU-N-akaVo-g8zY2C6kgtqAFnktwANxW5DEC_ZY1-oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرا رسیدن اربعین حسینی رو به همه شیعیان دنیا تسلیت عرض میکنیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81753" target="_blank">📅 01:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81752">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ستار هاشمی کیرم تو ناموست این چه نتیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81752" target="_blank">📅 00:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81751">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74b8952566.mp4?token=Abb1RUZIQ-D-sc2UdaOnTqqXvDmo-H6hsr5_r4ykIpjY8A6afgm99ybWQoETlWggjJHc-i-0MLAwphiK2tfVE1fwgTXQc-A94LIq9rqLe1FNFYzqFT01HQRpj6D_g--JHxoKu5LsLMK0NVCIhfj3hPs4G4P_M0gxusR3wJIq_3R-gvCUNV4f7UOc2fhYYT34bgyWM5xEeut0L190ahHtNhrvAP0txVz33oZouQe43PK3Ob2fGV1f6E1kTLp9onfeesvwJRglQIdBimMt4IlWMpvmliDIrgW5n3tTN1OHwBmGg-Xa3Ri9RLr6RPE_wMVBERVTUNzgqtRX-Lp5hX5Pcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74b8952566.mp4?token=Abb1RUZIQ-D-sc2UdaOnTqqXvDmo-H6hsr5_r4ykIpjY8A6afgm99ybWQoETlWggjJHc-i-0MLAwphiK2tfVE1fwgTXQc-A94LIq9rqLe1FNFYzqFT01HQRpj6D_g--JHxoKu5LsLMK0NVCIhfj3hPs4G4P_M0gxusR3wJIq_3R-gvCUNV4f7UOc2fhYYT34bgyWM5xEeut0L190ahHtNhrvAP0txVz33oZouQe43PK3Ob2fGV1f6E1kTLp9onfeesvwJRglQIdBimMt4IlWMpvmliDIrgW5n3tTN1OHwBmGg-Xa3Ri9RLr6RPE_wMVBERVTUNzgqtRX-Lp5hX5Pcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آره خلاصه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81751" target="_blank">📅 00:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81750">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=f9IZLHUmhXkIzai9C_dzJGM8vBObiTpZY4bt49pEK98WYgIdw-ZWV63CSX1Kza3pjg-2JpLSokiC702yg35JxyYTelQDOkVcMkhUXEeKIIhpBYtZMYd22HkHOK7l0FTiJoiA9fwyK29Sv8H0JI8kdQYPQ0rjGwwMAP5md7rTGwHmVhKuuUBplpOuo6gg-RkrlFkX0MM5vcb4fYy0fCJ6AcjUSAQ4VITBRFfReVAklW3Ag134VlyAepk76lEZk236wCCzC78UZEGl8NEECXjAXaHwgYbPQd62CKpIjGOlacLaKKu2v8mfY86ijKK8i6T0Xggs5OSV_CeRkZYT3N9TBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f96365f95a.mp4?token=f9IZLHUmhXkIzai9C_dzJGM8vBObiTpZY4bt49pEK98WYgIdw-ZWV63CSX1Kza3pjg-2JpLSokiC702yg35JxyYTelQDOkVcMkhUXEeKIIhpBYtZMYd22HkHOK7l0FTiJoiA9fwyK29Sv8H0JI8kdQYPQ0rjGwwMAP5md7rTGwHmVhKuuUBplpOuo6gg-RkrlFkX0MM5vcb4fYy0fCJ6AcjUSAQ4VITBRFfReVAklW3Ag134VlyAepk76lEZk236wCCzC78UZEGl8NEECXjAXaHwgYbPQd62CKpIjGOlacLaKKu2v8mfY86ijKK8i6T0Xggs5OSV_CeRkZYT3N9TBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81750" target="_blank">📅 23:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81749">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
الان میان میبرنم
ترامپ:
چمن مثل انسان‌هاست. آن هم زندگی دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81749" target="_blank">📅 22:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81748">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترامپ امروز (
درحالی که دیروز گفته بود فردا با ایران مذاکره مستقیم داریم و تنگه باز می‌شه
): فردا تنگه کاملا باز می‌شه و بعدش هم در مورد هسته‌ای مذاکره می‌کنیم و همه‌چی به خوبی پیش می‌ره وگرنه خواهیم دید چگونه کیر خواهم شد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81748" target="_blank">📅 22:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81747">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترامپ درباره ایران: این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81747" target="_blank">📅 21:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81746">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترامپ درباره ایران:
این آخرین فرصت آن‌ها برای امضای یک توافقنامه خوب است.
(آخرین فرصت از فرصت یکی مونده به آخر قبل فرصت جدید دادن.)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81746" target="_blank">📅 21:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81745">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSWgiRAdPjQFH1_UvntvXn4cXjXhut-gvsSMz5qxd5TkzmKWRyj2Sc4j79LY5WIcnHBC0xVlgTBO0ul78Ki78KFAlXPQT0VfEsqcaw_tcxcevFU1DfLzhT5ufluJWs5XkqQhSXdswv5Vi7Ey9xmbFpogwxZJTrhQ5Ygsk268UHD3RdyCAymbpOeZGJz_zjAGoDRwsu0fCNNalg8PeG1VNePMd_XN_jlqnEJ13S6FbsDIjuU1eOAiNYkFr5N4b1R8iskKBj_vMvpWg-Ikxq-TLUnpT6Kkh8nxeVinbtPYsIyuqFDFkapRXJxbiWyAfPEIyXBwqTwURr4YR0K11CEapA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسایی که جانفدا اسم نوشتید نگاه کنید شاید بکارتون بیاد
مستند تفنگداران دریایی که با همکاری نتفلیکس و ارتش امریکا ساخته شده درمورد تمرینات
و
مانورهای
واقعی هستش.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81745" target="_blank">📅 21:28 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81744">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv2L5DYcD2J5HliTjB-4Q5Tx95ZDJDjl0cuD7oj1PwV59WWbKAUb6rtvsY_fSdYIaaS-g1EBULjq0TCsl7hzoUfV8gdkLlu_ODr_gU-fFFjATn0swBUWl0YqGSAwxcssu3IWDIuxcLrdRSniV__2AYCCZo8MUO-bOD22bT_W5Cp5lMmxo3tdJmKH5MhfjZ_a2TPweJZpVYtfo6Sz9LlKw0-43TmU31RwSiUOgC1qWvPkKRIajaDuLFXW_u0KnnAdXmBN7J3TfLRvmyT22LDWfcoEQB6nsFbqMZGhfga8t6hE6R2-RVmcUEtHMdBMlrZPSArxte6flZZ3KgPbB5PJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاحالا دقت کرده بودید اگه نقشه ایران رو برعکس کنید میشه صورت ترامپ؟
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81744" target="_blank">📅 21:10 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81743">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMflGn06pxY_4xoh3Uk9yayQhx7ii-sWQM4mw-m0GQFZn_tkp04sJ3mHmN_zHW0hm4DRQT4vFTqsHytvHVb4aZi39ifvFRkls9SVzoOph9tXVb8mBDz2hv9TTHf8cgsCVrZ7HTAy4m69vXDGCJt8mpY6iFoWrXP-0MHoI4GQx3iPLu0xi_uv7ZWJJGHLtSBketURVicFNaOkeX4yO1g8MIX3Wiukb5Voq2DxkfnEYWJxpT8dZsbjxqaDug5fesBB12zTgjSkE8e8RjWWDXSTNDp-LPK2cKrStgNZCXMdObZRKEFS_dnCQJVeiukCwf3FHJzbIwxCimDeW2U0hRSQlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی جدی می‌خواید بگید هنوز هیچکدومتون تاکتیکای بسیار هوشمندانه‌ای مثل «انتشار عکس مونث بی‌حجاب کنار صندوق» و «مجهول ضرب در ۳» رو به این میانجیگرای خوش تکنیک یاد ندادید که به این زحمتا نیوفتن؟
این بود رسم رفاقت و برادری؟
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81743" target="_blank">📅 21:05 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81742">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNBMjEbRr3UN_IivRW6mBS0GCNhUv3t7YpxHK52ram6uUP6rdPecX4rCo2b3_B1aV6OsUdzjjVWXMkAhjUyBxGmVdIoRugh76CuVU12Wxr3txkVbNmRnG9YcXYoxhkBTqW_UPRIct_oKuHtJ1D7uUwWzd40Ko6YIcmnBv1qTMIO-RebdYMEWaoGp8G6NNzBgitPovU53JloPGpmn_jdr4exHtZmhWekIglVoEXAq7d5aLhEI6Nq3PhvQuxzny4T6JImIaRjnpSq8RfT-GKl8CTz8STj2GP78iym7jUCjlZdpAkSvV1W-OWuCw__qS2zGiZw-DIRdRwPRDTPytJhRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ یکی دو هفته‌ی دیگه به این شطرنج ۱۶ بعدیش و مذاکرات عمیق با توهمات و تخیلاتش ادامه بده، ارتش آمریکا تسلیم بی‌قید و شرط رو می‌پذیره و بعدش روند ۶۰ روزه مذاکرات سر فعالیت هسته‌ای آمریکا شروع میشه خدا بخواد.
#بماند_به_یادگار
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81742" target="_blank">📅 20:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81741">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">به ابر قهرمان های ترک میگن ترکمن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81741" target="_blank">📅 20:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81740">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVRrG9l6UonsV_OkXTiu1wEtuaQzUdJ72BGTmT2_FZSm9JTy4_nYhLDuxdQ9FFCKBfJur9u9uBdBnYXTIrTnTc1q1n9iNKMZ0-hxFScr1l96trB_lmlwgyJSGfAbCXC5NEo1Z-YCCJ6-Sqd5cmnyptNw1Wqvf25HD0XXvvglgELLVs3zDE7z33qtaEXHk7GFiYbUre77RP_-PKfNhJ5p4OxZVMCkbJ_n3Mw9H-H_Gv7Nzf7Fg1iCXR7zasIiVBzcICIz0WbW910FZQQRE-HRbRgNtWLjZndaP5A_KePOPFuq8V7WSwUTTPJS-1QBdalwMNr2m7qC7BJUy5jEeIOpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.2  پ‌ن: بهم اعتماد کنید و فصل چهار به بعد ادامه ندید و ولش کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81740" target="_blank">📅 18:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81738">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2wHA8OeN-PDueHYVOR47cviHQLw93OQSKXw1HOngfVC4K6PQbZN9hP7iVPdylaE7nnKmv1wCGll_pVigMrSQwCcyph0DuO-UEwRAo4dUN8P-aGvk0ijEpOtWmYyTw1f5J8y1IsW1501uZRjJmuTQgkAhpXrruTjHpGfoHW7ZiqrK40K_zxrZighHlifbNRrTUAh6APTNbGJRK-7c0cUiyb-MkTOzuByaYqmQvftPDK3TfFco6sJbhsoyIvEpV5q7Z79ZueGolyqXgDdxH4GYxQLXLCl_SQunj18q0ufj_4q8tswZsa_L2COGSYfNScwoirMku0bKPwClH_qS9YQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هری؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81738" target="_blank">📅 18:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81737">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlGJotRqsS_SGPiIm2ZD2TjKkISQvUseHK5CjbZF1d2sCJcWpHPYsQ7GJI_P4qgcRxAdpUu4LLCMXKVlRfqeuRyWdNQElvnWfwMcsUcFBj3YO-JV-OmPUwn2CQ6BA8Lrmc_O63ZTVphokC0JUw2sP1qegQyk-FfvPCal0-APrBtl4r6AtMtX_96MCRGvovT1uhsXmzyWkdEgssnXF0sgQBaYl6Jav6DBE5f7bFVZMREbWurGAg5q0kfC3qboeCfHYxBCxzjpkwsTvlpBW_MDvhLC2D0nbS7u44V5hL9FVC4tzCvR7r4t8V0hov4CP6QRGQrVEnnVHk-A9w2VpYNmjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از فنای تعصبی رونالدو و مسی و رپفارس شروع کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81737" target="_blank">📅 18:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81736">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحَسَ</strong></div>
<div class="tg-text">نشور سفید نمیشه</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81736" target="_blank">📅 17:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81735">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maw_Lkp_9OoooBRfbbSV7Vx3FX0PZJPqRJJJOAYQuOFgtQqATOU1uUQCo8pJU21pN27m0RiSQgGhQ5qCrqHSfQKsKKvBnbNyAqQ6-7brXooTDTgum_b08HrTAPPM5B6gTdEKmoNvJeb0N1IoIrCqjaYLnMJbAYdKXSuD8iAzewR-gqjAz2ank2rgpoA5wJ6O7Ry8D5LXNShJiMA9c80a3UvJnjiWWgRd-4YdJJ-ckaNBTlkXfKGyaNOt44yCH13qXMV86EECO8a6wQTKcqvwV1PONF2gGrGxUCQS2bKE5Z1SHjxnBDw0-3VRDcNkxnDaFYZrA0zPzHQfo4pqIeCLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوس دختر وینی داره پتشو میشوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81735" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81734">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZ9k-HbjGASIPpG3aGu1qLrXqk3anhmt_kpJToByk3owvs9nanMX5R2xBhCd4m0O87l_1xVKpC_C3nHAU127jztHSzgH9JdyOYsZ2rrpUJOaMHNilxEnDvj5z-hZ0bIhIw45Hwld7F15FQPrlAYxKeMyvnWN1wZZEmAVseUt1IcuJbt_SBYEKdrykqnIUM2xugTzjBYMiDbQ0ky028-i4bgwh_c-lg_4-nGmuVEXrxf9vXaXQxVfFC1Z_7s4_ZMvIMK0_oiY6cJRQomnSBA53_n9F5POegWzSDFhEegvIrigp9B5Ipil54uLNJ_ExGCrYUszfQmhcquRaQIHXZjvYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81734" target="_blank">📅 17:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81733">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">-خانوم جورجینا ایا وکیلم شمارو به عقد کریستیانو دربیارم؟
+عروس رفته جام جهانی دامادو بیاره.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81733" target="_blank">📅 17:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81732">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9qQJbggvJEzLCm0n76OsljePD2AGwUbUA-cMUKGXEBFc_ijxElIhYYUettpc19re5BQfcjWtoFVDVAPigSD6Lm_saq_2AmAqcl90YKV7RirtEZkeNaLSwPP0JmYZfdx-m-fTEaUKEfKDu7fJO5QRleYEx18Ysy0DZDhUP5r3L221Ut1ILic8HIYJedBLfDhf-RzqcyTDiwnlhOpS-6tFNLbycBUT4T_2Xph6np1aC7P6usvF3fScCMwaylDfNtTOnr5U6Rr4N-qSKb7lNMYnE3GLgbsyBO_LFwpWolJ-BwaBhG_Lc9OkKdHRYgpwmbcB2FcegKg7vpN79dOGnwPvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش هنوز انقلاب نشده ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81732" target="_blank">📅 16:45 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81731">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خفه شید تلخون ترک داده</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81731" target="_blank">📅 16:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81730">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جواد ظریف: بسته موندن تنگه هرمز، اجماع جهانی با همراهی چین علیه ما ایجاد میکنه
پ.ن: خدا از دهنت بشنوه اینا باورشون شده قراره تنگه تبدیل به یه سلاح خطرناک تر از بمب اتم بشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81730" target="_blank">📅 15:48 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81729">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AqPzgFd9ZZVPoZa9iDKPXhSrMCr0odhMsHr73dYyx0CoJdCwBx77k1Ms6nN1QXwVFfkmI7NwstMron7SGpAZvQCEWwxcgNuUwXPmz_XPBh266AQoHCwQ7RcHnjocHZXi-IYowUn9TKJ_pGbBy9MDJvs7z-QBZnTqvQToO6Mb-LTy-gDez92GZWTjhMRESTIZg8A8B5ILRCwLoLILZSOaAzfx_YesPOLuFjjn0PQ-xpwckWo3aT6dq8gHy8WOc0-3QxxtqxfNVSZyu1zU2iq-Gn2u2SuSEQJp9KKzEqFXSYrdTeFU7idOh2Smr_VWN9l1Vw_K7xsYqb0-HJN6qLehQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر دردناک بود و جانگداز
امیر و رهام از هم جدا شدن و گروه ماکان بند منحل شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81729" target="_blank">📅 15:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81728">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPUoXRYPGh1go9T3O9DOqLrdf7ZrFe6CGO3cGyHhdNhMTzZ8pqt8-80TsXtz7LOjy5Dw0eJlj34jJI6qzCC1i5lDmJN4RyvAY-HX2_AhosOdV9cNgfMfrezivse56xaRvL36Xj1eMQbSjhg2dcV3-fuoHX9br0Fh0UlI0gvDAWi0bEmer2SrAeE91zL9ia39__6Iqgd-wDrHHMY6x-DAWHrBNytIH-PAyCYpvRExMOZjbDuJaDw4SoubeCRWN66HkI3djGmgacHA97TaonuiIoMAiG1p_Tt71TC1tnv5dhWJyiJp8eiMqr4mb4STxoMphXk1VwhsxVlZf9IqZW62jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ترک چندوقت اخیر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81728" target="_blank">📅 15:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81727">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81727" target="_blank">📅 15:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81725">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgG7g8QufPZE9oObpB_Lm90BBFAveHnBHF74QoPJzi-MevTFRhnHoh7fz0cGRPsMXohAM-NBLnR-RgK-00WkMnrOAJLIFChY2sPkn_0cGnoURUgvdiZIlcU7q5LoVbXuBMCEGA9YpzMfufiqwn8QDFBeOCxK2sqNq9Mr3YiQ5SHgwIPIc6jP4se6kWNSS2JpM_NwuuUZ_I_zJDfQjxs5Ue4P_5TaMCfbHnP6uV8aNbg7YvwvCLjTmBvjiyjSHbfQdoAVXV0pobvAubREiaIhfGzLc5sqZ1UPoPg0DGamWZXLmBhe47idcVKhe8rDNWM9iRd5ioVg1GL8VlMbYc0q7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بستنی قسطی ندیده بودیم که اونم دیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81725" target="_blank">📅 14:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81724">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">هرچی پیج تو اینستاگرام میبینم به دستور مقام قضایی بسته شده، وقتشه برا پیشگیری علی رو دوباره ادمین کنم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81724" target="_blank">📅 14:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81723">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/so2gzd-XNVh4tZ6G6X7aj3tUSmJe7OAATIBf390fevPQ9jBmDeVzJTBP_mWOGtOCTesWlXphj85ytW93sssHQuB5768gY1lU5J7Yh6acLt7MhFUksEugi0xh13hrQqgJOtpTkPWJBo-4nKpa8UXozFJUaYSzQ4ewtoFR623bk_3a17hZcrK4qkZme0IKq6TCni8swL9ElV7Q1_YN4xLbC_io_JWhYK0ViuNteBNBoU7JG83BGM1wsWxrk6_DMqS5qmN1vGtjow2KGPQ7utdc_4Ww19zpvW8DpGYRRMeKV0au1K5rGCY_n-FALYnD9JOtQfIq3riabNXLycNjvkNLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا، حافظ ممبر های فان هیپ هاپ باش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81723" target="_blank">📅 14:18 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81722">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">با این حجم از هواپیماهای باربری نظامی آمریکا که به خاورمیانه میان و می‌رن دوتا احتمال بیشتر وجود نداره:
یا دکتر عراقچی پخت و پز کرده، توافق خیلی وقته پشت پرده بسته شده و آمریکا داره تجهیزاتشو از منطقه خالی می‌کنه؛
یا اینکه دکتر عراقچی به معنای واقعی کلمه پخت و پز کرده و آمریکا داره اونقدر بمب برا مراسم بعد از مذاکرات انبار می‌کنه که قراره ازمون یه سری یاد و خاطره و چند تا کلیپ فرید کنزو تو آپارات باقی بمونه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81722" target="_blank">📅 12:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81721">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e8ru4ncidHzWJ5-OcYWXr8acy8f5E7DQRpv2HUEKhAC6-mhe2YcloH1tnXfv4LGjum5C5VgisNtszuSlZUPU4N9pCMC25KA2U2kX390_XzA3_T40__5x37MoeqQO83QUWBXMps6P8xIT8KoEgx3v1DhAw_drzSPXsV6kh_VdO4zV6geZ4SqPe5zLBDRsii1GyxMkowQ3XU_Z1TNe0v4YjoGCg-18Fp9q4IDM8EIjLXWNn2EAQlOVs17qvmvKZSI9mXtQQ5wkMuPcdTZkYNYxLht2557jK-11qFXdOdlH1Z2wxDY6gtnMudjSlo81MpvzlUa4IhIm3zHdEfwe6OHAaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره واقعا به چه حقارتی افتاده بنده خدا؛
اگه بچه خوبی بود و ایران می‌موند خیلی راحت می‌تونست مجوز یه کنسرت خیلی خفن آنلاین تو لایو اینستاگرامش رو با اسپانسری دوغ آلیس بگیره و برا هزار دلار بره هیئت علی ضیا کاتالوگ فیلیمو رو پر کنه نعره بزنه اییینهههه خووونواااادهههه رپفارسییییی.
جدی آینده خودشو رو نابود کرد این پسر.
💔
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81721" target="_blank">📅 12:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81720">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رسایی زورش به مذاکره کننده ها نمیرسه هی میاد فتوا میده که اینترنتو باید قطع کنیم، ولمان کن دیگر</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81720" target="_blank">📅 11:50 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81719">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=YBe38eRXL1nwGQWwUh56GRfw9H9PYbV56rA8UJkGpqeQTtD4XD75R3VvNqN672PZMfbQ7F96wVyDmS4xJCV8hAIDOKmWZjioF6zDTPTZkMAdcdCXz9OIPaNmOOsgQmzoYeaWuIJxMlfTWUn-053wP02wDRdZQFlAl_DtZEyJrdCfpbLBVXgzTtwKXiLOWhdNbh0kPQ1NnPcSYrMWw7jloMT3-vzTGrY3j2Ne0l2nXVF3CxRGNTC1q4wcdXkJv6YVngPMO8rNfPQrjg0wAsyOkhk5HHB9Gz-bOb0_0eggMdo5Z52S29NC2grzjqn5gZJqCPYMDp6gucf1paFENQlrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae84dba5cb.mp4?token=YBe38eRXL1nwGQWwUh56GRfw9H9PYbV56rA8UJkGpqeQTtD4XD75R3VvNqN672PZMfbQ7F96wVyDmS4xJCV8hAIDOKmWZjioF6zDTPTZkMAdcdCXz9OIPaNmOOsgQmzoYeaWuIJxMlfTWUn-053wP02wDRdZQFlAl_DtZEyJrdCfpbLBVXgzTtwKXiLOWhdNbh0kPQ1NnPcSYrMWw7jloMT3-vzTGrY3j2Ne0l2nXVF3CxRGNTC1q4wcdXkJv6YVngPMO8rNfPQrjg0wAsyOkhk5HHB9Gz-bOb0_0eggMdo5Z52S29NC2grzjqn5gZJqCPYMDp6gucf1paFENQlrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی فنات دارن اکسپلورمو تسخیر میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81719" target="_blank">📅 11:35 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81718">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrZVlmHBS0suWhC5fI_WQXsGxNPX5_BBrWimzyLJXyE41BTEcKYalga2KEPlJUyAeq_iVCXV3HMO1svk0xt8BnOEYqy2SlefmeBbFOixafNynrL3Zgykp-RC9y_xC6AE7XIlBwsEBzBHjSc9EiSvIPcBoOk67m28113_7XnhYkibc-GtfuoI4i4dHf0b0qjkb1G3zzIUzwofVe1TJj7VDL_kl8wN_MRywRlMQj_d37SnPaZp_8Mvezg8FVgoTED_5OZGLDflem_k88PRC1vUnwk0lDNJfzGXVp_HGaF1aPZoYkb4qTQ02Rz8JkU9fwpuicLfP73FG0FpfJUJwMLo2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگولیییی
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81718" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81717">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=jdQPuA-xT6vgs3l_HObc6wXFg1-fM720u7yAkp68AJv6kETv6tlIsvggBL1iEsWSDS9_K5WB57iY03latECOEUHmdiu6Z-YIT6y_O_bLjOMSKBrP76MJIg93XMqwZAzv3CTRDTs3-RNIK4P0O79HwKzKT8JolGVP9TcXybCY1xa21X6HcBjNqocZHeJeR2J5jIxIo1yIYsU03vNDzHoGsrgpaP08TGD2ZlMysiQeU6QNDg5IY59-ihF94sR9gGQrIhBikxn3yszCYgNy41dyKDd2_cq73USm-hRLig98qX5XeGKiHIYuN0hNy8jynefNhtlqXwSRchlYdQlM7e8Q3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65e5e60e28.mp4?token=jdQPuA-xT6vgs3l_HObc6wXFg1-fM720u7yAkp68AJv6kETv6tlIsvggBL1iEsWSDS9_K5WB57iY03latECOEUHmdiu6Z-YIT6y_O_bLjOMSKBrP76MJIg93XMqwZAzv3CTRDTs3-RNIK4P0O79HwKzKT8JolGVP9TcXybCY1xa21X6HcBjNqocZHeJeR2J5jIxIo1yIYsU03vNDzHoGsrgpaP08TGD2ZlMysiQeU6QNDg5IY59-ihF94sR9gGQrIhBikxn3yszCYgNy41dyKDd2_cq73USm-hRLig98qX5XeGKiHIYuN0hNy8jynefNhtlqXwSRchlYdQlM7e8Q3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببین علی گرامی، پدر تشریفات ایران گفت اول تعارف، لطفا بگو الان کی بهت تعارف کرده رپر شی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81717" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81716">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DrrKITFK_tdoEHQGLv39JsZPaERatXd7vcQbb29Fi1Q4Jw9nnDwzyX8775cbZiHWW_dv7nVnc1AyMSqV18znz0TOC_XOdeneUL_NiyTsAAM2KeWUx_AZH5eAT7xd_JrugAxFPu30bC3_abeJmb77Ly4_W35YgwtttazC2jFqZ1VDbEMJkEqRB4KdtVaEOhK9R8XWGKTrzdX2S1vWGpQx-j7jGGwXkSJQ-BBsNN48p3E9Rhn1Bqk9fmuMBayE7FO6fNhpTvBJTA44-hncmd-pM0LbA7YMCDdy_Agj56JuvwUWUsj02lsOtVEOLoKryWA0qigH1hF79tVfjVbLay5dhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81716" target="_blank">📅 10:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81715">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">امید بهزاد و پویا صفوت، از معترضین دی ماه اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81715" target="_blank">📅 10:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81714">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ببینید ترامپ چه روانی ایه که لابی سیاسی یهودیا تو آمریکا هم نمیتونه کاریش کنه، رو اوردن به لابی کردن با کشورای عربی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81714" target="_blank">📅 10:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81713">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: حمله‌ای که آمریکا برای ایران در نظر گرفته بود، می‌تونست بزرگ‌ترین حمله از زمان جنگ جهانی دوم باشه، اما متوقف شد. محمد بن‌سلمان ترجیح داده به‌جای حمله، توافق با ایران حاصل بشه.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81713" target="_blank">📅 10:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81712">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5kCqehkri1uzy8wjPCLeQWrV9cSczt-PvsRjRakVLJCypvu3yggxLTxFdu_zB8rVLXWk3RQixCW7mHGO2HPTOlFpyU6dv_D3IQotSaYodlB0B_x6blxII6IfKwciSBBdPJyC81CdQMf6nwZ9z2gCwtx6q9ZgKWynRBclrncejQ9ZCCaRFeu2ABLf7WjUW9SYRXjIuMMNUUH2PjePh2a5v_n9ZLo4lDXmYfoy6NafMIJQ84-ck7S9qhUIDLAbW36MgOlKIo4eaEzk1qp0nFjX05okGzMAQ8TSc8EZ3oyhDc9aBP1mkgyGmVA5xgm0rVSjTqe1UGEo1W2J8Ric_5NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میبینم کاخ سفید این پستو زده بیشتر تنو بدنم میلرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81712" target="_blank">📅 09:49 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81711">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8hgpReS3mrrKx3MvWSosrpa8Xkp5caDbKtdc7v0pxrYB8xb5Bn00s-3eX6V9FoeYfIYD4eYYTigotsDjBj_-wAojpEveORv-EFMIE4BprdL64pcccChwdXUeQU0TIAGut_arrqHRdLblrC7MNe8GlrfbCCayxqoxADcJQt-IyFCV9FZCd7Y3uZIk2pndQFxbUbE7eJN5htugMFg1G7JHEabg2A5-2mZdvhD7LCBX7A02HD__vtdgslEPxP5UWvBEgeR6Eoy0XtG1ViCzMRnlHH1BNOBjoItOfpdLxkKDC43Y8Xuy6Ta6LMnX6E0wigUTQazbZ_sAR1dXLhSFR_BIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام نه قطعیم لطفا آهنگ نده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81711" target="_blank">📅 08:59 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فوررررررررری
آکسیوس: منابع نزدیک به کاخ سفید تایید کردند که تا دقایقی دیگر ترامپ دو نقطه را خواهد زد؛ پشم‌های زیربغل و خایه‌ش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81710" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/81709" target="_blank">📅 02:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عباس مگه صبح نگفتی تنگه بازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81708" target="_blank">📅 01:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/81707" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SroFp3d4-aDgCd8vhGPcNUgA6a0M-W9tkLWUx13ocd4P3aEk9K91mlLOwg8pOqIicX4t77LvlKqcZmtDboSj1Oh4hyY7kmkWQ3JWubjYuF48eQRaU_7S1i_J8vZDys8Cguwbl0hC4AVwDKNi071522QJEP6u16Q2xMFD9v_LjHrAzdKNmPFFF0fNKQcWnnnIl-NnrKGZuBD3i7yQ5-3uDTnY18XzHPEfU9ef1LuMHkJpqqBy5IVxuLBhcGzckLr0jAcUA4ZmDpHOc_mm8zuSb8-csD4Kx9BJ62gyaqrFrpqsoo4qs5qyxyX6p2cWVpBiIoas8LmGgt-7Rp-fKN9wxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی کصکشکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/funhiphop/81706" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u93jUQfmluENzpLcWxtn7ZdSncQK2gN0RdV_UJm0jfnPuB0oGF5aB14I5VSqFdIws4orDxvdBqwaRqDnPL2QIyeKe7EuPkaZTX9_P656aHSNpST6bH0I8Rp2cREPkGOD5Kx-rhNLjmW42DeAko5ggDQ1vLqE2GLPc_o2G9D-PnTfwiI780dSpeytNx52ObG-sXi8WR_hfEWzI0P8KxdKLBSkMbDYgwkhxUJr7pVzMzxXkTpwRscwd5hbEnIWKe5qOPyTHNfmPsDLb018vYAbEGVKZnMUrT73ILId5T-Xq4D18HGwBiAJOn29lQIX_TXw77vpvrfm-G1KFsrcoXic5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید راجب اتفاقای دیروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/funhiphop/81705" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-eSStsaQSucLvWVPNnGcczlGgNs8qzj1BL6VT71xE0n2L6DhgRd1WI5d4kkLdDWNiXxc3xwEV9hg6cgNlUWIrqOOijn57ObHNESI_XJudOX6Nl6vL8oaU0pkgzgF77-bkYhW2NuCpsO0Sb7mHhXlWz4hIPeTjYGbx3rLSsDL7fDS2y_LaTquk18fKtLL36cDW41Z3xoxcUF9ech4J2edoLTG_OUO2M9qvSE8JFkimdVifX_khiEjRTrSa8jyqnU9BYP70b9oUfQUJInMt_XxY4LFHkeaiNKDWmjFAePbrq9gf8tTbt3GSEyRWZb7DXr_ttvFjfxeRoK4VXyVa3ebQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81704" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">حماس خودش خلع سلاح رو قبول کرده امضا کرده، ایران بیانیه داده که نه توطئه در کار است ما نمیزاریم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81703" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIDXt5vqKzr2S1N4PMmv5v_YozqI9qYzk-7hmk4sEP0GYYmfWYjZq_0T6B9W253lMbYPbBlqUo6BQlyREbdPA8WrHrgiGGl3kHCeU-qf4TR3AtPJrYTdRtavfpIgdbdGDdvJfkeztN_XX2fLMxSZmz0FdHajzWV1UqilkVeTkcMZpOQpRm7ejmhKa2796Q2e1lindQWgzbJiEEMwdQLqLjdIQmND7JXHrSTPa5GryOeMJYdl7RYA4EbBr-HO4-Z02bW3GgGm2uf4wmt4iTEoDOI8TcuplVnsB8X-EATTx4rxh1oPG5zG1_OZQ4MPEU-UgKj-38P4IIYwerADo0-_EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی ناموسا ببین کاراتو
نيروي انتظامي تهران بزرگ امروز یه دختر پسره رو توی پارک با گزارشات همسایه دستگیر کردن! حالا میپرسید به چه علت ، چیکار این بدبختا داشتید؟ به این علت که هر روز این دختر پسر میومدن اینجا دختره به پاهاش کیک میمالیده و پسره پاهاشو می‌خورده و فیلم فوت فیتیش ضبط میکردن
همسایه ها هم دیدن و گزارش دادن به ماموران انتظامی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/81702" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81701">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbFoj60JUWeOjz8T-ZPMLp00Ajt7vYy7QDMEIdzYxvg_DIoN-ABIL4JbfzR4ZGyy5KHIUW--N25gmh8hPNEAmV8DVx1vEXvFOIR2CrMvfgRud15dyBM7ulWahyIlzAQr8b1LN6lPsK1-3QWHdpcrn0mrLvpPryvS2Ge5knx44gCfuSE95oHObRge9qov8jSv4KSih3tpHyfIegqG_008KOmvx70vCS5n49ltthB1uJxHf9DXEe3avXNOuKYR9m4MZjHHXCMDFqTgyRDxE7o1ZOfwNqd_bsCjgF8ZUXCcRNk48nGW_fDCaxfonFGnDOXBECI_YFozWToDASjWDrkLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- زنان با قاعدگی بارداری زایمان و یائسگی دست و پنجه نرم میکنند  مردان با چه چیزی؟
+ رونالد ارائوخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81701" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل: علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81699" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل:
علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81698" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI_Fff0gaWFzZZ-HkQpWum2apCQSjKstnQZKbZqySc-MUraoEPyEO8gFzohLd49xejpVNP9QUX8rsXmcGdf3MdIouowAvI1AK5w1_2qNaW7fBT2D2HeE6IXMABRSdpjzCSJARIH-wDaoEEtr1dcRVazTJ-AXB9prjGaioOvAi9B0PGc2KCWDJCJ-ji2fdQnN8oM9CTM3f-cfHc2SFP0Vcra6yNKgkRrrAOFzKGeFCdPGpAVb1OLz9M811YWe431a5sCINov9H-Dfrh8zbs4ChU9NQnHFShFVuP_ywpMmkDQYYp1PjyVFiWNaqSv5-eB9PWh2S4gX1NFa9FmIKjxf-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاس زدناشون
😅
😅
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81697" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81696" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81695" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_yqPUWON-kM_A4OmLV5P-Mgfwou900wlofEvAzgMNfRQ5mI_cxsy1z1fdxKx9xddeu9KhUs4_I9TS5ejEQ0D_7eJ46NN_VDodLtCL7eiM9SLNzjc3zFw2fq285HE-GMQ9p7N6CmCKSCFmDmurOzG9o4SatE97Ter9Yadsis9eH9bhRv8ELePMa6XNuYbjsahK2I0605bH7WKi9mEBM_sy72s8Z5ESni4YiaRvWlgz14RPema-BhD1EhCR-q-wNqt2BPW0oSOPOD7xw3mFknSvdCksm9PpDYV5yhHUlTb6k1VZu3djD9ZAZJwqMWFnel6F3nUolLzeoA7hXS3ryrlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHr4E9J2yV1Rj919vnnw9wMj3QrOv-UMCpdKdxQHo_uYzssOaoz18sVud12DWnDktSpMWMCb13CtpMDpgfmjCJczrvf95vEYvsH15iMd5TgVFaHFF0uPYszwvzaE2_aSYIVfsEJr4yhpIG0Yd-fO3D2CVkW2qfvYWjW2iHsDKsEPjJjJiNkvGp7uUJM9GYYUXMtNom3g2F5HnVXoPYWUmcjRQ9mho8dtgZr-H5I1qeK0zsLhkRzAc-hFG9wGFGRpeS26JU73O7urSIdhsozsJjYoHiIIHDmnOEFecCoSI4UVVQAqhk3KJHvUeq6E6LHqiF8dNsppVbb9bkvO9rGDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81688" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWUcFPXn2VRBV3I2k-s1wWKoZwmi_MXQ2W0DY4krfX3H03eGaKwdXpM3pOQvZp4HJHF4kARlPWC2BK4AaMDyTRV37v0uNXrmXIIZz5f_C9N7tCU9o0o1YitbEFax7j1UXV8JD024g6QeNMdjGfLUMs5cMQN-G0AYMafj_4U3pUC88IzyDad0tS9VA-tGON92yWMc9fl4FoxDBuNmsaSmYgizXy5PArRka3JYS9Ftl7-PV47Ew0o2AQ75j5X0vMFXpoBuqY20uzfQ0U741qGKgUzgVdBzPEhADWkuIOgZs1lGEzL0TYIu_vBkPqAaTrjPvbUtG9nYNgMpe2pBvh6I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81687" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🔴
چین میاد بهترشو میسازه
چین به عنوان بزرگترین خریدار نفت آرامکو، قراره سرمایه گذاری های بیشتری در این شرکت انجام بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81686" target="_blank">📅 15:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4Sbeobv1Sd2XPr9TwaBhEup5FPrtE-MJpbZJJpepF1Kjuq7rNt4rab8q_s-CjvjUydOcR4sngk1GxU2RaEaKUPxjr6gQ86VLuiyPxvHwIxoW5BuMc70YRWR2Aux0qUyV0ZoDclIENr1vNtQdGGM2K0hRitQTEWd6_nu_ZtGWtXZZAgl32JsMTBekiZrSHfY6IwvRb0bSXmwBf3uryaOo3tIWM8J6zCAOL33tJwRV8W9pIbVScQgG1hw5qJqJ980db27SqSFdORccUAuDT0ncrmw15rYG5vkt66vx61svA_X0AwTRlN6QBI2gn5ymlNTrxQ3j1mwdVt3OsKV9B_Q_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگا یکی ترجمه بکنه چی نوشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81685" target="_blank">📅 15:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81684" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81683">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
ببین ما داریم چی میکشیم
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81683" target="_blank">📅 14:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81682">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkXLDsG_wS7WaNr023xzl5cKImRu1Tjf1PdbWMmcScDPMPJ7sRg_NNrtSF41b9NESE8-KrpF81-Q5S9zDT4QsLRfIgSF1rMY9lFBnm51H4mEyI75EH_5c-XnWQLzAI1goL26DzIOsyoy0-bW2zDHB8DO_aLhG0mMMIs6KG_VwdRlcw9Dla3xrZ0Pp7jGAot6NN4WMQooSJxkyS4q9SVuMdzstD-jkm_JwB0ncuE3BzOOUqW2wzsz1Mdeav_dFF_nZrZaBe6F1ge9LDAHknOJzkeYSHPL84sTWboyh5p8564NuRGq03FZB3AF8rfzE2dK3-bNPDMgJoIeJyZrtxa0EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم قسم بخورم کسی پیام بده دارم میگه خب تو پولداری ۵۰۰ بزن کارتم رفیق شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81682" target="_blank">📅 14:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81681">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فارس خبر بازگشایی تنگه هرمز رو تکذیب کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81681" target="_blank">📅 13:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">خاک فرعی مگه داریم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81680" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kymy-gw2nelZTG-QmJhnCSYfYkA5kavBT4j6iEz90zHTXlTrUWt2KGUqrmdqj0ma7ED-zxWSTnplaUv2TEaWF0Sknb0PedkUgHCaPhFjvUxm0kXROhEF6ESYuNTnVvSh9IzYF9On6EiiX6NuBq3PdbKkvrtJa-ka5R3Y5Dr_KwP0lLwjA5k1967bFCfquijpJ9-lQoCDXYmZnXOb5uzrNoU94buC6X1MpKW2G1tAFg2hf6umJwXFUEt9-pnWn8zIwODxMWIl6pvgK-AS5H-FI6Of9UJYR8_FnbWmSPPq1fCXWfqYeJiAioKfMCPmmrVOsbci4l3nshKDUA_Q6irwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gnOI708nFVPT0YEv9vBC_Mf-ZxoRW-9rf59bI01D6l1ISWx1LN_7uS8gYE7vVDc8qc5ec-TXr8kfDyz2RcHx6exb8wwvlim1MZ6Ca3TKNQ-7CS0mlP-ma1nsIxlCPRFGVdLqJp4CciwlKCAXEvjcW6sSnKBughbvQUm5tmzMMs10SzfC2EUoVmKuiNBtO7HMVtnC4JefUJwrK-aUQHQUwB42w9YBlcm-FTk3j1-cG5Xa57JOBAc6JAwzgKoE_7Eln8nKTPcSxWXlM-FzMc7bBnc-LQuJLTQhzUTamcuO4EKl6ZCfRIFsPQKLFM4EO3D06adIE0ApvUq2eVK-BRS8FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسریا کسخل شدن فک میکنن مراکشیا به خاک اصلی اسپانیا حمله کردن
شهری که بهش حمله کردن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81678" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0E4nLfQE64JnFGPvIxVRh1Ru4D9hjrO1gtTFzTRRj4ZKg5M0La4wbyOLq1q7rMcBWeh3yBe8OaJFo7sxdYv8-lqodV49pzSouWn-FRFQHameLgRAe2WMBkXJ3x-dng5MPcwdPFZHW5Cz9VlRofnLwk8ulgjUEpHZDnpsIazLZzDvdMMeAO-rD1R0NuvoWh6wcDsPUXtKyn-UkgcnW0PV1NjC7dxb5ql6gsRr5fEIxieNzfzsN0Jqz1EAaYMsUTgurIoQ7YsqQiuwNDZl_tY6Zp0z-e4i0cc-rejKr2v8-V8Q3FPZfbKMYjYh9BAurqZjZpsObwPf-ESKosCKPjJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81677" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heZNFLX-6LaBWGPAI2jrttvs7xaPlFh0QWuuxMr0Gy28TQ1hUEugT_QBQ3V9LuBqW5wDB7cd-H0WPP3nrJJ66KjdhQXMUI2_UDDSubmbPwgu6-XRxweDByiEE5YtvQeHb3UbcpsTinUvRG42sBpRpOS1-S3gqAMpu8-1YoSWWp7JHVVn3h9RPCkwADJQ9hEvN9XDO-2jcZ65WZqCdBTWptMLAUcHR0Jy8HDqGre26l8pB3nOGB8D4zKcLtigL97zZ4wWqzPy7ZtGMZx7P6H5cp6jiRHZGDs4AiLs-qEfrx_l0le53v3hz3uuXN-ct8B4oYPrnmFKEm_V3eBLUP6ddw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های یامال درباره فان هیپ هاپ:
اگه چنلی بامزه تر از اون پیدا کردید، من ابرو هامو میزنم.
#Arash
@FunHipHop</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81676" target="_blank">📅 13:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9C5j9fNHtJEDKIJtv4Q4e9uJLE2wk6y9mFVEEdrfXVP-dvNnLCpf7yFFf4LWoj7krW7IjeQf94pxRrs0doRLkF-y9HbFU7wzDuWHL_MUb_-hlQzqvTpdojd9NUy3noUNbtDvJt91v_9bNBJWK08xOqOe_iC0ew_UezdiuRCBGnzk8GaImkPIHRH-9H96RyC0zYN1jKjToL8_HOC9fZYdRGsQaeX_FroR0Ep9-hSIWyyjEnkX7nlm2ntIttuUJRE5KmGuPn4ZSp8UuBQUVmWAFpjY8SoWOadaDtwPWQpq4WXFSlbN_d4PLis-rMeSXctIJH_z1usRRHRUbhd7Joepw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ اسفند، چند روز بعد از شروع جنگ، رسانه‌های حکومتی گفتن پدافند ایران یه جنگنده اسرائیلی رو بالای لواسان زده. حتی یه ویدیو هم پخش شد که چند نفر داشتن با خوشحالی «الله‌اکبر» می‌گفتن.
ولی خبرگزاری‌هلی اسرائیلی گفتن ماجرا برعکسه و یه اف-۳۵ اومده یه یاک-۱۳۰ ایرانی رو بالای تهران زده و بعدش هم رسانه‌های داخلی کلاً ساکت شدن و واکنشی نداشتن.
حالا بعداً معلوم شده خلبان یاک-۱۳۰ ایجکت کرده بوده و زنده مونده، یه طبیعت‌گرد به اسم جواد قارایی پیداش کرده و به خاطر همین کارش هم از فرمانده نیروی هوایی لوح تقدیر گرفته.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81675" target="_blank">📅 12:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y0-BgwV86DVyva2e_INbXTkJ7FG4MuUiRMh-tBUduGgm0wZavOc2DZZBkAZzgTobuAsWxrjFjEV5edONob7GZzuS0V-xyAK4hwI0qfHi34JhxotPGcGBelG_zox1XSQV7qtgIrfa2W79UBimQPVKqFyMbgldPbgckgxf1laYiZWnqH9wcBAg3fs-LmXGNwR8yS9oPHLEGX3vpzRLBL7tsLug3SmsSUxln15PXBUJTNNAy_s4VM6gmUxWHCFNFx10VuR2GPCi0vGvphIWGaJNxI5jp4n520q3f6OpzWx9pUdH-nk0X3Y--TAu9p8GxgfsLs607srGVh4LWYAV3zdZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران کیر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81674" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بیشتر از همه دلم برا اونایی که دیشب رفتن بنزین زدن میسوزه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81673" target="_blank">📅 12:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XH8Prce0GmUtrkeZ4r7bmJ2TmxQnD6e1IuWVDPcMV6T4S4XA9SRsfs2y7yYMRMdtIiGTJ0bq_q2Q4D7xi_97LYPcVPp695qluZSnd95aAubrN5l6oep_GrZYyYvZuSmtCtg9_B_2VhHdRAyNKUI0MPBZWNVMUuzmukjpRTID_IyLQ3qfv4CgVAoFJjZPKI79xEwNnZKXWafQNJk-NRtUNF-GHlwmNACcnv4wW_Tg-OyfCchspgumWNHvnJPxa5sPkppoOXZS07s382E7av4jeQXZLNd6-H9xHjj2nUuN-_GN1W47XMuOnVknYaJ6xF7fLVw4c8vu3tHYtG9EpejJSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقبی اردلان این میما واسه سال ۹۷ بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81672" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=gVyjfA2-ac6H4wgaILPPAkGSXUu162axQb7p_sD327JxPnXKdYWWou0JfHeYqPV7h-uiSeIN3XEQtxlrLVTna0RMJPyPqjgBAFR-JTQy3pz7_sz6uu465vwegf13z6FURpgmwXtOekn1F_O0b-TQU2_g6MrDn3Fw5VMrOetRR56QZK8KXUBlF6RlYisY06cs27sPphxAOA_NOGW19WV2S8yo-mvalwi9Tgeac8nYxhY66043Sks9CWZYD7KSGkPk3damNJgiHcVCKa9yOtmYftWor-bbFmL6CF0yNzliTxMawNmwWUySf9EqGqQuwgmU8y9jlr9f0lR62WKyXFJGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=gVyjfA2-ac6H4wgaILPPAkGSXUu162axQb7p_sD327JxPnXKdYWWou0JfHeYqPV7h-uiSeIN3XEQtxlrLVTna0RMJPyPqjgBAFR-JTQy3pz7_sz6uu465vwegf13z6FURpgmwXtOekn1F_O0b-TQU2_g6MrDn3Fw5VMrOetRR56QZK8KXUBlF6RlYisY06cs27sPphxAOA_NOGW19WV2S8yo-mvalwi9Tgeac8nYxhY66043Sks9CWZYD7KSGkPk3damNJgiHcVCKa9yOtmYftWor-bbFmL6CF0yNzliTxMawNmwWUySf9EqGqQuwgmU8y9jlr9f0lR62WKyXFJGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صرفا جهت یادآوری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81671" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81670" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcTgHqlK5wGytXzwOpcjCeuHL4phZnxHzXPA5QI9ssdKO49msKkPC7O1zduTnY5h7CH54DmKKdKjNkhXC_Y_3QkWQcY8Gt-456VwaN9O4iZiUC3atPHUZU1nHhfKHwbVgr0wr9N6semHTUF0h1DalSUrfoP0WmCKYT36KZ0crG2K4e5nHKovsOnRy-bKtvRZZbN6zll733Loinai20aUjR_Zz3JTlzLR1E3p1jrNwT5W1WPVVpZ-J5ktVloJYCH2v4YCHK_AbbmNNZBOR_6yn88g_OjaE7D9K-LsyWb50PfXcyhGIlk5n9n7GMKm-8ldSFe66RjexRv_zIPS3swDpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش یه سینگل میخوای بدی اندازه تریپل آلبوم دریک داری براش مارکتینگ میکنی، بده دیگه گاییدی
پ.ن: کوروش این عکسو با یه تیکه از بیت آهنگ Fiancée پست کرده اینستاش
#اخبار_جنگ_شرمنده_بابت_پست_رپی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81669" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">بخدا اگه این مارکو روبیو رئیس جمهور آمریکا بود الان یه جنگ جهانی رو شاخ دنیا بود</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81668" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81667" target="_blank">📅 09:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81666">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fV7rmZ3GknDU8Mp6Hm4NjNy-KKuhdmTR_yiYTm8QpYgNWH4aLTmVtxiuLvrJcMCyY5uvvDezuDge_4j_jUCJqOkyBg_8idTR1NpnjRq_QZ-KkP3qtQxnsv-BX1UJx8n8xH1AIpYFl71nKpsr7AdI8Te5WgS48BN72McrtWNho0xi5YMb6Sf4-ayzO_IY6yrHae7XOKuvp7BGGjJIKZ1xAkaCKFTWQL5o4asLTRz9K-OgSB5UvJlwEGywECQ4Oq6UPOLAzxLAMh0JOarZyjhrI52N5Z4cTTMFyLWx8y4Pgw3kCh0wgffxpmaaCF2sajt9qbfCeH5mOdY4lmCI0SxGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#معذرت_بابت_پست_رپی
رک بگو میخوای باهاش فیت بدی دیگه این کارا چیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81666" target="_blank">📅 09:29 · 11 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
