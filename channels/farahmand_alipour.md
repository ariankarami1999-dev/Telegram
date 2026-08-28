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
<img src="https://cdn4.telesco.pe/file/KBwFuk7Ors1l1F_jp4NJ6UUU7u7eizopNHPFRkACmANjHM0neF6_DkvJQsoXbe4j1hnEodB7S7rt5aMI5-Rd-sLmtdRH1gFf210VjIZMDVfs-xihL3R_F0F3qTRDwVhi9Zx-WKY61zyVXNwMnial3qDAVI2B_Vpro9P0k4kKvjSp6SwCQm5Kyy53VbX89X1dEokeqr6hgYlZvl3KXcgnZNwrtrh5YfU4keMvA-lU1zYfitJ70G4YNV7bdWvrBBt75GnWFOhXP8AIUwzp2zNSQz0uGsIUHDMW83w_OV77anvQDtE6eu_gh3c5IgR2i2JedGJvUjXAWJsr9SxA47XGlw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.8K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quIH2p7q7uulcZXVgtAlhTWLOd5ZQbOUNWCHjnd3E-by6S0gyNT6Vy5NNt4-z4ey-MQjYa1KcGPxu97YjtgKpnFTW8KqETX35tChW8eI2x2oMvoPL6sSjDV57iPpc2OKP91qs2fM3cSUppn4EVQ8_kH4NOpHe1Tyiy7VR0hxHuYeWGer3GX-tjBC6K6vd9XaboS3QX6sKENCV0KFjqu_tXdi75SJiUAu1G9jcC95RZXtKYnPqV7cTb2bHjy4LCKn96zdSSYsjFcBvB6A-VoC51OUpZd3OkThQFCG9xDQYHgeYkojvRAserijl1XmV0304WYGMQQK0xEYjMJjnT-pNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVD3RsqMQXKLNJGO0cFCbRLHgpABJoYJiBm8vqCN3-pYjofGxFAkHh8lideJDhfpIWJrPOydBADSAWa-3YYgn9gx-XTj5yVOQFvaLZTdteJm4KzjiszT3gOTF8EqntrpLz0R6o8DGbDCHPEkHQMLmcH81fOk_9I85RZnlEBJeukgsmAp9fBg8Iu3hidox4L_Ir-pSoWRvMdKOk83CgQtSW-QdJg33Ln2fsiuZmoUTJJ50SLhIQ6W_f1BAX1SfKJ_LeRsNvYViEYBy5p5jkT63R6_mOVFndeq2ayBFPxo-vPWRDIOpnV6ewfezN0A24viBTORQPAdl4vnK4-jdKc-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsm1E5iyIeqzTbEz6-q6LekU9vZVMTNoAf1weEyd67kY_UdxEQv9GDzU6CoJyglfn7yZYBDS3ruly_P2OCMMoVsE9YuaWzjZXGm9GBJfi1htvWJFvjTsWq5duELgPvriqgZPa3YLrec1Y1g6drvbhW_yGJA5rz-aqdIfO31q6r75-0G6oECbAtP6oJSkPM-UWmUllIcoRuEDTh3J26a-xIcsiM9CjgpUZ1UqS9YwfokwlSTvIqMbgSO6n2OX3SrIpnHiCF2ZpsncMmq0cEoTdBAJ3CziuzQZHYe83bF8vRuQ0fLVmIE0nfhkY75n92EVsFGQDzgoUW6buVJie5vfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuKOi6q8uhD8BHLQlQ1xEGE6A4m3A6wobbjT9k3DHiUZfzO249u9AXvNcBJVihG1oHXPtzlGr-9QUS5Gbchk_z0vwTfoD9bVqU61gjZhjbAU4jrf-YiOSY0v17SfahT7PsB0ckq4EIPru_I9HYpRkaSWZm0UAnhhOQecQmM5m_cxD4TImivTiq3MOdg5XHyxD3H5cSQOdl8YaP8OujBQW4exJ-d1qLn0KIup4t6-zD5PIonFT5rKMk8BLVLHJB0uMUWtcA3mjouGhDfOiZi5W9MhuqcbVhw2yrJJHttnopyqPLUX_YqRufpIGFHOCdctOw8wRf3wig8GJEDpDBVSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgy8AprIeayZF1KkO0YBzo9sy7Q4jiTrUVAJQ98BHuSx1pZNvsbvIPKfPmC9r1V3tAvptG5e8GQbmxo_S3ePe0NWniB7ILsYVWxFKPtktt3pZhcS1GnrUwqIJNc-PHVojh2IogOUjzcoRfHkHoaxKe50yvB0cXew6V9k6zGaMn-nbFkfUie7fixT0UoYQyt4LXVH1mbxLDlSmn8sBMGKilXFzsF9lq-eDKzHXL-6L0Ez18dNjY-ynhgIf_VquiyqZQ1R_bX2Vc5WR8tSumQP9Jr1U8wA7S5T3gLzXlJ2eXDvyBWhvYJk2wqymMevEiqGEVsS-coyBCLal_9JY0u-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/porOWLLrRtejVRKgoxaJ62Ujy_D9j8Zg9C-n7CeQ0kWzzDvmduVARexx1ztBjWGBHDGmn607COWHpcv4_VSOiucuh6kQQwFD5Y3N-XCdb6pX1vWDZGb_7BsciKs6NCLnNV8EtzVhEE-OtntdIGj-dG5id7OlnCg8RuxsCF3_ReKWrr-hJCWNpgk5XYGRuYMES4HZTfClpdhGDVWo5R2h2YzS-qNXYJZYUQlQZ9doBN4N8wukxVgQb9dWHUeHmNikszxhAIoJefXc4DxFyX6L37n7O_KHOhWMJrYslvjQKfmTaawxwbCbw0RZeNvVYHsIOaxzSTN4O6xXeiHHfKNwtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WjdPbyMKi7JhMZhuXugceKcqMsKszklly0h7CHtf1Gd7-MWWK_jZfMUgRte6-RjCGz695MMncJxqP7S5HCLOxZIO3dPz9a1x6lAVyuycmSLzVbPhW7icM152xqQL0sggfEUjytlSEh2K65Z2X_kcA5ESsofJIOAwybTu3nJji8W-M1B6GfwvBY7hFlYOznV8KKI0FZMny3i-ao4mcFT7_V_mUC5vTlO6Gd2cVFD_F2J5-4HuuRURt8OI_ChVyw4tLJQ1xTDRqQbLu71m6EfB8_dxfCVRE3lThXLDN5dfET7aIupiGsXe5wVcW9s5Do9orCK2SqzX9_VUuljlnaMKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=WjdPbyMKi7JhMZhuXugceKcqMsKszklly0h7CHtf1Gd7-MWWK_jZfMUgRte6-RjCGz695MMncJxqP7S5HCLOxZIO3dPz9a1x6lAVyuycmSLzVbPhW7icM152xqQL0sggfEUjytlSEh2K65Z2X_kcA5ESsofJIOAwybTu3nJji8W-M1B6GfwvBY7hFlYOznV8KKI0FZMny3i-ao4mcFT7_V_mUC5vTlO6Gd2cVFD_F2J5-4HuuRURt8OI_ChVyw4tLJQ1xTDRqQbLu71m6EfB8_dxfCVRE3lThXLDN5dfET7aIupiGsXe5wVcW9s5Do9orCK2SqzX9_VUuljlnaMKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpsPdZT9Whk9BFcMbcS6i4sTFuu1ZdRV2L_2WquOkcn1YCrrdmjlTx_lZcgxOQaKhcjCQmIYoMIVQNoS9lhAMaTM68sDs12DiJI6t_5iqeBXsFFssfU8KLZvPNsc2APLiUSHyecaECQXu5kiME4zG47knPuPcjPJdxNf6KaZ4zrwy6QRoYDp1fAp7FJgf0AgQxLWda82Vru538Za_fuGqt8Khkd2f5JFjKBRBc2R55C0iq5hguUGcsG4cre55dBZIjpejlHhVljQYejjS656_BlquIY-a8rgekEU9aIvNftr4VlJS9Yob3ASTFvKCBF3EZsTXUDvW-vphInqwPCXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=KktAqOHRmodfFw3FRcIqp8IObf0WRa2cxCB7g7XJOhI7DhMfJC0Mw267aNlRqe3WNyTaE8PmYaZ_vMgF7CewXzq1qDpY2emlIJg5hhCpMIHIxqKPJ8gcLC4qU3mp8CgNp0Z6tcL8Jmkh1iBjh1YJ1D9f4_clPFIj6iD-FQCVqAG1M0p4iCHpBAVrWBXsiJQtny230qX8gZExanqDPOOEjJA5GuhfN-46wJXPjxEXGj-CaSNLehmhLKMdR5KR3UOYrlwZwk4kt9kLua-K2fZXBtLZf2CIhqXLHNoTj_EFm0FYzZPAkYaqEXUXJTqXeyw4gd012RCECkAC9Phy5sbjLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=KktAqOHRmodfFw3FRcIqp8IObf0WRa2cxCB7g7XJOhI7DhMfJC0Mw267aNlRqe3WNyTaE8PmYaZ_vMgF7CewXzq1qDpY2emlIJg5hhCpMIHIxqKPJ8gcLC4qU3mp8CgNp0Z6tcL8Jmkh1iBjh1YJ1D9f4_clPFIj6iD-FQCVqAG1M0p4iCHpBAVrWBXsiJQtny230qX8gZExanqDPOOEjJA5GuhfN-46wJXPjxEXGj-CaSNLehmhLKMdR5KR3UOYrlwZwk4kt9kLua-K2fZXBtLZf2CIhqXLHNoTj_EFm0FYzZPAkYaqEXUXJTqXeyw4gd012RCECkAC9Phy5sbjLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=gHhDtDkoHgsoNszNqUwR85y1klPC4Vr6cCp9hdu8kuKXF93KZ5zoQsAREp6EZzX4DfmNaEBbg6k936J805Mnkg2Vdcccdm3Zcc9bE98ZiocBtqfy-ptvzDjHCNnygo8hwAnEo88oFpGymKdaO4ZqsEqKGczrr-305mvmaUl_z2yuvC22HA3-ke_mPLPQryjzVDpgOktbHns1411b6K3KnIwggnDiypSzpOCzzTNBQrdsX2Zg5XyPBsM_UDZAmC0vfR6wn4DYCLADi5cgQNro0E3e2LROq4yC0zIdMiU6fDhj_YGiLGSD4AeGUDT-u0jesI6489tiwgI4Q9VWv5KyVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=gHhDtDkoHgsoNszNqUwR85y1klPC4Vr6cCp9hdu8kuKXF93KZ5zoQsAREp6EZzX4DfmNaEBbg6k936J805Mnkg2Vdcccdm3Zcc9bE98ZiocBtqfy-ptvzDjHCNnygo8hwAnEo88oFpGymKdaO4ZqsEqKGczrr-305mvmaUl_z2yuvC22HA3-ke_mPLPQryjzVDpgOktbHns1411b6K3KnIwggnDiypSzpOCzzTNBQrdsX2Zg5XyPBsM_UDZAmC0vfR6wn4DYCLADi5cgQNro0E3e2LROq4yC0zIdMiU6fDhj_YGiLGSD4AeGUDT-u0jesI6489tiwgI4Q9VWv5KyVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NId5ZGOFUVccOd8FGOq8svPz-QmAqG19L7nsy7maDikLg0T0Igxak7SVEboRxcNOx6q17Rv0y8OZFck_iFj_YCtlcYxvfYpKARDl1e7xx0AfnE3ejniSBWzwq3cGo-DVCN6m89f7lo8xOs22GbERGsDi-IA894QxmNAzsbJvrNqbzzOQxwh1LrgOoKJtIWRc9yCaEJT8Nd_7uEYVsHvJai0NDMqY3pL9OGpgtx5cpnXWdB9KX8ogUi70UGgXPGq0Zs_VB365PcbWtq7hD0lxrRHN_LFq8JDrIE_UESqAkSVkWKQ5gdtbcGZy3puA1t4ZhiODgTQE_T6k0MPQ7hbTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o25CwgeweKnTGXL-uVZbHiK2GM1el8lNP_gCMKaRJLKMs7SA2F93hDmtk3GrCeJVFioDdzaljHnXc2DEEcd4NIhz64OnepaX8CYRsSDN7XmrCE-bigRmijelbd8FsKVQxFFBzOtb-Fw9QtIj2D8OSeFDe0VbCr35WtnzsJP0vCFaH-bow1-ptUmkg0qG_G4GmsRjkim5BVmYYLt47QTRn0Ip98yAvbEXPBzGICAbsZ7Pfh-krE7k9SCkraq3ZCskEq_xBtBGCkvISNkbqE8yHY04bPgWpOBNTLfI8MC_EMDnPCJcPZTzbJevN8fHAsuw97XtYcWqCFpFKHFuPM8IVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=XW8z6qu8Yl8CYmhzVfBIcahEnIwinmftEGi_OTmo9lhyq2fDakoi1rjIFOZ-SOl_BA1fQHXE64AP5WZ5xws4Oj7g9WaFSejfQZoty8OmKbK3FWR4S_pRSBWZaKfWCXmphuDErTtcIJTt3zeDJbQTNNKahubK0tiSSSaNXVOTPLr04ApgXQ3RnZoGulnL2GUeflJIq3lPnCsctHYE-oFccampDy3k0S1C0wWhWlocfPRP5PWM_0zbHKAq3cjSSjA0ugNbtWtNuCYHZVIiinBDudg1lEkpUF9oq0oHVZNdcBc79yBPHDlBJYy2nebOuIpUOxTHqoWxRxu4mt9qwNezG3dmqCh-riJ5NwezDdVKOva3DLjPYGigBrXWwoMPzH_RIuEJ7OMri5PyAqlHe6m6kDvV_HulHvFs2o-oe_2rDxShLe1qHpOT4lQBM05LhYF3O3zMhSkKM5UtMdUiVa-SoxqM_RKvV6npgJwP93KQfaXalXDouE7lHG-1vWNbA3iKih-fBt2oC5ooPcNlpjGyOfMWoQSbVA0J2EA3lV6lsFft1ef7nr4LVWO8yO8-U7nd8HgYLxH6fQ9EnXhnzHIAZ_AaK1xnGtbdtmE3S177PFHO6uYLEbxPbNqw_dqBKzVrubBOh-lbDKBmbTjpqCtYlgipT4s7sCxbW8IxSd3Wwwc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=XW8z6qu8Yl8CYmhzVfBIcahEnIwinmftEGi_OTmo9lhyq2fDakoi1rjIFOZ-SOl_BA1fQHXE64AP5WZ5xws4Oj7g9WaFSejfQZoty8OmKbK3FWR4S_pRSBWZaKfWCXmphuDErTtcIJTt3zeDJbQTNNKahubK0tiSSSaNXVOTPLr04ApgXQ3RnZoGulnL2GUeflJIq3lPnCsctHYE-oFccampDy3k0S1C0wWhWlocfPRP5PWM_0zbHKAq3cjSSjA0ugNbtWtNuCYHZVIiinBDudg1lEkpUF9oq0oHVZNdcBc79yBPHDlBJYy2nebOuIpUOxTHqoWxRxu4mt9qwNezG3dmqCh-riJ5NwezDdVKOva3DLjPYGigBrXWwoMPzH_RIuEJ7OMri5PyAqlHe6m6kDvV_HulHvFs2o-oe_2rDxShLe1qHpOT4lQBM05LhYF3O3zMhSkKM5UtMdUiVa-SoxqM_RKvV6npgJwP93KQfaXalXDouE7lHG-1vWNbA3iKih-fBt2oC5ooPcNlpjGyOfMWoQSbVA0J2EA3lV6lsFft1ef7nr4LVWO8yO8-U7nd8HgYLxH6fQ9EnXhnzHIAZ_AaK1xnGtbdtmE3S177PFHO6uYLEbxPbNqw_dqBKzVrubBOh-lbDKBmbTjpqCtYlgipT4s7sCxbW8IxSd3Wwwc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXHrppy6lWuh6WKzeyDBw1kz7_LyvnsxBne_oiZZLYIv2Gf5RRfrqbBRRvsIxZnA0DPn1JA4kQbtPVGoWGxqYN9MMsY5_4ZL7YgUU2ca_ztAAGABE0MBosQXjNAz5NiIYRXn0OABkVTN-n0d5ULheYYd--cg7wE-RGqVznaq7wzVvhH5T6sY9momi1zwu3kJrUk2rKy5jOFUdU-R9ieaMLRTi5x5csZsRFvEYeGoQDuhA4nnY-ySUez_B3n33uQxoS7rwzoum4Fz7diAaOxQuCpoIH5Pc-Gt9ZeLiTKW2a_4H1vjqly6nD8RO6wyLkNUDasJZ8zIpMnhXsh1-sinHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M5p7hP2xvISoeqiycekuChUKJPSD8IjDReAwuS-ymeQMdzwPJLY3X9Prt5vo6TbiOgzuc8RlsmMULhDZsaPWAC8VhKNQKCXwZURV_sxO1JgXMS6UAxng1UarmeG2J3QGptuV45Es7Q0VMqdn32kUGJoUdB_GxnUnSHtHzfq6-enJIe3NMZs6fiyR1lYjHyFP54rsAhog8VX408rpti3cEf5OBZMS9ByiTI0hAip74u5zJGUDsdcJHdmxWlQftWEin76ieapV70dKZWMtwvSZYCKxcHQoJWSPdUQfJH9JyPMmFcKemGhsdJLqHMdaDxB6WM0aA-in_hITnIF1Kguq5KP1myznTpuEQ6b9_FT9eNVMC7aHpb4Hj2Jx0tBsSVyqukJJyI3W1b-2hqGQgLxzTAEQT7y8foD6GUAqhQOvnIKWRoOvJa4kcXzzPWPz6hCHkDMXiYkW--f1axsmP7cVpVfSie7pcH6D7n-JPV1wnQ-GfIrCjQ160XdQ-8nO3VxFxTzm1J8pzz9pa9gXrQAlBOFI90bWtP3TIvHUWOQADCG23f7piU1k_mMORQ0yJVny-D7qnaQUIryittQdkAvvPgL1a4avPbu_q3ep5dcYnG2JdX7AvreQPD0ShXbmfc70MWLOIpr_MeYWkbZstrsBI2BGE1BQ60ZQcD8BH1elshI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=M5p7hP2xvISoeqiycekuChUKJPSD8IjDReAwuS-ymeQMdzwPJLY3X9Prt5vo6TbiOgzuc8RlsmMULhDZsaPWAC8VhKNQKCXwZURV_sxO1JgXMS6UAxng1UarmeG2J3QGptuV45Es7Q0VMqdn32kUGJoUdB_GxnUnSHtHzfq6-enJIe3NMZs6fiyR1lYjHyFP54rsAhog8VX408rpti3cEf5OBZMS9ByiTI0hAip74u5zJGUDsdcJHdmxWlQftWEin76ieapV70dKZWMtwvSZYCKxcHQoJWSPdUQfJH9JyPMmFcKemGhsdJLqHMdaDxB6WM0aA-in_hITnIF1Kguq5KP1myznTpuEQ6b9_FT9eNVMC7aHpb4Hj2Jx0tBsSVyqukJJyI3W1b-2hqGQgLxzTAEQT7y8foD6GUAqhQOvnIKWRoOvJa4kcXzzPWPz6hCHkDMXiYkW--f1axsmP7cVpVfSie7pcH6D7n-JPV1wnQ-GfIrCjQ160XdQ-8nO3VxFxTzm1J8pzz9pa9gXrQAlBOFI90bWtP3TIvHUWOQADCG23f7piU1k_mMORQ0yJVny-D7qnaQUIryittQdkAvvPgL1a4avPbu_q3ep5dcYnG2JdX7AvreQPD0ShXbmfc70MWLOIpr_MeYWkbZstrsBI2BGE1BQ60ZQcD8BH1elshI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_9jOTPDscH71UalRPv1OsYjex2ETOL6jQeFF5CYNNbjnChf0Ea4LHz23wQGf3UfrIhOtnWIoI1SjaZFc6NBasSZfviFI4_Tqgv-iLDvbDRpdxUL_KoWx05jUc6S65cIcoqeaaK1hV0N0M3scwo2ScvE8VT65Qp4AWSP4l_pW-m0-CB9mcbtWqyY28CWhwsb5wEjnsPan_MfTQlP5sriFnL8ESagLGwZgENNzN1Dt4vRpAImpxnwGunZrZvOfZfLOLhir9KbXpWz1a88oYVdV1T7fVW9-lNUyV5M3hgWzlMmy6kciX8ELO4dRN9iOCAa8v3EsGrbKSrtlFeYtwMtfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTG-pqUFnOigks1gWFZhrsarWrIDlCGuKp5zBfpJYd7GTdIAM2eGBOIWrH8JqgZidkZltKuMDBD3pnFlTnt-Xaw2kcFSu-4GBHlGTHux6b-hz-SojBVTn5DvNy06KRyPU3vaZ_6qCzj2NJA3MCbhgGFJmxyLZi_EU_p8irwF_Av2VqJfFTH6nfZXbzyuxL824vawEFAgqPfPS5bJTbYT0CtN_zraoaPnIOcOG7hzpdRu7kt9C1TDJAm36K4JnumVEwI7WJLdbKdeZ1-5xaZBdJxuuQdL-Ynam6SiAQB4TyvZ6Hvf0lWEAxRhFVTiIP5qzCg4wzEHbCTjjEUxywy2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeN1rhfKHzWLM3kACr6fBcqeoFAcUewJh2-NKORPFyf6KP9IJZNPaaSGITIYaFUYwgjtfkbLLSAHt34JTscZMqc4MdkllFfDVKNrddqLtbR5n0aLqBYgQ7XYp59vEmjYoKqLB2X9z7LitttGz060kv8Xhf2WWCTlabjnBne3-aXJmtduL1LsYNO89lDSyU6pN3ui5o1BTR7dp1ixufZ__E7M9hQk8jrQxGAUoyWPrsevDykvuAN-LfbomS5sE7xrZmBtMvuBgz2jYZCyAiPUCRmbore0PbedS7Rysk32QTpqYzlL6ja_UrXrPSFbKG013kmX-jFiR53lf1yEgJGXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pM5Z5fjuJVowrsbj4-WK0rGY_zw3qI6Ra6xAL4Z5gOzPGQPFNDCSH2FgEOHjk0GpBy0ptFc6owmg7Or0CS_ubbMJAJIigjbtQJA_QmA2dYaZTyrki8W08O-NDKGs9S64y-8TZM2_jxMIlXdpablY5GPBftazkLmYWgWyAyiwbvKW6qJTxw-nXgS54Tn5NfI98Bj6_jC_dFXWin5kStZ56dHBzXsjhWhqlmX-046ZZQ7Fi7xCTcSKkx2hTEct7Ql6ysw8knHs9ms3tn_X0O0Xm0eihqs85l9XcLa2Sb6gBoyLa5LYhfqikm7C9nFcqWJjyDgILKbOzDy7zjR6VKa4AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShKusG1DSBTFSAUjS5mpQtgVlUY6uTzSinvPuQtVbylJlVzHyTClOrm_3BO0fW8LTgozWwRpWO_e4uvo6zAZraMUJkWfkkQ83QWCpZwdKUCk_h21SMlPTC0G9vZUCdAc4kL5kxfx60DDob1OHc3mLs4WVsAiPYiDEZduVhWivVO4YyHhEbUKoux31ZFfL8IIW_zIc2piXWuvVyGLOy7u4I9_PeRZ80p1CIEupy5zmyDZ3cOnkfYowXEw4ShXWrqwnyDVMPYfNDFALGDQe1hCbf-jyhjcWMAQJmOiw-yW1FUbsJanXgEOh2NIyzEePA6wh_ctMl3_VbZ22Jt7gWK3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxbjjxTp4LFhOqYuRszdpaihG6vB6NEXofaAHvL_HqtghF5Ya4-YRMQmz-iG50kUiYY7nUN4j5rRWhXjfOLzOC6XHmQCET_RZfAgEhxGJn5MeKytUvviA9pW8SGOUq-3Ck4WjsF4NMZV1bhoYlmt1gGhUBz3q4LaeQPc8n46Yg2KYuOpyOeA1-1zWkMpWuSk87K9roTckGeUFBcPZdLsYC3ObPm13AowQivq0IHVR5OcCObTSVudeV9sATq24LTKqn_sw2E-oyzFonhSaJFdfIV9BApv3qF5WX7HTzm5cJd5WA1h6AYksjSPD-McPnUCo5fDym-XLU1aI_OOvWeX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKkV40XTgiBRp637c-vcWWuurjTzqY4U8BvXczb7GFTerza-0nVqpW4KhwwvVR8DbBozxp0NITYPjdmR4KV8RZ2CZZ9K2mywg_8JkGhkSRp61aL_bU7I_8YDbVmlIBHNQHy9TCHkiaK3qSp4eck0b5Xlgx9BewC57aO9Dwm8m0c-f4gbodM16lU9sYGO8YKN_MnTrOMdJUqYMOf9iTFp42e2LS-aUDm3yi18SjImiE9jyLl7t0Y2mprWP3_pYE7W2qzT3RAL5GsTaudu6Zn6ExXXNj7ZzaSoKlRMENpKcF9oPqjlp7eQyJKe4jJwoJK4QTy3Y1RdiRv9s_36bL0gKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAcDOqF7nE9AOkXFYBRH7My-7eresx5DhQSg9ANmba7JwWd-mcuXVvIvfRmcWLMOcT4NrUt8ELgNZXbVYAiUq9e3Nn4aYd-5GoU08nwygf79ljpjAKyFEV8C150yuVA-DbHggxBw_mYC8wg0t0ZJb4D-JSqNhQ0rzgmHKOCzKjZY0JLIHUwICqEptofzaqCtWuyLJ2i-KmYwZPiWDE6fm6NRSbU7usTuUt0Vx0Q3Kv9u6RR_3-a1VmYar6H0OTVSkmshHI0vjuAG_tYNUzlGw1s-pzEnUSGiLblW_hx9l3G4Cc7mEJEO1rlnXHbPfnSjzC6iiK7ZZb02YucGk-66cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nic_t5Wy2QpumYD0ByDVL59tx-of3eJ9YisJ8ZEBMrG0MxxHMurdP4FCgmP4-_GLyBEL9lYFIqLXUQwJYaBOLEGZKI36bR_KVjXQCluuDFBW7rPciAuhhUgsK3tlSjFssGisbkLuukj9grDWiyGj6KI4KSnuErW1AY-FDqjx9YHJEBv5DkZBXgg2U-5KPYcLvMWNyzNN2h5k-sDQK9xilI1tT9BbBKPxJAtqbYFFkHnlchJikCqh1tBztrtE6e6QkUsQy7qMt_JctC3bJMmWHnQswIBmhXyIvMM4aHAkakHq2W0lL62mYmvhiw3gHU9VwLrxF73sPagbxGTscElDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7UvEKlpa1NDsJ8IJwobEW4-upPovnxu9ciZbd7M4R29HRallIlqo0nRMIRyTK_BlQP96Gtz4BZB9NEf74U6hmgpoCDNvX4PpIesr1Kr_cnSkTxr4fLLT4f6MqfhHu4G9p3qwJbF0GI6bIa_y0SVqOZDBqBJIgpRCQaw3oo3BbIj3KKC_vH3ega6aBnrY_r9h8euXDl52MTgamtgN_x36T1M5d_pFV1odf81X7kea7o0MM0P0SYjfNxuR5KscgRzZ4Gy-8ouAGkS04MTp8Dx-3SWplJBi77KujCf6p-Tt3f8dpTOXpDhhlZuhAV3b2uwISEyDyMWUt3QGS9O6a0vXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7iMhNaBSQ-WdqmzpeLtOLA7qF-t-s8YerCK0ic6eOiFnr2vX8zWNyaFMJohA3BCX8TOOnV0MYn4hpbsBgRd36MmJGWdsgyHKVVUJg0Tp_PRUvHnHv7prJpeBh2gQnNGeLAjh-X_XK0XVdZaW51yy0sxU83do48BWan7bCQlYgFInGoZjiFGIyIvvwoSnS9VwDrwAbUkWM0OsWx5PQrP5TLId2wP9E3z9yOG8pinjQ6N-dnUfHuhhKVw38K9V6Jm7LVkZK58r5YjWZD-0HSrqZC3ijq5jLxMcKJt0A5hLv6f5bk5p0s_wbKuoy5BS9vDGNAj8wMV38P_0RkoTzv1ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L95hR8LQulcFfmwIDNjuqRphm891Ziu31eYzYg-_Rp_tSjEEChPuOjZethyPpUJGbEFBZTD3u40SoG4t9Mrc4cGQkgQFU-2b2BfrwWccXlyD4uCAKn8hT6DjjLAF2IxuRCoToFhBS0R-n6uHgm-SUQtvnJCwEiQ6fuUEtXeBZAboE0IfwYwXAyXP1w8iwngKknH5rfLpvoGrDQClGOOe6vnqhNK7NIqBBgELaJgE2aaiRuDJn2Ga4sGEzr9erFKIVSRhtXMV2aMpASgJPq2wuLM2jPwd9FsGUWb8cII2JGe64MuHDeBXIUt_vUZmsYKFvgnVEw3w_ZqI1VvZ7JL_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9whSk7or6W1eyrpQxuPyvqHXJHmu3n6urHBvnoX5D4dcqreHmf0X14Rov_QxoPOOfUGJjwS2hBP4RvmtWmRUgywfamAtlzYDInDMPkMG2TKKpSOlk1RVY8u0zn2i0_xtPUBCdB6ObbpFSPN3YjKoih5l-TS-8iiYQe0dvH7v3jUwvyGwTShbba1TGC3CpXrNcK2dr0pWpWL17gNEmiAnZbXPTHjE7UjxUiMVvaeiQJiUyVvi2u91IZ5OIETC5j6wbzXF_E7a-NOQjc0WypunvJlbJnZDkPVUEozPX4KRwK4xtMEgViOKd3eHEfAUFiuLsmFqynhRhBWNLWuGwq2DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crZtPxhoqBj3-gzqx-mQDslUxmoFPMYXvn8j_xQG98xU6y8Zq48fHjpt2U0roxvGEco9pM43FWgjphtXHkvCYU7t0yaznYCLz5xmxmY7do2OwmlbK1I4Cdu5TadxjlXm5Yo3_Y99NazbFRmAPMaHP4OC9iEGCTm-Cq9RnYbh-zIJgR04LRO32D_NGDEE_GNm008iV4-sp9aMMu3aZlysFbm-BRpJzCsFWDNhM_6WOY4PB5WNlqlBQJVUGgBoFtvEmEMJ6pmNsh1TuTCj-ZNcb53r8dB7YNYPURHRQRJLm7iiYfgFcdhrFf4x0DEOzUM-rDvMCRsFRwq_qY_Ifpsf6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRRY7-TddpxseslLgLxUMzGwh4kn8PSIV9ZlHxV08uAcIlbRs4sMWjKyNGE9mlFov-ZaFS_12y8Rzo7Iic-zUP7V37S8zqSazB6EbAbpbH_o8Q2KrIvJA0ut7ENkTc660KIq-kjBt_I3Em6mzrkK1_VKva1Srp6xohxUO3dIMw9l5JJPHOeFzwBncDSjMEDZWVCXBNTHOwy0RDL6zy6fkMCaik3oM02h2Eo5qlf7AfKz27DBac6Q8UFzI6D5X_vaWVFSsn9MD1ob-X1i6nHwJAScbPgQOMyqouhYV2aOIsc3oJ8Xdo1vCxaqaHDWjsV1urbTsOiITvhn73cQ1zjjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcSiEXI3y8yKVFh4kv_RXD956gHsDo7rr0CL5kHg3CdXL17VEG_ybS-At6U1fZl4VpNzdlzalPXIc-k1wJYStWzaLuJPYvrFQ1tQY48_HYqL5iNlT26GvNUeX5AvQ-DvdbrwzB4tQccz_2mti-o_RjNhDYZJuIWvACi6R47zH0uSsrFztcxQ9e8sBQ3DqifnU0PVMekeA95hsarDyQbu_0s9mihBtWAi0pbpA6mpoVVQtJ5iCIppN9_FBBzrCkpFvn0sk3roV3NeQEg6h7UoTNFX3ZsE52jepW3HGNYZdyzTiiuUsC3SD1-9ywvqQeqF3V-oT-vr6E9Cg_Uy8iplPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZARbLVe71-eI0-p74U_dilqNYZJBeHDLeHR-6OJ273iPvrpNseVv3t8HOnDd_u0ZEThEUKD26RBwBKM81mMPq9Y8VRE3NBIQd84WHdQfW2Aij4di_mq-iIgOZiG7sYPb_TUbwFP7NkctzpTkZcJa8PZNeOp0CwpHSfH51IscxfrpLfPCyk4u281syb4WPq8-5s7t7Ixb1ciBCMYv2eWv2ToTPHkAKBlwDjglaPtPJBk3FElaw03_2YKxFfYCEqUFqFbm4Ebwn8RuOiMFlYcI-YjRruj6pK55NG9p5D7K71qLkD8UMkt7fJ6Zu3Gp-q3Ib3dPPaGkZvHCtBSf7GMCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eF1q5qEJK3u3yLIGVyrF--9ESz2ruIjcZCFHYnz8CF5C7aaprbwLObPe7bDFGNBo6hXlTvzgyBU8EUH-3l6mBb0AyUczZ-4-yb8nLWx4mq76SFROF3afNrniPk7dtrNAWKm8RylQ7eizEFT3NfTM7b0s9fg8N0jcXQyALvvVVc18a4XQ4MMv3YcHp02Vv0R1-E57GhIxV89EWb5DniRvFenRcHLkXhxk23MZ4IxuWFSmAyyBKe8t8wxb8qemK11rM9kyG4hk7UPLCgy1LEaWvpO-k8cEbhGogkN5K4DkSbHJxQX9TXgyf_jY2Xl4Ti1p_5Ui2RzEiPc9QHAz0bIc6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekiCVxhc8tUrQHdXEUdGBs8FLUtyk3c07kvPuTrKCBDA-70XMGgxfBS3aDQccqF2GtjPUoJnKtav3-3_4Q1-IHboP2CrMu6_02lH819IF5tnJWBuj_fLvYchRfhAWwm1FDfvzAM83zU0-eRH_oMqBz-dJYKfvde2uUUfS4Mycks5zCanajxL4caE58lhOJBKaDJeSAIXVvmHb8alAfca28s7AQzW2e4_UOUpEIxFEQxIYkd2njdWGgBq6eXR7adz56kCDdM-IbTpOmhTjY9bhqrjavoMiepqOE-ummeLrHdfzCBocS5YMxN265cOwz3Xypc3LjzPqbQLslmGvHZE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTX9MZkUFW4AlhDjX3ZSbUb9S3lMQaoO_jGEbmWzSfxoxC2C88O4LIrWbElQijXtyEKSuuW16OZdnVjuD7MsGqKy5XnCslEUkD4HpIzyLkTM6lPCfXZZ8u9UUEG34ofunwWOulZTB4v0SUogHVrLq2Ugvq6LqvchrjyWmZhgFeDnzYHZCa3Va9v8HkOs40MX57XKmN_lLl-SPxTBFWUR60S2V5bbxEqDmHDZF5dNsmfxy2zfFLPbLY0nS3WPwYpOAOhQJeDVjnTedR-wkt_WPKeib5o-DEnFdrquwy15L7NwmDszBBRdJZf2u3SwnE-LRnuRlwgPvhzkJllnNgahGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXFoej4elZI6pfO6o35XmdjIjO7c80niWyL0en6Nshp_dD_i1B8H99D-DnYwU66kQaGT0ZNhohEW15v9cpt2fq3Gn7bewECs-MAcjZ7wWGB3DZ6T1rJp30Tm3SmStylMHjw3GQ7mKu0GaZRm0fLlniGQN0IsuFpRv1I_xwH8NAO-QZZzSf7FVXkhFZGeBQbuJ6A0K1jHts5Sq_3ECMrEAy0VGJuGQnnWg6wA_AGA9yEE5U7YNax1yC5pyRJLQXhiB2WiNnkan5W8RTBsjZY-q4qjyaYJrRTG3RITLte5g9sUxLWN2rdO9WYMmz80UGDJIqAVxOBzTDQpnuR7qH9giA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ8TUGdhTH_p1WH20NrcjYkkJXaob1bu5rAIy5d4DPkuCJxRh1IIxCOG00EdgvHwlbQ-_YURmvcxqucShpTC3akSPPHdNm_1FbnjAc3T5pK0uE-1HdzYQ9Zg9O-mH7t2UDeWTLvZoQ9Gm35Hgjfz6EAZtzE_7C3gGRWwbfW7WDCdKUpCHV3iDyR_5Ja8UGNB_j9kM31qJbjiBp4AOGaLxUCyyundNhcPh6jTIMONEaya5VNVz45UjE_CEd6tvad68Xt4m6qFciMuWBcX2puB5ZtWy4k5vLMuX10MImGuio-xXjqsJ6jNhK6mFScELkbQeYSoOOjTr83g3zOSdBqXzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSy3EN4MgvKLYbKLwTZJf4CHmzD_N5Kz2LIkRYW0Pt58fiiIIrhXwMEYqzpBfkx94n4NJIafsmO_HzzX6bV1hBcqbedA3j0tSkxJUajo9FbHQWUnBbZhc1UMdmQkvRZi9AoYYJ7WksvR_l5keFJMnW9xU7lmdLnZ_sL_ISzNArxtkOs_a0gTEetCOeP285PJA3cPqoGGdljw3VSprjaKcLQLHOpNCnZ7Dww_3WNz99ITfFnBOZApf88TMEWfvc-5XUennZnhWyu4NQCypqj0cc9Rx0zduLOcJNRikbPIM_AOCNsh-6lXvM0B7066ohkPoE0ci5JHQQeUmp1li2XDEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/il6lX1uJunwd58pM3hypb9hKWJjPTTSF2ZkRChe-8vuikCSMf-M5T2aZyqo32N3Hwl1EZNXhPnguCINq4h5tP2o19RmJSyO5VVn7ConUfaUja6ChwqIQghu-XEUiSSQUvi_iySkf90XsCr5Zh5nFp5NXRc8N7iRlep7e5-u2PcD9VRV2UNPDAGNPnRMh2r3X7cypy86sL9q6XBOG51YYa6fVvd1j3BwFG1WVgi2ynU99baVTgMbrnWhlT8q8MAo5t2vzhqTKw8bNO-SI4WOku_6z_3dLn1mLaPx-oU29V7MKssH4fFBRWPeW242rcW6PO9QuNnG_xJwi8VU2R6Qgbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mqb56ujH5qIk1o0k75BEX3KuBHJ0xKG3hZXjI-IJ1ggMP4f6YrEbzfRm7N586JoEKRt6ljsyCQKdadVgYDy55dtO2aE49YldcPlUXxl-wM-Q_Ku5_PcpE-2WV5_RC4P33ZEEg5A_wi2IA4_G4ETgMkmkp6Anf1evskgYdMe8Yq4yDjrgCF44yKAoNse4m-B4Epf5gAB865ONjY09-psTls3TiamUspPNDYpngqljqVyK5Ha4KnfvrXhapBhkkI-ek8jattH2DPwpTevFAHbESSTbaO3xVO1GKP1pMGlEiZY9p651HJ_dAeZR2dbExiv0F1ZznWhiEUKXxl1oLUZ9Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjkxOBCDJ4CdqQ0L_wHXOXN8pBl9QF5q0Tnhafkj7I5MhioWlS6HIB7P-82zB8h-sGgrskvF7v4TO5d3iTWVjehRQ5mFcH_eVpeOaVS-AsbzzhWM2LDB8aMUZ4dyf4mV9T7T103BAwV1Fl4Kws0mYfAXynxo7YyXXVdBjyHQtEjQvMWuWFo5yY2_pYR1spcMryL3h25ZIJ15gxbE81CqLNyF4L05fAZr1GydPU8BVVGM18qRncaIcnGJLrlCCMsrQXHX05UiN8GMBKdi6pnU63F4NbUi8nGp9W0GpDsz_Spzc3YCTMxo2kHMD-XFWT2I-EmnouCvSlXyl6J2zQ2F5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOwf3hC3x-6TaN0SzrR1k81jH6Cz_MHbRnc_xaqVlVlzmQq8w5Vu1xcdpBdZIUP8EYVg9EONVydlO63P_JC1QxIbTZklCIM_Nn_1CisZOxo-rvKa4nnK2KqS39MRjwXtRrKN2VIJ-PKZx8GDiDuUupv4Y4-iE2EKnx3I_udh98T7BWJqbcuDzoAhnq0Aoot_BwMcHmJ8aCdWxRptPf2HAECMePIAnNosf5-iiUWrMp7BpDQRGR1gqkw58E2hXasA3yaKOc9DACKhxjxieLAr_7hLCnsBfgo95trOIZhaG1APr6oPcfE_i1BcFZ60tPXw9GvF9pmCyvnsh89pewDZdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UdiuKbV9CYyRT4Pi7FkinpoCK_cI_nsAz-LG5i5EHiO1fXy_5-g2IMjCMDn1N024zxdEtrR8M3CqlKMBI-p18Qc6Q9V2V62xuGAvwPO7y5Hy64weS3ppFTjQB-m2KFTE8UodkYm2pu7E86WyRm-Lx2UKOmGTs9_VXSR3Gh26HnUKtLOlogYptsgpAtYziW7d60Yrzmpa77OwJiI2y49ATiorJ4jB_sWS1OWAG2H78Db-vVOq976fW0AUMk3f8VbiQqAnwF4hwKmcwaInueU8mle0EnaXnajdpGglKa3hP1F-sFfNMltzLhdsNmLTa3QJcuPO1GzaiHnSHkhDDN08Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3AL_5gIC6xWXjIivYMxG0sBJ0KWs19oV2Na5grXgwtX94ALufEAZPxGXY64P13NnFaUjmYDRDYdi0nRJtd0EpApwTVul9dnK1g8VjajBpYZMsUOclxDPBllT_27FAM8Mrryp7bOD5IqSUI3CllBZAxU2QWcPZRqTauWsKkxKFtj4aQ57mkE-RSwxOBP6MtXpBS-nUGLZcvVeGybhnEUF5Cfl-D74fqZzIlF7_Ch-qm5D1tvWM9HUXB1rsHhSlwq5rAZa4u9HNcghXYap0wtSOQWhJSHCyZMzlATCLMtzro8rnKJShNTQTegCXg41HmxxdN9PEXxGkyDt2hZK9O6fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eigDx-5R5ydovn15sSCJ_ocbUG3tuA13b-qwv8E7zfcqwKXl_R-WYfuKjrt8Notl5HAfR8eG53F2JwCj3ifKOpZ0Z03Ay-K6W3um5jadRRPlu9lzVTcx49HpLQwyfyhkhFU5yif4CMcr6GdFuFrzzCQg9nGXMc_UGL5evXlQJOFTwOuqjjLRM_LTzOFIzaX399q89LZUrcayOpezix2n50ak3_Cn0j9N8p1HPTJjOYNIVLwTnU6w_Meukh9bCZylJ_6xczBckmob44l1hOs0dr40ARESY-R3F0rsYmhNIujskgx8cKe4VocHiKTZfdv1_wTXcopxWyImV0zdIWpx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_sFN90FuDO189E-0elK9G8taEd4WZF2AzD-su51rQ247Gc7s0cwFS0vplQwJ8HJchwjI-dMPgVUX8X0HRnLsHFsaZYfUxpIwTfhQ1_nPYpPQAPHbPOEr5CfmSAa5HfWUgxs_h4CYKxHfmcguJ1Nr5KM3syoQ-4f-0Sa9j42tleORNJLli38fRozH8KdPlxetYO5ZrmIKlja481P98D0XCobC99ojDAO6StM0avcbuadnOT8qHLl5HIAimtqf3YLdNdjsViQA0b8bauKfOtrHTNg0l4zNGsNHgQqwyIZmWsw4cPVPq2e1EpIF7YszXw9yTxoanYoakG7O9dqMqdn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUKW8tK0d0i0o-ofS1qmBtRrmW71st2Gcchk-prkafC3YCqblph15zfA4QkJylzByl1IGlJ3w6BmYFFO2w01hvbuXEmRCK-OETref1Jbim9b82VqH-uAN0jbon054AKu65Ih_h0TExq2XL03qNyFHJjiMsxHyxkEW_soJbSDSLlZhkj7gBc60ZS7LtJsqq3BolXXz_vsFodvUTsIH5iA4_B4pyUikZEJzm5QnnEm91DiilOGbsL_XiIINstaFHfOAQ37zCd6oPP0ImVixPO644cWTfTOn31aA8GgZJhhq5Kp6HXbd-fzJ-HUmtjYIoKPGyPnc4co-MLeqUBOTvq-zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIVk-_FZLX6PJin_S2cOqmzcxLLKlTRbPfENcWFKgJUMBg8Oz3SAvFukgPbA8BwoW2Ur_VYi0iYfIJpT7-FX6XTo8C76NLILs9ud4ALndGqYXXMjxipPL8RV0siIa0Mo64LfIM0rDTpxjQVv_DHbBkZSssbjrUgUKRxO2SgpMnoIj5GhVVxX6DZl4Rr5DIiZ5cA4HW-vU4zDPgcFBpPiFfAKkvwB3BzyJ_PvR4eyZ3zNuQcf3xnYG8CerIYVgTJK7cnr54-xBMppqqsDOZml9AxTxVPh57pin-0RoQaIfq9DGav5-RZ6nfgBXimkPwu0TUVkZsuhe-DjF9_2jqIhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNIwuKnFswAgdFWNY3Tzp72hOhY_0g28JF_gTEkh4QcKuRlYcjCEQ2PyPCcmAoEcZPgMyvQ63_osxVnPwu2dXClfAoXFe1B5QgE1gR-I1FH29RzH3ZMX4ge4TbEPq_4iGBRRnDGtBRHukBRav2Dd32NdJDgMF6T0maYamD026HfcvJjXl34diKqpN9olUGUEp31Fz4W1O1EFWFBHJkd5RdOfjIBRR8gjs54TotlKB9OZwE8HUGX-IlHltwfV8ZGDfh17J3DnCA9cDYSHatK2DdMrY1Q8B4nwbTeoa8KwSNscvTBNdoTCPLVtkIgJX6l0S_Xu-YzMKjqeZ-8hM6-dJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=v7yYb_utspnh9e7ccniD61poEAGLh0igL0wVo1y5N1_UJOUlc2B5gbzRlMWX4SeQMCqhLKKJTeW7Sw2sB0oIttePv94FYJUd2h8-4LA6uC6Q5aE5HYm-f02ZI_IfadIQkQZitTQcQewSuJYPxN65nLD1nv69NJFvzUjufSyv5x-mX0SqZyrGECf-3tJzpKcky4_rwnOkdCYf3Pwtt31eQ_pKhx_3QnEL5CU-Fjt3hkRKvQzsEYt-wml0h3ykSu_lMXe44vRUVm-M0oKv5Qh6hY8rXS5SO0jLBsI0FAckRK5k5ETDVpiWsRHyltwS1QSsybGHl7GHXT_AhAUMXMA5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=v7yYb_utspnh9e7ccniD61poEAGLh0igL0wVo1y5N1_UJOUlc2B5gbzRlMWX4SeQMCqhLKKJTeW7Sw2sB0oIttePv94FYJUd2h8-4LA6uC6Q5aE5HYm-f02ZI_IfadIQkQZitTQcQewSuJYPxN65nLD1nv69NJFvzUjufSyv5x-mX0SqZyrGECf-3tJzpKcky4_rwnOkdCYf3Pwtt31eQ_pKhx_3QnEL5CU-Fjt3hkRKvQzsEYt-wml0h3ykSu_lMXe44vRUVm-M0oKv5Qh6hY8rXS5SO0jLBsI0FAckRK5k5ETDVpiWsRHyltwS1QSsybGHl7GHXT_AhAUMXMA5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJoBnFq7tsi07sH2O7LkBH-g3aqseaiwYJ3qoF_vDqOjQ8SKsICsDjp4yFD-DJQE9LsIa-wldbmleJ0bGSMvw08S5LLNLEBzlp7ViiRt3oZG4cTPWYS1uEtugBjgs7xm5LYbirIdRjfh-fF7qp2XYMXZMYn08Wpoijxm3btyuKRAG_En8wfJXw_OZGh3ffqKR-E7t058-AEhR9ayxtLwntU_Vx62SG-nFipEHq-0FpeITQDH1g5M_p_5SGhWWPO-FTvOYGSD0s8NeYLian4BAI-oFUgRayI8fLCN841Ph-g3VGRGfX9qp93tdZrp3RmbUb3-aBiYtBJmuBWCmTmVjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Xltc9HHjqJmpp2r2viwRK7KvcgLsf4dtItWe1FzCHvCzESOjAh6UXoYITXV9MZyxZzkrU4OsvzC3F39SQGNHeAUtYtHhl2KTdijd8HqESrgHUafnShkLLylCOh4fWIZl03MGc7LFgmaBLEPNSdCQJEIEAeDDzdjVbeVFiuxxU_r-xdRLQtrz18fX6EWABanQ5tUjgwkqlqwsy9zOs2v_AsGStreaNrfgZUz6jD9md422UipOODY_U1ZepX58YB4sLCvrDzG-Ko--MXQtrkXHK0Rhi3wRc5Uk3L2hq2RVXycVpggTijxvbEHlUsokWvZGCIZPuzgHVEIY81Pntx5g_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=Xltc9HHjqJmpp2r2viwRK7KvcgLsf4dtItWe1FzCHvCzESOjAh6UXoYITXV9MZyxZzkrU4OsvzC3F39SQGNHeAUtYtHhl2KTdijd8HqESrgHUafnShkLLylCOh4fWIZl03MGc7LFgmaBLEPNSdCQJEIEAeDDzdjVbeVFiuxxU_r-xdRLQtrz18fX6EWABanQ5tUjgwkqlqwsy9zOs2v_AsGStreaNrfgZUz6jD9md422UipOODY_U1ZepX58YB4sLCvrDzG-Ko--MXQtrkXHK0Rhi3wRc5Uk3L2hq2RVXycVpggTijxvbEHlUsokWvZGCIZPuzgHVEIY81Pntx5g_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KALtdyfhMDFTcZ0tabLOyKugZVIEDzlWAKremp3PGNoVe2VI8F-Iid7WDJnBH53HfKl6RMMnzZFG24uoD-Myy6IOWrr7t4nf_Qb5GuXd60H7J2_sfRxfDZ2ESmrUFjeI1gccdMdXadfjKYZmWDVnoLzFosYGe3aiJK-ePDFNtI-yN0ZW8SMkGty7d6fBddnYpDoSMva00devZFP7FwEpEkwFl6qFsxR_FhR1oT4xS6s4AZeOvGYJBOnjZgXjfvyh084nEnUVppkQ6V4wMcSbK5gqSVHUqLD89v1gB5bMCDvBPEPkRIbPbQBm3Dc_XHt0oW2Xrw7WYLe2XTxnU8H48g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lE8UaCIG7Rp9iWjfwESxohw8RAWvYTeNgEyjTLSacdVL3vO-QBpC_N2dX1LUcJ3mcShDJvG0n-cLf6vs13HOSgOMLRmF9O9zp1Z-tncmGsSYFsQyp2xkSZmmC2C1SnrpcsYIJibOcdKBaANxGl5h2pE1whIKxdcC7lR0hSPWzlw_FMozUV9xjKZgvJYfI08vUhwAiVSnhnAAEkxFKVEu0cJExKQJNTuF2E1yG5hQY8eURgrLOWA2484XTCFgw0VW_zpYJqMI5w5vWCoBl4xWS0qc8TKCQK38rPZf3-DQ0f_ZhZKJ0PVmHuvrmyE_xV0YYGpsQlBCk_nSu85CZKnsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=gxAsaSEPlB8GxXKUteLkH05aSeruowMhaB81STTs0-qwekMXDyn79BtOqbCM9oMVDMcVmv0qsCKwDmnOO8Qm1Zf5k_yCEnnjLZ_EgdMj4bHOo0uVu2XdN5n_D9DMzATGMropbZZ9in5L5lofVH1mD3Ld6a_JTiO8a5gTjZu5XRbXTMPPZviPyE_VlIFyKTK3ZA_I693UyFKSirLhBEQEGFl3uFObIFZdiYgeAqy_RQh-W_2n0RT9qxqnMTg7v-IzcivLTsyVTme5mFQ-lQjnFSepljGTQq_bu2ytDwMb-JHqDR6cPsAIUK5gtbONc5E_xUaNVjhaIYcvx4OR1AExbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=gxAsaSEPlB8GxXKUteLkH05aSeruowMhaB81STTs0-qwekMXDyn79BtOqbCM9oMVDMcVmv0qsCKwDmnOO8Qm1Zf5k_yCEnnjLZ_EgdMj4bHOo0uVu2XdN5n_D9DMzATGMropbZZ9in5L5lofVH1mD3Ld6a_JTiO8a5gTjZu5XRbXTMPPZviPyE_VlIFyKTK3ZA_I693UyFKSirLhBEQEGFl3uFObIFZdiYgeAqy_RQh-W_2n0RT9qxqnMTg7v-IzcivLTsyVTme5mFQ-lQjnFSepljGTQq_bu2ytDwMb-JHqDR6cPsAIUK5gtbONc5E_xUaNVjhaIYcvx4OR1AExbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ-Ptg3cU524UnY5l-yT89s9Q98CiCwWDKSTU_WmA4dzEwGHbBk4tZ9MIOiP0KpchywkDqrMOa289Sm3mKtFBtKia3DeSeNuMdgfqNRyXJPkRqXnwUSLE2zWlHzGSVoRF3AchO0FcEzaNk3wGDNn9-0dt7cR05LwRIHsttShPDIQq3--d_k3ccrJ2SVRkKVcUJsLverEncNewrV4P42OhRp1Q6WjwFy7kpt8S6Xx8reg4YssbwKTKt3MyAViu6vQ10qDZ7gIUXn11ujPjRrE8K7WfRqXHz5QEzvX7BP-UVDg9wmOMIeSYQ2zTN7Maci6Uqsg9A4h7q8R4Rctbx_sdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pzkJkSH2gYkpqmkBg7UquxtaYOyYbHSu96_exltR7KE7sWlrHYCl7F1wtILmieLiYYlgE8i6BCjPsOehv8S9f0VbhHGcZhq2jvye4FOEQEw8CjIk6fwEimoDd91sXrg5mVghW6LsTtc2hqiso1Akx3Jr9nXqyeb_ZxBHVI2-zEC24xRujHGYC3TcadsawTjs3IApibShlXiuccQKw0sz1CV1-t1tXe_bYZra2c63mYdEDGF3B6b6N8ldDBCzBbJyimBPLY_KB_LSHV5ji4UkcQ1lhd10wn6wbVgDojXBoo4lnFazRNswH4AL-myhklHFICOLprcWTUTjQMzmBaXYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShLLafAaTKfZ4i5d55tDP9asR-BEKXySLZPOpOsE2WeNhLvdY9JMGHkSiyNLWLwLvslJizmSgq2YIYuRGCdeePjmhIIF7NCQj8PGPrSTbf4AhwD1dg8uhGM7g0k6lFBgYibKJ1ZYeFXbzgloy_HR6-CVhAqH-6FMJpJl-F1eZ79mR6lGZx0qXRiKxafhTIIDCQRPBgyCDmR4n6FDA4dl2px3r6ULpaeZKZDcuuVgR0ONp4w-Bu-8KFQUMET9LxVdRmtyUOyNbwqZsqtjDLHDzoDmjEJ6D0obiZJGqcuRBSWiqJ0IT0a_Hslqrg6-ErEiRmg_LKc_V1NLRFJdv46AAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=CEx-tnuefIQf6s2WJ2hNRITAIUG1xKJVSq_uAJedw99OlVusFSc9ZfBrlgKAAz07p0DtMN-o9lU3NzneKcKpRsmZZsYpYpfRKjaAelLRRz0jGoXe9Y1DpyUa_B0LsZ2gQe5aj8AB_db3_5xyn5Pbqd7gFPRmyuW_5JbAlg9FllD7eTkcAxcmsS6OGxW28t21lGPWpQubXAX9evfmpkyXEVP9rAOQnSVGKYbMG6gaYjKKHu0MWB4U6xC_4VFdRbZH16MsFqh0herc5pgZ_uZNN2KswLJgPcsltdSsqi3efAAm0fMk31DEuca4PAMyLkdtqU28v-klRMN0-WqC9Zrm4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=CEx-tnuefIQf6s2WJ2hNRITAIUG1xKJVSq_uAJedw99OlVusFSc9ZfBrlgKAAz07p0DtMN-o9lU3NzneKcKpRsmZZsYpYpfRKjaAelLRRz0jGoXe9Y1DpyUa_B0LsZ2gQe5aj8AB_db3_5xyn5Pbqd7gFPRmyuW_5JbAlg9FllD7eTkcAxcmsS6OGxW28t21lGPWpQubXAX9evfmpkyXEVP9rAOQnSVGKYbMG6gaYjKKHu0MWB4U6xC_4VFdRbZH16MsFqh0herc5pgZ_uZNN2KswLJgPcsltdSsqi3efAAm0fMk31DEuca4PAMyLkdtqU28v-klRMN0-WqC9Zrm4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=DQ-PxdwIL38bhcB8-yibQpUXi3A8uV98-ftUvNImr2H5elR6mz5MyRjxhUOTWqkIaZrYouCnfbZTsj5uuzdJs-WDYtrnn3GGq4JUxdwd6DFalYF2ydiu51nvDkhAEaUCVu5Tc_Ayi18oxwKflLFFfzQ8pRywnDgLG-iWSqHHeEA35rH51yHiap27Ux_4GoO8Cx6v_ablX96o0ZjxV2p1UBHRArzjOwUYG-HrMLunNJWTIB79UARixUAwZbWq5spAssO3-9bll8suBvLPuvZUxNcD6fatconGJSGjY55VZK_St1qhsG4Bm357vW_Bk8kFnoriib3DFjy2AdMGZbQftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=DQ-PxdwIL38bhcB8-yibQpUXi3A8uV98-ftUvNImr2H5elR6mz5MyRjxhUOTWqkIaZrYouCnfbZTsj5uuzdJs-WDYtrnn3GGq4JUxdwd6DFalYF2ydiu51nvDkhAEaUCVu5Tc_Ayi18oxwKflLFFfzQ8pRywnDgLG-iWSqHHeEA35rH51yHiap27Ux_4GoO8Cx6v_ablX96o0ZjxV2p1UBHRArzjOwUYG-HrMLunNJWTIB79UARixUAwZbWq5spAssO3-9bll8suBvLPuvZUxNcD6fatconGJSGjY55VZK_St1qhsG4Bm357vW_Bk8kFnoriib3DFjy2AdMGZbQftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn2_05zZyCMBbwBqF1JtZVgArJ5TRYFaSYa25I0GDJsiznNgPx-1BBVcfevtjk-IAQtqR2VgG75kcC9ZlbwHSn8XTRnvWshVhS5khBXlGXuPg_vmZOaOFwOaN5OWF9VOvawiUCyHAzzJeYWj1NuOQ8S44kpqBZttzHoiOPk5DmFRbrdYWOmqTwQBnOc94mUiaNuPKjTDB_DRGSqfQ3TM8GgePdfvSM3ey37TeMkJ7GVUP5JylCEQSHzcg26xvNUJ_rRVJH7JMdP3fFO4SPV9RAGloJEoX83BPIVMV16lGdlGhiwKCh54r6yE2E1du8FubnPUFFcQwh6E2SKWyRmceg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PYVC_wLznm1qIhUmlHbLt5sV02YMjs1kzdEDbEtnlHR4Or8_h66z615PGAFKbLbK_wS5_zD3Op8lsl3qLOOSiBR0SwgOit2x9QWOs-aRg_WmwmbuoOQq20_OW5ikeHUHV4IWHbpSOPUmwGnHDHsPtJB6vLBX4chjo4xRjQ_RV3sTrOgbSFtn-qJA8ZiolGRRdRFtJ6j-UxKDMUuJF7HBs9JGuQ8MYwhLujDWDhQC4uI0RcsSoqbqIqCLOy6pqwdXgMVkwiXzJPqJX0y-hwZ22svRVOarmMxTOKtbdd3rEl7o64v7jU6a1u5zB92ZERxCScldKAeEWYrbFBAmIW1Wrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBhmTs6RZEMWXznak6r9a2OfvL8Pu_sOgRVim-m6ib93sWvNMD23wmEuGHYUdXyft8mmZTykjCuWjG4z12_Yfep9-IG8GtH5SaXPVNLMSwdMZuR1eMMsJvA_ZNc3tmKZX28WQxPT8G4NQZsfRRX8PCstXQ5j8IaqDMnAOc0pM8J-w5Suxv2yS2pK0Kx7taAMQKoZws-70RCEe63fZodJvwjqu_mnsfgsMPYcKCe9wXYlGn0VYlzVa4hjFRyy0QQ8xZcRbfGhtGc8kUnFlc5z2gYFLU3DjuDCtSPcVZs0jJJ5DJwgbkQ2G199gi6ZBf6q_7lwXuLsAeoizIXRGYFPAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byfOTVwew1ALSL9kGwC1QAvUBYdEAj4SeMB0u1xQWonQNlJSg4M2ad6BPbwLejOTBPLy3CCUbnxa1bGa7fpLuCaL-H_VJk5UyWGBQlaSxZ1G2w9cTnUI-OQM5FF_VqvaLLt19q00UFa_3T9JTJcJagmzx8_i6HDclxpWhh3r_GmAqqFrG6XxhLakq8qWdGPUKDN7_76NvNic6kBrLkSzpAxSr8voX9P4dhTWn0QdwGSr_7PPaC-Jkfltyxyx94mJ-eSDf617yzgy08s1ph1EAh3hL9eFfiORcq_gbrc46W-UqW0tnRwJ6H5OE3wxLo0XFeCljl8wcHHqzebZAh3fkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcNyJnaYG72CAKWe77BUJ5yXPCuLEdXCQdIpbzgicmsZ_NXchssZrabo70LBrqxaVVppYMKCpcK7fYTJwsBxC9Y2iKasz_70zPeey5HPB1zSfUAutBdYyUCsh1HFyZc_4Wp6LG1a7Gjgw5ztvPLWuJH0SzLg9fa9CaBGHSyLk7pa837kZXX6KWvIY5Xyt1zfprmOoiY4DT1-t9hgCr8kj5m8DvsrSeIRbWBQra9QZLB4qJJ677izZZisj2kASrs3OhgqAkvN3mFe4MPjFyixF6-IowuHEa8OGPS1HrKnoJETKjgWydJSNuW3kzn7XWeC3sjZhq9ujXKM7Cct3wAqbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fX7BcsXWoqsdS9UM-uNO0xBTpBqspQemeOrn-rWKDz4yYpsDuMRBbUiYmJOcp3anpT7QKDLY672upI4w4FI_FKXTtNdLgRrPE_xgBD-MtUSODF_7vInFoG-EDeamXeQ55W-sDE9oVdp4d_T-3bkSUZ9xgr4wd05Lu-Y5AvP0aCJTPNenED9N1SsrNsFeisA3lP79EIBZdtggguT9PRDFjgRBcXQc7ZWSk-Qv19czM2IAAnpPnvkns_0IUe-FnSq4LvvUUZ7cfOutdjA435LSIhtE-qH8G5OEinyaP-cPl6eJp2voQkVD-J3sz3aF17L3dBLb1zOoBlKs0tnlbf95sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9rfW0AIkEaRwT7C2KlMG5-6dhIcq0NRXsnR5ewk52aSDqJfc4n_OWmje04fsv-KzNsOuvdKjgvV-0KO6EXewBpFmCeFyXb594wV375EhcTBNz77rlohzZ2RHXh4A1jJqEqgF-XNyjY0LKvpbk-Gnneffyx_JJXQo9h9X-BDPERpxqBiRhAd_8mmJMsfX2n6bFFg9XJlbkoORt_UnCZGLxMZXoKmYBmml5uYvl2AqXrj7qnbNHYI4CwRMdTrueWPCDNDNY64fxmJZzlhmK3IVwo1fJdA_qquTfhT29uxLWTz1-vbXsqfJW3GAJhFyx0t9UfZckC3Hjrir_dIFHw_rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=F57r_Sza5CJU8BPwzdGMt_KzNZw96LZS0IHl8INNF7qgyw8lKajJS1yt8wnHora2mfwfg61YSHZA2BPxCB5MGQcJvJheZCWqfIdeFelp_iVqiL68XFOO0-3Nh8y8Ev8h57-b1xg--bMlO8EghPqoauztW-QCpMGf0oYwbNpSNpzLOQQFdmKnpe38tsEcbQ9ZA8cjwb8rCuCtryF2k71qurqXbyOwGmRWXHkQoP4wxLqT8eeqbJuLCJVB7zDHgxuy5WK2kRNB1DOFXAcPyCHMy27EI1f_5vcPM7Qzi2yuHZ6FlGwQpAypZww65mUfq0FFldP3gQFZAxI3Jhzslh2hMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=F57r_Sza5CJU8BPwzdGMt_KzNZw96LZS0IHl8INNF7qgyw8lKajJS1yt8wnHora2mfwfg61YSHZA2BPxCB5MGQcJvJheZCWqfIdeFelp_iVqiL68XFOO0-3Nh8y8Ev8h57-b1xg--bMlO8EghPqoauztW-QCpMGf0oYwbNpSNpzLOQQFdmKnpe38tsEcbQ9ZA8cjwb8rCuCtryF2k71qurqXbyOwGmRWXHkQoP4wxLqT8eeqbJuLCJVB7zDHgxuy5WK2kRNB1DOFXAcPyCHMy27EI1f_5vcPM7Qzi2yuHZ6FlGwQpAypZww65mUfq0FFldP3gQFZAxI3Jhzslh2hMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=cdCoz95WqYM7rPozUGvvCuK5P5NLceO5CEWlvLjU_gCAdgmIzZYQIcLe51e-ooE6ON36dTPIMyV_UtiMHspOdU7GIR3Tel3OqIaZcwZnf5QJekQ3ewj9BXlA17pNxppN6AH2147TVJQRsC1E4MkgCiF69A-dp-D9SsueOF6gkpdeR95N1ozir7VM426B41giNLfJMQ2W74Q92sWi8TKTvTeryf0nc_4XPnepCII9X1s25Je2ZASYKtem_SXJew8RS9fF1MeNIgncIj6S42tzcVrBTyMYvZNTuyyETH8nx5H9oIqOGyla2UaHi4I2-dtRDcvcGGaGXnq6abA871hC8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=cdCoz95WqYM7rPozUGvvCuK5P5NLceO5CEWlvLjU_gCAdgmIzZYQIcLe51e-ooE6ON36dTPIMyV_UtiMHspOdU7GIR3Tel3OqIaZcwZnf5QJekQ3ewj9BXlA17pNxppN6AH2147TVJQRsC1E4MkgCiF69A-dp-D9SsueOF6gkpdeR95N1ozir7VM426B41giNLfJMQ2W74Q92sWi8TKTvTeryf0nc_4XPnepCII9X1s25Je2ZASYKtem_SXJew8RS9fF1MeNIgncIj6S42tzcVrBTyMYvZNTuyyETH8nx5H9oIqOGyla2UaHi4I2-dtRDcvcGGaGXnq6abA871hC8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=RDVqHooVJ02riP1xJHxzaKtDDfdqjU_PvcbAijV7cflmPPLi8b4iFMVPXRCm30G69lEprkBIzSkSW2eRWQ-I7Xbaguo62CuUChgdadfKvHVK772kDSAfw1kE4b38NxyIv8THkT35uaDQpS0nmjReo136TP9HmdM2yhXDoxI9cZMO7bxBgDAy8MxpAidKXXNniy85LIoPLnyfh9XedQUCkLZGvzZB2doec2fmfUBDb8Yor118xRAs5kQxP1vo4JndcdqIr7HkOy3WBfCAt9zx72Dq6OX30CNCtbi6jiUOE17cWohGa_2XezdM-Um7kcIJFjwokud65WT2nomVXDmVSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=RDVqHooVJ02riP1xJHxzaKtDDfdqjU_PvcbAijV7cflmPPLi8b4iFMVPXRCm30G69lEprkBIzSkSW2eRWQ-I7Xbaguo62CuUChgdadfKvHVK772kDSAfw1kE4b38NxyIv8THkT35uaDQpS0nmjReo136TP9HmdM2yhXDoxI9cZMO7bxBgDAy8MxpAidKXXNniy85LIoPLnyfh9XedQUCkLZGvzZB2doec2fmfUBDb8Yor118xRAs5kQxP1vo4JndcdqIr7HkOy3WBfCAt9zx72Dq6OX30CNCtbi6jiUOE17cWohGa_2XezdM-Um7kcIJFjwokud65WT2nomVXDmVSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=e-aZ33Jx--7aQRwTnzRAG0EZZAXTEFWbGgIVYw9pVBQrZslmHQ_jg4GfMkPgukN9qhYFisj90fyVsG5MGq9Y_WqkWrnMHYf4NjL-cE0L8KGc3K1p7UxYxMgBiq96HbultZGJJuSYJu5TNm4FksLHCGGW4XnZzgVAV4IqR6-T9LLvwe1Ams2w-Sc1veN9s1IPcwp_mopUJe5V3q1JVxNe_Hf23eXfZVQMZ-jq75VQqbG4CRuHlPq7_4BALTJ18lD9gxtfa-T9NJy--HBbhC97Yb2ebv3zMazDPX3H8yCjuw9p2mfm7tqJdXcGv_SFf3SmCD-SAwwCttB18I2q06MyHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=e-aZ33Jx--7aQRwTnzRAG0EZZAXTEFWbGgIVYw9pVBQrZslmHQ_jg4GfMkPgukN9qhYFisj90fyVsG5MGq9Y_WqkWrnMHYf4NjL-cE0L8KGc3K1p7UxYxMgBiq96HbultZGJJuSYJu5TNm4FksLHCGGW4XnZzgVAV4IqR6-T9LLvwe1Ams2w-Sc1veN9s1IPcwp_mopUJe5V3q1JVxNe_Hf23eXfZVQMZ-jq75VQqbG4CRuHlPq7_4BALTJ18lD9gxtfa-T9NJy--HBbhC97Yb2ebv3zMazDPX3H8yCjuw9p2mfm7tqJdXcGv_SFf3SmCD-SAwwCttB18I2q06MyHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=LGxorkM611qMh7WpfiShB6qtARIOoyYxsTCD7_fAaeKJgt6fDXjGJRlfSKyz-_8OY7fcEhWUwIxF-QGuseAlqKUsbGC6WjgscAWDUgWtu2jddum20_eu00odaFhx-qMC3JY2bE7SJPsiWt_95_UptUroraB3fmmkyN4QwWDShvsXsnqB5kfeXa5dZIQLPds9Vhae3BabT1B1mCnkJPQy7F3eIiMCnVFQBN6aicx__ZljbMx-FBRNydzs82E6fzM3NRxocQj2z7Icjq7LaSFfxStp2JRCFx1s0q5MiB2C7r8aj_IB9SNO46FxYDRaC7AEr5-ZPZHF6r5ftJsp59FE_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=LGxorkM611qMh7WpfiShB6qtARIOoyYxsTCD7_fAaeKJgt6fDXjGJRlfSKyz-_8OY7fcEhWUwIxF-QGuseAlqKUsbGC6WjgscAWDUgWtu2jddum20_eu00odaFhx-qMC3JY2bE7SJPsiWt_95_UptUroraB3fmmkyN4QwWDShvsXsnqB5kfeXa5dZIQLPds9Vhae3BabT1B1mCnkJPQy7F3eIiMCnVFQBN6aicx__ZljbMx-FBRNydzs82E6fzM3NRxocQj2z7Icjq7LaSFfxStp2JRCFx1s0q5MiB2C7r8aj_IB9SNO46FxYDRaC7AEr5-ZPZHF6r5ftJsp59FE_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=SVyQ3rMxkbzA6hbteeJ2nOhuXIl8jFWPJvXQMrUIpCt1Maps-MlHEph17Dk2QmbHk14ilstgu535WaytA7sxBDE9iKFEl6Kz3oaS_mcDFbT7CWPX82pF-5Gx1kpNPokxtEgZswCt1LWzgHyrSKiKa_mTtgqoeWeJNtKvsc5zkMivVVbupIP-oWIr26XlEc6Yn9Ml9XrUX501q5pHE6jC4357pdjpMhQ7yrQmHtxPoccnYu3oNDVAUp6NIEMpEtjfF3Tvrc_tlxoNeeSsZBTOttj8Nh07WRB7oRHuUxzyBYNC4ibSjseM7LGllWD4q-0hnSGWMJfcb-_TPQky35RY0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=SVyQ3rMxkbzA6hbteeJ2nOhuXIl8jFWPJvXQMrUIpCt1Maps-MlHEph17Dk2QmbHk14ilstgu535WaytA7sxBDE9iKFEl6Kz3oaS_mcDFbT7CWPX82pF-5Gx1kpNPokxtEgZswCt1LWzgHyrSKiKa_mTtgqoeWeJNtKvsc5zkMivVVbupIP-oWIr26XlEc6Yn9Ml9XrUX501q5pHE6jC4357pdjpMhQ7yrQmHtxPoccnYu3oNDVAUp6NIEMpEtjfF3Tvrc_tlxoNeeSsZBTOttj8Nh07WRB7oRHuUxzyBYNC4ibSjseM7LGllWD4q-0hnSGWMJfcb-_TPQky35RY0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=RfrUysU7t2movZSpeQU3nOR8wkOjHLqrNhH3bSum_aKbx4sMdxGNJ8jGD2wYuiCMi8kGDsVcIIPYLG0ELTzg9fO91_t8rypNBxeWfyHp3ZZBroC8WkPwyCAF4MWGCe9Q6xNeGgqjN4clHyPAGrVspYAwJUK4Z5viKy4nzdIgB6OZxEdjnpLR75__X3Tyqh8nE493i8lLOOlZTBUfBfvfZXbdRO-VEMOXssUvG9uff9sslAlwtUhvg7VkVk_apiQ4QbciRxpTXRMJJQ6XhkcU-rXPTGUKACmQ_nwpKgDRnMz3n5WNxwBYKLZuRPIZIo5MB3o2gu8zSHFFncbtWuo68Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=RfrUysU7t2movZSpeQU3nOR8wkOjHLqrNhH3bSum_aKbx4sMdxGNJ8jGD2wYuiCMi8kGDsVcIIPYLG0ELTzg9fO91_t8rypNBxeWfyHp3ZZBroC8WkPwyCAF4MWGCe9Q6xNeGgqjN4clHyPAGrVspYAwJUK4Z5viKy4nzdIgB6OZxEdjnpLR75__X3Tyqh8nE493i8lLOOlZTBUfBfvfZXbdRO-VEMOXssUvG9uff9sslAlwtUhvg7VkVk_apiQ4QbciRxpTXRMJJQ6XhkcU-rXPTGUKACmQ_nwpKgDRnMz3n5WNxwBYKLZuRPIZIo5MB3o2gu8zSHFFncbtWuo68Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mek8ufGOQhG8yu83H_-Fe0Q26-DEmsQpFxY4CRAqwoL6-rQQYdgqYIVabzvoALUQO-yxTqt_lGylFK1WkgXbKja9Sg4ALjVs3LEf0kVD641Xe9Gaf-CzsBXoI3hXUvSSD5BogiXBawCZOwT4UYDxJz5n79-CEtKjamWyJnc-qyJxcl69KJMdYu3IY7wztBAuHdjlnAHGQQXYMnBREdX_5orUSBQm6hQjpP_IA_-yxnQShVpkTpnN7oiIwMgfB-uDYEQtKd6wBvuDXCjKWo2owNk-CfUhnBIzh2S9LmA1ri12PBKlm2G_v0sNiJjcmTmB8JJ0IGYNpwmtn-FHiofZVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=vFMeVavZg0cpXlg4vPl6vxr4hF9K6E_3sayVvXyAo6N8WlFB3TBMJ01GC4D_Kx3jy74PYn3M7857AmXjNiBaGhUaa8hE2_tizQ7eFI8h1uxZv63k3JhsmK0hAXRJ1TJ7tZtd8L28I_sO1aSUS-_tAlxreFpKHGQMmvXUPQQxJLPHslof442U7WJXAWFYueF522Pe05CiwEi-Atw7SmF_8tiy8L2kM0nUYU3ti-RRFTUoGLwVe4tQbCMez-6vS6RVQfMxJ1nkV1zvQQIljmjRg8BkIbqcb0ww7dLHmc56kuj9SbMzUiJq0Wnd1CZ_ZPERIRUM9_eJvM8oBmFeq4ZyXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=vFMeVavZg0cpXlg4vPl6vxr4hF9K6E_3sayVvXyAo6N8WlFB3TBMJ01GC4D_Kx3jy74PYn3M7857AmXjNiBaGhUaa8hE2_tizQ7eFI8h1uxZv63k3JhsmK0hAXRJ1TJ7tZtd8L28I_sO1aSUS-_tAlxreFpKHGQMmvXUPQQxJLPHslof442U7WJXAWFYueF522Pe05CiwEi-Atw7SmF_8tiy8L2kM0nUYU3ti-RRFTUoGLwVe4tQbCMez-6vS6RVQfMxJ1nkV1zvQQIljmjRg8BkIbqcb0ww7dLHmc56kuj9SbMzUiJq0Wnd1CZ_ZPERIRUM9_eJvM8oBmFeq4ZyXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUO3yFnlOkpamTdGpkSfHixqVQ_vjtgH4fanD3i4RgHYfo08sTIvjbtRaFoQLgslRmQOvrklu3yTBowyNvj_jWlPFDjfCJmJyFG4UIyACRiL0it5HOguc5GeY2ppqf_VPR4ksWn1Ah_8eADtHhO9bSaJA1JZAp4rXuV56zXY9xLT5nRWmnCWvSeuHYQqU6JbEfacYj-DoLsLa64vvfQBkYmpS7TaJJUiTow9zGeetqbF3Y5uqLOUCywBRSJ9RMtNiCMNM9Q0b0gEmPdG1oD5a2dbOeZeOQeUldMGJbh-EvxS-mTzlsKy4jyYeMHYuPHBDUZrEv4Hqh92VRHlsVm14g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUzCQwF05p9Dpre9Nh7O_LmLY3EP3XtWr730C62c-MjjnS6HFyjm-hIIy5CSPGjqcgHHOcWG29ae-_PB_4c7jD93wlcVQnDt_NMsDfDM_NRX5P8Ey25ivvOaDhPpSuEhSuocG8SP8me43conZUtszKKNXwP77qhBBODaJmChuACXr_w1NfsarbaMXl9fPtaixvL2O4D0P5Mvxf6e47NoTVvnfM8pq1HHS7a3KTldBkgl-Mz_3ePBtB_PB1ncXAQTM7oCJv26Od_0ujNNzdjc4vb5lHav9QuqQgKDHm7HE4dUsY4-7KV6a3AYNCiuZX6soh6N6mnZbmBnPwyARvrsog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
