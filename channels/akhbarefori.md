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
<img src="https://cdn4.telesco.pe/file/Ps-Lj4siS2NW9JMPFU7CIEXdxb3Q91K0zBsXb-KFCuNPH09DCoNifX2ycnGuDe_RsweuG7gp57CmyJVKN2Exq-omU_RFn1ROC2WPjZSVM72y9tCYYPamNBFzu8eoSssOy3aI1RbdCvy6BFDkg3t2SX-jV09RW_a41Iz67J11xwgYeAfFI5jrGX9_mfYpk-EtDs_2eVQYQTTFuib4Kr_En4357Jw1S_bzEe2WllecsLIwGq-h0L3HmynaYUE4eX8PnhFPp-pGJFCDBIQdxbzPts7WijDpBIt8OKu0atA3QJHdVkc0qB8zBKqS95wvhzrSCSWGOFXxC2A2iZg7slvNSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.33M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 13:27:39</div>
<hr>

<div class="tg-post" id="msg-688145">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATMOPjH4Kdk8FZWHX2Hm_xvseyBGt-Ib8iiJi7A0qmTYseWvLDUTLKTO30j3XwgW0-VdHzQb4SbAUpItCqPtasxozEx81486j0jlQdFwqqrkLJQgWaVmNld_QxKgJVjEQgYanPmFrD5Frk34jTKQAlE57l-m09W5Oq9c2p8aICSwdoQrudB3ZdOdF6gtHBX_owzjEQTP7mk2WCEmsR4i-QWqKfFXc5ngDqGh0X5J9QTUoe5Sr7THEhM4EhSDjzphxVjCEhf0eVhI_Wo1NigJS1Wxxr8k9IlKVXSyGFTz6NoCP00ihpAugMTqidFMvpWXNRL4czMsqbD3FggihlTHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نویسنده سیاسی یمنی: سپاس و ستایش خدایی را که عربستان سعودی را پر از نفت کرد و به ما کبریت داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/688145" target="_blank">📅 13:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688144">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcPcACRU_ZZdfVKTHrjE-NOVweEF_deddVdepqTb1-xvtWuWpJqUCQtFUdhFgv39GkdT2ZUtMQoj_Ka1MMo-QFWmX32u0C7MJqEPgWKsO0kFfd1M81sgmaEobF7acDOj5ZKeiMKT9cQz6GMS8VNMMxX4im_DK2ElrpDWHCvg1uc5kP6tdFmj-WOy51msChStbFWtEEuexOHfGb1HOEmCFtdh3D3eCu9uT4CBz-9Efa5EugkboOqngoD6Vhn3T3q9KqyLVbqJWymV83c1uAqHuWK5PYvfy4nctcq8agtI3FD9NTqgi4P01XKF6ijJ49UzUdoUnMMKl7s25y9xqaJkuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۷ شهریور ۱۴۰۵؛ ساعت ۱۲:۵۵
🔹
دلار آزاد امروز با رشد دو هزار تومانی به کانال ۲۲۴ هزار تومان برگشت و در آستانه ورود به کانال ۲۲۵ هزار تومان قرار گرفت.
🔹
عقب‌نشینی دیروز این ارز که حاصل مداخله گسترده بازارساز بود، دوام نیاورد و با بازگشت تقاضا به بازار، دلار بار دیگر مسیر صعودی را در پیش گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/688144" target="_blank">📅 13:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688143">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA2-CfgAqxUxl6Phnu9HcJTvxd2_4CRKzLyErB2CnF4lBF_QFlpZPlNAeh2c-4Ot7Wud8Zg9KGmhgRbZ-hC4afCUnkYrKEG4rFrC_Mubgdbg2YZh17BkUR9HFh6J1-eo4sXNOaSzYXSpNXwz0d4CtLHc01m1UM37L99F9t7GimZCJjc7tEcuDT6nqD3QcUnE3d2OdbllR-K9EwO8d9exJwEegQ8frp7zs_Y0eOPNaKQgr3qrTxC39Dyn6Mo3vOYPCmwo5axzNrFlX9WVliCU0lim7_kmmbdvZzgLtJQsLof7SWje4HcUKUIiXEIaUxtQAreWtOneT_1RxPT3yn4BEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دست‌نوشته رهبر شهید انقلاب برای آیت الله سید مجتبی حسینی خامنه‌ای
🔹
این کتاب ارزشمند را به نور چشم، عزیزم مجتبی حسینی هدیه می‌دهم که خداوند اسلام و مسلمین را بوسیله او منتفع سازد. و او را هدایت کند و از خطا و لغزش در گفتار و کردار دور باشد. الاحقر علی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/akhbarefori/688143" target="_blank">📅 12:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688142">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBjsIg7BnJkPmO2hq_RftI2IfJfzIwl3IzmziiOQl91iz63V7aG8dGSAuiM2AGQF2CoBRPnrNi0HnCoG691mUFI5-UYaI6G87rTkORaH_ABh2KXQTbHgPejchtj0SOeOyh8NBw43LNtpbnPpPihJExPtmwriPQP1XERDmr_EsGvmCV36dFaKJ24IW5vem1KL0Akkz1VIKttx31--yBQhnoUtONqloMCBiNMo3mBdZgi6z-Lv7eEcFiQhARUfhCRv5L2ePsPM1QdKzSTdME4ThTrqH7g_NS7-T61-oIDpsMy-v14jXTpevcHXtSKSpY9pt4b85XFPtxBE2tXGnmyPOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
قاب فرش اشک حرم حضرت عباس (ع)
یادگاری نفیس از حریمِ وفا و ادب.
این قاب، جلوه‌ای معنوی و چشم‌نواز از حال‌وهوای حرم حضرت عباس (ع) را به فضای شما می‌آورد.
✨
مشخصات محصول:
▫️
ابعاد: ۲۴.۵ × ۲۰ سانتی‌متر
▫️
جنس قاب: PVC
▫️
طراحی شکیل و مناسب دکور
▫️
انتخابی ارزشمند برای هدیه و یادمان معنوی
💰
قیمت:
۱.۳۹۰.۰۰۰ هزار تومان
✅
قیمت با تخفیف ویژه
۱,۲۹۰,۰۰۰ تومان
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop
@ghararshop</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/akhbarefori/688142" target="_blank">📅 12:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688141">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p05PZQzdrmKeXwF4G0D61ty3hwDvEkDIOnV3v_xHx6ZVSb4FoNmIuY_-csMPniOPkUS9CwMcjfeLJ0vRyugCvX9ddKwxfEhEjbzQp65wGnDNKLmUFcXXqfbtbP8PT7lrt4RRK9zhFLlaf2sSBWG5fijiqrC5teUF4cI7kDb_5WGvK2NaubKgXNn8DqH87FyVPaGvemhe7brbwQquv3ByhxIjuW7cVVoXMnrKtKQWZTFs8BQIZ4hksmUm2rQTbVHBkFKW3Rbva82v6lRoToItppoqBWwWVQUf8G8hQfpqQfCmhRp6owsGJRiaFZagDVBs2B2igUd5cjdnmy2GSFPH6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ به مقاله وال استریت ژورنال اشاره کرد که در آن ادعا شده: سران ایران خواستار پایان جنگ شدند #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/688141" target="_blank">📅 12:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688140">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3H4nEGb_f1JiXwYX6NsKEejuWbbugDjZoPdO8Q08WEqmhBSoownojNkhjbl1Cj3DFVo7dgyCB-fHJcgqCtVF30DHDv-Kiqr97M_mSYIwDNh3lZC9nSa-Y5Hg88IDjd_I6P_9DsjOCARg7awciKQtPY8Oou7F47ReN_FVaDJw_lYHd8y3EioZYey7LejxO8WEUFBi42lmfe30RwNyb_lL7WwGUZ0D1PxEBL2MicD7aJCXsWH2ytcbO1sLMxK43Wmq-z8o8yBxhUkZduuP4n0ecrDD85BXFB18ye9E5uSeyGVbDSi3DPdZ_dwjaEqxhYbCVGwc5-lEaPElJ1pXIQCMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بورس امروز را ۷ میلیونی تمام کرد؛ شاخص کل بورس در پایان معاملات امروز با افزایش ۱۶۷ هزار واحدی به ۷ میلیون و ۷۵ هزار واحد رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/688140" target="_blank">📅 12:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688139">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
سخنگوی دولت: قیمت بنزین سهمیه‌ای افزایشی نخواهد داشت و فعلاً همان ۱۰ هزار تومان خواهد بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/688139" target="_blank">📅 12:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688138">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای خبرگزاری آر‌تی: آمریکا پیشنهاد جدیدی را از طریق میانجی‌ها به تهران ارسال کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/688138" target="_blank">📅 12:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688137">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/224582e68f.mp4?token=c-EeQpfznJakXIALRJJFtFxl1d21mItdw1xhLHes7mzOufWSESJ0130lSBhyge1WCCg2a9-V1zzWlViH6I9ds3AcDNJev-hDY67aMhpCzxUWWzNl6jbpD2xggnDMPP6dWDUrD095oUuYtb2U2v92ftlID40VC7jY6MjDqZbQvTIY3Rv5DcFvqYQ8LqiJb5gmCxx2qMJWl64vspflGumVdk_v1A4zCJCIXHV0kInLh__zIjLgl9VC9u6GiW1MefGBx9uWNM5snmG793aKoFrIZJTkopANskRPuUIN2lDHvsehmGSodQTH6Bim8aGJGaKN20L7OH3s5VOAVOsTc59uEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/224582e68f.mp4?token=c-EeQpfznJakXIALRJJFtFxl1d21mItdw1xhLHes7mzOufWSESJ0130lSBhyge1WCCg2a9-V1zzWlViH6I9ds3AcDNJev-hDY67aMhpCzxUWWzNl6jbpD2xggnDMPP6dWDUrD095oUuYtb2U2v92ftlID40VC7jY6MjDqZbQvTIY3Rv5DcFvqYQ8LqiJb5gmCxx2qMJWl64vspflGumVdk_v1A4zCJCIXHV0kInLh__zIjLgl9VC9u6GiW1MefGBx9uWNM5snmG793aKoFrIZJTkopANskRPuUIN2lDHvsehmGSodQTH6Bim8aGJGaKN20L7OH3s5VOAVOsTc59uEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ عجیب هوش مصنوعی به این سؤال: اگر شیطان بودی، چطور مردم را بدون اینکه متوجه شوند از دین دور می‌کردی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/akhbarefori/688137" target="_blank">📅 12:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688135">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YHIUTibyW8NaR5ESNCkVbHaClEk_Ir_KtgdQxeL1UGytrSnSd2fb2V_OIc114aK8Wb1YCCMY9BANN7aKh3BM9idj2F9nKsZBJIBU-71pe2Id0xBYJB9Dta2gkuCEVqfqa7dlor-Hd3gKY_MEmO7l5dO3pGGlN1koZSLT2Vy6CPjDdxHD-RuGcLjRO6lgkr0LG_Xy4H-jJV0gRXNBjpIidnBETOaJPyb8fO0UD4nhqBstXZXruhl4GB-pjomb-P3ZAxpKPtAIwqaB6up6rUb0lyvoKGKJwTeaQzY-X5zjHBLIRaH_UkxZOgKTimP1bO950_07Vf4e5C4J5CBxi46RBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/101d1a835a.mp4?token=CPogoVFBxJBRvPts2F-TmSs_iMiyz_9s0o5hikA-3U5smuBMnimzwW4n8PC_y7gShvbZDYrWjkHKKY7JpEbUn2nv4ie8rTh46-tdnT8RxtQu-UlHEo7HIf4jmnO4lFH5E7-vDyuNgCpLaU53V6mmTUESLGS166kyK054rG0LphOPnFu5pL6l-1PXjX02bJM0-WBldvg99jRBuCN_ariOfxoVnoCLnZxTSN82ESw4I-040N1b-Jl22ZNA5axOwIzPQr5wa_pCBf2bkqEFVp0MHYEarpsKr5ImuydhyOr_hXglsYS-XHd3DyLA8MgWRjXlwI-ikx6ld2MT63cVBiEcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/101d1a835a.mp4?token=CPogoVFBxJBRvPts2F-TmSs_iMiyz_9s0o5hikA-3U5smuBMnimzwW4n8PC_y7gShvbZDYrWjkHKKY7JpEbUn2nv4ie8rTh46-tdnT8RxtQu-UlHEo7HIf4jmnO4lFH5E7-vDyuNgCpLaU53V6mmTUESLGS166kyK054rG0LphOPnFu5pL6l-1PXjX02bJM0-WBldvg99jRBuCN_ariOfxoVnoCLnZxTSN82ESw4I-040N1b-Jl22ZNA5axOwIzPQr5wa_pCBf2bkqEFVp0MHYEarpsKr5ImuydhyOr_hXglsYS-XHd3DyLA8MgWRjXlwI-ikx6ld2MT63cVBiEcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی نیروهای مسلح یمن: شرکت نفتی آرامکو و پایگاه هوایی خمیس‌مشیط را هدف حملات متعدد قرار دادیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/akhbarefori/688135" target="_blank">📅 12:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688134">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d8a875842.mp4?token=a6HyhIicy0uhmOYUaX7hN-IWib8lSXoN7nM69qUkUUm0WmMOVWdqRBNRRu9m35cOsafm90WP_6yFnzjneaXM6whFaLgXiMh-Jk3QhksSv1tqqrUdP63JgiyVUtzvQkF1nvBBn6f_cU6BKQJWGxoYn96EEJGxW2gUvtzkLt-ab5wu4YaOkgOaLP4xdW3iMCotZVvtb5xyYGd-Urgw6QWHpKMiRXfkiPliTrBuf75nDfHmvmsP67vI7N73NeFEnOKskaOis6RhCMIwUVkKLmJFswrbXdVSDCb0b4nGpzwbIfJOAHOJMtjoC_YZDgiWX6Nw04UIQRIi1lkQ91BFxtvyRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d8a875842.mp4?token=a6HyhIicy0uhmOYUaX7hN-IWib8lSXoN7nM69qUkUUm0WmMOVWdqRBNRRu9m35cOsafm90WP_6yFnzjneaXM6whFaLgXiMh-Jk3QhksSv1tqqrUdP63JgiyVUtzvQkF1nvBBn6f_cU6BKQJWGxoYn96EEJGxW2gUvtzkLt-ab5wu4YaOkgOaLP4xdW3iMCotZVvtb5xyYGd-Urgw6QWHpKMiRXfkiPliTrBuf75nDfHmvmsP67vI7N73NeFEnOKskaOis6RhCMIwUVkKLmJFswrbXdVSDCb0b4nGpzwbIfJOAHOJMtjoC_YZDgiWX6Nw04UIQRIi1lkQ91BFxtvyRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تماشای دنیای مخفی حیوانات، لحظات شگفت‌انگیز حیات وحش
🔹
دوربین‌هایی که با تشخیص حرکت فعال می‌شوند، تصاویر دیدنی و نادری از حیوانات در دل طبیعت ثبت کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/688134" target="_blank">📅 12:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688133">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
سقف وام ودیعه مسکن از محل اوراق در تهران به ۴۰۰ میلیون تومان افزایش یافت
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/688133" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688132">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyT2Cihq1cRTLzTnBVicynblySbO5DoaK2IXNXqbj8zI3z7oKjp85npcVgyRBsb4Hp_rlX1GxDxrJdFcVh9Z8GfnS1_wJpf7dEgdZgz9qGCtQ4p_UJ3iFxH7k5QN-GWzOJGlVszuPwezrIqi3_kKwpD63s1gqdxssATBulf7dU638LAFHUk3sOiySsI-PTaxD5AbYJIGeKgFuIq_VDvhXsrtfOU5qb9w2uNiYHu1KRXlwSdQ6KzTnSSAeGPFDp1cfKkQpTRhx19_c1hRbj9RaJ3w5qVATj3UNK4Ig69X8NAMNDrk-3F8dkPA9njsWWVZcYinvkfNQUZMTMM_BLJMFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حسن روحانی: امروز باید کاری کنیم که جنگ عزتمندانه پایان یابد
🔹
حالا شاید کسی بخواهد تا روز قیامت بجنگد!
🔹
یک اقلیتی بوق و بلندگو دارد و سروصدا می‌کند، این افراد غیر از اکثریت جامعه هستند.
🔹
تنگه هرمز هم نباید تنگه جنگ باشد؛ از تنگه بی‌رونق که هیچ کشتی عبور…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/688132" target="_blank">📅 12:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688131">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/087dff43ee.mp4?token=DXVfG7WJLSjN8klsQRIWJfzhKLz_ZKLgfl1LDOSgnbdZx2BX2BAQnIajlc0KQMapm50VmF9yex77xqgGqEq7ylltDV7zqNg45_YXpPh_TTqkaDPgrz-D8EF2_ITZMd4aeFT_kWn9shhKtEt6aGVDLJ_pI5ZAdvIAMW0VFEP9jHUpKewrCKIwOw6QvVCmJaOMiiiBwUR20t11YcLl3TP-vk_JzYuAEMFtpemY0jUt8I4knfktWPO3X_MrKceUsZt9REuyf4kyaF6SCSwvf5Yp87GfdTJJNdtcj1DtsFALM8RT-9yZ8Oq0sx5DHlK0QWj7le50qyyR6X5dSxMNNuiXyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/087dff43ee.mp4?token=DXVfG7WJLSjN8klsQRIWJfzhKLz_ZKLgfl1LDOSgnbdZx2BX2BAQnIajlc0KQMapm50VmF9yex77xqgGqEq7ylltDV7zqNg45_YXpPh_TTqkaDPgrz-D8EF2_ITZMd4aeFT_kWn9shhKtEt6aGVDLJ_pI5ZAdvIAMW0VFEP9jHUpKewrCKIwOw6QvVCmJaOMiiiBwUR20t11YcLl3TP-vk_JzYuAEMFtpemY0jUt8I4knfktWPO3X_MrKceUsZt9REuyf4kyaF6SCSwvf5Yp87GfdTJJNdtcj1DtsFALM8RT-9yZ8Oq0sx5DHlK0QWj7le50qyyR6X5dSxMNNuiXyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دوستی‌های زنانه سمی‌تر از دوستی‌های مردانه‌ان؟
#سلامت_روان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/688131" target="_blank">📅 12:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688130">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZP65itD7vcPdGSuVaDVKwwCsWctvNSavylL4Jwd2NngBwd_vQyKBMm83hHkX1sJZ-8_2tgZkkPW8V7DhFMCrWXDz07CwmVmSMZDa3yFnqtnJorawhtsFWPdCHz0DuPNVGip1o5BIqkQVX3ZPSB6Hs3N4_obCJNTne4x7LJK8BoF6LzfYs1wKHSnu_xbhGfxtbI_F5pNkZ_5keQ9ACqGx5MVj5lwo9PWJegvIdeSQxx-xMeEchqXpgj5P7eDJSMLVi7Cy8X2b5cuRhS9-HGQD_kshh8J0Tv5KR4lzG5jHMMoc9nE9Fbwr2RFlqKZ-PqTa2wT89DAtMwuAV5B0bAnkkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
تلویزیونت رو به راحتی هوشمند کن!
📌
چرا اندروید باکس دان بهترین گزینه هست؟
1️⃣
دسترسی به بیش از 30000 محتوای رایگان و پشتیبانی از تمام پلتفرم های نمایش خانگی ( فیلیمو، نماوا، فیلمنت ، شیدا و ... )
2️⃣
پشتیبانی از زبان فارسی و هوش مصنوعی
3️⃣
پشتیبانی از حافظه خارجی برای نصب هر اپلیکیشنی که دلتون بخواد
4️⃣
سبک، کوچک، قابل حمل و سازگار با هر نوع اینترنت ( WiFi , Mobile , LAN )
🛑
برای خرید اینجا کلیک کن
👈
👈
👈
done.tech</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/akhbarefori/688130" target="_blank">📅 12:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688129">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
توقیف دارایی‌های سنگین متهمان تراستی‌ها ، از ۱.۸ میلیون مترمربع ملک تا خودروهای لوکس متهمان
سخنگوی قوه قضائیه:
🔹
اموال زیادی از متهمان شناسایی و توقیف شده است؛ از جمله ۲ کارخانه، املاکی به‌وسعت ۱.۸۶۸ میلیون مترمربع، ۳۲۳ سیم‌کارت، ۴ ویلا، ۸۶ آپارتمان و ۸۶ خودروی لوکس.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/688129" target="_blank">📅 11:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688128">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
ادعای خبرگزاری آر‌تی: آمریکا پیشنهاد جدیدی را از طریق میانجی‌ها به تهران ارسال کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/688128" target="_blank">📅 11:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688127">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7BJiHpRSync3BaOUw4HUL5In84SmLGsRE5emJz8mvIK02wtWRvboTkwR3QNbdoXSMeTy2ViAHAb8qFGWx53gi3lbfzrUegVwFF8eiR5iKuUkwM3rsp4opGaFpZyY6_tD_c2VD2_GfDgltSVEb3mjv2xP0tOHYduhGsB8vHiD9wFswg-sOqkM0Ftp1AbGRCcnvhRuNbaggfZR4sEp5Kux_0Vgpq30PrKEo_ZgHejWCxhE96q_iUz_-mRYaJZ0h1VqJzKhCg0BADB3H4ElWyMKEC1_GVUVt8GOZNPB3QGSEJOikp3Jg2sI6dL9igq8SOYuNeQpzvQnxj91i64TjOP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به ۹۹ دلار در هر بشکه رسید و نفت خام آمریکا برای اولین بار در سه ماه گذشته از ۹۴ دلار عبور کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/688127" target="_blank">📅 11:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688126">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
مدیرعامل شرکت پخش فرآورده‌های نفتی: اصلاح قیمت بنزین از ساعت ۲۴ امشب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/688126" target="_blank">📅 11:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688125">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تأسیسات نفتی «أبها» نیز هدف قرار گرفت
🔹
تصاویر ماهواره‌ای وقوع آتش‌سوزی در تأسیسات نفتی «آرامکو» در شهرهای جیزان و أبها بر اثر حملات پهپادی و موشکی یمن را نشان می‌دهد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/688125" target="_blank">📅 11:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688124">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1460a5f568.mp4?token=eeCYH_IzlvJZC-p3PWE0wm5IUcIONUFOVaQJEVdFDJlqfGCQ0hL-gAIr5HlMe8IrS8yVhs7nhFfg0sJUmMRdI1bc-yzvcRSmMhFgLbjXSHmSvc1fOhWHYdD29PpBhY5xdd07KO5Rbr8JPPOoqKCxpddVVAf2PmNEv0B1rMsijDStWhckkvtYXclT3qfqTp9bfP5I32KcE5Boy1iwNikFSt-mDWkAx1EfU8J-jB-Oz2F3ydPQY_0DqaHb6W37v4u4u9fmsD1ifGzTfy92niB1zGryhbre9qT19JvwlM7KJErdCd3qfkKhOrU-UqD1RZhyFSX976TsO4CUtg0O35yN6JIZ_k45WevYaSWpbpPMwYxdETwAILa0X9jj9N4axjsjSei4qhYWhep-UDnotfNEva7AWm8sQXbnU5BpMo8ridj53OFx_ytjQJfEyBCFtbBmInjJvJ1DF9033qkGUs-qos0Cu9d20lTn486yuNCLqu6446mXB0pOJc5rf2aoKEnetGQqhtEON_LMPdgrq6k10p5AZLqGOudRvAAADtcOS1qiWQufHgTE_StvqNQ4P6tdc-UqSzPK04urt-u5BvQnhXQTjgV2fmFZzuxITu8xph4m5yJq2w1wL_Ylnrk8-ewPg1Yerfqkfps0lCKmBj0dccwFNElhYri3QEqCVg6ixUE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1460a5f568.mp4?token=eeCYH_IzlvJZC-p3PWE0wm5IUcIONUFOVaQJEVdFDJlqfGCQ0hL-gAIr5HlMe8IrS8yVhs7nhFfg0sJUmMRdI1bc-yzvcRSmMhFgLbjXSHmSvc1fOhWHYdD29PpBhY5xdd07KO5Rbr8JPPOoqKCxpddVVAf2PmNEv0B1rMsijDStWhckkvtYXclT3qfqTp9bfP5I32KcE5Boy1iwNikFSt-mDWkAx1EfU8J-jB-Oz2F3ydPQY_0DqaHb6W37v4u4u9fmsD1ifGzTfy92niB1zGryhbre9qT19JvwlM7KJErdCd3qfkKhOrU-UqD1RZhyFSX976TsO4CUtg0O35yN6JIZ_k45WevYaSWpbpPMwYxdETwAILa0X9jj9N4axjsjSei4qhYWhep-UDnotfNEva7AWm8sQXbnU5BpMo8ridj53OFx_ytjQJfEyBCFtbBmInjJvJ1DF9033qkGUs-qos0Cu9d20lTn486yuNCLqu6446mXB0pOJc5rf2aoKEnetGQqhtEON_LMPdgrq6k10p5AZLqGOudRvAAADtcOS1qiWQufHgTE_StvqNQ4P6tdc-UqSzPK04urt-u5BvQnhXQTjgV2fmFZzuxITu8xph4m5yJq2w1wL_Ylnrk8-ewPg1Yerfqkfps0lCKmBj0dccwFNElhYri3QEqCVg6ixUE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعلام رای تراکتور و گل گهر؛ خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/688124" target="_blank">📅 11:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688123">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ce3fff25.mp4?token=SuTsrrT-kjA1VwdqCs63cNxDwFTFQJ8NQ9wwpI44RPGUMmjpiLOaA2KJAhylKsXe_3Tv3ikXThHabaNnrIsT4mFGPPp6dmSzvyInhvKZoeMcrwcwIkEj1j6qhsskROmzkCxIhVg2YHLgWL63VmVYs7PntmeBvBDLgQzT9EorZiVHY1qiRTaKiZpGlpIbZEgdO6YCi0P5oOKzMllJNlfRayHtgaLHrC2WLxVDt4Ywtrv33zwr6KsQPelvB_Y-jwNyGsatGcWb4IihbbStG2Or61Fh-kkHOMLOaakrxUYET96rP2dUIGiGlyNA2mDg-c4m1ngRJn82CGf0JHDEZgXKlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ce3fff25.mp4?token=SuTsrrT-kjA1VwdqCs63cNxDwFTFQJ8NQ9wwpI44RPGUMmjpiLOaA2KJAhylKsXe_3Tv3ikXThHabaNnrIsT4mFGPPp6dmSzvyInhvKZoeMcrwcwIkEj1j6qhsskROmzkCxIhVg2YHLgWL63VmVYs7PntmeBvBDLgQzT9EorZiVHY1qiRTaKiZpGlpIbZEgdO6YCi0P5oOKzMllJNlfRayHtgaLHrC2WLxVDt4Ywtrv33zwr6KsQPelvB_Y-jwNyGsatGcWb4IihbbStG2Or61Fh-kkHOMLOaakrxUYET96rP2dUIGiGlyNA2mDg-c4m1ngRJn82CGf0JHDEZgXKlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید کولر ماشین چطور کار می‌کند این ویدئو رو از دست ندید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688123" target="_blank">📅 11:07 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688122">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/964a6d34dd.mp4?token=r8MfFpfOBkcL5Z_x_nCHqPLGhKEIKsCBV-yxAyp54asdGw-RhBgt_8XRg7953DCOJ1XbBRJZEpDgTQwBVU51LTCOVkerAjnAvP1Iva0zUgksXgJf8XGM4dXZQZDs6VZtquxP8fuPPy_p3ly_srzSILjPcHBgoSMqozmhnDI6iBr9CQGHr8oj8wAKdOrkBpsTdjIPcH44kXySoAwb3hhAVa7g_ESVpluo9aEf0IpVAeCualZMJfZSdc9bRTocgoc49ph4VuABq2NlawihSIEF6qcMAz4nSpZv2QYUgASTl2IZiEwcB-qGcHpvp_ACczzLueGoMNLTlNLXlGJKYaeQdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/964a6d34dd.mp4?token=r8MfFpfOBkcL5Z_x_nCHqPLGhKEIKsCBV-yxAyp54asdGw-RhBgt_8XRg7953DCOJ1XbBRJZEpDgTQwBVU51LTCOVkerAjnAvP1Iva0zUgksXgJf8XGM4dXZQZDs6VZtquxP8fuPPy_p3ly_srzSILjPcHBgoSMqozmhnDI6iBr9CQGHr8oj8wAKdOrkBpsTdjIPcH44kXySoAwb3hhAVa7g_ESVpluo9aEf0IpVAeCualZMJfZSdc9bRTocgoc49ph4VuABq2NlawihSIEF6qcMAz4nSpZv2QYUgASTl2IZiEwcB-qGcHpvp_ACczzLueGoMNLTlNLXlGJKYaeQdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای جدید محمدباقر خرازی: کلیپ‌ها جعلی و ساخته هوش‌مصنوعی است
🔹
من این حرف‌ها را نزدم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/688122" target="_blank">📅 11:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688121">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEsAJ2sJwb6O2LlBJF3eJGK7YNpPC3U3639v1tNiecDLIe6QKgNn-MMIp5KHinwjJXv5Z7sD7kSSvrX3PQ8ukrTRYHEya5cfsFsHUkKG6XZJqxA-wHHO9Vau9df_kKHKCIJVcdAfAEmG5H_esTyNMBtdFMDbFIfAcwKS4OKg5u76ilwkM3M3QeGqU-xUk-PfDpu3nVnLMq1KmfWdlgxxejIR3j8m7UfOtB1ChgT9aKqDsisWrWiZdBhub4uVDrea8iZQb7KcTUq0bHgHYu5-5gBJSgXPkbn5ZREHeIuPFGOnwJaLRNK6Kn5eJJAPU0-SSinuUFd3HsUGjOshtZEnIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلیس وایدل رهبر حزب راست افراطی آلترناتیو AfD آلمان
🔹
خودش لزبین هست.( AfD مخالف همجنسگرایی است)
🔹
پارتنرش سری لانکایی الاصل هست. (AfD مخالف مهاجران است)
🔹
دو تا پسر خوانده دارن.( AfD مخالف فرزند خواندگی توسط زوجهای همجنسگراست)
🔹
خودش هم سوییس زندگی میکنه نه آلمان. ( AfD خودش رو یک حزب میهن پرست می دونه)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688121" target="_blank">📅 10:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688120">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار خوزستان(Admin)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O_CIguQeaj6biBotnlMl83OjShlTTvbxmSbh9_CDGFKuIoshpUTb7jxk6rIlTRzh7ARHRfwBhfvDAMni_Gkb8EwERXJ8J8SWfxewIeYnaD4PeKzNqaSEhdKGzEw3fVrwWUWsVEzaMa5QZRP6WDfPO3VAGXn9PLWWKd1s31CVAV7qbokKx7FTxFIko7n-SN0sgqS8cBSJM2muu8KC0wml0_yvL_H95Q_ceXI96vtWowBv8hHwVrJHprEl6NUMlKI-YzF5pC0g4lFbANV0eY3-uZJEcmAZN4kgEdEDe--tn5kK9T94FLCBqHkx9KP-98knQ48qES4CcL6cf6LLGNITjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاکر بوری، بلاگر طنزپرداز اهل آبادان، به دلیل شکایت موسی غضنفرآبادی، نماینده مجلس، به ۱۳ ماه و ۲۰ روز حبس محکوم شد
/ باشگاه روزنامه‌نگاران ایران
#اخبار_خوزستان
در فضای مجازی
👇
@akhbar_Khozestan</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/688120" target="_blank">📅 10:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688119">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
دعوا بین آمریکا و کانادا بالا گرفت
🔹
ترامپ تهدید کرد شرکت هواپیماسازی کانادایی بمباردیر در صورت انتقال ندادن تولید خود به آمریکا، دیگر اجازه فروش هواپیما در بازار این کشور را نخواهد داشت.
🔹
رئیس دولت تروریستی آمریکا در شبکه اجتماعی تروث سوشال، محصولات بمباردیر را فاقد کیفیت کافی توصیف کرد و مدعی شد بیش از نیمی از درآمد این شرکت از بازار آمریکا تأمین می‌شود.
🔹
این اظهارات در حالی مطرح شده که کانادا از ۸ سپتامبر تعرفه‌های تلافی‌جویانه جدیدی علیه کالاهای آمریکایی اعمال کرده و تنش تجاری میان دو کشور افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688119" target="_blank">📅 10:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688118">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13d2a70f35.mp4?token=IzRlTJkYZMaNTJ98lZ0-dlAc0MRYlRKEfXdyyIFO2nje0kEURgFzs3a-i9J1quAYqj5cwUjayDp-_XkDiOefrw6TjhGNwhodPUK82BNal9dBsI2M991BltcbS0-p5-t8uEv_iAxvntX31unfh1fWJ6cuOgTmE2csq1ODuDloazjMbVmPznPehdU05UJZxXAlhUB09DhmtpHkB6InNgStk1LZSw74l84UewlgR42AB90A8KQCufZk5lGaEXCYH0pi3wGOVy_bWGTbkZIyjzMekCURfQlM_uKmGOhs5WznZe9ph1ff1XI1FPbOWoCoJfhxBkbWxx3XfTTQJXEoPIkxpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13d2a70f35.mp4?token=IzRlTJkYZMaNTJ98lZ0-dlAc0MRYlRKEfXdyyIFO2nje0kEURgFzs3a-i9J1quAYqj5cwUjayDp-_XkDiOefrw6TjhGNwhodPUK82BNal9dBsI2M991BltcbS0-p5-t8uEv_iAxvntX31unfh1fWJ6cuOgTmE2csq1ODuDloazjMbVmPznPehdU05UJZxXAlhUB09DhmtpHkB6InNgStk1LZSw74l84UewlgR42AB90A8KQCufZk5lGaEXCYH0pi3wGOVy_bWGTbkZIyjzMekCURfQlM_uKmGOhs5WznZe9ph1ff1XI1FPbOWoCoJfhxBkbWxx3XfTTQJXEoPIkxpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاندوزی وزیر اقتصاد دولت شهید رئیسی: دولت شهید رئیسی در تابستان ۱۴۰۱ در آستانه توافق با آمریکا بود که ماجرای مهسا امینی پیش آمد
🔹
دستگاه امنیتی رژیم صهیونیستی مخالف با توافق بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/688118" target="_blank">📅 10:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688117">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3caf6eb72.mp4?token=MZERdNAwq0dgUvnNAsjSHm8pKTmZuQE1j3LMq9AmihZynfFno1c7ik6XwlLQAoHGGnuv9UUkbVVeMUhJ8JtNq6oEhCIY6R47rDJ8i9nND26-22MDB-6mtRsIAjooZEqpebWvwSI9VZixsh5jr1mtUSgP2ssxh5OZE1CreKMg-xcmgV9owKJv5ejKhRnV9JlhYfXVYz14586GmitEPvqRi6j97XWYy9AYwImB1HayXNHHO1WHrSfldgQxyLqZf5yFax6zBCyuufXETAgl60l_qocyKiXa5vy7RbfphZKR641kDDyetzPHYf0-_4sy_jRlW-MqzeP1B_xt1pPJsb1xeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3caf6eb72.mp4?token=MZERdNAwq0dgUvnNAsjSHm8pKTmZuQE1j3LMq9AmihZynfFno1c7ik6XwlLQAoHGGnuv9UUkbVVeMUhJ8JtNq6oEhCIY6R47rDJ8i9nND26-22MDB-6mtRsIAjooZEqpebWvwSI9VZixsh5jr1mtUSgP2ssxh5OZE1CreKMg-xcmgV9owKJv5ejKhRnV9JlhYfXVYz14586GmitEPvqRi6j97XWYy9AYwImB1HayXNHHO1WHrSfldgQxyLqZf5yFax6zBCyuufXETAgl60l_qocyKiXa5vy7RbfphZKR641kDDyetzPHYf0-_4sy_jRlW-MqzeP1B_xt1pPJsb1xeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرماندار کالیفرنیا: دولت ترامپ آمریکا را فقیرتر و بیمارتر کرده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/688117" target="_blank">📅 10:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688116">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7lKIW_QYmkpWgYi_oFvT2LMllY7rcWGRCY23vU-ytQCxp5eE6WxvJ60h5FTMGOpFCs1Sj9kwytIH4pZ2hbPTmja7VPq2gK5IkhFsAJ_a5fVzKoUCd5DOAplj6PXjOT84wSZ-kgt1bhHdfkLDYFZqoAfuydRG4v1U4vJrGCiSnz8zW_rhP_AO-HhwKtxD0LtIEeUD5AQQ45OFb8IxOFHNE_GqnynWdWi-ttyieZsFrjGnxArkiA4rJrXbOec_CDMbKI2nBnIpRKafd3wFxCJJ4eiZaQISSy5dy5zYX9W9WntXsFA3lE6Xgdmed_cCrPkm70RNr06E_l4gH5UoW5sZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس روز ناسا از الگوی هندسی متفاوت قطب جنوب زحل
🔹
عکس روز ناسا یک ۱۰ ضلعی را در اطراف قطب جنوب زحل به نمایش می‌گذارد.
🔹
این مرزهای هندسی احتمالاً توسط امواجی ایجاد می‌شوند که در آنها گاز پرسرعت در حال دور شدن از قطب‌ها با گاز کندتر نزدیک‌تر به قطب‌ها در تعامل قرار می‌گیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/688116" target="_blank">📅 10:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d96b18f0.mp4?token=BpDZlMoW_XnmcfSg6Lw7YCiRpRDKayacRt8SnFVC_rvKjoTLee_6rv_Gq__aPT2jtR_wGRcQzI7Ib4lGg2oZ4QikxafBDcHzBuRBqUAxclXcxe34DzlxLyxNw2eOJrWxQC3UbaoJpqV85Syzjw_jjDaGmn7YKCAE7ph4XIQjj5qbDK8oQ63mr-KTBau5VowZ6-9kJfzNruU6Y1MzbfB5PEVldNC10BoINq6DPAm02HJf5bZjTKhaad3sWk2xaYsU6x1rpC1l2sBkl6ng3dgsJ9BmOMTla8aRRrTusAHcGWFTEC1ROyouUzYQjNPgPa7t0hA4qMK9znQJzY-H9xfiOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d96b18f0.mp4?token=BpDZlMoW_XnmcfSg6Lw7YCiRpRDKayacRt8SnFVC_rvKjoTLee_6rv_Gq__aPT2jtR_wGRcQzI7Ib4lGg2oZ4QikxafBDcHzBuRBqUAxclXcxe34DzlxLyxNw2eOJrWxQC3UbaoJpqV85Syzjw_jjDaGmn7YKCAE7ph4XIQjj5qbDK8oQ63mr-KTBau5VowZ6-9kJfzNruU6Y1MzbfB5PEVldNC10BoINq6DPAm02HJf5bZjTKhaad3sWk2xaYsU6x1rpC1l2sBkl6ng3dgsJ9BmOMTla8aRRrTusAHcGWFTEC1ROyouUzYQjNPgPa7t0hA4qMK9znQJzY-H9xfiOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در جنگل‌های آنتالیا
🔹
بیش از ۸۰۰ نیروی آتش‌نشانی به همراه پنج هواپیما، ۱۰ بالگرد و ۱۱۰ خودروی امدادی در حال مهار آتش در جنگل‌های آنتانیا هستند و جاده‌های آسیب‌دیده مسدود شده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/688113" target="_blank">📅 10:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688109">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d962a51b.mp4?token=LC3TMvrcHihQHGL4DbRKsgN3HI7VrXWFXYEupsdIzLK22HQDvEkOOEMPGR0gpLZPu_p9jNpUAHMDbNS6Y2Jyq3Y2i5lb8eUD8kxvJyTxjuGK1iphCbt5yv09BGwSOjCdo9QSCRN6Ytyo9ugFlHkwJ-GxoSNIxaqmWflFqVL8YlZ9ZPYmJM0zE4sqsdbUui2WDTPvR-qHu33Qvy7I5Q0daC4hG3MOY9AxArrk8xiFLM4bJO7p2U7LdVZC7f1yOVLcDkqC3PAR_2mAgSgoYVD_XGsMivc-w3cEKhKd8q70SJShvQPIU9L06gUssoYi_AgNo4pQS05d3Ps5vHmtdaKJkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d962a51b.mp4?token=LC3TMvrcHihQHGL4DbRKsgN3HI7VrXWFXYEupsdIzLK22HQDvEkOOEMPGR0gpLZPu_p9jNpUAHMDbNS6Y2Jyq3Y2i5lb8eUD8kxvJyTxjuGK1iphCbt5yv09BGwSOjCdo9QSCRN6Ytyo9ugFlHkwJ-GxoSNIxaqmWflFqVL8YlZ9ZPYmJM0zE4sqsdbUui2WDTPvR-qHu33Qvy7I5Q0daC4hG3MOY9AxArrk8xiFLM4bJO7p2U7LdVZC7f1yOVLcDkqC3PAR_2mAgSgoYVD_XGsMivc-w3cEKhKd8q70SJShvQPIU9L06gUssoYi_AgNo4pQS05d3Ps5vHmtdaKJkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت انرژی عربستان: تأسیسات انرژی در جنوب کشور هدف حمله قرار گرفت  وزارت انرژی عربستان سعودی:
🔹
چندین تأسیسات و مراکز انرژی در منطقه جنوبی این کشور صبح امروز هدف حمله قرار گرفته‌اند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/688109" target="_blank">📅 10:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688108">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8b570d569.mp4?token=lBdrEuo19ueuunfQLL_4_Uyotc_PEiBzoRxfOycb8LMdf2KdXiHax4OnZfIfvHGeXzxoM7FbfmAwaY6ZlH1SBXwlkCGKiE3I3npteBC_rwgyPXdZ7Iqk8oCLZ1O4PW_Z0aEyHABmzrGJ46w5omI0_SuQe_ifipprdpbLsvq6mlJ3ByXZsUm1kZzq9JrEbHeLXK4F5eioHHgz2CibYLaBa2BOrN1WafCzzS4B93n3CeNyzyum18VIhDN9B6wbdD-UAzI4L77Bmr-2RHYj1BImUWhg6QBVmWZmeHZOzhP0pYgGr-RplgZ400Epiq1SweE9IEoPYrvKAAHloqeiCUrgVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8b570d569.mp4?token=lBdrEuo19ueuunfQLL_4_Uyotc_PEiBzoRxfOycb8LMdf2KdXiHax4OnZfIfvHGeXzxoM7FbfmAwaY6ZlH1SBXwlkCGKiE3I3npteBC_rwgyPXdZ7Iqk8oCLZ1O4PW_Z0aEyHABmzrGJ46w5omI0_SuQe_ifipprdpbLsvq6mlJ3ByXZsUm1kZzq9JrEbHeLXK4F5eioHHgz2CibYLaBa2BOrN1WafCzzS4B93n3CeNyzyum18VIhDN9B6wbdD-UAzI4L77Bmr-2RHYj1BImUWhg6QBVmWZmeHZOzhP0pYgGr-RplgZ400Epiq1SweE9IEoPYrvKAAHloqeiCUrgVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این شیرین‌پلو رو هرجا درست کنی، همه دستورش‌ رو می‌پرسن
😍
مواد لازم:
🔹
برنج ۳ پیمانه
🔹
سینه مرغ ۱ عدد
🔹
۱ عدد پیاز
🔹
۲ عدد هویج
🔹
زرشک به میزان دلخواه
🔹
کره ۳۰ گرم
🔹
زعفران زیاد
🔹
شکر ۳ تا ۵ قاشق غذاخوری (بسته به ذائقه)
🔹
نمک، فلفل سیاه، زردچوبه و کمی دارچین
🔹
خلال…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/688108" target="_blank">📅 10:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3525babc8.mp4?token=RIN4K0O6ArFwvPUGx9AefeI0H9XX0oGP3L0bfv9YwOw018KzCJ2232P-HaHkIn59A-e8I-cp47MqqN4PNlMx477eJ4WG68fO6uj1QphYx7knzkdx7dOGw5ipZOF_8xykVeWwSoNxict7aEIVCJxfuk_ZKOoSDvkJ3uqTvqCgiP8d_07rokzM_DBhgely7I6lt6OSZ0xVp5O2p3VCAw1dvVqPdB3bCTLoyGa_pGduxMsEvir9Sw5G90SG3q_roAH8TLH8aHLEqnP0Z_U3VPZ9WH8Xu33zCtrcr9rEz4CZSoQqY1efbWweHE8RDWKliJXfldYOnKcQjhQFy5xqJDC-XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3525babc8.mp4?token=RIN4K0O6ArFwvPUGx9AefeI0H9XX0oGP3L0bfv9YwOw018KzCJ2232P-HaHkIn59A-e8I-cp47MqqN4PNlMx477eJ4WG68fO6uj1QphYx7knzkdx7dOGw5ipZOF_8xykVeWwSoNxict7aEIVCJxfuk_ZKOoSDvkJ3uqTvqCgiP8d_07rokzM_DBhgely7I6lt6OSZ0xVp5O2p3VCAw1dvVqPdB3bCTLoyGa_pGduxMsEvir9Sw5G90SG3q_roAH8TLH8aHLEqnP0Z_U3VPZ9WH8Xu33zCtrcr9rEz4CZSoQqY1efbWweHE8RDWKliJXfldYOnKcQjhQFy5xqJDC-XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادامه فوران‌های قدرتمند آتشفشان کراکاتوآ در اندونزی
🔹
این آتشفشان اندونزیایی خاکستر آتشفشانی را تا ارتفاع بیش از ۱۵ کیلومتر پرتاب کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/688106" target="_blank">📅 09:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688105">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
تکذیب شد/ تأمین اجتماعی توقف پرداخت معوقات بازنشستگان را تکذیب کرد
🔹
پرداخت معوقات فروردین‌ماه ۱۴۰۵ بازنشستگان از ۹ شهریور آغاز شده و طبق حروف الفبا، به‌صورت تدریجی و مستمر ادامه دارد؛ سازمان تأمین اجتماعی اعلام کرد این روند بدون وقفه تا تکمیل پرداخت‌ها…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/688105" target="_blank">📅 09:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688104">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=UegUWi221jb1gKId6x96MOfNge_6KmkY0Wht2cgp_wY7QNjRD-pRk3nJZkSBokSrRzytUwreOJ2f-uW9BuxzzFTrQ_yC2dOHZGr5XJSNmWND-DIwG24U-ilT0ubYg8qOCP99N9ZrH3K_m5W1Q-_Uyc_C3-w-h5h82yGc3PD5Ogy7Hnq3fzb3AiSibmk2k-YKHqKxLFOCMRrDllhaAJ3RGdGHmnu9x1euHQGKNV_36FjSNO3Nf5phuNBkMc-JHMrP0N7U2rige5EiR4xKf16-fB9XdIkxohTwKNMEoPFXdGa8Z2F4R4bJvJFFoJgkLFp2p0PZc6aLigUIq1-mhNK09A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e49b3dc7c6.mp4?token=UegUWi221jb1gKId6x96MOfNge_6KmkY0Wht2cgp_wY7QNjRD-pRk3nJZkSBokSrRzytUwreOJ2f-uW9BuxzzFTrQ_yC2dOHZGr5XJSNmWND-DIwG24U-ilT0ubYg8qOCP99N9ZrH3K_m5W1Q-_Uyc_C3-w-h5h82yGc3PD5Ogy7Hnq3fzb3AiSibmk2k-YKHqKxLFOCMRrDllhaAJ3RGdGHmnu9x1euHQGKNV_36FjSNO3Nf5phuNBkMc-JHMrP0N7U2rige5EiR4xKf16-fB9XdIkxohTwKNMEoPFXdGa8Z2F4R4bJvJFFoJgkLFp2p0PZc6aLigUIq1-mhNK09A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هشدار نارنجی سیلاب برای شمال کشور
هواشناسی:
🔹
امروز برای گیلان، مازندران و غرب گلستان هشدار نارنجی سیلاب، آب‌گرفتگی و طغیان رودخانه‌های فصلی صادر شده.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/688104" target="_blank">📅 09:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3u0q5OJy_UKYUD4Nfz5r8G7PPP4xaagE4P5-hQocVAreY5ZaOkNVWcGbTFVALE91mQqcLj-0dkv_GFXdxVgdnI--JkYF6hjVvf8hGCXf3KJg_AbuVNgNYlC16xZQXlRhG1CInkbWRfghsvogN59TI042F04bP4wnejO-erM7L3-11jY0UlWfWURAJqbdbAzfAlqxJ7q6Eknnae8rnsoaKQmdzISKB0acJG7U0wMrsHVQkzKuSDwtGacjdxbwCGSGkRNFopXrxCiXCOT27QRe35EergFM_GYynPWvjDXsegJGS6exTxX67XDZr9XX1GLpAAT3CS_KRa3yGoQW6N3lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ab820b6c.mp4?token=jDGtAj7q0K_1iDLH8aJ3OrLfIAggUFxaYzqdqGTiWSOCL14dzP73h-yL3dYAdmi4d3VBMKDOPjogMhjfEhrG0OMkL9tVofaZfAdEF-qNF77c1XT1VjHtt211F2VrjdbUUWdKPZuPMnHhp8VSOH-j_s5psI6MmbVrnZAxBol3fdDlS7rShrAmGQD4Kkl62KaMBDU9lP5wKih6ffTOZX5xHO8Er5iRfH4Bi8DjYbzuDLcF8Qnr5Tr8sxtLBy3O2hKRCUpH1wZaDjSN-pMxH-bVG7xp-hzitqDfe_MDcHjJmDGJ_pFkPTXwosPCNbR6Tqvvn7avEe3ArsmIGFpTwpXOpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ab820b6c.mp4?token=jDGtAj7q0K_1iDLH8aJ3OrLfIAggUFxaYzqdqGTiWSOCL14dzP73h-yL3dYAdmi4d3VBMKDOPjogMhjfEhrG0OMkL9tVofaZfAdEF-qNF77c1XT1VjHtt211F2VrjdbUUWdKPZuPMnHhp8VSOH-j_s5psI6MmbVrnZAxBol3fdDlS7rShrAmGQD4Kkl62KaMBDU9lP5wKih6ffTOZX5xHO8Er5iRfH4Bi8DjYbzuDLcF8Qnr5Tr8sxtLBy3O2hKRCUpH1wZaDjSN-pMxH-bVG7xp-hzitqDfe_MDcHjJmDGJ_pFkPTXwosPCNbR6Tqvvn7avEe3ArsmIGFpTwpXOpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از بارش‌های سیل‌آسا در شمال ایران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/688098" target="_blank">📅 09:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
فعال سیاسی عراقی: انفجارها عربستان را طوری به لرزه انداخته‌اند که حتی از لرزاندن شکیرا در ریاض هم بیشتر است
🔹
بامداد امروز شلیک موشک‌های انصارالله یمن به سمت عربستان سعودی رخ داد که هشت انفجار در جنوب عربستان سعودی پس از حمله یمن شنیده شده است.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/688095" target="_blank">📅 09:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688094">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عارف: از هر لیتر بنزین، ۹۰۰ تومان کارمزد جایگاه و ۶۰۰ تومان سهم دولت است
🔹
برای مصرف مازاد، سهمیه ۶۰ لیتر با قیمت ۱۵۰۰ تومان و ۵۰ لیتر با قیمت ۳۰۰۰ تومان اختصاص می‌یابد و هر کسی که هر هفته به شمال می رود باید پول بنزینش را بدهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/688094" target="_blank">📅 09:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
حسن شریعتمداری در کیهان نوشت: اظهارات آقای محمد خاتمی در پوشش «‌صلح شرافتمندانه‌»! و تاکید آقای حسن روحانی در پوشش «‌پایان عزتمندانه جنگ»!
🔹
دقیقاً همان خواسته بر زمین مانده و آرزوی برباد رفته آمریکا و رژیم صهیونیستی در جریان دو جنگ ۱۲ روزه و جنگ رمضان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/688093" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عارف: میزان تولید بنزین در کشور به‌عنوان یارانه به مردم عرضه خواهد شد/ بنزین وارداتی به‌تدریج آزادسازی می‌شود
🔹
استان‌های کرمان، سیستان و بلوچستان و هرمزگان طرح جدیدی برای کاهش قاچاق سوخت ارائه کردند که به تصویب رسید ولی اضافه کردن نرخ چهارم بدون تصویب و…</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/akhbarefori/688092" target="_blank">📅 09:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688091">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
عارف: اصلاح قیمت سوخت باید همراه با تحول در صنعت خودروسازی باشد؛ نمی‌توان خودروی قراضه به مردم تحویل داد و همزمان قیمت بنزین را افزایش داد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/688091" target="_blank">📅 09:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688090">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
کاهش حرکت کشتی‌ها در تنگه هرمز بعد از تهدیدات ایران
🔹
داده های کشتیرانی توسط شرکت کپلر نشان می‌دهد تردد کشتی‌های باری در تنگه هرمز طی روز گذشته به هفت عدد کاهش پیدا کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/688090" target="_blank">📅 09:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688089">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
عارف: اصلاح قیمت سوخت باید همراه با تحول در صنعت خودروسازی باشد؛ نمی‌توان خودروی قراضه به مردم تحویل داد و همزمان قیمت بنزین را افزایش داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/688089" target="_blank">📅 08:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X5Nz1Pty10FaWo1eCFd_CTmuzlZKA2WtJUi9yFnCcwrOQ6vNIRgAs2f7DyEnDMIxnDdBWLcPoe8vGKib31RiM2DUoUOMKE3J7mgj9l1kQsLbnqZQsUN3qXv1X3E5Qen_LGr0qLIJB3tS-3anI6oJeb1W4_bstb1SrSgql-LmG_0GkVqrKkOpOBqYXnvRcZAg6-oE2ixVcAIoM36mlpAdbtDJwb-5_Xi21zTv3Rp28gp_76oZ5fLdLEngJ0wXea1oZfBUu30ExOsanU2hVz3sJmNP2Z_cQkkvpEJkm3Sv-u9K_iBFN_pWiielbFNbOHFq6Tr3E14WntPOpL_vR9mLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأسیسات نفتی «أبها» نیز هدف قرار گرفت
🔹
تصاویر ماهواره‌ای وقوع آتش‌سوزی در تأسیسات نفتی «آرامکو» در شهرهای جیزان و أبها بر اثر حملات پهپادی و موشکی یمن را نشان می‌دهد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/688087" target="_blank">📅 08:51 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688085">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzY9L6hRzJPWWd4rpQG_9lKwfVAQI4Pw_atukQlzD1-FMdPqgadaH4Jp3IafQlB76hT6jK1IeFAPbok6ztDFSeSUW-VrairWfm-hjsBpfFaaC6q4LZnDTlBU7wVHFCXuXkkmBTsPrfb4wxbkCosXDGfvTVhDdNXOw9yqqx0BpDamJQ1n0NiCPd5CJO89Jy9TlaFvEJdtFt4zV7g48_eaqa3RwO85217KOulKeCBs_n9B2U4ROqd4mMKwmVd0Tk3fQo1r-XucXJP-169wW6yldQFGGE4hvAAq5ubNvEkGG5zWDq5oW9uf5Y_-jtdFprwKo9-oGzggx6TMfYSbDC6dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
این تصویر «میماس» قمر سیاره زحل رو در حال عبور از مقابل حلقه‌های زحل نشون میده
🪐
🔹
این تصویر از فاصله ی ۶۶ هزار کیلومتری از قمر، توسط فضاپیمای کاسینی ثبت شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/688085" target="_blank">📅 08:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688084">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_18l3Zuj1KuJS5lNcKthqwvryqo5_asiK-QXqfpNLipDu-21ODySv0jkR-NhnMKMjXSz9TL0W21ha-Vm07dsWZGzHbpb_bCfIwPu53WglQLJIgmSjAYBjOeFGxDl1Hs-sLCNsbaroLpIGkHEVaXxycxjw_FjhA1KIB3nxjit6qexcuKQEPtbyqVxpIsdX6lQcqKrYRyrLX-Vw_o0WtHnjkCABIXbZvccwVJHyCHf59kIbrwEZQDcsR9gNcF1EmLZ-hYhhpTISgErDBbpGlkD0rWz6qeTeturnxIM1xBJGER2Z1KhNcW-znOhDaEqdm0iE-PaLAmhDvsbWVTSdFKXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اشتباهاتی که موهاتو نابود میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/akhbarefori/688084" target="_blank">📅 08:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688083">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e5023397a.mp4?token=iVmgwU9iFUioLJjU5GZp5NfRS8HAcg8k4HvmhcYgWjlHH9UPWSni6FC01QSNC24j2gufb2d8WK5ARm6eUM-zBl4CKREXZCeelui9gTGPsogtr5GeNFKL_VY67c8ngrx8PlPdyD1IVGAVfVXwD1jVBaGmdGcr4T4H7nV2ss45bDvz6nZZIQJu5jz51WjTUxGV182a5J0Ngk6rEAoQCsnSTExkb3ztDdF-boebFhoO27jBvF6_OfN9nrsbJCMBnxpYstCb29R77D--XL3u4xJ3uKMan7_9GtSwNqifLQQOOY_dKyYB_iCjF2dH06du6Hnt1Dox584czOR9MaI276sjeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e5023397a.mp4?token=iVmgwU9iFUioLJjU5GZp5NfRS8HAcg8k4HvmhcYgWjlHH9UPWSni6FC01QSNC24j2gufb2d8WK5ARm6eUM-zBl4CKREXZCeelui9gTGPsogtr5GeNFKL_VY67c8ngrx8PlPdyD1IVGAVfVXwD1jVBaGmdGcr4T4H7nV2ss45bDvz6nZZIQJu5jz51WjTUxGV182a5J0Ngk6rEAoQCsnSTExkb3ztDdF-boebFhoO27jBvF6_OfN9nrsbJCMBnxpYstCb29R77D--XL3u4xJ3uKMan7_9GtSwNqifLQQOOY_dKyYB_iCjF2dH06du6Hnt1Dox584czOR9MaI276sjeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید باران و جاری شدن سیلاب در متل قو
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/688083" target="_blank">📅 08:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688082">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90688b4d2c.mp4?token=dU6UqOUPQkn9s9K9GVnXEblYUZAjs-5snbzdyD46UbK0f7C-JIt2OqctxM739fwyW7fay6XctlAUK2Zz4WmHsTRbi_pEAeSvyLupjGOPJgPHj7zWFJNXLlCJnl1Mk4Koywb82rf46XLkfLE52S-0HCiY27w2r-75njPFQGz465Lkudu7B4sAlVZHLb5kD5JSPMYAlbZtQAN_NVVXG1qg2g0DAibwVfjkkWCQo01KjCp1o_UsTxAfzlAJjdIPk5_Rb326mTDGExME2J4AH9gIe5xtUYjatnu4ciBXPOzOynk5oT6atMZfH46iPl04fxIAQOTvybWWHL4OWN93XoRwYgVnPe7vUyRbG7NztU8pkf-eEN1KpoBbauUCfQIgaXfMN1sUXcihsn3XBAc4JIt2KB5AM25PfjxbNvnSDkanIQ9jRzfJl-wiD7i9eKRE41pOsziDjydIJGBk6Y8cR7HjUPkRlxBTWGO7rbV7SDeqMWi_4_41uUY46h7ZEz1RvvhicxcQumshKPLEDwUOzgd4jljcpaUaI9QgMoMXTepABsW240j7zqbc4IZqVsv5xSw-NWK_rjAGfR6v3-wZyIEJMC8FjIVks_aaaAI1IKBg0MvN1F3mPk4I93rT0k1MU1G1BWrvf75-QsGsk5ZU0TeBNfrkyFC8iz9HeUJ7jGauqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90688b4d2c.mp4?token=dU6UqOUPQkn9s9K9GVnXEblYUZAjs-5snbzdyD46UbK0f7C-JIt2OqctxM739fwyW7fay6XctlAUK2Zz4WmHsTRbi_pEAeSvyLupjGOPJgPHj7zWFJNXLlCJnl1Mk4Koywb82rf46XLkfLE52S-0HCiY27w2r-75njPFQGz465Lkudu7B4sAlVZHLb5kD5JSPMYAlbZtQAN_NVVXG1qg2g0DAibwVfjkkWCQo01KjCp1o_UsTxAfzlAJjdIPk5_Rb326mTDGExME2J4AH9gIe5xtUYjatnu4ciBXPOzOynk5oT6atMZfH46iPl04fxIAQOTvybWWHL4OWN93XoRwYgVnPe7vUyRbG7NztU8pkf-eEN1KpoBbauUCfQIgaXfMN1sUXcihsn3XBAc4JIt2KB5AM25PfjxbNvnSDkanIQ9jRzfJl-wiD7i9eKRE41pOsziDjydIJGBk6Y8cR7HjUPkRlxBTWGO7rbV7SDeqMWi_4_41uUY46h7ZEz1RvvhicxcQumshKPLEDwUOzgd4jljcpaUaI9QgMoMXTepABsW240j7zqbc4IZqVsv5xSw-NWK_rjAGfR6v3-wZyIEJMC8FjIVks_aaaAI1IKBg0MvN1F3mPk4I93rT0k1MU1G1BWrvf75-QsGsk5ZU0TeBNfrkyFC8iz9HeUJ7jGauqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کارشناس بی‌بی‌سی: ایران از نظر تاکتیکی بسیار موفق عمل کرده و همچنان دست بالا را دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/688082" target="_blank">📅 08:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688080">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Syy_cLUA2gzitf6YEVehKWSsVgy_88b6CyDVPC071TGZdlHpKgUCzf1Kyy5_CfoKErJ117y793GSL6qrt93y_WOOR73B83J8oBi8IMDFZbyfAfDKSLuMlS7mkd9xypXDD8VVfapJzs0pY0a-nbOFSK_o7CNVKTN6C9YlGUiqQC8IXMkMZTWCFKHSK1FhjS4NSb5YjqkwTl7iy8eccZH0HZSzRyh_0ZIxaN8MYXO6k4iAYThwRb1qLRBGB7fFaF8WE_MLuo1ox6Wo9DSHk6VGuFHDH2lMSt2MHuAGkykQqkdrnlriVUT5l0-0n5yWMoUQOh8fz3e_d9jIdlOUf5KVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تأسیسات نفتی «أبها» نیز هدف قرار گرفت
🔹
تصاویر ماهواره‌ای وقوع آتش‌سوزی در تأسیسات نفتی «آرامکو» در شهرهای جیزان و أبها بر اثر حملات پهپادی و موشکی یمن را نشان می‌دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/688080" target="_blank">📅 08:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20d805d53a.mp4?token=TMVeUomGgYRaXNnflt9g_HJYh9itt475UPkFoEpM0_RJSvWf8OKDEqZL9JkJ6yOq1lItEgFGXOV7FOy8_qlh7059XjB2u6WpSpD5x2VPUFRfjMWqBdRKqsUI55968Rz-85A5rKAKbWaB8_BGkwADUqKGwAM58xV5KXKX50wLtaUhA2ivJCfWoPR6y_kzlpO5jECOOQYiK_V5jWT7lWUO2sgV_WGYRcuImvOWMEWLskE8ZybbnYonXvoS61ucqvAd7FaJScVC3fRf7kXwS2ZB-YPIE70mz093_RkD3Uho3ddtFw9qhzey0YvCx0uxRQLEavVanUd_yVf6eD7nBs9SPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20d805d53a.mp4?token=TMVeUomGgYRaXNnflt9g_HJYh9itt475UPkFoEpM0_RJSvWf8OKDEqZL9JkJ6yOq1lItEgFGXOV7FOy8_qlh7059XjB2u6WpSpD5x2VPUFRfjMWqBdRKqsUI55968Rz-85A5rKAKbWaB8_BGkwADUqKGwAM58xV5KXKX50wLtaUhA2ivJCfWoPR6y_kzlpO5jECOOQYiK_V5jWT7lWUO2sgV_WGYRcuImvOWMEWLskE8ZybbnYonXvoS61ucqvAd7FaJScVC3fRf7kXwS2ZB-YPIE70mz093_RkD3Uho3ddtFw9qhzey0YvCx0uxRQLEavVanUd_yVf6eD7nBs9SPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکتی ساده برای تقویت زانو؛ راهی برای کاهش درد و افزایش توان حرکتی #ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/688078" target="_blank">📅 08:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688076">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe981b6e7f.mp4?token=EoOC6DctfvqJxPCly3m1g0omsLACAuaG-pbOkQrGmhcK5_K_OlCEngQ_lJEeJOkxzgpHJCkafG2Ehg3-mx88Dh1lNimnaKqHuuNF54HD6IbyCY1s76GlLHxQyhx994yl34TUF_tyH7df08ZGdPU6qJK1sY1e5jZixuEzqkyonxsN1vCbaGMX7w-DrDS3QsXv1k4Jiz91Nfl1GKlujdHyywbw2KIFy-gtyPS1mbtMuT-xxQ5Yvntmv8ElUd7NcHtEifC9pADByVErZPHNBRcZe6p81dfcPZxnTFs4mZs0_AYaIpr-snqQscO4bD7z6ahTZI7xGju6JQ4sFYh2cdKAvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe981b6e7f.mp4?token=EoOC6DctfvqJxPCly3m1g0omsLACAuaG-pbOkQrGmhcK5_K_OlCEngQ_lJEeJOkxzgpHJCkafG2Ehg3-mx88Dh1lNimnaKqHuuNF54HD6IbyCY1s76GlLHxQyhx994yl34TUF_tyH7df08ZGdPU6qJK1sY1e5jZixuEzqkyonxsN1vCbaGMX7w-DrDS3QsXv1k4Jiz91Nfl1GKlujdHyywbw2KIFy-gtyPS1mbtMuT-xxQ5Yvntmv8ElUd7NcHtEifC9pADByVErZPHNBRcZe6p81dfcPZxnTFs4mZs0_AYaIpr-snqQscO4bD7z6ahTZI7xGju6JQ4sFYh2cdKAvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آب‌گرفتگی منازل در پی بارش و طوفان شدید در مازندران
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/688076" target="_blank">📅 07:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688074">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krYCIb1zNxRxhrFQXjDEGO5JKaNhAgAhtdKsXRTSE9uBg1XF56v2GIv4nuMl0fMST4_PFjNSGvnBp_qShHY2Mk3g3HnES_qZt7e_Koxz7wHm2HuphEkDmEL15I-j72I9SlCWRv43kiNpki3L5_VbS6qTta57FVH7WQft9OoPV4ZlXafBPYAR0RebnwwINSR4nhm462kYy--uqfFR49Kl8GF8RM0h7y_jchEQe21Q2CAUBOXBfVMeStnaRC7acqyVwzBXQ0ZFvR7SUohkQeNRbHWGRegd3jika0hMO4y4CFT7S-KzlYLexA4xY3LR1BkyzLAlhjljsGQPun-E6oyjJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: واشنگتن از موشک‌های جدید ایران هشدار واضحی دریافت کرده است
🔹
جنگ اقتصادی با ایجاد منطقه ممنوعه دریایی در سراسر خلیج فارس تا محدوده محاصره پاسخ داده خواهد شد.
🔹
موضع عملیاتی علیه کشتی‌ها و پایگاه‌های نظامی ایالات متحده، مورد بازنگری اساسی قرار گرفته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/688074" target="_blank">📅 07:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688073">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عارف: فیلترینگ و فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند و در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/688073" target="_blank">📅 07:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688072">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
بارش سیل‌آسا در مازندران؛ برق برخی مناطق شمال به دلیل آب‌گرفتگی قطع شد
🔹
بارش شدید و سیل‌آسای باران که از شب گذشته در نقاط مختلف این استان آغاز شده در بخش‌هایی از مرکز و شرق مازندران، علاوه بر آب‌گرفتگی معابر و اختلال در تردد، موجب قطع برق در برخی شهرهای…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688072" target="_blank">📅 07:31 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90746ccf0f.mp4?token=G3cXw-hVZZmmcRI_PjoBmrmW9GBp260O4qehX7jCvUMzhdfBhh15YolldyYI-KAdEmqSUq4R7_aXDfGGuaBBtncGVYMEz575nhjgiCr2BvmHr0oPvt4d-m7PIh8RrV4EzJXaN9elnnNTfMQ5DYYQ7DpSOkErAg6VzsffwVSAb5R2n721h4-X9eWOz6-q2Uw2YGSItr5RxGkhNv3SaXHTDsexWJJtqkHCzTLwDF3Coj23IopC2xt-odowOU1wN_UM6aEptPVwDEfx7diLIKCVjLulMQLnwq56GNzBcIRp4vZb5Jq3J3L44NMKgaxlfTUEnI7JWnlKYX_lwKWN__opQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90746ccf0f.mp4?token=G3cXw-hVZZmmcRI_PjoBmrmW9GBp260O4qehX7jCvUMzhdfBhh15YolldyYI-KAdEmqSUq4R7_aXDfGGuaBBtncGVYMEz575nhjgiCr2BvmHr0oPvt4d-m7PIh8RrV4EzJXaN9elnnNTfMQ5DYYQ7DpSOkErAg6VzsffwVSAb5R2n721h4-X9eWOz6-q2Uw2YGSItr5RxGkhNv3SaXHTDsexWJJtqkHCzTLwDF3Coj23IopC2xt-odowOU1wN_UM6aEptPVwDEfx7diLIKCVjLulMQLnwq56GNzBcIRp4vZb5Jq3J3L44NMKgaxlfTUEnI7JWnlKYX_lwKWN__opQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش سیل‌آسا در مازندران؛ برق برخی مناطق شمال به دلیل آب‌گرفتگی قطع شد
🔹
بارش شدید و سیل‌آسای باران که از شب گذشته در نقاط مختلف این استان آغاز شده در بخش‌هایی از مرکز و شرق مازندران، علاوه بر آب‌گرفتگی معابر و اختلال در تردد، موجب قطع برق در برخی شهرهای این منطقه از جمله جویبار و بروز خسارت در نقاط مختلف شده است.
#اخبار_مازندران
در فضای مجازی
👇
@akhbarmazandaran</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/688071" target="_blank">📅 07:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bjWs_zPKkE5rxJoMAalKQAeWvdPaJND9uz97nK6_fMWoqWwFUG5g3zodCY4eljKdg4hj65q0w6t7iP3WsocrlgItM7Ei-G4fAeNQqBmnCwLcVqpU6YxWDdt2wPvuI7fAS6pLH-m6JRtaNa0NASKLDcf_qrnoZXx-sOGzynDLH0YFj2bRUVusYEagD62v0u41GT_YuPylW9iuZROK9wIkknAhQxOjcLcDOy-yHTS-9HCIjBvf354pp4WyLCVZflIZQzGFGiToY23EQJPZDlHysbq2vFo-4ndI06BCaTs_7TESzj3myPPGkca4AhFPtm2qCSsbuF34anHOfnr2E0K_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۱۷ شهریور ماه
۲۶ ربیع‌الأول ‌۱۴۴۸
۸ سپتامبر۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/688070" target="_blank">📅 07:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تولید و پخش پوشاک مردانه یاشین(فقط عمده)
✅
این پست مخصوص بوتیک داران و فروشگاه های پوشاک می‌باشد
✅
✅
پرتنوع ترین دورس و‌ هودی های سه نخ
✅
با رنگ‌بندی های خفن در ایران و بازار
✅
مناسب ترین قیمت و بالاترین کیفیت
✅
محصول مشابه خارجی
✅
لینک کانال تلگرام
✅
👇
https://t.me/Yashinshow
پیج اینستاگرام
✅
👇
http://www.instagram.com/Yashin_men
کانال بله
✅
👇
https://ble.ir/YSHCOLLECTION</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/688069" target="_blank">📅 01:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076b9568c9.mp4?token=sBPAs2k_bYnepZyFJvh2VbHiJHV7nxb15pYtin8M8OjIxEwA5NWO0PDQKC2-Gw0eK5S95h4ZfkNw6VjbJ0ZzrQXolLjoUBhG7NENhD6rFCExBXXC8yUul8PoWO19eESRf_zft6Kd2WbWX8dl0_9b7crkkt2eKjiGz0WD8uuEb9sG3qXJY3jsrSLLeAlX1CnYDB6fTlH-nBmahCXz1Fr3WxPPAgc-qlMcWzGT_cU3jBVA0a9iyRgKzMOzhf2wS3mX5v3t6V4fivwaDGjHMYHjr0EuStkb8GrsDHbgIv0JQnoGs9WbjCQmxod_Je2syvMehDRCu53SFqy7hS3BgsiIxX9e-05QZW1e8d0WSPLWjP0SlFAP0K0ftuDEz380eIxYFtF0kvw7CGN8NOs8h269SVkbPdKB6Y-ZPPG1PqREKVMVaBBl7kCd6cgzuQqHc47fdUrCyRiKAGQF5oDD7HKd6yEiJEtQL9dkGZogjtRhzIiq2wi2R_lANQLT6mc4hsOan0JxgVomANNofuG0hnoXsVspMRaxmIqInl5fWEXh4Sz--A9VN2YmiAAxu5UGNNoe0qQYAi0RGR_8KmTDxNZ-NpPQrn8Y1BzlDUUvcnz73Zt9QmxlO2TRZxkGuH9d5oHSFB3ujKUqJsK2ruXpGkhlJh2bLmdAZwDXZdyqaIu1y1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076b9568c9.mp4?token=sBPAs2k_bYnepZyFJvh2VbHiJHV7nxb15pYtin8M8OjIxEwA5NWO0PDQKC2-Gw0eK5S95h4ZfkNw6VjbJ0ZzrQXolLjoUBhG7NENhD6rFCExBXXC8yUul8PoWO19eESRf_zft6Kd2WbWX8dl0_9b7crkkt2eKjiGz0WD8uuEb9sG3qXJY3jsrSLLeAlX1CnYDB6fTlH-nBmahCXz1Fr3WxPPAgc-qlMcWzGT_cU3jBVA0a9iyRgKzMOzhf2wS3mX5v3t6V4fivwaDGjHMYHjr0EuStkb8GrsDHbgIv0JQnoGs9WbjCQmxod_Je2syvMehDRCu53SFqy7hS3BgsiIxX9e-05QZW1e8d0WSPLWjP0SlFAP0K0ftuDEz380eIxYFtF0kvw7CGN8NOs8h269SVkbPdKB6Y-ZPPG1PqREKVMVaBBl7kCd6cgzuQqHc47fdUrCyRiKAGQF5oDD7HKd6yEiJEtQL9dkGZogjtRhzIiq2wi2R_lANQLT6mc4hsOan0JxgVomANNofuG0hnoXsVspMRaxmIqInl5fWEXh4Sz--A9VN2YmiAAxu5UGNNoe0qQYAi0RGR_8KmTDxNZ-NpPQrn8Y1BzlDUUvcnz73Zt9QmxlO2TRZxkGuH9d5oHSFB3ujKUqJsK2ruXpGkhlJh2bLmdAZwDXZdyqaIu1y1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
قبل از سرد شدن هوا، هیترتو بخر!
هنوز هوا سرد نشده و قیمت‌ها بالا نرفته؛ الان بهترین زمان خرید هیتر ریموت‌دار
HANDY HEATER
👌
✅
توان ۸۰۰ وات با گرمایش فوری
✅
ریموت و تنظیم دما ۱۵ تا ۳۲ درجه
✅
تایمر، نمایشگر دیجیتال و خاموشی خودکار
🔴
قیمت 1,798,000 تومان
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/35574/180124/</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/688068" target="_blank">📅 01:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhwOiGfAYOHMUvHco1tcB_Do7vAwkKhwsJHDi2RDbFuUXjXRs_yAE838JcU0ro2nXXn-kraR5P4Xe7D-KEgx_nw0JUon2HpbyWnwLEGelmjqhRAwfqji2V_ZTvhuEjVw9wlsUxFzX_pEu9qdb8gYR4xp6beIv2KBR8xCIyS5Ez1wLl1R_1l1DWwlcb2QiyVf_C9RWE8AGtWvyTdGRx9uwZp7_MUfK7H5_AGx1LADloXf7xpiDZwMkv0XUqwRRLZSGhbfqlMExGjRddm5-4Nm8RiIHaoRcsaHvcxj6l32oBnfCoqPCpUuJ73g_o27caSjJDlFjQ5zhqrafVQf6KQnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه می‌تونن با AI محتوای قشنگ بسازن؛
اما چرا بعضی برندها با همین محتوا
می‌فروشن
و بعضی‌ها نه؟
چون امروز مشکل خیلی از برندها «تولید محتوا» نیست؛
ساختن اعتماد و تبدیل محتوا به فروشه.
در
Digital Cast
درباره چیزهایی حرف می‌زنیم که محتوای برندت رو از «فقط دیده‌شدن» به
اعتماد، اعتبار و فروش
می‌رسونه.
اگر می‌خوای بدونی محتوای برندت واقعاً چقدر می‌فروشه،
کانال Digital Cast رو دنبال کن.
👇
🔗
اینجا قراره درباره بازاریابی، محتوا و فروش، متفاوت‌تر فکر کنیم
.</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/akhbarefori/688067" target="_blank">📅 01:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dd2a8dfb9.mp4?token=h6GTlWYdNLT1WIuh_hCOKyG_iJbVZVlupD4jSGf2h_3ymnYDPv1PoxDfrUl55MqO3UU1g-aUfRA1KMj8r4Dj6wV78yLE4a4wM8e9MsIYZ2nIelGCkE3dBgy62fJApYGnP75WHrSPAvtJTHIDcFoLikMOszS21WRfaHwzjpEeawRSL25I-rE65cAtP_f6tXY8a_QOpqb7WTzyeTlvbmz9jO6f1xVipOEjuqiHeTsxu1y_g2Fklcogx6H9a5fmYU_nlwGGQ7qG0wa8mjYw2fkLqVaNIQMDHKiAaYW-uUhhoqRUlhpQEv8unVVNEph3si-Oelpq1eN87FBxheFInNfVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dd2a8dfb9.mp4?token=h6GTlWYdNLT1WIuh_hCOKyG_iJbVZVlupD4jSGf2h_3ymnYDPv1PoxDfrUl55MqO3UU1g-aUfRA1KMj8r4Dj6wV78yLE4a4wM8e9MsIYZ2nIelGCkE3dBgy62fJApYGnP75WHrSPAvtJTHIDcFoLikMOszS21WRfaHwzjpEeawRSL25I-rE65cAtP_f6tXY8a_QOpqb7WTzyeTlvbmz9jO6f1xVipOEjuqiHeTsxu1y_g2Fklcogx6H9a5fmYU_nlwGGQ7qG0wa8mjYw2fkLqVaNIQMDHKiAaYW-uUhhoqRUlhpQEv8unVVNEph3si-Oelpq1eN87FBxheFInNfVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آبگرفتگی شدید معابر رشت| هم‌اکنون
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/688066" target="_blank">📅 00:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
فرماندهی مرکزی ارتش تروریست آمریکا (سنتکام) مدعی شد که نیروهای این فرماندهی همچنان به اجرای محاصره دریایی علیه ایران ادامه می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/688065" target="_blank">📅 00:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95337866b2.mp4?token=lBs5i1f4-qAi9kVofb6yllCbLJEVxwB2oEoUpyLENQC3GcKHqG4SW1mlTea6dj1YIpxMTQPajCR2saABeGrb2alYKqvmlgWTwvd__1YLeWDhDdDvxQLyoAl5RJz0-QrHlAeTnIuWp0DqhKF0FAj4hZ5RiteRBCFqD0XdMZS1PBxVWCg8Uc-qpIjq_MOaACktmKvDrMzuH4C0LJOtjLAZpfX1rgK5ILwDtWVV4w7iQhiJ7ddpYOQKinZPMz-LgQ5B36V3_ZMPAXZyMUp1sak1FY4umeZ6MR1WPPJAn_vEuH7KbI5Kf8dBLI7nNK9SC5511mnT5xVXQ8IWkCztxgypGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95337866b2.mp4?token=lBs5i1f4-qAi9kVofb6yllCbLJEVxwB2oEoUpyLENQC3GcKHqG4SW1mlTea6dj1YIpxMTQPajCR2saABeGrb2alYKqvmlgWTwvd__1YLeWDhDdDvxQLyoAl5RJz0-QrHlAeTnIuWp0DqhKF0FAj4hZ5RiteRBCFqD0XdMZS1PBxVWCg8Uc-qpIjq_MOaACktmKvDrMzuH4C0LJOtjLAZpfX1rgK5ILwDtWVV4w7iQhiJ7ddpYOQKinZPMz-LgQ5B36V3_ZMPAXZyMUp1sak1FY4umeZ6MR1WPPJAn_vEuH7KbI5Kf8dBLI7nNK9SC5511mnT5xVXQ8IWkCztxgypGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پل سه بلوطک، بلندترین و طولانی‌ترین پل  کابلی ایران
🔹
شاهکار مهندسی بر روی دریاچه سد کارون ۳ و رودخانه کارون؛ در مرز بین استان‌های خوزستان و چهارمحال و بختیاری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/688064" target="_blank">📅 00:46 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688063">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای سنتکام: از زمان ازسرگیری محاصره دریایی علیه ایران، مسیر ۹۴ کشتی تغییر یافته، ۳ فروند کشتی متوقف شده و ۲ مورد دیگر نیز مورد بازرسی قرار گرفته‌اند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/688063" target="_blank">📅 00:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688062">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/830d0d3599.mp4?token=TTxSK-hOwcMnnZp35L8Y9RR2jfpMS7BmEBbhLO7HLPMZ1pgCtHADCOlxeIa0MbWNm0mY9Tw2FcTqhK7YxHZAjqYTACS7USzYR3yhTSHEK768iNWUP6pe5YYFPghou96CeLd7Zyu3plZ6o5XREid27X76jApMIwVBNK6ebYsP6odRNMGkrqBqn9GufRVq5q64x574wdTCoYXUXyG9tcnaq_3X5aqbYtghZKMNjbp9N6Qy7Q5cbWEKHw-mrRrlln67rWAu8LIbBay0aYARsd7QVn_2BPbCYR4-XZkojUCFgC4xoCkX-QwbAmdgMdyrZNDeNTeudcsSJLfvlEN6EkSJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/830d0d3599.mp4?token=TTxSK-hOwcMnnZp35L8Y9RR2jfpMS7BmEBbhLO7HLPMZ1pgCtHADCOlxeIa0MbWNm0mY9Tw2FcTqhK7YxHZAjqYTACS7USzYR3yhTSHEK768iNWUP6pe5YYFPghou96CeLd7Zyu3plZ6o5XREid27X76jApMIwVBNK6ebYsP6odRNMGkrqBqn9GufRVq5q64x574wdTCoYXUXyG9tcnaq_3X5aqbYtghZKMNjbp9N6Qy7Q5cbWEKHw-mrRrlln67rWAu8LIbBay0aYARsd7QVn_2BPbCYR4-XZkojUCFgC4xoCkX-QwbAmdgMdyrZNDeNTeudcsSJLfvlEN6EkSJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه تغییر قیمت بنزین از ۵هزار تومان به ۱۰هزار تومان
@AkhbareFori</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/akhbarefori/688062" target="_blank">📅 00:15 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688061">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzzGi-mW8Nr7Pl_zD0Y7qKZGk_pHaLtCbDEfkgV62f_wQJs61hHl-Cv-3uwyLFXCkj3RC9WK0x9tqhj1fKc2wW0wrynRB9TrajWdcCulpgiBiwArLLWRWBOxaRnYGpJTg223_01La3p-QVCrsCaTb0aZEgZde1Www6nwEa7Uub-JGGKFy4ZTWJ7_8oq0Pm6FKPGF36Tkfo1oBr-ckt9QqRcEZjhPCwJwWwmMGRZ_K8bnOXrZOKFX7M3bObirl_un-grYcYUtZl_JanYvrbmDT4STSMDrQL_MCMknW8m9ZVHmL4bBpL_-DupIDIeDpUFDd8IZdrwdrKxlgyyrpNJHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ناتانیا مارشال، فعال مسیحی آمریکایی: چه زمانی رئیس‌جمهورهای ایالات متحده به اسرائیل نه خواهند گفت؟
🔹
پدرو سانتانا، یک فعال دیگر در جواب: آخرین رئیس‌جمهوری که به اسرائیل "نه" گفت، در سال ۱۹۶۳ ترور شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/akhbarefori/688061" target="_blank">📅 00:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688060">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
خبرفوری| هم‌اکنون نرخ سوم سوخت از ۵ هزار تومان به ۱۰ هزار تومان تغییر کرد
@AkhbareFori</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/688060" target="_blank">📅 00:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688059">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qyQNYV4c-GI_I5SbvZbZjJDthW7dB9oUofvqaSLGP65M84_ZdpYJ9BJvoAt_vFXVv45ecknxeaciiuWjBkpyg3Ey8TdHETw2iRTNaMArqiLplXzBd2RanLpVGj6KO9ONxAYfiNDg1qlK_QtHmSgkGlhpId5xuc33EEgVbNj5i_E46Fff35j0BOMxyD83mgJjbgbVICIrLAGa8eoEWaXEJHMSdTN6uMvziHeftX0jWBEKQWLfHogfdPOZAmHD2kTqw3zg3fCGm9RqDjNWAVsSc0SOqxI_C5AImzSGjyBqLlbx9HRBJXzxL-Lb8kGVxzcLyOc83yMfxQbt5gwCE7LDJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/688059" target="_blank">📅 00:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqFEuppuUGaO3W4L3cRcs3tw3HcdDayXrXYdggxdsk_4ESZfFifXvTi8H9XCA1XOL4QoWJHCdrC3gJm3cHtaQKsbOlPWRXGLpkTW6nLzg_vJlg3sDN7_SxUxL8j-obtF_oxro3B5Sn3pJCBxxRUXXA7shRB8_SOhnxgtFvZDz5TmfyO7FP6jyIvJg41T8qeBMOgnNlcAG0nGTnRGoR5t9lsKXH3XMWTKzFV4f_hAcQtK6jDqGv1ajMwzagthw2l_KinQv6muowmasZLNiWcMCQPjYuhSRGagJ0E___NBHTH7p4YihVR4mCtCcOHyP5ySJoYLEenBUVHFAr5xxmuXzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعال رسانه‌ای آمریکایی: وقتی کسی می‌گوید خدا به او گفته است که یک نفر را بکشد، ما او را روان‌پریش می‌نامیم
؛
وقتی یک ملت می‌گوید خدا به او گفته است که میلیون‌ها نفر را بکشد، ما آن را اسرائیل می‌نامیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/akhbarefori/688058" target="_blank">📅 23:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688057">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6706132e.mp4?token=OlbJBk5KTDKUVMKYdBOaNCAmHKGf6-mmMupH_z-r8BvVslgOwVcB_EtzHWUat3ruq10mQ4lTqoHEpVkQkXmvpYqQYFAeG2EjPiBQcNq4AWVngikvUR4YyRK_4ybiO__hC3NChk4qNBzAGNlwBuDjaIvokeeY1jiezWWgqijudD7S-Kv2FP-bS_06UuQndU-ec5WMenb8hmLqnnJqHZaTlYqAArmXMeuX51YOo-H9ccAQ9JKXXXadCrbQ33Yc-HuNOJLpy5iS4JjJ_PiqadQeX8mq7beBsI4fUDvBjdpzsZuZM_uqxTTyoIyU0kbA5XBdz_YS6Z3Vt3sy5isVsxzEcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6706132e.mp4?token=OlbJBk5KTDKUVMKYdBOaNCAmHKGf6-mmMupH_z-r8BvVslgOwVcB_EtzHWUat3ruq10mQ4lTqoHEpVkQkXmvpYqQYFAeG2EjPiBQcNq4AWVngikvUR4YyRK_4ybiO__hC3NChk4qNBzAGNlwBuDjaIvokeeY1jiezWWgqijudD7S-Kv2FP-bS_06UuQndU-ec5WMenb8hmLqnnJqHZaTlYqAArmXMeuX51YOo-H9ccAQ9JKXXXadCrbQ33Yc-HuNOJLpy5iS4JjJ_PiqadQeX8mq7beBsI4fUDvBjdpzsZuZM_uqxTTyoIyU0kbA5XBdz_YS6Z3Vt3sy5isVsxzEcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردار ابن‌الرضا، سرپرست وزارت دفاع: توان زدن ناوهای محاصره‌کننده آمریکایی را داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/akhbarefori/688057" target="_blank">📅 23:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688056">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
پزشکیان: از هر چیزی که حق است باید اطاعت کنیم، نه اینکه هر چیزی که منی که رئیس‌جمهور هستم اگر گفتم دیگران اطاعت کنند
🔹
گمراهی از جایی شروع می‌شود که فکر کنم منی که رئیس هستم هر چیزی که می‌گویم دیگران باید اطاعت کنند، انحراف از اینجا شروع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/akhbarefori/688056" target="_blank">📅 23:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688053">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BwdadbwpKbD_mpOR2hDl5Ibfukl9HZDYDVaFycdTF3WGOmlSMAl50T7v0EYjwbk3xxwXZDclmbnoVoBXq1iF7VjNLZ98zmDRd_r049EINqDG0hnCDFLHfbHqUFjVVOuVT263rGEtKm6nwanMzFNqDpjujZsAW6IIpiDD3-s2uO6d9D2uQkC-THTnD-eFI1dgiMWzYqsYVCCMkXKEmZsFGi-D4_uuD7Q7yEp8R1COouKhgMunwCCW7kfCUaLFcs3bxndwdLJWvrAiGIUoAMkYp0OgaaIeKb__Goz8cHsElCAtJfRxixrDAETDOzahkvTeTQ9r_VOE9_HfLyZC6HbvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h4k1PECpJME-thp6PpGWB6LLGCINaHd--gnMQUYNzt40qJs91Wa-oKMpCSr7HsANoIGmUWwZuOvrFPCFWAxwIqLlmOOpffykkQJIZhWodPU6mULNPIXSnmq-3qcC3ZCzG6nbE3PRgyZTt7SMXdMXi_VQ1jBeXRhhBE8XKl_35MO1wtb266RthiUKisXBvNwLDvcTy-QPDdOPWyC2TnAIxrJsalEM2QEy6aaTTbCtRj_u5xvQaMj6us9fJLJGBM4nZ8x4BNvBfM4vOl1GvAZXv8BJ5xwIAaHOJJKm2C0DNnHByr9St29gv9p6EhNPcV2gmBVcA9r5GRO-rv1eUveoMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jC3rlcrketwyZCgOI6GuEpA2WyWuw5R5u8cSwr7Hf-xls78hmOAb2Q5hFBNDHh9ikupYkVdYAWOSyq98isXCmZxcaD4XLXWKB5Ao9edkM_SrNsoytPNRviV-D9RpulOVKhUeSwHwZjzq8rjhhN971sVdmW0fc8hOceL552jk7fAm_1dqNMfBoPg_335tfR5a8FWMXBjC3TusdhPRbUC2MICmq2R8tJxcini07oM-vTAFzkLoOE2Xl3_Z1DNtDyU-vri5UKza-biX-Rh9LggSsdJQFrn-twkX-NgHj56O7WAigldInjLdHNEmZNyKaWZz0_9JUMuAoPnXHApyE2Hbsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
منظره غروب ماه از قله دماوند بر فراز تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/akhbarefori/688053" target="_blank">📅 23:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688052">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NiPk3WcKj3P5ZqXKt_9q__5VOLBqj_gQaFKjuFfc2vdEcP7JhFQq77AMsKwZOuonbtChkGIDGCPbx3dCKhSetdAj6iu-hsGQSkVP2sOAL-2gt-HWAyl8J4tekeHq1Ypwo4pX5gBr5RjCQacO9jRTmkvSqfjVIEHVQoWkV4o2eGIGwqbOtxjcUAPer84qJ31qd4qsIDBsSK4aHA9sWwcyVu7MA8U6k7b3ihB4QCwiYdxm-OUzOh9n89igbekc9DAlCkqjhu7aSw-4jEZd7eVPpdA7IVKmndtaKA55j7kLlChQTJ6_jiUHOxv9JJOmGp86qDWi_XvofpAiynBM8LFoJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقشه آنلاین یمن
🔹
مناطق قرمز: نیروهای انصارالله؛ هم پیمان با ایران
🔹
مناطق آبی: دولت فراری یمن؛ مزدور سعودی
🔹
مناطق زرد: شورای انتقالی جنوب؛ هم‌پیمان امارات
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/688052" target="_blank">📅 23:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688051">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
عادل فردوسی‌پور: خداداد عزیزی احساس می‌کند کسی باهاش کاری ندارد!
ادعای سخنگوی هیئت مدیره تراکتور درباره عزیزی:
🔹
آزاده‌ای که حاضر شده خودش را فدا کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/akhbarefori/688051" target="_blank">📅 23:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688050">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4bedf3511.mp4?token=RGSoooA_9XP1x9GFAhlf14KWeXgDhYpFKlL5ATV1khVs2LtIRRP2P4AIe9_ktc-H4_YlTO1SE9I_e_ZWhS71dGnSBN7vK6Z1xPnsZdotknUf0wZjXxwbKITmplFrssHe6oc6K3hQZPqOIiAi0cm5_CsoAUDapYFzNTHovUx8ZJeDxrSyehL_l4Q3T3g_TOj19MMIkhiFYBpfPtRvpeoWcfCd27lL5KZEcTKBHs7-hdM3Mz34bYNc1lXO5w_C0Fhxi8BCBrlSg7-xp6ApNhGptLbgzNr0MXR_Sgke-jZ21K1Uw6cZ5WHfJ1CHO_amRiq3JUlB7BnZRBSgGgcq6im-gEHE1yvTXp1ak2NGUE_QSDxnB54p8iZTwikxPdHBa2Pcu8IowC4m2FiFLSnGm_iIh1S8L1rz8B3bNOKm9QnTQfjlQCWrmYehBwfGcweqjoH4JGE2YQH5T7DSC2TXe5boeG4S27SS2fETddyvUR-K3JuTaOSsyGMhkZg0xFsTlLJhrdnyPpTXclGwbQuubjlX3bpZrjfv0j7raPmNAbYoTuxEQf8AySK_gJlnvSVkAlPuZ9nZRwWbFhV0bPPULbNjqHlyuadk5sPB1e058FEa7PGbwY4zxzKlH2NHKEFAU8A-6ctf0pkY-2LZcpLsBM4Vh6334tAkLK9UbrUirz9-6WM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4bedf3511.mp4?token=RGSoooA_9XP1x9GFAhlf14KWeXgDhYpFKlL5ATV1khVs2LtIRRP2P4AIe9_ktc-H4_YlTO1SE9I_e_ZWhS71dGnSBN7vK6Z1xPnsZdotknUf0wZjXxwbKITmplFrssHe6oc6K3hQZPqOIiAi0cm5_CsoAUDapYFzNTHovUx8ZJeDxrSyehL_l4Q3T3g_TOj19MMIkhiFYBpfPtRvpeoWcfCd27lL5KZEcTKBHs7-hdM3Mz34bYNc1lXO5w_C0Fhxi8BCBrlSg7-xp6ApNhGptLbgzNr0MXR_Sgke-jZ21K1Uw6cZ5WHfJ1CHO_amRiq3JUlB7BnZRBSgGgcq6im-gEHE1yvTXp1ak2NGUE_QSDxnB54p8iZTwikxPdHBa2Pcu8IowC4m2FiFLSnGm_iIh1S8L1rz8B3bNOKm9QnTQfjlQCWrmYehBwfGcweqjoH4JGE2YQH5T7DSC2TXe5boeG4S27SS2fETddyvUR-K3JuTaOSsyGMhkZg0xFsTlLJhrdnyPpTXclGwbQuubjlX3bpZrjfv0j7raPmNAbYoTuxEQf8AySK_gJlnvSVkAlPuZ9nZRwWbFhV0bPPULbNjqHlyuadk5sPB1e058FEa7PGbwY4zxzKlH2NHKEFAU8A-6ctf0pkY-2LZcpLsBM4Vh6334tAkLK9UbrUirz9-6WM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بنزین ۱۰ هزار تومانی به زبان ساده
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/688050" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688049">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
انصارالله با پخش این ویدیو اعلام کرد چندین کامیون حامل تسلیحات عربستانی که در راه ائتلاف در یمن یودند را در مرز ودیعه شناسایی و هدف قرار داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/akhbarefori/688049" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688048">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHUyYquEKGBQb7-ghAqR_01iB2dFnfSnZnrXrhqmjTzE5ZX0iAvL8byQpZGfGDVRaveVk9XxJ85ylwPLWPha86UO4dJlzDg_RBIY5VsXMNCmDuCKNNnoQONbdjxvTqodCbGW_bMesHJhaCQnF8xEcj0b2sEHfFCdv1r2x-4b6eUdavOPJDRTSwV1nEisodwGWtloc-q-ytMx5h1HohjzTfCK4RTdPdFPSpa1p7FRVsSteFMLuUFBn0dqvsYp1wl7Vsl4In4C1QU9LirHFlaEnx9o7DwtXsT3UCX96PJB1ukQPYDp5HdzppWRw2DgekdakoSWj45hEKzBFaW3Z0R45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر تا پیاز سوخت‌گیری با کارت‌های اضطراری جایگاه/ از محدودیت هر بار استفاده تا اعداد جدید روی نمایشگر پمپ‌های بنزین
در خبرفوری بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3243535</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/akhbarefori/688048" target="_blank">📅 23:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688047">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
قبایل جوف وابسته به انصارالله یمن با یک بسیج همگانی به میدان آمده‌اند تا مزدوران تحت حمایت عربستان سعودی را عقب برانند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/akhbarefori/688047" target="_blank">📅 23:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688046">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
زلنسکی: آمریکا به‌ دنبال کاهش تنش روسیه و اوکراین در زمستان است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/akhbarefori/688046" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
اعزام نیروهای باتجربه تروریستی از جنگ سوریه به یمن برای جنگ با انصارالله
🔹
درگیری‌ها در جبهه‌های منتهی به صنعا تشدید شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/akhbarefori/688045" target="_blank">📅 23:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hR9JvRnO0ThKdgBxOODVCrKiO9Nj87Wvscsfor8lujXLZNDiZCvf6CUzNOKplZy0rPkaVPrvDxr4ZNMJce7N8z8KPd5OhZPpAlQuhhbWmtqES2V2EX4yMbWGsJMfJxh6j9Txa36BnPjpz0f-gvHGSqAIOpfuVCw5g6SMtaT850dGIFaNKkAS6JKZlkLQyiKRkltLIvdcSg5BmvBE1Zqqzv6Io-Gy2b-grheeVpdm3i1q4Sq7WgQQ2VCa-PnyJJosQ3_n28W4-PMisH9sEe2DfxeeOgfPYryhFGxEL4bAfg6MCYXD1GYIFlvJFi6nDsds8px_5aSoEAjENP-A2XKSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بر اساس گزارش گلدمن اگر حملات به کشتیرانی در خاورمیانه افزایش یابد، نفت ممکن است تا سقف ۱۲۰ دلار در هر بشکه صعود کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/688044" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688042">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
قیمت گاز طبیعی اروپا امروز به ۹۰۰ دلار به ازای هر هزار مترمکعب رسید
🔹
قیمت گاز در این قاره قبل از آغاز جنگ ایران ، ۴۰۰ دلار به ازای هر هزار مترمکعب بوده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/688042" target="_blank">📅 23:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688040">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔹
خبرهای داغ امروز را از دست ندهید
🔹
🔹
نقشه شوم آمریکا برای جنگ با ایران: واشنگتن برای حمله منتظر انتخابات نمی‌ماند
👇
khabarfoori.com/fa/tiny/news-3243473
🔹
در کشوری که با کمبود مرد مواجه است؛ زنان «شوهر ساعتی» اجاره می‌کنند!
👇
khabarfoori.com/fa/tiny/news-3243120
🔹
اگر سهمیه کارت شخصی و کارت جایگاه تمام شود مردم چکار کنند؟
👇
khabarfoori.com/fa/tiny/news-3243324
🔹
هر گرم طلا تا پایان سال چند خواهد شد؟
👇
khabarfoori.com/fa/tiny/news-3243404
🔹
پشت پرده حمله به انبارهای سلاح تروریست ها در عراق | حمله پیشدستانه برای خنثی کردن توطئه نتانیاهو و ترامپ؟
👇
khabarfoori.com/fa/tiny/news-3243484
🔹
صفحه ویژه اخبار پربازدید وبسایت خبرفوری را اینجا کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/akhbarefori/688040" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688039">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
ایران: آمریکا و رژیم صهیونیستی اساسنامه آژانس اتمی و قواعد ایمنی هسته‌ای را بمباران کردند
🔹
جمهوری اسلامی ایران در نشست شورای حکام آژانس بین‌المللی انرژی اتمی با محکوم کردن تجاوز آمریکا و رژیم صهیونیستی به تأسیسات هسته‌ای صلح‌آمیز و تحت پادمان کشورمان تأکید کرد که متجاوزان با این حملات، منشور ملل متحد، اساسنامه آژانس و قواعد بنیادین ایمنی هسته‌ای را بمباران کردند./ ایرنا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/688039" target="_blank">📅 22:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688038">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ntl_WrUqIig2B_JtwKPlY-x2W7Xd5jgPQzILGkGNYYMkCqoloF-L-35fjZTm45i82SSo-cQKvTDy8_rwc-as6X9Kgybmu0z0O2YqmCe93Ovyh9006gH0fLPD-Z8xJJo_kBs9-odaxbK6OOwBN77dH3qVh6gGFB_prgkiTwH4cwVtnAc_n_zjKrEudFB9nLUKXL4ADELxQVRD0YOQxkD9BduMHLkhBSmMcpCTXGN8yB77C5a-KfH5s5nSAeuexO_a0f9agFeZKyYD5mAQo5u9xUDPUbLREJmRvqM87qD0femYjtnb1Eku1RlghqdhXX3b0dQxRt4uZVMcuGjevpfoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تولید هر خودرو در ایران‌خودرو حداقل سه‌هزار دلار و در سایپا دست‌کم ۲۵۰۰ دلار ارزبری دارد
🔹
یعنی برای تولید هر خودروی داخلی، به علت وابستگی به واردات قطعات، حداقل ۵۰۰ میلیون تومان منابع ارزی مصرف می‌شود.
🔹
جزئیات آماری نشان می‌دهد تارا اتوماتیک ۴۵۰۰ دلار، شاهین پلاس ۵ هزار دلار و ری‌را ۶ هزار دلار ارز مصرف می کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/akhbarefori/688038" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688037">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e682bbd6b.mp4?token=nVs8q592KBSAgtOLKcibHUfKqdft4ZGu1kkgUkpc2zrWeutRlJ07EwhUPuoh0DupSteNtYxo4RFbUJnzjctqh2hgzkPHwtQ-IjFhLeB2gehRybn2Snv9QEbCLuv36MPdUd4Fijuv6iwBkxGLuEm6QD9sQdVx4l9oQqt8ZwOjL4GZfQ7I82L5zmwC5Dt8NAUAB03usW12UZ1t8ha7cOwXHyf_C5e_MWfdONHkasQ3s4IbhiFB0kLnrzstcof0KXcaz8OD1QFtmL0Ks3vUxHGV4_Nt-AhS1F-gP0Egu9vRVIAi4M4izd5HhWr2kgtZaeTaxt_byGPm8jmfRd6mPE_HVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e682bbd6b.mp4?token=nVs8q592KBSAgtOLKcibHUfKqdft4ZGu1kkgUkpc2zrWeutRlJ07EwhUPuoh0DupSteNtYxo4RFbUJnzjctqh2hgzkPHwtQ-IjFhLeB2gehRybn2Snv9QEbCLuv36MPdUd4Fijuv6iwBkxGLuEm6QD9sQdVx4l9oQqt8ZwOjL4GZfQ7I82L5zmwC5Dt8NAUAB03usW12UZ1t8ha7cOwXHyf_C5e_MWfdONHkasQ3s4IbhiFB0kLnrzstcof0KXcaz8OD1QFtmL0Ks3vUxHGV4_Nt-AhS1F-gP0Egu9vRVIAi4M4izd5HhWr2kgtZaeTaxt_byGPm8jmfRd6mPE_HVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نجات معجزه‌آسای کودک در تایلند؛ راننده تحویل در آخرین لحظه او را از زیر کامیون بیرون کشید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/akhbarefori/688037" target="_blank">📅 22:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688036">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d607a02a97.mp4?token=hYiMuZ_Nft7DN4wid6uVdH2fr_f4lXNR1GY1_qr5tDM_YCSwf2PJFI0qclPYY93a7jJTwn1GfRBKtSRzIAi4y4jDjIlzAetbZLLfYM4tvLvd68EDeNAL80B-O0m2HV65fJoXmNiNoOLYSNm7BtkZZioX512HwQ-Yt2isZq973lILVoIjl9GURFgx697kmusvMTV3D1fs8jyASRU8g0QLBs71_nPQbhZJnkffwnHJ1JbvMj-TQwXK7wVqKgrtdtCHwA6FtjT4WN2MWeSHXH8-Jn4NOzexKXR1clSRP6K-wnN3EaUizeUJPKVsrP1uqiura_7TL5L3jZQzRuvQ1XTQLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d607a02a97.mp4?token=hYiMuZ_Nft7DN4wid6uVdH2fr_f4lXNR1GY1_qr5tDM_YCSwf2PJFI0qclPYY93a7jJTwn1GfRBKtSRzIAi4y4jDjIlzAetbZLLfYM4tvLvd68EDeNAL80B-O0m2HV65fJoXmNiNoOLYSNm7BtkZZioX512HwQ-Yt2isZq973lILVoIjl9GURFgx697kmusvMTV3D1fs8jyASRU8g0QLBs71_nPQbhZJnkffwnHJ1JbvMj-TQwXK7wVqKgrtdtCHwA6FtjT4WN2MWeSHXH8-Jn4NOzexKXR1clSRP6K-wnN3EaUizeUJPKVsrP1uqiura_7TL5L3jZQzRuvQ1XTQLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وقتی پسر‌بچه مهمان برنامه محفل ستاره ها به آرزوش رسید!
🔹
اقدام جالب فرمانده سپاه گلستان بعد از دیدن آرزوی جالب پسربچه گلستانی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/688036" target="_blank">📅 22:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688035">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf3ca54a33.mp4?token=OAnhspwoGzdG5BI9eNuL-Be7kHr0nbHpS4sjQ39TcJmEC1qtfAQt99I9D6lwlwpSUJfUWnrgOGpKpy6v6cqVrrQvwhQztz8zwnyZcGKx0uzQQGzTUndNgXCG2lhLSi64n6R1iLcCKGsPVzFFEh1-_hv3TkyTjrVPutth-2ezt3D-05Jb-ydYQcLI0BlP3OecWVkwaPr6oLqhwG8YtI2r6QPkocvT8LnxoJHbiKYBX4E0Bi4Z6V6c298FsSWbpCXmftBvwevf3zZw2olDJ7FEJIjtyL_fztcbXZyfhaZyhrezkvX1an4Zk3du3ZJBCkd8zv4Ulqxoc8EaTgS0yZ9uTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf3ca54a33.mp4?token=OAnhspwoGzdG5BI9eNuL-Be7kHr0nbHpS4sjQ39TcJmEC1qtfAQt99I9D6lwlwpSUJfUWnrgOGpKpy6v6cqVrrQvwhQztz8zwnyZcGKx0uzQQGzTUndNgXCG2lhLSi64n6R1iLcCKGsPVzFFEh1-_hv3TkyTjrVPutth-2ezt3D-05Jb-ydYQcLI0BlP3OecWVkwaPr6oLqhwG8YtI2r6QPkocvT8LnxoJHbiKYBX4E0Bi4Z6V6c298FsSWbpCXmftBvwevf3zZw2olDJ7FEJIjtyL_fztcbXZyfhaZyhrezkvX1an4Zk3du3ZJBCkd8zv4Ulqxoc8EaTgS0yZ9uTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی زیبا و دیدنی از یزد
😍
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/akhbarefori/688035" target="_blank">📅 22:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688034">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
عامل ضدانقلاب در ایست و بازرسی هنگ مرزی ارومیه دستگیر شد
فرمانده هنگ مرزی ارومیه:
🔹
در بررسی‌های انجام‌ شده، هویت و سوابق فرد مورد نظر بررسی و مشخص شد وی دارای ارتباط با عناصر ضدانقلاب و سلطنت‌طلب است و تبلیغ جنایات آمریکا را در فضای مجازی انجام می‌دهد که بلافاصله توسط مرزبانان دستگیر شد.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/688034" target="_blank">📅 22:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8NLu1E_GHglL-8nVS9U8cdsc1xI-fgMi1fwmBtMYuNQFnNSG14oc4ubqBEaWZmGkxjv2W6el8VoK76_JkzDrbMMane44xoFeQtzaGaWYoYNrZBL_H4Hm0cwq-aqajQWZmN6eJ4dfJdWBbciawE2gjbHRPjX9FZNyWxczGfR0EkYfSpW1TEYzgjzJ1Axu28hS9X61slCaeSj7cmFy7-5tv8KPqmxQR-JUz05e7CK_uYLR73f6jiaA-iigWY9XyrAlbnGJXnPIB23GVjS4tAiPImuUYsSnkWLa7O1enrH4kSqqGPR9YaklknTmCxjalWO9xLwmmJsrKZA5A8mfHYNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هر روز چه دعایی بخوانیم؟
🔹
شنبه،
#دعای_عهد
🔹
یکشنبه،
#حدیث_کسا
🔹
دوشنبه،
#زیارت_عاشورا
🔹
سه‌شنبه،
#دعای_توسل
🔹
چهارشنبه،
#زیارت_نامه_ائمه_اطهار
🔹
پنجشنبه،
#دعای_کمیل
🔹
جمعه،
#دعای_ندبه
🔹
دعای باران،
#رحمت_الهی
🔹
برای پیروزی جبهه مقاومت
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/akhbarefori/688033" target="_blank">📅 22:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DV1T9G_6S9k1FLU6tKdjsYz5TP2tRYhMs7s2BlXXkDZ3EEnYgHX9-aSwKfmieSq8arXg-fA-_-CV3nzsn7gojteJijiftD-MQufAjqDOnLI083jb-bCfcNJiiTq9gOVXgqrhc_1upePYNPnrMdw6uqtoul3U3D3s1civqFVioptk6jy1mSwU7i59tWWgui6KqI8OA2n9Cr6qqwzJyMZb0nFiMAF6_0zYcmyYIBNOIPijeCjhrGJHJMyFw55SS4FxxlgQh7isHqEGBmD5_dtJLlj6UiChdxs-iCWolt1Txd-IV-XapcrW7TywB36O8PaVv1rJS4xlmKeZkgXrwLdLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا بخریم؟ دلار بخریم؟ یا اصلاً هیچ‌کدوم؟
🤔
🔹
وقتی دلار به ۲۶۰ هزار تومان برسه، از قیمت فعلی فقط حدود ۱۵٪ فاصله داره.
🔹
از طرفی درآمد ثابت تا پایان سال حدود ۱۸٪ سود می‌ده.
پس سؤال اینه:
🔹
فرصت اصلی سرمایه‌گذاری الان کجاست؟
🔹
چهارشنبه ساعت ۲۱، توی یک لایو رایگان جواب این سؤال رو بررسی می‌کنیم؛ با عدد و منطق، نه حدس و هیجان.
👇
برای شرکت رایگان، همین الان ثبت‌نام کن:
[لینک ثبت‌نام]
[لینک ثبت‌نام]
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/akhbarefori/688032" target="_blank">📅 22:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688029">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_F6kRVjZUHJIshzz-3X_GNVQ4o3iV4tBlm47no2V_DJQ7hgjde4OEpGeHiGdeGnV-gdWnQPyioJ10QLoxGpsYl2K-iNZPgp0SaBpiQTzlHtL8qa3Ejx_uwhMz_-0B0iQihPJjMEWj81-Tx-QVcBRXpSJaze9QkBc4DTtEwgX3vZocCs-6BlC-jVYEzJeMSv9j17qAVYN5MqWl24uQZJH9tqlPaHMmynkRSdvBeZu-i-hbQztHQV6cCYBV9O7wI2i0YHOCHM7FadkMe12BT21hf_Q8x_uIq1DzYiFcoxrVWCDfRuwe6M71vLmZBl24qUM7OJfROa7K7S_3L9elxE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جدول لیگ برتر پس از پایان هفته ششم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/688029" target="_blank">📅 22:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688028">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
تصمیم جدید دولت برای تأمین سوخت کاربران راننده تاکسی‌های اینترنتی
🔹
در جلسه انرژی که عصر امروز، دوشنبه ۱۶ شهریور، به ریاست دکتر پزشکیان، رئیس‌جمهوری، برگزار شد، با درخواست و پیگیری شرکت‌های تاکسی اینترنتی برای تأمین سوخت مورد نیاز کاربران راننده موافقت شد.
🔹
این جلسه با توجه به ضرورت تأمین سوخت کاربران راننده و در پی درخواست شرکت‌های تاکسی اینترنتی برای رسیدگی فوری به این موضوع برگزار شد. سهمیه مازاد سوخت کاربران راننده تاکسی‌های اینترنتی متناسب با میزان پیمایش آن‌ها، تا سقف ۳۰۰ لیتر در ماه، روی کارت سوخت‌شان منظور خواهد شد تا بتوانند سوخت مورد نیازشان را تأمین کنند. این تصمیم در حالی اتخاذ شده است که از بامداد ۱۷ شهریور، نرخ سوم بنزین در جایگاه‌های سوخت به لیتری ۱۰ هزار تومان رسیده است.
🔹
محمد خلج، مدیرعامل اسنپ، ضمن قدردانی از رسیدگی فوری به این موضوع و تصمیم اتخاذشده در جلسه انرژی گفت: «رسیدگی سریع به موضوع تأمین سوخت کاربران راننده تاکسی‌های اینترنتی و تصمیم اتخاذشده در این زمینه می‌تواند به رفع یکی از دغدغه‌های مهم رانندگان کمک کند.
🔹
دسترسی به سوخت مورد نیاز بخش مهمی از امکان ادامه فعالیت اقتصادی رانندگان است و امیدواریم اجرای این تصمیم نیز با همین سرعت و دقت دنبال شود تا اثر آن در عمل برای کاربران راننده قابل لمس باشد.»
🔹
مصطفی سیدحسینی، مدیرعامل تپسی، نیز ضمن قدردانی از تصمیم دولت و شخص رئیس جمهور برای تأمین سوخت کاربران راننده تاکسی‌های اینترنتی گفت: «هزینه سوخت یکی از مؤلفه‌های مستقیم در هزینه فعالیت کاربران راننده است و هر تغییری در آن می‌تواند بر اقتصاد سفر در تاکسی‌های اینترنتی اثر بگذارد. امیدواریم اجرای دقیق و به‌موقع این تصمیم به حفظ پایداری فعالیت رانندگان و جلوگیری از انتقال بخشی از افزایش هزینه‌ها به سفرهای روزمره مردم کمک کند.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/688028" target="_blank">📅 22:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5dffacb8b9.mp4?token=CDiN0_CKoUMFwzW8s1QLY9jpJM1glyrp5zikqRlK8NTOPq38va1Mc6JZ0UBkOUsL9C85a6M82VYBY86DBb85QVjvJVjfHiRCOWUm72wGFLj4vyheb9piIOwTB50WaNu9okW5v8zW5UIrXsuBa1_XVmcmD5eIn2IpTYJry1dH93b1EXLMf1rNeNUjg33oT2kmxKMPezfmU0TrY-LAghiMaxlTWQ4r76Dxuvn0G3bisQaIuZjCovmZI8g0PsWna-R57BObUW1X-X76SwiS3IEu7C1TcyffVD1hUmuRLxxegBfPkLqn0CCt8QpX5b1tTch57nHeTqEZ2CQyAgEFtzo1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5dffacb8b9.mp4?token=CDiN0_CKoUMFwzW8s1QLY9jpJM1glyrp5zikqRlK8NTOPq38va1Mc6JZ0UBkOUsL9C85a6M82VYBY86DBb85QVjvJVjfHiRCOWUm72wGFLj4vyheb9piIOwTB50WaNu9okW5v8zW5UIrXsuBa1_XVmcmD5eIn2IpTYJry1dH93b1EXLMf1rNeNUjg33oT2kmxKMPezfmU0TrY-LAghiMaxlTWQ4r76Dxuvn0G3bisQaIuZjCovmZI8g0PsWna-R57BObUW1X-X76SwiS3IEu7C1TcyffVD1hUmuRLxxegBfPkLqn0CCt8QpX5b1tTch57nHeTqEZ2CQyAgEFtzo1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه احیای قلبی ریوی می‌تواند جان کسی را نجات دهد؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/akhbarefori/688027" target="_blank">📅 22:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688026">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEfisBzA5gQnryg7Ievz-PIrm1iqKGT3sCgYvz-aYrFsfQrBr46wAsNxL6FwWEWOePjMSEQRdOxiYirxr71lrn-Rcvv9-5WkjFL61r6QpqjbwN0NPtAHOiFY1mE5YCIJiIEe4TZ1JaoMkBo38D9UHy5je_9peukIoZxOyx3WFidIXoqgmTCuA-vFLJqhFgzBwTJBD3yYouxuIeuogQ1lvjkSXYZg-Vx73WdcDbKNROEuTewhWy8g18bnwFkrxMxxgVQMnJAqyu5nS7Fg3m6xIAkNKV0z0ptWmVXNpHnrwKLL_nZfNnHcd9D4AEFwWNkYnlHaXi0IpiLXI7GDR7pfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گزارشی از افتتاح خط تولید جدید کارخانه فعال صنعت باتری کشور در مشهد؛
🔹
نیروگستران؛ در مسیر جهش تولید
🔹
همزمان با هفته دولت،خط تولید جدید شرکت صنایع تولیدی نیروگستران خراسان با حضور معاون امور معادن و صنایع معدنی وزارت صنعت، معدن وتجارت، معاون هماهنگی امور اقتصادی استانداری خراسان رضوی و مدیرکل صنعت، معدن وتجارت استان به بهره‌برداری رسید؛ مجموعه‌ای که طی سال‌های اخیر با توسعه خطوط تولید و سرمایه‌گذاری در فناوری وتجهیزات، به یکی از واحدهای توانمند صنعت باتری کشور تبدیل شده است
ادامه مطلب در :
https://sarasari.khorasanonlin.ir/Newspaper/item/155777
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/akhbarefori/688026" target="_blank">📅 22:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213601a2f2.mp4?token=uqkXlfoR8gTKfYkcYuOZ3da2mMrE9wmIoK47B4Oi20dNDsnpKMSeNC_x0Mw1wxNY8wWoiaH53kadc3kniJDYCBN2LNtyo0VU-14rB7ZQSDKKEcBcAr8IQ-DirdlabMa5_IP8lqR8vKtnI79cCiUQvB0G5Zpfc76ijkjxeGptsA-_o9VoMWrw54TBPJK1EptUHMs7SuasWrSOjlQFQIh0wfmbjemIn1-NqT6fFHIN4W_kc_4d5duGyGkIOtIq7tCcBjajTAdPZ4vtYUriNXr8hTFKDJTyNQeXPrfW08lFn7NVPSgIp4PLfDO64ADeIGV02TI5-Tw5D54cl97QsO-tgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213601a2f2.mp4?token=uqkXlfoR8gTKfYkcYuOZ3da2mMrE9wmIoK47B4Oi20dNDsnpKMSeNC_x0Mw1wxNY8wWoiaH53kadc3kniJDYCBN2LNtyo0VU-14rB7ZQSDKKEcBcAr8IQ-DirdlabMa5_IP8lqR8vKtnI79cCiUQvB0G5Zpfc76ijkjxeGptsA-_o9VoMWrw54TBPJK1EptUHMs7SuasWrSOjlQFQIh0wfmbjemIn1-NqT6fFHIN4W_kc_4d5duGyGkIOtIq7tCcBjajTAdPZ4vtYUriNXr8hTFKDJTyNQeXPrfW08lFn7NVPSgIp4PLfDO64ADeIGV02TI5-Tw5D54cl97QsO-tgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شوره سر یعنی چی؟ دلیل شوره کثیفی نیست!
‌
🔹
در این ویدیو دلیل اصلی گفته شده
‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/akhbarefori/688025" target="_blank">📅 22:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFt5RNrtAGNbfLByvoDEN2_o5aKl_rc5zXtwiaEiYsikjPoRDIx9FdqTgrhth0tfcaIamPh2nNii6dYALizEASqW_sVF75E1gdt4A0BKoPsGyavuQth5UnHqw_glrER-A5juq94dBfLemER5tghcCvxTFo-p4t_z7mP71YRAF2NcCYR97z9TcWfY5Iw_l4HIf4sqyAiTabZvwXD3geTzWswJZ1S_dRF_S_OZR6ibOhCtZyQOkeGC64Gt_QXZXucCxwJqMavvx4sKmxTYhNIbYVvQHyQqQ3DeZalzBRaUd0FZfp-6JgmUOe3UlUnzkeJk4G8d6RMes87f0HCEoB_ThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده حمله به انبارهای سلاح تروریست‌ها در عراق/ حمله پیش‌دستانه برای خنثی کردن توطئه نتانیاهو و ترامپ؟
🔹
برخی معتقدند حمله دیشب مرتبط با خطراتی است که از غرب، کشور را تهدید می‌کند. این تهدیدات به خصوص از جانب آمریکایی‌ها زیاد شده است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3243484</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/688024" target="_blank">📅 21:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688023">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5a9e35199.mp4?token=gQ5MJC6bGkc7RCgnfGVPbOrUEX1kch_sLl-3Vod1prfHlruS1u7JPGeQFjONYsGXjh1pwklTy057TwGpsaR6kEPqO6iMGJt9jvLEmYze0hey8e4Mb26aqUnb_Lbl__nqFTS8Kt4A-nTljLXx8ekaUec-vGnOrinxotfLvnrka6VuCYfXTetWNPFbJci7OPLVmIzIFxJxiqEVzDPogRScjdxM-4JmgQJz4rCVjoR34e49kgzj2sdsJ0Z5LDna57MIVZHSbF84iFd-PcTqTrl6pL3pMoPb9l0U1PRRvtymRcu3kyWD2sC6qWd0qafLyAF-0klldXenahl3bCjtVXA9SRq_S8dgjyRQj13-oOOQRPhOJOI8z7C28c_3j6hYGxh5S3FljzD8yaKLxIbhUzzcm1d1_oV7fniBd5XcS-QzG_4mhIiKhCNUDv9A4-LxR-utZ3L7lzfMnp1CsGlKtcyaEge6LBYE57-PTKAyhpGznk8v86vUbxhQSX1lTSl1vV9b1oup4V-7bo3HJ0HcmU-bUvHFDJduuyQYnNmxp0HAVgshl0NSLuEEl9HJ6dYSawZjpf-kFw4JNSHTA-9QyT0xVtv-kBzgTOj8NIW_AUq1FP3Flflva90dIe0HZpCuNpfeW9J5agx8mpoXfxSs0EMqtbr9vxu0JMGKtogre35YvgI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5a9e35199.mp4?token=gQ5MJC6bGkc7RCgnfGVPbOrUEX1kch_sLl-3Vod1prfHlruS1u7JPGeQFjONYsGXjh1pwklTy057TwGpsaR6kEPqO6iMGJt9jvLEmYze0hey8e4Mb26aqUnb_Lbl__nqFTS8Kt4A-nTljLXx8ekaUec-vGnOrinxotfLvnrka6VuCYfXTetWNPFbJci7OPLVmIzIFxJxiqEVzDPogRScjdxM-4JmgQJz4rCVjoR34e49kgzj2sdsJ0Z5LDna57MIVZHSbF84iFd-PcTqTrl6pL3pMoPb9l0U1PRRvtymRcu3kyWD2sC6qWd0qafLyAF-0klldXenahl3bCjtVXA9SRq_S8dgjyRQj13-oOOQRPhOJOI8z7C28c_3j6hYGxh5S3FljzD8yaKLxIbhUzzcm1d1_oV7fniBd5XcS-QzG_4mhIiKhCNUDv9A4-LxR-utZ3L7lzfMnp1CsGlKtcyaEge6LBYE57-PTKAyhpGznk8v86vUbxhQSX1lTSl1vV9b1oup4V-7bo3HJ0HcmU-bUvHFDJduuyQYnNmxp0HAVgshl0NSLuEEl9HJ6dYSawZjpf-kFw4JNSHTA-9QyT0xVtv-kBzgTOj8NIW_AUq1FP3Flflva90dIe0HZpCuNpfeW9J5agx8mpoXfxSs0EMqtbr9vxu0JMGKtogre35YvgI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا در آستانه پاییز با کمبود بنزین مواجه خواهیم شد؟
/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/akhbarefori/688023" target="_blank">📅 21:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار اصفهان(Admin)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247a073d5e.mp4?token=FiBejjAGSASJUwbKnSq87jVKniQ-JL--n5-FBh6CjtYbJcCeK1R3fxGxFpgiRBDclcC69x9aa0QlZLqAa6P4aHbx8VZzn36PhvCqeh-eBLMrrhcExkRTvb4Xwo3x1Tb6E1fnawaRlSFsxg0GxZb_6xLu-Yhar7q0qzuhB9zq_Fg_xe5DC3ONWqBG2O_z5u_70EPU8u6BI0KmkdzJ1FfhvTGBcpLHZiOs83z4EgBaMZ5N_qlslh83cf2oBNWKvBNWuuNiTFc_WC1W_55hLHCu608mAPZ9T1Wo3fJEqajuUzraqbjtxk37B1lwAO_40JqImtijqk3UQMkVcREytCH3bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247a073d5e.mp4?token=FiBejjAGSASJUwbKnSq87jVKniQ-JL--n5-FBh6CjtYbJcCeK1R3fxGxFpgiRBDclcC69x9aa0QlZLqAa6P4aHbx8VZzn36PhvCqeh-eBLMrrhcExkRTvb4Xwo3x1Tb6E1fnawaRlSFsxg0GxZb_6xLu-Yhar7q0qzuhB9zq_Fg_xe5DC3ONWqBG2O_z5u_70EPU8u6BI0KmkdzJ1FfhvTGBcpLHZiOs83z4EgBaMZ5N_qlslh83cf2oBNWKvBNWuuNiTFc_WC1W_55hLHCu608mAPZ9T1Wo3fJEqajuUzraqbjtxk37B1lwAO_40JqImtijqk3UQMkVcREytCH3bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چهارمین فرونشست در ده روز گذشته در خیابان رباط اصفهان
#فرونشست_اصفهان
@akhbareisfahan</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/akhbarefori/688022" target="_blank">📅 21:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688021">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=QkFPPn2quC22lNEjOREnaNRUHTQe1aczDyEosIVLnGmV6rPVO2EJ1aJGr-u6co9Y89N0DxGz4RjPQiYRG-AHKUh9liUsHnhXiOJxNmFnD5E1dxpsodLewVmKOwcWY3W6mLFUjSs6A_o7yQvY6P_xhIjfq31TtoQVTJjwvVN2ei5KaEQ1cjT1pfYY_hzFrJaUSh-gA8HqrZkRkNQfMoexqXVBUl5-tDU0CeD4fOP555-2xVTfzgi4GORhZno0WlSs27XHyqZBeFOviwqimzu4uUmqW5O4RzQNenxcOAsx0o5xf7H3XbJvU80Anc8VWeWJ3wT5Yvqz7uvvQJd9PW7Rhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1a55c75f.mp4?token=QkFPPn2quC22lNEjOREnaNRUHTQe1aczDyEosIVLnGmV6rPVO2EJ1aJGr-u6co9Y89N0DxGz4RjPQiYRG-AHKUh9liUsHnhXiOJxNmFnD5E1dxpsodLewVmKOwcWY3W6mLFUjSs6A_o7yQvY6P_xhIjfq31TtoQVTJjwvVN2ei5KaEQ1cjT1pfYY_hzFrJaUSh-gA8HqrZkRkNQfMoexqXVBUl5-tDU0CeD4fOP555-2xVTfzgi4GORhZno0WlSs27XHyqZBeFOviwqimzu4uUmqW5O4RzQNenxcOAsx0o5xf7H3XbJvU80Anc8VWeWJ3wT5Yvqz7uvvQJd9PW7Rhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حجت‌الاسلام خلج در برنامۀ سمت خدا: تفکر فرعونی، قدرت و تجهیزات را عامل پیروزی می‌داند
🔹
همان تفکری که امروز در آمریکا و رژیم صهیونیستی دیده می‌شود.
🔹
قرآن پیروزی را از آنِ اهل ایمان و تقوا می‌داند، نه صاحبان قدرت و ثروت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/akhbarefori/688021" target="_blank">📅 21:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-688020">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
وام مسکن تهران یک میلیارد تومان شد
🔹
با اعلام مدیرعامل بانک مسکن، مبلغ وام مسکن به‌ازای هر نفر افزایش پیدا کرد.
🔹
تهران:  یک میلیارد تومان به‌ازای هر نفر
🔹
شهرهای بالای ۲۰۰ هزار نفر: ۸۰۰ میلیون تومان
🔹
سایر شهرها: ۶۰۰ میلیون تومان
🔹
یعنی زوجین در تهران مجموعا ۲ میلیارد تومان برای خرید مسکن دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/akhbarefori/688020" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
