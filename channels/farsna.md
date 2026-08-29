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
<img src="https://cdn4.telesco.pe/file/MeKHIglKcyox4uAnvDKeV4tJonoIN6bhol6Gx-kpe4YQho4RMw3vVQ-QMh34CBnVVaEWl6UgiV9ZkF2mdjc_RVZJSL722WhzZ815I2u2GLVoCTezQQBjiK_q2F6kNDAJNVr3wrRgZdeswSpjSm0AIbVl5NBrQzZ5cXPDC68KxMN6Vg40MIew8yaMotZuuC1kbAAyt_0QmU0wg6MJleEin9mffO7MCYMg2BoNEbC-xttzltWTRU74tPf6BeF84pNAW75siPbq8Pejtyx5_gt_j_UqWtWmV8Pz1TZZriCYjGJtLjHptdN9Lr4UtoElbVNJDXwjrN_SSFJjvWdTlzW_Jw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-08 01:20:26</div>
<hr>

<div class="tg-post" id="msg-458950">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icf86FZKqnCYr3CDgzTdkY9gzNLX6xGGWMgEywA2taiY2ShifZPdYflQySZW05r0f3NJ_JMvTqyj9WLxoywJGLwg-YSQvF0J-73RvwazwDhJHtpc_B-rEhac0-Y3VjU_Xwr3easJ8cXuLw7amKDnJr9PFlKyZhv4gg5aAycmqJJNjJeT7ycUh02G6ELbzPBleIKYpV1zbYwGDeb62dZdTZ6CC4aWAMcDn26D_qAXxm9l4M4E4nd1uaqu-Grky52O236a9exL-1MsSilZyzHp9sqQnhPMp8x0PbSs8y2qkUVZ3ld5y4GSulReFPqjwxoTZ5S2IEz07aCfHTh_Lq37KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام خیر محسن چاوشی برای دانش‌آموزان در آستانۀ اول مهر
🔹
محسن چاوشی، هنرمند سرشناس و خیّر کشورمان از راه‌اندازی پویشی تازه‌ برای کمک به دانش‌آموزان نیازمند خبر داد.
🔹
این خوانندۀ محبوب و متعهد، همچون همیشه از مخاطبان خود دعوت کرد در پویش خیرخواهانۀ جدیدی که این‌بار با هدف کمک به دانش‌آموزان نیازمند راه‌اندازی شده، همراهی‌اش کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 350 · <a href="https://t.me/farsna/458950" target="_blank">📅 01:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458949">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhXnoPol1T1363JFzzpiFGYsvMnWuMRRcsZiHuNnhdMa5dmnsC85ojwLLaXwloswwlVjwY3qbix1_MiTcmDJ_xEzpe5NqP_PUbPywu_e0dkiBQhqJL4rEeMrCigg6YpSUlpheRUb0NU1OyMzFbRA-LR_G3NjIHq_BVt_I73jt23aq_MQWIWpmWIo_DvLOkExW4CrgtW-Y1jZMD9fxQ6pYn9FstWupDF-vLX3Vz72vc4J7g67zV3vJnG0WDCXybcU26fw8liNFqoBrvRC_WjlQj_oLNlVANClHn79kO9qlLygmBAOnBnFo2anF8EWyksHk1XR_Usn7jvy8bBq7R3nFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات گوش به حرف آمریکا؛ بازرسی از بانک مصری کلید خورد
🔹
بانک مرکزی امارات فقط ۹ ساعت پس از اقدام آمریکا در تحریم یک بانک مصری، از آغاز بازرسی از فعالیت شعبۀ بانک مصر در این کشور خبر داد.
🔹
وزارت خزانه‌داری آمریکا پیشتر مدعی شده شعبۀ امارات بانک مصر از ژانویه ۲۰۲۴ تا ژوئن ۲۰۲۶ حدود ۱.۸ میلیارد دلار تراکنش برای ۱۰۳ شرکت پردازش کرده که احتمال ارتباط آن‌ها با شبکه‌های مالی ایران وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/farsna/458949" target="_blank">📅 01:03 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458947">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75afd74b23.mp4?token=DDqhCOcg5JYi3tGT6tXkxLqLKklElukb65MI1T6CLPU1d6QqnKtAQVwJIPQay0GqpEHaPouUmT7L0GfInRvs1BVcu0JDULVIjqma4zgrl8SJPgwgUeo6Uu7aGyjkyvVyB4WTBbK0R806AbFIesTJ1IjXhnoVrCzODSKtSXJha1Ij7RoQmlOr3kInJ3Ku-rLZqLBBM-mjvxdNTiQsv8FNu8RbIG521f1YNPJ_6XdBXyR2dfiX5OqrcCujrmaf5Svd_wSD4S25p4gF-J98MXqINdGIm30YZrHjCxSA-n546y1sxI4x0V1vVFKO0J60PbECZRT1Apjc6NNMj08e6Q6euQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75afd74b23.mp4?token=DDqhCOcg5JYi3tGT6tXkxLqLKklElukb65MI1T6CLPU1d6QqnKtAQVwJIPQay0GqpEHaPouUmT7L0GfInRvs1BVcu0JDULVIjqma4zgrl8SJPgwgUeo6Uu7aGyjkyvVyB4WTBbK0R806AbFIesTJ1IjXhnoVrCzODSKtSXJha1Ij7RoQmlOr3kInJ3Ku-rLZqLBBM-mjvxdNTiQsv8FNu8RbIG521f1YNPJ_6XdBXyR2dfiX5OqrcCujrmaf5Svd_wSD4S25p4gF-J98MXqINdGIm30YZrHjCxSA-n546y1sxI4x0V1vVFKO0J60PbECZRT1Apjc6NNMj08e6Q6euQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تظاهرات مردم فرانسه در حمایت از فلسطین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.57K · <a href="https://t.me/farsna/458947" target="_blank">📅 00:54 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458940">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BW1rzkGSRusx7CLSiYeXj1BnoyAqM6Us7ddlKxKbun8q8BnE2VvQdIwyJT6vfn_LEkRzZBMqVEeKbMS8XGzI0ox-gIEU-5hLIxVJaKmXtDq2v0FSrZXZ3FhlPYf6oqS3FDw48TLPem83o_m5aJwLTA54cKaxBBMyn82XcG6-oIZ-yviqwpTUSIUP1krAoWZN88pc95F5tbxubyI_HDaGoOhIrSESmN36PPg6YuI_KT4Btc0mKFrzrpzQjNfHyL8-_p4Wc37fcBWtCujGROyN5b13hlcfqc10fHOkR_s_hv95NcBqMGLUnETa_5NApx7ljGavYCQ5pfUd53RXcPrf7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmWed-rwICcBetJUI1VJumDsb50lG2RZOiWGMdcNF0KSMmhcq1lg-4we2B3FwAwJaC4zXRByS-8AEdCNIJjiAxBAgkNECjMjFMAiBazsNsquPoBG4Vl4w1Fg0VRTUod8XaNaH36sofcbZnEuGwqBKVWnDghzlHEJNWDyhGBIDrwAeZS_4jxFrB4Y_QBG76Wv0hXzNFqYzOgENslkHB91QkwOUSlOsPkFGRxd2U8r-lvGxmftsHLw_BiLW6nKn6XL0-1rU4tDnjxsVjWwKCMyOrPLw81iTYzz4sJyFiDOFMv-mzoyQEMhWUD_S3T_J-sL-8U18t_zOVW45i2JZhAtrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkbwjFfpBxuDOu_ZHD2QhM6si_kHGxx5T16XTS4DHVNQZ-9t-AqE18SQ2799O9ZB-vXFsJtot0rsQpNhuQisj95ei7VeGCLIrx7vCZ9afTuZLQLYrr1Tt69rzzUD5jeDfYoRxaAC9G1GStbWhdYi7S5r_TT_X8ZLZ6Vd52fApjm4AH8qcyr9cmnicF_uqRANVkVrHnQqF5d1V3PkiD4GyiktTeV3PjMuZO4VBxUAhnJPjPhGY5Bhp2P5bj4NAkOp3Ab7wcdlcvZCc2qaLwFa0NIEVzXXvUfy6Bx9_c1Fhret4ahXZfVTaptOAwGS4VOkgiC9C5h2-onDpaJ6mEKtJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AKmL1Qgj_km3NnXDLlc4tKBIoWvhrlGreveG6LrmaxLPveyLi4D6baRJNZfMkJzUERsjDUT1tXQOz0uMcBoAcCMVJyEx4g7bby5WKysZFTaR9BD4RE2EKH4ykuSj8e0ykPPSRfYtziLV1M0-6KJ9nA4RGSSvTJh0PdgUJ9dlmk-DiMwF9v85ThM711q73rVpbqBe7vECZBtVVFXJcHg7AqAyrs6eJY0A_iUPo0q7bpeWvO0d1yODciBgiQ7NLKV-XvuBIjdFfX6rjFgJVwHLx4cAAKHdRAUPIA1lM-gSyTSYyOUxkFq8HTHCj8AEPeKpO7cDOe44Yg663YxS69gs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0kfD1U3YbyqgqfXKFaajnpIdUBkvJhNv_uu9BUmRP9SiyKjTPr290KUgGIdWVrsA8MDLIg7Ye9XegAO3mHmElP8MA3ONzr6nbvZNb-pjZbl0XnA2wDFKHZKT2Jw7CRfm9bVpuCz5ykt4MADexDOSNLIIRk1O69tsaInP6Z1tIWj9S8RiVvIg0HNCq_0CoKRZS97Oh5D7dOd9pllCq5ix9BKTepLHQV0L4iP9N3XtUKGuk6vR1wQYDuaeiDaYHLvC98uanNQtq3aXzqTJTsAAx8th6mPdwyIq-TnAB9mSJMQNeKP3e-jgyt64F4Jeq3KdNRGHSNeDmxsDNafSpzoBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo-TEvHj2v66o9Up6K-BNFpb1k_ObbDTaL6FkpuvevBvrmjicgK9g3MRarWNrKLK1sud9O9y80uiBsUx8nwyupoOxFt4sGRMNezkfrbhUPXJH0gzXLLIwAGEkXEdeyLaJ32ymCpe5kWqbCw66y6eocZpyYXIkqz-ZDtYVGn03Dza3cVBydv51VKxLFmMEYbqVe2vqVX0ymNetNUMJY6g1bP8dhG8RLQSvtsfUeWAs8hvG1SD1a5pD7YKldWZMM_Di6yXhnjgBn61tqu2iMa_FdodKXsCpYFGypPlFU3AIYCcxZJIZ4z4q_b_mRRPs8EbEqnXhKupipDMK2MSSUjMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCxRQCmo13Cp9-Ps07ZMFtSIRRyJnr43bvoPgUSwUE1qJJOtVIkGTSIPU7Jn5npgSr-xn9krIjMcgrhpxDsn6ZjKFZwGC-OhNQtc7gQuZqicFAXa-NrNNIqj1oXDxRXUtZdPwBSg6IYGUrI4E1NYpDwpIFHvHk6F9rCSMTpuaQswvs6FfWsEaplKBWbgeaAOqLDS-XOf4IpEtgMEnPy4qFxdp9kSSqxeuOWYe3EkkJBRPdgpElPgjAx_rmUk_OaR-Y-aVaMxtvwBv4Vl4NVKw-f-rXbAyPaMAJWqWFQxumSNfovF70hiuRbQsHUqwbAYmPFx_QBejvdrLkvanP7PLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جشن میلاد رسول خوبی‌ها در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 2.91K · <a href="https://t.me/farsna/458940" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458939">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">استارت عجیب تیم امید برای طلای بازی‌های آسیایی با ۲ بازیکن
🔹
اردوی تیم ملی فوتبال امید ایران برای حضور در بازی‌های آسیایی ۲۰۲۶ آیچی–ناگویا، امشب در هتل المپیک آغاز شد. پیش از شروع اردو، با توجه به مخالفت برخی باشگاه‌ها و تداخل برنامه‌های لیگ برتر و لیگ نخبگان، پیش‌بینی می‌شد اردوی تیم امید با تعداد محدودی از بازیکنان آغاز شود.
🔹
با این حال، طبق پیگیری‌های انجام‌شده، از میان ۲۳ بازیکنی که حسین عبدی در فهرست نفرات اعزامی به ژاپن قرار داده، تاکنون تنها ۲ بازیکن خود را به کادر فنی معرفی کرده‌اند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/farsna/458939" target="_blank">📅 00:32 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458938">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9ytZMWbiIg3or42k8Dsen0A06wb1AeRKPZ2nPCt62V8pCD-RlPU9qQhugRDu7zXCTWavXhW2scK7hMBRTUtneV32A-DVHikZhGWdSr9MfYZZAB-xOsNcoc7Bjm8-NA9TsknkR-7AKMjjN1m3ZyjSnLUgBaMx3hrtnmlDznxC3bhNCiaVDHljWK2PbJBbFHLzxGJlH8wI-AvZ-eCwqp1DKQBnQ-yyG0VUCIogqE7tneSFsDBfdce54cZss__f7zxp5yDJhzo8-cNrRMdaGX0b0ugmWMAf8WIfKY7ozUraKjW8VIch3d6Ifx_PiC9fXYbLgOmkH5PUtCqWA-vhERxaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: طرح مقابله با نفوذ بیگانگان به فعالیت علمی ضربه می‌زند
🔹
معاون اول رئیس‌جمهور: تصویب این طرح برای فعالیت علمی کشور زیان‌بار است و می‌تواند استادان را نسبت به تعامل با دانشگاه‌های معتبر جهان نگران کند.
🔹
فکر و ذهن استاد و دانشمند باید بر پژوهش متمرکز…</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/farsna/458938" target="_blank">📅 00:19 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458937">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPNJ8-k6wdF4lEb_RydGu8Uvd6n_VxvKLb-Ki3xOXWPB2ay2KWGeEEjeKizwnhGbIMbY4itm3NRNmNP7B9qBtaHosTYH12q7aGv3HPMxJgACFmW9P-V_er6kxsh9L6K0NBfXVwaVlaoYaE5Uf1OKmnTiUQO2ucc0wc1H2r4pI5D7g6yAkIoE0kzh8lql5HvQeg5bG578i_OA8QA4SPv7ntJGZqltX-L4OkD4gQsyabybzydftOKQ7MmnGe8Fbd8qwHBQTuRzvClNm3xglY_sGDI0c7fBoYNk8pQlHHfto01_yVfwTsF7Vp-LgyRo4UCLpv7VNoF2sXGoRSbDUmV9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پزشکیان: نرخ سوم بنزین بیش از ۱۰ هزار تومان نخواهد بود
🔹
زمان اجرای این طرح هنوز مشخص نیست.  @Farsna</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/farsna/458937" target="_blank">📅 00:01 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458936">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c721af0cdc.mp4?token=hgJzSnKAWHJkQN6FnQXqMFac7sb2CdoODKEitAtEt_KBb1IY53zKaoomYJheWB2VQbS3HB0V08V23kiGoLLcmzqp_Nw0Z9y16S86AFugWKHqzrt_196-XFChBWynF21iN_5Kfpn_S0_esxrhup8iGsfYTcmIYgoF1vh5qdHJuF6KUx-Tc9mesfVrvYoyBBtHDQ0PCmp98HnOiUlJzPbrFJJ7gtXV3aZ4dlkhO4Tty-JkxlavhdNtWjRhd4fJUGYtxNZ8xDURhD6UljJGjl4vZFM6VehYVh2Jlmz5n5VBpkWZRv89j-9aqOLYXESsBzeOCH2sZNEFnYYJGHhwh0YqRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c721af0cdc.mp4?token=hgJzSnKAWHJkQN6FnQXqMFac7sb2CdoODKEitAtEt_KBb1IY53zKaoomYJheWB2VQbS3HB0V08V23kiGoLLcmzqp_Nw0Z9y16S86AFugWKHqzrt_196-XFChBWynF21iN_5Kfpn_S0_esxrhup8iGsfYTcmIYgoF1vh5qdHJuF6KUx-Tc9mesfVrvYoyBBtHDQ0PCmp98HnOiUlJzPbrFJJ7gtXV3aZ4dlkhO4Tty-JkxlavhdNtWjRhd4fJUGYtxNZ8xDURhD6UljJGjl4vZFM6VehYVh2Jlmz5n5VBpkWZRv89j-9aqOLYXESsBzeOCH2sZNEFnYYJGHhwh0YqRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر هوایی از آسمان نورانی تبریز در شب ولادت پیامبر(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/farsna/458936" target="_blank">📅 23:57 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458935">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c526c62f2.mp4?token=eyGXwG_TNAh3KM8tOl4a8XoXnnjkO8FDlwuo377rFR2Cta5VsRHPOHFicYOYDnP3U8pU2gCJwa2aToCctNOqTPecvwq1zZNaQY9aqarlpFeZ0fTQ7fqzVtOSbgOWTJ5efB7pOEL1Fx9vv-5K94Xh66X_5LwqEi5e89RnxfRtv6lnpkzzSRAci5rBZeO62RS07KhEuJWSRC_mldDJJrULoqNOPOlMiVvXGn-oXKyOOAQFgLGo1y463qWcSv3h8RPvGqcVnunOKyxczSRemSbySDoODvW7t1QV-Cx70VN83IJOk_0HJEmK_kpEccqxSuNo0-5yWiVflo2_7DFKhc27ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c526c62f2.mp4?token=eyGXwG_TNAh3KM8tOl4a8XoXnnjkO8FDlwuo377rFR2Cta5VsRHPOHFicYOYDnP3U8pU2gCJwa2aToCctNOqTPecvwq1zZNaQY9aqarlpFeZ0fTQ7fqzVtOSbgOWTJ5efB7pOEL1Fx9vv-5K94Xh66X_5LwqEi5e89RnxfRtv6lnpkzzSRAci5rBZeO62RS07KhEuJWSRC_mldDJJrULoqNOPOlMiVvXGn-oXKyOOAQFgLGo1y463qWcSv3h8RPvGqcVnunOKyxczSRemSbySDoODvW7t1QV-Cx70VN83IJOk_0HJEmK_kpEccqxSuNo0-5yWiVflo2_7DFKhc27ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجلی وحدت شیعه و اهل‌سنت در جشن مردم شهرستان قلعه‌گنج استان کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/farsna/458935" target="_blank">📅 23:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458934">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15212f3f87.mp4?token=Aw3fiuNz-o0HVERx_JSuC8EamWm8hc6MsgBHEAhwhs3_DLfZTgcRBN4Loci19J36CJE3W935etEKAN1FtXmzUVeDC5XbD_UudzwVVuLKvUILWVl9xFzRIbmGFcPTIcWajWPXgmWXdZkdPTexwtvFJcKt5ebNiBFPndPo-3bE_vhWANSlb1VVl8v4BVHyteBxl_ThiE942HC-DahGWP9iLewupu22iB-X5ApMoo844-PZlkUaavDvIwneh5v2o-0SPSoumm3R6O5yJqDJJL45fy_UL9-svZxBvIPxTDnHqUkW5iNeqF08wnRbgzrCLvC-_u8GS8YZgk0eC4nCZLdkMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15212f3f87.mp4?token=Aw3fiuNz-o0HVERx_JSuC8EamWm8hc6MsgBHEAhwhs3_DLfZTgcRBN4Loci19J36CJE3W935etEKAN1FtXmzUVeDC5XbD_UudzwVVuLKvUILWVl9xFzRIbmGFcPTIcWajWPXgmWXdZkdPTexwtvFJcKt5ebNiBFPndPo-3bE_vhWANSlb1VVl8v4BVHyteBxl_ThiE942HC-DahGWP9iLewupu22iB-X5ApMoo844-PZlkUaavDvIwneh5v2o-0SPSoumm3R6O5yJqDJJL45fy_UL9-svZxBvIPxTDnHqUkW5iNeqF08wnRbgzrCLvC-_u8GS8YZgk0eC4nCZLdkMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جشن بزرگ امت احمد فردا در تهران برگزار می‌شود
🔹
این مراسم از ساعت ۱۶ تا ۲۰ و در مسیر میدان هفت‌تیر تا میدان ولی‌عصر(عج) برگزار خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/458934" target="_blank">📅 23:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458933">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1beb11f27.mp4?token=h0fKyxG-kvAQAza9Ub50tUy_IhQReLFIGRHohUzmFpw5Yrhb4cnCER97bVxHN8PfPwV3-FVmtBsH45WxdVDFX2n6Wq5rvViDjNF8oM_vl4mGuSYvlgNViiGj2dQbAqQqGta03LNcmkdGDqh6xqq8SWcBDnzCVIXbaxIUQDq5fTMwbLbu9f51bpw8qtuDK4rWdrJmn8k8SzLwnYdOLzvsjtlkcobiIfi9wAbgeupsHddiwFO391soFpt6Rlr2oK7faFtIG-QCxJ-LbeptaQxJkjCW7qLGT6s2NiIGh2e24_D5xTau7ZTw1XQ2lrRMfPQ87Cw4CXVRF21cySpLl1uBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1beb11f27.mp4?token=h0fKyxG-kvAQAza9Ub50tUy_IhQReLFIGRHohUzmFpw5Yrhb4cnCER97bVxHN8PfPwV3-FVmtBsH45WxdVDFX2n6Wq5rvViDjNF8oM_vl4mGuSYvlgNViiGj2dQbAqQqGta03LNcmkdGDqh6xqq8SWcBDnzCVIXbaxIUQDq5fTMwbLbu9f51bpw8qtuDK4rWdrJmn8k8SzLwnYdOLzvsjtlkcobiIfi9wAbgeupsHddiwFO391soFpt6Rlr2oK7faFtIG-QCxJ-LbeptaQxJkjCW7qLGT6s2NiIGh2e24_D5xTau7ZTw1XQ2lrRMfPQ87Cw4CXVRF21cySpLl1uBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: در زمان شهادت شهیدان رجایی و باهنر، من نیز در همان ساختمان حضور داشتم که ترکش‌های انفجار نیز به محل جلسه ما هم رسید و من به واقعه نزدیک بودم  @Farsna</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farsna/458933" target="_blank">📅 23:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458932">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c781c42238.mp4?token=UC09mSFA4urI-AbdUe4F48Nd0PVfnTOOn0dJSVBqpn0UFbB8-Ue_LOa290-K0AmN56kZC9Kk9ZyUXsOu4bLID-_6FJ8qxGhOmFs8TAp5Np0iAYGzwRUcV5224Y-wYqORXl7XsfMBRSLlWoG7-amAgDvucAm3XwTyrwKS8_O12ZXdEYm69saZ17CzRNn9MXYXqi95pCe5a_3TXMMn_CVk-NHNt42Ek7cQVmsXQEnYB_BPySDMtNF4ONttja1gR-C0iwRkXjxHPbWt3jui50r_r7BDy6-k_INMXzd8oMUV3lIyR_wq7SafOnZ76FWCX47l6Bubj6uHLBX8ZdxwnYYLZR2GHyHTE42_xeMEyRiVXOHdvIM0B5egG5MRFA3qBA2isRZ7kre-S6agW2js9mNpJphwM636EKwE-pSD0AiJKQWcYwHmOXIFsgPZnzTSM3RBsN0fJwXIj5SHWWLr4YZiNCQMN6Bpya2zIS_kbopPMFtkWx2cbYeGIAjF9dSHMcWNhvK9OxsjqkQAL2dZuVRAApddaLK3F8U6chEyGmk05CXAFaQqy-LFWwxk_6wubsnNGh2I61qHpzIQCBED5XaC_mjKi3boU-9r3C2n8sF9-p2WfKBjP4kt2IkZ6AN53XocurPJtHmJ2UbSdgstWFaL6g1LtAU9-CBnVSE-_2OOp3I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c781c42238.mp4?token=UC09mSFA4urI-AbdUe4F48Nd0PVfnTOOn0dJSVBqpn0UFbB8-Ue_LOa290-K0AmN56kZC9Kk9ZyUXsOu4bLID-_6FJ8qxGhOmFs8TAp5Np0iAYGzwRUcV5224Y-wYqORXl7XsfMBRSLlWoG7-amAgDvucAm3XwTyrwKS8_O12ZXdEYm69saZ17CzRNn9MXYXqi95pCe5a_3TXMMn_CVk-NHNt42Ek7cQVmsXQEnYB_BPySDMtNF4ONttja1gR-C0iwRkXjxHPbWt3jui50r_r7BDy6-k_INMXzd8oMUV3lIyR_wq7SafOnZ76FWCX47l6Bubj6uHLBX8ZdxwnYYLZR2GHyHTE42_xeMEyRiVXOHdvIM0B5egG5MRFA3qBA2isRZ7kre-S6agW2js9mNpJphwM636EKwE-pSD0AiJKQWcYwHmOXIFsgPZnzTSM3RBsN0fJwXIj5SHWWLr4YZiNCQMN6Bpya2zIS_kbopPMFtkWx2cbYeGIAjF9dSHMcWNhvK9OxsjqkQAL2dZuVRAApddaLK3F8U6chEyGmk05CXAFaQqy-LFWwxk_6wubsnNGh2I61qHpzIQCBED5XaC_mjKi3boU-9r3C2n8sF9-p2WfKBjP4kt2IkZ6AN53XocurPJtHmJ2UbSdgstWFaL6g1LtAU9-CBnVSE-_2OOp3I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنزین کدملی در تله دلار
🔹
محمدحسن صبوری، کارشناس اقتصادی در گفت‌وگو با خبرنگار اقتصادی خبرگزاری فارس، درباره طرح اخیر رئیس سازمان بهینه‌سازی و مدیریت راهبردی مصرف انرژی درباره اختصاص بنزین به هر کد ملی به جای خودرو، گفت: اگر قرار باشد بنزین مازاد خانوارها در یک بازار عرضه شود، قیمت بنزین در آن بازار تحت تأثیر دو متغیر اصلی یعنی قیمت جهانی بنزین و نرخ ارز قرار خواهد گرفت.
🔹
این کارشناس اقتصادی افزود: قیمت جهانی بنزین متغیری است که اساساً در اختیار و مدیریت ما نیست. از سوی دیگر، نرخ ارز نیز در شرایط فعلی کشور متغیری نیست که توانسته باشیم آن را به شکل پایدار مدیریت کنیم.
🔹
وی با تأکید بر اینکه اجرای این طرح در شرایط کنونی به‌هیچ‌وجه به صلاح نیست، تصریح کرد: اگرچه این سیاست در شرایط پایدار می‌تواند کارآمد باشد، اما در وضعیت فعلی اجرای آن را توصیه نمی‌کنم.
@Farseconomy
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/458932" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458931">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17429cccc6.mp4?token=jy-94LZ4ZFAYyOZhKnYjhph7GBDzUeo8Tsc_QZuc1iY02OXrZxDZEqZYX-93M-Lo7_lKbGZjFutDVDEUDBOHXW54kJkgNpLOBFgREmkpO8OXvPdG12NsA-OhukAGTaICH4yiY4UrqeAYnsSaZya_MkQJR0x2ZlavNxdnUHp7mFV4PqFQxk0rzIHzU929pt6Ti4g7nFDPiqxwA3e3oRBCR7o8_NWi8RB4VST1s6WBlKjzjhcR1IJvMQMBwjdUHF7Km0w4tlmcuXitUXvPuHkJefl6FA7P2WNN_TnOuh044mSMeNDj5g7SqEEOLzqK0YnOoaew0dBaV48oBhGwocwfSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17429cccc6.mp4?token=jy-94LZ4ZFAYyOZhKnYjhph7GBDzUeo8Tsc_QZuc1iY02OXrZxDZEqZYX-93M-Lo7_lKbGZjFutDVDEUDBOHXW54kJkgNpLOBFgREmkpO8OXvPdG12NsA-OhukAGTaICH4yiY4UrqeAYnsSaZya_MkQJR0x2ZlavNxdnUHp7mFV4PqFQxk0rzIHzU929pt6Ti4g7nFDPiqxwA3e3oRBCR7o8_NWi8RB4VST1s6WBlKjzjhcR1IJvMQMBwjdUHF7Km0w4tlmcuXitUXvPuHkJefl6FA7P2WNN_TnOuh044mSMeNDj5g7SqEEOLzqK0YnOoaew0dBaV48oBhGwocwfSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
طنین وحدت و حماسه در مسیر گلزار شهدای کرمان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/458931" target="_blank">📅 23:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458930">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سهمیه‌های دهک‌محور؛ گام بعدی اصلاح کنکور
🔹
«نوجوانی که در خانواده‌ای کم‌برخوردار بزرگ می‌شود، اگر امیدی به رسیدن به دانشگاه نداشته باشد، مسیر پیشرفت را زودتر رها می‌کند»؛ این موضوعی است که دبیر ستاد تعلیم و تربیت شورای‌عالی انقلاب فرهنگی آن را یکی از چالش‌های…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/458930" target="_blank">📅 23:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458929">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82a48bd9a.mp4?token=ObpaK8oTsB2Zy6CM0Jl14QiMq4Y_qP7B_sIP1eXLclRuOR-MgUKXI89JqClPM5zZ4kfd5iP_HCy7vwIJaqa0XIEKdOmTJjC6l_J54o2v5hOgujPX2qP8q78s7gZ8bWI-HKtfZQwEh5XNwhfUA71DwaqlzCV0GEAF7_85Hfk-m7TKcegdVhOcMZcjFLTHbq3AR2ZeqKR7t0Jw05z7IhbCHcNsu8wlUm2_0X6wbSx3pDjqE8IV6DOfePo2DnfUjr3DPfXLIgqRNs1UeClLlZ2d-P2cdrTikl7XgKZ-QUkNnGrQYZG1Njj3-ZLC1ixUrtfqbOUbUmZz4mW63F7cvEsaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82a48bd9a.mp4?token=ObpaK8oTsB2Zy6CM0Jl14QiMq4Y_qP7B_sIP1eXLclRuOR-MgUKXI89JqClPM5zZ4kfd5iP_HCy7vwIJaqa0XIEKdOmTJjC6l_J54o2v5hOgujPX2qP8q78s7gZ8bWI-HKtfZQwEh5XNwhfUA71DwaqlzCV0GEAF7_85Hfk-m7TKcegdVhOcMZcjFLTHbq3AR2ZeqKR7t0Jw05z7IhbCHcNsu8wlUm2_0X6wbSx3pDjqE8IV6DOfePo2DnfUjr3DPfXLIgqRNs1UeClLlZ2d-P2cdrTikl7XgKZ-QUkNnGrQYZG1Njj3-ZLC1ixUrtfqbOUbUmZz4mW63F7cvEsaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حدادعادل: در زمان شهادت شهیدان رجایی و باهنر، من نیز در همان ساختمان حضور داشتم که ترکش‌های انفجار نیز به محل جلسه ما هم رسید و من به واقعه نزدیک بودم
@Farsna</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farsna/458929" target="_blank">📅 23:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458928">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e58c2255d.mp4?token=PEmnguKUdlYPhYfOjQthJKfElCfuUa4rjR61UmIrEa0t-RZBPIHBxzihCMOPGQcsrmrR-O5pnXBPNdKf2HJwExAl0JJetU9M4vRoOFAPGU_-anBDYM4YvhSFuuRzLbuqcwCcCMp0-96zz9vItlqTMtm7B0eTMhyBxppLLB_3Qz_AvB3SIJcbwSlvKfMSoQcryawLl3RFNcc-hG8uO4-mfr4Bx2v62ZZ1VvWMDXgO7femVCVrItzR24oSBIdKcVa3qZLBB9Zt4Xr6oAPxh4vRT5LWZbal16616VbDzgtUo0j8jd5b1b7hNW5XqVLWPbItvhjk4wIZkRoPYGlxMxwZyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e58c2255d.mp4?token=PEmnguKUdlYPhYfOjQthJKfElCfuUa4rjR61UmIrEa0t-RZBPIHBxzihCMOPGQcsrmrR-O5pnXBPNdKf2HJwExAl0JJetU9M4vRoOFAPGU_-anBDYM4YvhSFuuRzLbuqcwCcCMp0-96zz9vItlqTMtm7B0eTMhyBxppLLB_3Qz_AvB3SIJcbwSlvKfMSoQcryawLl3RFNcc-hG8uO4-mfr4Bx2v62ZZ1VvWMDXgO7femVCVrItzR24oSBIdKcVa3qZLBB9Zt4Xr6oAPxh4vRT5LWZbal16616VbDzgtUo0j8jd5b1b7hNW5XqVLWPbItvhjk4wIZkRoPYGlxMxwZyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نورافشانی آسمان شهرقدس در شب میلاد نبی اکرم(ص)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/458928" target="_blank">📅 23:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW0ST3JZnzMi9dGj-74skx8AqfCtKqUGhZNY2hBgaZMFlpBBxzGlatutKYT_meQJJU9tf2wUzr9WmlQ9DzgLD0nI15oSbLQ58GeOpuvd0jm1E5oLlphyYfj68pa95EqyO4DbbZUthnBFv0N_VUMwe7B6NVhIb2DAPNiKdU1yLfXu70Oxa03kfnsC1Qa87Sf1wYwIXiMdUAo9blmWI_e3ejZMUiPSFCKOB2XA_ibRtfK43fjH1hUgwcQoJkQ7NrenBazi3y0S_qVyju0Uk5Fx1hgOtDnKJDiNzOxUzXwrdX1Nu6eQo68AZPiEybnQJS0yT9tH1rnOZRpMuunZRdKE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات صهیونیست‌ها به انبارهای دارویی غزه
🔹
در حملهٔ پهپادی امروز اسرائیل به انبار دارویی بیمارستان «شهداء الاقصی» در شهر دیرالبلح واقع در مرکز نوار غزه ۳ فلسطینی مجروح شدند.
🔹
در همین ارتباط، مدیر بیمارستان شهداء الاقصی از جامعه بین‌المللی خواست تا برای توقف حملات اشغالگران به مراکز درمانی در غزه مداخله کند.
🔹
اشغالگران صهیونیست طی روزهای گذشته هم انبارهای دارویی این بیمارستان را هدف قرار داده بودند.
🔹
کمبود دارو به‌ ویژه اقلام مورد نیاز، افراد مبتلا به بیماری‌های مزمن همچنین داروهای کودکان و زنان باردار را تحت تأثیر قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/farsna/458927" target="_blank">📅 23:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b633bfd29.mp4?token=N7xVG9QX-9pFm5GldAOGn0xRec9tJW4_PsUE7WmwLPPdxnK_V6qaCRWko4c5g8EmPPUWqQ1tZHlROYg3LcrZMzs1OoThTsEa_-oqnnJ0g34FDvpmHYso2wH4Ra3YHY6AvpykAJqzgTcb8cmYw_wJ-x4Bfxxqs5ALS8lc9Svr4ru6foXTa3s0JD_P5ecNDGJ-ov6NBtVuqw3IFm0xkArxCPwsqWBTXnuEWOnjKNQRPOJ0i--tKLsdOnrX8mJDdrRdqn5_L7ff_ooKoCPfggDyLgJzUb_3x6aPqVZRWLzpFysGlvCAXDklX74ZwqBicurufO3ETD5GmFAOLCMNfdOv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b633bfd29.mp4?token=N7xVG9QX-9pFm5GldAOGn0xRec9tJW4_PsUE7WmwLPPdxnK_V6qaCRWko4c5g8EmPPUWqQ1tZHlROYg3LcrZMzs1OoThTsEa_-oqnnJ0g34FDvpmHYso2wH4Ra3YHY6AvpykAJqzgTcb8cmYw_wJ-x4Bfxxqs5ALS8lc9Svr4ru6foXTa3s0JD_P5ecNDGJ-ov6NBtVuqw3IFm0xkArxCPwsqWBTXnuEWOnjKNQRPOJ0i--tKLsdOnrX8mJDdrRdqn5_L7ff_ooKoCPfggDyLgJzUb_3x6aPqVZRWLzpFysGlvCAXDklX74ZwqBicurufO3ETD5GmFAOLCMNfdOv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیرعامل شرکت نفت: یک بانک ایرانی حساب شرکت نفت را بست
🔹
با وجود پیگیری‌های انجام‌شده، این حساب تاکنون باز نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/farsna/458926" target="_blank">📅 23:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6pzhJ7ghALiMs1EDBkpB9WhFYDxSZpU8sRMnYwTxpulNlb6vkparZOUKgXjFcf5feLg-aQHafUtQT_QTh-YAmy7Ffq4sO_fCPRcNs5-xxQ6J_q8xf0FkXIp6J05vM98D_zvecIdVyUfx9K3Qpm59zRpkBeaI28zNjo0bhCMQMeCdUci6daUNIMhPB-_TroUdp3RiozUYcooXo1wkk7gj6wh5IE2Cp4C5q-rJBjMLCs59dDTtIQTjI66FpVvkco0asAlfK0cnlGy7q231iEwf9P8Vbw3XbAJI0so9VIiG7zg8AQ_R11mjbseVAiutO20DU0cO8LuNGOj6uioqKk7Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فرمانده کل سپاه درپی قهرمانی والیبالیست‌های نوجوان ایران
🔹
سردار وحیدی: نوجوانان قهرمان تیم ملی والیبال؛ سلام و آفرین بر شما که با حماسه آفرینی خود عزم و اراده پولادین یک ملت عزتمند را در عرصه جهانی به نمایش گذاشتید و با غیرت و تلاش خستگی‌ناپذیر در اوج جنگ روانی دشمن بار دیگر "ما می‌توانیم" را تفسیر کردید.
🔹
درود بر شما و همه دست‌اندرکاران متعهد و فداکاری که شما را برای این درخشش امیدبخش پشتیبانی کردند.
🔹
در شب ولادت نورانی پیامبر اعظم(ص) دل ملت را شاد کردید. همیشه موفق و دلشاد باشید.
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/458925" target="_blank">📅 23:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🎥
مراسم جشن «نسل نبوی» در گرمسار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/458924" target="_blank">📅 23:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458921">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OxwPY4szMc5_Pedzvkg5zRVSxNezKaqxW0k6B2UKWi79eBA-RxL0_1MPEkBHO6xrgCcRx41tC3Qc--REhe1J5u6pSeCDMWDQkufzW7H2WdTB5_pLA5FDycJsPI4RlLGE5dFUMx4kz1ylvb80IdT9KxY-pPWMK81DLEzVqeR6yxup5i7B0BQ6wz2J23wIQQEpU0A7eOv9nNwYgRUxdiPNgZOe7ltZfwISjPT2zvdh99KEwE_UdE39axrrq0YpRhv3Hoab-o5IDQ6-WBn8CyysyyMDJGKchOhp4rT3jXZksYMBx9cwtWH_483oWBbAPfCY5XV5xQpc3hzB_qGsa139DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X67A7kPhglXc1AW2ysqo6PKdjiawiIQTZT7a28KJtfK0pl4Z7jPOZ1JlNhHCQm67a3ui86vNnhnBpWOxq6ACapljw85LAoa3Wm6Hx9MY2acQD7q15L6E3-i2qsq_seasLHLYa28GrP6QGP01RoGKZyANfrjbdxTLLv4xh-CY_iZ16_NlLbezJM18lSsFGGC1dKQP-PX2ua7YMmbIySaxtI6Evi8PE2AlSDWrxRIqrJ5nsMH4zYWNG8jICPI1qYZEdSVs0_bjy7BdfVlzxffvZKIdlK6xRS4_o_nYJdNPngyL8YvsTZ5NX-hePrXhxyDdHzr3m1hbnethRM11tEcvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p6AVV2Xkrzv1R0NFAVQFV6D8tpkhA2m3cRyk5LmJsl7blyBgon3_ytSWbfLIPc0IACsroCViCEgQ08K_MTQI1CcyNJQMJXYCEDks9DvJ4G5vIE1WdExPFTx7TsuS86RTnsqz62VRaXoD8N5SCyfdm-rHNB6WbF9wyt0YXZg984tRbm0zVpL4uDfSgknADG6bA2PTP-g2e0Q2PvlK8C2wra85Zpgl1fmFjCVbYaMUboX8dQItN9LsaNfcaDiaejwlbGRS4VI89p3a06uAIexak8fXMMsyzRyy2NHSoz66mDwnI7rhzE38rjIK7ckoI6yXSIc5eC3uqU1Ar3doKKoaKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گرامیداشت مدافعان آسمان ایران به‌مناسبت روز پدافند هوایی در میدان خانی‌آبادنو تهران  @Farsna</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/farsna/458921" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458920">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
اجتماع و شادی بروجردی‌ها در شب میلاد پیامبر(ص)
‌
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/farsna/458920" target="_blank">📅 22:58 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458919">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه‌های لبنانی گزارش دادند که ارتش رژیم صهیونیستی با بمب‌های ممنوعهٔ فسفری ارتفاعات راهبردی علی الطاهر که مشرف به شهر النبطیه است را هدف قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/458919" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458918">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">غریب‌آبادی: ما با عمان بر سر ترتیبات عبور از تنگهٔ هرمز تفاهم کرده‌ایم اما تا زمانی‌که آمریکا به تعهداتش عمل نکند، تنگه باز نخواهد شد
🔹
ما همچنان به اقدامات خودمان برای دفاع ادامه خواهیم داد و برای هر سناریویی آماده‌ایم‌. @Farsna</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/458918" target="_blank">📅 22:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458917">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">غریب‌آبادی: ما با عمان بر سر ترتیبات عبور از تنگهٔ هرمز تفاهم کرده‌ایم اما تا زمانی‌که آمریکا به تعهداتش عمل نکند، تنگه باز نخواهد شد
🔹
ما همچنان به اقدامات خودمان برای دفاع ادامه خواهیم داد و برای هر سناریویی آماده‌ایم‌.
@Farsna</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/farsna/458917" target="_blank">📅 22:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458916">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZZG_raXaTJAGg-hwH-V1QChZ0d1g1LrTCYmmEv6L2P9CD4Nj6YCj4X8zXx4Nz4takwl_XsTmNUxuk02RRNtUb3fLOUF47YWVbEZiEL-JMH-mzAroiMsoIy-Hqh39DXyQDOb-eOnV0ORumMIizon1v9gr9iIsHHqy19mZoPmUtNUtZHNQx7UEpoutd9r8l0HZ8Vw_6rV4VJFmicax7wGs7HkaDhoiCa-L5AnXs_zDJNFuFMDOz8fAqWXruZyYiEag-A5oCfPw7k6f_XmYZB03906y7XGQFSrzd816rD3ib322JhsgVzaQzZanFTqC_zazJbayUPSBenZa7pqZ8oNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدۀ عراق دربارۀ اخراج گروه‌های تروریستی ضدایرانی
🔹
مشاور امنیت ملی عراق با تأکید بر اینکه ایران خواستار اخراج گروههای تروریستی تجزیه‌طلب از خاک عراق است گفت: حضور نیروهای حزب کارگران کردستان (پ‌ک‌ک) در خاک عراق غیرقانونی است.
🔹
الاعرجی به صورت ضمنی متعهد به اخراج گروههای تروریستی حاضر در اراضی عراق شد و گفت: ما مصمم هستیم پرونده‌هایی را که به عراق و کشورهای همسایه آسیب می‌رساند، ببندیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/farsna/458916" target="_blank">📅 22:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458914">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab6c09b21b.mp4?token=Ls6FYKMois6yHJ0gmYg5QAVw0_0r1QGnV7W8Y46QMvZnaK2rF7PspebQxiUzetT2sxqpwnDP3S1LJlu-Oaj2aPi_pJjy2NXHgamsWCxIPwDnPLPnscBrCNP5QcEgFFHWOGuewFA2H-6S-rjSx49IM1rwx6ZLFyYxmyYIGhupE3nW0F8gqsUwZRHwsnMjFV4hLcSKXFFM_NvKE_PJfMVVpz7dnyezfOHhNz4z0UzPaErGOM_LIIDmWpC5McToWi5Ui6Dl25N2-qPRk3SzNiaVo0zz_RS9DCD1-_7OX9LprQ_8YmgSnSbhqV9XYPbd2_X0HRAS1ucrL27xhwTlb-YqHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab6c09b21b.mp4?token=Ls6FYKMois6yHJ0gmYg5QAVw0_0r1QGnV7W8Y46QMvZnaK2rF7PspebQxiUzetT2sxqpwnDP3S1LJlu-Oaj2aPi_pJjy2NXHgamsWCxIPwDnPLPnscBrCNP5QcEgFFHWOGuewFA2H-6S-rjSx49IM1rwx6ZLFyYxmyYIGhupE3nW0F8gqsUwZRHwsnMjFV4hLcSKXFFM_NvKE_PJfMVVpz7dnyezfOHhNz4z0UzPaErGOM_LIIDmWpC5McToWi5Ui6Dl25N2-qPRk3SzNiaVo0zz_RS9DCD1-_7OX9LprQ_8YmgSnSbhqV9XYPbd2_X0HRAS1ucrL27xhwTlb-YqHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: ایران در شرایط سخت جنگی، برای اولین بار در تولید گوشت مرغ خودکفا شده است و به سمت صادرات آن در حرکت هستیم  @Farsna</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/farsna/458914" target="_blank">📅 22:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mv0NS7xfsLVLIdVDsmb_LCkDFwKWtB9OCKyXkJa-JZ4L0dYmUmbZqONfDiJJo8e7VhAdD5mLWnelQiOJjzJTHkqd4TVKzJIVDTlzXHyfVwC9OLfdHjaADtNOCPSqYAdDzzcMLar6WVijHcGTw7N0exeE98KmJ7wWgADr0DMFSsBea4LNOvYFDUdw3gt4Zwh4GATnSaHdUO1Lz86hzwEDO0KErtb8jbr-AkxmCZVSOaZXaW3Ydru5rOHSSj7gdb4wRG1nI_II_QZfm85BZH_F6c8khkaNcCv0VDHZrNWjEkYKm6QNMCdVMue_1BKTn9xDnbYRGG9bZcA_dqyvLlfbqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hCHPyn_bazPG-gb08Z2K1sIOuoVQBcxNMfw7LvjbKC_eCTLMas9mI1D99-bhxehgFiNaKwsK-L9cIAlmSQlG5I_8tAd5Nbe0CHgFlOhiKSkdEz9-Pnibo_l2oQhTK8uILoazL5a1HnDQwpPgOf79jUR0NJUUbMU6gEcGoobUBH1bXiJvP5_jV8OOh0T_8xBYm_-mweJzURkEu9GZaCBkuQUTGyfPJCf-x2IHPMXzIg1OXBIGCHQEat_kmlzlmIIHyuaT4ZWYGhLqhYt1AFje0RjHMZORyCjAJ8GXqiu-lwY6i-ku02KkOoMN7FBeJ1juKkrX4oQaXaN15XYotKZVgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jFoxPrZfhYc0LEsXT1XBPv-kHqAVKQVbVFHpdZ4-5eHc0W_36EDjxXSUh6nOSTAyj1iMArynFEX5nw0lYtN9mesfP7eBFj3HccL633zcECzQeIxAPAwEG7WpE67YAfr-I3lKrA850STw_gq0Hi4L9tOnS50e5_u2GruKhjrYi-4Z52o4S7jR879Gi_R_uvHXLNBshL8plFhXJybickkKn8Jw7x4oD17M6Fh8yyy5G02q75gCrpJI768N6hTSbgQiwa07Zg2wrquuW3nQFDC2N6719ZOcRBlRqzyP_HVBQ-AYrCYUMQSSWZ8wAC1Gd1OJfc6UheZvsgNhwGynic7LmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TvKPR6QNuwfwfZqu-ZfUiK1aMKdgjftACt4OEM-R7MILmD-1-x7GTGHeEBFqSs-XAEmEv1PeLpaQeL7lHuMVjT1TEZxCxKop7HGIyUSLGY_ApaXwJtYdRjFWHilf4JJKz0ddM14Q_JZHP4NOIFMstVdbjUxn5ymiD-QWEF6FZYcQc44-Gm8kQ25R02CeUhX3b4DZSJ5Cn2YM-N15gKnz51B9RD7U-NyJwtovXFBQAun18C9jOde8ykeQwsHtosqNwYPWhucfN7WXIyPXGQ6RRidsMPJIC9OhJZTYnIW2KU8MZ_Pol0ZQeHPMgmvrJmB1RlaKUTDaLCe4qva4VHobkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CpZ1RWDl7kbXYr7T_EZAaAV8dj4Xt1HlxwfRS0NjGWDbP3ufMa1bwVwdrdzAO5LrsIxV3rxgR3bUfZanhqe-BoJK7rYwACHjAvh2Jg1RUkk5jRCUkK3X9zGFhBw-Q8-e_q3rqNDv4DOGPq7eEiA2jGhi6saRe2anLpifs2N_NR5S4t4Bu0c85ZlAPpjw9ETn8raMo6UPxHTkRKlpc1cvn8T3w5sbv3OjfoPLMshRew4t8PvnYK-hWMTvIMqO_VfDQqqLBY6ZOJiBlmJwfWUMbubMB8ChKw6jaR6Y_tHkg0A9bBrbxsL0elq8cTCFY5fCou26sGZuArSDJuX320_TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R4FZMHs5LCNe8as3wEeSTdTU9B_FpWFY_-VlguUL_PgciPG-d33NHh2gX037ciKsmZ-Is6cuEAdXX5Y1CiMzKlY06Oq4Xk460nu7ebRyhCWLAIaoEiXPxzcg_ChLfEIluFgDhFvylvj_WvAdpp0HGsllC4oWPmrT2n7lubkRmq8TT1RetqS1iulDqAhd9jt8PAn2OOwtdhte0zoQz7ClCgGV0Dzeg1GcNGzPD7lUf7C8HIbqZHsI9watPXzqopCTdJeCgbjRfo2v4Wt3bw0b8ujfgjQ0hrG7d7u-iR7CR_A0LbbV9fLYbbBuGRUvqd4PyOQrN_8nQwtq3lrGkQ02ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ipb714laypeFMj-kHzZ3bMo14MaGYtKqA2Jz1lkpfoBa4ksQ2iCwbyRKyXMNYaWusJlNq58lRoKnxI1faRBGk8msC1SRCndhemdP2POUXxUpT47iipqwrjXj999E63zh1_grMJpCWJ-pMhpKCAS7Jpsfdw3sgjjWQiopCpwj4SlAUl37BO6lTZKNfVcVGXHfpqMTg6G0f6OkYYDy-DBD0Af0JpzvEwNJG3zdad8TgYUMo_85InBRkYBk71prwGUtNk2FD-5WVcQYNv_wVR7sK-xlVtTp8ULOl716xP3K6tYMHuAD7640fNQcnzpNtfCgVX5l0PWNepbu5qkN_PM8Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حرم رضوی در شب میلاد پیامبر رحمت(ص)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/farsna/458907" target="_blank">📅 22:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c311d7f88.mp4?token=cIdLavmo-Ei46ooATt3DGCjo2Xc_WU7nCDqO7gGzQv0_4eeZi15vop3jhG4n4SoPGpLS6VK3vGRRaswcSUqsLPB9c2G3ZYephRViHTaoljxsrovncMor-20bisGHXZQoQAmOswZxwbP7GwL0KrD961mJNJTwTsW7XCnDt7bUgBNddSN98TkbijEuzvMoioxa3Nm_rd6nnTHfNouxJcv9c_MUZVer_NeaC2MbuIg0_AI8KhNv3J1_hLFWW4iW3t-4Uate-m5fPSMEzNWYnkRTHQyWOmGiE0lfLoLktRRE3xYB6qAfS7MVTNpedFEk_GJvwZAoOFH3a2dFCugXmrdCBzrQ3F2aMucdCk_zEyQEjJZE4dQidT4rQpEfbyr92aWeQVMGeibZ4tZv2PIR7A22QKCTMatGdF-ELhP6Di1Lqak6hfMPOvWQYP6b56XwWBljqRIkruNou1Mq5jNKMMkH0_Gb7eQGJUZMpN-W-y1dasitUIlhhcdChkRPkkV7qYZFuqtEWyV1uCNwyTgZ4FxppqZlTWLAgTl2u7zaAE5piEANUWYKFgsOJmDdEornrFLmvkyB3Cv8vuRtLD2FMZ6I8ybSXsNpT5l8VNoEuj0aQQ1I2C8mvrSD0MD5dcs79yOyRLunNoKU1W58N1MLU11TO5eXK7SbisIUUc5Nd4yJTZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c311d7f88.mp4?token=cIdLavmo-Ei46ooATt3DGCjo2Xc_WU7nCDqO7gGzQv0_4eeZi15vop3jhG4n4SoPGpLS6VK3vGRRaswcSUqsLPB9c2G3ZYephRViHTaoljxsrovncMor-20bisGHXZQoQAmOswZxwbP7GwL0KrD961mJNJTwTsW7XCnDt7bUgBNddSN98TkbijEuzvMoioxa3Nm_rd6nnTHfNouxJcv9c_MUZVer_NeaC2MbuIg0_AI8KhNv3J1_hLFWW4iW3t-4Uate-m5fPSMEzNWYnkRTHQyWOmGiE0lfLoLktRRE3xYB6qAfS7MVTNpedFEk_GJvwZAoOFH3a2dFCugXmrdCBzrQ3F2aMucdCk_zEyQEjJZE4dQidT4rQpEfbyr92aWeQVMGeibZ4tZv2PIR7A22QKCTMatGdF-ELhP6Di1Lqak6hfMPOvWQYP6b56XwWBljqRIkruNou1Mq5jNKMMkH0_Gb7eQGJUZMpN-W-y1dasitUIlhhcdChkRPkkV7qYZFuqtEWyV1uCNwyTgZ4FxppqZlTWLAgTl2u7zaAE5piEANUWYKFgsOJmDdEornrFLmvkyB3Cv8vuRtLD2FMZ6I8ybSXsNpT5l8VNoEuj0aQQ1I2C8mvrSD0MD5dcs79yOyRLunNoKU1W58N1MLU11TO5eXK7SbisIUUc5Nd4yJTZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گرامیداشت مدافعان آسمان ایران به‌مناسبت روز پدافند هوایی در میدان خانی‌آبادنو تهران
@Farsna</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/farsna/458906" target="_blank">📅 22:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔹
خواهش می‌کنیم پیگیر پرداخت مطالبات گندم‌کاران خوزستان و ... باشید. والله ما هم جزو این کشوریم. یک مقدار پول داده‌اند و مابقی را معلوم نیست کی پرداخت می‌کنند. تمام رفته‌ایم زیر قرض. ما خانواده داریم و گیر و گرفتاری داریم.
🔹
ما پارسال در تاریخ ۱۴۰۴/۴/۲۳ خودروی ساینا ثبت‌نام کردیم. هنوز دعوتنامه نیامده و بلاتکلیف هستیم. شرکت سایپا ماشین‌هایی را که ثبت‌نام کرده‌اند نمی‌دهد، اما ثبت‌نام جدید انجام می‌دهد.
🔹
به مسئولان بگید فکری به حال قیمت پوشک بکنن. کدوم خانواده می‌تونه پوشک ۸۰۰ هزار تومانی بخره.
🔹
هر سال در زمان بازگشایی مدارس و ایام امتحانات، مدام در رادیو و تلویزیون و رسانه‌ها اعلام می‌کنند که دریافت مبالغ از والدین ممنوع است. از سوی دیگر، مدیران مدارس طلب جلب مشارکت از خانواده‌ها را دارند.
🔹
ای کاش می‌آمدید یک گزارش از وضعیت بنزین استان کرمان تهیه می‌کردید. کار و زندگی مردم با این طرح جمع‌آوری کارت آزاد جایگاه مختل شده است. اگر کار کسی جوری است که باید مدام با ماشین شخصی بین شهرستان‌ها و بانک‌ها جابه‌جا شود؛ باید چه کار کند با این بنزین سهمیه‌ای؟
🔹
ما جمعی از مستطیعان جا‌مانده حج تمتع ۱۴۰۵ به‌خاطر شرایط جنگی هستیم. حج و زیارت با پیش‌پرداخت ۲۰۰ میلیون تومانی ما ارز ۷۵ هزار تومانی تهیه کرد و مبالغ بیشتری هم دریافت نمود، اما فقط اصل پول را برگرداند. حالا می‌خواهد هزینه سفر امسال را با قیمت روز حساب کند، در حالی که ارز خریداری‌شده از پول ما خرج نشده است. این موضوع حق‌الناس است. لطفاً به مسئولین حج و زیارت منعکس کنید تا از تضییع حقوق جا‌مانده‌گان جلوگیری شود.
🔹
اخیرا با تمهیدات دولت مبنی بر قطع برق در ساعات مختلف شبانه‌روزی در زمان قطع برق شبانه در روستاهای شمال کشور پدیده دزدی کنتور برق شدت پیدا کرده و این موضوع موجب نگرانی‌های زیادی شده. لطفا به اطلاع مراجع مربوطه برسانید.
🔹
لطفاً در خصوص عدم تعلق سهمیه سوخت به خودروی‌های پایین تر از مدل1385 پیگیری کنید. مگر مردم پول دارند که در این اوضاع بد اقتصادی ماشین خوب بخرند.
🔹
قضیه سگ‌های ولگرد برای اهالی رودهن معضل شده. نه امنیت داریم و نه آسایش. با شهرداری هم چندین‌بار تماس گرفتیم اما هیچ‌کاری انجام نمی‌دهند. فقط چند شماره تلفن می‌دهند و می‌گویند با این‌ها صحبت کنید. آن‌ها هم می‌آیند یکی‌دو تا را می‌گیرند و با دریافت مبالغی از افراد مثلاً دوستدار حیوانات، مجدداً یکی‌دوتا کوچه پایین‌تر رها می‌کنند.
🔹
ما کارمندان ادغامی از مؤسسه اعتباری نور هستیم که ۳ سال پیش در بانک ملی ادغام شدیم. متأسفانه سلیقه‌ای عمل می‌کنند و هنوز قرارداد با بعضی از ما انجام نشده است. خواهشاً اگر ممکن است کمک کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/458905" target="_blank">📅 22:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c71c8928f7.mp4?token=PQ-FBoH2UeFUnBtZnzJeUGmq7C6w0UgFtefva0J8SZiOf-Dw80OsqpyQvjY5m-iCcrnIbDV6J0Jb50sd9WWegm0ZBW7TNVaefRFI1LKfhuKyUKFlbI5n3daSX62LQi3SnWhnRDppKr7Ooi_uc5wwCzfNshLtXvWa2zEsiJtUxbyn70w2Q4T492d1UYDxlT5u8LAa-0Ck7x9lNnS4bkvkQtp5SdxfC2q8a3APaFwFPm0qNoTvUpGS4LYTgTIqPWgSaHNgJJz693HSpDzRibOy7G0VnF32_xckSZjD4HUlM3zU2I2_CxyZwgDhYIPuq9OG3abc61JE4qXPuJ9BhWs0HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c71c8928f7.mp4?token=PQ-FBoH2UeFUnBtZnzJeUGmq7C6w0UgFtefva0J8SZiOf-Dw80OsqpyQvjY5m-iCcrnIbDV6J0Jb50sd9WWegm0ZBW7TNVaefRFI1LKfhuKyUKFlbI5n3daSX62LQi3SnWhnRDppKr7Ooi_uc5wwCzfNshLtXvWa2zEsiJtUxbyn70w2Q4T492d1UYDxlT5u8LAa-0Ck7x9lNnS4bkvkQtp5SdxfC2q8a3APaFwFPm0qNoTvUpGS4LYTgTIqPWgSaHNgJJz693HSpDzRibOy7G0VnF32_xckSZjD4HUlM3zU2I2_CxyZwgDhYIPuq9OG3abc61JE4qXPuJ9BhWs0HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: ایران در شرایط سخت جنگی، برای اولین بار در تولید گوشت مرغ خودکفا شده است و به سمت صادرات آن در حرکت هستیم
@Farsna</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/farsna/458904" target="_blank">📅 22:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4efb3f48aa.mp4?token=mn_ZNou-m6s51LO7zbngTbYvR6nsdB6ymekuSchKpCvK_CG_HkuED9xYd_NEXzrXIGhE0XLCafRTRwJr0d5ybkbuSiMCOLi9xFNx2y7vXwKZxX39sIXAuX-sWilQZq6U0WinQc0W6EQjHds510lWdWhjy52kQ9UCWT3zOp_w-XJSnyHbcDOZhtXgc01FT2XI7ENYNQcfVuxiIoCyEvh4kAU3fGVO9CR5f09I96rEbTZHE_0kldfXWoIcw5Ep-DYK_bRPfkVxFU3-jiY6vyfoiI4WI7FL5ayiw2qCRMiwjRdp1jctgjxVZAQZduqhfmEWyShN5yipLXgmGDNSDMA1NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4efb3f48aa.mp4?token=mn_ZNou-m6s51LO7zbngTbYvR6nsdB6ymekuSchKpCvK_CG_HkuED9xYd_NEXzrXIGhE0XLCafRTRwJr0d5ybkbuSiMCOLi9xFNx2y7vXwKZxX39sIXAuX-sWilQZq6U0WinQc0W6EQjHds510lWdWhjy52kQ9UCWT3zOp_w-XJSnyHbcDOZhtXgc01FT2XI7ENYNQcfVuxiIoCyEvh4kAU3fGVO9CR5f09I96rEbTZHE_0kldfXWoIcw5Ep-DYK_bRPfkVxFU3-jiY6vyfoiI4WI7FL5ayiw2qCRMiwjRdp1jctgjxVZAQZduqhfmEWyShN5yipLXgmGDNSDMA1NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پایان زندگی هرکس مرگ اوست، جز مرد حق که مرگ وی آغاز دفتر است
◾️
دست‌نوشتۀ سپهبد موسوی فرمانده شهید ستاد کل نیروهای مسلح
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/farsna/458903" target="_blank">📅 22:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c3d1962e1.mp4?token=l4rH2V3Q1x_ORCNaDLaEEPm6f0Pw2ey7eOPCbKlmUwIBrKGRw2aBrlzSOib9fFVVkr-YQKAF6XAFwcoP-ugMz5CmKu7Klj36UDn9fBVYksulmxIcRHocUYLQ29mhk3Y27tKWugTOZ3PRk_iWCuVkcUL0cLP4xt1x2177HwDswPrdK7_9HIihPL8wEfXk2g8KRndWjW3Cvli0-aKhBMgaj7DHjdNPlYs8NWLH4OdbqyPlwNt17WbrY7gIbawXQuQUzpoYrHwfIOqOIhSBd_dK3TCocMAFW_MQJeNTZPVxqXJkQyZBW-jU8pCOZkJNH_pKs3iGk3bv9-nYAC2fg-7cFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c3d1962e1.mp4?token=l4rH2V3Q1x_ORCNaDLaEEPm6f0Pw2ey7eOPCbKlmUwIBrKGRw2aBrlzSOib9fFVVkr-YQKAF6XAFwcoP-ugMz5CmKu7Klj36UDn9fBVYksulmxIcRHocUYLQ29mhk3Y27tKWugTOZ3PRk_iWCuVkcUL0cLP4xt1x2177HwDswPrdK7_9HIihPL8wEfXk2g8KRndWjW3Cvli0-aKhBMgaj7DHjdNPlYs8NWLH4OdbqyPlwNt17WbrY7gIbawXQuQUzpoYrHwfIOqOIhSBd_dK3TCocMAFW_MQJeNTZPVxqXJkQyZBW-jU8pCOZkJNH_pKs3iGk3bv9-nYAC2fg-7cFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ و یک شکست دیگر؛ نارضایتی گستردهٔ آمریکایی‌ها از جنگ با ایران
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/458902" target="_blank">📅 22:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b904696a4.mp4?token=q2ks5gEhMYfFfTZCTmd6aWY6ZuXNEAYxhFyoA2AjjulGB0ojzoVqPdFdCd6rzaQlmSACl73SuPl0akDL__RPQlgK3-BUwod1rp3PINjbcTGYXpz4MqkYK1FiH54BCI749L0ujuVz9YU52Ebz4uG0UdhQ15-inUB7d6jZWUJIZKLeLsRXJisZcBjhD8ft6YJILYGIpNgkPlnmrZAtnsA0qCjfMk_4yzaf-izFIOYfjN-EcfJj3Vd9-9AmePAy2YqAUlP9-yYtYVjyNmLsBGi0MhmDRk78Wij-_2SDbaVI79_jK4Kve7Al88X_p-eWSyQ2RvQsoRslHhQPhxFe1V4HcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b904696a4.mp4?token=q2ks5gEhMYfFfTZCTmd6aWY6ZuXNEAYxhFyoA2AjjulGB0ojzoVqPdFdCd6rzaQlmSACl73SuPl0akDL__RPQlgK3-BUwod1rp3PINjbcTGYXpz4MqkYK1FiH54BCI749L0ujuVz9YU52Ebz4uG0UdhQ15-inUB7d6jZWUJIZKLeLsRXJisZcBjhD8ft6YJILYGIpNgkPlnmrZAtnsA0qCjfMk_4yzaf-izFIOYfjN-EcfJj3Vd9-9AmePAy2YqAUlP9-yYtYVjyNmLsBGi0MhmDRk78Wij-_2SDbaVI79_jK4Kve7Al88X_p-eWSyQ2RvQsoRslHhQPhxFe1V4HcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لبیک ملت مبعوث در شب ۱۸۲ ایستادگی: در میدان می‌مانیم
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/458901" target="_blank">📅 21:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLSrx6YbmQ7KFuTa9ud8L06g3Adlb8kRSFug__UeV3DnTEKkPQeCX7igKB8cBg2Y4MvihhnBdradljbNfz88-U9MbYkhikn3W1GkbZFEasU5s8H3O6uzQU1289K-JtCPoBnRivgmcZV7cje_f3MKCrdf2pPmMXg0saJQ0ZLBHdqRSKWL-y6wPlPJFl7uFTfqANJl_YYlNo8hUsj7GvhsKdhnVoR9wJsRrHxesrYBhtbl3KHcd_XpHSPWUiS6dZ3DYwzLvp50CGlS4uVOJyQrMNyd2KOi1cEhnOo44VSCU_b1_2nPWxIQqcj3fq0sOKzmpwgea3rjHN4RN-LMx5ezsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیام رهبر انقلاب اسلامی به مناسبت هفته وحدت صبح فردا مصادف با میلاد باسعادت پیامبر اکرم(ص) و امام صادق(ع) هم زمان با قرائت در اختتامیه کنفرانس بین‌المللی وحدت اسلامی، منتشر خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/458900" target="_blank">📅 21:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/716e739fd3.mp4?token=mrJQnYLaPzR_zfdid76F5gWn9V_8sGgyQS0iIfKdN_Hw6CBIQnJfZpKq-BLxSMmA5uL2jJQtPBJ5Er71ETf0ZFhALB_vLNZoMdplfkOobTx8wwmv3FdQHqBZ7_6woZZm2icmEIW9GPt15DFjXE0oaV-lArvAx2d6emNtAh5Kh5D_Mf_urdziyvFwWonRlLM-nusX9ei2YtXfGFh5nC21umogj3B3qttp0CZoW8MMpf2Jlm6FVl-EOak3sP1j-JlUx-I-Xp-NyUJG4CFnAdw8BLByuz68wipxDRyxanEFFspzkGzNkpIhNV-4reoCE0R-3uWtgqfUwYn52ep4KX6q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/716e739fd3.mp4?token=mrJQnYLaPzR_zfdid76F5gWn9V_8sGgyQS0iIfKdN_Hw6CBIQnJfZpKq-BLxSMmA5uL2jJQtPBJ5Er71ETf0ZFhALB_vLNZoMdplfkOobTx8wwmv3FdQHqBZ7_6woZZm2icmEIW9GPt15DFjXE0oaV-lArvAx2d6emNtAh5Kh5D_Mf_urdziyvFwWonRlLM-nusX9ei2YtXfGFh5nC21umogj3B3qttp0CZoW8MMpf2Jlm6FVl-EOak3sP1j-JlUx-I-Xp-NyUJG4CFnAdw8BLByuz68wipxDRyxanEFFspzkGzNkpIhNV-4reoCE0R-3uWtgqfUwYn52ep4KX6q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز فصل برداشت برنج در شمال کشور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/458899" target="_blank">📅 21:48 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzdhrbZFIEig8hvjVX2LFg1DO1p7P8NWZ-K_qm8E60iF3_2HL25nOVblocK4ZKfrUXqJh9-3t9-KdOUmzvj5aSZ9w0L0q_EIjRgZazob2x5oz0n8JPq8Bfw0m9-nEvVtmHgdvcGBBZBqc5gfS8WKF9tjtR7jv8rsVIRWY1D8_iTYlrGFhsg2qSTxmt9ie-VjrxJ4p8rx9IKSc-E6I_WXokfobO8KJAG5kIQsabxO3FR1-Yy__unzJlSPEkDaG41aybEdnhP7s-ROm-k1PR0kJyKjV-lN3TdlG17gPMyhgNw3XaN-vBRl5cqUBPFFVXlLQOt04kzdCwEinRIXt5lshg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس به یک قدمی استقلال رسید
🔹
جدول لیگ‌برتر ایران پس از پایان هفته چهارم
📊
نتایج:
پرسپولیس ۳ - ۰ ملوان
مس شهربابک ۰ - ۰ صنعت نفت
فجر ۰ - ۰ ذوب‌آهن
@Sportfars</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/farsna/458898" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca23eb794a.mp4?token=NvSWmM0aOseRGKYwpsSiIM5yGy5aBKZE50jpi71AjwKeJHRnjMffTzVvzFkDAJxtGHiBSR_ciBvnZQE8lQTVX40o2VgbvEDKR0R9EPqNMeYQ_3ZcF7kFcVXq9G6ip2kK-iw12JxZBf1y28kBPBn0Q18knDaNk3LDspLBzB7lTQRcoQD0e24f4cuKkd7y8RQxXUchbaJaT3dXlbqTntT8fWNJXdEf6V4LGD-sdBmnTdUM-A9cHh5twy0oHSHAsmUoERwBkEaElwTDmJg2FezfJh40CPTtFyr0FCZCPsO4ZGNxjijFJ5XAEEkdBPUuxendzvBC1YTM48K5ccungU714A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca23eb794a.mp4?token=NvSWmM0aOseRGKYwpsSiIM5yGy5aBKZE50jpi71AjwKeJHRnjMffTzVvzFkDAJxtGHiBSR_ciBvnZQE8lQTVX40o2VgbvEDKR0R9EPqNMeYQ_3ZcF7kFcVXq9G6ip2kK-iw12JxZBf1y28kBPBn0Q18knDaNk3LDspLBzB7lTQRcoQD0e24f4cuKkd7y8RQxXUchbaJaT3dXlbqTntT8fWNJXdEf6V4LGD-sdBmnTdUM-A9cHh5twy0oHSHAsmUoERwBkEaElwTDmJg2FezfJh40CPTtFyr0FCZCPsO4ZGNxjijFJ5XAEEkdBPUuxendzvBC1YTM48K5ccungU714A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
لحظاتی از دیدار سال گذشته رئیس‌جمهور و هیئت وزیران با رهبر شهید انقلاب به‌مناسب هفتۀ دولت
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/458897" target="_blank">📅 21:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b831417567.mp4?token=c4rhpqh3bsgMW_jkT0SlvGVa_hRa1UX-7_hDvsVFksKtOSZOdDuUdizQBV3qfOYdXyXu1CNzsnI9Ezt4I1ED0OdcC5D_r0Z3Q-hpxeyPxBCRxp2c4TKpzDpRc_8w0aZ7E008zHBHUQ-zuhf6KLLmMSDAOzaMcDVSvu11AhOqbMGXscAGx3OKokZyOVF34lpdzUNztV-kihszr4H-p5tDvEqg6qE6H-8hsc6YdLccAtwBj4jNia0iR8LdxT81oviFPGJLjamP--j6IIlXv2rgCseIncffnrpqcw4xbKWqhzsi6lwFD01BoN_bsuwwuipnRm6w-qUpMg9744HIzEm8Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b831417567.mp4?token=c4rhpqh3bsgMW_jkT0SlvGVa_hRa1UX-7_hDvsVFksKtOSZOdDuUdizQBV3qfOYdXyXu1CNzsnI9Ezt4I1ED0OdcC5D_r0Z3Q-hpxeyPxBCRxp2c4TKpzDpRc_8w0aZ7E008zHBHUQ-zuhf6KLLmMSDAOzaMcDVSvu11AhOqbMGXscAGx3OKokZyOVF34lpdzUNztV-kihszr4H-p5tDvEqg6qE6H-8hsc6YdLccAtwBj4jNia0iR8LdxT81oviFPGJLjamP--j6IIlXv2rgCseIncffnrpqcw4xbKWqhzsi6lwFD01BoN_bsuwwuipnRm6w-qUpMg9744HIzEm8Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبر دولت برای متقاضیان زمین در طرح جوانی جمعیت
@Farsna</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/458896" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYAN-LqbsuHDxRfBBT3SdSBHtDnf_lpAkVu0LawWVRJRIcyvfMG5pPW3pbJLku0rMefmwKxHm-9aRz3zByyFcW9Dui7zcosbSca1GVpPyRaggtXyPWxj9lIuNijsBDi6ijSCKt_gdDUZLv5fLMg0wfdYoynPNmaJL3ySJXFnrDDsaTyWeA6M3fBslAr282m7xBeCQ4zA7WdtBa7qlroz8i-avvzi7MH51AgLOv7AKsKuSszRZJrgT_cGNMwIOvxbb6qgU2yRAyR3dAK4gIii0daTFH6RNycfh9-PJREVir-MdYnM6gq1Ihvy0152XGYN3wZT2zYKjFr-FA7ZXvTbjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گفت‌وگو با حسام حبیب‌الله، معاون فناوری اطلاعات بانک شهر، درباره راه‌اندازی ردبانک، رقابت بانک‌ها بر سر تجربه مشتری و چشم‌انداز پنج‌ساله این پلتفرم
ردبانک می‌تواند یک بانک بزرگ شود
وقوع جنگ، افزایش حملات سایبری، دشوارتر شدن تأمین تجهیزات، محدودیت‌های ناشی از تحریم و تشدید رقابت برای جذب و نگهداشت نیروهای متخصص، بانک‌ها را در موقعیتی قرار داده است که باید هم‌زمان دو مأموریت دشوار را پیش ببرند: حفظ پایداری خدمات موجود و ایجاد تحول در محصولات و تجربه مشتری. به روایت حسام حبیب‌الله، بانک شهر نیز در سال ۱۴۰۴ در همین مسیر حرکت کرده است.
حبیب‌الله تأکید می‌کند رقابت اصلی بانک‌ها دیگر بر سر نرخ سود نیست و آینده از آنِ بانک‌هایی است که بتوانند تجربه‌ای ساده‌تر، مطلوب‌تر و شخصی‌سازی‌شده‌تر برای مشتریان خود ایجاد کنند. حبیب‌الله همچنین معتقد است ردبانک می‌تواند در پنج سال آینده، در صورت همراهی رگولاتور، از یک نئوبانک موفق فراتر برود و به یک بانک بزرگ تبدیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/458895" target="_blank">📅 21:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گام بزرگ ارس در مسیر توسعه | مروری بر پروژه‌های افتتاح‌شده
همزمان با هفته دولت پروژه های مهم زیرساختی، ورزشی، فرهنگی، عمرانی و صنعتی در منطقه آزاد ارس باحضور دبیر شورایعالی مناطق آزاد کشور و استاندار آذربایجان شرقی به بهره برداری رسید.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/farsna/458894" target="_blank">📅 21:23 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/farsna/458893" target="_blank">📅 21:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d55a12eff.mp4?token=Jlso29q3IyCX4PcKzVPFxCakLu6Y6h0fll4cMf-44tlCytIzPtGEkEBQmXdV8LCfYu50ywhsutJQYvpdmi2mOg6kvux2Xw0vimX7a3k1tpEWHX3I-3TFZGvUquPoZtK2XB1kHklmgAcLfzQZobFMs2OkNLiGhrvfCp2-jzm4JthaGmbng6kut7-4iexRukOdvYorgmMAl4ebkt1QjKiYWQfA_wNwfAi83SUmcI4aum3sulOdVzWOI-73DACX0rUi06ehmOXhbD3cTRrk7l8X1YZVwbb4TDG2j52oHuqwn03Jgv4pjpG16Px3aZKHCCRkYxNFYgfJnRMW2aH0Q4ta1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d55a12eff.mp4?token=Jlso29q3IyCX4PcKzVPFxCakLu6Y6h0fll4cMf-44tlCytIzPtGEkEBQmXdV8LCfYu50ywhsutJQYvpdmi2mOg6kvux2Xw0vimX7a3k1tpEWHX3I-3TFZGvUquPoZtK2XB1kHklmgAcLfzQZobFMs2OkNLiGhrvfCp2-jzm4JthaGmbng6kut7-4iexRukOdvYorgmMAl4ebkt1QjKiYWQfA_wNwfAi83SUmcI4aum3sulOdVzWOI-73DACX0rUi06ehmOXhbD3cTRrk7l8X1YZVwbb4TDG2j52oHuqwn03Jgv4pjpG16Px3aZKHCCRkYxNFYgfJnRMW2aH0Q4ta1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: ۲۵ درصد اعتبارات دانشگاه‌ها خرج تغذیه می‌شود اما همچنان کیفیت پایین است.  @Farsna</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/458892" target="_blank">📅 21:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9920ef2694.mp4?token=g5lrZZ7g5MTRqPyy_-O71_ByaU9GjkYshjA2r-sa1NmyfV78DbjXscI1sba7se-TCyd_KrfTXGY-HTQRoMoax81iS8-nJX9jCv6ejHlRvBdI1tEyxYasUCXz1y1lcYKtZpm5GoOmJSEdUPpHVRsBhXU3KTn8y3AL4jxQkQgQaqUDCCiqMydc2YDEBH9yzt9k0EFo3BF1r926eoYjBdU7-M8hzlS8r6ul67G0lTHp4dRGArF_1qJFAl009keRUnWOknNEojFZ6ZTewIbs4swmD0uobjIqP42LzxL6qpSAyiSjqoOAchaFiBT5ajrm_cvY4YOb0wWIKMwVWq7VkcQXaZMYFGwik8wI8PEAOZknpe8Y7PAMscvx_CK2fLW-dW1Uori84JUYkWacORvPLZKI5T6IT4Vqvdurb5iSB2NFl6Rl16hu8WSRirl6BbitVp3A3DYmIZwEO45eQNjJzn6lYxfpEUzRnsOnHGbemKfWKgS5lD9d3ONT8zgqhJsNH_Qc2mhBGb7GsGzw6_cctKYK1JhN8RHg38ypiRfeV3WN13lchN1UswFcC0s6iacf1HComRtbTHEXWsugI9f6J0ilnnlxtFh2JfGfm4EGDTHq4Adk09YiUj6QU16f3gl-Eleu4QYi9FmOVgMVgKghnk4ns80ZylYjOz7WuglYnAnbD80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9920ef2694.mp4?token=g5lrZZ7g5MTRqPyy_-O71_ByaU9GjkYshjA2r-sa1NmyfV78DbjXscI1sba7se-TCyd_KrfTXGY-HTQRoMoax81iS8-nJX9jCv6ejHlRvBdI1tEyxYasUCXz1y1lcYKtZpm5GoOmJSEdUPpHVRsBhXU3KTn8y3AL4jxQkQgQaqUDCCiqMydc2YDEBH9yzt9k0EFo3BF1r926eoYjBdU7-M8hzlS8r6ul67G0lTHp4dRGArF_1qJFAl009keRUnWOknNEojFZ6ZTewIbs4swmD0uobjIqP42LzxL6qpSAyiSjqoOAchaFiBT5ajrm_cvY4YOb0wWIKMwVWq7VkcQXaZMYFGwik8wI8PEAOZknpe8Y7PAMscvx_CK2fLW-dW1Uori84JUYkWacORvPLZKI5T6IT4Vqvdurb5iSB2NFl6Rl16hu8WSRirl6BbitVp3A3DYmIZwEO45eQNjJzn6lYxfpEUzRnsOnHGbemKfWKgS5lD9d3ONT8zgqhJsNH_Qc2mhBGb7GsGzw6_cctKYK1JhN8RHg38ypiRfeV3WN13lchN1UswFcC0s6iacf1HComRtbTHEXWsugI9f6J0ilnnlxtFh2JfGfm4EGDTHq4Adk09YiUj6QU16f3gl-Eleu4QYi9FmOVgMVgKghnk4ns80ZylYjOz7WuglYnAnbD80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌صدایی مردم با پیام رهبر انقلاب به دولت
@Farsna</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/farsna/458891" target="_blank">📅 21:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5618bf1104.mp4?token=RVQQDGxFs5MtPf03CIv1L2xNuwqD8iLx2N6X18Rh0gM3QxVnJsf2xt_qyw3xutbaE3-ftWI_QBKFjTWAUZXz-ucdVDq5dtrNEErsN4a72LhCm9nLUeVDtx6D-q-NpGABHX9fMaDuEDAwkFpUREJjMVfy_Dzy54QOdOnuwAK88EJwTBOwEFB2RBEg8z7Qqq6NPY49iNthopPsb8C_Z-tL8wFBTuhHQ6BQlb-ydazLQga7e5WRG950oZ2gu-U5BBL36XW13ZbWlyIabnPpPnbLRJdh-g0z-1zby4CSRkmgPKzBD8VEngy6HcJAQGH1fMLZUAWCj_OA3D4IWJET2wbDoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5618bf1104.mp4?token=RVQQDGxFs5MtPf03CIv1L2xNuwqD8iLx2N6X18Rh0gM3QxVnJsf2xt_qyw3xutbaE3-ftWI_QBKFjTWAUZXz-ucdVDq5dtrNEErsN4a72LhCm9nLUeVDtx6D-q-NpGABHX9fMaDuEDAwkFpUREJjMVfy_Dzy54QOdOnuwAK88EJwTBOwEFB2RBEg8z7Qqq6NPY49iNthopPsb8C_Z-tL8wFBTuhHQ6BQlb-ydazLQga7e5WRG950oZ2gu-U5BBL36XW13ZbWlyIabnPpPnbLRJdh-g0z-1zby4CSRkmgPKzBD8VEngy6HcJAQGH1fMLZUAWCj_OA3D4IWJET2wbDoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: در حوادث دی‌ماه ۱۴۰۴ در کف دانشگاه بازداشتی نداشتیم
🔹
بین قوا اجماعی برای برخورد منطعف و مهربانانه وجود داشت؛ ۹۰ درصد دانشجویان بازداشتی در کمتر از یکی دو روز آزاد شدند.  @Farsna</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/farsna/458890" target="_blank">📅 21:05 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458889">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccfef2a11a.mp4?token=PBEf0fI_OUq5UrAmCxK0xwI7dQ2SgVak_iDG_jNYvp6o5-Lhl6zOyb3vVxxV-N7bCtqnO_jZV38oVSi0kGJf3Yq9qeJIvYTh7PHwvqWA1yA_MM1TaFFmuvR8wsybRILu08vPWlyG3S5KZRejbMx-p9U-cSrQrVfAZUnIOEaWbp08m_-Ao3Y7g-l3qf65febcbVqDIkZKel7eW9d6J2yThtHWlFBVf2JFC3hQkU7UbJkUGL5_tTo7O6g3pr3I389eNZRI-Q1Qi6ht2Dmzpm9KBhTP9Fq05tDzQIcRvJBbN6spA3KNRnQSmsDOAVveayvgAPU0HcdLbW_uN54XCH3mtQitzOMgR9XDzOV28X6UMgvz3JpZWkQAuPkcScFgu5hdtlNih9nKeIA9bvS3QmaoM6atMVNarhZwIFSD6hTviFn1azC8YG64kygMfmrIiYT7ifNrd252ciJBrR2Skg88wwupSH3QDym_nE8JF-4XpGGp9tJmgh3e6jTGZiIyVG44JiNNQYGdiiOKjEck-SR7UbPwnhMmSVJ2z6bSpZZKHqCgZeqrMgNp-C1vY_NK4PWvoTzItdrgZ_fMCd7374wztezAXYdF7KUZCn8KBJPlMuiUn658MHUjWHzfhSDZMTYHZS4QSaE6bkexGzaoBoVt3TZ5t4ufXNrlY1vOQf-gP1s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccfef2a11a.mp4?token=PBEf0fI_OUq5UrAmCxK0xwI7dQ2SgVak_iDG_jNYvp6o5-Lhl6zOyb3vVxxV-N7bCtqnO_jZV38oVSi0kGJf3Yq9qeJIvYTh7PHwvqWA1yA_MM1TaFFmuvR8wsybRILu08vPWlyG3S5KZRejbMx-p9U-cSrQrVfAZUnIOEaWbp08m_-Ao3Y7g-l3qf65febcbVqDIkZKel7eW9d6J2yThtHWlFBVf2JFC3hQkU7UbJkUGL5_tTo7O6g3pr3I389eNZRI-Q1Qi6ht2Dmzpm9KBhTP9Fq05tDzQIcRvJBbN6spA3KNRnQSmsDOAVveayvgAPU0HcdLbW_uN54XCH3mtQitzOMgR9XDzOV28X6UMgvz3JpZWkQAuPkcScFgu5hdtlNih9nKeIA9bvS3QmaoM6atMVNarhZwIFSD6hTviFn1azC8YG64kygMfmrIiYT7ifNrd252ciJBrR2Skg88wwupSH3QDym_nE8JF-4XpGGp9tJmgh3e6jTGZiIyVG44JiNNQYGdiiOKjEck-SR7UbPwnhMmSVJ2z6bSpZZKHqCgZeqrMgNp-C1vY_NK4PWvoTzItdrgZ_fMCd7374wztezAXYdF7KUZCn8KBJPlMuiUn658MHUjWHzfhSDZMTYHZS4QSaE6bkexGzaoBoVt3TZ5t4ufXNrlY1vOQf-gP1s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماشین دروغ‌سازی؛ این‌گونه افکار عمومی را هدف می‌گیرد
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/458889" target="_blank">📅 21:04 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458888">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSQGjoecgiC5HnXHPMeKO-W9nEI1lXcjpEX-HL89LdMKzsFv8MCgTlL9a_Cb51-iS99mjvUTkqfvX-OP2ijwIgE-0Xm_KHMxwuT6G5xUDrDo6bsjAksNeWp5MLchHcu81JbrJ6V-Pag22tjQUoDSPFSQHsxqrUnxkJH5vsfbWu92zELoqhgC_iOBz3iNqGxUAgi55FnI5tF1jMjCdgO3RTWsVVMLgdnGv9THbbsI-Pp081MfBj0-oxtwaiw0KO-j8LK1E6q9fqlJFKBOLXiSJW1J2tqNNKeTYPWSdvkRzyM2ZiOhxYeke-KvLwx3MLSeC1YsEeobSKyjCMz8tbsW5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ پاریس به واشنگتن درباره جنگ علیه ایران: زیر بار تبعیت کورکورانه نمی‌رویم
🔹
نخست‌وزیر فرانسه سباستین لکورنو در واکنش به انتقادهای اخیر آمریکا از میزان حمایت متحدانش در جنگ با ایران گفت: بر کسی پوشیده نیست که ما یک متحد آزاد هستیم، متحدی بدون تبعیت کورکورانه.
🔹
اظهارات لکورنو در شرایطی مطرح شده انتقادهای ماه‌های اخیر آمریکا از متحدان اروپایی خود به دلیل سطح حمایتشان در جنگ با ایران، بار دیگر اختلاف‌نظرها دربارۀ تعهد متحدان ناتو به سیاست‌های واشنگتن را برجسته کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/farsna/458888" target="_blank">📅 21:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458887">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8876fc4190.mp4?token=h24UrPKuN_gwHTMBrJwLixR2kQkQnus9hcMqZteyrSm7liL2QFpU1obfx6V8sWjdn5sseBsChOApYb7GFZgkYP136eKugofRqIWiCrWt2SkT5i4FUEIITothd23SeujqOkVbpN_OnIkJVR8zsxWHBMwqSUqP-IPXMaGsSjyC3fVjXGCpeUgoRlEykCJnlhLM5SFTE2yCjsiGUKUSFJXJ1gMwkgf3seS37KsANRoqoYLoQGbVaFu3w_g7WP3JJtyrOUO_2FCW1Gush0qySY7t_pcU56OT7LxLCMXh3VXCwYR14fEkY6-JVlra5ZzCk1NCFA46b_MZ6NCe9ap_Zk5KOzmC7O62gqJhppReNXhtO3l69hyqt-dNRU1jN7ah5YAg-2Xi9wyMRffDZH3JOioOiyFyxDmBSZFrY4dJPTUTiohq0PwycPnWeAXk5FQrcAXlNzqZM5LjlWds7h-CLcvQZLQC_MLfr-959x_mGKdDCxkx2mDFVW8g6_4LBMPD1qsA33GNoylRkwyznZSPa1natiRPTeAdlHVFAOCKmFiBL2rHh8Uolpm8jwFZUJOtmbegMYaGNZGLQ0evGpJoU0vsrevyLVS1cTLsOdK3bn3KGTrdjmAr6ZGjEICZWjifvtttz32kX8y3S14YqZf5WStmTK7cXuPkzNXQWJIBEKqrW2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8876fc4190.mp4?token=h24UrPKuN_gwHTMBrJwLixR2kQkQnus9hcMqZteyrSm7liL2QFpU1obfx6V8sWjdn5sseBsChOApYb7GFZgkYP136eKugofRqIWiCrWt2SkT5i4FUEIITothd23SeujqOkVbpN_OnIkJVR8zsxWHBMwqSUqP-IPXMaGsSjyC3fVjXGCpeUgoRlEykCJnlhLM5SFTE2yCjsiGUKUSFJXJ1gMwkgf3seS37KsANRoqoYLoQGbVaFu3w_g7WP3JJtyrOUO_2FCW1Gush0qySY7t_pcU56OT7LxLCMXh3VXCwYR14fEkY6-JVlra5ZzCk1NCFA46b_MZ6NCe9ap_Zk5KOzmC7O62gqJhppReNXhtO3l69hyqt-dNRU1jN7ah5YAg-2Xi9wyMRffDZH3JOioOiyFyxDmBSZFrY4dJPTUTiohq0PwycPnWeAXk5FQrcAXlNzqZM5LjlWds7h-CLcvQZLQC_MLfr-959x_mGKdDCxkx2mDFVW8g6_4LBMPD1qsA33GNoylRkwyznZSPa1natiRPTeAdlHVFAOCKmFiBL2rHh8Uolpm8jwFZUJOtmbegMYaGNZGLQ0evGpJoU0vsrevyLVS1cTLsOdK3bn3KGTrdjmAr6ZGjEICZWjifvtttz32kX8y3S14YqZf5WStmTK7cXuPkzNXQWJIBEKqrW2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وحدت؛ توصیهٔ رهبر شهید که رنگ عمل گرفت
@Farsna</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/farsna/458887" target="_blank">📅 20:55 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458886">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cae6f6d88e.mp4?token=BoKoyZsAT2DimybAn5zmyJOdowwBBnPseT5ggqxKmYCLtGTEiQLIP2NB18v3BI2kL9C8-alQP4pOXF-0dwBwMzu2f-CJHL64x-TjbO34tcm0dq8KTVQuW3MHhusKNMf0YNFzIw1Pr5sx8IpQbd4u8OOkAiHNYY2zp07E3CMkd_9E9KARGJVJcfTAj0Vnzq2QPB4oNeNjZEKgK0VLmB-ke9h5lnrPnCU7Fyiz-47nW4EmuIs6PZErZd1YoNInnKCGiVqUvXr1RQANpT_8oz-MW-SiYB-NJl3Jw7xLeky55ic8C84LmJDWpv9YdgfnpUtTdkGLohYM7THHRj7TyA7fIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cae6f6d88e.mp4?token=BoKoyZsAT2DimybAn5zmyJOdowwBBnPseT5ggqxKmYCLtGTEiQLIP2NB18v3BI2kL9C8-alQP4pOXF-0dwBwMzu2f-CJHL64x-TjbO34tcm0dq8KTVQuW3MHhusKNMf0YNFzIw1Pr5sx8IpQbd4u8OOkAiHNYY2zp07E3CMkd_9E9KARGJVJcfTAj0Vnzq2QPB4oNeNjZEKgK0VLmB-ke9h5lnrPnCU7Fyiz-47nW4EmuIs6PZErZd1YoNInnKCGiVqUvXr1RQANpT_8oz-MW-SiYB-NJl3Jw7xLeky55ic8C84LmJDWpv9YdgfnpUtTdkGLohYM7THHRj7TyA7fIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: رئیس‌جمهور برای حل مشکلات کشور همچنان به دانشگاه امیدوار است  @Farsna</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/farsna/458886" target="_blank">📅 20:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458885">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=bcWzBiw38ucBKWTbiel29B9Z3Q7SG9EP27BG1gmkyl1gA94_4BxgPNTSBeT_mm5jasAa1DiXlBlV34ptcAW5tUugjAUstDtOekFevJDFNtKPKreL0t3Jufl6jLPtqbLu31jcVx8bDjhTYqqLcNZzxm7JQ1koEQLLpUstU0dUW5EruiCFgP-Ap7WxiBEXWI0--Ge4vhfhgwhJCm4TGGuFc6m7za-mV7cxoncIfQOu2C_lEKoMe-dl9cnPlf7SGS1r5QUxnRshX_u5EPHMmyf3J04w8RPfUutCKkgkXgaX1xaqRQ0cRleNQuxuK9aRyJRCzCuaPS3qRPQGUn6lu5FZ5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ef114bf55.mp4?token=bcWzBiw38ucBKWTbiel29B9Z3Q7SG9EP27BG1gmkyl1gA94_4BxgPNTSBeT_mm5jasAa1DiXlBlV34ptcAW5tUugjAUstDtOekFevJDFNtKPKreL0t3Jufl6jLPtqbLu31jcVx8bDjhTYqqLcNZzxm7JQ1koEQLLpUstU0dUW5EruiCFgP-Ap7WxiBEXWI0--Ge4vhfhgwhJCm4TGGuFc6m7za-mV7cxoncIfQOu2C_lEKoMe-dl9cnPlf7SGS1r5QUxnRshX_u5EPHMmyf3J04w8RPfUutCKkgkXgaX1xaqRQ0cRleNQuxuK9aRyJRCzCuaPS3qRPQGUn6lu5FZ5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
ترامپ: حالا فقط یک اقیانوس کم دارم!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/458885" target="_blank">📅 20:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458884">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f86aae29.mp4?token=qr5M4gvtZv9Dmj1gQkx83SXfIpIl4oPwaLi32kzDzmIZtAeObB2Slab-cgnaE1MG7wPrFDJiUAuhscsDDwwXl64pBYXweDPmlh3uswgq0Fs0xaKDDj6btdErwsv1s3bdh6ksAG01CyS8KWCc_1fw9TbyOmbrTn3YYOXCNmpc6IksVqUllVdxQPLtfdNT4VNCBJkVANF7d9eAKNFK0f-sUZ5Y5xN1oOlXq-PYXTH45_CwCPMgmUYCDCCaYnWXkfXAnApwZG4c3IntgX0EsnHxgsySmJE8T2F88knabIZIXkdkLzBXV8BhgcLFY7-t_uJe2DvdILBiXRoj3RTkZop5ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f86aae29.mp4?token=qr5M4gvtZv9Dmj1gQkx83SXfIpIl4oPwaLi32kzDzmIZtAeObB2Slab-cgnaE1MG7wPrFDJiUAuhscsDDwwXl64pBYXweDPmlh3uswgq0Fs0xaKDDj6btdErwsv1s3bdh6ksAG01CyS8KWCc_1fw9TbyOmbrTn3YYOXCNmpc6IksVqUllVdxQPLtfdNT4VNCBJkVANF7d9eAKNFK0f-sUZ5Y5xN1oOlXq-PYXTH45_CwCPMgmUYCDCCaYnWXkfXAnApwZG4c3IntgX0EsnHxgsySmJE8T2F88knabIZIXkdkLzBXV8BhgcLFY7-t_uJe2DvdILBiXRoj3RTkZop5ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملۀ رژیم صهیونیستی به یک مرکز نگهداری سالمندان در لبنان
🔹
رسانه‌های لبنان: رژیم اشغالگر اسرائیل یک مرکز مراقبت از سالمندان در شهر حولا واقع در جنوب لبنان را منفجر کرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/458884" target="_blank">📅 20:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458883">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/191ad8e91a.mp4?token=ZMBk7VP2-wnFdJSwmXe3z2D5tUHFK-JLjI_CMhvcZ-VDWW7vtHU0WDgSRKResc9Zn5vM0TMMU7Ll9lteO93dd7OucQ7B5EM2KWDrThwCq-hNdx0W_eD_kcaO5kEx19zrwCuSWesqzBgfy77EjTDi1d2-wXOOj5yTu3XrbKE0-tTAndWCjDgwU0TbC6JgZBVsaY4OwYnSDxN_rTkzVz4OAaAX1A5Z62frsy0H_W9o0veJsPWMMDBmkslGPPMLEQ7oJODCyh3fs6HaBPc8g75IZf3P0hOH_DmdvOnWp9UjUaSr7Phr0degAKjSxmyiFh4tzMU2GyaW7d7zhzxuz6blGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/191ad8e91a.mp4?token=ZMBk7VP2-wnFdJSwmXe3z2D5tUHFK-JLjI_CMhvcZ-VDWW7vtHU0WDgSRKResc9Zn5vM0TMMU7Ll9lteO93dd7OucQ7B5EM2KWDrThwCq-hNdx0W_eD_kcaO5kEx19zrwCuSWesqzBgfy77EjTDi1d2-wXOOj5yTu3XrbKE0-tTAndWCjDgwU0TbC6JgZBVsaY4OwYnSDxN_rTkzVz4OAaAX1A5Z62frsy0H_W9o0veJsPWMMDBmkslGPPMLEQ7oJODCyh3fs6HaBPc8g75IZf3P0hOH_DmdvOnWp9UjUaSr7Phr0degAKjSxmyiFh4tzMU2GyaW7d7zhzxuz6blGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس به ملوان توسط بیفوما در دقیقه ۳۴
⚽️
پرسپولیس ۲ - ۰ ملوان  @Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/458883" target="_blank">📅 20:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458882">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KRrk4QQfmsCOQfivt0S_kYahT7NEi89amEGASgBXLnv8BUitDq4SuSuNOAyDjhf5NSU3n59TkBTDR635IBlRVsoZCYUwU-OIBvh9kdPD5_FYm-nMzH_M28OyxyVC4BI5kYWuPuhmCJNc8qMH75XbgWqluuGXLmFH0nC2Z466XtPmJIxdYeaWaWED_9-ile-qQTf8EmUDB917D4UsMIQmgOE37Y5HeYIou7MoK1N9oGNNdrrDq49F5gHJ9sjv0YFccaTECHjRzI6vVWb3qTVbcmBGCf6lgQVeEF8M21JLlBAcZ4upyP_klmcVp-Q9uOxoGzmicqFFMHFgXPcQ4rU-gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازندهٔ چت‌جی‌پی‌تی شمشیر را برای ماسک از رو بست
🔹
رویترز: اپن‌ای‌آی قصد دارد ارائه مدل‌های هوش مصنوعی خود به «کرسیِر»، ابزار برنامه‌نویسی مبتنی بر هوش مصنوعی که اکنون تحت مالکیت اسپیس‌ایکس قرار دارد، متوقف کند.
🔹
تصمیمی که بار دیگر اختلاف طولانی‌مدت میان ایلان ماسک و مدیران اپن‌ای‌آی را به کانون توجهات بازگردانده است.
🔹
این شرکت دلیل تصمیم خود را نگرانی دربارهٔ نحوهٔ استفادهٔ اسپیس‌ایکس از فناوری‌های اپن‌ای‌آی و تجربهٔ قبلی از نقض مفاد قرارداد توسط برخی شرکت‌های متعلق به ماسک عنوان کرده است.
🔹
اپن‌ای‌آی همچنین گفته پس از تغییر مالکیت کرسیِر، براساس مفاد قرارداد فرصت محدودی برای پایان دادن به همکاری داشته است.
🔹
در واکنش به تصمیم اپن‌ای‌آی، ماسک با لحنی تند از سم آلتمن و گرگ براکمن، مدیران ارشد اپن‌ای‌آی، انتقاد کرد و آن‌ها را «غیرقابل اعتماد» خواند.
🔹
در مقابل، مایکل تروئل، از بنیان‌گذاران کرسیِر و مدیر فعلی در اسپیس‌ایکس، اعلام کرده که کرسیِر همچنان در حال مذاکره با تیم اپن‌ای‌آی برای حل این اختلاف است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/farsna/458882" target="_blank">📅 20:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458879">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2640e0cc48.mp4?token=EiLNGlbyujS_uOdM9FX-YevHFIB7mTN8wlMwnQfZsbGmzwWdLc63AIPSd1kZ-Z9LSUzDQsgjjLJ9QmC3QWLH1tm43xznbXTDnRbyt2OpvFOA8WFTacoUOpuiQtxw8GAzqHJwlF6iGDdleHvQDoFL33uNVUv8lZyKsYdkVkWmbG-QZcr6Sit80gi8Zjg29HZ5V0oRrTnIAon6_UlQorQUIhaBJ-kChfeMIrNUCVH_TghHSxs94K-FlI9WIFoa6DMpz0oXfikSQqNjY7MLQfqSsOuyo-iG4q38eGyqguqec8QfD8CU67oN0BagC9aYmbrWfnwRrZivc_FFSmvf0D7PDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2640e0cc48.mp4?token=EiLNGlbyujS_uOdM9FX-YevHFIB7mTN8wlMwnQfZsbGmzwWdLc63AIPSd1kZ-Z9LSUzDQsgjjLJ9QmC3QWLH1tm43xznbXTDnRbyt2OpvFOA8WFTacoUOpuiQtxw8GAzqHJwlF6iGDdleHvQDoFL33uNVUv8lZyKsYdkVkWmbG-QZcr6Sit80gi8Zjg29HZ5V0oRrTnIAon6_UlQorQUIhaBJ-kChfeMIrNUCVH_TghHSxs94K-FlI9WIFoa6DMpz0oXfikSQqNjY7MLQfqSsOuyo-iG4q38eGyqguqec8QfD8CU67oN0BagC9aYmbrWfnwRrZivc_FFSmvf0D7PDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: چهرهٔ ‌حراست در ذهن دانشجو موجه‌تر و مثبت‌تر شده است  @Farsna</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/458879" target="_blank">📅 20:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458872">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LymYNh05_Wc_BmH97ZwpHkNMseMCoZOPbxu3IFfb_GKgLrDDWfVltDf2piq-Q_k7xZ7NmSI1i6W5MFx6RFeM4ul3TjqD4ZUjDsXzae6W9_Meyj679ul3gYKMRaLgjOYy4zMDuedNv0dnEWCUsnxvQpJGPdU5RTwHPXrAaVFMPAOQpj2LXpeaTgWlV-5ydVTHI2PdxDV5I6ALWw7v5OUIMZ-O5-511tsF58KkCf0-ogAovg0i-FemcnPttYM07fHjfG9-dueBJfzYjflPp49eUa1rPMGEPcuSj2ji3sxCPNXfsJmA54fGRWUne55GuEIJzoe6r26u-brWjuhla3Ercw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c5T-FbBv_a_mHGloUYwGUyc8D2vYZfBOhUx6cxwR9AMDP-9MP-457em46oGPRShn4pugU9x3z-Fba2twYU8wdUdTi2Dnz5F6ZIhbZppIHOjn62-3mOEx5emA-noPN1xxaXiJYpw41UUowQ61_0mE0eaZQhmHczDfB6zT2770DLzmbPLAY5ctY8l_e-8nIZXgGYvQPrRg0X3RQEmEBUCE83UGvBB4iTeOgH2GN8mV4wekIrzi34ddoWn7d979IGinDedQYiRD7CVBWeV-9_lqKMNNWjWNul4JR4O4_4LFjbimEm6s25zQSsScQw_RH5oC_AZkCKiK9iIsLdo32N78zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bpOiMtFUeoPtb_Nz_RigBIRDkBHRIRirmgfE9tnrj7fyz1ABD9fzG_loJj6hueibur6yNJehcjdzHW3u_DhMOr6BPp2XB-BTKGUnVBi_mW_qcRETlPbUMuz8sdLht27aMReK7NR_F8GApO0N4zICUkCAZ43OTSy-wyKLmwQm-yknlg39932OFmF1hftQNMxoOYGRNFClQeEwTHEsh5DOpoKQUKvSiqy5-IVAxlRolh86ZIe1ka1GnHaFCiQMWFm4FqAF38BgviSALjD0Tf4zZDHWvaXoczPk3c_p6MHkvgO30SMwhFvTYGdRLunvVwkrJdH4agt-MN1YXt1jmksVrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OU4nd_B-Uf2onuGKAfU2yQlZ3SnfIIlnKaPExCic7eZ0K34EMhZU6lGgXQkGRhscqC6mAqldFq529BLS2GvmjKIHeMX7vOAHxUosVQ51eG-e_yn3ncZHeaJlkFd3ttnRiI27rgBKeFkUoxwf3BCk6VX-DiI1AqOI4p8p4WjG53TGErK1Ky1Zx1-p2pIbNRJ9Fvhc8YuP7PG-k9XGhvdEG9NMxr7rt8A5O6W8cD2gyx6pgMmdac41Ki8rQpevhVNHoyKz9rIve3MEuz8Bs1qK9lWFLFJKPGwDut3AvYh56sbGtCgvvmYXHlQ4GRkEy3efiuJJm3-F00O7jjqJojqqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/el7czrXPAtVgEDla9CdPw5-hfxTKZ8Nd_4S90fhaOiIs8v5LWe1DJipchPWG-EOqNhDwBPJgTQWONQ0haAo5gCzeVTuiwLyGwAhbGprD6JN2ZnvDphZVBl5w2notA4sgWRxd3Rv96ZirTt03SycUTsYvw7SpMSpr4zJjiaP9x-GgPcgoLJHtXmSeK-FsaIdupnDCNc2rFfh6DPXciN1vOPY76Eg5xgckJk_Uwr5oL1P7N132PoLetqhyGxeAYd8xaYTzwo3ck6Z-iSFOZtag3VC_L_OT9w_839xNGCtCuxI7b0wSqLbXd4eaXnuv3jIMecMisCFak5EAwhh0V04FLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1E400F7_BQUWKIdulLU_V-GMGVXRQKnQ3dO8GNrN8Catifjfw2ZRBamuUfn5cgTLE3XetH7qeXBBOqziC1T8C0vQ_aAG3_8DBNRMZTeVC0Rq0lYcenIdmdxQVfBg-z3XjKkD_nSPkPwrd5-BWQABHgMS1ytF1PeizHJ6-NT0Feid15CJljy5lFbW0FK_W9BF2iRiQchT4-alL0FmDm9U4I8dGYlo-0fwV1HAMMTu4LUiPn9i_2pmKHglipBO-tgHJHz_AKtfE2ckkhJ9E_XLv23rBQKzaLPDkBBQXy2oAV3TOTdAwz6vkx7cwcE84SINNV7umQu3QfB_a76OfTnJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugm29k9sDOLXvPlL6r8YLFfm3qobXC3X12b2zLp_mGx8chA7KDKrPRipZsnmevTe3KGr8sh_C7fZKpvcBy9gf0XDioULzdc231M4LuwR5FGNOEaH98xE3WHjV80N5wTrtnadPwbV51PPkfz9dL5HIFc3j-mCifWSxNYjsbD7fHsHtcRDXkni6JIHjs9onnEA5wm-4QVTa3rBm_a8-aWMc0k01Nk1aCf6svv16-5foYK1iMVL5ULuPJ0mdUDj6yFBLeFZS36G4q1xqOX2ZquhJjYi-N6rWJXkyHtiTuCza9NRT3JcG1oJxhBa_PQRE9t9L1Vdb2PDVeUApRgn6-cv2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین «روایت رحمت»
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/458872" target="_blank">📅 20:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458871">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPSuRBvRPRX4YAOwwuzUH_cE9eeNRsKkeY8UmgWqU2CRfgBRG5kUamVSPjYYJkQkTmVkikG3g5UCdXv7QhX_Y3s2bU7cnFOlPE-ssKs-Rket3ao93pQheabLH7Xys37LlvT7GoioeDam7bUd3PypAZzjLOSm9rEqalwjLMB1p25Mx535WyEf7fLWZuOjIxq7JkpyrdEX1S2lmbGAauiwJ6j-zuipn1omVsX-ctNghDvUveZaQjbeq-cH581otYEg2l3GxJ-bw6BIrwOw-lQ6bO8tpOPdFCplmtvTrv-cSlwKED0myKPfWFD6VPKnYCqbZH0Lb9_JD_i_ZLYJ7WlwWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: سیره پیامبر اعظم(ص) چراغ روشنایی بخش مسیر پرتلاطم بشر در جهان است
🔹
رئیس‌جمهور در پیام تبریک ولادت نبی مکرم اسلام(ص) به سران کشورهای اسلامی:  مفتخریم در امت پیامبری زیست می کنیم که پیام آور صلح و امنیت برای همه جهانیان است، پیامبری که نام دینش صلح و سلم و لقبش رحمت عالمیان است، رسولی که فلک را قدر و منزلت بخشیده و سیره پیامبر اعظم والاترین الگوی کمال و مظهر عالی ترین نمونه اخلاق و سجایای ارزشمند انسانی، همچون چراغی روشنایی بخش و هدایت گر مسیر پرتلاطم بشر در جهان بوده است.
🔹
امیدوارم به یمن و برکت این ایام خجسته و با استعانت از سیره گرانمایه رسول اکرم (ص)،‌ امینانی باشیم که امنیت، عدالت و آشتی را برای جهان پهناور و به ویژه کشورهای اسلامی به ارمغان می آورند و با تکیه بر عزم، اراده و ایمان مشترک همه مسلمین جهان، بیش از پیش شاهد وحدت و همبستگی میان امت اسلامی و رشد و اعتلای روزافزون اسلام در سراسر کره خاکی باشیم.
@Farsna</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/458871" target="_blank">📅 20:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458870">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIPHlz1fBZxB2fzrERkH639mF9tMfjgKO4a4loah9f28RtOlwYqgUdiS5a2LUzk_wVyF5BuSFb1BN1JDz60pWu72rFJnGblcHw6MCrZ6d4NrfXoxrDRkyS2iJ_ai3l-I1n8EHXCwRFBX7wS49XUdfQHu5eyUabX0TYEfxyYyk9YFp-Zu30aJRtlYuhSfs1UFtBlZx0o6e67TmmxgBV2MCA8tPyJBWiFVimawgj3sKJLiyg6YTo4m5Bu1srC5dleHFdr6A9SssmxSVwaKhgx_KHzBH_tj-yUoi2_3bwmnAR5usVEBQkVpTa0mJp8xfih0DBohpt-NAhPzw0IzPSJhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایت ۱۸ گشایش بزرگ در ششمین روز شهریور
🔹
روزگار ما، روزگار دوگانه‌هاست؛ از یک سو موج‌های ناامیدی و از سوی دیگر، تلاش‌هایی که بی‌سروصدا در گوشه و کنار کشور ادامه دارد. ما در خبرگزاری فارس، نه چشم بر مشکلات می‌بندیم و نه اجازه می‌دهیم سیاه‌نمایی، تلاش‌های شبانه‌روزی…</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/458870" target="_blank">📅 20:07 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458869">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5ac2e050.mp4?token=YHjypJTrv7EzVIbGv8olbACtyTgmEg8xKpvp4So-dDLWgVMhM_TBSXhQLtkoc-csa3jBePo01C53jM_1xVpTz-u0iLhesnKJJI_xfHyqikRqo7H7q4599NGBrOFDmaa7sKU_PwmWC-1N0OkTTZKLaTQOPjRJ4P9-L0s4l5kBPcl5LwrYhwmxCIT0tzXGpBybwjp7a9slILSr_mbC1inBFQYbBmAdTJynBgfH1WvYbrb0cdbQ0kRj_0akKAT_IrW-aWKa56TrdBJ1YMRqGwx7VTlm1m-GhvMbZ2C7fToQs6i-sR0nF5cnKvR2kqlU8AgyCuR7-x1jSducWk-Nj_-Osg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5ac2e050.mp4?token=YHjypJTrv7EzVIbGv8olbACtyTgmEg8xKpvp4So-dDLWgVMhM_TBSXhQLtkoc-csa3jBePo01C53jM_1xVpTz-u0iLhesnKJJI_xfHyqikRqo7H7q4599NGBrOFDmaa7sKU_PwmWC-1N0OkTTZKLaTQOPjRJ4P9-L0s4l5kBPcl5LwrYhwmxCIT0tzXGpBybwjp7a9slILSr_mbC1inBFQYbBmAdTJynBgfH1WvYbrb0cdbQ0kRj_0akKAT_IrW-aWKa56TrdBJ1YMRqGwx7VTlm1m-GhvMbZ2C7fToQs6i-sR0nF5cnKvR2kqlU8AgyCuR7-x1jSducWk-Nj_-Osg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خورشیدی که امشب تو مکه تابیده
🎙
مولودی‌خوانی محسن عرب‌خالقی
@Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/458869" target="_blank">📅 20:00 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458868">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11161a48b8.mp4?token=QD9Y5ve3qEevUmFOprCxYsMRKIiMnMINuDl3e41jNkR3CfwXFUR0cM1KVQCqotiMIJW2diLuXNQzjMKfJvdpgMFkuSYEA65sG4f2L7-eGflcPcybAG2EcoSaXfLIPaR5yxDI096gaxu8RCy7ahuKfLN16KyO49H-gwAXsmhLKF2FoHk9kNG1DdJLs4DfbaOBDn_oZcv5lOJTrBzFTMzVtQ0iOEHkfZ5XRFVzN0Q8vOmhiyr6tgG7oqNhh-dKTcZKfb9xyjyE8bvfOwAa4tbWsx3Th2ZY1s75ZAmLJuEiG4QePe9aJO482vE2WYyg3_083LfV6RwBFSqpCQ_gUTNJ8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11161a48b8.mp4?token=QD9Y5ve3qEevUmFOprCxYsMRKIiMnMINuDl3e41jNkR3CfwXFUR0cM1KVQCqotiMIJW2diLuXNQzjMKfJvdpgMFkuSYEA65sG4f2L7-eGflcPcybAG2EcoSaXfLIPaR5yxDI096gaxu8RCy7ahuKfLN16KyO49H-gwAXsmhLKF2FoHk9kNG1DdJLs4DfbaOBDn_oZcv5lOJTrBzFTMzVtQ0iOEHkfZ5XRFVzN0Q8vOmhiyr6tgG7oqNhh-dKTcZKfb9xyjyE8bvfOwAa4tbWsx3Th2ZY1s75ZAmLJuEiG4QePe9aJO482vE2WYyg3_083LfV6RwBFSqpCQ_gUTNJ8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم پرسپولیس به ملوان توسط بیفوما در دقیقه ۳۴
⚽️
پرسپولیس ۲ - ۰ ملوان
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/458868" target="_blank">📅 19:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458867">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YksBGCYveSahr1p96TbAS0NOx3iC-EePKnBsf9V-OaHeFSSwN3SicgfSaIMVQCRXYKwwfcVlQWim-YUnXtbvsSqynt3QHbevE2s-mUSwqRnldMXJIdCgKU5ZrpcaEch4OrvGJfbB5E4ziwdltiIZy6q1mVnekvUfs0yb74KJx6T1LrexcJ2c-TKN5fldbbBHe4rP4tEG0R1gZj70rjIGts3PqemLqpP7aMZvi9tv4efEc0Rz9oQKo_bNmwQ0plWtP63OuXwONRVRLtW5C02rNCZ-59DZKnUxmwvE4ndZr84EhFdb-yucmUNH2erctDX2UNegUaPXtkrDcP3FFWEWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت دبیرکل سازمان بدر از بیانیۀ گروه‌های مقاومت عراق
🔹
هادی العامری: گروه‎های مقاومت به شرط تحقق حاکمیت کامل ملی به سازماندهی سلاح در دست دولت باور دارند.
🔸
کتائب سیدالشهداء عراق امروز در بیانیه‌ای شروط ۱۰ گانه‌ای برای انحصار سلاح در دست دولت این کشور اعلام کرده و اولین شرط خود را خروج کامل آمریکای اشغالگر از خاک عراق دانست.
🔸
در این بیانیه آمده: حضور آمریکا در عراق باید تحت هر عنوانی پایان یابد و حریم هوایی عراق نقطه‌ای برای حمله به سایر کشورها به ویژه کشورهای همسایه نباشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/458867" target="_blank">📅 19:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458866">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYTbgsC4s7gXkGgAUGkm0dKinuIJoFT5t1Xm0f-XYX3I_HbwOBI0XqKqA_WMbdNR8eVpgRM5CJ9ngEXXn5gzzihi2mXj_CtoWjbUYfoszwAT2h2Ojjd8p58qWBDW954-uKjjMm3W-D8N2-K-v1Nc9xQGi_gJNLS2PeTljfbiQBNCUkf4P2k3agjLIxw-vbHQDi8PX6G2k-f0LAJcVFUqGEvmn8Ee8zAl_jr75E34bzYkPTp1iRWOdwodn91hFHs_cXN1XiExEAhyDmFMYcfmqkX_5kSgVVu5UlSfIxUEAQc7bPER1uIpuUSTUWU6k9dIR85WcIqeHvLlQL84iHOUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوجوانان والیبال ایران قهرمان جهان شدند
🔹
تیم ملی والیبال نوجوانان ایران با نمایشی درخشان در فینال مسابقات قهرمانی جهان، فرانسه را ۳ بر یک شکست داد و برای اولین‌بار عنوان قهرمانی جهان در ردهٔ سنی زیر ۱۷ سال را از آن خود کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/farsna/458866" target="_blank">📅 19:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458865">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2dd9bc819.mp4?token=cJj-j7i9fewtEEREnp2d2y20CzZKgzU8CpdifGVn7SdqDhCu_xvwfiLc_RgxbJ6ViQJIimThCESL9xA7-TzkzKwSA6KWRs1pnvks8n6Q2Rq1Th_PhPo2UG39ZW6YI6hhfnk43ICqmK2f6lf6mIcu7QyQ_Clfeiec874wgesDzvDu5PcV-Cs63AMU5oCnE-aAmbgZ-vB81-hluatGV3vfFHaVuXgTY2LwEvZne4zKy_kUrAHDsALzshoo0ssJ5_BZN-BpKrLxf_FCJLgcZAve5M7c3lFp6qlN8JSS1B-p6oczZq1hB_EsZY6GWH-Hk0iU_EowvdBVnIX7l-DUCgoxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2dd9bc819.mp4?token=cJj-j7i9fewtEEREnp2d2y20CzZKgzU8CpdifGVn7SdqDhCu_xvwfiLc_RgxbJ6ViQJIimThCESL9xA7-TzkzKwSA6KWRs1pnvks8n6Q2Rq1Th_PhPo2UG39ZW6YI6hhfnk43ICqmK2f6lf6mIcu7QyQ_Clfeiec874wgesDzvDu5PcV-Cs63AMU5oCnE-aAmbgZ-vB81-hluatGV3vfFHaVuXgTY2LwEvZne4zKy_kUrAHDsALzshoo0ssJ5_BZN-BpKrLxf_FCJLgcZAve5M7c3lFp6qlN8JSS1B-p6oczZq1hB_EsZY6GWH-Hk0iU_EowvdBVnIX7l-DUCgoxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: بیش از ۴۰۰ دانشجو و ۱۰۰ استاد اخراجی را برگرداندیم  @Farsna</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/458865" target="_blank">📅 19:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458864">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e5aa60403.mp4?token=BFTTleeLkYYhz38_P6ni2qVBT1UBsqy7DgXLoVIMn0v2h7HOH6yCBXk0X9YQhp21sl58Lb29P4paE7nykdnhxHK6LTolJYeAIaXy0ImBXrxTB5gIGGkzCfb-KfNl-cNY2Ksv_QW8WG7JKOApSslCKf1B3wh7Hlduqx04t4mshvCbS_Fs8AT2FfNvEjAmNCkPCJ-59qkdOUgvtTd6ZCFgDC_2YZOf83viku66fsyKB8KS1H2mlW27eB3pVOiZdVty7ojDKasedB5-GVH5zkCJhiTsJJPLuisKOzxDyXne8SDRcUxhuiq_icKk_GZ56jahSyYuvcA9T83EHoB82uCdIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e5aa60403.mp4?token=BFTTleeLkYYhz38_P6ni2qVBT1UBsqy7DgXLoVIMn0v2h7HOH6yCBXk0X9YQhp21sl58Lb29P4paE7nykdnhxHK6LTolJYeAIaXy0ImBXrxTB5gIGGkzCfb-KfNl-cNY2Ksv_QW8WG7JKOApSslCKf1B3wh7Hlduqx04t4mshvCbS_Fs8AT2FfNvEjAmNCkPCJ-59qkdOUgvtTd6ZCFgDC_2YZOf83viku66fsyKB8KS1H2mlW27eB3pVOiZdVty7ojDKasedB5-GVH5zkCJhiTsJJPLuisKOzxDyXne8SDRcUxhuiq_icKk_GZ56jahSyYuvcA9T83EHoB82uCdIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل‌ اول پرسپولیس به ملوان با گل‌به‌خودی پاپی در دقیقه ۱۹
⚽️
پرسپولیس ۱ - ۰ ملوان
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/458864" target="_blank">📅 19:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458863">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a20cc457.mp4?token=Fjy1bANt5Qq-5ADxbxFa5MkOVQwJWDIZiNYzw_d71g1xkLJqNcpIzdZ-riS5Awp6FxQOISgXfJ_lE-YmLDqcu3ZZkdBkswJWBrpEDcolni2CMaxnJ6GjtcwJqqCgisHAH46YkqvtsMQ_KCieeLSnGYqGBgq9MQo5Fd88oR79Ayunaz9T7aRomNDDzuRdSTvKSHM7a5IhaAvei_1YuRzicnLZ7352be348o4DQGrxcjzuNTKBizbvL1dze48dRhExZ3IkS8qhZEfpn4eMpUAAAAuvMglGehWVtctUTXPyQS7cdTnPoyRHCzCxYqM3148kPL6wbfi-i2M8ZF0AvQ9UFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a20cc457.mp4?token=Fjy1bANt5Qq-5ADxbxFa5MkOVQwJWDIZiNYzw_d71g1xkLJqNcpIzdZ-riS5Awp6FxQOISgXfJ_lE-YmLDqcu3ZZkdBkswJWBrpEDcolni2CMaxnJ6GjtcwJqqCgisHAH46YkqvtsMQ_KCieeLSnGYqGBgq9MQo5Fd88oR79Ayunaz9T7aRomNDDzuRdSTvKSHM7a5IhaAvei_1YuRzicnLZ7352be348o4DQGrxcjzuNTKBizbvL1dze48dRhExZ3IkS8qhZEfpn4eMpUAAAAuvMglGehWVtctUTXPyQS7cdTnPoyRHCzCxYqM3148kPL6wbfi-i2M8ZF0AvQ9UFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر علوم: بیش از ۴۰۰ دانشجو و ۱۰۰ استاد اخراجی را برگرداندیم
@Farsna</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/farsna/458863" target="_blank">📅 19:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458862">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f035f9bcd9.mp4?token=tRxZYzHve3OOjwQyb1zotZv32kJZ9SzJbMkkaeGC5JDa_6zKENTjR-_opNEZP-gj24EFnEv2rlK9FT87zNbnyxpZyJPTLmJFSYM7bczI2i5Caf3xv8WAn2BoNPLL0hl1MTNPKZRV9ez_uCnQoFEkgX8L3JU59XyDEOpmSgPWhWt0gmzJjgLAg8p9YXcWcN63qeouZpCHENl-YYSdM8Dfx4BwZjAYLfkmayml5WwQSH1Xt55rylGsFdbsc-hd6woOefstJggClj6Z63miWsheaZOpK5qM1fhFu3igYZr2xIKFjGs7oYvGBGNM3m7WMT8ib40sZgRC_50--srtpZnI2gbxtOGVCatyqY-ouqNLh31Z7l0PAnCSLTjsvFY6bTMqZ-8yHiXoYlHNYXv1Nz7cVEMfIfJ6r-tzmiVIK308FvLSgt5LRWUceS-aG4WJ4F0DGcPRQXra8MnkSUDz7_3NWGvZvomMiNJK7C-F3W1TI736QifnMtxWlU3753OyhjuyIrfaokzORcc_Lz4wJSIflyXw0pw3EpC_XG8d4ubdGwbizuHk20pS1GanA5jmTCaa9GTeYdj-NXa4R69lBSlGBM8-nI2uRgf1nazPPfYw00VC-bAUiRgwiCUiPqsqAq4DG4nj8EKURmxrgjCeJo7C8JLAB2JpRSVKh7tTo5O0Ccw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f035f9bcd9.mp4?token=tRxZYzHve3OOjwQyb1zotZv32kJZ9SzJbMkkaeGC5JDa_6zKENTjR-_opNEZP-gj24EFnEv2rlK9FT87zNbnyxpZyJPTLmJFSYM7bczI2i5Caf3xv8WAn2BoNPLL0hl1MTNPKZRV9ez_uCnQoFEkgX8L3JU59XyDEOpmSgPWhWt0gmzJjgLAg8p9YXcWcN63qeouZpCHENl-YYSdM8Dfx4BwZjAYLfkmayml5WwQSH1Xt55rylGsFdbsc-hd6woOefstJggClj6Z63miWsheaZOpK5qM1fhFu3igYZr2xIKFjGs7oYvGBGNM3m7WMT8ib40sZgRC_50--srtpZnI2gbxtOGVCatyqY-ouqNLh31Z7l0PAnCSLTjsvFY6bTMqZ-8yHiXoYlHNYXv1Nz7cVEMfIfJ6r-tzmiVIK308FvLSgt5LRWUceS-aG4WJ4F0DGcPRQXra8MnkSUDz7_3NWGvZvomMiNJK7C-F3W1TI736QifnMtxWlU3753OyhjuyIrfaokzORcc_Lz4wJSIflyXw0pw3EpC_XG8d4ubdGwbizuHk20pS1GanA5jmTCaa9GTeYdj-NXa4R69lBSlGBM8-nI2uRgf1nazPPfYw00VC-bAUiRgwiCUiPqsqAq4DG4nj8EKURmxrgjCeJo7C8JLAB2JpRSVKh7tTo5O0Ccw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قیمت تخم‌مرغ از شمال تا جنوب تهران چقدر فرق دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/458862" target="_blank">📅 19:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458861">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX6l34KkhV6yQ91gUQPBjZdbxjpdR56tXNTd5jXncvDshac1fx-VtujbstaX_CiInhknLefOJ2v2OeH0iKJ5XZdOc9I8dEA5YtpPFo10B9SfDwSDpm6g4ZSX24N-K533ZYOJUGumUo2IuJYXnswqhK1dZ5CSYRdLjKzxWpM1Dwgk9q-4HMBMENSx4T_aQBrcBiAOkkIbYU4ImKTmTCwsqWpVAg1xBGt8F-KRjrayjatQNuhNyk2gMhhPjrSaapFPfR30iy5PGpz1sPbhWGTG4mZgCVG9XRobyaZLlrE_NB-X0uSHwx_xmXUNLo9FnbqV53A1rYteElceHWljuRmpTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احضار سفیر اوکراین در آنکارا پس از حملات به ۲ کشتی ترکیه‌ای
🔹
وزارت خارجه ترکیه، سفیر اوکراین را در پی حملات پهپادی به ۲ کشتی باری مرتبط با این کشور در دریای سیاه احضار کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/farsna/458861" target="_blank">📅 19:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458860">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0KzhZM6pE_EsjyR3jskVHGcsaQU-InesoSYwRH054KcHPOJ_NQFE--fdx8LnS_kro44vQlbyNRnj9mMzi6VU0IpeehdLXJh6ttXBjfZDw4mWdXfY23Ask1fR60uPoeihuVJWnpYzXsUfOiysUmxZofCYcKkFIEk7YygZQdvN4rSlH52luGCJi5J_zjofzL7K6cw4lfcvrC4iEI3ZQN9SJhMKluRvPViC3s73Sj3f-eY79WjG5YPWcfIu-bj84esjnJwRrM3UMw9E3oxQ7h1VjHbQPW0i-VNW9SZBksEzE0VpGmLvondXHHMBf1UCnxG5w7YTRq2vHpkdxTmreDmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶ ماه پس از جنگ؛ بلاتکلیفی و اضطراب به خانهٔ نظامیان آمریکایی رسید
🔹
رویترز: ادامهٔ جنگ آمریکا و ایران طی ۶ ماه گذشته، علاوه بر تلفات نظامی، فشارهای روانی و اقتصادی قابل توجهی بر خانوادهٔ نیروهای مسلح آمریکا وارد کرده است.
🔹
خانواده‌هایی که با طولانی شدن مأموریت‌ها، دوری از اعضای خانواده و نگرانی از سرنوشت آنها دست‌وپنجه نرم می‌کنند.
🔹
«کورتنی ساندرز»، مسئول شعبه شیکاگولند سازمان غیرانتفاعی Blue Star Families، می‌گوید خانواده‌های نظامیان با مشکلاتی مانند هماهنگی رفت‌وآمد فرزندان به مدرسه، جبران کاهش درآمد و اضطراب دائمی ناشی از دوری اعضای خانواده مواجه بوده‌اند.
🔹
رسانه‌های نظامی همچنین از افزایش تلاش برای خودکشی و کاهش روحیه در میان حدود ۵ هزار ملوان و تفنگدار دریایی این ناو خبر داده‌اند؛ ادعاهایی که پیت هگزث، وزیر دفاع آمریکا، آنها را «نادرست و تحریف‌شده» توصیف کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/farsna/458860" target="_blank">📅 19:21 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458859">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkTjI87G0b3rfoUhzhnHagpRuwTv7HmhxqNXneJ2u9wBON03M0EYf_Hvp1UjmpV6riHz97Dop0P06sAPPjO7fIdXdRSO2MRjzkxgAIG2cjBSPqmYCqEOkKPpSaOC-RRJN1MJbX667R9G1tpHYeQq_nxjdvQReJT8S0KOWq7Fu1c44f-dGuSQQJC_K9V3NVJFvYSagaAU_8VsxqBUEl7q0gRKJEJsYU9qjyTrcvKzKcEcvkSDY8-zojFoa4xoIMHbi6E3Em4sfwhVvDJib3U3aQcO1daSSNzs3pBzP-18eBvZSUcfLibeOSEy20_LYn-YQzY66QTVlI3EzXdReasppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
شخصیت هوش مصنوعی بانک رفاه کارگران رونمایی شد
🔹️
همزمان با مراسم گرامیداشت شصت‌وششمین سالگرد تأسیس بانک رفاه کارگران، از شخصیت هوش مصنوعی این بانک رونمایی شد.
🔹️
در این مراسم که شامگاه سه‌شنبه سوم شهریور ماه با حضور دکتر غلامحسین محمدی، سرپرست سازمان تأمین اجتماعی، دکتر اسماعیل للـه‌گانی، مدیرعامل بانک رفاه کارگران، جمعی از مدیران‌عامل پیشین و اعضای سابق هیئت‌مدیره این بانک برگزار شد، شخصیت مذکور معرفی شد.
🔹️
شخصیت هوش مصنوعی بانک رفاه کارگران با هدف معرفی خدمات، محصولات و ظرفیت‌های متنوع بانک طراحی شده است و می‌تواند زمینه آشنایی مخاطبان با خدمات بانکی، طرح‌های تسهیلاتی و ابزارهای نوین و غیرحضوری این بانک را به شیوه‌ای ساده و تعاملی فراهم کند.
🔗
متن کامل خبر...
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/farsna/458859" target="_blank">📅 19:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458858">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بزرگترین مجموعه بین المللی ورزش های ساحلی کشور در منطقه آزاد ارس افتتاح شد</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/458858" target="_blank">📅 19:17 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458857">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/458857" target="_blank">📅 19:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458856">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjZsCyy4Vrtx3MCaU9oVs6QEXl2iCN-Ttx6gHwocAkBdWzzdaKK0O4YPDWNsW1GnkyQdtHo8-8H4YRY0PfB1IJsdrvVYJbfZbz_B_-Lrzl1YrSvolpEPCjeP1rS_OqMwfxnsctnSoBz0-FPomgjMVC_1q-DID7-SJ6NtbOjC3nZ_v-VswgVzjqxhAFDX790bnnUrmbpeZ1CPHPDiuinliHao5ITwGVCAXp-7K4xuxu7Y9HYvgnV2FtsWEaSXztU-t78tW1g_M67FYX7eLOYLejbhN-yWj6C8lK3-MJMA_WQ6GSPiExOS-eCePXonsghFHmnhBUKgR3OGXWSFZZA1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاسخ قالیباف به ادعاهای گزاف مسئول برنامهٔ تحریم ایران در کابینهٔ ترامپ
🔹
قالیباف در پاسخ به ادعاهای وزیر خزانه‌داری آمریکا، مقاله‌ای از پل کروگمن نوبلیست اقتصاد را بازنشر کرد که در آن این اقتصاددان، دروغگوبودن بسنت و شکست خوردن مطلق او در مدیریت بازارها را شرح داده و از کنترل خارج‌‌شدن بازار اوراق بدهی دولت امریکا به‌عنوان سند شکست مطلق سیاست دروغگویی بسنت یاد کرده بود.
🔹
قالیباف در ادامه با تمسخر ادعای بسنت در مورد عبور ۱۳۰ میلیون بشکه نفت از هرمز طی دو هفته، به او گفت: ۱۳۰ های واقعی، ۱۳۰ میلیارد دلار هزینه‌های جنگ با ایران (به نقل از شرکت مودی آلنالیتیکس)، یا ۱۳۰ میلیون دلار ضرر برای شرکتی است که به‌طور مخفیانه به نیابت از دولت امریکا در بازارهای کاغذی نفت مداخله کرده و ایران از آن اطلاع پیدا کرده است.
🔹
قالیباف در ادامه گفت: ای دروغگو! به بازده اوراق خزانه‌داری دولت امریکا نگاه کن که آتش گرفته و دارد بالا و بالاتر می‌رود.
🔸
لازم به ذکر است که بازده اوراق خزانه‌داری ۳۰ساله آمریکا به حدود ۵.۳ درصد (بالاترین سطح از سال ۲۰۰۸) رسیده است. خزانه‌داری آمریکا تلاش کرده با مانورهایی، قیمت اوراق بلندمدت را بالا ببرد و بازده را پایین نگه دارد تا تصویر بهتری از اقتصاد و هزینه بدهی نشان دهد. اما بازار این تلاش را نپذیرفته و بازده‌ها مجدداً صعود کرده‌اند.
🔸
این بازده حاکی از آن است که سرمایه‌گذاران حرفه‌ای به روایت رسمی دولت و وزارت خزانه‌داری اعتماد کامل ندارند و ریسک‌ها را جدی‌تر از آنچه مقامات می‌گویند ارزیابی می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/458856" target="_blank">📅 19:14 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458855">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ موعود رسولان</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/farsna/458855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
خبر آمده پشت خبر، شده بتکده زیر و زبر
🔹
نماهنگ موعود رسولان با صدای حنیف طاهری
@Farsna</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/farsna/458855" target="_blank">📅 19:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458854">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نتایج امتحانات نهایی اعلام شد
🔹
آموزش‌وپرورش: نتایج اولیهٔ آزمون‌های نهایی پایه‌های یازدهم و دوازدهم اعلام شد. دانش‌آموزان و متقاضیان ایجاد یا ترمیم سابقه تحصیلی می‌توانند نتایج خود را در سامانه مربوط یا از طریق مدرسه مشاهده کنند.
🔹
از زمان اعلام نتایج، ۷۲ ساعت برای ثبت اعتراض و درخواست بررسی مجدد فرصت وجود دارد.
@Farsna</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/458854" target="_blank">📅 18:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458853">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">دیوار چین مانع فینالیست شدن زنان والیبال ایران شد
تیم ملی والیبال زنان در مرحله نیمه‌نهایی رقابت‌های قهرمانی آسیا و کسب سهمیه المپیک لس‌آنجلس مقابل چین ۳ بر صفر شکست خورد. ایران با امتیازهای ۲۵ بر ۲۲، ۲۵ بر ۱۲ و ۲۵ بر ۱۹ نتیجه را واگذار کرد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/458853" target="_blank">📅 18:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458852">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e45864b05.mp4?token=Y0J0qcZUaQUSFw-ztOZt8o5iO4QZCMtJKQet6z5klunvUmv3IPUGIJzQSIJSh7XO44-H9QygrTrDUR5LyjHEPjlqcNXL_GOC3ARAKH1z28tkBsrAGirGoeM926L3YWbI2jVrPuKUpr5S1lyUjoAvlYhlY7qmXJMlX_s4QcH8rqXsbIZfsbaT7lCJu_jQJqauKLYNyXYcef24nGxWDTlpsHgYtwevuLG1oLz7fIsyXpXk3QJTH4GLXfPe00pT_fCIREgrkCT8ohKAs3wtFxP8xo1iYH6NIrE8fcX3uoY8O2QAh7qQ0_3oo6x9hXGQqzzOP4hAEm3KEs2BuyMGQIZTWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e45864b05.mp4?token=Y0J0qcZUaQUSFw-ztOZt8o5iO4QZCMtJKQet6z5klunvUmv3IPUGIJzQSIJSh7XO44-H9QygrTrDUR5LyjHEPjlqcNXL_GOC3ARAKH1z28tkBsrAGirGoeM926L3YWbI2jVrPuKUpr5S1lyUjoAvlYhlY7qmXJMlX_s4QcH8rqXsbIZfsbaT7lCJu_jQJqauKLYNyXYcef24nGxWDTlpsHgYtwevuLG1oLz7fIsyXpXk3QJTH4GLXfPe00pT_fCIREgrkCT8ohKAs3wtFxP8xo1iYH6NIrE8fcX3uoY8O2QAh7qQ0_3oo6x9hXGQqzzOP4hAEm3KEs2BuyMGQIZTWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نفت: اسنپ گاز در راه است
🔹
همان‌طور که پلتفرم‌های حمل‌ونقل توانستند ساختار سنتی این حوزه را تغییر دهند، در حوزه گاز نیز می‌توان از ظرفیت اقتصاد پلتفرمی برای افزایش بهره‌وری استفاده کرد.
🔹
تا روز گذشته ۱۰۲ قرارداد تجاری در ۲۹ استان کشور منعقد شده که برخی از این قراردادها به‌صورت مشترک میان چند استان بسته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/458852" target="_blank">📅 18:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458850">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ba4a21fbd.mp4?token=sGn3rSah-jsRl_kUYvC1k0NWJy6JIFchjwy6TULtm4AcG-qLpdN_YtitUaYsI0jvOkhWoYYTY9ifaloIOYNFV3CShhHHeG8wTzatA1wESjazdzw78b_enmlHveqzG6Mqwu_1B-J9IwEg-UC_4muRClSuCthmtp4tmCJA6gjvKqe5fvGf5gRHgvVCvxcR6yRb3qF0KCD_83jBBOk2c1g_-Xd1OEv69juInkzZC9oHTRDoeBs4HxaHjsjkn9h1gZ9g0A1RyzfNhzOU9faEpdhtdp6WQah5wdLWsLvbxD7wb6iP0-fF67mQeGQZkAgleyxLNBG6LqbLC6Qbrqo1hBmHGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ba4a21fbd.mp4?token=sGn3rSah-jsRl_kUYvC1k0NWJy6JIFchjwy6TULtm4AcG-qLpdN_YtitUaYsI0jvOkhWoYYTY9ifaloIOYNFV3CShhHHeG8wTzatA1wESjazdzw78b_enmlHveqzG6Mqwu_1B-J9IwEg-UC_4muRClSuCthmtp4tmCJA6gjvKqe5fvGf5gRHgvVCvxcR6yRb3qF0KCD_83jBBOk2c1g_-Xd1OEv69juInkzZC9oHTRDoeBs4HxaHjsjkn9h1gZ9g0A1RyzfNhzOU9faEpdhtdp6WQah5wdLWsLvbxD7wb6iP0-fF67mQeGQZkAgleyxLNBG6LqbLC6Qbrqo1hBmHGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان ثبت احوال: تا ۲۰ روز آینده «کیف هویت من» که شامل خدمات بدون مدرک هویتی است در سامانۀ سهیم برای همۀ مردم بارگزاری می شود.
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/458850" target="_blank">📅 18:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458849">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b00b02f4a4.mp4?token=s-eMtXniAItMyH_Hv46w7zL7Gmm9Z7VkmK7ia9vwJlPYc_b-UX6NP7bjGO38t0OeJmUuvriMR4SDKKZ5Tq4G_3BRN8disRzkA6_wfpn4gG7F3dRAszF-gswND8xNhGogJ1kWIexYz3NjRoTbFJ_Ume9CwjyH2Kw0mV0iB7GhCBcUt-HDs775y6cZUIK0IRMtL1O5wAXqWiOyB7iH2xKse_eu5tEt9EH8oR1sG7W_Im7nEaXvacdG5wRrjCdcysZHCNRbsPwjuhOCBG1AmFuF7fO8r10L64C0SQ7B7M80E1ZPwqaGgieBWwDLVIiqE_EvxEhMXbAW1XskReW9aROtbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b00b02f4a4.mp4?token=s-eMtXniAItMyH_Hv46w7zL7Gmm9Z7VkmK7ia9vwJlPYc_b-UX6NP7bjGO38t0OeJmUuvriMR4SDKKZ5Tq4G_3BRN8disRzkA6_wfpn4gG7F3dRAszF-gswND8xNhGogJ1kWIexYz3NjRoTbFJ_Ume9CwjyH2Kw0mV0iB7GhCBcUt-HDs775y6cZUIK0IRMtL1O5wAXqWiOyB7iH2xKse_eu5tEt9EH8oR1sG7W_Im7nEaXvacdG5wRrjCdcysZHCNRbsPwjuhOCBG1AmFuF7fO8r10L64C0SQ7B7M80E1ZPwqaGgieBWwDLVIiqE_EvxEhMXbAW1XskReW9aROtbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ اخیر به جهان اسلام درس ایستادگی دادند
🔹
اینکه مردم ایران در مقابل ظلم ایستادند،  درسی است که در جنگ اخیر به جهان اسلام دادند؛ مردم ایران ۴۰ روز در مقابل بزرگ‌ترین ارتش ظاهری دنیا، در حالی که ارتش‌ها و کشورهای دیگری نیز در کنار آن…</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/farsna/458849" target="_blank">📅 17:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458848">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d96339666f.mp4?token=jenteTuh8PHQ5qTnN5xvFpjI7guiYXuvyjJ5AUBWlV4IHzD7UwyLb6qUltNzwKAONV95lz6WYif0ouB_ZaC8aYeYgiiGoz0L9H9gPtUTpZZX-kylbRrW5KgwUx3HuOrVGbnxXz7aWsiHvRTQvfrbphUXW2zqxqYMG25-tSRprzXIgEOM_72U3sM9pWPiYWNSkDi-G1gAh-1ZMK_6KWMbOuB3XWRKv0JdeLG1db0NPf_DlQ5mXYkWZQ2Mbkr0wjUgVYMRmXHi3JS83cc9l15QGvGg2oKgPo7mvz-qag77fRUrXhVpppd_CyuU9L2a7iU_REYyTupDUXNMncGeDpXnvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d96339666f.mp4?token=jenteTuh8PHQ5qTnN5xvFpjI7guiYXuvyjJ5AUBWlV4IHzD7UwyLb6qUltNzwKAONV95lz6WYif0ouB_ZaC8aYeYgiiGoz0L9H9gPtUTpZZX-kylbRrW5KgwUx3HuOrVGbnxXz7aWsiHvRTQvfrbphUXW2zqxqYMG25-tSRprzXIgEOM_72U3sM9pWPiYWNSkDi-G1gAh-1ZMK_6KWMbOuB3XWRKv0JdeLG1db0NPf_DlQ5mXYkWZQ2Mbkr0wjUgVYMRmXHi3JS83cc9l15QGvGg2oKgPo7mvz-qag77fRUrXhVpppd_CyuU9L2a7iU_REYyTupDUXNMncGeDpXnvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: مردم ایران در جنگ اخیر به جهان اسلام درس ایستادگی دادند
🔹
اینکه مردم ایران در مقابل ظلم ایستادند،  درسی است که در جنگ اخیر به جهان اسلام دادند؛ مردم ایران ۴۰ روز در مقابل بزرگ‌ترین ارتش ظاهری دنیا، در حالی که ارتش‌ها و کشورهای دیگری نیز در کنار آن قرار داشتند و از آن حمایت و پشتیبانی می‌کردند، ایستادند. این مقاومت یک شگفتی بود و مردم ایران با ایستادگی خود درس بزرگی به همه دنیا دادند.
🔹
وحدت جهان اسلام را در هر شرایطی دنبال خواهیم کرد. عربستان، مصر، ترکیه، پاکستان و دیگر کشورهای اسلامی، خانواده بزرگ جهان اسلام را تشکیل می‌دهند.
🔹
اختلافات وجود دارد و حتی ممکن است اختلافات جدی با کشورهای اسلامی داشته باشیم، اما باید همۀ این اختلافات را کنار بگذاریم تا جهان اسلام بتواند در برابر زیاده‌خواهی قدرت‌های بزرگ بایستد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/458848" target="_blank">📅 17:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458847">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">🎥
تصاویر بالگرد چینی از  سرچشمه سیلاب مرگبار در مرز چین و نپال
🔹
یک بالگرد چینی خود را به نقطه‌ای رساند که در آن
یک یخچال طبیعی فروپاشیده و حجم عظیمی از آب آزاد شده بود
.
🔸
این حجم آب با حرکت به سمت نپال، خسارات گسترده‌ای بر جای گذاشت.
این پدیده که به آن
GLOF (سیلاب ناشی از طغیان دریاچه یخچالی)
گفته می‌شود، یکی از خطرناک‌ترین پیامدهای ذوب و ناپایداری یخچال‌های طبیعی در مناطق کوهستانی است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/farsna/458847" target="_blank">📅 17:42 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458846">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhwWhbnacqHzjb4CObCGNiso97Wa5Yq00Vd9m8QOUAf363FPOLLg2K31-v8eKggHOdVArpBY8nu3tCf-jyvWSwSfatAmQ4IRxfa4OX3a24w1zXPLDXVeaojHphkU5CKvOxaZAGgbLQ_PHDkyg8bcFxYRYlmSUF0V0D9R7caTZoTk99P0CoDW_rpe-bzaoGGe4xw-FnwKjhZr-IEQMVFLhD7sHwYbrrNifg_4fwCcNU6ZMLSHmwtPAK-Wiz1S99KuR2Z0Jde5BBswpI11qdEe5LUxPXxDeh0Ue_3Ow6PCphAPEqBu48nYy2ISdnzUzOzM7_U2q0W9fDA1MuXoygIY2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناموس اقتصادی ترامپ تحت فشار جنگ ایران
🔹
رئیس فدرال رزرو آمریکا می‌گوید که تورم همچنان بیش‌از حد بالاست و احتمالاً بانک مرکزی در ماه‌های آینده مجبور خواهد شد برای کاهش آن، نرخ بهره را افزایش دهد.
🔹
حساب امریکن اکونومی نوشته است که «نرخ بهره ناموس ترامپ است» و افزایش آن یک عقب‌نشینی بزرگ از سوی او محسوب می‌شود.
🔹
هم‌اکنون آمریکا تحت فشار شدید افزایش نرخ بهرهٔ اوراق قرضهٔ خزانه‌داری قرار گرفته و سقوط ین در ژاپن نیز بر این فشار اضافه می‌کند.
🔸
روند طی‌شده درحال‌حاضر مشابه اتفاقات پیش‌از بحران مالی بزرگ ۲۰۰۸ آمریکا است.
🔹
طبق ادعای بلومبرگ در ماه گذشته، ورود غیرمحاسبه‌شدهٔ آمریکا به جنگ ایران فشار اقتصادی بر پارامترهای اقتصاد کلان ایالات متحده را به‌طرز قابل‌توجهی افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/farsna/458846" target="_blank">📅 17:36 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458845">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWCLZoiPOdFMgB40SBJdNilSDDbl_E4QD3T4-rjP4iklcU3H9MvLTZuC52UW31UVQWmWL0ziPochSMPwEEdjVnjkFj79sjlX3ej4sY1ch4dZZM4v8o36yuDZxR5b7laFTJ7XHMK_pkDtL42t0lk468M2AGRdhSyRLRlc32_qfeAxZr18Ed9d4moim2yCb-3IE4EjKpGEmeoex8Piq4SyWxRha56z44Qiz7OTh54IKvvCpNtr8E4HTpVXT1Zg5FV1OIn2WdvcQA0g-5t7SFvlXyOmnGnAFAtArDzDNBzxm9nWz0ODYkP4i-nbui3ltlZyaaDjXb05qL08SazgUv53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفر ول کن؛ روایتی از یک اظهارنظر جنجالی و پاسخ به آن
🔹
ساعاتی پس از آنکه محمدجعفر قائم‌پناه، معاون اجرایی رئیس‌جمهور، در اظهارنظری بحث‌برانگیز درباره توقف غنی‌سازی هسته‌ای صحبت کرد، واکنش‌های گسترده‌ای در فضای سیاسی کشور شکل گرفت.
🔹
این اظهارات که با جمله…</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/458845" target="_blank">📅 17:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458843">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZiM3q9hnYioplrIcidjzzeYCzTf6DTn2AbhKI63XLFPuO3n7C8OK3Komy7wuIZ2tTn8OOfatAzd7LVCok_wfhiFnS4193QM9IhqfLZKZt7jt_d3LokbXqa1uXnSEUHhpjsZzOb6sU6r8_9E1hRwGxKvSoplh0Bj_kj8o62Bwo-TMokZeGw9vxhx-ek0FC7hzJZ3jg9aJoYcXPZC6_kTWmyxsAqbCqaxzFU5KSpYOfpiH9DJCsXsIPNwLp9ekFN2kxqtEU95y5k3n52ch3Tcs99188xGDlVj6yvbwe-UkMXX3drEu67bviM2Ap4Oi-0u2fk5t9m1d9IKQpwzRctLQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cn1IZAuOmswCOdiMRMeghu1FUmywfTgn3W9BXp_iPzSu8BCHpT3v-pDKYksxJvM0f8do7lAkPOm0Bw_ECgUQyQe3ZydoML-u4p_LxGyj1OOcdtU990J_mFBukErBHKBH5Q0P7O6Rto4hGGai4sNRiWuunhOA2jkeQfsNASFuHPyvENk3M_bu0BNP0vJc-VckDRyvJJtArHy5K7MHULioeGpmo6LiAnRIUM2xUSN2x5N4b2HUVUr7gAs546JfUDZritBupnGe5WljKXGbSkXJ1-KbVUK162uetGosM4yw5vUIBmj75OVkgUP9-5cbMQ5SE-0ifUwbbJikJdRCWDssYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دو حملۀ هوایی اسرائیل در جنوب لبنان
🔹
منابع لبنانی بعدازظهر امروز از ۲ حمله هوایی رژیم صهیونیستی به شهرک المنصوری و همچنین یک حمله هوایی به منطقه وادی الحجیر در جنوب این کشور خبر دادند. @Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/458843" target="_blank">📅 17:28 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458842">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سرکردهٔ شبکه تراستی با بدهی ۷۰ هزار میلیارد تومانی دستگیر شد
🔹
مرکز اطلاع‌رسانی پلیس اعلام کرد «الف.ل»، از سرکردگان شبکه تراستی که طی سال‌های گذشته مبادرت به دریافت ارز حاصل از صادرات کرده بود، توسط کارآگاهان پلیس امنیت اقتصادی فراجا شناسایی و دستگیر شد.
🔹
براساس اعلام پلیس، بدهی این فرد به شبکه بانکی کشور ۳۰۰ میلیون یورو، معادل بیش از ۷۰ هزار میلیارد تومان است.
🔹
این فرد تاکنون از اجرای تعهدات خود امتناع کرده و متواری بوده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/farsna/458842" target="_blank">📅 17:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458841">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJqpTMFaUUxkqm8mFoImJxLQCltEZPDffYpk4aUFjhpMjhoiwALmJFZVnamzlRJPnLlBrbQI31mS6ppd-4fV6XJa0HhNqJYJWNugjM19rIa-qOdr5_WCCxlQfKcFryhfVaOmNFvysFLgPGsFqzmIV-S70t68vEJ3QkjSeVp9ks3M4Lir5DQqDAhxaI37iSqfay4s_mQgKmR0Gr23eInN2Abo0BAm4EZJ7SoZIpapZ54-QfePzjE8nRLPVH-Hd2yi34FoZ-lbpd0N6V9ZX4jGxt15_SFwDJXt5El87V07FuUCklblqaUaaeH7ta4TYY-BtEgM-YDzFOuRk8iqOzcIVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلایی که ترامپ از آن می‌ترسید، سرش آمد
🔹
جیمی کارتر، رئیس‌جمهور ۴ دهه پیش آمریکا بود که ترامپ با تمسخر ضعف‌هایش، برای خود در انتخابات رای می‌خرید و می‌گفت که نمی‌خواهد شبیه او باشد. دو ضعف بزرگ کارتر که در تاریخ آمریکا از آن یاد می‌شود، عبارت‌اند از: «شکست در جنگ با ایران و تورم برای مردم آمریکا.»
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/farsna/458841" target="_blank">📅 16:59 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458840">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHLlFKBzJJZSArPr2AtFeH1X8RYpueAUULjnwS-Q0SskVc1cjgX6YO1rrcwR8HbgVWXvqIf-gz5BqYpvFrKrQkLJYJK30UGZ5CmG57D4udqq_-_tP7xn5vyNiRelomcN7QylzhPazMJU2Gm2G-q5QqigFR2AtgDTubShWo6ict1vAuj_L4U_HqcqWczvN1p3HyIQPOlvdOcmNon0D17_0ufT5IStNL9XSUhn2cmcOWkgwA2HB65OElis4j4yUkrfy4ZLf4zeK4oBbjG8PaRejOaYghdOha--DZMLjYDu85jbxgrXciITDrYyDVolpRulNkF5iTvGazxGiKaS95biKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف ۲۸۰۰ مگاوات مصرف غیرمجاز برق در کشور
🔹
توانیر: اوج بار مصرف برق در تابستان امسال نسبت به پیش‌بینی‌ها ۳ درصد کاهش یافت و حدود ۲۸۰۰ مگاوات مصرف غیرمجاز از شبکهٔ برق کشور حذف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/farsna/458840" target="_blank">📅 16:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458839">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">قالیباف: ثمرۀ وحدت چشاندن طعم شکست به دشمن بود
🔹
پیام رئیس‌مجلس به‌مناسبت هفتۀ وحدت: ایران اسلامی، سرزمین همزیستی برادرانه اقوام و مذاهب است امروز وحدت شیعه و سنی در ایران، نه یک شعار مناسبتی، بلکه یکی از پایه‌های اقتدار ملی و یکی از سرمایه‌های بزرگ امنیت و پیشرفت کشور است که نمونه بارز تحقق آن در جنگ های تحمیلی اول و دوم و سوم و ایستادگی همه ی مذاهب و ادیان در چارچوب ایران عزیز در مقابل دشمن بیگانه و خونخوار بود.
🔹
تحولات سال‌های اخیر در منطقه نشان داده که ملت‌ها و دولت‌های مسلمان، بیش از گذشته به این حقیقت پی برده‌اند که قدرت‌های بیگانه و دشمنان اسلام، نه قادرند برای ملت‌های منطقه امنیت پایدار فراهم کنند و نه اساساً اراده‌ای برای تحقق چنین امنیتی دارند.
🔹
امنیتی که بر حضور و دخالت قدرت‌های فرامنطقه‌ای بنا شود، امنیتی شکننده و وابسته است، اما امنیتی که بر اراده ملت‌های مسلمان و همکاری برادرانه کشورهای منطقه استوار باشد، می‌تواند پایدار، عزتمند و ماندگار باشد.
🔹
امروز نشانه‌های این بیداری را می‌توان در شکل‌گیری پیمان‌ها، همکاری‌ها و ترتیبات جدید منطقه‌ای مشاهده کرد. پیمان‌ها و ترتیبات جدید منطقه‌ای می‌تواند نوید بخش آغاز مرحله‌ای تازه باشد که همسایگان مسلمان به جای بیگانگان بر ظرفیت های خود تکیه کنند و به جای رقابت‌های فرساینده، مسیر همکاری و برادری را برگزینند.
🔹
ثمرۀ وحدت بین مسلمانان به‌ویژه در تحولات اخیر، چشاندن طعم شکست به دشمن و پیروزی‌های پی در پی با عقب راندن استکبار از مواضع و رویاپردازی‌های خود بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/458839" target="_blank">📅 16:46 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDlU53zqoQI7g0re8GGKTIGrQc4pMoSBb5BJTPI6-YQbh7GbGw9SuF4e1u-iPRuG_l2038bHWMuNwGHg3E8fxkHfq82ZLdF-1bICsB2BZ6CwFxSOb6G-149GzjHp4rROozdbUSdB_2pzR3O0_fJj0WOnY_4n2YxArhwFxwftLk5_qoI7slJZpErijd9D1u45ApDyNSy5j2yOmLyl79VC30hybWadsPF7jL7MgsvtgSlYnpbg8GFBcxZ5dGWNlKUI0GEXHMGsrGnCv-YE1cA0O2i6KJj-A6IWM22c7eVpoBzte-8vEsgwZCp1SIULVT2Dm6ZG6xaoQNiRC6ZUqMHCtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjSAsmFOc1l5ByO8YyUj_pRDY371O_axk0ursrlgC5PtvH3d2X2YmSBs_sJiQgh-TEIhyhDMVc0JSxHpK-pMrW8oYkL1cuknV1oWuou8CoscJsY617PJ_n1X_0VTH5N1B1B0ivMHqBOubF0pek9BNIJIUMjPypEERxDVWcAxvabqLkpFiIiGzZrqjetLijhBKcT_QBQtOVrtdvmNPgwnFcT5wAdhPKNlXMwShxznCFdTKo36FkDSjqMPdsP_C5jtF9P_IraWQtkBl9ssVBV3uxY-yRJSf3sah9by4qPTxYSw7rGnvPTZIOG0kXCP-LMjVx9N518hL0fAnM5zSa6YSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g9WacwXSs0-QO-TC9_vls688Z2sAMiplXA5ZpUNTXCvvrZ_ZRonuAwXLOnULwpT0-5VJM0ylKg-_Qyr9D3boOc5U50OWrjNwV_ng4Q_0JRUQilw3WA7q_d8Ihbljqy6cuMV2ga39oJ-kf-KNwADy-F7Hwe1pvB6mDk7ZhgtSqTH46e-l2-RmAt0_PUNRLrs5TRaYZcXe3VBhsmAXFVljYNTg9yQtEZJq9l6L59W3fcIMZhPX6oTcxbcLEz-tfHiG3Skuyi4tjqS06f2OcMgHz56Dab03A5i6BDTOrRj_onnPGGYWRkcCj5emtLZ6JxChIlfb6HXujHNnMrF6UwCwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
مطالبات مردم از دولت چهاردهم در سال ۱۴۰۵ چه تغییراتی داشته است؟
@Farsna</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/458836" target="_blank">📅 16:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هراز و کندوان یک‌طرفه می‌شوند
🔹
پلیس‌راه مازندران: ساعت ۱۵ مسیر جنوب به شمال آزاد‌راه تهران-شمال و جادهٔ کندوان مسدود شده و از حدود ساعت ۱۷:۳۰ از خروجی مرزن‌آباد به‌سمت جنوب یک‌طرفه خواهد شد؛ جادهٔ هراز نیز به‌صورت مقطعی یک‌طرفه خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/458835" target="_blank">📅 16:34 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دو حملۀ هوایی اسرائیل در جنوب لبنان
🔹
منابع لبنانی بعدازظهر امروز از ۲ حمله هوایی رژیم صهیونیستی به شهرک المنصوری و همچنین یک حمله هوایی به منطقه وادی الحجیر در جنوب این کشور خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/458834" target="_blank">📅 16:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5EurF7KslyaqTzIpv4Zy-0sdEqTJHUmj32DvAUHgW47TaCIEMTG5i_x4CK20Vmfq75GK7f2r5Y95cIIaoVJAPAQfXRU8f8_u8I1GpldcCZlurZkfot5dd9bI01343UU80ClnYKfHCqy3fH6FNFFWm18w-K0xJrIOn9D1zcqAbjo4hVv-csEKs-EuqTsLBVBxc61qW-fl2kik0wOa4bOWsHJTAPjU-N4T3urLd6H9pzSZhnf4z3yXh-JZuRSYFIY43k3jMaP78qO3tPl8tHVAjw6zd-exASh_GTmieC076hrOcjjoqCxhnrMbgWI1BnGgZXgouYbqgSb_g3t9NYyhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران از سه‌شنبه خنک می‌شود
🔹
هواشناسی استان تهران: از روز سه‌شنبه شاهد روند کاهش دمای هوا خواهیم بود که این روند تا پایان هفته ماندگار خواهد بود؛ تا روز دوشنبه وزش باد نسبتاً شدید خواهیم داشت.
🔹
احتمالا بارش‌های پاییز امسال در کشور بیشتر از نرمال پیش‌بینی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/458833" target="_blank">📅 16:11 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJGf4ZEZyBEM7LDPOw2EwTopeP43p82WOJGrPFjZvRYM7JeCYJGkbHew-fJSXuc3rtmHtPxkCgc9t3y5DHyRW1Dn-UplnyGq4NXh4_94jb4XCVwkHkjh04eh9my5QYN9tkJkOcJFMdwVThzxNp0I_hkPVf1MXEcMFOe0wA_qCToeXAHAzSmknSx9eweuIB22NAmAY2BNswT3EfwS0J96Eooac3xJflzpbUNm2DKqb_J5KcJR51o76W1GrT-c6rZyCXMnr_TzU8IhqTVl3BbtvjNpk7RltbXA_7smdXQThCujwDC3zUleiLxAOzQ3yiULxA5y39PFtVI2Ke41gEaGuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: از ساختن قدرت دفاعی ایران دست نخواهیم کشید
🔹
سردار ابن‌الرضا: از ساختن قدرت دفاعی ایران دست نخواهیم کشید و برای تحقق ایران قوی، از هیچ تلاش و مجاهدتی دریغ نخواهیم کرد.
🔹
جنگ‌های تحمیلی اخیر به ما نشان داد که ایران قوی، ایران همیشه آماده است؛ ایرانی که باید همواره توان خود را افزایش دهد و برای تهدیدهای امروز و فردا آماده باشد.
🔹
ما در این میدان آموختیم که نباید به داشته‌های امروز اکتفا کرد؛ باید هر روز و بدون وقفه قدرت‌افزایی کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/458832" target="_blank">📅 16:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab0b30a060.mp4?token=HDdXqeTwnN8f2RaFinywZHElIeHL0HQGcZCZuEVdtzdLsHHMTk-Z_1WHgVnEA0QqApGyt5VqXEcxXaKOYtNn2OfW8yA-XzXt0C_gibOcc2fxWfGJb3xjIVVSb8EibkKhaxwi8eO1nK8z3Czx1yfHC2_i12GqIwmxNONmmEbpiplPqZ__41Rc-7fg4XJrYtMksVje95eUAcz4AHS6w9oijW7itSNiwmS6bzNANJziXaCUwH2CzfUpRNvfFKO9feskTe4SHoIUTyggW50woKzJ6F92GVNAevTK1_AU9P1QDxb7-8mRaDvezo1-MjKV_qa3dZzc2U2P-81lZSbw-2FnB3pKbcyK3iAlRho5J69LLgg-wXit-dUfwIKpjTtry1uPeQbPuVLKgbpWzvTBffBEnkHXuxnFAMfUKnVWzxc8RKGTzkrsIpMFuJ_0Ygm_k5AppmCuSoqJS7VFsvgKLU_EsBIol1csPfQefsD-fgocFPlp78TLJTmJN1uvVaGfgbtwsyE8s2XExoXKPnH8GBZQ6NWtofPxFotEKVP20nNFg42UAI6za1Q2rE352ODW7KAhbmhjpqq9E2_ics-xInbIBplTywAuI3CSKbJi0iQRBFiHliAqWcSwcRGgYXPxuOPFE-zxD82o0TyKKR22EZehWHYkCm4oVkuaVlu1wES7brM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab0b30a060.mp4?token=HDdXqeTwnN8f2RaFinywZHElIeHL0HQGcZCZuEVdtzdLsHHMTk-Z_1WHgVnEA0QqApGyt5VqXEcxXaKOYtNn2OfW8yA-XzXt0C_gibOcc2fxWfGJb3xjIVVSb8EibkKhaxwi8eO1nK8z3Czx1yfHC2_i12GqIwmxNONmmEbpiplPqZ__41Rc-7fg4XJrYtMksVje95eUAcz4AHS6w9oijW7itSNiwmS6bzNANJziXaCUwH2CzfUpRNvfFKO9feskTe4SHoIUTyggW50woKzJ6F92GVNAevTK1_AU9P1QDxb7-8mRaDvezo1-MjKV_qa3dZzc2U2P-81lZSbw-2FnB3pKbcyK3iAlRho5J69LLgg-wXit-dUfwIKpjTtry1uPeQbPuVLKgbpWzvTBffBEnkHXuxnFAMfUKnVWzxc8RKGTzkrsIpMFuJ_0Ygm_k5AppmCuSoqJS7VFsvgKLU_EsBIol1csPfQefsD-fgocFPlp78TLJTmJN1uvVaGfgbtwsyE8s2XExoXKPnH8GBZQ6NWtofPxFotEKVP20nNFg42UAI6za1Q2rE352ODW7KAhbmhjpqq9E2_ics-xInbIBplTywAuI3CSKbJi0iQRBFiHliAqWcSwcRGgYXPxuOPFE-zxD82o0TyKKR22EZehWHYkCm4oVkuaVlu1wES7brM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قائم‌مقام اعتماد ملی: مدیریت رهبر شهید عامل جهش ایران در عرصۀ نظامی بود
🔹
گرامی‌مقدم: اگر امروز در این نقطه ایستاده‌ایم که توانسته‌ایم مقاومت جانانه‌ای داشته باشیم، به این دلیل است که با علم روز پیش رفته‌ایم؛ چراکه کسی که دانش سرعت و دقت را داشته باشد، برنده جنگ‌هاست. و این دستاورد، جز با مدیریت دقیق آقای شهید محقق نمی‌شد.
🔹
زمانی که شهید حاجی‌زاده اعلام می‌کرد به دستاوردهای بزرگی در صنعت موشک‌سازی، سوپرسونیک و هایپرسونیک دست پیدا کرده‌ایم، برای من اصلاً جای ابهام نبود. بسیاری از افرادی که از این مسائل اطلاع داشتند، می‌گفتند با توجه به تلاش‌هایی که نیروهای نظامی در ارتش و سایر بخش‌ها انجام می‌دهند، این مدیریت شخص آقای خامنه‌ای بوده که به‌عنوان فرمانده کل قوا، این مسیر را هدایت کرده است.
@Farspolitics
-
link</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/458831" target="_blank">📅 15:51 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458830">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvuHMrSCPWWLzaG3Bmfs8kZ3_swfIImzI83ntESnTrM7RFAhc7oIQHYZ1FqTgkJnqQrKFdSsU5iJAzNACp8dy8VCGQW2ehN7xT4EExg68hKM2inAOyPel49c63bCYFMDzppNcwbTT4KkBjFMroMVoZjm0JFCus0ute9ji96r8od54Tl_YJxACe1Esygw1rRaaN0oRmYiPqiG4rhMJSYD0BRpYadpay-TCLkWm7OZ4QawvRK8GKAiRSIsIRJGv8JtRNqdqtffPO4zJKEvo5wW471yrLIt6op9yxEjHAHj5AXXnr5Rlo6fnjltIphlkqzofDugZv3aAy1Uf6ORO53Fzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تپش قلب و سرگیجه در تابستان نشانهٔ چیست؟
🔹
کم‌آبی بدن در روزهای گرم تابستان می‌تواند با علائمی مانند سردرد، خستگی، خشکی دهان، سرگیجه و تپش قلب همراه باشد و در صورت بی‌توجهی به وضعیت خطرناک برسد.
🔹
کارشناسان توصیه می‌کنند فرد دچار کم‌آبی به محیط خنک منتقل شده و در صورت هوشیاری، مایعات و ترجیحا محلول‌های الکترولیت را به‌تدریج مصرف کند.
🔹
برای پیشگیری نیز مصرف کافی مایعات، پوشیدن لباس‌های خنک و روشن، مصرف میوه و سبزیجات آبدار و پرهیز از تابش مستقیم آفتاب توصیه می‌شود.
🔹
در صورت استفراغ مداوم یا گیجی شدید باید فورا با اورژانس ۱۱۵ تماس گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/458830" target="_blank">📅 15:31 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458829">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1014363f0.mp4?token=bwBayn395G5uy-vwMm8Eei5GpTsRg8Wn6YQQJW3Jt96kpvpK3LJfjZCM1k_Qw8ih84jd4o4Ufm65fAxjCDHPHJcCEUEx0PQQvI2ralB57fdMRT0tMA8jtzQiCQUyVJSaW-Xjg-2Vrn2RGkTc9wfhZXto-ZTpU6kFqALKVwgeSTPEZyeQYtxOjKFyXeEmFP2eP4kEGf-2rL8d-jZ_vkDAqRSqpvy_TK2cz0eSvumrkSgU1ixvix7gwdWYbt9NG5amoCsHy47szBh0bmcTfIMoTVqpzdC0uIGzEunSMBDwV0TowLteExIqNukBpIHmGPPaG0Dxh_zzaGBqz277DLrw95rTteuEErFgohdTohLEcXP0yMBt0B1GWFUWrLDtYMcYfp2uKqrcmPE74kiEnjlXWXtQ65vijlMI_SmF4xHfK3Sppz1eKnuKrRvPTWX8k2OaeQDCB8ZjmnWYagPccJbugrGSR1lGUZVfivYvunHOyZT03-unS71EnghfmxGO8ecjxUB3xw9PRXqTL7HNoOZCaiTR-F3yPphVzJ8j8qMBn1dd6omXDJrUm8esaKkP8qhScG6Vn5Nv97i4oAB_-yOKvu5rUiJtTj05hVxGJV3VzcoXHAXHFnosK_uCk0xFZEN_EOIJi91D5Wbh46iJ_ttmTa45GORmYY-PDYntXEgJN5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1014363f0.mp4?token=bwBayn395G5uy-vwMm8Eei5GpTsRg8Wn6YQQJW3Jt96kpvpK3LJfjZCM1k_Qw8ih84jd4o4Ufm65fAxjCDHPHJcCEUEx0PQQvI2ralB57fdMRT0tMA8jtzQiCQUyVJSaW-Xjg-2Vrn2RGkTc9wfhZXto-ZTpU6kFqALKVwgeSTPEZyeQYtxOjKFyXeEmFP2eP4kEGf-2rL8d-jZ_vkDAqRSqpvy_TK2cz0eSvumrkSgU1ixvix7gwdWYbt9NG5amoCsHy47szBh0bmcTfIMoTVqpzdC0uIGzEunSMBDwV0TowLteExIqNukBpIHmGPPaG0Dxh_zzaGBqz277DLrw95rTteuEErFgohdTohLEcXP0yMBt0B1GWFUWrLDtYMcYfp2uKqrcmPE74kiEnjlXWXtQ65vijlMI_SmF4xHfK3Sppz1eKnuKrRvPTWX8k2OaeQDCB8ZjmnWYagPccJbugrGSR1lGUZVfivYvunHOyZT03-unS71EnghfmxGO8ecjxUB3xw9PRXqTL7HNoOZCaiTR-F3yPphVzJ8j8qMBn1dd6omXDJrUm8esaKkP8qhScG6Vn5Nv97i4oAB_-yOKvu5rUiJtTj05hVxGJV3VzcoXHAXHFnosK_uCk0xFZEN_EOIJi91D5Wbh46iJ_ttmTa45GORmYY-PDYntXEgJN5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تومُخ‌ترین پیامکی که برات اومده چی بوده
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/458829" target="_blank">📅 15:22 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458828">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انهدام یک تیم تروریستی در سراوان
🔹
نیروی زمینی سپاه: یک تیم تروریستی که قصد انجام اقدامات تروریستی بر روی اهداف از پیش تعیین‌شده در جنوب سیستان‌وبلوچستان را داشت، به‌محض ورود به منطقه مورد ضربه قاطع قرار گرفت که منجربه هلاکت یک نفر و دستگیری ۶ نفر اعضا و پشتیبانان این تیم شد.
🔹
از این تیم ۲۰ بسته مواد انفجاری به‌همراه متعلقات انفجاری، تعداد زیادی سلاح جنگی به‌همراه مهمات و وسایل ارتباطی استارلینک کشف گردید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/458828" target="_blank">📅 15:10 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458827">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNRSGnjhUcXfv_hpa_uaOY6hmkdVfsrzUBUjw_Jx4eQuDXrGF4mTCYiJJ_CLqYpjpWuCosShxKiRBEtoSW4kbMAs8dDxLhI-nf7ydX4LpKzU0K5cS-49sCSBhvmN5SkrxN6S86YBUWHjkVHcq5-EOcCoVh6aomevgwexRvQeyWXESoxzSzqITYLG5qMVATTcRiQCZbD_p0xDLNc-7toFnzfxCVf6NfV_pEmGMh66h7XQ5iMuYtlJnuMGNf_kCJy1NpXKKXI2Jz9NoJ7gWJov7MObQpggn77y-Onzai6uN5UiR9-Hyyk_S2oPyo-0snE2FYiAIfY47nRwxM1rWtiYow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید گوشت قرمز به ۳۷ هزار تُن کاهش یافت
🔹
براساس اعلام مرکز آمار ایران، در تیر امسال حدود ۳۷ هزار و ۳۱۲ تن گوشت قرمز در کشتارگاه‌های رسمی کشور عرضه شد که نسبت به تیر سال گذشته ۶ درصد کاهش داشته است.
🔹
گوشت گاو و گوساله با ۲۱ هزار و ۶۹۹ تن و سهم ۵۸.۱ درصدی بیشترین میزان تولید را به خود اختصاص داده و پس‌از آن گوشت گوسفند و بره با ۱۲ هزار و ۲۳۴ تن قرار دارد.
🔹
عرضهٔ گوشت قرمز در کشتارگاه‌های رسمی در تیر نسبت به خرداد نیز حدود ۹ درصد کاهش داشته است؛ البته بخشی‌از کشتار دام، به‌ویژه دام سبک، خارج از کشتارگاه‌های رسمی انجام می‌شود و در این آمار لحاظ نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/458827" target="_blank">📅 14:49 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458826">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-YpgFp9M_mflw0MK4irJaSvDGcwJw97dV8W76IC3ZAHgZKjqDfp1WOXCiA-ytabvgtIQL12CHVh46Dc0QDQUnZ-3VXFKDHOg4GpO4zG3aMu3st7AM-s6em352P_zi6AAfQ8C3PmbOridJrKj2ovZVJFDHgYRsHiJATgPabiXGr2xsLJTX_8bVAw5-4Qj1UuyGYnGf-J9huYqGGaSCOXLOcfiV2Q6A5pM2mqI57xbYnkCnang496e_Fdaw-m6aaadvmlTOAQrVYCucyZ-pVKde2R8LkTBPB8uyhpfT19pJNRpHhAzzxnKYdJMXisC65suBHww8avGE7dH8cZi6skow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
فرصت طلایی ورود به دنیای رسانه با ثبت نام در دانشکده خبرگزاری فارس
اگر رویای فعالیت حرفه‌ای در رسانه را دارید، اینجا شروع قدرتمند شماست.
✨
چرا دانشکده رسانه فارس؟
✔️
آموزش تخصصی با برترین اساتید رسانه‌ای کشور
✔️
کار عملی از ترم اول در تحریریه و باشگاه خبرنگاران توانا
✔️
رشته‌های جذاب: خبرنگاری، عکاسی خبری، سینما و تدوین، گویندگی، روابط عمومی
✔️
کاهش هزینه های تحصیل با کار و تولید محتوای حرفه‌ای در باشگاه توانا!  (مهارت و درآمد)
✔️
پشتیبانی از اشتغال و همکاری با رسانه‌های معتبر مانند خبرگزاری فارس
📌
شرایط ثبت‌نام:
🔹
ارسال عدد ۱۴ به ۵۰۰۰۱۰۱۴
🔗
یا ثبت‌نام از طریق سایت
futurix.ir/go/rxDxXO
🔹
پذیرش پس از مصاحبه و استعدادسنجی
🔹
ظرفیت محدود است!
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/458826" target="_blank">📅 14:44 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458824">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l41nlIrA7-PpMOwyyOAawzkh5Ip_5TV5IS79lMwkOoiOsxdhw7MrDluYYlKEFF3m1stL3eOlJCc0hAEUDYucA57XkIrsNSfpWbfn7DqwjRqIqGdcF018f3qdZsykd50voRF_z7GzsxVP4rOTb8B0aQzwGnr2WYzqsAjB8MLhdrOx1D6P_PCCEXH5s0_2pIY43XC-bCOG-MMd6SrfCAPl7iPqdqIlzGZetNbk4Jv87Mx7IBFWX4f7wGCoqHkU8o5oO2g2kRXIEpDBRGwMeYPJwTPfTmOut7yRWMjJW84pd2GG4gJ5lCTtepld-fCNJUFpW6uE8vbrKxYTTReaj60SCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BJOAjDktCZgUPg0Fw9EJTX3dfYRW-79dMvilwS3n2nICps47kifdbV_EDUB7LxEBcMK2dNYw3IcexN7dB1Xu1fVbsYs5fl5jMfkVBwOqe7pa3hnXCXOoM0ORXvS95nxI3TsyHlW0w81o1L1emAPE1b35y3q0jlzsgy1ss8HT30-PeU2HzupxU5g304ZAgk_t7Me_9Zs9m49v434tfk1moT8OpX4xYyvYtIPLFZ96j8wxgmIfNJ7L6kdc9Upfv24ZTKoKSx-Rmg2IBvxMd1w4Rxz83oQlBT3YIQSo2NmXHEGPWXIEeCf3DS5zg9XEnkqBq-do5sMJguJlszXWPkmRsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تاوان جنگ با ایران برای ترامپ؛ دموکرات‌ها در مسیر فتح کنگره
🔹
در فاصله ۶۶ روز تا انتخابات میان‌دوره‌ای آمریکا، برآوردها از شانس بالای دموکرات‌ها برای پس گرفتن مجلس نمایندگان و رقابت نزدیک بر سر سنا حکایت دارد.
🔹
بر اساس برآورد زنده بازار پیش‌بینی Kalshi، دموکرات‌ها در حال حاضر ۸۵ درصد شانس دارند کنترل مجلس نمایندگان آمریکا را در انتخابات میان‌دوره‌ای امسال کنگره به دست بگیرند، در حالی که جمهوری‌خواهان تنها ۱۵ درصد شانس دارند.
🔹
این بازار در حالی که ۶۶ روز تا انتخابات میان‌دوره‌ای کنگره باقی مانده، ترکیب احتمالی مجلس نمایندگان را ۲۳۱ کرسی برای دموکرات‌ها در برابر ۱۹۸ کرسی برای جمهوری‌خواهان تخمین می‌زند. انتخابات مجلس نمایندگان شامل ۴۳۵ کرسی است و برای کسب اکثریت به ۲۱۸ کرسی نیاز است.
🔹
بازار پیش‌بینی Kalshi در خصوص انتخابات سنا، شانس جمهوری‌خواهان برای حفظ کنترل خود بر این مجلس را در انتخابات میان‌دوره‌ای ۲۰۲۶، ۵۳ درصد برآورد می‌کند، در حالی که دموکرات‌ها ۴۷ درصد شانس دارند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/458824" target="_blank">📅 14:33 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458823">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/799a878717.mp4?token=k7b7tOwk4E81IAw_6GwNRxtjDtJz6Dz5Hm2rwNXvIXGjcZ6Mza2qTpRPm6RsM1-uw-_C3VXy_7SOD-DSE1WyT3dK8VvJ8YKlgHbut28gEyzkc87BaLyHGa0X6J7z-lat9kFya31Leg9xMpiMScoo6KiF8XTcUWQkLcMiZSOT6u13nwlraRmazUOXg7k_0FjGeFj8UPugEvAyph9m006Y-0XdsfrSGATlTPvMAUU1a18NiVMhM8Eby68CHlD9Ot3jixG_LWMbncuJ6T2R_oIRsY42bnGE7m1nkDSKtqya0U8OYgcIWpHWa_7dNGfznn6x_4iwzYm2LAK6Q4kyZC8NGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/799a878717.mp4?token=k7b7tOwk4E81IAw_6GwNRxtjDtJz6Dz5Hm2rwNXvIXGjcZ6Mza2qTpRPm6RsM1-uw-_C3VXy_7SOD-DSE1WyT3dK8VvJ8YKlgHbut28gEyzkc87BaLyHGa0X6J7z-lat9kFya31Leg9xMpiMScoo6KiF8XTcUWQkLcMiZSOT6u13nwlraRmazUOXg7k_0FjGeFj8UPugEvAyph9m006Y-0XdsfrSGATlTPvMAUU1a18NiVMhM8Eby68CHlD9Ot3jixG_LWMbncuJ6T2R_oIRsY42bnGE7m1nkDSKtqya0U8OYgcIWpHWa_7dNGfznn6x_4iwzYm2LAK6Q4kyZC8NGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: برق صنایع نباید قطع شود
🔹
برای عبور موفق از فصل زمستان و مدیریت چالش‌های ناشی از ناترازی انرژی‌، ‌‌باید به گونه‌ای مدیریت کنیم که چرخه صنعت کشور بچرخد و در عین حال آب، برق و گاز مورد نیاز صنایع تأمین شود.
🔹
تأکید کرده‌ام که اگر لازم شد برق دولت را…</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/farsna/458823" target="_blank">📅 14:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-458820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E6TqO40oqG95SyBUSBSfJN-7DwlzJ0MiF_1tt2M0CTDeBXIR13-QUycgiRkIcNdVppFNSJQk602lIK8Y3ZipwL0Gczza2Mn-ZZyicXd9QTVfTNGUQ9sScXk-HyMuorxwWaK440B24NJQGeMWjdCqJ82EttQtoJoaHm5j1UQYY2Kcu9i52kxpYVn5LU7J39iqOVXC-HViaGH-6QFQkhKkoG0h0OjsiKv-vIoRmLy76tLmMzejGPxpDj8w4GgiLruGtfmoUT9eMjiQ5fYjXWtC_Mnbl5cf7izxwe2KzkdglfVmd1LEkaDax-MSCM_gEi1A7oE8scHYi3qZqmsq_VV43w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYC9S7Ehgm6jFNh4FVXXZwMoAAaTJrCeK28i7NkBtwtsy2v63PbK36odc8V_DgiWl8rCuF4KPftwifISoaKzgeSmd1H-4ROubelpZnwUZj6jUQfo4Wzr2FKWF1cYZHxm2XERw2plPcdOUZhqAYMc3Du5qBsA9p1cHzBFCVVN6DbUa-XqoEdq18NNGZOAaY1Uxtmt3f7UVttbyB5q6FDFcK-46u3QZVRMwIVUbx37w0HXzavtr4Hgvpmn_u9o9ENDL3Apd8GD24gneLW5CKKsQNNYvtHwnk1dkgmx3L2sRIuJFnIeixK6Bo2o1jAh_w6a9uFZn2PwSg4xtYIuW2ALaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iVM43j46Xjl9xNEoZQRVqCUuO2Q7Qjb6t0ZwiNRZOfmAbWRNV_KPY97s3_6WXNXcKJJqKl_EUctvrltpGRH_4Gopc02-XFLr0mvp58cRmWqeIuF05VuudlVKgeayZ6czZQieqqH2GKIex-_1TUBB2S5cb6oSQGqSoenZJrweUUqkTPkRh_355_UoreflmkJVuxfxVJqs6tBMrctfHTKI0toz969JrB19P2iN1dta_81V2mZNxKTMIDSD08CKO7t2QItKrbpbYJ5NrfBsgV9oFCg5zWclcJNfepn7hOrc_q6_TyeBibMsy7onkT_6Tm3rTlvMNyOHaOe6u0FzCznBEg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
پل B16 البرز به بهره‌برداری رسید
🔸
این پل بخشی‌از شاهراه حیاتی ارتباطی میان پایتخت و پهنهٔ گسترده‌ای از استان‌های غربی و شمالی کشور است.
عکس:
نسترن کرمانی
@Farsna</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/farsna/458820" target="_blank">📅 14:19 · 07 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
