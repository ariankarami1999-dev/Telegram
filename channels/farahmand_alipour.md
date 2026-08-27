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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-05 20:40:41</div>
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
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVD3RsqMQXKLNJGO0cFCbRLHgpABJoYJiBm8vqCN3-pYjofGxFAkHh8lideJDhfpIWJrPOydBADSAWa-3YYgn9gx-XTj5yVOQFvaLZTdteJm4KzjiszT3gOTF8EqntrpLz0R6o8DGbDCHPEkHQMLmcH81fOk_9I85RZnlEBJeukgsmAp9fBg8Iu3hidox4L_Ir-pSoWRvMdKOk83CgQtSW-QdJg33Ln2fsiuZmoUTJJ50SLhIQ6W_f1BAX1SfKJ_LeRsNvYViEYBy5p5jkT63R6_mOVFndeq2ayBFPxo-vPWRDIOpnV6ewfezN0A24viBTORQPAdl4vnK4-jdKc-1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsm1E5iyIeqzTbEz6-q6LekU9vZVMTNoAf1weEyd67kY_UdxEQv9GDzU6CoJyglfn7yZYBDS3ruly_P2OCMMoVsE9YuaWzjZXGm9GBJfi1htvWJFvjTsWq5duELgPvriqgZPa3YLrec1Y1g6drvbhW_yGJA5rz-aqdIfO31q6r75-0G6oECbAtP6oJSkPM-UWmUllIcoRuEDTh3J26a-xIcsiM9CjgpUZ1UqS9YwfokwlSTvIqMbgSO6n2OX3SrIpnHiCF2ZpsncMmq0cEoTdBAJ3CziuzQZHYe83bF8vRuQ0fLVmIE0nfhkY75n92EVsFGQDzgoUW6buVJie5vfRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuKOi6q8uhD8BHLQlQ1xEGE6A4m3A6wobbjT9k3DHiUZfzO249u9AXvNcBJVihG1oHXPtzlGr-9QUS5Gbchk_z0vwTfoD9bVqU61gjZhjbAU4jrf-YiOSY0v17SfahT7PsB0ckq4EIPru_I9HYpRkaSWZm0UAnhhOQecQmM5m_cxD4TImivTiq3MOdg5XHyxD3H5cSQOdl8YaP8OujBQW4exJ-d1qLn0KIup4t6-zD5PIonFT5rKMk8BLVLHJB0uMUWtcA3mjouGhDfOiZi5W9MhuqcbVhw2yrJJHttnopyqPLUX_YqRufpIGFHOCdctOw8wRf3wig8GJEDpDBVSLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vgy8AprIeayZF1KkO0YBzo9sy7Q4jiTrUVAJQ98BHuSx1pZNvsbvIPKfPmC9r1V3tAvptG5e8GQbmxo_S3ePe0NWniB7ILsYVWxFKPtktt3pZhcS1GnrUwqIJNc-PHVojh2IogOUjzcoRfHkHoaxKe50yvB0cXew6V9k6zGaMn-nbFkfUie7fixT0UoYQyt4LXVH1mbxLDlSmn8sBMGKilXFzsF9lq-eDKzHXL-6L0Ez18dNjY-ynhgIf_VquiyqZQ1R_bX2Vc5WR8tSumQP9Jr1U8wA7S5T3gLzXlJ2eXDvyBWhvYJk2wqymMevEiqGEVsS-coyBCLal_9JY0u-uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpsPdZT9Whk9BFcMbcS6i4sTFuu1ZdRV2L_2WquOkcn1YCrrdmjlTx_lZcgxOQaKhcjCQmIYoMIVQNoS9lhAMaTM68sDs12DiJI6t_5iqeBXsFFssfU8KLZvPNsc2APLiUSHyecaECQXu5kiME4zG47knPuPcjPJdxNf6KaZ4zrwy6QRoYDp1fAp7FJgf0AgQxLWda82Vru538Za_fuGqt8Khkd2f5JFjKBRBc2R55C0iq5hguUGcsG4cre55dBZIjpejlHhVljQYejjS656_BlquIY-a8rgekEU9aIvNftr4VlJS9Yob3ASTFvKCBF3EZsTXUDvW-vphInqwPCXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO4KolKv_NqPKlz6aixjZwqd1RQlc_2r_7wD3wezm8gK4iyHBDgGKbPoQOanRptJB2GaeS55Q8gCiG2lTvL9R_jPlP8qw8He4NFTmV6jPctB3wXxCdSYNpoejYB8mKw_UlkQBRLmdEbhQJI7exlu_mhK61Tlk7ClsCBble_tLc9WLU_PMRDjCpekY5yYz1jHQm-VVWPkx4F76a230crtrwi3aFkvLoWHgRWXTlD46eo79pqpAFHj6C2wjzoGWTDKMhv9C5lz0fGWUCmuxz6VanKnQb2z3eLhljcQFoRrJ5NLiBvUUiTBf1OOt7bcbXgnRukEMswW8cDQ1-EVAcAA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSvUqoG1NlLOir4bpijQZ9K6amXr2oSEMxgucqI3WHhJtPelY2Xd6o0LGy5sgwNMcHxpI0Dzip5Wp-rpi2Ce7sqOf0TEJ-N0fjLM8On4Gt8h9xvHkJ8-WYUPq_4oL4F8xAimJhN6-jnIimfnkzdMAU8is-3Gn74WqCwNcVa6nP3jzeJKKImUTob0k341d9aEscmDOoliYdSN0_SR5CGMflPFf-cc9SfhKKPP8s-r6lVpl6JvFAPPzD3Y9pv64SuqOVcyUBruGZzF0Vj5awF0nZTQPBHFW_dcO_e9tdL_tXEOI1IR_s0aSeGfjCQ-I2gqg1k036mIJFWr8KW2ZMDykg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSUkCW5yjepsd1K9uwsJXaVWvcUglLGAgIBEZCxUufnzCPXvbyEKI4G51sEJWk95KSIiBynaE1OoPGVVtWjMzyFqUSzHiAECPWjuG38jEsof7cum38DTL-A5CrFoPMgYJEe69NNKhm3g7ntvU8ZoqlUTJmH9L8XtPhAO8KBAVtl3ZvdsB3Qgz7M6Tst0PyhhsyB6lNDOz3awK_F00gIHdp89YR9iDI8ijpPDd2d4PtlGHIDSjsmU68rTA7Wi5e-n-GkhFQ7MSjvaRduTGFbNidXiV6XKxO6jQ7SP2ARIZfGO77VTw6g-jAg_AuDX1eBQQkpMsiHxFMnpeHUf86tB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj9uQUGJb8bNfQvUY5JFNP8W16VPWEV0Csa70AQU9wa14HoPp5n-wdRSfCTd9yMzfKbo_CX96faDHCfSyXg2Hi2ei_qCE1OoHE_wAuF8E8eeazyIibZqWgOYpbPPkidnpZ45r_2F3EPEnxGuMzWxxFiBvaEh-JO1MAAl8anfPxn0kD1RACnRCuzbsrgrJB2rASiB0JIClIE8ZYB-GUfOkAUIuOjUFEXzsRPYDh8AtQkkuDGVJ4S47-aBE1P8xsFRm_0enFRw7hkaBATajQgYxi-D9bQ6vbgcaIttBoNlieuGavAdhAMs52PLYJWQaS_LLhzGwyaHzvn_uWzG8H6emQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFO95H3l0T86xEQczv926Ohb7H8Ynxv8afwgW8wK74RFeSf2Dsdcb-p4_zDs9Lbw4ySIi5yDdcEiYcvIpUbHYi5PqwmZ4hH_hMqg4GMauKZLMSurvjXtk1lcH6hLuUwhUFbba2ETPwF6fXosfSBBl_FVJJ99k4MoTApPGDCWzVBhHAu2IOTVmR-rvzMo-YzW1eRGTsNAMW9q-PMF766N47BWiRBbpcV8eHwheX6vg3EEz5MJgaAZWQ4uC1oIeO0aK0aTo4rRXXFiEUEYepFHBkrEl2Pabv7xnF5uDPkO64BWBZkZcRHHU8Sd3t6AwUpR4Eqk7y6GLQpIKNCzOs-d8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cfevOxRZF4GTnJy7KSEpZnjjxuThv5vRkFLD3_jXzldtrMYEkEO8flLbj8s2Z6e2OwJcAo8NoM_zBaag6N2p_P7p2br67H31PJrZ9Y2ipPNYThBSTZkNxi6kCgvmrF-ds83TInf6x8xaNj1YT75y8uQeTwRIkvpqAweNhG_pmz7NF0NT5WxDhCIZ2kfgdE9DL34PsVMA-tO9uh5Yw2tL1OGjU1lqXkdoPtthzmrXR8yk_SQAAYyvplRQnbMHemPra-NHn5Cg2Udvq4NaCNDso5ZQdnGOO_FEK0qZExe5qLv7HjxTMqzU09svfKVsPaBcC9KCdeBqL8hW7SOhQ3E-2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_sEkr32q4C0t4bWv5jvLhjj77SuNyl2BTRDKV3S5ommLYF297uU0kWgCxIx7vC_GMNzqIeQoMAd3dY8avJeN_R3lhj2T7z4C9AOaiG9wO7go5UjSUKInUH0Hj2xU-szcstEiOio-iCJDUNjoh1SNCUXqEXqn8FWIwKZ9bbFThgM11pOICgUyMwhBK2hkSJVBMYQY9f1n5upZbCynJ-T6mIRn4siH6ns7SgGxEu2u1fcfpQYktO1XeQii_ajfA5z3oaEd7PGGm_qCJ8PuBtyDGNENtSe47NAJ84u3SG7lZ1Ks5scaGPHtJHd795i9ZxQ04-2cclsspPcUcu6tAKXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWGPEe4rwLucQMdlKVZEbd_FAc2oyeEnP-KLtMCZjrB_e4VFdPReOwVD9H1L46VzrVpm173g6FFudNA8urDu-nq3Hgp9Eg_86KoDo5ZeGcy-M35hUxvzlNF5wWllmLenzbdLlKrlYfX1MhXIWirnIDKLspmesiTOHnwRNCa4xbtXjCnjsiboMEHNn50O3idlgHwfI9Hv15_R5gwG2yA8BuKbVBaahK9Z_DxXSqyR0NTAuS7sqFDULv9PLN_oe4sBfzFZPElUGERodMGQYjJydGaytfTHzpMWz-Hej7zDmFFJLyYHuMongjwDty4eW8pHFDH_e8S8vVZtgfOnmZ4jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSdsu_3r3MHGxqwh2anaeEiZu-P0mT7Ght3QbDeKwBHahroY8I8hapMyiaI2AyBbaV1yn36JT5EytBkKImg8HCWJVzAQjjOPxFReQGPJuduVc6mJS75DgriZM6K-gN4ucu_59Jhk-rCV7cvnIzquYpuz46-f1b0jvkijbFT1KCwQkF4HSEwM-J9dVKUmZ6uNyoNw7yOPvxYtluhrhTwEjxFmnKt2z5KfXB96xUb2A4rRA8Vpm02cZBULp705q5aRV8Eobfar5ZJCTU2HvejdUgIkG_mCLZOZpS95tl6mat2MKZlZrAzGPAgr7OOGZeoldidgqP_FMN9qB1EUV0u4fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auxKwlKbRELeKBCcYUyO2s7pgh9OZhD0N-YZ7QlkRNFTuSdFsEIG374pGtBSw4sk3iYRpRQUzqQNldZG9TnaQcEdvlLXjSzoyG0-ane-XJO8bospd35zb0AJzQzXpLydhBnJXyOzdF4zGr_R3aOpPVRvh_aqqmBP84Iq8mG577z084KEguF_2bDeXDjqb0uxunSyZr6qQ1oxhiNMraRq6JwcTHESVo4jY6HIDgmqWqKmoR33bUnwSNn2QFj0XBApK-TNEF4gZRQ_yvZ-Ns34-WEGWTLkPGTedQ0gQkfRxuupm1gKgEwQ5znbHnz-9b7UCjRKpSBwEkgbTUiuLJXoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVOg6bRaC___S4EFQG5Ylp88PK1ZkNjchx8fVepqW3h9j9H2AeTaU3XPXPkAWtSimhYw4t2WMuVYn7jqS-daK6-3FCeOkIOvHg11y7vtO3IUIJBlLZkZ-riN06FBB4T4dFW2JHBfxw5wt_7bbRMIg4ZRC2I7YOc5SOgTFgQIsab6WVxTaisA6yCE7M1c433pLPYRgewHNwRlJx4jCfGkII74_CY2dmFkHLAcAvY7jrlmOaJabn3rEqFBhe0Dq_AEEH9t4unDZaXN0xGSkyEtn5WfrUD5wF8w01s60cc8ydU-rPMJvhPwDANb2R1oSSEdsvBUbRwKrp-PK2MiKE5jeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3GKOgHqE9YOkKokrlSLARO8PX0j5dodcCOdC17jH-cj8unBGPCdWSUORTuKO5j_-Rc-P-ncwcUl0P46JnJtunZXciOPQQ8wEzTTmD39sIT3vDR_uSKcEWSphzR04pXzut0Yio0UAXwjUrviVSUL_VyIsexcZF11HRx4hWFwu0GiplfUE4RHXLT8xVkEPVT2Nb1mq7Uo5CSHTy2bwV6AqabU-VUfguN_lnx7pUMhfp-wx7SeE_EBfZllTyBrsUyd_ryxLwP1cbKZYwC0ueWvi5PDt8LCn-ldBX0UXrMmsPnDeYb8M2Nz6uyoMEkWmnO1Bv5FbVtcK7SiAH_L1Zo3xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVVxDaacvC7U6TyEgweyjPmnq0vaZJFzrL-_7CiJmxu3CMPDGdFHQIjooRN63mvkt1iqMq6grpaeWyni4dYzr1aJfbUOk7v3b-LkouC4LB-rHjIZpOVOF2MfYqrouZyd07Wjtw84Q0kCcnkECVbfEfLkqT78Y2VhGXxlnA7yYfwaMEhgqD_CmYPEOzeBAXvu0Uvxfz0n_jCRVCAQ3Z9D222XaHzd_mIcnu76u-BnOW8rftvsDqAyDOeCP6J2Lcf1XsvclEM2qK_67D79yc5DUfKWhSVTblM47I6324dFjJdCQotv_9UfJjQ6QIKNhLprFbssG1W_T0sO-XOpukK6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1edX-SuphzQM9lauWTa47UEa8qdA6uoGz8YsAG7Ir8YEuwIxFDylFuImKBD_AXiXtsqioZ9nTv_ky6NjGy_YizHZzSdr6h8PWnEiBLvQwXesxEkU_pdWrJCAiD0Lt-8blkawI8VUqO8vhWxImfUv1tVgf6rH3dSxVgN7WupaELPOH3dMl-yXmQ4vAVHnRhXqhJ6PWSId4Nyp5XrJpI2MR77RpGOefCH-WXIbCWhKFJCN0CQws2uMY7O4JK_jejudLTh0hm0tfgOi1LAxj7kFBYcbUBOfdeVfnqsDl_FiMm_pblv-lv43O_XOBsa1gz8xMrORFLtjJQjMOWY65t3nQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYxqB6oB6ZUuu9ZoCFvCGhg0e-izdXmh1epbzzrubwtTN2vhzrRUpBhZsS0kg8sFbJdhGx-631tSMAwb60WVDT-rqnY2kOBMmYgWGJTF9JtuO-N0lxc6tNuyFCzWroOm4PUgzblQD9JPl64R_HJCP3Vd2fNSjoIqrZjQjePxFnUe32H04QHaIYSGOLNKtgPrdpnLi_d0xBOFAbcXEQTH6B25laWQ-onOsjb3WxJgZJdJReCB-LKlcyVI7mKCy_hcJdtVPLSouU07eT1asWNljFvZTfeGRpYOWlo8Z3Af8rRZ6BJg6cHTCAuzvuGZAQ4ci04gECBI7liA0i1jCCFifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4Vkf35ipd9pACfCthUJ2wps69UOODKhQ17R_VWoSi8lrvBsbqsqbIzWheEbG8HbdNC3fJei6-2eiJNuSa4AlaZVtvKTB7NhIXtH1RmyEk1KpTGY89kycB863gZGmzj3_RD8XBRVQlFpNn3i08TySv_j7hwgFyJY6hMb-gM-lok_Yt7cQN6wHRvoHPz8BqNBbANBTpI6EMxnP0bN3crjirSu9myJinFdMMM4kZL5LLJDgdkMVlxDPApn1oN2RvFI5j5bU_YuFinFVieBWZvMoT3Wo6hh_784gbnY1BxanLG_5VC0z5Y0OrEng_MGZi-SKF47kJJwN4SfypPm1hyQYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VX2qKPLoznH-JJy1hqYDH9X68v0LNtOMkPzUNCG2pvhnqbzr3rzVgfQRxMAHz16Pqey_IkqgrVaCkGYI6ARLLwj-iYAX8xePaz-PinJKPAqYcQwW3M4mpY50mEKKJwBvcbd6T5v6dxF9OhI7NdydJmQvmwWEE7eugiFc4uQK4fPjnkifDEwiij1K9R3OnzquGohoAgcT7NaOQ9dqVhw7tI9hIQMDXdX_BBYNgNu3NXWHYeHKMR5-zB-maaWw1lS4NavIRR-igVVOTTpxYFMut8cZ8lrIS_9PPQcgSir_MsriDyFySkbqjE533akd8tU9kX8csTOmTgm6bqKr3qgJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ClWN210_BtPYz4bMsSZ_TR1ToGFVrYuoAqQV2STXcbxgItW-NSBOeDOeIbSu5SJNtyFcRaT3NR4h4Nqjo2IWtV0vrSAQTWwoc_5cNojKIl91WxRmq-i8NsENsC5Dg7yepAkJfBS5f3fYvAvqd8UDQDONx_ojzq6oKmCXkzMNa47JFNqhMlGoEnayvXf1pSq9tBo1AQ8ac7Rdec7j2jA4-UofmK4j18v21jAHTLamOwp5sbAJIBWm3uVk7f7ALP6wOh84kv4p50a9dbd8KEbwcK_TzNGhY2woMAM1YT8HXTx1Szv15A_XzwCMUnlvgGB1ewPTJxd_qiq6VCskiSDyaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O01aSunLRogw355LAZj7-LyLhZmacO74GOe04RNWgeyzDE9UWBAY8i8e0MhBCxJn_rI2q9EtMwPV8vPv54WNFbXxy1ayP1aD4J0KP4MYNoph2VkECmMaVx4tl0inwOAuN2r2l6RahbcC1hNkSQvPG_Q-PvNF1lqVO9C5mhSk00mk8oCOl-Z64lNYNIHod9NVNAdzB7j4PSzAHMuzib-fmsfpmKgxJ5ejY27_3T3_xRoXU3VMSmFmBDEc0rUSJc7fvGPPzSmWVALUefJRL-bazwFha-IqCQtAqDiCCK9eHCElfoWZmI40UaxNxvUwqGw13oa-99lWCCzXWbG77DGe5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CF6L2zSLknIvB1i2CMx7tRvU36OlObcQzPbzEqJKlIOrQQkkSC_gCICv3RgDhB5x8QkAAT9sXelsB17cIOhQ_fQoUM22Yeech8iVVNHCX_bC53FQxl8KYJ1Aj1daC8zNOlfU2QV0Jk0NzTq0uh9uPZcgH70xR1COMa8uLsuEWF5amJAptnR2d4SaEa0b_RkiBnSAfEhRcE0uBiqYqbsa0zzeoxVmE9lzuU-_lYg3dqWE2-92bwg7NrCPzisziXv_8EORDznU2KrVEcVweLPe2MM1kNAG9b4MZe9qUXDfjIlWhFBHAjlE0-oyWq0955xdkbV-uB_qw28cCp89SZydsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OibRW4TgmpPLLcswOcOisVH4C1wllQD_4EbSJ4EEos7YsUyoT7cIkT4ZTDmJmVXcEAzCwclz-MZ49pF1MCk80RvhuKFitVziviv-cE9LB0Trwj_vDLsLbUx_duVrvAJ2O-iK2eNJqKk__zDjNmNoS0wQNcVlDZ9O_HMbz9dGyHwdbaBYcscNTA_8HYf57iiLpAqW9hZ0fz0LYY7d56MkLSUYjOuHp6NEjnB2F71-7zHr2RLpPqy98rC-QnyLf9KoNrnczaszH8IvCj3X8F0MXK4ntdK4azyUBmRiZ4I00oIdN-2skiGVeGhmcRUxbedevO_sghIh0ATNVYWsgWmwSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkkRYzyhO9toLFNMuqGR6Hh5KpRGdkfnLnTPTlrwNSUTBPHe_oUbRqs3I0V5G4QSjG4tjMgqrNxnqvMYzsjfeujrEAbJPEeeezb0WKBtYW3mRmIZsZZ1YDGPSx0TKsBcyDdmqRHnVLKYiwkuyCr_DYdm0_5dzWgyYR92Waj9YnZ_Vr6w74AITp8sJzU9EH1oeZc-k4G4zTtbGj5OTtXqOV5LS1AfkRwvMUfOOzW0hb_SgfupSpeF32H0O15GW_kTs3bfkMP_zpwt5oBwP7Wmz67G8M4n0No11IRBpXzQFMarCpUQ3cHlAu8GrbXg4pdlHLw2AL4Ai5_8gb-zKAIq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ed0ESaa9HhbPP7u4_dUc_DGXUhvJnKn-M717gNmuuPvfKN51YtZH1UYuHXoIrSGwfpnA3a2WFeEJTYFxuYX6N7YvcdHZN2C1Z9Jouvw7EwF3fWr8q2FpMhgcpD9I9X_Mf9X_-879BkdVUx68GhGJmAONvOaz8STWYIeuWi3sa1mRf-CJ6_NfbzajgqUxP3yeVIFSIJb4SBoNqV0c_Ex1O96ZjHMOAOOX31TAv5Dl4GCgNPKYI_XPbceydagXnG65KOwduX7KX3bnH3dxBUhmQx9fp3_GVS2XRlR78l4a_ldTPkekDru8AAk4cdyNPowWIke3ULn2HugN2O5bv1sZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j998YIb0uSZe4iUp2AaUqoHd9IyMj6oqs2iGqDR8B4bcCoc9NNvhi5D6zyJJvWbHFhXAqxZRWPt7xOdQB3Lr-n1zZyUBXFHZXwPzXwdgPcBF3A8QYti0kr162x-EPTANmJAMwYRnJEN2SNpW50ZL1ROQUntA3Qthy7Tw0g2Bi36mJpvxxEyihjjwR7-7kE95UEijanhF8OaJUWO0ZxOUnWoSyeh1I71Qy0E0Vv3s3c4HSDCUZaneqpn2YEq92BENkIj_u18YsnWJSqFHvb4dj9C8BTEWElHZHs8b7IpDJVtJ_ez4OaRfH71sAm7WPJ1wqi_L1gxlga1ecKDC3Tz9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiGW4NnI6xo_D9WwEu4oAkVr9TooZKY0K3V8IITWEkwfkBFi8F0dMZ40RhcuPJtLjkgArVS91iWxV8YNh4yQOE5OpEeGoob9-I2QYhzJ03X_DcflQrzcEFPGWs2eMn4N2DW4zY216C47dJHg3ANjBG_4UfS_egAyJ0ns5BO61IjzyBf6V7nc7twP7-zOrV2H0u3RiKw7JVF2DCXygb6tPdh9uRJ_QCyMdpZXjemErd-H4XnZpwNIPVO6jn51Fh2hLF7VoPPg_QhC_Or8jEyoF3gevf2JZTC-4HhH18g6FgTuYA9j3ppAhGIl9s-x7-30NS8aukwazQfIWalazqHOdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/medegNO6DXWle_Zc0xJexhhOkL7lf2_kr8xZGucCgraPNNwUxnpMpC5ZCe675G-V5SSz6Oikiya_JCCAJPNa5Wzp0zLrkBmMbCBo7ynovfg02bPjAi3fVDERVUDhOABD63aEKRUaZrPONqQucRqU8LjbWtL939PvJlP_y9G6rdguO5eRbehzBDK2IKW6wKTfuDxtKyX4_1w6h2anK64Ypwbh_1Tf5xmpq6HiihwlwB6EOCSigbkEwSTCb_tsvNsbuelYSDNXBOgw91IzsHkPl97E6LyDBkzzL0jhUAA1y5-D7yits70ZUcsARL66ExbO3iLEA9zkZ3eROGSMdrOycg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIiSEKLEoKU3HJrTxDYS1TMsHxCbetPgL3T24tBOkccxSXhdZijc2kIzEC5dnnLBmXFvNpNmL6iXYkPM_mXEvw6pgCttWhK-YR5V039uXaKa3X6So6ECdhOD5-fbW5g2C7YaM_vhg3Gk1GVnbsFH1DoIjdwdXhV1p911UAYMJjXxuhO3awr7v5cfYn1RG1aHx8qKZHFEW_ANdnrBr6N2nVXvJ_E-3HsZNo8R0hzOX4n5umbpEz17ADgUaO0rv-3ckRzqSUHiCRAToApcNHwHNDSe5BP5YTv6MzhpsYDzb9T-RvzUcPZfd9ms4pU5s82g7L2f48pRPvXCS3_WbgVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oc932JLeJ4PPkuaHJTtUgJyQ9qD2RNSS3n51uqMphK8tBgaRrr425v7ye3MNcOphJclZpvBPZWwYvrprmLfw-Xj2HccaNr7Xny7pqu7BiCkh3Ck8bUVOhBejkOTmO7RV4v2x2VezACQr7NjCC6FS7dWJvQ5wKEUe4aMdjUoTWLWvhyudSNe92Y0TF4ApH-WnaLeVo6rt8vkwHfuRqzjpUzEAXXIv0EFW1ZzY1oj87Wo0NOPhH0sG5Rv7OUr6szWH27CzKiGa23nMLWFdwvJvaZ67r1ALOovOxg2t4L8MmFYW5pSY8x1VfP-5Ljxbg-RR5nQJwucZeUx6rVnhoiszKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJInYVKdqAuKS6hDcJJfmCJU5J-bcl8vPG9aA7NGPNqURm5Q0OrA5S8_aB7bURrmVV6gn9xCifMQ7hgWhVEm0T5vdDNMkwtv2b9UBaQQRRHBy8Pjg0L8rR2pb_XBLjYGsShBI4H0lci0lrMl1SLrVwlXySlsEFPXerEF3l6ZUQRKHKKCrWlVD7jy0Rq32a7IpZlL4VGqSH1r4LKAFV-CVCy5C5vLaqiBBlJV6J4E_zcVsTwcy3ztHCTinwpqshUX_AUHe-cEL0L92qZ5MlAuSH5wKdBiilCA_-1QpDgjBJaz3ChlA10MDAalKDfIy9R1Q4gfRJMiAFAVlLocOa_IoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU1-DycaX7VbzhkW6BFsSfLk2iQ6yky1zqptZbMhb-uxSCcsw5R79RJI6px-UWkYRsv6yQOBx9Hs8giuCIOMufBkn31HRhccXPUX6XYqL64-jlbfwW3KFJlcu5Wf-WlfybpRcxuJp8oC3acD_u227t0T9NtqNOpFfmn8EYHXZzvkSaYxAIe-TsyPHMSmTR6BrzFRteINh5T4gGySea8z7Blukk1HukeXM1zUyw-nLKWTb3IcnKehiAW1hFb7Z19PEByOeLjE6DAYkqoGSix8qGPq2m22TQ9WB9d7n23k3qSLfHur114DAnpNV0dcFhpWv5B56GzrJWKdDn623LT7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFAMkWVyYpQsYOWgjyrqMvMIkJPDJp-J3EK1TOKQlXEsFgNfNCXzcsRiCwnPO6C0xsVUOGGZZ8Zp6fxgj6VzKnI1fC54x6twqhS6vpa6XwscR8uqvL0YVUz4EQs_FWwNxRvFGpdM5RFBu1ad1vSkYs9LJ-UQfmOWiCQrk-0n_VWnp9TtsgsfVYsXcyhPs5ktQbMzqEj_obzbpJ527MDzdZxC55szrPM40G2hAvQ5t_9ZzhZYzCxg8xyFzdRyCzWjWswboYSFo2QibK7zn0Z17jOeJr8gm7-8LgK4Tqo0X6baefJchMAV1TJSfmYqSNwBgXnszvdULk_xJLb-MgW0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8yZJlcc6TVgctn6-MCY8jounwGPY-tKY67vTMCLc42BUbYc_Q5a31vAKEP6Stwgm91vc6Z26nonMJBunRTR6OA7te_UMD361PNEFCb2t4QuO8sLgWx-SfPd4hrJleOILKrhjkFXC5UNAN2TRL1t9r7-oba_KqkqUMDamdOhTxPiQiZq5zKzVhejOft6YoJdCz2m4_5dKisFryZEzUOy2uAvFz78itXj0_q95MofuxvgN2qdAosXqXeC1cv2JXiL-0bzKx27-TxV2Wh22tXtgL7ERK3JVfxcBzyEN8JjpGA6CKkKoL3lZRZ01EhgK11rgmJY3rakNZoBKuXpfSRX8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUxDKW7zmmr25VRxk2U9CzdY4t-4Dt1Nxi2O5Ju0BiQvjKHoEwu8_OoAkLdepUxbQzlX4LL1hVbtATsBgLSMSAKsRCB8ZEeQ0XLiWeN3G7b-Wy2MYMIz_qhvm7jUAwcxSH02M-AKbqYucYvj2Lg_-GM3AFaQmZj2p5Pcr8LHP8mkw0_HCF3VyZ5RLeiv_0eG22_q4iD9VCt8mHIM1DCEWgtJY-nHiPcpJhGZyYeLy09_Mr1o8Zqh5Kkwi2ttAU1obaa4G0_xpYtNK-mrYWjC8vrckbe-qpIRHUkdTLYjM9pnsyI7Ak4ECv6jqu2YTsm9Ev14_hKWvKIiC5ks3uhAuQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Gu4HL-q11D9HBAUK_gwmamsm0mpVWfdrD-1ZNPm6uu39ePTFFTU1kDViM_eJmUA-0NDuI4Ng94QPdI1r7MY8v_-9IigqR4MBcSA8ZxfL4vod8HaYwg85kkv3-OVxk5xoKiNiUVua_M3axvaLwS815QiKMrb4CkUgBmfMM5ZV7npJyOV9L86lFl6n3Jpi5lf4VmCZUjUjp5baBqy7cp0zUYeW3F8SAqZMXDLxbzWYTDIFP2XIuzAPwh5Ak-7PBGUzT8fkhZzXFpN4453oz_BbvTnUals2yi1ak96PQ7xorqkMAQuPuk5vp-Q7LmTgFlNvVBbXF8wGo6G1RvEIU5eg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Dq31S7UDlD5_VupTzObqVAuc-UnuE2_04zu0Qx7FCMcGar-ST3YbX7YH7fn_rkuwUrFMtzy1xJ35cKhlyJIKNdwLY1vlzAevEdEWmvjHtHjjPs451FH1F4_u4WBNQV0i6Uhd7Ha0qkOoUDaC6IygfC8hM4jB_YXWEh-QuGuxKnbiCM-feO2Sq83jGrlUbNc1PzjDUcPA1ykPUSKAiG8WzIXEjcLfXd_yNpLGd4DWBUMTdU_I112pTNZGhRYpVelsvpBWU8anukwllHBZpWbQQQvoazS8YQrwZxYNPF1QyUs9LOrFz0boSO71oL7kP1GouhPa_CZvbP-_pc83boWvMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=Dq31S7UDlD5_VupTzObqVAuc-UnuE2_04zu0Qx7FCMcGar-ST3YbX7YH7fn_rkuwUrFMtzy1xJ35cKhlyJIKNdwLY1vlzAevEdEWmvjHtHjjPs451FH1F4_u4WBNQV0i6Uhd7Ha0qkOoUDaC6IygfC8hM4jB_YXWEh-QuGuxKnbiCM-feO2Sq83jGrlUbNc1PzjDUcPA1ykPUSKAiG8WzIXEjcLfXd_yNpLGd4DWBUMTdU_I112pTNZGhRYpVelsvpBWU8anukwllHBZpWbQQQvoazS8YQrwZxYNPF1QyUs9LOrFz0boSO71oL7kP1GouhPa_CZvbP-_pc83boWvMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IJb5rGNJDRB-PaOCYnTKKjZ7p5BvDDnHfashFWKt2L8P0-HH6ROFtO9WH_jOl7QA-20g_2UNRabXJ9DhJ1eQwYoNQ-tQ0CS4T2kwuejMZg7SzMBWvJ_Lf5r4fx_mmqCamn0jV1c525CIsIEmrA9_G7BZncnHglOaHL4L6tgH4RA6S4u7bb5o7_4ClZgT1su5r2WZNuISAvaNl9-1n-_Hu-B6GqZdDN4pVCROagt0kfVZYxOl9PpK0Ru9PTjCORvlg5KZDVLHoYJICCHvePL2qi0DJmSMSgHsUtLA1sWehpk2hVHJld7MoA_vauLqlKgcdAjbqMPFE-KaLRhuT0FUCw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=a5yG3ucbcAOjFLE113YFikt3SvsncLzJo3adKMNOLppkbPdfvWb4cixh4Kg8DcGECypJakbkwcVhJZF9_SYRu7_1w5qHIgp8AAiO3Lu_G-5olfz9VdFHcFOmwZqcJPxS7hzAl-YcuhUnEn2hZH2eE6vNVv_7QkY4J4MSdROE_a-KP-fpg7qF_FxlIXie7JZNwjnIRwYC6Fk3kuaxgHaL4qoA3Uibb6pz4LtM0_YbFvwW_C2B9_PE0M_sCnED9KQoek-4ApB6MOk5Y1I1IR2_vxEFC-KXUR2VXdxIaRrf2EL_B_9A9XvxyPg6JANdbQXX9Hl5Jg1mP1AliwghoKf9ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=a5yG3ucbcAOjFLE113YFikt3SvsncLzJo3adKMNOLppkbPdfvWb4cixh4Kg8DcGECypJakbkwcVhJZF9_SYRu7_1w5qHIgp8AAiO3Lu_G-5olfz9VdFHcFOmwZqcJPxS7hzAl-YcuhUnEn2hZH2eE6vNVv_7QkY4J4MSdROE_a-KP-fpg7qF_FxlIXie7JZNwjnIRwYC6Fk3kuaxgHaL4qoA3Uibb6pz4LtM0_YbFvwW_C2B9_PE0M_sCnED9KQoek-4ApB6MOk5Y1I1IR2_vxEFC-KXUR2VXdxIaRrf2EL_B_9A9XvxyPg6JANdbQXX9Hl5Jg1mP1AliwghoKf9ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1t0Rp7HcTRb5JSEGJI5XLzmzViNiAl5aB2P9-xSja6tLc7-KtlZvDemnHwk-a-ZykwDn67e-0b6PHpPmm-A-uaRvxFUPSGXaj5BIVr8VaM-0y86KLdm-sRNWB2pZQgXACy4A2ez2IzT_S2Afg9hVzkbCr7Ld04NwB7DG9YHiVfplFMO44bU1LIB7n1odulkzmdd8gCaBWA-S0MluCK7XLeY8impVp0HdWYiP7-MSmbNxs1oaKiWNj-oGGc19oGbPJrTUwGiof5nOOvexaG4rgkjrdbQGIMhAQgLnvrOnqHW-nbKOKOGfQg8A1S1gGvTBOCDgfoPU0NTVFfLlh0Pog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhhL1S_33oTcB2Z8VjP214RkEpwURs8V-GhpuY-VJmQ9IPsNJbgXqN-BM0_kTwFJnDfaMtPGVHSoap8xPWUnY8YZMgVwFK1p_6izDG60k-27TCl3m5OW_dQLyE4rXMammOEHgZWUzPLnSGGC26bXCgSMspHIWpmYiiH8KUYKTPbNmLQaeeUH0lYKyNKTnBabtHWdMmieV6eU5ChLBLH2H0_ykN1TkCH2g2Au-4UOG0iL4m-xwGLrrCJ5yeaUJiqH7Q8osqWMbjaOMlFajY4JMfbBX184WCaWt-4EEJG7EYtvvxzZUQ_OtMvba4IKUKGl8_2-gVE3pLFKsy7g5yltXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=EFHgy5XMzju_5pMUwokqyv0oK7dkjG5F1WTXTpFYgk4D85j1MusOOMvKpu0qU0axB4VT--aHX9bHFD9GaiAL2uC0TtX7L0NSzd2VPTuG1gJRP2aYbNoOaUDr6IQWk9e5oEPNicI7H4GbzcC2_GjIO8NrQGAmJf7UvlK5tbVOjlW1ELT2yi_MkhFI9ao_KsD_-dklnrMVwMFDMXNAAfjHa2nIt6uez8f5sQ8BL2S_SBY4hnTtV7jcIGT36dpuVWk667f_oE4TE_FCYclgjkjUoVUSjmQWFk2kuAQw0igiq_-nMJseyWOAeESdxpx5ASvFetjgI2KFzjnjV6s_A19PvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=EFHgy5XMzju_5pMUwokqyv0oK7dkjG5F1WTXTpFYgk4D85j1MusOOMvKpu0qU0axB4VT--aHX9bHFD9GaiAL2uC0TtX7L0NSzd2VPTuG1gJRP2aYbNoOaUDr6IQWk9e5oEPNicI7H4GbzcC2_GjIO8NrQGAmJf7UvlK5tbVOjlW1ELT2yi_MkhFI9ao_KsD_-dklnrMVwMFDMXNAAfjHa2nIt6uez8f5sQ8BL2S_SBY4hnTtV7jcIGT36dpuVWk667f_oE4TE_FCYclgjkjUoVUSjmQWFk2kuAQw0igiq_-nMJseyWOAeESdxpx5ASvFetjgI2KFzjnjV6s_A19PvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-L1QwGYt5-jYx5bLEqbJZtPwRnunhPzuXttXL2cTEiBE-iHJy8XSMhyd7SNibqIWOdkzz7Q6zdvcs_WTByRayqnx6RDFvAuhwQ8guy2P7wgguEC5p5jfuRQODxdpO9YebDL1IV6E999GN9tHp9pU3JUoQXGX4JxQoBEz1r0dZkk-NzZl5cAkiegTGJe7nen2_nhMFGbYtRLpKzVNWCKoEjXenHYZjwetX98G707I1mU3xWszYqkRpw6iPUeodTL3Fzf_yFULpL8npxe4Il2G41aLw2p2WJGz1iLcjbm3alQNXZsnCK9nHR4Fnz2gYUithLxRoAJPkIFBNvYDJtGMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrXkC23_-9GGz6SKqbrUxnU8NMdXuWgDUntA13gksHGOfwkOei26cJbF5wFAAsu6ljfOD4lSPkCpJSVtwnP8QZEH5c0mNds-ThF7xxJyXoN0o_lCih84Av6JJRVhR7I5UJDGu_3Uju3hmO8TIo4jyVS8WtQjB4tOt-YLHz7NO2M64V-X-6AAKp65LpNTF5P1rH2hE79hvQ1n1ZowR8gm3dzLzwTaGUkt2bhBQYOdhCLIV8NHg2cndIuAvANvtXk11QnMWIIE76hZXuMbdIud01ngxcqFOmsSl7_if0ClmggLntF9FkuMQJMCKE80W-5jkTBTPbNcu8eWJr3-MT42Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qydfHbIFOOuFQYWsli7FHJMe7760_lX5JcK5lNGLP-KTKMkOBSQzgA-AcaK3E1yG3gbjRE4z9D7scSZGZ9sK3pGuVJ85jdo4fVP04AyBeB1FhMsLIY2mXEGdU3teta1SdzZtEPOEerPF_zAidkD0l_ZBjPWrbSnCRLw6rWwsw5e9DVWbSFIZZo8oqZHbyjXhaamefqAs3QBEN9ne1OGM--snNm_Widpv_2902NxZShqLEVK62UBVXVk4NMYCEeM-urA3P4_yAezECJY3MaQH86Tjha3sIIH2elosD6xdTTUzxGttAUO2ZVgWGb8BRnQZuv7bb-ocChzsdVQdWOZzcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bMrDn6ur8QxtJtv0lKo5VwgZCFm2YjyojzEGEq8sl3r2ylDuVbO99syTkASKF52kBshy-afRTwlBp5ty6xQH6fEqRq3llneN8NBv5TfSA9lXCtbQGYmtxYBQ6DqHOvNPBw-dKTLJOZsB2fwamalrGULH7875f6d5It539sGV023RjzD082qsTj4BENeegHVfQx6CbckYoLEyEEpCPxxCjkrTZT83UihS8Pu1fIDVNFL8uybqqI9FmfhhhuSpgvV2Z7AK1-dwklzvbE8rC1210MzPrG0eQ4ww_aqzBpVx0gioYkvXrG7X_tGPMcIqJJa2M5rJ9-gblbKE0kSJwadU-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=bMrDn6ur8QxtJtv0lKo5VwgZCFm2YjyojzEGEq8sl3r2ylDuVbO99syTkASKF52kBshy-afRTwlBp5ty6xQH6fEqRq3llneN8NBv5TfSA9lXCtbQGYmtxYBQ6DqHOvNPBw-dKTLJOZsB2fwamalrGULH7875f6d5It539sGV023RjzD082qsTj4BENeegHVfQx6CbckYoLEyEEpCPxxCjkrTZT83UihS8Pu1fIDVNFL8uybqqI9FmfhhhuSpgvV2Z7AK1-dwklzvbE8rC1210MzPrG0eQ4ww_aqzBpVx0gioYkvXrG7X_tGPMcIqJJa2M5rJ9-gblbKE0kSJwadU-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Qol_oRIVjX1p_F99bLnTelV-vQvYdevLDvy6E3RKEL1NDSW9Kyy9tTgd79IDpUQUldGV88th_t68YEfFMK5vXiT7m5O_99n7tOH1i8e0SMDlPYU7pD_iwz1xxZjd6omU36hiZULtodUwXLjZTCkMBLL6CSEvza0_sOyhTMv_DI6jfdeDjSoT1oeITEgMXePNIbjnNLNcq6Mi0byQtetiQV-IeMrhc1Kz82hqYldzAdJj8_Rh8o8JUGRXZUIWxkj7La_Au2ZdR8ltxj-VXwTFIJCqrfFcDYgVx6Q6KgnWy2CoCjSdPe2kaEimO7kd7fYMeomyWdQfCTeeAcnyYP-zrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=Qol_oRIVjX1p_F99bLnTelV-vQvYdevLDvy6E3RKEL1NDSW9Kyy9tTgd79IDpUQUldGV88th_t68YEfFMK5vXiT7m5O_99n7tOH1i8e0SMDlPYU7pD_iwz1xxZjd6omU36hiZULtodUwXLjZTCkMBLL6CSEvza0_sOyhTMv_DI6jfdeDjSoT1oeITEgMXePNIbjnNLNcq6Mi0byQtetiQV-IeMrhc1Kz82hqYldzAdJj8_Rh8o8JUGRXZUIWxkj7La_Au2ZdR8ltxj-VXwTFIJCqrfFcDYgVx6Q6KgnWy2CoCjSdPe2kaEimO7kd7fYMeomyWdQfCTeeAcnyYP-zrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br72htq_pvqRmfWfPWdtSBBLy5wHPlneeZOvLMQHOmre1JbXYGW53r311zHHHHNmd1t9ht1Bw_XVcfC5X92Ao1v3dSSyetMEJj8IPZBXNNEcDbCja9Nb6cltI16tW4IN2pdZ7-wAdJEMw6N9uV0LriuSuxLwM3Q5fQaRZ87Pq2vaGUcV_OtnkurnzP2qfKqz4EJ70Tpw5LNgHxMdDUhW56PC15UXGC6h_9S6oOpg6Cz-r9zBdMN8dlMZWJ_psh9y4wwp6Ajh2qGCaFhbITGoLOU5GA2A1U7duLcwt2cz8cpSRHLNj84ruNaG0b6XrDHAel0h6t07x-_YwfhMSiALUQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnkoPGFY8ZeR-LqrFngZtTBBSR1yyQOLV-7lSEf_Zslnm8RPIcou9ozLF0l_PqtwE2kd82KbllpKnIcfNxqMrD0PI-UwChrs0TBnDc41i5HQlZc5ygUBF5OlMuzpmfPk485x1ESoVuYII-ef2wNK_Br_SVJzXs6N-3omQOsznnBo1zmwxQhP7h-V8yaD6yStxw6yV1Et2F4FTtKPTzsrzss_BKwiBs_QozXK5sbMFH6a6KUJP5uruxncZFVVBRZHaRI_hNSeTzh6bq7NiwxAmzwefm2g-kcCM6bQLsgn5rVDSqhThSJIZ3bwtdJvvnCZyveYIFi4cVH6dqvGrgrQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rl2ike70YYLMtLd9_63GsrKEuH3ygs-9yTL4UBZV-Zs3eJVs7TI6Yt0w7kT8vqDaQ1QPFrr4S66g3aoBh0JMWcDWbJSC2ybvGrAlO4VM_YaUX_MKMmNGxJgApVgYULWAqhSgRTDuq3n1eglrV7cH_tzfecd1A5f5ZIPS77HOKuw3hlMGbOSE_xexlkDI_BtpQ5uXqJ2vI9XRcGuuRAx1e_JBazzSmmNUJqpXxuqSOzqKgCNllAEBmNZ1XvfbAIoPf2bMCWtqZTUxCAKJGqhfF0LzKKUadSlW_NRAdM_lpR5zGDxdJ2sjAjwtLe03SO21lxr8CJcy7JaiN5TjQqWUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHfg5_APQ8e9q89SrKabw0Bs1PktpBeyHttZy5T6_AudCk-A6ItrRSnZjYXHa931COU5PWGkmgBiFe2KXNdQMTgRTg2X5BF8UhMcfSG5ZEmE8Iv2MOubc4dYcNeG1rOVvIihFNecKWbdbUwBwPXmZHGv2v9vsFI5zKtTznAtIAWJSF0EiaxkwXFsQR4pEOjNCeebvT4MNJIJp3fmGuFeqibG_IHzaDYQ9nfwOvxlyiQTmETMumwzIx3kHQHNjZ4vNMix2eEyGhEcS2dCBeH9k9ysR8LMibgi7lEJ_PK_A8g-4oWGAiPN69oGJOG_o9IuLXT19EB90tvZ3S4U_ZM0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ev3Fc-8M7Hos_xXtfm9wicaCdMLTLS6qlYXTkBuvySVs1dcp8roh5314E0TyCYuc8jMAKU_GhGKf9l7R5IoqECiznzITIjO67JsGAACgTRLnN0sXgLL2CPZ1QLbG3xCbDVCXB4HrPZEo7tCS-x5kiVAfQYfPlWxNM6GQRuZlhxhtaVQ09aiDHT81dx3f3Hy1hJDAUQvD_R6VRrG3zo-Y9ikSnFh5KaI4slNUzYS9Hrk_MtWxZyQzUS9P7xy86XvRh3QN2ppPPsTdH4FrzDgAkOLRtbFlo7OBmvPbfS2zPst26dhgY1HT_I1fEinkB3pXW4fOpcg15s2qXYhnN-sjng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJsyHUhk7ckEnUcmw1mSucBj3eYYdrFDIA5qPyDsSHPiLh4V1zalxznTgPIyspdWGivUvCL8IKS_A53t63pvhmj_XXtfhihvlFpa3cb31LTk--5aa9Kn7V5UkSVpz-Z9nv5JrkmRWxRNO1pwP-eIZe6lnFGcmP5oKt8X1nGfpjZ_4W03s0Fk38fmVJJ15EeHk0mlGZdw8E4t9CqFnEKqyBxNzrriv8S_gSLQRC190X8sV9zrrFB7l-s4H1XG4-Xo8NUfSckgN1yecuWmjnvh3E3Fh03M3X-CvzEowvf-HDtPAdYAMVdVWMqTMuITIJBP0kbuYbuQcyZ35LIHJ_QMuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8AobbK426EYJMOrkOX4fSNxFlfwlHJxp13IR-PrAxtnXkB-367nSHeQu211DqsUs0nZEQECCa1E7aDjUc0kRL0DSouiBmCilzDIrGLob-vwffQmacdy4RCT5RWzbPOejkZudgy7PmtO10rfpILlb2KtcQf9MsnKehtlp5Zc48o4if1APvgwZE0QdB6QNfC62WA12kq0TUb_b7mr1r0kcscfpVYiD6OYurmUgiXbAxbssawYh4IQFmmdPwxNNvUcBdYf-Tt0cAPJaNZ0ufu3e07b-_d3t-TqqNlSyLFP5NwZAJ2yB-MGB_uj-3tXXvkCrzWQwe5PiKu5ksSOfBm9KQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=AJAVYjm-dkUeAarv2NbTfVZobtWg3v2LtMFvEVXVaNPnTNqn5cSddGPX9aD6POrRbmdCBvCxSrc-hJJGRjvCFkK0tPVV9KnRuctNWh-Bq_wGvqmr3EZNLVT4kWheKVls6KjUJP-yQCxBduLAqxJCTLpVgvGdxtYfEioLcMsrZBHYOAEMryS3-ruOKc0T7dtkNas2IjCGaI85q1qzka9D1yOSZu3Twds4aki7_XVtZQf6c_dy89lG_fQZY3NibrihfaTRj6g3LEWI4O_a1jxnX315MCwovbeLwizU5O9lF29qmtQsODfg7PQduYpHlK6Fe0af62BalHiUlLQRg7MOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=AJAVYjm-dkUeAarv2NbTfVZobtWg3v2LtMFvEVXVaNPnTNqn5cSddGPX9aD6POrRbmdCBvCxSrc-hJJGRjvCFkK0tPVV9KnRuctNWh-Bq_wGvqmr3EZNLVT4kWheKVls6KjUJP-yQCxBduLAqxJCTLpVgvGdxtYfEioLcMsrZBHYOAEMryS3-ruOKc0T7dtkNas2IjCGaI85q1qzka9D1yOSZu3Twds4aki7_XVtZQf6c_dy89lG_fQZY3NibrihfaTRj6g3LEWI4O_a1jxnX315MCwovbeLwizU5O9lF29qmtQsODfg7PQduYpHlK6Fe0af62BalHiUlLQRg7MOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=jImi_VtlZYSYk_ekFSZUzA2idr2zm7o8YH3kp21_Y37yQ9xQOCxX-DiDFCBKno_p-GfxntojmRhilZsCJ-ZYCYhMEoHVavUi0MJ1nkQcCxCZBktRSpdoTUNjY16Dq5n0FE-z7KBLNRM9XsQYZuEQ-APssakVIfee8ggx3d_ARhD6mAqwrUulW_WN3Vs9u7Bkd1kRA724AzbIoohzwWJY13VwXQFOzxJP_AiBknnFCM-l6SmrCNhgTbRJGyIWR-KHhQk4PaH9Vb2l2TZnHECr6Rxp-JcUpAUqcqZJNiyNaEK6ALL4VKxdYy7WrMRCEjq_-WZQrroJtFCko9Vg9Dgaqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=jImi_VtlZYSYk_ekFSZUzA2idr2zm7o8YH3kp21_Y37yQ9xQOCxX-DiDFCBKno_p-GfxntojmRhilZsCJ-ZYCYhMEoHVavUi0MJ1nkQcCxCZBktRSpdoTUNjY16Dq5n0FE-z7KBLNRM9XsQYZuEQ-APssakVIfee8ggx3d_ARhD6mAqwrUulW_WN3Vs9u7Bkd1kRA724AzbIoohzwWJY13VwXQFOzxJP_AiBknnFCM-l6SmrCNhgTbRJGyIWR-KHhQk4PaH9Vb2l2TZnHECr6Rxp-JcUpAUqcqZJNiyNaEK6ALL4VKxdYy7WrMRCEjq_-WZQrroJtFCko9Vg9Dgaqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=in6bp6iiY2YvqHAkqj2DKMMP2Z6BblT2aqwDeiPEckn7BkEnqO8w7Jtleo94NPh9S5TePervaHtWqKUcIKt0gZP9sr-udNS4l4-w1qJFiljhtiKXbsx6yZT__Obd80hpEXGebrs4hmZLiN1JgJnvf7CvFoCJGpYo45ENm5tG7uDEbMbQvoaP1LAvUxEUV9eAoVxzYVTCWOVmX38aL2g2fXEJTtiLJXX8t2hyF6YbCC1w6O0BhX92xyRGyGASj3p0aHwUiDH9dDzRBaRO9VpiJptK9fK7X-Du6qNaizGzGtpY-YlWZoTgzejYPsTiA1C3wr_BjxFHKsU2NSd6Amp_EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=in6bp6iiY2YvqHAkqj2DKMMP2Z6BblT2aqwDeiPEckn7BkEnqO8w7Jtleo94NPh9S5TePervaHtWqKUcIKt0gZP9sr-udNS4l4-w1qJFiljhtiKXbsx6yZT__Obd80hpEXGebrs4hmZLiN1JgJnvf7CvFoCJGpYo45ENm5tG7uDEbMbQvoaP1LAvUxEUV9eAoVxzYVTCWOVmX38aL2g2fXEJTtiLJXX8t2hyF6YbCC1w6O0BhX92xyRGyGASj3p0aHwUiDH9dDzRBaRO9VpiJptK9fK7X-Du6qNaizGzGtpY-YlWZoTgzejYPsTiA1C3wr_BjxFHKsU2NSd6Amp_EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=qPWwq0RwqqC_p_xWaJcbirR4JeXRaBO8v3_iwV-dzsYA_OttBUWUG1o-DlLuZVssCg_6y9PcRWjBhF752Zyf-qMPmJmTHVgdAvoZy4TKNFDQNer34XnKc5WoBsNdir26bx1omal1jM80UpiZHVN9mMVN_ksplAF3ZwaSHDuWvoDtgyUXCxlQAXIxDO1mi72TWFW8HwYZpoiFuWyGSCv1x622tMecXdyrIytWIs6r6G4hmVXIJ861bPia-n5C-fc2mJwB003xBB4zzG_w7eOHGilVlQbiGvooqT6zzDmXGACAg0heOUKnYQ9pUiNYQQuD-WDCHJvCPa5N5NrcYYNdPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=qPWwq0RwqqC_p_xWaJcbirR4JeXRaBO8v3_iwV-dzsYA_OttBUWUG1o-DlLuZVssCg_6y9PcRWjBhF752Zyf-qMPmJmTHVgdAvoZy4TKNFDQNer34XnKc5WoBsNdir26bx1omal1jM80UpiZHVN9mMVN_ksplAF3ZwaSHDuWvoDtgyUXCxlQAXIxDO1mi72TWFW8HwYZpoiFuWyGSCv1x622tMecXdyrIytWIs6r6G4hmVXIJ861bPia-n5C-fc2mJwB003xBB4zzG_w7eOHGilVlQbiGvooqT6zzDmXGACAg0heOUKnYQ9pUiNYQQuD-WDCHJvCPa5N5NrcYYNdPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=R51f66SFeQuDnb7XzlcgBUltk27byAREp8GJU4KlgtA-2xshWsH54pgZ9-MR64mA8c-V-yJ2cxd787B_x36t1D0ESiitfNd0lgNX2I9t_uayxm8jl8xNn2tq231rFcUWOB8X-fbFs-4rbDKNYG-URfVym7iVFxbWPh9yIAowp_qFOyR8b1uJPG8SmwuUt-5uVanEcYrHEHTCTM4px3FOmVDt1qmMCbIqE05qdIu-q8eWuDITHVKlQSqI7gI6oAygiC2kNCwHSzYR1eYDBOPjemHUrBabe15dxeRhZ8zpXi_gXp6HPL14sc1j2wPd8MUf9cpZGi-D9O9uy1ribpPG8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=R51f66SFeQuDnb7XzlcgBUltk27byAREp8GJU4KlgtA-2xshWsH54pgZ9-MR64mA8c-V-yJ2cxd787B_x36t1D0ESiitfNd0lgNX2I9t_uayxm8jl8xNn2tq231rFcUWOB8X-fbFs-4rbDKNYG-URfVym7iVFxbWPh9yIAowp_qFOyR8b1uJPG8SmwuUt-5uVanEcYrHEHTCTM4px3FOmVDt1qmMCbIqE05qdIu-q8eWuDITHVKlQSqI7gI6oAygiC2kNCwHSzYR1eYDBOPjemHUrBabe15dxeRhZ8zpXi_gXp6HPL14sc1j2wPd8MUf9cpZGi-D9O9uy1ribpPG8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=R0bVVyTJbxhBUSzoCIov8F43wU5EsYqshw1fZy7SIZcDdOfQVPc5ohOxYYRdJxanryA1E0Y8H4y1v_gvikmfVCD6ytyr4KvgIrSlYCD1Kbi5oaUz-zEAL8mwmDpV1BbeWDLd9xUZ3djTxUsA50JuVn39gwFkpH3k1gZIH6xMz3FoXnE40qjnYRsIzPv-rrk2Stgl98KWfcHdorK0sFyND0GrTIFZ-vY0GI6H92zCuLHpAXXUNbIN3901FO1nDtnJR9GBNMSZIBqtZ2CZFv170UtnuWtxRZlWlmgrbNA0WCyBg_YthWgUYpv46a_FBUOhuJOF-4Txt-bVyJG5Eq0atA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=R0bVVyTJbxhBUSzoCIov8F43wU5EsYqshw1fZy7SIZcDdOfQVPc5ohOxYYRdJxanryA1E0Y8H4y1v_gvikmfVCD6ytyr4KvgIrSlYCD1Kbi5oaUz-zEAL8mwmDpV1BbeWDLd9xUZ3djTxUsA50JuVn39gwFkpH3k1gZIH6xMz3FoXnE40qjnYRsIzPv-rrk2Stgl98KWfcHdorK0sFyND0GrTIFZ-vY0GI6H92zCuLHpAXXUNbIN3901FO1nDtnJR9GBNMSZIBqtZ2CZFv170UtnuWtxRZlWlmgrbNA0WCyBg_YthWgUYpv46a_FBUOhuJOF-4Txt-bVyJG5Eq0atA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=bmRwKdX-QD2H_A8RSZ55PoetWL6nL2qK9TBkq3UTAVxe9fjgV2KsNTnseEhCWWjf78eALToNiaRiaN86xJRRZ6MjIVhbAMCHH-bqIBxQl7NmKZxiYk9BolMugRNYj8YV9mo3y5yc13MNBMShQHd6P1tdEL-gUUj3qmew9kplKy3rnJCi42dtAG-6rKBl8TnW3_v4qa4wB-idpEINGsw1qyVJdvLdPS26N5aIuitCisgXNNMqGNA12INL1DwC0-QYhqzfPZMG7sw-ZmqsM7nGnCP52WzX09pcO-9bgkhqLTFFmWtnZAZ5Sd7gd0HKaFAlqXZqk_wrACvJOZnPfBNSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=bmRwKdX-QD2H_A8RSZ55PoetWL6nL2qK9TBkq3UTAVxe9fjgV2KsNTnseEhCWWjf78eALToNiaRiaN86xJRRZ6MjIVhbAMCHH-bqIBxQl7NmKZxiYk9BolMugRNYj8YV9mo3y5yc13MNBMShQHd6P1tdEL-gUUj3qmew9kplKy3rnJCi42dtAG-6rKBl8TnW3_v4qa4wB-idpEINGsw1qyVJdvLdPS26N5aIuitCisgXNNMqGNA12INL1DwC0-QYhqzfPZMG7sw-ZmqsM7nGnCP52WzX09pcO-9bgkhqLTFFmWtnZAZ5Sd7gd0HKaFAlqXZqk_wrACvJOZnPfBNSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV1bQLt6uCB-K0XTV3b-mp_tPR3JrIkU3YyvyaEE1_SqlKsId35-swncYetc6VBIKrMno-4bv5VwN6ssQd85d6OfMlSNlO7SjmEY_Auehog9QNhB6Iwj0sApdMw18MvKGAunIgoVvKVO-SM3cZRFUJmitB_HYTmnaS0ab0sqnEbWdf6h8QsJRBRyYXjeXIndvn6vMpeObL_OxyYLQcv0wlHTxBPWVJ3ABlDVdfuwjtWQKCIV4Wh1xJ7PRygOX7agbWlmoQybg5mf7utpumpqk7IC_zhcpcvg90OdPO5sWM1q2kJEjq0tQNSYYdo87GBCUXEsB1QePPvcvTajYP8NBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=RxIIFOM_vMkYSvt9xVr4S64FB7DlHxEa7GOtZiPeb5opPz4QAoE1Fby3Vc13_EgJQrUlQGyAES1h0Xhs2LmUDoHtoHxJ2nF4hEI1MhlaGfL9enmrSwQBRnPgdtrzzo_HQOWdJ61QAl6tNjiKkjfKXEA4Mx__0qpaysmmnt3taICJP0jyxXtJrm4OoqMX_W13lp9PMbqJEm2Yq7oSgQlIGWXgRmq9e3ADsyO0vyv6Birc8oo4wut7rNDYKbwluXjaZZu-Z9-bDr1s0u__LB7nhgWmxXF0EU_NoONLyM6EewaeWwVD4-yQxyvTQ8nGXRcL8dH19IZpekhSHJ0LfXJKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=RxIIFOM_vMkYSvt9xVr4S64FB7DlHxEa7GOtZiPeb5opPz4QAoE1Fby3Vc13_EgJQrUlQGyAES1h0Xhs2LmUDoHtoHxJ2nF4hEI1MhlaGfL9enmrSwQBRnPgdtrzzo_HQOWdJ61QAl6tNjiKkjfKXEA4Mx__0qpaysmmnt3taICJP0jyxXtJrm4OoqMX_W13lp9PMbqJEm2Yq7oSgQlIGWXgRmq9e3ADsyO0vyv6Birc8oo4wut7rNDYKbwluXjaZZu-Z9-bDr1s0u__LB7nhgWmxXF0EU_NoONLyM6EewaeWwVD4-yQxyvTQ8nGXRcL8dH19IZpekhSHJ0LfXJKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXbSe4laRC07DuCBegxwBYdW75_sPY4R1_e2Lw-kKwroka2QZvR7Up1Vk72VyN7caIH-QyIDJrYRWKdhhCcYQLXaK2WVl4-VA-2hfwFzfoZl-3Cr1rC4UXrr8BmwOplGh5sV2wD5Fsh1Lw_xc7DxDw6N5diKyKVA95pBLycsdYv3lhVUme9hgXJ6RUWnaB1FBc6Pjp6xmYGULP5qwioy7Z8X18G318ZDWpfsE3vejtfYJCdh29MR2-R8aAoQ1MoPyp7CElo7IOJHkoct71WihTyFKSm_k1RqhnHDwNDWfzFVjSdnBLvpORxR-WRGy9n4XpT-0dmBM1TdezHM-roh2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nsXE-gOUU24YQLUs2gwUaLOJXq5QvN_ceIMebW13BFbfMm-UQaGeVdlF7pEdunfCFp8_TxDww8ZvqQ-NGnFcc1ZYJyzMxt6N86JGYQC5fNVsBqzGYbuXLK4EbRhSCi-ksX1Ikk6zaadLi4VTxUUQyvva91WMNi3MPolR0Oybj29qG2VrPgvrphXxwE6MjlIyA6pzSpjS6Gy0K4TjNjnCSzGP7PxlCUNuXaRbg_ZLoCEnFWuUY4-hV4S-7G7P0eEt5pewaxAgzFQXODE6YSAHHn4eSzUnUmEy8lEivZaxoG6ThIpRfiADtx5hbTAA_Jj-WX5MF3MbJ8t9ISloSXi4bg.jpg" alt="photo" loading="lazy"/></div>
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
