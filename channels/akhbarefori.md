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
<img src="https://cdn4.telesco.pe/file/P188c6ks6rkT5Ja_bHCdfIzk3UpLqLIGVsUlnHYVGSqbJpdaqLK2ViVZhAgHNWnNP7lc02s5ZJUU03ZhWAtqbVfdHMxsOL5rbkgW5qfeMq8LRdjowyQujaLKv7yYqJjVD53W5usaGfRVY_Qt4b9YzBrL7czuarcJzqGWLRFTezGQbmy5LDFDiuVGrmFYkxmZJcJqycj93_8Af2NLJFeyfYOfR9cUwk6beWXI9qNiD-UwlTP_jLuwltRBa2tuc3RW9tyzBtoM6QJzNMnQSafdjW44Veh1PNSZtMx1o_v742gd54m-OGWSwonjsZVRRQO0pEQ3ti_GU1SMbHCVZj19BQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.23M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 01:05:00</div>
<hr>

<div class="tg-post" id="msg-656724">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from-Salar-via@chToolsBot</strong></div>
<div class="tg-text">تست هوش زبانی امشب
🎯
🚀
معنی اصطلاح Hail Mary به نظرتون چی میشه؟
🧑‍🚀
روی جواب درست کلیک کنید
👇
👇</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/akhbarefori/656724" target="_blank">📅 00:19 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwnsQJFcMeEBE5LAm-_FsqKRSzXR7wz8ipZ5x-31ag9Jv9J5SZVxXEqxaipJanL6cDsAMCJwD0vc4W81wkZn1C6_WlkPC9yGfS3FugtW2JkYkxetT93HxXZ7K346Ecczt1FX7UAOdgYnajcdbvO1uF0HjdDUtuQnYMfvKkT95SxEu9HWQ9HhW-_VKniqUlqa2wO45g7-ScdwRyxUVjKllueiVtfxMEXEdFEQGnuRee0BG4Gj0Db1XiyuRgOltejEVePmo7UR6VkWRl3vba987ouQmo7bvsfAPMaJZIvLNBZGc1hy5iTbKyxzvaMaMYKlo1qNJ2VC82kcNla37YXMEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.3K · <a href="https://t.me/akhbarefori/656722" target="_blank">📅 00:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1Fj-ZujftFSzudirOcazjtAfkEF-eUy6lupRnHhqqKFyG4rWKng6inZeYblrvBO13vTEsV18z8MXv4E0M-b_qrGTSblxu_KydlSNcHCquhk3oHB29Qt_9_o07fNMt_wO9KS1fyqNzhXcCrEw3zRFk0k8VM1TuWuz7Qz77sFqxojMw5N1uqyxVaemRtWkVg412-LbzZP5a7j8KhpDOcVRJszWRynRDmBhp4aTY5R0ugjhe7fKICyx7kY1oAMJ3Y6W-9WXUiNyFpTvREPaXVonwfwZ1zHK1lq8geHHGPDXV7--0MQvqLI52GNHebh7BbAswWIpms8dSLdG32oXWUgPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انقلاب در انرژی پاک؛ برگ مصنوعی CO₂ را به سوخت مایع تبدیل کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/akhbarefori/656721" target="_blank">📅 23:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
خبر تکان‌دهنده معاون رئیس‌جمهور؛ آلودگی هوا جان ۵۹ هزار نفر را گرفت
شینا انصاری، معاون رییس‌جمهور و رییس سازمان حفاظت محیط زیست کشور در
#گفتگو
با خبرفوری:
🔹
مطابق با آخرین گزارش‌های وزارت بهداشت و مراجع ذی‌صلاح در سال ۱۴۰۳،  بررسی‌های اپیدمیولوژیک روی ذرات معلق کمتر از ۲.۵ میکرون (PM2.5) نشان‌دهنده ابعاد نگران‌کننده این پدیده (آلودگی هوا) بر سلامت عمومی است.
🔹
تلفات کل کشور در سال ۱۴۰۳، تعداد کل موارد مرگ ناشی از تمامی علل منتسب به ذرات معلق PM2.5 در افراد بالای ۳۰ سال، ۵۸,۹۷۵ نفر برآورد شده است. تلفات تهران از این میان، ۸,۸۵۵ مورد از مرگ‌ومیرها مستقیماً به آلودگی هوای پایتخت اختصاص دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/akhbarefori/656720" target="_blank">📅 23:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656712">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y1hpJFczElYXqz5HNhDlDz_X7v9KHZr0doa4wfdIBlfucmA9JtX_K6R8716z7RQwLREqg-gAfR-mQttNrXXx46kpiyIENHN-2BL4YMqRsLDFD4JeTaqhve7CA2tQrso1hJ0aZOH2x0Kb5O8bY4VqQOYqvkMBIpE2JDcqSHSfZZzFeY8tl6WTeJOs8v55EEoesLeTfnDBU3Bk3v811r56aNMc7pRPKNt2LmvpXjx3FEAZeWNCSCj5kZ-FXcvwdstGPqqH8MN3CLViuq7bbXS8Lje-Vw0Iw7xV0IR0sVc4pMPQATUOxm_0L0VJKWJ3_SK7X7ojc0aj3GTFEObxAr1_7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XOO0txudDsGVaKleDsFYwlElhNSO3btjJdNnSrwSMlhci0lZaBtuHqO9nQ1M0aCF7EvkmgCEDUYEs9paLcHTHU5G-mBIUTs_mb7E13O5G6iVr_6kAXb30AmJQ51FqDNCg7rmOecPeYNH5JcJ_HQchdyIJeu8oUBZ0m_wDsaitIXVNQhsaUKIFvhadoqKfIPAG-lE2OfIwyHJZmXB_Z8WoB9YxTaaLvqHE2ZL9na9eShaHParPHbdxU2zwSwuuCqZzSBPrgY71Gt47aV6lqEevBdrfukF_Lr4IwT6lbL3W4k1IMPHeuTorYciwyqSFHQ0_hTI2bW2uSQudX9y_qu4Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hIRrSV686i8SgqtJhwZxCRoVTYQUd5JTZRaYl1vEtXlOb4GV2JsuzNYk0FBC7aZAgBYzBTNb_Y011RsfMXj8o3zRfJ9wpvIcpUoUuK8y1XSLsmh4gchsTxJ1S69E0sLJ_0Tai3z62ocsi2Ph3SaS0BBmSmBb3yIv0OhEt9p_CNMTBvcTyMut_ZuvOhoPaxjmB3Vt95UzOeM1SPh_qskNwAOuIcbuo_woASfe6r1Z9e1MMeKdcKAf-bbtJ4OFBq5ZKtpvhqDaFi8SRcV4JuIfjID8txLp0zSCKyl_FskdczqGTQvCKVteFi3t7v_7bEihfmRPpeg-6gTs7EXb_SSHgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ofTUaRNmTp_fAMqidVH-8od2gK2PrQNVTKjnM_-mmHjy0o5FIhXm39bL4_6Nf8f3ddhLnwfNJrFYySxpQHm0S1trwGzTdhLL4KnD25SeVKqzvFij2ALyiO7HMSYhYlaOrJ6dCbFojvHwQlnQOhP8tlkl_s3-9Z9mJ4bv28-wSn2EIzPv2wALAfSuGv9_rBlPv_0AwSopMFrArtibBOOjdMvKZQui-5FXgKxDYZv9WHtQnTF6HeTs3koMoZ6dX_r_iETFFEwW2tKn9MbWOXZyvHg0tW09nuyveER_AUpB6EKe0xZIrzdVvOkYTItAaAdBts9xOnjvAFMbdCNdOpDWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/feuom3g_sHIYf7KMhC9hSC1S8JvTX-epb-BT2cW9M25YjzKTuh3MF5Mo-b2rme5fTrTx_2w_01ORYYi2mpl7vyW03zVVyGnVZb6Is5VfZYYw9u5GtrOcIdbbcBWb7q5OT_vQ9DqyubeHvEM9JhVEm3JSErxJUPN_CQ9NFIehLxWcr4WI5_n4I1GTFiKv4oQqmi3i4UGEgI9UU_oGZVgdAbXWGytKBQ9rXTRxvDjLZ3q6QY7kdwgtVfQAACShsQ0CyfwssdMAOvprMPKeNbDGoiLpSFFHB6Wy6t5Sa9xCIv98gFSMoBrxiZrxlV4PR4j62xjltjsRmamLJUszy4bPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Rzeij8eYPyW-Nl2WXVhXJ5LbyVW0iOIjZppDP5YYcK07JuB594GyvzvnRqso_zfhNxB7ofXHtH7whQkkSAYdUvbODu0S5Sqr1gt63v77te5X1Xsy6dnZAwnF9pbWLml83lpj4uCttJE2mxWKQXyUD4VfVN7RT6whYEDNxi7tUPE4RTlvsd34LE7ObzLLbO6pSgDaglkeSjjnyUFJSObOSYl0Nk4Gq8yuINQSAHfSa48T3qQhcTnIni8oAmrUwS_u5KD8VO4XyVSS7gt3zQFrUNdff3gulvK91yPraJWcjQDmCGBwTns6rVQWl4WFILIz3seBPFPxgVR-WvpAbcXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVc0zaEa36lhPHmWBLKz1k2ZLyofy97b-4APXnQBdn-uCaia4FbJbuPTdSVtMt0xweqT-JuovjKNLXUHXm-H1HZy1480XW01eFfDgkmTlVhboOOJHEQHSXINUi_9N8FpcLXavv_MkannJo9M30CaIBCIE2g6isskpqH00diq0TZrnE0vXK08636g3lSrY_0UOu4XQRdM5fFvWfkgFpUMhl-uXVC6x6OBAlS4GP0fe18TCUaCMqqVKEcjQ0BQlsaVXjBFV8pqyjsgODl4gZgfoo4maXJCVnYePAeIIA6yok6qX5xoL6isplpYtGrc0I8ssVqwKlvg8s0unPATvwWXWA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
به یاد ۱۶۸ دانش‌آموز شهید میناب، یادواره شهدای میناب در هامبورگ
🔹
برای دنبال کردن اخبار و گزارش‌های بیشتر، کلیک کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/656712" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656706">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EysLYX0cKCpoCjjS6xK6fQ4YOvUHuFNrV1Tc5XC7ReWWkBPUpewk5aP7T1KQ5aSeL3ANByuobkMYqWzxa17ZZS65R2zO52Gv1kP8Yilc-CTaIuUDjcNgy828ZFaQQZ58t_E-IioIeEaIwXBsOdr_gzhtS_ZkxHdOORPpRqqhAA0UTdYqeHUGyK7W7ma2sY50CFlFYYe-GMf0S4UqfAaX_ty2vnDdgXzTzyPoxASymn-YDXRMOwBaIlSJtUeokVa6l4waEBAmGiZTvOZp_mrPZZMCTfs9oW3cHZo78BeaKCoYppfWiX-naBROHLceXP_vf50Gil130dnzCjmxnxyo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLZtsLt1p6dv9oxtdQphUoLEY_zQxhOZmXgASlSY2uJzRFhslV-8hs_j3LQNehKNoUC7feeAHL59ZXbjIefGrP7-p3SKwK8AMWNOWDkJk6va8rLnMtSNVrxeGVJ2cKWXXZbrIK0r1gbkzBIrqUA-iHhf7zUJZyMky-Jm6Lui1BQLazVjNB-5EL1bCUmtYlJ3XaTx_BYeM2T17no1hZUxD--NC8yg-xsaAMOhrVWZP7pXYRnj3G5dwzTX8YQZ8luJz83MRbJ5X_F3hg0SPCjugyYf5tZHFPakpNij8Wrg2NkIboi74klHQOfYY5EfDSWvKXAqxPjp45ia1lbJ8iLjVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WkH4aCqHXPH7X9zib98LsHWT5L3araotlSRe8D3ddIg4lnhSdyTfPiADJFCF7dhcB6dKDhjicFRti49uLYlUdGmGyZZOXoDpzeO9T4u5rlJyxduWCJbQ-RQCJugFZbViPCONtWXwpAJCeWagHxwV2WQ8CBGucggZVecaPqxltEs1O7J0EbpceVWsnLMvEOCyDZbg3CpRpJOF56LsmbPbyYlOJI5Bsfo5Nt5jspY5_0_4HZkXmwGhBSgZlAh3zeYviXuZQV8PS1b3jhKaooj9TPzsltElw-E5_KuJI2XImRjnKFgK7ulL0aimi7OMc-SAQWZVev6qhmNT1wR_fs4rDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvy7skO7RwkfewHPlT8fIxIhAedPmT4JcXKQxihpIueARKUOr5ke6ISAqVTXkVZq8FlG-z22US7laB0TLIFmSyCfKOcKnfDLJH30C_BxVjPw_IhBehI72NNvxqedyrfpD4lDQQAStNU-meKWHQMel_RXUB68v-vb2kgHFG8Q6V5drOc92sNzs05szaau7ebJHHbvx5xC8JGs4tPvW_K7SgqBct9ETQy3r3q58fyHXSDeEOaoMJu_kJWjV-0aQclsTXnjyvQn-T_YYMtx4nhwQNDWYWFn12Sb3LACpKP20rkzya8XLWo9b5XlBugh-1IeSJzgoP_sz3iDojlZeFumZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDhFfsCHtVYKIWbuZhz2YNb_95VxipGQhTaeuS9bFTFx4M-nNj0Cd4QkwOHSiNEJFYD7HDzf5XjaY1WE3L0bejd8GPJ2eGs03nGI_tL83IMZYcvhe60K3wYfOn3xIlDp-68gBp5RusAR0hgmMT4pL9-b8IaIWIoYW63rBwkUo34UXoa2zmQKXGElu1EzsHUoLAr08vLIEja8HaDQwk2QALtLSIhedhPReC7QeRdFfYTzIpUFKUyrAXfPRCloFbzjCkRhcrd56Th7syHGtCCeit3VtidCAQ8RHnYtlGh5KcYanST3PnqRxMz2cYKcvA4daHhr0B3dxwFxe-dRuMlNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wr0qddcujTu7P2kktSLxS6YrjRka-h7VTG00bXdvA40fN971W8AA_jtV4XeFR4HgArxbEB22Wj23tysyr66gZxj4rYrg6PyKJtizHWp3mDxtf6l8jroe-UHpqBESQKaYhN9ArcVpfR8GTI9HU066J0x1RstOdjXrPWvVwUdVe9JAoARFI3c8KgY32mq98tMUsFT_zvNWnAXC4jMVHQ49IX_ACSTG1PYrh0FIQFSs5g89jaGOlv6JWly27iE1yLuMQJcndH3GOIfPsOTYggwXYa3_kQgIgfbAwTWfQB59fJLF0DcORGr4ph48YV-n2bZJnvbxpRyXzN2oDGgamvPyGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
ترسناک‌ترین سلاح‌های قرن/ یکی جلوی هوش مصنوعی را بگیرد!
🔹
وقتی هوش مصنوعی فرمان جنگ را به دست می‌گیرد، الگوریتم‌ها افراد را پیدا می‌کنند، خانه‌ها را ردیابی می‌کنند، اهداف را انتخاب می‌کنند و بدون دخالت انسان حمله می‌کنند.
🔹
۵ نمونه واقعی از هوش مصنوعی‌های جنگی که همین حالا در میدان نبرد استفاده می‌شوند را در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/656706" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656705">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
محمدجواد لاریجانی، کارشناس ارشد مسائل بین‌الملل: پاکستانی‌ها الان میانجی‌گری نمی‌کنند
🔹
نخست‌وزیر پاکستان، آدم خوبی است، اما لازم نیست ما و آمریکایی‌ها را مقابل هم قرار دهد تا مذاکره کنیم، باید میانجی‌گری بلد باشد.
🔹
اگر ما بخواهیم خودمان با آمریکا صحبت می‌کنیم…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/656705" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656704">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
ادعای منابع خبری: معاون موساد به دلیل شکست پروژه علیه ایران برکنار شد
🔹
باراک راوید، خبرنگار صهیونیست به نقل از منابع مطلع اعلام کرد که رومن گوفمن، رئیس جدید موسادمعاون خود را برکنار کرده است.
🔹
دو منبع آگاه گفتند که معاون رئیس موساد یک سال پیش بودجه‌ای معادل یک میلیارد شِکِل (واحد پول رژیم اسرائیل) دریافت کرد و گروهی شامل صدها نفر برای پروژه سرنگونی نظام ایران را تشکیل داد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/656704" target="_blank">📅 23:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656703">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔹
در لابلای خبرها، داغ‌ترین‌ها را از دست ندهید
🔹
🔹
ویدئوی منتشر شده از حمله دیشب آمریکا به قشم و سیریک
👇
khabarfoori.com/fa/tiny/news-3220813
🔹
ایران و آمریکا در آستانه جنگ سوم؛ دیشب در تنگه هرمز چه گذشت؟
👇
khabarfoori.com/fa/tiny/news-3220762
🔹
گزارش لحظه به لحظه از مذاکرات ایران و آمریکا؛ نامه مهمی که میانجی برای آیت‌الله خامنه ای فرستاد
👇
khabarfoori.com/fa/tiny/news-3220753
🔹
جنجالی‌ترین پرونده تیم ملی فوتبال قبل از جام جهانی؛ فهرست محرمانه ویزا نگرفته‌های آمریکا لو رفت
👇
khabarfoori.com/fa/tiny/news-3220848
🔹
پشت‌ پرده اولتیماتوم جدید ترامپ درباره پایان مذاکرات | پس از ۶۰ روز جنگ می‌شود؟
👇
khabarfoori.com/fa/tiny/news-3220986
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
aparat.com/akhbar.fori/videos</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/656703" target="_blank">📅 23:42 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656702">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nhdJ-r-LUwhbXAiCtFEFnW7y6OSREGibLcVPyF9TUdx2O0_izFbqBV5DAS1s4yJ9z8VTTp3Dc7UhuwIG0qQgVMNaD-8vSmeDLQ3eiBJYNXhhkcllEw0-WEoMzAHJusowUhhON5jBi0NhpYz6tUsxs8YA_n3ghIowSytZ3TArYCApL0PV0KVAi_SG4Jc9-y4-O0FyW9PwdbCS-NIz8FhbvnkHt5ttx1S3EszmREsqxsBU8vdcUAfv1t94X0vEkVER5BToi8tTte04C1-0gOEgAXKwz86cw9Mpq_e1mT7JpLH-9Fq69c-6RYp03ZmKeRBbG7e9Sylw4ZRF1M-f0lev9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فقط ۱۶ درصد آمریکایی‌ها فکر می‌کنند در جنگ با ایران پیروز شده‌اند
الجزیره:
🔹
۱۰۰ روز پس از جنگ علیه ایران، ترامپ در جلب حمایت آمریکا شکست خورد. یک نظرسنجی دانشگاه مریلند در مورد مسائل بحرانی روز پنجشنبه نشان داد که تنها ۱۶ درصد از رأی‌دهندگان آمریکایی فکر می‌کنند که آمریکا در جنگ پیروز شده یا در حال پیروزی است. عدم محبوبیت این جنگ ممکن است به جمهوری‌خواهان در انتخابات آسیب برساند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/656702" target="_blank">📅 23:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656701">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-text">💎
دارایی واقعی فیروزه چیست؟‌
🔹
خرید نماد
#وفیروزه
:  چهارشنبه، ۲۰ خرداد ماه
رامین ربیعی، مدیرعامل گروه مالی فیروزه (سهامی عام)، در آیین معارفه‌ی عرضه‌ی اولیه‌ی سهام این گروه، خطاب به سهامداران و سرمایه‌گذاران گفت: «دارایی واقعی فیروزه، تیمی ۵۰۰ نفره است؛ تیمی که هم از نظر حرفه‌ای، هم از نظر اخلاقی و هم از نظر تلاش و دانش، در سطح بالایی قرار دارد.
ما کارخانه نیستیم. برای رشد، به ماشین‌آلات نیاز نداریم؛ به انسان‌های درجه‌یک نیاز داریم تا فیروزه و ایران عزیز را بسازند.
شما با سهامدار شدن، در دانش و توان این افراد شریک می‌شوید.»
🎁
خرید نماد
#وفیروزه
با
آمادگی ۱۵۰٪ در کارگزاری فیروزه
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/656701" target="_blank">📅 23:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656700">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/961752bfc3.mp4?token=fWymlzcHwRg-is46LirlrHJVupdXOfMZH5D63d4I2UdUbttwC-EJVVHgU-OsjUXjt_ceDETge1b2gCHbVQjYa0k5lozGYG9HosBAnV62Ybp3nIFBPWPN2Aejq0tiINPrVt3G7YAokIoSB7KxXn-rthtvlV9ORQE0LNg587g82xs88RjChSFysdZV8yIt-FkvQdehDRA3MoaBfdKJZx1KQbDZ9QX0VkZc2wiLr84hzhrRKCTqo52IWYpVPUio9Dwu0DHwMUiBnvweb-2IB3Up5KVfydWyl-6IPGlBhUmiTicnF9GzRhG05NYTnZQUrIOuoTeTgEkH1AY4c7n0cB660w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بارش شدید امشب شهر سیرکان جنوب سراوان
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/656700" target="_blank">📅 23:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656699">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C_q8YLYI-aj2WKvzxhsnb02KBbULs-6qFvdKfMir0yhyki1NIM5T25EpLzZb6ocrHEDpPWMOANllQgMogDRtn-9I-IHJNRx9w605YlO61csE2LzS8DmR5_0VdwRfvv33n76EMA46W9tics0y55qZOxhmY3I9lPP36fvSols6RpCIRgk7_M0bIYdWhHvoL3nVKEry9ZSXOvwnibGwUYDYAzJWfduTwYzbymh16gCncMrXedvxs7eFrQhlQ9uwTQ2SWRChvXA5cNxmTIYydTEv31k9EZKil34gSdmNHNzAVXghpV_iTkNCJjdC7wy-0jWha51S1BREbcKnrvGienOfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آزادی قسمت همه
🔹
با رونمایی از نخستین پلاک اختصاصی خودرو در منطقه آزاد سرخس، گامی مهم برای شکستن انحصار خودرو برداشته شد. بر اساس طرح جدید، امکان استفاده از خودروهای خارجی در این منطقه با عوارض صفر فراهم شده و تردد آنها در استان با مجوز شورای تامین امکانپذیر است. در شرایطی که بازار خودرو در دست دو تولیدکننده محدود است، اجرای چنین سازوکاری در مناطق آزاد میتواند به رقابتی شدن قیمت‌ها، کاهش انحصار و بهبود شرایط برای مردم منجر شود.
🔹
هفتصدوشصت‌وهفتمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/656699" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656698">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIWV45YlPxeo-dsXozc-tZMxW7JP8oKKLrdhgLQnMY31jZlwBHOmo7YJdDLgJAe4Y1_kvZbmkb7JD0rBhX3GnQI6-_fNjoSnXZbgUp2nq2KOmeM2M-uNFrkKU9H6041qm2upk2bV4Iwm4KSYurlMGiZOix6dEDGqeFKCIdaIltkh6qCgqR9nW2qW5av8z7deUwrbsgiLkJlZeOmbWGGlN8wMEgoIQ9S4utiJ0No57nHMX-GaliO0RUsA9tCkfTlB6P0BvIIJLeLVXPOG67RSwyAH5AoewU2VGIc1X5j7lNjRsyejT8nxkEHiHW6mxgie1zfIQqICHNhcAoU4R86cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عاقبت بسته ماندن تنگه هرمز؛ شاید غذا هم گران شود!
🔹
هرگونه تنش یا اختلال در تنگه هرمز می‌تواند قیمت نفت را جهش دهد و در ادامه، از مسیر افزایش هزینه تولید، حمل‌ونقل و کودهای شیمیایی، فشار را به بازار جهانی غذا منتقل کند.
🔹
بررسی روندهای جهانی نشان می‌دهد هرگاه بازار نفت دچار شوک شود، با یک فاصله زمانی کوتاه، شاخص قیمت جهانی مواد غذایی نیز صعودی می‌شود./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/656698" target="_blank">📅 23:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656697">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
فرمانده صهیونیست: جنوب لبنان باید اشغال شود
🔹
فرمانده جبهه شمالی ارتش رژیم صهیونیستی خط بطلانی بر مذاکرات لبنان و رژیم صهیونیستی کشید و خواستار اشغال جنوب این کشور شد.
‌
🔹
او گفته که خلع سلاح حزب‌الله بدون کنترل و اشغال جنوب لبنان امکان‌پذیر نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/akhbarefori/656697" target="_blank">📅 23:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656696">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDl4u4jGul-yoEYHXv-CBWdJN4Nc3CZ0glg3-MakD7huiYT1DcubW6jeFvRtr3FXxLZlL2iMvm1ZKwRHzBe9pYwmh3oA3ZRUyVWBqUIfPigpEJ_EnfbBc4rVY3-DdNZY7htE7zVWQNezXntNsr63NSdMLWKdATg_cnpzLUkDCcmBkeJzl3AO_cQz2KO0H9uGHNIfPSTKL6PfmRigIdblLydnjAEFoWTqLSS70JTVDZAtuqVoBHvrIip_sN4YHGjxd2NVV5M1rmRlVXvwftKllrKO5LNuapUvtEnbHmrAVs8UgIMquk9GpoaI3aAQUiScIn7FQ4SKpI-dsUNANP_fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکزاد: بیش از پیش آماده جنگ هستیم/ دست بر ماشه به هر اقدامی که لازم باشد، پاسخ می‌دهیم
علی نیکزاد، نایب رئیس مجلس در
#گفتگو
با خبرفوری:
🔹
آمادگی کشور برای پاسخ به هر اقدامی در بالاترین سطح قرار دارد؛ ما دست بر ماشه آماده پاسخ هستیم و این یک ادعای صرف نیست. استراتژی ما با رویکرد آفندی و پدافندی تدوین شده تا دشمن از صبر ما سوءبرداشت نکند.
🔹
درباره احتمال حمله پیش‌دستانه نیز باید گفت زمان و نحوه واکنش، تنها در ساعت صفر و ثانیه طلایی تعیین می‌شود و هرگونه پیش‌بینی پیش از آن خطاست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/656696" target="_blank">📅 23:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/656695" target="_blank">📅 22:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
لاریجانی، کارشناس ارشد مسائل سیاسی: مردم خیالشان جمع باشد که ایران برنامه هسته‌ای خودش را به هیچ وجه از دست نمی‌دهد
🔹
برای گرفتن پول خودمان از آمریکا التماس نخواهیم کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/akhbarefori/656694" target="_blank">📅 22:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDcmj4DoVzM79vasmkRq5XjUeJuPviD5DV6TQXe-UScPHbps7bynehP1Gl-wQ8RdVHzgJM5shBF4gNzw1hXsAlp3EY9cMfoly9auA9wgPrMJTOQpO40bj--U6X76Xykahh28J3btEF8FwhvEd210e1Mf0c8x-XsD8nOrJ8CpSVjWtJerp8zTZ8ZqG9e4l1-0VVw5nm3uzZwPYtm6NZM0pz_P3JyWs37djNBEkrVdlSVgCLtreVkfYKMuXt8pHeN9uUYatkNR0N8aA9qbAFcNMFM6EL4K6cYx9XmcXQnBB8ViN56u18qe5Lj_5t9NIffrZLmtdiGEW0wa3OCN7yeWDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رفتار جالب ایرانی‌ها در بازار طلا در زمان جنگ
🔹
طبق گزارش منتشر شده از پلتفرم میلی ۸۲ درصد دارایی خود را حفظ کردند. این یعنی رفتار غالب کاربران، فروش هیجانی نبوده و به دنبال حفظ سرمایه طلای خود بودند
🔹
حجم خرید و فروش تقریباً متعادل بوده؛ ۶۹۵ کیلوگرم خرید در مقابل ۶۵۱ کیلوگرم فروش. خبری از خرید و فروش هیجانی نبوده
🔹
طبق گزارش بزرگترین پلتفرم فروش طلای آنلاین؛ بیشترین تمایل به خرید در ۱۹ اسفند ثبت شده؛ روزی که حجم خرید ۲.۷ برابر فروش بوده است. به بیان دیگر، بخشی از کاربران اوج بحران را فرصت خرید دیده‌اند.
🔹
در این بازه قیمت طلا از ۲۰ میلیون و ۳۱۶ هزار تومان به ۱۶ میلیون و ۷۴۴ هزار تومان رسید؛ نوسانی بیش از ۱۷ درصد در کمتر از سه هفته.
🔹
در حالی که ۱۳۴۶ کیلوگرم طلا در بستر میلی معامله شد، تنها حدود ۹ کیلوگرم طلای فیزیکی تحویل کاربران شد؛ الباقی کاربران ترجیح دادند طلای خود را در پلتفرم‌ها نگه دارند.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/656693" target="_blank">📅 22:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
سفیر چین در تهران: جنگ آمریکا و اسرائیل علیه ایران هرگز نباید رخ می‌داد
‌
🔹
هیچ ضرورتی برای ادامه این جنگ وجود ندارد.
🔹
همکاری‌های تجاری عادی ایران و چین تحت تاثیر موضوعات خارجی نیست.
🔹
به هر طرفی که «چین واحد» را به چالش بکشد، محکم واکنش نشان می‌دهیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/656692" target="_blank">📅 22:44 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4e31b59b5.mp4?token=WHfF3A_Xq6xZVFGfEJLihCRws2g8KWbqyTHXczFxW8Zho6eTTsZVd6B8yuUY5jDBS86eJBi6n_-hSJSCr0rd5KwdN5hORATpBstJJxOuFGOhCMFpNyycygBMO4cIzyK-ykR07FaLUDBsOSiaiBPRhS7ILH3uugfK-QjUdij6qvByLFEtSw4Ajy4fm0MaPoHo9tM-nGlM-kDW-kUalpprHZi-zgi6iEIrSXRTFPMhaYAKPY6iIE0Jcr5AnP7jbuXjAQMNGZEuWTBiz-aFBY-6MloUPeAUVg96dbcEqiES4-EsslvGmBUqf6p7AC26Mk0j_mK6AsXq7rD3MHm3gq3RJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4e31b59b5.mp4?token=WHfF3A_Xq6xZVFGfEJLihCRws2g8KWbqyTHXczFxW8Zho6eTTsZVd6B8yuUY5jDBS86eJBi6n_-hSJSCr0rd5KwdN5hORATpBstJJxOuFGOhCMFpNyycygBMO4cIzyK-ykR07FaLUDBsOSiaiBPRhS7ILH3uugfK-QjUdij6qvByLFEtSw4Ajy4fm0MaPoHo9tM-nGlM-kDW-kUalpprHZi-zgi6iEIrSXRTFPMhaYAKPY6iIE0Jcr5AnP7jbuXjAQMNGZEuWTBiz-aFBY-6MloUPeAUVg96dbcEqiES4-EsslvGmBUqf6p7AC26Mk0j_mK6AsXq7rD3MHm3gq3RJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیری فیزیکی در بازی دوستانه پرتغال و شیلی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/656691" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاسب بخار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slS-8q9JH0qQCVCGH39-WempiB4mZdrz8N2UnAXrLjaOrgwgNaz6Z4tDyhrFI-IENdur4TB4pMMHoTrKZUFr1zRJNJasg10w0RlKAPILm_4i8eOxxp5HTYpYJSh3kpxjy-uC2y_wfQ7IfGqw2lM4Ejga1SnmQH4hiXO16l0jbUol0d3ActIix4IYmcSj5TVriCvukkbOJWTX7v6DdMQB6n6DThIQ4D67N1bSmCJr1xRp4mS-b2hHZji-A6GX_9k6-z2XDakoegpQSIb3ut7nvzbu3097-nwkkCOtYsxGu0Fal18Jt7-kL-hSUbnprYdOMpozllz-FtsZg3TVSTzDBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
رمزگشایی از خودروهای ناقص سایپا ؛ تولید هیچ به جای خودرو
🔸
بازدید رئیس سازمان بازرسی از پارکینگ‌های سایپا فاش کرد که برخلاف ادعاهای مدیریتی، نقص خودروها محدود به چند قطعه خاص نیست. لیست‌های طولانیِ کسری بر روی شیشه‌ها، نشان‌دهنده فروپاشی زنجیره تأمین و بحران عمیق مالی است؛ فاجعه‌ای که فراتر از نقص فنی، ناشی از سوءمدیریت ساختاری است که سرمایه ملی را به گروگان گرفته است.
🔸
بازدید اخیر رئیس سازمان بازرسی کل کشور، ذبیح‌الله خدائیان از پارکینگ‌های مملو از خودروهای ناقص شرکت سایپا، فراتر از یک نظارت اداری، پرده از واقعیتی تلخ برداشت که مدیران جاده مخصوص سال‌هاست در پشت واژه‌هایی نظیر تحریم و بدعهدی قطعه‌سازان پنهان کرده‌اند.
🔸
واقعیت این است که بحران خودروهای ناقص در سایپا، دیگر یک مسئله فنی یا قطعاتی نیست؛ بلکه یک بن‌بست مدیریتی و اقتصادی است.
🔸
آنچه در سایپا می‌گذرد، تلاقی نگران‌کننده
فقدان نقدینگی و زوال نظارت است که دود آن مستقیماً به چشم مصرف‌کننده نهایی می‌رود.
🆔
@asbe_bokhar</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/656690" target="_blank">📅 22:33 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
یک هشدار پنهان برای صنایع ایران
🔹
شبیه‌سازی‌های پیچیده نشان می‌دهد که احتمال ورود ایران به وضعیت ناترازی شدید برق در سال ۱۴۰۵ به وضعیت نگران‌کننده‌ای رسیده است.
🔹
این ویدئو را تا پایان ببینید تا بفهمید چرا احتمال ناترازی، بزرگ‌ترین هشدار برای صنایع ایران است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/656689" target="_blank">📅 22:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد تهران شد ‌
🔹
وی قرار است در این سفر با مقامات ایران از جمله عراقچی، وزیر خارجه دیدار و رایزنی کند/تسنیم
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/656688" target="_blank">📅 22:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9CALhGnxGQ1mHLd94ckl7WCWlIGVYLzD3P-MZIlFyiH2xELP8wgOa6vc46ZaiiOjCz3vSrOyiaeWKpQMvcAChkcN6HWLMQVjI5A4cIMBnKJpeAriL3J9HlDYeciOjMAgqk1yGriRBZ1FgUtizklSIUNZ0sgyauHFrYpv_vlGLsW3lDkLepAClQ4eIpo4icR0bDfv4zO8fs1gGhDewAWnMfMdoxATMOZIN_iF5Elhjgb8WSGw_BlzeKm0v3F1ZQdQ84vU7nAvj5kijunM9FyqfbZhY-Tj8FoL-3HSZ4leUThTC5Xb8S4ZajnviNzKreX8wRFJk6GHsQwQizTAk5Jkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فارن پالیسی: استراتژی «مرد دیوانه» ترامپ [از سوی ایران] پاتک خورده است
‌
🔹
از آغاز دور دوم ریاست‌جمهوری ترامپ، بسیاری از ناظران تأکید کرده‌اند که او با اقدامات یا تهديدات دیوانه‌وارش احتمالاً از نظریه مرد دیوانه به عنوان ابزاری برای ترساندن دشمنان و تسلیم آنها استفاده می‌کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/656687" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h73AT2gKFzY56OLdV_Bm7jYgDRYBnE0hE7OnfLSbh8kxAyylLi5FCN7TFPp22fPREU5A17NIf_6MuQw8fHtje1jO24QlL5y0nP87ySMGFnlpNX0eVhiSHs0PtzllB56a1PPIFBLb_RPYpahKwZCIzkRQFbFlkacPTOjRgbdikw3HuOYUzZYI1jEHLsXma3PkGi5gtuoFvMJjmgRgFU_FyveNZrZPiEJewkJWtL5F4KKUcH--kNtE4IW9tfW6fInD34hnDloo71GxRa-lq8YafrahPuZK2c5I3-xQjJbSfMI-2-sraAazl408W36hDVoZ7CLBl4HP28WrEjRGI8oUEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت‌ پرده اولتیماتوم جدید ترامپ درباره پایان مذاکرات/ پس از ۶۰ روز جنگ می شود؟
🔹
اگر ترامپ می خواهد بعد از پایان دوره اولتیماتوم، مهلت مذاکره را تمدید کند، پس اصلا چرا اولتیماتوم ۶۰ روزه تعیین کرده است. شاید علت این مساله این باشد که ترامپ می خواهد ژست عجول بودن بگیرد و از طریق تعیین دوره های زمانی محدود و اولتیماتوم های مختلف، جلوی تعلیق و طولانی شدن مذاکرات را بگیرد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3220986</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/656686" target="_blank">📅 22:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
احمد خاتمی: آیت‌الله سید مجتبی خامنه‌ای در جنگ رمضان از ناحیه پا آسیب شدید دید به‌طوری که احتمال قطع پا مطرح بود، اما با تلاش کادر درمان اکنون در سلامت به سر می‌برند/ انتخاب
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3220989</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/656685" target="_blank">📅 22:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDMdcPVbqat0bBbgJB0v9TdUcyy06CoHXug7F02Thj4x7jp3zm2dE55HsmClWfMih9YQf7lrho0SSYusDhwhOtuHhk9UBKUjg2STxmlV113QSqNH-dvg8wk1i8CBh5pJBe2pLx-EWFUc_9ssE-n8TJIlhr7I-Gz5LTRba3uZT8DR9x70dOuEqSsK5RfRrEt19S4rPVtgYLpDuXgaWlAySreBW34wxPjlvzD_L8-Bj6x6o8R-fU2o5tLddI78GyOT5c_3CBr_25Y1Q08VCqpciAPF2_xvmSz3pGX4hQXIRUVdFsWkCg7dS_qbPwRj7zTKLCAHSSiwQt1cmMMzZdTMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
قابل توجه مالباختگان موبایل‌های سرقتی در سراسر ایران
چنانچه شما یا اطرافیانتان جزو مالباختگان گوشی‌های سرقتی هستید،
فقط ظرف ۴۸ ساعت آینده فرصت دارید اطلاعات خود را در
سامانه کشوری همیاب۲۴
ثبت نمایید.
⏳
بیش از ۵۰۰۰ گوشی سرقتی ولی بدون صاحب در همیاب۲۴ شناسایی شده‌اند
؛ شاید یکی از این گوشی‌ها مال شما باشد!
📱
🔍
برای شروع ردیابی، از لینک زیر بدون فیلترشکن اقدام کنید
👇🏻
https://hamyab24.ir/l/aix
https://hamyab24.ir/l/aix</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/656684" target="_blank">📅 22:03 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5Dphf0eFSKqYLmIMRhyZdiX9GpX_nxkImt6MVt6Nd0lYI7Uc8EplgX0y2y4twE50_59P6eVdnzxFFKhNhWIJwU6UIvo-mkLQvrHaaL_IGOG8sEaMV9Mp0-BTjQ4TOC4DHDAd5C2z_WZ9MqUC1eV63HaxhjhbKmdoBWkAEtqfs3Gs3WVBffaXrh4LYtdy934cg8dq-fndAtJjkYkho_q9csky-ixTuwTWsWgZMa8j4nSN2IEBeemczIRJJPvyMs1ZQ4nklDY_PyDCE-A4djoNrtlJCXLMDScC1mTp4WQaOA1j-B6dL_HUK1XLA2QK9g_Nrw_mtDTSVMJmXiP5ybYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ: کتابخانه باراک حسین اوباما، در ۱۰ سال، زمانی که به طور کامل رشد کند!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656683" target="_blank">📅 21:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
در شبی که ماه کامل شد؛ روح از بدن جدا شد و به آسمان بیکران رفت
🔹
00:14:30  روح وقتی تعالی پیدا کند توان خلق کردن می یابد
🔹
00:30:30 دل بریدن از دنیا
🔹
00:34:00 احساس سنگینی عالم ماده
🔹
00:43:50 پخش شدن ذرات وجود در عظمتی باور نکردنی
🔹
00:48:10 تمام عشق هستی در یک نگاه خلاصه شد
🔹
00:52:30 درک عمیقی از حقارت و کوچکی‌ام در عالم هستی
🔹
00:57:29 شادی و شعف وصف ناپذیری بعد از تجربه
🔹
قسمت هشتم (مهتاب شبی)، فصل چهارم
🔹
#تجربه‌گر
: فاطمه سجادی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/656682" target="_blank">📅 21:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
صدای انفجار در خارگ مربوط به خنثی سازی مهمات است
‌
🔹
لحظاتی پیش صدای انفجار در جزیره خارگ شنیده شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656681" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
بازداشت عکاس تیم ملی عراق در فرودگاه آمریکا
‌
🔹
«طلال صلاح»، عکاس رسمی تیم ملی عراق که برای پوشش مسابقات این تیم در جام جهانی ۲۰۲۶ به آمریکا سفر کرده بود، از ورود به این کشور منع شده و حدود ۱۲ ساعت است که در بازداشت موقت فرودگاهی به سر می‌برد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656680" target="_blank">📅 21:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
سناتور آمریکایی: ایران با ۷۰ درصد ذخایر موشکی دست برتر را در مذاکرات دارد
کریس مورفی، سناتور آمریکایی:
🔹
به رئیس‌جمهور آمریکا دو نکته هشدار داده شده که ایران در صورت حمله نظامی، تنگه هرمز را می‌بندد و اقتصاد جهانی را مختل می‌کند.
🔹
هیچ کارزار هوایی قادر به نابودی کامل برنامه هسته‌ای، موشک‌ها و پهپادهای ایران نیست. ایران بر این باور است که قوی‌ترین ضربه ما را تحمل کرده و دوام آورده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/656679" target="_blank">📅 21:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4B8hIICIyb_UNYG42evHCO2fciCqpgfeSYU1jc6OcorHBHmP-9_tGV7YnZWMuzprpoDUsE4cMrcCro_vqZsYXbDTkE9fQlzESTmIEtr-1gwUYeqfM4z7_xywm_DRceqlJimcCh_UmwmBd-jdMXh2rCwXf6Zw1z6uTAhM_5iHlXdWAsGP7ojUJZJ2dRZpfeEd-GH6vJDm5nKYVqY1P6baM71pN4WyITxXS7dpV4PO2lP9UHwh2wkvHXYdwDN_z_il5jdF3dCQV_OfOHx9CmUShvW3P2fWyETJKKCd_gTXLequWAHKXh2JPvI-t5r3ATCm3NG89Ggk1181Ykg0PgXSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از وزیر کشور پاکستان در تهران
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/akhbarefori/656678" target="_blank">📅 21:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
رئیس سازمان انرژی اتمی: نیروگاه اتمی بوشهر برای سومین سال پیاپی در حوزه بهره‌وری و ایمنی در جمع ۱۰ نیروگاه برتر جهان جای گرفته است
‌
🔹
این نیروگاه تاکنون معادل ۵ برابر هزینه ساخت خود را جبران کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/656677" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656676">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
قیمت مسکن افت پیدا می‌کند؟
🔹
بر اساس گزارش‌ها، بازار مسکن تهران از آغاز تنش‌های اخیر در منطقه، پیشتاز بازدهی در میان بازارهای دارایی بوده و میانگین قیمت هر متر مربع به حدود ۱۲۰۰ دلار رسیده است.
🔹
مسکن در سال ۱۳۸۷ با تخلیه حباب قیمتی افتی حدود ۲۵ درصد داشت. در سال ۱۳۹۲ هم‌زمان با آغاز مسیر مذاکرات هسته‌ای کاهش ۷ درصدی قیمت داشت.
🔹
کارشناسان معتقدند در صورت تحولات سیاسی مثبت، وقوع کاهش قیمت در این بازار کاملاً نامحتمل نیست./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656676" target="_blank">📅 20:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656675">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
عارف: هیچ اختلافی درباره متن و پیشنهادات مذاکره میان مسئولان کشور وجود ندارد
‌
🔹
جمهوری اسلامی ایران یک راهبرد مشخص در مذاکرات داشته و همه مسئولان با هماهنگی کامل آن را دنبال کرده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/656675" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzzzQTFCMql7x-ldRRPYf4mQKU2z-OJNIH-trD3NS4cN2VkQ_KQemiW-HC3XJdq244A2y1_O-sdNAwpEzYNNJ0wZslv1SPz5a_lmJ21CKTiRt9_FspdSdyYRMjHOmN7izhmcGZxCtaz2yBjM8EMTwALYXdQJVO9SUdJbgTVtkSbpa8snYZhFWiWUzfQmKT29X-xOh22Xwbc4csqApsZo0beaie2E58eyuyWOtvRZb5r1QyM5CS6hjnsIp92h4qIGV8uhyQ6UnKe-jXD5ZmThk4nMPRXEfBSlt0ElBcJYIt2a8lYhyEkupIhmRdaAS2VHGOjOPBhADZKo4d53ZZ-nyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هک گروهک تروریستی پژاک توسط حنظله
گروه هکری حنظله:
🔹
در یک عملیات سایبری پیچیده و طولانی‌مدت، کل زیرساخت‌های ارتباطی گروه تروریستی پژاک هک شد و تمام مکاتبات، ایمیل‌ها و اسناد امن اکنون در اختیار ماست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/656674" target="_blank">📅 20:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEhG0w7AvO4hYsFCS8zdZn9mbohGdLkAag62QfS-uGImV-cIEZL0B7kcLEDzHMWXFYqW_SKHa8ReilS1wnFifD0G8BQY9oWSPTPAj8xdi51AXU7Lv_7SigGAQ5490BDnKZmWlIA9KIO8jubydHL32RgUKk43C_r7_OgccmbjVgUQlyUPPUv7oRhE1UkRZhQmEjjOSxH9ngeXJL1wyPXoyVmK2DLRhJt-P8ccE2PJzf8D4xdcKTEaAAE-23Nfn4rmHgQJWjMS7TRk3ZShpRo5B4kv5acte7hq62yRNe4fZaO6PC05m8wGImzyulWEUTE5egji3JqyPuXkASFsZybB2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند قابلیت مخفی تلگرام
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/656673" target="_blank">📅 20:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
هوش مصنوعی برای اولین بار واکسن جهانی کرونا ساخت
‌
🔹
پژوهشگران دانشگاه کمبریج و شرکت دی‌آی‌او‌سین‌وکس موفق شده‌اند نخستین واکسن «جهانی» کرونا را در فاز نخست آزمایش انسانی با موفقیت آزمایش کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/akhbarefori/656672" target="_blank">📅 20:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
وزیر کشور پاکستان وارد تهران شد
‌
🔹
وی قرار است در این سفر با مقامات ایران از جمله عراقچی، وزیر خارجه دیدار و رایزنی کند/تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/656671" target="_blank">📅 20:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So160a0Zzynv5-SqHc8EZGjYWkg794LwNraUgrqT2KaehMA9-bLDsqHs3AvtIQryIc5wPrza6KxDpZ59q0B4ocym5WcTYFIVvhK4arAa2feuzqs19VmWxTrAF-XmnIE_27NR9f0R0hLxCSwhZ0lctc4gd1aQ4qU1c4JZ0JyGj0589oMfjuuAQNA_TIB3pep3bI72zMiq6dc3et3Wd8yGC37CK-XMQEp4c0ikBd_A68B0NMDlpC-lnqPB7QMXskk4aGnalFTtR8IYsi9MsVb19V9cxXf1v19H78XcmWKJzh7AJiJUK0OW3Bj1_7YZqXKlxqUfgCN7uslt9MZPTEgRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هوش مصنوعی مستقل شد؛ ۸۰٪ کدهای Claude توسط خودش نوشته می‌شود
گاردین:
🔹
آنتروپیک خواستار یک توقف موقت جهانی در توسعه هوش مصنوعی پیشرفته شده و هشدار داده مدل Claude به سمت «بهبود بازگشتی» حرکت می‌کند؛ روندی که می‌تواند خطر از دست رفتن کنترل انسان را افزایش دهد.
🔹
همزمان گزارش شده بیش از ۸۰٪ کدهای جدید شرکت تا مه ۲۰۲۶ توسط Claude نوشته می‌شود و آنتروپیک برای عرضه اولیه سهام با ارزشی احتمالی نزدیک به یک تریلیون دلار اقدام کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656670" target="_blank">📅 20:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656668">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YNNJlHDnou3hUV2ZmjV32XvOmitywWr0ro72D_B02ue4oCsaxS7oeToEMWqe7DVmLvY3W0P7Xsx-usuD6KAMTwnyqKCbqDzYhyG_7fSsepwVvFnLEym2W1DUtvCj2QsiCKmMmFwYBAHudgNW7gE1MM3iWICVLsn7UBX5yH44ktyGtfaSi5c2PNWFaXWztE9ukMbwHYT4SGQBbruEzwggu13-LN_0tOy9CY57BUWNc1VEMh3MYVaDMDmguUkKwRRdbI_Q9eqLfZTZqssjgTjm89MCtdwTFNpyPFG_GLleHMQ3Nbo2nrjchqY-HfVcVj2M-og4t3cb0dHVFPsAc6WH5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5rZ0UPVRz4hPmFE6DpRYJ-Jd8RsmCmaRSc_V6QT4KonIr1GxTjkaIkvKStxPJe5_Dh2Hk-1nzxJ8NYkWQQyIeQ8Hp10y98RSRBwSzuqBUwiOBho4N55eG9GkipYJvA1FL5rK3yXRZiy2aYg4BP4IDUJs5q6mrC7-HXd82ykidVi8B-Ihkb-YtJ8tN0KgfJvgXLjzu0QzScALdYIkRJAeQKNU_5sn7LC-R8H50M8r--s79mcJ2BeagRdCPL6BcXo1iOk4OyZfmxnUQHqa-MHNHfNJw41nXHxGBkD9FoNj9VzpHRMYClcUtmcZi0OK06KXqcOsb3Nby7yU6FGmpHQHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: بی‌کتابی
🖋
نویسنده: محمدرضا شرفی خبوشان
🔹
بی‌کتابی، داستان میرزایعقوب آنتیک‌فروش و دلباخته کتاب‌های خطی را در دوران مظفرالدین شاه قاجار با نثری دلنشین و خاص روایت می‌کند. کتابی عمیق و تامل‌برانگیز که سند جان‌سوزِ تاریخی است با زبانی ادبی.
🔹
اگر دلتان می‌خواهد تاریخ را از میان ناله‌های یک دلال کتاب عاشق بشنوید، کتاب «بی‌کتابی» را ورق بزنید.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656668" target="_blank">📅 20:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656667">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk8Hdbtq487hzHcOc64fqRVf1TYh69sc9-hKbBKmpx80QUlbceJEuz1swqNdonIClEnVeFlErK6sGDSC1izHyc5nL7r6PEZ3_l_LLlPpMHuBNYu8OnmiTkSKnTZJ9cAl0RiZBGug-4mSqVNLPaKYZQITJgucxdOuOwXT03tqTT3Og8t6P4oH92WlE1rOaHoZeL0Qin34AxIy61Gu1R5Su1q976LemMfs2zzZ9BYeN77nsF27kPYFur_q-8cSA49UjCnWDR9YZwCtxTC81Anr9olovRDhVk1iewyV9J87M2M6aS_LN8C-s1DrMW2NonIOE1L-XvEe0UpXgGkhcpTZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیم ملی فوتبال ایران برای حضور در جام جهانی ۲۰۲۶ عازم مکزیک شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656667" target="_blank">📅 19:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656666">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMbyu0GddF4uhGRIVPMBbvkhQX1ETWIRe5XVZ4m9eRyD5KgII8QHETBbZZDs_OmR3T7GBrfU1MSyXQrE_qpf307oQhn6gkdVyWvyLmfBKLyWNZlQBw7t5mKJUH2y0utgy-ZlFLhENnXbRbxZPfHJJsr4ntdFB6y4ikOO4vvpfbpPWlMrDXOcDQ9M_Nf3Wwu9_LqtOyiWpe6Cyq0VSg9_Hhbupd2UTY_4FBl59NIwckF4Kgp0QG_oErctuapWfrO1U8Y02y_F1BMNCwK04hbXBQQ1LfkSf0a-8IWNFQ6y7dZpafSs_MO2IberHLz60t9uqyDpzWjTifFfDoPU-afTqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگر به‌دنبال تبلیغاتی مؤثر و دیده‌شدن واقعی هستید
این کانال آماده همکاری با مجموعه‌ها و برندها و تیم های تبلیغاتی بزرگ است
🎯
مخاطب فعال |
📊
بازدید بالا |
💼
همکاری حرفه‌ای
📩
برای رزرو و هماهنگی پیام دهید
👇
@newsadmin</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/656666" target="_blank">📅 19:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656665">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDzelEFrlFJdWYG2-YTOhgYY4ybrzqKmHFvl9qwkVxz-mqL4PJVVGodvfZhyjBIsoANapIufCgw8um_1PztS-zrE1YjqLiu4VxdwADJ3G5Qt2VcmkrZOYq9Q8p6wqZYFrjDvAJyZESWx4qls2VAXZYMilMYzjn3MPkPNKSfsCq9pylvj5qHjCi3uCzZDXXDTr5_V_DUefnawJMLfbFrOJ0jbt1qUl-3h9DaN214sAKY1N9-99KuPRnVOVLmQ1ROVo4ZWdE956W68hmvkPgv5Vlun1Ox5LarwQENnURm1RSocwmrKElD5LOgYN-gpO1mcP_bnZ8dfVjtkcNm6fpg7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیا واقعا عموی دونالد ترامپ یک «ابرقهرمان» بود؟ | جان ترامپ کیست و چه کرد؟
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، بارها عموی خود جان ترامپ را که در سال ۱۹۸۵ درگذشت، «مردی بزرگ، درخشان و نابغه» و حتی «ابرقهرمان» توصیف کرده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3220885</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/656665" target="_blank">📅 19:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656664">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
ادعای کانال ۱۲ رژیم صهیونیستی: گزینه‌های غیرمستقیم ترامپ برای کاهش فشار بر ایران
🔹
ترامپ ممکن است به مسیر‌های غیرمستقیم، مانند برداشتن محدودیت‌های دارایی‌های ایران در قطر، عمان و عراق یا اعطای معافیت‌های تحریمی برای فروش نفت ایران به چین، روی آورد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/akhbarefori/656664" target="_blank">📅 19:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656663">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
معاون تحقیقات و فناوری وزارت بهداشت: قطعی اینترنت در سال گذشته باعث از دست رفتن ۵۶۰۰ مقاله علمی و سقوط یک پله‌ای جایگاه علمی ایران شد
🔹
اگر این مقالات در زمان مقرر منتشر می‌شد، ایران از نظر تعداد مقالات علمی حدود ۳ هزار مقاله از عربستان سعودی جلوتر بود. ما سال گذشته به دلیل قطعی اینترنت، یک رتبه علمی را از دست دادیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/656663" target="_blank">📅 19:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656653">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KiWhcGZsPp1588XcV_ptoIewZE0MjQWJUYQsBVcT-z1kmnqHQtESGsjTwF85Kbn4r-CWppFpz1I6oVzHiILIsmlyOEW43S3wZPZzrwtIGRYoiMh0OXvNS4S-IkMtzecsVc9J3T_xUOdjx_DaNrxzdWmLuioTzXiLbBEWAHIBH0CeMiBWWPZcwC4xk6ursc_a7XWAyOwVGx-6GVmFnncG2YH8yN3fl5eEiaYLMzO9PhI4qP1-QpfiFdUjqi1bOFj0L58wQxyW9-88LsZvtL8iRbUZVq_cDyHE4V1HGbg5zoX3yDmA1qV8J6NYUKcaV6VyOpbUyQDxde6mFD79YBTZkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IikpEHxfeDhn0ma_Z3vAEhm3Snbpe5dCHXxWdPfYTvawVfOaTQ-CXxTQfWQV0NC3UIWYrxAyqxC86w1A5iBnXoTt1jMvUP8-9RfuBnBkBPYNrqYa5T-J5VWWtA95GotSdMzmLnUsAr-4sm5CAr10jXfMX_niFwhz8q1TgNF6eQgkzRwFTrBCm4jB_u1EnTQ5bVrBJ_F6jcsgdZJFlHCfg4N8mHeBOwBnyoW43chd9sVfVeV6AJlIvWSvu6-Mat2B8cMSLIM8oe-SjKdVn72cgUbwr4wkaZ6UEnMZ_auYTRaFnUm0KRyHZie26paBNXH1HcVN6JhOMtZarJimniFhSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RtTiNvaiKJd8Znoyy7cB8vmxZ2ZnAknEHGYDV1CM5M8ymUj4gd3xO-jhONcqSs5XYsmZ2zTN3dyqBXBWZ5AeXhO9EfCNOT0a-HH99kb6mrFXYundrifd7VhK8OUgh1qZiaaxTWpXUfvpIqc-VURJvDrgUtJWlVJR8ywkuDGk7XtzUQy4GO-loorPKdU_i8nmHbUMCctn0NcFTi3IILhgqkbxGWo_6jRgvo-tdVnAjWII7uRvPZJg7fKZdesCxwSDOUttcleocq6qdcgI8m1sZqROBY4psSC0YDezkQyJKI2010uGmMCPxclqdu6X2BRme1C47IPGQV8eApxkVWkDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/klj60bF07BuxsMsEndnkGIoZlUZ-EL927aXS4gNXurTCy4ZS0vU9u-f9Fty1eDb9zjWtD97rO0b7EnuvmeVMp1jO_vkz8QldrQXaT0l52rpiAGKaUDLTmvLlZIgVTBd6BFgUIcOSgqBTLEj8Hc1I9kIwOsjh5qJ1Dp1jSNsOFVIcFhmS6meeIV3aD5mHqehLD5bVKl3EmIeAuaEeMR9ybuwgS6cgbsty_96dnozxTWIHTOGfVE5gu_TLxCzSI7ZDokKBwTApgH089wwiv2OasIZeGR1BmkoD-sT43yuevo7yOQKJ9xqG7_ELXi9OotVCrcvoJZR58_mNFSB7Zm5cuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JpS6qsE6rgMS9ZmKg-0BvZZMlmXOsAGOXpVBTMEOnpdTCfqoIdaINF6TlbjQG8ruTxUsMc10K95avjZol8nj_CiwSAOpz6YvfWhUrF56okDvxfKZ6Z-FT57sBvRKlLB0cy-BeAcEhF-k4znkt82lB1CbeCjii1qzhHTQG-2OVtFXSt9FsRKGltKqflcXyWWgTMD5xBetMLhubddPbWCY4XaI3fxOaNLO-2H5mlmy-IvHBIYcnbWJkYZk2mvnofwPwfRZUS3G5S9M87egQNldL5Iwv2XFM5mhmAbFIq-3i_pkHFXMuxyJ-tgQ8c_BD318Zew1SZKFE9Spg8BBf6Xjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxy8tMF71O-yoUNeyXCKy1ePtnwdFqHuIeZAYx7wSd1crmRYX_7FaOsw3DEEXChLqXE3RtclEBTouqH6tkmSzi2iLVZW160b0fttGj0vKeZetp7cTWSMwyia34rKVE8wIo_EUf-7QGN3AJNs5Q3eiL4voPQEz0W4O7MUSTPGjBETP6tkVbJiTLV4ozT0D5uUHtgc5cXtNStUBDoNy3z5zSLJhgAq15266E3THAnAOBT9VA9RmAq-9iAPq7oTqZjUsLkJPgCbiLivRu6E1wmzL94WfQS5xRcSi5KA42UxktbfZ4fGKuTu10eUqIsB458qpXrqK86nLyMNs0oU0UL38A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FVEkxzXukiczjbE6W07mZiANA8Tf7_czbL6qd3k2xgkyY8H1UT_AiHmVhwFFYz2I0EDgnZWNjq9juwsp9BHuby8x4Xj763jawd9mjZmsj2vWctOfzJPtGIC8XrK7BtxkpqwYY7waubmdDzTEcsmd4UHG9GCF17wnvsbNZ3rZD3zQncrtBvRKULMys2YrTHM3AE310AwgTahKK0md6-OXdOiY7RN_y-4MEPLdJnxqKKfdyK6dAAJPKJI6jKPY-qq0N5wM8988zkdbn6ocCEXu06LVQ8GScQBRbLJbnXn0drJcBA_3lFaEH2x76c_qUu5kfWIUinKaPzNunrGo_cfOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPqbbzpWRy2j2Kl7-zQ5-kuB9hJHJdzZbyW1SSpNZpD0IC3nu24-KZr4GPFLcyOGA_FTqNtO5Mj4UA4uhOqOfWVJCz7ryRDxqgVVCdOUh1nuWM1LommvZAEwPoQRw51nw3EzqV7SkQQZnxHKC9qt3nP3KH-8BsqCrns77W9BNb9GoHGzanqQrAvzDnTNsjzlj2at-RlXO_-Xj2xtcbPZ_hGRc34AncgaxNYyHxHq43RBswMHYBkBJHcvUNXeOF0C2FLcbCM9XahfqF1UVMuvX8-iQVVIoVIwjYLtgfN-BCjpSxZrEgUU_1tr9BHkkQv2qPZEc7MflfPtdVmPNjGktA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XF62iGE1z5iu2GZ5RIsWCxpPe--1lTH3zG2mbt8BrdCrFKJ6yUcJPOt2_8aZOBFczCfJcUydgEC4UEIoB0eALEl5_XbQPcilKGleWA-BoXVp1nRNqXADbGKwyqyUJ1XD0v980TSAYOT5Rk0MaxS1MnqxllUWBbdv4N9CKxOuJ1LnHCvieXpMNNwp07lw8I8ouebb4BgD-kzdgC3NtKqmnokHhxfOhazxAwcmR-9e_vjLL9Yn11lB5kbt2CU-XyD0XiUctCDulxvJGeundmDPwTHibdla61V7c3xWh73JPt1xGjlNQ_jQ6cdsgvDCj59NmPB1P_p7VLq-Lfoq3lK47w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BNk75s9XcwW3fHkMQimgEXrI4Nnu6XFZEWhlAq2Hvu-vzeoIEtlJ9NBYhf8X6knZBUnUEz4HiOvYhc5hGFhm0L_As1uosI9nmIYiAw1KXmq818tZfyZLYWv55N5J3APerf3hPU990MFtb10Te6quU1SLPGJaVJknzC9k1i2OwsFNnrBrLBdIPzwRK_uhVOdjtNPM14xfK4-omaGHN0m5z5rUVYxEthfcK3mxJRAhWNqXB-mbZELl_NwoLqMgOEWlneFLyPOafIAJlGuJrxWqY0IcUE1lAXV9vurh408bm3VgcozxTRX1NyTMGU0YZYnk4Gh1Cxf23k5qxUTLDNSuag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مهمونی کیلومتری غدیر در زاهدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656653" target="_blank">📅 19:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656652">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed997974f.mp4?token=KJ4AQ-PUf-b7K26K-rCkotQI3_qHkBd_tGvg9PF3OFRIItjQ6XveAYiX7X7sJd32CbCdModkntHH2qrRnhmTEg4iStLWTMU9gT1XdkriZ3VIXEDiI5YOWQizZ90jUiPaVlZzG_ap7mg8klf0Y7F0h_E10sjVU3a3qvMkSaL65UzbNJBmcM5j0y6P4ZGh5IjoZ0yYrC1qmee4ymI0V4CvFTixlI8jH8TiHAa5xN5fmqxKBV2-4qR7PLFzwWKKSYTKdYnpI61VgiscFHrlFRpfMe8JDgY7BFVMFwdmI2NeQmUW4MQ-gmmq9LzNQ8XqPR05FyMD1i9dTdhcLVJkiqEDWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed997974f.mp4?token=KJ4AQ-PUf-b7K26K-rCkotQI3_qHkBd_tGvg9PF3OFRIItjQ6XveAYiX7X7sJd32CbCdModkntHH2qrRnhmTEg4iStLWTMU9gT1XdkriZ3VIXEDiI5YOWQizZ90jUiPaVlZzG_ap7mg8klf0Y7F0h_E10sjVU3a3qvMkSaL65UzbNJBmcM5j0y6P4ZGh5IjoZ0yYrC1qmee4ymI0V4CvFTixlI8jH8TiHAa5xN5fmqxKBV2-4qR7PLFzwWKKSYTKdYnpI61VgiscFHrlFRpfMe8JDgY7BFVMFwdmI2NeQmUW4MQ-gmmq9LzNQ8XqPR05FyMD1i9dTdhcLVJkiqEDWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آمار حیرت‌انگیز مصرف سرم در ایران
@Tv_Fori</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/akhbarefori/656652" target="_blank">📅 19:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656650">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/So5XEqul3mcQ2u08pvikvnLpw0jC3YsWeQwBNXaHbeZfhHGwS6RPrBvWvVtqGkOMqrlN02QmCDYSyBsW0hSnh0pt5J5ocy9aaFsWqtWxw-73JbddllUb3aF6L31OHwRiMmyVWeQoBBHlp57XVotfoEWCcM7fzzSP4Ob1mCKkgq1k1YScKL0lo56GJBUhJZM23GvgpRFmtwDPY7AnNLQemW9hn6KxNjjxE2zmKzF7fEHJ7yrwU3T0qtlM0E6vpxtLDVIG8wwTM_iTcKVnphqgDA8JK2W5cqi0-Ef8Mti-A64oYviIXjyL67bm7kruxn70vVoCyDVE-sSeQrNwP7Im-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هفت گلوگاه حیاتی دریایی جهان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/656650" target="_blank">📅 19:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656649">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv7vSY3w1P_Zw3DU_s7glU9ntcCtRa3bsBuC9Lu8nb2-UMuJ_uJxYiSSYw5ktbcLHox8-sM-6JUUb46mDNCpB0jXEM8nZgEoU5qfG2-gR_90GYm7AjusgAIKE8SXV7ROldJorA6rm9yjCzzY148VadQla4XcW5tFnOj1v0jwY6iTbpl2PHpkTXXeLM9-SttqSBzNKWXrqONhausTon8_0P850zc2SDsOmaqkne2C3oRRxQDENx2V5dx2Kof47P8nL27BeW9uBZ6c4m3aYVvdkQzD47B9i5WuYRadE10QKnZ9Q_C1jx-N9j_ag7nqLFi7g3Si91LZqqH6zTVS0zc2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه اقتصاد نوشت؛
🔸
پشت پرده یک انتصاب مهم در وزارت نفت؛ آیا پرونده فروش و بازگشت ارزهای نفتی دوباره باز می شود؟
🔹
بازگشت محمدجواد باوند به وزارت نفت، بار دیگر نگاه‌ها را به پرونده‌های فروش نفت و بازگشت ارز حاصل از آن معطوف کرده است. باوند که ۱۰ خردادماه با حکم محسن پاک‌نژاد به‌عنوان دستیار ویژه وزیر در امور فروش نفت خام و فرآورده‌های نفتی منصوب شد، پیش‌تر در حوزه نظارت بر فروش نفت نقش داشت و حدود یک‌ونیم سال قبل از مسئولیت کنار گذاشته شده بود. اکنون برخی ناظران این انتصاب را فراتر از یک جابه‌جایی مدیریتی و نشانه‌ای از تشدید نظارت بر روندهای گذشته ارزیابی می‌کنند.
🔹
برخی گزارش‌های غیررسمی حاکی از آن است که بازگشت باوند با تأکید مقامات عالی کشور و در پی افزایش نگرانی‌ها نسبت به وضعیت فروش نفت و بازگشت منابع ارزی صورت گرفته است. طی یک‌ونیم سال اخیر، مجموعه‌ای از گزارش‌ها و مستندات درباره آنچه برخی از آن با عنوان «تخلفات جدی»، «ضعف نظارتی» و «ابهامات ساختاری» در فرآیند فروش نفت یاد می‌کنند‌به نهادهای نظارتی و مراجع عالی ارسال شده و گفته می‌شود این موضوع حتی در جلسات مهم اقتصادی کشور نیز مورد بررسی قرار گرفته است.
🔹
همزمان، فشارها بر وزیر نفت نیز در ماه‌های اخیر افزایش یافت؛ تا جایی که رسانه‌ها به‌صورت متواتر از احتمال استعفا یا برکناری محسن پاک‌نژاد خبر دادند. هرچند این اخبار هیچ‌گاه به‌طور رسمی تأیید نشد، اما بسیاری آن را بازتاب انتقادات فزاینده نسبت به عملکرد وزارت نفت، به‌ویژه در حوزه فروش نفت و بازگشت ارز حاصل از آن می‌دانند. افزون بر این، شماری از نمایندگان مجلس نیز بارها درباره وجود «شبهات جدی» در این حوزه هشدار داده و خواستار شفاف‌سازی از سوی وزارت نفت و بانک مرکزی شده بودند.
🔹
اگرچه وقوع جنگ و تحولات امنیتی اخیر روند پیگیری این پرونده‌ها را تا حدی متوقف کرد، اما اکنون برخی بازگشت باوند را نشانه‌ای از ازسرگیری جدی‌تر بررسی‌ها می‌دانند؛ به‌ویژه آنکه گفته می‌شود او پیش‌تر نیز نسبت به برخی رویه‌های فروش نفت انتقادات صریحی داشته است. از نگاه تحلیلگران، هفته‌های آینده می‌تواند شاهد تحولات مهمی در زمینه شفاف‌سازی، اصلاح سازوکارهای نظارتی و حتی رسیدگی قضایی به تخلفات احتمالی در حوزه فروش نفت و بازگشت منابع ارزی باشد./صفحه اقتصاد
https://www.khabarfoori.com/fa/tiny/news-3220955
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/akhbarefori/656649" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656648">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-uaigutlaTu0viqrqRsWsfeMzcgqE6lExKXeAKYI60CYY8x6fmwhGqKXds91yx1h47r1woND5tNqb92c3IeOJLmAX02PDn_7Fh3XW0MoeoNrcv48-Wyfa8j-ltUsfQP0iTxa6A4gaDGAw2tFOkziDvRTnyHCSBly9XV-0uz3BiGrLtR9lVKeh7bZiS_1qBfV0Dx3IdB0VgIA_Io7YjbH6-_-AlnQ4u7ix_8kofmQojIqFHGhwy2HzqTvvuMAZyMrdADNXfJN-Lbm_b1duC9o6LtZVvm3bpe3IeQRxpWF6C77jwrFEfE1YgYdBBBR2lO_mSqQxYczXGblzBOUMYr0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادامه پرونده‌سازی برای اتباع ایرانی در آمریکا
چارلز نیل فلوید، معاون اول دادستان آمریکا:
🔹
یک شهروند ۴۴ ساله ایرانی امروز در سیاتل به جرایم فدرال مربوط به طرح خود برای نقض تحریم‌های تجاری علیه ایران اعتراف کرد.
🔹
رضا دیندار، معروف به رندا دیندار، در اوت ۲۰۱۴ توسط هیئت منصفه عالی متهم شد. ادعا شده او امروز به دو فقره صادرات به یک کشور تحریم شده و دو فقره قاچاق کالا از آمریکا اعتراف کرده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/656648" target="_blank">📅 18:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656646">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vArlHvy95NuEJqLhdya0QMo9RTxBibiXoIuKmi2_zGmNi51BWg9JEthv9h5kYKEv8nH3qMA6Fkp9IV3PaReqfk1irpB5vtD5HSDyODEc26oQoa4Hvyw7z8omDowQUSqvZ25zjq8SU2y9E9yooegAtXO1de6o3wOIrL3Ns7YHcg9CWc_SXKqLoKOnqcvU4303F6vRWiXRSyVAaGthY_j05lfjbKjlYwdKYb0aulaR21YJyVhDE9jEQq2JcH7g9S4hRqr9wu2tZ_wW3tMYokdQpmRZS-0E0jBjuzWKO46rTc_y0X02K-0O3vx8_5WmGNW6XKW5kgQZeuuqhKkIfZQj7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/akhbarefori/656646" target="_blank">📅 18:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656645">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f2279c3d.mp4?token=KcOERTQkECgmhinF8aNpES7y9aVty_bhbWbpLzPhci0ZxVkx2XgEudwykVxI958Oj-d0w9ClZLUtH2e5Ni_5YzYNrCbQrT0wqM-VKaf-Pm-Sz8MEAmQwyaaYmqncV6bgn7aQjAxVjOKbw97qDXba29o-mGWX7bMJPzoT3BjHTYtRPwHBAfQB-Rr0d3HUpnZS_wU9ILOiCfEF6KOVgTgxkrs5jvYuQHjLPHx7C7H78Hg19twnEJR9Te_cQdwNuJWwpzan4UkUthNwWpkzjA7eaB-zPV4OqF8ZiZ_oEZC91UCkJaQLQVo0PNQjCuBmXtclA-kjyOgPqctK02FN6UK_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f2279c3d.mp4?token=KcOERTQkECgmhinF8aNpES7y9aVty_bhbWbpLzPhci0ZxVkx2XgEudwykVxI958Oj-d0w9ClZLUtH2e5Ni_5YzYNrCbQrT0wqM-VKaf-Pm-Sz8MEAmQwyaaYmqncV6bgn7aQjAxVjOKbw97qDXba29o-mGWX7bMJPzoT3BjHTYtRPwHBAfQB-Rr0d3HUpnZS_wU9ILOiCfEF6KOVgTgxkrs5jvYuQHjLPHx7C7H78Hg19twnEJR9Te_cQdwNuJWwpzan4UkUthNwWpkzjA7eaB-zPV4OqF8ZiZ_oEZC91UCkJaQLQVo0PNQjCuBmXtclA-kjyOgPqctK02FN6UK_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراف نیکبخت به تبانی استقلال و پرسپولیس در دربی!
نیکبخت واحدی:
🔹
سردار طلایی داخل رختکن آمد و گفت چون جو استادیوم بهم ریخته است بازی باید مساوی تمام شود!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656645" target="_blank">📅 18:47 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656639">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6QV5JcIZGSUwNlC37c7BhKdsTtM2-B3aQ1n05hlT-rJ6S1TLqiBgt50njNqK1uFokmaUOE6J3QpRg0QcAup-6lrHH_C2ZoKa4YyAtD2t1IbOoF7JzrizjD3qJglYxq5xoZk95nlqmyIpzKi0AhjRrn8-fYFuG_xcQsC2Z3IG7yO4JQMJ-4LGUqdfMLHUCT9nMjMlssjYddEUEWMiKlS_1NW5LRpA0Tw6Uv6Z-2cgfV90q4jI1SAebqAln_GtzCvNqEd7x3-bRCwmtC0UEtEcNQChCijfqx2Nxvb09BRPZGb7nQBDxlrqkomGBdZllWVxIi6auQBv-cMjYcQDTjtMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lbxZ8xTxr3FdtliE34wg3bJPHZNtdSRa3xQtMUB_MOqJyvXQhwGoSn5cYlYw3UsvXafwS6jmk7Faejdv0mXMsyvpJCryvIu2l1DCpe6lUTCPtc9mYn3KDx82qVfHvJrXGzyUwYq3NYvlIfX08zR0IRgDfjSLBC5mu06hpxgXiTbQ67wQpvL1Os7IWz6EpTQcoAu4i-Z0RUqpE4ISFVl62TNZh2B76z91hhUUo0lrdSe0QLfsvlajrp5BJy5r7fAcBcEp0oEmdlZGp2SIkl6sZZIx5yWmMDNIVSsTA2i1U1vYIvw2x-efblvdzbyMqtxQ-GQS0ZB-wI4coyIJLVm6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDdlG4aqmBOyCvulqQ78UAy2o593bI2Jxk9xIn4b5mc37o2tLhQxPVxqBJ-ueO4O4i5_yv-qduOHFSgEp9JtD-V_u2KNirSFbkFg9hBLIq3--Cc_TuzzcNJWjp21Qi7NFCGbSSqlmeBtRL26RdypKfY36mfr0GQMrwfZXc_KJBEUc0jbSvP6oT5RMM3EElwbBbs6K5c38gpTDrvpLeVVohvSC1DSB2tvDOzhWjbVsEO1V5TUaEQx-qC3IUIF1VQsU3Jg26q4aYtYODEveFhkk0sjkHh-ldyWrMSQoW_BRCzcEp9OEbBz1o0rMOQzXoD2gnRql929j-Yu4RiL70HusQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VlVzcHv6QNJhNikOuMC37L1Q_sF5TiqfhlZNZEAwjdVjk8nllyznVSA13ljTMFxUsX59u6UGfTWwqE2xPiolECZfX8tRnml-xxO_bzFCMlmiVHnllAx5uwwXhyRBJ2zxTgDh_jkhi14TuDK0RYye2Y2s2ptpDXSYHwZC_6tkZiEtbdWRW7qqa3lkKaOSb8ZsR84C5yggmzMEMKW5NcH8qmzbargYwiy6DWOXMoj2N3EjQjPJ7BUc5NT-qgIVuQU46FM_Ibzsr6YhRiWgenVGxPFSDks0E9MW2Fsob3iKM9sqe2Cb49PSMcvkEIErIAdydkWGr3YaTEpDDYn7bGHlpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKxfpNr2o-0xxdw61hd45LoXWf1YYTrvt8WAeTQ2yKVVh8D0kUXBNYXatkvm0a9S1hiYzsOcxhxc9VRLDefLVy5H3IBBTocMkXNwT4mMMt97L77Zm7BO3AZCg6nP2Tt90MbeqZHtVUAu9cqgRPxfRlaakODSVqL0sMUKd-aUfb4cYAqPC0Nk-Xlh6Dj4mo4gUQOLxd9pKojFIVtCJjpZF7g4IRhpbIlNUZJG1Sl_n9cHJZ_dvt6Msf1266gmHdAS2ylh7wMf0X1hddFQKkNIKnHSsJY7k1f4JIDdz6lTKSrDGcSpCHYOdcfJQiNruHIZPi7ln0OTq-BvegglLuDVeg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کاخ‌ها و دروازه‌های تخت‌جمشید
🔹
۵۰۰ سال قبل از میلاد مسیح و امروز
#اخبار_فارس
در فضای مجازی
👇
@akhbarfars</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/656639" target="_blank">📅 18:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656638">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX6KVjxBhQeeoTanVa1xjFanSW1wHj8bhUig8CyYPwDicoUrv-6C-ux8Qs06vvgGeq9nole0ATixIMH2HdEyPseX6RdxNtjQjvr82k7dSCLmBRSE4VeNIGYQ6FrDm7aaQ4BKuLZ-mQh7fato2Q0FJEF8g1JNxkj-3_3P6-WwO08GvkGQvFr8Grb4Pg7k0lHzjxvWt1DzlsV46exlFNa5Kpj-aSbWp7QA2b5IB6jG7fdkSf49-XCLeCz-EWZEu4HQQph62Ei18KqFk4DX0ml33UYTn08ORe2UDl-OeUbqLMByB7-imKUPpQQDNYVreQJGOq4Oz0BGeysSZ421lqrwKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: امروز بیش از هر زمان به مدارا، گفتگو، تحمل تفاوت‌ها، همبستگی و همکاری نیاز داریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/656638" target="_blank">📅 18:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656637">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481dea67d1.mp4?token=Ss4sOitH3HsyCfi3yhQ4eTyLBlNG--I9tc1C4NARuWeOUAO_7nWPvZh1f9Di0EKnYUBmI6MiWOxdk0KiCpXxchUlXETFg_JunHqMX3REWMw20AfRAJTSXbFf5LcGV721mQs8WGXeQWUJPNTKLixksy7O5Sg12R9dTSsRpFaxYhMEfQOBWi7mR5fGkmEHO6u7TahStcm5g2WSj7KhHcxLiFZPWd4Fb4h1jwa6Icjxgky9FDcY8bGS2XEisQyLPPdJ3jcxUw8tr9XHMkV0xjk_9NChbSr455A6udJ8ITKf_y_cdyJjXO38tnfD7OqRkhwFp9NQt5Y4SejZD-dORCjDSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481dea67d1.mp4?token=Ss4sOitH3HsyCfi3yhQ4eTyLBlNG--I9tc1C4NARuWeOUAO_7nWPvZh1f9Di0EKnYUBmI6MiWOxdk0KiCpXxchUlXETFg_JunHqMX3REWMw20AfRAJTSXbFf5LcGV721mQs8WGXeQWUJPNTKLixksy7O5Sg12R9dTSsRpFaxYhMEfQOBWi7mR5fGkmEHO6u7TahStcm5g2WSj7KhHcxLiFZPWd4Fb4h1jwa6Icjxgky9FDcY8bGS2XEisQyLPPdJ3jcxUw8tr9XHMkV0xjk_9NChbSr455A6udJ8ITKf_y_cdyJjXO38tnfD7OqRkhwFp9NQt5Y4SejZD-dORCjDSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چینی‌ها سیستم ضدپهپادی جدیدی را رونمایی کردند
🔹
ارتش چین استفاده از سیستم دودزای آئروسل را علیه پهپادهای هدایت‌شونده نوری آغاز کرده است. این سیستم با ایجاد یک لایه دود غلیظ، مانع از دیدن هدف توسط پهپادها و انجام ردیابی نوری می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/656637" target="_blank">📅 18:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656635">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jbdHwYp7O6Btr4yqgy_-Icr_ogry-nt-CWFODWZWLHeeu_ecx-JVlKmI3uP2LmADJft77ymn9Vvr8vEIvh6lGGDkidhY5B4nIbW1Fp87N2lVQ3kap4EZqy83kx-F8QiA1xczjZm5lojkcCP0kRj9XG4uCpQpZ_2jjRSPy6kuS7dBHSehV22fD-tHfKuUaShK4UbXCRBtm20t3lD-XQ1KSh_o80zlK7WCJuPyjygo2dZ4USAJBr0EoYAZTHktzOfrP_bmiK1dGkM1Acnc-NddZDwCEMU3ufRZfKNXdcBP-RI5RVOFhsXNcfMLtpNjkVQPiXehEZXwzJ4damPTuYBj-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سلمان فارسی؛ یار ایرانی امام علی (ع)
🔹
سلمان فارسی، افتخار جاودان ایران و اسلام، سال‌ها در جست‌وجوی حقیقت از سرزمین فارس تا مدینه سفر کرد و سرانجام در دامان پیامبر اکرم(ص) آرام گرفت. او با ایمان، خرد و ولایت‌مداری به جایگاه «سلمان از اهل‌بیت ماست» رسید…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/656635" target="_blank">📅 18:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656634">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
فیلترینگ دسترسی مردم به دارک‌وب را باز کرد
🔹
گزارش‌ها حاکی است محدودیت‌های طولانی‌ مدت اینترنت در ایران، کاربران را به استفاده از روش‌های پیچیده‌تر برای دور زدن فیلترینگ سوق داده است؛ موضوعی که به گفته برخی کارشناسان، دسترسی آسان‌تر به دارک‌وب و سایت‌های پرخطر را فراهم کرده و می‌تواند زمینه‌ساز افزایش جرایم و سوءاستفاده‌های سایبری شود.
🔹
این یعنی حتی سایت‌های خطرناکی که در اروپا و آمریکا مسدود هستند به راحتی در دسترس عموم جامعه ایران قرار می‌گیرد و دسترسی به محتواهای خطرناک جهانی را در داخل کشور فراهم می‌کند/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/656634" target="_blank">📅 18:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656633">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-5PXBBHrxwxhaFCWP2mPCINwLQenzikcHss2Arl7Q-TWOokv8297D6dUnKAF_TYL0vLMx_RrEaBO7MdB-P8MjxDBppWQGr7MzuhdCvcpztE0DKGTAoz8h02pS5wGF5FR9ocw6LTndPFgYMOOWRVkVmv-f4jxyEangyHTtq7jjE_MHi9-zjmN1OBZ1MkeSfJNtNSCQahmwHrMxL3GSj96zOyUHIIhj38Y2g139VYpJBMAFS-btYReVNbxh8P0UGcy6hH0DU0XXRd3FhDQT3nicPXLqRonrr0RSxRL4-ROA5o4sqUFpMLbVYrTsZiwmqW1OhaTkLeJIdQRTFp_T1zLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین قیمت نفت ۹۳.۰۹ دلار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/656633" target="_blank">📅 18:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656632">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5362fe20b.mp4?token=v4_JeR04ANePRvNKwdOxle2z-rV4aG_IlgmBhMHkJQr6mpO8EvigMkM5QOPUylkUasMfCJEGN6tR1PPTJ7rr_eMSTDF1Ffhc7Ft-LFL12nwNapWGQfcbUbGJR0Zi2K2i2ya42wUTSOOaNBCm_ZEisnO_7dCzASXzermWZCBPqRV6w1bneGU5x0JH2R9ufsRHFDEj5klkHfKO3WVTTTyJRSYyD2PzAuyFHCXF-GrFWCg2tCIfXVA3T_Rt_jXI_5RJmxZNWV5tPVqVTVyYgIc_oUGAqEFOj0jmKXnUrtw18pZnvdv26tlsCcJgv76okyNAA9YjoTqWKKUnl8ju_w2c0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5362fe20b.mp4?token=v4_JeR04ANePRvNKwdOxle2z-rV4aG_IlgmBhMHkJQr6mpO8EvigMkM5QOPUylkUasMfCJEGN6tR1PPTJ7rr_eMSTDF1Ffhc7Ft-LFL12nwNapWGQfcbUbGJR0Zi2K2i2ya42wUTSOOaNBCm_ZEisnO_7dCzASXzermWZCBPqRV6w1bneGU5x0JH2R9ufsRHFDEj5klkHfKO3WVTTTyJRSYyD2PzAuyFHCXF-GrFWCg2tCIfXVA3T_Rt_jXI_5RJmxZNWV5tPVqVTVyYgIc_oUGAqEFOj0jmKXnUrtw18pZnvdv26tlsCcJgv76okyNAA9YjoTqWKKUnl8ju_w2c0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رهبر شهید انقلاب: من و شما همه رفتنی هستیم
🔹
ما هم عالم برزخ رو در پیش داریم، اگر انسان اونجا بتونه شفیعی داشته باشه، خیلی قیمت داره
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/656632" target="_blank">📅 17:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656631">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXU8gFbluDQwNJUbri3lkLI6bVS9V3Xbb2afvLH80P0YgIJsWjAnTLkNydS6f_bHnfbNVK8biJ_2hozZpiYh5gKLL6CpN2ZlskY-5b8cPlct2XCDi7X-LE0oyvgiYYBRoMLr9Zi_DNsvzaJh3-ABtCTnbeKYx-Cue5dz0WsKjU5D9GtPkR-wDCwbmI_gvyvfgmdjSSuwpn6F_p_R6q8Svv0eo1pJee3sf7Rve-pLxfhZCU6KOR0xcvCZXBvb-GPF7lx9MSfxGUUEwWe8oggj8CqKzXj0_ETA033PMRVKkZXU-wAKVo8ZwZS2GQbGkWgTwM-1VsJm-47ipeobDDbSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی: حمله ایران پایگاه آمریکایی «علی السالم» در کویت را هدف قرار داد   رسانه‌های اسرائیلی:
🔹
در این حمله یک ساختمان محل نگهداری هواپیما و تعدادی از پهپادهای مستقر در این پایگاه هدف قرار گرفته است.
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/656631" target="_blank">📅 17:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656630">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d271feecd.mp4?token=OlaslAuzU1g5Fa0iK5watudaWDoXM77QIA4T7-6zBJAE7sesvyGlV4Xb5UR9Amt2_4h6OIlAPawHuGifbH5twCRIYDrpgzpiDGZgdNHgu-fT4X34QUe5vC-oaPveFpKOt3SA38RyDQeFChjMe7Td-UHxY1pYj2t-VQ0RK3MWnq-FtiAEIB8aTZlH5RxfYJorQd68Zj7JULCNlW8ErreoSWNYFnCBZdsjXwAPVQpqN-hkeHZYHn4E-VH_LhuoH6oJE4I1MsoHKIpMaJYdjrSaFht04b5ff5PBDjIAQgAOetwdZvPIbdnViHzIv7nYfOcOmcHagJWhlfqokzdDO-QORKJlZoDMgXZX0k_IDBRNjCc82jBCJ0qmTUov4uEym7_4EinsLG4sedYHs8boszMxlivR-jH8-6hAzB256VaUoVvq-0IZ0Ji5V5P-Z1PY2sYXhprsxQ1rMkxeDOinhnIKvAvzn-Ut_1cXYszaOh6Noa1LZfzPuUyWKL7UmBlqZn_o8bMbFVLgNB-OGT13zNZOypNjiSq7p99NRrjQzvIcKrzQgndxiBqOwGirFz1hC1iIoGVKYwmWIOBP6iFKdmjQxdlN1zniAsYXEBE-uezIFU9T-VTzA1sG3MGQYTGQj5Q36CumhauDYB7c_Dk6TRuD5yEEKMNb60DUUUW71rhqsqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d271feecd.mp4?token=OlaslAuzU1g5Fa0iK5watudaWDoXM77QIA4T7-6zBJAE7sesvyGlV4Xb5UR9Amt2_4h6OIlAPawHuGifbH5twCRIYDrpgzpiDGZgdNHgu-fT4X34QUe5vC-oaPveFpKOt3SA38RyDQeFChjMe7Td-UHxY1pYj2t-VQ0RK3MWnq-FtiAEIB8aTZlH5RxfYJorQd68Zj7JULCNlW8ErreoSWNYFnCBZdsjXwAPVQpqN-hkeHZYHn4E-VH_LhuoH6oJE4I1MsoHKIpMaJYdjrSaFht04b5ff5PBDjIAQgAOetwdZvPIbdnViHzIv7nYfOcOmcHagJWhlfqokzdDO-QORKJlZoDMgXZX0k_IDBRNjCc82jBCJ0qmTUov4uEym7_4EinsLG4sedYHs8boszMxlivR-jH8-6hAzB256VaUoVvq-0IZ0Ji5V5P-Z1PY2sYXhprsxQ1rMkxeDOinhnIKvAvzn-Ut_1cXYszaOh6Noa1LZfzPuUyWKL7UmBlqZn_o8bMbFVLgNB-OGT13zNZOypNjiSq7p99NRrjQzvIcKrzQgndxiBqOwGirFz1hC1iIoGVKYwmWIOBP6iFKdmjQxdlN1zniAsYXEBE-uezIFU9T-VTzA1sG3MGQYTGQj5Q36CumhauDYB7c_Dk6TRuD5yEEKMNb60DUUUW71rhqsqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت محسن رضایی از آخرین دیدارش با امام خمینی (ره) و جمله مهم ایشان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/656630" target="_blank">📅 17:46 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656629">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rsLZlGa6W4AAlxm-70vshQcWdU8fvkCCXR24GdBOMmotWnXU2lj8fzmnxzNliSQRUe24_kPEcVfy8b9N7I1oyrgjXpkrrDotuX1O54g-MjJ3AjtcLonVra2_yMqm6wxetxwk6BOIstnvOEfe127N3-UkQ5f0RYi_dxwoT39pHKBfsm7ZnwkA4uvtsAUXYwt77QFutiDkUUccItbLfXJYrRzgoPCsV90jxlFK0XrK_kxhlGubGRzwKRlHcB5NkK_RYetXxlc2bZZOjQr03sNRCbHAD4nFqxEHvxHrAKhik33_mg_6KjDLwZNUd6qTNAzpScPx_BuiA_2wO1eKVQROSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گاهی فقط یک رنگ خوب، حالتو بهتر می‌کنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656629" target="_blank">📅 17:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656627">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
ممنوعیت دریافت وجه اجباری در مدارس دولتی
وزیر آموزش و پرورش:
🔹
دریافت هرگونه وجه به‌عنوان شرط ثبت‌نام دانش‌آموزان غیرمجاز است و ثبت‌نام نباید با فشار مالی بر خانواده‌ها همراه باشد. کمک‌های مردمی کاملاً داوطلبانه است و هیچ‌گونه اجبار در پرداخت آن‌ها وجود ندارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/656627" target="_blank">📅 17:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656625">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f566b3db.mp4?token=PMuTuvUc_lW-_mYfDgAnETfwH62o8_5YcUVZSz5aUhnf_nJ5gcjtGrHhAfxl0HBqvWzmGTcbqRAjBrYC-CSvy-MJuHCNWArkcxnf6V3Mtp-FdvghCqQrkHuJNgcgWdVW4WNG4pyHUbkqbjUU99zB5Vv9NxElYZl5Tq49dbJgS7FyXqoK9BJYzBvCp5p5Eik5ZhaegVBOGMvXq1n9BRL8RnoBZBNBmTcdV7BM50_KHhHugRDWY96AyKngX1GM2yebqHurxjW-mamRT_PNgbWGzociJb3RPdyGmsKLQnYuJqWAfF3JOwnj1tTwytM3iLJn62niybtDbR9XhB_okH5oVV8NaGJM8tAwZpGvkOapiTUcQmRZv1a8YhejXgEbUweaCnhjHdmG-JXstZOczPLY8gFx4XUC91-mk4XzznrpiuXxcTndQDiJCqA6dchVIXQ1KTLkX5UJmzopd8XCO9xQh2EtEGCz0OJfRL3_nCnod0S5FkPyklKM4HLikmCHxmVeWcA0B06LVIKOMmnjQ-cqHuXtHNfcgwXOL4bErebvQ0cJIJgImrOFVu8BzIjFDPNpPaZJPgOZfE8iSXuqXVtZm9xFuKq0F08G5tZEmfoC0uh1eIuDv2gM95XDmFprtv-AWIc9GZhjeg-iwsAKCn2rX7J1QnapFIE209Y8F93FdRU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f566b3db.mp4?token=PMuTuvUc_lW-_mYfDgAnETfwH62o8_5YcUVZSz5aUhnf_nJ5gcjtGrHhAfxl0HBqvWzmGTcbqRAjBrYC-CSvy-MJuHCNWArkcxnf6V3Mtp-FdvghCqQrkHuJNgcgWdVW4WNG4pyHUbkqbjUU99zB5Vv9NxElYZl5Tq49dbJgS7FyXqoK9BJYzBvCp5p5Eik5ZhaegVBOGMvXq1n9BRL8RnoBZBNBmTcdV7BM50_KHhHugRDWY96AyKngX1GM2yebqHurxjW-mamRT_PNgbWGzociJb3RPdyGmsKLQnYuJqWAfF3JOwnj1tTwytM3iLJn62niybtDbR9XhB_okH5oVV8NaGJM8tAwZpGvkOapiTUcQmRZv1a8YhejXgEbUweaCnhjHdmG-JXstZOczPLY8gFx4XUC91-mk4XzznrpiuXxcTndQDiJCqA6dchVIXQ1KTLkX5UJmzopd8XCO9xQh2EtEGCz0OJfRL3_nCnod0S5FkPyklKM4HLikmCHxmVeWcA0B06LVIKOMmnjQ-cqHuXtHNfcgwXOL4bErebvQ0cJIJgImrOFVu8BzIjFDPNpPaZJPgOZfE8iSXuqXVtZm9xFuKq0F08G5tZEmfoC0uh1eIuDv2gM95XDmFprtv-AWIc9GZhjeg-iwsAKCn2rX7J1QnapFIE209Y8F93FdRU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیوی ترند اینستاگرام برای تیم ملی فوتبال در جام جهانی
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656625" target="_blank">📅 17:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656623">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWao0njeMy0Wal9HtHqV-HCUZLi-c3-6RwhnWHE6-zTSs3a8pgsmr41aHNuVux8CR0x884_-7p0s9z4-Mos7R1c8ki98iTSSG24OC2EShoXss-JHl5R8EphqDnV8yp0AN5hggyYBtbqPCMvTmCDHKpYIwXxvO9Bz5oyyVniNnSQ4tINYpIvVTWs8-Zm5jNPCeinhKCstLvfj62M6_TpwsI1MdjUCy4NnOrTCFsaI2_JLj6Loqwac3S9BBYT-0PKrfcq4wHNBLe8tPAzDeGnyVcFQTnoEd46eFIKcwAlrvtfTNrQvZoe5X7MXjpChmm34CVe-INEksSspFY6vIXvxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وال‌استریت‌ژورنال: ایران برای صلح پول می‌خواهد/ ترامپ سختش می‌آید!
وال‌استریت‌ژورنال:
🔹
یکی از دلایل اصلی گیر افتادن مذاکره ایران و آمریکا، این است که تهران می‌خواهد به پول نقد سرد و فیزیکی دسترسی سریع داشته باشد و از نظر سیاسی برای ترامپ موافقت با این موضوع خطرناک است.
🔹
آزادسازی دارایی‌های ایران از سوی ترامپ، با انتقادهایی روبه‌رو شده و با حملات گذشته او به اوباما درباره پرداخت پول به تهران مقایسه می‌شود؛ ترامپ پیش‌تر وعده داده بود به‌جای توافق هسته‌ای، «توافقی بهتر» با ایران منعقد کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/656623" target="_blank">📅 17:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656621">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjNNXb2Fs5uERygoZxntjKh8g9HaykLp2yfP_O2kiwN8gplzzJRMfOF0rvcKFZgOcC9l2x2ZkUwRBOo6Ig6kJ9HaccwG3SoKL7KeLwyE_1IRLDUOfMhzZnXP3qZkH8e6vye_GbT0MgkJ4ORLrBNHu-sLvBzKhRWosSUuXvBpoc8VGrN3sfpLNturOf0jvKlvf_zDb6ZW70cthjgoSXKNhx6pIvisnMuNLKwSV8WOe5VQytG4mJhcUJ6_A7VNQaMLD-hAM_r-y8QyptdVwfQ_A_v6h_yg4Rj4uc0AdnpbNkCRXjZQ55KIPSC86fdwGY64PlulQFFgYkFRILE7g7JNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جوان‌ترین و مسن‌ترین بازیکن‌های حاضر در جام جهانی حدود ۲۶ سال باهم اختلاف دارند
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/656621" target="_blank">📅 16:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656620">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
تمدید خودکار گواهینامه‌ها متوقف شد
رئیس پلیس راهور تهران بزرگ:
🔹
در دوره جنگ، برخی خدمات از جمله تمدید گواهینامه‌ها با تسهیلات ویژه همراه بود و مقرر شد اعتبار گواهینامه‌های مشمول، به‌صورت خودکار تمدید شود، اما اکنون روند ارائه این خدمات به حالت عادی بازگشته است./ مهر
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/656620" target="_blank">📅 16:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656619">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd6e0fc384.mp4?token=UKvGB8foXlVusYFjyC8f0TJBWlYr5pVDflC4i4_Sqm8JUm31Ty_yqLiPx8G_O0KlQJ8egatS1HMCXxPTyH838yTkYm6MyAr3TTT4JKuqx77MRqF90mOaoHYaJJ8yvlNIV4n6iSiajpWGLjBbLZV5AuDyjfFN2Pt639HZrQ8bWD1LoOKUJ-r42q9lDADLOVMgHA9Fyp8tQYqnntJY--PdhSwIvVJtDyNbK41k-LRliq3gbOKbBl0kLmWaRnPf3S37RMWpAQKVe7SZqemOqRIzeKJF-mjb7Uqzfqxd-VKenzd4ppUyD8_mttNmcB9EZyq7UeYm_QqkvESJU2mJDm-CQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd6e0fc384.mp4?token=UKvGB8foXlVusYFjyC8f0TJBWlYr5pVDflC4i4_Sqm8JUm31Ty_yqLiPx8G_O0KlQJ8egatS1HMCXxPTyH838yTkYm6MyAr3TTT4JKuqx77MRqF90mOaoHYaJJ8yvlNIV4n6iSiajpWGLjBbLZV5AuDyjfFN2Pt639HZrQ8bWD1LoOKUJ-r42q9lDADLOVMgHA9Fyp8tQYqnntJY--PdhSwIvVJtDyNbK41k-LRliq3gbOKbBl0kLmWaRnPf3S37RMWpAQKVe7SZqemOqRIzeKJF-mjb7Uqzfqxd-VKenzd4ppUyD8_mttNmcB9EZyq7UeYm_QqkvESJU2mJDm-CQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/656619" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656618">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5531e602d2.mp4?token=D2Etk0RRx8luecclsMUbxs2v8PJLXRiDgbihY3AHC_dofW8-wuBrNoEs23-o-cjx8a1GpQuXa14RCOKkn7YcTw9_-xCs7jzzBI-K3XZCa-iQV7I_hnMKuHSNUAaU_3d6L1K0m2AFn7QBcWH_L7MgNA-nSzqw-CxMlwaua-nzsShi7k-ZmaMzojiF47lizhRIyYBxZZK7dDNf_D9cPQBMvJEdHLXsTGTBeIx5erLxVOiP-PROtTvdS4CdEtEUAJlYFOpcpUYLUzJuzm1fnZH-6qFX-FTwOUZWtFK27sVYlW5toRrhQ9qyVHIpNx2zJnvH0fpuSSjvI0szTCK4IIAJGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5531e602d2.mp4?token=D2Etk0RRx8luecclsMUbxs2v8PJLXRiDgbihY3AHC_dofW8-wuBrNoEs23-o-cjx8a1GpQuXa14RCOKkn7YcTw9_-xCs7jzzBI-K3XZCa-iQV7I_hnMKuHSNUAaU_3d6L1K0m2AFn7QBcWH_L7MgNA-nSzqw-CxMlwaua-nzsShi7k-ZmaMzojiF47lizhRIyYBxZZK7dDNf_D9cPQBMvJEdHLXsTGTBeIx5erLxVOiP-PROtTvdS4CdEtEUAJlYFOpcpUYLUzJuzm1fnZH-6qFX-FTwOUZWtFK27sVYlW5toRrhQ9qyVHIpNx2zJnvH0fpuSSjvI0szTCK4IIAJGzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: اعتبار ۲ میلیون تومانی کارت امید مادر به حساب مادران واریز شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/656618" target="_blank">📅 16:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656617">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
منبع آگاه: وزیر کشور پاکستان امروز به تهران سفر می‌کند/ ایرنا
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/656617" target="_blank">📅 16:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656615">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UuLNvK3yDvlYat22MOBZcUCP8L3qcroebLBbbzJDI2Li65bRDzq1wyJbiZffXQJ19tzdzddbroaAfx4nbojkSx48eIAB4jWZoZvPerqHhihGX-iVmjLhRan9PjRw-btV19DFXlcq5f_IP8Yr6IySvIiQO6bcEPKbATANOz_cohfmcgXGebTsD3nk8JPxu7Uviz2qqIEwbr3jv6pRG01WXAJ-EKfMNN4DhUjEN1uFdK-CxWftowRIbQSuU04vGwirezNv_2ricjG9S4TN54QmMZP06Oup9dYK6IYVC78dEcngSyH4SVMWaZmZ3CFKO3fuQPEcfQuwi9R7WmcoZc63tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PFblXjtdKOBb1d4jbt4OZnsJb5r7IKJGrgH8e8cMaCIa1JrnFOnEvwhbX5HPkoVsM0lBVCcpwMNUbnQ-NvEuizOj--ECFLigz4OEuzog46lf5mT0RjoNGZP-XCL9d7aqDCtxv7rg6o-yR1_nieq2vRwcNMZOTlmNfvKSk4E7ByUqKf75SR3DhMzdl7MhIU8CVsI0Iwz1kWgDTsMXb2u2N7r6dkWuS3P_VuICSqF7ZAOz9Squih0WTBUXRumA0Th0cC4TwouKkog-_IvvdsAZUrfMoBsNcDvG37hsn758HoRwG_orswXuXB2WKx2MqaWFzNTerXHKyiXpmSTfmdXW_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از اعضای تیم ملی فوتبال ایران پیش از عزیمت به مکزیک
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656615" target="_blank">📅 16:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656613">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تکلیف ۵ بازیکن خط خورده برای سفر به مکزیک مشخص شد
🔹
کاروان تیم ملی فوتبال ایران امروز اردوی خود در آنتالیا را به پایان رسانده و ملی‌پوشان تا ساعاتی دیگر با اندکی تاخیر راهی تیخوانا مکزیک می‌شوند.
🔹
بر این اساس محمد خلیفه، هادی حبیبی‌نژاد و امیرحسین محمودی سه بازیکنی هستند که با وجود خروج از فهرست نهایی، در کنار تیم ملی باقی مانده و راهی مکزیک می‌شوند. در مقابل، امید نورافکن و کسری طاهری از جمع ملی‌پوشان جدا شده و به ایران باز خواهند گشت.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/656613" target="_blank">📅 16:35 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656611">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34b44d587.mp4?token=S9qnS4kwiPtKLEMW0NRh5wVAJ0R2wTSO1aHKITPZavdxJ6EIXn8Gr4b0AK2YQ6Z75hoRxrhKXU3t-loBLU93sYz8y6ZPhi4LprPe7yaR9CEgNg4PtedwP8-8JuRekQ8HUotQ7bG9prN_tXS4kpbznyYuMrKgLVW8n5eJ9aSVgGe8Im1-ow2n9e23o_1EQ1H6hjrnLzakqdSwhreI7_ImN2MgbHedSnFQDdZkIiN19jrA2i7OwneL6rYfOcwvwt-Jd2LMRyjTxvfM7Wra61P_rTeILmosDILmLNIOI2sn6S1kOX2nnKNtbuOeaYOBq2UdS9Qwg7MLNYmaGmlZ5Tv2uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34b44d587.mp4?token=S9qnS4kwiPtKLEMW0NRh5wVAJ0R2wTSO1aHKITPZavdxJ6EIXn8Gr4b0AK2YQ6Z75hoRxrhKXU3t-loBLU93sYz8y6ZPhi4LprPe7yaR9CEgNg4PtedwP8-8JuRekQ8HUotQ7bG9prN_tXS4kpbznyYuMrKgLVW8n5eJ9aSVgGe8Im1-ow2n9e23o_1EQ1H6hjrnLzakqdSwhreI7_ImN2MgbHedSnFQDdZkIiN19jrA2i7OwneL6rYfOcwvwt-Jd2LMRyjTxvfM7Wra61P_rTeILmosDILmLNIOI2sn6S1kOX2nnKNtbuOeaYOBq2UdS9Qwg7MLNYmaGmlZ5Tv2uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گستاخی سفیر آمریکا: واشنگتن هر طوری بخواهد در لبنان تصمیم‌گیری می‌کند!
سفیر آمریکا در لبنان:
🔹
مذاکراتی که در واشنگتن برگزار شد، بسیار مهم بود، هر طرفی حق دارد تصمیمات خود را بر اساس منافع و رویکرد سیاسی خود در پیش بگیرد.
🔹
ما در لبنان هر طوری که بخواهیم تصمیم می‌گیریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/656611" target="_blank">📅 16:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656610">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9jdXV67MRtIHD3HoyQAtXf8tOYWoKBwuHx2UjL8_gNUCvMwiAtlXnAgj2g7cSWNdZZma3t1ht_jR5h8WIAzSApnnEFroIjF4jNK_TUQIRfntbRxCFLlrjdPCUyyb_wV_5KuXieM4l0gqJUnBQA4LLS3E0pfUpmK_zgeWkCZXbmYZ2PjWMR00jiXijVV7-Q0MJvoLktR8mag0-DzPT1GDAeckj5eUI8iUC0aeCTqSVVrPLIvcIYUojtknt8P2bMEtMIjv8Iz4WGHx4gduyMCJbrpynhgB_JO4ZYLyi2QnirzmvlYRXLYx2-JKOJALCOuUrS5K8FPdrTroYlgK70Pug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هزینه‌های برگزاری جام‌جهانی در ادوار مختلف
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656610" target="_blank">📅 16:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656609">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3c84cedc.mp4?token=PQgV6C5LpMlOxJerByxztbNiGBDN4pAGEyGb5EGDUUHLN_bOcBCYSjtnDSQV0iJsdVjU2BpYENFCiwKchrCaxi8EuRHKQZgV86ikSvoiTfMpNu8ScOpQoW11ajq7vegZ18C1n3RpXNNmy2AA6xgNZWkLj-TU8oPPKe1SyjVLrkNGQFl_y4XmRnU8JlFON-qakDYHWTW7eLErCNyHg0vRKRe1GdV_e6e-JGiK9x3uDABRwNLxrjdrA2KesVufBOiSOWskwhwGk_OeDE7dn5JNb79eNffkUCzeOjZs5DD2Hd0FPeKj8xLl-W2y1aANbZDKKEfNkqv001SApZMkVUhVhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3c84cedc.mp4?token=PQgV6C5LpMlOxJerByxztbNiGBDN4pAGEyGb5EGDUUHLN_bOcBCYSjtnDSQV0iJsdVjU2BpYENFCiwKchrCaxi8EuRHKQZgV86ikSvoiTfMpNu8ScOpQoW11ajq7vegZ18C1n3RpXNNmy2AA6xgNZWkLj-TU8oPPKe1SyjVLrkNGQFl_y4XmRnU8JlFON-qakDYHWTW7eLErCNyHg0vRKRe1GdV_e6e-JGiK9x3uDABRwNLxrjdrA2KesVufBOiSOWskwhwGk_OeDE7dn5JNb79eNffkUCzeOjZs5DD2Hd0FPeKj8xLl-W2y1aANbZDKKEfNkqv001SApZMkVUhVhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاراگوئه‌ای‌ها به این شکل تیم ملیشون رو برای جام جهانی بدرقه کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/656609" target="_blank">📅 16:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656608">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/130a36096c.mp4?token=kiYnE6L-vTG5KskQUybq-LHSgyCXn78yrI5UGjOTynVg__mfzux01oTObhJ_4Ar-cBwkmzgq-nqiL6l4801izzhkRhAxw9v-pmZQ6IkY95-gqDAnjY-lPFwr3cNKVowtFIPz_o1V0xU54u7nTOAV2h7btNUH-9pBTji8ljvFvAuXqKI6Y0R8vPi9HEmpU4E7q3GioVIaoq9zdMfmcaLth0IBoUwzByZqY5klKWauDOGEk7qf_1e1wG8oz0cIBz6-49_t4KBb4_5n1C7cvmG3TVxcOMm-zOacZsK4q7Ccl2dbPjB6d4YjpnCP-Al7X9c8pOFIDkiKtCx4A_wDYitwgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/130a36096c.mp4?token=kiYnE6L-vTG5KskQUybq-LHSgyCXn78yrI5UGjOTynVg__mfzux01oTObhJ_4Ar-cBwkmzgq-nqiL6l4801izzhkRhAxw9v-pmZQ6IkY95-gqDAnjY-lPFwr3cNKVowtFIPz_o1V0xU54u7nTOAV2h7btNUH-9pBTji8ljvFvAuXqKI6Y0R8vPi9HEmpU4E7q3GioVIaoq9zdMfmcaLth0IBoUwzByZqY5klKWauDOGEk7qf_1e1wG8oz0cIBz6-49_t4KBb4_5n1C7cvmG3TVxcOMm-zOacZsK4q7Ccl2dbPjB6d4YjpnCP-Al7X9c8pOFIDkiKtCx4A_wDYitwgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترند در ترید یعنی چی؟ #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/656608" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656607">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
خودروسازان موظف به اعلام تعداد عرضه شدند/ قرعه‌کشی پابرجاست!
🔹
شورای رقابت با اصلاح دستورالعمل بازار خودرو سواری، خودروسازان را مکلف کرد اطلاعات مربوط به مشخصات خودرو، تعداد عرضه و مهلت ثبت‌نام را در تمامی طرح‌های فروش و پیش‌فروش خود منتشر کنند و در صورت بیشتر بودن تقاضا از عرضه، روش ثبت نام خودرو را از طریق قرعه‌کشی انجام دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/656607" target="_blank">📅 15:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656606">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بارونه بارونه بارونه</div>
  <div class="tg-doc-extra">کربلایی محمد فصولی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/656606" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
بارونه بارونه
#شور
🎙
کربلایی‌
#محمد_فصولی
#ولادت_امام_موسی_کاظم
(ع)
مرجع رسمی مداحی
👇
👇
@gharar_madahi</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/656606" target="_blank">📅 15:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656603">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OMmHdvnUl_aa1zEzz70X8A-55-SExETvC39sb8idTtnpATl9soTNPOjnJKKnSyeSsOLPOesqZu0m3gYBiaH1_tYuUQBYc7oxln8rAz_B9J7o87zAi71tMHEfwPfOG-WMNJo0vhqbqO57Z67zK1uUNmEr_UZ1CK8yCEUFXCgHJjzxMRmKUwb4i5UPa78EI3G172pjUPmn7EPfyCuPjrvz6s5oWF2HVYl5ymUpNAwjzXAhss-u8o5K9IJKJgOfpalWcaY7vMl3nV5idEZU3gl5d5ROMDB0YqKItcy8g2CvT776DRHFTxwZ9eLaC4aYtV-cLaTdeSp1W3Rv8Y0CFhwAPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u9G6NxJtEu_jxnSk0-XvTzYL_i_RQvvGfw3Me36OpwOD_cC3-Pf8V_xbkegnw8O312NVW-8JTaUqb5snjH7Q_7RdrlYum6bU39jER1HXtTRSGI5ItG5cWEyVwG51Hz1eur4PR3CdJG90CO9l5N3TAO-fP0FHFANcBKOmRcP5F7PzlVTXCJg465pSscgvn2Z7xCHcdNiYNz1MY9jZqefXMLhwCHc9E_LIXPeiUQnNjquuNzw0Rq893Gf4gmoK0d_YtOTOgmFAv32o0ephqex5XM4pre_bVFR8SxPJ0pYjvds9TwbU0vdqhyGu_QYUo62MI0iFQAdcyGAOQO_CgLaydQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-vCxY77WFwNcO3KYUv4P_-TyreJRSO2UPZGekhVSIl08y8fMV0c2LpvIpWwodTEbDYoWO_cjskR8N0nhaFDEouoZZD1ti7loOPPoBN3MWEgwUwJcc5ruTcBFp0aDcdkbdQCP4o8rg6U8eMJNin_35rErNTABK6AiGQ02O5orToWdDukBqK7SW5kXWKkvGTI_MU0j-sVBCfnu5zRpnnuENXP2nLtOOV8jrUDUn1kPz5N14du3xIb7_Kb0VBp3gD22cqNzvsdUZXei1qK_sLMpESlHaYT4ZBzZPw_rKIkG19GoY3xHLqHqfiC-515Tt6pUHMECUgKFZwRb3a98Fig2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری عجیب از کاخ سفید؛ آماده سازی کاخ سفید برای برگزاری مسابقات UFC
🔹
قرار است کاخ سفید روز ۲۴ خرداد میزبان شش مسابقه UFC در قالب برنامه «آزادی ۲۵٠» باشد؛ رویدادی که همزمان با تولد ۸۰ سالگی ترامپ برگزار می‌شود و برای آن سکویی بزرگ در محوطه کاخ سفید ساخته شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/656603" target="_blank">📅 15:48 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656602">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9906cfb11a.mp4?token=Z9ljtvz_5F0CIz2JPjIMTazfLWKiQQ2mNBIIf1gCGVQVs3ES0_Wo1qZbk-wRlk6Sxc-2YuT_C8XEHM-PbHKOSaB0UvBUk_xZyQ2EZ9eUK2fjJXctnM2kSHkvSFyrpqHiyJh1t_cEmuCYQPwU4X2qVEMK-cYUN8Kk7NxNF0p5145MYf8ZdRBSE7yg32E5igCjwiIrhxQ9ib0b4TV9hsuRco_8HzgrFS6wseTgz6FebA95AQVU0QygzwD9vsUBoeZNI_tXlJi3775XMdnWIEDC_mpLuRNeCZHqa2YpUUZ41u-_ufBUVRk65Kw7GdSiJ0uJN0jHoEAEZaFrcf1YuDwZj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9906cfb11a.mp4?token=Z9ljtvz_5F0CIz2JPjIMTazfLWKiQQ2mNBIIf1gCGVQVs3ES0_Wo1qZbk-wRlk6Sxc-2YuT_C8XEHM-PbHKOSaB0UvBUk_xZyQ2EZ9eUK2fjJXctnM2kSHkvSFyrpqHiyJh1t_cEmuCYQPwU4X2qVEMK-cYUN8Kk7NxNF0p5145MYf8ZdRBSE7yg32E5igCjwiIrhxQ9ib0b4TV9hsuRco_8HzgrFS6wseTgz6FebA95AQVU0QygzwD9vsUBoeZNI_tXlJi3775XMdnWIEDC_mpLuRNeCZHqa2YpUUZ41u-_ufBUVRk65Kw7GdSiJ0uJN0jHoEAEZaFrcf1YuDwZj4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تهران روی پوست تخم‌مرغ!
🔹
اعداد و ارقام این ویدئو می‌گوید تهران دارد منفجر می‌شود و باید فکری به حال آن کرد!
🔹
۲۶ نهاد متولی تصمیم‌گیری برای حریم تهران هستند اما عملا هیچ‌کدام تمرکز کنترل بحران را ندارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/656602" target="_blank">📅 15:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656600">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShtEVAIB5VwS2RTZ_DyovpScMO9rWMAshQHQJqrE_IvJ5mC40PRqFfIxXs2J-GZGL6Hvt4XEWfq2Y4NMIESrqhE03k6V5VOqF7KQWQDbZNI3r2BHXqGGsNVm3YkOPLouTU3EpfQSp7tzMVsZzY_su5crRiU1RAW2IUu-IRmogby2BaEPDO9DTfN58_skAQZkWyXWwlokOsmXeMu0Be3075lVtd6wqFepzCgY8eB6Ib1KPVtfCmR0N3czqJVAt94QUVZL_IkEHxXVocSvqOsP4CYk9CfKfwGFKzLUxpGnYtfpbBbkoY_zFnfXpBbp_XI2MbS_LGEBWR30xHQ-wcLCVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امیرحسین قیاسی: سکوتم در جنگ اشتباه بود!
🔹
حتى در صورت سكوت هم معلومه كه من مقابل كسى هستم كه بدخواه كشورمه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/656600" target="_blank">📅 15:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656598">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9yQz9I6IQ6wtbq3w3RNTAi2GbR1AfHbT3PFEnGf81g6JgOFvBs9o4Y6Tj6lICus64t_9uYHXytAIblJxvc1qY3gkH_2EPLrBPWm3yLgTpOAs3ZgOPRzZTb9jkTZQg5HSr_ZePakgtn4tWYiyhldaJoaa2jZedNsjsCGN66Oof9dfyOp4u-zzOLFGjkjhXjsA-eTqU8BHe3io01rBTJWUvtSrmtGwnegosOfQt0kaaoosny4YulwkMh57c0uEKem1MPaAyAtsKoaEONPSbrkJ-GST3yGTcYZw8_3uLd77Ih2YJLYLW3aDphVaj_1i1vPZIhymKkP_IhWhxx3DXQcbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
به جای طلا، مس بخرید!
🔹
کریس واتلینگ، مدیر یک مؤسسه تحقیقاتی مستقر در لندن، با بیان اینکه دوران «ابرچرخه صنعتی» فرا رسیده است، اعلام کرد: اکنون زمان ترجیح کالاهای صنعتی مانند مس بر کالاهای پولی مانند طلاست.
🔹
نیاز شدید به توسعه مراکز داده (دیتاسنترها) برای پردازش مدل‌های پیشرفته هوش مصنوعی، تقاضای فلزات صنعتی به ویژه مس و آلومینیوم را به سطحی بی‌سابقه می‌رساند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/akhbarefori/656598" target="_blank">📅 15:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656597">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/khr8zi-kfvpEXhi8pIKlYHLLB6zhvhVpsi2USL46zCJYlre0YwrIsE1YV_tJHK7gFR5rjFV7gH6fn_F5Tfnlb_IeGE-JdqRvmQvxM6KKdsZo3Q__dJ66x6Qnbp-Y2R3_DhqxUyCpspu4BLfvhiUtIKjILLv1vGtVLSdzUU4j4skA7u1UAEPNgOlvo3BNsR-J519EZM0365xXUG5U8PwvWVTVqS0Zkg2QdAci0v16ijzQhoM9zB_C-DTl78a1O7a4Ltgh6oYPijw2rilcrpFdPCOBDCAJ6jpELJEWerOnbEJxdi-X9YwVpNPmWLAMCSMDTojPbU1zfYnkSf-s7w3f0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درخواست عراقی‌ها در جام جهانی؛ مجوز برای پوشیدن لباس مشکی عاشورایی
🔹
فدراسیون فوتبال عراق به دلیل همزمانی بازی این تیم با سنگال در جام جهانی با شب شهادت امام حسین، از فیفا درخواست کرد مجوز پوشیدن پیراهن مشکی (لباس سوم این تیم) را برای این مسابقه صادر کند.
#جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/656597" target="_blank">📅 14:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656595">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
افزایش قیمت بنزین تکذیب شد
🔹
چندی پیش شایعاتی حاکی از افزایش قیمت بنزین منتشر شده بود که اسماعیل حسینی، سخنگوی کمیسیون انرژی در
#گفتگو
با خبرفوری بیان کرد: طبق آخرین گزارش به کمیسیون انرژی، افزایش قیمت در دستور کار نیست./خبرفوری
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/656595" target="_blank">📅 14:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656593">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گوشه هایی از مهمونی کیلومتری غدیر تهران که امسال رنگ و و بوی «بیعت» داشت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656593" target="_blank">📅 14:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656592">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1wmU7qsg16ILABlPEr7NIpV5Z-1M3R0H8qQywq8WqTlOIDStORaVdjUmjhaYMRVmFVtUiAFgJbySPkKCB3nE8VqbdXGE_gR5tYhmxHxko8ry2E4P9ApbC6u9O3zfy_j-C-qK-tsPxucJvHjjIgjytfjgHei90RkINjhF5EO13VSHMCsGJQUW1Fsik7KIkvatfCk4pvp5wwZVl2rbjl-RF_Yc0ly1zUit_Bt1YzX0z7tYvyOru6CwlxpXlCqzuNluMaBzIGzRhD0WQ474jk_6shTNgpqSBso2bwQgsiDLgrUPnATwME3hURtqMdlxW3cds-Cxqw76N0zUrtts8ICxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵ هوش مصنوعی که دارند آینده را تسخیر می‌کنند
🔹
OpenAI همه‌فن‌حریف دنیای AI؛ از مکالمه و تحلیل تا ساخت ویدیوهای خیره‌کننده.
🔹
Gemini پژوهشگری که می‌تواند ساعت‌ها تحقیق را در چند دقیقه جمع‌بندی کند.
🔹
Claude وقتی پای منطق، استدلال و مسائل پیچیده وسط باشد،…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/656592" target="_blank">📅 14:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656591">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
فقط ضروری‌ها ویزا گرفتند
🔹
وزارت امور خارجه آمریکا مدعی شد که «برای افراد ضروری» از جمله بازیکنان و کادر پشتیانی تیم ملی فوتبال ایران ویزای این کشور صادر شده است. #جام_جهانی_۲٠۲۶
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/656591" target="_blank">📅 14:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656590">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای الحدث: ایران خواستار مذاکرات سه‌ماهه درباره جزئیات پرونده هسته‌ای است.
/ انتخاب
🔹
سفیر پاکستان:
اسلام‌آباد آماده ارائه پیشنهاد برای مذاکرات ایران و آمریکا است.
🔹
سفیر چین در تهران: همه طرف ها باید به حقوق مشروع ایران در تنگه هرمز احترام بگذارند.
🔹
استانداری هرمزگان از احتمال شنیدن صدای انفجار در بندرعباس به‌مدت ۴ روز خبر داد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/656590" target="_blank">📅 14:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656589">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da218c54b4.mp4?token=SD4em33LhFbhQvWHCFlmQ9WoWvRbmdnip5aLt8PhRf0oI_z_rb6O08JAUqZax7RbEtAQenaQOFoLKaG9WOHSNUumPlK2iRytdNS0RdYLzQIFPfOvrHy8066ufJvH14mAWqA93jgoUk9SF9vc1rDKvcgbQYuQTYEvw4jWSpgH4b4oqPxCNorutL0pod1JGYNHkwTl1sNHZhtJSvhtNpY9Qga7DJkny20t9xJkxCzdse0zmsDHQnbDzbR_Q_JL2qLSPogWWuW4GE7wrlTXkPgBzM1uKrLFIddmK3fthRmEN8pIS-bxeutEJ3o4gObh5-Pc-_ke9RMU2DCmVbXcTlG9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da218c54b4.mp4?token=SD4em33LhFbhQvWHCFlmQ9WoWvRbmdnip5aLt8PhRf0oI_z_rb6O08JAUqZax7RbEtAQenaQOFoLKaG9WOHSNUumPlK2iRytdNS0RdYLzQIFPfOvrHy8066ufJvH14mAWqA93jgoUk9SF9vc1rDKvcgbQYuQTYEvw4jWSpgH4b4oqPxCNorutL0pod1JGYNHkwTl1sNHZhtJSvhtNpY9Qga7DJkny20t9xJkxCzdse0zmsDHQnbDzbR_Q_JL2qLSPogWWuW4GE7wrlTXkPgBzM1uKrLFIddmK3fthRmEN8pIS-bxeutEJ3o4gObh5-Pc-_ke9RMU2DCmVbXcTlG9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فوران آخرالزمانی یک آتشفشان در هاوایی
🔹
طبق اعلام وزارت کشور آمریکا، فعالیت این آتشفشان در ایالت هاوایی همچنان ادامه دارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/656589" target="_blank">📅 14:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656588">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/055f3b54ae.mp4?token=Qu6Ruc-mhxF_2TDPQa2dqGwUt6KOap3oNyLPpfBYtlj_FEtLRFuCEdfSRj7f3ithH2PS0zjIaSbIe3HpTqKdidvvXiPUi1GWgVF-jX-fKLPgyz8Dk5MT2DZn8DCmUhccUAKDfaXRXdgbJO51zUMlLCrBaUY9UCvNyuao997Y4x5xImC1Rx7Nut_jBKOAalDLukXiV8EO93IKagcZ1OE6YvDEZr0JvDfpQ8I_6xdogOC72TeDoyzqAigfU4ie6hVvf6k1KJ4hOyrKrbGrx95K1yxy97jnLfMjdaQNB_O8NK9-tQ0FG4Wq1M5nGftAl27g4pjmmse5eLqzoxdYBP3MCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/055f3b54ae.mp4?token=Qu6Ruc-mhxF_2TDPQa2dqGwUt6KOap3oNyLPpfBYtlj_FEtLRFuCEdfSRj7f3ithH2PS0zjIaSbIe3HpTqKdidvvXiPUi1GWgVF-jX-fKLPgyz8Dk5MT2DZn8DCmUhccUAKDfaXRXdgbJO51zUMlLCrBaUY9UCvNyuao997Y4x5xImC1Rx7Nut_jBKOAalDLukXiV8EO93IKagcZ1OE6YvDEZr0JvDfpQ8I_6xdogOC72TeDoyzqAigfU4ie6hVvf6k1KJ4hOyrKrbGrx95K1yxy97jnLfMjdaQNB_O8NK9-tQ0FG4Wq1M5nGftAl27g4pjmmse5eLqzoxdYBP3MCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ننگ بر آنکه خواسته شمر به ما کمک کند #ایران_من
🇮🇷
✊
@AkhbareFori | khabarfoori.com</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/656588" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656587">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
افزایش ۲۱ درصدی کرایه حمل‌ونقل عمومی جاده‌ای از ۱۶ خرداد ‌
🔹
بر اساس این ابلاغیه، نرخ‌های جدید شامل تمامی مسیر‌ها و ناوگان مسافری اعم از اتوبوس، میدل‌باس، مینی‌بوس، ون و سواری کرایه خواهد شد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/656587" target="_blank">📅 13:58 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656585">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
تیزر قسمت هشتم از فصل چهارم
🔹
در این قسمت روایت ۲ تجربه نزدیک به مرگ سرکار خانم فاطمه سجادی که به خاطر مسائلی در زندگی از دنیا دل بریده و در شبی که ماه کامل می شود روح از بدن جدا شده و به آسمان بیکران رفته و تجربیاتی را از عالم غیر ماده را درک می کند را نظاره می کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: فاطمه سجادی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/656585" target="_blank">📅 13:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656583">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U_fa5nLg9eTlh1yy2Y1YSqU39B61XWyd2mE8Qlk_63JEVxotxSv217PfZhNslZm9N2r1xZBbzG2X-AefPXHkgFCS_wNYEH5yYDQ6VjCL4zrVwTEZyWpt87VAp56OsMITfEEto2TBbqiUDEnBnl4OWcq230CdueMPzkCNMithHAG40RxKv3OWvqcZOiBr0m3wPBDKn_rxvt8diToEK8YsGKjqijh0G-Ily_jfhvavGZSRrAI7l6Y32FZHThIH_lCawUwU8nRPB046QkBuO0sAVhlQfc2snvTPAZgtl7hQAH1ue-e7zfYG2ruXzb3oMm6bHhZeX1ILJxtEjIl7bcTdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نصف حقابه ایران از طالبان نقد شد
🔹
۴۱۷ میلیون مترمکعب آب از افغانستان به چاه‌نیمه‌های ایران رسیده که کمتر از نصف حقابه سالانه است. طبق معاهده هیرمند (۱۳۵۳)، در سال‌های نرمال باید ۸۵۰ میلیون مترمکعب آب تحویل شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/656583" target="_blank">📅 13:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656582">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJpZRQ7c0XPzc7tFYtHA2Tn9g_ri4usS6dX1ySrDau49suLd6Jk6HzlwV_MHSd2Ng0YLVS0eX3OIOf4C-ABNjFwP0dSyLXJp5hf0ZWD3Cef7ZOs8xLHRl9zaTHFqH6yF22rlZLIlMRQ_t1NP-8bXcmEazEOfLv6BsAmg3coJEuGe5xbkpxQumsjB50QQCJ-0tQjJ47Arl_ESyGXBYoMhD6bRV8bC89nXz1EbV6HFbhazctZiQBRosCU2D0e4DpKHPeOfuipHdReJt-sueXjqlzkjQcQ5scFid63Z5sDTbt12IrK2Z_9v2LXGRFIGg9qCHDiapPtXQXFB_IWydjsq8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔷
بانک اقتصادنوین در جمع سالم‌ترین بانک‌های کشور
🔸
بررسی شاخص بین‌المللی CAMELS، معتبرترین مدل سنجش سلامت و پایداری بانک‌ها، نشان می‌دهد بانک اقتصادنوین موفق شده رتبه سوم بانک‌های بورسی کشور را از منظر سلامت مالی کسب کند.
🔸
این موفقیت بیانگر عملکرد فوق‌العاده بانک در حوزه مدیریت سرمایه، کنترل ریسک و تقویت ثبات مالی است.
🔸
همچنین نسبت کفایت سرمایه بانک اقتصادنوین به ۱۰.۵۵ درصد رسیده؛ رقمی بالاتر از حداقل استاندارد ۸ درصدی بانک مرکزی.
🔸
قرار گرفتن اقتصادنوین در میان سه بانک برتر کشور بر اساس شاخص CAMELS، نشان‌دهنده پیشروی این بانک در مسیر استانداردهای نوین بانکداری و تقویت اعتماد سپرده‌گذاران، سهامداران و فعالان بازار سرمایه است.</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/656582" target="_blank">📅 13:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656580">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آخرین وضعیت ۲ دختر سنندجی که در توالت حبس شده بودند
سلمان حسینی، رییس اورژانس اجتماعی کشور در
#گفتگو
با خبر فوری:
🔹
همکاران ما در سنندج به محض اطلاع از این قضیه از طریق همکاران محترم‌مان در فراجا مداخلات تخصصی لازم را انجام دادند. درحال حاضر خواهر بزرگتر بابت انجام کارهای درمانی در بیمارستان است و خواهر کوچکتر در یکی از مراکز بهزیستی است.
🔹
در خصوص واگذاری این دو کودک به مادر خود، بعد از بررسی‌های مددکاری و روانشناختی این روند طی می‌شود و بر اساس قوانین مربوطه اقدام لازم صورت می‌گیرد. درحال حاضر روند واگذاری سرپرستی این دو کودک به مادر خود مشخص نیست.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/656580" target="_blank">📅 13:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656578">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c900f1da4e.mp4?token=LDFTfNw7q5sVxrNbWvNMM_TU89OH3w2iup22YZiRbURjqXGll6juZvjXcOO-aZCtk3kZjGjw8raoz4rZBNwqbdpG1RXKESkFt0GtnWB2LlwSJAyp0wG8CT45WhSQTbSZt33Ve81keFAS4oIXscR5a-j3WuoptrjS61LzTtygga8GX_IFpIhxEeGwimPCY79DeMpOgxnB7CkDd1blX1dztLvDJpoEhLbjSHDOD7krFF1Nrwe8FheDLqtIRv9zFcrsTPFeLsoZRzDKhECD7QlLeCmN_6m2MhJfcMTD6g7nR5U1CUu70MOJf5N9OO6EYsRayRhgkHwph705P49xl5TLpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c900f1da4e.mp4?token=LDFTfNw7q5sVxrNbWvNMM_TU89OH3w2iup22YZiRbURjqXGll6juZvjXcOO-aZCtk3kZjGjw8raoz4rZBNwqbdpG1RXKESkFt0GtnWB2LlwSJAyp0wG8CT45WhSQTbSZt33Ve81keFAS4oIXscR5a-j3WuoptrjS61LzTtygga8GX_IFpIhxEeGwimPCY79DeMpOgxnB7CkDd1blX1dztLvDJpoEhLbjSHDOD7krFF1Nrwe8FheDLqtIRv9zFcrsTPFeLsoZRzDKhECD7QlLeCmN_6m2MhJfcMTD6g7nR5U1CUu70MOJf5N9OO6EYsRayRhgkHwph705P49xl5TLpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لازانیا با سس بشامل
🔹
لازانیا یک غذای خوشمزه و دل‌چسب است که با لایه‌های نرم و سس بشامل خامه‌ای، همراه با مواد گوشتی و قارچ، تجربه‌ای لذیذ را برای شما به ارمغان می‌آورد.
🔹
این دستور می‌تواند دل هر کسی را به دست بیاورد و عاشق لازانیا شود!
#آشپزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/656578" target="_blank">📅 13:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-656576">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
مرغ تازه؛ کیلویی ۳۵۰ هزار تومان
🔹
قیمت مرغ تازه در میادین و بازارهای میوه و تره بار، بسته‌بندی کیسه‌ای( پوشش کیسه نایلونی) کیلویی ۳۵۰ هزار تومان است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/akhbarefori/656576" target="_blank">📅 12:53 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
